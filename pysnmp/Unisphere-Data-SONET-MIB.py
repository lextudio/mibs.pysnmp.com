# SNMP MIB module (Unisphere-Data-SONET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-SONET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:39 2024
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
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
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

(DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdNextIfIndex,) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdNextIfIndex")


# MODULE-IDENTITY

usdSonetMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7)
)
usdSonetMIB.setRevisions(
        ("2001-10-10 20:42",
         "2001-01-02 18:00",
         "1998-11-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UsdSonetLineSpeed(Integer32, TextualConvention):
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



class UsdSonetLogicalPathChannel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class UsdSonetPathHierarchy(OctetString, TextualConvention):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class UsdSonetVTType(Integer32, TextualConvention):
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

_UsdSonetObjects_ObjectIdentity = ObjectIdentity
usdSonetObjects = _UsdSonetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1)
)
_UsdSonetMediumTable_Object = MibTable
usdSonetMediumTable = _UsdSonetMediumTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    usdSonetMediumTable.setStatus("current")
_UsdSonetMediumEntry_Object = MibTableRow
usdSonetMediumEntry = _UsdSonetMediumEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1, 1, 1)
)
usdSonetMediumEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    usdSonetMediumEntry.setStatus("current")


class _UsdSonetMediumType_Type(Integer32):
    """Custom type usdSonetMediumType based on Integer32"""
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


_UsdSonetMediumType_Type.__name__ = "Integer32"
_UsdSonetMediumType_Object = MibTableColumn
usdSonetMediumType = _UsdSonetMediumType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1, 1, 1, 1),
    _UsdSonetMediumType_Type()
)
usdSonetMediumType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSonetMediumType.setStatus("deprecated")


class _UsdSonetMediumLoopbackConfig_Type(Integer32):
    """Custom type usdSonetMediumLoopbackConfig based on Integer32"""
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


_UsdSonetMediumLoopbackConfig_Type.__name__ = "Integer32"
_UsdSonetMediumLoopbackConfig_Object = MibTableColumn
usdSonetMediumLoopbackConfig = _UsdSonetMediumLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1, 1, 1, 2),
    _UsdSonetMediumLoopbackConfig_Type()
)
usdSonetMediumLoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSonetMediumLoopbackConfig.setStatus("current")


class _UsdSonetMediumTimingSource_Type(Integer32):
    """Custom type usdSonetMediumTimingSource based on Integer32"""
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


_UsdSonetMediumTimingSource_Type.__name__ = "Integer32"
_UsdSonetMediumTimingSource_Object = MibTableColumn
usdSonetMediumTimingSource = _UsdSonetMediumTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1, 1, 1, 3),
    _UsdSonetMediumTimingSource_Type()
)
usdSonetMediumTimingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSonetMediumTimingSource.setStatus("current")
_UsdSonetMediumCircuitIdentifier_Type = DisplayString
_UsdSonetMediumCircuitIdentifier_Object = MibTableColumn
usdSonetMediumCircuitIdentifier = _UsdSonetMediumCircuitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1, 1, 1, 4),
    _UsdSonetMediumCircuitIdentifier_Type()
)
usdSonetMediumCircuitIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSonetMediumCircuitIdentifier.setStatus("deprecated")
_UsdSonetPathObjects_ObjectIdentity = ObjectIdentity
usdSonetPathObjects = _UsdSonetPathObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2)
)
_UsdSonetPathCapabilityTable_Object = MibTable
usdSonetPathCapabilityTable = _UsdSonetPathCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 1)
)
if mibBuilder.loadTexts:
    usdSonetPathCapabilityTable.setStatus("current")
_UsdSonetPathCapabilityEntry_Object = MibTableRow
usdSonetPathCapabilityEntry = _UsdSonetPathCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 1, 1)
)
usdSonetPathCapabilityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    usdSonetPathCapabilityEntry.setStatus("current")
_UsdSonetPathRemoveFlag_Type = TruthValue
_UsdSonetPathRemoveFlag_Object = MibTableColumn
usdSonetPathRemoveFlag = _UsdSonetPathRemoveFlag_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 1, 1, 1),
    _UsdSonetPathRemoveFlag_Type()
)
usdSonetPathRemoveFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSonetPathRemoveFlag.setStatus("current")
_UsdSonetPathChannelized_Type = TruthValue
_UsdSonetPathChannelized_Object = MibTableColumn
usdSonetPathChannelized = _UsdSonetPathChannelized_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 1, 1, 2),
    _UsdSonetPathChannelized_Type()
)
usdSonetPathChannelized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSonetPathChannelized.setStatus("current")
_UsdSonetPathMaximumChannels_Type = Unsigned32
_UsdSonetPathMaximumChannels_Object = MibTableColumn
usdSonetPathMaximumChannels = _UsdSonetPathMaximumChannels_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 1, 1, 3),
    _UsdSonetPathMaximumChannels_Type()
)
usdSonetPathMaximumChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSonetPathMaximumChannels.setStatus("current")
_UsdSonetPathMinimumPathSpeed_Type = UsdSonetLineSpeed
_UsdSonetPathMinimumPathSpeed_Object = MibTableColumn
usdSonetPathMinimumPathSpeed = _UsdSonetPathMinimumPathSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 1, 1, 4),
    _UsdSonetPathMinimumPathSpeed_Type()
)
usdSonetPathMinimumPathSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSonetPathMinimumPathSpeed.setStatus("current")
_UsdSonetPathMaximumPathSpeed_Type = UsdSonetLineSpeed
_UsdSonetPathMaximumPathSpeed_Object = MibTableColumn
usdSonetPathMaximumPathSpeed = _UsdSonetPathMaximumPathSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 1, 1, 5),
    _UsdSonetPathMaximumPathSpeed_Type()
)
usdSonetPathMaximumPathSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSonetPathMaximumPathSpeed.setStatus("current")
_UsdSonetPathNextIfIndex_Type = UsdNextIfIndex
_UsdSonetPathNextIfIndex_Object = MibScalar
usdSonetPathNextIfIndex = _UsdSonetPathNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 2),
    _UsdSonetPathNextIfIndex_Type()
)
usdSonetPathNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSonetPathNextIfIndex.setStatus("current")
_UsdSonetPathTable_Object = MibTable
usdSonetPathTable = _UsdSonetPathTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3)
)
if mibBuilder.loadTexts:
    usdSonetPathTable.setStatus("current")
_UsdSonetPathEntry_Object = MibTableRow
usdSonetPathEntry = _UsdSonetPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1)
)
usdSonetPathEntry.setIndexNames(
    (0, "Unisphere-Data-SONET-MIB", "usdSonetPathIfIndex"),
)
if mibBuilder.loadTexts:
    usdSonetPathEntry.setStatus("current")
_UsdSonetPathIfIndex_Type = InterfaceIndex
_UsdSonetPathIfIndex_Object = MibTableColumn
usdSonetPathIfIndex = _UsdSonetPathIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 1),
    _UsdSonetPathIfIndex_Type()
)
usdSonetPathIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdSonetPathIfIndex.setStatus("current")
_UsdSonetPathLogicalChannel_Type = UsdSonetLogicalPathChannel
_UsdSonetPathLogicalChannel_Object = MibTableColumn
usdSonetPathLogicalChannel = _UsdSonetPathLogicalChannel_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 2),
    _UsdSonetPathLogicalChannel_Type()
)
usdSonetPathLogicalChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSonetPathLogicalChannel.setStatus("current")
_UsdSonetPathSpeed_Type = UsdSonetLineSpeed
_UsdSonetPathSpeed_Object = MibTableColumn
usdSonetPathSpeed = _UsdSonetPathSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 3),
    _UsdSonetPathSpeed_Type()
)
usdSonetPathSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSonetPathSpeed.setStatus("current")
_UsdSonetPathHierarchy_Type = UsdSonetPathHierarchy
_UsdSonetPathHierarchy_Object = MibTableColumn
usdSonetPathHierarchy = _UsdSonetPathHierarchy_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 4),
    _UsdSonetPathHierarchy_Type()
)
usdSonetPathHierarchy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSonetPathHierarchy.setStatus("current")
_UsdSonetPathLowerIfIndex_Type = InterfaceIndexOrZero
_UsdSonetPathLowerIfIndex_Object = MibTableColumn
usdSonetPathLowerIfIndex = _UsdSonetPathLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 5),
    _UsdSonetPathLowerIfIndex_Type()
)
usdSonetPathLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSonetPathLowerIfIndex.setStatus("current")
_UsdSonetPathRowStatus_Type = RowStatus
_UsdSonetPathRowStatus_Object = MibTableColumn
usdSonetPathRowStatus = _UsdSonetPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 6),
    _UsdSonetPathRowStatus_Type()
)
usdSonetPathRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSonetPathRowStatus.setStatus("current")
_UsdSonetVTObjects_ObjectIdentity = ObjectIdentity
usdSonetVTObjects = _UsdSonetVTObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3)
)
_UsdSonetVTNextIfIndex_Type = UsdNextIfIndex
_UsdSonetVTNextIfIndex_Object = MibScalar
usdSonetVTNextIfIndex = _UsdSonetVTNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 1),
    _UsdSonetVTNextIfIndex_Type()
)
usdSonetVTNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSonetVTNextIfIndex.setStatus("current")
_UsdSonetVTTable_Object = MibTable
usdSonetVTTable = _UsdSonetVTTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2)
)
if mibBuilder.loadTexts:
    usdSonetVTTable.setStatus("current")
_UsdSonetVTEntry_Object = MibTableRow
usdSonetVTEntry = _UsdSonetVTEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1)
)
usdSonetVTEntry.setIndexNames(
    (0, "Unisphere-Data-SONET-MIB", "usdSonetVTIfIndex"),
)
if mibBuilder.loadTexts:
    usdSonetVTEntry.setStatus("current")
_UsdSonetVTIfIndex_Type = InterfaceIndex
_UsdSonetVTIfIndex_Object = MibTableColumn
usdSonetVTIfIndex = _UsdSonetVTIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 1),
    _UsdSonetVTIfIndex_Type()
)
usdSonetVTIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdSonetVTIfIndex.setStatus("current")
_UsdSonetVTPathLogicalChannel_Type = UsdSonetLogicalPathChannel
_UsdSonetVTPathLogicalChannel_Object = MibTableColumn
usdSonetVTPathLogicalChannel = _UsdSonetVTPathLogicalChannel_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 2),
    _UsdSonetVTPathLogicalChannel_Type()
)
usdSonetVTPathLogicalChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSonetVTPathLogicalChannel.setStatus("current")
_UsdSonetVTType_Type = UsdSonetVTType
_UsdSonetVTType_Object = MibTableColumn
usdSonetVTType = _UsdSonetVTType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 3),
    _UsdSonetVTType_Type()
)
usdSonetVTType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSonetVTType.setStatus("deprecated")
_UsdSonetVTPathPayload_Type = Unsigned32
_UsdSonetVTPathPayload_Object = MibTableColumn
usdSonetVTPathPayload = _UsdSonetVTPathPayload_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 4),
    _UsdSonetVTPathPayload_Type()
)
usdSonetVTPathPayload.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSonetVTPathPayload.setStatus("current")
_UsdSonetVTTributaryGroup_Type = Unsigned32
_UsdSonetVTTributaryGroup_Object = MibTableColumn
usdSonetVTTributaryGroup = _UsdSonetVTTributaryGroup_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 5),
    _UsdSonetVTTributaryGroup_Type()
)
usdSonetVTTributaryGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSonetVTTributaryGroup.setStatus("current")
_UsdSonetVTTributarySubChannel_Type = Unsigned32
_UsdSonetVTTributarySubChannel_Object = MibTableColumn
usdSonetVTTributarySubChannel = _UsdSonetVTTributarySubChannel_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 6),
    _UsdSonetVTTributarySubChannel_Type()
)
usdSonetVTTributarySubChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSonetVTTributarySubChannel.setStatus("current")
_UsdSonetVTLowerIfIndex_Type = InterfaceIndexOrZero
_UsdSonetVTLowerIfIndex_Object = MibTableColumn
usdSonetVTLowerIfIndex = _UsdSonetVTLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 7),
    _UsdSonetVTLowerIfIndex_Type()
)
usdSonetVTLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSonetVTLowerIfIndex.setStatus("current")
_UsdSonetVTRowStatus_Type = RowStatus
_UsdSonetVTRowStatus_Object = MibTableColumn
usdSonetVTRowStatus = _UsdSonetVTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 8),
    _UsdSonetVTRowStatus_Type()
)
usdSonetVTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSonetVTRowStatus.setStatus("current")
_UsdSonetConformance_ObjectIdentity = ObjectIdentity
usdSonetConformance = _UsdSonetConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4)
)
_UsdSonetCompliances_ObjectIdentity = ObjectIdentity
usdSonetCompliances = _UsdSonetCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 1)
)
_UsdSonetGroups_ObjectIdentity = ObjectIdentity
usdSonetGroups = _UsdSonetGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2)
)

# Managed Objects groups

usdSonetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 1)
)
usdSonetGroup.setObjects(
      *(("Unisphere-Data-SONET-MIB", "usdSonetMediumType"),
        ("Unisphere-Data-SONET-MIB", "usdSonetMediumLoopbackConfig"),
        ("Unisphere-Data-SONET-MIB", "usdSonetMediumTimingSource"),
        ("Unisphere-Data-SONET-MIB", "usdSonetMediumCircuitIdentifier"))
)
if mibBuilder.loadTexts:
    usdSonetGroup.setStatus("deprecated")

usdSonetPathGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 2)
)
usdSonetPathGroup.setObjects(
      *(("Unisphere-Data-SONET-MIB", "usdSonetPathRemoveFlag"),
        ("Unisphere-Data-SONET-MIB", "usdSonetPathChannelized"),
        ("Unisphere-Data-SONET-MIB", "usdSonetPathMaximumChannels"),
        ("Unisphere-Data-SONET-MIB", "usdSonetPathMinimumPathSpeed"),
        ("Unisphere-Data-SONET-MIB", "usdSonetPathMaximumPathSpeed"),
        ("Unisphere-Data-SONET-MIB", "usdSonetPathNextIfIndex"),
        ("Unisphere-Data-SONET-MIB", "usdSonetPathLogicalChannel"),
        ("Unisphere-Data-SONET-MIB", "usdSonetPathSpeed"),
        ("Unisphere-Data-SONET-MIB", "usdSonetPathHierarchy"),
        ("Unisphere-Data-SONET-MIB", "usdSonetPathLowerIfIndex"),
        ("Unisphere-Data-SONET-MIB", "usdSonetPathRowStatus"))
)
if mibBuilder.loadTexts:
    usdSonetPathGroup.setStatus("current")

usdSonetVirtualTributaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 3)
)
usdSonetVirtualTributaryGroup.setObjects(
      *(("Unisphere-Data-SONET-MIB", "usdSonetVTNextIfIndex"),
        ("Unisphere-Data-SONET-MIB", "usdSonetVTPathLogicalChannel"),
        ("Unisphere-Data-SONET-MIB", "usdSonetVTType"),
        ("Unisphere-Data-SONET-MIB", "usdSonetVTPathPayload"),
        ("Unisphere-Data-SONET-MIB", "usdSonetVTTributaryGroup"),
        ("Unisphere-Data-SONET-MIB", "usdSonetVTTributarySubChannel"),
        ("Unisphere-Data-SONET-MIB", "usdSonetVTLowerIfIndex"),
        ("Unisphere-Data-SONET-MIB", "usdSonetVTRowStatus"))
)
if mibBuilder.loadTexts:
    usdSonetVirtualTributaryGroup.setStatus("deprecated")

usdSonetGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 4)
)
usdSonetGroup2.setObjects(
      *(("Unisphere-Data-SONET-MIB", "usdSonetMediumLoopbackConfig"),
        ("Unisphere-Data-SONET-MIB", "usdSonetMediumTimingSource"))
)
if mibBuilder.loadTexts:
    usdSonetGroup2.setStatus("current")

usdSonetVirtualTributaryGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 5)
)
usdSonetVirtualTributaryGroup2.setObjects(
      *(("Unisphere-Data-SONET-MIB", "usdSonetVTNextIfIndex"),
        ("Unisphere-Data-SONET-MIB", "usdSonetVTPathLogicalChannel"),
        ("Unisphere-Data-SONET-MIB", "usdSonetVTPathPayload"),
        ("Unisphere-Data-SONET-MIB", "usdSonetVTTributaryGroup"),
        ("Unisphere-Data-SONET-MIB", "usdSonetVTTributarySubChannel"),
        ("Unisphere-Data-SONET-MIB", "usdSonetVTLowerIfIndex"),
        ("Unisphere-Data-SONET-MIB", "usdSonetVTRowStatus"))
)
if mibBuilder.loadTexts:
    usdSonetVirtualTributaryGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdSonetCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdSonetCompliance.setStatus(
        "obsolete"
    )

usdSonetCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 1, 2)
)
if mibBuilder.loadTexts:
    usdSonetCompliance2.setStatus(
        "deprecated"
    )

usdSonetCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 1, 3)
)
if mibBuilder.loadTexts:
    usdSonetCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-SONET-MIB",
    **{"UsdSonetLineSpeed": UsdSonetLineSpeed,
       "UsdSonetLogicalPathChannel": UsdSonetLogicalPathChannel,
       "UsdSonetPathHierarchy": UsdSonetPathHierarchy,
       "UsdSonetVTType": UsdSonetVTType,
       "usdSonetMIB": usdSonetMIB,
       "usdSonetObjects": usdSonetObjects,
       "usdSonetMediumTable": usdSonetMediumTable,
       "usdSonetMediumEntry": usdSonetMediumEntry,
       "usdSonetMediumType": usdSonetMediumType,
       "usdSonetMediumLoopbackConfig": usdSonetMediumLoopbackConfig,
       "usdSonetMediumTimingSource": usdSonetMediumTimingSource,
       "usdSonetMediumCircuitIdentifier": usdSonetMediumCircuitIdentifier,
       "usdSonetPathObjects": usdSonetPathObjects,
       "usdSonetPathCapabilityTable": usdSonetPathCapabilityTable,
       "usdSonetPathCapabilityEntry": usdSonetPathCapabilityEntry,
       "usdSonetPathRemoveFlag": usdSonetPathRemoveFlag,
       "usdSonetPathChannelized": usdSonetPathChannelized,
       "usdSonetPathMaximumChannels": usdSonetPathMaximumChannels,
       "usdSonetPathMinimumPathSpeed": usdSonetPathMinimumPathSpeed,
       "usdSonetPathMaximumPathSpeed": usdSonetPathMaximumPathSpeed,
       "usdSonetPathNextIfIndex": usdSonetPathNextIfIndex,
       "usdSonetPathTable": usdSonetPathTable,
       "usdSonetPathEntry": usdSonetPathEntry,
       "usdSonetPathIfIndex": usdSonetPathIfIndex,
       "usdSonetPathLogicalChannel": usdSonetPathLogicalChannel,
       "usdSonetPathSpeed": usdSonetPathSpeed,
       "usdSonetPathHierarchy": usdSonetPathHierarchy,
       "usdSonetPathLowerIfIndex": usdSonetPathLowerIfIndex,
       "usdSonetPathRowStatus": usdSonetPathRowStatus,
       "usdSonetVTObjects": usdSonetVTObjects,
       "usdSonetVTNextIfIndex": usdSonetVTNextIfIndex,
       "usdSonetVTTable": usdSonetVTTable,
       "usdSonetVTEntry": usdSonetVTEntry,
       "usdSonetVTIfIndex": usdSonetVTIfIndex,
       "usdSonetVTPathLogicalChannel": usdSonetVTPathLogicalChannel,
       "usdSonetVTType": usdSonetVTType,
       "usdSonetVTPathPayload": usdSonetVTPathPayload,
       "usdSonetVTTributaryGroup": usdSonetVTTributaryGroup,
       "usdSonetVTTributarySubChannel": usdSonetVTTributarySubChannel,
       "usdSonetVTLowerIfIndex": usdSonetVTLowerIfIndex,
       "usdSonetVTRowStatus": usdSonetVTRowStatus,
       "usdSonetConformance": usdSonetConformance,
       "usdSonetCompliances": usdSonetCompliances,
       "usdSonetCompliance": usdSonetCompliance,
       "usdSonetCompliance2": usdSonetCompliance2,
       "usdSonetCompliance3": usdSonetCompliance3,
       "usdSonetGroups": usdSonetGroups,
       "usdSonetGroup": usdSonetGroup,
       "usdSonetPathGroup": usdSonetPathGroup,
       "usdSonetVirtualTributaryGroup": usdSonetVirtualTributaryGroup,
       "usdSonetGroup2": usdSonetGroup2,
       "usdSonetVirtualTributaryGroup2": usdSonetVirtualTributaryGroup2}
)
