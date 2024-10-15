# SNMP MIB module (Fore-Switch-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-Switch-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:50 2024
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

(ipFilterStatsIfName,
 ipFilterStatsVCI,
 ipFilterStatsVPI) = mibBuilder.importSymbols(
    "Fore-Adapter-MIB",
    "ipFilterStatsIfName",
    "ipFilterStatsVCI",
    "ipFilterStatsVPI")

(crMemoryAllocated,
 crXfrIndex,
 crXfrPrimaryTrapStatus,
 crXfrSecondaryTrapStatus) = mibBuilder.importSymbols(
    "Fore-Callrecord-MIB",
    "crMemoryAllocated",
    "crXfrIndex",
    "crXfrPrimaryTrapStatus",
    "crXfrSecondaryTrapStatus")

(AtmSigProtocol,
 ConnectionType,
 EntryStatus,
 GeneralState,
 IntegerBitString,
 NsapAddr,
 NsapPrefix,
 SpansAddress,
 TransitNetwork,
 asx,
 asxd,
 atmSwitch,
 hardware,
 software,
 systems) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "AtmSigProtocol",
    "ConnectionType",
    "EntryStatus",
    "GeneralState",
    "IntegerBitString",
    "NsapAddr",
    "NsapPrefix",
    "SpansAddress",
    "TransitNetwork",
    "asx",
    "asxd",
    "atmSwitch",
    "hardware",
    "software",
    "systems")

(trapLogIndex,) = mibBuilder.importSymbols(
    "Fore-TrapLog-MIB",
    "trapLogIndex")

(hrSystemDate,) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "hrSystemDate")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(pnniNodeId,) = mibBuilder.importSymbols(
    "PNNI-MIB",
    "pnniNodeId")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TimeStamp")


# MODULE-IDENTITY

foreSwitchModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class E164Address(OctetString, TextualConvention):
    status = "current"
    displayHint = "15a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )



class AtmConnSchedMode(Integer32, TextualConvention):
    status = "current"
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
        *(("default", 1),
          ("guaranteed", 4),
          ("roundrobin", 2),
          ("smoothed", 3))
    )



class AtmOrigPathSchedMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flat", 1),
          ("shaped", 2),
          ("shaped-roundrobin", 3))
    )



class AAL5CountingMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cell-counting", 2),
          ("default", 1),
          ("packet-counting", 3))
    )



# MIB Managed Objects in the order of their OIDs

_BoardGroup_ObjectIdentity = ObjectIdentity
boardGroup = _BoardGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1)
)
_BoardTable_Object = MibTable
boardTable = _BoardTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    boardTable.setStatus("current")
_BoardEntry_Object = MibTableRow
boardEntry = _BoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 1, 1)
)
boardEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "boardIndex"),
)
if mibBuilder.loadTexts:
    boardEntry.setStatus("current")
_BoardIndex_Type = Integer32
_BoardIndex_Object = MibTableColumn
boardIndex = _BoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 1, 1, 1),
    _BoardIndex_Type()
)
boardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardIndex.setStatus("current")
_BoardVersion_Type = Integer32
_BoardVersion_Object = MibTableColumn
boardVersion = _BoardVersion_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 1, 1, 2),
    _BoardVersion_Type()
)
boardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardVersion.setStatus("current")


class _BoardModel_Type(Integer32):
    """Custom type boardModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("asx100", 1),
          ("asx1000", 8),
          ("asx1200", 17),
          ("asx150", 22),
          ("asx200", 2),
          ("asx200bx", 5),
          ("asx200bxe", 6),
          ("asx200wg", 4),
          ("asx4000", 18),
          ("cabletron9A000", 7),
          ("esx3000", 20),
          ("le155", 9),
          ("le25", 19),
          ("sfcs1000", 12),
          ("sfcs200bx", 11),
          ("sfcs200wg", 10),
          ("tnx1100", 16),
          ("tnx1100b", 21),
          ("tnx210", 15),
          ("unknown", 0))
    )


_BoardModel_Type.__name__ = "Integer32"
_BoardModel_Object = MibTableColumn
boardModel = _BoardModel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 1, 1, 3),
    _BoardModel_Type()
)
boardModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardModel.setStatus("current")
_BoardSerialNumber_Type = Integer32
_BoardSerialNumber_Object = MibTableColumn
boardSerialNumber = _BoardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 1, 1, 4),
    _BoardSerialNumber_Type()
)
boardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardSerialNumber.setStatus("current")
_NumberOfModules_Type = Integer32
_NumberOfModules_Object = MibTableColumn
numberOfModules = _NumberOfModules_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 1, 1, 5),
    _NumberOfModules_Type()
)
numberOfModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfModules.setStatus("current")
_VpiLookupErrors_Type = Counter32
_VpiLookupErrors_Object = MibTableColumn
vpiLookupErrors = _VpiLookupErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 1, 1, 6),
    _VpiLookupErrors_Type()
)
vpiLookupErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpiLookupErrors.setStatus("obsolete")
_VciLookupErrors_Type = Counter32
_VciLookupErrors_Object = MibTableColumn
vciLookupErrors = _VciLookupErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 1, 1, 7),
    _VciLookupErrors_Type()
)
vciLookupErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vciLookupErrors.setStatus("obsolete")
_BoardControlPort_Type = Integer32
_BoardControlPort_Object = MibTableColumn
boardControlPort = _BoardControlPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 1, 1, 8),
    _BoardControlPort_Type()
)
boardControlPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardControlPort.setStatus("current")
_BoardHDCOMPAsicVersion_Type = Integer32
_BoardHDCOMPAsicVersion_Object = MibTableColumn
boardHDCOMPAsicVersion = _BoardHDCOMPAsicVersion_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 1, 1, 9),
    _BoardHDCOMPAsicVersion_Type()
)
boardHDCOMPAsicVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardHDCOMPAsicVersion.setStatus("obsolete")
_BoardMcastSpaceIndex_Type = Integer32
_BoardMcastSpaceIndex_Object = MibTableColumn
boardMcastSpaceIndex = _BoardMcastSpaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 1, 1, 10),
    _BoardMcastSpaceIndex_Type()
)
boardMcastSpaceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardMcastSpaceIndex.setStatus("current")
_NumberOfBoards_Type = Integer32
_NumberOfBoards_Object = MibScalar
numberOfBoards = _NumberOfBoards_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 2),
    _NumberOfBoards_Type()
)
numberOfBoards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfBoards.setStatus("current")
_Utilization_ObjectIdentity = ObjectIdentity
utilization = _Utilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3)
)
_ProcUtilGroup_ObjectIdentity = ObjectIdentity
procUtilGroup = _ProcUtilGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 1)
)
_ProcUtilLastUpdate_Type = TimeTicks
_ProcUtilLastUpdate_Object = MibScalar
procUtilLastUpdate = _ProcUtilLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 1, 1),
    _ProcUtilLastUpdate_Type()
)
procUtilLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procUtilLastUpdate.setStatus("current")


class _ProcUtilValue_Type(Gauge32):
    """Custom type procUtilValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ProcUtilValue_Type.__name__ = "Gauge32"
_ProcUtilValue_Object = MibScalar
procUtilValue = _ProcUtilValue_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 1, 2),
    _ProcUtilValue_Type()
)
procUtilValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procUtilValue.setStatus("current")


class _ProcUtilMonInterval_Type(Integer32):
    """Custom type procUtilMonInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 6000),
    )


_ProcUtilMonInterval_Type.__name__ = "Integer32"
_ProcUtilMonInterval_Object = MibScalar
procUtilMonInterval = _ProcUtilMonInterval_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 1, 3),
    _ProcUtilMonInterval_Type()
)
procUtilMonInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    procUtilMonInterval.setStatus("current")


class _ProcUtilMinLoad_Type(Gauge32):
    """Custom type procUtilMinLoad based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ProcUtilMinLoad_Type.__name__ = "Gauge32"
_ProcUtilMinLoad_Object = MibScalar
procUtilMinLoad = _ProcUtilMinLoad_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 1, 4),
    _ProcUtilMinLoad_Type()
)
procUtilMinLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procUtilMinLoad.setStatus("current")
_ProcUtilMinLoadLastUpdate_Type = TimeTicks
_ProcUtilMinLoadLastUpdate_Object = MibScalar
procUtilMinLoadLastUpdate = _ProcUtilMinLoadLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 1, 5),
    _ProcUtilMinLoadLastUpdate_Type()
)
procUtilMinLoadLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procUtilMinLoadLastUpdate.setStatus("current")


class _ProcUtilMaxLoad_Type(Gauge32):
    """Custom type procUtilMaxLoad based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ProcUtilMaxLoad_Type.__name__ = "Gauge32"
_ProcUtilMaxLoad_Object = MibScalar
procUtilMaxLoad = _ProcUtilMaxLoad_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 1, 6),
    _ProcUtilMaxLoad_Type()
)
procUtilMaxLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procUtilMaxLoad.setStatus("current")
_ProcUtilMaxLoadLastUpdate_Type = TimeTicks
_ProcUtilMaxLoadLastUpdate_Object = MibScalar
procUtilMaxLoadLastUpdate = _ProcUtilMaxLoadLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 1, 7),
    _ProcUtilMaxLoadLastUpdate_Type()
)
procUtilMaxLoadLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procUtilMaxLoadLastUpdate.setStatus("current")


class _ProcUtilHistoryReset_Type(Integer32):
    """Custom type procUtilHistoryReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_ProcUtilHistoryReset_Type.__name__ = "Integer32"
_ProcUtilHistoryReset_Object = MibScalar
procUtilHistoryReset = _ProcUtilHistoryReset_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 1, 8),
    _ProcUtilHistoryReset_Type()
)
procUtilHistoryReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    procUtilHistoryReset.setStatus("current")
_ProcUtilsNumMallocPart_Type = Integer32
_ProcUtilsNumMallocPart_Object = MibScalar
procUtilsNumMallocPart = _ProcUtilsNumMallocPart_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 1, 9),
    _ProcUtilsNumMallocPart_Type()
)
procUtilsNumMallocPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procUtilsNumMallocPart.setStatus("current")
_ProcUtilsSystemPartitionID_Type = Integer32
_ProcUtilsSystemPartitionID_Object = MibScalar
procUtilsSystemPartitionID = _ProcUtilsSystemPartitionID_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 1, 10),
    _ProcUtilsSystemPartitionID_Type()
)
procUtilsSystemPartitionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procUtilsSystemPartitionID.setStatus("current")
_MallocUtilTable_Object = MibTable
mallocUtilTable = _MallocUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    mallocUtilTable.setStatus("current")
_MallocUtilEntry_Object = MibTableRow
mallocUtilEntry = _MallocUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 2, 1)
)
mallocUtilEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "mallocPartId"),
)
if mibBuilder.loadTexts:
    mallocUtilEntry.setStatus("current")
_MallocPartId_Type = Integer32
_MallocPartId_Object = MibTableColumn
mallocPartId = _MallocPartId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 2, 1, 1),
    _MallocPartId_Type()
)
mallocPartId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mallocPartId.setStatus("current")
_NumBytesFree_Type = Integer32
_NumBytesFree_Object = MibTableColumn
numBytesFree = _NumBytesFree_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 2, 1, 2),
    _NumBytesFree_Type()
)
numBytesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBytesFree.setStatus("current")
_NumBlocksFree_Type = Integer32
_NumBlocksFree_Object = MibTableColumn
numBlocksFree = _NumBlocksFree_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 2, 1, 3),
    _NumBlocksFree_Type()
)
numBlocksFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBlocksFree.setStatus("current")
_MaxBlockSizeFree_Type = Integer32
_MaxBlockSizeFree_Object = MibTableColumn
maxBlockSizeFree = _MaxBlockSizeFree_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 2, 1, 4),
    _MaxBlockSizeFree_Type()
)
maxBlockSizeFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxBlockSizeFree.setStatus("current")
_NumBytesAlloc_Type = Integer32
_NumBytesAlloc_Object = MibTableColumn
numBytesAlloc = _NumBytesAlloc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 2, 1, 5),
    _NumBytesAlloc_Type()
)
numBytesAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBytesAlloc.setStatus("current")
_NumBlocksAlloc_Type = Integer32
_NumBlocksAlloc_Object = MibTableColumn
numBlocksAlloc = _NumBlocksAlloc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 2, 1, 6),
    _NumBlocksAlloc_Type()
)
numBlocksAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBlocksAlloc.setStatus("current")
_MbufUtilGroup_ObjectIdentity = ObjectIdentity
mbufUtilGroup = _MbufUtilGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 3)
)
_MbufsCount_Type = Integer32
_MbufsCount_Object = MibScalar
mbufsCount = _MbufsCount_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 3, 1),
    _MbufsCount_Type()
)
mbufsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbufsCount.setStatus("current")
_MbufsClusters_Type = Integer32
_MbufsClusters_Object = MibScalar
mbufsClusters = _MbufsClusters_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 3, 2),
    _MbufsClusters_Type()
)
mbufsClusters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbufsClusters.setStatus("current")
_MbufsSpace_Type = Integer32
_MbufsSpace_Object = MibScalar
mbufsSpace = _MbufsSpace_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 3, 3),
    _MbufsSpace_Type()
)
mbufsSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbufsSpace.setStatus("current")
_MbufsClFree_Type = Integer32
_MbufsClFree_Object = MibScalar
mbufsClFree = _MbufsClFree_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 3, 4),
    _MbufsClFree_Type()
)
mbufsClFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbufsClFree.setStatus("current")
_MbufsDrops_Type = Integer32
_MbufsDrops_Object = MibScalar
mbufsDrops = _MbufsDrops_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 3, 5),
    _MbufsDrops_Type()
)
mbufsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbufsDrops.setStatus("current")
_MbufsWait_Type = Integer32
_MbufsWait_Object = MibScalar
mbufsWait = _MbufsWait_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 3, 6),
    _MbufsWait_Type()
)
mbufsWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbufsWait.setStatus("current")
_MbufsDrain_Type = Integer32
_MbufsDrain_Object = MibScalar
mbufsDrain = _MbufsDrain_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 3, 7),
    _MbufsDrain_Type()
)
mbufsDrain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbufsDrain.setStatus("current")
_MbufsFreeAlloc_Type = Integer32
_MbufsFreeAlloc_Object = MibScalar
mbufsFreeAlloc = _MbufsFreeAlloc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 3, 8),
    _MbufsFreeAlloc_Type()
)
mbufsFreeAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbufsFreeAlloc.setStatus("current")
_MbufsDataFreeAlloc_Type = Integer32
_MbufsDataFreeAlloc_Object = MibScalar
mbufsDataFreeAlloc = _MbufsDataFreeAlloc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 3, 9),
    _MbufsDataFreeAlloc_Type()
)
mbufsDataFreeAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbufsDataFreeAlloc.setStatus("current")
_MbufsHeaderAlloc_Type = Integer32
_MbufsHeaderAlloc_Object = MibScalar
mbufsHeaderAlloc = _MbufsHeaderAlloc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 3, 10),
    _MbufsHeaderAlloc_Type()
)
mbufsHeaderAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbufsHeaderAlloc.setStatus("current")
_MbufsSocketAlloc_Type = Integer32
_MbufsSocketAlloc_Object = MibScalar
mbufsSocketAlloc = _MbufsSocketAlloc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 3, 11),
    _MbufsSocketAlloc_Type()
)
mbufsSocketAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbufsSocketAlloc.setStatus("current")
_MbufsPcbAlloc_Type = Integer32
_MbufsPcbAlloc_Object = MibScalar
mbufsPcbAlloc = _MbufsPcbAlloc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 3, 12),
    _MbufsPcbAlloc_Type()
)
mbufsPcbAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbufsPcbAlloc.setStatus("current")
_MbufsRtableAlloc_Type = Integer32
_MbufsRtableAlloc_Object = MibScalar
mbufsRtableAlloc = _MbufsRtableAlloc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 3, 13),
    _MbufsRtableAlloc_Type()
)
mbufsRtableAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbufsRtableAlloc.setStatus("current")
_MbufsHtableAlloc_Type = Integer32
_MbufsHtableAlloc_Object = MibScalar
mbufsHtableAlloc = _MbufsHtableAlloc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 3, 14),
    _MbufsHtableAlloc_Type()
)
mbufsHtableAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbufsHtableAlloc.setStatus("current")
_MbufsAtableAlloc_Type = Integer32
_MbufsAtableAlloc_Object = MibScalar
mbufsAtableAlloc = _MbufsAtableAlloc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 3, 15),
    _MbufsAtableAlloc_Type()
)
mbufsAtableAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbufsAtableAlloc.setStatus("current")
_MbufsSoNameAlloc_Type = Integer32
_MbufsSoNameAlloc_Object = MibScalar
mbufsSoNameAlloc = _MbufsSoNameAlloc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 3, 16),
    _MbufsSoNameAlloc_Type()
)
mbufsSoNameAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbufsSoNameAlloc.setStatus("current")
_MbufsZombieAlloc_Type = Integer32
_MbufsZombieAlloc_Object = MibScalar
mbufsZombieAlloc = _MbufsZombieAlloc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 3, 17),
    _MbufsZombieAlloc_Type()
)
mbufsZombieAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbufsZombieAlloc.setStatus("current")
_MbufsSoOptsAlloc_Type = Integer32
_MbufsSoOptsAlloc_Object = MibScalar
mbufsSoOptsAlloc = _MbufsSoOptsAlloc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 3, 18),
    _MbufsSoOptsAlloc_Type()
)
mbufsSoOptsAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbufsSoOptsAlloc.setStatus("current")
_MbufsFtableAlloc_Type = Integer32
_MbufsFtableAlloc_Object = MibScalar
mbufsFtableAlloc = _MbufsFtableAlloc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 3, 19),
    _MbufsFtableAlloc_Type()
)
mbufsFtableAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbufsFtableAlloc.setStatus("current")
_MbufsRightsAlloc_Type = Integer32
_MbufsRightsAlloc_Object = MibScalar
mbufsRightsAlloc = _MbufsRightsAlloc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 3, 20),
    _MbufsRightsAlloc_Type()
)
mbufsRightsAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbufsRightsAlloc.setStatus("current")
_MbufsIFaddrAlloc_Type = Integer32
_MbufsIFaddrAlloc_Object = MibScalar
mbufsIFaddrAlloc = _MbufsIFaddrAlloc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 3, 3, 21),
    _MbufsIFaddrAlloc_Type()
)
mbufsIFaddrAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbufsIFaddrAlloc.setStatus("current")
_BoardStatsTable_Object = MibTable
boardStatsTable = _BoardStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    boardStatsTable.setStatus("current")
_BoardStatsEntry_Object = MibTableRow
boardStatsEntry = _BoardStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 4, 1)
)
boardStatsEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "boardStatsBoard"),
    (0, "Fore-Switch-MIB", "boardStatsIndex"),
)
if mibBuilder.loadTexts:
    boardStatsEntry.setStatus("current")
_BoardStatsBoard_Type = Integer32
_BoardStatsBoard_Object = MibTableColumn
boardStatsBoard = _BoardStatsBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 4, 1, 1),
    _BoardStatsBoard_Type()
)
boardStatsBoard.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    boardStatsBoard.setStatus("current")
_BoardStatsIndex_Type = Integer32
_BoardStatsIndex_Object = MibTableColumn
boardStatsIndex = _BoardStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 4, 1, 2),
    _BoardStatsIndex_Type()
)
boardStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    boardStatsIndex.setStatus("current")
_BoardStatsName_Type = DisplayString
_BoardStatsName_Object = MibTableColumn
boardStatsName = _BoardStatsName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 4, 1, 3),
    _BoardStatsName_Type()
)
boardStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardStatsName.setStatus("current")
_BoardStatsValue_Type = Gauge32
_BoardStatsValue_Object = MibTableColumn
boardStatsValue = _BoardStatsValue_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 4, 1, 4),
    _BoardStatsValue_Type()
)
boardStatsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardStatsValue.setStatus("current")
_PortCardGroup_ObjectIdentity = ObjectIdentity
portCardGroup = _PortCardGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 5)
)
_PortCardTable_Object = MibTable
portCardTable = _PortCardTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    portCardTable.setStatus("current")
_PortCardEntry_Object = MibTableRow
portCardEntry = _PortCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 5, 1, 1)
)
portCardEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "portCardIndex"),
)
if mibBuilder.loadTexts:
    portCardEntry.setStatus("current")
_PortCardIndex_Type = Integer32
_PortCardIndex_Object = MibTableColumn
portCardIndex = _PortCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 5, 1, 1, 1),
    _PortCardIndex_Type()
)
portCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portCardIndex.setStatus("current")
_PortCardName_Type = DisplayString
_PortCardName_Object = MibTableColumn
portCardName = _PortCardName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 5, 1, 1, 2),
    _PortCardName_Type()
)
portCardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCardName.setStatus("current")
_PortCardFlavor_Type = DisplayString
_PortCardFlavor_Object = MibTableColumn
portCardFlavor = _PortCardFlavor_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 5, 1, 1, 3),
    _PortCardFlavor_Type()
)
portCardFlavor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCardFlavor.setStatus("current")
_PortCardType_Type = DisplayString
_PortCardType_Object = MibTableColumn
portCardType = _PortCardType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 5, 1, 1, 4),
    _PortCardType_Type()
)
portCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCardType.setStatus("current")
_PortCardUptime_Type = TimeTicks
_PortCardUptime_Object = MibTableColumn
portCardUptime = _PortCardUptime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 5, 1, 1, 5),
    _PortCardUptime_Type()
)
portCardUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCardUptime.setStatus("current")
_PortCardSerialNumber_Type = DisplayString
_PortCardSerialNumber_Object = MibTableColumn
portCardSerialNumber = _PortCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 5, 1, 1, 6),
    _PortCardSerialNumber_Type()
)
portCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCardSerialNumber.setStatus("current")
_PortCardAssemblyRevision_Type = Integer32
_PortCardAssemblyRevision_Object = MibTableColumn
portCardAssemblyRevision = _PortCardAssemblyRevision_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 5, 1, 1, 7),
    _PortCardAssemblyRevision_Type()
)
portCardAssemblyRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCardAssemblyRevision.setStatus("current")
_PortCardHardwareConf_Type = Integer32
_PortCardHardwareConf_Object = MibTableColumn
portCardHardwareConf = _PortCardHardwareConf_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 5, 1, 1, 8),
    _PortCardHardwareConf_Type()
)
portCardHardwareConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCardHardwareConf.setStatus("current")


class _PortCardState_Type(Integer32):
    """Custom type portCardState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inService", 2),
          ("outOfService", 3),
          ("reset", 1))
    )


_PortCardState_Type.__name__ = "Integer32"
_PortCardState_Object = MibTableColumn
portCardState = _PortCardState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 5, 1, 1, 9),
    _PortCardState_Type()
)
portCardState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCardState.setStatus("current")
_BoardTrafficManagementGroup_ObjectIdentity = ObjectIdentity
boardTrafficManagementGroup = _BoardTrafficManagementGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 6)
)
_BoardTrafficManagementPerPriorityTable_Object = MibTable
boardTrafficManagementPerPriorityTable = _BoardTrafficManagementPerPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    boardTrafficManagementPerPriorityTable.setStatus("current")
_BoardTrafficManagementPerPriorityEntry_Object = MibTableRow
boardTrafficManagementPerPriorityEntry = _BoardTrafficManagementPerPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 6, 1, 1)
)
boardTrafficManagementPerPriorityEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "btmPerPriorityBoard"),
    (0, "Fore-Switch-MIB", "btmPerPriorityPriority"),
    (0, "Fore-Switch-MIB", "btmPerPriorityFeature"),
)
if mibBuilder.loadTexts:
    boardTrafficManagementPerPriorityEntry.setStatus("current")
_BtmPerPriorityBoard_Type = Integer32
_BtmPerPriorityBoard_Object = MibTableColumn
btmPerPriorityBoard = _BtmPerPriorityBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 6, 1, 1, 1),
    _BtmPerPriorityBoard_Type()
)
btmPerPriorityBoard.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    btmPerPriorityBoard.setStatus("current")
_BtmPerPriorityPriority_Type = Integer32
_BtmPerPriorityPriority_Object = MibTableColumn
btmPerPriorityPriority = _BtmPerPriorityPriority_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 6, 1, 1, 2),
    _BtmPerPriorityPriority_Type()
)
btmPerPriorityPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    btmPerPriorityPriority.setStatus("current")
_BtmPerPriorityFeature_Type = Integer32
_BtmPerPriorityFeature_Object = MibTableColumn
btmPerPriorityFeature = _BtmPerPriorityFeature_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 6, 1, 1, 3),
    _BtmPerPriorityFeature_Type()
)
btmPerPriorityFeature.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    btmPerPriorityFeature.setStatus("current")
_BtmPerPriorityPriorityName_Type = DisplayString
_BtmPerPriorityPriorityName_Object = MibTableColumn
btmPerPriorityPriorityName = _BtmPerPriorityPriorityName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 6, 1, 1, 4),
    _BtmPerPriorityPriorityName_Type()
)
btmPerPriorityPriorityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmPerPriorityPriorityName.setStatus("current")
_BtmPerPriorityValue_Type = Integer32
_BtmPerPriorityValue_Object = MibTableColumn
btmPerPriorityValue = _BtmPerPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 1, 6, 1, 1, 5),
    _BtmPerPriorityValue_Type()
)
btmPerPriorityValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btmPerPriorityValue.setStatus("current")
_ModuleGroup_ObjectIdentity = ObjectIdentity
moduleGroup = _ModuleGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2)
)
_ModuleTable_Object = MibTable
moduleTable = _ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    moduleTable.setStatus("current")
_ModuleEntry_Object = MibTableRow
moduleEntry = _ModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 1, 1)
)
moduleEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "moduleBoard"),
    (0, "Fore-Switch-MIB", "moduleNumber"),
)
if mibBuilder.loadTexts:
    moduleEntry.setStatus("current")
_ModuleBoard_Type = Integer32
_ModuleBoard_Object = MibTableColumn
moduleBoard = _ModuleBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 1, 1, 1),
    _ModuleBoard_Type()
)
moduleBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBoard.setStatus("current")
_ModuleNumber_Type = Integer32
_ModuleNumber_Object = MibTableColumn
moduleNumber = _ModuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 1, 1, 2),
    _ModuleNumber_Type()
)
moduleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleNumber.setStatus("current")


class _ModuleName_Type(DisplayString):
    """Custom type moduleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ModuleName_Type.__name__ = "DisplayString"
_ModuleName_Object = MibTableColumn
moduleName = _ModuleName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 1, 1, 3),
    _ModuleName_Type()
)
moduleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleName.setStatus("current")
_ModuleSpeed_Type = Unsigned32
_ModuleSpeed_Object = MibTableColumn
moduleSpeed = _ModuleSpeed_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 1, 1, 4),
    _ModuleSpeed_Type()
)
moduleSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSpeed.setStatus("current")
_ModuleNumberOfPorts_Type = Integer32
_ModuleNumberOfPorts_Object = MibTableColumn
moduleNumberOfPorts = _ModuleNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 1, 1, 5),
    _ModuleNumberOfPorts_Type()
)
moduleNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleNumberOfPorts.setStatus("current")
_ModuleUptime_Type = TimeTicks
_ModuleUptime_Object = MibTableColumn
moduleUptime = _ModuleUptime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 1, 1, 6),
    _ModuleUptime_Type()
)
moduleUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleUptime.setStatus("current")
_ModuleHwMajorRev_Type = Integer32
_ModuleHwMajorRev_Object = MibTableColumn
moduleHwMajorRev = _ModuleHwMajorRev_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 1, 1, 7),
    _ModuleHwMajorRev_Type()
)
moduleHwMajorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleHwMajorRev.setStatus("current")
_ModuleHwMinorRev_Type = Integer32
_ModuleHwMinorRev_Object = MibTableColumn
moduleHwMinorRev = _ModuleHwMinorRev_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 1, 1, 8),
    _ModuleHwMinorRev_Type()
)
moduleHwMinorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleHwMinorRev.setStatus("current")


class _ModuleVersion_Type(Integer32):
    """Custom type moduleVersion based on Integer32"""
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
              10,
              11,
              67)
        )
    )
    namedValues = NamedValues(
        *(("generationA", 1),
          ("generationB", 2),
          ("generationC", 3),
          ("generationC2", 67),
          ("generationD", 6),
          ("generationE", 10),
          ("generationLC", 4),
          ("generationLE", 5),
          ("generationPC1", 7),
          ("generationPC2", 8),
          ("generationPCF1", 11))
    )


_ModuleVersion_Type.__name__ = "Integer32"
_ModuleVersion_Object = MibTableColumn
moduleVersion = _ModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 1, 1, 9),
    _ModuleVersion_Type()
)
moduleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleVersion.setStatus("current")


class _ModuleTimingSupport_Type(Integer32):
    """Custom type moduleTimingSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ModuleTimingSupport_Type.__name__ = "Integer32"
_ModuleTimingSupport_Object = MibTableColumn
moduleTimingSupport = _ModuleTimingSupport_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 1, 1, 10),
    _ModuleTimingSupport_Type()
)
moduleTimingSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleTimingSupport.setStatus("current")


class _ModuleProductNumber_Type(DisplayString):
    """Custom type moduleProductNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ModuleProductNumber_Type.__name__ = "DisplayString"
_ModuleProductNumber_Object = MibTableColumn
moduleProductNumber = _ModuleProductNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 1, 1, 11),
    _ModuleProductNumber_Type()
)
moduleProductNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleProductNumber.setStatus("current")


class _ModuleState_Type(Integer32):
    """Custom type moduleState based on Integer32"""
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
        *(("inService", 2),
          ("outOfService", 3),
          ("reset", 1),
          ("resetPair", 4))
    )


_ModuleState_Type.__name__ = "Integer32"
_ModuleState_Object = MibTableColumn
moduleState = _ModuleState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 1, 1, 12),
    _ModuleState_Type()
)
moduleState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleState.setStatus("current")
_ModuleSerialNumber_Type = DisplayString
_ModuleSerialNumber_Object = MibTableColumn
moduleSerialNumber = _ModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 1, 1, 13),
    _ModuleSerialNumber_Type()
)
moduleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSerialNumber.setStatus("current")


class _ModuleTestAdminStatus_Type(Integer32):
    """Custom type moduleTestAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("abortTest", 3),
          ("normal", 1),
          ("startTest", 2))
    )


_ModuleTestAdminStatus_Type.__name__ = "Integer32"
_ModuleTestAdminStatus_Object = MibTableColumn
moduleTestAdminStatus = _ModuleTestAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 1, 1, 14),
    _ModuleTestAdminStatus_Type()
)
moduleTestAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleTestAdminStatus.setStatus("current")


class _ModuleTestOperStatus_Type(Integer32):
    """Custom type moduleTestOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("testAborted", 5),
          ("testFailed", 4),
          ("testSuccessful", 3),
          ("testUnsupported", 6),
          ("underTest", 2))
    )


_ModuleTestOperStatus_Type.__name__ = "Integer32"
_ModuleTestOperStatus_Object = MibTableColumn
moduleTestOperStatus = _ModuleTestOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 1, 1, 15),
    _ModuleTestOperStatus_Type()
)
moduleTestOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleTestOperStatus.setStatus("current")


class _ModuleTestStatusText_Type(DisplayString):
    """Custom type moduleTestStatusText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_ModuleTestStatusText_Type.__name__ = "DisplayString"
_ModuleTestStatusText_Object = MibTableColumn
moduleTestStatusText = _ModuleTestStatusText_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 1, 1, 16),
    _ModuleTestStatusText_Type()
)
moduleTestStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleTestStatusText.setStatus("current")


class _ModuleAttachState_Type(Integer32):
    """Custom type moduleAttachState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("outOfService", 2))
    )


_ModuleAttachState_Type.__name__ = "Integer32"
_ModuleAttachState_Object = MibTableColumn
moduleAttachState = _ModuleAttachState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 1, 1, 17),
    _ModuleAttachState_Type()
)
moduleAttachState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleAttachState.setStatus("current")


class _ModuleCLEI_Type(DisplayString):
    """Custom type moduleCLEI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ModuleCLEI_Type.__name__ = "DisplayString"
_ModuleCLEI_Object = MibTableColumn
moduleCLEI = _ModuleCLEI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 1, 1, 18),
    _ModuleCLEI_Type()
)
moduleCLEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCLEI.setStatus("current")
_OutputBufferTable_Object = MibTable
outputBufferTable = _OutputBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    outputBufferTable.setStatus("current")
_OutputBufferEntry_Object = MibTableRow
outputBufferEntry = _OutputBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 2, 1)
)
outputBufferEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "obufBoard"),
    (0, "Fore-Switch-MIB", "obufNumber"),
    (0, "Fore-Switch-MIB", "obufType"),
)
if mibBuilder.loadTexts:
    outputBufferEntry.setStatus("current")
_ObufBoard_Type = Integer32
_ObufBoard_Object = MibTableColumn
obufBoard = _ObufBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 2, 1, 1),
    _ObufBoard_Type()
)
obufBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obufBoard.setStatus("current")
_ObufNumber_Type = Integer32
_ObufNumber_Object = MibTableColumn
obufNumber = _ObufNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 2, 1, 2),
    _ObufNumber_Type()
)
obufNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obufNumber.setStatus("current")
_ObufType_Type = Integer32
_ObufType_Object = MibTableColumn
obufType = _ObufType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 2, 1, 3),
    _ObufType_Type()
)
obufType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obufType.setStatus("current")


class _ObufOperStatus_Type(Integer32):
    """Custom type obufOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_ObufOperStatus_Type.__name__ = "Integer32"
_ObufOperStatus_Object = MibTableColumn
obufOperStatus = _ObufOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 2, 1, 4),
    _ObufOperStatus_Type()
)
obufOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obufOperStatus.setStatus("current")
_ObufBufferSize_Type = Integer32
_ObufBufferSize_Object = MibTableColumn
obufBufferSize = _ObufBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 2, 1, 5),
    _ObufBufferSize_Type()
)
obufBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obufBufferSize.setStatus("current")
_ObufQueueLength_Type = Gauge32
_ObufQueueLength_Object = MibTableColumn
obufQueueLength = _ObufQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 2, 1, 6),
    _ObufQueueLength_Type()
)
obufQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obufQueueLength.setStatus("current")
_ObufOverflows_Type = Gauge32
_ObufOverflows_Object = MibTableColumn
obufOverflows = _ObufOverflows_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 2, 1, 7),
    _ObufOverflows_Type()
)
obufOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obufOverflows.setStatus("current")
_ObufPriorityName_Type = DisplayString
_ObufPriorityName_Object = MibTableColumn
obufPriorityName = _ObufPriorityName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 2, 1, 8),
    _ObufPriorityName_Type()
)
obufPriorityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obufPriorityName.setStatus("current")
_ObufName_Type = DisplayString
_ObufName_Object = MibTableColumn
obufName = _ObufName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 2, 1, 9),
    _ObufName_Type()
)
obufName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obufName.setStatus("current")
_HwPortTable_Object = MibTable
hwPortTable = _HwPortTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hwPortTable.setStatus("current")
_HwPortEntry_Object = MibTableRow
hwPortEntry = _HwPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 3, 1)
)
hwPortEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "hwPortBoard"),
    (0, "Fore-Switch-MIB", "hwPortModule"),
    (0, "Fore-Switch-MIB", "hwPortNumber"),
)
if mibBuilder.loadTexts:
    hwPortEntry.setStatus("current")
_HwPortBoard_Type = Integer32
_HwPortBoard_Object = MibTableColumn
hwPortBoard = _HwPortBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 3, 1, 1),
    _HwPortBoard_Type()
)
hwPortBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortBoard.setStatus("current")
_HwPortModule_Type = Integer32
_HwPortModule_Object = MibTableColumn
hwPortModule = _HwPortModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 3, 1, 2),
    _HwPortModule_Type()
)
hwPortModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortModule.setStatus("current")
_HwPortNumber_Type = Integer32
_HwPortNumber_Object = MibTableColumn
hwPortNumber = _HwPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 3, 1, 3),
    _HwPortNumber_Type()
)
hwPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortNumber.setStatus("current")


class _HwPortVersion_Type(Integer32):
    """Custom type hwPortVersion based on Integer32"""
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
              10,
              11,
              67)
        )
    )
    namedValues = NamedValues(
        *(("generationA", 1),
          ("generationB", 2),
          ("generationC", 3),
          ("generationC2", 67),
          ("generationD", 6),
          ("generationE", 10),
          ("generationLC", 4),
          ("generationLE", 5),
          ("generationPC1", 7),
          ("generationPC2", 8),
          ("generationPCF1", 11))
    )


_HwPortVersion_Type.__name__ = "Integer32"
_HwPortVersion_Object = MibTableColumn
hwPortVersion = _HwPortVersion_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 3, 1, 4),
    _HwPortVersion_Type()
)
hwPortVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortVersion.setStatus("current")


class _HwPortModel_Type(Integer32):
    """Custom type hwPortModel based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35)
        )
    )
    namedValues = NamedValues(
        *(("model-6port-TAXI-100", 6),
          ("model-8B10B", 5),
          ("model-ASX-BP", 22),
          ("model-ASX-CTL", 7),
          ("model-CESDS1", 23),
          ("model-CESE1", 24),
          ("model-CHOC12", 30),
          ("model-CHOC3", 34),
          ("model-DS1", 19),
          ("model-DS3", 3),
          ("model-DS3-PDH", 16),
          ("model-E1", 20),
          ("model-E3", 17),
          ("model-ETH", 35),
          ("model-FRAMDS1", 25),
          ("model-FRAME1", 26),
          ("model-IMADS1", 27),
          ("model-IMAE1", 28),
          ("model-J2", 18),
          ("model-OC12", 8),
          ("model-OC12-POS", 33),
          ("model-OC3", 4),
          ("model-OC3-POS", 32),
          ("model-OC48", 9),
          ("model-RJ-45", 29),
          ("model-STM1", 31),
          ("model-TAXI-100", 1),
          ("model-TAXI-140", 2),
          ("model-TP25", 21))
    )


_HwPortModel_Type.__name__ = "Integer32"
_HwPortModel_Object = MibTableColumn
hwPortModel = _HwPortModel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 3, 1, 5),
    _HwPortModel_Type()
)
hwPortModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortModel.setStatus("current")


class _HwPortOperStatus_Type(Integer32):
    """Custom type hwPortOperStatus based on Integer32"""
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
        *(("down", 3),
          ("other", 1),
          ("unused", 4),
          ("up", 2))
    )


_HwPortOperStatus_Type.__name__ = "Integer32"
_HwPortOperStatus_Object = MibTableColumn
hwPortOperStatus = _HwPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 3, 1, 6),
    _HwPortOperStatus_Type()
)
hwPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortOperStatus.setStatus("current")
_HwPortBufferSize_Type = Integer32
_HwPortBufferSize_Object = MibTableColumn
hwPortBufferSize = _HwPortBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 3, 1, 7),
    _HwPortBufferSize_Type()
)
hwPortBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortBufferSize.setStatus("deprecated")
_HwPortQueueLength_Type = Gauge32
_HwPortQueueLength_Object = MibTableColumn
hwPortQueueLength = _HwPortQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 3, 1, 8),
    _HwPortQueueLength_Type()
)
hwPortQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortQueueLength.setStatus("deprecated")
_HwPortOverflows_Type = Counter32
_HwPortOverflows_Object = MibTableColumn
hwPortOverflows = _HwPortOverflows_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 3, 1, 9),
    _HwPortOverflows_Type()
)
hwPortOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortOverflows.setStatus("deprecated")
_HwPortErrors_Type = Counter32
_HwPortErrors_Object = MibTableColumn
hwPortErrors = _HwPortErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 3, 1, 10),
    _HwPortErrors_Type()
)
hwPortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortErrors.setStatus("deprecated")


class _HwPortCarrier_Type(Integer32):
    """Custom type hwPortCarrier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("carrier", 1),
          ("noCarrier", 2))
    )


_HwPortCarrier_Type.__name__ = "Integer32"
_HwPortCarrier_Object = MibTableColumn
hwPortCarrier = _HwPortCarrier_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 3, 1, 11),
    _HwPortCarrier_Type()
)
hwPortCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortCarrier.setStatus("current")
_HwPortGlobalIndex_Type = Integer32
_HwPortGlobalIndex_Object = MibTableColumn
hwPortGlobalIndex = _HwPortGlobalIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 3, 1, 12),
    _HwPortGlobalIndex_Type()
)
hwPortGlobalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortGlobalIndex.setStatus("deprecated")


class _HwPortName_Type(DisplayString):
    """Custom type hwPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_HwPortName_Type.__name__ = "DisplayString"
_HwPortName_Object = MibTableColumn
hwPortName = _HwPortName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 3, 1, 13),
    _HwPortName_Type()
)
hwPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortName.setStatus("current")


class _HwPortAdminStatus_Type(Integer32):
    """Custom type hwPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_HwPortAdminStatus_Type.__name__ = "Integer32"
_HwPortAdminStatus_Object = MibTableColumn
hwPortAdminStatus = _HwPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 3, 1, 14),
    _HwPortAdminStatus_Type()
)
hwPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortAdminStatus.setStatus("current")


class _HwPortTAXILoopback_Type(Integer32):
    """Custom type hwPortTAXILoopback based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopback", 2),
          ("noLoopback", 1))
    )


_HwPortTAXILoopback_Type.__name__ = "Integer32"
_HwPortTAXILoopback_Object = MibTableColumn
hwPortTAXILoopback = _HwPortTAXILoopback_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 3, 1, 15),
    _HwPortTAXILoopback_Type()
)
hwPortTAXILoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortTAXILoopback.setStatus("current")


class _HwPortLEDModel_Type(Integer32):
    """Custom type hwPortLEDModel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lan", 1),
          ("wan", 2))
    )


_HwPortLEDModel_Type.__name__ = "Integer32"
_HwPortLEDModel_Object = MibTableColumn
hwPortLEDModel = _HwPortLEDModel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 3, 1, 16),
    _HwPortLEDModel_Type()
)
hwPortLEDModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortLEDModel.setStatus("current")


class _HwPortTxLED_Type(Integer32):
    """Custom type hwPortTxLED based on Integer32"""
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
        *(("auto", 5),
          ("green", 2),
          ("off", 1),
          ("red", 3),
          ("yellow", 4))
    )


_HwPortTxLED_Type.__name__ = "Integer32"
_HwPortTxLED_Object = MibTableColumn
hwPortTxLED = _HwPortTxLED_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 3, 1, 17),
    _HwPortTxLED_Type()
)
hwPortTxLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortTxLED.setStatus("current")


class _HwPortRxLED_Type(Integer32):
    """Custom type hwPortRxLED based on Integer32"""
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
        *(("auto", 5),
          ("green", 2),
          ("off", 1),
          ("red", 3),
          ("yellow", 4))
    )


_HwPortRxLED_Type.__name__ = "Integer32"
_HwPortRxLED_Object = MibTableColumn
hwPortRxLED = _HwPortRxLED_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 3, 1, 18),
    _HwPortRxLED_Type()
)
hwPortRxLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortRxLED.setStatus("current")
_HwPortIfIndex_Type = Integer32
_HwPortIfIndex_Object = MibTableColumn
hwPortIfIndex = _HwPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 3, 1, 19),
    _HwPortIfIndex_Type()
)
hwPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortIfIndex.setStatus("current")


class _HwPortRxSyncLED_Type(Integer32):
    """Custom type hwPortRxSyncLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("green", 2),
          ("off", 1))
    )


_HwPortRxSyncLED_Type.__name__ = "Integer32"
_HwPortRxSyncLED_Object = MibTableColumn
hwPortRxSyncLED = _HwPortRxSyncLED_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 3, 1, 20),
    _HwPortRxSyncLED_Type()
)
hwPortRxSyncLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortRxSyncLED.setStatus("current")
_HwPortCounterResetTime_Type = TimeStamp
_HwPortCounterResetTime_Object = MibTableColumn
hwPortCounterResetTime = _HwPortCounterResetTime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 3, 1, 21),
    _HwPortCounterResetTime_Type()
)
hwPortCounterResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortCounterResetTime.setStatus("current")


class _HwPortCounterReset_Type(Integer32):
    """Custom type hwPortCounterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("resetFalse", 4),
          ("resetRequest", 1),
          ("resetTrue", 3))
    )


_HwPortCounterReset_Type.__name__ = "Integer32"
_HwPortCounterReset_Object = MibTableColumn
hwPortCounterReset = _HwPortCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 3, 1, 22),
    _HwPortCounterReset_Type()
)
hwPortCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortCounterReset.setStatus("current")
_HwPortSpeed_Type = Unsigned32
_HwPortSpeed_Object = MibTableColumn
hwPortSpeed = _HwPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 3, 1, 23),
    _HwPortSpeed_Type()
)
hwPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortSpeed.setStatus("current")
_NetmodAlarmsTable_Object = MibTable
netmodAlarmsTable = _NetmodAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    netmodAlarmsTable.setStatus("current")
_NetmodAlarmsEntry_Object = MibTableRow
netmodAlarmsEntry = _NetmodAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 4, 1)
)
netmodAlarmsEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "netmodSlot"),
)
if mibBuilder.loadTexts:
    netmodAlarmsEntry.setStatus("current")
_NetmodSlot_Type = Integer32
_NetmodSlot_Object = MibTableColumn
netmodSlot = _NetmodSlot_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 4, 1, 1),
    _NetmodSlot_Type()
)
netmodSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netmodSlot.setStatus("current")


class _NetmodSlotPriority_Type(Integer32):
    """Custom type netmodSlotPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 2),
          ("none", 3))
    )


_NetmodSlotPriority_Type.__name__ = "Integer32"
_NetmodSlotPriority_Object = MibTableColumn
netmodSlotPriority = _NetmodSlotPriority_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 4, 1, 2),
    _NetmodSlotPriority_Type()
)
netmodSlotPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netmodSlotPriority.setStatus("current")


class _NetmodStatus_Type(Integer32):
    """Custom type netmodStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absent", 2),
          ("present", 1))
    )


_NetmodStatus_Type.__name__ = "Integer32"
_NetmodStatus_Object = MibTableColumn
netmodStatus = _NetmodStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 4, 1, 3),
    _NetmodStatus_Type()
)
netmodStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netmodStatus.setStatus("current")
_NetmodName_Type = DisplayString
_NetmodName_Object = MibTableColumn
netmodName = _NetmodName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 4, 1, 4),
    _NetmodName_Type()
)
netmodName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netmodName.setStatus("current")
_HdcompTable_Object = MibTable
hdcompTable = _HdcompTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    hdcompTable.setStatus("current")
_HdcompEntry_Object = MibTableRow
hdcompEntry = _HdcompEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 5, 1)
)
hdcompEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "hdcompIndex"),
)
if mibBuilder.loadTexts:
    hdcompEntry.setStatus("current")
_HdcompIndex_Type = Integer32
_HdcompIndex_Object = MibTableColumn
hdcompIndex = _HdcompIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 5, 1, 1),
    _HdcompIndex_Type()
)
hdcompIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hdcompIndex.setStatus("current")


class _HdcompDescr_Type(DisplayString):
    """Custom type hdcompDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_HdcompDescr_Type.__name__ = "DisplayString"
_HdcompDescr_Object = MibTableColumn
hdcompDescr = _HdcompDescr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 5, 1, 2),
    _HdcompDescr_Type()
)
hdcompDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdcompDescr.setStatus("current")
_HdcompAsicVersion_Type = Integer32
_HdcompAsicVersion_Object = MibTableColumn
hdcompAsicVersion = _HdcompAsicVersion_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 5, 1, 3),
    _HdcompAsicVersion_Type()
)
hdcompAsicVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdcompAsicVersion.setStatus("current")
_HdcompVpiLookupErrors_Type = Counter32
_HdcompVpiLookupErrors_Object = MibTableColumn
hdcompVpiLookupErrors = _HdcompVpiLookupErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 5, 1, 4),
    _HdcompVpiLookupErrors_Type()
)
hdcompVpiLookupErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdcompVpiLookupErrors.setStatus("current")
_HdcompVciLookupErrors_Type = Counter32
_HdcompVciLookupErrors_Object = MibTableColumn
hdcompVciLookupErrors = _HdcompVciLookupErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 5, 1, 5),
    _HdcompVciLookupErrors_Type()
)
hdcompVciLookupErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdcompVciLookupErrors.setStatus("current")
_AppModuleTable_Object = MibTable
appModuleTable = _AppModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    appModuleTable.setStatus("current")
_AppModuleEntry_Object = MibTableRow
appModuleEntry = _AppModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 6, 1)
)
appModuleEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "appModuleIndex"),
)
if mibBuilder.loadTexts:
    appModuleEntry.setStatus("current")
_AppModuleIndex_Type = Integer32
_AppModuleIndex_Object = MibTableColumn
appModuleIndex = _AppModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 6, 1, 1),
    _AppModuleIndex_Type()
)
appModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appModuleIndex.setStatus("current")
_AppModuleName_Type = DisplayString
_AppModuleName_Object = MibTableColumn
appModuleName = _AppModuleName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 6, 1, 2),
    _AppModuleName_Type()
)
appModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appModuleName.setStatus("current")


class _AppModuleOperState_Type(Integer32):
    """Custom type appModuleOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("down", 5),
          ("failed", 6),
          ("hwInitInProgress", 2),
          ("notConfigured", 1),
          ("shutDownInProgress", 4),
          ("up", 3))
    )


_AppModuleOperState_Type.__name__ = "Integer32"
_AppModuleOperState_Object = MibTableColumn
appModuleOperState = _AppModuleOperState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 6, 1, 3),
    _AppModuleOperState_Type()
)
appModuleOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appModuleOperState.setStatus("current")


class _AppModuleStatusText_Type(DisplayString):
    """Custom type appModuleStatusText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AppModuleStatusText_Type.__name__ = "DisplayString"
_AppModuleStatusText_Object = MibTableColumn
appModuleStatusText = _AppModuleStatusText_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 6, 1, 4),
    _AppModuleStatusText_Type()
)
appModuleStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appModuleStatusText.setStatus("current")
_AppModuleApplicationType_Type = DisplayString
_AppModuleApplicationType_Object = MibTableColumn
appModuleApplicationType = _AppModuleApplicationType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 6, 1, 5),
    _AppModuleApplicationType_Type()
)
appModuleApplicationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appModuleApplicationType.setStatus("current")


class _AppModuleSoftwareVersion_Type(DisplayString):
    """Custom type appModuleSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AppModuleSoftwareVersion_Type.__name__ = "DisplayString"
_AppModuleSoftwareVersion_Object = MibTableColumn
appModuleSoftwareVersion = _AppModuleSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 6, 1, 6),
    _AppModuleSoftwareVersion_Type()
)
appModuleSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appModuleSoftwareVersion.setStatus("current")


class _AppModuleBootSoftwareVersion_Type(DisplayString):
    """Custom type appModuleBootSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AppModuleBootSoftwareVersion_Type.__name__ = "DisplayString"
_AppModuleBootSoftwareVersion_Object = MibTableColumn
appModuleBootSoftwareVersion = _AppModuleBootSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 6, 1, 7),
    _AppModuleBootSoftwareVersion_Type()
)
appModuleBootSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appModuleBootSoftwareVersion.setStatus("current")


class _AppModuleOosLed_Type(Integer32):
    """Custom type appModuleOosLed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("red", 2))
    )


_AppModuleOosLed_Type.__name__ = "Integer32"
_AppModuleOosLed_Object = MibTableColumn
appModuleOosLed = _AppModuleOosLed_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 6, 1, 8),
    _AppModuleOosLed_Type()
)
appModuleOosLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appModuleOosLed.setStatus("current")


class _AppModulePanicAction_Type(Integer32):
    """Custom type appModulePanicAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("suspend", 2))
    )


_AppModulePanicAction_Type.__name__ = "Integer32"
_AppModulePanicAction_Object = MibTableColumn
appModulePanicAction = _AppModulePanicAction_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 2, 6, 1, 9),
    _AppModulePanicAction_Type()
)
appModulePanicAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appModulePanicAction.setStatus("current")
_Timing_ObjectIdentity = ObjectIdentity
timing = _Timing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 3)
)
_NetmodTimingGroup_ObjectIdentity = ObjectIdentity
netmodTimingGroup = _NetmodTimingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 3, 1)
)
_NetmodTimingTable_Object = MibTable
netmodTimingTable = _NetmodTimingTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    netmodTimingTable.setStatus("obsolete")
_NetmodTimingEntry_Object = MibTableRow
netmodTimingEntry = _NetmodTimingEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 3, 1, 1, 1)
)
netmodTimingEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "ntBoard"),
    (0, "Fore-Switch-MIB", "ntModule"),
)
if mibBuilder.loadTexts:
    netmodTimingEntry.setStatus("obsolete")
_NtBoard_Type = Integer32
_NtBoard_Object = MibTableColumn
ntBoard = _NtBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 3, 1, 1, 1, 1),
    _NtBoard_Type()
)
ntBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntBoard.setStatus("obsolete")
_NtModule_Type = Integer32
_NtModule_Object = MibTableColumn
ntModule = _NtModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 3, 1, 1, 1, 2),
    _NtModule_Type()
)
ntModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntModule.setStatus("obsolete")
_NtPrimaryRecoveredClock_Type = Integer32
_NtPrimaryRecoveredClock_Object = MibTableColumn
ntPrimaryRecoveredClock = _NtPrimaryRecoveredClock_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 3, 1, 1, 1, 3),
    _NtPrimaryRecoveredClock_Type()
)
ntPrimaryRecoveredClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntPrimaryRecoveredClock.setStatus("obsolete")
_NtSecondaryRecoveredClock_Type = Integer32
_NtSecondaryRecoveredClock_Object = MibTableColumn
ntSecondaryRecoveredClock = _NtSecondaryRecoveredClock_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 3, 1, 1, 1, 4),
    _NtSecondaryRecoveredClock_Type()
)
ntSecondaryRecoveredClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntSecondaryRecoveredClock.setStatus("obsolete")


class _NtPrimaryExportClock_Type(Integer32):
    """Custom type ntPrimaryExportClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crystalClock", 2),
          ("noClock", 3),
          ("primaryRecoveredClock", 1))
    )


_NtPrimaryExportClock_Type.__name__ = "Integer32"
_NtPrimaryExportClock_Object = MibTableColumn
ntPrimaryExportClock = _NtPrimaryExportClock_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 3, 1, 1, 1, 5),
    _NtPrimaryExportClock_Type()
)
ntPrimaryExportClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntPrimaryExportClock.setStatus("obsolete")


class _NtSecondaryExportClock_Type(Integer32):
    """Custom type ntSecondaryExportClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crystalClock", 2),
          ("noClock", 3),
          ("secondaryRecoveredClock", 1))
    )


_NtSecondaryExportClock_Type.__name__ = "Integer32"
_NtSecondaryExportClock_Object = MibTableColumn
ntSecondaryExportClock = _NtSecondaryExportClock_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 3, 1, 1, 1, 6),
    _NtSecondaryExportClock_Type()
)
ntSecondaryExportClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntSecondaryExportClock.setStatus("obsolete")


class _NtGlobalClock_Type(Integer32):
    """Custom type ntGlobalClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exportClock", 1),
          ("importClock", 2))
    )


_NtGlobalClock_Type.__name__ = "Integer32"
_NtGlobalClock_Object = MibTableColumn
ntGlobalClock = _NtGlobalClock_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 3, 1, 1, 1, 7),
    _NtGlobalClock_Type()
)
ntGlobalClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntGlobalClock.setStatus("obsolete")


class _NtExportClockOperStatus_Type(Integer32):
    """Custom type ntExportClockOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crystalClock", 3),
          ("primaryClock", 1),
          ("secondaryClock", 2))
    )


_NtExportClockOperStatus_Type.__name__ = "Integer32"
_NtExportClockOperStatus_Object = MibTableColumn
ntExportClockOperStatus = _NtExportClockOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 3, 1, 1, 1, 8),
    _NtExportClockOperStatus_Type()
)
ntExportClockOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntExportClockOperStatus.setStatus("obsolete")


class _NtPrimaryImportClock_Type(Integer32):
    """Custom type ntPrimaryImportClock based on Integer32"""
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
        *(("board1PrimaryClock", 5),
          ("board2PrimaryClock", 6),
          ("board3PrimaryClock", 7),
          ("board4PrimaryClock", 8),
          ("managementStationClock", 9),
          ("netmodAExportClock", 1),
          ("netmodBExportClock", 2),
          ("netmodCExportClock", 3),
          ("netmodDExportClock", 4))
    )


_NtPrimaryImportClock_Type.__name__ = "Integer32"
_NtPrimaryImportClock_Object = MibTableColumn
ntPrimaryImportClock = _NtPrimaryImportClock_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 3, 1, 1, 1, 9),
    _NtPrimaryImportClock_Type()
)
ntPrimaryImportClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntPrimaryImportClock.setStatus("obsolete")


class _NtSecondaryImportClock_Type(Integer32):
    """Custom type ntSecondaryImportClock based on Integer32"""
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
        *(("board1PrimaryClock", 5),
          ("board2PrimaryClock", 6),
          ("board3PrimaryClock", 7),
          ("board4PrimaryClock", 8),
          ("managementStationClock", 9),
          ("netmodAExportClock", 1),
          ("netmodBExportClock", 2),
          ("netmodCExportClock", 3),
          ("netmodDExportClock", 4))
    )


_NtSecondaryImportClock_Type.__name__ = "Integer32"
_NtSecondaryImportClock_Object = MibTableColumn
ntSecondaryImportClock = _NtSecondaryImportClock_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 3, 1, 1, 1, 10),
    _NtSecondaryImportClock_Type()
)
ntSecondaryImportClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntSecondaryImportClock.setStatus("obsolete")


class _NtImportClockOperStatus_Type(Integer32):
    """Custom type ntImportClockOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("netmodExportClock", 3),
          ("primaryClock", 1),
          ("secondaryClock", 2))
    )


_NtImportClockOperStatus_Type.__name__ = "Integer32"
_NtImportClockOperStatus_Object = MibTableColumn
ntImportClockOperStatus = _NtImportClockOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 3, 1, 1, 1, 11),
    _NtImportClockOperStatus_Type()
)
ntImportClockOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntImportClockOperStatus.setStatus("obsolete")
_BoardTimingGroup_ObjectIdentity = ObjectIdentity
boardTimingGroup = _BoardTimingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 3, 2)
)
_BoardTimingTable_Object = MibTable
boardTimingTable = _BoardTimingTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    boardTimingTable.setStatus("obsolete")
_BoardTimingEntry_Object = MibTableRow
boardTimingEntry = _BoardTimingEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 3, 2, 1, 1)
)
boardTimingEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "btBoard"),
)
if mibBuilder.loadTexts:
    boardTimingEntry.setStatus("obsolete")
_BtBoard_Type = Integer32
_BtBoard_Object = MibTableColumn
btBoard = _BtBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 3, 2, 1, 1, 1),
    _BtBoard_Type()
)
btBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btBoard.setStatus("obsolete")


class _BtPrimaryClock_Type(Integer32):
    """Custom type btPrimaryClock based on Integer32"""
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
        *(("netmodAExportClock", 1),
          ("netmodBExportClock", 2),
          ("netmodCExportClock", 3),
          ("netmodDExportClock", 4),
          ("netmodNone", 5))
    )


_BtPrimaryClock_Type.__name__ = "Integer32"
_BtPrimaryClock_Object = MibTableColumn
btPrimaryClock = _BtPrimaryClock_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 3, 2, 1, 1, 2),
    _BtPrimaryClock_Type()
)
btPrimaryClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btPrimaryClock.setStatus("obsolete")


class _BtSecondaryClock_Type(Integer32):
    """Custom type btSecondaryClock based on Integer32"""
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
        *(("netmodAExportClock", 1),
          ("netmodBExportClock", 2),
          ("netmodCExportClock", 3),
          ("netmodDExportClock", 4),
          ("netmodNone", 5))
    )


_BtSecondaryClock_Type.__name__ = "Integer32"
_BtSecondaryClock_Object = MibTableColumn
btSecondaryClock = _BtSecondaryClock_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 3, 2, 1, 1, 3),
    _BtSecondaryClock_Type()
)
btSecondaryClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btSecondaryClock.setStatus("obsolete")


class _BtPrimaryClockOperStatus_Type(Integer32):
    """Custom type btPrimaryClockOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clockDown", 2),
          ("clockUp", 1))
    )


_BtPrimaryClockOperStatus_Type.__name__ = "Integer32"
_BtPrimaryClockOperStatus_Object = MibTableColumn
btPrimaryClockOperStatus = _BtPrimaryClockOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 3, 2, 1, 1, 4),
    _BtPrimaryClockOperStatus_Type()
)
btPrimaryClockOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btPrimaryClockOperStatus.setStatus("obsolete")


class _BtSecondaryClockOperStatus_Type(Integer32):
    """Custom type btSecondaryClockOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clockDown", 2),
          ("clockUp", 1))
    )


_BtSecondaryClockOperStatus_Type.__name__ = "Integer32"
_BtSecondaryClockOperStatus_Object = MibTableColumn
btSecondaryClockOperStatus = _BtSecondaryClockOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 3, 2, 1, 1, 5),
    _BtSecondaryClockOperStatus_Type()
)
btSecondaryClockOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btSecondaryClockOperStatus.setStatus("obsolete")
_Environment_ObjectIdentity = ObjectIdentity
environment = _Environment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4)
)
_AlarmGroup_ObjectIdentity = ObjectIdentity
alarmGroup = _AlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 1)
)
_SwAlarmTable_Object = MibTable
swAlarmTable = _SwAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    swAlarmTable.setStatus("current")
_SwAlarmEntry_Object = MibTableRow
swAlarmEntry = _SwAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 1, 1, 1)
)
swAlarmEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "swAlarmType"),
)
if mibBuilder.loadTexts:
    swAlarmEntry.setStatus("current")


class _SwAlarmType_Type(Integer32):
    """Custom type swAlarmType based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("allTCMsFailed", 16),
          ("allTimingRefsFailed", 14),
          ("fabricRemoved", 11),
          ("fanBankFailed", 3),
          ("genPortFailure", 12),
          ("linkFailed", 5),
          ("netmodRemovedHighPrio", 9),
          ("netmodRemovedLowPrio", 10),
          ("powerSupply5VoltFailed", 8),
          ("powerSupplyInputFailed", 1),
          ("powerSupplyOutputFailed", 2),
          ("powerSupplyOverCurrent", 7),
          ("singleTCMFailed", 15),
          ("singleTimingRefFailed", 13),
          ("spansFailed", 6),
          ("tempSensorOverTemp", 4))
    )


_SwAlarmType_Type.__name__ = "Integer32"
_SwAlarmType_Object = MibTableColumn
swAlarmType = _SwAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 1, 1, 1, 1),
    _SwAlarmType_Type()
)
swAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAlarmType.setStatus("current")


class _SwAlarmStatus_Type(Integer32):
    """Custom type swAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_SwAlarmStatus_Type.__name__ = "Integer32"
_SwAlarmStatus_Object = MibTableColumn
swAlarmStatus = _SwAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 1, 1, 1, 2),
    _SwAlarmStatus_Type()
)
swAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAlarmStatus.setStatus("current")


class _SwAlarmMinorCategory_Type(Integer32):
    """Custom type swAlarmMinorCategory based on Integer32"""
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


_SwAlarmMinorCategory_Type.__name__ = "Integer32"
_SwAlarmMinorCategory_Object = MibTableColumn
swAlarmMinorCategory = _SwAlarmMinorCategory_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 1, 1, 1, 3),
    _SwAlarmMinorCategory_Type()
)
swAlarmMinorCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAlarmMinorCategory.setStatus("current")


class _SwAlarmMajorCategory_Type(Integer32):
    """Custom type swAlarmMajorCategory based on Integer32"""
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


_SwAlarmMajorCategory_Type.__name__ = "Integer32"
_SwAlarmMajorCategory_Object = MibTableColumn
swAlarmMajorCategory = _SwAlarmMajorCategory_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 1, 1, 1, 4),
    _SwAlarmMajorCategory_Type()
)
swAlarmMajorCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAlarmMajorCategory.setStatus("current")


class _SwAlarmReset_Type(Integer32):
    """Custom type swAlarmReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("enabled", 1))
    )


_SwAlarmReset_Type.__name__ = "Integer32"
_SwAlarmReset_Object = MibTableColumn
swAlarmReset = _SwAlarmReset_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 1, 1, 1, 5),
    _SwAlarmReset_Type()
)
swAlarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAlarmReset.setStatus("current")


class _SwAlarmCriticalCategory_Type(Integer32):
    """Custom type swAlarmCriticalCategory based on Integer32"""
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


_SwAlarmCriticalCategory_Type.__name__ = "Integer32"
_SwAlarmCriticalCategory_Object = MibTableColumn
swAlarmCriticalCategory = _SwAlarmCriticalCategory_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 1, 1, 1, 6),
    _SwAlarmCriticalCategory_Type()
)
swAlarmCriticalCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAlarmCriticalCategory.setStatus("current")


class _SwAlarmACOState_Type(Integer32):
    """Custom type swAlarmACOState based on Integer32"""
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


_SwAlarmACOState_Type.__name__ = "Integer32"
_SwAlarmACOState_Object = MibTableColumn
swAlarmACOState = _SwAlarmACOState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 1, 1, 1, 7),
    _SwAlarmACOState_Type()
)
swAlarmACOState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAlarmACOState.setStatus("current")


class _SwAlarmMajorRelayState_Type(Integer32):
    """Custom type swAlarmMajorRelayState based on Integer32"""
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


_SwAlarmMajorRelayState_Type.__name__ = "Integer32"
_SwAlarmMajorRelayState_Object = MibScalar
swAlarmMajorRelayState = _SwAlarmMajorRelayState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 1, 2),
    _SwAlarmMajorRelayState_Type()
)
swAlarmMajorRelayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAlarmMajorRelayState.setStatus("current")


class _SwAlarmMinorRelayState_Type(Integer32):
    """Custom type swAlarmMinorRelayState based on Integer32"""
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


_SwAlarmMinorRelayState_Type.__name__ = "Integer32"
_SwAlarmMinorRelayState_Object = MibScalar
swAlarmMinorRelayState = _SwAlarmMinorRelayState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 1, 3),
    _SwAlarmMinorRelayState_Type()
)
swAlarmMinorRelayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAlarmMinorRelayState.setStatus("current")


class _SwAlarmCriticalRelayState_Type(Integer32):
    """Custom type swAlarmCriticalRelayState based on Integer32"""
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


_SwAlarmCriticalRelayState_Type.__name__ = "Integer32"
_SwAlarmCriticalRelayState_Object = MibScalar
swAlarmCriticalRelayState = _SwAlarmCriticalRelayState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 1, 4),
    _SwAlarmCriticalRelayState_Type()
)
swAlarmCriticalRelayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAlarmCriticalRelayState.setStatus("current")
_SwAlarmRelayTable_Object = MibTable
swAlarmRelayTable = _SwAlarmRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 1, 5)
)
if mibBuilder.loadTexts:
    swAlarmRelayTable.setStatus("current")
_SwAlarmRelayEntry_Object = MibTableRow
swAlarmRelayEntry = _SwAlarmRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 1, 5, 1)
)
swAlarmRelayEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "swAlarmRelayIndex"),
)
if mibBuilder.loadTexts:
    swAlarmRelayEntry.setStatus("current")
_SwAlarmRelayIndex_Type = Integer32
_SwAlarmRelayIndex_Object = MibTableColumn
swAlarmRelayIndex = _SwAlarmRelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 1, 5, 1, 1),
    _SwAlarmRelayIndex_Type()
)
swAlarmRelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAlarmRelayIndex.setStatus("current")


class _SwAlarmRelayFunction_Type(Integer32):
    """Custom type swAlarmRelayFunction based on Integer32"""
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
        *(("swCriticalAlarmRelay", 4),
          ("swMajorAlarmRelay", 2),
          ("swMinorAlarmRelay", 3),
          ("swUnusedRelay", 1))
    )


_SwAlarmRelayFunction_Type.__name__ = "Integer32"
_SwAlarmRelayFunction_Object = MibTableColumn
swAlarmRelayFunction = _SwAlarmRelayFunction_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 1, 5, 1, 2),
    _SwAlarmRelayFunction_Type()
)
swAlarmRelayFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAlarmRelayFunction.setStatus("current")


class _SwAlarmRelayState_Type(Integer32):
    """Custom type swAlarmRelayState based on Integer32"""
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


_SwAlarmRelayState_Type.__name__ = "Integer32"
_SwAlarmRelayState_Object = MibTableColumn
swAlarmRelayState = _SwAlarmRelayState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 1, 5, 1, 3),
    _SwAlarmRelayState_Type()
)
swAlarmRelayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAlarmRelayState.setStatus("current")


class _SwAlarmRelayOperMode_Type(Integer32):
    """Custom type swAlarmRelayOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("test", 3))
    )


_SwAlarmRelayOperMode_Type.__name__ = "Integer32"
_SwAlarmRelayOperMode_Object = MibTableColumn
swAlarmRelayOperMode = _SwAlarmRelayOperMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 1, 5, 1, 4),
    _SwAlarmRelayOperMode_Type()
)
swAlarmRelayOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAlarmRelayOperMode.setStatus("current")
_PowerGroup_ObjectIdentity = ObjectIdentity
powerGroup = _PowerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 2)
)
_EnvMaxNumberOfPowerSupplies_Type = Integer32
_EnvMaxNumberOfPowerSupplies_Object = MibScalar
envMaxNumberOfPowerSupplies = _EnvMaxNumberOfPowerSupplies_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 2, 1),
    _EnvMaxNumberOfPowerSupplies_Type()
)
envMaxNumberOfPowerSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMaxNumberOfPowerSupplies.setStatus("current")
_EnvNumberOfPowerSupplies_Type = Integer32
_EnvNumberOfPowerSupplies_Object = MibScalar
envNumberOfPowerSupplies = _EnvNumberOfPowerSupplies_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 2, 2),
    _EnvNumberOfPowerSupplies_Type()
)
envNumberOfPowerSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envNumberOfPowerSupplies.setStatus("current")
_EnvPowerSupplyTable_Object = MibTable
envPowerSupplyTable = _EnvPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 2, 3)
)
if mibBuilder.loadTexts:
    envPowerSupplyTable.setStatus("current")
_EnvPowerSupplyEntry_Object = MibTableRow
envPowerSupplyEntry = _EnvPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 2, 3, 1)
)
envPowerSupplyEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "envPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    envPowerSupplyEntry.setStatus("current")
_EnvPowerSupplyIndex_Type = Integer32
_EnvPowerSupplyIndex_Object = MibTableColumn
envPowerSupplyIndex = _EnvPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 2, 3, 1, 1),
    _EnvPowerSupplyIndex_Type()
)
envPowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envPowerSupplyIndex.setStatus("current")


class _EnvPowerSupplyType_Type(Integer32):
    """Custom type envPowerSupplyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ps30ADC", 7),
          ("ps48VDC", 5),
          ("psAutoRangeAC", 4),
          ("psRM1000HA", 6),
          ("psRM1000HA-C", 8),
          ("psUnknown", 1))
    )


_EnvPowerSupplyType_Type.__name__ = "Integer32"
_EnvPowerSupplyType_Object = MibTableColumn
envPowerSupplyType = _EnvPowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 2, 3, 1, 2),
    _EnvPowerSupplyType_Type()
)
envPowerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envPowerSupplyType.setStatus("current")
_EnvPowerSupplyInputState_Type = GeneralState
_EnvPowerSupplyInputState_Object = MibTableColumn
envPowerSupplyInputState = _EnvPowerSupplyInputState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 2, 3, 1, 3),
    _EnvPowerSupplyInputState_Type()
)
envPowerSupplyInputState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envPowerSupplyInputState.setStatus("current")
_EnvPowerSupplyOutputState_Type = GeneralState
_EnvPowerSupplyOutputState_Object = MibTableColumn
envPowerSupplyOutputState = _EnvPowerSupplyOutputState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 2, 3, 1, 4),
    _EnvPowerSupplyOutputState_Type()
)
envPowerSupplyOutputState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envPowerSupplyOutputState.setStatus("current")
_EnvPowerSupplySerialNumber_Type = Integer32
_EnvPowerSupplySerialNumber_Object = MibTableColumn
envPowerSupplySerialNumber = _EnvPowerSupplySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 2, 3, 1, 5),
    _EnvPowerSupplySerialNumber_Type()
)
envPowerSupplySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envPowerSupplySerialNumber.setStatus("current")
_EnvPowerSupplyVersion_Type = Integer32
_EnvPowerSupplyVersion_Object = MibTableColumn
envPowerSupplyVersion = _EnvPowerSupplyVersion_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 2, 3, 1, 6),
    _EnvPowerSupplyVersion_Type()
)
envPowerSupplyVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envPowerSupplyVersion.setStatus("current")
_EnvPowerSupplyCurrentState_Type = GeneralState
_EnvPowerSupplyCurrentState_Object = MibTableColumn
envPowerSupplyCurrentState = _EnvPowerSupplyCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 2, 3, 1, 7),
    _EnvPowerSupplyCurrentState_Type()
)
envPowerSupplyCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envPowerSupplyCurrentState.setStatus("current")
_EnvPowerSupply5VoltState_Type = GeneralState
_EnvPowerSupply5VoltState_Object = MibTableColumn
envPowerSupply5VoltState = _EnvPowerSupply5VoltState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 2, 3, 1, 8),
    _EnvPowerSupply5VoltState_Type()
)
envPowerSupply5VoltState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envPowerSupply5VoltState.setStatus("current")
_FansGroup_ObjectIdentity = ObjectIdentity
fansGroup = _FansGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 3)
)
_EnvNumberOfFanBanks_Type = Integer32
_EnvNumberOfFanBanks_Object = MibScalar
envNumberOfFanBanks = _EnvNumberOfFanBanks_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 3, 1),
    _EnvNumberOfFanBanks_Type()
)
envNumberOfFanBanks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envNumberOfFanBanks.setStatus("current")
_EnvFanBanksTable_Object = MibTable
envFanBanksTable = _EnvFanBanksTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    envFanBanksTable.setStatus("current")
_EnvFanBanksEntry_Object = MibTableRow
envFanBanksEntry = _EnvFanBanksEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 3, 2, 1)
)
envFanBanksEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "envFanBankIndex"),
)
if mibBuilder.loadTexts:
    envFanBanksEntry.setStatus("current")
_EnvFanBankIndex_Type = Integer32
_EnvFanBankIndex_Object = MibTableColumn
envFanBankIndex = _EnvFanBankIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 3, 2, 1, 1),
    _EnvFanBankIndex_Type()
)
envFanBankIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envFanBankIndex.setStatus("current")
_EnvFanBankState_Type = GeneralState
_EnvFanBankState_Object = MibTableColumn
envFanBankState = _EnvFanBankState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 3, 2, 1, 3),
    _EnvFanBankState_Type()
)
envFanBankState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envFanBankState.setStatus("current")
_EnvFanBankSerialNumber_Type = DisplayString
_EnvFanBankSerialNumber_Object = MibTableColumn
envFanBankSerialNumber = _EnvFanBankSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 3, 2, 1, 4),
    _EnvFanBankSerialNumber_Type()
)
envFanBankSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envFanBankSerialNumber.setStatus("current")
_EnvFanBankType_Type = Integer32
_EnvFanBankType_Object = MibTableColumn
envFanBankType = _EnvFanBankType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 3, 2, 1, 5),
    _EnvFanBankType_Type()
)
envFanBankType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envFanBankType.setStatus("current")
_EnvFanBankRevision_Type = Integer32
_EnvFanBankRevision_Object = MibTableColumn
envFanBankRevision = _EnvFanBankRevision_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 3, 2, 1, 6),
    _EnvFanBankRevision_Type()
)
envFanBankRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envFanBankRevision.setStatus("current")
_TempGroup_ObjectIdentity = ObjectIdentity
tempGroup = _TempGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 4)
)
_EnvNumberOfTempSensors_Type = Integer32
_EnvNumberOfTempSensors_Object = MibScalar
envNumberOfTempSensors = _EnvNumberOfTempSensors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 4, 1),
    _EnvNumberOfTempSensors_Type()
)
envNumberOfTempSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envNumberOfTempSensors.setStatus("current")
_EnvTempSensorsTable_Object = MibTable
envTempSensorsTable = _EnvTempSensorsTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 4, 2)
)
if mibBuilder.loadTexts:
    envTempSensorsTable.setStatus("current")
_EnvTempSensorsEntry_Object = MibTableRow
envTempSensorsEntry = _EnvTempSensorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 4, 2, 1)
)
envTempSensorsEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "envTempSensorIndex"),
)
if mibBuilder.loadTexts:
    envTempSensorsEntry.setStatus("current")


class _EnvTempSensorIndex_Type(Integer32):
    """Custom type envTempSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("enclosure", 1),
          ("power-supply-1", 2),
          ("power-supply-2", 3),
          ("power-supply-3", 4),
          ("power-supply-4", 5),
          ("power-supply-5", 6))
    )


_EnvTempSensorIndex_Type.__name__ = "Integer32"
_EnvTempSensorIndex_Object = MibTableColumn
envTempSensorIndex = _EnvTempSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 4, 2, 1, 1),
    _EnvTempSensorIndex_Type()
)
envTempSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTempSensorIndex.setStatus("current")


class _EnvTempSensorState_Type(Integer32):
    """Custom type envTempSensorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("overTemp", 2))
    )


_EnvTempSensorState_Type.__name__ = "Integer32"
_EnvTempSensorState_Object = MibTableColumn
envTempSensorState = _EnvTempSensorState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 4, 2, 1, 2),
    _EnvTempSensorState_Type()
)
envTempSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTempSensorState.setStatus("current")
_CpuGroup_ObjectIdentity = ObjectIdentity
cpuGroup = _CpuGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 5)
)
_EnvMaxNumberOfCPUs_Type = Integer32
_EnvMaxNumberOfCPUs_Object = MibScalar
envMaxNumberOfCPUs = _EnvMaxNumberOfCPUs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 5, 1),
    _EnvMaxNumberOfCPUs_Type()
)
envMaxNumberOfCPUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMaxNumberOfCPUs.setStatus("current")
_EnvNumberOfCPUs_Type = Integer32
_EnvNumberOfCPUs_Object = MibScalar
envNumberOfCPUs = _EnvNumberOfCPUs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 5, 2),
    _EnvNumberOfCPUs_Type()
)
envNumberOfCPUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envNumberOfCPUs.setStatus("current")
_EnvCPUsTable_Object = MibTable
envCPUsTable = _EnvCPUsTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 5, 3)
)
if mibBuilder.loadTexts:
    envCPUsTable.setStatus("current")
_EnvCPUsEntry_Object = MibTableRow
envCPUsEntry = _EnvCPUsEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 5, 3, 1)
)
envCPUsEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "envCpuBoard"),
    (0, "Fore-Switch-MIB", "envCpuSlot"),
)
if mibBuilder.loadTexts:
    envCPUsEntry.setStatus("current")
_EnvCpuBoard_Type = Integer32
_EnvCpuBoard_Object = MibTableColumn
envCpuBoard = _EnvCpuBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 5, 3, 1, 1),
    _EnvCpuBoard_Type()
)
envCpuBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envCpuBoard.setStatus("current")
_EnvCpuSlot_Type = Integer32
_EnvCpuSlot_Object = MibTableColumn
envCpuSlot = _EnvCpuSlot_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 5, 3, 1, 2),
    _EnvCpuSlot_Type()
)
envCpuSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envCpuSlot.setStatus("current")


class _EnvCpuType_Type(Integer32):
    """Custom type envCpuType based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("cpv5000", 11),
          ("i960ca", 5),
          ("i960cf", 6),
          ("i960ha", 7),
          ("i960hd", 8),
          ("other", 1),
          ("p200", 13),
          ("p266", 12),
          ("p55", 9),
          ("p6", 10),
          ("sparc", 4),
          ("sun4c", 3),
          ("sun4e", 2))
    )


_EnvCpuType_Type.__name__ = "Integer32"
_EnvCpuType_Object = MibTableColumn
envCpuType = _EnvCpuType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 5, 3, 1, 3),
    _EnvCpuType_Type()
)
envCpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envCpuType.setStatus("current")


class _EnvCPUState_Type(Integer32):
    """Custom type envCPUState based on Integer32"""
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
        *(("boot", 4),
          ("fail", 2),
          ("normal", 1),
          ("standby", 3))
    )


_EnvCPUState_Type.__name__ = "Integer32"
_EnvCPUState_Object = MibTableColumn
envCPUState = _EnvCPUState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 5, 3, 1, 4),
    _EnvCPUState_Type()
)
envCPUState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envCPUState.setStatus("current")
_EnvCpuDRAMSize_Type = Integer32
_EnvCpuDRAMSize_Object = MibTableColumn
envCpuDRAMSize = _EnvCpuDRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 5, 3, 1, 5),
    _EnvCpuDRAMSize_Type()
)
envCpuDRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envCpuDRAMSize.setStatus("current")
_EnvCpuRevLevel_Type = Integer32
_EnvCpuRevLevel_Object = MibTableColumn
envCpuRevLevel = _EnvCpuRevLevel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 5, 3, 1, 6),
    _EnvCpuRevLevel_Type()
)
envCpuRevLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envCpuRevLevel.setStatus("current")
_EnvCpuFlashSize_Type = Integer32
_EnvCpuFlashSize_Object = MibTableColumn
envCpuFlashSize = _EnvCpuFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 5, 3, 1, 7),
    _EnvCpuFlashSize_Type()
)
envCpuFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envCpuFlashSize.setStatus("current")
_EnvCpuBoardRevision_Type = Integer32
_EnvCpuBoardRevision_Object = MibTableColumn
envCpuBoardRevision = _EnvCpuBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 5, 3, 1, 8),
    _EnvCpuBoardRevision_Type()
)
envCpuBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envCpuBoardRevision.setStatus("current")
_EnvCpuPromRevision_Type = Integer32
_EnvCpuPromRevision_Object = MibTableColumn
envCpuPromRevision = _EnvCpuPromRevision_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 5, 3, 1, 9),
    _EnvCpuPromRevision_Type()
)
envCpuPromRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envCpuPromRevision.setStatus("current")
_EnvCpuMACAddress_Type = PhysAddress
_EnvCpuMACAddress_Object = MibTableColumn
envCpuMACAddress = _EnvCpuMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 5, 3, 1, 10),
    _EnvCpuMACAddress_Type()
)
envCpuMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envCpuMACAddress.setStatus("current")
_EnvCpuSerialNumber_Type = DisplayString
_EnvCpuSerialNumber_Object = MibTableColumn
envCpuSerialNumber = _EnvCpuSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 5, 3, 1, 11),
    _EnvCpuSerialNumber_Type()
)
envCpuSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envCpuSerialNumber.setStatus("current")
_EnvCpuProductPartNumber_Type = DisplayString
_EnvCpuProductPartNumber_Object = MibTableColumn
envCpuProductPartNumber = _EnvCpuProductPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 5, 3, 1, 12),
    _EnvCpuProductPartNumber_Type()
)
envCpuProductPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envCpuProductPartNumber.setStatus("current")
_EnvCpuCLEI_Type = DisplayString
_EnvCpuCLEI_Object = MibTableColumn
envCpuCLEI = _EnvCpuCLEI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 5, 3, 1, 13),
    _EnvCpuCLEI_Type()
)
envCpuCLEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envCpuCLEI.setStatus("current")
_EnvCpuIDESize_Type = Integer32
_EnvCpuIDESize_Object = MibTableColumn
envCpuIDESize = _EnvCpuIDESize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 5, 3, 1, 14),
    _EnvCpuIDESize_Type()
)
envCpuIDESize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envCpuIDESize.setStatus("current")
_MgmtGroup_ObjectIdentity = ObjectIdentity
mgmtGroup = _MgmtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 6)
)
_EnvMgmtBoardType_Type = Integer32
_EnvMgmtBoardType_Object = MibScalar
envMgmtBoardType = _EnvMgmtBoardType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 6, 1),
    _EnvMgmtBoardType_Type()
)
envMgmtBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMgmtBoardType.setStatus("current")
_EnvMgmtBoardRevision_Type = Integer32
_EnvMgmtBoardRevision_Object = MibScalar
envMgmtBoardRevision = _EnvMgmtBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 6, 2),
    _EnvMgmtBoardRevision_Type()
)
envMgmtBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMgmtBoardRevision.setStatus("current")
_EnvMgmtBoardSerialNumber_Type = Integer32
_EnvMgmtBoardSerialNumber_Object = MibScalar
envMgmtBoardSerialNumber = _EnvMgmtBoardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 6, 3),
    _EnvMgmtBoardSerialNumber_Type()
)
envMgmtBoardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMgmtBoardSerialNumber.setStatus("current")
_FabricGroup_ObjectIdentity = ObjectIdentity
fabricGroup = _FabricGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 7)
)
_EnvFabricAlarmTripTemperature_Type = Integer32
_EnvFabricAlarmTripTemperature_Object = MibScalar
envFabricAlarmTripTemperature = _EnvFabricAlarmTripTemperature_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 7, 1),
    _EnvFabricAlarmTripTemperature_Type()
)
envFabricAlarmTripTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envFabricAlarmTripTemperature.setStatus("current")
_EnvFabricAlarmResetTemperature_Type = Integer32
_EnvFabricAlarmResetTemperature_Object = MibScalar
envFabricAlarmResetTemperature = _EnvFabricAlarmResetTemperature_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 7, 2),
    _EnvFabricAlarmResetTemperature_Type()
)
envFabricAlarmResetTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envFabricAlarmResetTemperature.setStatus("current")
_EnvFabricTable_Object = MibTable
envFabricTable = _EnvFabricTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 7, 3)
)
if mibBuilder.loadTexts:
    envFabricTable.setStatus("current")
_EnvFabricEntry_Object = MibTableRow
envFabricEntry = _EnvFabricEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 7, 3, 1)
)
envFabricEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "envFabricIndex"),
)
if mibBuilder.loadTexts:
    envFabricEntry.setStatus("current")
_EnvFabricIndex_Type = Integer32
_EnvFabricIndex_Object = MibTableColumn
envFabricIndex = _EnvFabricIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 7, 3, 1, 1),
    _EnvFabricIndex_Type()
)
envFabricIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envFabricIndex.setStatus("current")
_EnvFabricTemperature_Type = Integer32
_EnvFabricTemperature_Object = MibTableColumn
envFabricTemperature = _EnvFabricTemperature_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 7, 3, 1, 2),
    _EnvFabricTemperature_Type()
)
envFabricTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envFabricTemperature.setStatus("current")


class _EnvFabricTemperatureState_Type(Integer32):
    """Custom type envFabricTemperatureState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("overTemp", 2))
    )


_EnvFabricTemperatureState_Type.__name__ = "Integer32"
_EnvFabricTemperatureState_Object = MibTableColumn
envFabricTemperatureState = _EnvFabricTemperatureState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 4, 7, 3, 1, 3),
    _EnvFabricTemperatureState_Type()
)
envFabricTemperatureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envFabricTemperatureState.setStatus("current")
_Shmem_ObjectIdentity = ObjectIdentity
shmem = _Shmem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5)
)
_NetmodShmemGroup_ObjectIdentity = ObjectIdentity
netmodShmemGroup = _NetmodShmemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 1)
)
_ShmemConfTable_Object = MibTable
shmemConfTable = _ShmemConfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    shmemConfTable.setStatus("current")
_ShmemConfEntry_Object = MibTableRow
shmemConfEntry = _ShmemConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 1, 1, 1)
)
shmemConfEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "shmemConfIndex"),
)
if mibBuilder.loadTexts:
    shmemConfEntry.setStatus("current")
_ShmemConfIndex_Type = Integer32
_ShmemConfIndex_Object = MibTableColumn
shmemConfIndex = _ShmemConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 1, 1, 1, 1),
    _ShmemConfIndex_Type()
)
shmemConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmemConfIndex.setStatus("current")
_ShmemUcastConnections_Type = Integer32
_ShmemUcastConnections_Object = MibTableColumn
shmemUcastConnections = _ShmemUcastConnections_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 1, 1, 1, 2),
    _ShmemUcastConnections_Type()
)
shmemUcastConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmemUcastConnections.setStatus("current")
_ShmemMcastConnections_Type = Integer32
_ShmemMcastConnections_Object = MibTableColumn
shmemMcastConnections = _ShmemMcastConnections_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 1, 1, 1, 3),
    _ShmemMcastConnections_Type()
)
shmemMcastConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmemMcastConnections.setStatus("current")
_ShmemVpiVciLists_Type = Integer32
_ShmemVpiVciLists_Object = MibTableColumn
shmemVpiVciLists = _ShmemVpiVciLists_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 1, 1, 1, 4),
    _ShmemVpiVciLists_Type()
)
shmemVpiVciLists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmemVpiVciLists.setStatus("current")
_ShmemCellsBuffers_Type = Integer32
_ShmemCellsBuffers_Object = MibTableColumn
shmemCellsBuffers = _ShmemCellsBuffers_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 1, 1, 1, 5),
    _ShmemCellsBuffers_Type()
)
shmemCellsBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmemCellsBuffers.setStatus("current")
_ShmemConfName_Type = DisplayString
_ShmemConfName_Object = MibTableColumn
shmemConfName = _ShmemConfName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 1, 1, 1, 6),
    _ShmemConfName_Type()
)
shmemConfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmemConfName.setStatus("current")
_ShmemMemorySize_Type = Integer32
_ShmemMemorySize_Object = MibTableColumn
shmemMemorySize = _ShmemMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 1, 1, 1, 7),
    _ShmemMemorySize_Type()
)
shmemMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmemMemorySize.setStatus("current")
_NetmodShmemTable_Object = MibTable
netmodShmemTable = _NetmodShmemTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    netmodShmemTable.setStatus("current")
_NetmodShmemEntry_Object = MibTableRow
netmodShmemEntry = _NetmodShmemEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 1, 2, 1)
)
netmodShmemEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "nshmemBoard"),
    (0, "Fore-Switch-MIB", "nshmemModule"),
)
if mibBuilder.loadTexts:
    netmodShmemEntry.setStatus("current")
_NshmemBoard_Type = Integer32
_NshmemBoard_Object = MibTableColumn
nshmemBoard = _NshmemBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 1, 2, 1, 1),
    _NshmemBoard_Type()
)
nshmemBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nshmemBoard.setStatus("current")
_NshmemModule_Type = Integer32
_NshmemModule_Object = MibTableColumn
nshmemModule = _NshmemModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 1, 2, 1, 2),
    _NshmemModule_Type()
)
nshmemModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nshmemModule.setStatus("current")
_NshmemConfRow_Type = Integer32
_NshmemConfRow_Object = MibTableColumn
nshmemConfRow = _NshmemConfRow_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 1, 2, 1, 3),
    _NshmemConfRow_Type()
)
nshmemConfRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nshmemConfRow.setStatus("current")
_NshmemConfSharedMemory_Type = Integer32
_NshmemConfSharedMemory_Object = MibTableColumn
nshmemConfSharedMemory = _NshmemConfSharedMemory_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 1, 2, 1, 4),
    _NshmemConfSharedMemory_Type()
)
nshmemConfSharedMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nshmemConfSharedMemory.setStatus("current")
_NshmemCurrentUcastConnections_Type = Gauge32
_NshmemCurrentUcastConnections_Object = MibTableColumn
nshmemCurrentUcastConnections = _NshmemCurrentUcastConnections_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 1, 2, 1, 5),
    _NshmemCurrentUcastConnections_Type()
)
nshmemCurrentUcastConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nshmemCurrentUcastConnections.setStatus("current")
_NshmemCurrentMcastConnections_Type = Gauge32
_NshmemCurrentMcastConnections_Object = MibTableColumn
nshmemCurrentMcastConnections = _NshmemCurrentMcastConnections_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 1, 2, 1, 6),
    _NshmemCurrentMcastConnections_Type()
)
nshmemCurrentMcastConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nshmemCurrentMcastConnections.setStatus("current")
_NshmemCurrentVpiVciLists_Type = Gauge32
_NshmemCurrentVpiVciLists_Object = MibTableColumn
nshmemCurrentVpiVciLists = _NshmemCurrentVpiVciLists_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 1, 2, 1, 7),
    _NshmemCurrentVpiVciLists_Type()
)
nshmemCurrentVpiVciLists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nshmemCurrentVpiVciLists.setStatus("current")
_NshmemCurrentCellsBuffers_Type = Gauge32
_NshmemCurrentCellsBuffers_Object = MibTableColumn
nshmemCurrentCellsBuffers = _NshmemCurrentCellsBuffers_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 1, 2, 1, 8),
    _NshmemCurrentCellsBuffers_Type()
)
nshmemCurrentCellsBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nshmemCurrentCellsBuffers.setStatus("current")
_NshmemCurrentSharedMemory_Type = Gauge32
_NshmemCurrentSharedMemory_Object = MibTableColumn
nshmemCurrentSharedMemory = _NshmemCurrentSharedMemory_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 1, 2, 1, 9),
    _NshmemCurrentSharedMemory_Type()
)
nshmemCurrentSharedMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nshmemCurrentSharedMemory.setStatus("current")
_NshmemConfAal5PacketDrop_Type = Integer32
_NshmemConfAal5PacketDrop_Object = MibTableColumn
nshmemConfAal5PacketDrop = _NshmemConfAal5PacketDrop_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 1, 2, 1, 10),
    _NshmemConfAal5PacketDrop_Type()
)
nshmemConfAal5PacketDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nshmemConfAal5PacketDrop.setStatus("current")


class _NshmemAssertXACPT_Type(Integer32):
    """Custom type nshmemAssertXACPT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("assertXACPT", 2),
          ("clearXACPT", 1))
    )


_NshmemAssertXACPT_Type.__name__ = "Integer32"
_NshmemAssertXACPT_Object = MibTableColumn
nshmemAssertXACPT = _NshmemAssertXACPT_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 1, 2, 1, 11),
    _NshmemAssertXACPT_Type()
)
nshmemAssertXACPT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nshmemAssertXACPT.setStatus("current")
_NshmemMemorySize_Type = Integer32
_NshmemMemorySize_Object = MibTableColumn
nshmemMemorySize = _NshmemMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 1, 2, 1, 12),
    _NshmemMemorySize_Type()
)
nshmemMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nshmemMemorySize.setStatus("current")
_PortShmemGroup_ObjectIdentity = ObjectIdentity
portShmemGroup = _PortShmemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 2)
)
_PortShmemConfTable_Object = MibTable
portShmemConfTable = _PortShmemConfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    portShmemConfTable.setStatus("current")
_PortShmemConfEntry_Object = MibTableRow
portShmemConfEntry = _PortShmemConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 2, 1, 1)
)
portShmemConfEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "pshmemConfBoard"),
    (0, "Fore-Switch-MIB", "pshmemConfModule"),
    (0, "Fore-Switch-MIB", "pshmemConfPort"),
)
if mibBuilder.loadTexts:
    portShmemConfEntry.setStatus("current")
_PshmemConfBoard_Type = Integer32
_PshmemConfBoard_Object = MibTableColumn
pshmemConfBoard = _PshmemConfBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 2, 1, 1, 1),
    _PshmemConfBoard_Type()
)
pshmemConfBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pshmemConfBoard.setStatus("current")
_PshmemConfModule_Type = Integer32
_PshmemConfModule_Object = MibTableColumn
pshmemConfModule = _PshmemConfModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 2, 1, 1, 2),
    _PshmemConfModule_Type()
)
pshmemConfModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pshmemConfModule.setStatus("current")
_PshmemConfPort_Type = Integer32
_PshmemConfPort_Object = MibTableColumn
pshmemConfPort = _PshmemConfPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 2, 1, 1, 3),
    _PshmemConfPort_Type()
)
pshmemConfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pshmemConfPort.setStatus("current")
_PshmemMaxCDVforCBR_Type = Integer32
_PshmemMaxCDVforCBR_Object = MibTableColumn
pshmemMaxCDVforCBR = _PshmemMaxCDVforCBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 2, 1, 1, 4),
    _PshmemMaxCDVforCBR_Type()
)
pshmemMaxCDVforCBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pshmemMaxCDVforCBR.setStatus("current")
_PshmemMaxCDVforVBR_Type = Integer32
_PshmemMaxCDVforVBR_Object = MibTableColumn
pshmemMaxCDVforVBR = _PshmemMaxCDVforVBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 2, 1, 1, 5),
    _PshmemMaxCDVforVBR_Type()
)
pshmemMaxCDVforVBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pshmemMaxCDVforVBR.setStatus("current")
_PshmemQsizeforABR_Type = Integer32
_PshmemQsizeforABR_Object = MibTableColumn
pshmemQsizeforABR = _PshmemQsizeforABR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 2, 1, 1, 6),
    _PshmemQsizeforABR_Type()
)
pshmemQsizeforABR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pshmemQsizeforABR.setStatus("current")
_PshmemEfciOnABR_Type = Integer32
_PshmemEfciOnABR_Object = MibTableColumn
pshmemEfciOnABR = _PshmemEfciOnABR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 2, 1, 1, 7),
    _PshmemEfciOnABR_Type()
)
pshmemEfciOnABR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pshmemEfciOnABR.setStatus("current")
_PshmemEfciOffABR_Type = Integer32
_PshmemEfciOffABR_Object = MibTableColumn
pshmemEfciOffABR = _PshmemEfciOffABR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 2, 1, 1, 8),
    _PshmemEfciOffABR_Type()
)
pshmemEfciOffABR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pshmemEfciOffABR.setStatus("current")
_PshmemQsizeforCBR_Type = Integer32
_PshmemQsizeforCBR_Object = MibTableColumn
pshmemQsizeforCBR = _PshmemQsizeforCBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 2, 1, 1, 9),
    _PshmemQsizeforCBR_Type()
)
pshmemQsizeforCBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pshmemQsizeforCBR.setStatus("current")
_PshmemQsizeforVBR_Type = Integer32
_PshmemQsizeforVBR_Object = MibTableColumn
pshmemQsizeforVBR = _PshmemQsizeforVBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 2, 1, 1, 10),
    _PshmemQsizeforVBR_Type()
)
pshmemQsizeforVBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pshmemQsizeforVBR.setStatus("current")
_PshmemClpThreshforCBR_Type = Integer32
_PshmemClpThreshforCBR_Object = MibTableColumn
pshmemClpThreshforCBR = _PshmemClpThreshforCBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 2, 1, 1, 11),
    _PshmemClpThreshforCBR_Type()
)
pshmemClpThreshforCBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pshmemClpThreshforCBR.setStatus("current")
_PshmemClpThreshforVBR_Type = Integer32
_PshmemClpThreshforVBR_Object = MibTableColumn
pshmemClpThreshforVBR = _PshmemClpThreshforVBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 2, 1, 1, 12),
    _PshmemClpThreshforVBR_Type()
)
pshmemClpThreshforVBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pshmemClpThreshforVBR.setStatus("current")
_PshmemClpThreshforABR_Type = Integer32
_PshmemClpThreshforABR_Object = MibTableColumn
pshmemClpThreshforABR = _PshmemClpThreshforABR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 2, 1, 1, 13),
    _PshmemClpThreshforABR_Type()
)
pshmemClpThreshforABR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pshmemClpThreshforABR.setStatus("current")
_PShmemAtmInterfaceIndex_Type = Integer32
_PShmemAtmInterfaceIndex_Object = MibTableColumn
pShmemAtmInterfaceIndex = _PShmemAtmInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 2, 1, 1, 14),
    _PShmemAtmInterfaceIndex_Type()
)
pShmemAtmInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmemAtmInterfaceIndex.setStatus("current")
_PortShmemTable_Object = MibTable
portShmemTable = _PortShmemTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    portShmemTable.setStatus("current")
_PortShmemEntry_Object = MibTableRow
portShmemEntry = _PortShmemEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 2, 2, 1)
)
portShmemEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "pshmemBoard"),
    (0, "Fore-Switch-MIB", "pshmemModule"),
    (0, "Fore-Switch-MIB", "pshmemPort"),
    (0, "Fore-Switch-MIB", "pshmemPriority"),
)
if mibBuilder.loadTexts:
    portShmemEntry.setStatus("current")
_PshmemBoard_Type = Integer32
_PshmemBoard_Object = MibTableColumn
pshmemBoard = _PshmemBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 2, 2, 1, 1),
    _PshmemBoard_Type()
)
pshmemBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pshmemBoard.setStatus("current")
_PshmemModule_Type = Integer32
_PshmemModule_Object = MibTableColumn
pshmemModule = _PshmemModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 2, 2, 1, 2),
    _PshmemModule_Type()
)
pshmemModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pshmemModule.setStatus("current")
_PshmemPort_Type = Integer32
_PshmemPort_Object = MibTableColumn
pshmemPort = _PshmemPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 2, 2, 1, 3),
    _PshmemPort_Type()
)
pshmemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pshmemPort.setStatus("current")


class _PshmemPriority_Type(Integer32):
    """Custom type pshmemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("priorityCBR", 3),
          ("priorityUBR-ABR", 1),
          ("priorityVBR", 2))
    )


_PshmemPriority_Type.__name__ = "Integer32"
_PshmemPriority_Object = MibTableColumn
pshmemPriority = _PshmemPriority_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 2, 2, 1, 4),
    _PshmemPriority_Type()
)
pshmemPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pshmemPriority.setStatus("current")
_PshmemClpThreshold_Type = Integer32
_PshmemClpThreshold_Object = MibTableColumn
pshmemClpThreshold = _PshmemClpThreshold_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 2, 2, 1, 5),
    _PshmemClpThreshold_Type()
)
pshmemClpThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pshmemClpThreshold.setStatus("current")
_PshmemDedicatedQsize_Type = Integer32
_PshmemDedicatedQsize_Object = MibTableColumn
pshmemDedicatedQsize = _PshmemDedicatedQsize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 2, 2, 1, 6),
    _PshmemDedicatedQsize_Type()
)
pshmemDedicatedQsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pshmemDedicatedQsize.setStatus("current")
_PshmemCurrentQsize_Type = Integer32
_PshmemCurrentQsize_Object = MibTableColumn
pshmemCurrentQsize = _PshmemCurrentQsize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 2, 2, 1, 7),
    _PshmemCurrentQsize_Type()
)
pshmemCurrentQsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pshmemCurrentQsize.setStatus("current")
_PshmemTxCells_Type = Counter32
_PshmemTxCells_Object = MibTableColumn
pshmemTxCells = _PshmemTxCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 2, 2, 1, 8),
    _PshmemTxCells_Type()
)
pshmemTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pshmemTxCells.setStatus("current")
_PshmemLostCells_Type = Counter32
_PshmemLostCells_Object = MibTableColumn
pshmemLostCells = _PshmemLostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 2, 2, 1, 9),
    _PshmemLostCells_Type()
)
pshmemLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pshmemLostCells.setStatus("current")
_NetmodShmem2Group_ObjectIdentity = ObjectIdentity
netmodShmem2Group = _NetmodShmem2Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3)
)
_Shmem2ConfTable_Object = MibTable
shmem2ConfTable = _Shmem2ConfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 1)
)
if mibBuilder.loadTexts:
    shmem2ConfTable.setStatus("current")
_Shmem2ConfEntry_Object = MibTableRow
shmem2ConfEntry = _Shmem2ConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 1, 1)
)
shmem2ConfEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "shmem2ConfIndex"),
)
if mibBuilder.loadTexts:
    shmem2ConfEntry.setStatus("current")
_Shmem2ConfIndex_Type = Integer32
_Shmem2ConfIndex_Object = MibTableColumn
shmem2ConfIndex = _Shmem2ConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 1, 1, 1),
    _Shmem2ConfIndex_Type()
)
shmem2ConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmem2ConfIndex.setStatus("current")
_Shmem2UcastConnections_Type = Integer32
_Shmem2UcastConnections_Object = MibTableColumn
shmem2UcastConnections = _Shmem2UcastConnections_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 1, 1, 2),
    _Shmem2UcastConnections_Type()
)
shmem2UcastConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmem2UcastConnections.setStatus("current")
_Shmem2McastConnections_Type = Integer32
_Shmem2McastConnections_Object = MibTableColumn
shmem2McastConnections = _Shmem2McastConnections_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 1, 1, 3),
    _Shmem2McastConnections_Type()
)
shmem2McastConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmem2McastConnections.setStatus("current")
_Shmem2CellsBuffers_Type = Integer32
_Shmem2CellsBuffers_Object = MibTableColumn
shmem2CellsBuffers = _Shmem2CellsBuffers_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 1, 1, 4),
    _Shmem2CellsBuffers_Type()
)
shmem2CellsBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmem2CellsBuffers.setStatus("current")
_Shmem2ConfName_Type = DisplayString
_Shmem2ConfName_Object = MibTableColumn
shmem2ConfName = _Shmem2ConfName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 1, 1, 5),
    _Shmem2ConfName_Type()
)
shmem2ConfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmem2ConfName.setStatus("current")
_Shmem2Counters_Type = Integer32
_Shmem2Counters_Object = MibTableColumn
shmem2Counters = _Shmem2Counters_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 1, 1, 6),
    _Shmem2Counters_Type()
)
shmem2Counters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmem2Counters.setStatus("current")
_Shmem2CellMemorySize_Type = Integer32
_Shmem2CellMemorySize_Object = MibTableColumn
shmem2CellMemorySize = _Shmem2CellMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 1, 1, 7),
    _Shmem2CellMemorySize_Type()
)
shmem2CellMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmem2CellMemorySize.setStatus("current")
_Shmem2TableMemorySize_Type = Integer32
_Shmem2TableMemorySize_Object = MibTableColumn
shmem2TableMemorySize = _Shmem2TableMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 1, 1, 8),
    _Shmem2TableMemorySize_Type()
)
shmem2TableMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmem2TableMemorySize.setStatus("current")
_Shmem2NumPriorities_Type = Integer32
_Shmem2NumPriorities_Object = MibTableColumn
shmem2NumPriorities = _Shmem2NumPriorities_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 1, 1, 9),
    _Shmem2NumPriorities_Type()
)
shmem2NumPriorities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmem2NumPriorities.setStatus("current")
_NetmodShmem2Table_Object = MibTable
netmodShmem2Table = _NetmodShmem2Table_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 2)
)
if mibBuilder.loadTexts:
    netmodShmem2Table.setStatus("current")
_NetmodShmem2Entry_Object = MibTableRow
netmodShmem2Entry = _NetmodShmem2Entry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 2, 1)
)
netmodShmem2Entry.setIndexNames(
    (0, "Fore-Switch-MIB", "nShmem2Board"),
    (0, "Fore-Switch-MIB", "nShmem2Module"),
)
if mibBuilder.loadTexts:
    netmodShmem2Entry.setStatus("current")
_NShmem2Board_Type = Integer32
_NShmem2Board_Object = MibTableColumn
nShmem2Board = _NShmem2Board_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 2, 1, 1),
    _NShmem2Board_Type()
)
nShmem2Board.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nShmem2Board.setStatus("current")
_NShmem2Module_Type = Integer32
_NShmem2Module_Object = MibTableColumn
nShmem2Module = _NShmem2Module_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 2, 1, 2),
    _NShmem2Module_Type()
)
nShmem2Module.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nShmem2Module.setStatus("current")
_NShmem2ConfRow_Type = Integer32
_NShmem2ConfRow_Object = MibTableColumn
nShmem2ConfRow = _NShmem2ConfRow_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 2, 1, 3),
    _NShmem2ConfRow_Type()
)
nShmem2ConfRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem2ConfRow.setStatus("current")
_NShmem2ConfSharedMemory_Type = Integer32
_NShmem2ConfSharedMemory_Object = MibTableColumn
nShmem2ConfSharedMemory = _NShmem2ConfSharedMemory_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 2, 1, 4),
    _NShmem2ConfSharedMemory_Type()
)
nShmem2ConfSharedMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nShmem2ConfSharedMemory.setStatus("current")
_NShmem2CurrentUcastConnections_Type = Gauge32
_NShmem2CurrentUcastConnections_Object = MibTableColumn
nShmem2CurrentUcastConnections = _NShmem2CurrentUcastConnections_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 2, 1, 5),
    _NShmem2CurrentUcastConnections_Type()
)
nShmem2CurrentUcastConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nShmem2CurrentUcastConnections.setStatus("current")
_NShmem2CurrentMcastConnections_Type = Gauge32
_NShmem2CurrentMcastConnections_Object = MibTableColumn
nShmem2CurrentMcastConnections = _NShmem2CurrentMcastConnections_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 2, 1, 6),
    _NShmem2CurrentMcastConnections_Type()
)
nShmem2CurrentMcastConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nShmem2CurrentMcastConnections.setStatus("current")
_NShmem2CurrentCellsBuffers_Type = Gauge32
_NShmem2CurrentCellsBuffers_Object = MibTableColumn
nShmem2CurrentCellsBuffers = _NShmem2CurrentCellsBuffers_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 2, 1, 7),
    _NShmem2CurrentCellsBuffers_Type()
)
nShmem2CurrentCellsBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nShmem2CurrentCellsBuffers.setStatus("current")
_NShmem2CurrentSharedMemory_Type = Gauge32
_NShmem2CurrentSharedMemory_Object = MibTableColumn
nShmem2CurrentSharedMemory = _NShmem2CurrentSharedMemory_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 2, 1, 8),
    _NShmem2CurrentSharedMemory_Type()
)
nShmem2CurrentSharedMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nShmem2CurrentSharedMemory.setStatus("current")
_NShmem2ConfAal5PacketDrop_Type = Integer32
_NShmem2ConfAal5PacketDrop_Object = MibTableColumn
nShmem2ConfAal5PacketDrop = _NShmem2ConfAal5PacketDrop_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 2, 1, 9),
    _NShmem2ConfAal5PacketDrop_Type()
)
nShmem2ConfAal5PacketDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem2ConfAal5PacketDrop.setStatus("current")
_NShmem2ConfAal5PacketDropforUBR_Type = Integer32
_NShmem2ConfAal5PacketDropforUBR_Object = MibTableColumn
nShmem2ConfAal5PacketDropforUBR = _NShmem2ConfAal5PacketDropforUBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 2, 1, 10),
    _NShmem2ConfAal5PacketDropforUBR_Type()
)
nShmem2ConfAal5PacketDropforUBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem2ConfAal5PacketDropforUBR.setStatus("current")
_NShmem2ConfEfciOn_Type = Integer32
_NShmem2ConfEfciOn_Object = MibTableColumn
nShmem2ConfEfciOn = _NShmem2ConfEfciOn_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 2, 1, 11),
    _NShmem2ConfEfciOn_Type()
)
nShmem2ConfEfciOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem2ConfEfciOn.setStatus("current")
_NShmem2ConfEfciOff_Type = Integer32
_NShmem2ConfEfciOff_Object = MibTableColumn
nShmem2ConfEfciOff = _NShmem2ConfEfciOff_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 2, 1, 12),
    _NShmem2ConfEfciOff_Type()
)
nShmem2ConfEfciOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem2ConfEfciOff.setStatus("current")
_NShmem2CellMemorySize_Type = Integer32
_NShmem2CellMemorySize_Object = MibTableColumn
nShmem2CellMemorySize = _NShmem2CellMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 2, 1, 13),
    _NShmem2CellMemorySize_Type()
)
nShmem2CellMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nShmem2CellMemorySize.setStatus("current")
_NShmem2TableMemorySize_Type = Integer32
_NShmem2TableMemorySize_Object = MibTableColumn
nShmem2TableMemorySize = _NShmem2TableMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 2, 1, 14),
    _NShmem2TableMemorySize_Type()
)
nShmem2TableMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nShmem2TableMemorySize.setStatus("current")
_NShmem2NumPriorities_Type = Integer32
_NShmem2NumPriorities_Object = MibTableColumn
nShmem2NumPriorities = _NShmem2NumPriorities_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 2, 1, 15),
    _NShmem2NumPriorities_Type()
)
nShmem2NumPriorities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nShmem2NumPriorities.setStatus("current")


class _NShmem2VBRPriority_Type(Integer32):
    """Custom type nShmem2VBRPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("priorityNrt", 2),
          ("priorityRt", 1),
          ("unSupported", 3))
    )


_NShmem2VBRPriority_Type.__name__ = "Integer32"
_NShmem2VBRPriority_Object = MibTableColumn
nShmem2VBRPriority = _NShmem2VBRPriority_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 2, 1, 16),
    _NShmem2VBRPriority_Type()
)
nShmem2VBRPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem2VBRPriority.setStatus("current")
_NetmodShmem2CustomBCSTable_Object = MibTable
netmodShmem2CustomBCSTable = _NetmodShmem2CustomBCSTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 3)
)
if mibBuilder.loadTexts:
    netmodShmem2CustomBCSTable.setStatus("current")
_NetmodShmem2CustomBCSEntry_Object = MibTableRow
netmodShmem2CustomBCSEntry = _NetmodShmem2CustomBCSEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 3, 1)
)
netmodShmem2CustomBCSEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "nShmem2CustomBCSBoard"),
    (0, "Fore-Switch-MIB", "nShmem2CustomBCSModule"),
    (0, "Fore-Switch-MIB", "nShmem2CustomBCSValue"),
)
if mibBuilder.loadTexts:
    netmodShmem2CustomBCSEntry.setStatus("current")
_NShmem2CustomBCSBoard_Type = Integer32
_NShmem2CustomBCSBoard_Object = MibTableColumn
nShmem2CustomBCSBoard = _NShmem2CustomBCSBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 3, 1, 1),
    _NShmem2CustomBCSBoard_Type()
)
nShmem2CustomBCSBoard.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nShmem2CustomBCSBoard.setStatus("current")
_NShmem2CustomBCSModule_Type = Integer32
_NShmem2CustomBCSModule_Object = MibTableColumn
nShmem2CustomBCSModule = _NShmem2CustomBCSModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 3, 1, 2),
    _NShmem2CustomBCSModule_Type()
)
nShmem2CustomBCSModule.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nShmem2CustomBCSModule.setStatus("current")
_NShmem2CustomBCSValue_Type = Integer32
_NShmem2CustomBCSValue_Object = MibTableColumn
nShmem2CustomBCSValue = _NShmem2CustomBCSValue_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 3, 1, 3),
    _NShmem2CustomBCSValue_Type()
)
nShmem2CustomBCSValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nShmem2CustomBCSValue.setStatus("current")
_NShmem2CustomBCSWeight_Type = Integer32
_NShmem2CustomBCSWeight_Object = MibTableColumn
nShmem2CustomBCSWeight = _NShmem2CustomBCSWeight_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 3, 1, 4),
    _NShmem2CustomBCSWeight_Type()
)
nShmem2CustomBCSWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem2CustomBCSWeight.setStatus("current")
_NShmem2CustomBCSRowStatus_Type = RowStatus
_NShmem2CustomBCSRowStatus_Object = MibTableColumn
nShmem2CustomBCSRowStatus = _NShmem2CustomBCSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 3, 3, 1, 5),
    _NShmem2CustomBCSRowStatus_Type()
)
nShmem2CustomBCSRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem2CustomBCSRowStatus.setStatus("current")
_PortShmem2Group_ObjectIdentity = ObjectIdentity
portShmem2Group = _PortShmem2Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4)
)
_PortShmem2ConfTable_Object = MibTable
portShmem2ConfTable = _PortShmem2ConfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 1)
)
if mibBuilder.loadTexts:
    portShmem2ConfTable.setStatus("current")
_PortShmem2ConfEntry_Object = MibTableRow
portShmem2ConfEntry = _PortShmem2ConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 1, 1)
)
portShmem2ConfEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "pShmem2ConfBoard"),
    (0, "Fore-Switch-MIB", "pShmem2ConfModule"),
    (0, "Fore-Switch-MIB", "pShmem2ConfPort"),
)
if mibBuilder.loadTexts:
    portShmem2ConfEntry.setStatus("current")
_PShmem2ConfBoard_Type = Integer32
_PShmem2ConfBoard_Object = MibTableColumn
pShmem2ConfBoard = _PShmem2ConfBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 1, 1, 1),
    _PShmem2ConfBoard_Type()
)
pShmem2ConfBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem2ConfBoard.setStatus("current")
_PShmem2ConfModule_Type = Integer32
_PShmem2ConfModule_Object = MibTableColumn
pShmem2ConfModule = _PShmem2ConfModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 1, 1, 2),
    _PShmem2ConfModule_Type()
)
pShmem2ConfModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem2ConfModule.setStatus("current")
_PShmem2ConfPort_Type = Integer32
_PShmem2ConfPort_Object = MibTableColumn
pShmem2ConfPort = _PShmem2ConfPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 1, 1, 3),
    _PShmem2ConfPort_Type()
)
pShmem2ConfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem2ConfPort.setStatus("current")
_PShmem2QsizeforCBR_Type = Integer32
_PShmem2QsizeforCBR_Object = MibTableColumn
pShmem2QsizeforCBR = _PShmem2QsizeforCBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 1, 1, 4),
    _PShmem2QsizeforCBR_Type()
)
pShmem2QsizeforCBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pShmem2QsizeforCBR.setStatus("deprecated")
_PShmem2QsizeforVBR_Type = Integer32
_PShmem2QsizeforVBR_Object = MibTableColumn
pShmem2QsizeforVBR = _PShmem2QsizeforVBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 1, 1, 5),
    _PShmem2QsizeforVBR_Type()
)
pShmem2QsizeforVBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pShmem2QsizeforVBR.setStatus("deprecated")
_PShmem2QsizeforABR_Type = Integer32
_PShmem2QsizeforABR_Object = MibTableColumn
pShmem2QsizeforABR = _PShmem2QsizeforABR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 1, 1, 6),
    _PShmem2QsizeforABR_Type()
)
pShmem2QsizeforABR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pShmem2QsizeforABR.setStatus("deprecated")
_PShmem2QsizeforUBR_Type = Integer32
_PShmem2QsizeforUBR_Object = MibTableColumn
pShmem2QsizeforUBR = _PShmem2QsizeforUBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 1, 1, 7),
    _PShmem2QsizeforUBR_Type()
)
pShmem2QsizeforUBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pShmem2QsizeforUBR.setStatus("deprecated")
_PShmem2ClpThreshforCBR_Type = Integer32
_PShmem2ClpThreshforCBR_Object = MibTableColumn
pShmem2ClpThreshforCBR = _PShmem2ClpThreshforCBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 1, 1, 8),
    _PShmem2ClpThreshforCBR_Type()
)
pShmem2ClpThreshforCBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pShmem2ClpThreshforCBR.setStatus("deprecated")
_PShmem2ClpThreshforVBR_Type = Integer32
_PShmem2ClpThreshforVBR_Object = MibTableColumn
pShmem2ClpThreshforVBR = _PShmem2ClpThreshforVBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 1, 1, 9),
    _PShmem2ClpThreshforVBR_Type()
)
pShmem2ClpThreshforVBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pShmem2ClpThreshforVBR.setStatus("deprecated")
_PShmem2ClpThreshforABR_Type = Integer32
_PShmem2ClpThreshforABR_Object = MibTableColumn
pShmem2ClpThreshforABR = _PShmem2ClpThreshforABR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 1, 1, 10),
    _PShmem2ClpThreshforABR_Type()
)
pShmem2ClpThreshforABR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pShmem2ClpThreshforABR.setStatus("deprecated")
_PShmem2ClpThreshforUBR_Type = Integer32
_PShmem2ClpThreshforUBR_Object = MibTableColumn
pShmem2ClpThreshforUBR = _PShmem2ClpThreshforUBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 1, 1, 11),
    _PShmem2ClpThreshforUBR_Type()
)
pShmem2ClpThreshforUBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pShmem2ClpThreshforUBR.setStatus("deprecated")
_PShmem2AtmInterfaceIndex_Type = Integer32
_PShmem2AtmInterfaceIndex_Object = MibTableColumn
pShmem2AtmInterfaceIndex = _PShmem2AtmInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 1, 1, 12),
    _PShmem2AtmInterfaceIndex_Type()
)
pShmem2AtmInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem2AtmInterfaceIndex.setStatus("current")
_PortShmem2Table_Object = MibTable
portShmem2Table = _PortShmem2Table_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 2)
)
if mibBuilder.loadTexts:
    portShmem2Table.setStatus("current")
_PortShmem2Entry_Object = MibTableRow
portShmem2Entry = _PortShmem2Entry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 2, 1)
)
portShmem2Entry.setIndexNames(
    (0, "Fore-Switch-MIB", "pShmem2Board"),
    (0, "Fore-Switch-MIB", "pShmem2Module"),
    (0, "Fore-Switch-MIB", "pShmem2Port"),
    (0, "Fore-Switch-MIB", "pShmem2Priority"),
)
if mibBuilder.loadTexts:
    portShmem2Entry.setStatus("current")
_PShmem2Board_Type = Integer32
_PShmem2Board_Object = MibTableColumn
pShmem2Board = _PShmem2Board_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 2, 1, 1),
    _PShmem2Board_Type()
)
pShmem2Board.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem2Board.setStatus("current")
_PShmem2Module_Type = Integer32
_PShmem2Module_Object = MibTableColumn
pShmem2Module = _PShmem2Module_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 2, 1, 2),
    _PShmem2Module_Type()
)
pShmem2Module.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem2Module.setStatus("current")
_PShmem2Port_Type = Integer32
_PShmem2Port_Object = MibTableColumn
pShmem2Port = _PShmem2Port_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 2, 1, 3),
    _PShmem2Port_Type()
)
pShmem2Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem2Port.setStatus("current")


class _PShmem2Priority_Type(Integer32):
    """Custom type pShmem2Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("priorityABR", 1),
          ("priorityCBR", 3),
          ("priorityNrt", 6),
          ("priorityRt", 5),
          ("priorityUBR", 4),
          ("priorityVBR", 2))
    )


_PShmem2Priority_Type.__name__ = "Integer32"
_PShmem2Priority_Object = MibTableColumn
pShmem2Priority = _PShmem2Priority_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 2, 1, 4),
    _PShmem2Priority_Type()
)
pShmem2Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem2Priority.setStatus("current")
_PShmem2ClpThreshold_Type = Integer32
_PShmem2ClpThreshold_Object = MibTableColumn
pShmem2ClpThreshold = _PShmem2ClpThreshold_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 2, 1, 5),
    _PShmem2ClpThreshold_Type()
)
pShmem2ClpThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem2ClpThreshold.setStatus("current")
_PShmem2DedicatedQsize_Type = Integer32
_PShmem2DedicatedQsize_Object = MibTableColumn
pShmem2DedicatedQsize = _PShmem2DedicatedQsize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 2, 1, 6),
    _PShmem2DedicatedQsize_Type()
)
pShmem2DedicatedQsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem2DedicatedQsize.setStatus("current")
_PShmem2CurrentQsize_Type = Integer32
_PShmem2CurrentQsize_Object = MibTableColumn
pShmem2CurrentQsize = _PShmem2CurrentQsize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 2, 1, 7),
    _PShmem2CurrentQsize_Type()
)
pShmem2CurrentQsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem2CurrentQsize.setStatus("current")
_PShmem2TxCells_Type = Counter32
_PShmem2TxCells_Object = MibTableColumn
pShmem2TxCells = _PShmem2TxCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 2, 1, 8),
    _PShmem2TxCells_Type()
)
pShmem2TxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem2TxCells.setStatus("current")
_PShmem2LostCells_Type = Counter32
_PShmem2LostCells_Object = MibTableColumn
pShmem2LostCells = _PShmem2LostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 2, 1, 9),
    _PShmem2LostCells_Type()
)
pShmem2LostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem2LostCells.setStatus("current")
_PShmem2IntentionalLostCells_Type = Counter32
_PShmem2IntentionalLostCells_Object = MibTableColumn
pShmem2IntentionalLostCells = _PShmem2IntentionalLostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 2, 1, 10),
    _PShmem2IntentionalLostCells_Type()
)
pShmem2IntentionalLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem2IntentionalLostCells.setStatus("current")
_PShmem2UnintentionalLostCells_Type = Counter32
_PShmem2UnintentionalLostCells_Object = MibTableColumn
pShmem2UnintentionalLostCells = _PShmem2UnintentionalLostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 2, 1, 11),
    _PShmem2UnintentionalLostCells_Type()
)
pShmem2UnintentionalLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem2UnintentionalLostCells.setStatus("current")
_PortPriorityShmem2ConfTable_Object = MibTable
portPriorityShmem2ConfTable = _PortPriorityShmem2ConfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 3)
)
if mibBuilder.loadTexts:
    portPriorityShmem2ConfTable.setStatus("current")
_PortPriorityShmem2ConfEntry_Object = MibTableRow
portPriorityShmem2ConfEntry = _PortPriorityShmem2ConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 3, 1)
)
portPriorityShmem2ConfEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "ppShmem2ConfBoard"),
    (0, "Fore-Switch-MIB", "ppShmem2ConfModule"),
    (0, "Fore-Switch-MIB", "ppShmem2ConfPort"),
    (0, "Fore-Switch-MIB", "ppShmem2ConfPriority"),
)
if mibBuilder.loadTexts:
    portPriorityShmem2ConfEntry.setStatus("current")
_PpShmem2ConfBoard_Type = Integer32
_PpShmem2ConfBoard_Object = MibTableColumn
ppShmem2ConfBoard = _PpShmem2ConfBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 3, 1, 1),
    _PpShmem2ConfBoard_Type()
)
ppShmem2ConfBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppShmem2ConfBoard.setStatus("current")
_PpShmem2ConfModule_Type = Integer32
_PpShmem2ConfModule_Object = MibTableColumn
ppShmem2ConfModule = _PpShmem2ConfModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 3, 1, 2),
    _PpShmem2ConfModule_Type()
)
ppShmem2ConfModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppShmem2ConfModule.setStatus("current")
_PpShmem2ConfPort_Type = Integer32
_PpShmem2ConfPort_Object = MibTableColumn
ppShmem2ConfPort = _PpShmem2ConfPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 3, 1, 3),
    _PpShmem2ConfPort_Type()
)
ppShmem2ConfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppShmem2ConfPort.setStatus("current")


class _PpShmem2ConfPriority_Type(Integer32):
    """Custom type ppShmem2ConfPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("priorityABR", 1),
          ("priorityCBR", 3),
          ("priorityNrt", 6),
          ("priorityRt", 5),
          ("priorityUBR", 4),
          ("priorityVBR", 2))
    )


_PpShmem2ConfPriority_Type.__name__ = "Integer32"
_PpShmem2ConfPriority_Object = MibTableColumn
ppShmem2ConfPriority = _PpShmem2ConfPriority_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 3, 1, 4),
    _PpShmem2ConfPriority_Type()
)
ppShmem2ConfPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppShmem2ConfPriority.setStatus("current")
_PpShmem2Qsize_Type = Integer32
_PpShmem2Qsize_Object = MibTableColumn
ppShmem2Qsize = _PpShmem2Qsize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 3, 1, 5),
    _PpShmem2Qsize_Type()
)
ppShmem2Qsize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppShmem2Qsize.setStatus("current")
_PpShmem2ClpThreshold_Type = Integer32
_PpShmem2ClpThreshold_Object = MibTableColumn
ppShmem2ClpThreshold = _PpShmem2ClpThreshold_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 4, 3, 1, 6),
    _PpShmem2ClpThreshold_Type()
)
ppShmem2ClpThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppShmem2ClpThreshold.setStatus("current")
_ConnShmem2Group_ObjectIdentity = ObjectIdentity
connShmem2Group = _ConnShmem2Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 5)
)
_ChannelShmem2Table_Object = MibTable
channelShmem2Table = _ChannelShmem2Table_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 5, 1)
)
if mibBuilder.loadTexts:
    channelShmem2Table.setStatus("current")
_ChannelShmem2Entry_Object = MibTableRow
channelShmem2Entry = _ChannelShmem2Entry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 5, 1, 1)
)
channelShmem2Entry.setIndexNames(
    (0, "Fore-Switch-MIB", "vcShmem2OutputPort"),
    (0, "Fore-Switch-MIB", "vcShmem2OutputVPI"),
    (0, "Fore-Switch-MIB", "vcShmem2OutputVCI"),
)
if mibBuilder.loadTexts:
    channelShmem2Entry.setStatus("current")
_VcShmem2OutputPort_Type = Integer32
_VcShmem2OutputPort_Object = MibTableColumn
vcShmem2OutputPort = _VcShmem2OutputPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 5, 1, 1, 1),
    _VcShmem2OutputPort_Type()
)
vcShmem2OutputPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcShmem2OutputPort.setStatus("current")
_VcShmem2OutputVPI_Type = Integer32
_VcShmem2OutputVPI_Object = MibTableColumn
vcShmem2OutputVPI = _VcShmem2OutputVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 5, 1, 1, 2),
    _VcShmem2OutputVPI_Type()
)
vcShmem2OutputVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcShmem2OutputVPI.setStatus("current")
_VcShmem2OutputVCI_Type = Integer32
_VcShmem2OutputVCI_Object = MibTableColumn
vcShmem2OutputVCI = _VcShmem2OutputVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 5, 1, 1, 3),
    _VcShmem2OutputVCI_Type()
)
vcShmem2OutputVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcShmem2OutputVCI.setStatus("current")
_VcShmem2TotalLostCells_Type = Counter32
_VcShmem2TotalLostCells_Object = MibTableColumn
vcShmem2TotalLostCells = _VcShmem2TotalLostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 5, 1, 1, 4),
    _VcShmem2TotalLostCells_Type()
)
vcShmem2TotalLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcShmem2TotalLostCells.setStatus("current")
_VcShmem2IntentionalLostCells_Type = Counter32
_VcShmem2IntentionalLostCells_Object = MibTableColumn
vcShmem2IntentionalLostCells = _VcShmem2IntentionalLostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 5, 1, 1, 5),
    _VcShmem2IntentionalLostCells_Type()
)
vcShmem2IntentionalLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcShmem2IntentionalLostCells.setStatus("current")
_VcShmem2UnintentionalLostCells_Type = Counter32
_VcShmem2UnintentionalLostCells_Object = MibTableColumn
vcShmem2UnintentionalLostCells = _VcShmem2UnintentionalLostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 5, 1, 1, 6),
    _VcShmem2UnintentionalLostCells_Type()
)
vcShmem2UnintentionalLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcShmem2UnintentionalLostCells.setStatus("current")
_VcShmem2TransmittedCells_Type = Counter32
_VcShmem2TransmittedCells_Object = MibTableColumn
vcShmem2TransmittedCells = _VcShmem2TransmittedCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 5, 1, 1, 7),
    _VcShmem2TransmittedCells_Type()
)
vcShmem2TransmittedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcShmem2TransmittedCells.setStatus("current")
_PathShmem2Table_Object = MibTable
pathShmem2Table = _PathShmem2Table_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 5, 2)
)
if mibBuilder.loadTexts:
    pathShmem2Table.setStatus("current")
_PathShmem2Entry_Object = MibTableRow
pathShmem2Entry = _PathShmem2Entry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 5, 2, 1)
)
pathShmem2Entry.setIndexNames(
    (0, "Fore-Switch-MIB", "vpShmem2OutputPort"),
    (0, "Fore-Switch-MIB", "vpShmem2OutputVPI"),
)
if mibBuilder.loadTexts:
    pathShmem2Entry.setStatus("current")
_VpShmem2OutputPort_Type = Integer32
_VpShmem2OutputPort_Object = MibTableColumn
vpShmem2OutputPort = _VpShmem2OutputPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 5, 2, 1, 1),
    _VpShmem2OutputPort_Type()
)
vpShmem2OutputPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpShmem2OutputPort.setStatus("current")
_VpShmem2OutputVPI_Type = Integer32
_VpShmem2OutputVPI_Object = MibTableColumn
vpShmem2OutputVPI = _VpShmem2OutputVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 5, 2, 1, 2),
    _VpShmem2OutputVPI_Type()
)
vpShmem2OutputVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpShmem2OutputVPI.setStatus("current")
_VpShmem2TotalLostCells_Type = Counter32
_VpShmem2TotalLostCells_Object = MibTableColumn
vpShmem2TotalLostCells = _VpShmem2TotalLostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 5, 2, 1, 3),
    _VpShmem2TotalLostCells_Type()
)
vpShmem2TotalLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpShmem2TotalLostCells.setStatus("current")
_VpShmem2IntentionalLostCells_Type = Counter32
_VpShmem2IntentionalLostCells_Object = MibTableColumn
vpShmem2IntentionalLostCells = _VpShmem2IntentionalLostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 5, 2, 1, 4),
    _VpShmem2IntentionalLostCells_Type()
)
vpShmem2IntentionalLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpShmem2IntentionalLostCells.setStatus("current")
_VpShmem2UnintentionalLostCells_Type = Counter32
_VpShmem2UnintentionalLostCells_Object = MibTableColumn
vpShmem2UnintentionalLostCells = _VpShmem2UnintentionalLostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 5, 2, 1, 5),
    _VpShmem2UnintentionalLostCells_Type()
)
vpShmem2UnintentionalLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpShmem2UnintentionalLostCells.setStatus("current")
_VpShmem2TransmittedCells_Type = Counter32
_VpShmem2TransmittedCells_Object = MibTableColumn
vpShmem2TransmittedCells = _VpShmem2TransmittedCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 5, 2, 1, 6),
    _VpShmem2TransmittedCells_Type()
)
vpShmem2TransmittedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpShmem2TransmittedCells.setStatus("current")
_NetmodShmem3Group_ObjectIdentity = ObjectIdentity
netmodShmem3Group = _NetmodShmem3Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6)
)
_Shmem3ConfTable_Object = MibTable
shmem3ConfTable = _Shmem3ConfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 1)
)
if mibBuilder.loadTexts:
    shmem3ConfTable.setStatus("current")
_Shmem3ConfEntry_Object = MibTableRow
shmem3ConfEntry = _Shmem3ConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 1, 1)
)
shmem3ConfEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "shmem3ConfIndex"),
)
if mibBuilder.loadTexts:
    shmem3ConfEntry.setStatus("current")
_Shmem3ConfIndex_Type = Integer32
_Shmem3ConfIndex_Object = MibTableColumn
shmem3ConfIndex = _Shmem3ConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 1, 1, 1),
    _Shmem3ConfIndex_Type()
)
shmem3ConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmem3ConfIndex.setStatus("current")
_Shmem3UcastConnections_Type = Integer32
_Shmem3UcastConnections_Object = MibTableColumn
shmem3UcastConnections = _Shmem3UcastConnections_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 1, 1, 2),
    _Shmem3UcastConnections_Type()
)
shmem3UcastConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmem3UcastConnections.setStatus("current")
_Shmem3McastConnections_Type = Integer32
_Shmem3McastConnections_Object = MibTableColumn
shmem3McastConnections = _Shmem3McastConnections_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 1, 1, 3),
    _Shmem3McastConnections_Type()
)
shmem3McastConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmem3McastConnections.setStatus("current")
_Shmem3VpiVciLists_Type = Integer32
_Shmem3VpiVciLists_Object = MibTableColumn
shmem3VpiVciLists = _Shmem3VpiVciLists_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 1, 1, 4),
    _Shmem3VpiVciLists_Type()
)
shmem3VpiVciLists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmem3VpiVciLists.setStatus("current")
_Shmem3CellsBuffers_Type = Integer32
_Shmem3CellsBuffers_Object = MibTableColumn
shmem3CellsBuffers = _Shmem3CellsBuffers_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 1, 1, 5),
    _Shmem3CellsBuffers_Type()
)
shmem3CellsBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmem3CellsBuffers.setStatus("current")
_Shmem3ConfName_Type = DisplayString
_Shmem3ConfName_Object = MibTableColumn
shmem3ConfName = _Shmem3ConfName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 1, 1, 6),
    _Shmem3ConfName_Type()
)
shmem3ConfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmem3ConfName.setStatus("current")
_Shmem3Counters_Type = Integer32
_Shmem3Counters_Object = MibTableColumn
shmem3Counters = _Shmem3Counters_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 1, 1, 7),
    _Shmem3Counters_Type()
)
shmem3Counters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmem3Counters.setStatus("current")
_Shmem3CellMemorySize_Type = Integer32
_Shmem3CellMemorySize_Object = MibTableColumn
shmem3CellMemorySize = _Shmem3CellMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 1, 1, 8),
    _Shmem3CellMemorySize_Type()
)
shmem3CellMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmem3CellMemorySize.setStatus("current")
_Shmem3TableMemorySize_Type = Integer32
_Shmem3TableMemorySize_Object = MibTableColumn
shmem3TableMemorySize = _Shmem3TableMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 1, 1, 9),
    _Shmem3TableMemorySize_Type()
)
shmem3TableMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmem3TableMemorySize.setStatus("current")
_NetmodShmem3Table_Object = MibTable
netmodShmem3Table = _NetmodShmem3Table_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 2)
)
if mibBuilder.loadTexts:
    netmodShmem3Table.setStatus("current")
_NetmodShmem3Entry_Object = MibTableRow
netmodShmem3Entry = _NetmodShmem3Entry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 2, 1)
)
netmodShmem3Entry.setIndexNames(
    (0, "Fore-Switch-MIB", "nShmem3Board"),
    (0, "Fore-Switch-MIB", "nShmem3Module"),
)
if mibBuilder.loadTexts:
    netmodShmem3Entry.setStatus("current")
_NShmem3Board_Type = Integer32
_NShmem3Board_Object = MibTableColumn
nShmem3Board = _NShmem3Board_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 2, 1, 1),
    _NShmem3Board_Type()
)
nShmem3Board.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nShmem3Board.setStatus("current")
_NShmem3Module_Type = Integer32
_NShmem3Module_Object = MibTableColumn
nShmem3Module = _NShmem3Module_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 2, 1, 2),
    _NShmem3Module_Type()
)
nShmem3Module.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nShmem3Module.setStatus("current")
_NShmem3ConfRow_Type = Integer32
_NShmem3ConfRow_Object = MibTableColumn
nShmem3ConfRow = _NShmem3ConfRow_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 2, 1, 3),
    _NShmem3ConfRow_Type()
)
nShmem3ConfRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem3ConfRow.setStatus("current")
_NShmem3ConfSharedMemory_Type = Integer32
_NShmem3ConfSharedMemory_Object = MibTableColumn
nShmem3ConfSharedMemory = _NShmem3ConfSharedMemory_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 2, 1, 4),
    _NShmem3ConfSharedMemory_Type()
)
nShmem3ConfSharedMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nShmem3ConfSharedMemory.setStatus("current")
_NShmem3CurrentUcastConnections_Type = Gauge32
_NShmem3CurrentUcastConnections_Object = MibTableColumn
nShmem3CurrentUcastConnections = _NShmem3CurrentUcastConnections_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 2, 1, 5),
    _NShmem3CurrentUcastConnections_Type()
)
nShmem3CurrentUcastConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nShmem3CurrentUcastConnections.setStatus("current")
_NShmem3CurrentMcastConnections_Type = Gauge32
_NShmem3CurrentMcastConnections_Object = MibTableColumn
nShmem3CurrentMcastConnections = _NShmem3CurrentMcastConnections_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 2, 1, 6),
    _NShmem3CurrentMcastConnections_Type()
)
nShmem3CurrentMcastConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nShmem3CurrentMcastConnections.setStatus("current")
_NShmem3CurrentVpiVciLists_Type = Gauge32
_NShmem3CurrentVpiVciLists_Object = MibTableColumn
nShmem3CurrentVpiVciLists = _NShmem3CurrentVpiVciLists_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 2, 1, 7),
    _NShmem3CurrentVpiVciLists_Type()
)
nShmem3CurrentVpiVciLists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nShmem3CurrentVpiVciLists.setStatus("current")
_NShmem3CurrentCellsBuffers_Type = Gauge32
_NShmem3CurrentCellsBuffers_Object = MibTableColumn
nShmem3CurrentCellsBuffers = _NShmem3CurrentCellsBuffers_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 2, 1, 8),
    _NShmem3CurrentCellsBuffers_Type()
)
nShmem3CurrentCellsBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nShmem3CurrentCellsBuffers.setStatus("current")
_NShmem3ConfAal5PacketDrop_Type = Integer32
_NShmem3ConfAal5PacketDrop_Object = MibTableColumn
nShmem3ConfAal5PacketDrop = _NShmem3ConfAal5PacketDrop_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 2, 1, 10),
    _NShmem3ConfAal5PacketDrop_Type()
)
nShmem3ConfAal5PacketDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem3ConfAal5PacketDrop.setStatus("current")
_NShmem3ConfAal5PacketDropforUBR_Type = Integer32
_NShmem3ConfAal5PacketDropforUBR_Object = MibTableColumn
nShmem3ConfAal5PacketDropforUBR = _NShmem3ConfAal5PacketDropforUBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 2, 1, 11),
    _NShmem3ConfAal5PacketDropforUBR_Type()
)
nShmem3ConfAal5PacketDropforUBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem3ConfAal5PacketDropforUBR.setStatus("current")
_NShmem3ConfEfciOn_Type = Integer32
_NShmem3ConfEfciOn_Object = MibTableColumn
nShmem3ConfEfciOn = _NShmem3ConfEfciOn_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 2, 1, 12),
    _NShmem3ConfEfciOn_Type()
)
nShmem3ConfEfciOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem3ConfEfciOn.setStatus("current")
_NShmem3ConfEfciOff_Type = Integer32
_NShmem3ConfEfciOff_Object = MibTableColumn
nShmem3ConfEfciOff = _NShmem3ConfEfciOff_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 2, 1, 13),
    _NShmem3ConfEfciOff_Type()
)
nShmem3ConfEfciOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem3ConfEfciOff.setStatus("current")
_NShmem3CellMemorySize_Type = Integer32
_NShmem3CellMemorySize_Object = MibTableColumn
nShmem3CellMemorySize = _NShmem3CellMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 2, 1, 14),
    _NShmem3CellMemorySize_Type()
)
nShmem3CellMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nShmem3CellMemorySize.setStatus("current")
_NShmem3TableMemorySize_Type = Integer32
_NShmem3TableMemorySize_Object = MibTableColumn
nShmem3TableMemorySize = _NShmem3TableMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 2, 1, 15),
    _NShmem3TableMemorySize_Type()
)
nShmem3TableMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nShmem3TableMemorySize.setStatus("current")


class _NShmem3ConfCountPackets_Type(Integer32):
    """Custom type nShmem3ConfCountPackets based on Integer32"""
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


_NShmem3ConfCountPackets_Type.__name__ = "Integer32"
_NShmem3ConfCountPackets_Object = MibTableColumn
nShmem3ConfCountPackets = _NShmem3ConfCountPackets_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 2, 1, 16),
    _NShmem3ConfCountPackets_Type()
)
nShmem3ConfCountPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem3ConfCountPackets.setStatus("current")
_NShmem3ConfAltCLP1Threshold_Type = Integer32
_NShmem3ConfAltCLP1Threshold_Object = MibTableColumn
nShmem3ConfAltCLP1Threshold = _NShmem3ConfAltCLP1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 2, 1, 17),
    _NShmem3ConfAltCLP1Threshold_Type()
)
nShmem3ConfAltCLP1Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem3ConfAltCLP1Threshold.setStatus("current")
_NShmem3ConfAltCLP01Threshold_Type = Integer32
_NShmem3ConfAltCLP01Threshold_Object = MibTableColumn
nShmem3ConfAltCLP01Threshold = _NShmem3ConfAltCLP01Threshold_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 2, 1, 18),
    _NShmem3ConfAltCLP01Threshold_Type()
)
nShmem3ConfAltCLP01Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem3ConfAltCLP01Threshold.setStatus("current")
_NShmem3ConfVcCLP1ForCBR_Type = Integer32
_NShmem3ConfVcCLP1ForCBR_Object = MibTableColumn
nShmem3ConfVcCLP1ForCBR = _NShmem3ConfVcCLP1ForCBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 2, 1, 19),
    _NShmem3ConfVcCLP1ForCBR_Type()
)
nShmem3ConfVcCLP1ForCBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem3ConfVcCLP1ForCBR.setStatus("current")
_NShmem3ConfVcCLP01ForCBR_Type = Integer32
_NShmem3ConfVcCLP01ForCBR_Object = MibTableColumn
nShmem3ConfVcCLP01ForCBR = _NShmem3ConfVcCLP01ForCBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 2, 1, 20),
    _NShmem3ConfVcCLP01ForCBR_Type()
)
nShmem3ConfVcCLP01ForCBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem3ConfVcCLP01ForCBR.setStatus("current")
_NShmem3ConfVcCLP1ForVBR_Type = Integer32
_NShmem3ConfVcCLP1ForVBR_Object = MibTableColumn
nShmem3ConfVcCLP1ForVBR = _NShmem3ConfVcCLP1ForVBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 2, 1, 21),
    _NShmem3ConfVcCLP1ForVBR_Type()
)
nShmem3ConfVcCLP1ForVBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem3ConfVcCLP1ForVBR.setStatus("current")
_NShmem3ConfVcCLP01ForVBR_Type = Integer32
_NShmem3ConfVcCLP01ForVBR_Object = MibTableColumn
nShmem3ConfVcCLP01ForVBR = _NShmem3ConfVcCLP01ForVBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 2, 1, 22),
    _NShmem3ConfVcCLP01ForVBR_Type()
)
nShmem3ConfVcCLP01ForVBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem3ConfVcCLP01ForVBR.setStatus("current")
_NShmem3ConfVcCLP1ForABR_Type = Integer32
_NShmem3ConfVcCLP1ForABR_Object = MibTableColumn
nShmem3ConfVcCLP1ForABR = _NShmem3ConfVcCLP1ForABR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 2, 1, 23),
    _NShmem3ConfVcCLP1ForABR_Type()
)
nShmem3ConfVcCLP1ForABR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem3ConfVcCLP1ForABR.setStatus("current")
_NShmem3ConfVcCLP01ForABR_Type = Integer32
_NShmem3ConfVcCLP01ForABR_Object = MibTableColumn
nShmem3ConfVcCLP01ForABR = _NShmem3ConfVcCLP01ForABR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 2, 1, 24),
    _NShmem3ConfVcCLP01ForABR_Type()
)
nShmem3ConfVcCLP01ForABR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem3ConfVcCLP01ForABR.setStatus("current")
_NShmem3ConfVcCLP1ForUBR_Type = Integer32
_NShmem3ConfVcCLP1ForUBR_Object = MibTableColumn
nShmem3ConfVcCLP1ForUBR = _NShmem3ConfVcCLP1ForUBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 2, 1, 25),
    _NShmem3ConfVcCLP1ForUBR_Type()
)
nShmem3ConfVcCLP1ForUBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem3ConfVcCLP1ForUBR.setStatus("current")
_NShmem3ConfVcCLP01ForUBR_Type = Integer32
_NShmem3ConfVcCLP01ForUBR_Object = MibTableColumn
nShmem3ConfVcCLP01ForUBR = _NShmem3ConfVcCLP01ForUBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 6, 2, 1, 26),
    _NShmem3ConfVcCLP01ForUBR_Type()
)
nShmem3ConfVcCLP01ForUBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem3ConfVcCLP01ForUBR.setStatus("current")
_PortShmem3Group_ObjectIdentity = ObjectIdentity
portShmem3Group = _PortShmem3Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7)
)
_PortShmem3ConfTable_Object = MibTable
portShmem3ConfTable = _PortShmem3ConfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 1)
)
if mibBuilder.loadTexts:
    portShmem3ConfTable.setStatus("current")
_PortShmem3ConfEntry_Object = MibTableRow
portShmem3ConfEntry = _PortShmem3ConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 1, 1)
)
portShmem3ConfEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "pShmem3ConfBoard"),
    (0, "Fore-Switch-MIB", "pShmem3ConfModule"),
    (0, "Fore-Switch-MIB", "pShmem3ConfPort"),
)
if mibBuilder.loadTexts:
    portShmem3ConfEntry.setStatus("current")
_PShmem3ConfBoard_Type = Integer32
_PShmem3ConfBoard_Object = MibTableColumn
pShmem3ConfBoard = _PShmem3ConfBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 1, 1, 1),
    _PShmem3ConfBoard_Type()
)
pShmem3ConfBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem3ConfBoard.setStatus("current")
_PShmem3ConfModule_Type = Integer32
_PShmem3ConfModule_Object = MibTableColumn
pShmem3ConfModule = _PShmem3ConfModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 1, 1, 2),
    _PShmem3ConfModule_Type()
)
pShmem3ConfModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem3ConfModule.setStatus("current")
_PShmem3ConfPort_Type = Integer32
_PShmem3ConfPort_Object = MibTableColumn
pShmem3ConfPort = _PShmem3ConfPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 1, 1, 3),
    _PShmem3ConfPort_Type()
)
pShmem3ConfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem3ConfPort.setStatus("current")
_PShmem3QsizeforCBR_Type = Integer32
_PShmem3QsizeforCBR_Object = MibTableColumn
pShmem3QsizeforCBR = _PShmem3QsizeforCBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 1, 1, 4),
    _PShmem3QsizeforCBR_Type()
)
pShmem3QsizeforCBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pShmem3QsizeforCBR.setStatus("current")
_PShmem3QsizeforVBR_Type = Integer32
_PShmem3QsizeforVBR_Object = MibTableColumn
pShmem3QsizeforVBR = _PShmem3QsizeforVBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 1, 1, 5),
    _PShmem3QsizeforVBR_Type()
)
pShmem3QsizeforVBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pShmem3QsizeforVBR.setStatus("current")
_PShmem3QsizeforABR_Type = Integer32
_PShmem3QsizeforABR_Object = MibTableColumn
pShmem3QsizeforABR = _PShmem3QsizeforABR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 1, 1, 6),
    _PShmem3QsizeforABR_Type()
)
pShmem3QsizeforABR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pShmem3QsizeforABR.setStatus("current")
_PShmem3QsizeforUBR_Type = Integer32
_PShmem3QsizeforUBR_Object = MibTableColumn
pShmem3QsizeforUBR = _PShmem3QsizeforUBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 1, 1, 7),
    _PShmem3QsizeforUBR_Type()
)
pShmem3QsizeforUBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pShmem3QsizeforUBR.setStatus("current")
_PShmem3Clp01ThreshforCBR_Type = Integer32
_PShmem3Clp01ThreshforCBR_Object = MibTableColumn
pShmem3Clp01ThreshforCBR = _PShmem3Clp01ThreshforCBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 1, 1, 8),
    _PShmem3Clp01ThreshforCBR_Type()
)
pShmem3Clp01ThreshforCBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pShmem3Clp01ThreshforCBR.setStatus("current")
_PShmem3Clp1ThreshforCBR_Type = Integer32
_PShmem3Clp1ThreshforCBR_Object = MibTableColumn
pShmem3Clp1ThreshforCBR = _PShmem3Clp1ThreshforCBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 1, 1, 9),
    _PShmem3Clp1ThreshforCBR_Type()
)
pShmem3Clp1ThreshforCBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pShmem3Clp1ThreshforCBR.setStatus("current")
_PShmem3Clp01ThreshforVBR_Type = Integer32
_PShmem3Clp01ThreshforVBR_Object = MibTableColumn
pShmem3Clp01ThreshforVBR = _PShmem3Clp01ThreshforVBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 1, 1, 10),
    _PShmem3Clp01ThreshforVBR_Type()
)
pShmem3Clp01ThreshforVBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pShmem3Clp01ThreshforVBR.setStatus("current")
_PShmem3Clp1ThreshforVBR_Type = Integer32
_PShmem3Clp1ThreshforVBR_Object = MibTableColumn
pShmem3Clp1ThreshforVBR = _PShmem3Clp1ThreshforVBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 1, 1, 11),
    _PShmem3Clp1ThreshforVBR_Type()
)
pShmem3Clp1ThreshforVBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pShmem3Clp1ThreshforVBR.setStatus("current")
_PShmem3Clp01ThreshforABR_Type = Integer32
_PShmem3Clp01ThreshforABR_Object = MibTableColumn
pShmem3Clp01ThreshforABR = _PShmem3Clp01ThreshforABR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 1, 1, 12),
    _PShmem3Clp01ThreshforABR_Type()
)
pShmem3Clp01ThreshforABR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pShmem3Clp01ThreshforABR.setStatus("current")
_PShmem3Clp1ThreshforABR_Type = Integer32
_PShmem3Clp1ThreshforABR_Object = MibTableColumn
pShmem3Clp1ThreshforABR = _PShmem3Clp1ThreshforABR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 1, 1, 13),
    _PShmem3Clp1ThreshforABR_Type()
)
pShmem3Clp1ThreshforABR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pShmem3Clp1ThreshforABR.setStatus("current")
_PShmem3Clp01ThreshforUBR_Type = Integer32
_PShmem3Clp01ThreshforUBR_Object = MibTableColumn
pShmem3Clp01ThreshforUBR = _PShmem3Clp01ThreshforUBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 1, 1, 14),
    _PShmem3Clp01ThreshforUBR_Type()
)
pShmem3Clp01ThreshforUBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pShmem3Clp01ThreshforUBR.setStatus("current")
_PShmem3Clp1ThreshforUBR_Type = Integer32
_PShmem3Clp1ThreshforUBR_Object = MibTableColumn
pShmem3Clp1ThreshforUBR = _PShmem3Clp1ThreshforUBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 1, 1, 15),
    _PShmem3Clp1ThreshforUBR_Type()
)
pShmem3Clp1ThreshforUBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pShmem3Clp1ThreshforUBR.setStatus("current")
_PShmem3RateLimit_Type = Integer32
_PShmem3RateLimit_Object = MibTableColumn
pShmem3RateLimit = _PShmem3RateLimit_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 1, 1, 16),
    _PShmem3RateLimit_Type()
)
pShmem3RateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pShmem3RateLimit.setStatus("current")


class _PShmem3ConfSVCSchedulingCBR_Type(Integer32):
    """Custom type pShmem3ConfSVCSchedulingCBR based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("guaranteed", 4),
          ("roundrobin", 2),
          ("smoothed", 3))
    )


_PShmem3ConfSVCSchedulingCBR_Type.__name__ = "Integer32"
_PShmem3ConfSVCSchedulingCBR_Object = MibTableColumn
pShmem3ConfSVCSchedulingCBR = _PShmem3ConfSVCSchedulingCBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 1, 1, 17),
    _PShmem3ConfSVCSchedulingCBR_Type()
)
pShmem3ConfSVCSchedulingCBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pShmem3ConfSVCSchedulingCBR.setStatus("deprecated")


class _PShmem3ConfPVCSchedulingCBR_Type(Integer32):
    """Custom type pShmem3ConfPVCSchedulingCBR based on Integer32"""
    defaultValue = 2

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
        *(("guaranteed", 4),
          ("perupc", 1),
          ("roundrobin", 2),
          ("smoothed", 3))
    )


_PShmem3ConfPVCSchedulingCBR_Type.__name__ = "Integer32"
_PShmem3ConfPVCSchedulingCBR_Object = MibTableColumn
pShmem3ConfPVCSchedulingCBR = _PShmem3ConfPVCSchedulingCBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 1, 1, 18),
    _PShmem3ConfPVCSchedulingCBR_Type()
)
pShmem3ConfPVCSchedulingCBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pShmem3ConfPVCSchedulingCBR.setStatus("deprecated")


class _PShmem3ConfSVCSchedulingVBR_Type(Integer32):
    """Custom type pShmem3ConfSVCSchedulingVBR based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("guaranteed", 4),
          ("roundrobin", 2),
          ("smoothed", 3))
    )


_PShmem3ConfSVCSchedulingVBR_Type.__name__ = "Integer32"
_PShmem3ConfSVCSchedulingVBR_Object = MibTableColumn
pShmem3ConfSVCSchedulingVBR = _PShmem3ConfSVCSchedulingVBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 1, 1, 19),
    _PShmem3ConfSVCSchedulingVBR_Type()
)
pShmem3ConfSVCSchedulingVBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pShmem3ConfSVCSchedulingVBR.setStatus("deprecated")


class _PShmem3ConfPVCSchedulingVBR_Type(Integer32):
    """Custom type pShmem3ConfPVCSchedulingVBR based on Integer32"""
    defaultValue = 2

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
        *(("guaranteed", 4),
          ("perupc", 1),
          ("roundrobin", 2),
          ("smoothed", 3))
    )


_PShmem3ConfPVCSchedulingVBR_Type.__name__ = "Integer32"
_PShmem3ConfPVCSchedulingVBR_Object = MibTableColumn
pShmem3ConfPVCSchedulingVBR = _PShmem3ConfPVCSchedulingVBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 1, 1, 20),
    _PShmem3ConfPVCSchedulingVBR_Type()
)
pShmem3ConfPVCSchedulingVBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pShmem3ConfPVCSchedulingVBR.setStatus("deprecated")


class _PShmem3ConfAltCLPConfigCBR_Type(Integer32):
    """Custom type pShmem3ConfAltCLPConfigCBR based on Integer32"""
    defaultValue = 2

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
        *(("allOff", 2),
          ("allOn", 1),
          ("svcOff", 4),
          ("svcOn", 3))
    )


_PShmem3ConfAltCLPConfigCBR_Type.__name__ = "Integer32"
_PShmem3ConfAltCLPConfigCBR_Object = MibTableColumn
pShmem3ConfAltCLPConfigCBR = _PShmem3ConfAltCLPConfigCBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 1, 1, 21),
    _PShmem3ConfAltCLPConfigCBR_Type()
)
pShmem3ConfAltCLPConfigCBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pShmem3ConfAltCLPConfigCBR.setStatus("current")


class _PShmem3ConfAltCLPConfigVBR_Type(Integer32):
    """Custom type pShmem3ConfAltCLPConfigVBR based on Integer32"""
    defaultValue = 2

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
        *(("allOff", 2),
          ("allOn", 1),
          ("svcOff", 4),
          ("svcOn", 3))
    )


_PShmem3ConfAltCLPConfigVBR_Type.__name__ = "Integer32"
_PShmem3ConfAltCLPConfigVBR_Object = MibTableColumn
pShmem3ConfAltCLPConfigVBR = _PShmem3ConfAltCLPConfigVBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 1, 1, 22),
    _PShmem3ConfAltCLPConfigVBR_Type()
)
pShmem3ConfAltCLPConfigVBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pShmem3ConfAltCLPConfigVBR.setStatus("current")


class _PShmem3ConfAltCLPConfigUBR_Type(Integer32):
    """Custom type pShmem3ConfAltCLPConfigUBR based on Integer32"""
    defaultValue = 2

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
        *(("allOff", 2),
          ("allOn", 1),
          ("svcOff", 4),
          ("svcOn", 3))
    )


_PShmem3ConfAltCLPConfigUBR_Type.__name__ = "Integer32"
_PShmem3ConfAltCLPConfigUBR_Object = MibTableColumn
pShmem3ConfAltCLPConfigUBR = _PShmem3ConfAltCLPConfigUBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 1, 1, 23),
    _PShmem3ConfAltCLPConfigUBR_Type()
)
pShmem3ConfAltCLPConfigUBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pShmem3ConfAltCLPConfigUBR.setStatus("current")
_PShmem3AtmInterfaceIndex_Type = Integer32
_PShmem3AtmInterfaceIndex_Object = MibTableColumn
pShmem3AtmInterfaceIndex = _PShmem3AtmInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 1, 1, 24),
    _PShmem3AtmInterfaceIndex_Type()
)
pShmem3AtmInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem3AtmInterfaceIndex.setStatus("current")
_PortShmem3Table_Object = MibTable
portShmem3Table = _PortShmem3Table_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 2)
)
if mibBuilder.loadTexts:
    portShmem3Table.setStatus("current")
_PortShmem3Entry_Object = MibTableRow
portShmem3Entry = _PortShmem3Entry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 2, 1)
)
portShmem3Entry.setIndexNames(
    (0, "Fore-Switch-MIB", "pShmem3Board"),
    (0, "Fore-Switch-MIB", "pShmem3Module"),
    (0, "Fore-Switch-MIB", "pShmem3Port"),
    (0, "Fore-Switch-MIB", "pShmem3Priority"),
)
if mibBuilder.loadTexts:
    portShmem3Entry.setStatus("current")
_PShmem3Board_Type = Integer32
_PShmem3Board_Object = MibTableColumn
pShmem3Board = _PShmem3Board_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 2, 1, 1),
    _PShmem3Board_Type()
)
pShmem3Board.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem3Board.setStatus("current")
_PShmem3Module_Type = Integer32
_PShmem3Module_Object = MibTableColumn
pShmem3Module = _PShmem3Module_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 2, 1, 2),
    _PShmem3Module_Type()
)
pShmem3Module.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem3Module.setStatus("current")
_PShmem3Port_Type = Integer32
_PShmem3Port_Object = MibTableColumn
pShmem3Port = _PShmem3Port_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 2, 1, 3),
    _PShmem3Port_Type()
)
pShmem3Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem3Port.setStatus("current")


class _PShmem3Priority_Type(Integer32):
    """Custom type pShmem3Priority based on Integer32"""
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
        *(("priorityABR", 1),
          ("priorityCBR", 3),
          ("priorityUBR", 4),
          ("priorityVBR", 2))
    )


_PShmem3Priority_Type.__name__ = "Integer32"
_PShmem3Priority_Object = MibTableColumn
pShmem3Priority = _PShmem3Priority_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 2, 1, 4),
    _PShmem3Priority_Type()
)
pShmem3Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem3Priority.setStatus("current")
_PShmem3CurrentQsize_Type = Integer32
_PShmem3CurrentQsize_Object = MibTableColumn
pShmem3CurrentQsize = _PShmem3CurrentQsize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 2, 1, 5),
    _PShmem3CurrentQsize_Type()
)
pShmem3CurrentQsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem3CurrentQsize.setStatus("current")
_PShmem3TxCells_Type = Counter32
_PShmem3TxCells_Object = MibTableColumn
pShmem3TxCells = _PShmem3TxCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 2, 1, 6),
    _PShmem3TxCells_Type()
)
pShmem3TxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem3TxCells.setStatus("current")
_PShmem3EPDLostCells_Type = Counter32
_PShmem3EPDLostCells_Object = MibTableColumn
pShmem3EPDLostCells = _PShmem3EPDLostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 2, 1, 7),
    _PShmem3EPDLostCells_Type()
)
pShmem3EPDLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem3EPDLostCells.setStatus("current")
_PShmem3CLP01LostCells_Type = Counter32
_PShmem3CLP01LostCells_Object = MibTableColumn
pShmem3CLP01LostCells = _PShmem3CLP01LostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 2, 1, 8),
    _PShmem3CLP01LostCells_Type()
)
pShmem3CLP01LostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem3CLP01LostCells.setStatus("current")
_PShmem3CLP1LostCells_Type = Counter32
_PShmem3CLP1LostCells_Object = MibTableColumn
pShmem3CLP1LostCells = _PShmem3CLP1LostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 2, 1, 9),
    _PShmem3CLP1LostCells_Type()
)
pShmem3CLP1LostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem3CLP1LostCells.setStatus("current")
_PShmem3VcCLPLostCells_Type = Counter32
_PShmem3VcCLPLostCells_Object = MibTableColumn
pShmem3VcCLPLostCells = _PShmem3VcCLPLostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 2, 1, 10),
    _PShmem3VcCLPLostCells_Type()
)
pShmem3VcCLPLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem3VcCLPLostCells.setStatus("current")
_PShmem3OverflowLostCells_Type = Counter32
_PShmem3OverflowLostCells_Object = MibTableColumn
pShmem3OverflowLostCells = _PShmem3OverflowLostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 2, 1, 11),
    _PShmem3OverflowLostCells_Type()
)
pShmem3OverflowLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem3OverflowLostCells.setStatus("current")
_PShmem3PPDLostCells_Type = Counter32
_PShmem3PPDLostCells_Object = MibTableColumn
pShmem3PPDLostCells = _PShmem3PPDLostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 7, 2, 1, 12),
    _PShmem3PPDLostCells_Type()
)
pShmem3PPDLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pShmem3PPDLostCells.setStatus("current")
_ConnShmem3Group_ObjectIdentity = ObjectIdentity
connShmem3Group = _ConnShmem3Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 8)
)
_ChannelShmem3Table_Object = MibTable
channelShmem3Table = _ChannelShmem3Table_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 8, 1)
)
if mibBuilder.loadTexts:
    channelShmem3Table.setStatus("current")
_ChannelShmem3Entry_Object = MibTableRow
channelShmem3Entry = _ChannelShmem3Entry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 8, 1, 1)
)
channelShmem3Entry.setIndexNames(
    (0, "Fore-Switch-MIB", "vcShmem3OutputPort"),
    (0, "Fore-Switch-MIB", "vcShmem3OutputVPI"),
    (0, "Fore-Switch-MIB", "vcShmem3OutputVCI"),
)
if mibBuilder.loadTexts:
    channelShmem3Entry.setStatus("current")
_VcShmem3OutputPort_Type = Integer32
_VcShmem3OutputPort_Object = MibTableColumn
vcShmem3OutputPort = _VcShmem3OutputPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 8, 1, 1, 1),
    _VcShmem3OutputPort_Type()
)
vcShmem3OutputPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcShmem3OutputPort.setStatus("current")
_VcShmem3OutputVPI_Type = Integer32
_VcShmem3OutputVPI_Object = MibTableColumn
vcShmem3OutputVPI = _VcShmem3OutputVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 8, 1, 1, 2),
    _VcShmem3OutputVPI_Type()
)
vcShmem3OutputVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcShmem3OutputVPI.setStatus("current")
_VcShmem3OutputVCI_Type = Integer32
_VcShmem3OutputVCI_Object = MibTableColumn
vcShmem3OutputVCI = _VcShmem3OutputVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 8, 1, 1, 3),
    _VcShmem3OutputVCI_Type()
)
vcShmem3OutputVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcShmem3OutputVCI.setStatus("current")
_VcShmem3IntentionalLostCells_Type = Counter32
_VcShmem3IntentionalLostCells_Object = MibTableColumn
vcShmem3IntentionalLostCells = _VcShmem3IntentionalLostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 8, 1, 1, 4),
    _VcShmem3IntentionalLostCells_Type()
)
vcShmem3IntentionalLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcShmem3IntentionalLostCells.setStatus("current")
_VcShmem3UnintentionalLostCells_Type = Counter32
_VcShmem3UnintentionalLostCells_Object = MibTableColumn
vcShmem3UnintentionalLostCells = _VcShmem3UnintentionalLostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 8, 1, 1, 5),
    _VcShmem3UnintentionalLostCells_Type()
)
vcShmem3UnintentionalLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcShmem3UnintentionalLostCells.setStatus("current")
_VcShmem3CLP0TxCells_Type = Counter32
_VcShmem3CLP0TxCells_Object = MibTableColumn
vcShmem3CLP0TxCells = _VcShmem3CLP0TxCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 8, 1, 1, 6),
    _VcShmem3CLP0TxCells_Type()
)
vcShmem3CLP0TxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcShmem3CLP0TxCells.setStatus("current")
_VcShmem3CLP1TxCells_Type = Counter32
_VcShmem3CLP1TxCells_Object = MibTableColumn
vcShmem3CLP1TxCells = _VcShmem3CLP1TxCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 8, 1, 1, 7),
    _VcShmem3CLP1TxCells_Type()
)
vcShmem3CLP1TxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcShmem3CLP1TxCells.setStatus("current")
_VcShmem3EPDLostCells_Type = Counter32
_VcShmem3EPDLostCells_Object = MibTableColumn
vcShmem3EPDLostCells = _VcShmem3EPDLostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 8, 1, 1, 8),
    _VcShmem3EPDLostCells_Type()
)
vcShmem3EPDLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcShmem3EPDLostCells.setStatus("current")
_VcShmem3CLP1LostCells_Type = Counter32
_VcShmem3CLP1LostCells_Object = MibTableColumn
vcShmem3CLP1LostCells = _VcShmem3CLP1LostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 8, 1, 1, 9),
    _VcShmem3CLP1LostCells_Type()
)
vcShmem3CLP1LostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcShmem3CLP1LostCells.setStatus("current")
_VcShmem3CLP01LostCells_Type = Counter32
_VcShmem3CLP01LostCells_Object = MibTableColumn
vcShmem3CLP01LostCells = _VcShmem3CLP01LostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 8, 1, 1, 10),
    _VcShmem3CLP01LostCells_Type()
)
vcShmem3CLP01LostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcShmem3CLP01LostCells.setStatus("current")
_VcShmem3TransmittedPackets_Type = Counter32
_VcShmem3TransmittedPackets_Object = MibTableColumn
vcShmem3TransmittedPackets = _VcShmem3TransmittedPackets_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 8, 1, 1, 11),
    _VcShmem3TransmittedPackets_Type()
)
vcShmem3TransmittedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcShmem3TransmittedPackets.setStatus("current")
_VcShmem3CurrentQsize_Type = Integer32
_VcShmem3CurrentQsize_Object = MibTableColumn
vcShmem3CurrentQsize = _VcShmem3CurrentQsize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 8, 1, 1, 12),
    _VcShmem3CurrentQsize_Type()
)
vcShmem3CurrentQsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcShmem3CurrentQsize.setStatus("current")
_PathShmem3Table_Object = MibTable
pathShmem3Table = _PathShmem3Table_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 8, 2)
)
if mibBuilder.loadTexts:
    pathShmem3Table.setStatus("current")
_PathShmem3Entry_Object = MibTableRow
pathShmem3Entry = _PathShmem3Entry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 8, 2, 1)
)
pathShmem3Entry.setIndexNames(
    (0, "Fore-Switch-MIB", "vpShmem3OutputPort"),
    (0, "Fore-Switch-MIB", "vpShmem3OutputVPI"),
)
if mibBuilder.loadTexts:
    pathShmem3Entry.setStatus("current")
_VpShmem3OutputPort_Type = Integer32
_VpShmem3OutputPort_Object = MibTableColumn
vpShmem3OutputPort = _VpShmem3OutputPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 8, 2, 1, 1),
    _VpShmem3OutputPort_Type()
)
vpShmem3OutputPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpShmem3OutputPort.setStatus("current")
_VpShmem3OutputVPI_Type = Integer32
_VpShmem3OutputVPI_Object = MibTableColumn
vpShmem3OutputVPI = _VpShmem3OutputVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 8, 2, 1, 2),
    _VpShmem3OutputVPI_Type()
)
vpShmem3OutputVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpShmem3OutputVPI.setStatus("current")
_VpShmem3UnintentionalLostCells_Type = Counter32
_VpShmem3UnintentionalLostCells_Object = MibTableColumn
vpShmem3UnintentionalLostCells = _VpShmem3UnintentionalLostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 8, 2, 1, 4),
    _VpShmem3UnintentionalLostCells_Type()
)
vpShmem3UnintentionalLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpShmem3UnintentionalLostCells.setStatus("current")
_VpShmem3CLP0TxCells_Type = Counter32
_VpShmem3CLP0TxCells_Object = MibTableColumn
vpShmem3CLP0TxCells = _VpShmem3CLP0TxCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 8, 2, 1, 5),
    _VpShmem3CLP0TxCells_Type()
)
vpShmem3CLP0TxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpShmem3CLP0TxCells.setStatus("current")
_VpShmem3CLP1TxCells_Type = Counter32
_VpShmem3CLP1TxCells_Object = MibTableColumn
vpShmem3CLP1TxCells = _VpShmem3CLP1TxCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 8, 2, 1, 6),
    _VpShmem3CLP1TxCells_Type()
)
vpShmem3CLP1TxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpShmem3CLP1TxCells.setStatus("current")
_VpShmem3CLP1LostCells_Type = Counter32
_VpShmem3CLP1LostCells_Object = MibTableColumn
vpShmem3CLP1LostCells = _VpShmem3CLP1LostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 8, 2, 1, 8),
    _VpShmem3CLP1LostCells_Type()
)
vpShmem3CLP1LostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpShmem3CLP1LostCells.setStatus("current")
_VpShmem3CLP01LostCells_Type = Counter32
_VpShmem3CLP01LostCells_Object = MibTableColumn
vpShmem3CLP01LostCells = _VpShmem3CLP01LostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 8, 2, 1, 9),
    _VpShmem3CLP01LostCells_Type()
)
vpShmem3CLP01LostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpShmem3CLP01LostCells.setStatus("current")
_VpShmem3TransmittedPackets_Type = Counter32
_VpShmem3TransmittedPackets_Object = MibTableColumn
vpShmem3TransmittedPackets = _VpShmem3TransmittedPackets_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 8, 2, 1, 10),
    _VpShmem3TransmittedPackets_Type()
)
vpShmem3TransmittedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpShmem3TransmittedPackets.setStatus("current")
_VpShmem3CurrentQsize_Type = Integer32
_VpShmem3CurrentQsize_Object = MibTableColumn
vpShmem3CurrentQsize = _VpShmem3CurrentQsize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 8, 2, 1, 11),
    _VpShmem3CurrentQsize_Type()
)
vpShmem3CurrentQsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpShmem3CurrentQsize.setStatus("current")
_NetmodGenericShmemGroup_ObjectIdentity = ObjectIdentity
netmodGenericShmemGroup = _NetmodGenericShmemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 9)
)
_NetmodGenericShmemTable_Object = MibTable
netmodGenericShmemTable = _NetmodGenericShmemTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 9, 1)
)
if mibBuilder.loadTexts:
    netmodGenericShmemTable.setStatus("current")
_NetmodGenericShmemEntry_Object = MibTableRow
netmodGenericShmemEntry = _NetmodGenericShmemEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 9, 1, 1)
)
netmodGenericShmemEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "nGenericShmemBoard"),
    (0, "Fore-Switch-MIB", "nGenericShmemModule"),
    (0, "Fore-Switch-MIB", "nGenericShmemSubindex"),
)
if mibBuilder.loadTexts:
    netmodGenericShmemEntry.setStatus("current")
_NGenericShmemBoard_Type = Integer32
_NGenericShmemBoard_Object = MibTableColumn
nGenericShmemBoard = _NGenericShmemBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 9, 1, 1, 1),
    _NGenericShmemBoard_Type()
)
nGenericShmemBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nGenericShmemBoard.setStatus("current")
_NGenericShmemModule_Type = Integer32
_NGenericShmemModule_Object = MibTableColumn
nGenericShmemModule = _NGenericShmemModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 9, 1, 1, 2),
    _NGenericShmemModule_Type()
)
nGenericShmemModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nGenericShmemModule.setStatus("current")
_NGenericShmemSubindex_Type = Integer32
_NGenericShmemSubindex_Object = MibTableColumn
nGenericShmemSubindex = _NGenericShmemSubindex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 9, 1, 1, 3),
    _NGenericShmemSubindex_Type()
)
nGenericShmemSubindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nGenericShmemSubindex.setStatus("current")
_NGenericShmemCurrentUcastConnections_Type = Integer32
_NGenericShmemCurrentUcastConnections_Object = MibTableColumn
nGenericShmemCurrentUcastConnections = _NGenericShmemCurrentUcastConnections_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 9, 1, 1, 4),
    _NGenericShmemCurrentUcastConnections_Type()
)
nGenericShmemCurrentUcastConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nGenericShmemCurrentUcastConnections.setStatus("current")
_NGenericShmemCurrentMcastConnections_Type = Integer32
_NGenericShmemCurrentMcastConnections_Object = MibTableColumn
nGenericShmemCurrentMcastConnections = _NGenericShmemCurrentMcastConnections_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 9, 1, 1, 5),
    _NGenericShmemCurrentMcastConnections_Type()
)
nGenericShmemCurrentMcastConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nGenericShmemCurrentMcastConnections.setStatus("current")
_NGenericShmemCurrentConnections_Type = Integer32
_NGenericShmemCurrentConnections_Object = MibTableColumn
nGenericShmemCurrentConnections = _NGenericShmemCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 9, 1, 1, 6),
    _NGenericShmemCurrentConnections_Type()
)
nGenericShmemCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nGenericShmemCurrentConnections.setStatus("current")
_NGenericShmemMaxUcastConnections_Type = Integer32
_NGenericShmemMaxUcastConnections_Object = MibTableColumn
nGenericShmemMaxUcastConnections = _NGenericShmemMaxUcastConnections_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 9, 1, 1, 7),
    _NGenericShmemMaxUcastConnections_Type()
)
nGenericShmemMaxUcastConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nGenericShmemMaxUcastConnections.setStatus("current")
_NGenericShmemMaxMcastConnections_Type = Integer32
_NGenericShmemMaxMcastConnections_Object = MibTableColumn
nGenericShmemMaxMcastConnections = _NGenericShmemMaxMcastConnections_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 9, 1, 1, 8),
    _NGenericShmemMaxMcastConnections_Type()
)
nGenericShmemMaxMcastConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nGenericShmemMaxMcastConnections.setStatus("current")
_NGenericShmemMaxConnections_Type = Integer32
_NGenericShmemMaxConnections_Object = MibTableColumn
nGenericShmemMaxConnections = _NGenericShmemMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 9, 1, 1, 9),
    _NGenericShmemMaxConnections_Type()
)
nGenericShmemMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nGenericShmemMaxConnections.setStatus("current")
_GenericPortGroupConfTable_Object = MibTable
genericPortGroupConfTable = _GenericPortGroupConfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 9, 2)
)
if mibBuilder.loadTexts:
    genericPortGroupConfTable.setStatus("current")
_GenericPortGroupConfEntry_Object = MibTableRow
genericPortGroupConfEntry = _GenericPortGroupConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 9, 2, 1)
)
genericPortGroupConfEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "genericPortGroupBoard"),
    (0, "Fore-Switch-MIB", "genericPortGroupIndex"),
    (0, "Fore-Switch-MIB", "genericPortGroupSubindex"),
    (0, "Fore-Switch-MIB", "genericPortGroupPrioIndex"),
)
if mibBuilder.loadTexts:
    genericPortGroupConfEntry.setStatus("current")
_GenericPortGroupBoard_Type = Integer32
_GenericPortGroupBoard_Object = MibTableColumn
genericPortGroupBoard = _GenericPortGroupBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 9, 2, 1, 1),
    _GenericPortGroupBoard_Type()
)
genericPortGroupBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericPortGroupBoard.setStatus("current")
_GenericPortGroupIndex_Type = Integer32
_GenericPortGroupIndex_Object = MibTableColumn
genericPortGroupIndex = _GenericPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 9, 2, 1, 2),
    _GenericPortGroupIndex_Type()
)
genericPortGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericPortGroupIndex.setStatus("current")
_GenericPortGroupSubindex_Type = Integer32
_GenericPortGroupSubindex_Object = MibTableColumn
genericPortGroupSubindex = _GenericPortGroupSubindex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 9, 2, 1, 3),
    _GenericPortGroupSubindex_Type()
)
genericPortGroupSubindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericPortGroupSubindex.setStatus("current")
_GenericPortGroupPrioIndex_Type = Integer32
_GenericPortGroupPrioIndex_Object = MibTableColumn
genericPortGroupPrioIndex = _GenericPortGroupPrioIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 9, 2, 1, 4),
    _GenericPortGroupPrioIndex_Type()
)
genericPortGroupPrioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericPortGroupPrioIndex.setStatus("current")
_GenericPortGroupAal5PacketDrop_Type = Integer32
_GenericPortGroupAal5PacketDrop_Object = MibTableColumn
genericPortGroupAal5PacketDrop = _GenericPortGroupAal5PacketDrop_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 9, 2, 1, 5),
    _GenericPortGroupAal5PacketDrop_Type()
)
genericPortGroupAal5PacketDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericPortGroupAal5PacketDrop.setStatus("current")
_GenericPortGroupEfciOn_Type = Integer32
_GenericPortGroupEfciOn_Object = MibTableColumn
genericPortGroupEfciOn = _GenericPortGroupEfciOn_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 9, 2, 1, 6),
    _GenericPortGroupEfciOn_Type()
)
genericPortGroupEfciOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericPortGroupEfciOn.setStatus("current")
_GenericPortGroupEfciOff_Type = Integer32
_GenericPortGroupEfciOff_Object = MibTableColumn
genericPortGroupEfciOff = _GenericPortGroupEfciOff_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 9, 2, 1, 7),
    _GenericPortGroupEfciOff_Type()
)
genericPortGroupEfciOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericPortGroupEfciOff.setStatus("current")
_GenericPortGroupPrioName_Type = DisplayString
_GenericPortGroupPrioName_Object = MibTableColumn
genericPortGroupPrioName = _GenericPortGroupPrioName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 9, 2, 1, 8),
    _GenericPortGroupPrioName_Type()
)
genericPortGroupPrioName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericPortGroupPrioName.setStatus("current")
_NetmodGenericShmemCustomBCSTable_Object = MibTable
netmodGenericShmemCustomBCSTable = _NetmodGenericShmemCustomBCSTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 9, 3)
)
if mibBuilder.loadTexts:
    netmodGenericShmemCustomBCSTable.setStatus("current")
_NetmodGenericShmemCustomBCSEntry_Object = MibTableRow
netmodGenericShmemCustomBCSEntry = _NetmodGenericShmemCustomBCSEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 9, 3, 1)
)
netmodGenericShmemCustomBCSEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "nGenericShmemCustomBCSBoard"),
    (0, "Fore-Switch-MIB", "nGenericShmemCustomBCSModule"),
    (0, "Fore-Switch-MIB", "nGenericShmemCustomBCSSubindex"),
    (0, "Fore-Switch-MIB", "nGenericShmemCustomBCSValue"),
)
if mibBuilder.loadTexts:
    netmodGenericShmemCustomBCSEntry.setStatus("current")
_NGenericShmemCustomBCSBoard_Type = Integer32
_NGenericShmemCustomBCSBoard_Object = MibTableColumn
nGenericShmemCustomBCSBoard = _NGenericShmemCustomBCSBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 9, 3, 1, 1),
    _NGenericShmemCustomBCSBoard_Type()
)
nGenericShmemCustomBCSBoard.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nGenericShmemCustomBCSBoard.setStatus("current")
_NGenericShmemCustomBCSModule_Type = Integer32
_NGenericShmemCustomBCSModule_Object = MibTableColumn
nGenericShmemCustomBCSModule = _NGenericShmemCustomBCSModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 9, 3, 1, 2),
    _NGenericShmemCustomBCSModule_Type()
)
nGenericShmemCustomBCSModule.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nGenericShmemCustomBCSModule.setStatus("current")
_NGenericShmemCustomBCSSubindex_Type = Integer32
_NGenericShmemCustomBCSSubindex_Object = MibTableColumn
nGenericShmemCustomBCSSubindex = _NGenericShmemCustomBCSSubindex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 9, 3, 1, 3),
    _NGenericShmemCustomBCSSubindex_Type()
)
nGenericShmemCustomBCSSubindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nGenericShmemCustomBCSSubindex.setStatus("current")
_NGenericShmemCustomBCSValue_Type = Integer32
_NGenericShmemCustomBCSValue_Object = MibTableColumn
nGenericShmemCustomBCSValue = _NGenericShmemCustomBCSValue_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 9, 3, 1, 4),
    _NGenericShmemCustomBCSValue_Type()
)
nGenericShmemCustomBCSValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nGenericShmemCustomBCSValue.setStatus("current")
_NGenericShmemCustomBCSWeight_Type = Integer32
_NGenericShmemCustomBCSWeight_Object = MibTableColumn
nGenericShmemCustomBCSWeight = _NGenericShmemCustomBCSWeight_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 9, 3, 1, 5),
    _NGenericShmemCustomBCSWeight_Type()
)
nGenericShmemCustomBCSWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nGenericShmemCustomBCSWeight.setStatus("current")
_NGenericShmemCustomBCSRowStatus_Type = RowStatus
_NGenericShmemCustomBCSRowStatus_Object = MibTableColumn
nGenericShmemCustomBCSRowStatus = _NGenericShmemCustomBCSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 9, 3, 1, 6),
    _NGenericShmemCustomBCSRowStatus_Type()
)
nGenericShmemCustomBCSRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nGenericShmemCustomBCSRowStatus.setStatus("current")
_GenericOutputPortGroup_ObjectIdentity = ObjectIdentity
genericOutputPortGroup = _GenericOutputPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 10)
)
_GenericOutputPortConfTable_Object = MibTable
genericOutputPortConfTable = _GenericOutputPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 10, 1)
)
if mibBuilder.loadTexts:
    genericOutputPortConfTable.setStatus("current")
_GenericOutputPortConfEntry_Object = MibTableRow
genericOutputPortConfEntry = _GenericOutputPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 10, 1, 1)
)
genericOutputPortConfEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "genericOutputPortConfBoard"),
    (0, "Fore-Switch-MIB", "genericOutputPortConfModule"),
    (0, "Fore-Switch-MIB", "genericOutputPortConfPort"),
    (0, "Fore-Switch-MIB", "genericOutputPortConfPrio"),
)
if mibBuilder.loadTexts:
    genericOutputPortConfEntry.setStatus("current")
_GenericOutputPortConfBoard_Type = Integer32
_GenericOutputPortConfBoard_Object = MibTableColumn
genericOutputPortConfBoard = _GenericOutputPortConfBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 10, 1, 1, 1),
    _GenericOutputPortConfBoard_Type()
)
genericOutputPortConfBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericOutputPortConfBoard.setStatus("current")
_GenericOutputPortConfModule_Type = Integer32
_GenericOutputPortConfModule_Object = MibTableColumn
genericOutputPortConfModule = _GenericOutputPortConfModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 10, 1, 1, 2),
    _GenericOutputPortConfModule_Type()
)
genericOutputPortConfModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericOutputPortConfModule.setStatus("current")
_GenericOutputPortConfPort_Type = Integer32
_GenericOutputPortConfPort_Object = MibTableColumn
genericOutputPortConfPort = _GenericOutputPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 10, 1, 1, 3),
    _GenericOutputPortConfPort_Type()
)
genericOutputPortConfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericOutputPortConfPort.setStatus("current")
_GenericOutputPortConfPrio_Type = Integer32
_GenericOutputPortConfPrio_Object = MibTableColumn
genericOutputPortConfPrio = _GenericOutputPortConfPrio_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 10, 1, 1, 4),
    _GenericOutputPortConfPrio_Type()
)
genericOutputPortConfPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericOutputPortConfPrio.setStatus("current")
_GenericOutputPortConfPrioDedicatedQSize_Type = Integer32
_GenericOutputPortConfPrioDedicatedQSize_Object = MibTableColumn
genericOutputPortConfPrioDedicatedQSize = _GenericOutputPortConfPrioDedicatedQSize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 10, 1, 1, 5),
    _GenericOutputPortConfPrioDedicatedQSize_Type()
)
genericOutputPortConfPrioDedicatedQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericOutputPortConfPrioDedicatedQSize.setStatus("current")
_GenericOutputPortConfPrioClp1Threshold_Type = Integer32
_GenericOutputPortConfPrioClp1Threshold_Object = MibTableColumn
genericOutputPortConfPrioClp1Threshold = _GenericOutputPortConfPrioClp1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 10, 1, 1, 6),
    _GenericOutputPortConfPrioClp1Threshold_Type()
)
genericOutputPortConfPrioClp1Threshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericOutputPortConfPrioClp1Threshold.setStatus("current")
_GenericOutputPortConfPrioClp01Threshold_Type = Integer32
_GenericOutputPortConfPrioClp01Threshold_Object = MibTableColumn
genericOutputPortConfPrioClp01Threshold = _GenericOutputPortConfPrioClp01Threshold_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 10, 1, 1, 7),
    _GenericOutputPortConfPrioClp01Threshold_Type()
)
genericOutputPortConfPrioClp01Threshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericOutputPortConfPrioClp01Threshold.setStatus("current")
_GenericOutputPortConfPrioName_Type = DisplayString
_GenericOutputPortConfPrioName_Object = MibTableColumn
genericOutputPortConfPrioName = _GenericOutputPortConfPrioName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 10, 1, 1, 8),
    _GenericOutputPortConfPrioName_Type()
)
genericOutputPortConfPrioName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericOutputPortConfPrioName.setStatus("current")
_GenericOutputPortConfAtmif_Type = Integer32
_GenericOutputPortConfAtmif_Object = MibTableColumn
genericOutputPortConfAtmif = _GenericOutputPortConfAtmif_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 10, 1, 1, 9),
    _GenericOutputPortConfAtmif_Type()
)
genericOutputPortConfAtmif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericOutputPortConfAtmif.setStatus("current")
_GenericOutputPortStatsTable_Object = MibTable
genericOutputPortStatsTable = _GenericOutputPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 10, 2)
)
if mibBuilder.loadTexts:
    genericOutputPortStatsTable.setStatus("current")
_GenericOutputPortStatsEntry_Object = MibTableRow
genericOutputPortStatsEntry = _GenericOutputPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 10, 2, 1)
)
genericOutputPortStatsEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "genericOutputPortStatsBoard"),
    (0, "Fore-Switch-MIB", "genericOutputPortStatsModule"),
    (0, "Fore-Switch-MIB", "genericOutputPortStatsPort"),
    (0, "Fore-Switch-MIB", "genericOutputPortStatsPrio"),
)
if mibBuilder.loadTexts:
    genericOutputPortStatsEntry.setStatus("current")
_GenericOutputPortStatsBoard_Type = Integer32
_GenericOutputPortStatsBoard_Object = MibTableColumn
genericOutputPortStatsBoard = _GenericOutputPortStatsBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 10, 2, 1, 1),
    _GenericOutputPortStatsBoard_Type()
)
genericOutputPortStatsBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericOutputPortStatsBoard.setStatus("current")
_GenericOutputPortStatsModule_Type = Integer32
_GenericOutputPortStatsModule_Object = MibTableColumn
genericOutputPortStatsModule = _GenericOutputPortStatsModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 10, 2, 1, 2),
    _GenericOutputPortStatsModule_Type()
)
genericOutputPortStatsModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericOutputPortStatsModule.setStatus("current")
_GenericOutputPortStatsPort_Type = Integer32
_GenericOutputPortStatsPort_Object = MibTableColumn
genericOutputPortStatsPort = _GenericOutputPortStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 10, 2, 1, 3),
    _GenericOutputPortStatsPort_Type()
)
genericOutputPortStatsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericOutputPortStatsPort.setStatus("current")
_GenericOutputPortStatsPrio_Type = Integer32
_GenericOutputPortStatsPrio_Object = MibTableColumn
genericOutputPortStatsPrio = _GenericOutputPortStatsPrio_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 10, 2, 1, 4),
    _GenericOutputPortStatsPrio_Type()
)
genericOutputPortStatsPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericOutputPortStatsPrio.setStatus("current")
_GenericOutputPortStatsPrioTransmittedCells_Type = Counter32
_GenericOutputPortStatsPrioTransmittedCells_Object = MibTableColumn
genericOutputPortStatsPrioTransmittedCells = _GenericOutputPortStatsPrioTransmittedCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 10, 2, 1, 5),
    _GenericOutputPortStatsPrioTransmittedCells_Type()
)
genericOutputPortStatsPrioTransmittedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericOutputPortStatsPrioTransmittedCells.setStatus("current")
_GenericOutputPortStatsPrioClp1LostCells_Type = Counter32
_GenericOutputPortStatsPrioClp1LostCells_Object = MibTableColumn
genericOutputPortStatsPrioClp1LostCells = _GenericOutputPortStatsPrioClp1LostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 10, 2, 1, 6),
    _GenericOutputPortStatsPrioClp1LostCells_Type()
)
genericOutputPortStatsPrioClp1LostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericOutputPortStatsPrioClp1LostCells.setStatus("current")
_GenericOutputPortStatsPrioClp01LostCells_Type = Counter32
_GenericOutputPortStatsPrioClp01LostCells_Object = MibTableColumn
genericOutputPortStatsPrioClp01LostCells = _GenericOutputPortStatsPrioClp01LostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 10, 2, 1, 7),
    _GenericOutputPortStatsPrioClp01LostCells_Type()
)
genericOutputPortStatsPrioClp01LostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericOutputPortStatsPrioClp01LostCells.setStatus("current")
_GenericOutputPortStatsPrioName_Type = DisplayString
_GenericOutputPortStatsPrioName_Object = MibTableColumn
genericOutputPortStatsPrioName = _GenericOutputPortStatsPrioName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 10, 2, 1, 8),
    _GenericOutputPortStatsPrioName_Type()
)
genericOutputPortStatsPrioName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericOutputPortStatsPrioName.setStatus("current")
_GenericOutputPortStatsAtmif_Type = Integer32
_GenericOutputPortStatsAtmif_Object = MibTableColumn
genericOutputPortStatsAtmif = _GenericOutputPortStatsAtmif_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 10, 2, 1, 9),
    _GenericOutputPortStatsAtmif_Type()
)
genericOutputPortStatsAtmif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericOutputPortStatsAtmif.setStatus("current")
_GenericOutputPortStatsPrioEpdPpdLostCells_Type = Counter32
_GenericOutputPortStatsPrioEpdPpdLostCells_Object = MibTableColumn
genericOutputPortStatsPrioEpdPpdLostCells = _GenericOutputPortStatsPrioEpdPpdLostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 10, 2, 1, 10),
    _GenericOutputPortStatsPrioEpdPpdLostCells_Type()
)
genericOutputPortStatsPrioEpdPpdLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericOutputPortStatsPrioEpdPpdLostCells.setStatus("current")
_DualScp_ObjectIdentity = ObjectIdentity
dualScp = _DualScp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 6)
)
_DualScpGroup_ObjectIdentity = ObjectIdentity
dualScpGroup = _DualScpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 6, 1)
)
_DualScpConfTable_Object = MibTable
dualScpConfTable = _DualScpConfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    dualScpConfTable.setStatus("current")
_DualScpConfEntry_Object = MibTableRow
dualScpConfEntry = _DualScpConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 6, 1, 1, 1)
)
dualScpConfEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "boardIndex"),
)
if mibBuilder.loadTexts:
    dualScpConfEntry.setStatus("current")


class _DualScpSlot_Type(Integer32):
    """Custom type dualScpSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("slotX", 1),
          ("slotY", 2))
    )


_DualScpSlot_Type.__name__ = "Integer32"
_DualScpSlot_Object = MibTableColumn
dualScpSlot = _DualScpSlot_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 6, 1, 1, 1, 1),
    _DualScpSlot_Type()
)
dualScpSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualScpSlot.setStatus("current")


class _DualScpState_Type(Integer32):
    """Custom type dualScpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dual", 2),
          ("other", 3),
          ("standalone", 1))
    )


_DualScpState_Type.__name__ = "Integer32"
_DualScpState_Object = MibTableColumn
dualScpState = _DualScpState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 6, 1, 1, 1, 2),
    _DualScpState_Type()
)
dualScpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualScpState.setStatus("current")
_DualScpSyncState_Type = DisplayString
_DualScpSyncState_Object = MibTableColumn
dualScpSyncState = _DualScpSyncState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 6, 1, 1, 1, 3),
    _DualScpSyncState_Type()
)
dualScpSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualScpSyncState.setStatus("current")


class _DualScpPrimary_Type(Integer32):
    """Custom type dualScpPrimary based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("slotX", 1),
          ("slotY", 2))
    )


_DualScpPrimary_Type.__name__ = "Integer32"
_DualScpPrimary_Object = MibTableColumn
dualScpPrimary = _DualScpPrimary_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 6, 1, 1, 1, 4),
    _DualScpPrimary_Type()
)
dualScpPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dualScpPrimary.setStatus("current")


class _DualScpFailover_Type(Integer32):
    """Custom type dualScpFailover based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_DualScpFailover_Type.__name__ = "Integer32"
_DualScpFailover_Object = MibTableColumn
dualScpFailover = _DualScpFailover_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 6, 1, 1, 1, 5),
    _DualScpFailover_Type()
)
dualScpFailover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dualScpFailover.setStatus("current")


class _DualScpManualSyncRequest_Type(Integer32):
    """Custom type dualScpManualSyncRequest based on Integer32"""
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
              9,
              10,
              12)
        )
    )
    namedValues = NamedValues(
        *(("syncCdb", 3),
          ("syncFlash", 2),
          ("syncIdle", 1),
          ("syncInit", 7),
          ("syncKrb5KeyTab", 12),
          ("syncLecsConfig", 5),
          ("syncLoader", 10),
          ("syncOS", 6),
          ("syncPassword", 4),
          ("syncSecret", 9),
          ("syncSecurid", 8))
    )


_DualScpManualSyncRequest_Type.__name__ = "Integer32"
_DualScpManualSyncRequest_Object = MibTableColumn
dualScpManualSyncRequest = _DualScpManualSyncRequest_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 6, 1, 1, 1, 6),
    _DualScpManualSyncRequest_Type()
)
dualScpManualSyncRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dualScpManualSyncRequest.setStatus("current")


class _DualScpCdbSyncMode_Type(Integer32):
    """Custom type dualScpCdbSyncMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 2),
          ("manual", 1))
    )


_DualScpCdbSyncMode_Type.__name__ = "Integer32"
_DualScpCdbSyncMode_Object = MibTableColumn
dualScpCdbSyncMode = _DualScpCdbSyncMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 6, 1, 1, 1, 7),
    _DualScpCdbSyncMode_Type()
)
dualScpCdbSyncMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dualScpCdbSyncMode.setStatus("current")


class _DualScpManualSwitchOver_Type(Integer32):
    """Custom type dualScpManualSwitchOver based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_DualScpManualSwitchOver_Type.__name__ = "Integer32"
_DualScpManualSwitchOver_Object = MibTableColumn
dualScpManualSwitchOver = _DualScpManualSwitchOver_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 6, 1, 1, 1, 8),
    _DualScpManualSwitchOver_Type()
)
dualScpManualSwitchOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dualScpManualSwitchOver.setStatus("current")
_DualScpSwitchOverTime_Type = DateAndTime
_DualScpSwitchOverTime_Object = MibTableColumn
dualScpSwitchOverTime = _DualScpSwitchOverTime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 6, 1, 1, 1, 9),
    _DualScpSwitchOverTime_Type()
)
dualScpSwitchOverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualScpSwitchOverTime.setStatus("current")


class _DualScpSwitchOverThreshold_Type(Integer32):
    """Custom type dualScpSwitchOverThreshold based on Integer32"""
    defaultValue = 2


_DualScpSwitchOverThreshold_Object = MibTableColumn
dualScpSwitchOverThreshold = _DualScpSwitchOverThreshold_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 6, 1, 1, 1, 10),
    _DualScpSwitchOverThreshold_Type()
)
dualScpSwitchOverThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dualScpSwitchOverThreshold.setStatus("current")
_DualScpSyncRequestList_Type = IntegerBitString
_DualScpSyncRequestList_Object = MibTableColumn
dualScpSyncRequestList = _DualScpSyncRequestList_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 6, 1, 1, 1, 11),
    _DualScpSyncRequestList_Type()
)
dualScpSyncRequestList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualScpSyncRequestList.setStatus("current")
_DualScpNumSyncRequests_Type = Counter32
_DualScpNumSyncRequests_Object = MibTableColumn
dualScpNumSyncRequests = _DualScpNumSyncRequests_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 6, 1, 1, 1, 12),
    _DualScpNumSyncRequests_Type()
)
dualScpNumSyncRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualScpNumSyncRequests.setStatus("current")
_DualScpNumSyncFailures_Type = Counter32
_DualScpNumSyncFailures_Object = MibTableColumn
dualScpNumSyncFailures = _DualScpNumSyncFailures_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 6, 1, 1, 1, 13),
    _DualScpNumSyncFailures_Type()
)
dualScpNumSyncFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualScpNumSyncFailures.setStatus("current")


class _DualScpResetStandbyScp_Type(Integer32):
    """Custom type dualScpResetStandbyScp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_DualScpResetStandbyScp_Type.__name__ = "Integer32"
_DualScpResetStandbyScp_Object = MibTableColumn
dualScpResetStandbyScp = _DualScpResetStandbyScp_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 6, 1, 1, 1, 14),
    _DualScpResetStandbyScp_Type()
)
dualScpResetStandbyScp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dualScpResetStandbyScp.setStatus("current")


class _DualScpAutoRemoveOldFiles_Type(Integer32):
    """Custom type dualScpAutoRemoveOldFiles based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_DualScpAutoRemoveOldFiles_Type.__name__ = "Integer32"
_DualScpAutoRemoveOldFiles_Object = MibTableColumn
dualScpAutoRemoveOldFiles = _DualScpAutoRemoveOldFiles_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 6, 1, 1, 1, 15),
    _DualScpAutoRemoveOldFiles_Type()
)
dualScpAutoRemoveOldFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dualScpAutoRemoveOldFiles.setStatus("current")
_DualScpRedundancyState_Type = DisplayString
_DualScpRedundancyState_Object = MibTableColumn
dualScpRedundancyState = _DualScpRedundancyState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 6, 1, 1, 1, 16),
    _DualScpRedundancyState_Type()
)
dualScpRedundancyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualScpRedundancyState.setStatus("current")


class _DualScpSVXCPStateSyncPercent_Type(Gauge32):
    """Custom type dualScpSVXCPStateSyncPercent based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DualScpSVXCPStateSyncPercent_Type.__name__ = "Gauge32"
_DualScpSVXCPStateSyncPercent_Object = MibTableColumn
dualScpSVXCPStateSyncPercent = _DualScpSVXCPStateSyncPercent_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 6, 1, 1, 1, 17),
    _DualScpSVXCPStateSyncPercent_Type()
)
dualScpSVXCPStateSyncPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualScpSVXCPStateSyncPercent.setStatus("current")


class _DualScpSVXCPStateTransferFailed_Type(Integer32):
    """Custom type dualScpSVXCPStateTransferFailed based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("ok", 2))
    )


_DualScpSVXCPStateTransferFailed_Type.__name__ = "Integer32"
_DualScpSVXCPStateTransferFailed_Object = MibTableColumn
dualScpSVXCPStateTransferFailed = _DualScpSVXCPStateTransferFailed_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 6, 1, 1, 1, 18),
    _DualScpSVXCPStateTransferFailed_Type()
)
dualScpSVXCPStateTransferFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualScpSVXCPStateTransferFailed.setStatus("current")
_DualScpSVXCPdroppedCallCount_Type = Integer32
_DualScpSVXCPdroppedCallCount_Object = MibTableColumn
dualScpSVXCPdroppedCallCount = _DualScpSVXCPdroppedCallCount_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 6, 1, 1, 1, 19),
    _DualScpSVXCPdroppedCallCount_Type()
)
dualScpSVXCPdroppedCallCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualScpSVXCPdroppedCallCount.setStatus("current")
_EtherChipSet_ObjectIdentity = ObjectIdentity
etherChipSet = _EtherChipSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 10)
)
_EtherChipSetDec_ObjectIdentity = ObjectIdentity
etherChipSetDec = _EtherChipSetDec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 10, 1)
)
_EtherChipSetDec21440_ObjectIdentity = ObjectIdentity
etherChipSetDec21440 = _EtherChipSetDec21440_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 10, 1, 1)
)
_SwitchGroup_ObjectIdentity = ObjectIdentity
switchGroup = _SwitchGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1)
)
_HardwareVersion_Type = Integer32
_HardwareVersion_Object = MibScalar
hardwareVersion = _HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 1),
    _HardwareVersion_Type()
)
hardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareVersion.setStatus("current")
_SoftwareVersion_Type = Integer32
_SoftwareVersion_Object = MibScalar
softwareVersion = _SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 2),
    _SoftwareVersion_Type()
)
softwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersion.setStatus("current")
_MaxPaths_Type = Integer32
_MaxPaths_Object = MibScalar
maxPaths = _MaxPaths_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 3),
    _MaxPaths_Type()
)
maxPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxPaths.setStatus("current")
_MaxChannels_Type = Integer32
_MaxChannels_Object = MibScalar
maxChannels = _MaxChannels_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 4),
    _MaxChannels_Type()
)
maxChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxChannels.setStatus("current")
_AtmAddress_Type = SpansAddress
_AtmAddress_Object = MibScalar
atmAddress = _AtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 5),
    _AtmAddress_Type()
)
atmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAddress.setStatus("current")
_Uptime_Type = TimeTicks
_Uptime_Object = MibScalar
uptime = _Uptime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 6),
    _Uptime_Type()
)
uptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uptime.setStatus("current")
_SwitchCDV_Type = Integer32
_SwitchCDV_Object = MibScalar
switchCDV = _SwitchCDV_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 7),
    _SwitchCDV_Type()
)
switchCDV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchCDV.setStatus("obsolete")


class _SwitchPolicingAction_Type(Integer32):
    """Custom type switchPolicingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("tag", 1))
    )


_SwitchPolicingAction_Type.__name__ = "Integer32"
_SwitchPolicingAction_Object = MibScalar
switchPolicingAction = _SwitchPolicingAction_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 8),
    _SwitchPolicingAction_Type()
)
switchPolicingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchPolicingAction.setStatus("obsolete")
_SoftwareVersionText_Type = DisplayString
_SoftwareVersionText_Object = MibScalar
softwareVersionText = _SoftwareVersionText_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 9),
    _SoftwareVersionText_Type()
)
softwareVersionText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersionText.setStatus("current")


class _SwitchType_Type(Integer32):
    """Custom type switchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              15,
              16,
              17,
              18,
              19,
              20,
              22)
        )
    )
    namedValues = NamedValues(
        *(("asx100", 1),
          ("asx1000", 8),
          ("asx1200", 17),
          ("asx150", 22),
          ("asx200", 2),
          ("asx200bx", 5),
          ("asx200bxe", 6),
          ("asx200wg", 4),
          ("asx4000", 18),
          ("cabletron9A000", 7),
          ("esx3000", 20),
          ("le155", 9),
          ("le25", 19),
          ("sfcs1000", 12),
          ("sfcs200bx", 11),
          ("sfcs200wg", 10),
          ("tnx1100", 16),
          ("tnx210", 15))
    )


_SwitchType_Type.__name__ = "Integer32"
_SwitchType_Object = MibScalar
switchType = _SwitchType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 10),
    _SwitchType_Type()
)
switchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchType.setStatus("current")
_SwitchReservedPMPMinVCI_Type = Integer32
_SwitchReservedPMPMinVCI_Object = MibScalar
switchReservedPMPMinVCI = _SwitchReservedPMPMinVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 12),
    _SwitchReservedPMPMinVCI_Type()
)
switchReservedPMPMinVCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchReservedPMPMinVCI.setStatus("current")
_SwitchReservedPMPMaxVCI_Type = Integer32
_SwitchReservedPMPMaxVCI_Object = MibScalar
switchReservedPMPMaxVCI = _SwitchReservedPMPMaxVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 13),
    _SwitchReservedPMPMaxVCI_Type()
)
switchReservedPMPMaxVCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchReservedPMPMaxVCI.setStatus("current")


class _SwitchTimeZone_Type(DisplayString):
    """Custom type switchTimeZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwitchTimeZone_Type.__name__ = "DisplayString"
_SwitchTimeZone_Object = MibScalar
switchTimeZone = _SwitchTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 14),
    _SwitchTimeZone_Type()
)
switchTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchTimeZone.setStatus("current")
_SwitchGMTime_Type = DateAndTime
_SwitchGMTime_Object = MibScalar
switchGMTime = _SwitchGMTime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 15),
    _SwitchGMTime_Type()
)
switchGMTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchGMTime.setStatus("current")


class _SwitchProtocolType_Type(Integer32):
    """Custom type switchProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 2),
          ("tftp", 1))
    )


_SwitchProtocolType_Type.__name__ = "Integer32"
_SwitchProtocolType_Object = MibScalar
switchProtocolType = _SwitchProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 16),
    _SwitchProtocolType_Type()
)
switchProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchProtocolType.setStatus("current")
_SwitchCurrentUserid_Type = DisplayString
_SwitchCurrentUserid_Object = MibScalar
switchCurrentUserid = _SwitchCurrentUserid_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 17),
    _SwitchCurrentUserid_Type()
)
switchCurrentUserid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCurrentUserid.setStatus("current")
_SwitchCurrentLoginFrom_Type = DisplayString
_SwitchCurrentLoginFrom_Object = MibScalar
switchCurrentLoginFrom = _SwitchCurrentLoginFrom_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 18),
    _SwitchCurrentLoginFrom_Type()
)
switchCurrentLoginFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCurrentLoginFrom.setStatus("current")
_SwitchPrimaryClock_Type = Integer32
_SwitchPrimaryClock_Object = MibScalar
switchPrimaryClock = _SwitchPrimaryClock_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 19),
    _SwitchPrimaryClock_Type()
)
switchPrimaryClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchPrimaryClock.setStatus("deprecated")
_SwitchSecondaryClock_Type = Integer32
_SwitchSecondaryClock_Object = MibScalar
switchSecondaryClock = _SwitchSecondaryClock_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 20),
    _SwitchSecondaryClock_Type()
)
switchSecondaryClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchSecondaryClock.setStatus("deprecated")


class _SwitchClockOperStatus_Type(Integer32):
    """Custom type switchClockOperStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("crystalAClock", 3),
          ("crystalBClock", 4),
          ("crystalCClock", 5),
          ("crystalDClock", 6),
          ("localCrystalClock", 8),
          ("primaryClock", 1),
          ("primaryClockPartner", 9),
          ("secondaryClock", 2),
          ("secondaryClockPartner", 10),
          ("tcmClock", 7))
    )


_SwitchClockOperStatus_Type.__name__ = "Integer32"
_SwitchClockOperStatus_Object = MibScalar
switchClockOperStatus = _SwitchClockOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 21),
    _SwitchClockOperStatus_Type()
)
switchClockOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchClockOperStatus.setStatus("deprecated")


class _SwitchTimingMode_Type(Integer32):
    """Custom type switchTimingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("switchMode", 1),
          ("tcmMode", 3))
    )


_SwitchTimingMode_Type.__name__ = "Integer32"
_SwitchTimingMode_Object = MibScalar
switchTimingMode = _SwitchTimingMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 22),
    _SwitchTimingMode_Type()
)
switchTimingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchTimingMode.setStatus("current")


class _SwitchConnectionPreservation_Type(Integer32):
    """Custom type switchConnectionPreservation based on Integer32"""
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


_SwitchConnectionPreservation_Type.__name__ = "Integer32"
_SwitchConnectionPreservation_Object = MibScalar
switchConnectionPreservation = _SwitchConnectionPreservation_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 23),
    _SwitchConnectionPreservation_Type()
)
switchConnectionPreservation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchConnectionPreservation.setStatus("current")


class _SwitchATMLayerOAM_Type(Integer32):
    """Custom type switchATMLayerOAM based on Integer32"""
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


_SwitchATMLayerOAM_Type.__name__ = "Integer32"
_SwitchATMLayerOAM_Object = MibScalar
switchATMLayerOAM = _SwitchATMLayerOAM_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 24),
    _SwitchATMLayerOAM_Type()
)
switchATMLayerOAM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchATMLayerOAM.setStatus("current")


class _SwitchHttpServer_Type(Integer32):
    """Custom type switchHttpServer based on Integer32"""
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


_SwitchHttpServer_Type.__name__ = "Integer32"
_SwitchHttpServer_Object = MibScalar
switchHttpServer = _SwitchHttpServer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 25),
    _SwitchHttpServer_Type()
)
switchHttpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchHttpServer.setStatus("current")
_SwitchHttpHelpUrl_Type = DisplayString
_SwitchHttpHelpUrl_Object = MibScalar
switchHttpHelpUrl = _SwitchHttpHelpUrl_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 26),
    _SwitchHttpHelpUrl_Type()
)
switchHttpHelpUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchHttpHelpUrl.setStatus("current")
_McastGroup_ObjectIdentity = ObjectIdentity
mcastGroup = _McastGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 27)
)
_McastSpaceTable_Object = MibTable
mcastSpaceTable = _McastSpaceTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 27, 1)
)
if mibBuilder.loadTexts:
    mcastSpaceTable.setStatus("current")
_McastSpaceEntry_Object = MibTableRow
mcastSpaceEntry = _McastSpaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 27, 1, 1)
)
mcastSpaceEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "mcastSpaceIndex"),
)
if mibBuilder.loadTexts:
    mcastSpaceEntry.setStatus("current")
_McastSpaceIndex_Type = Integer32
_McastSpaceIndex_Object = MibTableColumn
mcastSpaceIndex = _McastSpaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 27, 1, 1, 1),
    _McastSpaceIndex_Type()
)
mcastSpaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mcastSpaceIndex.setStatus("current")
_McastSpaceNumConn_Type = Integer32
_McastSpaceNumConn_Object = MibTableColumn
mcastSpaceNumConn = _McastSpaceNumConn_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 27, 1, 1, 2),
    _McastSpaceNumConn_Type()
)
mcastSpaceNumConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcastSpaceNumConn.setStatus("current")
_McastSpaceName_Type = DisplayString
_McastSpaceName_Object = MibTableColumn
mcastSpaceName = _McastSpaceName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 27, 1, 1, 3),
    _McastSpaceName_Type()
)
mcastSpaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcastSpaceName.setStatus("current")
_SwitchCtrlLinkid_Type = Integer32
_SwitchCtrlLinkid_Object = MibScalar
switchCtrlLinkid = _SwitchCtrlLinkid_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 28),
    _SwitchCtrlLinkid_Type()
)
switchCtrlLinkid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCtrlLinkid.setStatus("current")
_SwitchClockCurrentStatus_Type = DisplayString
_SwitchClockCurrentStatus_Object = MibScalar
switchClockCurrentStatus = _SwitchClockCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 29),
    _SwitchClockCurrentStatus_Type()
)
switchClockCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchClockCurrentStatus.setStatus("current")
_SwitchDebounceTable_Object = MibTable
switchDebounceTable = _SwitchDebounceTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 30)
)
if mibBuilder.loadTexts:
    switchDebounceTable.setStatus("current")
_SwitchDebounceEntry_Object = MibTableRow
switchDebounceEntry = _SwitchDebounceEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 30, 1)
)
switchDebounceEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "switchDebounceIndex"),
)
if mibBuilder.loadTexts:
    switchDebounceEntry.setStatus("current")
_SwitchDebounceIndex_Type = Integer32
_SwitchDebounceIndex_Object = MibTableColumn
switchDebounceIndex = _SwitchDebounceIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 30, 1, 1),
    _SwitchDebounceIndex_Type()
)
switchDebounceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchDebounceIndex.setStatus("current")
_SwitchDebounceName_Type = DisplayString
_SwitchDebounceName_Object = MibTableColumn
switchDebounceName = _SwitchDebounceName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 30, 1, 2),
    _SwitchDebounceName_Type()
)
switchDebounceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchDebounceName.setStatus("current")
_SwitchDebounceHysteresis_Type = Integer32
_SwitchDebounceHysteresis_Object = MibTableColumn
switchDebounceHysteresis = _SwitchDebounceHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 30, 1, 3),
    _SwitchDebounceHysteresis_Type()
)
switchDebounceHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchDebounceHysteresis.setStatus("current")


class _SoftwareLicenseKey_Type(DisplayString):
    """Custom type softwareLicenseKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SoftwareLicenseKey_Type.__name__ = "DisplayString"
_SoftwareLicenseKey_Object = MibScalar
softwareLicenseKey = _SoftwareLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 31),
    _SoftwareLicenseKey_Type()
)
softwareLicenseKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareLicenseKey.setStatus("current")
_SwitchCounterResetTime_Type = TimeStamp
_SwitchCounterResetTime_Object = MibScalar
switchCounterResetTime = _SwitchCounterResetTime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 32),
    _SwitchCounterResetTime_Type()
)
switchCounterResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCounterResetTime.setStatus("current")


class _SwitchCounterReset_Type(Integer32):
    """Custom type switchCounterReset based on Integer32"""
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
        *(("resetFalse", 4),
          ("resetRequest", 1),
          ("resetTrue", 3),
          ("unresetRequest", 2))
    )


_SwitchCounterReset_Type.__name__ = "Integer32"
_SwitchCounterReset_Object = MibScalar
switchCounterReset = _SwitchCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 33),
    _SwitchCounterReset_Type()
)
switchCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchCounterReset.setStatus("current")
_SwitchSbprServerAddressTable_Object = MibTable
switchSbprServerAddressTable = _SwitchSbprServerAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 34)
)
if mibBuilder.loadTexts:
    switchSbprServerAddressTable.setStatus("current")
_SwitchSbprServerAddressEntry_Object = MibTableRow
switchSbprServerAddressEntry = _SwitchSbprServerAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 34, 1)
)
switchSbprServerAddressEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "sbprServerAddressIndex"),
)
if mibBuilder.loadTexts:
    switchSbprServerAddressEntry.setStatus("current")
_SbprServerAddressIndex_Type = Integer32
_SbprServerAddressIndex_Object = MibTableColumn
sbprServerAddressIndex = _SbprServerAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 34, 1, 1),
    _SbprServerAddressIndex_Type()
)
sbprServerAddressIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbprServerAddressIndex.setStatus("current")


class _SbprServerAddressIndexName_Type(DisplayString):
    """Custom type sbprServerAddressIndexName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SbprServerAddressIndexName_Type.__name__ = "DisplayString"
_SbprServerAddressIndexName_Object = MibTableColumn
sbprServerAddressIndexName = _SbprServerAddressIndexName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 34, 1, 2),
    _SbprServerAddressIndexName_Type()
)
sbprServerAddressIndexName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbprServerAddressIndexName.setStatus("current")


class _SbprServerMaxHops_Type(Integer32):
    """Custom type sbprServerMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SbprServerMaxHops_Type.__name__ = "Integer32"
_SbprServerMaxHops_Object = MibTableColumn
sbprServerMaxHops = _SbprServerMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 34, 1, 3),
    _SbprServerMaxHops_Type()
)
sbprServerMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbprServerMaxHops.setStatus("current")


class _SbprServerMinSeconds_Type(Integer32):
    """Custom type sbprServerMinSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SbprServerMinSeconds_Type.__name__ = "Integer32"
_SbprServerMinSeconds_Object = MibTableColumn
sbprServerMinSeconds = _SbprServerMinSeconds_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 34, 1, 4),
    _SbprServerMinSeconds_Type()
)
sbprServerMinSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbprServerMinSeconds.setStatus("current")
_SbprServerAddress1_Type = IpAddress
_SbprServerAddress1_Object = MibTableColumn
sbprServerAddress1 = _SbprServerAddress1_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 34, 1, 5),
    _SbprServerAddress1_Type()
)
sbprServerAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbprServerAddress1.setStatus("current")
_SbprServerAddress2_Type = IpAddress
_SbprServerAddress2_Object = MibTableColumn
sbprServerAddress2 = _SbprServerAddress2_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 34, 1, 6),
    _SbprServerAddress2_Type()
)
sbprServerAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbprServerAddress2.setStatus("current")
_SbprServerAddress3_Type = IpAddress
_SbprServerAddress3_Object = MibTableColumn
sbprServerAddress3 = _SbprServerAddress3_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 34, 1, 7),
    _SbprServerAddress3_Type()
)
sbprServerAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbprServerAddress3.setStatus("current")
_SbprServerAddress4_Type = IpAddress
_SbprServerAddress4_Object = MibTableColumn
sbprServerAddress4 = _SbprServerAddress4_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 34, 1, 8),
    _SbprServerAddress4_Type()
)
sbprServerAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbprServerAddress4.setStatus("current")
_SbprServerAddress5_Type = IpAddress
_SbprServerAddress5_Object = MibTableColumn
sbprServerAddress5 = _SbprServerAddress5_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 34, 1, 9),
    _SbprServerAddress5_Type()
)
sbprServerAddress5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbprServerAddress5.setStatus("current")
_SbprServerRowStatus_Type = RowStatus
_SbprServerRowStatus_Object = MibTableColumn
sbprServerRowStatus = _SbprServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 34, 1, 10),
    _SbprServerRowStatus_Type()
)
sbprServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbprServerRowStatus.setStatus("current")


class _SwitchPrimaryClockPort_Type(DisplayString):
    """Custom type switchPrimaryClockPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_SwitchPrimaryClockPort_Type.__name__ = "DisplayString"
_SwitchPrimaryClockPort_Object = MibScalar
switchPrimaryClockPort = _SwitchPrimaryClockPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 35),
    _SwitchPrimaryClockPort_Type()
)
switchPrimaryClockPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchPrimaryClockPort.setStatus("current")


class _SwitchSecondaryClockPort_Type(DisplayString):
    """Custom type switchSecondaryClockPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_SwitchSecondaryClockPort_Type.__name__ = "DisplayString"
_SwitchSecondaryClockPort_Object = MibScalar
switchSecondaryClockPort = _SwitchSecondaryClockPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 36),
    _SwitchSecondaryClockPort_Type()
)
switchSecondaryClockPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchSecondaryClockPort.setStatus("current")
_ServiceCategoryTable_Object = MibTable
serviceCategoryTable = _ServiceCategoryTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 37)
)
if mibBuilder.loadTexts:
    serviceCategoryTable.setStatus("current")
_ServiceCategoryEntry_Object = MibTableRow
serviceCategoryEntry = _ServiceCategoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 37, 1)
)
serviceCategoryEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "serviceCategoryIndex"),
)
if mibBuilder.loadTexts:
    serviceCategoryEntry.setStatus("current")
_ServiceCategoryIndex_Type = Integer32
_ServiceCategoryIndex_Object = MibTableColumn
serviceCategoryIndex = _ServiceCategoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 37, 1, 1),
    _ServiceCategoryIndex_Type()
)
serviceCategoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceCategoryIndex.setStatus("current")
_ServiceCategoryName_Type = DisplayString
_ServiceCategoryName_Object = MibTableColumn
serviceCategoryName = _ServiceCategoryName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 37, 1, 2),
    _ServiceCategoryName_Type()
)
serviceCategoryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceCategoryName.setStatus("current")


class _SwitchPmpEnable_Type(Integer32):
    """Custom type switchPmpEnable based on Integer32"""
    defaultValue = 2

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


_SwitchPmpEnable_Type.__name__ = "Integer32"
_SwitchPmpEnable_Object = MibScalar
switchPmpEnable = _SwitchPmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 38),
    _SwitchPmpEnable_Type()
)
switchPmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchPmpEnable.setStatus("current")


class _SwitchCallPreservation_Type(Integer32):
    """Custom type switchCallPreservation based on Integer32"""
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


_SwitchCallPreservation_Type.__name__ = "Integer32"
_SwitchCallPreservation_Object = MibScalar
switchCallPreservation = _SwitchCallPreservation_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 39),
    _SwitchCallPreservation_Type()
)
switchCallPreservation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchCallPreservation.setStatus("current")


class _SwitchCallPresOperStatus_Type(Integer32):
    """Custom type switchCallPresOperStatus based on Integer32"""
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


_SwitchCallPresOperStatus_Type.__name__ = "Integer32"
_SwitchCallPresOperStatus_Object = MibScalar
switchCallPresOperStatus = _SwitchCallPresOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 1, 40),
    _SwitchCallPresOperStatus_Type()
)
switchCallPresOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCallPresOperStatus.setStatus("current")
_PortGroup_ObjectIdentity = ObjectIdentity
portGroup = _PortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2)
)
_NumberOfPorts_Type = Integer32
_NumberOfPorts_Object = MibScalar
numberOfPorts = _NumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 1),
    _NumberOfPorts_Type()
)
numberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfPorts.setStatus("current")
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    portTable.setStatus("current")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1)
)
portEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "portNumber"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("current")
_PortNumber_Type = Integer32
_PortNumber_Object = MibTableColumn
portNumber = _PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 1),
    _PortNumber_Type()
)
portNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portNumber.setStatus("current")


class _PortAdminStatus_Type(Integer32):
    """Custom type portAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 3))
    )


_PortAdminStatus_Type.__name__ = "Integer32"
_PortAdminStatus_Object = MibTableColumn
portAdminStatus = _PortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 2),
    _PortAdminStatus_Type()
)
portAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAdminStatus.setStatus("current")


class _PortOperStatus_Type(Integer32):
    """Custom type portOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_PortOperStatus_Type.__name__ = "Integer32"
_PortOperStatus_Object = MibTableColumn
portOperStatus = _PortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 3),
    _PortOperStatus_Type()
)
portOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOperStatus.setStatus("current")
_PortTime_Type = TimeTicks
_PortTime_Object = MibTableColumn
portTime = _PortTime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 4),
    _PortTime_Type()
)
portTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTime.setStatus("current")
_PortRemoteAtmAddress_Type = SpansAddress
_PortRemoteAtmAddress_Object = MibTableColumn
portRemoteAtmAddress = _PortRemoteAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 5),
    _PortRemoteAtmAddress_Type()
)
portRemoteAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portRemoteAtmAddress.setStatus("current")
_PortRemoteIpAddress_Type = IpAddress
_PortRemoteIpAddress_Object = MibTableColumn
portRemoteIpAddress = _PortRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 6),
    _PortRemoteIpAddress_Type()
)
portRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portRemoteIpAddress.setStatus("current")
_PortMaxPathsIn_Type = Integer32
_PortMaxPathsIn_Object = MibTableColumn
portMaxPathsIn = _PortMaxPathsIn_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 7),
    _PortMaxPathsIn_Type()
)
portMaxPathsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMaxPathsIn.setStatus("current")
_PortNumPathsIn_Type = Gauge32
_PortNumPathsIn_Object = MibTableColumn
portNumPathsIn = _PortNumPathsIn_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 8),
    _PortNumPathsIn_Type()
)
portNumPathsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portNumPathsIn.setStatus("current")
_PortMaxBandwidthIn_Type = Integer32
_PortMaxBandwidthIn_Object = MibTableColumn
portMaxBandwidthIn = _PortMaxBandwidthIn_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 9),
    _PortMaxBandwidthIn_Type()
)
portMaxBandwidthIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMaxBandwidthIn.setStatus("current")
_PortAllocBandwidthIn_Type = Gauge32
_PortAllocBandwidthIn_Object = MibTableColumn
portAllocBandwidthIn = _PortAllocBandwidthIn_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 10),
    _PortAllocBandwidthIn_Type()
)
portAllocBandwidthIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAllocBandwidthIn.setStatus("current")
_PortUsedBandwidthIn_Type = Gauge32
_PortUsedBandwidthIn_Object = MibTableColumn
portUsedBandwidthIn = _PortUsedBandwidthIn_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 11),
    _PortUsedBandwidthIn_Type()
)
portUsedBandwidthIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portUsedBandwidthIn.setStatus("deprecated")
_PortReceivedCells_Type = Counter32
_PortReceivedCells_Object = MibTableColumn
portReceivedCells = _PortReceivedCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 12),
    _PortReceivedCells_Type()
)
portReceivedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portReceivedCells.setStatus("current")
_PortMaxPathsOut_Type = Integer32
_PortMaxPathsOut_Object = MibTableColumn
portMaxPathsOut = _PortMaxPathsOut_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 13),
    _PortMaxPathsOut_Type()
)
portMaxPathsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMaxPathsOut.setStatus("current")
_PortNumPathsOut_Type = Gauge32
_PortNumPathsOut_Object = MibTableColumn
portNumPathsOut = _PortNumPathsOut_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 14),
    _PortNumPathsOut_Type()
)
portNumPathsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portNumPathsOut.setStatus("current")
_PortMaxBandwidthOut_Type = Integer32
_PortMaxBandwidthOut_Object = MibTableColumn
portMaxBandwidthOut = _PortMaxBandwidthOut_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 15),
    _PortMaxBandwidthOut_Type()
)
portMaxBandwidthOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMaxBandwidthOut.setStatus("current")
_PortAllocBandwidthOut_Type = Gauge32
_PortAllocBandwidthOut_Object = MibTableColumn
portAllocBandwidthOut = _PortAllocBandwidthOut_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 16),
    _PortAllocBandwidthOut_Type()
)
portAllocBandwidthOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAllocBandwidthOut.setStatus("current")
_PortUsedBandwidthOut_Type = Gauge32
_PortUsedBandwidthOut_Object = MibTableColumn
portUsedBandwidthOut = _PortUsedBandwidthOut_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 17),
    _PortUsedBandwidthOut_Type()
)
portUsedBandwidthOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portUsedBandwidthOut.setStatus("deprecated")
_PortTransmittedCells_Type = Counter32
_PortTransmittedCells_Object = MibTableColumn
portTransmittedCells = _PortTransmittedCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 18),
    _PortTransmittedCells_Type()
)
portTransmittedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTransmittedCells.setStatus("current")
_PortHwBoard_Type = Integer32
_PortHwBoard_Object = MibTableColumn
portHwBoard = _PortHwBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 19),
    _PortHwBoard_Type()
)
portHwBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHwBoard.setStatus("current")
_PortHwModule_Type = Integer32
_PortHwModule_Object = MibTableColumn
portHwModule = _PortHwModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 20),
    _PortHwModule_Type()
)
portHwModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHwModule.setStatus("current")
_PortHwNumber_Type = Integer32
_PortHwNumber_Object = MibTableColumn
portHwNumber = _PortHwNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 21),
    _PortHwNumber_Type()
)
portHwNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHwNumber.setStatus("deprecated")
_PortILMIRemoteIpAddress_Type = IpAddress
_PortILMIRemoteIpAddress_Object = MibTableColumn
portILMIRemoteIpAddress = _PortILMIRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 22),
    _PortILMIRemoteIpAddress_Type()
)
portILMIRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portILMIRemoteIpAddress.setStatus("current")
_PortCDVT_Type = Integer32
_PortCDVT_Object = MibTableColumn
portCDVT = _PortCDVT_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 23),
    _PortCDVT_Type()
)
portCDVT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCDVT.setStatus("current")


class _PortInputPolicingStatus_Type(Integer32):
    """Custom type portInputPolicingStatus based on Integer32"""
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


_PortInputPolicingStatus_Type.__name__ = "Integer32"
_PortInputPolicingStatus_Object = MibTableColumn
portInputPolicingStatus = _PortInputPolicingStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 24),
    _PortInputPolicingStatus_Type()
)
portInputPolicingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portInputPolicingStatus.setStatus("deprecated")


class _PortVbrOverbooking_Type(Integer32):
    """Custom type portVbrOverbooking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_PortVbrOverbooking_Type.__name__ = "Integer32"
_PortVbrOverbooking_Object = MibTableColumn
portVbrOverbooking = _PortVbrOverbooking_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 25),
    _PortVbrOverbooking_Type()
)
portVbrOverbooking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVbrOverbooking.setStatus("deprecated")


class _PortVbrBufferOverb_Type(Integer32):
    """Custom type portVbrBufferOverb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_PortVbrBufferOverb_Type.__name__ = "Integer32"
_PortVbrBufferOverb_Object = MibTableColumn
portVbrBufferOverb = _PortVbrBufferOverb_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 26),
    _PortVbrBufferOverb_Type()
)
portVbrBufferOverb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVbrBufferOverb.setStatus("deprecated")


class _PortManagementStatus_Type(Integer32):
    """Custom type portManagementStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("managed", 1),
          ("un-managed", 2))
    )


_PortManagementStatus_Type.__name__ = "Integer32"
_PortManagementStatus_Object = MibTableColumn
portManagementStatus = _PortManagementStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 27),
    _PortManagementStatus_Type()
)
portManagementStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portManagementStatus.setStatus("current")


class _PortAISRDIGeneration_Type(Integer32):
    """Custom type portAISRDIGeneration based on Integer32"""
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


_PortAISRDIGeneration_Type.__name__ = "Integer32"
_PortAISRDIGeneration_Object = MibTableColumn
portAISRDIGeneration = _PortAISRDIGeneration_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 28),
    _PortAISRDIGeneration_Type()
)
portAISRDIGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAISRDIGeneration.setStatus("current")


class _PortGCRAPolicingCBR_Type(Integer32):
    """Custom type portGCRAPolicingCBR based on Integer32"""
    defaultValue = 5

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
        *(("allOff", 2),
          ("allOn", 1),
          ("default", 5),
          ("svcOff", 4),
          ("svcOn", 3))
    )


_PortGCRAPolicingCBR_Type.__name__ = "Integer32"
_PortGCRAPolicingCBR_Object = MibTableColumn
portGCRAPolicingCBR = _PortGCRAPolicingCBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 33),
    _PortGCRAPolicingCBR_Type()
)
portGCRAPolicingCBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portGCRAPolicingCBR.setStatus("current")


class _PortGCRAPolicingVBR_Type(Integer32):
    """Custom type portGCRAPolicingVBR based on Integer32"""
    defaultValue = 5

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
        *(("allOff", 2),
          ("allOn", 1),
          ("default", 5),
          ("svcOff", 4),
          ("svcOn", 3))
    )


_PortGCRAPolicingVBR_Type.__name__ = "Integer32"
_PortGCRAPolicingVBR_Object = MibTableColumn
portGCRAPolicingVBR = _PortGCRAPolicingVBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 34),
    _PortGCRAPolicingVBR_Type()
)
portGCRAPolicingVBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portGCRAPolicingVBR.setStatus("deprecated")


class _PortAAL5PacketDiscardCBR_Type(Integer32):
    """Custom type portAAL5PacketDiscardCBR based on Integer32"""
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
        *(("allOff", 2),
          ("allOn", 1),
          ("svcOff", 4),
          ("svcOn", 3))
    )


_PortAAL5PacketDiscardCBR_Type.__name__ = "Integer32"
_PortAAL5PacketDiscardCBR_Object = MibTableColumn
portAAL5PacketDiscardCBR = _PortAAL5PacketDiscardCBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 35),
    _PortAAL5PacketDiscardCBR_Type()
)
portAAL5PacketDiscardCBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAAL5PacketDiscardCBR.setStatus("current")


class _PortAAL5PacketDiscardVBR_Type(Integer32):
    """Custom type portAAL5PacketDiscardVBR based on Integer32"""
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
        *(("allOff", 2),
          ("allOn", 1),
          ("svcOff", 4),
          ("svcOn", 3))
    )


_PortAAL5PacketDiscardVBR_Type.__name__ = "Integer32"
_PortAAL5PacketDiscardVBR_Object = MibTableColumn
portAAL5PacketDiscardVBR = _PortAAL5PacketDiscardVBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 36),
    _PortAAL5PacketDiscardVBR_Type()
)
portAAL5PacketDiscardVBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAAL5PacketDiscardVBR.setStatus("deprecated")


class _PortAAL5PacketDiscardUBR_Type(Integer32):
    """Custom type portAAL5PacketDiscardUBR based on Integer32"""
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
        *(("allOff", 2),
          ("allOn", 1),
          ("svcOff", 4),
          ("svcOn", 3))
    )


_PortAAL5PacketDiscardUBR_Type.__name__ = "Integer32"
_PortAAL5PacketDiscardUBR_Object = MibTableColumn
portAAL5PacketDiscardUBR = _PortAAL5PacketDiscardUBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 37),
    _PortAAL5PacketDiscardUBR_Type()
)
portAAL5PacketDiscardUBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAAL5PacketDiscardUBR.setStatus("current")
_PortInputCACErrors_Type = Counter32
_PortInputCACErrors_Object = MibTableColumn
portInputCACErrors = _PortInputCACErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 38),
    _PortInputCACErrors_Type()
)
portInputCACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInputCACErrors.setStatus("current")
_PortInputVPIErrors_Type = Counter32
_PortInputVPIErrors_Object = MibTableColumn
portInputVPIErrors = _PortInputVPIErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 39),
    _PortInputVPIErrors_Type()
)
portInputVPIErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInputVPIErrors.setStatus("current")
_PortInputVCIErrors_Type = Counter32
_PortInputVCIErrors_Object = MibTableColumn
portInputVCIErrors = _PortInputVCIErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 40),
    _PortInputVCIErrors_Type()
)
portInputVCIErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInputVCIErrors.setStatus("current")
_PortInputSetupErrors_Type = Counter32
_PortInputSetupErrors_Object = MibTableColumn
portInputSetupErrors = _PortInputSetupErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 41),
    _PortInputSetupErrors_Type()
)
portInputSetupErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInputSetupErrors.setStatus("current")
_PortOutputCACErrors_Type = Counter32
_PortOutputCACErrors_Object = MibTableColumn
portOutputCACErrors = _PortOutputCACErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 42),
    _PortOutputCACErrors_Type()
)
portOutputCACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOutputCACErrors.setStatus("current")
_PortOutputVPIErrors_Type = Counter32
_PortOutputVPIErrors_Object = MibTableColumn
portOutputVPIErrors = _PortOutputVPIErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 43),
    _PortOutputVPIErrors_Type()
)
portOutputVPIErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOutputVPIErrors.setStatus("current")
_PortOutputVCIErrors_Type = Counter32
_PortOutputVCIErrors_Object = MibTableColumn
portOutputVCIErrors = _PortOutputVCIErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 44),
    _PortOutputVCIErrors_Type()
)
portOutputVCIErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOutputVCIErrors.setStatus("current")
_PortOutputSetupErrors_Type = Counter32
_PortOutputSetupErrors_Object = MibTableColumn
portOutputSetupErrors = _PortOutputSetupErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 45),
    _PortOutputSetupErrors_Type()
)
portOutputSetupErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOutputSetupErrors.setStatus("current")


class _PortPPPolicingCBR_Type(Integer32):
    """Custom type portPPPolicingCBR based on Integer32"""
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
        *(("allOff", 2),
          ("allOn", 1),
          ("svcOff", 4),
          ("svcOn", 3))
    )


_PortPPPolicingCBR_Type.__name__ = "Integer32"
_PortPPPolicingCBR_Object = MibTableColumn
portPPPolicingCBR = _PortPPPolicingCBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 46),
    _PortPPPolicingCBR_Type()
)
portPPPolicingCBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPPPolicingCBR.setStatus("current")


class _PortPPPolicingVBR_Type(Integer32):
    """Custom type portPPPolicingVBR based on Integer32"""
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
        *(("allOff", 2),
          ("allOn", 1),
          ("svcOff", 4),
          ("svcOn", 3))
    )


_PortPPPolicingVBR_Type.__name__ = "Integer32"
_PortPPPolicingVBR_Object = MibTableColumn
portPPPolicingVBR = _PortPPPolicingVBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 47),
    _PortPPPolicingVBR_Type()
)
portPPPolicingVBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPPPolicingVBR.setStatus("deprecated")


class _PortUBRTagging_Type(Integer32):
    """Custom type portUBRTagging based on Integer32"""
    defaultValue = 4

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
        *(("allOff", 2),
          ("allOn", 1),
          ("svcOff", 4),
          ("svcOn", 3))
    )


_PortUBRTagging_Type.__name__ = "Integer32"
_PortUBRTagging_Object = MibTableColumn
portUBRTagging = _PortUBRTagging_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 48),
    _PortUBRTagging_Type()
)
portUBRTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portUBRTagging.setStatus("current")
_PortInputCdv_Type = Integer32
_PortInputCdv_Object = MibTableColumn
portInputCdv = _PortInputCdv_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 49),
    _PortInputCdv_Type()
)
portInputCdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portInputCdv.setStatus("current")
_PortInputMaxctd_Type = Integer32
_PortInputMaxctd_Object = MibTableColumn
portInputMaxctd = _PortInputMaxctd_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 50),
    _PortInputMaxctd_Type()
)
portInputMaxctd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portInputMaxctd.setStatus("current")


class _PortInputDelayMode_Type(Integer32):
    """Custom type portInputDelayMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("systemDefault", 1),
          ("userSpecified", 2))
    )


_PortInputDelayMode_Type.__name__ = "Integer32"
_PortInputDelayMode_Object = MibTableColumn
portInputDelayMode = _PortInputDelayMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 51),
    _PortInputDelayMode_Type()
)
portInputDelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portInputDelayMode.setStatus("current")
_PortOutputCdv_Type = Integer32
_PortOutputCdv_Object = MibTableColumn
portOutputCdv = _PortOutputCdv_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 52),
    _PortOutputCdv_Type()
)
portOutputCdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOutputCdv.setStatus("current")
_PortOutputMaxctd_Type = Integer32
_PortOutputMaxctd_Object = MibTableColumn
portOutputMaxctd = _PortOutputMaxctd_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 53),
    _PortOutputMaxctd_Type()
)
portOutputMaxctd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOutputMaxctd.setStatus("current")


class _PortOutputDelayMode_Type(Integer32):
    """Custom type portOutputDelayMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("systemDefault", 1),
          ("userSpecified", 2))
    )


_PortOutputDelayMode_Type.__name__ = "Integer32"
_PortOutputDelayMode_Object = MibTableColumn
portOutputDelayMode = _PortOutputDelayMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 54),
    _PortOutputDelayMode_Type()
)
portOutputDelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOutputDelayMode.setStatus("current")


class _PortCACStatus_Type(Integer32):
    """Custom type portCACStatus based on Integer32"""
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


_PortCACStatus_Type.__name__ = "Integer32"
_PortCACStatus_Object = MibTableColumn
portCACStatus = _PortCACStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 59),
    _PortCACStatus_Type()
)
portCACStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCACStatus.setStatus("current")
_PortCounterResetTime_Type = TimeStamp
_PortCounterResetTime_Object = MibTableColumn
portCounterResetTime = _PortCounterResetTime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 60),
    _PortCounterResetTime_Type()
)
portCounterResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCounterResetTime.setStatus("deprecated")


class _PortCounterReset_Type(Integer32):
    """Custom type portCounterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("resetFalse", 4),
          ("resetRequest", 1),
          ("resetTrue", 3))
    )


_PortCounterReset_Type.__name__ = "Integer32"
_PortCounterReset_Object = MibTableColumn
portCounterReset = _PortCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 61),
    _PortCounterReset_Type()
)
portCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCounterReset.setStatus("deprecated")
_PortName_Type = DisplayString
_PortName_Object = MibTableColumn
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 62),
    _PortName_Type()
)
portName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portName.setStatus("current")


class _PortGCRAPolicingRTVBR_Type(Integer32):
    """Custom type portGCRAPolicingRTVBR based on Integer32"""
    defaultValue = 5

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
        *(("allOff", 2),
          ("allOn", 1),
          ("default", 5),
          ("svcOff", 4),
          ("svcOn", 3))
    )


_PortGCRAPolicingRTVBR_Type.__name__ = "Integer32"
_PortGCRAPolicingRTVBR_Object = MibTableColumn
portGCRAPolicingRTVBR = _PortGCRAPolicingRTVBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 64),
    _PortGCRAPolicingRTVBR_Type()
)
portGCRAPolicingRTVBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portGCRAPolicingRTVBR.setStatus("current")


class _PortGCRAPolicingNRTVBR_Type(Integer32):
    """Custom type portGCRAPolicingNRTVBR based on Integer32"""
    defaultValue = 5

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
        *(("allOff", 2),
          ("allOn", 1),
          ("default", 5),
          ("svcOff", 4),
          ("svcOn", 3))
    )


_PortGCRAPolicingNRTVBR_Type.__name__ = "Integer32"
_PortGCRAPolicingNRTVBR_Object = MibTableColumn
portGCRAPolicingNRTVBR = _PortGCRAPolicingNRTVBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 65),
    _PortGCRAPolicingNRTVBR_Type()
)
portGCRAPolicingNRTVBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portGCRAPolicingNRTVBR.setStatus("current")


class _PortAAL5PacketDiscardRTVBR_Type(Integer32):
    """Custom type portAAL5PacketDiscardRTVBR based on Integer32"""
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
        *(("allOff", 2),
          ("allOn", 1),
          ("svcOff", 4),
          ("svcOn", 3))
    )


_PortAAL5PacketDiscardRTVBR_Type.__name__ = "Integer32"
_PortAAL5PacketDiscardRTVBR_Object = MibTableColumn
portAAL5PacketDiscardRTVBR = _PortAAL5PacketDiscardRTVBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 66),
    _PortAAL5PacketDiscardRTVBR_Type()
)
portAAL5PacketDiscardRTVBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAAL5PacketDiscardRTVBR.setStatus("current")


class _PortAAL5PacketDiscardNRTVBR_Type(Integer32):
    """Custom type portAAL5PacketDiscardNRTVBR based on Integer32"""
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
        *(("allOff", 2),
          ("allOn", 1),
          ("svcOff", 4),
          ("svcOn", 3))
    )


_PortAAL5PacketDiscardNRTVBR_Type.__name__ = "Integer32"
_PortAAL5PacketDiscardNRTVBR_Object = MibTableColumn
portAAL5PacketDiscardNRTVBR = _PortAAL5PacketDiscardNRTVBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 67),
    _PortAAL5PacketDiscardNRTVBR_Type()
)
portAAL5PacketDiscardNRTVBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAAL5PacketDiscardNRTVBR.setStatus("current")


class _PortPPPolicingNRTVBR_Type(Integer32):
    """Custom type portPPPolicingNRTVBR based on Integer32"""
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
        *(("allOff", 2),
          ("allOn", 1),
          ("svcOff", 4),
          ("svcOn", 3))
    )


_PortPPPolicingNRTVBR_Type.__name__ = "Integer32"
_PortPPPolicingNRTVBR_Object = MibTableColumn
portPPPolicingNRTVBR = _PortPPPolicingNRTVBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 68),
    _PortPPPolicingNRTVBR_Type()
)
portPPPolicingNRTVBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPPPolicingNRTVBR.setStatus("current")


class _PortPPPolicingRTVBR_Type(Integer32):
    """Custom type portPPPolicingRTVBR based on Integer32"""
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
        *(("allOff", 2),
          ("allOn", 1),
          ("svcOff", 4),
          ("svcOn", 3))
    )


_PortPPPolicingRTVBR_Type.__name__ = "Integer32"
_PortPPPolicingRTVBR_Object = MibTableColumn
portPPPolicingRTVBR = _PortPPPolicingRTVBR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 69),
    _PortPPPolicingRTVBR_Type()
)
portPPPolicingRTVBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPPPolicingRTVBR.setStatus("current")


class _PortNrtVbrOverbooking_Type(Integer32):
    """Custom type portNrtVbrOverbooking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_PortNrtVbrOverbooking_Type.__name__ = "Integer32"
_PortNrtVbrOverbooking_Object = MibTableColumn
portNrtVbrOverbooking = _PortNrtVbrOverbooking_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 70),
    _PortNrtVbrOverbooking_Type()
)
portNrtVbrOverbooking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portNrtVbrOverbooking.setStatus("current")


class _PortNrtVbrBufferOverb_Type(Integer32):
    """Custom type portNrtVbrBufferOverb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_PortNrtVbrBufferOverb_Type.__name__ = "Integer32"
_PortNrtVbrBufferOverb_Object = MibTableColumn
portNrtVbrBufferOverb = _PortNrtVbrBufferOverb_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 71),
    _PortNrtVbrBufferOverb_Type()
)
portNrtVbrBufferOverb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portNrtVbrBufferOverb.setStatus("current")


class _PortRtVbrOverbooking_Type(Integer32):
    """Custom type portRtVbrOverbooking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_PortRtVbrOverbooking_Type.__name__ = "Integer32"
_PortRtVbrOverbooking_Object = MibTableColumn
portRtVbrOverbooking = _PortRtVbrOverbooking_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 72),
    _PortRtVbrOverbooking_Type()
)
portRtVbrOverbooking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portRtVbrOverbooking.setStatus("current")


class _PortRtVbrBufferOverb_Type(Integer32):
    """Custom type portRtVbrBufferOverb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_PortRtVbrBufferOverb_Type.__name__ = "Integer32"
_PortRtVbrBufferOverb_Object = MibTableColumn
portRtVbrBufferOverb = _PortRtVbrBufferOverb_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 73),
    _PortRtVbrBufferOverb_Type()
)
portRtVbrBufferOverb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portRtVbrBufferOverb.setStatus("current")


class _PortPathOverbooking_Type(Integer32):
    """Custom type portPathOverbooking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_PortPathOverbooking_Type.__name__ = "Integer32"
_PortPathOverbooking_Object = MibTableColumn
portPathOverbooking = _PortPathOverbooking_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 2, 1, 74),
    _PortPathOverbooking_Type()
)
portPathOverbooking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPathOverbooking.setStatus("current")
_AtmIfConnSchedTable_Object = MibTable
atmIfConnSchedTable = _AtmIfConnSchedTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    atmIfConnSchedTable.setStatus("current")
_AtmIfConnSchedEntry_Object = MibTableRow
atmIfConnSchedEntry = _AtmIfConnSchedEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 3, 1)
)
atmIfConnSchedEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "atmIfConnSchedLink"),
    (0, "Fore-Switch-MIB", "atmIfConnSchedServCat"),
)
if mibBuilder.loadTexts:
    atmIfConnSchedEntry.setStatus("current")
_AtmIfConnSchedLink_Type = Integer32
_AtmIfConnSchedLink_Object = MibTableColumn
atmIfConnSchedLink = _AtmIfConnSchedLink_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 3, 1, 1),
    _AtmIfConnSchedLink_Type()
)
atmIfConnSchedLink.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfConnSchedLink.setStatus("current")
_AtmIfConnSchedServCat_Type = Integer32
_AtmIfConnSchedServCat_Object = MibTableColumn
atmIfConnSchedServCat = _AtmIfConnSchedServCat_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 3, 1, 2),
    _AtmIfConnSchedServCat_Type()
)
atmIfConnSchedServCat.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfConnSchedServCat.setStatus("current")
_AtmIfConnSchedMode_Type = AtmConnSchedMode
_AtmIfConnSchedMode_Object = MibTableColumn
atmIfConnSchedMode = _AtmIfConnSchedMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 3, 1, 3),
    _AtmIfConnSchedMode_Type()
)
atmIfConnSchedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfConnSchedMode.setStatus("current")


class _AtmIfConnSchedOverride_Type(Integer32):
    """Custom type atmIfConnSchedOverride based on Integer32"""
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


_AtmIfConnSchedOverride_Type.__name__ = "Integer32"
_AtmIfConnSchedOverride_Object = MibTableColumn
atmIfConnSchedOverride = _AtmIfConnSchedOverride_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 2, 3, 1, 4),
    _AtmIfConnSchedOverride_Type()
)
atmIfConnSchedOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfConnSchedOverride.setStatus("current")
_PathGroup_ObjectIdentity = ObjectIdentity
pathGroup = _PathGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3)
)
_PathTable_Object = MibTable
pathTable = _PathTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    pathTable.setStatus("current")
_PathEntry_Object = MibTableRow
pathEntry = _PathEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 1, 1)
)
pathEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "pathPort"),
    (0, "Fore-Switch-MIB", "pathVPI"),
)
if mibBuilder.loadTexts:
    pathEntry.setStatus("current")
_PathPort_Type = Integer32
_PathPort_Object = MibTableColumn
pathPort = _PathPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 1, 1, 1),
    _PathPort_Type()
)
pathPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pathPort.setStatus("current")
_PathVPI_Type = Integer32
_PathVPI_Object = MibTableColumn
pathVPI = _PathVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 1, 1, 2),
    _PathVPI_Type()
)
pathVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pathVPI.setStatus("current")
_PathStatus_Type = EntryStatus
_PathStatus_Object = MibTableColumn
pathStatus = _PathStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 1, 1, 3),
    _PathStatus_Type()
)
pathStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pathStatus.setStatus("current")
_PathNumOutputs_Type = Gauge32
_PathNumOutputs_Object = MibTableColumn
pathNumOutputs = _PathNumOutputs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 1, 1, 4),
    _PathNumOutputs_Type()
)
pathNumOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pathNumOutputs.setStatus("current")
_PathMaxChannels_Type = Integer32
_PathMaxChannels_Object = MibTableColumn
pathMaxChannels = _PathMaxChannels_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 1, 1, 5),
    _PathMaxChannels_Type()
)
pathMaxChannels.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pathMaxChannels.setStatus("current")
_PathNumChannels_Type = Gauge32
_PathNumChannels_Object = MibTableColumn
pathNumChannels = _PathNumChannels_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 1, 1, 6),
    _PathNumChannels_Type()
)
pathNumChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pathNumChannels.setStatus("current")
_PathMaxBandwidth_Type = Integer32
_PathMaxBandwidth_Object = MibTableColumn
pathMaxBandwidth = _PathMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 1, 1, 7),
    _PathMaxBandwidth_Type()
)
pathMaxBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pathMaxBandwidth.setStatus("current")
_PathAllocBandwidth_Type = Gauge32
_PathAllocBandwidth_Object = MibTableColumn
pathAllocBandwidth = _PathAllocBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 1, 1, 8),
    _PathAllocBandwidth_Type()
)
pathAllocBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pathAllocBandwidth.setStatus("current")
_PathUsedBandwidth_Type = Gauge32
_PathUsedBandwidth_Object = MibTableColumn
pathUsedBandwidth = _PathUsedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 1, 1, 9),
    _PathUsedBandwidth_Type()
)
pathUsedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pathUsedBandwidth.setStatus("deprecated")
_PathCells_Type = Counter32
_PathCells_Object = MibTableColumn
pathCells = _PathCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 1, 1, 10),
    _PathCells_Type()
)
pathCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pathCells.setStatus("current")
_PathUptime_Type = TimeTicks
_PathUptime_Object = MibTableColumn
pathUptime = _PathUptime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 1, 1, 11),
    _PathUptime_Type()
)
pathUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pathUptime.setStatus("current")
_PathSigProtocol_Type = AtmSigProtocol
_PathSigProtocol_Object = MibTableColumn
pathSigProtocol = _PathSigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 1, 1, 12),
    _PathSigProtocol_Type()
)
pathSigProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pathSigProtocol.setStatus("current")
_PathRejectedCells_Type = Counter32
_PathRejectedCells_Object = MibTableColumn
pathRejectedCells = _PathRejectedCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 1, 1, 13),
    _PathRejectedCells_Type()
)
pathRejectedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pathRejectedCells.setStatus("current")
_PathMinVCI_Type = Integer32
_PathMinVCI_Object = MibTableColumn
pathMinVCI = _PathMinVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 1, 1, 14),
    _PathMinVCI_Type()
)
pathMinVCI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pathMinVCI.setStatus("current")
_PathMaxVCI_Type = Integer32
_PathMaxVCI_Object = MibTableColumn
pathMaxVCI = _PathMaxVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 1, 1, 15),
    _PathMaxVCI_Type()
)
pathMaxVCI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pathMaxVCI.setStatus("current")
_PathCACErrors_Type = Counter32
_PathCACErrors_Object = MibTableColumn
pathCACErrors = _PathCACErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 1, 1, 16),
    _PathCACErrors_Type()
)
pathCACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pathCACErrors.setStatus("current")
_PathVCIErrors_Type = Counter32
_PathVCIErrors_Object = MibTableColumn
pathVCIErrors = _PathVCIErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 1, 1, 17),
    _PathVCIErrors_Type()
)
pathVCIErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pathVCIErrors.setStatus("current")
_PathSetupErrors_Type = Counter32
_PathSetupErrors_Object = MibTableColumn
pathSetupErrors = _PathSetupErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 1, 1, 18),
    _PathSetupErrors_Type()
)
pathSetupErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pathSetupErrors.setStatus("current")
_PathRouteTable_Object = MibTable
pathRouteTable = _PathRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    pathRouteTable.setStatus("current")
_PathRouteEntry_Object = MibTableRow
pathRouteEntry = _PathRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 2, 1)
)
pathRouteEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "pathrInputPort"),
    (0, "Fore-Switch-MIB", "pathrInputVPI"),
    (0, "Fore-Switch-MIB", "pathrOutputPort"),
    (0, "Fore-Switch-MIB", "pathrOutputVPI"),
)
if mibBuilder.loadTexts:
    pathRouteEntry.setStatus("current")
_PathrInputPort_Type = Integer32
_PathrInputPort_Object = MibTableColumn
pathrInputPort = _PathrInputPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 2, 1, 1),
    _PathrInputPort_Type()
)
pathrInputPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pathrInputPort.setStatus("current")
_PathrInputVPI_Type = Integer32
_PathrInputVPI_Object = MibTableColumn
pathrInputVPI = _PathrInputVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 2, 1, 2),
    _PathrInputVPI_Type()
)
pathrInputVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pathrInputVPI.setStatus("current")
_PathrOutputPort_Type = Integer32
_PathrOutputPort_Object = MibTableColumn
pathrOutputPort = _PathrOutputPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 2, 1, 3),
    _PathrOutputPort_Type()
)
pathrOutputPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pathrOutputPort.setStatus("current")
_PathrOutputVPI_Type = Integer32
_PathrOutputVPI_Object = MibTableColumn
pathrOutputVPI = _PathrOutputVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 2, 1, 4),
    _PathrOutputVPI_Type()
)
pathrOutputVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pathrOutputVPI.setStatus("current")
_PathrStatus_Type = EntryStatus
_PathrStatus_Object = MibTableColumn
pathrStatus = _PathrStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 2, 1, 5),
    _PathrStatus_Type()
)
pathrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pathrStatus.setStatus("current")
_PathrMaxBandwidth_Type = Integer32
_PathrMaxBandwidth_Object = MibTableColumn
pathrMaxBandwidth = _PathrMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 2, 1, 6),
    _PathrMaxBandwidth_Type()
)
pathrMaxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pathrMaxBandwidth.setStatus("current")
_PathrAllocBandwidth_Type = Gauge32
_PathrAllocBandwidth_Object = MibTableColumn
pathrAllocBandwidth = _PathrAllocBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 2, 1, 7),
    _PathrAllocBandwidth_Type()
)
pathrAllocBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pathrAllocBandwidth.setStatus("current")
_PathrCells_Type = Counter32
_PathrCells_Object = MibTableColumn
pathrCells = _PathrCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 2, 1, 8),
    _PathrCells_Type()
)
pathrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pathrCells.setStatus("current")
_PathrUptime_Type = TimeTicks
_PathrUptime_Object = MibTableColumn
pathrUptime = _PathrUptime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 2, 1, 9),
    _PathrUptime_Type()
)
pathrUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pathrUptime.setStatus("current")
_PathrSigProtocol_Type = AtmSigProtocol
_PathrSigProtocol_Object = MibTableColumn
pathrSigProtocol = _PathrSigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 2, 1, 10),
    _PathrSigProtocol_Type()
)
pathrSigProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pathrSigProtocol.setStatus("current")
_PathrRejectedCells_Type = Counter32
_PathrRejectedCells_Object = MibTableColumn
pathrRejectedCells = _PathrRejectedCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 2, 1, 11),
    _PathrRejectedCells_Type()
)
pathrRejectedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pathrRejectedCells.setStatus("current")
_PathrLoopVPI_Type = Integer32
_PathrLoopVPI_Object = MibTableColumn
pathrLoopVPI = _PathrLoopVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 2, 1, 12),
    _PathrLoopVPI_Type()
)
pathrLoopVPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pathrLoopVPI.setStatus("current")
_PathrUpcContract_Type = Integer32
_PathrUpcContract_Object = MibTableColumn
pathrUpcContract = _PathrUpcContract_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 2, 1, 13),
    _PathrUpcContract_Type()
)
pathrUpcContract.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pathrUpcContract.setStatus("current")


class _PathrName_Type(OctetString):
    """Custom type pathrName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PathrName_Type.__name__ = "OctetString"
_PathrName_Object = MibTableColumn
pathrName = _PathrName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 2, 1, 14),
    _PathrName_Type()
)
pathrName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pathrName.setStatus("current")
_PathrConnectionType_Type = ConnectionType
_PathrConnectionType_Object = MibTableColumn
pathrConnectionType = _PathrConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 2, 1, 15),
    _PathrConnectionType_Type()
)
pathrConnectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pathrConnectionType.setStatus("current")
_PathrServCat_Type = Integer32
_PathrServCat_Object = MibTableColumn
pathrServCat = _PathrServCat_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 2, 1, 16),
    _PathrServCat_Type()
)
pathrServCat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pathrServCat.setStatus("current")
_OutputPathTable_Object = MibTable
outputPathTable = _OutputPathTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    outputPathTable.setStatus("current")
_OutputPathEntry_Object = MibTableRow
outputPathEntry = _OutputPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 3, 1)
)
outputPathEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "opathPort"),
    (0, "Fore-Switch-MIB", "opathVPI"),
)
if mibBuilder.loadTexts:
    outputPathEntry.setStatus("current")
_OpathPort_Type = Integer32
_OpathPort_Object = MibTableColumn
opathPort = _OpathPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 3, 1, 1),
    _OpathPort_Type()
)
opathPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opathPort.setStatus("current")
_OpathVPI_Type = Integer32
_OpathVPI_Object = MibTableColumn
opathVPI = _OpathVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 3, 1, 2),
    _OpathVPI_Type()
)
opathVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opathVPI.setStatus("current")
_OpathStatus_Type = EntryStatus
_OpathStatus_Object = MibTableColumn
opathStatus = _OpathStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 3, 1, 3),
    _OpathStatus_Type()
)
opathStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    opathStatus.setStatus("current")
_OpathMaxChannels_Type = Integer32
_OpathMaxChannels_Object = MibTableColumn
opathMaxChannels = _OpathMaxChannels_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 3, 1, 4),
    _OpathMaxChannels_Type()
)
opathMaxChannels.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    opathMaxChannels.setStatus("current")
_OpathNumChannels_Type = Gauge32
_OpathNumChannels_Object = MibTableColumn
opathNumChannels = _OpathNumChannels_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 3, 1, 5),
    _OpathNumChannels_Type()
)
opathNumChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opathNumChannels.setStatus("current")
_OpathMaxBandwidth_Type = Integer32
_OpathMaxBandwidth_Object = MibTableColumn
opathMaxBandwidth = _OpathMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 3, 1, 6),
    _OpathMaxBandwidth_Type()
)
opathMaxBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    opathMaxBandwidth.setStatus("current")
_OpathAllocBandwidth_Type = Gauge32
_OpathAllocBandwidth_Object = MibTableColumn
opathAllocBandwidth = _OpathAllocBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 3, 1, 7),
    _OpathAllocBandwidth_Type()
)
opathAllocBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    opathAllocBandwidth.setStatus("current")
_OpathUsedBandwidth_Type = Gauge32
_OpathUsedBandwidth_Object = MibTableColumn
opathUsedBandwidth = _OpathUsedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 3, 1, 8),
    _OpathUsedBandwidth_Type()
)
opathUsedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opathUsedBandwidth.setStatus("deprecated")
_OpathCells_Type = Counter32
_OpathCells_Object = MibTableColumn
opathCells = _OpathCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 3, 1, 9),
    _OpathCells_Type()
)
opathCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opathCells.setStatus("current")
_OpathUptime_Type = TimeTicks
_OpathUptime_Object = MibTableColumn
opathUptime = _OpathUptime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 3, 1, 10),
    _OpathUptime_Type()
)
opathUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opathUptime.setStatus("current")
_OpathSigProtocol_Type = AtmSigProtocol
_OpathSigProtocol_Object = MibTableColumn
opathSigProtocol = _OpathSigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 3, 1, 11),
    _OpathSigProtocol_Type()
)
opathSigProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opathSigProtocol.setStatus("current")
_OpathRejectedCells_Type = Counter32
_OpathRejectedCells_Object = MibTableColumn
opathRejectedCells = _OpathRejectedCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 3, 1, 12),
    _OpathRejectedCells_Type()
)
opathRejectedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opathRejectedCells.setStatus("current")
_OpathTrafficShapeVPI_Type = Integer32
_OpathTrafficShapeVPI_Object = MibTableColumn
opathTrafficShapeVPI = _OpathTrafficShapeVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 3, 1, 13),
    _OpathTrafficShapeVPI_Type()
)
opathTrafficShapeVPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    opathTrafficShapeVPI.setStatus("current")


class _OpathVbrOverbooking_Type(Integer32):
    """Custom type opathVbrOverbooking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_OpathVbrOverbooking_Type.__name__ = "Integer32"
_OpathVbrOverbooking_Object = MibTableColumn
opathVbrOverbooking = _OpathVbrOverbooking_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 3, 1, 14),
    _OpathVbrOverbooking_Type()
)
opathVbrOverbooking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    opathVbrOverbooking.setStatus("deprecated")


class _OpathVbrBufferOverb_Type(Integer32):
    """Custom type opathVbrBufferOverb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_OpathVbrBufferOverb_Type.__name__ = "Integer32"
_OpathVbrBufferOverb_Object = MibTableColumn
opathVbrBufferOverb = _OpathVbrBufferOverb_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 3, 1, 15),
    _OpathVbrBufferOverb_Type()
)
opathVbrBufferOverb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    opathVbrBufferOverb.setStatus("deprecated")
_OpathMinVCI_Type = Integer32
_OpathMinVCI_Object = MibTableColumn
opathMinVCI = _OpathMinVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 3, 1, 16),
    _OpathMinVCI_Type()
)
opathMinVCI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    opathMinVCI.setStatus("current")
_OpathMaxVCI_Type = Integer32
_OpathMaxVCI_Object = MibTableColumn
opathMaxVCI = _OpathMaxVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 3, 1, 17),
    _OpathMaxVCI_Type()
)
opathMaxVCI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    opathMaxVCI.setStatus("current")
_OpathCACErrors_Type = Counter32
_OpathCACErrors_Object = MibTableColumn
opathCACErrors = _OpathCACErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 3, 1, 18),
    _OpathCACErrors_Type()
)
opathCACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opathCACErrors.setStatus("current")
_OpathVCIErrors_Type = Counter32
_OpathVCIErrors_Object = MibTableColumn
opathVCIErrors = _OpathVCIErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 3, 1, 19),
    _OpathVCIErrors_Type()
)
opathVCIErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opathVCIErrors.setStatus("current")
_OpathSetupErrors_Type = Counter32
_OpathSetupErrors_Object = MibTableColumn
opathSetupErrors = _OpathSetupErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 3, 1, 20),
    _OpathSetupErrors_Type()
)
opathSetupErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opathSetupErrors.setStatus("current")
_OpathLoopVPI_Type = Integer32
_OpathLoopVPI_Object = MibTableColumn
opathLoopVPI = _OpathLoopVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 3, 1, 21),
    _OpathLoopVPI_Type()
)
opathLoopVPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    opathLoopVPI.setStatus("current")


class _OpathSchedMode_Type(AtmOrigPathSchedMode):
    """Custom type opathSchedMode based on AtmOrigPathSchedMode"""


_OpathSchedMode_Object = MibTableColumn
opathSchedMode = _OpathSchedMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 3, 1, 22),
    _OpathSchedMode_Type()
)
opathSchedMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    opathSchedMode.setStatus("current")


class _OpathNrtVbrOverbooking_Type(Integer32):
    """Custom type opathNrtVbrOverbooking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_OpathNrtVbrOverbooking_Type.__name__ = "Integer32"
_OpathNrtVbrOverbooking_Object = MibTableColumn
opathNrtVbrOverbooking = _OpathNrtVbrOverbooking_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 3, 1, 23),
    _OpathNrtVbrOverbooking_Type()
)
opathNrtVbrOverbooking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    opathNrtVbrOverbooking.setStatus("current")


class _OpathNrtVbrBufferOverb_Type(Integer32):
    """Custom type opathNrtVbrBufferOverb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_OpathNrtVbrBufferOverb_Type.__name__ = "Integer32"
_OpathNrtVbrBufferOverb_Object = MibTableColumn
opathNrtVbrBufferOverb = _OpathNrtVbrBufferOverb_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 3, 1, 24),
    _OpathNrtVbrBufferOverb_Type()
)
opathNrtVbrBufferOverb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    opathNrtVbrBufferOverb.setStatus("current")


class _OpathRtVbrOverbooking_Type(Integer32):
    """Custom type opathRtVbrOverbooking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_OpathRtVbrOverbooking_Type.__name__ = "Integer32"
_OpathRtVbrOverbooking_Object = MibTableColumn
opathRtVbrOverbooking = _OpathRtVbrOverbooking_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 3, 1, 25),
    _OpathRtVbrOverbooking_Type()
)
opathRtVbrOverbooking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    opathRtVbrOverbooking.setStatus("current")


class _OpathRtVbrBufferOverb_Type(Integer32):
    """Custom type opathRtVbrBufferOverb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_OpathRtVbrBufferOverb_Type.__name__ = "Integer32"
_OpathRtVbrBufferOverb_Object = MibTableColumn
opathRtVbrBufferOverb = _OpathRtVbrBufferOverb_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 3, 1, 26),
    _OpathRtVbrBufferOverb_Type()
)
opathRtVbrBufferOverb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    opathRtVbrBufferOverb.setStatus("current")
_OutputPathStatsTable_Object = MibTable
outputPathStatsTable = _OutputPathStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 4)
)
if mibBuilder.loadTexts:
    outputPathStatsTable.setStatus("current")
_OutputPathStatsEntry_Object = MibTableRow
outputPathStatsEntry = _OutputPathStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 4, 1)
)
outputPathStatsEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "opathStatsPort"),
    (0, "Fore-Switch-MIB", "opathStatsVPI"),
)
if mibBuilder.loadTexts:
    outputPathStatsEntry.setStatus("current")
_OpathStatsPort_Type = Integer32
_OpathStatsPort_Object = MibTableColumn
opathStatsPort = _OpathStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 4, 1, 1),
    _OpathStatsPort_Type()
)
opathStatsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opathStatsPort.setStatus("current")
_OpathStatsVPI_Type = Integer32
_OpathStatsVPI_Object = MibTableColumn
opathStatsVPI = _OpathStatsVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 4, 1, 2),
    _OpathStatsVPI_Type()
)
opathStatsVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opathStatsVPI.setStatus("current")
_OpathStatsLostCells_Type = Counter32
_OpathStatsLostCells_Object = MibTableColumn
opathStatsLostCells = _OpathStatsLostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 4, 1, 3),
    _OpathStatsLostCells_Type()
)
opathStatsLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opathStatsLostCells.setStatus("current")
_OpathStatsTransmittedCells_Type = Counter32
_OpathStatsTransmittedCells_Object = MibTableColumn
opathStatsTransmittedCells = _OpathStatsTransmittedCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 4, 1, 4),
    _OpathStatsTransmittedCells_Type()
)
opathStatsTransmittedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opathStatsTransmittedCells.setStatus("current")
_OpathStatsIntentionalLostCells_Type = Counter32
_OpathStatsIntentionalLostCells_Object = MibTableColumn
opathStatsIntentionalLostCells = _OpathStatsIntentionalLostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 4, 1, 5),
    _OpathStatsIntentionalLostCells_Type()
)
opathStatsIntentionalLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opathStatsIntentionalLostCells.setStatus("current")
_OpathStatsCLP0Cells_Type = Counter32
_OpathStatsCLP0Cells_Object = MibTableColumn
opathStatsCLP0Cells = _OpathStatsCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 4, 1, 6),
    _OpathStatsCLP0Cells_Type()
)
opathStatsCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opathStatsCLP0Cells.setStatus("current")
_OpathStatsLostPackets_Type = Counter32
_OpathStatsLostPackets_Object = MibTableColumn
opathStatsLostPackets = _OpathStatsLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 4, 1, 7),
    _OpathStatsLostPackets_Type()
)
opathStatsLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opathStatsLostPackets.setStatus("current")
_OpathStatsTransmittedPackets_Type = Counter32
_OpathStatsTransmittedPackets_Object = MibTableColumn
opathStatsTransmittedPackets = _OpathStatsTransmittedPackets_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 4, 1, 8),
    _OpathStatsTransmittedPackets_Type()
)
opathStatsTransmittedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opathStatsTransmittedPackets.setStatus("current")
_OutputPathChannelSchedTable_Object = MibTable
outputPathChannelSchedTable = _OutputPathChannelSchedTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 5)
)
if mibBuilder.loadTexts:
    outputPathChannelSchedTable.setStatus("current")
_OutputPathChannelSchedEntry_Object = MibTableRow
outputPathChannelSchedEntry = _OutputPathChannelSchedEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 5, 1)
)
outputPathChannelSchedEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "opathChannelSchedPort"),
    (0, "Fore-Switch-MIB", "opathChannelSchedVPI"),
    (0, "Fore-Switch-MIB", "opathChannelSchedServCat"),
)
if mibBuilder.loadTexts:
    outputPathChannelSchedEntry.setStatus("current")
_OpathChannelSchedPort_Type = Integer32
_OpathChannelSchedPort_Object = MibTableColumn
opathChannelSchedPort = _OpathChannelSchedPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 5, 1, 1),
    _OpathChannelSchedPort_Type()
)
opathChannelSchedPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    opathChannelSchedPort.setStatus("current")
_OpathChannelSchedVPI_Type = Integer32
_OpathChannelSchedVPI_Object = MibTableColumn
opathChannelSchedVPI = _OpathChannelSchedVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 5, 1, 2),
    _OpathChannelSchedVPI_Type()
)
opathChannelSchedVPI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    opathChannelSchedVPI.setStatus("current")
_OpathChannelSchedServCat_Type = Integer32
_OpathChannelSchedServCat_Object = MibTableColumn
opathChannelSchedServCat = _OpathChannelSchedServCat_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 5, 1, 3),
    _OpathChannelSchedServCat_Type()
)
opathChannelSchedServCat.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    opathChannelSchedServCat.setStatus("current")
_OpathChannelSchedSchedMode_Type = AtmConnSchedMode
_OpathChannelSchedSchedMode_Object = MibTableColumn
opathChannelSchedSchedMode = _OpathChannelSchedSchedMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 5, 1, 4),
    _OpathChannelSchedSchedMode_Type()
)
opathChannelSchedSchedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opathChannelSchedSchedMode.setStatus("current")


class _OpathChannelSchedSchedOverride_Type(Integer32):
    """Custom type opathChannelSchedSchedOverride based on Integer32"""
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


_OpathChannelSchedSchedOverride_Type.__name__ = "Integer32"
_OpathChannelSchedSchedOverride_Object = MibTableColumn
opathChannelSchedSchedOverride = _OpathChannelSchedSchedOverride_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 3, 5, 1, 5),
    _OpathChannelSchedSchedOverride_Type()
)
opathChannelSchedSchedOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opathChannelSchedSchedOverride.setStatus("current")
_ChannelGroup_ObjectIdentity = ObjectIdentity
channelGroup = _ChannelGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4)
)
_ChannelTable_Object = MibTable
channelTable = _ChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    channelTable.setStatus("current")
_ChannelEntry_Object = MibTableRow
channelEntry = _ChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 1, 1)
)
channelEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "chanPort"),
    (0, "Fore-Switch-MIB", "chanVPI"),
    (0, "Fore-Switch-MIB", "chanVCI"),
)
if mibBuilder.loadTexts:
    channelEntry.setStatus("current")
_ChanPort_Type = Integer32
_ChanPort_Object = MibTableColumn
chanPort = _ChanPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 1, 1, 1),
    _ChanPort_Type()
)
chanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanPort.setStatus("current")
_ChanVPI_Type = Integer32
_ChanVPI_Object = MibTableColumn
chanVPI = _ChanVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 1, 1, 2),
    _ChanVPI_Type()
)
chanVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanVPI.setStatus("current")
_ChanVCI_Type = Integer32
_ChanVCI_Object = MibTableColumn
chanVCI = _ChanVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 1, 1, 3),
    _ChanVCI_Type()
)
chanVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanVCI.setStatus("current")
_ChanStatus_Type = EntryStatus
_ChanStatus_Object = MibTableColumn
chanStatus = _ChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 1, 1, 4),
    _ChanStatus_Type()
)
chanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chanStatus.setStatus("current")
_ChanNumOutputs_Type = Gauge32
_ChanNumOutputs_Object = MibTableColumn
chanNumOutputs = _ChanNumOutputs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 1, 1, 5),
    _ChanNumOutputs_Type()
)
chanNumOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanNumOutputs.setStatus("current")
_ChanAllocBandwidth_Type = Gauge32
_ChanAllocBandwidth_Object = MibTableColumn
chanAllocBandwidth = _ChanAllocBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 1, 1, 6),
    _ChanAllocBandwidth_Type()
)
chanAllocBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chanAllocBandwidth.setStatus("current")
_ChanUsedBandwidth_Type = Gauge32
_ChanUsedBandwidth_Object = MibTableColumn
chanUsedBandwidth = _ChanUsedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 1, 1, 7),
    _ChanUsedBandwidth_Type()
)
chanUsedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanUsedBandwidth.setStatus("deprecated")
_ChanCells_Type = Counter32
_ChanCells_Object = MibTableColumn
chanCells = _ChanCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 1, 1, 8),
    _ChanCells_Type()
)
chanCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanCells.setStatus("current")
_ChanUptime_Type = TimeTicks
_ChanUptime_Object = MibTableColumn
chanUptime = _ChanUptime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 1, 1, 9),
    _ChanUptime_Type()
)
chanUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanUptime.setStatus("current")
_ChanSigProtocol_Type = AtmSigProtocol
_ChanSigProtocol_Object = MibTableColumn
chanSigProtocol = _ChanSigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 1, 1, 10),
    _ChanSigProtocol_Type()
)
chanSigProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanSigProtocol.setStatus("current")
_ChanRejectedCells_Type = Counter32
_ChanRejectedCells_Object = MibTableColumn
chanRejectedCells = _ChanRejectedCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 1, 1, 11),
    _ChanRejectedCells_Type()
)
chanRejectedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanRejectedCells.setStatus("current")
_ChanCDV_Type = Integer32
_ChanCDV_Object = MibTableColumn
chanCDV = _ChanCDV_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 1, 1, 12),
    _ChanCDV_Type()
)
chanCDV.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chanCDV.setStatus("current")


class _ChanPolicingAction_Type(Integer32):
    """Custom type chanPolicingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("tag", 1))
    )


_ChanPolicingAction_Type.__name__ = "Integer32"
_ChanPolicingAction_Object = MibTableColumn
chanPolicingAction = _ChanPolicingAction_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 1, 1, 13),
    _ChanPolicingAction_Type()
)
chanPolicingAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chanPolicingAction.setStatus("current")
_ChanUpcContract_Type = Integer32
_ChanUpcContract_Object = MibTableColumn
chanUpcContract = _ChanUpcContract_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 1, 1, 14),
    _ChanUpcContract_Type()
)
chanUpcContract.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chanUpcContract.setStatus("current")
_ChanServCat_Type = Integer32
_ChanServCat_Object = MibTableColumn
chanServCat = _ChanServCat_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 1, 1, 15),
    _ChanServCat_Type()
)
chanServCat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanServCat.setStatus("current")


class _ChanQosPoliceScheme_Type(Integer32):
    """Custom type chanQosPoliceScheme based on Integer32"""
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
        *(("abr1", 7),
          ("cbr0", 2),
          ("cbr0tag", 3),
          ("cbr1", 1),
          ("ubr1", 8),
          ("ubr2", 9),
          ("vbr1", 4),
          ("vbr2", 5),
          ("vbr3", 6))
    )


_ChanQosPoliceScheme_Type.__name__ = "Integer32"
_ChanQosPoliceScheme_Object = MibTableColumn
chanQosPoliceScheme = _ChanQosPoliceScheme_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 1, 1, 16),
    _ChanQosPoliceScheme_Type()
)
chanQosPoliceScheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanQosPoliceScheme.setStatus("current")
_ChanQosPCR_Type = Integer32
_ChanQosPCR_Object = MibTableColumn
chanQosPCR = _ChanQosPCR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 1, 1, 17),
    _ChanQosPCR_Type()
)
chanQosPCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanQosPCR.setStatus("current")
_ChanQosSCR_Type = Integer32
_ChanQosSCR_Object = MibTableColumn
chanQosSCR = _ChanQosSCR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 1, 1, 18),
    _ChanQosSCR_Type()
)
chanQosSCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanQosSCR.setStatus("current")
_ChanQosMBS_Type = Integer32
_ChanQosMBS_Object = MibTableColumn
chanQosMBS = _ChanQosMBS_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 1, 1, 19),
    _ChanQosMBS_Type()
)
chanQosMBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanQosMBS.setStatus("current")
_ChanQosCDVT_Type = Integer32
_ChanQosCDVT_Object = MibTableColumn
chanQosCDVT = _ChanQosCDVT_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 1, 1, 20),
    _ChanQosCDVT_Type()
)
chanQosCDVT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanQosCDVT.setStatus("current")


class _ChanQosPoliceState_Type(Integer32):
    """Custom type chanQosPoliceState based on Integer32"""
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


_ChanQosPoliceState_Type.__name__ = "Integer32"
_ChanQosPoliceState_Object = MibTableColumn
chanQosPoliceState = _ChanQosPoliceState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 1, 1, 21),
    _ChanQosPoliceState_Type()
)
chanQosPoliceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanQosPoliceState.setStatus("current")


class _ChanQosIsAAL5_Type(Integer32):
    """Custom type chanQosIsAAL5 based on Integer32"""
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


_ChanQosIsAAL5_Type.__name__ = "Integer32"
_ChanQosIsAAL5_Object = MibTableColumn
chanQosIsAAL5 = _ChanQosIsAAL5_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 1, 1, 22),
    _ChanQosIsAAL5_Type()
)
chanQosIsAAL5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanQosIsAAL5.setStatus("current")


class _ChanQosPerPacketPolicing_Type(Integer32):
    """Custom type chanQosPerPacketPolicing based on Integer32"""
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


_ChanQosPerPacketPolicing_Type.__name__ = "Integer32"
_ChanQosPerPacketPolicing_Object = MibTableColumn
chanQosPerPacketPolicing = _ChanQosPerPacketPolicing_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 1, 1, 23),
    _ChanQosPerPacketPolicing_Type()
)
chanQosPerPacketPolicing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanQosPerPacketPolicing.setStatus("current")
_ChannelRouteTable_Object = MibTable
channelRouteTable = _ChannelRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    channelRouteTable.setStatus("current")
_ChannelRouteEntry_Object = MibTableRow
channelRouteEntry = _ChannelRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 2, 1)
)
channelRouteEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "chanrInputPort"),
    (0, "Fore-Switch-MIB", "chanrInputVPI"),
    (0, "Fore-Switch-MIB", "chanrInputVCI"),
    (0, "Fore-Switch-MIB", "chanrOutputPort"),
    (0, "Fore-Switch-MIB", "chanrOutputVPI"),
    (0, "Fore-Switch-MIB", "chanrOutputVCI"),
)
if mibBuilder.loadTexts:
    channelRouteEntry.setStatus("current")
_ChanrInputPort_Type = Integer32
_ChanrInputPort_Object = MibTableColumn
chanrInputPort = _ChanrInputPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 2, 1, 1),
    _ChanrInputPort_Type()
)
chanrInputPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanrInputPort.setStatus("current")
_ChanrInputVPI_Type = Integer32
_ChanrInputVPI_Object = MibTableColumn
chanrInputVPI = _ChanrInputVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 2, 1, 2),
    _ChanrInputVPI_Type()
)
chanrInputVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanrInputVPI.setStatus("current")
_ChanrInputVCI_Type = Integer32
_ChanrInputVCI_Object = MibTableColumn
chanrInputVCI = _ChanrInputVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 2, 1, 3),
    _ChanrInputVCI_Type()
)
chanrInputVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanrInputVCI.setStatus("current")
_ChanrOutputPort_Type = Integer32
_ChanrOutputPort_Object = MibTableColumn
chanrOutputPort = _ChanrOutputPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 2, 1, 4),
    _ChanrOutputPort_Type()
)
chanrOutputPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanrOutputPort.setStatus("current")
_ChanrOutputVPI_Type = Integer32
_ChanrOutputVPI_Object = MibTableColumn
chanrOutputVPI = _ChanrOutputVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 2, 1, 5),
    _ChanrOutputVPI_Type()
)
chanrOutputVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanrOutputVPI.setStatus("current")
_ChanrOutputVCI_Type = Integer32
_ChanrOutputVCI_Object = MibTableColumn
chanrOutputVCI = _ChanrOutputVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 2, 1, 6),
    _ChanrOutputVCI_Type()
)
chanrOutputVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanrOutputVCI.setStatus("current")
_ChanrStatus_Type = EntryStatus
_ChanrStatus_Object = MibTableColumn
chanrStatus = _ChanrStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 2, 1, 7),
    _ChanrStatus_Type()
)
chanrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chanrStatus.setStatus("current")
_ChanrSigProtocol_Type = AtmSigProtocol
_ChanrSigProtocol_Object = MibTableColumn
chanrSigProtocol = _ChanrSigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 2, 1, 8),
    _ChanrSigProtocol_Type()
)
chanrSigProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanrSigProtocol.setStatus("current")


class _ChanrName_Type(OctetString):
    """Custom type chanrName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ChanrName_Type.__name__ = "OctetString"
_ChanrName_Object = MibTableColumn
chanrName = _ChanrName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 2, 1, 9),
    _ChanrName_Type()
)
chanrName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chanrName.setStatus("current")
_ChanrConnectionType_Type = ConnectionType
_ChanrConnectionType_Object = MibTableColumn
chanrConnectionType = _ChanrConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 2, 1, 10),
    _ChanrConnectionType_Type()
)
chanrConnectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chanrConnectionType.setStatus("current")
_ReverseChannelRouteTable_Object = MibTable
reverseChannelRouteTable = _ReverseChannelRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 3)
)
if mibBuilder.loadTexts:
    reverseChannelRouteTable.setStatus("current")
_ReverseChannelRouteEntry_Object = MibTableRow
reverseChannelRouteEntry = _ReverseChannelRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 3, 1)
)
reverseChannelRouteEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "revChanrOutputPort"),
    (0, "Fore-Switch-MIB", "revChanrOutputVPI"),
    (0, "Fore-Switch-MIB", "revChanrOutputVCI"),
    (0, "Fore-Switch-MIB", "revChanrInputPort"),
    (0, "Fore-Switch-MIB", "revChanrInputVPI"),
    (0, "Fore-Switch-MIB", "revChanrInputVCI"),
)
if mibBuilder.loadTexts:
    reverseChannelRouteEntry.setStatus("current")
_RevChanrOutputPort_Type = Integer32
_RevChanrOutputPort_Object = MibTableColumn
revChanrOutputPort = _RevChanrOutputPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 3, 1, 1),
    _RevChanrOutputPort_Type()
)
revChanrOutputPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    revChanrOutputPort.setStatus("current")
_RevChanrOutputVPI_Type = Integer32
_RevChanrOutputVPI_Object = MibTableColumn
revChanrOutputVPI = _RevChanrOutputVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 3, 1, 2),
    _RevChanrOutputVPI_Type()
)
revChanrOutputVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    revChanrOutputVPI.setStatus("current")
_RevChanrOutputVCI_Type = Integer32
_RevChanrOutputVCI_Object = MibTableColumn
revChanrOutputVCI = _RevChanrOutputVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 3, 1, 3),
    _RevChanrOutputVCI_Type()
)
revChanrOutputVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    revChanrOutputVCI.setStatus("current")
_RevChanrInputPort_Type = Integer32
_RevChanrInputPort_Object = MibTableColumn
revChanrInputPort = _RevChanrInputPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 3, 1, 4),
    _RevChanrInputPort_Type()
)
revChanrInputPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    revChanrInputPort.setStatus("current")
_RevChanrInputVPI_Type = Integer32
_RevChanrInputVPI_Object = MibTableColumn
revChanrInputVPI = _RevChanrInputVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 3, 1, 5),
    _RevChanrInputVPI_Type()
)
revChanrInputVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    revChanrInputVPI.setStatus("current")
_RevChanrInputVCI_Type = Integer32
_RevChanrInputVCI_Object = MibTableColumn
revChanrInputVCI = _RevChanrInputVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 3, 1, 6),
    _RevChanrInputVCI_Type()
)
revChanrInputVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    revChanrInputVCI.setStatus("current")
_RevChanrSigProtocol_Type = AtmSigProtocol
_RevChanrSigProtocol_Object = MibTableColumn
revChanrSigProtocol = _RevChanrSigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 3, 1, 7),
    _RevChanrSigProtocol_Type()
)
revChanrSigProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    revChanrSigProtocol.setStatus("current")
_OutputChannelStatsTable_Object = MibTable
outputChannelStatsTable = _OutputChannelStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 4)
)
if mibBuilder.loadTexts:
    outputChannelStatsTable.setStatus("current")
_OutputChannelStatsEntry_Object = MibTableRow
outputChannelStatsEntry = _OutputChannelStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 4, 1)
)
outputChannelStatsEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "ochanStatsPort"),
    (0, "Fore-Switch-MIB", "ochanStatsVPI"),
    (0, "Fore-Switch-MIB", "ochanStatsVCI"),
)
if mibBuilder.loadTexts:
    outputChannelStatsEntry.setStatus("current")
_OchanStatsPort_Type = Integer32
_OchanStatsPort_Object = MibTableColumn
ochanStatsPort = _OchanStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 4, 1, 1),
    _OchanStatsPort_Type()
)
ochanStatsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochanStatsPort.setStatus("current")
_OchanStatsVPI_Type = Integer32
_OchanStatsVPI_Object = MibTableColumn
ochanStatsVPI = _OchanStatsVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 4, 1, 2),
    _OchanStatsVPI_Type()
)
ochanStatsVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochanStatsVPI.setStatus("current")
_OchanStatsVCI_Type = Integer32
_OchanStatsVCI_Object = MibTableColumn
ochanStatsVCI = _OchanStatsVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 4, 1, 3),
    _OchanStatsVCI_Type()
)
ochanStatsVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochanStatsVCI.setStatus("current")
_OchanStatsLostCells_Type = Counter32
_OchanStatsLostCells_Object = MibTableColumn
ochanStatsLostCells = _OchanStatsLostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 4, 1, 4),
    _OchanStatsLostCells_Type()
)
ochanStatsLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochanStatsLostCells.setStatus("current")
_OchanStatsTransmittedCells_Type = Counter32
_OchanStatsTransmittedCells_Object = MibTableColumn
ochanStatsTransmittedCells = _OchanStatsTransmittedCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 4, 1, 5),
    _OchanStatsTransmittedCells_Type()
)
ochanStatsTransmittedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochanStatsTransmittedCells.setStatus("current")
_OchanStatsIntentionalLostCells_Type = Counter32
_OchanStatsIntentionalLostCells_Object = MibTableColumn
ochanStatsIntentionalLostCells = _OchanStatsIntentionalLostCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 4, 1, 6),
    _OchanStatsIntentionalLostCells_Type()
)
ochanStatsIntentionalLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochanStatsIntentionalLostCells.setStatus("current")
_OchanStatsCLP0Cells_Type = Counter32
_OchanStatsCLP0Cells_Object = MibTableColumn
ochanStatsCLP0Cells = _OchanStatsCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 4, 1, 7),
    _OchanStatsCLP0Cells_Type()
)
ochanStatsCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochanStatsCLP0Cells.setStatus("current")
_OchanStatsLostPackets_Type = Counter32
_OchanStatsLostPackets_Object = MibTableColumn
ochanStatsLostPackets = _OchanStatsLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 4, 1, 8),
    _OchanStatsLostPackets_Type()
)
ochanStatsLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochanStatsLostPackets.setStatus("current")
_OchanStatsTransmittedPackets_Type = Counter32
_OchanStatsTransmittedPackets_Object = MibTableColumn
ochanStatsTransmittedPackets = _OchanStatsTransmittedPackets_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 4, 4, 1, 9),
    _OchanStatsTransmittedPackets_Type()
)
ochanStatsTransmittedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochanStatsTransmittedPackets.setStatus("current")
_TopologyGroup_ObjectIdentity = ObjectIdentity
topologyGroup = _TopologyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 5)
)
_NumberOfLinks_Type = Integer32
_NumberOfLinks_Object = MibScalar
numberOfLinks = _NumberOfLinks_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 5, 1),
    _NumberOfLinks_Type()
)
numberOfLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfLinks.setStatus("current")
_LinkTable_Object = MibTable
linkTable = _LinkTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    linkTable.setStatus("current")
_LinkEntry_Object = MibTableRow
linkEntry = _LinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 5, 2, 1)
)
linkEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "linkSrc"),
    (0, "Fore-Switch-MIB", "linkDest"),
)
if mibBuilder.loadTexts:
    linkEntry.setStatus("current")
_LinkSrc_Type = SpansAddress
_LinkSrc_Object = MibTableColumn
linkSrc = _LinkSrc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 5, 2, 1, 1),
    _LinkSrc_Type()
)
linkSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkSrc.setStatus("current")
_LinkDest_Type = SpansAddress
_LinkDest_Object = MibTableColumn
linkDest = _LinkDest_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 5, 2, 1, 2),
    _LinkDest_Type()
)
linkDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDest.setStatus("current")
_LinkCapacity_Type = Integer32
_LinkCapacity_Object = MibTableColumn
linkCapacity = _LinkCapacity_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 5, 2, 1, 3),
    _LinkCapacity_Type()
)
linkCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCapacity.setStatus("current")
_LinkAge_Type = Integer32
_LinkAge_Object = MibTableColumn
linkAge = _LinkAge_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 5, 2, 1, 4),
    _LinkAge_Type()
)
linkAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAge.setStatus("current")
_SignalingGroup_ObjectIdentity = ObjectIdentity
signalingGroup = _SignalingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6)
)
_SpansGroup_ObjectIdentity = ObjectIdentity
spansGroup = _SpansGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1)
)
_SigPathTable_Object = MibTable
sigPathTable = _SigPathTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    sigPathTable.setStatus("current")
_SigPathEntry_Object = MibTableRow
sigPathEntry = _SigPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 1, 1)
)
sigPathEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "sigPathPort"),
    (0, "Fore-Switch-MIB", "sigPathVPI"),
)
if mibBuilder.loadTexts:
    sigPathEntry.setStatus("current")
_SigPathPort_Type = Integer32
_SigPathPort_Object = MibTableColumn
sigPathPort = _SigPathPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 1, 1, 1),
    _SigPathPort_Type()
)
sigPathPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigPathPort.setStatus("current")
_SigPathVPI_Type = Integer32
_SigPathVPI_Object = MibTableColumn
sigPathVPI = _SigPathVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 1, 1, 2),
    _SigPathVPI_Type()
)
sigPathVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigPathVPI.setStatus("current")
_SigPathVCI_Type = Integer32
_SigPathVCI_Object = MibTableColumn
sigPathVCI = _SigPathVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 1, 1, 3),
    _SigPathVCI_Type()
)
sigPathVCI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sigPathVCI.setStatus("current")
_SigPathClsVCI_Type = Integer32
_SigPathClsVCI_Object = MibTableColumn
sigPathClsVCI = _SigPathClsVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 1, 1, 4),
    _SigPathClsVCI_Type()
)
sigPathClsVCI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sigPathClsVCI.setStatus("current")


class _SigPathAdminStatus_Type(Integer32):
    """Custom type sigPathAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_SigPathAdminStatus_Type.__name__ = "Integer32"
_SigPathAdminStatus_Object = MibTableColumn
sigPathAdminStatus = _SigPathAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 1, 1, 5),
    _SigPathAdminStatus_Type()
)
sigPathAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sigPathAdminStatus.setStatus("current")


class _SigPathOperStatus_Type(Integer32):
    """Custom type sigPathOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_SigPathOperStatus_Type.__name__ = "Integer32"
_SigPathOperStatus_Object = MibTableColumn
sigPathOperStatus = _SigPathOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 1, 1, 6),
    _SigPathOperStatus_Type()
)
sigPathOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigPathOperStatus.setStatus("current")
_SigPathEntryStatus_Type = EntryStatus
_SigPathEntryStatus_Object = MibTableColumn
sigPathEntryStatus = _SigPathEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 1, 1, 7),
    _SigPathEntryStatus_Type()
)
sigPathEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sigPathEntryStatus.setStatus("current")


class _SigPathAALType_Type(Integer32):
    """Custom type sigPathAALType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("type34", 1),
          ("type5", 2))
    )


_SigPathAALType_Type.__name__ = "Integer32"
_SigPathAALType_Object = MibTableColumn
sigPathAALType = _SigPathAALType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 1, 1, 8),
    _SigPathAALType_Type()
)
sigPathAALType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sigPathAALType.setStatus("current")
_SigPathCDV_Type = Integer32
_SigPathCDV_Object = MibTableColumn
sigPathCDV = _SigPathCDV_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 1, 1, 9),
    _SigPathCDV_Type()
)
sigPathCDV.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sigPathCDV.setStatus("current")


class _SigPathPolicingAction_Type(Integer32):
    """Custom type sigPathPolicingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("tag", 1))
    )


_SigPathPolicingAction_Type.__name__ = "Integer32"
_SigPathPolicingAction_Object = MibTableColumn
sigPathPolicingAction = _SigPathPolicingAction_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 1, 1, 10),
    _SigPathPolicingAction_Type()
)
sigPathPolicingAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sigPathPolicingAction.setStatus("current")
_SigPathRemoteAtmAddress_Type = SpansAddress
_SigPathRemoteAtmAddress_Object = MibTableColumn
sigPathRemoteAtmAddress = _SigPathRemoteAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 1, 1, 11),
    _SigPathRemoteAtmAddress_Type()
)
sigPathRemoteAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigPathRemoteAtmAddress.setStatus("current")
_SigPathRemoteIpAddress_Type = IpAddress
_SigPathRemoteIpAddress_Object = MibTableColumn
sigPathRemoteIpAddress = _SigPathRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 1, 1, 12),
    _SigPathRemoteIpAddress_Type()
)
sigPathRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigPathRemoteIpAddress.setStatus("current")


class _SigPathType_Type(Integer32):
    """Custom type sigPathType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nni", 2),
          ("uni", 1))
    )


_SigPathType_Type.__name__ = "Integer32"
_SigPathType_Object = MibTableColumn
sigPathType = _SigPathType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 1, 1, 13),
    _SigPathType_Type()
)
sigPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigPathType.setStatus("current")
_SigPathClsUpcContract_Type = Integer32
_SigPathClsUpcContract_Object = MibTableColumn
sigPathClsUpcContract = _SigPathClsUpcContract_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 1, 1, 14),
    _SigPathClsUpcContract_Type()
)
sigPathClsUpcContract.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sigPathClsUpcContract.setStatus("current")
_SigPathSigReservedBW_Type = Integer32
_SigPathSigReservedBW_Object = MibTableColumn
sigPathSigReservedBW = _SigPathSigReservedBW_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 1, 1, 15),
    _SigPathSigReservedBW_Type()
)
sigPathSigReservedBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sigPathSigReservedBW.setStatus("current")
_SigPathMinVCI_Type = Integer32
_SigPathMinVCI_Object = MibTableColumn
sigPathMinVCI = _SigPathMinVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 1, 1, 16),
    _SigPathMinVCI_Type()
)
sigPathMinVCI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sigPathMinVCI.setStatus("current")
_SigPathMaxVCI_Type = Integer32
_SigPathMaxVCI_Object = MibTableColumn
sigPathMaxVCI = _SigPathMaxVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 1, 1, 17),
    _SigPathMaxVCI_Type()
)
sigPathMaxVCI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sigPathMaxVCI.setStatus("current")


class _SigPathOpenTimeout_Type(Integer32):
    """Custom type sigPathOpenTimeout based on Integer32"""
    defaultValue = 300


_SigPathOpenTimeout_Object = MibTableColumn
sigPathOpenTimeout = _SigPathOpenTimeout_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 1, 1, 18),
    _SigPathOpenTimeout_Type()
)
sigPathOpenTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sigPathOpenTimeout.setStatus("current")


class _SigPathCloseTimeout_Type(Integer32):
    """Custom type sigPathCloseTimeout based on Integer32"""
    defaultValue = 500


_SigPathCloseTimeout_Object = MibTableColumn
sigPathCloseTimeout = _SigPathCloseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 1, 1, 19),
    _SigPathCloseTimeout_Type()
)
sigPathCloseTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sigPathCloseTimeout.setStatus("current")


class _SigPathOutputSigService_Type(Integer32):
    """Custom type sigPathOutputSigService based on Integer32"""
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
        *(("default", 4),
          ("oam", 3),
          ("ubr", 2),
          ("vbr", 1))
    )


_SigPathOutputSigService_Type.__name__ = "Integer32"
_SigPathOutputSigService_Object = MibTableColumn
sigPathOutputSigService = _SigPathOutputSigService_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 1, 1, 20),
    _SigPathOutputSigService_Type()
)
sigPathOutputSigService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sigPathOutputSigService.setStatus("current")


class _SigPathAALOperType_Type(Integer32):
    """Custom type sigPathAALOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type34", 1),
          ("type5", 2))
    )


_SigPathAALOperType_Type.__name__ = "Integer32"
_SigPathAALOperType_Object = MibTableColumn
sigPathAALOperType = _SigPathAALOperType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 1, 1, 21),
    _SigPathAALOperType_Type()
)
sigPathAALOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigPathAALOperType.setStatus("current")
_SigPathStatsTable_Object = MibTable
sigPathStatsTable = _SigPathStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    sigPathStatsTable.setStatus("current")
_SigPathStatsEntry_Object = MibTableRow
sigPathStatsEntry = _SigPathStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 2, 1)
)
sigPathStatsEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "sigPathStatsPort"),
    (0, "Fore-Switch-MIB", "sigPathStatsVPI"),
)
if mibBuilder.loadTexts:
    sigPathStatsEntry.setStatus("current")
_SigPathStatsPort_Type = Integer32
_SigPathStatsPort_Object = MibTableColumn
sigPathStatsPort = _SigPathStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 2, 1, 1),
    _SigPathStatsPort_Type()
)
sigPathStatsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigPathStatsPort.setStatus("current")
_SigPathStatsVPI_Type = Integer32
_SigPathStatsVPI_Object = MibTableColumn
sigPathStatsVPI = _SigPathStatsVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 2, 1, 2),
    _SigPathStatsVPI_Type()
)
sigPathStatsVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigPathStatsVPI.setStatus("current")
_SigPathVCCs_Type = Gauge32
_SigPathVCCs_Object = MibTableColumn
sigPathVCCs = _SigPathVCCs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 2, 1, 3),
    _SigPathVCCs_Type()
)
sigPathVCCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigPathVCCs.setStatus("current")
_SigPathRestarts_Type = Counter32
_SigPathRestarts_Object = MibTableColumn
sigPathRestarts = _SigPathRestarts_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 2, 1, 4),
    _SigPathRestarts_Type()
)
sigPathRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigPathRestarts.setStatus("current")
_SigPathCallsCompletions_Type = Counter32
_SigPathCallsCompletions_Object = MibTableColumn
sigPathCallsCompletions = _SigPathCallsCompletions_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 2, 1, 5),
    _SigPathCallsCompletions_Type()
)
sigPathCallsCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigPathCallsCompletions.setStatus("current")
_SigPathCallsFailures_Type = Counter32
_SigPathCallsFailures_Object = MibTableColumn
sigPathCallsFailures = _SigPathCallsFailures_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 2, 1, 6),
    _SigPathCallsFailures_Type()
)
sigPathCallsFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigPathCallsFailures.setStatus("current")
_SigPathCallsRejections_Type = Counter32
_SigPathCallsRejections_Object = MibTableColumn
sigPathCallsRejections = _SigPathCallsRejections_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 2, 1, 7),
    _SigPathCallsRejections_Type()
)
sigPathCallsRejections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigPathCallsRejections.setStatus("current")
_SigPathSpansTransmittedMessages_Type = Counter32
_SigPathSpansTransmittedMessages_Object = MibTableColumn
sigPathSpansTransmittedMessages = _SigPathSpansTransmittedMessages_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 2, 1, 8),
    _SigPathSpansTransmittedMessages_Type()
)
sigPathSpansTransmittedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigPathSpansTransmittedMessages.setStatus("current")
_SigPathSpansReceivedMessages_Type = Counter32
_SigPathSpansReceivedMessages_Object = MibTableColumn
sigPathSpansReceivedMessages = _SigPathSpansReceivedMessages_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 2, 1, 9),
    _SigPathSpansReceivedMessages_Type()
)
sigPathSpansReceivedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigPathSpansReceivedMessages.setStatus("current")
_SigPathClsTransmittedMessages_Type = Counter32
_SigPathClsTransmittedMessages_Object = MibTableColumn
sigPathClsTransmittedMessages = _SigPathClsTransmittedMessages_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 2, 1, 10),
    _SigPathClsTransmittedMessages_Type()
)
sigPathClsTransmittedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigPathClsTransmittedMessages.setStatus("current")
_SigPathClsReceivedMessages_Type = Counter32
_SigPathClsReceivedMessages_Object = MibTableColumn
sigPathClsReceivedMessages = _SigPathClsReceivedMessages_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 2, 1, 11),
    _SigPathClsReceivedMessages_Type()
)
sigPathClsReceivedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigPathClsReceivedMessages.setStatus("current")
_SpvcSrcNumberOfSPVCs_Type = Integer32
_SpvcSrcNumberOfSPVCs_Object = MibScalar
spvcSrcNumberOfSPVCs = _SpvcSrcNumberOfSPVCs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 3),
    _SpvcSrcNumberOfSPVCs_Type()
)
spvcSrcNumberOfSPVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spvcSrcNumberOfSPVCs.setStatus("current")
_SpvcSrcTable_Object = MibTable
spvcSrcTable = _SpvcSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 4)
)
if mibBuilder.loadTexts:
    spvcSrcTable.setStatus("current")
_SpvcSrcEntry_Object = MibTableRow
spvcSrcEntry = _SpvcSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 4, 1)
)
spvcSrcEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "spvcSrcSpvcId"),
)
if mibBuilder.loadTexts:
    spvcSrcEntry.setStatus("current")
_SpvcSrcSpvcId_Type = Integer32
_SpvcSrcSpvcId_Object = MibTableColumn
spvcSrcSpvcId = _SpvcSrcSpvcId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 4, 1, 1),
    _SpvcSrcSpvcId_Type()
)
spvcSrcSpvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spvcSrcSpvcId.setStatus("current")
_SpvcSrcSwitchAddr_Type = SpansAddress
_SpvcSrcSwitchAddr_Object = MibTableColumn
spvcSrcSwitchAddr = _SpvcSrcSwitchAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 4, 1, 2),
    _SpvcSrcSwitchAddr_Type()
)
spvcSrcSwitchAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spvcSrcSwitchAddr.setStatus("current")
_SpvcSrcDestSpvcId_Type = Integer32
_SpvcSrcDestSpvcId_Object = MibTableColumn
spvcSrcDestSpvcId = _SpvcSrcDestSpvcId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 4, 1, 3),
    _SpvcSrcDestSpvcId_Type()
)
spvcSrcDestSpvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spvcSrcDestSpvcId.setStatus("current")
_SpvcSrcDestSwitchAddr_Type = SpansAddress
_SpvcSrcDestSwitchAddr_Object = MibTableColumn
spvcSrcDestSwitchAddr = _SpvcSrcDestSwitchAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 4, 1, 4),
    _SpvcSrcDestSwitchAddr_Type()
)
spvcSrcDestSwitchAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spvcSrcDestSwitchAddr.setStatus("current")
_SpvcSrcInPort_Type = Integer32
_SpvcSrcInPort_Object = MibTableColumn
spvcSrcInPort = _SpvcSrcInPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 4, 1, 5),
    _SpvcSrcInPort_Type()
)
spvcSrcInPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spvcSrcInPort.setStatus("current")
_SpvcSrcInVPI_Type = Integer32
_SpvcSrcInVPI_Object = MibTableColumn
spvcSrcInVPI = _SpvcSrcInVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 4, 1, 6),
    _SpvcSrcInVPI_Type()
)
spvcSrcInVPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spvcSrcInVPI.setStatus("current")
_SpvcSrcInVCI_Type = Integer32
_SpvcSrcInVCI_Object = MibTableColumn
spvcSrcInVCI = _SpvcSrcInVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 4, 1, 7),
    _SpvcSrcInVCI_Type()
)
spvcSrcInVCI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spvcSrcInVCI.setStatus("current")
_SpvcSrcAllocBandwidth_Type = Gauge32
_SpvcSrcAllocBandwidth_Object = MibTableColumn
spvcSrcAllocBandwidth = _SpvcSrcAllocBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 4, 1, 8),
    _SpvcSrcAllocBandwidth_Type()
)
spvcSrcAllocBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spvcSrcAllocBandwidth.setStatus("current")
_SpvcSrcUpTime_Type = TimeTicks
_SpvcSrcUpTime_Object = MibTableColumn
spvcSrcUpTime = _SpvcSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 4, 1, 9),
    _SpvcSrcUpTime_Type()
)
spvcSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spvcSrcUpTime.setStatus("current")


class _SpvcSrcStatus_Type(Integer32):
    """Custom type spvcSrcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_SpvcSrcStatus_Type.__name__ = "Integer32"
_SpvcSrcStatus_Object = MibTableColumn
spvcSrcStatus = _SpvcSrcStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 4, 1, 10),
    _SpvcSrcStatus_Type()
)
spvcSrcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spvcSrcStatus.setStatus("current")
_SpvcSrcEntryStatus_Type = EntryStatus
_SpvcSrcEntryStatus_Object = MibTableColumn
spvcSrcEntryStatus = _SpvcSrcEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 4, 1, 11),
    _SpvcSrcEntryStatus_Type()
)
spvcSrcEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spvcSrcEntryStatus.setStatus("current")
_SpvcDestNumberOfSPVCs_Type = Integer32
_SpvcDestNumberOfSPVCs_Object = MibScalar
spvcDestNumberOfSPVCs = _SpvcDestNumberOfSPVCs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 5),
    _SpvcDestNumberOfSPVCs_Type()
)
spvcDestNumberOfSPVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spvcDestNumberOfSPVCs.setStatus("current")
_SpvcDestTable_Object = MibTable
spvcDestTable = _SpvcDestTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 6)
)
if mibBuilder.loadTexts:
    spvcDestTable.setStatus("current")
_SpvcDestEntry_Object = MibTableRow
spvcDestEntry = _SpvcDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 6, 1)
)
spvcDestEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "spvcDestSpvcId"),
)
if mibBuilder.loadTexts:
    spvcDestEntry.setStatus("current")
_SpvcDestSpvcId_Type = Integer32
_SpvcDestSpvcId_Object = MibTableColumn
spvcDestSpvcId = _SpvcDestSpvcId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 6, 1, 1),
    _SpvcDestSpvcId_Type()
)
spvcDestSpvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spvcDestSpvcId.setStatus("current")
_SpvcDestSwitchAddr_Type = SpansAddress
_SpvcDestSwitchAddr_Object = MibTableColumn
spvcDestSwitchAddr = _SpvcDestSwitchAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 6, 1, 2),
    _SpvcDestSwitchAddr_Type()
)
spvcDestSwitchAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spvcDestSwitchAddr.setStatus("current")
_SpvcDestSrcSpvcId_Type = Integer32
_SpvcDestSrcSpvcId_Object = MibTableColumn
spvcDestSrcSpvcId = _SpvcDestSrcSpvcId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 6, 1, 3),
    _SpvcDestSrcSpvcId_Type()
)
spvcDestSrcSpvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spvcDestSrcSpvcId.setStatus("current")
_SpvcDestSrcSwitchAddr_Type = SpansAddress
_SpvcDestSrcSwitchAddr_Object = MibTableColumn
spvcDestSrcSwitchAddr = _SpvcDestSrcSwitchAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 6, 1, 4),
    _SpvcDestSrcSwitchAddr_Type()
)
spvcDestSrcSwitchAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spvcDestSrcSwitchAddr.setStatus("current")
_SpvcDestOutPort_Type = Integer32
_SpvcDestOutPort_Object = MibTableColumn
spvcDestOutPort = _SpvcDestOutPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 6, 1, 5),
    _SpvcDestOutPort_Type()
)
spvcDestOutPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spvcDestOutPort.setStatus("current")
_SpvcDestOutVPI_Type = Integer32
_SpvcDestOutVPI_Object = MibTableColumn
spvcDestOutVPI = _SpvcDestOutVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 6, 1, 6),
    _SpvcDestOutVPI_Type()
)
spvcDestOutVPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spvcDestOutVPI.setStatus("current")
_SpvcDestOutVCI_Type = Integer32
_SpvcDestOutVCI_Object = MibTableColumn
spvcDestOutVCI = _SpvcDestOutVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 6, 1, 7),
    _SpvcDestOutVCI_Type()
)
spvcDestOutVCI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spvcDestOutVCI.setStatus("current")
_SpvcDestAllocBandwidth_Type = Gauge32
_SpvcDestAllocBandwidth_Object = MibTableColumn
spvcDestAllocBandwidth = _SpvcDestAllocBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 6, 1, 8),
    _SpvcDestAllocBandwidth_Type()
)
spvcDestAllocBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spvcDestAllocBandwidth.setStatus("current")
_SpvcDestUpTime_Type = TimeTicks
_SpvcDestUpTime_Object = MibTableColumn
spvcDestUpTime = _SpvcDestUpTime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 6, 1, 9),
    _SpvcDestUpTime_Type()
)
spvcDestUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spvcDestUpTime.setStatus("current")


class _SpvcDestStatus_Type(Integer32):
    """Custom type spvcDestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_SpvcDestStatus_Type.__name__ = "Integer32"
_SpvcDestStatus_Object = MibTableColumn
spvcDestStatus = _SpvcDestStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 6, 1, 10),
    _SpvcDestStatus_Type()
)
spvcDestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spvcDestStatus.setStatus("current")
_SpvcDestEntryStatus_Type = EntryStatus
_SpvcDestEntryStatus_Object = MibTableColumn
spvcDestEntryStatus = _SpvcDestEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 1, 6, 1, 11),
    _SpvcDestEntryStatus_Type()
)
spvcDestEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spvcDestEntryStatus.setStatus("current")
_Q2931Group_ObjectIdentity = ObjectIdentity
q2931Group = _Q2931Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2)
)
_Q2931LayerGroup_ObjectIdentity = ObjectIdentity
q2931LayerGroup = _Q2931LayerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1)
)
_Q2931AdminTable_Object = MibTable
q2931AdminTable = _Q2931AdminTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    q2931AdminTable.setStatus("current")
_Q2931AdminEntry_Object = MibTableRow
q2931AdminEntry = _Q2931AdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1)
)
q2931AdminEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "q2931AdminPort"),
    (0, "Fore-Switch-MIB", "q2931AdminVPI"),
)
if mibBuilder.loadTexts:
    q2931AdminEntry.setStatus("current")
_Q2931AdminPort_Type = Integer32
_Q2931AdminPort_Object = MibTableColumn
q2931AdminPort = _Q2931AdminPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 1),
    _Q2931AdminPort_Type()
)
q2931AdminPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931AdminPort.setStatus("current")
_Q2931AdminVPI_Type = Integer32
_Q2931AdminVPI_Object = MibTableColumn
q2931AdminVPI = _Q2931AdminVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 2),
    _Q2931AdminVPI_Type()
)
q2931AdminVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931AdminVPI.setStatus("current")
_Q2931AdminVCI_Type = Integer32
_Q2931AdminVCI_Object = MibTableColumn
q2931AdminVCI = _Q2931AdminVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 3),
    _Q2931AdminVCI_Type()
)
q2931AdminVCI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931AdminVCI.setStatus("current")


class _Q2931AdminStatus_Type(Integer32):
    """Custom type q2931AdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_Q2931AdminStatus_Type.__name__ = "Integer32"
_Q2931AdminStatus_Object = MibTableColumn
q2931AdminStatus = _Q2931AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 4),
    _Q2931AdminStatus_Type()
)
q2931AdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931AdminStatus.setStatus("current")


class _Q2931OperStatus_Type(Integer32):
    """Custom type q2931OperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_Q2931OperStatus_Type.__name__ = "Integer32"
_Q2931OperStatus_Object = MibTableColumn
q2931OperStatus = _Q2931OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 5),
    _Q2931OperStatus_Type()
)
q2931OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931OperStatus.setStatus("current")


class _Q2931SSCOPOperStatus_Type(Integer32):
    """Custom type q2931SSCOPOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_Q2931SSCOPOperStatus_Type.__name__ = "Integer32"
_Q2931SSCOPOperStatus_Object = MibTableColumn
q2931SSCOPOperStatus = _Q2931SSCOPOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 6),
    _Q2931SSCOPOperStatus_Type()
)
q2931SSCOPOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931SSCOPOperStatus.setStatus("current")


class _Q2931ILMIAdminStatus_Type(Integer32):
    """Custom type q2931ILMIAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_Q2931ILMIAdminStatus_Type.__name__ = "Integer32"
_Q2931ILMIAdminStatus_Object = MibTableColumn
q2931ILMIAdminStatus = _Q2931ILMIAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 7),
    _Q2931ILMIAdminStatus_Type()
)
q2931ILMIAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931ILMIAdminStatus.setStatus("current")


class _Q2931ILMIOperStatus_Type(Integer32):
    """Custom type q2931ILMIOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_Q2931ILMIOperStatus_Type.__name__ = "Integer32"
_Q2931ILMIOperStatus_Object = MibTableColumn
q2931ILMIOperStatus = _Q2931ILMIOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 8),
    _Q2931ILMIOperStatus_Type()
)
q2931ILMIOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931ILMIOperStatus.setStatus("current")


class _Q2931AdminAALType_Type(Integer32):
    """Custom type q2931AdminAALType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type34", 1),
          ("type5", 2))
    )


_Q2931AdminAALType_Type.__name__ = "Integer32"
_Q2931AdminAALType_Object = MibTableColumn
q2931AdminAALType = _Q2931AdminAALType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 9),
    _Q2931AdminAALType_Type()
)
q2931AdminAALType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931AdminAALType.setStatus("current")


class _Q2931AdminUNISide_Type(Integer32):
    """Custom type q2931AdminUNISide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 2),
          ("user", 1))
    )


_Q2931AdminUNISide_Type.__name__ = "Integer32"
_Q2931AdminUNISide_Object = MibTableColumn
q2931AdminUNISide = _Q2931AdminUNISide_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 10),
    _Q2931AdminUNISide_Type()
)
q2931AdminUNISide.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931AdminUNISide.setStatus("current")


class _Q2931AdminConfigType_Type(Integer32):
    """Custom type q2931AdminConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("automode", 2),
          ("ftPNNI", 4),
          ("iisp", 3),
          ("privateNNI", 5),
          ("privateUNI", 6),
          ("publicUNI", 1))
    )


_Q2931AdminConfigType_Type.__name__ = "Integer32"
_Q2931AdminConfigType_Object = MibTableColumn
q2931AdminConfigType = _Q2931AdminConfigType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 11),
    _Q2931AdminConfigType_Type()
)
q2931AdminConfigType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931AdminConfigType.setStatus("current")


class _Q2931AdminOperType_Type(Integer32):
    """Custom type q2931AdminOperType based on Integer32"""
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
        *(("ftPNNI", 4),
          ("iisp", 3),
          ("privateNNI", 5),
          ("privateUNI", 2),
          ("publicUNI", 1))
    )


_Q2931AdminOperType_Type.__name__ = "Integer32"
_Q2931AdminOperType_Object = MibTableColumn
q2931AdminOperType = _Q2931AdminOperType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 12),
    _Q2931AdminOperType_Type()
)
q2931AdminOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931AdminOperType.setStatus("current")
_Q2931AdminEntryStatus_Type = EntryStatus
_Q2931AdminEntryStatus_Object = MibTableColumn
q2931AdminEntryStatus = _Q2931AdminEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 13),
    _Q2931AdminEntryStatus_Type()
)
q2931AdminEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931AdminEntryStatus.setStatus("current")
_Q2931AdminRemoteIpAddress_Type = IpAddress
_Q2931AdminRemoteIpAddress_Object = MibTableColumn
q2931AdminRemoteIpAddress = _Q2931AdminRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 14),
    _Q2931AdminRemoteIpAddress_Type()
)
q2931AdminRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931AdminRemoteIpAddress.setStatus("current")
_Q2931SigReservedBW_Type = Integer32
_Q2931SigReservedBW_Object = MibTableColumn
q2931SigReservedBW = _Q2931SigReservedBW_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 15),
    _Q2931SigReservedBW_Type()
)
q2931SigReservedBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931SigReservedBW.setStatus("deprecated")
_Q2931ILMIReservedBW_Type = Integer32
_Q2931ILMIReservedBW_Object = MibTableColumn
q2931ILMIReservedBW = _Q2931ILMIReservedBW_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 16),
    _Q2931ILMIReservedBW_Type()
)
q2931ILMIReservedBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931ILMIReservedBW.setStatus("deprecated")
_Q2931ILMIAdminVCI_Type = Integer32
_Q2931ILMIAdminVCI_Object = MibTableColumn
q2931ILMIAdminVCI = _Q2931ILMIAdminVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 17),
    _Q2931ILMIAdminVCI_Type()
)
q2931ILMIAdminVCI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931ILMIAdminVCI.setStatus("current")
_Q2931AdminMinVCI_Type = Integer32
_Q2931AdminMinVCI_Object = MibTableColumn
q2931AdminMinVCI = _Q2931AdminMinVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 18),
    _Q2931AdminMinVCI_Type()
)
q2931AdminMinVCI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931AdminMinVCI.setStatus("current")
_Q2931AdminMaxVCI_Type = Integer32
_Q2931AdminMaxVCI_Object = MibTableColumn
q2931AdminMaxVCI = _Q2931AdminMaxVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 19),
    _Q2931AdminMaxVCI_Type()
)
q2931AdminMaxVCI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931AdminMaxVCI.setStatus("current")
_Q2931MinVCI_Type = Integer32
_Q2931MinVCI_Object = MibTableColumn
q2931MinVCI = _Q2931MinVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 20),
    _Q2931MinVCI_Type()
)
q2931MinVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931MinVCI.setStatus("current")
_Q2931MaxVCI_Type = Integer32
_Q2931MaxVCI_Object = MibTableColumn
q2931MaxVCI = _Q2931MaxVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 21),
    _Q2931MaxVCI_Type()
)
q2931MaxVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931MaxVCI.setStatus("current")


class _Q2931UNIConfigVersion_Type(Integer32):
    """Custom type q2931UNIConfigVersion based on Integer32"""
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
        *(("auto", 1),
          ("pnni10", 4),
          ("uni30", 2),
          ("uni31", 3),
          ("uni40", 5))
    )


_Q2931UNIConfigVersion_Type.__name__ = "Integer32"
_Q2931UNIConfigVersion_Object = MibTableColumn
q2931UNIConfigVersion = _Q2931UNIConfigVersion_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 22),
    _Q2931UNIConfigVersion_Type()
)
q2931UNIConfigVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931UNIConfigVersion.setStatus("current")


class _Q2931UNIOperVersion_Type(Integer32):
    """Custom type q2931UNIOperVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("pnni10", 3),
          ("uni30", 1),
          ("uni31", 2),
          ("uni40", 4))
    )


_Q2931UNIOperVersion_Type.__name__ = "Integer32"
_Q2931UNIOperVersion_Object = MibTableColumn
q2931UNIOperVersion = _Q2931UNIOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 23),
    _Q2931UNIOperVersion_Type()
)
q2931UNIOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931UNIOperVersion.setStatus("current")


class _Q2931ILMIRegistration_Type(Integer32):
    """Custom type q2931ILMIRegistration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("ignore", 3))
    )


_Q2931ILMIRegistration_Type.__name__ = "Integer32"
_Q2931ILMIRegistration_Object = MibTableColumn
q2931ILMIRegistration = _Q2931ILMIRegistration_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 24),
    _Q2931ILMIRegistration_Type()
)
q2931ILMIRegistration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931ILMIRegistration.setStatus("current")
_Q2931CallingPDefaultAddress_Type = NsapAddr
_Q2931CallingPDefaultAddress_Object = MibTableColumn
q2931CallingPDefaultAddress = _Q2931CallingPDefaultAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 25),
    _Q2931CallingPDefaultAddress_Type()
)
q2931CallingPDefaultAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931CallingPDefaultAddress.setStatus("current")


class _Q2931AdminUseNativeE164_Type(Integer32):
    """Custom type q2931AdminUseNativeE164 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_Q2931AdminUseNativeE164_Type.__name__ = "Integer32"
_Q2931AdminUseNativeE164_Object = MibTableColumn
q2931AdminUseNativeE164 = _Q2931AdminUseNativeE164_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 26),
    _Q2931AdminUseNativeE164_Type()
)
q2931AdminUseNativeE164.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931AdminUseNativeE164.setStatus("current")
_Q2931AdminNativeE164Address_Type = E164Address
_Q2931AdminNativeE164Address_Object = MibTableColumn
q2931AdminNativeE164Address = _Q2931AdminNativeE164Address_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 27),
    _Q2931AdminNativeE164Address_Type()
)
q2931AdminNativeE164Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931AdminNativeE164Address.setStatus("current")


class _Q2931AdminE164AddressResolution_Type(Integer32):
    """Custom type q2931AdminE164AddressResolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_Q2931AdminE164AddressResolution_Type.__name__ = "Integer32"
_Q2931AdminE164AddressResolution_Object = MibTableColumn
q2931AdminE164AddressResolution = _Q2931AdminE164AddressResolution_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 28),
    _Q2931AdminE164AddressResolution_Type()
)
q2931AdminE164AddressResolution.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931AdminE164AddressResolution.setStatus("current")


class _Q2931AdminFtPnniOrigCost_Type(Integer32):
    """Custom type q2931AdminFtPnniOrigCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Q2931AdminFtPnniOrigCost_Type.__name__ = "Integer32"
_Q2931AdminFtPnniOrigCost_Object = MibTableColumn
q2931AdminFtPnniOrigCost = _Q2931AdminFtPnniOrigCost_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 29),
    _Q2931AdminFtPnniOrigCost_Type()
)
q2931AdminFtPnniOrigCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931AdminFtPnniOrigCost.setStatus("deprecated")
_Q2931AdminFtPnniTermCost_Type = Integer32
_Q2931AdminFtPnniTermCost_Object = MibTableColumn
q2931AdminFtPnniTermCost = _Q2931AdminFtPnniTermCost_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 30),
    _Q2931AdminFtPnniTermCost_Type()
)
q2931AdminFtPnniTermCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931AdminFtPnniTermCost.setStatus("deprecated")
_Q2931AdminAVPresentation_Type = Integer32
_Q2931AdminAVPresentation_Object = MibTableColumn
q2931AdminAVPresentation = _Q2931AdminAVPresentation_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 31),
    _Q2931AdminAVPresentation_Type()
)
q2931AdminAVPresentation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931AdminAVPresentation.setStatus("deprecated")


class _Q2931AdminSigMode_Type(Integer32):
    """Custom type q2931AdminSigMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("nonAssoc", 2),
          ("vpAssoc", 1))
    )


_Q2931AdminSigMode_Type.__name__ = "Integer32"
_Q2931AdminSigMode_Object = MibTableColumn
q2931AdminSigMode = _Q2931AdminSigMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 32),
    _Q2931AdminSigMode_Type()
)
q2931AdminSigMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931AdminSigMode.setStatus("current")


class _Q2931AdminSigAlloc_Type(Integer32):
    """Custom type q2931AdminSigAlloc based on Integer32"""
    defaultValue = 3

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
        *(("allocLink", 2),
          ("allocProxy", 5),
          ("allocVP", 1),
          ("allocVpBundle", 4),
          ("auto", 3))
    )


_Q2931AdminSigAlloc_Type.__name__ = "Integer32"
_Q2931AdminSigAlloc_Object = MibTableColumn
q2931AdminSigAlloc = _Q2931AdminSigAlloc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 33),
    _Q2931AdminSigAlloc_Type()
)
q2931AdminSigAlloc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931AdminSigAlloc.setStatus("current")
_Q2931PeerPort_Type = Integer32
_Q2931PeerPort_Object = MibTableColumn
q2931PeerPort = _Q2931PeerPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 34),
    _Q2931PeerPort_Type()
)
q2931PeerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931PeerPort.setStatus("current")
_Q2931InputSigContract_Type = Integer32
_Q2931InputSigContract_Object = MibTableColumn
q2931InputSigContract = _Q2931InputSigContract_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 35),
    _Q2931InputSigContract_Type()
)
q2931InputSigContract.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931InputSigContract.setStatus("current")


class _Q2931OutputSigService_Type(Integer32):
    """Custom type q2931OutputSigService based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ubr", 2),
          ("unknown", 3),
          ("vbr", 1))
    )


_Q2931OutputSigService_Type.__name__ = "Integer32"
_Q2931OutputSigService_Object = MibTableColumn
q2931OutputSigService = _Q2931OutputSigService_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 36),
    _Q2931OutputSigService_Type()
)
q2931OutputSigService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931OutputSigService.setStatus("deprecated")
_Q2931SSCOPNoRespTimer_Type = Integer32
_Q2931SSCOPNoRespTimer_Object = MibTableColumn
q2931SSCOPNoRespTimer = _Q2931SSCOPNoRespTimer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 37),
    _Q2931SSCOPNoRespTimer_Type()
)
q2931SSCOPNoRespTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931SSCOPNoRespTimer.setStatus("current")
_Q2931AdminIncomingNSAPFilterIndex_Type = Integer32
_Q2931AdminIncomingNSAPFilterIndex_Object = MibTableColumn
q2931AdminIncomingNSAPFilterIndex = _Q2931AdminIncomingNSAPFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 46),
    _Q2931AdminIncomingNSAPFilterIndex_Type()
)
q2931AdminIncomingNSAPFilterIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931AdminIncomingNSAPFilterIndex.setStatus("current")
_Q2931AdminOutgoingNSAPFilterIndex_Type = Integer32
_Q2931AdminOutgoingNSAPFilterIndex_Object = MibTableColumn
q2931AdminOutgoingNSAPFilterIndex = _Q2931AdminOutgoingNSAPFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 47),
    _Q2931AdminOutgoingNSAPFilterIndex_Type()
)
q2931AdminOutgoingNSAPFilterIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931AdminOutgoingNSAPFilterIndex.setStatus("current")
_Q2931AdminIEFilter_Type = Integer32
_Q2931AdminIEFilter_Object = MibTableColumn
q2931AdminIEFilter = _Q2931AdminIEFilter_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 48),
    _Q2931AdminIEFilter_Type()
)
q2931AdminIEFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931AdminIEFilter.setStatus("current")


class _Q2931SendCallProc_Type(Integer32):
    """Custom type q2931SendCallProc based on Integer32"""
    defaultValue = 1

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


_Q2931SendCallProc_Type.__name__ = "Integer32"
_Q2931SendCallProc_Object = MibTableColumn
q2931SendCallProc = _Q2931SendCallProc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 49),
    _Q2931SendCallProc_Type()
)
q2931SendCallProc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931SendCallProc.setStatus("deprecated")


class _Q2931VCIRangeStatus_Type(Integer32):
    """Custom type q2931VCIRangeStatus based on Integer32"""
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


_Q2931VCIRangeStatus_Type.__name__ = "Integer32"
_Q2931VCIRangeStatus_Object = MibTableColumn
q2931VCIRangeStatus = _Q2931VCIRangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 51),
    _Q2931VCIRangeStatus_Type()
)
q2931VCIRangeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931VCIRangeStatus.setStatus("current")


class _Q2931ClearOnCarrierLoss_Type(Integer32):
    """Custom type q2931ClearOnCarrierLoss based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearCalls", 2),
          ("noClear", 1))
    )


_Q2931ClearOnCarrierLoss_Type.__name__ = "Integer32"
_Q2931ClearOnCarrierLoss_Object = MibTableColumn
q2931ClearOnCarrierLoss = _Q2931ClearOnCarrierLoss_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 52),
    _Q2931ClearOnCarrierLoss_Type()
)
q2931ClearOnCarrierLoss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931ClearOnCarrierLoss.setStatus("obsolete")
_Q2931QosClassExpansionKey_Type = Integer32
_Q2931QosClassExpansionKey_Object = MibTableColumn
q2931QosClassExpansionKey = _Q2931QosClassExpansionKey_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 54),
    _Q2931QosClassExpansionKey_Type()
)
q2931QosClassExpansionKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931QosClassExpansionKey.setStatus("current")
_Q2931AtmrConfDomainID_Type = Integer32
_Q2931AtmrConfDomainID_Object = MibTableColumn
q2931AtmrConfDomainID = _Q2931AtmrConfDomainID_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 55),
    _Q2931AtmrConfDomainID_Type()
)
q2931AtmrConfDomainID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931AtmrConfDomainID.setStatus("current")
_Q2931AtmrPnniNodeIndex_Type = Integer32
_Q2931AtmrPnniNodeIndex_Object = MibTableColumn
q2931AtmrPnniNodeIndex = _Q2931AtmrPnniNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 56),
    _Q2931AtmrPnniNodeIndex_Type()
)
q2931AtmrPnniNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931AtmrPnniNodeIndex.setStatus("current")


class _Q2931AdminOperSigMode_Type(Integer32):
    """Custom type q2931AdminOperSigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonAssoc", 2),
          ("vpAssoc", 1))
    )


_Q2931AdminOperSigMode_Type.__name__ = "Integer32"
_Q2931AdminOperSigMode_Object = MibTableColumn
q2931AdminOperSigMode = _Q2931AdminOperSigMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 57),
    _Q2931AdminOperSigMode_Type()
)
q2931AdminOperSigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931AdminOperSigMode.setStatus("current")


class _Q2931AdminOperSigAlloc_Type(Integer32):
    """Custom type q2931AdminOperSigAlloc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("allocLink", 2),
          ("allocProxy", 5),
          ("allocVP", 1),
          ("allocVpBundle", 4))
    )


_Q2931AdminOperSigAlloc_Type.__name__ = "Integer32"
_Q2931AdminOperSigAlloc_Object = MibTableColumn
q2931AdminOperSigAlloc = _Q2931AdminOperSigAlloc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 58),
    _Q2931AdminOperSigAlloc_Type()
)
q2931AdminOperSigAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931AdminOperSigAlloc.setStatus("current")
_Q2931OutputSigUpc_Type = Integer32
_Q2931OutputSigUpc_Object = MibTableColumn
q2931OutputSigUpc = _Q2931OutputSigUpc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 60),
    _Q2931OutputSigUpc_Type()
)
q2931OutputSigUpc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931OutputSigUpc.setStatus("current")


class _Q2931AdminPlanType_Type(Integer32):
    """Custom type q2931AdminPlanType based on Integer32"""
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
        *(("international", 2),
          ("national", 3),
          ("subscriber", 4),
          ("unknown", 1))
    )


_Q2931AdminPlanType_Type.__name__ = "Integer32"
_Q2931AdminPlanType_Object = MibTableColumn
q2931AdminPlanType = _Q2931AdminPlanType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 61),
    _Q2931AdminPlanType_Type()
)
q2931AdminPlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931AdminPlanType.setStatus("current")


class _Q2931AdminMaxVPI_Type(Integer32):
    """Custom type q2931AdminMaxVPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_Q2931AdminMaxVPI_Type.__name__ = "Integer32"
_Q2931AdminMaxVPI_Object = MibTableColumn
q2931AdminMaxVPI = _Q2931AdminMaxVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 62),
    _Q2931AdminMaxVPI_Type()
)
q2931AdminMaxVPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931AdminMaxVPI.setStatus("current")


class _Q2931MaxSvccVPI_Type(Integer32):
    """Custom type q2931MaxSvccVPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_Q2931MaxSvccVPI_Type.__name__ = "Integer32"
_Q2931MaxSvccVPI_Object = MibTableColumn
q2931MaxSvccVPI = _Q2931MaxSvccVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 63),
    _Q2931MaxSvccVPI_Type()
)
q2931MaxSvccVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931MaxSvccVPI.setStatus("current")
_Q2931LastChangeTime_Type = TimeStamp
_Q2931LastChangeTime_Object = MibTableColumn
q2931LastChangeTime = _Q2931LastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 64),
    _Q2931LastChangeTime_Type()
)
q2931LastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931LastChangeTime.setStatus("current")


class _Q2931NNIProto_Type(Integer32):
    """Custom type q2931NNIProto based on Integer32"""
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
        *(("forum-pnni", 3),
          ("ftpnni", 2),
          ("iisp", 4),
          ("none", 1))
    )


_Q2931NNIProto_Type.__name__ = "Integer32"
_Q2931NNIProto_Object = MibTableColumn
q2931NNIProto = _Q2931NNIProto_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 66),
    _Q2931NNIProto_Type()
)
q2931NNIProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931NNIProto.setStatus("current")


class _Q2931MaxSvpcVPI_Type(Integer32):
    """Custom type q2931MaxSvpcVPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_Q2931MaxSvpcVPI_Type.__name__ = "Integer32"
_Q2931MaxSvpcVPI_Object = MibTableColumn
q2931MaxSvpcVPI = _Q2931MaxSvpcVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 67),
    _Q2931MaxSvpcVPI_Type()
)
q2931MaxSvpcVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931MaxSvpcVPI.setStatus("current")


class _Q2931VpCapability_Type(Integer32):
    """Custom type q2931VpCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notVpCapable", 3),
          ("undefined", 1),
          ("vpCapable", 2))
    )


_Q2931VpCapability_Type.__name__ = "Integer32"
_Q2931VpCapability_Object = MibTableColumn
q2931VpCapability = _Q2931VpCapability_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 68),
    _Q2931VpCapability_Type()
)
q2931VpCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931VpCapability.setStatus("current")


class _Q2931VpciGroupIndex_Type(Integer32):
    """Custom type q2931VpciGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99999),
    )


_Q2931VpciGroupIndex_Type.__name__ = "Integer32"
_Q2931VpciGroupIndex_Object = MibTableColumn
q2931VpciGroupIndex = _Q2931VpciGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 69),
    _Q2931VpciGroupIndex_Type()
)
q2931VpciGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931VpciGroupIndex.setStatus("current")


class _Q2931AcceleratedClear_Type(Integer32):
    """Custom type q2931AcceleratedClear based on Integer32"""
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


_Q2931AcceleratedClear_Type.__name__ = "Integer32"
_Q2931AcceleratedClear_Object = MibTableColumn
q2931AcceleratedClear = _Q2931AcceleratedClear_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 70),
    _Q2931AcceleratedClear_Type()
)
q2931AcceleratedClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931AcceleratedClear.setStatus("current")


class _Q2931SupplementaryServicesStatus_Type(Integer32):
    """Custom type q2931SupplementaryServicesStatus based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("undefined", 3))
    )


_Q2931SupplementaryServicesStatus_Type.__name__ = "Integer32"
_Q2931SupplementaryServicesStatus_Object = MibTableColumn
q2931SupplementaryServicesStatus = _Q2931SupplementaryServicesStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 71),
    _Q2931SupplementaryServicesStatus_Type()
)
q2931SupplementaryServicesStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931SupplementaryServicesStatus.setStatus("current")


class _Q2931CallingPAddressPresentation_Type(Integer32):
    """Custom type q2931CallingPAddressPresentation based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("undefined", 3))
    )


_Q2931CallingPAddressPresentation_Type.__name__ = "Integer32"
_Q2931CallingPAddressPresentation_Object = MibTableColumn
q2931CallingPAddressPresentation = _Q2931CallingPAddressPresentation_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 72),
    _Q2931CallingPAddressPresentation_Type()
)
q2931CallingPAddressPresentation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931CallingPAddressPresentation.setStatus("current")


class _Q2931CallingPAddressRestriction_Type(Integer32):
    """Custom type q2931CallingPAddressRestriction based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("undefined", 3))
    )


_Q2931CallingPAddressRestriction_Type.__name__ = "Integer32"
_Q2931CallingPAddressRestriction_Object = MibTableColumn
q2931CallingPAddressRestriction = _Q2931CallingPAddressRestriction_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 73),
    _Q2931CallingPAddressRestriction_Type()
)
q2931CallingPAddressRestriction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931CallingPAddressRestriction.setStatus("current")


class _Q2931ConnectedPAddressPresentation_Type(Integer32):
    """Custom type q2931ConnectedPAddressPresentation based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("undefined", 3))
    )


_Q2931ConnectedPAddressPresentation_Type.__name__ = "Integer32"
_Q2931ConnectedPAddressPresentation_Object = MibTableColumn
q2931ConnectedPAddressPresentation = _Q2931ConnectedPAddressPresentation_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 74),
    _Q2931ConnectedPAddressPresentation_Type()
)
q2931ConnectedPAddressPresentation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931ConnectedPAddressPresentation.setStatus("current")


class _Q2931ConnectedPAddressRestriction_Type(Integer32):
    """Custom type q2931ConnectedPAddressRestriction based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("undefined", 3))
    )


_Q2931ConnectedPAddressRestriction_Type.__name__ = "Integer32"
_Q2931ConnectedPAddressRestriction_Object = MibTableColumn
q2931ConnectedPAddressRestriction = _Q2931ConnectedPAddressRestriction_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 75),
    _Q2931ConnectedPAddressRestriction_Type()
)
q2931ConnectedPAddressRestriction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931ConnectedPAddressRestriction.setStatus("current")
_Q2931ConnectedPDefaultAddress_Type = NsapAddr
_Q2931ConnectedPDefaultAddress_Object = MibTableColumn
q2931ConnectedPDefaultAddress = _Q2931ConnectedPDefaultAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 76),
    _Q2931ConnectedPDefaultAddress_Type()
)
q2931ConnectedPDefaultAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931ConnectedPDefaultAddress.setStatus("current")


class _Q2931SubaddressingAdminStatus_Type(Integer32):
    """Custom type q2931SubaddressingAdminStatus based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("undefined", 3))
    )


_Q2931SubaddressingAdminStatus_Type.__name__ = "Integer32"
_Q2931SubaddressingAdminStatus_Object = MibTableColumn
q2931SubaddressingAdminStatus = _Q2931SubaddressingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 77),
    _Q2931SubaddressingAdminStatus_Type()
)
q2931SubaddressingAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931SubaddressingAdminStatus.setStatus("current")


class _Q2931UserUserSignallingAdminStatus_Type(Integer32):
    """Custom type q2931UserUserSignallingAdminStatus based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("undefined", 3))
    )


_Q2931UserUserSignallingAdminStatus_Type.__name__ = "Integer32"
_Q2931UserUserSignallingAdminStatus_Object = MibTableColumn
q2931UserUserSignallingAdminStatus = _Q2931UserUserSignallingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 78),
    _Q2931UserUserSignallingAdminStatus_Type()
)
q2931UserUserSignallingAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931UserUserSignallingAdminStatus.setStatus("current")
_Q2931OutputIlmiUpc_Type = Integer32
_Q2931OutputIlmiUpc_Object = MibTableColumn
q2931OutputIlmiUpc = _Q2931OutputIlmiUpc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 79),
    _Q2931OutputIlmiUpc_Type()
)
q2931OutputIlmiUpc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931OutputIlmiUpc.setStatus("current")
_Q2931OutputRccUpc_Type = Integer32
_Q2931OutputRccUpc_Object = MibTableColumn
q2931OutputRccUpc = _Q2931OutputRccUpc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 80),
    _Q2931OutputRccUpc_Type()
)
q2931OutputRccUpc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931OutputRccUpc.setStatus("current")


class _Q2931PnniRccVci_Type(Integer32):
    """Custom type q2931PnniRccVci based on Integer32"""
    defaultValue = 18


_Q2931PnniRccVci_Object = MibTableColumn
q2931PnniRccVci = _Q2931PnniRccVci_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 81),
    _Q2931PnniRccVci_Type()
)
q2931PnniRccVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931PnniRccVci.setStatus("current")


class _Q2931AdminubrCalls_Type(Integer32):
    """Custom type q2931AdminubrCalls based on Integer32"""
    defaultValue = 1

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


_Q2931AdminubrCalls_Type.__name__ = "Integer32"
_Q2931AdminubrCalls_Object = MibTableColumn
q2931AdminubrCalls = _Q2931AdminubrCalls_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 82),
    _Q2931AdminubrCalls_Type()
)
q2931AdminubrCalls.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931AdminubrCalls.setStatus("current")


class _Q2931AdmincbrCalls_Type(Integer32):
    """Custom type q2931AdmincbrCalls based on Integer32"""
    defaultValue = 1

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


_Q2931AdmincbrCalls_Type.__name__ = "Integer32"
_Q2931AdmincbrCalls_Object = MibTableColumn
q2931AdmincbrCalls = _Q2931AdmincbrCalls_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 83),
    _Q2931AdmincbrCalls_Type()
)
q2931AdmincbrCalls.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931AdmincbrCalls.setStatus("current")


class _Q2931AdminabrCalls_Type(Integer32):
    """Custom type q2931AdminabrCalls based on Integer32"""
    defaultValue = 1

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


_Q2931AdminabrCalls_Type.__name__ = "Integer32"
_Q2931AdminabrCalls_Object = MibTableColumn
q2931AdminabrCalls = _Q2931AdminabrCalls_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 84),
    _Q2931AdminabrCalls_Type()
)
q2931AdminabrCalls.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931AdminabrCalls.setStatus("current")


class _Q2931AdminrtvbrCalls_Type(Integer32):
    """Custom type q2931AdminrtvbrCalls based on Integer32"""
    defaultValue = 1

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


_Q2931AdminrtvbrCalls_Type.__name__ = "Integer32"
_Q2931AdminrtvbrCalls_Object = MibTableColumn
q2931AdminrtvbrCalls = _Q2931AdminrtvbrCalls_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 85),
    _Q2931AdminrtvbrCalls_Type()
)
q2931AdminrtvbrCalls.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931AdminrtvbrCalls.setStatus("current")


class _Q2931AdminnrtvbrCalls_Type(Integer32):
    """Custom type q2931AdminnrtvbrCalls based on Integer32"""
    defaultValue = 1

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


_Q2931AdminnrtvbrCalls_Type.__name__ = "Integer32"
_Q2931AdminnrtvbrCalls_Object = MibTableColumn
q2931AdminnrtvbrCalls = _Q2931AdminnrtvbrCalls_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 86),
    _Q2931AdminnrtvbrCalls_Type()
)
q2931AdminnrtvbrCalls.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931AdminnrtvbrCalls.setStatus("current")


class _Q2931ProxyDirGroupIndex_Type(Integer32):
    """Custom type q2931ProxyDirGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99999),
    )


_Q2931ProxyDirGroupIndex_Type.__name__ = "Integer32"
_Q2931ProxyDirGroupIndex_Object = MibTableColumn
q2931ProxyDirGroupIndex = _Q2931ProxyDirGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 1, 1, 87),
    _Q2931ProxyDirGroupIndex_Type()
)
q2931ProxyDirGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931ProxyDirGroupIndex.setStatus("current")
_Q2931StatsTable_Object = MibTable
q2931StatsTable = _Q2931StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 2)
)
if mibBuilder.loadTexts:
    q2931StatsTable.setStatus("current")
_Q2931StatsEntry_Object = MibTableRow
q2931StatsEntry = _Q2931StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 2, 1)
)
q2931StatsEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "q2931StatsPort"),
    (0, "Fore-Switch-MIB", "q2931StatsVPI"),
)
if mibBuilder.loadTexts:
    q2931StatsEntry.setStatus("current")
_Q2931StatsPort_Type = Integer32
_Q2931StatsPort_Object = MibTableColumn
q2931StatsPort = _Q2931StatsPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 2, 1, 1),
    _Q2931StatsPort_Type()
)
q2931StatsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931StatsPort.setStatus("current")
_Q2931StatsVPI_Type = Integer32
_Q2931StatsVPI_Object = MibTableColumn
q2931StatsVPI = _Q2931StatsVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 2, 1, 2),
    _Q2931StatsVPI_Type()
)
q2931StatsVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931StatsVPI.setStatus("current")
_Q2931VCCs_Type = Gauge32
_Q2931VCCs_Object = MibTableColumn
q2931VCCs = _Q2931VCCs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 2, 1, 3),
    _Q2931VCCs_Type()
)
q2931VCCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931VCCs.setStatus("current")
_Q2931Restarts_Type = Counter32
_Q2931Restarts_Object = MibTableColumn
q2931Restarts = _Q2931Restarts_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 2, 1, 4),
    _Q2931Restarts_Type()
)
q2931Restarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931Restarts.setStatus("current")
_Q2931CallsCompletions_Type = Counter32
_Q2931CallsCompletions_Object = MibTableColumn
q2931CallsCompletions = _Q2931CallsCompletions_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 2, 1, 5),
    _Q2931CallsCompletions_Type()
)
q2931CallsCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931CallsCompletions.setStatus("current")
_Q2931CallsFailures_Type = Counter32
_Q2931CallsFailures_Object = MibTableColumn
q2931CallsFailures = _Q2931CallsFailures_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 2, 1, 6),
    _Q2931CallsFailures_Type()
)
q2931CallsFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931CallsFailures.setStatus("current")
_Q2931CallsRejections_Type = Counter32
_Q2931CallsRejections_Object = MibTableColumn
q2931CallsRejections = _Q2931CallsRejections_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 2, 1, 7),
    _Q2931CallsRejections_Type()
)
q2931CallsRejections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931CallsRejections.setStatus("current")
_Q2931TransmittedMessages_Type = Counter32
_Q2931TransmittedMessages_Object = MibTableColumn
q2931TransmittedMessages = _Q2931TransmittedMessages_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 2, 1, 8),
    _Q2931TransmittedMessages_Type()
)
q2931TransmittedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931TransmittedMessages.setStatus("current")
_Q2931ReceivedMessages_Type = Counter32
_Q2931ReceivedMessages_Object = MibTableColumn
q2931ReceivedMessages = _Q2931ReceivedMessages_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 2, 1, 9),
    _Q2931ReceivedMessages_Type()
)
q2931ReceivedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931ReceivedMessages.setStatus("current")
_Q2931AddressFilterGroup_ObjectIdentity = ObjectIdentity
q2931AddressFilterGroup = _Q2931AddressFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6)
)
_Q2931AFTemplateTable_Object = MibTable
q2931AFTemplateTable = _Q2931AFTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    q2931AFTemplateTable.setStatus("current")
_Q2931AFTemplateEntry_Object = MibTableRow
q2931AFTemplateEntry = _Q2931AFTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 1, 1)
)
q2931AFTemplateEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "q2931AFTemplateIndex"),
)
if mibBuilder.loadTexts:
    q2931AFTemplateEntry.setStatus("current")
_Q2931AFTemplateIndex_Type = Integer32
_Q2931AFTemplateIndex_Object = MibTableColumn
q2931AFTemplateIndex = _Q2931AFTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 1, 1, 1),
    _Q2931AFTemplateIndex_Type()
)
q2931AFTemplateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    q2931AFTemplateIndex.setStatus("current")
_Q2931AFTemplateSrcPort_Type = Integer32
_Q2931AFTemplateSrcPort_Object = MibTableColumn
q2931AFTemplateSrcPort = _Q2931AFTemplateSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 1, 1, 2),
    _Q2931AFTemplateSrcPort_Type()
)
q2931AFTemplateSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931AFTemplateSrcPort.setStatus("current")
_Q2931AFTemplateSrcVPI_Type = Integer32
_Q2931AFTemplateSrcVPI_Object = MibTableColumn
q2931AFTemplateSrcVPI = _Q2931AFTemplateSrcVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 1, 1, 3),
    _Q2931AFTemplateSrcVPI_Type()
)
q2931AFTemplateSrcVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931AFTemplateSrcVPI.setStatus("current")
_Q2931AFTemplateSrcNsap_Type = NsapAddr
_Q2931AFTemplateSrcNsap_Object = MibTableColumn
q2931AFTemplateSrcNsap = _Q2931AFTemplateSrcNsap_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 1, 1, 4),
    _Q2931AFTemplateSrcNsap_Type()
)
q2931AFTemplateSrcNsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931AFTemplateSrcNsap.setStatus("current")
_Q2931AFTemplateSrcNsapMask_Type = Integer32
_Q2931AFTemplateSrcNsapMask_Object = MibTableColumn
q2931AFTemplateSrcNsapMask = _Q2931AFTemplateSrcNsapMask_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 1, 1, 5),
    _Q2931AFTemplateSrcNsapMask_Type()
)
q2931AFTemplateSrcNsapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931AFTemplateSrcNsapMask.setStatus("current")
_Q2931AFTemplateDstPort_Type = Integer32
_Q2931AFTemplateDstPort_Object = MibTableColumn
q2931AFTemplateDstPort = _Q2931AFTemplateDstPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 1, 1, 6),
    _Q2931AFTemplateDstPort_Type()
)
q2931AFTemplateDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931AFTemplateDstPort.setStatus("current")
_Q2931AFTemplateDstVPI_Type = Integer32
_Q2931AFTemplateDstVPI_Object = MibTableColumn
q2931AFTemplateDstVPI = _Q2931AFTemplateDstVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 1, 1, 7),
    _Q2931AFTemplateDstVPI_Type()
)
q2931AFTemplateDstVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931AFTemplateDstVPI.setStatus("current")
_Q2931AFTemplateDstNsap_Type = NsapAddr
_Q2931AFTemplateDstNsap_Object = MibTableColumn
q2931AFTemplateDstNsap = _Q2931AFTemplateDstNsap_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 1, 1, 8),
    _Q2931AFTemplateDstNsap_Type()
)
q2931AFTemplateDstNsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931AFTemplateDstNsap.setStatus("current")
_Q2931AFTemplateDstNsapMask_Type = Integer32
_Q2931AFTemplateDstNsapMask_Object = MibTableColumn
q2931AFTemplateDstNsapMask = _Q2931AFTemplateDstNsapMask_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 1, 1, 9),
    _Q2931AFTemplateDstNsapMask_Type()
)
q2931AFTemplateDstNsapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931AFTemplateDstNsapMask.setStatus("current")


class _Q2931AFTemplateAction_Type(Integer32):
    """Custom type q2931AFTemplateAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2))
    )


_Q2931AFTemplateAction_Type.__name__ = "Integer32"
_Q2931AFTemplateAction_Object = MibTableColumn
q2931AFTemplateAction = _Q2931AFTemplateAction_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 1, 1, 10),
    _Q2931AFTemplateAction_Type()
)
q2931AFTemplateAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931AFTemplateAction.setStatus("current")


class _Q2931AFTemplateName_Type(OctetString):
    """Custom type q2931AFTemplateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Q2931AFTemplateName_Type.__name__ = "OctetString"
_Q2931AFTemplateName_Object = MibTableColumn
q2931AFTemplateName = _Q2931AFTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 1, 1, 11),
    _Q2931AFTemplateName_Type()
)
q2931AFTemplateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931AFTemplateName.setStatus("current")
_Q2931AFTemplateStatus_Type = RowStatus
_Q2931AFTemplateStatus_Object = MibTableColumn
q2931AFTemplateStatus = _Q2931AFTemplateStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 1, 1, 12),
    _Q2931AFTemplateStatus_Type()
)
q2931AFTemplateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931AFTemplateStatus.setStatus("current")
_Q2931AFTemplateNextIndex_Type = TestAndIncr
_Q2931AFTemplateNextIndex_Object = MibScalar
q2931AFTemplateNextIndex = _Q2931AFTemplateNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 1, 2),
    _Q2931AFTemplateNextIndex_Type()
)
q2931AFTemplateNextIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931AFTemplateNextIndex.setStatus("current")
_Q2931AFFilterTable_Object = MibTable
q2931AFFilterTable = _Q2931AFFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 2)
)
if mibBuilder.loadTexts:
    q2931AFFilterTable.setStatus("current")
_Q2931AFFilterEntry_Object = MibTableRow
q2931AFFilterEntry = _Q2931AFFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 2, 1)
)
q2931AFFilterEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "q2931AFFilterIndex"),
)
if mibBuilder.loadTexts:
    q2931AFFilterEntry.setStatus("current")
_Q2931AFFilterIndex_Type = Integer32
_Q2931AFFilterIndex_Object = MibTableColumn
q2931AFFilterIndex = _Q2931AFFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 2, 1, 1),
    _Q2931AFFilterIndex_Type()
)
q2931AFFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    q2931AFFilterIndex.setStatus("current")


class _Q2931AFFilterName_Type(OctetString):
    """Custom type q2931AFFilterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Q2931AFFilterName_Type.__name__ = "OctetString"
_Q2931AFFilterName_Object = MibTableColumn
q2931AFFilterName = _Q2931AFFilterName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 2, 1, 2),
    _Q2931AFFilterName_Type()
)
q2931AFFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931AFFilterName.setStatus("current")
_Q2931AFFilterStatus_Type = RowStatus
_Q2931AFFilterStatus_Object = MibTableColumn
q2931AFFilterStatus = _Q2931AFFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 2, 1, 3),
    _Q2931AFFilterStatus_Type()
)
q2931AFFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931AFFilterStatus.setStatus("current")
_Q2931AFFilterNextIndex_Type = TestAndIncr
_Q2931AFFilterNextIndex_Object = MibScalar
q2931AFFilterNextIndex = _Q2931AFFilterNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 2, 2),
    _Q2931AFFilterNextIndex_Type()
)
q2931AFFilterNextIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931AFFilterNextIndex.setStatus("current")
_Q2931AFFilterTListTable_Object = MibTable
q2931AFFilterTListTable = _Q2931AFFilterTListTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 3)
)
if mibBuilder.loadTexts:
    q2931AFFilterTListTable.setStatus("current")
_Q2931AFFilterTListEntry_Object = MibTableRow
q2931AFFilterTListEntry = _Q2931AFFilterTListEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 3, 1)
)
q2931AFFilterTListEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "q2931AFFilterIndex"),
    (0, "Fore-Switch-MIB", "q2931AFFilterTListIndex"),
)
if mibBuilder.loadTexts:
    q2931AFFilterTListEntry.setStatus("current")
_Q2931AFFilterTListIndex_Type = Integer32
_Q2931AFFilterTListIndex_Object = MibTableColumn
q2931AFFilterTListIndex = _Q2931AFFilterTListIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 3, 1, 1),
    _Q2931AFFilterTListIndex_Type()
)
q2931AFFilterTListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    q2931AFFilterTListIndex.setStatus("current")
_Q2931AFFilterTListTemplateIndex_Type = Integer32
_Q2931AFFilterTListTemplateIndex_Object = MibTableColumn
q2931AFFilterTListTemplateIndex = _Q2931AFFilterTListTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 3, 1, 2),
    _Q2931AFFilterTListTemplateIndex_Type()
)
q2931AFFilterTListTemplateIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931AFFilterTListTemplateIndex.setStatus("current")
_Q2931AFFilterTListStatus_Type = RowStatus
_Q2931AFFilterTListStatus_Object = MibTableColumn
q2931AFFilterTListStatus = _Q2931AFFilterTListStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 3, 1, 3),
    _Q2931AFFilterTListStatus_Type()
)
q2931AFFilterTListStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931AFFilterTListStatus.setStatus("current")
_Q2931AFStatsTable_Object = MibTable
q2931AFStatsTable = _Q2931AFStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 4)
)
if mibBuilder.loadTexts:
    q2931AFStatsTable.setStatus("current")
_Q2931AFStatsEntry_Object = MibTableRow
q2931AFStatsEntry = _Q2931AFStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 4, 1)
)
q2931AFStatsEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "q2931AdminPort"),
    (0, "Fore-Switch-MIB", "q2931AdminVPI"),
    (0, "Fore-Switch-MIB", "q2931AFDirection"),
)
if mibBuilder.loadTexts:
    q2931AFStatsEntry.setStatus("current")


class _Q2931AFDirection_Type(Integer32):
    """Custom type q2931AFDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2))
    )


_Q2931AFDirection_Type.__name__ = "Integer32"
_Q2931AFDirection_Object = MibTableColumn
q2931AFDirection = _Q2931AFDirection_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 4, 1, 1),
    _Q2931AFDirection_Type()
)
q2931AFDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    q2931AFDirection.setStatus("current")
_Q2931AFAccepts_Type = Counter32
_Q2931AFAccepts_Object = MibTableColumn
q2931AFAccepts = _Q2931AFAccepts_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 4, 1, 2),
    _Q2931AFAccepts_Type()
)
q2931AFAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931AFAccepts.setStatus("current")
_Q2931AFRejectKnowns_Type = Counter32
_Q2931AFRejectKnowns_Object = MibTableColumn
q2931AFRejectKnowns = _Q2931AFRejectKnowns_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 4, 1, 3),
    _Q2931AFRejectKnowns_Type()
)
q2931AFRejectKnowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931AFRejectKnowns.setStatus("current")
_Q2931AFRejectUnknowns_Type = Counter32
_Q2931AFRejectUnknowns_Object = MibTableColumn
q2931AFRejectUnknowns = _Q2931AFRejectUnknowns_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 4, 1, 4),
    _Q2931AFRejectUnknowns_Type()
)
q2931AFRejectUnknowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931AFRejectUnknowns.setStatus("current")
_Q2931AFLookupTable_Object = MibTable
q2931AFLookupTable = _Q2931AFLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 5)
)
if mibBuilder.loadTexts:
    q2931AFLookupTable.setStatus("current")
_Q2931AFLookupEntry_Object = MibTableRow
q2931AFLookupEntry = _Q2931AFLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 5, 1)
)
q2931AFLookupEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "q2931AFLookupIndex"),
)
if mibBuilder.loadTexts:
    q2931AFLookupEntry.setStatus("current")
_Q2931AFLookupIndex_Type = Integer32
_Q2931AFLookupIndex_Object = MibTableColumn
q2931AFLookupIndex = _Q2931AFLookupIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 5, 1, 1),
    _Q2931AFLookupIndex_Type()
)
q2931AFLookupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    q2931AFLookupIndex.setStatus("current")
_Q2931AFLookupNSAPFilterIndex_Type = Integer32
_Q2931AFLookupNSAPFilterIndex_Object = MibTableColumn
q2931AFLookupNSAPFilterIndex = _Q2931AFLookupNSAPFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 5, 1, 2),
    _Q2931AFLookupNSAPFilterIndex_Type()
)
q2931AFLookupNSAPFilterIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931AFLookupNSAPFilterIndex.setStatus("current")
_Q2931AFLookupSrcPort_Type = Integer32
_Q2931AFLookupSrcPort_Object = MibTableColumn
q2931AFLookupSrcPort = _Q2931AFLookupSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 5, 1, 3),
    _Q2931AFLookupSrcPort_Type()
)
q2931AFLookupSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931AFLookupSrcPort.setStatus("current")
_Q2931AFLookupSrcVPI_Type = Integer32
_Q2931AFLookupSrcVPI_Object = MibTableColumn
q2931AFLookupSrcVPI = _Q2931AFLookupSrcVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 5, 1, 4),
    _Q2931AFLookupSrcVPI_Type()
)
q2931AFLookupSrcVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931AFLookupSrcVPI.setStatus("current")
_Q2931AFLookupSrcNsap_Type = NsapAddr
_Q2931AFLookupSrcNsap_Object = MibTableColumn
q2931AFLookupSrcNsap = _Q2931AFLookupSrcNsap_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 5, 1, 5),
    _Q2931AFLookupSrcNsap_Type()
)
q2931AFLookupSrcNsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931AFLookupSrcNsap.setStatus("current")
_Q2931AFLookupDstPort_Type = Integer32
_Q2931AFLookupDstPort_Object = MibTableColumn
q2931AFLookupDstPort = _Q2931AFLookupDstPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 5, 1, 6),
    _Q2931AFLookupDstPort_Type()
)
q2931AFLookupDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931AFLookupDstPort.setStatus("current")
_Q2931AFLookupDstVPI_Type = Integer32
_Q2931AFLookupDstVPI_Object = MibTableColumn
q2931AFLookupDstVPI = _Q2931AFLookupDstVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 5, 1, 7),
    _Q2931AFLookupDstVPI_Type()
)
q2931AFLookupDstVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931AFLookupDstVPI.setStatus("current")
_Q2931AFLookupDstNsap_Type = NsapAddr
_Q2931AFLookupDstNsap_Object = MibTableColumn
q2931AFLookupDstNsap = _Q2931AFLookupDstNsap_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 5, 1, 8),
    _Q2931AFLookupDstNsap_Type()
)
q2931AFLookupDstNsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931AFLookupDstNsap.setStatus("current")


class _Q2931AFLookupResult_Type(Integer32):
    """Custom type q2931AFLookupResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2))
    )


_Q2931AFLookupResult_Type.__name__ = "Integer32"
_Q2931AFLookupResult_Object = MibTableColumn
q2931AFLookupResult = _Q2931AFLookupResult_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 5, 1, 9),
    _Q2931AFLookupResult_Type()
)
q2931AFLookupResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931AFLookupResult.setStatus("current")
_Q2931AFLookupTemplate_Type = Integer32
_Q2931AFLookupTemplate_Object = MibTableColumn
q2931AFLookupTemplate = _Q2931AFLookupTemplate_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 5, 1, 10),
    _Q2931AFLookupTemplate_Type()
)
q2931AFLookupTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931AFLookupTemplate.setStatus("current")
_Q2931AFLookupStatus_Type = RowStatus
_Q2931AFLookupStatus_Object = MibTableColumn
q2931AFLookupStatus = _Q2931AFLookupStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 5, 1, 11),
    _Q2931AFLookupStatus_Type()
)
q2931AFLookupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931AFLookupStatus.setStatus("current")
_Q2931AFLastFailureGroup_ObjectIdentity = ObjectIdentity
q2931AFLastFailureGroup = _Q2931AFLastFailureGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 6)
)
_Q2931AFLastFailureSrcPort_Type = Integer32
_Q2931AFLastFailureSrcPort_Object = MibScalar
q2931AFLastFailureSrcPort = _Q2931AFLastFailureSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 6, 1),
    _Q2931AFLastFailureSrcPort_Type()
)
q2931AFLastFailureSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931AFLastFailureSrcPort.setStatus("current")
_Q2931AFLastFailureSrcVPI_Type = Integer32
_Q2931AFLastFailureSrcVPI_Object = MibScalar
q2931AFLastFailureSrcVPI = _Q2931AFLastFailureSrcVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 6, 2),
    _Q2931AFLastFailureSrcVPI_Type()
)
q2931AFLastFailureSrcVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931AFLastFailureSrcVPI.setStatus("current")
_Q2931AFLastFailureSrcNsap_Type = NsapAddr
_Q2931AFLastFailureSrcNsap_Object = MibScalar
q2931AFLastFailureSrcNsap = _Q2931AFLastFailureSrcNsap_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 6, 3),
    _Q2931AFLastFailureSrcNsap_Type()
)
q2931AFLastFailureSrcNsap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931AFLastFailureSrcNsap.setStatus("current")
_Q2931AFLastFailureDstPort_Type = Integer32
_Q2931AFLastFailureDstPort_Object = MibScalar
q2931AFLastFailureDstPort = _Q2931AFLastFailureDstPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 6, 4),
    _Q2931AFLastFailureDstPort_Type()
)
q2931AFLastFailureDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931AFLastFailureDstPort.setStatus("current")
_Q2931AFLastFailureDstVPI_Type = Integer32
_Q2931AFLastFailureDstVPI_Object = MibScalar
q2931AFLastFailureDstVPI = _Q2931AFLastFailureDstVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 6, 5),
    _Q2931AFLastFailureDstVPI_Type()
)
q2931AFLastFailureDstVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931AFLastFailureDstVPI.setStatus("current")
_Q2931AFLastFailureDstNsap_Type = NsapAddr
_Q2931AFLastFailureDstNsap_Object = MibScalar
q2931AFLastFailureDstNsap = _Q2931AFLastFailureDstNsap_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 6, 6),
    _Q2931AFLastFailureDstNsap_Type()
)
q2931AFLastFailureDstNsap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931AFLastFailureDstNsap.setStatus("current")
_Q2931AFLastFailureTemplateIndex_Type = Integer32
_Q2931AFLastFailureTemplateIndex_Object = MibScalar
q2931AFLastFailureTemplateIndex = _Q2931AFLastFailureTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 6, 7),
    _Q2931AFLastFailureTemplateIndex_Type()
)
q2931AFLastFailureTemplateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931AFLastFailureTemplateIndex.setStatus("current")


class _Q2931AFLastFailureDirection_Type(Integer32):
    """Custom type q2931AFLastFailureDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2))
    )


_Q2931AFLastFailureDirection_Type.__name__ = "Integer32"
_Q2931AFLastFailureDirection_Object = MibScalar
q2931AFLastFailureDirection = _Q2931AFLastFailureDirection_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 6, 6, 8),
    _Q2931AFLastFailureDirection_Type()
)
q2931AFLastFailureDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931AFLastFailureDirection.setStatus("current")
_Q2931NSAPPingGroup_ObjectIdentity = ObjectIdentity
q2931NSAPPingGroup = _Q2931NSAPPingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 7)
)
_Q2931NPCallTable_Object = MibTable
q2931NPCallTable = _Q2931NPCallTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    q2931NPCallTable.setStatus("current")
_Q2931NPCallEntry_Object = MibTableRow
q2931NPCallEntry = _Q2931NPCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 7, 1, 1)
)
q2931NPCallEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "q2931NPCallIndex"),
)
if mibBuilder.loadTexts:
    q2931NPCallEntry.setStatus("current")
_Q2931NPCallIndex_Type = Integer32
_Q2931NPCallIndex_Object = MibTableColumn
q2931NPCallIndex = _Q2931NPCallIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 7, 1, 1, 1),
    _Q2931NPCallIndex_Type()
)
q2931NPCallIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    q2931NPCallIndex.setStatus("current")
_Q2931NPCallDstNsap_Type = NsapAddr
_Q2931NPCallDstNsap_Object = MibTableColumn
q2931NPCallDstNsap = _Q2931NPCallDstNsap_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 7, 1, 1, 2),
    _Q2931NPCallDstNsap_Type()
)
q2931NPCallDstNsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931NPCallDstNsap.setStatus("current")


class _Q2931NPCallState_Type(Integer32):
    """Custom type q2931NPCallState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("err", 4),
          ("inprogress", 2),
          ("lochost", 6),
          ("locpref", 5),
          ("up", 3))
    )


_Q2931NPCallState_Type.__name__ = "Integer32"
_Q2931NPCallState_Object = MibTableColumn
q2931NPCallState = _Q2931NPCallState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 7, 1, 1, 3),
    _Q2931NPCallState_Type()
)
q2931NPCallState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931NPCallState.setStatus("current")


class _Q2931NPCallClientType_Type(Integer32):
    """Custom type q2931NPCallClientType based on Integer32"""
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
        *(("bus", 4),
          ("lec", 3),
          ("lecs", 2),
          ("les", 5),
          ("noIndication", 1))
    )


_Q2931NPCallClientType_Type.__name__ = "Integer32"
_Q2931NPCallClientType_Object = MibTableColumn
q2931NPCallClientType = _Q2931NPCallClientType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 7, 1, 1, 4),
    _Q2931NPCallClientType_Type()
)
q2931NPCallClientType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931NPCallClientType.setStatus("current")
_Q2931NPCallFwdUpcKey_Type = Integer32
_Q2931NPCallFwdUpcKey_Object = MibTableColumn
q2931NPCallFwdUpcKey = _Q2931NPCallFwdUpcKey_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 7, 1, 1, 6),
    _Q2931NPCallFwdUpcKey_Type()
)
q2931NPCallFwdUpcKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931NPCallFwdUpcKey.setStatus("current")
_Q2931NPCallBckUpcKey_Type = Integer32
_Q2931NPCallBckUpcKey_Object = MibTableColumn
q2931NPCallBckUpcKey = _Q2931NPCallBckUpcKey_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 7, 1, 1, 7),
    _Q2931NPCallBckUpcKey_Type()
)
q2931NPCallBckUpcKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931NPCallBckUpcKey.setStatus("current")
_Q2931NPCallCallingDomain_Type = Integer32
_Q2931NPCallCallingDomain_Object = MibTableColumn
q2931NPCallCallingDomain = _Q2931NPCallCallingDomain_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 7, 1, 1, 8),
    _Q2931NPCallCallingDomain_Type()
)
q2931NPCallCallingDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931NPCallCallingDomain.setStatus("current")
_Q2931NPCallQosIndex_Type = Integer32
_Q2931NPCallQosIndex_Object = MibTableColumn
q2931NPCallQosIndex = _Q2931NPCallQosIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 7, 1, 1, 9),
    _Q2931NPCallQosIndex_Type()
)
q2931NPCallQosIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931NPCallQosIndex.setStatus("current")


class _Q2931NPCallQosClassFwd_Type(Integer32):
    """Custom type q2931NPCallQosClassFwd based on Integer32"""
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
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5))
    )


_Q2931NPCallQosClassFwd_Type.__name__ = "Integer32"
_Q2931NPCallQosClassFwd_Object = MibTableColumn
q2931NPCallQosClassFwd = _Q2931NPCallQosClassFwd_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 7, 1, 1, 10),
    _Q2931NPCallQosClassFwd_Type()
)
q2931NPCallQosClassFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931NPCallQosClassFwd.setStatus("current")


class _Q2931NPCallQosClassBwd_Type(Integer32):
    """Custom type q2931NPCallQosClassBwd based on Integer32"""
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
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5))
    )


_Q2931NPCallQosClassBwd_Type.__name__ = "Integer32"
_Q2931NPCallQosClassBwd_Object = MibTableColumn
q2931NPCallQosClassBwd = _Q2931NPCallQosClassBwd_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 7, 1, 1, 11),
    _Q2931NPCallQosClassBwd_Type()
)
q2931NPCallQosClassBwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931NPCallQosClassBwd.setStatus("current")


class _Q2931NPCallBearerClass_Type(Integer32):
    """Custom type q2931NPCallBearerClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("classA", 1),
          ("classC", 2),
          ("classX", 3))
    )


_Q2931NPCallBearerClass_Type.__name__ = "Integer32"
_Q2931NPCallBearerClass_Object = MibTableColumn
q2931NPCallBearerClass = _Q2931NPCallBearerClass_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 7, 1, 1, 12),
    _Q2931NPCallBearerClass_Type()
)
q2931NPCallBearerClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931NPCallBearerClass.setStatus("current")


class _Q2931NPCallVerbose_Type(Integer32):
    """Custom type q2931NPCallVerbose based on Integer32"""
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


_Q2931NPCallVerbose_Type.__name__ = "Integer32"
_Q2931NPCallVerbose_Object = MibTableColumn
q2931NPCallVerbose = _Q2931NPCallVerbose_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 7, 1, 1, 13),
    _Q2931NPCallVerbose_Type()
)
q2931NPCallVerbose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931NPCallVerbose.setStatus("current")
_Q2931NPCallStatus_Type = RowStatus
_Q2931NPCallStatus_Object = MibTableColumn
q2931NPCallStatus = _Q2931NPCallStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 7, 1, 1, 14),
    _Q2931NPCallStatus_Type()
)
q2931NPCallStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931NPCallStatus.setStatus("current")


class _Q2931NPPingState_Type(Integer32):
    """Custom type q2931NPPingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("complete", 2),
          ("inprogress", 1),
          ("invalid", 0))
    )


_Q2931NPPingState_Type.__name__ = "Integer32"
_Q2931NPPingState_Object = MibTableColumn
q2931NPPingState = _Q2931NPPingState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 7, 1, 1, 15),
    _Q2931NPPingState_Type()
)
q2931NPPingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931NPPingState.setStatus("current")
_Q2931NPCallCauseCode_Type = Integer32
_Q2931NPCallCauseCode_Object = MibTableColumn
q2931NPCallCauseCode = _Q2931NPCallCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 7, 1, 1, 16),
    _Q2931NPCallCauseCode_Type()
)
q2931NPCallCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931NPCallCauseCode.setStatus("current")
_Q2931NPPingPktCount_Type = Integer32
_Q2931NPPingPktCount_Object = MibTableColumn
q2931NPPingPktCount = _Q2931NPPingPktCount_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 7, 1, 1, 17),
    _Q2931NPPingPktCount_Type()
)
q2931NPPingPktCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931NPPingPktCount.setStatus("current")
_Q2931NPPingStatsPktsSent_Type = Integer32
_Q2931NPPingStatsPktsSent_Object = MibTableColumn
q2931NPPingStatsPktsSent = _Q2931NPPingStatsPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 7, 1, 1, 18),
    _Q2931NPPingStatsPktsSent_Type()
)
q2931NPPingStatsPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931NPPingStatsPktsSent.setStatus("current")
_Q2931NPPingStatsPktsReceived_Type = Integer32
_Q2931NPPingStatsPktsReceived_Object = MibTableColumn
q2931NPPingStatsPktsReceived = _Q2931NPPingStatsPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 7, 1, 1, 19),
    _Q2931NPPingStatsPktsReceived_Type()
)
q2931NPPingStatsPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931NPPingStatsPktsReceived.setStatus("current")
_Q2931NPPingStatsAverageDelay_Type = Integer32
_Q2931NPPingStatsAverageDelay_Object = MibTableColumn
q2931NPPingStatsAverageDelay = _Q2931NPPingStatsAverageDelay_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 7, 1, 1, 20),
    _Q2931NPPingStatsAverageDelay_Type()
)
q2931NPPingStatsAverageDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931NPPingStatsAverageDelay.setStatus("current")


class _Q2931NPMeasureRoundTripDelay_Type(Integer32):
    """Custom type q2931NPMeasureRoundTripDelay based on Integer32"""
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


_Q2931NPMeasureRoundTripDelay_Type.__name__ = "Integer32"
_Q2931NPMeasureRoundTripDelay_Object = MibTableColumn
q2931NPMeasureRoundTripDelay = _Q2931NPMeasureRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 7, 1, 1, 21),
    _Q2931NPMeasureRoundTripDelay_Type()
)
q2931NPMeasureRoundTripDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931NPMeasureRoundTripDelay.setStatus("current")
_Q2931NPPingStatsMaximumDelay_Type = Integer32
_Q2931NPPingStatsMaximumDelay_Object = MibTableColumn
q2931NPPingStatsMaximumDelay = _Q2931NPPingStatsMaximumDelay_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 7, 1, 1, 22),
    _Q2931NPPingStatsMaximumDelay_Type()
)
q2931NPPingStatsMaximumDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931NPPingStatsMaximumDelay.setStatus("current")
_Q2931NPPingStatsMinimumDelay_Type = Integer32
_Q2931NPPingStatsMinimumDelay_Object = MibTableColumn
q2931NPPingStatsMinimumDelay = _Q2931NPPingStatsMinimumDelay_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 7, 1, 1, 23),
    _Q2931NPPingStatsMinimumDelay_Type()
)
q2931NPPingStatsMinimumDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931NPPingStatsMinimumDelay.setStatus("current")
_Q2931NPCallNextIndex_Type = TestAndIncr
_Q2931NPCallNextIndex_Object = MibScalar
q2931NPCallNextIndex = _Q2931NPCallNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 7, 2),
    _Q2931NPCallNextIndex_Type()
)
q2931NPCallNextIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    q2931NPCallNextIndex.setStatus("current")
_PerCallDbgFilterGroup_ObjectIdentity = ObjectIdentity
perCallDbgFilterGroup = _PerCallDbgFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 8)
)
_PerCallDbgFilterTable_Object = MibTable
perCallDbgFilterTable = _PerCallDbgFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    perCallDbgFilterTable.setStatus("current")
_PerCallDbgFilterEntry_Object = MibTableRow
perCallDbgFilterEntry = _PerCallDbgFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 8, 1, 1)
)
perCallDbgFilterEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "perCallDbgFilterIndex"),
)
if mibBuilder.loadTexts:
    perCallDbgFilterEntry.setStatus("current")
_PerCallDbgFilterIndex_Type = Integer32
_PerCallDbgFilterIndex_Object = MibTableColumn
perCallDbgFilterIndex = _PerCallDbgFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 8, 1, 1, 1),
    _PerCallDbgFilterIndex_Type()
)
perCallDbgFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    perCallDbgFilterIndex.setStatus("current")
_PerCallDbgFilterTemplateId_Type = Integer32
_PerCallDbgFilterTemplateId_Object = MibTableColumn
perCallDbgFilterTemplateId = _PerCallDbgFilterTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 8, 1, 1, 2),
    _PerCallDbgFilterTemplateId_Type()
)
perCallDbgFilterTemplateId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perCallDbgFilterTemplateId.setStatus("current")


class _PerCallDbgFilterName_Type(OctetString):
    """Custom type perCallDbgFilterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PerCallDbgFilterName_Type.__name__ = "OctetString"
_PerCallDbgFilterName_Object = MibTableColumn
perCallDbgFilterName = _PerCallDbgFilterName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 8, 1, 1, 3),
    _PerCallDbgFilterName_Type()
)
perCallDbgFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perCallDbgFilterName.setStatus("current")
_PerCallDbgFilterFlavor_Type = Integer32
_PerCallDbgFilterFlavor_Object = MibTableColumn
perCallDbgFilterFlavor = _PerCallDbgFilterFlavor_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 8, 1, 1, 4),
    _PerCallDbgFilterFlavor_Type()
)
perCallDbgFilterFlavor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perCallDbgFilterFlavor.setStatus("current")
_PerCallDbgFilterMatches_Type = Counter32
_PerCallDbgFilterMatches_Object = MibTableColumn
perCallDbgFilterMatches = _PerCallDbgFilterMatches_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 8, 1, 1, 5),
    _PerCallDbgFilterMatches_Type()
)
perCallDbgFilterMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perCallDbgFilterMatches.setStatus("current")
_PerCallDbgFilterRowStatus_Type = RowStatus
_PerCallDbgFilterRowStatus_Object = MibTableColumn
perCallDbgFilterRowStatus = _PerCallDbgFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 8, 1, 1, 6),
    _PerCallDbgFilterRowStatus_Type()
)
perCallDbgFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perCallDbgFilterRowStatus.setStatus("current")


class _PerCallDbgTransFlag_Type(Integer32):
    """Custom type perCallDbgTransFlag based on Integer32"""
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


_PerCallDbgTransFlag_Type.__name__ = "Integer32"
_PerCallDbgTransFlag_Object = MibScalar
perCallDbgTransFlag = _PerCallDbgTransFlag_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 1, 8, 2),
    _PerCallDbgTransFlag_Type()
)
perCallDbgTransFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perCallDbgTransFlag.setStatus("current")
_PnniSpvcSrcNumberOfSPVCs_Type = Integer32
_PnniSpvcSrcNumberOfSPVCs_Object = MibScalar
pnniSpvcSrcNumberOfSPVCs = _PnniSpvcSrcNumberOfSPVCs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 2),
    _PnniSpvcSrcNumberOfSPVCs_Type()
)
pnniSpvcSrcNumberOfSPVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcSrcNumberOfSPVCs.setStatus("current")
_PnniSpvcSrcTable_Object = MibTable
pnniSpvcSrcTable = _PnniSpvcSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3)
)
if mibBuilder.loadTexts:
    pnniSpvcSrcTable.setStatus("current")
_PnniSpvcSrcEntry_Object = MibTableRow
pnniSpvcSrcEntry = _PnniSpvcSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1)
)
pnniSpvcSrcEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "pnniSpvcSrcIndex"),
)
if mibBuilder.loadTexts:
    pnniSpvcSrcEntry.setStatus("current")
_PnniSpvcSrcIndex_Type = Integer32
_PnniSpvcSrcIndex_Object = MibTableColumn
pnniSpvcSrcIndex = _PnniSpvcSrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 1),
    _PnniSpvcSrcIndex_Type()
)
pnniSpvcSrcIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcIndex.setStatus("current")
_PnniSpvcSrcCallingPort_Type = Integer32
_PnniSpvcSrcCallingPort_Object = MibTableColumn
pnniSpvcSrcCallingPort = _PnniSpvcSrcCallingPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 2),
    _PnniSpvcSrcCallingPort_Type()
)
pnniSpvcSrcCallingPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcCallingPort.setStatus("current")
_PnniSpvcSrcCallingVPI_Type = Integer32
_PnniSpvcSrcCallingVPI_Object = MibTableColumn
pnniSpvcSrcCallingVPI = _PnniSpvcSrcCallingVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 3),
    _PnniSpvcSrcCallingVPI_Type()
)
pnniSpvcSrcCallingVPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcCallingVPI.setStatus("current")
_PnniSpvcSrcCallingVCI_Type = Integer32
_PnniSpvcSrcCallingVCI_Object = MibTableColumn
pnniSpvcSrcCallingVCI = _PnniSpvcSrcCallingVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 4),
    _PnniSpvcSrcCallingVCI_Type()
)
pnniSpvcSrcCallingVCI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcCallingVCI.setStatus("current")
_PnniSpvcSrcCalledAtmAddr_Type = NsapAddr
_PnniSpvcSrcCalledAtmAddr_Object = MibTableColumn
pnniSpvcSrcCalledAtmAddr = _PnniSpvcSrcCalledAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 5),
    _PnniSpvcSrcCalledAtmAddr_Type()
)
pnniSpvcSrcCalledAtmAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcCalledAtmAddr.setStatus("current")
_PnniSpvcSrcCalledPort_Type = Integer32
_PnniSpvcSrcCalledPort_Object = MibTableColumn
pnniSpvcSrcCalledPort = _PnniSpvcSrcCalledPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 6),
    _PnniSpvcSrcCalledPort_Type()
)
pnniSpvcSrcCalledPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcSrcCalledPort.setStatus("current")


class _PnniSpvcSrcCalledVPVCSel_Type(Integer32):
    """Custom type pnniSpvcSrcCalledVPVCSel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPref", 1),
          ("require", 2))
    )


_PnniSpvcSrcCalledVPVCSel_Type.__name__ = "Integer32"
_PnniSpvcSrcCalledVPVCSel_Object = MibTableColumn
pnniSpvcSrcCalledVPVCSel = _PnniSpvcSrcCalledVPVCSel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 7),
    _PnniSpvcSrcCalledVPVCSel_Type()
)
pnniSpvcSrcCalledVPVCSel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcCalledVPVCSel.setStatus("current")
_PnniSpvcSrcCalledVPI_Type = Integer32
_PnniSpvcSrcCalledVPI_Object = MibTableColumn
pnniSpvcSrcCalledVPI = _PnniSpvcSrcCalledVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 8),
    _PnniSpvcSrcCalledVPI_Type()
)
pnniSpvcSrcCalledVPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcCalledVPI.setStatus("current")
_PnniSpvcSrcCalledVCI_Type = Integer32
_PnniSpvcSrcCalledVCI_Object = MibTableColumn
pnniSpvcSrcCalledVCI = _PnniSpvcSrcCalledVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 9),
    _PnniSpvcSrcCalledVCI_Type()
)
pnniSpvcSrcCalledVCI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcCalledVCI.setStatus("current")
_PnniSpvcSrcCalledAssignedVPI_Type = Integer32
_PnniSpvcSrcCalledAssignedVPI_Object = MibTableColumn
pnniSpvcSrcCalledAssignedVPI = _PnniSpvcSrcCalledAssignedVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 10),
    _PnniSpvcSrcCalledAssignedVPI_Type()
)
pnniSpvcSrcCalledAssignedVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcSrcCalledAssignedVPI.setStatus("current")
_PnniSpvcSrcCalledAssignedVCI_Type = Integer32
_PnniSpvcSrcCalledAssignedVCI_Object = MibTableColumn
pnniSpvcSrcCalledAssignedVCI = _PnniSpvcSrcCalledAssignedVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 11),
    _PnniSpvcSrcCalledAssignedVCI_Type()
)
pnniSpvcSrcCalledAssignedVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcSrcCalledAssignedVCI.setStatus("current")
_PnniSpvcSrcFwdUpcKey_Type = Integer32
_PnniSpvcSrcFwdUpcKey_Object = MibTableColumn
pnniSpvcSrcFwdUpcKey = _PnniSpvcSrcFwdUpcKey_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 12),
    _PnniSpvcSrcFwdUpcKey_Type()
)
pnniSpvcSrcFwdUpcKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcFwdUpcKey.setStatus("current")
_PnniSpvcSrcBckUpcKey_Type = Integer32
_PnniSpvcSrcBckUpcKey_Object = MibTableColumn
pnniSpvcSrcBckUpcKey = _PnniSpvcSrcBckUpcKey_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 13),
    _PnniSpvcSrcBckUpcKey_Type()
)
pnniSpvcSrcBckUpcKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcBckUpcKey.setStatus("current")


class _PnniSpvcSrcBearerClass_Type(Integer32):
    """Custom type pnniSpvcSrcBearerClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("classA", 1),
          ("classC", 2),
          ("classX", 3))
    )


_PnniSpvcSrcBearerClass_Type.__name__ = "Integer32"
_PnniSpvcSrcBearerClass_Object = MibTableColumn
pnniSpvcSrcBearerClass = _PnniSpvcSrcBearerClass_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 14),
    _PnniSpvcSrcBearerClass_Type()
)
pnniSpvcSrcBearerClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcBearerClass.setStatus("current")


class _PnniSpvcSrcTrafficType_Type(Integer32):
    """Custom type pnniSpvcSrcTrafficType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 2),
          ("noIndication", 1),
          ("vbr", 3))
    )


_PnniSpvcSrcTrafficType_Type.__name__ = "Integer32"
_PnniSpvcSrcTrafficType_Object = MibTableColumn
pnniSpvcSrcTrafficType = _PnniSpvcSrcTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 15),
    _PnniSpvcSrcTrafficType_Type()
)
pnniSpvcSrcTrafficType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcTrafficType.setStatus("obsolete")


class _PnniSpvcSrcTimingReq_Type(Integer32):
    """Custom type pnniSpvcSrcTimingReq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("end2endNotReqd", 3),
          ("end2endRequired", 2),
          ("noIndication", 1))
    )


_PnniSpvcSrcTimingReq_Type.__name__ = "Integer32"
_PnniSpvcSrcTimingReq_Object = MibTableColumn
pnniSpvcSrcTimingReq = _PnniSpvcSrcTimingReq_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 16),
    _PnniSpvcSrcTimingReq_Type()
)
pnniSpvcSrcTimingReq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcTimingReq.setStatus("obsolete")


class _PnniSpvcSrcSusceptClip_Type(Integer32):
    """Custom type pnniSpvcSrcSusceptClip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PnniSpvcSrcSusceptClip_Type.__name__ = "Integer32"
_PnniSpvcSrcSusceptClip_Object = MibTableColumn
pnniSpvcSrcSusceptClip = _PnniSpvcSrcSusceptClip_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 17),
    _PnniSpvcSrcSusceptClip_Type()
)
pnniSpvcSrcSusceptClip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcSusceptClip.setStatus("current")


class _PnniSpvcSrcFwdQoSClass_Type(Integer32):
    """Custom type pnniSpvcSrcFwdQoSClass based on Integer32"""
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
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5))
    )


_PnniSpvcSrcFwdQoSClass_Type.__name__ = "Integer32"
_PnniSpvcSrcFwdQoSClass_Object = MibTableColumn
pnniSpvcSrcFwdQoSClass = _PnniSpvcSrcFwdQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 18),
    _PnniSpvcSrcFwdQoSClass_Type()
)
pnniSpvcSrcFwdQoSClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcFwdQoSClass.setStatus("current")


class _PnniSpvcSrcBckQoSClass_Type(Integer32):
    """Custom type pnniSpvcSrcBckQoSClass based on Integer32"""
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
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5))
    )


_PnniSpvcSrcBckQoSClass_Type.__name__ = "Integer32"
_PnniSpvcSrcBckQoSClass_Object = MibTableColumn
pnniSpvcSrcBckQoSClass = _PnniSpvcSrcBckQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 19),
    _PnniSpvcSrcBckQoSClass_Type()
)
pnniSpvcSrcBckQoSClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcBckQoSClass.setStatus("current")
_PnniSpvcSrcTransitNetSel_Type = TransitNetwork
_PnniSpvcSrcTransitNetSel_Object = MibTableColumn
pnniSpvcSrcTransitNetSel = _PnniSpvcSrcTransitNetSel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 20),
    _PnniSpvcSrcTransitNetSel_Type()
)
pnniSpvcSrcTransitNetSel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcSrcTransitNetSel.setStatus("current")
_PnniSpvcSrcLastFailCause_Type = DisplayString
_PnniSpvcSrcLastFailCause_Object = MibTableColumn
pnniSpvcSrcLastFailCause = _PnniSpvcSrcLastFailCause_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 21),
    _PnniSpvcSrcLastFailCause_Type()
)
pnniSpvcSrcLastFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcSrcLastFailCause.setStatus("current")
_PnniSpvcSrcRetryCount_Type = Integer32
_PnniSpvcSrcRetryCount_Object = MibTableColumn
pnniSpvcSrcRetryCount = _PnniSpvcSrcRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 22),
    _PnniSpvcSrcRetryCount_Type()
)
pnniSpvcSrcRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcSrcRetryCount.setStatus("current")
_PnniSpvcSrcLastChangeTime_Type = TimeTicks
_PnniSpvcSrcLastChangeTime_Object = MibTableColumn
pnniSpvcSrcLastChangeTime = _PnniSpvcSrcLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 23),
    _PnniSpvcSrcLastChangeTime_Type()
)
pnniSpvcSrcLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcSrcLastChangeTime.setStatus("current")


class _PnniSpvcSrcStatus_Type(Integer32):
    """Custom type pnniSpvcSrcStatus based on Integer32"""
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
          ("failed", 3),
          ("up", 1))
    )


_PnniSpvcSrcStatus_Type.__name__ = "Integer32"
_PnniSpvcSrcStatus_Object = MibTableColumn
pnniSpvcSrcStatus = _PnniSpvcSrcStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 24),
    _PnniSpvcSrcStatus_Type()
)
pnniSpvcSrcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcSrcStatus.setStatus("current")


class _PnniSpvcSrcName_Type(OctetString):
    """Custom type pnniSpvcSrcName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PnniSpvcSrcName_Type.__name__ = "OctetString"
_PnniSpvcSrcName_Object = MibTableColumn
pnniSpvcSrcName = _PnniSpvcSrcName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 25),
    _PnniSpvcSrcName_Type()
)
pnniSpvcSrcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcName.setStatus("current")
_PnniSpvcSrcEntryStatus_Type = EntryStatus
_PnniSpvcSrcEntryStatus_Object = MibTableColumn
pnniSpvcSrcEntryStatus = _PnniSpvcSrcEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 26),
    _PnniSpvcSrcEntryStatus_Type()
)
pnniSpvcSrcEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcEntryStatus.setStatus("current")
_PnniSpvcSrcRouteCost_Type = Integer32
_PnniSpvcSrcRouteCost_Object = MibTableColumn
pnniSpvcSrcRouteCost = _PnniSpvcSrcRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 27),
    _PnniSpvcSrcRouteCost_Type()
)
pnniSpvcSrcRouteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcSrcRouteCost.setStatus("current")
_PnniSpvcSrcDtlIndex_Type = Integer32
_PnniSpvcSrcDtlIndex_Object = MibTableColumn
pnniSpvcSrcDtlIndex = _PnniSpvcSrcDtlIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 28),
    _PnniSpvcSrcDtlIndex_Type()
)
pnniSpvcSrcDtlIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcDtlIndex.setStatus("obsolete")
_PnniSpvcSrcActiveDtlIndex_Type = Integer32
_PnniSpvcSrcActiveDtlIndex_Object = MibTableColumn
pnniSpvcSrcActiveDtlIndex = _PnniSpvcSrcActiveDtlIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 29),
    _PnniSpvcSrcActiveDtlIndex_Type()
)
pnniSpvcSrcActiveDtlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcSrcActiveDtlIndex.setStatus("current")


class _PnniSpvcSrcRerouteStatus_Type(Integer32):
    """Custom type pnniSpvcSrcRerouteStatus based on Integer32"""
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


_PnniSpvcSrcRerouteStatus_Type.__name__ = "Integer32"
_PnniSpvcSrcRerouteStatus_Object = MibTableColumn
pnniSpvcSrcRerouteStatus = _PnniSpvcSrcRerouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 30),
    _PnniSpvcSrcRerouteStatus_Type()
)
pnniSpvcSrcRerouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcRerouteStatus.setStatus("current")
_PnniSpvcSrcCallingDomain_Type = Integer32
_PnniSpvcSrcCallingDomain_Object = MibTableColumn
pnniSpvcSrcCallingDomain = _PnniSpvcSrcCallingDomain_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 31),
    _PnniSpvcSrcCallingDomain_Type()
)
pnniSpvcSrcCallingDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcCallingDomain.setStatus("current")
_PnniSpvcSrcQosIndex_Type = Integer32
_PnniSpvcSrcQosIndex_Object = MibTableColumn
pnniSpvcSrcQosIndex = _PnniSpvcSrcQosIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 32),
    _PnniSpvcSrcQosIndex_Type()
)
pnniSpvcSrcQosIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcQosIndex.setStatus("current")
_PnniSpvcSrcDtlIndex1_Type = Integer32
_PnniSpvcSrcDtlIndex1_Object = MibTableColumn
pnniSpvcSrcDtlIndex1 = _PnniSpvcSrcDtlIndex1_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 33),
    _PnniSpvcSrcDtlIndex1_Type()
)
pnniSpvcSrcDtlIndex1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcDtlIndex1.setStatus("obsolete")
_PnniSpvcSrcDtlIndex2_Type = Integer32
_PnniSpvcSrcDtlIndex2_Object = MibTableColumn
pnniSpvcSrcDtlIndex2 = _PnniSpvcSrcDtlIndex2_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 34),
    _PnniSpvcSrcDtlIndex2_Type()
)
pnniSpvcSrcDtlIndex2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcDtlIndex2.setStatus("obsolete")
_PnniSpvcSrcDtlIndex3_Type = Integer32
_PnniSpvcSrcDtlIndex3_Object = MibTableColumn
pnniSpvcSrcDtlIndex3 = _PnniSpvcSrcDtlIndex3_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 35),
    _PnniSpvcSrcDtlIndex3_Type()
)
pnniSpvcSrcDtlIndex3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcDtlIndex3.setStatus("obsolete")
_PnniSpvcSrcDtlIndex4_Type = Integer32
_PnniSpvcSrcDtlIndex4_Object = MibTableColumn
pnniSpvcSrcDtlIndex4 = _PnniSpvcSrcDtlIndex4_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 36),
    _PnniSpvcSrcDtlIndex4_Type()
)
pnniSpvcSrcDtlIndex4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcDtlIndex4.setStatus("obsolete")


class _PnniSpvcSrcDtlWeight1_Type(Integer32):
    """Custom type pnniSpvcSrcDtlWeight1 based on Integer32"""
    defaultValue = 0


_PnniSpvcSrcDtlWeight1_Object = MibTableColumn
pnniSpvcSrcDtlWeight1 = _PnniSpvcSrcDtlWeight1_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 37),
    _PnniSpvcSrcDtlWeight1_Type()
)
pnniSpvcSrcDtlWeight1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcDtlWeight1.setStatus("obsolete")


class _PnniSpvcSrcDtlWeight2_Type(Integer32):
    """Custom type pnniSpvcSrcDtlWeight2 based on Integer32"""
    defaultValue = 0


_PnniSpvcSrcDtlWeight2_Object = MibTableColumn
pnniSpvcSrcDtlWeight2 = _PnniSpvcSrcDtlWeight2_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 38),
    _PnniSpvcSrcDtlWeight2_Type()
)
pnniSpvcSrcDtlWeight2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcDtlWeight2.setStatus("obsolete")


class _PnniSpvcSrcDtlWeight3_Type(Integer32):
    """Custom type pnniSpvcSrcDtlWeight3 based on Integer32"""
    defaultValue = 0


_PnniSpvcSrcDtlWeight3_Object = MibTableColumn
pnniSpvcSrcDtlWeight3 = _PnniSpvcSrcDtlWeight3_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 39),
    _PnniSpvcSrcDtlWeight3_Type()
)
pnniSpvcSrcDtlWeight3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcDtlWeight3.setStatus("obsolete")


class _PnniSpvcSrcDtlWeight4_Type(Integer32):
    """Custom type pnniSpvcSrcDtlWeight4 based on Integer32"""
    defaultValue = 0


_PnniSpvcSrcDtlWeight4_Object = MibTableColumn
pnniSpvcSrcDtlWeight4 = _PnniSpvcSrcDtlWeight4_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 40),
    _PnniSpvcSrcDtlWeight4_Type()
)
pnniSpvcSrcDtlWeight4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcDtlWeight4.setStatus("obsolete")


class _PnniSpvcSrcBackoffStatus_Type(Integer32):
    """Custom type pnniSpvcSrcBackoffStatus based on Integer32"""
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


_PnniSpvcSrcBackoffStatus_Type.__name__ = "Integer32"
_PnniSpvcSrcBackoffStatus_Object = MibTableColumn
pnniSpvcSrcBackoffStatus = _PnniSpvcSrcBackoffStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 41),
    _PnniSpvcSrcBackoffStatus_Type()
)
pnniSpvcSrcBackoffStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcBackoffStatus.setStatus("current")
_PnniSpvcSrcPriority_Type = Integer32
_PnniSpvcSrcPriority_Object = MibTableColumn
pnniSpvcSrcPriority = _PnniSpvcSrcPriority_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 42),
    _PnniSpvcSrcPriority_Type()
)
pnniSpvcSrcPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcPriority.setStatus("current")
_PnniSpvcSrcLastLocation_Type = DisplayString
_PnniSpvcSrcLastLocation_Object = MibTableColumn
pnniSpvcSrcLastLocation = _PnniSpvcSrcLastLocation_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 43),
    _PnniSpvcSrcLastLocation_Type()
)
pnniSpvcSrcLastLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcSrcLastLocation.setStatus("current")
_PnniSpvcSrcOldRouteCost_Type = Integer32
_PnniSpvcSrcOldRouteCost_Object = MibTableColumn
pnniSpvcSrcOldRouteCost = _PnniSpvcSrcOldRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 44),
    _PnniSpvcSrcOldRouteCost_Type()
)
pnniSpvcSrcOldRouteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcSrcOldRouteCost.setStatus("current")


class _PnniSpvcSrcDownReason_Type(Integer32):
    """Custom type pnniSpvcSrcDownReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deletion", 3),
          ("failure", 2),
          ("reroute", 1))
    )


_PnniSpvcSrcDownReason_Type.__name__ = "Integer32"
_PnniSpvcSrcDownReason_Object = MibTableColumn
pnniSpvcSrcDownReason = _PnniSpvcSrcDownReason_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 45),
    _PnniSpvcSrcDownReason_Type()
)
pnniSpvcSrcDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcSrcDownReason.setStatus("current")
_PnniSpvcSrcActiveDtlNodeIndex_Type = Integer32
_PnniSpvcSrcActiveDtlNodeIndex_Object = MibTableColumn
pnniSpvcSrcActiveDtlNodeIndex = _PnniSpvcSrcActiveDtlNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 46),
    _PnniSpvcSrcActiveDtlNodeIndex_Type()
)
pnniSpvcSrcActiveDtlNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcSrcActiveDtlNodeIndex.setStatus("current")
_PnniSpvcSrcDtlTag_Type = Integer32
_PnniSpvcSrcDtlTag_Object = MibTableColumn
pnniSpvcSrcDtlTag = _PnniSpvcSrcDtlTag_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 47),
    _PnniSpvcSrcDtlTag_Type()
)
pnniSpvcSrcDtlTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcDtlTag.setStatus("current")


class _PnniSpvcSrcAutoDtlStatus_Type(Integer32):
    """Custom type pnniSpvcSrcAutoDtlStatus based on Integer32"""
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


_PnniSpvcSrcAutoDtlStatus_Type.__name__ = "Integer32"
_PnniSpvcSrcAutoDtlStatus_Object = MibTableColumn
pnniSpvcSrcAutoDtlStatus = _PnniSpvcSrcAutoDtlStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 48),
    _PnniSpvcSrcAutoDtlStatus_Type()
)
pnniSpvcSrcAutoDtlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcAutoDtlStatus.setStatus("current")


class _PnniSpvcSrcRGroupIndex_Type(Integer32):
    """Custom type pnniSpvcSrcRGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PnniSpvcSrcRGroupIndex_Type.__name__ = "Integer32"
_PnniSpvcSrcRGroupIndex_Object = MibTableColumn
pnniSpvcSrcRGroupIndex = _PnniSpvcSrcRGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 49),
    _PnniSpvcSrcRGroupIndex_Type()
)
pnniSpvcSrcRGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcRGroupIndex.setStatus("current")
_PnniSpvcSrcSecondaryVPI_Type = Integer32
_PnniSpvcSrcSecondaryVPI_Object = MibTableColumn
pnniSpvcSrcSecondaryVPI = _PnniSpvcSrcSecondaryVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 50),
    _PnniSpvcSrcSecondaryVPI_Type()
)
pnniSpvcSrcSecondaryVPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcSecondaryVPI.setStatus("current")
_PnniSpvcSrcSecondaryVCI_Type = Integer32
_PnniSpvcSrcSecondaryVCI_Object = MibTableColumn
pnniSpvcSrcSecondaryVCI = _PnniSpvcSrcSecondaryVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 3, 1, 51),
    _PnniSpvcSrcSecondaryVCI_Type()
)
pnniSpvcSrcSecondaryVCI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvcSrcSecondaryVCI.setStatus("current")
_PnniSpvcDestNumberOfSPVCs_Type = Integer32
_PnniSpvcDestNumberOfSPVCs_Object = MibScalar
pnniSpvcDestNumberOfSPVCs = _PnniSpvcDestNumberOfSPVCs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 4),
    _PnniSpvcDestNumberOfSPVCs_Type()
)
pnniSpvcDestNumberOfSPVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcDestNumberOfSPVCs.setStatus("current")
_PnniSpvcDestTable_Object = MibTable
pnniSpvcDestTable = _PnniSpvcDestTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 5)
)
if mibBuilder.loadTexts:
    pnniSpvcDestTable.setStatus("current")
_PnniSpvcDestEntry_Object = MibTableRow
pnniSpvcDestEntry = _PnniSpvcDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 5, 1)
)
pnniSpvcDestEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "pnniSpvcDestIndex"),
)
if mibBuilder.loadTexts:
    pnniSpvcDestEntry.setStatus("current")
_PnniSpvcDestIndex_Type = Integer32
_PnniSpvcDestIndex_Object = MibTableColumn
pnniSpvcDestIndex = _PnniSpvcDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 5, 1, 1),
    _PnniSpvcDestIndex_Type()
)
pnniSpvcDestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcDestIndex.setStatus("current")
_PnniSpvcDestCallingAtmAddr_Type = NsapAddr
_PnniSpvcDestCallingAtmAddr_Object = MibTableColumn
pnniSpvcDestCallingAtmAddr = _PnniSpvcDestCallingAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 5, 1, 2),
    _PnniSpvcDestCallingAtmAddr_Type()
)
pnniSpvcDestCallingAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcDestCallingAtmAddr.setStatus("current")
_PnniSpvcDestCallingPort_Type = Integer32
_PnniSpvcDestCallingPort_Object = MibTableColumn
pnniSpvcDestCallingPort = _PnniSpvcDestCallingPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 5, 1, 3),
    _PnniSpvcDestCallingPort_Type()
)
pnniSpvcDestCallingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcDestCallingPort.setStatus("current")
_PnniSpvcDestCallingVPI_Type = Integer32
_PnniSpvcDestCallingVPI_Object = MibTableColumn
pnniSpvcDestCallingVPI = _PnniSpvcDestCallingVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 5, 1, 4),
    _PnniSpvcDestCallingVPI_Type()
)
pnniSpvcDestCallingVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcDestCallingVPI.setStatus("current")
_PnniSpvcDestCallingVCI_Type = Integer32
_PnniSpvcDestCallingVCI_Object = MibTableColumn
pnniSpvcDestCallingVCI = _PnniSpvcDestCallingVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 5, 1, 5),
    _PnniSpvcDestCallingVCI_Type()
)
pnniSpvcDestCallingVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcDestCallingVCI.setStatus("current")
_PnniSpvcDestCalledAtmAddr_Type = NsapAddr
_PnniSpvcDestCalledAtmAddr_Object = MibTableColumn
pnniSpvcDestCalledAtmAddr = _PnniSpvcDestCalledAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 5, 1, 6),
    _PnniSpvcDestCalledAtmAddr_Type()
)
pnniSpvcDestCalledAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcDestCalledAtmAddr.setStatus("current")
_PnniSpvcDestCalledPort_Type = Integer32
_PnniSpvcDestCalledPort_Object = MibTableColumn
pnniSpvcDestCalledPort = _PnniSpvcDestCalledPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 5, 1, 7),
    _PnniSpvcDestCalledPort_Type()
)
pnniSpvcDestCalledPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcDestCalledPort.setStatus("current")
_PnniSpvcDestAssignedVPI_Type = Integer32
_PnniSpvcDestAssignedVPI_Object = MibTableColumn
pnniSpvcDestAssignedVPI = _PnniSpvcDestAssignedVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 5, 1, 8),
    _PnniSpvcDestAssignedVPI_Type()
)
pnniSpvcDestAssignedVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcDestAssignedVPI.setStatus("current")
_PnniSpvcDestAssignedVCI_Type = Integer32
_PnniSpvcDestAssignedVCI_Object = MibTableColumn
pnniSpvcDestAssignedVCI = _PnniSpvcDestAssignedVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 5, 1, 9),
    _PnniSpvcDestAssignedVCI_Type()
)
pnniSpvcDestAssignedVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcDestAssignedVCI.setStatus("current")


class _PnniSpvcDestBearerClass_Type(Integer32):
    """Custom type pnniSpvcDestBearerClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("classA", 1),
          ("classC", 2),
          ("classX", 3))
    )


_PnniSpvcDestBearerClass_Type.__name__ = "Integer32"
_PnniSpvcDestBearerClass_Object = MibTableColumn
pnniSpvcDestBearerClass = _PnniSpvcDestBearerClass_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 5, 1, 10),
    _PnniSpvcDestBearerClass_Type()
)
pnniSpvcDestBearerClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcDestBearerClass.setStatus("current")


class _PnniSpvcDestTrafficType_Type(Integer32):
    """Custom type pnniSpvcDestTrafficType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 2),
          ("noIndication", 1),
          ("vbr", 3))
    )


_PnniSpvcDestTrafficType_Type.__name__ = "Integer32"
_PnniSpvcDestTrafficType_Object = MibTableColumn
pnniSpvcDestTrafficType = _PnniSpvcDestTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 5, 1, 11),
    _PnniSpvcDestTrafficType_Type()
)
pnniSpvcDestTrafficType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcDestTrafficType.setStatus("deprecated")


class _PnniSpvcDestTimingReq_Type(Integer32):
    """Custom type pnniSpvcDestTimingReq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("end2endNotReqd", 3),
          ("end2endRequired", 2),
          ("noIndication", 1))
    )


_PnniSpvcDestTimingReq_Type.__name__ = "Integer32"
_PnniSpvcDestTimingReq_Object = MibTableColumn
pnniSpvcDestTimingReq = _PnniSpvcDestTimingReq_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 5, 1, 12),
    _PnniSpvcDestTimingReq_Type()
)
pnniSpvcDestTimingReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcDestTimingReq.setStatus("deprecated")


class _PnniSpvcDestSusceptClip_Type(Integer32):
    """Custom type pnniSpvcDestSusceptClip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PnniSpvcDestSusceptClip_Type.__name__ = "Integer32"
_PnniSpvcDestSusceptClip_Object = MibTableColumn
pnniSpvcDestSusceptClip = _PnniSpvcDestSusceptClip_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 5, 1, 13),
    _PnniSpvcDestSusceptClip_Type()
)
pnniSpvcDestSusceptClip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcDestSusceptClip.setStatus("current")
_PnniSpvcDestUpTime_Type = TimeTicks
_PnniSpvcDestUpTime_Object = MibTableColumn
pnniSpvcDestUpTime = _PnniSpvcDestUpTime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 5, 1, 14),
    _PnniSpvcDestUpTime_Type()
)
pnniSpvcDestUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcDestUpTime.setStatus("current")


class _PnniSpvcDestFwdQoSClass_Type(Integer32):
    """Custom type pnniSpvcDestFwdQoSClass based on Integer32"""
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
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5))
    )


_PnniSpvcDestFwdQoSClass_Type.__name__ = "Integer32"
_PnniSpvcDestFwdQoSClass_Object = MibTableColumn
pnniSpvcDestFwdQoSClass = _PnniSpvcDestFwdQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 5, 1, 15),
    _PnniSpvcDestFwdQoSClass_Type()
)
pnniSpvcDestFwdQoSClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcDestFwdQoSClass.setStatus("current")


class _PnniSpvcDestBckQoSClass_Type(Integer32):
    """Custom type pnniSpvcDestBckQoSClass based on Integer32"""
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
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5))
    )


_PnniSpvcDestBckQoSClass_Type.__name__ = "Integer32"
_PnniSpvcDestBckQoSClass_Object = MibTableColumn
pnniSpvcDestBckQoSClass = _PnniSpvcDestBckQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 5, 1, 16),
    _PnniSpvcDestBckQoSClass_Type()
)
pnniSpvcDestBckQoSClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcDestBckQoSClass.setStatus("current")
_PnniSpvcDestTransitNetSel_Type = TransitNetwork
_PnniSpvcDestTransitNetSel_Object = MibTableColumn
pnniSpvcDestTransitNetSel = _PnniSpvcDestTransitNetSel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 5, 1, 17),
    _PnniSpvcDestTransitNetSel_Type()
)
pnniSpvcDestTransitNetSel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcDestTransitNetSel.setStatus("current")


class _PnniSpvcDestStatus_Type(Integer32):
    """Custom type pnniSpvcDestStatus based on Integer32"""
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
          ("failed", 3),
          ("up", 1))
    )


_PnniSpvcDestStatus_Type.__name__ = "Integer32"
_PnniSpvcDestStatus_Object = MibTableColumn
pnniSpvcDestStatus = _PnniSpvcDestStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 5, 1, 18),
    _PnniSpvcDestStatus_Type()
)
pnniSpvcDestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcDestStatus.setStatus("current")


class _PnniSpvcDestRGroupIndex_Type(Integer32):
    """Custom type pnniSpvcDestRGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PnniSpvcDestRGroupIndex_Type.__name__ = "Integer32"
_PnniSpvcDestRGroupIndex_Object = MibTableColumn
pnniSpvcDestRGroupIndex = _PnniSpvcDestRGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 5, 1, 19),
    _PnniSpvcDestRGroupIndex_Type()
)
pnniSpvcDestRGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvcDestRGroupIndex.setStatus("current")
_Q2931PublicGroup_ObjectIdentity = ObjectIdentity
q2931PublicGroup = _Q2931PublicGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 6)
)
_Q2931E164AddrResTable_Object = MibTable
q2931E164AddrResTable = _Q2931E164AddrResTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 6, 1)
)
if mibBuilder.loadTexts:
    q2931E164AddrResTable.setStatus("current")
_Q2931E164AddrResEntry_Object = MibTableRow
q2931E164AddrResEntry = _Q2931E164AddrResEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 6, 1, 1)
)
q2931E164AddrResEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "q2931E164Port"),
    (0, "Fore-Switch-MIB", "q2931E164VPI"),
    (0, "Fore-Switch-MIB", "q2931E164Nsap"),
    (0, "Fore-Switch-MIB", "q2931E164NsapMask"),
)
if mibBuilder.loadTexts:
    q2931E164AddrResEntry.setStatus("current")
_Q2931E164Port_Type = Integer32
_Q2931E164Port_Object = MibTableColumn
q2931E164Port = _Q2931E164Port_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 6, 1, 1, 1),
    _Q2931E164Port_Type()
)
q2931E164Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931E164Port.setStatus("current")
_Q2931E164VPI_Type = Integer32
_Q2931E164VPI_Object = MibTableColumn
q2931E164VPI = _Q2931E164VPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 6, 1, 1, 2),
    _Q2931E164VPI_Type()
)
q2931E164VPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931E164VPI.setStatus("current")
_Q2931E164Nsap_Type = NsapAddr
_Q2931E164Nsap_Object = MibTableColumn
q2931E164Nsap = _Q2931E164Nsap_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 6, 1, 1, 3),
    _Q2931E164Nsap_Type()
)
q2931E164Nsap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931E164Nsap.setStatus("current")
_Q2931E164NsapMask_Type = Integer32
_Q2931E164NsapMask_Object = MibTableColumn
q2931E164NsapMask = _Q2931E164NsapMask_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 6, 1, 1, 4),
    _Q2931E164NsapMask_Type()
)
q2931E164NsapMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q2931E164NsapMask.setStatus("current")
_Q2931E164Address_Type = E164Address
_Q2931E164Address_Object = MibTableColumn
q2931E164Address = _Q2931E164Address_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 6, 1, 1, 5),
    _Q2931E164Address_Type()
)
q2931E164Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931E164Address.setStatus("current")
_Q2931E164AddrResStatus_Type = EntryStatus
_Q2931E164AddrResStatus_Object = MibTableColumn
q2931E164AddrResStatus = _Q2931E164AddrResStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 6, 1, 1, 6),
    _Q2931E164AddrResStatus_Type()
)
q2931E164AddrResStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    q2931E164AddrResStatus.setStatus("current")
_PnniSpvcParamGroup_ObjectIdentity = ObjectIdentity
pnniSpvcParamGroup = _PnniSpvcParamGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 7)
)


class _PnniSpvcPaceInterval_Type(TimeInterval):
    """Custom type pnniSpvcPaceInterval based on TimeInterval"""
    defaultValue = 200


_PnniSpvcPaceInterval_Object = MibScalar
pnniSpvcPaceInterval = _PnniSpvcPaceInterval_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 7, 1),
    _PnniSpvcPaceInterval_Type()
)
pnniSpvcPaceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSpvcPaceInterval.setStatus("current")


class _PnniSpvcPaceNumSpvcs_Type(Integer32):
    """Custom type pnniSpvcPaceNumSpvcs based on Integer32"""
    defaultValue = 20


_PnniSpvcPaceNumSpvcs_Object = MibScalar
pnniSpvcPaceNumSpvcs = _PnniSpvcPaceNumSpvcs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 7, 2),
    _PnniSpvcPaceNumSpvcs_Type()
)
pnniSpvcPaceNumSpvcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSpvcPaceNumSpvcs.setStatus("current")


class _PnniSpvcRerouteInterval_Type(TimeInterval):
    """Custom type pnniSpvcRerouteInterval based on TimeInterval"""
    defaultValue = 1000


_PnniSpvcRerouteInterval_Object = MibScalar
pnniSpvcRerouteInterval = _PnniSpvcRerouteInterval_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 7, 3),
    _PnniSpvcRerouteInterval_Type()
)
pnniSpvcRerouteInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSpvcRerouteInterval.setStatus("current")


class _PnniSpvcRerouteNumSpvcs_Type(Integer32):
    """Custom type pnniSpvcRerouteNumSpvcs based on Integer32"""
    defaultValue = 20


_PnniSpvcRerouteNumSpvcs_Object = MibScalar
pnniSpvcRerouteNumSpvcs = _PnniSpvcRerouteNumSpvcs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 7, 4),
    _PnniSpvcRerouteNumSpvcs_Type()
)
pnniSpvcRerouteNumSpvcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSpvcRerouteNumSpvcs.setStatus("current")


class _PnniSpvcRerouteThreshold_Type(Integer32):
    """Custom type pnniSpvcRerouteThreshold based on Integer32"""
    defaultValue = 50


_PnniSpvcRerouteThreshold_Object = MibScalar
pnniSpvcRerouteThreshold = _PnniSpvcRerouteThreshold_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 7, 5),
    _PnniSpvcRerouteThreshold_Type()
)
pnniSpvcRerouteThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSpvcRerouteThreshold.setStatus("current")


class _PnniSpvcLowestPriority_Type(Integer32):
    """Custom type pnniSpvcLowestPriority based on Integer32"""
    defaultValue = 10


_PnniSpvcLowestPriority_Object = MibScalar
pnniSpvcLowestPriority = _PnniSpvcLowestPriority_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 7, 6),
    _PnniSpvcLowestPriority_Type()
)
pnniSpvcLowestPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSpvcLowestPriority.setStatus("current")


class _PnniSpvcDefaultUbrBandwidth_Type(Integer32):
    """Custom type pnniSpvcDefaultUbrBandwidth based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_PnniSpvcDefaultUbrBandwidth_Type.__name__ = "Integer32"
_PnniSpvcDefaultUbrBandwidth_Object = MibScalar
pnniSpvcDefaultUbrBandwidth = _PnniSpvcDefaultUbrBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 7, 7),
    _PnniSpvcDefaultUbrBandwidth_Type()
)
pnniSpvcDefaultUbrBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSpvcDefaultUbrBandwidth.setStatus("current")


class _PnniSpvcTrapMode_Type(Integer32):
    """Custom type pnniSpvcTrapMode based on Integer32"""
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
        *(("all", 3),
          ("failure", 2),
          ("none", 4),
          ("reroute", 1))
    )


_PnniSpvcTrapMode_Type.__name__ = "Integer32"
_PnniSpvcTrapMode_Object = MibScalar
pnniSpvcTrapMode = _PnniSpvcTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 7, 8),
    _PnniSpvcTrapMode_Type()
)
pnniSpvcTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSpvcTrapMode.setStatus("current")


class _PnniSpvcBackoffInterval_Type(TimeInterval):
    """Custom type pnniSpvcBackoffInterval based on TimeInterval"""
    defaultValue = 60000


_PnniSpvcBackoffInterval_Object = MibScalar
pnniSpvcBackoffInterval = _PnniSpvcBackoffInterval_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 7, 9),
    _PnniSpvcBackoffInterval_Type()
)
pnniSpvcBackoffInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSpvcBackoffInterval.setStatus("current")


class _PnniPmpSpvcPartyPaceNum_Type(Integer32):
    """Custom type pnniPmpSpvcPartyPaceNum based on Integer32"""
    defaultValue = 10


_PnniPmpSpvcPartyPaceNum_Object = MibScalar
pnniPmpSpvcPartyPaceNum = _PnniPmpSpvcPartyPaceNum_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 7, 10),
    _PnniPmpSpvcPartyPaceNum_Type()
)
pnniPmpSpvcPartyPaceNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniPmpSpvcPartyPaceNum.setStatus("current")
_PnniSpvpcParamGroup_ObjectIdentity = ObjectIdentity
pnniSpvpcParamGroup = _PnniSpvpcParamGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 8)
)


class _PnniSpvpcPaceInterval_Type(TimeInterval):
    """Custom type pnniSpvpcPaceInterval based on TimeInterval"""
    defaultValue = 200


_PnniSpvpcPaceInterval_Object = MibScalar
pnniSpvpcPaceInterval = _PnniSpvpcPaceInterval_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 8, 1),
    _PnniSpvpcPaceInterval_Type()
)
pnniSpvpcPaceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSpvpcPaceInterval.setStatus("current")


class _PnniSpvpcPaceNumSpvpcs_Type(Integer32):
    """Custom type pnniSpvpcPaceNumSpvpcs based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_PnniSpvpcPaceNumSpvpcs_Type.__name__ = "Integer32"
_PnniSpvpcPaceNumSpvpcs_Object = MibScalar
pnniSpvpcPaceNumSpvpcs = _PnniSpvpcPaceNumSpvpcs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 8, 2),
    _PnniSpvpcPaceNumSpvpcs_Type()
)
pnniSpvpcPaceNumSpvpcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSpvpcPaceNumSpvpcs.setStatus("current")


class _PnniSpvpcRerouteInterval_Type(TimeInterval):
    """Custom type pnniSpvpcRerouteInterval based on TimeInterval"""
    defaultValue = 1500


_PnniSpvpcRerouteInterval_Object = MibScalar
pnniSpvpcRerouteInterval = _PnniSpvpcRerouteInterval_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 8, 3),
    _PnniSpvpcRerouteInterval_Type()
)
pnniSpvpcRerouteInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSpvpcRerouteInterval.setStatus("current")


class _PnniSpvpcRerouteNumSpvpcs_Type(Integer32):
    """Custom type pnniSpvpcRerouteNumSpvpcs based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_PnniSpvpcRerouteNumSpvpcs_Type.__name__ = "Integer32"
_PnniSpvpcRerouteNumSpvpcs_Object = MibScalar
pnniSpvpcRerouteNumSpvpcs = _PnniSpvpcRerouteNumSpvpcs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 8, 4),
    _PnniSpvpcRerouteNumSpvpcs_Type()
)
pnniSpvpcRerouteNumSpvpcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSpvpcRerouteNumSpvpcs.setStatus("current")


class _PnniSpvpcRerouteThreshold_Type(Integer32):
    """Custom type pnniSpvpcRerouteThreshold based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PnniSpvpcRerouteThreshold_Type.__name__ = "Integer32"
_PnniSpvpcRerouteThreshold_Object = MibScalar
pnniSpvpcRerouteThreshold = _PnniSpvpcRerouteThreshold_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 8, 5),
    _PnniSpvpcRerouteThreshold_Type()
)
pnniSpvpcRerouteThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSpvpcRerouteThreshold.setStatus("current")


class _PnniSpvpcLowestPriority_Type(Integer32):
    """Custom type pnniSpvpcLowestPriority based on Integer32"""
    defaultValue = 10


_PnniSpvpcLowestPriority_Object = MibScalar
pnniSpvpcLowestPriority = _PnniSpvpcLowestPriority_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 8, 6),
    _PnniSpvpcLowestPriority_Type()
)
pnniSpvpcLowestPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSpvpcLowestPriority.setStatus("current")


class _PnniSpvpcTrapMode_Type(Integer32):
    """Custom type pnniSpvpcTrapMode based on Integer32"""
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
        *(("all", 3),
          ("failure", 2),
          ("none", 4),
          ("reroute", 1))
    )


_PnniSpvpcTrapMode_Type.__name__ = "Integer32"
_PnniSpvpcTrapMode_Object = MibScalar
pnniSpvpcTrapMode = _PnniSpvpcTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 8, 7),
    _PnniSpvpcTrapMode_Type()
)
pnniSpvpcTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSpvpcTrapMode.setStatus("current")


class _PnniSpvpcBackoffInterval_Type(TimeInterval):
    """Custom type pnniSpvpcBackoffInterval based on TimeInterval"""
    defaultValue = 60000


_PnniSpvpcBackoffInterval_Object = MibScalar
pnniSpvpcBackoffInterval = _PnniSpvpcBackoffInterval_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 8, 8),
    _PnniSpvpcBackoffInterval_Type()
)
pnniSpvpcBackoffInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSpvpcBackoffInterval.setStatus("current")
_PnniSpvpcSrcTable_Object = MibTable
pnniSpvpcSrcTable = _PnniSpvpcSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9)
)
if mibBuilder.loadTexts:
    pnniSpvpcSrcTable.setStatus("current")
_PnniSpvpcSrcEntry_Object = MibTableRow
pnniSpvpcSrcEntry = _PnniSpvpcSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1)
)
pnniSpvpcSrcEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "pnniSpvpcSrcIndex"),
)
if mibBuilder.loadTexts:
    pnniSpvpcSrcEntry.setStatus("current")


class _PnniSpvpcSrcIndex_Type(Integer32):
    """Custom type pnniSpvpcSrcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PnniSpvpcSrcIndex_Type.__name__ = "Integer32"
_PnniSpvpcSrcIndex_Object = MibTableColumn
pnniSpvpcSrcIndex = _PnniSpvpcSrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 1),
    _PnniSpvpcSrcIndex_Type()
)
pnniSpvpcSrcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniSpvpcSrcIndex.setStatus("current")


class _PnniSpvpcSrcCallingPort_Type(Integer32):
    """Custom type pnniSpvpcSrcCallingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1025),
    )


_PnniSpvpcSrcCallingPort_Type.__name__ = "Integer32"
_PnniSpvpcSrcCallingPort_Object = MibTableColumn
pnniSpvpcSrcCallingPort = _PnniSpvpcSrcCallingPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 2),
    _PnniSpvpcSrcCallingPort_Type()
)
pnniSpvpcSrcCallingPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvpcSrcCallingPort.setStatus("current")
_PnniSpvpcSrcCallingVPI_Type = Integer32
_PnniSpvpcSrcCallingVPI_Object = MibTableColumn
pnniSpvpcSrcCallingVPI = _PnniSpvpcSrcCallingVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 3),
    _PnniSpvpcSrcCallingVPI_Type()
)
pnniSpvpcSrcCallingVPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvpcSrcCallingVPI.setStatus("current")
_PnniSpvpcSrcCalledAtmAddr_Type = NsapAddr
_PnniSpvpcSrcCalledAtmAddr_Object = MibTableColumn
pnniSpvpcSrcCalledAtmAddr = _PnniSpvpcSrcCalledAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 4),
    _PnniSpvpcSrcCalledAtmAddr_Type()
)
pnniSpvpcSrcCalledAtmAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvpcSrcCalledAtmAddr.setStatus("current")
_PnniSpvpcSrcCalledPort_Type = Integer32
_PnniSpvpcSrcCalledPort_Object = MibTableColumn
pnniSpvpcSrcCalledPort = _PnniSpvpcSrcCalledPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 5),
    _PnniSpvpcSrcCalledPort_Type()
)
pnniSpvpcSrcCalledPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvpcSrcCalledPort.setStatus("current")


class _PnniSpvpcSrcCalledVPVCSel_Type(Integer32):
    """Custom type pnniSpvpcSrcCalledVPVCSel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPref", 1),
          ("require", 2))
    )


_PnniSpvpcSrcCalledVPVCSel_Type.__name__ = "Integer32"
_PnniSpvpcSrcCalledVPVCSel_Object = MibTableColumn
pnniSpvpcSrcCalledVPVCSel = _PnniSpvpcSrcCalledVPVCSel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 6),
    _PnniSpvpcSrcCalledVPVCSel_Type()
)
pnniSpvpcSrcCalledVPVCSel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvpcSrcCalledVPVCSel.setStatus("current")


class _PnniSpvpcSrcCalledVPI_Type(Integer32):
    """Custom type pnniSpvpcSrcCalledVPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_PnniSpvpcSrcCalledVPI_Type.__name__ = "Integer32"
_PnniSpvpcSrcCalledVPI_Object = MibTableColumn
pnniSpvpcSrcCalledVPI = _PnniSpvpcSrcCalledVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 7),
    _PnniSpvpcSrcCalledVPI_Type()
)
pnniSpvpcSrcCalledVPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvpcSrcCalledVPI.setStatus("current")


class _PnniSpvpcSrcCalledAssignedVPI_Type(Integer32):
    """Custom type pnniSpvpcSrcCalledAssignedVPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_PnniSpvpcSrcCalledAssignedVPI_Type.__name__ = "Integer32"
_PnniSpvpcSrcCalledAssignedVPI_Object = MibTableColumn
pnniSpvpcSrcCalledAssignedVPI = _PnniSpvpcSrcCalledAssignedVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 8),
    _PnniSpvpcSrcCalledAssignedVPI_Type()
)
pnniSpvpcSrcCalledAssignedVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvpcSrcCalledAssignedVPI.setStatus("current")


class _PnniSpvpcSrcFwdUpcKey_Type(Integer32):
    """Custom type pnniSpvpcSrcFwdUpcKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_PnniSpvpcSrcFwdUpcKey_Type.__name__ = "Integer32"
_PnniSpvpcSrcFwdUpcKey_Object = MibTableColumn
pnniSpvpcSrcFwdUpcKey = _PnniSpvpcSrcFwdUpcKey_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 9),
    _PnniSpvpcSrcFwdUpcKey_Type()
)
pnniSpvpcSrcFwdUpcKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvpcSrcFwdUpcKey.setStatus("current")


class _PnniSpvpcSrcBckUpcKey_Type(Integer32):
    """Custom type pnniSpvpcSrcBckUpcKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_PnniSpvpcSrcBckUpcKey_Type.__name__ = "Integer32"
_PnniSpvpcSrcBckUpcKey_Object = MibTableColumn
pnniSpvpcSrcBckUpcKey = _PnniSpvpcSrcBckUpcKey_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 10),
    _PnniSpvpcSrcBckUpcKey_Type()
)
pnniSpvpcSrcBckUpcKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvpcSrcBckUpcKey.setStatus("current")


class _PnniSpvpcSrcSusceptClip_Type(Integer32):
    """Custom type pnniSpvpcSrcSusceptClip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PnniSpvpcSrcSusceptClip_Type.__name__ = "Integer32"
_PnniSpvpcSrcSusceptClip_Object = MibTableColumn
pnniSpvpcSrcSusceptClip = _PnniSpvpcSrcSusceptClip_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 11),
    _PnniSpvpcSrcSusceptClip_Type()
)
pnniSpvpcSrcSusceptClip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvpcSrcSusceptClip.setStatus("current")


class _PnniSpvpcSrcFwdQoSClass_Type(Integer32):
    """Custom type pnniSpvpcSrcFwdQoSClass based on Integer32"""
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
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5))
    )


_PnniSpvpcSrcFwdQoSClass_Type.__name__ = "Integer32"
_PnniSpvpcSrcFwdQoSClass_Object = MibTableColumn
pnniSpvpcSrcFwdQoSClass = _PnniSpvpcSrcFwdQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 12),
    _PnniSpvpcSrcFwdQoSClass_Type()
)
pnniSpvpcSrcFwdQoSClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvpcSrcFwdQoSClass.setStatus("current")


class _PnniSpvpcSrcBckQoSClass_Type(Integer32):
    """Custom type pnniSpvpcSrcBckQoSClass based on Integer32"""
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
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5))
    )


_PnniSpvpcSrcBckQoSClass_Type.__name__ = "Integer32"
_PnniSpvpcSrcBckQoSClass_Object = MibTableColumn
pnniSpvpcSrcBckQoSClass = _PnniSpvpcSrcBckQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 13),
    _PnniSpvpcSrcBckQoSClass_Type()
)
pnniSpvpcSrcBckQoSClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvpcSrcBckQoSClass.setStatus("current")


class _PnniSpvpcSrcLastFailCause_Type(DisplayString):
    """Custom type pnniSpvpcSrcLastFailCause based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_PnniSpvpcSrcLastFailCause_Type.__name__ = "DisplayString"
_PnniSpvpcSrcLastFailCause_Object = MibTableColumn
pnniSpvpcSrcLastFailCause = _PnniSpvpcSrcLastFailCause_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 14),
    _PnniSpvpcSrcLastFailCause_Type()
)
pnniSpvpcSrcLastFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvpcSrcLastFailCause.setStatus("current")
_PnniSpvpcSrcRetryCount_Type = Integer32
_PnniSpvpcSrcRetryCount_Object = MibTableColumn
pnniSpvpcSrcRetryCount = _PnniSpvpcSrcRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 15),
    _PnniSpvpcSrcRetryCount_Type()
)
pnniSpvpcSrcRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvpcSrcRetryCount.setStatus("current")
_PnniSpvpcSrcLastChangeTime_Type = TimeTicks
_PnniSpvpcSrcLastChangeTime_Object = MibTableColumn
pnniSpvpcSrcLastChangeTime = _PnniSpvpcSrcLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 16),
    _PnniSpvpcSrcLastChangeTime_Type()
)
pnniSpvpcSrcLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvpcSrcLastChangeTime.setStatus("current")


class _PnniSpvpcSrcStatus_Type(Integer32):
    """Custom type pnniSpvpcSrcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_PnniSpvpcSrcStatus_Type.__name__ = "Integer32"
_PnniSpvpcSrcStatus_Object = MibTableColumn
pnniSpvpcSrcStatus = _PnniSpvpcSrcStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 17),
    _PnniSpvpcSrcStatus_Type()
)
pnniSpvpcSrcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvpcSrcStatus.setStatus("current")


class _PnniSpvpcSrcName_Type(OctetString):
    """Custom type pnniSpvpcSrcName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PnniSpvpcSrcName_Type.__name__ = "OctetString"
_PnniSpvpcSrcName_Object = MibTableColumn
pnniSpvpcSrcName = _PnniSpvpcSrcName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 18),
    _PnniSpvpcSrcName_Type()
)
pnniSpvpcSrcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvpcSrcName.setStatus("current")
_PnniSpvpcSrcRowStatus_Type = RowStatus
_PnniSpvpcSrcRowStatus_Object = MibTableColumn
pnniSpvpcSrcRowStatus = _PnniSpvpcSrcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 19),
    _PnniSpvpcSrcRowStatus_Type()
)
pnniSpvpcSrcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvpcSrcRowStatus.setStatus("current")
_PnniSpvpcSrcRouteCost_Type = Integer32
_PnniSpvpcSrcRouteCost_Object = MibTableColumn
pnniSpvpcSrcRouteCost = _PnniSpvpcSrcRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 20),
    _PnniSpvpcSrcRouteCost_Type()
)
pnniSpvpcSrcRouteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvpcSrcRouteCost.setStatus("current")


class _PnniSpvpcSrcRerouteStatus_Type(Integer32):
    """Custom type pnniSpvpcSrcRerouteStatus based on Integer32"""
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


_PnniSpvpcSrcRerouteStatus_Type.__name__ = "Integer32"
_PnniSpvpcSrcRerouteStatus_Object = MibTableColumn
pnniSpvpcSrcRerouteStatus = _PnniSpvpcSrcRerouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 21),
    _PnniSpvpcSrcRerouteStatus_Type()
)
pnniSpvpcSrcRerouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvpcSrcRerouteStatus.setStatus("current")
_PnniSpvpcSrcCallingDomain_Type = Integer32
_PnniSpvpcSrcCallingDomain_Object = MibTableColumn
pnniSpvpcSrcCallingDomain = _PnniSpvpcSrcCallingDomain_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 22),
    _PnniSpvpcSrcCallingDomain_Type()
)
pnniSpvpcSrcCallingDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvpcSrcCallingDomain.setStatus("current")
_PnniSpvpcSrcQosIndex_Type = Integer32
_PnniSpvpcSrcQosIndex_Object = MibTableColumn
pnniSpvpcSrcQosIndex = _PnniSpvpcSrcQosIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 23),
    _PnniSpvpcSrcQosIndex_Type()
)
pnniSpvpcSrcQosIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvpcSrcQosIndex.setStatus("current")
_PnniSpvpcSrcPriority_Type = Integer32
_PnniSpvpcSrcPriority_Object = MibTableColumn
pnniSpvpcSrcPriority = _PnniSpvpcSrcPriority_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 24),
    _PnniSpvpcSrcPriority_Type()
)
pnniSpvpcSrcPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvpcSrcPriority.setStatus("current")
_PnniSpvpcSrcLastLocation_Type = DisplayString
_PnniSpvpcSrcLastLocation_Object = MibTableColumn
pnniSpvpcSrcLastLocation = _PnniSpvpcSrcLastLocation_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 25),
    _PnniSpvpcSrcLastLocation_Type()
)
pnniSpvpcSrcLastLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvpcSrcLastLocation.setStatus("current")
_PnniSpvpcSrcOldRouteCost_Type = Integer32
_PnniSpvpcSrcOldRouteCost_Object = MibTableColumn
pnniSpvpcSrcOldRouteCost = _PnniSpvpcSrcOldRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 26),
    _PnniSpvpcSrcOldRouteCost_Type()
)
pnniSpvpcSrcOldRouteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvpcSrcOldRouteCost.setStatus("current")


class _PnniSpvpcSrcDownReason_Type(Integer32):
    """Custom type pnniSpvpcSrcDownReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deletion", 3),
          ("failure", 2),
          ("reroute", 1))
    )


_PnniSpvpcSrcDownReason_Type.__name__ = "Integer32"
_PnniSpvpcSrcDownReason_Object = MibTableColumn
pnniSpvpcSrcDownReason = _PnniSpvpcSrcDownReason_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 27),
    _PnniSpvpcSrcDownReason_Type()
)
pnniSpvpcSrcDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvpcSrcDownReason.setStatus("current")


class _PnniSpvpcSrcBackoffStatus_Type(Integer32):
    """Custom type pnniSpvpcSrcBackoffStatus based on Integer32"""
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


_PnniSpvpcSrcBackoffStatus_Type.__name__ = "Integer32"
_PnniSpvpcSrcBackoffStatus_Object = MibTableColumn
pnniSpvpcSrcBackoffStatus = _PnniSpvpcSrcBackoffStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 28),
    _PnniSpvpcSrcBackoffStatus_Type()
)
pnniSpvpcSrcBackoffStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvpcSrcBackoffStatus.setStatus("current")
_PnniSpvpcSrcActiveDtlIndex_Type = Integer32
_PnniSpvpcSrcActiveDtlIndex_Object = MibTableColumn
pnniSpvpcSrcActiveDtlIndex = _PnniSpvpcSrcActiveDtlIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 29),
    _PnniSpvpcSrcActiveDtlIndex_Type()
)
pnniSpvpcSrcActiveDtlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvpcSrcActiveDtlIndex.setStatus("current")
_PnniSpvpcSrcActiveDtlNodeIndex_Type = Integer32
_PnniSpvpcSrcActiveDtlNodeIndex_Object = MibTableColumn
pnniSpvpcSrcActiveDtlNodeIndex = _PnniSpvpcSrcActiveDtlNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 30),
    _PnniSpvpcSrcActiveDtlNodeIndex_Type()
)
pnniSpvpcSrcActiveDtlNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvpcSrcActiveDtlNodeIndex.setStatus("current")
_PnniSpvpcSrcDtlTag_Type = Integer32
_PnniSpvpcSrcDtlTag_Object = MibTableColumn
pnniSpvpcSrcDtlTag = _PnniSpvpcSrcDtlTag_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 31),
    _PnniSpvpcSrcDtlTag_Type()
)
pnniSpvpcSrcDtlTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvpcSrcDtlTag.setStatus("current")


class _PnniSpvpcSrcAutoDtlStatus_Type(Integer32):
    """Custom type pnniSpvpcSrcAutoDtlStatus based on Integer32"""
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


_PnniSpvpcSrcAutoDtlStatus_Type.__name__ = "Integer32"
_PnniSpvpcSrcAutoDtlStatus_Object = MibTableColumn
pnniSpvpcSrcAutoDtlStatus = _PnniSpvpcSrcAutoDtlStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 32),
    _PnniSpvpcSrcAutoDtlStatus_Type()
)
pnniSpvpcSrcAutoDtlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvpcSrcAutoDtlStatus.setStatus("current")


class _PnniSpvpcSrcRGroupIndex_Type(Integer32):
    """Custom type pnniSpvpcSrcRGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PnniSpvpcSrcRGroupIndex_Type.__name__ = "Integer32"
_PnniSpvpcSrcRGroupIndex_Object = MibTableColumn
pnniSpvpcSrcRGroupIndex = _PnniSpvpcSrcRGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 33),
    _PnniSpvpcSrcRGroupIndex_Type()
)
pnniSpvpcSrcRGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvpcSrcRGroupIndex.setStatus("current")
_PnniSpvpcSrcSecondaryVPI_Type = Integer32
_PnniSpvpcSrcSecondaryVPI_Object = MibTableColumn
pnniSpvpcSrcSecondaryVPI = _PnniSpvpcSrcSecondaryVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 9, 1, 34),
    _PnniSpvpcSrcSecondaryVPI_Type()
)
pnniSpvpcSrcSecondaryVPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSpvpcSrcSecondaryVPI.setStatus("current")
_PnniSpvpcStatsGroup_ObjectIdentity = ObjectIdentity
pnniSpvpcStatsGroup = _PnniSpvpcStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 10)
)
_PnniSpvpcSrcNumberOfSPVPCs_Type = Gauge32
_PnniSpvpcSrcNumberOfSPVPCs_Object = MibScalar
pnniSpvpcSrcNumberOfSPVPCs = _PnniSpvpcSrcNumberOfSPVPCs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 10, 1),
    _PnniSpvpcSrcNumberOfSPVPCs_Type()
)
pnniSpvpcSrcNumberOfSPVPCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvpcSrcNumberOfSPVPCs.setStatus("current")
_PnniSpvpcDestNumberOfSPVPCs_Type = Gauge32
_PnniSpvpcDestNumberOfSPVPCs_Object = MibScalar
pnniSpvpcDestNumberOfSPVPCs = _PnniSpvpcDestNumberOfSPVPCs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 10, 2),
    _PnniSpvpcDestNumberOfSPVPCs_Type()
)
pnniSpvpcDestNumberOfSPVPCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvpcDestNumberOfSPVPCs.setStatus("current")
_PnniSpvpcDestTable_Object = MibTable
pnniSpvpcDestTable = _PnniSpvpcDestTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 11)
)
if mibBuilder.loadTexts:
    pnniSpvpcDestTable.setStatus("current")
_PnniSpvpcDestEntry_Object = MibTableRow
pnniSpvpcDestEntry = _PnniSpvpcDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 11, 1)
)
pnniSpvpcDestEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "pnniSpvpcDestIndex"),
)
if mibBuilder.loadTexts:
    pnniSpvpcDestEntry.setStatus("current")


class _PnniSpvpcDestIndex_Type(Integer32):
    """Custom type pnniSpvpcDestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PnniSpvpcDestIndex_Type.__name__ = "Integer32"
_PnniSpvpcDestIndex_Object = MibTableColumn
pnniSpvpcDestIndex = _PnniSpvpcDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 11, 1, 1),
    _PnniSpvpcDestIndex_Type()
)
pnniSpvpcDestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvpcDestIndex.setStatus("current")
_PnniSpvpcDestCallingAtmAddr_Type = NsapAddr
_PnniSpvpcDestCallingAtmAddr_Object = MibTableColumn
pnniSpvpcDestCallingAtmAddr = _PnniSpvpcDestCallingAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 11, 1, 2),
    _PnniSpvpcDestCallingAtmAddr_Type()
)
pnniSpvpcDestCallingAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvpcDestCallingAtmAddr.setStatus("current")


class _PnniSpvpcDestCallingPort_Type(Integer32):
    """Custom type pnniSpvpcDestCallingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1025),
    )


_PnniSpvpcDestCallingPort_Type.__name__ = "Integer32"
_PnniSpvpcDestCallingPort_Object = MibTableColumn
pnniSpvpcDestCallingPort = _PnniSpvpcDestCallingPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 11, 1, 3),
    _PnniSpvpcDestCallingPort_Type()
)
pnniSpvpcDestCallingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvpcDestCallingPort.setStatus("current")


class _PnniSpvpcDestCallingVPI_Type(Integer32):
    """Custom type pnniSpvpcDestCallingVPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_PnniSpvpcDestCallingVPI_Type.__name__ = "Integer32"
_PnniSpvpcDestCallingVPI_Object = MibTableColumn
pnniSpvpcDestCallingVPI = _PnniSpvpcDestCallingVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 11, 1, 4),
    _PnniSpvpcDestCallingVPI_Type()
)
pnniSpvpcDestCallingVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvpcDestCallingVPI.setStatus("current")
_PnniSpvpcDestCalledAtmAddr_Type = NsapAddr
_PnniSpvpcDestCalledAtmAddr_Object = MibTableColumn
pnniSpvpcDestCalledAtmAddr = _PnniSpvpcDestCalledAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 11, 1, 5),
    _PnniSpvpcDestCalledAtmAddr_Type()
)
pnniSpvpcDestCalledAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvpcDestCalledAtmAddr.setStatus("current")


class _PnniSpvpcDestCalledPort_Type(Integer32):
    """Custom type pnniSpvpcDestCalledPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1025),
    )


_PnniSpvpcDestCalledPort_Type.__name__ = "Integer32"
_PnniSpvpcDestCalledPort_Object = MibTableColumn
pnniSpvpcDestCalledPort = _PnniSpvpcDestCalledPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 11, 1, 6),
    _PnniSpvpcDestCalledPort_Type()
)
pnniSpvpcDestCalledPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvpcDestCalledPort.setStatus("current")


class _PnniSpvpcDestAssignedVPI_Type(Integer32):
    """Custom type pnniSpvpcDestAssignedVPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_PnniSpvpcDestAssignedVPI_Type.__name__ = "Integer32"
_PnniSpvpcDestAssignedVPI_Object = MibTableColumn
pnniSpvpcDestAssignedVPI = _PnniSpvpcDestAssignedVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 11, 1, 7),
    _PnniSpvpcDestAssignedVPI_Type()
)
pnniSpvpcDestAssignedVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvpcDestAssignedVPI.setStatus("current")


class _PnniSpvpcDestSusceptClip_Type(Integer32):
    """Custom type pnniSpvpcDestSusceptClip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PnniSpvpcDestSusceptClip_Type.__name__ = "Integer32"
_PnniSpvpcDestSusceptClip_Object = MibTableColumn
pnniSpvpcDestSusceptClip = _PnniSpvpcDestSusceptClip_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 11, 1, 8),
    _PnniSpvpcDestSusceptClip_Type()
)
pnniSpvpcDestSusceptClip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvpcDestSusceptClip.setStatus("current")
_PnniSpvpcDestUpTime_Type = TimeTicks
_PnniSpvpcDestUpTime_Object = MibTableColumn
pnniSpvpcDestUpTime = _PnniSpvpcDestUpTime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 11, 1, 9),
    _PnniSpvpcDestUpTime_Type()
)
pnniSpvpcDestUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvpcDestUpTime.setStatus("current")


class _PnniSpvpcDestFwdQoSClass_Type(Integer32):
    """Custom type pnniSpvpcDestFwdQoSClass based on Integer32"""
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
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5))
    )


_PnniSpvpcDestFwdQoSClass_Type.__name__ = "Integer32"
_PnniSpvpcDestFwdQoSClass_Object = MibTableColumn
pnniSpvpcDestFwdQoSClass = _PnniSpvpcDestFwdQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 11, 1, 10),
    _PnniSpvpcDestFwdQoSClass_Type()
)
pnniSpvpcDestFwdQoSClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvpcDestFwdQoSClass.setStatus("current")


class _PnniSpvpcDestBckQoSClass_Type(Integer32):
    """Custom type pnniSpvpcDestBckQoSClass based on Integer32"""
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
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5))
    )


_PnniSpvpcDestBckQoSClass_Type.__name__ = "Integer32"
_PnniSpvpcDestBckQoSClass_Object = MibTableColumn
pnniSpvpcDestBckQoSClass = _PnniSpvpcDestBckQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 11, 1, 11),
    _PnniSpvpcDestBckQoSClass_Type()
)
pnniSpvpcDestBckQoSClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvpcDestBckQoSClass.setStatus("current")


class _PnniSpvpcDestStatus_Type(Integer32):
    """Custom type pnniSpvpcDestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_PnniSpvpcDestStatus_Type.__name__ = "Integer32"
_PnniSpvpcDestStatus_Object = MibTableColumn
pnniSpvpcDestStatus = _PnniSpvpcDestStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 11, 1, 12),
    _PnniSpvpcDestStatus_Type()
)
pnniSpvpcDestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvpcDestStatus.setStatus("current")


class _PnniSpvpcDestRGroupIndex_Type(Integer32):
    """Custom type pnniSpvpcDestRGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PnniSpvpcDestRGroupIndex_Type.__name__ = "Integer32"
_PnniSpvpcDestRGroupIndex_Object = MibTableColumn
pnniSpvpcDestRGroupIndex = _PnniSpvpcDestRGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 11, 1, 13),
    _PnniSpvpcDestRGroupIndex_Type()
)
pnniSpvpcDestRGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvpcDestRGroupIndex.setStatus("current")
_PnniPmpSpvccGroup_ObjectIdentity = ObjectIdentity
pnniPmpSpvccGroup = _PnniPmpSpvccGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12)
)
_PnniPmpSpvccSrcNextRootIndex_Type = TestAndIncr
_PnniPmpSpvccSrcNextRootIndex_Object = MibScalar
pnniPmpSpvccSrcNextRootIndex = _PnniPmpSpvccSrcNextRootIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 1),
    _PnniPmpSpvccSrcNextRootIndex_Type()
)
pnniPmpSpvccSrcNextRootIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcNextRootIndex.setStatus("current")
_PnniPmpSpvccSrcNumberOfSpvccs_Type = Integer32
_PnniPmpSpvccSrcNumberOfSpvccs_Object = MibScalar
pnniPmpSpvccSrcNumberOfSpvccs = _PnniPmpSpvccSrcNumberOfSpvccs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 2),
    _PnniPmpSpvccSrcNumberOfSpvccs_Type()
)
pnniPmpSpvccSrcNumberOfSpvccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcNumberOfSpvccs.setStatus("current")
_PnniPmpSpvccSrcRootTable_Object = MibTable
pnniPmpSpvccSrcRootTable = _PnniPmpSpvccSrcRootTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 3)
)
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcRootTable.setStatus("current")
_PnniPmpSpvccSrcRootEntry_Object = MibTableRow
pnniPmpSpvccSrcRootEntry = _PnniPmpSpvccSrcRootEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 3, 1)
)
pnniPmpSpvccSrcRootEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "pnniPmpSpvccSrcRootIndex"),
)
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcRootEntry.setStatus("current")
_PnniPmpSpvccSrcRootIndex_Type = Integer32
_PnniPmpSpvccSrcRootIndex_Object = MibTableColumn
pnniPmpSpvccSrcRootIndex = _PnniPmpSpvccSrcRootIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 3, 1, 1),
    _PnniPmpSpvccSrcRootIndex_Type()
)
pnniPmpSpvccSrcRootIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcRootIndex.setStatus("current")
_PnniPmpSpvccSrcRootPort_Type = Integer32
_PnniPmpSpvccSrcRootPort_Object = MibTableColumn
pnniPmpSpvccSrcRootPort = _PnniPmpSpvccSrcRootPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 3, 1, 2),
    _PnniPmpSpvccSrcRootPort_Type()
)
pnniPmpSpvccSrcRootPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcRootPort.setStatus("current")
_PnniPmpSpvccSrcRootVPI_Type = Integer32
_PnniPmpSpvccSrcRootVPI_Object = MibTableColumn
pnniPmpSpvccSrcRootVPI = _PnniPmpSpvccSrcRootVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 3, 1, 3),
    _PnniPmpSpvccSrcRootVPI_Type()
)
pnniPmpSpvccSrcRootVPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcRootVPI.setStatus("current")
_PnniPmpSpvccSrcRootVCI_Type = Integer32
_PnniPmpSpvccSrcRootVCI_Object = MibTableColumn
pnniPmpSpvccSrcRootVCI = _PnniPmpSpvccSrcRootVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 3, 1, 4),
    _PnniPmpSpvccSrcRootVCI_Type()
)
pnniPmpSpvccSrcRootVCI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcRootVCI.setStatus("current")
_PnniPmpSpvccSrcRootFwdUpcKey_Type = Integer32
_PnniPmpSpvccSrcRootFwdUpcKey_Object = MibTableColumn
pnniPmpSpvccSrcRootFwdUpcKey = _PnniPmpSpvccSrcRootFwdUpcKey_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 3, 1, 5),
    _PnniPmpSpvccSrcRootFwdUpcKey_Type()
)
pnniPmpSpvccSrcRootFwdUpcKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcRootFwdUpcKey.setStatus("current")


class _PnniPmpSpvccSrcRootBearerClass_Type(Integer32):
    """Custom type pnniPmpSpvccSrcRootBearerClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("classA", 1),
          ("classC", 2),
          ("classX", 3))
    )


_PnniPmpSpvccSrcRootBearerClass_Type.__name__ = "Integer32"
_PnniPmpSpvccSrcRootBearerClass_Object = MibTableColumn
pnniPmpSpvccSrcRootBearerClass = _PnniPmpSpvccSrcRootBearerClass_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 3, 1, 6),
    _PnniPmpSpvccSrcRootBearerClass_Type()
)
pnniPmpSpvccSrcRootBearerClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcRootBearerClass.setStatus("current")


class _PnniPmpSpvccSrcRootSusceptClip_Type(Integer32):
    """Custom type pnniPmpSpvccSrcRootSusceptClip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PnniPmpSpvccSrcRootSusceptClip_Type.__name__ = "Integer32"
_PnniPmpSpvccSrcRootSusceptClip_Object = MibTableColumn
pnniPmpSpvccSrcRootSusceptClip = _PnniPmpSpvccSrcRootSusceptClip_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 3, 1, 7),
    _PnniPmpSpvccSrcRootSusceptClip_Type()
)
pnniPmpSpvccSrcRootSusceptClip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcRootSusceptClip.setStatus("current")


class _PnniPmpSpvccSrcRootFwdQoSClass_Type(Integer32):
    """Custom type pnniPmpSpvccSrcRootFwdQoSClass based on Integer32"""
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
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5))
    )


_PnniPmpSpvccSrcRootFwdQoSClass_Type.__name__ = "Integer32"
_PnniPmpSpvccSrcRootFwdQoSClass_Object = MibTableColumn
pnniPmpSpvccSrcRootFwdQoSClass = _PnniPmpSpvccSrcRootFwdQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 3, 1, 8),
    _PnniPmpSpvccSrcRootFwdQoSClass_Type()
)
pnniPmpSpvccSrcRootFwdQoSClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcRootFwdQoSClass.setStatus("current")


class _PnniPmpSpvccSrcRootStatus_Type(Integer32):
    """Custom type pnniPmpSpvccSrcRootStatus based on Integer32"""
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
          ("up", 1),
          ("wait", 3))
    )


_PnniPmpSpvccSrcRootStatus_Type.__name__ = "Integer32"
_PnniPmpSpvccSrcRootStatus_Object = MibTableColumn
pnniPmpSpvccSrcRootStatus = _PnniPmpSpvccSrcRootStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 3, 1, 9),
    _PnniPmpSpvccSrcRootStatus_Type()
)
pnniPmpSpvccSrcRootStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcRootStatus.setStatus("current")


class _PnniPmpSpvccSrcRootName_Type(OctetString):
    """Custom type pnniPmpSpvccSrcRootName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PnniPmpSpvccSrcRootName_Type.__name__ = "OctetString"
_PnniPmpSpvccSrcRootName_Object = MibTableColumn
pnniPmpSpvccSrcRootName = _PnniPmpSpvccSrcRootName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 3, 1, 10),
    _PnniPmpSpvccSrcRootName_Type()
)
pnniPmpSpvccSrcRootName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcRootName.setStatus("current")
_PnniPmpSpvccSrcRootPriority_Type = Integer32
_PnniPmpSpvccSrcRootPriority_Object = MibTableColumn
pnniPmpSpvccSrcRootPriority = _PnniPmpSpvccSrcRootPriority_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 3, 1, 11),
    _PnniPmpSpvccSrcRootPriority_Type()
)
pnniPmpSpvccSrcRootPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcRootPriority.setStatus("current")
_PnniPmpSpvccSrcRootNumberOfParties_Type = Integer32
_PnniPmpSpvccSrcRootNumberOfParties_Object = MibTableColumn
pnniPmpSpvccSrcRootNumberOfParties = _PnniPmpSpvccSrcRootNumberOfParties_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 3, 1, 12),
    _PnniPmpSpvccSrcRootNumberOfParties_Type()
)
pnniPmpSpvccSrcRootNumberOfParties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcRootNumberOfParties.setStatus("current")
_PnniPmpSpvccSrcRootNextPartyIndex_Type = TestAndIncr
_PnniPmpSpvccSrcRootNextPartyIndex_Object = MibTableColumn
pnniPmpSpvccSrcRootNextPartyIndex = _PnniPmpSpvccSrcRootNextPartyIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 3, 1, 13),
    _PnniPmpSpvccSrcRootNextPartyIndex_Type()
)
pnniPmpSpvccSrcRootNextPartyIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcRootNextPartyIndex.setStatus("current")
_PnniPmpSpvccSrcRootCallingDomain_Type = Integer32
_PnniPmpSpvccSrcRootCallingDomain_Object = MibTableColumn
pnniPmpSpvccSrcRootCallingDomain = _PnniPmpSpvccSrcRootCallingDomain_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 3, 1, 14),
    _PnniPmpSpvccSrcRootCallingDomain_Type()
)
pnniPmpSpvccSrcRootCallingDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcRootCallingDomain.setStatus("current")
_PnniPmpSpvccSrcRootRowStatus_Type = RowStatus
_PnniPmpSpvccSrcRootRowStatus_Object = MibTableColumn
pnniPmpSpvccSrcRootRowStatus = _PnniPmpSpvccSrcRootRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 3, 1, 15),
    _PnniPmpSpvccSrcRootRowStatus_Type()
)
pnniPmpSpvccSrcRootRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcRootRowStatus.setStatus("current")


class _PnniPmpSpvccSrcRootRGroupIndex_Type(Integer32):
    """Custom type pnniPmpSpvccSrcRootRGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PnniPmpSpvccSrcRootRGroupIndex_Type.__name__ = "Integer32"
_PnniPmpSpvccSrcRootRGroupIndex_Object = MibTableColumn
pnniPmpSpvccSrcRootRGroupIndex = _PnniPmpSpvccSrcRootRGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 3, 1, 16),
    _PnniPmpSpvccSrcRootRGroupIndex_Type()
)
pnniPmpSpvccSrcRootRGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcRootRGroupIndex.setStatus("current")
_PnniPmpSpvccSrcRootSecondaryVPI_Type = Integer32
_PnniPmpSpvccSrcRootSecondaryVPI_Object = MibTableColumn
pnniPmpSpvccSrcRootSecondaryVPI = _PnniPmpSpvccSrcRootSecondaryVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 3, 1, 17),
    _PnniPmpSpvccSrcRootSecondaryVPI_Type()
)
pnniPmpSpvccSrcRootSecondaryVPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcRootSecondaryVPI.setStatus("current")
_PnniPmpSpvccSrcRootSecondaryVCI_Type = Integer32
_PnniPmpSpvccSrcRootSecondaryVCI_Object = MibTableColumn
pnniPmpSpvccSrcRootSecondaryVCI = _PnniPmpSpvccSrcRootSecondaryVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 3, 1, 18),
    _PnniPmpSpvccSrcRootSecondaryVCI_Type()
)
pnniPmpSpvccSrcRootSecondaryVCI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcRootSecondaryVCI.setStatus("current")
_PnniPmpSpvccSrcPartyTable_Object = MibTable
pnniPmpSpvccSrcPartyTable = _PnniPmpSpvccSrcPartyTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 4)
)
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcPartyTable.setStatus("current")
_PnniPmpSpvccSrcPartyEntry_Object = MibTableRow
pnniPmpSpvccSrcPartyEntry = _PnniPmpSpvccSrcPartyEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 4, 1)
)
pnniPmpSpvccSrcPartyEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "pnniPmpSpvccSrcRootIndex"),
    (0, "Fore-Switch-MIB", "pnniPmpSpvccSrcPartyIndex"),
)
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcPartyEntry.setStatus("current")
_PnniPmpSpvccSrcPartyIndex_Type = Integer32
_PnniPmpSpvccSrcPartyIndex_Object = MibTableColumn
pnniPmpSpvccSrcPartyIndex = _PnniPmpSpvccSrcPartyIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 4, 1, 1),
    _PnniPmpSpvccSrcPartyIndex_Type()
)
pnniPmpSpvccSrcPartyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcPartyIndex.setStatus("current")
_PnniPmpSpvccSrcPartyAtmAddr_Type = NsapAddr
_PnniPmpSpvccSrcPartyAtmAddr_Object = MibTableColumn
pnniPmpSpvccSrcPartyAtmAddr = _PnniPmpSpvccSrcPartyAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 4, 1, 2),
    _PnniPmpSpvccSrcPartyAtmAddr_Type()
)
pnniPmpSpvccSrcPartyAtmAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcPartyAtmAddr.setStatus("current")


class _PnniPmpSpvccSrcPartyVPVCSel_Type(Integer32):
    """Custom type pnniPmpSpvccSrcPartyVPVCSel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPref", 1),
          ("require", 2))
    )


_PnniPmpSpvccSrcPartyVPVCSel_Type.__name__ = "Integer32"
_PnniPmpSpvccSrcPartyVPVCSel_Object = MibTableColumn
pnniPmpSpvccSrcPartyVPVCSel = _PnniPmpSpvccSrcPartyVPVCSel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 4, 1, 3),
    _PnniPmpSpvccSrcPartyVPVCSel_Type()
)
pnniPmpSpvccSrcPartyVPVCSel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcPartyVPVCSel.setStatus("current")
_PnniPmpSpvccSrcPartyVPI_Type = Integer32
_PnniPmpSpvccSrcPartyVPI_Object = MibTableColumn
pnniPmpSpvccSrcPartyVPI = _PnniPmpSpvccSrcPartyVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 4, 1, 4),
    _PnniPmpSpvccSrcPartyVPI_Type()
)
pnniPmpSpvccSrcPartyVPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcPartyVPI.setStatus("current")
_PnniPmpSpvccSrcPartyVCI_Type = Integer32
_PnniPmpSpvccSrcPartyVCI_Object = MibTableColumn
pnniPmpSpvccSrcPartyVCI = _PnniPmpSpvccSrcPartyVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 4, 1, 5),
    _PnniPmpSpvccSrcPartyVCI_Type()
)
pnniPmpSpvccSrcPartyVCI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcPartyVCI.setStatus("current")
_PnniPmpSpvccSrcPartyAssignedVPI_Type = Integer32
_PnniPmpSpvccSrcPartyAssignedVPI_Object = MibTableColumn
pnniPmpSpvccSrcPartyAssignedVPI = _PnniPmpSpvccSrcPartyAssignedVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 4, 1, 6),
    _PnniPmpSpvccSrcPartyAssignedVPI_Type()
)
pnniPmpSpvccSrcPartyAssignedVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcPartyAssignedVPI.setStatus("current")
_PnniPmpSpvccSrcPartyAssignedVCI_Type = Integer32
_PnniPmpSpvccSrcPartyAssignedVCI_Object = MibTableColumn
pnniPmpSpvccSrcPartyAssignedVCI = _PnniPmpSpvccSrcPartyAssignedVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 4, 1, 7),
    _PnniPmpSpvccSrcPartyAssignedVCI_Type()
)
pnniPmpSpvccSrcPartyAssignedVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcPartyAssignedVCI.setStatus("current")


class _PnniPmpSpvccSrcPartyStatus_Type(Integer32):
    """Custom type pnniPmpSpvccSrcPartyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connecting", 3),
          ("down", 2),
          ("up", 1))
    )


_PnniPmpSpvccSrcPartyStatus_Type.__name__ = "Integer32"
_PnniPmpSpvccSrcPartyStatus_Object = MibTableColumn
pnniPmpSpvccSrcPartyStatus = _PnniPmpSpvccSrcPartyStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 4, 1, 8),
    _PnniPmpSpvccSrcPartyStatus_Type()
)
pnniPmpSpvccSrcPartyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcPartyStatus.setStatus("current")


class _PnniPmpSpvccSrcPartyName_Type(OctetString):
    """Custom type pnniPmpSpvccSrcPartyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PnniPmpSpvccSrcPartyName_Type.__name__ = "OctetString"
_PnniPmpSpvccSrcPartyName_Object = MibTableColumn
pnniPmpSpvccSrcPartyName = _PnniPmpSpvccSrcPartyName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 4, 1, 9),
    _PnniPmpSpvccSrcPartyName_Type()
)
pnniPmpSpvccSrcPartyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcPartyName.setStatus("current")
_PnniPmpSpvccSrcPartyLastFailCause_Type = DisplayString
_PnniPmpSpvccSrcPartyLastFailCause_Object = MibTableColumn
pnniPmpSpvccSrcPartyLastFailCause = _PnniPmpSpvccSrcPartyLastFailCause_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 4, 1, 10),
    _PnniPmpSpvccSrcPartyLastFailCause_Type()
)
pnniPmpSpvccSrcPartyLastFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcPartyLastFailCause.setStatus("current")
_PnniPmpSpvccSrcPartyRetryCount_Type = Integer32
_PnniPmpSpvccSrcPartyRetryCount_Object = MibTableColumn
pnniPmpSpvccSrcPartyRetryCount = _PnniPmpSpvccSrcPartyRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 4, 1, 11),
    _PnniPmpSpvccSrcPartyRetryCount_Type()
)
pnniPmpSpvccSrcPartyRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcPartyRetryCount.setStatus("current")
_PnniPmpSpvccSrcPartyLastChangeTime_Type = TimeTicks
_PnniPmpSpvccSrcPartyLastChangeTime_Object = MibTableColumn
pnniPmpSpvccSrcPartyLastChangeTime = _PnniPmpSpvccSrcPartyLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 4, 1, 12),
    _PnniPmpSpvccSrcPartyLastChangeTime_Type()
)
pnniPmpSpvccSrcPartyLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcPartyLastChangeTime.setStatus("current")
_PnniPmpSpvccSrcPartyFtDtlIndex_Type = Integer32
_PnniPmpSpvccSrcPartyFtDtlIndex_Object = MibTableColumn
pnniPmpSpvccSrcPartyFtDtlIndex = _PnniPmpSpvccSrcPartyFtDtlIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 4, 1, 13),
    _PnniPmpSpvccSrcPartyFtDtlIndex_Type()
)
pnniPmpSpvccSrcPartyFtDtlIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcPartyFtDtlIndex.setStatus("current")


class _PnniPmpSpvccSrcPartyRerouteStatus_Type(Integer32):
    """Custom type pnniPmpSpvccSrcPartyRerouteStatus based on Integer32"""
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
        *(("rerouteCompleted", 3),
          ("rerouteNotApplicable", 4),
          ("rerouteNotRequested", 1),
          ("rerouteRequested", 2))
    )


_PnniPmpSpvccSrcPartyRerouteStatus_Type.__name__ = "Integer32"
_PnniPmpSpvccSrcPartyRerouteStatus_Object = MibTableColumn
pnniPmpSpvccSrcPartyRerouteStatus = _PnniPmpSpvccSrcPartyRerouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 4, 1, 14),
    _PnniPmpSpvccSrcPartyRerouteStatus_Type()
)
pnniPmpSpvccSrcPartyRerouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcPartyRerouteStatus.setStatus("current")
_PnniPmpSpvccSrcPartyQosIndex_Type = Integer32
_PnniPmpSpvccSrcPartyQosIndex_Object = MibTableColumn
pnniPmpSpvccSrcPartyQosIndex = _PnniPmpSpvccSrcPartyQosIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 4, 1, 15),
    _PnniPmpSpvccSrcPartyQosIndex_Type()
)
pnniPmpSpvccSrcPartyQosIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcPartyQosIndex.setStatus("current")
_PnniPmpSpvccSrcPartyRowStatus_Type = RowStatus
_PnniPmpSpvccSrcPartyRowStatus_Object = MibTableColumn
pnniPmpSpvccSrcPartyRowStatus = _PnniPmpSpvccSrcPartyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 4, 1, 16),
    _PnniPmpSpvccSrcPartyRowStatus_Type()
)
pnniPmpSpvccSrcPartyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcPartyRowStatus.setStatus("current")
_PnniPmpSpvccSrcPartyLastLocation_Type = DisplayString
_PnniPmpSpvccSrcPartyLastLocation_Object = MibTableColumn
pnniPmpSpvccSrcPartyLastLocation = _PnniPmpSpvccSrcPartyLastLocation_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 4, 1, 17),
    _PnniPmpSpvccSrcPartyLastLocation_Type()
)
pnniPmpSpvccSrcPartyLastLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcPartyLastLocation.setStatus("current")


class _PnniPmpSpvccSrcPartyAutoDtlStatus_Type(Integer32):
    """Custom type pnniPmpSpvccSrcPartyAutoDtlStatus based on Integer32"""
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


_PnniPmpSpvccSrcPartyAutoDtlStatus_Type.__name__ = "Integer32"
_PnniPmpSpvccSrcPartyAutoDtlStatus_Object = MibTableColumn
pnniPmpSpvccSrcPartyAutoDtlStatus = _PnniPmpSpvccSrcPartyAutoDtlStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 4, 1, 18),
    _PnniPmpSpvccSrcPartyAutoDtlStatus_Type()
)
pnniPmpSpvccSrcPartyAutoDtlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcPartyAutoDtlStatus.setStatus("current")


class _PnniPmpSpvccSrcPartyDownReason_Type(Integer32):
    """Custom type pnniPmpSpvccSrcPartyDownReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deletion", 3),
          ("failure", 2),
          ("reroute", 1))
    )


_PnniPmpSpvccSrcPartyDownReason_Type.__name__ = "Integer32"
_PnniPmpSpvccSrcPartyDownReason_Object = MibTableColumn
pnniPmpSpvccSrcPartyDownReason = _PnniPmpSpvccSrcPartyDownReason_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 4, 1, 19),
    _PnniPmpSpvccSrcPartyDownReason_Type()
)
pnniPmpSpvccSrcPartyDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcPartyDownReason.setStatus("current")
_PnniPmpSpvccSrcPartyRouteCost_Type = Integer32
_PnniPmpSpvccSrcPartyRouteCost_Object = MibTableColumn
pnniPmpSpvccSrcPartyRouteCost = _PnniPmpSpvccSrcPartyRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 4, 1, 20),
    _PnniPmpSpvccSrcPartyRouteCost_Type()
)
pnniPmpSpvccSrcPartyRouteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccSrcPartyRouteCost.setStatus("current")
_PnniPmpSpvccDestNumberOfSpvccs_Type = Integer32
_PnniPmpSpvccDestNumberOfSpvccs_Object = MibScalar
pnniPmpSpvccDestNumberOfSpvccs = _PnniPmpSpvccDestNumberOfSpvccs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 5),
    _PnniPmpSpvccDestNumberOfSpvccs_Type()
)
pnniPmpSpvccDestNumberOfSpvccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccDestNumberOfSpvccs.setStatus("current")
_PnniPmpSpvccDestRootTable_Object = MibTable
pnniPmpSpvccDestRootTable = _PnniPmpSpvccDestRootTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 6)
)
if mibBuilder.loadTexts:
    pnniPmpSpvccDestRootTable.setStatus("current")
_PnniPmpSpvccDestRootEntry_Object = MibTableRow
pnniPmpSpvccDestRootEntry = _PnniPmpSpvccDestRootEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 6, 1)
)
pnniPmpSpvccDestRootEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "pnniPmpSpvccDestRootIndex"),
)
if mibBuilder.loadTexts:
    pnniPmpSpvccDestRootEntry.setStatus("current")
_PnniPmpSpvccDestRootIndex_Type = Integer32
_PnniPmpSpvccDestRootIndex_Object = MibTableColumn
pnniPmpSpvccDestRootIndex = _PnniPmpSpvccDestRootIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 6, 1, 1),
    _PnniPmpSpvccDestRootIndex_Type()
)
pnniPmpSpvccDestRootIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccDestRootIndex.setStatus("current")
_PnniPmpSpvccDestRootAtmAddr_Type = NsapAddr
_PnniPmpSpvccDestRootAtmAddr_Object = MibTableColumn
pnniPmpSpvccDestRootAtmAddr = _PnniPmpSpvccDestRootAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 6, 1, 2),
    _PnniPmpSpvccDestRootAtmAddr_Type()
)
pnniPmpSpvccDestRootAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccDestRootAtmAddr.setStatus("current")
_PnniPmpSpvccDestRootPort_Type = Integer32
_PnniPmpSpvccDestRootPort_Object = MibTableColumn
pnniPmpSpvccDestRootPort = _PnniPmpSpvccDestRootPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 6, 1, 3),
    _PnniPmpSpvccDestRootPort_Type()
)
pnniPmpSpvccDestRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccDestRootPort.setStatus("current")
_PnniPmpSpvccDestRootVPI_Type = Integer32
_PnniPmpSpvccDestRootVPI_Object = MibTableColumn
pnniPmpSpvccDestRootVPI = _PnniPmpSpvccDestRootVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 6, 1, 4),
    _PnniPmpSpvccDestRootVPI_Type()
)
pnniPmpSpvccDestRootVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccDestRootVPI.setStatus("current")
_PnniPmpSpvccDestRootVCI_Type = Integer32
_PnniPmpSpvccDestRootVCI_Object = MibTableColumn
pnniPmpSpvccDestRootVCI = _PnniPmpSpvccDestRootVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 6, 1, 5),
    _PnniPmpSpvccDestRootVCI_Type()
)
pnniPmpSpvccDestRootVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccDestRootVCI.setStatus("current")


class _PnniPmpSpvccDestRootBearerClass_Type(Integer32):
    """Custom type pnniPmpSpvccDestRootBearerClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("classA", 1),
          ("classC", 2),
          ("classX", 3))
    )


_PnniPmpSpvccDestRootBearerClass_Type.__name__ = "Integer32"
_PnniPmpSpvccDestRootBearerClass_Object = MibTableColumn
pnniPmpSpvccDestRootBearerClass = _PnniPmpSpvccDestRootBearerClass_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 6, 1, 6),
    _PnniPmpSpvccDestRootBearerClass_Type()
)
pnniPmpSpvccDestRootBearerClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccDestRootBearerClass.setStatus("current")


class _PnniPmpSpvccDestRootSusceptClip_Type(Integer32):
    """Custom type pnniPmpSpvccDestRootSusceptClip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PnniPmpSpvccDestRootSusceptClip_Type.__name__ = "Integer32"
_PnniPmpSpvccDestRootSusceptClip_Object = MibTableColumn
pnniPmpSpvccDestRootSusceptClip = _PnniPmpSpvccDestRootSusceptClip_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 6, 1, 7),
    _PnniPmpSpvccDestRootSusceptClip_Type()
)
pnniPmpSpvccDestRootSusceptClip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccDestRootSusceptClip.setStatus("current")


class _PnniPmpSpvccDestRootFwdQoSClass_Type(Integer32):
    """Custom type pnniPmpSpvccDestRootFwdQoSClass based on Integer32"""
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
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5))
    )


_PnniPmpSpvccDestRootFwdQoSClass_Type.__name__ = "Integer32"
_PnniPmpSpvccDestRootFwdQoSClass_Object = MibTableColumn
pnniPmpSpvccDestRootFwdQoSClass = _PnniPmpSpvccDestRootFwdQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 6, 1, 8),
    _PnniPmpSpvccDestRootFwdQoSClass_Type()
)
pnniPmpSpvccDestRootFwdQoSClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccDestRootFwdQoSClass.setStatus("current")
_PnniPmpSpvccDestRootNumberOfParties_Type = Integer32
_PnniPmpSpvccDestRootNumberOfParties_Object = MibTableColumn
pnniPmpSpvccDestRootNumberOfParties = _PnniPmpSpvccDestRootNumberOfParties_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 6, 1, 9),
    _PnniPmpSpvccDestRootNumberOfParties_Type()
)
pnniPmpSpvccDestRootNumberOfParties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccDestRootNumberOfParties.setStatus("current")
_PnniPmpSpvccDestPartyTable_Object = MibTable
pnniPmpSpvccDestPartyTable = _PnniPmpSpvccDestPartyTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 7)
)
if mibBuilder.loadTexts:
    pnniPmpSpvccDestPartyTable.setStatus("current")
_PnniPmpSpvccDestPartyEntry_Object = MibTableRow
pnniPmpSpvccDestPartyEntry = _PnniPmpSpvccDestPartyEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 7, 1)
)
pnniPmpSpvccDestPartyEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "pnniPmpSpvccDestRootIndex"),
    (0, "Fore-Switch-MIB", "pnniPmpSpvccDestPartyIndex"),
)
if mibBuilder.loadTexts:
    pnniPmpSpvccDestPartyEntry.setStatus("current")
_PnniPmpSpvccDestPartyIndex_Type = Integer32
_PnniPmpSpvccDestPartyIndex_Object = MibTableColumn
pnniPmpSpvccDestPartyIndex = _PnniPmpSpvccDestPartyIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 7, 1, 1),
    _PnniPmpSpvccDestPartyIndex_Type()
)
pnniPmpSpvccDestPartyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccDestPartyIndex.setStatus("current")
_PnniPmpSpvccDestPartyAtmAddr_Type = NsapAddr
_PnniPmpSpvccDestPartyAtmAddr_Object = MibTableColumn
pnniPmpSpvccDestPartyAtmAddr = _PnniPmpSpvccDestPartyAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 7, 1, 2),
    _PnniPmpSpvccDestPartyAtmAddr_Type()
)
pnniPmpSpvccDestPartyAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccDestPartyAtmAddr.setStatus("current")
_PnniPmpSpvccDestPartyPort_Type = Integer32
_PnniPmpSpvccDestPartyPort_Object = MibTableColumn
pnniPmpSpvccDestPartyPort = _PnniPmpSpvccDestPartyPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 7, 1, 3),
    _PnniPmpSpvccDestPartyPort_Type()
)
pnniPmpSpvccDestPartyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccDestPartyPort.setStatus("current")
_PnniPmpSpvccDestPartyAssignedVPI_Type = Integer32
_PnniPmpSpvccDestPartyAssignedVPI_Object = MibTableColumn
pnniPmpSpvccDestPartyAssignedVPI = _PnniPmpSpvccDestPartyAssignedVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 7, 1, 4),
    _PnniPmpSpvccDestPartyAssignedVPI_Type()
)
pnniPmpSpvccDestPartyAssignedVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccDestPartyAssignedVPI.setStatus("current")
_PnniPmpSpvccDestPartyAssignedVCI_Type = Integer32
_PnniPmpSpvccDestPartyAssignedVCI_Object = MibTableColumn
pnniPmpSpvccDestPartyAssignedVCI = _PnniPmpSpvccDestPartyAssignedVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 7, 1, 5),
    _PnniPmpSpvccDestPartyAssignedVCI_Type()
)
pnniPmpSpvccDestPartyAssignedVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccDestPartyAssignedVCI.setStatus("current")
_PnniPmpSpvccDestPartyUpTime_Type = TimeTicks
_PnniPmpSpvccDestPartyUpTime_Object = MibTableColumn
pnniPmpSpvccDestPartyUpTime = _PnniPmpSpvccDestPartyUpTime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 7, 1, 6),
    _PnniPmpSpvccDestPartyUpTime_Type()
)
pnniPmpSpvccDestPartyUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccDestPartyUpTime.setStatus("current")
_PnniPmpSpvccDestPartyTransitNetSel_Type = TransitNetwork
_PnniPmpSpvccDestPartyTransitNetSel_Object = MibTableColumn
pnniPmpSpvccDestPartyTransitNetSel = _PnniPmpSpvccDestPartyTransitNetSel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 7, 1, 7),
    _PnniPmpSpvccDestPartyTransitNetSel_Type()
)
pnniPmpSpvccDestPartyTransitNetSel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccDestPartyTransitNetSel.setStatus("current")


class _PnniPmpSpvccDestPartyStatus_Type(Integer32):
    """Custom type pnniPmpSpvccDestPartyStatus based on Integer32"""
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
          ("failed", 3),
          ("up", 1))
    )


_PnniPmpSpvccDestPartyStatus_Type.__name__ = "Integer32"
_PnniPmpSpvccDestPartyStatus_Object = MibTableColumn
pnniPmpSpvccDestPartyStatus = _PnniPmpSpvccDestPartyStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 7, 1, 8),
    _PnniPmpSpvccDestPartyStatus_Type()
)
pnniPmpSpvccDestPartyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccDestPartyStatus.setStatus("current")


class _PnniPmpSpvccDestPartyRGroupIndex_Type(Integer32):
    """Custom type pnniPmpSpvccDestPartyRGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PnniPmpSpvccDestPartyRGroupIndex_Type.__name__ = "Integer32"
_PnniPmpSpvccDestPartyRGroupIndex_Object = MibTableColumn
pnniPmpSpvccDestPartyRGroupIndex = _PnniPmpSpvccDestPartyRGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 12, 7, 1, 9),
    _PnniPmpSpvccDestPartyRGroupIndex_Type()
)
pnniPmpSpvccDestPartyRGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPmpSpvccDestPartyRGroupIndex.setStatus("current")
_VpciMappingTableGroup_ObjectIdentity = ObjectIdentity
vpciMappingTableGroup = _VpciMappingTableGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 13)
)
_VmtVpciMapTable_Object = MibTable
vmtVpciMapTable = _VmtVpciMapTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 13, 1)
)
if mibBuilder.loadTexts:
    vmtVpciMapTable.setStatus("current")
_VmtVpciMapEntry_Object = MibTableRow
vmtVpciMapEntry = _VmtVpciMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 13, 1, 1)
)
vmtVpciMapEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "vmtVpciMapIndex"),
)
if mibBuilder.loadTexts:
    vmtVpciMapEntry.setStatus("current")


class _VmtVpciMapIndex_Type(Integer32):
    """Custom type vmtVpciMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99999),
    )


_VmtVpciMapIndex_Type.__name__ = "Integer32"
_VmtVpciMapIndex_Object = MibTableColumn
vmtVpciMapIndex = _VmtVpciMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 13, 1, 1, 1),
    _VmtVpciMapIndex_Type()
)
vmtVpciMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmtVpciMapIndex.setStatus("current")


class _VmtVpciMapVPCI_Type(Integer32):
    """Custom type vmtVpciMapVPCI based on Integer32"""
    defaultValue = 0


_VmtVpciMapVPCI_Object = MibTableColumn
vmtVpciMapVPCI = _VmtVpciMapVPCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 13, 1, 1, 2),
    _VmtVpciMapVPCI_Type()
)
vmtVpciMapVPCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmtVpciMapVPCI.setStatus("current")


class _VmtVpciMapVPI_Type(Integer32):
    """Custom type vmtVpciMapVPI based on Integer32"""
    defaultValue = -1


_VmtVpciMapVPI_Object = MibTableColumn
vmtVpciMapVPI = _VmtVpciMapVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 13, 1, 1, 3),
    _VmtVpciMapVPI_Type()
)
vmtVpciMapVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmtVpciMapVPI.setStatus("current")


class _VmtVpciMapPort_Type(Integer32):
    """Custom type vmtVpciMapPort based on Integer32"""
    defaultValue = -1


_VmtVpciMapPort_Object = MibTableColumn
vmtVpciMapPort = _VmtVpciMapPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 13, 1, 1, 4),
    _VmtVpciMapPort_Type()
)
vmtVpciMapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmtVpciMapPort.setStatus("current")
_VmtVpciMapStatus_Type = RowStatus
_VmtVpciMapStatus_Object = MibTableColumn
vmtVpciMapStatus = _VmtVpciMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 13, 1, 1, 5),
    _VmtVpciMapStatus_Type()
)
vmtVpciMapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmtVpciMapStatus.setStatus("current")
_VmtVpciMapGroupTable_Object = MibTable
vmtVpciMapGroupTable = _VmtVpciMapGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 13, 2)
)
if mibBuilder.loadTexts:
    vmtVpciMapGroupTable.setStatus("current")
_VmtVpciMapGroupEntry_Object = MibTableRow
vmtVpciMapGroupEntry = _VmtVpciMapGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 13, 2, 1)
)
vmtVpciMapGroupEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "vmtVpciMapGroupIndex"),
)
if mibBuilder.loadTexts:
    vmtVpciMapGroupEntry.setStatus("current")


class _VmtVpciMapGroupIndex_Type(Integer32):
    """Custom type vmtVpciMapGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99999),
    )


_VmtVpciMapGroupIndex_Type.__name__ = "Integer32"
_VmtVpciMapGroupIndex_Object = MibTableColumn
vmtVpciMapGroupIndex = _VmtVpciMapGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 13, 2, 1, 1),
    _VmtVpciMapGroupIndex_Type()
)
vmtVpciMapGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmtVpciMapGroupIndex.setStatus("current")
_VmtVpciMapGroupStatus_Type = RowStatus
_VmtVpciMapGroupStatus_Object = MibTableColumn
vmtVpciMapGroupStatus = _VmtVpciMapGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 13, 2, 1, 2),
    _VmtVpciMapGroupStatus_Type()
)
vmtVpciMapGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmtVpciMapGroupStatus.setStatus("current")
_VmtVpciMapListTable_Object = MibTable
vmtVpciMapListTable = _VmtVpciMapListTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 13, 3)
)
if mibBuilder.loadTexts:
    vmtVpciMapListTable.setStatus("current")
_VmtVpciMapListEntry_Object = MibTableRow
vmtVpciMapListEntry = _VmtVpciMapListEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 13, 3, 1)
)
vmtVpciMapListEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "vmtVpciMapGroupIndex"),
    (0, "Fore-Switch-MIB", "vmtVpciMapListIndex"),
)
if mibBuilder.loadTexts:
    vmtVpciMapListEntry.setStatus("current")


class _VmtVpciMapListIndex_Type(Integer32):
    """Custom type vmtVpciMapListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99999),
    )


_VmtVpciMapListIndex_Type.__name__ = "Integer32"
_VmtVpciMapListIndex_Object = MibTableColumn
vmtVpciMapListIndex = _VmtVpciMapListIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 13, 3, 1, 1),
    _VmtVpciMapListIndex_Type()
)
vmtVpciMapListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmtVpciMapListIndex.setStatus("current")
_VmtVpciMapListMEIndex_Type = Integer32
_VmtVpciMapListMEIndex_Object = MibTableColumn
vmtVpciMapListMEIndex = _VmtVpciMapListMEIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 13, 3, 1, 2),
    _VmtVpciMapListMEIndex_Type()
)
vmtVpciMapListMEIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmtVpciMapListMEIndex.setStatus("current")
_VmtVpciMapListStatus_Type = RowStatus
_VmtVpciMapListStatus_Object = MibTableColumn
vmtVpciMapListStatus = _VmtVpciMapListStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 13, 3, 1, 3),
    _VmtVpciMapListStatus_Type()
)
vmtVpciMapListStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmtVpciMapListStatus.setStatus("current")
_PnniSpvxcRGroupTable_Object = MibTable
pnniSpvxcRGroupTable = _PnniSpvxcRGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 14)
)
if mibBuilder.loadTexts:
    pnniSpvxcRGroupTable.setStatus("current")
_PnniSpvxcRGroupEntry_Object = MibTableRow
pnniSpvxcRGroupEntry = _PnniSpvxcRGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 14, 1)
)
pnniSpvxcRGroupEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "pnniSpvxcRGroupIndex"),
)
if mibBuilder.loadTexts:
    pnniSpvxcRGroupEntry.setStatus("current")


class _PnniSpvxcRGroupIndex_Type(Integer32):
    """Custom type pnniSpvxcRGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PnniSpvxcRGroupIndex_Type.__name__ = "Integer32"
_PnniSpvxcRGroupIndex_Object = MibTableColumn
pnniSpvxcRGroupIndex = _PnniSpvxcRGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 14, 1, 1),
    _PnniSpvxcRGroupIndex_Type()
)
pnniSpvxcRGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniSpvxcRGroupIndex.setStatus("current")
_PnniSpvxcRGroupPrimaryPort_Type = Integer32
_PnniSpvxcRGroupPrimaryPort_Object = MibTableColumn
pnniSpvxcRGroupPrimaryPort = _PnniSpvxcRGroupPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 14, 1, 2),
    _PnniSpvxcRGroupPrimaryPort_Type()
)
pnniSpvxcRGroupPrimaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSpvxcRGroupPrimaryPort.setStatus("current")
_PnniSpvxcRGroupSecondaryPort_Type = Integer32
_PnniSpvxcRGroupSecondaryPort_Object = MibTableColumn
pnniSpvxcRGroupSecondaryPort = _PnniSpvxcRGroupSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 14, 1, 3),
    _PnniSpvxcRGroupSecondaryPort_Type()
)
pnniSpvxcRGroupSecondaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSpvxcRGroupSecondaryPort.setStatus("current")
_PnniSpvxcRGroupNsapAddr_Type = NsapAddr
_PnniSpvxcRGroupNsapAddr_Object = MibTableColumn
pnniSpvxcRGroupNsapAddr = _PnniSpvxcRGroupNsapAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 14, 1, 4),
    _PnniSpvxcRGroupNsapAddr_Type()
)
pnniSpvxcRGroupNsapAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvxcRGroupNsapAddr.setStatus("current")


class _PnniSpvxcRGroupSwitchoverCmd_Type(Integer32):
    """Custom type pnniSpvxcRGroupSwitchoverCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switch2primary", 1),
          ("switch2secondary", 2))
    )


_PnniSpvxcRGroupSwitchoverCmd_Type.__name__ = "Integer32"
_PnniSpvxcRGroupSwitchoverCmd_Object = MibTableColumn
pnniSpvxcRGroupSwitchoverCmd = _PnniSpvxcRGroupSwitchoverCmd_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 14, 1, 5),
    _PnniSpvxcRGroupSwitchoverCmd_Type()
)
pnniSpvxcRGroupSwitchoverCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSpvxcRGroupSwitchoverCmd.setStatus("current")
_PnniSpvxcRGroupActivePort_Type = Integer32
_PnniSpvxcRGroupActivePort_Object = MibTableColumn
pnniSpvxcRGroupActivePort = _PnniSpvxcRGroupActivePort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 14, 1, 6),
    _PnniSpvxcRGroupActivePort_Type()
)
pnniSpvxcRGroupActivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvxcRGroupActivePort.setStatus("current")
_PnniSpvxcRGroupPacingNumber_Type = Integer32
_PnniSpvxcRGroupPacingNumber_Object = MibTableColumn
pnniSpvxcRGroupPacingNumber = _PnniSpvxcRGroupPacingNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 14, 1, 7),
    _PnniSpvxcRGroupPacingNumber_Type()
)
pnniSpvxcRGroupPacingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSpvxcRGroupPacingNumber.setStatus("current")
_PnniSpvxcRGroupPacingInterval_Type = Integer32
_PnniSpvxcRGroupPacingInterval_Object = MibTableColumn
pnniSpvxcRGroupPacingInterval = _PnniSpvxcRGroupPacingInterval_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 14, 1, 8),
    _PnniSpvxcRGroupPacingInterval_Type()
)
pnniSpvxcRGroupPacingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSpvxcRGroupPacingInterval.setStatus("current")


class _PnniSpvxcRGroupAutoPVCSwitchover_Type(Integer32):
    """Custom type pnniSpvxcRGroupAutoPVCSwitchover based on Integer32"""
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


_PnniSpvxcRGroupAutoPVCSwitchover_Type.__name__ = "Integer32"
_PnniSpvxcRGroupAutoPVCSwitchover_Object = MibTableColumn
pnniSpvxcRGroupAutoPVCSwitchover = _PnniSpvxcRGroupAutoPVCSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 14, 1, 9),
    _PnniSpvxcRGroupAutoPVCSwitchover_Type()
)
pnniSpvxcRGroupAutoPVCSwitchover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSpvxcRGroupAutoPVCSwitchover.setStatus("current")


class _PnniSpvxcRGroupName_Type(OctetString):
    """Custom type pnniSpvxcRGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PnniSpvxcRGroupName_Type.__name__ = "OctetString"
_PnniSpvxcRGroupName_Object = MibTableColumn
pnniSpvxcRGroupName = _PnniSpvxcRGroupName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 14, 1, 10),
    _PnniSpvxcRGroupName_Type()
)
pnniSpvxcRGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSpvxcRGroupName.setStatus("current")


class _PnniSpvxcRGroupState_Type(Integer32):
    """Custom type pnniSpvxcRGroupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("operational", 1),
          ("switchoverInProgress", 2))
    )


_PnniSpvxcRGroupState_Type.__name__ = "Integer32"
_PnniSpvxcRGroupState_Object = MibTableColumn
pnniSpvxcRGroupState = _PnniSpvxcRGroupState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 14, 1, 11),
    _PnniSpvxcRGroupState_Type()
)
pnniSpvxcRGroupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpvxcRGroupState.setStatus("current")
_PnniSpvxcRGroupRowStatus_Type = RowStatus
_PnniSpvxcRGroupRowStatus_Object = MibTableColumn
pnniSpvxcRGroupRowStatus = _PnniSpvxcRGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 14, 1, 12),
    _PnniSpvxcRGroupRowStatus_Type()
)
pnniSpvxcRGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniSpvxcRGroupRowStatus.setStatus("current")
_ProxyDirMapEntryGroup_ObjectIdentity = ObjectIdentity
proxyDirMapEntryGroup = _ProxyDirMapEntryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 15)
)
_ProxyDirMapEntryTable_Object = MibTable
proxyDirMapEntryTable = _ProxyDirMapEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 15, 1)
)
if mibBuilder.loadTexts:
    proxyDirMapEntryTable.setStatus("current")
_ProxyDirMapEntry_Object = MibTableRow
proxyDirMapEntry = _ProxyDirMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 15, 1, 1)
)
proxyDirMapEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "proxyDirMapIndex"),
)
if mibBuilder.loadTexts:
    proxyDirMapEntry.setStatus("current")


class _ProxyDirMapIndex_Type(Integer32):
    """Custom type proxyDirMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99999),
    )


_ProxyDirMapIndex_Type.__name__ = "Integer32"
_ProxyDirMapIndex_Object = MibTableColumn
proxyDirMapIndex = _ProxyDirMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 15, 1, 1, 1),
    _ProxyDirMapIndex_Type()
)
proxyDirMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    proxyDirMapIndex.setStatus("current")
_ProxyDirMapAESA_Type = OctetString
_ProxyDirMapAESA_Object = MibTableColumn
proxyDirMapAESA = _ProxyDirMapAESA_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 15, 1, 1, 2),
    _ProxyDirMapAESA_Type()
)
proxyDirMapAESA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proxyDirMapAESA.setStatus("current")
_ProxyDirMapGroup_Type = Integer32
_ProxyDirMapGroup_Object = MibTableColumn
proxyDirMapGroup = _ProxyDirMapGroup_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 15, 1, 1, 3),
    _ProxyDirMapGroup_Type()
)
proxyDirMapGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proxyDirMapGroup.setStatus("current")
_ProxyDirMapVPCI_Type = Integer32
_ProxyDirMapVPCI_Object = MibTableColumn
proxyDirMapVPCI = _ProxyDirMapVPCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 15, 1, 1, 4),
    _ProxyDirMapVPCI_Type()
)
proxyDirMapVPCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proxyDirMapVPCI.setStatus("current")
_ProxyDirMapStatus_Type = RowStatus
_ProxyDirMapStatus_Object = MibTableColumn
proxyDirMapStatus = _ProxyDirMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 15, 1, 1, 5),
    _ProxyDirMapStatus_Type()
)
proxyDirMapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proxyDirMapStatus.setStatus("current")
_ProxyDirMapVp_Type = Integer32
_ProxyDirMapVp_Object = MibTableColumn
proxyDirMapVp = _ProxyDirMapVp_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 15, 1, 1, 6),
    _ProxyDirMapVp_Type()
)
proxyDirMapVp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyDirMapVp.setStatus("current")
_ProxyDirMapPort_Type = Integer32
_ProxyDirMapPort_Object = MibTableColumn
proxyDirMapPort = _ProxyDirMapPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 15, 1, 1, 7),
    _ProxyDirMapPort_Type()
)
proxyDirMapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyDirMapPort.setStatus("current")
_ProxyDirGroupGroup_ObjectIdentity = ObjectIdentity
proxyDirGroupGroup = _ProxyDirGroupGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 16)
)
_ProxyDirGroupTable_Object = MibTable
proxyDirGroupTable = _ProxyDirGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 16, 1)
)
if mibBuilder.loadTexts:
    proxyDirGroupTable.setStatus("current")
_ProxyDirGroupEntry_Object = MibTableRow
proxyDirGroupEntry = _ProxyDirGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 16, 1, 1)
)
proxyDirGroupEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "proxyDirGroupIndex"),
)
if mibBuilder.loadTexts:
    proxyDirGroupEntry.setStatus("current")


class _ProxyDirGroupIndex_Type(Integer32):
    """Custom type proxyDirGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99999),
    )


_ProxyDirGroupIndex_Type.__name__ = "Integer32"
_ProxyDirGroupIndex_Object = MibTableColumn
proxyDirGroupIndex = _ProxyDirGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 16, 1, 1, 1),
    _ProxyDirGroupIndex_Type()
)
proxyDirGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    proxyDirGroupIndex.setStatus("current")
_ProxyDirGroupPrefix_Type = Integer32
_ProxyDirGroupPrefix_Object = MibTableColumn
proxyDirGroupPrefix = _ProxyDirGroupPrefix_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 16, 1, 1, 2),
    _ProxyDirGroupPrefix_Type()
)
proxyDirGroupPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proxyDirGroupPrefix.setStatus("current")
_ProxyDirGroupVPCIGroup_Type = Integer32
_ProxyDirGroupVPCIGroup_Object = MibTableColumn
proxyDirGroupVPCIGroup = _ProxyDirGroupVPCIGroup_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 16, 1, 1, 3),
    _ProxyDirGroupVPCIGroup_Type()
)
proxyDirGroupVPCIGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proxyDirGroupVPCIGroup.setStatus("current")
_ProxyDirGroupStatus_Type = RowStatus
_ProxyDirGroupStatus_Object = MibTableColumn
proxyDirGroupStatus = _ProxyDirGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 6, 2, 16, 1, 1, 4),
    _ProxyDirGroupStatus_Type()
)
proxyDirGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proxyDirGroupStatus.setStatus("current")
_SwBoardGroup_ObjectIdentity = ObjectIdentity
swBoardGroup = _SwBoardGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 7)
)
_SwBoardTable_Object = MibTable
swBoardTable = _SwBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    swBoardTable.setStatus("current")
_SwBoardEntry_Object = MibTableRow
swBoardEntry = _SwBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 7, 1, 1)
)
swBoardEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "swBoardIndex"),
)
if mibBuilder.loadTexts:
    swBoardEntry.setStatus("current")
_SwBoardIndex_Type = Integer32
_SwBoardIndex_Object = MibTableColumn
swBoardIndex = _SwBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 7, 1, 1, 1),
    _SwBoardIndex_Type()
)
swBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBoardIndex.setStatus("current")
_SwBoardMaxPaths_Type = Integer32
_SwBoardMaxPaths_Object = MibTableColumn
swBoardMaxPaths = _SwBoardMaxPaths_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 7, 1, 1, 2),
    _SwBoardMaxPaths_Type()
)
swBoardMaxPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBoardMaxPaths.setStatus("current")
_SwBoardMaxChannels_Type = Integer32
_SwBoardMaxChannels_Object = MibTableColumn
swBoardMaxChannels = _SwBoardMaxChannels_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 7, 1, 1, 3),
    _SwBoardMaxChannels_Type()
)
swBoardMaxChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBoardMaxChannels.setStatus("current")
_SwBoardAtmAddress_Type = SpansAddress
_SwBoardAtmAddress_Object = MibTableColumn
swBoardAtmAddress = _SwBoardAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 7, 1, 1, 4),
    _SwBoardAtmAddress_Type()
)
swBoardAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBoardAtmAddress.setStatus("current")
_SwBoardUptime_Type = TimeTicks
_SwBoardUptime_Object = MibTableColumn
swBoardUptime = _SwBoardUptime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 7, 1, 1, 5),
    _SwBoardUptime_Type()
)
swBoardUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBoardUptime.setStatus("current")
_SwBoardCDV_Type = Integer32
_SwBoardCDV_Object = MibTableColumn
swBoardCDV = _SwBoardCDV_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 7, 1, 1, 6),
    _SwBoardCDV_Type()
)
swBoardCDV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swBoardCDV.setStatus("deprecated")


class _SwBoardPolicingAction_Type(Integer32):
    """Custom type swBoardPolicingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("tag", 1))
    )


_SwBoardPolicingAction_Type.__name__ = "Integer32"
_SwBoardPolicingAction_Object = MibTableColumn
swBoardPolicingAction = _SwBoardPolicingAction_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 7, 1, 1, 7),
    _SwBoardPolicingAction_Type()
)
swBoardPolicingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swBoardPolicingAction.setStatus("deprecated")
_SwBoardNsapPrefix_Type = NsapPrefix
_SwBoardNsapPrefix_Object = MibTableColumn
swBoardNsapPrefix = _SwBoardNsapPrefix_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 7, 1, 1, 8),
    _SwBoardNsapPrefix_Type()
)
swBoardNsapPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swBoardNsapPrefix.setStatus("current")
_SwBoardClockScalingFactor_Type = Integer32
_SwBoardClockScalingFactor_Object = MibTableColumn
swBoardClockScalingFactor = _SwBoardClockScalingFactor_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 7, 1, 1, 9),
    _SwBoardClockScalingFactor_Type()
)
swBoardClockScalingFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swBoardClockScalingFactor.setStatus("current")


class _SwBoardDebugMode_Type(Integer32):
    """Custom type swBoardDebugMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_SwBoardDebugMode_Type.__name__ = "Integer32"
_SwBoardDebugMode_Object = MibTableColumn
swBoardDebugMode = _SwBoardDebugMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 7, 1, 1, 10),
    _SwBoardDebugMode_Type()
)
swBoardDebugMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swBoardDebugMode.setStatus("current")


class _SwBoardMulticastMode_Type(Integer32):
    """Custom type swBoardMulticastMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extended", 2),
          ("non-extended", 1))
    )


_SwBoardMulticastMode_Type.__name__ = "Integer32"
_SwBoardMulticastMode_Object = MibTableColumn
swBoardMulticastMode = _SwBoardMulticastMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 7, 1, 1, 11),
    _SwBoardMulticastMode_Type()
)
swBoardMulticastMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBoardMulticastMode.setStatus("current")


class _SwBoardFingerMode_Type(Integer32):
    """Custom type swBoardFingerMode based on Integer32"""
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


_SwBoardFingerMode_Type.__name__ = "Integer32"
_SwBoardFingerMode_Object = MibTableColumn
swBoardFingerMode = _SwBoardFingerMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 7, 1, 1, 12),
    _SwBoardFingerMode_Type()
)
swBoardFingerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swBoardFingerMode.setStatus("current")


class _SwBoardATMLayerOAM_Type(Integer32):
    """Custom type swBoardATMLayerOAM based on Integer32"""
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


_SwBoardATMLayerOAM_Type.__name__ = "Integer32"
_SwBoardATMLayerOAM_Object = MibTableColumn
swBoardATMLayerOAM = _SwBoardATMLayerOAM_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 7, 1, 1, 13),
    _SwBoardATMLayerOAM_Type()
)
swBoardATMLayerOAM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swBoardATMLayerOAM.setStatus("deprecated")
_SwBoardTopologyGroup_ObjectIdentity = ObjectIdentity
swBoardTopologyGroup = _SwBoardTopologyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 8)
)
_SwBoardTopoTable_Object = MibTable
swBoardTopoTable = _SwBoardTopoTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    swBoardTopoTable.setStatus("current")
_SwBoardTopoEntry_Object = MibTableRow
swBoardTopoEntry = _SwBoardTopoEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 8, 1, 1)
)
swBoardTopoEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "swBoardTopoIndex"),
)
if mibBuilder.loadTexts:
    swBoardTopoEntry.setStatus("current")
_SwBoardTopoIndex_Type = Integer32
_SwBoardTopoIndex_Object = MibTableColumn
swBoardTopoIndex = _SwBoardTopoIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 8, 1, 1, 1),
    _SwBoardTopoIndex_Type()
)
swBoardTopoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBoardTopoIndex.setStatus("current")
_SwBoardTopoNumberOfLinks_Type = Integer32
_SwBoardTopoNumberOfLinks_Object = MibTableColumn
swBoardTopoNumberOfLinks = _SwBoardTopoNumberOfLinks_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 8, 1, 1, 2),
    _SwBoardTopoNumberOfLinks_Type()
)
swBoardTopoNumberOfLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBoardTopoNumberOfLinks.setStatus("current")
_SwBoardLinkTable_Object = MibTable
swBoardLinkTable = _SwBoardLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 8, 2)
)
if mibBuilder.loadTexts:
    swBoardLinkTable.setStatus("current")
_SwBoardLinkEntry_Object = MibTableRow
swBoardLinkEntry = _SwBoardLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 8, 2, 1)
)
swBoardLinkEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "swBoardLinkIndex"),
    (0, "Fore-Switch-MIB", "swBoardLinkSrc"),
    (0, "Fore-Switch-MIB", "swBoardLinkDest"),
)
if mibBuilder.loadTexts:
    swBoardLinkEntry.setStatus("current")
_SwBoardLinkIndex_Type = Integer32
_SwBoardLinkIndex_Object = MibTableColumn
swBoardLinkIndex = _SwBoardLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 8, 2, 1, 1),
    _SwBoardLinkIndex_Type()
)
swBoardLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBoardLinkIndex.setStatus("current")
_SwBoardLinkSrc_Type = SpansAddress
_SwBoardLinkSrc_Object = MibTableColumn
swBoardLinkSrc = _SwBoardLinkSrc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 8, 2, 1, 2),
    _SwBoardLinkSrc_Type()
)
swBoardLinkSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBoardLinkSrc.setStatus("current")
_SwBoardLinkDest_Type = SpansAddress
_SwBoardLinkDest_Object = MibTableColumn
swBoardLinkDest = _SwBoardLinkDest_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 8, 2, 1, 3),
    _SwBoardLinkDest_Type()
)
swBoardLinkDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBoardLinkDest.setStatus("current")
_SwBoardLinkCapacity_Type = Integer32
_SwBoardLinkCapacity_Object = MibTableColumn
swBoardLinkCapacity = _SwBoardLinkCapacity_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 8, 2, 1, 4),
    _SwBoardLinkCapacity_Type()
)
swBoardLinkCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBoardLinkCapacity.setStatus("current")
_SwBoardLinkAge_Type = Integer32
_SwBoardLinkAge_Object = MibTableColumn
swBoardLinkAge = _SwBoardLinkAge_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 8, 2, 1, 5),
    _SwBoardLinkAge_Type()
)
swBoardLinkAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBoardLinkAge.setStatus("current")
_NsapGroup_ObjectIdentity = ObjectIdentity
nsapGroup = _NsapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9)
)
_NsapNetworkPrefixTable_Object = MibTable
nsapNetworkPrefixTable = _NsapNetworkPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 1)
)
if mibBuilder.loadTexts:
    nsapNetworkPrefixTable.setStatus("current")
_NsapNetworkPrefixEntry_Object = MibTableRow
nsapNetworkPrefixEntry = _NsapNetworkPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 1, 1)
)
nsapNetworkPrefixEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "nsapNetworkPrefixPort"),
    (0, "Fore-Switch-MIB", "nsapNetworkPrefixVPI"),
    (0, "Fore-Switch-MIB", "nsapNetworkPrefixValue"),
)
if mibBuilder.loadTexts:
    nsapNetworkPrefixEntry.setStatus("current")
_NsapNetworkPrefixPort_Type = Integer32
_NsapNetworkPrefixPort_Object = MibTableColumn
nsapNetworkPrefixPort = _NsapNetworkPrefixPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 1, 1, 1),
    _NsapNetworkPrefixPort_Type()
)
nsapNetworkPrefixPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsapNetworkPrefixPort.setStatus("current")
_NsapNetworkPrefixVPI_Type = Integer32
_NsapNetworkPrefixVPI_Object = MibTableColumn
nsapNetworkPrefixVPI = _NsapNetworkPrefixVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 1, 1, 2),
    _NsapNetworkPrefixVPI_Type()
)
nsapNetworkPrefixVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsapNetworkPrefixVPI.setStatus("current")
_NsapNetworkPrefixValue_Type = NsapPrefix
_NsapNetworkPrefixValue_Object = MibTableColumn
nsapNetworkPrefixValue = _NsapNetworkPrefixValue_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 1, 1, 3),
    _NsapNetworkPrefixValue_Type()
)
nsapNetworkPrefixValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsapNetworkPrefixValue.setStatus("current")
_NsapNetworkPrefixStatus_Type = EntryStatus
_NsapNetworkPrefixStatus_Object = MibTableColumn
nsapNetworkPrefixStatus = _NsapNetworkPrefixStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 1, 1, 4),
    _NsapNetworkPrefixStatus_Type()
)
nsapNetworkPrefixStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsapNetworkPrefixStatus.setStatus("current")
_NsapTopologyTable_Object = MibTable
nsapTopologyTable = _NsapTopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 3)
)
if mibBuilder.loadTexts:
    nsapTopologyTable.setStatus("current")
_NsapTopologyEntry_Object = MibTableRow
nsapTopologyEntry = _NsapTopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 3, 1)
)
nsapTopologyEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "nsapTopoBoard"),
    (0, "Fore-Switch-MIB", "nsapTopoLinkSrc"),
    (0, "Fore-Switch-MIB", "nsapTopoLinkSrcMask"),
    (0, "Fore-Switch-MIB", "nsapTopoLinkSrcPort"),
    (0, "Fore-Switch-MIB", "nsapTopoLinkSrcVpi"),
    (0, "Fore-Switch-MIB", "nsapTopoLinkDest"),
    (0, "Fore-Switch-MIB", "nsapTopoLinkDestMask"),
    (0, "Fore-Switch-MIB", "nsapTopoLinkDestPort"),
    (0, "Fore-Switch-MIB", "nsapTopoLinkDestVpi"),
)
if mibBuilder.loadTexts:
    nsapTopologyEntry.setStatus("current")
_NsapTopoBoard_Type = Integer32
_NsapTopoBoard_Object = MibTableColumn
nsapTopoBoard = _NsapTopoBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 3, 1, 1),
    _NsapTopoBoard_Type()
)
nsapTopoBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsapTopoBoard.setStatus("current")
_NsapTopoLinkSrc_Type = NsapAddr
_NsapTopoLinkSrc_Object = MibTableColumn
nsapTopoLinkSrc = _NsapTopoLinkSrc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 3, 1, 2),
    _NsapTopoLinkSrc_Type()
)
nsapTopoLinkSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsapTopoLinkSrc.setStatus("current")
_NsapTopoLinkSrcMask_Type = Integer32
_NsapTopoLinkSrcMask_Object = MibTableColumn
nsapTopoLinkSrcMask = _NsapTopoLinkSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 3, 1, 3),
    _NsapTopoLinkSrcMask_Type()
)
nsapTopoLinkSrcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsapTopoLinkSrcMask.setStatus("current")
_NsapTopoLinkSrcPort_Type = Integer32
_NsapTopoLinkSrcPort_Object = MibTableColumn
nsapTopoLinkSrcPort = _NsapTopoLinkSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 3, 1, 4),
    _NsapTopoLinkSrcPort_Type()
)
nsapTopoLinkSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsapTopoLinkSrcPort.setStatus("current")
_NsapTopoLinkSrcVpi_Type = Integer32
_NsapTopoLinkSrcVpi_Object = MibTableColumn
nsapTopoLinkSrcVpi = _NsapTopoLinkSrcVpi_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 3, 1, 5),
    _NsapTopoLinkSrcVpi_Type()
)
nsapTopoLinkSrcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsapTopoLinkSrcVpi.setStatus("current")
_NsapTopoLinkDest_Type = NsapAddr
_NsapTopoLinkDest_Object = MibTableColumn
nsapTopoLinkDest = _NsapTopoLinkDest_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 3, 1, 6),
    _NsapTopoLinkDest_Type()
)
nsapTopoLinkDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsapTopoLinkDest.setStatus("current")
_NsapTopoLinkDestMask_Type = Integer32
_NsapTopoLinkDestMask_Object = MibTableColumn
nsapTopoLinkDestMask = _NsapTopoLinkDestMask_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 3, 1, 7),
    _NsapTopoLinkDestMask_Type()
)
nsapTopoLinkDestMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsapTopoLinkDestMask.setStatus("current")
_NsapTopoLinkDestPort_Type = Integer32
_NsapTopoLinkDestPort_Object = MibTableColumn
nsapTopoLinkDestPort = _NsapTopoLinkDestPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 3, 1, 8),
    _NsapTopoLinkDestPort_Type()
)
nsapTopoLinkDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsapTopoLinkDestPort.setStatus("current")
_NsapTopoLinkDestVpi_Type = Integer32
_NsapTopoLinkDestVpi_Object = MibTableColumn
nsapTopoLinkDestVpi = _NsapTopoLinkDestVpi_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 3, 1, 9),
    _NsapTopoLinkDestVpi_Type()
)
nsapTopoLinkDestVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsapTopoLinkDestVpi.setStatus("current")
_NsapTopoLinkCost_Type = Integer32
_NsapTopoLinkCost_Object = MibTableColumn
nsapTopoLinkCost = _NsapTopoLinkCost_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 3, 1, 10),
    _NsapTopoLinkCost_Type()
)
nsapTopoLinkCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsapTopoLinkCost.setStatus("current")
_NsapTopoLinkUbrVCs_Type = Gauge32
_NsapTopoLinkUbrVCs_Object = MibTableColumn
nsapTopoLinkUbrVCs = _NsapTopoLinkUbrVCs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 3, 1, 11),
    _NsapTopoLinkUbrVCs_Type()
)
nsapTopoLinkUbrVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsapTopoLinkUbrVCs.setStatus("deprecated")
_NsapTopoLinkCbrCapacity_Type = Integer32
_NsapTopoLinkCbrCapacity_Object = MibTableColumn
nsapTopoLinkCbrCapacity = _NsapTopoLinkCbrCapacity_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 3, 1, 12),
    _NsapTopoLinkCbrCapacity_Type()
)
nsapTopoLinkCbrCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsapTopoLinkCbrCapacity.setStatus("current")
_NsapTopoLinkCbrFifo_Type = Integer32
_NsapTopoLinkCbrFifo_Object = MibTableColumn
nsapTopoLinkCbrFifo = _NsapTopoLinkCbrFifo_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 3, 1, 13),
    _NsapTopoLinkCbrFifo_Type()
)
nsapTopoLinkCbrFifo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsapTopoLinkCbrFifo.setStatus("current")
_NsapTopoLinkVbrCapacity_Type = Integer32
_NsapTopoLinkVbrCapacity_Object = MibTableColumn
nsapTopoLinkVbrCapacity = _NsapTopoLinkVbrCapacity_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 3, 1, 14),
    _NsapTopoLinkVbrCapacity_Type()
)
nsapTopoLinkVbrCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsapTopoLinkVbrCapacity.setStatus("current")
_NsapTopoLinkVbrFifo_Type = Integer32
_NsapTopoLinkVbrFifo_Object = MibTableColumn
nsapTopoLinkVbrFifo = _NsapTopoLinkVbrFifo_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 3, 1, 15),
    _NsapTopoLinkVbrFifo_Type()
)
nsapTopoLinkVbrFifo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsapTopoLinkVbrFifo.setStatus("current")


class _NsapTopoLinkOrig_Type(Integer32):
    """Custom type nsapTopoLinkOrig based on Integer32"""
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
        *(("external", 5),
          ("ilmi-registered", 3),
          ("pnni", 4),
          ("spans-pnni", 2),
          ("static-route", 1))
    )


_NsapTopoLinkOrig_Type.__name__ = "Integer32"
_NsapTopoLinkOrig_Object = MibTableColumn
nsapTopoLinkOrig = _NsapTopoLinkOrig_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 3, 1, 16),
    _NsapTopoLinkOrig_Type()
)
nsapTopoLinkOrig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsapTopoLinkOrig.setStatus("current")
_NsapTopoLinkCapabilitySet_Type = Integer32
_NsapTopoLinkCapabilitySet_Object = MibTableColumn
nsapTopoLinkCapabilitySet = _NsapTopoLinkCapabilitySet_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 3, 1, 17),
    _NsapTopoLinkCapabilitySet_Type()
)
nsapTopoLinkCapabilitySet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsapTopoLinkCapabilitySet.setStatus("current")
_NsapTopoLinkFreshness_Type = Integer32
_NsapTopoLinkFreshness_Object = MibTableColumn
nsapTopoLinkFreshness = _NsapTopoLinkFreshness_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 3, 1, 18),
    _NsapTopoLinkFreshness_Type()
)
nsapTopoLinkFreshness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsapTopoLinkFreshness.setStatus("current")
_NsapTopoLinkUbrEstimatedBandwidth_Type = Integer32
_NsapTopoLinkUbrEstimatedBandwidth_Object = MibTableColumn
nsapTopoLinkUbrEstimatedBandwidth = _NsapTopoLinkUbrEstimatedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 3, 1, 19),
    _NsapTopoLinkUbrEstimatedBandwidth_Type()
)
nsapTopoLinkUbrEstimatedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsapTopoLinkUbrEstimatedBandwidth.setStatus("current")
_NsapStaticRouteTable_Object = MibTable
nsapStaticRouteTable = _NsapStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 4)
)
if mibBuilder.loadTexts:
    nsapStaticRouteTable.setStatus("current")
_NsapStaticRouteEntry_Object = MibTableRow
nsapStaticRouteEntry = _NsapStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 4, 1)
)
nsapStaticRouteEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "nsapStaticRouteAddress"),
    (0, "Fore-Switch-MIB", "nsapStaticRouteMask"),
    (0, "Fore-Switch-MIB", "nsapStaticRoutePort"),
    (0, "Fore-Switch-MIB", "nsapStaticRouteVPI"),
)
if mibBuilder.loadTexts:
    nsapStaticRouteEntry.setStatus("current")
_NsapStaticRouteAddress_Type = NsapAddr
_NsapStaticRouteAddress_Object = MibTableColumn
nsapStaticRouteAddress = _NsapStaticRouteAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 4, 1, 1),
    _NsapStaticRouteAddress_Type()
)
nsapStaticRouteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsapStaticRouteAddress.setStatus("current")
_NsapStaticRouteMask_Type = Integer32
_NsapStaticRouteMask_Object = MibTableColumn
nsapStaticRouteMask = _NsapStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 4, 1, 2),
    _NsapStaticRouteMask_Type()
)
nsapStaticRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsapStaticRouteMask.setStatus("current")
_NsapStaticRoutePort_Type = Integer32
_NsapStaticRoutePort_Object = MibTableColumn
nsapStaticRoutePort = _NsapStaticRoutePort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 4, 1, 3),
    _NsapStaticRoutePort_Type()
)
nsapStaticRoutePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsapStaticRoutePort.setStatus("current")
_NsapStaticRouteVPI_Type = Integer32
_NsapStaticRouteVPI_Object = MibTableColumn
nsapStaticRouteVPI = _NsapStaticRouteVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 4, 1, 4),
    _NsapStaticRouteVPI_Type()
)
nsapStaticRouteVPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsapStaticRouteVPI.setStatus("current")
_NsapStaticRouteCost_Type = Integer32
_NsapStaticRouteCost_Object = MibTableColumn
nsapStaticRouteCost = _NsapStaticRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 4, 1, 5),
    _NsapStaticRouteCost_Type()
)
nsapStaticRouteCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsapStaticRouteCost.setStatus("current")
_NsapStaticRouteMaxCbrCap_Type = Integer32
_NsapStaticRouteMaxCbrCap_Object = MibTableColumn
nsapStaticRouteMaxCbrCap = _NsapStaticRouteMaxCbrCap_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 4, 1, 6),
    _NsapStaticRouteMaxCbrCap_Type()
)
nsapStaticRouteMaxCbrCap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsapStaticRouteMaxCbrCap.setStatus("current")
_NsapStaticRouteMaxVbrCap_Type = Integer32
_NsapStaticRouteMaxVbrCap_Object = MibTableColumn
nsapStaticRouteMaxVbrCap = _NsapStaticRouteMaxVbrCap_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 4, 1, 7),
    _NsapStaticRouteMaxVbrCap_Type()
)
nsapStaticRouteMaxVbrCap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsapStaticRouteMaxVbrCap.setStatus("current")


class _NsapStaticRouteAbrSupport_Type(Integer32):
    """Custom type nsapStaticRouteAbrSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_NsapStaticRouteAbrSupport_Type.__name__ = "Integer32"
_NsapStaticRouteAbrSupport_Object = MibTableColumn
nsapStaticRouteAbrSupport = _NsapStaticRouteAbrSupport_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 4, 1, 8),
    _NsapStaticRouteAbrSupport_Type()
)
nsapStaticRouteAbrSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsapStaticRouteAbrSupport.setStatus("current")


class _NsapStaticRouteEpdSupport_Type(Integer32):
    """Custom type nsapStaticRouteEpdSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_NsapStaticRouteEpdSupport_Type.__name__ = "Integer32"
_NsapStaticRouteEpdSupport_Object = MibTableColumn
nsapStaticRouteEpdSupport = _NsapStaticRouteEpdSupport_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 4, 1, 9),
    _NsapStaticRouteEpdSupport_Type()
)
nsapStaticRouteEpdSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsapStaticRouteEpdSupport.setStatus("current")
_NsapStaticRouteStatus_Type = EntryStatus
_NsapStaticRouteStatus_Object = MibTableColumn
nsapStaticRouteStatus = _NsapStaticRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 4, 1, 10),
    _NsapStaticRouteStatus_Type()
)
nsapStaticRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsapStaticRouteStatus.setStatus("current")
_FtPnniDTLTable_Object = MibTable
ftPnniDTLTable = _FtPnniDTLTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 5)
)
if mibBuilder.loadTexts:
    ftPnniDTLTable.setStatus("deprecated")
_FtPnniDTLEntry_Object = MibTableRow
ftPnniDTLEntry = _FtPnniDTLEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 5, 1)
)
ftPnniDTLEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "ftPnniDTLIndex"),
    (0, "Fore-Switch-MIB", "ftPnniDTLEntryIndex"),
)
if mibBuilder.loadTexts:
    ftPnniDTLEntry.setStatus("deprecated")
_FtPnniDTLIndex_Type = Integer32
_FtPnniDTLIndex_Object = MibTableColumn
ftPnniDTLIndex = _FtPnniDTLIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 5, 1, 1),
    _FtPnniDTLIndex_Type()
)
ftPnniDTLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftPnniDTLIndex.setStatus("deprecated")
_FtPnniDTLEntryIndex_Type = Integer32
_FtPnniDTLEntryIndex_Object = MibTableColumn
ftPnniDTLEntryIndex = _FtPnniDTLEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 5, 1, 2),
    _FtPnniDTLEntryIndex_Type()
)
ftPnniDTLEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftPnniDTLEntryIndex.setStatus("deprecated")
_FtPnniDTLNodePrefix_Type = NsapPrefix
_FtPnniDTLNodePrefix_Object = MibTableColumn
ftPnniDTLNodePrefix = _FtPnniDTLNodePrefix_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 5, 1, 3),
    _FtPnniDTLNodePrefix_Type()
)
ftPnniDTLNodePrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ftPnniDTLNodePrefix.setStatus("deprecated")


class _FtPnniDTLNodeMask_Type(Integer32):
    """Custom type ftPnniDTLNodeMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 104),
    )


_FtPnniDTLNodeMask_Type.__name__ = "Integer32"
_FtPnniDTLNodeMask_Object = MibTableColumn
ftPnniDTLNodeMask = _FtPnniDTLNodeMask_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 5, 1, 4),
    _FtPnniDTLNodeMask_Type()
)
ftPnniDTLNodeMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ftPnniDTLNodeMask.setStatus("deprecated")
_FtPnniDTLPort_Type = Integer32
_FtPnniDTLPort_Object = MibTableColumn
ftPnniDTLPort = _FtPnniDTLPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 5, 1, 5),
    _FtPnniDTLPort_Type()
)
ftPnniDTLPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ftPnniDTLPort.setStatus("deprecated")
_FtPnniDTLVPI_Type = Integer32
_FtPnniDTLVPI_Object = MibTableColumn
ftPnniDTLVPI = _FtPnniDTLVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 5, 1, 6),
    _FtPnniDTLVPI_Type()
)
ftPnniDTLVPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ftPnniDTLVPI.setStatus("deprecated")
_FtPnniDTLStatus_Type = EntryStatus
_FtPnniDTLStatus_Object = MibTableColumn
ftPnniDTLStatus = _FtPnniDTLStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 5, 1, 7),
    _FtPnniDTLStatus_Type()
)
ftPnniDTLStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ftPnniDTLStatus.setStatus("deprecated")
_FtPnniSummaryTable_Object = MibTable
ftPnniSummaryTable = _FtPnniSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 6)
)
if mibBuilder.loadTexts:
    ftPnniSummaryTable.setStatus("deprecated")
_FtPnniSummaryEntry_Object = MibTableRow
ftPnniSummaryEntry = _FtPnniSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 6, 1)
)
ftPnniSummaryEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "ftPnniSummaryAddress"),
    (0, "Fore-Switch-MIB", "ftPnniSummaryPrefixLength"),
)
if mibBuilder.loadTexts:
    ftPnniSummaryEntry.setStatus("deprecated")
_FtPnniSummaryAddress_Type = Integer32
_FtPnniSummaryAddress_Object = MibTableColumn
ftPnniSummaryAddress = _FtPnniSummaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 6, 1, 1),
    _FtPnniSummaryAddress_Type()
)
ftPnniSummaryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftPnniSummaryAddress.setStatus("deprecated")
_FtPnniSummaryPrefixLength_Type = Integer32
_FtPnniSummaryPrefixLength_Object = MibTableColumn
ftPnniSummaryPrefixLength = _FtPnniSummaryPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 6, 1, 2),
    _FtPnniSummaryPrefixLength_Type()
)
ftPnniSummaryPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftPnniSummaryPrefixLength.setStatus("deprecated")


class _FtPnniSummaryType_Type(Integer32):
    """Custom type ftPnniSummaryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exterior", 2),
          ("internal", 1))
    )


_FtPnniSummaryType_Type.__name__ = "Integer32"
_FtPnniSummaryType_Object = MibTableColumn
ftPnniSummaryType = _FtPnniSummaryType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 6, 1, 3),
    _FtPnniSummaryType_Type()
)
ftPnniSummaryType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ftPnniSummaryType.setStatus("deprecated")


class _FtPnniSummarySuppress_Type(Integer32):
    """Custom type ftPnniSummarySuppress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FtPnniSummarySuppress_Type.__name__ = "Integer32"
_FtPnniSummarySuppress_Object = MibTableColumn
ftPnniSummarySuppress = _FtPnniSummarySuppress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 6, 1, 4),
    _FtPnniSummarySuppress_Type()
)
ftPnniSummarySuppress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ftPnniSummarySuppress.setStatus("deprecated")


class _FtPnniSummaryState_Type(Integer32):
    """Custom type ftPnniSummaryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("advertising", 1),
          ("inactive", 3),
          ("suppressing", 2))
    )


_FtPnniSummaryState_Type.__name__ = "Integer32"
_FtPnniSummaryState_Object = MibTableColumn
ftPnniSummaryState = _FtPnniSummaryState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 6, 1, 5),
    _FtPnniSummaryState_Type()
)
ftPnniSummaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftPnniSummaryState.setStatus("deprecated")
_FtPnniSummaryStatus_Type = EntryStatus
_FtPnniSummaryStatus_Object = MibTableColumn
ftPnniSummaryStatus = _FtPnniSummaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 9, 6, 1, 6),
    _FtPnniSummaryStatus_Type()
)
ftPnniSummaryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ftPnniSummaryStatus.setStatus("deprecated")
_UpcContractGroup_ObjectIdentity = ObjectIdentity
upcContractGroup = _UpcContractGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10)
)
_UpcContractTable_Object = MibTable
upcContractTable = _UpcContractTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1)
)
if mibBuilder.loadTexts:
    upcContractTable.setStatus("current")
_UpcContractEntry_Object = MibTableRow
upcContractEntry = _UpcContractEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1)
)
upcContractEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "upcContractKey"),
)
if mibBuilder.loadTexts:
    upcContractEntry.setStatus("current")


class _UpcContractKey_Type(Integer32):
    """Custom type upcContractKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_UpcContractKey_Type.__name__ = "Integer32"
_UpcContractKey_Object = MibTableColumn
upcContractKey = _UpcContractKey_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1, 1),
    _UpcContractKey_Type()
)
upcContractKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upcContractKey.setStatus("current")
_UpcContractEntryStatus_Type = EntryStatus
_UpcContractEntryStatus_Object = MibTableColumn
upcContractEntryStatus = _UpcContractEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1, 2),
    _UpcContractEntryStatus_Type()
)
upcContractEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upcContractEntryStatus.setStatus("current")
_UpcContractPCR01_Type = Integer32
_UpcContractPCR01_Object = MibTableColumn
upcContractPCR01 = _UpcContractPCR01_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1, 3),
    _UpcContractPCR01_Type()
)
upcContractPCR01.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upcContractPCR01.setStatus("deprecated")
_UpcContractSCR01_Type = Integer32
_UpcContractSCR01_Object = MibTableColumn
upcContractSCR01 = _UpcContractSCR01_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1, 4),
    _UpcContractSCR01_Type()
)
upcContractSCR01.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upcContractSCR01.setStatus("deprecated")
_UpcContractMBS01_Type = Integer32
_UpcContractMBS01_Object = MibTableColumn
upcContractMBS01 = _UpcContractMBS01_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1, 5),
    _UpcContractMBS01_Type()
)
upcContractMBS01.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upcContractMBS01.setStatus("deprecated")
_UpcContractPCR0_Type = Integer32
_UpcContractPCR0_Object = MibTableColumn
upcContractPCR0 = _UpcContractPCR0_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1, 6),
    _UpcContractPCR0_Type()
)
upcContractPCR0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upcContractPCR0.setStatus("deprecated")
_UpcContractSCR0_Type = Integer32
_UpcContractSCR0_Object = MibTableColumn
upcContractSCR0 = _UpcContractSCR0_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1, 7),
    _UpcContractSCR0_Type()
)
upcContractSCR0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upcContractSCR0.setStatus("deprecated")
_UpcContractMBS0_Type = Integer32
_UpcContractMBS0_Object = MibTableColumn
upcContractMBS0 = _UpcContractMBS0_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1, 8),
    _UpcContractMBS0_Type()
)
upcContractMBS0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upcContractMBS0.setStatus("deprecated")
_UpcContractCDVT_Type = Integer32
_UpcContractCDVT_Object = MibTableColumn
upcContractCDVT = _UpcContractCDVT_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1, 9),
    _UpcContractCDVT_Type()
)
upcContractCDVT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upcContractCDVT.setStatus("current")
_UpcContractTagReq_Type = Integer32
_UpcContractTagReq_Object = MibTableColumn
upcContractTagReq = _UpcContractTagReq_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1, 10),
    _UpcContractTagReq_Type()
)
upcContractTagReq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upcContractTagReq.setStatus("deprecated")
_UpcContractAal5Epd_Type = Integer32
_UpcContractAal5Epd_Object = MibTableColumn
upcContractAal5Epd = _UpcContractAal5Epd_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1, 11),
    _UpcContractAal5Epd_Type()
)
upcContractAal5Epd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upcContractAal5Epd.setStatus("deprecated")


class _UpcContractName_Type(DisplayString):
    """Custom type upcContractName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_UpcContractName_Type.__name__ = "DisplayString"
_UpcContractName_Object = MibTableColumn
upcContractName = _UpcContractName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1, 12),
    _UpcContractName_Type()
)
upcContractName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upcContractName.setStatus("current")


class _UpcContractDoGCRAPolicing_Type(Integer32):
    """Custom type upcContractDoGCRAPolicing based on Integer32"""
    defaultValue = 1

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


_UpcContractDoGCRAPolicing_Type.__name__ = "Integer32"
_UpcContractDoGCRAPolicing_Object = MibTableColumn
upcContractDoGCRAPolicing = _UpcContractDoGCRAPolicing_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1, 13),
    _UpcContractDoGCRAPolicing_Type()
)
upcContractDoGCRAPolicing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upcContractDoGCRAPolicing.setStatus("current")


class _UpcContractIsAAL5_Type(Integer32):
    """Custom type upcContractIsAAL5 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_UpcContractIsAAL5_Type.__name__ = "Integer32"
_UpcContractIsAAL5_Object = MibTableColumn
upcContractIsAAL5 = _UpcContractIsAAL5_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1, 14),
    _UpcContractIsAAL5_Type()
)
upcContractIsAAL5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upcContractIsAAL5.setStatus("current")


class _UpcContractDoPacketDiscard_Type(Integer32):
    """Custom type upcContractDoPacketDiscard based on Integer32"""
    defaultValue = 1

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


_UpcContractDoPacketDiscard_Type.__name__ = "Integer32"
_UpcContractDoPacketDiscard_Object = MibTableColumn
upcContractDoPacketDiscard = _UpcContractDoPacketDiscard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1, 15),
    _UpcContractDoPacketDiscard_Type()
)
upcContractDoPacketDiscard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upcContractDoPacketDiscard.setStatus("current")


class _UpcContractDoPPPolicing_Type(Integer32):
    """Custom type upcContractDoPPPolicing based on Integer32"""
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


_UpcContractDoPPPolicing_Type.__name__ = "Integer32"
_UpcContractDoPPPolicing_Object = MibTableColumn
upcContractDoPPPolicing = _UpcContractDoPPPolicing_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1, 16),
    _UpcContractDoPPPolicing_Type()
)
upcContractDoPPPolicing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upcContractDoPPPolicing.setStatus("current")


class _UpcContractDoUBRTagging_Type(Integer32):
    """Custom type upcContractDoUBRTagging based on Integer32"""
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


_UpcContractDoUBRTagging_Type.__name__ = "Integer32"
_UpcContractDoUBRTagging_Object = MibTableColumn
upcContractDoUBRTagging = _UpcContractDoUBRTagging_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1, 17),
    _UpcContractDoUBRTagging_Type()
)
upcContractDoUBRTagging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upcContractDoUBRTagging.setStatus("deprecated")


class _UpcContractSchedMode_Type(AtmConnSchedMode):
    """Custom type upcContractSchedMode based on AtmConnSchedMode"""


_UpcContractSchedMode_Object = MibTableColumn
upcContractSchedMode = _UpcContractSchedMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1, 18),
    _UpcContractSchedMode_Type()
)
upcContractSchedMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upcContractSchedMode.setStatus("current")


class _UpcContractUseAltCLPThreshold_Type(Integer32):
    """Custom type upcContractUseAltCLPThreshold based on Integer32"""
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


_UpcContractUseAltCLPThreshold_Type.__name__ = "Integer32"
_UpcContractUseAltCLPThreshold_Object = MibTableColumn
upcContractUseAltCLPThreshold = _UpcContractUseAltCLPThreshold_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1, 19),
    _UpcContractUseAltCLPThreshold_Type()
)
upcContractUseAltCLPThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upcContractUseAltCLPThreshold.setStatus("current")
_UpcContractMCR_Type = Integer32
_UpcContractMCR_Object = MibTableColumn
upcContractMCR = _UpcContractMCR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1, 20),
    _UpcContractMCR_Type()
)
upcContractMCR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upcContractMCR.setStatus("current")
_UpcContractEstimatedUbrBandwidth_Type = Integer32
_UpcContractEstimatedUbrBandwidth_Object = MibTableColumn
upcContractEstimatedUbrBandwidth = _UpcContractEstimatedUbrBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1, 21),
    _UpcContractEstimatedUbrBandwidth_Type()
)
upcContractEstimatedUbrBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upcContractEstimatedUbrBandwidth.setStatus("current")


class _UpcContractAAL5CountingMode_Type(AAL5CountingMode):
    """Custom type upcContractAAL5CountingMode based on AAL5CountingMode"""


_UpcContractAAL5CountingMode_Object = MibTableColumn
upcContractAAL5CountingMode = _UpcContractAAL5CountingMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1, 22),
    _UpcContractAAL5CountingMode_Type()
)
upcContractAAL5CountingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upcContractAAL5CountingMode.setStatus("current")
_UpcContractServiceCategory_Type = Integer32
_UpcContractServiceCategory_Object = MibTableColumn
upcContractServiceCategory = _UpcContractServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1, 23),
    _UpcContractServiceCategory_Type()
)
upcContractServiceCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upcContractServiceCategory.setStatus("current")


class _UpcContractPoliceScheme_Type(Integer32):
    """Custom type upcContractPoliceScheme based on Integer32"""
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
        *(("abr1", 7),
          ("cbr0", 2),
          ("cbr0tag", 3),
          ("cbr1", 1),
          ("ubr1", 8),
          ("ubr2", 9),
          ("vbr1", 4),
          ("vbr2", 5),
          ("vbr3", 6))
    )


_UpcContractPoliceScheme_Type.__name__ = "Integer32"
_UpcContractPoliceScheme_Object = MibTableColumn
upcContractPoliceScheme = _UpcContractPoliceScheme_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1, 24),
    _UpcContractPoliceScheme_Type()
)
upcContractPoliceScheme.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upcContractPoliceScheme.setStatus("current")
_UpcContractPCR_Type = Integer32
_UpcContractPCR_Object = MibTableColumn
upcContractPCR = _UpcContractPCR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1, 25),
    _UpcContractPCR_Type()
)
upcContractPCR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upcContractPCR.setStatus("current")
_UpcContractSCR_Type = Integer32
_UpcContractSCR_Object = MibTableColumn
upcContractSCR = _UpcContractSCR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1, 26),
    _UpcContractSCR_Type()
)
upcContractSCR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upcContractSCR.setStatus("current")
_UpcContractMBS_Type = Integer32
_UpcContractMBS_Object = MibTableColumn
upcContractMBS = _UpcContractMBS_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1, 27),
    _UpcContractMBS_Type()
)
upcContractMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upcContractMBS.setStatus("current")


class _UpcContractServiceSubCategory_Type(Integer32):
    """Custom type upcContractServiceSubCategory based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_UpcContractServiceSubCategory_Type.__name__ = "Integer32"
_UpcContractServiceSubCategory_Object = MibTableColumn
upcContractServiceSubCategory = _UpcContractServiceSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1, 28),
    _UpcContractServiceSubCategory_Type()
)
upcContractServiceSubCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upcContractServiceSubCategory.setStatus("current")
_UpcContractCongestionBasedPeakBw_Type = Integer32
_UpcContractCongestionBasedPeakBw_Object = MibTableColumn
upcContractCongestionBasedPeakBw = _UpcContractCongestionBasedPeakBw_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1, 29),
    _UpcContractCongestionBasedPeakBw_Type()
)
upcContractCongestionBasedPeakBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upcContractCongestionBasedPeakBw.setStatus("current")
_UpcContractBehaviorClassSelector_Type = Integer32
_UpcContractBehaviorClassSelector_Object = MibTableColumn
upcContractBehaviorClassSelector = _UpcContractBehaviorClassSelector_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 10, 1, 1, 30),
    _UpcContractBehaviorClassSelector_Type()
)
upcContractBehaviorClassSelector.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upcContractBehaviorClassSelector.setStatus("current")
_ConfTopologyGroup_ObjectIdentity = ObjectIdentity
confTopologyGroup = _ConfTopologyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 11)
)
_ConfTopoHelloInterval_Type = Integer32
_ConfTopoHelloInterval_Object = MibScalar
confTopoHelloInterval = _ConfTopoHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 11, 1),
    _ConfTopoHelloInterval_Type()
)
confTopoHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confTopoHelloInterval.setStatus("current")
_ConfTopoNsapIndInterval_Type = Integer32
_ConfTopoNsapIndInterval_Object = MibScalar
confTopoNsapIndInterval = _ConfTopoNsapIndInterval_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 11, 2),
    _ConfTopoNsapIndInterval_Type()
)
confTopoNsapIndInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confTopoNsapIndInterval.setStatus("current")
_ConfTopoStaticUpdateInterval_Type = Integer32
_ConfTopoStaticUpdateInterval_Object = MibScalar
confTopoStaticUpdateInterval = _ConfTopoStaticUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 11, 3),
    _ConfTopoStaticUpdateInterval_Type()
)
confTopoStaticUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confTopoStaticUpdateInterval.setStatus("current")
_ConfTopoMaxHopCount_Type = Integer32
_ConfTopoMaxHopCount_Object = MibScalar
confTopoMaxHopCount = _ConfTopoMaxHopCount_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 11, 4),
    _ConfTopoMaxHopCount_Type()
)
confTopoMaxHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confTopoMaxHopCount.setStatus("current")
_ConfTopoACRPropMult_Type = Integer32
_ConfTopoACRPropMult_Object = MibScalar
confTopoACRPropMult = _ConfTopoACRPropMult_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 11, 5),
    _ConfTopoACRPropMult_Type()
)
confTopoACRPropMult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confTopoACRPropMult.setStatus("current")
_ConfTopoMinThresh_Type = Integer32
_ConfTopoMinThresh_Object = MibScalar
confTopoMinThresh = _ConfTopoMinThresh_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 11, 6),
    _ConfTopoMinThresh_Type()
)
confTopoMinThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confTopoMinThresh.setStatus("current")
_ConfTopoMinVCAvail_Type = Integer32
_ConfTopoMinVCAvail_Object = MibScalar
confTopoMinVCAvail = _ConfTopoMinVCAvail_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 11, 7),
    _ConfTopoMinVCAvail_Type()
)
confTopoMinVCAvail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confTopoMinVCAvail.setStatus("current")
_ConfTopoSpansAreaID_Type = Integer32
_ConfTopoSpansAreaID_Object = MibScalar
confTopoSpansAreaID = _ConfTopoSpansAreaID_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 11, 8),
    _ConfTopoSpansAreaID_Type()
)
confTopoSpansAreaID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confTopoSpansAreaID.setStatus("current")


class _ConfTopoSpansBorderSwitch_Type(Integer32):
    """Custom type confTopoSpansBorderSwitch based on Integer32"""
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


_ConfTopoSpansBorderSwitch_Type.__name__ = "Integer32"
_ConfTopoSpansBorderSwitch_Object = MibScalar
confTopoSpansBorderSwitch = _ConfTopoSpansBorderSwitch_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 11, 9),
    _ConfTopoSpansBorderSwitch_Type()
)
confTopoSpansBorderSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confTopoSpansBorderSwitch.setStatus("current")
_ConfTopoSwitchPrefix_Type = NsapPrefix
_ConfTopoSwitchPrefix_Object = MibScalar
confTopoSwitchPrefix = _ConfTopoSwitchPrefix_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 11, 10),
    _ConfTopoSwitchPrefix_Type()
)
confTopoSwitchPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confTopoSwitchPrefix.setStatus("current")
_ConfTopoSwitchPrefixMask_Type = Integer32
_ConfTopoSwitchPrefixMask_Object = MibScalar
confTopoSwitchPrefixMask = _ConfTopoSwitchPrefixMask_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 11, 11),
    _ConfTopoSwitchPrefixMask_Type()
)
confTopoSwitchPrefixMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confTopoSwitchPrefixMask.setStatus("current")
_ConfTopoPeerGroupMask_Type = Integer32
_ConfTopoPeerGroupMask_Object = MibScalar
confTopoPeerGroupMask = _ConfTopoPeerGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 11, 12),
    _ConfTopoPeerGroupMask_Type()
)
confTopoPeerGroupMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confTopoPeerGroupMask.setStatus("current")


class _ConfTopoSpansPnniBorderSwitch_Type(Integer32):
    """Custom type confTopoSpansPnniBorderSwitch based on Integer32"""
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


_ConfTopoSpansPnniBorderSwitch_Type.__name__ = "Integer32"
_ConfTopoSpansPnniBorderSwitch_Object = MibScalar
confTopoSpansPnniBorderSwitch = _ConfTopoSpansPnniBorderSwitch_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 11, 13),
    _ConfTopoSpansPnniBorderSwitch_Type()
)
confTopoSpansPnniBorderSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confTopoSpansPnniBorderSwitch.setStatus("current")


class _ConfTopoPGSNReachCost_Type(Integer32):
    """Custom type confTopoPGSNReachCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ConfTopoPGSNReachCost_Type.__name__ = "Integer32"
_ConfTopoPGSNReachCost_Object = MibScalar
confTopoPGSNReachCost = _ConfTopoPGSNReachCost_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 11, 14),
    _ConfTopoPGSNReachCost_Type()
)
confTopoPGSNReachCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confTopoPGSNReachCost.setStatus("current")


class _ConfTopoPGSNReachCostMethod_Type(Integer32):
    """Custom type confTopoPGSNReachCostMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("user", 2))
    )


_ConfTopoPGSNReachCostMethod_Type.__name__ = "Integer32"
_ConfTopoPGSNReachCostMethod_Object = MibScalar
confTopoPGSNReachCostMethod = _ConfTopoPGSNReachCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 11, 15),
    _ConfTopoPGSNReachCostMethod_Type()
)
confTopoPGSNReachCostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confTopoPGSNReachCostMethod.setStatus("current")
_ConfTopoFtPnniForeArea_Type = Integer32
_ConfTopoFtPnniForeArea_Object = MibScalar
confTopoFtPnniForeArea = _ConfTopoFtPnniForeArea_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 11, 16),
    _ConfTopoFtPnniForeArea_Type()
)
confTopoFtPnniForeArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confTopoFtPnniForeArea.setStatus("deprecated")
_ConfTopoFtPnniForeLevel_Type = Integer32
_ConfTopoFtPnniForeLevel_Object = MibScalar
confTopoFtPnniForeLevel = _ConfTopoFtPnniForeLevel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 11, 17),
    _ConfTopoFtPnniForeLevel_Type()
)
confTopoFtPnniForeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confTopoFtPnniForeLevel.setStatus("deprecated")


class _ConfTopoLBUbrLoadBalance_Type(Integer32):
    """Custom type confTopoLBUbrLoadBalance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ConfTopoLBUbrLoadBalance_Type.__name__ = "Integer32"
_ConfTopoLBUbrLoadBalance_Object = MibScalar
confTopoLBUbrLoadBalance = _ConfTopoLBUbrLoadBalance_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 11, 18),
    _ConfTopoLBUbrLoadBalance_Type()
)
confTopoLBUbrLoadBalance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confTopoLBUbrLoadBalance.setStatus("current")
_OamGroup_ObjectIdentity = ObjectIdentity
oamGroup = _OamGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 12)
)
_OamGeneratingChannelTable_Object = MibTable
oamGeneratingChannelTable = _OamGeneratingChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 12, 1)
)
if mibBuilder.loadTexts:
    oamGeneratingChannelTable.setStatus("current")
_OamGeneratingChannelEntry_Object = MibTableRow
oamGeneratingChannelEntry = _OamGeneratingChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 12, 1, 1)
)
oamGeneratingChannelEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "chanPort"),
    (0, "Fore-Switch-MIB", "chanVPI"),
    (0, "Fore-Switch-MIB", "chanVCI"),
)
if mibBuilder.loadTexts:
    oamGeneratingChannelEntry.setStatus("current")
_OamGeneratingChannelCells_Type = Counter32
_OamGeneratingChannelCells_Object = MibTableColumn
oamGeneratingChannelCells = _OamGeneratingChannelCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 12, 1, 1, 1),
    _OamGeneratingChannelCells_Type()
)
oamGeneratingChannelCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oamGeneratingChannelCells.setStatus("current")
_OamGeneratingOpathTable_Object = MibTable
oamGeneratingOpathTable = _OamGeneratingOpathTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 12, 2)
)
if mibBuilder.loadTexts:
    oamGeneratingOpathTable.setStatus("current")
_OamGeneratingOpathEntry_Object = MibTableRow
oamGeneratingOpathEntry = _OamGeneratingOpathEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 12, 2, 1)
)
oamGeneratingOpathEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "opathPort"),
    (0, "Fore-Switch-MIB", "opathVPI"),
)
if mibBuilder.loadTexts:
    oamGeneratingOpathEntry.setStatus("current")
_OamGeneratingOpathCells_Type = Counter32
_OamGeneratingOpathCells_Object = MibTableColumn
oamGeneratingOpathCells = _OamGeneratingOpathCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 12, 2, 1, 1),
    _OamGeneratingOpathCells_Type()
)
oamGeneratingOpathCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oamGeneratingOpathCells.setStatus("current")
_OamGeneratingPathrTable_Object = MibTable
oamGeneratingPathrTable = _OamGeneratingPathrTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 12, 3)
)
if mibBuilder.loadTexts:
    oamGeneratingPathrTable.setStatus("current")
_OamGeneratingPathrEntry_Object = MibTableRow
oamGeneratingPathrEntry = _OamGeneratingPathrEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 12, 3, 1)
)
oamGeneratingPathrEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "pathrInputPort"),
    (0, "Fore-Switch-MIB", "pathrInputVPI"),
    (0, "Fore-Switch-MIB", "pathrOutputPort"),
    (0, "Fore-Switch-MIB", "pathrOutputVPI"),
)
if mibBuilder.loadTexts:
    oamGeneratingPathrEntry.setStatus("current")
_OamGeneratingPathrCells_Type = Counter32
_OamGeneratingPathrCells_Object = MibTableColumn
oamGeneratingPathrCells = _OamGeneratingPathrCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 12, 3, 1, 1),
    _OamGeneratingPathrCells_Type()
)
oamGeneratingPathrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oamGeneratingPathrCells.setStatus("current")
_OamReceivedPathTable_Object = MibTable
oamReceivedPathTable = _OamReceivedPathTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 12, 4)
)
if mibBuilder.loadTexts:
    oamReceivedPathTable.setStatus("current")
_OamReceivedPathEntry_Object = MibTableRow
oamReceivedPathEntry = _OamReceivedPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 12, 4, 1)
)
oamReceivedPathEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "pathPort"),
    (0, "Fore-Switch-MIB", "pathVPI"),
)
if mibBuilder.loadTexts:
    oamReceivedPathEntry.setStatus("current")
_OamReceivedPathAISCells_Type = Counter32
_OamReceivedPathAISCells_Object = MibTableColumn
oamReceivedPathAISCells = _OamReceivedPathAISCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 12, 4, 1, 1),
    _OamReceivedPathAISCells_Type()
)
oamReceivedPathAISCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oamReceivedPathAISCells.setStatus("current")
_OamReceivedPathRDICells_Type = Counter32
_OamReceivedPathRDICells_Object = MibTableColumn
oamReceivedPathRDICells = _OamReceivedPathRDICells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 12, 4, 1, 2),
    _OamReceivedPathRDICells_Type()
)
oamReceivedPathRDICells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oamReceivedPathRDICells.setStatus("current")
_GuardGroup_ObjectIdentity = ObjectIdentity
guardGroup = _GuardGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 13)
)
_GuardTable_Object = MibTable
guardTable = _GuardTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 13, 1)
)
if mibBuilder.loadTexts:
    guardTable.setStatus("current")
_GuardEntry_Object = MibTableRow
guardEntry = _GuardEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 13, 1, 1)
)
guardEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "boardIndex"),
)
if mibBuilder.loadTexts:
    guardEntry.setStatus("current")
_OamGuard_Type = TimeStamp
_OamGuard_Object = MibTableColumn
oamGuard = _OamGuard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 13, 1, 1, 1),
    _OamGuard_Type()
)
oamGuard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oamGuard.setStatus("current")
_IfIndexMapGroup_ObjectIdentity = ObjectIdentity
ifIndexMapGroup = _IfIndexMapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 14)
)
_IfIndexMapTable_Object = MibTable
ifIndexMapTable = _IfIndexMapTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 14, 1)
)
if mibBuilder.loadTexts:
    ifIndexMapTable.setStatus("current")
_IfIndexMapEntry_Object = MibTableRow
ifIndexMapEntry = _IfIndexMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 14, 1, 1)
)
ifIndexMapEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "ifIndexMapIndex"),
)
if mibBuilder.loadTexts:
    ifIndexMapEntry.setStatus("current")
_IfIndexMapIndex_Type = Integer32
_IfIndexMapIndex_Object = MibTableColumn
ifIndexMapIndex = _IfIndexMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 14, 1, 1, 1),
    _IfIndexMapIndex_Type()
)
ifIndexMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIndexMapIndex.setStatus("current")
_IfIndexMapBoard_Type = Integer32
_IfIndexMapBoard_Object = MibTableColumn
ifIndexMapBoard = _IfIndexMapBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 14, 1, 1, 2),
    _IfIndexMapBoard_Type()
)
ifIndexMapBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIndexMapBoard.setStatus("current")
_IfIndexMapNetmod_Type = Integer32
_IfIndexMapNetmod_Object = MibTableColumn
ifIndexMapNetmod = _IfIndexMapNetmod_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 14, 1, 1, 3),
    _IfIndexMapNetmod_Type()
)
ifIndexMapNetmod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIndexMapNetmod.setStatus("current")
_IfIndexMapPort_Type = Integer32
_IfIndexMapPort_Object = MibTableColumn
ifIndexMapPort = _IfIndexMapPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 14, 1, 1, 4),
    _IfIndexMapPort_Type()
)
ifIndexMapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIndexMapPort.setStatus("current")
_IfIndexNameGroup_ObjectIdentity = ObjectIdentity
ifIndexNameGroup = _IfIndexNameGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 15)
)
_CesExtGroup_ObjectIdentity = ObjectIdentity
cesExtGroup = _CesExtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16)
)
_CesExtTable_Type = TestAndIncr
_CesExtTable_Object = MibScalar
cesExtTable = _CesExtTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16, 1),
    _CesExtTable_Type()
)
cesExtTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesExtTable.setStatus("current")
_CbrctConfTable_Object = MibTable
cbrctConfTable = _CbrctConfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16, 2)
)
if mibBuilder.loadTexts:
    cbrctConfTable.setStatus("current")
_CbrctConfEntry_Object = MibTableRow
cbrctConfEntry = _CbrctConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16, 2, 1)
)
cbrctConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cbrctConfEntry.setStatus("current")


class _CbrctState_Type(Integer32):
    """Custom type cbrctState based on Integer32"""
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


_CbrctState_Type.__name__ = "Integer32"
_CbrctState_Object = MibTableColumn
cbrctState = _CbrctState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16, 2, 1, 1),
    _CbrctState_Type()
)
cbrctState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbrctState.setStatus("current")


class _CbrctIdleDetection_Type(Integer32):
    """Custom type cbrctIdleDetection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cas", 2),
          ("idlePattern", 1))
    )


_CbrctIdleDetection_Type.__name__ = "Integer32"
_CbrctIdleDetection_Object = MibTableColumn
cbrctIdleDetection = _CbrctIdleDetection_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16, 2, 1, 2),
    _CbrctIdleDetection_Type()
)
cbrctIdleDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbrctIdleDetection.setStatus("current")


class _CbrctIdleMask_Type(Integer32):
    """Custom type cbrctIdleMask based on Integer32"""
    defaultHexValue = 255


_CbrctIdleMask_Object = MibTableColumn
cbrctIdleMask = _CbrctIdleMask_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16, 2, 1, 3),
    _CbrctIdleMask_Type()
)
cbrctIdleMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbrctIdleMask.setStatus("current")


class _CbrctNoOfIdlePatterns_Type(Integer32):
    """Custom type cbrctNoOfIdlePatterns based on Integer32"""
    defaultValue = 2


_CbrctNoOfIdlePatterns_Object = MibTableColumn
cbrctNoOfIdlePatterns = _CbrctNoOfIdlePatterns_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16, 2, 1, 4),
    _CbrctNoOfIdlePatterns_Type()
)
cbrctNoOfIdlePatterns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbrctNoOfIdlePatterns.setStatus("current")


class _CbrctIdlePatterns_Type(Integer32):
    """Custom type cbrctIdlePatterns based on Integer32"""
    defaultHexValue = 32767


_CbrctIdlePatterns_Object = MibTableColumn
cbrctIdlePatterns = _CbrctIdlePatterns_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16, 2, 1, 5),
    _CbrctIdlePatterns_Type()
)
cbrctIdlePatterns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbrctIdlePatterns.setStatus("current")


class _CbrctIdleIntPeriod_Type(TimeInterval):
    """Custom type cbrctIdleIntPeriod based on TimeInterval"""
    defaultValue = 6


_CbrctIdleIntPeriod_Object = MibTableColumn
cbrctIdleIntPeriod = _CbrctIdleIntPeriod_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16, 2, 1, 6),
    _CbrctIdleIntPeriod_Type()
)
cbrctIdleIntPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbrctIdleIntPeriod.setStatus("current")


class _CbrctActiveIntPeriod_Type(TimeInterval):
    """Custom type cbrctActiveIntPeriod based on TimeInterval"""
    defaultValue = 6


_CbrctActiveIntPeriod_Object = MibTableColumn
cbrctActiveIntPeriod = _CbrctActiveIntPeriod_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 16, 2, 1, 7),
    _CbrctActiveIntPeriod_Type()
)
cbrctActiveIntPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbrctActiveIntPeriod.setStatus("current")
_QosClassExpansionGroup_ObjectIdentity = ObjectIdentity
qosClassExpansionGroup = _QosClassExpansionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 17)
)
_QosClassExpansionTable_Object = MibTable
qosClassExpansionTable = _QosClassExpansionTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 17, 1)
)
if mibBuilder.loadTexts:
    qosClassExpansionTable.setStatus("current")
_QosClassExpansionEntry_Object = MibTableRow
qosClassExpansionEntry = _QosClassExpansionEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 17, 1, 1)
)
qosClassExpansionEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "qosClassExpansionKey"),
    (0, "Fore-Switch-MIB", "qosClassValue"),
)
if mibBuilder.loadTexts:
    qosClassExpansionEntry.setStatus("current")
_QosClassExpansionKey_Type = Integer32
_QosClassExpansionKey_Object = MibTableColumn
qosClassExpansionKey = _QosClassExpansionKey_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 17, 1, 1, 1),
    _QosClassExpansionKey_Type()
)
qosClassExpansionKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosClassExpansionKey.setStatus("current")


class _QosClassValue_Type(Integer32):
    """Custom type qosClassValue based on Integer32"""
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
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5))
    )


_QosClassValue_Type.__name__ = "Integer32"
_QosClassValue_Object = MibTableColumn
qosClassValue = _QosClassValue_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 17, 1, 1, 2),
    _QosClassValue_Type()
)
qosClassValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosClassValue.setStatus("current")
_QosClassExpansionEntryStatus_Type = EntryStatus
_QosClassExpansionEntryStatus_Object = MibTableColumn
qosClassExpansionEntryStatus = _QosClassExpansionEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 17, 1, 1, 3),
    _QosClassExpansionEntryStatus_Type()
)
qosClassExpansionEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosClassExpansionEntryStatus.setStatus("current")


class _QosClassFwdCtd_Type(Integer32):
    """Custom type qosClassFwdCtd based on Integer32"""
    defaultValue = 16777215

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_QosClassFwdCtd_Type.__name__ = "Integer32"
_QosClassFwdCtd_Object = MibTableColumn
qosClassFwdCtd = _QosClassFwdCtd_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 17, 1, 1, 4),
    _QosClassFwdCtd_Type()
)
qosClassFwdCtd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosClassFwdCtd.setStatus("current")


class _QosClassFwdCdv_Type(Integer32):
    """Custom type qosClassFwdCdv based on Integer32"""
    defaultValue = 16777215

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_QosClassFwdCdv_Type.__name__ = "Integer32"
_QosClassFwdCdv_Object = MibTableColumn
qosClassFwdCdv = _QosClassFwdCdv_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 17, 1, 1, 5),
    _QosClassFwdCdv_Type()
)
qosClassFwdCdv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosClassFwdCdv.setStatus("current")


class _QosClassBackCdv_Type(Integer32):
    """Custom type qosClassBackCdv based on Integer32"""
    defaultValue = 16777215

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_QosClassBackCdv_Type.__name__ = "Integer32"
_QosClassBackCdv_Object = MibTableColumn
qosClassBackCdv = _QosClassBackCdv_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 17, 1, 1, 6),
    _QosClassBackCdv_Type()
)
qosClassBackCdv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosClassBackCdv.setStatus("current")


class _QosClassFwdClr_Type(Integer32):
    """Custom type qosClassFwdClr based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_QosClassFwdClr_Type.__name__ = "Integer32"
_QosClassFwdClr_Object = MibTableColumn
qosClassFwdClr = _QosClassFwdClr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 17, 1, 1, 7),
    _QosClassFwdClr_Type()
)
qosClassFwdClr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosClassFwdClr.setStatus("current")


class _QosClassBackClr_Type(Integer32):
    """Custom type qosClassBackClr based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_QosClassBackClr_Type.__name__ = "Integer32"
_QosClassBackClr_Object = MibTableColumn
qosClassBackClr = _QosClassBackClr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 17, 1, 1, 8),
    _QosClassBackClr_Type()
)
qosClassBackClr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosClassBackClr.setStatus("current")


class _QosClassName_Type(DisplayString):
    """Custom type qosClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_QosClassName_Type.__name__ = "DisplayString"
_QosClassName_Object = MibTableColumn
qosClassName = _QosClassName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 17, 1, 1, 9),
    _QosClassName_Type()
)
qosClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosClassName.setStatus("current")
_PathExtGroup_ObjectIdentity = ObjectIdentity
pathExtGroup = _PathExtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18)
)
_PathExtQosMetricTable_Object = MibTable
pathExtQosMetricTable = _PathExtQosMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18, 1)
)
if mibBuilder.loadTexts:
    pathExtQosMetricTable.setStatus("current")
_PathExtQosMetricEntry_Object = MibTableRow
pathExtQosMetricEntry = _PathExtQosMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18, 1, 1)
)
pathExtQosMetricEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "pathExtQosMetricIndex"),
)
if mibBuilder.loadTexts:
    pathExtQosMetricEntry.setStatus("current")
_PathExtQosMetricIndex_Type = Integer32
_PathExtQosMetricIndex_Object = MibTableColumn
pathExtQosMetricIndex = _PathExtQosMetricIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18, 1, 1, 1),
    _PathExtQosMetricIndex_Type()
)
pathExtQosMetricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pathExtQosMetricIndex.setStatus("current")
_PathExtQosMetricMaxCtd_Type = Integer32
_PathExtQosMetricMaxCtd_Object = MibTableColumn
pathExtQosMetricMaxCtd = _PathExtQosMetricMaxCtd_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18, 1, 1, 2),
    _PathExtQosMetricMaxCtd_Type()
)
pathExtQosMetricMaxCtd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pathExtQosMetricMaxCtd.setStatus("current")
_PathExtQosMetricMaxCdv_Type = Integer32
_PathExtQosMetricMaxCdv_Object = MibTableColumn
pathExtQosMetricMaxCdv = _PathExtQosMetricMaxCdv_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18, 1, 1, 3),
    _PathExtQosMetricMaxCdv_Type()
)
pathExtQosMetricMaxCdv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pathExtQosMetricMaxCdv.setStatus("current")
_PathExtQosMetricMaxClr_Type = Integer32
_PathExtQosMetricMaxClr_Object = MibTableColumn
pathExtQosMetricMaxClr = _PathExtQosMetricMaxClr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18, 1, 1, 4),
    _PathExtQosMetricMaxClr_Type()
)
pathExtQosMetricMaxClr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pathExtQosMetricMaxClr.setStatus("current")
_PathExtQosMetricEntryStatus_Type = EntryStatus
_PathExtQosMetricEntryStatus_Object = MibTableColumn
pathExtQosMetricEntryStatus = _PathExtQosMetricEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18, 1, 1, 5),
    _PathExtQosMetricEntryStatus_Type()
)
pathExtQosMetricEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pathExtQosMetricEntryStatus.setStatus("current")
_PathExtTable_Object = MibTable
pathExtTable = _PathExtTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18, 2)
)
if mibBuilder.loadTexts:
    pathExtTable.setStatus("current")
_PathExtEntry_Object = MibTableRow
pathExtEntry = _PathExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18, 2, 1)
)
pathExtEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "pathPort"),
    (0, "Fore-Switch-MIB", "pathVPI"),
)
if mibBuilder.loadTexts:
    pathExtEntry.setStatus("current")
_PathExtCbrMetric_Type = Integer32
_PathExtCbrMetric_Object = MibTableColumn
pathExtCbrMetric = _PathExtCbrMetric_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18, 2, 1, 1),
    _PathExtCbrMetric_Type()
)
pathExtCbrMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pathExtCbrMetric.setStatus("current")
_PathExtRtVbrMetric_Type = Integer32
_PathExtRtVbrMetric_Object = MibTableColumn
pathExtRtVbrMetric = _PathExtRtVbrMetric_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18, 2, 1, 2),
    _PathExtRtVbrMetric_Type()
)
pathExtRtVbrMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pathExtRtVbrMetric.setStatus("current")
_PathExtNrtVbrMetric_Type = Integer32
_PathExtNrtVbrMetric_Object = MibTableColumn
pathExtNrtVbrMetric = _PathExtNrtVbrMetric_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18, 2, 1, 3),
    _PathExtNrtVbrMetric_Type()
)
pathExtNrtVbrMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pathExtNrtVbrMetric.setStatus("current")
_PathExtAbrMetric_Type = Integer32
_PathExtAbrMetric_Object = MibTableColumn
pathExtAbrMetric = _PathExtAbrMetric_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18, 2, 1, 4),
    _PathExtAbrMetric_Type()
)
pathExtAbrMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pathExtAbrMetric.setStatus("current")
_PathExtUbrMetric_Type = Integer32
_PathExtUbrMetric_Object = MibTableColumn
pathExtUbrMetric = _PathExtUbrMetric_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18, 2, 1, 5),
    _PathExtUbrMetric_Type()
)
pathExtUbrMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pathExtUbrMetric.setStatus("current")
_PathExtEntryStatus_Type = EntryStatus
_PathExtEntryStatus_Object = MibTableColumn
pathExtEntryStatus = _PathExtEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18, 2, 1, 6),
    _PathExtEntryStatus_Type()
)
pathExtEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pathExtEntryStatus.setStatus("current")
_OutputPathExtTable_Object = MibTable
outputPathExtTable = _OutputPathExtTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18, 3)
)
if mibBuilder.loadTexts:
    outputPathExtTable.setStatus("current")
_OutputPathExtEntry_Object = MibTableRow
outputPathExtEntry = _OutputPathExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18, 3, 1)
)
outputPathExtEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "opathPort"),
    (0, "Fore-Switch-MIB", "opathVPI"),
)
if mibBuilder.loadTexts:
    outputPathExtEntry.setStatus("current")
_OpathExtCbrMetric_Type = Integer32
_OpathExtCbrMetric_Object = MibTableColumn
opathExtCbrMetric = _OpathExtCbrMetric_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18, 3, 1, 1),
    _OpathExtCbrMetric_Type()
)
opathExtCbrMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    opathExtCbrMetric.setStatus("current")
_OpathExtRtVbrMetric_Type = Integer32
_OpathExtRtVbrMetric_Object = MibTableColumn
opathExtRtVbrMetric = _OpathExtRtVbrMetric_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18, 3, 1, 2),
    _OpathExtRtVbrMetric_Type()
)
opathExtRtVbrMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    opathExtRtVbrMetric.setStatus("current")
_OpathExtNrtVbrMetric_Type = Integer32
_OpathExtNrtVbrMetric_Object = MibTableColumn
opathExtNrtVbrMetric = _OpathExtNrtVbrMetric_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18, 3, 1, 3),
    _OpathExtNrtVbrMetric_Type()
)
opathExtNrtVbrMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    opathExtNrtVbrMetric.setStatus("current")
_OpathExtAbrMetric_Type = Integer32
_OpathExtAbrMetric_Object = MibTableColumn
opathExtAbrMetric = _OpathExtAbrMetric_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18, 3, 1, 4),
    _OpathExtAbrMetric_Type()
)
opathExtAbrMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    opathExtAbrMetric.setStatus("current")
_OpathExtUbrMetric_Type = Integer32
_OpathExtUbrMetric_Object = MibTableColumn
opathExtUbrMetric = _OpathExtUbrMetric_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18, 3, 1, 5),
    _OpathExtUbrMetric_Type()
)
opathExtUbrMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    opathExtUbrMetric.setStatus("current")
_OpathExtEntryStatus_Type = EntryStatus
_OpathExtEntryStatus_Object = MibTableColumn
opathExtEntryStatus = _OpathExtEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18, 3, 1, 6),
    _OpathExtEntryStatus_Type()
)
opathExtEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    opathExtEntryStatus.setStatus("current")
_VpGroupTable_Object = MibTable
vpGroupTable = _VpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18, 4)
)
if mibBuilder.loadTexts:
    vpGroupTable.setStatus("current")
_VpGroupEntry_Object = MibTableRow
vpGroupEntry = _VpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18, 4, 1)
)
vpGroupEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "vpGroupIndex"),
    (0, "Fore-Switch-MIB", "vpGroupPort"),
    (0, "Fore-Switch-MIB", "vpGroupVPI"),
)
if mibBuilder.loadTexts:
    vpGroupEntry.setStatus("current")
_VpGroupIndex_Type = Integer32
_VpGroupIndex_Object = MibTableColumn
vpGroupIndex = _VpGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18, 4, 1, 1),
    _VpGroupIndex_Type()
)
vpGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpGroupIndex.setStatus("current")
_VpGroupPort_Type = Integer32
_VpGroupPort_Object = MibTableColumn
vpGroupPort = _VpGroupPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18, 4, 1, 2),
    _VpGroupPort_Type()
)
vpGroupPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpGroupPort.setStatus("current")
_VpGroupVPI_Type = Integer32
_VpGroupVPI_Object = MibTableColumn
vpGroupVPI = _VpGroupVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18, 4, 1, 3),
    _VpGroupVPI_Type()
)
vpGroupVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpGroupVPI.setStatus("current")
_VpGroupVPCI_Type = Integer32
_VpGroupVPCI_Object = MibTableColumn
vpGroupVPCI = _VpGroupVPCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18, 4, 1, 4),
    _VpGroupVPCI_Type()
)
vpGroupVPCI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpGroupVPCI.setStatus("current")
_VpGroupEntryStatus_Type = EntryStatus
_VpGroupEntryStatus_Object = MibTableColumn
vpGroupEntryStatus = _VpGroupEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 18, 4, 1, 5),
    _VpGroupEntryStatus_Type()
)
vpGroupEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpGroupEntryStatus.setStatus("current")
_PoolGroup_ObjectIdentity = ObjectIdentity
poolGroup = _PoolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 19)
)
_PoolConfGroup_ObjectIdentity = ObjectIdentity
poolConfGroup = _PoolConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 19, 1)
)
_PoolConfPPCalls_Type = Integer32
_PoolConfPPCalls_Object = MibScalar
poolConfPPCalls = _PoolConfPPCalls_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 19, 1, 1),
    _PoolConfPPCalls_Type()
)
poolConfPPCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poolConfPPCalls.setStatus("current")
_PoolConfPMPCalls_Type = Integer32
_PoolConfPMPCalls_Object = MibScalar
poolConfPMPCalls = _PoolConfPMPCalls_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 19, 1, 2),
    _PoolConfPMPCalls_Type()
)
poolConfPMPCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poolConfPMPCalls.setStatus("current")
_PoolConfMaxPercentage_Type = Integer32
_PoolConfMaxPercentage_Object = MibScalar
poolConfMaxPercentage = _PoolConfMaxPercentage_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 19, 1, 5),
    _PoolConfMaxPercentage_Type()
)
poolConfMaxPercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poolConfMaxPercentage.setStatus("current")
_AsxAtmIfGroup_ObjectIdentity = ObjectIdentity
asxAtmIfGroup = _AsxAtmIfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 20)
)
_AsxAtmIfTable_Object = MibTable
asxAtmIfTable = _AsxAtmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 20, 1)
)
if mibBuilder.loadTexts:
    asxAtmIfTable.setStatus("current")
_AsxAtmIfEntry_Object = MibTableRow
asxAtmIfEntry = _AsxAtmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 20, 1, 1)
)
asxAtmIfEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "asxAtmIfName"),
)
if mibBuilder.loadTexts:
    asxAtmIfEntry.setStatus("current")
_AsxAtmIfName_Type = DisplayString
_AsxAtmIfName_Object = MibTableColumn
asxAtmIfName = _AsxAtmIfName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 20, 1, 1, 1),
    _AsxAtmIfName_Type()
)
asxAtmIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asxAtmIfName.setStatus("current")
_AsxAtmIfLinkid_Type = Integer32
_AsxAtmIfLinkid_Object = MibTableColumn
asxAtmIfLinkid = _AsxAtmIfLinkid_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 20, 1, 1, 2),
    _AsxAtmIfLinkid_Type()
)
asxAtmIfLinkid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asxAtmIfLinkid.setStatus("current")
_SyncStatusMsgGroup_ObjectIdentity = ObjectIdentity
syncStatusMsgGroup = _SyncStatusMsgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 21)
)
_SyslogGroup_ObjectIdentity = ObjectIdentity
syslogGroup = _SyslogGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 22)
)


class _SyslogFacility_Type(Integer32):
    """Custom type syslogFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("daemon", 0),
          ("local0", 1),
          ("local1", 2),
          ("local2", 3),
          ("local3", 4),
          ("local4", 5),
          ("local5", 6),
          ("local6", 7),
          ("local7", 8))
    )


_SyslogFacility_Type.__name__ = "Integer32"
_SyslogFacility_Object = MibScalar
syslogFacility = _SyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 22, 1),
    _SyslogFacility_Type()
)
syslogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogFacility.setStatus("current")


class _SyslogConsoleState_Type(Integer32):
    """Custom type syslogConsoleState based on Integer32"""
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


_SyslogConsoleState_Type.__name__ = "Integer32"
_SyslogConsoleState_Object = MibScalar
syslogConsoleState = _SyslogConsoleState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 22, 2),
    _SyslogConsoleState_Type()
)
syslogConsoleState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogConsoleState.setStatus("current")
_SyslogDestinationTable_Object = MibTable
syslogDestinationTable = _SyslogDestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 22, 3)
)
if mibBuilder.loadTexts:
    syslogDestinationTable.setStatus("current")
_SyslogDestinationEntry_Object = MibTableRow
syslogDestinationEntry = _SyslogDestinationEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 22, 3, 1)
)
syslogDestinationEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "syslogDestinationHost"),
)
if mibBuilder.loadTexts:
    syslogDestinationEntry.setStatus("current")
_SyslogDestinationHost_Type = IpAddress
_SyslogDestinationHost_Object = MibTableColumn
syslogDestinationHost = _SyslogDestinationHost_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 22, 3, 1, 1),
    _SyslogDestinationHost_Type()
)
syslogDestinationHost.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    syslogDestinationHost.setStatus("current")
_SyslogDestinationStatus_Type = RowStatus
_SyslogDestinationStatus_Object = MibTableColumn
syslogDestinationStatus = _SyslogDestinationStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 22, 3, 1, 2),
    _SyslogDestinationStatus_Type()
)
syslogDestinationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogDestinationStatus.setStatus("current")
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 2)
)
_TrapConfGroup_ObjectIdentity = ObjectIdentity
trapConfGroup = _TrapConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 2, 1)
)
_TrapNumberOfDest_Type = Integer32
_TrapNumberOfDest_Object = MibScalar
trapNumberOfDest = _TrapNumberOfDest_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 2, 1, 1),
    _TrapNumberOfDest_Type()
)
trapNumberOfDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapNumberOfDest.setStatus("deprecated")
_TrapDestTable_Object = MibTable
trapDestTable = _TrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    trapDestTable.setStatus("deprecated")
_TrapDestEntry_Object = MibTableRow
trapDestEntry = _TrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 2, 1, 2, 1)
)
trapDestEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "trapDest"),
)
if mibBuilder.loadTexts:
    trapDestEntry.setStatus("deprecated")
_TrapDest_Type = IpAddress
_TrapDest_Object = MibTableColumn
trapDest = _TrapDest_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 2, 1, 2, 1, 1),
    _TrapDest_Type()
)
trapDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDest.setStatus("deprecated")
_TrapDestStatus_Type = EntryStatus
_TrapDestStatus_Object = MibTableColumn
trapDestStatus = _TrapDestStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 2, 1, 2, 1, 2),
    _TrapDestStatus_Type()
)
trapDestStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapDestStatus.setStatus("deprecated")
_SnmpConfGroup_ObjectIdentity = ObjectIdentity
snmpConfGroup = _SnmpConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 2, 2)
)


class _SnmpReconfigure_Type(Integer32):
    """Custom type snmpReconfigure based on Integer32"""
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


_SnmpReconfigure_Type.__name__ = "Integer32"
_SnmpReconfigure_Object = MibScalar
snmpReconfigure = _SnmpReconfigure_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 2, 2, 1),
    _SnmpReconfigure_Type()
)
snmpReconfigure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpReconfigure.setStatus("deprecated")
_SnmpReadCommunity_Type = OctetString
_SnmpReadCommunity_Object = MibScalar
snmpReadCommunity = _SnmpReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 2, 2, 2),
    _SnmpReadCommunity_Type()
)
snmpReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpReadCommunity.setStatus("deprecated")
_SnmpWriteCommunity_Type = OctetString
_SnmpWriteCommunity_Object = MibScalar
snmpWriteCommunity = _SnmpWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 2, 2, 3),
    _SnmpWriteCommunity_Type()
)
snmpWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpWriteCommunity.setStatus("deprecated")


class _SnmpWarmStart_Type(Integer32):
    """Custom type snmpWarmStart based on Integer32"""
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


_SnmpWarmStart_Type.__name__ = "Integer32"
_SnmpWarmStart_Object = MibScalar
snmpWarmStart = _SnmpWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 2, 2, 4),
    _SnmpWarmStart_Type()
)
snmpWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpWarmStart.setStatus("current")


class _SnmpColdStart_Type(Integer32):
    """Custom type snmpColdStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enableResetATMconf", 2),
          ("enableResetAllConf", 3))
    )


_SnmpColdStart_Type.__name__ = "Integer32"
_SnmpColdStart_Object = MibScalar
snmpColdStart = _SnmpColdStart_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 2, 2, 5),
    _SnmpColdStart_Type()
)
snmpColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpColdStart.setStatus("current")


class _SnmpRemoteSetsStatus_Type(Integer32):
    """Custom type snmpRemoteSetsStatus based on Integer32"""
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


_SnmpRemoteSetsStatus_Type.__name__ = "Integer32"
_SnmpRemoteSetsStatus_Object = MibScalar
snmpRemoteSetsStatus = _SnmpRemoteSetsStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 2, 2, 6),
    _SnmpRemoteSetsStatus_Type()
)
snmpRemoteSetsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpRemoteSetsStatus.setStatus("deprecated")
_SnmpAgentAddressGroup_ObjectIdentity = ObjectIdentity
snmpAgentAddressGroup = _SnmpAgentAddressGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 2, 5)
)


class _SnmpThisAgentBoardNumber_Type(Integer32):
    """Custom type snmpThisAgentBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SnmpThisAgentBoardNumber_Type.__name__ = "Integer32"
_SnmpThisAgentBoardNumber_Object = MibScalar
snmpThisAgentBoardNumber = _SnmpThisAgentBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 2, 5, 1),
    _SnmpThisAgentBoardNumber_Type()
)
snmpThisAgentBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpThisAgentBoardNumber.setStatus("current")
_SnmpAgentTable_Object = MibTable
snmpAgentTable = _SnmpAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 2, 5, 2)
)
if mibBuilder.loadTexts:
    snmpAgentTable.setStatus("current")
_SnmpAgentEntry_Object = MibTableRow
snmpAgentEntry = _SnmpAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 2, 5, 2, 1)
)
snmpAgentEntry.setIndexNames(
    (0, "Fore-Switch-MIB", "snmpAgentBoardNumber"),
    (0, "Fore-Switch-MIB", "snmpAgentInterface"),
)
if mibBuilder.loadTexts:
    snmpAgentEntry.setStatus("current")
_SnmpAgentBoardNumber_Type = Integer32
_SnmpAgentBoardNumber_Object = MibTableColumn
snmpAgentBoardNumber = _SnmpAgentBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 2, 5, 2, 1, 1),
    _SnmpAgentBoardNumber_Type()
)
snmpAgentBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentBoardNumber.setStatus("current")
_SnmpAgentInterface_Type = Integer32
_SnmpAgentInterface_Object = MibTableColumn
snmpAgentInterface = _SnmpAgentInterface_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 2, 5, 2, 1, 2),
    _SnmpAgentInterface_Type()
)
snmpAgentInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentInterface.setStatus("current")
_SnmpAgentAddress_Type = IpAddress
_SnmpAgentAddress_Object = MibTableColumn
snmpAgentAddress = _SnmpAgentAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 2, 5, 2, 1, 3),
    _SnmpAgentAddress_Type()
)
snmpAgentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentAddress.setStatus("current")

# Managed Objects groups


# Notification objects

asxSwLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 0)
)
asxSwLinkDown.setObjects(
      *(("Fore-Switch-MIB", "portNumber"),
        ("Fore-Switch-MIB", "portName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxSwLinkDown.setStatus(
        "current"
    )

asxSwLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1)
)
asxSwLinkUp.setObjects(
      *(("Fore-Switch-MIB", "portNumber"),
        ("Fore-Switch-MIB", "portName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxSwLinkUp.setStatus(
        "current"
    )

asxHostLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 2)
)
asxHostLinkDown.setObjects(
      *(("Fore-Switch-MIB", "portNumber"),
        ("Fore-Switch-MIB", "portName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxHostLinkDown.setStatus(
        "current"
    )

asxHostLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 3)
)
asxHostLinkUp.setObjects(
      *(("Fore-Switch-MIB", "portNumber"),
        ("Fore-Switch-MIB", "portName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxHostLinkUp.setStatus(
        "current"
    )

asxNetModuleDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 4)
)
asxNetModuleDown.setObjects(
      *(("Fore-Switch-MIB", "moduleBoard"),
        ("Fore-Switch-MIB", "moduleNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxNetModuleDown.setStatus(
        "current"
    )

asxNetModuleUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 5)
)
asxNetModuleUp.setObjects(
      *(("Fore-Switch-MIB", "moduleBoard"),
        ("Fore-Switch-MIB", "moduleNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxNetModuleUp.setStatus(
        "current"
    )

asxPsInputDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 6)
)
asxPsInputDown.setObjects(
      *(("Fore-Switch-MIB", "envPowerSupplyIndex"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxPsInputDown.setStatus(
        "current"
    )

asxPsInputUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 7)
)
asxPsInputUp.setObjects(
      *(("Fore-Switch-MIB", "envPowerSupplyIndex"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxPsInputUp.setStatus(
        "current"
    )

asxPsOutputDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 9)
)
asxPsOutputDown.setObjects(
      *(("Fore-Switch-MIB", "envPowerSupplyIndex"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxPsOutputDown.setStatus(
        "current"
    )

asxPsOutputUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 10)
)
asxPsOutputUp.setObjects(
      *(("Fore-Switch-MIB", "envPowerSupplyIndex"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxPsOutputUp.setStatus(
        "current"
    )

asxFanBankDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 22)
)
asxFanBankDown.setObjects(
      *(("Fore-Switch-MIB", "envFanBankIndex"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxFanBankDown.setStatus(
        "current"
    )

asxFanBankUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 23)
)
asxFanBankUp.setObjects(
      *(("Fore-Switch-MIB", "envFanBankIndex"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxFanBankUp.setStatus(
        "current"
    )

asxLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 28)
)
asxLinkDown.setObjects(
      *(("Fore-Switch-MIB", "portNumber"),
        ("Fore-Switch-MIB", "portName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxLinkDown.setStatus(
        "current"
    )

asxLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 29)
)
asxLinkUp.setObjects(
      *(("Fore-Switch-MIB", "portNumber"),
        ("Fore-Switch-MIB", "portName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxLinkUp.setStatus(
        "current"
    )

asxSpansDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 30)
)
asxSpansDown.setObjects(
      *(("Fore-Switch-MIB", "portName"),
        ("Fore-Switch-MIB", "sigPathPort"),
        ("Fore-Switch-MIB", "sigPathVPI"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxSpansDown.setStatus(
        "current"
    )

asxSpansUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 31)
)
asxSpansUp.setObjects(
      *(("Fore-Switch-MIB", "portName"),
        ("Fore-Switch-MIB", "sigPathPort"),
        ("Fore-Switch-MIB", "sigPathVPI"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxSpansUp.setStatus(
        "current"
    )

asxTempSensorOverTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 32)
)
asxTempSensorOverTemp.setObjects(
      *(("Fore-Switch-MIB", "envTempSensorIndex"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxTempSensorOverTemp.setStatus(
        "current"
    )

asxTempSensorRegularTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 33)
)
asxTempSensorRegularTemp.setObjects(
      *(("Fore-Switch-MIB", "envTempSensorIndex"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxTempSensorRegularTemp.setStatus(
        "current"
    )

asxFabricTemperatureOverTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 34)
)
asxFabricTemperatureOverTemp.setObjects(
      *(("Fore-Switch-MIB", "envFabricIndex"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxFabricTemperatureOverTemp.setStatus(
        "current"
    )

asxFabricTemperatureRegularTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 35)
)
asxFabricTemperatureRegularTemp.setObjects(
      *(("Fore-Switch-MIB", "envFabricIndex"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxFabricTemperatureRegularTemp.setStatus(
        "current"
    )

asxSonetLOSDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 36)
)
asxSonetLOSDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxSonetLOSDetected.setStatus(
        "current"
    )

asxSonetLOSCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 37)
)
asxSonetLOSCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxSonetLOSCleared.setStatus(
        "current"
    )

asxSonetPathLabelDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 38)
)
asxSonetPathLabelDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxSonetPathLabelDetected.setStatus(
        "current"
    )

asxSonetPathLabelCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 39)
)
asxSonetPathLabelCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxSonetPathLabelCleared.setStatus(
        "current"
    )

asxSonetLineAISDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 40)
)
asxSonetLineAISDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxSonetLineAISDetected.setStatus(
        "current"
    )

asxSonetLineAISCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 41)
)
asxSonetLineAISCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxSonetLineAISCleared.setStatus(
        "current"
    )

asxDS3PLCPYellowDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 46)
)
asxDS3PLCPYellowDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS3PLCPYellowDetected.setStatus(
        "current"
    )

asxDS3PLCPYellowCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 47)
)
asxDS3PLCPYellowCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS3PLCPYellowCleared.setStatus(
        "current"
    )

asxDS3PLCPLOFDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 48)
)
asxDS3PLCPLOFDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS3PLCPLOFDetected.setStatus(
        "current"
    )

asxDS3PLCPLOFCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 49)
)
asxDS3PLCPLOFCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS3PLCPLOFCleared.setStatus(
        "current"
    )

asxDS3LOFDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 50)
)
asxDS3LOFDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS3LOFDetected.setStatus(
        "current"
    )

asxDS3LOFCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 51)
)
asxDS3LOFCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS3LOFCleared.setStatus(
        "current"
    )

asxDS3AISDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 52)
)
asxDS3AISDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS3AISDetected.setStatus(
        "current"
    )

asxDS3AISCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 53)
)
asxDS3AISCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS3AISCleared.setStatus(
        "current"
    )

asxDS1PLCPYellowDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 60)
)
asxDS1PLCPYellowDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS1PLCPYellowDetected.setStatus(
        "current"
    )

asxDS1PLCPYellowCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 61)
)
asxDS1PLCPYellowCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS1PLCPYellowCleared.setStatus(
        "current"
    )

asxDS1PLCPLOFDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 62)
)
asxDS1PLCPLOFDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS1PLCPLOFDetected.setStatus(
        "current"
    )

asxDS1PLCPLOFCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 63)
)
asxDS1PLCPLOFCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS1PLCPLOFCleared.setStatus(
        "current"
    )

asxDS1YellowDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 64)
)
asxDS1YellowDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS1YellowDetected.setStatus(
        "current"
    )

asxDS1YellowCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 65)
)
asxDS1YellowCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS1YellowCleared.setStatus(
        "current"
    )

asxDS1AISDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 66)
)
asxDS1AISDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS1AISDetected.setStatus(
        "current"
    )

asxDS1AISCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 67)
)
asxDS1AISCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS1AISCleared.setStatus(
        "current"
    )

asxDS1LOSDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 68)
)
asxDS1LOSDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS1LOSDetected.setStatus(
        "current"
    )

asxDS1LOSCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 69)
)
asxDS1LOSCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS1LOSCleared.setStatus(
        "current"
    )

asxDS1LOFDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 70)
)
asxDS1LOFDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS1LOFDetected.setStatus(
        "current"
    )

asxDS1LOFCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 71)
)
asxDS1LOFCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS1LOFCleared.setStatus(
        "current"
    )

asxDS3FERFDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 74)
)
asxDS3FERFDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS3FERFDetected.setStatus(
        "current"
    )

asxDS3FERFCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 75)
)
asxDS3FERFCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS3FERFCleared.setStatus(
        "current"
    )

asxE3YellowDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 78)
)
asxE3YellowDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxE3YellowDetected.setStatus(
        "current"
    )

asxE3YellowCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 79)
)
asxE3YellowCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxE3YellowCleared.setStatus(
        "current"
    )

asxE3OOFDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 80)
)
asxE3OOFDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxE3OOFDetected.setStatus(
        "current"
    )

asxE3OOFCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 81)
)
asxE3OOFCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxE3OOFCleared.setStatus(
        "current"
    )

asxE3AtmLCDDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 82)
)
asxE3AtmLCDDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxE3AtmLCDDetected.setStatus(
        "current"
    )

asxE3AtmLCDCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 83)
)
asxE3AtmLCDCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxE3AtmLCDCleared.setStatus(
        "current"
    )

asxE3PLCPYellowDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 86)
)
asxE3PLCPYellowDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxE3PLCPYellowDetected.setStatus(
        "current"
    )

asxE3PLCPYellowCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 87)
)
asxE3PLCPYellowCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxE3PLCPYellowCleared.setStatus(
        "current"
    )

asxE1YellowDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 90)
)
asxE1YellowDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxE1YellowDetected.setStatus(
        "current"
    )

asxE1YellowCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 91)
)
asxE1YellowCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxE1YellowCleared.setStatus(
        "current"
    )

asxE1LOFDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 92)
)
asxE1LOFDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxE1LOFDetected.setStatus(
        "current"
    )

asxE1LOFCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 93)
)
asxE1LOFCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxE1LOFCleared.setStatus(
        "current"
    )

asxE1PLCPYellowDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 96)
)
asxE1PLCPYellowDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxE1PLCPYellowDetected.setStatus(
        "current"
    )

asxE1PLCPYellowCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 97)
)
asxE1PLCPYellowCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxE1PLCPYellowCleared.setStatus(
        "current"
    )

asxE1PLCPLOFDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 98)
)
asxE1PLCPLOFDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxE1PLCPLOFDetected.setStatus(
        "current"
    )

asxE1PLCPLOFCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 99)
)
asxE1PLCPLOFCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxE1PLCPLOFCleared.setStatus(
        "current"
    )

asxE1LOSDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 100)
)
asxE1LOSDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxE1LOSDetected.setStatus(
        "current"
    )

asxE1LOSCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 101)
)
asxE1LOSCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxE1LOSCleared.setStatus(
        "current"
    )

asxE1AISDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 102)
)
asxE1AISDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxE1AISDetected.setStatus(
        "current"
    )

asxE1AISCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 103)
)
asxE1AISCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxE1AISCleared.setStatus(
        "current"
    )

asxE3AISDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 104)
)
asxE3AISDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxE3AISDetected.setStatus(
        "current"
    )

asxE3AISCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 105)
)
asxE3AISCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxE3AISCleared.setStatus(
        "current"
    )

asxE3LOSDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 106)
)
asxE3LOSDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxE3LOSDetected.setStatus(
        "current"
    )

asxE3LOSCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 107)
)
asxE3LOSCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxE3LOSCleared.setStatus(
        "current"
    )

asxE3PLCPLOFDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 108)
)
asxE3PLCPLOFDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxE3PLCPLOFDetected.setStatus(
        "current"
    )

asxE3PLCPLOFCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 109)
)
asxE3PLCPLOFCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxE3PLCPLOFCleared.setStatus(
        "current"
    )

asxJ2YellowDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 112)
)
asxJ2YellowDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxJ2YellowDetected.setStatus(
        "current"
    )

asxJ2YellowCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 113)
)
asxJ2YellowCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxJ2YellowCleared.setStatus(
        "current"
    )

asxJ2AISDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 114)
)
asxJ2AISDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxJ2AISDetected.setStatus(
        "current"
    )

asxJ2AISCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 115)
)
asxJ2AISCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxJ2AISCleared.setStatus(
        "current"
    )

asxJ2LOSDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 116)
)
asxJ2LOSDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxJ2LOSDetected.setStatus(
        "current"
    )

asxJ2LOSCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 117)
)
asxJ2LOSCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxJ2LOSCleared.setStatus(
        "current"
    )

asxJ2LOFDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 118)
)
asxJ2LOFDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxJ2LOFDetected.setStatus(
        "current"
    )

asxJ2LOFCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 119)
)
asxJ2LOFCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxJ2LOFCleared.setStatus(
        "current"
    )

asxDS3LOSDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 120)
)
asxDS3LOSDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS3LOSDetected.setStatus(
        "current"
    )

asxDS3LOSCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 121)
)
asxDS3LOSCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS3LOSCleared.setStatus(
        "current"
    )

asxSonetLOFDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 130)
)
asxSonetLOFDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxSonetLOFDetected.setStatus(
        "current"
    )

asxSonetLOFCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 131)
)
asxSonetLOFCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxSonetLOFCleared.setStatus(
        "current"
    )

asxSonetLineRDIDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 132)
)
asxSonetLineRDIDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxSonetLineRDIDetected.setStatus(
        "current"
    )

asxSonetLineRDICleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 133)
)
asxSonetLineRDICleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxSonetLineRDICleared.setStatus(
        "current"
    )

asxSonetPathAISDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 134)
)
asxSonetPathAISDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxSonetPathAISDetected.setStatus(
        "current"
    )

asxSonetPathAISCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 135)
)
asxSonetPathAISCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxSonetPathAISCleared.setStatus(
        "current"
    )

asxSonetPathLOPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 136)
)
asxSonetPathLOPDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxSonetPathLOPDetected.setStatus(
        "current"
    )

asxSonetPathLOPCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 137)
)
asxSonetPathLOPCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxSonetPathLOPCleared.setStatus(
        "current"
    )

asxSonetPathUNEQDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 138)
)
asxSonetPathUNEQDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxSonetPathUNEQDetected.setStatus(
        "current"
    )

asxSonetPathUNEQCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 139)
)
asxSonetPathUNEQCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxSonetPathUNEQCleared.setStatus(
        "current"
    )

asxSonetPathRDIDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 140)
)
asxSonetPathRDIDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxSonetPathRDIDetected.setStatus(
        "current"
    )

asxSonetPathRDICleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 141)
)
asxSonetPathRDICleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxSonetPathRDICleared.setStatus(
        "current"
    )

asxSonetAtmLCDDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 142)
)
asxSonetAtmLCDDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxSonetAtmLCDDetected.setStatus(
        "current"
    )

asxSonetAtmLCDCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 143)
)
asxSonetAtmLCDCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxSonetAtmLCDCleared.setStatus(
        "current"
    )

asxSonetAtmLineBIPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 144)
)
asxSonetAtmLineBIPDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxSonetAtmLineBIPDetected.setStatus(
        "current"
    )

asxSonetAtmLineBIPCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 145)
)
asxSonetAtmLineBIPCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxSonetAtmLineBIPCleared.setStatus(
        "current"
    )

asxDS3IdleDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 160)
)
asxDS3IdleDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS3IdleDetected.setStatus(
        "current"
    )

asxDS3IdleCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 161)
)
asxDS3IdleCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS3IdleCleared.setStatus(
        "current"
    )

asxDS3AtmLCDDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 162)
)
asxDS3AtmLCDDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS3AtmLCDDetected.setStatus(
        "current"
    )

asxDS3AtmLCDCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 163)
)
asxDS3AtmLCDCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS3AtmLCDCleared.setStatus(
        "current"
    )

asxDS3PbitPerrDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 164)
)
asxDS3PbitPerrDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS3PbitPerrDetected.setStatus(
        "current"
    )

asxDS3PbitPerrCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 165)
)
asxDS3PbitPerrCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS3PbitPerrCleared.setStatus(
        "current"
    )

asxDS1PRBSDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 176)
)
asxDS1PRBSDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS1PRBSDetected.setStatus(
        "current"
    )

asxDS1PRBSCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 177)
)
asxDS1PRBSCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS1PRBSCleared.setStatus(
        "current"
    )

asxDS1AtmLCDDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 178)
)
asxDS1AtmLCDDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS1AtmLCDDetected.setStatus(
        "current"
    )

asxDS1AtmLCDCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 179)
)
asxDS1AtmLCDCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS1AtmLCDCleared.setStatus(
        "current"
    )

asxDS1CRCErrDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 180)
)
asxDS1CRCErrDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS1CRCErrDetected.setStatus(
        "current"
    )

asxDS1CRCErrCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 181)
)
asxDS1CRCErrCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDS1CRCErrCleared.setStatus(
        "current"
    )

asxE3TrailChangeDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 192)
)
asxE3TrailChangeDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxE3TrailChangeDetected.setStatus(
        "current"
    )

asxE1AtmLCDDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 208)
)
asxE1AtmLCDDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxE1AtmLCDDetected.setStatus(
        "current"
    )

asxE1AtmLCDCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 209)
)
asxE1AtmLCDCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxE1AtmLCDCleared.setStatus(
        "current"
    )

asxJ2RLOCDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 224)
)
asxJ2RLOCDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxJ2RLOCDetected.setStatus(
        "current"
    )

asxJ2RLOCCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 225)
)
asxJ2RLOCCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxJ2RLOCCleared.setStatus(
        "current"
    )

asxJ2HBERDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 226)
)
asxJ2HBERDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxJ2HBERDetected.setStatus(
        "current"
    )

asxJ2HBERCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 227)
)
asxJ2HBERCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxJ2HBERCleared.setStatus(
        "current"
    )

asxJ2PAISDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 228)
)
asxJ2PAISDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxJ2PAISDetected.setStatus(
        "current"
    )

asxJ2PAISCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 229)
)
asxJ2PAISCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxJ2PAISCleared.setStatus(
        "current"
    )

asxJ2AtmLCDDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 230)
)
asxJ2AtmLCDDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxJ2AtmLCDDetected.setStatus(
        "current"
    )

asxJ2AtmLCDCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 231)
)
asxJ2AtmLCDCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxJ2AtmLCDCleared.setStatus(
        "current"
    )

asxJ2TLOCDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 232)
)
asxJ2TLOCDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxJ2TLOCDetected.setStatus(
        "current"
    )

asxJ2TLOCCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 233)
)
asxJ2TLOCCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxJ2TLOCCleared.setStatus(
        "current"
    )

asxTP25LOSDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 250)
)
asxTP25LOSDetected.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxTP25LOSDetected.setStatus(
        "current"
    )

asxTP25LOSCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 251)
)
asxTP25LOSCleared.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxTP25LOSCleared.setStatus(
        "current"
    )

asxOutputQueueCongested = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1024)
)
asxOutputQueueCongested.setObjects(
      *(("Fore-Switch-MIB", "portName"),
        ("Fore-Switch-MIB", "pshmemPriority"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxOutputQueueCongested.setStatus(
        "current"
    )

asxOutputQueueCellLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1025)
)
asxOutputQueueCellLoss.setObjects(
      *(("Fore-Switch-MIB", "portName"),
        ("Fore-Switch-MIB", "pshmemPriority"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxOutputQueueCellLoss.setStatus(
        "current"
    )

asxExtendedModeViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1026)
)
asxExtendedModeViolation.setObjects(
      *(("Fore-Switch-MIB", "moduleBoard"),
        ("Fore-Switch-MIB", "moduleNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxExtendedModeViolation.setStatus(
        "current"
    )

asxNonextendedModeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1027)
)
asxNonextendedModeWarning.setObjects(
      *(("Fore-Switch-MIB", "moduleBoard"),
        ("Fore-Switch-MIB", "moduleNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxNonextendedModeWarning.setStatus(
        "current"
    )

crConfMemoryOflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1029)
)
crConfMemoryOflow.setObjects(
      *(("Fore-Callrecord-MIB", "crMemoryAllocated"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    crConfMemoryOflow.setStatus(
        "current"
    )

crXfrPrimaryXfrFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1030)
)
crXfrPrimaryXfrFailed.setObjects(
      *(("Fore-Callrecord-MIB", "crXfrIndex"),
        ("Fore-Callrecord-MIB", "crXfrPrimaryTrapStatus"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    crXfrPrimaryXfrFailed.setStatus(
        "current"
    )

crXfrSecondaryXfrFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1031)
)
crXfrSecondaryXfrFailed.setObjects(
      *(("Fore-Callrecord-MIB", "crXfrIndex"),
        ("Fore-Callrecord-MIB", "crXfrSecondaryTrapStatus"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    crXfrSecondaryXfrFailed.setStatus(
        "current"
    )

crConfMemAllocFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1032)
)
crConfMemAllocFail.setObjects(
      *(("Fore-Callrecord-MIB", "crMemoryAllocated"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    crConfMemAllocFail.setStatus(
        "current"
    )

crGeneralFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1033)
)
crGeneralFailure.setObjects(
      *(("Fore-Callrecord-MIB", "crXfrIndex"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    crGeneralFailure.setStatus(
        "current"
    )

asxDualScpSyncFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1034)
)
asxDualScpSyncFailure.setObjects(
      *(("Fore-Switch-MIB", "boardIndex"),
        ("Fore-Switch-MIB", "dualScpSyncState"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDualScpSyncFailure.setStatus(
        "current"
    )

asxDualScpSwitchOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1035)
)
asxDualScpSwitchOver.setObjects(
      *(("Fore-Switch-MIB", "boardIndex"),
        ("Fore-Switch-MIB", "dualScpSlot"),
        ("Fore-Switch-MIB", "dualScpSwitchOverTime"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDualScpSwitchOver.setStatus(
        "current"
    )

asxDualScpHotSwap = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1036)
)
asxDualScpHotSwap.setObjects(
      *(("Fore-Switch-MIB", "boardIndex"),
        ("Fore-Switch-MIB", "dualScpSlot"),
        ("Fore-Switch-MIB", "dualScpState"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDualScpHotSwap.setStatus(
        "current"
    )

asxVPAISDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1037)
)
asxVPAISDetected.setObjects(
      *(("Fore-Switch-MIB", "portName"),
        ("Fore-Switch-MIB", "pathPort"),
        ("Fore-Switch-MIB", "pathVPI"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxVPAISDetected.setStatus(
        "current"
    )

asxVPAISCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1038)
)
asxVPAISCleared.setObjects(
      *(("Fore-Switch-MIB", "portName"),
        ("Fore-Switch-MIB", "pathPort"),
        ("Fore-Switch-MIB", "pathVPI"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxVPAISCleared.setStatus(
        "current"
    )

asxVPRDIDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1039)
)
asxVPRDIDetected.setObjects(
      *(("Fore-Switch-MIB", "portName"),
        ("Fore-Switch-MIB", "pathPort"),
        ("Fore-Switch-MIB", "pathVPI"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxVPRDIDetected.setStatus(
        "current"
    )

asxVPRDICleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1040)
)
asxVPRDICleared.setObjects(
      *(("Fore-Switch-MIB", "portName"),
        ("Fore-Switch-MIB", "pathPort"),
        ("Fore-Switch-MIB", "pathVPI"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxVPRDICleared.setStatus(
        "current"
    )

asxNonextendedModeViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1041)
)
asxNonextendedModeViolation.setObjects(
      *(("Fore-Switch-MIB", "moduleBoard"),
        ("Fore-Switch-MIB", "moduleNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxNonextendedModeViolation.setStatus(
        "current"
    )

asxUnsupportedNetworkModule = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1042)
)
asxUnsupportedNetworkModule.setObjects(
      *(("Fore-Switch-MIB", "moduleBoard"),
        ("Fore-Switch-MIB", "moduleNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxUnsupportedNetworkModule.setStatus(
        "current"
    )

asxDualScpRedundancy = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1043)
)
asxDualScpRedundancy.setObjects(
      *(("Fore-Switch-MIB", "boardIndex"),
        ("Fore-Switch-MIB", "dualScpSlot"),
        ("Fore-Switch-MIB", "dualScpRedundancyState"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxDualScpRedundancy.setStatus(
        "current"
    )

asxIpFilterViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1049)
)
asxIpFilterViolation.setObjects(
      *(("Fore-Adapter-MIB", "ipFilterStatsVPI"),
        ("Fore-Adapter-MIB", "ipFilterStatsVCI"),
        ("Fore-Adapter-MIB", "ipFilterStatsIfName"))
)
if mibBuilder.loadTexts:
    asxIpFilterViolation.setStatus(
        "current"
    )

q2931AFRejectKnown = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1053)
)
q2931AFRejectKnown.setObjects(
      *(("Fore-Switch-MIB", "portName"),
        ("Fore-Switch-MIB", "pathPort"),
        ("Fore-Switch-MIB", "pathVPI"),
        ("Fore-Switch-MIB", "portName"),
        ("Fore-Switch-MIB", "opathPort"),
        ("Fore-Switch-MIB", "opathVPI"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    q2931AFRejectKnown.setStatus(
        "current"
    )

q2931AFRejectUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1054)
)
q2931AFRejectUnknown.setObjects(
      *(("Fore-Switch-MIB", "portName"),
        ("Fore-Switch-MIB", "pathPort"),
        ("Fore-Switch-MIB", "pathVPI"),
        ("Fore-Switch-MIB", "portName"),
        ("Fore-Switch-MIB", "opathPort"),
        ("Fore-Switch-MIB", "opathVPI"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    q2931AFRejectUnknown.setStatus(
        "current"
    )

q2931CreationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1061)
)
q2931CreationFailure.setObjects(
      *(("Fore-Switch-MIB", "portName"),
        ("Fore-Switch-MIB", "q2931AdminPort"),
        ("Fore-Switch-MIB", "q2931AdminVPI"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    q2931CreationFailure.setStatus(
        "current"
    )

asxPsCurrentDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1068)
)
asxPsCurrentDown.setObjects(
      *(("Fore-Switch-MIB", "envPowerSupplyIndex"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxPsCurrentDown.setStatus(
        "current"
    )

asxPsCurrentUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1069)
)
asxPsCurrentUp.setObjects(
      *(("Fore-Switch-MIB", "envPowerSupplyIndex"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxPsCurrentUp.setStatus(
        "current"
    )

asxPs5VoltDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1070)
)
asxPs5VoltDown.setObjects(
      *(("Fore-Switch-MIB", "envPowerSupplyIndex"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxPs5VoltDown.setStatus(
        "current"
    )

asxPs5VoltUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1071)
)
asxPs5VoltUp.setObjects(
      *(("Fore-Switch-MIB", "envPowerSupplyIndex"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxPs5VoltUp.setStatus(
        "current"
    )

asxSwitchLoginDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1072)
)
asxSwitchLoginDetected.setObjects(
      *(("Fore-Switch-MIB", "switchCurrentUserid"),
        ("Fore-Switch-MIB", "switchCurrentLoginFrom"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxSwitchLoginDetected.setStatus(
        "current"
    )

asxSwitchLoginFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1073)
)
asxSwitchLoginFailed.setObjects(
      *(("Fore-Switch-MIB", "switchCurrentUserid"),
        ("Fore-Switch-MIB", "switchCurrentLoginFrom"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxSwitchLoginFailed.setStatus(
        "current"
    )

pnniTdbGuardbandResrvFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1074)
)
pnniTdbGuardbandResrvFail.setObjects(
      *(("PNNI-MIB", "pnniNodeId"),
        ("HOST-RESOURCES-MIB", "hrSystemDate"),
        ("Fore-Switch-MIB", "numBytesFree"),
        ("Fore-Switch-MIB", "numBlocksFree"),
        ("Fore-Switch-MIB", "numBlocksAlloc"),
        ("Fore-Switch-MIB", "maxBlockSizeFree"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    pnniTdbGuardbandResrvFail.setStatus(
        "current"
    )

pnniTdbInconsistentState = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1075)
)
pnniTdbInconsistentState.setObjects(
      *(("PNNI-MIB", "pnniNodeId"),
        ("HOST-RESOURCES-MIB", "hrSystemDate"),
        ("Fore-Switch-MIB", "numBytesFree"),
        ("Fore-Switch-MIB", "numBlocksFree"),
        ("Fore-Switch-MIB", "numBlocksAlloc"),
        ("Fore-Switch-MIB", "maxBlockSizeFree"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    pnniTdbInconsistentState.setStatus(
        "current"
    )

asxShmem2OutputQueueCongested = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1077)
)
asxShmem2OutputQueueCongested.setObjects(
      *(("Fore-Switch-MIB", "portName"),
        ("Fore-Switch-MIB", "pShmem2Priority"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxShmem2OutputQueueCongested.setStatus(
        "current"
    )

asxShmem2OutputQueueCellLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1078)
)
asxShmem2OutputQueueCellLoss.setObjects(
      *(("Fore-Switch-MIB", "portName"),
        ("Fore-Switch-MIB", "pShmem2Priority"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxShmem2OutputQueueCellLoss.setStatus(
        "current"
    )

fabricLvl3Lookup = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1080)
)
fabricLvl3Lookup.setObjects(
    ("Fore-Switch-MIB", "boardIndex")
)
if mibBuilder.loadTexts:
    fabricLvl3Lookup.setStatus(
        "current"
    )

fabricCorrectedLookup = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1081)
)
fabricCorrectedLookup.setObjects(
    ("Fore-Switch-MIB", "boardIndex")
)
if mibBuilder.loadTexts:
    fabricCorrectedLookup.setStatus(
        "current"
    )

spvcRerouteInitiated = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1090)
)
spvcRerouteInitiated.setObjects(
      *(("Fore-Switch-MIB", "boardIndex"),
        ("Fore-Switch-MIB", "spvcSrcInPort"),
        ("Fore-Switch-MIB", "spvcSrcInVPI"),
        ("Fore-Switch-MIB", "spvcSrcInVCI"))
)
if mibBuilder.loadTexts:
    spvcRerouteInitiated.setStatus(
        "current"
    )

asxQ2931Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1091)
)
asxQ2931Down.setObjects(
      *(("Fore-Switch-MIB", "portName"),
        ("Fore-Switch-MIB", "q2931AdminPort"),
        ("Fore-Switch-MIB", "q2931AdminVPI"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxQ2931Down.setStatus(
        "current"
    )

asxQ2931Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1092)
)
asxQ2931Up.setObjects(
      *(("Fore-Switch-MIB", "portName"),
        ("Fore-Switch-MIB", "q2931AdminPort"),
        ("Fore-Switch-MIB", "q2931AdminVPI"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxQ2931Up.setStatus(
        "current"
    )

asxFabricDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1093)
)
asxFabricDown.setObjects(
      *(("Fore-Switch-MIB", "boardIndex"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxFabricDown.setStatus(
        "current"
    )

asxFabricUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1094)
)
asxFabricUp.setObjects(
      *(("Fore-Switch-MIB", "boardIndex"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxFabricUp.setStatus(
        "current"
    )

asxQ2931CallClearing = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1095)
)
asxQ2931CallClearing.setObjects(
      *(("Fore-Switch-MIB", "portName"),
        ("Fore-Switch-MIB", "q2931AdminPort"),
        ("Fore-Switch-MIB", "q2931AdminVPI"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxQ2931CallClearing.setStatus(
        "current"
    )

pnniSpvccDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 2004)
)
pnniSpvccDown.setObjects(
      *(("Fore-Switch-MIB", "boardIndex"),
        ("Fore-Switch-MIB", "pnniSpvcSrcCallingPort"),
        ("Fore-Switch-MIB", "pnniSpvcSrcCallingVPI"),
        ("Fore-Switch-MIB", "pnniSpvcSrcCallingVCI"),
        ("Fore-Switch-MIB", "pnniSpvcSrcDownReason"),
        ("Fore-Switch-MIB", "pnniSpvcSrcName"),
        ("Fore-Switch-MIB", "pnniSpvcSrcLastFailCause"),
        ("Fore-Switch-MIB", "pnniSpvcSrcLastLocation"))
)
if mibBuilder.loadTexts:
    pnniSpvccDown.setStatus(
        "current"
    )

pnniSpvccUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 2005)
)
pnniSpvccUp.setObjects(
      *(("Fore-Switch-MIB", "boardIndex"),
        ("Fore-Switch-MIB", "pnniSpvcSrcCallingPort"),
        ("Fore-Switch-MIB", "pnniSpvcSrcCallingVPI"),
        ("Fore-Switch-MIB", "pnniSpvcSrcCallingVCI"),
        ("Fore-Switch-MIB", "pnniSpvcSrcOldRouteCost"),
        ("Fore-Switch-MIB", "pnniSpvcSrcName"),
        ("Fore-Switch-MIB", "pnniSpvcSrcRouteCost"))
)
if mibBuilder.loadTexts:
    pnniSpvccUp.setStatus(
        "current"
    )

pnniSpvccFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 2006)
)
pnniSpvccFail.setObjects(
      *(("Fore-Switch-MIB", "boardIndex"),
        ("Fore-Switch-MIB", "pnniSpvcSrcCallingPort"),
        ("Fore-Switch-MIB", "pnniSpvcSrcCallingVPI"),
        ("Fore-Switch-MIB", "pnniSpvcSrcCallingVCI"),
        ("Fore-Switch-MIB", "pnniSpvcSrcDownReason"),
        ("Fore-Switch-MIB", "pnniSpvcSrcName"),
        ("Fore-Switch-MIB", "pnniSpvcSrcLastFailCause"),
        ("Fore-Switch-MIB", "pnniSpvcSrcLastLocation"))
)
if mibBuilder.loadTexts:
    pnniSpvccFail.setStatus(
        "current"
    )

pnniSpvpcDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 2007)
)
pnniSpvpcDown.setObjects(
      *(("Fore-Switch-MIB", "boardIndex"),
        ("Fore-Switch-MIB", "pnniSpvpcSrcCallingPort"),
        ("Fore-Switch-MIB", "pnniSpvpcSrcCallingVPI"),
        ("Fore-Switch-MIB", "pnniSpvpcSrcDownReason"),
        ("Fore-Switch-MIB", "pnniSpvpcSrcName"),
        ("Fore-Switch-MIB", "pnniSpvpcSrcLastFailCause"),
        ("Fore-Switch-MIB", "pnniSpvpcSrcLastLocation"))
)
if mibBuilder.loadTexts:
    pnniSpvpcDown.setStatus(
        "current"
    )

pnniSpvpcUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 2008)
)
pnniSpvpcUp.setObjects(
      *(("Fore-Switch-MIB", "boardIndex"),
        ("Fore-Switch-MIB", "pnniSpvpcSrcCallingPort"),
        ("Fore-Switch-MIB", "pnniSpvpcSrcCallingVPI"),
        ("Fore-Switch-MIB", "pnniSpvpcSrcOldRouteCost"),
        ("Fore-Switch-MIB", "pnniSpvpcSrcName"),
        ("Fore-Switch-MIB", "pnniSpvpcSrcRouteCost"))
)
if mibBuilder.loadTexts:
    pnniSpvpcUp.setStatus(
        "current"
    )

pnniSpvpcFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 2009)
)
pnniSpvpcFail.setObjects(
      *(("Fore-Switch-MIB", "boardIndex"),
        ("Fore-Switch-MIB", "pnniSpvpcSrcCallingPort"),
        ("Fore-Switch-MIB", "pnniSpvpcSrcCallingVPI"),
        ("Fore-Switch-MIB", "pnniSpvpcSrcDownReason"),
        ("Fore-Switch-MIB", "pnniSpvpcSrcName"),
        ("Fore-Switch-MIB", "pnniSpvpcSrcLastFailCause"),
        ("Fore-Switch-MIB", "pnniSpvpcSrcLastLocation"))
)
if mibBuilder.loadTexts:
    pnniSpvpcFail.setStatus(
        "current"
    )

asxPortCardDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 2010)
)
asxPortCardDown.setObjects(
      *(("Fore-Switch-MIB", "portCardName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxPortCardDown.setStatus(
        "current"
    )

asxPortCardUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 2011)
)
asxPortCardUp.setObjects(
      *(("Fore-Switch-MIB", "portCardName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxPortCardUp.setStatus(
        "current"
    )

asxServiceCategoryOutputQueueCongested = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 2013)
)
asxServiceCategoryOutputQueueCongested.setObjects(
      *(("Fore-Switch-MIB", "portName"),
        ("Fore-Switch-MIB", "serviceCategoryName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxServiceCategoryOutputQueueCongested.setStatus(
        "current"
    )

asxServiceCategoryOutputQueueCellLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 2014)
)
asxServiceCategoryOutputQueueCellLoss.setObjects(
      *(("Fore-Switch-MIB", "portName"),
        ("Fore-Switch-MIB", "serviceCategoryName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxServiceCategoryOutputQueueCellLoss.setStatus(
        "current"
    )

pnniNormalToOverloadTransition = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 2015)
)
pnniNormalToOverloadTransition.setObjects(
      *(("PNNI-MIB", "pnniNodeId"),
        ("HOST-RESOURCES-MIB", "hrSystemDate"),
        ("Fore-Switch-MIB", "numBytesFree"),
        ("Fore-Switch-MIB", "numBlocksFree"),
        ("Fore-Switch-MIB", "numBlocksAlloc"),
        ("Fore-Switch-MIB", "maxBlockSizeFree"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    pnniNormalToOverloadTransition.setStatus(
        "current"
    )

pnniOverloadToNormalTransition = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 2016)
)
pnniOverloadToNormalTransition.setObjects(
      *(("PNNI-MIB", "pnniNodeId"),
        ("HOST-RESOURCES-MIB", "hrSystemDate"),
        ("Fore-Switch-MIB", "numBytesFree"),
        ("Fore-Switch-MIB", "numBlocksFree"),
        ("Fore-Switch-MIB", "numBlocksAlloc"),
        ("Fore-Switch-MIB", "maxBlockSizeFree"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    pnniOverloadToNormalTransition.setStatus(
        "current"
    )

pnniPmpRerouteInitiated = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 2020)
)
pnniPmpRerouteInitiated.setObjects(
      *(("Fore-Switch-MIB", "pnniPmpSpvccSrcRootPort"),
        ("Fore-Switch-MIB", "pnniPmpSpvccSrcRootVPI"),
        ("Fore-Switch-MIB", "pnniPmpSpvccSrcRootVCI"))
)
if mibBuilder.loadTexts:
    pnniPmpRerouteInitiated.setStatus(
        "current"
    )

pnniPmpSpvcUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 2021)
)
pnniPmpSpvcUp.setObjects(
      *(("Fore-Switch-MIB", "pnniPmpSpvccSrcRootPort"),
        ("Fore-Switch-MIB", "pnniPmpSpvccSrcRootVPI"),
        ("Fore-Switch-MIB", "pnniPmpSpvccSrcRootVCI"),
        ("Fore-Switch-MIB", "pnniPmpSpvccSrcPartyName"),
        ("Fore-Switch-MIB", "pnniPmpSpvccSrcPartyRouteCost"))
)
if mibBuilder.loadTexts:
    pnniPmpSpvcUp.setStatus(
        "current"
    )

pnniPmpSpvcDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 2022)
)
pnniPmpSpvcDown.setObjects(
      *(("Fore-Switch-MIB", "pnniPmpSpvccSrcRootPort"),
        ("Fore-Switch-MIB", "pnniPmpSpvccSrcRootVPI"),
        ("Fore-Switch-MIB", "pnniPmpSpvccSrcRootVCI"),
        ("Fore-Switch-MIB", "pnniPmpSpvccSrcPartyDownReason"),
        ("Fore-Switch-MIB", "pnniPmpSpvccSrcPartyName"),
        ("Fore-Switch-MIB", "pnniPmpSpvccSrcPartyLastFailCause"),
        ("Fore-Switch-MIB", "pnniPmpSpvccSrcPartyLastLocation"))
)
if mibBuilder.loadTexts:
    pnniPmpSpvcDown.setStatus(
        "current"
    )

pnniPmpSpvcFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 2023)
)
pnniPmpSpvcFail.setObjects(
      *(("Fore-Switch-MIB", "pnniPmpSpvccSrcRootPort"),
        ("Fore-Switch-MIB", "pnniPmpSpvccSrcRootVPI"),
        ("Fore-Switch-MIB", "pnniPmpSpvccSrcRootVCI"),
        ("Fore-Switch-MIB", "pnniPmpSpvccSrcPartyDownReason"),
        ("Fore-Switch-MIB", "pnniPmpSpvccSrcPartyName"),
        ("Fore-Switch-MIB", "pnniPmpSpvccSrcPartyLastFailCause"),
        ("Fore-Switch-MIB", "pnniPmpSpvccSrcPartyLastLocation"))
)
if mibBuilder.loadTexts:
    pnniPmpSpvcFail.setStatus(
        "current"
    )

pnniSpvxRGroupSwover = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 2024)
)
pnniSpvxRGroupSwover.setObjects(
      *(("Fore-Switch-MIB", "pnniSpvxcRGroupSwitchoverCmd"),
        ("Fore-Switch-MIB", "pnniSpvxcRGroupActivePort"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    pnniSpvxRGroupSwover.setStatus(
        "current"
    )

asxSVXCPStateTransferFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 2025)
)
asxSVXCPStateTransferFailed.setObjects(
      *(("Fore-Switch-MIB", "dualScpSlot"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxSVXCPStateTransferFailed.setStatus(
        "current"
    )

asxSVXCPStateTransferRestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 2026)
)
asxSVXCPStateTransferRestarted.setObjects(
      *(("Fore-Switch-MIB", "dualScpSlot"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    asxSVXCPStateTransferRestarted.setStatus(
        "current"
    )

asxSVXCPStateDroppedCall = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 2027)
)
asxSVXCPStateDroppedCall.setObjects(
    ("Fore-TrapLog-MIB", "trapLogIndex")
)
if mibBuilder.loadTexts:
    asxSVXCPStateDroppedCall.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-Switch-MIB",
    **{"E164Address": E164Address,
       "AtmConnSchedMode": AtmConnSchedMode,
       "AtmOrigPathSchedMode": AtmOrigPathSchedMode,
       "AAL5CountingMode": AAL5CountingMode,
       "asxSwLinkDown": asxSwLinkDown,
       "asxSwLinkUp": asxSwLinkUp,
       "asxHostLinkDown": asxHostLinkDown,
       "asxHostLinkUp": asxHostLinkUp,
       "asxNetModuleDown": asxNetModuleDown,
       "asxNetModuleUp": asxNetModuleUp,
       "asxPsInputDown": asxPsInputDown,
       "asxPsInputUp": asxPsInputUp,
       "asxPsOutputDown": asxPsOutputDown,
       "asxPsOutputUp": asxPsOutputUp,
       "asxFanBankDown": asxFanBankDown,
       "asxFanBankUp": asxFanBankUp,
       "asxLinkDown": asxLinkDown,
       "asxLinkUp": asxLinkUp,
       "asxSpansDown": asxSpansDown,
       "asxSpansUp": asxSpansUp,
       "asxTempSensorOverTemp": asxTempSensorOverTemp,
       "asxTempSensorRegularTemp": asxTempSensorRegularTemp,
       "asxFabricTemperatureOverTemp": asxFabricTemperatureOverTemp,
       "asxFabricTemperatureRegularTemp": asxFabricTemperatureRegularTemp,
       "asxSonetLOSDetected": asxSonetLOSDetected,
       "asxSonetLOSCleared": asxSonetLOSCleared,
       "asxSonetPathLabelDetected": asxSonetPathLabelDetected,
       "asxSonetPathLabelCleared": asxSonetPathLabelCleared,
       "asxSonetLineAISDetected": asxSonetLineAISDetected,
       "asxSonetLineAISCleared": asxSonetLineAISCleared,
       "asxDS3PLCPYellowDetected": asxDS3PLCPYellowDetected,
       "asxDS3PLCPYellowCleared": asxDS3PLCPYellowCleared,
       "asxDS3PLCPLOFDetected": asxDS3PLCPLOFDetected,
       "asxDS3PLCPLOFCleared": asxDS3PLCPLOFCleared,
       "asxDS3LOFDetected": asxDS3LOFDetected,
       "asxDS3LOFCleared": asxDS3LOFCleared,
       "asxDS3AISDetected": asxDS3AISDetected,
       "asxDS3AISCleared": asxDS3AISCleared,
       "asxDS1PLCPYellowDetected": asxDS1PLCPYellowDetected,
       "asxDS1PLCPYellowCleared": asxDS1PLCPYellowCleared,
       "asxDS1PLCPLOFDetected": asxDS1PLCPLOFDetected,
       "asxDS1PLCPLOFCleared": asxDS1PLCPLOFCleared,
       "asxDS1YellowDetected": asxDS1YellowDetected,
       "asxDS1YellowCleared": asxDS1YellowCleared,
       "asxDS1AISDetected": asxDS1AISDetected,
       "asxDS1AISCleared": asxDS1AISCleared,
       "asxDS1LOSDetected": asxDS1LOSDetected,
       "asxDS1LOSCleared": asxDS1LOSCleared,
       "asxDS1LOFDetected": asxDS1LOFDetected,
       "asxDS1LOFCleared": asxDS1LOFCleared,
       "asxDS3FERFDetected": asxDS3FERFDetected,
       "asxDS3FERFCleared": asxDS3FERFCleared,
       "asxE3YellowDetected": asxE3YellowDetected,
       "asxE3YellowCleared": asxE3YellowCleared,
       "asxE3OOFDetected": asxE3OOFDetected,
       "asxE3OOFCleared": asxE3OOFCleared,
       "asxE3AtmLCDDetected": asxE3AtmLCDDetected,
       "asxE3AtmLCDCleared": asxE3AtmLCDCleared,
       "asxE3PLCPYellowDetected": asxE3PLCPYellowDetected,
       "asxE3PLCPYellowCleared": asxE3PLCPYellowCleared,
       "asxE1YellowDetected": asxE1YellowDetected,
       "asxE1YellowCleared": asxE1YellowCleared,
       "asxE1LOFDetected": asxE1LOFDetected,
       "asxE1LOFCleared": asxE1LOFCleared,
       "asxE1PLCPYellowDetected": asxE1PLCPYellowDetected,
       "asxE1PLCPYellowCleared": asxE1PLCPYellowCleared,
       "asxE1PLCPLOFDetected": asxE1PLCPLOFDetected,
       "asxE1PLCPLOFCleared": asxE1PLCPLOFCleared,
       "asxE1LOSDetected": asxE1LOSDetected,
       "asxE1LOSCleared": asxE1LOSCleared,
       "asxE1AISDetected": asxE1AISDetected,
       "asxE1AISCleared": asxE1AISCleared,
       "asxE3AISDetected": asxE3AISDetected,
       "asxE3AISCleared": asxE3AISCleared,
       "asxE3LOSDetected": asxE3LOSDetected,
       "asxE3LOSCleared": asxE3LOSCleared,
       "asxE3PLCPLOFDetected": asxE3PLCPLOFDetected,
       "asxE3PLCPLOFCleared": asxE3PLCPLOFCleared,
       "asxJ2YellowDetected": asxJ2YellowDetected,
       "asxJ2YellowCleared": asxJ2YellowCleared,
       "asxJ2AISDetected": asxJ2AISDetected,
       "asxJ2AISCleared": asxJ2AISCleared,
       "asxJ2LOSDetected": asxJ2LOSDetected,
       "asxJ2LOSCleared": asxJ2LOSCleared,
       "asxJ2LOFDetected": asxJ2LOFDetected,
       "asxJ2LOFCleared": asxJ2LOFCleared,
       "asxDS3LOSDetected": asxDS3LOSDetected,
       "asxDS3LOSCleared": asxDS3LOSCleared,
       "asxSonetLOFDetected": asxSonetLOFDetected,
       "asxSonetLOFCleared": asxSonetLOFCleared,
       "asxSonetLineRDIDetected": asxSonetLineRDIDetected,
       "asxSonetLineRDICleared": asxSonetLineRDICleared,
       "asxSonetPathAISDetected": asxSonetPathAISDetected,
       "asxSonetPathAISCleared": asxSonetPathAISCleared,
       "asxSonetPathLOPDetected": asxSonetPathLOPDetected,
       "asxSonetPathLOPCleared": asxSonetPathLOPCleared,
       "asxSonetPathUNEQDetected": asxSonetPathUNEQDetected,
       "asxSonetPathUNEQCleared": asxSonetPathUNEQCleared,
       "asxSonetPathRDIDetected": asxSonetPathRDIDetected,
       "asxSonetPathRDICleared": asxSonetPathRDICleared,
       "asxSonetAtmLCDDetected": asxSonetAtmLCDDetected,
       "asxSonetAtmLCDCleared": asxSonetAtmLCDCleared,
       "asxSonetAtmLineBIPDetected": asxSonetAtmLineBIPDetected,
       "asxSonetAtmLineBIPCleared": asxSonetAtmLineBIPCleared,
       "asxDS3IdleDetected": asxDS3IdleDetected,
       "asxDS3IdleCleared": asxDS3IdleCleared,
       "asxDS3AtmLCDDetected": asxDS3AtmLCDDetected,
       "asxDS3AtmLCDCleared": asxDS3AtmLCDCleared,
       "asxDS3PbitPerrDetected": asxDS3PbitPerrDetected,
       "asxDS3PbitPerrCleared": asxDS3PbitPerrCleared,
       "asxDS1PRBSDetected": asxDS1PRBSDetected,
       "asxDS1PRBSCleared": asxDS1PRBSCleared,
       "asxDS1AtmLCDDetected": asxDS1AtmLCDDetected,
       "asxDS1AtmLCDCleared": asxDS1AtmLCDCleared,
       "asxDS1CRCErrDetected": asxDS1CRCErrDetected,
       "asxDS1CRCErrCleared": asxDS1CRCErrCleared,
       "asxE3TrailChangeDetected": asxE3TrailChangeDetected,
       "asxE1AtmLCDDetected": asxE1AtmLCDDetected,
       "asxE1AtmLCDCleared": asxE1AtmLCDCleared,
       "asxJ2RLOCDetected": asxJ2RLOCDetected,
       "asxJ2RLOCCleared": asxJ2RLOCCleared,
       "asxJ2HBERDetected": asxJ2HBERDetected,
       "asxJ2HBERCleared": asxJ2HBERCleared,
       "asxJ2PAISDetected": asxJ2PAISDetected,
       "asxJ2PAISCleared": asxJ2PAISCleared,
       "asxJ2AtmLCDDetected": asxJ2AtmLCDDetected,
       "asxJ2AtmLCDCleared": asxJ2AtmLCDCleared,
       "asxJ2TLOCDetected": asxJ2TLOCDetected,
       "asxJ2TLOCCleared": asxJ2TLOCCleared,
       "asxTP25LOSDetected": asxTP25LOSDetected,
       "asxTP25LOSCleared": asxTP25LOSCleared,
       "asxOutputQueueCongested": asxOutputQueueCongested,
       "asxOutputQueueCellLoss": asxOutputQueueCellLoss,
       "asxExtendedModeViolation": asxExtendedModeViolation,
       "asxNonextendedModeWarning": asxNonextendedModeWarning,
       "crConfMemoryOflow": crConfMemoryOflow,
       "crXfrPrimaryXfrFailed": crXfrPrimaryXfrFailed,
       "crXfrSecondaryXfrFailed": crXfrSecondaryXfrFailed,
       "crConfMemAllocFail": crConfMemAllocFail,
       "crGeneralFailure": crGeneralFailure,
       "asxDualScpSyncFailure": asxDualScpSyncFailure,
       "asxDualScpSwitchOver": asxDualScpSwitchOver,
       "asxDualScpHotSwap": asxDualScpHotSwap,
       "asxVPAISDetected": asxVPAISDetected,
       "asxVPAISCleared": asxVPAISCleared,
       "asxVPRDIDetected": asxVPRDIDetected,
       "asxVPRDICleared": asxVPRDICleared,
       "asxNonextendedModeViolation": asxNonextendedModeViolation,
       "asxUnsupportedNetworkModule": asxUnsupportedNetworkModule,
       "asxDualScpRedundancy": asxDualScpRedundancy,
       "asxIpFilterViolation": asxIpFilterViolation,
       "q2931AFRejectKnown": q2931AFRejectKnown,
       "q2931AFRejectUnknown": q2931AFRejectUnknown,
       "q2931CreationFailure": q2931CreationFailure,
       "asxPsCurrentDown": asxPsCurrentDown,
       "asxPsCurrentUp": asxPsCurrentUp,
       "asxPs5VoltDown": asxPs5VoltDown,
       "asxPs5VoltUp": asxPs5VoltUp,
       "asxSwitchLoginDetected": asxSwitchLoginDetected,
       "asxSwitchLoginFailed": asxSwitchLoginFailed,
       "pnniTdbGuardbandResrvFail": pnniTdbGuardbandResrvFail,
       "pnniTdbInconsistentState": pnniTdbInconsistentState,
       "asxShmem2OutputQueueCongested": asxShmem2OutputQueueCongested,
       "asxShmem2OutputQueueCellLoss": asxShmem2OutputQueueCellLoss,
       "fabricLvl3Lookup": fabricLvl3Lookup,
       "fabricCorrectedLookup": fabricCorrectedLookup,
       "spvcRerouteInitiated": spvcRerouteInitiated,
       "asxQ2931Down": asxQ2931Down,
       "asxQ2931Up": asxQ2931Up,
       "asxFabricDown": asxFabricDown,
       "asxFabricUp": asxFabricUp,
       "asxQ2931CallClearing": asxQ2931CallClearing,
       "pnniSpvccDown": pnniSpvccDown,
       "pnniSpvccUp": pnniSpvccUp,
       "pnniSpvccFail": pnniSpvccFail,
       "pnniSpvpcDown": pnniSpvpcDown,
       "pnniSpvpcUp": pnniSpvpcUp,
       "pnniSpvpcFail": pnniSpvpcFail,
       "asxPortCardDown": asxPortCardDown,
       "asxPortCardUp": asxPortCardUp,
       "asxServiceCategoryOutputQueueCongested": asxServiceCategoryOutputQueueCongested,
       "asxServiceCategoryOutputQueueCellLoss": asxServiceCategoryOutputQueueCellLoss,
       "pnniNormalToOverloadTransition": pnniNormalToOverloadTransition,
       "pnniOverloadToNormalTransition": pnniOverloadToNormalTransition,
       "pnniPmpRerouteInitiated": pnniPmpRerouteInitiated,
       "pnniPmpSpvcUp": pnniPmpSpvcUp,
       "pnniPmpSpvcDown": pnniPmpSpvcDown,
       "pnniPmpSpvcFail": pnniPmpSpvcFail,
       "pnniSpvxRGroupSwover": pnniSpvxRGroupSwover,
       "asxSVXCPStateTransferFailed": asxSVXCPStateTransferFailed,
       "asxSVXCPStateTransferRestarted": asxSVXCPStateTransferRestarted,
       "asxSVXCPStateDroppedCall": asxSVXCPStateDroppedCall,
       "boardGroup": boardGroup,
       "boardTable": boardTable,
       "boardEntry": boardEntry,
       "boardIndex": boardIndex,
       "boardVersion": boardVersion,
       "boardModel": boardModel,
       "boardSerialNumber": boardSerialNumber,
       "numberOfModules": numberOfModules,
       "vpiLookupErrors": vpiLookupErrors,
       "vciLookupErrors": vciLookupErrors,
       "boardControlPort": boardControlPort,
       "boardHDCOMPAsicVersion": boardHDCOMPAsicVersion,
       "boardMcastSpaceIndex": boardMcastSpaceIndex,
       "numberOfBoards": numberOfBoards,
       "utilization": utilization,
       "procUtilGroup": procUtilGroup,
       "procUtilLastUpdate": procUtilLastUpdate,
       "procUtilValue": procUtilValue,
       "procUtilMonInterval": procUtilMonInterval,
       "procUtilMinLoad": procUtilMinLoad,
       "procUtilMinLoadLastUpdate": procUtilMinLoadLastUpdate,
       "procUtilMaxLoad": procUtilMaxLoad,
       "procUtilMaxLoadLastUpdate": procUtilMaxLoadLastUpdate,
       "procUtilHistoryReset": procUtilHistoryReset,
       "procUtilsNumMallocPart": procUtilsNumMallocPart,
       "procUtilsSystemPartitionID": procUtilsSystemPartitionID,
       "mallocUtilTable": mallocUtilTable,
       "mallocUtilEntry": mallocUtilEntry,
       "mallocPartId": mallocPartId,
       "numBytesFree": numBytesFree,
       "numBlocksFree": numBlocksFree,
       "maxBlockSizeFree": maxBlockSizeFree,
       "numBytesAlloc": numBytesAlloc,
       "numBlocksAlloc": numBlocksAlloc,
       "mbufUtilGroup": mbufUtilGroup,
       "mbufsCount": mbufsCount,
       "mbufsClusters": mbufsClusters,
       "mbufsSpace": mbufsSpace,
       "mbufsClFree": mbufsClFree,
       "mbufsDrops": mbufsDrops,
       "mbufsWait": mbufsWait,
       "mbufsDrain": mbufsDrain,
       "mbufsFreeAlloc": mbufsFreeAlloc,
       "mbufsDataFreeAlloc": mbufsDataFreeAlloc,
       "mbufsHeaderAlloc": mbufsHeaderAlloc,
       "mbufsSocketAlloc": mbufsSocketAlloc,
       "mbufsPcbAlloc": mbufsPcbAlloc,
       "mbufsRtableAlloc": mbufsRtableAlloc,
       "mbufsHtableAlloc": mbufsHtableAlloc,
       "mbufsAtableAlloc": mbufsAtableAlloc,
       "mbufsSoNameAlloc": mbufsSoNameAlloc,
       "mbufsZombieAlloc": mbufsZombieAlloc,
       "mbufsSoOptsAlloc": mbufsSoOptsAlloc,
       "mbufsFtableAlloc": mbufsFtableAlloc,
       "mbufsRightsAlloc": mbufsRightsAlloc,
       "mbufsIFaddrAlloc": mbufsIFaddrAlloc,
       "boardStatsTable": boardStatsTable,
       "boardStatsEntry": boardStatsEntry,
       "boardStatsBoard": boardStatsBoard,
       "boardStatsIndex": boardStatsIndex,
       "boardStatsName": boardStatsName,
       "boardStatsValue": boardStatsValue,
       "portCardGroup": portCardGroup,
       "portCardTable": portCardTable,
       "portCardEntry": portCardEntry,
       "portCardIndex": portCardIndex,
       "portCardName": portCardName,
       "portCardFlavor": portCardFlavor,
       "portCardType": portCardType,
       "portCardUptime": portCardUptime,
       "portCardSerialNumber": portCardSerialNumber,
       "portCardAssemblyRevision": portCardAssemblyRevision,
       "portCardHardwareConf": portCardHardwareConf,
       "portCardState": portCardState,
       "boardTrafficManagementGroup": boardTrafficManagementGroup,
       "boardTrafficManagementPerPriorityTable": boardTrafficManagementPerPriorityTable,
       "boardTrafficManagementPerPriorityEntry": boardTrafficManagementPerPriorityEntry,
       "btmPerPriorityBoard": btmPerPriorityBoard,
       "btmPerPriorityPriority": btmPerPriorityPriority,
       "btmPerPriorityFeature": btmPerPriorityFeature,
       "btmPerPriorityPriorityName": btmPerPriorityPriorityName,
       "btmPerPriorityValue": btmPerPriorityValue,
       "moduleGroup": moduleGroup,
       "moduleTable": moduleTable,
       "moduleEntry": moduleEntry,
       "moduleBoard": moduleBoard,
       "moduleNumber": moduleNumber,
       "moduleName": moduleName,
       "moduleSpeed": moduleSpeed,
       "moduleNumberOfPorts": moduleNumberOfPorts,
       "moduleUptime": moduleUptime,
       "moduleHwMajorRev": moduleHwMajorRev,
       "moduleHwMinorRev": moduleHwMinorRev,
       "moduleVersion": moduleVersion,
       "moduleTimingSupport": moduleTimingSupport,
       "moduleProductNumber": moduleProductNumber,
       "moduleState": moduleState,
       "moduleSerialNumber": moduleSerialNumber,
       "moduleTestAdminStatus": moduleTestAdminStatus,
       "moduleTestOperStatus": moduleTestOperStatus,
       "moduleTestStatusText": moduleTestStatusText,
       "moduleAttachState": moduleAttachState,
       "moduleCLEI": moduleCLEI,
       "outputBufferTable": outputBufferTable,
       "outputBufferEntry": outputBufferEntry,
       "obufBoard": obufBoard,
       "obufNumber": obufNumber,
       "obufType": obufType,
       "obufOperStatus": obufOperStatus,
       "obufBufferSize": obufBufferSize,
       "obufQueueLength": obufQueueLength,
       "obufOverflows": obufOverflows,
       "obufPriorityName": obufPriorityName,
       "obufName": obufName,
       "hwPortTable": hwPortTable,
       "hwPortEntry": hwPortEntry,
       "hwPortBoard": hwPortBoard,
       "hwPortModule": hwPortModule,
       "hwPortNumber": hwPortNumber,
       "hwPortVersion": hwPortVersion,
       "hwPortModel": hwPortModel,
       "hwPortOperStatus": hwPortOperStatus,
       "hwPortBufferSize": hwPortBufferSize,
       "hwPortQueueLength": hwPortQueueLength,
       "hwPortOverflows": hwPortOverflows,
       "hwPortErrors": hwPortErrors,
       "hwPortCarrier": hwPortCarrier,
       "hwPortGlobalIndex": hwPortGlobalIndex,
       "hwPortName": hwPortName,
       "hwPortAdminStatus": hwPortAdminStatus,
       "hwPortTAXILoopback": hwPortTAXILoopback,
       "hwPortLEDModel": hwPortLEDModel,
       "hwPortTxLED": hwPortTxLED,
       "hwPortRxLED": hwPortRxLED,
       "hwPortIfIndex": hwPortIfIndex,
       "hwPortRxSyncLED": hwPortRxSyncLED,
       "hwPortCounterResetTime": hwPortCounterResetTime,
       "hwPortCounterReset": hwPortCounterReset,
       "hwPortSpeed": hwPortSpeed,
       "netmodAlarmsTable": netmodAlarmsTable,
       "netmodAlarmsEntry": netmodAlarmsEntry,
       "netmodSlot": netmodSlot,
       "netmodSlotPriority": netmodSlotPriority,
       "netmodStatus": netmodStatus,
       "netmodName": netmodName,
       "hdcompTable": hdcompTable,
       "hdcompEntry": hdcompEntry,
       "hdcompIndex": hdcompIndex,
       "hdcompDescr": hdcompDescr,
       "hdcompAsicVersion": hdcompAsicVersion,
       "hdcompVpiLookupErrors": hdcompVpiLookupErrors,
       "hdcompVciLookupErrors": hdcompVciLookupErrors,
       "appModuleTable": appModuleTable,
       "appModuleEntry": appModuleEntry,
       "appModuleIndex": appModuleIndex,
       "appModuleName": appModuleName,
       "appModuleOperState": appModuleOperState,
       "appModuleStatusText": appModuleStatusText,
       "appModuleApplicationType": appModuleApplicationType,
       "appModuleSoftwareVersion": appModuleSoftwareVersion,
       "appModuleBootSoftwareVersion": appModuleBootSoftwareVersion,
       "appModuleOosLed": appModuleOosLed,
       "appModulePanicAction": appModulePanicAction,
       "timing": timing,
       "netmodTimingGroup": netmodTimingGroup,
       "netmodTimingTable": netmodTimingTable,
       "netmodTimingEntry": netmodTimingEntry,
       "ntBoard": ntBoard,
       "ntModule": ntModule,
       "ntPrimaryRecoveredClock": ntPrimaryRecoveredClock,
       "ntSecondaryRecoveredClock": ntSecondaryRecoveredClock,
       "ntPrimaryExportClock": ntPrimaryExportClock,
       "ntSecondaryExportClock": ntSecondaryExportClock,
       "ntGlobalClock": ntGlobalClock,
       "ntExportClockOperStatus": ntExportClockOperStatus,
       "ntPrimaryImportClock": ntPrimaryImportClock,
       "ntSecondaryImportClock": ntSecondaryImportClock,
       "ntImportClockOperStatus": ntImportClockOperStatus,
       "boardTimingGroup": boardTimingGroup,
       "boardTimingTable": boardTimingTable,
       "boardTimingEntry": boardTimingEntry,
       "btBoard": btBoard,
       "btPrimaryClock": btPrimaryClock,
       "btSecondaryClock": btSecondaryClock,
       "btPrimaryClockOperStatus": btPrimaryClockOperStatus,
       "btSecondaryClockOperStatus": btSecondaryClockOperStatus,
       "environment": environment,
       "alarmGroup": alarmGroup,
       "swAlarmTable": swAlarmTable,
       "swAlarmEntry": swAlarmEntry,
       "swAlarmType": swAlarmType,
       "swAlarmStatus": swAlarmStatus,
       "swAlarmMinorCategory": swAlarmMinorCategory,
       "swAlarmMajorCategory": swAlarmMajorCategory,
       "swAlarmReset": swAlarmReset,
       "swAlarmCriticalCategory": swAlarmCriticalCategory,
       "swAlarmACOState": swAlarmACOState,
       "swAlarmMajorRelayState": swAlarmMajorRelayState,
       "swAlarmMinorRelayState": swAlarmMinorRelayState,
       "swAlarmCriticalRelayState": swAlarmCriticalRelayState,
       "swAlarmRelayTable": swAlarmRelayTable,
       "swAlarmRelayEntry": swAlarmRelayEntry,
       "swAlarmRelayIndex": swAlarmRelayIndex,
       "swAlarmRelayFunction": swAlarmRelayFunction,
       "swAlarmRelayState": swAlarmRelayState,
       "swAlarmRelayOperMode": swAlarmRelayOperMode,
       "powerGroup": powerGroup,
       "envMaxNumberOfPowerSupplies": envMaxNumberOfPowerSupplies,
       "envNumberOfPowerSupplies": envNumberOfPowerSupplies,
       "envPowerSupplyTable": envPowerSupplyTable,
       "envPowerSupplyEntry": envPowerSupplyEntry,
       "envPowerSupplyIndex": envPowerSupplyIndex,
       "envPowerSupplyType": envPowerSupplyType,
       "envPowerSupplyInputState": envPowerSupplyInputState,
       "envPowerSupplyOutputState": envPowerSupplyOutputState,
       "envPowerSupplySerialNumber": envPowerSupplySerialNumber,
       "envPowerSupplyVersion": envPowerSupplyVersion,
       "envPowerSupplyCurrentState": envPowerSupplyCurrentState,
       "envPowerSupply5VoltState": envPowerSupply5VoltState,
       "fansGroup": fansGroup,
       "envNumberOfFanBanks": envNumberOfFanBanks,
       "envFanBanksTable": envFanBanksTable,
       "envFanBanksEntry": envFanBanksEntry,
       "envFanBankIndex": envFanBankIndex,
       "envFanBankState": envFanBankState,
       "envFanBankSerialNumber": envFanBankSerialNumber,
       "envFanBankType": envFanBankType,
       "envFanBankRevision": envFanBankRevision,
       "tempGroup": tempGroup,
       "envNumberOfTempSensors": envNumberOfTempSensors,
       "envTempSensorsTable": envTempSensorsTable,
       "envTempSensorsEntry": envTempSensorsEntry,
       "envTempSensorIndex": envTempSensorIndex,
       "envTempSensorState": envTempSensorState,
       "cpuGroup": cpuGroup,
       "envMaxNumberOfCPUs": envMaxNumberOfCPUs,
       "envNumberOfCPUs": envNumberOfCPUs,
       "envCPUsTable": envCPUsTable,
       "envCPUsEntry": envCPUsEntry,
       "envCpuBoard": envCpuBoard,
       "envCpuSlot": envCpuSlot,
       "envCpuType": envCpuType,
       "envCPUState": envCPUState,
       "envCpuDRAMSize": envCpuDRAMSize,
       "envCpuRevLevel": envCpuRevLevel,
       "envCpuFlashSize": envCpuFlashSize,
       "envCpuBoardRevision": envCpuBoardRevision,
       "envCpuPromRevision": envCpuPromRevision,
       "envCpuMACAddress": envCpuMACAddress,
       "envCpuSerialNumber": envCpuSerialNumber,
       "envCpuProductPartNumber": envCpuProductPartNumber,
       "envCpuCLEI": envCpuCLEI,
       "envCpuIDESize": envCpuIDESize,
       "mgmtGroup": mgmtGroup,
       "envMgmtBoardType": envMgmtBoardType,
       "envMgmtBoardRevision": envMgmtBoardRevision,
       "envMgmtBoardSerialNumber": envMgmtBoardSerialNumber,
       "fabricGroup": fabricGroup,
       "envFabricAlarmTripTemperature": envFabricAlarmTripTemperature,
       "envFabricAlarmResetTemperature": envFabricAlarmResetTemperature,
       "envFabricTable": envFabricTable,
       "envFabricEntry": envFabricEntry,
       "envFabricIndex": envFabricIndex,
       "envFabricTemperature": envFabricTemperature,
       "envFabricTemperatureState": envFabricTemperatureState,
       "shmem": shmem,
       "netmodShmemGroup": netmodShmemGroup,
       "shmemConfTable": shmemConfTable,
       "shmemConfEntry": shmemConfEntry,
       "shmemConfIndex": shmemConfIndex,
       "shmemUcastConnections": shmemUcastConnections,
       "shmemMcastConnections": shmemMcastConnections,
       "shmemVpiVciLists": shmemVpiVciLists,
       "shmemCellsBuffers": shmemCellsBuffers,
       "shmemConfName": shmemConfName,
       "shmemMemorySize": shmemMemorySize,
       "netmodShmemTable": netmodShmemTable,
       "netmodShmemEntry": netmodShmemEntry,
       "nshmemBoard": nshmemBoard,
       "nshmemModule": nshmemModule,
       "nshmemConfRow": nshmemConfRow,
       "nshmemConfSharedMemory": nshmemConfSharedMemory,
       "nshmemCurrentUcastConnections": nshmemCurrentUcastConnections,
       "nshmemCurrentMcastConnections": nshmemCurrentMcastConnections,
       "nshmemCurrentVpiVciLists": nshmemCurrentVpiVciLists,
       "nshmemCurrentCellsBuffers": nshmemCurrentCellsBuffers,
       "nshmemCurrentSharedMemory": nshmemCurrentSharedMemory,
       "nshmemConfAal5PacketDrop": nshmemConfAal5PacketDrop,
       "nshmemAssertXACPT": nshmemAssertXACPT,
       "nshmemMemorySize": nshmemMemorySize,
       "portShmemGroup": portShmemGroup,
       "portShmemConfTable": portShmemConfTable,
       "portShmemConfEntry": portShmemConfEntry,
       "pshmemConfBoard": pshmemConfBoard,
       "pshmemConfModule": pshmemConfModule,
       "pshmemConfPort": pshmemConfPort,
       "pshmemMaxCDVforCBR": pshmemMaxCDVforCBR,
       "pshmemMaxCDVforVBR": pshmemMaxCDVforVBR,
       "pshmemQsizeforABR": pshmemQsizeforABR,
       "pshmemEfciOnABR": pshmemEfciOnABR,
       "pshmemEfciOffABR": pshmemEfciOffABR,
       "pshmemQsizeforCBR": pshmemQsizeforCBR,
       "pshmemQsizeforVBR": pshmemQsizeforVBR,
       "pshmemClpThreshforCBR": pshmemClpThreshforCBR,
       "pshmemClpThreshforVBR": pshmemClpThreshforVBR,
       "pshmemClpThreshforABR": pshmemClpThreshforABR,
       "pShmemAtmInterfaceIndex": pShmemAtmInterfaceIndex,
       "portShmemTable": portShmemTable,
       "portShmemEntry": portShmemEntry,
       "pshmemBoard": pshmemBoard,
       "pshmemModule": pshmemModule,
       "pshmemPort": pshmemPort,
       "pshmemPriority": pshmemPriority,
       "pshmemClpThreshold": pshmemClpThreshold,
       "pshmemDedicatedQsize": pshmemDedicatedQsize,
       "pshmemCurrentQsize": pshmemCurrentQsize,
       "pshmemTxCells": pshmemTxCells,
       "pshmemLostCells": pshmemLostCells,
       "netmodShmem2Group": netmodShmem2Group,
       "shmem2ConfTable": shmem2ConfTable,
       "shmem2ConfEntry": shmem2ConfEntry,
       "shmem2ConfIndex": shmem2ConfIndex,
       "shmem2UcastConnections": shmem2UcastConnections,
       "shmem2McastConnections": shmem2McastConnections,
       "shmem2CellsBuffers": shmem2CellsBuffers,
       "shmem2ConfName": shmem2ConfName,
       "shmem2Counters": shmem2Counters,
       "shmem2CellMemorySize": shmem2CellMemorySize,
       "shmem2TableMemorySize": shmem2TableMemorySize,
       "shmem2NumPriorities": shmem2NumPriorities,
       "netmodShmem2Table": netmodShmem2Table,
       "netmodShmem2Entry": netmodShmem2Entry,
       "nShmem2Board": nShmem2Board,
       "nShmem2Module": nShmem2Module,
       "nShmem2ConfRow": nShmem2ConfRow,
       "nShmem2ConfSharedMemory": nShmem2ConfSharedMemory,
       "nShmem2CurrentUcastConnections": nShmem2CurrentUcastConnections,
       "nShmem2CurrentMcastConnections": nShmem2CurrentMcastConnections,
       "nShmem2CurrentCellsBuffers": nShmem2CurrentCellsBuffers,
       "nShmem2CurrentSharedMemory": nShmem2CurrentSharedMemory,
       "nShmem2ConfAal5PacketDrop": nShmem2ConfAal5PacketDrop,
       "nShmem2ConfAal5PacketDropforUBR": nShmem2ConfAal5PacketDropforUBR,
       "nShmem2ConfEfciOn": nShmem2ConfEfciOn,
       "nShmem2ConfEfciOff": nShmem2ConfEfciOff,
       "nShmem2CellMemorySize": nShmem2CellMemorySize,
       "nShmem2TableMemorySize": nShmem2TableMemorySize,
       "nShmem2NumPriorities": nShmem2NumPriorities,
       "nShmem2VBRPriority": nShmem2VBRPriority,
       "netmodShmem2CustomBCSTable": netmodShmem2CustomBCSTable,
       "netmodShmem2CustomBCSEntry": netmodShmem2CustomBCSEntry,
       "nShmem2CustomBCSBoard": nShmem2CustomBCSBoard,
       "nShmem2CustomBCSModule": nShmem2CustomBCSModule,
       "nShmem2CustomBCSValue": nShmem2CustomBCSValue,
       "nShmem2CustomBCSWeight": nShmem2CustomBCSWeight,
       "nShmem2CustomBCSRowStatus": nShmem2CustomBCSRowStatus,
       "portShmem2Group": portShmem2Group,
       "portShmem2ConfTable": portShmem2ConfTable,
       "portShmem2ConfEntry": portShmem2ConfEntry,
       "pShmem2ConfBoard": pShmem2ConfBoard,
       "pShmem2ConfModule": pShmem2ConfModule,
       "pShmem2ConfPort": pShmem2ConfPort,
       "pShmem2QsizeforCBR": pShmem2QsizeforCBR,
       "pShmem2QsizeforVBR": pShmem2QsizeforVBR,
       "pShmem2QsizeforABR": pShmem2QsizeforABR,
       "pShmem2QsizeforUBR": pShmem2QsizeforUBR,
       "pShmem2ClpThreshforCBR": pShmem2ClpThreshforCBR,
       "pShmem2ClpThreshforVBR": pShmem2ClpThreshforVBR,
       "pShmem2ClpThreshforABR": pShmem2ClpThreshforABR,
       "pShmem2ClpThreshforUBR": pShmem2ClpThreshforUBR,
       "pShmem2AtmInterfaceIndex": pShmem2AtmInterfaceIndex,
       "portShmem2Table": portShmem2Table,
       "portShmem2Entry": portShmem2Entry,
       "pShmem2Board": pShmem2Board,
       "pShmem2Module": pShmem2Module,
       "pShmem2Port": pShmem2Port,
       "pShmem2Priority": pShmem2Priority,
       "pShmem2ClpThreshold": pShmem2ClpThreshold,
       "pShmem2DedicatedQsize": pShmem2DedicatedQsize,
       "pShmem2CurrentQsize": pShmem2CurrentQsize,
       "pShmem2TxCells": pShmem2TxCells,
       "pShmem2LostCells": pShmem2LostCells,
       "pShmem2IntentionalLostCells": pShmem2IntentionalLostCells,
       "pShmem2UnintentionalLostCells": pShmem2UnintentionalLostCells,
       "portPriorityShmem2ConfTable": portPriorityShmem2ConfTable,
       "portPriorityShmem2ConfEntry": portPriorityShmem2ConfEntry,
       "ppShmem2ConfBoard": ppShmem2ConfBoard,
       "ppShmem2ConfModule": ppShmem2ConfModule,
       "ppShmem2ConfPort": ppShmem2ConfPort,
       "ppShmem2ConfPriority": ppShmem2ConfPriority,
       "ppShmem2Qsize": ppShmem2Qsize,
       "ppShmem2ClpThreshold": ppShmem2ClpThreshold,
       "connShmem2Group": connShmem2Group,
       "channelShmem2Table": channelShmem2Table,
       "channelShmem2Entry": channelShmem2Entry,
       "vcShmem2OutputPort": vcShmem2OutputPort,
       "vcShmem2OutputVPI": vcShmem2OutputVPI,
       "vcShmem2OutputVCI": vcShmem2OutputVCI,
       "vcShmem2TotalLostCells": vcShmem2TotalLostCells,
       "vcShmem2IntentionalLostCells": vcShmem2IntentionalLostCells,
       "vcShmem2UnintentionalLostCells": vcShmem2UnintentionalLostCells,
       "vcShmem2TransmittedCells": vcShmem2TransmittedCells,
       "pathShmem2Table": pathShmem2Table,
       "pathShmem2Entry": pathShmem2Entry,
       "vpShmem2OutputPort": vpShmem2OutputPort,
       "vpShmem2OutputVPI": vpShmem2OutputVPI,
       "vpShmem2TotalLostCells": vpShmem2TotalLostCells,
       "vpShmem2IntentionalLostCells": vpShmem2IntentionalLostCells,
       "vpShmem2UnintentionalLostCells": vpShmem2UnintentionalLostCells,
       "vpShmem2TransmittedCells": vpShmem2TransmittedCells,
       "netmodShmem3Group": netmodShmem3Group,
       "shmem3ConfTable": shmem3ConfTable,
       "shmem3ConfEntry": shmem3ConfEntry,
       "shmem3ConfIndex": shmem3ConfIndex,
       "shmem3UcastConnections": shmem3UcastConnections,
       "shmem3McastConnections": shmem3McastConnections,
       "shmem3VpiVciLists": shmem3VpiVciLists,
       "shmem3CellsBuffers": shmem3CellsBuffers,
       "shmem3ConfName": shmem3ConfName,
       "shmem3Counters": shmem3Counters,
       "shmem3CellMemorySize": shmem3CellMemorySize,
       "shmem3TableMemorySize": shmem3TableMemorySize,
       "netmodShmem3Table": netmodShmem3Table,
       "netmodShmem3Entry": netmodShmem3Entry,
       "nShmem3Board": nShmem3Board,
       "nShmem3Module": nShmem3Module,
       "nShmem3ConfRow": nShmem3ConfRow,
       "nShmem3ConfSharedMemory": nShmem3ConfSharedMemory,
       "nShmem3CurrentUcastConnections": nShmem3CurrentUcastConnections,
       "nShmem3CurrentMcastConnections": nShmem3CurrentMcastConnections,
       "nShmem3CurrentVpiVciLists": nShmem3CurrentVpiVciLists,
       "nShmem3CurrentCellsBuffers": nShmem3CurrentCellsBuffers,
       "nShmem3ConfAal5PacketDrop": nShmem3ConfAal5PacketDrop,
       "nShmem3ConfAal5PacketDropforUBR": nShmem3ConfAal5PacketDropforUBR,
       "nShmem3ConfEfciOn": nShmem3ConfEfciOn,
       "nShmem3ConfEfciOff": nShmem3ConfEfciOff,
       "nShmem3CellMemorySize": nShmem3CellMemorySize,
       "nShmem3TableMemorySize": nShmem3TableMemorySize,
       "nShmem3ConfCountPackets": nShmem3ConfCountPackets,
       "nShmem3ConfAltCLP1Threshold": nShmem3ConfAltCLP1Threshold,
       "nShmem3ConfAltCLP01Threshold": nShmem3ConfAltCLP01Threshold,
       "nShmem3ConfVcCLP1ForCBR": nShmem3ConfVcCLP1ForCBR,
       "nShmem3ConfVcCLP01ForCBR": nShmem3ConfVcCLP01ForCBR,
       "nShmem3ConfVcCLP1ForVBR": nShmem3ConfVcCLP1ForVBR,
       "nShmem3ConfVcCLP01ForVBR": nShmem3ConfVcCLP01ForVBR,
       "nShmem3ConfVcCLP1ForABR": nShmem3ConfVcCLP1ForABR,
       "nShmem3ConfVcCLP01ForABR": nShmem3ConfVcCLP01ForABR,
       "nShmem3ConfVcCLP1ForUBR": nShmem3ConfVcCLP1ForUBR,
       "nShmem3ConfVcCLP01ForUBR": nShmem3ConfVcCLP01ForUBR,
       "portShmem3Group": portShmem3Group,
       "portShmem3ConfTable": portShmem3ConfTable,
       "portShmem3ConfEntry": portShmem3ConfEntry,
       "pShmem3ConfBoard": pShmem3ConfBoard,
       "pShmem3ConfModule": pShmem3ConfModule,
       "pShmem3ConfPort": pShmem3ConfPort,
       "pShmem3QsizeforCBR": pShmem3QsizeforCBR,
       "pShmem3QsizeforVBR": pShmem3QsizeforVBR,
       "pShmem3QsizeforABR": pShmem3QsizeforABR,
       "pShmem3QsizeforUBR": pShmem3QsizeforUBR,
       "pShmem3Clp01ThreshforCBR": pShmem3Clp01ThreshforCBR,
       "pShmem3Clp1ThreshforCBR": pShmem3Clp1ThreshforCBR,
       "pShmem3Clp01ThreshforVBR": pShmem3Clp01ThreshforVBR,
       "pShmem3Clp1ThreshforVBR": pShmem3Clp1ThreshforVBR,
       "pShmem3Clp01ThreshforABR": pShmem3Clp01ThreshforABR,
       "pShmem3Clp1ThreshforABR": pShmem3Clp1ThreshforABR,
       "pShmem3Clp01ThreshforUBR": pShmem3Clp01ThreshforUBR,
       "pShmem3Clp1ThreshforUBR": pShmem3Clp1ThreshforUBR,
       "pShmem3RateLimit": pShmem3RateLimit,
       "pShmem3ConfSVCSchedulingCBR": pShmem3ConfSVCSchedulingCBR,
       "pShmem3ConfPVCSchedulingCBR": pShmem3ConfPVCSchedulingCBR,
       "pShmem3ConfSVCSchedulingVBR": pShmem3ConfSVCSchedulingVBR,
       "pShmem3ConfPVCSchedulingVBR": pShmem3ConfPVCSchedulingVBR,
       "pShmem3ConfAltCLPConfigCBR": pShmem3ConfAltCLPConfigCBR,
       "pShmem3ConfAltCLPConfigVBR": pShmem3ConfAltCLPConfigVBR,
       "pShmem3ConfAltCLPConfigUBR": pShmem3ConfAltCLPConfigUBR,
       "pShmem3AtmInterfaceIndex": pShmem3AtmInterfaceIndex,
       "portShmem3Table": portShmem3Table,
       "portShmem3Entry": portShmem3Entry,
       "pShmem3Board": pShmem3Board,
       "pShmem3Module": pShmem3Module,
       "pShmem3Port": pShmem3Port,
       "pShmem3Priority": pShmem3Priority,
       "pShmem3CurrentQsize": pShmem3CurrentQsize,
       "pShmem3TxCells": pShmem3TxCells,
       "pShmem3EPDLostCells": pShmem3EPDLostCells,
       "pShmem3CLP01LostCells": pShmem3CLP01LostCells,
       "pShmem3CLP1LostCells": pShmem3CLP1LostCells,
       "pShmem3VcCLPLostCells": pShmem3VcCLPLostCells,
       "pShmem3OverflowLostCells": pShmem3OverflowLostCells,
       "pShmem3PPDLostCells": pShmem3PPDLostCells,
       "connShmem3Group": connShmem3Group,
       "channelShmem3Table": channelShmem3Table,
       "channelShmem3Entry": channelShmem3Entry,
       "vcShmem3OutputPort": vcShmem3OutputPort,
       "vcShmem3OutputVPI": vcShmem3OutputVPI,
       "vcShmem3OutputVCI": vcShmem3OutputVCI,
       "vcShmem3IntentionalLostCells": vcShmem3IntentionalLostCells,
       "vcShmem3UnintentionalLostCells": vcShmem3UnintentionalLostCells,
       "vcShmem3CLP0TxCells": vcShmem3CLP0TxCells,
       "vcShmem3CLP1TxCells": vcShmem3CLP1TxCells,
       "vcShmem3EPDLostCells": vcShmem3EPDLostCells,
       "vcShmem3CLP1LostCells": vcShmem3CLP1LostCells,
       "vcShmem3CLP01LostCells": vcShmem3CLP01LostCells,
       "vcShmem3TransmittedPackets": vcShmem3TransmittedPackets,
       "vcShmem3CurrentQsize": vcShmem3CurrentQsize,
       "pathShmem3Table": pathShmem3Table,
       "pathShmem3Entry": pathShmem3Entry,
       "vpShmem3OutputPort": vpShmem3OutputPort,
       "vpShmem3OutputVPI": vpShmem3OutputVPI,
       "vpShmem3UnintentionalLostCells": vpShmem3UnintentionalLostCells,
       "vpShmem3CLP0TxCells": vpShmem3CLP0TxCells,
       "vpShmem3CLP1TxCells": vpShmem3CLP1TxCells,
       "vpShmem3CLP1LostCells": vpShmem3CLP1LostCells,
       "vpShmem3CLP01LostCells": vpShmem3CLP01LostCells,
       "vpShmem3TransmittedPackets": vpShmem3TransmittedPackets,
       "vpShmem3CurrentQsize": vpShmem3CurrentQsize,
       "netmodGenericShmemGroup": netmodGenericShmemGroup,
       "netmodGenericShmemTable": netmodGenericShmemTable,
       "netmodGenericShmemEntry": netmodGenericShmemEntry,
       "nGenericShmemBoard": nGenericShmemBoard,
       "nGenericShmemModule": nGenericShmemModule,
       "nGenericShmemSubindex": nGenericShmemSubindex,
       "nGenericShmemCurrentUcastConnections": nGenericShmemCurrentUcastConnections,
       "nGenericShmemCurrentMcastConnections": nGenericShmemCurrentMcastConnections,
       "nGenericShmemCurrentConnections": nGenericShmemCurrentConnections,
       "nGenericShmemMaxUcastConnections": nGenericShmemMaxUcastConnections,
       "nGenericShmemMaxMcastConnections": nGenericShmemMaxMcastConnections,
       "nGenericShmemMaxConnections": nGenericShmemMaxConnections,
       "genericPortGroupConfTable": genericPortGroupConfTable,
       "genericPortGroupConfEntry": genericPortGroupConfEntry,
       "genericPortGroupBoard": genericPortGroupBoard,
       "genericPortGroupIndex": genericPortGroupIndex,
       "genericPortGroupSubindex": genericPortGroupSubindex,
       "genericPortGroupPrioIndex": genericPortGroupPrioIndex,
       "genericPortGroupAal5PacketDrop": genericPortGroupAal5PacketDrop,
       "genericPortGroupEfciOn": genericPortGroupEfciOn,
       "genericPortGroupEfciOff": genericPortGroupEfciOff,
       "genericPortGroupPrioName": genericPortGroupPrioName,
       "netmodGenericShmemCustomBCSTable": netmodGenericShmemCustomBCSTable,
       "netmodGenericShmemCustomBCSEntry": netmodGenericShmemCustomBCSEntry,
       "nGenericShmemCustomBCSBoard": nGenericShmemCustomBCSBoard,
       "nGenericShmemCustomBCSModule": nGenericShmemCustomBCSModule,
       "nGenericShmemCustomBCSSubindex": nGenericShmemCustomBCSSubindex,
       "nGenericShmemCustomBCSValue": nGenericShmemCustomBCSValue,
       "nGenericShmemCustomBCSWeight": nGenericShmemCustomBCSWeight,
       "nGenericShmemCustomBCSRowStatus": nGenericShmemCustomBCSRowStatus,
       "genericOutputPortGroup": genericOutputPortGroup,
       "genericOutputPortConfTable": genericOutputPortConfTable,
       "genericOutputPortConfEntry": genericOutputPortConfEntry,
       "genericOutputPortConfBoard": genericOutputPortConfBoard,
       "genericOutputPortConfModule": genericOutputPortConfModule,
       "genericOutputPortConfPort": genericOutputPortConfPort,
       "genericOutputPortConfPrio": genericOutputPortConfPrio,
       "genericOutputPortConfPrioDedicatedQSize": genericOutputPortConfPrioDedicatedQSize,
       "genericOutputPortConfPrioClp1Threshold": genericOutputPortConfPrioClp1Threshold,
       "genericOutputPortConfPrioClp01Threshold": genericOutputPortConfPrioClp01Threshold,
       "genericOutputPortConfPrioName": genericOutputPortConfPrioName,
       "genericOutputPortConfAtmif": genericOutputPortConfAtmif,
       "genericOutputPortStatsTable": genericOutputPortStatsTable,
       "genericOutputPortStatsEntry": genericOutputPortStatsEntry,
       "genericOutputPortStatsBoard": genericOutputPortStatsBoard,
       "genericOutputPortStatsModule": genericOutputPortStatsModule,
       "genericOutputPortStatsPort": genericOutputPortStatsPort,
       "genericOutputPortStatsPrio": genericOutputPortStatsPrio,
       "genericOutputPortStatsPrioTransmittedCells": genericOutputPortStatsPrioTransmittedCells,
       "genericOutputPortStatsPrioClp1LostCells": genericOutputPortStatsPrioClp1LostCells,
       "genericOutputPortStatsPrioClp01LostCells": genericOutputPortStatsPrioClp01LostCells,
       "genericOutputPortStatsPrioName": genericOutputPortStatsPrioName,
       "genericOutputPortStatsAtmif": genericOutputPortStatsAtmif,
       "genericOutputPortStatsPrioEpdPpdLostCells": genericOutputPortStatsPrioEpdPpdLostCells,
       "dualScp": dualScp,
       "dualScpGroup": dualScpGroup,
       "dualScpConfTable": dualScpConfTable,
       "dualScpConfEntry": dualScpConfEntry,
       "dualScpSlot": dualScpSlot,
       "dualScpState": dualScpState,
       "dualScpSyncState": dualScpSyncState,
       "dualScpPrimary": dualScpPrimary,
       "dualScpFailover": dualScpFailover,
       "dualScpManualSyncRequest": dualScpManualSyncRequest,
       "dualScpCdbSyncMode": dualScpCdbSyncMode,
       "dualScpManualSwitchOver": dualScpManualSwitchOver,
       "dualScpSwitchOverTime": dualScpSwitchOverTime,
       "dualScpSwitchOverThreshold": dualScpSwitchOverThreshold,
       "dualScpSyncRequestList": dualScpSyncRequestList,
       "dualScpNumSyncRequests": dualScpNumSyncRequests,
       "dualScpNumSyncFailures": dualScpNumSyncFailures,
       "dualScpResetStandbyScp": dualScpResetStandbyScp,
       "dualScpAutoRemoveOldFiles": dualScpAutoRemoveOldFiles,
       "dualScpRedundancyState": dualScpRedundancyState,
       "dualScpSVXCPStateSyncPercent": dualScpSVXCPStateSyncPercent,
       "dualScpSVXCPStateTransferFailed": dualScpSVXCPStateTransferFailed,
       "dualScpSVXCPdroppedCallCount": dualScpSVXCPdroppedCallCount,
       "etherChipSet": etherChipSet,
       "etherChipSetDec": etherChipSetDec,
       "etherChipSetDec21440": etherChipSetDec21440,
       "switchGroup": switchGroup,
       "hardwareVersion": hardwareVersion,
       "softwareVersion": softwareVersion,
       "maxPaths": maxPaths,
       "maxChannels": maxChannels,
       "atmAddress": atmAddress,
       "uptime": uptime,
       "switchCDV": switchCDV,
       "switchPolicingAction": switchPolicingAction,
       "softwareVersionText": softwareVersionText,
       "switchType": switchType,
       "switchReservedPMPMinVCI": switchReservedPMPMinVCI,
       "switchReservedPMPMaxVCI": switchReservedPMPMaxVCI,
       "switchTimeZone": switchTimeZone,
       "switchGMTime": switchGMTime,
       "switchProtocolType": switchProtocolType,
       "switchCurrentUserid": switchCurrentUserid,
       "switchCurrentLoginFrom": switchCurrentLoginFrom,
       "switchPrimaryClock": switchPrimaryClock,
       "switchSecondaryClock": switchSecondaryClock,
       "switchClockOperStatus": switchClockOperStatus,
       "switchTimingMode": switchTimingMode,
       "switchConnectionPreservation": switchConnectionPreservation,
       "switchATMLayerOAM": switchATMLayerOAM,
       "switchHttpServer": switchHttpServer,
       "switchHttpHelpUrl": switchHttpHelpUrl,
       "mcastGroup": mcastGroup,
       "mcastSpaceTable": mcastSpaceTable,
       "mcastSpaceEntry": mcastSpaceEntry,
       "mcastSpaceIndex": mcastSpaceIndex,
       "mcastSpaceNumConn": mcastSpaceNumConn,
       "mcastSpaceName": mcastSpaceName,
       "switchCtrlLinkid": switchCtrlLinkid,
       "switchClockCurrentStatus": switchClockCurrentStatus,
       "switchDebounceTable": switchDebounceTable,
       "switchDebounceEntry": switchDebounceEntry,
       "switchDebounceIndex": switchDebounceIndex,
       "switchDebounceName": switchDebounceName,
       "switchDebounceHysteresis": switchDebounceHysteresis,
       "softwareLicenseKey": softwareLicenseKey,
       "switchCounterResetTime": switchCounterResetTime,
       "switchCounterReset": switchCounterReset,
       "switchSbprServerAddressTable": switchSbprServerAddressTable,
       "switchSbprServerAddressEntry": switchSbprServerAddressEntry,
       "sbprServerAddressIndex": sbprServerAddressIndex,
       "sbprServerAddressIndexName": sbprServerAddressIndexName,
       "sbprServerMaxHops": sbprServerMaxHops,
       "sbprServerMinSeconds": sbprServerMinSeconds,
       "sbprServerAddress1": sbprServerAddress1,
       "sbprServerAddress2": sbprServerAddress2,
       "sbprServerAddress3": sbprServerAddress3,
       "sbprServerAddress4": sbprServerAddress4,
       "sbprServerAddress5": sbprServerAddress5,
       "sbprServerRowStatus": sbprServerRowStatus,
       "switchPrimaryClockPort": switchPrimaryClockPort,
       "switchSecondaryClockPort": switchSecondaryClockPort,
       "serviceCategoryTable": serviceCategoryTable,
       "serviceCategoryEntry": serviceCategoryEntry,
       "serviceCategoryIndex": serviceCategoryIndex,
       "serviceCategoryName": serviceCategoryName,
       "switchPmpEnable": switchPmpEnable,
       "switchCallPreservation": switchCallPreservation,
       "switchCallPresOperStatus": switchCallPresOperStatus,
       "portGroup": portGroup,
       "numberOfPorts": numberOfPorts,
       "portTable": portTable,
       "portEntry": portEntry,
       "portNumber": portNumber,
       "portAdminStatus": portAdminStatus,
       "portOperStatus": portOperStatus,
       "portTime": portTime,
       "portRemoteAtmAddress": portRemoteAtmAddress,
       "portRemoteIpAddress": portRemoteIpAddress,
       "portMaxPathsIn": portMaxPathsIn,
       "portNumPathsIn": portNumPathsIn,
       "portMaxBandwidthIn": portMaxBandwidthIn,
       "portAllocBandwidthIn": portAllocBandwidthIn,
       "portUsedBandwidthIn": portUsedBandwidthIn,
       "portReceivedCells": portReceivedCells,
       "portMaxPathsOut": portMaxPathsOut,
       "portNumPathsOut": portNumPathsOut,
       "portMaxBandwidthOut": portMaxBandwidthOut,
       "portAllocBandwidthOut": portAllocBandwidthOut,
       "portUsedBandwidthOut": portUsedBandwidthOut,
       "portTransmittedCells": portTransmittedCells,
       "portHwBoard": portHwBoard,
       "portHwModule": portHwModule,
       "portHwNumber": portHwNumber,
       "portILMIRemoteIpAddress": portILMIRemoteIpAddress,
       "portCDVT": portCDVT,
       "portInputPolicingStatus": portInputPolicingStatus,
       "portVbrOverbooking": portVbrOverbooking,
       "portVbrBufferOverb": portVbrBufferOverb,
       "portManagementStatus": portManagementStatus,
       "portAISRDIGeneration": portAISRDIGeneration,
       "portGCRAPolicingCBR": portGCRAPolicingCBR,
       "portGCRAPolicingVBR": portGCRAPolicingVBR,
       "portAAL5PacketDiscardCBR": portAAL5PacketDiscardCBR,
       "portAAL5PacketDiscardVBR": portAAL5PacketDiscardVBR,
       "portAAL5PacketDiscardUBR": portAAL5PacketDiscardUBR,
       "portInputCACErrors": portInputCACErrors,
       "portInputVPIErrors": portInputVPIErrors,
       "portInputVCIErrors": portInputVCIErrors,
       "portInputSetupErrors": portInputSetupErrors,
       "portOutputCACErrors": portOutputCACErrors,
       "portOutputVPIErrors": portOutputVPIErrors,
       "portOutputVCIErrors": portOutputVCIErrors,
       "portOutputSetupErrors": portOutputSetupErrors,
       "portPPPolicingCBR": portPPPolicingCBR,
       "portPPPolicingVBR": portPPPolicingVBR,
       "portUBRTagging": portUBRTagging,
       "portInputCdv": portInputCdv,
       "portInputMaxctd": portInputMaxctd,
       "portInputDelayMode": portInputDelayMode,
       "portOutputCdv": portOutputCdv,
       "portOutputMaxctd": portOutputMaxctd,
       "portOutputDelayMode": portOutputDelayMode,
       "portCACStatus": portCACStatus,
       "portCounterResetTime": portCounterResetTime,
       "portCounterReset": portCounterReset,
       "portName": portName,
       "portGCRAPolicingRTVBR": portGCRAPolicingRTVBR,
       "portGCRAPolicingNRTVBR": portGCRAPolicingNRTVBR,
       "portAAL5PacketDiscardRTVBR": portAAL5PacketDiscardRTVBR,
       "portAAL5PacketDiscardNRTVBR": portAAL5PacketDiscardNRTVBR,
       "portPPPolicingNRTVBR": portPPPolicingNRTVBR,
       "portPPPolicingRTVBR": portPPPolicingRTVBR,
       "portNrtVbrOverbooking": portNrtVbrOverbooking,
       "portNrtVbrBufferOverb": portNrtVbrBufferOverb,
       "portRtVbrOverbooking": portRtVbrOverbooking,
       "portRtVbrBufferOverb": portRtVbrBufferOverb,
       "portPathOverbooking": portPathOverbooking,
       "atmIfConnSchedTable": atmIfConnSchedTable,
       "atmIfConnSchedEntry": atmIfConnSchedEntry,
       "atmIfConnSchedLink": atmIfConnSchedLink,
       "atmIfConnSchedServCat": atmIfConnSchedServCat,
       "atmIfConnSchedMode": atmIfConnSchedMode,
       "atmIfConnSchedOverride": atmIfConnSchedOverride,
       "pathGroup": pathGroup,
       "pathTable": pathTable,
       "pathEntry": pathEntry,
       "pathPort": pathPort,
       "pathVPI": pathVPI,
       "pathStatus": pathStatus,
       "pathNumOutputs": pathNumOutputs,
       "pathMaxChannels": pathMaxChannels,
       "pathNumChannels": pathNumChannels,
       "pathMaxBandwidth": pathMaxBandwidth,
       "pathAllocBandwidth": pathAllocBandwidth,
       "pathUsedBandwidth": pathUsedBandwidth,
       "pathCells": pathCells,
       "pathUptime": pathUptime,
       "pathSigProtocol": pathSigProtocol,
       "pathRejectedCells": pathRejectedCells,
       "pathMinVCI": pathMinVCI,
       "pathMaxVCI": pathMaxVCI,
       "pathCACErrors": pathCACErrors,
       "pathVCIErrors": pathVCIErrors,
       "pathSetupErrors": pathSetupErrors,
       "pathRouteTable": pathRouteTable,
       "pathRouteEntry": pathRouteEntry,
       "pathrInputPort": pathrInputPort,
       "pathrInputVPI": pathrInputVPI,
       "pathrOutputPort": pathrOutputPort,
       "pathrOutputVPI": pathrOutputVPI,
       "pathrStatus": pathrStatus,
       "pathrMaxBandwidth": pathrMaxBandwidth,
       "pathrAllocBandwidth": pathrAllocBandwidth,
       "pathrCells": pathrCells,
       "pathrUptime": pathrUptime,
       "pathrSigProtocol": pathrSigProtocol,
       "pathrRejectedCells": pathrRejectedCells,
       "pathrLoopVPI": pathrLoopVPI,
       "pathrUpcContract": pathrUpcContract,
       "pathrName": pathrName,
       "pathrConnectionType": pathrConnectionType,
       "pathrServCat": pathrServCat,
       "outputPathTable": outputPathTable,
       "outputPathEntry": outputPathEntry,
       "opathPort": opathPort,
       "opathVPI": opathVPI,
       "opathStatus": opathStatus,
       "opathMaxChannels": opathMaxChannels,
       "opathNumChannels": opathNumChannels,
       "opathMaxBandwidth": opathMaxBandwidth,
       "opathAllocBandwidth": opathAllocBandwidth,
       "opathUsedBandwidth": opathUsedBandwidth,
       "opathCells": opathCells,
       "opathUptime": opathUptime,
       "opathSigProtocol": opathSigProtocol,
       "opathRejectedCells": opathRejectedCells,
       "opathTrafficShapeVPI": opathTrafficShapeVPI,
       "opathVbrOverbooking": opathVbrOverbooking,
       "opathVbrBufferOverb": opathVbrBufferOverb,
       "opathMinVCI": opathMinVCI,
       "opathMaxVCI": opathMaxVCI,
       "opathCACErrors": opathCACErrors,
       "opathVCIErrors": opathVCIErrors,
       "opathSetupErrors": opathSetupErrors,
       "opathLoopVPI": opathLoopVPI,
       "opathSchedMode": opathSchedMode,
       "opathNrtVbrOverbooking": opathNrtVbrOverbooking,
       "opathNrtVbrBufferOverb": opathNrtVbrBufferOverb,
       "opathRtVbrOverbooking": opathRtVbrOverbooking,
       "opathRtVbrBufferOverb": opathRtVbrBufferOverb,
       "outputPathStatsTable": outputPathStatsTable,
       "outputPathStatsEntry": outputPathStatsEntry,
       "opathStatsPort": opathStatsPort,
       "opathStatsVPI": opathStatsVPI,
       "opathStatsLostCells": opathStatsLostCells,
       "opathStatsTransmittedCells": opathStatsTransmittedCells,
       "opathStatsIntentionalLostCells": opathStatsIntentionalLostCells,
       "opathStatsCLP0Cells": opathStatsCLP0Cells,
       "opathStatsLostPackets": opathStatsLostPackets,
       "opathStatsTransmittedPackets": opathStatsTransmittedPackets,
       "outputPathChannelSchedTable": outputPathChannelSchedTable,
       "outputPathChannelSchedEntry": outputPathChannelSchedEntry,
       "opathChannelSchedPort": opathChannelSchedPort,
       "opathChannelSchedVPI": opathChannelSchedVPI,
       "opathChannelSchedServCat": opathChannelSchedServCat,
       "opathChannelSchedSchedMode": opathChannelSchedSchedMode,
       "opathChannelSchedSchedOverride": opathChannelSchedSchedOverride,
       "channelGroup": channelGroup,
       "channelTable": channelTable,
       "channelEntry": channelEntry,
       "chanPort": chanPort,
       "chanVPI": chanVPI,
       "chanVCI": chanVCI,
       "chanStatus": chanStatus,
       "chanNumOutputs": chanNumOutputs,
       "chanAllocBandwidth": chanAllocBandwidth,
       "chanUsedBandwidth": chanUsedBandwidth,
       "chanCells": chanCells,
       "chanUptime": chanUptime,
       "chanSigProtocol": chanSigProtocol,
       "chanRejectedCells": chanRejectedCells,
       "chanCDV": chanCDV,
       "chanPolicingAction": chanPolicingAction,
       "chanUpcContract": chanUpcContract,
       "chanServCat": chanServCat,
       "chanQosPoliceScheme": chanQosPoliceScheme,
       "chanQosPCR": chanQosPCR,
       "chanQosSCR": chanQosSCR,
       "chanQosMBS": chanQosMBS,
       "chanQosCDVT": chanQosCDVT,
       "chanQosPoliceState": chanQosPoliceState,
       "chanQosIsAAL5": chanQosIsAAL5,
       "chanQosPerPacketPolicing": chanQosPerPacketPolicing,
       "channelRouteTable": channelRouteTable,
       "channelRouteEntry": channelRouteEntry,
       "chanrInputPort": chanrInputPort,
       "chanrInputVPI": chanrInputVPI,
       "chanrInputVCI": chanrInputVCI,
       "chanrOutputPort": chanrOutputPort,
       "chanrOutputVPI": chanrOutputVPI,
       "chanrOutputVCI": chanrOutputVCI,
       "chanrStatus": chanrStatus,
       "chanrSigProtocol": chanrSigProtocol,
       "chanrName": chanrName,
       "chanrConnectionType": chanrConnectionType,
       "reverseChannelRouteTable": reverseChannelRouteTable,
       "reverseChannelRouteEntry": reverseChannelRouteEntry,
       "revChanrOutputPort": revChanrOutputPort,
       "revChanrOutputVPI": revChanrOutputVPI,
       "revChanrOutputVCI": revChanrOutputVCI,
       "revChanrInputPort": revChanrInputPort,
       "revChanrInputVPI": revChanrInputVPI,
       "revChanrInputVCI": revChanrInputVCI,
       "revChanrSigProtocol": revChanrSigProtocol,
       "outputChannelStatsTable": outputChannelStatsTable,
       "outputChannelStatsEntry": outputChannelStatsEntry,
       "ochanStatsPort": ochanStatsPort,
       "ochanStatsVPI": ochanStatsVPI,
       "ochanStatsVCI": ochanStatsVCI,
       "ochanStatsLostCells": ochanStatsLostCells,
       "ochanStatsTransmittedCells": ochanStatsTransmittedCells,
       "ochanStatsIntentionalLostCells": ochanStatsIntentionalLostCells,
       "ochanStatsCLP0Cells": ochanStatsCLP0Cells,
       "ochanStatsLostPackets": ochanStatsLostPackets,
       "ochanStatsTransmittedPackets": ochanStatsTransmittedPackets,
       "topologyGroup": topologyGroup,
       "numberOfLinks": numberOfLinks,
       "linkTable": linkTable,
       "linkEntry": linkEntry,
       "linkSrc": linkSrc,
       "linkDest": linkDest,
       "linkCapacity": linkCapacity,
       "linkAge": linkAge,
       "signalingGroup": signalingGroup,
       "spansGroup": spansGroup,
       "sigPathTable": sigPathTable,
       "sigPathEntry": sigPathEntry,
       "sigPathPort": sigPathPort,
       "sigPathVPI": sigPathVPI,
       "sigPathVCI": sigPathVCI,
       "sigPathClsVCI": sigPathClsVCI,
       "sigPathAdminStatus": sigPathAdminStatus,
       "sigPathOperStatus": sigPathOperStatus,
       "sigPathEntryStatus": sigPathEntryStatus,
       "sigPathAALType": sigPathAALType,
       "sigPathCDV": sigPathCDV,
       "sigPathPolicingAction": sigPathPolicingAction,
       "sigPathRemoteAtmAddress": sigPathRemoteAtmAddress,
       "sigPathRemoteIpAddress": sigPathRemoteIpAddress,
       "sigPathType": sigPathType,
       "sigPathClsUpcContract": sigPathClsUpcContract,
       "sigPathSigReservedBW": sigPathSigReservedBW,
       "sigPathMinVCI": sigPathMinVCI,
       "sigPathMaxVCI": sigPathMaxVCI,
       "sigPathOpenTimeout": sigPathOpenTimeout,
       "sigPathCloseTimeout": sigPathCloseTimeout,
       "sigPathOutputSigService": sigPathOutputSigService,
       "sigPathAALOperType": sigPathAALOperType,
       "sigPathStatsTable": sigPathStatsTable,
       "sigPathStatsEntry": sigPathStatsEntry,
       "sigPathStatsPort": sigPathStatsPort,
       "sigPathStatsVPI": sigPathStatsVPI,
       "sigPathVCCs": sigPathVCCs,
       "sigPathRestarts": sigPathRestarts,
       "sigPathCallsCompletions": sigPathCallsCompletions,
       "sigPathCallsFailures": sigPathCallsFailures,
       "sigPathCallsRejections": sigPathCallsRejections,
       "sigPathSpansTransmittedMessages": sigPathSpansTransmittedMessages,
       "sigPathSpansReceivedMessages": sigPathSpansReceivedMessages,
       "sigPathClsTransmittedMessages": sigPathClsTransmittedMessages,
       "sigPathClsReceivedMessages": sigPathClsReceivedMessages,
       "spvcSrcNumberOfSPVCs": spvcSrcNumberOfSPVCs,
       "spvcSrcTable": spvcSrcTable,
       "spvcSrcEntry": spvcSrcEntry,
       "spvcSrcSpvcId": spvcSrcSpvcId,
       "spvcSrcSwitchAddr": spvcSrcSwitchAddr,
       "spvcSrcDestSpvcId": spvcSrcDestSpvcId,
       "spvcSrcDestSwitchAddr": spvcSrcDestSwitchAddr,
       "spvcSrcInPort": spvcSrcInPort,
       "spvcSrcInVPI": spvcSrcInVPI,
       "spvcSrcInVCI": spvcSrcInVCI,
       "spvcSrcAllocBandwidth": spvcSrcAllocBandwidth,
       "spvcSrcUpTime": spvcSrcUpTime,
       "spvcSrcStatus": spvcSrcStatus,
       "spvcSrcEntryStatus": spvcSrcEntryStatus,
       "spvcDestNumberOfSPVCs": spvcDestNumberOfSPVCs,
       "spvcDestTable": spvcDestTable,
       "spvcDestEntry": spvcDestEntry,
       "spvcDestSpvcId": spvcDestSpvcId,
       "spvcDestSwitchAddr": spvcDestSwitchAddr,
       "spvcDestSrcSpvcId": spvcDestSrcSpvcId,
       "spvcDestSrcSwitchAddr": spvcDestSrcSwitchAddr,
       "spvcDestOutPort": spvcDestOutPort,
       "spvcDestOutVPI": spvcDestOutVPI,
       "spvcDestOutVCI": spvcDestOutVCI,
       "spvcDestAllocBandwidth": spvcDestAllocBandwidth,
       "spvcDestUpTime": spvcDestUpTime,
       "spvcDestStatus": spvcDestStatus,
       "spvcDestEntryStatus": spvcDestEntryStatus,
       "q2931Group": q2931Group,
       "q2931LayerGroup": q2931LayerGroup,
       "q2931AdminTable": q2931AdminTable,
       "q2931AdminEntry": q2931AdminEntry,
       "q2931AdminPort": q2931AdminPort,
       "q2931AdminVPI": q2931AdminVPI,
       "q2931AdminVCI": q2931AdminVCI,
       "q2931AdminStatus": q2931AdminStatus,
       "q2931OperStatus": q2931OperStatus,
       "q2931SSCOPOperStatus": q2931SSCOPOperStatus,
       "q2931ILMIAdminStatus": q2931ILMIAdminStatus,
       "q2931ILMIOperStatus": q2931ILMIOperStatus,
       "q2931AdminAALType": q2931AdminAALType,
       "q2931AdminUNISide": q2931AdminUNISide,
       "q2931AdminConfigType": q2931AdminConfigType,
       "q2931AdminOperType": q2931AdminOperType,
       "q2931AdminEntryStatus": q2931AdminEntryStatus,
       "q2931AdminRemoteIpAddress": q2931AdminRemoteIpAddress,
       "q2931SigReservedBW": q2931SigReservedBW,
       "q2931ILMIReservedBW": q2931ILMIReservedBW,
       "q2931ILMIAdminVCI": q2931ILMIAdminVCI,
       "q2931AdminMinVCI": q2931AdminMinVCI,
       "q2931AdminMaxVCI": q2931AdminMaxVCI,
       "q2931MinVCI": q2931MinVCI,
       "q2931MaxVCI": q2931MaxVCI,
       "q2931UNIConfigVersion": q2931UNIConfigVersion,
       "q2931UNIOperVersion": q2931UNIOperVersion,
       "q2931ILMIRegistration": q2931ILMIRegistration,
       "q2931CallingPDefaultAddress": q2931CallingPDefaultAddress,
       "q2931AdminUseNativeE164": q2931AdminUseNativeE164,
       "q2931AdminNativeE164Address": q2931AdminNativeE164Address,
       "q2931AdminE164AddressResolution": q2931AdminE164AddressResolution,
       "q2931AdminFtPnniOrigCost": q2931AdminFtPnniOrigCost,
       "q2931AdminFtPnniTermCost": q2931AdminFtPnniTermCost,
       "q2931AdminAVPresentation": q2931AdminAVPresentation,
       "q2931AdminSigMode": q2931AdminSigMode,
       "q2931AdminSigAlloc": q2931AdminSigAlloc,
       "q2931PeerPort": q2931PeerPort,
       "q2931InputSigContract": q2931InputSigContract,
       "q2931OutputSigService": q2931OutputSigService,
       "q2931SSCOPNoRespTimer": q2931SSCOPNoRespTimer,
       "q2931AdminIncomingNSAPFilterIndex": q2931AdminIncomingNSAPFilterIndex,
       "q2931AdminOutgoingNSAPFilterIndex": q2931AdminOutgoingNSAPFilterIndex,
       "q2931AdminIEFilter": q2931AdminIEFilter,
       "q2931SendCallProc": q2931SendCallProc,
       "q2931VCIRangeStatus": q2931VCIRangeStatus,
       "q2931ClearOnCarrierLoss": q2931ClearOnCarrierLoss,
       "q2931QosClassExpansionKey": q2931QosClassExpansionKey,
       "q2931AtmrConfDomainID": q2931AtmrConfDomainID,
       "q2931AtmrPnniNodeIndex": q2931AtmrPnniNodeIndex,
       "q2931AdminOperSigMode": q2931AdminOperSigMode,
       "q2931AdminOperSigAlloc": q2931AdminOperSigAlloc,
       "q2931OutputSigUpc": q2931OutputSigUpc,
       "q2931AdminPlanType": q2931AdminPlanType,
       "q2931AdminMaxVPI": q2931AdminMaxVPI,
       "q2931MaxSvccVPI": q2931MaxSvccVPI,
       "q2931LastChangeTime": q2931LastChangeTime,
       "q2931NNIProto": q2931NNIProto,
       "q2931MaxSvpcVPI": q2931MaxSvpcVPI,
       "q2931VpCapability": q2931VpCapability,
       "q2931VpciGroupIndex": q2931VpciGroupIndex,
       "q2931AcceleratedClear": q2931AcceleratedClear,
       "q2931SupplementaryServicesStatus": q2931SupplementaryServicesStatus,
       "q2931CallingPAddressPresentation": q2931CallingPAddressPresentation,
       "q2931CallingPAddressRestriction": q2931CallingPAddressRestriction,
       "q2931ConnectedPAddressPresentation": q2931ConnectedPAddressPresentation,
       "q2931ConnectedPAddressRestriction": q2931ConnectedPAddressRestriction,
       "q2931ConnectedPDefaultAddress": q2931ConnectedPDefaultAddress,
       "q2931SubaddressingAdminStatus": q2931SubaddressingAdminStatus,
       "q2931UserUserSignallingAdminStatus": q2931UserUserSignallingAdminStatus,
       "q2931OutputIlmiUpc": q2931OutputIlmiUpc,
       "q2931OutputRccUpc": q2931OutputRccUpc,
       "q2931PnniRccVci": q2931PnniRccVci,
       "q2931AdminubrCalls": q2931AdminubrCalls,
       "q2931AdmincbrCalls": q2931AdmincbrCalls,
       "q2931AdminabrCalls": q2931AdminabrCalls,
       "q2931AdminrtvbrCalls": q2931AdminrtvbrCalls,
       "q2931AdminnrtvbrCalls": q2931AdminnrtvbrCalls,
       "q2931ProxyDirGroupIndex": q2931ProxyDirGroupIndex,
       "q2931StatsTable": q2931StatsTable,
       "q2931StatsEntry": q2931StatsEntry,
       "q2931StatsPort": q2931StatsPort,
       "q2931StatsVPI": q2931StatsVPI,
       "q2931VCCs": q2931VCCs,
       "q2931Restarts": q2931Restarts,
       "q2931CallsCompletions": q2931CallsCompletions,
       "q2931CallsFailures": q2931CallsFailures,
       "q2931CallsRejections": q2931CallsRejections,
       "q2931TransmittedMessages": q2931TransmittedMessages,
       "q2931ReceivedMessages": q2931ReceivedMessages,
       "q2931AddressFilterGroup": q2931AddressFilterGroup,
       "q2931AFTemplateTable": q2931AFTemplateTable,
       "q2931AFTemplateEntry": q2931AFTemplateEntry,
       "q2931AFTemplateIndex": q2931AFTemplateIndex,
       "q2931AFTemplateSrcPort": q2931AFTemplateSrcPort,
       "q2931AFTemplateSrcVPI": q2931AFTemplateSrcVPI,
       "q2931AFTemplateSrcNsap": q2931AFTemplateSrcNsap,
       "q2931AFTemplateSrcNsapMask": q2931AFTemplateSrcNsapMask,
       "q2931AFTemplateDstPort": q2931AFTemplateDstPort,
       "q2931AFTemplateDstVPI": q2931AFTemplateDstVPI,
       "q2931AFTemplateDstNsap": q2931AFTemplateDstNsap,
       "q2931AFTemplateDstNsapMask": q2931AFTemplateDstNsapMask,
       "q2931AFTemplateAction": q2931AFTemplateAction,
       "q2931AFTemplateName": q2931AFTemplateName,
       "q2931AFTemplateStatus": q2931AFTemplateStatus,
       "q2931AFTemplateNextIndex": q2931AFTemplateNextIndex,
       "q2931AFFilterTable": q2931AFFilterTable,
       "q2931AFFilterEntry": q2931AFFilterEntry,
       "q2931AFFilterIndex": q2931AFFilterIndex,
       "q2931AFFilterName": q2931AFFilterName,
       "q2931AFFilterStatus": q2931AFFilterStatus,
       "q2931AFFilterNextIndex": q2931AFFilterNextIndex,
       "q2931AFFilterTListTable": q2931AFFilterTListTable,
       "q2931AFFilterTListEntry": q2931AFFilterTListEntry,
       "q2931AFFilterTListIndex": q2931AFFilterTListIndex,
       "q2931AFFilterTListTemplateIndex": q2931AFFilterTListTemplateIndex,
       "q2931AFFilterTListStatus": q2931AFFilterTListStatus,
       "q2931AFStatsTable": q2931AFStatsTable,
       "q2931AFStatsEntry": q2931AFStatsEntry,
       "q2931AFDirection": q2931AFDirection,
       "q2931AFAccepts": q2931AFAccepts,
       "q2931AFRejectKnowns": q2931AFRejectKnowns,
       "q2931AFRejectUnknowns": q2931AFRejectUnknowns,
       "q2931AFLookupTable": q2931AFLookupTable,
       "q2931AFLookupEntry": q2931AFLookupEntry,
       "q2931AFLookupIndex": q2931AFLookupIndex,
       "q2931AFLookupNSAPFilterIndex": q2931AFLookupNSAPFilterIndex,
       "q2931AFLookupSrcPort": q2931AFLookupSrcPort,
       "q2931AFLookupSrcVPI": q2931AFLookupSrcVPI,
       "q2931AFLookupSrcNsap": q2931AFLookupSrcNsap,
       "q2931AFLookupDstPort": q2931AFLookupDstPort,
       "q2931AFLookupDstVPI": q2931AFLookupDstVPI,
       "q2931AFLookupDstNsap": q2931AFLookupDstNsap,
       "q2931AFLookupResult": q2931AFLookupResult,
       "q2931AFLookupTemplate": q2931AFLookupTemplate,
       "q2931AFLookupStatus": q2931AFLookupStatus,
       "q2931AFLastFailureGroup": q2931AFLastFailureGroup,
       "q2931AFLastFailureSrcPort": q2931AFLastFailureSrcPort,
       "q2931AFLastFailureSrcVPI": q2931AFLastFailureSrcVPI,
       "q2931AFLastFailureSrcNsap": q2931AFLastFailureSrcNsap,
       "q2931AFLastFailureDstPort": q2931AFLastFailureDstPort,
       "q2931AFLastFailureDstVPI": q2931AFLastFailureDstVPI,
       "q2931AFLastFailureDstNsap": q2931AFLastFailureDstNsap,
       "q2931AFLastFailureTemplateIndex": q2931AFLastFailureTemplateIndex,
       "q2931AFLastFailureDirection": q2931AFLastFailureDirection,
       "q2931NSAPPingGroup": q2931NSAPPingGroup,
       "q2931NPCallTable": q2931NPCallTable,
       "q2931NPCallEntry": q2931NPCallEntry,
       "q2931NPCallIndex": q2931NPCallIndex,
       "q2931NPCallDstNsap": q2931NPCallDstNsap,
       "q2931NPCallState": q2931NPCallState,
       "q2931NPCallClientType": q2931NPCallClientType,
       "q2931NPCallFwdUpcKey": q2931NPCallFwdUpcKey,
       "q2931NPCallBckUpcKey": q2931NPCallBckUpcKey,
       "q2931NPCallCallingDomain": q2931NPCallCallingDomain,
       "q2931NPCallQosIndex": q2931NPCallQosIndex,
       "q2931NPCallQosClassFwd": q2931NPCallQosClassFwd,
       "q2931NPCallQosClassBwd": q2931NPCallQosClassBwd,
       "q2931NPCallBearerClass": q2931NPCallBearerClass,
       "q2931NPCallVerbose": q2931NPCallVerbose,
       "q2931NPCallStatus": q2931NPCallStatus,
       "q2931NPPingState": q2931NPPingState,
       "q2931NPCallCauseCode": q2931NPCallCauseCode,
       "q2931NPPingPktCount": q2931NPPingPktCount,
       "q2931NPPingStatsPktsSent": q2931NPPingStatsPktsSent,
       "q2931NPPingStatsPktsReceived": q2931NPPingStatsPktsReceived,
       "q2931NPPingStatsAverageDelay": q2931NPPingStatsAverageDelay,
       "q2931NPMeasureRoundTripDelay": q2931NPMeasureRoundTripDelay,
       "q2931NPPingStatsMaximumDelay": q2931NPPingStatsMaximumDelay,
       "q2931NPPingStatsMinimumDelay": q2931NPPingStatsMinimumDelay,
       "q2931NPCallNextIndex": q2931NPCallNextIndex,
       "perCallDbgFilterGroup": perCallDbgFilterGroup,
       "perCallDbgFilterTable": perCallDbgFilterTable,
       "perCallDbgFilterEntry": perCallDbgFilterEntry,
       "perCallDbgFilterIndex": perCallDbgFilterIndex,
       "perCallDbgFilterTemplateId": perCallDbgFilterTemplateId,
       "perCallDbgFilterName": perCallDbgFilterName,
       "perCallDbgFilterFlavor": perCallDbgFilterFlavor,
       "perCallDbgFilterMatches": perCallDbgFilterMatches,
       "perCallDbgFilterRowStatus": perCallDbgFilterRowStatus,
       "perCallDbgTransFlag": perCallDbgTransFlag,
       "pnniSpvcSrcNumberOfSPVCs": pnniSpvcSrcNumberOfSPVCs,
       "pnniSpvcSrcTable": pnniSpvcSrcTable,
       "pnniSpvcSrcEntry": pnniSpvcSrcEntry,
       "pnniSpvcSrcIndex": pnniSpvcSrcIndex,
       "pnniSpvcSrcCallingPort": pnniSpvcSrcCallingPort,
       "pnniSpvcSrcCallingVPI": pnniSpvcSrcCallingVPI,
       "pnniSpvcSrcCallingVCI": pnniSpvcSrcCallingVCI,
       "pnniSpvcSrcCalledAtmAddr": pnniSpvcSrcCalledAtmAddr,
       "pnniSpvcSrcCalledPort": pnniSpvcSrcCalledPort,
       "pnniSpvcSrcCalledVPVCSel": pnniSpvcSrcCalledVPVCSel,
       "pnniSpvcSrcCalledVPI": pnniSpvcSrcCalledVPI,
       "pnniSpvcSrcCalledVCI": pnniSpvcSrcCalledVCI,
       "pnniSpvcSrcCalledAssignedVPI": pnniSpvcSrcCalledAssignedVPI,
       "pnniSpvcSrcCalledAssignedVCI": pnniSpvcSrcCalledAssignedVCI,
       "pnniSpvcSrcFwdUpcKey": pnniSpvcSrcFwdUpcKey,
       "pnniSpvcSrcBckUpcKey": pnniSpvcSrcBckUpcKey,
       "pnniSpvcSrcBearerClass": pnniSpvcSrcBearerClass,
       "pnniSpvcSrcTrafficType": pnniSpvcSrcTrafficType,
       "pnniSpvcSrcTimingReq": pnniSpvcSrcTimingReq,
       "pnniSpvcSrcSusceptClip": pnniSpvcSrcSusceptClip,
       "pnniSpvcSrcFwdQoSClass": pnniSpvcSrcFwdQoSClass,
       "pnniSpvcSrcBckQoSClass": pnniSpvcSrcBckQoSClass,
       "pnniSpvcSrcTransitNetSel": pnniSpvcSrcTransitNetSel,
       "pnniSpvcSrcLastFailCause": pnniSpvcSrcLastFailCause,
       "pnniSpvcSrcRetryCount": pnniSpvcSrcRetryCount,
       "pnniSpvcSrcLastChangeTime": pnniSpvcSrcLastChangeTime,
       "pnniSpvcSrcStatus": pnniSpvcSrcStatus,
       "pnniSpvcSrcName": pnniSpvcSrcName,
       "pnniSpvcSrcEntryStatus": pnniSpvcSrcEntryStatus,
       "pnniSpvcSrcRouteCost": pnniSpvcSrcRouteCost,
       "pnniSpvcSrcDtlIndex": pnniSpvcSrcDtlIndex,
       "pnniSpvcSrcActiveDtlIndex": pnniSpvcSrcActiveDtlIndex,
       "pnniSpvcSrcRerouteStatus": pnniSpvcSrcRerouteStatus,
       "pnniSpvcSrcCallingDomain": pnniSpvcSrcCallingDomain,
       "pnniSpvcSrcQosIndex": pnniSpvcSrcQosIndex,
       "pnniSpvcSrcDtlIndex1": pnniSpvcSrcDtlIndex1,
       "pnniSpvcSrcDtlIndex2": pnniSpvcSrcDtlIndex2,
       "pnniSpvcSrcDtlIndex3": pnniSpvcSrcDtlIndex3,
       "pnniSpvcSrcDtlIndex4": pnniSpvcSrcDtlIndex4,
       "pnniSpvcSrcDtlWeight1": pnniSpvcSrcDtlWeight1,
       "pnniSpvcSrcDtlWeight2": pnniSpvcSrcDtlWeight2,
       "pnniSpvcSrcDtlWeight3": pnniSpvcSrcDtlWeight3,
       "pnniSpvcSrcDtlWeight4": pnniSpvcSrcDtlWeight4,
       "pnniSpvcSrcBackoffStatus": pnniSpvcSrcBackoffStatus,
       "pnniSpvcSrcPriority": pnniSpvcSrcPriority,
       "pnniSpvcSrcLastLocation": pnniSpvcSrcLastLocation,
       "pnniSpvcSrcOldRouteCost": pnniSpvcSrcOldRouteCost,
       "pnniSpvcSrcDownReason": pnniSpvcSrcDownReason,
       "pnniSpvcSrcActiveDtlNodeIndex": pnniSpvcSrcActiveDtlNodeIndex,
       "pnniSpvcSrcDtlTag": pnniSpvcSrcDtlTag,
       "pnniSpvcSrcAutoDtlStatus": pnniSpvcSrcAutoDtlStatus,
       "pnniSpvcSrcRGroupIndex": pnniSpvcSrcRGroupIndex,
       "pnniSpvcSrcSecondaryVPI": pnniSpvcSrcSecondaryVPI,
       "pnniSpvcSrcSecondaryVCI": pnniSpvcSrcSecondaryVCI,
       "pnniSpvcDestNumberOfSPVCs": pnniSpvcDestNumberOfSPVCs,
       "pnniSpvcDestTable": pnniSpvcDestTable,
       "pnniSpvcDestEntry": pnniSpvcDestEntry,
       "pnniSpvcDestIndex": pnniSpvcDestIndex,
       "pnniSpvcDestCallingAtmAddr": pnniSpvcDestCallingAtmAddr,
       "pnniSpvcDestCallingPort": pnniSpvcDestCallingPort,
       "pnniSpvcDestCallingVPI": pnniSpvcDestCallingVPI,
       "pnniSpvcDestCallingVCI": pnniSpvcDestCallingVCI,
       "pnniSpvcDestCalledAtmAddr": pnniSpvcDestCalledAtmAddr,
       "pnniSpvcDestCalledPort": pnniSpvcDestCalledPort,
       "pnniSpvcDestAssignedVPI": pnniSpvcDestAssignedVPI,
       "pnniSpvcDestAssignedVCI": pnniSpvcDestAssignedVCI,
       "pnniSpvcDestBearerClass": pnniSpvcDestBearerClass,
       "pnniSpvcDestTrafficType": pnniSpvcDestTrafficType,
       "pnniSpvcDestTimingReq": pnniSpvcDestTimingReq,
       "pnniSpvcDestSusceptClip": pnniSpvcDestSusceptClip,
       "pnniSpvcDestUpTime": pnniSpvcDestUpTime,
       "pnniSpvcDestFwdQoSClass": pnniSpvcDestFwdQoSClass,
       "pnniSpvcDestBckQoSClass": pnniSpvcDestBckQoSClass,
       "pnniSpvcDestTransitNetSel": pnniSpvcDestTransitNetSel,
       "pnniSpvcDestStatus": pnniSpvcDestStatus,
       "pnniSpvcDestRGroupIndex": pnniSpvcDestRGroupIndex,
       "q2931PublicGroup": q2931PublicGroup,
       "q2931E164AddrResTable": q2931E164AddrResTable,
       "q2931E164AddrResEntry": q2931E164AddrResEntry,
       "q2931E164Port": q2931E164Port,
       "q2931E164VPI": q2931E164VPI,
       "q2931E164Nsap": q2931E164Nsap,
       "q2931E164NsapMask": q2931E164NsapMask,
       "q2931E164Address": q2931E164Address,
       "q2931E164AddrResStatus": q2931E164AddrResStatus,
       "pnniSpvcParamGroup": pnniSpvcParamGroup,
       "pnniSpvcPaceInterval": pnniSpvcPaceInterval,
       "pnniSpvcPaceNumSpvcs": pnniSpvcPaceNumSpvcs,
       "pnniSpvcRerouteInterval": pnniSpvcRerouteInterval,
       "pnniSpvcRerouteNumSpvcs": pnniSpvcRerouteNumSpvcs,
       "pnniSpvcRerouteThreshold": pnniSpvcRerouteThreshold,
       "pnniSpvcLowestPriority": pnniSpvcLowestPriority,
       "pnniSpvcDefaultUbrBandwidth": pnniSpvcDefaultUbrBandwidth,
       "pnniSpvcTrapMode": pnniSpvcTrapMode,
       "pnniSpvcBackoffInterval": pnniSpvcBackoffInterval,
       "pnniPmpSpvcPartyPaceNum": pnniPmpSpvcPartyPaceNum,
       "pnniSpvpcParamGroup": pnniSpvpcParamGroup,
       "pnniSpvpcPaceInterval": pnniSpvpcPaceInterval,
       "pnniSpvpcPaceNumSpvpcs": pnniSpvpcPaceNumSpvpcs,
       "pnniSpvpcRerouteInterval": pnniSpvpcRerouteInterval,
       "pnniSpvpcRerouteNumSpvpcs": pnniSpvpcRerouteNumSpvpcs,
       "pnniSpvpcRerouteThreshold": pnniSpvpcRerouteThreshold,
       "pnniSpvpcLowestPriority": pnniSpvpcLowestPriority,
       "pnniSpvpcTrapMode": pnniSpvpcTrapMode,
       "pnniSpvpcBackoffInterval": pnniSpvpcBackoffInterval,
       "pnniSpvpcSrcTable": pnniSpvpcSrcTable,
       "pnniSpvpcSrcEntry": pnniSpvpcSrcEntry,
       "pnniSpvpcSrcIndex": pnniSpvpcSrcIndex,
       "pnniSpvpcSrcCallingPort": pnniSpvpcSrcCallingPort,
       "pnniSpvpcSrcCallingVPI": pnniSpvpcSrcCallingVPI,
       "pnniSpvpcSrcCalledAtmAddr": pnniSpvpcSrcCalledAtmAddr,
       "pnniSpvpcSrcCalledPort": pnniSpvpcSrcCalledPort,
       "pnniSpvpcSrcCalledVPVCSel": pnniSpvpcSrcCalledVPVCSel,
       "pnniSpvpcSrcCalledVPI": pnniSpvpcSrcCalledVPI,
       "pnniSpvpcSrcCalledAssignedVPI": pnniSpvpcSrcCalledAssignedVPI,
       "pnniSpvpcSrcFwdUpcKey": pnniSpvpcSrcFwdUpcKey,
       "pnniSpvpcSrcBckUpcKey": pnniSpvpcSrcBckUpcKey,
       "pnniSpvpcSrcSusceptClip": pnniSpvpcSrcSusceptClip,
       "pnniSpvpcSrcFwdQoSClass": pnniSpvpcSrcFwdQoSClass,
       "pnniSpvpcSrcBckQoSClass": pnniSpvpcSrcBckQoSClass,
       "pnniSpvpcSrcLastFailCause": pnniSpvpcSrcLastFailCause,
       "pnniSpvpcSrcRetryCount": pnniSpvpcSrcRetryCount,
       "pnniSpvpcSrcLastChangeTime": pnniSpvpcSrcLastChangeTime,
       "pnniSpvpcSrcStatus": pnniSpvpcSrcStatus,
       "pnniSpvpcSrcName": pnniSpvpcSrcName,
       "pnniSpvpcSrcRowStatus": pnniSpvpcSrcRowStatus,
       "pnniSpvpcSrcRouteCost": pnniSpvpcSrcRouteCost,
       "pnniSpvpcSrcRerouteStatus": pnniSpvpcSrcRerouteStatus,
       "pnniSpvpcSrcCallingDomain": pnniSpvpcSrcCallingDomain,
       "pnniSpvpcSrcQosIndex": pnniSpvpcSrcQosIndex,
       "pnniSpvpcSrcPriority": pnniSpvpcSrcPriority,
       "pnniSpvpcSrcLastLocation": pnniSpvpcSrcLastLocation,
       "pnniSpvpcSrcOldRouteCost": pnniSpvpcSrcOldRouteCost,
       "pnniSpvpcSrcDownReason": pnniSpvpcSrcDownReason,
       "pnniSpvpcSrcBackoffStatus": pnniSpvpcSrcBackoffStatus,
       "pnniSpvpcSrcActiveDtlIndex": pnniSpvpcSrcActiveDtlIndex,
       "pnniSpvpcSrcActiveDtlNodeIndex": pnniSpvpcSrcActiveDtlNodeIndex,
       "pnniSpvpcSrcDtlTag": pnniSpvpcSrcDtlTag,
       "pnniSpvpcSrcAutoDtlStatus": pnniSpvpcSrcAutoDtlStatus,
       "pnniSpvpcSrcRGroupIndex": pnniSpvpcSrcRGroupIndex,
       "pnniSpvpcSrcSecondaryVPI": pnniSpvpcSrcSecondaryVPI,
       "pnniSpvpcStatsGroup": pnniSpvpcStatsGroup,
       "pnniSpvpcSrcNumberOfSPVPCs": pnniSpvpcSrcNumberOfSPVPCs,
       "pnniSpvpcDestNumberOfSPVPCs": pnniSpvpcDestNumberOfSPVPCs,
       "pnniSpvpcDestTable": pnniSpvpcDestTable,
       "pnniSpvpcDestEntry": pnniSpvpcDestEntry,
       "pnniSpvpcDestIndex": pnniSpvpcDestIndex,
       "pnniSpvpcDestCallingAtmAddr": pnniSpvpcDestCallingAtmAddr,
       "pnniSpvpcDestCallingPort": pnniSpvpcDestCallingPort,
       "pnniSpvpcDestCallingVPI": pnniSpvpcDestCallingVPI,
       "pnniSpvpcDestCalledAtmAddr": pnniSpvpcDestCalledAtmAddr,
       "pnniSpvpcDestCalledPort": pnniSpvpcDestCalledPort,
       "pnniSpvpcDestAssignedVPI": pnniSpvpcDestAssignedVPI,
       "pnniSpvpcDestSusceptClip": pnniSpvpcDestSusceptClip,
       "pnniSpvpcDestUpTime": pnniSpvpcDestUpTime,
       "pnniSpvpcDestFwdQoSClass": pnniSpvpcDestFwdQoSClass,
       "pnniSpvpcDestBckQoSClass": pnniSpvpcDestBckQoSClass,
       "pnniSpvpcDestStatus": pnniSpvpcDestStatus,
       "pnniSpvpcDestRGroupIndex": pnniSpvpcDestRGroupIndex,
       "pnniPmpSpvccGroup": pnniPmpSpvccGroup,
       "pnniPmpSpvccSrcNextRootIndex": pnniPmpSpvccSrcNextRootIndex,
       "pnniPmpSpvccSrcNumberOfSpvccs": pnniPmpSpvccSrcNumberOfSpvccs,
       "pnniPmpSpvccSrcRootTable": pnniPmpSpvccSrcRootTable,
       "pnniPmpSpvccSrcRootEntry": pnniPmpSpvccSrcRootEntry,
       "pnniPmpSpvccSrcRootIndex": pnniPmpSpvccSrcRootIndex,
       "pnniPmpSpvccSrcRootPort": pnniPmpSpvccSrcRootPort,
       "pnniPmpSpvccSrcRootVPI": pnniPmpSpvccSrcRootVPI,
       "pnniPmpSpvccSrcRootVCI": pnniPmpSpvccSrcRootVCI,
       "pnniPmpSpvccSrcRootFwdUpcKey": pnniPmpSpvccSrcRootFwdUpcKey,
       "pnniPmpSpvccSrcRootBearerClass": pnniPmpSpvccSrcRootBearerClass,
       "pnniPmpSpvccSrcRootSusceptClip": pnniPmpSpvccSrcRootSusceptClip,
       "pnniPmpSpvccSrcRootFwdQoSClass": pnniPmpSpvccSrcRootFwdQoSClass,
       "pnniPmpSpvccSrcRootStatus": pnniPmpSpvccSrcRootStatus,
       "pnniPmpSpvccSrcRootName": pnniPmpSpvccSrcRootName,
       "pnniPmpSpvccSrcRootPriority": pnniPmpSpvccSrcRootPriority,
       "pnniPmpSpvccSrcRootNumberOfParties": pnniPmpSpvccSrcRootNumberOfParties,
       "pnniPmpSpvccSrcRootNextPartyIndex": pnniPmpSpvccSrcRootNextPartyIndex,
       "pnniPmpSpvccSrcRootCallingDomain": pnniPmpSpvccSrcRootCallingDomain,
       "pnniPmpSpvccSrcRootRowStatus": pnniPmpSpvccSrcRootRowStatus,
       "pnniPmpSpvccSrcRootRGroupIndex": pnniPmpSpvccSrcRootRGroupIndex,
       "pnniPmpSpvccSrcRootSecondaryVPI": pnniPmpSpvccSrcRootSecondaryVPI,
       "pnniPmpSpvccSrcRootSecondaryVCI": pnniPmpSpvccSrcRootSecondaryVCI,
       "pnniPmpSpvccSrcPartyTable": pnniPmpSpvccSrcPartyTable,
       "pnniPmpSpvccSrcPartyEntry": pnniPmpSpvccSrcPartyEntry,
       "pnniPmpSpvccSrcPartyIndex": pnniPmpSpvccSrcPartyIndex,
       "pnniPmpSpvccSrcPartyAtmAddr": pnniPmpSpvccSrcPartyAtmAddr,
       "pnniPmpSpvccSrcPartyVPVCSel": pnniPmpSpvccSrcPartyVPVCSel,
       "pnniPmpSpvccSrcPartyVPI": pnniPmpSpvccSrcPartyVPI,
       "pnniPmpSpvccSrcPartyVCI": pnniPmpSpvccSrcPartyVCI,
       "pnniPmpSpvccSrcPartyAssignedVPI": pnniPmpSpvccSrcPartyAssignedVPI,
       "pnniPmpSpvccSrcPartyAssignedVCI": pnniPmpSpvccSrcPartyAssignedVCI,
       "pnniPmpSpvccSrcPartyStatus": pnniPmpSpvccSrcPartyStatus,
       "pnniPmpSpvccSrcPartyName": pnniPmpSpvccSrcPartyName,
       "pnniPmpSpvccSrcPartyLastFailCause": pnniPmpSpvccSrcPartyLastFailCause,
       "pnniPmpSpvccSrcPartyRetryCount": pnniPmpSpvccSrcPartyRetryCount,
       "pnniPmpSpvccSrcPartyLastChangeTime": pnniPmpSpvccSrcPartyLastChangeTime,
       "pnniPmpSpvccSrcPartyFtDtlIndex": pnniPmpSpvccSrcPartyFtDtlIndex,
       "pnniPmpSpvccSrcPartyRerouteStatus": pnniPmpSpvccSrcPartyRerouteStatus,
       "pnniPmpSpvccSrcPartyQosIndex": pnniPmpSpvccSrcPartyQosIndex,
       "pnniPmpSpvccSrcPartyRowStatus": pnniPmpSpvccSrcPartyRowStatus,
       "pnniPmpSpvccSrcPartyLastLocation": pnniPmpSpvccSrcPartyLastLocation,
       "pnniPmpSpvccSrcPartyAutoDtlStatus": pnniPmpSpvccSrcPartyAutoDtlStatus,
       "pnniPmpSpvccSrcPartyDownReason": pnniPmpSpvccSrcPartyDownReason,
       "pnniPmpSpvccSrcPartyRouteCost": pnniPmpSpvccSrcPartyRouteCost,
       "pnniPmpSpvccDestNumberOfSpvccs": pnniPmpSpvccDestNumberOfSpvccs,
       "pnniPmpSpvccDestRootTable": pnniPmpSpvccDestRootTable,
       "pnniPmpSpvccDestRootEntry": pnniPmpSpvccDestRootEntry,
       "pnniPmpSpvccDestRootIndex": pnniPmpSpvccDestRootIndex,
       "pnniPmpSpvccDestRootAtmAddr": pnniPmpSpvccDestRootAtmAddr,
       "pnniPmpSpvccDestRootPort": pnniPmpSpvccDestRootPort,
       "pnniPmpSpvccDestRootVPI": pnniPmpSpvccDestRootVPI,
       "pnniPmpSpvccDestRootVCI": pnniPmpSpvccDestRootVCI,
       "pnniPmpSpvccDestRootBearerClass": pnniPmpSpvccDestRootBearerClass,
       "pnniPmpSpvccDestRootSusceptClip": pnniPmpSpvccDestRootSusceptClip,
       "pnniPmpSpvccDestRootFwdQoSClass": pnniPmpSpvccDestRootFwdQoSClass,
       "pnniPmpSpvccDestRootNumberOfParties": pnniPmpSpvccDestRootNumberOfParties,
       "pnniPmpSpvccDestPartyTable": pnniPmpSpvccDestPartyTable,
       "pnniPmpSpvccDestPartyEntry": pnniPmpSpvccDestPartyEntry,
       "pnniPmpSpvccDestPartyIndex": pnniPmpSpvccDestPartyIndex,
       "pnniPmpSpvccDestPartyAtmAddr": pnniPmpSpvccDestPartyAtmAddr,
       "pnniPmpSpvccDestPartyPort": pnniPmpSpvccDestPartyPort,
       "pnniPmpSpvccDestPartyAssignedVPI": pnniPmpSpvccDestPartyAssignedVPI,
       "pnniPmpSpvccDestPartyAssignedVCI": pnniPmpSpvccDestPartyAssignedVCI,
       "pnniPmpSpvccDestPartyUpTime": pnniPmpSpvccDestPartyUpTime,
       "pnniPmpSpvccDestPartyTransitNetSel": pnniPmpSpvccDestPartyTransitNetSel,
       "pnniPmpSpvccDestPartyStatus": pnniPmpSpvccDestPartyStatus,
       "pnniPmpSpvccDestPartyRGroupIndex": pnniPmpSpvccDestPartyRGroupIndex,
       "vpciMappingTableGroup": vpciMappingTableGroup,
       "vmtVpciMapTable": vmtVpciMapTable,
       "vmtVpciMapEntry": vmtVpciMapEntry,
       "vmtVpciMapIndex": vmtVpciMapIndex,
       "vmtVpciMapVPCI": vmtVpciMapVPCI,
       "vmtVpciMapVPI": vmtVpciMapVPI,
       "vmtVpciMapPort": vmtVpciMapPort,
       "vmtVpciMapStatus": vmtVpciMapStatus,
       "vmtVpciMapGroupTable": vmtVpciMapGroupTable,
       "vmtVpciMapGroupEntry": vmtVpciMapGroupEntry,
       "vmtVpciMapGroupIndex": vmtVpciMapGroupIndex,
       "vmtVpciMapGroupStatus": vmtVpciMapGroupStatus,
       "vmtVpciMapListTable": vmtVpciMapListTable,
       "vmtVpciMapListEntry": vmtVpciMapListEntry,
       "vmtVpciMapListIndex": vmtVpciMapListIndex,
       "vmtVpciMapListMEIndex": vmtVpciMapListMEIndex,
       "vmtVpciMapListStatus": vmtVpciMapListStatus,
       "pnniSpvxcRGroupTable": pnniSpvxcRGroupTable,
       "pnniSpvxcRGroupEntry": pnniSpvxcRGroupEntry,
       "pnniSpvxcRGroupIndex": pnniSpvxcRGroupIndex,
       "pnniSpvxcRGroupPrimaryPort": pnniSpvxcRGroupPrimaryPort,
       "pnniSpvxcRGroupSecondaryPort": pnniSpvxcRGroupSecondaryPort,
       "pnniSpvxcRGroupNsapAddr": pnniSpvxcRGroupNsapAddr,
       "pnniSpvxcRGroupSwitchoverCmd": pnniSpvxcRGroupSwitchoverCmd,
       "pnniSpvxcRGroupActivePort": pnniSpvxcRGroupActivePort,
       "pnniSpvxcRGroupPacingNumber": pnniSpvxcRGroupPacingNumber,
       "pnniSpvxcRGroupPacingInterval": pnniSpvxcRGroupPacingInterval,
       "pnniSpvxcRGroupAutoPVCSwitchover": pnniSpvxcRGroupAutoPVCSwitchover,
       "pnniSpvxcRGroupName": pnniSpvxcRGroupName,
       "pnniSpvxcRGroupState": pnniSpvxcRGroupState,
       "pnniSpvxcRGroupRowStatus": pnniSpvxcRGroupRowStatus,
       "proxyDirMapEntryGroup": proxyDirMapEntryGroup,
       "proxyDirMapEntryTable": proxyDirMapEntryTable,
       "proxyDirMapEntry": proxyDirMapEntry,
       "proxyDirMapIndex": proxyDirMapIndex,
       "proxyDirMapAESA": proxyDirMapAESA,
       "proxyDirMapGroup": proxyDirMapGroup,
       "proxyDirMapVPCI": proxyDirMapVPCI,
       "proxyDirMapStatus": proxyDirMapStatus,
       "proxyDirMapVp": proxyDirMapVp,
       "proxyDirMapPort": proxyDirMapPort,
       "proxyDirGroupGroup": proxyDirGroupGroup,
       "proxyDirGroupTable": proxyDirGroupTable,
       "proxyDirGroupEntry": proxyDirGroupEntry,
       "proxyDirGroupIndex": proxyDirGroupIndex,
       "proxyDirGroupPrefix": proxyDirGroupPrefix,
       "proxyDirGroupVPCIGroup": proxyDirGroupVPCIGroup,
       "proxyDirGroupStatus": proxyDirGroupStatus,
       "swBoardGroup": swBoardGroup,
       "swBoardTable": swBoardTable,
       "swBoardEntry": swBoardEntry,
       "swBoardIndex": swBoardIndex,
       "swBoardMaxPaths": swBoardMaxPaths,
       "swBoardMaxChannels": swBoardMaxChannels,
       "swBoardAtmAddress": swBoardAtmAddress,
       "swBoardUptime": swBoardUptime,
       "swBoardCDV": swBoardCDV,
       "swBoardPolicingAction": swBoardPolicingAction,
       "swBoardNsapPrefix": swBoardNsapPrefix,
       "swBoardClockScalingFactor": swBoardClockScalingFactor,
       "swBoardDebugMode": swBoardDebugMode,
       "swBoardMulticastMode": swBoardMulticastMode,
       "swBoardFingerMode": swBoardFingerMode,
       "swBoardATMLayerOAM": swBoardATMLayerOAM,
       "swBoardTopologyGroup": swBoardTopologyGroup,
       "swBoardTopoTable": swBoardTopoTable,
       "swBoardTopoEntry": swBoardTopoEntry,
       "swBoardTopoIndex": swBoardTopoIndex,
       "swBoardTopoNumberOfLinks": swBoardTopoNumberOfLinks,
       "swBoardLinkTable": swBoardLinkTable,
       "swBoardLinkEntry": swBoardLinkEntry,
       "swBoardLinkIndex": swBoardLinkIndex,
       "swBoardLinkSrc": swBoardLinkSrc,
       "swBoardLinkDest": swBoardLinkDest,
       "swBoardLinkCapacity": swBoardLinkCapacity,
       "swBoardLinkAge": swBoardLinkAge,
       "nsapGroup": nsapGroup,
       "nsapNetworkPrefixTable": nsapNetworkPrefixTable,
       "nsapNetworkPrefixEntry": nsapNetworkPrefixEntry,
       "nsapNetworkPrefixPort": nsapNetworkPrefixPort,
       "nsapNetworkPrefixVPI": nsapNetworkPrefixVPI,
       "nsapNetworkPrefixValue": nsapNetworkPrefixValue,
       "nsapNetworkPrefixStatus": nsapNetworkPrefixStatus,
       "nsapTopologyTable": nsapTopologyTable,
       "nsapTopologyEntry": nsapTopologyEntry,
       "nsapTopoBoard": nsapTopoBoard,
       "nsapTopoLinkSrc": nsapTopoLinkSrc,
       "nsapTopoLinkSrcMask": nsapTopoLinkSrcMask,
       "nsapTopoLinkSrcPort": nsapTopoLinkSrcPort,
       "nsapTopoLinkSrcVpi": nsapTopoLinkSrcVpi,
       "nsapTopoLinkDest": nsapTopoLinkDest,
       "nsapTopoLinkDestMask": nsapTopoLinkDestMask,
       "nsapTopoLinkDestPort": nsapTopoLinkDestPort,
       "nsapTopoLinkDestVpi": nsapTopoLinkDestVpi,
       "nsapTopoLinkCost": nsapTopoLinkCost,
       "nsapTopoLinkUbrVCs": nsapTopoLinkUbrVCs,
       "nsapTopoLinkCbrCapacity": nsapTopoLinkCbrCapacity,
       "nsapTopoLinkCbrFifo": nsapTopoLinkCbrFifo,
       "nsapTopoLinkVbrCapacity": nsapTopoLinkVbrCapacity,
       "nsapTopoLinkVbrFifo": nsapTopoLinkVbrFifo,
       "nsapTopoLinkOrig": nsapTopoLinkOrig,
       "nsapTopoLinkCapabilitySet": nsapTopoLinkCapabilitySet,
       "nsapTopoLinkFreshness": nsapTopoLinkFreshness,
       "nsapTopoLinkUbrEstimatedBandwidth": nsapTopoLinkUbrEstimatedBandwidth,
       "nsapStaticRouteTable": nsapStaticRouteTable,
       "nsapStaticRouteEntry": nsapStaticRouteEntry,
       "nsapStaticRouteAddress": nsapStaticRouteAddress,
       "nsapStaticRouteMask": nsapStaticRouteMask,
       "nsapStaticRoutePort": nsapStaticRoutePort,
       "nsapStaticRouteVPI": nsapStaticRouteVPI,
       "nsapStaticRouteCost": nsapStaticRouteCost,
       "nsapStaticRouteMaxCbrCap": nsapStaticRouteMaxCbrCap,
       "nsapStaticRouteMaxVbrCap": nsapStaticRouteMaxVbrCap,
       "nsapStaticRouteAbrSupport": nsapStaticRouteAbrSupport,
       "nsapStaticRouteEpdSupport": nsapStaticRouteEpdSupport,
       "nsapStaticRouteStatus": nsapStaticRouteStatus,
       "ftPnniDTLTable": ftPnniDTLTable,
       "ftPnniDTLEntry": ftPnniDTLEntry,
       "ftPnniDTLIndex": ftPnniDTLIndex,
       "ftPnniDTLEntryIndex": ftPnniDTLEntryIndex,
       "ftPnniDTLNodePrefix": ftPnniDTLNodePrefix,
       "ftPnniDTLNodeMask": ftPnniDTLNodeMask,
       "ftPnniDTLPort": ftPnniDTLPort,
       "ftPnniDTLVPI": ftPnniDTLVPI,
       "ftPnniDTLStatus": ftPnniDTLStatus,
       "ftPnniSummaryTable": ftPnniSummaryTable,
       "ftPnniSummaryEntry": ftPnniSummaryEntry,
       "ftPnniSummaryAddress": ftPnniSummaryAddress,
       "ftPnniSummaryPrefixLength": ftPnniSummaryPrefixLength,
       "ftPnniSummaryType": ftPnniSummaryType,
       "ftPnniSummarySuppress": ftPnniSummarySuppress,
       "ftPnniSummaryState": ftPnniSummaryState,
       "ftPnniSummaryStatus": ftPnniSummaryStatus,
       "upcContractGroup": upcContractGroup,
       "upcContractTable": upcContractTable,
       "upcContractEntry": upcContractEntry,
       "upcContractKey": upcContractKey,
       "upcContractEntryStatus": upcContractEntryStatus,
       "upcContractPCR01": upcContractPCR01,
       "upcContractSCR01": upcContractSCR01,
       "upcContractMBS01": upcContractMBS01,
       "upcContractPCR0": upcContractPCR0,
       "upcContractSCR0": upcContractSCR0,
       "upcContractMBS0": upcContractMBS0,
       "upcContractCDVT": upcContractCDVT,
       "upcContractTagReq": upcContractTagReq,
       "upcContractAal5Epd": upcContractAal5Epd,
       "upcContractName": upcContractName,
       "upcContractDoGCRAPolicing": upcContractDoGCRAPolicing,
       "upcContractIsAAL5": upcContractIsAAL5,
       "upcContractDoPacketDiscard": upcContractDoPacketDiscard,
       "upcContractDoPPPolicing": upcContractDoPPPolicing,
       "upcContractDoUBRTagging": upcContractDoUBRTagging,
       "upcContractSchedMode": upcContractSchedMode,
       "upcContractUseAltCLPThreshold": upcContractUseAltCLPThreshold,
       "upcContractMCR": upcContractMCR,
       "upcContractEstimatedUbrBandwidth": upcContractEstimatedUbrBandwidth,
       "upcContractAAL5CountingMode": upcContractAAL5CountingMode,
       "upcContractServiceCategory": upcContractServiceCategory,
       "upcContractPoliceScheme": upcContractPoliceScheme,
       "upcContractPCR": upcContractPCR,
       "upcContractSCR": upcContractSCR,
       "upcContractMBS": upcContractMBS,
       "upcContractServiceSubCategory": upcContractServiceSubCategory,
       "upcContractCongestionBasedPeakBw": upcContractCongestionBasedPeakBw,
       "upcContractBehaviorClassSelector": upcContractBehaviorClassSelector,
       "confTopologyGroup": confTopologyGroup,
       "confTopoHelloInterval": confTopoHelloInterval,
       "confTopoNsapIndInterval": confTopoNsapIndInterval,
       "confTopoStaticUpdateInterval": confTopoStaticUpdateInterval,
       "confTopoMaxHopCount": confTopoMaxHopCount,
       "confTopoACRPropMult": confTopoACRPropMult,
       "confTopoMinThresh": confTopoMinThresh,
       "confTopoMinVCAvail": confTopoMinVCAvail,
       "confTopoSpansAreaID": confTopoSpansAreaID,
       "confTopoSpansBorderSwitch": confTopoSpansBorderSwitch,
       "confTopoSwitchPrefix": confTopoSwitchPrefix,
       "confTopoSwitchPrefixMask": confTopoSwitchPrefixMask,
       "confTopoPeerGroupMask": confTopoPeerGroupMask,
       "confTopoSpansPnniBorderSwitch": confTopoSpansPnniBorderSwitch,
       "confTopoPGSNReachCost": confTopoPGSNReachCost,
       "confTopoPGSNReachCostMethod": confTopoPGSNReachCostMethod,
       "confTopoFtPnniForeArea": confTopoFtPnniForeArea,
       "confTopoFtPnniForeLevel": confTopoFtPnniForeLevel,
       "confTopoLBUbrLoadBalance": confTopoLBUbrLoadBalance,
       "oamGroup": oamGroup,
       "oamGeneratingChannelTable": oamGeneratingChannelTable,
       "oamGeneratingChannelEntry": oamGeneratingChannelEntry,
       "oamGeneratingChannelCells": oamGeneratingChannelCells,
       "oamGeneratingOpathTable": oamGeneratingOpathTable,
       "oamGeneratingOpathEntry": oamGeneratingOpathEntry,
       "oamGeneratingOpathCells": oamGeneratingOpathCells,
       "oamGeneratingPathrTable": oamGeneratingPathrTable,
       "oamGeneratingPathrEntry": oamGeneratingPathrEntry,
       "oamGeneratingPathrCells": oamGeneratingPathrCells,
       "oamReceivedPathTable": oamReceivedPathTable,
       "oamReceivedPathEntry": oamReceivedPathEntry,
       "oamReceivedPathAISCells": oamReceivedPathAISCells,
       "oamReceivedPathRDICells": oamReceivedPathRDICells,
       "guardGroup": guardGroup,
       "guardTable": guardTable,
       "guardEntry": guardEntry,
       "oamGuard": oamGuard,
       "ifIndexMapGroup": ifIndexMapGroup,
       "ifIndexMapTable": ifIndexMapTable,
       "ifIndexMapEntry": ifIndexMapEntry,
       "ifIndexMapIndex": ifIndexMapIndex,
       "ifIndexMapBoard": ifIndexMapBoard,
       "ifIndexMapNetmod": ifIndexMapNetmod,
       "ifIndexMapPort": ifIndexMapPort,
       "ifIndexNameGroup": ifIndexNameGroup,
       "cesExtGroup": cesExtGroup,
       "cesExtTable": cesExtTable,
       "cbrctConfTable": cbrctConfTable,
       "cbrctConfEntry": cbrctConfEntry,
       "cbrctState": cbrctState,
       "cbrctIdleDetection": cbrctIdleDetection,
       "cbrctIdleMask": cbrctIdleMask,
       "cbrctNoOfIdlePatterns": cbrctNoOfIdlePatterns,
       "cbrctIdlePatterns": cbrctIdlePatterns,
       "cbrctIdleIntPeriod": cbrctIdleIntPeriod,
       "cbrctActiveIntPeriod": cbrctActiveIntPeriod,
       "qosClassExpansionGroup": qosClassExpansionGroup,
       "qosClassExpansionTable": qosClassExpansionTable,
       "qosClassExpansionEntry": qosClassExpansionEntry,
       "qosClassExpansionKey": qosClassExpansionKey,
       "qosClassValue": qosClassValue,
       "qosClassExpansionEntryStatus": qosClassExpansionEntryStatus,
       "qosClassFwdCtd": qosClassFwdCtd,
       "qosClassFwdCdv": qosClassFwdCdv,
       "qosClassBackCdv": qosClassBackCdv,
       "qosClassFwdClr": qosClassFwdClr,
       "qosClassBackClr": qosClassBackClr,
       "qosClassName": qosClassName,
       "pathExtGroup": pathExtGroup,
       "pathExtQosMetricTable": pathExtQosMetricTable,
       "pathExtQosMetricEntry": pathExtQosMetricEntry,
       "pathExtQosMetricIndex": pathExtQosMetricIndex,
       "pathExtQosMetricMaxCtd": pathExtQosMetricMaxCtd,
       "pathExtQosMetricMaxCdv": pathExtQosMetricMaxCdv,
       "pathExtQosMetricMaxClr": pathExtQosMetricMaxClr,
       "pathExtQosMetricEntryStatus": pathExtQosMetricEntryStatus,
       "pathExtTable": pathExtTable,
       "pathExtEntry": pathExtEntry,
       "pathExtCbrMetric": pathExtCbrMetric,
       "pathExtRtVbrMetric": pathExtRtVbrMetric,
       "pathExtNrtVbrMetric": pathExtNrtVbrMetric,
       "pathExtAbrMetric": pathExtAbrMetric,
       "pathExtUbrMetric": pathExtUbrMetric,
       "pathExtEntryStatus": pathExtEntryStatus,
       "outputPathExtTable": outputPathExtTable,
       "outputPathExtEntry": outputPathExtEntry,
       "opathExtCbrMetric": opathExtCbrMetric,
       "opathExtRtVbrMetric": opathExtRtVbrMetric,
       "opathExtNrtVbrMetric": opathExtNrtVbrMetric,
       "opathExtAbrMetric": opathExtAbrMetric,
       "opathExtUbrMetric": opathExtUbrMetric,
       "opathExtEntryStatus": opathExtEntryStatus,
       "vpGroupTable": vpGroupTable,
       "vpGroupEntry": vpGroupEntry,
       "vpGroupIndex": vpGroupIndex,
       "vpGroupPort": vpGroupPort,
       "vpGroupVPI": vpGroupVPI,
       "vpGroupVPCI": vpGroupVPCI,
       "vpGroupEntryStatus": vpGroupEntryStatus,
       "poolGroup": poolGroup,
       "poolConfGroup": poolConfGroup,
       "poolConfPPCalls": poolConfPPCalls,
       "poolConfPMPCalls": poolConfPMPCalls,
       "poolConfMaxPercentage": poolConfMaxPercentage,
       "asxAtmIfGroup": asxAtmIfGroup,
       "asxAtmIfTable": asxAtmIfTable,
       "asxAtmIfEntry": asxAtmIfEntry,
       "asxAtmIfName": asxAtmIfName,
       "asxAtmIfLinkid": asxAtmIfLinkid,
       "syncStatusMsgGroup": syncStatusMsgGroup,
       "syslogGroup": syslogGroup,
       "syslogFacility": syslogFacility,
       "syslogConsoleState": syslogConsoleState,
       "syslogDestinationTable": syslogDestinationTable,
       "syslogDestinationEntry": syslogDestinationEntry,
       "syslogDestinationHost": syslogDestinationHost,
       "syslogDestinationStatus": syslogDestinationStatus,
       "snmp": snmp,
       "trapConfGroup": trapConfGroup,
       "trapNumberOfDest": trapNumberOfDest,
       "trapDestTable": trapDestTable,
       "trapDestEntry": trapDestEntry,
       "trapDest": trapDest,
       "trapDestStatus": trapDestStatus,
       "snmpConfGroup": snmpConfGroup,
       "snmpReconfigure": snmpReconfigure,
       "snmpReadCommunity": snmpReadCommunity,
       "snmpWriteCommunity": snmpWriteCommunity,
       "snmpWarmStart": snmpWarmStart,
       "snmpColdStart": snmpColdStart,
       "snmpRemoteSetsStatus": snmpRemoteSetsStatus,
       "snmpAgentAddressGroup": snmpAgentAddressGroup,
       "snmpThisAgentBoardNumber": snmpThisAgentBoardNumber,
       "snmpAgentTable": snmpAgentTable,
       "snmpAgentEntry": snmpAgentEntry,
       "snmpAgentBoardNumber": snmpAgentBoardNumber,
       "snmpAgentInterface": snmpAgentInterface,
       "snmpAgentAddress": snmpAgentAddress,
       "foreSwitchModule": foreSwitchModule}
)
