# SNMP MIB module (DOT12-RPTR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOT12-RPTR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:12 2024
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
 mib_2) = mibBuilder.importSymbols(
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
    "mib-2")

(DisplayString,
 MacAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

vgRptrMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 53)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VgRptrObjects_ObjectIdentity = ObjectIdentity
vgRptrObjects = _VgRptrObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 53, 1)
)
_VgRptrBasic_ObjectIdentity = ObjectIdentity
vgRptrBasic = _VgRptrBasic_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 53, 1, 1)
)
_VgRptrBasicRptr_ObjectIdentity = ObjectIdentity
vgRptrBasicRptr = _VgRptrBasicRptr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 1)
)
_VgRptrInfoTable_Object = MibTable
vgRptrInfoTable = _VgRptrInfoTable_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    vgRptrInfoTable.setStatus("current")
_VgRptrInfoEntry_Object = MibTableRow
vgRptrInfoEntry = _VgRptrInfoEntry_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 1, 1, 1)
)
vgRptrInfoEntry.setIndexNames(
    (0, "DOT12-RPTR-MIB", "vgRptrInfoIndex"),
)
if mibBuilder.loadTexts:
    vgRptrInfoEntry.setStatus("current")


class _VgRptrInfoIndex_Type(Integer32):
    """Custom type vgRptrInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VgRptrInfoIndex_Type.__name__ = "Integer32"
_VgRptrInfoIndex_Object = MibTableColumn
vgRptrInfoIndex = _VgRptrInfoIndex_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 1, 1, 1, 1),
    _VgRptrInfoIndex_Type()
)
vgRptrInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vgRptrInfoIndex.setStatus("current")
_VgRptrInfoMACAddress_Type = MacAddress
_VgRptrInfoMACAddress_Object = MibTableColumn
vgRptrInfoMACAddress = _VgRptrInfoMACAddress_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 1, 1, 1, 2),
    _VgRptrInfoMACAddress_Type()
)
vgRptrInfoMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrInfoMACAddress.setStatus("current")


class _VgRptrInfoCurrentFramingType_Type(Integer32):
    """Custom type vgRptrInfoCurrentFramingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frameType88023", 1),
          ("frameType88025", 2))
    )


_VgRptrInfoCurrentFramingType_Type.__name__ = "Integer32"
_VgRptrInfoCurrentFramingType_Object = MibTableColumn
vgRptrInfoCurrentFramingType = _VgRptrInfoCurrentFramingType_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 1, 1, 1, 3),
    _VgRptrInfoCurrentFramingType_Type()
)
vgRptrInfoCurrentFramingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrInfoCurrentFramingType.setStatus("current")


class _VgRptrInfoDesiredFramingType_Type(Integer32):
    """Custom type vgRptrInfoDesiredFramingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frameType88023", 1),
          ("frameType88025", 2))
    )


_VgRptrInfoDesiredFramingType_Type.__name__ = "Integer32"
_VgRptrInfoDesiredFramingType_Object = MibTableColumn
vgRptrInfoDesiredFramingType = _VgRptrInfoDesiredFramingType_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 1, 1, 1, 4),
    _VgRptrInfoDesiredFramingType_Type()
)
vgRptrInfoDesiredFramingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vgRptrInfoDesiredFramingType.setStatus("current")


class _VgRptrInfoFramingCapability_Type(Integer32):
    """Custom type vgRptrInfoFramingCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("frameType88023", 1),
          ("frameType88025", 2),
          ("frameTypeEither", 3))
    )


_VgRptrInfoFramingCapability_Type.__name__ = "Integer32"
_VgRptrInfoFramingCapability_Object = MibTableColumn
vgRptrInfoFramingCapability = _VgRptrInfoFramingCapability_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 1, 1, 1, 5),
    _VgRptrInfoFramingCapability_Type()
)
vgRptrInfoFramingCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrInfoFramingCapability.setStatus("current")


class _VgRptrInfoTrainingVersion_Type(Integer32):
    """Custom type vgRptrInfoTrainingVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VgRptrInfoTrainingVersion_Type.__name__ = "Integer32"
_VgRptrInfoTrainingVersion_Object = MibTableColumn
vgRptrInfoTrainingVersion = _VgRptrInfoTrainingVersion_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 1, 1, 1, 6),
    _VgRptrInfoTrainingVersion_Type()
)
vgRptrInfoTrainingVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrInfoTrainingVersion.setStatus("current")


class _VgRptrInfoOperStatus_Type(Integer32):
    """Custom type vgRptrInfoOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("generalFailure", 3),
          ("ok", 2),
          ("other", 1))
    )


_VgRptrInfoOperStatus_Type.__name__ = "Integer32"
_VgRptrInfoOperStatus_Object = MibTableColumn
vgRptrInfoOperStatus = _VgRptrInfoOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 1, 1, 1, 7),
    _VgRptrInfoOperStatus_Type()
)
vgRptrInfoOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrInfoOperStatus.setStatus("current")


class _VgRptrInfoReset_Type(Integer32):
    """Custom type vgRptrInfoReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_VgRptrInfoReset_Type.__name__ = "Integer32"
_VgRptrInfoReset_Object = MibTableColumn
vgRptrInfoReset = _VgRptrInfoReset_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 1, 1, 1, 8),
    _VgRptrInfoReset_Type()
)
vgRptrInfoReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vgRptrInfoReset.setStatus("current")
_VgRptrInfoLastChange_Type = TimeStamp
_VgRptrInfoLastChange_Object = MibTableColumn
vgRptrInfoLastChange = _VgRptrInfoLastChange_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 1, 1, 1, 9),
    _VgRptrInfoLastChange_Type()
)
vgRptrInfoLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrInfoLastChange.setStatus("current")
_VgRptrBasicGroup_ObjectIdentity = ObjectIdentity
vgRptrBasicGroup = _VgRptrBasicGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 2)
)
_VgRptrBasicGroupTable_Object = MibTable
vgRptrBasicGroupTable = _VgRptrBasicGroupTable_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    vgRptrBasicGroupTable.setStatus("current")
_VgRptrBasicGroupEntry_Object = MibTableRow
vgRptrBasicGroupEntry = _VgRptrBasicGroupEntry_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 2, 1, 1)
)
vgRptrBasicGroupEntry.setIndexNames(
    (0, "DOT12-RPTR-MIB", "vgRptrGroupIndex"),
)
if mibBuilder.loadTexts:
    vgRptrBasicGroupEntry.setStatus("current")


class _VgRptrGroupIndex_Type(Integer32):
    """Custom type vgRptrGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2146483647),
    )


_VgRptrGroupIndex_Type.__name__ = "Integer32"
_VgRptrGroupIndex_Object = MibTableColumn
vgRptrGroupIndex = _VgRptrGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 2, 1, 1, 1),
    _VgRptrGroupIndex_Type()
)
vgRptrGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vgRptrGroupIndex.setStatus("current")
_VgRptrGroupObjectID_Type = ObjectIdentifier
_VgRptrGroupObjectID_Object = MibTableColumn
vgRptrGroupObjectID = _VgRptrGroupObjectID_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 2, 1, 1, 2),
    _VgRptrGroupObjectID_Type()
)
vgRptrGroupObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrGroupObjectID.setStatus("current")


class _VgRptrGroupOperStatus_Type(Integer32):
    """Custom type vgRptrGroupOperStatus based on Integer32"""
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
        *(("malfunctioning", 3),
          ("notPresent", 4),
          ("operational", 2),
          ("other", 1),
          ("resetInProgress", 6),
          ("underTest", 5))
    )


_VgRptrGroupOperStatus_Type.__name__ = "Integer32"
_VgRptrGroupOperStatus_Object = MibTableColumn
vgRptrGroupOperStatus = _VgRptrGroupOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 2, 1, 1, 3),
    _VgRptrGroupOperStatus_Type()
)
vgRptrGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrGroupOperStatus.setStatus("current")


class _VgRptrGroupPortCapacity_Type(Integer32):
    """Custom type vgRptrGroupPortCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2146483647),
    )


_VgRptrGroupPortCapacity_Type.__name__ = "Integer32"
_VgRptrGroupPortCapacity_Object = MibTableColumn
vgRptrGroupPortCapacity = _VgRptrGroupPortCapacity_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 2, 1, 1, 4),
    _VgRptrGroupPortCapacity_Type()
)
vgRptrGroupPortCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrGroupPortCapacity.setStatus("current")


class _VgRptrGroupCablesBundled_Type(Integer32):
    """Custom type vgRptrGroupCablesBundled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noCablesBundled", 2),
          ("someCablesBundled", 1))
    )


_VgRptrGroupCablesBundled_Type.__name__ = "Integer32"
_VgRptrGroupCablesBundled_Object = MibTableColumn
vgRptrGroupCablesBundled = _VgRptrGroupCablesBundled_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 2, 1, 1, 5),
    _VgRptrGroupCablesBundled_Type()
)
vgRptrGroupCablesBundled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vgRptrGroupCablesBundled.setStatus("current")
_VgRptrBasicPort_ObjectIdentity = ObjectIdentity
vgRptrBasicPort = _VgRptrBasicPort_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 3)
)
_VgRptrBasicPortTable_Object = MibTable
vgRptrBasicPortTable = _VgRptrBasicPortTable_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    vgRptrBasicPortTable.setStatus("current")
_VgRptrBasicPortEntry_Object = MibTableRow
vgRptrBasicPortEntry = _VgRptrBasicPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 3, 1, 1)
)
vgRptrBasicPortEntry.setIndexNames(
    (0, "DOT12-RPTR-MIB", "vgRptrGroupIndex"),
    (0, "DOT12-RPTR-MIB", "vgRptrPortIndex"),
)
if mibBuilder.loadTexts:
    vgRptrBasicPortEntry.setStatus("current")


class _VgRptrPortIndex_Type(Integer32):
    """Custom type vgRptrPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VgRptrPortIndex_Type.__name__ = "Integer32"
_VgRptrPortIndex_Object = MibTableColumn
vgRptrPortIndex = _VgRptrPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 3, 1, 1, 1),
    _VgRptrPortIndex_Type()
)
vgRptrPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vgRptrPortIndex.setStatus("current")


class _VgRptrPortType_Type(Integer32):
    """Custom type vgRptrPortType based on Integer32"""
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
        *(("cascadeExternal", 1),
          ("cascadeInternal", 2),
          ("localExternal", 3),
          ("localInternal", 4))
    )


_VgRptrPortType_Type.__name__ = "Integer32"
_VgRptrPortType_Object = MibTableColumn
vgRptrPortType = _VgRptrPortType_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 3, 1, 1, 2),
    _VgRptrPortType_Type()
)
vgRptrPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortType.setStatus("current")


class _VgRptrPortAdminStatus_Type(Integer32):
    """Custom type vgRptrPortAdminStatus based on Integer32"""
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


_VgRptrPortAdminStatus_Type.__name__ = "Integer32"
_VgRptrPortAdminStatus_Object = MibTableColumn
vgRptrPortAdminStatus = _VgRptrPortAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 3, 1, 1, 3),
    _VgRptrPortAdminStatus_Type()
)
vgRptrPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vgRptrPortAdminStatus.setStatus("current")


class _VgRptrPortOperStatus_Type(Integer32):
    """Custom type vgRptrPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("training", 3))
    )


_VgRptrPortOperStatus_Type.__name__ = "Integer32"
_VgRptrPortOperStatus_Object = MibTableColumn
vgRptrPortOperStatus = _VgRptrPortOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 3, 1, 1, 4),
    _VgRptrPortOperStatus_Type()
)
vgRptrPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortOperStatus.setStatus("current")


class _VgRptrPortSupportedPromiscMode_Type(Integer32):
    """Custom type vgRptrPortSupportedPromiscMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("promiscModeOnly", 3),
          ("singleModeOnly", 1),
          ("singleOrPromiscMode", 2))
    )


_VgRptrPortSupportedPromiscMode_Type.__name__ = "Integer32"
_VgRptrPortSupportedPromiscMode_Object = MibTableColumn
vgRptrPortSupportedPromiscMode = _VgRptrPortSupportedPromiscMode_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 3, 1, 1, 5),
    _VgRptrPortSupportedPromiscMode_Type()
)
vgRptrPortSupportedPromiscMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortSupportedPromiscMode.setStatus("current")


class _VgRptrPortSupportedCascadeMode_Type(Integer32):
    """Custom type vgRptrPortSupportedCascadeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cascadePort", 3),
          ("endNodesOnly", 1),
          ("endNodesOrRepeaters", 2))
    )


_VgRptrPortSupportedCascadeMode_Type.__name__ = "Integer32"
_VgRptrPortSupportedCascadeMode_Object = MibTableColumn
vgRptrPortSupportedCascadeMode = _VgRptrPortSupportedCascadeMode_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 3, 1, 1, 6),
    _VgRptrPortSupportedCascadeMode_Type()
)
vgRptrPortSupportedCascadeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortSupportedCascadeMode.setStatus("current")


class _VgRptrPortAllowedTrainType_Type(Integer32):
    """Custom type vgRptrPortAllowedTrainType based on Integer32"""
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
        *(("allowAnything", 4),
          ("allowEndNodesOnly", 1),
          ("allowEndNodesOrRepeaters", 3),
          ("allowPromiscuousEndNodes", 2))
    )


_VgRptrPortAllowedTrainType_Type.__name__ = "Integer32"
_VgRptrPortAllowedTrainType_Object = MibTableColumn
vgRptrPortAllowedTrainType = _VgRptrPortAllowedTrainType_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 3, 1, 1, 7),
    _VgRptrPortAllowedTrainType_Type()
)
vgRptrPortAllowedTrainType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vgRptrPortAllowedTrainType.setStatus("current")


class _VgRptrPortLastTrainConfig_Type(OctetString):
    """Custom type vgRptrPortLastTrainConfig based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_VgRptrPortLastTrainConfig_Type.__name__ = "OctetString"
_VgRptrPortLastTrainConfig_Object = MibTableColumn
vgRptrPortLastTrainConfig = _VgRptrPortLastTrainConfig_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 3, 1, 1, 8),
    _VgRptrPortLastTrainConfig_Type()
)
vgRptrPortLastTrainConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortLastTrainConfig.setStatus("current")


class _VgRptrPortTrainingResult_Type(OctetString):
    """Custom type vgRptrPortTrainingResult based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_VgRptrPortTrainingResult_Type.__name__ = "OctetString"
_VgRptrPortTrainingResult_Object = MibTableColumn
vgRptrPortTrainingResult = _VgRptrPortTrainingResult_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 3, 1, 1, 9),
    _VgRptrPortTrainingResult_Type()
)
vgRptrPortTrainingResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortTrainingResult.setStatus("current")
_VgRptrPortPriorityEnable_Type = TruthValue
_VgRptrPortPriorityEnable_Object = MibTableColumn
vgRptrPortPriorityEnable = _VgRptrPortPriorityEnable_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 3, 1, 1, 10),
    _VgRptrPortPriorityEnable_Type()
)
vgRptrPortPriorityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vgRptrPortPriorityEnable.setStatus("current")


class _VgRptrPortRptrInfoIndex_Type(Integer32):
    """Custom type vgRptrPortRptrInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VgRptrPortRptrInfoIndex_Type.__name__ = "Integer32"
_VgRptrPortRptrInfoIndex_Object = MibTableColumn
vgRptrPortRptrInfoIndex = _VgRptrPortRptrInfoIndex_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 1, 3, 1, 1, 11),
    _VgRptrPortRptrInfoIndex_Type()
)
vgRptrPortRptrInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortRptrInfoIndex.setStatus("current")
_VgRptrMonitor_ObjectIdentity = ObjectIdentity
vgRptrMonitor = _VgRptrMonitor_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 53, 1, 2)
)
_VgRptrMonRepeater_ObjectIdentity = ObjectIdentity
vgRptrMonRepeater = _VgRptrMonRepeater_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 1)
)
_VgRptrMonitorTable_Object = MibTable
vgRptrMonitorTable = _VgRptrMonitorTable_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    vgRptrMonitorTable.setStatus("current")
_VgRptrMonitorEntry_Object = MibTableRow
vgRptrMonitorEntry = _VgRptrMonitorEntry_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 1, 1, 1)
)
vgRptrMonitorEntry.setIndexNames(
    (0, "DOT12-RPTR-MIB", "vgRptrInfoIndex"),
)
if mibBuilder.loadTexts:
    vgRptrMonitorEntry.setStatus("current")
_VgRptrMonTotalReadableFrames_Type = Counter32
_VgRptrMonTotalReadableFrames_Object = MibTableColumn
vgRptrMonTotalReadableFrames = _VgRptrMonTotalReadableFrames_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 1, 1, 1, 1),
    _VgRptrMonTotalReadableFrames_Type()
)
vgRptrMonTotalReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrMonTotalReadableFrames.setStatus("current")
_VgRptrMonTotalReadableOctets_Type = Counter32
_VgRptrMonTotalReadableOctets_Object = MibTableColumn
vgRptrMonTotalReadableOctets = _VgRptrMonTotalReadableOctets_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 1, 1, 1, 2),
    _VgRptrMonTotalReadableOctets_Type()
)
vgRptrMonTotalReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrMonTotalReadableOctets.setStatus("current")
_VgRptrMonReadableOctetRollovers_Type = Counter32
_VgRptrMonReadableOctetRollovers_Object = MibTableColumn
vgRptrMonReadableOctetRollovers = _VgRptrMonReadableOctetRollovers_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 1, 1, 1, 3),
    _VgRptrMonReadableOctetRollovers_Type()
)
vgRptrMonReadableOctetRollovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrMonReadableOctetRollovers.setStatus("current")
_VgRptrMonHCTotalReadableOctets_Type = Counter64
_VgRptrMonHCTotalReadableOctets_Object = MibTableColumn
vgRptrMonHCTotalReadableOctets = _VgRptrMonHCTotalReadableOctets_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 1, 1, 1, 4),
    _VgRptrMonHCTotalReadableOctets_Type()
)
vgRptrMonHCTotalReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrMonHCTotalReadableOctets.setStatus("current")
_VgRptrMonTotalErrors_Type = Counter32
_VgRptrMonTotalErrors_Object = MibTableColumn
vgRptrMonTotalErrors = _VgRptrMonTotalErrors_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 1, 1, 1, 5),
    _VgRptrMonTotalErrors_Type()
)
vgRptrMonTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrMonTotalErrors.setStatus("current")
_VgRptrMonGroup_ObjectIdentity = ObjectIdentity
vgRptrMonGroup = _VgRptrMonGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 2)
)
_VgRptrMonPort_ObjectIdentity = ObjectIdentity
vgRptrMonPort = _VgRptrMonPort_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 3)
)
_VgRptrMonPortTable_Object = MibTable
vgRptrMonPortTable = _VgRptrMonPortTable_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    vgRptrMonPortTable.setStatus("current")
_VgRptrMonPortEntry_Object = MibTableRow
vgRptrMonPortEntry = _VgRptrMonPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 3, 1, 1)
)
vgRptrMonPortEntry.setIndexNames(
    (0, "DOT12-RPTR-MIB", "vgRptrGroupIndex"),
    (0, "DOT12-RPTR-MIB", "vgRptrPortIndex"),
)
if mibBuilder.loadTexts:
    vgRptrMonPortEntry.setStatus("current")
_VgRptrPortReadableFrames_Type = Counter32
_VgRptrPortReadableFrames_Object = MibTableColumn
vgRptrPortReadableFrames = _VgRptrPortReadableFrames_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 3, 1, 1, 1),
    _VgRptrPortReadableFrames_Type()
)
vgRptrPortReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortReadableFrames.setStatus("current")
_VgRptrPortReadableOctets_Type = Counter32
_VgRptrPortReadableOctets_Object = MibTableColumn
vgRptrPortReadableOctets = _VgRptrPortReadableOctets_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 3, 1, 1, 2),
    _VgRptrPortReadableOctets_Type()
)
vgRptrPortReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortReadableOctets.setStatus("current")
_VgRptrPortReadOctetRollovers_Type = Counter32
_VgRptrPortReadOctetRollovers_Object = MibTableColumn
vgRptrPortReadOctetRollovers = _VgRptrPortReadOctetRollovers_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 3, 1, 1, 3),
    _VgRptrPortReadOctetRollovers_Type()
)
vgRptrPortReadOctetRollovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortReadOctetRollovers.setStatus("current")
_VgRptrPortHCReadableOctets_Type = Counter64
_VgRptrPortHCReadableOctets_Object = MibTableColumn
vgRptrPortHCReadableOctets = _VgRptrPortHCReadableOctets_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 3, 1, 1, 4),
    _VgRptrPortHCReadableOctets_Type()
)
vgRptrPortHCReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortHCReadableOctets.setStatus("current")
_VgRptrPortUnreadableOctets_Type = Counter32
_VgRptrPortUnreadableOctets_Object = MibTableColumn
vgRptrPortUnreadableOctets = _VgRptrPortUnreadableOctets_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 3, 1, 1, 5),
    _VgRptrPortUnreadableOctets_Type()
)
vgRptrPortUnreadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortUnreadableOctets.setStatus("current")
_VgRptrPortUnreadOctetRollovers_Type = Counter32
_VgRptrPortUnreadOctetRollovers_Object = MibTableColumn
vgRptrPortUnreadOctetRollovers = _VgRptrPortUnreadOctetRollovers_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 3, 1, 1, 6),
    _VgRptrPortUnreadOctetRollovers_Type()
)
vgRptrPortUnreadOctetRollovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortUnreadOctetRollovers.setStatus("current")
_VgRptrPortHCUnreadableOctets_Type = Counter64
_VgRptrPortHCUnreadableOctets_Object = MibTableColumn
vgRptrPortHCUnreadableOctets = _VgRptrPortHCUnreadableOctets_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 3, 1, 1, 7),
    _VgRptrPortHCUnreadableOctets_Type()
)
vgRptrPortHCUnreadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortHCUnreadableOctets.setStatus("current")
_VgRptrPortHighPriorityFrames_Type = Counter32
_VgRptrPortHighPriorityFrames_Object = MibTableColumn
vgRptrPortHighPriorityFrames = _VgRptrPortHighPriorityFrames_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 3, 1, 1, 8),
    _VgRptrPortHighPriorityFrames_Type()
)
vgRptrPortHighPriorityFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortHighPriorityFrames.setStatus("current")
_VgRptrPortHighPriorityOctets_Type = Counter32
_VgRptrPortHighPriorityOctets_Object = MibTableColumn
vgRptrPortHighPriorityOctets = _VgRptrPortHighPriorityOctets_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 3, 1, 1, 9),
    _VgRptrPortHighPriorityOctets_Type()
)
vgRptrPortHighPriorityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortHighPriorityOctets.setStatus("current")
_VgRptrPortHighPriOctetRollovers_Type = Counter32
_VgRptrPortHighPriOctetRollovers_Object = MibTableColumn
vgRptrPortHighPriOctetRollovers = _VgRptrPortHighPriOctetRollovers_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 3, 1, 1, 10),
    _VgRptrPortHighPriOctetRollovers_Type()
)
vgRptrPortHighPriOctetRollovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortHighPriOctetRollovers.setStatus("current")
_VgRptrPortHCHighPriorityOctets_Type = Counter64
_VgRptrPortHCHighPriorityOctets_Object = MibTableColumn
vgRptrPortHCHighPriorityOctets = _VgRptrPortHCHighPriorityOctets_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 3, 1, 1, 11),
    _VgRptrPortHCHighPriorityOctets_Type()
)
vgRptrPortHCHighPriorityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortHCHighPriorityOctets.setStatus("current")
_VgRptrPortNormPriorityFrames_Type = Counter32
_VgRptrPortNormPriorityFrames_Object = MibTableColumn
vgRptrPortNormPriorityFrames = _VgRptrPortNormPriorityFrames_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 3, 1, 1, 12),
    _VgRptrPortNormPriorityFrames_Type()
)
vgRptrPortNormPriorityFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortNormPriorityFrames.setStatus("current")
_VgRptrPortNormPriorityOctets_Type = Counter32
_VgRptrPortNormPriorityOctets_Object = MibTableColumn
vgRptrPortNormPriorityOctets = _VgRptrPortNormPriorityOctets_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 3, 1, 1, 13),
    _VgRptrPortNormPriorityOctets_Type()
)
vgRptrPortNormPriorityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortNormPriorityOctets.setStatus("current")
_VgRptrPortNormPriOctetRollovers_Type = Counter32
_VgRptrPortNormPriOctetRollovers_Object = MibTableColumn
vgRptrPortNormPriOctetRollovers = _VgRptrPortNormPriOctetRollovers_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 3, 1, 1, 14),
    _VgRptrPortNormPriOctetRollovers_Type()
)
vgRptrPortNormPriOctetRollovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortNormPriOctetRollovers.setStatus("current")
_VgRptrPortHCNormPriorityOctets_Type = Counter64
_VgRptrPortHCNormPriorityOctets_Object = MibTableColumn
vgRptrPortHCNormPriorityOctets = _VgRptrPortHCNormPriorityOctets_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 3, 1, 1, 15),
    _VgRptrPortHCNormPriorityOctets_Type()
)
vgRptrPortHCNormPriorityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortHCNormPriorityOctets.setStatus("current")
_VgRptrPortBroadcastFrames_Type = Counter32
_VgRptrPortBroadcastFrames_Object = MibTableColumn
vgRptrPortBroadcastFrames = _VgRptrPortBroadcastFrames_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 3, 1, 1, 16),
    _VgRptrPortBroadcastFrames_Type()
)
vgRptrPortBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortBroadcastFrames.setStatus("current")
_VgRptrPortMulticastFrames_Type = Counter32
_VgRptrPortMulticastFrames_Object = MibTableColumn
vgRptrPortMulticastFrames = _VgRptrPortMulticastFrames_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 3, 1, 1, 17),
    _VgRptrPortMulticastFrames_Type()
)
vgRptrPortMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortMulticastFrames.setStatus("current")
_VgRptrPortNullAddressedFrames_Type = Counter32
_VgRptrPortNullAddressedFrames_Object = MibTableColumn
vgRptrPortNullAddressedFrames = _VgRptrPortNullAddressedFrames_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 3, 1, 1, 18),
    _VgRptrPortNullAddressedFrames_Type()
)
vgRptrPortNullAddressedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortNullAddressedFrames.setStatus("current")
_VgRptrPortIPMFrames_Type = Counter32
_VgRptrPortIPMFrames_Object = MibTableColumn
vgRptrPortIPMFrames = _VgRptrPortIPMFrames_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 3, 1, 1, 19),
    _VgRptrPortIPMFrames_Type()
)
vgRptrPortIPMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortIPMFrames.setStatus("current")
_VgRptrPortOversizeFrames_Type = Counter32
_VgRptrPortOversizeFrames_Object = MibTableColumn
vgRptrPortOversizeFrames = _VgRptrPortOversizeFrames_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 3, 1, 1, 20),
    _VgRptrPortOversizeFrames_Type()
)
vgRptrPortOversizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortOversizeFrames.setStatus("current")
_VgRptrPortDataErrorFrames_Type = Counter32
_VgRptrPortDataErrorFrames_Object = MibTableColumn
vgRptrPortDataErrorFrames = _VgRptrPortDataErrorFrames_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 3, 1, 1, 21),
    _VgRptrPortDataErrorFrames_Type()
)
vgRptrPortDataErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortDataErrorFrames.setStatus("current")
_VgRptrPortPriorityPromotions_Type = Counter32
_VgRptrPortPriorityPromotions_Object = MibTableColumn
vgRptrPortPriorityPromotions = _VgRptrPortPriorityPromotions_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 3, 1, 1, 22),
    _VgRptrPortPriorityPromotions_Type()
)
vgRptrPortPriorityPromotions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortPriorityPromotions.setStatus("current")
_VgRptrPortTransitionToTrainings_Type = Counter32
_VgRptrPortTransitionToTrainings_Object = MibTableColumn
vgRptrPortTransitionToTrainings = _VgRptrPortTransitionToTrainings_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 3, 1, 1, 23),
    _VgRptrPortTransitionToTrainings_Type()
)
vgRptrPortTransitionToTrainings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortTransitionToTrainings.setStatus("current")
_VgRptrPortLastChange_Type = TimeStamp
_VgRptrPortLastChange_Object = MibTableColumn
vgRptrPortLastChange = _VgRptrPortLastChange_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 2, 3, 1, 1, 24),
    _VgRptrPortLastChange_Type()
)
vgRptrPortLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrPortLastChange.setStatus("current")
_VgRptrAddrTrack_ObjectIdentity = ObjectIdentity
vgRptrAddrTrack = _VgRptrAddrTrack_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 53, 1, 3)
)
_VgRptrAddrTrackRptr_ObjectIdentity = ObjectIdentity
vgRptrAddrTrackRptr = _VgRptrAddrTrackRptr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 53, 1, 3, 1)
)
_VgRptrAddrTrackGroup_ObjectIdentity = ObjectIdentity
vgRptrAddrTrackGroup = _VgRptrAddrTrackGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 53, 1, 3, 2)
)
_VgRptrAddrTrackPort_ObjectIdentity = ObjectIdentity
vgRptrAddrTrackPort = _VgRptrAddrTrackPort_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 53, 1, 3, 3)
)
_VgRptrAddrTrackTable_Object = MibTable
vgRptrAddrTrackTable = _VgRptrAddrTrackTable_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    vgRptrAddrTrackTable.setStatus("current")
_VgRptrAddrTrackEntry_Object = MibTableRow
vgRptrAddrTrackEntry = _VgRptrAddrTrackEntry_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 3, 3, 1, 1)
)
vgRptrAddrTrackEntry.setIndexNames(
    (0, "DOT12-RPTR-MIB", "vgRptrGroupIndex"),
    (0, "DOT12-RPTR-MIB", "vgRptrPortIndex"),
)
if mibBuilder.loadTexts:
    vgRptrAddrTrackEntry.setStatus("current")


class _VgRptrAddrLastTrainedAddress_Type(OctetString):
    """Custom type vgRptrAddrLastTrainedAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(6, 6),
    )


_VgRptrAddrLastTrainedAddress_Type.__name__ = "OctetString"
_VgRptrAddrLastTrainedAddress_Object = MibTableColumn
vgRptrAddrLastTrainedAddress = _VgRptrAddrLastTrainedAddress_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 3, 3, 1, 1, 1),
    _VgRptrAddrLastTrainedAddress_Type()
)
vgRptrAddrLastTrainedAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrAddrLastTrainedAddress.setStatus("current")
_VgRptrAddrTrainedAddrChanges_Type = Counter32
_VgRptrAddrTrainedAddrChanges_Object = MibTableColumn
vgRptrAddrTrainedAddrChanges = _VgRptrAddrTrainedAddrChanges_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 3, 3, 1, 1, 2),
    _VgRptrAddrTrainedAddrChanges_Type()
)
vgRptrAddrTrainedAddrChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrAddrTrainedAddrChanges.setStatus("current")
_VgRptrRptrDetectedDupAddress_Type = TruthValue
_VgRptrRptrDetectedDupAddress_Object = MibTableColumn
vgRptrRptrDetectedDupAddress = _VgRptrRptrDetectedDupAddress_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 3, 3, 1, 1, 3),
    _VgRptrRptrDetectedDupAddress_Type()
)
vgRptrRptrDetectedDupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgRptrRptrDetectedDupAddress.setStatus("current")
_VgRptrMgrDetectedDupAddress_Type = TruthValue
_VgRptrMgrDetectedDupAddress_Object = MibTableColumn
vgRptrMgrDetectedDupAddress = _VgRptrMgrDetectedDupAddress_Object(
    (1, 3, 6, 1, 2, 1, 53, 1, 3, 3, 1, 1, 4),
    _VgRptrMgrDetectedDupAddress_Type()
)
vgRptrMgrDetectedDupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vgRptrMgrDetectedDupAddress.setStatus("current")
_VgRptrTraps_ObjectIdentity = ObjectIdentity
vgRptrTraps = _VgRptrTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 53, 2)
)
_VgRptrTrapPrefix_ObjectIdentity = ObjectIdentity
vgRptrTrapPrefix = _VgRptrTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 53, 2, 0)
)
_VgRptrConformance_ObjectIdentity = ObjectIdentity
vgRptrConformance = _VgRptrConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 53, 3)
)
_VgRptrCompliances_ObjectIdentity = ObjectIdentity
vgRptrCompliances = _VgRptrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 53, 3, 1)
)
_VgRptrGroups_ObjectIdentity = ObjectIdentity
vgRptrGroups = _VgRptrGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 53, 3, 2)
)

# Managed Objects groups

vgRptrConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 53, 3, 2, 1)
)
vgRptrConfigGroup.setObjects(
      *(("DOT12-RPTR-MIB", "vgRptrInfoMACAddress"),
        ("DOT12-RPTR-MIB", "vgRptrInfoCurrentFramingType"),
        ("DOT12-RPTR-MIB", "vgRptrInfoDesiredFramingType"),
        ("DOT12-RPTR-MIB", "vgRptrInfoFramingCapability"),
        ("DOT12-RPTR-MIB", "vgRptrInfoTrainingVersion"),
        ("DOT12-RPTR-MIB", "vgRptrInfoOperStatus"),
        ("DOT12-RPTR-MIB", "vgRptrInfoReset"),
        ("DOT12-RPTR-MIB", "vgRptrInfoLastChange"),
        ("DOT12-RPTR-MIB", "vgRptrGroupObjectID"),
        ("DOT12-RPTR-MIB", "vgRptrGroupOperStatus"),
        ("DOT12-RPTR-MIB", "vgRptrGroupPortCapacity"),
        ("DOT12-RPTR-MIB", "vgRptrGroupCablesBundled"),
        ("DOT12-RPTR-MIB", "vgRptrPortType"),
        ("DOT12-RPTR-MIB", "vgRptrPortAdminStatus"),
        ("DOT12-RPTR-MIB", "vgRptrPortOperStatus"),
        ("DOT12-RPTR-MIB", "vgRptrPortSupportedPromiscMode"),
        ("DOT12-RPTR-MIB", "vgRptrPortSupportedCascadeMode"),
        ("DOT12-RPTR-MIB", "vgRptrPortAllowedTrainType"),
        ("DOT12-RPTR-MIB", "vgRptrPortLastTrainConfig"),
        ("DOT12-RPTR-MIB", "vgRptrPortTrainingResult"),
        ("DOT12-RPTR-MIB", "vgRptrPortPriorityEnable"),
        ("DOT12-RPTR-MIB", "vgRptrPortRptrInfoIndex"))
)
if mibBuilder.loadTexts:
    vgRptrConfigGroup.setStatus("current")

vgRptrStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 53, 3, 2, 2)
)
vgRptrStatsGroup.setObjects(
      *(("DOT12-RPTR-MIB", "vgRptrMonTotalReadableFrames"),
        ("DOT12-RPTR-MIB", "vgRptrMonTotalReadableOctets"),
        ("DOT12-RPTR-MIB", "vgRptrMonReadableOctetRollovers"),
        ("DOT12-RPTR-MIB", "vgRptrMonTotalErrors"),
        ("DOT12-RPTR-MIB", "vgRptrPortReadableFrames"),
        ("DOT12-RPTR-MIB", "vgRptrPortReadableOctets"),
        ("DOT12-RPTR-MIB", "vgRptrPortReadOctetRollovers"),
        ("DOT12-RPTR-MIB", "vgRptrPortUnreadableOctets"),
        ("DOT12-RPTR-MIB", "vgRptrPortUnreadOctetRollovers"),
        ("DOT12-RPTR-MIB", "vgRptrPortHighPriorityFrames"),
        ("DOT12-RPTR-MIB", "vgRptrPortHighPriorityOctets"),
        ("DOT12-RPTR-MIB", "vgRptrPortHighPriOctetRollovers"),
        ("DOT12-RPTR-MIB", "vgRptrPortNormPriorityFrames"),
        ("DOT12-RPTR-MIB", "vgRptrPortNormPriorityOctets"),
        ("DOT12-RPTR-MIB", "vgRptrPortNormPriOctetRollovers"),
        ("DOT12-RPTR-MIB", "vgRptrPortBroadcastFrames"),
        ("DOT12-RPTR-MIB", "vgRptrPortMulticastFrames"),
        ("DOT12-RPTR-MIB", "vgRptrPortNullAddressedFrames"),
        ("DOT12-RPTR-MIB", "vgRptrPortIPMFrames"),
        ("DOT12-RPTR-MIB", "vgRptrPortOversizeFrames"),
        ("DOT12-RPTR-MIB", "vgRptrPortDataErrorFrames"),
        ("DOT12-RPTR-MIB", "vgRptrPortPriorityPromotions"),
        ("DOT12-RPTR-MIB", "vgRptrPortTransitionToTrainings"),
        ("DOT12-RPTR-MIB", "vgRptrPortLastChange"))
)
if mibBuilder.loadTexts:
    vgRptrStatsGroup.setStatus("current")

vgRptrStats64Group = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 53, 3, 2, 3)
)
vgRptrStats64Group.setObjects(
      *(("DOT12-RPTR-MIB", "vgRptrMonHCTotalReadableOctets"),
        ("DOT12-RPTR-MIB", "vgRptrPortHCReadableOctets"),
        ("DOT12-RPTR-MIB", "vgRptrPortHCUnreadableOctets"),
        ("DOT12-RPTR-MIB", "vgRptrPortHCHighPriorityOctets"),
        ("DOT12-RPTR-MIB", "vgRptrPortHCNormPriorityOctets"))
)
if mibBuilder.loadTexts:
    vgRptrStats64Group.setStatus("current")

vgRptrAddrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 53, 3, 2, 4)
)
vgRptrAddrGroup.setObjects(
      *(("DOT12-RPTR-MIB", "vgRptrAddrLastTrainedAddress"),
        ("DOT12-RPTR-MIB", "vgRptrAddrTrainedAddrChanges"),
        ("DOT12-RPTR-MIB", "vgRptrRptrDetectedDupAddress"),
        ("DOT12-RPTR-MIB", "vgRptrMgrDetectedDupAddress"))
)
if mibBuilder.loadTexts:
    vgRptrAddrGroup.setStatus("current")


# Notification objects

vgRptrHealth = NotificationType(
    (1, 3, 6, 1, 2, 1, 53, 2, 0, 1)
)
vgRptrHealth.setObjects(
    ("DOT12-RPTR-MIB", "vgRptrInfoOperStatus")
)
if mibBuilder.loadTexts:
    vgRptrHealth.setStatus(
        "current"
    )

vgRptrResetEvent = NotificationType(
    (1, 3, 6, 1, 2, 1, 53, 2, 0, 2)
)
vgRptrResetEvent.setObjects(
    ("DOT12-RPTR-MIB", "vgRptrInfoOperStatus")
)
if mibBuilder.loadTexts:
    vgRptrResetEvent.setStatus(
        "current"
    )


# Notifications groups

vgRptrNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 53, 3, 2, 5)
)
vgRptrNotificationsGroup.setObjects(
      *(("DOT12-RPTR-MIB", "vgRptrHealth"),
        ("DOT12-RPTR-MIB", "vgRptrResetEvent"))
)
if mibBuilder.loadTexts:
    vgRptrNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vgRptrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 53, 3, 1, 1)
)
if mibBuilder.loadTexts:
    vgRptrCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOT12-RPTR-MIB",
    **{"vgRptrMIB": vgRptrMIB,
       "vgRptrObjects": vgRptrObjects,
       "vgRptrBasic": vgRptrBasic,
       "vgRptrBasicRptr": vgRptrBasicRptr,
       "vgRptrInfoTable": vgRptrInfoTable,
       "vgRptrInfoEntry": vgRptrInfoEntry,
       "vgRptrInfoIndex": vgRptrInfoIndex,
       "vgRptrInfoMACAddress": vgRptrInfoMACAddress,
       "vgRptrInfoCurrentFramingType": vgRptrInfoCurrentFramingType,
       "vgRptrInfoDesiredFramingType": vgRptrInfoDesiredFramingType,
       "vgRptrInfoFramingCapability": vgRptrInfoFramingCapability,
       "vgRptrInfoTrainingVersion": vgRptrInfoTrainingVersion,
       "vgRptrInfoOperStatus": vgRptrInfoOperStatus,
       "vgRptrInfoReset": vgRptrInfoReset,
       "vgRptrInfoLastChange": vgRptrInfoLastChange,
       "vgRptrBasicGroup": vgRptrBasicGroup,
       "vgRptrBasicGroupTable": vgRptrBasicGroupTable,
       "vgRptrBasicGroupEntry": vgRptrBasicGroupEntry,
       "vgRptrGroupIndex": vgRptrGroupIndex,
       "vgRptrGroupObjectID": vgRptrGroupObjectID,
       "vgRptrGroupOperStatus": vgRptrGroupOperStatus,
       "vgRptrGroupPortCapacity": vgRptrGroupPortCapacity,
       "vgRptrGroupCablesBundled": vgRptrGroupCablesBundled,
       "vgRptrBasicPort": vgRptrBasicPort,
       "vgRptrBasicPortTable": vgRptrBasicPortTable,
       "vgRptrBasicPortEntry": vgRptrBasicPortEntry,
       "vgRptrPortIndex": vgRptrPortIndex,
       "vgRptrPortType": vgRptrPortType,
       "vgRptrPortAdminStatus": vgRptrPortAdminStatus,
       "vgRptrPortOperStatus": vgRptrPortOperStatus,
       "vgRptrPortSupportedPromiscMode": vgRptrPortSupportedPromiscMode,
       "vgRptrPortSupportedCascadeMode": vgRptrPortSupportedCascadeMode,
       "vgRptrPortAllowedTrainType": vgRptrPortAllowedTrainType,
       "vgRptrPortLastTrainConfig": vgRptrPortLastTrainConfig,
       "vgRptrPortTrainingResult": vgRptrPortTrainingResult,
       "vgRptrPortPriorityEnable": vgRptrPortPriorityEnable,
       "vgRptrPortRptrInfoIndex": vgRptrPortRptrInfoIndex,
       "vgRptrMonitor": vgRptrMonitor,
       "vgRptrMonRepeater": vgRptrMonRepeater,
       "vgRptrMonitorTable": vgRptrMonitorTable,
       "vgRptrMonitorEntry": vgRptrMonitorEntry,
       "vgRptrMonTotalReadableFrames": vgRptrMonTotalReadableFrames,
       "vgRptrMonTotalReadableOctets": vgRptrMonTotalReadableOctets,
       "vgRptrMonReadableOctetRollovers": vgRptrMonReadableOctetRollovers,
       "vgRptrMonHCTotalReadableOctets": vgRptrMonHCTotalReadableOctets,
       "vgRptrMonTotalErrors": vgRptrMonTotalErrors,
       "vgRptrMonGroup": vgRptrMonGroup,
       "vgRptrMonPort": vgRptrMonPort,
       "vgRptrMonPortTable": vgRptrMonPortTable,
       "vgRptrMonPortEntry": vgRptrMonPortEntry,
       "vgRptrPortReadableFrames": vgRptrPortReadableFrames,
       "vgRptrPortReadableOctets": vgRptrPortReadableOctets,
       "vgRptrPortReadOctetRollovers": vgRptrPortReadOctetRollovers,
       "vgRptrPortHCReadableOctets": vgRptrPortHCReadableOctets,
       "vgRptrPortUnreadableOctets": vgRptrPortUnreadableOctets,
       "vgRptrPortUnreadOctetRollovers": vgRptrPortUnreadOctetRollovers,
       "vgRptrPortHCUnreadableOctets": vgRptrPortHCUnreadableOctets,
       "vgRptrPortHighPriorityFrames": vgRptrPortHighPriorityFrames,
       "vgRptrPortHighPriorityOctets": vgRptrPortHighPriorityOctets,
       "vgRptrPortHighPriOctetRollovers": vgRptrPortHighPriOctetRollovers,
       "vgRptrPortHCHighPriorityOctets": vgRptrPortHCHighPriorityOctets,
       "vgRptrPortNormPriorityFrames": vgRptrPortNormPriorityFrames,
       "vgRptrPortNormPriorityOctets": vgRptrPortNormPriorityOctets,
       "vgRptrPortNormPriOctetRollovers": vgRptrPortNormPriOctetRollovers,
       "vgRptrPortHCNormPriorityOctets": vgRptrPortHCNormPriorityOctets,
       "vgRptrPortBroadcastFrames": vgRptrPortBroadcastFrames,
       "vgRptrPortMulticastFrames": vgRptrPortMulticastFrames,
       "vgRptrPortNullAddressedFrames": vgRptrPortNullAddressedFrames,
       "vgRptrPortIPMFrames": vgRptrPortIPMFrames,
       "vgRptrPortOversizeFrames": vgRptrPortOversizeFrames,
       "vgRptrPortDataErrorFrames": vgRptrPortDataErrorFrames,
       "vgRptrPortPriorityPromotions": vgRptrPortPriorityPromotions,
       "vgRptrPortTransitionToTrainings": vgRptrPortTransitionToTrainings,
       "vgRptrPortLastChange": vgRptrPortLastChange,
       "vgRptrAddrTrack": vgRptrAddrTrack,
       "vgRptrAddrTrackRptr": vgRptrAddrTrackRptr,
       "vgRptrAddrTrackGroup": vgRptrAddrTrackGroup,
       "vgRptrAddrTrackPort": vgRptrAddrTrackPort,
       "vgRptrAddrTrackTable": vgRptrAddrTrackTable,
       "vgRptrAddrTrackEntry": vgRptrAddrTrackEntry,
       "vgRptrAddrLastTrainedAddress": vgRptrAddrLastTrainedAddress,
       "vgRptrAddrTrainedAddrChanges": vgRptrAddrTrainedAddrChanges,
       "vgRptrRptrDetectedDupAddress": vgRptrRptrDetectedDupAddress,
       "vgRptrMgrDetectedDupAddress": vgRptrMgrDetectedDupAddress,
       "vgRptrTraps": vgRptrTraps,
       "vgRptrTrapPrefix": vgRptrTrapPrefix,
       "vgRptrHealth": vgRptrHealth,
       "vgRptrResetEvent": vgRptrResetEvent,
       "vgRptrConformance": vgRptrConformance,
       "vgRptrCompliances": vgRptrCompliances,
       "vgRptrCompliance": vgRptrCompliance,
       "vgRptrGroups": vgRptrGroups,
       "vgRptrConfigGroup": vgRptrConfigGroup,
       "vgRptrStatsGroup": vgRptrStatsGroup,
       "vgRptrStats64Group": vgRptrStats64Group,
       "vgRptrAddrGroup": vgRptrAddrGroup,
       "vgRptrNotificationsGroup": vgRptrNotificationsGroup}
)
