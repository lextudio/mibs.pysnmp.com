# SNMP MIB module (ATM-FORUM-M4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATM-FORUM-M4-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:52 2024
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

(atmForum,) = mibBuilder.importSymbols(
    "ATM-FORUM-TC-MIB",
    "atmForum")

(atmVcCrossConnectEntry,
 atmVcCrossConnectHighIfIndex,
 atmVcCrossConnectHighVci,
 atmVcCrossConnectHighVpi,
 atmVcCrossConnectIndex,
 atmVcCrossConnectLowIfIndex,
 atmVcCrossConnectLowVci,
 atmVcCrossConnectLowVpi,
 atmVclEntry,
 atmVclVci,
 atmVclVpi,
 atmVpCrossConnectEntry,
 atmVpCrossConnectHighIfIndex,
 atmVpCrossConnectHighVpi,
 atmVpCrossConnectIndex,
 atmVpCrossConnectLowIfIndex,
 atmVpCrossConnectLowVpi,
 atmVplEntry,
 atmVplVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmVcCrossConnectEntry",
    "atmVcCrossConnectHighIfIndex",
    "atmVcCrossConnectHighVci",
    "atmVcCrossConnectHighVpi",
    "atmVcCrossConnectIndex",
    "atmVcCrossConnectLowIfIndex",
    "atmVcCrossConnectLowVci",
    "atmVcCrossConnectLowVpi",
    "atmVclEntry",
    "atmVclVci",
    "atmVclVpi",
    "atmVpCrossConnectEntry",
    "atmVpCrossConnectHighIfIndex",
    "atmVpCrossConnectHighVpi",
    "atmVpCrossConnectIndex",
    "atmVpCrossConnectLowIfIndex",
    "atmVpCrossConnectLowVpi",
    "atmVplEntry",
    "atmVplVpi")

(entPhysicalClass,
 entPhysicalContainedIn,
 entPhysicalIndex,
 entPhysicalParentRelPos) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalClass",
    "entPhysicalContainedIn",
    "entPhysicalIndex",
    "entPhysicalParentRelPos")

(hrSWInstalledIndex,
 hrSWInstalledName) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "hrSWInstalledIndex",
    "hrSWInstalledName")

(OwnerString,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "OwnerString",
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

(AutonomousType,
 DateAndTime,
 DisplayString,
 RowPointer,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

atmfM4MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 353, 100)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AtmfM4AlarmLogSeverity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cleared", -1),
          ("critical", 1),
          ("indeterminate", 0),
          ("major", 2),
          ("minor", 3),
          ("warning", 4))
    )



class AtmfM4AlarmSeverity(Integer32, TextualConvention):
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
        *(("critical", 1),
          ("indeterminate", 0),
          ("major", 2),
          ("minor", 3),
          ("warning", 4))
    )



# MIB Managed Objects in the order of their OIDs

_AtmfM4MIBObjects_ObjectIdentity = ObjectIdentity
atmfM4MIBObjects = _AtmfM4MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 100, 1)
)
_AtmfM4NeVendor_Type = DisplayString
_AtmfM4NeVendor_Object = MibScalar
atmfM4NeVendor = _AtmfM4NeVendor_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 1),
    _AtmfM4NeVendor_Type()
)
atmfM4NeVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4NeVendor.setStatus("current")
_AtmfM4NeVersion_Type = AutonomousType
_AtmfM4NeVersion_Object = MibScalar
atmfM4NeVersion = _AtmfM4NeVersion_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 2),
    _AtmfM4NeVersion_Type()
)
atmfM4NeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4NeVersion.setStatus("current")
_AtmfM4NeStartTime_Type = DateAndTime
_AtmfM4NeStartTime_Object = MibScalar
atmfM4NeStartTime = _AtmfM4NeStartTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 3),
    _AtmfM4NeStartTime_Type()
)
atmfM4NeStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4NeStartTime.setStatus("current")


class _AtmfM4NeAlarmSeverityIndex_Type(Integer32):
    """Custom type atmfM4NeAlarmSeverityIndex based on Integer32"""
    defaultValue = 0


_AtmfM4NeAlarmSeverityIndex_Object = MibScalar
atmfM4NeAlarmSeverityIndex = _AtmfM4NeAlarmSeverityIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 4),
    _AtmfM4NeAlarmSeverityIndex_Type()
)
atmfM4NeAlarmSeverityIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfM4NeAlarmSeverityIndex.setStatus("current")


class _AtmfM4NeSuppressZeroStats_Type(TruthValue):
    """Custom type atmfM4NeSuppressZeroStats based on TruthValue"""


_AtmfM4NeSuppressZeroStats_Object = MibScalar
atmfM4NeSuppressZeroStats = _AtmfM4NeSuppressZeroStats_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 5),
    _AtmfM4NeSuppressZeroStats_Type()
)
atmfM4NeSuppressZeroStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfM4NeSuppressZeroStats.setStatus("current")
_AtmfM4PhysPathTpTable_Object = MibTable
atmfM4PhysPathTpTable = _AtmfM4PhysPathTpTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 6)
)
if mibBuilder.loadTexts:
    atmfM4PhysPathTpTable.setStatus("current")
_AtmfM4PhysPathTpEntry_Object = MibTableRow
atmfM4PhysPathTpEntry = _AtmfM4PhysPathTpEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 6, 1)
)
atmfM4PhysPathTpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmfM4PhysPathTpEntry.setStatus("current")


class _AtmfM4PhysPathTpHwUnitIndex_Type(Integer32):
    """Custom type atmfM4PhysPathTpHwUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AtmfM4PhysPathTpHwUnitIndex_Type.__name__ = "Integer32"
_AtmfM4PhysPathTpHwUnitIndex_Object = MibTableColumn
atmfM4PhysPathTpHwUnitIndex = _AtmfM4PhysPathTpHwUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 6, 1, 1),
    _AtmfM4PhysPathTpHwUnitIndex_Type()
)
atmfM4PhysPathTpHwUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4PhysPathTpHwUnitIndex.setStatus("current")


class _AtmfM4PhysPathTpPortID_Type(Integer32):
    """Custom type atmfM4PhysPathTpPortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AtmfM4PhysPathTpPortID_Type.__name__ = "Integer32"
_AtmfM4PhysPathTpPortID_Object = MibTableColumn
atmfM4PhysPathTpPortID = _AtmfM4PhysPathTpPortID_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 6, 1, 2),
    _AtmfM4PhysPathTpPortID_Type()
)
atmfM4PhysPathTpPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4PhysPathTpPortID.setStatus("current")


class _AtmfM4PhysPathTpAlarmSeverityIndex_Type(Integer32):
    """Custom type atmfM4PhysPathTpAlarmSeverityIndex based on Integer32"""
    defaultValue = 0


_AtmfM4PhysPathTpAlarmSeverityIndex_Object = MibTableColumn
atmfM4PhysPathTpAlarmSeverityIndex = _AtmfM4PhysPathTpAlarmSeverityIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 6, 1, 3),
    _AtmfM4PhysPathTpAlarmSeverityIndex_Type()
)
atmfM4PhysPathTpAlarmSeverityIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfM4PhysPathTpAlarmSeverityIndex.setStatus("current")
_AtmfM4TcAdaptorTable_Object = MibTable
atmfM4TcAdaptorTable = _AtmfM4TcAdaptorTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 7)
)
if mibBuilder.loadTexts:
    atmfM4TcAdaptorTable.setStatus("current")
_AtmfM4TcAdaptorEntry_Object = MibTableRow
atmfM4TcAdaptorEntry = _AtmfM4TcAdaptorEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 7, 1)
)
atmfM4TcAdaptorEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmfM4TcAdaptorEntry.setStatus("current")


class _AtmfM4TcACellScrambling_Type(TruthValue):
    """Custom type atmfM4TcACellScrambling based on TruthValue"""


_AtmfM4TcACellScrambling_Object = MibTableColumn
atmfM4TcACellScrambling = _AtmfM4TcACellScrambling_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 7, 1, 1),
    _AtmfM4TcACellScrambling_Type()
)
atmfM4TcACellScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfM4TcACellScrambling.setStatus("current")


class _AtmfM4TcAlarmSeverityIndex_Type(Integer32):
    """Custom type atmfM4TcAlarmSeverityIndex based on Integer32"""
    defaultValue = 0


_AtmfM4TcAlarmSeverityIndex_Object = MibTableColumn
atmfM4TcAlarmSeverityIndex = _AtmfM4TcAlarmSeverityIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 7, 1, 2),
    _AtmfM4TcAlarmSeverityIndex_Type()
)
atmfM4TcAlarmSeverityIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfM4TcAlarmSeverityIndex.setStatus("current")
_AtmfM4AtmLayerTable_Object = MibTable
atmfM4AtmLayerTable = _AtmfM4AtmLayerTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 8)
)
if mibBuilder.loadTexts:
    atmfM4AtmLayerTable.setStatus("current")
_AtmfM4AtmLayerEntry_Object = MibTableRow
atmfM4AtmLayerEntry = _AtmfM4AtmLayerEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 8, 1)
)
atmfM4AtmLayerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmfM4AtmLayerEntry.setStatus("current")


class _AtmfM4IfType_Type(Integer32):
    """Custom type atmfM4IfType based on Integer32"""
    defaultValue = 0

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
        *(("bici", 2),
          ("bissi", 3),
          ("none", 0),
          ("uni", 1))
    )


_AtmfM4IfType_Type.__name__ = "Integer32"
_AtmfM4IfType_Object = MibTableColumn
atmfM4IfType = _AtmfM4IfType_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 8, 1, 1),
    _AtmfM4IfType_Type()
)
atmfM4IfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfM4IfType.setStatus("current")


class _AtmfM4IfLoopbackLocationCode_Type(Integer32):
    """Custom type atmfM4IfLoopbackLocationCode based on Integer32"""
    defaultValue = 0


_AtmfM4IfLoopbackLocationCode_Object = MibTableColumn
atmfM4IfLoopbackLocationCode = _AtmfM4IfLoopbackLocationCode_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 8, 1, 2),
    _AtmfM4IfLoopbackLocationCode_Type()
)
atmfM4IfLoopbackLocationCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfM4IfLoopbackLocationCode.setStatus("current")
_AtmfM4IfSubscriberAddress_Type = DisplayString
_AtmfM4IfSubscriberAddress_Object = MibTableColumn
atmfM4IfSubscriberAddress = _AtmfM4IfSubscriberAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 8, 1, 3),
    _AtmfM4IfSubscriberAddress_Type()
)
atmfM4IfSubscriberAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfM4IfSubscriberAddress.setStatus("current")
_AtmfM4IfPreferredCarrier_Type = DisplayString
_AtmfM4IfPreferredCarrier_Object = MibTableColumn
atmfM4IfPreferredCarrier = _AtmfM4IfPreferredCarrier_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 8, 1, 4),
    _AtmfM4IfPreferredCarrier_Type()
)
atmfM4IfPreferredCarrier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfM4IfPreferredCarrier.setStatus("current")
_AtmfM4IfFarEndCarrierNetwork_Type = DisplayString
_AtmfM4IfFarEndCarrierNetwork_Object = MibTableColumn
atmfM4IfFarEndCarrierNetwork = _AtmfM4IfFarEndCarrierNetwork_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 8, 1, 5),
    _AtmfM4IfFarEndCarrierNetwork_Type()
)
atmfM4IfFarEndCarrierNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfM4IfFarEndCarrierNetwork.setStatus("current")
_AtmfM4VplTable_Object = MibTable
atmfM4VplTable = _AtmfM4VplTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 9)
)
if mibBuilder.loadTexts:
    atmfM4VplTable.setStatus("current")
_AtmfM4VplEntry_Object = MibTableRow
atmfM4VplEntry = _AtmfM4VplEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 9, 1)
)
if mibBuilder.loadTexts:
    atmfM4VplEntry.setStatus("current")
_AtmfM4VplSegEndPt_Type = TruthValue
_AtmfM4VplSegEndPt_Object = MibTableColumn
atmfM4VplSegEndPt = _AtmfM4VplSegEndPt_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 9, 1, 1),
    _AtmfM4VplSegEndPt_Type()
)
atmfM4VplSegEndPt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmfM4VplSegEndPt.setStatus("current")
_AtmfM4VclTable_Object = MibTable
atmfM4VclTable = _AtmfM4VclTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 10)
)
if mibBuilder.loadTexts:
    atmfM4VclTable.setStatus("current")
_AtmfM4VclEntry_Object = MibTableRow
atmfM4VclEntry = _AtmfM4VclEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 10, 1)
)
if mibBuilder.loadTexts:
    atmfM4VclEntry.setStatus("current")
_AtmfM4VclSegEndPt_Type = TruthValue
_AtmfM4VclSegEndPt_Object = MibTableColumn
atmfM4VclSegEndPt = _AtmfM4VclSegEndPt_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 10, 1, 1),
    _AtmfM4VclSegEndPt_Type()
)
atmfM4VclSegEndPt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmfM4VclSegEndPt.setStatus("current")
_AtmfM4VpXConnTable_Object = MibTable
atmfM4VpXConnTable = _AtmfM4VpXConnTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 11)
)
if mibBuilder.loadTexts:
    atmfM4VpXConnTable.setStatus("current")
_AtmfM4VpXConnEntry_Object = MibTableRow
atmfM4VpXConnEntry = _AtmfM4VpXConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 11, 1)
)
if mibBuilder.loadTexts:
    atmfM4VpXConnEntry.setStatus("current")
_AtmfM4VpXConnRecover_Type = TruthValue
_AtmfM4VpXConnRecover_Object = MibTableColumn
atmfM4VpXConnRecover = _AtmfM4VpXConnRecover_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 11, 1, 1),
    _AtmfM4VpXConnRecover_Type()
)
atmfM4VpXConnRecover.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmfM4VpXConnRecover.setStatus("current")
_AtmfM4VcXConnTable_Object = MibTable
atmfM4VcXConnTable = _AtmfM4VcXConnTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 12)
)
if mibBuilder.loadTexts:
    atmfM4VcXConnTable.setStatus("current")
_AtmfM4VcXConnEntry_Object = MibTableRow
atmfM4VcXConnEntry = _AtmfM4VcXConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 12, 1)
)
if mibBuilder.loadTexts:
    atmfM4VcXConnEntry.setStatus("current")
_AtmfM4VcXConnRecover_Type = TruthValue
_AtmfM4VcXConnRecover_Object = MibTableColumn
atmfM4VcXConnRecover = _AtmfM4VcXConnRecover_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 12, 1, 1),
    _AtmfM4VcXConnRecover_Type()
)
atmfM4VcXConnRecover.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmfM4VcXConnRecover.setStatus("current")
_AtmfM4VpNextVpiTable_Object = MibTable
atmfM4VpNextVpiTable = _AtmfM4VpNextVpiTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 13)
)
if mibBuilder.loadTexts:
    atmfM4VpNextVpiTable.setStatus("current")
_AtmfM4VpNextVpiEntry_Object = MibTableRow
atmfM4VpNextVpiEntry = _AtmfM4VpNextVpiEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 13, 1)
)
atmfM4VpNextVpiEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmfM4VpNextVpiEntry.setStatus("current")


class _AtmfM4VpNextVpiValue_Type(Integer32):
    """Custom type atmfM4VpNextVpiValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4095),
    )


_AtmfM4VpNextVpiValue_Type.__name__ = "Integer32"
_AtmfM4VpNextVpiValue_Object = MibTableColumn
atmfM4VpNextVpiValue = _AtmfM4VpNextVpiValue_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 13, 1, 1),
    _AtmfM4VpNextVpiValue_Type()
)
atmfM4VpNextVpiValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VpNextVpiValue.setStatus("current")
_AtmfM4VcNextVciTable_Object = MibTable
atmfM4VcNextVciTable = _AtmfM4VcNextVciTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 14)
)
if mibBuilder.loadTexts:
    atmfM4VcNextVciTable.setStatus("current")
_AtmfM4VcNextVciEntry_Object = MibTableRow
atmfM4VcNextVciEntry = _AtmfM4VcNextVciEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 14, 1)
)
atmfM4VcNextVciEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    atmfM4VcNextVciEntry.setStatus("current")


class _AtmfM4VcNextVciValue_Type(Integer32):
    """Custom type atmfM4VcNextVciValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_AtmfM4VcNextVciValue_Type.__name__ = "Integer32"
_AtmfM4VcNextVciValue_Object = MibTableColumn
atmfM4VcNextVciValue = _AtmfM4VcNextVciValue_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 14, 1, 1),
    _AtmfM4VcNextVciValue_Type()
)
atmfM4VcNextVciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VcNextVciValue.setStatus("current")
_AtmfM4CellProtoCurrTable_Object = MibTable
atmfM4CellProtoCurrTable = _AtmfM4CellProtoCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 15)
)
if mibBuilder.loadTexts:
    atmfM4CellProtoCurrTable.setStatus("current")
_AtmfM4CellProtoCurrEntry_Object = MibTableRow
atmfM4CellProtoCurrEntry = _AtmfM4CellProtoCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 15, 1)
)
atmfM4CellProtoCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmfM4CellProtoCurrEntry.setStatus("current")
_AtmfM4CellProtoCurrSuspect_Type = TruthValue
_AtmfM4CellProtoCurrSuspect_Object = MibTableColumn
atmfM4CellProtoCurrSuspect = _AtmfM4CellProtoCurrSuspect_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 15, 1, 1),
    _AtmfM4CellProtoCurrSuspect_Type()
)
atmfM4CellProtoCurrSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4CellProtoCurrSuspect.setStatus("current")
_AtmfM4CellProtoCurrElapsedTime_Type = TimeInterval
_AtmfM4CellProtoCurrElapsedTime_Object = MibTableColumn
atmfM4CellProtoCurrElapsedTime = _AtmfM4CellProtoCurrElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 15, 1, 2),
    _AtmfM4CellProtoCurrElapsedTime_Type()
)
atmfM4CellProtoCurrElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4CellProtoCurrElapsedTime.setStatus("current")
_AtmfM4CellProtoCurrSupprIntvls_Type = Counter32
_AtmfM4CellProtoCurrSupprIntvls_Object = MibTableColumn
atmfM4CellProtoCurrSupprIntvls = _AtmfM4CellProtoCurrSupprIntvls_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 15, 1, 3),
    _AtmfM4CellProtoCurrSupprIntvls_Type()
)
atmfM4CellProtoCurrSupprIntvls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4CellProtoCurrSupprIntvls.setStatus("current")
_AtmfM4CellProtoCurrProtoErrors_Type = Counter32
_AtmfM4CellProtoCurrProtoErrors_Object = MibTableColumn
atmfM4CellProtoCurrProtoErrors = _AtmfM4CellProtoCurrProtoErrors_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 15, 1, 4),
    _AtmfM4CellProtoCurrProtoErrors_Type()
)
atmfM4CellProtoCurrProtoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4CellProtoCurrProtoErrors.setStatus("current")
_AtmfM4CellProtoCurrInOAMCells_Type = Counter32
_AtmfM4CellProtoCurrInOAMCells_Object = MibTableColumn
atmfM4CellProtoCurrInOAMCells = _AtmfM4CellProtoCurrInOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 15, 1, 5),
    _AtmfM4CellProtoCurrInOAMCells_Type()
)
atmfM4CellProtoCurrInOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4CellProtoCurrInOAMCells.setStatus("current")
_AtmfM4CellProtoHistTable_Object = MibTable
atmfM4CellProtoHistTable = _AtmfM4CellProtoHistTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 16)
)
if mibBuilder.loadTexts:
    atmfM4CellProtoHistTable.setStatus("current")
_AtmfM4CellProtoHistEntry_Object = MibTableRow
atmfM4CellProtoHistEntry = _AtmfM4CellProtoHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 16, 1)
)
atmfM4CellProtoHistEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-FORUM-M4-MIB", "atmfM4CellProtoHistIndex"),
)
if mibBuilder.loadTexts:
    atmfM4CellProtoHistEntry.setStatus("current")


class _AtmfM4CellProtoHistIndex_Type(Integer32):
    """Custom type atmfM4CellProtoHistIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AtmfM4CellProtoHistIndex_Type.__name__ = "Integer32"
_AtmfM4CellProtoHistIndex_Object = MibTableColumn
atmfM4CellProtoHistIndex = _AtmfM4CellProtoHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 16, 1, 1),
    _AtmfM4CellProtoHistIndex_Type()
)
atmfM4CellProtoHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmfM4CellProtoHistIndex.setStatus("current")
_AtmfM4CellProtoHistSuspect_Type = TruthValue
_AtmfM4CellProtoHistSuspect_Object = MibTableColumn
atmfM4CellProtoHistSuspect = _AtmfM4CellProtoHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 16, 1, 2),
    _AtmfM4CellProtoHistSuspect_Type()
)
atmfM4CellProtoHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4CellProtoHistSuspect.setStatus("current")
_AtmfM4CellProtoHistElapsedTime_Type = TimeInterval
_AtmfM4CellProtoHistElapsedTime_Object = MibTableColumn
atmfM4CellProtoHistElapsedTime = _AtmfM4CellProtoHistElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 16, 1, 3),
    _AtmfM4CellProtoHistElapsedTime_Type()
)
atmfM4CellProtoHistElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4CellProtoHistElapsedTime.setStatus("current")
_AtmfM4CellProtoHistSupprIntvls_Type = Counter32
_AtmfM4CellProtoHistSupprIntvls_Object = MibTableColumn
atmfM4CellProtoHistSupprIntvls = _AtmfM4CellProtoHistSupprIntvls_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 16, 1, 4),
    _AtmfM4CellProtoHistSupprIntvls_Type()
)
atmfM4CellProtoHistSupprIntvls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4CellProtoHistSupprIntvls.setStatus("current")
_AtmfM4CellProtoHistProtoErrors_Type = Counter32
_AtmfM4CellProtoHistProtoErrors_Object = MibTableColumn
atmfM4CellProtoHistProtoErrors = _AtmfM4CellProtoHistProtoErrors_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 16, 1, 5),
    _AtmfM4CellProtoHistProtoErrors_Type()
)
atmfM4CellProtoHistProtoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4CellProtoHistProtoErrors.setStatus("current")
_AtmfM4CellProtoHistInOAMCells_Type = Counter32
_AtmfM4CellProtoHistInOAMCells_Object = MibTableColumn
atmfM4CellProtoHistInOAMCells = _AtmfM4CellProtoHistInOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 16, 1, 6),
    _AtmfM4CellProtoHistInOAMCells_Type()
)
atmfM4CellProtoHistInOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4CellProtoHistInOAMCells.setStatus("current")
_AtmfM4CellProtoErrorTable_Object = MibTable
atmfM4CellProtoErrorTable = _AtmfM4CellProtoErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 17)
)
if mibBuilder.loadTexts:
    atmfM4CellProtoErrorTable.setStatus("current")
_AtmfM4CellProtoErrorEntry_Object = MibTableRow
atmfM4CellProtoErrorEntry = _AtmfM4CellProtoErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 17, 1)
)
atmfM4CellProtoErrorEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-FORUM-M4-MIB", "atmfM4CellProtoErrorCode"),
)
if mibBuilder.loadTexts:
    atmfM4CellProtoErrorEntry.setStatus("current")
_AtmfM4CellProtoErrorCode_Type = Integer32
_AtmfM4CellProtoErrorCode_Object = MibTableColumn
atmfM4CellProtoErrorCode = _AtmfM4CellProtoErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 17, 1, 1),
    _AtmfM4CellProtoErrorCode_Type()
)
atmfM4CellProtoErrorCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmfM4CellProtoErrorCode.setStatus("current")
_AtmfM4CellProtoErrorTime_Type = TimeStamp
_AtmfM4CellProtoErrorTime_Object = MibTableColumn
atmfM4CellProtoErrorTime = _AtmfM4CellProtoErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 17, 1, 2),
    _AtmfM4CellProtoErrorTime_Type()
)
atmfM4CellProtoErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4CellProtoErrorTime.setStatus("current")
_AtmfM4CellProtoErrorReason_Type = Integer32
_AtmfM4CellProtoErrorReason_Object = MibTableColumn
atmfM4CellProtoErrorReason = _AtmfM4CellProtoErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 17, 1, 3),
    _AtmfM4CellProtoErrorReason_Type()
)
atmfM4CellProtoErrorReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4CellProtoErrorReason.setStatus("current")


class _AtmfM4CellProtoErrorVpi_Type(Integer32):
    """Custom type atmfM4CellProtoErrorVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AtmfM4CellProtoErrorVpi_Type.__name__ = "Integer32"
_AtmfM4CellProtoErrorVpi_Object = MibTableColumn
atmfM4CellProtoErrorVpi = _AtmfM4CellProtoErrorVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 17, 1, 4),
    _AtmfM4CellProtoErrorVpi_Type()
)
atmfM4CellProtoErrorVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4CellProtoErrorVpi.setStatus("current")


class _AtmfM4CellProtoErrorVci_Type(Integer32):
    """Custom type atmfM4CellProtoErrorVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmfM4CellProtoErrorVci_Type.__name__ = "Integer32"
_AtmfM4CellProtoErrorVci_Object = MibTableColumn
atmfM4CellProtoErrorVci = _AtmfM4CellProtoErrorVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 17, 1, 5),
    _AtmfM4CellProtoErrorVci_Type()
)
atmfM4CellProtoErrorVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4CellProtoErrorVci.setStatus("current")
_AtmfM4TcProtoCurrTable_Object = MibTable
atmfM4TcProtoCurrTable = _AtmfM4TcProtoCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 18)
)
if mibBuilder.loadTexts:
    atmfM4TcProtoCurrTable.setStatus("current")
_AtmfM4TcProtoCurrEntry_Object = MibTableRow
atmfM4TcProtoCurrEntry = _AtmfM4TcProtoCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 18, 1)
)
atmfM4TcProtoCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmfM4TcProtoCurrEntry.setStatus("current")
_AtmfM4TcProtoCurrSuspect_Type = TruthValue
_AtmfM4TcProtoCurrSuspect_Object = MibTableColumn
atmfM4TcProtoCurrSuspect = _AtmfM4TcProtoCurrSuspect_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 18, 1, 1),
    _AtmfM4TcProtoCurrSuspect_Type()
)
atmfM4TcProtoCurrSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4TcProtoCurrSuspect.setStatus("current")
_AtmfM4TcProtoCurrElapsedTime_Type = TimeInterval
_AtmfM4TcProtoCurrElapsedTime_Object = MibTableColumn
atmfM4TcProtoCurrElapsedTime = _AtmfM4TcProtoCurrElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 18, 1, 2),
    _AtmfM4TcProtoCurrElapsedTime_Type()
)
atmfM4TcProtoCurrElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4TcProtoCurrElapsedTime.setStatus("current")
_AtmfM4TcProtoCurrSupprIntvls_Type = Counter32
_AtmfM4TcProtoCurrSupprIntvls_Object = MibTableColumn
atmfM4TcProtoCurrSupprIntvls = _AtmfM4TcProtoCurrSupprIntvls_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 18, 1, 3),
    _AtmfM4TcProtoCurrSupprIntvls_Type()
)
atmfM4TcProtoCurrSupprIntvls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4TcProtoCurrSupprIntvls.setStatus("current")
_AtmfM4TcProtoCurrDiscardHECViol_Type = Counter32
_AtmfM4TcProtoCurrDiscardHECViol_Object = MibTableColumn
atmfM4TcProtoCurrDiscardHECViol = _AtmfM4TcProtoCurrDiscardHECViol_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 18, 1, 4),
    _AtmfM4TcProtoCurrDiscardHECViol_Type()
)
atmfM4TcProtoCurrDiscardHECViol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4TcProtoCurrDiscardHECViol.setStatus("current")
_AtmfM4TcProtoHistTable_Object = MibTable
atmfM4TcProtoHistTable = _AtmfM4TcProtoHistTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 19)
)
if mibBuilder.loadTexts:
    atmfM4TcProtoHistTable.setStatus("current")
_AtmfM4TcProtoHistEntry_Object = MibTableRow
atmfM4TcProtoHistEntry = _AtmfM4TcProtoHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 19, 1)
)
atmfM4TcProtoHistEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-FORUM-M4-MIB", "atmfM4TcProtoHistIndex"),
)
if mibBuilder.loadTexts:
    atmfM4TcProtoHistEntry.setStatus("current")


class _AtmfM4TcProtoHistIndex_Type(Integer32):
    """Custom type atmfM4TcProtoHistIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AtmfM4TcProtoHistIndex_Type.__name__ = "Integer32"
_AtmfM4TcProtoHistIndex_Object = MibTableColumn
atmfM4TcProtoHistIndex = _AtmfM4TcProtoHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 19, 1, 1),
    _AtmfM4TcProtoHistIndex_Type()
)
atmfM4TcProtoHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmfM4TcProtoHistIndex.setStatus("current")
_AtmfM4TcProtoHistSuspect_Type = TruthValue
_AtmfM4TcProtoHistSuspect_Object = MibTableColumn
atmfM4TcProtoHistSuspect = _AtmfM4TcProtoHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 19, 1, 2),
    _AtmfM4TcProtoHistSuspect_Type()
)
atmfM4TcProtoHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4TcProtoHistSuspect.setStatus("current")
_AtmfM4TcProtoHistElapsedTime_Type = TimeInterval
_AtmfM4TcProtoHistElapsedTime_Object = MibTableColumn
atmfM4TcProtoHistElapsedTime = _AtmfM4TcProtoHistElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 19, 1, 3),
    _AtmfM4TcProtoHistElapsedTime_Type()
)
atmfM4TcProtoHistElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4TcProtoHistElapsedTime.setStatus("current")
_AtmfM4TcProtoHistSupprIntvls_Type = Unsigned32
_AtmfM4TcProtoHistSupprIntvls_Object = MibTableColumn
atmfM4TcProtoHistSupprIntvls = _AtmfM4TcProtoHistSupprIntvls_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 19, 1, 4),
    _AtmfM4TcProtoHistSupprIntvls_Type()
)
atmfM4TcProtoHistSupprIntvls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4TcProtoHistSupprIntvls.setStatus("current")
_AtmfM4TcProtoHistDiscardHECViol_Type = Unsigned32
_AtmfM4TcProtoHistDiscardHECViol_Object = MibTableColumn
atmfM4TcProtoHistDiscardHECViol = _AtmfM4TcProtoHistDiscardHECViol_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 19, 1, 5),
    _AtmfM4TcProtoHistDiscardHECViol_Type()
)
atmfM4TcProtoHistDiscardHECViol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4TcProtoHistDiscardHECViol.setStatus("current")
_AtmfM4VpUpcNpcCurrTable_Object = MibTable
atmfM4VpUpcNpcCurrTable = _AtmfM4VpUpcNpcCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 20)
)
if mibBuilder.loadTexts:
    atmfM4VpUpcNpcCurrTable.setStatus("current")
_AtmfM4VpUpcNpcCurrEntry_Object = MibTableRow
atmfM4VpUpcNpcCurrEntry = _AtmfM4VpUpcNpcCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 20, 1)
)
atmfM4VpUpcNpcCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    atmfM4VpUpcNpcCurrEntry.setStatus("current")
_AtmfM4VpUpcNpcCurrSuspect_Type = TruthValue
_AtmfM4VpUpcNpcCurrSuspect_Object = MibTableColumn
atmfM4VpUpcNpcCurrSuspect = _AtmfM4VpUpcNpcCurrSuspect_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 20, 1, 1),
    _AtmfM4VpUpcNpcCurrSuspect_Type()
)
atmfM4VpUpcNpcCurrSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VpUpcNpcCurrSuspect.setStatus("current")
_AtmfM4VpUpcNpcCurrElapsedTime_Type = TimeInterval
_AtmfM4VpUpcNpcCurrElapsedTime_Object = MibTableColumn
atmfM4VpUpcNpcCurrElapsedTime = _AtmfM4VpUpcNpcCurrElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 20, 1, 2),
    _AtmfM4VpUpcNpcCurrElapsedTime_Type()
)
atmfM4VpUpcNpcCurrElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VpUpcNpcCurrElapsedTime.setStatus("current")
_AtmfM4VpUpcNpcCurrSupprIntvls_Type = Counter32
_AtmfM4VpUpcNpcCurrSupprIntvls_Object = MibTableColumn
atmfM4VpUpcNpcCurrSupprIntvls = _AtmfM4VpUpcNpcCurrSupprIntvls_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 20, 1, 3),
    _AtmfM4VpUpcNpcCurrSupprIntvls_Type()
)
atmfM4VpUpcNpcCurrSupprIntvls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VpUpcNpcCurrSupprIntvls.setStatus("current")
_AtmfM4VpUpcNpcCurrDiscardedCells_Type = Counter32
_AtmfM4VpUpcNpcCurrDiscardedCells_Object = MibTableColumn
atmfM4VpUpcNpcCurrDiscardedCells = _AtmfM4VpUpcNpcCurrDiscardedCells_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 20, 1, 4),
    _AtmfM4VpUpcNpcCurrDiscardedCells_Type()
)
atmfM4VpUpcNpcCurrDiscardedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VpUpcNpcCurrDiscardedCells.setStatus("current")
_AtmfM4VpUpcNpcCurrDiscardedClp0_Type = Counter32
_AtmfM4VpUpcNpcCurrDiscardedClp0_Object = MibTableColumn
atmfM4VpUpcNpcCurrDiscardedClp0 = _AtmfM4VpUpcNpcCurrDiscardedClp0_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 20, 1, 5),
    _AtmfM4VpUpcNpcCurrDiscardedClp0_Type()
)
atmfM4VpUpcNpcCurrDiscardedClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VpUpcNpcCurrDiscardedClp0.setStatus("current")
_AtmfM4VpUpcNpcCurrPassedCells_Type = Counter32
_AtmfM4VpUpcNpcCurrPassedCells_Object = MibTableColumn
atmfM4VpUpcNpcCurrPassedCells = _AtmfM4VpUpcNpcCurrPassedCells_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 20, 1, 6),
    _AtmfM4VpUpcNpcCurrPassedCells_Type()
)
atmfM4VpUpcNpcCurrPassedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VpUpcNpcCurrPassedCells.setStatus("current")
_AtmfM4VpUpcNpcCurrPassedClp0_Type = Counter32
_AtmfM4VpUpcNpcCurrPassedClp0_Object = MibTableColumn
atmfM4VpUpcNpcCurrPassedClp0 = _AtmfM4VpUpcNpcCurrPassedClp0_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 20, 1, 7),
    _AtmfM4VpUpcNpcCurrPassedClp0_Type()
)
atmfM4VpUpcNpcCurrPassedClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VpUpcNpcCurrPassedClp0.setStatus("current")
_AtmfM4VpUpcNpcHistTable_Object = MibTable
atmfM4VpUpcNpcHistTable = _AtmfM4VpUpcNpcHistTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 21)
)
if mibBuilder.loadTexts:
    atmfM4VpUpcNpcHistTable.setStatus("current")
_AtmfM4VpUpcNpcHistEntry_Object = MibTableRow
atmfM4VpUpcNpcHistEntry = _AtmfM4VpUpcNpcHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 21, 1)
)
atmfM4VpUpcNpcHistEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
    (0, "ATM-FORUM-M4-MIB", "atmfM4VpUpcNpcHistIndex"),
)
if mibBuilder.loadTexts:
    atmfM4VpUpcNpcHistEntry.setStatus("current")


class _AtmfM4VpUpcNpcHistIndex_Type(Integer32):
    """Custom type atmfM4VpUpcNpcHistIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AtmfM4VpUpcNpcHistIndex_Type.__name__ = "Integer32"
_AtmfM4VpUpcNpcHistIndex_Object = MibTableColumn
atmfM4VpUpcNpcHistIndex = _AtmfM4VpUpcNpcHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 21, 1, 1),
    _AtmfM4VpUpcNpcHistIndex_Type()
)
atmfM4VpUpcNpcHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmfM4VpUpcNpcHistIndex.setStatus("current")
_AtmfM4VpUpcNpcHistSuspect_Type = TruthValue
_AtmfM4VpUpcNpcHistSuspect_Object = MibTableColumn
atmfM4VpUpcNpcHistSuspect = _AtmfM4VpUpcNpcHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 21, 1, 2),
    _AtmfM4VpUpcNpcHistSuspect_Type()
)
atmfM4VpUpcNpcHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VpUpcNpcHistSuspect.setStatus("current")
_AtmfM4VpUpcNpcHistElapsedTime_Type = TimeInterval
_AtmfM4VpUpcNpcHistElapsedTime_Object = MibTableColumn
atmfM4VpUpcNpcHistElapsedTime = _AtmfM4VpUpcNpcHistElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 21, 1, 3),
    _AtmfM4VpUpcNpcHistElapsedTime_Type()
)
atmfM4VpUpcNpcHistElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VpUpcNpcHistElapsedTime.setStatus("current")
_AtmfM4VpUpcNpcHistSupprIntvls_Type = Unsigned32
_AtmfM4VpUpcNpcHistSupprIntvls_Object = MibTableColumn
atmfM4VpUpcNpcHistSupprIntvls = _AtmfM4VpUpcNpcHistSupprIntvls_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 21, 1, 4),
    _AtmfM4VpUpcNpcHistSupprIntvls_Type()
)
atmfM4VpUpcNpcHistSupprIntvls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VpUpcNpcHistSupprIntvls.setStatus("current")
_AtmfM4VpUpcNpcHistDiscardedCells_Type = Unsigned32
_AtmfM4VpUpcNpcHistDiscardedCells_Object = MibTableColumn
atmfM4VpUpcNpcHistDiscardedCells = _AtmfM4VpUpcNpcHistDiscardedCells_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 21, 1, 5),
    _AtmfM4VpUpcNpcHistDiscardedCells_Type()
)
atmfM4VpUpcNpcHistDiscardedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VpUpcNpcHistDiscardedCells.setStatus("current")
_AtmfM4VpUpcNpcHistDiscardedClp0_Type = Unsigned32
_AtmfM4VpUpcNpcHistDiscardedClp0_Object = MibTableColumn
atmfM4VpUpcNpcHistDiscardedClp0 = _AtmfM4VpUpcNpcHistDiscardedClp0_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 21, 1, 6),
    _AtmfM4VpUpcNpcHistDiscardedClp0_Type()
)
atmfM4VpUpcNpcHistDiscardedClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VpUpcNpcHistDiscardedClp0.setStatus("current")
_AtmfM4VpUpcNpcHistPassedCells_Type = Unsigned32
_AtmfM4VpUpcNpcHistPassedCells_Object = MibTableColumn
atmfM4VpUpcNpcHistPassedCells = _AtmfM4VpUpcNpcHistPassedCells_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 21, 1, 7),
    _AtmfM4VpUpcNpcHistPassedCells_Type()
)
atmfM4VpUpcNpcHistPassedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VpUpcNpcHistPassedCells.setStatus("current")
_AtmfM4VpUpcNpcHistPassedClp0_Type = Unsigned32
_AtmfM4VpUpcNpcHistPassedClp0_Object = MibTableColumn
atmfM4VpUpcNpcHistPassedClp0 = _AtmfM4VpUpcNpcHistPassedClp0_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 21, 1, 8),
    _AtmfM4VpUpcNpcHistPassedClp0_Type()
)
atmfM4VpUpcNpcHistPassedClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VpUpcNpcHistPassedClp0.setStatus("current")
_AtmfM4VcUpcNpcCurrTable_Object = MibTable
atmfM4VcUpcNpcCurrTable = _AtmfM4VcUpcNpcCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 22)
)
if mibBuilder.loadTexts:
    atmfM4VcUpcNpcCurrTable.setStatus("current")
_AtmfM4VcUpcNpcCurrEntry_Object = MibTableRow
atmfM4VcUpcNpcCurrEntry = _AtmfM4VcUpcNpcCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 22, 1)
)
atmfM4VcUpcNpcCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    atmfM4VcUpcNpcCurrEntry.setStatus("current")
_AtmfM4VcUpcNpcCurrSuspect_Type = TruthValue
_AtmfM4VcUpcNpcCurrSuspect_Object = MibTableColumn
atmfM4VcUpcNpcCurrSuspect = _AtmfM4VcUpcNpcCurrSuspect_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 22, 1, 1),
    _AtmfM4VcUpcNpcCurrSuspect_Type()
)
atmfM4VcUpcNpcCurrSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VcUpcNpcCurrSuspect.setStatus("current")
_AtmfM4VcUpcNpcCurrElapsedTime_Type = TimeInterval
_AtmfM4VcUpcNpcCurrElapsedTime_Object = MibTableColumn
atmfM4VcUpcNpcCurrElapsedTime = _AtmfM4VcUpcNpcCurrElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 22, 1, 2),
    _AtmfM4VcUpcNpcCurrElapsedTime_Type()
)
atmfM4VcUpcNpcCurrElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VcUpcNpcCurrElapsedTime.setStatus("current")
_AtmfM4VcUpcNpcCurrSupprIntvls_Type = Counter32
_AtmfM4VcUpcNpcCurrSupprIntvls_Object = MibTableColumn
atmfM4VcUpcNpcCurrSupprIntvls = _AtmfM4VcUpcNpcCurrSupprIntvls_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 22, 1, 3),
    _AtmfM4VcUpcNpcCurrSupprIntvls_Type()
)
atmfM4VcUpcNpcCurrSupprIntvls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VcUpcNpcCurrSupprIntvls.setStatus("current")
_AtmfM4VcUpcNpcCurrDiscardedCells_Type = Counter32
_AtmfM4VcUpcNpcCurrDiscardedCells_Object = MibTableColumn
atmfM4VcUpcNpcCurrDiscardedCells = _AtmfM4VcUpcNpcCurrDiscardedCells_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 22, 1, 4),
    _AtmfM4VcUpcNpcCurrDiscardedCells_Type()
)
atmfM4VcUpcNpcCurrDiscardedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VcUpcNpcCurrDiscardedCells.setStatus("current")
_AtmfM4VcUpcNpcCurrDiscardedClp0_Type = Counter32
_AtmfM4VcUpcNpcCurrDiscardedClp0_Object = MibTableColumn
atmfM4VcUpcNpcCurrDiscardedClp0 = _AtmfM4VcUpcNpcCurrDiscardedClp0_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 22, 1, 5),
    _AtmfM4VcUpcNpcCurrDiscardedClp0_Type()
)
atmfM4VcUpcNpcCurrDiscardedClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VcUpcNpcCurrDiscardedClp0.setStatus("current")
_AtmfM4VcUpcNpcCurrPassedCells_Type = Counter32
_AtmfM4VcUpcNpcCurrPassedCells_Object = MibTableColumn
atmfM4VcUpcNpcCurrPassedCells = _AtmfM4VcUpcNpcCurrPassedCells_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 22, 1, 6),
    _AtmfM4VcUpcNpcCurrPassedCells_Type()
)
atmfM4VcUpcNpcCurrPassedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VcUpcNpcCurrPassedCells.setStatus("current")
_AtmfM4VcUpcNpcCurrPassedClp0_Type = Counter32
_AtmfM4VcUpcNpcCurrPassedClp0_Object = MibTableColumn
atmfM4VcUpcNpcCurrPassedClp0 = _AtmfM4VcUpcNpcCurrPassedClp0_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 22, 1, 7),
    _AtmfM4VcUpcNpcCurrPassedClp0_Type()
)
atmfM4VcUpcNpcCurrPassedClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VcUpcNpcCurrPassedClp0.setStatus("current")
_AtmfM4VcUpcNpcHistTable_Object = MibTable
atmfM4VcUpcNpcHistTable = _AtmfM4VcUpcNpcHistTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 23)
)
if mibBuilder.loadTexts:
    atmfM4VcUpcNpcHistTable.setStatus("current")
_AtmfM4VcUpcNpcHistEntry_Object = MibTableRow
atmfM4VcUpcNpcHistEntry = _AtmfM4VcUpcNpcHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 23, 1)
)
atmfM4VcUpcNpcHistEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
    (0, "ATM-FORUM-M4-MIB", "atmfM4VcUpcNpcHistIndex"),
)
if mibBuilder.loadTexts:
    atmfM4VcUpcNpcHistEntry.setStatus("current")


class _AtmfM4VcUpcNpcHistIndex_Type(Integer32):
    """Custom type atmfM4VcUpcNpcHistIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AtmfM4VcUpcNpcHistIndex_Type.__name__ = "Integer32"
_AtmfM4VcUpcNpcHistIndex_Object = MibTableColumn
atmfM4VcUpcNpcHistIndex = _AtmfM4VcUpcNpcHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 23, 1, 1),
    _AtmfM4VcUpcNpcHistIndex_Type()
)
atmfM4VcUpcNpcHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmfM4VcUpcNpcHistIndex.setStatus("current")
_AtmfM4VcUpcNpcHistSuspect_Type = TruthValue
_AtmfM4VcUpcNpcHistSuspect_Object = MibTableColumn
atmfM4VcUpcNpcHistSuspect = _AtmfM4VcUpcNpcHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 23, 1, 2),
    _AtmfM4VcUpcNpcHistSuspect_Type()
)
atmfM4VcUpcNpcHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VcUpcNpcHistSuspect.setStatus("current")
_AtmfM4VcUpcNpcHistElapsedTime_Type = TimeInterval
_AtmfM4VcUpcNpcHistElapsedTime_Object = MibTableColumn
atmfM4VcUpcNpcHistElapsedTime = _AtmfM4VcUpcNpcHistElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 23, 1, 3),
    _AtmfM4VcUpcNpcHistElapsedTime_Type()
)
atmfM4VcUpcNpcHistElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VcUpcNpcHistElapsedTime.setStatus("current")
_AtmfM4VcUpcNpcHistSupprIntvls_Type = Unsigned32
_AtmfM4VcUpcNpcHistSupprIntvls_Object = MibTableColumn
atmfM4VcUpcNpcHistSupprIntvls = _AtmfM4VcUpcNpcHistSupprIntvls_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 23, 1, 4),
    _AtmfM4VcUpcNpcHistSupprIntvls_Type()
)
atmfM4VcUpcNpcHistSupprIntvls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VcUpcNpcHistSupprIntvls.setStatus("current")
_AtmfM4VcUpcNpcHistDiscardedCells_Type = Unsigned32
_AtmfM4VcUpcNpcHistDiscardedCells_Object = MibTableColumn
atmfM4VcUpcNpcHistDiscardedCells = _AtmfM4VcUpcNpcHistDiscardedCells_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 23, 1, 5),
    _AtmfM4VcUpcNpcHistDiscardedCells_Type()
)
atmfM4VcUpcNpcHistDiscardedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VcUpcNpcHistDiscardedCells.setStatus("current")
_AtmfM4VcUpcNpcHistDiscardedClp0_Type = Unsigned32
_AtmfM4VcUpcNpcHistDiscardedClp0_Object = MibTableColumn
atmfM4VcUpcNpcHistDiscardedClp0 = _AtmfM4VcUpcNpcHistDiscardedClp0_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 23, 1, 6),
    _AtmfM4VcUpcNpcHistDiscardedClp0_Type()
)
atmfM4VcUpcNpcHistDiscardedClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VcUpcNpcHistDiscardedClp0.setStatus("current")
_AtmfM4VcUpcNpcHistPassedCells_Type = Unsigned32
_AtmfM4VcUpcNpcHistPassedCells_Object = MibTableColumn
atmfM4VcUpcNpcHistPassedCells = _AtmfM4VcUpcNpcHistPassedCells_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 23, 1, 7),
    _AtmfM4VcUpcNpcHistPassedCells_Type()
)
atmfM4VcUpcNpcHistPassedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VcUpcNpcHistPassedCells.setStatus("current")
_AtmfM4VcUpcNpcHistPassedClp0_Type = Unsigned32
_AtmfM4VcUpcNpcHistPassedClp0_Object = MibTableColumn
atmfM4VcUpcNpcHistPassedClp0 = _AtmfM4VcUpcNpcHistPassedClp0_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 23, 1, 8),
    _AtmfM4VcUpcNpcHistPassedClp0_Type()
)
atmfM4VcUpcNpcHistPassedClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VcUpcNpcHistPassedClp0.setStatus("current")
_AtmfM4TestTypes_ObjectIdentity = ObjectIdentity
atmfM4TestTypes = _AtmfM4TestTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 24)
)
_AtmfM4TestOAMLoopbackSeg_ObjectIdentity = ObjectIdentity
atmfM4TestOAMLoopbackSeg = _AtmfM4TestOAMLoopbackSeg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 24, 1)
)
if mibBuilder.loadTexts:
    atmfM4TestOAMLoopbackSeg.setStatus("current")
_AtmfM4TestOAMLoopbackE2E_ObjectIdentity = ObjectIdentity
atmfM4TestOAMLoopbackE2E = _AtmfM4TestOAMLoopbackE2E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 24, 2)
)
if mibBuilder.loadTexts:
    atmfM4TestOAMLoopbackE2E.setStatus("current")
_AtmfM4VpTestTable_Object = MibTable
atmfM4VpTestTable = _AtmfM4VpTestTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 25)
)
if mibBuilder.loadTexts:
    atmfM4VpTestTable.setStatus("current")
_AtmfM4VpTestEntry_Object = MibTableRow
atmfM4VpTestEntry = _AtmfM4VpTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 25, 1)
)
atmfM4VpTestEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
    (0, "ATM-FORUM-M4-MIB", "atmfM4VpTestObject"),
)
if mibBuilder.loadTexts:
    atmfM4VpTestEntry.setStatus("current")


class _AtmfM4VpTestObject_Type(Integer32):
    """Custom type atmfM4VpTestObject based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vpcTp", 2),
          ("vplTp", 1))
    )


_AtmfM4VpTestObject_Type.__name__ = "Integer32"
_AtmfM4VpTestObject_Object = MibTableColumn
atmfM4VpTestObject = _AtmfM4VpTestObject_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 25, 1, 1),
    _AtmfM4VpTestObject_Type()
)
atmfM4VpTestObject.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmfM4VpTestObject.setStatus("current")
_AtmfM4VpTestId_Type = TestAndIncr
_AtmfM4VpTestId_Object = MibTableColumn
atmfM4VpTestId = _AtmfM4VpTestId_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 25, 1, 2),
    _AtmfM4VpTestId_Type()
)
atmfM4VpTestId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfM4VpTestId.setStatus("current")


class _AtmfM4VpTestStatus_Type(Integer32):
    """Custom type atmfM4VpTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inUse", 2),
          ("notInUse", 1))
    )


_AtmfM4VpTestStatus_Type.__name__ = "Integer32"
_AtmfM4VpTestStatus_Object = MibTableColumn
atmfM4VpTestStatus = _AtmfM4VpTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 25, 1, 3),
    _AtmfM4VpTestStatus_Type()
)
atmfM4VpTestStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfM4VpTestStatus.setStatus("current")
_AtmfM4VpTestType_Type = AutonomousType
_AtmfM4VpTestType_Object = MibTableColumn
atmfM4VpTestType = _AtmfM4VpTestType_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 25, 1, 4),
    _AtmfM4VpTestType_Type()
)
atmfM4VpTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfM4VpTestType.setStatus("current")


class _AtmfM4VpTestResult_Type(Integer32):
    """Custom type atmfM4VpTestResult based on Integer32"""
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
        *(("aborted", 6),
          ("failed", 7),
          ("inProgress", 3),
          ("none", 1),
          ("notSupported", 4),
          ("success", 2),
          ("unAbleToRun", 5))
    )


_AtmfM4VpTestResult_Type.__name__ = "Integer32"
_AtmfM4VpTestResult_Object = MibTableColumn
atmfM4VpTestResult = _AtmfM4VpTestResult_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 25, 1, 5),
    _AtmfM4VpTestResult_Type()
)
atmfM4VpTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VpTestResult.setStatus("current")
_AtmfM4VpTestCode_Type = ObjectIdentifier
_AtmfM4VpTestCode_Object = MibTableColumn
atmfM4VpTestCode = _AtmfM4VpTestCode_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 25, 1, 6),
    _AtmfM4VpTestCode_Type()
)
atmfM4VpTestCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VpTestCode.setStatus("current")
_AtmfM4VpTestOwner_Type = OwnerString
_AtmfM4VpTestOwner_Object = MibTableColumn
atmfM4VpTestOwner = _AtmfM4VpTestOwner_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 25, 1, 7),
    _AtmfM4VpTestOwner_Type()
)
atmfM4VpTestOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfM4VpTestOwner.setStatus("current")
_AtmfM4VcTestTable_Object = MibTable
atmfM4VcTestTable = _AtmfM4VcTestTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 26)
)
if mibBuilder.loadTexts:
    atmfM4VcTestTable.setStatus("current")
_AtmfM4VcTestEntry_Object = MibTableRow
atmfM4VcTestEntry = _AtmfM4VcTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 26, 1)
)
atmfM4VcTestEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
    (0, "ATM-FORUM-M4-MIB", "atmfM4VcTestObject"),
)
if mibBuilder.loadTexts:
    atmfM4VcTestEntry.setStatus("current")


class _AtmfM4VcTestObject_Type(Integer32):
    """Custom type atmfM4VcTestObject based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vccTp", 2),
          ("vclTp", 1))
    )


_AtmfM4VcTestObject_Type.__name__ = "Integer32"
_AtmfM4VcTestObject_Object = MibTableColumn
atmfM4VcTestObject = _AtmfM4VcTestObject_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 26, 1, 1),
    _AtmfM4VcTestObject_Type()
)
atmfM4VcTestObject.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmfM4VcTestObject.setStatus("current")
_AtmfM4VcTestId_Type = TestAndIncr
_AtmfM4VcTestId_Object = MibTableColumn
atmfM4VcTestId = _AtmfM4VcTestId_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 26, 1, 2),
    _AtmfM4VcTestId_Type()
)
atmfM4VcTestId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfM4VcTestId.setStatus("current")


class _AtmfM4VcTestStatus_Type(Integer32):
    """Custom type atmfM4VcTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inUse", 2),
          ("notInUse", 1))
    )


_AtmfM4VcTestStatus_Type.__name__ = "Integer32"
_AtmfM4VcTestStatus_Object = MibTableColumn
atmfM4VcTestStatus = _AtmfM4VcTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 26, 1, 3),
    _AtmfM4VcTestStatus_Type()
)
atmfM4VcTestStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfM4VcTestStatus.setStatus("current")
_AtmfM4VcTestType_Type = AutonomousType
_AtmfM4VcTestType_Object = MibTableColumn
atmfM4VcTestType = _AtmfM4VcTestType_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 26, 1, 4),
    _AtmfM4VcTestType_Type()
)
atmfM4VcTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfM4VcTestType.setStatus("current")


class _AtmfM4VcTestResult_Type(Integer32):
    """Custom type atmfM4VcTestResult based on Integer32"""
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
        *(("aborted", 6),
          ("failed", 7),
          ("inProgress", 3),
          ("none", 1),
          ("notSupported", 4),
          ("success", 2),
          ("unAbleToRun", 5))
    )


_AtmfM4VcTestResult_Type.__name__ = "Integer32"
_AtmfM4VcTestResult_Object = MibTableColumn
atmfM4VcTestResult = _AtmfM4VcTestResult_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 26, 1, 5),
    _AtmfM4VcTestResult_Type()
)
atmfM4VcTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VcTestResult.setStatus("current")
_AtmfM4VcTestCode_Type = ObjectIdentifier
_AtmfM4VcTestCode_Object = MibTableColumn
atmfM4VcTestCode = _AtmfM4VcTestCode_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 26, 1, 6),
    _AtmfM4VcTestCode_Type()
)
atmfM4VcTestCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4VcTestCode.setStatus("current")
_AtmfM4VcTestOwner_Type = OwnerString
_AtmfM4VcTestOwner_Object = MibTableColumn
atmfM4VcTestOwner = _AtmfM4VcTestOwner_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 26, 1, 7),
    _AtmfM4VcTestOwner_Type()
)
atmfM4VcTestOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfM4VcTestOwner.setStatus("current")
_AtmfM4EquipTable_Object = MibTable
atmfM4EquipTable = _AtmfM4EquipTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 28)
)
if mibBuilder.loadTexts:
    atmfM4EquipTable.setStatus("current")
_AtmfM4EquipEntry_Object = MibTableRow
atmfM4EquipEntry = _AtmfM4EquipEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 28, 1)
)
atmfM4EquipEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    atmfM4EquipEntry.setStatus("current")


class _AtmfM4EquipAdminStatus_Type(Integer32):
    """Custom type atmfM4EquipAdminStatus based on Integer32"""
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


_AtmfM4EquipAdminStatus_Type.__name__ = "Integer32"
_AtmfM4EquipAdminStatus_Object = MibTableColumn
atmfM4EquipAdminStatus = _AtmfM4EquipAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 28, 1, 1),
    _AtmfM4EquipAdminStatus_Type()
)
atmfM4EquipAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfM4EquipAdminStatus.setStatus("current")
_AtmfM4EquipLocation_Type = DisplayString
_AtmfM4EquipLocation_Object = MibTableColumn
atmfM4EquipLocation = _AtmfM4EquipLocation_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 28, 1, 2),
    _AtmfM4EquipLocation_Type()
)
atmfM4EquipLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfM4EquipLocation.setStatus("current")


class _AtmfM4EquipOperStatus_Type(Integer32):
    """Custom type atmfM4EquipOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_AtmfM4EquipOperStatus_Type.__name__ = "Integer32"
_AtmfM4EquipOperStatus_Object = MibTableColumn
atmfM4EquipOperStatus = _AtmfM4EquipOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 28, 1, 3),
    _AtmfM4EquipOperStatus_Type()
)
atmfM4EquipOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4EquipOperStatus.setStatus("current")
_AtmfM4EquipVendor_Type = DisplayString
_AtmfM4EquipVendor_Object = MibTableColumn
atmfM4EquipVendor = _AtmfM4EquipVendor_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 28, 1, 4),
    _AtmfM4EquipVendor_Type()
)
atmfM4EquipVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4EquipVendor.setStatus("current")
_AtmfM4EquipVersion_Type = AutonomousType
_AtmfM4EquipVersion_Object = MibTableColumn
atmfM4EquipVersion = _AtmfM4EquipVersion_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 28, 1, 5),
    _AtmfM4EquipVersion_Type()
)
atmfM4EquipVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4EquipVersion.setStatus("current")
_AtmfM4EquipUserLabel_Type = DisplayString
_AtmfM4EquipUserLabel_Object = MibTableColumn
atmfM4EquipUserLabel = _AtmfM4EquipUserLabel_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 28, 1, 6),
    _AtmfM4EquipUserLabel_Type()
)
atmfM4EquipUserLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfM4EquipUserLabel.setStatus("current")


class _AtmfM4EquipAlarmSeverityIndex_Type(Integer32):
    """Custom type atmfM4EquipAlarmSeverityIndex based on Integer32"""
    defaultValue = 0


_AtmfM4EquipAlarmSeverityIndex_Object = MibTableColumn
atmfM4EquipAlarmSeverityIndex = _AtmfM4EquipAlarmSeverityIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 28, 1, 7),
    _AtmfM4EquipAlarmSeverityIndex_Type()
)
atmfM4EquipAlarmSeverityIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfM4EquipAlarmSeverityIndex.setStatus("current")
_AtmfM4EquipHolderTable_Object = MibTable
atmfM4EquipHolderTable = _AtmfM4EquipHolderTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 29)
)
if mibBuilder.loadTexts:
    atmfM4EquipHolderTable.setStatus("current")
_AtmfM4EquipHolderEntry_Object = MibTableRow
atmfM4EquipHolderEntry = _AtmfM4EquipHolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 29, 1)
)
atmfM4EquipHolderEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    atmfM4EquipHolderEntry.setStatus("current")


class _AtmfM4EquipHolderType_Type(Integer32):
    """Custom type atmfM4EquipHolderType based on Integer32"""
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
        *(("drawer", 3),
          ("rack", 1),
          ("shelf", 2),
          ("slot", 4))
    )


_AtmfM4EquipHolderType_Type.__name__ = "Integer32"
_AtmfM4EquipHolderType_Object = MibTableColumn
atmfM4EquipHolderType = _AtmfM4EquipHolderType_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 29, 1, 1),
    _AtmfM4EquipHolderType_Type()
)
atmfM4EquipHolderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4EquipHolderType.setStatus("current")
_AtmfM4EquipHolderAcceptableTypes_Type = DisplayString
_AtmfM4EquipHolderAcceptableTypes_Object = MibTableColumn
atmfM4EquipHolderAcceptableTypes = _AtmfM4EquipHolderAcceptableTypes_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 29, 1, 2),
    _AtmfM4EquipHolderAcceptableTypes_Type()
)
atmfM4EquipHolderAcceptableTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4EquipHolderAcceptableTypes.setStatus("current")


class _AtmfM4EquipHolderSlotStatus_Type(Integer32):
    """Custom type atmfM4EquipHolderSlotStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("empty", 1),
          ("full", 2))
    )


_AtmfM4EquipHolderSlotStatus_Type.__name__ = "Integer32"
_AtmfM4EquipHolderSlotStatus_Object = MibTableColumn
atmfM4EquipHolderSlotStatus = _AtmfM4EquipHolderSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 29, 1, 3),
    _AtmfM4EquipHolderSlotStatus_Type()
)
atmfM4EquipHolderSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4EquipHolderSlotStatus.setStatus("current")


class _AtmfM4EquipHolderSwLoad_Type(Integer32):
    """Custom type atmfM4EquipHolderSwLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AtmfM4EquipHolderSwLoad_Type.__name__ = "Integer32"
_AtmfM4EquipHolderSwLoad_Object = MibTableColumn
atmfM4EquipHolderSwLoad = _AtmfM4EquipHolderSwLoad_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 29, 1, 4),
    _AtmfM4EquipHolderSwLoad_Type()
)
atmfM4EquipHolderSwLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfM4EquipHolderSwLoad.setStatus("current")
_AtmfM4PlugInUnitTable_Object = MibTable
atmfM4PlugInUnitTable = _AtmfM4PlugInUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 30)
)
if mibBuilder.loadTexts:
    atmfM4PlugInUnitTable.setStatus("current")
_AtmfM4PlugInUnitEntry_Object = MibTableRow
atmfM4PlugInUnitEntry = _AtmfM4PlugInUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 30, 1)
)
atmfM4PlugInUnitEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    atmfM4PlugInUnitEntry.setStatus("current")


class _AtmfM4PlugInUnitAdminStatus_Type(Integer32):
    """Custom type atmfM4PlugInUnitAdminStatus based on Integer32"""
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


_AtmfM4PlugInUnitAdminStatus_Type.__name__ = "Integer32"
_AtmfM4PlugInUnitAdminStatus_Object = MibTableColumn
atmfM4PlugInUnitAdminStatus = _AtmfM4PlugInUnitAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 30, 1, 1),
    _AtmfM4PlugInUnitAdminStatus_Type()
)
atmfM4PlugInUnitAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfM4PlugInUnitAdminStatus.setStatus("current")


class _AtmfM4PlugInUnitAvailStatus_Type(Integer32):
    """Custom type atmfM4PlugInUnitAvailStatus based on Integer32"""
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
        *(("available", 1),
          ("dependency", 7),
          ("failed", 3),
          ("inTest", 2),
          ("notInstalled", 5),
          ("offLine", 6),
          ("powerOff", 4))
    )


_AtmfM4PlugInUnitAvailStatus_Type.__name__ = "Integer32"
_AtmfM4PlugInUnitAvailStatus_Object = MibTableColumn
atmfM4PlugInUnitAvailStatus = _AtmfM4PlugInUnitAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 30, 1, 2),
    _AtmfM4PlugInUnitAvailStatus_Type()
)
atmfM4PlugInUnitAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4PlugInUnitAvailStatus.setStatus("current")


class _AtmfM4PlugInUnitOperStatus_Type(Integer32):
    """Custom type atmfM4PlugInUnitOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_AtmfM4PlugInUnitOperStatus_Type.__name__ = "Integer32"
_AtmfM4PlugInUnitOperStatus_Object = MibTableColumn
atmfM4PlugInUnitOperStatus = _AtmfM4PlugInUnitOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 30, 1, 3),
    _AtmfM4PlugInUnitOperStatus_Type()
)
atmfM4PlugInUnitOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4PlugInUnitOperStatus.setStatus("current")
_AtmfM4PlugInUnitVendor_Type = DisplayString
_AtmfM4PlugInUnitVendor_Object = MibTableColumn
atmfM4PlugInUnitVendor = _AtmfM4PlugInUnitVendor_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 30, 1, 4),
    _AtmfM4PlugInUnitVendor_Type()
)
atmfM4PlugInUnitVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4PlugInUnitVendor.setStatus("current")
_AtmfM4PlugInUnitVersion_Type = AutonomousType
_AtmfM4PlugInUnitVersion_Object = MibTableColumn
atmfM4PlugInUnitVersion = _AtmfM4PlugInUnitVersion_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 30, 1, 5),
    _AtmfM4PlugInUnitVersion_Type()
)
atmfM4PlugInUnitVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4PlugInUnitVersion.setStatus("current")


class _AtmfM4PlugInUnitAlarmSeverityIndex_Type(Integer32):
    """Custom type atmfM4PlugInUnitAlarmSeverityIndex based on Integer32"""
    defaultValue = 0


_AtmfM4PlugInUnitAlarmSeverityIndex_Object = MibTableColumn
atmfM4PlugInUnitAlarmSeverityIndex = _AtmfM4PlugInUnitAlarmSeverityIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 30, 1, 6),
    _AtmfM4PlugInUnitAlarmSeverityIndex_Type()
)
atmfM4PlugInUnitAlarmSeverityIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfM4PlugInUnitAlarmSeverityIndex.setStatus("current")
_AtmfM4HwRunningSwTable_Object = MibTable
atmfM4HwRunningSwTable = _AtmfM4HwRunningSwTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 32)
)
if mibBuilder.loadTexts:
    atmfM4HwRunningSwTable.setStatus("current")
_AtmfM4HwRunningSwEntry_Object = MibTableRow
atmfM4HwRunningSwEntry = _AtmfM4HwRunningSwEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 32, 1)
)
atmfM4HwRunningSwEntry.setIndexNames(
    (0, "ATM-FORUM-M4-MIB", "atmfM4HwRunningSwHwIndex"),
    (0, "ATM-FORUM-M4-MIB", "atmfM4HwRunningSwIndex"),
)
if mibBuilder.loadTexts:
    atmfM4HwRunningSwEntry.setStatus("current")


class _AtmfM4HwRunningSwHwIndex_Type(Integer32):
    """Custom type atmfM4HwRunningSwHwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AtmfM4HwRunningSwHwIndex_Type.__name__ = "Integer32"
_AtmfM4HwRunningSwHwIndex_Object = MibTableColumn
atmfM4HwRunningSwHwIndex = _AtmfM4HwRunningSwHwIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 32, 1, 1),
    _AtmfM4HwRunningSwHwIndex_Type()
)
atmfM4HwRunningSwHwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmfM4HwRunningSwHwIndex.setStatus("current")


class _AtmfM4HwRunningSwIndex_Type(Integer32):
    """Custom type atmfM4HwRunningSwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AtmfM4HwRunningSwIndex_Type.__name__ = "Integer32"
_AtmfM4HwRunningSwIndex_Object = MibTableColumn
atmfM4HwRunningSwIndex = _AtmfM4HwRunningSwIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 32, 1, 2),
    _AtmfM4HwRunningSwIndex_Type()
)
atmfM4HwRunningSwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmfM4HwRunningSwIndex.setStatus("current")


class _AtmfM4HwRunningSwSwIndex_Type(Integer32):
    """Custom type atmfM4HwRunningSwSwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AtmfM4HwRunningSwSwIndex_Type.__name__ = "Integer32"
_AtmfM4HwRunningSwSwIndex_Object = MibTableColumn
atmfM4HwRunningSwSwIndex = _AtmfM4HwRunningSwSwIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 32, 1, 3),
    _AtmfM4HwRunningSwSwIndex_Type()
)
atmfM4HwRunningSwSwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4HwRunningSwSwIndex.setStatus("current")
_AtmfM4HwInstalledSwTable_Object = MibTable
atmfM4HwInstalledSwTable = _AtmfM4HwInstalledSwTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 33)
)
if mibBuilder.loadTexts:
    atmfM4HwInstalledSwTable.setStatus("current")
_AtmfM4HwInstalledSwEntry_Object = MibTableRow
atmfM4HwInstalledSwEntry = _AtmfM4HwInstalledSwEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 33, 1)
)
atmfM4HwInstalledSwEntry.setIndexNames(
    (0, "ATM-FORUM-M4-MIB", "atmfM4HwInstalledSwHwIndex"),
    (0, "ATM-FORUM-M4-MIB", "atmfM4HwInstalledSwIndex"),
)
if mibBuilder.loadTexts:
    atmfM4HwInstalledSwEntry.setStatus("current")


class _AtmfM4HwInstalledSwHwIndex_Type(Integer32):
    """Custom type atmfM4HwInstalledSwHwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AtmfM4HwInstalledSwHwIndex_Type.__name__ = "Integer32"
_AtmfM4HwInstalledSwHwIndex_Object = MibTableColumn
atmfM4HwInstalledSwHwIndex = _AtmfM4HwInstalledSwHwIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 33, 1, 1),
    _AtmfM4HwInstalledSwHwIndex_Type()
)
atmfM4HwInstalledSwHwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmfM4HwInstalledSwHwIndex.setStatus("current")


class _AtmfM4HwInstalledSwIndex_Type(Integer32):
    """Custom type atmfM4HwInstalledSwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AtmfM4HwInstalledSwIndex_Type.__name__ = "Integer32"
_AtmfM4HwInstalledSwIndex_Object = MibTableColumn
atmfM4HwInstalledSwIndex = _AtmfM4HwInstalledSwIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 33, 1, 2),
    _AtmfM4HwInstalledSwIndex_Type()
)
atmfM4HwInstalledSwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4HwInstalledSwIndex.setStatus("current")


class _AtmfM4HwInstalledSwSwIndex_Type(Integer32):
    """Custom type atmfM4HwInstalledSwSwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AtmfM4HwInstalledSwSwIndex_Type.__name__ = "Integer32"
_AtmfM4HwInstalledSwSwIndex_Object = MibTableColumn
atmfM4HwInstalledSwSwIndex = _AtmfM4HwInstalledSwSwIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 33, 1, 3),
    _AtmfM4HwInstalledSwSwIndex_Type()
)
atmfM4HwInstalledSwSwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4HwInstalledSwSwIndex.setStatus("current")


class _AtmfM4HwSwAlarmSeverityIndex_Type(Integer32):
    """Custom type atmfM4HwSwAlarmSeverityIndex based on Integer32"""
    defaultValue = 0


_AtmfM4HwSwAlarmSeverityIndex_Object = MibTableColumn
atmfM4HwSwAlarmSeverityIndex = _AtmfM4HwSwAlarmSeverityIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 33, 1, 4),
    _AtmfM4HwSwAlarmSeverityIndex_Type()
)
atmfM4HwSwAlarmSeverityIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfM4HwSwAlarmSeverityIndex.setStatus("current")


class _AtmfM4AlarmSevDefault_Type(AtmfM4AlarmSeverity):
    """Custom type atmfM4AlarmSevDefault based on AtmfM4AlarmSeverity"""


_AtmfM4AlarmSevDefault_Object = MibScalar
atmfM4AlarmSevDefault = _AtmfM4AlarmSevDefault_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 34),
    _AtmfM4AlarmSevDefault_Type()
)
atmfM4AlarmSevDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfM4AlarmSevDefault.setStatus("current")
_AtmfM4AlarmSevProfileIndexNext_Type = Integer32
_AtmfM4AlarmSevProfileIndexNext_Object = MibScalar
atmfM4AlarmSevProfileIndexNext = _AtmfM4AlarmSevProfileIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 35),
    _AtmfM4AlarmSevProfileIndexNext_Type()
)
atmfM4AlarmSevProfileIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4AlarmSevProfileIndexNext.setStatus("current")
_AtmfM4AlarmSevProfileTable_Object = MibTable
atmfM4AlarmSevProfileTable = _AtmfM4AlarmSevProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 36)
)
if mibBuilder.loadTexts:
    atmfM4AlarmSevProfileTable.setStatus("current")
_AtmfM4AlarmSevProfileEntry_Object = MibTableRow
atmfM4AlarmSevProfileEntry = _AtmfM4AlarmSevProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 36, 1)
)
atmfM4AlarmSevProfileEntry.setIndexNames(
    (0, "ATM-FORUM-M4-MIB", "atmfM4AlarmSevProfileIndex"),
)
if mibBuilder.loadTexts:
    atmfM4AlarmSevProfileEntry.setStatus("current")
_AtmfM4AlarmSevProfileIndex_Type = Integer32
_AtmfM4AlarmSevProfileIndex_Object = MibTableColumn
atmfM4AlarmSevProfileIndex = _AtmfM4AlarmSevProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 36, 1, 1),
    _AtmfM4AlarmSevProfileIndex_Type()
)
atmfM4AlarmSevProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmfM4AlarmSevProfileIndex.setStatus("current")
_AtmfM4AlarmSevProfileRowStatus_Type = RowStatus
_AtmfM4AlarmSevProfileRowStatus_Object = MibTableColumn
atmfM4AlarmSevProfileRowStatus = _AtmfM4AlarmSevProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 36, 1, 2),
    _AtmfM4AlarmSevProfileRowStatus_Type()
)
atmfM4AlarmSevProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmfM4AlarmSevProfileRowStatus.setStatus("current")
_AtmfM4AlarmSevTable_Object = MibTable
atmfM4AlarmSevTable = _AtmfM4AlarmSevTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 37)
)
if mibBuilder.loadTexts:
    atmfM4AlarmSevTable.setStatus("current")
_AtmfM4AlarmSevEntry_Object = MibTableRow
atmfM4AlarmSevEntry = _AtmfM4AlarmSevEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 37, 1)
)
atmfM4AlarmSevEntry.setIndexNames(
    (0, "ATM-FORUM-M4-MIB", "atmfM4AlarmSevProfileIndex"),
    (0, "ATM-FORUM-M4-MIB", "atmfM4AlarmSevTrapId"),
)
if mibBuilder.loadTexts:
    atmfM4AlarmSevEntry.setStatus("current")
_AtmfM4AlarmSevTrapId_Type = Integer32
_AtmfM4AlarmSevTrapId_Object = MibTableColumn
atmfM4AlarmSevTrapId = _AtmfM4AlarmSevTrapId_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 37, 1, 1),
    _AtmfM4AlarmSevTrapId_Type()
)
atmfM4AlarmSevTrapId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmfM4AlarmSevTrapId.setStatus("current")
_AtmfM4AlarmSeverity_Type = AtmfM4AlarmSeverity
_AtmfM4AlarmSeverity_Object = MibTableColumn
atmfM4AlarmSeverity = _AtmfM4AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 37, 1, 2),
    _AtmfM4AlarmSeverity_Type()
)
atmfM4AlarmSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmfM4AlarmSeverity.setStatus("current")
_AtmfM4ForwardAllTraps_ObjectIdentity = ObjectIdentity
atmfM4ForwardAllTraps = _AtmfM4ForwardAllTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 38)
)
if mibBuilder.loadTexts:
    atmfM4ForwardAllTraps.setStatus("current")
_AtmfM4TrapForwardingTable_Object = MibTable
atmfM4TrapForwardingTable = _AtmfM4TrapForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 39)
)
if mibBuilder.loadTexts:
    atmfM4TrapForwardingTable.setStatus("current")
_AtmfM4TrapForwardingEntry_Object = MibTableRow
atmfM4TrapForwardingEntry = _AtmfM4TrapForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 39, 1)
)
atmfM4TrapForwardingEntry.setIndexNames(
    (0, "ATM-FORUM-M4-MIB", "atmfM4TrapForwardingIndex"),
)
if mibBuilder.loadTexts:
    atmfM4TrapForwardingEntry.setStatus("current")
_AtmfM4TrapForwardingIndex_Type = Integer32
_AtmfM4TrapForwardingIndex_Object = MibTableColumn
atmfM4TrapForwardingIndex = _AtmfM4TrapForwardingIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 39, 1, 1),
    _AtmfM4TrapForwardingIndex_Type()
)
atmfM4TrapForwardingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmfM4TrapForwardingIndex.setStatus("current")
_AtmfM4TrapForwardingDest_Type = IpAddress
_AtmfM4TrapForwardingDest_Object = MibTableColumn
atmfM4TrapForwardingDest = _AtmfM4TrapForwardingDest_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 39, 1, 2),
    _AtmfM4TrapForwardingDest_Type()
)
atmfM4TrapForwardingDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmfM4TrapForwardingDest.setStatus("current")
_AtmfM4ForwardedTrapId_Type = Integer32
_AtmfM4ForwardedTrapId_Object = MibTableColumn
atmfM4ForwardedTrapId = _AtmfM4ForwardedTrapId_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 39, 1, 3),
    _AtmfM4ForwardedTrapId_Type()
)
atmfM4ForwardedTrapId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmfM4ForwardedTrapId.setStatus("current")
_AtmfM4ForwardedTrapObject_Type = RowPointer
_AtmfM4ForwardedTrapObject_Object = MibTableColumn
atmfM4ForwardedTrapObject = _AtmfM4ForwardedTrapObject_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 39, 1, 4),
    _AtmfM4ForwardedTrapObject_Type()
)
atmfM4ForwardedTrapObject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmfM4ForwardedTrapObject.setStatus("current")


class _AtmfM4TrapForwardingPort_Type(Integer32):
    """Custom type atmfM4TrapForwardingPort based on Integer32"""
    defaultValue = 161


_AtmfM4TrapForwardingPort_Object = MibTableColumn
atmfM4TrapForwardingPort = _AtmfM4TrapForwardingPort_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 39, 1, 5),
    _AtmfM4TrapForwardingPort_Type()
)
atmfM4TrapForwardingPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmfM4TrapForwardingPort.setStatus("current")


class _AtmfM4LowestForwardedSeverity_Type(AtmfM4AlarmSeverity):
    """Custom type atmfM4LowestForwardedSeverity based on AtmfM4AlarmSeverity"""


_AtmfM4LowestForwardedSeverity_Object = MibTableColumn
atmfM4LowestForwardedSeverity = _AtmfM4LowestForwardedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 39, 1, 6),
    _AtmfM4LowestForwardedSeverity_Type()
)
atmfM4LowestForwardedSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmfM4LowestForwardedSeverity.setStatus("current")


class _AtmfM4ForwardedIndeterminate_Type(TruthValue):
    """Custom type atmfM4ForwardedIndeterminate based on TruthValue"""


_AtmfM4ForwardedIndeterminate_Object = MibTableColumn
atmfM4ForwardedIndeterminate = _AtmfM4ForwardedIndeterminate_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 39, 1, 7),
    _AtmfM4ForwardedIndeterminate_Type()
)
atmfM4ForwardedIndeterminate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmfM4ForwardedIndeterminate.setStatus("current")
_AtmfM4TrapForwardingRowStatus_Type = RowStatus
_AtmfM4TrapForwardingRowStatus_Object = MibTableColumn
atmfM4TrapForwardingRowStatus = _AtmfM4TrapForwardingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 39, 1, 8),
    _AtmfM4TrapForwardingRowStatus_Type()
)
atmfM4TrapForwardingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmfM4TrapForwardingRowStatus.setStatus("current")
_AtmfM4TrapLogTable_Object = MibTable
atmfM4TrapLogTable = _AtmfM4TrapLogTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 40)
)
if mibBuilder.loadTexts:
    atmfM4TrapLogTable.setStatus("current")
_AtmfM4TrapLogEntry_Object = MibTableRow
atmfM4TrapLogEntry = _AtmfM4TrapLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 40, 1)
)
atmfM4TrapLogEntry.setIndexNames(
    (0, "ATM-FORUM-M4-MIB", "atmfM4TrapLogSrc"),
    (0, "ATM-FORUM-M4-MIB", "atmfM4TrapLogType"),
)
if mibBuilder.loadTexts:
    atmfM4TrapLogEntry.setStatus("current")
_AtmfM4TrapLogSrc_Type = IpAddress
_AtmfM4TrapLogSrc_Object = MibTableColumn
atmfM4TrapLogSrc = _AtmfM4TrapLogSrc_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 40, 1, 1),
    _AtmfM4TrapLogSrc_Type()
)
atmfM4TrapLogSrc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmfM4TrapLogSrc.setStatus("current")


class _AtmfM4TrapLogType_Type(Integer32):
    """Custom type atmfM4TrapLogType based on Integer32"""
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
        *(("alarm", 5),
          ("configChange", 3),
          ("objectCreated", 1),
          ("objectDeleted", 2),
          ("stateChange", 4))
    )


_AtmfM4TrapLogType_Type.__name__ = "Integer32"
_AtmfM4TrapLogType_Object = MibTableColumn
atmfM4TrapLogType = _AtmfM4TrapLogType_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 40, 1, 2),
    _AtmfM4TrapLogType_Type()
)
atmfM4TrapLogType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmfM4TrapLogType.setStatus("current")


class _AtmfM4TrapLogAdminStatus_Type(Integer32):
    """Custom type atmfM4TrapLogAdminStatus based on Integer32"""
    defaultValue = 1

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


_AtmfM4TrapLogAdminStatus_Type.__name__ = "Integer32"
_AtmfM4TrapLogAdminStatus_Object = MibTableColumn
atmfM4TrapLogAdminStatus = _AtmfM4TrapLogAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 40, 1, 3),
    _AtmfM4TrapLogAdminStatus_Type()
)
atmfM4TrapLogAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmfM4TrapLogAdminStatus.setStatus("current")


class _AtmfM4TrapLogOperStatus_Type(Integer32):
    """Custom type atmfM4TrapLogOperStatus based on Integer32"""
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
        *(("down", 2),
          ("logFull", 3),
          ("up", 1))
    )


_AtmfM4TrapLogOperStatus_Type.__name__ = "Integer32"
_AtmfM4TrapLogOperStatus_Object = MibTableColumn
atmfM4TrapLogOperStatus = _AtmfM4TrapLogOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 40, 1, 4),
    _AtmfM4TrapLogOperStatus_Type()
)
atmfM4TrapLogOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4TrapLogOperStatus.setStatus("current")


class _AtmfM4TrapLogFullAction_Type(Integer32):
    """Custom type atmfM4TrapLogFullAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("halt", 1),
          ("wrap", 2))
    )


_AtmfM4TrapLogFullAction_Type.__name__ = "Integer32"
_AtmfM4TrapLogFullAction_Object = MibTableColumn
atmfM4TrapLogFullAction = _AtmfM4TrapLogFullAction_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 40, 1, 5),
    _AtmfM4TrapLogFullAction_Type()
)
atmfM4TrapLogFullAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmfM4TrapLogFullAction.setStatus("current")
_AtmfM4TrapLogRowStatus_Type = RowStatus
_AtmfM4TrapLogRowStatus_Object = MibTableColumn
atmfM4TrapLogRowStatus = _AtmfM4TrapLogRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 40, 1, 6),
    _AtmfM4TrapLogRowStatus_Type()
)
atmfM4TrapLogRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmfM4TrapLogRowStatus.setStatus("current")
_AtmfM4LoggedTrapTable_Object = MibTable
atmfM4LoggedTrapTable = _AtmfM4LoggedTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 41)
)
if mibBuilder.loadTexts:
    atmfM4LoggedTrapTable.setStatus("current")
_AtmfM4LoggedTrapEntry_Object = MibTableRow
atmfM4LoggedTrapEntry = _AtmfM4LoggedTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 41, 1)
)
atmfM4LoggedTrapEntry.setIndexNames(
    (0, "ATM-FORUM-M4-MIB", "atmfM4TrapLogSrc"),
    (0, "ATM-FORUM-M4-MIB", "atmfM4TrapLogType"),
    (0, "ATM-FORUM-M4-MIB", "atmfM4LoggedTrapIndex"),
)
if mibBuilder.loadTexts:
    atmfM4LoggedTrapEntry.setStatus("current")
_AtmfM4LoggedTrapIndex_Type = Unsigned32
_AtmfM4LoggedTrapIndex_Object = MibTableColumn
atmfM4LoggedTrapIndex = _AtmfM4LoggedTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 41, 1, 1),
    _AtmfM4LoggedTrapIndex_Type()
)
atmfM4LoggedTrapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmfM4LoggedTrapIndex.setStatus("current")
_AtmfM4LoggedTrapTime_Type = DateAndTime
_AtmfM4LoggedTrapTime_Object = MibTableColumn
atmfM4LoggedTrapTime = _AtmfM4LoggedTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 41, 1, 2),
    _AtmfM4LoggedTrapTime_Type()
)
atmfM4LoggedTrapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4LoggedTrapTime.setStatus("current")
_AtmfM4LoggedTrapID_Type = Integer32
_AtmfM4LoggedTrapID_Object = MibTableColumn
atmfM4LoggedTrapID = _AtmfM4LoggedTrapID_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 41, 1, 3),
    _AtmfM4LoggedTrapID_Type()
)
atmfM4LoggedTrapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4LoggedTrapID.setStatus("current")
_AtmfM4LoggedTrapObject_Type = RowPointer
_AtmfM4LoggedTrapObject_Object = MibTableColumn
atmfM4LoggedTrapObject = _AtmfM4LoggedTrapObject_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 41, 1, 4),
    _AtmfM4LoggedTrapObject_Type()
)
atmfM4LoggedTrapObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4LoggedTrapObject.setStatus("current")
_AtmfM4LoggedTrapRowStatus_Type = RowStatus
_AtmfM4LoggedTrapRowStatus_Object = MibTableColumn
atmfM4LoggedTrapRowStatus = _AtmfM4LoggedTrapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 41, 1, 5),
    _AtmfM4LoggedTrapRowStatus_Type()
)
atmfM4LoggedTrapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfM4LoggedTrapRowStatus.setStatus("current")
_AtmfM4LoggedAlarmTable_Object = MibTable
atmfM4LoggedAlarmTable = _AtmfM4LoggedAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 42)
)
if mibBuilder.loadTexts:
    atmfM4LoggedAlarmTable.setStatus("current")
_AtmfM4LoggedAlarmEntry_Object = MibTableRow
atmfM4LoggedAlarmEntry = _AtmfM4LoggedAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 42, 1)
)
atmfM4LoggedAlarmEntry.setIndexNames(
    (0, "ATM-FORUM-M4-MIB", "atmfM4TrapLogSrc"),
    (0, "ATM-FORUM-M4-MIB", "atmfM4TrapLogType"),
    (0, "ATM-FORUM-M4-MIB", "atmfM4LoggedTrapIndex"),
)
if mibBuilder.loadTexts:
    atmfM4LoggedAlarmEntry.setStatus("current")
_AtmfM4LoggedAlarmSeverity_Type = AtmfM4AlarmLogSeverity
_AtmfM4LoggedAlarmSeverity_Object = MibTableColumn
atmfM4LoggedAlarmSeverity = _AtmfM4LoggedAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 42, 1, 1),
    _AtmfM4LoggedAlarmSeverity_Type()
)
atmfM4LoggedAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4LoggedAlarmSeverity.setStatus("current")
_AtmfM4LoggedAlarmBackedUp_Type = TruthValue
_AtmfM4LoggedAlarmBackedUp_Object = MibTableColumn
atmfM4LoggedAlarmBackedUp = _AtmfM4LoggedAlarmBackedUp_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 42, 1, 2),
    _AtmfM4LoggedAlarmBackedUp_Type()
)
atmfM4LoggedAlarmBackedUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4LoggedAlarmBackedUp.setStatus("current")
_AtmfM4LoggedAlarmBUObject_Type = RowPointer
_AtmfM4LoggedAlarmBUObject_Object = MibTableColumn
atmfM4LoggedAlarmBUObject = _AtmfM4LoggedAlarmBUObject_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 42, 1, 3),
    _AtmfM4LoggedAlarmBUObject_Type()
)
atmfM4LoggedAlarmBUObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4LoggedAlarmBUObject.setStatus("current")
_AtmfM4LoggedAlarmSpecificProb_Type = DisplayString
_AtmfM4LoggedAlarmSpecificProb_Object = MibTableColumn
atmfM4LoggedAlarmSpecificProb = _AtmfM4LoggedAlarmSpecificProb_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 42, 1, 4),
    _AtmfM4LoggedAlarmSpecificProb_Type()
)
atmfM4LoggedAlarmSpecificProb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4LoggedAlarmSpecificProb.setStatus("current")
_AtmfM4LoggedAlarmRepairAct_Type = DisplayString
_AtmfM4LoggedAlarmRepairAct_Object = MibTableColumn
atmfM4LoggedAlarmRepairAct = _AtmfM4LoggedAlarmRepairAct_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 42, 1, 5),
    _AtmfM4LoggedAlarmRepairAct_Type()
)
atmfM4LoggedAlarmRepairAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfM4LoggedAlarmRepairAct.setStatus("current")
_AtmfM4TrapAlarmSeverity_Type = AtmfM4AlarmLogSeverity
_AtmfM4TrapAlarmSeverity_Object = MibScalar
atmfM4TrapAlarmSeverity = _AtmfM4TrapAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 43),
    _AtmfM4TrapAlarmSeverity_Type()
)
atmfM4TrapAlarmSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    atmfM4TrapAlarmSeverity.setStatus("current")
_AtmfM4TrapAlarmBackedUp_Type = TruthValue
_AtmfM4TrapAlarmBackedUp_Object = MibScalar
atmfM4TrapAlarmBackedUp = _AtmfM4TrapAlarmBackedUp_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 44),
    _AtmfM4TrapAlarmBackedUp_Type()
)
atmfM4TrapAlarmBackedUp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    atmfM4TrapAlarmBackedUp.setStatus("current")
_AtmfM4TrapAlarmBUObject_Type = RowPointer
_AtmfM4TrapAlarmBUObject_Object = MibScalar
atmfM4TrapAlarmBUObject = _AtmfM4TrapAlarmBUObject_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 45),
    _AtmfM4TrapAlarmBUObject_Type()
)
atmfM4TrapAlarmBUObject.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    atmfM4TrapAlarmBUObject.setStatus("current")
_AtmfM4TrapAlarmSpecificProb_Type = DisplayString
_AtmfM4TrapAlarmSpecificProb_Object = MibScalar
atmfM4TrapAlarmSpecificProb = _AtmfM4TrapAlarmSpecificProb_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 46),
    _AtmfM4TrapAlarmSpecificProb_Type()
)
atmfM4TrapAlarmSpecificProb.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    atmfM4TrapAlarmSpecificProb.setStatus("current")
_AtmfM4TrapAlarmRepairAct_Type = Unsigned32
_AtmfM4TrapAlarmRepairAct_Object = MibScalar
atmfM4TrapAlarmRepairAct = _AtmfM4TrapAlarmRepairAct_Object(
    (1, 3, 6, 1, 4, 1, 353, 100, 1, 47),
    _AtmfM4TrapAlarmRepairAct_Type()
)
atmfM4TrapAlarmRepairAct.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    atmfM4TrapAlarmRepairAct.setStatus("current")
_AtmfM4MIBTraps_ObjectIdentity = ObjectIdentity
atmfM4MIBTraps = _AtmfM4MIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 100, 2)
)
_AtmfM4MIBCompliance_ObjectIdentity = ObjectIdentity
atmfM4MIBCompliance = _AtmfM4MIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 100, 3)
)
_AtmfM4Groups_ObjectIdentity = ObjectIdentity
atmfM4Groups = _AtmfM4Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1)
)
_AtmfM4Compliances_ObjectIdentity = ObjectIdentity
atmfM4Compliances = _AtmfM4Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 2)
)
atmVplEntry.registerAugmentions(
    ("ATM-FORUM-M4-MIB",
     "atmfM4VplEntry")
)
atmfM4VplEntry.setIndexNames(*atmVplEntry.getIndexNames())
atmVclEntry.registerAugmentions(
    ("ATM-FORUM-M4-MIB",
     "atmfM4VclEntry")
)
atmfM4VclEntry.setIndexNames(*atmVclEntry.getIndexNames())
atmVpCrossConnectEntry.registerAugmentions(
    ("ATM-FORUM-M4-MIB",
     "atmfM4VpXConnEntry")
)
atmfM4VpXConnEntry.setIndexNames(*atmVpCrossConnectEntry.getIndexNames())
atmVcCrossConnectEntry.registerAugmentions(
    ("ATM-FORUM-M4-MIB",
     "atmfM4VcXConnEntry")
)
atmfM4VcXConnEntry.setIndexNames(*atmVcCrossConnectEntry.getIndexNames())

# Managed Objects groups

atmfM4General = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 1)
)
atmfM4General.setObjects(
      *(("ATM-FORUM-M4-MIB", "atmfM4NeVendor"),
        ("ATM-FORUM-M4-MIB", "atmfM4NeVersion"),
        ("ATM-FORUM-M4-MIB", "atmfM4NeStartTime"),
        ("ATM-FORUM-M4-MIB", "atmfM4NeAlarmSeverityIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4NeSuppressZeroStats"))
)
if mibBuilder.loadTexts:
    atmfM4General.setStatus("current")

atmfM4PhysPathTpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 2)
)
atmfM4PhysPathTpGroup.setObjects(
      *(("ATM-FORUM-M4-MIB", "atmfM4PhysPathTpHwUnitIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4PhysPathTpPortID"),
        ("ATM-FORUM-M4-MIB", "atmfM4PhysPathTpAlarmSeverityIndex"))
)
if mibBuilder.loadTexts:
    atmfM4PhysPathTpGroup.setStatus("current")

atmfM4TcAdaptorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 3)
)
atmfM4TcAdaptorGroup.setObjects(
      *(("ATM-FORUM-M4-MIB", "atmfM4TcACellScrambling"),
        ("ATM-FORUM-M4-MIB", "atmfM4TcAlarmSeverityIndex"))
)
if mibBuilder.loadTexts:
    atmfM4TcAdaptorGroup.setStatus("current")

atmfM4AtmLayerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 4)
)
atmfM4AtmLayerGroup.setObjects(
      *(("ATM-FORUM-M4-MIB", "atmfM4IfType"),
        ("ATM-FORUM-M4-MIB", "atmfM4IfLoopbackLocationCode"),
        ("ATM-FORUM-M4-MIB", "atmfM4IfSubscriberAddress"),
        ("ATM-FORUM-M4-MIB", "atmfM4IfPreferredCarrier"),
        ("ATM-FORUM-M4-MIB", "atmfM4IfFarEndCarrierNetwork"))
)
if mibBuilder.loadTexts:
    atmfM4AtmLayerGroup.setStatus("current")

atmfM4VplGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 5)
)
atmfM4VplGroup.setObjects(
    ("ATM-FORUM-M4-MIB", "atmfM4VplSegEndPt")
)
if mibBuilder.loadTexts:
    atmfM4VplGroup.setStatus("current")

atmfM4VclGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 6)
)
atmfM4VclGroup.setObjects(
    ("ATM-FORUM-M4-MIB", "atmfM4VclSegEndPt")
)
if mibBuilder.loadTexts:
    atmfM4VclGroup.setStatus("current")

atmfM4VpXConnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 7)
)
atmfM4VpXConnGroup.setObjects(
    ("ATM-FORUM-M4-MIB", "atmfM4VpXConnRecover")
)
if mibBuilder.loadTexts:
    atmfM4VpXConnGroup.setStatus("current")

atmfM4VcXConnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 8)
)
atmfM4VcXConnGroup.setObjects(
    ("ATM-FORUM-M4-MIB", "atmfM4VcXConnRecover")
)
if mibBuilder.loadTexts:
    atmfM4VcXConnGroup.setStatus("current")

atmfM4VpNextVpiGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 9)
)
atmfM4VpNextVpiGroup.setObjects(
    ("ATM-FORUM-M4-MIB", "atmfM4VpNextVpiValue")
)
if mibBuilder.loadTexts:
    atmfM4VpNextVpiGroup.setStatus("current")

atmfM4VcNextVciGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 10)
)
atmfM4VcNextVciGroup.setObjects(
    ("ATM-FORUM-M4-MIB", "atmfM4VcNextVciValue")
)
if mibBuilder.loadTexts:
    atmfM4VcNextVciGroup.setStatus("current")

atmfM4CellProtoCurrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 11)
)
atmfM4CellProtoCurrGroup.setObjects(
      *(("ATM-FORUM-M4-MIB", "atmfM4CellProtoCurrSuspect"),
        ("ATM-FORUM-M4-MIB", "atmfM4CellProtoCurrElapsedTime"),
        ("ATM-FORUM-M4-MIB", "atmfM4CellProtoCurrSupprIntvls"),
        ("ATM-FORUM-M4-MIB", "atmfM4CellProtoCurrProtoErrors"),
        ("ATM-FORUM-M4-MIB", "atmfM4CellProtoCurrInOAMCells"))
)
if mibBuilder.loadTexts:
    atmfM4CellProtoCurrGroup.setStatus("current")

atmfM4CellProtoHistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 12)
)
atmfM4CellProtoHistGroup.setObjects(
      *(("ATM-FORUM-M4-MIB", "atmfM4CellProtoHistSuspect"),
        ("ATM-FORUM-M4-MIB", "atmfM4CellProtoHistElapsedTime"),
        ("ATM-FORUM-M4-MIB", "atmfM4CellProtoHistSupprIntvls"),
        ("ATM-FORUM-M4-MIB", "atmfM4CellProtoHistProtoErrors"),
        ("ATM-FORUM-M4-MIB", "atmfM4CellProtoHistInOAMCells"))
)
if mibBuilder.loadTexts:
    atmfM4CellProtoHistGroup.setStatus("current")

atmfM4CellProtoErrorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 13)
)
atmfM4CellProtoErrorGroup.setObjects(
      *(("ATM-FORUM-M4-MIB", "atmfM4CellProtoErrorTime"),
        ("ATM-FORUM-M4-MIB", "atmfM4CellProtoErrorReason"),
        ("ATM-FORUM-M4-MIB", "atmfM4CellProtoErrorVpi"),
        ("ATM-FORUM-M4-MIB", "atmfM4CellProtoErrorVci"))
)
if mibBuilder.loadTexts:
    atmfM4CellProtoErrorGroup.setStatus("current")

atmfM4TcProtoCurrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 14)
)
atmfM4TcProtoCurrGroup.setObjects(
      *(("ATM-FORUM-M4-MIB", "atmfM4TcProtoCurrSuspect"),
        ("ATM-FORUM-M4-MIB", "atmfM4TcProtoCurrElapsedTime"),
        ("ATM-FORUM-M4-MIB", "atmfM4TcProtoCurrSupprIntvls"),
        ("ATM-FORUM-M4-MIB", "atmfM4TcProtoCurrDiscardHECViol"))
)
if mibBuilder.loadTexts:
    atmfM4TcProtoCurrGroup.setStatus("current")

atmfM4TcProtoHistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 15)
)
atmfM4TcProtoHistGroup.setObjects(
      *(("ATM-FORUM-M4-MIB", "atmfM4TcProtoHistSuspect"),
        ("ATM-FORUM-M4-MIB", "atmfM4TcProtoHistElapsedTime"),
        ("ATM-FORUM-M4-MIB", "atmfM4TcProtoHistSupprIntvls"),
        ("ATM-FORUM-M4-MIB", "atmfM4TcProtoHistDiscardHECViol"))
)
if mibBuilder.loadTexts:
    atmfM4TcProtoHistGroup.setStatus("current")

atmfM4VpUpcNpcCurrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 16)
)
atmfM4VpUpcNpcCurrGroup.setObjects(
      *(("ATM-FORUM-M4-MIB", "atmfM4VpUpcNpcCurrSuspect"),
        ("ATM-FORUM-M4-MIB", "atmfM4VpUpcNpcCurrElapsedTime"),
        ("ATM-FORUM-M4-MIB", "atmfM4VpUpcNpcCurrSupprIntvls"),
        ("ATM-FORUM-M4-MIB", "atmfM4VpUpcNpcCurrDiscardedCells"),
        ("ATM-FORUM-M4-MIB", "atmfM4VpUpcNpcCurrDiscardedClp0"),
        ("ATM-FORUM-M4-MIB", "atmfM4VpUpcNpcCurrPassedCells"),
        ("ATM-FORUM-M4-MIB", "atmfM4VpUpcNpcCurrPassedClp0"))
)
if mibBuilder.loadTexts:
    atmfM4VpUpcNpcCurrGroup.setStatus("current")

atmfM4VpUpcNpcHistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 17)
)
atmfM4VpUpcNpcHistGroup.setObjects(
      *(("ATM-FORUM-M4-MIB", "atmfM4VpUpcNpcHistSuspect"),
        ("ATM-FORUM-M4-MIB", "atmfM4VpUpcNpcHistElapsedTime"),
        ("ATM-FORUM-M4-MIB", "atmfM4VpUpcNpcHistSupprIntvls"),
        ("ATM-FORUM-M4-MIB", "atmfM4VpUpcNpcHistDiscardedCells"),
        ("ATM-FORUM-M4-MIB", "atmfM4VpUpcNpcHistDiscardedClp0"),
        ("ATM-FORUM-M4-MIB", "atmfM4VpUpcNpcHistPassedCells"),
        ("ATM-FORUM-M4-MIB", "atmfM4VpUpcNpcHistPassedClp0"))
)
if mibBuilder.loadTexts:
    atmfM4VpUpcNpcHistGroup.setStatus("current")

atmfM4VcUpcNpcCurrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 18)
)
atmfM4VcUpcNpcCurrGroup.setObjects(
      *(("ATM-FORUM-M4-MIB", "atmfM4VcUpcNpcCurrSuspect"),
        ("ATM-FORUM-M4-MIB", "atmfM4VcUpcNpcCurrElapsedTime"),
        ("ATM-FORUM-M4-MIB", "atmfM4VcUpcNpcCurrSupprIntvls"),
        ("ATM-FORUM-M4-MIB", "atmfM4VcUpcNpcCurrDiscardedCells"),
        ("ATM-FORUM-M4-MIB", "atmfM4VcUpcNpcCurrDiscardedClp0"),
        ("ATM-FORUM-M4-MIB", "atmfM4VcUpcNpcCurrPassedCells"),
        ("ATM-FORUM-M4-MIB", "atmfM4VcUpcNpcCurrPassedClp0"))
)
if mibBuilder.loadTexts:
    atmfM4VcUpcNpcCurrGroup.setStatus("current")

atmfM4VcUpcNpcHistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 19)
)
atmfM4VcUpcNpcHistGroup.setObjects(
      *(("ATM-FORUM-M4-MIB", "atmfM4VcUpcNpcHistSuspect"),
        ("ATM-FORUM-M4-MIB", "atmfM4VcUpcNpcHistElapsedTime"),
        ("ATM-FORUM-M4-MIB", "atmfM4VcUpcNpcHistSupprIntvls"),
        ("ATM-FORUM-M4-MIB", "atmfM4VcUpcNpcHistDiscardedCells"),
        ("ATM-FORUM-M4-MIB", "atmfM4VcUpcNpcHistDiscardedClp0"),
        ("ATM-FORUM-M4-MIB", "atmfM4VcUpcNpcHistPassedCells"),
        ("ATM-FORUM-M4-MIB", "atmfM4VcUpcNpcHistPassedClp0"))
)
if mibBuilder.loadTexts:
    atmfM4VcUpcNpcHistGroup.setStatus("current")

atmfM4VpTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 20)
)
atmfM4VpTestGroup.setObjects(
      *(("ATM-FORUM-M4-MIB", "atmfM4VpTestId"),
        ("ATM-FORUM-M4-MIB", "atmfM4VpTestStatus"),
        ("ATM-FORUM-M4-MIB", "atmfM4VpTestType"),
        ("ATM-FORUM-M4-MIB", "atmfM4VpTestResult"),
        ("ATM-FORUM-M4-MIB", "atmfM4VpTestCode"),
        ("ATM-FORUM-M4-MIB", "atmfM4VpTestOwner"))
)
if mibBuilder.loadTexts:
    atmfM4VpTestGroup.setStatus("current")

atmfM4VcTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 21)
)
atmfM4VcTestGroup.setObjects(
      *(("ATM-FORUM-M4-MIB", "atmfM4VcTestId"),
        ("ATM-FORUM-M4-MIB", "atmfM4VcTestStatus"),
        ("ATM-FORUM-M4-MIB", "atmfM4VcTestType"),
        ("ATM-FORUM-M4-MIB", "atmfM4VcTestResult"),
        ("ATM-FORUM-M4-MIB", "atmfM4VcTestCode"),
        ("ATM-FORUM-M4-MIB", "atmfM4VcTestOwner"))
)
if mibBuilder.loadTexts:
    atmfM4VcTestGroup.setStatus("current")

atmfM4EquipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 22)
)
atmfM4EquipGroup.setObjects(
      *(("ATM-FORUM-M4-MIB", "atmfM4EquipAdminStatus"),
        ("ATM-FORUM-M4-MIB", "atmfM4EquipLocation"),
        ("ATM-FORUM-M4-MIB", "atmfM4EquipOperStatus"),
        ("ATM-FORUM-M4-MIB", "atmfM4EquipVendor"),
        ("ATM-FORUM-M4-MIB", "atmfM4EquipVersion"),
        ("ATM-FORUM-M4-MIB", "atmfM4EquipUserLabel"),
        ("ATM-FORUM-M4-MIB", "atmfM4EquipAlarmSeverityIndex"))
)
if mibBuilder.loadTexts:
    atmfM4EquipGroup.setStatus("current")

atmfM4EquipHolderGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 23)
)
atmfM4EquipHolderGroup.setObjects(
      *(("ATM-FORUM-M4-MIB", "atmfM4EquipHolderType"),
        ("ATM-FORUM-M4-MIB", "atmfM4EquipHolderAcceptableTypes"),
        ("ATM-FORUM-M4-MIB", "atmfM4EquipHolderSlotStatus"),
        ("ATM-FORUM-M4-MIB", "atmfM4EquipHolderSwLoad"))
)
if mibBuilder.loadTexts:
    atmfM4EquipHolderGroup.setStatus("current")

atmfM4PlugInUnitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 24)
)
atmfM4PlugInUnitGroup.setObjects(
      *(("ATM-FORUM-M4-MIB", "atmfM4PlugInUnitAdminStatus"),
        ("ATM-FORUM-M4-MIB", "atmfM4PlugInUnitAvailStatus"),
        ("ATM-FORUM-M4-MIB", "atmfM4PlugInUnitOperStatus"),
        ("ATM-FORUM-M4-MIB", "atmfM4PlugInUnitVendor"),
        ("ATM-FORUM-M4-MIB", "atmfM4PlugInUnitVersion"),
        ("ATM-FORUM-M4-MIB", "atmfM4PlugInUnitAlarmSeverityIndex"))
)
if mibBuilder.loadTexts:
    atmfM4PlugInUnitGroup.setStatus("current")

atmfM4HwRunningSwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 25)
)
atmfM4HwRunningSwGroup.setObjects(
    ("ATM-FORUM-M4-MIB", "atmfM4HwRunningSwSwIndex")
)
if mibBuilder.loadTexts:
    atmfM4HwRunningSwGroup.setStatus("current")

atmfM4HwInstalledSwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 26)
)
atmfM4HwInstalledSwGroup.setObjects(
      *(("ATM-FORUM-M4-MIB", "atmfM4HwInstalledSwSwIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4HwSwAlarmSeverityIndex"))
)
if mibBuilder.loadTexts:
    atmfM4HwInstalledSwGroup.setStatus("current")

atmfM4AlarmSevGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 27)
)
atmfM4AlarmSevGroup.setObjects(
      *(("ATM-FORUM-M4-MIB", "atmfM4AlarmSevProfileRowStatus"),
        ("ATM-FORUM-M4-MIB", "atmfM4AlarmSeverity"),
        ("ATM-FORUM-M4-MIB", "atmfM4AlarmSevDefault"),
        ("ATM-FORUM-M4-MIB", "atmfM4AlarmSevProfileIndexNext"))
)
if mibBuilder.loadTexts:
    atmfM4AlarmSevGroup.setStatus("current")

atmfM4TrapForwardingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 28)
)
atmfM4TrapForwardingGroup.setObjects(
      *(("ATM-FORUM-M4-MIB", "atmfM4TrapForwardingDest"),
        ("ATM-FORUM-M4-MIB", "atmfM4ForwardedTrapId"),
        ("ATM-FORUM-M4-MIB", "atmfM4ForwardedTrapObject"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapForwardingPort"),
        ("ATM-FORUM-M4-MIB", "atmfM4LowestForwardedSeverity"),
        ("ATM-FORUM-M4-MIB", "atmfM4ForwardedIndeterminate"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapForwardingRowStatus"))
)
if mibBuilder.loadTexts:
    atmfM4TrapForwardingGroup.setStatus("current")

atmfM4TrapLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 29)
)
atmfM4TrapLogGroup.setObjects(
      *(("ATM-FORUM-M4-MIB", "atmfM4TrapLogAdminStatus"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapLogOperStatus"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapLogFullAction"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapLogRowStatus"))
)
if mibBuilder.loadTexts:
    atmfM4TrapLogGroup.setStatus("current")

atmfM4LoggedTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 30)
)
atmfM4LoggedTrapGroup.setObjects(
      *(("ATM-FORUM-M4-MIB", "atmfM4LoggedTrapTime"),
        ("ATM-FORUM-M4-MIB", "atmfM4LoggedTrapID"),
        ("ATM-FORUM-M4-MIB", "atmfM4LoggedTrapObject"),
        ("ATM-FORUM-M4-MIB", "atmfM4LoggedTrapRowStatus"))
)
if mibBuilder.loadTexts:
    atmfM4LoggedTrapGroup.setStatus("current")

atmfM4LoggedAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 1, 31)
)
atmfM4LoggedAlarmGroup.setObjects(
      *(("ATM-FORUM-M4-MIB", "atmfM4LoggedAlarmSeverity"),
        ("ATM-FORUM-M4-MIB", "atmfM4LoggedAlarmBackedUp"),
        ("ATM-FORUM-M4-MIB", "atmfM4LoggedAlarmBUObject"),
        ("ATM-FORUM-M4-MIB", "atmfM4LoggedAlarmSpecificProb"),
        ("ATM-FORUM-M4-MIB", "atmfM4LoggedAlarmRepairAct"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmBackedUp"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmBUObject"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSpecificProb"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmRepairAct"))
)
if mibBuilder.loadTexts:
    atmfM4LoggedAlarmGroup.setStatus("current")


# Notification objects

atmfM4IfAisAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 100, 2, 1)
)
atmfM4IfAisAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    atmfM4IfAisAlarm.setStatus(
        "current"
    )

atmfM4IfLcdAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 100, 2, 2)
)
atmfM4IfLcdAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    atmfM4IfLcdAlarm.setStatus(
        "current"
    )

atmfM4IfLofAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 100, 2, 3)
)
atmfM4IfLofAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    atmfM4IfLofAlarm.setStatus(
        "current"
    )

atmfM4IfLopAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 100, 2, 4)
)
atmfM4IfLopAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    atmfM4IfLopAlarm.setStatus(
        "current"
    )

atmfM4IfLosAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 100, 2, 5)
)
atmfM4IfLosAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    atmfM4IfLosAlarm.setStatus(
        "current"
    )

atmfM4IfPayloadMismatchAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 100, 2, 6)
)
atmfM4IfPayloadMismatchAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    atmfM4IfPayloadMismatchAlarm.setStatus(
        "current"
    )

atmfM4IfXmissionErrAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 100, 2, 7)
)
atmfM4IfXmissionErrAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    atmfM4IfXmissionErrAlarm.setStatus(
        "current"
    )

atmfM4IfPathTraceMismatchAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 100, 2, 8)
)
atmfM4IfPathTraceMismatchAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    atmfM4IfPathTraceMismatchAlarm.setStatus(
        "current"
    )

atmfM4IfRdiAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 100, 2, 9)
)
atmfM4IfRdiAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    atmfM4IfRdiAlarm.setStatus(
        "current"
    )

atmfM4IfSignalLabelMismatchAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 100, 2, 10)
)
atmfM4IfSignalLabelMismatchAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    atmfM4IfSignalLabelMismatchAlarm.setStatus(
        "current"
    )

atmfM4HwLineCardAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 100, 2, 23)
)
atmfM4HwLineCardAlarm.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    atmfM4HwLineCardAlarm.setStatus(
        "current"
    )

atmfM4HwPowerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 100, 2, 25)
)
atmfM4HwPowerAlarm.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    atmfM4HwPowerAlarm.setStatus(
        "current"
    )

atmfM4HwPIUnitMissingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 100, 2, 29)
)
atmfM4HwPIUnitMissingAlarm.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    atmfM4HwPIUnitMissingAlarm.setStatus(
        "current"
    )

atmfM4HwPIUnitProbAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 100, 2, 30)
)
atmfM4HwPIUnitProbAlarm.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    atmfM4HwPIUnitProbAlarm.setStatus(
        "current"
    )

atmfM4HwPIUnitMismatchAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 100, 2, 31)
)
atmfM4HwPIUnitMismatchAlarm.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    atmfM4HwPIUnitMismatchAlarm.setStatus(
        "current"
    )

atmfM4HwTimingProbAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 100, 2, 32)
)
atmfM4HwTimingProbAlarm.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    atmfM4HwTimingProbAlarm.setStatus(
        "current"
    )

atmfM4HwSwDownloadFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 100, 2, 39)
)
atmfM4HwSwDownloadFailAlarm.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    atmfM4HwSwDownloadFailAlarm.setStatus(
        "current"
    )

atmfM4HwVersionMismatchAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 100, 2, 40)
)
atmfM4HwVersionMismatchAlarm.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    atmfM4HwVersionMismatchAlarm.setStatus(
        "current"
    )

atmfM4HwFanFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 100, 2, 41)
)
atmfM4HwFanFailAlarm.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    atmfM4HwFanFailAlarm.setStatus(
        "current"
    )

atmfM4HwHighTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 100, 2, 44)
)
atmfM4HwHighTempAlarm.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    atmfM4HwHighTempAlarm.setStatus(
        "current"
    )

atmfM4SwVersionMismatchAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 100, 2, 45)
)
atmfM4SwVersionMismatchAlarm.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4HwInstalledSwIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    atmfM4SwVersionMismatchAlarm.setStatus(
        "current"
    )

atmfM4HwUnitUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 100, 2, 54)
)
atmfM4HwUnitUp.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    atmfM4HwUnitUp.setStatus(
        "current"
    )

atmfM4HwUnitDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 100, 2, 55)
)
atmfM4HwUnitDown.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    atmfM4HwUnitDown.setStatus(
        "current"
    )

atmfM4AtmCellIfCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 100, 2, 56)
)
atmfM4AtmCellIfCreated.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4IfType"))
)
if mibBuilder.loadTexts:
    atmfM4AtmCellIfCreated.setStatus(
        "current"
    )

atmfM4AtmCellIfDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 100, 2, 57)
)
atmfM4AtmCellIfDeleted.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    atmfM4AtmCellIfDeleted.setStatus(
        "current"
    )

atmfM4HwUnitCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 100, 2, 66)
)
atmfM4HwUnitCreated.setObjects(
      *(("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalParentRelPos"),
        ("ENTITY-MIB", "entPhysicalClass"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    atmfM4HwUnitCreated.setStatus(
        "current"
    )

atmfM4HwUnitDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 100, 2, 67)
)
atmfM4HwUnitDeleted.setObjects(
      *(("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalParentRelPos"),
        ("ENTITY-MIB", "entPhysicalClass"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    atmfM4HwUnitDeleted.setStatus(
        "current"
    )

atmfM4IfChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 100, 2, 70)
)
atmfM4IfChanged.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    atmfM4IfChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

atmfM4Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 353, 100, 3, 2, 1)
)
if mibBuilder.loadTexts:
    atmfM4Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATM-FORUM-M4-MIB",
    **{"AtmfM4AlarmLogSeverity": AtmfM4AlarmLogSeverity,
       "AtmfM4AlarmSeverity": AtmfM4AlarmSeverity,
       "atmfM4MIB": atmfM4MIB,
       "atmfM4MIBObjects": atmfM4MIBObjects,
       "atmfM4NeVendor": atmfM4NeVendor,
       "atmfM4NeVersion": atmfM4NeVersion,
       "atmfM4NeStartTime": atmfM4NeStartTime,
       "atmfM4NeAlarmSeverityIndex": atmfM4NeAlarmSeverityIndex,
       "atmfM4NeSuppressZeroStats": atmfM4NeSuppressZeroStats,
       "atmfM4PhysPathTpTable": atmfM4PhysPathTpTable,
       "atmfM4PhysPathTpEntry": atmfM4PhysPathTpEntry,
       "atmfM4PhysPathTpHwUnitIndex": atmfM4PhysPathTpHwUnitIndex,
       "atmfM4PhysPathTpPortID": atmfM4PhysPathTpPortID,
       "atmfM4PhysPathTpAlarmSeverityIndex": atmfM4PhysPathTpAlarmSeverityIndex,
       "atmfM4TcAdaptorTable": atmfM4TcAdaptorTable,
       "atmfM4TcAdaptorEntry": atmfM4TcAdaptorEntry,
       "atmfM4TcACellScrambling": atmfM4TcACellScrambling,
       "atmfM4TcAlarmSeverityIndex": atmfM4TcAlarmSeverityIndex,
       "atmfM4AtmLayerTable": atmfM4AtmLayerTable,
       "atmfM4AtmLayerEntry": atmfM4AtmLayerEntry,
       "atmfM4IfType": atmfM4IfType,
       "atmfM4IfLoopbackLocationCode": atmfM4IfLoopbackLocationCode,
       "atmfM4IfSubscriberAddress": atmfM4IfSubscriberAddress,
       "atmfM4IfPreferredCarrier": atmfM4IfPreferredCarrier,
       "atmfM4IfFarEndCarrierNetwork": atmfM4IfFarEndCarrierNetwork,
       "atmfM4VplTable": atmfM4VplTable,
       "atmfM4VplEntry": atmfM4VplEntry,
       "atmfM4VplSegEndPt": atmfM4VplSegEndPt,
       "atmfM4VclTable": atmfM4VclTable,
       "atmfM4VclEntry": atmfM4VclEntry,
       "atmfM4VclSegEndPt": atmfM4VclSegEndPt,
       "atmfM4VpXConnTable": atmfM4VpXConnTable,
       "atmfM4VpXConnEntry": atmfM4VpXConnEntry,
       "atmfM4VpXConnRecover": atmfM4VpXConnRecover,
       "atmfM4VcXConnTable": atmfM4VcXConnTable,
       "atmfM4VcXConnEntry": atmfM4VcXConnEntry,
       "atmfM4VcXConnRecover": atmfM4VcXConnRecover,
       "atmfM4VpNextVpiTable": atmfM4VpNextVpiTable,
       "atmfM4VpNextVpiEntry": atmfM4VpNextVpiEntry,
       "atmfM4VpNextVpiValue": atmfM4VpNextVpiValue,
       "atmfM4VcNextVciTable": atmfM4VcNextVciTable,
       "atmfM4VcNextVciEntry": atmfM4VcNextVciEntry,
       "atmfM4VcNextVciValue": atmfM4VcNextVciValue,
       "atmfM4CellProtoCurrTable": atmfM4CellProtoCurrTable,
       "atmfM4CellProtoCurrEntry": atmfM4CellProtoCurrEntry,
       "atmfM4CellProtoCurrSuspect": atmfM4CellProtoCurrSuspect,
       "atmfM4CellProtoCurrElapsedTime": atmfM4CellProtoCurrElapsedTime,
       "atmfM4CellProtoCurrSupprIntvls": atmfM4CellProtoCurrSupprIntvls,
       "atmfM4CellProtoCurrProtoErrors": atmfM4CellProtoCurrProtoErrors,
       "atmfM4CellProtoCurrInOAMCells": atmfM4CellProtoCurrInOAMCells,
       "atmfM4CellProtoHistTable": atmfM4CellProtoHistTable,
       "atmfM4CellProtoHistEntry": atmfM4CellProtoHistEntry,
       "atmfM4CellProtoHistIndex": atmfM4CellProtoHistIndex,
       "atmfM4CellProtoHistSuspect": atmfM4CellProtoHistSuspect,
       "atmfM4CellProtoHistElapsedTime": atmfM4CellProtoHistElapsedTime,
       "atmfM4CellProtoHistSupprIntvls": atmfM4CellProtoHistSupprIntvls,
       "atmfM4CellProtoHistProtoErrors": atmfM4CellProtoHistProtoErrors,
       "atmfM4CellProtoHistInOAMCells": atmfM4CellProtoHistInOAMCells,
       "atmfM4CellProtoErrorTable": atmfM4CellProtoErrorTable,
       "atmfM4CellProtoErrorEntry": atmfM4CellProtoErrorEntry,
       "atmfM4CellProtoErrorCode": atmfM4CellProtoErrorCode,
       "atmfM4CellProtoErrorTime": atmfM4CellProtoErrorTime,
       "atmfM4CellProtoErrorReason": atmfM4CellProtoErrorReason,
       "atmfM4CellProtoErrorVpi": atmfM4CellProtoErrorVpi,
       "atmfM4CellProtoErrorVci": atmfM4CellProtoErrorVci,
       "atmfM4TcProtoCurrTable": atmfM4TcProtoCurrTable,
       "atmfM4TcProtoCurrEntry": atmfM4TcProtoCurrEntry,
       "atmfM4TcProtoCurrSuspect": atmfM4TcProtoCurrSuspect,
       "atmfM4TcProtoCurrElapsedTime": atmfM4TcProtoCurrElapsedTime,
       "atmfM4TcProtoCurrSupprIntvls": atmfM4TcProtoCurrSupprIntvls,
       "atmfM4TcProtoCurrDiscardHECViol": atmfM4TcProtoCurrDiscardHECViol,
       "atmfM4TcProtoHistTable": atmfM4TcProtoHistTable,
       "atmfM4TcProtoHistEntry": atmfM4TcProtoHistEntry,
       "atmfM4TcProtoHistIndex": atmfM4TcProtoHistIndex,
       "atmfM4TcProtoHistSuspect": atmfM4TcProtoHistSuspect,
       "atmfM4TcProtoHistElapsedTime": atmfM4TcProtoHistElapsedTime,
       "atmfM4TcProtoHistSupprIntvls": atmfM4TcProtoHistSupprIntvls,
       "atmfM4TcProtoHistDiscardHECViol": atmfM4TcProtoHistDiscardHECViol,
       "atmfM4VpUpcNpcCurrTable": atmfM4VpUpcNpcCurrTable,
       "atmfM4VpUpcNpcCurrEntry": atmfM4VpUpcNpcCurrEntry,
       "atmfM4VpUpcNpcCurrSuspect": atmfM4VpUpcNpcCurrSuspect,
       "atmfM4VpUpcNpcCurrElapsedTime": atmfM4VpUpcNpcCurrElapsedTime,
       "atmfM4VpUpcNpcCurrSupprIntvls": atmfM4VpUpcNpcCurrSupprIntvls,
       "atmfM4VpUpcNpcCurrDiscardedCells": atmfM4VpUpcNpcCurrDiscardedCells,
       "atmfM4VpUpcNpcCurrDiscardedClp0": atmfM4VpUpcNpcCurrDiscardedClp0,
       "atmfM4VpUpcNpcCurrPassedCells": atmfM4VpUpcNpcCurrPassedCells,
       "atmfM4VpUpcNpcCurrPassedClp0": atmfM4VpUpcNpcCurrPassedClp0,
       "atmfM4VpUpcNpcHistTable": atmfM4VpUpcNpcHistTable,
       "atmfM4VpUpcNpcHistEntry": atmfM4VpUpcNpcHistEntry,
       "atmfM4VpUpcNpcHistIndex": atmfM4VpUpcNpcHistIndex,
       "atmfM4VpUpcNpcHistSuspect": atmfM4VpUpcNpcHistSuspect,
       "atmfM4VpUpcNpcHistElapsedTime": atmfM4VpUpcNpcHistElapsedTime,
       "atmfM4VpUpcNpcHistSupprIntvls": atmfM4VpUpcNpcHistSupprIntvls,
       "atmfM4VpUpcNpcHistDiscardedCells": atmfM4VpUpcNpcHistDiscardedCells,
       "atmfM4VpUpcNpcHistDiscardedClp0": atmfM4VpUpcNpcHistDiscardedClp0,
       "atmfM4VpUpcNpcHistPassedCells": atmfM4VpUpcNpcHistPassedCells,
       "atmfM4VpUpcNpcHistPassedClp0": atmfM4VpUpcNpcHistPassedClp0,
       "atmfM4VcUpcNpcCurrTable": atmfM4VcUpcNpcCurrTable,
       "atmfM4VcUpcNpcCurrEntry": atmfM4VcUpcNpcCurrEntry,
       "atmfM4VcUpcNpcCurrSuspect": atmfM4VcUpcNpcCurrSuspect,
       "atmfM4VcUpcNpcCurrElapsedTime": atmfM4VcUpcNpcCurrElapsedTime,
       "atmfM4VcUpcNpcCurrSupprIntvls": atmfM4VcUpcNpcCurrSupprIntvls,
       "atmfM4VcUpcNpcCurrDiscardedCells": atmfM4VcUpcNpcCurrDiscardedCells,
       "atmfM4VcUpcNpcCurrDiscardedClp0": atmfM4VcUpcNpcCurrDiscardedClp0,
       "atmfM4VcUpcNpcCurrPassedCells": atmfM4VcUpcNpcCurrPassedCells,
       "atmfM4VcUpcNpcCurrPassedClp0": atmfM4VcUpcNpcCurrPassedClp0,
       "atmfM4VcUpcNpcHistTable": atmfM4VcUpcNpcHistTable,
       "atmfM4VcUpcNpcHistEntry": atmfM4VcUpcNpcHistEntry,
       "atmfM4VcUpcNpcHistIndex": atmfM4VcUpcNpcHistIndex,
       "atmfM4VcUpcNpcHistSuspect": atmfM4VcUpcNpcHistSuspect,
       "atmfM4VcUpcNpcHistElapsedTime": atmfM4VcUpcNpcHistElapsedTime,
       "atmfM4VcUpcNpcHistSupprIntvls": atmfM4VcUpcNpcHistSupprIntvls,
       "atmfM4VcUpcNpcHistDiscardedCells": atmfM4VcUpcNpcHistDiscardedCells,
       "atmfM4VcUpcNpcHistDiscardedClp0": atmfM4VcUpcNpcHistDiscardedClp0,
       "atmfM4VcUpcNpcHistPassedCells": atmfM4VcUpcNpcHistPassedCells,
       "atmfM4VcUpcNpcHistPassedClp0": atmfM4VcUpcNpcHistPassedClp0,
       "atmfM4TestTypes": atmfM4TestTypes,
       "atmfM4TestOAMLoopbackSeg": atmfM4TestOAMLoopbackSeg,
       "atmfM4TestOAMLoopbackE2E": atmfM4TestOAMLoopbackE2E,
       "atmfM4VpTestTable": atmfM4VpTestTable,
       "atmfM4VpTestEntry": atmfM4VpTestEntry,
       "atmfM4VpTestObject": atmfM4VpTestObject,
       "atmfM4VpTestId": atmfM4VpTestId,
       "atmfM4VpTestStatus": atmfM4VpTestStatus,
       "atmfM4VpTestType": atmfM4VpTestType,
       "atmfM4VpTestResult": atmfM4VpTestResult,
       "atmfM4VpTestCode": atmfM4VpTestCode,
       "atmfM4VpTestOwner": atmfM4VpTestOwner,
       "atmfM4VcTestTable": atmfM4VcTestTable,
       "atmfM4VcTestEntry": atmfM4VcTestEntry,
       "atmfM4VcTestObject": atmfM4VcTestObject,
       "atmfM4VcTestId": atmfM4VcTestId,
       "atmfM4VcTestStatus": atmfM4VcTestStatus,
       "atmfM4VcTestType": atmfM4VcTestType,
       "atmfM4VcTestResult": atmfM4VcTestResult,
       "atmfM4VcTestCode": atmfM4VcTestCode,
       "atmfM4VcTestOwner": atmfM4VcTestOwner,
       "atmfM4EquipTable": atmfM4EquipTable,
       "atmfM4EquipEntry": atmfM4EquipEntry,
       "atmfM4EquipAdminStatus": atmfM4EquipAdminStatus,
       "atmfM4EquipLocation": atmfM4EquipLocation,
       "atmfM4EquipOperStatus": atmfM4EquipOperStatus,
       "atmfM4EquipVendor": atmfM4EquipVendor,
       "atmfM4EquipVersion": atmfM4EquipVersion,
       "atmfM4EquipUserLabel": atmfM4EquipUserLabel,
       "atmfM4EquipAlarmSeverityIndex": atmfM4EquipAlarmSeverityIndex,
       "atmfM4EquipHolderTable": atmfM4EquipHolderTable,
       "atmfM4EquipHolderEntry": atmfM4EquipHolderEntry,
       "atmfM4EquipHolderType": atmfM4EquipHolderType,
       "atmfM4EquipHolderAcceptableTypes": atmfM4EquipHolderAcceptableTypes,
       "atmfM4EquipHolderSlotStatus": atmfM4EquipHolderSlotStatus,
       "atmfM4EquipHolderSwLoad": atmfM4EquipHolderSwLoad,
       "atmfM4PlugInUnitTable": atmfM4PlugInUnitTable,
       "atmfM4PlugInUnitEntry": atmfM4PlugInUnitEntry,
       "atmfM4PlugInUnitAdminStatus": atmfM4PlugInUnitAdminStatus,
       "atmfM4PlugInUnitAvailStatus": atmfM4PlugInUnitAvailStatus,
       "atmfM4PlugInUnitOperStatus": atmfM4PlugInUnitOperStatus,
       "atmfM4PlugInUnitVendor": atmfM4PlugInUnitVendor,
       "atmfM4PlugInUnitVersion": atmfM4PlugInUnitVersion,
       "atmfM4PlugInUnitAlarmSeverityIndex": atmfM4PlugInUnitAlarmSeverityIndex,
       "atmfM4HwRunningSwTable": atmfM4HwRunningSwTable,
       "atmfM4HwRunningSwEntry": atmfM4HwRunningSwEntry,
       "atmfM4HwRunningSwHwIndex": atmfM4HwRunningSwHwIndex,
       "atmfM4HwRunningSwIndex": atmfM4HwRunningSwIndex,
       "atmfM4HwRunningSwSwIndex": atmfM4HwRunningSwSwIndex,
       "atmfM4HwInstalledSwTable": atmfM4HwInstalledSwTable,
       "atmfM4HwInstalledSwEntry": atmfM4HwInstalledSwEntry,
       "atmfM4HwInstalledSwHwIndex": atmfM4HwInstalledSwHwIndex,
       "atmfM4HwInstalledSwIndex": atmfM4HwInstalledSwIndex,
       "atmfM4HwInstalledSwSwIndex": atmfM4HwInstalledSwSwIndex,
       "atmfM4HwSwAlarmSeverityIndex": atmfM4HwSwAlarmSeverityIndex,
       "atmfM4AlarmSevDefault": atmfM4AlarmSevDefault,
       "atmfM4AlarmSevProfileIndexNext": atmfM4AlarmSevProfileIndexNext,
       "atmfM4AlarmSevProfileTable": atmfM4AlarmSevProfileTable,
       "atmfM4AlarmSevProfileEntry": atmfM4AlarmSevProfileEntry,
       "atmfM4AlarmSevProfileIndex": atmfM4AlarmSevProfileIndex,
       "atmfM4AlarmSevProfileRowStatus": atmfM4AlarmSevProfileRowStatus,
       "atmfM4AlarmSevTable": atmfM4AlarmSevTable,
       "atmfM4AlarmSevEntry": atmfM4AlarmSevEntry,
       "atmfM4AlarmSevTrapId": atmfM4AlarmSevTrapId,
       "atmfM4AlarmSeverity": atmfM4AlarmSeverity,
       "atmfM4ForwardAllTraps": atmfM4ForwardAllTraps,
       "atmfM4TrapForwardingTable": atmfM4TrapForwardingTable,
       "atmfM4TrapForwardingEntry": atmfM4TrapForwardingEntry,
       "atmfM4TrapForwardingIndex": atmfM4TrapForwardingIndex,
       "atmfM4TrapForwardingDest": atmfM4TrapForwardingDest,
       "atmfM4ForwardedTrapId": atmfM4ForwardedTrapId,
       "atmfM4ForwardedTrapObject": atmfM4ForwardedTrapObject,
       "atmfM4TrapForwardingPort": atmfM4TrapForwardingPort,
       "atmfM4LowestForwardedSeverity": atmfM4LowestForwardedSeverity,
       "atmfM4ForwardedIndeterminate": atmfM4ForwardedIndeterminate,
       "atmfM4TrapForwardingRowStatus": atmfM4TrapForwardingRowStatus,
       "atmfM4TrapLogTable": atmfM4TrapLogTable,
       "atmfM4TrapLogEntry": atmfM4TrapLogEntry,
       "atmfM4TrapLogSrc": atmfM4TrapLogSrc,
       "atmfM4TrapLogType": atmfM4TrapLogType,
       "atmfM4TrapLogAdminStatus": atmfM4TrapLogAdminStatus,
       "atmfM4TrapLogOperStatus": atmfM4TrapLogOperStatus,
       "atmfM4TrapLogFullAction": atmfM4TrapLogFullAction,
       "atmfM4TrapLogRowStatus": atmfM4TrapLogRowStatus,
       "atmfM4LoggedTrapTable": atmfM4LoggedTrapTable,
       "atmfM4LoggedTrapEntry": atmfM4LoggedTrapEntry,
       "atmfM4LoggedTrapIndex": atmfM4LoggedTrapIndex,
       "atmfM4LoggedTrapTime": atmfM4LoggedTrapTime,
       "atmfM4LoggedTrapID": atmfM4LoggedTrapID,
       "atmfM4LoggedTrapObject": atmfM4LoggedTrapObject,
       "atmfM4LoggedTrapRowStatus": atmfM4LoggedTrapRowStatus,
       "atmfM4LoggedAlarmTable": atmfM4LoggedAlarmTable,
       "atmfM4LoggedAlarmEntry": atmfM4LoggedAlarmEntry,
       "atmfM4LoggedAlarmSeverity": atmfM4LoggedAlarmSeverity,
       "atmfM4LoggedAlarmBackedUp": atmfM4LoggedAlarmBackedUp,
       "atmfM4LoggedAlarmBUObject": atmfM4LoggedAlarmBUObject,
       "atmfM4LoggedAlarmSpecificProb": atmfM4LoggedAlarmSpecificProb,
       "atmfM4LoggedAlarmRepairAct": atmfM4LoggedAlarmRepairAct,
       "atmfM4TrapAlarmSeverity": atmfM4TrapAlarmSeverity,
       "atmfM4TrapAlarmBackedUp": atmfM4TrapAlarmBackedUp,
       "atmfM4TrapAlarmBUObject": atmfM4TrapAlarmBUObject,
       "atmfM4TrapAlarmSpecificProb": atmfM4TrapAlarmSpecificProb,
       "atmfM4TrapAlarmRepairAct": atmfM4TrapAlarmRepairAct,
       "atmfM4MIBTraps": atmfM4MIBTraps,
       "atmfM4IfAisAlarm": atmfM4IfAisAlarm,
       "atmfM4IfLcdAlarm": atmfM4IfLcdAlarm,
       "atmfM4IfLofAlarm": atmfM4IfLofAlarm,
       "atmfM4IfLopAlarm": atmfM4IfLopAlarm,
       "atmfM4IfLosAlarm": atmfM4IfLosAlarm,
       "atmfM4IfPayloadMismatchAlarm": atmfM4IfPayloadMismatchAlarm,
       "atmfM4IfXmissionErrAlarm": atmfM4IfXmissionErrAlarm,
       "atmfM4IfPathTraceMismatchAlarm": atmfM4IfPathTraceMismatchAlarm,
       "atmfM4IfRdiAlarm": atmfM4IfRdiAlarm,
       "atmfM4IfSignalLabelMismatchAlarm": atmfM4IfSignalLabelMismatchAlarm,
       "atmfM4HwLineCardAlarm": atmfM4HwLineCardAlarm,
       "atmfM4HwPowerAlarm": atmfM4HwPowerAlarm,
       "atmfM4HwPIUnitMissingAlarm": atmfM4HwPIUnitMissingAlarm,
       "atmfM4HwPIUnitProbAlarm": atmfM4HwPIUnitProbAlarm,
       "atmfM4HwPIUnitMismatchAlarm": atmfM4HwPIUnitMismatchAlarm,
       "atmfM4HwTimingProbAlarm": atmfM4HwTimingProbAlarm,
       "atmfM4HwSwDownloadFailAlarm": atmfM4HwSwDownloadFailAlarm,
       "atmfM4HwVersionMismatchAlarm": atmfM4HwVersionMismatchAlarm,
       "atmfM4HwFanFailAlarm": atmfM4HwFanFailAlarm,
       "atmfM4HwHighTempAlarm": atmfM4HwHighTempAlarm,
       "atmfM4SwVersionMismatchAlarm": atmfM4SwVersionMismatchAlarm,
       "atmfM4HwUnitUp": atmfM4HwUnitUp,
       "atmfM4HwUnitDown": atmfM4HwUnitDown,
       "atmfM4AtmCellIfCreated": atmfM4AtmCellIfCreated,
       "atmfM4AtmCellIfDeleted": atmfM4AtmCellIfDeleted,
       "atmfM4HwUnitCreated": atmfM4HwUnitCreated,
       "atmfM4HwUnitDeleted": atmfM4HwUnitDeleted,
       "atmfM4IfChanged": atmfM4IfChanged,
       "atmfM4MIBCompliance": atmfM4MIBCompliance,
       "atmfM4Groups": atmfM4Groups,
       "atmfM4General": atmfM4General,
       "atmfM4PhysPathTpGroup": atmfM4PhysPathTpGroup,
       "atmfM4TcAdaptorGroup": atmfM4TcAdaptorGroup,
       "atmfM4AtmLayerGroup": atmfM4AtmLayerGroup,
       "atmfM4VplGroup": atmfM4VplGroup,
       "atmfM4VclGroup": atmfM4VclGroup,
       "atmfM4VpXConnGroup": atmfM4VpXConnGroup,
       "atmfM4VcXConnGroup": atmfM4VcXConnGroup,
       "atmfM4VpNextVpiGroup": atmfM4VpNextVpiGroup,
       "atmfM4VcNextVciGroup": atmfM4VcNextVciGroup,
       "atmfM4CellProtoCurrGroup": atmfM4CellProtoCurrGroup,
       "atmfM4CellProtoHistGroup": atmfM4CellProtoHistGroup,
       "atmfM4CellProtoErrorGroup": atmfM4CellProtoErrorGroup,
       "atmfM4TcProtoCurrGroup": atmfM4TcProtoCurrGroup,
       "atmfM4TcProtoHistGroup": atmfM4TcProtoHistGroup,
       "atmfM4VpUpcNpcCurrGroup": atmfM4VpUpcNpcCurrGroup,
       "atmfM4VpUpcNpcHistGroup": atmfM4VpUpcNpcHistGroup,
       "atmfM4VcUpcNpcCurrGroup": atmfM4VcUpcNpcCurrGroup,
       "atmfM4VcUpcNpcHistGroup": atmfM4VcUpcNpcHistGroup,
       "atmfM4VpTestGroup": atmfM4VpTestGroup,
       "atmfM4VcTestGroup": atmfM4VcTestGroup,
       "atmfM4EquipGroup": atmfM4EquipGroup,
       "atmfM4EquipHolderGroup": atmfM4EquipHolderGroup,
       "atmfM4PlugInUnitGroup": atmfM4PlugInUnitGroup,
       "atmfM4HwRunningSwGroup": atmfM4HwRunningSwGroup,
       "atmfM4HwInstalledSwGroup": atmfM4HwInstalledSwGroup,
       "atmfM4AlarmSevGroup": atmfM4AlarmSevGroup,
       "atmfM4TrapForwardingGroup": atmfM4TrapForwardingGroup,
       "atmfM4TrapLogGroup": atmfM4TrapLogGroup,
       "atmfM4LoggedTrapGroup": atmfM4LoggedTrapGroup,
       "atmfM4LoggedAlarmGroup": atmfM4LoggedAlarmGroup,
       "atmfM4Compliances": atmfM4Compliances,
       "atmfM4Compliance": atmfM4Compliance}
)
