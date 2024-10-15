# SNMP MIB module (ES-MODULE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ES-MODULE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:40 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Grandjunction_ObjectIdentity = ObjectIdentity
grandjunction = _Grandjunction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437, 1)
)
_FastLink_ObjectIdentity = ObjectIdentity
fastLink = _FastLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437, 1, 1)
)
_SeriesG2xx_ObjectIdentity = ObjectIdentity
seriesG2xx = _SeriesG2xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2)
)
_EsModuleBasic_ObjectIdentity = ObjectIdentity
esModuleBasic = _EsModuleBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1)
)
_EsModuleBasicInfo_ObjectIdentity = ObjectIdentity
esModuleBasicInfo = _EsModuleBasicInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 1)
)
_EsModuleCapacity_Type = Integer32
_EsModuleCapacity_Object = MibScalar
esModuleCapacity = _EsModuleCapacity_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 1, 1),
    _EsModuleCapacity_Type()
)
esModuleCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModuleCapacity.setStatus("mandatory")
_EsModuleInfo_ObjectIdentity = ObjectIdentity
esModuleInfo = _EsModuleInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 2)
)
_EsModuleTable_Object = MibTable
esModuleTable = _EsModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    esModuleTable.setStatus("mandatory")
_EsModuleEntry_Object = MibTableRow
esModuleEntry = _EsModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 2, 1, 1)
)
esModuleEntry.setIndexNames(
    (0, "ES-MODULE-MIB", "esModuleIndex"),
)
if mibBuilder.loadTexts:
    esModuleEntry.setStatus("mandatory")
_EsModuleIndex_Type = Integer32
_EsModuleIndex_Object = MibTableColumn
esModuleIndex = _EsModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 2, 1, 1, 1),
    _EsModuleIndex_Type()
)
esModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModuleIndex.setStatus("mandatory")


class _EsModuleStatus_Type(Integer32):
    """Custom type esModuleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("disabled-mgmt", 2),
          ("disabled-no-vlan", 18),
          ("disabled-self-test", 14),
          ("disabled-violation", 7),
          ("enabled", 1),
          ("enabled-degraded", 15),
          ("reset", 11),
          ("suspended-atm-lane-down", 16),
          ("suspended-atm-network-down", 19),
          ("suspended-disl", 20),
          ("suspended-jabber", 4),
          ("suspended-linkbeat", 3),
          ("suspended-no-vlan", 17),
          ("suspended-not-present", 9),
          ("suspended-not-recognized", 10),
          ("suspended-ringdown", 12),
          ("suspended-stp", 13),
          ("suspended-violation", 5))
    )


_EsModuleStatus_Type.__name__ = "Integer32"
_EsModuleStatus_Object = MibTableColumn
esModuleStatus = _EsModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 2, 1, 1, 2),
    _EsModuleStatus_Type()
)
esModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModuleStatus.setStatus("mandatory")


class _EsModuleAdminStatus_Type(Integer32):
    """Custom type esModuleAdminStatus based on Integer32"""
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


_EsModuleAdminStatus_Type.__name__ = "Integer32"
_EsModuleAdminStatus_Object = MibTableColumn
esModuleAdminStatus = _EsModuleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 2, 1, 1, 3),
    _EsModuleAdminStatus_Type()
)
esModuleAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esModuleAdminStatus.setStatus("mandatory")


class _EsModuleDescr_Type(DisplayString):
    """Custom type esModuleDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EsModuleDescr_Type.__name__ = "DisplayString"
_EsModuleDescr_Object = MibTableColumn
esModuleDescr = _EsModuleDescr_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 2, 1, 1, 4),
    _EsModuleDescr_Type()
)
esModuleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModuleDescr.setStatus("mandatory")


class _EsModuleID_Type(DisplayString):
    """Custom type esModuleID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_EsModuleID_Type.__name__ = "DisplayString"
_EsModuleID_Object = MibTableColumn
esModuleID = _EsModuleID_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 2, 1, 1, 5),
    _EsModuleID_Type()
)
esModuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModuleID.setStatus("mandatory")
_EsModuleVersion_Type = Integer32
_EsModuleVersion_Object = MibTableColumn
esModuleVersion = _EsModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 2, 1, 1, 6),
    _EsModuleVersion_Type()
)
esModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModuleVersion.setStatus("mandatory")
_EsModuleObjectID_Type = ObjectIdentifier
_EsModuleObjectID_Object = MibTableColumn
esModuleObjectID = _EsModuleObjectID_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 2, 1, 1, 7),
    _EsModuleObjectID_Type()
)
esModuleObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModuleObjectID.setStatus("mandatory")
_EsModulePortCapacity_Type = Integer32
_EsModulePortCapacity_Object = MibTableColumn
esModulePortCapacity = _EsModulePortCapacity_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 2, 1, 1, 8),
    _EsModulePortCapacity_Type()
)
esModulePortCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModulePortCapacity.setStatus("mandatory")


class _EsModuleReset_Type(Integer32):
    """Custom type esModuleReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 2),
          ("reset", 1))
    )


_EsModuleReset_Type.__name__ = "Integer32"
_EsModuleReset_Object = MibTableColumn
esModuleReset = _EsModuleReset_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 2, 1, 1, 9),
    _EsModuleReset_Type()
)
esModuleReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esModuleReset.setStatus("mandatory")
_EsModuleLastStatusChange_Type = TimeTicks
_EsModuleLastStatusChange_Object = MibTableColumn
esModuleLastStatusChange = _EsModuleLastStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 2, 1, 1, 10),
    _EsModuleLastStatusChange_Type()
)
esModuleLastStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModuleLastStatusChange.setStatus("mandatory")
_EsModuleCollisionPeriods_Type = Counter32
_EsModuleCollisionPeriods_Object = MibTableColumn
esModuleCollisionPeriods = _EsModuleCollisionPeriods_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 2, 1, 1, 11),
    _EsModuleCollisionPeriods_Type()
)
esModuleCollisionPeriods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModuleCollisionPeriods.setStatus("mandatory")
_EsModuleLinkDisplayMap_Type = OctetString
_EsModuleLinkDisplayMap_Object = MibTableColumn
esModuleLinkDisplayMap = _EsModuleLinkDisplayMap_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 2, 1, 1, 12),
    _EsModuleLinkDisplayMap_Type()
)
esModuleLinkDisplayMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModuleLinkDisplayMap.setStatus("mandatory")
_EsModuleDisabledDisplayMap_Type = OctetString
_EsModuleDisabledDisplayMap_Object = MibTableColumn
esModuleDisabledDisplayMap = _EsModuleDisabledDisplayMap_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 2, 1, 1, 13),
    _EsModuleDisabledDisplayMap_Type()
)
esModuleDisabledDisplayMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModuleDisabledDisplayMap.setStatus("mandatory")


class _EsModuleBroadcastStormBlocked_Type(Integer32):
    """Custom type esModuleBroadcastStormBlocked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 2),
          ("notBlocked", 1))
    )


_EsModuleBroadcastStormBlocked_Type.__name__ = "Integer32"
_EsModuleBroadcastStormBlocked_Object = MibTableColumn
esModuleBroadcastStormBlocked = _EsModuleBroadcastStormBlocked_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 2, 1, 1, 14),
    _EsModuleBroadcastStormBlocked_Type()
)
esModuleBroadcastStormBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModuleBroadcastStormBlocked.setStatus("mandatory")


class _EsModuleFirmwareVersion_Type(DisplayString):
    """Custom type esModuleFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EsModuleFirmwareVersion_Type.__name__ = "DisplayString"
_EsModuleFirmwareVersion_Object = MibTableColumn
esModuleFirmwareVersion = _EsModuleFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 2, 1, 1, 15),
    _EsModuleFirmwareVersion_Type()
)
esModuleFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModuleFirmwareVersion.setStatus("mandatory")


class _EsModuleBOOTCodeVersion_Type(DisplayString):
    """Custom type esModuleBOOTCodeVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EsModuleBOOTCodeVersion_Type.__name__ = "DisplayString"
_EsModuleBOOTCodeVersion_Object = MibTableColumn
esModuleBOOTCodeVersion = _EsModuleBOOTCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 2, 1, 1, 16),
    _EsModuleBOOTCodeVersion_Type()
)
esModuleBOOTCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModuleBOOTCodeVersion.setStatus("mandatory")


class _EsModuleFlashStatus_Type(DisplayString):
    """Custom type esModuleFlashStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EsModuleFlashStatus_Type.__name__ = "DisplayString"
_EsModuleFlashStatus_Object = MibTableColumn
esModuleFlashStatus = _EsModuleFlashStatus_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 2, 1, 1, 17),
    _EsModuleFlashStatus_Type()
)
esModuleFlashStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModuleFlashStatus.setStatus("mandatory")


class _EsModuleResetToFactoryDefaults_Type(Integer32):
    """Custom type esModuleResetToFactoryDefaults based on Integer32"""
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


_EsModuleResetToFactoryDefaults_Type.__name__ = "Integer32"
_EsModuleResetToFactoryDefaults_Object = MibTableColumn
esModuleResetToFactoryDefaults = _EsModuleResetToFactoryDefaults_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 2, 1, 1, 18),
    _EsModuleResetToFactoryDefaults_Type()
)
esModuleResetToFactoryDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esModuleResetToFactoryDefaults.setStatus("mandatory")
_EsModuleSwPortIndex_Type = Integer32
_EsModuleSwPortIndex_Object = MibTableColumn
esModuleSwPortIndex = _EsModuleSwPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 2, 1, 1, 19),
    _EsModuleSwPortIndex_Type()
)
esModuleSwPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModuleSwPortIndex.setStatus("mandatory")
_EsModulePortInfo_ObjectIdentity = ObjectIdentity
esModulePortInfo = _EsModulePortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 3)
)
_EsModulePortTable_Object = MibTable
esModulePortTable = _EsModulePortTable_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    esModulePortTable.setStatus("mandatory")
_EsModulePortEntry_Object = MibTableRow
esModulePortEntry = _EsModulePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 3, 1, 1)
)
esModulePortEntry.setIndexNames(
    (0, "ES-MODULE-MIB", "esModuleSlotIndex"),
    (0, "ES-MODULE-MIB", "esModulePortIndex"),
)
if mibBuilder.loadTexts:
    esModulePortEntry.setStatus("mandatory")
_EsModuleSlotIndex_Type = Integer32
_EsModuleSlotIndex_Object = MibTableColumn
esModuleSlotIndex = _EsModuleSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 3, 1, 1, 1),
    _EsModuleSlotIndex_Type()
)
esModuleSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModuleSlotIndex.setStatus("mandatory")
_EsModulePortIndex_Type = Integer32
_EsModulePortIndex_Object = MibTableColumn
esModulePortIndex = _EsModulePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 3, 1, 1, 2),
    _EsModulePortIndex_Type()
)
esModulePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModulePortIndex.setStatus("mandatory")


class _EsModulePortDescr_Type(DisplayString):
    """Custom type esModulePortDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_EsModulePortDescr_Type.__name__ = "DisplayString"
_EsModulePortDescr_Object = MibTableColumn
esModulePortDescr = _EsModulePortDescr_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 3, 1, 1, 3),
    _EsModulePortDescr_Type()
)
esModulePortDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esModulePortDescr.setStatus("mandatory")


class _EsModulePortAdminStatus_Type(Integer32):
    """Custom type esModulePortAdminStatus based on Integer32"""
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


_EsModulePortAdminStatus_Type.__name__ = "Integer32"
_EsModulePortAdminStatus_Object = MibTableColumn
esModulePortAdminStatus = _EsModulePortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 3, 1, 1, 4),
    _EsModulePortAdminStatus_Type()
)
esModulePortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esModulePortAdminStatus.setStatus("mandatory")


class _EsModulePortAutoPartitionState_Type(Integer32):
    """Custom type esModulePortAutoPartitionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoPartitioned", 2),
          ("notAutoPartitioned", 1))
    )


_EsModulePortAutoPartitionState_Type.__name__ = "Integer32"
_EsModulePortAutoPartitionState_Object = MibTableColumn
esModulePortAutoPartitionState = _EsModulePortAutoPartitionState_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 3, 1, 1, 5),
    _EsModulePortAutoPartitionState_Type()
)
esModulePortAutoPartitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModulePortAutoPartitionState.setStatus("mandatory")


class _EsModulePortOperStatus_Type(Integer32):
    """Custom type esModulePortOperStatus based on Integer32"""
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
          ("suspended-not-present", 3))
    )


_EsModulePortOperStatus_Type.__name__ = "Integer32"
_EsModulePortOperStatus_Object = MibTableColumn
esModulePortOperStatus = _EsModulePortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 3, 1, 1, 6),
    _EsModulePortOperStatus_Type()
)
esModulePortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModulePortOperStatus.setStatus("mandatory")


class _EsModulePortLinkbeatStatus_Type(Integer32):
    """Custom type esModulePortLinkbeatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkbeat", 1),
          ("noLinkbeat", 2))
    )


_EsModulePortLinkbeatStatus_Type.__name__ = "Integer32"
_EsModulePortLinkbeatStatus_Object = MibTableColumn
esModulePortLinkbeatStatus = _EsModulePortLinkbeatStatus_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 3, 1, 1, 7),
    _EsModulePortLinkbeatStatus_Type()
)
esModulePortLinkbeatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModulePortLinkbeatStatus.setStatus("mandatory")


class _EsModulePortConnectorType_Type(Integer32):
    """Custom type esModulePortConnectorType based on Integer32"""
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
        *(("aui", 4),
          ("bnc", 3),
          ("empty", 7),
          ("fddi-mic", 8),
          ("fiber-sc", 5),
          ("fiber-st", 6),
          ("other", 1),
          ("rj45", 2))
    )


_EsModulePortConnectorType_Type.__name__ = "Integer32"
_EsModulePortConnectorType_Object = MibTableColumn
esModulePortConnectorType = _EsModulePortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 3, 1, 1, 8),
    _EsModulePortConnectorType_Type()
)
esModulePortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModulePortConnectorType.setStatus("mandatory")
_EsModulePortReceivePeriods_Type = Counter32
_EsModulePortReceivePeriods_Object = MibTableColumn
esModulePortReceivePeriods = _EsModulePortReceivePeriods_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1, 3, 1, 1, 9),
    _EsModulePortReceivePeriods_Type()
)
esModulePortReceivePeriods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModulePortReceivePeriods.setStatus("mandatory")
_EsModuleSpecific_ObjectIdentity = ObjectIdentity
esModuleSpecific = _EsModuleSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2)
)
_FmFDDIBasic_ObjectIdentity = ObjectIdentity
fmFDDIBasic = _FmFDDIBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1)
)
_FmFDDICfgInfo_ObjectIdentity = ObjectIdentity
fmFDDICfgInfo = _FmFDDICfgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 1)
)
_FmCfgTable_Object = MibTable
fmCfgTable = _FmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fmCfgTable.setStatus("mandatory")
_FmCfgEntry_Object = MibTableRow
fmCfgEntry = _FmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 1, 1, 1)
)
fmCfgEntry.setIndexNames(
    (0, "ES-MODULE-MIB", "fmCfgIndex"),
)
if mibBuilder.loadTexts:
    fmCfgEntry.setStatus("mandatory")
_FmCfgIndex_Type = Integer32
_FmCfgIndex_Object = MibTableColumn
fmCfgIndex = _FmCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 1, 1, 1, 1),
    _FmCfgIndex_Type()
)
fmCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmCfgIndex.setStatus("mandatory")


class _FmCfgFirmwareVersion_Type(DisplayString):
    """Custom type fmCfgFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_FmCfgFirmwareVersion_Type.__name__ = "DisplayString"
_FmCfgFirmwareVersion_Object = MibTableColumn
fmCfgFirmwareVersion = _FmCfgFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 1, 1, 1, 2),
    _FmCfgFirmwareVersion_Type()
)
fmCfgFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmCfgFirmwareVersion.setStatus("mandatory")


class _FmCfgBOOTCodeVersion_Type(DisplayString):
    """Custom type fmCfgBOOTCodeVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_FmCfgBOOTCodeVersion_Type.__name__ = "DisplayString"
_FmCfgBOOTCodeVersion_Object = MibTableColumn
fmCfgBOOTCodeVersion = _FmCfgBOOTCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 1, 1, 1, 3),
    _FmCfgBOOTCodeVersion_Type()
)
fmCfgBOOTCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmCfgBOOTCodeVersion.setStatus("mandatory")


class _FmCfgPOSTResult_Type(Integer32):
    """Custom type fmCfgPOSTResult based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("arbiter", 6),
          ("cpu", 3),
          ("dram", 5),
          ("ethernet", 8),
          ("fddi-mac", 9),
          ("fddi-phy-a", 10),
          ("fddi-phy-b", 11),
          ("flash", 4),
          ("noFailure", 1),
          ("packet-ram", 12),
          ("prom", 2),
          ("shared-ram", 7))
    )


_FmCfgPOSTResult_Type.__name__ = "Integer32"
_FmCfgPOSTResult_Object = MibTableColumn
fmCfgPOSTResult = _FmCfgPOSTResult_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 1, 1, 1, 4),
    _FmCfgPOSTResult_Type()
)
fmCfgPOSTResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmCfgPOSTResult.setStatus("mandatory")


class _FmCfgPOSTTest_Type(Integer32):
    """Custom type fmCfgPOSTTest based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("arbiter-id", 7),
          ("checkerboard", 6),
          ("checksum", 3),
          ("ethernet-interrupt", 10),
          ("invalid-marker", 2),
          ("invalid-version", 12),
          ("loopback", 11),
          ("noFailure", 1),
          ("ram-byte-test", 5),
          ("ram-quick-scan", 4),
          ("read-only-register", 8),
          ("read-write-register", 9))
    )


_FmCfgPOSTTest_Type.__name__ = "Integer32"
_FmCfgPOSTTest_Object = MibTableColumn
fmCfgPOSTTest = _FmCfgPOSTTest_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 1, 1, 1, 5),
    _FmCfgPOSTTest_Type()
)
fmCfgPOSTTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmCfgPOSTTest.setStatus("mandatory")


class _FmCfgPOSTLoopbackResult_Type(Integer32):
    """Custom type fmCfgPOSTLoopbackResult based on Integer32"""
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
        *(("buffer-error", 7),
          ("cannot-transmit", 2),
          ("data-mismatch", 4),
          ("length-mismatch", 5),
          ("noFailure", 1),
          ("receive-timeout", 3),
          ("receiver-error", 6))
    )


_FmCfgPOSTLoopbackResult_Type.__name__ = "Integer32"
_FmCfgPOSTLoopbackResult_Object = MibTableColumn
fmCfgPOSTLoopbackResult = _FmCfgPOSTLoopbackResult_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 1, 1, 1, 6),
    _FmCfgPOSTLoopbackResult_Type()
)
fmCfgPOSTLoopbackResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmCfgPOSTLoopbackResult.setStatus("mandatory")


class _FmCfgFlashStatus_Type(DisplayString):
    """Custom type fmCfgFlashStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FmCfgFlashStatus_Type.__name__ = "DisplayString"
_FmCfgFlashStatus_Object = MibTableColumn
fmCfgFlashStatus = _FmCfgFlashStatus_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 1, 1, 1, 7),
    _FmCfgFlashStatus_Type()
)
fmCfgFlashStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmCfgFlashStatus.setStatus("mandatory")


class _FmCfgResetToFactoryDefaults_Type(Integer32):
    """Custom type fmCfgResetToFactoryDefaults based on Integer32"""
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


_FmCfgResetToFactoryDefaults_Type.__name__ = "Integer32"
_FmCfgResetToFactoryDefaults_Object = MibTableColumn
fmCfgResetToFactoryDefaults = _FmCfgResetToFactoryDefaults_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 1, 1, 1, 8),
    _FmCfgResetToFactoryDefaults_Type()
)
fmCfgResetToFactoryDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmCfgResetToFactoryDefaults.setStatus("mandatory")


class _FmCfgResetModule_Type(Integer32):
    """Custom type fmCfgResetModule based on Integer32"""
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


_FmCfgResetModule_Type.__name__ = "Integer32"
_FmCfgResetModule_Object = MibTableColumn
fmCfgResetModule = _FmCfgResetModule_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 1, 1, 1, 9),
    _FmCfgResetModule_Type()
)
fmCfgResetModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmCfgResetModule.setStatus("mandatory")


class _FmCfgNovellFDDISNAPTranslation_Type(Integer32):
    """Custom type fmCfgNovellFDDISNAPTranslation based on Integer32"""
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
        *(("automatic", 1),
          ("drop", 5),
          ("ethernet-8023", 2),
          ("ethernet-II", 4),
          ("ethernet-SNAP", 3))
    )


_FmCfgNovellFDDISNAPTranslation_Type.__name__ = "Integer32"
_FmCfgNovellFDDISNAPTranslation_Object = MibTableColumn
fmCfgNovellFDDISNAPTranslation = _FmCfgNovellFDDISNAPTranslation_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 1, 1, 1, 10),
    _FmCfgNovellFDDISNAPTranslation_Type()
)
fmCfgNovellFDDISNAPTranslation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmCfgNovellFDDISNAPTranslation.setStatus("mandatory")


class _FmCfgUnmatchedSNAPDestination_Type(Integer32):
    """Custom type fmCfgUnmatchedSNAPDestination based on Integer32"""
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
        *(("all", 1),
          ("drop", 5),
          ("ethernet-8023", 2),
          ("ethernet-II", 4),
          ("ethernet-SNAP", 3))
    )


_FmCfgUnmatchedSNAPDestination_Type.__name__ = "Integer32"
_FmCfgUnmatchedSNAPDestination_Object = MibTableColumn
fmCfgUnmatchedSNAPDestination = _FmCfgUnmatchedSNAPDestination_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 1, 1, 1, 11),
    _FmCfgUnmatchedSNAPDestination_Type()
)
fmCfgUnmatchedSNAPDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmCfgUnmatchedSNAPDestination.setStatus("mandatory")


class _FmCfgAuthorizationChecking_Type(Integer32):
    """Custom type fmCfgAuthorizationChecking based on Integer32"""
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


_FmCfgAuthorizationChecking_Type.__name__ = "Integer32"
_FmCfgAuthorizationChecking_Object = MibTableColumn
fmCfgAuthorizationChecking = _FmCfgAuthorizationChecking_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 1, 1, 1, 12),
    _FmCfgAuthorizationChecking_Type()
)
fmCfgAuthorizationChecking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmCfgAuthorizationChecking.setStatus("mandatory")


class _FmCfgAuthorizationString_Type(DisplayString):
    """Custom type fmCfgAuthorizationString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FmCfgAuthorizationString_Type.__name__ = "DisplayString"
_FmCfgAuthorizationString_Object = MibTableColumn
fmCfgAuthorizationString = _FmCfgAuthorizationString_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 1, 1, 1, 13),
    _FmCfgAuthorizationString_Type()
)
fmCfgAuthorizationString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmCfgAuthorizationString.setStatus("mandatory")
_FmFDDIXlateToEthInfo_ObjectIdentity = ObjectIdentity
fmFDDIXlateToEthInfo = _FmFDDIXlateToEthInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 2)
)
_FmXlateToEthTable_Object = MibTable
fmXlateToEthTable = _FmXlateToEthTable_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fmXlateToEthTable.setStatus("mandatory")
_FmXlateToEthEntry_Object = MibTableRow
fmXlateToEthEntry = _FmXlateToEthEntry_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 2, 1, 1)
)
fmXlateToEthEntry.setIndexNames(
    (0, "ES-MODULE-MIB", "fmXlateToEthIndex"),
)
if mibBuilder.loadTexts:
    fmXlateToEthEntry.setStatus("mandatory")
_FmXlateToEthIndex_Type = Integer32
_FmXlateToEthIndex_Object = MibTableColumn
fmXlateToEthIndex = _FmXlateToEthIndex_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 2, 1, 1, 1),
    _FmXlateToEthIndex_Type()
)
fmXlateToEthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmXlateToEthIndex.setStatus("mandatory")
_FmXlateToEthNovellSnapToRaw8023Frames_Type = Counter32
_FmXlateToEthNovellSnapToRaw8023Frames_Object = MibTableColumn
fmXlateToEthNovellSnapToRaw8023Frames = _FmXlateToEthNovellSnapToRaw8023Frames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 2, 1, 1, 2),
    _FmXlateToEthNovellSnapToRaw8023Frames_Type()
)
fmXlateToEthNovellSnapToRaw8023Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmXlateToEthNovellSnapToRaw8023Frames.setStatus("mandatory")
_FmXlateToEthNovellSnapToEthIIFrames_Type = Counter32
_FmXlateToEthNovellSnapToEthIIFrames_Object = MibTableColumn
fmXlateToEthNovellSnapToEthIIFrames = _FmXlateToEthNovellSnapToEthIIFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 2, 1, 1, 3),
    _FmXlateToEthNovellSnapToEthIIFrames_Type()
)
fmXlateToEthNovellSnapToEthIIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmXlateToEthNovellSnapToEthIIFrames.setStatus("mandatory")
_FmXlateToEthNovellSnapToSnapFrames_Type = Counter32
_FmXlateToEthNovellSnapToSnapFrames_Object = MibTableColumn
fmXlateToEthNovellSnapToSnapFrames = _FmXlateToEthNovellSnapToSnapFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 2, 1, 1, 4),
    _FmXlateToEthNovellSnapToSnapFrames_Type()
)
fmXlateToEthNovellSnapToSnapFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmXlateToEthNovellSnapToSnapFrames.setStatus("mandatory")
_FmXlateToEthAppleTalkSnapToSnapFrames_Type = Counter32
_FmXlateToEthAppleTalkSnapToSnapFrames_Object = MibTableColumn
fmXlateToEthAppleTalkSnapToSnapFrames = _FmXlateToEthAppleTalkSnapToSnapFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 2, 1, 1, 5),
    _FmXlateToEthAppleTalkSnapToSnapFrames_Type()
)
fmXlateToEthAppleTalkSnapToSnapFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmXlateToEthAppleTalkSnapToSnapFrames.setStatus("mandatory")
_FmXlateToEthIpSnapForFragmentationFrames_Type = Counter32
_FmXlateToEthIpSnapForFragmentationFrames_Object = MibTableColumn
fmXlateToEthIpSnapForFragmentationFrames = _FmXlateToEthIpSnapForFragmentationFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 2, 1, 1, 6),
    _FmXlateToEthIpSnapForFragmentationFrames_Type()
)
fmXlateToEthIpSnapForFragmentationFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmXlateToEthIpSnapForFragmentationFrames.setStatus("mandatory")
_FmXlateToEthIpSnapFragmentedFrames_Type = Counter32
_FmXlateToEthIpSnapFragmentedFrames_Object = MibTableColumn
fmXlateToEthIpSnapFragmentedFrames = _FmXlateToEthIpSnapFragmentedFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 2, 1, 1, 7),
    _FmXlateToEthIpSnapFragmentedFrames_Type()
)
fmXlateToEthIpSnapFragmentedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmXlateToEthIpSnapFragmentedFrames.setStatus("mandatory")
_FmXlateToEthBridgeTunnelToEthIIFrames_Type = Counter32
_FmXlateToEthBridgeTunnelToEthIIFrames_Object = MibTableColumn
fmXlateToEthBridgeTunnelToEthIIFrames = _FmXlateToEthBridgeTunnelToEthIIFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 2, 1, 1, 8),
    _FmXlateToEthBridgeTunnelToEthIIFrames_Type()
)
fmXlateToEthBridgeTunnelToEthIIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmXlateToEthBridgeTunnelToEthIIFrames.setStatus("mandatory")
_FmXlateToEthOtherSnapToEthIIFrames_Type = Counter32
_FmXlateToEthOtherSnapToEthIIFrames_Object = MibTableColumn
fmXlateToEthOtherSnapToEthIIFrames = _FmXlateToEthOtherSnapToEthIIFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 2, 1, 1, 9),
    _FmXlateToEthOtherSnapToEthIIFrames_Type()
)
fmXlateToEthOtherSnapToEthIIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmXlateToEthOtherSnapToEthIIFrames.setStatus("mandatory")
_FmXlateToEthOtherSnapToSnapFrames_Type = Counter32
_FmXlateToEthOtherSnapToSnapFrames_Object = MibTableColumn
fmXlateToEthOtherSnapToSnapFrames = _FmXlateToEthOtherSnapToSnapFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 2, 1, 1, 10),
    _FmXlateToEthOtherSnapToSnapFrames_Type()
)
fmXlateToEthOtherSnapToSnapFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmXlateToEthOtherSnapToSnapFrames.setStatus("mandatory")
_FmXlateToEth8022To8022Frames_Type = Counter32
_FmXlateToEth8022To8022Frames_Object = MibTableColumn
fmXlateToEth8022To8022Frames = _FmXlateToEth8022To8022Frames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 2, 1, 1, 11),
    _FmXlateToEth8022To8022Frames_Type()
)
fmXlateToEth8022To8022Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmXlateToEth8022To8022Frames.setStatus("mandatory")
_FmFDDIXlateToFDDIInfo_ObjectIdentity = ObjectIdentity
fmFDDIXlateToFDDIInfo = _FmFDDIXlateToFDDIInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 3)
)
_FmXlateToFDDITable_Object = MibTable
fmXlateToFDDITable = _FmXlateToFDDITable_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fmXlateToFDDITable.setStatus("mandatory")
_FmXlateToFDDIEntry_Object = MibTableRow
fmXlateToFDDIEntry = _FmXlateToFDDIEntry_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 3, 1, 1)
)
fmXlateToFDDIEntry.setIndexNames(
    (0, "ES-MODULE-MIB", "fmXlateToFDDIIndex"),
)
if mibBuilder.loadTexts:
    fmXlateToFDDIEntry.setStatus("mandatory")
_FmXlateToFDDIIndex_Type = Integer32
_FmXlateToFDDIIndex_Object = MibTableColumn
fmXlateToFDDIIndex = _FmXlateToFDDIIndex_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 3, 1, 1, 1),
    _FmXlateToFDDIIndex_Type()
)
fmXlateToFDDIIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmXlateToFDDIIndex.setStatus("mandatory")
_FmXlateToFDDINovellRaw8023ToSnapFrames_Type = Counter32
_FmXlateToFDDINovellRaw8023ToSnapFrames_Object = MibTableColumn
fmXlateToFDDINovellRaw8023ToSnapFrames = _FmXlateToFDDINovellRaw8023ToSnapFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 3, 1, 1, 2),
    _FmXlateToFDDINovellRaw8023ToSnapFrames_Type()
)
fmXlateToFDDINovellRaw8023ToSnapFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmXlateToFDDINovellRaw8023ToSnapFrames.setStatus("mandatory")
_FmXlateToFDDINovellEthIIToSnapFrames_Type = Counter32
_FmXlateToFDDINovellEthIIToSnapFrames_Object = MibTableColumn
fmXlateToFDDINovellEthIIToSnapFrames = _FmXlateToFDDINovellEthIIToSnapFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 3, 1, 1, 3),
    _FmXlateToFDDINovellEthIIToSnapFrames_Type()
)
fmXlateToFDDINovellEthIIToSnapFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmXlateToFDDINovellEthIIToSnapFrames.setStatus("mandatory")
_FmXlateToFDDINovellSnapToSnapFrames_Type = Counter32
_FmXlateToFDDINovellSnapToSnapFrames_Object = MibTableColumn
fmXlateToFDDINovellSnapToSnapFrames = _FmXlateToFDDINovellSnapToSnapFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 3, 1, 1, 4),
    _FmXlateToFDDINovellSnapToSnapFrames_Type()
)
fmXlateToFDDINovellSnapToSnapFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmXlateToFDDINovellSnapToSnapFrames.setStatus("mandatory")
_FmXlateToFDDIEthIIToBridgeTunnelFrames_Type = Counter32
_FmXlateToFDDIEthIIToBridgeTunnelFrames_Object = MibTableColumn
fmXlateToFDDIEthIIToBridgeTunnelFrames = _FmXlateToFDDIEthIIToBridgeTunnelFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 3, 1, 1, 5),
    _FmXlateToFDDIEthIIToBridgeTunnelFrames_Type()
)
fmXlateToFDDIEthIIToBridgeTunnelFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmXlateToFDDIEthIIToBridgeTunnelFrames.setStatus("mandatory")
_FmXlateToFDDIEthIIToSnapFrames_Type = Counter32
_FmXlateToFDDIEthIIToSnapFrames_Object = MibTableColumn
fmXlateToFDDIEthIIToSnapFrames = _FmXlateToFDDIEthIIToSnapFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 3, 1, 1, 6),
    _FmXlateToFDDIEthIIToSnapFrames_Type()
)
fmXlateToFDDIEthIIToSnapFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmXlateToFDDIEthIIToSnapFrames.setStatus("mandatory")
_FmXlateToFDDIOtherSnapToSnapFrames_Type = Counter32
_FmXlateToFDDIOtherSnapToSnapFrames_Object = MibTableColumn
fmXlateToFDDIOtherSnapToSnapFrames = _FmXlateToFDDIOtherSnapToSnapFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 3, 1, 1, 7),
    _FmXlateToFDDIOtherSnapToSnapFrames_Type()
)
fmXlateToFDDIOtherSnapToSnapFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmXlateToFDDIOtherSnapToSnapFrames.setStatus("mandatory")
_FmXlateToFDDI8022To8022Frames_Type = Counter32
_FmXlateToFDDI8022To8022Frames_Object = MibTableColumn
fmXlateToFDDI8022To8022Frames = _FmXlateToFDDI8022To8022Frames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 3, 1, 1, 8),
    _FmXlateToFDDI8022To8022Frames_Type()
)
fmXlateToFDDI8022To8022Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmXlateToFDDI8022To8022Frames.setStatus("mandatory")
_FmFDDIFilterInfo_ObjectIdentity = ObjectIdentity
fmFDDIFilterInfo = _FmFDDIFilterInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 4)
)
_FmFilterTable_Object = MibTable
fmFilterTable = _FmFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    fmFilterTable.setStatus("mandatory")
_FmFilterEntry_Object = MibTableRow
fmFilterEntry = _FmFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 4, 1, 1)
)
fmFilterEntry.setIndexNames(
    (0, "ES-MODULE-MIB", "fmFilterIndex"),
)
if mibBuilder.loadTexts:
    fmFilterEntry.setStatus("mandatory")
_FmFilterIndex_Type = Integer32
_FmFilterIndex_Object = MibTableColumn
fmFilterIndex = _FmFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 4, 1, 1, 1),
    _FmFilterIndex_Type()
)
fmFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmFilterIndex.setStatus("mandatory")
_FmFilterFcsInvalidFrames_Type = Counter32
_FmFilterFcsInvalidFrames_Object = MibTableColumn
fmFilterFcsInvalidFrames = _FmFilterFcsInvalidFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 4, 1, 1, 2),
    _FmFilterFcsInvalidFrames_Type()
)
fmFilterFcsInvalidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmFilterFcsInvalidFrames.setStatus("mandatory")
_FmFilterDataLengthFrames_Type = Counter32
_FmFilterDataLengthFrames_Object = MibTableColumn
fmFilterDataLengthFrames = _FmFilterDataLengthFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 4, 1, 1, 3),
    _FmFilterDataLengthFrames_Type()
)
fmFilterDataLengthFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmFilterDataLengthFrames.setStatus("mandatory")
_FmFilterErrorIndFrames_Type = Counter32
_FmFilterErrorIndFrames_Object = MibTableColumn
fmFilterErrorIndFrames = _FmFilterErrorIndFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 4, 1, 1, 4),
    _FmFilterErrorIndFrames_Type()
)
fmFilterErrorIndFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmFilterErrorIndFrames.setStatus("mandatory")
_FmFilterFddiFifoOverrunFrames_Type = Counter32
_FmFilterFddiFifoOverrunFrames_Object = MibTableColumn
fmFilterFddiFifoOverrunFrames = _FmFilterFddiFifoOverrunFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 4, 1, 1, 5),
    _FmFilterFddiFifoOverrunFrames_Type()
)
fmFilterFddiFifoOverrunFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmFilterFddiFifoOverrunFrames.setStatus("mandatory")
_FmFilterFddiInternalErrorFrames_Type = Counter32
_FmFilterFddiInternalErrorFrames_Object = MibTableColumn
fmFilterFddiInternalErrorFrames = _FmFilterFddiInternalErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 4, 1, 1, 6),
    _FmFilterFddiInternalErrorFrames_Type()
)
fmFilterFddiInternalErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmFilterFddiInternalErrorFrames.setStatus("mandatory")
_FmFilterNoBufferSpaceFrames_Type = Counter32
_FmFilterNoBufferSpaceFrames_Object = MibTableColumn
fmFilterNoBufferSpaceFrames = _FmFilterNoBufferSpaceFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 4, 1, 1, 7),
    _FmFilterNoBufferSpaceFrames_Type()
)
fmFilterNoBufferSpaceFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmFilterNoBufferSpaceFrames.setStatus("mandatory")
_FmFilterNoEndDelimitFrames_Type = Counter32
_FmFilterNoEndDelimitFrames_Object = MibTableColumn
fmFilterNoEndDelimitFrames = _FmFilterNoEndDelimitFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 4, 1, 1, 8),
    _FmFilterNoEndDelimitFrames_Type()
)
fmFilterNoEndDelimitFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmFilterNoEndDelimitFrames.setStatus("mandatory")
_FmFilterNoLlcHeaderFrames_Type = Counter32
_FmFilterNoLlcHeaderFrames_Object = MibTableColumn
fmFilterNoLlcHeaderFrames = _FmFilterNoLlcHeaderFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 4, 1, 1, 9),
    _FmFilterNoLlcHeaderFrames_Type()
)
fmFilterNoLlcHeaderFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmFilterNoLlcHeaderFrames.setStatus("mandatory")
_FmFilterSourceRouteFrames_Type = Counter32
_FmFilterSourceRouteFrames_Object = MibTableColumn
fmFilterSourceRouteFrames = _FmFilterSourceRouteFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 4, 1, 1, 10),
    _FmFilterSourceRouteFrames_Type()
)
fmFilterSourceRouteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmFilterSourceRouteFrames.setStatus("mandatory")
_FmFilterNoSnapHeaderFrames_Type = Counter32
_FmFilterNoSnapHeaderFrames_Object = MibTableColumn
fmFilterNoSnapHeaderFrames = _FmFilterNoSnapHeaderFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 4, 1, 1, 11),
    _FmFilterNoSnapHeaderFrames_Type()
)
fmFilterNoSnapHeaderFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmFilterNoSnapHeaderFrames.setStatus("mandatory")
_FmFilterTooLargeFrames_Type = Counter32
_FmFilterTooLargeFrames_Object = MibTableColumn
fmFilterTooLargeFrames = _FmFilterTooLargeFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 4, 1, 1, 12),
    _FmFilterTooLargeFrames_Type()
)
fmFilterTooLargeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmFilterTooLargeFrames.setStatus("mandatory")
_FmFilterNovellSnapFilteredFrames_Type = Counter32
_FmFilterNovellSnapFilteredFrames_Object = MibTableColumn
fmFilterNovellSnapFilteredFrames = _FmFilterNovellSnapFilteredFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 4, 1, 1, 13),
    _FmFilterNovellSnapFilteredFrames_Type()
)
fmFilterNovellSnapFilteredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmFilterNovellSnapFilteredFrames.setStatus("mandatory")
_FmFilterCantFragmentFrames_Type = Counter32
_FmFilterCantFragmentFrames_Object = MibTableColumn
fmFilterCantFragmentFrames = _FmFilterCantFragmentFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 4, 1, 1, 14),
    _FmFilterCantFragmentFrames_Type()
)
fmFilterCantFragmentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmFilterCantFragmentFrames.setStatus("mandatory")
_FmFilterBadIpHeaderFrames_Type = Counter32
_FmFilterBadIpHeaderFrames_Object = MibTableColumn
fmFilterBadIpHeaderFrames = _FmFilterBadIpHeaderFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 4, 1, 1, 15),
    _FmFilterBadIpHeaderFrames_Type()
)
fmFilterBadIpHeaderFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmFilterBadIpHeaderFrames.setStatus("mandatory")
_FmFilterRingDownDiscards_Type = Counter32
_FmFilterRingDownDiscards_Object = MibTableColumn
fmFilterRingDownDiscards = _FmFilterRingDownDiscards_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 4, 1, 1, 16),
    _FmFilterRingDownDiscards_Type()
)
fmFilterRingDownDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmFilterRingDownDiscards.setStatus("mandatory")
_FmFilterNovellOtherFilteredFrames_Type = Counter32
_FmFilterNovellOtherFilteredFrames_Object = MibTableColumn
fmFilterNovellOtherFilteredFrames = _FmFilterNovellOtherFilteredFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 1, 4, 1, 1, 17),
    _FmFilterNovellOtherFilteredFrames_Type()
)
fmFilterNovellOtherFilteredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmFilterNovellOtherFilteredFrames.setStatus("mandatory")
_FmAtmBasic_ObjectIdentity = ObjectIdentity
fmAtmBasic = _FmAtmBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 2)
)
_FmAtmCfgInfo_ObjectIdentity = ObjectIdentity
fmAtmCfgInfo = _FmAtmCfgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 2, 1)
)
_FmAtmCfgTable_Object = MibTable
fmAtmCfgTable = _FmAtmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fmAtmCfgTable.setStatus("mandatory")
_FmAtmCfgEntry_Object = MibTableRow
fmAtmCfgEntry = _FmAtmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 2, 1, 1, 1)
)
fmAtmCfgEntry.setIndexNames(
    (0, "ES-MODULE-MIB", "fmAtmCfgIndex"),
)
if mibBuilder.loadTexts:
    fmAtmCfgEntry.setStatus("mandatory")
_FmAtmCfgIndex_Type = Integer32
_FmAtmCfgIndex_Object = MibTableColumn
fmAtmCfgIndex = _FmAtmCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 2, 1, 1, 1, 1),
    _FmAtmCfgIndex_Type()
)
fmAtmCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAtmCfgIndex.setStatus("mandatory")


class _FmAtmCfgPOSTResult_Type(Integer32):
    """Custom type fmAtmCfgPOSTResult based on Integer32"""
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
        *(("ethernet-controller", 7),
          ("flash", 13),
          ("fpga", 4),
          ("framer", 10),
          ("host-interface", 6),
          ("no-failure", 3),
          ("other", 1),
          ("sar-controller", 8),
          ("sar-memory", 9),
          ("shared-memory", 5),
          ("traffic-co-processor", 11),
          ("traffic-co-processor-memory", 12),
          ("unknown", 2))
    )


_FmAtmCfgPOSTResult_Type.__name__ = "Integer32"
_FmAtmCfgPOSTResult_Object = MibTableColumn
fmAtmCfgPOSTResult = _FmAtmCfgPOSTResult_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 2, 1, 1, 1, 2),
    _FmAtmCfgPOSTResult_Type()
)
fmAtmCfgPOSTResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAtmCfgPOSTResult.setStatus("mandatory")


class _FmAtmCfgPOSTTest_Type(Integer32):
    """Custom type fmAtmCfgPOSTTest based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("byte-pattern", 7),
          ("checkerboard", 8),
          ("checksum", 13),
          ("control-memory", 12),
          ("data-mismatch", 10),
          ("host-loopback", 19),
          ("host-to-module-interrupt", 21),
          ("interrupt", 11),
          ("local-loopback", 18),
          ("module-to-host-interrupt", 20),
          ("no-failure", 3),
          ("no-response", 9),
          ("other", 1),
          ("quick-scan-byte", 6),
          ("quick-scan-word", 5),
          ("read-only-configuration-register", 14),
          ("read-only-register", 16),
          ("read-write-configuration-register", 15),
          ("read-write-register", 17),
          ("refresh", 4),
          ("unknown", 2))
    )


_FmAtmCfgPOSTTest_Type.__name__ = "Integer32"
_FmAtmCfgPOSTTest_Object = MibTableColumn
fmAtmCfgPOSTTest = _FmAtmCfgPOSTTest_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 2, 1, 1, 1, 3),
    _FmAtmCfgPOSTTest_Type()
)
fmAtmCfgPOSTTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAtmCfgPOSTTest.setStatus("mandatory")


class _FmAtmCfgPOSTLoopbackResult_Type(Integer32):
    """Custom type fmAtmCfgPOSTLoopbackResult based on Integer32"""
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
        *(("buffer-error", 9),
          ("cannot-transmit", 4),
          ("data-mismatch", 6),
          ("length-mismatch", 7),
          ("no-failure", 3),
          ("other", 1),
          ("receive-timeout", 5),
          ("receiver-error", 8),
          ("unknown", 2))
    )


_FmAtmCfgPOSTLoopbackResult_Type.__name__ = "Integer32"
_FmAtmCfgPOSTLoopbackResult_Object = MibTableColumn
fmAtmCfgPOSTLoopbackResult = _FmAtmCfgPOSTLoopbackResult_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 2, 1, 1, 1, 4),
    _FmAtmCfgPOSTLoopbackResult_Type()
)
fmAtmCfgPOSTLoopbackResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAtmCfgPOSTLoopbackResult.setStatus("mandatory")


class _FmAtmCfgFramingMode_Type(Integer32):
    """Custom type fmAtmCfgFramingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stm-1", 2),
          ("sts-3c", 1))
    )


_FmAtmCfgFramingMode_Type.__name__ = "Integer32"
_FmAtmCfgFramingMode_Object = MibTableColumn
fmAtmCfgFramingMode = _FmAtmCfgFramingMode_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 2, 1, 1, 1, 5),
    _FmAtmCfgFramingMode_Type()
)
fmAtmCfgFramingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAtmCfgFramingMode.setStatus("mandatory")
_FmAtmStatsInfo_ObjectIdentity = ObjectIdentity
fmAtmStatsInfo = _FmAtmStatsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 2, 2)
)
_FmAtmRxStatTable_Object = MibTable
fmAtmRxStatTable = _FmAtmRxStatTable_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fmAtmRxStatTable.setStatus("mandatory")
_FmAtmRxStatEntry_Object = MibTableRow
fmAtmRxStatEntry = _FmAtmRxStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 2, 2, 1, 1)
)
fmAtmRxStatEntry.setIndexNames(
    (0, "ES-MODULE-MIB", "fmAtmRxStatIndex"),
)
if mibBuilder.loadTexts:
    fmAtmRxStatEntry.setStatus("mandatory")
_FmAtmRxStatIndex_Type = Integer32
_FmAtmRxStatIndex_Object = MibTableColumn
fmAtmRxStatIndex = _FmAtmRxStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 2, 2, 1, 1, 1),
    _FmAtmRxStatIndex_Type()
)
fmAtmRxStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAtmRxStatIndex.setStatus("mandatory")
_FmAtmRxControlFrames_Type = Counter32
_FmAtmRxControlFrames_Object = MibTableColumn
fmAtmRxControlFrames = _FmAtmRxControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 2, 2, 1, 1, 2),
    _FmAtmRxControlFrames_Type()
)
fmAtmRxControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAtmRxControlFrames.setStatus("mandatory")
_FmAtmRxLocalLecFrames_Type = Counter32
_FmAtmRxLocalLecFrames_Object = MibTableColumn
fmAtmRxLocalLecFrames = _FmAtmRxLocalLecFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 2, 2, 1, 1, 3),
    _FmAtmRxLocalLecFrames_Type()
)
fmAtmRxLocalLecFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAtmRxLocalLecFrames.setStatus("mandatory")
_FmAtmRxNoBufferDiscards_Type = Counter32
_FmAtmRxNoBufferDiscards_Object = MibTableColumn
fmAtmRxNoBufferDiscards = _FmAtmRxNoBufferDiscards_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 2, 2, 1, 1, 4),
    _FmAtmRxNoBufferDiscards_Type()
)
fmAtmRxNoBufferDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAtmRxNoBufferDiscards.setStatus("mandatory")
_FmAtmRxCRCErrors_Type = Counter32
_FmAtmRxCRCErrors_Object = MibTableColumn
fmAtmRxCRCErrors = _FmAtmRxCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 2, 2, 1, 1, 5),
    _FmAtmRxCRCErrors_Type()
)
fmAtmRxCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAtmRxCRCErrors.setStatus("mandatory")
_FmAtmRxFrameTooLongs_Type = Counter32
_FmAtmRxFrameTooLongs_Object = MibTableColumn
fmAtmRxFrameTooLongs = _FmAtmRxFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 2, 2, 1, 1, 6),
    _FmAtmRxFrameTooLongs_Type()
)
fmAtmRxFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAtmRxFrameTooLongs.setStatus("mandatory")
_FmAtmRxOtherDiscards_Type = Counter32
_FmAtmRxOtherDiscards_Object = MibTableColumn
fmAtmRxOtherDiscards = _FmAtmRxOtherDiscards_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 2, 2, 1, 1, 7),
    _FmAtmRxOtherDiscards_Type()
)
fmAtmRxOtherDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAtmRxOtherDiscards.setStatus("mandatory")
_FmAtmRxHecCellErrors_Type = Counter32
_FmAtmRxHecCellErrors_Object = MibTableColumn
fmAtmRxHecCellErrors = _FmAtmRxHecCellErrors_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 2, 2, 2, 1, 1, 8),
    _FmAtmRxHecCellErrors_Type()
)
fmAtmRxHecCellErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAtmRxHecCellErrors.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ES-MODULE-MIB",
    **{"grandjunction": grandjunction,
       "products": products,
       "fastLink": fastLink,
       "seriesG2xx": seriesG2xx,
       "esModuleBasic": esModuleBasic,
       "esModuleBasicInfo": esModuleBasicInfo,
       "esModuleCapacity": esModuleCapacity,
       "esModuleInfo": esModuleInfo,
       "esModuleTable": esModuleTable,
       "esModuleEntry": esModuleEntry,
       "esModuleIndex": esModuleIndex,
       "esModuleStatus": esModuleStatus,
       "esModuleAdminStatus": esModuleAdminStatus,
       "esModuleDescr": esModuleDescr,
       "esModuleID": esModuleID,
       "esModuleVersion": esModuleVersion,
       "esModuleObjectID": esModuleObjectID,
       "esModulePortCapacity": esModulePortCapacity,
       "esModuleReset": esModuleReset,
       "esModuleLastStatusChange": esModuleLastStatusChange,
       "esModuleCollisionPeriods": esModuleCollisionPeriods,
       "esModuleLinkDisplayMap": esModuleLinkDisplayMap,
       "esModuleDisabledDisplayMap": esModuleDisabledDisplayMap,
       "esModuleBroadcastStormBlocked": esModuleBroadcastStormBlocked,
       "esModuleFirmwareVersion": esModuleFirmwareVersion,
       "esModuleBOOTCodeVersion": esModuleBOOTCodeVersion,
       "esModuleFlashStatus": esModuleFlashStatus,
       "esModuleResetToFactoryDefaults": esModuleResetToFactoryDefaults,
       "esModuleSwPortIndex": esModuleSwPortIndex,
       "esModulePortInfo": esModulePortInfo,
       "esModulePortTable": esModulePortTable,
       "esModulePortEntry": esModulePortEntry,
       "esModuleSlotIndex": esModuleSlotIndex,
       "esModulePortIndex": esModulePortIndex,
       "esModulePortDescr": esModulePortDescr,
       "esModulePortAdminStatus": esModulePortAdminStatus,
       "esModulePortAutoPartitionState": esModulePortAutoPartitionState,
       "esModulePortOperStatus": esModulePortOperStatus,
       "esModulePortLinkbeatStatus": esModulePortLinkbeatStatus,
       "esModulePortConnectorType": esModulePortConnectorType,
       "esModulePortReceivePeriods": esModulePortReceivePeriods,
       "esModuleSpecific": esModuleSpecific,
       "fmFDDIBasic": fmFDDIBasic,
       "fmFDDICfgInfo": fmFDDICfgInfo,
       "fmCfgTable": fmCfgTable,
       "fmCfgEntry": fmCfgEntry,
       "fmCfgIndex": fmCfgIndex,
       "fmCfgFirmwareVersion": fmCfgFirmwareVersion,
       "fmCfgBOOTCodeVersion": fmCfgBOOTCodeVersion,
       "fmCfgPOSTResult": fmCfgPOSTResult,
       "fmCfgPOSTTest": fmCfgPOSTTest,
       "fmCfgPOSTLoopbackResult": fmCfgPOSTLoopbackResult,
       "fmCfgFlashStatus": fmCfgFlashStatus,
       "fmCfgResetToFactoryDefaults": fmCfgResetToFactoryDefaults,
       "fmCfgResetModule": fmCfgResetModule,
       "fmCfgNovellFDDISNAPTranslation": fmCfgNovellFDDISNAPTranslation,
       "fmCfgUnmatchedSNAPDestination": fmCfgUnmatchedSNAPDestination,
       "fmCfgAuthorizationChecking": fmCfgAuthorizationChecking,
       "fmCfgAuthorizationString": fmCfgAuthorizationString,
       "fmFDDIXlateToEthInfo": fmFDDIXlateToEthInfo,
       "fmXlateToEthTable": fmXlateToEthTable,
       "fmXlateToEthEntry": fmXlateToEthEntry,
       "fmXlateToEthIndex": fmXlateToEthIndex,
       "fmXlateToEthNovellSnapToRaw8023Frames": fmXlateToEthNovellSnapToRaw8023Frames,
       "fmXlateToEthNovellSnapToEthIIFrames": fmXlateToEthNovellSnapToEthIIFrames,
       "fmXlateToEthNovellSnapToSnapFrames": fmXlateToEthNovellSnapToSnapFrames,
       "fmXlateToEthAppleTalkSnapToSnapFrames": fmXlateToEthAppleTalkSnapToSnapFrames,
       "fmXlateToEthIpSnapForFragmentationFrames": fmXlateToEthIpSnapForFragmentationFrames,
       "fmXlateToEthIpSnapFragmentedFrames": fmXlateToEthIpSnapFragmentedFrames,
       "fmXlateToEthBridgeTunnelToEthIIFrames": fmXlateToEthBridgeTunnelToEthIIFrames,
       "fmXlateToEthOtherSnapToEthIIFrames": fmXlateToEthOtherSnapToEthIIFrames,
       "fmXlateToEthOtherSnapToSnapFrames": fmXlateToEthOtherSnapToSnapFrames,
       "fmXlateToEth8022To8022Frames": fmXlateToEth8022To8022Frames,
       "fmFDDIXlateToFDDIInfo": fmFDDIXlateToFDDIInfo,
       "fmXlateToFDDITable": fmXlateToFDDITable,
       "fmXlateToFDDIEntry": fmXlateToFDDIEntry,
       "fmXlateToFDDIIndex": fmXlateToFDDIIndex,
       "fmXlateToFDDINovellRaw8023ToSnapFrames": fmXlateToFDDINovellRaw8023ToSnapFrames,
       "fmXlateToFDDINovellEthIIToSnapFrames": fmXlateToFDDINovellEthIIToSnapFrames,
       "fmXlateToFDDINovellSnapToSnapFrames": fmXlateToFDDINovellSnapToSnapFrames,
       "fmXlateToFDDIEthIIToBridgeTunnelFrames": fmXlateToFDDIEthIIToBridgeTunnelFrames,
       "fmXlateToFDDIEthIIToSnapFrames": fmXlateToFDDIEthIIToSnapFrames,
       "fmXlateToFDDIOtherSnapToSnapFrames": fmXlateToFDDIOtherSnapToSnapFrames,
       "fmXlateToFDDI8022To8022Frames": fmXlateToFDDI8022To8022Frames,
       "fmFDDIFilterInfo": fmFDDIFilterInfo,
       "fmFilterTable": fmFilterTable,
       "fmFilterEntry": fmFilterEntry,
       "fmFilterIndex": fmFilterIndex,
       "fmFilterFcsInvalidFrames": fmFilterFcsInvalidFrames,
       "fmFilterDataLengthFrames": fmFilterDataLengthFrames,
       "fmFilterErrorIndFrames": fmFilterErrorIndFrames,
       "fmFilterFddiFifoOverrunFrames": fmFilterFddiFifoOverrunFrames,
       "fmFilterFddiInternalErrorFrames": fmFilterFddiInternalErrorFrames,
       "fmFilterNoBufferSpaceFrames": fmFilterNoBufferSpaceFrames,
       "fmFilterNoEndDelimitFrames": fmFilterNoEndDelimitFrames,
       "fmFilterNoLlcHeaderFrames": fmFilterNoLlcHeaderFrames,
       "fmFilterSourceRouteFrames": fmFilterSourceRouteFrames,
       "fmFilterNoSnapHeaderFrames": fmFilterNoSnapHeaderFrames,
       "fmFilterTooLargeFrames": fmFilterTooLargeFrames,
       "fmFilterNovellSnapFilteredFrames": fmFilterNovellSnapFilteredFrames,
       "fmFilterCantFragmentFrames": fmFilterCantFragmentFrames,
       "fmFilterBadIpHeaderFrames": fmFilterBadIpHeaderFrames,
       "fmFilterRingDownDiscards": fmFilterRingDownDiscards,
       "fmFilterNovellOtherFilteredFrames": fmFilterNovellOtherFilteredFrames,
       "fmAtmBasic": fmAtmBasic,
       "fmAtmCfgInfo": fmAtmCfgInfo,
       "fmAtmCfgTable": fmAtmCfgTable,
       "fmAtmCfgEntry": fmAtmCfgEntry,
       "fmAtmCfgIndex": fmAtmCfgIndex,
       "fmAtmCfgPOSTResult": fmAtmCfgPOSTResult,
       "fmAtmCfgPOSTTest": fmAtmCfgPOSTTest,
       "fmAtmCfgPOSTLoopbackResult": fmAtmCfgPOSTLoopbackResult,
       "fmAtmCfgFramingMode": fmAtmCfgFramingMode,
       "fmAtmStatsInfo": fmAtmStatsInfo,
       "fmAtmRxStatTable": fmAtmRxStatTable,
       "fmAtmRxStatEntry": fmAtmRxStatEntry,
       "fmAtmRxStatIndex": fmAtmRxStatIndex,
       "fmAtmRxControlFrames": fmAtmRxControlFrames,
       "fmAtmRxLocalLecFrames": fmAtmRxLocalLecFrames,
       "fmAtmRxNoBufferDiscards": fmAtmRxNoBufferDiscards,
       "fmAtmRxCRCErrors": fmAtmRxCRCErrors,
       "fmAtmRxFrameTooLongs": fmAtmRxFrameTooLongs,
       "fmAtmRxOtherDiscards": fmAtmRxOtherDiscards,
       "fmAtmRxHecCellErrors": fmAtmRxHecCellErrors}
)
