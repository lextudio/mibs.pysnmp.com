# SNMP MIB module (Hitachi-DF-RAID-LAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Hitachi-DF-RAID-LAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:52 2024
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
 NotificationType,
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
    "NotificationType",
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

_Hitachi_ObjectIdentity = ObjectIdentity
hitachi = _Hitachi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 3)
)
_Storage_ObjectIdentity = ObjectIdentity
storage = _Storage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 3, 11)
)
_Dfraid_ObjectIdentity = ObjectIdentity
dfraid = _Dfraid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 1)
)
_DfraidLan_ObjectIdentity = ObjectIdentity
dfraidLan = _DfraidLan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2)
)
_SystemExMib_ObjectIdentity = ObjectIdentity
systemExMib = _SystemExMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5)
)
_StorageExMib_ObjectIdentity = ObjectIdentity
storageExMib = _StorageExMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11)
)
_DfraidExMib_ObjectIdentity = ObjectIdentity
dfraidExMib = _DfraidExMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1)
)
_DfraidLanExMib_ObjectIdentity = ObjectIdentity
dfraidLanExMib = _DfraidLanExMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2)
)
_DfSystemParameter_ObjectIdentity = ObjectIdentity
dfSystemParameter = _DfSystemParameter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 1)
)


class _DfSystemProductName_Type(DisplayString):
    """Custom type dfSystemProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_DfSystemProductName_Type.__name__ = "DisplayString"
_DfSystemProductName_Object = MibScalar
dfSystemProductName = _DfSystemProductName_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 1, 1),
    _DfSystemProductName_Type()
)
dfSystemProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfSystemProductName.setStatus("mandatory")


class _DfSystemMicroRevision_Type(DisplayString):
    """Custom type dfSystemMicroRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_DfSystemMicroRevision_Type.__name__ = "DisplayString"
_DfSystemMicroRevision_Object = MibScalar
dfSystemMicroRevision = _DfSystemMicroRevision_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 1, 2),
    _DfSystemMicroRevision_Type()
)
dfSystemMicroRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfSystemMicroRevision.setStatus("mandatory")
_DfSystemSerialNumber_Type = Integer32
_DfSystemSerialNumber_Object = MibScalar
dfSystemSerialNumber = _DfSystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 1, 3),
    _DfSystemSerialNumber_Type()
)
dfSystemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfSystemSerialNumber.setStatus("mandatory")
_DfWarningCondition_ObjectIdentity = ObjectIdentity
dfWarningCondition = _DfWarningCondition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 2)
)
_DfRegressionStatus_Type = Integer32
_DfRegressionStatus_Object = MibScalar
dfRegressionStatus = _DfRegressionStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 2, 1),
    _DfRegressionStatus_Type()
)
dfRegressionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfRegressionStatus.setStatus("mandatory")
_DfPreventiveMaintenanceInformation_Type = Integer32
_DfPreventiveMaintenanceInformation_Object = MibScalar
dfPreventiveMaintenanceInformation = _DfPreventiveMaintenanceInformation_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 2, 2),
    _DfPreventiveMaintenanceInformation_Type()
)
dfPreventiveMaintenanceInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfPreventiveMaintenanceInformation.setStatus("mandatory")
_DfWarningReserve1_Type = Integer32
_DfWarningReserve1_Object = MibScalar
dfWarningReserve1 = _DfWarningReserve1_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 2, 3),
    _DfWarningReserve1_Type()
)
dfWarningReserve1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfWarningReserve1.setStatus("mandatory")
_DfWarningReserve2_Type = Integer32
_DfWarningReserve2_Object = MibScalar
dfWarningReserve2 = _DfWarningReserve2_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 2, 4),
    _DfWarningReserve2_Type()
)
dfWarningReserve2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfWarningReserve2.setStatus("mandatory")
_DfCommandExecutionCondition_ObjectIdentity = ObjectIdentity
dfCommandExecutionCondition = _DfCommandExecutionCondition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 3)
)
_DfCommandTable_Object = MibTable
dfCommandTable = _DfCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    dfCommandTable.setStatus("mandatory")
_DfCommandEntry_Object = MibTableRow
dfCommandEntry = _DfCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 3, 1, 1)
)
dfCommandEntry.setIndexNames(
    (0, "Hitachi-DF-RAID-LAN-MIB", "dfLun"),
)
if mibBuilder.loadTexts:
    dfCommandEntry.setStatus("mandatory")
_DfLun_Type = Integer32
_DfLun_Object = MibTableColumn
dfLun = _DfLun_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 3, 1, 1, 1),
    _DfLun_Type()
)
dfLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfLun.setStatus("mandatory")
_DfReadCommandNumber_Type = Integer32
_DfReadCommandNumber_Object = MibTableColumn
dfReadCommandNumber = _DfReadCommandNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 3, 1, 1, 2),
    _DfReadCommandNumber_Type()
)
dfReadCommandNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfReadCommandNumber.setStatus("mandatory")
_DfReadHitNumber_Type = Integer32
_DfReadHitNumber_Object = MibTableColumn
dfReadHitNumber = _DfReadHitNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 3, 1, 1, 3),
    _DfReadHitNumber_Type()
)
dfReadHitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfReadHitNumber.setStatus("mandatory")
_DfReadHitRate_Type = Integer32
_DfReadHitRate_Object = MibTableColumn
dfReadHitRate = _DfReadHitRate_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 3, 1, 1, 4),
    _DfReadHitRate_Type()
)
dfReadHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfReadHitRate.setStatus("mandatory")
_DfWriteCommandNumber_Type = Integer32
_DfWriteCommandNumber_Object = MibTableColumn
dfWriteCommandNumber = _DfWriteCommandNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 3, 1, 1, 5),
    _DfWriteCommandNumber_Type()
)
dfWriteCommandNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfWriteCommandNumber.setStatus("mandatory")
_DfWriteHitNumber_Type = Integer32
_DfWriteHitNumber_Object = MibTableColumn
dfWriteHitNumber = _DfWriteHitNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 3, 1, 1, 6),
    _DfWriteHitNumber_Type()
)
dfWriteHitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfWriteHitNumber.setStatus("mandatory")
_DfWriteHitRate_Type = Integer32
_DfWriteHitRate_Object = MibTableColumn
dfWriteHitRate = _DfWriteHitRate_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 3, 1, 1, 7),
    _DfWriteHitRate_Type()
)
dfWriteHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfWriteHitRate.setStatus("mandatory")
_DfCacheLoadCondition_ObjectIdentity = ObjectIdentity
dfCacheLoadCondition = _DfCacheLoadCondition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 4)
)
_DfWriteDataRate_Type = Integer32
_DfWriteDataRate_Object = MibScalar
dfWriteDataRate = _DfWriteDataRate_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 4, 1),
    _DfWriteDataRate_Type()
)
dfWriteDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfWriteDataRate.setStatus("mandatory")
_DfLUNS_ObjectIdentity = ObjectIdentity
dfLUNS = _DfLUNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5)
)
_DfLUNSSwitch_Object = MibTable
dfLUNSSwitch = _DfLUNSSwitch_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    dfLUNSSwitch.setStatus("mandatory")
_DfLUNSSwitchEntry_Object = MibTableRow
dfLUNSSwitchEntry = _DfLUNSSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 1, 1)
)
dfLUNSSwitchEntry.setIndexNames(
    (0, "Hitachi-DF-RAID-LAN-MIB", "dfSwitchSerialNumber"),
    (0, "Hitachi-DF-RAID-LAN-MIB", "dfSwitchPortID"),
)
if mibBuilder.loadTexts:
    dfLUNSSwitchEntry.setStatus("mandatory")
_DfSwitchSerialNumber_Type = Integer32
_DfSwitchSerialNumber_Object = MibTableColumn
dfSwitchSerialNumber = _DfSwitchSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 1, 1, 1),
    _DfSwitchSerialNumber_Type()
)
dfSwitchSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfSwitchSerialNumber.setStatus("mandatory")
_DfSwitchPortID_Type = Integer32
_DfSwitchPortID_Object = MibTableColumn
dfSwitchPortID = _DfSwitchPortID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 1, 1, 2),
    _DfSwitchPortID_Type()
)
dfSwitchPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfSwitchPortID.setStatus("mandatory")
_DfSwitchOnOff_Type = Integer32
_DfSwitchOnOff_Object = MibTableColumn
dfSwitchOnOff = _DfSwitchOnOff_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 1, 1, 3),
    _DfSwitchOnOff_Type()
)
dfSwitchOnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfSwitchOnOff.setStatus("mandatory")
_DfSwitchControlStatus_Type = Integer32
_DfSwitchControlStatus_Object = MibTableColumn
dfSwitchControlStatus = _DfSwitchControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 1, 1, 4),
    _DfSwitchControlStatus_Type()
)
dfSwitchControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfSwitchControlStatus.setStatus("mandatory")
_DfLUNSWWN_Object = MibTable
dfLUNSWWN = _DfLUNSWWN_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    dfLUNSWWN.setStatus("mandatory")
_DfLUNSWWNEntry_Object = MibTableRow
dfLUNSWWNEntry = _DfLUNSWWNEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 2, 1)
)
dfLUNSWWNEntry.setIndexNames(
    (0, "Hitachi-DF-RAID-LAN-MIB", "dfWWNSerialNumber"),
    (0, "Hitachi-DF-RAID-LAN-MIB", "dfWWNPortID"),
    (0, "Hitachi-DF-RAID-LAN-MIB", "dfWWNControlIndex"),
)
if mibBuilder.loadTexts:
    dfLUNSWWNEntry.setStatus("mandatory")
_DfWWNSerialNumber_Type = Integer32
_DfWWNSerialNumber_Object = MibTableColumn
dfWWNSerialNumber = _DfWWNSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 2, 1, 1),
    _DfWWNSerialNumber_Type()
)
dfWWNSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfWWNSerialNumber.setStatus("mandatory")
_DfWWNPortID_Type = Integer32
_DfWWNPortID_Object = MibTableColumn
dfWWNPortID = _DfWWNPortID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 2, 1, 2),
    _DfWWNPortID_Type()
)
dfWWNPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfWWNPortID.setStatus("mandatory")
_DfWWNControlIndex_Type = Integer32
_DfWWNControlIndex_Object = MibTableColumn
dfWWNControlIndex = _DfWWNControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 2, 1, 3),
    _DfWWNControlIndex_Type()
)
dfWWNControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfWWNControlIndex.setStatus("mandatory")


class _DfWWNWWN_Type(OctetString):
    """Custom type dfWWNWWN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DfWWNWWN_Type.__name__ = "OctetString"
_DfWWNWWN_Object = MibTableColumn
dfWWNWWN = _DfWWNWWN_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 2, 1, 4),
    _DfWWNWWN_Type()
)
dfWWNWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfWWNWWN.setStatus("mandatory")
_DfWWNID_Type = Integer32
_DfWWNID_Object = MibTableColumn
dfWWNID = _DfWWNID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 2, 1, 5),
    _DfWWNID_Type()
)
dfWWNID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfWWNID.setStatus("mandatory")


class _DfWWNNickname_Type(DisplayString):
    """Custom type dfWWNNickname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DfWWNNickname_Type.__name__ = "DisplayString"
_DfWWNNickname_Object = MibTableColumn
dfWWNNickname = _DfWWNNickname_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 2, 1, 6),
    _DfWWNNickname_Type()
)
dfWWNNickname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfWWNNickname.setStatus("deprecated")
_DfWWNUseNickname_Type = Integer32
_DfWWNUseNickname_Object = MibTableColumn
dfWWNUseNickname = _DfWWNUseNickname_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 2, 1, 7),
    _DfWWNUseNickname_Type()
)
dfWWNUseNickname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfWWNUseNickname.setStatus("mandatory")
_DfWWNControlStatus_Type = Integer32
_DfWWNControlStatus_Object = MibTableColumn
dfWWNControlStatus = _DfWWNControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 2, 1, 8),
    _DfWWNControlStatus_Type()
)
dfWWNControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfWWNControlStatus.setStatus("mandatory")
_DfLUNSWWNGroup_Object = MibTable
dfLUNSWWNGroup = _DfLUNSWWNGroup_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 3)
)
if mibBuilder.loadTexts:
    dfLUNSWWNGroup.setStatus("mandatory")
_DfLUNSWWNGroupEntry_Object = MibTableRow
dfLUNSWWNGroupEntry = _DfLUNSWWNGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 3, 1)
)
dfLUNSWWNGroupEntry.setIndexNames(
    (0, "Hitachi-DF-RAID-LAN-MIB", "dfWWNGroupSerialNumber"),
    (0, "Hitachi-DF-RAID-LAN-MIB", "dfWWNGroupPortID"),
    (0, "Hitachi-DF-RAID-LAN-MIB", "dfWWNGroupControlIndex"),
)
if mibBuilder.loadTexts:
    dfLUNSWWNGroupEntry.setStatus("mandatory")
_DfWWNGroupSerialNumber_Type = Integer32
_DfWWNGroupSerialNumber_Object = MibTableColumn
dfWWNGroupSerialNumber = _DfWWNGroupSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 3, 1, 1),
    _DfWWNGroupSerialNumber_Type()
)
dfWWNGroupSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfWWNGroupSerialNumber.setStatus("mandatory")
_DfWWNGroupPortID_Type = Integer32
_DfWWNGroupPortID_Object = MibTableColumn
dfWWNGroupPortID = _DfWWNGroupPortID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 3, 1, 2),
    _DfWWNGroupPortID_Type()
)
dfWWNGroupPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfWWNGroupPortID.setStatus("mandatory")
_DfWWNGroupControlIndex_Type = Integer32
_DfWWNGroupControlIndex_Object = MibTableColumn
dfWWNGroupControlIndex = _DfWWNGroupControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 3, 1, 3),
    _DfWWNGroupControlIndex_Type()
)
dfWWNGroupControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfWWNGroupControlIndex.setStatus("mandatory")
_DfWWNGroupID_Type = Integer32
_DfWWNGroupID_Object = MibTableColumn
dfWWNGroupID = _DfWWNGroupID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 3, 1, 4),
    _DfWWNGroupID_Type()
)
dfWWNGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfWWNGroupID.setStatus("mandatory")


class _DfWWNGroupNickname_Type(DisplayString):
    """Custom type dfWWNGroupNickname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DfWWNGroupNickname_Type.__name__ = "DisplayString"
_DfWWNGroupNickname_Object = MibTableColumn
dfWWNGroupNickname = _DfWWNGroupNickname_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 3, 1, 5),
    _DfWWNGroupNickname_Type()
)
dfWWNGroupNickname.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfWWNGroupNickname.setStatus("mandatory")


class _DfWWNGroupedWWNs_Type(OctetString):
    """Custom type dfWWNGroupedWWNs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_DfWWNGroupedWWNs_Type.__name__ = "OctetString"
_DfWWNGroupedWWNs_Object = MibTableColumn
dfWWNGroupedWWNs = _DfWWNGroupedWWNs_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 3, 1, 6),
    _DfWWNGroupedWWNs_Type()
)
dfWWNGroupedWWNs.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfWWNGroupedWWNs.setStatus("mandatory")
_DfWWNGroupControlStatus_Type = Integer32
_DfWWNGroupControlStatus_Object = MibTableColumn
dfWWNGroupControlStatus = _DfWWNGroupControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 3, 1, 7),
    _DfWWNGroupControlStatus_Type()
)
dfWWNGroupControlStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfWWNGroupControlStatus.setStatus("mandatory")
_DfLUNSLUN_Object = MibTable
dfLUNSLUN = _DfLUNSLUN_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 4)
)
if mibBuilder.loadTexts:
    dfLUNSLUN.setStatus("mandatory")
_DfLUNSLUNEntry_Object = MibTableRow
dfLUNSLUNEntry = _DfLUNSLUNEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 4, 1)
)
dfLUNSLUNEntry.setIndexNames(
    (0, "Hitachi-DF-RAID-LAN-MIB", "dfLUNSerialNumber"),
    (0, "Hitachi-DF-RAID-LAN-MIB", "dfLUNPortID"),
    (0, "Hitachi-DF-RAID-LAN-MIB", "dfLUNLUN"),
)
if mibBuilder.loadTexts:
    dfLUNSLUNEntry.setStatus("mandatory")
_DfLUNSerialNumber_Type = Integer32
_DfLUNSerialNumber_Object = MibTableColumn
dfLUNSerialNumber = _DfLUNSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 4, 1, 1),
    _DfLUNSerialNumber_Type()
)
dfLUNSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfLUNSerialNumber.setStatus("mandatory")
_DfLUNPortID_Type = Integer32
_DfLUNPortID_Object = MibTableColumn
dfLUNPortID = _DfLUNPortID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 4, 1, 2),
    _DfLUNPortID_Type()
)
dfLUNPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfLUNPortID.setStatus("mandatory")
_DfLUNLUN_Type = Integer32
_DfLUNLUN_Object = MibTableColumn
dfLUNLUN = _DfLUNLUN_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 4, 1, 3),
    _DfLUNLUN_Type()
)
dfLUNLUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfLUNLUN.setStatus("mandatory")


class _DfLUNWWNSecurity_Type(OctetString):
    """Custom type dfLUNWWNSecurity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DfLUNWWNSecurity_Type.__name__ = "OctetString"
_DfLUNWWNSecurity_Object = MibTableColumn
dfLUNWWNSecurity = _DfLUNWWNSecurity_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 4, 1, 4),
    _DfLUNWWNSecurity_Type()
)
dfLUNWWNSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfLUNWWNSecurity.setStatus("mandatory")


class _DfLUNWWNGroupSecurity_Type(OctetString):
    """Custom type dfLUNWWNGroupSecurity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_DfLUNWWNGroupSecurity_Type.__name__ = "OctetString"
_DfLUNWWNGroupSecurity_Object = MibTableColumn
dfLUNWWNGroupSecurity = _DfLUNWWNGroupSecurity_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 4, 1, 5),
    _DfLUNWWNGroupSecurity_Type()
)
dfLUNWWNGroupSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfLUNWWNGroupSecurity.setStatus("mandatory")
_DfLUNControlStatus_Type = Integer32
_DfLUNControlStatus_Object = MibTableColumn
dfLUNControlStatus = _DfLUNControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 4, 1, 6),
    _DfLUNControlStatus_Type()
)
dfLUNControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfLUNControlStatus.setStatus("mandatory")
_DfLUNSLUNGroup_Object = MibTable
dfLUNSLUNGroup = _DfLUNSLUNGroup_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 5)
)
if mibBuilder.loadTexts:
    dfLUNSLUNGroup.setStatus("mandatory")
_DfLUNSLUNGroupEntry_Object = MibTableRow
dfLUNSLUNGroupEntry = _DfLUNSLUNGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 5, 1)
)
dfLUNSLUNGroupEntry.setIndexNames(
    (0, "Hitachi-DF-RAID-LAN-MIB", "dfLUNGroupSerialNumber"),
    (0, "Hitachi-DF-RAID-LAN-MIB", "dfLUNGroupPortID"),
    (0, "Hitachi-DF-RAID-LAN-MIB", "dfLUNGroupControlIndex"),
)
if mibBuilder.loadTexts:
    dfLUNSLUNGroupEntry.setStatus("mandatory")
_DfLUNGroupSerialNumber_Type = Integer32
_DfLUNGroupSerialNumber_Object = MibTableColumn
dfLUNGroupSerialNumber = _DfLUNGroupSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 5, 1, 1),
    _DfLUNGroupSerialNumber_Type()
)
dfLUNGroupSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfLUNGroupSerialNumber.setStatus("mandatory")
_DfLUNGroupPortID_Type = Integer32
_DfLUNGroupPortID_Object = MibTableColumn
dfLUNGroupPortID = _DfLUNGroupPortID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 5, 1, 2),
    _DfLUNGroupPortID_Type()
)
dfLUNGroupPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfLUNGroupPortID.setStatus("mandatory")
_DfLUNGroupControlIndex_Type = Integer32
_DfLUNGroupControlIndex_Object = MibTableColumn
dfLUNGroupControlIndex = _DfLUNGroupControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 5, 1, 3),
    _DfLUNGroupControlIndex_Type()
)
dfLUNGroupControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfLUNGroupControlIndex.setStatus("mandatory")
_DfLUNGroupID_Type = Integer32
_DfLUNGroupID_Object = MibTableColumn
dfLUNGroupID = _DfLUNGroupID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 5, 1, 4),
    _DfLUNGroupID_Type()
)
dfLUNGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfLUNGroupID.setStatus("mandatory")


class _DfLUNGroupNickname_Type(DisplayString):
    """Custom type dfLUNGroupNickname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DfLUNGroupNickname_Type.__name__ = "DisplayString"
_DfLUNGroupNickname_Object = MibTableColumn
dfLUNGroupNickname = _DfLUNGroupNickname_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 5, 1, 5),
    _DfLUNGroupNickname_Type()
)
dfLUNGroupNickname.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfLUNGroupNickname.setStatus("deprecated")


class _DfLUNGroupedLUNs_Type(OctetString):
    """Custom type dfLUNGroupedLUNs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DfLUNGroupedLUNs_Type.__name__ = "OctetString"
_DfLUNGroupedLUNs_Object = MibTableColumn
dfLUNGroupedLUNs = _DfLUNGroupedLUNs_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 5, 1, 6),
    _DfLUNGroupedLUNs_Type()
)
dfLUNGroupedLUNs.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfLUNGroupedLUNs.setStatus("mandatory")


class _DfLUNGroupWWNSecurity_Type(OctetString):
    """Custom type dfLUNGroupWWNSecurity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_DfLUNGroupWWNSecurity_Type.__name__ = "OctetString"
_DfLUNGroupWWNSecurity_Object = MibTableColumn
dfLUNGroupWWNSecurity = _DfLUNGroupWWNSecurity_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 5, 1, 7),
    _DfLUNGroupWWNSecurity_Type()
)
dfLUNGroupWWNSecurity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfLUNGroupWWNSecurity.setStatus("mandatory")


class _DfLUNGroupWWNGroupSecurity_Type(OctetString):
    """Custom type dfLUNGroupWWNGroupSecurity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_DfLUNGroupWWNGroupSecurity_Type.__name__ = "OctetString"
_DfLUNGroupWWNGroupSecurity_Object = MibTableColumn
dfLUNGroupWWNGroupSecurity = _DfLUNGroupWWNGroupSecurity_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 5, 1, 8),
    _DfLUNGroupWWNGroupSecurity_Type()
)
dfLUNGroupWWNGroupSecurity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfLUNGroupWWNGroupSecurity.setStatus("mandatory")
_DfLUNGroupControlStatus_Type = Integer32
_DfLUNGroupControlStatus_Object = MibTableColumn
dfLUNGroupControlStatus = _DfLUNGroupControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 5, 1, 9),
    _DfLUNGroupControlStatus_Type()
)
dfLUNGroupControlStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfLUNGroupControlStatus.setStatus("mandatory")
_DfPort_ObjectIdentity = ObjectIdentity
dfPort = _DfPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 6)
)
_DfPortinf_Object = MibTable
dfPortinf = _DfPortinf_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    dfPortinf.setStatus("mandatory")
_DfPortinfEntry_Object = MibTableRow
dfPortinfEntry = _DfPortinfEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 6, 1, 1)
)
dfPortinfEntry.setIndexNames(
    (0, "Hitachi-DF-RAID-LAN-MIB", "dfPortSerialNumber"),
    (0, "Hitachi-DF-RAID-LAN-MIB", "dfPortID"),
)
if mibBuilder.loadTexts:
    dfPortinfEntry.setStatus("mandatory")
_DfPortSerialNumber_Type = Integer32
_DfPortSerialNumber_Object = MibTableColumn
dfPortSerialNumber = _DfPortSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 6, 1, 1, 1),
    _DfPortSerialNumber_Type()
)
dfPortSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfPortSerialNumber.setStatus("mandatory")
_DfPortID_Type = Integer32
_DfPortID_Object = MibTableColumn
dfPortID = _DfPortID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 6, 1, 1, 2),
    _DfPortID_Type()
)
dfPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfPortID.setStatus("mandatory")


class _DfPortKind_Type(DisplayString):
    """Custom type dfPortKind based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DfPortKind_Type.__name__ = "DisplayString"
_DfPortKind_Object = MibTableColumn
dfPortKind = _DfPortKind_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 6, 1, 1, 3),
    _DfPortKind_Type()
)
dfPortKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfPortKind.setStatus("mandatory")


class _DfPortHostMode_Type(OctetString):
    """Custom type dfPortHostMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_DfPortHostMode_Type.__name__ = "OctetString"
_DfPortHostMode_Object = MibTableColumn
dfPortHostMode = _DfPortHostMode_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 6, 1, 1, 4),
    _DfPortHostMode_Type()
)
dfPortHostMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfPortHostMode.setStatus("mandatory")
_DfPortFibreAddress_Type = Integer32
_DfPortFibreAddress_Object = MibTableColumn
dfPortFibreAddress = _DfPortFibreAddress_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 6, 1, 1, 5),
    _DfPortFibreAddress_Type()
)
dfPortFibreAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfPortFibreAddress.setStatus("mandatory")
_DfPortFibreTopology_Type = Integer32
_DfPortFibreTopology_Object = MibTableColumn
dfPortFibreTopology = _DfPortFibreTopology_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 6, 1, 1, 6),
    _DfPortFibreTopology_Type()
)
dfPortFibreTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfPortFibreTopology.setStatus("mandatory")
_DfPortControlStatus_Type = Integer32
_DfPortControlStatus_Object = MibTableColumn
dfPortControlStatus = _DfPortControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 6, 1, 1, 7),
    _DfPortControlStatus_Type()
)
dfPortControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfPortControlStatus.setStatus("mandatory")


class _DfPortDisplayName_Type(DisplayString):
    """Custom type dfPortDisplayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DfPortDisplayName_Type.__name__ = "DisplayString"
_DfPortDisplayName_Object = MibTableColumn
dfPortDisplayName = _DfPortDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 6, 1, 1, 8),
    _DfPortDisplayName_Type()
)
dfPortDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfPortDisplayName.setStatus("mandatory")


class _DfPortWWN_Type(OctetString):
    """Custom type dfPortWWN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DfPortWWN_Type.__name__ = "OctetString"
_DfPortWWN_Object = MibTableColumn
dfPortWWN = _DfPortWWN_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 6, 1, 1, 9),
    _DfPortWWN_Type()
)
dfPortWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfPortWWN.setStatus("mandatory")
_DfCommandExecutionInternalCondition_ObjectIdentity = ObjectIdentity
dfCommandExecutionInternalCondition = _DfCommandExecutionInternalCondition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 7)
)
_DfCommandInternalTable_Object = MibTable
dfCommandInternalTable = _DfCommandInternalTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    dfCommandInternalTable.setStatus("mandatory")
_DfCommandInternalEntry_Object = MibTableRow
dfCommandInternalEntry = _DfCommandInternalEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 7, 1, 1)
)
dfCommandInternalEntry.setIndexNames(
    (0, "Hitachi-DF-RAID-LAN-MIB", "dfInternalLun"),
)
if mibBuilder.loadTexts:
    dfCommandInternalEntry.setStatus("mandatory")
_DfInternalLun_Type = Integer32
_DfInternalLun_Object = MibTableColumn
dfInternalLun = _DfInternalLun_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 7, 1, 1, 1),
    _DfInternalLun_Type()
)
dfInternalLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfInternalLun.setStatus("mandatory")
_DfInternalReadCommandNumber_Type = Integer32
_DfInternalReadCommandNumber_Object = MibTableColumn
dfInternalReadCommandNumber = _DfInternalReadCommandNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 7, 1, 1, 2),
    _DfInternalReadCommandNumber_Type()
)
dfInternalReadCommandNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfInternalReadCommandNumber.setStatus("mandatory")
_DfInternalReadHitNumber_Type = Integer32
_DfInternalReadHitNumber_Object = MibTableColumn
dfInternalReadHitNumber = _DfInternalReadHitNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 7, 1, 1, 3),
    _DfInternalReadHitNumber_Type()
)
dfInternalReadHitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfInternalReadHitNumber.setStatus("mandatory")
_DfInternalReadHitRate_Type = Integer32
_DfInternalReadHitRate_Object = MibTableColumn
dfInternalReadHitRate = _DfInternalReadHitRate_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 7, 1, 1, 4),
    _DfInternalReadHitRate_Type()
)
dfInternalReadHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfInternalReadHitRate.setStatus("mandatory")
_DfInternalWriteCommandNumber_Type = Integer32
_DfInternalWriteCommandNumber_Object = MibTableColumn
dfInternalWriteCommandNumber = _DfInternalWriteCommandNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 7, 1, 1, 5),
    _DfInternalWriteCommandNumber_Type()
)
dfInternalWriteCommandNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfInternalWriteCommandNumber.setStatus("mandatory")
_DfInternalWriteHitNumber_Type = Integer32
_DfInternalWriteHitNumber_Object = MibTableColumn
dfInternalWriteHitNumber = _DfInternalWriteHitNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 7, 1, 1, 6),
    _DfInternalWriteHitNumber_Type()
)
dfInternalWriteHitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfInternalWriteHitNumber.setStatus("mandatory")
_DfInternalWriteHitRate_Type = Integer32
_DfInternalWriteHitRate_Object = MibTableColumn
dfInternalWriteHitRate = _DfInternalWriteHitRate_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 7, 1, 1, 7),
    _DfInternalWriteHitRate_Type()
)
dfInternalWriteHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfInternalWriteHitRate.setStatus("mandatory")

# Managed Objects groups


# Notification objects

systemDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2, 0, 1)
)
if mibBuilder.loadTexts:
    systemDown.setStatus(
        ""
    )

driveFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2, 0, 2)
)
if mibBuilder.loadTexts:
    driveFailure.setStatus(
        ""
    )

fanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2, 0, 3)
)
if mibBuilder.loadTexts:
    fanFailure.setStatus(
        ""
    )

powerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2, 0, 4)
)
if mibBuilder.loadTexts:
    powerSupplyFailure.setStatus(
        ""
    )

batteryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2, 0, 5)
)
if mibBuilder.loadTexts:
    batteryFailure.setStatus(
        ""
    )

cacheFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2, 0, 6)
)
if mibBuilder.loadTexts:
    cacheFailure.setStatus(
        ""
    )

upsFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2, 0, 7)
)
if mibBuilder.loadTexts:
    upsFailure.setStatus(
        ""
    )

inboxFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2, 0, 8)
)
if mibBuilder.loadTexts:
    inboxFailure.setStatus(
        ""
    )

backupCircuitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2, 0, 9)
)
if mibBuilder.loadTexts:
    backupCircuitFailure.setStatus(
        ""
    )

otherControllerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2, 0, 10)
)
if mibBuilder.loadTexts:
    otherControllerFailure.setStatus(
        ""
    )

warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2, 0, 11)
)
if mibBuilder.loadTexts:
    warning.setStatus(
        ""
    )

spareDriveFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2, 0, 12)
)
if mibBuilder.loadTexts:
    spareDriveFailure.setStatus(
        ""
    )

microprogramReplacementExecuted = NotificationType(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2, 0, 13)
)
if mibBuilder.loadTexts:
    microprogramReplacementExecuted.setStatus(
        ""
    )

encFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2, 0, 14)
)
if mibBuilder.loadTexts:
    encFailure.setStatus(
        ""
    )

loopFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2, 0, 15)
)
if mibBuilder.loadTexts:
    loopFailure.setStatus(
        ""
    )

pathFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2, 0, 16)
)
if mibBuilder.loadTexts:
    pathFailure.setStatus(
        ""
    )

drivePreMainte = NotificationType(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2, 0, 21)
)
if mibBuilder.loadTexts:
    drivePreMainte.setStatus(
        ""
    )

nasServerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2, 0, 200)
)
if mibBuilder.loadTexts:
    nasServerFailure.setStatus(
        ""
    )

nasPathFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2, 0, 201)
)
if mibBuilder.loadTexts:
    nasPathFailure.setStatus(
        ""
    )

nasUpsFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2, 0, 202)
)
if mibBuilder.loadTexts:
    nasUpsFailure.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Hitachi-DF-RAID-LAN-MIB",
    **{"hitachi": hitachi,
       "system": system,
       "storage": storage,
       "dfraid": dfraid,
       "dfraidLan": dfraidLan,
       "systemDown": systemDown,
       "driveFailure": driveFailure,
       "fanFailure": fanFailure,
       "powerSupplyFailure": powerSupplyFailure,
       "batteryFailure": batteryFailure,
       "cacheFailure": cacheFailure,
       "upsFailure": upsFailure,
       "inboxFailure": inboxFailure,
       "backupCircuitFailure": backupCircuitFailure,
       "otherControllerFailure": otherControllerFailure,
       "warning": warning,
       "spareDriveFailure": spareDriveFailure,
       "microprogramReplacementExecuted": microprogramReplacementExecuted,
       "encFailure": encFailure,
       "loopFailure": loopFailure,
       "pathFailure": pathFailure,
       "drivePreMainte": drivePreMainte,
       "nasServerFailure": nasServerFailure,
       "nasPathFailure": nasPathFailure,
       "nasUpsFailure": nasUpsFailure,
       "systemExMib": systemExMib,
       "storageExMib": storageExMib,
       "dfraidExMib": dfraidExMib,
       "dfraidLanExMib": dfraidLanExMib,
       "dfSystemParameter": dfSystemParameter,
       "dfSystemProductName": dfSystemProductName,
       "dfSystemMicroRevision": dfSystemMicroRevision,
       "dfSystemSerialNumber": dfSystemSerialNumber,
       "dfWarningCondition": dfWarningCondition,
       "dfRegressionStatus": dfRegressionStatus,
       "dfPreventiveMaintenanceInformation": dfPreventiveMaintenanceInformation,
       "dfWarningReserve1": dfWarningReserve1,
       "dfWarningReserve2": dfWarningReserve2,
       "dfCommandExecutionCondition": dfCommandExecutionCondition,
       "dfCommandTable": dfCommandTable,
       "dfCommandEntry": dfCommandEntry,
       "dfLun": dfLun,
       "dfReadCommandNumber": dfReadCommandNumber,
       "dfReadHitNumber": dfReadHitNumber,
       "dfReadHitRate": dfReadHitRate,
       "dfWriteCommandNumber": dfWriteCommandNumber,
       "dfWriteHitNumber": dfWriteHitNumber,
       "dfWriteHitRate": dfWriteHitRate,
       "dfCacheLoadCondition": dfCacheLoadCondition,
       "dfWriteDataRate": dfWriteDataRate,
       "dfLUNS": dfLUNS,
       "dfLUNSSwitch": dfLUNSSwitch,
       "dfLUNSSwitchEntry": dfLUNSSwitchEntry,
       "dfSwitchSerialNumber": dfSwitchSerialNumber,
       "dfSwitchPortID": dfSwitchPortID,
       "dfSwitchOnOff": dfSwitchOnOff,
       "dfSwitchControlStatus": dfSwitchControlStatus,
       "dfLUNSWWN": dfLUNSWWN,
       "dfLUNSWWNEntry": dfLUNSWWNEntry,
       "dfWWNSerialNumber": dfWWNSerialNumber,
       "dfWWNPortID": dfWWNPortID,
       "dfWWNControlIndex": dfWWNControlIndex,
       "dfWWNWWN": dfWWNWWN,
       "dfWWNID": dfWWNID,
       "dfWWNNickname": dfWWNNickname,
       "dfWWNUseNickname": dfWWNUseNickname,
       "dfWWNControlStatus": dfWWNControlStatus,
       "dfLUNSWWNGroup": dfLUNSWWNGroup,
       "dfLUNSWWNGroupEntry": dfLUNSWWNGroupEntry,
       "dfWWNGroupSerialNumber": dfWWNGroupSerialNumber,
       "dfWWNGroupPortID": dfWWNGroupPortID,
       "dfWWNGroupControlIndex": dfWWNGroupControlIndex,
       "dfWWNGroupID": dfWWNGroupID,
       "dfWWNGroupNickname": dfWWNGroupNickname,
       "dfWWNGroupedWWNs": dfWWNGroupedWWNs,
       "dfWWNGroupControlStatus": dfWWNGroupControlStatus,
       "dfLUNSLUN": dfLUNSLUN,
       "dfLUNSLUNEntry": dfLUNSLUNEntry,
       "dfLUNSerialNumber": dfLUNSerialNumber,
       "dfLUNPortID": dfLUNPortID,
       "dfLUNLUN": dfLUNLUN,
       "dfLUNWWNSecurity": dfLUNWWNSecurity,
       "dfLUNWWNGroupSecurity": dfLUNWWNGroupSecurity,
       "dfLUNControlStatus": dfLUNControlStatus,
       "dfLUNSLUNGroup": dfLUNSLUNGroup,
       "dfLUNSLUNGroupEntry": dfLUNSLUNGroupEntry,
       "dfLUNGroupSerialNumber": dfLUNGroupSerialNumber,
       "dfLUNGroupPortID": dfLUNGroupPortID,
       "dfLUNGroupControlIndex": dfLUNGroupControlIndex,
       "dfLUNGroupID": dfLUNGroupID,
       "dfLUNGroupNickname": dfLUNGroupNickname,
       "dfLUNGroupedLUNs": dfLUNGroupedLUNs,
       "dfLUNGroupWWNSecurity": dfLUNGroupWWNSecurity,
       "dfLUNGroupWWNGroupSecurity": dfLUNGroupWWNGroupSecurity,
       "dfLUNGroupControlStatus": dfLUNGroupControlStatus,
       "dfPort": dfPort,
       "dfPortinf": dfPortinf,
       "dfPortinfEntry": dfPortinfEntry,
       "dfPortSerialNumber": dfPortSerialNumber,
       "dfPortID": dfPortID,
       "dfPortKind": dfPortKind,
       "dfPortHostMode": dfPortHostMode,
       "dfPortFibreAddress": dfPortFibreAddress,
       "dfPortFibreTopology": dfPortFibreTopology,
       "dfPortControlStatus": dfPortControlStatus,
       "dfPortDisplayName": dfPortDisplayName,
       "dfPortWWN": dfPortWWN,
       "dfCommandExecutionInternalCondition": dfCommandExecutionInternalCondition,
       "dfCommandInternalTable": dfCommandInternalTable,
       "dfCommandInternalEntry": dfCommandInternalEntry,
       "dfInternalLun": dfInternalLun,
       "dfInternalReadCommandNumber": dfInternalReadCommandNumber,
       "dfInternalReadHitNumber": dfInternalReadHitNumber,
       "dfInternalReadHitRate": dfInternalReadHitRate,
       "dfInternalWriteCommandNumber": dfInternalWriteCommandNumber,
       "dfInternalWriteHitNumber": dfInternalWriteHitNumber,
       "dfInternalWriteHitRate": dfInternalWriteHitRate}
)
