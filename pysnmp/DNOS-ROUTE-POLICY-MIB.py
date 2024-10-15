# SNMP MIB module (DNOS-ROUTE-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DNOS-ROUTE-POLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:13 2024
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

(fastPathRouting,) = mibBuilder.importSymbols(
    "DNOS-ROUTING-MIB",
    "fastPathRouting")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fastPathRoutePolicy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FastpathRoutePolicyAction(Integer32, TextualConvention):
    status = "current"
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



class FastpathRoutePolicyStmtIpPrecedence(Integer32, TextualConvention):
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
          ("flash-override", 4),
          ("immediate", 2),
          ("internet", 6),
          ("invalid", 8),
          ("network", 7),
          ("priority", 1),
          ("routine", 0))
    )



# MIB Managed Objects in the order of their OIDs

_FastpathRoutePolicyNameTable_Object = MibTable
fastpathRoutePolicyNameTable = _FastpathRoutePolicyNameTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 1)
)
if mibBuilder.loadTexts:
    fastpathRoutePolicyNameTable.setStatus("current")
_FastpathRoutePolicyNameEntry_Object = MibTableRow
fastpathRoutePolicyNameEntry = _FastpathRoutePolicyNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 1, 1)
)
fastpathRoutePolicyNameEntry.setIndexNames(
    (0, "DNOS-ROUTE-POLICY-MIB", "fastpathRoutePolicyName"),
    (0, "DNOS-ROUTE-POLICY-MIB", "fastpathRoutePolicyStmtActionType"),
    (0, "DNOS-ROUTE-POLICY-MIB", "fastpathRoutePolicySequence"),
)
if mibBuilder.loadTexts:
    fastpathRoutePolicyNameEntry.setStatus("current")


class _FastpathRoutePolicyName_Type(DisplayString):
    """Custom type fastpathRoutePolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FastpathRoutePolicyName_Type.__name__ = "DisplayString"
_FastpathRoutePolicyName_Object = MibTableColumn
fastpathRoutePolicyName = _FastpathRoutePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 1, 1, 1),
    _FastpathRoutePolicyName_Type()
)
fastpathRoutePolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fastpathRoutePolicyName.setStatus("current")
_FastpathRoutePolicyStmtActionType_Type = FastpathRoutePolicyAction
_FastpathRoutePolicyStmtActionType_Object = MibTableColumn
fastpathRoutePolicyStmtActionType = _FastpathRoutePolicyStmtActionType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 1, 1, 2),
    _FastpathRoutePolicyStmtActionType_Type()
)
fastpathRoutePolicyStmtActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fastpathRoutePolicyStmtActionType.setStatus("current")


class _FastpathRoutePolicySequence_Type(Unsigned32):
    """Custom type fastpathRoutePolicySequence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FastpathRoutePolicySequence_Type.__name__ = "Unsigned32"
_FastpathRoutePolicySequence_Object = MibTableColumn
fastpathRoutePolicySequence = _FastpathRoutePolicySequence_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 1, 1, 3),
    _FastpathRoutePolicySequence_Type()
)
fastpathRoutePolicySequence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fastpathRoutePolicySequence.setStatus("current")
_FastpathRoutePolicyNameRowStatus_Type = RowStatus
_FastpathRoutePolicyNameRowStatus_Object = MibTableColumn
fastpathRoutePolicyNameRowStatus = _FastpathRoutePolicyNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 1, 1, 4),
    _FastpathRoutePolicyNameRowStatus_Type()
)
fastpathRoutePolicyNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fastpathRoutePolicyNameRowStatus.setStatus("current")
_FastpathRoutePolicyStamentTable_Object = MibTable
fastpathRoutePolicyStamentTable = _FastpathRoutePolicyStamentTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2)
)
if mibBuilder.loadTexts:
    fastpathRoutePolicyStamentTable.setStatus("current")
_FastpathRoutePolicyStatementEntry_Object = MibTableRow
fastpathRoutePolicyStatementEntry = _FastpathRoutePolicyStatementEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1)
)
fastpathRoutePolicyStatementEntry.setIndexNames(
    (0, "DNOS-ROUTE-POLICY-MIB", "fastpathRoutePolicyStmtName"),
    (0, "DNOS-ROUTE-POLICY-MIB", "fastpathRoutePolicyStmtSeqNum"),
    (0, "DNOS-ROUTE-POLICY-MIB", "fastpathRoutePolicyStmtAction"),
)
if mibBuilder.loadTexts:
    fastpathRoutePolicyStatementEntry.setStatus("current")


class _FastpathRoutePolicyStmtName_Type(DisplayString):
    """Custom type fastpathRoutePolicyStmtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_FastpathRoutePolicyStmtName_Type.__name__ = "DisplayString"
_FastpathRoutePolicyStmtName_Object = MibTableColumn
fastpathRoutePolicyStmtName = _FastpathRoutePolicyStmtName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1, 1),
    _FastpathRoutePolicyStmtName_Type()
)
fastpathRoutePolicyStmtName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fastpathRoutePolicyStmtName.setStatus("current")
_FastpathRoutePolicyStmtSeqNum_Type = Unsigned32
_FastpathRoutePolicyStmtSeqNum_Object = MibTableColumn
fastpathRoutePolicyStmtSeqNum = _FastpathRoutePolicyStmtSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1, 2),
    _FastpathRoutePolicyStmtSeqNum_Type()
)
fastpathRoutePolicyStmtSeqNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fastpathRoutePolicyStmtSeqNum.setStatus("current")
_FastpathRoutePolicyStmtAction_Type = FastpathRoutePolicyAction
_FastpathRoutePolicyStmtAction_Object = MibTableColumn
fastpathRoutePolicyStmtAction = _FastpathRoutePolicyStmtAction_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1, 3),
    _FastpathRoutePolicyStmtAction_Type()
)
fastpathRoutePolicyStmtAction.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fastpathRoutePolicyStmtAction.setStatus("current")
_FastpathRoutePolicyStmtMatchIpv4AclList_Type = DisplayString
_FastpathRoutePolicyStmtMatchIpv4AclList_Object = MibTableColumn
fastpathRoutePolicyStmtMatchIpv4AclList = _FastpathRoutePolicyStmtMatchIpv4AclList_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1, 4),
    _FastpathRoutePolicyStmtMatchIpv4AclList_Type()
)
fastpathRoutePolicyStmtMatchIpv4AclList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastpathRoutePolicyStmtMatchIpv4AclList.setStatus("current")
_FastpathRoutePolicyStmtMatchIpv4AclDelList_Type = DisplayString
_FastpathRoutePolicyStmtMatchIpv4AclDelList_Object = MibTableColumn
fastpathRoutePolicyStmtMatchIpv4AclDelList = _FastpathRoutePolicyStmtMatchIpv4AclDelList_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1, 5),
    _FastpathRoutePolicyStmtMatchIpv4AclDelList_Type()
)
fastpathRoutePolicyStmtMatchIpv4AclDelList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastpathRoutePolicyStmtMatchIpv4AclDelList.setStatus("current")
_FastpathRoutePolicyStmtMatchMacAclList_Type = DisplayString
_FastpathRoutePolicyStmtMatchMacAclList_Object = MibTableColumn
fastpathRoutePolicyStmtMatchMacAclList = _FastpathRoutePolicyStmtMatchMacAclList_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1, 6),
    _FastpathRoutePolicyStmtMatchMacAclList_Type()
)
fastpathRoutePolicyStmtMatchMacAclList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastpathRoutePolicyStmtMatchMacAclList.setStatus("current")
_FastpathRoutePolicyStmtMatchMacAclDelList_Type = DisplayString
_FastpathRoutePolicyStmtMatchMacAclDelList_Object = MibTableColumn
fastpathRoutePolicyStmtMatchMacAclDelList = _FastpathRoutePolicyStmtMatchMacAclDelList_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1, 7),
    _FastpathRoutePolicyStmtMatchMacAclDelList_Type()
)
fastpathRoutePolicyStmtMatchMacAclDelList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastpathRoutePolicyStmtMatchMacAclDelList.setStatus("current")
_FastpathRoutePolicyStmtMatchPacketLengthRangeMin_Type = Unsigned32
_FastpathRoutePolicyStmtMatchPacketLengthRangeMin_Object = MibTableColumn
fastpathRoutePolicyStmtMatchPacketLengthRangeMin = _FastpathRoutePolicyStmtMatchPacketLengthRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1, 8),
    _FastpathRoutePolicyStmtMatchPacketLengthRangeMin_Type()
)
fastpathRoutePolicyStmtMatchPacketLengthRangeMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastpathRoutePolicyStmtMatchPacketLengthRangeMin.setStatus("current")
_FastpathRoutePolicyStmtMatchPacketLengthRangeMax_Type = Unsigned32
_FastpathRoutePolicyStmtMatchPacketLengthRangeMax_Object = MibTableColumn
fastpathRoutePolicyStmtMatchPacketLengthRangeMax = _FastpathRoutePolicyStmtMatchPacketLengthRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1, 9),
    _FastpathRoutePolicyStmtMatchPacketLengthRangeMax_Type()
)
fastpathRoutePolicyStmtMatchPacketLengthRangeMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastpathRoutePolicyStmtMatchPacketLengthRangeMax.setStatus("current")
_FastpathRoutePolicyStmtSetIpNextHopList_Type = DisplayString
_FastpathRoutePolicyStmtSetIpNextHopList_Object = MibTableColumn
fastpathRoutePolicyStmtSetIpNextHopList = _FastpathRoutePolicyStmtSetIpNextHopList_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1, 10),
    _FastpathRoutePolicyStmtSetIpNextHopList_Type()
)
fastpathRoutePolicyStmtSetIpNextHopList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastpathRoutePolicyStmtSetIpNextHopList.setStatus("current")
_FastpathRoutePolicyStmtSetIpNextHopDelList_Type = DisplayString
_FastpathRoutePolicyStmtSetIpNextHopDelList_Object = MibTableColumn
fastpathRoutePolicyStmtSetIpNextHopDelList = _FastpathRoutePolicyStmtSetIpNextHopDelList_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1, 11),
    _FastpathRoutePolicyStmtSetIpNextHopDelList_Type()
)
fastpathRoutePolicyStmtSetIpNextHopDelList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastpathRoutePolicyStmtSetIpNextHopDelList.setStatus("current")
_FastpathRoutePolicyStmtSetDefaultIpNextHopList_Type = DisplayString
_FastpathRoutePolicyStmtSetDefaultIpNextHopList_Object = MibTableColumn
fastpathRoutePolicyStmtSetDefaultIpNextHopList = _FastpathRoutePolicyStmtSetDefaultIpNextHopList_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1, 12),
    _FastpathRoutePolicyStmtSetDefaultIpNextHopList_Type()
)
fastpathRoutePolicyStmtSetDefaultIpNextHopList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastpathRoutePolicyStmtSetDefaultIpNextHopList.setStatus("current")
_FastpathRoutePolicyStmtSetDefaultIpNextHopDelList_Type = DisplayString
_FastpathRoutePolicyStmtSetDefaultIpNextHopDelList_Object = MibTableColumn
fastpathRoutePolicyStmtSetDefaultIpNextHopDelList = _FastpathRoutePolicyStmtSetDefaultIpNextHopDelList_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1, 13),
    _FastpathRoutePolicyStmtSetDefaultIpNextHopDelList_Type()
)
fastpathRoutePolicyStmtSetDefaultIpNextHopDelList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastpathRoutePolicyStmtSetDefaultIpNextHopDelList.setStatus("current")
_FastpathRoutePolicyStmtSetIpPrecedence_Type = FastpathRoutePolicyStmtIpPrecedence
_FastpathRoutePolicyStmtSetIpPrecedence_Object = MibTableColumn
fastpathRoutePolicyStmtSetIpPrecedence = _FastpathRoutePolicyStmtSetIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1, 14),
    _FastpathRoutePolicyStmtSetIpPrecedence_Type()
)
fastpathRoutePolicyStmtSetIpPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastpathRoutePolicyStmtSetIpPrecedence.setStatus("current")
_FastpathRoutePolicyStmtSetIntfNull0_Type = TruthValue
_FastpathRoutePolicyStmtSetIntfNull0_Object = MibTableColumn
fastpathRoutePolicyStmtSetIntfNull0 = _FastpathRoutePolicyStmtSetIntfNull0_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1, 15),
    _FastpathRoutePolicyStmtSetIntfNull0_Type()
)
fastpathRoutePolicyStmtSetIntfNull0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastpathRoutePolicyStmtSetIntfNull0.setStatus("current")
_FastpathRoutePolicyIfTable_Object = MibTable
fastpathRoutePolicyIfTable = _FastpathRoutePolicyIfTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 3)
)
if mibBuilder.loadTexts:
    fastpathRoutePolicyIfTable.setStatus("current")
_FastpathRoutePolicyIfEntry_Object = MibTableRow
fastpathRoutePolicyIfEntry = _FastpathRoutePolicyIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 3, 1)
)
fastpathRoutePolicyIfEntry.setIndexNames(
    (0, "DNOS-ROUTE-POLICY-MIB", "fastpathRoutePolicyIfIndex"),
    (0, "DNOS-ROUTE-POLICY-MIB", "fastpathRoutePolicyIfName"),
)
if mibBuilder.loadTexts:
    fastpathRoutePolicyIfEntry.setStatus("current")
_FastpathRoutePolicyIfIndex_Type = InterfaceIndex
_FastpathRoutePolicyIfIndex_Object = MibTableColumn
fastpathRoutePolicyIfIndex = _FastpathRoutePolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 3, 1, 1),
    _FastpathRoutePolicyIfIndex_Type()
)
fastpathRoutePolicyIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fastpathRoutePolicyIfIndex.setStatus("current")


class _FastpathRoutePolicyIfName_Type(DisplayString):
    """Custom type fastpathRoutePolicyIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_FastpathRoutePolicyIfName_Type.__name__ = "DisplayString"
_FastpathRoutePolicyIfName_Object = MibTableColumn
fastpathRoutePolicyIfName = _FastpathRoutePolicyIfName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 3, 1, 2),
    _FastpathRoutePolicyIfName_Type()
)
fastpathRoutePolicyIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fastpathRoutePolicyIfName.setStatus("current")
_FastpathRoutePolicyIfRowStatus_Type = RowStatus
_FastpathRoutePolicyIfRowStatus_Object = MibTableColumn
fastpathRoutePolicyIfRowStatus = _FastpathRoutePolicyIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 3, 1, 3),
    _FastpathRoutePolicyIfRowStatus_Type()
)
fastpathRoutePolicyIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fastpathRoutePolicyIfRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-ROUTE-POLICY-MIB",
    **{"FastpathRoutePolicyAction": FastpathRoutePolicyAction,
       "FastpathRoutePolicyStmtIpPrecedence": FastpathRoutePolicyStmtIpPrecedence,
       "fastPathRoutePolicy": fastPathRoutePolicy,
       "fastpathRoutePolicyNameTable": fastpathRoutePolicyNameTable,
       "fastpathRoutePolicyNameEntry": fastpathRoutePolicyNameEntry,
       "fastpathRoutePolicyName": fastpathRoutePolicyName,
       "fastpathRoutePolicyStmtActionType": fastpathRoutePolicyStmtActionType,
       "fastpathRoutePolicySequence": fastpathRoutePolicySequence,
       "fastpathRoutePolicyNameRowStatus": fastpathRoutePolicyNameRowStatus,
       "fastpathRoutePolicyStamentTable": fastpathRoutePolicyStamentTable,
       "fastpathRoutePolicyStatementEntry": fastpathRoutePolicyStatementEntry,
       "fastpathRoutePolicyStmtName": fastpathRoutePolicyStmtName,
       "fastpathRoutePolicyStmtSeqNum": fastpathRoutePolicyStmtSeqNum,
       "fastpathRoutePolicyStmtAction": fastpathRoutePolicyStmtAction,
       "fastpathRoutePolicyStmtMatchIpv4AclList": fastpathRoutePolicyStmtMatchIpv4AclList,
       "fastpathRoutePolicyStmtMatchIpv4AclDelList": fastpathRoutePolicyStmtMatchIpv4AclDelList,
       "fastpathRoutePolicyStmtMatchMacAclList": fastpathRoutePolicyStmtMatchMacAclList,
       "fastpathRoutePolicyStmtMatchMacAclDelList": fastpathRoutePolicyStmtMatchMacAclDelList,
       "fastpathRoutePolicyStmtMatchPacketLengthRangeMin": fastpathRoutePolicyStmtMatchPacketLengthRangeMin,
       "fastpathRoutePolicyStmtMatchPacketLengthRangeMax": fastpathRoutePolicyStmtMatchPacketLengthRangeMax,
       "fastpathRoutePolicyStmtSetIpNextHopList": fastpathRoutePolicyStmtSetIpNextHopList,
       "fastpathRoutePolicyStmtSetIpNextHopDelList": fastpathRoutePolicyStmtSetIpNextHopDelList,
       "fastpathRoutePolicyStmtSetDefaultIpNextHopList": fastpathRoutePolicyStmtSetDefaultIpNextHopList,
       "fastpathRoutePolicyStmtSetDefaultIpNextHopDelList": fastpathRoutePolicyStmtSetDefaultIpNextHopDelList,
       "fastpathRoutePolicyStmtSetIpPrecedence": fastpathRoutePolicyStmtSetIpPrecedence,
       "fastpathRoutePolicyStmtSetIntfNull0": fastpathRoutePolicyStmtSetIntfNull0,
       "fastpathRoutePolicyIfTable": fastpathRoutePolicyIfTable,
       "fastpathRoutePolicyIfEntry": fastpathRoutePolicyIfEntry,
       "fastpathRoutePolicyIfIndex": fastpathRoutePolicyIfIndex,
       "fastpathRoutePolicyIfName": fastpathRoutePolicyIfName,
       "fastpathRoutePolicyIfRowStatus": fastpathRoutePolicyIfRowStatus}
)
