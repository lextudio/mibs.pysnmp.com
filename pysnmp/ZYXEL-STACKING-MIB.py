# SNMP MIB module (ZYXEL-STACKING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-STACKING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:49 2024
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelStacking = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelStackingSetup_ObjectIdentity = ObjectIdentity
zyxelStackingSetup = _ZyxelStackingSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 1)
)


class _ZyStackingPriority_Type(Integer32):
    """Custom type zyStackingPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_ZyStackingPriority_Type.__name__ = "Integer32"
_ZyStackingPriority_Object = MibScalar
zyStackingPriority = _ZyStackingPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 1, 1),
    _ZyStackingPriority_Type()
)
zyStackingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyStackingPriority.setStatus("current")
_ZyStackingForceMasterModeState_Type = EnabledStatus
_ZyStackingForceMasterModeState_Object = MibScalar
zyStackingForceMasterModeState = _ZyStackingForceMasterModeState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 1, 2),
    _ZyStackingForceMasterModeState_Type()
)
zyStackingForceMasterModeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyStackingForceMasterModeState.setStatus("current")
_ZyxelStackingSlotTable_Object = MibTable
zyxelStackingSlotTable = _ZyxelStackingSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 1, 3)
)
if mibBuilder.loadTexts:
    zyxelStackingSlotTable.setStatus("current")
_ZyxelStackingSlotEntry_Object = MibTableRow
zyxelStackingSlotEntry = _ZyxelStackingSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 1, 3, 1)
)
zyxelStackingSlotEntry.setIndexNames(
    (0, "ZYXEL-STACKING-MIB", "zyStackingSlotCurrentSlotId"),
)
if mibBuilder.loadTexts:
    zyxelStackingSlotEntry.setStatus("current")
_ZyStackingSlotCurrentSlotId_Type = Integer32
_ZyStackingSlotCurrentSlotId_Object = MibTableColumn
zyStackingSlotCurrentSlotId = _ZyStackingSlotCurrentSlotId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 1, 3, 1, 1),
    _ZyStackingSlotCurrentSlotId_Type()
)
zyStackingSlotCurrentSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyStackingSlotCurrentSlotId.setStatus("current")


class _ZyStackingSlotActiveSlotIdAfterReboot_Type(Integer32):
    """Custom type zyStackingSlotActiveSlotIdAfterReboot based on Integer32"""
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
        *(("auto", 0),
          ("slotId1", 1),
          ("slotId2", 2),
          ("slotId3", 3),
          ("slotId4", 4),
          ("slotId5", 5),
          ("slotId6", 6),
          ("slotId7", 7),
          ("slotId8", 8))
    )


_ZyStackingSlotActiveSlotIdAfterReboot_Type.__name__ = "Integer32"
_ZyStackingSlotActiveSlotIdAfterReboot_Object = MibTableColumn
zyStackingSlotActiveSlotIdAfterReboot = _ZyStackingSlotActiveSlotIdAfterReboot_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 1, 3, 1, 2),
    _ZyStackingSlotActiveSlotIdAfterReboot_Type()
)
zyStackingSlotActiveSlotIdAfterReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyStackingSlotActiveSlotIdAfterReboot.setStatus("current")
_ZyStackingSlotIdFreeze_Type = EnabledStatus
_ZyStackingSlotIdFreeze_Object = MibScalar
zyStackingSlotIdFreeze = _ZyStackingSlotIdFreeze_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 1, 4),
    _ZyStackingSlotIdFreeze_Type()
)
zyStackingSlotIdFreeze.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyStackingSlotIdFreeze.setStatus("current")
_ZyxelStackingStatus_ObjectIdentity = ObjectIdentity
zyxelStackingStatus = _ZyxelStackingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 2)
)
_ZyxelStackingSlotInfoTable_Object = MibTable
zyxelStackingSlotInfoTable = _ZyxelStackingSlotInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 2, 1)
)
if mibBuilder.loadTexts:
    zyxelStackingSlotInfoTable.setStatus("current")
_ZyxelStackingSlotInfoEntry_Object = MibTableRow
zyxelStackingSlotInfoEntry = _ZyxelStackingSlotInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 2, 1, 1)
)
zyxelStackingSlotInfoEntry.setIndexNames(
    (0, "ZYXEL-STACKING-MIB", "zyStackingSlotInfoSlot"),
)
if mibBuilder.loadTexts:
    zyxelStackingSlotInfoEntry.setStatus("current")
_ZyStackingSlotInfoSlot_Type = Integer32
_ZyStackingSlotInfoSlot_Object = MibTableColumn
zyStackingSlotInfoSlot = _ZyStackingSlotInfoSlot_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 2, 1, 1, 1),
    _ZyStackingSlotInfoSlot_Type()
)
zyStackingSlotInfoSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyStackingSlotInfoSlot.setStatus("current")


class _ZyStackingSlotInfoStackingStatus_Type(Integer32):
    """Custom type zyStackingSlotInfoStackingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 0),
          ("init", 1))
    )


_ZyStackingSlotInfoStackingStatus_Type.__name__ = "Integer32"
_ZyStackingSlotInfoStackingStatus_Object = MibTableColumn
zyStackingSlotInfoStackingStatus = _ZyStackingSlotInfoStackingStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 2, 1, 1, 2),
    _ZyStackingSlotInfoStackingStatus_Type()
)
zyStackingSlotInfoStackingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyStackingSlotInfoStackingStatus.setStatus("current")
_ZyStackingSlotInfoForceMasterMode_Type = EnabledStatus
_ZyStackingSlotInfoForceMasterMode_Object = MibTableColumn
zyStackingSlotInfoForceMasterMode = _ZyStackingSlotInfoForceMasterMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 2, 1, 1, 3),
    _ZyStackingSlotInfoForceMasterMode_Type()
)
zyStackingSlotInfoForceMasterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyStackingSlotInfoForceMasterMode.setStatus("current")
_ZyStackingSlotInfoPriority_Type = Integer32
_ZyStackingSlotInfoPriority_Object = MibTableColumn
zyStackingSlotInfoPriority = _ZyStackingSlotInfoPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 2, 1, 1, 4),
    _ZyStackingSlotInfoPriority_Type()
)
zyStackingSlotInfoPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyStackingSlotInfoPriority.setStatus("current")


class _ZyStackingSlotInfoRole_Type(Integer32):
    """Custom type zyStackingSlotInfoRole based on Integer32"""
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
        *(("backup", 2),
          ("linecard", 3),
          ("master", 1),
          ("none", 0))
    )


_ZyStackingSlotInfoRole_Type.__name__ = "Integer32"
_ZyStackingSlotInfoRole_Object = MibTableColumn
zyStackingSlotInfoRole = _ZyStackingSlotInfoRole_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 2, 1, 1, 5),
    _ZyStackingSlotInfoRole_Type()
)
zyStackingSlotInfoRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyStackingSlotInfoRole.setStatus("current")
_ZyStackingSlotInfoMacAddress_Type = OctetString
_ZyStackingSlotInfoMacAddress_Object = MibTableColumn
zyStackingSlotInfoMacAddress = _ZyStackingSlotInfoMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 2, 1, 1, 6),
    _ZyStackingSlotInfoMacAddress_Type()
)
zyStackingSlotInfoMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyStackingSlotInfoMacAddress.setStatus("current")
_ZyStackingSlotInfoUptime_Type = TimeTicks
_ZyStackingSlotInfoUptime_Object = MibTableColumn
zyStackingSlotInfoUptime = _ZyStackingSlotInfoUptime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 2, 1, 1, 7),
    _ZyStackingSlotInfoUptime_Type()
)
zyStackingSlotInfoUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyStackingSlotInfoUptime.setStatus("current")
_ZyStackingSlotInfoFirmwareVersionRunning_Type = OctetString
_ZyStackingSlotInfoFirmwareVersionRunning_Object = MibTableColumn
zyStackingSlotInfoFirmwareVersionRunning = _ZyStackingSlotInfoFirmwareVersionRunning_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 2, 1, 1, 8),
    _ZyStackingSlotInfoFirmwareVersionRunning_Type()
)
zyStackingSlotInfoFirmwareVersionRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyStackingSlotInfoFirmwareVersionRunning.setStatus("current")
_ZyStackingSlotInfoFirmwareVersionFlash1_Type = OctetString
_ZyStackingSlotInfoFirmwareVersionFlash1_Object = MibTableColumn
zyStackingSlotInfoFirmwareVersionFlash1 = _ZyStackingSlotInfoFirmwareVersionFlash1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 2, 1, 1, 9),
    _ZyStackingSlotInfoFirmwareVersionFlash1_Type()
)
zyStackingSlotInfoFirmwareVersionFlash1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyStackingSlotInfoFirmwareVersionFlash1.setStatus("current")
_ZyStackingSlotInfoFirmwareVersionFlash2_Type = OctetString
_ZyStackingSlotInfoFirmwareVersionFlash2_Object = MibTableColumn
zyStackingSlotInfoFirmwareVersionFlash2 = _ZyStackingSlotInfoFirmwareVersionFlash2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 2, 1, 1, 10),
    _ZyStackingSlotInfoFirmwareVersionFlash2_Type()
)
zyStackingSlotInfoFirmwareVersionFlash2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyStackingSlotInfoFirmwareVersionFlash2.setStatus("current")
_ZyxelStackingSlotChannelInfoTable_Object = MibTable
zyxelStackingSlotChannelInfoTable = _ZyxelStackingSlotChannelInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 2, 2)
)
if mibBuilder.loadTexts:
    zyxelStackingSlotChannelInfoTable.setStatus("current")
_ZyxelStackingSlotChannelInfoEntry_Object = MibTableRow
zyxelStackingSlotChannelInfoEntry = _ZyxelStackingSlotChannelInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 2, 2, 1)
)
zyxelStackingSlotChannelInfoEntry.setIndexNames(
    (0, "ZYXEL-STACKING-MIB", "zyStackingSlotChannelInfoSlot"),
    (0, "ZYXEL-STACKING-MIB", "zyStackingSlotChannelInfoChannnel"),
)
if mibBuilder.loadTexts:
    zyxelStackingSlotChannelInfoEntry.setStatus("current")
_ZyStackingSlotChannelInfoSlot_Type = Integer32
_ZyStackingSlotChannelInfoSlot_Object = MibTableColumn
zyStackingSlotChannelInfoSlot = _ZyStackingSlotChannelInfoSlot_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 2, 2, 1, 1),
    _ZyStackingSlotChannelInfoSlot_Type()
)
zyStackingSlotChannelInfoSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyStackingSlotChannelInfoSlot.setStatus("current")
_ZyStackingSlotChannelInfoChannnel_Type = Integer32
_ZyStackingSlotChannelInfoChannnel_Object = MibTableColumn
zyStackingSlotChannelInfoChannnel = _ZyStackingSlotChannelInfoChannnel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 2, 2, 1, 2),
    _ZyStackingSlotChannelInfoChannnel_Type()
)
zyStackingSlotChannelInfoChannnel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyStackingSlotChannelInfoChannnel.setStatus("current")


class _ZyStackingSlotChannelInfoStatus_Type(Integer32):
    """Custom type zyStackingSlotChannelInfoStatus based on Integer32"""
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


_ZyStackingSlotChannelInfoStatus_Type.__name__ = "Integer32"
_ZyStackingSlotChannelInfoStatus_Object = MibTableColumn
zyStackingSlotChannelInfoStatus = _ZyStackingSlotChannelInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 2, 2, 1, 3),
    _ZyStackingSlotChannelInfoStatus_Type()
)
zyStackingSlotChannelInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyStackingSlotChannelInfoStatus.setStatus("current")
_ZyStackingSlotChannelInfoPorts_Type = PortList
_ZyStackingSlotChannelInfoPorts_Object = MibTableColumn
zyStackingSlotChannelInfoPorts = _ZyStackingSlotChannelInfoPorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 2, 2, 1, 4),
    _ZyStackingSlotChannelInfoPorts_Type()
)
zyStackingSlotChannelInfoPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyStackingSlotChannelInfoPorts.setStatus("current")
_ZyStackingSlotChannelInfoNeighbor_Type = Integer32
_ZyStackingSlotChannelInfoNeighbor_Object = MibTableColumn
zyStackingSlotChannelInfoNeighbor = _ZyStackingSlotChannelInfoNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 2, 2, 1, 5),
    _ZyStackingSlotChannelInfoNeighbor_Type()
)
zyStackingSlotChannelInfoNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyStackingSlotChannelInfoNeighbor.setStatus("current")


class _ZyStackingSlotChannelInfoSpeed_Type(Integer32):
    """Custom type zyStackingSlotChannelInfoSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("speed_10G", 1),
          ("speed_12G", 2))
    )


_ZyStackingSlotChannelInfoSpeed_Type.__name__ = "Integer32"
_ZyStackingSlotChannelInfoSpeed_Object = MibTableColumn
zyStackingSlotChannelInfoSpeed = _ZyStackingSlotChannelInfoSpeed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 2, 2, 1, 6),
    _ZyStackingSlotChannelInfoSpeed_Type()
)
zyStackingSlotChannelInfoSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyStackingSlotChannelInfoSpeed.setStatus("current")


class _ZyStackingTopology_Type(Integer32):
    """Custom type zyStackingTopology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chain", 1),
          ("ring", 2))
    )


_ZyStackingTopology_Type.__name__ = "Integer32"
_ZyStackingTopology_Object = MibScalar
zyStackingTopology = _ZyStackingTopology_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 2, 3),
    _ZyStackingTopology_Type()
)
zyStackingTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyStackingTopology.setStatus("current")
_ZyxelStackingTrapInfoObjects_ObjectIdentity = ObjectIdentity
zyxelStackingTrapInfoObjects = _ZyxelStackingTrapInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 3)
)
_ZyStackingTrapInfoMsg_Type = OctetString
_ZyStackingTrapInfoMsg_Object = MibScalar
zyStackingTrapInfoMsg = _ZyStackingTrapInfoMsg_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 3, 1),
    _ZyStackingTrapInfoMsg_Type()
)
zyStackingTrapInfoMsg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyStackingTrapInfoMsg.setStatus("current")
_ZyxelStackingNotifications_ObjectIdentity = ObjectIdentity
zyxelStackingNotifications = _ZyxelStackingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 4)
)

# Managed Objects groups


# Notification objects

zyStackingChannelUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 4, 1)
)
zyStackingChannelUp.setObjects(
      *(("ZYXEL-STACKING-MIB", "zyStackingSlotChannelInfoSlot"),
        ("ZYXEL-STACKING-MIB", "zyStackingSlotChannelInfoChannnel"))
)
if mibBuilder.loadTexts:
    zyStackingChannelUp.setStatus(
        "current"
    )

zyStackingChannelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 4, 2)
)
zyStackingChannelDown.setObjects(
      *(("ZYXEL-STACKING-MIB", "zyStackingSlotChannelInfoSlot"),
        ("ZYXEL-STACKING-MIB", "zyStackingSlotChannelInfoChannnel"))
)
if mibBuilder.loadTexts:
    zyStackingChannelDown.setStatus(
        "current"
    )

zyStackingSlotAttach = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 4, 3)
)
zyStackingSlotAttach.setObjects(
    ("ZYXEL-STACKING-MIB", "zyStackingSlotChannelInfoSlot")
)
if mibBuilder.loadTexts:
    zyStackingSlotAttach.setStatus(
        "current"
    )

zyStackingSlotDetach = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 4, 4)
)
zyStackingSlotDetach.setObjects(
    ("ZYXEL-STACKING-MIB", "zyStackingSlotChannelInfoSlot")
)
if mibBuilder.loadTexts:
    zyStackingSlotDetach.setStatus(
        "current"
    )

zyStackingNewMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 4, 5)
)
zyStackingNewMaster.setObjects(
    ("ZYXEL-STACKING-MIB", "zyStackingSlotChannelInfoSlot")
)
if mibBuilder.loadTexts:
    zyStackingNewMaster.setStatus(
        "current"
    )

zyStackingUpgradeFirmwareFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 4, 6)
)
zyStackingUpgradeFirmwareFail.setObjects(
    ("ZYXEL-STACKING-MIB", "zyStackingSlotChannelInfoSlot")
)
if mibBuilder.loadTexts:
    zyStackingUpgradeFirmwareFail.setStatus(
        "current"
    )

zyStackingNewBackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 4, 7)
)
zyStackingNewBackup.setObjects(
    ("ZYXEL-STACKING-MIB", "zyStackingSlotChannelInfoSlot")
)
if mibBuilder.loadTexts:
    zyStackingNewBackup.setStatus(
        "current"
    )

zyStackingBackupTakeover = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 4, 8)
)
zyStackingBackupTakeover.setObjects(
    ("ZYXEL-STACKING-MIB", "zyStackingSlotChannelInfoSlot")
)
if mibBuilder.loadTexts:
    zyStackingBackupTakeover.setStatus(
        "current"
    )

zyStackingNewMasterFromTakeover = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 4, 9)
)
zyStackingNewMasterFromTakeover.setObjects(
    ("ZYXEL-STACKING-MIB", "zyStackingSlotChannelInfoSlot")
)
if mibBuilder.loadTexts:
    zyStackingNewMasterFromTakeover.setStatus(
        "current"
    )

zyStackingSyncConfFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 4, 10)
)
zyStackingSyncConfFail.setObjects(
    ("ZYXEL-STACKING-MIB", "zyStackingSlotChannelInfoSlot")
)
if mibBuilder.loadTexts:
    zyStackingSyncConfFail.setStatus(
        "current"
    )

zyStackingSysRestoreConfFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 4, 11)
)
zyStackingSysRestoreConfFail.setObjects(
    ("ZYXEL-STACKING-MIB", "zyStackingSlotChannelInfoSlot")
)
if mibBuilder.loadTexts:
    zyStackingSysRestoreConfFail.setStatus(
        "current"
    )

zyStackingSlotInitFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 4, 12)
)
zyStackingSlotInitFail.setObjects(
    ("ZYXEL-STACKING-MIB", "zyStackingTrapInfoMsg")
)
if mibBuilder.loadTexts:
    zyStackingSlotInitFail.setStatus(
        "current"
    )

zyStackingSlotChangeIndex = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 4, 13)
)
zyStackingSlotChangeIndex.setObjects(
    ("ZYXEL-STACKING-MIB", "zyStackingTrapInfoMsg")
)
if mibBuilder.loadTexts:
    zyStackingSlotChangeIndex.setStatus(
        "current"
    )

zyStackingPriorityChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 4, 14)
)
zyStackingPriorityChange.setObjects(
    ("ZYXEL-STACKING-MIB", "zyStackingTrapInfoMsg")
)
if mibBuilder.loadTexts:
    zyStackingPriorityChange.setStatus(
        "current"
    )

zyStackingTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 97, 4, 15)
)
zyStackingTopologyChange.setObjects(
    ("ZYXEL-STACKING-MIB", "zyStackingTrapInfoMsg")
)
if mibBuilder.loadTexts:
    zyStackingTopologyChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-STACKING-MIB",
    **{"zyxelStacking": zyxelStacking,
       "zyxelStackingSetup": zyxelStackingSetup,
       "zyStackingPriority": zyStackingPriority,
       "zyStackingForceMasterModeState": zyStackingForceMasterModeState,
       "zyxelStackingSlotTable": zyxelStackingSlotTable,
       "zyxelStackingSlotEntry": zyxelStackingSlotEntry,
       "zyStackingSlotCurrentSlotId": zyStackingSlotCurrentSlotId,
       "zyStackingSlotActiveSlotIdAfterReboot": zyStackingSlotActiveSlotIdAfterReboot,
       "zyStackingSlotIdFreeze": zyStackingSlotIdFreeze,
       "zyxelStackingStatus": zyxelStackingStatus,
       "zyxelStackingSlotInfoTable": zyxelStackingSlotInfoTable,
       "zyxelStackingSlotInfoEntry": zyxelStackingSlotInfoEntry,
       "zyStackingSlotInfoSlot": zyStackingSlotInfoSlot,
       "zyStackingSlotInfoStackingStatus": zyStackingSlotInfoStackingStatus,
       "zyStackingSlotInfoForceMasterMode": zyStackingSlotInfoForceMasterMode,
       "zyStackingSlotInfoPriority": zyStackingSlotInfoPriority,
       "zyStackingSlotInfoRole": zyStackingSlotInfoRole,
       "zyStackingSlotInfoMacAddress": zyStackingSlotInfoMacAddress,
       "zyStackingSlotInfoUptime": zyStackingSlotInfoUptime,
       "zyStackingSlotInfoFirmwareVersionRunning": zyStackingSlotInfoFirmwareVersionRunning,
       "zyStackingSlotInfoFirmwareVersionFlash1": zyStackingSlotInfoFirmwareVersionFlash1,
       "zyStackingSlotInfoFirmwareVersionFlash2": zyStackingSlotInfoFirmwareVersionFlash2,
       "zyxelStackingSlotChannelInfoTable": zyxelStackingSlotChannelInfoTable,
       "zyxelStackingSlotChannelInfoEntry": zyxelStackingSlotChannelInfoEntry,
       "zyStackingSlotChannelInfoSlot": zyStackingSlotChannelInfoSlot,
       "zyStackingSlotChannelInfoChannnel": zyStackingSlotChannelInfoChannnel,
       "zyStackingSlotChannelInfoStatus": zyStackingSlotChannelInfoStatus,
       "zyStackingSlotChannelInfoPorts": zyStackingSlotChannelInfoPorts,
       "zyStackingSlotChannelInfoNeighbor": zyStackingSlotChannelInfoNeighbor,
       "zyStackingSlotChannelInfoSpeed": zyStackingSlotChannelInfoSpeed,
       "zyStackingTopology": zyStackingTopology,
       "zyxelStackingTrapInfoObjects": zyxelStackingTrapInfoObjects,
       "zyStackingTrapInfoMsg": zyStackingTrapInfoMsg,
       "zyxelStackingNotifications": zyxelStackingNotifications,
       "zyStackingChannelUp": zyStackingChannelUp,
       "zyStackingChannelDown": zyStackingChannelDown,
       "zyStackingSlotAttach": zyStackingSlotAttach,
       "zyStackingSlotDetach": zyStackingSlotDetach,
       "zyStackingNewMaster": zyStackingNewMaster,
       "zyStackingUpgradeFirmwareFail": zyStackingUpgradeFirmwareFail,
       "zyStackingNewBackup": zyStackingNewBackup,
       "zyStackingBackupTakeover": zyStackingBackupTakeover,
       "zyStackingNewMasterFromTakeover": zyStackingNewMasterFromTakeover,
       "zyStackingSyncConfFail": zyStackingSyncConfFail,
       "zyStackingSysRestoreConfFail": zyStackingSysRestoreConfFail,
       "zyStackingSlotInitFail": zyStackingSlotInitFail,
       "zyStackingSlotChangeIndex": zyStackingSlotChangeIndex,
       "zyStackingPriorityChange": zyStackingPriorityChange,
       "zyStackingTopologyChange": zyStackingTopologyChange}
)
