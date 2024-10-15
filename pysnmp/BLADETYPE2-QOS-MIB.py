# SNMP MIB module (BLADETYPE2-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BLADETYPE2-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:04 2024
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

(BridgeId,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId")

(hpSwitchBladeType2_Mgmt,) = mibBuilder.importSymbols(
    "HP-SWITCH-PL-MIB",
    "hpSwitchBladeType2-Mgmt")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

qos = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QosConfigs_ObjectIdentity = ObjectIdentity
qosConfigs = _QosConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1)
)
_Qos8021p_ObjectIdentity = ObjectIdentity
qos8021p = _Qos8021p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1)
)
_QosCurCfgPortPriorityTable_Object = MibTable
qosCurCfgPortPriorityTable = _QosCurCfgPortPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    qosCurCfgPortPriorityTable.setStatus("current")
_QosCurCfgPortPriorityEntry_Object = MibTableRow
qosCurCfgPortPriorityEntry = _QosCurCfgPortPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 1, 1)
)
qosCurCfgPortPriorityEntry.setIndexNames(
    (0, "BLADETYPE2-QOS-MIB", "qosCurCfgPortIndex"),
)
if mibBuilder.loadTexts:
    qosCurCfgPortPriorityEntry.setStatus("current")
_QosCurCfgPortIndex_Type = Integer32
_QosCurCfgPortIndex_Object = MibTableColumn
qosCurCfgPortIndex = _QosCurCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 1, 1, 1),
    _QosCurCfgPortIndex_Type()
)
qosCurCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCurCfgPortIndex.setStatus("current")


class _QosCurCfgPortPriority_Type(Integer32):
    """Custom type qosCurCfgPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosCurCfgPortPriority_Type.__name__ = "Integer32"
_QosCurCfgPortPriority_Object = MibTableColumn
qosCurCfgPortPriority = _QosCurCfgPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 1, 1, 2),
    _QosCurCfgPortPriority_Type()
)
qosCurCfgPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCurCfgPortPriority.setStatus("current")
_QosNewCfgPortPriorityTable_Object = MibTable
qosNewCfgPortPriorityTable = _QosNewCfgPortPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 2)
)
if mibBuilder.loadTexts:
    qosNewCfgPortPriorityTable.setStatus("current")
_QosNewCfgPortPriorityEntry_Object = MibTableRow
qosNewCfgPortPriorityEntry = _QosNewCfgPortPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 2, 1)
)
qosNewCfgPortPriorityEntry.setIndexNames(
    (0, "BLADETYPE2-QOS-MIB", "qosNewCfgPortIndex"),
)
if mibBuilder.loadTexts:
    qosNewCfgPortPriorityEntry.setStatus("current")
_QosNewCfgPortIndex_Type = Integer32
_QosNewCfgPortIndex_Object = MibTableColumn
qosNewCfgPortIndex = _QosNewCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 2, 1, 1),
    _QosNewCfgPortIndex_Type()
)
qosNewCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosNewCfgPortIndex.setStatus("current")


class _QosNewCfgPortPriority_Type(Integer32):
    """Custom type qosNewCfgPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosNewCfgPortPriority_Type.__name__ = "Integer32"
_QosNewCfgPortPriority_Object = MibTableColumn
qosNewCfgPortPriority = _QosNewCfgPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 2, 1, 2),
    _QosNewCfgPortPriority_Type()
)
qosNewCfgPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosNewCfgPortPriority.setStatus("current")
_QosCurCfgPriorityCoSTable_Object = MibTable
qosCurCfgPriorityCoSTable = _QosCurCfgPriorityCoSTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 3)
)
if mibBuilder.loadTexts:
    qosCurCfgPriorityCoSTable.setStatus("current")
_QosCurCfgPriorityCoSEntry_Object = MibTableRow
qosCurCfgPriorityCoSEntry = _QosCurCfgPriorityCoSEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 3, 1)
)
qosCurCfgPriorityCoSEntry.setIndexNames(
    (0, "BLADETYPE2-QOS-MIB", "qosCurCfgPriorityIndex"),
)
if mibBuilder.loadTexts:
    qosCurCfgPriorityCoSEntry.setStatus("current")


class _QosCurCfgPriorityIndex_Type(Integer32):
    """Custom type qosCurCfgPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosCurCfgPriorityIndex_Type.__name__ = "Integer32"
_QosCurCfgPriorityIndex_Object = MibTableColumn
qosCurCfgPriorityIndex = _QosCurCfgPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 3, 1, 1),
    _QosCurCfgPriorityIndex_Type()
)
qosCurCfgPriorityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCurCfgPriorityIndex.setStatus("current")


class _QosCurCfgPriorityCoSq_Type(Integer32):
    """Custom type qosCurCfgPriorityCoSq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosCurCfgPriorityCoSq_Type.__name__ = "Integer32"
_QosCurCfgPriorityCoSq_Object = MibTableColumn
qosCurCfgPriorityCoSq = _QosCurCfgPriorityCoSq_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 3, 1, 2),
    _QosCurCfgPriorityCoSq_Type()
)
qosCurCfgPriorityCoSq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCurCfgPriorityCoSq.setStatus("current")
_QosNewCfgPriorityCoSTable_Object = MibTable
qosNewCfgPriorityCoSTable = _QosNewCfgPriorityCoSTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 4)
)
if mibBuilder.loadTexts:
    qosNewCfgPriorityCoSTable.setStatus("current")
_QosNewCfgPriorityCoSEntry_Object = MibTableRow
qosNewCfgPriorityCoSEntry = _QosNewCfgPriorityCoSEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 4, 1)
)
qosNewCfgPriorityCoSEntry.setIndexNames(
    (0, "BLADETYPE2-QOS-MIB", "qosNewCfgPriorityIndex"),
)
if mibBuilder.loadTexts:
    qosNewCfgPriorityCoSEntry.setStatus("current")


class _QosNewCfgPriorityIndex_Type(Integer32):
    """Custom type qosNewCfgPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosNewCfgPriorityIndex_Type.__name__ = "Integer32"
_QosNewCfgPriorityIndex_Object = MibTableColumn
qosNewCfgPriorityIndex = _QosNewCfgPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 4, 1, 1),
    _QosNewCfgPriorityIndex_Type()
)
qosNewCfgPriorityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosNewCfgPriorityIndex.setStatus("current")


class _QosNewCfgPriorityCoSq_Type(Integer32):
    """Custom type qosNewCfgPriorityCoSq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosNewCfgPriorityCoSq_Type.__name__ = "Integer32"
_QosNewCfgPriorityCoSq_Object = MibTableColumn
qosNewCfgPriorityCoSq = _QosNewCfgPriorityCoSq_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 4, 1, 2),
    _QosNewCfgPriorityCoSq_Type()
)
qosNewCfgPriorityCoSq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosNewCfgPriorityCoSq.setStatus("current")
_QosCurCfgCosWeightTable_Object = MibTable
qosCurCfgCosWeightTable = _QosCurCfgCosWeightTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 5)
)
if mibBuilder.loadTexts:
    qosCurCfgCosWeightTable.setStatus("current")
_QosCurCfgCosWeightEntry_Object = MibTableRow
qosCurCfgCosWeightEntry = _QosCurCfgCosWeightEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 5, 1)
)
qosCurCfgCosWeightEntry.setIndexNames(
    (0, "BLADETYPE2-QOS-MIB", "qosCurCfgCosIndex"),
)
if mibBuilder.loadTexts:
    qosCurCfgCosWeightEntry.setStatus("current")


class _QosCurCfgCosIndex_Type(Integer32):
    """Custom type qosCurCfgCosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosCurCfgCosIndex_Type.__name__ = "Integer32"
_QosCurCfgCosIndex_Object = MibTableColumn
qosCurCfgCosIndex = _QosCurCfgCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 5, 1, 1),
    _QosCurCfgCosIndex_Type()
)
qosCurCfgCosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCurCfgCosIndex.setStatus("current")


class _QosCurCfgCosWeight_Type(Integer32):
    """Custom type qosCurCfgCosWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_QosCurCfgCosWeight_Type.__name__ = "Integer32"
_QosCurCfgCosWeight_Object = MibTableColumn
qosCurCfgCosWeight = _QosCurCfgCosWeight_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 5, 1, 2),
    _QosCurCfgCosWeight_Type()
)
qosCurCfgCosWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCurCfgCosWeight.setStatus("current")
_QosNewCfgCosWeightTable_Object = MibTable
qosNewCfgCosWeightTable = _QosNewCfgCosWeightTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 6)
)
if mibBuilder.loadTexts:
    qosNewCfgCosWeightTable.setStatus("current")
_QosNewCfgCosWeightEntry_Object = MibTableRow
qosNewCfgCosWeightEntry = _QosNewCfgCosWeightEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 6, 1)
)
qosNewCfgCosWeightEntry.setIndexNames(
    (0, "BLADETYPE2-QOS-MIB", "qosNewCfgCosIndex"),
)
if mibBuilder.loadTexts:
    qosNewCfgCosWeightEntry.setStatus("current")


class _QosNewCfgCosIndex_Type(Integer32):
    """Custom type qosNewCfgCosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosNewCfgCosIndex_Type.__name__ = "Integer32"
_QosNewCfgCosIndex_Object = MibTableColumn
qosNewCfgCosIndex = _QosNewCfgCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 6, 1, 1),
    _QosNewCfgCosIndex_Type()
)
qosNewCfgCosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosNewCfgCosIndex.setStatus("current")


class _QosNewCfgCosWeight_Type(Integer32):
    """Custom type qosNewCfgCosWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_QosNewCfgCosWeight_Type.__name__ = "Integer32"
_QosNewCfgCosWeight_Object = MibTableColumn
qosNewCfgCosWeight = _QosNewCfgCosWeight_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 6, 1, 2),
    _QosNewCfgCosWeight_Type()
)
qosNewCfgCosWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosNewCfgCosWeight.setStatus("current")


class _QosCurCfgCosNum_Type(Integer32):
    """Custom type qosCurCfgCosNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              8)
        )
    )
    namedValues = NamedValues(
        *(("num2", 2),
          ("num8", 8))
    )


_QosCurCfgCosNum_Type.__name__ = "Integer32"
_QosCurCfgCosNum_Object = MibScalar
qosCurCfgCosNum = _QosCurCfgCosNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 7),
    _QosCurCfgCosNum_Type()
)
qosCurCfgCosNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCurCfgCosNum.setStatus("current")


class _QosNewCfgCosNum_Type(Integer32):
    """Custom type qosNewCfgCosNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              8)
        )
    )
    namedValues = NamedValues(
        *(("num2", 2),
          ("num8", 8))
    )


_QosNewCfgCosNum_Type.__name__ = "Integer32"
_QosNewCfgCosNum_Object = MibScalar
qosNewCfgCosNum = _QosNewCfgCosNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 1, 8),
    _QosNewCfgCosNum_Type()
)
qosNewCfgCosNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosNewCfgCosNum.setStatus("current")
_AclCfg_ObjectIdentity = ObjectIdentity
aclCfg = _AclCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2)
)
_AclCurCfgPortTable_Object = MibTable
aclCurCfgPortTable = _AclCurCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 1)
)
if mibBuilder.loadTexts:
    aclCurCfgPortTable.setStatus("current")
_AclCurCfgPortTableEntry_Object = MibTableRow
aclCurCfgPortTableEntry = _AclCurCfgPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 1, 1)
)
aclCurCfgPortTableEntry.setIndexNames(
    (0, "BLADETYPE2-QOS-MIB", "aclCurCfgPortIndex"),
)
if mibBuilder.loadTexts:
    aclCurCfgPortTableEntry.setStatus("current")
_AclCurCfgPortIndex_Type = Integer32
_AclCurCfgPortIndex_Object = MibTableColumn
aclCurCfgPortIndex = _AclCurCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 1, 1, 1),
    _AclCurCfgPortIndex_Type()
)
aclCurCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgPortIndex.setStatus("current")


class _AclCurCfgPortAclBmap_Type(OctetString):
    """Custom type aclCurCfgPortAclBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AclCurCfgPortAclBmap_Type.__name__ = "OctetString"
_AclCurCfgPortAclBmap_Object = MibTableColumn
aclCurCfgPortAclBmap = _AclCurCfgPortAclBmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 1, 1, 2),
    _AclCurCfgPortAclBmap_Type()
)
aclCurCfgPortAclBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgPortAclBmap.setStatus("current")


class _AclCurCfgPortAclBlkBmap_Type(OctetString):
    """Custom type aclCurCfgPortAclBlkBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AclCurCfgPortAclBlkBmap_Type.__name__ = "OctetString"
_AclCurCfgPortAclBlkBmap_Object = MibTableColumn
aclCurCfgPortAclBlkBmap = _AclCurCfgPortAclBlkBmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 1, 1, 3),
    _AclCurCfgPortAclBlkBmap_Type()
)
aclCurCfgPortAclBlkBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgPortAclBlkBmap.setStatus("current")


class _AclCurCfgPortAclGrpBmap_Type(OctetString):
    """Custom type aclCurCfgPortAclGrpBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AclCurCfgPortAclGrpBmap_Type.__name__ = "OctetString"
_AclCurCfgPortAclGrpBmap_Object = MibTableColumn
aclCurCfgPortAclGrpBmap = _AclCurCfgPortAclGrpBmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 1, 1, 4),
    _AclCurCfgPortAclGrpBmap_Type()
)
aclCurCfgPortAclGrpBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgPortAclGrpBmap.setStatus("current")
_AclNewCfgPortTable_Object = MibTable
aclNewCfgPortTable = _AclNewCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 2)
)
if mibBuilder.loadTexts:
    aclNewCfgPortTable.setStatus("current")
_AclNewCfgPortTableEntry_Object = MibTableRow
aclNewCfgPortTableEntry = _AclNewCfgPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 2, 1)
)
aclNewCfgPortTableEntry.setIndexNames(
    (0, "BLADETYPE2-QOS-MIB", "aclNewCfgPortIndex"),
)
if mibBuilder.loadTexts:
    aclNewCfgPortTableEntry.setStatus("current")
_AclNewCfgPortIndex_Type = Integer32
_AclNewCfgPortIndex_Object = MibTableColumn
aclNewCfgPortIndex = _AclNewCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 2, 1, 1),
    _AclNewCfgPortIndex_Type()
)
aclNewCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNewCfgPortIndex.setStatus("current")
_AclNewCfgPortAddAcl_Type = Unsigned32
_AclNewCfgPortAddAcl_Object = MibTableColumn
aclNewCfgPortAddAcl = _AclNewCfgPortAddAcl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 2, 1, 2),
    _AclNewCfgPortAddAcl_Type()
)
aclNewCfgPortAddAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgPortAddAcl.setStatus("current")
_AclNewCfgPortAddAclBlk_Type = Unsigned32
_AclNewCfgPortAddAclBlk_Object = MibTableColumn
aclNewCfgPortAddAclBlk = _AclNewCfgPortAddAclBlk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 2, 1, 3),
    _AclNewCfgPortAddAclBlk_Type()
)
aclNewCfgPortAddAclBlk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgPortAddAclBlk.setStatus("current")
_AclNewCfgPortAddAclGrp_Type = Unsigned32
_AclNewCfgPortAddAclGrp_Object = MibTableColumn
aclNewCfgPortAddAclGrp = _AclNewCfgPortAddAclGrp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 2, 1, 4),
    _AclNewCfgPortAddAclGrp_Type()
)
aclNewCfgPortAddAclGrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgPortAddAclGrp.setStatus("current")
_AclNewCfgPortRemoveAcl_Type = Unsigned32
_AclNewCfgPortRemoveAcl_Object = MibTableColumn
aclNewCfgPortRemoveAcl = _AclNewCfgPortRemoveAcl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 2, 1, 5),
    _AclNewCfgPortRemoveAcl_Type()
)
aclNewCfgPortRemoveAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgPortRemoveAcl.setStatus("current")
_AclNewCfgPortRemoveAclBlk_Type = Unsigned32
_AclNewCfgPortRemoveAclBlk_Object = MibTableColumn
aclNewCfgPortRemoveAclBlk = _AclNewCfgPortRemoveAclBlk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 2, 1, 6),
    _AclNewCfgPortRemoveAclBlk_Type()
)
aclNewCfgPortRemoveAclBlk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgPortRemoveAclBlk.setStatus("current")
_AclNewCfgPortRemoveAclGrp_Type = Unsigned32
_AclNewCfgPortRemoveAclGrp_Object = MibTableColumn
aclNewCfgPortRemoveAclGrp = _AclNewCfgPortRemoveAclGrp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 2, 1, 7),
    _AclNewCfgPortRemoveAclGrp_Type()
)
aclNewCfgPortRemoveAclGrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgPortRemoveAclGrp.setStatus("current")


class _AclNewCfgPortAclBmap_Type(OctetString):
    """Custom type aclNewCfgPortAclBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AclNewCfgPortAclBmap_Type.__name__ = "OctetString"
_AclNewCfgPortAclBmap_Object = MibTableColumn
aclNewCfgPortAclBmap = _AclNewCfgPortAclBmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 2, 1, 8),
    _AclNewCfgPortAclBmap_Type()
)
aclNewCfgPortAclBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNewCfgPortAclBmap.setStatus("current")


class _AclNewCfgPortAclBlkBmap_Type(OctetString):
    """Custom type aclNewCfgPortAclBlkBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AclNewCfgPortAclBlkBmap_Type.__name__ = "OctetString"
_AclNewCfgPortAclBlkBmap_Object = MibTableColumn
aclNewCfgPortAclBlkBmap = _AclNewCfgPortAclBlkBmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 2, 1, 9),
    _AclNewCfgPortAclBlkBmap_Type()
)
aclNewCfgPortAclBlkBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNewCfgPortAclBlkBmap.setStatus("current")


class _AclNewCfgPortAclGrpBmap_Type(OctetString):
    """Custom type aclNewCfgPortAclGrpBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AclNewCfgPortAclGrpBmap_Type.__name__ = "OctetString"
_AclNewCfgPortAclGrpBmap_Object = MibTableColumn
aclNewCfgPortAclGrpBmap = _AclNewCfgPortAclGrpBmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 2, 1, 10),
    _AclNewCfgPortAclGrpBmap_Type()
)
aclNewCfgPortAclGrpBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNewCfgPortAclGrpBmap.setStatus("current")
_AclCurCfgPortAclMeterTable_Object = MibTable
aclCurCfgPortAclMeterTable = _AclCurCfgPortAclMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 3)
)
if mibBuilder.loadTexts:
    aclCurCfgPortAclMeterTable.setStatus("current")
_AclCurCfgPortAclMeterTableEntry_Object = MibTableRow
aclCurCfgPortAclMeterTableEntry = _AclCurCfgPortAclMeterTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 3, 1)
)
aclCurCfgPortAclMeterTableEntry.setIndexNames(
    (0, "BLADETYPE2-QOS-MIB", "aclCurCfgPortMeterConfigIndex"),
    (0, "BLADETYPE2-QOS-MIB", "aclCurCfgAclMeterIndex"),
)
if mibBuilder.loadTexts:
    aclCurCfgPortAclMeterTableEntry.setStatus("current")
_AclCurCfgPortMeterConfigIndex_Type = Integer32
_AclCurCfgPortMeterConfigIndex_Object = MibTableColumn
aclCurCfgPortMeterConfigIndex = _AclCurCfgPortMeterConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 3, 1, 1),
    _AclCurCfgPortMeterConfigIndex_Type()
)
aclCurCfgPortMeterConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgPortMeterConfigIndex.setStatus("current")
_AclCurCfgAclMeterIndex_Type = Integer32
_AclCurCfgAclMeterIndex_Object = MibTableColumn
aclCurCfgAclMeterIndex = _AclCurCfgAclMeterIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 3, 1, 2),
    _AclCurCfgAclMeterIndex_Type()
)
aclCurCfgAclMeterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgAclMeterIndex.setStatus("current")


class _AclCurCfgAclMeterCommitRate_Type(Integer32):
    """Custom type aclCurCfgAclMeterCommitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 1000000),
    )


_AclCurCfgAclMeterCommitRate_Type.__name__ = "Integer32"
_AclCurCfgAclMeterCommitRate_Object = MibTableColumn
aclCurCfgAclMeterCommitRate = _AclCurCfgAclMeterCommitRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 3, 1, 3),
    _AclCurCfgAclMeterCommitRate_Type()
)
aclCurCfgAclMeterCommitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgAclMeterCommitRate.setStatus("current")


class _AclCurCfgAclMeterMaxBurstSize_Type(Integer32):
    """Custom type aclCurCfgAclMeterMaxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32,
              64,
              128,
              256,
              512,
              1024,
              2048,
              4096)
        )
    )
    namedValues = NamedValues(
        *(("k1024", 1024),
          ("k128", 128),
          ("k2048", 2048),
          ("k256", 256),
          ("k32", 32),
          ("k4096", 4096),
          ("k512", 512),
          ("k64", 64))
    )


_AclCurCfgAclMeterMaxBurstSize_Type.__name__ = "Integer32"
_AclCurCfgAclMeterMaxBurstSize_Object = MibTableColumn
aclCurCfgAclMeterMaxBurstSize = _AclCurCfgAclMeterMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 3, 1, 4),
    _AclCurCfgAclMeterMaxBurstSize_Type()
)
aclCurCfgAclMeterMaxBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgAclMeterMaxBurstSize.setStatus("current")


class _AclCurCfgAclMeterStatus_Type(Integer32):
    """Custom type aclCurCfgAclMeterStatus based on Integer32"""
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


_AclCurCfgAclMeterStatus_Type.__name__ = "Integer32"
_AclCurCfgAclMeterStatus_Object = MibTableColumn
aclCurCfgAclMeterStatus = _AclCurCfgAclMeterStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 3, 1, 5),
    _AclCurCfgAclMeterStatus_Type()
)
aclCurCfgAclMeterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgAclMeterStatus.setStatus("current")


class _AclCurCfgAclMeterDropOrPass_Type(Integer32):
    """Custom type aclCurCfgAclMeterDropOrPass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("none", 1),
          ("pass", 3))
    )


_AclCurCfgAclMeterDropOrPass_Type.__name__ = "Integer32"
_AclCurCfgAclMeterDropOrPass_Object = MibTableColumn
aclCurCfgAclMeterDropOrPass = _AclCurCfgAclMeterDropOrPass_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 3, 1, 6),
    _AclCurCfgAclMeterDropOrPass_Type()
)
aclCurCfgAclMeterDropOrPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgAclMeterDropOrPass.setStatus("current")


class _AclCurCfgAclMeterAclBmap_Type(OctetString):
    """Custom type aclCurCfgAclMeterAclBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AclCurCfgAclMeterAclBmap_Type.__name__ = "OctetString"
_AclCurCfgAclMeterAclBmap_Object = MibTableColumn
aclCurCfgAclMeterAclBmap = _AclCurCfgAclMeterAclBmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 3, 1, 7),
    _AclCurCfgAclMeterAclBmap_Type()
)
aclCurCfgAclMeterAclBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgAclMeterAclBmap.setStatus("current")


class _AclCurCfgAclMeterAclBlkBmap_Type(OctetString):
    """Custom type aclCurCfgAclMeterAclBlkBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AclCurCfgAclMeterAclBlkBmap_Type.__name__ = "OctetString"
_AclCurCfgAclMeterAclBlkBmap_Object = MibTableColumn
aclCurCfgAclMeterAclBlkBmap = _AclCurCfgAclMeterAclBlkBmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 3, 1, 8),
    _AclCurCfgAclMeterAclBlkBmap_Type()
)
aclCurCfgAclMeterAclBlkBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgAclMeterAclBlkBmap.setStatus("current")


class _AclCurCfgAclMeterAclGrpBmap_Type(OctetString):
    """Custom type aclCurCfgAclMeterAclGrpBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AclCurCfgAclMeterAclGrpBmap_Type.__name__ = "OctetString"
_AclCurCfgAclMeterAclGrpBmap_Object = MibTableColumn
aclCurCfgAclMeterAclGrpBmap = _AclCurCfgAclMeterAclGrpBmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 3, 1, 9),
    _AclCurCfgAclMeterAclGrpBmap_Type()
)
aclCurCfgAclMeterAclGrpBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgAclMeterAclGrpBmap.setStatus("current")
_AclNewCfgPortAclMeterTable_Object = MibTable
aclNewCfgPortAclMeterTable = _AclNewCfgPortAclMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4)
)
if mibBuilder.loadTexts:
    aclNewCfgPortAclMeterTable.setStatus("current")
_AclNewCfgPortAclMeterTableEntry_Object = MibTableRow
aclNewCfgPortAclMeterTableEntry = _AclNewCfgPortAclMeterTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1)
)
aclNewCfgPortAclMeterTableEntry.setIndexNames(
    (0, "BLADETYPE2-QOS-MIB", "aclNewCfgPortMeterConfigIndex"),
    (0, "BLADETYPE2-QOS-MIB", "aclNewCfgAclMeterIndex"),
)
if mibBuilder.loadTexts:
    aclNewCfgPortAclMeterTableEntry.setStatus("current")
_AclNewCfgPortMeterConfigIndex_Type = Integer32
_AclNewCfgPortMeterConfigIndex_Object = MibTableColumn
aclNewCfgPortMeterConfigIndex = _AclNewCfgPortMeterConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1, 1),
    _AclNewCfgPortMeterConfigIndex_Type()
)
aclNewCfgPortMeterConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNewCfgPortMeterConfigIndex.setStatus("current")
_AclNewCfgAclMeterIndex_Type = Integer32
_AclNewCfgAclMeterIndex_Object = MibTableColumn
aclNewCfgAclMeterIndex = _AclNewCfgAclMeterIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1, 2),
    _AclNewCfgAclMeterIndex_Type()
)
aclNewCfgAclMeterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNewCfgAclMeterIndex.setStatus("current")


class _AclNewCfgAclMeterCommitRate_Type(Integer32):
    """Custom type aclNewCfgAclMeterCommitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 1000000),
    )


_AclNewCfgAclMeterCommitRate_Type.__name__ = "Integer32"
_AclNewCfgAclMeterCommitRate_Object = MibTableColumn
aclNewCfgAclMeterCommitRate = _AclNewCfgAclMeterCommitRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1, 3),
    _AclNewCfgAclMeterCommitRate_Type()
)
aclNewCfgAclMeterCommitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgAclMeterCommitRate.setStatus("current")


class _AclNewCfgAclMeterMaxBurstSize_Type(Integer32):
    """Custom type aclNewCfgAclMeterMaxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32,
              64,
              128,
              256,
              512,
              1024,
              2048,
              4096)
        )
    )
    namedValues = NamedValues(
        *(("k1024", 1024),
          ("k128", 128),
          ("k2048", 2048),
          ("k256", 256),
          ("k32", 32),
          ("k4096", 4096),
          ("k512", 512),
          ("k64", 64))
    )


_AclNewCfgAclMeterMaxBurstSize_Type.__name__ = "Integer32"
_AclNewCfgAclMeterMaxBurstSize_Object = MibTableColumn
aclNewCfgAclMeterMaxBurstSize = _AclNewCfgAclMeterMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1, 4),
    _AclNewCfgAclMeterMaxBurstSize_Type()
)
aclNewCfgAclMeterMaxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgAclMeterMaxBurstSize.setStatus("current")


class _AclNewCfgAclMeterStatus_Type(Integer32):
    """Custom type aclNewCfgAclMeterStatus based on Integer32"""
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


_AclNewCfgAclMeterStatus_Type.__name__ = "Integer32"
_AclNewCfgAclMeterStatus_Object = MibTableColumn
aclNewCfgAclMeterStatus = _AclNewCfgAclMeterStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1, 5),
    _AclNewCfgAclMeterStatus_Type()
)
aclNewCfgAclMeterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgAclMeterStatus.setStatus("current")


class _AclNewCfgAclMeterDropOrPass_Type(Integer32):
    """Custom type aclNewCfgAclMeterDropOrPass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("none", 1),
          ("pass", 3))
    )


_AclNewCfgAclMeterDropOrPass_Type.__name__ = "Integer32"
_AclNewCfgAclMeterDropOrPass_Object = MibTableColumn
aclNewCfgAclMeterDropOrPass = _AclNewCfgAclMeterDropOrPass_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1, 6),
    _AclNewCfgAclMeterDropOrPass_Type()
)
aclNewCfgAclMeterDropOrPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgAclMeterDropOrPass.setStatus("current")
_AclNewCfgAclMeterAssignAcl_Type = Unsigned32
_AclNewCfgAclMeterAssignAcl_Object = MibTableColumn
aclNewCfgAclMeterAssignAcl = _AclNewCfgAclMeterAssignAcl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1, 7),
    _AclNewCfgAclMeterAssignAcl_Type()
)
aclNewCfgAclMeterAssignAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgAclMeterAssignAcl.setStatus("current")
_AclNewCfgAclMeterAssignAclBlk_Type = Unsigned32
_AclNewCfgAclMeterAssignAclBlk_Object = MibTableColumn
aclNewCfgAclMeterAssignAclBlk = _AclNewCfgAclMeterAssignAclBlk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1, 8),
    _AclNewCfgAclMeterAssignAclBlk_Type()
)
aclNewCfgAclMeterAssignAclBlk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgAclMeterAssignAclBlk.setStatus("current")
_AclNewCfgAclMeterAssignAclGrp_Type = Unsigned32
_AclNewCfgAclMeterAssignAclGrp_Object = MibTableColumn
aclNewCfgAclMeterAssignAclGrp = _AclNewCfgAclMeterAssignAclGrp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1, 9),
    _AclNewCfgAclMeterAssignAclGrp_Type()
)
aclNewCfgAclMeterAssignAclGrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgAclMeterAssignAclGrp.setStatus("current")
_AclNewCfgAclMeterUnAssignAcl_Type = Unsigned32
_AclNewCfgAclMeterUnAssignAcl_Object = MibTableColumn
aclNewCfgAclMeterUnAssignAcl = _AclNewCfgAclMeterUnAssignAcl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1, 10),
    _AclNewCfgAclMeterUnAssignAcl_Type()
)
aclNewCfgAclMeterUnAssignAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgAclMeterUnAssignAcl.setStatus("current")
_AclNewCfgAclMeterUnAssignAclBlk_Type = Unsigned32
_AclNewCfgAclMeterUnAssignAclBlk_Object = MibTableColumn
aclNewCfgAclMeterUnAssignAclBlk = _AclNewCfgAclMeterUnAssignAclBlk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1, 11),
    _AclNewCfgAclMeterUnAssignAclBlk_Type()
)
aclNewCfgAclMeterUnAssignAclBlk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgAclMeterUnAssignAclBlk.setStatus("current")
_AclNewCfgAclMeterUnAssignAclGrp_Type = Unsigned32
_AclNewCfgAclMeterUnAssignAclGrp_Object = MibTableColumn
aclNewCfgAclMeterUnAssignAclGrp = _AclNewCfgAclMeterUnAssignAclGrp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1, 12),
    _AclNewCfgAclMeterUnAssignAclGrp_Type()
)
aclNewCfgAclMeterUnAssignAclGrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgAclMeterUnAssignAclGrp.setStatus("current")


class _AclNewCfgAclMeterAclBmap_Type(OctetString):
    """Custom type aclNewCfgAclMeterAclBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AclNewCfgAclMeterAclBmap_Type.__name__ = "OctetString"
_AclNewCfgAclMeterAclBmap_Object = MibTableColumn
aclNewCfgAclMeterAclBmap = _AclNewCfgAclMeterAclBmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1, 13),
    _AclNewCfgAclMeterAclBmap_Type()
)
aclNewCfgAclMeterAclBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNewCfgAclMeterAclBmap.setStatus("current")


class _AclNewCfgAclMeterAclBlkBmap_Type(OctetString):
    """Custom type aclNewCfgAclMeterAclBlkBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AclNewCfgAclMeterAclBlkBmap_Type.__name__ = "OctetString"
_AclNewCfgAclMeterAclBlkBmap_Object = MibTableColumn
aclNewCfgAclMeterAclBlkBmap = _AclNewCfgAclMeterAclBlkBmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1, 14),
    _AclNewCfgAclMeterAclBlkBmap_Type()
)
aclNewCfgAclMeterAclBlkBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNewCfgAclMeterAclBlkBmap.setStatus("current")


class _AclNewCfgAclMeterAclGrpBmap_Type(OctetString):
    """Custom type aclNewCfgAclMeterAclGrpBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AclNewCfgAclMeterAclGrpBmap_Type.__name__ = "OctetString"
_AclNewCfgAclMeterAclGrpBmap_Object = MibTableColumn
aclNewCfgAclMeterAclGrpBmap = _AclNewCfgAclMeterAclGrpBmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 4, 1, 15),
    _AclNewCfgAclMeterAclGrpBmap_Type()
)
aclNewCfgAclMeterAclGrpBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNewCfgAclMeterAclGrpBmap.setStatus("current")
_AclCurCfgPortAclRemarkTable_Object = MibTable
aclCurCfgPortAclRemarkTable = _AclCurCfgPortAclRemarkTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 5)
)
if mibBuilder.loadTexts:
    aclCurCfgPortAclRemarkTable.setStatus("current")
_AclCurCfgPortAclRemarkTableEntry_Object = MibTableRow
aclCurCfgPortAclRemarkTableEntry = _AclCurCfgPortAclRemarkTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 5, 1)
)
aclCurCfgPortAclRemarkTableEntry.setIndexNames(
    (0, "BLADETYPE2-QOS-MIB", "aclCurCfgPortRemarkConfigIndex"),
    (0, "BLADETYPE2-QOS-MIB", "aclCurCfgAclRemarkIndex"),
)
if mibBuilder.loadTexts:
    aclCurCfgPortAclRemarkTableEntry.setStatus("current")
_AclCurCfgPortRemarkConfigIndex_Type = Integer32
_AclCurCfgPortRemarkConfigIndex_Object = MibTableColumn
aclCurCfgPortRemarkConfigIndex = _AclCurCfgPortRemarkConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 5, 1, 1),
    _AclCurCfgPortRemarkConfigIndex_Type()
)
aclCurCfgPortRemarkConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgPortRemarkConfigIndex.setStatus("current")
_AclCurCfgAclRemarkIndex_Type = Integer32
_AclCurCfgAclRemarkIndex_Object = MibTableColumn
aclCurCfgAclRemarkIndex = _AclCurCfgAclRemarkIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 5, 1, 2),
    _AclCurCfgAclRemarkIndex_Type()
)
aclCurCfgAclRemarkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgAclRemarkIndex.setStatus("current")


class _AclCurCfgAclRemarkInProfUpdatePri_Type(Integer32):
    """Custom type aclCurCfgAclRemarkInProfUpdatePri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AclCurCfgAclRemarkInProfUpdatePri_Type.__name__ = "Integer32"
_AclCurCfgAclRemarkInProfUpdatePri_Object = MibTableColumn
aclCurCfgAclRemarkInProfUpdatePri = _AclCurCfgAclRemarkInProfUpdatePri_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 5, 1, 3),
    _AclCurCfgAclRemarkInProfUpdatePri_Type()
)
aclCurCfgAclRemarkInProfUpdatePri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgAclRemarkInProfUpdatePri.setStatus("current")


class _AclCurCfgAclRemarkInProfUpdateTosPrec_Type(Integer32):
    """Custom type aclCurCfgAclRemarkInProfUpdateTosPrec based on Integer32"""
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


_AclCurCfgAclRemarkInProfUpdateTosPrec_Type.__name__ = "Integer32"
_AclCurCfgAclRemarkInProfUpdateTosPrec_Object = MibTableColumn
aclCurCfgAclRemarkInProfUpdateTosPrec = _AclCurCfgAclRemarkInProfUpdateTosPrec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 5, 1, 4),
    _AclCurCfgAclRemarkInProfUpdateTosPrec_Type()
)
aclCurCfgAclRemarkInProfUpdateTosPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgAclRemarkInProfUpdateTosPrec.setStatus("current")


class _AclCurCfgAclRemarkInProfUpdateDscp_Type(Integer32):
    """Custom type aclCurCfgAclRemarkInProfUpdateDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AclCurCfgAclRemarkInProfUpdateDscp_Type.__name__ = "Integer32"
_AclCurCfgAclRemarkInProfUpdateDscp_Object = MibTableColumn
aclCurCfgAclRemarkInProfUpdateDscp = _AclCurCfgAclRemarkInProfUpdateDscp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 5, 1, 5),
    _AclCurCfgAclRemarkInProfUpdateDscp_Type()
)
aclCurCfgAclRemarkInProfUpdateDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgAclRemarkInProfUpdateDscp.setStatus("current")


class _AclCurCfgAclRemarkOutProfUpdateDscp_Type(Integer32):
    """Custom type aclCurCfgAclRemarkOutProfUpdateDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AclCurCfgAclRemarkOutProfUpdateDscp_Type.__name__ = "Integer32"
_AclCurCfgAclRemarkOutProfUpdateDscp_Object = MibTableColumn
aclCurCfgAclRemarkOutProfUpdateDscp = _AclCurCfgAclRemarkOutProfUpdateDscp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 5, 1, 6),
    _AclCurCfgAclRemarkOutProfUpdateDscp_Type()
)
aclCurCfgAclRemarkOutProfUpdateDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgAclRemarkOutProfUpdateDscp.setStatus("current")


class _AclCurCfgAclRemarkAclBmap_Type(OctetString):
    """Custom type aclCurCfgAclRemarkAclBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AclCurCfgAclRemarkAclBmap_Type.__name__ = "OctetString"
_AclCurCfgAclRemarkAclBmap_Object = MibTableColumn
aclCurCfgAclRemarkAclBmap = _AclCurCfgAclRemarkAclBmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 5, 1, 7),
    _AclCurCfgAclRemarkAclBmap_Type()
)
aclCurCfgAclRemarkAclBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgAclRemarkAclBmap.setStatus("current")


class _AclCurCfgAclRemarkAclBlkBmap_Type(OctetString):
    """Custom type aclCurCfgAclRemarkAclBlkBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AclCurCfgAclRemarkAclBlkBmap_Type.__name__ = "OctetString"
_AclCurCfgAclRemarkAclBlkBmap_Object = MibTableColumn
aclCurCfgAclRemarkAclBlkBmap = _AclCurCfgAclRemarkAclBlkBmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 5, 1, 8),
    _AclCurCfgAclRemarkAclBlkBmap_Type()
)
aclCurCfgAclRemarkAclBlkBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgAclRemarkAclBlkBmap.setStatus("current")


class _AclCurCfgAclRemarkAclGrpBmap_Type(OctetString):
    """Custom type aclCurCfgAclRemarkAclGrpBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AclCurCfgAclRemarkAclGrpBmap_Type.__name__ = "OctetString"
_AclCurCfgAclRemarkAclGrpBmap_Object = MibTableColumn
aclCurCfgAclRemarkAclGrpBmap = _AclCurCfgAclRemarkAclGrpBmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 5, 1, 9),
    _AclCurCfgAclRemarkAclGrpBmap_Type()
)
aclCurCfgAclRemarkAclGrpBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgAclRemarkAclGrpBmap.setStatus("current")
_AclNewCfgPortAclRemarkTable_Object = MibTable
aclNewCfgPortAclRemarkTable = _AclNewCfgPortAclRemarkTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6)
)
if mibBuilder.loadTexts:
    aclNewCfgPortAclRemarkTable.setStatus("current")
_AclNewCfgPortAclRemarkTableEntry_Object = MibTableRow
aclNewCfgPortAclRemarkTableEntry = _AclNewCfgPortAclRemarkTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1)
)
aclNewCfgPortAclRemarkTableEntry.setIndexNames(
    (0, "BLADETYPE2-QOS-MIB", "aclNewCfgPortRemarkConfigIndex"),
    (0, "BLADETYPE2-QOS-MIB", "aclNewCfgAclRemarkIndex"),
)
if mibBuilder.loadTexts:
    aclNewCfgPortAclRemarkTableEntry.setStatus("current")
_AclNewCfgPortRemarkConfigIndex_Type = Integer32
_AclNewCfgPortRemarkConfigIndex_Object = MibTableColumn
aclNewCfgPortRemarkConfigIndex = _AclNewCfgPortRemarkConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 1),
    _AclNewCfgPortRemarkConfigIndex_Type()
)
aclNewCfgPortRemarkConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNewCfgPortRemarkConfigIndex.setStatus("current")
_AclNewCfgAclRemarkIndex_Type = Integer32
_AclNewCfgAclRemarkIndex_Object = MibTableColumn
aclNewCfgAclRemarkIndex = _AclNewCfgAclRemarkIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 2),
    _AclNewCfgAclRemarkIndex_Type()
)
aclNewCfgAclRemarkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNewCfgAclRemarkIndex.setStatus("current")


class _AclNewCfgAclRemarkInProfUpdatePri_Type(Integer32):
    """Custom type aclNewCfgAclRemarkInProfUpdatePri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AclNewCfgAclRemarkInProfUpdatePri_Type.__name__ = "Integer32"
_AclNewCfgAclRemarkInProfUpdatePri_Object = MibTableColumn
aclNewCfgAclRemarkInProfUpdatePri = _AclNewCfgAclRemarkInProfUpdatePri_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 3),
    _AclNewCfgAclRemarkInProfUpdatePri_Type()
)
aclNewCfgAclRemarkInProfUpdatePri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgAclRemarkInProfUpdatePri.setStatus("current")


class _AclNewCfgAclRemarkInProfUpdateTosPrec_Type(Integer32):
    """Custom type aclNewCfgAclRemarkInProfUpdateTosPrec based on Integer32"""
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


_AclNewCfgAclRemarkInProfUpdateTosPrec_Type.__name__ = "Integer32"
_AclNewCfgAclRemarkInProfUpdateTosPrec_Object = MibTableColumn
aclNewCfgAclRemarkInProfUpdateTosPrec = _AclNewCfgAclRemarkInProfUpdateTosPrec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 4),
    _AclNewCfgAclRemarkInProfUpdateTosPrec_Type()
)
aclNewCfgAclRemarkInProfUpdateTosPrec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgAclRemarkInProfUpdateTosPrec.setStatus("current")


class _AclNewCfgAclRemarkInProfUpdateDscp_Type(Integer32):
    """Custom type aclNewCfgAclRemarkInProfUpdateDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AclNewCfgAclRemarkInProfUpdateDscp_Type.__name__ = "Integer32"
_AclNewCfgAclRemarkInProfUpdateDscp_Object = MibTableColumn
aclNewCfgAclRemarkInProfUpdateDscp = _AclNewCfgAclRemarkInProfUpdateDscp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 5),
    _AclNewCfgAclRemarkInProfUpdateDscp_Type()
)
aclNewCfgAclRemarkInProfUpdateDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgAclRemarkInProfUpdateDscp.setStatus("current")


class _AclNewCfgAclRemarkOutProfUpdateDscp_Type(Integer32):
    """Custom type aclNewCfgAclRemarkOutProfUpdateDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AclNewCfgAclRemarkOutProfUpdateDscp_Type.__name__ = "Integer32"
_AclNewCfgAclRemarkOutProfUpdateDscp_Object = MibTableColumn
aclNewCfgAclRemarkOutProfUpdateDscp = _AclNewCfgAclRemarkOutProfUpdateDscp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 6),
    _AclNewCfgAclRemarkOutProfUpdateDscp_Type()
)
aclNewCfgAclRemarkOutProfUpdateDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgAclRemarkOutProfUpdateDscp.setStatus("current")
_AclNewCfgAclRemarkAssignAcl_Type = Unsigned32
_AclNewCfgAclRemarkAssignAcl_Object = MibTableColumn
aclNewCfgAclRemarkAssignAcl = _AclNewCfgAclRemarkAssignAcl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 7),
    _AclNewCfgAclRemarkAssignAcl_Type()
)
aclNewCfgAclRemarkAssignAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgAclRemarkAssignAcl.setStatus("current")
_AclNewCfgAclRemarkAssignAclBlk_Type = Unsigned32
_AclNewCfgAclRemarkAssignAclBlk_Object = MibTableColumn
aclNewCfgAclRemarkAssignAclBlk = _AclNewCfgAclRemarkAssignAclBlk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 8),
    _AclNewCfgAclRemarkAssignAclBlk_Type()
)
aclNewCfgAclRemarkAssignAclBlk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgAclRemarkAssignAclBlk.setStatus("current")
_AclNewCfgAclRemarkAssignAclGrp_Type = Unsigned32
_AclNewCfgAclRemarkAssignAclGrp_Object = MibTableColumn
aclNewCfgAclRemarkAssignAclGrp = _AclNewCfgAclRemarkAssignAclGrp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 9),
    _AclNewCfgAclRemarkAssignAclGrp_Type()
)
aclNewCfgAclRemarkAssignAclGrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgAclRemarkAssignAclGrp.setStatus("current")
_AclNewCfgAclRemarkUnAssignAcl_Type = Unsigned32
_AclNewCfgAclRemarkUnAssignAcl_Object = MibTableColumn
aclNewCfgAclRemarkUnAssignAcl = _AclNewCfgAclRemarkUnAssignAcl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 10),
    _AclNewCfgAclRemarkUnAssignAcl_Type()
)
aclNewCfgAclRemarkUnAssignAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgAclRemarkUnAssignAcl.setStatus("current")
_AclNewCfgAclRemarkUnAssignAclBlk_Type = Unsigned32
_AclNewCfgAclRemarkUnAssignAclBlk_Object = MibTableColumn
aclNewCfgAclRemarkUnAssignAclBlk = _AclNewCfgAclRemarkUnAssignAclBlk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 11),
    _AclNewCfgAclRemarkUnAssignAclBlk_Type()
)
aclNewCfgAclRemarkUnAssignAclBlk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgAclRemarkUnAssignAclBlk.setStatus("current")
_AclNewCfgAclRemarkUnAssignAclGrp_Type = Unsigned32
_AclNewCfgAclRemarkUnAssignAclGrp_Object = MibTableColumn
aclNewCfgAclRemarkUnAssignAclGrp = _AclNewCfgAclRemarkUnAssignAclGrp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 12),
    _AclNewCfgAclRemarkUnAssignAclGrp_Type()
)
aclNewCfgAclRemarkUnAssignAclGrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgAclRemarkUnAssignAclGrp.setStatus("current")


class _AclNewCfgAclRemarkAclBmap_Type(OctetString):
    """Custom type aclNewCfgAclRemarkAclBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AclNewCfgAclRemarkAclBmap_Type.__name__ = "OctetString"
_AclNewCfgAclRemarkAclBmap_Object = MibTableColumn
aclNewCfgAclRemarkAclBmap = _AclNewCfgAclRemarkAclBmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 13),
    _AclNewCfgAclRemarkAclBmap_Type()
)
aclNewCfgAclRemarkAclBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNewCfgAclRemarkAclBmap.setStatus("current")


class _AclNewCfgAclRemarkAclBlkBmap_Type(OctetString):
    """Custom type aclNewCfgAclRemarkAclBlkBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AclNewCfgAclRemarkAclBlkBmap_Type.__name__ = "OctetString"
_AclNewCfgAclRemarkAclBlkBmap_Object = MibTableColumn
aclNewCfgAclRemarkAclBlkBmap = _AclNewCfgAclRemarkAclBlkBmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 14),
    _AclNewCfgAclRemarkAclBlkBmap_Type()
)
aclNewCfgAclRemarkAclBlkBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNewCfgAclRemarkAclBlkBmap.setStatus("current")


class _AclNewCfgAclRemarkAclGrpBmap_Type(OctetString):
    """Custom type aclNewCfgAclRemarkAclGrpBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AclNewCfgAclRemarkAclGrpBmap_Type.__name__ = "OctetString"
_AclNewCfgAclRemarkAclGrpBmap_Object = MibTableColumn
aclNewCfgAclRemarkAclGrpBmap = _AclNewCfgAclRemarkAclGrpBmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 15),
    _AclNewCfgAclRemarkAclGrpBmap_Type()
)
aclNewCfgAclRemarkAclGrpBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNewCfgAclRemarkAclGrpBmap.setStatus("current")


class _AclNewCfgAclRemarkReset_Type(Integer32):
    """Custom type aclNewCfgAclRemarkReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_AclNewCfgAclRemarkReset_Type.__name__ = "Integer32"
_AclNewCfgAclRemarkReset_Object = MibTableColumn
aclNewCfgAclRemarkReset = _AclNewCfgAclRemarkReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 1, 2, 6, 1, 16),
    _AclNewCfgAclRemarkReset_Type()
)
aclNewCfgAclRemarkReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgAclRemarkReset.setStatus("current")
_QosStats_ObjectIdentity = ObjectIdentity
qosStats = _QosStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 2)
)
_QosInfo_ObjectIdentity = ObjectIdentity
qosInfo = _QosInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 3)
)
_QosOper_ObjectIdentity = ObjectIdentity
qosOper = _QosOper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 8, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLADETYPE2-QOS-MIB",
    **{"qos": qos,
       "qosConfigs": qosConfigs,
       "qos8021p": qos8021p,
       "qosCurCfgPortPriorityTable": qosCurCfgPortPriorityTable,
       "qosCurCfgPortPriorityEntry": qosCurCfgPortPriorityEntry,
       "qosCurCfgPortIndex": qosCurCfgPortIndex,
       "qosCurCfgPortPriority": qosCurCfgPortPriority,
       "qosNewCfgPortPriorityTable": qosNewCfgPortPriorityTable,
       "qosNewCfgPortPriorityEntry": qosNewCfgPortPriorityEntry,
       "qosNewCfgPortIndex": qosNewCfgPortIndex,
       "qosNewCfgPortPriority": qosNewCfgPortPriority,
       "qosCurCfgPriorityCoSTable": qosCurCfgPriorityCoSTable,
       "qosCurCfgPriorityCoSEntry": qosCurCfgPriorityCoSEntry,
       "qosCurCfgPriorityIndex": qosCurCfgPriorityIndex,
       "qosCurCfgPriorityCoSq": qosCurCfgPriorityCoSq,
       "qosNewCfgPriorityCoSTable": qosNewCfgPriorityCoSTable,
       "qosNewCfgPriorityCoSEntry": qosNewCfgPriorityCoSEntry,
       "qosNewCfgPriorityIndex": qosNewCfgPriorityIndex,
       "qosNewCfgPriorityCoSq": qosNewCfgPriorityCoSq,
       "qosCurCfgCosWeightTable": qosCurCfgCosWeightTable,
       "qosCurCfgCosWeightEntry": qosCurCfgCosWeightEntry,
       "qosCurCfgCosIndex": qosCurCfgCosIndex,
       "qosCurCfgCosWeight": qosCurCfgCosWeight,
       "qosNewCfgCosWeightTable": qosNewCfgCosWeightTable,
       "qosNewCfgCosWeightEntry": qosNewCfgCosWeightEntry,
       "qosNewCfgCosIndex": qosNewCfgCosIndex,
       "qosNewCfgCosWeight": qosNewCfgCosWeight,
       "qosCurCfgCosNum": qosCurCfgCosNum,
       "qosNewCfgCosNum": qosNewCfgCosNum,
       "aclCfg": aclCfg,
       "aclCurCfgPortTable": aclCurCfgPortTable,
       "aclCurCfgPortTableEntry": aclCurCfgPortTableEntry,
       "aclCurCfgPortIndex": aclCurCfgPortIndex,
       "aclCurCfgPortAclBmap": aclCurCfgPortAclBmap,
       "aclCurCfgPortAclBlkBmap": aclCurCfgPortAclBlkBmap,
       "aclCurCfgPortAclGrpBmap": aclCurCfgPortAclGrpBmap,
       "aclNewCfgPortTable": aclNewCfgPortTable,
       "aclNewCfgPortTableEntry": aclNewCfgPortTableEntry,
       "aclNewCfgPortIndex": aclNewCfgPortIndex,
       "aclNewCfgPortAddAcl": aclNewCfgPortAddAcl,
       "aclNewCfgPortAddAclBlk": aclNewCfgPortAddAclBlk,
       "aclNewCfgPortAddAclGrp": aclNewCfgPortAddAclGrp,
       "aclNewCfgPortRemoveAcl": aclNewCfgPortRemoveAcl,
       "aclNewCfgPortRemoveAclBlk": aclNewCfgPortRemoveAclBlk,
       "aclNewCfgPortRemoveAclGrp": aclNewCfgPortRemoveAclGrp,
       "aclNewCfgPortAclBmap": aclNewCfgPortAclBmap,
       "aclNewCfgPortAclBlkBmap": aclNewCfgPortAclBlkBmap,
       "aclNewCfgPortAclGrpBmap": aclNewCfgPortAclGrpBmap,
       "aclCurCfgPortAclMeterTable": aclCurCfgPortAclMeterTable,
       "aclCurCfgPortAclMeterTableEntry": aclCurCfgPortAclMeterTableEntry,
       "aclCurCfgPortMeterConfigIndex": aclCurCfgPortMeterConfigIndex,
       "aclCurCfgAclMeterIndex": aclCurCfgAclMeterIndex,
       "aclCurCfgAclMeterCommitRate": aclCurCfgAclMeterCommitRate,
       "aclCurCfgAclMeterMaxBurstSize": aclCurCfgAclMeterMaxBurstSize,
       "aclCurCfgAclMeterStatus": aclCurCfgAclMeterStatus,
       "aclCurCfgAclMeterDropOrPass": aclCurCfgAclMeterDropOrPass,
       "aclCurCfgAclMeterAclBmap": aclCurCfgAclMeterAclBmap,
       "aclCurCfgAclMeterAclBlkBmap": aclCurCfgAclMeterAclBlkBmap,
       "aclCurCfgAclMeterAclGrpBmap": aclCurCfgAclMeterAclGrpBmap,
       "aclNewCfgPortAclMeterTable": aclNewCfgPortAclMeterTable,
       "aclNewCfgPortAclMeterTableEntry": aclNewCfgPortAclMeterTableEntry,
       "aclNewCfgPortMeterConfigIndex": aclNewCfgPortMeterConfigIndex,
       "aclNewCfgAclMeterIndex": aclNewCfgAclMeterIndex,
       "aclNewCfgAclMeterCommitRate": aclNewCfgAclMeterCommitRate,
       "aclNewCfgAclMeterMaxBurstSize": aclNewCfgAclMeterMaxBurstSize,
       "aclNewCfgAclMeterStatus": aclNewCfgAclMeterStatus,
       "aclNewCfgAclMeterDropOrPass": aclNewCfgAclMeterDropOrPass,
       "aclNewCfgAclMeterAssignAcl": aclNewCfgAclMeterAssignAcl,
       "aclNewCfgAclMeterAssignAclBlk": aclNewCfgAclMeterAssignAclBlk,
       "aclNewCfgAclMeterAssignAclGrp": aclNewCfgAclMeterAssignAclGrp,
       "aclNewCfgAclMeterUnAssignAcl": aclNewCfgAclMeterUnAssignAcl,
       "aclNewCfgAclMeterUnAssignAclBlk": aclNewCfgAclMeterUnAssignAclBlk,
       "aclNewCfgAclMeterUnAssignAclGrp": aclNewCfgAclMeterUnAssignAclGrp,
       "aclNewCfgAclMeterAclBmap": aclNewCfgAclMeterAclBmap,
       "aclNewCfgAclMeterAclBlkBmap": aclNewCfgAclMeterAclBlkBmap,
       "aclNewCfgAclMeterAclGrpBmap": aclNewCfgAclMeterAclGrpBmap,
       "aclCurCfgPortAclRemarkTable": aclCurCfgPortAclRemarkTable,
       "aclCurCfgPortAclRemarkTableEntry": aclCurCfgPortAclRemarkTableEntry,
       "aclCurCfgPortRemarkConfigIndex": aclCurCfgPortRemarkConfigIndex,
       "aclCurCfgAclRemarkIndex": aclCurCfgAclRemarkIndex,
       "aclCurCfgAclRemarkInProfUpdatePri": aclCurCfgAclRemarkInProfUpdatePri,
       "aclCurCfgAclRemarkInProfUpdateTosPrec": aclCurCfgAclRemarkInProfUpdateTosPrec,
       "aclCurCfgAclRemarkInProfUpdateDscp": aclCurCfgAclRemarkInProfUpdateDscp,
       "aclCurCfgAclRemarkOutProfUpdateDscp": aclCurCfgAclRemarkOutProfUpdateDscp,
       "aclCurCfgAclRemarkAclBmap": aclCurCfgAclRemarkAclBmap,
       "aclCurCfgAclRemarkAclBlkBmap": aclCurCfgAclRemarkAclBlkBmap,
       "aclCurCfgAclRemarkAclGrpBmap": aclCurCfgAclRemarkAclGrpBmap,
       "aclNewCfgPortAclRemarkTable": aclNewCfgPortAclRemarkTable,
       "aclNewCfgPortAclRemarkTableEntry": aclNewCfgPortAclRemarkTableEntry,
       "aclNewCfgPortRemarkConfigIndex": aclNewCfgPortRemarkConfigIndex,
       "aclNewCfgAclRemarkIndex": aclNewCfgAclRemarkIndex,
       "aclNewCfgAclRemarkInProfUpdatePri": aclNewCfgAclRemarkInProfUpdatePri,
       "aclNewCfgAclRemarkInProfUpdateTosPrec": aclNewCfgAclRemarkInProfUpdateTosPrec,
       "aclNewCfgAclRemarkInProfUpdateDscp": aclNewCfgAclRemarkInProfUpdateDscp,
       "aclNewCfgAclRemarkOutProfUpdateDscp": aclNewCfgAclRemarkOutProfUpdateDscp,
       "aclNewCfgAclRemarkAssignAcl": aclNewCfgAclRemarkAssignAcl,
       "aclNewCfgAclRemarkAssignAclBlk": aclNewCfgAclRemarkAssignAclBlk,
       "aclNewCfgAclRemarkAssignAclGrp": aclNewCfgAclRemarkAssignAclGrp,
       "aclNewCfgAclRemarkUnAssignAcl": aclNewCfgAclRemarkUnAssignAcl,
       "aclNewCfgAclRemarkUnAssignAclBlk": aclNewCfgAclRemarkUnAssignAclBlk,
       "aclNewCfgAclRemarkUnAssignAclGrp": aclNewCfgAclRemarkUnAssignAclGrp,
       "aclNewCfgAclRemarkAclBmap": aclNewCfgAclRemarkAclBmap,
       "aclNewCfgAclRemarkAclBlkBmap": aclNewCfgAclRemarkAclBlkBmap,
       "aclNewCfgAclRemarkAclGrpBmap": aclNewCfgAclRemarkAclGrpBmap,
       "aclNewCfgAclRemarkReset": aclNewCfgAclRemarkReset,
       "qosStats": qosStats,
       "qosInfo": qosInfo,
       "qosOper": qosOper}
)
