# SNMP MIB module (CISCO-ENHANCED-WRED-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ENHANCED-WRED-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:27 2024
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

(PhysicalIndex,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoEnhancedWredMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 222)
)
ciscoEnhancedWredMIB.setRevisions(
        ("2001-12-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CewredQueueNumber(Unsigned32, TextualConvention):
    status = "current"


class CewredRedMechanism(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dscp", 2),
          ("precedence", 1))
    )



class CewredRedProfile(Unsigned32, TextualConvention):
    status = "current"


class CewredIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs

_CewredMIBNotifications_ObjectIdentity = ObjectIdentity
cewredMIBNotifications = _CewredMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 0)
)
_CiscoEnhancedWredMIBObjects_ObjectIdentity = ObjectIdentity
ciscoEnhancedWredMIBObjects = _CiscoEnhancedWredMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1)
)
_CewredTx_ObjectIdentity = ObjectIdentity
cewredTx = _CewredTx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 1)
)
_CewredTxTable_Object = MibTable
cewredTxTable = _CewredTxTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cewredTxTable.setStatus("current")
_CewredTxEntry_Object = MibTableRow
cewredTxEntry = _CewredTxEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 1, 1, 1)
)
cewredTxEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cewredTxEntry.setStatus("current")
_CewredTxValue_Type = CewredIndex
_CewredTxValue_Object = MibTableColumn
cewredTxValue = _CewredTxValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 1, 1, 1, 1),
    _CewredTxValue_Type()
)
cewredTxValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewredTxValue.setStatus("current")
_CewredTxRowStatus_Type = RowStatus
_CewredTxRowStatus_Object = MibTableColumn
cewredTxRowStatus = _CewredTxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 1, 1, 1, 2),
    _CewredTxRowStatus_Type()
)
cewredTxRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewredTxRowStatus.setStatus("current")
_CewredRx_ObjectIdentity = ObjectIdentity
cewredRx = _CewredRx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 2)
)
_CewredRxIfTable_Object = MibTable
cewredRxIfTable = _CewredRxIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cewredRxIfTable.setStatus("current")
_CewredRxIfEntry_Object = MibTableRow
cewredRxIfEntry = _CewredRxIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 2, 1, 1)
)
cewredRxIfEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cewredRxIfEntry.setStatus("current")
_CewredRxIfValue_Type = CewredIndex
_CewredRxIfValue_Object = MibTableColumn
cewredRxIfValue = _CewredRxIfValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 2, 1, 1, 1),
    _CewredRxIfValue_Type()
)
cewredRxIfValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewredRxIfValue.setStatus("current")
_CewredRxIfRowStatus_Type = RowStatus
_CewredRxIfRowStatus_Object = MibTableColumn
cewredRxIfRowStatus = _CewredRxIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 2, 1, 1, 2),
    _CewredRxIfRowStatus_Type()
)
cewredRxIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewredRxIfRowStatus.setStatus("current")
_CewredRxTable_Object = MibTable
cewredRxTable = _CewredRxTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cewredRxTable.setStatus("current")
_CewredRxEntry_Object = MibTableRow
cewredRxEntry = _CewredRxEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 2, 2, 1)
)
cewredRxEntry.setIndexNames(
    (0, "CISCO-ENHANCED-WRED-MIB", "cewredRxSourceId"),
    (0, "CISCO-ENHANCED-WRED-MIB", "cewredRxDestId"),
)
if mibBuilder.loadTexts:
    cewredRxEntry.setStatus("current")
_CewredRxSourceId_Type = PhysicalIndex
_CewredRxSourceId_Object = MibTableColumn
cewredRxSourceId = _CewredRxSourceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 2, 2, 1, 1),
    _CewredRxSourceId_Type()
)
cewredRxSourceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cewredRxSourceId.setStatus("current")
_CewredRxDestId_Type = PhysicalIndex
_CewredRxDestId_Object = MibTableColumn
cewredRxDestId = _CewredRxDestId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 2, 2, 1, 2),
    _CewredRxDestId_Type()
)
cewredRxDestId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cewredRxDestId.setStatus("current")
_CewredRxValue_Type = CewredIndex
_CewredRxValue_Object = MibTableColumn
cewredRxValue = _CewredRxValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 2, 2, 1, 3),
    _CewredRxValue_Type()
)
cewredRxValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewredRxValue.setStatus("current")
_CewredRxRowStatus_Type = RowStatus
_CewredRxRowStatus_Object = MibTableColumn
cewredRxRowStatus = _CewredRxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 2, 2, 1, 4),
    _CewredRxRowStatus_Type()
)
cewredRxRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewredRxRowStatus.setStatus("current")
_CewredRxMulticastTable_Object = MibTable
cewredRxMulticastTable = _CewredRxMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cewredRxMulticastTable.setStatus("current")
_CewredRxMulticastEntry_Object = MibTableRow
cewredRxMulticastEntry = _CewredRxMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 2, 3, 1)
)
cewredRxMulticastEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cewredRxMulticastEntry.setStatus("current")
_CewredRxMulticastValue_Type = CewredIndex
_CewredRxMulticastValue_Object = MibTableColumn
cewredRxMulticastValue = _CewredRxMulticastValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 2, 3, 1, 1),
    _CewredRxMulticastValue_Type()
)
cewredRxMulticastValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewredRxMulticastValue.setStatus("current")
_CewredRxMulticastRowStatus_Type = RowStatus
_CewredRxMulticastRowStatus_Object = MibTableColumn
cewredRxMulticastRowStatus = _CewredRxMulticastRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 2, 3, 1, 2),
    _CewredRxMulticastRowStatus_Type()
)
cewredRxMulticastRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewredRxMulticastRowStatus.setStatus("current")
_CewredConfig_ObjectIdentity = ObjectIdentity
cewredConfig = _CewredConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 3)
)
_CewredConfigGlobTable_Object = MibTable
cewredConfigGlobTable = _CewredConfigGlobTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cewredConfigGlobTable.setStatus("current")
_CewredConfigGlobEntry_Object = MibTableRow
cewredConfigGlobEntry = _CewredConfigGlobEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 3, 1, 1)
)
cewredConfigGlobEntry.setIndexNames(
    (0, "CISCO-ENHANCED-WRED-MIB", "cewredConfigGlobIndex"),
)
if mibBuilder.loadTexts:
    cewredConfigGlobEntry.setStatus("current")
_CewredConfigGlobIndex_Type = CewredIndex
_CewredConfigGlobIndex_Object = MibTableColumn
cewredConfigGlobIndex = _CewredConfigGlobIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 3, 1, 1, 1),
    _CewredConfigGlobIndex_Type()
)
cewredConfigGlobIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cewredConfigGlobIndex.setStatus("current")
_CewredConfigGlobCosGroupName_Type = SnmpAdminString
_CewredConfigGlobCosGroupName_Object = MibTableColumn
cewredConfigGlobCosGroupName = _CewredConfigGlobCosGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 3, 1, 1, 2),
    _CewredConfigGlobCosGroupName_Type()
)
cewredConfigGlobCosGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewredConfigGlobCosGroupName.setStatus("current")
_CewredConfigGlobQueueWeight_Type = Unsigned32
_CewredConfigGlobQueueWeight_Object = MibTableColumn
cewredConfigGlobQueueWeight = _CewredConfigGlobQueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 3, 1, 1, 3),
    _CewredConfigGlobQueueWeight_Type()
)
cewredConfigGlobQueueWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewredConfigGlobQueueWeight.setStatus("current")
_CewredConfigGlobDscpPrec_Type = CewredRedMechanism
_CewredConfigGlobDscpPrec_Object = MibTableColumn
cewredConfigGlobDscpPrec = _CewredConfigGlobDscpPrec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 3, 1, 1, 4),
    _CewredConfigGlobDscpPrec_Type()
)
cewredConfigGlobDscpPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewredConfigGlobDscpPrec.setStatus("current")
_CewredConfigGlobRowStatus_Type = RowStatus
_CewredConfigGlobRowStatus_Object = MibTableColumn
cewredConfigGlobRowStatus = _CewredConfigGlobRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 3, 1, 1, 5),
    _CewredConfigGlobRowStatus_Type()
)
cewredConfigGlobRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewredConfigGlobRowStatus.setStatus("current")
_CewredConfigRedTable_Object = MibTable
cewredConfigRedTable = _CewredConfigRedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cewredConfigRedTable.setStatus("current")
_CewredConfigRedEntry_Object = MibTableRow
cewredConfigRedEntry = _CewredConfigRedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 3, 2, 1)
)
cewredConfigRedEntry.setIndexNames(
    (0, "CISCO-ENHANCED-WRED-MIB", "cewredConfigGlobIndex"),
    (0, "CISCO-ENHANCED-WRED-MIB", "cewredConfigRedValue"),
)
if mibBuilder.loadTexts:
    cewredConfigRedEntry.setStatus("current")
_CewredConfigRedValue_Type = Unsigned32
_CewredConfigRedValue_Object = MibTableColumn
cewredConfigRedValue = _CewredConfigRedValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 3, 2, 1, 1),
    _CewredConfigRedValue_Type()
)
cewredConfigRedValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cewredConfigRedValue.setStatus("current")
_CewredConfigRedQueueNumber_Type = CewredQueueNumber
_CewredConfigRedQueueNumber_Object = MibTableColumn
cewredConfigRedQueueNumber = _CewredConfigRedQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 3, 2, 1, 2),
    _CewredConfigRedQueueNumber_Type()
)
cewredConfigRedQueueNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewredConfigRedQueueNumber.setStatus("current")
_CewredConfigRedProfile_Type = CewredRedProfile
_CewredConfigRedProfile_Object = MibTableColumn
cewredConfigRedProfile = _CewredConfigRedProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 3, 2, 1, 3),
    _CewredConfigRedProfile_Type()
)
cewredConfigRedProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewredConfigRedProfile.setStatus("current")
_CewredConfigRedMinThreshold_Type = Unsigned32
_CewredConfigRedMinThreshold_Object = MibTableColumn
cewredConfigRedMinThreshold = _CewredConfigRedMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 3, 2, 1, 4),
    _CewredConfigRedMinThreshold_Type()
)
cewredConfigRedMinThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewredConfigRedMinThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cewredConfigRedMinThreshold.setUnits("packets")
_CewredConfigRedMaxThreshold_Type = Unsigned32
_CewredConfigRedMaxThreshold_Object = MibTableColumn
cewredConfigRedMaxThreshold = _CewredConfigRedMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 3, 2, 1, 5),
    _CewredConfigRedMaxThreshold_Type()
)
cewredConfigRedMaxThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewredConfigRedMaxThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cewredConfigRedMaxThreshold.setUnits("packets")
_CewredConfigRedPktsDropFract_Type = Unsigned32
_CewredConfigRedPktsDropFract_Object = MibTableColumn
cewredConfigRedPktsDropFract = _CewredConfigRedPktsDropFract_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 3, 2, 1, 6),
    _CewredConfigRedPktsDropFract_Type()
)
cewredConfigRedPktsDropFract.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewredConfigRedPktsDropFract.setStatus("current")
_CewredConfigRedRowStatus_Type = RowStatus
_CewredConfigRedRowStatus_Object = MibTableColumn
cewredConfigRedRowStatus = _CewredConfigRedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 3, 2, 1, 7),
    _CewredConfigRedRowStatus_Type()
)
cewredConfigRedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cewredConfigRedRowStatus.setStatus("current")
_CewredQueue_ObjectIdentity = ObjectIdentity
cewredQueue = _CewredQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 4)
)
_CewredQueueParamTable_Object = MibTable
cewredQueueParamTable = _CewredQueueParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cewredQueueParamTable.setStatus("current")
_CewredQueueParamEntry_Object = MibTableRow
cewredQueueParamEntry = _CewredQueueParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 4, 1, 1)
)
cewredQueueParamEntry.setIndexNames(
    (0, "CISCO-ENHANCED-WRED-MIB", "cewredConfigGlobIndex"),
    (0, "CISCO-ENHANCED-WRED-MIB", "cewredQueueParamNumber"),
)
if mibBuilder.loadTexts:
    cewredQueueParamEntry.setStatus("current")
_CewredQueueParamNumber_Type = CewredQueueNumber
_CewredQueueParamNumber_Object = MibTableColumn
cewredQueueParamNumber = _CewredQueueParamNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 4, 1, 1, 1),
    _CewredQueueParamNumber_Type()
)
cewredQueueParamNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cewredQueueParamNumber.setStatus("current")
_CewredQueueParamWeight_Type = Unsigned32
_CewredQueueParamWeight_Object = MibTableColumn
cewredQueueParamWeight = _CewredQueueParamWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 4, 1, 1, 2),
    _CewredQueueParamWeight_Type()
)
cewredQueueParamWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cewredQueueParamWeight.setStatus("current")
_CewredQueueParamAverage_Type = Gauge32
_CewredQueueParamAverage_Object = MibTableColumn
cewredQueueParamAverage = _CewredQueueParamAverage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 4, 1, 1, 3),
    _CewredQueueParamAverage_Type()
)
cewredQueueParamAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewredQueueParamAverage.setStatus("current")
if mibBuilder.loadTexts:
    cewredQueueParamAverage.setUnits("packets")
_CewredQueueParamMaxAverage_Type = Gauge32
_CewredQueueParamMaxAverage_Object = MibTableColumn
cewredQueueParamMaxAverage = _CewredQueueParamMaxAverage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 4, 1, 1, 4),
    _CewredQueueParamMaxAverage_Type()
)
cewredQueueParamMaxAverage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cewredQueueParamMaxAverage.setStatus("current")
if mibBuilder.loadTexts:
    cewredQueueParamMaxAverage.setUnits("packets")
_CewredQueueParamDepth_Type = Gauge32
_CewredQueueParamDepth_Object = MibTableColumn
cewredQueueParamDepth = _CewredQueueParamDepth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 4, 1, 1, 5),
    _CewredQueueParamDepth_Type()
)
cewredQueueParamDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewredQueueParamDepth.setStatus("current")
if mibBuilder.loadTexts:
    cewredQueueParamDepth.setUnits("packets")
_CewredQueueParamMaxDepth_Type = Gauge32
_CewredQueueParamMaxDepth_Object = MibTableColumn
cewredQueueParamMaxDepth = _CewredQueueParamMaxDepth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 4, 1, 1, 6),
    _CewredQueueParamMaxDepth_Type()
)
cewredQueueParamMaxDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cewredQueueParamMaxDepth.setStatus("current")
if mibBuilder.loadTexts:
    cewredQueueParamMaxDepth.setUnits("packets")
_CewredStat_ObjectIdentity = ObjectIdentity
cewredStat = _CewredStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 5)
)
_CewredStatTable_Object = MibTable
cewredStatTable = _CewredStatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cewredStatTable.setStatus("current")
_CewredStatEntry_Object = MibTableRow
cewredStatEntry = _CewredStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 5, 1, 1)
)
cewredStatEntry.setIndexNames(
    (0, "CISCO-ENHANCED-WRED-MIB", "cewredConfigGlobIndex"),
    (0, "CISCO-ENHANCED-WRED-MIB", "cewredStatRedProfile"),
)
if mibBuilder.loadTexts:
    cewredStatEntry.setStatus("current")
_CewredStatRedProfile_Type = CewredRedProfile
_CewredStatRedProfile_Object = MibTableColumn
cewredStatRedProfile = _CewredStatRedProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 5, 1, 1, 1),
    _CewredStatRedProfile_Type()
)
cewredStatRedProfile.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cewredStatRedProfile.setStatus("current")
_CewredStatSwitchedPkts_Type = Counter32
_CewredStatSwitchedPkts_Object = MibTableColumn
cewredStatSwitchedPkts = _CewredStatSwitchedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 5, 1, 1, 2),
    _CewredStatSwitchedPkts_Type()
)
cewredStatSwitchedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewredStatSwitchedPkts.setStatus("current")
if mibBuilder.loadTexts:
    cewredStatSwitchedPkts.setUnits("packets")
_CewredStatRandomFilteredPkts_Type = Counter32
_CewredStatRandomFilteredPkts_Object = MibTableColumn
cewredStatRandomFilteredPkts = _CewredStatRandomFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 5, 1, 1, 3),
    _CewredStatRandomFilteredPkts_Type()
)
cewredStatRandomFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewredStatRandomFilteredPkts.setStatus("current")
if mibBuilder.loadTexts:
    cewredStatRandomFilteredPkts.setUnits("packets")
_CewredStatMaxFilteredPkts_Type = Counter32
_CewredStatMaxFilteredPkts_Object = MibTableColumn
cewredStatMaxFilteredPkts = _CewredStatMaxFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 5, 1, 1, 4),
    _CewredStatMaxFilteredPkts_Type()
)
cewredStatMaxFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewredStatMaxFilteredPkts.setStatus("current")
if mibBuilder.loadTexts:
    cewredStatMaxFilteredPkts.setUnits("packets")
_CewredStatSwitchedPkts64_Type = Counter64
_CewredStatSwitchedPkts64_Object = MibTableColumn
cewredStatSwitchedPkts64 = _CewredStatSwitchedPkts64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 5, 1, 1, 5),
    _CewredStatSwitchedPkts64_Type()
)
cewredStatSwitchedPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewredStatSwitchedPkts64.setStatus("current")
if mibBuilder.loadTexts:
    cewredStatSwitchedPkts64.setUnits("packets")
_CewredStatRandomFilteredPkts64_Type = Counter64
_CewredStatRandomFilteredPkts64_Object = MibTableColumn
cewredStatRandomFilteredPkts64 = _CewredStatRandomFilteredPkts64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 5, 1, 1, 6),
    _CewredStatRandomFilteredPkts64_Type()
)
cewredStatRandomFilteredPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewredStatRandomFilteredPkts64.setStatus("current")
if mibBuilder.loadTexts:
    cewredStatRandomFilteredPkts64.setUnits("packets")
_CewredStatMaxFilteredPkts64_Type = Counter64
_CewredStatMaxFilteredPkts64_Object = MibTableColumn
cewredStatMaxFilteredPkts64 = _CewredStatMaxFilteredPkts64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 1, 5, 1, 1, 7),
    _CewredStatMaxFilteredPkts64_Type()
)
cewredStatMaxFilteredPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cewredStatMaxFilteredPkts64.setStatus("current")
if mibBuilder.loadTexts:
    cewredStatMaxFilteredPkts64.setUnits("packets")
_CewredMIBConformance_ObjectIdentity = ObjectIdentity
cewredMIBConformance = _CewredMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 3)
)
_CewredMIBCompliances_ObjectIdentity = ObjectIdentity
cewredMIBCompliances = _CewredMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 3, 1)
)
_CewredMIBGroups_ObjectIdentity = ObjectIdentity
cewredMIBGroups = _CewredMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 3, 2)
)

# Managed Objects groups

ciscoEnhancedWredGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 3, 2, 1)
)
ciscoEnhancedWredGroup.setObjects(
      *(("CISCO-ENHANCED-WRED-MIB", "cewredConfigGlobQueueWeight"),
        ("CISCO-ENHANCED-WRED-MIB", "cewredConfigGlobDscpPrec"),
        ("CISCO-ENHANCED-WRED-MIB", "cewredConfigGlobRowStatus"),
        ("CISCO-ENHANCED-WRED-MIB", "cewredConfigRedMinThreshold"),
        ("CISCO-ENHANCED-WRED-MIB", "cewredConfigRedMaxThreshold"),
        ("CISCO-ENHANCED-WRED-MIB", "cewredConfigRedPktsDropFract"),
        ("CISCO-ENHANCED-WRED-MIB", "cewredConfigRedRowStatus"),
        ("CISCO-ENHANCED-WRED-MIB", "cewredQueueParamAverage"),
        ("CISCO-ENHANCED-WRED-MIB", "cewredStatRandomFilteredPkts"),
        ("CISCO-ENHANCED-WRED-MIB", "cewredStatMaxFilteredPkts"),
        ("CISCO-ENHANCED-WRED-MIB", "cewredStatRandomFilteredPkts64"),
        ("CISCO-ENHANCED-WRED-MIB", "cewredStatMaxFilteredPkts64"))
)
if mibBuilder.loadTexts:
    ciscoEnhancedWredGroup.setStatus("current")

ciscoEnhancedWredDrrQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 3, 2, 2)
)
ciscoEnhancedWredDrrQueueGroup.setObjects(
      *(("CISCO-ENHANCED-WRED-MIB", "cewredConfigRedQueueNumber"),
        ("CISCO-ENHANCED-WRED-MIB", "cewredQueueParamWeight"),
        ("CISCO-ENHANCED-WRED-MIB", "cewredQueueParamMaxAverage"),
        ("CISCO-ENHANCED-WRED-MIB", "cewredQueueParamDepth"),
        ("CISCO-ENHANCED-WRED-MIB", "cewredQueueParamMaxDepth"))
)
if mibBuilder.loadTexts:
    ciscoEnhancedWredDrrQueueGroup.setStatus("current")

ciscoEnhancedWredStatCountGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 3, 2, 3)
)
ciscoEnhancedWredStatCountGroup.setObjects(
      *(("CISCO-ENHANCED-WRED-MIB", "cewredStatSwitchedPkts"),
        ("CISCO-ENHANCED-WRED-MIB", "cewredStatSwitchedPkts64"))
)
if mibBuilder.loadTexts:
    ciscoEnhancedWredStatCountGroup.setStatus("current")

ciscoEnhancedWredCosQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 3, 2, 4)
)
ciscoEnhancedWredCosQueueGroup.setObjects(
      *(("CISCO-ENHANCED-WRED-MIB", "cewredConfigGlobCosGroupName"),
        ("CISCO-ENHANCED-WRED-MIB", "cewredConfigRedProfile"))
)
if mibBuilder.loadTexts:
    ciscoEnhancedWredCosQueueGroup.setStatus("current")

ciscoEnhancedWredTxInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 3, 2, 5)
)
ciscoEnhancedWredTxInfoGroup.setObjects(
      *(("CISCO-ENHANCED-WRED-MIB", "cewredTxValue"),
        ("CISCO-ENHANCED-WRED-MIB", "cewredTxRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoEnhancedWredTxInfoGroup.setStatus("current")

ciscoEnhancedWredRxIfInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 3, 2, 6)
)
ciscoEnhancedWredRxIfInfoGroup.setObjects(
      *(("CISCO-ENHANCED-WRED-MIB", "cewredRxIfValue"),
        ("CISCO-ENHANCED-WRED-MIB", "cewredRxIfRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoEnhancedWredRxIfInfoGroup.setStatus("current")

ciscoEnhancedWredRxInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 3, 2, 7)
)
ciscoEnhancedWredRxInfoGroup.setObjects(
      *(("CISCO-ENHANCED-WRED-MIB", "cewredRxValue"),
        ("CISCO-ENHANCED-WRED-MIB", "cewredRxRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoEnhancedWredRxInfoGroup.setStatus("current")

ciscoEnhancedWredRxMcInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 3, 2, 8)
)
ciscoEnhancedWredRxMcInfoGroup.setObjects(
      *(("CISCO-ENHANCED-WRED-MIB", "cewredRxMulticastValue"),
        ("CISCO-ENHANCED-WRED-MIB", "cewredRxMulticastRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoEnhancedWredRxMcInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cewredMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 222, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cewredMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENHANCED-WRED-MIB",
    **{"CewredQueueNumber": CewredQueueNumber,
       "CewredRedMechanism": CewredRedMechanism,
       "CewredRedProfile": CewredRedProfile,
       "CewredIndex": CewredIndex,
       "ciscoEnhancedWredMIB": ciscoEnhancedWredMIB,
       "cewredMIBNotifications": cewredMIBNotifications,
       "ciscoEnhancedWredMIBObjects": ciscoEnhancedWredMIBObjects,
       "cewredTx": cewredTx,
       "cewredTxTable": cewredTxTable,
       "cewredTxEntry": cewredTxEntry,
       "cewredTxValue": cewredTxValue,
       "cewredTxRowStatus": cewredTxRowStatus,
       "cewredRx": cewredRx,
       "cewredRxIfTable": cewredRxIfTable,
       "cewredRxIfEntry": cewredRxIfEntry,
       "cewredRxIfValue": cewredRxIfValue,
       "cewredRxIfRowStatus": cewredRxIfRowStatus,
       "cewredRxTable": cewredRxTable,
       "cewredRxEntry": cewredRxEntry,
       "cewredRxSourceId": cewredRxSourceId,
       "cewredRxDestId": cewredRxDestId,
       "cewredRxValue": cewredRxValue,
       "cewredRxRowStatus": cewredRxRowStatus,
       "cewredRxMulticastTable": cewredRxMulticastTable,
       "cewredRxMulticastEntry": cewredRxMulticastEntry,
       "cewredRxMulticastValue": cewredRxMulticastValue,
       "cewredRxMulticastRowStatus": cewredRxMulticastRowStatus,
       "cewredConfig": cewredConfig,
       "cewredConfigGlobTable": cewredConfigGlobTable,
       "cewredConfigGlobEntry": cewredConfigGlobEntry,
       "cewredConfigGlobIndex": cewredConfigGlobIndex,
       "cewredConfigGlobCosGroupName": cewredConfigGlobCosGroupName,
       "cewredConfigGlobQueueWeight": cewredConfigGlobQueueWeight,
       "cewredConfigGlobDscpPrec": cewredConfigGlobDscpPrec,
       "cewredConfigGlobRowStatus": cewredConfigGlobRowStatus,
       "cewredConfigRedTable": cewredConfigRedTable,
       "cewredConfigRedEntry": cewredConfigRedEntry,
       "cewredConfigRedValue": cewredConfigRedValue,
       "cewredConfigRedQueueNumber": cewredConfigRedQueueNumber,
       "cewredConfigRedProfile": cewredConfigRedProfile,
       "cewredConfigRedMinThreshold": cewredConfigRedMinThreshold,
       "cewredConfigRedMaxThreshold": cewredConfigRedMaxThreshold,
       "cewredConfigRedPktsDropFract": cewredConfigRedPktsDropFract,
       "cewredConfigRedRowStatus": cewredConfigRedRowStatus,
       "cewredQueue": cewredQueue,
       "cewredQueueParamTable": cewredQueueParamTable,
       "cewredQueueParamEntry": cewredQueueParamEntry,
       "cewredQueueParamNumber": cewredQueueParamNumber,
       "cewredQueueParamWeight": cewredQueueParamWeight,
       "cewredQueueParamAverage": cewredQueueParamAverage,
       "cewredQueueParamMaxAverage": cewredQueueParamMaxAverage,
       "cewredQueueParamDepth": cewredQueueParamDepth,
       "cewredQueueParamMaxDepth": cewredQueueParamMaxDepth,
       "cewredStat": cewredStat,
       "cewredStatTable": cewredStatTable,
       "cewredStatEntry": cewredStatEntry,
       "cewredStatRedProfile": cewredStatRedProfile,
       "cewredStatSwitchedPkts": cewredStatSwitchedPkts,
       "cewredStatRandomFilteredPkts": cewredStatRandomFilteredPkts,
       "cewredStatMaxFilteredPkts": cewredStatMaxFilteredPkts,
       "cewredStatSwitchedPkts64": cewredStatSwitchedPkts64,
       "cewredStatRandomFilteredPkts64": cewredStatRandomFilteredPkts64,
       "cewredStatMaxFilteredPkts64": cewredStatMaxFilteredPkts64,
       "cewredMIBConformance": cewredMIBConformance,
       "cewredMIBCompliances": cewredMIBCompliances,
       "cewredMIBCompliance": cewredMIBCompliance,
       "cewredMIBGroups": cewredMIBGroups,
       "ciscoEnhancedWredGroup": ciscoEnhancedWredGroup,
       "ciscoEnhancedWredDrrQueueGroup": ciscoEnhancedWredDrrQueueGroup,
       "ciscoEnhancedWredStatCountGroup": ciscoEnhancedWredStatCountGroup,
       "ciscoEnhancedWredCosQueueGroup": ciscoEnhancedWredCosQueueGroup,
       "ciscoEnhancedWredTxInfoGroup": ciscoEnhancedWredTxInfoGroup,
       "ciscoEnhancedWredRxIfInfoGroup": ciscoEnhancedWredRxIfInfoGroup,
       "ciscoEnhancedWredRxInfoGroup": ciscoEnhancedWredRxInfoGroup,
       "ciscoEnhancedWredRxMcInfoGroup": ciscoEnhancedWredRxMcInfoGroup}
)
