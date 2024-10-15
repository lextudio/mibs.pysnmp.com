# SNMP MIB module (HP-SN-IP-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-SN-IP-ACL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:44 2024
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

(snIp,) = mibBuilder.importSymbols(
    "HP-SN-ROOT-MIB",
    "snIp")

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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class RtrStatus(Integer32):
    """Custom type RtrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )





class SnRowStatus(Integer32):
    """Custom type SnRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("other", 1),
          ("valid", 2))
    )





class Action(Integer32):
    """Custom type Action based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )





class TruthVal(Integer32):
    """Custom type TruthVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )





class AclNumber(Integer32):
    """Custom type AclNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 199),
    )





class Operator(Integer32):
    """Custom type Operator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("eq", 0),
          ("gt", 3),
          ("lt", 2),
          ("neq", 1),
          ("range", 4),
          ("undefined", 7))
    )





class IpProtocol(Integer32):
    """Custom type IpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class PrecedenceValue(Integer32):
    """Custom type PrecedenceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("critical", 5),
          ("flash", 3),
          ("flashoverride", 4),
          ("immediate", 2),
          ("internet", 6),
          ("network", 7),
          ("priority", 1),
          ("routine", 0),
          ("undefined", 8))
    )





class TosValue(Integer32):
    """Custom type TosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("maxReliability", 2),
          ("maxThroughput", 4),
          ("minDelay", 8),
          ("minMonetaryCost", 1),
          ("normal", 0),
          ("tosValue10", 10),
          ("tosValue11", 11),
          ("tosValue12", 12),
          ("tosValue13", 13),
          ("tosValue14", 14),
          ("tosValue15", 15),
          ("tosValue3", 3),
          ("tosValue5", 5),
          ("tosValue6", 6),
          ("tosValue7", 7),
          ("tosValue9", 9),
          ("undefined", 16))
    )





class Direction(Integer32):
    """Custom type Direction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 0),
          ("outbound", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnAgAcl_ObjectIdentity = ObjectIdentity
snAgAcl = _SnAgAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15)
)
_SnAgAclGlobal_ObjectIdentity = ObjectIdentity
snAgAclGlobal = _SnAgAclGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 1)
)
_SnAgAclGblCurRowIndex_Type = Integer32
_SnAgAclGblCurRowIndex_Object = MibScalar
snAgAclGblCurRowIndex = _SnAgAclGblCurRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 1, 1),
    _SnAgAclGblCurRowIndex_Type()
)
snAgAclGblCurRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgAclGblCurRowIndex.setStatus("mandatory")
_SnAgAclTable_Object = MibTable
snAgAclTable = _SnAgAclTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2)
)
if mibBuilder.loadTexts:
    snAgAclTable.setStatus("mandatory")
_SnAgAclEntry_Object = MibTableRow
snAgAclEntry = _SnAgAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1)
)
snAgAclEntry.setIndexNames(
    (0, "HP-SN-IP-ACL-MIB", "snAgAclIndex"),
)
if mibBuilder.loadTexts:
    snAgAclEntry.setStatus("mandatory")
_SnAgAclIndex_Type = Integer32
_SnAgAclIndex_Object = MibTableColumn
snAgAclIndex = _SnAgAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 1),
    _SnAgAclIndex_Type()
)
snAgAclIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgAclIndex.setStatus("mandatory")
_SnAgAclNumber_Type = AclNumber
_SnAgAclNumber_Object = MibTableColumn
snAgAclNumber = _SnAgAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 2),
    _SnAgAclNumber_Type()
)
snAgAclNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclNumber.setStatus("mandatory")
_SnAgAclName_Type = DisplayString
_SnAgAclName_Object = MibTableColumn
snAgAclName = _SnAgAclName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 3),
    _SnAgAclName_Type()
)
snAgAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclName.setStatus("mandatory")
_SnAgAclAction_Type = Action
_SnAgAclAction_Object = MibTableColumn
snAgAclAction = _SnAgAclAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 4),
    _SnAgAclAction_Type()
)
snAgAclAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclAction.setStatus("mandatory")
_SnAgAclProtocol_Type = IpProtocol
_SnAgAclProtocol_Object = MibTableColumn
snAgAclProtocol = _SnAgAclProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 5),
    _SnAgAclProtocol_Type()
)
snAgAclProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclProtocol.setStatus("mandatory")
_SnAgAclSourceIp_Type = IpAddress
_SnAgAclSourceIp_Object = MibTableColumn
snAgAclSourceIp = _SnAgAclSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 6),
    _SnAgAclSourceIp_Type()
)
snAgAclSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclSourceIp.setStatus("mandatory")
_SnAgAclSourceMask_Type = IpAddress
_SnAgAclSourceMask_Object = MibTableColumn
snAgAclSourceMask = _SnAgAclSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 7),
    _SnAgAclSourceMask_Type()
)
snAgAclSourceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclSourceMask.setStatus("mandatory")
_SnAgAclSourceOperator_Type = Operator
_SnAgAclSourceOperator_Object = MibTableColumn
snAgAclSourceOperator = _SnAgAclSourceOperator_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 8),
    _SnAgAclSourceOperator_Type()
)
snAgAclSourceOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclSourceOperator.setStatus("mandatory")


class _SnAgAclSourceOperand1_Type(Integer32):
    """Custom type snAgAclSourceOperand1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnAgAclSourceOperand1_Type.__name__ = "Integer32"
_SnAgAclSourceOperand1_Object = MibTableColumn
snAgAclSourceOperand1 = _SnAgAclSourceOperand1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 9),
    _SnAgAclSourceOperand1_Type()
)
snAgAclSourceOperand1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclSourceOperand1.setStatus("mandatory")


class _SnAgAclSourceOperand2_Type(Integer32):
    """Custom type snAgAclSourceOperand2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnAgAclSourceOperand2_Type.__name__ = "Integer32"
_SnAgAclSourceOperand2_Object = MibTableColumn
snAgAclSourceOperand2 = _SnAgAclSourceOperand2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 10),
    _SnAgAclSourceOperand2_Type()
)
snAgAclSourceOperand2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclSourceOperand2.setStatus("mandatory")
_SnAgAclDestinationIp_Type = IpAddress
_SnAgAclDestinationIp_Object = MibTableColumn
snAgAclDestinationIp = _SnAgAclDestinationIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 11),
    _SnAgAclDestinationIp_Type()
)
snAgAclDestinationIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclDestinationIp.setStatus("mandatory")
_SnAgAclDestinationMask_Type = IpAddress
_SnAgAclDestinationMask_Object = MibTableColumn
snAgAclDestinationMask = _SnAgAclDestinationMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 12),
    _SnAgAclDestinationMask_Type()
)
snAgAclDestinationMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclDestinationMask.setStatus("mandatory")
_SnAgAclDestinationOperator_Type = Operator
_SnAgAclDestinationOperator_Object = MibTableColumn
snAgAclDestinationOperator = _SnAgAclDestinationOperator_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 13),
    _SnAgAclDestinationOperator_Type()
)
snAgAclDestinationOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclDestinationOperator.setStatus("mandatory")


class _SnAgAclDestinationOperand1_Type(Integer32):
    """Custom type snAgAclDestinationOperand1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnAgAclDestinationOperand1_Type.__name__ = "Integer32"
_SnAgAclDestinationOperand1_Object = MibTableColumn
snAgAclDestinationOperand1 = _SnAgAclDestinationOperand1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 14),
    _SnAgAclDestinationOperand1_Type()
)
snAgAclDestinationOperand1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclDestinationOperand1.setStatus("mandatory")


class _SnAgAclDestinationOperand2_Type(Integer32):
    """Custom type snAgAclDestinationOperand2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnAgAclDestinationOperand2_Type.__name__ = "Integer32"
_SnAgAclDestinationOperand2_Object = MibTableColumn
snAgAclDestinationOperand2 = _SnAgAclDestinationOperand2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 15),
    _SnAgAclDestinationOperand2_Type()
)
snAgAclDestinationOperand2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclDestinationOperand2.setStatus("mandatory")
_SnAgAclPrecedence_Type = PrecedenceValue
_SnAgAclPrecedence_Object = MibTableColumn
snAgAclPrecedence = _SnAgAclPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 16),
    _SnAgAclPrecedence_Type()
)
snAgAclPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclPrecedence.setStatus("mandatory")
_SnAgAclTos_Type = TosValue
_SnAgAclTos_Object = MibTableColumn
snAgAclTos = _SnAgAclTos_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 17),
    _SnAgAclTos_Type()
)
snAgAclTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclTos.setStatus("mandatory")
_SnAgAclEstablished_Type = RtrStatus
_SnAgAclEstablished_Object = MibTableColumn
snAgAclEstablished = _SnAgAclEstablished_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 18),
    _SnAgAclEstablished_Type()
)
snAgAclEstablished.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclEstablished.setStatus("mandatory")
_SnAgAclLogOption_Type = TruthVal
_SnAgAclLogOption_Object = MibTableColumn
snAgAclLogOption = _SnAgAclLogOption_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 19),
    _SnAgAclLogOption_Type()
)
snAgAclLogOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclLogOption.setStatus("mandatory")
_SnAgAclStandardFlag_Type = TruthVal
_SnAgAclStandardFlag_Object = MibTableColumn
snAgAclStandardFlag = _SnAgAclStandardFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 20),
    _SnAgAclStandardFlag_Type()
)
snAgAclStandardFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclStandardFlag.setStatus("mandatory")
_SnAgAclRowStatus_Type = SnRowStatus
_SnAgAclRowStatus_Object = MibTableColumn
snAgAclRowStatus = _SnAgAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 21),
    _SnAgAclRowStatus_Type()
)
snAgAclRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclRowStatus.setStatus("mandatory")
_SnAgAclFlowCounter_Type = Counter64
_SnAgAclFlowCounter_Object = MibTableColumn
snAgAclFlowCounter = _SnAgAclFlowCounter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 22),
    _SnAgAclFlowCounter_Type()
)
snAgAclFlowCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgAclFlowCounter.setStatus("mandatory")
_SnAgAclPacketCounter_Type = Counter64
_SnAgAclPacketCounter_Object = MibTableColumn
snAgAclPacketCounter = _SnAgAclPacketCounter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 23),
    _SnAgAclPacketCounter_Type()
)
snAgAclPacketCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgAclPacketCounter.setStatus("mandatory")
_SnAgAclComments_Type = DisplayString
_SnAgAclComments_Object = MibTableColumn
snAgAclComments = _SnAgAclComments_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 24),
    _SnAgAclComments_Type()
)
snAgAclComments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclComments.setStatus("mandatory")


class _SnAgAclIpPriority_Type(Integer32):
    """Custom type snAgAclIpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_SnAgAclIpPriority_Type.__name__ = "Integer32"
_SnAgAclIpPriority_Object = MibTableColumn
snAgAclIpPriority = _SnAgAclIpPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 25),
    _SnAgAclIpPriority_Type()
)
snAgAclIpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclIpPriority.setStatus("mandatory")


class _SnAgAclPriorityForce_Type(Integer32):
    """Custom type snAgAclPriorityForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_SnAgAclPriorityForce_Type.__name__ = "Integer32"
_SnAgAclPriorityForce_Object = MibTableColumn
snAgAclPriorityForce = _SnAgAclPriorityForce_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 26),
    _SnAgAclPriorityForce_Type()
)
snAgAclPriorityForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclPriorityForce.setStatus("mandatory")


class _SnAgAclPriorityMapping_Type(Integer32):
    """Custom type snAgAclPriorityMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SnAgAclPriorityMapping_Type.__name__ = "Integer32"
_SnAgAclPriorityMapping_Object = MibTableColumn
snAgAclPriorityMapping = _SnAgAclPriorityMapping_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 27),
    _SnAgAclPriorityMapping_Type()
)
snAgAclPriorityMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclPriorityMapping.setStatus("mandatory")


class _SnAgAclDscpMarking_Type(Integer32):
    """Custom type snAgAclDscpMarking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_SnAgAclDscpMarking_Type.__name__ = "Integer32"
_SnAgAclDscpMarking_Object = MibTableColumn
snAgAclDscpMarking = _SnAgAclDscpMarking_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 28),
    _SnAgAclDscpMarking_Type()
)
snAgAclDscpMarking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclDscpMarking.setStatus("mandatory")


class _SnAgAclDscpMapping_Type(Integer32):
    """Custom type snAgAclDscpMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_SnAgAclDscpMapping_Type.__name__ = "Integer32"
_SnAgAclDscpMapping_Object = MibTableColumn
snAgAclDscpMapping = _SnAgAclDscpMapping_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 2, 1, 29),
    _SnAgAclDscpMapping_Type()
)
snAgAclDscpMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclDscpMapping.setStatus("mandatory")
_SnAgAclBindToPortTable_Object = MibTable
snAgAclBindToPortTable = _SnAgAclBindToPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 3)
)
if mibBuilder.loadTexts:
    snAgAclBindToPortTable.setStatus("mandatory")
_SnAgAclBindToPortEntry_Object = MibTableRow
snAgAclBindToPortEntry = _SnAgAclBindToPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 3, 1)
)
snAgAclBindToPortEntry.setIndexNames(
    (0, "HP-SN-IP-ACL-MIB", "snAgAclPortNum"),
    (0, "HP-SN-IP-ACL-MIB", "snAgAclPortBindDirection"),
)
if mibBuilder.loadTexts:
    snAgAclBindToPortEntry.setStatus("mandatory")
_SnAgAclPortNum_Type = Integer32
_SnAgAclPortNum_Object = MibTableColumn
snAgAclPortNum = _SnAgAclPortNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 3, 1, 1),
    _SnAgAclPortNum_Type()
)
snAgAclPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgAclPortNum.setStatus("mandatory")
_SnAgAclPortBindDirection_Type = Direction
_SnAgAclPortBindDirection_Object = MibTableColumn
snAgAclPortBindDirection = _SnAgAclPortBindDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 3, 1, 2),
    _SnAgAclPortBindDirection_Type()
)
snAgAclPortBindDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgAclPortBindDirection.setStatus("mandatory")
_SnAgAclNum_Type = Integer32
_SnAgAclNum_Object = MibTableColumn
snAgAclNum = _SnAgAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 3, 1, 3),
    _SnAgAclNum_Type()
)
snAgAclNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclNum.setStatus("mandatory")
_SnAgAclNameString_Type = DisplayString
_SnAgAclNameString_Object = MibTableColumn
snAgAclNameString = _SnAgAclNameString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 3, 1, 4),
    _SnAgAclNameString_Type()
)
snAgAclNameString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclNameString.setStatus("mandatory")
_SnAgBindPortListInVirtualInterface_Type = OctetString
_SnAgBindPortListInVirtualInterface_Object = MibTableColumn
snAgBindPortListInVirtualInterface = _SnAgBindPortListInVirtualInterface_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 3, 1, 5),
    _SnAgBindPortListInVirtualInterface_Type()
)
snAgBindPortListInVirtualInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgBindPortListInVirtualInterface.setStatus("mandatory")
_SnAgAclPortRowStatus_Type = SnRowStatus
_SnAgAclPortRowStatus_Object = MibTableColumn
snAgAclPortRowStatus = _SnAgAclPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 15, 3, 1, 6),
    _SnAgAclPortRowStatus_Type()
)
snAgAclPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclPortRowStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-SN-IP-ACL-MIB",
    **{"DisplayString": DisplayString,
       "RtrStatus": RtrStatus,
       "SnRowStatus": SnRowStatus,
       "Action": Action,
       "TruthVal": TruthVal,
       "AclNumber": AclNumber,
       "Operator": Operator,
       "IpProtocol": IpProtocol,
       "PrecedenceValue": PrecedenceValue,
       "TosValue": TosValue,
       "Direction": Direction,
       "snAgAcl": snAgAcl,
       "snAgAclGlobal": snAgAclGlobal,
       "snAgAclGblCurRowIndex": snAgAclGblCurRowIndex,
       "snAgAclTable": snAgAclTable,
       "snAgAclEntry": snAgAclEntry,
       "snAgAclIndex": snAgAclIndex,
       "snAgAclNumber": snAgAclNumber,
       "snAgAclName": snAgAclName,
       "snAgAclAction": snAgAclAction,
       "snAgAclProtocol": snAgAclProtocol,
       "snAgAclSourceIp": snAgAclSourceIp,
       "snAgAclSourceMask": snAgAclSourceMask,
       "snAgAclSourceOperator": snAgAclSourceOperator,
       "snAgAclSourceOperand1": snAgAclSourceOperand1,
       "snAgAclSourceOperand2": snAgAclSourceOperand2,
       "snAgAclDestinationIp": snAgAclDestinationIp,
       "snAgAclDestinationMask": snAgAclDestinationMask,
       "snAgAclDestinationOperator": snAgAclDestinationOperator,
       "snAgAclDestinationOperand1": snAgAclDestinationOperand1,
       "snAgAclDestinationOperand2": snAgAclDestinationOperand2,
       "snAgAclPrecedence": snAgAclPrecedence,
       "snAgAclTos": snAgAclTos,
       "snAgAclEstablished": snAgAclEstablished,
       "snAgAclLogOption": snAgAclLogOption,
       "snAgAclStandardFlag": snAgAclStandardFlag,
       "snAgAclRowStatus": snAgAclRowStatus,
       "snAgAclFlowCounter": snAgAclFlowCounter,
       "snAgAclPacketCounter": snAgAclPacketCounter,
       "snAgAclComments": snAgAclComments,
       "snAgAclIpPriority": snAgAclIpPriority,
       "snAgAclPriorityForce": snAgAclPriorityForce,
       "snAgAclPriorityMapping": snAgAclPriorityMapping,
       "snAgAclDscpMarking": snAgAclDscpMarking,
       "snAgAclDscpMapping": snAgAclDscpMapping,
       "snAgAclBindToPortTable": snAgAclBindToPortTable,
       "snAgAclBindToPortEntry": snAgAclBindToPortEntry,
       "snAgAclPortNum": snAgAclPortNum,
       "snAgAclPortBindDirection": snAgAclPortBindDirection,
       "snAgAclNum": snAgAclNum,
       "snAgAclNameString": snAgAclNameString,
       "snAgBindPortListInVirtualInterface": snAgBindPortListInVirtualInterface,
       "snAgAclPortRowStatus": snAgAclPortRowStatus}
)
