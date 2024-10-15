# SNMP MIB module (CISCO-IEEE8021-CFM-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IEEE8021-CFM-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:23 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(Dot1agCfmMpDirection,
 dot1agCfmMaIndex,
 dot1agCfmMdIndex) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmMpDirection",
    "dot1agCfmMaIndex",
    "dot1agCfmMdIndex")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 MacAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoIeee8021CfmExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 679)
)
ciscoIeee8021CfmExtMIB.setRevisions(
        ("2008-11-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CIeeeCfmExtMIBNotifs_ObjectIdentity = ObjectIdentity
cIeeeCfmExtMIBNotifs = _CIeeeCfmExtMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 0)
)
_CIeeeCfmExtMIBObjects_ObjectIdentity = ObjectIdentity
cIeeeCfmExtMIBObjects = _CIeeeCfmExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1)
)
_CiceCfmGlobal_ObjectIdentity = ObjectIdentity
ciceCfmGlobal = _CiceCfmGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 1)
)
_CiceCfmEnable_Type = TruthValue
_CiceCfmEnable_Object = MibScalar
ciceCfmEnable = _CiceCfmEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 1, 1),
    _CiceCfmEnable_Type()
)
ciceCfmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciceCfmEnable.setStatus("current")
_CiceCfmMaxMdLevel_Type = Unsigned32
_CiceCfmMaxMdLevel_Object = MibScalar
ciceCfmMaxMdLevel = _CiceCfmMaxMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 1, 2),
    _CiceCfmMaxMdLevel_Type()
)
ciceCfmMaxMdLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciceCfmMaxMdLevel.setStatus("current")
_CiceCfmBrainAddress_Type = MacAddress
_CiceCfmBrainAddress_Object = MibScalar
ciceCfmBrainAddress = _CiceCfmBrainAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 1, 3),
    _CiceCfmBrainAddress_Type()
)
ciceCfmBrainAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciceCfmBrainAddress.setStatus("current")
_CiceCfmCcMulticastAddress_Type = MacAddress
_CiceCfmCcMulticastAddress_Object = MibScalar
ciceCfmCcMulticastAddress = _CiceCfmCcMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 1, 4),
    _CiceCfmCcMulticastAddress_Type()
)
ciceCfmCcMulticastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciceCfmCcMulticastAddress.setStatus("current")
_CiceCfmLtmMulticastAddress_Type = MacAddress
_CiceCfmLtmMulticastAddress_Object = MibScalar
ciceCfmLtmMulticastAddress = _CiceCfmLtmMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 1, 5),
    _CiceCfmLtmMulticastAddress_Type()
)
ciceCfmLtmMulticastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciceCfmLtmMulticastAddress.setStatus("current")
_CiceCfmEnableFaultAlarm_Type = TruthValue
_CiceCfmEnableFaultAlarm_Object = MibScalar
ciceCfmEnableFaultAlarm = _CiceCfmEnableFaultAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 1, 6),
    _CiceCfmEnableFaultAlarm_Type()
)
ciceCfmEnableFaultAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciceCfmEnableFaultAlarm.setStatus("current")
_CiceCfmLtr_ObjectIdentity = ObjectIdentity
ciceCfmLtr = _CiceCfmLtr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 2)
)
_CiceCfmLtrEnable_Type = TruthValue
_CiceCfmLtrEnable_Object = MibScalar
ciceCfmLtrEnable = _CiceCfmLtrEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 2, 1),
    _CiceCfmLtrEnable_Type()
)
ciceCfmLtrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciceCfmLtrEnable.setStatus("current")


class _CiceCfmLtrHoldTime_Type(Unsigned32):
    """Custom type ciceCfmLtrHoldTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CiceCfmLtrHoldTime_Type.__name__ = "Unsigned32"
_CiceCfmLtrHoldTime_Object = MibScalar
ciceCfmLtrHoldTime = _CiceCfmLtrHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 2, 2),
    _CiceCfmLtrHoldTime_Type()
)
ciceCfmLtrHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciceCfmLtrHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    ciceCfmLtrHoldTime.setUnits("minutes")
_CiceCfmLtrSize_Type = Unsigned32
_CiceCfmLtrSize_Object = MibScalar
ciceCfmLtrSize = _CiceCfmLtrSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 2, 3),
    _CiceCfmLtrSize_Type()
)
ciceCfmLtrSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciceCfmLtrSize.setStatus("current")
_CiceCfmMa_ObjectIdentity = ObjectIdentity
ciceCfmMa = _CiceCfmMa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 3)
)
_CiceCfmMaNetTable_Object = MibTable
ciceCfmMaNetTable = _CiceCfmMaNetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ciceCfmMaNetTable.setStatus("current")
_CiceCfmMaNetEntry_Object = MibTableRow
ciceCfmMaNetEntry = _CiceCfmMaNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 3, 1, 1)
)
ciceCfmMaNetEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
)
if mibBuilder.loadTexts:
    ciceCfmMaNetEntry.setStatus("current")
_CiceCfmMaNetCciEnable_Type = TruthValue
_CiceCfmMaNetCciEnable_Object = MibTableColumn
ciceCfmMaNetCciEnable = _CiceCfmMaNetCciEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 3, 1, 1, 1),
    _CiceCfmMaNetCciEnable_Type()
)
ciceCfmMaNetCciEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciceCfmMaNetCciEnable.setStatus("current")
_CiceCfmMaNetCciDirection_Type = Dot1agCfmMpDirection
_CiceCfmMaNetCciDirection_Object = MibTableColumn
ciceCfmMaNetCciDirection = _CiceCfmMaNetCciDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 3, 1, 1, 2),
    _CiceCfmMaNetCciDirection_Type()
)
ciceCfmMaNetCciDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciceCfmMaNetCciDirection.setStatus("current")
_CiceCfmMaNetLossThreshold_Type = Unsigned32
_CiceCfmMaNetLossThreshold_Object = MibTableColumn
ciceCfmMaNetLossThreshold = _CiceCfmMaNetLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 3, 1, 1, 3),
    _CiceCfmMaNetLossThreshold_Type()
)
ciceCfmMaNetLossThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciceCfmMaNetLossThreshold.setStatus("current")
_CiceCfmIfObjects_ObjectIdentity = ObjectIdentity
ciceCfmIfObjects = _CiceCfmIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 4)
)
_CiceCfmInterfaceTable_Object = MibTable
ciceCfmInterfaceTable = _CiceCfmInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ciceCfmInterfaceTable.setStatus("current")
_CiceCfmInterfaceEntry_Object = MibTableRow
ciceCfmInterfaceEntry = _CiceCfmInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 4, 1, 1)
)
ciceCfmInterfaceEntry.setIndexNames(
    (0, "CISCO-IEEE8021-CFM-EXT-MIB", "ciceCfmIfIndex"),
)
if mibBuilder.loadTexts:
    ciceCfmInterfaceEntry.setStatus("current")
_CiceCfmIfIndex_Type = InterfaceIndex
_CiceCfmIfIndex_Object = MibTableColumn
ciceCfmIfIndex = _CiceCfmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 4, 1, 1, 1),
    _CiceCfmIfIndex_Type()
)
ciceCfmIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciceCfmIfIndex.setStatus("current")


class _CiceCfmIfState_Type(Integer32):
    """Custom type ciceCfmIfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("transparent", 3))
    )


_CiceCfmIfState_Type.__name__ = "Integer32"
_CiceCfmIfState_Object = MibTableColumn
ciceCfmIfState = _CiceCfmIfState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 4, 1, 1, 2),
    _CiceCfmIfState_Type()
)
ciceCfmIfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciceCfmIfState.setStatus("current")
_CiceCfmMipTable_Object = MibTable
ciceCfmMipTable = _CiceCfmMipTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 4, 2)
)
if mibBuilder.loadTexts:
    ciceCfmMipTable.setStatus("current")
_CiceCfmMipEntry_Object = MibTableRow
ciceCfmMipEntry = _CiceCfmMipEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 4, 2, 1)
)
ciceCfmMipEntry.setIndexNames(
    (0, "CISCO-IEEE8021-CFM-EXT-MIB", "ciceCfmIfIndex"),
    (0, "CISCO-IEEE8021-CFM-EXT-MIB", "ciceCfmMipVlanIndex"),
)
if mibBuilder.loadTexts:
    ciceCfmMipEntry.setStatus("current")
_CiceCfmMipVlanIndex_Type = VlanId
_CiceCfmMipVlanIndex_Object = MibTableColumn
ciceCfmMipVlanIndex = _CiceCfmMipVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 4, 2, 1, 1),
    _CiceCfmMipVlanIndex_Type()
)
ciceCfmMipVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciceCfmMipVlanIndex.setStatus("current")
_CiceCfmMipMdLevel_Type = Unsigned32
_CiceCfmMipMdLevel_Object = MibTableColumn
ciceCfmMipMdLevel = _CiceCfmMipMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 4, 2, 1, 2),
    _CiceCfmMipMdLevel_Type()
)
ciceCfmMipMdLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciceCfmMipMdLevel.setStatus("current")


class _CiceCfmMipStorageType_Type(StorageType):
    """Custom type ciceCfmMipStorageType based on StorageType"""


_CiceCfmMipStorageType_Object = MibTableColumn
ciceCfmMipStorageType = _CiceCfmMipStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 4, 2, 1, 3),
    _CiceCfmMipStorageType_Type()
)
ciceCfmMipStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciceCfmMipStorageType.setStatus("current")
_CiceCfmMipRowStatus_Type = RowStatus
_CiceCfmMipRowStatus_Object = MibTableColumn
ciceCfmMipRowStatus = _CiceCfmMipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 4, 2, 1, 4),
    _CiceCfmMipRowStatus_Type()
)
ciceCfmMipRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciceCfmMipRowStatus.setStatus("current")
_CiceCfmMacEnableIfTable_Object = MibTable
ciceCfmMacEnableIfTable = _CiceCfmMacEnableIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 4, 3)
)
if mibBuilder.loadTexts:
    ciceCfmMacEnableIfTable.setStatus("current")
_CiceCfmMacEnableIfEntry_Object = MibTableRow
ciceCfmMacEnableIfEntry = _CiceCfmMacEnableIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 4, 3, 1)
)
ciceCfmMacEnableIfEntry.setIndexNames(
    (0, "CISCO-IEEE8021-CFM-EXT-MIB", "ciceCfmIfIndex"),
    (0, "CISCO-IEEE8021-CFM-EXT-MIB", "ciceCfmMacEnableVlanIndex"),
)
if mibBuilder.loadTexts:
    ciceCfmMacEnableIfEntry.setStatus("current")
_CiceCfmMacEnableVlanIndex_Type = VlanId
_CiceCfmMacEnableVlanIndex_Object = MibTableColumn
ciceCfmMacEnableVlanIndex = _CiceCfmMacEnableVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 4, 3, 1, 1),
    _CiceCfmMacEnableVlanIndex_Type()
)
ciceCfmMacEnableVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciceCfmMacEnableVlanIndex.setStatus("current")


class _CiceCfmMacEnableStorageType_Type(StorageType):
    """Custom type ciceCfmMacEnableStorageType based on StorageType"""


_CiceCfmMacEnableStorageType_Object = MibTableColumn
ciceCfmMacEnableStorageType = _CiceCfmMacEnableStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 4, 3, 1, 2),
    _CiceCfmMacEnableStorageType_Type()
)
ciceCfmMacEnableStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciceCfmMacEnableStorageType.setStatus("current")
_CiceCfmMacEnableRowStatus_Type = RowStatus
_CiceCfmMacEnableRowStatus_Object = MibTableColumn
ciceCfmMacEnableRowStatus = _CiceCfmMacEnableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 4, 3, 1, 3),
    _CiceCfmMacEnableRowStatus_Type()
)
ciceCfmMacEnableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciceCfmMacEnableRowStatus.setStatus("current")
_CiceCfmMep_ObjectIdentity = ObjectIdentity
ciceCfmMep = _CiceCfmMep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 1, 5)
)
_CIeeeCfmExtMIBConformance_ObjectIdentity = ObjectIdentity
cIeeeCfmExtMIBConformance = _CIeeeCfmExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 2)
)
_CiceCfmMIBCompliances_ObjectIdentity = ObjectIdentity
ciceCfmMIBCompliances = _CiceCfmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 2, 1)
)
_CiceCfmMIBGroups_ObjectIdentity = ObjectIdentity
ciceCfmMIBGroups = _CiceCfmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 2, 2)
)

# Managed Objects groups

ciceCfmGlobalObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 2, 2, 1)
)
ciceCfmGlobalObjectsGroup.setObjects(
      *(("CISCO-IEEE8021-CFM-EXT-MIB", "ciceCfmEnable"),
        ("CISCO-IEEE8021-CFM-EXT-MIB", "ciceCfmMaxMdLevel"),
        ("CISCO-IEEE8021-CFM-EXT-MIB", "ciceCfmBrainAddress"),
        ("CISCO-IEEE8021-CFM-EXT-MIB", "ciceCfmCcMulticastAddress"),
        ("CISCO-IEEE8021-CFM-EXT-MIB", "ciceCfmLtmMulticastAddress"),
        ("CISCO-IEEE8021-CFM-EXT-MIB", "ciceCfmEnableFaultAlarm"))
)
if mibBuilder.loadTexts:
    ciceCfmGlobalObjectsGroup.setStatus("current")

ciceCfmLtrConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 2, 2, 2)
)
ciceCfmLtrConfigGroup.setObjects(
      *(("CISCO-IEEE8021-CFM-EXT-MIB", "ciceCfmLtrEnable"),
        ("CISCO-IEEE8021-CFM-EXT-MIB", "ciceCfmLtrHoldTime"),
        ("CISCO-IEEE8021-CFM-EXT-MIB", "ciceCfmLtrSize"))
)
if mibBuilder.loadTexts:
    ciceCfmLtrConfigGroup.setStatus("current")

ciceCfmMaNetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 2, 2, 3)
)
ciceCfmMaNetGroup.setObjects(
      *(("CISCO-IEEE8021-CFM-EXT-MIB", "ciceCfmMaNetCciEnable"),
        ("CISCO-IEEE8021-CFM-EXT-MIB", "ciceCfmMaNetCciDirection"),
        ("CISCO-IEEE8021-CFM-EXT-MIB", "ciceCfmMaNetLossThreshold"))
)
if mibBuilder.loadTexts:
    ciceCfmMaNetGroup.setStatus("current")

ciceCfmInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 2, 2, 4)
)
ciceCfmInterfaceGroup.setObjects(
    ("CISCO-IEEE8021-CFM-EXT-MIB", "ciceCfmIfState")
)
if mibBuilder.loadTexts:
    ciceCfmInterfaceGroup.setStatus("current")

ciceCfmMipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 2, 2, 5)
)
ciceCfmMipGroup.setObjects(
      *(("CISCO-IEEE8021-CFM-EXT-MIB", "ciceCfmMipMdLevel"),
        ("CISCO-IEEE8021-CFM-EXT-MIB", "ciceCfmMipStorageType"),
        ("CISCO-IEEE8021-CFM-EXT-MIB", "ciceCfmMipRowStatus"))
)
if mibBuilder.loadTexts:
    ciceCfmMipGroup.setStatus("current")

ciceCfmMacEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 2, 2, 6)
)
ciceCfmMacEnableGroup.setObjects(
      *(("CISCO-IEEE8021-CFM-EXT-MIB", "ciceCfmMacEnableStorageType"),
        ("CISCO-IEEE8021-CFM-EXT-MIB", "ciceCfmMacEnableRowStatus"))
)
if mibBuilder.loadTexts:
    ciceCfmMacEnableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciceCfmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 679, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciceCfmMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IEEE8021-CFM-EXT-MIB",
    **{"ciscoIeee8021CfmExtMIB": ciscoIeee8021CfmExtMIB,
       "cIeeeCfmExtMIBNotifs": cIeeeCfmExtMIBNotifs,
       "cIeeeCfmExtMIBObjects": cIeeeCfmExtMIBObjects,
       "ciceCfmGlobal": ciceCfmGlobal,
       "ciceCfmEnable": ciceCfmEnable,
       "ciceCfmMaxMdLevel": ciceCfmMaxMdLevel,
       "ciceCfmBrainAddress": ciceCfmBrainAddress,
       "ciceCfmCcMulticastAddress": ciceCfmCcMulticastAddress,
       "ciceCfmLtmMulticastAddress": ciceCfmLtmMulticastAddress,
       "ciceCfmEnableFaultAlarm": ciceCfmEnableFaultAlarm,
       "ciceCfmLtr": ciceCfmLtr,
       "ciceCfmLtrEnable": ciceCfmLtrEnable,
       "ciceCfmLtrHoldTime": ciceCfmLtrHoldTime,
       "ciceCfmLtrSize": ciceCfmLtrSize,
       "ciceCfmMa": ciceCfmMa,
       "ciceCfmMaNetTable": ciceCfmMaNetTable,
       "ciceCfmMaNetEntry": ciceCfmMaNetEntry,
       "ciceCfmMaNetCciEnable": ciceCfmMaNetCciEnable,
       "ciceCfmMaNetCciDirection": ciceCfmMaNetCciDirection,
       "ciceCfmMaNetLossThreshold": ciceCfmMaNetLossThreshold,
       "ciceCfmIfObjects": ciceCfmIfObjects,
       "ciceCfmInterfaceTable": ciceCfmInterfaceTable,
       "ciceCfmInterfaceEntry": ciceCfmInterfaceEntry,
       "ciceCfmIfIndex": ciceCfmIfIndex,
       "ciceCfmIfState": ciceCfmIfState,
       "ciceCfmMipTable": ciceCfmMipTable,
       "ciceCfmMipEntry": ciceCfmMipEntry,
       "ciceCfmMipVlanIndex": ciceCfmMipVlanIndex,
       "ciceCfmMipMdLevel": ciceCfmMipMdLevel,
       "ciceCfmMipStorageType": ciceCfmMipStorageType,
       "ciceCfmMipRowStatus": ciceCfmMipRowStatus,
       "ciceCfmMacEnableIfTable": ciceCfmMacEnableIfTable,
       "ciceCfmMacEnableIfEntry": ciceCfmMacEnableIfEntry,
       "ciceCfmMacEnableVlanIndex": ciceCfmMacEnableVlanIndex,
       "ciceCfmMacEnableStorageType": ciceCfmMacEnableStorageType,
       "ciceCfmMacEnableRowStatus": ciceCfmMacEnableRowStatus,
       "ciceCfmMep": ciceCfmMep,
       "cIeeeCfmExtMIBConformance": cIeeeCfmExtMIBConformance,
       "ciceCfmMIBCompliances": ciceCfmMIBCompliances,
       "ciceCfmMIBCompliance": ciceCfmMIBCompliance,
       "ciceCfmMIBGroups": ciceCfmMIBGroups,
       "ciceCfmGlobalObjectsGroup": ciceCfmGlobalObjectsGroup,
       "ciceCfmLtrConfigGroup": ciceCfmLtrConfigGroup,
       "ciceCfmMaNetGroup": ciceCfmMaNetGroup,
       "ciceCfmInterfaceGroup": ciceCfmInterfaceGroup,
       "ciceCfmMipGroup": ciceCfmMipGroup,
       "ciceCfmMacEnableGroup": ciceCfmMacEnableGroup}
)
