# SNMP MIB module (IP-ACCESS-LIST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IP-ACCESS-LIST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:31 2024
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

(cjnMgmt,) = mibBuilder.importSymbols(
    "Cajun-ROOT",
    "cjnMgmt")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cjnIpAListMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpACListCtlTable_Object = MibTable
ipACListCtlTable = _IpACListCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 5, 1)
)
if mibBuilder.loadTexts:
    ipACListCtlTable.setStatus("current")
_IpACListCtlEntry_Object = MibTableRow
ipACListCtlEntry = _IpACListCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 5, 1, 1)
)
ipACListCtlEntry.setIndexNames(
    (0, "IP-ACCESS-LIST-MIB", "ipACListCtlName"),
)
if mibBuilder.loadTexts:
    ipACListCtlEntry.setStatus("current")


class _IpACListCtlName_Type(OctetString):
    """Custom type ipACListCtlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_IpACListCtlName_Type.__name__ = "OctetString"
_IpACListCtlName_Object = MibTableColumn
ipACListCtlName = _IpACListCtlName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 5, 1, 1, 1),
    _IpACListCtlName_Type()
)
ipACListCtlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipACListCtlName.setStatus("current")


class _IpACListCtlType_Type(Integer32):
    """Custom type ipACListCtlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_IpACListCtlType_Type.__name__ = "Integer32"
_IpACListCtlType_Object = MibTableColumn
ipACListCtlType = _IpACListCtlType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 5, 1, 1, 2),
    _IpACListCtlType_Type()
)
ipACListCtlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipACListCtlType.setStatus("current")
_IpACListCtlStatus_Type = RowStatus
_IpACListCtlStatus_Object = MibTableColumn
ipACListCtlStatus = _IpACListCtlStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 5, 1, 1, 3),
    _IpACListCtlStatus_Type()
)
ipACListCtlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipACListCtlStatus.setStatus("current")
_IpACRuleTable_Object = MibTable
ipACRuleTable = _IpACRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 5, 2)
)
if mibBuilder.loadTexts:
    ipACRuleTable.setStatus("current")
_IpACRuleEntry_Object = MibTableRow
ipACRuleEntry = _IpACRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 5, 2, 1)
)
ipACRuleEntry.setIndexNames(
    (0, "IP-ACCESS-LIST-MIB", "ipACRuleName"),
    (0, "IP-ACCESS-LIST-MIB", "ipACRuleSubIndex"),
)
if mibBuilder.loadTexts:
    ipACRuleEntry.setStatus("current")


class _IpACRuleName_Type(OctetString):
    """Custom type ipACRuleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_IpACRuleName_Type.__name__ = "OctetString"
_IpACRuleName_Object = MibTableColumn
ipACRuleName = _IpACRuleName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 5, 2, 1, 1),
    _IpACRuleName_Type()
)
ipACRuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipACRuleName.setStatus("current")


class _IpACRuleSubIndex_Type(Integer32):
    """Custom type ipACRuleSubIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_IpACRuleSubIndex_Type.__name__ = "Integer32"
_IpACRuleSubIndex_Object = MibTableColumn
ipACRuleSubIndex = _IpACRuleSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 5, 2, 1, 2),
    _IpACRuleSubIndex_Type()
)
ipACRuleSubIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipACRuleSubIndex.setStatus("current")


class _IpACRuleOwner_Type(Integer32):
    """Custom type ipACRuleOwner based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("local", 1))
    )


_IpACRuleOwner_Type.__name__ = "Integer32"
_IpACRuleOwner_Object = MibTableColumn
ipACRuleOwner = _IpACRuleOwner_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 5, 2, 1, 3),
    _IpACRuleOwner_Type()
)
ipACRuleOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipACRuleOwner.setStatus("current")
_IpACRuleSrcAddr_Type = IpAddress
_IpACRuleSrcAddr_Object = MibTableColumn
ipACRuleSrcAddr = _IpACRuleSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 5, 2, 1, 4),
    _IpACRuleSrcAddr_Type()
)
ipACRuleSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipACRuleSrcAddr.setStatus("current")
_IpACRuleSrcAddrWild_Type = IpAddress
_IpACRuleSrcAddrWild_Object = MibTableColumn
ipACRuleSrcAddrWild = _IpACRuleSrcAddrWild_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 5, 2, 1, 5),
    _IpACRuleSrcAddrWild_Type()
)
ipACRuleSrcAddrWild.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipACRuleSrcAddrWild.setStatus("current")
_IpACRuleSrcMask_Type = IpAddress
_IpACRuleSrcMask_Object = MibTableColumn
ipACRuleSrcMask = _IpACRuleSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 5, 2, 1, 6),
    _IpACRuleSrcMask_Type()
)
ipACRuleSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipACRuleSrcMask.setStatus("current")
_IpACRuleSrcMaskWild_Type = IpAddress
_IpACRuleSrcMaskWild_Object = MibTableColumn
ipACRuleSrcMaskWild = _IpACRuleSrcMaskWild_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 5, 2, 1, 7),
    _IpACRuleSrcMaskWild_Type()
)
ipACRuleSrcMaskWild.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipACRuleSrcMaskWild.setStatus("current")
_IpACRuleDstAddr_Type = IpAddress
_IpACRuleDstAddr_Object = MibTableColumn
ipACRuleDstAddr = _IpACRuleDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 5, 2, 1, 8),
    _IpACRuleDstAddr_Type()
)
ipACRuleDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipACRuleDstAddr.setStatus("current")
_IpACRuleDstAddrWild_Type = IpAddress
_IpACRuleDstAddrWild_Object = MibTableColumn
ipACRuleDstAddrWild = _IpACRuleDstAddrWild_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 5, 2, 1, 9),
    _IpACRuleDstAddrWild_Type()
)
ipACRuleDstAddrWild.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipACRuleDstAddrWild.setStatus("current")
_IpACRuleDstMask_Type = IpAddress
_IpACRuleDstMask_Object = MibTableColumn
ipACRuleDstMask = _IpACRuleDstMask_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 5, 2, 1, 10),
    _IpACRuleDstMask_Type()
)
ipACRuleDstMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipACRuleDstMask.setStatus("current")
_IpACRuleDstMaskWild_Type = IpAddress
_IpACRuleDstMaskWild_Object = MibTableColumn
ipACRuleDstMaskWild = _IpACRuleDstMaskWild_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 5, 2, 1, 11),
    _IpACRuleDstMaskWild_Type()
)
ipACRuleDstMaskWild.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipACRuleDstMaskWild.setStatus("current")


class _IpACRuleOperation_Type(Integer32):
    """Custom type ipACRuleOperation based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("forwardNoChange", 10),
          ("forwardPriority1", 2),
          ("forwardPriority2", 3),
          ("forwardPriority3", 4),
          ("forwardPriority4", 5),
          ("forwardPriority5", 6),
          ("forwardPriority6", 7),
          ("forwardPriority7", 8),
          ("forwardPriority8", 9))
    )


_IpACRuleOperation_Type.__name__ = "Integer32"
_IpACRuleOperation_Object = MibTableColumn
ipACRuleOperation = _IpACRuleOperation_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 5, 2, 1, 12),
    _IpACRuleOperation_Type()
)
ipACRuleOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipACRuleOperation.setStatus("current")


class _IpACRuleProtocol_Type(Integer32):
    """Custom type ipACRuleProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65537),
    )


_IpACRuleProtocol_Type.__name__ = "Integer32"
_IpACRuleProtocol_Object = MibTableColumn
ipACRuleProtocol = _IpACRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 5, 2, 1, 13),
    _IpACRuleProtocol_Type()
)
ipACRuleProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipACRuleProtocol.setStatus("current")


class _IpACRuleL4SrcPortMin_Type(Integer32):
    """Custom type ipACRuleL4SrcPortMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_IpACRuleL4SrcPortMin_Type.__name__ = "Integer32"
_IpACRuleL4SrcPortMin_Object = MibTableColumn
ipACRuleL4SrcPortMin = _IpACRuleL4SrcPortMin_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 5, 2, 1, 14),
    _IpACRuleL4SrcPortMin_Type()
)
ipACRuleL4SrcPortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipACRuleL4SrcPortMin.setStatus("current")


class _IpACRuleL4SrcPortMax_Type(Integer32):
    """Custom type ipACRuleL4SrcPortMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_IpACRuleL4SrcPortMax_Type.__name__ = "Integer32"
_IpACRuleL4SrcPortMax_Object = MibTableColumn
ipACRuleL4SrcPortMax = _IpACRuleL4SrcPortMax_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 5, 2, 1, 15),
    _IpACRuleL4SrcPortMax_Type()
)
ipACRuleL4SrcPortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipACRuleL4SrcPortMax.setStatus("current")


class _IpACRuleL4DestPortMin_Type(Integer32):
    """Custom type ipACRuleL4DestPortMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_IpACRuleL4DestPortMin_Type.__name__ = "Integer32"
_IpACRuleL4DestPortMin_Object = MibTableColumn
ipACRuleL4DestPortMin = _IpACRuleL4DestPortMin_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 5, 2, 1, 16),
    _IpACRuleL4DestPortMin_Type()
)
ipACRuleL4DestPortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipACRuleL4DestPortMin.setStatus("current")


class _IpACRuleL4DestPortMax_Type(Integer32):
    """Custom type ipACRuleL4DestPortMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_IpACRuleL4DestPortMax_Type.__name__ = "Integer32"
_IpACRuleL4DestPortMax_Object = MibTableColumn
ipACRuleL4DestPortMax = _IpACRuleL4DestPortMax_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 5, 2, 1, 17),
    _IpACRuleL4DestPortMax_Type()
)
ipACRuleL4DestPortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipACRuleL4DestPortMax.setStatus("current")
_IpACRuleStatus_Type = RowStatus
_IpACRuleStatus_Object = MibTableColumn
ipACRuleStatus = _IpACRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 5, 2, 1, 18),
    _IpACRuleStatus_Type()
)
ipACRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipACRuleStatus.setStatus("current")


class _IpACRuleEstablished_Type(TruthValue):
    """Custom type ipACRuleEstablished based on TruthValue"""


_IpACRuleEstablished_Object = MibTableColumn
ipACRuleEstablished = _IpACRuleEstablished_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 5, 2, 1, 19),
    _IpACRuleEstablished_Type()
)
ipACRuleEstablished.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipACRuleEstablished.setStatus("current")


class _IpACRuleLog_Type(TruthValue):
    """Custom type ipACRuleLog based on TruthValue"""


_IpACRuleLog_Object = MibTableColumn
ipACRuleLog = _IpACRuleLog_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 5, 2, 1, 20),
    _IpACRuleLog_Type()
)
ipACRuleLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipACRuleLog.setStatus("current")
_CjnIpForwardCtlMgt_ObjectIdentity = ObjectIdentity
cjnIpForwardCtlMgt = _CjnIpForwardCtlMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 6)
)


class _IpForwardCtlEnabled_Type(Integer32):
    """Custom type ipForwardCtlEnabled based on Integer32"""
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


_IpForwardCtlEnabled_Type.__name__ = "Integer32"
_IpForwardCtlEnabled_Object = MibScalar
ipForwardCtlEnabled = _IpForwardCtlEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 6, 1),
    _IpForwardCtlEnabled_Type()
)
ipForwardCtlEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipForwardCtlEnabled.setStatus("current")


class _IpForwardCtlACName_Type(OctetString):
    """Custom type ipForwardCtlACName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_IpForwardCtlACName_Type.__name__ = "OctetString"
_IpForwardCtlACName_Object = MibScalar
ipForwardCtlACName = _IpForwardCtlACName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 6, 2),
    _IpForwardCtlACName_Type()
)
ipForwardCtlACName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipForwardCtlACName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IP-ACCESS-LIST-MIB",
    **{"cjnIpAListMgmt": cjnIpAListMgmt,
       "ipACListCtlTable": ipACListCtlTable,
       "ipACListCtlEntry": ipACListCtlEntry,
       "ipACListCtlName": ipACListCtlName,
       "ipACListCtlType": ipACListCtlType,
       "ipACListCtlStatus": ipACListCtlStatus,
       "ipACRuleTable": ipACRuleTable,
       "ipACRuleEntry": ipACRuleEntry,
       "ipACRuleName": ipACRuleName,
       "ipACRuleSubIndex": ipACRuleSubIndex,
       "ipACRuleOwner": ipACRuleOwner,
       "ipACRuleSrcAddr": ipACRuleSrcAddr,
       "ipACRuleSrcAddrWild": ipACRuleSrcAddrWild,
       "ipACRuleSrcMask": ipACRuleSrcMask,
       "ipACRuleSrcMaskWild": ipACRuleSrcMaskWild,
       "ipACRuleDstAddr": ipACRuleDstAddr,
       "ipACRuleDstAddrWild": ipACRuleDstAddrWild,
       "ipACRuleDstMask": ipACRuleDstMask,
       "ipACRuleDstMaskWild": ipACRuleDstMaskWild,
       "ipACRuleOperation": ipACRuleOperation,
       "ipACRuleProtocol": ipACRuleProtocol,
       "ipACRuleL4SrcPortMin": ipACRuleL4SrcPortMin,
       "ipACRuleL4SrcPortMax": ipACRuleL4SrcPortMax,
       "ipACRuleL4DestPortMin": ipACRuleL4DestPortMin,
       "ipACRuleL4DestPortMax": ipACRuleL4DestPortMax,
       "ipACRuleStatus": ipACRuleStatus,
       "ipACRuleEstablished": ipACRuleEstablished,
       "ipACRuleLog": ipACRuleLog,
       "cjnIpForwardCtlMgt": cjnIpForwardCtlMgt,
       "ipForwardCtlEnabled": ipForwardCtlEnabled,
       "ipForwardCtlACName": ipForwardCtlACName}
)
