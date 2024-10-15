# SNMP MIB module (CT-FASTPATH-ARPACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CT-FASTPATH-ARPACL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:10 2024
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

(ctArpAclExpMib,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctArpAclExpMib")

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
 PhysAddress,
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ctFastPathArpAclMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 34, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtAgentArpAclGroup_ObjectIdentity = ObjectIdentity
ctAgentArpAclGroup = _CtAgentArpAclGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 34, 1, 1)
)
_CtAgentArpAclTable_Object = MibTable
ctAgentArpAclTable = _CtAgentArpAclTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 34, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ctAgentArpAclTable.setStatus("current")
_CtAgentArpAclEntry_Object = MibTableRow
ctAgentArpAclEntry = _CtAgentArpAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 34, 1, 1, 1, 1)
)
ctAgentArpAclEntry.setIndexNames(
    (0, "CT-FASTPATH-ARPACL-MIB", "ctAgentArpAclName"),
)
if mibBuilder.loadTexts:
    ctAgentArpAclEntry.setStatus("current")


class _CtAgentArpAclName_Type(DisplayString):
    """Custom type ctAgentArpAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CtAgentArpAclName_Type.__name__ = "DisplayString"
_CtAgentArpAclName_Object = MibTableColumn
ctAgentArpAclName = _CtAgentArpAclName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 34, 1, 1, 1, 1, 1),
    _CtAgentArpAclName_Type()
)
ctAgentArpAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctAgentArpAclName.setStatus("current")
_CtAgentArpAclRowStatus_Type = RowStatus
_CtAgentArpAclRowStatus_Object = MibTableColumn
ctAgentArpAclRowStatus = _CtAgentArpAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 34, 1, 1, 1, 1, 2),
    _CtAgentArpAclRowStatus_Type()
)
ctAgentArpAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctAgentArpAclRowStatus.setStatus("current")
_CtAgentArpAclRuleTable_Object = MibTable
ctAgentArpAclRuleTable = _CtAgentArpAclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 34, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ctAgentArpAclRuleTable.setStatus("current")
_CtAgentArpAclRuleEntry_Object = MibTableRow
ctAgentArpAclRuleEntry = _CtAgentArpAclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 34, 1, 1, 2, 1)
)
ctAgentArpAclRuleEntry.setIndexNames(
    (0, "CT-FASTPATH-ARPACL-MIB", "ctAgentArpAclName"),
    (0, "CT-FASTPATH-ARPACL-MIB", "ctAgentArpAclRuleMatchSenderIpAddr"),
    (0, "CT-FASTPATH-ARPACL-MIB", "ctAgentArpAclRuleMatchSenderMacAddr"),
)
if mibBuilder.loadTexts:
    ctAgentArpAclRuleEntry.setStatus("current")
_CtAgentArpAclRuleMatchSenderIpAddr_Type = IpAddress
_CtAgentArpAclRuleMatchSenderIpAddr_Object = MibTableColumn
ctAgentArpAclRuleMatchSenderIpAddr = _CtAgentArpAclRuleMatchSenderIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 34, 1, 1, 2, 1, 1),
    _CtAgentArpAclRuleMatchSenderIpAddr_Type()
)
ctAgentArpAclRuleMatchSenderIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctAgentArpAclRuleMatchSenderIpAddr.setStatus("current")
_CtAgentArpAclRuleMatchSenderMacAddr_Type = MacAddress
_CtAgentArpAclRuleMatchSenderMacAddr_Object = MibTableColumn
ctAgentArpAclRuleMatchSenderMacAddr = _CtAgentArpAclRuleMatchSenderMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 34, 1, 1, 2, 1, 2),
    _CtAgentArpAclRuleMatchSenderMacAddr_Type()
)
ctAgentArpAclRuleMatchSenderMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctAgentArpAclRuleMatchSenderMacAddr.setStatus("current")
_CtAgentArpAclRuleRowStatus_Type = RowStatus
_CtAgentArpAclRuleRowStatus_Object = MibTableColumn
ctAgentArpAclRuleRowStatus = _CtAgentArpAclRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 34, 1, 1, 2, 1, 3),
    _CtAgentArpAclRuleRowStatus_Type()
)
ctAgentArpAclRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctAgentArpAclRuleRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CT-FASTPATH-ARPACL-MIB",
    **{"ctFastPathArpAclMIB": ctFastPathArpAclMIB,
       "ctAgentArpAclGroup": ctAgentArpAclGroup,
       "ctAgentArpAclTable": ctAgentArpAclTable,
       "ctAgentArpAclEntry": ctAgentArpAclEntry,
       "ctAgentArpAclName": ctAgentArpAclName,
       "ctAgentArpAclRowStatus": ctAgentArpAclRowStatus,
       "ctAgentArpAclRuleTable": ctAgentArpAclRuleTable,
       "ctAgentArpAclRuleEntry": ctAgentArpAclRuleEntry,
       "ctAgentArpAclRuleMatchSenderIpAddr": ctAgentArpAclRuleMatchSenderIpAddr,
       "ctAgentArpAclRuleMatchSenderMacAddr": ctAgentArpAclRuleMatchSenderMacAddr,
       "ctAgentArpAclRuleRowStatus": ctAgentArpAclRuleRowStatus}
)
