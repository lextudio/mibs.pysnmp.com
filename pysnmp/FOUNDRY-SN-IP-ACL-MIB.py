# SNMP MIB module (FOUNDRY-SN-IP-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FOUNDRY-SN-IP-ACL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:32 2024
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

(RtrStatus,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-IP-MIB",
    "RtrStatus")

(router,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "router")

(FdryVlanIdOrNoneTC,
 PortQosTC) = mibBuilder.importSymbols(
    "FOUNDRY-SN-SWITCH-GROUP-MIB",
    "FdryVlanIdOrNoneTC",
    "PortQosTC")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

snAgAcl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15)
)
snAgAcl.setRevisions(
        ("2014-01-28 00:00",
         "2011-03-02 00:00",
         "2010-06-02 00:00",
         "2009-09-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SnRowStatus(Integer32, TextualConvention):
    status = "current"
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



class Action(Integer32, TextualConvention):
    status = "current"
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



class TruthVal(Integer32, TextualConvention):
    status = "current"
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



class FdryClauseIndexTC(Unsigned32, TextualConvention):
    status = "current"


class AclNumber(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5100),
    )



class AclNameString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class Operator(Integer32, TextualConvention):
    status = "current"
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



class IpProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class PrecedenceValue(Integer32, TextualConvention):
    status = "current"
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



class TosValue(Integer32, TextualConvention):
    status = "current"
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



class Direction(Integer32, TextualConvention):
    status = "current"
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



class FdryEnetTypeOrZeroTC(Integer32, TextualConvention):
    status = "current"
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
        *(("arp", 2),
          ("invalid", 0),
          ("ipv4", 1),
          ("ipv6", 3))
    )



# MIB Managed Objects in the order of their OIDs

_SnAgAclGlobal_ObjectIdentity = ObjectIdentity
snAgAclGlobal = _SnAgAclGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 1)
)
_SnAgAclGblCurRowIndex_Type = Integer32
_SnAgAclGblCurRowIndex_Object = MibScalar
snAgAclGblCurRowIndex = _SnAgAclGblCurRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 1, 1),
    _SnAgAclGblCurRowIndex_Type()
)
snAgAclGblCurRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgAclGblCurRowIndex.setStatus("current")


class _SnAgAclGblAcctEnable_Type(Integer32):
    """Custom type snAgAclGblAcctEnable based on Integer32"""
    defaultValue = 0

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


_SnAgAclGblAcctEnable_Type.__name__ = "Integer32"
_SnAgAclGblAcctEnable_Object = MibScalar
snAgAclGblAcctEnable = _SnAgAclGblAcctEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 1, 2),
    _SnAgAclGblAcctEnable_Type()
)
snAgAclGblAcctEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclGblAcctEnable.setStatus("current")
_SnAgAclGblIfIPv4AcctClear_Type = InterfaceIndexOrZero
_SnAgAclGblIfIPv4AcctClear_Object = MibScalar
snAgAclGblIfIPv4AcctClear = _SnAgAclGblIfIPv4AcctClear_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 1, 3),
    _SnAgAclGblIfIPv4AcctClear_Type()
)
snAgAclGblIfIPv4AcctClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclGblIfIPv4AcctClear.setStatus("current")
_SnAgAclGblIfIPv6AcctClear_Type = InterfaceIndexOrZero
_SnAgAclGblIfIPv6AcctClear_Object = MibScalar
snAgAclGblIfIPv6AcctClear = _SnAgAclGblIfIPv6AcctClear_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 1, 4),
    _SnAgAclGblIfIPv6AcctClear_Type()
)
snAgAclGblIfIPv6AcctClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclGblIfIPv6AcctClear.setStatus("current")
_SnAgAclGblRebindAclNumber_Type = AclNumber
_SnAgAclGblRebindAclNumber_Object = MibScalar
snAgAclGblRebindAclNumber = _SnAgAclGblRebindAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 1, 5),
    _SnAgAclGblRebindAclNumber_Type()
)
snAgAclGblRebindAclNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclGblRebindAclNumber.setStatus("current")
_SnAgAclGblRebindAclName_Type = DisplayString
_SnAgAclGblRebindAclName_Object = MibScalar
snAgAclGblRebindAclName = _SnAgAclGblRebindAclName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 1, 6),
    _SnAgAclGblRebindAclName_Type()
)
snAgAclGblRebindAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclGblRebindAclName.setStatus("current")
_BrcdPbrAclAccntFilterAclName_Type = DisplayString
_BrcdPbrAclAccntFilterAclName_Object = MibScalar
brcdPbrAclAccntFilterAclName = _BrcdPbrAclAccntFilterAclName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 1, 7),
    _BrcdPbrAclAccntFilterAclName_Type()
)
brcdPbrAclAccntFilterAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdPbrAclAccntFilterAclName.setStatus("current")


class _BrcdPbrAclAccntCounterType_Type(Integer32):
    """Custom type brcdPbrAclAccntCounterType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cumulative", 1),
          ("last5min", 2))
    )


_BrcdPbrAclAccntCounterType_Type.__name__ = "Integer32"
_BrcdPbrAclAccntCounterType_Object = MibScalar
brcdPbrAclAccntCounterType = _BrcdPbrAclAccntCounterType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 1, 8),
    _BrcdPbrAclAccntCounterType_Type()
)
brcdPbrAclAccntCounterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdPbrAclAccntCounterType.setStatus("current")
_SnAgAclTable_Object = MibTable
snAgAclTable = _SnAgAclTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2)
)
if mibBuilder.loadTexts:
    snAgAclTable.setStatus("current")
_SnAgAclEntry_Object = MibTableRow
snAgAclEntry = _SnAgAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1)
)
snAgAclEntry.setIndexNames(
    (0, "FOUNDRY-SN-IP-ACL-MIB", "snAgAclIndex"),
)
if mibBuilder.loadTexts:
    snAgAclEntry.setStatus("current")
_SnAgAclIndex_Type = Integer32
_SnAgAclIndex_Object = MibTableColumn
snAgAclIndex = _SnAgAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 1),
    _SnAgAclIndex_Type()
)
snAgAclIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgAclIndex.setStatus("current")
_SnAgAclNumber_Type = AclNumber
_SnAgAclNumber_Object = MibTableColumn
snAgAclNumber = _SnAgAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 2),
    _SnAgAclNumber_Type()
)
snAgAclNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclNumber.setStatus("current")
_SnAgAclName_Type = DisplayString
_SnAgAclName_Object = MibTableColumn
snAgAclName = _SnAgAclName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 3),
    _SnAgAclName_Type()
)
snAgAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclName.setStatus("current")
_SnAgAclAction_Type = Action
_SnAgAclAction_Object = MibTableColumn
snAgAclAction = _SnAgAclAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 4),
    _SnAgAclAction_Type()
)
snAgAclAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclAction.setStatus("current")
_SnAgAclProtocol_Type = IpProtocol
_SnAgAclProtocol_Object = MibTableColumn
snAgAclProtocol = _SnAgAclProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 5),
    _SnAgAclProtocol_Type()
)
snAgAclProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclProtocol.setStatus("current")
_SnAgAclSourceIp_Type = IpAddress
_SnAgAclSourceIp_Object = MibTableColumn
snAgAclSourceIp = _SnAgAclSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 6),
    _SnAgAclSourceIp_Type()
)
snAgAclSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclSourceIp.setStatus("current")
_SnAgAclSourceMask_Type = IpAddress
_SnAgAclSourceMask_Object = MibTableColumn
snAgAclSourceMask = _SnAgAclSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 7),
    _SnAgAclSourceMask_Type()
)
snAgAclSourceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclSourceMask.setStatus("current")
_SnAgAclSourceOperator_Type = Operator
_SnAgAclSourceOperator_Object = MibTableColumn
snAgAclSourceOperator = _SnAgAclSourceOperator_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 8),
    _SnAgAclSourceOperator_Type()
)
snAgAclSourceOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclSourceOperator.setStatus("current")


class _SnAgAclSourceOperand1_Type(Integer32):
    """Custom type snAgAclSourceOperand1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnAgAclSourceOperand1_Type.__name__ = "Integer32"
_SnAgAclSourceOperand1_Object = MibTableColumn
snAgAclSourceOperand1 = _SnAgAclSourceOperand1_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 9),
    _SnAgAclSourceOperand1_Type()
)
snAgAclSourceOperand1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclSourceOperand1.setStatus("current")


class _SnAgAclSourceOperand2_Type(Integer32):
    """Custom type snAgAclSourceOperand2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnAgAclSourceOperand2_Type.__name__ = "Integer32"
_SnAgAclSourceOperand2_Object = MibTableColumn
snAgAclSourceOperand2 = _SnAgAclSourceOperand2_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 10),
    _SnAgAclSourceOperand2_Type()
)
snAgAclSourceOperand2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclSourceOperand2.setStatus("current")
_SnAgAclDestinationIp_Type = IpAddress
_SnAgAclDestinationIp_Object = MibTableColumn
snAgAclDestinationIp = _SnAgAclDestinationIp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 11),
    _SnAgAclDestinationIp_Type()
)
snAgAclDestinationIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclDestinationIp.setStatus("current")
_SnAgAclDestinationMask_Type = IpAddress
_SnAgAclDestinationMask_Object = MibTableColumn
snAgAclDestinationMask = _SnAgAclDestinationMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 12),
    _SnAgAclDestinationMask_Type()
)
snAgAclDestinationMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclDestinationMask.setStatus("current")
_SnAgAclDestinationOperator_Type = Operator
_SnAgAclDestinationOperator_Object = MibTableColumn
snAgAclDestinationOperator = _SnAgAclDestinationOperator_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 13),
    _SnAgAclDestinationOperator_Type()
)
snAgAclDestinationOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclDestinationOperator.setStatus("current")


class _SnAgAclDestinationOperand1_Type(Integer32):
    """Custom type snAgAclDestinationOperand1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnAgAclDestinationOperand1_Type.__name__ = "Integer32"
_SnAgAclDestinationOperand1_Object = MibTableColumn
snAgAclDestinationOperand1 = _SnAgAclDestinationOperand1_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 14),
    _SnAgAclDestinationOperand1_Type()
)
snAgAclDestinationOperand1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclDestinationOperand1.setStatus("current")


class _SnAgAclDestinationOperand2_Type(Integer32):
    """Custom type snAgAclDestinationOperand2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnAgAclDestinationOperand2_Type.__name__ = "Integer32"
_SnAgAclDestinationOperand2_Object = MibTableColumn
snAgAclDestinationOperand2 = _SnAgAclDestinationOperand2_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 15),
    _SnAgAclDestinationOperand2_Type()
)
snAgAclDestinationOperand2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclDestinationOperand2.setStatus("current")
_SnAgAclPrecedence_Type = PrecedenceValue
_SnAgAclPrecedence_Object = MibTableColumn
snAgAclPrecedence = _SnAgAclPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 16),
    _SnAgAclPrecedence_Type()
)
snAgAclPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclPrecedence.setStatus("current")
_SnAgAclTos_Type = TosValue
_SnAgAclTos_Object = MibTableColumn
snAgAclTos = _SnAgAclTos_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 17),
    _SnAgAclTos_Type()
)
snAgAclTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclTos.setStatus("current")
_SnAgAclEstablished_Type = RtrStatus
_SnAgAclEstablished_Object = MibTableColumn
snAgAclEstablished = _SnAgAclEstablished_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 18),
    _SnAgAclEstablished_Type()
)
snAgAclEstablished.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclEstablished.setStatus("current")
_SnAgAclLogOption_Type = TruthVal
_SnAgAclLogOption_Object = MibTableColumn
snAgAclLogOption = _SnAgAclLogOption_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 19),
    _SnAgAclLogOption_Type()
)
snAgAclLogOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclLogOption.setStatus("current")
_SnAgAclStandardFlag_Type = TruthVal
_SnAgAclStandardFlag_Object = MibTableColumn
snAgAclStandardFlag = _SnAgAclStandardFlag_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 20),
    _SnAgAclStandardFlag_Type()
)
snAgAclStandardFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclStandardFlag.setStatus("current")
_SnAgAclRowStatus_Type = SnRowStatus
_SnAgAclRowStatus_Object = MibTableColumn
snAgAclRowStatus = _SnAgAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 21),
    _SnAgAclRowStatus_Type()
)
snAgAclRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclRowStatus.setStatus("current")
_SnAgAclFlowCounter_Type = Counter64
_SnAgAclFlowCounter_Object = MibTableColumn
snAgAclFlowCounter = _SnAgAclFlowCounter_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 22),
    _SnAgAclFlowCounter_Type()
)
snAgAclFlowCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgAclFlowCounter.setStatus("current")
_SnAgAclPacketCounter_Type = Counter64
_SnAgAclPacketCounter_Object = MibTableColumn
snAgAclPacketCounter = _SnAgAclPacketCounter_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 23),
    _SnAgAclPacketCounter_Type()
)
snAgAclPacketCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgAclPacketCounter.setStatus("current")
_SnAgAclComments_Type = DisplayString
_SnAgAclComments_Object = MibTableColumn
snAgAclComments = _SnAgAclComments_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 24),
    _SnAgAclComments_Type()
)
snAgAclComments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclComments.setStatus("current")


class _SnAgAclIpPriority_Type(Integer32):
    """Custom type snAgAclIpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_SnAgAclIpPriority_Type.__name__ = "Integer32"
_SnAgAclIpPriority_Object = MibTableColumn
snAgAclIpPriority = _SnAgAclIpPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 25),
    _SnAgAclIpPriority_Type()
)
snAgAclIpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclIpPriority.setStatus("current")


class _SnAgAclPriorityForce_Type(Integer32):
    """Custom type snAgAclPriorityForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_SnAgAclPriorityForce_Type.__name__ = "Integer32"
_SnAgAclPriorityForce_Object = MibTableColumn
snAgAclPriorityForce = _SnAgAclPriorityForce_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 26),
    _SnAgAclPriorityForce_Type()
)
snAgAclPriorityForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclPriorityForce.setStatus("current")


class _SnAgAclPriorityMapping_Type(Integer32):
    """Custom type snAgAclPriorityMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SnAgAclPriorityMapping_Type.__name__ = "Integer32"
_SnAgAclPriorityMapping_Object = MibTableColumn
snAgAclPriorityMapping = _SnAgAclPriorityMapping_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 27),
    _SnAgAclPriorityMapping_Type()
)
snAgAclPriorityMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclPriorityMapping.setStatus("current")


class _SnAgAclDscpMarking_Type(Integer32):
    """Custom type snAgAclDscpMarking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_SnAgAclDscpMarking_Type.__name__ = "Integer32"
_SnAgAclDscpMarking_Object = MibTableColumn
snAgAclDscpMarking = _SnAgAclDscpMarking_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 28),
    _SnAgAclDscpMarking_Type()
)
snAgAclDscpMarking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclDscpMarking.setStatus("current")


class _SnAgAclDscpMapping_Type(Integer32):
    """Custom type snAgAclDscpMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_SnAgAclDscpMapping_Type.__name__ = "Integer32"
_SnAgAclDscpMapping_Object = MibTableColumn
snAgAclDscpMapping = _SnAgAclDscpMapping_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 29),
    _SnAgAclDscpMapping_Type()
)
snAgAclDscpMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclDscpMapping.setStatus("current")


class _SnAgAclIcmpCode_Type(Integer32):
    """Custom type snAgAclIcmpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnAgAclIcmpCode_Type.__name__ = "Integer32"
_SnAgAclIcmpCode_Object = MibTableColumn
snAgAclIcmpCode = _SnAgAclIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 30),
    _SnAgAclIcmpCode_Type()
)
snAgAclIcmpCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclIcmpCode.setStatus("current")


class _SnAgAclParameters_Type(Bits):
    """Custom type snAgAclParameters based on Bits"""
    namedValues = NamedValues(
        *(("dscpMappingFlagSet", 6),
          ("dscpMarkingFlagSet", 7),
          ("matchFragmentedPackets", 0),
          ("matchNonFragmentedPackets", 1),
          ("matchTcpSynSetPackets", 2),
          ("mirrorPermitPackets", 4),
          ("permitFailedRPFCheckPackets", 3),
          ("sendPermitPacketsToSflowCollector", 5))
    )

_SnAgAclParameters_Type.__name__ = "Bits"
_SnAgAclParameters_Object = MibTableColumn
snAgAclParameters = _SnAgAclParameters_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 31),
    _SnAgAclParameters_Type()
)
snAgAclParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclParameters.setStatus("current")


class _SnAgAclVlanId_Type(FdryVlanIdOrNoneTC):
    """Custom type snAgAclVlanId based on FdryVlanIdOrNoneTC"""
    defaultValue = 0


_SnAgAclVlanId_Object = MibTableColumn
snAgAclVlanId = _SnAgAclVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 32),
    _SnAgAclVlanId_Type()
)
snAgAclVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snAgAclVlanId.setStatus("current")
_SnAgAclClauseString_Type = DisplayString
_SnAgAclClauseString_Object = MibTableColumn
snAgAclClauseString = _SnAgAclClauseString_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 2, 1, 33),
    _SnAgAclClauseString_Type()
)
snAgAclClauseString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgAclClauseString.setStatus("current")
_SnAgAclBindToPortTable_Object = MibTable
snAgAclBindToPortTable = _SnAgAclBindToPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 3)
)
if mibBuilder.loadTexts:
    snAgAclBindToPortTable.setStatus("current")
_SnAgAclBindToPortEntry_Object = MibTableRow
snAgAclBindToPortEntry = _SnAgAclBindToPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 3, 1)
)
snAgAclBindToPortEntry.setIndexNames(
    (0, "FOUNDRY-SN-IP-ACL-MIB", "snAgAclPortNum"),
    (0, "FOUNDRY-SN-IP-ACL-MIB", "snAgAclPortBindDirection"),
)
if mibBuilder.loadTexts:
    snAgAclBindToPortEntry.setStatus("current")
_SnAgAclPortNum_Type = Integer32
_SnAgAclPortNum_Object = MibTableColumn
snAgAclPortNum = _SnAgAclPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 3, 1, 1),
    _SnAgAclPortNum_Type()
)
snAgAclPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgAclPortNum.setStatus("current")
_SnAgAclPortBindDirection_Type = Direction
_SnAgAclPortBindDirection_Object = MibTableColumn
snAgAclPortBindDirection = _SnAgAclPortBindDirection_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 3, 1, 2),
    _SnAgAclPortBindDirection_Type()
)
snAgAclPortBindDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgAclPortBindDirection.setStatus("current")
_SnAgAclNum_Type = Integer32
_SnAgAclNum_Object = MibTableColumn
snAgAclNum = _SnAgAclNum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 3, 1, 3),
    _SnAgAclNum_Type()
)
snAgAclNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclNum.setStatus("current")
_SnAgAclNameString_Type = DisplayString
_SnAgAclNameString_Object = MibTableColumn
snAgAclNameString = _SnAgAclNameString_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 3, 1, 4),
    _SnAgAclNameString_Type()
)
snAgAclNameString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclNameString.setStatus("current")
_SnAgBindPortListInVirtualInterface_Type = OctetString
_SnAgBindPortListInVirtualInterface_Object = MibTableColumn
snAgBindPortListInVirtualInterface = _SnAgBindPortListInVirtualInterface_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 3, 1, 5),
    _SnAgBindPortListInVirtualInterface_Type()
)
snAgBindPortListInVirtualInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgBindPortListInVirtualInterface.setStatus("current")
_SnAgAclPortRowStatus_Type = SnRowStatus
_SnAgAclPortRowStatus_Object = MibTableColumn
snAgAclPortRowStatus = _SnAgAclPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 3, 1, 6),
    _SnAgAclPortRowStatus_Type()
)
snAgAclPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgAclPortRowStatus.setStatus("current")
_SnAgAclIfBindTable_Object = MibTable
snAgAclIfBindTable = _SnAgAclIfBindTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 4)
)
if mibBuilder.loadTexts:
    snAgAclIfBindTable.setStatus("current")
_SnAgAclIfBindEntry_Object = MibTableRow
snAgAclIfBindEntry = _SnAgAclIfBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 4, 1)
)
snAgAclIfBindEntry.setIndexNames(
    (0, "FOUNDRY-SN-IP-ACL-MIB", "snAgAclIfBindIndex"),
    (0, "FOUNDRY-SN-IP-ACL-MIB", "snAgAclIfBindDirection"),
)
if mibBuilder.loadTexts:
    snAgAclIfBindEntry.setStatus("current")
_SnAgAclIfBindIndex_Type = InterfaceIndex
_SnAgAclIfBindIndex_Object = MibTableColumn
snAgAclIfBindIndex = _SnAgAclIfBindIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 4, 1, 1),
    _SnAgAclIfBindIndex_Type()
)
snAgAclIfBindIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgAclIfBindIndex.setStatus("current")
_SnAgAclIfBindDirection_Type = Direction
_SnAgAclIfBindDirection_Object = MibTableColumn
snAgAclIfBindDirection = _SnAgAclIfBindDirection_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 4, 1, 2),
    _SnAgAclIfBindDirection_Type()
)
snAgAclIfBindDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgAclIfBindDirection.setStatus("current")


class _SnAgAclIfBindNum_Type(Integer32):
    """Custom type snAgAclIfBindNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_SnAgAclIfBindNum_Type.__name__ = "Integer32"
_SnAgAclIfBindNum_Object = MibTableColumn
snAgAclIfBindNum = _SnAgAclIfBindNum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 4, 1, 3),
    _SnAgAclIfBindNum_Type()
)
snAgAclIfBindNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snAgAclIfBindNum.setStatus("current")


class _SnAgAclIfBindName_Type(DisplayString):
    """Custom type snAgAclIfBindName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnAgAclIfBindName_Type.__name__ = "DisplayString"
_SnAgAclIfBindName_Object = MibTableColumn
snAgAclIfBindName = _SnAgAclIfBindName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 4, 1, 4),
    _SnAgAclIfBindName_Type()
)
snAgAclIfBindName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snAgAclIfBindName.setStatus("current")
_SnAgAclIfBindVifPortList_Type = OctetString
_SnAgAclIfBindVifPortList_Object = MibTableColumn
snAgAclIfBindVifPortList = _SnAgAclIfBindVifPortList_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 4, 1, 5),
    _SnAgAclIfBindVifPortList_Type()
)
snAgAclIfBindVifPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snAgAclIfBindVifPortList.setStatus("current")
_SnAgAclIfBindRowStatus_Type = SnRowStatus
_SnAgAclIfBindRowStatus_Object = MibTableColumn
snAgAclIfBindRowStatus = _SnAgAclIfBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 4, 1, 6),
    _SnAgAclIfBindRowStatus_Type()
)
snAgAclIfBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snAgAclIfBindRowStatus.setStatus("current")


class _SnAgAclIfBindDenyLogging_Type(Integer32):
    """Custom type snAgAclIfBindDenyLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SnAgAclIfBindDenyLogging_Type.__name__ = "Integer32"
_SnAgAclIfBindDenyLogging_Object = MibTableColumn
snAgAclIfBindDenyLogging = _SnAgAclIfBindDenyLogging_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 4, 1, 7),
    _SnAgAclIfBindDenyLogging_Type()
)
snAgAclIfBindDenyLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snAgAclIfBindDenyLogging.setStatus("current")


class _SnAgAclIfIpv6BindName_Type(DisplayString):
    """Custom type snAgAclIfIpv6BindName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_SnAgAclIfIpv6BindName_Type.__name__ = "DisplayString"
_SnAgAclIfIpv6BindName_Object = MibTableColumn
snAgAclIfIpv6BindName = _SnAgAclIfIpv6BindName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 4, 1, 8),
    _SnAgAclIfIpv6BindName_Type()
)
snAgAclIfIpv6BindName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snAgAclIfIpv6BindName.setStatus("current")
_AgAclAccntTable_Object = MibTable
agAclAccntTable = _AgAclAccntTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5)
)
if mibBuilder.loadTexts:
    agAclAccntTable.setStatus("current")
_AgAclAccntEntry_Object = MibTableRow
agAclAccntEntry = _AgAclAccntEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1)
)
agAclAccntEntry.setIndexNames(
    (0, "FOUNDRY-SN-IP-ACL-MIB", "agAclAccntKind"),
    (0, "FOUNDRY-SN-IP-ACL-MIB", "agAclAccntIfIndex"),
    (0, "FOUNDRY-SN-IP-ACL-MIB", "agAclAccntDirection"),
    (0, "FOUNDRY-SN-IP-ACL-MIB", "agAclAccntAclNumber"),
    (0, "FOUNDRY-SN-IP-ACL-MIB", "agAclAccntFilterId"),
)
if mibBuilder.loadTexts:
    agAclAccntEntry.setStatus("current")


class _AgAclAccntKind_Type(Integer32):
    """Custom type agAclAccntKind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 0),
          ("ipv6", 5),
          ("ipv6ReceiveAcl", 7),
          ("l2", 1),
          ("rateLimit", 3),
          ("receiveAcl", 4))
    )


_AgAclAccntKind_Type.__name__ = "Integer32"
_AgAclAccntKind_Object = MibTableColumn
agAclAccntKind = _AgAclAccntKind_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1, 1),
    _AgAclAccntKind_Type()
)
agAclAccntKind.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agAclAccntKind.setStatus("current")
_AgAclAccntIfIndex_Type = InterfaceIndex
_AgAclAccntIfIndex_Object = MibTableColumn
agAclAccntIfIndex = _AgAclAccntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1, 2),
    _AgAclAccntIfIndex_Type()
)
agAclAccntIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agAclAccntIfIndex.setStatus("current")
_AgAclAccntDirection_Type = Direction
_AgAclAccntDirection_Object = MibTableColumn
agAclAccntDirection = _AgAclAccntDirection_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1, 3),
    _AgAclAccntDirection_Type()
)
agAclAccntDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agAclAccntDirection.setStatus("current")
_AgAclAccntAclNumber_Type = AclNumber
_AgAclAccntAclNumber_Object = MibTableColumn
agAclAccntAclNumber = _AgAclAccntAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1, 4),
    _AgAclAccntAclNumber_Type()
)
agAclAccntAclNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agAclAccntAclNumber.setStatus("current")
_AgAclAccntFilterId_Type = Unsigned32
_AgAclAccntFilterId_Object = MibTableColumn
agAclAccntFilterId = _AgAclAccntFilterId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1, 5),
    _AgAclAccntFilterId_Type()
)
agAclAccntFilterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agAclAccntFilterId.setStatus("current")
_AgAclAccntAclName_Type = AclNameString
_AgAclAccntAclName_Object = MibTableColumn
agAclAccntAclName = _AgAclAccntAclName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1, 6),
    _AgAclAccntAclName_Type()
)
agAclAccntAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agAclAccntAclName.setStatus("current")
_AgAclAccntOneSecond_Type = Counter64
_AgAclAccntOneSecond_Object = MibTableColumn
agAclAccntOneSecond = _AgAclAccntOneSecond_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1, 7),
    _AgAclAccntOneSecond_Type()
)
agAclAccntOneSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agAclAccntOneSecond.setStatus("current")
_AgAclAccntOneMinute_Type = Counter64
_AgAclAccntOneMinute_Object = MibTableColumn
agAclAccntOneMinute = _AgAclAccntOneMinute_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1, 8),
    _AgAclAccntOneMinute_Type()
)
agAclAccntOneMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agAclAccntOneMinute.setStatus("current")
_AgAclAccntFiveMinute_Type = Counter64
_AgAclAccntFiveMinute_Object = MibTableColumn
agAclAccntFiveMinute = _AgAclAccntFiveMinute_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1, 9),
    _AgAclAccntFiveMinute_Type()
)
agAclAccntFiveMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agAclAccntFiveMinute.setStatus("current")
_AgAclAccntCumulative_Type = Counter64
_AgAclAccntCumulative_Object = MibTableColumn
agAclAccntCumulative = _AgAclAccntCumulative_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1, 10),
    _AgAclAccntCumulative_Type()
)
agAclAccntCumulative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agAclAccntCumulative.setStatus("current")
_AgAclAccntRaclDropCnt_Type = Counter64
_AgAclAccntRaclDropCnt_Object = MibTableColumn
agAclAccntRaclDropCnt = _AgAclAccntRaclDropCnt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1, 11),
    _AgAclAccntRaclDropCnt_Type()
)
agAclAccntRaclDropCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agAclAccntRaclDropCnt.setStatus("current")
_AgAclAccntRaclFwdCnt_Type = Counter64
_AgAclAccntRaclFwdCnt_Object = MibTableColumn
agAclAccntRaclFwdCnt = _AgAclAccntRaclFwdCnt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1, 12),
    _AgAclAccntRaclFwdCnt_Type()
)
agAclAccntRaclFwdCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agAclAccntRaclFwdCnt.setStatus("current")
_AgAclAccntRaclRemarkCnt_Type = Counter64
_AgAclAccntRaclRemarkCnt_Object = MibTableColumn
agAclAccntRaclRemarkCnt = _AgAclAccntRaclRemarkCnt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1, 13),
    _AgAclAccntRaclRemarkCnt_Type()
)
agAclAccntRaclRemarkCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agAclAccntRaclRemarkCnt.setStatus("current")
_AgAclAccntRaclTotalCnt_Type = Counter64
_AgAclAccntRaclTotalCnt_Object = MibTableColumn
agAclAccntRaclTotalCnt = _AgAclAccntRaclTotalCnt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1, 14),
    _AgAclAccntRaclTotalCnt_Type()
)
agAclAccntRaclTotalCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agAclAccntRaclTotalCnt.setStatus("current")
_AgAclAccntRaclTotalSWHitCountCnt_Type = Counter64
_AgAclAccntRaclTotalSWHitCountCnt_Object = MibTableColumn
agAclAccntRaclTotalSWHitCountCnt = _AgAclAccntRaclTotalSWHitCountCnt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 5, 1, 15),
    _AgAclAccntRaclTotalSWHitCountCnt_Type()
)
agAclAccntRaclTotalSWHitCountCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agAclAccntRaclTotalSWHitCountCnt.setStatus("current")
_FdryL2AclNextClauseTable_Object = MibTable
fdryL2AclNextClauseTable = _FdryL2AclNextClauseTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 6)
)
if mibBuilder.loadTexts:
    fdryL2AclNextClauseTable.setStatus("current")
_FdryL2AclNextClauseEntry_Object = MibTableRow
fdryL2AclNextClauseEntry = _FdryL2AclNextClauseEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 6, 1)
)
fdryL2AclNextClauseEntry.setIndexNames(
    (0, "FOUNDRY-SN-IP-ACL-MIB", "fdryL2AclNumber"),
)
if mibBuilder.loadTexts:
    fdryL2AclNextClauseEntry.setStatus("current")
_FdryL2AclNextClauseIndex_Type = FdryClauseIndexTC
_FdryL2AclNextClauseIndex_Object = MibTableColumn
fdryL2AclNextClauseIndex = _FdryL2AclNextClauseIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 6, 1, 1),
    _FdryL2AclNextClauseIndex_Type()
)
fdryL2AclNextClauseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryL2AclNextClauseIndex.setStatus("current")
_FdryL2AclTable_Object = MibTable
fdryL2AclTable = _FdryL2AclTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7)
)
if mibBuilder.loadTexts:
    fdryL2AclTable.setStatus("current")
_FdryL2AclEntry_Object = MibTableRow
fdryL2AclEntry = _FdryL2AclEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1)
)
fdryL2AclEntry.setIndexNames(
    (0, "FOUNDRY-SN-IP-ACL-MIB", "fdryL2AclNumber"),
    (0, "FOUNDRY-SN-IP-ACL-MIB", "fdryL2AclClauseIndex"),
)
if mibBuilder.loadTexts:
    fdryL2AclEntry.setStatus("current")
_FdryL2AclNumber_Type = AclNumber
_FdryL2AclNumber_Object = MibTableColumn
fdryL2AclNumber = _FdryL2AclNumber_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1, 1),
    _FdryL2AclNumber_Type()
)
fdryL2AclNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryL2AclNumber.setStatus("current")
_FdryL2AclClauseIndex_Type = FdryClauseIndexTC
_FdryL2AclClauseIndex_Object = MibTableColumn
fdryL2AclClauseIndex = _FdryL2AclClauseIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1, 2),
    _FdryL2AclClauseIndex_Type()
)
fdryL2AclClauseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryL2AclClauseIndex.setStatus("current")
_FdryL2AclAction_Type = Action
_FdryL2AclAction_Object = MibTableColumn
fdryL2AclAction = _FdryL2AclAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1, 3),
    _FdryL2AclAction_Type()
)
fdryL2AclAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryL2AclAction.setStatus("current")


class _FdryL2AclSourceMac_Type(MacAddress):
    """Custom type fdryL2AclSourceMac based on MacAddress"""
    defaultHexValue = "000000000000"


_FdryL2AclSourceMac_Object = MibTableColumn
fdryL2AclSourceMac = _FdryL2AclSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1, 4),
    _FdryL2AclSourceMac_Type()
)
fdryL2AclSourceMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryL2AclSourceMac.setStatus("current")


class _FdryL2AclSourceMacMask_Type(MacAddress):
    """Custom type fdryL2AclSourceMacMask based on MacAddress"""
    defaultHexValue = "000000000000"


_FdryL2AclSourceMacMask_Object = MibTableColumn
fdryL2AclSourceMacMask = _FdryL2AclSourceMacMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1, 5),
    _FdryL2AclSourceMacMask_Type()
)
fdryL2AclSourceMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryL2AclSourceMacMask.setStatus("current")


class _FdryL2AclDestinationMac_Type(MacAddress):
    """Custom type fdryL2AclDestinationMac based on MacAddress"""
    defaultHexValue = "000000000000"


_FdryL2AclDestinationMac_Object = MibTableColumn
fdryL2AclDestinationMac = _FdryL2AclDestinationMac_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1, 6),
    _FdryL2AclDestinationMac_Type()
)
fdryL2AclDestinationMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryL2AclDestinationMac.setStatus("current")


class _FdryL2AclDestinationMacMask_Type(MacAddress):
    """Custom type fdryL2AclDestinationMacMask based on MacAddress"""
    defaultHexValue = "000000000000"


_FdryL2AclDestinationMacMask_Object = MibTableColumn
fdryL2AclDestinationMacMask = _FdryL2AclDestinationMacMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1, 7),
    _FdryL2AclDestinationMacMask_Type()
)
fdryL2AclDestinationMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryL2AclDestinationMacMask.setStatus("current")


class _FdryL2AclVlanId_Type(FdryVlanIdOrNoneTC):
    """Custom type fdryL2AclVlanId based on FdryVlanIdOrNoneTC"""
    defaultValue = 0


_FdryL2AclVlanId_Object = MibTableColumn
fdryL2AclVlanId = _FdryL2AclVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1, 8),
    _FdryL2AclVlanId_Type()
)
fdryL2AclVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryL2AclVlanId.setStatus("current")


class _FdryL2AclEthernetType_Type(FdryEnetTypeOrZeroTC):
    """Custom type fdryL2AclEthernetType based on FdryEnetTypeOrZeroTC"""


_FdryL2AclEthernetType_Object = MibTableColumn
fdryL2AclEthernetType = _FdryL2AclEthernetType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1, 9),
    _FdryL2AclEthernetType_Type()
)
fdryL2AclEthernetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryL2AclEthernetType.setStatus("current")


class _FdryL2AclDot1pPriority_Type(PortQosTC):
    """Custom type fdryL2AclDot1pPriority based on PortQosTC"""


_FdryL2AclDot1pPriority_Object = MibTableColumn
fdryL2AclDot1pPriority = _FdryL2AclDot1pPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1, 10),
    _FdryL2AclDot1pPriority_Type()
)
fdryL2AclDot1pPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryL2AclDot1pPriority.setStatus("current")


class _FdryL2AclDot1pPriorityForce_Type(PortQosTC):
    """Custom type fdryL2AclDot1pPriorityForce based on PortQosTC"""


_FdryL2AclDot1pPriorityForce_Object = MibTableColumn
fdryL2AclDot1pPriorityForce = _FdryL2AclDot1pPriorityForce_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1, 11),
    _FdryL2AclDot1pPriorityForce_Type()
)
fdryL2AclDot1pPriorityForce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryL2AclDot1pPriorityForce.setStatus("current")


class _FdryL2AclDot1pPriorityMapping_Type(PortQosTC):
    """Custom type fdryL2AclDot1pPriorityMapping based on PortQosTC"""


_FdryL2AclDot1pPriorityMapping_Object = MibTableColumn
fdryL2AclDot1pPriorityMapping = _FdryL2AclDot1pPriorityMapping_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1, 12),
    _FdryL2AclDot1pPriorityMapping_Type()
)
fdryL2AclDot1pPriorityMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryL2AclDot1pPriorityMapping.setStatus("current")


class _FdryL2AclMirrorPackets_Type(TruthValue):
    """Custom type fdryL2AclMirrorPackets based on TruthValue"""


_FdryL2AclMirrorPackets_Object = MibTableColumn
fdryL2AclMirrorPackets = _FdryL2AclMirrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1, 13),
    _FdryL2AclMirrorPackets_Type()
)
fdryL2AclMirrorPackets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryL2AclMirrorPackets.setStatus("current")


class _FdryL2AclLogEnable_Type(TruthValue):
    """Custom type fdryL2AclLogEnable based on TruthValue"""


_FdryL2AclLogEnable_Object = MibTableColumn
fdryL2AclLogEnable = _FdryL2AclLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1, 14),
    _FdryL2AclLogEnable_Type()
)
fdryL2AclLogEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryL2AclLogEnable.setStatus("current")
_FdryL2AclRowStatus_Type = RowStatus
_FdryL2AclRowStatus_Object = MibTableColumn
fdryL2AclRowStatus = _FdryL2AclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 7, 1, 15),
    _FdryL2AclRowStatus_Type()
)
fdryL2AclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryL2AclRowStatus.setStatus("current")
_FdryL2AclIfBindTable_Object = MibTable
fdryL2AclIfBindTable = _FdryL2AclIfBindTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 8)
)
if mibBuilder.loadTexts:
    fdryL2AclIfBindTable.setStatus("current")
_FdryL2AclIfBindEntry_Object = MibTableRow
fdryL2AclIfBindEntry = _FdryL2AclIfBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 8, 1)
)
fdryL2AclIfBindEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FOUNDRY-SN-IP-ACL-MIB", "fdryL2AclIfBindDirection"),
)
if mibBuilder.loadTexts:
    fdryL2AclIfBindEntry.setStatus("current")
_FdryL2AclIfBindDirection_Type = Direction
_FdryL2AclIfBindDirection_Object = MibTableColumn
fdryL2AclIfBindDirection = _FdryL2AclIfBindDirection_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 8, 1, 1),
    _FdryL2AclIfBindDirection_Type()
)
fdryL2AclIfBindDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryL2AclIfBindDirection.setStatus("current")
_FdryL2AclIfBindAclNumber_Type = Unsigned32
_FdryL2AclIfBindAclNumber_Object = MibTableColumn
fdryL2AclIfBindAclNumber = _FdryL2AclIfBindAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 8, 1, 2),
    _FdryL2AclIfBindAclNumber_Type()
)
fdryL2AclIfBindAclNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryL2AclIfBindAclNumber.setStatus("current")
_FdryL2AclIfBindRowStatus_Type = RowStatus
_FdryL2AclIfBindRowStatus_Object = MibTableColumn
fdryL2AclIfBindRowStatus = _FdryL2AclIfBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 8, 1, 3),
    _FdryL2AclIfBindRowStatus_Type()
)
fdryL2AclIfBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryL2AclIfBindRowStatus.setStatus("current")
_BrcdPbrAclAccntTable_Object = MibTable
brcdPbrAclAccntTable = _BrcdPbrAclAccntTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 9)
)
if mibBuilder.loadTexts:
    brcdPbrAclAccntTable.setStatus("current")
_BrcdPbrAclAccntEntry_Object = MibTableRow
brcdPbrAclAccntEntry = _BrcdPbrAclAccntEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 9, 1)
)
brcdPbrAclAccntEntry.setIndexNames(
    (0, "FOUNDRY-SN-IP-ACL-MIB", "brcdPbrAclAccntKind"),
    (0, "FOUNDRY-SN-IP-ACL-MIB", "brcdPbrAclAccntIfIndex"),
    (0, "FOUNDRY-SN-IP-ACL-MIB", "brcdPbrSerialNumber"),
)
if mibBuilder.loadTexts:
    brcdPbrAclAccntEntry.setStatus("current")


class _BrcdPbrAclAccntKind_Type(Integer32):
    """Custom type brcdPbrAclAccntKind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4PolicyBasedRouting", 1),
          ("ipv6PolicyBasedRouting", 2))
    )


_BrcdPbrAclAccntKind_Type.__name__ = "Integer32"
_BrcdPbrAclAccntKind_Object = MibTableColumn
brcdPbrAclAccntKind = _BrcdPbrAclAccntKind_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 9, 1, 1),
    _BrcdPbrAclAccntKind_Type()
)
brcdPbrAclAccntKind.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdPbrAclAccntKind.setStatus("current")
_BrcdPbrAclAccntIfIndex_Type = InterfaceIndex
_BrcdPbrAclAccntIfIndex_Object = MibTableColumn
brcdPbrAclAccntIfIndex = _BrcdPbrAclAccntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 9, 1, 2),
    _BrcdPbrAclAccntIfIndex_Type()
)
brcdPbrAclAccntIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdPbrAclAccntIfIndex.setStatus("current")


class _BrcdPbrSerialNumber_Type(Integer32):
    """Custom type brcdPbrSerialNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BrcdPbrSerialNumber_Type.__name__ = "Integer32"
_BrcdPbrSerialNumber_Object = MibTableColumn
brcdPbrSerialNumber = _BrcdPbrSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 9, 1, 3),
    _BrcdPbrSerialNumber_Type()
)
brcdPbrSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdPbrSerialNumber.setStatus("current")
_BrcdPbrAclAccntAclInfo_Type = DisplayString
_BrcdPbrAclAccntAclInfo_Object = MibTableColumn
brcdPbrAclAccntAclInfo = _BrcdPbrAclAccntAclInfo_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 15, 9, 1, 4),
    _BrcdPbrAclAccntAclInfo_Type()
)
brcdPbrAclAccntAclInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdPbrAclAccntAclInfo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-SN-IP-ACL-MIB",
    **{"SnRowStatus": SnRowStatus,
       "Action": Action,
       "TruthVal": TruthVal,
       "FdryClauseIndexTC": FdryClauseIndexTC,
       "AclNumber": AclNumber,
       "AclNameString": AclNameString,
       "Operator": Operator,
       "IpProtocol": IpProtocol,
       "PrecedenceValue": PrecedenceValue,
       "TosValue": TosValue,
       "Direction": Direction,
       "FdryEnetTypeOrZeroTC": FdryEnetTypeOrZeroTC,
       "snAgAcl": snAgAcl,
       "snAgAclGlobal": snAgAclGlobal,
       "snAgAclGblCurRowIndex": snAgAclGblCurRowIndex,
       "snAgAclGblAcctEnable": snAgAclGblAcctEnable,
       "snAgAclGblIfIPv4AcctClear": snAgAclGblIfIPv4AcctClear,
       "snAgAclGblIfIPv6AcctClear": snAgAclGblIfIPv6AcctClear,
       "snAgAclGblRebindAclNumber": snAgAclGblRebindAclNumber,
       "snAgAclGblRebindAclName": snAgAclGblRebindAclName,
       "brcdPbrAclAccntFilterAclName": brcdPbrAclAccntFilterAclName,
       "brcdPbrAclAccntCounterType": brcdPbrAclAccntCounterType,
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
       "snAgAclIcmpCode": snAgAclIcmpCode,
       "snAgAclParameters": snAgAclParameters,
       "snAgAclVlanId": snAgAclVlanId,
       "snAgAclClauseString": snAgAclClauseString,
       "snAgAclBindToPortTable": snAgAclBindToPortTable,
       "snAgAclBindToPortEntry": snAgAclBindToPortEntry,
       "snAgAclPortNum": snAgAclPortNum,
       "snAgAclPortBindDirection": snAgAclPortBindDirection,
       "snAgAclNum": snAgAclNum,
       "snAgAclNameString": snAgAclNameString,
       "snAgBindPortListInVirtualInterface": snAgBindPortListInVirtualInterface,
       "snAgAclPortRowStatus": snAgAclPortRowStatus,
       "snAgAclIfBindTable": snAgAclIfBindTable,
       "snAgAclIfBindEntry": snAgAclIfBindEntry,
       "snAgAclIfBindIndex": snAgAclIfBindIndex,
       "snAgAclIfBindDirection": snAgAclIfBindDirection,
       "snAgAclIfBindNum": snAgAclIfBindNum,
       "snAgAclIfBindName": snAgAclIfBindName,
       "snAgAclIfBindVifPortList": snAgAclIfBindVifPortList,
       "snAgAclIfBindRowStatus": snAgAclIfBindRowStatus,
       "snAgAclIfBindDenyLogging": snAgAclIfBindDenyLogging,
       "snAgAclIfIpv6BindName": snAgAclIfIpv6BindName,
       "agAclAccntTable": agAclAccntTable,
       "agAclAccntEntry": agAclAccntEntry,
       "agAclAccntKind": agAclAccntKind,
       "agAclAccntIfIndex": agAclAccntIfIndex,
       "agAclAccntDirection": agAclAccntDirection,
       "agAclAccntAclNumber": agAclAccntAclNumber,
       "agAclAccntFilterId": agAclAccntFilterId,
       "agAclAccntAclName": agAclAccntAclName,
       "agAclAccntOneSecond": agAclAccntOneSecond,
       "agAclAccntOneMinute": agAclAccntOneMinute,
       "agAclAccntFiveMinute": agAclAccntFiveMinute,
       "agAclAccntCumulative": agAclAccntCumulative,
       "agAclAccntRaclDropCnt": agAclAccntRaclDropCnt,
       "agAclAccntRaclFwdCnt": agAclAccntRaclFwdCnt,
       "agAclAccntRaclRemarkCnt": agAclAccntRaclRemarkCnt,
       "agAclAccntRaclTotalCnt": agAclAccntRaclTotalCnt,
       "agAclAccntRaclTotalSWHitCountCnt": agAclAccntRaclTotalSWHitCountCnt,
       "fdryL2AclNextClauseTable": fdryL2AclNextClauseTable,
       "fdryL2AclNextClauseEntry": fdryL2AclNextClauseEntry,
       "fdryL2AclNextClauseIndex": fdryL2AclNextClauseIndex,
       "fdryL2AclTable": fdryL2AclTable,
       "fdryL2AclEntry": fdryL2AclEntry,
       "fdryL2AclNumber": fdryL2AclNumber,
       "fdryL2AclClauseIndex": fdryL2AclClauseIndex,
       "fdryL2AclAction": fdryL2AclAction,
       "fdryL2AclSourceMac": fdryL2AclSourceMac,
       "fdryL2AclSourceMacMask": fdryL2AclSourceMacMask,
       "fdryL2AclDestinationMac": fdryL2AclDestinationMac,
       "fdryL2AclDestinationMacMask": fdryL2AclDestinationMacMask,
       "fdryL2AclVlanId": fdryL2AclVlanId,
       "fdryL2AclEthernetType": fdryL2AclEthernetType,
       "fdryL2AclDot1pPriority": fdryL2AclDot1pPriority,
       "fdryL2AclDot1pPriorityForce": fdryL2AclDot1pPriorityForce,
       "fdryL2AclDot1pPriorityMapping": fdryL2AclDot1pPriorityMapping,
       "fdryL2AclMirrorPackets": fdryL2AclMirrorPackets,
       "fdryL2AclLogEnable": fdryL2AclLogEnable,
       "fdryL2AclRowStatus": fdryL2AclRowStatus,
       "fdryL2AclIfBindTable": fdryL2AclIfBindTable,
       "fdryL2AclIfBindEntry": fdryL2AclIfBindEntry,
       "fdryL2AclIfBindDirection": fdryL2AclIfBindDirection,
       "fdryL2AclIfBindAclNumber": fdryL2AclIfBindAclNumber,
       "fdryL2AclIfBindRowStatus": fdryL2AclIfBindRowStatus,
       "brcdPbrAclAccntTable": brcdPbrAclAccntTable,
       "brcdPbrAclAccntEntry": brcdPbrAclAccntEntry,
       "brcdPbrAclAccntKind": brcdPbrAclAccntKind,
       "brcdPbrAclAccntIfIndex": brcdPbrAclAccntIfIndex,
       "brcdPbrSerialNumber": brcdPbrSerialNumber,
       "brcdPbrAclAccntAclInfo": brcdPbrAclAccntAclInfo}
)
