# SNMP MIB module (MERU-CONFIG-ROGUEAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MERU-CONFIG-ROGUEAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:06 2024
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(mwConfiguration,) = mibBuilder.importSymbols(
    "MERU-SMI",
    "mwConfiguration")

(MwlApType,
 MwlArrayDataTypeAction,
 MwlBlock,
 MwlOnOffSwitch) = mibBuilder.importSymbols(
    "MERU-TC",
    "MwlApType",
    "MwlArrayDataTypeAction",
    "MwlBlock",
    "MwlOnOffSwitch")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mwConfigRogueAp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MwRogueapVars_ObjectIdentity = ObjectIdentity
mwRogueapVars = _MwRogueapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 1)
)
_MwRogueapVarsDetection_Type = MwlOnOffSwitch
_MwRogueapVarsDetection_Object = MibScalar
mwRogueapVarsDetection = _MwRogueapVarsDetection_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 1, 1),
    _MwRogueapVarsDetection_Type()
)
mwRogueapVarsDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwRogueapVarsDetection.setStatus("current")
_MwRogueapVarsBlock_Type = MwlBlock
_MwRogueapVarsBlock_Object = MibScalar
mwRogueapVarsBlock = _MwRogueapVarsBlock_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 1, 2),
    _MwRogueapVarsBlock_Type()
)
mwRogueapVarsBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwRogueapVarsBlock.setStatus("current")
_MwRogueapVarsAging_Type = Unsigned32
_MwRogueapVarsAging_Object = MibScalar
mwRogueapVarsAging = _MwRogueapVarsAging_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 1, 3),
    _MwRogueapVarsAging_Type()
)
mwRogueapVarsAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwRogueapVarsAging.setStatus("current")
_MwRogueapVarsMitigateAps_Type = Unsigned32
_MwRogueapVarsMitigateAps_Object = MibScalar
mwRogueapVarsMitigateAps = _MwRogueapVarsMitigateAps_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 1, 4),
    _MwRogueapVarsMitigateAps_Type()
)
mwRogueapVarsMitigateAps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwRogueapVarsMitigateAps.setStatus("current")
_MwRogueapVarsScanningTime_Type = Unsigned32
_MwRogueapVarsScanningTime_Object = MibScalar
mwRogueapVarsScanningTime = _MwRogueapVarsScanningTime_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 1, 5),
    _MwRogueapVarsScanningTime_Type()
)
mwRogueapVarsScanningTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwRogueapVarsScanningTime.setStatus("current")
_MwRogueapVarsOperationalTime_Type = Unsigned32
_MwRogueapVarsOperationalTime_Object = MibScalar
mwRogueapVarsOperationalTime = _MwRogueapVarsOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 1, 6),
    _MwRogueapVarsOperationalTime_Type()
)
mwRogueapVarsOperationalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwRogueapVarsOperationalTime.setStatus("current")
_MwRogueapVarsMitigationFrames_Type = Unsigned32
_MwRogueapVarsMitigationFrames_Object = MibScalar
mwRogueapVarsMitigationFrames = _MwRogueapVarsMitigationFrames_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 1, 7),
    _MwRogueapVarsMitigationFrames_Type()
)
mwRogueapVarsMitigationFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwRogueapVarsMitigationFrames.setStatus("current")
_MwRogueapVarsScanChannelMask_Type = DisplayString
_MwRogueapVarsScanChannelMask_Object = MibScalar
mwRogueapVarsScanChannelMask = _MwRogueapVarsScanChannelMask_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 1, 8),
    _MwRogueapVarsScanChannelMask_Type()
)
mwRogueapVarsScanChannelMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwRogueapVarsScanChannelMask.setStatus("current")


class _MwRogueapVarsMinRSSI_Type(Integer32):
    """Custom type mwRogueapVarsMinRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 0),
    )


_MwRogueapVarsMinRSSI_Type.__name__ = "Integer32"
_MwRogueapVarsMinRSSI_Object = MibScalar
mwRogueapVarsMinRSSI = _MwRogueapVarsMinRSSI_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 1, 9),
    _MwRogueapVarsMinRSSI_Type()
)
mwRogueapVarsMinRSSI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwRogueapVarsMinRSSI.setStatus("current")
_MwRogueapAclTable_Object = MibTable
mwRogueapAclTable = _MwRogueapAclTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 2)
)
if mibBuilder.loadTexts:
    mwRogueapAclTable.setStatus("current")
_MwRogueapAclEntry_Object = MibTableRow
mwRogueapAclEntry = _MwRogueapAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 2, 1)
)
mwRogueapAclEntry.setIndexNames(
    (0, "MERU-CONFIG-ROGUEAP-MIB", "mwRogueapAclTableIndex"),
)
if mibBuilder.loadTexts:
    mwRogueapAclEntry.setStatus("current")
_MwRogueapAclTableIndex_Type = Integer32
_MwRogueapAclTableIndex_Object = MibTableColumn
mwRogueapAclTableIndex = _MwRogueapAclTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 2, 1, 1),
    _MwRogueapAclTableIndex_Type()
)
mwRogueapAclTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwRogueapAclTableIndex.setStatus("current")
_MwRogueapAclBssId_Type = MacAddress
_MwRogueapAclBssId_Object = MibTableColumn
mwRogueapAclBssId = _MwRogueapAclBssId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 2, 1, 2),
    _MwRogueapAclBssId_Type()
)
mwRogueapAclBssId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwRogueapAclBssId.setStatus("current")
_MwRogueapAclRowStatus_Type = RowStatus
_MwRogueapAclRowStatus_Object = MibTableColumn
mwRogueapAclRowStatus = _MwRogueapAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 2, 1, 3),
    _MwRogueapAclRowStatus_Type()
)
mwRogueapAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwRogueapAclRowStatus.setStatus("current")
_MwRogueapBlockTable_Object = MibTable
mwRogueapBlockTable = _MwRogueapBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 3)
)
if mibBuilder.loadTexts:
    mwRogueapBlockTable.setStatus("current")
_MwRogueapBlockEntry_Object = MibTableRow
mwRogueapBlockEntry = _MwRogueapBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 3, 1)
)
mwRogueapBlockEntry.setIndexNames(
    (0, "MERU-CONFIG-ROGUEAP-MIB", "mwRogueapBlockTableIndex"),
)
if mibBuilder.loadTexts:
    mwRogueapBlockEntry.setStatus("current")
_MwRogueapBlockTableIndex_Type = Integer32
_MwRogueapBlockTableIndex_Object = MibTableColumn
mwRogueapBlockTableIndex = _MwRogueapBlockTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 3, 1, 1),
    _MwRogueapBlockTableIndex_Type()
)
mwRogueapBlockTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwRogueapBlockTableIndex.setStatus("current")
_MwRogueapBlockBssId_Type = MacAddress
_MwRogueapBlockBssId_Object = MibTableColumn
mwRogueapBlockBssId = _MwRogueapBlockBssId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 3, 1, 2),
    _MwRogueapBlockBssId_Type()
)
mwRogueapBlockBssId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwRogueapBlockBssId.setStatus("current")
_MwRogueapBlockCreationDate_Type = DateAndTime
_MwRogueapBlockCreationDate_Object = MibTableColumn
mwRogueapBlockCreationDate = _MwRogueapBlockCreationDate_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 3, 1, 3),
    _MwRogueapBlockCreationDate_Type()
)
mwRogueapBlockCreationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRogueapBlockCreationDate.setStatus("current")
_MwRogueapBlockLastReported_Type = DateAndTime
_MwRogueapBlockLastReported_Object = MibTableColumn
mwRogueapBlockLastReported = _MwRogueapBlockLastReported_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 3, 1, 4),
    _MwRogueapBlockLastReported_Type()
)
mwRogueapBlockLastReported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRogueapBlockLastReported.setStatus("current")
_MwRogueapBlockRowStatus_Type = RowStatus
_MwRogueapBlockRowStatus_Object = MibTableColumn
mwRogueapBlockRowStatus = _MwRogueapBlockRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 3, 1, 5),
    _MwRogueapBlockRowStatus_Type()
)
mwRogueapBlockRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwRogueapBlockRowStatus.setStatus("current")
_MwRogueApListTable_Object = MibTable
mwRogueApListTable = _MwRogueApListTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 4)
)
if mibBuilder.loadTexts:
    mwRogueApListTable.setStatus("current")
_MwRogueApListEntry_Object = MibTableRow
mwRogueApListEntry = _MwRogueApListEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 4, 1)
)
mwRogueApListEntry.setIndexNames(
    (0, "MERU-CONFIG-ROGUEAP-MIB", "mwRogueApListTableIndex"),
)
if mibBuilder.loadTexts:
    mwRogueApListEntry.setStatus("current")
_MwRogueApListTableIndex_Type = Integer32
_MwRogueApListTableIndex_Object = MibTableColumn
mwRogueApListTableIndex = _MwRogueApListTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 4, 1, 1),
    _MwRogueApListTableIndex_Type()
)
mwRogueApListTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwRogueApListTableIndex.setStatus("current")
_MwRogueApListMac_Type = MacAddress
_MwRogueApListMac_Object = MibTableColumn
mwRogueApListMac = _MwRogueApListMac_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 4, 1, 2),
    _MwRogueApListMac_Type()
)
mwRogueApListMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRogueApListMac.setStatus("current")
_MwRogueApListEssid_Type = DisplayString
_MwRogueApListEssid_Object = MibTableColumn
mwRogueApListEssid = _MwRogueApListEssid_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 4, 1, 3),
    _MwRogueApListEssid_Type()
)
mwRogueApListEssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRogueApListEssid.setStatus("current")
_MwRogueApListBssid_Type = MacAddress
_MwRogueApListBssid_Object = MibTableColumn
mwRogueApListBssid = _MwRogueApListBssid_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 4, 1, 4),
    _MwRogueApListBssid_Type()
)
mwRogueApListBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRogueApListBssid.setStatus("current")
_MwRogueApListChannel_Type = Unsigned32
_MwRogueApListChannel_Object = MibTableColumn
mwRogueApListChannel = _MwRogueApListChannel_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 4, 1, 5),
    _MwRogueApListChannel_Type()
)
mwRogueApListChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRogueApListChannel.setStatus("current")
_MwRogueApListMeruAp1Id_Type = Integer32
_MwRogueApListMeruAp1Id_Object = MibTableColumn
mwRogueApListMeruAp1Id = _MwRogueApListMeruAp1Id_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 4, 1, 6),
    _MwRogueApListMeruAp1Id_Type()
)
mwRogueApListMeruAp1Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRogueApListMeruAp1Id.setStatus("current")
_MwRogueApListMeruAp2Id_Type = Integer32
_MwRogueApListMeruAp2Id_Object = MibTableColumn
mwRogueApListMeruAp2Id = _MwRogueApListMeruAp2Id_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 4, 1, 7),
    _MwRogueApListMeruAp2Id_Type()
)
mwRogueApListMeruAp2Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRogueApListMeruAp2Id.setStatus("current")
_MwRogueApListMeruAp3Id_Type = Integer32
_MwRogueApListMeruAp3Id_Object = MibTableColumn
mwRogueApListMeruAp3Id = _MwRogueApListMeruAp3Id_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 4, 1, 8),
    _MwRogueApListMeruAp3Id_Type()
)
mwRogueApListMeruAp3Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRogueApListMeruAp3Id.setStatus("current")
_MwRogueApListDeviceType_Type = MwlApType
_MwRogueApListDeviceType_Object = MibTableColumn
mwRogueApListDeviceType = _MwRogueApListDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 4, 1, 9),
    _MwRogueApListDeviceType_Type()
)
mwRogueApListDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRogueApListDeviceType.setStatus("current")
_MwRogueApListWiredRogue_Type = MwlOnOffSwitch
_MwRogueApListWiredRogue_Object = MibTableColumn
mwRogueApListWiredRogue = _MwRogueApListWiredRogue_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 4, 1, 10),
    _MwRogueApListWiredRogue_Type()
)
mwRogueApListWiredRogue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRogueApListWiredRogue.setStatus("current")
_MwRogueApListMeruAp1Rssi_Type = Integer32
_MwRogueApListMeruAp1Rssi_Object = MibTableColumn
mwRogueApListMeruAp1Rssi = _MwRogueApListMeruAp1Rssi_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 4, 1, 11),
    _MwRogueApListMeruAp1Rssi_Type()
)
mwRogueApListMeruAp1Rssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRogueApListMeruAp1Rssi.setStatus("current")
_MwRogueApListMeruAp2Rssi_Type = Integer32
_MwRogueApListMeruAp2Rssi_Object = MibTableColumn
mwRogueApListMeruAp2Rssi = _MwRogueApListMeruAp2Rssi_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 4, 1, 12),
    _MwRogueApListMeruAp2Rssi_Type()
)
mwRogueApListMeruAp2Rssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRogueApListMeruAp2Rssi.setStatus("current")
_MwRogueApListMeruAp3Rssi_Type = Integer32
_MwRogueApListMeruAp3Rssi_Object = MibTableColumn
mwRogueApListMeruAp3Rssi = _MwRogueApListMeruAp3Rssi_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 4, 1, 13),
    _MwRogueApListMeruAp3Rssi_Type()
)
mwRogueApListMeruAp3Rssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRogueApListMeruAp3Rssi.setStatus("current")
_MwRogueApListNonReportedAudits_Type = Unsigned32
_MwRogueApListNonReportedAudits_Object = MibTableColumn
mwRogueApListNonReportedAudits = _MwRogueApListNonReportedAudits_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 4, 1, 14),
    _MwRogueApListNonReportedAudits_Type()
)
mwRogueApListNonReportedAudits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRogueApListNonReportedAudits.setStatus("current")
_MwRogueApListMeruAp1LastActivity_Type = TimeTicks
_MwRogueApListMeruAp1LastActivity_Object = MibTableColumn
mwRogueApListMeruAp1LastActivity = _MwRogueApListMeruAp1LastActivity_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 4, 1, 15),
    _MwRogueApListMeruAp1LastActivity_Type()
)
mwRogueApListMeruAp1LastActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRogueApListMeruAp1LastActivity.setStatus("current")
_MwRogueApListMeruAp2LastActivity_Type = TimeTicks
_MwRogueApListMeruAp2LastActivity_Object = MibTableColumn
mwRogueApListMeruAp2LastActivity = _MwRogueApListMeruAp2LastActivity_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 4, 1, 16),
    _MwRogueApListMeruAp2LastActivity_Type()
)
mwRogueApListMeruAp2LastActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRogueApListMeruAp2LastActivity.setStatus("current")
_MwRogueApListMeruAp3LastActivity_Type = TimeTicks
_MwRogueApListMeruAp3LastActivity_Object = MibTableColumn
mwRogueApListMeruAp3LastActivity = _MwRogueApListMeruAp3LastActivity_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 7, 4, 1, 17),
    _MwRogueApListMeruAp3LastActivity_Type()
)
mwRogueApListMeruAp3LastActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRogueApListMeruAp3LastActivity.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-CONFIG-ROGUEAP-MIB",
    **{"mwConfigRogueAp": mwConfigRogueAp,
       "mwRogueapVars": mwRogueapVars,
       "mwRogueapVarsDetection": mwRogueapVarsDetection,
       "mwRogueapVarsBlock": mwRogueapVarsBlock,
       "mwRogueapVarsAging": mwRogueapVarsAging,
       "mwRogueapVarsMitigateAps": mwRogueapVarsMitigateAps,
       "mwRogueapVarsScanningTime": mwRogueapVarsScanningTime,
       "mwRogueapVarsOperationalTime": mwRogueapVarsOperationalTime,
       "mwRogueapVarsMitigationFrames": mwRogueapVarsMitigationFrames,
       "mwRogueapVarsScanChannelMask": mwRogueapVarsScanChannelMask,
       "mwRogueapVarsMinRSSI": mwRogueapVarsMinRSSI,
       "mwRogueapAclTable": mwRogueapAclTable,
       "mwRogueapAclEntry": mwRogueapAclEntry,
       "mwRogueapAclTableIndex": mwRogueapAclTableIndex,
       "mwRogueapAclBssId": mwRogueapAclBssId,
       "mwRogueapAclRowStatus": mwRogueapAclRowStatus,
       "mwRogueapBlockTable": mwRogueapBlockTable,
       "mwRogueapBlockEntry": mwRogueapBlockEntry,
       "mwRogueapBlockTableIndex": mwRogueapBlockTableIndex,
       "mwRogueapBlockBssId": mwRogueapBlockBssId,
       "mwRogueapBlockCreationDate": mwRogueapBlockCreationDate,
       "mwRogueapBlockLastReported": mwRogueapBlockLastReported,
       "mwRogueapBlockRowStatus": mwRogueapBlockRowStatus,
       "mwRogueApListTable": mwRogueApListTable,
       "mwRogueApListEntry": mwRogueApListEntry,
       "mwRogueApListTableIndex": mwRogueApListTableIndex,
       "mwRogueApListMac": mwRogueApListMac,
       "mwRogueApListEssid": mwRogueApListEssid,
       "mwRogueApListBssid": mwRogueApListBssid,
       "mwRogueApListChannel": mwRogueApListChannel,
       "mwRogueApListMeruAp1Id": mwRogueApListMeruAp1Id,
       "mwRogueApListMeruAp2Id": mwRogueApListMeruAp2Id,
       "mwRogueApListMeruAp3Id": mwRogueApListMeruAp3Id,
       "mwRogueApListDeviceType": mwRogueApListDeviceType,
       "mwRogueApListWiredRogue": mwRogueApListWiredRogue,
       "mwRogueApListMeruAp1Rssi": mwRogueApListMeruAp1Rssi,
       "mwRogueApListMeruAp2Rssi": mwRogueApListMeruAp2Rssi,
       "mwRogueApListMeruAp3Rssi": mwRogueApListMeruAp3Rssi,
       "mwRogueApListNonReportedAudits": mwRogueApListNonReportedAudits,
       "mwRogueApListMeruAp1LastActivity": mwRogueApListMeruAp1LastActivity,
       "mwRogueApListMeruAp2LastActivity": mwRogueApListMeruAp2LastActivity,
       "mwRogueApListMeruAp3LastActivity": mwRogueApListMeruAp3LastActivity}
)
