# SNMP MIB module (ARISTA-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ARISTA-ACL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:15 2024
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

(aristaMibs,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaMibs")

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

(TimeFilter,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "TimeFilter")

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
 MacAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

aristaAclMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5)
)
aristaAclMIB.setRevisions(
        ("2014-08-15 00:00",
         "2013-02-08 11:00",
         "2012-06-20 13:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AristaAclRuleAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 0),
          ("remark", 2))
    )



class AristaAclRangeOperator(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("eq", 1),
          ("gt", 2),
          ("lt", 3),
          ("neq", 4),
          ("range", 5))
    )



# MIB Managed Objects in the order of their OIDs

_AristaAcl_ObjectIdentity = ObjectIdentity
aristaAcl = _AristaAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1)
)
_AristaIpAcl_ObjectIdentity = ObjectIdentity
aristaIpAcl = _AristaIpAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1)
)
_AristaIpAclTable_Object = MibTable
aristaIpAclTable = _AristaIpAclTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    aristaIpAclTable.setStatus("current")
_AristaIpAclEntry_Object = MibTableRow
aristaIpAclEntry = _AristaIpAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 1, 1)
)
aristaIpAclEntry.setIndexNames(
    (0, "ARISTA-ACL-MIB", "aristaIpAclName"),
)
if mibBuilder.loadTexts:
    aristaIpAclEntry.setStatus("current")


class _AristaIpAclName_Type(DisplayString):
    """Custom type aristaIpAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AristaIpAclName_Type.__name__ = "DisplayString"
_AristaIpAclName_Object = MibTableColumn
aristaIpAclName = _AristaIpAclName_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 1, 1, 1),
    _AristaIpAclName_Type()
)
aristaIpAclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaIpAclName.setStatus("current")
_AristaIpAclReadOnly_Type = TruthValue
_AristaIpAclReadOnly_Object = MibTableColumn
aristaIpAclReadOnly = _AristaIpAclReadOnly_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 1, 1, 2),
    _AristaIpAclReadOnly_Type()
)
aristaIpAclReadOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpAclReadOnly.setStatus("current")
_AristaIpAclStatsEnabled_Type = TruthValue
_AristaIpAclStatsEnabled_Object = MibTableColumn
aristaIpAclStatsEnabled = _AristaIpAclStatsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 1, 1, 3),
    _AristaIpAclStatsEnabled_Type()
)
aristaIpAclStatsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpAclStatsEnabled.setStatus("current")
_AristaIpAclCountersIncomplete_Type = TruthValue
_AristaIpAclCountersIncomplete_Object = MibTableColumn
aristaIpAclCountersIncomplete = _AristaIpAclCountersIncomplete_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 1, 1, 4),
    _AristaIpAclCountersIncomplete_Type()
)
aristaIpAclCountersIncomplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpAclCountersIncomplete.setStatus("current")
_AristaIpAclRuleTable_Object = MibTable
aristaIpAclRuleTable = _AristaIpAclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    aristaIpAclRuleTable.setStatus("current")
_AristaIpAclRuleEntry_Object = MibTableRow
aristaIpAclRuleEntry = _AristaIpAclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 2, 1)
)
aristaIpAclRuleEntry.setIndexNames(
    (0, "ARISTA-ACL-MIB", "aristaIpAclName"),
    (0, "ARISTA-ACL-MIB", "aristaIpAclRuleSeqId"),
)
if mibBuilder.loadTexts:
    aristaIpAclRuleEntry.setStatus("current")
_AristaIpAclRuleSeqId_Type = Unsigned32
_AristaIpAclRuleSeqId_Object = MibTableColumn
aristaIpAclRuleSeqId = _AristaIpAclRuleSeqId_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 2, 1, 1),
    _AristaIpAclRuleSeqId_Type()
)
aristaIpAclRuleSeqId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaIpAclRuleSeqId.setStatus("current")


class _AristaIpAclRuleProto_Type(Unsigned32):
    """Custom type aristaIpAclRuleProto based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AristaIpAclRuleProto_Type.__name__ = "Unsigned32"
_AristaIpAclRuleProto_Object = MibTableColumn
aristaIpAclRuleProto = _AristaIpAclRuleProto_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 2, 1, 2),
    _AristaIpAclRuleProto_Type()
)
aristaIpAclRuleProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpAclRuleProto.setStatus("current")
_AristaIpAclRuleSrc_Type = IpAddress
_AristaIpAclRuleSrc_Object = MibTableColumn
aristaIpAclRuleSrc = _AristaIpAclRuleSrc_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 2, 1, 3),
    _AristaIpAclRuleSrc_Type()
)
aristaIpAclRuleSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpAclRuleSrc.setStatus("current")
_AristaIpAclRuleSrcMask_Type = IpAddress
_AristaIpAclRuleSrcMask_Object = MibTableColumn
aristaIpAclRuleSrcMask = _AristaIpAclRuleSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 2, 1, 4),
    _AristaIpAclRuleSrcMask_Type()
)
aristaIpAclRuleSrcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpAclRuleSrcMask.setStatus("current")
_AristaIpAclRuleDest_Type = IpAddress
_AristaIpAclRuleDest_Object = MibTableColumn
aristaIpAclRuleDest = _AristaIpAclRuleDest_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 2, 1, 5),
    _AristaIpAclRuleDest_Type()
)
aristaIpAclRuleDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpAclRuleDest.setStatus("current")
_AristaIpAclRuleDestMask_Type = IpAddress
_AristaIpAclRuleDestMask_Object = MibTableColumn
aristaIpAclRuleDestMask = _AristaIpAclRuleDestMask_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 2, 1, 6),
    _AristaIpAclRuleDestMask_Type()
)
aristaIpAclRuleDestMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpAclRuleDestMask.setStatus("current")
_AristaIpAclRuleL4PortSrcOper_Type = AristaAclRangeOperator
_AristaIpAclRuleL4PortSrcOper_Object = MibTableColumn
aristaIpAclRuleL4PortSrcOper = _AristaIpAclRuleL4PortSrcOper_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 2, 1, 7),
    _AristaIpAclRuleL4PortSrcOper_Type()
)
aristaIpAclRuleL4PortSrcOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpAclRuleL4PortSrcOper.setStatus("current")


class _AristaIpAclRuleL4PortsSrc_Type(OctetString):
    """Custom type aristaIpAclRuleL4PortsSrc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_AristaIpAclRuleL4PortsSrc_Type.__name__ = "OctetString"
_AristaIpAclRuleL4PortsSrc_Object = MibTableColumn
aristaIpAclRuleL4PortsSrc = _AristaIpAclRuleL4PortsSrc_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 2, 1, 8),
    _AristaIpAclRuleL4PortsSrc_Type()
)
aristaIpAclRuleL4PortsSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpAclRuleL4PortsSrc.setStatus("current")
_AristaIpAclRuleL4PortDestOper_Type = AristaAclRangeOperator
_AristaIpAclRuleL4PortDestOper_Object = MibTableColumn
aristaIpAclRuleL4PortDestOper = _AristaIpAclRuleL4PortDestOper_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 2, 1, 9),
    _AristaIpAclRuleL4PortDestOper_Type()
)
aristaIpAclRuleL4PortDestOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpAclRuleL4PortDestOper.setStatus("current")


class _AristaIpAclRuleL4PortsDest_Type(OctetString):
    """Custom type aristaIpAclRuleL4PortsDest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_AristaIpAclRuleL4PortsDest_Type.__name__ = "OctetString"
_AristaIpAclRuleL4PortsDest_Object = MibTableColumn
aristaIpAclRuleL4PortsDest = _AristaIpAclRuleL4PortsDest_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 2, 1, 10),
    _AristaIpAclRuleL4PortsDest_Type()
)
aristaIpAclRuleL4PortsDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpAclRuleL4PortsDest.setStatus("current")
_AristaIpAclRuleTtlOper_Type = AristaAclRangeOperator
_AristaIpAclRuleTtlOper_Object = MibTableColumn
aristaIpAclRuleTtlOper = _AristaIpAclRuleTtlOper_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 2, 1, 11),
    _AristaIpAclRuleTtlOper_Type()
)
aristaIpAclRuleTtlOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpAclRuleTtlOper.setStatus("current")


class _AristaIpAclRuleTtl_Type(Unsigned32):
    """Custom type aristaIpAclRuleTtl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AristaIpAclRuleTtl_Type.__name__ = "Unsigned32"
_AristaIpAclRuleTtl_Object = MibTableColumn
aristaIpAclRuleTtl = _AristaIpAclRuleTtl_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 2, 1, 12),
    _AristaIpAclRuleTtl_Type()
)
aristaIpAclRuleTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpAclRuleTtl.setStatus("current")
_AristaIpAclRuleTracked_Type = TruthValue
_AristaIpAclRuleTracked_Object = MibTableColumn
aristaIpAclRuleTracked = _AristaIpAclRuleTracked_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 2, 1, 13),
    _AristaIpAclRuleTracked_Type()
)
aristaIpAclRuleTracked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpAclRuleTracked.setStatus("current")
_AristaIpAclRuleFragments_Type = TruthValue
_AristaIpAclRuleFragments_Object = MibTableColumn
aristaIpAclRuleFragments = _AristaIpAclRuleFragments_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 2, 1, 14),
    _AristaIpAclRuleFragments_Type()
)
aristaIpAclRuleFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpAclRuleFragments.setStatus("current")


class _AristaIpAclRuleTcpFlags_Type(Bits):
    """Custom type aristaIpAclRuleTcpFlags based on Bits"""
    namedValues = NamedValues(
        *(("ack", 4),
          ("fin", 0),
          ("psh", 3),
          ("rst", 2),
          ("syn", 1),
          ("urg", 5))
    )

_AristaIpAclRuleTcpFlags_Type.__name__ = "Bits"
_AristaIpAclRuleTcpFlags_Object = MibTableColumn
aristaIpAclRuleTcpFlags = _AristaIpAclRuleTcpFlags_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 2, 1, 15),
    _AristaIpAclRuleTcpFlags_Type()
)
aristaIpAclRuleTcpFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpAclRuleTcpFlags.setStatus("current")
_AristaIpAclRuleEstablished_Type = TruthValue
_AristaIpAclRuleEstablished_Object = MibTableColumn
aristaIpAclRuleEstablished = _AristaIpAclRuleEstablished_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 2, 1, 16),
    _AristaIpAclRuleEstablished_Type()
)
aristaIpAclRuleEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpAclRuleEstablished.setStatus("current")


class _AristaIpAclRuleIcmpType_Type(Unsigned32):
    """Custom type aristaIpAclRuleIcmpType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AristaIpAclRuleIcmpType_Type.__name__ = "Unsigned32"
_AristaIpAclRuleIcmpType_Object = MibTableColumn
aristaIpAclRuleIcmpType = _AristaIpAclRuleIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 2, 1, 17),
    _AristaIpAclRuleIcmpType_Type()
)
aristaIpAclRuleIcmpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpAclRuleIcmpType.setStatus("current")


class _AristaIpAclRuleIcmpCode_Type(Unsigned32):
    """Custom type aristaIpAclRuleIcmpCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AristaIpAclRuleIcmpCode_Type.__name__ = "Unsigned32"
_AristaIpAclRuleIcmpCode_Object = MibTableColumn
aristaIpAclRuleIcmpCode = _AristaIpAclRuleIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 2, 1, 18),
    _AristaIpAclRuleIcmpCode_Type()
)
aristaIpAclRuleIcmpCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpAclRuleIcmpCode.setStatus("current")
_AristaIpAclRuleAction_Type = AristaAclRuleAction
_AristaIpAclRuleAction_Object = MibTableColumn
aristaIpAclRuleAction = _AristaIpAclRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 2, 1, 19),
    _AristaIpAclRuleAction_Type()
)
aristaIpAclRuleAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpAclRuleAction.setStatus("current")
_AristaIpAclRuleLog_Type = TruthValue
_AristaIpAclRuleLog_Object = MibTableColumn
aristaIpAclRuleLog = _AristaIpAclRuleLog_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 2, 1, 20),
    _AristaIpAclRuleLog_Type()
)
aristaIpAclRuleLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpAclRuleLog.setStatus("current")


class _AristaIpAclRuleRemark_Type(DisplayString):
    """Custom type aristaIpAclRuleRemark based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AristaIpAclRuleRemark_Type.__name__ = "DisplayString"
_AristaIpAclRuleRemark_Object = MibTableColumn
aristaIpAclRuleRemark = _AristaIpAclRuleRemark_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 2, 1, 21),
    _AristaIpAclRuleRemark_Type()
)
aristaIpAclRuleRemark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpAclRuleRemark.setStatus("current")
_AristaIpAclRuleStatsTable_Object = MibTable
aristaIpAclRuleStatsTable = _AristaIpAclRuleStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 3)
)
if mibBuilder.loadTexts:
    aristaIpAclRuleStatsTable.setStatus("current")
_AristaIpAclRuleStatsEntry_Object = MibTableRow
aristaIpAclRuleStatsEntry = _AristaIpAclRuleStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 3, 1)
)
aristaIpAclRuleStatsEntry.setIndexNames(
    (0, "ARISTA-ACL-MIB", "aristaIpAclRuleTimeMark"),
    (0, "ARISTA-ACL-MIB", "aristaIpAclName"),
    (0, "ARISTA-ACL-MIB", "aristaIpAclRuleSeqId"),
)
if mibBuilder.loadTexts:
    aristaIpAclRuleStatsEntry.setStatus("current")
_AristaIpAclRuleTimeMark_Type = TimeFilter
_AristaIpAclRuleTimeMark_Object = MibTableColumn
aristaIpAclRuleTimeMark = _AristaIpAclRuleTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 3, 1, 1),
    _AristaIpAclRuleTimeMark_Type()
)
aristaIpAclRuleTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaIpAclRuleTimeMark.setStatus("current")
_AristaIpAclRuleStatsPktCount_Type = Counter64
_AristaIpAclRuleStatsPktCount_Object = MibTableColumn
aristaIpAclRuleStatsPktCount = _AristaIpAclRuleStatsPktCount_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 3, 1, 2),
    _AristaIpAclRuleStatsPktCount_Type()
)
aristaIpAclRuleStatsPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpAclRuleStatsPktCount.setStatus("current")
_AristaIpAclRuleStatsLastUpdateTime_Type = TimeStamp
_AristaIpAclRuleStatsLastUpdateTime_Object = MibTableColumn
aristaIpAclRuleStatsLastUpdateTime = _AristaIpAclRuleStatsLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 1, 3, 1, 3),
    _AristaIpAclRuleStatsLastUpdateTime_Type()
)
aristaIpAclRuleStatsLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpAclRuleStatsLastUpdateTime.setStatus("current")
_AristaMacAcl_ObjectIdentity = ObjectIdentity
aristaMacAcl = _AristaMacAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 2)
)
_AristaMacAclTable_Object = MibTable
aristaMacAclTable = _AristaMacAclTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    aristaMacAclTable.setStatus("current")
_AristaMacAclEntry_Object = MibTableRow
aristaMacAclEntry = _AristaMacAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 2, 1, 1)
)
aristaMacAclEntry.setIndexNames(
    (0, "ARISTA-ACL-MIB", "aristaMacAclName"),
)
if mibBuilder.loadTexts:
    aristaMacAclEntry.setStatus("current")


class _AristaMacAclName_Type(DisplayString):
    """Custom type aristaMacAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AristaMacAclName_Type.__name__ = "DisplayString"
_AristaMacAclName_Object = MibTableColumn
aristaMacAclName = _AristaMacAclName_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 2, 1, 1, 1),
    _AristaMacAclName_Type()
)
aristaMacAclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaMacAclName.setStatus("current")
_AristaMacAclReadOnly_Type = TruthValue
_AristaMacAclReadOnly_Object = MibTableColumn
aristaMacAclReadOnly = _AristaMacAclReadOnly_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 2, 1, 1, 2),
    _AristaMacAclReadOnly_Type()
)
aristaMacAclReadOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaMacAclReadOnly.setStatus("current")
_AristaMacAclStatsEnabled_Type = TruthValue
_AristaMacAclStatsEnabled_Object = MibTableColumn
aristaMacAclStatsEnabled = _AristaMacAclStatsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 2, 1, 1, 3),
    _AristaMacAclStatsEnabled_Type()
)
aristaMacAclStatsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaMacAclStatsEnabled.setStatus("current")
_AristaMacAclCountersIncomplete_Type = TruthValue
_AristaMacAclCountersIncomplete_Object = MibTableColumn
aristaMacAclCountersIncomplete = _AristaMacAclCountersIncomplete_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 2, 1, 1, 4),
    _AristaMacAclCountersIncomplete_Type()
)
aristaMacAclCountersIncomplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaMacAclCountersIncomplete.setStatus("current")
_AristaMacAclRuleTable_Object = MibTable
aristaMacAclRuleTable = _AristaMacAclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 2, 2)
)
if mibBuilder.loadTexts:
    aristaMacAclRuleTable.setStatus("current")
_AristaMacAclRuleEntry_Object = MibTableRow
aristaMacAclRuleEntry = _AristaMacAclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 2, 2, 1)
)
aristaMacAclRuleEntry.setIndexNames(
    (0, "ARISTA-ACL-MIB", "aristaMacAclName"),
    (0, "ARISTA-ACL-MIB", "aristaMacAclRuleSeqId"),
)
if mibBuilder.loadTexts:
    aristaMacAclRuleEntry.setStatus("current")
_AristaMacAclRuleSeqId_Type = Unsigned32
_AristaMacAclRuleSeqId_Object = MibTableColumn
aristaMacAclRuleSeqId = _AristaMacAclRuleSeqId_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 2, 2, 1, 1),
    _AristaMacAclRuleSeqId_Type()
)
aristaMacAclRuleSeqId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaMacAclRuleSeqId.setStatus("current")
_AristaMacAclRuleSrc_Type = MacAddress
_AristaMacAclRuleSrc_Object = MibTableColumn
aristaMacAclRuleSrc = _AristaMacAclRuleSrc_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 2, 2, 1, 2),
    _AristaMacAclRuleSrc_Type()
)
aristaMacAclRuleSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaMacAclRuleSrc.setStatus("current")
_AristaMacAclRuleSrcMask_Type = MacAddress
_AristaMacAclRuleSrcMask_Object = MibTableColumn
aristaMacAclRuleSrcMask = _AristaMacAclRuleSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 2, 2, 1, 3),
    _AristaMacAclRuleSrcMask_Type()
)
aristaMacAclRuleSrcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaMacAclRuleSrcMask.setStatus("current")
_AristaMacAclRuleDest_Type = MacAddress
_AristaMacAclRuleDest_Object = MibTableColumn
aristaMacAclRuleDest = _AristaMacAclRuleDest_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 2, 2, 1, 4),
    _AristaMacAclRuleDest_Type()
)
aristaMacAclRuleDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaMacAclRuleDest.setStatus("current")
_AristaMacAclRuleDestMask_Type = MacAddress
_AristaMacAclRuleDestMask_Object = MibTableColumn
aristaMacAclRuleDestMask = _AristaMacAclRuleDestMask_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 2, 2, 1, 5),
    _AristaMacAclRuleDestMask_Type()
)
aristaMacAclRuleDestMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaMacAclRuleDestMask.setStatus("current")
_AristaMacAclRuleProto_Type = Unsigned32
_AristaMacAclRuleProto_Object = MibTableColumn
aristaMacAclRuleProto = _AristaMacAclRuleProto_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 2, 2, 1, 6),
    _AristaMacAclRuleProto_Type()
)
aristaMacAclRuleProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaMacAclRuleProto.setStatus("current")
_AristaMacAclRuleAction_Type = AristaAclRuleAction
_AristaMacAclRuleAction_Object = MibTableColumn
aristaMacAclRuleAction = _AristaMacAclRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 2, 2, 1, 7),
    _AristaMacAclRuleAction_Type()
)
aristaMacAclRuleAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaMacAclRuleAction.setStatus("current")
_AristaMacAclRuleLog_Type = TruthValue
_AristaMacAclRuleLog_Object = MibTableColumn
aristaMacAclRuleLog = _AristaMacAclRuleLog_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 2, 2, 1, 8),
    _AristaMacAclRuleLog_Type()
)
aristaMacAclRuleLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaMacAclRuleLog.setStatus("current")


class _AristaMacAclRuleRemark_Type(DisplayString):
    """Custom type aristaMacAclRuleRemark based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AristaMacAclRuleRemark_Type.__name__ = "DisplayString"
_AristaMacAclRuleRemark_Object = MibTableColumn
aristaMacAclRuleRemark = _AristaMacAclRuleRemark_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 2, 2, 1, 9),
    _AristaMacAclRuleRemark_Type()
)
aristaMacAclRuleRemark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaMacAclRuleRemark.setStatus("current")
_AristaMacAclRuleStatsTable_Object = MibTable
aristaMacAclRuleStatsTable = _AristaMacAclRuleStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 2, 3)
)
if mibBuilder.loadTexts:
    aristaMacAclRuleStatsTable.setStatus("current")
_AristaMacAclRuleStatsEntry_Object = MibTableRow
aristaMacAclRuleStatsEntry = _AristaMacAclRuleStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 2, 3, 1)
)
aristaMacAclRuleStatsEntry.setIndexNames(
    (0, "ARISTA-ACL-MIB", "aristaMacAclRuleTimeMark"),
    (0, "ARISTA-ACL-MIB", "aristaMacAclName"),
    (0, "ARISTA-ACL-MIB", "aristaMacAclRuleSeqId"),
)
if mibBuilder.loadTexts:
    aristaMacAclRuleStatsEntry.setStatus("current")
_AristaMacAclRuleTimeMark_Type = TimeFilter
_AristaMacAclRuleTimeMark_Object = MibTableColumn
aristaMacAclRuleTimeMark = _AristaMacAclRuleTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 2, 3, 1, 1),
    _AristaMacAclRuleTimeMark_Type()
)
aristaMacAclRuleTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaMacAclRuleTimeMark.setStatus("current")
_AristaMacAclRuleStatsPktCount_Type = Counter64
_AristaMacAclRuleStatsPktCount_Object = MibTableColumn
aristaMacAclRuleStatsPktCount = _AristaMacAclRuleStatsPktCount_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 2, 3, 1, 2),
    _AristaMacAclRuleStatsPktCount_Type()
)
aristaMacAclRuleStatsPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaMacAclRuleStatsPktCount.setStatus("current")
_AristaMacAclRuleStatsLastUpdateTime_Type = TimeStamp
_AristaMacAclRuleStatsLastUpdateTime_Object = MibTableColumn
aristaMacAclRuleStatsLastUpdateTime = _AristaMacAclRuleStatsLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 2, 3, 1, 3),
    _AristaMacAclRuleStatsLastUpdateTime_Type()
)
aristaMacAclRuleStatsLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaMacAclRuleStatsLastUpdateTime.setStatus("current")
_AristaIpv6Acl_ObjectIdentity = ObjectIdentity
aristaIpv6Acl = _AristaIpv6Acl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3)
)
_AristaIpv6AclTable_Object = MibTable
aristaIpv6AclTable = _AristaIpv6AclTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    aristaIpv6AclTable.setStatus("current")
_AristaIpv6AclEntry_Object = MibTableRow
aristaIpv6AclEntry = _AristaIpv6AclEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 1, 1)
)
aristaIpv6AclEntry.setIndexNames(
    (0, "ARISTA-ACL-MIB", "aristaIpv6AclName"),
)
if mibBuilder.loadTexts:
    aristaIpv6AclEntry.setStatus("current")


class _AristaIpv6AclName_Type(DisplayString):
    """Custom type aristaIpv6AclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AristaIpv6AclName_Type.__name__ = "DisplayString"
_AristaIpv6AclName_Object = MibTableColumn
aristaIpv6AclName = _AristaIpv6AclName_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 1, 1, 1),
    _AristaIpv6AclName_Type()
)
aristaIpv6AclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaIpv6AclName.setStatus("current")
_AristaIpv6AclReadOnly_Type = TruthValue
_AristaIpv6AclReadOnly_Object = MibTableColumn
aristaIpv6AclReadOnly = _AristaIpv6AclReadOnly_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 1, 1, 2),
    _AristaIpv6AclReadOnly_Type()
)
aristaIpv6AclReadOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpv6AclReadOnly.setStatus("current")
_AristaIpv6AclStatsEnabled_Type = TruthValue
_AristaIpv6AclStatsEnabled_Object = MibTableColumn
aristaIpv6AclStatsEnabled = _AristaIpv6AclStatsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 1, 1, 3),
    _AristaIpv6AclStatsEnabled_Type()
)
aristaIpv6AclStatsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpv6AclStatsEnabled.setStatus("current")
_AristaIpv6AclCountersIncomplete_Type = TruthValue
_AristaIpv6AclCountersIncomplete_Object = MibTableColumn
aristaIpv6AclCountersIncomplete = _AristaIpv6AclCountersIncomplete_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 1, 1, 4),
    _AristaIpv6AclCountersIncomplete_Type()
)
aristaIpv6AclCountersIncomplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpv6AclCountersIncomplete.setStatus("current")
_AristaIpv6AclRuleTable_Object = MibTable
aristaIpv6AclRuleTable = _AristaIpv6AclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 2)
)
if mibBuilder.loadTexts:
    aristaIpv6AclRuleTable.setStatus("current")
_AristaIpv6AclRuleEntry_Object = MibTableRow
aristaIpv6AclRuleEntry = _AristaIpv6AclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 2, 1)
)
aristaIpv6AclRuleEntry.setIndexNames(
    (0, "ARISTA-ACL-MIB", "aristaIpv6AclName"),
    (0, "ARISTA-ACL-MIB", "aristaIpv6AclRuleSeqId"),
)
if mibBuilder.loadTexts:
    aristaIpv6AclRuleEntry.setStatus("current")
_AristaIpv6AclRuleSeqId_Type = Unsigned32
_AristaIpv6AclRuleSeqId_Object = MibTableColumn
aristaIpv6AclRuleSeqId = _AristaIpv6AclRuleSeqId_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 2, 1, 1),
    _AristaIpv6AclRuleSeqId_Type()
)
aristaIpv6AclRuleSeqId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaIpv6AclRuleSeqId.setStatus("current")


class _AristaIpv6AclRuleProto_Type(Unsigned32):
    """Custom type aristaIpv6AclRuleProto based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AristaIpv6AclRuleProto_Type.__name__ = "Unsigned32"
_AristaIpv6AclRuleProto_Object = MibTableColumn
aristaIpv6AclRuleProto = _AristaIpv6AclRuleProto_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 2, 1, 2),
    _AristaIpv6AclRuleProto_Type()
)
aristaIpv6AclRuleProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpv6AclRuleProto.setStatus("current")
_AristaIpv6AclRuleSrc_Type = InetAddressIPv6
_AristaIpv6AclRuleSrc_Object = MibTableColumn
aristaIpv6AclRuleSrc = _AristaIpv6AclRuleSrc_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 2, 1, 3),
    _AristaIpv6AclRuleSrc_Type()
)
aristaIpv6AclRuleSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpv6AclRuleSrc.setStatus("current")
_AristaIpv6AclRuleSrcMask_Type = InetAddressIPv6
_AristaIpv6AclRuleSrcMask_Object = MibTableColumn
aristaIpv6AclRuleSrcMask = _AristaIpv6AclRuleSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 2, 1, 4),
    _AristaIpv6AclRuleSrcMask_Type()
)
aristaIpv6AclRuleSrcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpv6AclRuleSrcMask.setStatus("current")
_AristaIpv6AclRuleDest_Type = InetAddressIPv6
_AristaIpv6AclRuleDest_Object = MibTableColumn
aristaIpv6AclRuleDest = _AristaIpv6AclRuleDest_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 2, 1, 5),
    _AristaIpv6AclRuleDest_Type()
)
aristaIpv6AclRuleDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpv6AclRuleDest.setStatus("current")
_AristaIpv6AclRuleDestMask_Type = InetAddressIPv6
_AristaIpv6AclRuleDestMask_Object = MibTableColumn
aristaIpv6AclRuleDestMask = _AristaIpv6AclRuleDestMask_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 2, 1, 6),
    _AristaIpv6AclRuleDestMask_Type()
)
aristaIpv6AclRuleDestMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpv6AclRuleDestMask.setStatus("current")
_AristaIpv6AclRuleL4PortSrcOper_Type = AristaAclRangeOperator
_AristaIpv6AclRuleL4PortSrcOper_Object = MibTableColumn
aristaIpv6AclRuleL4PortSrcOper = _AristaIpv6AclRuleL4PortSrcOper_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 2, 1, 7),
    _AristaIpv6AclRuleL4PortSrcOper_Type()
)
aristaIpv6AclRuleL4PortSrcOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpv6AclRuleL4PortSrcOper.setStatus("current")


class _AristaIpv6AclRuleL4PortsSrc_Type(OctetString):
    """Custom type aristaIpv6AclRuleL4PortsSrc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_AristaIpv6AclRuleL4PortsSrc_Type.__name__ = "OctetString"
_AristaIpv6AclRuleL4PortsSrc_Object = MibTableColumn
aristaIpv6AclRuleL4PortsSrc = _AristaIpv6AclRuleL4PortsSrc_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 2, 1, 8),
    _AristaIpv6AclRuleL4PortsSrc_Type()
)
aristaIpv6AclRuleL4PortsSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpv6AclRuleL4PortsSrc.setStatus("current")
_AristaIpv6AclRuleL4PortDestOper_Type = AristaAclRangeOperator
_AristaIpv6AclRuleL4PortDestOper_Object = MibTableColumn
aristaIpv6AclRuleL4PortDestOper = _AristaIpv6AclRuleL4PortDestOper_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 2, 1, 9),
    _AristaIpv6AclRuleL4PortDestOper_Type()
)
aristaIpv6AclRuleL4PortDestOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpv6AclRuleL4PortDestOper.setStatus("current")


class _AristaIpv6AclRuleL4PortsDest_Type(OctetString):
    """Custom type aristaIpv6AclRuleL4PortsDest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_AristaIpv6AclRuleL4PortsDest_Type.__name__ = "OctetString"
_AristaIpv6AclRuleL4PortsDest_Object = MibTableColumn
aristaIpv6AclRuleL4PortsDest = _AristaIpv6AclRuleL4PortsDest_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 2, 1, 10),
    _AristaIpv6AclRuleL4PortsDest_Type()
)
aristaIpv6AclRuleL4PortsDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpv6AclRuleL4PortsDest.setStatus("current")
_AristaIpv6AclRuleHopLimitOper_Type = AristaAclRangeOperator
_AristaIpv6AclRuleHopLimitOper_Object = MibTableColumn
aristaIpv6AclRuleHopLimitOper = _AristaIpv6AclRuleHopLimitOper_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 2, 1, 11),
    _AristaIpv6AclRuleHopLimitOper_Type()
)
aristaIpv6AclRuleHopLimitOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpv6AclRuleHopLimitOper.setStatus("current")


class _AristaIpv6AclRuleHopLimit_Type(Unsigned32):
    """Custom type aristaIpv6AclRuleHopLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AristaIpv6AclRuleHopLimit_Type.__name__ = "Unsigned32"
_AristaIpv6AclRuleHopLimit_Object = MibTableColumn
aristaIpv6AclRuleHopLimit = _AristaIpv6AclRuleHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 2, 1, 12),
    _AristaIpv6AclRuleHopLimit_Type()
)
aristaIpv6AclRuleHopLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpv6AclRuleHopLimit.setStatus("current")


class _AristaIpv6AclRuleTcpFlags_Type(Bits):
    """Custom type aristaIpv6AclRuleTcpFlags based on Bits"""
    namedValues = NamedValues(
        *(("ack", 4),
          ("fin", 0),
          ("psh", 3),
          ("rst", 2),
          ("syn", 1),
          ("urg", 5))
    )

_AristaIpv6AclRuleTcpFlags_Type.__name__ = "Bits"
_AristaIpv6AclRuleTcpFlags_Object = MibTableColumn
aristaIpv6AclRuleTcpFlags = _AristaIpv6AclRuleTcpFlags_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 2, 1, 13),
    _AristaIpv6AclRuleTcpFlags_Type()
)
aristaIpv6AclRuleTcpFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpv6AclRuleTcpFlags.setStatus("current")
_AristaIpv6AclRuleEstablished_Type = TruthValue
_AristaIpv6AclRuleEstablished_Object = MibTableColumn
aristaIpv6AclRuleEstablished = _AristaIpv6AclRuleEstablished_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 2, 1, 14),
    _AristaIpv6AclRuleEstablished_Type()
)
aristaIpv6AclRuleEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpv6AclRuleEstablished.setStatus("current")


class _AristaIpv6AclRuleIcmpType_Type(Unsigned32):
    """Custom type aristaIpv6AclRuleIcmpType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AristaIpv6AclRuleIcmpType_Type.__name__ = "Unsigned32"
_AristaIpv6AclRuleIcmpType_Object = MibTableColumn
aristaIpv6AclRuleIcmpType = _AristaIpv6AclRuleIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 2, 1, 15),
    _AristaIpv6AclRuleIcmpType_Type()
)
aristaIpv6AclRuleIcmpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpv6AclRuleIcmpType.setStatus("current")


class _AristaIpv6AclRuleIcmpCode_Type(Unsigned32):
    """Custom type aristaIpv6AclRuleIcmpCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AristaIpv6AclRuleIcmpCode_Type.__name__ = "Unsigned32"
_AristaIpv6AclRuleIcmpCode_Object = MibTableColumn
aristaIpv6AclRuleIcmpCode = _AristaIpv6AclRuleIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 2, 1, 16),
    _AristaIpv6AclRuleIcmpCode_Type()
)
aristaIpv6AclRuleIcmpCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpv6AclRuleIcmpCode.setStatus("current")
_AristaIpv6AclRuleAction_Type = AristaAclRuleAction
_AristaIpv6AclRuleAction_Object = MibTableColumn
aristaIpv6AclRuleAction = _AristaIpv6AclRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 2, 1, 17),
    _AristaIpv6AclRuleAction_Type()
)
aristaIpv6AclRuleAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpv6AclRuleAction.setStatus("current")
_AristaIpv6AclRuleLog_Type = TruthValue
_AristaIpv6AclRuleLog_Object = MibTableColumn
aristaIpv6AclRuleLog = _AristaIpv6AclRuleLog_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 2, 1, 18),
    _AristaIpv6AclRuleLog_Type()
)
aristaIpv6AclRuleLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpv6AclRuleLog.setStatus("current")


class _AristaIpv6AclRuleRemark_Type(DisplayString):
    """Custom type aristaIpv6AclRuleRemark based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AristaIpv6AclRuleRemark_Type.__name__ = "DisplayString"
_AristaIpv6AclRuleRemark_Object = MibTableColumn
aristaIpv6AclRuleRemark = _AristaIpv6AclRuleRemark_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 2, 1, 19),
    _AristaIpv6AclRuleRemark_Type()
)
aristaIpv6AclRuleRemark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpv6AclRuleRemark.setStatus("current")
_AristaIpv6AclRuleStatsTable_Object = MibTable
aristaIpv6AclRuleStatsTable = _AristaIpv6AclRuleStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 3)
)
if mibBuilder.loadTexts:
    aristaIpv6AclRuleStatsTable.setStatus("current")
_AristaIpv6AclRuleStatsEntry_Object = MibTableRow
aristaIpv6AclRuleStatsEntry = _AristaIpv6AclRuleStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 3, 1)
)
aristaIpv6AclRuleStatsEntry.setIndexNames(
    (0, "ARISTA-ACL-MIB", "aristaIpv6AclRuleTimeMark"),
    (0, "ARISTA-ACL-MIB", "aristaIpv6AclName"),
    (0, "ARISTA-ACL-MIB", "aristaIpv6AclRuleSeqId"),
)
if mibBuilder.loadTexts:
    aristaIpv6AclRuleStatsEntry.setStatus("current")
_AristaIpv6AclRuleTimeMark_Type = TimeFilter
_AristaIpv6AclRuleTimeMark_Object = MibTableColumn
aristaIpv6AclRuleTimeMark = _AristaIpv6AclRuleTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 3, 1, 1),
    _AristaIpv6AclRuleTimeMark_Type()
)
aristaIpv6AclRuleTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaIpv6AclRuleTimeMark.setStatus("current")
_AristaIpv6AclRuleStatsPktCount_Type = Counter64
_AristaIpv6AclRuleStatsPktCount_Object = MibTableColumn
aristaIpv6AclRuleStatsPktCount = _AristaIpv6AclRuleStatsPktCount_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 3, 1, 2),
    _AristaIpv6AclRuleStatsPktCount_Type()
)
aristaIpv6AclRuleStatsPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpv6AclRuleStatsPktCount.setStatus("current")
_AristaIpv6AclRuleStatsLastUpdateTime_Type = TimeStamp
_AristaIpv6AclRuleStatsLastUpdateTime_Object = MibTableColumn
aristaIpv6AclRuleStatsLastUpdateTime = _AristaIpv6AclRuleStatsLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 3, 3, 1, 3),
    _AristaIpv6AclRuleStatsLastUpdateTime_Type()
)
aristaIpv6AclRuleStatsLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpv6AclRuleStatsLastUpdateTime.setStatus("current")


class _AristaAclDpSupportFlags_Type(Bits):
    """Custom type aristaAclDpSupportFlags based on Bits"""
    namedValues = NamedValues(
        *(("acl", 0),
          ("counter", 2),
          ("logging", 1),
          ("routerAcl", 3))
    )

_AristaAclDpSupportFlags_Type.__name__ = "Bits"
_AristaAclDpSupportFlags_Object = MibScalar
aristaAclDpSupportFlags = _AristaAclDpSupportFlags_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 1, 4),
    _AristaAclDpSupportFlags_Type()
)
aristaAclDpSupportFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaAclDpSupportFlags.setStatus("current")
_AristaAclConformance_ObjectIdentity = ObjectIdentity
aristaAclConformance = _AristaAclConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 2)
)
_AristaAclCompliances_ObjectIdentity = ObjectIdentity
aristaAclCompliances = _AristaAclCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 2, 1)
)
_AristaAclGroups_ObjectIdentity = ObjectIdentity
aristaAclGroups = _AristaAclGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 2, 2)
)

# Managed Objects groups

aristaAclGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 2, 2, 1)
)
aristaAclGroup.setObjects(
      *(("ARISTA-ACL-MIB", "aristaAclDpSupportFlags"),
        ("ARISTA-ACL-MIB", "aristaIpAclReadOnly"),
        ("ARISTA-ACL-MIB", "aristaIpAclStatsEnabled"),
        ("ARISTA-ACL-MIB", "aristaIpAclCountersIncomplete"),
        ("ARISTA-ACL-MIB", "aristaIpAclRuleProto"),
        ("ARISTA-ACL-MIB", "aristaIpAclRuleSrc"),
        ("ARISTA-ACL-MIB", "aristaIpAclRuleSrcMask"),
        ("ARISTA-ACL-MIB", "aristaIpAclRuleDest"),
        ("ARISTA-ACL-MIB", "aristaIpAclRuleDestMask"),
        ("ARISTA-ACL-MIB", "aristaIpAclRuleL4PortSrcOper"),
        ("ARISTA-ACL-MIB", "aristaIpAclRuleL4PortsSrc"),
        ("ARISTA-ACL-MIB", "aristaIpAclRuleL4PortDestOper"),
        ("ARISTA-ACL-MIB", "aristaIpAclRuleL4PortsDest"),
        ("ARISTA-ACL-MIB", "aristaIpAclRuleTtlOper"),
        ("ARISTA-ACL-MIB", "aristaIpAclRuleTtl"),
        ("ARISTA-ACL-MIB", "aristaIpAclRuleTracked"),
        ("ARISTA-ACL-MIB", "aristaIpAclRuleFragments"),
        ("ARISTA-ACL-MIB", "aristaIpAclRuleTcpFlags"),
        ("ARISTA-ACL-MIB", "aristaIpAclRuleEstablished"),
        ("ARISTA-ACL-MIB", "aristaIpAclRuleIcmpType"),
        ("ARISTA-ACL-MIB", "aristaIpAclRuleIcmpCode"),
        ("ARISTA-ACL-MIB", "aristaIpAclRuleAction"),
        ("ARISTA-ACL-MIB", "aristaIpAclRuleLog"),
        ("ARISTA-ACL-MIB", "aristaIpAclRuleRemark"),
        ("ARISTA-ACL-MIB", "aristaIpAclRuleStatsPktCount"),
        ("ARISTA-ACL-MIB", "aristaIpAclRuleStatsLastUpdateTime"),
        ("ARISTA-ACL-MIB", "aristaMacAclReadOnly"),
        ("ARISTA-ACL-MIB", "aristaMacAclStatsEnabled"),
        ("ARISTA-ACL-MIB", "aristaMacAclCountersIncomplete"),
        ("ARISTA-ACL-MIB", "aristaMacAclRuleSrc"),
        ("ARISTA-ACL-MIB", "aristaMacAclRuleSrcMask"),
        ("ARISTA-ACL-MIB", "aristaMacAclRuleDest"),
        ("ARISTA-ACL-MIB", "aristaMacAclRuleDestMask"),
        ("ARISTA-ACL-MIB", "aristaMacAclRuleProto"),
        ("ARISTA-ACL-MIB", "aristaMacAclRuleAction"),
        ("ARISTA-ACL-MIB", "aristaMacAclRuleLog"),
        ("ARISTA-ACL-MIB", "aristaMacAclRuleRemark"),
        ("ARISTA-ACL-MIB", "aristaMacAclRuleStatsPktCount"),
        ("ARISTA-ACL-MIB", "aristaMacAclRuleStatsLastUpdateTime"),
        ("ARISTA-ACL-MIB", "aristaIpv6AclReadOnly"),
        ("ARISTA-ACL-MIB", "aristaIpv6AclStatsEnabled"),
        ("ARISTA-ACL-MIB", "aristaIpv6AclCountersIncomplete"),
        ("ARISTA-ACL-MIB", "aristaIpv6AclRuleProto"),
        ("ARISTA-ACL-MIB", "aristaIpv6AclRuleSrc"),
        ("ARISTA-ACL-MIB", "aristaIpv6AclRuleSrcMask"),
        ("ARISTA-ACL-MIB", "aristaIpv6AclRuleDest"),
        ("ARISTA-ACL-MIB", "aristaIpv6AclRuleDestMask"),
        ("ARISTA-ACL-MIB", "aristaIpv6AclRuleL4PortSrcOper"),
        ("ARISTA-ACL-MIB", "aristaIpv6AclRuleL4PortsSrc"),
        ("ARISTA-ACL-MIB", "aristaIpv6AclRuleL4PortDestOper"),
        ("ARISTA-ACL-MIB", "aristaIpv6AclRuleL4PortsDest"),
        ("ARISTA-ACL-MIB", "aristaIpv6AclRuleHopLimitOper"),
        ("ARISTA-ACL-MIB", "aristaIpv6AclRuleHopLimit"),
        ("ARISTA-ACL-MIB", "aristaIpv6AclRuleTcpFlags"),
        ("ARISTA-ACL-MIB", "aristaIpv6AclRuleEstablished"),
        ("ARISTA-ACL-MIB", "aristaIpv6AclRuleIcmpType"),
        ("ARISTA-ACL-MIB", "aristaIpv6AclRuleIcmpCode"),
        ("ARISTA-ACL-MIB", "aristaIpv6AclRuleAction"),
        ("ARISTA-ACL-MIB", "aristaIpv6AclRuleLog"),
        ("ARISTA-ACL-MIB", "aristaIpv6AclRuleRemark"),
        ("ARISTA-ACL-MIB", "aristaIpv6AclRuleStatsPktCount"),
        ("ARISTA-ACL-MIB", "aristaIpv6AclRuleStatsLastUpdateTime"))
)
if mibBuilder.loadTexts:
    aristaAclGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aristaAclCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    aristaAclCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-ACL-MIB",
    **{"AristaAclRuleAction": AristaAclRuleAction,
       "AristaAclRangeOperator": AristaAclRangeOperator,
       "aristaAclMIB": aristaAclMIB,
       "aristaAcl": aristaAcl,
       "aristaIpAcl": aristaIpAcl,
       "aristaIpAclTable": aristaIpAclTable,
       "aristaIpAclEntry": aristaIpAclEntry,
       "aristaIpAclName": aristaIpAclName,
       "aristaIpAclReadOnly": aristaIpAclReadOnly,
       "aristaIpAclStatsEnabled": aristaIpAclStatsEnabled,
       "aristaIpAclCountersIncomplete": aristaIpAclCountersIncomplete,
       "aristaIpAclRuleTable": aristaIpAclRuleTable,
       "aristaIpAclRuleEntry": aristaIpAclRuleEntry,
       "aristaIpAclRuleSeqId": aristaIpAclRuleSeqId,
       "aristaIpAclRuleProto": aristaIpAclRuleProto,
       "aristaIpAclRuleSrc": aristaIpAclRuleSrc,
       "aristaIpAclRuleSrcMask": aristaIpAclRuleSrcMask,
       "aristaIpAclRuleDest": aristaIpAclRuleDest,
       "aristaIpAclRuleDestMask": aristaIpAclRuleDestMask,
       "aristaIpAclRuleL4PortSrcOper": aristaIpAclRuleL4PortSrcOper,
       "aristaIpAclRuleL4PortsSrc": aristaIpAclRuleL4PortsSrc,
       "aristaIpAclRuleL4PortDestOper": aristaIpAclRuleL4PortDestOper,
       "aristaIpAclRuleL4PortsDest": aristaIpAclRuleL4PortsDest,
       "aristaIpAclRuleTtlOper": aristaIpAclRuleTtlOper,
       "aristaIpAclRuleTtl": aristaIpAclRuleTtl,
       "aristaIpAclRuleTracked": aristaIpAclRuleTracked,
       "aristaIpAclRuleFragments": aristaIpAclRuleFragments,
       "aristaIpAclRuleTcpFlags": aristaIpAclRuleTcpFlags,
       "aristaIpAclRuleEstablished": aristaIpAclRuleEstablished,
       "aristaIpAclRuleIcmpType": aristaIpAclRuleIcmpType,
       "aristaIpAclRuleIcmpCode": aristaIpAclRuleIcmpCode,
       "aristaIpAclRuleAction": aristaIpAclRuleAction,
       "aristaIpAclRuleLog": aristaIpAclRuleLog,
       "aristaIpAclRuleRemark": aristaIpAclRuleRemark,
       "aristaIpAclRuleStatsTable": aristaIpAclRuleStatsTable,
       "aristaIpAclRuleStatsEntry": aristaIpAclRuleStatsEntry,
       "aristaIpAclRuleTimeMark": aristaIpAclRuleTimeMark,
       "aristaIpAclRuleStatsPktCount": aristaIpAclRuleStatsPktCount,
       "aristaIpAclRuleStatsLastUpdateTime": aristaIpAclRuleStatsLastUpdateTime,
       "aristaMacAcl": aristaMacAcl,
       "aristaMacAclTable": aristaMacAclTable,
       "aristaMacAclEntry": aristaMacAclEntry,
       "aristaMacAclName": aristaMacAclName,
       "aristaMacAclReadOnly": aristaMacAclReadOnly,
       "aristaMacAclStatsEnabled": aristaMacAclStatsEnabled,
       "aristaMacAclCountersIncomplete": aristaMacAclCountersIncomplete,
       "aristaMacAclRuleTable": aristaMacAclRuleTable,
       "aristaMacAclRuleEntry": aristaMacAclRuleEntry,
       "aristaMacAclRuleSeqId": aristaMacAclRuleSeqId,
       "aristaMacAclRuleSrc": aristaMacAclRuleSrc,
       "aristaMacAclRuleSrcMask": aristaMacAclRuleSrcMask,
       "aristaMacAclRuleDest": aristaMacAclRuleDest,
       "aristaMacAclRuleDestMask": aristaMacAclRuleDestMask,
       "aristaMacAclRuleProto": aristaMacAclRuleProto,
       "aristaMacAclRuleAction": aristaMacAclRuleAction,
       "aristaMacAclRuleLog": aristaMacAclRuleLog,
       "aristaMacAclRuleRemark": aristaMacAclRuleRemark,
       "aristaMacAclRuleStatsTable": aristaMacAclRuleStatsTable,
       "aristaMacAclRuleStatsEntry": aristaMacAclRuleStatsEntry,
       "aristaMacAclRuleTimeMark": aristaMacAclRuleTimeMark,
       "aristaMacAclRuleStatsPktCount": aristaMacAclRuleStatsPktCount,
       "aristaMacAclRuleStatsLastUpdateTime": aristaMacAclRuleStatsLastUpdateTime,
       "aristaIpv6Acl": aristaIpv6Acl,
       "aristaIpv6AclTable": aristaIpv6AclTable,
       "aristaIpv6AclEntry": aristaIpv6AclEntry,
       "aristaIpv6AclName": aristaIpv6AclName,
       "aristaIpv6AclReadOnly": aristaIpv6AclReadOnly,
       "aristaIpv6AclStatsEnabled": aristaIpv6AclStatsEnabled,
       "aristaIpv6AclCountersIncomplete": aristaIpv6AclCountersIncomplete,
       "aristaIpv6AclRuleTable": aristaIpv6AclRuleTable,
       "aristaIpv6AclRuleEntry": aristaIpv6AclRuleEntry,
       "aristaIpv6AclRuleSeqId": aristaIpv6AclRuleSeqId,
       "aristaIpv6AclRuleProto": aristaIpv6AclRuleProto,
       "aristaIpv6AclRuleSrc": aristaIpv6AclRuleSrc,
       "aristaIpv6AclRuleSrcMask": aristaIpv6AclRuleSrcMask,
       "aristaIpv6AclRuleDest": aristaIpv6AclRuleDest,
       "aristaIpv6AclRuleDestMask": aristaIpv6AclRuleDestMask,
       "aristaIpv6AclRuleL4PortSrcOper": aristaIpv6AclRuleL4PortSrcOper,
       "aristaIpv6AclRuleL4PortsSrc": aristaIpv6AclRuleL4PortsSrc,
       "aristaIpv6AclRuleL4PortDestOper": aristaIpv6AclRuleL4PortDestOper,
       "aristaIpv6AclRuleL4PortsDest": aristaIpv6AclRuleL4PortsDest,
       "aristaIpv6AclRuleHopLimitOper": aristaIpv6AclRuleHopLimitOper,
       "aristaIpv6AclRuleHopLimit": aristaIpv6AclRuleHopLimit,
       "aristaIpv6AclRuleTcpFlags": aristaIpv6AclRuleTcpFlags,
       "aristaIpv6AclRuleEstablished": aristaIpv6AclRuleEstablished,
       "aristaIpv6AclRuleIcmpType": aristaIpv6AclRuleIcmpType,
       "aristaIpv6AclRuleIcmpCode": aristaIpv6AclRuleIcmpCode,
       "aristaIpv6AclRuleAction": aristaIpv6AclRuleAction,
       "aristaIpv6AclRuleLog": aristaIpv6AclRuleLog,
       "aristaIpv6AclRuleRemark": aristaIpv6AclRuleRemark,
       "aristaIpv6AclRuleStatsTable": aristaIpv6AclRuleStatsTable,
       "aristaIpv6AclRuleStatsEntry": aristaIpv6AclRuleStatsEntry,
       "aristaIpv6AclRuleTimeMark": aristaIpv6AclRuleTimeMark,
       "aristaIpv6AclRuleStatsPktCount": aristaIpv6AclRuleStatsPktCount,
       "aristaIpv6AclRuleStatsLastUpdateTime": aristaIpv6AclRuleStatsLastUpdateTime,
       "aristaAclDpSupportFlags": aristaAclDpSupportFlags,
       "aristaAclConformance": aristaAclConformance,
       "aristaAclCompliances": aristaAclCompliances,
       "aristaAclCompliance": aristaAclCompliance,
       "aristaAclGroups": aristaAclGroups,
       "aristaAclGroup": aristaAclGroup}
)
