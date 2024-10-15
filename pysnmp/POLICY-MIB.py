# SNMP MIB module (POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/POLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:39 2024
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

(lannet,) = mibBuilder.importSymbols(
    "GEN-MIB",
    "lannet")

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


# Types definitions



class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpPolicyMgmt_ObjectIdentity = ObjectIdentity
ipPolicyMgmt = _IpPolicyMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 36)
)
_IpPolicyListTable_Object = MibTable
ipPolicyListTable = _IpPolicyListTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1)
)
if mibBuilder.loadTexts:
    ipPolicyListTable.setStatus("mandatory")
_IpPolicyListEntry_Object = MibTableRow
ipPolicyListEntry = _IpPolicyListEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1)
)
ipPolicyListEntry.setIndexNames(
    (0, "POLICY-MIB", "ipPolicyListSlot"),
    (0, "POLICY-MIB", "ipPolicyListID"),
)
if mibBuilder.loadTexts:
    ipPolicyListEntry.setStatus("mandatory")
_IpPolicyListSlot_Type = Integer32
_IpPolicyListSlot_Object = MibTableColumn
ipPolicyListSlot = _IpPolicyListSlot_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1, 1),
    _IpPolicyListSlot_Type()
)
ipPolicyListSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyListSlot.setStatus("mandatory")
_IpPolicyListID_Type = Integer32
_IpPolicyListID_Object = MibTableColumn
ipPolicyListID = _IpPolicyListID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1, 2),
    _IpPolicyListID_Type()
)
ipPolicyListID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyListID.setStatus("mandatory")


class _IpPolicyListName_Type(DisplayString):
    """Custom type ipPolicyListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IpPolicyListName_Type.__name__ = "DisplayString"
_IpPolicyListName_Object = MibTableColumn
ipPolicyListName = _IpPolicyListName_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1, 3),
    _IpPolicyListName_Type()
)
ipPolicyListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyListName.setStatus("mandatory")


class _IpPolicyListValidityStatus_Type(Integer32):
    """Custom type ipPolicyListValidityStatus based on Integer32"""
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
        *(("invalid", 3),
          ("partiallyValid", 2),
          ("valid", 1),
          ("validationInProgress", 4))
    )


_IpPolicyListValidityStatus_Type.__name__ = "Integer32"
_IpPolicyListValidityStatus_Object = MibTableColumn
ipPolicyListValidityStatus = _IpPolicyListValidityStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1, 4),
    _IpPolicyListValidityStatus_Type()
)
ipPolicyListValidityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyListValidityStatus.setStatus("mandatory")
_IpPolicyListChecksum_Type = Integer32
_IpPolicyListChecksum_Object = MibTableColumn
ipPolicyListChecksum = _IpPolicyListChecksum_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1, 5),
    _IpPolicyListChecksum_Type()
)
ipPolicyListChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyListChecksum.setStatus("obsolete")
_IpPolicyListRowStatus_Type = RowStatus
_IpPolicyListRowStatus_Object = MibTableColumn
ipPolicyListRowStatus = _IpPolicyListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1, 6),
    _IpPolicyListRowStatus_Type()
)
ipPolicyListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyListRowStatus.setStatus("mandatory")


class _IpPolicyListDefaultOperation_Type(Integer32):
    """Custom type ipPolicyListDefaultOperation based on Integer32"""
    defaultValue = 9

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
              12)
        )
    )
    namedValues = NamedValues(
        *(("deny", 10),
          ("denyAndNotify", 11),
          ("forward", 9),
          ("forwardPriority0", 1),
          ("forwardPriority1", 2),
          ("forwardPriority2", 3),
          ("forwardPriority3", 4),
          ("forwardPriority4", 5),
          ("forwardPriority5", 6),
          ("forwardPriority6", 7),
          ("forwardPriority7", 8),
          ("layer2Switching", 12))
    )


_IpPolicyListDefaultOperation_Type.__name__ = "Integer32"
_IpPolicyListDefaultOperation_Object = MibTableColumn
ipPolicyListDefaultOperation = _IpPolicyListDefaultOperation_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1, 7),
    _IpPolicyListDefaultOperation_Type()
)
ipPolicyListDefaultOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyListDefaultOperation.setStatus("mandatory")


class _IpPolicyListCookie_Type(Integer32):
    """Custom type ipPolicyListCookie based on Integer32"""
    defaultValue = 0


_IpPolicyListCookie_Object = MibTableColumn
ipPolicyListCookie = _IpPolicyListCookie_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1, 8),
    _IpPolicyListCookie_Type()
)
ipPolicyListCookie.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyListCookie.setStatus("mandatory")
_IpPolicyListTrackChanges_Type = Integer32
_IpPolicyListTrackChanges_Object = MibTableColumn
ipPolicyListTrackChanges = _IpPolicyListTrackChanges_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1, 9),
    _IpPolicyListTrackChanges_Type()
)
ipPolicyListTrackChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyListTrackChanges.setStatus("mandatory")


class _IpPolicyListOwner_Type(DisplayString):
    """Custom type ipPolicyListOwner based on DisplayString"""
    defaultValue = OctetString("other")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IpPolicyListOwner_Type.__name__ = "DisplayString"
_IpPolicyListOwner_Object = MibTableColumn
ipPolicyListOwner = _IpPolicyListOwner_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1, 10),
    _IpPolicyListOwner_Type()
)
ipPolicyListOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyListOwner.setStatus("mandatory")


class _IpPolicyListErrMsg_Type(DisplayString):
    """Custom type ipPolicyListErrMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IpPolicyListErrMsg_Type.__name__ = "DisplayString"
_IpPolicyListErrMsg_Object = MibTableColumn
ipPolicyListErrMsg = _IpPolicyListErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 1, 1, 11),
    _IpPolicyListErrMsg_Type()
)
ipPolicyListErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyListErrMsg.setStatus("mandatory")
_IpPolicyRuleTable_Object = MibTable
ipPolicyRuleTable = _IpPolicyRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2)
)
if mibBuilder.loadTexts:
    ipPolicyRuleTable.setStatus("mandatory")
_IpPolicyRuleEntry_Object = MibTableRow
ipPolicyRuleEntry = _IpPolicyRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1)
)
ipPolicyRuleEntry.setIndexNames(
    (0, "POLICY-MIB", "ipPolicyRuleSlot"),
    (0, "POLICY-MIB", "ipPolicyRuleListID"),
    (0, "POLICY-MIB", "ipPolicyRuleID"),
)
if mibBuilder.loadTexts:
    ipPolicyRuleEntry.setStatus("mandatory")
_IpPolicyRuleSlot_Type = Integer32
_IpPolicyRuleSlot_Object = MibTableColumn
ipPolicyRuleSlot = _IpPolicyRuleSlot_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 1),
    _IpPolicyRuleSlot_Type()
)
ipPolicyRuleSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyRuleSlot.setStatus("mandatory")
_IpPolicyRuleListID_Type = Integer32
_IpPolicyRuleListID_Object = MibTableColumn
ipPolicyRuleListID = _IpPolicyRuleListID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 2),
    _IpPolicyRuleListID_Type()
)
ipPolicyRuleListID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyRuleListID.setStatus("mandatory")


class _IpPolicyRuleID_Type(Integer32):
    """Custom type ipPolicyRuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_IpPolicyRuleID_Type.__name__ = "Integer32"
_IpPolicyRuleID_Object = MibTableColumn
ipPolicyRuleID = _IpPolicyRuleID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 3),
    _IpPolicyRuleID_Type()
)
ipPolicyRuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyRuleID.setStatus("mandatory")


class _IpPolicyRuleSrcAddr_Type(IpAddress):
    """Custom type ipPolicyRuleSrcAddr based on IpAddress"""
    defaultHexValue = "00000000"


_IpPolicyRuleSrcAddr_Object = MibTableColumn
ipPolicyRuleSrcAddr = _IpPolicyRuleSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 4),
    _IpPolicyRuleSrcAddr_Type()
)
ipPolicyRuleSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleSrcAddr.setStatus("mandatory")


class _IpPolicyRuleSrcAddrWild_Type(IpAddress):
    """Custom type ipPolicyRuleSrcAddrWild based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_IpPolicyRuleSrcAddrWild_Object = MibTableColumn
ipPolicyRuleSrcAddrWild = _IpPolicyRuleSrcAddrWild_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 5),
    _IpPolicyRuleSrcAddrWild_Type()
)
ipPolicyRuleSrcAddrWild.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleSrcAddrWild.setStatus("mandatory")


class _IpPolicyRuleDstAddr_Type(IpAddress):
    """Custom type ipPolicyRuleDstAddr based on IpAddress"""
    defaultHexValue = "00000000"


_IpPolicyRuleDstAddr_Object = MibTableColumn
ipPolicyRuleDstAddr = _IpPolicyRuleDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 6),
    _IpPolicyRuleDstAddr_Type()
)
ipPolicyRuleDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleDstAddr.setStatus("mandatory")


class _IpPolicyRuleDstAddrWild_Type(IpAddress):
    """Custom type ipPolicyRuleDstAddrWild based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_IpPolicyRuleDstAddrWild_Object = MibTableColumn
ipPolicyRuleDstAddrWild = _IpPolicyRuleDstAddrWild_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 7),
    _IpPolicyRuleDstAddrWild_Type()
)
ipPolicyRuleDstAddrWild.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleDstAddrWild.setStatus("mandatory")


class _IpPolicyRuleProtocol_Type(Integer32):
    """Custom type ipPolicyRuleProtocol based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_IpPolicyRuleProtocol_Type.__name__ = "Integer32"
_IpPolicyRuleProtocol_Object = MibTableColumn
ipPolicyRuleProtocol = _IpPolicyRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 8),
    _IpPolicyRuleProtocol_Type()
)
ipPolicyRuleProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleProtocol.setStatus("mandatory")


class _IpPolicyRuleL4SrcPortMin_Type(Integer32):
    """Custom type ipPolicyRuleL4SrcPortMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpPolicyRuleL4SrcPortMin_Type.__name__ = "Integer32"
_IpPolicyRuleL4SrcPortMin_Object = MibTableColumn
ipPolicyRuleL4SrcPortMin = _IpPolicyRuleL4SrcPortMin_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 9),
    _IpPolicyRuleL4SrcPortMin_Type()
)
ipPolicyRuleL4SrcPortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleL4SrcPortMin.setStatus("mandatory")


class _IpPolicyRuleL4SrcPortMax_Type(Integer32):
    """Custom type ipPolicyRuleL4SrcPortMax based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpPolicyRuleL4SrcPortMax_Type.__name__ = "Integer32"
_IpPolicyRuleL4SrcPortMax_Object = MibTableColumn
ipPolicyRuleL4SrcPortMax = _IpPolicyRuleL4SrcPortMax_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 10),
    _IpPolicyRuleL4SrcPortMax_Type()
)
ipPolicyRuleL4SrcPortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleL4SrcPortMax.setStatus("mandatory")


class _IpPolicyRuleL4DestPortMin_Type(Integer32):
    """Custom type ipPolicyRuleL4DestPortMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpPolicyRuleL4DestPortMin_Type.__name__ = "Integer32"
_IpPolicyRuleL4DestPortMin_Object = MibTableColumn
ipPolicyRuleL4DestPortMin = _IpPolicyRuleL4DestPortMin_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 11),
    _IpPolicyRuleL4DestPortMin_Type()
)
ipPolicyRuleL4DestPortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleL4DestPortMin.setStatus("mandatory")


class _IpPolicyRuleL4DestPortMax_Type(Integer32):
    """Custom type ipPolicyRuleL4DestPortMax based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpPolicyRuleL4DestPortMax_Type.__name__ = "Integer32"
_IpPolicyRuleL4DestPortMax_Object = MibTableColumn
ipPolicyRuleL4DestPortMax = _IpPolicyRuleL4DestPortMax_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 12),
    _IpPolicyRuleL4DestPortMax_Type()
)
ipPolicyRuleL4DestPortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleL4DestPortMax.setStatus("mandatory")


class _IpPolicyRuleEstablished_Type(Integer32):
    """Custom type ipPolicyRuleEstablished based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dontCare", 2),
          ("yes", 1))
    )


_IpPolicyRuleEstablished_Type.__name__ = "Integer32"
_IpPolicyRuleEstablished_Object = MibTableColumn
ipPolicyRuleEstablished = _IpPolicyRuleEstablished_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 13),
    _IpPolicyRuleEstablished_Type()
)
ipPolicyRuleEstablished.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleEstablished.setStatus("mandatory")


class _IpPolicyRuleOperation_Type(Integer32):
    """Custom type ipPolicyRuleOperation based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("deny", 10),
          ("denyAndNotify", 11),
          ("forward", 9),
          ("forwardPriority0", 1),
          ("forwardPriority1", 2),
          ("forwardPriority2", 3),
          ("forwardPriority3", 4),
          ("forwardPriority4", 5),
          ("forwardPriority5", 6),
          ("forwardPriority6", 7),
          ("forwardPriority7", 8),
          ("layer2Switching", 12))
    )


_IpPolicyRuleOperation_Type.__name__ = "Integer32"
_IpPolicyRuleOperation_Object = MibTableColumn
ipPolicyRuleOperation = _IpPolicyRuleOperation_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 14),
    _IpPolicyRuleOperation_Type()
)
ipPolicyRuleOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleOperation.setStatus("mandatory")


class _IpPolicyRuleApplicabilityPrecedence_Type(Integer32):
    """Custom type ipPolicyRuleApplicabilityPrecedence based on Integer32"""
    defaultValue = 9999

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_IpPolicyRuleApplicabilityPrecedence_Type.__name__ = "Integer32"
_IpPolicyRuleApplicabilityPrecedence_Object = MibTableColumn
ipPolicyRuleApplicabilityPrecedence = _IpPolicyRuleApplicabilityPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 15),
    _IpPolicyRuleApplicabilityPrecedence_Type()
)
ipPolicyRuleApplicabilityPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleApplicabilityPrecedence.setStatus("mandatory")


class _IpPolicyRuleApplicabilityStatus_Type(Integer32):
    """Custom type ipPolicyRuleApplicabilityStatus based on Integer32"""
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
        *(("applicable", 1),
          ("notApplicable", 3),
          ("partiallyApplicable", 2),
          ("unknown", 4))
    )


_IpPolicyRuleApplicabilityStatus_Type.__name__ = "Integer32"
_IpPolicyRuleApplicabilityStatus_Object = MibTableColumn
ipPolicyRuleApplicabilityStatus = _IpPolicyRuleApplicabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 16),
    _IpPolicyRuleApplicabilityStatus_Type()
)
ipPolicyRuleApplicabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyRuleApplicabilityStatus.setStatus("mandatory")


class _IpPolicyRuleApplicabilityType_Type(Integer32):
    """Custom type ipPolicyRuleApplicabilityType based on Integer32"""
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
        *(("dynamic", 3),
          ("quasiStatic", 2),
          ("static", 1),
          ("unknown", 4))
    )


_IpPolicyRuleApplicabilityType_Type.__name__ = "Integer32"
_IpPolicyRuleApplicabilityType_Object = MibTableColumn
ipPolicyRuleApplicabilityType = _IpPolicyRuleApplicabilityType_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 17),
    _IpPolicyRuleApplicabilityType_Type()
)
ipPolicyRuleApplicabilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyRuleApplicabilityType.setStatus("mandatory")


class _IpPolicyRuleErrMsg_Type(DisplayString):
    """Custom type ipPolicyRuleErrMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IpPolicyRuleErrMsg_Type.__name__ = "DisplayString"
_IpPolicyRuleErrMsg_Object = MibTableColumn
ipPolicyRuleErrMsg = _IpPolicyRuleErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 18),
    _IpPolicyRuleErrMsg_Type()
)
ipPolicyRuleErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyRuleErrMsg.setStatus("mandatory")
_IpPolicyRuleStatus_Type = RowStatus
_IpPolicyRuleStatus_Object = MibTableColumn
ipPolicyRuleStatus = _IpPolicyRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 19),
    _IpPolicyRuleStatus_Type()
)
ipPolicyRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleStatus.setStatus("mandatory")


class _IpPolicyRuleDSCPOperation_Type(Integer32):
    """Custom type ipPolicyRuleDSCPOperation based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_IpPolicyRuleDSCPOperation_Type.__name__ = "Integer32"
_IpPolicyRuleDSCPOperation_Object = MibTableColumn
ipPolicyRuleDSCPOperation = _IpPolicyRuleDSCPOperation_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 2, 1, 20),
    _IpPolicyRuleDSCPOperation_Type()
)
ipPolicyRuleDSCPOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyRuleDSCPOperation.setStatus("mandatory")
_IpPolicyControlTable_Object = MibTable
ipPolicyControlTable = _IpPolicyControlTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 3)
)
if mibBuilder.loadTexts:
    ipPolicyControlTable.setStatus("mandatory")
_IpPolicyControlEntry_Object = MibTableRow
ipPolicyControlEntry = _IpPolicyControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 3, 1)
)
ipPolicyControlEntry.setIndexNames(
    (0, "POLICY-MIB", "ipPolicyControlSlot"),
)
if mibBuilder.loadTexts:
    ipPolicyControlEntry.setStatus("mandatory")
_IpPolicyControlSlot_Type = Integer32
_IpPolicyControlSlot_Object = MibTableColumn
ipPolicyControlSlot = _IpPolicyControlSlot_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 3, 1, 1),
    _IpPolicyControlSlot_Type()
)
ipPolicyControlSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyControlSlot.setStatus("mandatory")
_IpPolicyControlActiveGeneralList_Type = Integer32
_IpPolicyControlActiveGeneralList_Object = MibTableColumn
ipPolicyControlActiveGeneralList = _IpPolicyControlActiveGeneralList_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 3, 1, 2),
    _IpPolicyControlActiveGeneralList_Type()
)
ipPolicyControlActiveGeneralList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyControlActiveGeneralList.setStatus("mandatory")


class _IpPolicyControlAllowedPolicyManagers_Type(Integer32):
    """Custom type ipPolicyControlAllowedPolicyManagers based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_IpPolicyControlAllowedPolicyManagers_Type.__name__ = "Integer32"
_IpPolicyControlAllowedPolicyManagers_Object = MibTableColumn
ipPolicyControlAllowedPolicyManagers = _IpPolicyControlAllowedPolicyManagers_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 3, 1, 3),
    _IpPolicyControlAllowedPolicyManagers_Type()
)
ipPolicyControlAllowedPolicyManagers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyControlAllowedPolicyManagers.setStatus("mandatory")
_IpPolicyControlCurrentChecksum_Type = Integer32
_IpPolicyControlCurrentChecksum_Object = MibTableColumn
ipPolicyControlCurrentChecksum = _IpPolicyControlCurrentChecksum_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 3, 1, 4),
    _IpPolicyControlCurrentChecksum_Type()
)
ipPolicyControlCurrentChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyControlCurrentChecksum.setStatus("mandatory")


class _IpPolicyControlMinimalPolicyManagmentVersion_Type(OctetString):
    """Custom type ipPolicyControlMinimalPolicyManagmentVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 25),
    )


_IpPolicyControlMinimalPolicyManagmentVersion_Type.__name__ = "OctetString"
_IpPolicyControlMinimalPolicyManagmentVersion_Object = MibTableColumn
ipPolicyControlMinimalPolicyManagmentVersion = _IpPolicyControlMinimalPolicyManagmentVersion_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 3, 1, 5),
    _IpPolicyControlMinimalPolicyManagmentVersion_Type()
)
ipPolicyControlMinimalPolicyManagmentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyControlMinimalPolicyManagmentVersion.setStatus("mandatory")


class _IpPolicyControlMaximalPolicyManagmentVersion_Type(OctetString):
    """Custom type ipPolicyControlMaximalPolicyManagmentVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 25),
    )


_IpPolicyControlMaximalPolicyManagmentVersion_Type.__name__ = "OctetString"
_IpPolicyControlMaximalPolicyManagmentVersion_Object = MibTableColumn
ipPolicyControlMaximalPolicyManagmentVersion = _IpPolicyControlMaximalPolicyManagmentVersion_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 3, 1, 6),
    _IpPolicyControlMaximalPolicyManagmentVersion_Type()
)
ipPolicyControlMaximalPolicyManagmentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyControlMaximalPolicyManagmentVersion.setStatus("mandatory")
_IpPolicyDiffServTable_Object = MibTable
ipPolicyDiffServTable = _IpPolicyDiffServTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 4)
)
if mibBuilder.loadTexts:
    ipPolicyDiffServTable.setStatus("mandatory")
_IpPolicyDiffServEntry_Object = MibTableRow
ipPolicyDiffServEntry = _IpPolicyDiffServEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 4, 1)
)
ipPolicyDiffServEntry.setIndexNames(
    (0, "POLICY-MIB", "ipPolicyDiffServSlot"),
    (0, "POLICY-MIB", "ipPolicyDiffServDSCP"),
)
if mibBuilder.loadTexts:
    ipPolicyDiffServEntry.setStatus("mandatory")
_IpPolicyDiffServSlot_Type = Integer32
_IpPolicyDiffServSlot_Object = MibTableColumn
ipPolicyDiffServSlot = _IpPolicyDiffServSlot_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 4, 1, 1),
    _IpPolicyDiffServSlot_Type()
)
ipPolicyDiffServSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyDiffServSlot.setStatus("mandatory")


class _IpPolicyDiffServDSCP_Type(Integer32):
    """Custom type ipPolicyDiffServDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_IpPolicyDiffServDSCP_Type.__name__ = "Integer32"
_IpPolicyDiffServDSCP_Object = MibTableColumn
ipPolicyDiffServDSCP = _IpPolicyDiffServDSCP_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 4, 1, 2),
    _IpPolicyDiffServDSCP_Type()
)
ipPolicyDiffServDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyDiffServDSCP.setStatus("mandatory")


class _IpPolicyDiffServOperation_Type(Integer32):
    """Custom type ipPolicyDiffServOperation based on Integer32"""
    defaultValue = 9

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
              11)
        )
    )
    namedValues = NamedValues(
        *(("deny", 10),
          ("denyAndNotify", 11),
          ("forwardNoChange", 9),
          ("forwardPriority0", 1),
          ("forwardPriority1", 2),
          ("forwardPriority2", 3),
          ("forwardPriority3", 4),
          ("forwardPriority4", 5),
          ("forwardPriority5", 6),
          ("forwardPriority6", 7),
          ("forwardPriority7", 8))
    )


_IpPolicyDiffServOperation_Type.__name__ = "Integer32"
_IpPolicyDiffServOperation_Object = MibTableColumn
ipPolicyDiffServOperation = _IpPolicyDiffServOperation_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 4, 1, 3),
    _IpPolicyDiffServOperation_Type()
)
ipPolicyDiffServOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyDiffServOperation.setStatus("mandatory")


class _IpPolicyDiffServName_Type(DisplayString):
    """Custom type ipPolicyDiffServName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_IpPolicyDiffServName_Type.__name__ = "DisplayString"
_IpPolicyDiffServName_Object = MibTableColumn
ipPolicyDiffServName = _IpPolicyDiffServName_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 4, 1, 4),
    _IpPolicyDiffServName_Type()
)
ipPolicyDiffServName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyDiffServName.setStatus("mandatory")


class _IpPolicyDiffServAggIndex_Type(Integer32):
    """Custom type ipPolicyDiffServAggIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_IpPolicyDiffServAggIndex_Type.__name__ = "Integer32"
_IpPolicyDiffServAggIndex_Object = MibTableColumn
ipPolicyDiffServAggIndex = _IpPolicyDiffServAggIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 4, 1, 5),
    _IpPolicyDiffServAggIndex_Type()
)
ipPolicyDiffServAggIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyDiffServAggIndex.setStatus("obsolete")


class _IpPolicyDiffServApplicabilityPrecedence_Type(Integer32):
    """Custom type ipPolicyDiffServApplicabilityPrecedence based on Integer32"""
    defaultValue = 9999

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_IpPolicyDiffServApplicabilityPrecedence_Type.__name__ = "Integer32"
_IpPolicyDiffServApplicabilityPrecedence_Object = MibTableColumn
ipPolicyDiffServApplicabilityPrecedence = _IpPolicyDiffServApplicabilityPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 4, 1, 6),
    _IpPolicyDiffServApplicabilityPrecedence_Type()
)
ipPolicyDiffServApplicabilityPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyDiffServApplicabilityPrecedence.setStatus("mandatory")


class _IpPolicyDiffServApplicabilityStatus_Type(Integer32):
    """Custom type ipPolicyDiffServApplicabilityStatus based on Integer32"""
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
        *(("applicable", 1),
          ("notApplicable", 3),
          ("partiallyApplicable", 2),
          ("unknown", 4))
    )


_IpPolicyDiffServApplicabilityStatus_Type.__name__ = "Integer32"
_IpPolicyDiffServApplicabilityStatus_Object = MibTableColumn
ipPolicyDiffServApplicabilityStatus = _IpPolicyDiffServApplicabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 4, 1, 7),
    _IpPolicyDiffServApplicabilityStatus_Type()
)
ipPolicyDiffServApplicabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyDiffServApplicabilityStatus.setStatus("mandatory")


class _IpPolicyDiffServApplicabilityType_Type(Integer32):
    """Custom type ipPolicyDiffServApplicabilityType based on Integer32"""
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
        *(("dynamic", 3),
          ("quasiStatic", 2),
          ("static", 1),
          ("unknown", 4))
    )


_IpPolicyDiffServApplicabilityType_Type.__name__ = "Integer32"
_IpPolicyDiffServApplicabilityType_Object = MibTableColumn
ipPolicyDiffServApplicabilityType = _IpPolicyDiffServApplicabilityType_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 4, 1, 8),
    _IpPolicyDiffServApplicabilityType_Type()
)
ipPolicyDiffServApplicabilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyDiffServApplicabilityType.setStatus("mandatory")


class _IpPolicyDiffServErrMsg_Type(DisplayString):
    """Custom type ipPolicyDiffServErrMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IpPolicyDiffServErrMsg_Type.__name__ = "DisplayString"
_IpPolicyDiffServErrMsg_Object = MibTableColumn
ipPolicyDiffServErrMsg = _IpPolicyDiffServErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 4, 1, 9),
    _IpPolicyDiffServErrMsg_Type()
)
ipPolicyDiffServErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyDiffServErrMsg.setStatus("mandatory")
_IpPolicyQueryTable_Object = MibTable
ipPolicyQueryTable = _IpPolicyQueryTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5)
)
if mibBuilder.loadTexts:
    ipPolicyQueryTable.setStatus("mandatory")
_IpPolicyQueryEntry_Object = MibTableRow
ipPolicyQueryEntry = _IpPolicyQueryEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1)
)
ipPolicyQueryEntry.setIndexNames(
    (0, "POLICY-MIB", "ipPolicyQuerySlot"),
)
if mibBuilder.loadTexts:
    ipPolicyQueryEntry.setStatus("mandatory")
_IpPolicyQuerySlot_Type = Integer32
_IpPolicyQuerySlot_Object = MibTableColumn
ipPolicyQuerySlot = _IpPolicyQuerySlot_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 1),
    _IpPolicyQuerySlot_Type()
)
ipPolicyQuerySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyQuerySlot.setStatus("mandatory")
_IpPolicyQueryListID_Type = Integer32
_IpPolicyQueryListID_Object = MibTableColumn
ipPolicyQueryListID = _IpPolicyQueryListID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 2),
    _IpPolicyQueryListID_Type()
)
ipPolicyQueryListID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyQueryListID.setStatus("mandatory")
_IpPolicyQuerySrcAddr_Type = IpAddress
_IpPolicyQuerySrcAddr_Object = MibTableColumn
ipPolicyQuerySrcAddr = _IpPolicyQuerySrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 3),
    _IpPolicyQuerySrcAddr_Type()
)
ipPolicyQuerySrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyQuerySrcAddr.setStatus("mandatory")
_IpPolicyQueryDstAddr_Type = IpAddress
_IpPolicyQueryDstAddr_Object = MibTableColumn
ipPolicyQueryDstAddr = _IpPolicyQueryDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 4),
    _IpPolicyQueryDstAddr_Type()
)
ipPolicyQueryDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyQueryDstAddr.setStatus("mandatory")


class _IpPolicyQueryProtocol_Type(Integer32):
    """Custom type ipPolicyQueryProtocol based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_IpPolicyQueryProtocol_Type.__name__ = "Integer32"
_IpPolicyQueryProtocol_Object = MibTableColumn
ipPolicyQueryProtocol = _IpPolicyQueryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 5),
    _IpPolicyQueryProtocol_Type()
)
ipPolicyQueryProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyQueryProtocol.setStatus("mandatory")


class _IpPolicyQueryL4SrcPort_Type(Integer32):
    """Custom type ipPolicyQueryL4SrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_IpPolicyQueryL4SrcPort_Type.__name__ = "Integer32"
_IpPolicyQueryL4SrcPort_Object = MibTableColumn
ipPolicyQueryL4SrcPort = _IpPolicyQueryL4SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 6),
    _IpPolicyQueryL4SrcPort_Type()
)
ipPolicyQueryL4SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyQueryL4SrcPort.setStatus("mandatory")


class _IpPolicyQueryL4DestPort_Type(Integer32):
    """Custom type ipPolicyQueryL4DestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpPolicyQueryL4DestPort_Type.__name__ = "Integer32"
_IpPolicyQueryL4DestPort_Object = MibTableColumn
ipPolicyQueryL4DestPort = _IpPolicyQueryL4DestPort_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 7),
    _IpPolicyQueryL4DestPort_Type()
)
ipPolicyQueryL4DestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyQueryL4DestPort.setStatus("mandatory")


class _IpPolicyQueryEstablished_Type(Integer32):
    """Custom type ipPolicyQueryEstablished based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IpPolicyQueryEstablished_Type.__name__ = "Integer32"
_IpPolicyQueryEstablished_Object = MibTableColumn
ipPolicyQueryEstablished = _IpPolicyQueryEstablished_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 8),
    _IpPolicyQueryEstablished_Type()
)
ipPolicyQueryEstablished.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyQueryEstablished.setStatus("mandatory")


class _IpPolicyQueryDSCP_Type(Integer32):
    """Custom type ipPolicyQueryDSCP based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_IpPolicyQueryDSCP_Type.__name__ = "Integer32"
_IpPolicyQueryDSCP_Object = MibTableColumn
ipPolicyQueryDSCP = _IpPolicyQueryDSCP_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 9),
    _IpPolicyQueryDSCP_Type()
)
ipPolicyQueryDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyQueryDSCP.setStatus("mandatory")


class _IpPolicyQueryOperation_Type(Integer32):
    """Custom type ipPolicyQueryOperation based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("deny", 10),
          ("denyAndNotify", 11),
          ("error", 99),
          ("forwardNoChange", 9),
          ("forwardPriority0", 1),
          ("forwardPriority1", 2),
          ("forwardPriority2", 3),
          ("forwardPriority3", 4),
          ("forwardPriority4", 5),
          ("forwardPriority5", 6),
          ("forwardPriority6", 7),
          ("forwardPriority7", 8),
          ("layer2Switching", 12),
          ("notEnoughInfo", 13))
    )


_IpPolicyQueryOperation_Type.__name__ = "Integer32"
_IpPolicyQueryOperation_Object = MibTableColumn
ipPolicyQueryOperation = _IpPolicyQueryOperation_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 10),
    _IpPolicyQueryOperation_Type()
)
ipPolicyQueryOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyQueryOperation.setStatus("mandatory")


class _IpPolicyQueryRuleID_Type(Integer32):
    """Custom type ipPolicyQueryRuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_IpPolicyQueryRuleID_Type.__name__ = "Integer32"
_IpPolicyQueryRuleID_Object = MibTableColumn
ipPolicyQueryRuleID = _IpPolicyQueryRuleID_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 11),
    _IpPolicyQueryRuleID_Type()
)
ipPolicyQueryRuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyQueryRuleID.setStatus("mandatory")


class _IpPolicyQueryDSCPOperation_Type(Integer32):
    """Custom type ipPolicyQueryDSCPOperation based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_IpPolicyQueryDSCPOperation_Type.__name__ = "Integer32"
_IpPolicyQueryDSCPOperation_Object = MibTableColumn
ipPolicyQueryDSCPOperation = _IpPolicyQueryDSCPOperation_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 12),
    _IpPolicyQueryDSCPOperation_Type()
)
ipPolicyQueryDSCPOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyQueryDSCPOperation.setStatus("mandatory")


class _IpPolicyQueryPriority_Type(Integer32):
    """Custom type ipPolicyQueryPriority based on Integer32"""
    defaultValue = 99

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
              99)
        )
    )
    namedValues = NamedValues(
        *(("dontCare", 99),
          ("forwardPriority0", 1),
          ("forwardPriority1", 2),
          ("forwardPriority2", 3),
          ("forwardPriority3", 4),
          ("forwardPriority4", 5),
          ("forwardPriority5", 6),
          ("forwardPriority6", 7),
          ("forwardPriority7", 8))
    )


_IpPolicyQueryPriority_Type.__name__ = "Integer32"
_IpPolicyQueryPriority_Object = MibTableColumn
ipPolicyQueryPriority = _IpPolicyQueryPriority_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 5, 1, 13),
    _IpPolicyQueryPriority_Type()
)
ipPolicyQueryPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyQueryPriority.setStatus("mandatory")
_IpPolicyDiffServControlTable_Object = MibTable
ipPolicyDiffServControlTable = _IpPolicyDiffServControlTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 6)
)
if mibBuilder.loadTexts:
    ipPolicyDiffServControlTable.setStatus("mandatory")
_IpPolicyDiffServControlEntry_Object = MibTableRow
ipPolicyDiffServControlEntry = _IpPolicyDiffServControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 6, 1)
)
ipPolicyDiffServControlEntry.setIndexNames(
    (0, "POLICY-MIB", "ipPolicyDiffServControlSlot"),
)
if mibBuilder.loadTexts:
    ipPolicyDiffServControlEntry.setStatus("mandatory")
_IpPolicyDiffServControlSlot_Type = Integer32
_IpPolicyDiffServControlSlot_Object = MibTableColumn
ipPolicyDiffServControlSlot = _IpPolicyDiffServControlSlot_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 6, 1, 1),
    _IpPolicyDiffServControlSlot_Type()
)
ipPolicyDiffServControlSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyDiffServControlSlot.setStatus("mandatory")
_IpPolicyDiffServControlChecksum_Type = Integer32
_IpPolicyDiffServControlChecksum_Object = MibTableColumn
ipPolicyDiffServControlChecksum = _IpPolicyDiffServControlChecksum_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 6, 1, 2),
    _IpPolicyDiffServControlChecksum_Type()
)
ipPolicyDiffServControlChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyDiffServControlChecksum.setStatus("mandatory")


class _IpPolicyDiffServControlTrustedFields_Type(Integer32):
    """Custom type ipPolicyDiffServControlTrustedFields based on Integer32"""
    defaultValue = 2

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
        *(("cos", 1),
          ("cos-dscp", 3),
          ("dscp", 2),
          ("untrust", 4))
    )


_IpPolicyDiffServControlTrustedFields_Type.__name__ = "Integer32"
_IpPolicyDiffServControlTrustedFields_Object = MibTableColumn
ipPolicyDiffServControlTrustedFields = _IpPolicyDiffServControlTrustedFields_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 6, 1, 3),
    _IpPolicyDiffServControlTrustedFields_Type()
)
ipPolicyDiffServControlTrustedFields.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPolicyDiffServControlTrustedFields.setStatus("mandatory")


class _IpPolicyDiffServControlValidityStatus_Type(Integer32):
    """Custom type ipPolicyDiffServControlValidityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_IpPolicyDiffServControlValidityStatus_Type.__name__ = "Integer32"
_IpPolicyDiffServControlValidityStatus_Object = MibTableColumn
ipPolicyDiffServControlValidityStatus = _IpPolicyDiffServControlValidityStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 6, 1, 4),
    _IpPolicyDiffServControlValidityStatus_Type()
)
ipPolicyDiffServControlValidityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyDiffServControlValidityStatus.setStatus("mandatory")


class _IpPolicyDiffServControlErrMsg_Type(DisplayString):
    """Custom type ipPolicyDiffServControlErrMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IpPolicyDiffServControlErrMsg_Type.__name__ = "DisplayString"
_IpPolicyDiffServControlErrMsg_Object = MibTableColumn
ipPolicyDiffServControlErrMsg = _IpPolicyDiffServControlErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 6, 1, 5),
    _IpPolicyDiffServControlErrMsg_Type()
)
ipPolicyDiffServControlErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyDiffServControlErrMsg.setStatus("mandatory")
_IpPolicyAccessControlViolationTable_Object = MibTable
ipPolicyAccessControlViolationTable = _IpPolicyAccessControlViolationTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 7)
)
if mibBuilder.loadTexts:
    ipPolicyAccessControlViolationTable.setStatus("mandatory")
_IpPolicyAccessControlViolationEntry_Object = MibTableRow
ipPolicyAccessControlViolationEntry = _IpPolicyAccessControlViolationEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 7, 1)
)
ipPolicyAccessControlViolationEntry.setIndexNames(
    (0, "POLICY-MIB", "ipPolicyAccessControlViolationSlot"),
)
if mibBuilder.loadTexts:
    ipPolicyAccessControlViolationEntry.setStatus("mandatory")
_IpPolicyAccessControlViolationSlot_Type = Integer32
_IpPolicyAccessControlViolationSlot_Object = MibTableColumn
ipPolicyAccessControlViolationSlot = _IpPolicyAccessControlViolationSlot_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 7, 1, 1),
    _IpPolicyAccessControlViolationSlot_Type()
)
ipPolicyAccessControlViolationSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyAccessControlViolationSlot.setStatus("mandatory")
_IpPolicyAccessControlViolationSrcAddr_Type = IpAddress
_IpPolicyAccessControlViolationSrcAddr_Object = MibTableColumn
ipPolicyAccessControlViolationSrcAddr = _IpPolicyAccessControlViolationSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 7, 1, 2),
    _IpPolicyAccessControlViolationSrcAddr_Type()
)
ipPolicyAccessControlViolationSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyAccessControlViolationSrcAddr.setStatus("mandatory")
_IpPolicyAccessControlViolationDstAddr_Type = IpAddress
_IpPolicyAccessControlViolationDstAddr_Object = MibTableColumn
ipPolicyAccessControlViolationDstAddr = _IpPolicyAccessControlViolationDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 7, 1, 3),
    _IpPolicyAccessControlViolationDstAddr_Type()
)
ipPolicyAccessControlViolationDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyAccessControlViolationDstAddr.setStatus("mandatory")


class _IpPolicyAccessControlViolationProtocol_Type(Integer32):
    """Custom type ipPolicyAccessControlViolationProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_IpPolicyAccessControlViolationProtocol_Type.__name__ = "Integer32"
_IpPolicyAccessControlViolationProtocol_Object = MibTableColumn
ipPolicyAccessControlViolationProtocol = _IpPolicyAccessControlViolationProtocol_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 7, 1, 4),
    _IpPolicyAccessControlViolationProtocol_Type()
)
ipPolicyAccessControlViolationProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyAccessControlViolationProtocol.setStatus("mandatory")


class _IpPolicyAccessControlViolationL4SrcPort_Type(Integer32):
    """Custom type ipPolicyAccessControlViolationL4SrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_IpPolicyAccessControlViolationL4SrcPort_Type.__name__ = "Integer32"
_IpPolicyAccessControlViolationL4SrcPort_Object = MibTableColumn
ipPolicyAccessControlViolationL4SrcPort = _IpPolicyAccessControlViolationL4SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 7, 1, 5),
    _IpPolicyAccessControlViolationL4SrcPort_Type()
)
ipPolicyAccessControlViolationL4SrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyAccessControlViolationL4SrcPort.setStatus("mandatory")


class _IpPolicyAccessControlViolationL4DstPort_Type(Integer32):
    """Custom type ipPolicyAccessControlViolationL4DstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpPolicyAccessControlViolationL4DstPort_Type.__name__ = "Integer32"
_IpPolicyAccessControlViolationL4DstPort_Object = MibTableColumn
ipPolicyAccessControlViolationL4DstPort = _IpPolicyAccessControlViolationL4DstPort_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 7, 1, 6),
    _IpPolicyAccessControlViolationL4DstPort_Type()
)
ipPolicyAccessControlViolationL4DstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyAccessControlViolationL4DstPort.setStatus("mandatory")


class _IpPolicyAccessControlViolationEstablished_Type(Integer32):
    """Custom type ipPolicyAccessControlViolationEstablished based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dontCare", 2),
          ("no", 3),
          ("yes", 1))
    )


_IpPolicyAccessControlViolationEstablished_Type.__name__ = "Integer32"
_IpPolicyAccessControlViolationEstablished_Object = MibTableColumn
ipPolicyAccessControlViolationEstablished = _IpPolicyAccessControlViolationEstablished_Object(
    (1, 3, 6, 1, 4, 1, 81, 36, 7, 1, 7),
    _IpPolicyAccessControlViolationEstablished_Type()
)
ipPolicyAccessControlViolationEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPolicyAccessControlViolationEstablished.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "POLICY-MIB",
    **{"RowStatus": RowStatus,
       "ipPolicyMgmt": ipPolicyMgmt,
       "ipPolicyListTable": ipPolicyListTable,
       "ipPolicyListEntry": ipPolicyListEntry,
       "ipPolicyListSlot": ipPolicyListSlot,
       "ipPolicyListID": ipPolicyListID,
       "ipPolicyListName": ipPolicyListName,
       "ipPolicyListValidityStatus": ipPolicyListValidityStatus,
       "ipPolicyListChecksum": ipPolicyListChecksum,
       "ipPolicyListRowStatus": ipPolicyListRowStatus,
       "ipPolicyListDefaultOperation": ipPolicyListDefaultOperation,
       "ipPolicyListCookie": ipPolicyListCookie,
       "ipPolicyListTrackChanges": ipPolicyListTrackChanges,
       "ipPolicyListOwner": ipPolicyListOwner,
       "ipPolicyListErrMsg": ipPolicyListErrMsg,
       "ipPolicyRuleTable": ipPolicyRuleTable,
       "ipPolicyRuleEntry": ipPolicyRuleEntry,
       "ipPolicyRuleSlot": ipPolicyRuleSlot,
       "ipPolicyRuleListID": ipPolicyRuleListID,
       "ipPolicyRuleID": ipPolicyRuleID,
       "ipPolicyRuleSrcAddr": ipPolicyRuleSrcAddr,
       "ipPolicyRuleSrcAddrWild": ipPolicyRuleSrcAddrWild,
       "ipPolicyRuleDstAddr": ipPolicyRuleDstAddr,
       "ipPolicyRuleDstAddrWild": ipPolicyRuleDstAddrWild,
       "ipPolicyRuleProtocol": ipPolicyRuleProtocol,
       "ipPolicyRuleL4SrcPortMin": ipPolicyRuleL4SrcPortMin,
       "ipPolicyRuleL4SrcPortMax": ipPolicyRuleL4SrcPortMax,
       "ipPolicyRuleL4DestPortMin": ipPolicyRuleL4DestPortMin,
       "ipPolicyRuleL4DestPortMax": ipPolicyRuleL4DestPortMax,
       "ipPolicyRuleEstablished": ipPolicyRuleEstablished,
       "ipPolicyRuleOperation": ipPolicyRuleOperation,
       "ipPolicyRuleApplicabilityPrecedence": ipPolicyRuleApplicabilityPrecedence,
       "ipPolicyRuleApplicabilityStatus": ipPolicyRuleApplicabilityStatus,
       "ipPolicyRuleApplicabilityType": ipPolicyRuleApplicabilityType,
       "ipPolicyRuleErrMsg": ipPolicyRuleErrMsg,
       "ipPolicyRuleStatus": ipPolicyRuleStatus,
       "ipPolicyRuleDSCPOperation": ipPolicyRuleDSCPOperation,
       "ipPolicyControlTable": ipPolicyControlTable,
       "ipPolicyControlEntry": ipPolicyControlEntry,
       "ipPolicyControlSlot": ipPolicyControlSlot,
       "ipPolicyControlActiveGeneralList": ipPolicyControlActiveGeneralList,
       "ipPolicyControlAllowedPolicyManagers": ipPolicyControlAllowedPolicyManagers,
       "ipPolicyControlCurrentChecksum": ipPolicyControlCurrentChecksum,
       "ipPolicyControlMinimalPolicyManagmentVersion": ipPolicyControlMinimalPolicyManagmentVersion,
       "ipPolicyControlMaximalPolicyManagmentVersion": ipPolicyControlMaximalPolicyManagmentVersion,
       "ipPolicyDiffServTable": ipPolicyDiffServTable,
       "ipPolicyDiffServEntry": ipPolicyDiffServEntry,
       "ipPolicyDiffServSlot": ipPolicyDiffServSlot,
       "ipPolicyDiffServDSCP": ipPolicyDiffServDSCP,
       "ipPolicyDiffServOperation": ipPolicyDiffServOperation,
       "ipPolicyDiffServName": ipPolicyDiffServName,
       "ipPolicyDiffServAggIndex": ipPolicyDiffServAggIndex,
       "ipPolicyDiffServApplicabilityPrecedence": ipPolicyDiffServApplicabilityPrecedence,
       "ipPolicyDiffServApplicabilityStatus": ipPolicyDiffServApplicabilityStatus,
       "ipPolicyDiffServApplicabilityType": ipPolicyDiffServApplicabilityType,
       "ipPolicyDiffServErrMsg": ipPolicyDiffServErrMsg,
       "ipPolicyQueryTable": ipPolicyQueryTable,
       "ipPolicyQueryEntry": ipPolicyQueryEntry,
       "ipPolicyQuerySlot": ipPolicyQuerySlot,
       "ipPolicyQueryListID": ipPolicyQueryListID,
       "ipPolicyQuerySrcAddr": ipPolicyQuerySrcAddr,
       "ipPolicyQueryDstAddr": ipPolicyQueryDstAddr,
       "ipPolicyQueryProtocol": ipPolicyQueryProtocol,
       "ipPolicyQueryL4SrcPort": ipPolicyQueryL4SrcPort,
       "ipPolicyQueryL4DestPort": ipPolicyQueryL4DestPort,
       "ipPolicyQueryEstablished": ipPolicyQueryEstablished,
       "ipPolicyQueryDSCP": ipPolicyQueryDSCP,
       "ipPolicyQueryOperation": ipPolicyQueryOperation,
       "ipPolicyQueryRuleID": ipPolicyQueryRuleID,
       "ipPolicyQueryDSCPOperation": ipPolicyQueryDSCPOperation,
       "ipPolicyQueryPriority": ipPolicyQueryPriority,
       "ipPolicyDiffServControlTable": ipPolicyDiffServControlTable,
       "ipPolicyDiffServControlEntry": ipPolicyDiffServControlEntry,
       "ipPolicyDiffServControlSlot": ipPolicyDiffServControlSlot,
       "ipPolicyDiffServControlChecksum": ipPolicyDiffServControlChecksum,
       "ipPolicyDiffServControlTrustedFields": ipPolicyDiffServControlTrustedFields,
       "ipPolicyDiffServControlValidityStatus": ipPolicyDiffServControlValidityStatus,
       "ipPolicyDiffServControlErrMsg": ipPolicyDiffServControlErrMsg,
       "ipPolicyAccessControlViolationTable": ipPolicyAccessControlViolationTable,
       "ipPolicyAccessControlViolationEntry": ipPolicyAccessControlViolationEntry,
       "ipPolicyAccessControlViolationSlot": ipPolicyAccessControlViolationSlot,
       "ipPolicyAccessControlViolationSrcAddr": ipPolicyAccessControlViolationSrcAddr,
       "ipPolicyAccessControlViolationDstAddr": ipPolicyAccessControlViolationDstAddr,
       "ipPolicyAccessControlViolationProtocol": ipPolicyAccessControlViolationProtocol,
       "ipPolicyAccessControlViolationL4SrcPort": ipPolicyAccessControlViolationL4SrcPort,
       "ipPolicyAccessControlViolationL4DstPort": ipPolicyAccessControlViolationL4DstPort,
       "ipPolicyAccessControlViolationEstablished": ipPolicyAccessControlViolationEstablished}
)
