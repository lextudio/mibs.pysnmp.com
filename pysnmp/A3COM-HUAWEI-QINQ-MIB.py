# SNMP MIB module (A3COM-HUAWEI-QINQ-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-QINQ-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:54 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

h3cQINQ = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69)
)
h3cQINQ.setRevisions(
        ("2006-03-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cQinQSwitchState(Integer32, TextualConvention):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_H3cQinQMibObject_ObjectIdentity = ObjectIdentity
h3cQinQMibObject = _H3cQinQMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1)
)
_H3cQinQGlobalConfigGroup_ObjectIdentity = ObjectIdentity
h3cQinQGlobalConfigGroup = _H3cQinQGlobalConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 1)
)


class _H3cQinQBpduTunnelSwitch_Type(H3cQinQSwitchState):
    """Custom type h3cQinQBpduTunnelSwitch based on H3cQinQSwitchState"""


_H3cQinQBpduTunnelSwitch_Object = MibScalar
h3cQinQBpduTunnelSwitch = _H3cQinQBpduTunnelSwitch_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 1, 1),
    _H3cQinQBpduTunnelSwitch_Type()
)
h3cQinQBpduTunnelSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cQinQBpduTunnelSwitch.setStatus("current")


class _H3cQinQEthernetTypeValue_Type(Integer32):
    """Custom type h3cQinQEthernetTypeValue based on Integer32"""
    defaultValue = 33024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cQinQEthernetTypeValue_Type.__name__ = "Integer32"
_H3cQinQEthernetTypeValue_Object = MibScalar
h3cQinQEthernetTypeValue = _H3cQinQEthernetTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 1, 2),
    _H3cQinQEthernetTypeValue_Type()
)
h3cQinQEthernetTypeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cQinQEthernetTypeValue.setStatus("current")


class _H3cQinQServiceTPIDValue_Type(Integer32):
    """Custom type h3cQinQServiceTPIDValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cQinQServiceTPIDValue_Type.__name__ = "Integer32"
_H3cQinQServiceTPIDValue_Object = MibScalar
h3cQinQServiceTPIDValue = _H3cQinQServiceTPIDValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 1, 3),
    _H3cQinQServiceTPIDValue_Type()
)
h3cQinQServiceTPIDValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cQinQServiceTPIDValue.setStatus("current")


class _H3cQinQCustomerTPIDValue_Type(Integer32):
    """Custom type h3cQinQCustomerTPIDValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cQinQCustomerTPIDValue_Type.__name__ = "Integer32"
_H3cQinQCustomerTPIDValue_Object = MibScalar
h3cQinQCustomerTPIDValue = _H3cQinQCustomerTPIDValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 1, 4),
    _H3cQinQCustomerTPIDValue_Type()
)
h3cQinQCustomerTPIDValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cQinQCustomerTPIDValue.setStatus("current")
_H3cQinQBpduTunnelTable_Object = MibTable
h3cQinQBpduTunnelTable = _H3cQinQBpduTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 2)
)
if mibBuilder.loadTexts:
    h3cQinQBpduTunnelTable.setStatus("current")
_H3cQinQBpduTunnelEntry_Object = MibTableRow
h3cQinQBpduTunnelEntry = _H3cQinQBpduTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 2, 1)
)
h3cQinQBpduTunnelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-QINQ-MIB", "h3cQinQProtocolIndex"),
)
if mibBuilder.loadTexts:
    h3cQinQBpduTunnelEntry.setStatus("current")


class _H3cQinQProtocolIndex_Type(Integer32):
    """Custom type h3cQinQProtocolIndex based on Integer32"""
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
        *(("bpdu", 1),
          ("gvrp", 3),
          ("igmp", 4),
          ("stp", 2))
    )


_H3cQinQProtocolIndex_Type.__name__ = "Integer32"
_H3cQinQProtocolIndex_Object = MibTableColumn
h3cQinQProtocolIndex = _H3cQinQProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 2, 1, 1),
    _H3cQinQProtocolIndex_Type()
)
h3cQinQProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQinQProtocolIndex.setStatus("current")
_H3cQinQBpduRowStatus_Type = RowStatus
_H3cQinQBpduRowStatus_Object = MibTableColumn
h3cQinQBpduRowStatus = _H3cQinQBpduRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 2, 1, 2),
    _H3cQinQBpduRowStatus_Type()
)
h3cQinQBpduRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQinQBpduRowStatus.setStatus("current")
_H3cQinQPriorityRemarkTable_Object = MibTable
h3cQinQPriorityRemarkTable = _H3cQinQPriorityRemarkTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 3)
)
if mibBuilder.loadTexts:
    h3cQinQPriorityRemarkTable.setStatus("current")
_H3cQinQPriorityRemarkEntry_Object = MibTableRow
h3cQinQPriorityRemarkEntry = _H3cQinQPriorityRemarkEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 3, 1)
)
h3cQinQPriorityRemarkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-QINQ-MIB", "h3cQinQPriorityValue"),
)
if mibBuilder.loadTexts:
    h3cQinQPriorityRemarkEntry.setStatus("current")


class _H3cQinQPriorityValue_Type(Integer32):
    """Custom type h3cQinQPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_H3cQinQPriorityValue_Type.__name__ = "Integer32"
_H3cQinQPriorityValue_Object = MibTableColumn
h3cQinQPriorityValue = _H3cQinQPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 3, 1, 1),
    _H3cQinQPriorityValue_Type()
)
h3cQinQPriorityValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQinQPriorityValue.setStatus("current")


class _H3cQinQPriorityRemarkValue_Type(Integer32):
    """Custom type h3cQinQPriorityRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_H3cQinQPriorityRemarkValue_Type.__name__ = "Integer32"
_H3cQinQPriorityRemarkValue_Object = MibTableColumn
h3cQinQPriorityRemarkValue = _H3cQinQPriorityRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 3, 1, 2),
    _H3cQinQPriorityRemarkValue_Type()
)
h3cQinQPriorityRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQinQPriorityRemarkValue.setStatus("current")
_H3cQinQPriorityRowStatus_Type = RowStatus
_H3cQinQPriorityRowStatus_Object = MibTableColumn
h3cQinQPriorityRowStatus = _H3cQinQPriorityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 3, 1, 3),
    _H3cQinQPriorityRowStatus_Type()
)
h3cQinQPriorityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQinQPriorityRowStatus.setStatus("current")
_H3cQinQVidTable_Object = MibTable
h3cQinQVidTable = _H3cQinQVidTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 4)
)
if mibBuilder.loadTexts:
    h3cQinQVidTable.setStatus("current")
_H3cQinQVidEntry_Object = MibTableRow
h3cQinQVidEntry = _H3cQinQVidEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 4, 1)
)
h3cQinQVidEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-QINQ-MIB", "h3cQinQVlanID"),
)
if mibBuilder.loadTexts:
    h3cQinQVidEntry.setStatus("current")


class _H3cQinQVlanID_Type(Integer32):
    """Custom type h3cQinQVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_H3cQinQVlanID_Type.__name__ = "Integer32"
_H3cQinQVlanID_Object = MibTableColumn
h3cQinQVlanID = _H3cQinQVlanID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 4, 1, 1),
    _H3cQinQVlanID_Type()
)
h3cQinQVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQinQVlanID.setStatus("current")


class _H3cQinQInboundVidListLow_Type(OctetString):
    """Custom type h3cQinQInboundVidListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_H3cQinQInboundVidListLow_Type.__name__ = "OctetString"
_H3cQinQInboundVidListLow_Object = MibTableColumn
h3cQinQInboundVidListLow = _H3cQinQInboundVidListLow_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 4, 1, 2),
    _H3cQinQInboundVidListLow_Type()
)
h3cQinQInboundVidListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQinQInboundVidListLow.setStatus("current")


class _H3cQinQInboundVidListHigh_Type(OctetString):
    """Custom type h3cQinQInboundVidListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_H3cQinQInboundVidListHigh_Type.__name__ = "OctetString"
_H3cQinQInboundVidListHigh_Object = MibTableColumn
h3cQinQInboundVidListHigh = _H3cQinQInboundVidListHigh_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 4, 1, 3),
    _H3cQinQInboundVidListHigh_Type()
)
h3cQinQInboundVidListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQinQInboundVidListHigh.setStatus("current")


class _H3cQinQVidEthernetType_Type(Integer32):
    """Custom type h3cQinQVidEthernetType based on Integer32"""
    defaultValue = 33024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cQinQVidEthernetType_Type.__name__ = "Integer32"
_H3cQinQVidEthernetType_Object = MibTableColumn
h3cQinQVidEthernetType = _H3cQinQVidEthernetType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 4, 1, 4),
    _H3cQinQVidEthernetType_Type()
)
h3cQinQVidEthernetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQinQVidEthernetType.setStatus("current")
_H3cQinQVidRowStatus_Type = RowStatus
_H3cQinQVidRowStatus_Object = MibTableColumn
h3cQinQVidRowStatus = _H3cQinQVidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 4, 1, 5),
    _H3cQinQVidRowStatus_Type()
)
h3cQinQVidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQinQVidRowStatus.setStatus("current")
_H3cQinQVidSwapTable_Object = MibTable
h3cQinQVidSwapTable = _H3cQinQVidSwapTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 5)
)
if mibBuilder.loadTexts:
    h3cQinQVidSwapTable.setStatus("current")
_H3cQinQVidSwapEntry_Object = MibTableRow
h3cQinQVidSwapEntry = _H3cQinQVidSwapEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 5, 1)
)
h3cQinQVidSwapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-QINQ-MIB", "h3cQinQVlanID"),
    (0, "A3COM-HUAWEI-QINQ-MIB", "h3cQinQVidSwapOld"),
)
if mibBuilder.loadTexts:
    h3cQinQVidSwapEntry.setStatus("current")


class _H3cQinQVidSwapOld_Type(Integer32):
    """Custom type h3cQinQVidSwapOld based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_H3cQinQVidSwapOld_Type.__name__ = "Integer32"
_H3cQinQVidSwapOld_Object = MibTableColumn
h3cQinQVidSwapOld = _H3cQinQVidSwapOld_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 5, 1, 1),
    _H3cQinQVidSwapOld_Type()
)
h3cQinQVidSwapOld.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQinQVidSwapOld.setStatus("current")


class _H3cQinQVidSwapNew_Type(Integer32):
    """Custom type h3cQinQVidSwapNew based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_H3cQinQVidSwapNew_Type.__name__ = "Integer32"
_H3cQinQVidSwapNew_Object = MibTableColumn
h3cQinQVidSwapNew = _H3cQinQVidSwapNew_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 5, 1, 2),
    _H3cQinQVidSwapNew_Type()
)
h3cQinQVidSwapNew.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQinQVidSwapNew.setStatus("current")
_H3cQinQVidSwapRowStatus_Type = RowStatus
_H3cQinQVidSwapRowStatus_Object = MibTableColumn
h3cQinQVidSwapRowStatus = _H3cQinQVidSwapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 5, 1, 3),
    _H3cQinQVidSwapRowStatus_Type()
)
h3cQinQVidSwapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQinQVidSwapRowStatus.setStatus("current")
_H3cQinQPrioritySwapTable_Object = MibTable
h3cQinQPrioritySwapTable = _H3cQinQPrioritySwapTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 6)
)
if mibBuilder.loadTexts:
    h3cQinQPrioritySwapTable.setStatus("current")
_H3cQinQPrioritySwapEntry_Object = MibTableRow
h3cQinQPrioritySwapEntry = _H3cQinQPrioritySwapEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 6, 1)
)
h3cQinQPrioritySwapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-QINQ-MIB", "h3cQinQVlanID"),
    (0, "A3COM-HUAWEI-QINQ-MIB", "h3cQinQPrioritySwapOld"),
)
if mibBuilder.loadTexts:
    h3cQinQPrioritySwapEntry.setStatus("current")


class _H3cQinQPrioritySwapOld_Type(Integer32):
    """Custom type h3cQinQPrioritySwapOld based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_H3cQinQPrioritySwapOld_Type.__name__ = "Integer32"
_H3cQinQPrioritySwapOld_Object = MibTableColumn
h3cQinQPrioritySwapOld = _H3cQinQPrioritySwapOld_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 6, 1, 1),
    _H3cQinQPrioritySwapOld_Type()
)
h3cQinQPrioritySwapOld.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQinQPrioritySwapOld.setStatus("current")


class _H3cQinQPrioritySwapNew_Type(Integer32):
    """Custom type h3cQinQPrioritySwapNew based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_H3cQinQPrioritySwapNew_Type.__name__ = "Integer32"
_H3cQinQPrioritySwapNew_Object = MibTableColumn
h3cQinQPrioritySwapNew = _H3cQinQPrioritySwapNew_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 6, 1, 2),
    _H3cQinQPrioritySwapNew_Type()
)
h3cQinQPrioritySwapNew.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQinQPrioritySwapNew.setStatus("current")
_H3cQinQPrioritySwapRowStatus_Type = RowStatus
_H3cQinQPrioritySwapRowStatus_Object = MibTableColumn
h3cQinQPrioritySwapRowStatus = _H3cQinQPrioritySwapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 6, 1, 3),
    _H3cQinQPrioritySwapRowStatus_Type()
)
h3cQinQPrioritySwapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQinQPrioritySwapRowStatus.setStatus("current")
_H3cQinQIfConfigTable_Object = MibTable
h3cQinQIfConfigTable = _H3cQinQIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 7)
)
if mibBuilder.loadTexts:
    h3cQinQIfConfigTable.setStatus("current")
_H3cQinQIfConfigEntry_Object = MibTableRow
h3cQinQIfConfigEntry = _H3cQinQIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 7, 1)
)
h3cQinQIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cQinQIfConfigEntry.setStatus("current")


class _H3cQinQIfEthernetType_Type(Integer32):
    """Custom type h3cQinQIfEthernetType based on Integer32"""
    defaultValue = 33024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cQinQIfEthernetType_Type.__name__ = "Integer32"
_H3cQinQIfEthernetType_Object = MibTableColumn
h3cQinQIfEthernetType = _H3cQinQIfEthernetType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 7, 1, 1),
    _H3cQinQIfEthernetType_Type()
)
h3cQinQIfEthernetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQinQIfEthernetType.setStatus("current")


class _H3cQinQIfSwitch_Type(H3cQinQSwitchState):
    """Custom type h3cQinQIfSwitch based on H3cQinQSwitchState"""


_H3cQinQIfSwitch_Object = MibTableColumn
h3cQinQIfSwitch = _H3cQinQIfSwitch_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 7, 1, 2),
    _H3cQinQIfSwitch_Type()
)
h3cQinQIfSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQinQIfSwitch.setStatus("current")
_H3cQinQIfRowStatus_Type = RowStatus
_H3cQinQIfRowStatus_Object = MibTableColumn
h3cQinQIfRowStatus = _H3cQinQIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 7, 1, 3),
    _H3cQinQIfRowStatus_Type()
)
h3cQinQIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQinQIfRowStatus.setStatus("current")


class _H3cQinQIfServiceTPIDValue_Type(Integer32):
    """Custom type h3cQinQIfServiceTPIDValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cQinQIfServiceTPIDValue_Type.__name__ = "Integer32"
_H3cQinQIfServiceTPIDValue_Object = MibTableColumn
h3cQinQIfServiceTPIDValue = _H3cQinQIfServiceTPIDValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 7, 1, 4),
    _H3cQinQIfServiceTPIDValue_Type()
)
h3cQinQIfServiceTPIDValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQinQIfServiceTPIDValue.setStatus("current")


class _H3cQinQIfCustomerTPIDValue_Type(Integer32):
    """Custom type h3cQinQIfCustomerTPIDValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cQinQIfCustomerTPIDValue_Type.__name__ = "Integer32"
_H3cQinQIfCustomerTPIDValue_Object = MibTableColumn
h3cQinQIfCustomerTPIDValue = _H3cQinQIfCustomerTPIDValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 7, 1, 5),
    _H3cQinQIfCustomerTPIDValue_Type()
)
h3cQinQIfCustomerTPIDValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQinQIfCustomerTPIDValue.setStatus("current")


class _H3cQinQIfUplinkSwitch_Type(H3cQinQSwitchState):
    """Custom type h3cQinQIfUplinkSwitch based on H3cQinQSwitchState"""


_H3cQinQIfUplinkSwitch_Object = MibTableColumn
h3cQinQIfUplinkSwitch = _H3cQinQIfUplinkSwitch_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 7, 1, 6),
    _H3cQinQIfUplinkSwitch_Type()
)
h3cQinQIfUplinkSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQinQIfUplinkSwitch.setStatus("current")


class _H3cQinQIfDownlinkSwitch_Type(H3cQinQSwitchState):
    """Custom type h3cQinQIfDownlinkSwitch based on H3cQinQSwitchState"""


_H3cQinQIfDownlinkSwitch_Object = MibTableColumn
h3cQinQIfDownlinkSwitch = _H3cQinQIfDownlinkSwitch_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 69, 1, 7, 1, 7),
    _H3cQinQIfDownlinkSwitch_Type()
)
h3cQinQIfDownlinkSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQinQIfDownlinkSwitch.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-QINQ-MIB",
    **{"H3cQinQSwitchState": H3cQinQSwitchState,
       "h3cQINQ": h3cQINQ,
       "h3cQinQMibObject": h3cQinQMibObject,
       "h3cQinQGlobalConfigGroup": h3cQinQGlobalConfigGroup,
       "h3cQinQBpduTunnelSwitch": h3cQinQBpduTunnelSwitch,
       "h3cQinQEthernetTypeValue": h3cQinQEthernetTypeValue,
       "h3cQinQServiceTPIDValue": h3cQinQServiceTPIDValue,
       "h3cQinQCustomerTPIDValue": h3cQinQCustomerTPIDValue,
       "h3cQinQBpduTunnelTable": h3cQinQBpduTunnelTable,
       "h3cQinQBpduTunnelEntry": h3cQinQBpduTunnelEntry,
       "h3cQinQProtocolIndex": h3cQinQProtocolIndex,
       "h3cQinQBpduRowStatus": h3cQinQBpduRowStatus,
       "h3cQinQPriorityRemarkTable": h3cQinQPriorityRemarkTable,
       "h3cQinQPriorityRemarkEntry": h3cQinQPriorityRemarkEntry,
       "h3cQinQPriorityValue": h3cQinQPriorityValue,
       "h3cQinQPriorityRemarkValue": h3cQinQPriorityRemarkValue,
       "h3cQinQPriorityRowStatus": h3cQinQPriorityRowStatus,
       "h3cQinQVidTable": h3cQinQVidTable,
       "h3cQinQVidEntry": h3cQinQVidEntry,
       "h3cQinQVlanID": h3cQinQVlanID,
       "h3cQinQInboundVidListLow": h3cQinQInboundVidListLow,
       "h3cQinQInboundVidListHigh": h3cQinQInboundVidListHigh,
       "h3cQinQVidEthernetType": h3cQinQVidEthernetType,
       "h3cQinQVidRowStatus": h3cQinQVidRowStatus,
       "h3cQinQVidSwapTable": h3cQinQVidSwapTable,
       "h3cQinQVidSwapEntry": h3cQinQVidSwapEntry,
       "h3cQinQVidSwapOld": h3cQinQVidSwapOld,
       "h3cQinQVidSwapNew": h3cQinQVidSwapNew,
       "h3cQinQVidSwapRowStatus": h3cQinQVidSwapRowStatus,
       "h3cQinQPrioritySwapTable": h3cQinQPrioritySwapTable,
       "h3cQinQPrioritySwapEntry": h3cQinQPrioritySwapEntry,
       "h3cQinQPrioritySwapOld": h3cQinQPrioritySwapOld,
       "h3cQinQPrioritySwapNew": h3cQinQPrioritySwapNew,
       "h3cQinQPrioritySwapRowStatus": h3cQinQPrioritySwapRowStatus,
       "h3cQinQIfConfigTable": h3cQinQIfConfigTable,
       "h3cQinQIfConfigEntry": h3cQinQIfConfigEntry,
       "h3cQinQIfEthernetType": h3cQinQIfEthernetType,
       "h3cQinQIfSwitch": h3cQinQIfSwitch,
       "h3cQinQIfRowStatus": h3cQinQIfRowStatus,
       "h3cQinQIfServiceTPIDValue": h3cQinQIfServiceTPIDValue,
       "h3cQinQIfCustomerTPIDValue": h3cQinQIfCustomerTPIDValue,
       "h3cQinQIfUplinkSwitch": h3cQinQIfUplinkSwitch,
       "h3cQinQIfDownlinkSwitch": h3cQinQIfDownlinkSwitch}
)
