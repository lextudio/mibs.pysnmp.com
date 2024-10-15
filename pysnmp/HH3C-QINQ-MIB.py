# SNMP MIB module (HH3C-QINQ-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-QINQ-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:37 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cQINQ = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69)
)
hh3cQINQ.setRevisions(
        ("2006-03-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cQinQSwitchState(Integer32, TextualConvention):
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

_Hh3cQinQMibObject_ObjectIdentity = ObjectIdentity
hh3cQinQMibObject = _Hh3cQinQMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1)
)
_Hh3cQinQGlobalConfigGroup_ObjectIdentity = ObjectIdentity
hh3cQinQGlobalConfigGroup = _Hh3cQinQGlobalConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 1)
)


class _Hh3cQinQBpduTunnelSwitch_Type(Hh3cQinQSwitchState):
    """Custom type hh3cQinQBpduTunnelSwitch based on Hh3cQinQSwitchState"""


_Hh3cQinQBpduTunnelSwitch_Object = MibScalar
hh3cQinQBpduTunnelSwitch = _Hh3cQinQBpduTunnelSwitch_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 1, 1),
    _Hh3cQinQBpduTunnelSwitch_Type()
)
hh3cQinQBpduTunnelSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cQinQBpduTunnelSwitch.setStatus("current")


class _Hh3cQinQEthernetTypeValue_Type(Integer32):
    """Custom type hh3cQinQEthernetTypeValue based on Integer32"""
    defaultValue = 33024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cQinQEthernetTypeValue_Type.__name__ = "Integer32"
_Hh3cQinQEthernetTypeValue_Object = MibScalar
hh3cQinQEthernetTypeValue = _Hh3cQinQEthernetTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 1, 2),
    _Hh3cQinQEthernetTypeValue_Type()
)
hh3cQinQEthernetTypeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cQinQEthernetTypeValue.setStatus("current")


class _Hh3cQinQServiceTPIDValue_Type(Integer32):
    """Custom type hh3cQinQServiceTPIDValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cQinQServiceTPIDValue_Type.__name__ = "Integer32"
_Hh3cQinQServiceTPIDValue_Object = MibScalar
hh3cQinQServiceTPIDValue = _Hh3cQinQServiceTPIDValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 1, 3),
    _Hh3cQinQServiceTPIDValue_Type()
)
hh3cQinQServiceTPIDValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cQinQServiceTPIDValue.setStatus("current")


class _Hh3cQinQCustomerTPIDValue_Type(Integer32):
    """Custom type hh3cQinQCustomerTPIDValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cQinQCustomerTPIDValue_Type.__name__ = "Integer32"
_Hh3cQinQCustomerTPIDValue_Object = MibScalar
hh3cQinQCustomerTPIDValue = _Hh3cQinQCustomerTPIDValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 1, 4),
    _Hh3cQinQCustomerTPIDValue_Type()
)
hh3cQinQCustomerTPIDValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cQinQCustomerTPIDValue.setStatus("current")
_Hh3cQinQBpduTunnelTable_Object = MibTable
hh3cQinQBpduTunnelTable = _Hh3cQinQBpduTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cQinQBpduTunnelTable.setStatus("current")
_Hh3cQinQBpduTunnelEntry_Object = MibTableRow
hh3cQinQBpduTunnelEntry = _Hh3cQinQBpduTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 2, 1)
)
hh3cQinQBpduTunnelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-QINQ-MIB", "hh3cQinQProtocolIndex"),
)
if mibBuilder.loadTexts:
    hh3cQinQBpduTunnelEntry.setStatus("current")


class _Hh3cQinQProtocolIndex_Type(Integer32):
    """Custom type hh3cQinQProtocolIndex based on Integer32"""
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
          ("gmosaic", 3),
          ("igmp", 4),
          ("stp", 2))
    )


_Hh3cQinQProtocolIndex_Type.__name__ = "Integer32"
_Hh3cQinQProtocolIndex_Object = MibTableColumn
hh3cQinQProtocolIndex = _Hh3cQinQProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 2, 1, 1),
    _Hh3cQinQProtocolIndex_Type()
)
hh3cQinQProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQinQProtocolIndex.setStatus("current")
_Hh3cQinQBpduRowStatus_Type = RowStatus
_Hh3cQinQBpduRowStatus_Object = MibTableColumn
hh3cQinQBpduRowStatus = _Hh3cQinQBpduRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 2, 1, 2),
    _Hh3cQinQBpduRowStatus_Type()
)
hh3cQinQBpduRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQinQBpduRowStatus.setStatus("current")
_Hh3cQinQPriorityRemarkTable_Object = MibTable
hh3cQinQPriorityRemarkTable = _Hh3cQinQPriorityRemarkTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cQinQPriorityRemarkTable.setStatus("current")
_Hh3cQinQPriorityRemarkEntry_Object = MibTableRow
hh3cQinQPriorityRemarkEntry = _Hh3cQinQPriorityRemarkEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 3, 1)
)
hh3cQinQPriorityRemarkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-QINQ-MIB", "hh3cQinQPriorityValue"),
)
if mibBuilder.loadTexts:
    hh3cQinQPriorityRemarkEntry.setStatus("current")


class _Hh3cQinQPriorityValue_Type(Integer32):
    """Custom type hh3cQinQPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Hh3cQinQPriorityValue_Type.__name__ = "Integer32"
_Hh3cQinQPriorityValue_Object = MibTableColumn
hh3cQinQPriorityValue = _Hh3cQinQPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 3, 1, 1),
    _Hh3cQinQPriorityValue_Type()
)
hh3cQinQPriorityValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQinQPriorityValue.setStatus("current")


class _Hh3cQinQPriorityRemarkValue_Type(Integer32):
    """Custom type hh3cQinQPriorityRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cQinQPriorityRemarkValue_Type.__name__ = "Integer32"
_Hh3cQinQPriorityRemarkValue_Object = MibTableColumn
hh3cQinQPriorityRemarkValue = _Hh3cQinQPriorityRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 3, 1, 2),
    _Hh3cQinQPriorityRemarkValue_Type()
)
hh3cQinQPriorityRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQinQPriorityRemarkValue.setStatus("current")
_Hh3cQinQPriorityRowStatus_Type = RowStatus
_Hh3cQinQPriorityRowStatus_Object = MibTableColumn
hh3cQinQPriorityRowStatus = _Hh3cQinQPriorityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 3, 1, 3),
    _Hh3cQinQPriorityRowStatus_Type()
)
hh3cQinQPriorityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQinQPriorityRowStatus.setStatus("current")
_Hh3cQinQVidTable_Object = MibTable
hh3cQinQVidTable = _Hh3cQinQVidTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cQinQVidTable.setStatus("current")
_Hh3cQinQVidEntry_Object = MibTableRow
hh3cQinQVidEntry = _Hh3cQinQVidEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 4, 1)
)
hh3cQinQVidEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-QINQ-MIB", "hh3cQinQVlanID"),
)
if mibBuilder.loadTexts:
    hh3cQinQVidEntry.setStatus("current")


class _Hh3cQinQVlanID_Type(Integer32):
    """Custom type hh3cQinQVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cQinQVlanID_Type.__name__ = "Integer32"
_Hh3cQinQVlanID_Object = MibTableColumn
hh3cQinQVlanID = _Hh3cQinQVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 4, 1, 1),
    _Hh3cQinQVlanID_Type()
)
hh3cQinQVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQinQVlanID.setStatus("current")


class _Hh3cQinQInboundVidListLow_Type(OctetString):
    """Custom type hh3cQinQInboundVidListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_Hh3cQinQInboundVidListLow_Type.__name__ = "OctetString"
_Hh3cQinQInboundVidListLow_Object = MibTableColumn
hh3cQinQInboundVidListLow = _Hh3cQinQInboundVidListLow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 4, 1, 2),
    _Hh3cQinQInboundVidListLow_Type()
)
hh3cQinQInboundVidListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQinQInboundVidListLow.setStatus("current")


class _Hh3cQinQInboundVidListHigh_Type(OctetString):
    """Custom type hh3cQinQInboundVidListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_Hh3cQinQInboundVidListHigh_Type.__name__ = "OctetString"
_Hh3cQinQInboundVidListHigh_Object = MibTableColumn
hh3cQinQInboundVidListHigh = _Hh3cQinQInboundVidListHigh_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 4, 1, 3),
    _Hh3cQinQInboundVidListHigh_Type()
)
hh3cQinQInboundVidListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQinQInboundVidListHigh.setStatus("current")


class _Hh3cQinQVidEthernetType_Type(Integer32):
    """Custom type hh3cQinQVidEthernetType based on Integer32"""
    defaultValue = 33024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cQinQVidEthernetType_Type.__name__ = "Integer32"
_Hh3cQinQVidEthernetType_Object = MibTableColumn
hh3cQinQVidEthernetType = _Hh3cQinQVidEthernetType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 4, 1, 4),
    _Hh3cQinQVidEthernetType_Type()
)
hh3cQinQVidEthernetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQinQVidEthernetType.setStatus("current")
_Hh3cQinQVidRowStatus_Type = RowStatus
_Hh3cQinQVidRowStatus_Object = MibTableColumn
hh3cQinQVidRowStatus = _Hh3cQinQVidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 4, 1, 5),
    _Hh3cQinQVidRowStatus_Type()
)
hh3cQinQVidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQinQVidRowStatus.setStatus("current")
_Hh3cQinQVidSwapTable_Object = MibTable
hh3cQinQVidSwapTable = _Hh3cQinQVidSwapTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cQinQVidSwapTable.setStatus("current")
_Hh3cQinQVidSwapEntry_Object = MibTableRow
hh3cQinQVidSwapEntry = _Hh3cQinQVidSwapEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 5, 1)
)
hh3cQinQVidSwapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-QINQ-MIB", "hh3cQinQVlanID"),
    (0, "HH3C-QINQ-MIB", "hh3cQinQVidSwapOld"),
)
if mibBuilder.loadTexts:
    hh3cQinQVidSwapEntry.setStatus("current")


class _Hh3cQinQVidSwapOld_Type(Integer32):
    """Custom type hh3cQinQVidSwapOld based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cQinQVidSwapOld_Type.__name__ = "Integer32"
_Hh3cQinQVidSwapOld_Object = MibTableColumn
hh3cQinQVidSwapOld = _Hh3cQinQVidSwapOld_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 5, 1, 1),
    _Hh3cQinQVidSwapOld_Type()
)
hh3cQinQVidSwapOld.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQinQVidSwapOld.setStatus("current")


class _Hh3cQinQVidSwapNew_Type(Integer32):
    """Custom type hh3cQinQVidSwapNew based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cQinQVidSwapNew_Type.__name__ = "Integer32"
_Hh3cQinQVidSwapNew_Object = MibTableColumn
hh3cQinQVidSwapNew = _Hh3cQinQVidSwapNew_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 5, 1, 2),
    _Hh3cQinQVidSwapNew_Type()
)
hh3cQinQVidSwapNew.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQinQVidSwapNew.setStatus("current")
_Hh3cQinQVidSwapRowStatus_Type = RowStatus
_Hh3cQinQVidSwapRowStatus_Object = MibTableColumn
hh3cQinQVidSwapRowStatus = _Hh3cQinQVidSwapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 5, 1, 3),
    _Hh3cQinQVidSwapRowStatus_Type()
)
hh3cQinQVidSwapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQinQVidSwapRowStatus.setStatus("current")
_Hh3cQinQPrioritySwapTable_Object = MibTable
hh3cQinQPrioritySwapTable = _Hh3cQinQPrioritySwapTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cQinQPrioritySwapTable.setStatus("current")
_Hh3cQinQPrioritySwapEntry_Object = MibTableRow
hh3cQinQPrioritySwapEntry = _Hh3cQinQPrioritySwapEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 6, 1)
)
hh3cQinQPrioritySwapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-QINQ-MIB", "hh3cQinQVlanID"),
    (0, "HH3C-QINQ-MIB", "hh3cQinQPrioritySwapOld"),
)
if mibBuilder.loadTexts:
    hh3cQinQPrioritySwapEntry.setStatus("current")


class _Hh3cQinQPrioritySwapOld_Type(Integer32):
    """Custom type hh3cQinQPrioritySwapOld based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Hh3cQinQPrioritySwapOld_Type.__name__ = "Integer32"
_Hh3cQinQPrioritySwapOld_Object = MibTableColumn
hh3cQinQPrioritySwapOld = _Hh3cQinQPrioritySwapOld_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 6, 1, 1),
    _Hh3cQinQPrioritySwapOld_Type()
)
hh3cQinQPrioritySwapOld.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQinQPrioritySwapOld.setStatus("current")


class _Hh3cQinQPrioritySwapNew_Type(Integer32):
    """Custom type hh3cQinQPrioritySwapNew based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cQinQPrioritySwapNew_Type.__name__ = "Integer32"
_Hh3cQinQPrioritySwapNew_Object = MibTableColumn
hh3cQinQPrioritySwapNew = _Hh3cQinQPrioritySwapNew_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 6, 1, 2),
    _Hh3cQinQPrioritySwapNew_Type()
)
hh3cQinQPrioritySwapNew.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQinQPrioritySwapNew.setStatus("current")
_Hh3cQinQPrioritySwapRowStatus_Type = RowStatus
_Hh3cQinQPrioritySwapRowStatus_Object = MibTableColumn
hh3cQinQPrioritySwapRowStatus = _Hh3cQinQPrioritySwapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 6, 1, 3),
    _Hh3cQinQPrioritySwapRowStatus_Type()
)
hh3cQinQPrioritySwapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQinQPrioritySwapRowStatus.setStatus("current")
_Hh3cQinQIfConfigTable_Object = MibTable
hh3cQinQIfConfigTable = _Hh3cQinQIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 7)
)
if mibBuilder.loadTexts:
    hh3cQinQIfConfigTable.setStatus("current")
_Hh3cQinQIfConfigEntry_Object = MibTableRow
hh3cQinQIfConfigEntry = _Hh3cQinQIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 7, 1)
)
hh3cQinQIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cQinQIfConfigEntry.setStatus("current")


class _Hh3cQinQIfEthernetType_Type(Integer32):
    """Custom type hh3cQinQIfEthernetType based on Integer32"""
    defaultValue = 33024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cQinQIfEthernetType_Type.__name__ = "Integer32"
_Hh3cQinQIfEthernetType_Object = MibTableColumn
hh3cQinQIfEthernetType = _Hh3cQinQIfEthernetType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 7, 1, 1),
    _Hh3cQinQIfEthernetType_Type()
)
hh3cQinQIfEthernetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQinQIfEthernetType.setStatus("current")


class _Hh3cQinQIfSwitch_Type(Hh3cQinQSwitchState):
    """Custom type hh3cQinQIfSwitch based on Hh3cQinQSwitchState"""


_Hh3cQinQIfSwitch_Object = MibTableColumn
hh3cQinQIfSwitch = _Hh3cQinQIfSwitch_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 7, 1, 2),
    _Hh3cQinQIfSwitch_Type()
)
hh3cQinQIfSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQinQIfSwitch.setStatus("current")
_Hh3cQinQIfRowStatus_Type = RowStatus
_Hh3cQinQIfRowStatus_Object = MibTableColumn
hh3cQinQIfRowStatus = _Hh3cQinQIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 7, 1, 3),
    _Hh3cQinQIfRowStatus_Type()
)
hh3cQinQIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQinQIfRowStatus.setStatus("current")


class _Hh3cQinQIfServiceTPIDValue_Type(Integer32):
    """Custom type hh3cQinQIfServiceTPIDValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cQinQIfServiceTPIDValue_Type.__name__ = "Integer32"
_Hh3cQinQIfServiceTPIDValue_Object = MibTableColumn
hh3cQinQIfServiceTPIDValue = _Hh3cQinQIfServiceTPIDValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 7, 1, 4),
    _Hh3cQinQIfServiceTPIDValue_Type()
)
hh3cQinQIfServiceTPIDValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQinQIfServiceTPIDValue.setStatus("current")


class _Hh3cQinQIfCustomerTPIDValue_Type(Integer32):
    """Custom type hh3cQinQIfCustomerTPIDValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cQinQIfCustomerTPIDValue_Type.__name__ = "Integer32"
_Hh3cQinQIfCustomerTPIDValue_Object = MibTableColumn
hh3cQinQIfCustomerTPIDValue = _Hh3cQinQIfCustomerTPIDValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 7, 1, 5),
    _Hh3cQinQIfCustomerTPIDValue_Type()
)
hh3cQinQIfCustomerTPIDValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQinQIfCustomerTPIDValue.setStatus("current")


class _Hh3cQinQIfUplinkSwitch_Type(Hh3cQinQSwitchState):
    """Custom type hh3cQinQIfUplinkSwitch based on Hh3cQinQSwitchState"""


_Hh3cQinQIfUplinkSwitch_Object = MibTableColumn
hh3cQinQIfUplinkSwitch = _Hh3cQinQIfUplinkSwitch_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 7, 1, 6),
    _Hh3cQinQIfUplinkSwitch_Type()
)
hh3cQinQIfUplinkSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQinQIfUplinkSwitch.setStatus("current")


class _Hh3cQinQIfDownlinkSwitch_Type(Hh3cQinQSwitchState):
    """Custom type hh3cQinQIfDownlinkSwitch based on Hh3cQinQSwitchState"""


_Hh3cQinQIfDownlinkSwitch_Object = MibTableColumn
hh3cQinQIfDownlinkSwitch = _Hh3cQinQIfDownlinkSwitch_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69, 1, 7, 1, 7),
    _Hh3cQinQIfDownlinkSwitch_Type()
)
hh3cQinQIfDownlinkSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQinQIfDownlinkSwitch.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-QINQ-MIB",
    **{"Hh3cQinQSwitchState": Hh3cQinQSwitchState,
       "hh3cQINQ": hh3cQINQ,
       "hh3cQinQMibObject": hh3cQinQMibObject,
       "hh3cQinQGlobalConfigGroup": hh3cQinQGlobalConfigGroup,
       "hh3cQinQBpduTunnelSwitch": hh3cQinQBpduTunnelSwitch,
       "hh3cQinQEthernetTypeValue": hh3cQinQEthernetTypeValue,
       "hh3cQinQServiceTPIDValue": hh3cQinQServiceTPIDValue,
       "hh3cQinQCustomerTPIDValue": hh3cQinQCustomerTPIDValue,
       "hh3cQinQBpduTunnelTable": hh3cQinQBpduTunnelTable,
       "hh3cQinQBpduTunnelEntry": hh3cQinQBpduTunnelEntry,
       "hh3cQinQProtocolIndex": hh3cQinQProtocolIndex,
       "hh3cQinQBpduRowStatus": hh3cQinQBpduRowStatus,
       "hh3cQinQPriorityRemarkTable": hh3cQinQPriorityRemarkTable,
       "hh3cQinQPriorityRemarkEntry": hh3cQinQPriorityRemarkEntry,
       "hh3cQinQPriorityValue": hh3cQinQPriorityValue,
       "hh3cQinQPriorityRemarkValue": hh3cQinQPriorityRemarkValue,
       "hh3cQinQPriorityRowStatus": hh3cQinQPriorityRowStatus,
       "hh3cQinQVidTable": hh3cQinQVidTable,
       "hh3cQinQVidEntry": hh3cQinQVidEntry,
       "hh3cQinQVlanID": hh3cQinQVlanID,
       "hh3cQinQInboundVidListLow": hh3cQinQInboundVidListLow,
       "hh3cQinQInboundVidListHigh": hh3cQinQInboundVidListHigh,
       "hh3cQinQVidEthernetType": hh3cQinQVidEthernetType,
       "hh3cQinQVidRowStatus": hh3cQinQVidRowStatus,
       "hh3cQinQVidSwapTable": hh3cQinQVidSwapTable,
       "hh3cQinQVidSwapEntry": hh3cQinQVidSwapEntry,
       "hh3cQinQVidSwapOld": hh3cQinQVidSwapOld,
       "hh3cQinQVidSwapNew": hh3cQinQVidSwapNew,
       "hh3cQinQVidSwapRowStatus": hh3cQinQVidSwapRowStatus,
       "hh3cQinQPrioritySwapTable": hh3cQinQPrioritySwapTable,
       "hh3cQinQPrioritySwapEntry": hh3cQinQPrioritySwapEntry,
       "hh3cQinQPrioritySwapOld": hh3cQinQPrioritySwapOld,
       "hh3cQinQPrioritySwapNew": hh3cQinQPrioritySwapNew,
       "hh3cQinQPrioritySwapRowStatus": hh3cQinQPrioritySwapRowStatus,
       "hh3cQinQIfConfigTable": hh3cQinQIfConfigTable,
       "hh3cQinQIfConfigEntry": hh3cQinQIfConfigEntry,
       "hh3cQinQIfEthernetType": hh3cQinQIfEthernetType,
       "hh3cQinQIfSwitch": hh3cQinQIfSwitch,
       "hh3cQinQIfRowStatus": hh3cQinQIfRowStatus,
       "hh3cQinQIfServiceTPIDValue": hh3cQinQIfServiceTPIDValue,
       "hh3cQinQIfCustomerTPIDValue": hh3cQinQIfCustomerTPIDValue,
       "hh3cQinQIfUplinkSwitch": hh3cQinQIfUplinkSwitch,
       "hh3cQinQIfDownlinkSwitch": hh3cQinQIfDownlinkSwitch}
)
