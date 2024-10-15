# SNMP MIB module (CISCO-STP-EXTENSIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-STP-EXTENSIONS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:56 2024
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

(dot1dStpPortEntry,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dStpPortEntry")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(VlanIndex,
 vlanTrunkPortEntry,
 vtpVlanEditEntry,
 vtpVlanEntry) = mibBuilder.importSymbols(
    "CISCO-VTP-MIB",
    "VlanIndex",
    "vlanTrunkPortEntry",
    "vtpVlanEditEntry",
    "vtpVlanEntry")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoStpExtensionsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 82)
)
ciscoStpExtensionsMIB.setRevisions(
        ("2013-03-07 00:00",
         "2005-12-20 00:00",
         "2005-04-12 00:00",
         "2004-07-21 00:00",
         "2004-04-08 00:00",
         "2004-01-14 00:00",
         "2003-10-23 00:00",
         "2002-07-11 00:00",
         "2001-12-06 00:00",
         "2001-09-14 00:00",
         "2001-06-20 00:00",
         "2001-04-12 00:00",
         "2000-05-23 00:00",
         "2000-03-21 00:00",
         "1997-11-10 12:00",
         "1997-08-19 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class StpxMSTConfigurationDigest(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



# MIB Managed Objects in the order of their OIDs

_StpxObjects_ObjectIdentity = ObjectIdentity
stpxObjects = _StpxObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1)
)
_StpxUplinkFastObjects_ObjectIdentity = ObjectIdentity
stpxUplinkFastObjects = _StpxUplinkFastObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 1)
)
_StpxUplinkFastEnabled_Type = TruthValue
_StpxUplinkFastEnabled_Object = MibScalar
stpxUplinkFastEnabled = _StpxUplinkFastEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 1, 1),
    _StpxUplinkFastEnabled_Type()
)
stpxUplinkFastEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxUplinkFastEnabled.setStatus("current")
_StpxUplinkFastTransitions_Type = Counter32
_StpxUplinkFastTransitions_Object = MibScalar
stpxUplinkFastTransitions = _StpxUplinkFastTransitions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 1, 2),
    _StpxUplinkFastTransitions_Type()
)
stpxUplinkFastTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxUplinkFastTransitions.setStatus("current")
if mibBuilder.loadTexts:
    stpxUplinkFastTransitions.setUnits("transitions")


class _StpxUplinkStationLearningGenRate_Type(Integer32):
    """Custom type stpxUplinkStationLearningGenRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_StpxUplinkStationLearningGenRate_Type.__name__ = "Integer32"
_StpxUplinkStationLearningGenRate_Object = MibScalar
stpxUplinkStationLearningGenRate = _StpxUplinkStationLearningGenRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 1, 3),
    _StpxUplinkStationLearningGenRate_Type()
)
stpxUplinkStationLearningGenRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxUplinkStationLearningGenRate.setStatus("current")
if mibBuilder.loadTexts:
    stpxUplinkStationLearningGenRate.setUnits("frames")
_StpxUplinkStationLearningFrames_Type = Counter32
_StpxUplinkStationLearningFrames_Object = MibScalar
stpxUplinkStationLearningFrames = _StpxUplinkStationLearningFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 1, 4),
    _StpxUplinkStationLearningFrames_Type()
)
stpxUplinkStationLearningFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxUplinkStationLearningFrames.setStatus("current")
if mibBuilder.loadTexts:
    stpxUplinkStationLearningFrames.setUnits("frames")
_StpxUplinkFastOperEnabled_Type = TruthValue
_StpxUplinkFastOperEnabled_Object = MibScalar
stpxUplinkFastOperEnabled = _StpxUplinkFastOperEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 1, 5),
    _StpxUplinkFastOperEnabled_Type()
)
stpxUplinkFastOperEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxUplinkFastOperEnabled.setStatus("current")
_StpxVlanObjects_ObjectIdentity = ObjectIdentity
stpxVlanObjects = _StpxVlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 2)
)
_StpxPreferredVlansTable_Object = MibTable
stpxPreferredVlansTable = _StpxPreferredVlansTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 2, 1)
)
if mibBuilder.loadTexts:
    stpxPreferredVlansTable.setStatus("current")
_StpxPreferredVlansEntry_Object = MibTableRow
stpxPreferredVlansEntry = _StpxPreferredVlansEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    stpxPreferredVlansEntry.setStatus("current")


class _StpxPreferredVlansMap_Type(OctetString):
    """Custom type stpxPreferredVlansMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_StpxPreferredVlansMap_Type.__name__ = "OctetString"
_StpxPreferredVlansMap_Object = MibTableColumn
stpxPreferredVlansMap = _StpxPreferredVlansMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 2, 1, 1, 1),
    _StpxPreferredVlansMap_Type()
)
stpxPreferredVlansMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxPreferredVlansMap.setStatus("current")


class _StpxPreferredVlansMap2k_Type(OctetString):
    """Custom type stpxPreferredVlansMap2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_StpxPreferredVlansMap2k_Type.__name__ = "OctetString"
_StpxPreferredVlansMap2k_Object = MibTableColumn
stpxPreferredVlansMap2k = _StpxPreferredVlansMap2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 2, 1, 1, 2),
    _StpxPreferredVlansMap2k_Type()
)
stpxPreferredVlansMap2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxPreferredVlansMap2k.setStatus("current")


class _StpxPreferredVlansMap3k_Type(OctetString):
    """Custom type stpxPreferredVlansMap3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_StpxPreferredVlansMap3k_Type.__name__ = "OctetString"
_StpxPreferredVlansMap3k_Object = MibTableColumn
stpxPreferredVlansMap3k = _StpxPreferredVlansMap3k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 2, 1, 1, 3),
    _StpxPreferredVlansMap3k_Type()
)
stpxPreferredVlansMap3k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxPreferredVlansMap3k.setStatus("current")


class _StpxPreferredVlansMap4k_Type(OctetString):
    """Custom type stpxPreferredVlansMap4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_StpxPreferredVlansMap4k_Type.__name__ = "OctetString"
_StpxPreferredVlansMap4k_Object = MibTableColumn
stpxPreferredVlansMap4k = _StpxPreferredVlansMap4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 2, 1, 1, 4),
    _StpxPreferredVlansMap4k_Type()
)
stpxPreferredVlansMap4k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxPreferredVlansMap4k.setStatus("current")
_StpxPVSTVlanTable_Object = MibTable
stpxPVSTVlanTable = _StpxPVSTVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 2, 2)
)
if mibBuilder.loadTexts:
    stpxPVSTVlanTable.setStatus("current")
_StpxPVSTVlanEntry_Object = MibTableRow
stpxPVSTVlanEntry = _StpxPVSTVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 2, 2, 1)
)
stpxPVSTVlanEntry.setIndexNames(
    (0, "CISCO-STP-EXTENSIONS-MIB", "stpxPVSTVlanIndex"),
)
if mibBuilder.loadTexts:
    stpxPVSTVlanEntry.setStatus("current")
_StpxPVSTVlanIndex_Type = VlanIndex
_StpxPVSTVlanIndex_Object = MibTableColumn
stpxPVSTVlanIndex = _StpxPVSTVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 2, 2, 1, 1),
    _StpxPVSTVlanIndex_Type()
)
stpxPVSTVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpxPVSTVlanIndex.setStatus("current")


class _StpxPVSTVlanEnable_Type(Integer32):
    """Custom type stpxPVSTVlanEnable based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_StpxPVSTVlanEnable_Type.__name__ = "Integer32"
_StpxPVSTVlanEnable_Object = MibTableColumn
stpxPVSTVlanEnable = _StpxPVSTVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 2, 2, 1, 2),
    _StpxPVSTVlanEnable_Type()
)
stpxPVSTVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxPVSTVlanEnable.setStatus("current")
_StpxInconsistencyObjects_ObjectIdentity = ObjectIdentity
stpxInconsistencyObjects = _StpxInconsistencyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 3)
)
_StpxInconsistencyTable_Object = MibTable
stpxInconsistencyTable = _StpxInconsistencyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 3, 1)
)
if mibBuilder.loadTexts:
    stpxInconsistencyTable.setStatus("current")
_StpxInconsistencyEntry_Object = MibTableRow
stpxInconsistencyEntry = _StpxInconsistencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 3, 1, 1)
)
stpxInconsistencyEntry.setIndexNames(
    (0, "CISCO-STP-EXTENSIONS-MIB", "stpxVlanIndex"),
    (0, "CISCO-STP-EXTENSIONS-MIB", "stpxPortIndex"),
)
if mibBuilder.loadTexts:
    stpxInconsistencyEntry.setStatus("current")
_StpxVlanIndex_Type = VlanIndex
_StpxVlanIndex_Object = MibTableColumn
stpxVlanIndex = _StpxVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 3, 1, 1, 1),
    _StpxVlanIndex_Type()
)
stpxVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpxVlanIndex.setStatus("current")


class _StpxPortIndex_Type(Integer32):
    """Custom type stpxPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StpxPortIndex_Type.__name__ = "Integer32"
_StpxPortIndex_Object = MibTableColumn
stpxPortIndex = _StpxPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 3, 1, 1, 2),
    _StpxPortIndex_Type()
)
stpxPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpxPortIndex.setStatus("current")


class _StpxInconsistentState_Type(Bits):
    """Custom type stpxInconsistentState based on Bits"""
    namedValues = NamedValues(
        *(("pvidInconsistent", 1),
          ("typeInconsistent", 0))
    )

_StpxInconsistentState_Type.__name__ = "Bits"
_StpxInconsistentState_Object = MibTableColumn
stpxInconsistentState = _StpxInconsistentState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 3, 1, 1, 3),
    _StpxInconsistentState_Type()
)
stpxInconsistentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxInconsistentState.setStatus("current")
_StpxBackboneFastObjects_ObjectIdentity = ObjectIdentity
stpxBackboneFastObjects = _StpxBackboneFastObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 4)
)
_StpxBackboneFastEnabled_Type = TruthValue
_StpxBackboneFastEnabled_Object = MibScalar
stpxBackboneFastEnabled = _StpxBackboneFastEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 4, 1),
    _StpxBackboneFastEnabled_Type()
)
stpxBackboneFastEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxBackboneFastEnabled.setStatus("current")
_StpxBackboneFastInInferiorBPDUs_Type = Counter32
_StpxBackboneFastInInferiorBPDUs_Object = MibScalar
stpxBackboneFastInInferiorBPDUs = _StpxBackboneFastInInferiorBPDUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 4, 2),
    _StpxBackboneFastInInferiorBPDUs_Type()
)
stpxBackboneFastInInferiorBPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxBackboneFastInInferiorBPDUs.setStatus("current")
_StpxBackboneFastInRLQRequestPDUs_Type = Counter32
_StpxBackboneFastInRLQRequestPDUs_Object = MibScalar
stpxBackboneFastInRLQRequestPDUs = _StpxBackboneFastInRLQRequestPDUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 4, 3),
    _StpxBackboneFastInRLQRequestPDUs_Type()
)
stpxBackboneFastInRLQRequestPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxBackboneFastInRLQRequestPDUs.setStatus("current")
_StpxBackboneFastInRLQResponsePDUs_Type = Counter32
_StpxBackboneFastInRLQResponsePDUs_Object = MibScalar
stpxBackboneFastInRLQResponsePDUs = _StpxBackboneFastInRLQResponsePDUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 4, 4),
    _StpxBackboneFastInRLQResponsePDUs_Type()
)
stpxBackboneFastInRLQResponsePDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxBackboneFastInRLQResponsePDUs.setStatus("current")
_StpxBackboneFastOutRLQRequestPDUs_Type = Counter32
_StpxBackboneFastOutRLQRequestPDUs_Object = MibScalar
stpxBackboneFastOutRLQRequestPDUs = _StpxBackboneFastOutRLQRequestPDUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 4, 5),
    _StpxBackboneFastOutRLQRequestPDUs_Type()
)
stpxBackboneFastOutRLQRequestPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxBackboneFastOutRLQRequestPDUs.setStatus("current")
_StpxBackboneFastOutRLQResponsePDUs_Type = Counter32
_StpxBackboneFastOutRLQResponsePDUs_Object = MibScalar
stpxBackboneFastOutRLQResponsePDUs = _StpxBackboneFastOutRLQResponsePDUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 4, 6),
    _StpxBackboneFastOutRLQResponsePDUs_Type()
)
stpxBackboneFastOutRLQResponsePDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxBackboneFastOutRLQResponsePDUs.setStatus("current")
_StpxBackboneFastOperEnabled_Type = TruthValue
_StpxBackboneFastOperEnabled_Object = MibScalar
stpxBackboneFastOperEnabled = _StpxBackboneFastOperEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 4, 7),
    _StpxBackboneFastOperEnabled_Type()
)
stpxBackboneFastOperEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxBackboneFastOperEnabled.setStatus("current")
_StpxRootGuardObjects_ObjectIdentity = ObjectIdentity
stpxRootGuardObjects = _StpxRootGuardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 5)
)
_StpxRootGuardConfigTable_Object = MibTable
stpxRootGuardConfigTable = _StpxRootGuardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 5, 1)
)
if mibBuilder.loadTexts:
    stpxRootGuardConfigTable.setStatus("current")
_StpxRootGuardConfigEntry_Object = MibTableRow
stpxRootGuardConfigEntry = _StpxRootGuardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 5, 1, 1)
)
stpxRootGuardConfigEntry.setIndexNames(
    (0, "CISCO-STP-EXTENSIONS-MIB", "stpxRootGuardConfigPortIndex"),
)
if mibBuilder.loadTexts:
    stpxRootGuardConfigEntry.setStatus("current")


class _StpxRootGuardConfigPortIndex_Type(Integer32):
    """Custom type stpxRootGuardConfigPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StpxRootGuardConfigPortIndex_Type.__name__ = "Integer32"
_StpxRootGuardConfigPortIndex_Object = MibTableColumn
stpxRootGuardConfigPortIndex = _StpxRootGuardConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 5, 1, 1, 1),
    _StpxRootGuardConfigPortIndex_Type()
)
stpxRootGuardConfigPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpxRootGuardConfigPortIndex.setStatus("current")


class _StpxRootGuardConfigEnabled_Type(TruthValue):
    """Custom type stpxRootGuardConfigEnabled based on TruthValue"""


_StpxRootGuardConfigEnabled_Object = MibTableColumn
stpxRootGuardConfigEnabled = _StpxRootGuardConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 5, 1, 1, 2),
    _StpxRootGuardConfigEnabled_Type()
)
stpxRootGuardConfigEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxRootGuardConfigEnabled.setStatus("current")
_StpxRootInconsistencyTable_Object = MibTable
stpxRootInconsistencyTable = _StpxRootInconsistencyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 5, 2)
)
if mibBuilder.loadTexts:
    stpxRootInconsistencyTable.setStatus("current")
_StpxRootInconsistencyEntry_Object = MibTableRow
stpxRootInconsistencyEntry = _StpxRootInconsistencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 5, 2, 1)
)
stpxRootInconsistencyEntry.setIndexNames(
    (0, "CISCO-STP-EXTENSIONS-MIB", "stpxRootInconsistencyIndex"),
    (0, "CISCO-STP-EXTENSIONS-MIB", "stpxRootInconsistencyPortIndex"),
)
if mibBuilder.loadTexts:
    stpxRootInconsistencyEntry.setStatus("current")


class _StpxRootInconsistencyIndex_Type(Integer32):
    """Custom type stpxRootInconsistencyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StpxRootInconsistencyIndex_Type.__name__ = "Integer32"
_StpxRootInconsistencyIndex_Object = MibTableColumn
stpxRootInconsistencyIndex = _StpxRootInconsistencyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 5, 2, 1, 1),
    _StpxRootInconsistencyIndex_Type()
)
stpxRootInconsistencyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpxRootInconsistencyIndex.setStatus("current")


class _StpxRootInconsistencyPortIndex_Type(Integer32):
    """Custom type stpxRootInconsistencyPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StpxRootInconsistencyPortIndex_Type.__name__ = "Integer32"
_StpxRootInconsistencyPortIndex_Object = MibTableColumn
stpxRootInconsistencyPortIndex = _StpxRootInconsistencyPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 5, 2, 1, 2),
    _StpxRootInconsistencyPortIndex_Type()
)
stpxRootInconsistencyPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpxRootInconsistencyPortIndex.setStatus("current")
_StpxRootInconsistencyState_Type = TruthValue
_StpxRootInconsistencyState_Object = MibTableColumn
stpxRootInconsistencyState = _StpxRootInconsistencyState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 5, 2, 1, 3),
    _StpxRootInconsistencyState_Type()
)
stpxRootInconsistencyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxRootInconsistencyState.setStatus("current")
_StpxSpanningTreeObjects_ObjectIdentity = ObjectIdentity
stpxSpanningTreeObjects = _StpxSpanningTreeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 6)
)


class _StpxSpanningTreeType_Type(Integer32):
    """Custom type stpxSpanningTreeType based on Integer32"""
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
        *(("mistp", 2),
          ("mistpPvstPlus", 3),
          ("mst", 4),
          ("pvstPlus", 1),
          ("rapidPvstPlus", 5))
    )


_StpxSpanningTreeType_Type.__name__ = "Integer32"
_StpxSpanningTreeType_Object = MibScalar
stpxSpanningTreeType = _StpxSpanningTreeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 6, 1),
    _StpxSpanningTreeType_Type()
)
stpxSpanningTreeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxSpanningTreeType.setStatus("current")


class _StpxSpanningTreePathCostMode_Type(Integer32):
    """Custom type stpxSpanningTreePathCostMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 2),
          ("short", 1))
    )


_StpxSpanningTreePathCostMode_Type.__name__ = "Integer32"
_StpxSpanningTreePathCostMode_Object = MibScalar
stpxSpanningTreePathCostMode = _StpxSpanningTreePathCostMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 6, 2),
    _StpxSpanningTreePathCostMode_Type()
)
stpxSpanningTreePathCostMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxSpanningTreePathCostMode.setStatus("current")
_StpxLongStpPortPathCostTable_Object = MibTable
stpxLongStpPortPathCostTable = _StpxLongStpPortPathCostTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 6, 3)
)
if mibBuilder.loadTexts:
    stpxLongStpPortPathCostTable.setStatus("current")
_StpxLongStpPortPathCostEntry_Object = MibTableRow
stpxLongStpPortPathCostEntry = _StpxLongStpPortPathCostEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    stpxLongStpPortPathCostEntry.setStatus("current")
_StpxLongStpPortPathCost_Type = Unsigned32
_StpxLongStpPortPathCost_Object = MibTableColumn
stpxLongStpPortPathCost = _StpxLongStpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 6, 3, 1, 1),
    _StpxLongStpPortPathCost_Type()
)
stpxLongStpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxLongStpPortPathCost.setStatus("current")
_StpxExtendedSysIDAdminEnabled_Type = TruthValue
_StpxExtendedSysIDAdminEnabled_Object = MibScalar
stpxExtendedSysIDAdminEnabled = _StpxExtendedSysIDAdminEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 6, 4),
    _StpxExtendedSysIDAdminEnabled_Type()
)
stpxExtendedSysIDAdminEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxExtendedSysIDAdminEnabled.setStatus("current")
_StpxExtendedSysIDOperEnabled_Type = TruthValue
_StpxExtendedSysIDOperEnabled_Object = MibScalar
stpxExtendedSysIDOperEnabled = _StpxExtendedSysIDOperEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 6, 5),
    _StpxExtendedSysIDOperEnabled_Type()
)
stpxExtendedSysIDOperEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxExtendedSysIDOperEnabled.setStatus("current")


class _StpxNotificationEnable_Type(Bits):
    """Custom type stpxNotificationEnable based on Bits"""
    namedValues = NamedValues(
        *(("inconsistency", 2),
          ("loopInconsistency", 4),
          ("newRoot", 0),
          ("rootInconsistency", 3),
          ("topologyChange", 1))
    )

_StpxNotificationEnable_Type.__name__ = "Bits"
_StpxNotificationEnable_Object = MibScalar
stpxNotificationEnable = _StpxNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 6, 6),
    _StpxNotificationEnable_Type()
)
stpxNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxNotificationEnable.setStatus("current")


class _StpxSpanningTreePathCostOperMode_Type(Integer32):
    """Custom type stpxSpanningTreePathCostOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 2),
          ("short", 1))
    )


_StpxSpanningTreePathCostOperMode_Type.__name__ = "Integer32"
_StpxSpanningTreePathCostOperMode_Object = MibScalar
stpxSpanningTreePathCostOperMode = _StpxSpanningTreePathCostOperMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 6, 7),
    _StpxSpanningTreePathCostOperMode_Type()
)
stpxSpanningTreePathCostOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxSpanningTreePathCostOperMode.setStatus("current")
_StpxMISTPObjects_ObjectIdentity = ObjectIdentity
stpxMISTPObjects = _StpxMISTPObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 7)
)


class _StpxMISTPInstanceNumber_Type(Integer32):
    """Custom type stpxMISTPInstanceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_StpxMISTPInstanceNumber_Type.__name__ = "Integer32"
_StpxMISTPInstanceNumber_Object = MibScalar
stpxMISTPInstanceNumber = _StpxMISTPInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 7, 1),
    _StpxMISTPInstanceNumber_Type()
)
stpxMISTPInstanceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxMISTPInstanceNumber.setStatus("current")
_StpxMISTPInstanceTable_Object = MibTable
stpxMISTPInstanceTable = _StpxMISTPInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 7, 2)
)
if mibBuilder.loadTexts:
    stpxMISTPInstanceTable.setStatus("current")
_StpxMISTPInstanceEntry_Object = MibTableRow
stpxMISTPInstanceEntry = _StpxMISTPInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 7, 2, 1)
)
stpxMISTPInstanceEntry.setIndexNames(
    (0, "CISCO-STP-EXTENSIONS-MIB", "stpxMISTPInstanceIndex"),
)
if mibBuilder.loadTexts:
    stpxMISTPInstanceEntry.setStatus("current")


class _StpxMISTPInstanceIndex_Type(Integer32):
    """Custom type stpxMISTPInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_StpxMISTPInstanceIndex_Type.__name__ = "Integer32"
_StpxMISTPInstanceIndex_Object = MibTableColumn
stpxMISTPInstanceIndex = _StpxMISTPInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 7, 2, 1, 1),
    _StpxMISTPInstanceIndex_Type()
)
stpxMISTPInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpxMISTPInstanceIndex.setStatus("current")


class _StpxMISTPInstanceEnable_Type(TruthValue):
    """Custom type stpxMISTPInstanceEnable based on TruthValue"""


_StpxMISTPInstanceEnable_Object = MibTableColumn
stpxMISTPInstanceEnable = _StpxMISTPInstanceEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 7, 2, 1, 2),
    _StpxMISTPInstanceEnable_Type()
)
stpxMISTPInstanceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxMISTPInstanceEnable.setStatus("current")


class _StpxMISTPInstanceVlansMapped_Type(OctetString):
    """Custom type stpxMISTPInstanceVlansMapped based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_StpxMISTPInstanceVlansMapped_Type.__name__ = "OctetString"
_StpxMISTPInstanceVlansMapped_Object = MibTableColumn
stpxMISTPInstanceVlansMapped = _StpxMISTPInstanceVlansMapped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 7, 2, 1, 3),
    _StpxMISTPInstanceVlansMapped_Type()
)
stpxMISTPInstanceVlansMapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxMISTPInstanceVlansMapped.setStatus("current")


class _StpxMISTPInstanceVlansMapped2k_Type(OctetString):
    """Custom type stpxMISTPInstanceVlansMapped2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_StpxMISTPInstanceVlansMapped2k_Type.__name__ = "OctetString"
_StpxMISTPInstanceVlansMapped2k_Object = MibTableColumn
stpxMISTPInstanceVlansMapped2k = _StpxMISTPInstanceVlansMapped2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 7, 2, 1, 4),
    _StpxMISTPInstanceVlansMapped2k_Type()
)
stpxMISTPInstanceVlansMapped2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxMISTPInstanceVlansMapped2k.setStatus("current")


class _StpxMISTPInstanceVlansMapped3k_Type(OctetString):
    """Custom type stpxMISTPInstanceVlansMapped3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_StpxMISTPInstanceVlansMapped3k_Type.__name__ = "OctetString"
_StpxMISTPInstanceVlansMapped3k_Object = MibTableColumn
stpxMISTPInstanceVlansMapped3k = _StpxMISTPInstanceVlansMapped3k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 7, 2, 1, 5),
    _StpxMISTPInstanceVlansMapped3k_Type()
)
stpxMISTPInstanceVlansMapped3k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxMISTPInstanceVlansMapped3k.setStatus("current")


class _StpxMISTPInstanceVlansMapped4k_Type(OctetString):
    """Custom type stpxMISTPInstanceVlansMapped4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_StpxMISTPInstanceVlansMapped4k_Type.__name__ = "OctetString"
_StpxMISTPInstanceVlansMapped4k_Object = MibTableColumn
stpxMISTPInstanceVlansMapped4k = _StpxMISTPInstanceVlansMapped4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 7, 2, 1, 6),
    _StpxMISTPInstanceVlansMapped4k_Type()
)
stpxMISTPInstanceVlansMapped4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxMISTPInstanceVlansMapped4k.setStatus("current")
_StpxVlanMISTPInstMapTable_Object = MibTable
stpxVlanMISTPInstMapTable = _StpxVlanMISTPInstMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 7, 3)
)
if mibBuilder.loadTexts:
    stpxVlanMISTPInstMapTable.setStatus("current")
_StpxVlanMISTPInstMapEntry_Object = MibTableRow
stpxVlanMISTPInstMapEntry = _StpxVlanMISTPInstMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 7, 3, 1)
)
if mibBuilder.loadTexts:
    stpxVlanMISTPInstMapEntry.setStatus("current")


class _StpxVlanMISTPInstMapInstIndex_Type(Integer32):
    """Custom type stpxVlanMISTPInstMapInstIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_StpxVlanMISTPInstMapInstIndex_Type.__name__ = "Integer32"
_StpxVlanMISTPInstMapInstIndex_Object = MibTableColumn
stpxVlanMISTPInstMapInstIndex = _StpxVlanMISTPInstMapInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 7, 3, 1, 1),
    _StpxVlanMISTPInstMapInstIndex_Type()
)
stpxVlanMISTPInstMapInstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxVlanMISTPInstMapInstIndex.setStatus("current")
_StpxVlanMISTPInstMapEditTable_Object = MibTable
stpxVlanMISTPInstMapEditTable = _StpxVlanMISTPInstMapEditTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 7, 4)
)
if mibBuilder.loadTexts:
    stpxVlanMISTPInstMapEditTable.setStatus("current")
_StpxVlanMISTPInstMapEditEntry_Object = MibTableRow
stpxVlanMISTPInstMapEditEntry = _StpxVlanMISTPInstMapEditEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 7, 4, 1)
)
if mibBuilder.loadTexts:
    stpxVlanMISTPInstMapEditEntry.setStatus("current")


class _StpxVlanMISTPInstMapEditInstIndex_Type(Integer32):
    """Custom type stpxVlanMISTPInstMapEditInstIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_StpxVlanMISTPInstMapEditInstIndex_Type.__name__ = "Integer32"
_StpxVlanMISTPInstMapEditInstIndex_Object = MibTableColumn
stpxVlanMISTPInstMapEditInstIndex = _StpxVlanMISTPInstMapEditInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 7, 4, 1, 1),
    _StpxVlanMISTPInstMapEditInstIndex_Type()
)
stpxVlanMISTPInstMapEditInstIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stpxVlanMISTPInstMapEditInstIndex.setStatus("current")
_StpxPreferredMISTPInstancesTable_Object = MibTable
stpxPreferredMISTPInstancesTable = _StpxPreferredMISTPInstancesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 7, 5)
)
if mibBuilder.loadTexts:
    stpxPreferredMISTPInstancesTable.setStatus("current")
_StpxPreferredMISTPInstancesEntry_Object = MibTableRow
stpxPreferredMISTPInstancesEntry = _StpxPreferredMISTPInstancesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 7, 5, 1)
)
if mibBuilder.loadTexts:
    stpxPreferredMISTPInstancesEntry.setStatus("current")


class _StpxPreferredMISTPInstancesMap_Type(OctetString):
    """Custom type stpxPreferredMISTPInstancesMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_StpxPreferredMISTPInstancesMap_Type.__name__ = "OctetString"
_StpxPreferredMISTPInstancesMap_Object = MibTableColumn
stpxPreferredMISTPInstancesMap = _StpxPreferredMISTPInstancesMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 7, 5, 1, 1),
    _StpxPreferredMISTPInstancesMap_Type()
)
stpxPreferredMISTPInstancesMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxPreferredMISTPInstancesMap.setStatus("current")
_StpxLoopGuardObjects_ObjectIdentity = ObjectIdentity
stpxLoopGuardObjects = _StpxLoopGuardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 8)
)
_StpxLoopGuardConfigTable_Object = MibTable
stpxLoopGuardConfigTable = _StpxLoopGuardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 8, 1)
)
if mibBuilder.loadTexts:
    stpxLoopGuardConfigTable.setStatus("current")
_StpxLoopGuardConfigEntry_Object = MibTableRow
stpxLoopGuardConfigEntry = _StpxLoopGuardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 8, 1, 1)
)
stpxLoopGuardConfigEntry.setIndexNames(
    (0, "CISCO-STP-EXTENSIONS-MIB", "stpxLoopGuardConfigPortIndex"),
)
if mibBuilder.loadTexts:
    stpxLoopGuardConfigEntry.setStatus("current")


class _StpxLoopGuardConfigPortIndex_Type(Integer32):
    """Custom type stpxLoopGuardConfigPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StpxLoopGuardConfigPortIndex_Type.__name__ = "Integer32"
_StpxLoopGuardConfigPortIndex_Object = MibTableColumn
stpxLoopGuardConfigPortIndex = _StpxLoopGuardConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 8, 1, 1, 1),
    _StpxLoopGuardConfigPortIndex_Type()
)
stpxLoopGuardConfigPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpxLoopGuardConfigPortIndex.setStatus("current")


class _StpxLoopGuardConfigEnabled_Type(TruthValue):
    """Custom type stpxLoopGuardConfigEnabled based on TruthValue"""


_StpxLoopGuardConfigEnabled_Object = MibTableColumn
stpxLoopGuardConfigEnabled = _StpxLoopGuardConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 8, 1, 1, 2),
    _StpxLoopGuardConfigEnabled_Type()
)
stpxLoopGuardConfigEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxLoopGuardConfigEnabled.setStatus("deprecated")


class _StpxLoopGuardConfigMode_Type(Integer32):
    """Custom type stpxLoopGuardConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("disable", 2),
          ("enable", 1))
    )


_StpxLoopGuardConfigMode_Type.__name__ = "Integer32"
_StpxLoopGuardConfigMode_Object = MibTableColumn
stpxLoopGuardConfigMode = _StpxLoopGuardConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 8, 1, 1, 3),
    _StpxLoopGuardConfigMode_Type()
)
stpxLoopGuardConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxLoopGuardConfigMode.setStatus("current")
_StpxLoopInconsistencyTable_Object = MibTable
stpxLoopInconsistencyTable = _StpxLoopInconsistencyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 8, 2)
)
if mibBuilder.loadTexts:
    stpxLoopInconsistencyTable.setStatus("current")
_StpxLoopInconsistencyEntry_Object = MibTableRow
stpxLoopInconsistencyEntry = _StpxLoopInconsistencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 8, 2, 1)
)
stpxLoopInconsistencyEntry.setIndexNames(
    (0, "CISCO-STP-EXTENSIONS-MIB", "stpxLoopInconsistencyIndex"),
    (0, "CISCO-STP-EXTENSIONS-MIB", "stpxLoopInconsistencyPortIndex"),
)
if mibBuilder.loadTexts:
    stpxLoopInconsistencyEntry.setStatus("current")


class _StpxLoopInconsistencyIndex_Type(Integer32):
    """Custom type stpxLoopInconsistencyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StpxLoopInconsistencyIndex_Type.__name__ = "Integer32"
_StpxLoopInconsistencyIndex_Object = MibTableColumn
stpxLoopInconsistencyIndex = _StpxLoopInconsistencyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 8, 2, 1, 1),
    _StpxLoopInconsistencyIndex_Type()
)
stpxLoopInconsistencyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpxLoopInconsistencyIndex.setStatus("current")


class _StpxLoopInconsistencyPortIndex_Type(Integer32):
    """Custom type stpxLoopInconsistencyPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StpxLoopInconsistencyPortIndex_Type.__name__ = "Integer32"
_StpxLoopInconsistencyPortIndex_Object = MibTableColumn
stpxLoopInconsistencyPortIndex = _StpxLoopInconsistencyPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 8, 2, 1, 2),
    _StpxLoopInconsistencyPortIndex_Type()
)
stpxLoopInconsistencyPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpxLoopInconsistencyPortIndex.setStatus("current")
_StpxLoopInconsistencyState_Type = TruthValue
_StpxLoopInconsistencyState_Object = MibTableColumn
stpxLoopInconsistencyState = _StpxLoopInconsistencyState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 8, 2, 1, 3),
    _StpxLoopInconsistencyState_Type()
)
stpxLoopInconsistencyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxLoopInconsistencyState.setStatus("current")


class _StpxLoopGuardGlobalDefaultMode_Type(Integer32):
    """Custom type stpxLoopGuardGlobalDefaultMode based on Integer32"""
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


_StpxLoopGuardGlobalDefaultMode_Type.__name__ = "Integer32"
_StpxLoopGuardGlobalDefaultMode_Object = MibScalar
stpxLoopGuardGlobalDefaultMode = _StpxLoopGuardGlobalDefaultMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 8, 3),
    _StpxLoopGuardGlobalDefaultMode_Type()
)
stpxLoopGuardGlobalDefaultMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxLoopGuardGlobalDefaultMode.setStatus("current")
_StpxFastStartObjects_ObjectIdentity = ObjectIdentity
stpxFastStartObjects = _StpxFastStartObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 9)
)


class _StpxFastStartBpduGuardEnable_Type(TruthValue):
    """Custom type stpxFastStartBpduGuardEnable based on TruthValue"""


_StpxFastStartBpduGuardEnable_Object = MibScalar
stpxFastStartBpduGuardEnable = _StpxFastStartBpduGuardEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 9, 1),
    _StpxFastStartBpduGuardEnable_Type()
)
stpxFastStartBpduGuardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxFastStartBpduGuardEnable.setStatus("current")


class _StpxFastStartBpduFilterEnable_Type(TruthValue):
    """Custom type stpxFastStartBpduFilterEnable based on TruthValue"""


_StpxFastStartBpduFilterEnable_Object = MibScalar
stpxFastStartBpduFilterEnable = _StpxFastStartBpduFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 9, 2),
    _StpxFastStartBpduFilterEnable_Type()
)
stpxFastStartBpduFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxFastStartBpduFilterEnable.setStatus("current")
_StpxFastStartPortTable_Object = MibTable
stpxFastStartPortTable = _StpxFastStartPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 9, 3)
)
if mibBuilder.loadTexts:
    stpxFastStartPortTable.setStatus("current")
_StpxFastStartPortEntry_Object = MibTableRow
stpxFastStartPortEntry = _StpxFastStartPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 9, 3, 1)
)
stpxFastStartPortEntry.setIndexNames(
    (0, "CISCO-STP-EXTENSIONS-MIB", "stpxFastStartPortIndex"),
)
if mibBuilder.loadTexts:
    stpxFastStartPortEntry.setStatus("current")


class _StpxFastStartPortIndex_Type(Integer32):
    """Custom type stpxFastStartPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StpxFastStartPortIndex_Type.__name__ = "Integer32"
_StpxFastStartPortIndex_Object = MibTableColumn
stpxFastStartPortIndex = _StpxFastStartPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 9, 3, 1, 1),
    _StpxFastStartPortIndex_Type()
)
stpxFastStartPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpxFastStartPortIndex.setStatus("current")


class _StpxFastStartPortEnable_Type(TruthValue):
    """Custom type stpxFastStartPortEnable based on TruthValue"""


_StpxFastStartPortEnable_Object = MibTableColumn
stpxFastStartPortEnable = _StpxFastStartPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 9, 3, 1, 2),
    _StpxFastStartPortEnable_Type()
)
stpxFastStartPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxFastStartPortEnable.setStatus("deprecated")


class _StpxFastStartPortMode_Type(Integer32):
    """Custom type stpxFastStartPortMode based on Integer32"""
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
        *(("default", 4),
          ("disable", 2),
          ("enable", 1),
          ("enableForTrunk", 3),
          ("network", 5))
    )


_StpxFastStartPortMode_Type.__name__ = "Integer32"
_StpxFastStartPortMode_Object = MibTableColumn
stpxFastStartPortMode = _StpxFastStartPortMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 9, 3, 1, 3),
    _StpxFastStartPortMode_Type()
)
stpxFastStartPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxFastStartPortMode.setStatus("current")


class _StpxFastStartPortBpduGuardMode_Type(Integer32):
    """Custom type stpxFastStartPortBpduGuardMode based on Integer32"""
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
        *(("default", 3),
          ("disable", 2),
          ("enable", 1))
    )


_StpxFastStartPortBpduGuardMode_Type.__name__ = "Integer32"
_StpxFastStartPortBpduGuardMode_Object = MibTableColumn
stpxFastStartPortBpduGuardMode = _StpxFastStartPortBpduGuardMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 9, 3, 1, 4),
    _StpxFastStartPortBpduGuardMode_Type()
)
stpxFastStartPortBpduGuardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxFastStartPortBpduGuardMode.setStatus("current")


class _StpxFastStartPortBpduFilterMode_Type(Integer32):
    """Custom type stpxFastStartPortBpduFilterMode based on Integer32"""
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
        *(("default", 3),
          ("disable", 2),
          ("enable", 1))
    )


_StpxFastStartPortBpduFilterMode_Type.__name__ = "Integer32"
_StpxFastStartPortBpduFilterMode_Object = MibTableColumn
stpxFastStartPortBpduFilterMode = _StpxFastStartPortBpduFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 9, 3, 1, 5),
    _StpxFastStartPortBpduFilterMode_Type()
)
stpxFastStartPortBpduFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxFastStartPortBpduFilterMode.setStatus("current")


class _StpxFastStartGlobalDefaultMode_Type(Integer32):
    """Custom type stpxFastStartGlobalDefaultMode based on Integer32"""
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


_StpxFastStartGlobalDefaultMode_Type.__name__ = "Integer32"
_StpxFastStartGlobalDefaultMode_Object = MibScalar
stpxFastStartGlobalDefaultMode = _StpxFastStartGlobalDefaultMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 9, 4),
    _StpxFastStartGlobalDefaultMode_Type()
)
stpxFastStartGlobalDefaultMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxFastStartGlobalDefaultMode.setStatus("current")
_StpxFastStartOperModeTable_Object = MibTable
stpxFastStartOperModeTable = _StpxFastStartOperModeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 9, 5)
)
if mibBuilder.loadTexts:
    stpxFastStartOperModeTable.setStatus("current")
_StpxFastStartOperModeEntry_Object = MibTableRow
stpxFastStartOperModeEntry = _StpxFastStartOperModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 9, 5, 1)
)
stpxFastStartOperModeEntry.setIndexNames(
    (0, "CISCO-STP-EXTENSIONS-MIB", "stpxFastStartOperModeInstIndex"),
    (0, "CISCO-STP-EXTENSIONS-MIB", "stpxFastStartOperModePortIndex"),
)
if mibBuilder.loadTexts:
    stpxFastStartOperModeEntry.setStatus("current")


class _StpxFastStartOperModeInstIndex_Type(Integer32):
    """Custom type stpxFastStartOperModeInstIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StpxFastStartOperModeInstIndex_Type.__name__ = "Integer32"
_StpxFastStartOperModeInstIndex_Object = MibTableColumn
stpxFastStartOperModeInstIndex = _StpxFastStartOperModeInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 9, 5, 1, 1),
    _StpxFastStartOperModeInstIndex_Type()
)
stpxFastStartOperModeInstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpxFastStartOperModeInstIndex.setStatus("current")


class _StpxFastStartOperModePortIndex_Type(Integer32):
    """Custom type stpxFastStartOperModePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StpxFastStartOperModePortIndex_Type.__name__ = "Integer32"
_StpxFastStartOperModePortIndex_Object = MibTableColumn
stpxFastStartOperModePortIndex = _StpxFastStartOperModePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 9, 5, 1, 2),
    _StpxFastStartOperModePortIndex_Type()
)
stpxFastStartOperModePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpxFastStartOperModePortIndex.setStatus("current")


class _StpxFastStartOperMode_Type(Integer32):
    """Custom type stpxFastStartOperMode based on Integer32"""
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


_StpxFastStartOperMode_Type.__name__ = "Integer32"
_StpxFastStartOperMode_Object = MibTableColumn
stpxFastStartOperMode = _StpxFastStartOperMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 9, 5, 1, 3),
    _StpxFastStartOperMode_Type()
)
stpxFastStartOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxFastStartOperMode.setStatus("current")
_StpxBpduSkewingObjects_ObjectIdentity = ObjectIdentity
stpxBpduSkewingObjects = _StpxBpduSkewingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 10)
)


class _StpxBpduSkewingDetectionEnable_Type(TruthValue):
    """Custom type stpxBpduSkewingDetectionEnable based on TruthValue"""


_StpxBpduSkewingDetectionEnable_Object = MibScalar
stpxBpduSkewingDetectionEnable = _StpxBpduSkewingDetectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 10, 1),
    _StpxBpduSkewingDetectionEnable_Type()
)
stpxBpduSkewingDetectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxBpduSkewingDetectionEnable.setStatus("current")
_StpxBpduSkewingTable_Object = MibTable
stpxBpduSkewingTable = _StpxBpduSkewingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 10, 2)
)
if mibBuilder.loadTexts:
    stpxBpduSkewingTable.setStatus("current")
_StpxBpduSkewingEntry_Object = MibTableRow
stpxBpduSkewingEntry = _StpxBpduSkewingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 10, 2, 1)
)
stpxBpduSkewingEntry.setIndexNames(
    (0, "CISCO-STP-EXTENSIONS-MIB", "stpxBpduSkewingInstanceIndex"),
    (0, "CISCO-STP-EXTENSIONS-MIB", "stpxBpduSkewingPortIndex"),
)
if mibBuilder.loadTexts:
    stpxBpduSkewingEntry.setStatus("current")


class _StpxBpduSkewingInstanceIndex_Type(Integer32):
    """Custom type stpxBpduSkewingInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StpxBpduSkewingInstanceIndex_Type.__name__ = "Integer32"
_StpxBpduSkewingInstanceIndex_Object = MibTableColumn
stpxBpduSkewingInstanceIndex = _StpxBpduSkewingInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 10, 2, 1, 1),
    _StpxBpduSkewingInstanceIndex_Type()
)
stpxBpduSkewingInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpxBpduSkewingInstanceIndex.setStatus("current")


class _StpxBpduSkewingPortIndex_Type(Integer32):
    """Custom type stpxBpduSkewingPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StpxBpduSkewingPortIndex_Type.__name__ = "Integer32"
_StpxBpduSkewingPortIndex_Object = MibTableColumn
stpxBpduSkewingPortIndex = _StpxBpduSkewingPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 10, 2, 1, 2),
    _StpxBpduSkewingPortIndex_Type()
)
stpxBpduSkewingPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpxBpduSkewingPortIndex.setStatus("current")
_StpxBpduSkewingLastSkewDuration_Type = Unsigned32
_StpxBpduSkewingLastSkewDuration_Object = MibTableColumn
stpxBpduSkewingLastSkewDuration = _StpxBpduSkewingLastSkewDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 10, 2, 1, 3),
    _StpxBpduSkewingLastSkewDuration_Type()
)
stpxBpduSkewingLastSkewDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxBpduSkewingLastSkewDuration.setStatus("current")
if mibBuilder.loadTexts:
    stpxBpduSkewingLastSkewDuration.setUnits("milliseconds")
_StpxBpduSkewingWorstSkewDuration_Type = Unsigned32
_StpxBpduSkewingWorstSkewDuration_Object = MibTableColumn
stpxBpduSkewingWorstSkewDuration = _StpxBpduSkewingWorstSkewDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 10, 2, 1, 4),
    _StpxBpduSkewingWorstSkewDuration_Type()
)
stpxBpduSkewingWorstSkewDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxBpduSkewingWorstSkewDuration.setStatus("current")
if mibBuilder.loadTexts:
    stpxBpduSkewingWorstSkewDuration.setUnits("milliseconds")
_StpxBpduSkewingWorstSkewTime_Type = TimeStamp
_StpxBpduSkewingWorstSkewTime_Object = MibTableColumn
stpxBpduSkewingWorstSkewTime = _StpxBpduSkewingWorstSkewTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 10, 2, 1, 5),
    _StpxBpduSkewingWorstSkewTime_Type()
)
stpxBpduSkewingWorstSkewTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxBpduSkewingWorstSkewTime.setStatus("current")
_StpxMSTObjects_ObjectIdentity = ObjectIdentity
stpxMSTObjects = _StpxMSTObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11)
)


class _StpxMSTMaxInstanceNumber_Type(Integer32):
    """Custom type stpxMSTMaxInstanceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_StpxMSTMaxInstanceNumber_Type.__name__ = "Integer32"
_StpxMSTMaxInstanceNumber_Object = MibScalar
stpxMSTMaxInstanceNumber = _StpxMSTMaxInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 1),
    _StpxMSTMaxInstanceNumber_Type()
)
stpxMSTMaxInstanceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxMSTMaxInstanceNumber.setStatus("deprecated")


class _StpxMSTRegionName_Type(DisplayString):
    """Custom type stpxMSTRegionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StpxMSTRegionName_Type.__name__ = "DisplayString"
_StpxMSTRegionName_Object = MibScalar
stpxMSTRegionName = _StpxMSTRegionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 2),
    _StpxMSTRegionName_Type()
)
stpxMSTRegionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxMSTRegionName.setStatus("current")


class _StpxMSTRegionRevision_Type(Integer32):
    """Custom type stpxMSTRegionRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StpxMSTRegionRevision_Type.__name__ = "Integer32"
_StpxMSTRegionRevision_Object = MibScalar
stpxMSTRegionRevision = _StpxMSTRegionRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 3),
    _StpxMSTRegionRevision_Type()
)
stpxMSTRegionRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxMSTRegionRevision.setStatus("deprecated")
_StpxMSTInstanceTable_Object = MibTable
stpxMSTInstanceTable = _StpxMSTInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 4)
)
if mibBuilder.loadTexts:
    stpxMSTInstanceTable.setStatus("deprecated")
_StpxMSTInstanceEntry_Object = MibTableRow
stpxMSTInstanceEntry = _StpxMSTInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 4, 1)
)
stpxMSTInstanceEntry.setIndexNames(
    (0, "CISCO-STP-EXTENSIONS-MIB", "stpxMSTInstanceIndex"),
)
if mibBuilder.loadTexts:
    stpxMSTInstanceEntry.setStatus("deprecated")


class _StpxMSTInstanceIndex_Type(Integer32):
    """Custom type stpxMSTInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_StpxMSTInstanceIndex_Type.__name__ = "Integer32"
_StpxMSTInstanceIndex_Object = MibTableColumn
stpxMSTInstanceIndex = _StpxMSTInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 4, 1, 1),
    _StpxMSTInstanceIndex_Type()
)
stpxMSTInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpxMSTInstanceIndex.setStatus("deprecated")


class _StpxMSTInstanceVlansMapped_Type(OctetString):
    """Custom type stpxMSTInstanceVlansMapped based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_StpxMSTInstanceVlansMapped_Type.__name__ = "OctetString"
_StpxMSTInstanceVlansMapped_Object = MibTableColumn
stpxMSTInstanceVlansMapped = _StpxMSTInstanceVlansMapped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 4, 1, 2),
    _StpxMSTInstanceVlansMapped_Type()
)
stpxMSTInstanceVlansMapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxMSTInstanceVlansMapped.setStatus("deprecated")


class _StpxMSTInstanceVlansMapped2k_Type(OctetString):
    """Custom type stpxMSTInstanceVlansMapped2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_StpxMSTInstanceVlansMapped2k_Type.__name__ = "OctetString"
_StpxMSTInstanceVlansMapped2k_Object = MibTableColumn
stpxMSTInstanceVlansMapped2k = _StpxMSTInstanceVlansMapped2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 4, 1, 3),
    _StpxMSTInstanceVlansMapped2k_Type()
)
stpxMSTInstanceVlansMapped2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxMSTInstanceVlansMapped2k.setStatus("deprecated")


class _StpxMSTInstanceVlansMapped3k_Type(OctetString):
    """Custom type stpxMSTInstanceVlansMapped3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_StpxMSTInstanceVlansMapped3k_Type.__name__ = "OctetString"
_StpxMSTInstanceVlansMapped3k_Object = MibTableColumn
stpxMSTInstanceVlansMapped3k = _StpxMSTInstanceVlansMapped3k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 4, 1, 4),
    _StpxMSTInstanceVlansMapped3k_Type()
)
stpxMSTInstanceVlansMapped3k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxMSTInstanceVlansMapped3k.setStatus("deprecated")


class _StpxMSTInstanceVlansMapped4k_Type(OctetString):
    """Custom type stpxMSTInstanceVlansMapped4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_StpxMSTInstanceVlansMapped4k_Type.__name__ = "OctetString"
_StpxMSTInstanceVlansMapped4k_Object = MibTableColumn
stpxMSTInstanceVlansMapped4k = _StpxMSTInstanceVlansMapped4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 4, 1, 5),
    _StpxMSTInstanceVlansMapped4k_Type()
)
stpxMSTInstanceVlansMapped4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxMSTInstanceVlansMapped4k.setStatus("deprecated")


class _StpxMSTInstanceRemainingHopCount_Type(Integer32):
    """Custom type stpxMSTInstanceRemainingHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_StpxMSTInstanceRemainingHopCount_Type.__name__ = "Integer32"
_StpxMSTInstanceRemainingHopCount_Object = MibTableColumn
stpxMSTInstanceRemainingHopCount = _StpxMSTInstanceRemainingHopCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 4, 1, 6),
    _StpxMSTInstanceRemainingHopCount_Type()
)
stpxMSTInstanceRemainingHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxMSTInstanceRemainingHopCount.setStatus("deprecated")


class _StpxMSTRegionEditBufferStatus_Type(Integer32):
    """Custom type stpxMSTRegionEditBufferStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acquiredByNonSnmp", 3),
          ("acquiredBySnmp", 2),
          ("released", 1))
    )


_StpxMSTRegionEditBufferStatus_Type.__name__ = "Integer32"
_StpxMSTRegionEditBufferStatus_Object = MibScalar
stpxMSTRegionEditBufferStatus = _StpxMSTRegionEditBufferStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 5),
    _StpxMSTRegionEditBufferStatus_Type()
)
stpxMSTRegionEditBufferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxMSTRegionEditBufferStatus.setStatus("current")


class _StpxMSTRegionEditBufferOperation_Type(Integer32):
    """Custom type stpxMSTRegionEditBufferOperation based on Integer32"""
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
        *(("acquire", 2),
          ("commit", 4),
          ("other", 1),
          ("releaseWithForce", 3),
          ("rollBack", 5))
    )


_StpxMSTRegionEditBufferOperation_Type.__name__ = "Integer32"
_StpxMSTRegionEditBufferOperation_Object = MibScalar
stpxMSTRegionEditBufferOperation = _StpxMSTRegionEditBufferOperation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 6),
    _StpxMSTRegionEditBufferOperation_Type()
)
stpxMSTRegionEditBufferOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxMSTRegionEditBufferOperation.setStatus("current")


class _StpxMSTRegionEditName_Type(DisplayString):
    """Custom type stpxMSTRegionEditName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StpxMSTRegionEditName_Type.__name__ = "DisplayString"
_StpxMSTRegionEditName_Object = MibScalar
stpxMSTRegionEditName = _StpxMSTRegionEditName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 7),
    _StpxMSTRegionEditName_Type()
)
stpxMSTRegionEditName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxMSTRegionEditName.setStatus("current")


class _StpxMSTRegionEditRevision_Type(Integer32):
    """Custom type stpxMSTRegionEditRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StpxMSTRegionEditRevision_Type.__name__ = "Integer32"
_StpxMSTRegionEditRevision_Object = MibScalar
stpxMSTRegionEditRevision = _StpxMSTRegionEditRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 8),
    _StpxMSTRegionEditRevision_Type()
)
stpxMSTRegionEditRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxMSTRegionEditRevision.setStatus("deprecated")
_StpxMSTInstanceEditTable_Object = MibTable
stpxMSTInstanceEditTable = _StpxMSTInstanceEditTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 9)
)
if mibBuilder.loadTexts:
    stpxMSTInstanceEditTable.setStatus("deprecated")
_StpxMSTInstanceEditEntry_Object = MibTableRow
stpxMSTInstanceEditEntry = _StpxMSTInstanceEditEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 9, 1)
)
stpxMSTInstanceEditEntry.setIndexNames(
    (0, "CISCO-STP-EXTENSIONS-MIB", "stpxMSTInstanceEditIndex"),
)
if mibBuilder.loadTexts:
    stpxMSTInstanceEditEntry.setStatus("deprecated")


class _StpxMSTInstanceEditIndex_Type(Integer32):
    """Custom type stpxMSTInstanceEditIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_StpxMSTInstanceEditIndex_Type.__name__ = "Integer32"
_StpxMSTInstanceEditIndex_Object = MibTableColumn
stpxMSTInstanceEditIndex = _StpxMSTInstanceEditIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 9, 1, 1),
    _StpxMSTInstanceEditIndex_Type()
)
stpxMSTInstanceEditIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpxMSTInstanceEditIndex.setStatus("deprecated")


class _StpxMSTInstanceEditVlansMap_Type(OctetString):
    """Custom type stpxMSTInstanceEditVlansMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_StpxMSTInstanceEditVlansMap_Type.__name__ = "OctetString"
_StpxMSTInstanceEditVlansMap_Object = MibTableColumn
stpxMSTInstanceEditVlansMap = _StpxMSTInstanceEditVlansMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 9, 1, 2),
    _StpxMSTInstanceEditVlansMap_Type()
)
stpxMSTInstanceEditVlansMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxMSTInstanceEditVlansMap.setStatus("deprecated")


class _StpxMSTInstanceEditVlansMap2k_Type(OctetString):
    """Custom type stpxMSTInstanceEditVlansMap2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_StpxMSTInstanceEditVlansMap2k_Type.__name__ = "OctetString"
_StpxMSTInstanceEditVlansMap2k_Object = MibTableColumn
stpxMSTInstanceEditVlansMap2k = _StpxMSTInstanceEditVlansMap2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 9, 1, 3),
    _StpxMSTInstanceEditVlansMap2k_Type()
)
stpxMSTInstanceEditVlansMap2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxMSTInstanceEditVlansMap2k.setStatus("deprecated")


class _StpxMSTInstanceEditVlansMap3k_Type(OctetString):
    """Custom type stpxMSTInstanceEditVlansMap3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_StpxMSTInstanceEditVlansMap3k_Type.__name__ = "OctetString"
_StpxMSTInstanceEditVlansMap3k_Object = MibTableColumn
stpxMSTInstanceEditVlansMap3k = _StpxMSTInstanceEditVlansMap3k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 9, 1, 4),
    _StpxMSTInstanceEditVlansMap3k_Type()
)
stpxMSTInstanceEditVlansMap3k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxMSTInstanceEditVlansMap3k.setStatus("deprecated")


class _StpxMSTInstanceEditVlansMap4k_Type(OctetString):
    """Custom type stpxMSTInstanceEditVlansMap4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_StpxMSTInstanceEditVlansMap4k_Type.__name__ = "OctetString"
_StpxMSTInstanceEditVlansMap4k_Object = MibTableColumn
stpxMSTInstanceEditVlansMap4k = _StpxMSTInstanceEditVlansMap4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 9, 1, 5),
    _StpxMSTInstanceEditVlansMap4k_Type()
)
stpxMSTInstanceEditVlansMap4k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxMSTInstanceEditVlansMap4k.setStatus("deprecated")
_StpxPreferredMSTInstancesTable_Object = MibTable
stpxPreferredMSTInstancesTable = _StpxPreferredMSTInstancesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 10)
)
if mibBuilder.loadTexts:
    stpxPreferredMSTInstancesTable.setStatus("deprecated")
_StpxPreferredMSTInstancesEntry_Object = MibTableRow
stpxPreferredMSTInstancesEntry = _StpxPreferredMSTInstancesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 10, 1)
)
if mibBuilder.loadTexts:
    stpxPreferredMSTInstancesEntry.setStatus("deprecated")


class _StpxPreferredMSTInstancesMap_Type(OctetString):
    """Custom type stpxPreferredMSTInstancesMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_StpxPreferredMSTInstancesMap_Type.__name__ = "OctetString"
_StpxPreferredMSTInstancesMap_Object = MibTableColumn
stpxPreferredMSTInstancesMap = _StpxPreferredMSTInstancesMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 10, 1, 1),
    _StpxPreferredMSTInstancesMap_Type()
)
stpxPreferredMSTInstancesMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxPreferredMSTInstancesMap.setStatus("deprecated")
_StpxMSTPortTable_Object = MibTable
stpxMSTPortTable = _StpxMSTPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 11)
)
if mibBuilder.loadTexts:
    stpxMSTPortTable.setStatus("deprecated")
_StpxMSTPortEntry_Object = MibTableRow
stpxMSTPortEntry = _StpxMSTPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 11, 1)
)
stpxMSTPortEntry.setIndexNames(
    (0, "CISCO-STP-EXTENSIONS-MIB", "stpxMSTPortIndex"),
)
if mibBuilder.loadTexts:
    stpxMSTPortEntry.setStatus("deprecated")


class _StpxMSTPortIndex_Type(Integer32):
    """Custom type stpxMSTPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StpxMSTPortIndex_Type.__name__ = "Integer32"
_StpxMSTPortIndex_Object = MibTableColumn
stpxMSTPortIndex = _StpxMSTPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 11, 1, 1),
    _StpxMSTPortIndex_Type()
)
stpxMSTPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpxMSTPortIndex.setStatus("deprecated")


class _StpxMSTPortAdminLinkType_Type(Integer32):
    """Custom type stpxMSTPortAdminLinkType based on Integer32"""
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
          ("pointToPoint", 1),
          ("shared", 2))
    )


_StpxMSTPortAdminLinkType_Type.__name__ = "Integer32"
_StpxMSTPortAdminLinkType_Object = MibTableColumn
stpxMSTPortAdminLinkType = _StpxMSTPortAdminLinkType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 11, 1, 2),
    _StpxMSTPortAdminLinkType_Type()
)
stpxMSTPortAdminLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxMSTPortAdminLinkType.setStatus("deprecated")


class _StpxMSTPortOperLinkType_Type(Integer32):
    """Custom type stpxMSTPortOperLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 3),
          ("pointToPoint", 1),
          ("shared", 2))
    )


_StpxMSTPortOperLinkType_Type.__name__ = "Integer32"
_StpxMSTPortOperLinkType_Object = MibTableColumn
stpxMSTPortOperLinkType = _StpxMSTPortOperLinkType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 11, 1, 3),
    _StpxMSTPortOperLinkType_Type()
)
stpxMSTPortOperLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxMSTPortOperLinkType.setStatus("deprecated")
_StpxMSTPortProtocolMigration_Type = TruthValue
_StpxMSTPortProtocolMigration_Object = MibTableColumn
stpxMSTPortProtocolMigration = _StpxMSTPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 11, 1, 4),
    _StpxMSTPortProtocolMigration_Type()
)
stpxMSTPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxMSTPortProtocolMigration.setStatus("deprecated")


class _StpxMSTPortStatus_Type(Bits):
    """Custom type stpxMSTPortStatus based on Bits"""
    namedValues = NamedValues(
        *(("boundary", 1),
          ("edge", 0),
          ("pvst", 2),
          ("stp", 3))
    )

_StpxMSTPortStatus_Type.__name__ = "Bits"
_StpxMSTPortStatus_Object = MibTableColumn
stpxMSTPortStatus = _StpxMSTPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 11, 1, 5),
    _StpxMSTPortStatus_Type()
)
stpxMSTPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxMSTPortStatus.setStatus("deprecated")
_StpxMSTPortRoleTable_Object = MibTable
stpxMSTPortRoleTable = _StpxMSTPortRoleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 12)
)
if mibBuilder.loadTexts:
    stpxMSTPortRoleTable.setStatus("deprecated")
_StpxMSTPortRoleEntry_Object = MibTableRow
stpxMSTPortRoleEntry = _StpxMSTPortRoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 12, 1)
)
stpxMSTPortRoleEntry.setIndexNames(
    (0, "CISCO-STP-EXTENSIONS-MIB", "stpxMSTPortRoleInstanceIndex"),
    (0, "CISCO-STP-EXTENSIONS-MIB", "stpxMSTPortRolePortIndex"),
)
if mibBuilder.loadTexts:
    stpxMSTPortRoleEntry.setStatus("deprecated")


class _StpxMSTPortRoleInstanceIndex_Type(Integer32):
    """Custom type stpxMSTPortRoleInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_StpxMSTPortRoleInstanceIndex_Type.__name__ = "Integer32"
_StpxMSTPortRoleInstanceIndex_Object = MibTableColumn
stpxMSTPortRoleInstanceIndex = _StpxMSTPortRoleInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 12, 1, 1),
    _StpxMSTPortRoleInstanceIndex_Type()
)
stpxMSTPortRoleInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpxMSTPortRoleInstanceIndex.setStatus("deprecated")


class _StpxMSTPortRolePortIndex_Type(Integer32):
    """Custom type stpxMSTPortRolePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StpxMSTPortRolePortIndex_Type.__name__ = "Integer32"
_StpxMSTPortRolePortIndex_Object = MibTableColumn
stpxMSTPortRolePortIndex = _StpxMSTPortRolePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 12, 1, 2),
    _StpxMSTPortRolePortIndex_Type()
)
stpxMSTPortRolePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpxMSTPortRolePortIndex.setStatus("deprecated")


class _StpxMSTPortRoleValue_Type(Integer32):
    """Custom type stpxMSTPortRoleValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 4),
          ("backUp", 5),
          ("boundary", 6),
          ("designated", 3),
          ("disabled", 1),
          ("master", 7),
          ("root", 2))
    )


_StpxMSTPortRoleValue_Type.__name__ = "Integer32"
_StpxMSTPortRoleValue_Object = MibTableColumn
stpxMSTPortRoleValue = _StpxMSTPortRoleValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 12, 1, 3),
    _StpxMSTPortRoleValue_Type()
)
stpxMSTPortRoleValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxMSTPortRoleValue.setStatus("deprecated")


class _StpxMSTMaxHopCount_Type(Integer32):
    """Custom type stpxMSTMaxHopCount based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_StpxMSTMaxHopCount_Type.__name__ = "Integer32"
_StpxMSTMaxHopCount_Object = MibScalar
stpxMSTMaxHopCount = _StpxMSTMaxHopCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 11, 13),
    _StpxMSTMaxHopCount_Type()
)
stpxMSTMaxHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxMSTMaxHopCount.setStatus("deprecated")
_StpxRSTPObjects_ObjectIdentity = ObjectIdentity
stpxRSTPObjects = _StpxRSTPObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 12)
)
_StpxRSTPPortTable_Object = MibTable
stpxRSTPPortTable = _StpxRSTPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 12, 1)
)
if mibBuilder.loadTexts:
    stpxRSTPPortTable.setStatus("current")
_StpxRSTPPortEntry_Object = MibTableRow
stpxRSTPPortEntry = _StpxRSTPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 12, 1, 1)
)
stpxRSTPPortEntry.setIndexNames(
    (0, "CISCO-STP-EXTENSIONS-MIB", "stpxRSTPPortIndex"),
)
if mibBuilder.loadTexts:
    stpxRSTPPortEntry.setStatus("current")


class _StpxRSTPPortIndex_Type(Integer32):
    """Custom type stpxRSTPPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StpxRSTPPortIndex_Type.__name__ = "Integer32"
_StpxRSTPPortIndex_Object = MibTableColumn
stpxRSTPPortIndex = _StpxRSTPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 12, 1, 1, 1),
    _StpxRSTPPortIndex_Type()
)
stpxRSTPPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpxRSTPPortIndex.setStatus("current")


class _StpxRSTPPortAdminLinkType_Type(Integer32):
    """Custom type stpxRSTPPortAdminLinkType based on Integer32"""
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
          ("pointToPoint", 1),
          ("shared", 2))
    )


_StpxRSTPPortAdminLinkType_Type.__name__ = "Integer32"
_StpxRSTPPortAdminLinkType_Object = MibTableColumn
stpxRSTPPortAdminLinkType = _StpxRSTPPortAdminLinkType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 12, 1, 1, 2),
    _StpxRSTPPortAdminLinkType_Type()
)
stpxRSTPPortAdminLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxRSTPPortAdminLinkType.setStatus("current")


class _StpxRSTPPortOperLinkType_Type(Integer32):
    """Custom type stpxRSTPPortOperLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 3),
          ("pointToPoint", 1),
          ("shared", 2))
    )


_StpxRSTPPortOperLinkType_Type.__name__ = "Integer32"
_StpxRSTPPortOperLinkType_Object = MibTableColumn
stpxRSTPPortOperLinkType = _StpxRSTPPortOperLinkType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 12, 1, 1, 3),
    _StpxRSTPPortOperLinkType_Type()
)
stpxRSTPPortOperLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxRSTPPortOperLinkType.setStatus("current")
_StpxRSTPPortProtocolMigration_Type = TruthValue
_StpxRSTPPortProtocolMigration_Object = MibTableColumn
stpxRSTPPortProtocolMigration = _StpxRSTPPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 12, 1, 1, 4),
    _StpxRSTPPortProtocolMigration_Type()
)
stpxRSTPPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxRSTPPortProtocolMigration.setStatus("current")
_StpxRSTPPortRoleTable_Object = MibTable
stpxRSTPPortRoleTable = _StpxRSTPPortRoleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 12, 2)
)
if mibBuilder.loadTexts:
    stpxRSTPPortRoleTable.setStatus("current")
_StpxRSTPPortRoleEntry_Object = MibTableRow
stpxRSTPPortRoleEntry = _StpxRSTPPortRoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 12, 2, 1)
)
stpxRSTPPortRoleEntry.setIndexNames(
    (0, "CISCO-STP-EXTENSIONS-MIB", "stpxRSTPPortRoleInstanceIndex"),
    (0, "CISCO-STP-EXTENSIONS-MIB", "stpxRSTPPortRolePortIndex"),
)
if mibBuilder.loadTexts:
    stpxRSTPPortRoleEntry.setStatus("current")


class _StpxRSTPPortRoleInstanceIndex_Type(Integer32):
    """Custom type stpxRSTPPortRoleInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_StpxRSTPPortRoleInstanceIndex_Type.__name__ = "Integer32"
_StpxRSTPPortRoleInstanceIndex_Object = MibTableColumn
stpxRSTPPortRoleInstanceIndex = _StpxRSTPPortRoleInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 12, 2, 1, 1),
    _StpxRSTPPortRoleInstanceIndex_Type()
)
stpxRSTPPortRoleInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpxRSTPPortRoleInstanceIndex.setStatus("current")


class _StpxRSTPPortRolePortIndex_Type(Integer32):
    """Custom type stpxRSTPPortRolePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StpxRSTPPortRolePortIndex_Type.__name__ = "Integer32"
_StpxRSTPPortRolePortIndex_Object = MibTableColumn
stpxRSTPPortRolePortIndex = _StpxRSTPPortRolePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 12, 2, 1, 2),
    _StpxRSTPPortRolePortIndex_Type()
)
stpxRSTPPortRolePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpxRSTPPortRolePortIndex.setStatus("current")


class _StpxRSTPPortRoleValue_Type(Integer32):
    """Custom type stpxRSTPPortRoleValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 4),
          ("backUp", 5),
          ("boundary", 6),
          ("designated", 3),
          ("disabled", 1),
          ("master", 7),
          ("root", 2))
    )


_StpxRSTPPortRoleValue_Type.__name__ = "Integer32"
_StpxRSTPPortRoleValue_Object = MibTableColumn
stpxRSTPPortRoleValue = _StpxRSTPPortRoleValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 12, 2, 1, 3),
    _StpxRSTPPortRoleValue_Type()
)
stpxRSTPPortRoleValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxRSTPPortRoleValue.setStatus("current")
_StpxRSTPTransmitHoldCount_Type = Unsigned32
_StpxRSTPTransmitHoldCount_Object = MibScalar
stpxRSTPTransmitHoldCount = _StpxRSTPTransmitHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 12, 3),
    _StpxRSTPTransmitHoldCount_Type()
)
stpxRSTPTransmitHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxRSTPTransmitHoldCount.setStatus("current")
_StpxRPVSTObjects_ObjectIdentity = ObjectIdentity
stpxRPVSTObjects = _StpxRPVSTObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 13)
)
_StpxRPVSTPortTable_Object = MibTable
stpxRPVSTPortTable = _StpxRPVSTPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 13, 1)
)
if mibBuilder.loadTexts:
    stpxRPVSTPortTable.setStatus("current")
_StpxRPVSTPortEntry_Object = MibTableRow
stpxRPVSTPortEntry = _StpxRPVSTPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 13, 1, 1)
)
stpxRPVSTPortEntry.setIndexNames(
    (0, "CISCO-STP-EXTENSIONS-MIB", "stpxRPVSTPortVlanIndex"),
    (0, "CISCO-STP-EXTENSIONS-MIB", "stpxRPVSTPortIndex"),
)
if mibBuilder.loadTexts:
    stpxRPVSTPortEntry.setStatus("current")
_StpxRPVSTPortVlanIndex_Type = VlanIndex
_StpxRPVSTPortVlanIndex_Object = MibTableColumn
stpxRPVSTPortVlanIndex = _StpxRPVSTPortVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 13, 1, 1, 1),
    _StpxRPVSTPortVlanIndex_Type()
)
stpxRPVSTPortVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpxRPVSTPortVlanIndex.setStatus("current")


class _StpxRPVSTPortIndex_Type(Integer32):
    """Custom type stpxRPVSTPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StpxRPVSTPortIndex_Type.__name__ = "Integer32"
_StpxRPVSTPortIndex_Object = MibTableColumn
stpxRPVSTPortIndex = _StpxRPVSTPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 13, 1, 1, 2),
    _StpxRPVSTPortIndex_Type()
)
stpxRPVSTPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpxRPVSTPortIndex.setStatus("current")


class _StpxRPVSTPortStatus_Type(Bits):
    """Custom type stpxRPVSTPortStatus based on Bits"""
    namedValues = NamedValues(
        *(("dispute", 4),
          ("edge", 0),
          ("stp", 3),
          ("unused1", 1),
          ("unused2", 2))
    )

_StpxRPVSTPortStatus_Type.__name__ = "Bits"
_StpxRPVSTPortStatus_Object = MibTableColumn
stpxRPVSTPortStatus = _StpxRPVSTPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 13, 1, 1, 3),
    _StpxRPVSTPortStatus_Type()
)
stpxRPVSTPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxRPVSTPortStatus.setStatus("current")
_StpxSMSTObjects_ObjectIdentity = ObjectIdentity
stpxSMSTObjects = _StpxSMSTObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14)
)
_StpxSMSTMaxInstances_Type = Unsigned32
_StpxSMSTMaxInstances_Object = MibScalar
stpxSMSTMaxInstances = _StpxSMSTMaxInstances_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14, 1),
    _StpxSMSTMaxInstances_Type()
)
stpxSMSTMaxInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxSMSTMaxInstances.setStatus("current")
_StpxSMSTMaxInstanceID_Type = Unsigned32
_StpxSMSTMaxInstanceID_Object = MibScalar
stpxSMSTMaxInstanceID = _StpxSMSTMaxInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14, 2),
    _StpxSMSTMaxInstanceID_Type()
)
stpxSMSTMaxInstanceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxSMSTMaxInstanceID.setStatus("current")
_StpxSMSTRegionRevision_Type = Unsigned32
_StpxSMSTRegionRevision_Object = MibScalar
stpxSMSTRegionRevision = _StpxSMSTRegionRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14, 3),
    _StpxSMSTRegionRevision_Type()
)
stpxSMSTRegionRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxSMSTRegionRevision.setStatus("current")
_StpxSMSTRegionEditRevision_Type = Unsigned32
_StpxSMSTRegionEditRevision_Object = MibScalar
stpxSMSTRegionEditRevision = _StpxSMSTRegionEditRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14, 4),
    _StpxSMSTRegionEditRevision_Type()
)
stpxSMSTRegionEditRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxSMSTRegionEditRevision.setStatus("current")
_StpxSMSTInstanceTable_Object = MibTable
stpxSMSTInstanceTable = _StpxSMSTInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14, 5)
)
if mibBuilder.loadTexts:
    stpxSMSTInstanceTable.setStatus("current")
_StpxSMSTInstanceEntry_Object = MibTableRow
stpxSMSTInstanceEntry = _StpxSMSTInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14, 5, 1)
)
stpxSMSTInstanceEntry.setIndexNames(
    (0, "CISCO-STP-EXTENSIONS-MIB", "stpxSMSTInstanceIndex"),
)
if mibBuilder.loadTexts:
    stpxSMSTInstanceEntry.setStatus("current")
_StpxSMSTInstanceIndex_Type = Unsigned32
_StpxSMSTInstanceIndex_Object = MibTableColumn
stpxSMSTInstanceIndex = _StpxSMSTInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14, 5, 1, 1),
    _StpxSMSTInstanceIndex_Type()
)
stpxSMSTInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpxSMSTInstanceIndex.setStatus("current")


class _StpxSMSTInstanceVlansMapped1k2k_Type(OctetString):
    """Custom type stpxSMSTInstanceVlansMapped1k2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_StpxSMSTInstanceVlansMapped1k2k_Type.__name__ = "OctetString"
_StpxSMSTInstanceVlansMapped1k2k_Object = MibTableColumn
stpxSMSTInstanceVlansMapped1k2k = _StpxSMSTInstanceVlansMapped1k2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14, 5, 1, 2),
    _StpxSMSTInstanceVlansMapped1k2k_Type()
)
stpxSMSTInstanceVlansMapped1k2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxSMSTInstanceVlansMapped1k2k.setStatus("current")


class _StpxSMSTInstanceVlansMapped3k4k_Type(OctetString):
    """Custom type stpxSMSTInstanceVlansMapped3k4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_StpxSMSTInstanceVlansMapped3k4k_Type.__name__ = "OctetString"
_StpxSMSTInstanceVlansMapped3k4k_Object = MibTableColumn
stpxSMSTInstanceVlansMapped3k4k = _StpxSMSTInstanceVlansMapped3k4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14, 5, 1, 3),
    _StpxSMSTInstanceVlansMapped3k4k_Type()
)
stpxSMSTInstanceVlansMapped3k4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxSMSTInstanceVlansMapped3k4k.setStatus("current")


class _StpxSMSTInstanceRemainingHopCount_Type(Integer32):
    """Custom type stpxSMSTInstanceRemainingHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_StpxSMSTInstanceRemainingHopCount_Type.__name__ = "Integer32"
_StpxSMSTInstanceRemainingHopCount_Object = MibTableColumn
stpxSMSTInstanceRemainingHopCount = _StpxSMSTInstanceRemainingHopCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14, 5, 1, 4),
    _StpxSMSTInstanceRemainingHopCount_Type()
)
stpxSMSTInstanceRemainingHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxSMSTInstanceRemainingHopCount.setStatus("current")


class _StpxSMSTInstanceCISTRegionalRoot_Type(OctetString):
    """Custom type stpxSMSTInstanceCISTRegionalRoot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_StpxSMSTInstanceCISTRegionalRoot_Type.__name__ = "OctetString"
_StpxSMSTInstanceCISTRegionalRoot_Object = MibTableColumn
stpxSMSTInstanceCISTRegionalRoot = _StpxSMSTInstanceCISTRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14, 5, 1, 5),
    _StpxSMSTInstanceCISTRegionalRoot_Type()
)
stpxSMSTInstanceCISTRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxSMSTInstanceCISTRegionalRoot.setStatus("current")
_StpxSMSTInstanceCISTIntRootCost_Type = Unsigned32
_StpxSMSTInstanceCISTIntRootCost_Object = MibTableColumn
stpxSMSTInstanceCISTIntRootCost = _StpxSMSTInstanceCISTIntRootCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14, 5, 1, 6),
    _StpxSMSTInstanceCISTIntRootCost_Type()
)
stpxSMSTInstanceCISTIntRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxSMSTInstanceCISTIntRootCost.setStatus("current")
_StpxSMSTInstanceEditTable_Object = MibTable
stpxSMSTInstanceEditTable = _StpxSMSTInstanceEditTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14, 6)
)
if mibBuilder.loadTexts:
    stpxSMSTInstanceEditTable.setStatus("current")
_StpxSMSTInstanceEditEntry_Object = MibTableRow
stpxSMSTInstanceEditEntry = _StpxSMSTInstanceEditEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14, 6, 1)
)
stpxSMSTInstanceEditEntry.setIndexNames(
    (0, "CISCO-STP-EXTENSIONS-MIB", "stpxSMSTInstanceEditIndex"),
)
if mibBuilder.loadTexts:
    stpxSMSTInstanceEditEntry.setStatus("current")
_StpxSMSTInstanceEditIndex_Type = Unsigned32
_StpxSMSTInstanceEditIndex_Object = MibTableColumn
stpxSMSTInstanceEditIndex = _StpxSMSTInstanceEditIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14, 6, 1, 1),
    _StpxSMSTInstanceEditIndex_Type()
)
stpxSMSTInstanceEditIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpxSMSTInstanceEditIndex.setStatus("current")


class _StpxSMSTInstanceEditVlansMap1k2k_Type(OctetString):
    """Custom type stpxSMSTInstanceEditVlansMap1k2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_StpxSMSTInstanceEditVlansMap1k2k_Type.__name__ = "OctetString"
_StpxSMSTInstanceEditVlansMap1k2k_Object = MibTableColumn
stpxSMSTInstanceEditVlansMap1k2k = _StpxSMSTInstanceEditVlansMap1k2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14, 6, 1, 2),
    _StpxSMSTInstanceEditVlansMap1k2k_Type()
)
stpxSMSTInstanceEditVlansMap1k2k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stpxSMSTInstanceEditVlansMap1k2k.setStatus("current")


class _StpxSMSTInstanceEditVlansMap3k4k_Type(OctetString):
    """Custom type stpxSMSTInstanceEditVlansMap3k4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_StpxSMSTInstanceEditVlansMap3k4k_Type.__name__ = "OctetString"
_StpxSMSTInstanceEditVlansMap3k4k_Object = MibTableColumn
stpxSMSTInstanceEditVlansMap3k4k = _StpxSMSTInstanceEditVlansMap3k4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14, 6, 1, 3),
    _StpxSMSTInstanceEditVlansMap3k4k_Type()
)
stpxSMSTInstanceEditVlansMap3k4k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stpxSMSTInstanceEditVlansMap3k4k.setStatus("current")
_StpxSMSTInstanceEditRowStatus_Type = RowStatus
_StpxSMSTInstanceEditRowStatus_Object = MibTableColumn
stpxSMSTInstanceEditRowStatus = _StpxSMSTInstanceEditRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14, 6, 1, 4),
    _StpxSMSTInstanceEditRowStatus_Type()
)
stpxSMSTInstanceEditRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stpxSMSTInstanceEditRowStatus.setStatus("current")
_StpxSMSTPortTable_Object = MibTable
stpxSMSTPortTable = _StpxSMSTPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14, 7)
)
if mibBuilder.loadTexts:
    stpxSMSTPortTable.setStatus("current")
_StpxSMSTPortEntry_Object = MibTableRow
stpxSMSTPortEntry = _StpxSMSTPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14, 7, 1)
)
stpxSMSTPortEntry.setIndexNames(
    (0, "CISCO-STP-EXTENSIONS-MIB", "stpxSMSTPortIndex"),
)
if mibBuilder.loadTexts:
    stpxSMSTPortEntry.setStatus("current")


class _StpxSMSTPortIndex_Type(Integer32):
    """Custom type stpxSMSTPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StpxSMSTPortIndex_Type.__name__ = "Integer32"
_StpxSMSTPortIndex_Object = MibTableColumn
stpxSMSTPortIndex = _StpxSMSTPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14, 7, 1, 1),
    _StpxSMSTPortIndex_Type()
)
stpxSMSTPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpxSMSTPortIndex.setStatus("current")


class _StpxSMSTPortStatus_Type(Bits):
    """Custom type stpxSMSTPortStatus based on Bits"""
    namedValues = NamedValues(
        *(("boundary", 1),
          ("dispute", 4),
          ("edge", 0),
          ("pvst", 2),
          ("rstp", 5),
          ("stp", 3))
    )

_StpxSMSTPortStatus_Type.__name__ = "Bits"
_StpxSMSTPortStatus_Object = MibTableColumn
stpxSMSTPortStatus = _StpxSMSTPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14, 7, 1, 2),
    _StpxSMSTPortStatus_Type()
)
stpxSMSTPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxSMSTPortStatus.setStatus("current")
_StpxSMSTPortAdminHelloTime_Type = Unsigned32
_StpxSMSTPortAdminHelloTime_Object = MibTableColumn
stpxSMSTPortAdminHelloTime = _StpxSMSTPortAdminHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14, 7, 1, 3),
    _StpxSMSTPortAdminHelloTime_Type()
)
stpxSMSTPortAdminHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxSMSTPortAdminHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    stpxSMSTPortAdminHelloTime.setUnits("hundredth of seconds")
_StpxSMSTPortConfigedHelloTime_Type = Unsigned32
_StpxSMSTPortConfigedHelloTime_Object = MibTableColumn
stpxSMSTPortConfigedHelloTime = _StpxSMSTPortConfigedHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14, 7, 1, 4),
    _StpxSMSTPortConfigedHelloTime_Type()
)
stpxSMSTPortConfigedHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxSMSTPortConfigedHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    stpxSMSTPortConfigedHelloTime.setUnits("hundredth of seconds")


class _StpxSMSTPortOperHelloTime_Type(Integer32):
    """Custom type stpxSMSTPortOperHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_StpxSMSTPortOperHelloTime_Type.__name__ = "Integer32"
_StpxSMSTPortOperHelloTime_Object = MibTableColumn
stpxSMSTPortOperHelloTime = _StpxSMSTPortOperHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14, 7, 1, 5),
    _StpxSMSTPortOperHelloTime_Type()
)
stpxSMSTPortOperHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxSMSTPortOperHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    stpxSMSTPortOperHelloTime.setUnits("hundredth of seconds")


class _StpxSMSTPortAdminMSTMode_Type(Integer32):
    """Custom type stpxSMSTPortAdminMSTMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("preStandard", 1))
    )


_StpxSMSTPortAdminMSTMode_Type.__name__ = "Integer32"
_StpxSMSTPortAdminMSTMode_Object = MibTableColumn
stpxSMSTPortAdminMSTMode = _StpxSMSTPortAdminMSTMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14, 7, 1, 6),
    _StpxSMSTPortAdminMSTMode_Type()
)
stpxSMSTPortAdminMSTMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxSMSTPortAdminMSTMode.setStatus("current")


class _StpxSMSTPortOperMSTMode_Type(Integer32):
    """Custom type stpxSMSTPortOperMSTMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("preStandard", 2),
          ("standard", 3),
          ("unknown", 1))
    )


_StpxSMSTPortOperMSTMode_Type.__name__ = "Integer32"
_StpxSMSTPortOperMSTMode_Object = MibTableColumn
stpxSMSTPortOperMSTMode = _StpxSMSTPortOperMSTMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14, 7, 1, 7),
    _StpxSMSTPortOperMSTMode_Type()
)
stpxSMSTPortOperMSTMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxSMSTPortOperMSTMode.setStatus("current")
_StpxSMSTMaxHopCount_Type = Unsigned32
_StpxSMSTMaxHopCount_Object = MibScalar
stpxSMSTMaxHopCount = _StpxSMSTMaxHopCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14, 8),
    _StpxSMSTMaxHopCount_Type()
)
stpxSMSTMaxHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpxSMSTMaxHopCount.setStatus("current")
_StpxSMSTConfigDigest_Type = StpxMSTConfigurationDigest
_StpxSMSTConfigDigest_Object = MibScalar
stpxSMSTConfigDigest = _StpxSMSTConfigDigest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14, 9),
    _StpxSMSTConfigDigest_Type()
)
stpxSMSTConfigDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxSMSTConfigDigest.setStatus("current")
_StpxSMSTConfigPreStandardDigest_Type = StpxMSTConfigurationDigest
_StpxSMSTConfigPreStandardDigest_Object = MibScalar
stpxSMSTConfigPreStandardDigest = _StpxSMSTConfigPreStandardDigest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 1, 14, 10),
    _StpxSMSTConfigPreStandardDigest_Type()
)
stpxSMSTConfigPreStandardDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpxSMSTConfigPreStandardDigest.setStatus("current")
_StpxNotifications_ObjectIdentity = ObjectIdentity
stpxNotifications = _StpxNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 2)
)
_StpxNotificationsPrefix_ObjectIdentity = ObjectIdentity
stpxNotificationsPrefix = _StpxNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 2, 0)
)
_StpxMIBConformance_ObjectIdentity = ObjectIdentity
stpxMIBConformance = _StpxMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3)
)
_StpxMIBCompliances_ObjectIdentity = ObjectIdentity
stpxMIBCompliances = _StpxMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 1)
)
_StpxMIBGroups_ObjectIdentity = ObjectIdentity
stpxMIBGroups = _StpxMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2)
)
vlanTrunkPortEntry.registerAugmentions(
    ("CISCO-STP-EXTENSIONS-MIB",
     "stpxPreferredVlansEntry")
)
stpxPreferredVlansEntry.setIndexNames(*vlanTrunkPortEntry.getIndexNames())
dot1dStpPortEntry.registerAugmentions(
    ("CISCO-STP-EXTENSIONS-MIB",
     "stpxLongStpPortPathCostEntry")
)
stpxLongStpPortPathCostEntry.setIndexNames(*dot1dStpPortEntry.getIndexNames())
vtpVlanEntry.registerAugmentions(
    ("CISCO-STP-EXTENSIONS-MIB",
     "stpxVlanMISTPInstMapEntry")
)
stpxVlanMISTPInstMapEntry.setIndexNames(*vtpVlanEntry.getIndexNames())
vtpVlanEditEntry.registerAugmentions(
    ("CISCO-STP-EXTENSIONS-MIB",
     "stpxVlanMISTPInstMapEditEntry")
)
stpxVlanMISTPInstMapEditEntry.setIndexNames(*vtpVlanEditEntry.getIndexNames())
vlanTrunkPortEntry.registerAugmentions(
    ("CISCO-STP-EXTENSIONS-MIB",
     "stpxPreferredMISTPInstancesEntry")
)
stpxPreferredMISTPInstancesEntry.setIndexNames(*vlanTrunkPortEntry.getIndexNames())
vlanTrunkPortEntry.registerAugmentions(
    ("CISCO-STP-EXTENSIONS-MIB",
     "stpxPreferredMSTInstancesEntry")
)
stpxPreferredMSTInstancesEntry.setIndexNames(*vlanTrunkPortEntry.getIndexNames())

# Managed Objects groups

stpxUplinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 1)
)
stpxUplinkGroup.setObjects(
      *(("CISCO-STP-EXTENSIONS-MIB", "stpxUplinkFastEnabled"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxUplinkFastTransitions"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxUplinkStationLearningGenRate"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxUplinkStationLearningFrames"))
)
if mibBuilder.loadTexts:
    stpxUplinkGroup.setStatus("current")

stpxPreferredVlansGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 2)
)
stpxPreferredVlansGroup.setObjects(
    ("CISCO-STP-EXTENSIONS-MIB", "stpxPreferredVlansMap")
)
if mibBuilder.loadTexts:
    stpxPreferredVlansGroup.setStatus("current")

stpxSstpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 3)
)
stpxSstpGroup.setObjects(
    ("CISCO-STP-EXTENSIONS-MIB", "stpxInconsistentState")
)
if mibBuilder.loadTexts:
    stpxSstpGroup.setStatus("current")

stpxBackboneGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 5)
)
stpxBackboneGroup.setObjects(
      *(("CISCO-STP-EXTENSIONS-MIB", "stpxBackboneFastEnabled"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxBackboneFastInInferiorBPDUs"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxBackboneFastInRLQRequestPDUs"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxBackboneFastInRLQResponsePDUs"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxBackboneFastOutRLQRequestPDUs"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxBackboneFastOutRLQResponsePDUs"))
)
if mibBuilder.loadTexts:
    stpxBackboneGroup.setStatus("current")

stpxRootGuardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 6)
)
stpxRootGuardGroup.setObjects(
      *(("CISCO-STP-EXTENSIONS-MIB", "stpxRootGuardConfigEnabled"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxRootInconsistencyState"))
)
if mibBuilder.loadTexts:
    stpxRootGuardGroup.setStatus("current")

stpx4kVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 8)
)
stpx4kVlanGroup.setObjects(
      *(("CISCO-STP-EXTENSIONS-MIB", "stpxPreferredVlansMap2k"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxPreferredVlansMap3k"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxPreferredVlansMap4k"))
)
if mibBuilder.loadTexts:
    stpx4kVlanGroup.setStatus("current")

stpxSpanningTreeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 9)
)
stpxSpanningTreeGroup.setObjects(
    ("CISCO-STP-EXTENSIONS-MIB", "stpxSpanningTreeType")
)
if mibBuilder.loadTexts:
    stpxSpanningTreeGroup.setStatus("current")

stpxMISTPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 10)
)
stpxMISTPGroup.setObjects(
      *(("CISCO-STP-EXTENSIONS-MIB", "stpxMISTPInstanceNumber"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMISTPInstanceEnable"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxVlanMISTPInstMapInstIndex"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxVlanMISTPInstMapEditInstIndex"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxPreferredMISTPInstancesMap"))
)
if mibBuilder.loadTexts:
    stpxMISTPGroup.setStatus("current")

stpxLongPathCostModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 11)
)
stpxLongPathCostModeGroup.setObjects(
      *(("CISCO-STP-EXTENSIONS-MIB", "stpxSpanningTreePathCostMode"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxLongStpPortPathCost"))
)
if mibBuilder.loadTexts:
    stpxLongPathCostModeGroup.setStatus("current")

stpxPVSTVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 12)
)
stpxPVSTVlanGroup.setObjects(
    ("CISCO-STP-EXTENSIONS-MIB", "stpxPVSTVlanEnable")
)
if mibBuilder.loadTexts:
    stpxPVSTVlanGroup.setStatus("current")

stpxMISTPGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 13)
)
stpxMISTPGroup2.setObjects(
      *(("CISCO-STP-EXTENSIONS-MIB", "stpxMISTPInstanceVlansMapped"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMISTPInstanceVlansMapped2k"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMISTPInstanceVlansMapped3k"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMISTPInstanceVlansMapped4k"))
)
if mibBuilder.loadTexts:
    stpxMISTPGroup2.setStatus("current")

stpxLoopGuardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 14)
)
stpxLoopGuardGroup.setObjects(
      *(("CISCO-STP-EXTENSIONS-MIB", "stpxLoopGuardConfigEnabled"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxLoopInconsistencyState"))
)
if mibBuilder.loadTexts:
    stpxLoopGuardGroup.setStatus("deprecated")

stpxFastStartGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 16)
)
stpxFastStartGroup.setObjects(
      *(("CISCO-STP-EXTENSIONS-MIB", "stpxFastStartBpduGuardEnable"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxFastStartBpduFilterEnable"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxFastStartPortEnable"))
)
if mibBuilder.loadTexts:
    stpxFastStartGroup.setStatus("deprecated")

stpxBpduSkewingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 17)
)
stpxBpduSkewingGroup.setObjects(
      *(("CISCO-STP-EXTENSIONS-MIB", "stpxBpduSkewingDetectionEnable"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxBpduSkewingLastSkewDuration"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxBpduSkewingWorstSkewDuration"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxBpduSkewingWorstSkewTime"))
)
if mibBuilder.loadTexts:
    stpxBpduSkewingGroup.setStatus("current")

stpxFastStartGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 18)
)
stpxFastStartGroup2.setObjects(
      *(("CISCO-STP-EXTENSIONS-MIB", "stpxFastStartBpduGuardEnable"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxFastStartBpduFilterEnable"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxFastStartPortMode"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxFastStartGlobalDefaultMode"))
)
if mibBuilder.loadTexts:
    stpxFastStartGroup2.setStatus("current")

stpxLoopGuardGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 19)
)
stpxLoopGuardGroup2.setObjects(
      *(("CISCO-STP-EXTENSIONS-MIB", "stpxLoopInconsistencyState"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxLoopGuardConfigMode"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxLoopGuardGlobalDefaultMode"))
)
if mibBuilder.loadTexts:
    stpxLoopGuardGroup2.setStatus("current")

stpxMSTGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 20)
)
stpxMSTGroup.setObjects(
      *(("CISCO-STP-EXTENSIONS-MIB", "stpxMSTMaxInstanceNumber"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTRegionName"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTRegionRevision"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTInstanceVlansMapped"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTInstanceVlansMapped2k"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTInstanceVlansMapped3k"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTInstanceVlansMapped4k"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTInstanceRemainingHopCount"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTRegionEditBufferStatus"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTRegionEditBufferOperation"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTRegionEditName"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTRegionEditRevision"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTInstanceEditVlansMap"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTInstanceEditVlansMap2k"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTInstanceEditVlansMap3k"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTInstanceEditVlansMap4k"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTPortAdminLinkType"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTPortOperLinkType"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTPortProtocolMigration"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTPortStatus"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTPortRoleValue"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTMaxHopCount"))
)
if mibBuilder.loadTexts:
    stpxMSTGroup.setStatus("deprecated")

stpxPreferredMSTInstancesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 21)
)
stpxPreferredMSTInstancesGroup.setObjects(
    ("CISCO-STP-EXTENSIONS-MIB", "stpxPreferredMSTInstancesMap")
)
if mibBuilder.loadTexts:
    stpxPreferredMSTInstancesGroup.setStatus("deprecated")

stpxFastStartGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 22)
)
stpxFastStartGroup3.setObjects(
      *(("CISCO-STP-EXTENSIONS-MIB", "stpxFastStartPortBpduGuardMode"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxFastStartPortBpduFilterMode"))
)
if mibBuilder.loadTexts:
    stpxFastStartGroup3.setStatus("current")

stpxUplinkGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 23)
)
stpxUplinkGroup2.setObjects(
    ("CISCO-STP-EXTENSIONS-MIB", "stpxUplinkFastOperEnabled")
)
if mibBuilder.loadTexts:
    stpxUplinkGroup2.setStatus("current")

stpxBackboneGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 24)
)
stpxBackboneGroup2.setObjects(
    ("CISCO-STP-EXTENSIONS-MIB", "stpxBackboneFastOperEnabled")
)
if mibBuilder.loadTexts:
    stpxBackboneGroup2.setStatus("current")

stpxMSTGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 25)
)
stpxMSTGroup2.setObjects(
      *(("CISCO-STP-EXTENSIONS-MIB", "stpxMSTMaxInstanceNumber"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTRegionName"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTRegionRevision"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTInstanceVlansMapped"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTInstanceVlansMapped2k"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTInstanceVlansMapped3k"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTInstanceVlansMapped4k"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTInstanceRemainingHopCount"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTRegionEditBufferStatus"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTRegionEditBufferOperation"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTRegionEditName"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTRegionEditRevision"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTInstanceEditVlansMap"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTInstanceEditVlansMap2k"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTInstanceEditVlansMap3k"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTInstanceEditVlansMap4k"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTPortStatus"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTMaxHopCount"))
)
if mibBuilder.loadTexts:
    stpxMSTGroup2.setStatus("deprecated")

stpxRSTPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 26)
)
stpxRSTPGroup.setObjects(
      *(("CISCO-STP-EXTENSIONS-MIB", "stpxRSTPPortAdminLinkType"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxRSTPPortOperLinkType"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxRSTPPortProtocolMigration"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxRSTPPortRoleValue"))
)
if mibBuilder.loadTexts:
    stpxRSTPGroup.setStatus("current")

stpxRPVSTGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 27)
)
stpxRPVSTGroup.setObjects(
    ("CISCO-STP-EXTENSIONS-MIB", "stpxRPVSTPortStatus")
)
if mibBuilder.loadTexts:
    stpxRPVSTGroup.setStatus("current")

stpxExtendedSysIDGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 28)
)
stpxExtendedSysIDGroup.setObjects(
      *(("CISCO-STP-EXTENSIONS-MIB", "stpxExtendedSysIDAdminEnabled"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxExtendedSysIDOperEnabled"))
)
if mibBuilder.loadTexts:
    stpxExtendedSysIDGroup.setStatus("current")

stpxNotificationEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 29)
)
stpxNotificationEnableGroup.setObjects(
    ("CISCO-STP-EXTENSIONS-MIB", "stpxNotificationEnable")
)
if mibBuilder.loadTexts:
    stpxNotificationEnableGroup.setStatus("current")

stpxFastStartOperModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 30)
)
stpxFastStartOperModeGroup.setObjects(
    ("CISCO-STP-EXTENSIONS-MIB", "stpxFastStartOperMode")
)
if mibBuilder.loadTexts:
    stpxFastStartOperModeGroup.setStatus("current")

stpxMSTGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 31)
)
stpxMSTGroup3.setObjects(
      *(("CISCO-STP-EXTENSIONS-MIB", "stpxMSTRegionName"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTRegionEditBufferStatus"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTRegionEditBufferOperation"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTRegionEditName"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTMaxHopCount"))
)
if mibBuilder.loadTexts:
    stpxMSTGroup3.setStatus("deprecated")

stpxSMSTGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 32)
)
stpxSMSTGroup.setObjects(
      *(("CISCO-STP-EXTENSIONS-MIB", "stpxSMSTMaxInstances"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxSMSTMaxInstanceID"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxSMSTRegionRevision"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxSMSTRegionEditRevision"))
)
if mibBuilder.loadTexts:
    stpxSMSTGroup.setStatus("current")

stpxSMSTInstanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 33)
)
stpxSMSTInstanceGroup.setObjects(
      *(("CISCO-STP-EXTENSIONS-MIB", "stpxSMSTInstanceVlansMapped1k2k"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxSMSTInstanceVlansMapped3k4k"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxSMSTInstanceRemainingHopCount"))
)
if mibBuilder.loadTexts:
    stpxSMSTInstanceGroup.setStatus("current")

stpxSMSTInstanceEditGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 34)
)
stpxSMSTInstanceEditGroup.setObjects(
      *(("CISCO-STP-EXTENSIONS-MIB", "stpxSMSTInstanceEditVlansMap1k2k"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxSMSTInstanceEditVlansMap3k4k"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxSMSTInstanceEditRowStatus"))
)
if mibBuilder.loadTexts:
    stpxSMSTInstanceEditGroup.setStatus("current")

stpxSMSTPortStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 35)
)
stpxSMSTPortStatusGroup.setObjects(
    ("CISCO-STP-EXTENSIONS-MIB", "stpxSMSTPortStatus")
)
if mibBuilder.loadTexts:
    stpxSMSTPortStatusGroup.setStatus("current")

stpxSMSTPortHelloTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 36)
)
stpxSMSTPortHelloTimeGroup.setObjects(
      *(("CISCO-STP-EXTENSIONS-MIB", "stpxSMSTPortAdminHelloTime"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxSMSTPortConfigedHelloTime"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxSMSTPortOperHelloTime"))
)
if mibBuilder.loadTexts:
    stpxSMSTPortHelloTimeGroup.setStatus("current")

stpxSMSTInstanceCISTGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 37)
)
stpxSMSTInstanceCISTGroup.setObjects(
      *(("CISCO-STP-EXTENSIONS-MIB", "stpxSMSTInstanceCISTRegionalRoot"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxSMSTInstanceCISTIntRootCost"))
)
if mibBuilder.loadTexts:
    stpxSMSTInstanceCISTGroup.setStatus("current")

stpxPathCostOperModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 38)
)
stpxPathCostOperModeGroup.setObjects(
    ("CISCO-STP-EXTENSIONS-MIB", "stpxSpanningTreePathCostOperMode")
)
if mibBuilder.loadTexts:
    stpxPathCostOperModeGroup.setStatus("current")

stpxRSTPTransmitHoldCountGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 39)
)
stpxRSTPTransmitHoldCountGroup.setObjects(
    ("CISCO-STP-EXTENSIONS-MIB", "stpxRSTPTransmitHoldCount")
)
if mibBuilder.loadTexts:
    stpxRSTPTransmitHoldCountGroup.setStatus("current")

stpxSMSTPortMSTModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 40)
)
stpxSMSTPortMSTModeGroup.setObjects(
      *(("CISCO-STP-EXTENSIONS-MIB", "stpxSMSTPortAdminMSTMode"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxSMSTPortOperMSTMode"))
)
if mibBuilder.loadTexts:
    stpxSMSTPortMSTModeGroup.setStatus("current")

stpxSMSTMaxHopCountGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 41)
)
stpxSMSTMaxHopCountGroup.setObjects(
    ("CISCO-STP-EXTENSIONS-MIB", "stpxSMSTMaxHopCount")
)
if mibBuilder.loadTexts:
    stpxSMSTMaxHopCountGroup.setStatus("current")

stpxSMSTConfigDigestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 42)
)
stpxSMSTConfigDigestGroup.setObjects(
      *(("CISCO-STP-EXTENSIONS-MIB", "stpxSMSTConfigDigest"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxSMSTConfigPreStandardDigest"))
)
if mibBuilder.loadTexts:
    stpxSMSTConfigDigestGroup.setStatus("current")

stpxMSTGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 43)
)
stpxMSTGroup4.setObjects(
      *(("CISCO-STP-EXTENSIONS-MIB", "stpxMSTRegionName"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTRegionEditBufferStatus"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTRegionEditBufferOperation"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxMSTRegionEditName"))
)
if mibBuilder.loadTexts:
    stpxMSTGroup4.setStatus("current")


# Notification objects

stpxInconsistencyUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 2, 0, 1)
)
stpxInconsistencyUpdate.setObjects(
    ("CISCO-STP-EXTENSIONS-MIB", "stpxInconsistentState")
)
if mibBuilder.loadTexts:
    stpxInconsistencyUpdate.setStatus(
        "current"
    )

stpxRootInconsistencyUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 2, 0, 2)
)
stpxRootInconsistencyUpdate.setObjects(
      *(("CISCO-STP-EXTENSIONS-MIB", "stpxRootInconsistencyState"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxSpanningTreeType"))
)
if mibBuilder.loadTexts:
    stpxRootInconsistencyUpdate.setStatus(
        "current"
    )

stpxLoopInconsistencyUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 2, 0, 3)
)
stpxLoopInconsistencyUpdate.setObjects(
      *(("CISCO-STP-EXTENSIONS-MIB", "stpxLoopInconsistencyState"),
        ("CISCO-STP-EXTENSIONS-MIB", "stpxSpanningTreeType"))
)
if mibBuilder.loadTexts:
    stpxLoopInconsistencyUpdate.setStatus(
        "current"
    )


# Notifications groups

stpxNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 4)
)
stpxNotificationsGroup.setObjects(
    ("CISCO-STP-EXTENSIONS-MIB", "stpxInconsistencyUpdate")
)
if mibBuilder.loadTexts:
    stpxNotificationsGroup.setStatus(
        "current"
    )

stpxRootInconsistencyNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 7)
)
stpxRootInconsistencyNotificationsGroup.setObjects(
    ("CISCO-STP-EXTENSIONS-MIB", "stpxRootInconsistencyUpdate")
)
if mibBuilder.loadTexts:
    stpxRootInconsistencyNotificationsGroup.setStatus(
        "current"
    )

stpxLoopInconsistencyNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 2, 15)
)
stpxLoopInconsistencyNotificationsGroup.setObjects(
    ("CISCO-STP-EXTENSIONS-MIB", "stpxLoopInconsistencyUpdate")
)
if mibBuilder.loadTexts:
    stpxLoopInconsistencyNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

stpxMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 1, 1)
)
if mibBuilder.loadTexts:
    stpxMIBCompliance.setStatus(
        "deprecated"
    )

stpxMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 1, 2)
)
if mibBuilder.loadTexts:
    stpxMIBCompliance2.setStatus(
        "deprecated"
    )

stpxMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 1, 3)
)
if mibBuilder.loadTexts:
    stpxMIBCompliance3.setStatus(
        "deprecated"
    )

stpxMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 1, 4)
)
if mibBuilder.loadTexts:
    stpxMIBCompliance4.setStatus(
        "deprecated"
    )

stpxMIBCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 1, 5)
)
if mibBuilder.loadTexts:
    stpxMIBCompliance5.setStatus(
        "deprecated"
    )

stpxMIBCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 1, 6)
)
if mibBuilder.loadTexts:
    stpxMIBCompliance6.setStatus(
        "deprecated"
    )

stpxMIBCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 1, 7)
)
if mibBuilder.loadTexts:
    stpxMIBCompliance7.setStatus(
        "deprecated"
    )

stpxMIBCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 1, 8)
)
if mibBuilder.loadTexts:
    stpxMIBCompliance8.setStatus(
        "deprecated"
    )

stpxMIBCompliance9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 1, 9)
)
if mibBuilder.loadTexts:
    stpxMIBCompliance9.setStatus(
        "deprecated"
    )

stpxMIBCompliance10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 1, 10)
)
if mibBuilder.loadTexts:
    stpxMIBCompliance10.setStatus(
        "deprecated"
    )

stpxMIBCompliance11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 1, 11)
)
if mibBuilder.loadTexts:
    stpxMIBCompliance11.setStatus(
        "deprecated"
    )

stpxMIBCompliance12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 82, 3, 1, 12)
)
if mibBuilder.loadTexts:
    stpxMIBCompliance12.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-STP-EXTENSIONS-MIB",
    **{"StpxMSTConfigurationDigest": StpxMSTConfigurationDigest,
       "ciscoStpExtensionsMIB": ciscoStpExtensionsMIB,
       "stpxObjects": stpxObjects,
       "stpxUplinkFastObjects": stpxUplinkFastObjects,
       "stpxUplinkFastEnabled": stpxUplinkFastEnabled,
       "stpxUplinkFastTransitions": stpxUplinkFastTransitions,
       "stpxUplinkStationLearningGenRate": stpxUplinkStationLearningGenRate,
       "stpxUplinkStationLearningFrames": stpxUplinkStationLearningFrames,
       "stpxUplinkFastOperEnabled": stpxUplinkFastOperEnabled,
       "stpxVlanObjects": stpxVlanObjects,
       "stpxPreferredVlansTable": stpxPreferredVlansTable,
       "stpxPreferredVlansEntry": stpxPreferredVlansEntry,
       "stpxPreferredVlansMap": stpxPreferredVlansMap,
       "stpxPreferredVlansMap2k": stpxPreferredVlansMap2k,
       "stpxPreferredVlansMap3k": stpxPreferredVlansMap3k,
       "stpxPreferredVlansMap4k": stpxPreferredVlansMap4k,
       "stpxPVSTVlanTable": stpxPVSTVlanTable,
       "stpxPVSTVlanEntry": stpxPVSTVlanEntry,
       "stpxPVSTVlanIndex": stpxPVSTVlanIndex,
       "stpxPVSTVlanEnable": stpxPVSTVlanEnable,
       "stpxInconsistencyObjects": stpxInconsistencyObjects,
       "stpxInconsistencyTable": stpxInconsistencyTable,
       "stpxInconsistencyEntry": stpxInconsistencyEntry,
       "stpxVlanIndex": stpxVlanIndex,
       "stpxPortIndex": stpxPortIndex,
       "stpxInconsistentState": stpxInconsistentState,
       "stpxBackboneFastObjects": stpxBackboneFastObjects,
       "stpxBackboneFastEnabled": stpxBackboneFastEnabled,
       "stpxBackboneFastInInferiorBPDUs": stpxBackboneFastInInferiorBPDUs,
       "stpxBackboneFastInRLQRequestPDUs": stpxBackboneFastInRLQRequestPDUs,
       "stpxBackboneFastInRLQResponsePDUs": stpxBackboneFastInRLQResponsePDUs,
       "stpxBackboneFastOutRLQRequestPDUs": stpxBackboneFastOutRLQRequestPDUs,
       "stpxBackboneFastOutRLQResponsePDUs": stpxBackboneFastOutRLQResponsePDUs,
       "stpxBackboneFastOperEnabled": stpxBackboneFastOperEnabled,
       "stpxRootGuardObjects": stpxRootGuardObjects,
       "stpxRootGuardConfigTable": stpxRootGuardConfigTable,
       "stpxRootGuardConfigEntry": stpxRootGuardConfigEntry,
       "stpxRootGuardConfigPortIndex": stpxRootGuardConfigPortIndex,
       "stpxRootGuardConfigEnabled": stpxRootGuardConfigEnabled,
       "stpxRootInconsistencyTable": stpxRootInconsistencyTable,
       "stpxRootInconsistencyEntry": stpxRootInconsistencyEntry,
       "stpxRootInconsistencyIndex": stpxRootInconsistencyIndex,
       "stpxRootInconsistencyPortIndex": stpxRootInconsistencyPortIndex,
       "stpxRootInconsistencyState": stpxRootInconsistencyState,
       "stpxSpanningTreeObjects": stpxSpanningTreeObjects,
       "stpxSpanningTreeType": stpxSpanningTreeType,
       "stpxSpanningTreePathCostMode": stpxSpanningTreePathCostMode,
       "stpxLongStpPortPathCostTable": stpxLongStpPortPathCostTable,
       "stpxLongStpPortPathCostEntry": stpxLongStpPortPathCostEntry,
       "stpxLongStpPortPathCost": stpxLongStpPortPathCost,
       "stpxExtendedSysIDAdminEnabled": stpxExtendedSysIDAdminEnabled,
       "stpxExtendedSysIDOperEnabled": stpxExtendedSysIDOperEnabled,
       "stpxNotificationEnable": stpxNotificationEnable,
       "stpxSpanningTreePathCostOperMode": stpxSpanningTreePathCostOperMode,
       "stpxMISTPObjects": stpxMISTPObjects,
       "stpxMISTPInstanceNumber": stpxMISTPInstanceNumber,
       "stpxMISTPInstanceTable": stpxMISTPInstanceTable,
       "stpxMISTPInstanceEntry": stpxMISTPInstanceEntry,
       "stpxMISTPInstanceIndex": stpxMISTPInstanceIndex,
       "stpxMISTPInstanceEnable": stpxMISTPInstanceEnable,
       "stpxMISTPInstanceVlansMapped": stpxMISTPInstanceVlansMapped,
       "stpxMISTPInstanceVlansMapped2k": stpxMISTPInstanceVlansMapped2k,
       "stpxMISTPInstanceVlansMapped3k": stpxMISTPInstanceVlansMapped3k,
       "stpxMISTPInstanceVlansMapped4k": stpxMISTPInstanceVlansMapped4k,
       "stpxVlanMISTPInstMapTable": stpxVlanMISTPInstMapTable,
       "stpxVlanMISTPInstMapEntry": stpxVlanMISTPInstMapEntry,
       "stpxVlanMISTPInstMapInstIndex": stpxVlanMISTPInstMapInstIndex,
       "stpxVlanMISTPInstMapEditTable": stpxVlanMISTPInstMapEditTable,
       "stpxVlanMISTPInstMapEditEntry": stpxVlanMISTPInstMapEditEntry,
       "stpxVlanMISTPInstMapEditInstIndex": stpxVlanMISTPInstMapEditInstIndex,
       "stpxPreferredMISTPInstancesTable": stpxPreferredMISTPInstancesTable,
       "stpxPreferredMISTPInstancesEntry": stpxPreferredMISTPInstancesEntry,
       "stpxPreferredMISTPInstancesMap": stpxPreferredMISTPInstancesMap,
       "stpxLoopGuardObjects": stpxLoopGuardObjects,
       "stpxLoopGuardConfigTable": stpxLoopGuardConfigTable,
       "stpxLoopGuardConfigEntry": stpxLoopGuardConfigEntry,
       "stpxLoopGuardConfigPortIndex": stpxLoopGuardConfigPortIndex,
       "stpxLoopGuardConfigEnabled": stpxLoopGuardConfigEnabled,
       "stpxLoopGuardConfigMode": stpxLoopGuardConfigMode,
       "stpxLoopInconsistencyTable": stpxLoopInconsistencyTable,
       "stpxLoopInconsistencyEntry": stpxLoopInconsistencyEntry,
       "stpxLoopInconsistencyIndex": stpxLoopInconsistencyIndex,
       "stpxLoopInconsistencyPortIndex": stpxLoopInconsistencyPortIndex,
       "stpxLoopInconsistencyState": stpxLoopInconsistencyState,
       "stpxLoopGuardGlobalDefaultMode": stpxLoopGuardGlobalDefaultMode,
       "stpxFastStartObjects": stpxFastStartObjects,
       "stpxFastStartBpduGuardEnable": stpxFastStartBpduGuardEnable,
       "stpxFastStartBpduFilterEnable": stpxFastStartBpduFilterEnable,
       "stpxFastStartPortTable": stpxFastStartPortTable,
       "stpxFastStartPortEntry": stpxFastStartPortEntry,
       "stpxFastStartPortIndex": stpxFastStartPortIndex,
       "stpxFastStartPortEnable": stpxFastStartPortEnable,
       "stpxFastStartPortMode": stpxFastStartPortMode,
       "stpxFastStartPortBpduGuardMode": stpxFastStartPortBpduGuardMode,
       "stpxFastStartPortBpduFilterMode": stpxFastStartPortBpduFilterMode,
       "stpxFastStartGlobalDefaultMode": stpxFastStartGlobalDefaultMode,
       "stpxFastStartOperModeTable": stpxFastStartOperModeTable,
       "stpxFastStartOperModeEntry": stpxFastStartOperModeEntry,
       "stpxFastStartOperModeInstIndex": stpxFastStartOperModeInstIndex,
       "stpxFastStartOperModePortIndex": stpxFastStartOperModePortIndex,
       "stpxFastStartOperMode": stpxFastStartOperMode,
       "stpxBpduSkewingObjects": stpxBpduSkewingObjects,
       "stpxBpduSkewingDetectionEnable": stpxBpduSkewingDetectionEnable,
       "stpxBpduSkewingTable": stpxBpduSkewingTable,
       "stpxBpduSkewingEntry": stpxBpduSkewingEntry,
       "stpxBpduSkewingInstanceIndex": stpxBpduSkewingInstanceIndex,
       "stpxBpduSkewingPortIndex": stpxBpduSkewingPortIndex,
       "stpxBpduSkewingLastSkewDuration": stpxBpduSkewingLastSkewDuration,
       "stpxBpduSkewingWorstSkewDuration": stpxBpduSkewingWorstSkewDuration,
       "stpxBpduSkewingWorstSkewTime": stpxBpduSkewingWorstSkewTime,
       "stpxMSTObjects": stpxMSTObjects,
       "stpxMSTMaxInstanceNumber": stpxMSTMaxInstanceNumber,
       "stpxMSTRegionName": stpxMSTRegionName,
       "stpxMSTRegionRevision": stpxMSTRegionRevision,
       "stpxMSTInstanceTable": stpxMSTInstanceTable,
       "stpxMSTInstanceEntry": stpxMSTInstanceEntry,
       "stpxMSTInstanceIndex": stpxMSTInstanceIndex,
       "stpxMSTInstanceVlansMapped": stpxMSTInstanceVlansMapped,
       "stpxMSTInstanceVlansMapped2k": stpxMSTInstanceVlansMapped2k,
       "stpxMSTInstanceVlansMapped3k": stpxMSTInstanceVlansMapped3k,
       "stpxMSTInstanceVlansMapped4k": stpxMSTInstanceVlansMapped4k,
       "stpxMSTInstanceRemainingHopCount": stpxMSTInstanceRemainingHopCount,
       "stpxMSTRegionEditBufferStatus": stpxMSTRegionEditBufferStatus,
       "stpxMSTRegionEditBufferOperation": stpxMSTRegionEditBufferOperation,
       "stpxMSTRegionEditName": stpxMSTRegionEditName,
       "stpxMSTRegionEditRevision": stpxMSTRegionEditRevision,
       "stpxMSTInstanceEditTable": stpxMSTInstanceEditTable,
       "stpxMSTInstanceEditEntry": stpxMSTInstanceEditEntry,
       "stpxMSTInstanceEditIndex": stpxMSTInstanceEditIndex,
       "stpxMSTInstanceEditVlansMap": stpxMSTInstanceEditVlansMap,
       "stpxMSTInstanceEditVlansMap2k": stpxMSTInstanceEditVlansMap2k,
       "stpxMSTInstanceEditVlansMap3k": stpxMSTInstanceEditVlansMap3k,
       "stpxMSTInstanceEditVlansMap4k": stpxMSTInstanceEditVlansMap4k,
       "stpxPreferredMSTInstancesTable": stpxPreferredMSTInstancesTable,
       "stpxPreferredMSTInstancesEntry": stpxPreferredMSTInstancesEntry,
       "stpxPreferredMSTInstancesMap": stpxPreferredMSTInstancesMap,
       "stpxMSTPortTable": stpxMSTPortTable,
       "stpxMSTPortEntry": stpxMSTPortEntry,
       "stpxMSTPortIndex": stpxMSTPortIndex,
       "stpxMSTPortAdminLinkType": stpxMSTPortAdminLinkType,
       "stpxMSTPortOperLinkType": stpxMSTPortOperLinkType,
       "stpxMSTPortProtocolMigration": stpxMSTPortProtocolMigration,
       "stpxMSTPortStatus": stpxMSTPortStatus,
       "stpxMSTPortRoleTable": stpxMSTPortRoleTable,
       "stpxMSTPortRoleEntry": stpxMSTPortRoleEntry,
       "stpxMSTPortRoleInstanceIndex": stpxMSTPortRoleInstanceIndex,
       "stpxMSTPortRolePortIndex": stpxMSTPortRolePortIndex,
       "stpxMSTPortRoleValue": stpxMSTPortRoleValue,
       "stpxMSTMaxHopCount": stpxMSTMaxHopCount,
       "stpxRSTPObjects": stpxRSTPObjects,
       "stpxRSTPPortTable": stpxRSTPPortTable,
       "stpxRSTPPortEntry": stpxRSTPPortEntry,
       "stpxRSTPPortIndex": stpxRSTPPortIndex,
       "stpxRSTPPortAdminLinkType": stpxRSTPPortAdminLinkType,
       "stpxRSTPPortOperLinkType": stpxRSTPPortOperLinkType,
       "stpxRSTPPortProtocolMigration": stpxRSTPPortProtocolMigration,
       "stpxRSTPPortRoleTable": stpxRSTPPortRoleTable,
       "stpxRSTPPortRoleEntry": stpxRSTPPortRoleEntry,
       "stpxRSTPPortRoleInstanceIndex": stpxRSTPPortRoleInstanceIndex,
       "stpxRSTPPortRolePortIndex": stpxRSTPPortRolePortIndex,
       "stpxRSTPPortRoleValue": stpxRSTPPortRoleValue,
       "stpxRSTPTransmitHoldCount": stpxRSTPTransmitHoldCount,
       "stpxRPVSTObjects": stpxRPVSTObjects,
       "stpxRPVSTPortTable": stpxRPVSTPortTable,
       "stpxRPVSTPortEntry": stpxRPVSTPortEntry,
       "stpxRPVSTPortVlanIndex": stpxRPVSTPortVlanIndex,
       "stpxRPVSTPortIndex": stpxRPVSTPortIndex,
       "stpxRPVSTPortStatus": stpxRPVSTPortStatus,
       "stpxSMSTObjects": stpxSMSTObjects,
       "stpxSMSTMaxInstances": stpxSMSTMaxInstances,
       "stpxSMSTMaxInstanceID": stpxSMSTMaxInstanceID,
       "stpxSMSTRegionRevision": stpxSMSTRegionRevision,
       "stpxSMSTRegionEditRevision": stpxSMSTRegionEditRevision,
       "stpxSMSTInstanceTable": stpxSMSTInstanceTable,
       "stpxSMSTInstanceEntry": stpxSMSTInstanceEntry,
       "stpxSMSTInstanceIndex": stpxSMSTInstanceIndex,
       "stpxSMSTInstanceVlansMapped1k2k": stpxSMSTInstanceVlansMapped1k2k,
       "stpxSMSTInstanceVlansMapped3k4k": stpxSMSTInstanceVlansMapped3k4k,
       "stpxSMSTInstanceRemainingHopCount": stpxSMSTInstanceRemainingHopCount,
       "stpxSMSTInstanceCISTRegionalRoot": stpxSMSTInstanceCISTRegionalRoot,
       "stpxSMSTInstanceCISTIntRootCost": stpxSMSTInstanceCISTIntRootCost,
       "stpxSMSTInstanceEditTable": stpxSMSTInstanceEditTable,
       "stpxSMSTInstanceEditEntry": stpxSMSTInstanceEditEntry,
       "stpxSMSTInstanceEditIndex": stpxSMSTInstanceEditIndex,
       "stpxSMSTInstanceEditVlansMap1k2k": stpxSMSTInstanceEditVlansMap1k2k,
       "stpxSMSTInstanceEditVlansMap3k4k": stpxSMSTInstanceEditVlansMap3k4k,
       "stpxSMSTInstanceEditRowStatus": stpxSMSTInstanceEditRowStatus,
       "stpxSMSTPortTable": stpxSMSTPortTable,
       "stpxSMSTPortEntry": stpxSMSTPortEntry,
       "stpxSMSTPortIndex": stpxSMSTPortIndex,
       "stpxSMSTPortStatus": stpxSMSTPortStatus,
       "stpxSMSTPortAdminHelloTime": stpxSMSTPortAdminHelloTime,
       "stpxSMSTPortConfigedHelloTime": stpxSMSTPortConfigedHelloTime,
       "stpxSMSTPortOperHelloTime": stpxSMSTPortOperHelloTime,
       "stpxSMSTPortAdminMSTMode": stpxSMSTPortAdminMSTMode,
       "stpxSMSTPortOperMSTMode": stpxSMSTPortOperMSTMode,
       "stpxSMSTMaxHopCount": stpxSMSTMaxHopCount,
       "stpxSMSTConfigDigest": stpxSMSTConfigDigest,
       "stpxSMSTConfigPreStandardDigest": stpxSMSTConfigPreStandardDigest,
       "stpxNotifications": stpxNotifications,
       "stpxNotificationsPrefix": stpxNotificationsPrefix,
       "stpxInconsistencyUpdate": stpxInconsistencyUpdate,
       "stpxRootInconsistencyUpdate": stpxRootInconsistencyUpdate,
       "stpxLoopInconsistencyUpdate": stpxLoopInconsistencyUpdate,
       "stpxMIBConformance": stpxMIBConformance,
       "stpxMIBCompliances": stpxMIBCompliances,
       "stpxMIBCompliance": stpxMIBCompliance,
       "stpxMIBCompliance2": stpxMIBCompliance2,
       "stpxMIBCompliance3": stpxMIBCompliance3,
       "stpxMIBCompliance4": stpxMIBCompliance4,
       "stpxMIBCompliance5": stpxMIBCompliance5,
       "stpxMIBCompliance6": stpxMIBCompliance6,
       "stpxMIBCompliance7": stpxMIBCompliance7,
       "stpxMIBCompliance8": stpxMIBCompliance8,
       "stpxMIBCompliance9": stpxMIBCompliance9,
       "stpxMIBCompliance10": stpxMIBCompliance10,
       "stpxMIBCompliance11": stpxMIBCompliance11,
       "stpxMIBCompliance12": stpxMIBCompliance12,
       "stpxMIBGroups": stpxMIBGroups,
       "stpxUplinkGroup": stpxUplinkGroup,
       "stpxPreferredVlansGroup": stpxPreferredVlansGroup,
       "stpxSstpGroup": stpxSstpGroup,
       "stpxNotificationsGroup": stpxNotificationsGroup,
       "stpxBackboneGroup": stpxBackboneGroup,
       "stpxRootGuardGroup": stpxRootGuardGroup,
       "stpxRootInconsistencyNotificationsGroup": stpxRootInconsistencyNotificationsGroup,
       "stpx4kVlanGroup": stpx4kVlanGroup,
       "stpxSpanningTreeGroup": stpxSpanningTreeGroup,
       "stpxMISTPGroup": stpxMISTPGroup,
       "stpxLongPathCostModeGroup": stpxLongPathCostModeGroup,
       "stpxPVSTVlanGroup": stpxPVSTVlanGroup,
       "stpxMISTPGroup2": stpxMISTPGroup2,
       "stpxLoopGuardGroup": stpxLoopGuardGroup,
       "stpxLoopInconsistencyNotificationsGroup": stpxLoopInconsistencyNotificationsGroup,
       "stpxFastStartGroup": stpxFastStartGroup,
       "stpxBpduSkewingGroup": stpxBpduSkewingGroup,
       "stpxFastStartGroup2": stpxFastStartGroup2,
       "stpxLoopGuardGroup2": stpxLoopGuardGroup2,
       "stpxMSTGroup": stpxMSTGroup,
       "stpxPreferredMSTInstancesGroup": stpxPreferredMSTInstancesGroup,
       "stpxFastStartGroup3": stpxFastStartGroup3,
       "stpxUplinkGroup2": stpxUplinkGroup2,
       "stpxBackboneGroup2": stpxBackboneGroup2,
       "stpxMSTGroup2": stpxMSTGroup2,
       "stpxRSTPGroup": stpxRSTPGroup,
       "stpxRPVSTGroup": stpxRPVSTGroup,
       "stpxExtendedSysIDGroup": stpxExtendedSysIDGroup,
       "stpxNotificationEnableGroup": stpxNotificationEnableGroup,
       "stpxFastStartOperModeGroup": stpxFastStartOperModeGroup,
       "stpxMSTGroup3": stpxMSTGroup3,
       "stpxSMSTGroup": stpxSMSTGroup,
       "stpxSMSTInstanceGroup": stpxSMSTInstanceGroup,
       "stpxSMSTInstanceEditGroup": stpxSMSTInstanceEditGroup,
       "stpxSMSTPortStatusGroup": stpxSMSTPortStatusGroup,
       "stpxSMSTPortHelloTimeGroup": stpxSMSTPortHelloTimeGroup,
       "stpxSMSTInstanceCISTGroup": stpxSMSTInstanceCISTGroup,
       "stpxPathCostOperModeGroup": stpxPathCostOperModeGroup,
       "stpxRSTPTransmitHoldCountGroup": stpxRSTPTransmitHoldCountGroup,
       "stpxSMSTPortMSTModeGroup": stpxSMSTPortMSTModeGroup,
       "stpxSMSTMaxHopCountGroup": stpxSMSTMaxHopCountGroup,
       "stpxSMSTConfigDigestGroup": stpxSMSTConfigDigestGroup,
       "stpxMSTGroup4": stpxMSTGroup4}
)
