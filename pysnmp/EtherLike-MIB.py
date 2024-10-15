# SNMP MIB module (ETHERLIKE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EtherLike-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:59 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
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
 iso,
 mib_2,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2",
    "transmission")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

etherMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 35)
)
etherMIB.setRevisions(
        ("1999-08-24 04:00",
         "1998-06-03 21:50",
         "1994-02-03 04:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dot3_ObjectIdentity = ObjectIdentity
dot3 = _Dot3_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7)
)
_Dot3StatsTable_Object = MibTable
dot3StatsTable = _Dot3StatsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2)
)
if mibBuilder.loadTexts:
    dot3StatsTable.setStatus("current")
_Dot3StatsEntry_Object = MibTableRow
dot3StatsEntry = _Dot3StatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1)
)
dot3StatsEntry.setIndexNames(
    (0, "ETHERLIKE-MIB", "dot3StatsIndex"),
)
if mibBuilder.loadTexts:
    dot3StatsEntry.setStatus("current")
_Dot3StatsIndex_Type = InterfaceIndex
_Dot3StatsIndex_Object = MibTableColumn
dot3StatsIndex = _Dot3StatsIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 1),
    _Dot3StatsIndex_Type()
)
dot3StatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsIndex.setStatus("current")
_Dot3StatsAlignmentErrors_Type = Counter32
_Dot3StatsAlignmentErrors_Object = MibTableColumn
dot3StatsAlignmentErrors = _Dot3StatsAlignmentErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 2),
    _Dot3StatsAlignmentErrors_Type()
)
dot3StatsAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsAlignmentErrors.setStatus("current")
_Dot3StatsFCSErrors_Type = Counter32
_Dot3StatsFCSErrors_Object = MibTableColumn
dot3StatsFCSErrors = _Dot3StatsFCSErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 3),
    _Dot3StatsFCSErrors_Type()
)
dot3StatsFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsFCSErrors.setStatus("current")
_Dot3StatsSingleCollisionFrames_Type = Counter32
_Dot3StatsSingleCollisionFrames_Object = MibTableColumn
dot3StatsSingleCollisionFrames = _Dot3StatsSingleCollisionFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 4),
    _Dot3StatsSingleCollisionFrames_Type()
)
dot3StatsSingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsSingleCollisionFrames.setStatus("current")
_Dot3StatsMultipleCollisionFrames_Type = Counter32
_Dot3StatsMultipleCollisionFrames_Object = MibTableColumn
dot3StatsMultipleCollisionFrames = _Dot3StatsMultipleCollisionFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 5),
    _Dot3StatsMultipleCollisionFrames_Type()
)
dot3StatsMultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsMultipleCollisionFrames.setStatus("current")
_Dot3StatsSQETestErrors_Type = Counter32
_Dot3StatsSQETestErrors_Object = MibTableColumn
dot3StatsSQETestErrors = _Dot3StatsSQETestErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 6),
    _Dot3StatsSQETestErrors_Type()
)
dot3StatsSQETestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsSQETestErrors.setStatus("current")
_Dot3StatsDeferredTransmissions_Type = Counter32
_Dot3StatsDeferredTransmissions_Object = MibTableColumn
dot3StatsDeferredTransmissions = _Dot3StatsDeferredTransmissions_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 7),
    _Dot3StatsDeferredTransmissions_Type()
)
dot3StatsDeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsDeferredTransmissions.setStatus("current")
_Dot3StatsLateCollisions_Type = Counter32
_Dot3StatsLateCollisions_Object = MibTableColumn
dot3StatsLateCollisions = _Dot3StatsLateCollisions_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 8),
    _Dot3StatsLateCollisions_Type()
)
dot3StatsLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsLateCollisions.setStatus("current")
_Dot3StatsExcessiveCollisions_Type = Counter32
_Dot3StatsExcessiveCollisions_Object = MibTableColumn
dot3StatsExcessiveCollisions = _Dot3StatsExcessiveCollisions_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 9),
    _Dot3StatsExcessiveCollisions_Type()
)
dot3StatsExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsExcessiveCollisions.setStatus("current")
_Dot3StatsInternalMacTransmitErrors_Type = Counter32
_Dot3StatsInternalMacTransmitErrors_Object = MibTableColumn
dot3StatsInternalMacTransmitErrors = _Dot3StatsInternalMacTransmitErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 10),
    _Dot3StatsInternalMacTransmitErrors_Type()
)
dot3StatsInternalMacTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsInternalMacTransmitErrors.setStatus("current")
_Dot3StatsCarrierSenseErrors_Type = Counter32
_Dot3StatsCarrierSenseErrors_Object = MibTableColumn
dot3StatsCarrierSenseErrors = _Dot3StatsCarrierSenseErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 11),
    _Dot3StatsCarrierSenseErrors_Type()
)
dot3StatsCarrierSenseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsCarrierSenseErrors.setStatus("current")
_Dot3StatsFrameTooLongs_Type = Counter32
_Dot3StatsFrameTooLongs_Object = MibTableColumn
dot3StatsFrameTooLongs = _Dot3StatsFrameTooLongs_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 13),
    _Dot3StatsFrameTooLongs_Type()
)
dot3StatsFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsFrameTooLongs.setStatus("current")
_Dot3StatsInternalMacReceiveErrors_Type = Counter32
_Dot3StatsInternalMacReceiveErrors_Object = MibTableColumn
dot3StatsInternalMacReceiveErrors = _Dot3StatsInternalMacReceiveErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 16),
    _Dot3StatsInternalMacReceiveErrors_Type()
)
dot3StatsInternalMacReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsInternalMacReceiveErrors.setStatus("current")
_Dot3StatsEtherChipSet_Type = ObjectIdentifier
_Dot3StatsEtherChipSet_Object = MibTableColumn
dot3StatsEtherChipSet = _Dot3StatsEtherChipSet_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 17),
    _Dot3StatsEtherChipSet_Type()
)
dot3StatsEtherChipSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsEtherChipSet.setStatus("deprecated")
_Dot3StatsSymbolErrors_Type = Counter32
_Dot3StatsSymbolErrors_Object = MibTableColumn
dot3StatsSymbolErrors = _Dot3StatsSymbolErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 18),
    _Dot3StatsSymbolErrors_Type()
)
dot3StatsSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsSymbolErrors.setStatus("current")


class _Dot3StatsDuplexStatus_Type(Integer32):
    """Custom type dot3StatsDuplexStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 3),
          ("halfDuplex", 2),
          ("unknown", 1))
    )


_Dot3StatsDuplexStatus_Type.__name__ = "Integer32"
_Dot3StatsDuplexStatus_Object = MibTableColumn
dot3StatsDuplexStatus = _Dot3StatsDuplexStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 19),
    _Dot3StatsDuplexStatus_Type()
)
dot3StatsDuplexStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsDuplexStatus.setStatus("current")
_Dot3CollTable_Object = MibTable
dot3CollTable = _Dot3CollTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 5)
)
if mibBuilder.loadTexts:
    dot3CollTable.setStatus("current")
_Dot3CollEntry_Object = MibTableRow
dot3CollEntry = _Dot3CollEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 5, 1)
)
dot3CollEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ETHERLIKE-MIB", "dot3CollCount"),
)
if mibBuilder.loadTexts:
    dot3CollEntry.setStatus("current")


class _Dot3CollCount_Type(Integer32):
    """Custom type dot3CollCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Dot3CollCount_Type.__name__ = "Integer32"
_Dot3CollCount_Object = MibTableColumn
dot3CollCount = _Dot3CollCount_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 5, 1, 2),
    _Dot3CollCount_Type()
)
dot3CollCount.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3CollCount.setStatus("current")
_Dot3CollFrequencies_Type = Counter32
_Dot3CollFrequencies_Object = MibTableColumn
dot3CollFrequencies = _Dot3CollFrequencies_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 5, 1, 3),
    _Dot3CollFrequencies_Type()
)
dot3CollFrequencies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3CollFrequencies.setStatus("current")
_Dot3Tests_ObjectIdentity = ObjectIdentity
dot3Tests = _Dot3Tests_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 6)
)
_Dot3TestTdr_ObjectIdentity = ObjectIdentity
dot3TestTdr = _Dot3TestTdr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 6, 1)
)
if mibBuilder.loadTexts:
    dot3TestTdr.setStatus("current")
_Dot3TestLoopBack_ObjectIdentity = ObjectIdentity
dot3TestLoopBack = _Dot3TestLoopBack_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 6, 2)
)
if mibBuilder.loadTexts:
    dot3TestLoopBack.setStatus("current")
_Dot3Errors_ObjectIdentity = ObjectIdentity
dot3Errors = _Dot3Errors_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 7)
)
_Dot3ErrorInitError_ObjectIdentity = ObjectIdentity
dot3ErrorInitError = _Dot3ErrorInitError_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 7, 1)
)
if mibBuilder.loadTexts:
    dot3ErrorInitError.setStatus("current")
_Dot3ErrorLoopbackError_ObjectIdentity = ObjectIdentity
dot3ErrorLoopbackError = _Dot3ErrorLoopbackError_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 7, 2)
)
if mibBuilder.loadTexts:
    dot3ErrorLoopbackError.setStatus("current")
_Dot3ControlTable_Object = MibTable
dot3ControlTable = _Dot3ControlTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 9)
)
if mibBuilder.loadTexts:
    dot3ControlTable.setStatus("current")
_Dot3ControlEntry_Object = MibTableRow
dot3ControlEntry = _Dot3ControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 9, 1)
)
dot3ControlEntry.setIndexNames(
    (0, "ETHERLIKE-MIB", "dot3StatsIndex"),
)
if mibBuilder.loadTexts:
    dot3ControlEntry.setStatus("current")


class _Dot3ControlFunctionsSupported_Type(Bits):
    """Custom type dot3ControlFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        ("pause", 0)
    )

_Dot3ControlFunctionsSupported_Type.__name__ = "Bits"
_Dot3ControlFunctionsSupported_Object = MibTableColumn
dot3ControlFunctionsSupported = _Dot3ControlFunctionsSupported_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 9, 1, 1),
    _Dot3ControlFunctionsSupported_Type()
)
dot3ControlFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3ControlFunctionsSupported.setStatus("current")
_Dot3ControlInUnknownOpcodes_Type = Counter32
_Dot3ControlInUnknownOpcodes_Object = MibTableColumn
dot3ControlInUnknownOpcodes = _Dot3ControlInUnknownOpcodes_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 9, 1, 2),
    _Dot3ControlInUnknownOpcodes_Type()
)
dot3ControlInUnknownOpcodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3ControlInUnknownOpcodes.setStatus("current")
_Dot3PauseTable_Object = MibTable
dot3PauseTable = _Dot3PauseTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 10)
)
if mibBuilder.loadTexts:
    dot3PauseTable.setStatus("current")
_Dot3PauseEntry_Object = MibTableRow
dot3PauseEntry = _Dot3PauseEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 10, 1)
)
dot3PauseEntry.setIndexNames(
    (0, "ETHERLIKE-MIB", "dot3StatsIndex"),
)
if mibBuilder.loadTexts:
    dot3PauseEntry.setStatus("current")


class _Dot3PauseAdminMode_Type(Integer32):
    """Custom type dot3PauseAdminMode based on Integer32"""
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
        *(("disabled", 1),
          ("enabledRcv", 3),
          ("enabledXmit", 2),
          ("enabledXmitAndRcv", 4))
    )


_Dot3PauseAdminMode_Type.__name__ = "Integer32"
_Dot3PauseAdminMode_Object = MibTableColumn
dot3PauseAdminMode = _Dot3PauseAdminMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 10, 1, 1),
    _Dot3PauseAdminMode_Type()
)
dot3PauseAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3PauseAdminMode.setStatus("current")


class _Dot3PauseOperMode_Type(Integer32):
    """Custom type dot3PauseOperMode based on Integer32"""
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
        *(("disabled", 1),
          ("enabledRcv", 3),
          ("enabledXmit", 2),
          ("enabledXmitAndRcv", 4))
    )


_Dot3PauseOperMode_Type.__name__ = "Integer32"
_Dot3PauseOperMode_Object = MibTableColumn
dot3PauseOperMode = _Dot3PauseOperMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 10, 1, 2),
    _Dot3PauseOperMode_Type()
)
dot3PauseOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3PauseOperMode.setStatus("current")
_Dot3InPauseFrames_Type = Counter32
_Dot3InPauseFrames_Object = MibTableColumn
dot3InPauseFrames = _Dot3InPauseFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 10, 1, 3),
    _Dot3InPauseFrames_Type()
)
dot3InPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3InPauseFrames.setStatus("current")
_Dot3OutPauseFrames_Type = Counter32
_Dot3OutPauseFrames_Object = MibTableColumn
dot3OutPauseFrames = _Dot3OutPauseFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 10, 1, 4),
    _Dot3OutPauseFrames_Type()
)
dot3OutPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OutPauseFrames.setStatus("current")
_EtherMIBObjects_ObjectIdentity = ObjectIdentity
etherMIBObjects = _EtherMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 35, 1)
)
_EtherConformance_ObjectIdentity = ObjectIdentity
etherConformance = _EtherConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 35, 2)
)
_EtherGroups_ObjectIdentity = ObjectIdentity
etherGroups = _EtherGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 35, 2, 1)
)
_EtherCompliances_ObjectIdentity = ObjectIdentity
etherCompliances = _EtherCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 35, 2, 2)
)

# Managed Objects groups

etherStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 1)
)
etherStatsGroup.setObjects(
      *(("ETHERLIKE-MIB", "dot3StatsIndex"),
        ("ETHERLIKE-MIB", "dot3StatsAlignmentErrors"),
        ("ETHERLIKE-MIB", "dot3StatsFCSErrors"),
        ("ETHERLIKE-MIB", "dot3StatsSingleCollisionFrames"),
        ("ETHERLIKE-MIB", "dot3StatsMultipleCollisionFrames"),
        ("ETHERLIKE-MIB", "dot3StatsSQETestErrors"),
        ("ETHERLIKE-MIB", "dot3StatsDeferredTransmissions"),
        ("ETHERLIKE-MIB", "dot3StatsLateCollisions"),
        ("ETHERLIKE-MIB", "dot3StatsExcessiveCollisions"),
        ("ETHERLIKE-MIB", "dot3StatsInternalMacTransmitErrors"),
        ("ETHERLIKE-MIB", "dot3StatsCarrierSenseErrors"),
        ("ETHERLIKE-MIB", "dot3StatsFrameTooLongs"),
        ("ETHERLIKE-MIB", "dot3StatsInternalMacReceiveErrors"),
        ("ETHERLIKE-MIB", "dot3StatsEtherChipSet"))
)
if mibBuilder.loadTexts:
    etherStatsGroup.setStatus("deprecated")

etherCollisionTableGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 2)
)
etherCollisionTableGroup.setObjects(
    ("ETHERLIKE-MIB", "dot3CollFrequencies")
)
if mibBuilder.loadTexts:
    etherCollisionTableGroup.setStatus("current")

etherStats100MbsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 3)
)
etherStats100MbsGroup.setObjects(
      *(("ETHERLIKE-MIB", "dot3StatsIndex"),
        ("ETHERLIKE-MIB", "dot3StatsAlignmentErrors"),
        ("ETHERLIKE-MIB", "dot3StatsFCSErrors"),
        ("ETHERLIKE-MIB", "dot3StatsSingleCollisionFrames"),
        ("ETHERLIKE-MIB", "dot3StatsMultipleCollisionFrames"),
        ("ETHERLIKE-MIB", "dot3StatsDeferredTransmissions"),
        ("ETHERLIKE-MIB", "dot3StatsLateCollisions"),
        ("ETHERLIKE-MIB", "dot3StatsExcessiveCollisions"),
        ("ETHERLIKE-MIB", "dot3StatsInternalMacTransmitErrors"),
        ("ETHERLIKE-MIB", "dot3StatsCarrierSenseErrors"),
        ("ETHERLIKE-MIB", "dot3StatsFrameTooLongs"),
        ("ETHERLIKE-MIB", "dot3StatsInternalMacReceiveErrors"),
        ("ETHERLIKE-MIB", "dot3StatsEtherChipSet"),
        ("ETHERLIKE-MIB", "dot3StatsSymbolErrors"))
)
if mibBuilder.loadTexts:
    etherStats100MbsGroup.setStatus("deprecated")

etherStatsBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 4)
)
etherStatsBaseGroup.setObjects(
      *(("ETHERLIKE-MIB", "dot3StatsIndex"),
        ("ETHERLIKE-MIB", "dot3StatsAlignmentErrors"),
        ("ETHERLIKE-MIB", "dot3StatsFCSErrors"),
        ("ETHERLIKE-MIB", "dot3StatsSingleCollisionFrames"),
        ("ETHERLIKE-MIB", "dot3StatsMultipleCollisionFrames"),
        ("ETHERLIKE-MIB", "dot3StatsDeferredTransmissions"),
        ("ETHERLIKE-MIB", "dot3StatsLateCollisions"),
        ("ETHERLIKE-MIB", "dot3StatsExcessiveCollisions"),
        ("ETHERLIKE-MIB", "dot3StatsInternalMacTransmitErrors"),
        ("ETHERLIKE-MIB", "dot3StatsCarrierSenseErrors"),
        ("ETHERLIKE-MIB", "dot3StatsFrameTooLongs"),
        ("ETHERLIKE-MIB", "dot3StatsInternalMacReceiveErrors"))
)
if mibBuilder.loadTexts:
    etherStatsBaseGroup.setStatus("current")

etherStatsLowSpeedGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 5)
)
etherStatsLowSpeedGroup.setObjects(
    ("ETHERLIKE-MIB", "dot3StatsSQETestErrors")
)
if mibBuilder.loadTexts:
    etherStatsLowSpeedGroup.setStatus("current")

etherStatsHighSpeedGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 6)
)
etherStatsHighSpeedGroup.setObjects(
    ("ETHERLIKE-MIB", "dot3StatsSymbolErrors")
)
if mibBuilder.loadTexts:
    etherStatsHighSpeedGroup.setStatus("current")

etherDuplexGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 7)
)
etherDuplexGroup.setObjects(
    ("ETHERLIKE-MIB", "dot3StatsDuplexStatus")
)
if mibBuilder.loadTexts:
    etherDuplexGroup.setStatus("current")

etherControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 8)
)
etherControlGroup.setObjects(
      *(("ETHERLIKE-MIB", "dot3ControlFunctionsSupported"),
        ("ETHERLIKE-MIB", "dot3ControlInUnknownOpcodes"))
)
if mibBuilder.loadTexts:
    etherControlGroup.setStatus("current")

etherControlPauseGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 9)
)
etherControlPauseGroup.setObjects(
      *(("ETHERLIKE-MIB", "dot3PauseAdminMode"),
        ("ETHERLIKE-MIB", "dot3PauseOperMode"),
        ("ETHERLIKE-MIB", "dot3InPauseFrames"),
        ("ETHERLIKE-MIB", "dot3OutPauseFrames"))
)
if mibBuilder.loadTexts:
    etherControlPauseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etherCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 35, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etherCompliance.setStatus(
        "deprecated"
    )

ether100MbsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 35, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ether100MbsCompliance.setStatus(
        "deprecated"
    )

dot3Compliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 35, 2, 2, 3)
)
if mibBuilder.loadTexts:
    dot3Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ETHERLIKE-MIB",
    **{"dot3": dot3,
       "dot3StatsTable": dot3StatsTable,
       "dot3StatsEntry": dot3StatsEntry,
       "dot3StatsIndex": dot3StatsIndex,
       "dot3StatsAlignmentErrors": dot3StatsAlignmentErrors,
       "dot3StatsFCSErrors": dot3StatsFCSErrors,
       "dot3StatsSingleCollisionFrames": dot3StatsSingleCollisionFrames,
       "dot3StatsMultipleCollisionFrames": dot3StatsMultipleCollisionFrames,
       "dot3StatsSQETestErrors": dot3StatsSQETestErrors,
       "dot3StatsDeferredTransmissions": dot3StatsDeferredTransmissions,
       "dot3StatsLateCollisions": dot3StatsLateCollisions,
       "dot3StatsExcessiveCollisions": dot3StatsExcessiveCollisions,
       "dot3StatsInternalMacTransmitErrors": dot3StatsInternalMacTransmitErrors,
       "dot3StatsCarrierSenseErrors": dot3StatsCarrierSenseErrors,
       "dot3StatsFrameTooLongs": dot3StatsFrameTooLongs,
       "dot3StatsInternalMacReceiveErrors": dot3StatsInternalMacReceiveErrors,
       "dot3StatsEtherChipSet": dot3StatsEtherChipSet,
       "dot3StatsSymbolErrors": dot3StatsSymbolErrors,
       "dot3StatsDuplexStatus": dot3StatsDuplexStatus,
       "dot3CollTable": dot3CollTable,
       "dot3CollEntry": dot3CollEntry,
       "dot3CollCount": dot3CollCount,
       "dot3CollFrequencies": dot3CollFrequencies,
       "dot3Tests": dot3Tests,
       "dot3TestTdr": dot3TestTdr,
       "dot3TestLoopBack": dot3TestLoopBack,
       "dot3Errors": dot3Errors,
       "dot3ErrorInitError": dot3ErrorInitError,
       "dot3ErrorLoopbackError": dot3ErrorLoopbackError,
       "dot3ControlTable": dot3ControlTable,
       "dot3ControlEntry": dot3ControlEntry,
       "dot3ControlFunctionsSupported": dot3ControlFunctionsSupported,
       "dot3ControlInUnknownOpcodes": dot3ControlInUnknownOpcodes,
       "dot3PauseTable": dot3PauseTable,
       "dot3PauseEntry": dot3PauseEntry,
       "dot3PauseAdminMode": dot3PauseAdminMode,
       "dot3PauseOperMode": dot3PauseOperMode,
       "dot3InPauseFrames": dot3InPauseFrames,
       "dot3OutPauseFrames": dot3OutPauseFrames,
       "etherMIB": etherMIB,
       "etherMIBObjects": etherMIBObjects,
       "etherConformance": etherConformance,
       "etherGroups": etherGroups,
       "etherStatsGroup": etherStatsGroup,
       "etherCollisionTableGroup": etherCollisionTableGroup,
       "etherStats100MbsGroup": etherStats100MbsGroup,
       "etherStatsBaseGroup": etherStatsBaseGroup,
       "etherStatsLowSpeedGroup": etherStatsLowSpeedGroup,
       "etherStatsHighSpeedGroup": etherStatsHighSpeedGroup,
       "etherDuplexGroup": etherDuplexGroup,
       "etherControlGroup": etherControlGroup,
       "etherControlPauseGroup": etherControlPauseGroup,
       "etherCompliances": etherCompliances,
       "etherCompliance": etherCompliance,
       "ether100MbsCompliance": ether100MbsCompliance,
       "dot3Compliance": dot3Compliance}
)
