# SNMP MIB module (ATM-RMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATM-RMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:00 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(OwnerString,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "OwnerString",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

atmRmon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 16)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ZeroBasedCounter32(Gauge32, TextualConvention):
    status = "current"


class LastCreateTime(TimeTicks, TextualConvention):
    status = "current"


class AtmAddr(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(13, 13),
        ValueSizeConstraint(20, 20),
    )



class ServiceClass(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abrAndUbr", 2),
          ("cbrAndVbr", 1))
    )



class ResourcePriority(Integer32, TextualConvention):
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
        *(("highPriority", 3),
          ("lowPriority", 1),
          ("normalPriority", 2))
    )



class AddressCollectScope(Integer32, TextualConvention):
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
        *(("entireAddr", 3),
          ("prefix", 1),
          ("prefixAndEsi", 2))
    )



class ConnectTime(Gauge32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_AtmRmonMIBObjects_ObjectIdentity = ObjectIdentity
atmRmonMIBObjects = _AtmRmonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1)
)
_PortSelect_ObjectIdentity = ObjectIdentity
portSelect = _PortSelect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 1)
)
_PortSelGrpTable_Object = MibTable
portSelGrpTable = _PortSelGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 1, 1)
)
if mibBuilder.loadTexts:
    portSelGrpTable.setStatus("current")
_PortSelGrpEntry_Object = MibTableRow
portSelGrpEntry = _PortSelGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 1, 1, 1)
)
portSelGrpEntry.setIndexNames(
    (0, "ATM-RMON-MIB", "portSelGrpIndex"),
)
if mibBuilder.loadTexts:
    portSelGrpEntry.setStatus("current")


class _PortSelGrpIndex_Type(Integer32):
    """Custom type portSelGrpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortSelGrpIndex_Type.__name__ = "Integer32"
_PortSelGrpIndex_Object = MibTableColumn
portSelGrpIndex = _PortSelGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 1, 1, 1, 1),
    _PortSelGrpIndex_Type()
)
portSelGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portSelGrpIndex.setStatus("current")


class _PortSelGrpDescr_Type(DisplayString):
    """Custom type portSelGrpDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PortSelGrpDescr_Type.__name__ = "DisplayString"
_PortSelGrpDescr_Object = MibTableColumn
portSelGrpDescr = _PortSelGrpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 1, 1, 1, 2),
    _PortSelGrpDescr_Type()
)
portSelGrpDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portSelGrpDescr.setStatus("current")
_PortSelGrpCreateTime_Type = LastCreateTime
_PortSelGrpCreateTime_Object = MibTableColumn
portSelGrpCreateTime = _PortSelGrpCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 1, 1, 1, 3),
    _PortSelGrpCreateTime_Type()
)
portSelGrpCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSelGrpCreateTime.setStatus("current")
_PortSelGrpOwner_Type = OwnerString
_PortSelGrpOwner_Object = MibTableColumn
portSelGrpOwner = _PortSelGrpOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 1, 1, 1, 4),
    _PortSelGrpOwner_Type()
)
portSelGrpOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portSelGrpOwner.setStatus("current")
_PortSelGrpStatus_Type = RowStatus
_PortSelGrpStatus_Object = MibTableColumn
portSelGrpStatus = _PortSelGrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 1, 1, 1, 5),
    _PortSelGrpStatus_Type()
)
portSelGrpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portSelGrpStatus.setStatus("current")
_PortSelTable_Object = MibTable
portSelTable = _PortSelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 1, 2)
)
if mibBuilder.loadTexts:
    portSelTable.setStatus("current")
_PortSelEntry_Object = MibTableRow
portSelEntry = _PortSelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 1, 2, 1)
)
portSelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    portSelEntry.setStatus("current")


class _PortSelCollectGroup_Type(Integer32):
    """Custom type portSelCollectGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortSelCollectGroup_Type.__name__ = "Integer32"
_PortSelCollectGroup_Object = MibTableColumn
portSelCollectGroup = _PortSelCollectGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 1, 2, 1, 1),
    _PortSelCollectGroup_Type()
)
portSelCollectGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portSelCollectGroup.setStatus("current")
_PortSelCreateTime_Type = LastCreateTime
_PortSelCreateTime_Object = MibTableColumn
portSelCreateTime = _PortSelCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 1, 2, 1, 2),
    _PortSelCreateTime_Type()
)
portSelCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSelCreateTime.setStatus("current")
_PortSelOwner_Type = OwnerString
_PortSelOwner_Object = MibTableColumn
portSelOwner = _PortSelOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 1, 2, 1, 3),
    _PortSelOwner_Type()
)
portSelOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portSelOwner.setStatus("current")
_PortSelStatus_Type = RowStatus
_PortSelStatus_Object = MibTableColumn
portSelStatus = _PortSelStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 1, 2, 1, 4),
    _PortSelStatus_Type()
)
portSelStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portSelStatus.setStatus("current")
_AtmStats_ObjectIdentity = ObjectIdentity
atmStats = _AtmStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 2)
)
_AtmStatsControlTable_Object = MibTable
atmStatsControlTable = _AtmStatsControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 2, 1)
)
if mibBuilder.loadTexts:
    atmStatsControlTable.setStatus("current")
_AtmStatsControlEntry_Object = MibTableRow
atmStatsControlEntry = _AtmStatsControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 2, 1, 1)
)
atmStatsControlEntry.setIndexNames(
    (0, "ATM-RMON-MIB", "portSelGrpIndex"),
)
if mibBuilder.loadTexts:
    atmStatsControlEntry.setStatus("current")
_AtmStatsControlDropEvents_Type = Counter32
_AtmStatsControlDropEvents_Object = MibTableColumn
atmStatsControlDropEvents = _AtmStatsControlDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 2, 1, 1, 1),
    _AtmStatsControlDropEvents_Type()
)
atmStatsControlDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmStatsControlDropEvents.setStatus("current")
_AtmStatsControlOwner_Type = OwnerString
_AtmStatsControlOwner_Object = MibTableColumn
atmStatsControlOwner = _AtmStatsControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 2, 1, 1, 2),
    _AtmStatsControlOwner_Type()
)
atmStatsControlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmStatsControlOwner.setStatus("current")
_AtmStatsControlStatus_Type = RowStatus
_AtmStatsControlStatus_Object = MibTableColumn
atmStatsControlStatus = _AtmStatsControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 2, 1, 1, 3),
    _AtmStatsControlStatus_Type()
)
atmStatsControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmStatsControlStatus.setStatus("current")
_AtmStatsTable_Object = MibTable
atmStatsTable = _AtmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 2, 2)
)
if mibBuilder.loadTexts:
    atmStatsTable.setStatus("current")
_AtmStatsEntry_Object = MibTableRow
atmStatsEntry = _AtmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 2, 2, 1)
)
atmStatsEntry.setIndexNames(
    (0, "ATM-RMON-MIB", "portSelGrpIndex"),
    (0, "ATM-RMON-MIB", "atmStatsSClass"),
)
if mibBuilder.loadTexts:
    atmStatsEntry.setStatus("current")
_AtmStatsSClass_Type = ServiceClass
_AtmStatsSClass_Object = MibTableColumn
atmStatsSClass = _AtmStatsSClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 2, 2, 1, 1),
    _AtmStatsSClass_Type()
)
atmStatsSClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmStatsSClass.setStatus("current")
_AtmStatsCreateTime_Type = LastCreateTime
_AtmStatsCreateTime_Object = MibTableColumn
atmStatsCreateTime = _AtmStatsCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 2, 2, 1, 2),
    _AtmStatsCreateTime_Type()
)
atmStatsCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmStatsCreateTime.setStatus("current")
_AtmStatsCells_Type = Counter32
_AtmStatsCells_Object = MibTableColumn
atmStatsCells = _AtmStatsCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 2, 2, 1, 3),
    _AtmStatsCells_Type()
)
atmStatsCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmStatsCells.setStatus("current")
_AtmStatsCellsRollovers_Type = Counter32
_AtmStatsCellsRollovers_Object = MibTableColumn
atmStatsCellsRollovers = _AtmStatsCellsRollovers_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 2, 2, 1, 4),
    _AtmStatsCellsRollovers_Type()
)
atmStatsCellsRollovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmStatsCellsRollovers.setStatus("current")
_AtmStatsHCCells_Type = Counter64
_AtmStatsHCCells_Object = MibTableColumn
atmStatsHCCells = _AtmStatsHCCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 2, 2, 1, 5),
    _AtmStatsHCCells_Type()
)
atmStatsHCCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmStatsHCCells.setStatus("current")
_AtmStatsNumCallAttempts_Type = Counter32
_AtmStatsNumCallAttempts_Object = MibTableColumn
atmStatsNumCallAttempts = _AtmStatsNumCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 2, 2, 1, 6),
    _AtmStatsNumCallAttempts_Type()
)
atmStatsNumCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmStatsNumCallAttempts.setStatus("current")
_AtmStatsNumCalls_Type = Counter32
_AtmStatsNumCalls_Object = MibTableColumn
atmStatsNumCalls = _AtmStatsNumCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 2, 2, 1, 7),
    _AtmStatsNumCalls_Type()
)
atmStatsNumCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmStatsNumCalls.setStatus("current")
_AtmStatsConnTime_Type = ConnectTime
_AtmStatsConnTime_Object = MibTableColumn
atmStatsConnTime = _AtmStatsConnTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 2, 2, 1, 8),
    _AtmStatsConnTime_Type()
)
atmStatsConnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmStatsConnTime.setStatus("current")
if mibBuilder.loadTexts:
    atmStatsConnTime.setUnits("seconds")
_AtmHost_ObjectIdentity = ObjectIdentity
atmHost = _AtmHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3)
)
_AtmHostControlTable_Object = MibTable
atmHostControlTable = _AtmHostControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 1)
)
if mibBuilder.loadTexts:
    atmHostControlTable.setStatus("current")
_AtmHostControlEntry_Object = MibTableRow
atmHostControlEntry = _AtmHostControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 1, 1)
)
atmHostControlEntry.setIndexNames(
    (0, "ATM-RMON-MIB", "portSelGrpIndex"),
)
if mibBuilder.loadTexts:
    atmHostControlEntry.setStatus("current")
_AtmHostControlInserts_Type = Counter32
_AtmHostControlInserts_Object = MibTableColumn
atmHostControlInserts = _AtmHostControlInserts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 1, 1, 1),
    _AtmHostControlInserts_Type()
)
atmHostControlInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmHostControlInserts.setStatus("current")
_AtmHostControlDeletes_Type = Counter32
_AtmHostControlDeletes_Object = MibTableColumn
atmHostControlDeletes = _AtmHostControlDeletes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 1, 1, 2),
    _AtmHostControlDeletes_Type()
)
atmHostControlDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmHostControlDeletes.setStatus("current")


class _AtmHostControlMaxDesiredEntries_Type(Integer32):
    """Custom type atmHostControlMaxDesiredEntries based on Integer32"""
    defaultValue = -1


_AtmHostControlMaxDesiredEntries_Object = MibTableColumn
atmHostControlMaxDesiredEntries = _AtmHostControlMaxDesiredEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 1, 1, 3),
    _AtmHostControlMaxDesiredEntries_Type()
)
atmHostControlMaxDesiredEntries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmHostControlMaxDesiredEntries.setStatus("current")


class _AtmHostControlPriority_Type(ResourcePriority):
    """Custom type atmHostControlPriority based on ResourcePriority"""


_AtmHostControlPriority_Object = MibTableColumn
atmHostControlPriority = _AtmHostControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 1, 1, 4),
    _AtmHostControlPriority_Type()
)
atmHostControlPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmHostControlPriority.setStatus("current")


class _AtmHostControlAddrCollectScope_Type(AddressCollectScope):
    """Custom type atmHostControlAddrCollectScope based on AddressCollectScope"""


_AtmHostControlAddrCollectScope_Object = MibTableColumn
atmHostControlAddrCollectScope = _AtmHostControlAddrCollectScope_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 1, 1, 5),
    _AtmHostControlAddrCollectScope_Type()
)
atmHostControlAddrCollectScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmHostControlAddrCollectScope.setStatus("current")
_AtmHostControlDropEvents_Type = Counter32
_AtmHostControlDropEvents_Object = MibTableColumn
atmHostControlDropEvents = _AtmHostControlDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 1, 1, 6),
    _AtmHostControlDropEvents_Type()
)
atmHostControlDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmHostControlDropEvents.setStatus("current")
_AtmHostControlOwner_Type = OwnerString
_AtmHostControlOwner_Object = MibTableColumn
atmHostControlOwner = _AtmHostControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 1, 1, 7),
    _AtmHostControlOwner_Type()
)
atmHostControlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmHostControlOwner.setStatus("current")
_AtmHostControlStatus_Type = RowStatus
_AtmHostControlStatus_Object = MibTableColumn
atmHostControlStatus = _AtmHostControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 1, 1, 8),
    _AtmHostControlStatus_Type()
)
atmHostControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmHostControlStatus.setStatus("current")
_AtmHostTable_Object = MibTable
atmHostTable = _AtmHostTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2)
)
if mibBuilder.loadTexts:
    atmHostTable.setStatus("current")
_AtmHostEntry_Object = MibTableRow
atmHostEntry = _AtmHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1)
)
atmHostEntry.setIndexNames(
    (0, "ATM-RMON-MIB", "portSelGrpIndex"),
    (0, "ATM-RMON-MIB", "atmHostAddress"),
    (0, "ATM-RMON-MIB", "atmHostSClass"),
)
if mibBuilder.loadTexts:
    atmHostEntry.setStatus("current")
_AtmHostAddress_Type = AtmAddr
_AtmHostAddress_Object = MibTableColumn
atmHostAddress = _AtmHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1, 1),
    _AtmHostAddress_Type()
)
atmHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmHostAddress.setStatus("current")
_AtmHostSClass_Type = ServiceClass
_AtmHostSClass_Object = MibTableColumn
atmHostSClass = _AtmHostSClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1, 2),
    _AtmHostSClass_Type()
)
atmHostSClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmHostSClass.setStatus("current")
_AtmHostCreateTime_Type = LastCreateTime
_AtmHostCreateTime_Object = MibTableColumn
atmHostCreateTime = _AtmHostCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1, 3),
    _AtmHostCreateTime_Type()
)
atmHostCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmHostCreateTime.setStatus("current")
_AtmHostInCells_Type = ZeroBasedCounter32
_AtmHostInCells_Object = MibTableColumn
atmHostInCells = _AtmHostInCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1, 4),
    _AtmHostInCells_Type()
)
atmHostInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmHostInCells.setStatus("current")
_AtmHostInCellsRollovers_Type = ZeroBasedCounter32
_AtmHostInCellsRollovers_Object = MibTableColumn
atmHostInCellsRollovers = _AtmHostInCellsRollovers_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1, 5),
    _AtmHostInCellsRollovers_Type()
)
atmHostInCellsRollovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmHostInCellsRollovers.setStatus("current")
_AtmHostInHCCells_Type = Counter64
_AtmHostInHCCells_Object = MibTableColumn
atmHostInHCCells = _AtmHostInHCCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1, 6),
    _AtmHostInHCCells_Type()
)
atmHostInHCCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmHostInHCCells.setStatus("current")
_AtmHostOutCells_Type = ZeroBasedCounter32
_AtmHostOutCells_Object = MibTableColumn
atmHostOutCells = _AtmHostOutCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1, 7),
    _AtmHostOutCells_Type()
)
atmHostOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmHostOutCells.setStatus("current")
_AtmHostOutCellsRollovers_Type = ZeroBasedCounter32
_AtmHostOutCellsRollovers_Object = MibTableColumn
atmHostOutCellsRollovers = _AtmHostOutCellsRollovers_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1, 8),
    _AtmHostOutCellsRollovers_Type()
)
atmHostOutCellsRollovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmHostOutCellsRollovers.setStatus("current")
_AtmHostOutHCCells_Type = Counter64
_AtmHostOutHCCells_Object = MibTableColumn
atmHostOutHCCells = _AtmHostOutHCCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1, 9),
    _AtmHostOutHCCells_Type()
)
atmHostOutHCCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmHostOutHCCells.setStatus("current")
_AtmHostInNumCallAttempts_Type = ZeroBasedCounter32
_AtmHostInNumCallAttempts_Object = MibTableColumn
atmHostInNumCallAttempts = _AtmHostInNumCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1, 10),
    _AtmHostInNumCallAttempts_Type()
)
atmHostInNumCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmHostInNumCallAttempts.setStatus("current")
_AtmHostInNumCalls_Type = ZeroBasedCounter32
_AtmHostInNumCalls_Object = MibTableColumn
atmHostInNumCalls = _AtmHostInNumCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1, 11),
    _AtmHostInNumCalls_Type()
)
atmHostInNumCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmHostInNumCalls.setStatus("current")
_AtmHostOutNumCallAttempts_Type = ZeroBasedCounter32
_AtmHostOutNumCallAttempts_Object = MibTableColumn
atmHostOutNumCallAttempts = _AtmHostOutNumCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1, 12),
    _AtmHostOutNumCallAttempts_Type()
)
atmHostOutNumCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmHostOutNumCallAttempts.setStatus("current")
_AtmHostOutNumCalls_Type = ZeroBasedCounter32
_AtmHostOutNumCalls_Object = MibTableColumn
atmHostOutNumCalls = _AtmHostOutNumCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1, 13),
    _AtmHostOutNumCalls_Type()
)
atmHostOutNumCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmHostOutNumCalls.setStatus("current")
_AtmHostInConnTime_Type = ConnectTime
_AtmHostInConnTime_Object = MibTableColumn
atmHostInConnTime = _AtmHostInConnTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1, 14),
    _AtmHostInConnTime_Type()
)
atmHostInConnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmHostInConnTime.setStatus("current")
if mibBuilder.loadTexts:
    atmHostInConnTime.setUnits("seconds")
_AtmHostOutConnTime_Type = ConnectTime
_AtmHostOutConnTime_Object = MibTableColumn
atmHostOutConnTime = _AtmHostOutConnTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 3, 2, 1, 15),
    _AtmHostOutConnTime_Type()
)
atmHostOutConnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmHostOutConnTime.setStatus("current")
if mibBuilder.loadTexts:
    atmHostOutConnTime.setUnits("seconds")
_AtmMatrix_ObjectIdentity = ObjectIdentity
atmMatrix = _AtmMatrix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4)
)
_AtmMatrixControlTable_Object = MibTable
atmMatrixControlTable = _AtmMatrixControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 1)
)
if mibBuilder.loadTexts:
    atmMatrixControlTable.setStatus("current")
_AtmMatrixControlEntry_Object = MibTableRow
atmMatrixControlEntry = _AtmMatrixControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 1, 1)
)
atmMatrixControlEntry.setIndexNames(
    (0, "ATM-RMON-MIB", "portSelGrpIndex"),
)
if mibBuilder.loadTexts:
    atmMatrixControlEntry.setStatus("current")
_AtmMatrixControlInserts_Type = Counter32
_AtmMatrixControlInserts_Object = MibTableColumn
atmMatrixControlInserts = _AtmMatrixControlInserts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 1, 1, 1),
    _AtmMatrixControlInserts_Type()
)
atmMatrixControlInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMatrixControlInserts.setStatus("current")
_AtmMatrixControlDeletes_Type = Counter32
_AtmMatrixControlDeletes_Object = MibTableColumn
atmMatrixControlDeletes = _AtmMatrixControlDeletes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 1, 1, 2),
    _AtmMatrixControlDeletes_Type()
)
atmMatrixControlDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMatrixControlDeletes.setStatus("current")


class _AtmMatrixControlMaxDesiredEntries_Type(Integer32):
    """Custom type atmMatrixControlMaxDesiredEntries based on Integer32"""
    defaultValue = -1


_AtmMatrixControlMaxDesiredEntries_Object = MibTableColumn
atmMatrixControlMaxDesiredEntries = _AtmMatrixControlMaxDesiredEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 1, 1, 3),
    _AtmMatrixControlMaxDesiredEntries_Type()
)
atmMatrixControlMaxDesiredEntries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmMatrixControlMaxDesiredEntries.setStatus("current")


class _AtmMatrixControlPriority_Type(ResourcePriority):
    """Custom type atmMatrixControlPriority based on ResourcePriority"""


_AtmMatrixControlPriority_Object = MibTableColumn
atmMatrixControlPriority = _AtmMatrixControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 1, 1, 4),
    _AtmMatrixControlPriority_Type()
)
atmMatrixControlPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmMatrixControlPriority.setStatus("current")


class _AtmMatrixControlAddrCollectScope_Type(AddressCollectScope):
    """Custom type atmMatrixControlAddrCollectScope based on AddressCollectScope"""


_AtmMatrixControlAddrCollectScope_Object = MibTableColumn
atmMatrixControlAddrCollectScope = _AtmMatrixControlAddrCollectScope_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 1, 1, 5),
    _AtmMatrixControlAddrCollectScope_Type()
)
atmMatrixControlAddrCollectScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmMatrixControlAddrCollectScope.setStatus("current")
_AtmMatrixControlDropEvents_Type = Counter32
_AtmMatrixControlDropEvents_Object = MibTableColumn
atmMatrixControlDropEvents = _AtmMatrixControlDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 1, 1, 6),
    _AtmMatrixControlDropEvents_Type()
)
atmMatrixControlDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMatrixControlDropEvents.setStatus("current")
_AtmMatrixControlOwner_Type = OwnerString
_AtmMatrixControlOwner_Object = MibTableColumn
atmMatrixControlOwner = _AtmMatrixControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 1, 1, 7),
    _AtmMatrixControlOwner_Type()
)
atmMatrixControlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmMatrixControlOwner.setStatus("current")
_AtmMatrixControlStatus_Type = RowStatus
_AtmMatrixControlStatus_Object = MibTableColumn
atmMatrixControlStatus = _AtmMatrixControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 1, 1, 8),
    _AtmMatrixControlStatus_Type()
)
atmMatrixControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmMatrixControlStatus.setStatus("current")
_AtmMatrixSDTable_Object = MibTable
atmMatrixSDTable = _AtmMatrixSDTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 2)
)
if mibBuilder.loadTexts:
    atmMatrixSDTable.setStatus("current")
_AtmMatrixSDEntry_Object = MibTableRow
atmMatrixSDEntry = _AtmMatrixSDEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 2, 1)
)
atmMatrixSDEntry.setIndexNames(
    (0, "ATM-RMON-MIB", "portSelGrpIndex"),
    (0, "ATM-RMON-MIB", "atmMatrixSDSrcAddress"),
    (0, "ATM-RMON-MIB", "atmMatrixSDDstAddress"),
    (0, "ATM-RMON-MIB", "atmMatrixSDSClass"),
)
if mibBuilder.loadTexts:
    atmMatrixSDEntry.setStatus("current")
_AtmMatrixSDSrcAddress_Type = AtmAddr
_AtmMatrixSDSrcAddress_Object = MibTableColumn
atmMatrixSDSrcAddress = _AtmMatrixSDSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 2, 1, 1),
    _AtmMatrixSDSrcAddress_Type()
)
atmMatrixSDSrcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmMatrixSDSrcAddress.setStatus("current")
_AtmMatrixSDDstAddress_Type = AtmAddr
_AtmMatrixSDDstAddress_Object = MibTableColumn
atmMatrixSDDstAddress = _AtmMatrixSDDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 2, 1, 2),
    _AtmMatrixSDDstAddress_Type()
)
atmMatrixSDDstAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmMatrixSDDstAddress.setStatus("current")
_AtmMatrixSDSClass_Type = ServiceClass
_AtmMatrixSDSClass_Object = MibTableColumn
atmMatrixSDSClass = _AtmMatrixSDSClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 2, 1, 3),
    _AtmMatrixSDSClass_Type()
)
atmMatrixSDSClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmMatrixSDSClass.setStatus("current")
_AtmMatrixSDCreateTime_Type = LastCreateTime
_AtmMatrixSDCreateTime_Object = MibTableColumn
atmMatrixSDCreateTime = _AtmMatrixSDCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 2, 1, 4),
    _AtmMatrixSDCreateTime_Type()
)
atmMatrixSDCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMatrixSDCreateTime.setStatus("current")
_AtmMatrixSDCells_Type = ZeroBasedCounter32
_AtmMatrixSDCells_Object = MibTableColumn
atmMatrixSDCells = _AtmMatrixSDCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 2, 1, 5),
    _AtmMatrixSDCells_Type()
)
atmMatrixSDCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMatrixSDCells.setStatus("current")
_AtmMatrixSDCellsRollovers_Type = ZeroBasedCounter32
_AtmMatrixSDCellsRollovers_Object = MibTableColumn
atmMatrixSDCellsRollovers = _AtmMatrixSDCellsRollovers_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 2, 1, 6),
    _AtmMatrixSDCellsRollovers_Type()
)
atmMatrixSDCellsRollovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMatrixSDCellsRollovers.setStatus("current")
_AtmMatrixSDHCCells_Type = Counter64
_AtmMatrixSDHCCells_Object = MibTableColumn
atmMatrixSDHCCells = _AtmMatrixSDHCCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 2, 1, 7),
    _AtmMatrixSDHCCells_Type()
)
atmMatrixSDHCCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMatrixSDHCCells.setStatus("current")
_AtmMatrixSDNumCallAttempts_Type = ZeroBasedCounter32
_AtmMatrixSDNumCallAttempts_Object = MibTableColumn
atmMatrixSDNumCallAttempts = _AtmMatrixSDNumCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 2, 1, 8),
    _AtmMatrixSDNumCallAttempts_Type()
)
atmMatrixSDNumCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMatrixSDNumCallAttempts.setStatus("current")
_AtmMatrixSDNumCalls_Type = ZeroBasedCounter32
_AtmMatrixSDNumCalls_Object = MibTableColumn
atmMatrixSDNumCalls = _AtmMatrixSDNumCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 2, 1, 9),
    _AtmMatrixSDNumCalls_Type()
)
atmMatrixSDNumCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMatrixSDNumCalls.setStatus("current")
_AtmMatrixSDConnTime_Type = ConnectTime
_AtmMatrixSDConnTime_Object = MibTableColumn
atmMatrixSDConnTime = _AtmMatrixSDConnTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 2, 1, 10),
    _AtmMatrixSDConnTime_Type()
)
atmMatrixSDConnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMatrixSDConnTime.setStatus("current")
if mibBuilder.loadTexts:
    atmMatrixSDConnTime.setUnits("seconds")
_AtmMatrixDSTable_Object = MibTable
atmMatrixDSTable = _AtmMatrixDSTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 3)
)
if mibBuilder.loadTexts:
    atmMatrixDSTable.setStatus("current")
_AtmMatrixDSEntry_Object = MibTableRow
atmMatrixDSEntry = _AtmMatrixDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 3, 1)
)
atmMatrixDSEntry.setIndexNames(
    (0, "ATM-RMON-MIB", "portSelGrpIndex"),
    (0, "ATM-RMON-MIB", "atmMatrixDSDstAddress"),
    (0, "ATM-RMON-MIB", "atmMatrixDSSrcAddress"),
    (0, "ATM-RMON-MIB", "atmMatrixDSSClass"),
)
if mibBuilder.loadTexts:
    atmMatrixDSEntry.setStatus("current")
_AtmMatrixDSSrcAddress_Type = AtmAddr
_AtmMatrixDSSrcAddress_Object = MibTableColumn
atmMatrixDSSrcAddress = _AtmMatrixDSSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 3, 1, 1),
    _AtmMatrixDSSrcAddress_Type()
)
atmMatrixDSSrcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmMatrixDSSrcAddress.setStatus("current")
_AtmMatrixDSDstAddress_Type = AtmAddr
_AtmMatrixDSDstAddress_Object = MibTableColumn
atmMatrixDSDstAddress = _AtmMatrixDSDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 3, 1, 2),
    _AtmMatrixDSDstAddress_Type()
)
atmMatrixDSDstAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmMatrixDSDstAddress.setStatus("current")
_AtmMatrixDSSClass_Type = ServiceClass
_AtmMatrixDSSClass_Object = MibTableColumn
atmMatrixDSSClass = _AtmMatrixDSSClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 3, 1, 3),
    _AtmMatrixDSSClass_Type()
)
atmMatrixDSSClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmMatrixDSSClass.setStatus("current")
_AtmMatrixDSCreateTime_Type = LastCreateTime
_AtmMatrixDSCreateTime_Object = MibTableColumn
atmMatrixDSCreateTime = _AtmMatrixDSCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 3, 1, 4),
    _AtmMatrixDSCreateTime_Type()
)
atmMatrixDSCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMatrixDSCreateTime.setStatus("current")
_AtmMatrixDSCells_Type = ZeroBasedCounter32
_AtmMatrixDSCells_Object = MibTableColumn
atmMatrixDSCells = _AtmMatrixDSCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 3, 1, 5),
    _AtmMatrixDSCells_Type()
)
atmMatrixDSCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMatrixDSCells.setStatus("current")
_AtmMatrixDSCellsRollovers_Type = ZeroBasedCounter32
_AtmMatrixDSCellsRollovers_Object = MibTableColumn
atmMatrixDSCellsRollovers = _AtmMatrixDSCellsRollovers_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 3, 1, 6),
    _AtmMatrixDSCellsRollovers_Type()
)
atmMatrixDSCellsRollovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMatrixDSCellsRollovers.setStatus("current")
_AtmMatrixDSHCCells_Type = Counter64
_AtmMatrixDSHCCells_Object = MibTableColumn
atmMatrixDSHCCells = _AtmMatrixDSHCCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 3, 1, 7),
    _AtmMatrixDSHCCells_Type()
)
atmMatrixDSHCCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMatrixDSHCCells.setStatus("current")
_AtmMatrixDSNumCallAttempts_Type = ZeroBasedCounter32
_AtmMatrixDSNumCallAttempts_Object = MibTableColumn
atmMatrixDSNumCallAttempts = _AtmMatrixDSNumCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 3, 1, 8),
    _AtmMatrixDSNumCallAttempts_Type()
)
atmMatrixDSNumCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMatrixDSNumCallAttempts.setStatus("current")
_AtmMatrixDSNumCalls_Type = ZeroBasedCounter32
_AtmMatrixDSNumCalls_Object = MibTableColumn
atmMatrixDSNumCalls = _AtmMatrixDSNumCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 3, 1, 9),
    _AtmMatrixDSNumCalls_Type()
)
atmMatrixDSNumCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMatrixDSNumCalls.setStatus("current")
_AtmMatrixDSConnTime_Type = ConnectTime
_AtmMatrixDSConnTime_Object = MibTableColumn
atmMatrixDSConnTime = _AtmMatrixDSConnTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 3, 1, 10),
    _AtmMatrixDSConnTime_Type()
)
atmMatrixDSConnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMatrixDSConnTime.setStatus("current")
if mibBuilder.loadTexts:
    atmMatrixDSConnTime.setUnits("seconds")
_AtmMatrixTopNControlTable_Object = MibTable
atmMatrixTopNControlTable = _AtmMatrixTopNControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 4)
)
if mibBuilder.loadTexts:
    atmMatrixTopNControlTable.setStatus("current")
_AtmMatrixTopNControlEntry_Object = MibTableRow
atmMatrixTopNControlEntry = _AtmMatrixTopNControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 4, 1)
)
atmMatrixTopNControlEntry.setIndexNames(
    (0, "ATM-RMON-MIB", "portSelGrpIndex"),
    (0, "ATM-RMON-MIB", "atmMatrixTopNControlIndex"),
)
if mibBuilder.loadTexts:
    atmMatrixTopNControlEntry.setStatus("current")


class _AtmMatrixTopNControlIndex_Type(Integer32):
    """Custom type atmMatrixTopNControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtmMatrixTopNControlIndex_Type.__name__ = "Integer32"
_AtmMatrixTopNControlIndex_Object = MibTableColumn
atmMatrixTopNControlIndex = _AtmMatrixTopNControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 4, 1, 1),
    _AtmMatrixTopNControlIndex_Type()
)
atmMatrixTopNControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmMatrixTopNControlIndex.setStatus("current")


class _AtmMatrixTopNControlRateBase_Type(Integer32):
    """Custom type atmMatrixTopNControlRateBase based on Integer32"""
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
        *(("atmMatrixTopNCells", 1),
          ("atmMatrixTopNConnTime", 4),
          ("atmMatrixTopNNumCallAttempts", 2),
          ("atmMatrixTopNNumCalls", 3))
    )


_AtmMatrixTopNControlRateBase_Type.__name__ = "Integer32"
_AtmMatrixTopNControlRateBase_Object = MibTableColumn
atmMatrixTopNControlRateBase = _AtmMatrixTopNControlRateBase_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 4, 1, 2),
    _AtmMatrixTopNControlRateBase_Type()
)
atmMatrixTopNControlRateBase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmMatrixTopNControlRateBase.setStatus("current")
_AtmMatrixTopNControlSClass_Type = ServiceClass
_AtmMatrixTopNControlSClass_Object = MibTableColumn
atmMatrixTopNControlSClass = _AtmMatrixTopNControlSClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 4, 1, 3),
    _AtmMatrixTopNControlSClass_Type()
)
atmMatrixTopNControlSClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmMatrixTopNControlSClass.setStatus("current")


class _AtmMatrixTopNControlTimeRemaining_Type(Integer32):
    """Custom type atmMatrixTopNControlTimeRemaining based on Integer32"""
    defaultValue = 1800


_AtmMatrixTopNControlTimeRemaining_Object = MibTableColumn
atmMatrixTopNControlTimeRemaining = _AtmMatrixTopNControlTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 4, 1, 4),
    _AtmMatrixTopNControlTimeRemaining_Type()
)
atmMatrixTopNControlTimeRemaining.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmMatrixTopNControlTimeRemaining.setStatus("current")
_AtmMatrixTopNControlGeneratedReports_Type = Counter32
_AtmMatrixTopNControlGeneratedReports_Object = MibTableColumn
atmMatrixTopNControlGeneratedReports = _AtmMatrixTopNControlGeneratedReports_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 4, 1, 5),
    _AtmMatrixTopNControlGeneratedReports_Type()
)
atmMatrixTopNControlGeneratedReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMatrixTopNControlGeneratedReports.setStatus("current")
_AtmMatrixTopNControlDuration_Type = Integer32
_AtmMatrixTopNControlDuration_Object = MibTableColumn
atmMatrixTopNControlDuration = _AtmMatrixTopNControlDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 4, 1, 6),
    _AtmMatrixTopNControlDuration_Type()
)
atmMatrixTopNControlDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMatrixTopNControlDuration.setStatus("current")


class _AtmMatrixTopNControlRequestedSize_Type(Integer32):
    """Custom type atmMatrixTopNControlRequestedSize based on Integer32"""
    defaultValue = 150


_AtmMatrixTopNControlRequestedSize_Object = MibTableColumn
atmMatrixTopNControlRequestedSize = _AtmMatrixTopNControlRequestedSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 4, 1, 7),
    _AtmMatrixTopNControlRequestedSize_Type()
)
atmMatrixTopNControlRequestedSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmMatrixTopNControlRequestedSize.setStatus("current")
_AtmMatrixTopNControlGrantedSize_Type = Integer32
_AtmMatrixTopNControlGrantedSize_Object = MibTableColumn
atmMatrixTopNControlGrantedSize = _AtmMatrixTopNControlGrantedSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 4, 1, 8),
    _AtmMatrixTopNControlGrantedSize_Type()
)
atmMatrixTopNControlGrantedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMatrixTopNControlGrantedSize.setStatus("current")
_AtmMatrixTopNControlStartTime_Type = TimeStamp
_AtmMatrixTopNControlStartTime_Object = MibTableColumn
atmMatrixTopNControlStartTime = _AtmMatrixTopNControlStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 4, 1, 9),
    _AtmMatrixTopNControlStartTime_Type()
)
atmMatrixTopNControlStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMatrixTopNControlStartTime.setStatus("current")
_AtmMatrixTopNControlOwner_Type = OwnerString
_AtmMatrixTopNControlOwner_Object = MibTableColumn
atmMatrixTopNControlOwner = _AtmMatrixTopNControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 4, 1, 10),
    _AtmMatrixTopNControlOwner_Type()
)
atmMatrixTopNControlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmMatrixTopNControlOwner.setStatus("current")
_AtmMatrixTopNControlStatus_Type = RowStatus
_AtmMatrixTopNControlStatus_Object = MibTableColumn
atmMatrixTopNControlStatus = _AtmMatrixTopNControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 4, 1, 11),
    _AtmMatrixTopNControlStatus_Type()
)
atmMatrixTopNControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmMatrixTopNControlStatus.setStatus("current")
_AtmMatrixTopNTable_Object = MibTable
atmMatrixTopNTable = _AtmMatrixTopNTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 5)
)
if mibBuilder.loadTexts:
    atmMatrixTopNTable.setStatus("current")
_AtmMatrixTopNEntry_Object = MibTableRow
atmMatrixTopNEntry = _AtmMatrixTopNEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 5, 1)
)
atmMatrixTopNEntry.setIndexNames(
    (0, "ATM-RMON-MIB", "portSelGrpIndex"),
    (0, "ATM-RMON-MIB", "atmMatrixTopNControlIndex"),
    (0, "ATM-RMON-MIB", "atmMatrixTopNIndex"),
)
if mibBuilder.loadTexts:
    atmMatrixTopNEntry.setStatus("current")


class _AtmMatrixTopNIndex_Type(Integer32):
    """Custom type atmMatrixTopNIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtmMatrixTopNIndex_Type.__name__ = "Integer32"
_AtmMatrixTopNIndex_Object = MibTableColumn
atmMatrixTopNIndex = _AtmMatrixTopNIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 5, 1, 1),
    _AtmMatrixTopNIndex_Type()
)
atmMatrixTopNIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmMatrixTopNIndex.setStatus("current")
_AtmMatrixTopNSrcAddress_Type = AtmAddr
_AtmMatrixTopNSrcAddress_Object = MibTableColumn
atmMatrixTopNSrcAddress = _AtmMatrixTopNSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 5, 1, 2),
    _AtmMatrixTopNSrcAddress_Type()
)
atmMatrixTopNSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMatrixTopNSrcAddress.setStatus("current")
_AtmMatrixTopNDstAddress_Type = AtmAddr
_AtmMatrixTopNDstAddress_Object = MibTableColumn
atmMatrixTopNDstAddress = _AtmMatrixTopNDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 5, 1, 3),
    _AtmMatrixTopNDstAddress_Type()
)
atmMatrixTopNDstAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMatrixTopNDstAddress.setStatus("current")
_AtmMatrixTopNRate_Type = Integer32
_AtmMatrixTopNRate_Object = MibTableColumn
atmMatrixTopNRate = _AtmMatrixTopNRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 5, 1, 4),
    _AtmMatrixTopNRate_Type()
)
atmMatrixTopNRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMatrixTopNRate.setStatus("current")
_AtmMatrixTopNReverseRate_Type = Integer32
_AtmMatrixTopNReverseRate_Object = MibTableColumn
atmMatrixTopNReverseRate = _AtmMatrixTopNReverseRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 4, 5, 1, 5),
    _AtmMatrixTopNReverseRate_Type()
)
atmMatrixTopNReverseRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMatrixTopNReverseRate.setStatus("current")
_AtmConfig_ObjectIdentity = ObjectIdentity
atmConfig = _AtmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 5)
)


class _AtmRmonDataCollectMode_Type(Integer32):
    """Custom type atmRmonDataCollectMode based on Integer32"""
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


_AtmRmonDataCollectMode_Type.__name__ = "Integer32"
_AtmRmonDataCollectMode_Object = MibScalar
atmRmonDataCollectMode = _AtmRmonDataCollectMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 1, 5, 1),
    _AtmRmonDataCollectMode_Type()
)
atmRmonDataCollectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmRmonDataCollectMode.setStatus("current")
_AtmRmonNotifications_ObjectIdentity = ObjectIdentity
atmRmonNotifications = _AtmRmonNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 2)
)
_AtmRmonConformance_ObjectIdentity = ObjectIdentity
atmRmonConformance = _AtmRmonConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 3)
)
_AtmRmonMIBCompliances_ObjectIdentity = ObjectIdentity
atmRmonMIBCompliances = _AtmRmonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 3, 1)
)
_AtmRmonMIBGroups_ObjectIdentity = ObjectIdentity
atmRmonMIBGroups = _AtmRmonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 3, 2)
)

# Managed Objects groups

portSelectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 3, 2, 1)
)
portSelectGroup.setObjects(
      *(("ATM-RMON-MIB", "portSelGrpDescr"),
        ("ATM-RMON-MIB", "portSelGrpCreateTime"),
        ("ATM-RMON-MIB", "portSelGrpOwner"),
        ("ATM-RMON-MIB", "portSelGrpStatus"),
        ("ATM-RMON-MIB", "portSelCollectGroup"),
        ("ATM-RMON-MIB", "portSelCreateTime"),
        ("ATM-RMON-MIB", "portSelOwner"),
        ("ATM-RMON-MIB", "portSelStatus"))
)
if mibBuilder.loadTexts:
    portSelectGroup.setStatus("current")

atmStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 3, 2, 2)
)
atmStatsGroup.setObjects(
      *(("ATM-RMON-MIB", "atmStatsControlDropEvents"),
        ("ATM-RMON-MIB", "atmStatsControlOwner"),
        ("ATM-RMON-MIB", "atmStatsControlStatus"),
        ("ATM-RMON-MIB", "atmStatsCreateTime"),
        ("ATM-RMON-MIB", "atmStatsCells"),
        ("ATM-RMON-MIB", "atmStatsCellsRollovers"),
        ("ATM-RMON-MIB", "atmStatsNumCallAttempts"),
        ("ATM-RMON-MIB", "atmStatsNumCalls"),
        ("ATM-RMON-MIB", "atmStatsConnTime"))
)
if mibBuilder.loadTexts:
    atmStatsGroup.setStatus("current")

atmStatsHCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 3, 2, 3)
)
atmStatsHCGroup.setObjects(
    ("ATM-RMON-MIB", "atmStatsHCCells")
)
if mibBuilder.loadTexts:
    atmStatsHCGroup.setStatus("current")

atmHostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 3, 2, 4)
)
atmHostGroup.setObjects(
      *(("ATM-RMON-MIB", "atmHostControlInserts"),
        ("ATM-RMON-MIB", "atmHostControlDeletes"),
        ("ATM-RMON-MIB", "atmHostControlMaxDesiredEntries"),
        ("ATM-RMON-MIB", "atmHostControlPriority"),
        ("ATM-RMON-MIB", "atmHostControlAddrCollectScope"),
        ("ATM-RMON-MIB", "atmHostControlDropEvents"),
        ("ATM-RMON-MIB", "atmHostControlOwner"),
        ("ATM-RMON-MIB", "atmHostControlStatus"),
        ("ATM-RMON-MIB", "atmHostCreateTime"),
        ("ATM-RMON-MIB", "atmHostInCells"),
        ("ATM-RMON-MIB", "atmHostInCellsRollovers"),
        ("ATM-RMON-MIB", "atmHostOutCells"),
        ("ATM-RMON-MIB", "atmHostOutCellsRollovers"),
        ("ATM-RMON-MIB", "atmHostInNumCallAttempts"),
        ("ATM-RMON-MIB", "atmHostInNumCalls"),
        ("ATM-RMON-MIB", "atmHostOutNumCallAttempts"),
        ("ATM-RMON-MIB", "atmHostOutNumCalls"),
        ("ATM-RMON-MIB", "atmHostInConnTime"),
        ("ATM-RMON-MIB", "atmHostOutConnTime"))
)
if mibBuilder.loadTexts:
    atmHostGroup.setStatus("current")

atmHostHCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 3, 2, 5)
)
atmHostHCGroup.setObjects(
      *(("ATM-RMON-MIB", "atmHostInHCCells"),
        ("ATM-RMON-MIB", "atmHostOutHCCells"))
)
if mibBuilder.loadTexts:
    atmHostHCGroup.setStatus("current")

atmMatrixGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 3, 2, 6)
)
atmMatrixGroup.setObjects(
      *(("ATM-RMON-MIB", "atmMatrixControlInserts"),
        ("ATM-RMON-MIB", "atmMatrixControlDeletes"),
        ("ATM-RMON-MIB", "atmMatrixControlMaxDesiredEntries"),
        ("ATM-RMON-MIB", "atmMatrixControlPriority"),
        ("ATM-RMON-MIB", "atmMatrixControlAddrCollectScope"),
        ("ATM-RMON-MIB", "atmMatrixControlDropEvents"),
        ("ATM-RMON-MIB", "atmMatrixControlOwner"),
        ("ATM-RMON-MIB", "atmMatrixControlStatus"),
        ("ATM-RMON-MIB", "atmMatrixSDCreateTime"),
        ("ATM-RMON-MIB", "atmMatrixSDCells"),
        ("ATM-RMON-MIB", "atmMatrixSDCellsRollovers"),
        ("ATM-RMON-MIB", "atmMatrixSDNumCallAttempts"),
        ("ATM-RMON-MIB", "atmMatrixSDNumCalls"),
        ("ATM-RMON-MIB", "atmMatrixSDConnTime"),
        ("ATM-RMON-MIB", "atmMatrixDSCreateTime"),
        ("ATM-RMON-MIB", "atmMatrixDSCells"),
        ("ATM-RMON-MIB", "atmMatrixDSCellsRollovers"),
        ("ATM-RMON-MIB", "atmMatrixDSNumCallAttempts"),
        ("ATM-RMON-MIB", "atmMatrixDSNumCalls"),
        ("ATM-RMON-MIB", "atmMatrixDSConnTime"),
        ("ATM-RMON-MIB", "atmMatrixTopNControlRateBase"),
        ("ATM-RMON-MIB", "atmMatrixTopNControlSClass"),
        ("ATM-RMON-MIB", "atmMatrixTopNControlTimeRemaining"),
        ("ATM-RMON-MIB", "atmMatrixTopNControlGeneratedReports"),
        ("ATM-RMON-MIB", "atmMatrixTopNControlDuration"),
        ("ATM-RMON-MIB", "atmMatrixTopNControlRequestedSize"),
        ("ATM-RMON-MIB", "atmMatrixTopNControlGrantedSize"),
        ("ATM-RMON-MIB", "atmMatrixTopNControlStartTime"),
        ("ATM-RMON-MIB", "atmMatrixTopNControlOwner"),
        ("ATM-RMON-MIB", "atmMatrixTopNControlStatus"),
        ("ATM-RMON-MIB", "atmMatrixTopNSrcAddress"),
        ("ATM-RMON-MIB", "atmMatrixTopNDstAddress"),
        ("ATM-RMON-MIB", "atmMatrixTopNRate"),
        ("ATM-RMON-MIB", "atmMatrixTopNReverseRate"))
)
if mibBuilder.loadTexts:
    atmMatrixGroup.setStatus("current")

atmMatrixHCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 3, 2, 7)
)
atmMatrixHCGroup.setObjects(
      *(("ATM-RMON-MIB", "atmMatrixSDHCCells"),
        ("ATM-RMON-MIB", "atmMatrixDSHCCells"))
)
if mibBuilder.loadTexts:
    atmMatrixHCGroup.setStatus("current")

atmConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 3, 2, 8)
)
atmConfigGroup.setObjects(
    ("ATM-RMON-MIB", "atmRmonDataCollectMode")
)
if mibBuilder.loadTexts:
    atmConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

atmRmonMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 16, 3, 1, 1)
)
if mibBuilder.loadTexts:
    atmRmonMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATM-RMON-MIB",
    **{"ZeroBasedCounter32": ZeroBasedCounter32,
       "LastCreateTime": LastCreateTime,
       "AtmAddr": AtmAddr,
       "ServiceClass": ServiceClass,
       "ResourcePriority": ResourcePriority,
       "AddressCollectScope": AddressCollectScope,
       "ConnectTime": ConnectTime,
       "atmRmon": atmRmon,
       "atmRmonMIBObjects": atmRmonMIBObjects,
       "portSelect": portSelect,
       "portSelGrpTable": portSelGrpTable,
       "portSelGrpEntry": portSelGrpEntry,
       "portSelGrpIndex": portSelGrpIndex,
       "portSelGrpDescr": portSelGrpDescr,
       "portSelGrpCreateTime": portSelGrpCreateTime,
       "portSelGrpOwner": portSelGrpOwner,
       "portSelGrpStatus": portSelGrpStatus,
       "portSelTable": portSelTable,
       "portSelEntry": portSelEntry,
       "portSelCollectGroup": portSelCollectGroup,
       "portSelCreateTime": portSelCreateTime,
       "portSelOwner": portSelOwner,
       "portSelStatus": portSelStatus,
       "atmStats": atmStats,
       "atmStatsControlTable": atmStatsControlTable,
       "atmStatsControlEntry": atmStatsControlEntry,
       "atmStatsControlDropEvents": atmStatsControlDropEvents,
       "atmStatsControlOwner": atmStatsControlOwner,
       "atmStatsControlStatus": atmStatsControlStatus,
       "atmStatsTable": atmStatsTable,
       "atmStatsEntry": atmStatsEntry,
       "atmStatsSClass": atmStatsSClass,
       "atmStatsCreateTime": atmStatsCreateTime,
       "atmStatsCells": atmStatsCells,
       "atmStatsCellsRollovers": atmStatsCellsRollovers,
       "atmStatsHCCells": atmStatsHCCells,
       "atmStatsNumCallAttempts": atmStatsNumCallAttempts,
       "atmStatsNumCalls": atmStatsNumCalls,
       "atmStatsConnTime": atmStatsConnTime,
       "atmHost": atmHost,
       "atmHostControlTable": atmHostControlTable,
       "atmHostControlEntry": atmHostControlEntry,
       "atmHostControlInserts": atmHostControlInserts,
       "atmHostControlDeletes": atmHostControlDeletes,
       "atmHostControlMaxDesiredEntries": atmHostControlMaxDesiredEntries,
       "atmHostControlPriority": atmHostControlPriority,
       "atmHostControlAddrCollectScope": atmHostControlAddrCollectScope,
       "atmHostControlDropEvents": atmHostControlDropEvents,
       "atmHostControlOwner": atmHostControlOwner,
       "atmHostControlStatus": atmHostControlStatus,
       "atmHostTable": atmHostTable,
       "atmHostEntry": atmHostEntry,
       "atmHostAddress": atmHostAddress,
       "atmHostSClass": atmHostSClass,
       "atmHostCreateTime": atmHostCreateTime,
       "atmHostInCells": atmHostInCells,
       "atmHostInCellsRollovers": atmHostInCellsRollovers,
       "atmHostInHCCells": atmHostInHCCells,
       "atmHostOutCells": atmHostOutCells,
       "atmHostOutCellsRollovers": atmHostOutCellsRollovers,
       "atmHostOutHCCells": atmHostOutHCCells,
       "atmHostInNumCallAttempts": atmHostInNumCallAttempts,
       "atmHostInNumCalls": atmHostInNumCalls,
       "atmHostOutNumCallAttempts": atmHostOutNumCallAttempts,
       "atmHostOutNumCalls": atmHostOutNumCalls,
       "atmHostInConnTime": atmHostInConnTime,
       "atmHostOutConnTime": atmHostOutConnTime,
       "atmMatrix": atmMatrix,
       "atmMatrixControlTable": atmMatrixControlTable,
       "atmMatrixControlEntry": atmMatrixControlEntry,
       "atmMatrixControlInserts": atmMatrixControlInserts,
       "atmMatrixControlDeletes": atmMatrixControlDeletes,
       "atmMatrixControlMaxDesiredEntries": atmMatrixControlMaxDesiredEntries,
       "atmMatrixControlPriority": atmMatrixControlPriority,
       "atmMatrixControlAddrCollectScope": atmMatrixControlAddrCollectScope,
       "atmMatrixControlDropEvents": atmMatrixControlDropEvents,
       "atmMatrixControlOwner": atmMatrixControlOwner,
       "atmMatrixControlStatus": atmMatrixControlStatus,
       "atmMatrixSDTable": atmMatrixSDTable,
       "atmMatrixSDEntry": atmMatrixSDEntry,
       "atmMatrixSDSrcAddress": atmMatrixSDSrcAddress,
       "atmMatrixSDDstAddress": atmMatrixSDDstAddress,
       "atmMatrixSDSClass": atmMatrixSDSClass,
       "atmMatrixSDCreateTime": atmMatrixSDCreateTime,
       "atmMatrixSDCells": atmMatrixSDCells,
       "atmMatrixSDCellsRollovers": atmMatrixSDCellsRollovers,
       "atmMatrixSDHCCells": atmMatrixSDHCCells,
       "atmMatrixSDNumCallAttempts": atmMatrixSDNumCallAttempts,
       "atmMatrixSDNumCalls": atmMatrixSDNumCalls,
       "atmMatrixSDConnTime": atmMatrixSDConnTime,
       "atmMatrixDSTable": atmMatrixDSTable,
       "atmMatrixDSEntry": atmMatrixDSEntry,
       "atmMatrixDSSrcAddress": atmMatrixDSSrcAddress,
       "atmMatrixDSDstAddress": atmMatrixDSDstAddress,
       "atmMatrixDSSClass": atmMatrixDSSClass,
       "atmMatrixDSCreateTime": atmMatrixDSCreateTime,
       "atmMatrixDSCells": atmMatrixDSCells,
       "atmMatrixDSCellsRollovers": atmMatrixDSCellsRollovers,
       "atmMatrixDSHCCells": atmMatrixDSHCCells,
       "atmMatrixDSNumCallAttempts": atmMatrixDSNumCallAttempts,
       "atmMatrixDSNumCalls": atmMatrixDSNumCalls,
       "atmMatrixDSConnTime": atmMatrixDSConnTime,
       "atmMatrixTopNControlTable": atmMatrixTopNControlTable,
       "atmMatrixTopNControlEntry": atmMatrixTopNControlEntry,
       "atmMatrixTopNControlIndex": atmMatrixTopNControlIndex,
       "atmMatrixTopNControlRateBase": atmMatrixTopNControlRateBase,
       "atmMatrixTopNControlSClass": atmMatrixTopNControlSClass,
       "atmMatrixTopNControlTimeRemaining": atmMatrixTopNControlTimeRemaining,
       "atmMatrixTopNControlGeneratedReports": atmMatrixTopNControlGeneratedReports,
       "atmMatrixTopNControlDuration": atmMatrixTopNControlDuration,
       "atmMatrixTopNControlRequestedSize": atmMatrixTopNControlRequestedSize,
       "atmMatrixTopNControlGrantedSize": atmMatrixTopNControlGrantedSize,
       "atmMatrixTopNControlStartTime": atmMatrixTopNControlStartTime,
       "atmMatrixTopNControlOwner": atmMatrixTopNControlOwner,
       "atmMatrixTopNControlStatus": atmMatrixTopNControlStatus,
       "atmMatrixTopNTable": atmMatrixTopNTable,
       "atmMatrixTopNEntry": atmMatrixTopNEntry,
       "atmMatrixTopNIndex": atmMatrixTopNIndex,
       "atmMatrixTopNSrcAddress": atmMatrixTopNSrcAddress,
       "atmMatrixTopNDstAddress": atmMatrixTopNDstAddress,
       "atmMatrixTopNRate": atmMatrixTopNRate,
       "atmMatrixTopNReverseRate": atmMatrixTopNReverseRate,
       "atmConfig": atmConfig,
       "atmRmonDataCollectMode": atmRmonDataCollectMode,
       "atmRmonNotifications": atmRmonNotifications,
       "atmRmonConformance": atmRmonConformance,
       "atmRmonMIBCompliances": atmRmonMIBCompliances,
       "atmRmonMIBCompliance": atmRmonMIBCompliance,
       "atmRmonMIBGroups": atmRmonMIBGroups,
       "portSelectGroup": portSelectGroup,
       "atmStatsGroup": atmStatsGroup,
       "atmStatsHCGroup": atmStatsHCGroup,
       "atmHostGroup": atmHostGroup,
       "atmHostHCGroup": atmHostHCGroup,
       "atmMatrixGroup": atmMatrixGroup,
       "atmMatrixHCGroup": atmMatrixHCGroup,
       "atmConfigGroup": atmConfigGroup}
)
