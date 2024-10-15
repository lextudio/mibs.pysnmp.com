# SNMP MIB module (PBC-KODIAK-M-G10-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PBC-KODIAK-M-G10-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:01 2024
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

(pbcCaps,
 pbcModuleRegs,
 pbcProducts,
 pbcReqs) = mibBuilder.importSymbols(
    "PBC-ENT-MIB",
    "pbcCaps",
    "pbcModuleRegs",
    "pbcProducts",
    "pbcReqs")

(pbcCardIfCardIndex,) = mibBuilder.importSymbols(
    "PBC-GENERIC-MIB",
    "pbcCardIfCardIndex")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

pbcKodiakMG10Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 1, 1, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PbcKodiakMG10Cmts_ObjectIdentity = ObjectIdentity
pbcKodiakMG10Cmts = _PbcKodiakMG10Cmts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1)
)
_PbcG10SystemEnvMon_ObjectIdentity = ObjectIdentity
pbcG10SystemEnvMon = _PbcG10SystemEnvMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 1)
)
_SytemEnvMonObjects_ObjectIdentity = ObjectIdentity
sytemEnvMonObjects = _SytemEnvMonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 1, 1)
)
_SystemEnvMonPowerSupply_ObjectIdentity = ObjectIdentity
systemEnvMonPowerSupply = _SystemEnvMonPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 1, 1, 1)
)
_SystemEnvMonPowerSupplyEntityIndex_Type = Integer32
_SystemEnvMonPowerSupplyEntityIndex_Object = MibScalar
systemEnvMonPowerSupplyEntityIndex = _SystemEnvMonPowerSupplyEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 1, 1, 1, 1),
    _SystemEnvMonPowerSupplyEntityIndex_Type()
)
systemEnvMonPowerSupplyEntityIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemEnvMonPowerSupplyEntityIndex.setStatus("current")


class _SystemEnvMonPowerSupplyStatus_Type(Integer32):
    """Custom type systemEnvMonPowerSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 2),
          ("failed", 3),
          ("normal", 1))
    )


_SystemEnvMonPowerSupplyStatus_Type.__name__ = "Integer32"
_SystemEnvMonPowerSupplyStatus_Object = MibScalar
systemEnvMonPowerSupplyStatus = _SystemEnvMonPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 1, 1, 1, 2),
    _SystemEnvMonPowerSupplyStatus_Type()
)
systemEnvMonPowerSupplyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemEnvMonPowerSupplyStatus.setStatus("current")
_SystemEnvMonTemperature_ObjectIdentity = ObjectIdentity
systemEnvMonTemperature = _SystemEnvMonTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 1, 1, 3)
)
_SystemEnvMonAmbientTemperatureHighThreshold_Type = Integer32
_SystemEnvMonAmbientTemperatureHighThreshold_Object = MibScalar
systemEnvMonAmbientTemperatureHighThreshold = _SystemEnvMonAmbientTemperatureHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 1, 1, 3, 1),
    _SystemEnvMonAmbientTemperatureHighThreshold_Type()
)
systemEnvMonAmbientTemperatureHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemEnvMonAmbientTemperatureHighThreshold.setStatus("current")
_SystemEnvMonAmbientTemperatureLowThreshold_Type = Integer32
_SystemEnvMonAmbientTemperatureLowThreshold_Object = MibScalar
systemEnvMonAmbientTemperatureLowThreshold = _SystemEnvMonAmbientTemperatureLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 1, 1, 3, 2),
    _SystemEnvMonAmbientTemperatureLowThreshold_Type()
)
systemEnvMonAmbientTemperatureLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemEnvMonAmbientTemperatureLowThreshold.setStatus("current")
_SystemEnvMonAmbientTermperatureNumEntries_Type = Unsigned32
_SystemEnvMonAmbientTermperatureNumEntries_Object = MibScalar
systemEnvMonAmbientTermperatureNumEntries = _SystemEnvMonAmbientTermperatureNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 1, 1, 3, 3),
    _SystemEnvMonAmbientTermperatureNumEntries_Type()
)
systemEnvMonAmbientTermperatureNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemEnvMonAmbientTermperatureNumEntries.setStatus("current")
_SystemEnvMonAmbientTemperatureTable_Object = MibTable
systemEnvMonAmbientTemperatureTable = _SystemEnvMonAmbientTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    systemEnvMonAmbientTemperatureTable.setStatus("current")
_SystemEnvMonAmbientTemperatureEntry_Object = MibTableRow
systemEnvMonAmbientTemperatureEntry = _SystemEnvMonAmbientTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 1, 1, 3, 4, 1)
)
systemEnvMonAmbientTemperatureEntry.setIndexNames(
    (0, "PBC-GENERIC-MIB", "pbcCardIfCardIndex"),
)
if mibBuilder.loadTexts:
    systemEnvMonAmbientTemperatureEntry.setStatus("current")
_SystemEnvMonAmbientTemperature_Type = Integer32
_SystemEnvMonAmbientTemperature_Object = MibTableColumn
systemEnvMonAmbientTemperature = _SystemEnvMonAmbientTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 1, 1, 3, 4, 1, 1),
    _SystemEnvMonAmbientTemperature_Type()
)
systemEnvMonAmbientTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemEnvMonAmbientTemperature.setStatus("current")
_SystemEnvMonFanTrayStatusNumEntries_Type = Unsigned32
_SystemEnvMonFanTrayStatusNumEntries_Object = MibScalar
systemEnvMonFanTrayStatusNumEntries = _SystemEnvMonFanTrayStatusNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 1, 1, 5),
    _SystemEnvMonFanTrayStatusNumEntries_Type()
)
systemEnvMonFanTrayStatusNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemEnvMonFanTrayStatusNumEntries.setStatus("current")
_SystemEnvMonFanTrayStatusTable_Object = MibTable
systemEnvMonFanTrayStatusTable = _SystemEnvMonFanTrayStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    systemEnvMonFanTrayStatusTable.setStatus("current")
_SystemEnvMonFanTrayStatusEntry_Object = MibTableRow
systemEnvMonFanTrayStatusEntry = _SystemEnvMonFanTrayStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 1, 1, 6, 1)
)
systemEnvMonFanTrayStatusEntry.setIndexNames(
    (0, "PBC-KODIAK-M-G10-MIB", "systemEnvMonFanStatusIndex"),
)
if mibBuilder.loadTexts:
    systemEnvMonFanTrayStatusEntry.setStatus("current")
_SystemEnvMonFanTrayStatusIndex_Type = Unsigned32
_SystemEnvMonFanTrayStatusIndex_Object = MibTableColumn
systemEnvMonFanTrayStatusIndex = _SystemEnvMonFanTrayStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 1, 1, 6, 1, 1),
    _SystemEnvMonFanTrayStatusIndex_Type()
)
systemEnvMonFanTrayStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemEnvMonFanTrayStatusIndex.setStatus("current")
_SystemEnvMonFanTrayStatusEntityIndex_Type = Unsigned32
_SystemEnvMonFanTrayStatusEntityIndex_Object = MibTableColumn
systemEnvMonFanTrayStatusEntityIndex = _SystemEnvMonFanTrayStatusEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 1, 1, 6, 1, 2),
    _SystemEnvMonFanTrayStatusEntityIndex_Type()
)
systemEnvMonFanTrayStatusEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemEnvMonFanTrayStatusEntityIndex.setStatus("current")
_SystemEnvMonFanStatusNumEntries_Type = Integer32
_SystemEnvMonFanStatusNumEntries_Object = MibScalar
systemEnvMonFanStatusNumEntries = _SystemEnvMonFanStatusNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 1, 1, 7),
    _SystemEnvMonFanStatusNumEntries_Type()
)
systemEnvMonFanStatusNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemEnvMonFanStatusNumEntries.setStatus("current")
_SystemEnvMonFanStatusTable_Object = MibTable
systemEnvMonFanStatusTable = _SystemEnvMonFanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    systemEnvMonFanStatusTable.setStatus("current")
_SystemEnvMonFanStatusEntry_Object = MibTableRow
systemEnvMonFanStatusEntry = _SystemEnvMonFanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 1, 1, 8, 1)
)
systemEnvMonFanStatusEntry.setIndexNames(
    (0, "PBC-KODIAK-M-G10-MIB", "systemEnvMonFanTrayStatusIndex"),
    (0, "PBC-KODIAK-M-G10-MIB", "systemEnvMonFanStatusIndex"),
)
if mibBuilder.loadTexts:
    systemEnvMonFanStatusEntry.setStatus("current")
_SystemEnvMonFanStatusIndex_Type = Unsigned32
_SystemEnvMonFanStatusIndex_Object = MibTableColumn
systemEnvMonFanStatusIndex = _SystemEnvMonFanStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 1, 1, 8, 1, 1),
    _SystemEnvMonFanStatusIndex_Type()
)
systemEnvMonFanStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemEnvMonFanStatusIndex.setStatus("current")
_SystemEnvMonFanStatusSpeed_Type = Integer32
_SystemEnvMonFanStatusSpeed_Object = MibTableColumn
systemEnvMonFanStatusSpeed = _SystemEnvMonFanStatusSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 1, 1, 8, 1, 2),
    _SystemEnvMonFanStatusSpeed_Type()
)
systemEnvMonFanStatusSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemEnvMonFanStatusSpeed.setStatus("current")
_PbcG10SystemConformance_ObjectIdentity = ObjectIdentity
pbcG10SystemConformance = _PbcG10SystemConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 2)
)
_PbcG10SystemGroups_ObjectIdentity = ObjectIdentity
pbcG10SystemGroups = _PbcG10SystemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 2, 1)
)
_PbcG10SystemCompliance_ObjectIdentity = ObjectIdentity
pbcG10SystemCompliance = _PbcG10SystemCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 2, 3)
)
_PbcG10DMRedundancy_ObjectIdentity = ObjectIdentity
pbcG10DMRedundancy = _PbcG10DMRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 3)
)
_PbcG10CmtsDMRGroupTable_Object = MibTable
pbcG10CmtsDMRGroupTable = _PbcG10CmtsDMRGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    pbcG10CmtsDMRGroupTable.setStatus("current")
_PbcG10CmtsDMRGroupEntry_Object = MibTableRow
pbcG10CmtsDMRGroupEntry = _PbcG10CmtsDMRGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 3, 1, 1)
)
pbcG10CmtsDMRGroupEntry.setIndexNames(
    (0, "PBC-KODIAK-M-G10-MIB", "pbcG10CmtsDMRGroupIndex"),
    (0, "PBC-KODIAK-M-G10-MIB", "pbcG10CmtsDMRGroupSlotNbr"),
)
if mibBuilder.loadTexts:
    pbcG10CmtsDMRGroupEntry.setStatus("current")
_PbcG10CmtsDMRGroupIndex_Type = Unsigned32
_PbcG10CmtsDMRGroupIndex_Object = MibTableColumn
pbcG10CmtsDMRGroupIndex = _PbcG10CmtsDMRGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 3, 1, 1, 1),
    _PbcG10CmtsDMRGroupIndex_Type()
)
pbcG10CmtsDMRGroupIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pbcG10CmtsDMRGroupIndex.setStatus("current")
_PbcG10CmtsDMRGroupSlotNbr_Type = Unsigned32
_PbcG10CmtsDMRGroupSlotNbr_Object = MibTableColumn
pbcG10CmtsDMRGroupSlotNbr = _PbcG10CmtsDMRGroupSlotNbr_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 3, 1, 1, 2),
    _PbcG10CmtsDMRGroupSlotNbr_Type()
)
pbcG10CmtsDMRGroupSlotNbr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pbcG10CmtsDMRGroupSlotNbr.setStatus("current")
_PbcG10CmtsDMRGroupDmCardIndex_Type = Unsigned32
_PbcG10CmtsDMRGroupDmCardIndex_Object = MibTableColumn
pbcG10CmtsDMRGroupDmCardIndex = _PbcG10CmtsDMRGroupDmCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 3, 1, 1, 3),
    _PbcG10CmtsDMRGroupDmCardIndex_Type()
)
pbcG10CmtsDMRGroupDmCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcG10CmtsDMRGroupDmCardIndex.setStatus("current")
_PbcG10CmtsDMRGroupImCardIndex_Type = Unsigned32
_PbcG10CmtsDMRGroupImCardIndex_Object = MibTableColumn
pbcG10CmtsDMRGroupImCardIndex = _PbcG10CmtsDMRGroupImCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 3, 1, 1, 4),
    _PbcG10CmtsDMRGroupImCardIndex_Type()
)
pbcG10CmtsDMRGroupImCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcG10CmtsDMRGroupImCardIndex.setStatus("current")


class _PbcG10CmtsDMRGroupRole_Type(Integer32):
    """Custom type pbcG10CmtsDMRGroupRole based on Integer32"""
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
          ("excluded", 3),
          ("standby", 2))
    )


_PbcG10CmtsDMRGroupRole_Type.__name__ = "Integer32"
_PbcG10CmtsDMRGroupRole_Object = MibTableColumn
pbcG10CmtsDMRGroupRole = _PbcG10CmtsDMRGroupRole_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 3, 1, 1, 5),
    _PbcG10CmtsDMRGroupRole_Type()
)
pbcG10CmtsDMRGroupRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcG10CmtsDMRGroupRole.setStatus("current")


class _PbcG10CmtsDMRGroupStatus_Type(Integer32):
    """Custom type pbcG10CmtsDMRGroupStatus based on Integer32"""
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
        *(("covering", 5),
          ("failed", 4),
          ("notPresent", 1),
          ("offline", 2),
          ("online", 3))
    )


_PbcG10CmtsDMRGroupStatus_Type.__name__ = "Integer32"
_PbcG10CmtsDMRGroupStatus_Object = MibTableColumn
pbcG10CmtsDMRGroupStatus = _PbcG10CmtsDMRGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 3, 1, 1, 6),
    _PbcG10CmtsDMRGroupStatus_Type()
)
pbcG10CmtsDMRGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcG10CmtsDMRGroupStatus.setStatus("current")
_PbcG10CmtsDMRGroupAlias_Type = Unsigned32
_PbcG10CmtsDMRGroupAlias_Object = MibTableColumn
pbcG10CmtsDMRGroupAlias = _PbcG10CmtsDMRGroupAlias_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 3, 1, 1, 7),
    _PbcG10CmtsDMRGroupAlias_Type()
)
pbcG10CmtsDMRGroupAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcG10CmtsDMRGroupAlias.setStatus("current")


class _PbcG10CmtsDMRGroupAction_Type(Integer32):
    """Custom type pbcG10CmtsDMRGroupAction based on Integer32"""
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
        *(("excluded", 2),
          ("include", 3),
          ("none", 1),
          ("switchAt", 5),
          ("switchIn", 4))
    )


_PbcG10CmtsDMRGroupAction_Type.__name__ = "Integer32"
_PbcG10CmtsDMRGroupAction_Object = MibTableColumn
pbcG10CmtsDMRGroupAction = _PbcG10CmtsDMRGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 3, 1, 1, 8),
    _PbcG10CmtsDMRGroupAction_Type()
)
pbcG10CmtsDMRGroupAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcG10CmtsDMRGroupAction.setStatus("current")
_PbcG10CmtsDMRGroupSwitchIn_Type = Unsigned32
_PbcG10CmtsDMRGroupSwitchIn_Object = MibTableColumn
pbcG10CmtsDMRGroupSwitchIn = _PbcG10CmtsDMRGroupSwitchIn_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 3, 1, 1, 9),
    _PbcG10CmtsDMRGroupSwitchIn_Type()
)
pbcG10CmtsDMRGroupSwitchIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcG10CmtsDMRGroupSwitchIn.setStatus("current")
_PbcG10CmtsDMRGroupSwitchAt_Type = DateAndTime
_PbcG10CmtsDMRGroupSwitchAt_Object = MibTableColumn
pbcG10CmtsDMRGroupSwitchAt = _PbcG10CmtsDMRGroupSwitchAt_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 3, 1, 1, 10),
    _PbcG10CmtsDMRGroupSwitchAt_Type()
)
pbcG10CmtsDMRGroupSwitchAt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcG10CmtsDMRGroupSwitchAt.setStatus("current")


class _PbcG10CmtsDMRGroupFreeze_Type(Integer32):
    """Custom type pbcG10CmtsDMRGroupFreeze based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("freeze", 1),
          ("nofreeze", 2))
    )


_PbcG10CmtsDMRGroupFreeze_Type.__name__ = "Integer32"
_PbcG10CmtsDMRGroupFreeze_Object = MibScalar
pbcG10CmtsDMRGroupFreeze = _PbcG10CmtsDMRGroupFreeze_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 3, 2),
    _PbcG10CmtsDMRGroupFreeze_Type()
)
pbcG10CmtsDMRGroupFreeze.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcG10CmtsDMRGroupFreeze.setStatus("current")
_PbcG10CmtsCCMRedundancy_ObjectIdentity = ObjectIdentity
pbcG10CmtsCCMRedundancy = _PbcG10CmtsCCMRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 4)
)
_PbcG10CmtsCCMRedundancyObject_ObjectIdentity = ObjectIdentity
pbcG10CmtsCCMRedundancyObject = _PbcG10CmtsCCMRedundancyObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 4, 1)
)
_PbcG10CmtsCCMPrimarySlot_Type = Unsigned32
_PbcG10CmtsCCMPrimarySlot_Object = MibScalar
pbcG10CmtsCCMPrimarySlot = _PbcG10CmtsCCMPrimarySlot_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 4, 1, 1),
    _PbcG10CmtsCCMPrimarySlot_Type()
)
pbcG10CmtsCCMPrimarySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbcG10CmtsCCMPrimarySlot.setStatus("current")


class _PbcG10CmtsCCMAction_Type(Integer32):
    """Custom type pbcG10CmtsCCMAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("switchAt", 3),
          ("switchIn", 2))
    )


_PbcG10CmtsCCMAction_Type.__name__ = "Integer32"
_PbcG10CmtsCCMAction_Object = MibScalar
pbcG10CmtsCCMAction = _PbcG10CmtsCCMAction_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 4, 1, 2),
    _PbcG10CmtsCCMAction_Type()
)
pbcG10CmtsCCMAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcG10CmtsCCMAction.setStatus("current")
_PbcG10CmtsCCMSwitchIn_Type = Unsigned32
_PbcG10CmtsCCMSwitchIn_Object = MibScalar
pbcG10CmtsCCMSwitchIn = _PbcG10CmtsCCMSwitchIn_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 4, 1, 3),
    _PbcG10CmtsCCMSwitchIn_Type()
)
pbcG10CmtsCCMSwitchIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcG10CmtsCCMSwitchIn.setStatus("current")
_PbcG10CmtsCCMSwitchAt_Type = DateAndTime
_PbcG10CmtsCCMSwitchAt_Object = MibScalar
pbcG10CmtsCCMSwitchAt = _PbcG10CmtsCCMSwitchAt_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 4, 1, 4),
    _PbcG10CmtsCCMSwitchAt_Type()
)
pbcG10CmtsCCMSwitchAt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcG10CmtsCCMSwitchAt.setStatus("current")
_PbcG10CmtsNICRedundancy_ObjectIdentity = ObjectIdentity
pbcG10CmtsNICRedundancy = _PbcG10CmtsNICRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 5)
)
_PbcG10CmtsNICRedundancyObject_ObjectIdentity = ObjectIdentity
pbcG10CmtsNICRedundancyObject = _PbcG10CmtsNICRedundancyObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 5, 1)
)


class _PbcG10CmtsNICRedundancyEnable_Type(Integer32):
    """Custom type pbcG10CmtsNICRedundancyEnable based on Integer32"""
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


_PbcG10CmtsNICRedundancyEnable_Type.__name__ = "Integer32"
_PbcG10CmtsNICRedundancyEnable_Object = MibScalar
pbcG10CmtsNICRedundancyEnable = _PbcG10CmtsNICRedundancyEnable_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 5, 1, 1),
    _PbcG10CmtsNICRedundancyEnable_Type()
)
pbcG10CmtsNICRedundancyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcG10CmtsNICRedundancyEnable.setStatus("current")
_PbcG10CmtsNicDmConnectivityTable_Object = MibTable
pbcG10CmtsNicDmConnectivityTable = _PbcG10CmtsNicDmConnectivityTable_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    pbcG10CmtsNicDmConnectivityTable.setStatus("current")
_PbcG10CmtsNicDmConnectivityEntry_Object = MibTableRow
pbcG10CmtsNicDmConnectivityEntry = _PbcG10CmtsNicDmConnectivityEntry_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 5, 1, 2, 1)
)
pbcG10CmtsNicDmConnectivityEntry.setIndexNames(
    (0, "PBC-KODIAK-M-G10-MIB", "pbcG10CmtsNicDmConnectivityDmIndex"),
    (0, "PBC-KODIAK-M-G10-MIB", "pbcG10CmtsNicDmConnectivityCableInterfaceIndex"),
)
if mibBuilder.loadTexts:
    pbcG10CmtsNicDmConnectivityEntry.setStatus("current")
_PbcG10CmtsNicDmConnectivityDmIndex_Type = Unsigned32
_PbcG10CmtsNicDmConnectivityDmIndex_Object = MibTableColumn
pbcG10CmtsNicDmConnectivityDmIndex = _PbcG10CmtsNicDmConnectivityDmIndex_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 5, 1, 2, 1, 1),
    _PbcG10CmtsNicDmConnectivityDmIndex_Type()
)
pbcG10CmtsNicDmConnectivityDmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pbcG10CmtsNicDmConnectivityDmIndex.setStatus("current")


class _PbcG10CmtsNicDmConnectivityCableInterfaceIndex_Type(Integer32):
    """Custom type pbcG10CmtsNicDmConnectivityCableInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("evenCableInterface", 2),
          ("oddCableInterface", 1))
    )


_PbcG10CmtsNicDmConnectivityCableInterfaceIndex_Type.__name__ = "Integer32"
_PbcG10CmtsNicDmConnectivityCableInterfaceIndex_Object = MibTableColumn
pbcG10CmtsNicDmConnectivityCableInterfaceIndex = _PbcG10CmtsNicDmConnectivityCableInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 5, 1, 2, 1, 2),
    _PbcG10CmtsNicDmConnectivityCableInterfaceIndex_Type()
)
pbcG10CmtsNicDmConnectivityCableInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pbcG10CmtsNicDmConnectivityCableInterfaceIndex.setStatus("current")
_PbcG10CmtsNicDmConnectivityDmCardSlotNumber_Type = Unsigned32
_PbcG10CmtsNicDmConnectivityDmCardSlotNumber_Object = MibTableColumn
pbcG10CmtsNicDmConnectivityDmCardSlotNumber = _PbcG10CmtsNicDmConnectivityDmCardSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 5, 1, 2, 1, 3),
    _PbcG10CmtsNicDmConnectivityDmCardSlotNumber_Type()
)
pbcG10CmtsNicDmConnectivityDmCardSlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcG10CmtsNicDmConnectivityDmCardSlotNumber.setStatus("current")


class _PbcG10CmtsNicDmConnectivityConnectTo_Type(Integer32):
    """Custom type pbcG10CmtsNicDmConnectivityConnectTo based on Integer32"""
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
        *(("nic5", 1),
          ("nic9", 2),
          ("rf45a", 3),
          ("rf45b", 4))
    )


_PbcG10CmtsNicDmConnectivityConnectTo_Type.__name__ = "Integer32"
_PbcG10CmtsNicDmConnectivityConnectTo_Object = MibTableColumn
pbcG10CmtsNicDmConnectivityConnectTo = _PbcG10CmtsNicDmConnectivityConnectTo_Object(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 5, 1, 2, 1, 4),
    _PbcG10CmtsNicDmConnectivityConnectTo_Type()
)
pbcG10CmtsNicDmConnectivityConnectTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcG10CmtsNicDmConnectivityConnectTo.setStatus("current")

# Managed Objects groups

pbcSystemEnvMonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 2, 1, 1)
)
pbcSystemEnvMonGroup.setObjects(
      *(("PBC-KODIAK-M-G10-MIB", "systemEnvMonFanStatusNumEntries"),
        ("PBC-KODIAK-M-G10-MIB", "systemEnvMonFanStatusIndex"),
        ("PBC-KODIAK-M-G10-MIB", "systemEnvMonPowerSupplyEntityIndex"),
        ("PBC-KODIAK-M-G10-MIB", "systemEnvMonPowerSupplyStatus"),
        ("PBC-KODIAK-M-G10-MIB", "systemEnvMonAmbientTermperatureNumEntries"),
        ("PBC-KODIAK-M-G10-MIB", "systemEnvMonAmbientTemperature"),
        ("PBC-KODIAK-M-G10-MIB", "systemEnvMonFanTrayStatusNumEntries"),
        ("PBC-KODIAK-M-G10-MIB", "systemEnvMonFanTrayStatusIndex"),
        ("PBC-KODIAK-M-G10-MIB", "systemEnvMonFanTrayStatusEntityIndex"),
        ("PBC-KODIAK-M-G10-MIB", "systemEnvMonFanStatusSpeed"),
        ("PBC-KODIAK-M-G10-MIB", "systemEnvMonAmbientTemperatureLowThreshold"),
        ("PBC-KODIAK-M-G10-MIB", "systemEnvMonAmbientTemperatureHighThreshold"))
)
if mibBuilder.loadTexts:
    pbcSystemEnvMonGroup.setStatus("current")

pbcG10RedundancyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 2, 1, 2)
)
pbcG10RedundancyGroup.setObjects(
      *(("PBC-KODIAK-M-G10-MIB", "pbcG10CmtsDMRGroupIndex"),
        ("PBC-KODIAK-M-G10-MIB", "pbcG10CmtsDMRGroupSlotNbr"),
        ("PBC-KODIAK-M-G10-MIB", "pbcG10CmtsDMRGroupDmCardIndex"),
        ("PBC-KODIAK-M-G10-MIB", "pbcG10CmtsDMRGroupImCardIndex"),
        ("PBC-KODIAK-M-G10-MIB", "pbcG10CmtsDMRGroupRole"),
        ("PBC-KODIAK-M-G10-MIB", "pbcG10CmtsDMRGroupStatus"),
        ("PBC-KODIAK-M-G10-MIB", "pbcG10CmtsDMRGroupAlias"),
        ("PBC-KODIAK-M-G10-MIB", "pbcG10CmtsDMRGroupAction"),
        ("PBC-KODIAK-M-G10-MIB", "pbcG10CmtsDMRGroupSwitchIn"),
        ("PBC-KODIAK-M-G10-MIB", "pbcG10CmtsDMRGroupSwitchAt"),
        ("PBC-KODIAK-M-G10-MIB", "pbcG10CmtsDMRGroupFreeze"),
        ("PBC-KODIAK-M-G10-MIB", "pbcG10CmtsCCMPrimarySlot"),
        ("PBC-KODIAK-M-G10-MIB", "pbcG10CmtsCCMAction"),
        ("PBC-KODIAK-M-G10-MIB", "pbcG10CmtsCCMSwitchIn"),
        ("PBC-KODIAK-M-G10-MIB", "pbcG10CmtsCCMSwitchAt"),
        ("PBC-KODIAK-M-G10-MIB", "pbcG10CmtsNICRedundancyEnable"),
        ("PBC-KODIAK-M-G10-MIB", "pbcG10CmtsNicDmConnectivityDmCardSlotNumber"),
        ("PBC-KODIAK-M-G10-MIB", "pbcG10CmtsNicDmConnectivityConnectTo"))
)
if mibBuilder.loadTexts:
    pbcG10RedundancyGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pbcG10SystemBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    pbcG10SystemBasicCompliance.setStatus(
        "current"
    )

pbcG10RedundancyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5987, 3, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    pbcG10RedundancyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PBC-KODIAK-M-G10-MIB",
    **{"pbcKodiakMG10Mib": pbcKodiakMG10Mib,
       "pbcKodiakMG10Cmts": pbcKodiakMG10Cmts,
       "pbcG10SystemEnvMon": pbcG10SystemEnvMon,
       "sytemEnvMonObjects": sytemEnvMonObjects,
       "systemEnvMonPowerSupply": systemEnvMonPowerSupply,
       "systemEnvMonPowerSupplyEntityIndex": systemEnvMonPowerSupplyEntityIndex,
       "systemEnvMonPowerSupplyStatus": systemEnvMonPowerSupplyStatus,
       "systemEnvMonTemperature": systemEnvMonTemperature,
       "systemEnvMonAmbientTemperatureHighThreshold": systemEnvMonAmbientTemperatureHighThreshold,
       "systemEnvMonAmbientTemperatureLowThreshold": systemEnvMonAmbientTemperatureLowThreshold,
       "systemEnvMonAmbientTermperatureNumEntries": systemEnvMonAmbientTermperatureNumEntries,
       "systemEnvMonAmbientTemperatureTable": systemEnvMonAmbientTemperatureTable,
       "systemEnvMonAmbientTemperatureEntry": systemEnvMonAmbientTemperatureEntry,
       "systemEnvMonAmbientTemperature": systemEnvMonAmbientTemperature,
       "systemEnvMonFanTrayStatusNumEntries": systemEnvMonFanTrayStatusNumEntries,
       "systemEnvMonFanTrayStatusTable": systemEnvMonFanTrayStatusTable,
       "systemEnvMonFanTrayStatusEntry": systemEnvMonFanTrayStatusEntry,
       "systemEnvMonFanTrayStatusIndex": systemEnvMonFanTrayStatusIndex,
       "systemEnvMonFanTrayStatusEntityIndex": systemEnvMonFanTrayStatusEntityIndex,
       "systemEnvMonFanStatusNumEntries": systemEnvMonFanStatusNumEntries,
       "systemEnvMonFanStatusTable": systemEnvMonFanStatusTable,
       "systemEnvMonFanStatusEntry": systemEnvMonFanStatusEntry,
       "systemEnvMonFanStatusIndex": systemEnvMonFanStatusIndex,
       "systemEnvMonFanStatusSpeed": systemEnvMonFanStatusSpeed,
       "pbcG10SystemConformance": pbcG10SystemConformance,
       "pbcG10SystemGroups": pbcG10SystemGroups,
       "pbcSystemEnvMonGroup": pbcSystemEnvMonGroup,
       "pbcG10RedundancyGroup": pbcG10RedundancyGroup,
       "pbcG10SystemCompliance": pbcG10SystemCompliance,
       "pbcG10SystemBasicCompliance": pbcG10SystemBasicCompliance,
       "pbcG10RedundancyCompliance": pbcG10RedundancyCompliance,
       "pbcG10DMRedundancy": pbcG10DMRedundancy,
       "pbcG10CmtsDMRGroupTable": pbcG10CmtsDMRGroupTable,
       "pbcG10CmtsDMRGroupEntry": pbcG10CmtsDMRGroupEntry,
       "pbcG10CmtsDMRGroupIndex": pbcG10CmtsDMRGroupIndex,
       "pbcG10CmtsDMRGroupSlotNbr": pbcG10CmtsDMRGroupSlotNbr,
       "pbcG10CmtsDMRGroupDmCardIndex": pbcG10CmtsDMRGroupDmCardIndex,
       "pbcG10CmtsDMRGroupImCardIndex": pbcG10CmtsDMRGroupImCardIndex,
       "pbcG10CmtsDMRGroupRole": pbcG10CmtsDMRGroupRole,
       "pbcG10CmtsDMRGroupStatus": pbcG10CmtsDMRGroupStatus,
       "pbcG10CmtsDMRGroupAlias": pbcG10CmtsDMRGroupAlias,
       "pbcG10CmtsDMRGroupAction": pbcG10CmtsDMRGroupAction,
       "pbcG10CmtsDMRGroupSwitchIn": pbcG10CmtsDMRGroupSwitchIn,
       "pbcG10CmtsDMRGroupSwitchAt": pbcG10CmtsDMRGroupSwitchAt,
       "pbcG10CmtsDMRGroupFreeze": pbcG10CmtsDMRGroupFreeze,
       "pbcG10CmtsCCMRedundancy": pbcG10CmtsCCMRedundancy,
       "pbcG10CmtsCCMRedundancyObject": pbcG10CmtsCCMRedundancyObject,
       "pbcG10CmtsCCMPrimarySlot": pbcG10CmtsCCMPrimarySlot,
       "pbcG10CmtsCCMAction": pbcG10CmtsCCMAction,
       "pbcG10CmtsCCMSwitchIn": pbcG10CmtsCCMSwitchIn,
       "pbcG10CmtsCCMSwitchAt": pbcG10CmtsCCMSwitchAt,
       "pbcG10CmtsNICRedundancy": pbcG10CmtsNICRedundancy,
       "pbcG10CmtsNICRedundancyObject": pbcG10CmtsNICRedundancyObject,
       "pbcG10CmtsNICRedundancyEnable": pbcG10CmtsNICRedundancyEnable,
       "pbcG10CmtsNicDmConnectivityTable": pbcG10CmtsNicDmConnectivityTable,
       "pbcG10CmtsNicDmConnectivityEntry": pbcG10CmtsNicDmConnectivityEntry,
       "pbcG10CmtsNicDmConnectivityDmIndex": pbcG10CmtsNicDmConnectivityDmIndex,
       "pbcG10CmtsNicDmConnectivityCableInterfaceIndex": pbcG10CmtsNicDmConnectivityCableInterfaceIndex,
       "pbcG10CmtsNicDmConnectivityDmCardSlotNumber": pbcG10CmtsNicDmConnectivityDmCardSlotNumber,
       "pbcG10CmtsNicDmConnectivityConnectTo": pbcG10CmtsNicDmConnectivityConnectTo}
)
