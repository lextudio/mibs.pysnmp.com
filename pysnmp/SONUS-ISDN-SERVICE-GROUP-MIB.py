# SNMP MIB module (SONUS-ISDN-SERVICE-GROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-ISDN-SERVICE-GROUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:01 2024
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

(sonusEventClass,
 sonusEventDescription,
 sonusEventLevel) = mibBuilder.importSymbols(
    "SONUS-COMMON-MIB",
    "sonusEventClass",
    "sonusEventDescription",
    "sonusEventLevel")

(sonusSignallingMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusSignallingMIBs")

(SonusAdminState,
 SonusName,
 SonusNameReference,
 SonusServiceState) = mibBuilder.importSymbols(
    "SONUS-TC",
    "SonusAdminState",
    "SonusName",
    "SonusNameReference",
    "SonusServiceState")


# MODULE-IDENTITY

sonusIsdnServiceGroupMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusIsdnServiceGroupMIBObjects_ObjectIdentity = ObjectIdentity
sonusIsdnServiceGroupMIBObjects = _SonusIsdnServiceGroupMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1)
)
_SonusIsdnsgServiceGroup_ObjectIdentity = ObjectIdentity
sonusIsdnsgServiceGroup = _SonusIsdnsgServiceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1)
)
_SonusIsdnsgServiceGroupNextIndex_Type = Integer32
_SonusIsdnsgServiceGroupNextIndex_Object = MibScalar
sonusIsdnsgServiceGroupNextIndex = _SonusIsdnsgServiceGroupNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 1),
    _SonusIsdnsgServiceGroupNextIndex_Type()
)
sonusIsdnsgServiceGroupNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupNextIndex.setStatus("current")
_SonusIsdnsgServiceGroupTable_Object = MibTable
sonusIsdnsgServiceGroupTable = _SonusIsdnsgServiceGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupTable.setStatus("current")
_SonusIsdnsgServiceGroupEntry_Object = MibTableRow
sonusIsdnsgServiceGroupEntry = _SonusIsdnsgServiceGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1)
)
sonusIsdnsgServiceGroupEntry.setIndexNames(
    (0, "SONUS-ISDN-SERVICE-GROUP-MIB", "sonusIsdnsgServiceGroupListIndex"),
)
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupEntry.setStatus("current")
_SonusIsdnsgServiceGroupListIndex_Type = Integer32
_SonusIsdnsgServiceGroupListIndex_Object = MibTableColumn
sonusIsdnsgServiceGroupListIndex = _SonusIsdnsgServiceGroupListIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 1),
    _SonusIsdnsgServiceGroupListIndex_Type()
)
sonusIsdnsgServiceGroupListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupListIndex.setStatus("current")
_SonusIsdnsgServiceGroupName_Type = SonusName
_SonusIsdnsgServiceGroupName_Object = MibTableColumn
sonusIsdnsgServiceGroupName = _SonusIsdnsgServiceGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 2),
    _SonusIsdnsgServiceGroupName_Type()
)
sonusIsdnsgServiceGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupName.setStatus("current")
_SonusIsdnsgServiceGroupTrunkGroup_Type = SonusNameReference
_SonusIsdnsgServiceGroupTrunkGroup_Object = MibTableColumn
sonusIsdnsgServiceGroupTrunkGroup = _SonusIsdnsgServiceGroupTrunkGroup_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 3),
    _SonusIsdnsgServiceGroupTrunkGroup_Type()
)
sonusIsdnsgServiceGroupTrunkGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupTrunkGroup.setStatus("current")


class _SonusIsdnsgServiceGroupHuntAlgorithm_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupHuntAlgorithm based on Integer32"""
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
        *(("circularbackward", 4),
          ("circularforward", 3),
          ("highhigh", 2),
          ("lowlow", 1))
    )


_SonusIsdnsgServiceGroupHuntAlgorithm_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupHuntAlgorithm_Object = MibTableColumn
sonusIsdnsgServiceGroupHuntAlgorithm = _SonusIsdnsgServiceGroupHuntAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 4),
    _SonusIsdnsgServiceGroupHuntAlgorithm_Type()
)
sonusIsdnsgServiceGroupHuntAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupHuntAlgorithm.setStatus("current")


class _SonusIsdnsgServiceGroupCost_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupCost based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SonusIsdnsgServiceGroupCost_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupCost_Object = MibTableColumn
sonusIsdnsgServiceGroupCost = _SonusIsdnsgServiceGroupCost_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 5),
    _SonusIsdnsgServiceGroupCost_Type()
)
sonusIsdnsgServiceGroupCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupCost.setStatus("current")


class _SonusIsdnsgServiceGroupSwitchSide_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupSwitchSide based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 1),
          ("user", 2))
    )


_SonusIsdnsgServiceGroupSwitchSide_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupSwitchSide_Object = MibTableColumn
sonusIsdnsgServiceGroupSwitchSide = _SonusIsdnsgServiceGroupSwitchSide_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 6),
    _SonusIsdnsgServiceGroupSwitchSide_Type()
)
sonusIsdnsgServiceGroupSwitchSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupSwitchSide.setStatus("current")


class _SonusIsdnsgServiceGroupSwitchType_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupSwitchType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("dms100", 3),
          ("dms250", 2),
          ("euroIsdn", 6),
          ("ins1500", 7),
          ("lucent4ESS", 5),
          ("lucent5ESS", 4),
          ("ni2", 1))
    )


_SonusIsdnsgServiceGroupSwitchType_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupSwitchType_Object = MibTableColumn
sonusIsdnsgServiceGroupSwitchType = _SonusIsdnsgServiceGroupSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 7),
    _SonusIsdnsgServiceGroupSwitchType_Type()
)
sonusIsdnsgServiceGroupSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupSwitchType.setStatus("current")


class _SonusIsdnsgServiceGroupSwitchProfileName_Type(DisplayString):
    """Custom type sonusIsdnsgServiceGroupSwitchProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusIsdnsgServiceGroupSwitchProfileName_Type.__name__ = "DisplayString"
_SonusIsdnsgServiceGroupSwitchProfileName_Object = MibTableColumn
sonusIsdnsgServiceGroupSwitchProfileName = _SonusIsdnsgServiceGroupSwitchProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 8),
    _SonusIsdnsgServiceGroupSwitchProfileName_Type()
)
sonusIsdnsgServiceGroupSwitchProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupSwitchProfileName.setStatus("current")


class _SonusIsdnsgServiceGroupOperation_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupOperation based on Integer32"""
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
        *(("clearStats", 5),
          ("dchannelSwitchover", 6),
          ("inService", 3),
          ("maintenance", 2),
          ("outOfService", 1),
          ("restart", 4))
    )


_SonusIsdnsgServiceGroupOperation_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupOperation_Object = MibTableColumn
sonusIsdnsgServiceGroupOperation = _SonusIsdnsgServiceGroupOperation_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 9),
    _SonusIsdnsgServiceGroupOperation_Type()
)
sonusIsdnsgServiceGroupOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupOperation.setStatus("current")


class _SonusIsdnsgServiceGroupPrimaryDchannelInterface_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupPrimaryDchannelInterface based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgServiceGroupPrimaryDchannelInterface_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupPrimaryDchannelInterface_Object = MibTableColumn
sonusIsdnsgServiceGroupPrimaryDchannelInterface = _SonusIsdnsgServiceGroupPrimaryDchannelInterface_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 10),
    _SonusIsdnsgServiceGroupPrimaryDchannelInterface_Type()
)
sonusIsdnsgServiceGroupPrimaryDchannelInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupPrimaryDchannelInterface.setStatus("current")


class _SonusIsdnsgServiceGroupPrimaryDchannelTimeSlot_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupPrimaryDchannelTimeSlot based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_SonusIsdnsgServiceGroupPrimaryDchannelTimeSlot_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupPrimaryDchannelTimeSlot_Object = MibTableColumn
sonusIsdnsgServiceGroupPrimaryDchannelTimeSlot = _SonusIsdnsgServiceGroupPrimaryDchannelTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 11),
    _SonusIsdnsgServiceGroupPrimaryDchannelTimeSlot_Type()
)
sonusIsdnsgServiceGroupPrimaryDchannelTimeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupPrimaryDchannelTimeSlot.setStatus("current")


class _SonusIsdnsgServiceGroupPrimaryDchannelMode_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupPrimaryDchannelMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 2),
          ("outOfService", 1))
    )


_SonusIsdnsgServiceGroupPrimaryDchannelMode_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupPrimaryDchannelMode_Object = MibTableColumn
sonusIsdnsgServiceGroupPrimaryDchannelMode = _SonusIsdnsgServiceGroupPrimaryDchannelMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 12),
    _SonusIsdnsgServiceGroupPrimaryDchannelMode_Type()
)
sonusIsdnsgServiceGroupPrimaryDchannelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupPrimaryDchannelMode.setStatus("current")


class _SonusIsdnsgServiceGroupBackupDchannelInterface_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupBackupDchannelInterface based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgServiceGroupBackupDchannelInterface_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupBackupDchannelInterface_Object = MibTableColumn
sonusIsdnsgServiceGroupBackupDchannelInterface = _SonusIsdnsgServiceGroupBackupDchannelInterface_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 13),
    _SonusIsdnsgServiceGroupBackupDchannelInterface_Type()
)
sonusIsdnsgServiceGroupBackupDchannelInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupBackupDchannelInterface.setStatus("current")


class _SonusIsdnsgServiceGroupBackupDchannelTimeSlot_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupBackupDchannelTimeSlot based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_SonusIsdnsgServiceGroupBackupDchannelTimeSlot_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupBackupDchannelTimeSlot_Object = MibTableColumn
sonusIsdnsgServiceGroupBackupDchannelTimeSlot = _SonusIsdnsgServiceGroupBackupDchannelTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 14),
    _SonusIsdnsgServiceGroupBackupDchannelTimeSlot_Type()
)
sonusIsdnsgServiceGroupBackupDchannelTimeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupBackupDchannelTimeSlot.setStatus("current")


class _SonusIsdnsgServiceGroupBackupDchannelMode_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupBackupDchannelMode based on Integer32"""
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
        *(("inService", 2),
          ("outOfService", 1),
          ("unEquipped", 3))
    )


_SonusIsdnsgServiceGroupBackupDchannelMode_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupBackupDchannelMode_Object = MibTableColumn
sonusIsdnsgServiceGroupBackupDchannelMode = _SonusIsdnsgServiceGroupBackupDchannelMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 15),
    _SonusIsdnsgServiceGroupBackupDchannelMode_Type()
)
sonusIsdnsgServiceGroupBackupDchannelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupBackupDchannelMode.setStatus("current")


class _SonusIsdnsgServiceGroupLayerTrace_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupLayerTrace based on Integer32"""
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
        *(("both", 4),
          ("layer2", 2),
          ("layer3", 3),
          ("none", 1))
    )


_SonusIsdnsgServiceGroupLayerTrace_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupLayerTrace_Object = MibTableColumn
sonusIsdnsgServiceGroupLayerTrace = _SonusIsdnsgServiceGroupLayerTrace_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 16),
    _SonusIsdnsgServiceGroupLayerTrace_Type()
)
sonusIsdnsgServiceGroupLayerTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupLayerTrace.setStatus("current")


class _SonusIsdnsgServiceGroupMode_Type(SonusServiceState):
    """Custom type sonusIsdnsgServiceGroupMode based on SonusServiceState"""


_SonusIsdnsgServiceGroupMode_Object = MibTableColumn
sonusIsdnsgServiceGroupMode = _SonusIsdnsgServiceGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 17),
    _SonusIsdnsgServiceGroupMode_Type()
)
sonusIsdnsgServiceGroupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupMode.setStatus("current")


class _SonusIsdnsgServiceGroupAction_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dryUp", 1),
          ("force", 2))
    )


_SonusIsdnsgServiceGroupAction_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupAction_Object = MibTableColumn
sonusIsdnsgServiceGroupAction = _SonusIsdnsgServiceGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 18),
    _SonusIsdnsgServiceGroupAction_Type()
)
sonusIsdnsgServiceGroupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupAction.setStatus("current")


class _SonusIsdnsgServiceGroupTimeout_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_SonusIsdnsgServiceGroupTimeout_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupTimeout_Object = MibTableColumn
sonusIsdnsgServiceGroupTimeout = _SonusIsdnsgServiceGroupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 19),
    _SonusIsdnsgServiceGroupTimeout_Type()
)
sonusIsdnsgServiceGroupTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupTimeout.setStatus("current")


class _SonusIsdnsgServiceGroupAdminState_Type(SonusAdminState):
    """Custom type sonusIsdnsgServiceGroupAdminState based on SonusAdminState"""


_SonusIsdnsgServiceGroupAdminState_Object = MibTableColumn
sonusIsdnsgServiceGroupAdminState = _SonusIsdnsgServiceGroupAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 20),
    _SonusIsdnsgServiceGroupAdminState_Type()
)
sonusIsdnsgServiceGroupAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupAdminState.setStatus("current")


class _SonusIsdnsgServiceGroupProfileName_Type(DisplayString):
    """Custom type sonusIsdnsgServiceGroupProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusIsdnsgServiceGroupProfileName_Type.__name__ = "DisplayString"
_SonusIsdnsgServiceGroupProfileName_Object = MibTableColumn
sonusIsdnsgServiceGroupProfileName = _SonusIsdnsgServiceGroupProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 21),
    _SonusIsdnsgServiceGroupProfileName_Type()
)
sonusIsdnsgServiceGroupProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupProfileName.setStatus("current")
_SonusIsdnsgServiceGroupRowStatus_Type = RowStatus
_SonusIsdnsgServiceGroupRowStatus_Object = MibTableColumn
sonusIsdnsgServiceGroupRowStatus = _SonusIsdnsgServiceGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 22),
    _SonusIsdnsgServiceGroupRowStatus_Type()
)
sonusIsdnsgServiceGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupRowStatus.setStatus("current")


class _SonusIsdnsgServiceGroupDefaultDirectoryNumber_Type(DisplayString):
    """Custom type sonusIsdnsgServiceGroupDefaultDirectoryNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SonusIsdnsgServiceGroupDefaultDirectoryNumber_Type.__name__ = "DisplayString"
_SonusIsdnsgServiceGroupDefaultDirectoryNumber_Object = MibTableColumn
sonusIsdnsgServiceGroupDefaultDirectoryNumber = _SonusIsdnsgServiceGroupDefaultDirectoryNumber_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 23),
    _SonusIsdnsgServiceGroupDefaultDirectoryNumber_Type()
)
sonusIsdnsgServiceGroupDefaultDirectoryNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupDefaultDirectoryNumber.setStatus("current")


class _SonusIsdnsgServiceGroupCallingPartyNumberProvision_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupCallingPartyNumberProvision based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("necessary", 1),
          ("notNecessary", 2))
    )


_SonusIsdnsgServiceGroupCallingPartyNumberProvision_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupCallingPartyNumberProvision_Object = MibTableColumn
sonusIsdnsgServiceGroupCallingPartyNumberProvision = _SonusIsdnsgServiceGroupCallingPartyNumberProvision_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 24),
    _SonusIsdnsgServiceGroupCallingPartyNumberProvision_Type()
)
sonusIsdnsgServiceGroupCallingPartyNumberProvision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupCallingPartyNumberProvision.setStatus("current")


class _SonusIsdnsgServiceGroupCallingPartyNumberDiscard_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupCallingPartyNumberDiscard based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SonusIsdnsgServiceGroupCallingPartyNumberDiscard_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupCallingPartyNumberDiscard_Object = MibTableColumn
sonusIsdnsgServiceGroupCallingPartyNumberDiscard = _SonusIsdnsgServiceGroupCallingPartyNumberDiscard_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 25),
    _SonusIsdnsgServiceGroupCallingPartyNumberDiscard_Type()
)
sonusIsdnsgServiceGroupCallingPartyNumberDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupCallingPartyNumberDiscard.setStatus("current")


class _SonusIsdnsgServiceGroupCallingPartyNumberDelivery_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupCallingPartyNumberDelivery based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SonusIsdnsgServiceGroupCallingPartyNumberDelivery_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupCallingPartyNumberDelivery_Object = MibTableColumn
sonusIsdnsgServiceGroupCallingPartyNumberDelivery = _SonusIsdnsgServiceGroupCallingPartyNumberDelivery_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 26),
    _SonusIsdnsgServiceGroupCallingPartyNumberDelivery_Type()
)
sonusIsdnsgServiceGroupCallingPartyNumberDelivery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupCallingPartyNumberDelivery.setStatus("current")


class _SonusIsdnsgServiceGroupCallingPartySubAddressTransfer_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupCallingPartySubAddressTransfer based on Integer32"""
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
        *(("conditional", 3),
          ("no", 2),
          ("yes", 1))
    )


_SonusIsdnsgServiceGroupCallingPartySubAddressTransfer_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupCallingPartySubAddressTransfer_Object = MibTableColumn
sonusIsdnsgServiceGroupCallingPartySubAddressTransfer = _SonusIsdnsgServiceGroupCallingPartySubAddressTransfer_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 27),
    _SonusIsdnsgServiceGroupCallingPartySubAddressTransfer_Type()
)
sonusIsdnsgServiceGroupCallingPartySubAddressTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupCallingPartySubAddressTransfer.setStatus("current")


class _SonusIsdnsgServiceGroupCallingPartySubAddressDelivery_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupCallingPartySubAddressDelivery based on Integer32"""
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
        *(("conditional", 3),
          ("no", 2),
          ("yes", 1))
    )


_SonusIsdnsgServiceGroupCallingPartySubAddressDelivery_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupCallingPartySubAddressDelivery_Object = MibTableColumn
sonusIsdnsgServiceGroupCallingPartySubAddressDelivery = _SonusIsdnsgServiceGroupCallingPartySubAddressDelivery_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 28),
    _SonusIsdnsgServiceGroupCallingPartySubAddressDelivery_Type()
)
sonusIsdnsgServiceGroupCallingPartySubAddressDelivery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupCallingPartySubAddressDelivery.setStatus("current")


class _SonusIsdnsgServiceGroupBchannelAvailabilitySignaling_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupBchannelAvailabilitySignaling based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SonusIsdnsgServiceGroupBchannelAvailabilitySignaling_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupBchannelAvailabilitySignaling_Object = MibTableColumn
sonusIsdnsgServiceGroupBchannelAvailabilitySignaling = _SonusIsdnsgServiceGroupBchannelAvailabilitySignaling_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 29),
    _SonusIsdnsgServiceGroupBchannelAvailabilitySignaling_Type()
)
sonusIsdnsgServiceGroupBchannelAvailabilitySignaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupBchannelAvailabilitySignaling.setStatus("current")


class _SonusIsdnsgServiceGroupVerboseTrace_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupVerboseTrace based on Integer32"""
    defaultValue = 2

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


_SonusIsdnsgServiceGroupVerboseTrace_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupVerboseTrace_Object = MibTableColumn
sonusIsdnsgServiceGroupVerboseTrace = _SonusIsdnsgServiceGroupVerboseTrace_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 30),
    _SonusIsdnsgServiceGroupVerboseTrace_Type()
)
sonusIsdnsgServiceGroupVerboseTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupVerboseTrace.setStatus("current")


class _SonusIsdnsgServiceGroupCallingPartyNumberPresentation_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupCallingPartyNumberPresentation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SonusIsdnsgServiceGroupCallingPartyNumberPresentation_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupCallingPartyNumberPresentation_Object = MibTableColumn
sonusIsdnsgServiceGroupCallingPartyNumberPresentation = _SonusIsdnsgServiceGroupCallingPartyNumberPresentation_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 31),
    _SonusIsdnsgServiceGroupCallingPartyNumberPresentation_Type()
)
sonusIsdnsgServiceGroupCallingPartyNumberPresentation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupCallingPartyNumberPresentation.setStatus("current")
_SonusIsdnsgServiceGroupDiscTreatmentProfileName_Type = SonusNameReference
_SonusIsdnsgServiceGroupDiscTreatmentProfileName_Object = MibTableColumn
sonusIsdnsgServiceGroupDiscTreatmentProfileName = _SonusIsdnsgServiceGroupDiscTreatmentProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 32),
    _SonusIsdnsgServiceGroupDiscTreatmentProfileName_Type()
)
sonusIsdnsgServiceGroupDiscTreatmentProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupDiscTreatmentProfileName.setStatus("current")
_SonusIsdnsgServiceGroupTonePackageName_Type = SonusNameReference
_SonusIsdnsgServiceGroupTonePackageName_Object = MibTableColumn
sonusIsdnsgServiceGroupTonePackageName = _SonusIsdnsgServiceGroupTonePackageName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 33),
    _SonusIsdnsgServiceGroupTonePackageName_Type()
)
sonusIsdnsgServiceGroupTonePackageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupTonePackageName.setStatus("current")


class _SonusIsdnsgServiceGroupT302_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupT302 based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgServiceGroupT302_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupT302_Object = MibTableColumn
sonusIsdnsgServiceGroupT302 = _SonusIsdnsgServiceGroupT302_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 34),
    _SonusIsdnsgServiceGroupT302_Type()
)
sonusIsdnsgServiceGroupT302.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupT302.setStatus("current")


class _SonusIsdnsgServiceGroupT303_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupT303 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgServiceGroupT303_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupT303_Object = MibTableColumn
sonusIsdnsgServiceGroupT303 = _SonusIsdnsgServiceGroupT303_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 35),
    _SonusIsdnsgServiceGroupT303_Type()
)
sonusIsdnsgServiceGroupT303.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupT303.setStatus("current")


class _SonusIsdnsgServiceGroupT304_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupT304 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgServiceGroupT304_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupT304_Object = MibTableColumn
sonusIsdnsgServiceGroupT304 = _SonusIsdnsgServiceGroupT304_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 36),
    _SonusIsdnsgServiceGroupT304_Type()
)
sonusIsdnsgServiceGroupT304.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupT304.setStatus("current")


class _SonusIsdnsgServiceGroupT305_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupT305 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgServiceGroupT305_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupT305_Object = MibTableColumn
sonusIsdnsgServiceGroupT305 = _SonusIsdnsgServiceGroupT305_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 37),
    _SonusIsdnsgServiceGroupT305_Type()
)
sonusIsdnsgServiceGroupT305.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupT305.setStatus("current")


class _SonusIsdnsgServiceGroupT306_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupT306 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgServiceGroupT306_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupT306_Object = MibTableColumn
sonusIsdnsgServiceGroupT306 = _SonusIsdnsgServiceGroupT306_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 38),
    _SonusIsdnsgServiceGroupT306_Type()
)
sonusIsdnsgServiceGroupT306.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupT306.setStatus("current")


class _SonusIsdnsgServiceGroupT308_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupT308 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgServiceGroupT308_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupT308_Object = MibTableColumn
sonusIsdnsgServiceGroupT308 = _SonusIsdnsgServiceGroupT308_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 39),
    _SonusIsdnsgServiceGroupT308_Type()
)
sonusIsdnsgServiceGroupT308.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupT308.setStatus("current")


class _SonusIsdnsgServiceGroupT309_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupT309 based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgServiceGroupT309_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupT309_Object = MibTableColumn
sonusIsdnsgServiceGroupT309 = _SonusIsdnsgServiceGroupT309_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 40),
    _SonusIsdnsgServiceGroupT309_Type()
)
sonusIsdnsgServiceGroupT309.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupT309.setStatus("current")


class _SonusIsdnsgServiceGroupT310_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupT310 based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgServiceGroupT310_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupT310_Object = MibTableColumn
sonusIsdnsgServiceGroupT310 = _SonusIsdnsgServiceGroupT310_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 41),
    _SonusIsdnsgServiceGroupT310_Type()
)
sonusIsdnsgServiceGroupT310.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupT310.setStatus("current")


class _SonusIsdnsgServiceGroupT312_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupT312 based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgServiceGroupT312_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupT312_Object = MibTableColumn
sonusIsdnsgServiceGroupT312 = _SonusIsdnsgServiceGroupT312_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 42),
    _SonusIsdnsgServiceGroupT312_Type()
)
sonusIsdnsgServiceGroupT312.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupT312.setStatus("current")


class _SonusIsdnsgServiceGroupT313_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupT313 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgServiceGroupT313_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupT313_Object = MibTableColumn
sonusIsdnsgServiceGroupT313 = _SonusIsdnsgServiceGroupT313_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 43),
    _SonusIsdnsgServiceGroupT313_Type()
)
sonusIsdnsgServiceGroupT313.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupT313.setStatus("current")


class _SonusIsdnsgServiceGroupT314_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupT314 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgServiceGroupT314_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupT314_Object = MibTableColumn
sonusIsdnsgServiceGroupT314 = _SonusIsdnsgServiceGroupT314_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 44),
    _SonusIsdnsgServiceGroupT314_Type()
)
sonusIsdnsgServiceGroupT314.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupT314.setStatus("current")


class _SonusIsdnsgServiceGroupT318_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupT318 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgServiceGroupT318_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupT318_Object = MibTableColumn
sonusIsdnsgServiceGroupT318 = _SonusIsdnsgServiceGroupT318_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 45),
    _SonusIsdnsgServiceGroupT318_Type()
)
sonusIsdnsgServiceGroupT318.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupT318.setStatus("current")


class _SonusIsdnsgServiceGroupT319_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupT319 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgServiceGroupT319_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupT319_Object = MibTableColumn
sonusIsdnsgServiceGroupT319 = _SonusIsdnsgServiceGroupT319_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 46),
    _SonusIsdnsgServiceGroupT319_Type()
)
sonusIsdnsgServiceGroupT319.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupT319.setStatus("current")


class _SonusIsdnsgServiceGroupT322_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupT322 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgServiceGroupT322_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupT322_Object = MibTableColumn
sonusIsdnsgServiceGroupT322 = _SonusIsdnsgServiceGroupT322_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 47),
    _SonusIsdnsgServiceGroupT322_Type()
)
sonusIsdnsgServiceGroupT322.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupT322.setStatus("current")


class _SonusIsdnsgServiceGroupK_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupK based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_SonusIsdnsgServiceGroupK_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupK_Object = MibTableColumn
sonusIsdnsgServiceGroupK = _SonusIsdnsgServiceGroupK_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 48),
    _SonusIsdnsgServiceGroupK_Type()
)
sonusIsdnsgServiceGroupK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupK.setStatus("current")


class _SonusIsdnsgServiceGroupT200_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupT200 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SonusIsdnsgServiceGroupT200_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupT200_Object = MibTableColumn
sonusIsdnsgServiceGroupT200 = _SonusIsdnsgServiceGroupT200_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 49),
    _SonusIsdnsgServiceGroupT200_Type()
)
sonusIsdnsgServiceGroupT200.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupT200.setStatus("current")


class _SonusIsdnsgServiceGroupT203_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupT203 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SonusIsdnsgServiceGroupT203_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupT203_Object = MibTableColumn
sonusIsdnsgServiceGroupT203 = _SonusIsdnsgServiceGroupT203_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 50),
    _SonusIsdnsgServiceGroupT203_Type()
)
sonusIsdnsgServiceGroupT203.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupT203.setStatus("current")


class _SonusIsdnsgServiceGroupN200_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupN200 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SonusIsdnsgServiceGroupN200_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupN200_Object = MibTableColumn
sonusIsdnsgServiceGroupN200 = _SonusIsdnsgServiceGroupN200_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 51),
    _SonusIsdnsgServiceGroupN200_Type()
)
sonusIsdnsgServiceGroupN200.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupN200.setStatus("current")


class _SonusIsdnsgServiceGroupN201_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupN201 based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 260),
    )


_SonusIsdnsgServiceGroupN201_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupN201_Object = MibTableColumn
sonusIsdnsgServiceGroupN201 = _SonusIsdnsgServiceGroupN201_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 52),
    _SonusIsdnsgServiceGroupN201_Type()
)
sonusIsdnsgServiceGroupN201.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupN201.setStatus("current")


class _SonusIsdnsgServiceGroupBchannelInitialRestart_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupBchannelInitialRestart based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SonusIsdnsgServiceGroupBchannelInitialRestart_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupBchannelInitialRestart_Object = MibTableColumn
sonusIsdnsgServiceGroupBchannelInitialRestart = _SonusIsdnsgServiceGroupBchannelInitialRestart_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 53),
    _SonusIsdnsgServiceGroupBchannelInitialRestart_Type()
)
sonusIsdnsgServiceGroupBchannelInitialRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupBchannelInitialRestart.setStatus("current")
_SonusIsdnsgServiceGroupIuaApplicationServer_Type = SonusNameReference
_SonusIsdnsgServiceGroupIuaApplicationServer_Object = MibTableColumn
sonusIsdnsgServiceGroupIuaApplicationServer = _SonusIsdnsgServiceGroupIuaApplicationServer_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 54),
    _SonusIsdnsgServiceGroupIuaApplicationServer_Type()
)
sonusIsdnsgServiceGroupIuaApplicationServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupIuaApplicationServer.setStatus("current")


class _SonusIsdnsgServiceGroupIuaAutoDatalinkEstablish_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupIuaAutoDatalinkEstablish based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SonusIsdnsgServiceGroupIuaAutoDatalinkEstablish_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupIuaAutoDatalinkEstablish_Object = MibTableColumn
sonusIsdnsgServiceGroupIuaAutoDatalinkEstablish = _SonusIsdnsgServiceGroupIuaAutoDatalinkEstablish_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 1, 2, 1, 55),
    _SonusIsdnsgServiceGroupIuaAutoDatalinkEstablish_Type()
)
sonusIsdnsgServiceGroupIuaAutoDatalinkEstablish.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupIuaAutoDatalinkEstablish.setStatus("current")
_SonusIsdnsgServiceGroupStatTable_Object = MibTable
sonusIsdnsgServiceGroupStatTable = _SonusIsdnsgServiceGroupStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 2)
)
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupStatTable.setStatus("current")
_SonusIsdnsgServiceGroupStatEntry_Object = MibTableRow
sonusIsdnsgServiceGroupStatEntry = _SonusIsdnsgServiceGroupStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 2, 1)
)
sonusIsdnsgServiceGroupStatEntry.setIndexNames(
    (0, "SONUS-ISDN-SERVICE-GROUP-MIB", "sonusIsdnsgServiceGroupStatListIndex"),
)
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupStatEntry.setStatus("current")
_SonusIsdnsgServiceGroupStatListIndex_Type = Integer32
_SonusIsdnsgServiceGroupStatListIndex_Object = MibTableColumn
sonusIsdnsgServiceGroupStatListIndex = _SonusIsdnsgServiceGroupStatListIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 2, 1, 1),
    _SonusIsdnsgServiceGroupStatListIndex_Type()
)
sonusIsdnsgServiceGroupStatListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupStatListIndex.setStatus("current")


class _SonusIsdnsgServiceGroupStatStatus_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupStatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("dryup", 3),
          ("unavailable", 2))
    )


_SonusIsdnsgServiceGroupStatStatus_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupStatStatus_Object = MibTableColumn
sonusIsdnsgServiceGroupStatStatus = _SonusIsdnsgServiceGroupStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 2, 1, 2),
    _SonusIsdnsgServiceGroupStatStatus_Type()
)
sonusIsdnsgServiceGroupStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupStatStatus.setStatus("current")


class _SonusIsdnsgServiceGroupStatTgMode_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupStatTgMode based on Integer32"""
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


_SonusIsdnsgServiceGroupStatTgMode_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupStatTgMode_Object = MibTableColumn
sonusIsdnsgServiceGroupStatTgMode = _SonusIsdnsgServiceGroupStatTgMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 2, 1, 3),
    _SonusIsdnsgServiceGroupStatTgMode_Type()
)
sonusIsdnsgServiceGroupStatTgMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupStatTgMode.setStatus("current")
_SonusIsdnsgServiceGroupStatNumBchConfigured_Type = Integer32
_SonusIsdnsgServiceGroupStatNumBchConfigured_Object = MibTableColumn
sonusIsdnsgServiceGroupStatNumBchConfigured = _SonusIsdnsgServiceGroupStatNumBchConfigured_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 2, 1, 4),
    _SonusIsdnsgServiceGroupStatNumBchConfigured_Type()
)
sonusIsdnsgServiceGroupStatNumBchConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupStatNumBchConfigured.setStatus("current")
_SonusIsdnsgServiceGroupStatNumBchAvailable_Type = Integer32
_SonusIsdnsgServiceGroupStatNumBchAvailable_Object = MibTableColumn
sonusIsdnsgServiceGroupStatNumBchAvailable = _SonusIsdnsgServiceGroupStatNumBchAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 2, 1, 5),
    _SonusIsdnsgServiceGroupStatNumBchAvailable_Type()
)
sonusIsdnsgServiceGroupStatNumBchAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupStatNumBchAvailable.setStatus("current")
_SonusIsdnsgServiceGroupStatInCallsActive_Type = Counter32
_SonusIsdnsgServiceGroupStatInCallsActive_Object = MibTableColumn
sonusIsdnsgServiceGroupStatInCallsActive = _SonusIsdnsgServiceGroupStatInCallsActive_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 2, 1, 6),
    _SonusIsdnsgServiceGroupStatInCallsActive_Type()
)
sonusIsdnsgServiceGroupStatInCallsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupStatInCallsActive.setStatus("current")
_SonusIsdnsgServiceGroupStatInCalls_Type = Counter32
_SonusIsdnsgServiceGroupStatInCalls_Object = MibTableColumn
sonusIsdnsgServiceGroupStatInCalls = _SonusIsdnsgServiceGroupStatInCalls_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 2, 1, 7),
    _SonusIsdnsgServiceGroupStatInCalls_Type()
)
sonusIsdnsgServiceGroupStatInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupStatInCalls.setStatus("current")
_SonusIsdnsgServiceGroupStatInConnected_Type = Counter32
_SonusIsdnsgServiceGroupStatInConnected_Object = MibTableColumn
sonusIsdnsgServiceGroupStatInConnected = _SonusIsdnsgServiceGroupStatInConnected_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 2, 1, 8),
    _SonusIsdnsgServiceGroupStatInConnected_Type()
)
sonusIsdnsgServiceGroupStatInConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupStatInConnected.setStatus("current")
_SonusIsdnsgServiceGroupStatOutCallsActive_Type = Counter32
_SonusIsdnsgServiceGroupStatOutCallsActive_Object = MibTableColumn
sonusIsdnsgServiceGroupStatOutCallsActive = _SonusIsdnsgServiceGroupStatOutCallsActive_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 2, 1, 9),
    _SonusIsdnsgServiceGroupStatOutCallsActive_Type()
)
sonusIsdnsgServiceGroupStatOutCallsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupStatOutCallsActive.setStatus("current")
_SonusIsdnsgServiceGroupStatOutCalls_Type = Counter32
_SonusIsdnsgServiceGroupStatOutCalls_Object = MibTableColumn
sonusIsdnsgServiceGroupStatOutCalls = _SonusIsdnsgServiceGroupStatOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 2, 1, 10),
    _SonusIsdnsgServiceGroupStatOutCalls_Type()
)
sonusIsdnsgServiceGroupStatOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupStatOutCalls.setStatus("current")
_SonusIsdnsgServiceGroupStatOutConnected_Type = Counter32
_SonusIsdnsgServiceGroupStatOutConnected_Object = MibTableColumn
sonusIsdnsgServiceGroupStatOutConnected = _SonusIsdnsgServiceGroupStatOutConnected_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 2, 1, 11),
    _SonusIsdnsgServiceGroupStatOutConnected_Type()
)
sonusIsdnsgServiceGroupStatOutConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupStatOutConnected.setStatus("current")


class _SonusIsdnsgServiceGroupStatPrimaryDchannel_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupStatPrimaryDchannel based on Integer32"""
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
        *(("inService", 1),
          ("maintenanceBusy", 5),
          ("manualOos", 3),
          ("outOfService", 2),
          ("standby", 4),
          ("unEquipped", 6),
          ("wait", 7))
    )


_SonusIsdnsgServiceGroupStatPrimaryDchannel_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupStatPrimaryDchannel_Object = MibTableColumn
sonusIsdnsgServiceGroupStatPrimaryDchannel = _SonusIsdnsgServiceGroupStatPrimaryDchannel_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 2, 1, 12),
    _SonusIsdnsgServiceGroupStatPrimaryDchannel_Type()
)
sonusIsdnsgServiceGroupStatPrimaryDchannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupStatPrimaryDchannel.setStatus("current")
_SonusIsdnsgServiceGroupStatPrimaryDchInPkts_Type = Counter32
_SonusIsdnsgServiceGroupStatPrimaryDchInPkts_Object = MibTableColumn
sonusIsdnsgServiceGroupStatPrimaryDchInPkts = _SonusIsdnsgServiceGroupStatPrimaryDchInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 2, 1, 13),
    _SonusIsdnsgServiceGroupStatPrimaryDchInPkts_Type()
)
sonusIsdnsgServiceGroupStatPrimaryDchInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupStatPrimaryDchInPkts.setStatus("current")
_SonusIsdnsgServiceGroupStatPrimaryDchOutPkts_Type = Counter32
_SonusIsdnsgServiceGroupStatPrimaryDchOutPkts_Object = MibTableColumn
sonusIsdnsgServiceGroupStatPrimaryDchOutPkts = _SonusIsdnsgServiceGroupStatPrimaryDchOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 2, 1, 14),
    _SonusIsdnsgServiceGroupStatPrimaryDchOutPkts_Type()
)
sonusIsdnsgServiceGroupStatPrimaryDchOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupStatPrimaryDchOutPkts.setStatus("current")
_SonusIsdnsgServiceGroupStatPrimaryDchInBytes_Type = Counter32
_SonusIsdnsgServiceGroupStatPrimaryDchInBytes_Object = MibTableColumn
sonusIsdnsgServiceGroupStatPrimaryDchInBytes = _SonusIsdnsgServiceGroupStatPrimaryDchInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 2, 1, 15),
    _SonusIsdnsgServiceGroupStatPrimaryDchInBytes_Type()
)
sonusIsdnsgServiceGroupStatPrimaryDchInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupStatPrimaryDchInBytes.setStatus("current")
_SonusIsdnsgServiceGroupStatPrimaryDchOutBytes_Type = Counter32
_SonusIsdnsgServiceGroupStatPrimaryDchOutBytes_Object = MibTableColumn
sonusIsdnsgServiceGroupStatPrimaryDchOutBytes = _SonusIsdnsgServiceGroupStatPrimaryDchOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 2, 1, 16),
    _SonusIsdnsgServiceGroupStatPrimaryDchOutBytes_Type()
)
sonusIsdnsgServiceGroupStatPrimaryDchOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupStatPrimaryDchOutBytes.setStatus("current")


class _SonusIsdnsgServiceGroupStatBackupDchannel_Type(Integer32):
    """Custom type sonusIsdnsgServiceGroupStatBackupDchannel based on Integer32"""
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
        *(("inService", 1),
          ("maintenanceBusy", 5),
          ("manualOos", 3),
          ("outOfService", 2),
          ("standby", 4),
          ("unEquipped", 6),
          ("wait", 7))
    )


_SonusIsdnsgServiceGroupStatBackupDchannel_Type.__name__ = "Integer32"
_SonusIsdnsgServiceGroupStatBackupDchannel_Object = MibTableColumn
sonusIsdnsgServiceGroupStatBackupDchannel = _SonusIsdnsgServiceGroupStatBackupDchannel_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 2, 1, 17),
    _SonusIsdnsgServiceGroupStatBackupDchannel_Type()
)
sonusIsdnsgServiceGroupStatBackupDchannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupStatBackupDchannel.setStatus("current")
_SonusIsdnsgServiceGroupStatBackupDchInPkts_Type = Counter32
_SonusIsdnsgServiceGroupStatBackupDchInPkts_Object = MibTableColumn
sonusIsdnsgServiceGroupStatBackupDchInPkts = _SonusIsdnsgServiceGroupStatBackupDchInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 2, 1, 18),
    _SonusIsdnsgServiceGroupStatBackupDchInPkts_Type()
)
sonusIsdnsgServiceGroupStatBackupDchInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupStatBackupDchInPkts.setStatus("current")
_SonusIsdnsgServiceGroupStatBackupDchOutPkts_Type = Counter32
_SonusIsdnsgServiceGroupStatBackupDchOutPkts_Object = MibTableColumn
sonusIsdnsgServiceGroupStatBackupDchOutPkts = _SonusIsdnsgServiceGroupStatBackupDchOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 2, 1, 19),
    _SonusIsdnsgServiceGroupStatBackupDchOutPkts_Type()
)
sonusIsdnsgServiceGroupStatBackupDchOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupStatBackupDchOutPkts.setStatus("current")
_SonusIsdnsgServiceGroupStatBackupDchInBytes_Type = Counter32
_SonusIsdnsgServiceGroupStatBackupDchInBytes_Object = MibTableColumn
sonusIsdnsgServiceGroupStatBackupDchInBytes = _SonusIsdnsgServiceGroupStatBackupDchInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 2, 1, 20),
    _SonusIsdnsgServiceGroupStatBackupDchInBytes_Type()
)
sonusIsdnsgServiceGroupStatBackupDchInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupStatBackupDchInBytes.setStatus("current")
_SonusIsdnsgServiceGroupStatBackupDchOutBytes_Type = Counter32
_SonusIsdnsgServiceGroupStatBackupDchOutBytes_Object = MibTableColumn
sonusIsdnsgServiceGroupStatBackupDchOutBytes = _SonusIsdnsgServiceGroupStatBackupDchOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 2, 1, 21),
    _SonusIsdnsgServiceGroupStatBackupDchOutBytes_Type()
)
sonusIsdnsgServiceGroupStatBackupDchOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgServiceGroupStatBackupDchOutBytes.setStatus("current")
_SonusIsdnsgProfile_ObjectIdentity = ObjectIdentity
sonusIsdnsgProfile = _SonusIsdnsgProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 3)
)
_SonusIsdnsgProfileNextIndex_Type = Integer32
_SonusIsdnsgProfileNextIndex_Object = MibScalar
sonusIsdnsgProfileNextIndex = _SonusIsdnsgProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 3, 1),
    _SonusIsdnsgProfileNextIndex_Type()
)
sonusIsdnsgProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgProfileNextIndex.setStatus("current")
_SonusIsdnsgProfileTable_Object = MibTable
sonusIsdnsgProfileTable = _SonusIsdnsgProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 3, 2)
)
if mibBuilder.loadTexts:
    sonusIsdnsgProfileTable.setStatus("current")
_SonusIsdnsgProfileEntry_Object = MibTableRow
sonusIsdnsgProfileEntry = _SonusIsdnsgProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 3, 2, 1)
)
sonusIsdnsgProfileEntry.setIndexNames(
    (0, "SONUS-ISDN-SERVICE-GROUP-MIB", "sonusIsdnsgProfileListIndex"),
)
if mibBuilder.loadTexts:
    sonusIsdnsgProfileEntry.setStatus("current")


class _SonusIsdnsgProfileListIndex_Type(Integer32):
    """Custom type sonusIsdnsgProfileListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SonusIsdnsgProfileListIndex_Type.__name__ = "Integer32"
_SonusIsdnsgProfileListIndex_Object = MibTableColumn
sonusIsdnsgProfileListIndex = _SonusIsdnsgProfileListIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 3, 2, 1, 1),
    _SonusIsdnsgProfileListIndex_Type()
)
sonusIsdnsgProfileListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgProfileListIndex.setStatus("current")
_SonusIsdnsgProfileName_Type = SonusName
_SonusIsdnsgProfileName_Object = MibTableColumn
sonusIsdnsgProfileName = _SonusIsdnsgProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 3, 2, 1, 2),
    _SonusIsdnsgProfileName_Type()
)
sonusIsdnsgProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgProfileName.setStatus("current")
_SonusIsdnsgProfileTrunkGroup_Type = SonusNameReference
_SonusIsdnsgProfileTrunkGroup_Object = MibTableColumn
sonusIsdnsgProfileTrunkGroup = _SonusIsdnsgProfileTrunkGroup_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 3, 2, 1, 3),
    _SonusIsdnsgProfileTrunkGroup_Type()
)
sonusIsdnsgProfileTrunkGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgProfileTrunkGroup.setStatus("current")


class _SonusIsdnsgProfileHuntAlgorithm_Type(Integer32):
    """Custom type sonusIsdnsgProfileHuntAlgorithm based on Integer32"""
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
        *(("circularbackward", 4),
          ("circularforward", 3),
          ("highhigh", 2),
          ("lowlow", 1))
    )


_SonusIsdnsgProfileHuntAlgorithm_Type.__name__ = "Integer32"
_SonusIsdnsgProfileHuntAlgorithm_Object = MibTableColumn
sonusIsdnsgProfileHuntAlgorithm = _SonusIsdnsgProfileHuntAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 3, 2, 1, 4),
    _SonusIsdnsgProfileHuntAlgorithm_Type()
)
sonusIsdnsgProfileHuntAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgProfileHuntAlgorithm.setStatus("current")


class _SonusIsdnsgProfileCost_Type(Integer32):
    """Custom type sonusIsdnsgProfileCost based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SonusIsdnsgProfileCost_Type.__name__ = "Integer32"
_SonusIsdnsgProfileCost_Object = MibTableColumn
sonusIsdnsgProfileCost = _SonusIsdnsgProfileCost_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 3, 2, 1, 5),
    _SonusIsdnsgProfileCost_Type()
)
sonusIsdnsgProfileCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgProfileCost.setStatus("current")


class _SonusIsdnsgProfileSwitchSide_Type(Integer32):
    """Custom type sonusIsdnsgProfileSwitchSide based on Integer32"""
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
        *(("network", 1),
          ("user", 2),
          ("usersym", 3))
    )


_SonusIsdnsgProfileSwitchSide_Type.__name__ = "Integer32"
_SonusIsdnsgProfileSwitchSide_Object = MibTableColumn
sonusIsdnsgProfileSwitchSide = _SonusIsdnsgProfileSwitchSide_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 3, 2, 1, 6),
    _SonusIsdnsgProfileSwitchSide_Type()
)
sonusIsdnsgProfileSwitchSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgProfileSwitchSide.setStatus("deprecated")


class _SonusIsdnsgProfileSwitchType_Type(Integer32):
    """Custom type sonusIsdnsgProfileSwitchType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("dms100", 3),
          ("dms250", 2),
          ("euroIsdn", 6),
          ("ins1500", 7),
          ("lucent4ESS", 5),
          ("lucent5ESS", 4),
          ("ni2", 1))
    )


_SonusIsdnsgProfileSwitchType_Type.__name__ = "Integer32"
_SonusIsdnsgProfileSwitchType_Object = MibTableColumn
sonusIsdnsgProfileSwitchType = _SonusIsdnsgProfileSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 3, 2, 1, 7),
    _SonusIsdnsgProfileSwitchType_Type()
)
sonusIsdnsgProfileSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgProfileSwitchType.setStatus("deprecated")


class _SonusIsdnsgProfileSwitchProfile_Type(DisplayString):
    """Custom type sonusIsdnsgProfileSwitchProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusIsdnsgProfileSwitchProfile_Type.__name__ = "DisplayString"
_SonusIsdnsgProfileSwitchProfile_Object = MibTableColumn
sonusIsdnsgProfileSwitchProfile = _SonusIsdnsgProfileSwitchProfile_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 3, 2, 1, 8),
    _SonusIsdnsgProfileSwitchProfile_Type()
)
sonusIsdnsgProfileSwitchProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgProfileSwitchProfile.setStatus("obsolete")


class _SonusIsdnsgProfileMode_Type(SonusServiceState):
    """Custom type sonusIsdnsgProfileMode based on SonusServiceState"""


_SonusIsdnsgProfileMode_Object = MibTableColumn
sonusIsdnsgProfileMode = _SonusIsdnsgProfileMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 3, 2, 1, 9),
    _SonusIsdnsgProfileMode_Type()
)
sonusIsdnsgProfileMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgProfileMode.setStatus("obsolete")


class _SonusIsdnsgProfileAdminState_Type(SonusAdminState):
    """Custom type sonusIsdnsgProfileAdminState based on SonusAdminState"""


_SonusIsdnsgProfileAdminState_Object = MibTableColumn
sonusIsdnsgProfileAdminState = _SonusIsdnsgProfileAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 3, 2, 1, 10),
    _SonusIsdnsgProfileAdminState_Type()
)
sonusIsdnsgProfileAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgProfileAdminState.setStatus("current")
_SonusIsdnsgProfileRowStatus_Type = RowStatus
_SonusIsdnsgProfileRowStatus_Object = MibTableColumn
sonusIsdnsgProfileRowStatus = _SonusIsdnsgProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 3, 2, 1, 11),
    _SonusIsdnsgProfileRowStatus_Type()
)
sonusIsdnsgProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgProfileRowStatus.setStatus("current")


class _SonusIsdnsgProfileDefaultDirectoryNumber_Type(DisplayString):
    """Custom type sonusIsdnsgProfileDefaultDirectoryNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SonusIsdnsgProfileDefaultDirectoryNumber_Type.__name__ = "DisplayString"
_SonusIsdnsgProfileDefaultDirectoryNumber_Object = MibTableColumn
sonusIsdnsgProfileDefaultDirectoryNumber = _SonusIsdnsgProfileDefaultDirectoryNumber_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 3, 2, 1, 12),
    _SonusIsdnsgProfileDefaultDirectoryNumber_Type()
)
sonusIsdnsgProfileDefaultDirectoryNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgProfileDefaultDirectoryNumber.setStatus("current")


class _SonusIsdnsgProfileCallingPartyNumberProvision_Type(Integer32):
    """Custom type sonusIsdnsgProfileCallingPartyNumberProvision based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("necessary", 1),
          ("notNecessary", 2))
    )


_SonusIsdnsgProfileCallingPartyNumberProvision_Type.__name__ = "Integer32"
_SonusIsdnsgProfileCallingPartyNumberProvision_Object = MibTableColumn
sonusIsdnsgProfileCallingPartyNumberProvision = _SonusIsdnsgProfileCallingPartyNumberProvision_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 3, 2, 1, 13),
    _SonusIsdnsgProfileCallingPartyNumberProvision_Type()
)
sonusIsdnsgProfileCallingPartyNumberProvision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgProfileCallingPartyNumberProvision.setStatus("current")


class _SonusIsdnsgProfileCallingPartyNumberDiscard_Type(Integer32):
    """Custom type sonusIsdnsgProfileCallingPartyNumberDiscard based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SonusIsdnsgProfileCallingPartyNumberDiscard_Type.__name__ = "Integer32"
_SonusIsdnsgProfileCallingPartyNumberDiscard_Object = MibTableColumn
sonusIsdnsgProfileCallingPartyNumberDiscard = _SonusIsdnsgProfileCallingPartyNumberDiscard_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 3, 2, 1, 14),
    _SonusIsdnsgProfileCallingPartyNumberDiscard_Type()
)
sonusIsdnsgProfileCallingPartyNumberDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgProfileCallingPartyNumberDiscard.setStatus("current")


class _SonusIsdnsgProfileCallingPartyNumberDelivery_Type(Integer32):
    """Custom type sonusIsdnsgProfileCallingPartyNumberDelivery based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SonusIsdnsgProfileCallingPartyNumberDelivery_Type.__name__ = "Integer32"
_SonusIsdnsgProfileCallingPartyNumberDelivery_Object = MibTableColumn
sonusIsdnsgProfileCallingPartyNumberDelivery = _SonusIsdnsgProfileCallingPartyNumberDelivery_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 3, 2, 1, 15),
    _SonusIsdnsgProfileCallingPartyNumberDelivery_Type()
)
sonusIsdnsgProfileCallingPartyNumberDelivery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgProfileCallingPartyNumberDelivery.setStatus("current")


class _SonusIsdnsgProfileCallingPartySubAddressTransfer_Type(Integer32):
    """Custom type sonusIsdnsgProfileCallingPartySubAddressTransfer based on Integer32"""
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
        *(("conditional", 3),
          ("no", 2),
          ("yes", 1))
    )


_SonusIsdnsgProfileCallingPartySubAddressTransfer_Type.__name__ = "Integer32"
_SonusIsdnsgProfileCallingPartySubAddressTransfer_Object = MibTableColumn
sonusIsdnsgProfileCallingPartySubAddressTransfer = _SonusIsdnsgProfileCallingPartySubAddressTransfer_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 3, 2, 1, 16),
    _SonusIsdnsgProfileCallingPartySubAddressTransfer_Type()
)
sonusIsdnsgProfileCallingPartySubAddressTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgProfileCallingPartySubAddressTransfer.setStatus("current")


class _SonusIsdnsgProfileCallingPartySubAddressDelivery_Type(Integer32):
    """Custom type sonusIsdnsgProfileCallingPartySubAddressDelivery based on Integer32"""
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
        *(("conditional", 3),
          ("no", 2),
          ("yes", 1))
    )


_SonusIsdnsgProfileCallingPartySubAddressDelivery_Type.__name__ = "Integer32"
_SonusIsdnsgProfileCallingPartySubAddressDelivery_Object = MibTableColumn
sonusIsdnsgProfileCallingPartySubAddressDelivery = _SonusIsdnsgProfileCallingPartySubAddressDelivery_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 3, 2, 1, 17),
    _SonusIsdnsgProfileCallingPartySubAddressDelivery_Type()
)
sonusIsdnsgProfileCallingPartySubAddressDelivery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgProfileCallingPartySubAddressDelivery.setStatus("current")


class _SonusIsdnsgProfileCallingPartyNumberPresentation_Type(Integer32):
    """Custom type sonusIsdnsgProfileCallingPartyNumberPresentation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SonusIsdnsgProfileCallingPartyNumberPresentation_Type.__name__ = "Integer32"
_SonusIsdnsgProfileCallingPartyNumberPresentation_Object = MibTableColumn
sonusIsdnsgProfileCallingPartyNumberPresentation = _SonusIsdnsgProfileCallingPartyNumberPresentation_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 3, 2, 1, 18),
    _SonusIsdnsgProfileCallingPartyNumberPresentation_Type()
)
sonusIsdnsgProfileCallingPartyNumberPresentation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgProfileCallingPartyNumberPresentation.setStatus("current")
_SonusIsdnsgInterfaceTable_Object = MibTable
sonusIsdnsgInterfaceTable = _SonusIsdnsgInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 4)
)
if mibBuilder.loadTexts:
    sonusIsdnsgInterfaceTable.setStatus("current")
_SonusIsdnsgInterfaceEntry_Object = MibTableRow
sonusIsdnsgInterfaceEntry = _SonusIsdnsgInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 4, 1)
)
sonusIsdnsgInterfaceEntry.setIndexNames(
    (0, "SONUS-ISDN-SERVICE-GROUP-MIB", "sonusIsdnsgInterfaceServiceListIndex"),
    (0, "SONUS-ISDN-SERVICE-GROUP-MIB", "sonusIsdnsgInterfaceIdentifier"),
)
if mibBuilder.loadTexts:
    sonusIsdnsgInterfaceEntry.setStatus("current")
_SonusIsdnsgInterfaceServiceListIndex_Type = Integer32
_SonusIsdnsgInterfaceServiceListIndex_Object = MibTableColumn
sonusIsdnsgInterfaceServiceListIndex = _SonusIsdnsgInterfaceServiceListIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 4, 1, 1),
    _SonusIsdnsgInterfaceServiceListIndex_Type()
)
sonusIsdnsgInterfaceServiceListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgInterfaceServiceListIndex.setStatus("current")


class _SonusIsdnsgInterfaceIdentifier_Type(Integer32):
    """Custom type sonusIsdnsgInterfaceIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgInterfaceIdentifier_Type.__name__ = "Integer32"
_SonusIsdnsgInterfaceIdentifier_Object = MibTableColumn
sonusIsdnsgInterfaceIdentifier = _SonusIsdnsgInterfaceIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 4, 1, 2),
    _SonusIsdnsgInterfaceIdentifier_Type()
)
sonusIsdnsgInterfaceIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgInterfaceIdentifier.setStatus("current")
_SonusIsdnsgInterfacePortName_Type = SonusNameReference
_SonusIsdnsgInterfacePortName_Object = MibTableColumn
sonusIsdnsgInterfacePortName = _SonusIsdnsgInterfacePortName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 4, 1, 3),
    _SonusIsdnsgInterfacePortName_Type()
)
sonusIsdnsgInterfacePortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgInterfacePortName.setStatus("current")


class _SonusIsdnsgInterfaceOperation_Type(Integer32):
    """Custom type sonusIsdnsgInterfaceOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restart", 1)
    )


_SonusIsdnsgInterfaceOperation_Type.__name__ = "Integer32"
_SonusIsdnsgInterfaceOperation_Object = MibTableColumn
sonusIsdnsgInterfaceOperation = _SonusIsdnsgInterfaceOperation_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 4, 1, 4),
    _SonusIsdnsgInterfaceOperation_Type()
)
sonusIsdnsgInterfaceOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgInterfaceOperation.setStatus("current")


class _SonusIsdnsgInterfaceAdminState_Type(SonusAdminState):
    """Custom type sonusIsdnsgInterfaceAdminState based on SonusAdminState"""


_SonusIsdnsgInterfaceAdminState_Object = MibTableColumn
sonusIsdnsgInterfaceAdminState = _SonusIsdnsgInterfaceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 4, 1, 5),
    _SonusIsdnsgInterfaceAdminState_Type()
)
sonusIsdnsgInterfaceAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgInterfaceAdminState.setStatus("current")
_SonusIsdnsgInterfaceRowStatus_Type = RowStatus
_SonusIsdnsgInterfaceRowStatus_Object = MibTableColumn
sonusIsdnsgInterfaceRowStatus = _SonusIsdnsgInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 4, 1, 6),
    _SonusIsdnsgInterfaceRowStatus_Type()
)
sonusIsdnsgInterfaceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgInterfaceRowStatus.setStatus("current")
_SonusIsdnsgBchannelTable_Object = MibTable
sonusIsdnsgBchannelTable = _SonusIsdnsgBchannelTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 5)
)
if mibBuilder.loadTexts:
    sonusIsdnsgBchannelTable.setStatus("current")
_SonusIsdnsgBchannelEntry_Object = MibTableRow
sonusIsdnsgBchannelEntry = _SonusIsdnsgBchannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 5, 1)
)
sonusIsdnsgBchannelEntry.setIndexNames(
    (0, "SONUS-ISDN-SERVICE-GROUP-MIB", "sonusIsdnsgBchannelServiceListIndex"),
    (0, "SONUS-ISDN-SERVICE-GROUP-MIB", "sonusIsdnsgBchannelInterfaceIdentifier"),
    (0, "SONUS-ISDN-SERVICE-GROUP-MIB", "sonusIsdnsgBchannelNumber"),
)
if mibBuilder.loadTexts:
    sonusIsdnsgBchannelEntry.setStatus("current")
_SonusIsdnsgBchannelServiceListIndex_Type = Integer32
_SonusIsdnsgBchannelServiceListIndex_Object = MibTableColumn
sonusIsdnsgBchannelServiceListIndex = _SonusIsdnsgBchannelServiceListIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 5, 1, 1),
    _SonusIsdnsgBchannelServiceListIndex_Type()
)
sonusIsdnsgBchannelServiceListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgBchannelServiceListIndex.setStatus("current")


class _SonusIsdnsgBchannelInterfaceIdentifier_Type(Integer32):
    """Custom type sonusIsdnsgBchannelInterfaceIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgBchannelInterfaceIdentifier_Type.__name__ = "Integer32"
_SonusIsdnsgBchannelInterfaceIdentifier_Object = MibTableColumn
sonusIsdnsgBchannelInterfaceIdentifier = _SonusIsdnsgBchannelInterfaceIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 5, 1, 2),
    _SonusIsdnsgBchannelInterfaceIdentifier_Type()
)
sonusIsdnsgBchannelInterfaceIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgBchannelInterfaceIdentifier.setStatus("current")


class _SonusIsdnsgBchannelNumber_Type(Integer32):
    """Custom type sonusIsdnsgBchannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SonusIsdnsgBchannelNumber_Type.__name__ = "Integer32"
_SonusIsdnsgBchannelNumber_Object = MibTableColumn
sonusIsdnsgBchannelNumber = _SonusIsdnsgBchannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 5, 1, 3),
    _SonusIsdnsgBchannelNumber_Type()
)
sonusIsdnsgBchannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgBchannelNumber.setStatus("current")
_SonusIsdnsgBchannelCircuitProfileName_Type = SonusNameReference
_SonusIsdnsgBchannelCircuitProfileName_Object = MibTableColumn
sonusIsdnsgBchannelCircuitProfileName = _SonusIsdnsgBchannelCircuitProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 5, 1, 4),
    _SonusIsdnsgBchannelCircuitProfileName_Type()
)
sonusIsdnsgBchannelCircuitProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgBchannelCircuitProfileName.setStatus("current")


class _SonusIsdnsgBchannelDirection_Type(Integer32):
    """Custom type sonusIsdnsgBchannelDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneWayIn", 2),
          ("oneWayOut", 3),
          ("twoWay", 1))
    )


_SonusIsdnsgBchannelDirection_Type.__name__ = "Integer32"
_SonusIsdnsgBchannelDirection_Object = MibTableColumn
sonusIsdnsgBchannelDirection = _SonusIsdnsgBchannelDirection_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 5, 1, 5),
    _SonusIsdnsgBchannelDirection_Type()
)
sonusIsdnsgBchannelDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgBchannelDirection.setStatus("current")


class _SonusIsdnsgBchannelOperation_Type(Integer32):
    """Custom type sonusIsdnsgBchannelOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restart", 1)
    )


_SonusIsdnsgBchannelOperation_Type.__name__ = "Integer32"
_SonusIsdnsgBchannelOperation_Object = MibTableColumn
sonusIsdnsgBchannelOperation = _SonusIsdnsgBchannelOperation_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 5, 1, 6),
    _SonusIsdnsgBchannelOperation_Type()
)
sonusIsdnsgBchannelOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgBchannelOperation.setStatus("current")


class _SonusIsdnsgBchannelMode_Type(Integer32):
    """Custom type sonusIsdnsgBchannelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inService", 3),
          ("maintenance", 2),
          ("outOfService", 1))
    )


_SonusIsdnsgBchannelMode_Type.__name__ = "Integer32"
_SonusIsdnsgBchannelMode_Object = MibTableColumn
sonusIsdnsgBchannelMode = _SonusIsdnsgBchannelMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 5, 1, 7),
    _SonusIsdnsgBchannelMode_Type()
)
sonusIsdnsgBchannelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgBchannelMode.setStatus("current")


class _SonusIsdnsgBchannelAction_Type(Integer32):
    """Custom type sonusIsdnsgBchannelAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dryUp", 1),
          ("force", 2))
    )


_SonusIsdnsgBchannelAction_Type.__name__ = "Integer32"
_SonusIsdnsgBchannelAction_Object = MibTableColumn
sonusIsdnsgBchannelAction = _SonusIsdnsgBchannelAction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 5, 1, 8),
    _SonusIsdnsgBchannelAction_Type()
)
sonusIsdnsgBchannelAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgBchannelAction.setStatus("current")


class _SonusIsdnsgBchannelTimeout_Type(Integer32):
    """Custom type sonusIsdnsgBchannelTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_SonusIsdnsgBchannelTimeout_Type.__name__ = "Integer32"
_SonusIsdnsgBchannelTimeout_Object = MibTableColumn
sonusIsdnsgBchannelTimeout = _SonusIsdnsgBchannelTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 5, 1, 9),
    _SonusIsdnsgBchannelTimeout_Type()
)
sonusIsdnsgBchannelTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgBchannelTimeout.setStatus("current")
_SonusIsdnsgBchannelAdminState_Type = SonusAdminState
_SonusIsdnsgBchannelAdminState_Object = MibTableColumn
sonusIsdnsgBchannelAdminState = _SonusIsdnsgBchannelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 5, 1, 10),
    _SonusIsdnsgBchannelAdminState_Type()
)
sonusIsdnsgBchannelAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgBchannelAdminState.setStatus("current")
_SonusIsdnsgBchannelStatTable_Object = MibTable
sonusIsdnsgBchannelStatTable = _SonusIsdnsgBchannelStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 6)
)
if mibBuilder.loadTexts:
    sonusIsdnsgBchannelStatTable.setStatus("current")
_SonusIsdnsgBchannelStatEntry_Object = MibTableRow
sonusIsdnsgBchannelStatEntry = _SonusIsdnsgBchannelStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 6, 1)
)
sonusIsdnsgBchannelStatEntry.setIndexNames(
    (0, "SONUS-ISDN-SERVICE-GROUP-MIB", "sonusIsdnsgBchannelStatServiceListIndex"),
    (0, "SONUS-ISDN-SERVICE-GROUP-MIB", "sonusIsdnsgBchannelStatInterfaceIdentifier"),
    (0, "SONUS-ISDN-SERVICE-GROUP-MIB", "sonusIsdnsgBchannelStatNumber"),
)
if mibBuilder.loadTexts:
    sonusIsdnsgBchannelStatEntry.setStatus("current")
_SonusIsdnsgBchannelStatServiceListIndex_Type = Integer32
_SonusIsdnsgBchannelStatServiceListIndex_Object = MibTableColumn
sonusIsdnsgBchannelStatServiceListIndex = _SonusIsdnsgBchannelStatServiceListIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 6, 1, 1),
    _SonusIsdnsgBchannelStatServiceListIndex_Type()
)
sonusIsdnsgBchannelStatServiceListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgBchannelStatServiceListIndex.setStatus("current")


class _SonusIsdnsgBchannelStatInterfaceIdentifier_Type(Integer32):
    """Custom type sonusIsdnsgBchannelStatInterfaceIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgBchannelStatInterfaceIdentifier_Type.__name__ = "Integer32"
_SonusIsdnsgBchannelStatInterfaceIdentifier_Object = MibTableColumn
sonusIsdnsgBchannelStatInterfaceIdentifier = _SonusIsdnsgBchannelStatInterfaceIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 6, 1, 2),
    _SonusIsdnsgBchannelStatInterfaceIdentifier_Type()
)
sonusIsdnsgBchannelStatInterfaceIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgBchannelStatInterfaceIdentifier.setStatus("current")


class _SonusIsdnsgBchannelStatNumber_Type(Integer32):
    """Custom type sonusIsdnsgBchannelStatNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SonusIsdnsgBchannelStatNumber_Type.__name__ = "Integer32"
_SonusIsdnsgBchannelStatNumber_Object = MibTableColumn
sonusIsdnsgBchannelStatNumber = _SonusIsdnsgBchannelStatNumber_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 6, 1, 3),
    _SonusIsdnsgBchannelStatNumber_Type()
)
sonusIsdnsgBchannelStatNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgBchannelStatNumber.setStatus("current")


class _SonusIsdnsgBchannelStatUsage_Type(Integer32):
    """Custom type sonusIsdnsgBchannelStatUsage based on Integer32"""
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
        *(("idle", 2),
          ("inBusy", 3),
          ("outBusy", 4),
          ("transientRelease", 6),
          ("transientSetup", 5),
          ("unequipped", 1))
    )


_SonusIsdnsgBchannelStatUsage_Type.__name__ = "Integer32"
_SonusIsdnsgBchannelStatUsage_Object = MibTableColumn
sonusIsdnsgBchannelStatUsage = _SonusIsdnsgBchannelStatUsage_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 6, 1, 4),
    _SonusIsdnsgBchannelStatUsage_Type()
)
sonusIsdnsgBchannelStatUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgBchannelStatUsage.setStatus("current")


class _SonusIsdnsgBchannelStatLocalMaint_Type(Integer32):
    """Custom type sonusIsdnsgBchannelStatLocalMaint based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("dryup", 7),
          ("inService", 1),
          ("maintenance", 2),
          ("notAvailable", 8),
          ("outOfService", 3),
          ("transientInService", 4),
          ("transientMaintenance", 5),
          ("transientOutOfService", 6))
    )


_SonusIsdnsgBchannelStatLocalMaint_Type.__name__ = "Integer32"
_SonusIsdnsgBchannelStatLocalMaint_Object = MibTableColumn
sonusIsdnsgBchannelStatLocalMaint = _SonusIsdnsgBchannelStatLocalMaint_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 6, 1, 5),
    _SonusIsdnsgBchannelStatLocalMaint_Type()
)
sonusIsdnsgBchannelStatLocalMaint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgBchannelStatLocalMaint.setStatus("current")


class _SonusIsdnsgBchannelStatLocalHw_Type(Integer32):
    """Custom type sonusIsdnsgBchannelStatLocalHw based on Integer32"""
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
        *(("inService", 1),
          ("notAvailable", 5),
          ("outOfService", 2),
          ("transientInService", 3),
          ("transientOutOfService", 4))
    )


_SonusIsdnsgBchannelStatLocalHw_Type.__name__ = "Integer32"
_SonusIsdnsgBchannelStatLocalHw_Object = MibTableColumn
sonusIsdnsgBchannelStatLocalHw = _SonusIsdnsgBchannelStatLocalHw_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 6, 1, 6),
    _SonusIsdnsgBchannelStatLocalHw_Type()
)
sonusIsdnsgBchannelStatLocalHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgBchannelStatLocalHw.setStatus("current")


class _SonusIsdnsgBchannelStatRemoteMaint_Type(Integer32):
    """Custom type sonusIsdnsgBchannelStatRemoteMaint based on Integer32"""
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
        *(("autoOutOfService", 10),
          ("inService", 1),
          ("maintenance", 2),
          ("notAvailable", 7),
          ("outOfService", 3),
          ("restartError", 9),
          ("restarting", 8),
          ("transientInService", 4),
          ("transientMaintenance", 5),
          ("transientOutOfService", 6))
    )


_SonusIsdnsgBchannelStatRemoteMaint_Type.__name__ = "Integer32"
_SonusIsdnsgBchannelStatRemoteMaint_Object = MibTableColumn
sonusIsdnsgBchannelStatRemoteMaint = _SonusIsdnsgBchannelStatRemoteMaint_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 6, 1, 7),
    _SonusIsdnsgBchannelStatRemoteMaint_Type()
)
sonusIsdnsgBchannelStatRemoteMaint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgBchannelStatRemoteMaint.setStatus("current")
_SonusIsdnsgSwitchProfile_ObjectIdentity = ObjectIdentity
sonusIsdnsgSwitchProfile = _SonusIsdnsgSwitchProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7)
)
_SonusIsdnsgSwitchProfileNextIndex_Type = Integer32
_SonusIsdnsgSwitchProfileNextIndex_Object = MibScalar
sonusIsdnsgSwitchProfileNextIndex = _SonusIsdnsgSwitchProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7, 1),
    _SonusIsdnsgSwitchProfileNextIndex_Type()
)
sonusIsdnsgSwitchProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgSwitchProfileNextIndex.setStatus("current")
_SonusIsdnsgSwitchProfileTable_Object = MibTable
sonusIsdnsgSwitchProfileTable = _SonusIsdnsgSwitchProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7, 2)
)
if mibBuilder.loadTexts:
    sonusIsdnsgSwitchProfileTable.setStatus("current")
_SonusIsdnsgSwitchProfileEntry_Object = MibTableRow
sonusIsdnsgSwitchProfileEntry = _SonusIsdnsgSwitchProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7, 2, 1)
)
sonusIsdnsgSwitchProfileEntry.setIndexNames(
    (0, "SONUS-ISDN-SERVICE-GROUP-MIB", "sonusIsdnsgSwitchProfileListIndex"),
)
if mibBuilder.loadTexts:
    sonusIsdnsgSwitchProfileEntry.setStatus("current")


class _SonusIsdnsgSwitchProfileListIndex_Type(Integer32):
    """Custom type sonusIsdnsgSwitchProfileListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SonusIsdnsgSwitchProfileListIndex_Type.__name__ = "Integer32"
_SonusIsdnsgSwitchProfileListIndex_Object = MibTableColumn
sonusIsdnsgSwitchProfileListIndex = _SonusIsdnsgSwitchProfileListIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7, 2, 1, 1),
    _SonusIsdnsgSwitchProfileListIndex_Type()
)
sonusIsdnsgSwitchProfileListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnsgSwitchProfileListIndex.setStatus("current")
_SonusIsdnsgSwitchProfileName_Type = SonusName
_SonusIsdnsgSwitchProfileName_Object = MibTableColumn
sonusIsdnsgSwitchProfileName = _SonusIsdnsgSwitchProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7, 2, 1, 2),
    _SonusIsdnsgSwitchProfileName_Type()
)
sonusIsdnsgSwitchProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgSwitchProfileName.setStatus("current")


class _SonusIsdnsgSwitchProfileSwitchSide_Type(Integer32):
    """Custom type sonusIsdnsgSwitchProfileSwitchSide based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 1),
          ("user", 2))
    )


_SonusIsdnsgSwitchProfileSwitchSide_Type.__name__ = "Integer32"
_SonusIsdnsgSwitchProfileSwitchSide_Object = MibTableColumn
sonusIsdnsgSwitchProfileSwitchSide = _SonusIsdnsgSwitchProfileSwitchSide_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7, 2, 1, 3),
    _SonusIsdnsgSwitchProfileSwitchSide_Type()
)
sonusIsdnsgSwitchProfileSwitchSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgSwitchProfileSwitchSide.setStatus("current")


class _SonusIsdnsgSwitchProfileSwitchType_Type(Integer32):
    """Custom type sonusIsdnsgSwitchProfileSwitchType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("dms100", 3),
          ("dms250", 2),
          ("euroIsdn", 6),
          ("ins1500", 7),
          ("lucent4ESS", 5),
          ("lucent5ESS", 4),
          ("ni2", 1))
    )


_SonusIsdnsgSwitchProfileSwitchType_Type.__name__ = "Integer32"
_SonusIsdnsgSwitchProfileSwitchType_Object = MibTableColumn
sonusIsdnsgSwitchProfileSwitchType = _SonusIsdnsgSwitchProfileSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7, 2, 1, 4),
    _SonusIsdnsgSwitchProfileSwitchType_Type()
)
sonusIsdnsgSwitchProfileSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgSwitchProfileSwitchType.setStatus("current")


class _SonusIsdnsgSwitchProfileBchannelAvailabilitySignaling_Type(Integer32):
    """Custom type sonusIsdnsgSwitchProfileBchannelAvailabilitySignaling based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SonusIsdnsgSwitchProfileBchannelAvailabilitySignaling_Type.__name__ = "Integer32"
_SonusIsdnsgSwitchProfileBchannelAvailabilitySignaling_Object = MibTableColumn
sonusIsdnsgSwitchProfileBchannelAvailabilitySignaling = _SonusIsdnsgSwitchProfileBchannelAvailabilitySignaling_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7, 2, 1, 5),
    _SonusIsdnsgSwitchProfileBchannelAvailabilitySignaling_Type()
)
sonusIsdnsgSwitchProfileBchannelAvailabilitySignaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgSwitchProfileBchannelAvailabilitySignaling.setStatus("current")


class _SonusIsdnsgSwitchProfileT302_Type(Integer32):
    """Custom type sonusIsdnsgSwitchProfileT302 based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgSwitchProfileT302_Type.__name__ = "Integer32"
_SonusIsdnsgSwitchProfileT302_Object = MibTableColumn
sonusIsdnsgSwitchProfileT302 = _SonusIsdnsgSwitchProfileT302_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7, 2, 1, 6),
    _SonusIsdnsgSwitchProfileT302_Type()
)
sonusIsdnsgSwitchProfileT302.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgSwitchProfileT302.setStatus("current")


class _SonusIsdnsgSwitchProfileT303_Type(Integer32):
    """Custom type sonusIsdnsgSwitchProfileT303 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgSwitchProfileT303_Type.__name__ = "Integer32"
_SonusIsdnsgSwitchProfileT303_Object = MibTableColumn
sonusIsdnsgSwitchProfileT303 = _SonusIsdnsgSwitchProfileT303_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7, 2, 1, 7),
    _SonusIsdnsgSwitchProfileT303_Type()
)
sonusIsdnsgSwitchProfileT303.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgSwitchProfileT303.setStatus("current")


class _SonusIsdnsgSwitchProfileT304_Type(Integer32):
    """Custom type sonusIsdnsgSwitchProfileT304 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgSwitchProfileT304_Type.__name__ = "Integer32"
_SonusIsdnsgSwitchProfileT304_Object = MibTableColumn
sonusIsdnsgSwitchProfileT304 = _SonusIsdnsgSwitchProfileT304_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7, 2, 1, 8),
    _SonusIsdnsgSwitchProfileT304_Type()
)
sonusIsdnsgSwitchProfileT304.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgSwitchProfileT304.setStatus("current")


class _SonusIsdnsgSwitchProfileT305_Type(Integer32):
    """Custom type sonusIsdnsgSwitchProfileT305 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgSwitchProfileT305_Type.__name__ = "Integer32"
_SonusIsdnsgSwitchProfileT305_Object = MibTableColumn
sonusIsdnsgSwitchProfileT305 = _SonusIsdnsgSwitchProfileT305_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7, 2, 1, 9),
    _SonusIsdnsgSwitchProfileT305_Type()
)
sonusIsdnsgSwitchProfileT305.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgSwitchProfileT305.setStatus("current")


class _SonusIsdnsgSwitchProfileT306_Type(Integer32):
    """Custom type sonusIsdnsgSwitchProfileT306 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgSwitchProfileT306_Type.__name__ = "Integer32"
_SonusIsdnsgSwitchProfileT306_Object = MibTableColumn
sonusIsdnsgSwitchProfileT306 = _SonusIsdnsgSwitchProfileT306_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7, 2, 1, 10),
    _SonusIsdnsgSwitchProfileT306_Type()
)
sonusIsdnsgSwitchProfileT306.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgSwitchProfileT306.setStatus("current")


class _SonusIsdnsgSwitchProfileT308_Type(Integer32):
    """Custom type sonusIsdnsgSwitchProfileT308 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgSwitchProfileT308_Type.__name__ = "Integer32"
_SonusIsdnsgSwitchProfileT308_Object = MibTableColumn
sonusIsdnsgSwitchProfileT308 = _SonusIsdnsgSwitchProfileT308_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7, 2, 1, 11),
    _SonusIsdnsgSwitchProfileT308_Type()
)
sonusIsdnsgSwitchProfileT308.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgSwitchProfileT308.setStatus("current")


class _SonusIsdnsgSwitchProfileT309_Type(Integer32):
    """Custom type sonusIsdnsgSwitchProfileT309 based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgSwitchProfileT309_Type.__name__ = "Integer32"
_SonusIsdnsgSwitchProfileT309_Object = MibTableColumn
sonusIsdnsgSwitchProfileT309 = _SonusIsdnsgSwitchProfileT309_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7, 2, 1, 12),
    _SonusIsdnsgSwitchProfileT309_Type()
)
sonusIsdnsgSwitchProfileT309.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgSwitchProfileT309.setStatus("current")


class _SonusIsdnsgSwitchProfileT310_Type(Integer32):
    """Custom type sonusIsdnsgSwitchProfileT310 based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgSwitchProfileT310_Type.__name__ = "Integer32"
_SonusIsdnsgSwitchProfileT310_Object = MibTableColumn
sonusIsdnsgSwitchProfileT310 = _SonusIsdnsgSwitchProfileT310_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7, 2, 1, 13),
    _SonusIsdnsgSwitchProfileT310_Type()
)
sonusIsdnsgSwitchProfileT310.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgSwitchProfileT310.setStatus("current")


class _SonusIsdnsgSwitchProfileT312_Type(Integer32):
    """Custom type sonusIsdnsgSwitchProfileT312 based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgSwitchProfileT312_Type.__name__ = "Integer32"
_SonusIsdnsgSwitchProfileT312_Object = MibTableColumn
sonusIsdnsgSwitchProfileT312 = _SonusIsdnsgSwitchProfileT312_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7, 2, 1, 14),
    _SonusIsdnsgSwitchProfileT312_Type()
)
sonusIsdnsgSwitchProfileT312.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgSwitchProfileT312.setStatus("current")


class _SonusIsdnsgSwitchProfileT313_Type(Integer32):
    """Custom type sonusIsdnsgSwitchProfileT313 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgSwitchProfileT313_Type.__name__ = "Integer32"
_SonusIsdnsgSwitchProfileT313_Object = MibTableColumn
sonusIsdnsgSwitchProfileT313 = _SonusIsdnsgSwitchProfileT313_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7, 2, 1, 15),
    _SonusIsdnsgSwitchProfileT313_Type()
)
sonusIsdnsgSwitchProfileT313.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgSwitchProfileT313.setStatus("current")


class _SonusIsdnsgSwitchProfileT314_Type(Integer32):
    """Custom type sonusIsdnsgSwitchProfileT314 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgSwitchProfileT314_Type.__name__ = "Integer32"
_SonusIsdnsgSwitchProfileT314_Object = MibTableColumn
sonusIsdnsgSwitchProfileT314 = _SonusIsdnsgSwitchProfileT314_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7, 2, 1, 16),
    _SonusIsdnsgSwitchProfileT314_Type()
)
sonusIsdnsgSwitchProfileT314.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgSwitchProfileT314.setStatus("current")


class _SonusIsdnsgSwitchProfileT318_Type(Integer32):
    """Custom type sonusIsdnsgSwitchProfileT318 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgSwitchProfileT318_Type.__name__ = "Integer32"
_SonusIsdnsgSwitchProfileT318_Object = MibTableColumn
sonusIsdnsgSwitchProfileT318 = _SonusIsdnsgSwitchProfileT318_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7, 2, 1, 17),
    _SonusIsdnsgSwitchProfileT318_Type()
)
sonusIsdnsgSwitchProfileT318.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgSwitchProfileT318.setStatus("current")


class _SonusIsdnsgSwitchProfileT319_Type(Integer32):
    """Custom type sonusIsdnsgSwitchProfileT319 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgSwitchProfileT319_Type.__name__ = "Integer32"
_SonusIsdnsgSwitchProfileT319_Object = MibTableColumn
sonusIsdnsgSwitchProfileT319 = _SonusIsdnsgSwitchProfileT319_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7, 2, 1, 18),
    _SonusIsdnsgSwitchProfileT319_Type()
)
sonusIsdnsgSwitchProfileT319.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgSwitchProfileT319.setStatus("current")


class _SonusIsdnsgSwitchProfileT322_Type(Integer32):
    """Custom type sonusIsdnsgSwitchProfileT322 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnsgSwitchProfileT322_Type.__name__ = "Integer32"
_SonusIsdnsgSwitchProfileT322_Object = MibTableColumn
sonusIsdnsgSwitchProfileT322 = _SonusIsdnsgSwitchProfileT322_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7, 2, 1, 19),
    _SonusIsdnsgSwitchProfileT322_Type()
)
sonusIsdnsgSwitchProfileT322.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgSwitchProfileT322.setStatus("current")


class _SonusIsdnsgSwitchProfileK_Type(Integer32):
    """Custom type sonusIsdnsgSwitchProfileK based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_SonusIsdnsgSwitchProfileK_Type.__name__ = "Integer32"
_SonusIsdnsgSwitchProfileK_Object = MibTableColumn
sonusIsdnsgSwitchProfileK = _SonusIsdnsgSwitchProfileK_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7, 2, 1, 20),
    _SonusIsdnsgSwitchProfileK_Type()
)
sonusIsdnsgSwitchProfileK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgSwitchProfileK.setStatus("current")


class _SonusIsdnsgSwitchProfileT200_Type(Integer32):
    """Custom type sonusIsdnsgSwitchProfileT200 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SonusIsdnsgSwitchProfileT200_Type.__name__ = "Integer32"
_SonusIsdnsgSwitchProfileT200_Object = MibTableColumn
sonusIsdnsgSwitchProfileT200 = _SonusIsdnsgSwitchProfileT200_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7, 2, 1, 21),
    _SonusIsdnsgSwitchProfileT200_Type()
)
sonusIsdnsgSwitchProfileT200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgSwitchProfileT200.setStatus("current")


class _SonusIsdnsgSwitchProfileT203_Type(Integer32):
    """Custom type sonusIsdnsgSwitchProfileT203 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SonusIsdnsgSwitchProfileT203_Type.__name__ = "Integer32"
_SonusIsdnsgSwitchProfileT203_Object = MibTableColumn
sonusIsdnsgSwitchProfileT203 = _SonusIsdnsgSwitchProfileT203_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7, 2, 1, 22),
    _SonusIsdnsgSwitchProfileT203_Type()
)
sonusIsdnsgSwitchProfileT203.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgSwitchProfileT203.setStatus("current")


class _SonusIsdnsgSwitchProfileN200_Type(Integer32):
    """Custom type sonusIsdnsgSwitchProfileN200 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SonusIsdnsgSwitchProfileN200_Type.__name__ = "Integer32"
_SonusIsdnsgSwitchProfileN200_Object = MibTableColumn
sonusIsdnsgSwitchProfileN200 = _SonusIsdnsgSwitchProfileN200_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7, 2, 1, 23),
    _SonusIsdnsgSwitchProfileN200_Type()
)
sonusIsdnsgSwitchProfileN200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgSwitchProfileN200.setStatus("current")


class _SonusIsdnsgSwitchProfileN201_Type(Integer32):
    """Custom type sonusIsdnsgSwitchProfileN201 based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 260),
    )


_SonusIsdnsgSwitchProfileN201_Type.__name__ = "Integer32"
_SonusIsdnsgSwitchProfileN201_Object = MibTableColumn
sonusIsdnsgSwitchProfileN201 = _SonusIsdnsgSwitchProfileN201_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7, 2, 1, 24),
    _SonusIsdnsgSwitchProfileN201_Type()
)
sonusIsdnsgSwitchProfileN201.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgSwitchProfileN201.setStatus("current")


class _SonusIsdnsgSwitchProfileAdminState_Type(SonusAdminState):
    """Custom type sonusIsdnsgSwitchProfileAdminState based on SonusAdminState"""


_SonusIsdnsgSwitchProfileAdminState_Object = MibTableColumn
sonusIsdnsgSwitchProfileAdminState = _SonusIsdnsgSwitchProfileAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7, 2, 1, 25),
    _SonusIsdnsgSwitchProfileAdminState_Type()
)
sonusIsdnsgSwitchProfileAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgSwitchProfileAdminState.setStatus("current")
_SonusIsdnsgSwitchProfileRowStatus_Type = RowStatus
_SonusIsdnsgSwitchProfileRowStatus_Object = MibTableColumn
sonusIsdnsgSwitchProfileRowStatus = _SonusIsdnsgSwitchProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7, 2, 1, 26),
    _SonusIsdnsgSwitchProfileRowStatus_Type()
)
sonusIsdnsgSwitchProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgSwitchProfileRowStatus.setStatus("current")


class _SonusIsdnsgSwitchProfileBchannelInitialRestart_Type(Integer32):
    """Custom type sonusIsdnsgSwitchProfileBchannelInitialRestart based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SonusIsdnsgSwitchProfileBchannelInitialRestart_Type.__name__ = "Integer32"
_SonusIsdnsgSwitchProfileBchannelInitialRestart_Object = MibTableColumn
sonusIsdnsgSwitchProfileBchannelInitialRestart = _SonusIsdnsgSwitchProfileBchannelInitialRestart_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 1, 7, 2, 1, 27),
    _SonusIsdnsgSwitchProfileBchannelInitialRestart_Type()
)
sonusIsdnsgSwitchProfileBchannelInitialRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsdnsgSwitchProfileBchannelInitialRestart.setStatus("current")
_SonusIsdnServiceGroupMIBNotifications_ObjectIdentity = ObjectIdentity
sonusIsdnServiceGroupMIBNotifications = _SonusIsdnServiceGroupMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 2)
)
_SonusIsdnServiceGroupMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
sonusIsdnServiceGroupMIBNotificationsPrefix = _SonusIsdnServiceGroupMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 2, 0)
)
_SonusIsdnServiceGroupMIBNotificationsObjects_ObjectIdentity = ObjectIdentity
sonusIsdnServiceGroupMIBNotificationsObjects = _SonusIsdnServiceGroupMIBNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 2, 1)
)


class _SonusIsdnSvcGrpName_Type(DisplayString):
    """Custom type sonusIsdnSvcGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusIsdnSvcGrpName_Type.__name__ = "DisplayString"
_SonusIsdnSvcGrpName_Object = MibScalar
sonusIsdnSvcGrpName = _SonusIsdnSvcGrpName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 2, 1, 1),
    _SonusIsdnSvcGrpName_Type()
)
sonusIsdnSvcGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnSvcGrpName.setStatus("current")


class _SonusIsdnInterfaceId_Type(Integer32):
    """Custom type sonusIsdnInterfaceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsdnInterfaceId_Type.__name__ = "Integer32"
_SonusIsdnInterfaceId_Object = MibScalar
sonusIsdnInterfaceId = _SonusIsdnInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 2, 1, 2),
    _SonusIsdnInterfaceId_Type()
)
sonusIsdnInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnInterfaceId.setStatus("current")


class _SonusIsdnBchannelOffsets_Type(Bits):
    """Custom type sonusIsdnBchannelOffsets based on Bits"""
    namedValues = NamedValues(
        *(("bchOffset0", 0),
          ("bchOffset1", 1),
          ("bchOffset10", 10),
          ("bchOffset11", 11),
          ("bchOffset12", 12),
          ("bchOffset13", 13),
          ("bchOffset14", 14),
          ("bchOffset15", 15),
          ("bchOffset16", 16),
          ("bchOffset17", 17),
          ("bchOffset18", 18),
          ("bchOffset19", 19),
          ("bchOffset2", 2),
          ("bchOffset20", 20),
          ("bchOffset21", 21),
          ("bchOffset22", 22),
          ("bchOffset23", 23),
          ("bchOffset3", 3),
          ("bchOffset4", 4),
          ("bchOffset5", 5),
          ("bchOffset6", 6),
          ("bchOffset7", 7),
          ("bchOffset8", 8),
          ("bchOffset9", 9))
    )

_SonusIsdnBchannelOffsets_Type.__name__ = "Bits"
_SonusIsdnBchannelOffsets_Object = MibScalar
sonusIsdnBchannelOffsets = _SonusIsdnBchannelOffsets_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 2, 1, 3),
    _SonusIsdnBchannelOffsets_Type()
)
sonusIsdnBchannelOffsets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsdnBchannelOffsets.setStatus("current")

# Managed Objects groups


# Notification objects

sonusIsdnSvcGrpInServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 2, 0, 1)
)
sonusIsdnSvcGrpInServiceNotification.setObjects(
      *(("SONUS-ISDN-SERVICE-GROUP-MIB", "sonusIsdnSvcGrpName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusIsdnSvcGrpInServiceNotification.setStatus(
        "current"
    )

sonusIsdnSvcGrpOutOfServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 2, 0, 2)
)
sonusIsdnSvcGrpOutOfServiceNotification.setObjects(
      *(("SONUS-ISDN-SERVICE-GROUP-MIB", "sonusIsdnSvcGrpName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusIsdnSvcGrpOutOfServiceNotification.setStatus(
        "current"
    )

sonusIsdnBChannelInServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 2, 0, 3)
)
sonusIsdnBChannelInServiceNotification.setObjects(
      *(("SONUS-ISDN-SERVICE-GROUP-MIB", "sonusIsdnSvcGrpName"),
        ("SONUS-ISDN-SERVICE-GROUP-MIB", "sonusIsdnInterfaceId"),
        ("SONUS-ISDN-SERVICE-GROUP-MIB", "sonusIsdnBchannelOffsets"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusIsdnBChannelInServiceNotification.setStatus(
        "current"
    )

sonusIsdnBChannelOutOfServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 2, 0, 4)
)
sonusIsdnBChannelOutOfServiceNotification.setObjects(
      *(("SONUS-ISDN-SERVICE-GROUP-MIB", "sonusIsdnSvcGrpName"),
        ("SONUS-ISDN-SERVICE-GROUP-MIB", "sonusIsdnInterfaceId"),
        ("SONUS-ISDN-SERVICE-GROUP-MIB", "sonusIsdnBchannelOffsets"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusIsdnBChannelOutOfServiceNotification.setStatus(
        "current"
    )

sonusIsdnPrimaryDChannelInServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 2, 0, 5)
)
sonusIsdnPrimaryDChannelInServiceNotification.setObjects(
      *(("SONUS-ISDN-SERVICE-GROUP-MIB", "sonusIsdnSvcGrpName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusIsdnPrimaryDChannelInServiceNotification.setStatus(
        "current"
    )

sonusIsdnPrimaryDChannelOutOfServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 2, 0, 6)
)
sonusIsdnPrimaryDChannelOutOfServiceNotification.setObjects(
      *(("SONUS-ISDN-SERVICE-GROUP-MIB", "sonusIsdnSvcGrpName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusIsdnPrimaryDChannelOutOfServiceNotification.setStatus(
        "current"
    )

sonusIsdnBackupDChannelInServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 2, 0, 7)
)
sonusIsdnBackupDChannelInServiceNotification.setObjects(
      *(("SONUS-ISDN-SERVICE-GROUP-MIB", "sonusIsdnSvcGrpName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusIsdnBackupDChannelInServiceNotification.setStatus(
        "current"
    )

sonusIsdnBackupDChannelOutOfServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 4, 2, 0, 8)
)
sonusIsdnBackupDChannelOutOfServiceNotification.setObjects(
      *(("SONUS-ISDN-SERVICE-GROUP-MIB", "sonusIsdnSvcGrpName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusIsdnBackupDChannelOutOfServiceNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-ISDN-SERVICE-GROUP-MIB",
    **{"sonusIsdnServiceGroupMIB": sonusIsdnServiceGroupMIB,
       "sonusIsdnServiceGroupMIBObjects": sonusIsdnServiceGroupMIBObjects,
       "sonusIsdnsgServiceGroup": sonusIsdnsgServiceGroup,
       "sonusIsdnsgServiceGroupNextIndex": sonusIsdnsgServiceGroupNextIndex,
       "sonusIsdnsgServiceGroupTable": sonusIsdnsgServiceGroupTable,
       "sonusIsdnsgServiceGroupEntry": sonusIsdnsgServiceGroupEntry,
       "sonusIsdnsgServiceGroupListIndex": sonusIsdnsgServiceGroupListIndex,
       "sonusIsdnsgServiceGroupName": sonusIsdnsgServiceGroupName,
       "sonusIsdnsgServiceGroupTrunkGroup": sonusIsdnsgServiceGroupTrunkGroup,
       "sonusIsdnsgServiceGroupHuntAlgorithm": sonusIsdnsgServiceGroupHuntAlgorithm,
       "sonusIsdnsgServiceGroupCost": sonusIsdnsgServiceGroupCost,
       "sonusIsdnsgServiceGroupSwitchSide": sonusIsdnsgServiceGroupSwitchSide,
       "sonusIsdnsgServiceGroupSwitchType": sonusIsdnsgServiceGroupSwitchType,
       "sonusIsdnsgServiceGroupSwitchProfileName": sonusIsdnsgServiceGroupSwitchProfileName,
       "sonusIsdnsgServiceGroupOperation": sonusIsdnsgServiceGroupOperation,
       "sonusIsdnsgServiceGroupPrimaryDchannelInterface": sonusIsdnsgServiceGroupPrimaryDchannelInterface,
       "sonusIsdnsgServiceGroupPrimaryDchannelTimeSlot": sonusIsdnsgServiceGroupPrimaryDchannelTimeSlot,
       "sonusIsdnsgServiceGroupPrimaryDchannelMode": sonusIsdnsgServiceGroupPrimaryDchannelMode,
       "sonusIsdnsgServiceGroupBackupDchannelInterface": sonusIsdnsgServiceGroupBackupDchannelInterface,
       "sonusIsdnsgServiceGroupBackupDchannelTimeSlot": sonusIsdnsgServiceGroupBackupDchannelTimeSlot,
       "sonusIsdnsgServiceGroupBackupDchannelMode": sonusIsdnsgServiceGroupBackupDchannelMode,
       "sonusIsdnsgServiceGroupLayerTrace": sonusIsdnsgServiceGroupLayerTrace,
       "sonusIsdnsgServiceGroupMode": sonusIsdnsgServiceGroupMode,
       "sonusIsdnsgServiceGroupAction": sonusIsdnsgServiceGroupAction,
       "sonusIsdnsgServiceGroupTimeout": sonusIsdnsgServiceGroupTimeout,
       "sonusIsdnsgServiceGroupAdminState": sonusIsdnsgServiceGroupAdminState,
       "sonusIsdnsgServiceGroupProfileName": sonusIsdnsgServiceGroupProfileName,
       "sonusIsdnsgServiceGroupRowStatus": sonusIsdnsgServiceGroupRowStatus,
       "sonusIsdnsgServiceGroupDefaultDirectoryNumber": sonusIsdnsgServiceGroupDefaultDirectoryNumber,
       "sonusIsdnsgServiceGroupCallingPartyNumberProvision": sonusIsdnsgServiceGroupCallingPartyNumberProvision,
       "sonusIsdnsgServiceGroupCallingPartyNumberDiscard": sonusIsdnsgServiceGroupCallingPartyNumberDiscard,
       "sonusIsdnsgServiceGroupCallingPartyNumberDelivery": sonusIsdnsgServiceGroupCallingPartyNumberDelivery,
       "sonusIsdnsgServiceGroupCallingPartySubAddressTransfer": sonusIsdnsgServiceGroupCallingPartySubAddressTransfer,
       "sonusIsdnsgServiceGroupCallingPartySubAddressDelivery": sonusIsdnsgServiceGroupCallingPartySubAddressDelivery,
       "sonusIsdnsgServiceGroupBchannelAvailabilitySignaling": sonusIsdnsgServiceGroupBchannelAvailabilitySignaling,
       "sonusIsdnsgServiceGroupVerboseTrace": sonusIsdnsgServiceGroupVerboseTrace,
       "sonusIsdnsgServiceGroupCallingPartyNumberPresentation": sonusIsdnsgServiceGroupCallingPartyNumberPresentation,
       "sonusIsdnsgServiceGroupDiscTreatmentProfileName": sonusIsdnsgServiceGroupDiscTreatmentProfileName,
       "sonusIsdnsgServiceGroupTonePackageName": sonusIsdnsgServiceGroupTonePackageName,
       "sonusIsdnsgServiceGroupT302": sonusIsdnsgServiceGroupT302,
       "sonusIsdnsgServiceGroupT303": sonusIsdnsgServiceGroupT303,
       "sonusIsdnsgServiceGroupT304": sonusIsdnsgServiceGroupT304,
       "sonusIsdnsgServiceGroupT305": sonusIsdnsgServiceGroupT305,
       "sonusIsdnsgServiceGroupT306": sonusIsdnsgServiceGroupT306,
       "sonusIsdnsgServiceGroupT308": sonusIsdnsgServiceGroupT308,
       "sonusIsdnsgServiceGroupT309": sonusIsdnsgServiceGroupT309,
       "sonusIsdnsgServiceGroupT310": sonusIsdnsgServiceGroupT310,
       "sonusIsdnsgServiceGroupT312": sonusIsdnsgServiceGroupT312,
       "sonusIsdnsgServiceGroupT313": sonusIsdnsgServiceGroupT313,
       "sonusIsdnsgServiceGroupT314": sonusIsdnsgServiceGroupT314,
       "sonusIsdnsgServiceGroupT318": sonusIsdnsgServiceGroupT318,
       "sonusIsdnsgServiceGroupT319": sonusIsdnsgServiceGroupT319,
       "sonusIsdnsgServiceGroupT322": sonusIsdnsgServiceGroupT322,
       "sonusIsdnsgServiceGroupK": sonusIsdnsgServiceGroupK,
       "sonusIsdnsgServiceGroupT200": sonusIsdnsgServiceGroupT200,
       "sonusIsdnsgServiceGroupT203": sonusIsdnsgServiceGroupT203,
       "sonusIsdnsgServiceGroupN200": sonusIsdnsgServiceGroupN200,
       "sonusIsdnsgServiceGroupN201": sonusIsdnsgServiceGroupN201,
       "sonusIsdnsgServiceGroupBchannelInitialRestart": sonusIsdnsgServiceGroupBchannelInitialRestart,
       "sonusIsdnsgServiceGroupIuaApplicationServer": sonusIsdnsgServiceGroupIuaApplicationServer,
       "sonusIsdnsgServiceGroupIuaAutoDatalinkEstablish": sonusIsdnsgServiceGroupIuaAutoDatalinkEstablish,
       "sonusIsdnsgServiceGroupStatTable": sonusIsdnsgServiceGroupStatTable,
       "sonusIsdnsgServiceGroupStatEntry": sonusIsdnsgServiceGroupStatEntry,
       "sonusIsdnsgServiceGroupStatListIndex": sonusIsdnsgServiceGroupStatListIndex,
       "sonusIsdnsgServiceGroupStatStatus": sonusIsdnsgServiceGroupStatStatus,
       "sonusIsdnsgServiceGroupStatTgMode": sonusIsdnsgServiceGroupStatTgMode,
       "sonusIsdnsgServiceGroupStatNumBchConfigured": sonusIsdnsgServiceGroupStatNumBchConfigured,
       "sonusIsdnsgServiceGroupStatNumBchAvailable": sonusIsdnsgServiceGroupStatNumBchAvailable,
       "sonusIsdnsgServiceGroupStatInCallsActive": sonusIsdnsgServiceGroupStatInCallsActive,
       "sonusIsdnsgServiceGroupStatInCalls": sonusIsdnsgServiceGroupStatInCalls,
       "sonusIsdnsgServiceGroupStatInConnected": sonusIsdnsgServiceGroupStatInConnected,
       "sonusIsdnsgServiceGroupStatOutCallsActive": sonusIsdnsgServiceGroupStatOutCallsActive,
       "sonusIsdnsgServiceGroupStatOutCalls": sonusIsdnsgServiceGroupStatOutCalls,
       "sonusIsdnsgServiceGroupStatOutConnected": sonusIsdnsgServiceGroupStatOutConnected,
       "sonusIsdnsgServiceGroupStatPrimaryDchannel": sonusIsdnsgServiceGroupStatPrimaryDchannel,
       "sonusIsdnsgServiceGroupStatPrimaryDchInPkts": sonusIsdnsgServiceGroupStatPrimaryDchInPkts,
       "sonusIsdnsgServiceGroupStatPrimaryDchOutPkts": sonusIsdnsgServiceGroupStatPrimaryDchOutPkts,
       "sonusIsdnsgServiceGroupStatPrimaryDchInBytes": sonusIsdnsgServiceGroupStatPrimaryDchInBytes,
       "sonusIsdnsgServiceGroupStatPrimaryDchOutBytes": sonusIsdnsgServiceGroupStatPrimaryDchOutBytes,
       "sonusIsdnsgServiceGroupStatBackupDchannel": sonusIsdnsgServiceGroupStatBackupDchannel,
       "sonusIsdnsgServiceGroupStatBackupDchInPkts": sonusIsdnsgServiceGroupStatBackupDchInPkts,
       "sonusIsdnsgServiceGroupStatBackupDchOutPkts": sonusIsdnsgServiceGroupStatBackupDchOutPkts,
       "sonusIsdnsgServiceGroupStatBackupDchInBytes": sonusIsdnsgServiceGroupStatBackupDchInBytes,
       "sonusIsdnsgServiceGroupStatBackupDchOutBytes": sonusIsdnsgServiceGroupStatBackupDchOutBytes,
       "sonusIsdnsgProfile": sonusIsdnsgProfile,
       "sonusIsdnsgProfileNextIndex": sonusIsdnsgProfileNextIndex,
       "sonusIsdnsgProfileTable": sonusIsdnsgProfileTable,
       "sonusIsdnsgProfileEntry": sonusIsdnsgProfileEntry,
       "sonusIsdnsgProfileListIndex": sonusIsdnsgProfileListIndex,
       "sonusIsdnsgProfileName": sonusIsdnsgProfileName,
       "sonusIsdnsgProfileTrunkGroup": sonusIsdnsgProfileTrunkGroup,
       "sonusIsdnsgProfileHuntAlgorithm": sonusIsdnsgProfileHuntAlgorithm,
       "sonusIsdnsgProfileCost": sonusIsdnsgProfileCost,
       "sonusIsdnsgProfileSwitchSide": sonusIsdnsgProfileSwitchSide,
       "sonusIsdnsgProfileSwitchType": sonusIsdnsgProfileSwitchType,
       "sonusIsdnsgProfileSwitchProfile": sonusIsdnsgProfileSwitchProfile,
       "sonusIsdnsgProfileMode": sonusIsdnsgProfileMode,
       "sonusIsdnsgProfileAdminState": sonusIsdnsgProfileAdminState,
       "sonusIsdnsgProfileRowStatus": sonusIsdnsgProfileRowStatus,
       "sonusIsdnsgProfileDefaultDirectoryNumber": sonusIsdnsgProfileDefaultDirectoryNumber,
       "sonusIsdnsgProfileCallingPartyNumberProvision": sonusIsdnsgProfileCallingPartyNumberProvision,
       "sonusIsdnsgProfileCallingPartyNumberDiscard": sonusIsdnsgProfileCallingPartyNumberDiscard,
       "sonusIsdnsgProfileCallingPartyNumberDelivery": sonusIsdnsgProfileCallingPartyNumberDelivery,
       "sonusIsdnsgProfileCallingPartySubAddressTransfer": sonusIsdnsgProfileCallingPartySubAddressTransfer,
       "sonusIsdnsgProfileCallingPartySubAddressDelivery": sonusIsdnsgProfileCallingPartySubAddressDelivery,
       "sonusIsdnsgProfileCallingPartyNumberPresentation": sonusIsdnsgProfileCallingPartyNumberPresentation,
       "sonusIsdnsgInterfaceTable": sonusIsdnsgInterfaceTable,
       "sonusIsdnsgInterfaceEntry": sonusIsdnsgInterfaceEntry,
       "sonusIsdnsgInterfaceServiceListIndex": sonusIsdnsgInterfaceServiceListIndex,
       "sonusIsdnsgInterfaceIdentifier": sonusIsdnsgInterfaceIdentifier,
       "sonusIsdnsgInterfacePortName": sonusIsdnsgInterfacePortName,
       "sonusIsdnsgInterfaceOperation": sonusIsdnsgInterfaceOperation,
       "sonusIsdnsgInterfaceAdminState": sonusIsdnsgInterfaceAdminState,
       "sonusIsdnsgInterfaceRowStatus": sonusIsdnsgInterfaceRowStatus,
       "sonusIsdnsgBchannelTable": sonusIsdnsgBchannelTable,
       "sonusIsdnsgBchannelEntry": sonusIsdnsgBchannelEntry,
       "sonusIsdnsgBchannelServiceListIndex": sonusIsdnsgBchannelServiceListIndex,
       "sonusIsdnsgBchannelInterfaceIdentifier": sonusIsdnsgBchannelInterfaceIdentifier,
       "sonusIsdnsgBchannelNumber": sonusIsdnsgBchannelNumber,
       "sonusIsdnsgBchannelCircuitProfileName": sonusIsdnsgBchannelCircuitProfileName,
       "sonusIsdnsgBchannelDirection": sonusIsdnsgBchannelDirection,
       "sonusIsdnsgBchannelOperation": sonusIsdnsgBchannelOperation,
       "sonusIsdnsgBchannelMode": sonusIsdnsgBchannelMode,
       "sonusIsdnsgBchannelAction": sonusIsdnsgBchannelAction,
       "sonusIsdnsgBchannelTimeout": sonusIsdnsgBchannelTimeout,
       "sonusIsdnsgBchannelAdminState": sonusIsdnsgBchannelAdminState,
       "sonusIsdnsgBchannelStatTable": sonusIsdnsgBchannelStatTable,
       "sonusIsdnsgBchannelStatEntry": sonusIsdnsgBchannelStatEntry,
       "sonusIsdnsgBchannelStatServiceListIndex": sonusIsdnsgBchannelStatServiceListIndex,
       "sonusIsdnsgBchannelStatInterfaceIdentifier": sonusIsdnsgBchannelStatInterfaceIdentifier,
       "sonusIsdnsgBchannelStatNumber": sonusIsdnsgBchannelStatNumber,
       "sonusIsdnsgBchannelStatUsage": sonusIsdnsgBchannelStatUsage,
       "sonusIsdnsgBchannelStatLocalMaint": sonusIsdnsgBchannelStatLocalMaint,
       "sonusIsdnsgBchannelStatLocalHw": sonusIsdnsgBchannelStatLocalHw,
       "sonusIsdnsgBchannelStatRemoteMaint": sonusIsdnsgBchannelStatRemoteMaint,
       "sonusIsdnsgSwitchProfile": sonusIsdnsgSwitchProfile,
       "sonusIsdnsgSwitchProfileNextIndex": sonusIsdnsgSwitchProfileNextIndex,
       "sonusIsdnsgSwitchProfileTable": sonusIsdnsgSwitchProfileTable,
       "sonusIsdnsgSwitchProfileEntry": sonusIsdnsgSwitchProfileEntry,
       "sonusIsdnsgSwitchProfileListIndex": sonusIsdnsgSwitchProfileListIndex,
       "sonusIsdnsgSwitchProfileName": sonusIsdnsgSwitchProfileName,
       "sonusIsdnsgSwitchProfileSwitchSide": sonusIsdnsgSwitchProfileSwitchSide,
       "sonusIsdnsgSwitchProfileSwitchType": sonusIsdnsgSwitchProfileSwitchType,
       "sonusIsdnsgSwitchProfileBchannelAvailabilitySignaling": sonusIsdnsgSwitchProfileBchannelAvailabilitySignaling,
       "sonusIsdnsgSwitchProfileT302": sonusIsdnsgSwitchProfileT302,
       "sonusIsdnsgSwitchProfileT303": sonusIsdnsgSwitchProfileT303,
       "sonusIsdnsgSwitchProfileT304": sonusIsdnsgSwitchProfileT304,
       "sonusIsdnsgSwitchProfileT305": sonusIsdnsgSwitchProfileT305,
       "sonusIsdnsgSwitchProfileT306": sonusIsdnsgSwitchProfileT306,
       "sonusIsdnsgSwitchProfileT308": sonusIsdnsgSwitchProfileT308,
       "sonusIsdnsgSwitchProfileT309": sonusIsdnsgSwitchProfileT309,
       "sonusIsdnsgSwitchProfileT310": sonusIsdnsgSwitchProfileT310,
       "sonusIsdnsgSwitchProfileT312": sonusIsdnsgSwitchProfileT312,
       "sonusIsdnsgSwitchProfileT313": sonusIsdnsgSwitchProfileT313,
       "sonusIsdnsgSwitchProfileT314": sonusIsdnsgSwitchProfileT314,
       "sonusIsdnsgSwitchProfileT318": sonusIsdnsgSwitchProfileT318,
       "sonusIsdnsgSwitchProfileT319": sonusIsdnsgSwitchProfileT319,
       "sonusIsdnsgSwitchProfileT322": sonusIsdnsgSwitchProfileT322,
       "sonusIsdnsgSwitchProfileK": sonusIsdnsgSwitchProfileK,
       "sonusIsdnsgSwitchProfileT200": sonusIsdnsgSwitchProfileT200,
       "sonusIsdnsgSwitchProfileT203": sonusIsdnsgSwitchProfileT203,
       "sonusIsdnsgSwitchProfileN200": sonusIsdnsgSwitchProfileN200,
       "sonusIsdnsgSwitchProfileN201": sonusIsdnsgSwitchProfileN201,
       "sonusIsdnsgSwitchProfileAdminState": sonusIsdnsgSwitchProfileAdminState,
       "sonusIsdnsgSwitchProfileRowStatus": sonusIsdnsgSwitchProfileRowStatus,
       "sonusIsdnsgSwitchProfileBchannelInitialRestart": sonusIsdnsgSwitchProfileBchannelInitialRestart,
       "sonusIsdnServiceGroupMIBNotifications": sonusIsdnServiceGroupMIBNotifications,
       "sonusIsdnServiceGroupMIBNotificationsPrefix": sonusIsdnServiceGroupMIBNotificationsPrefix,
       "sonusIsdnSvcGrpInServiceNotification": sonusIsdnSvcGrpInServiceNotification,
       "sonusIsdnSvcGrpOutOfServiceNotification": sonusIsdnSvcGrpOutOfServiceNotification,
       "sonusIsdnBChannelInServiceNotification": sonusIsdnBChannelInServiceNotification,
       "sonusIsdnBChannelOutOfServiceNotification": sonusIsdnBChannelOutOfServiceNotification,
       "sonusIsdnPrimaryDChannelInServiceNotification": sonusIsdnPrimaryDChannelInServiceNotification,
       "sonusIsdnPrimaryDChannelOutOfServiceNotification": sonusIsdnPrimaryDChannelOutOfServiceNotification,
       "sonusIsdnBackupDChannelInServiceNotification": sonusIsdnBackupDChannelInServiceNotification,
       "sonusIsdnBackupDChannelOutOfServiceNotification": sonusIsdnBackupDChannelOutOfServiceNotification,
       "sonusIsdnServiceGroupMIBNotificationsObjects": sonusIsdnServiceGroupMIBNotificationsObjects,
       "sonusIsdnSvcGrpName": sonusIsdnSvcGrpName,
       "sonusIsdnInterfaceId": sonusIsdnInterfaceId,
       "sonusIsdnBchannelOffsets": sonusIsdnBchannelOffsets}
)
