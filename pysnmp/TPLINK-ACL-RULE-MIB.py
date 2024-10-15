# SNMP MIB module (TPLINK-ACL-RULE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-ACL-RULE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:46 2024
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

(tplinkAclMIBObjects,) = mibBuilder.importSymbols(
    "TPLINK-ACL-MIB",
    "tplinkAclMIBObjects")

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TpAclRuleConfigure_ObjectIdentity = ObjectIdentity
tpAclRuleConfigure = _TpAclRuleConfigure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1)
)
_TpMacRuleTable_Object = MibTable
tpMacRuleTable = _TpMacRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tpMacRuleTable.setStatus("current")
_TpMacRuleEntry_Object = MibTableRow
tpMacRuleEntry = _TpMacRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1)
)
tpMacRuleEntry.setIndexNames(
    (0, "TPLINK-ACL-RULE-MIB", "tpMacAclId"),
    (0, "TPLINK-ACL-RULE-MIB", "tpMacRuleId"),
)
if mibBuilder.loadTexts:
    tpMacRuleEntry.setStatus("current")
_TpMacAclId_Type = Integer32
_TpMacAclId_Object = MibTableColumn
tpMacAclId = _TpMacAclId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 1),
    _TpMacAclId_Type()
)
tpMacAclId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMacAclId.setStatus("current")
_TpMacRuleId_Type = Integer32
_TpMacRuleId_Object = MibTableColumn
tpMacRuleId = _TpMacRuleId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 2),
    _TpMacRuleId_Type()
)
tpMacRuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMacRuleId.setStatus("current")


class _TpMacSecOperation_Type(Integer32):
    """Custom type tpMacSecOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 0))
    )


_TpMacSecOperation_Type.__name__ = "Integer32"
_TpMacSecOperation_Object = MibTableColumn
tpMacSecOperation = _TpMacSecOperation_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 3),
    _TpMacSecOperation_Type()
)
tpMacSecOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMacSecOperation.setStatus("current")
_TpMacSmacAddress_Type = OctetString
_TpMacSmacAddress_Object = MibTableColumn
tpMacSmacAddress = _TpMacSmacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 4),
    _TpMacSmacAddress_Type()
)
tpMacSmacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMacSmacAddress.setStatus("current")
_TpMacSmacMask_Type = OctetString
_TpMacSmacMask_Object = MibTableColumn
tpMacSmacMask = _TpMacSmacMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 5),
    _TpMacSmacMask_Type()
)
tpMacSmacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMacSmacMask.setStatus("current")
_TpMacDmacAddress_Type = OctetString
_TpMacDmacAddress_Object = MibTableColumn
tpMacDmacAddress = _TpMacDmacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 6),
    _TpMacDmacAddress_Type()
)
tpMacDmacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMacDmacAddress.setStatus("current")
_TpMacDmacMask_Type = OctetString
_TpMacDmacMask_Object = MibTableColumn
tpMacDmacMask = _TpMacDmacMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 7),
    _TpMacDmacMask_Type()
)
tpMacDmacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMacDmacMask.setStatus("current")
_TpMacVlanId_Type = Integer32
_TpMacVlanId_Object = MibTableColumn
tpMacVlanId = _TpMacVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 8),
    _TpMacVlanId_Type()
)
tpMacVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMacVlanId.setStatus("current")
_TpMacEtherType_Type = Integer32
_TpMacEtherType_Object = MibTableColumn
tpMacEtherType = _TpMacEtherType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 9),
    _TpMacEtherType_Type()
)
tpMacEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMacEtherType.setStatus("current")
_TpMacPri_Type = Integer32
_TpMacPri_Object = MibTableColumn
tpMacPri = _TpMacPri_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 10),
    _TpMacPri_Type()
)
tpMacPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMacPri.setStatus("current")
_TpMacTimeSegment_Type = OctetString
_TpMacTimeSegment_Object = MibTableColumn
tpMacTimeSegment = _TpMacTimeSegment_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 11),
    _TpMacTimeSegment_Type()
)
tpMacTimeSegment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMacTimeSegment.setStatus("current")
_TpMacRuleStatus_Type = TPRowStatus
_TpMacRuleStatus_Object = MibTableColumn
tpMacRuleStatus = _TpMacRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 12),
    _TpMacRuleStatus_Type()
)
tpMacRuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMacRuleStatus.setStatus("current")
_TpStdipRuleTable_Object = MibTable
tpStdipRuleTable = _TpStdipRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tpStdipRuleTable.setStatus("current")
_TpStdipRuleEntry_Object = MibTableRow
tpStdipRuleEntry = _TpStdipRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1)
)
tpStdipRuleEntry.setIndexNames(
    (0, "TPLINK-ACL-RULE-MIB", "tpStdipAclId"),
    (0, "TPLINK-ACL-RULE-MIB", "tpStdipRuleId"),
)
if mibBuilder.loadTexts:
    tpStdipRuleEntry.setStatus("current")
_TpStdipAclId_Type = Integer32
_TpStdipAclId_Object = MibTableColumn
tpStdipAclId = _TpStdipAclId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 1),
    _TpStdipAclId_Type()
)
tpStdipAclId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStdipAclId.setStatus("current")
_TpStdipRuleId_Type = Integer32
_TpStdipRuleId_Object = MibTableColumn
tpStdipRuleId = _TpStdipRuleId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 2),
    _TpStdipRuleId_Type()
)
tpStdipRuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStdipRuleId.setStatus("current")


class _TpStdipSecOperation_Type(Integer32):
    """Custom type tpStdipSecOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 0))
    )


_TpStdipSecOperation_Type.__name__ = "Integer32"
_TpStdipSecOperation_Object = MibTableColumn
tpStdipSecOperation = _TpStdipSecOperation_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 3),
    _TpStdipSecOperation_Type()
)
tpStdipSecOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpStdipSecOperation.setStatus("current")
_TpStdipSipAddress_Type = IpAddress
_TpStdipSipAddress_Object = MibTableColumn
tpStdipSipAddress = _TpStdipSipAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 4),
    _TpStdipSipAddress_Type()
)
tpStdipSipAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpStdipSipAddress.setStatus("current")
_TpStdipSipMask_Type = IpAddress
_TpStdipSipMask_Object = MibTableColumn
tpStdipSipMask = _TpStdipSipMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 5),
    _TpStdipSipMask_Type()
)
tpStdipSipMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpStdipSipMask.setStatus("current")
_TpStdipDipAddress_Type = IpAddress
_TpStdipDipAddress_Object = MibTableColumn
tpStdipDipAddress = _TpStdipDipAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 6),
    _TpStdipDipAddress_Type()
)
tpStdipDipAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpStdipDipAddress.setStatus("current")
_TpStdipDipMask_Type = IpAddress
_TpStdipDipMask_Object = MibTableColumn
tpStdipDipMask = _TpStdipDipMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 7),
    _TpStdipDipMask_Type()
)
tpStdipDipMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpStdipDipMask.setStatus("current")
_TpStdipTimeSegment_Type = OctetString
_TpStdipTimeSegment_Object = MibTableColumn
tpStdipTimeSegment = _TpStdipTimeSegment_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 8),
    _TpStdipTimeSegment_Type()
)
tpStdipTimeSegment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpStdipTimeSegment.setStatus("current")
_TpStdipRuleStatus_Type = TPRowStatus
_TpStdipRuleStatus_Object = MibTableColumn
tpStdipRuleStatus = _TpStdipRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 9),
    _TpStdipRuleStatus_Type()
)
tpStdipRuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpStdipRuleStatus.setStatus("current")
_TpExtipRuleTable_Object = MibTable
tpExtipRuleTable = _TpExtipRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tpExtipRuleTable.setStatus("current")
_TpExtipRuleEntry_Object = MibTableRow
tpExtipRuleEntry = _TpExtipRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1)
)
tpExtipRuleEntry.setIndexNames(
    (0, "TPLINK-ACL-RULE-MIB", "tpExtipAclId"),
    (0, "TPLINK-ACL-RULE-MIB", "tpExtipRuleId"),
)
if mibBuilder.loadTexts:
    tpExtipRuleEntry.setStatus("current")
_TpExtipAclId_Type = Integer32
_TpExtipAclId_Object = MibTableColumn
tpExtipAclId = _TpExtipAclId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 1),
    _TpExtipAclId_Type()
)
tpExtipAclId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpExtipAclId.setStatus("current")
_TpExtipRuleId_Type = Integer32
_TpExtipRuleId_Object = MibTableColumn
tpExtipRuleId = _TpExtipRuleId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 2),
    _TpExtipRuleId_Type()
)
tpExtipRuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpExtipRuleId.setStatus("current")


class _TpExtipSecOperation_Type(Integer32):
    """Custom type tpExtipSecOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 0))
    )


_TpExtipSecOperation_Type.__name__ = "Integer32"
_TpExtipSecOperation_Object = MibTableColumn
tpExtipSecOperation = _TpExtipSecOperation_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 3),
    _TpExtipSecOperation_Type()
)
tpExtipSecOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpExtipSecOperation.setStatus("current")


class _TpExtipFragment_Type(Integer32):
    """Custom type tpExtipFragment based on Integer32"""
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


_TpExtipFragment_Type.__name__ = "Integer32"
_TpExtipFragment_Object = MibTableColumn
tpExtipFragment = _TpExtipFragment_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 4),
    _TpExtipFragment_Type()
)
tpExtipFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpExtipFragment.setStatus("current")
_TpExtipSipAddress_Type = IpAddress
_TpExtipSipAddress_Object = MibTableColumn
tpExtipSipAddress = _TpExtipSipAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 5),
    _TpExtipSipAddress_Type()
)
tpExtipSipAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpExtipSipAddress.setStatus("current")
_TpExtipSipMask_Type = IpAddress
_TpExtipSipMask_Object = MibTableColumn
tpExtipSipMask = _TpExtipSipMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 6),
    _TpExtipSipMask_Type()
)
tpExtipSipMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpExtipSipMask.setStatus("current")
_TpExtipDipAddress_Type = IpAddress
_TpExtipDipAddress_Object = MibTableColumn
tpExtipDipAddress = _TpExtipDipAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 7),
    _TpExtipDipAddress_Type()
)
tpExtipDipAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpExtipDipAddress.setStatus("current")
_TpExtipDipMask_Type = IpAddress
_TpExtipDipMask_Object = MibTableColumn
tpExtipDipMask = _TpExtipDipMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 8),
    _TpExtipDipMask_Type()
)
tpExtipDipMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpExtipDipMask.setStatus("current")
_TpExtipProtocol_Type = Integer32
_TpExtipProtocol_Object = MibTableColumn
tpExtipProtocol = _TpExtipProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 9),
    _TpExtipProtocol_Type()
)
tpExtipProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpExtipProtocol.setStatus("current")
_TpExtipTcpFlag_Type = Integer32
_TpExtipTcpFlag_Object = MibTableColumn
tpExtipTcpFlag = _TpExtipTcpFlag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 10),
    _TpExtipTcpFlag_Type()
)
tpExtipTcpFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpExtipTcpFlag.setStatus("current")
_TpExtipSourcePort_Type = Integer32
_TpExtipSourcePort_Object = MibTableColumn
tpExtipSourcePort = _TpExtipSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 11),
    _TpExtipSourcePort_Type()
)
tpExtipSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpExtipSourcePort.setStatus("current")
_TpExtipDestPort_Type = Integer32
_TpExtipDestPort_Object = MibTableColumn
tpExtipDestPort = _TpExtipDestPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 12),
    _TpExtipDestPort_Type()
)
tpExtipDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpExtipDestPort.setStatus("current")
_TpExtipDscp_Type = Integer32
_TpExtipDscp_Object = MibTableColumn
tpExtipDscp = _TpExtipDscp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 13),
    _TpExtipDscp_Type()
)
tpExtipDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpExtipDscp.setStatus("current")
_TpExtipTos_Type = Integer32
_TpExtipTos_Object = MibTableColumn
tpExtipTos = _TpExtipTos_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 14),
    _TpExtipTos_Type()
)
tpExtipTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpExtipTos.setStatus("current")
_TpExtipPre_Type = Integer32
_TpExtipPre_Object = MibTableColumn
tpExtipPre = _TpExtipPre_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 15),
    _TpExtipPre_Type()
)
tpExtipPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpExtipPre.setStatus("current")
_TpExtipTimeSegment_Type = OctetString
_TpExtipTimeSegment_Object = MibTableColumn
tpExtipTimeSegment = _TpExtipTimeSegment_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 16),
    _TpExtipTimeSegment_Type()
)
tpExtipTimeSegment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpExtipTimeSegment.setStatus("current")
_TpExtipRuleStatus_Type = TPRowStatus
_TpExtipRuleStatus_Object = MibTableColumn
tpExtipRuleStatus = _TpExtipRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 17),
    _TpExtipRuleStatus_Type()
)
tpExtipRuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpExtipRuleStatus.setStatus("current")
_TpCombRuleTable_Object = MibTable
tpCombRuleTable = _TpCombRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tpCombRuleTable.setStatus("current")
_TpCombRuleEntry_Object = MibTableRow
tpCombRuleEntry = _TpCombRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1)
)
tpCombRuleEntry.setIndexNames(
    (0, "TPLINK-ACL-RULE-MIB", "tpCombAclId"),
    (0, "TPLINK-ACL-RULE-MIB", "tpCombRuleId"),
)
if mibBuilder.loadTexts:
    tpCombRuleEntry.setStatus("current")
_TpCombAclId_Type = Integer32
_TpCombAclId_Object = MibTableColumn
tpCombAclId = _TpCombAclId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 1),
    _TpCombAclId_Type()
)
tpCombAclId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpCombAclId.setStatus("current")
_TpCombRuleId_Type = Integer32
_TpCombRuleId_Object = MibTableColumn
tpCombRuleId = _TpCombRuleId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 2),
    _TpCombRuleId_Type()
)
tpCombRuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpCombRuleId.setStatus("current")


class _TpCombSecOperation_Type(Integer32):
    """Custom type tpCombSecOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 0))
    )


_TpCombSecOperation_Type.__name__ = "Integer32"
_TpCombSecOperation_Object = MibTableColumn
tpCombSecOperation = _TpCombSecOperation_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 3),
    _TpCombSecOperation_Type()
)
tpCombSecOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombSecOperation.setStatus("current")
_TpCombSmacAddress_Type = OctetString
_TpCombSmacAddress_Object = MibTableColumn
tpCombSmacAddress = _TpCombSmacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 4),
    _TpCombSmacAddress_Type()
)
tpCombSmacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombSmacAddress.setStatus("current")
_TpCombSmacMask_Type = OctetString
_TpCombSmacMask_Object = MibTableColumn
tpCombSmacMask = _TpCombSmacMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 5),
    _TpCombSmacMask_Type()
)
tpCombSmacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombSmacMask.setStatus("current")
_TpCombDmacAddress_Type = OctetString
_TpCombDmacAddress_Object = MibTableColumn
tpCombDmacAddress = _TpCombDmacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 6),
    _TpCombDmacAddress_Type()
)
tpCombDmacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombDmacAddress.setStatus("current")
_TpCombDmacMask_Type = OctetString
_TpCombDmacMask_Object = MibTableColumn
tpCombDmacMask = _TpCombDmacMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 7),
    _TpCombDmacMask_Type()
)
tpCombDmacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombDmacMask.setStatus("current")
_TpCombVlanId_Type = Integer32
_TpCombVlanId_Object = MibTableColumn
tpCombVlanId = _TpCombVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 8),
    _TpCombVlanId_Type()
)
tpCombVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombVlanId.setStatus("current")
_TpCombEtherType_Type = Integer32
_TpCombEtherType_Object = MibTableColumn
tpCombEtherType = _TpCombEtherType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 9),
    _TpCombEtherType_Type()
)
tpCombEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombEtherType.setStatus("current")
_TpCombPri_Type = Integer32
_TpCombPri_Object = MibTableColumn
tpCombPri = _TpCombPri_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 10),
    _TpCombPri_Type()
)
tpCombPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombPri.setStatus("current")
_TpCombSipAddress_Type = IpAddress
_TpCombSipAddress_Object = MibTableColumn
tpCombSipAddress = _TpCombSipAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 11),
    _TpCombSipAddress_Type()
)
tpCombSipAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombSipAddress.setStatus("current")
_TpCombSipMask_Type = IpAddress
_TpCombSipMask_Object = MibTableColumn
tpCombSipMask = _TpCombSipMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 12),
    _TpCombSipMask_Type()
)
tpCombSipMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombSipMask.setStatus("current")
_TpCombDipAddress_Type = IpAddress
_TpCombDipAddress_Object = MibTableColumn
tpCombDipAddress = _TpCombDipAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 13),
    _TpCombDipAddress_Type()
)
tpCombDipAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombDipAddress.setStatus("current")
_TpCombDipMask_Type = IpAddress
_TpCombDipMask_Object = MibTableColumn
tpCombDipMask = _TpCombDipMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 14),
    _TpCombDipMask_Type()
)
tpCombDipMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombDipMask.setStatus("current")
_TpCombTimeSegment_Type = OctetString
_TpCombTimeSegment_Object = MibTableColumn
tpCombTimeSegment = _TpCombTimeSegment_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 15),
    _TpCombTimeSegment_Type()
)
tpCombTimeSegment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombTimeSegment.setStatus("current")
_TpCombRuleStatus_Type = TPRowStatus
_TpCombRuleStatus_Object = MibTableColumn
tpCombRuleStatus = _TpCombRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 16),
    _TpCombRuleStatus_Type()
)
tpCombRuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpCombRuleStatus.setStatus("current")
_TpIPv6RuleTable_Object = MibTable
tpIPv6RuleTable = _TpIPv6RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5)
)
if mibBuilder.loadTexts:
    tpIPv6RuleTable.setStatus("current")
_TpIPv6RuleEntry_Object = MibTableRow
tpIPv6RuleEntry = _TpIPv6RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 1)
)
tpIPv6RuleEntry.setIndexNames(
    (0, "TPLINK-ACL-RULE-MIB", "tpIPv6AclId"),
    (0, "TPLINK-ACL-RULE-MIB", "tpIPv6RuleId"),
)
if mibBuilder.loadTexts:
    tpIPv6RuleEntry.setStatus("current")
_TpIPv6AclId_Type = Integer32
_TpIPv6AclId_Object = MibTableColumn
tpIPv6AclId = _TpIPv6AclId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 1, 1),
    _TpIPv6AclId_Type()
)
tpIPv6AclId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIPv6AclId.setStatus("current")
_TpIPv6RuleId_Type = Integer32
_TpIPv6RuleId_Object = MibTableColumn
tpIPv6RuleId = _TpIPv6RuleId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 1, 2),
    _TpIPv6RuleId_Type()
)
tpIPv6RuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIPv6RuleId.setStatus("current")


class _TpIPv6SecOperation_Type(Integer32):
    """Custom type tpIPv6SecOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 0))
    )


_TpIPv6SecOperation_Type.__name__ = "Integer32"
_TpIPv6SecOperation_Object = MibTableColumn
tpIPv6SecOperation = _TpIPv6SecOperation_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 1, 3),
    _TpIPv6SecOperation_Type()
)
tpIPv6SecOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIPv6SecOperation.setStatus("current")
_TpIPv6TrafficClass_Type = Integer32
_TpIPv6TrafficClass_Object = MibTableColumn
tpIPv6TrafficClass = _TpIPv6TrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 1, 4),
    _TpIPv6TrafficClass_Type()
)
tpIPv6TrafficClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIPv6TrafficClass.setStatus("current")
_TpIPv6FlowLabel_Type = Integer32
_TpIPv6FlowLabel_Object = MibTableColumn
tpIPv6FlowLabel = _TpIPv6FlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 1, 5),
    _TpIPv6FlowLabel_Type()
)
tpIPv6FlowLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIPv6FlowLabel.setStatus("current")
_TpIPv6SipAddress_Type = OctetString
_TpIPv6SipAddress_Object = MibTableColumn
tpIPv6SipAddress = _TpIPv6SipAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 1, 6),
    _TpIPv6SipAddress_Type()
)
tpIPv6SipAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIPv6SipAddress.setStatus("current")
_TpIPv6SipMask_Type = OctetString
_TpIPv6SipMask_Object = MibTableColumn
tpIPv6SipMask = _TpIPv6SipMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 1, 7),
    _TpIPv6SipMask_Type()
)
tpIPv6SipMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIPv6SipMask.setStatus("current")
_TpIPv6DipAddress_Type = OctetString
_TpIPv6DipAddress_Object = MibTableColumn
tpIPv6DipAddress = _TpIPv6DipAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 1, 8),
    _TpIPv6DipAddress_Type()
)
tpIPv6DipAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIPv6DipAddress.setStatus("current")
_TpIPv6DipMask_Type = OctetString
_TpIPv6DipMask_Object = MibTableColumn
tpIPv6DipMask = _TpIPv6DipMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 1, 9),
    _TpIPv6DipMask_Type()
)
tpIPv6DipMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIPv6DipMask.setStatus("current")
_TpIPv6SourcePort_Type = Integer32
_TpIPv6SourcePort_Object = MibTableColumn
tpIPv6SourcePort = _TpIPv6SourcePort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 1, 10),
    _TpIPv6SourcePort_Type()
)
tpIPv6SourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIPv6SourcePort.setStatus("current")
_TpIPv6DestPort_Type = Integer32
_TpIPv6DestPort_Object = MibTableColumn
tpIPv6DestPort = _TpIPv6DestPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 1, 11),
    _TpIPv6DestPort_Type()
)
tpIPv6DestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIPv6DestPort.setStatus("current")
_TpIPv6TimeSegment_Type = OctetString
_TpIPv6TimeSegment_Object = MibTableColumn
tpIPv6TimeSegment = _TpIPv6TimeSegment_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 1, 12),
    _TpIPv6TimeSegment_Type()
)
tpIPv6TimeSegment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIPv6TimeSegment.setStatus("current")
_TpIPv6RuleStatus_Type = TPRowStatus
_TpIPv6RuleStatus_Object = MibTableColumn
tpIPv6RuleStatus = _TpIPv6RuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 1, 13),
    _TpIPv6RuleStatus_Type()
)
tpIPv6RuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIPv6RuleStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-ACL-RULE-MIB",
    **{"tpAclRuleConfigure": tpAclRuleConfigure,
       "tpMacRuleTable": tpMacRuleTable,
       "tpMacRuleEntry": tpMacRuleEntry,
       "tpMacAclId": tpMacAclId,
       "tpMacRuleId": tpMacRuleId,
       "tpMacSecOperation": tpMacSecOperation,
       "tpMacSmacAddress": tpMacSmacAddress,
       "tpMacSmacMask": tpMacSmacMask,
       "tpMacDmacAddress": tpMacDmacAddress,
       "tpMacDmacMask": tpMacDmacMask,
       "tpMacVlanId": tpMacVlanId,
       "tpMacEtherType": tpMacEtherType,
       "tpMacPri": tpMacPri,
       "tpMacTimeSegment": tpMacTimeSegment,
       "tpMacRuleStatus": tpMacRuleStatus,
       "tpStdipRuleTable": tpStdipRuleTable,
       "tpStdipRuleEntry": tpStdipRuleEntry,
       "tpStdipAclId": tpStdipAclId,
       "tpStdipRuleId": tpStdipRuleId,
       "tpStdipSecOperation": tpStdipSecOperation,
       "tpStdipSipAddress": tpStdipSipAddress,
       "tpStdipSipMask": tpStdipSipMask,
       "tpStdipDipAddress": tpStdipDipAddress,
       "tpStdipDipMask": tpStdipDipMask,
       "tpStdipTimeSegment": tpStdipTimeSegment,
       "tpStdipRuleStatus": tpStdipRuleStatus,
       "tpExtipRuleTable": tpExtipRuleTable,
       "tpExtipRuleEntry": tpExtipRuleEntry,
       "tpExtipAclId": tpExtipAclId,
       "tpExtipRuleId": tpExtipRuleId,
       "tpExtipSecOperation": tpExtipSecOperation,
       "tpExtipFragment": tpExtipFragment,
       "tpExtipSipAddress": tpExtipSipAddress,
       "tpExtipSipMask": tpExtipSipMask,
       "tpExtipDipAddress": tpExtipDipAddress,
       "tpExtipDipMask": tpExtipDipMask,
       "tpExtipProtocol": tpExtipProtocol,
       "tpExtipTcpFlag": tpExtipTcpFlag,
       "tpExtipSourcePort": tpExtipSourcePort,
       "tpExtipDestPort": tpExtipDestPort,
       "tpExtipDscp": tpExtipDscp,
       "tpExtipTos": tpExtipTos,
       "tpExtipPre": tpExtipPre,
       "tpExtipTimeSegment": tpExtipTimeSegment,
       "tpExtipRuleStatus": tpExtipRuleStatus,
       "tpCombRuleTable": tpCombRuleTable,
       "tpCombRuleEntry": tpCombRuleEntry,
       "tpCombAclId": tpCombAclId,
       "tpCombRuleId": tpCombRuleId,
       "tpCombSecOperation": tpCombSecOperation,
       "tpCombSmacAddress": tpCombSmacAddress,
       "tpCombSmacMask": tpCombSmacMask,
       "tpCombDmacAddress": tpCombDmacAddress,
       "tpCombDmacMask": tpCombDmacMask,
       "tpCombVlanId": tpCombVlanId,
       "tpCombEtherType": tpCombEtherType,
       "tpCombPri": tpCombPri,
       "tpCombSipAddress": tpCombSipAddress,
       "tpCombSipMask": tpCombSipMask,
       "tpCombDipAddress": tpCombDipAddress,
       "tpCombDipMask": tpCombDipMask,
       "tpCombTimeSegment": tpCombTimeSegment,
       "tpCombRuleStatus": tpCombRuleStatus,
       "tpIPv6RuleTable": tpIPv6RuleTable,
       "tpIPv6RuleEntry": tpIPv6RuleEntry,
       "tpIPv6AclId": tpIPv6AclId,
       "tpIPv6RuleId": tpIPv6RuleId,
       "tpIPv6SecOperation": tpIPv6SecOperation,
       "tpIPv6TrafficClass": tpIPv6TrafficClass,
       "tpIPv6FlowLabel": tpIPv6FlowLabel,
       "tpIPv6SipAddress": tpIPv6SipAddress,
       "tpIPv6SipMask": tpIPv6SipMask,
       "tpIPv6DipAddress": tpIPv6DipAddress,
       "tpIPv6DipMask": tpIPv6DipMask,
       "tpIPv6SourcePort": tpIPv6SourcePort,
       "tpIPv6DestPort": tpIPv6DestPort,
       "tpIPv6TimeSegment": tpIPv6TimeSegment,
       "tpIPv6RuleStatus": tpIPv6RuleStatus}
)
