# SNMP MIB module (CADANT-CMTS-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-CMTS-POLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:48 2024
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

(cadPolicy,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadPolicy")

(CadAclString,
 CadAclType,
 CadExtAclCondition,
 CadIfDirection,
 CadIpTos,
 CadIpTosMask,
 CadProtocolType,
 CadTcpFlags,
 InetAddressIPv4or6) = mibBuilder.importSymbols(
    "CADANT-TC",
    "CadAclString",
    "CadAclType",
    "CadExtAclCondition",
    "CadIfDirection",
    "CadIpTos",
    "CadIpTosMask",
    "CadProtocolType",
    "CadTcpFlags",
    "InetAddressIPv4or6")

(InfoSourceDest,) = mibBuilder.importSymbols(
    "DC-RTM-MIB",
    "InfoSourceDest")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cadPolicyMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1)
)
cadPolicyMib.setRevisions(
        ("2014-03-26 00:00",
         "2014-03-06 00:00",
         "2013-05-03 00:00",
         "2013-04-16 00:00",
         "2011-12-02 00:00",
         "2011-11-08 00:00",
         "2010-08-26 00:00",
         "2010-08-11 00:00",
         "2010-07-02 00:00",
         "2010-06-02 00:00",
         "2009-09-14 00:00",
         "2008-03-31 00:00",
         "2008-03-17 00:00",
         "2007-04-30 00:00",
         "2006-08-24 00:00",
         "2005-09-09 00:00",
         "2005-08-31 00:00",
         "2005-06-20 00:00",
         "2005-06-10 00:00",
         "2005-06-06 00:00",
         "2005-04-14 00:00",
         "2005-03-14 00:00",
         "2004-11-29 00:00",
         "2004-11-18 00:00",
         "2004-10-26 00:00",
         "2004-09-14 00:00",
         "2002-07-09 00:00",
         "2002-05-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CadPolicyRateLimitAction(Integer32, TextualConvention):
    status = "current"
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
        *(("drop", 2),
          ("set-dscp-transmit", 4),
          ("set-prec-transmit", 3),
          ("set-priority-transmit", 5),
          ("transmit", 1))
    )



class CadPolicyAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )



class CadPolicyProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
        *(("bbnSpfIgp", 12),
          ("bgp", 14),
          ("ciscoEigrp", 16),
          ("ciscoIgrp", 11),
          ("egp", 5),
          ("esIs", 10),
          ("ggp", 6),
          ("hello", 7),
          ("icmp", 4),
          ("idpr", 15),
          ("isIs", 9),
          ("local", 2),
          ("netmgmt", 3),
          ("ospf", 13),
          ("other", 1),
          ("rip", 8))
    )



# MIB Managed Objects in the order of their OIDs

_CadScmAccessTable_Object = MibTable
cadScmAccessTable = _CadScmAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 1)
)
if mibBuilder.loadTexts:
    cadScmAccessTable.setStatus("current")
_CadScmAccessEntry_Object = MibTableRow
cadScmAccessEntry = _CadScmAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 1, 1)
)
cadScmAccessEntry.setIndexNames(
    (0, "CADANT-CMTS-POLICY-MIB", "cadScmAccIfIndex"),
)
if mibBuilder.loadTexts:
    cadScmAccessEntry.setStatus("current")
_CadScmAccIfIndex_Type = InterfaceIndex
_CadScmAccIfIndex_Object = MibTableColumn
cadScmAccIfIndex = _CadScmAccIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 1, 1, 1),
    _CadScmAccIfIndex_Type()
)
cadScmAccIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadScmAccIfIndex.setStatus("current")


class _CadScmAccListNumber_Type(Integer32):
    """Custom type cadScmAccListNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CadScmAccListNumber_Type.__name__ = "Integer32"
_CadScmAccListNumber_Object = MibTableColumn
cadScmAccListNumber = _CadScmAccListNumber_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 1, 1, 2),
    _CadScmAccListNumber_Type()
)
cadScmAccListNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadScmAccListNumber.setStatus("current")
_CadScmAccRowStatus_Type = RowStatus
_CadScmAccRowStatus_Object = MibTableColumn
cadScmAccRowStatus = _CadScmAccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 1, 1, 3),
    _CadScmAccRowStatus_Type()
)
cadScmAccRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadScmAccRowStatus.setStatus("current")
_CadDistListInTable_Object = MibTable
cadDistListInTable = _CadDistListInTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 2)
)
if mibBuilder.loadTexts:
    cadDistListInTable.setStatus("current")
_CadDistListInEntry_Object = MibTableRow
cadDistListInEntry = _CadDistListInEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 2, 1)
)
cadDistListInEntry.setIndexNames(
    (0, "CADANT-CMTS-POLICY-MIB", "cadDistListInProtocol"),
    (0, "CADANT-CMTS-POLICY-MIB", "cadDistListInProtocolProcess"),
    (0, "CADANT-CMTS-POLICY-MIB", "cadDistListInIfIndex"),
    (0, "CADANT-CMTS-POLICY-MIB", "cadDistListInAccessListNum"),
)
if mibBuilder.loadTexts:
    cadDistListInEntry.setStatus("current")
_CadDistListInProtocol_Type = CadPolicyProtocol
_CadDistListInProtocol_Object = MibTableColumn
cadDistListInProtocol = _CadDistListInProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 2, 1, 1),
    _CadDistListInProtocol_Type()
)
cadDistListInProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDistListInProtocol.setStatus("current")


class _CadDistListInProtocolProcess_Type(Integer32):
    """Custom type cadDistListInProtocolProcess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CadDistListInProtocolProcess_Type.__name__ = "Integer32"
_CadDistListInProtocolProcess_Object = MibTableColumn
cadDistListInProtocolProcess = _CadDistListInProtocolProcess_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 2, 1, 2),
    _CadDistListInProtocolProcess_Type()
)
cadDistListInProtocolProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDistListInProtocolProcess.setStatus("current")
_CadDistListInIfIndex_Type = InterfaceIndex
_CadDistListInIfIndex_Object = MibTableColumn
cadDistListInIfIndex = _CadDistListInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 2, 1, 3),
    _CadDistListInIfIndex_Type()
)
cadDistListInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDistListInIfIndex.setStatus("current")


class _CadDistListInAccessListNum_Type(Integer32):
    """Custom type cadDistListInAccessListNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CadDistListInAccessListNum_Type.__name__ = "Integer32"
_CadDistListInAccessListNum_Object = MibTableColumn
cadDistListInAccessListNum = _CadDistListInAccessListNum_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 2, 1, 4),
    _CadDistListInAccessListNum_Type()
)
cadDistListInAccessListNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDistListInAccessListNum.setStatus("current")


class _CadDistListInAccessListName_Type(OctetString):
    """Custom type cadDistListInAccessListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CadDistListInAccessListName_Type.__name__ = "OctetString"
_CadDistListInAccessListName_Object = MibTableColumn
cadDistListInAccessListName = _CadDistListInAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 2, 1, 5),
    _CadDistListInAccessListName_Type()
)
cadDistListInAccessListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadDistListInAccessListName.setStatus("current")
_CadDistListInStatus_Type = RowStatus
_CadDistListInStatus_Object = MibTableColumn
cadDistListInStatus = _CadDistListInStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 2, 1, 6),
    _CadDistListInStatus_Type()
)
cadDistListInStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadDistListInStatus.setStatus("current")
_CadPolicyRateLimitTable_Object = MibTable
cadPolicyRateLimitTable = _CadPolicyRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 4)
)
if mibBuilder.loadTexts:
    cadPolicyRateLimitTable.setStatus("current")
_CadPolicyRateLimitEntry_Object = MibTableRow
cadPolicyRateLimitEntry = _CadPolicyRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 4, 1)
)
cadPolicyRateLimitEntry.setIndexNames(
    (0, "CADANT-CMTS-POLICY-MIB", "cadPolicyRateLimitIfIndex"),
    (0, "CADANT-CMTS-POLICY-MIB", "cadPolicyRateLimitDirection"),
    (0, "CADANT-CMTS-POLICY-MIB", "cadPolicyRateLimitIndex"),
)
if mibBuilder.loadTexts:
    cadPolicyRateLimitEntry.setStatus("current")
_CadPolicyRateLimitIfIndex_Type = InterfaceIndex
_CadPolicyRateLimitIfIndex_Object = MibTableColumn
cadPolicyRateLimitIfIndex = _CadPolicyRateLimitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 4, 1, 1),
    _CadPolicyRateLimitIfIndex_Type()
)
cadPolicyRateLimitIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadPolicyRateLimitIfIndex.setStatus("current")
_CadPolicyRateLimitDirection_Type = CadIfDirection
_CadPolicyRateLimitDirection_Object = MibTableColumn
cadPolicyRateLimitDirection = _CadPolicyRateLimitDirection_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 4, 1, 2),
    _CadPolicyRateLimitDirection_Type()
)
cadPolicyRateLimitDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadPolicyRateLimitDirection.setStatus("current")


class _CadPolicyRateLimitIndex_Type(Integer32):
    """Custom type cadPolicyRateLimitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CadPolicyRateLimitIndex_Type.__name__ = "Integer32"
_CadPolicyRateLimitIndex_Object = MibTableColumn
cadPolicyRateLimitIndex = _CadPolicyRateLimitIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 4, 1, 3),
    _CadPolicyRateLimitIndex_Type()
)
cadPolicyRateLimitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadPolicyRateLimitIndex.setStatus("current")
_CadPolicyRateLimitStatus_Type = RowStatus
_CadPolicyRateLimitStatus_Object = MibTableColumn
cadPolicyRateLimitStatus = _CadPolicyRateLimitStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 4, 1, 4),
    _CadPolicyRateLimitStatus_Type()
)
cadPolicyRateLimitStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadPolicyRateLimitStatus.setStatus("current")


class _CadPolicyRateLimitAclType_Type(CadAclType):
    """Custom type cadPolicyRateLimitAclType based on CadAclType"""


_CadPolicyRateLimitAclType_Object = MibTableColumn
cadPolicyRateLimitAclType = _CadPolicyRateLimitAclType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 4, 1, 5),
    _CadPolicyRateLimitAclType_Type()
)
cadPolicyRateLimitAclType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadPolicyRateLimitAclType.setStatus("current")


class _CadPolicyRateLimitAclNum_Type(Integer32):
    """Custom type cadPolicyRateLimitAclNum based on Integer32"""
    defaultValue = 0


_CadPolicyRateLimitAclNum_Object = MibTableColumn
cadPolicyRateLimitAclNum = _CadPolicyRateLimitAclNum_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 4, 1, 6),
    _CadPolicyRateLimitAclNum_Type()
)
cadPolicyRateLimitAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadPolicyRateLimitAclNum.setStatus("current")


class _CadPolicyRateLimitBps_Type(Integer32):
    """Custom type cadPolicyRateLimitBps based on Integer32"""
    defaultValue = 0


_CadPolicyRateLimitBps_Object = MibTableColumn
cadPolicyRateLimitBps = _CadPolicyRateLimitBps_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 4, 1, 7),
    _CadPolicyRateLimitBps_Type()
)
cadPolicyRateLimitBps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadPolicyRateLimitBps.setStatus("current")


class _CadPolicyRateLimitBurstNormal_Type(Integer32):
    """Custom type cadPolicyRateLimitBurstNormal based on Integer32"""
    defaultValue = 0


_CadPolicyRateLimitBurstNormal_Object = MibTableColumn
cadPolicyRateLimitBurstNormal = _CadPolicyRateLimitBurstNormal_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 4, 1, 8),
    _CadPolicyRateLimitBurstNormal_Type()
)
cadPolicyRateLimitBurstNormal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadPolicyRateLimitBurstNormal.setStatus("current")


class _CadPolicyRateLimitBurstMax_Type(Integer32):
    """Custom type cadPolicyRateLimitBurstMax based on Integer32"""
    defaultValue = 0


_CadPolicyRateLimitBurstMax_Object = MibTableColumn
cadPolicyRateLimitBurstMax = _CadPolicyRateLimitBurstMax_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 4, 1, 9),
    _CadPolicyRateLimitBurstMax_Type()
)
cadPolicyRateLimitBurstMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadPolicyRateLimitBurstMax.setStatus("current")


class _CadPolicyRateLimitConformAction_Type(CadPolicyRateLimitAction):
    """Custom type cadPolicyRateLimitConformAction based on CadPolicyRateLimitAction"""


_CadPolicyRateLimitConformAction_Object = MibTableColumn
cadPolicyRateLimitConformAction = _CadPolicyRateLimitConformAction_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 4, 1, 10),
    _CadPolicyRateLimitConformAction_Type()
)
cadPolicyRateLimitConformAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadPolicyRateLimitConformAction.setStatus("current")


class _CadPolicyRateLimitConformValue_Type(Integer32):
    """Custom type cadPolicyRateLimitConformValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CadPolicyRateLimitConformValue_Type.__name__ = "Integer32"
_CadPolicyRateLimitConformValue_Object = MibTableColumn
cadPolicyRateLimitConformValue = _CadPolicyRateLimitConformValue_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 4, 1, 11),
    _CadPolicyRateLimitConformValue_Type()
)
cadPolicyRateLimitConformValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadPolicyRateLimitConformValue.setStatus("current")


class _CadPolicyRateLimitExceedAction_Type(CadPolicyRateLimitAction):
    """Custom type cadPolicyRateLimitExceedAction based on CadPolicyRateLimitAction"""


_CadPolicyRateLimitExceedAction_Object = MibTableColumn
cadPolicyRateLimitExceedAction = _CadPolicyRateLimitExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 4, 1, 12),
    _CadPolicyRateLimitExceedAction_Type()
)
cadPolicyRateLimitExceedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadPolicyRateLimitExceedAction.setStatus("current")


class _CadPolicyRateLimitExceedValue_Type(Integer32):
    """Custom type cadPolicyRateLimitExceedValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CadPolicyRateLimitExceedValue_Type.__name__ = "Integer32"
_CadPolicyRateLimitExceedValue_Object = MibTableColumn
cadPolicyRateLimitExceedValue = _CadPolicyRateLimitExceedValue_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 4, 1, 13),
    _CadPolicyRateLimitExceedValue_Type()
)
cadPolicyRateLimitExceedValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadPolicyRateLimitExceedValue.setStatus("current")


class _CadPolicyRateLimitClearCounts_Type(TruthValue):
    """Custom type cadPolicyRateLimitClearCounts based on TruthValue"""


_CadPolicyRateLimitClearCounts_Object = MibTableColumn
cadPolicyRateLimitClearCounts = _CadPolicyRateLimitClearCounts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 4, 1, 14),
    _CadPolicyRateLimitClearCounts_Type()
)
cadPolicyRateLimitClearCounts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadPolicyRateLimitClearCounts.setStatus("current")
_CadPolicyRateLimitStatusTable_Object = MibTable
cadPolicyRateLimitStatusTable = _CadPolicyRateLimitStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 5)
)
if mibBuilder.loadTexts:
    cadPolicyRateLimitStatusTable.setStatus("current")
_CadPolicyRateLimitStatusEntry_Object = MibTableRow
cadPolicyRateLimitStatusEntry = _CadPolicyRateLimitStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cadPolicyRateLimitStatusEntry.setStatus("current")
_CadPolicyRateLimitConformPackets_Type = Counter64
_CadPolicyRateLimitConformPackets_Object = MibTableColumn
cadPolicyRateLimitConformPackets = _CadPolicyRateLimitConformPackets_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 5, 1, 1),
    _CadPolicyRateLimitConformPackets_Type()
)
cadPolicyRateLimitConformPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPolicyRateLimitConformPackets.setStatus("current")
_CadPolicyRateLimitConformBytes_Type = Counter64
_CadPolicyRateLimitConformBytes_Object = MibTableColumn
cadPolicyRateLimitConformBytes = _CadPolicyRateLimitConformBytes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 5, 1, 2),
    _CadPolicyRateLimitConformBytes_Type()
)
cadPolicyRateLimitConformBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPolicyRateLimitConformBytes.setStatus("current")
_CadPolicyRateLimitExceedPackets_Type = Counter64
_CadPolicyRateLimitExceedPackets_Object = MibTableColumn
cadPolicyRateLimitExceedPackets = _CadPolicyRateLimitExceedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 5, 1, 3),
    _CadPolicyRateLimitExceedPackets_Type()
)
cadPolicyRateLimitExceedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPolicyRateLimitExceedPackets.setStatus("current")
_CadPolicyRateLimitExceedBytes_Type = Counter64
_CadPolicyRateLimitExceedBytes_Object = MibTableColumn
cadPolicyRateLimitExceedBytes = _CadPolicyRateLimitExceedBytes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 5, 1, 4),
    _CadPolicyRateLimitExceedBytes_Type()
)
cadPolicyRateLimitExceedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPolicyRateLimitExceedBytes.setStatus("current")
_CadPolicyRateLimitCurrentBurst_Type = Integer32
_CadPolicyRateLimitCurrentBurst_Object = MibTableColumn
cadPolicyRateLimitCurrentBurst = _CadPolicyRateLimitCurrentBurst_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 5, 1, 5),
    _CadPolicyRateLimitCurrentBurst_Type()
)
cadPolicyRateLimitCurrentBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPolicyRateLimitCurrentBurst.setStatus("current")
_CadPolicyRateLimitLastCleared_Type = TimeStamp
_CadPolicyRateLimitLastCleared_Object = MibTableColumn
cadPolicyRateLimitLastCleared = _CadPolicyRateLimitLastCleared_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 5, 1, 6),
    _CadPolicyRateLimitLastCleared_Type()
)
cadPolicyRateLimitLastCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPolicyRateLimitLastCleared.setStatus("current")
_CadPolicyAclTable_Object = MibTable
cadPolicyAclTable = _CadPolicyAclTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 6)
)
if mibBuilder.loadTexts:
    cadPolicyAclTable.setStatus("current")
_CadPolicyAclEntry_Object = MibTableRow
cadPolicyAclEntry = _CadPolicyAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 6, 1)
)
cadPolicyAclEntry.setIndexNames(
    (0, "CADANT-CMTS-POLICY-MIB", "cadAclNumber"),
    (0, "CADANT-CMTS-POLICY-MIB", "cadAclIndex"),
)
if mibBuilder.loadTexts:
    cadPolicyAclEntry.setStatus("current")


class _CadAclNumber_Type(Integer32):
    """Custom type cadAclNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 399),
    )


_CadAclNumber_Type.__name__ = "Integer32"
_CadAclNumber_Object = MibTableColumn
cadAclNumber = _CadAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 6, 1, 1),
    _CadAclNumber_Type()
)
cadAclNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadAclNumber.setStatus("current")


class _CadAclIndex_Type(Integer32):
    """Custom type cadAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CadAclIndex_Type.__name__ = "Integer32"
_CadAclIndex_Object = MibTableColumn
cadAclIndex = _CadAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 6, 1, 2),
    _CadAclIndex_Type()
)
cadAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadAclIndex.setStatus("current")
_CadAclType_Type = CadAclType
_CadAclType_Object = MibTableColumn
cadAclType = _CadAclType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 6, 1, 3),
    _CadAclType_Type()
)
cadAclType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadAclType.setStatus("current")
_CadAclStatus_Type = RowStatus
_CadAclStatus_Object = MibTableColumn
cadAclStatus = _CadAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 6, 1, 4),
    _CadAclStatus_Type()
)
cadAclStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadAclStatus.setStatus("current")


class _CadAclPermit_Type(TruthValue):
    """Custom type cadAclPermit based on TruthValue"""


_CadAclPermit_Object = MibTableColumn
cadAclPermit = _CadAclPermit_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 6, 1, 5),
    _CadAclPermit_Type()
)
cadAclPermit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadAclPermit.setStatus("current")


class _CadAclProtocol_Type(CadProtocolType):
    """Custom type cadAclProtocol based on CadProtocolType"""
    defaultValue = -1


_CadAclProtocol_Object = MibTableColumn
cadAclProtocol = _CadAclProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 6, 1, 6),
    _CadAclProtocol_Type()
)
cadAclProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadAclProtocol.setStatus("current")


class _CadAclSrcIp_Type(InetAddressIPv4or6):
    """Custom type cadAclSrcIp based on InetAddressIPv4or6"""
    defaultHexValue = "00000000"


_CadAclSrcIp_Object = MibTableColumn
cadAclSrcIp = _CadAclSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 6, 1, 7),
    _CadAclSrcIp_Type()
)
cadAclSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadAclSrcIp.setStatus("current")


class _CadAclSrcIpMask_Type(InetAddressIPv4or6):
    """Custom type cadAclSrcIpMask based on InetAddressIPv4or6"""
    defaultHexValue = "FFFFFFFF"


_CadAclSrcIpMask_Object = MibTableColumn
cadAclSrcIpMask = _CadAclSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 6, 1, 8),
    _CadAclSrcIpMask_Type()
)
cadAclSrcIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadAclSrcIpMask.setStatus("current")


class _CadAclSrcPortOp_Type(CadExtAclCondition):
    """Custom type cadAclSrcPortOp based on CadExtAclCondition"""


_CadAclSrcPortOp_Object = MibTableColumn
cadAclSrcPortOp = _CadAclSrcPortOp_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 6, 1, 9),
    _CadAclSrcPortOp_Type()
)
cadAclSrcPortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadAclSrcPortOp.setStatus("current")


class _CadAclSrcPortLo_Type(Integer32):
    """Custom type cadAclSrcPortLo based on Integer32"""
    defaultValue = -1


_CadAclSrcPortLo_Object = MibTableColumn
cadAclSrcPortLo = _CadAclSrcPortLo_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 6, 1, 10),
    _CadAclSrcPortLo_Type()
)
cadAclSrcPortLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadAclSrcPortLo.setStatus("current")


class _CadAclSrcPortHi_Type(Integer32):
    """Custom type cadAclSrcPortHi based on Integer32"""
    defaultValue = -1


_CadAclSrcPortHi_Object = MibTableColumn
cadAclSrcPortHi = _CadAclSrcPortHi_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 6, 1, 11),
    _CadAclSrcPortHi_Type()
)
cadAclSrcPortHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadAclSrcPortHi.setStatus("current")


class _CadAclDstIp_Type(InetAddressIPv4or6):
    """Custom type cadAclDstIp based on InetAddressIPv4or6"""
    defaultHexValue = "00000000"


_CadAclDstIp_Object = MibTableColumn
cadAclDstIp = _CadAclDstIp_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 6, 1, 12),
    _CadAclDstIp_Type()
)
cadAclDstIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadAclDstIp.setStatus("current")


class _CadAclDstIpMask_Type(InetAddressIPv4or6):
    """Custom type cadAclDstIpMask based on InetAddressIPv4or6"""
    defaultHexValue = "FFFFFFFF"


_CadAclDstIpMask_Object = MibTableColumn
cadAclDstIpMask = _CadAclDstIpMask_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 6, 1, 13),
    _CadAclDstIpMask_Type()
)
cadAclDstIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadAclDstIpMask.setStatus("current")


class _CadAclDstPortOp_Type(CadExtAclCondition):
    """Custom type cadAclDstPortOp based on CadExtAclCondition"""


_CadAclDstPortOp_Object = MibTableColumn
cadAclDstPortOp = _CadAclDstPortOp_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 6, 1, 14),
    _CadAclDstPortOp_Type()
)
cadAclDstPortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadAclDstPortOp.setStatus("current")


class _CadAclDstPortLo_Type(Integer32):
    """Custom type cadAclDstPortLo based on Integer32"""
    defaultValue = -1


_CadAclDstPortLo_Object = MibTableColumn
cadAclDstPortLo = _CadAclDstPortLo_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 6, 1, 15),
    _CadAclDstPortLo_Type()
)
cadAclDstPortLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadAclDstPortLo.setStatus("current")


class _CadAclDstPortHi_Type(Integer32):
    """Custom type cadAclDstPortHi based on Integer32"""
    defaultValue = -1


_CadAclDstPortHi_Object = MibTableColumn
cadAclDstPortHi = _CadAclDstPortHi_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 6, 1, 16),
    _CadAclDstPortHi_Type()
)
cadAclDstPortHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadAclDstPortHi.setStatus("current")


class _CadAclLogging_Type(TruthValue):
    """Custom type cadAclLogging based on TruthValue"""


_CadAclLogging_Object = MibTableColumn
cadAclLogging = _CadAclLogging_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 6, 1, 17),
    _CadAclLogging_Type()
)
cadAclLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadAclLogging.setStatus("current")


class _CadAclProtoType_Type(Integer32):
    """Custom type cadAclProtoType based on Integer32"""
    defaultValue = -1


_CadAclProtoType_Object = MibTableColumn
cadAclProtoType = _CadAclProtoType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 6, 1, 18),
    _CadAclProtoType_Type()
)
cadAclProtoType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadAclProtoType.setStatus("current")


class _CadAclProtoCode_Type(Integer32):
    """Custom type cadAclProtoCode based on Integer32"""
    defaultValue = -1


_CadAclProtoCode_Object = MibTableColumn
cadAclProtoCode = _CadAclProtoCode_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 6, 1, 19),
    _CadAclProtoCode_Type()
)
cadAclProtoCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadAclProtoCode.setStatus("current")


class _CadAclIpTos_Type(CadIpTos):
    """Custom type cadAclIpTos based on CadIpTos"""
    defaultValue = 0


_CadAclIpTos_Object = MibTableColumn
cadAclIpTos = _CadAclIpTos_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 6, 1, 20),
    _CadAclIpTos_Type()
)
cadAclIpTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadAclIpTos.setStatus("current")


class _CadAclIpTosMask_Type(CadIpTosMask):
    """Custom type cadAclIpTosMask based on CadIpTosMask"""
    defaultValue = 0


_CadAclIpTosMask_Object = MibTableColumn
cadAclIpTosMask = _CadAclIpTosMask_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 6, 1, 21),
    _CadAclIpTosMask_Type()
)
cadAclIpTosMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadAclIpTosMask.setStatus("current")


class _CadAclTcpFlags_Type(CadTcpFlags):
    """Custom type cadAclTcpFlags based on CadTcpFlags"""
    defaultBinValue = "0"


_CadAclTcpFlags_Object = MibTableColumn
cadAclTcpFlags = _CadAclTcpFlags_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 6, 1, 22),
    _CadAclTcpFlags_Type()
)
cadAclTcpFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadAclTcpFlags.setStatus("current")


class _CadAclTcpFlagsMask_Type(CadTcpFlags):
    """Custom type cadAclTcpFlagsMask based on CadTcpFlags"""
    defaultBinValue = "0"


_CadAclTcpFlagsMask_Object = MibTableColumn
cadAclTcpFlagsMask = _CadAclTcpFlagsMask_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 6, 1, 23),
    _CadAclTcpFlagsMask_Type()
)
cadAclTcpFlagsMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadAclTcpFlagsMask.setStatus("current")


class _CadAclFragments_Type(TruthValue):
    """Custom type cadAclFragments based on TruthValue"""


_CadAclFragments_Object = MibTableColumn
cadAclFragments = _CadAclFragments_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 6, 1, 24),
    _CadAclFragments_Type()
)
cadAclFragments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadAclFragments.setStatus("current")


class _CadAclRemark_Type(CadAclString):
    """Custom type cadAclRemark based on CadAclString"""
    defaultHexValue = ""


_CadAclRemark_Object = MibTableColumn
cadAclRemark = _CadAclRemark_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 6, 1, 26),
    _CadAclRemark_Type()
)
cadAclRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadAclRemark.setStatus("current")


class _CadAclIpAddrType_Type(InetAddressType):
    """Custom type cadAclIpAddrType based on InetAddressType"""


_CadAclIpAddrType_Object = MibTableColumn
cadAclIpAddrType = _CadAclIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 6, 1, 27),
    _CadAclIpAddrType_Type()
)
cadAclIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadAclIpAddrType.setStatus("current")
_CadSnmpCommAccessTable_Object = MibTable
cadSnmpCommAccessTable = _CadSnmpCommAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 7)
)
if mibBuilder.loadTexts:
    cadSnmpCommAccessTable.setStatus("current")
_CadSnmpCommAccessEntry_Object = MibTableRow
cadSnmpCommAccessEntry = _CadSnmpCommAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 7, 1)
)
cadSnmpCommAccessEntry.setIndexNames(
    (1, "CADANT-CMTS-POLICY-MIB", "cadSnmpCommAccessName"),
)
if mibBuilder.loadTexts:
    cadSnmpCommAccessEntry.setStatus("current")


class _CadSnmpCommAccessName_Type(SnmpAdminString):
    """Custom type cadSnmpCommAccessName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CadSnmpCommAccessName_Type.__name__ = "SnmpAdminString"
_CadSnmpCommAccessName_Object = MibTableColumn
cadSnmpCommAccessName = _CadSnmpCommAccessName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 7, 1, 1),
    _CadSnmpCommAccessName_Type()
)
cadSnmpCommAccessName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadSnmpCommAccessName.setStatus("current")


class _CadSnmpCommAccessList_Type(Integer32):
    """Custom type cadSnmpCommAccessList based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CadSnmpCommAccessList_Type.__name__ = "Integer32"
_CadSnmpCommAccessList_Object = MibTableColumn
cadSnmpCommAccessList = _CadSnmpCommAccessList_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 7, 1, 2),
    _CadSnmpCommAccessList_Type()
)
cadSnmpCommAccessList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSnmpCommAccessList.setStatus("current")
_CadSnmpCommAccessStatus_Type = RowStatus
_CadSnmpCommAccessStatus_Object = MibTableColumn
cadSnmpCommAccessStatus = _CadSnmpCommAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 7, 1, 3),
    _CadSnmpCommAccessStatus_Type()
)
cadSnmpCommAccessStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadSnmpCommAccessStatus.setStatus("current")
_CadPolicyAccessGroupTable_Object = MibTable
cadPolicyAccessGroupTable = _CadPolicyAccessGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 8)
)
if mibBuilder.loadTexts:
    cadPolicyAccessGroupTable.setStatus("current")
_CadPolicyAccessGroupEntry_Object = MibTableRow
cadPolicyAccessGroupEntry = _CadPolicyAccessGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 8, 1)
)
cadPolicyAccessGroupEntry.setIndexNames(
    (0, "CADANT-CMTS-POLICY-MIB", "cadPolicyAccessGroupIfIndex"),
    (0, "CADANT-CMTS-POLICY-MIB", "cadPolicyAccessGroupDirection"),
)
if mibBuilder.loadTexts:
    cadPolicyAccessGroupEntry.setStatus("current")
_CadPolicyAccessGroupIfIndex_Type = InterfaceIndex
_CadPolicyAccessGroupIfIndex_Object = MibTableColumn
cadPolicyAccessGroupIfIndex = _CadPolicyAccessGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 8, 1, 1),
    _CadPolicyAccessGroupIfIndex_Type()
)
cadPolicyAccessGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadPolicyAccessGroupIfIndex.setStatus("current")
_CadPolicyAccessGroupDirection_Type = CadIfDirection
_CadPolicyAccessGroupDirection_Object = MibTableColumn
cadPolicyAccessGroupDirection = _CadPolicyAccessGroupDirection_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 8, 1, 2),
    _CadPolicyAccessGroupDirection_Type()
)
cadPolicyAccessGroupDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadPolicyAccessGroupDirection.setStatus("current")
_CadPolicyAccessGroupStatus_Type = RowStatus
_CadPolicyAccessGroupStatus_Object = MibTableColumn
cadPolicyAccessGroupStatus = _CadPolicyAccessGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 8, 1, 3),
    _CadPolicyAccessGroupStatus_Type()
)
cadPolicyAccessGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadPolicyAccessGroupStatus.setStatus("current")


class _CadPolicyAccessGroupIpv4AclNum_Type(Integer32):
    """Custom type cadPolicyAccessGroupIpv4AclNum based on Integer32"""
    defaultValue = 0


_CadPolicyAccessGroupIpv4AclNum_Object = MibTableColumn
cadPolicyAccessGroupIpv4AclNum = _CadPolicyAccessGroupIpv4AclNum_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 8, 1, 4),
    _CadPolicyAccessGroupIpv4AclNum_Type()
)
cadPolicyAccessGroupIpv4AclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadPolicyAccessGroupIpv4AclNum.setStatus("current")


class _CadPolicyAccessGroupClearCounts_Type(TruthValue):
    """Custom type cadPolicyAccessGroupClearCounts based on TruthValue"""


_CadPolicyAccessGroupClearCounts_Object = MibTableColumn
cadPolicyAccessGroupClearCounts = _CadPolicyAccessGroupClearCounts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 8, 1, 5),
    _CadPolicyAccessGroupClearCounts_Type()
)
cadPolicyAccessGroupClearCounts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadPolicyAccessGroupClearCounts.setStatus("current")


class _CadPolicyAccessGroupIpv6AclNum_Type(Integer32):
    """Custom type cadPolicyAccessGroupIpv6AclNum based on Integer32"""
    defaultValue = 0


_CadPolicyAccessGroupIpv6AclNum_Object = MibTableColumn
cadPolicyAccessGroupIpv6AclNum = _CadPolicyAccessGroupIpv6AclNum_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 8, 1, 6),
    _CadPolicyAccessGroupIpv6AclNum_Type()
)
cadPolicyAccessGroupIpv6AclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadPolicyAccessGroupIpv6AclNum.setStatus("current")


class _CadPolicyAccessGroupIpv6AclName_Type(SnmpAdminString):
    """Custom type cadPolicyAccessGroupIpv6AclName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CadPolicyAccessGroupIpv6AclName_Type.__name__ = "SnmpAdminString"
_CadPolicyAccessGroupIpv6AclName_Object = MibTableColumn
cadPolicyAccessGroupIpv6AclName = _CadPolicyAccessGroupIpv6AclName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 8, 1, 7),
    _CadPolicyAccessGroupIpv6AclName_Type()
)
cadPolicyAccessGroupIpv6AclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadPolicyAccessGroupIpv6AclName.setStatus("current")
_CadPolicyAccessGroupStatusTable_Object = MibTable
cadPolicyAccessGroupStatusTable = _CadPolicyAccessGroupStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 9)
)
if mibBuilder.loadTexts:
    cadPolicyAccessGroupStatusTable.setStatus("current")
_CadPolicyAccessGroupStatusEntry_Object = MibTableRow
cadPolicyAccessGroupStatusEntry = _CadPolicyAccessGroupStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 9, 1)
)
if mibBuilder.loadTexts:
    cadPolicyAccessGroupStatusEntry.setStatus("current")
_CadPolicyAccessGroupPermitPackets_Type = Counter64
_CadPolicyAccessGroupPermitPackets_Object = MibTableColumn
cadPolicyAccessGroupPermitPackets = _CadPolicyAccessGroupPermitPackets_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 9, 1, 1),
    _CadPolicyAccessGroupPermitPackets_Type()
)
cadPolicyAccessGroupPermitPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPolicyAccessGroupPermitPackets.setStatus("current")
_CadPolicyAccessGroupDenyPackets_Type = Counter64
_CadPolicyAccessGroupDenyPackets_Object = MibTableColumn
cadPolicyAccessGroupDenyPackets = _CadPolicyAccessGroupDenyPackets_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 9, 1, 2),
    _CadPolicyAccessGroupDenyPackets_Type()
)
cadPolicyAccessGroupDenyPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPolicyAccessGroupDenyPackets.setStatus("current")
_CadPolicyAccessGroupLastCleared_Type = TimeStamp
_CadPolicyAccessGroupLastCleared_Object = MibTableColumn
cadPolicyAccessGroupLastCleared = _CadPolicyAccessGroupLastCleared_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 9, 1, 3),
    _CadPolicyAccessGroupLastCleared_Type()
)
cadPolicyAccessGroupLastCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPolicyAccessGroupLastCleared.setStatus("current")
_CadPolicyPfxListTable_Object = MibTable
cadPolicyPfxListTable = _CadPolicyPfxListTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 11)
)
if mibBuilder.loadTexts:
    cadPolicyPfxListTable.setStatus("current")
_CadPolicyPfxListEntry_Object = MibTableRow
cadPolicyPfxListEntry = _CadPolicyPfxListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 11, 1)
)
cadPolicyPfxListEntry.setIndexNames(
    (0, "CADANT-CMTS-POLICY-MIB", "cadPolicyPfxListNumber"),
    (0, "CADANT-CMTS-POLICY-MIB", "cadPolicyPfxListName"),
    (0, "CADANT-CMTS-POLICY-MIB", "cadPolicyPfxListSeqNumber"),
    (0, "CADANT-CMTS-POLICY-MIB", "cadPolicyPfxListAfi"),
    (0, "CADANT-CMTS-POLICY-MIB", "cadPolicyPfxListSafi"),
    (0, "CADANT-CMTS-POLICY-MIB", "cadPolicyPfxListIpAddress"),
    (0, "CADANT-CMTS-POLICY-MIB", "cadPolicyPfxListIpAddMaskLen"),
    (0, "CADANT-CMTS-POLICY-MIB", "cadPolicyPfxListMaskGeValue"),
    (0, "CADANT-CMTS-POLICY-MIB", "cadPolicyPfxListMaskLeValue"),
)
if mibBuilder.loadTexts:
    cadPolicyPfxListEntry.setStatus("current")


class _CadPolicyPfxListNumber_Type(Integer32):
    """Custom type cadPolicyPfxListNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CadPolicyPfxListNumber_Type.__name__ = "Integer32"
_CadPolicyPfxListNumber_Object = MibTableColumn
cadPolicyPfxListNumber = _CadPolicyPfxListNumber_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 11, 1, 1),
    _CadPolicyPfxListNumber_Type()
)
cadPolicyPfxListNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPolicyPfxListNumber.setStatus("current")


class _CadPolicyPfxListName_Type(OctetString):
    """Custom type cadPolicyPfxListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CadPolicyPfxListName_Type.__name__ = "OctetString"
_CadPolicyPfxListName_Object = MibTableColumn
cadPolicyPfxListName = _CadPolicyPfxListName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 11, 1, 2),
    _CadPolicyPfxListName_Type()
)
cadPolicyPfxListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPolicyPfxListName.setStatus("current")


class _CadPolicyPfxListSeqNumber_Type(Integer32):
    """Custom type cadPolicyPfxListSeqNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 2147483645),
    )


_CadPolicyPfxListSeqNumber_Type.__name__ = "Integer32"
_CadPolicyPfxListSeqNumber_Object = MibTableColumn
cadPolicyPfxListSeqNumber = _CadPolicyPfxListSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 11, 1, 3),
    _CadPolicyPfxListSeqNumber_Type()
)
cadPolicyPfxListSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPolicyPfxListSeqNumber.setStatus("current")
_CadPolicyPfxListIpAddress_Type = InetAddress
_CadPolicyPfxListIpAddress_Object = MibTableColumn
cadPolicyPfxListIpAddress = _CadPolicyPfxListIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 11, 1, 4),
    _CadPolicyPfxListIpAddress_Type()
)
cadPolicyPfxListIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPolicyPfxListIpAddress.setStatus("current")


class _CadPolicyPfxListIpAddMaskLen_Type(Integer32):
    """Custom type cadPolicyPfxListIpAddMaskLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CadPolicyPfxListIpAddMaskLen_Type.__name__ = "Integer32"
_CadPolicyPfxListIpAddMaskLen_Object = MibTableColumn
cadPolicyPfxListIpAddMaskLen = _CadPolicyPfxListIpAddMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 11, 1, 5),
    _CadPolicyPfxListIpAddMaskLen_Type()
)
cadPolicyPfxListIpAddMaskLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPolicyPfxListIpAddMaskLen.setStatus("current")


class _CadPolicyPfxListMaskGeValue_Type(Integer32):
    """Custom type cadPolicyPfxListMaskGeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CadPolicyPfxListMaskGeValue_Type.__name__ = "Integer32"
_CadPolicyPfxListMaskGeValue_Object = MibTableColumn
cadPolicyPfxListMaskGeValue = _CadPolicyPfxListMaskGeValue_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 11, 1, 6),
    _CadPolicyPfxListMaskGeValue_Type()
)
cadPolicyPfxListMaskGeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPolicyPfxListMaskGeValue.setStatus("current")


class _CadPolicyPfxListMaskLeValue_Type(Integer32):
    """Custom type cadPolicyPfxListMaskLeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CadPolicyPfxListMaskLeValue_Type.__name__ = "Integer32"
_CadPolicyPfxListMaskLeValue_Object = MibTableColumn
cadPolicyPfxListMaskLeValue = _CadPolicyPfxListMaskLeValue_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 11, 1, 7),
    _CadPolicyPfxListMaskLeValue_Type()
)
cadPolicyPfxListMaskLeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPolicyPfxListMaskLeValue.setStatus("current")
_CadPolicyPfxListAction_Type = CadPolicyAction
_CadPolicyPfxListAction_Object = MibTableColumn
cadPolicyPfxListAction = _CadPolicyPfxListAction_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 11, 1, 8),
    _CadPolicyPfxListAction_Type()
)
cadPolicyPfxListAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadPolicyPfxListAction.setStatus("current")
_CadPolicyPfxListStatus_Type = RowStatus
_CadPolicyPfxListStatus_Object = MibTableColumn
cadPolicyPfxListStatus = _CadPolicyPfxListStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 11, 1, 9),
    _CadPolicyPfxListStatus_Type()
)
cadPolicyPfxListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadPolicyPfxListStatus.setStatus("current")
_CadPolicyPfxListAfi_Type = InetAddressType
_CadPolicyPfxListAfi_Object = MibTableColumn
cadPolicyPfxListAfi = _CadPolicyPfxListAfi_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 11, 1, 10),
    _CadPolicyPfxListAfi_Type()
)
cadPolicyPfxListAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadPolicyPfxListAfi.setStatus("current")


class _CadPolicyPfxListSafi_Type(Integer32):
    """Custom type cadPolicyPfxListSafi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              128)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("mplsBgpVpn", 128),
          ("multicast", 2),
          ("unicast", 1))
    )


_CadPolicyPfxListSafi_Type.__name__ = "Integer32"
_CadPolicyPfxListSafi_Object = MibTableColumn
cadPolicyPfxListSafi = _CadPolicyPfxListSafi_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 11, 1, 11),
    _CadPolicyPfxListSafi_Type()
)
cadPolicyPfxListSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadPolicyPfxListSafi.setStatus("current")
_CadPolicyDistListOutTable_Object = MibTable
cadPolicyDistListOutTable = _CadPolicyDistListOutTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 12)
)
if mibBuilder.loadTexts:
    cadPolicyDistListOutTable.setStatus("current")
_CadPolicyDistListOutEntry_Object = MibTableRow
cadPolicyDistListOutEntry = _CadPolicyDistListOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 12, 1)
)
cadPolicyDistListOutEntry.setIndexNames(
    (0, "CADANT-CMTS-POLICY-MIB", "cadPolicyDistListOutSrcProtocol"),
    (0, "CADANT-CMTS-POLICY-MIB", "cadPolicyDistListOutSrcProtocolProcess"),
    (0, "CADANT-CMTS-POLICY-MIB", "cadPolicyDistListOutRoutingProtocol"),
    (0, "CADANT-CMTS-POLICY-MIB", "cadPolicyDistListOutRoutingProcess"),
    (0, "CADANT-CMTS-POLICY-MIB", "cadPolicyDistListOutAutonomousSystemNum"),
    (0, "CADANT-CMTS-POLICY-MIB", "cadPolicyDistListOutIfIndex"),
    (0, "CADANT-CMTS-POLICY-MIB", "cadPolicyDistListOutAccessListNum"),
)
if mibBuilder.loadTexts:
    cadPolicyDistListOutEntry.setStatus("current")
_CadPolicyDistListOutSrcProtocol_Type = CadPolicyProtocol
_CadPolicyDistListOutSrcProtocol_Object = MibTableColumn
cadPolicyDistListOutSrcProtocol = _CadPolicyDistListOutSrcProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 12, 1, 1),
    _CadPolicyDistListOutSrcProtocol_Type()
)
cadPolicyDistListOutSrcProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPolicyDistListOutSrcProtocol.setStatus("current")


class _CadPolicyDistListOutSrcProtocolProcess_Type(Integer32):
    """Custom type cadPolicyDistListOutSrcProtocolProcess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CadPolicyDistListOutSrcProtocolProcess_Type.__name__ = "Integer32"
_CadPolicyDistListOutSrcProtocolProcess_Object = MibTableColumn
cadPolicyDistListOutSrcProtocolProcess = _CadPolicyDistListOutSrcProtocolProcess_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 12, 1, 2),
    _CadPolicyDistListOutSrcProtocolProcess_Type()
)
cadPolicyDistListOutSrcProtocolProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPolicyDistListOutSrcProtocolProcess.setStatus("current")
_CadPolicyDistListOutRoutingProtocol_Type = CadPolicyProtocol
_CadPolicyDistListOutRoutingProtocol_Object = MibTableColumn
cadPolicyDistListOutRoutingProtocol = _CadPolicyDistListOutRoutingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 12, 1, 3),
    _CadPolicyDistListOutRoutingProtocol_Type()
)
cadPolicyDistListOutRoutingProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPolicyDistListOutRoutingProtocol.setStatus("current")


class _CadPolicyDistListOutRoutingProcess_Type(Integer32):
    """Custom type cadPolicyDistListOutRoutingProcess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CadPolicyDistListOutRoutingProcess_Type.__name__ = "Integer32"
_CadPolicyDistListOutRoutingProcess_Object = MibTableColumn
cadPolicyDistListOutRoutingProcess = _CadPolicyDistListOutRoutingProcess_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 12, 1, 4),
    _CadPolicyDistListOutRoutingProcess_Type()
)
cadPolicyDistListOutRoutingProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPolicyDistListOutRoutingProcess.setStatus("current")


class _CadPolicyDistListOutAutonomousSystemNum_Type(Integer32):
    """Custom type cadPolicyDistListOutAutonomousSystemNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_CadPolicyDistListOutAutonomousSystemNum_Type.__name__ = "Integer32"
_CadPolicyDistListOutAutonomousSystemNum_Object = MibTableColumn
cadPolicyDistListOutAutonomousSystemNum = _CadPolicyDistListOutAutonomousSystemNum_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 12, 1, 5),
    _CadPolicyDistListOutAutonomousSystemNum_Type()
)
cadPolicyDistListOutAutonomousSystemNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPolicyDistListOutAutonomousSystemNum.setStatus("current")


class _CadPolicyDistListOutAccessListNum_Type(Integer32):
    """Custom type cadPolicyDistListOutAccessListNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CadPolicyDistListOutAccessListNum_Type.__name__ = "Integer32"
_CadPolicyDistListOutAccessListNum_Object = MibTableColumn
cadPolicyDistListOutAccessListNum = _CadPolicyDistListOutAccessListNum_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 12, 1, 6),
    _CadPolicyDistListOutAccessListNum_Type()
)
cadPolicyDistListOutAccessListNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPolicyDistListOutAccessListNum.setStatus("current")


class _CadPolicyDistListOutAccessListName_Type(OctetString):
    """Custom type cadPolicyDistListOutAccessListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CadPolicyDistListOutAccessListName_Type.__name__ = "OctetString"
_CadPolicyDistListOutAccessListName_Object = MibTableColumn
cadPolicyDistListOutAccessListName = _CadPolicyDistListOutAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 12, 1, 7),
    _CadPolicyDistListOutAccessListName_Type()
)
cadPolicyDistListOutAccessListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadPolicyDistListOutAccessListName.setStatus("current")
_CadPolicyDistListOutStatus_Type = RowStatus
_CadPolicyDistListOutStatus_Object = MibTableColumn
cadPolicyDistListOutStatus = _CadPolicyDistListOutStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 12, 1, 8),
    _CadPolicyDistListOutStatus_Type()
)
cadPolicyDistListOutStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadPolicyDistListOutStatus.setStatus("current")
_CadPolicyDistListOutIfIndex_Type = InterfaceIndex
_CadPolicyDistListOutIfIndex_Object = MibTableColumn
cadPolicyDistListOutIfIndex = _CadPolicyDistListOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 12, 1, 9),
    _CadPolicyDistListOutIfIndex_Type()
)
cadPolicyDistListOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadPolicyDistListOutIfIndex.setStatus("current")
_CadDistListOutTable_Object = MibTable
cadDistListOutTable = _CadDistListOutTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 13)
)
if mibBuilder.loadTexts:
    cadDistListOutTable.setStatus("current")
_CadDistListOutEntry_Object = MibTableRow
cadDistListOutEntry = _CadDistListOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 13, 1)
)
cadDistListOutEntry.setIndexNames(
    (0, "CADANT-CMTS-POLICY-MIB", "cadDistListOutVrIndex"),
    (0, "CADANT-CMTS-POLICY-MIB", "cadDistListOutDestProtocol"),
    (0, "CADANT-CMTS-POLICY-MIB", "cadDistListOutSrcProtocol"),
)
if mibBuilder.loadTexts:
    cadDistListOutEntry.setStatus("current")


class _CadDistListOutVrIndex_Type(Integer32):
    """Custom type cadDistListOutVrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CadDistListOutVrIndex_Type.__name__ = "Integer32"
_CadDistListOutVrIndex_Object = MibTableColumn
cadDistListOutVrIndex = _CadDistListOutVrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 13, 1, 1),
    _CadDistListOutVrIndex_Type()
)
cadDistListOutVrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDistListOutVrIndex.setStatus("current")
_CadDistListOutDestProtocol_Type = InfoSourceDest
_CadDistListOutDestProtocol_Object = MibTableColumn
cadDistListOutDestProtocol = _CadDistListOutDestProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 13, 1, 2),
    _CadDistListOutDestProtocol_Type()
)
cadDistListOutDestProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDistListOutDestProtocol.setStatus("current")
_CadDistListOutSrcProtocol_Type = InfoSourceDest
_CadDistListOutSrcProtocol_Object = MibTableColumn
cadDistListOutSrcProtocol = _CadDistListOutSrcProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 13, 1, 3),
    _CadDistListOutSrcProtocol_Type()
)
cadDistListOutSrcProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDistListOutSrcProtocol.setStatus("current")


class _CadDistListOutAccessListNum_Type(Integer32):
    """Custom type cadDistListOutAccessListNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_CadDistListOutAccessListNum_Type.__name__ = "Integer32"
_CadDistListOutAccessListNum_Object = MibTableColumn
cadDistListOutAccessListNum = _CadDistListOutAccessListNum_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 13, 1, 4),
    _CadDistListOutAccessListNum_Type()
)
cadDistListOutAccessListNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadDistListOutAccessListNum.setStatus("current")
_CadDistListOutStatus_Type = RowStatus
_CadDistListOutStatus_Object = MibTableColumn
cadDistListOutStatus = _CadDistListOutStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 13, 1, 5),
    _CadDistListOutStatus_Type()
)
cadDistListOutStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadDistListOutStatus.setStatus("current")


class _CadDistListOutAccessListName_Type(SnmpAdminString):
    """Custom type cadDistListOutAccessListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CadDistListOutAccessListName_Type.__name__ = "SnmpAdminString"
_CadDistListOutAccessListName_Object = MibTableColumn
cadDistListOutAccessListName = _CadDistListOutAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 13, 1, 6),
    _CadDistListOutAccessListName_Type()
)
cadDistListOutAccessListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadDistListOutAccessListName.setStatus("current")
_CadAclNameTable_Object = MibTable
cadAclNameTable = _CadAclNameTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 14)
)
if mibBuilder.loadTexts:
    cadAclNameTable.setStatus("current")
_CadAclNameEntry_Object = MibTableRow
cadAclNameEntry = _CadAclNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 14, 1)
)
cadAclNameEntry.setIndexNames(
    (0, "CADANT-CMTS-POLICY-MIB", "cadNameAclName"),
    (0, "CADANT-CMTS-POLICY-MIB", "cadNameAclNumber"),
)
if mibBuilder.loadTexts:
    cadAclNameEntry.setStatus("current")


class _CadNameAclName_Type(SnmpAdminString):
    """Custom type cadNameAclName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CadNameAclName_Type.__name__ = "SnmpAdminString"
_CadNameAclName_Object = MibTableColumn
cadNameAclName = _CadNameAclName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 14, 1, 1),
    _CadNameAclName_Type()
)
cadNameAclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadNameAclName.setStatus("current")


class _CadNameAclNumber_Type(Integer32):
    """Custom type cadNameAclNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 399),
    )


_CadNameAclNumber_Type.__name__ = "Integer32"
_CadNameAclNumber_Object = MibTableColumn
cadNameAclNumber = _CadNameAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 14, 1, 2),
    _CadNameAclNumber_Type()
)
cadNameAclNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadNameAclNumber.setStatus("current")
_CadNameAclStatus_Type = RowStatus
_CadNameAclStatus_Object = MibTableColumn
cadNameAclStatus = _CadNameAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 14, 1, 3),
    _CadNameAclStatus_Type()
)
cadNameAclStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadNameAclStatus.setStatus("current")
_CadAclControl_ObjectIdentity = ObjectIdentity
cadAclControl = _CadAclControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 15)
)


class _CadAclOrderAcl_Type(TruthValue):
    """Custom type cadAclOrderAcl based on TruthValue"""


_CadAclOrderAcl_Object = MibScalar
cadAclOrderAcl = _CadAclOrderAcl_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 15, 1),
    _CadAclOrderAcl_Type()
)
cadAclOrderAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAclOrderAcl.setStatus("current")


class _CadAclOrderAclIndex_Type(Integer32):
    """Custom type cadAclOrderAclIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 399),
    )


_CadAclOrderAclIndex_Type.__name__ = "Integer32"
_CadAclOrderAclIndex_Object = MibScalar
cadAclOrderAclIndex = _CadAclOrderAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 15, 2),
    _CadAclOrderAclIndex_Type()
)
cadAclOrderAclIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAclOrderAclIndex.setStatus("current")


class _CadAclOrderAclInterval_Type(Integer32):
    """Custom type cadAclOrderAclInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CadAclOrderAclInterval_Type.__name__ = "Integer32"
_CadAclOrderAclInterval_Object = MibScalar
cadAclOrderAclInterval = _CadAclOrderAclInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 15, 3),
    _CadAclOrderAclInterval_Type()
)
cadAclOrderAclInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAclOrderAclInterval.setStatus("current")


class _CadAclOrderAclStart_Type(Integer32):
    """Custom type cadAclOrderAclStart based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CadAclOrderAclStart_Type.__name__ = "Integer32"
_CadAclOrderAclStart_Object = MibScalar
cadAclOrderAclStart = _CadAclOrderAclStart_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 15, 4),
    _CadAclOrderAclStart_Type()
)
cadAclOrderAclStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAclOrderAclStart.setStatus("current")


class _CadAclClearIpv4AclCounts_Type(Integer32):
    """Custom type cadAclClearIpv4AclCounts based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_CadAclClearIpv4AclCounts_Type.__name__ = "Integer32"
_CadAclClearIpv4AclCounts_Object = MibScalar
cadAclClearIpv4AclCounts = _CadAclClearIpv4AclCounts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 15, 5),
    _CadAclClearIpv4AclCounts_Type()
)
cadAclClearIpv4AclCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAclClearIpv4AclCounts.setStatus("current")


class _CadAclClearIpv6AclCounts_Type(Integer32):
    """Custom type cadAclClearIpv6AclCounts based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(200, 399),
    )


_CadAclClearIpv6AclCounts_Type.__name__ = "Integer32"
_CadAclClearIpv6AclCounts_Object = MibScalar
cadAclClearIpv6AclCounts = _CadAclClearIpv6AclCounts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 15, 6),
    _CadAclClearIpv6AclCounts_Type()
)
cadAclClearIpv6AclCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAclClearIpv6AclCounts.setStatus("current")
_CadPolicyAclExtTable_Object = MibTable
cadPolicyAclExtTable = _CadPolicyAclExtTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 16)
)
if mibBuilder.loadTexts:
    cadPolicyAclExtTable.setStatus("current")
_CadPolicyAclExtEntry_Object = MibTableRow
cadPolicyAclExtEntry = _CadPolicyAclExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 16, 1)
)
if mibBuilder.loadTexts:
    cadPolicyAclExtEntry.setStatus("current")
_CadAclEntryCount_Type = Counter64
_CadAclEntryCount_Object = MibTableColumn
cadAclEntryCount = _CadAclEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 16, 1, 1),
    _CadAclEntryCount_Type()
)
cadAclEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadAclEntryCount.setStatus("current")
_CadPolicyRouting_ObjectIdentity = ObjectIdentity
cadPolicyRouting = _CadPolicyRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30)
)
_CadRouteMapTagTable_Object = MibTable
cadRouteMapTagTable = _CadRouteMapTagTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 1)
)
if mibBuilder.loadTexts:
    cadRouteMapTagTable.setStatus("current")
_CadRouteMapTagEntry_Object = MibTableRow
cadRouteMapTagEntry = _CadRouteMapTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 1, 1)
)
cadRouteMapTagEntry.setIndexNames(
    (0, "CADANT-CMTS-POLICY-MIB", "cadRouteMapTagName"),
)
if mibBuilder.loadTexts:
    cadRouteMapTagEntry.setStatus("current")


class _CadRouteMapTagName_Type(SnmpAdminString):
    """Custom type cadRouteMapTagName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CadRouteMapTagName_Type.__name__ = "SnmpAdminString"
_CadRouteMapTagName_Object = MibTableColumn
cadRouteMapTagName = _CadRouteMapTagName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 1, 1, 1),
    _CadRouteMapTagName_Type()
)
cadRouteMapTagName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadRouteMapTagName.setStatus("current")


class _CadRouteMapTagId_Type(Integer32):
    """Custom type cadRouteMapTagId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CadRouteMapTagId_Type.__name__ = "Integer32"
_CadRouteMapTagId_Object = MibTableColumn
cadRouteMapTagId = _CadRouteMapTagId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 1, 1, 2),
    _CadRouteMapTagId_Type()
)
cadRouteMapTagId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadRouteMapTagId.setStatus("current")
_CadRouteMapTagRowStatus_Type = RowStatus
_CadRouteMapTagRowStatus_Object = MibTableColumn
cadRouteMapTagRowStatus = _CadRouteMapTagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 1, 1, 3),
    _CadRouteMapTagRowStatus_Type()
)
cadRouteMapTagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadRouteMapTagRowStatus.setStatus("current")
_CadRouteMapTable_Object = MibTable
cadRouteMapTable = _CadRouteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 2)
)
if mibBuilder.loadTexts:
    cadRouteMapTable.setStatus("current")
_CadRouteMapEntry_Object = MibTableRow
cadRouteMapEntry = _CadRouteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 2, 1)
)
cadRouteMapEntry.setIndexNames(
    (0, "CADANT-CMTS-POLICY-MIB", "cadRouteMapId"),
    (0, "CADANT-CMTS-POLICY-MIB", "cadRouteMapSeqNum"),
)
if mibBuilder.loadTexts:
    cadRouteMapEntry.setStatus("current")


class _CadRouteMapId_Type(Integer32):
    """Custom type cadRouteMapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CadRouteMapId_Type.__name__ = "Integer32"
_CadRouteMapId_Object = MibTableColumn
cadRouteMapId = _CadRouteMapId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 2, 1, 1),
    _CadRouteMapId_Type()
)
cadRouteMapId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadRouteMapId.setStatus("current")


class _CadRouteMapSeqNum_Type(Integer32):
    """Custom type cadRouteMapSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CadRouteMapSeqNum_Type.__name__ = "Integer32"
_CadRouteMapSeqNum_Object = MibTableColumn
cadRouteMapSeqNum = _CadRouteMapSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 2, 1, 2),
    _CadRouteMapSeqNum_Type()
)
cadRouteMapSeqNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadRouteMapSeqNum.setStatus("current")


class _CadRouteMapMatchType_Type(Integer32):
    """Custom type cadRouteMapMatchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_CadRouteMapMatchType_Type.__name__ = "Integer32"
_CadRouteMapMatchType_Object = MibTableColumn
cadRouteMapMatchType = _CadRouteMapMatchType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 2, 1, 3),
    _CadRouteMapMatchType_Type()
)
cadRouteMapMatchType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadRouteMapMatchType.setStatus("current")


class _CadRouteMapMatchAcl_Type(Integer32):
    """Custom type cadRouteMapMatchAcl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_CadRouteMapMatchAcl_Type.__name__ = "Integer32"
_CadRouteMapMatchAcl_Object = MibTableColumn
cadRouteMapMatchAcl = _CadRouteMapMatchAcl_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 2, 1, 4),
    _CadRouteMapMatchAcl_Type()
)
cadRouteMapMatchAcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadRouteMapMatchAcl.setStatus("current")


class _CadRouteMapSetIpPrec_Type(TruthValue):
    """Custom type cadRouteMapSetIpPrec based on TruthValue"""


_CadRouteMapSetIpPrec_Object = MibTableColumn
cadRouteMapSetIpPrec = _CadRouteMapSetIpPrec_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 2, 1, 5),
    _CadRouteMapSetIpPrec_Type()
)
cadRouteMapSetIpPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadRouteMapSetIpPrec.setStatus("current")


class _CadRouteMapIpPrec_Type(Integer32):
    """Custom type cadRouteMapIpPrec based on Integer32"""
    defaultValue = 0

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
              7)
        )
    )
    namedValues = NamedValues(
        *(("critical", 5),
          ("flash", 3),
          ("flash-override", 4),
          ("immediate", 2),
          ("internet", 6),
          ("network", 7),
          ("priority", 1),
          ("routine", 0))
    )


_CadRouteMapIpPrec_Type.__name__ = "Integer32"
_CadRouteMapIpPrec_Object = MibTableColumn
cadRouteMapIpPrec = _CadRouteMapIpPrec_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 2, 1, 6),
    _CadRouteMapIpPrec_Type()
)
cadRouteMapIpPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadRouteMapIpPrec.setStatus("current")


class _CadRouteMapSetIpTos_Type(TruthValue):
    """Custom type cadRouteMapSetIpTos based on TruthValue"""


_CadRouteMapSetIpTos_Object = MibTableColumn
cadRouteMapSetIpTos = _CadRouteMapSetIpTos_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 2, 1, 7),
    _CadRouteMapSetIpTos_Type()
)
cadRouteMapSetIpTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadRouteMapSetIpTos.setStatus("current")


class _CadRouteMapIpTos_Type(Integer32):
    """Custom type cadRouteMapIpTos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("max-reliability", 2),
          ("max-throughput", 4),
          ("min-delay", 8),
          ("min-monetary-cost", 1),
          ("normal", 0))
    )


_CadRouteMapIpTos_Type.__name__ = "Integer32"
_CadRouteMapIpTos_Object = MibTableColumn
cadRouteMapIpTos = _CadRouteMapIpTos_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 2, 1, 8),
    _CadRouteMapIpTos_Type()
)
cadRouteMapIpTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadRouteMapIpTos.setStatus("current")


class _CadRouteMapSetNextHop_Type(TruthValue):
    """Custom type cadRouteMapSetNextHop based on TruthValue"""


_CadRouteMapSetNextHop_Object = MibTableColumn
cadRouteMapSetNextHop = _CadRouteMapSetNextHop_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 2, 1, 9),
    _CadRouteMapSetNextHop_Type()
)
cadRouteMapSetNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadRouteMapSetNextHop.setStatus("current")


class _CadRouteMapNextHopAddrType_Type(InetAddressType):
    """Custom type cadRouteMapNextHopAddrType based on InetAddressType"""


_CadRouteMapNextHopAddrType_Object = MibTableColumn
cadRouteMapNextHopAddrType = _CadRouteMapNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 2, 1, 10),
    _CadRouteMapNextHopAddrType_Type()
)
cadRouteMapNextHopAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadRouteMapNextHopAddrType.setStatus("current")


class _CadRouteMapNextHop_Type(InetAddress):
    """Custom type cadRouteMapNextHop based on InetAddress"""
    defaultHexValue = ""


_CadRouteMapNextHop_Object = MibTableColumn
cadRouteMapNextHop = _CadRouteMapNextHop_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 2, 1, 11),
    _CadRouteMapNextHop_Type()
)
cadRouteMapNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadRouteMapNextHop.setStatus("current")


class _CadRouteMapSetBackupNextHop_Type(TruthValue):
    """Custom type cadRouteMapSetBackupNextHop based on TruthValue"""


_CadRouteMapSetBackupNextHop_Object = MibTableColumn
cadRouteMapSetBackupNextHop = _CadRouteMapSetBackupNextHop_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 2, 1, 12),
    _CadRouteMapSetBackupNextHop_Type()
)
cadRouteMapSetBackupNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadRouteMapSetBackupNextHop.setStatus("current")


class _CadRouteMapBackupNextHop_Type(InetAddress):
    """Custom type cadRouteMapBackupNextHop based on InetAddress"""
    defaultHexValue = ""


_CadRouteMapBackupNextHop_Object = MibTableColumn
cadRouteMapBackupNextHop = _CadRouteMapBackupNextHop_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 2, 1, 13),
    _CadRouteMapBackupNextHop_Type()
)
cadRouteMapBackupNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadRouteMapBackupNextHop.setStatus("current")


class _CadRouteMapSetNullInterface_Type(TruthValue):
    """Custom type cadRouteMapSetNullInterface based on TruthValue"""


_CadRouteMapSetNullInterface_Object = MibTableColumn
cadRouteMapSetNullInterface = _CadRouteMapSetNullInterface_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 2, 1, 14),
    _CadRouteMapSetNullInterface_Type()
)
cadRouteMapSetNullInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadRouteMapSetNullInterface.setStatus("current")
_CadRouteMapRowStatus_Type = RowStatus
_CadRouteMapRowStatus_Object = MibTableColumn
cadRouteMapRowStatus = _CadRouteMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 2, 1, 15),
    _CadRouteMapRowStatus_Type()
)
cadRouteMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadRouteMapRowStatus.setStatus("current")


class _CadRouteMapSetIpDscp_Type(TruthValue):
    """Custom type cadRouteMapSetIpDscp based on TruthValue"""


_CadRouteMapSetIpDscp_Object = MibTableColumn
cadRouteMapSetIpDscp = _CadRouteMapSetIpDscp_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 2, 1, 16),
    _CadRouteMapSetIpDscp_Type()
)
cadRouteMapSetIpDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadRouteMapSetIpDscp.setStatus("current")


class _CadRouteMapIpDscp_Type(Integer32):
    """Custom type cadRouteMapIpDscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CadRouteMapIpDscp_Type.__name__ = "Integer32"
_CadRouteMapIpDscp_Object = MibTableColumn
cadRouteMapIpDscp = _CadRouteMapIpDscp_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 2, 1, 17),
    _CadRouteMapIpDscp_Type()
)
cadRouteMapIpDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadRouteMapIpDscp.setStatus("current")


class _CadRouteMapSetRecursiveNextHop_Type(TruthValue):
    """Custom type cadRouteMapSetRecursiveNextHop based on TruthValue"""


_CadRouteMapSetRecursiveNextHop_Object = MibTableColumn
cadRouteMapSetRecursiveNextHop = _CadRouteMapSetRecursiveNextHop_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 2, 1, 18),
    _CadRouteMapSetRecursiveNextHop_Type()
)
cadRouteMapSetRecursiveNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadRouteMapSetRecursiveNextHop.setStatus("current")


class _CadRouteMapRecursiveNextHop_Type(InetAddress):
    """Custom type cadRouteMapRecursiveNextHop based on InetAddress"""
    defaultHexValue = ""


_CadRouteMapRecursiveNextHop_Object = MibTableColumn
cadRouteMapRecursiveNextHop = _CadRouteMapRecursiveNextHop_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 2, 1, 19),
    _CadRouteMapRecursiveNextHop_Type()
)
cadRouteMapRecursiveNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadRouteMapRecursiveNextHop.setStatus("current")
_CadRouteMapStatsTable_Object = MibTable
cadRouteMapStatsTable = _CadRouteMapStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 3)
)
if mibBuilder.loadTexts:
    cadRouteMapStatsTable.setStatus("current")
_CadRouteMapStatsEntry_Object = MibTableRow
cadRouteMapStatsEntry = _CadRouteMapStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 3, 1)
)
cadRouteMapStatsEntry.setIndexNames(
    (0, "CADANT-CMTS-POLICY-MIB", "cadRouteMapId"),
    (0, "CADANT-CMTS-POLICY-MIB", "cadRouteMapSeqNum"),
)
if mibBuilder.loadTexts:
    cadRouteMapStatsEntry.setStatus("current")
_CadRouteMapPktMatched_Type = Counter32
_CadRouteMapPktMatched_Object = MibTableColumn
cadRouteMapPktMatched = _CadRouteMapPktMatched_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 3, 1, 1),
    _CadRouteMapPktMatched_Type()
)
cadRouteMapPktMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadRouteMapPktMatched.setStatus("current")
_CadRouteMapByteMatched_Type = Counter64
_CadRouteMapByteMatched_Object = MibTableColumn
cadRouteMapByteMatched = _CadRouteMapByteMatched_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 3, 1, 2),
    _CadRouteMapByteMatched_Type()
)
cadRouteMapByteMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadRouteMapByteMatched.setStatus("current")
_CadRouteMapPktFailed_Type = Counter32
_CadRouteMapPktFailed_Object = MibTableColumn
cadRouteMapPktFailed = _CadRouteMapPktFailed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 3, 1, 3),
    _CadRouteMapPktFailed_Type()
)
cadRouteMapPktFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadRouteMapPktFailed.setStatus("current")
_CadRouteMapByteFailed_Type = Counter64
_CadRouteMapByteFailed_Object = MibTableColumn
cadRouteMapByteFailed = _CadRouteMapByteFailed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 3, 1, 4),
    _CadRouteMapByteFailed_Type()
)
cadRouteMapByteFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadRouteMapByteFailed.setStatus("current")


class _CadRouteMapClearStats_Type(Integer32):
    """Custom type cadRouteMapClearStats based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_CadRouteMapClearStats_Type.__name__ = "Integer32"
_CadRouteMapClearStats_Object = MibScalar
cadRouteMapClearStats = _CadRouteMapClearStats_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 4),
    _CadRouteMapClearStats_Type()
)
cadRouteMapClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadRouteMapClearStats.setStatus("current")


class _CadLocalPolicyRouteMap_Type(Integer32):
    """Custom type cadLocalPolicyRouteMap based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_CadLocalPolicyRouteMap_Type.__name__ = "Integer32"
_CadLocalPolicyRouteMap_Object = MibScalar
cadLocalPolicyRouteMap = _CadLocalPolicyRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35, 1, 30, 5),
    _CadLocalPolicyRouteMap_Type()
)
cadLocalPolicyRouteMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadLocalPolicyRouteMap.setStatus("current")
cadPolicyRateLimitEntry.registerAugmentions(
    ("CADANT-CMTS-POLICY-MIB",
     "cadPolicyRateLimitStatusEntry")
)
cadPolicyRateLimitStatusEntry.setIndexNames(*cadPolicyRateLimitEntry.getIndexNames())
cadPolicyAccessGroupEntry.registerAugmentions(
    ("CADANT-CMTS-POLICY-MIB",
     "cadPolicyAccessGroupStatusEntry")
)
cadPolicyAccessGroupStatusEntry.setIndexNames(*cadPolicyAccessGroupEntry.getIndexNames())
cadPolicyAclEntry.registerAugmentions(
    ("CADANT-CMTS-POLICY-MIB",
     "cadPolicyAclExtEntry")
)
cadPolicyAclExtEntry.setIndexNames(*cadPolicyAclEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-CMTS-POLICY-MIB",
    **{"CadPolicyRateLimitAction": CadPolicyRateLimitAction,
       "CadPolicyAction": CadPolicyAction,
       "CadPolicyProtocol": CadPolicyProtocol,
       "cadPolicyMib": cadPolicyMib,
       "cadScmAccessTable": cadScmAccessTable,
       "cadScmAccessEntry": cadScmAccessEntry,
       "cadScmAccIfIndex": cadScmAccIfIndex,
       "cadScmAccListNumber": cadScmAccListNumber,
       "cadScmAccRowStatus": cadScmAccRowStatus,
       "cadDistListInTable": cadDistListInTable,
       "cadDistListInEntry": cadDistListInEntry,
       "cadDistListInProtocol": cadDistListInProtocol,
       "cadDistListInProtocolProcess": cadDistListInProtocolProcess,
       "cadDistListInIfIndex": cadDistListInIfIndex,
       "cadDistListInAccessListNum": cadDistListInAccessListNum,
       "cadDistListInAccessListName": cadDistListInAccessListName,
       "cadDistListInStatus": cadDistListInStatus,
       "cadPolicyRateLimitTable": cadPolicyRateLimitTable,
       "cadPolicyRateLimitEntry": cadPolicyRateLimitEntry,
       "cadPolicyRateLimitIfIndex": cadPolicyRateLimitIfIndex,
       "cadPolicyRateLimitDirection": cadPolicyRateLimitDirection,
       "cadPolicyRateLimitIndex": cadPolicyRateLimitIndex,
       "cadPolicyRateLimitStatus": cadPolicyRateLimitStatus,
       "cadPolicyRateLimitAclType": cadPolicyRateLimitAclType,
       "cadPolicyRateLimitAclNum": cadPolicyRateLimitAclNum,
       "cadPolicyRateLimitBps": cadPolicyRateLimitBps,
       "cadPolicyRateLimitBurstNormal": cadPolicyRateLimitBurstNormal,
       "cadPolicyRateLimitBurstMax": cadPolicyRateLimitBurstMax,
       "cadPolicyRateLimitConformAction": cadPolicyRateLimitConformAction,
       "cadPolicyRateLimitConformValue": cadPolicyRateLimitConformValue,
       "cadPolicyRateLimitExceedAction": cadPolicyRateLimitExceedAction,
       "cadPolicyRateLimitExceedValue": cadPolicyRateLimitExceedValue,
       "cadPolicyRateLimitClearCounts": cadPolicyRateLimitClearCounts,
       "cadPolicyRateLimitStatusTable": cadPolicyRateLimitStatusTable,
       "cadPolicyRateLimitStatusEntry": cadPolicyRateLimitStatusEntry,
       "cadPolicyRateLimitConformPackets": cadPolicyRateLimitConformPackets,
       "cadPolicyRateLimitConformBytes": cadPolicyRateLimitConformBytes,
       "cadPolicyRateLimitExceedPackets": cadPolicyRateLimitExceedPackets,
       "cadPolicyRateLimitExceedBytes": cadPolicyRateLimitExceedBytes,
       "cadPolicyRateLimitCurrentBurst": cadPolicyRateLimitCurrentBurst,
       "cadPolicyRateLimitLastCleared": cadPolicyRateLimitLastCleared,
       "cadPolicyAclTable": cadPolicyAclTable,
       "cadPolicyAclEntry": cadPolicyAclEntry,
       "cadAclNumber": cadAclNumber,
       "cadAclIndex": cadAclIndex,
       "cadAclType": cadAclType,
       "cadAclStatus": cadAclStatus,
       "cadAclPermit": cadAclPermit,
       "cadAclProtocol": cadAclProtocol,
       "cadAclSrcIp": cadAclSrcIp,
       "cadAclSrcIpMask": cadAclSrcIpMask,
       "cadAclSrcPortOp": cadAclSrcPortOp,
       "cadAclSrcPortLo": cadAclSrcPortLo,
       "cadAclSrcPortHi": cadAclSrcPortHi,
       "cadAclDstIp": cadAclDstIp,
       "cadAclDstIpMask": cadAclDstIpMask,
       "cadAclDstPortOp": cadAclDstPortOp,
       "cadAclDstPortLo": cadAclDstPortLo,
       "cadAclDstPortHi": cadAclDstPortHi,
       "cadAclLogging": cadAclLogging,
       "cadAclProtoType": cadAclProtoType,
       "cadAclProtoCode": cadAclProtoCode,
       "cadAclIpTos": cadAclIpTos,
       "cadAclIpTosMask": cadAclIpTosMask,
       "cadAclTcpFlags": cadAclTcpFlags,
       "cadAclTcpFlagsMask": cadAclTcpFlagsMask,
       "cadAclFragments": cadAclFragments,
       "cadAclRemark": cadAclRemark,
       "cadAclIpAddrType": cadAclIpAddrType,
       "cadSnmpCommAccessTable": cadSnmpCommAccessTable,
       "cadSnmpCommAccessEntry": cadSnmpCommAccessEntry,
       "cadSnmpCommAccessName": cadSnmpCommAccessName,
       "cadSnmpCommAccessList": cadSnmpCommAccessList,
       "cadSnmpCommAccessStatus": cadSnmpCommAccessStatus,
       "cadPolicyAccessGroupTable": cadPolicyAccessGroupTable,
       "cadPolicyAccessGroupEntry": cadPolicyAccessGroupEntry,
       "cadPolicyAccessGroupIfIndex": cadPolicyAccessGroupIfIndex,
       "cadPolicyAccessGroupDirection": cadPolicyAccessGroupDirection,
       "cadPolicyAccessGroupStatus": cadPolicyAccessGroupStatus,
       "cadPolicyAccessGroupIpv4AclNum": cadPolicyAccessGroupIpv4AclNum,
       "cadPolicyAccessGroupClearCounts": cadPolicyAccessGroupClearCounts,
       "cadPolicyAccessGroupIpv6AclNum": cadPolicyAccessGroupIpv6AclNum,
       "cadPolicyAccessGroupIpv6AclName": cadPolicyAccessGroupIpv6AclName,
       "cadPolicyAccessGroupStatusTable": cadPolicyAccessGroupStatusTable,
       "cadPolicyAccessGroupStatusEntry": cadPolicyAccessGroupStatusEntry,
       "cadPolicyAccessGroupPermitPackets": cadPolicyAccessGroupPermitPackets,
       "cadPolicyAccessGroupDenyPackets": cadPolicyAccessGroupDenyPackets,
       "cadPolicyAccessGroupLastCleared": cadPolicyAccessGroupLastCleared,
       "cadPolicyPfxListTable": cadPolicyPfxListTable,
       "cadPolicyPfxListEntry": cadPolicyPfxListEntry,
       "cadPolicyPfxListNumber": cadPolicyPfxListNumber,
       "cadPolicyPfxListName": cadPolicyPfxListName,
       "cadPolicyPfxListSeqNumber": cadPolicyPfxListSeqNumber,
       "cadPolicyPfxListIpAddress": cadPolicyPfxListIpAddress,
       "cadPolicyPfxListIpAddMaskLen": cadPolicyPfxListIpAddMaskLen,
       "cadPolicyPfxListMaskGeValue": cadPolicyPfxListMaskGeValue,
       "cadPolicyPfxListMaskLeValue": cadPolicyPfxListMaskLeValue,
       "cadPolicyPfxListAction": cadPolicyPfxListAction,
       "cadPolicyPfxListStatus": cadPolicyPfxListStatus,
       "cadPolicyPfxListAfi": cadPolicyPfxListAfi,
       "cadPolicyPfxListSafi": cadPolicyPfxListSafi,
       "cadPolicyDistListOutTable": cadPolicyDistListOutTable,
       "cadPolicyDistListOutEntry": cadPolicyDistListOutEntry,
       "cadPolicyDistListOutSrcProtocol": cadPolicyDistListOutSrcProtocol,
       "cadPolicyDistListOutSrcProtocolProcess": cadPolicyDistListOutSrcProtocolProcess,
       "cadPolicyDistListOutRoutingProtocol": cadPolicyDistListOutRoutingProtocol,
       "cadPolicyDistListOutRoutingProcess": cadPolicyDistListOutRoutingProcess,
       "cadPolicyDistListOutAutonomousSystemNum": cadPolicyDistListOutAutonomousSystemNum,
       "cadPolicyDistListOutAccessListNum": cadPolicyDistListOutAccessListNum,
       "cadPolicyDistListOutAccessListName": cadPolicyDistListOutAccessListName,
       "cadPolicyDistListOutStatus": cadPolicyDistListOutStatus,
       "cadPolicyDistListOutIfIndex": cadPolicyDistListOutIfIndex,
       "cadDistListOutTable": cadDistListOutTable,
       "cadDistListOutEntry": cadDistListOutEntry,
       "cadDistListOutVrIndex": cadDistListOutVrIndex,
       "cadDistListOutDestProtocol": cadDistListOutDestProtocol,
       "cadDistListOutSrcProtocol": cadDistListOutSrcProtocol,
       "cadDistListOutAccessListNum": cadDistListOutAccessListNum,
       "cadDistListOutStatus": cadDistListOutStatus,
       "cadDistListOutAccessListName": cadDistListOutAccessListName,
       "cadAclNameTable": cadAclNameTable,
       "cadAclNameEntry": cadAclNameEntry,
       "cadNameAclName": cadNameAclName,
       "cadNameAclNumber": cadNameAclNumber,
       "cadNameAclStatus": cadNameAclStatus,
       "cadAclControl": cadAclControl,
       "cadAclOrderAcl": cadAclOrderAcl,
       "cadAclOrderAclIndex": cadAclOrderAclIndex,
       "cadAclOrderAclInterval": cadAclOrderAclInterval,
       "cadAclOrderAclStart": cadAclOrderAclStart,
       "cadAclClearIpv4AclCounts": cadAclClearIpv4AclCounts,
       "cadAclClearIpv6AclCounts": cadAclClearIpv6AclCounts,
       "cadPolicyAclExtTable": cadPolicyAclExtTable,
       "cadPolicyAclExtEntry": cadPolicyAclExtEntry,
       "cadAclEntryCount": cadAclEntryCount,
       "cadPolicyRouting": cadPolicyRouting,
       "cadRouteMapTagTable": cadRouteMapTagTable,
       "cadRouteMapTagEntry": cadRouteMapTagEntry,
       "cadRouteMapTagName": cadRouteMapTagName,
       "cadRouteMapTagId": cadRouteMapTagId,
       "cadRouteMapTagRowStatus": cadRouteMapTagRowStatus,
       "cadRouteMapTable": cadRouteMapTable,
       "cadRouteMapEntry": cadRouteMapEntry,
       "cadRouteMapId": cadRouteMapId,
       "cadRouteMapSeqNum": cadRouteMapSeqNum,
       "cadRouteMapMatchType": cadRouteMapMatchType,
       "cadRouteMapMatchAcl": cadRouteMapMatchAcl,
       "cadRouteMapSetIpPrec": cadRouteMapSetIpPrec,
       "cadRouteMapIpPrec": cadRouteMapIpPrec,
       "cadRouteMapSetIpTos": cadRouteMapSetIpTos,
       "cadRouteMapIpTos": cadRouteMapIpTos,
       "cadRouteMapSetNextHop": cadRouteMapSetNextHop,
       "cadRouteMapNextHopAddrType": cadRouteMapNextHopAddrType,
       "cadRouteMapNextHop": cadRouteMapNextHop,
       "cadRouteMapSetBackupNextHop": cadRouteMapSetBackupNextHop,
       "cadRouteMapBackupNextHop": cadRouteMapBackupNextHop,
       "cadRouteMapSetNullInterface": cadRouteMapSetNullInterface,
       "cadRouteMapRowStatus": cadRouteMapRowStatus,
       "cadRouteMapSetIpDscp": cadRouteMapSetIpDscp,
       "cadRouteMapIpDscp": cadRouteMapIpDscp,
       "cadRouteMapSetRecursiveNextHop": cadRouteMapSetRecursiveNextHop,
       "cadRouteMapRecursiveNextHop": cadRouteMapRecursiveNextHop,
       "cadRouteMapStatsTable": cadRouteMapStatsTable,
       "cadRouteMapStatsEntry": cadRouteMapStatsEntry,
       "cadRouteMapPktMatched": cadRouteMapPktMatched,
       "cadRouteMapByteMatched": cadRouteMapByteMatched,
       "cadRouteMapPktFailed": cadRouteMapPktFailed,
       "cadRouteMapByteFailed": cadRouteMapByteFailed,
       "cadRouteMapClearStats": cadRouteMapClearStats,
       "cadLocalPolicyRouteMap": cadLocalPolicyRouteMap}
)
