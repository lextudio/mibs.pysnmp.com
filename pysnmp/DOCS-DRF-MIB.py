# SNMP MIB module (DOCS-DRF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOCS-DRF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:35 2024
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

(clabProjDocsis,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjDocsis")

(docsIfDownstreamChannelEntry,) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "docsIfDownstreamChannelEntry")

(PhysicalIndex,
 PhysicalIndexOrZero) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "PhysicalIndexOrZero")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
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

(AutonomousType,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

docsDrfMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23)
)
docsDrfMib.setRevisions(
        ("2008-12-09 00:00",
         "2007-12-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DocsDrfNotifications_ObjectIdentity = ObjectIdentity
docsDrfNotifications = _DocsDrfNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 0)
)
_DocsDrfObjects_ObjectIdentity = ObjectIdentity
docsDrfObjects = _DocsDrfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1)
)
_DocsDrfRegistry_ObjectIdentity = ObjectIdentity
docsDrfRegistry = _DocsDrfRegistry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 1)
)
if mibBuilder.loadTexts:
    docsDrfRegistry.setStatus("current")
_DocsDrfPhyParamFixValue_ObjectIdentity = ObjectIdentity
docsDrfPhyParamFixValue = _DocsDrfPhyParamFixValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 1, 1)
)
if mibBuilder.loadTexts:
    docsDrfPhyParamFixValue.setStatus("current")
_DocsDrfPhyParamSameValue_ObjectIdentity = ObjectIdentity
docsDrfPhyParamSameValue = _DocsDrfPhyParamSameValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 1, 2)
)
if mibBuilder.loadTexts:
    docsDrfPhyParamSameValue.setStatus("current")
_DocsDrfPhyParamAdjacentValues_ObjectIdentity = ObjectIdentity
docsDrfPhyParamAdjacentValues = _DocsDrfPhyParamAdjacentValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 1, 3)
)
if mibBuilder.loadTexts:
    docsDrfPhyParamAdjacentValues.setStatus("current")
_DocsDrfPhyParamFrequencyRange_ObjectIdentity = ObjectIdentity
docsDrfPhyParamFrequencyRange = _DocsDrfPhyParamFrequencyRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 1, 4)
)
if mibBuilder.loadTexts:
    docsDrfPhyParamFrequencyRange.setStatus("current")
_DocsDrfDownstreamTable_Object = MibTable
docsDrfDownstreamTable = _DocsDrfDownstreamTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 2)
)
if mibBuilder.loadTexts:
    docsDrfDownstreamTable.setStatus("current")
_DocsDrfDownstreamEntry_Object = MibTableRow
docsDrfDownstreamEntry = _DocsDrfDownstreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 2, 1)
)
if mibBuilder.loadTexts:
    docsDrfDownstreamEntry.setStatus("current")


class _DocsDrfDownstreamPhyDependencies_Type(Bits):
    """Custom type docsDrfDownstreamPhyDependencies based on Bits"""
    namedValues = NamedValues(
        *(("bandwidth", 1),
          ("frequency", 0),
          ("interleaver", 4),
          ("j83Annex", 5),
          ("modulation", 3),
          ("mute", 7),
          ("power", 2),
          ("symbolRate", 6))
    )

_DocsDrfDownstreamPhyDependencies_Type.__name__ = "Bits"
_DocsDrfDownstreamPhyDependencies_Object = MibTableColumn
docsDrfDownstreamPhyDependencies = _DocsDrfDownstreamPhyDependencies_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 2, 1, 1),
    _DocsDrfDownstreamPhyDependencies_Type()
)
docsDrfDownstreamPhyDependencies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDrfDownstreamPhyDependencies.setStatus("current")
_DocsDrfDownstreamCapabilitiesTable_Object = MibTable
docsDrfDownstreamCapabilitiesTable = _DocsDrfDownstreamCapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 3)
)
if mibBuilder.loadTexts:
    docsDrfDownstreamCapabilitiesTable.setStatus("current")
_DocsDrfDownstreamCapabilitiesEntry_Object = MibTableRow
docsDrfDownstreamCapabilitiesEntry = _DocsDrfDownstreamCapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 3, 1)
)
docsDrfDownstreamCapabilitiesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsDrfDownstreamCapabilitiesEntry.setStatus("current")


class _DocsDrfDownstreamCapabFrequency_Type(Bits):
    """Custom type docsDrfDownstreamCapabFrequency based on Bits"""
    namedValues = NamedValues(
        *(("adjacentChannel", 1),
          ("adjacentChannelOrder", 2),
          ("qamDependency", 0))
    )

_DocsDrfDownstreamCapabFrequency_Type.__name__ = "Bits"
_DocsDrfDownstreamCapabFrequency_Object = MibTableColumn
docsDrfDownstreamCapabFrequency = _DocsDrfDownstreamCapabFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 3, 1, 1),
    _DocsDrfDownstreamCapabFrequency_Type()
)
docsDrfDownstreamCapabFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDrfDownstreamCapabFrequency.setStatus("current")


class _DocsDrfDownstreamCapabBandwidth_Type(Bits):
    """Custom type docsDrfDownstreamCapabBandwidth based on Bits"""
    namedValues = NamedValues(
        *(("chan6Mhz", 1),
          ("chan8Mhz", 2),
          ("qamDependency", 0))
    )

_DocsDrfDownstreamCapabBandwidth_Type.__name__ = "Bits"
_DocsDrfDownstreamCapabBandwidth_Object = MibTableColumn
docsDrfDownstreamCapabBandwidth = _DocsDrfDownstreamCapabBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 3, 1, 2),
    _DocsDrfDownstreamCapabBandwidth_Type()
)
docsDrfDownstreamCapabBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDrfDownstreamCapabBandwidth.setStatus("current")


class _DocsDrfDownstreamCapabPower_Type(Bits):
    """Custom type docsDrfDownstreamCapabPower based on Bits"""
    namedValues = NamedValues(
        ("qamDependency", 0)
    )

_DocsDrfDownstreamCapabPower_Type.__name__ = "Bits"
_DocsDrfDownstreamCapabPower_Object = MibTableColumn
docsDrfDownstreamCapabPower = _DocsDrfDownstreamCapabPower_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 3, 1, 3),
    _DocsDrfDownstreamCapabPower_Type()
)
docsDrfDownstreamCapabPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDrfDownstreamCapabPower.setStatus("current")


class _DocsDrfDownstreamCapabModulation_Type(Bits):
    """Custom type docsDrfDownstreamCapabModulation based on Bits"""
    namedValues = NamedValues(
        *(("qam256", 2),
          ("qam64", 1),
          ("qamDependency", 0))
    )

_DocsDrfDownstreamCapabModulation_Type.__name__ = "Bits"
_DocsDrfDownstreamCapabModulation_Object = MibTableColumn
docsDrfDownstreamCapabModulation = _DocsDrfDownstreamCapabModulation_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 3, 1, 4),
    _DocsDrfDownstreamCapabModulation_Type()
)
docsDrfDownstreamCapabModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDrfDownstreamCapabModulation.setStatus("current")


class _DocsDrfDownstreamCapabInterleaver_Type(Bits):
    """Custom type docsDrfDownstreamCapabInterleaver based on Bits"""
    namedValues = NamedValues(
        *(("qamDependency", 0),
          ("taps128Increment1", 5),
          ("taps128increment2", 7),
          ("taps128increment3", 8),
          ("taps128increment4", 9),
          ("taps128increment5", 10),
          ("taps128increment6", 11),
          ("taps128increment7", 12),
          ("taps128increment8", 13),
          ("taps12increment17", 6),
          ("taps16Increment8", 2),
          ("taps32Increment4", 3),
          ("taps64Increment2", 4),
          ("taps8Increment16", 1))
    )

_DocsDrfDownstreamCapabInterleaver_Type.__name__ = "Bits"
_DocsDrfDownstreamCapabInterleaver_Object = MibTableColumn
docsDrfDownstreamCapabInterleaver = _DocsDrfDownstreamCapabInterleaver_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 3, 1, 5),
    _DocsDrfDownstreamCapabInterleaver_Type()
)
docsDrfDownstreamCapabInterleaver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDrfDownstreamCapabInterleaver.setStatus("current")


class _DocsDrfDownstreamCapabJ83Annex_Type(Bits):
    """Custom type docsDrfDownstreamCapabJ83Annex based on Bits"""
    namedValues = NamedValues(
        *(("annexA", 1),
          ("annexB", 2),
          ("annexC", 3),
          ("qamDependency", 0))
    )

_DocsDrfDownstreamCapabJ83Annex_Type.__name__ = "Bits"
_DocsDrfDownstreamCapabJ83Annex_Object = MibTableColumn
docsDrfDownstreamCapabJ83Annex = _DocsDrfDownstreamCapabJ83Annex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 3, 1, 6),
    _DocsDrfDownstreamCapabJ83Annex_Type()
)
docsDrfDownstreamCapabJ83Annex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDrfDownstreamCapabJ83Annex.setStatus("current")


class _DocsDrfDownstreamCapabConcurrentServices_Type(Bits):
    """Custom type docsDrfDownstreamCapabConcurrentServices based on Bits"""
    namedValues = NamedValues(
        *(("qamDependency", 0),
          ("videoAndDocsis", 1))
    )

_DocsDrfDownstreamCapabConcurrentServices_Type.__name__ = "Bits"
_DocsDrfDownstreamCapabConcurrentServices_Object = MibTableColumn
docsDrfDownstreamCapabConcurrentServices = _DocsDrfDownstreamCapabConcurrentServices_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 3, 1, 7),
    _DocsDrfDownstreamCapabConcurrentServices_Type()
)
docsDrfDownstreamCapabConcurrentServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDrfDownstreamCapabConcurrentServices.setStatus("current")


class _DocsDrfDownstreamCapabServicesTransport_Type(Bits):
    """Custom type docsDrfDownstreamCapabServicesTransport based on Bits"""
    namedValues = NamedValues(
        *(("dmpt", 2),
          ("mpeg2OverIP", 1),
          ("psp", 3),
          ("qamDependency", 0))
    )

_DocsDrfDownstreamCapabServicesTransport_Type.__name__ = "Bits"
_DocsDrfDownstreamCapabServicesTransport_Object = MibTableColumn
docsDrfDownstreamCapabServicesTransport = _DocsDrfDownstreamCapabServicesTransport_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 3, 1, 8),
    _DocsDrfDownstreamCapabServicesTransport_Type()
)
docsDrfDownstreamCapabServicesTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDrfDownstreamCapabServicesTransport.setStatus("current")


class _DocsDrfDownstreamCapabMuting_Type(Bits):
    """Custom type docsDrfDownstreamCapabMuting based on Bits"""
    namedValues = NamedValues(
        ("qamDependency", 0)
    )

_DocsDrfDownstreamCapabMuting_Type.__name__ = "Bits"
_DocsDrfDownstreamCapabMuting_Object = MibTableColumn
docsDrfDownstreamCapabMuting = _DocsDrfDownstreamCapabMuting_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 3, 1, 9),
    _DocsDrfDownstreamCapabMuting_Type()
)
docsDrfDownstreamCapabMuting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDrfDownstreamCapabMuting.setStatus("current")
_DocsDrfGroupDependencyTable_Object = MibTable
docsDrfGroupDependencyTable = _DocsDrfGroupDependencyTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 4)
)
if mibBuilder.loadTexts:
    docsDrfGroupDependencyTable.setStatus("current")
_DocsDrfGroupDependencyEntry_Object = MibTableRow
docsDrfGroupDependencyEntry = _DocsDrfGroupDependencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 4, 1)
)
docsDrfGroupDependencyEntry.setIndexNames(
    (0, "DOCS-DRF-MIB", "docsDrfGroupDependencyPhyParam"),
    (0, "DOCS-DRF-MIB", "docsDrfGroupDependencyPhysicalIndex"),
)
if mibBuilder.loadTexts:
    docsDrfGroupDependencyEntry.setStatus("current")


class _DocsDrfGroupDependencyPhyParam_Type(Integer32):
    """Custom type docsDrfGroupDependencyPhyParam based on Integer32"""
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("annex", 7),
          ("bandwidth", 3),
          ("frequency", 2),
          ("interleave", 6),
          ("modulation", 5),
          ("mute", 9),
          ("noDependencies", 0),
          ("power", 4),
          ("symbolRate", 8))
    )


_DocsDrfGroupDependencyPhyParam_Type.__name__ = "Integer32"
_DocsDrfGroupDependencyPhyParam_Object = MibTableColumn
docsDrfGroupDependencyPhyParam = _DocsDrfGroupDependencyPhyParam_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 4, 1, 1),
    _DocsDrfGroupDependencyPhyParam_Type()
)
docsDrfGroupDependencyPhyParam.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsDrfGroupDependencyPhyParam.setStatus("current")
_DocsDrfGroupDependencyPhysicalIndex_Type = PhysicalIndexOrZero
_DocsDrfGroupDependencyPhysicalIndex_Object = MibTableColumn
docsDrfGroupDependencyPhysicalIndex = _DocsDrfGroupDependencyPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 4, 1, 2),
    _DocsDrfGroupDependencyPhysicalIndex_Type()
)
docsDrfGroupDependencyPhysicalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsDrfGroupDependencyPhysicalIndex.setStatus("current")


class _DocsDrfGroupDependencyGroupID_Type(Unsigned32):
    """Custom type docsDrfGroupDependencyGroupID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_DocsDrfGroupDependencyGroupID_Type.__name__ = "Unsigned32"
_DocsDrfGroupDependencyGroupID_Object = MibTableColumn
docsDrfGroupDependencyGroupID = _DocsDrfGroupDependencyGroupID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 4, 1, 3),
    _DocsDrfGroupDependencyGroupID_Type()
)
docsDrfGroupDependencyGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDrfGroupDependencyGroupID.setStatus("current")
_DocsDrfGroupDependencyType_Type = AutonomousType
_DocsDrfGroupDependencyType_Object = MibTableColumn
docsDrfGroupDependencyType = _DocsDrfGroupDependencyType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 4, 1, 4),
    _DocsDrfGroupDependencyType_Type()
)
docsDrfGroupDependencyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDrfGroupDependencyType.setStatus("current")
_DocsDrfChannelBlockTable_Object = MibTable
docsDrfChannelBlockTable = _DocsDrfChannelBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 5)
)
if mibBuilder.loadTexts:
    docsDrfChannelBlockTable.setStatus("current")
_DocsDrfChannelBlockEntry_Object = MibTableRow
docsDrfChannelBlockEntry = _DocsDrfChannelBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 5, 1)
)
docsDrfChannelBlockEntry.setIndexNames(
    (0, "DOCS-DRF-MIB", "docsDrfChannelBlockPhysicalIndex"),
)
if mibBuilder.loadTexts:
    docsDrfChannelBlockEntry.setStatus("current")
_DocsDrfChannelBlockPhysicalIndex_Type = PhysicalIndex
_DocsDrfChannelBlockPhysicalIndex_Object = MibTableColumn
docsDrfChannelBlockPhysicalIndex = _DocsDrfChannelBlockPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 5, 1, 1),
    _DocsDrfChannelBlockPhysicalIndex_Type()
)
docsDrfChannelBlockPhysicalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsDrfChannelBlockPhysicalIndex.setStatus("current")
_DocsDrfChannelBlockNumberChannels_Type = Unsigned32
_DocsDrfChannelBlockNumberChannels_Object = MibTableColumn
docsDrfChannelBlockNumberChannels = _DocsDrfChannelBlockNumberChannels_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 5, 1, 2),
    _DocsDrfChannelBlockNumberChannels_Type()
)
docsDrfChannelBlockNumberChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDrfChannelBlockNumberChannels.setStatus("current")
_DocsDrfChannelBlockCfgNumberChannels_Type = Unsigned32
_DocsDrfChannelBlockCfgNumberChannels_Object = MibTableColumn
docsDrfChannelBlockCfgNumberChannels = _DocsDrfChannelBlockCfgNumberChannels_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 5, 1, 3),
    _DocsDrfChannelBlockCfgNumberChannels_Type()
)
docsDrfChannelBlockCfgNumberChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDrfChannelBlockCfgNumberChannels.setStatus("current")
_DocsDrfChannelBlockMute_Type = TruthValue
_DocsDrfChannelBlockMute_Object = MibTableColumn
docsDrfChannelBlockMute = _DocsDrfChannelBlockMute_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 5, 1, 4),
    _DocsDrfChannelBlockMute_Type()
)
docsDrfChannelBlockMute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDrfChannelBlockMute.setStatus("current")


class _DocsDrfChannelBlockTestType_Type(Integer32):
    """Custom type docsDrfChannelBlockTestType based on Integer32"""
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
        *(("allOff", 3),
          ("clockTest", 7),
          ("cwOnOthersNormal", 6),
          ("cwOnOthersOff", 5),
          ("noTest", 1),
          ("offOthersNormal", 2),
          ("onOthersOff", 4))
    )


_DocsDrfChannelBlockTestType_Type.__name__ = "Integer32"
_DocsDrfChannelBlockTestType_Object = MibTableColumn
docsDrfChannelBlockTestType = _DocsDrfChannelBlockTestType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 5, 1, 5),
    _DocsDrfChannelBlockTestType_Type()
)
docsDrfChannelBlockTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDrfChannelBlockTestType.setStatus("current")
_DocsDrfChannelBlockTestIfIndex_Type = InterfaceIndexOrZero
_DocsDrfChannelBlockTestIfIndex_Object = MibTableColumn
docsDrfChannelBlockTestIfIndex = _DocsDrfChannelBlockTestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 1, 5, 1, 6),
    _DocsDrfChannelBlockTestIfIndex_Type()
)
docsDrfChannelBlockTestIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDrfChannelBlockTestIfIndex.setStatus("current")
_DocsDrfConformance_ObjectIdentity = ObjectIdentity
docsDrfConformance = _DocsDrfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 2)
)
_DocsDrfCompliances_ObjectIdentity = ObjectIdentity
docsDrfCompliances = _DocsDrfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 2, 1)
)
_DocsDrfGroups_ObjectIdentity = ObjectIdentity
docsDrfGroups = _DocsDrfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 2, 2)
)
docsIfDownstreamChannelEntry.registerAugmentions(
    ("DOCS-DRF-MIB",
     "docsDrfDownstreamEntry")
)
docsDrfDownstreamEntry.setIndexNames(*docsIfDownstreamChannelEntry.getIndexNames())

# Managed Objects groups

docsDrfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 2, 2, 1)
)
docsDrfGroup.setObjects(
      *(("DOCS-DRF-MIB", "docsDrfDownstreamCapabFrequency"),
        ("DOCS-DRF-MIB", "docsDrfDownstreamCapabBandwidth"),
        ("DOCS-DRF-MIB", "docsDrfDownstreamCapabPower"),
        ("DOCS-DRF-MIB", "docsDrfDownstreamCapabModulation"),
        ("DOCS-DRF-MIB", "docsDrfDownstreamCapabInterleaver"),
        ("DOCS-DRF-MIB", "docsDrfDownstreamCapabJ83Annex"),
        ("DOCS-DRF-MIB", "docsDrfDownstreamCapabConcurrentServices"),
        ("DOCS-DRF-MIB", "docsDrfDownstreamCapabServicesTransport"),
        ("DOCS-DRF-MIB", "docsDrfDownstreamCapabMuting"),
        ("DOCS-DRF-MIB", "docsDrfGroupDependencyGroupID"),
        ("DOCS-DRF-MIB", "docsDrfGroupDependencyType"),
        ("DOCS-DRF-MIB", "docsDrfChannelBlockNumberChannels"),
        ("DOCS-DRF-MIB", "docsDrfChannelBlockCfgNumberChannels"),
        ("DOCS-DRF-MIB", "docsDrfChannelBlockMute"),
        ("DOCS-DRF-MIB", "docsDrfChannelBlockTestType"),
        ("DOCS-DRF-MIB", "docsDrfChannelBlockTestIfIndex"))
)
if mibBuilder.loadTexts:
    docsDrfGroup.setStatus("current")

docsDrfCmtsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 2, 2, 2)
)
docsDrfCmtsGroup.setObjects(
    ("DOCS-DRF-MIB", "docsDrfDownstreamPhyDependencies")
)
if mibBuilder.loadTexts:
    docsDrfCmtsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

docsDrfDeviceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 2, 1, 1)
)
if mibBuilder.loadTexts:
    docsDrfDeviceCompliance.setStatus(
        "current"
    )

docsDrfCmtsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 23, 2, 1, 2)
)
if mibBuilder.loadTexts:
    docsDrfCmtsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-DRF-MIB",
    **{"docsDrfMib": docsDrfMib,
       "docsDrfNotifications": docsDrfNotifications,
       "docsDrfObjects": docsDrfObjects,
       "docsDrfRegistry": docsDrfRegistry,
       "docsDrfPhyParamFixValue": docsDrfPhyParamFixValue,
       "docsDrfPhyParamSameValue": docsDrfPhyParamSameValue,
       "docsDrfPhyParamAdjacentValues": docsDrfPhyParamAdjacentValues,
       "docsDrfPhyParamFrequencyRange": docsDrfPhyParamFrequencyRange,
       "docsDrfDownstreamTable": docsDrfDownstreamTable,
       "docsDrfDownstreamEntry": docsDrfDownstreamEntry,
       "docsDrfDownstreamPhyDependencies": docsDrfDownstreamPhyDependencies,
       "docsDrfDownstreamCapabilitiesTable": docsDrfDownstreamCapabilitiesTable,
       "docsDrfDownstreamCapabilitiesEntry": docsDrfDownstreamCapabilitiesEntry,
       "docsDrfDownstreamCapabFrequency": docsDrfDownstreamCapabFrequency,
       "docsDrfDownstreamCapabBandwidth": docsDrfDownstreamCapabBandwidth,
       "docsDrfDownstreamCapabPower": docsDrfDownstreamCapabPower,
       "docsDrfDownstreamCapabModulation": docsDrfDownstreamCapabModulation,
       "docsDrfDownstreamCapabInterleaver": docsDrfDownstreamCapabInterleaver,
       "docsDrfDownstreamCapabJ83Annex": docsDrfDownstreamCapabJ83Annex,
       "docsDrfDownstreamCapabConcurrentServices": docsDrfDownstreamCapabConcurrentServices,
       "docsDrfDownstreamCapabServicesTransport": docsDrfDownstreamCapabServicesTransport,
       "docsDrfDownstreamCapabMuting": docsDrfDownstreamCapabMuting,
       "docsDrfGroupDependencyTable": docsDrfGroupDependencyTable,
       "docsDrfGroupDependencyEntry": docsDrfGroupDependencyEntry,
       "docsDrfGroupDependencyPhyParam": docsDrfGroupDependencyPhyParam,
       "docsDrfGroupDependencyPhysicalIndex": docsDrfGroupDependencyPhysicalIndex,
       "docsDrfGroupDependencyGroupID": docsDrfGroupDependencyGroupID,
       "docsDrfGroupDependencyType": docsDrfGroupDependencyType,
       "docsDrfChannelBlockTable": docsDrfChannelBlockTable,
       "docsDrfChannelBlockEntry": docsDrfChannelBlockEntry,
       "docsDrfChannelBlockPhysicalIndex": docsDrfChannelBlockPhysicalIndex,
       "docsDrfChannelBlockNumberChannels": docsDrfChannelBlockNumberChannels,
       "docsDrfChannelBlockCfgNumberChannels": docsDrfChannelBlockCfgNumberChannels,
       "docsDrfChannelBlockMute": docsDrfChannelBlockMute,
       "docsDrfChannelBlockTestType": docsDrfChannelBlockTestType,
       "docsDrfChannelBlockTestIfIndex": docsDrfChannelBlockTestIfIndex,
       "docsDrfConformance": docsDrfConformance,
       "docsDrfCompliances": docsDrfCompliances,
       "docsDrfDeviceCompliance": docsDrfDeviceCompliance,
       "docsDrfCmtsCompliance": docsDrfCmtsCompliance,
       "docsDrfGroups": docsDrfGroups,
       "docsDrfGroup": docsDrfGroup,
       "docsDrfCmtsGroup": docsDrfCmtsGroup}
)
