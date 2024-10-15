# SNMP MIB module (RH-ATT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RH-ATT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:34 2024
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

_Att_2_ObjectIdentity = ObjectIdentity
att_2 = _Att_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74)
)
_Att_products_ObjectIdentity = ObjectIdentity
att_products = _Att_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 1)
)
_Att_rh1products_ObjectIdentity = ObjectIdentity
att_rh1products = _Att_rh1products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 1, 6)
)
_Att_rh1xe_ObjectIdentity = ObjectIdentity
att_rh1xe = _Att_rh1xe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 1, 6, 1)
)
_Att_mgmt_ObjectIdentity = ObjectIdentity
att_mgmt = _Att_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2)
)
_Att_rh1mgt_ObjectIdentity = ObjectIdentity
att_rh1mgt = _Att_rh1mgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 14)
)
_Rh1BasicCtrlCapability_ObjectIdentity = ObjectIdentity
rh1BasicCtrlCapability = _Rh1BasicCtrlCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 1)
)
_Rh1BasicCtrlRackMAC_Type = OctetString
_Rh1BasicCtrlRackMAC_Object = MibScalar
rh1BasicCtrlRackMAC = _Rh1BasicCtrlRackMAC_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 1, 1),
    _Rh1BasicCtrlRackMAC_Type()
)
rh1BasicCtrlRackMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1BasicCtrlRackMAC.setStatus("mandatory")
_Rh1BasicCtrlCardCapacity_Type = Integer32
_Rh1BasicCtrlCardCapacity_Object = MibScalar
rh1BasicCtrlCardCapacity = _Rh1BasicCtrlCardCapacity_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 1, 2),
    _Rh1BasicCtrlCardCapacity_Type()
)
rh1BasicCtrlCardCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1BasicCtrlCardCapacity.setStatus("mandatory")
_Rh1BasicCtrlCardTable_Object = MibTable
rh1BasicCtrlCardTable = _Rh1BasicCtrlCardTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 1, 3)
)
if mibBuilder.loadTexts:
    rh1BasicCtrlCardTable.setStatus("mandatory")
_Rh1BasicCtrlCardEntry_Object = MibTableRow
rh1BasicCtrlCardEntry = _Rh1BasicCtrlCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 1, 3, 1)
)
rh1BasicCtrlCardEntry.setIndexNames(
    (0, "RH-ATT-MIB", "rh1BasicCtrlCardID"),
)
if mibBuilder.loadTexts:
    rh1BasicCtrlCardEntry.setStatus("mandatory")
_Rh1BasicCtrlCardID_Type = Integer32
_Rh1BasicCtrlCardID_Object = MibTableColumn
rh1BasicCtrlCardID = _Rh1BasicCtrlCardID_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 1, 3, 1, 1),
    _Rh1BasicCtrlCardID_Type()
)
rh1BasicCtrlCardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1BasicCtrlCardID.setStatus("mandatory")
_Rh1BasicCtrlNumberOfPorts_Type = Integer32
_Rh1BasicCtrlNumberOfPorts_Object = MibTableColumn
rh1BasicCtrlNumberOfPorts = _Rh1BasicCtrlNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 1, 3, 1, 2),
    _Rh1BasicCtrlNumberOfPorts_Type()
)
rh1BasicCtrlNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1BasicCtrlNumberOfPorts.setStatus("mandatory")
_Rh1BasicCtrlPortTable_Object = MibTable
rh1BasicCtrlPortTable = _Rh1BasicCtrlPortTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 1, 4)
)
if mibBuilder.loadTexts:
    rh1BasicCtrlPortTable.setStatus("mandatory")
_Rh1BasicCtrlPortEntry_Object = MibTableRow
rh1BasicCtrlPortEntry = _Rh1BasicCtrlPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 1, 4, 1)
)
rh1BasicCtrlPortEntry.setIndexNames(
    (0, "RH-ATT-MIB", "rh1BasicPortCtrlCardID"),
    (0, "RH-ATT-MIB", "rh1BasicCtrlPortID"),
)
if mibBuilder.loadTexts:
    rh1BasicCtrlPortEntry.setStatus("mandatory")
_Rh1BasicPortCtrlCardID_Type = Integer32
_Rh1BasicPortCtrlCardID_Object = MibTableColumn
rh1BasicPortCtrlCardID = _Rh1BasicPortCtrlCardID_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 1, 4, 1, 1),
    _Rh1BasicPortCtrlCardID_Type()
)
rh1BasicPortCtrlCardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1BasicPortCtrlCardID.setStatus("mandatory")
_Rh1BasicCtrlPortID_Type = Integer32
_Rh1BasicCtrlPortID_Object = MibTableColumn
rh1BasicCtrlPortID = _Rh1BasicCtrlPortID_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 1, 4, 1, 2),
    _Rh1BasicCtrlPortID_Type()
)
rh1BasicCtrlPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1BasicCtrlPortID.setStatus("mandatory")


class _Rh1BasicCtrlPortType_Type(Integer32):
    """Custom type rh1BasicCtrlPortType based on Integer32"""
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
        *(("other", 1),
          ("repeater", 2),
          ("tenBASE-F-Async", 3),
          ("tenBASE-F-Synch", 4))
    )


_Rh1BasicCtrlPortType_Type.__name__ = "Integer32"
_Rh1BasicCtrlPortType_Object = MibTableColumn
rh1BasicCtrlPortType = _Rh1BasicCtrlPortType_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 1, 4, 1, 3),
    _Rh1BasicCtrlPortType_Type()
)
rh1BasicCtrlPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1BasicCtrlPortType.setStatus("mandatory")


class _Rh1BasicCtrlPortCtrl_Type(Integer32):
    """Custom type rh1BasicCtrlPortCtrl based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_Rh1BasicCtrlPortCtrl_Type.__name__ = "Integer32"
_Rh1BasicCtrlPortCtrl_Object = MibTableColumn
rh1BasicCtrlPortCtrl = _Rh1BasicCtrlPortCtrl_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 1, 4, 1, 4),
    _Rh1BasicCtrlPortCtrl_Type()
)
rh1BasicCtrlPortCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1BasicCtrlPortCtrl.setStatus("mandatory")


class _Rh1BasicCtrlAutoPartitionState_Type(Integer32):
    """Custom type rh1BasicCtrlAutoPartitionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto-partitioned", 3),
          ("not-auto-partitioned", 2),
          ("other", 1))
    )


_Rh1BasicCtrlAutoPartitionState_Type.__name__ = "Integer32"
_Rh1BasicCtrlAutoPartitionState_Object = MibTableColumn
rh1BasicCtrlAutoPartitionState = _Rh1BasicCtrlAutoPartitionState_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 1, 4, 1, 5),
    _Rh1BasicCtrlAutoPartitionState_Type()
)
rh1BasicCtrlAutoPartitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1BasicCtrlAutoPartitionState.setStatus("mandatory")
_Rh1SelfTestCapability_ObjectIdentity = ObjectIdentity
rh1SelfTestCapability = _Rh1SelfTestCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 2)
)


class _Rh1SelfTestResetRack_Type(Integer32):
    """Custom type rh1SelfTestResetRack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-reset", 1),
          ("reset", 2))
    )


_Rh1SelfTestResetRack_Type.__name__ = "Integer32"
_Rh1SelfTestResetRack_Object = MibScalar
rh1SelfTestResetRack = _Rh1SelfTestResetRack_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 2, 1),
    _Rh1SelfTestResetRack_Type()
)
rh1SelfTestResetRack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1SelfTestResetRack.setStatus("mandatory")


class _Rh1SelfTestExecuteSelfTest1_Type(Integer32):
    """Custom type rh1SelfTestExecuteSelfTest1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-test", 1),
          ("test", 2))
    )


_Rh1SelfTestExecuteSelfTest1_Type.__name__ = "Integer32"
_Rh1SelfTestExecuteSelfTest1_Object = MibScalar
rh1SelfTestExecuteSelfTest1 = _Rh1SelfTestExecuteSelfTest1_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 2, 2),
    _Rh1SelfTestExecuteSelfTest1_Type()
)
rh1SelfTestExecuteSelfTest1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1SelfTestExecuteSelfTest1.setStatus("mandatory")


class _Rh1SelfTestExecuteSelfTest2_Type(Integer32):
    """Custom type rh1SelfTestExecuteSelfTest2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-test", 1),
          ("test", 2))
    )


_Rh1SelfTestExecuteSelfTest2_Type.__name__ = "Integer32"
_Rh1SelfTestExecuteSelfTest2_Object = MibScalar
rh1SelfTestExecuteSelfTest2 = _Rh1SelfTestExecuteSelfTest2_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 2, 3),
    _Rh1SelfTestExecuteSelfTest2_Type()
)
rh1SelfTestExecuteSelfTest2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1SelfTestExecuteSelfTest2.setStatus("mandatory")


class _Rh1SelfTestRackHealthState_Type(Integer32):
    """Custom type rh1SelfTestRackHealthState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 3),
          ("ok", 2),
          ("other", 1))
    )


_Rh1SelfTestRackHealthState_Type.__name__ = "Integer32"
_Rh1SelfTestRackHealthState_Object = MibScalar
rh1SelfTestRackHealthState = _Rh1SelfTestRackHealthState_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 2, 4),
    _Rh1SelfTestRackHealthState_Type()
)
rh1SelfTestRackHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1SelfTestRackHealthState.setStatus("mandatory")
_Rh1SelfTestRackHealthData_Type = OctetString
_Rh1SelfTestRackHealthData_Object = MibScalar
rh1SelfTestRackHealthData = _Rh1SelfTestRackHealthData_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 2, 5),
    _Rh1SelfTestRackHealthData_Type()
)
rh1SelfTestRackHealthData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1SelfTestRackHealthData.setStatus("mandatory")
_Rh1SelfTestCardTable_Object = MibTable
rh1SelfTestCardTable = _Rh1SelfTestCardTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 2, 6)
)
if mibBuilder.loadTexts:
    rh1SelfTestCardTable.setStatus("mandatory")
_Rh1SelfTestCardEntry_Object = MibTableRow
rh1SelfTestCardEntry = _Rh1SelfTestCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 2, 6, 1)
)
rh1SelfTestCardEntry.setIndexNames(
    (0, "RH-ATT-MIB", "rh1SelfTestCardID"),
)
if mibBuilder.loadTexts:
    rh1SelfTestCardEntry.setStatus("mandatory")
_Rh1SelfTestCardID_Type = Integer32
_Rh1SelfTestCardID_Object = MibTableColumn
rh1SelfTestCardID = _Rh1SelfTestCardID_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 2, 6, 1, 1),
    _Rh1SelfTestCardID_Type()
)
rh1SelfTestCardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1SelfTestCardID.setStatus("mandatory")
_Rh1SelfTestCardResetTimeStamp_Type = TimeTicks
_Rh1SelfTestCardResetTimeStamp_Object = MibTableColumn
rh1SelfTestCardResetTimeStamp = _Rh1SelfTestCardResetTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 2, 6, 1, 2),
    _Rh1SelfTestCardResetTimeStamp_Type()
)
rh1SelfTestCardResetTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1SelfTestCardResetTimeStamp.setStatus("mandatory")


class _Rh1SelfTestResetCard_Type(Integer32):
    """Custom type rh1SelfTestResetCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-reset", 1),
          ("reset", 2))
    )


_Rh1SelfTestResetCard_Type.__name__ = "Integer32"
_Rh1SelfTestResetCard_Object = MibTableColumn
rh1SelfTestResetCard = _Rh1SelfTestResetCard_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 2, 6, 1, 3),
    _Rh1SelfTestResetCard_Type()
)
rh1SelfTestResetCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1SelfTestResetCard.setStatus("mandatory")


class _Rh1SelfTestResetMPR_Type(Integer32):
    """Custom type rh1SelfTestResetMPR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-reset", 1),
          ("reset", 2))
    )


_Rh1SelfTestResetMPR_Type.__name__ = "Integer32"
_Rh1SelfTestResetMPR_Object = MibTableColumn
rh1SelfTestResetMPR = _Rh1SelfTestResetMPR_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 2, 6, 1, 4),
    _Rh1SelfTestResetMPR_Type()
)
rh1SelfTestResetMPR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1SelfTestResetMPR.setStatus("mandatory")


class _Rh1SelfTestExecuteCardSelfTest1_Type(Integer32):
    """Custom type rh1SelfTestExecuteCardSelfTest1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-test", 1),
          ("test", 2))
    )


_Rh1SelfTestExecuteCardSelfTest1_Type.__name__ = "Integer32"
_Rh1SelfTestExecuteCardSelfTest1_Object = MibTableColumn
rh1SelfTestExecuteCardSelfTest1 = _Rh1SelfTestExecuteCardSelfTest1_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 2, 6, 1, 5),
    _Rh1SelfTestExecuteCardSelfTest1_Type()
)
rh1SelfTestExecuteCardSelfTest1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1SelfTestExecuteCardSelfTest1.setStatus("mandatory")


class _Rh1SelfTestExecuteCardSelfTest2_Type(Integer32):
    """Custom type rh1SelfTestExecuteCardSelfTest2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-test", 1),
          ("test", 2))
    )


_Rh1SelfTestExecuteCardSelfTest2_Type.__name__ = "Integer32"
_Rh1SelfTestExecuteCardSelfTest2_Object = MibTableColumn
rh1SelfTestExecuteCardSelfTest2 = _Rh1SelfTestExecuteCardSelfTest2_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 2, 6, 1, 6),
    _Rh1SelfTestExecuteCardSelfTest2_Type()
)
rh1SelfTestExecuteCardSelfTest2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1SelfTestExecuteCardSelfTest2.setStatus("mandatory")


class _Rh1SelfTestCardHealthState_Type(Integer32):
    """Custom type rh1SelfTestCardHealthState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 3),
          ("ok", 2),
          ("other", 1))
    )


_Rh1SelfTestCardHealthState_Type.__name__ = "Integer32"
_Rh1SelfTestCardHealthState_Object = MibTableColumn
rh1SelfTestCardHealthState = _Rh1SelfTestCardHealthState_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 2, 6, 1, 7),
    _Rh1SelfTestCardHealthState_Type()
)
rh1SelfTestCardHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1SelfTestCardHealthState.setStatus("mandatory")
_Rh1SelfTestCardHealthData_Type = OctetString
_Rh1SelfTestCardHealthData_Object = MibTableColumn
rh1SelfTestCardHealthData = _Rh1SelfTestCardHealthData_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 2, 6, 1, 8),
    _Rh1SelfTestCardHealthData_Type()
)
rh1SelfTestCardHealthData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1SelfTestCardHealthData.setStatus("mandatory")
_Rh1PerfMonCapability_ObjectIdentity = ObjectIdentity
rh1PerfMonCapability = _Rh1PerfMonCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3)
)
_Rh1PerfMonSegmentTable_Object = MibTable
rh1PerfMonSegmentTable = _Rh1PerfMonSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 1)
)
if mibBuilder.loadTexts:
    rh1PerfMonSegmentTable.setStatus("mandatory")
_Rh1PerfMonSegmentEntry_Object = MibTableRow
rh1PerfMonSegmentEntry = _Rh1PerfMonSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 1, 1)
)
rh1PerfMonSegmentEntry.setIndexNames(
    (0, "RH-ATT-MIB", "rh1PerfMonSegmentID"),
)
if mibBuilder.loadTexts:
    rh1PerfMonSegmentEntry.setStatus("mandatory")
_Rh1PerfMonSegmentID_Type = Integer32
_Rh1PerfMonSegmentID_Object = MibTableColumn
rh1PerfMonSegmentID = _Rh1PerfMonSegmentID_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 1, 1, 1),
    _Rh1PerfMonSegmentID_Type()
)
rh1PerfMonSegmentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonSegmentID.setStatus("mandatory")
_Rh1PerfMonSegFrameSize1Bound_Type = Integer32
_Rh1PerfMonSegFrameSize1Bound_Object = MibTableColumn
rh1PerfMonSegFrameSize1Bound = _Rh1PerfMonSegFrameSize1Bound_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 1, 1, 2),
    _Rh1PerfMonSegFrameSize1Bound_Type()
)
rh1PerfMonSegFrameSize1Bound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1PerfMonSegFrameSize1Bound.setStatus("mandatory")
_Rh1PerfMonSegFrameSize2Bound_Type = Integer32
_Rh1PerfMonSegFrameSize2Bound_Object = MibTableColumn
rh1PerfMonSegFrameSize2Bound = _Rh1PerfMonSegFrameSize2Bound_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 1, 1, 3),
    _Rh1PerfMonSegFrameSize2Bound_Type()
)
rh1PerfMonSegFrameSize2Bound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1PerfMonSegFrameSize2Bound.setStatus("mandatory")
_Rh1PerfMonSegFrameSize3Bound_Type = Integer32
_Rh1PerfMonSegFrameSize3Bound_Object = MibTableColumn
rh1PerfMonSegFrameSize3Bound = _Rh1PerfMonSegFrameSize3Bound_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 1, 1, 4),
    _Rh1PerfMonSegFrameSize3Bound_Type()
)
rh1PerfMonSegFrameSize3Bound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1PerfMonSegFrameSize3Bound.setStatus("mandatory")
_Rh1PerfMonSegFrameSize4Bound_Type = Integer32
_Rh1PerfMonSegFrameSize4Bound_Object = MibTableColumn
rh1PerfMonSegFrameSize4Bound = _Rh1PerfMonSegFrameSize4Bound_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 1, 1, 5),
    _Rh1PerfMonSegFrameSize4Bound_Type()
)
rh1PerfMonSegFrameSize4Bound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1PerfMonSegFrameSize4Bound.setStatus("mandatory")
_Rh1PerfMonSegTotalFramesProcessedOk_Type = Counter32
_Rh1PerfMonSegTotalFramesProcessedOk_Object = MibTableColumn
rh1PerfMonSegTotalFramesProcessedOk = _Rh1PerfMonSegTotalFramesProcessedOk_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 1, 1, 6),
    _Rh1PerfMonSegTotalFramesProcessedOk_Type()
)
rh1PerfMonSegTotalFramesProcessedOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonSegTotalFramesProcessedOk.setStatus("mandatory")
_Rh1PerfMonSegTotalOctetsProcessedOk_Type = Counter32
_Rh1PerfMonSegTotalOctetsProcessedOk_Object = MibTableColumn
rh1PerfMonSegTotalOctetsProcessedOk = _Rh1PerfMonSegTotalOctetsProcessedOk_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 1, 1, 7),
    _Rh1PerfMonSegTotalOctetsProcessedOk_Type()
)
rh1PerfMonSegTotalOctetsProcessedOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonSegTotalOctetsProcessedOk.setStatus("mandatory")
_Rh1PerfMonSegTotalCollisions_Type = Counter32
_Rh1PerfMonSegTotalCollisions_Object = MibTableColumn
rh1PerfMonSegTotalCollisions = _Rh1PerfMonSegTotalCollisions_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 1, 1, 8),
    _Rh1PerfMonSegTotalCollisions_Type()
)
rh1PerfMonSegTotalCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonSegTotalCollisions.setStatus("mandatory")
_Rh1PerfMonSegTotalLateCollisions_Type = Counter32
_Rh1PerfMonSegTotalLateCollisions_Object = MibTableColumn
rh1PerfMonSegTotalLateCollisions = _Rh1PerfMonSegTotalLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 1, 1, 9),
    _Rh1PerfMonSegTotalLateCollisions_Type()
)
rh1PerfMonSegTotalLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonSegTotalLateCollisions.setStatus("mandatory")
_Rh1PerfMonSegTotalRunts_Type = Counter32
_Rh1PerfMonSegTotalRunts_Object = MibTableColumn
rh1PerfMonSegTotalRunts = _Rh1PerfMonSegTotalRunts_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 1, 1, 10),
    _Rh1PerfMonSegTotalRunts_Type()
)
rh1PerfMonSegTotalRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonSegTotalRunts.setStatus("mandatory")
_Rh1PerfMonSegTotalShortEvents_Type = Counter32
_Rh1PerfMonSegTotalShortEvents_Object = MibTableColumn
rh1PerfMonSegTotalShortEvents = _Rh1PerfMonSegTotalShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 1, 1, 11),
    _Rh1PerfMonSegTotalShortEvents_Type()
)
rh1PerfMonSegTotalShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonSegTotalShortEvents.setStatus("mandatory")
_Rh1PerfMonSegTotalFrameTooLongs_Type = Counter32
_Rh1PerfMonSegTotalFrameTooLongs_Object = MibTableColumn
rh1PerfMonSegTotalFrameTooLongs = _Rh1PerfMonSegTotalFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 1, 1, 12),
    _Rh1PerfMonSegTotalFrameTooLongs_Type()
)
rh1PerfMonSegTotalFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonSegTotalFrameTooLongs.setStatus("mandatory")
_Rh1PerfMonSegTotalAutoPartitions_Type = Counter32
_Rh1PerfMonSegTotalAutoPartitions_Object = MibTableColumn
rh1PerfMonSegTotalAutoPartitions = _Rh1PerfMonSegTotalAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 1, 1, 13),
    _Rh1PerfMonSegTotalAutoPartitions_Type()
)
rh1PerfMonSegTotalAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonSegTotalAutoPartitions.setStatus("mandatory")
_Rh1PerfMonSegTotalLongFragments_Type = Counter32
_Rh1PerfMonSegTotalLongFragments_Object = MibTableColumn
rh1PerfMonSegTotalLongFragments = _Rh1PerfMonSegTotalLongFragments_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 1, 1, 14),
    _Rh1PerfMonSegTotalLongFragments_Type()
)
rh1PerfMonSegTotalLongFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonSegTotalLongFragments.setStatus("mandatory")
_Rh1PerfMonSegTotalFifoErrors_Type = Counter32
_Rh1PerfMonSegTotalFifoErrors_Object = MibTableColumn
rh1PerfMonSegTotalFifoErrors = _Rh1PerfMonSegTotalFifoErrors_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 1, 1, 15),
    _Rh1PerfMonSegTotalFifoErrors_Type()
)
rh1PerfMonSegTotalFifoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonSegTotalFifoErrors.setStatus("mandatory")
_Rh1PerfMonSegTotalErrorEnergy_Type = Counter32
_Rh1PerfMonSegTotalErrorEnergy_Object = MibTableColumn
rh1PerfMonSegTotalErrorEnergy = _Rh1PerfMonSegTotalErrorEnergy_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 1, 1, 16),
    _Rh1PerfMonSegTotalErrorEnergy_Type()
)
rh1PerfMonSegTotalErrorEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonSegTotalErrorEnergy.setStatus("mandatory")
_Rh1PerfMonSegTotalNondataEnergy_Type = Counter32
_Rh1PerfMonSegTotalNondataEnergy_Object = MibTableColumn
rh1PerfMonSegTotalNondataEnergy = _Rh1PerfMonSegTotalNondataEnergy_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 1, 1, 17),
    _Rh1PerfMonSegTotalNondataEnergy_Type()
)
rh1PerfMonSegTotalNondataEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonSegTotalNondataEnergy.setStatus("mandatory")
_Rh1PerfMonSegTotalManchesterViolations_Type = Counter32
_Rh1PerfMonSegTotalManchesterViolations_Object = MibTableColumn
rh1PerfMonSegTotalManchesterViolations = _Rh1PerfMonSegTotalManchesterViolations_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 1, 1, 18),
    _Rh1PerfMonSegTotalManchesterViolations_Type()
)
rh1PerfMonSegTotalManchesterViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonSegTotalManchesterViolations.setStatus("mandatory")
_Rh1PerfMonSegTotalBand1Frames_Type = Counter32
_Rh1PerfMonSegTotalBand1Frames_Object = MibTableColumn
rh1PerfMonSegTotalBand1Frames = _Rh1PerfMonSegTotalBand1Frames_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 1, 1, 19),
    _Rh1PerfMonSegTotalBand1Frames_Type()
)
rh1PerfMonSegTotalBand1Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonSegTotalBand1Frames.setStatus("mandatory")
_Rh1PerfMonSegTotalBand2Frames_Type = Counter32
_Rh1PerfMonSegTotalBand2Frames_Object = MibTableColumn
rh1PerfMonSegTotalBand2Frames = _Rh1PerfMonSegTotalBand2Frames_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 1, 1, 20),
    _Rh1PerfMonSegTotalBand2Frames_Type()
)
rh1PerfMonSegTotalBand2Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonSegTotalBand2Frames.setStatus("mandatory")
_Rh1PerfMonSegTotalBand3Frames_Type = Counter32
_Rh1PerfMonSegTotalBand3Frames_Object = MibTableColumn
rh1PerfMonSegTotalBand3Frames = _Rh1PerfMonSegTotalBand3Frames_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 1, 1, 21),
    _Rh1PerfMonSegTotalBand3Frames_Type()
)
rh1PerfMonSegTotalBand3Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonSegTotalBand3Frames.setStatus("mandatory")
_Rh1PerfMonSegTotalBand4Frames_Type = Counter32
_Rh1PerfMonSegTotalBand4Frames_Object = MibTableColumn
rh1PerfMonSegTotalBand4Frames = _Rh1PerfMonSegTotalBand4Frames_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 1, 1, 22),
    _Rh1PerfMonSegTotalBand4Frames_Type()
)
rh1PerfMonSegTotalBand4Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonSegTotalBand4Frames.setStatus("mandatory")
_Rh1PerfMonSegTotalBand5Frames_Type = Counter32
_Rh1PerfMonSegTotalBand5Frames_Object = MibTableColumn
rh1PerfMonSegTotalBand5Frames = _Rh1PerfMonSegTotalBand5Frames_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 1, 1, 23),
    _Rh1PerfMonSegTotalBand5Frames_Type()
)
rh1PerfMonSegTotalBand5Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonSegTotalBand5Frames.setStatus("mandatory")
_Rh1PerfMonSegCounts_Type = OctetString
_Rh1PerfMonSegCounts_Object = MibTableColumn
rh1PerfMonSegCounts = _Rh1PerfMonSegCounts_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 1, 1, 24),
    _Rh1PerfMonSegCounts_Type()
)
rh1PerfMonSegCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonSegCounts.setStatus("mandatory")
_Rh1PerfMonPortTable_Object = MibTable
rh1PerfMonPortTable = _Rh1PerfMonPortTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 2)
)
if mibBuilder.loadTexts:
    rh1PerfMonPortTable.setStatus("mandatory")
_Rh1PerfMonPortEntry_Object = MibTableRow
rh1PerfMonPortEntry = _Rh1PerfMonPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 2, 1)
)
rh1PerfMonPortEntry.setIndexNames(
    (0, "RH-ATT-MIB", "rh1PerfMonCardID"),
    (0, "RH-ATT-MIB", "rh1PerfMonPortID"),
)
if mibBuilder.loadTexts:
    rh1PerfMonPortEntry.setStatus("mandatory")
_Rh1PerfMonCardID_Type = Integer32
_Rh1PerfMonCardID_Object = MibTableColumn
rh1PerfMonCardID = _Rh1PerfMonCardID_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 2, 1, 1),
    _Rh1PerfMonCardID_Type()
)
rh1PerfMonCardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonCardID.setStatus("mandatory")
_Rh1PerfMonPortID_Type = Integer32
_Rh1PerfMonPortID_Object = MibTableColumn
rh1PerfMonPortID = _Rh1PerfMonPortID_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 2, 1, 2),
    _Rh1PerfMonPortID_Type()
)
rh1PerfMonPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonPortID.setStatus("mandatory")
_Rh1PerfMonFramesReceivedOk_Type = Counter32
_Rh1PerfMonFramesReceivedOk_Object = MibTableColumn
rh1PerfMonFramesReceivedOk = _Rh1PerfMonFramesReceivedOk_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 2, 1, 3),
    _Rh1PerfMonFramesReceivedOk_Type()
)
rh1PerfMonFramesReceivedOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonFramesReceivedOk.setStatus("mandatory")
_Rh1PerfMonOctetsReceivedOk_Type = Counter32
_Rh1PerfMonOctetsReceivedOk_Object = MibTableColumn
rh1PerfMonOctetsReceivedOk = _Rh1PerfMonOctetsReceivedOk_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 2, 1, 4),
    _Rh1PerfMonOctetsReceivedOk_Type()
)
rh1PerfMonOctetsReceivedOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonOctetsReceivedOk.setStatus("mandatory")
_Rh1PerfMonCollisions_Type = Counter32
_Rh1PerfMonCollisions_Object = MibTableColumn
rh1PerfMonCollisions = _Rh1PerfMonCollisions_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 2, 1, 5),
    _Rh1PerfMonCollisions_Type()
)
rh1PerfMonCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonCollisions.setStatus("mandatory")
_Rh1PerfMonLateCollisions_Type = Counter32
_Rh1PerfMonLateCollisions_Object = MibTableColumn
rh1PerfMonLateCollisions = _Rh1PerfMonLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 2, 1, 6),
    _Rh1PerfMonLateCollisions_Type()
)
rh1PerfMonLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonLateCollisions.setStatus("mandatory")
_Rh1PerfMonRunts_Type = Counter32
_Rh1PerfMonRunts_Object = MibTableColumn
rh1PerfMonRunts = _Rh1PerfMonRunts_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 2, 1, 7),
    _Rh1PerfMonRunts_Type()
)
rh1PerfMonRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonRunts.setStatus("mandatory")
_Rh1PerfMonShortEvents_Type = Counter32
_Rh1PerfMonShortEvents_Object = MibTableColumn
rh1PerfMonShortEvents = _Rh1PerfMonShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 2, 1, 8),
    _Rh1PerfMonShortEvents_Type()
)
rh1PerfMonShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonShortEvents.setStatus("mandatory")
_Rh1PerfMonFrameTooLongs_Type = Counter32
_Rh1PerfMonFrameTooLongs_Object = MibTableColumn
rh1PerfMonFrameTooLongs = _Rh1PerfMonFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 2, 1, 9),
    _Rh1PerfMonFrameTooLongs_Type()
)
rh1PerfMonFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonFrameTooLongs.setStatus("mandatory")
_Rh1PerfMonAutoPartitions_Type = Counter32
_Rh1PerfMonAutoPartitions_Object = MibTableColumn
rh1PerfMonAutoPartitions = _Rh1PerfMonAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 2, 1, 10),
    _Rh1PerfMonAutoPartitions_Type()
)
rh1PerfMonAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonAutoPartitions.setStatus("mandatory")
_Rh1PerfMonLongFragments_Type = Counter32
_Rh1PerfMonLongFragments_Object = MibTableColumn
rh1PerfMonLongFragments = _Rh1PerfMonLongFragments_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 2, 1, 11),
    _Rh1PerfMonLongFragments_Type()
)
rh1PerfMonLongFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonLongFragments.setStatus("mandatory")
_Rh1PerfMonFifoErrors_Type = Counter32
_Rh1PerfMonFifoErrors_Object = MibTableColumn
rh1PerfMonFifoErrors = _Rh1PerfMonFifoErrors_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 2, 1, 12),
    _Rh1PerfMonFifoErrors_Type()
)
rh1PerfMonFifoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonFifoErrors.setStatus("mandatory")
_Rh1PerfMonFramesTransmittedOk_Type = Counter32
_Rh1PerfMonFramesTransmittedOk_Object = MibTableColumn
rh1PerfMonFramesTransmittedOk = _Rh1PerfMonFramesTransmittedOk_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 2, 1, 13),
    _Rh1PerfMonFramesTransmittedOk_Type()
)
rh1PerfMonFramesTransmittedOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonFramesTransmittedOk.setStatus("mandatory")
_Rh1PerfMonOctetsTransmittedOk_Type = Counter32
_Rh1PerfMonOctetsTransmittedOk_Object = MibTableColumn
rh1PerfMonOctetsTransmittedOk = _Rh1PerfMonOctetsTransmittedOk_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 2, 1, 14),
    _Rh1PerfMonOctetsTransmittedOk_Type()
)
rh1PerfMonOctetsTransmittedOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonOctetsTransmittedOk.setStatus("mandatory")
_Rh1PerfMonErrorEnergy_Type = Counter32
_Rh1PerfMonErrorEnergy_Object = MibTableColumn
rh1PerfMonErrorEnergy = _Rh1PerfMonErrorEnergy_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 2, 1, 15),
    _Rh1PerfMonErrorEnergy_Type()
)
rh1PerfMonErrorEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonErrorEnergy.setStatus("mandatory")
_Rh1PerfMonNondataEnergy_Type = Counter32
_Rh1PerfMonNondataEnergy_Object = MibTableColumn
rh1PerfMonNondataEnergy = _Rh1PerfMonNondataEnergy_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 2, 1, 16),
    _Rh1PerfMonNondataEnergy_Type()
)
rh1PerfMonNondataEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonNondataEnergy.setStatus("mandatory")
_Rh1PerfMonManchesterViolations_Type = Counter32
_Rh1PerfMonManchesterViolations_Object = MibTableColumn
rh1PerfMonManchesterViolations = _Rh1PerfMonManchesterViolations_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 2, 1, 17),
    _Rh1PerfMonManchesterViolations_Type()
)
rh1PerfMonManchesterViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonManchesterViolations.setStatus("mandatory")
_Rh1PerfMonBand1Frames_Type = Counter32
_Rh1PerfMonBand1Frames_Object = MibTableColumn
rh1PerfMonBand1Frames = _Rh1PerfMonBand1Frames_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 2, 1, 18),
    _Rh1PerfMonBand1Frames_Type()
)
rh1PerfMonBand1Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonBand1Frames.setStatus("mandatory")
_Rh1PerfMonBand2Frames_Type = Counter32
_Rh1PerfMonBand2Frames_Object = MibTableColumn
rh1PerfMonBand2Frames = _Rh1PerfMonBand2Frames_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 2, 1, 19),
    _Rh1PerfMonBand2Frames_Type()
)
rh1PerfMonBand2Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonBand2Frames.setStatus("mandatory")
_Rh1PerfMonBand3Frames_Type = Counter32
_Rh1PerfMonBand3Frames_Object = MibTableColumn
rh1PerfMonBand3Frames = _Rh1PerfMonBand3Frames_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 2, 1, 20),
    _Rh1PerfMonBand3Frames_Type()
)
rh1PerfMonBand3Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonBand3Frames.setStatus("mandatory")
_Rh1PerfMonBand4Frames_Type = Counter32
_Rh1PerfMonBand4Frames_Object = MibTableColumn
rh1PerfMonBand4Frames = _Rh1PerfMonBand4Frames_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 2, 1, 21),
    _Rh1PerfMonBand4Frames_Type()
)
rh1PerfMonBand4Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonBand4Frames.setStatus("mandatory")
_Rh1PerfMonBand5Frames_Type = Counter32
_Rh1PerfMonBand5Frames_Object = MibTableColumn
rh1PerfMonBand5Frames = _Rh1PerfMonBand5Frames_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 2, 1, 22),
    _Rh1PerfMonBand5Frames_Type()
)
rh1PerfMonBand5Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonBand5Frames.setStatus("mandatory")
_Rh1PerfMonPortCounts_Type = OctetString
_Rh1PerfMonPortCounts_Object = MibTableColumn
rh1PerfMonPortCounts = _Rh1PerfMonPortCounts_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 2, 1, 23),
    _Rh1PerfMonPortCounts_Type()
)
rh1PerfMonPortCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonPortCounts.setStatus("mandatory")
_Rh1PerfMonFrameSize1Bound_Type = Integer32
_Rh1PerfMonFrameSize1Bound_Object = MibTableColumn
rh1PerfMonFrameSize1Bound = _Rh1PerfMonFrameSize1Bound_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 2, 1, 24),
    _Rh1PerfMonFrameSize1Bound_Type()
)
rh1PerfMonFrameSize1Bound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonFrameSize1Bound.setStatus("mandatory")
_Rh1PerfMonFrameSize2Bound_Type = Integer32
_Rh1PerfMonFrameSize2Bound_Object = MibTableColumn
rh1PerfMonFrameSize2Bound = _Rh1PerfMonFrameSize2Bound_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 2, 1, 25),
    _Rh1PerfMonFrameSize2Bound_Type()
)
rh1PerfMonFrameSize2Bound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonFrameSize2Bound.setStatus("mandatory")
_Rh1PerfMonFrameSize3Bound_Type = Integer32
_Rh1PerfMonFrameSize3Bound_Object = MibTableColumn
rh1PerfMonFrameSize3Bound = _Rh1PerfMonFrameSize3Bound_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 2, 1, 26),
    _Rh1PerfMonFrameSize3Bound_Type()
)
rh1PerfMonFrameSize3Bound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonFrameSize3Bound.setStatus("mandatory")
_Rh1PerfMonFrameSize4Bound_Type = Counter32
_Rh1PerfMonFrameSize4Bound_Object = MibTableColumn
rh1PerfMonFrameSize4Bound = _Rh1PerfMonFrameSize4Bound_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 3, 2, 1, 27),
    _Rh1PerfMonFrameSize4Bound_Type()
)
rh1PerfMonFrameSize4Bound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1PerfMonFrameSize4Bound.setStatus("mandatory")
_Rh1DownloadCapability_ObjectIdentity = ObjectIdentity
rh1DownloadCapability = _Rh1DownloadCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 4)
)
_Rh1DownloadImageFile_Type = OctetString
_Rh1DownloadImageFile_Object = MibScalar
rh1DownloadImageFile = _Rh1DownloadImageFile_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 4, 1),
    _Rh1DownloadImageFile_Type()
)
rh1DownloadImageFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1DownloadImageFile.setStatus("mandatory")
_Rh1DownloadIpAddr_Type = IpAddress
_Rh1DownloadIpAddr_Object = MibScalar
rh1DownloadIpAddr = _Rh1DownloadIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 4, 2),
    _Rh1DownloadIpAddr_Type()
)
rh1DownloadIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1DownloadIpAddr.setStatus("mandatory")
_Rh1DownloadMacAddr_Type = OctetString
_Rh1DownloadMacAddr_Object = MibScalar
rh1DownloadMacAddr = _Rh1DownloadMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 4, 3),
    _Rh1DownloadMacAddr_Type()
)
rh1DownloadMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1DownloadMacAddr.setStatus("mandatory")
_Rh1DownloadCardTable_Object = MibTable
rh1DownloadCardTable = _Rh1DownloadCardTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 4, 4)
)
if mibBuilder.loadTexts:
    rh1DownloadCardTable.setStatus("mandatory")
_Rh1DownloadCardEntry_Object = MibTableRow
rh1DownloadCardEntry = _Rh1DownloadCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 4, 4, 1)
)
rh1DownloadCardEntry.setIndexNames(
    (0, "RH-ATT-MIB", "rh1DownloadCardID"),
)
if mibBuilder.loadTexts:
    rh1DownloadCardEntry.setStatus("mandatory")
_Rh1DownloadCardID_Type = Integer32
_Rh1DownloadCardID_Object = MibTableColumn
rh1DownloadCardID = _Rh1DownloadCardID_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 4, 4, 1, 1),
    _Rh1DownloadCardID_Type()
)
rh1DownloadCardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1DownloadCardID.setStatus("mandatory")


class _Rh1DownloadExecute_Type(Integer32):
    """Custom type rh1DownloadExecute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("no-execute", 1))
    )


_Rh1DownloadExecute_Type.__name__ = "Integer32"
_Rh1DownloadExecute_Object = MibTableColumn
rh1DownloadExecute = _Rh1DownloadExecute_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 4, 4, 1, 2),
    _Rh1DownloadExecute_Type()
)
rh1DownloadExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1DownloadExecute.setStatus("mandatory")
_Rh1AddrTrackCapability_ObjectIdentity = ObjectIdentity
rh1AddrTrackCapability = _Rh1AddrTrackCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 5)
)
_Rh1AddrTrackSegmentTable_Object = MibTable
rh1AddrTrackSegmentTable = _Rh1AddrTrackSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 5, 1)
)
if mibBuilder.loadTexts:
    rh1AddrTrackSegmentTable.setStatus("mandatory")
_Rh1AddrTrackEntry_Object = MibTableRow
rh1AddrTrackEntry = _Rh1AddrTrackEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 5, 1, 1)
)
rh1AddrTrackEntry.setIndexNames(
    (0, "RH-ATT-MIB", "rh1AddrTrackSegmentID"),
)
if mibBuilder.loadTexts:
    rh1AddrTrackEntry.setStatus("mandatory")
_Rh1AddrTrackSegmentID_Type = Integer32
_Rh1AddrTrackSegmentID_Object = MibTableColumn
rh1AddrTrackSegmentID = _Rh1AddrTrackSegmentID_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 5, 1, 1, 1),
    _Rh1AddrTrackSegmentID_Type()
)
rh1AddrTrackSegmentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1AddrTrackSegmentID.setStatus("mandatory")


class _Rh1AddrTrackSendHubLearn_Type(Integer32):
    """Custom type rh1AddrTrackSendHubLearn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("learning", 1),
          ("send-learn-packet", 2))
    )


_Rh1AddrTrackSendHubLearn_Type.__name__ = "Integer32"
_Rh1AddrTrackSendHubLearn_Object = MibTableColumn
rh1AddrTrackSendHubLearn = _Rh1AddrTrackSendHubLearn_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 5, 1, 1, 2),
    _Rh1AddrTrackSendHubLearn_Type()
)
rh1AddrTrackSendHubLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1AddrTrackSendHubLearn.setStatus("mandatory")


class _Rh1AddrTrackSendHubLearnCtrl_Type(Integer32):
    """Custom type rh1AddrTrackSendHubLearnCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allow-learn-packet", 3),
          ("inhibit-learn-packet", 2),
          ("other", 1))
    )


_Rh1AddrTrackSendHubLearnCtrl_Type.__name__ = "Integer32"
_Rh1AddrTrackSendHubLearnCtrl_Object = MibTableColumn
rh1AddrTrackSendHubLearnCtrl = _Rh1AddrTrackSendHubLearnCtrl_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 5, 1, 1, 3),
    _Rh1AddrTrackSendHubLearnCtrl_Type()
)
rh1AddrTrackSendHubLearnCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1AddrTrackSendHubLearnCtrl.setStatus("mandatory")
_Rh1AddrTrackPortTable_Object = MibTable
rh1AddrTrackPortTable = _Rh1AddrTrackPortTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 5, 2)
)
if mibBuilder.loadTexts:
    rh1AddrTrackPortTable.setStatus("mandatory")
_Rh1AddrTrackPortEntry_Object = MibTableRow
rh1AddrTrackPortEntry = _Rh1AddrTrackPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 5, 2, 1)
)
rh1AddrTrackPortEntry.setIndexNames(
    (0, "RH-ATT-MIB", "rh1AddrTrackCardID"),
    (0, "RH-ATT-MIB", "rh1AddrTrackPortID"),
)
if mibBuilder.loadTexts:
    rh1AddrTrackPortEntry.setStatus("mandatory")
_Rh1AddrTrackCardID_Type = Integer32
_Rh1AddrTrackCardID_Object = MibTableColumn
rh1AddrTrackCardID = _Rh1AddrTrackCardID_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 5, 2, 1, 1),
    _Rh1AddrTrackCardID_Type()
)
rh1AddrTrackCardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1AddrTrackCardID.setStatus("mandatory")
_Rh1AddrTrackPortID_Type = Integer32
_Rh1AddrTrackPortID_Object = MibTableColumn
rh1AddrTrackPortID = _Rh1AddrTrackPortID_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 5, 2, 1, 2),
    _Rh1AddrTrackPortID_Type()
)
rh1AddrTrackPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1AddrTrackPortID.setStatus("mandatory")
_Rh1AddrTrackDetectedMacAddr_Type = OctetString
_Rh1AddrTrackDetectedMacAddr_Object = MibTableColumn
rh1AddrTrackDetectedMacAddr = _Rh1AddrTrackDetectedMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 5, 2, 1, 3),
    _Rh1AddrTrackDetectedMacAddr_Type()
)
rh1AddrTrackDetectedMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1AddrTrackDetectedMacAddr.setStatus("mandatory")


class _Rh1AddrTrackDetectedAddrType_Type(Integer32):
    """Custom type rh1AddrTrackDetectedAddrType based on Integer32"""
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
        *(("connected-to-another-hub", 3),
          ("multiply-connected", 4),
          ("none", 1),
          ("singly-connected", 2))
    )


_Rh1AddrTrackDetectedAddrType_Type.__name__ = "Integer32"
_Rh1AddrTrackDetectedAddrType_Object = MibTableColumn
rh1AddrTrackDetectedAddrType = _Rh1AddrTrackDetectedAddrType_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 5, 2, 1, 4),
    _Rh1AddrTrackDetectedAddrType_Type()
)
rh1AddrTrackDetectedAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1AddrTrackDetectedAddrType.setStatus("mandatory")
_Rh1AddrTrackAuthMacAddr_Type = OctetString
_Rh1AddrTrackAuthMacAddr_Object = MibTableColumn
rh1AddrTrackAuthMacAddr = _Rh1AddrTrackAuthMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 5, 2, 1, 5),
    _Rh1AddrTrackAuthMacAddr_Type()
)
rh1AddrTrackAuthMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1AddrTrackAuthMacAddr.setStatus("mandatory")


class _Rh1AddrTrackAuthAddrType_Type(Integer32):
    """Custom type rh1AddrTrackAuthAddrType based on Integer32"""
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
        *(("connected-to-another-hub", 3),
          ("multiply-connected", 4),
          ("none", 1),
          ("singly-connected", 2))
    )


_Rh1AddrTrackAuthAddrType_Type.__name__ = "Integer32"
_Rh1AddrTrackAuthAddrType_Object = MibTableColumn
rh1AddrTrackAuthAddrType = _Rh1AddrTrackAuthAddrType_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 5, 2, 1, 6),
    _Rh1AddrTrackAuthAddrType_Type()
)
rh1AddrTrackAuthAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1AddrTrackAuthAddrType.setStatus("mandatory")
_Rh1AddrTrackNewHubAddr_Type = OctetString
_Rh1AddrTrackNewHubAddr_Object = MibTableColumn
rh1AddrTrackNewHubAddr = _Rh1AddrTrackNewHubAddr_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 5, 2, 1, 7),
    _Rh1AddrTrackNewHubAddr_Type()
)
rh1AddrTrackNewHubAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rh1AddrTrackNewHubAddr.setStatus("mandatory")
_Rh1EnhCtrlCapability_ObjectIdentity = ObjectIdentity
rh1EnhCtrlCapability = _Rh1EnhCtrlCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6)
)


class _Rh1EnhCtrlResetRackConfig_Type(Integer32):
    """Custom type rh1EnhCtrlResetRackConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-reset", 1),
          ("reset", 2))
    )


_Rh1EnhCtrlResetRackConfig_Type.__name__ = "Integer32"
_Rh1EnhCtrlResetRackConfig_Object = MibScalar
rh1EnhCtrlResetRackConfig = _Rh1EnhCtrlResetRackConfig_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 1),
    _Rh1EnhCtrlResetRackConfig_Type()
)
rh1EnhCtrlResetRackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1EnhCtrlResetRackConfig.setStatus("mandatory")
_Rh1EnhCtrlRackVersion_Type = OctetString
_Rh1EnhCtrlRackVersion_Object = MibScalar
rh1EnhCtrlRackVersion = _Rh1EnhCtrlRackVersion_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 2),
    _Rh1EnhCtrlRackVersion_Type()
)
rh1EnhCtrlRackVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1EnhCtrlRackVersion.setStatus("mandatory")
_Rh1EnhCtrlPowerTable_Object = MibTable
rh1EnhCtrlPowerTable = _Rh1EnhCtrlPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 3)
)
if mibBuilder.loadTexts:
    rh1EnhCtrlPowerTable.setStatus("mandatory")
_Rh1EnhCtrlPowerEntry_Object = MibTableRow
rh1EnhCtrlPowerEntry = _Rh1EnhCtrlPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 3, 1)
)
rh1EnhCtrlPowerEntry.setIndexNames(
    (0, "RH-ATT-MIB", "rh1EnhCtrlPowerID"),
)
if mibBuilder.loadTexts:
    rh1EnhCtrlPowerEntry.setStatus("mandatory")
_Rh1EnhCtrlPowerID_Type = Integer32
_Rh1EnhCtrlPowerID_Object = MibTableColumn
rh1EnhCtrlPowerID = _Rh1EnhCtrlPowerID_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 3, 1, 1),
    _Rh1EnhCtrlPowerID_Type()
)
rh1EnhCtrlPowerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1EnhCtrlPowerID.setStatus("mandatory")


class _Rh1EnhCtrlPowerType_Type(Integer32):
    """Custom type rh1EnhCtrlPowerType based on Integer32"""
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
        *(("alternate", 3),
          ("none", 2),
          ("other", 1),
          ("standard", 4))
    )


_Rh1EnhCtrlPowerType_Type.__name__ = "Integer32"
_Rh1EnhCtrlPowerType_Object = MibTableColumn
rh1EnhCtrlPowerType = _Rh1EnhCtrlPowerType_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 3, 1, 2),
    _Rh1EnhCtrlPowerType_Type()
)
rh1EnhCtrlPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1EnhCtrlPowerType.setStatus("mandatory")
_Rh1EnhCtrlCardMap_Type = OctetString
_Rh1EnhCtrlCardMap_Object = MibScalar
rh1EnhCtrlCardMap = _Rh1EnhCtrlCardMap_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 4),
    _Rh1EnhCtrlCardMap_Type()
)
rh1EnhCtrlCardMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1EnhCtrlCardMap.setStatus("mandatory")
_Rh1EnhCtrlRackMap_Type = OctetString
_Rh1EnhCtrlRackMap_Object = MibScalar
rh1EnhCtrlRackMap = _Rh1EnhCtrlRackMap_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 5),
    _Rh1EnhCtrlRackMap_Type()
)
rh1EnhCtrlRackMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1EnhCtrlRackMap.setStatus("mandatory")
_Rh1EnhCtrlRackmaster_Type = Integer32
_Rh1EnhCtrlRackmaster_Object = MibScalar
rh1EnhCtrlRackmaster = _Rh1EnhCtrlRackmaster_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 6),
    _Rh1EnhCtrlRackmaster_Type()
)
rh1EnhCtrlRackmaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1EnhCtrlRackmaster.setStatus("mandatory")
_Rh1EnhCtrlLastRackmaster_Type = Integer32
_Rh1EnhCtrlLastRackmaster_Object = MibScalar
rh1EnhCtrlLastRackmaster = _Rh1EnhCtrlLastRackmaster_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 7),
    _Rh1EnhCtrlLastRackmaster_Type()
)
rh1EnhCtrlLastRackmaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1EnhCtrlLastRackmaster.setStatus("mandatory")
_Rh1EnhCtrlGatewayIpAddr_Type = IpAddress
_Rh1EnhCtrlGatewayIpAddr_Object = MibScalar
rh1EnhCtrlGatewayIpAddr = _Rh1EnhCtrlGatewayIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 8),
    _Rh1EnhCtrlGatewayIpAddr_Type()
)
rh1EnhCtrlGatewayIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1EnhCtrlGatewayIpAddr.setStatus("mandatory")
_Rh1EnhCtrlNetworkMask_Type = IpAddress
_Rh1EnhCtrlNetworkMask_Object = MibScalar
rh1EnhCtrlNetworkMask = _Rh1EnhCtrlNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 9),
    _Rh1EnhCtrlNetworkMask_Type()
)
rh1EnhCtrlNetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1EnhCtrlNetworkMask.setStatus("mandatory")
_Rh1EnhCtrlRackIpAddr_Type = IpAddress
_Rh1EnhCtrlRackIpAddr_Object = MibScalar
rh1EnhCtrlRackIpAddr = _Rh1EnhCtrlRackIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 10),
    _Rh1EnhCtrlRackIpAddr_Type()
)
rh1EnhCtrlRackIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1EnhCtrlRackIpAddr.setStatus("mandatory")


class _Rh1EnhCtrlRs232State_Type(Integer32):
    """Custom type rh1EnhCtrlRs232State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("connected-logged-in", 3),
          ("not-connected", 1))
    )


_Rh1EnhCtrlRs232State_Type.__name__ = "Integer32"
_Rh1EnhCtrlRs232State_Object = MibScalar
rh1EnhCtrlRs232State = _Rh1EnhCtrlRs232State_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 11),
    _Rh1EnhCtrlRs232State_Type()
)
rh1EnhCtrlRs232State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1EnhCtrlRs232State.setStatus("mandatory")


class _Rh1EnhCtrlRs232DataRate_Type(Integer32):
    """Custom type rh1EnhCtrlRs232DataRate based on Integer32"""
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
        *(("bps-1200", 2),
          ("bps-2400", 3),
          ("bps-300", 1),
          ("bps-4800", 4),
          ("bps-9600", 5))
    )


_Rh1EnhCtrlRs232DataRate_Type.__name__ = "Integer32"
_Rh1EnhCtrlRs232DataRate_Object = MibScalar
rh1EnhCtrlRs232DataRate = _Rh1EnhCtrlRs232DataRate_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 12),
    _Rh1EnhCtrlRs232DataRate_Type()
)
rh1EnhCtrlRs232DataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1EnhCtrlRs232DataRate.setStatus("mandatory")


class _Rh1EnhCtrlTrapCountPeriodCtrl_Type(Integer32):
    """Custom type rh1EnhCtrlTrapCountPeriodCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_Rh1EnhCtrlTrapCountPeriodCtrl_Type.__name__ = "Integer32"
_Rh1EnhCtrlTrapCountPeriodCtrl_Object = MibScalar
rh1EnhCtrlTrapCountPeriodCtrl = _Rh1EnhCtrlTrapCountPeriodCtrl_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 13),
    _Rh1EnhCtrlTrapCountPeriodCtrl_Type()
)
rh1EnhCtrlTrapCountPeriodCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1EnhCtrlTrapCountPeriodCtrl.setStatus("mandatory")


class _Rh1EnhCtrlFlashRackStatusLED_Type(Integer32):
    """Custom type rh1EnhCtrlFlashRackStatusLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flash", 3),
          ("noflash", 2),
          ("other", 1))
    )


_Rh1EnhCtrlFlashRackStatusLED_Type.__name__ = "Integer32"
_Rh1EnhCtrlFlashRackStatusLED_Object = MibScalar
rh1EnhCtrlFlashRackStatusLED = _Rh1EnhCtrlFlashRackStatusLED_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 14),
    _Rh1EnhCtrlFlashRackStatusLED_Type()
)
rh1EnhCtrlFlashRackStatusLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1EnhCtrlFlashRackStatusLED.setStatus("mandatory")


class _Rh1EnhCtrlSendTrapConfig_Type(Integer32):
    """Custom type rh1EnhCtrlSendTrapConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("send-trap", 2),
          ("sending", 1))
    )


_Rh1EnhCtrlSendTrapConfig_Type.__name__ = "Integer32"
_Rh1EnhCtrlSendTrapConfig_Object = MibScalar
rh1EnhCtrlSendTrapConfig = _Rh1EnhCtrlSendTrapConfig_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 15),
    _Rh1EnhCtrlSendTrapConfig_Type()
)
rh1EnhCtrlSendTrapConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1EnhCtrlSendTrapConfig.setStatus("mandatory")
_Rh1EnhCtrlMngrTable_Object = MibTable
rh1EnhCtrlMngrTable = _Rh1EnhCtrlMngrTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 16)
)
if mibBuilder.loadTexts:
    rh1EnhCtrlMngrTable.setStatus("mandatory")
_Rh1EnhCtrlMngrEntry_Object = MibTableRow
rh1EnhCtrlMngrEntry = _Rh1EnhCtrlMngrEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 16, 1)
)
rh1EnhCtrlMngrEntry.setIndexNames(
    (0, "RH-ATT-MIB", "rh1EnhCtrlMngrID"),
)
if mibBuilder.loadTexts:
    rh1EnhCtrlMngrEntry.setStatus("mandatory")
_Rh1EnhCtrlMngrID_Type = Integer32
_Rh1EnhCtrlMngrID_Object = MibTableColumn
rh1EnhCtrlMngrID = _Rh1EnhCtrlMngrID_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 16, 1, 1),
    _Rh1EnhCtrlMngrID_Type()
)
rh1EnhCtrlMngrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1EnhCtrlMngrID.setStatus("mandatory")
_Rh1EnhCtrlTrapMacAddr_Type = OctetString
_Rh1EnhCtrlTrapMacAddr_Object = MibTableColumn
rh1EnhCtrlTrapMacAddr = _Rh1EnhCtrlTrapMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 16, 1, 2),
    _Rh1EnhCtrlTrapMacAddr_Type()
)
rh1EnhCtrlTrapMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1EnhCtrlTrapMacAddr.setStatus("mandatory")
_Rh1EnhCtrlTrapIpAddr_Type = IpAddress
_Rh1EnhCtrlTrapIpAddr_Object = MibTableColumn
rh1EnhCtrlTrapIpAddr = _Rh1EnhCtrlTrapIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 16, 1, 3),
    _Rh1EnhCtrlTrapIpAddr_Type()
)
rh1EnhCtrlTrapIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1EnhCtrlTrapIpAddr.setStatus("mandatory")
_Rh1EnhCtrlCardTable_Object = MibTable
rh1EnhCtrlCardTable = _Rh1EnhCtrlCardTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 17)
)
if mibBuilder.loadTexts:
    rh1EnhCtrlCardTable.setStatus("mandatory")
_Rh1EnhCtrlCardEntry_Object = MibTableRow
rh1EnhCtrlCardEntry = _Rh1EnhCtrlCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 17, 1)
)
rh1EnhCtrlCardEntry.setIndexNames(
    (0, "RH-ATT-MIB", "rh1EnhCtrlCardID"),
)
if mibBuilder.loadTexts:
    rh1EnhCtrlCardEntry.setStatus("mandatory")
_Rh1EnhCtrlCardID_Type = Integer32
_Rh1EnhCtrlCardID_Object = MibTableColumn
rh1EnhCtrlCardID = _Rh1EnhCtrlCardID_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 17, 1, 1),
    _Rh1EnhCtrlCardID_Type()
)
rh1EnhCtrlCardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1EnhCtrlCardID.setStatus("mandatory")
_Rh1EnhCtrlSegment_Type = OctetString
_Rh1EnhCtrlSegment_Object = MibTableColumn
rh1EnhCtrlSegment = _Rh1EnhCtrlSegment_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 17, 1, 2),
    _Rh1EnhCtrlSegment_Type()
)
rh1EnhCtrlSegment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1EnhCtrlSegment.setStatus("mandatory")
_Rh1EnhCtrlCardVersion_Type = OctetString
_Rh1EnhCtrlCardVersion_Object = MibTableColumn
rh1EnhCtrlCardVersion = _Rh1EnhCtrlCardVersion_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 17, 1, 3),
    _Rh1EnhCtrlCardVersion_Type()
)
rh1EnhCtrlCardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1EnhCtrlCardVersion.setStatus("mandatory")
_Rh1EnhCtrlCardType_Type = OctetString
_Rh1EnhCtrlCardType_Object = MibTableColumn
rh1EnhCtrlCardType = _Rh1EnhCtrlCardType_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 17, 1, 4),
    _Rh1EnhCtrlCardType_Type()
)
rh1EnhCtrlCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1EnhCtrlCardType.setStatus("mandatory")
_Rh1EnhCtrlCardIpAddr_Type = IpAddress
_Rh1EnhCtrlCardIpAddr_Object = MibTableColumn
rh1EnhCtrlCardIpAddr = _Rh1EnhCtrlCardIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 17, 1, 5),
    _Rh1EnhCtrlCardIpAddr_Type()
)
rh1EnhCtrlCardIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1EnhCtrlCardIpAddr.setStatus("mandatory")


class _Rh1EnhCtrlResetCardConfig_Type(Integer32):
    """Custom type rh1EnhCtrlResetCardConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-reset", 1),
          ("reset", 2))
    )


_Rh1EnhCtrlResetCardConfig_Type.__name__ = "Integer32"
_Rh1EnhCtrlResetCardConfig_Object = MibTableColumn
rh1EnhCtrlResetCardConfig = _Rh1EnhCtrlResetCardConfig_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 17, 1, 6),
    _Rh1EnhCtrlResetCardConfig_Type()
)
rh1EnhCtrlResetCardConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1EnhCtrlResetCardConfig.setStatus("mandatory")


class _Rh1EnhCtrlFlashCardStatusLED_Type(Integer32):
    """Custom type rh1EnhCtrlFlashCardStatusLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flash", 3),
          ("noflash", 2),
          ("other", 1))
    )


_Rh1EnhCtrlFlashCardStatusLED_Type.__name__ = "Integer32"
_Rh1EnhCtrlFlashCardStatusLED_Object = MibTableColumn
rh1EnhCtrlFlashCardStatusLED = _Rh1EnhCtrlFlashCardStatusLED_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 17, 1, 7),
    _Rh1EnhCtrlFlashCardStatusLED_Type()
)
rh1EnhCtrlFlashCardStatusLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1EnhCtrlFlashCardStatusLED.setStatus("mandatory")
_Rh1EnhCtrlPortTable_Object = MibTable
rh1EnhCtrlPortTable = _Rh1EnhCtrlPortTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 18)
)
if mibBuilder.loadTexts:
    rh1EnhCtrlPortTable.setStatus("mandatory")
_Rh1EnhCtrlPortEntry_Object = MibTableRow
rh1EnhCtrlPortEntry = _Rh1EnhCtrlPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 18, 1)
)
rh1EnhCtrlPortEntry.setIndexNames(
    (0, "RH-ATT-MIB", "rh1EnhPortCtrlCardID"),
    (0, "RH-ATT-MIB", "rh1EnhCtrlPortID"),
)
if mibBuilder.loadTexts:
    rh1EnhCtrlPortEntry.setStatus("mandatory")
_Rh1EnhPortCtrlCardID_Type = Integer32
_Rh1EnhPortCtrlCardID_Object = MibTableColumn
rh1EnhPortCtrlCardID = _Rh1EnhPortCtrlCardID_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 18, 1, 1),
    _Rh1EnhPortCtrlCardID_Type()
)
rh1EnhPortCtrlCardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1EnhPortCtrlCardID.setStatus("mandatory")
_Rh1EnhCtrlPortID_Type = Integer32
_Rh1EnhCtrlPortID_Object = MibTableColumn
rh1EnhCtrlPortID = _Rh1EnhCtrlPortID_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 18, 1, 2),
    _Rh1EnhCtrlPortID_Type()
)
rh1EnhCtrlPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1EnhCtrlPortID.setStatus("mandatory")


class _Rh1EnhCtrlLinkIntegrityCtrl_Type(Integer32):
    """Custom type rh1EnhCtrlLinkIntegrityCtrl based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_Rh1EnhCtrlLinkIntegrityCtrl_Type.__name__ = "Integer32"
_Rh1EnhCtrlLinkIntegrityCtrl_Object = MibTableColumn
rh1EnhCtrlLinkIntegrityCtrl = _Rh1EnhCtrlLinkIntegrityCtrl_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 18, 1, 3),
    _Rh1EnhCtrlLinkIntegrityCtrl_Type()
)
rh1EnhCtrlLinkIntegrityCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1EnhCtrlLinkIntegrityCtrl.setStatus("mandatory")


class _Rh1EnhCtrlLinkIntegrityAlarmingCtrl_Type(Integer32):
    """Custom type rh1EnhCtrlLinkIntegrityAlarmingCtrl based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_Rh1EnhCtrlLinkIntegrityAlarmingCtrl_Type.__name__ = "Integer32"
_Rh1EnhCtrlLinkIntegrityAlarmingCtrl_Object = MibTableColumn
rh1EnhCtrlLinkIntegrityAlarmingCtrl = _Rh1EnhCtrlLinkIntegrityAlarmingCtrl_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 18, 1, 4),
    _Rh1EnhCtrlLinkIntegrityAlarmingCtrl_Type()
)
rh1EnhCtrlLinkIntegrityAlarmingCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1EnhCtrlLinkIntegrityAlarmingCtrl.setStatus("mandatory")


class _Rh1EnhCtrlLinkIntegrityState_Type(Integer32):
    """Custom type rh1EnhCtrlLinkIntegrityState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("failed", 3),
          ("not-applicable", 1))
    )


_Rh1EnhCtrlLinkIntegrityState_Type.__name__ = "Integer32"
_Rh1EnhCtrlLinkIntegrityState_Object = MibTableColumn
rh1EnhCtrlLinkIntegrityState = _Rh1EnhCtrlLinkIntegrityState_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 18, 1, 5),
    _Rh1EnhCtrlLinkIntegrityState_Type()
)
rh1EnhCtrlLinkIntegrityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1EnhCtrlLinkIntegrityState.setStatus("mandatory")


class _Rh1EnhCtrlExtendedDistanceCtrl_Type(Integer32):
    """Custom type rh1EnhCtrlExtendedDistanceCtrl based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_Rh1EnhCtrlExtendedDistanceCtrl_Type.__name__ = "Integer32"
_Rh1EnhCtrlExtendedDistanceCtrl_Object = MibTableColumn
rh1EnhCtrlExtendedDistanceCtrl = _Rh1EnhCtrlExtendedDistanceCtrl_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 18, 1, 6),
    _Rh1EnhCtrlExtendedDistanceCtrl_Type()
)
rh1EnhCtrlExtendedDistanceCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1EnhCtrlExtendedDistanceCtrl.setStatus("mandatory")
_Rh1EnhCtrlPortConfig_Type = OctetString
_Rh1EnhCtrlPortConfig_Object = MibTableColumn
rh1EnhCtrlPortConfig = _Rh1EnhCtrlPortConfig_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 18, 1, 7),
    _Rh1EnhCtrlPortConfig_Type()
)
rh1EnhCtrlPortConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1EnhCtrlPortConfig.setStatus("mandatory")


class _Rh1EnhCtrlPAPortCtrl_Type(Integer32):
    """Custom type rh1EnhCtrlPAPortCtrl based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_Rh1EnhCtrlPAPortCtrl_Type.__name__ = "Integer32"
_Rh1EnhCtrlPAPortCtrl_Object = MibScalar
rh1EnhCtrlPAPortCtrl = _Rh1EnhCtrlPAPortCtrl_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 19),
    _Rh1EnhCtrlPAPortCtrl_Type()
)
rh1EnhCtrlPAPortCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1EnhCtrlPAPortCtrl.setStatus("mandatory")


class _Rh1EnhCtrlPALinkIntegrityState_Type(Integer32):
    """Custom type rh1EnhCtrlPALinkIntegrityState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("failed", 3),
          ("other", 1))
    )


_Rh1EnhCtrlPALinkIntegrityState_Type.__name__ = "Integer32"
_Rh1EnhCtrlPALinkIntegrityState_Object = MibScalar
rh1EnhCtrlPALinkIntegrityState = _Rh1EnhCtrlPALinkIntegrityState_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 20),
    _Rh1EnhCtrlPALinkIntegrityState_Type()
)
rh1EnhCtrlPALinkIntegrityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1EnhCtrlPALinkIntegrityState.setStatus("mandatory")
_Rh1EnhCtrlSegmentTable_Object = MibTable
rh1EnhCtrlSegmentTable = _Rh1EnhCtrlSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 21)
)
if mibBuilder.loadTexts:
    rh1EnhCtrlSegmentTable.setStatus("mandatory")
_Rh1EnhCtrlSegmentEntry_Object = MibTableRow
rh1EnhCtrlSegmentEntry = _Rh1EnhCtrlSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 21, 1)
)
rh1EnhCtrlSegmentEntry.setIndexNames(
    (0, "RH-ATT-MIB", "rh1EnhCtrlSegmentID"),
)
if mibBuilder.loadTexts:
    rh1EnhCtrlSegmentEntry.setStatus("mandatory")
_Rh1EnhCtrlSegmentID_Type = Integer32
_Rh1EnhCtrlSegmentID_Object = MibTableColumn
rh1EnhCtrlSegmentID = _Rh1EnhCtrlSegmentID_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 21, 1, 1),
    _Rh1EnhCtrlSegmentID_Type()
)
rh1EnhCtrlSegmentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1EnhCtrlSegmentID.setStatus("mandatory")


class _Rh1EnhCtrlSegConfigReset_Type(Integer32):
    """Custom type rh1EnhCtrlSegConfigReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-reset", 1),
          ("reset", 2))
    )


_Rh1EnhCtrlSegConfigReset_Type.__name__ = "Integer32"
_Rh1EnhCtrlSegConfigReset_Object = MibTableColumn
rh1EnhCtrlSegConfigReset = _Rh1EnhCtrlSegConfigReset_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 21, 1, 2),
    _Rh1EnhCtrlSegConfigReset_Type()
)
rh1EnhCtrlSegConfigReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1EnhCtrlSegConfigReset.setStatus("mandatory")


class _Rh1EnhCtrlConfigResetHub_Type(Integer32):
    """Custom type rh1EnhCtrlConfigResetHub based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-reset", 1),
          ("reset", 2))
    )


_Rh1EnhCtrlConfigResetHub_Type.__name__ = "Integer32"
_Rh1EnhCtrlConfigResetHub_Object = MibScalar
rh1EnhCtrlConfigResetHub = _Rh1EnhCtrlConfigResetHub_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 22),
    _Rh1EnhCtrlConfigResetHub_Type()
)
rh1EnhCtrlConfigResetHub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1EnhCtrlConfigResetHub.setStatus("mandatory")
_Rh1EnhCtrlSegmentMap_Type = OctetString
_Rh1EnhCtrlSegmentMap_Object = MibScalar
rh1EnhCtrlSegmentMap = _Rh1EnhCtrlSegmentMap_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 6, 23),
    _Rh1EnhCtrlSegmentMap_Type()
)
rh1EnhCtrlSegmentMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1EnhCtrlSegmentMap.setStatus("mandatory")
_Rh1SecurityCapability_ObjectIdentity = ObjectIdentity
rh1SecurityCapability = _Rh1SecurityCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 7)
)
_Rh1SecPassword_Type = OctetString
_Rh1SecPassword_Object = MibScalar
rh1SecPassword = _Rh1SecPassword_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 7, 1),
    _Rh1SecPassword_Type()
)
rh1SecPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    rh1SecPassword.setStatus("mandatory")
_Rh1SecBadComPasswords_Type = Counter32
_Rh1SecBadComPasswords_Object = MibScalar
rh1SecBadComPasswords = _Rh1SecBadComPasswords_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 7, 2),
    _Rh1SecBadComPasswords_Type()
)
rh1SecBadComPasswords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1SecBadComPasswords.setStatus("mandatory")
_Rh1SecSettingAdminMacAddr_Type = OctetString
_Rh1SecSettingAdminMacAddr_Object = MibScalar
rh1SecSettingAdminMacAddr = _Rh1SecSettingAdminMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 7, 3),
    _Rh1SecSettingAdminMacAddr_Type()
)
rh1SecSettingAdminMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1SecSettingAdminMacAddr.setStatus("mandatory")
_Rh1SecSettingAdminIpAddr_Type = IpAddress
_Rh1SecSettingAdminIpAddr_Object = MibScalar
rh1SecSettingAdminIpAddr = _Rh1SecSettingAdminIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 7, 4),
    _Rh1SecSettingAdminIpAddr_Type()
)
rh1SecSettingAdminIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1SecSettingAdminIpAddr.setStatus("mandatory")


class _Rh1SecInbandSetsState_Type(Integer32):
    """Custom type rh1SecInbandSetsState based on Integer32"""
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
        *(("disable-all", 2),
          ("disable-private", 4),
          ("disable-public", 3),
          ("enabled", 5),
          ("other", 1))
    )


_Rh1SecInbandSetsState_Type.__name__ = "Integer32"
_Rh1SecInbandSetsState_Object = MibScalar
rh1SecInbandSetsState = _Rh1SecInbandSetsState_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 7, 5),
    _Rh1SecInbandSetsState_Type()
)
rh1SecInbandSetsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1SecInbandSetsState.setStatus("mandatory")
_Rh1SecSegmentTable_Object = MibTable
rh1SecSegmentTable = _Rh1SecSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 7, 6)
)
if mibBuilder.loadTexts:
    rh1SecSegmentTable.setStatus("mandatory")
_Rh1SecSegmentEntry_Object = MibTableRow
rh1SecSegmentEntry = _Rh1SecSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 7, 6, 1)
)
rh1SecSegmentEntry.setIndexNames(
    (0, "RH-ATT-MIB", "rh1SecSegmentID"),
)
if mibBuilder.loadTexts:
    rh1SecSegmentEntry.setStatus("mandatory")
_Rh1SecSegmentID_Type = Integer32
_Rh1SecSegmentID_Object = MibTableColumn
rh1SecSegmentID = _Rh1SecSegmentID_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 7, 6, 1, 1),
    _Rh1SecSegmentID_Type()
)
rh1SecSegmentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1SecSegmentID.setStatus("mandatory")


class _Rh1SecEavesdroppingCtrl_Type(Integer32):
    """Custom type rh1SecEavesdroppingCtrl based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_Rh1SecEavesdroppingCtrl_Type.__name__ = "Integer32"
_Rh1SecEavesdroppingCtrl_Object = MibTableColumn
rh1SecEavesdroppingCtrl = _Rh1SecEavesdroppingCtrl_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 7, 6, 1, 2),
    _Rh1SecEavesdroppingCtrl_Type()
)
rh1SecEavesdroppingCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1SecEavesdroppingCtrl.setStatus("mandatory")


class _Rh1SecIntrusionCtrl_Type(Integer32):
    """Custom type rh1SecIntrusionCtrl based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_Rh1SecIntrusionCtrl_Type.__name__ = "Integer32"
_Rh1SecIntrusionCtrl_Object = MibTableColumn
rh1SecIntrusionCtrl = _Rh1SecIntrusionCtrl_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 7, 6, 1, 3),
    _Rh1SecIntrusionCtrl_Type()
)
rh1SecIntrusionCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1SecIntrusionCtrl.setStatus("mandatory")


class _Rh1SecIntrusionAlarmCtrl_Type(Integer32):
    """Custom type rh1SecIntrusionAlarmCtrl based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_Rh1SecIntrusionAlarmCtrl_Type.__name__ = "Integer32"
_Rh1SecIntrusionAlarmCtrl_Object = MibTableColumn
rh1SecIntrusionAlarmCtrl = _Rh1SecIntrusionAlarmCtrl_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 7, 6, 1, 4),
    _Rh1SecIntrusionAlarmCtrl_Type()
)
rh1SecIntrusionAlarmCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rh1SecIntrusionAlarmCtrl.setStatus("mandatory")
_Rh1SecPortTable_Object = MibTable
rh1SecPortTable = _Rh1SecPortTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 7, 7)
)
if mibBuilder.loadTexts:
    rh1SecPortTable.setStatus("mandatory")
_Rh1SecPortEntry_Object = MibTableRow
rh1SecPortEntry = _Rh1SecPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 7, 7, 1)
)
rh1SecPortEntry.setIndexNames(
    (0, "RH-ATT-MIB", "rh1SecCardID"),
    (0, "RH-ATT-MIB", "rh1SecPortID"),
)
if mibBuilder.loadTexts:
    rh1SecPortEntry.setStatus("mandatory")
_Rh1SecCardID_Type = Integer32
_Rh1SecCardID_Object = MibTableColumn
rh1SecCardID = _Rh1SecCardID_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 7, 7, 1, 1),
    _Rh1SecCardID_Type()
)
rh1SecCardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1SecCardID.setStatus("mandatory")
_Rh1SecPortID_Type = Integer32
_Rh1SecPortID_Object = MibTableColumn
rh1SecPortID = _Rh1SecPortID_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 7, 7, 1, 2),
    _Rh1SecPortID_Type()
)
rh1SecPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1SecPortID.setStatus("mandatory")
_Rh1SecIntrusionAddr_Type = OctetString
_Rh1SecIntrusionAddr_Object = MibTableColumn
rh1SecIntrusionAddr = _Rh1SecIntrusionAddr_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 7, 7, 1, 3),
    _Rh1SecIntrusionAddr_Type()
)
rh1SecIntrusionAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1SecIntrusionAddr.setStatus("mandatory")
_Rh1SecIntrusionTimeStamp_Type = TimeTicks
_Rh1SecIntrusionTimeStamp_Object = MibTableColumn
rh1SecIntrusionTimeStamp = _Rh1SecIntrusionTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 7, 7, 1, 4),
    _Rh1SecIntrusionTimeStamp_Type()
)
rh1SecIntrusionTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1SecIntrusionTimeStamp.setStatus("mandatory")
_Rh1SecIntrusions_Type = Counter32
_Rh1SecIntrusions_Object = MibTableColumn
rh1SecIntrusions = _Rh1SecIntrusions_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 14, 7, 7, 1, 5),
    _Rh1SecIntrusions_Type()
)
rh1SecIntrusions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rh1SecIntrusions.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RH-ATT-MIB",
    **{"att-2": att_2,
       "att-products": att_products,
       "att-rh1products": att_rh1products,
       "att-rh1xe": att_rh1xe,
       "att-mgmt": att_mgmt,
       "att-rh1mgt": att_rh1mgt,
       "rh1BasicCtrlCapability": rh1BasicCtrlCapability,
       "rh1BasicCtrlRackMAC": rh1BasicCtrlRackMAC,
       "rh1BasicCtrlCardCapacity": rh1BasicCtrlCardCapacity,
       "rh1BasicCtrlCardTable": rh1BasicCtrlCardTable,
       "rh1BasicCtrlCardEntry": rh1BasicCtrlCardEntry,
       "rh1BasicCtrlCardID": rh1BasicCtrlCardID,
       "rh1BasicCtrlNumberOfPorts": rh1BasicCtrlNumberOfPorts,
       "rh1BasicCtrlPortTable": rh1BasicCtrlPortTable,
       "rh1BasicCtrlPortEntry": rh1BasicCtrlPortEntry,
       "rh1BasicPortCtrlCardID": rh1BasicPortCtrlCardID,
       "rh1BasicCtrlPortID": rh1BasicCtrlPortID,
       "rh1BasicCtrlPortType": rh1BasicCtrlPortType,
       "rh1BasicCtrlPortCtrl": rh1BasicCtrlPortCtrl,
       "rh1BasicCtrlAutoPartitionState": rh1BasicCtrlAutoPartitionState,
       "rh1SelfTestCapability": rh1SelfTestCapability,
       "rh1SelfTestResetRack": rh1SelfTestResetRack,
       "rh1SelfTestExecuteSelfTest1": rh1SelfTestExecuteSelfTest1,
       "rh1SelfTestExecuteSelfTest2": rh1SelfTestExecuteSelfTest2,
       "rh1SelfTestRackHealthState": rh1SelfTestRackHealthState,
       "rh1SelfTestRackHealthData": rh1SelfTestRackHealthData,
       "rh1SelfTestCardTable": rh1SelfTestCardTable,
       "rh1SelfTestCardEntry": rh1SelfTestCardEntry,
       "rh1SelfTestCardID": rh1SelfTestCardID,
       "rh1SelfTestCardResetTimeStamp": rh1SelfTestCardResetTimeStamp,
       "rh1SelfTestResetCard": rh1SelfTestResetCard,
       "rh1SelfTestResetMPR": rh1SelfTestResetMPR,
       "rh1SelfTestExecuteCardSelfTest1": rh1SelfTestExecuteCardSelfTest1,
       "rh1SelfTestExecuteCardSelfTest2": rh1SelfTestExecuteCardSelfTest2,
       "rh1SelfTestCardHealthState": rh1SelfTestCardHealthState,
       "rh1SelfTestCardHealthData": rh1SelfTestCardHealthData,
       "rh1PerfMonCapability": rh1PerfMonCapability,
       "rh1PerfMonSegmentTable": rh1PerfMonSegmentTable,
       "rh1PerfMonSegmentEntry": rh1PerfMonSegmentEntry,
       "rh1PerfMonSegmentID": rh1PerfMonSegmentID,
       "rh1PerfMonSegFrameSize1Bound": rh1PerfMonSegFrameSize1Bound,
       "rh1PerfMonSegFrameSize2Bound": rh1PerfMonSegFrameSize2Bound,
       "rh1PerfMonSegFrameSize3Bound": rh1PerfMonSegFrameSize3Bound,
       "rh1PerfMonSegFrameSize4Bound": rh1PerfMonSegFrameSize4Bound,
       "rh1PerfMonSegTotalFramesProcessedOk": rh1PerfMonSegTotalFramesProcessedOk,
       "rh1PerfMonSegTotalOctetsProcessedOk": rh1PerfMonSegTotalOctetsProcessedOk,
       "rh1PerfMonSegTotalCollisions": rh1PerfMonSegTotalCollisions,
       "rh1PerfMonSegTotalLateCollisions": rh1PerfMonSegTotalLateCollisions,
       "rh1PerfMonSegTotalRunts": rh1PerfMonSegTotalRunts,
       "rh1PerfMonSegTotalShortEvents": rh1PerfMonSegTotalShortEvents,
       "rh1PerfMonSegTotalFrameTooLongs": rh1PerfMonSegTotalFrameTooLongs,
       "rh1PerfMonSegTotalAutoPartitions": rh1PerfMonSegTotalAutoPartitions,
       "rh1PerfMonSegTotalLongFragments": rh1PerfMonSegTotalLongFragments,
       "rh1PerfMonSegTotalFifoErrors": rh1PerfMonSegTotalFifoErrors,
       "rh1PerfMonSegTotalErrorEnergy": rh1PerfMonSegTotalErrorEnergy,
       "rh1PerfMonSegTotalNondataEnergy": rh1PerfMonSegTotalNondataEnergy,
       "rh1PerfMonSegTotalManchesterViolations": rh1PerfMonSegTotalManchesterViolations,
       "rh1PerfMonSegTotalBand1Frames": rh1PerfMonSegTotalBand1Frames,
       "rh1PerfMonSegTotalBand2Frames": rh1PerfMonSegTotalBand2Frames,
       "rh1PerfMonSegTotalBand3Frames": rh1PerfMonSegTotalBand3Frames,
       "rh1PerfMonSegTotalBand4Frames": rh1PerfMonSegTotalBand4Frames,
       "rh1PerfMonSegTotalBand5Frames": rh1PerfMonSegTotalBand5Frames,
       "rh1PerfMonSegCounts": rh1PerfMonSegCounts,
       "rh1PerfMonPortTable": rh1PerfMonPortTable,
       "rh1PerfMonPortEntry": rh1PerfMonPortEntry,
       "rh1PerfMonCardID": rh1PerfMonCardID,
       "rh1PerfMonPortID": rh1PerfMonPortID,
       "rh1PerfMonFramesReceivedOk": rh1PerfMonFramesReceivedOk,
       "rh1PerfMonOctetsReceivedOk": rh1PerfMonOctetsReceivedOk,
       "rh1PerfMonCollisions": rh1PerfMonCollisions,
       "rh1PerfMonLateCollisions": rh1PerfMonLateCollisions,
       "rh1PerfMonRunts": rh1PerfMonRunts,
       "rh1PerfMonShortEvents": rh1PerfMonShortEvents,
       "rh1PerfMonFrameTooLongs": rh1PerfMonFrameTooLongs,
       "rh1PerfMonAutoPartitions": rh1PerfMonAutoPartitions,
       "rh1PerfMonLongFragments": rh1PerfMonLongFragments,
       "rh1PerfMonFifoErrors": rh1PerfMonFifoErrors,
       "rh1PerfMonFramesTransmittedOk": rh1PerfMonFramesTransmittedOk,
       "rh1PerfMonOctetsTransmittedOk": rh1PerfMonOctetsTransmittedOk,
       "rh1PerfMonErrorEnergy": rh1PerfMonErrorEnergy,
       "rh1PerfMonNondataEnergy": rh1PerfMonNondataEnergy,
       "rh1PerfMonManchesterViolations": rh1PerfMonManchesterViolations,
       "rh1PerfMonBand1Frames": rh1PerfMonBand1Frames,
       "rh1PerfMonBand2Frames": rh1PerfMonBand2Frames,
       "rh1PerfMonBand3Frames": rh1PerfMonBand3Frames,
       "rh1PerfMonBand4Frames": rh1PerfMonBand4Frames,
       "rh1PerfMonBand5Frames": rh1PerfMonBand5Frames,
       "rh1PerfMonPortCounts": rh1PerfMonPortCounts,
       "rh1PerfMonFrameSize1Bound": rh1PerfMonFrameSize1Bound,
       "rh1PerfMonFrameSize2Bound": rh1PerfMonFrameSize2Bound,
       "rh1PerfMonFrameSize3Bound": rh1PerfMonFrameSize3Bound,
       "rh1PerfMonFrameSize4Bound": rh1PerfMonFrameSize4Bound,
       "rh1DownloadCapability": rh1DownloadCapability,
       "rh1DownloadImageFile": rh1DownloadImageFile,
       "rh1DownloadIpAddr": rh1DownloadIpAddr,
       "rh1DownloadMacAddr": rh1DownloadMacAddr,
       "rh1DownloadCardTable": rh1DownloadCardTable,
       "rh1DownloadCardEntry": rh1DownloadCardEntry,
       "rh1DownloadCardID": rh1DownloadCardID,
       "rh1DownloadExecute": rh1DownloadExecute,
       "rh1AddrTrackCapability": rh1AddrTrackCapability,
       "rh1AddrTrackSegmentTable": rh1AddrTrackSegmentTable,
       "rh1AddrTrackEntry": rh1AddrTrackEntry,
       "rh1AddrTrackSegmentID": rh1AddrTrackSegmentID,
       "rh1AddrTrackSendHubLearn": rh1AddrTrackSendHubLearn,
       "rh1AddrTrackSendHubLearnCtrl": rh1AddrTrackSendHubLearnCtrl,
       "rh1AddrTrackPortTable": rh1AddrTrackPortTable,
       "rh1AddrTrackPortEntry": rh1AddrTrackPortEntry,
       "rh1AddrTrackCardID": rh1AddrTrackCardID,
       "rh1AddrTrackPortID": rh1AddrTrackPortID,
       "rh1AddrTrackDetectedMacAddr": rh1AddrTrackDetectedMacAddr,
       "rh1AddrTrackDetectedAddrType": rh1AddrTrackDetectedAddrType,
       "rh1AddrTrackAuthMacAddr": rh1AddrTrackAuthMacAddr,
       "rh1AddrTrackAuthAddrType": rh1AddrTrackAuthAddrType,
       "rh1AddrTrackNewHubAddr": rh1AddrTrackNewHubAddr,
       "rh1EnhCtrlCapability": rh1EnhCtrlCapability,
       "rh1EnhCtrlResetRackConfig": rh1EnhCtrlResetRackConfig,
       "rh1EnhCtrlRackVersion": rh1EnhCtrlRackVersion,
       "rh1EnhCtrlPowerTable": rh1EnhCtrlPowerTable,
       "rh1EnhCtrlPowerEntry": rh1EnhCtrlPowerEntry,
       "rh1EnhCtrlPowerID": rh1EnhCtrlPowerID,
       "rh1EnhCtrlPowerType": rh1EnhCtrlPowerType,
       "rh1EnhCtrlCardMap": rh1EnhCtrlCardMap,
       "rh1EnhCtrlRackMap": rh1EnhCtrlRackMap,
       "rh1EnhCtrlRackmaster": rh1EnhCtrlRackmaster,
       "rh1EnhCtrlLastRackmaster": rh1EnhCtrlLastRackmaster,
       "rh1EnhCtrlGatewayIpAddr": rh1EnhCtrlGatewayIpAddr,
       "rh1EnhCtrlNetworkMask": rh1EnhCtrlNetworkMask,
       "rh1EnhCtrlRackIpAddr": rh1EnhCtrlRackIpAddr,
       "rh1EnhCtrlRs232State": rh1EnhCtrlRs232State,
       "rh1EnhCtrlRs232DataRate": rh1EnhCtrlRs232DataRate,
       "rh1EnhCtrlTrapCountPeriodCtrl": rh1EnhCtrlTrapCountPeriodCtrl,
       "rh1EnhCtrlFlashRackStatusLED": rh1EnhCtrlFlashRackStatusLED,
       "rh1EnhCtrlSendTrapConfig": rh1EnhCtrlSendTrapConfig,
       "rh1EnhCtrlMngrTable": rh1EnhCtrlMngrTable,
       "rh1EnhCtrlMngrEntry": rh1EnhCtrlMngrEntry,
       "rh1EnhCtrlMngrID": rh1EnhCtrlMngrID,
       "rh1EnhCtrlTrapMacAddr": rh1EnhCtrlTrapMacAddr,
       "rh1EnhCtrlTrapIpAddr": rh1EnhCtrlTrapIpAddr,
       "rh1EnhCtrlCardTable": rh1EnhCtrlCardTable,
       "rh1EnhCtrlCardEntry": rh1EnhCtrlCardEntry,
       "rh1EnhCtrlCardID": rh1EnhCtrlCardID,
       "rh1EnhCtrlSegment": rh1EnhCtrlSegment,
       "rh1EnhCtrlCardVersion": rh1EnhCtrlCardVersion,
       "rh1EnhCtrlCardType": rh1EnhCtrlCardType,
       "rh1EnhCtrlCardIpAddr": rh1EnhCtrlCardIpAddr,
       "rh1EnhCtrlResetCardConfig": rh1EnhCtrlResetCardConfig,
       "rh1EnhCtrlFlashCardStatusLED": rh1EnhCtrlFlashCardStatusLED,
       "rh1EnhCtrlPortTable": rh1EnhCtrlPortTable,
       "rh1EnhCtrlPortEntry": rh1EnhCtrlPortEntry,
       "rh1EnhPortCtrlCardID": rh1EnhPortCtrlCardID,
       "rh1EnhCtrlPortID": rh1EnhCtrlPortID,
       "rh1EnhCtrlLinkIntegrityCtrl": rh1EnhCtrlLinkIntegrityCtrl,
       "rh1EnhCtrlLinkIntegrityAlarmingCtrl": rh1EnhCtrlLinkIntegrityAlarmingCtrl,
       "rh1EnhCtrlLinkIntegrityState": rh1EnhCtrlLinkIntegrityState,
       "rh1EnhCtrlExtendedDistanceCtrl": rh1EnhCtrlExtendedDistanceCtrl,
       "rh1EnhCtrlPortConfig": rh1EnhCtrlPortConfig,
       "rh1EnhCtrlPAPortCtrl": rh1EnhCtrlPAPortCtrl,
       "rh1EnhCtrlPALinkIntegrityState": rh1EnhCtrlPALinkIntegrityState,
       "rh1EnhCtrlSegmentTable": rh1EnhCtrlSegmentTable,
       "rh1EnhCtrlSegmentEntry": rh1EnhCtrlSegmentEntry,
       "rh1EnhCtrlSegmentID": rh1EnhCtrlSegmentID,
       "rh1EnhCtrlSegConfigReset": rh1EnhCtrlSegConfigReset,
       "rh1EnhCtrlConfigResetHub": rh1EnhCtrlConfigResetHub,
       "rh1EnhCtrlSegmentMap": rh1EnhCtrlSegmentMap,
       "rh1SecurityCapability": rh1SecurityCapability,
       "rh1SecPassword": rh1SecPassword,
       "rh1SecBadComPasswords": rh1SecBadComPasswords,
       "rh1SecSettingAdminMacAddr": rh1SecSettingAdminMacAddr,
       "rh1SecSettingAdminIpAddr": rh1SecSettingAdminIpAddr,
       "rh1SecInbandSetsState": rh1SecInbandSetsState,
       "rh1SecSegmentTable": rh1SecSegmentTable,
       "rh1SecSegmentEntry": rh1SecSegmentEntry,
       "rh1SecSegmentID": rh1SecSegmentID,
       "rh1SecEavesdroppingCtrl": rh1SecEavesdroppingCtrl,
       "rh1SecIntrusionCtrl": rh1SecIntrusionCtrl,
       "rh1SecIntrusionAlarmCtrl": rh1SecIntrusionAlarmCtrl,
       "rh1SecPortTable": rh1SecPortTable,
       "rh1SecPortEntry": rh1SecPortEntry,
       "rh1SecCardID": rh1SecCardID,
       "rh1SecPortID": rh1SecPortID,
       "rh1SecIntrusionAddr": rh1SecIntrusionAddr,
       "rh1SecIntrusionTimeStamp": rh1SecIntrusionTimeStamp,
       "rh1SecIntrusions": rh1SecIntrusions}
)
