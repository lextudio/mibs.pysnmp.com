# SNMP MIB module (SH-ATT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SH-ATT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:50:27 2024
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
_Att_hubmgtProd_ObjectIdentity = ObjectIdentity
att_hubmgtProd = _Att_hubmgtProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 1, 1)
)
_Att_mgmt_ObjectIdentity = ObjectIdentity
att_mgmt = _Att_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2)
)
_Att_hubmgt_ObjectIdentity = ObjectIdentity
att_hubmgt = _Att_hubmgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 1)
)
_Sh1BasicCtrlCapability_ObjectIdentity = ObjectIdentity
sh1BasicCtrlCapability = _Sh1BasicCtrlCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 1)
)
_Sh1BasicCtrlHubID_Type = OctetString
_Sh1BasicCtrlHubID_Object = MibScalar
sh1BasicCtrlHubID = _Sh1BasicCtrlHubID_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 1, 1),
    _Sh1BasicCtrlHubID_Type()
)
sh1BasicCtrlHubID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1BasicCtrlHubID.setStatus("mandatory")
_Sh1BasicCtrlHubGroupCapacity_Type = Integer32
_Sh1BasicCtrlHubGroupCapacity_Object = MibScalar
sh1BasicCtrlHubGroupCapacity = _Sh1BasicCtrlHubGroupCapacity_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 1, 2),
    _Sh1BasicCtrlHubGroupCapacity_Type()
)
sh1BasicCtrlHubGroupCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1BasicCtrlHubGroupCapacity.setStatus("mandatory")
_Sh1BasicCtrlGroupMap_Type = OctetString
_Sh1BasicCtrlGroupMap_Object = MibScalar
sh1BasicCtrlGroupMap = _Sh1BasicCtrlGroupMap_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 1, 3),
    _Sh1BasicCtrlGroupMap_Type()
)
sh1BasicCtrlGroupMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1BasicCtrlGroupMap.setStatus("mandatory")
_Sh1BasicCtrlGroupID_Type = Integer32
_Sh1BasicCtrlGroupID_Object = MibScalar
sh1BasicCtrlGroupID = _Sh1BasicCtrlGroupID_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 1, 4),
    _Sh1BasicCtrlGroupID_Type()
)
sh1BasicCtrlGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1BasicCtrlGroupID.setStatus("mandatory")
_Sh1BasicCtrlNumberOfPorts_Type = Integer32
_Sh1BasicCtrlNumberOfPorts_Object = MibScalar
sh1BasicCtrlNumberOfPorts = _Sh1BasicCtrlNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 1, 5),
    _Sh1BasicCtrlNumberOfPorts_Type()
)
sh1BasicCtrlNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1BasicCtrlNumberOfPorts.setStatus("mandatory")
_Sh1BasicCtrlPortTable_Object = MibTable
sh1BasicCtrlPortTable = _Sh1BasicCtrlPortTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    sh1BasicCtrlPortTable.setStatus("mandatory")
_Sh1BasicCtrlPortEntry_Object = MibTableRow
sh1BasicCtrlPortEntry = _Sh1BasicCtrlPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 1, 6, 1)
)
sh1BasicCtrlPortEntry.setIndexNames(
    (0, "SH-ATT-MIB", "sh1BasicCtrlPortID"),
)
if mibBuilder.loadTexts:
    sh1BasicCtrlPortEntry.setStatus("mandatory")
_Sh1BasicCtrlPortID_Type = Integer32
_Sh1BasicCtrlPortID_Object = MibTableColumn
sh1BasicCtrlPortID = _Sh1BasicCtrlPortID_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 1, 6, 1, 1),
    _Sh1BasicCtrlPortID_Type()
)
sh1BasicCtrlPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1BasicCtrlPortID.setStatus("mandatory")


class _Sh1BasicCtrlPortType_Type(Integer32):
    """Custom type sh1BasicCtrlPortType based on Integer32"""
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
          ("tenBASE-FAsync", 3),
          ("tenBASE-FSynch", 4))
    )


_Sh1BasicCtrlPortType_Type.__name__ = "Integer32"
_Sh1BasicCtrlPortType_Object = MibTableColumn
sh1BasicCtrlPortType = _Sh1BasicCtrlPortType_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 1, 6, 1, 2),
    _Sh1BasicCtrlPortType_Type()
)
sh1BasicCtrlPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1BasicCtrlPortType.setStatus("mandatory")


class _Sh1BasicCtrlPortCtrl_Type(Integer32):
    """Custom type sh1BasicCtrlPortCtrl based on Integer32"""
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


_Sh1BasicCtrlPortCtrl_Type.__name__ = "Integer32"
_Sh1BasicCtrlPortCtrl_Object = MibTableColumn
sh1BasicCtrlPortCtrl = _Sh1BasicCtrlPortCtrl_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 1, 6, 1, 3),
    _Sh1BasicCtrlPortCtrl_Type()
)
sh1BasicCtrlPortCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sh1BasicCtrlPortCtrl.setStatus("mandatory")


class _Sh1BasicCtrlAutoPartitionState_Type(Integer32):
    """Custom type sh1BasicCtrlAutoPartitionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoPartitioned", 3),
          ("notAutoPartitioned", 2),
          ("other", 1))
    )


_Sh1BasicCtrlAutoPartitionState_Type.__name__ = "Integer32"
_Sh1BasicCtrlAutoPartitionState_Object = MibTableColumn
sh1BasicCtrlAutoPartitionState = _Sh1BasicCtrlAutoPartitionState_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 1, 6, 1, 4),
    _Sh1BasicCtrlAutoPartitionState_Type()
)
sh1BasicCtrlAutoPartitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1BasicCtrlAutoPartitionState.setStatus("mandatory")
_Sh1SelfTestCapability_ObjectIdentity = ObjectIdentity
sh1SelfTestCapability = _Sh1SelfTestCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 2)
)
_Sh1SelfTestHubResetTimeStamp_Type = TimeTicks
_Sh1SelfTestHubResetTimeStamp_Object = MibScalar
sh1SelfTestHubResetTimeStamp = _Sh1SelfTestHubResetTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 2, 1),
    _Sh1SelfTestHubResetTimeStamp_Type()
)
sh1SelfTestHubResetTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1SelfTestHubResetTimeStamp.setStatus("mandatory")


class _Sh1SelfTestResetHubSystem_Type(Integer32):
    """Custom type sh1SelfTestResetHubSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Sh1SelfTestResetHubSystem_Type.__name__ = "Integer32"
_Sh1SelfTestResetHubSystem_Object = MibScalar
sh1SelfTestResetHubSystem = _Sh1SelfTestResetHubSystem_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 2, 2),
    _Sh1SelfTestResetHubSystem_Type()
)
sh1SelfTestResetHubSystem.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sh1SelfTestResetHubSystem.setStatus("mandatory")


class _Sh1SelfTestResetHub_Type(Integer32):
    """Custom type sh1SelfTestResetHub based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Sh1SelfTestResetHub_Type.__name__ = "Integer32"
_Sh1SelfTestResetHub_Object = MibScalar
sh1SelfTestResetHub = _Sh1SelfTestResetHub_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 2, 3),
    _Sh1SelfTestResetHub_Type()
)
sh1SelfTestResetHub.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sh1SelfTestResetHub.setStatus("mandatory")


class _Sh1SelfTestExecuteSelfTest1_Type(Integer32):
    """Custom type sh1SelfTestExecuteSelfTest1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("performTest", 1)
    )


_Sh1SelfTestExecuteSelfTest1_Type.__name__ = "Integer32"
_Sh1SelfTestExecuteSelfTest1_Object = MibScalar
sh1SelfTestExecuteSelfTest1 = _Sh1SelfTestExecuteSelfTest1_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 2, 4),
    _Sh1SelfTestExecuteSelfTest1_Type()
)
sh1SelfTestExecuteSelfTest1.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sh1SelfTestExecuteSelfTest1.setStatus("mandatory")


class _Sh1SelfTestExecuteSelfTest2_Type(Integer32):
    """Custom type sh1SelfTestExecuteSelfTest2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("performTest", 1)
    )


_Sh1SelfTestExecuteSelfTest2_Type.__name__ = "Integer32"
_Sh1SelfTestExecuteSelfTest2_Object = MibScalar
sh1SelfTestExecuteSelfTest2 = _Sh1SelfTestExecuteSelfTest2_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 2, 5),
    _Sh1SelfTestExecuteSelfTest2_Type()
)
sh1SelfTestExecuteSelfTest2.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sh1SelfTestExecuteSelfTest2.setStatus("mandatory")


class _Sh1SelfTestHubHealthState_Type(Integer32):
    """Custom type sh1SelfTestHubHealthState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("ok", 2),
          ("other", 1))
    )


_Sh1SelfTestHubHealthState_Type.__name__ = "Integer32"
_Sh1SelfTestHubHealthState_Object = MibScalar
sh1SelfTestHubHealthState = _Sh1SelfTestHubHealthState_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 2, 6),
    _Sh1SelfTestHubHealthState_Type()
)
sh1SelfTestHubHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1SelfTestHubHealthState.setStatus("mandatory")
_Sh1SelfTestHubHealthData_Type = OctetString
_Sh1SelfTestHubHealthData_Object = MibScalar
sh1SelfTestHubHealthData = _Sh1SelfTestHubHealthData_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 2, 7),
    _Sh1SelfTestHubHealthData_Type()
)
sh1SelfTestHubHealthData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1SelfTestHubHealthData.setStatus("mandatory")
_Sh1PerfMonCapability_ObjectIdentity = ObjectIdentity
sh1PerfMonCapability = _Sh1PerfMonCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3)
)
_Sh1PerfMonFrameSize1Bound_Type = Integer32
_Sh1PerfMonFrameSize1Bound_Object = MibScalar
sh1PerfMonFrameSize1Bound = _Sh1PerfMonFrameSize1Bound_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 1),
    _Sh1PerfMonFrameSize1Bound_Type()
)
sh1PerfMonFrameSize1Bound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sh1PerfMonFrameSize1Bound.setStatus("mandatory")
_Sh1PerfMonFrameSize2Bound_Type = Integer32
_Sh1PerfMonFrameSize2Bound_Object = MibScalar
sh1PerfMonFrameSize2Bound = _Sh1PerfMonFrameSize2Bound_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 2),
    _Sh1PerfMonFrameSize2Bound_Type()
)
sh1PerfMonFrameSize2Bound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sh1PerfMonFrameSize2Bound.setStatus("mandatory")
_Sh1PerfMonFrameSize3Bound_Type = Integer32
_Sh1PerfMonFrameSize3Bound_Object = MibScalar
sh1PerfMonFrameSize3Bound = _Sh1PerfMonFrameSize3Bound_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 3),
    _Sh1PerfMonFrameSize3Bound_Type()
)
sh1PerfMonFrameSize3Bound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sh1PerfMonFrameSize3Bound.setStatus("mandatory")
_Sh1PerfMonFrameSize4Bound_Type = Integer32
_Sh1PerfMonFrameSize4Bound_Object = MibScalar
sh1PerfMonFrameSize4Bound = _Sh1PerfMonFrameSize4Bound_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 4),
    _Sh1PerfMonFrameSize4Bound_Type()
)
sh1PerfMonFrameSize4Bound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sh1PerfMonFrameSize4Bound.setStatus("mandatory")
_Sh1PerfMonRelayCounts_Type = OctetString
_Sh1PerfMonRelayCounts_Object = MibScalar
sh1PerfMonRelayCounts = _Sh1PerfMonRelayCounts_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 5),
    _Sh1PerfMonRelayCounts_Type()
)
sh1PerfMonRelayCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonRelayCounts.setStatus("mandatory")
_Sh1PerfMonTotalFramesReceivedOk_Type = Counter32
_Sh1PerfMonTotalFramesReceivedOk_Object = MibScalar
sh1PerfMonTotalFramesReceivedOk = _Sh1PerfMonTotalFramesReceivedOk_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 6),
    _Sh1PerfMonTotalFramesReceivedOk_Type()
)
sh1PerfMonTotalFramesReceivedOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonTotalFramesReceivedOk.setStatus("mandatory")
_Sh1PerfMonTotalOctetsReceivedOk_Type = Counter32
_Sh1PerfMonTotalOctetsReceivedOk_Object = MibScalar
sh1PerfMonTotalOctetsReceivedOk = _Sh1PerfMonTotalOctetsReceivedOk_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 7),
    _Sh1PerfMonTotalOctetsReceivedOk_Type()
)
sh1PerfMonTotalOctetsReceivedOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonTotalOctetsReceivedOk.setStatus("mandatory")
_Sh1PerfMonTotalCollisions_Type = Counter32
_Sh1PerfMonTotalCollisions_Object = MibScalar
sh1PerfMonTotalCollisions = _Sh1PerfMonTotalCollisions_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 8),
    _Sh1PerfMonTotalCollisions_Type()
)
sh1PerfMonTotalCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonTotalCollisions.setStatus("mandatory")
_Sh1PerfMonTotalLateCollisions_Type = Counter32
_Sh1PerfMonTotalLateCollisions_Object = MibScalar
sh1PerfMonTotalLateCollisions = _Sh1PerfMonTotalLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 9),
    _Sh1PerfMonTotalLateCollisions_Type()
)
sh1PerfMonTotalLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonTotalLateCollisions.setStatus("mandatory")
_Sh1PerfMonTotalRunts_Type = Counter32
_Sh1PerfMonTotalRunts_Object = MibScalar
sh1PerfMonTotalRunts = _Sh1PerfMonTotalRunts_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 10),
    _Sh1PerfMonTotalRunts_Type()
)
sh1PerfMonTotalRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonTotalRunts.setStatus("mandatory")
_Sh1PerfMonTotalShortEvents_Type = Counter32
_Sh1PerfMonTotalShortEvents_Object = MibScalar
sh1PerfMonTotalShortEvents = _Sh1PerfMonTotalShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 11),
    _Sh1PerfMonTotalShortEvents_Type()
)
sh1PerfMonTotalShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonTotalShortEvents.setStatus("mandatory")
_Sh1PerfMonTotalFrameTooLongs_Type = Counter32
_Sh1PerfMonTotalFrameTooLongs_Object = MibScalar
sh1PerfMonTotalFrameTooLongs = _Sh1PerfMonTotalFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 12),
    _Sh1PerfMonTotalFrameTooLongs_Type()
)
sh1PerfMonTotalFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonTotalFrameTooLongs.setStatus("mandatory")
_Sh1PerfMonTotalAutoPartitions_Type = Counter32
_Sh1PerfMonTotalAutoPartitions_Object = MibScalar
sh1PerfMonTotalAutoPartitions = _Sh1PerfMonTotalAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 13),
    _Sh1PerfMonTotalAutoPartitions_Type()
)
sh1PerfMonTotalAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonTotalAutoPartitions.setStatus("mandatory")
_Sh1PerfMonTotalLongFragments_Type = Counter32
_Sh1PerfMonTotalLongFragments_Object = MibScalar
sh1PerfMonTotalLongFragments = _Sh1PerfMonTotalLongFragments_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 14),
    _Sh1PerfMonTotalLongFragments_Type()
)
sh1PerfMonTotalLongFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonTotalLongFragments.setStatus("mandatory")
_Sh1PerfMonTotalFifoErrors_Type = Counter32
_Sh1PerfMonTotalFifoErrors_Object = MibScalar
sh1PerfMonTotalFifoErrors = _Sh1PerfMonTotalFifoErrors_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 15),
    _Sh1PerfMonTotalFifoErrors_Type()
)
sh1PerfMonTotalFifoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonTotalFifoErrors.setStatus("mandatory")
_Sh1PerfMonTotalFramesTransmittedOk_Type = Counter32
_Sh1PerfMonTotalFramesTransmittedOk_Object = MibScalar
sh1PerfMonTotalFramesTransmittedOk = _Sh1PerfMonTotalFramesTransmittedOk_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 16),
    _Sh1PerfMonTotalFramesTransmittedOk_Type()
)
sh1PerfMonTotalFramesTransmittedOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonTotalFramesTransmittedOk.setStatus("mandatory")
_Sh1PerfMonTotalOctetsTransmittedOk_Type = Counter32
_Sh1PerfMonTotalOctetsTransmittedOk_Object = MibScalar
sh1PerfMonTotalOctetsTransmittedOk = _Sh1PerfMonTotalOctetsTransmittedOk_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 17),
    _Sh1PerfMonTotalOctetsTransmittedOk_Type()
)
sh1PerfMonTotalOctetsTransmittedOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonTotalOctetsTransmittedOk.setStatus("mandatory")
_Sh1PerfMonTotalErrorEnergy_Type = Counter32
_Sh1PerfMonTotalErrorEnergy_Object = MibScalar
sh1PerfMonTotalErrorEnergy = _Sh1PerfMonTotalErrorEnergy_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 18),
    _Sh1PerfMonTotalErrorEnergy_Type()
)
sh1PerfMonTotalErrorEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonTotalErrorEnergy.setStatus("mandatory")
_Sh1PerfMonTotalManchesterCodeViolations_Type = Counter32
_Sh1PerfMonTotalManchesterCodeViolations_Object = MibScalar
sh1PerfMonTotalManchesterCodeViolations = _Sh1PerfMonTotalManchesterCodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 19),
    _Sh1PerfMonTotalManchesterCodeViolations_Type()
)
sh1PerfMonTotalManchesterCodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonTotalManchesterCodeViolations.setStatus("mandatory")
_Sh1PerfMonTotalBand1Frames_Type = Counter32
_Sh1PerfMonTotalBand1Frames_Object = MibScalar
sh1PerfMonTotalBand1Frames = _Sh1PerfMonTotalBand1Frames_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 20),
    _Sh1PerfMonTotalBand1Frames_Type()
)
sh1PerfMonTotalBand1Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonTotalBand1Frames.setStatus("mandatory")
_Sh1PerfMonTotalBand2Frames_Type = Counter32
_Sh1PerfMonTotalBand2Frames_Object = MibScalar
sh1PerfMonTotalBand2Frames = _Sh1PerfMonTotalBand2Frames_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 21),
    _Sh1PerfMonTotalBand2Frames_Type()
)
sh1PerfMonTotalBand2Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonTotalBand2Frames.setStatus("mandatory")
_Sh1PerfMonTotalBand3Frames_Type = Counter32
_Sh1PerfMonTotalBand3Frames_Object = MibScalar
sh1PerfMonTotalBand3Frames = _Sh1PerfMonTotalBand3Frames_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 22),
    _Sh1PerfMonTotalBand3Frames_Type()
)
sh1PerfMonTotalBand3Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonTotalBand3Frames.setStatus("mandatory")
_Sh1PerfMonTotalBand4Frames_Type = Counter32
_Sh1PerfMonTotalBand4Frames_Object = MibScalar
sh1PerfMonTotalBand4Frames = _Sh1PerfMonTotalBand4Frames_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 23),
    _Sh1PerfMonTotalBand4Frames_Type()
)
sh1PerfMonTotalBand4Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonTotalBand4Frames.setStatus("mandatory")
_Sh1PerfMonTotalBand5Frames_Type = Counter32
_Sh1PerfMonTotalBand5Frames_Object = MibScalar
sh1PerfMonTotalBand5Frames = _Sh1PerfMonTotalBand5Frames_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 24),
    _Sh1PerfMonTotalBand5Frames_Type()
)
sh1PerfMonTotalBand5Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonTotalBand5Frames.setStatus("mandatory")
_Sh1PerfMonPortTable_Object = MibTable
sh1PerfMonPortTable = _Sh1PerfMonPortTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 25)
)
if mibBuilder.loadTexts:
    sh1PerfMonPortTable.setStatus("mandatory")
_Sh1PerfMonPortEntry_Object = MibTableRow
sh1PerfMonPortEntry = _Sh1PerfMonPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 25, 1)
)
sh1PerfMonPortEntry.setIndexNames(
    (0, "SH-ATT-MIB", "sh1PerfMonPortID"),
)
if mibBuilder.loadTexts:
    sh1PerfMonPortEntry.setStatus("mandatory")
_Sh1PerfMonPortID_Type = Integer32
_Sh1PerfMonPortID_Object = MibTableColumn
sh1PerfMonPortID = _Sh1PerfMonPortID_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 25, 1, 1),
    _Sh1PerfMonPortID_Type()
)
sh1PerfMonPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonPortID.setStatus("mandatory")
_Sh1PerfMonPortCounts_Type = OctetString
_Sh1PerfMonPortCounts_Object = MibTableColumn
sh1PerfMonPortCounts = _Sh1PerfMonPortCounts_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 25, 1, 2),
    _Sh1PerfMonPortCounts_Type()
)
sh1PerfMonPortCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonPortCounts.setStatus("mandatory")
_Sh1PerfMonFramesReceivedOk_Type = Counter32
_Sh1PerfMonFramesReceivedOk_Object = MibTableColumn
sh1PerfMonFramesReceivedOk = _Sh1PerfMonFramesReceivedOk_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 25, 1, 3),
    _Sh1PerfMonFramesReceivedOk_Type()
)
sh1PerfMonFramesReceivedOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonFramesReceivedOk.setStatus("mandatory")
_Sh1PerfMonOctetsReceivedOk_Type = Counter32
_Sh1PerfMonOctetsReceivedOk_Object = MibTableColumn
sh1PerfMonOctetsReceivedOk = _Sh1PerfMonOctetsReceivedOk_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 25, 1, 4),
    _Sh1PerfMonOctetsReceivedOk_Type()
)
sh1PerfMonOctetsReceivedOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonOctetsReceivedOk.setStatus("mandatory")
_Sh1PerfMonCollisions_Type = Counter32
_Sh1PerfMonCollisions_Object = MibTableColumn
sh1PerfMonCollisions = _Sh1PerfMonCollisions_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 25, 1, 5),
    _Sh1PerfMonCollisions_Type()
)
sh1PerfMonCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonCollisions.setStatus("mandatory")
_Sh1PerfMonLateCollisions_Type = Counter32
_Sh1PerfMonLateCollisions_Object = MibTableColumn
sh1PerfMonLateCollisions = _Sh1PerfMonLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 25, 1, 6),
    _Sh1PerfMonLateCollisions_Type()
)
sh1PerfMonLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonLateCollisions.setStatus("mandatory")
_Sh1PerfMonRunts_Type = Counter32
_Sh1PerfMonRunts_Object = MibTableColumn
sh1PerfMonRunts = _Sh1PerfMonRunts_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 25, 1, 7),
    _Sh1PerfMonRunts_Type()
)
sh1PerfMonRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonRunts.setStatus("mandatory")
_Sh1PerfMonShortEvents_Type = Counter32
_Sh1PerfMonShortEvents_Object = MibTableColumn
sh1PerfMonShortEvents = _Sh1PerfMonShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 25, 1, 8),
    _Sh1PerfMonShortEvents_Type()
)
sh1PerfMonShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonShortEvents.setStatus("mandatory")
_Sh1PerfMonFrameTooLongs_Type = Counter32
_Sh1PerfMonFrameTooLongs_Object = MibTableColumn
sh1PerfMonFrameTooLongs = _Sh1PerfMonFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 25, 1, 9),
    _Sh1PerfMonFrameTooLongs_Type()
)
sh1PerfMonFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonFrameTooLongs.setStatus("mandatory")
_Sh1PerfMonAutoPartitions_Type = Counter32
_Sh1PerfMonAutoPartitions_Object = MibTableColumn
sh1PerfMonAutoPartitions = _Sh1PerfMonAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 25, 1, 10),
    _Sh1PerfMonAutoPartitions_Type()
)
sh1PerfMonAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonAutoPartitions.setStatus("mandatory")
_Sh1PerfMonLongFragments_Type = Counter32
_Sh1PerfMonLongFragments_Object = MibTableColumn
sh1PerfMonLongFragments = _Sh1PerfMonLongFragments_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 25, 1, 11),
    _Sh1PerfMonLongFragments_Type()
)
sh1PerfMonLongFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonLongFragments.setStatus("mandatory")
_Sh1PerfMonFifoErrors_Type = Counter32
_Sh1PerfMonFifoErrors_Object = MibTableColumn
sh1PerfMonFifoErrors = _Sh1PerfMonFifoErrors_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 25, 1, 12),
    _Sh1PerfMonFifoErrors_Type()
)
sh1PerfMonFifoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonFifoErrors.setStatus("mandatory")
_Sh1PerfMonFramesTransmittedOk_Type = Counter32
_Sh1PerfMonFramesTransmittedOk_Object = MibTableColumn
sh1PerfMonFramesTransmittedOk = _Sh1PerfMonFramesTransmittedOk_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 25, 1, 13),
    _Sh1PerfMonFramesTransmittedOk_Type()
)
sh1PerfMonFramesTransmittedOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonFramesTransmittedOk.setStatus("mandatory")
_Sh1PerfMonOctetsTransmittedOk_Type = Counter32
_Sh1PerfMonOctetsTransmittedOk_Object = MibTableColumn
sh1PerfMonOctetsTransmittedOk = _Sh1PerfMonOctetsTransmittedOk_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 25, 1, 14),
    _Sh1PerfMonOctetsTransmittedOk_Type()
)
sh1PerfMonOctetsTransmittedOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonOctetsTransmittedOk.setStatus("mandatory")
_Sh1PerfMonErrorEnergy_Type = Counter32
_Sh1PerfMonErrorEnergy_Object = MibTableColumn
sh1PerfMonErrorEnergy = _Sh1PerfMonErrorEnergy_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 25, 1, 15),
    _Sh1PerfMonErrorEnergy_Type()
)
sh1PerfMonErrorEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonErrorEnergy.setStatus("mandatory")
_Sh1PerfMonManchesterCodeViolations_Type = Counter32
_Sh1PerfMonManchesterCodeViolations_Object = MibTableColumn
sh1PerfMonManchesterCodeViolations = _Sh1PerfMonManchesterCodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 25, 1, 16),
    _Sh1PerfMonManchesterCodeViolations_Type()
)
sh1PerfMonManchesterCodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonManchesterCodeViolations.setStatus("mandatory")
_Sh1PerfMonBand1Frames_Type = Counter32
_Sh1PerfMonBand1Frames_Object = MibTableColumn
sh1PerfMonBand1Frames = _Sh1PerfMonBand1Frames_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 25, 1, 17),
    _Sh1PerfMonBand1Frames_Type()
)
sh1PerfMonBand1Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonBand1Frames.setStatus("mandatory")
_Sh1PerfMonBand2Frames_Type = Counter32
_Sh1PerfMonBand2Frames_Object = MibTableColumn
sh1PerfMonBand2Frames = _Sh1PerfMonBand2Frames_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 25, 1, 18),
    _Sh1PerfMonBand2Frames_Type()
)
sh1PerfMonBand2Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonBand2Frames.setStatus("mandatory")
_Sh1PerfMonBand3Frames_Type = Counter32
_Sh1PerfMonBand3Frames_Object = MibTableColumn
sh1PerfMonBand3Frames = _Sh1PerfMonBand3Frames_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 25, 1, 19),
    _Sh1PerfMonBand3Frames_Type()
)
sh1PerfMonBand3Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonBand3Frames.setStatus("mandatory")
_Sh1PerfMonBand4Frames_Type = Counter32
_Sh1PerfMonBand4Frames_Object = MibTableColumn
sh1PerfMonBand4Frames = _Sh1PerfMonBand4Frames_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 25, 1, 20),
    _Sh1PerfMonBand4Frames_Type()
)
sh1PerfMonBand4Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonBand4Frames.setStatus("mandatory")
_Sh1PerfMonBand5Frames_Type = Counter32
_Sh1PerfMonBand5Frames_Object = MibTableColumn
sh1PerfMonBand5Frames = _Sh1PerfMonBand5Frames_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 3, 25, 1, 21),
    _Sh1PerfMonBand5Frames_Type()
)
sh1PerfMonBand5Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1PerfMonBand5Frames.setStatus("mandatory")
_Sh1DownloadCapability_ObjectIdentity = ObjectIdentity
sh1DownloadCapability = _Sh1DownloadCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 4)
)
_Sh1DownloadImageFile_Type = OctetString
_Sh1DownloadImageFile_Object = MibScalar
sh1DownloadImageFile = _Sh1DownloadImageFile_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 4, 1),
    _Sh1DownloadImageFile_Type()
)
sh1DownloadImageFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sh1DownloadImageFile.setStatus("mandatory")
_Sh1DownloadIpAddress_Type = IpAddress
_Sh1DownloadIpAddress_Object = MibScalar
sh1DownloadIpAddress = _Sh1DownloadIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 4, 2),
    _Sh1DownloadIpAddress_Type()
)
sh1DownloadIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sh1DownloadIpAddress.setStatus("mandatory")
_Sh1DownloadMacAddress_Type = OctetString
_Sh1DownloadMacAddress_Object = MibScalar
sh1DownloadMacAddress = _Sh1DownloadMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 4, 3),
    _Sh1DownloadMacAddress_Type()
)
sh1DownloadMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sh1DownloadMacAddress.setStatus("mandatory")


class _Sh1DownloadExecute_Type(Integer32):
    """Custom type sh1DownloadExecute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("performDownload", 1)
    )


_Sh1DownloadExecute_Type.__name__ = "Integer32"
_Sh1DownloadExecute_Object = MibScalar
sh1DownloadExecute = _Sh1DownloadExecute_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 4, 4),
    _Sh1DownloadExecute_Type()
)
sh1DownloadExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sh1DownloadExecute.setStatus("mandatory")
_Sh1AddrTrackCapability_ObjectIdentity = ObjectIdentity
sh1AddrTrackCapability = _Sh1AddrTrackCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 5)
)


class _Sh1AddrTrackSendHubLearn_Type(Integer32):
    """Custom type sh1AddrTrackSendHubLearn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("sendHubLearnFrame", 1)
    )


_Sh1AddrTrackSendHubLearn_Type.__name__ = "Integer32"
_Sh1AddrTrackSendHubLearn_Object = MibScalar
sh1AddrTrackSendHubLearn = _Sh1AddrTrackSendHubLearn_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 5, 1),
    _Sh1AddrTrackSendHubLearn_Type()
)
sh1AddrTrackSendHubLearn.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sh1AddrTrackSendHubLearn.setStatus("mandatory")
_Sh1AddrTrackPortTable_Object = MibTable
sh1AddrTrackPortTable = _Sh1AddrTrackPortTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    sh1AddrTrackPortTable.setStatus("mandatory")
_Sh1AddrTrackPortEntry_Object = MibTableRow
sh1AddrTrackPortEntry = _Sh1AddrTrackPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 5, 2, 1)
)
sh1AddrTrackPortEntry.setIndexNames(
    (0, "SH-ATT-MIB", "sh1AddrTrackPortID"),
)
if mibBuilder.loadTexts:
    sh1AddrTrackPortEntry.setStatus("mandatory")
_Sh1AddrTrackPortID_Type = Integer32
_Sh1AddrTrackPortID_Object = MibTableColumn
sh1AddrTrackPortID = _Sh1AddrTrackPortID_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 5, 2, 1, 1),
    _Sh1AddrTrackPortID_Type()
)
sh1AddrTrackPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1AddrTrackPortID.setStatus("mandatory")
_Sh1AddrTrackDetectedMacAddr_Type = OctetString
_Sh1AddrTrackDetectedMacAddr_Object = MibTableColumn
sh1AddrTrackDetectedMacAddr = _Sh1AddrTrackDetectedMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 5, 2, 1, 2),
    _Sh1AddrTrackDetectedMacAddr_Type()
)
sh1AddrTrackDetectedMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1AddrTrackDetectedMacAddr.setStatus("mandatory")


class _Sh1AddrTrackDetectedAddrType_Type(Integer32):
    """Custom type sh1AddrTrackDetectedAddrType based on Integer32"""
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
        *(("hubAddress", 3),
          ("multipleAddresses", 4),
          ("none", 1),
          ("singleAddress", 2))
    )


_Sh1AddrTrackDetectedAddrType_Type.__name__ = "Integer32"
_Sh1AddrTrackDetectedAddrType_Object = MibTableColumn
sh1AddrTrackDetectedAddrType = _Sh1AddrTrackDetectedAddrType_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 5, 2, 1, 3),
    _Sh1AddrTrackDetectedAddrType_Type()
)
sh1AddrTrackDetectedAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1AddrTrackDetectedAddrType.setStatus("mandatory")
_Sh1AddrTrackAuthMacAddr_Type = OctetString
_Sh1AddrTrackAuthMacAddr_Object = MibTableColumn
sh1AddrTrackAuthMacAddr = _Sh1AddrTrackAuthMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 5, 2, 1, 4),
    _Sh1AddrTrackAuthMacAddr_Type()
)
sh1AddrTrackAuthMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sh1AddrTrackAuthMacAddr.setStatus("mandatory")


class _Sh1AddrTrackAuthAddrType_Type(Integer32):
    """Custom type sh1AddrTrackAuthAddrType based on Integer32"""
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
        *(("hubAddress", 3),
          ("multipleAddresses", 4),
          ("none", 1),
          ("singleAddress", 2))
    )


_Sh1AddrTrackAuthAddrType_Type.__name__ = "Integer32"
_Sh1AddrTrackAuthAddrType_Object = MibTableColumn
sh1AddrTrackAuthAddrType = _Sh1AddrTrackAuthAddrType_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 5, 2, 1, 5),
    _Sh1AddrTrackAuthAddrType_Type()
)
sh1AddrTrackAuthAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sh1AddrTrackAuthAddrType.setStatus("mandatory")
_Sh1AddrTrackNewHubAddr_Type = OctetString
_Sh1AddrTrackNewHubAddr_Object = MibTableColumn
sh1AddrTrackNewHubAddr = _Sh1AddrTrackNewHubAddr_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 5, 2, 1, 6),
    _Sh1AddrTrackNewHubAddr_Type()
)
sh1AddrTrackNewHubAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sh1AddrTrackNewHubAddr.setStatus("mandatory")
_Sh1EnhancedCtrlCapability_ObjectIdentity = ObjectIdentity
sh1EnhancedCtrlCapability = _Sh1EnhancedCtrlCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 6)
)


class _Sh1EnhCtrlResetFirmwareConfig_Type(Integer32):
    """Custom type sh1EnhCtrlResetFirmwareConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("performReset", 1)
    )


_Sh1EnhCtrlResetFirmwareConfig_Type.__name__ = "Integer32"
_Sh1EnhCtrlResetFirmwareConfig_Object = MibScalar
sh1EnhCtrlResetFirmwareConfig = _Sh1EnhCtrlResetFirmwareConfig_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 6, 1),
    _Sh1EnhCtrlResetFirmwareConfig_Type()
)
sh1EnhCtrlResetFirmwareConfig.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sh1EnhCtrlResetFirmwareConfig.setStatus("mandatory")
_Sh1EnhCtrlHubVersion_Type = OctetString
_Sh1EnhCtrlHubVersion_Object = MibScalar
sh1EnhCtrlHubVersion = _Sh1EnhCtrlHubVersion_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 6, 2),
    _Sh1EnhCtrlHubVersion_Type()
)
sh1EnhCtrlHubVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1EnhCtrlHubVersion.setStatus("mandatory")
_Sh1EnhCtrlTrapMacAddr_Type = OctetString
_Sh1EnhCtrlTrapMacAddr_Object = MibScalar
sh1EnhCtrlTrapMacAddr = _Sh1EnhCtrlTrapMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 6, 3),
    _Sh1EnhCtrlTrapMacAddr_Type()
)
sh1EnhCtrlTrapMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sh1EnhCtrlTrapMacAddr.setStatus("mandatory")
_Sh1EnhCtrlTrapIpAddr_Type = IpAddress
_Sh1EnhCtrlTrapIpAddr_Object = MibScalar
sh1EnhCtrlTrapIpAddr = _Sh1EnhCtrlTrapIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 6, 4),
    _Sh1EnhCtrlTrapIpAddr_Type()
)
sh1EnhCtrlTrapIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sh1EnhCtrlTrapIpAddr.setStatus("mandatory")
_Sh1EnhCtrlGatewayIpAddr_Type = IpAddress
_Sh1EnhCtrlGatewayIpAddr_Object = MibScalar
sh1EnhCtrlGatewayIpAddr = _Sh1EnhCtrlGatewayIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 6, 5),
    _Sh1EnhCtrlGatewayIpAddr_Type()
)
sh1EnhCtrlGatewayIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sh1EnhCtrlGatewayIpAddr.setStatus("mandatory")
_Sh1EnhCtrlNetworkMask_Type = IpAddress
_Sh1EnhCtrlNetworkMask_Object = MibScalar
sh1EnhCtrlNetworkMask = _Sh1EnhCtrlNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 6, 6),
    _Sh1EnhCtrlNetworkMask_Type()
)
sh1EnhCtrlNetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sh1EnhCtrlNetworkMask.setStatus("mandatory")
_Sh1EnhCtrlHubIpAddr_Type = IpAddress
_Sh1EnhCtrlHubIpAddr_Object = MibScalar
sh1EnhCtrlHubIpAddr = _Sh1EnhCtrlHubIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 6, 7),
    _Sh1EnhCtrlHubIpAddr_Type()
)
sh1EnhCtrlHubIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sh1EnhCtrlHubIpAddr.setStatus("mandatory")
_Sh1EnhCtrlHubAlias_Type = DisplayString
_Sh1EnhCtrlHubAlias_Object = MibScalar
sh1EnhCtrlHubAlias = _Sh1EnhCtrlHubAlias_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 6, 8),
    _Sh1EnhCtrlHubAlias_Type()
)
sh1EnhCtrlHubAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sh1EnhCtrlHubAlias.setStatus("mandatory")


class _Sh1EnhCtrlRs232State_Type(Integer32):
    """Custom type sh1EnhCtrlRs232State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dteConnectedLoggedIn", 3),
          ("dteConnectedNotLoggedIn", 2),
          ("dteNotConnected", 1))
    )


_Sh1EnhCtrlRs232State_Type.__name__ = "Integer32"
_Sh1EnhCtrlRs232State_Object = MibScalar
sh1EnhCtrlRs232State = _Sh1EnhCtrlRs232State_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 6, 9),
    _Sh1EnhCtrlRs232State_Type()
)
sh1EnhCtrlRs232State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1EnhCtrlRs232State.setStatus("mandatory")


class _Sh1EnhCtrlRs232DataRate_Type(Integer32):
    """Custom type sh1EnhCtrlRs232DataRate based on Integer32"""
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
        *(("bps1200", 2),
          ("bps2400", 3),
          ("bps300", 1),
          ("bps4800", 4),
          ("bps9600", 5))
    )


_Sh1EnhCtrlRs232DataRate_Type.__name__ = "Integer32"
_Sh1EnhCtrlRs232DataRate_Object = MibScalar
sh1EnhCtrlRs232DataRate = _Sh1EnhCtrlRs232DataRate_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 6, 10),
    _Sh1EnhCtrlRs232DataRate_Type()
)
sh1EnhCtrlRs232DataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sh1EnhCtrlRs232DataRate.setStatus("mandatory")
_Sh1EnhCtrlTrapCountPeriodCtrl_Type = Integer32
_Sh1EnhCtrlTrapCountPeriodCtrl_Object = MibScalar
sh1EnhCtrlTrapCountPeriodCtrl = _Sh1EnhCtrlTrapCountPeriodCtrl_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 6, 11),
    _Sh1EnhCtrlTrapCountPeriodCtrl_Type()
)
sh1EnhCtrlTrapCountPeriodCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sh1EnhCtrlTrapCountPeriodCtrl.setStatus("mandatory")


class _Sh1EnhCtrlTrapCountContentsCtrl_Type(Integer32):
    """Custom type sh1EnhCtrlTrapCountContentsCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullContents", 3),
          ("minimumContents", 2),
          ("other", 1))
    )


_Sh1EnhCtrlTrapCountContentsCtrl_Type.__name__ = "Integer32"
_Sh1EnhCtrlTrapCountContentsCtrl_Object = MibScalar
sh1EnhCtrlTrapCountContentsCtrl = _Sh1EnhCtrlTrapCountContentsCtrl_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 6, 12),
    _Sh1EnhCtrlTrapCountContentsCtrl_Type()
)
sh1EnhCtrlTrapCountContentsCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sh1EnhCtrlTrapCountContentsCtrl.setStatus("mandatory")


class _Sh1EnhCtrlSendTrapConfig_Type(Integer32):
    """Custom type sh1EnhCtrlSendTrapConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("sendTrapConfig", 1)
    )


_Sh1EnhCtrlSendTrapConfig_Type.__name__ = "Integer32"
_Sh1EnhCtrlSendTrapConfig_Object = MibScalar
sh1EnhCtrlSendTrapConfig = _Sh1EnhCtrlSendTrapConfig_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 6, 13),
    _Sh1EnhCtrlSendTrapConfig_Type()
)
sh1EnhCtrlSendTrapConfig.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sh1EnhCtrlSendTrapConfig.setStatus("mandatory")
_Sh1EnhCtrlPortTable_Object = MibTable
sh1EnhCtrlPortTable = _Sh1EnhCtrlPortTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 6, 14)
)
if mibBuilder.loadTexts:
    sh1EnhCtrlPortTable.setStatus("mandatory")
_Sh1EnhCtrlPortEntry_Object = MibTableRow
sh1EnhCtrlPortEntry = _Sh1EnhCtrlPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 6, 14, 1)
)
sh1EnhCtrlPortEntry.setIndexNames(
    (0, "SH-ATT-MIB", "sh1EnhCtrlPortID"),
)
if mibBuilder.loadTexts:
    sh1EnhCtrlPortEntry.setStatus("mandatory")
_Sh1EnhCtrlPortID_Type = Integer32
_Sh1EnhCtrlPortID_Object = MibTableColumn
sh1EnhCtrlPortID = _Sh1EnhCtrlPortID_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 6, 14, 1, 1),
    _Sh1EnhCtrlPortID_Type()
)
sh1EnhCtrlPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1EnhCtrlPortID.setStatus("mandatory")


class _Sh1EnhCtrlLinkIntegrityCtrl_Type(Integer32):
    """Custom type sh1EnhCtrlLinkIntegrityCtrl based on Integer32"""
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


_Sh1EnhCtrlLinkIntegrityCtrl_Type.__name__ = "Integer32"
_Sh1EnhCtrlLinkIntegrityCtrl_Object = MibTableColumn
sh1EnhCtrlLinkIntegrityCtrl = _Sh1EnhCtrlLinkIntegrityCtrl_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 6, 14, 1, 2),
    _Sh1EnhCtrlLinkIntegrityCtrl_Type()
)
sh1EnhCtrlLinkIntegrityCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sh1EnhCtrlLinkIntegrityCtrl.setStatus("mandatory")


class _Sh1EnhCtrlLinkIntegrityAlarmCtrl_Type(Integer32):
    """Custom type sh1EnhCtrlLinkIntegrityAlarmCtrl based on Integer32"""
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


_Sh1EnhCtrlLinkIntegrityAlarmCtrl_Type.__name__ = "Integer32"
_Sh1EnhCtrlLinkIntegrityAlarmCtrl_Object = MibTableColumn
sh1EnhCtrlLinkIntegrityAlarmCtrl = _Sh1EnhCtrlLinkIntegrityAlarmCtrl_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 6, 14, 1, 3),
    _Sh1EnhCtrlLinkIntegrityAlarmCtrl_Type()
)
sh1EnhCtrlLinkIntegrityAlarmCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sh1EnhCtrlLinkIntegrityAlarmCtrl.setStatus("mandatory")


class _Sh1EnhCtrlLinkIntegrityState_Type(Integer32):
    """Custom type sh1EnhCtrlLinkIntegrityState based on Integer32"""
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
          ("notApplicable", 1))
    )


_Sh1EnhCtrlLinkIntegrityState_Type.__name__ = "Integer32"
_Sh1EnhCtrlLinkIntegrityState_Object = MibTableColumn
sh1EnhCtrlLinkIntegrityState = _Sh1EnhCtrlLinkIntegrityState_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 6, 14, 1, 4),
    _Sh1EnhCtrlLinkIntegrityState_Type()
)
sh1EnhCtrlLinkIntegrityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1EnhCtrlLinkIntegrityState.setStatus("mandatory")


class _Sh1EnhCtrlExtendedDistanceCtrl_Type(Integer32):
    """Custom type sh1EnhCtrlExtendedDistanceCtrl based on Integer32"""
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


_Sh1EnhCtrlExtendedDistanceCtrl_Type.__name__ = "Integer32"
_Sh1EnhCtrlExtendedDistanceCtrl_Object = MibTableColumn
sh1EnhCtrlExtendedDistanceCtrl = _Sh1EnhCtrlExtendedDistanceCtrl_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 6, 14, 1, 5),
    _Sh1EnhCtrlExtendedDistanceCtrl_Type()
)
sh1EnhCtrlExtendedDistanceCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sh1EnhCtrlExtendedDistanceCtrl.setStatus("mandatory")
_Sh1EnhCtrlPortConfig_Type = OctetString
_Sh1EnhCtrlPortConfig_Object = MibTableColumn
sh1EnhCtrlPortConfig = _Sh1EnhCtrlPortConfig_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 6, 14, 1, 6),
    _Sh1EnhCtrlPortConfig_Type()
)
sh1EnhCtrlPortConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1EnhCtrlPortConfig.setStatus("mandatory")
_Sh1SecurityCapability_ObjectIdentity = ObjectIdentity
sh1SecurityCapability = _Sh1SecurityCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 7)
)


class _Sh1SecEavesdroppingCtrl_Type(Integer32):
    """Custom type sh1SecEavesdroppingCtrl based on Integer32"""
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


_Sh1SecEavesdroppingCtrl_Type.__name__ = "Integer32"
_Sh1SecEavesdroppingCtrl_Object = MibScalar
sh1SecEavesdroppingCtrl = _Sh1SecEavesdroppingCtrl_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 7, 1),
    _Sh1SecEavesdroppingCtrl_Type()
)
sh1SecEavesdroppingCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sh1SecEavesdroppingCtrl.setStatus("mandatory")


class _Sh1SecIntrusionCtrl_Type(Integer32):
    """Custom type sh1SecIntrusionCtrl based on Integer32"""
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


_Sh1SecIntrusionCtrl_Type.__name__ = "Integer32"
_Sh1SecIntrusionCtrl_Object = MibScalar
sh1SecIntrusionCtrl = _Sh1SecIntrusionCtrl_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 7, 2),
    _Sh1SecIntrusionCtrl_Type()
)
sh1SecIntrusionCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sh1SecIntrusionCtrl.setStatus("mandatory")


class _Sh1SecIntrusionAlarmCtrl_Type(Integer32):
    """Custom type sh1SecIntrusionAlarmCtrl based on Integer32"""
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


_Sh1SecIntrusionAlarmCtrl_Type.__name__ = "Integer32"
_Sh1SecIntrusionAlarmCtrl_Object = MibScalar
sh1SecIntrusionAlarmCtrl = _Sh1SecIntrusionAlarmCtrl_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 7, 3),
    _Sh1SecIntrusionAlarmCtrl_Type()
)
sh1SecIntrusionAlarmCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sh1SecIntrusionAlarmCtrl.setStatus("mandatory")
_Sh1SecPassword_Type = OctetString
_Sh1SecPassword_Object = MibScalar
sh1SecPassword = _Sh1SecPassword_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 7, 4),
    _Sh1SecPassword_Type()
)
sh1SecPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sh1SecPassword.setStatus("mandatory")
_Sh1SecBadPasswords_Type = Counter32
_Sh1SecBadPasswords_Object = MibScalar
sh1SecBadPasswords = _Sh1SecBadPasswords_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 7, 5),
    _Sh1SecBadPasswords_Type()
)
sh1SecBadPasswords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1SecBadPasswords.setStatus("mandatory")
_Sh1SecSettingAdminMacAddr_Type = OctetString
_Sh1SecSettingAdminMacAddr_Object = MibScalar
sh1SecSettingAdminMacAddr = _Sh1SecSettingAdminMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 7, 6),
    _Sh1SecSettingAdminMacAddr_Type()
)
sh1SecSettingAdminMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1SecSettingAdminMacAddr.setStatus("mandatory")
_Sh1SecSettingAdminIpAddr_Type = IpAddress
_Sh1SecSettingAdminIpAddr_Object = MibScalar
sh1SecSettingAdminIpAddr = _Sh1SecSettingAdminIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 7, 7),
    _Sh1SecSettingAdminIpAddr_Type()
)
sh1SecSettingAdminIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1SecSettingAdminIpAddr.setStatus("mandatory")


class _Sh1SecInbandSetsState_Type(Integer32):
    """Custom type sh1SecInbandSetsState based on Integer32"""
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


_Sh1SecInbandSetsState_Type.__name__ = "Integer32"
_Sh1SecInbandSetsState_Object = MibScalar
sh1SecInbandSetsState = _Sh1SecInbandSetsState_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 7, 8),
    _Sh1SecInbandSetsState_Type()
)
sh1SecInbandSetsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1SecInbandSetsState.setStatus("mandatory")
_Sh1SecPortTable_Object = MibTable
sh1SecPortTable = _Sh1SecPortTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 7, 9)
)
if mibBuilder.loadTexts:
    sh1SecPortTable.setStatus("mandatory")
_Sh1SecPortEntry_Object = MibTableRow
sh1SecPortEntry = _Sh1SecPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 7, 9, 1)
)
sh1SecPortEntry.setIndexNames(
    (0, "SH-ATT-MIB", "sh1SecPortID"),
)
if mibBuilder.loadTexts:
    sh1SecPortEntry.setStatus("mandatory")
_Sh1SecPortID_Type = Integer32
_Sh1SecPortID_Object = MibTableColumn
sh1SecPortID = _Sh1SecPortID_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 7, 9, 1, 1),
    _Sh1SecPortID_Type()
)
sh1SecPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1SecPortID.setStatus("mandatory")
_Sh1SecIntrusionAddr_Type = OctetString
_Sh1SecIntrusionAddr_Object = MibTableColumn
sh1SecIntrusionAddr = _Sh1SecIntrusionAddr_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 7, 9, 1, 2),
    _Sh1SecIntrusionAddr_Type()
)
sh1SecIntrusionAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1SecIntrusionAddr.setStatus("mandatory")
_Sh1SecIntrusionTimeStamp_Type = TimeTicks
_Sh1SecIntrusionTimeStamp_Object = MibTableColumn
sh1SecIntrusionTimeStamp = _Sh1SecIntrusionTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 7, 9, 1, 3),
    _Sh1SecIntrusionTimeStamp_Type()
)
sh1SecIntrusionTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1SecIntrusionTimeStamp.setStatus("mandatory")
_Sh1SecIntrusions_Type = Counter32
_Sh1SecIntrusions_Object = MibTableColumn
sh1SecIntrusions = _Sh1SecIntrusions_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 1, 7, 9, 1, 4),
    _Sh1SecIntrusions_Type()
)
sh1SecIntrusions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sh1SecIntrusions.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SH-ATT-MIB",
    **{"att-2": att_2,
       "att-products": att_products,
       "att-hubmgtProd": att_hubmgtProd,
       "att-mgmt": att_mgmt,
       "att-hubmgt": att_hubmgt,
       "sh1BasicCtrlCapability": sh1BasicCtrlCapability,
       "sh1BasicCtrlHubID": sh1BasicCtrlHubID,
       "sh1BasicCtrlHubGroupCapacity": sh1BasicCtrlHubGroupCapacity,
       "sh1BasicCtrlGroupMap": sh1BasicCtrlGroupMap,
       "sh1BasicCtrlGroupID": sh1BasicCtrlGroupID,
       "sh1BasicCtrlNumberOfPorts": sh1BasicCtrlNumberOfPorts,
       "sh1BasicCtrlPortTable": sh1BasicCtrlPortTable,
       "sh1BasicCtrlPortEntry": sh1BasicCtrlPortEntry,
       "sh1BasicCtrlPortID": sh1BasicCtrlPortID,
       "sh1BasicCtrlPortType": sh1BasicCtrlPortType,
       "sh1BasicCtrlPortCtrl": sh1BasicCtrlPortCtrl,
       "sh1BasicCtrlAutoPartitionState": sh1BasicCtrlAutoPartitionState,
       "sh1SelfTestCapability": sh1SelfTestCapability,
       "sh1SelfTestHubResetTimeStamp": sh1SelfTestHubResetTimeStamp,
       "sh1SelfTestResetHubSystem": sh1SelfTestResetHubSystem,
       "sh1SelfTestResetHub": sh1SelfTestResetHub,
       "sh1SelfTestExecuteSelfTest1": sh1SelfTestExecuteSelfTest1,
       "sh1SelfTestExecuteSelfTest2": sh1SelfTestExecuteSelfTest2,
       "sh1SelfTestHubHealthState": sh1SelfTestHubHealthState,
       "sh1SelfTestHubHealthData": sh1SelfTestHubHealthData,
       "sh1PerfMonCapability": sh1PerfMonCapability,
       "sh1PerfMonFrameSize1Bound": sh1PerfMonFrameSize1Bound,
       "sh1PerfMonFrameSize2Bound": sh1PerfMonFrameSize2Bound,
       "sh1PerfMonFrameSize3Bound": sh1PerfMonFrameSize3Bound,
       "sh1PerfMonFrameSize4Bound": sh1PerfMonFrameSize4Bound,
       "sh1PerfMonRelayCounts": sh1PerfMonRelayCounts,
       "sh1PerfMonTotalFramesReceivedOk": sh1PerfMonTotalFramesReceivedOk,
       "sh1PerfMonTotalOctetsReceivedOk": sh1PerfMonTotalOctetsReceivedOk,
       "sh1PerfMonTotalCollisions": sh1PerfMonTotalCollisions,
       "sh1PerfMonTotalLateCollisions": sh1PerfMonTotalLateCollisions,
       "sh1PerfMonTotalRunts": sh1PerfMonTotalRunts,
       "sh1PerfMonTotalShortEvents": sh1PerfMonTotalShortEvents,
       "sh1PerfMonTotalFrameTooLongs": sh1PerfMonTotalFrameTooLongs,
       "sh1PerfMonTotalAutoPartitions": sh1PerfMonTotalAutoPartitions,
       "sh1PerfMonTotalLongFragments": sh1PerfMonTotalLongFragments,
       "sh1PerfMonTotalFifoErrors": sh1PerfMonTotalFifoErrors,
       "sh1PerfMonTotalFramesTransmittedOk": sh1PerfMonTotalFramesTransmittedOk,
       "sh1PerfMonTotalOctetsTransmittedOk": sh1PerfMonTotalOctetsTransmittedOk,
       "sh1PerfMonTotalErrorEnergy": sh1PerfMonTotalErrorEnergy,
       "sh1PerfMonTotalManchesterCodeViolations": sh1PerfMonTotalManchesterCodeViolations,
       "sh1PerfMonTotalBand1Frames": sh1PerfMonTotalBand1Frames,
       "sh1PerfMonTotalBand2Frames": sh1PerfMonTotalBand2Frames,
       "sh1PerfMonTotalBand3Frames": sh1PerfMonTotalBand3Frames,
       "sh1PerfMonTotalBand4Frames": sh1PerfMonTotalBand4Frames,
       "sh1PerfMonTotalBand5Frames": sh1PerfMonTotalBand5Frames,
       "sh1PerfMonPortTable": sh1PerfMonPortTable,
       "sh1PerfMonPortEntry": sh1PerfMonPortEntry,
       "sh1PerfMonPortID": sh1PerfMonPortID,
       "sh1PerfMonPortCounts": sh1PerfMonPortCounts,
       "sh1PerfMonFramesReceivedOk": sh1PerfMonFramesReceivedOk,
       "sh1PerfMonOctetsReceivedOk": sh1PerfMonOctetsReceivedOk,
       "sh1PerfMonCollisions": sh1PerfMonCollisions,
       "sh1PerfMonLateCollisions": sh1PerfMonLateCollisions,
       "sh1PerfMonRunts": sh1PerfMonRunts,
       "sh1PerfMonShortEvents": sh1PerfMonShortEvents,
       "sh1PerfMonFrameTooLongs": sh1PerfMonFrameTooLongs,
       "sh1PerfMonAutoPartitions": sh1PerfMonAutoPartitions,
       "sh1PerfMonLongFragments": sh1PerfMonLongFragments,
       "sh1PerfMonFifoErrors": sh1PerfMonFifoErrors,
       "sh1PerfMonFramesTransmittedOk": sh1PerfMonFramesTransmittedOk,
       "sh1PerfMonOctetsTransmittedOk": sh1PerfMonOctetsTransmittedOk,
       "sh1PerfMonErrorEnergy": sh1PerfMonErrorEnergy,
       "sh1PerfMonManchesterCodeViolations": sh1PerfMonManchesterCodeViolations,
       "sh1PerfMonBand1Frames": sh1PerfMonBand1Frames,
       "sh1PerfMonBand2Frames": sh1PerfMonBand2Frames,
       "sh1PerfMonBand3Frames": sh1PerfMonBand3Frames,
       "sh1PerfMonBand4Frames": sh1PerfMonBand4Frames,
       "sh1PerfMonBand5Frames": sh1PerfMonBand5Frames,
       "sh1DownloadCapability": sh1DownloadCapability,
       "sh1DownloadImageFile": sh1DownloadImageFile,
       "sh1DownloadIpAddress": sh1DownloadIpAddress,
       "sh1DownloadMacAddress": sh1DownloadMacAddress,
       "sh1DownloadExecute": sh1DownloadExecute,
       "sh1AddrTrackCapability": sh1AddrTrackCapability,
       "sh1AddrTrackSendHubLearn": sh1AddrTrackSendHubLearn,
       "sh1AddrTrackPortTable": sh1AddrTrackPortTable,
       "sh1AddrTrackPortEntry": sh1AddrTrackPortEntry,
       "sh1AddrTrackPortID": sh1AddrTrackPortID,
       "sh1AddrTrackDetectedMacAddr": sh1AddrTrackDetectedMacAddr,
       "sh1AddrTrackDetectedAddrType": sh1AddrTrackDetectedAddrType,
       "sh1AddrTrackAuthMacAddr": sh1AddrTrackAuthMacAddr,
       "sh1AddrTrackAuthAddrType": sh1AddrTrackAuthAddrType,
       "sh1AddrTrackNewHubAddr": sh1AddrTrackNewHubAddr,
       "sh1EnhancedCtrlCapability": sh1EnhancedCtrlCapability,
       "sh1EnhCtrlResetFirmwareConfig": sh1EnhCtrlResetFirmwareConfig,
       "sh1EnhCtrlHubVersion": sh1EnhCtrlHubVersion,
       "sh1EnhCtrlTrapMacAddr": sh1EnhCtrlTrapMacAddr,
       "sh1EnhCtrlTrapIpAddr": sh1EnhCtrlTrapIpAddr,
       "sh1EnhCtrlGatewayIpAddr": sh1EnhCtrlGatewayIpAddr,
       "sh1EnhCtrlNetworkMask": sh1EnhCtrlNetworkMask,
       "sh1EnhCtrlHubIpAddr": sh1EnhCtrlHubIpAddr,
       "sh1EnhCtrlHubAlias": sh1EnhCtrlHubAlias,
       "sh1EnhCtrlRs232State": sh1EnhCtrlRs232State,
       "sh1EnhCtrlRs232DataRate": sh1EnhCtrlRs232DataRate,
       "sh1EnhCtrlTrapCountPeriodCtrl": sh1EnhCtrlTrapCountPeriodCtrl,
       "sh1EnhCtrlTrapCountContentsCtrl": sh1EnhCtrlTrapCountContentsCtrl,
       "sh1EnhCtrlSendTrapConfig": sh1EnhCtrlSendTrapConfig,
       "sh1EnhCtrlPortTable": sh1EnhCtrlPortTable,
       "sh1EnhCtrlPortEntry": sh1EnhCtrlPortEntry,
       "sh1EnhCtrlPortID": sh1EnhCtrlPortID,
       "sh1EnhCtrlLinkIntegrityCtrl": sh1EnhCtrlLinkIntegrityCtrl,
       "sh1EnhCtrlLinkIntegrityAlarmCtrl": sh1EnhCtrlLinkIntegrityAlarmCtrl,
       "sh1EnhCtrlLinkIntegrityState": sh1EnhCtrlLinkIntegrityState,
       "sh1EnhCtrlExtendedDistanceCtrl": sh1EnhCtrlExtendedDistanceCtrl,
       "sh1EnhCtrlPortConfig": sh1EnhCtrlPortConfig,
       "sh1SecurityCapability": sh1SecurityCapability,
       "sh1SecEavesdroppingCtrl": sh1SecEavesdroppingCtrl,
       "sh1SecIntrusionCtrl": sh1SecIntrusionCtrl,
       "sh1SecIntrusionAlarmCtrl": sh1SecIntrusionAlarmCtrl,
       "sh1SecPassword": sh1SecPassword,
       "sh1SecBadPasswords": sh1SecBadPasswords,
       "sh1SecSettingAdminMacAddr": sh1SecSettingAdminMacAddr,
       "sh1SecSettingAdminIpAddr": sh1SecSettingAdminIpAddr,
       "sh1SecInbandSetsState": sh1SecInbandSetsState,
       "sh1SecPortTable": sh1SecPortTable,
       "sh1SecPortEntry": sh1SecPortEntry,
       "sh1SecPortID": sh1SecPortID,
       "sh1SecIntrusionAddr": sh1SecIntrusionAddr,
       "sh1SecIntrusionTimeStamp": sh1SecIntrusionTimeStamp,
       "sh1SecIntrusions": sh1SecIntrusions}
)
