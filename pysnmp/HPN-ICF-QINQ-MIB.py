# SNMP MIB module (HPN-ICF-QINQ-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-QINQ-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:35 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfQINQ = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69)
)
hpnicfQINQ.setRevisions(
        ("2006-03-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfQinQSwitchState(Integer32, TextualConvention):
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

_HpnicfQinQMibObject_ObjectIdentity = ObjectIdentity
hpnicfQinQMibObject = _HpnicfQinQMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1)
)
_HpnicfQinQGlobalConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfQinQGlobalConfigGroup = _HpnicfQinQGlobalConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 1)
)


class _HpnicfQinQBpduTunnelSwitch_Type(HpnicfQinQSwitchState):
    """Custom type hpnicfQinQBpduTunnelSwitch based on HpnicfQinQSwitchState"""


_HpnicfQinQBpduTunnelSwitch_Object = MibScalar
hpnicfQinQBpduTunnelSwitch = _HpnicfQinQBpduTunnelSwitch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 1, 1),
    _HpnicfQinQBpduTunnelSwitch_Type()
)
hpnicfQinQBpduTunnelSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfQinQBpduTunnelSwitch.setStatus("current")


class _HpnicfQinQEthernetTypeValue_Type(Integer32):
    """Custom type hpnicfQinQEthernetTypeValue based on Integer32"""
    defaultValue = 33024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfQinQEthernetTypeValue_Type.__name__ = "Integer32"
_HpnicfQinQEthernetTypeValue_Object = MibScalar
hpnicfQinQEthernetTypeValue = _HpnicfQinQEthernetTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 1, 2),
    _HpnicfQinQEthernetTypeValue_Type()
)
hpnicfQinQEthernetTypeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfQinQEthernetTypeValue.setStatus("current")


class _HpnicfQinQServiceTPIDValue_Type(Integer32):
    """Custom type hpnicfQinQServiceTPIDValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfQinQServiceTPIDValue_Type.__name__ = "Integer32"
_HpnicfQinQServiceTPIDValue_Object = MibScalar
hpnicfQinQServiceTPIDValue = _HpnicfQinQServiceTPIDValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 1, 3),
    _HpnicfQinQServiceTPIDValue_Type()
)
hpnicfQinQServiceTPIDValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfQinQServiceTPIDValue.setStatus("current")


class _HpnicfQinQCustomerTPIDValue_Type(Integer32):
    """Custom type hpnicfQinQCustomerTPIDValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfQinQCustomerTPIDValue_Type.__name__ = "Integer32"
_HpnicfQinQCustomerTPIDValue_Object = MibScalar
hpnicfQinQCustomerTPIDValue = _HpnicfQinQCustomerTPIDValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 1, 4),
    _HpnicfQinQCustomerTPIDValue_Type()
)
hpnicfQinQCustomerTPIDValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfQinQCustomerTPIDValue.setStatus("current")
_HpnicfQinQBpduTunnelTable_Object = MibTable
hpnicfQinQBpduTunnelTable = _HpnicfQinQBpduTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfQinQBpduTunnelTable.setStatus("current")
_HpnicfQinQBpduTunnelEntry_Object = MibTableRow
hpnicfQinQBpduTunnelEntry = _HpnicfQinQBpduTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 2, 1)
)
hpnicfQinQBpduTunnelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-QINQ-MIB", "hpnicfQinQProtocolIndex"),
)
if mibBuilder.loadTexts:
    hpnicfQinQBpduTunnelEntry.setStatus("current")


class _HpnicfQinQProtocolIndex_Type(Integer32):
    """Custom type hpnicfQinQProtocolIndex based on Integer32"""
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


_HpnicfQinQProtocolIndex_Type.__name__ = "Integer32"
_HpnicfQinQProtocolIndex_Object = MibTableColumn
hpnicfQinQProtocolIndex = _HpnicfQinQProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 2, 1, 1),
    _HpnicfQinQProtocolIndex_Type()
)
hpnicfQinQProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQinQProtocolIndex.setStatus("current")
_HpnicfQinQBpduRowStatus_Type = RowStatus
_HpnicfQinQBpduRowStatus_Object = MibTableColumn
hpnicfQinQBpduRowStatus = _HpnicfQinQBpduRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 2, 1, 2),
    _HpnicfQinQBpduRowStatus_Type()
)
hpnicfQinQBpduRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQinQBpduRowStatus.setStatus("current")
_HpnicfQinQPriorityRemarkTable_Object = MibTable
hpnicfQinQPriorityRemarkTable = _HpnicfQinQPriorityRemarkTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfQinQPriorityRemarkTable.setStatus("current")
_HpnicfQinQPriorityRemarkEntry_Object = MibTableRow
hpnicfQinQPriorityRemarkEntry = _HpnicfQinQPriorityRemarkEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 3, 1)
)
hpnicfQinQPriorityRemarkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-QINQ-MIB", "hpnicfQinQPriorityValue"),
)
if mibBuilder.loadTexts:
    hpnicfQinQPriorityRemarkEntry.setStatus("current")


class _HpnicfQinQPriorityValue_Type(Integer32):
    """Custom type hpnicfQinQPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HpnicfQinQPriorityValue_Type.__name__ = "Integer32"
_HpnicfQinQPriorityValue_Object = MibTableColumn
hpnicfQinQPriorityValue = _HpnicfQinQPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 3, 1, 1),
    _HpnicfQinQPriorityValue_Type()
)
hpnicfQinQPriorityValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQinQPriorityValue.setStatus("current")


class _HpnicfQinQPriorityRemarkValue_Type(Integer32):
    """Custom type hpnicfQinQPriorityRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfQinQPriorityRemarkValue_Type.__name__ = "Integer32"
_HpnicfQinQPriorityRemarkValue_Object = MibTableColumn
hpnicfQinQPriorityRemarkValue = _HpnicfQinQPriorityRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 3, 1, 2),
    _HpnicfQinQPriorityRemarkValue_Type()
)
hpnicfQinQPriorityRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQinQPriorityRemarkValue.setStatus("current")
_HpnicfQinQPriorityRowStatus_Type = RowStatus
_HpnicfQinQPriorityRowStatus_Object = MibTableColumn
hpnicfQinQPriorityRowStatus = _HpnicfQinQPriorityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 3, 1, 3),
    _HpnicfQinQPriorityRowStatus_Type()
)
hpnicfQinQPriorityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQinQPriorityRowStatus.setStatus("current")
_HpnicfQinQVidTable_Object = MibTable
hpnicfQinQVidTable = _HpnicfQinQVidTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfQinQVidTable.setStatus("current")
_HpnicfQinQVidEntry_Object = MibTableRow
hpnicfQinQVidEntry = _HpnicfQinQVidEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 4, 1)
)
hpnicfQinQVidEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-QINQ-MIB", "hpnicfQinQVlanID"),
)
if mibBuilder.loadTexts:
    hpnicfQinQVidEntry.setStatus("current")


class _HpnicfQinQVlanID_Type(Integer32):
    """Custom type hpnicfQinQVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpnicfQinQVlanID_Type.__name__ = "Integer32"
_HpnicfQinQVlanID_Object = MibTableColumn
hpnicfQinQVlanID = _HpnicfQinQVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 4, 1, 1),
    _HpnicfQinQVlanID_Type()
)
hpnicfQinQVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQinQVlanID.setStatus("current")


class _HpnicfQinQInboundVidListLow_Type(OctetString):
    """Custom type hpnicfQinQInboundVidListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HpnicfQinQInboundVidListLow_Type.__name__ = "OctetString"
_HpnicfQinQInboundVidListLow_Object = MibTableColumn
hpnicfQinQInboundVidListLow = _HpnicfQinQInboundVidListLow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 4, 1, 2),
    _HpnicfQinQInboundVidListLow_Type()
)
hpnicfQinQInboundVidListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQinQInboundVidListLow.setStatus("current")


class _HpnicfQinQInboundVidListHigh_Type(OctetString):
    """Custom type hpnicfQinQInboundVidListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HpnicfQinQInboundVidListHigh_Type.__name__ = "OctetString"
_HpnicfQinQInboundVidListHigh_Object = MibTableColumn
hpnicfQinQInboundVidListHigh = _HpnicfQinQInboundVidListHigh_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 4, 1, 3),
    _HpnicfQinQInboundVidListHigh_Type()
)
hpnicfQinQInboundVidListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQinQInboundVidListHigh.setStatus("current")


class _HpnicfQinQVidEthernetType_Type(Integer32):
    """Custom type hpnicfQinQVidEthernetType based on Integer32"""
    defaultValue = 33024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfQinQVidEthernetType_Type.__name__ = "Integer32"
_HpnicfQinQVidEthernetType_Object = MibTableColumn
hpnicfQinQVidEthernetType = _HpnicfQinQVidEthernetType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 4, 1, 4),
    _HpnicfQinQVidEthernetType_Type()
)
hpnicfQinQVidEthernetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQinQVidEthernetType.setStatus("current")
_HpnicfQinQVidRowStatus_Type = RowStatus
_HpnicfQinQVidRowStatus_Object = MibTableColumn
hpnicfQinQVidRowStatus = _HpnicfQinQVidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 4, 1, 5),
    _HpnicfQinQVidRowStatus_Type()
)
hpnicfQinQVidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQinQVidRowStatus.setStatus("current")
_HpnicfQinQVidSwapTable_Object = MibTable
hpnicfQinQVidSwapTable = _HpnicfQinQVidSwapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 5)
)
if mibBuilder.loadTexts:
    hpnicfQinQVidSwapTable.setStatus("current")
_HpnicfQinQVidSwapEntry_Object = MibTableRow
hpnicfQinQVidSwapEntry = _HpnicfQinQVidSwapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 5, 1)
)
hpnicfQinQVidSwapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-QINQ-MIB", "hpnicfQinQVlanID"),
    (0, "HPN-ICF-QINQ-MIB", "hpnicfQinQVidSwapOld"),
)
if mibBuilder.loadTexts:
    hpnicfQinQVidSwapEntry.setStatus("current")


class _HpnicfQinQVidSwapOld_Type(Integer32):
    """Custom type hpnicfQinQVidSwapOld based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpnicfQinQVidSwapOld_Type.__name__ = "Integer32"
_HpnicfQinQVidSwapOld_Object = MibTableColumn
hpnicfQinQVidSwapOld = _HpnicfQinQVidSwapOld_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 5, 1, 1),
    _HpnicfQinQVidSwapOld_Type()
)
hpnicfQinQVidSwapOld.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQinQVidSwapOld.setStatus("current")


class _HpnicfQinQVidSwapNew_Type(Integer32):
    """Custom type hpnicfQinQVidSwapNew based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpnicfQinQVidSwapNew_Type.__name__ = "Integer32"
_HpnicfQinQVidSwapNew_Object = MibTableColumn
hpnicfQinQVidSwapNew = _HpnicfQinQVidSwapNew_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 5, 1, 2),
    _HpnicfQinQVidSwapNew_Type()
)
hpnicfQinQVidSwapNew.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQinQVidSwapNew.setStatus("current")
_HpnicfQinQVidSwapRowStatus_Type = RowStatus
_HpnicfQinQVidSwapRowStatus_Object = MibTableColumn
hpnicfQinQVidSwapRowStatus = _HpnicfQinQVidSwapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 5, 1, 3),
    _HpnicfQinQVidSwapRowStatus_Type()
)
hpnicfQinQVidSwapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQinQVidSwapRowStatus.setStatus("current")
_HpnicfQinQPrioritySwapTable_Object = MibTable
hpnicfQinQPrioritySwapTable = _HpnicfQinQPrioritySwapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 6)
)
if mibBuilder.loadTexts:
    hpnicfQinQPrioritySwapTable.setStatus("current")
_HpnicfQinQPrioritySwapEntry_Object = MibTableRow
hpnicfQinQPrioritySwapEntry = _HpnicfQinQPrioritySwapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 6, 1)
)
hpnicfQinQPrioritySwapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-QINQ-MIB", "hpnicfQinQVlanID"),
    (0, "HPN-ICF-QINQ-MIB", "hpnicfQinQPrioritySwapOld"),
)
if mibBuilder.loadTexts:
    hpnicfQinQPrioritySwapEntry.setStatus("current")


class _HpnicfQinQPrioritySwapOld_Type(Integer32):
    """Custom type hpnicfQinQPrioritySwapOld based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HpnicfQinQPrioritySwapOld_Type.__name__ = "Integer32"
_HpnicfQinQPrioritySwapOld_Object = MibTableColumn
hpnicfQinQPrioritySwapOld = _HpnicfQinQPrioritySwapOld_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 6, 1, 1),
    _HpnicfQinQPrioritySwapOld_Type()
)
hpnicfQinQPrioritySwapOld.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQinQPrioritySwapOld.setStatus("current")


class _HpnicfQinQPrioritySwapNew_Type(Integer32):
    """Custom type hpnicfQinQPrioritySwapNew based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfQinQPrioritySwapNew_Type.__name__ = "Integer32"
_HpnicfQinQPrioritySwapNew_Object = MibTableColumn
hpnicfQinQPrioritySwapNew = _HpnicfQinQPrioritySwapNew_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 6, 1, 2),
    _HpnicfQinQPrioritySwapNew_Type()
)
hpnicfQinQPrioritySwapNew.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQinQPrioritySwapNew.setStatus("current")
_HpnicfQinQPrioritySwapRowStatus_Type = RowStatus
_HpnicfQinQPrioritySwapRowStatus_Object = MibTableColumn
hpnicfQinQPrioritySwapRowStatus = _HpnicfQinQPrioritySwapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 6, 1, 3),
    _HpnicfQinQPrioritySwapRowStatus_Type()
)
hpnicfQinQPrioritySwapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQinQPrioritySwapRowStatus.setStatus("current")
_HpnicfQinQIfConfigTable_Object = MibTable
hpnicfQinQIfConfigTable = _HpnicfQinQIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 7)
)
if mibBuilder.loadTexts:
    hpnicfQinQIfConfigTable.setStatus("current")
_HpnicfQinQIfConfigEntry_Object = MibTableRow
hpnicfQinQIfConfigEntry = _HpnicfQinQIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 7, 1)
)
hpnicfQinQIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfQinQIfConfigEntry.setStatus("current")


class _HpnicfQinQIfEthernetType_Type(Integer32):
    """Custom type hpnicfQinQIfEthernetType based on Integer32"""
    defaultValue = 33024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfQinQIfEthernetType_Type.__name__ = "Integer32"
_HpnicfQinQIfEthernetType_Object = MibTableColumn
hpnicfQinQIfEthernetType = _HpnicfQinQIfEthernetType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 7, 1, 1),
    _HpnicfQinQIfEthernetType_Type()
)
hpnicfQinQIfEthernetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQinQIfEthernetType.setStatus("current")


class _HpnicfQinQIfSwitch_Type(HpnicfQinQSwitchState):
    """Custom type hpnicfQinQIfSwitch based on HpnicfQinQSwitchState"""


_HpnicfQinQIfSwitch_Object = MibTableColumn
hpnicfQinQIfSwitch = _HpnicfQinQIfSwitch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 7, 1, 2),
    _HpnicfQinQIfSwitch_Type()
)
hpnicfQinQIfSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQinQIfSwitch.setStatus("current")
_HpnicfQinQIfRowStatus_Type = RowStatus
_HpnicfQinQIfRowStatus_Object = MibTableColumn
hpnicfQinQIfRowStatus = _HpnicfQinQIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 7, 1, 3),
    _HpnicfQinQIfRowStatus_Type()
)
hpnicfQinQIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQinQIfRowStatus.setStatus("current")


class _HpnicfQinQIfServiceTPIDValue_Type(Integer32):
    """Custom type hpnicfQinQIfServiceTPIDValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfQinQIfServiceTPIDValue_Type.__name__ = "Integer32"
_HpnicfQinQIfServiceTPIDValue_Object = MibTableColumn
hpnicfQinQIfServiceTPIDValue = _HpnicfQinQIfServiceTPIDValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 7, 1, 4),
    _HpnicfQinQIfServiceTPIDValue_Type()
)
hpnicfQinQIfServiceTPIDValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQinQIfServiceTPIDValue.setStatus("current")


class _HpnicfQinQIfCustomerTPIDValue_Type(Integer32):
    """Custom type hpnicfQinQIfCustomerTPIDValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfQinQIfCustomerTPIDValue_Type.__name__ = "Integer32"
_HpnicfQinQIfCustomerTPIDValue_Object = MibTableColumn
hpnicfQinQIfCustomerTPIDValue = _HpnicfQinQIfCustomerTPIDValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 7, 1, 5),
    _HpnicfQinQIfCustomerTPIDValue_Type()
)
hpnicfQinQIfCustomerTPIDValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQinQIfCustomerTPIDValue.setStatus("current")


class _HpnicfQinQIfUplinkSwitch_Type(HpnicfQinQSwitchState):
    """Custom type hpnicfQinQIfUplinkSwitch based on HpnicfQinQSwitchState"""


_HpnicfQinQIfUplinkSwitch_Object = MibTableColumn
hpnicfQinQIfUplinkSwitch = _HpnicfQinQIfUplinkSwitch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 7, 1, 6),
    _HpnicfQinQIfUplinkSwitch_Type()
)
hpnicfQinQIfUplinkSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQinQIfUplinkSwitch.setStatus("current")


class _HpnicfQinQIfDownlinkSwitch_Type(HpnicfQinQSwitchState):
    """Custom type hpnicfQinQIfDownlinkSwitch based on HpnicfQinQSwitchState"""


_HpnicfQinQIfDownlinkSwitch_Object = MibTableColumn
hpnicfQinQIfDownlinkSwitch = _HpnicfQinQIfDownlinkSwitch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69, 1, 7, 1, 7),
    _HpnicfQinQIfDownlinkSwitch_Type()
)
hpnicfQinQIfDownlinkSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQinQIfDownlinkSwitch.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-QINQ-MIB",
    **{"HpnicfQinQSwitchState": HpnicfQinQSwitchState,
       "hpnicfQINQ": hpnicfQINQ,
       "hpnicfQinQMibObject": hpnicfQinQMibObject,
       "hpnicfQinQGlobalConfigGroup": hpnicfQinQGlobalConfigGroup,
       "hpnicfQinQBpduTunnelSwitch": hpnicfQinQBpduTunnelSwitch,
       "hpnicfQinQEthernetTypeValue": hpnicfQinQEthernetTypeValue,
       "hpnicfQinQServiceTPIDValue": hpnicfQinQServiceTPIDValue,
       "hpnicfQinQCustomerTPIDValue": hpnicfQinQCustomerTPIDValue,
       "hpnicfQinQBpduTunnelTable": hpnicfQinQBpduTunnelTable,
       "hpnicfQinQBpduTunnelEntry": hpnicfQinQBpduTunnelEntry,
       "hpnicfQinQProtocolIndex": hpnicfQinQProtocolIndex,
       "hpnicfQinQBpduRowStatus": hpnicfQinQBpduRowStatus,
       "hpnicfQinQPriorityRemarkTable": hpnicfQinQPriorityRemarkTable,
       "hpnicfQinQPriorityRemarkEntry": hpnicfQinQPriorityRemarkEntry,
       "hpnicfQinQPriorityValue": hpnicfQinQPriorityValue,
       "hpnicfQinQPriorityRemarkValue": hpnicfQinQPriorityRemarkValue,
       "hpnicfQinQPriorityRowStatus": hpnicfQinQPriorityRowStatus,
       "hpnicfQinQVidTable": hpnicfQinQVidTable,
       "hpnicfQinQVidEntry": hpnicfQinQVidEntry,
       "hpnicfQinQVlanID": hpnicfQinQVlanID,
       "hpnicfQinQInboundVidListLow": hpnicfQinQInboundVidListLow,
       "hpnicfQinQInboundVidListHigh": hpnicfQinQInboundVidListHigh,
       "hpnicfQinQVidEthernetType": hpnicfQinQVidEthernetType,
       "hpnicfQinQVidRowStatus": hpnicfQinQVidRowStatus,
       "hpnicfQinQVidSwapTable": hpnicfQinQVidSwapTable,
       "hpnicfQinQVidSwapEntry": hpnicfQinQVidSwapEntry,
       "hpnicfQinQVidSwapOld": hpnicfQinQVidSwapOld,
       "hpnicfQinQVidSwapNew": hpnicfQinQVidSwapNew,
       "hpnicfQinQVidSwapRowStatus": hpnicfQinQVidSwapRowStatus,
       "hpnicfQinQPrioritySwapTable": hpnicfQinQPrioritySwapTable,
       "hpnicfQinQPrioritySwapEntry": hpnicfQinQPrioritySwapEntry,
       "hpnicfQinQPrioritySwapOld": hpnicfQinQPrioritySwapOld,
       "hpnicfQinQPrioritySwapNew": hpnicfQinQPrioritySwapNew,
       "hpnicfQinQPrioritySwapRowStatus": hpnicfQinQPrioritySwapRowStatus,
       "hpnicfQinQIfConfigTable": hpnicfQinQIfConfigTable,
       "hpnicfQinQIfConfigEntry": hpnicfQinQIfConfigEntry,
       "hpnicfQinQIfEthernetType": hpnicfQinQIfEthernetType,
       "hpnicfQinQIfSwitch": hpnicfQinQIfSwitch,
       "hpnicfQinQIfRowStatus": hpnicfQinQIfRowStatus,
       "hpnicfQinQIfServiceTPIDValue": hpnicfQinQIfServiceTPIDValue,
       "hpnicfQinQIfCustomerTPIDValue": hpnicfQinQIfCustomerTPIDValue,
       "hpnicfQinQIfUplinkSwitch": hpnicfQinQIfUplinkSwitch,
       "hpnicfQinQIfDownlinkSwitch": hpnicfQinQIfDownlinkSwitch}
)
