# SNMP MIB module (BAS-TOPOLOGY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-TOPOLOGY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:35 2024
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

(BasCardClass,
 BasChassisId,
 BasChassisType,
 BasIfClass,
 BasInterfaceId,
 BasLogicalPortId,
 BasSlotId,
 basTopology) = mibBuilder.importSymbols(
    "BAS-MIB",
    "BasCardClass",
    "BasChassisId",
    "BasChassisType",
    "BasIfClass",
    "BasInterfaceId",
    "BasLogicalPortId",
    "BasSlotId",
    "basTopology")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(InterfaceIndex,
 ifEntry) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifEntry")

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


# MODULE-IDENTITY

basTopologyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BasChassisTopTable_Object = MibTable
basChassisTopTable = _BasChassisTopTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 1)
)
if mibBuilder.loadTexts:
    basChassisTopTable.setStatus("current")
_BasChassisTopEntry_Object = MibTableRow
basChassisTopEntry = _BasChassisTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 1, 1)
)
basChassisTopEntry.setIndexNames(
    (0, "BAS-TOPOLOGY-MIB", "basChassisTopChassis"),
    (0, "BAS-TOPOLOGY-MIB", "basChassisTopSlot"),
    (0, "BAS-TOPOLOGY-MIB", "basChassisTopIf"),
    (0, "BAS-TOPOLOGY-MIB", "basChassisTopLPort"),
)
if mibBuilder.loadTexts:
    basChassisTopEntry.setStatus("current")
_BasChassisTopChassis_Type = BasChassisId
_BasChassisTopChassis_Object = MibTableColumn
basChassisTopChassis = _BasChassisTopChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 1, 1, 1),
    _BasChassisTopChassis_Type()
)
basChassisTopChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basChassisTopChassis.setStatus("current")
_BasChassisTopSlot_Type = BasSlotId
_BasChassisTopSlot_Object = MibTableColumn
basChassisTopSlot = _BasChassisTopSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 1, 1, 2),
    _BasChassisTopSlot_Type()
)
basChassisTopSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basChassisTopSlot.setStatus("current")
_BasChassisTopIf_Type = BasInterfaceId
_BasChassisTopIf_Object = MibTableColumn
basChassisTopIf = _BasChassisTopIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 1, 1, 3),
    _BasChassisTopIf_Type()
)
basChassisTopIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basChassisTopIf.setStatus("current")
_BasChassisTopLPort_Type = BasLogicalPortId
_BasChassisTopLPort_Object = MibTableColumn
basChassisTopLPort = _BasChassisTopLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 1, 1, 4),
    _BasChassisTopLPort_Type()
)
basChassisTopLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basChassisTopLPort.setStatus("current")
_BasChassisTopChassisNumber_Type = Integer32
_BasChassisTopChassisNumber_Object = MibTableColumn
basChassisTopChassisNumber = _BasChassisTopChassisNumber_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 1, 1, 5),
    _BasChassisTopChassisNumber_Type()
)
basChassisTopChassisNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basChassisTopChassisNumber.setStatus("current")
_BasChassisTopChassisType_Type = BasChassisType
_BasChassisTopChassisType_Object = MibTableColumn
basChassisTopChassisType = _BasChassisTopChassisType_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 1, 1, 6),
    _BasChassisTopChassisType_Type()
)
basChassisTopChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basChassisTopChassisType.setStatus("current")
_BasChassisTopSlotInfo_Type = OctetString
_BasChassisTopSlotInfo_Object = MibTableColumn
basChassisTopSlotInfo = _BasChassisTopSlotInfo_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 1, 1, 7),
    _BasChassisTopSlotInfo_Type()
)
basChassisTopSlotInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basChassisTopSlotInfo.setStatus("current")


class _BasChassisTopStatus_Type(Integer32):
    """Custom type basChassisTopStatus based on Integer32"""
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


_BasChassisTopStatus_Type.__name__ = "Integer32"
_BasChassisTopStatus_Object = MibTableColumn
basChassisTopStatus = _BasChassisTopStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 1, 1, 8),
    _BasChassisTopStatus_Type()
)
basChassisTopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basChassisTopStatus.setStatus("current")
_BasSlotTopTable_Object = MibTable
basSlotTopTable = _BasSlotTopTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 2)
)
if mibBuilder.loadTexts:
    basSlotTopTable.setStatus("current")
_BasSlotTopEntry_Object = MibTableRow
basSlotTopEntry = _BasSlotTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 2, 1)
)
basSlotTopEntry.setIndexNames(
    (0, "BAS-TOPOLOGY-MIB", "basSlotTopChassis"),
    (0, "BAS-TOPOLOGY-MIB", "basSlotTopSlot"),
    (0, "BAS-TOPOLOGY-MIB", "basSlotTopIf"),
    (0, "BAS-TOPOLOGY-MIB", "basSlotTopLPort"),
    (0, "BAS-TOPOLOGY-MIB", "basSlotTopACChassis"),
    (0, "BAS-TOPOLOGY-MIB", "basSlotTopACSlot"),
    (0, "BAS-TOPOLOGY-MIB", "basSlotTopACIf"),
    (0, "BAS-TOPOLOGY-MIB", "basSlotTopACLPort"),
)
if mibBuilder.loadTexts:
    basSlotTopEntry.setStatus("current")
_BasSlotTopChassis_Type = BasChassisId
_BasSlotTopChassis_Object = MibTableColumn
basSlotTopChassis = _BasSlotTopChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 2, 1, 1),
    _BasSlotTopChassis_Type()
)
basSlotTopChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basSlotTopChassis.setStatus("current")
_BasSlotTopSlot_Type = BasSlotId
_BasSlotTopSlot_Object = MibTableColumn
basSlotTopSlot = _BasSlotTopSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 2, 1, 2),
    _BasSlotTopSlot_Type()
)
basSlotTopSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basSlotTopSlot.setStatus("current")
_BasSlotTopIf_Type = BasInterfaceId
_BasSlotTopIf_Object = MibTableColumn
basSlotTopIf = _BasSlotTopIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 2, 1, 3),
    _BasSlotTopIf_Type()
)
basSlotTopIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basSlotTopIf.setStatus("current")
_BasSlotTopLPort_Type = BasLogicalPortId
_BasSlotTopLPort_Object = MibTableColumn
basSlotTopLPort = _BasSlotTopLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 2, 1, 4),
    _BasSlotTopLPort_Type()
)
basSlotTopLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basSlotTopLPort.setStatus("current")
_BasSlotTopACChassis_Type = BasChassisId
_BasSlotTopACChassis_Object = MibTableColumn
basSlotTopACChassis = _BasSlotTopACChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 2, 1, 5),
    _BasSlotTopACChassis_Type()
)
basSlotTopACChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basSlotTopACChassis.setStatus("current")
_BasSlotTopACSlot_Type = BasSlotId
_BasSlotTopACSlot_Object = MibTableColumn
basSlotTopACSlot = _BasSlotTopACSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 2, 1, 6),
    _BasSlotTopACSlot_Type()
)
basSlotTopACSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basSlotTopACSlot.setStatus("current")
_BasSlotTopACIf_Type = BasInterfaceId
_BasSlotTopACIf_Object = MibTableColumn
basSlotTopACIf = _BasSlotTopACIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 2, 1, 7),
    _BasSlotTopACIf_Type()
)
basSlotTopACIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basSlotTopACIf.setStatus("current")
_BasSlotTopACLPort_Type = BasLogicalPortId
_BasSlotTopACLPort_Object = MibTableColumn
basSlotTopACLPort = _BasSlotTopACLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 2, 1, 8),
    _BasSlotTopACLPort_Type()
)
basSlotTopACLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basSlotTopACLPort.setStatus("current")
_BasSlotTopNumberOfIfs_Type = Integer32
_BasSlotTopNumberOfIfs_Object = MibTableColumn
basSlotTopNumberOfIfs = _BasSlotTopNumberOfIfs_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 2, 1, 9),
    _BasSlotTopNumberOfIfs_Type()
)
basSlotTopNumberOfIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSlotTopNumberOfIfs.setStatus("current")
_BasSlotTopIfInfo_Type = OctetString
_BasSlotTopIfInfo_Object = MibTableColumn
basSlotTopIfInfo = _BasSlotTopIfInfo_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 2, 1, 10),
    _BasSlotTopIfInfo_Type()
)
basSlotTopIfInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSlotTopIfInfo.setStatus("current")
_BasSlotTopCardType_Type = BasCardClass
_BasSlotTopCardType_Object = MibTableColumn
basSlotTopCardType = _BasSlotTopCardType_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 2, 1, 11),
    _BasSlotTopCardType_Type()
)
basSlotTopCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSlotTopCardType.setStatus("current")
_BasSlotTopInterChassisIP_Type = IpAddress
_BasSlotTopInterChassisIP_Object = MibTableColumn
basSlotTopInterChassisIP = _BasSlotTopInterChassisIP_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 2, 1, 12),
    _BasSlotTopInterChassisIP_Type()
)
basSlotTopInterChassisIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSlotTopInterChassisIP.setStatus("current")
_BasSlotTopIntraChassisIP_Type = IpAddress
_BasSlotTopIntraChassisIP_Object = MibTableColumn
basSlotTopIntraChassisIP = _BasSlotTopIntraChassisIP_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 2, 1, 13),
    _BasSlotTopIntraChassisIP_Type()
)
basSlotTopIntraChassisIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSlotTopIntraChassisIP.setStatus("current")


class _BasSlotTopStatus_Type(Integer32):
    """Custom type basSlotTopStatus based on Integer32"""
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


_BasSlotTopStatus_Type.__name__ = "Integer32"
_BasSlotTopStatus_Object = MibTableColumn
basSlotTopStatus = _BasSlotTopStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 2, 1, 14),
    _BasSlotTopStatus_Type()
)
basSlotTopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSlotTopStatus.setStatus("current")
_BasIfTopTable_Object = MibTable
basIfTopTable = _BasIfTopTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 3)
)
if mibBuilder.loadTexts:
    basIfTopTable.setStatus("current")
_BasIfTopEntry_Object = MibTableRow
basIfTopEntry = _BasIfTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 3, 1)
)
if mibBuilder.loadTexts:
    basIfTopEntry.setStatus("current")
_BasIfTopIfClass_Type = BasIfClass
_BasIfTopIfClass_Object = MibTableColumn
basIfTopIfClass = _BasIfTopIfClass_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 3, 1, 1),
    _BasIfTopIfClass_Type()
)
basIfTopIfClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIfTopIfClass.setStatus("current")
_BasIfTopIfType_Type = IANAifType
_BasIfTopIfType_Object = MibTableColumn
basIfTopIfType = _BasIfTopIfType_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 3, 1, 3),
    _BasIfTopIfType_Type()
)
basIfTopIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIfTopIfType.setStatus("current")
_BasIfTopICLNeighbor_Type = InterfaceIndex
_BasIfTopICLNeighbor_Object = MibTableColumn
basIfTopICLNeighbor = _BasIfTopICLNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 3, 1, 4),
    _BasIfTopICLNeighbor_Type()
)
basIfTopICLNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIfTopICLNeighbor.setStatus("current")


class _BasIfTopICLMode_Type(Integer32):
    """Custom type basIfTopICLMode based on Integer32"""
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
          ("other", 3),
          ("redundant", 2))
    )


_BasIfTopICLMode_Type.__name__ = "Integer32"
_BasIfTopICLMode_Object = MibTableColumn
basIfTopICLMode = _BasIfTopICLMode_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 3, 1, 5),
    _BasIfTopICLMode_Type()
)
basIfTopICLMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIfTopICLMode.setStatus("current")


class _BasIfTopIfStatus_Type(Integer32):
    """Custom type basIfTopIfStatus based on Integer32"""
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


_BasIfTopIfStatus_Type.__name__ = "Integer32"
_BasIfTopIfStatus_Object = MibTableColumn
basIfTopIfStatus = _BasIfTopIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 3, 1, 6),
    _BasIfTopIfStatus_Type()
)
basIfTopIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIfTopIfStatus.setStatus("current")
_BasRSTable_Object = MibTable
basRSTable = _BasRSTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 4)
)
if mibBuilder.loadTexts:
    basRSTable.setStatus("current")
_BasRSEntry_Object = MibTableRow
basRSEntry = _BasRSEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 4, 1)
)
basRSEntry.setIndexNames(
    (0, "BAS-TOPOLOGY-MIB", "basRSMgrChassis"),
    (0, "BAS-TOPOLOGY-MIB", "basRSMgrSlot"),
    (0, "BAS-TOPOLOGY-MIB", "basRSMgrIf"),
    (0, "BAS-TOPOLOGY-MIB", "basRSMgrLPort"),
    (0, "BAS-TOPOLOGY-MIB", "basRSChassis"),
    (0, "BAS-TOPOLOGY-MIB", "basRSSlot"),
    (0, "BAS-TOPOLOGY-MIB", "basRSIf"),
    (0, "BAS-TOPOLOGY-MIB", "basRSLPort"),
)
if mibBuilder.loadTexts:
    basRSEntry.setStatus("current")
_BasRSMgrChassis_Type = BasChassisId
_BasRSMgrChassis_Object = MibTableColumn
basRSMgrChassis = _BasRSMgrChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 4, 1, 1),
    _BasRSMgrChassis_Type()
)
basRSMgrChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basRSMgrChassis.setStatus("current")
_BasRSMgrSlot_Type = BasSlotId
_BasRSMgrSlot_Object = MibTableColumn
basRSMgrSlot = _BasRSMgrSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 4, 1, 2),
    _BasRSMgrSlot_Type()
)
basRSMgrSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basRSMgrSlot.setStatus("current")
_BasRSMgrIf_Type = BasInterfaceId
_BasRSMgrIf_Object = MibTableColumn
basRSMgrIf = _BasRSMgrIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 4, 1, 3),
    _BasRSMgrIf_Type()
)
basRSMgrIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basRSMgrIf.setStatus("current")
_BasRSMgrLPort_Type = BasLogicalPortId
_BasRSMgrLPort_Object = MibTableColumn
basRSMgrLPort = _BasRSMgrLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 4, 1, 4),
    _BasRSMgrLPort_Type()
)
basRSMgrLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basRSMgrLPort.setStatus("current")
_BasRSChassis_Type = BasChassisId
_BasRSChassis_Object = MibTableColumn
basRSChassis = _BasRSChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 4, 1, 5),
    _BasRSChassis_Type()
)
basRSChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basRSChassis.setStatus("current")
_BasRSSlot_Type = BasSlotId
_BasRSSlot_Object = MibTableColumn
basRSSlot = _BasRSSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 4, 1, 6),
    _BasRSSlot_Type()
)
basRSSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basRSSlot.setStatus("current")
_BasRSIf_Type = BasInterfaceId
_BasRSIf_Object = MibTableColumn
basRSIf = _BasRSIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 4, 1, 7),
    _BasRSIf_Type()
)
basRSIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basRSIf.setStatus("current")
_BasRSLPort_Type = BasLogicalPortId
_BasRSLPort_Object = MibTableColumn
basRSLPort = _BasRSLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 4, 1, 8),
    _BasRSLPort_Type()
)
basRSLPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basRSLPort.setStatus("current")


class _BasRSRole_Type(Integer32):
    """Custom type basRSRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_BasRSRole_Type.__name__ = "Integer32"
_BasRSRole_Object = MibTableColumn
basRSRole = _BasRSRole_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9, 1, 4, 1, 9),
    _BasRSRole_Type()
)
basRSRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basRSRole.setStatus("current")
ifEntry.registerAugmentions(
    ("BAS-TOPOLOGY-MIB",
     "basIfTopEntry")
)
basIfTopEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-TOPOLOGY-MIB",
    **{"basTopologyMIB": basTopologyMIB,
       "basChassisTopTable": basChassisTopTable,
       "basChassisTopEntry": basChassisTopEntry,
       "basChassisTopChassis": basChassisTopChassis,
       "basChassisTopSlot": basChassisTopSlot,
       "basChassisTopIf": basChassisTopIf,
       "basChassisTopLPort": basChassisTopLPort,
       "basChassisTopChassisNumber": basChassisTopChassisNumber,
       "basChassisTopChassisType": basChassisTopChassisType,
       "basChassisTopSlotInfo": basChassisTopSlotInfo,
       "basChassisTopStatus": basChassisTopStatus,
       "basSlotTopTable": basSlotTopTable,
       "basSlotTopEntry": basSlotTopEntry,
       "basSlotTopChassis": basSlotTopChassis,
       "basSlotTopSlot": basSlotTopSlot,
       "basSlotTopIf": basSlotTopIf,
       "basSlotTopLPort": basSlotTopLPort,
       "basSlotTopACChassis": basSlotTopACChassis,
       "basSlotTopACSlot": basSlotTopACSlot,
       "basSlotTopACIf": basSlotTopACIf,
       "basSlotTopACLPort": basSlotTopACLPort,
       "basSlotTopNumberOfIfs": basSlotTopNumberOfIfs,
       "basSlotTopIfInfo": basSlotTopIfInfo,
       "basSlotTopCardType": basSlotTopCardType,
       "basSlotTopInterChassisIP": basSlotTopInterChassisIP,
       "basSlotTopIntraChassisIP": basSlotTopIntraChassisIP,
       "basSlotTopStatus": basSlotTopStatus,
       "basIfTopTable": basIfTopTable,
       "basIfTopEntry": basIfTopEntry,
       "basIfTopIfClass": basIfTopIfClass,
       "basIfTopIfType": basIfTopIfType,
       "basIfTopICLNeighbor": basIfTopICLNeighbor,
       "basIfTopICLMode": basIfTopICLMode,
       "basIfTopIfStatus": basIfTopIfStatus,
       "basRSTable": basRSTable,
       "basRSEntry": basRSEntry,
       "basRSMgrChassis": basRSMgrChassis,
       "basRSMgrSlot": basRSMgrSlot,
       "basRSMgrIf": basRSMgrIf,
       "basRSMgrLPort": basRSMgrLPort,
       "basRSChassis": basRSChassis,
       "basRSSlot": basRSSlot,
       "basRSIf": basRSIf,
       "basRSLPort": basRSLPort,
       "basRSRole": basRSRole}
)
