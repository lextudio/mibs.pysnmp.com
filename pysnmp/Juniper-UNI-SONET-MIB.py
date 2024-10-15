# SNMP MIB module (Juniper-UNI-SONET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-UNI-SONET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:34 2024
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
 InterfaceIndexOrZero,
 ifAlias,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifAlias",
    "ifIndex")

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniNextIfIndex,) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniNextIfIndex")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

juniSonetMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7)
)
juniSonetMIB.setRevisions(
        ("2003-07-16 19:52",
         "2002-11-22 16:37",
         "2001-10-10 20:42",
         "2001-01-02 18:00",
         "1998-11-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniSonetLineSpeed(Integer32, TextualConvention):
    status = "current"
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
        *(("sonetOc12Stm3", 3),
          ("sonetOc1Stm0", 1),
          ("sonetOc3Stm1", 2),
          ("sonetOc48Stm16", 4),
          ("sonetUnknownSpeed", 0))
    )



class JuniSonetLogicalPathChannel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class JuniSonetPathHierarchy(OctetString, TextualConvention):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class JuniSonetPathC2ByteOverride(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class JuniSonetVTType(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("tribVT15TU11", 0),
          ("tribVT20TU12", 1),
          ("tribVT3", 3),
          ("tribVT6", 4),
          ("tribVT6c", 5))
    )



# MIB Managed Objects in the order of their OIDs

_JuniSonetObjects_ObjectIdentity = ObjectIdentity
juniSonetObjects = _JuniSonetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1)
)
_JuniSonetMediumTable_Object = MibTable
juniSonetMediumTable = _JuniSonetMediumTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    juniSonetMediumTable.setStatus("current")
_JuniSonetMediumEntry_Object = MibTableRow
juniSonetMediumEntry = _JuniSonetMediumEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1, 1, 1)
)
juniSonetMediumEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    juniSonetMediumEntry.setStatus("current")


class _JuniSonetMediumType_Type(Integer32):
    """Custom type juniSonetMediumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdh", 2),
          ("sonet", 1))
    )


_JuniSonetMediumType_Type.__name__ = "Integer32"
_JuniSonetMediumType_Object = MibTableColumn
juniSonetMediumType = _JuniSonetMediumType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1, 1, 1, 1),
    _JuniSonetMediumType_Type()
)
juniSonetMediumType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSonetMediumType.setStatus("deprecated")


class _JuniSonetMediumLoopbackConfig_Type(Integer32):
    """Custom type juniSonetMediumLoopbackConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sonetFacilityLoop", 1),
          ("sonetNoLoop", 0),
          ("sonetOtherLoop", 3),
          ("sonetTerminalLoop", 2))
    )


_JuniSonetMediumLoopbackConfig_Type.__name__ = "Integer32"
_JuniSonetMediumLoopbackConfig_Object = MibTableColumn
juniSonetMediumLoopbackConfig = _JuniSonetMediumLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1, 1, 1, 2),
    _JuniSonetMediumLoopbackConfig_Type()
)
juniSonetMediumLoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSonetMediumLoopbackConfig.setStatus("current")


class _JuniSonetMediumTimingSource_Type(Integer32):
    """Custom type juniSonetMediumTimingSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internalChassis", 2),
          ("internalModule", 1),
          ("loop", 0))
    )


_JuniSonetMediumTimingSource_Type.__name__ = "Integer32"
_JuniSonetMediumTimingSource_Object = MibTableColumn
juniSonetMediumTimingSource = _JuniSonetMediumTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1, 1, 1, 3),
    _JuniSonetMediumTimingSource_Type()
)
juniSonetMediumTimingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSonetMediumTimingSource.setStatus("current")
_JuniSonetMediumCircuitIdentifier_Type = DisplayString
_JuniSonetMediumCircuitIdentifier_Object = MibTableColumn
juniSonetMediumCircuitIdentifier = _JuniSonetMediumCircuitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1, 1, 1, 4),
    _JuniSonetMediumCircuitIdentifier_Type()
)
juniSonetMediumCircuitIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSonetMediumCircuitIdentifier.setStatus("deprecated")


class _JuniSonetMediumTriggerAlarms_Type(Bits):
    """Custom type juniSonetMediumTriggerAlarms based on Bits"""
    defaultBinValue = "1011"

    namedValues = NamedValues(
        *(("lineAIS", 2),
          ("lineRDI", 3),
          ("sectionLOF", 1),
          ("sectionLOS", 0))
    )

_JuniSonetMediumTriggerAlarms_Type.__name__ = "Bits"
_JuniSonetMediumTriggerAlarms_Object = MibTableColumn
juniSonetMediumTriggerAlarms = _JuniSonetMediumTriggerAlarms_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1, 1, 1, 5),
    _JuniSonetMediumTriggerAlarms_Type()
)
juniSonetMediumTriggerAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSonetMediumTriggerAlarms.setStatus("current")


class _JuniSonetMediumTriggerDelay_Type(Integer32):
    """Custom type juniSonetMediumTriggerDelay based on Integer32"""
    defaultValue = 2500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2500),
    )


_JuniSonetMediumTriggerDelay_Type.__name__ = "Integer32"
_JuniSonetMediumTriggerDelay_Object = MibTableColumn
juniSonetMediumTriggerDelay = _JuniSonetMediumTriggerDelay_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1, 1, 1, 6),
    _JuniSonetMediumTriggerDelay_Type()
)
juniSonetMediumTriggerDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSonetMediumTriggerDelay.setStatus("current")
if mibBuilder.loadTexts:
    juniSonetMediumTriggerDelay.setUnits("ms")
_JuniSonetPathObjects_ObjectIdentity = ObjectIdentity
juniSonetPathObjects = _JuniSonetPathObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2)
)
_JuniSonetPathCapabilityTable_Object = MibTable
juniSonetPathCapabilityTable = _JuniSonetPathCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 1)
)
if mibBuilder.loadTexts:
    juniSonetPathCapabilityTable.setStatus("current")
_JuniSonetPathCapabilityEntry_Object = MibTableRow
juniSonetPathCapabilityEntry = _JuniSonetPathCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 1, 1)
)
juniSonetPathCapabilityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    juniSonetPathCapabilityEntry.setStatus("current")
_JuniSonetPathRemoveFlag_Type = TruthValue
_JuniSonetPathRemoveFlag_Object = MibTableColumn
juniSonetPathRemoveFlag = _JuniSonetPathRemoveFlag_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 1, 1, 1),
    _JuniSonetPathRemoveFlag_Type()
)
juniSonetPathRemoveFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSonetPathRemoveFlag.setStatus("current")
_JuniSonetPathChannelized_Type = TruthValue
_JuniSonetPathChannelized_Object = MibTableColumn
juniSonetPathChannelized = _JuniSonetPathChannelized_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 1, 1, 2),
    _JuniSonetPathChannelized_Type()
)
juniSonetPathChannelized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSonetPathChannelized.setStatus("current")
_JuniSonetPathMaximumChannels_Type = Unsigned32
_JuniSonetPathMaximumChannels_Object = MibTableColumn
juniSonetPathMaximumChannels = _JuniSonetPathMaximumChannels_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 1, 1, 3),
    _JuniSonetPathMaximumChannels_Type()
)
juniSonetPathMaximumChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSonetPathMaximumChannels.setStatus("current")
_JuniSonetPathMinimumPathSpeed_Type = JuniSonetLineSpeed
_JuniSonetPathMinimumPathSpeed_Object = MibTableColumn
juniSonetPathMinimumPathSpeed = _JuniSonetPathMinimumPathSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 1, 1, 4),
    _JuniSonetPathMinimumPathSpeed_Type()
)
juniSonetPathMinimumPathSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSonetPathMinimumPathSpeed.setStatus("current")
_JuniSonetPathMaximumPathSpeed_Type = JuniSonetLineSpeed
_JuniSonetPathMaximumPathSpeed_Object = MibTableColumn
juniSonetPathMaximumPathSpeed = _JuniSonetPathMaximumPathSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 1, 1, 5),
    _JuniSonetPathMaximumPathSpeed_Type()
)
juniSonetPathMaximumPathSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSonetPathMaximumPathSpeed.setStatus("current")
_JuniSonetPathNextIfIndex_Type = JuniNextIfIndex
_JuniSonetPathNextIfIndex_Object = MibScalar
juniSonetPathNextIfIndex = _JuniSonetPathNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 2),
    _JuniSonetPathNextIfIndex_Type()
)
juniSonetPathNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSonetPathNextIfIndex.setStatus("current")
_JuniSonetPathTable_Object = MibTable
juniSonetPathTable = _JuniSonetPathTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3)
)
if mibBuilder.loadTexts:
    juniSonetPathTable.setStatus("current")
_JuniSonetPathEntry_Object = MibTableRow
juniSonetPathEntry = _JuniSonetPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1)
)
juniSonetPathEntry.setIndexNames(
    (0, "Juniper-UNI-SONET-MIB", "juniSonetPathIfIndex"),
)
if mibBuilder.loadTexts:
    juniSonetPathEntry.setStatus("current")
_JuniSonetPathIfIndex_Type = InterfaceIndex
_JuniSonetPathIfIndex_Object = MibTableColumn
juniSonetPathIfIndex = _JuniSonetPathIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 1),
    _JuniSonetPathIfIndex_Type()
)
juniSonetPathIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniSonetPathIfIndex.setStatus("current")
_JuniSonetPathLogicalChannel_Type = JuniSonetLogicalPathChannel
_JuniSonetPathLogicalChannel_Object = MibTableColumn
juniSonetPathLogicalChannel = _JuniSonetPathLogicalChannel_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 2),
    _JuniSonetPathLogicalChannel_Type()
)
juniSonetPathLogicalChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSonetPathLogicalChannel.setStatus("current")
_JuniSonetPathSpeed_Type = JuniSonetLineSpeed
_JuniSonetPathSpeed_Object = MibTableColumn
juniSonetPathSpeed = _JuniSonetPathSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 3),
    _JuniSonetPathSpeed_Type()
)
juniSonetPathSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSonetPathSpeed.setStatus("current")
_JuniSonetPathHierarchy_Type = JuniSonetPathHierarchy
_JuniSonetPathHierarchy_Object = MibTableColumn
juniSonetPathHierarchy = _JuniSonetPathHierarchy_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 4),
    _JuniSonetPathHierarchy_Type()
)
juniSonetPathHierarchy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSonetPathHierarchy.setStatus("current")
_JuniSonetPathLowerIfIndex_Type = InterfaceIndexOrZero
_JuniSonetPathLowerIfIndex_Object = MibTableColumn
juniSonetPathLowerIfIndex = _JuniSonetPathLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 5),
    _JuniSonetPathLowerIfIndex_Type()
)
juniSonetPathLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSonetPathLowerIfIndex.setStatus("current")
_JuniSonetPathRowStatus_Type = RowStatus
_JuniSonetPathRowStatus_Object = MibTableColumn
juniSonetPathRowStatus = _JuniSonetPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 6),
    _JuniSonetPathRowStatus_Type()
)
juniSonetPathRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSonetPathRowStatus.setStatus("current")


class _JuniSonetPathTriggerAlarms_Type(Bits):
    """Custom type juniSonetPathTriggerAlarms based on Bits"""
    defaultBinValue = "11"

    namedValues = NamedValues(
        *(("pathAIS", 1),
          ("pathLOP", 0),
          ("pathRDI", 2))
    )

_JuniSonetPathTriggerAlarms_Type.__name__ = "Bits"
_JuniSonetPathTriggerAlarms_Object = MibTableColumn
juniSonetPathTriggerAlarms = _JuniSonetPathTriggerAlarms_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 7),
    _JuniSonetPathTriggerAlarms_Type()
)
juniSonetPathTriggerAlarms.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSonetPathTriggerAlarms.setStatus("current")


class _JuniSonetPathC2ByteOverrideFlag_Type(TruthValue):
    """Custom type juniSonetPathC2ByteOverrideFlag based on TruthValue"""


_JuniSonetPathC2ByteOverrideFlag_Object = MibTableColumn
juniSonetPathC2ByteOverrideFlag = _JuniSonetPathC2ByteOverrideFlag_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 8),
    _JuniSonetPathC2ByteOverrideFlag_Type()
)
juniSonetPathC2ByteOverrideFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSonetPathC2ByteOverrideFlag.setStatus("current")


class _JuniSonetPathC2ByteOverride_Type(JuniSonetPathC2ByteOverride):
    """Custom type juniSonetPathC2ByteOverride based on JuniSonetPathC2ByteOverride"""
    defaultValue = 0


_JuniSonetPathC2ByteOverride_Object = MibTableColumn
juniSonetPathC2ByteOverride = _JuniSonetPathC2ByteOverride_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 9),
    _JuniSonetPathC2ByteOverride_Type()
)
juniSonetPathC2ByteOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSonetPathC2ByteOverride.setStatus("current")


class _JuniSonetPathTriggerDelay_Type(Integer32):
    """Custom type juniSonetPathTriggerDelay based on Integer32"""
    defaultValue = 2500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2500),
    )


_JuniSonetPathTriggerDelay_Type.__name__ = "Integer32"
_JuniSonetPathTriggerDelay_Object = MibTableColumn
juniSonetPathTriggerDelay = _JuniSonetPathTriggerDelay_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 10),
    _JuniSonetPathTriggerDelay_Type()
)
juniSonetPathTriggerDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSonetPathTriggerDelay.setStatus("current")
if mibBuilder.loadTexts:
    juniSonetPathTriggerDelay.setUnits("ms")


class _JuniSonetPathEventStatus_Type(Unsigned32):
    """Custom type juniSonetPathEventStatus based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_JuniSonetPathEventStatus_Type.__name__ = "Unsigned32"
_JuniSonetPathEventStatus_Object = MibTableColumn
juniSonetPathEventStatus = _JuniSonetPathEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 11),
    _JuniSonetPathEventStatus_Type()
)
juniSonetPathEventStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniSonetPathEventStatus.setStatus("current")
_JuniSonetVTObjects_ObjectIdentity = ObjectIdentity
juniSonetVTObjects = _JuniSonetVTObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3)
)
_JuniSonetVTNextIfIndex_Type = JuniNextIfIndex
_JuniSonetVTNextIfIndex_Object = MibScalar
juniSonetVTNextIfIndex = _JuniSonetVTNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 1),
    _JuniSonetVTNextIfIndex_Type()
)
juniSonetVTNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSonetVTNextIfIndex.setStatus("current")
_JuniSonetVTTable_Object = MibTable
juniSonetVTTable = _JuniSonetVTTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2)
)
if mibBuilder.loadTexts:
    juniSonetVTTable.setStatus("current")
_JuniSonetVTEntry_Object = MibTableRow
juniSonetVTEntry = _JuniSonetVTEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1)
)
juniSonetVTEntry.setIndexNames(
    (0, "Juniper-UNI-SONET-MIB", "juniSonetVTIfIndex"),
)
if mibBuilder.loadTexts:
    juniSonetVTEntry.setStatus("current")
_JuniSonetVTIfIndex_Type = InterfaceIndex
_JuniSonetVTIfIndex_Object = MibTableColumn
juniSonetVTIfIndex = _JuniSonetVTIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 1),
    _JuniSonetVTIfIndex_Type()
)
juniSonetVTIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniSonetVTIfIndex.setStatus("current")
_JuniSonetVTPathLogicalChannel_Type = JuniSonetLogicalPathChannel
_JuniSonetVTPathLogicalChannel_Object = MibTableColumn
juniSonetVTPathLogicalChannel = _JuniSonetVTPathLogicalChannel_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 2),
    _JuniSonetVTPathLogicalChannel_Type()
)
juniSonetVTPathLogicalChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSonetVTPathLogicalChannel.setStatus("current")
_JuniSonetVTType_Type = JuniSonetVTType
_JuniSonetVTType_Object = MibTableColumn
juniSonetVTType = _JuniSonetVTType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 3),
    _JuniSonetVTType_Type()
)
juniSonetVTType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSonetVTType.setStatus("deprecated")
_JuniSonetVTPathPayload_Type = Unsigned32
_JuniSonetVTPathPayload_Object = MibTableColumn
juniSonetVTPathPayload = _JuniSonetVTPathPayload_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 4),
    _JuniSonetVTPathPayload_Type()
)
juniSonetVTPathPayload.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSonetVTPathPayload.setStatus("current")
_JuniSonetVTTributaryGroup_Type = Unsigned32
_JuniSonetVTTributaryGroup_Object = MibTableColumn
juniSonetVTTributaryGroup = _JuniSonetVTTributaryGroup_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 5),
    _JuniSonetVTTributaryGroup_Type()
)
juniSonetVTTributaryGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSonetVTTributaryGroup.setStatus("current")
_JuniSonetVTTributarySubChannel_Type = Unsigned32
_JuniSonetVTTributarySubChannel_Object = MibTableColumn
juniSonetVTTributarySubChannel = _JuniSonetVTTributarySubChannel_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 6),
    _JuniSonetVTTributarySubChannel_Type()
)
juniSonetVTTributarySubChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSonetVTTributarySubChannel.setStatus("current")
_JuniSonetVTLowerIfIndex_Type = InterfaceIndexOrZero
_JuniSonetVTLowerIfIndex_Object = MibTableColumn
juniSonetVTLowerIfIndex = _JuniSonetVTLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 7),
    _JuniSonetVTLowerIfIndex_Type()
)
juniSonetVTLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSonetVTLowerIfIndex.setStatus("current")
_JuniSonetVTRowStatus_Type = RowStatus
_JuniSonetVTRowStatus_Object = MibTableColumn
juniSonetVTRowStatus = _JuniSonetVTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 8),
    _JuniSonetVTRowStatus_Type()
)
juniSonetVTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSonetVTRowStatus.setStatus("current")
_JuniSonetConformance_ObjectIdentity = ObjectIdentity
juniSonetConformance = _JuniSonetConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4)
)
_JuniSonetCompliances_ObjectIdentity = ObjectIdentity
juniSonetCompliances = _JuniSonetCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 1)
)
_JuniSonetGroups_ObjectIdentity = ObjectIdentity
juniSonetGroups = _JuniSonetGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2)
)
_JuniSonetTrapControl_ObjectIdentity = ObjectIdentity
juniSonetTrapControl = _JuniSonetTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 5)
)
_JuniSonetPathEventIfIndex_Type = InterfaceIndex
_JuniSonetPathEventIfIndex_Object = MibScalar
juniSonetPathEventIfIndex = _JuniSonetPathEventIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 5, 1),
    _JuniSonetPathEventIfIndex_Type()
)
juniSonetPathEventIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniSonetPathEventIfIndex.setStatus("current")
_JuniSonetTraps_ObjectIdentity = ObjectIdentity
juniSonetTraps = _JuniSonetTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 6)
)
_JuniSonetTrapPrefix_ObjectIdentity = ObjectIdentity
juniSonetTrapPrefix = _JuniSonetTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 6, 0)
)

# Managed Objects groups

juniSonetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 1)
)
juniSonetGroup.setObjects(
      *(("Juniper-UNI-SONET-MIB", "juniSonetMediumType"),
        ("Juniper-UNI-SONET-MIB", "juniSonetMediumLoopbackConfig"),
        ("Juniper-UNI-SONET-MIB", "juniSonetMediumTimingSource"),
        ("Juniper-UNI-SONET-MIB", "juniSonetMediumCircuitIdentifier"))
)
if mibBuilder.loadTexts:
    juniSonetGroup.setStatus("obsolete")

juniSonetPathGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 2)
)
juniSonetPathGroup.setObjects(
      *(("Juniper-UNI-SONET-MIB", "juniSonetPathRemoveFlag"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathChannelized"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathMaximumChannels"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathMinimumPathSpeed"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathMaximumPathSpeed"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathNextIfIndex"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathLogicalChannel"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathSpeed"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathHierarchy"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathLowerIfIndex"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathRowStatus"))
)
if mibBuilder.loadTexts:
    juniSonetPathGroup.setStatus("obsolete")

juniSonetVirtualTributaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 3)
)
juniSonetVirtualTributaryGroup.setObjects(
      *(("Juniper-UNI-SONET-MIB", "juniSonetVTNextIfIndex"),
        ("Juniper-UNI-SONET-MIB", "juniSonetVTPathLogicalChannel"),
        ("Juniper-UNI-SONET-MIB", "juniSonetVTType"),
        ("Juniper-UNI-SONET-MIB", "juniSonetVTPathPayload"),
        ("Juniper-UNI-SONET-MIB", "juniSonetVTTributaryGroup"),
        ("Juniper-UNI-SONET-MIB", "juniSonetVTTributarySubChannel"),
        ("Juniper-UNI-SONET-MIB", "juniSonetVTLowerIfIndex"),
        ("Juniper-UNI-SONET-MIB", "juniSonetVTRowStatus"))
)
if mibBuilder.loadTexts:
    juniSonetVirtualTributaryGroup.setStatus("obsolete")

juniSonetGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 4)
)
juniSonetGroup2.setObjects(
      *(("Juniper-UNI-SONET-MIB", "juniSonetMediumLoopbackConfig"),
        ("Juniper-UNI-SONET-MIB", "juniSonetMediumTimingSource"))
)
if mibBuilder.loadTexts:
    juniSonetGroup2.setStatus("obsolete")

juniSonetVirtualTributaryGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 5)
)
juniSonetVirtualTributaryGroup2.setObjects(
      *(("Juniper-UNI-SONET-MIB", "juniSonetVTNextIfIndex"),
        ("Juniper-UNI-SONET-MIB", "juniSonetVTPathLogicalChannel"),
        ("Juniper-UNI-SONET-MIB", "juniSonetVTPathPayload"),
        ("Juniper-UNI-SONET-MIB", "juniSonetVTTributaryGroup"),
        ("Juniper-UNI-SONET-MIB", "juniSonetVTTributarySubChannel"),
        ("Juniper-UNI-SONET-MIB", "juniSonetVTLowerIfIndex"),
        ("Juniper-UNI-SONET-MIB", "juniSonetVTRowStatus"))
)
if mibBuilder.loadTexts:
    juniSonetVirtualTributaryGroup2.setStatus("current")

juniSonetDeprecatedMediumGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 6)
)
juniSonetDeprecatedMediumGroup.setObjects(
      *(("Juniper-UNI-SONET-MIB", "juniSonetMediumType"),
        ("Juniper-UNI-SONET-MIB", "juniSonetMediumCircuitIdentifier"))
)
if mibBuilder.loadTexts:
    juniSonetDeprecatedMediumGroup.setStatus("deprecated")

juniSonetDeprecatedVTGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 7)
)
juniSonetDeprecatedVTGroup.setObjects(
    ("Juniper-UNI-SONET-MIB", "juniSonetVTType")
)
if mibBuilder.loadTexts:
    juniSonetDeprecatedVTGroup.setStatus("deprecated")

juniSonetGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 8)
)
juniSonetGroup3.setObjects(
      *(("Juniper-UNI-SONET-MIB", "juniSonetMediumLoopbackConfig"),
        ("Juniper-UNI-SONET-MIB", "juniSonetMediumTimingSource"),
        ("Juniper-UNI-SONET-MIB", "juniSonetMediumTriggerAlarms"),
        ("Juniper-UNI-SONET-MIB", "juniSonetMediumTriggerDelay"))
)
if mibBuilder.loadTexts:
    juniSonetGroup3.setStatus("current")

juniSonetPathGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 9)
)
juniSonetPathGroup2.setObjects(
      *(("Juniper-UNI-SONET-MIB", "juniSonetPathRemoveFlag"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathChannelized"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathMaximumChannels"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathMinimumPathSpeed"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathMaximumPathSpeed"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathNextIfIndex"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathLogicalChannel"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathSpeed"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathHierarchy"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathLowerIfIndex"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathRowStatus"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathTriggerAlarms"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathC2ByteOverrideFlag"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathC2ByteOverride"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathTriggerDelay"))
)
if mibBuilder.loadTexts:
    juniSonetPathGroup2.setStatus("obsolete")

juniSonetPathGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 10)
)
juniSonetPathGroup3.setObjects(
      *(("Juniper-UNI-SONET-MIB", "juniSonetPathRemoveFlag"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathChannelized"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathMaximumChannels"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathMinimumPathSpeed"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathMaximumPathSpeed"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathNextIfIndex"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathLogicalChannel"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathSpeed"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathHierarchy"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathLowerIfIndex"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathRowStatus"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathTriggerAlarms"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathC2ByteOverrideFlag"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathC2ByteOverride"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathTriggerDelay"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathEventIfIndex"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathEventStatus"))
)
if mibBuilder.loadTexts:
    juniSonetPathGroup3.setStatus("current")


# Notification objects

juniSonetPathEvents = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 6, 0, 1)
)
juniSonetPathEvents.setObjects(
      *(("Juniper-UNI-SONET-MIB", "juniSonetPathEventIfIndex"),
        ("Juniper-UNI-SONET-MIB", "juniSonetPathEventStatus"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    juniSonetPathEvents.setStatus(
        "current"
    )


# Notifications groups

juniSonetPathNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 11)
)
juniSonetPathNotificationGroup.setObjects(
    ("Juniper-UNI-SONET-MIB", "juniSonetPathEvents")
)
if mibBuilder.loadTexts:
    juniSonetPathNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

juniSonetCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniSonetCompliance.setStatus(
        "obsolete"
    )

juniSonetCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniSonetCompliance2.setStatus(
        "obsolete"
    )

juniSonetCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 1, 3)
)
if mibBuilder.loadTexts:
    juniSonetCompliance3.setStatus(
        "obsolete"
    )

juniSonetCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 1, 4)
)
if mibBuilder.loadTexts:
    juniSonetCompliance4.setStatus(
        "obsolete"
    )

juniSonetCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 1, 5)
)
if mibBuilder.loadTexts:
    juniSonetCompliance5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-UNI-SONET-MIB",
    **{"JuniSonetLineSpeed": JuniSonetLineSpeed,
       "JuniSonetLogicalPathChannel": JuniSonetLogicalPathChannel,
       "JuniSonetPathHierarchy": JuniSonetPathHierarchy,
       "JuniSonetPathC2ByteOverride": JuniSonetPathC2ByteOverride,
       "JuniSonetVTType": JuniSonetVTType,
       "juniSonetMIB": juniSonetMIB,
       "juniSonetObjects": juniSonetObjects,
       "juniSonetMediumTable": juniSonetMediumTable,
       "juniSonetMediumEntry": juniSonetMediumEntry,
       "juniSonetMediumType": juniSonetMediumType,
       "juniSonetMediumLoopbackConfig": juniSonetMediumLoopbackConfig,
       "juniSonetMediumTimingSource": juniSonetMediumTimingSource,
       "juniSonetMediumCircuitIdentifier": juniSonetMediumCircuitIdentifier,
       "juniSonetMediumTriggerAlarms": juniSonetMediumTriggerAlarms,
       "juniSonetMediumTriggerDelay": juniSonetMediumTriggerDelay,
       "juniSonetPathObjects": juniSonetPathObjects,
       "juniSonetPathCapabilityTable": juniSonetPathCapabilityTable,
       "juniSonetPathCapabilityEntry": juniSonetPathCapabilityEntry,
       "juniSonetPathRemoveFlag": juniSonetPathRemoveFlag,
       "juniSonetPathChannelized": juniSonetPathChannelized,
       "juniSonetPathMaximumChannels": juniSonetPathMaximumChannels,
       "juniSonetPathMinimumPathSpeed": juniSonetPathMinimumPathSpeed,
       "juniSonetPathMaximumPathSpeed": juniSonetPathMaximumPathSpeed,
       "juniSonetPathNextIfIndex": juniSonetPathNextIfIndex,
       "juniSonetPathTable": juniSonetPathTable,
       "juniSonetPathEntry": juniSonetPathEntry,
       "juniSonetPathIfIndex": juniSonetPathIfIndex,
       "juniSonetPathLogicalChannel": juniSonetPathLogicalChannel,
       "juniSonetPathSpeed": juniSonetPathSpeed,
       "juniSonetPathHierarchy": juniSonetPathHierarchy,
       "juniSonetPathLowerIfIndex": juniSonetPathLowerIfIndex,
       "juniSonetPathRowStatus": juniSonetPathRowStatus,
       "juniSonetPathTriggerAlarms": juniSonetPathTriggerAlarms,
       "juniSonetPathC2ByteOverrideFlag": juniSonetPathC2ByteOverrideFlag,
       "juniSonetPathC2ByteOverride": juniSonetPathC2ByteOverride,
       "juniSonetPathTriggerDelay": juniSonetPathTriggerDelay,
       "juniSonetPathEventStatus": juniSonetPathEventStatus,
       "juniSonetVTObjects": juniSonetVTObjects,
       "juniSonetVTNextIfIndex": juniSonetVTNextIfIndex,
       "juniSonetVTTable": juniSonetVTTable,
       "juniSonetVTEntry": juniSonetVTEntry,
       "juniSonetVTIfIndex": juniSonetVTIfIndex,
       "juniSonetVTPathLogicalChannel": juniSonetVTPathLogicalChannel,
       "juniSonetVTType": juniSonetVTType,
       "juniSonetVTPathPayload": juniSonetVTPathPayload,
       "juniSonetVTTributaryGroup": juniSonetVTTributaryGroup,
       "juniSonetVTTributarySubChannel": juniSonetVTTributarySubChannel,
       "juniSonetVTLowerIfIndex": juniSonetVTLowerIfIndex,
       "juniSonetVTRowStatus": juniSonetVTRowStatus,
       "juniSonetConformance": juniSonetConformance,
       "juniSonetCompliances": juniSonetCompliances,
       "juniSonetCompliance": juniSonetCompliance,
       "juniSonetCompliance2": juniSonetCompliance2,
       "juniSonetCompliance3": juniSonetCompliance3,
       "juniSonetCompliance4": juniSonetCompliance4,
       "juniSonetCompliance5": juniSonetCompliance5,
       "juniSonetGroups": juniSonetGroups,
       "juniSonetGroup": juniSonetGroup,
       "juniSonetPathGroup": juniSonetPathGroup,
       "juniSonetVirtualTributaryGroup": juniSonetVirtualTributaryGroup,
       "juniSonetGroup2": juniSonetGroup2,
       "juniSonetVirtualTributaryGroup2": juniSonetVirtualTributaryGroup2,
       "juniSonetDeprecatedMediumGroup": juniSonetDeprecatedMediumGroup,
       "juniSonetDeprecatedVTGroup": juniSonetDeprecatedVTGroup,
       "juniSonetGroup3": juniSonetGroup3,
       "juniSonetPathGroup2": juniSonetPathGroup2,
       "juniSonetPathGroup3": juniSonetPathGroup3,
       "juniSonetPathNotificationGroup": juniSonetPathNotificationGroup,
       "juniSonetTrapControl": juniSonetTrapControl,
       "juniSonetPathEventIfIndex": juniSonetPathEventIfIndex,
       "juniSonetTraps": juniSonetTraps,
       "juniSonetTrapPrefix": juniSonetTrapPrefix,
       "juniSonetPathEvents": juniSonetPathEvents}
)
