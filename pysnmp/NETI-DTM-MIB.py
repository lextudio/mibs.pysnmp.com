# SNMP MIB module (NETI-DTM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETI-DTM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:30 2024
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

(FaultStatus,
 netiExperimentalGeneric) = mibBuilder.importSymbols(
    "NETI-COMMON-MIB",
    "FaultStatus",
    "netiExperimentalGeneric")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

netiDTMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4)
)
netiDTMMIB.setRevisions(
        ("2013-11-12 08:00",
         "2013-09-10 13:00",
         "2010-09-01 14:00",
         "2010-03-03 09:00",
         "2009-06-25 14:00",
         "2008-02-06 17:00",
         "2006-08-22 10:00",
         "2006-05-16 13:00",
         "2004-09-29 00:00",
         "2003-02-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DtmAddress(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x."
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class DtmSourceRoute(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x.1x.1x.1x.1x.1x.1x.1x 1x:1x"


# MIB Managed Objects in the order of their OIDs

_NetiDTMMIBObjects_ObjectIdentity = ObjectIdentity
netiDTMMIBObjects = _NetiDTMMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1)
)
_DtmAddrGroup_ObjectIdentity = ObjectIdentity
dtmAddrGroup = _DtmAddrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 1)
)
_DtmAddrTable_Object = MibTable
dtmAddrTable = _DtmAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dtmAddrTable.setStatus("current")
_DtmAddrEntry_Object = MibTableRow
dtmAddrEntry = _DtmAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 1, 1, 1)
)
dtmAddrEntry.setIndexNames(
    (0, "NETI-DTM-MIB", "dtmAddrEntryIndex"),
)
if mibBuilder.loadTexts:
    dtmAddrEntry.setStatus("current")


class _DtmAddrEntryIndex_Type(Unsigned32):
    """Custom type dtmAddrEntryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DtmAddrEntryIndex_Type.__name__ = "Unsigned32"
_DtmAddrEntryIndex_Object = MibTableColumn
dtmAddrEntryIndex = _DtmAddrEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 1, 1, 1, 1),
    _DtmAddrEntryIndex_Type()
)
dtmAddrEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmAddrEntryIndex.setStatus("current")
_DtmAddrEntryAddr_Type = DtmAddress
_DtmAddrEntryAddr_Object = MibTableColumn
dtmAddrEntryAddr = _DtmAddrEntryAddr_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 1, 1, 1, 2),
    _DtmAddrEntryAddr_Type()
)
dtmAddrEntryAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtmAddrEntryAddr.setStatus("current")


class _DtmAddrEntryIsAlias_Type(TruthValue):
    """Custom type dtmAddrEntryIsAlias based on TruthValue"""


_DtmAddrEntryIsAlias_Object = MibTableColumn
dtmAddrEntryIsAlias = _DtmAddrEntryIsAlias_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 1, 1, 1, 3),
    _DtmAddrEntryIsAlias_Type()
)
dtmAddrEntryIsAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtmAddrEntryIsAlias.setStatus("current")


class _DtmAddrEntryAddrType_Type(Integer32):
    """Custom type dtmAddrEntryAddrType based on Integer32"""
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
        *(("global", 5),
          ("local", 3),
          ("loopback", 2),
          ("multicast", 4),
          ("unspecified", 1))
    )


_DtmAddrEntryAddrType_Type.__name__ = "Integer32"
_DtmAddrEntryAddrType_Object = MibTableColumn
dtmAddrEntryAddrType = _DtmAddrEntryAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 1, 1, 1, 4),
    _DtmAddrEntryAddrType_Type()
)
dtmAddrEntryAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmAddrEntryAddrType.setStatus("current")
_DtmAddrEntryRowStatus_Type = RowStatus
_DtmAddrEntryRowStatus_Object = MibTableColumn
dtmAddrEntryRowStatus = _DtmAddrEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 1, 1, 1, 5),
    _DtmAddrEntryRowStatus_Type()
)
dtmAddrEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtmAddrEntryRowStatus.setStatus("current")
_DtmHostsTable_Object = MibTable
dtmHostsTable = _DtmHostsTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dtmHostsTable.setStatus("current")
_DtmHostsEntry_Object = MibTableRow
dtmHostsEntry = _DtmHostsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 1, 2, 1)
)
dtmHostsEntry.setIndexNames(
    (0, "NETI-DTM-MIB", "dtmHostsEntryIndex"),
)
if mibBuilder.loadTexts:
    dtmHostsEntry.setStatus("current")


class _DtmHostsEntryIndex_Type(Unsigned32):
    """Custom type dtmHostsEntryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DtmHostsEntryIndex_Type.__name__ = "Unsigned32"
_DtmHostsEntryIndex_Object = MibTableColumn
dtmHostsEntryIndex = _DtmHostsEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 1, 2, 1, 1),
    _DtmHostsEntryIndex_Type()
)
dtmHostsEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dtmHostsEntryIndex.setStatus("current")
_DtmHostsEntryAddr_Type = DtmAddress
_DtmHostsEntryAddr_Object = MibTableColumn
dtmHostsEntryAddr = _DtmHostsEntryAddr_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 1, 2, 1, 2),
    _DtmHostsEntryAddr_Type()
)
dtmHostsEntryAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtmHostsEntryAddr.setStatus("current")
_DtmHostsEntryName_Type = DisplayString
_DtmHostsEntryName_Object = MibTableColumn
dtmHostsEntryName = _DtmHostsEntryName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 1, 2, 1, 3),
    _DtmHostsEntryName_Type()
)
dtmHostsEntryName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtmHostsEntryName.setStatus("current")
_DtmHostsEntryRowStatus_Type = RowStatus
_DtmHostsEntryRowStatus_Object = MibTableColumn
dtmHostsEntryRowStatus = _DtmHostsEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 1, 2, 1, 4),
    _DtmHostsEntryRowStatus_Type()
)
dtmHostsEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtmHostsEntryRowStatus.setStatus("current")
_DtmIfGroup_ObjectIdentity = ObjectIdentity
dtmIfGroup = _DtmIfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2)
)
_DtmIfTable_Object = MibTable
dtmIfTable = _DtmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dtmIfTable.setStatus("current")
_DtmIfEntry_Object = MibTableRow
dtmIfEntry = _DtmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1)
)
dtmIfEntry.setIndexNames(
    (0, "NETI-DTM-MIB", "dtmIfIndex"),
)
if mibBuilder.loadTexts:
    dtmIfEntry.setStatus("current")


class _DtmIfIndex_Type(Integer32):
    """Custom type dtmIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DtmIfIndex_Type.__name__ = "Integer32"
_DtmIfIndex_Object = MibTableColumn
dtmIfIndex = _DtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 1),
    _DtmIfIndex_Type()
)
dtmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmIfIndex.setStatus("current")
_DtmIfName_Type = DisplayString
_DtmIfName_Object = MibTableColumn
dtmIfName = _DtmIfName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 2),
    _DtmIfName_Type()
)
dtmIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtmIfName.setStatus("current")
_DtmIfMacAddress_Type = MacAddress
_DtmIfMacAddress_Object = MibTableColumn
dtmIfMacAddress = _DtmIfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 3),
    _DtmIfMacAddress_Type()
)
dtmIfMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmIfMacAddress.setStatus("current")
_DtmIfTxCapacity_Type = Gauge32
_DtmIfTxCapacity_Object = MibTableColumn
dtmIfTxCapacity = _DtmIfTxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 4),
    _DtmIfTxCapacity_Type()
)
dtmIfTxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmIfTxCapacity.setStatus("current")


class _DtmIfTxCapacityCtrl_Type(Gauge32):
    """Custom type dtmIfTxCapacityCtrl based on Gauge32"""
    defaultValue = 5


_DtmIfTxCapacityCtrl_Object = MibTableColumn
dtmIfTxCapacityCtrl = _DtmIfTxCapacityCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 5),
    _DtmIfTxCapacityCtrl_Type()
)
dtmIfTxCapacityCtrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtmIfTxCapacityCtrl.setStatus("current")


class _DtmIfTxCapacityStart_Type(Gauge32):
    """Custom type dtmIfTxCapacityStart based on Gauge32"""
    defaultValue = 1


_DtmIfTxCapacityStart_Object = MibTableColumn
dtmIfTxCapacityStart = _DtmIfTxCapacityStart_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 6),
    _DtmIfTxCapacityStart_Type()
)
dtmIfTxCapacityStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmIfTxCapacityStart.setStatus("deprecated")


class _DtmIfTxCapacityOwned_Type(Gauge32):
    """Custom type dtmIfTxCapacityOwned based on Gauge32"""
    defaultValue = 0


_DtmIfTxCapacityOwned_Object = MibTableColumn
dtmIfTxCapacityOwned = _DtmIfTxCapacityOwned_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 7),
    _DtmIfTxCapacityOwned_Type()
)
dtmIfTxCapacityOwned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmIfTxCapacityOwned.setStatus("deprecated")
_DtmIfTxCapacityBorrowed_Type = Gauge32
_DtmIfTxCapacityBorrowed_Object = MibTableColumn
dtmIfTxCapacityBorrowed = _DtmIfTxCapacityBorrowed_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 8),
    _DtmIfTxCapacityBorrowed_Type()
)
dtmIfTxCapacityBorrowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmIfTxCapacityBorrowed.setStatus("deprecated")


class _DtmIfTxCapacityMaxLend_Type(Gauge32):
    """Custom type dtmIfTxCapacityMaxLend based on Gauge32"""
    defaultValue = 0


_DtmIfTxCapacityMaxLend_Object = MibTableColumn
dtmIfTxCapacityMaxLend = _DtmIfTxCapacityMaxLend_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 9),
    _DtmIfTxCapacityMaxLend_Type()
)
dtmIfTxCapacityMaxLend.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtmIfTxCapacityMaxLend.setStatus("deprecated")
_DtmIfTxCapacityLent_Type = Gauge32
_DtmIfTxCapacityLent_Object = MibTableColumn
dtmIfTxCapacityLent = _DtmIfTxCapacityLent_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 10),
    _DtmIfTxCapacityLent_Type()
)
dtmIfTxCapacityLent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmIfTxCapacityLent.setStatus("deprecated")
_DtmIfTxCapacityUsed_Type = Gauge32
_DtmIfTxCapacityUsed_Object = MibTableColumn
dtmIfTxCapacityUsed = _DtmIfTxCapacityUsed_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 11),
    _DtmIfTxCapacityUsed_Type()
)
dtmIfTxCapacityUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmIfTxCapacityUsed.setStatus("current")
_DtmIfRxCapacity_Type = Gauge32
_DtmIfRxCapacity_Object = MibTableColumn
dtmIfRxCapacity = _DtmIfRxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 12),
    _DtmIfRxCapacity_Type()
)
dtmIfRxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmIfRxCapacity.setStatus("current")
_DtmIfRxCapacityUsed_Type = Gauge32
_DtmIfRxCapacityUsed_Object = MibTableColumn
dtmIfRxCapacityUsed = _DtmIfRxCapacityUsed_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 13),
    _DtmIfRxCapacityUsed_Type()
)
dtmIfRxCapacityUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmIfRxCapacityUsed.setStatus("current")


class _DtmIfIfIndex_Type(Integer32):
    """Custom type dtmIfIfIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DtmIfIfIndex_Type.__name__ = "Integer32"
_DtmIfIfIndex_Object = MibTableColumn
dtmIfIfIndex = _DtmIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 14),
    _DtmIfIfIndex_Type()
)
dtmIfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmIfIfIndex.setStatus("deprecated")


class _DtmIfAdminStatus_Type(Integer32):
    """Custom type dtmIfAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_DtmIfAdminStatus_Type.__name__ = "Integer32"
_DtmIfAdminStatus_Object = MibTableColumn
dtmIfAdminStatus = _DtmIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 15),
    _DtmIfAdminStatus_Type()
)
dtmIfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtmIfAdminStatus.setStatus("current")


class _DtmIfOperStatus_Type(Integer32):
    """Custom type dtmIfOperStatus based on Integer32"""
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
        *(("absent", 3),
          ("down", 2),
          ("lowerLayerDown", 4),
          ("up", 1))
    )


_DtmIfOperStatus_Type.__name__ = "Integer32"
_DtmIfOperStatus_Object = MibTableColumn
dtmIfOperStatus = _DtmIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 16),
    _DtmIfOperStatus_Type()
)
dtmIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmIfOperStatus.setStatus("current")
_DtmIfRowStatus_Type = RowStatus
_DtmIfRowStatus_Object = MibTableColumn
dtmIfRowStatus = _DtmIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 17),
    _DtmIfRowStatus_Type()
)
dtmIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtmIfRowStatus.setStatus("current")
_DtmIfAbsent_Type = FaultStatus
_DtmIfAbsent_Object = MibTableColumn
dtmIfAbsent = _DtmIfAbsent_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 18),
    _DtmIfAbsent_Type()
)
dtmIfAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmIfAbsent.setStatus("deprecated")
_DtmIfLOS_Type = FaultStatus
_DtmIfLOS_Object = MibTableColumn
dtmIfLOS = _DtmIfLOS_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 19),
    _DtmIfLOS_Type()
)
dtmIfLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmIfLOS.setStatus("current")
_DtmIfReducedCtrlCapacity_Type = FaultStatus
_DtmIfReducedCtrlCapacity_Object = MibTableColumn
dtmIfReducedCtrlCapacity = _DtmIfReducedCtrlCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 20),
    _DtmIfReducedCtrlCapacity_Type()
)
dtmIfReducedCtrlCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmIfReducedCtrlCapacity.setStatus("current")


class _DtmIfTxCapacityOwnedFirstSlot_Type(Gauge32):
    """Custom type dtmIfTxCapacityOwnedFirstSlot based on Gauge32"""
    defaultValue = 0


_DtmIfTxCapacityOwnedFirstSlot_Object = MibTableColumn
dtmIfTxCapacityOwnedFirstSlot = _DtmIfTxCapacityOwnedFirstSlot_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 21),
    _DtmIfTxCapacityOwnedFirstSlot_Type()
)
dtmIfTxCapacityOwnedFirstSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtmIfTxCapacityOwnedFirstSlot.setStatus("deprecated")


class _DtmIfTxCapacityOwnedLastSlot_Type(Gauge32):
    """Custom type dtmIfTxCapacityOwnedLastSlot based on Gauge32"""
    defaultValue = 0


_DtmIfTxCapacityOwnedLastSlot_Object = MibTableColumn
dtmIfTxCapacityOwnedLastSlot = _DtmIfTxCapacityOwnedLastSlot_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 22),
    _DtmIfTxCapacityOwnedLastSlot_Type()
)
dtmIfTxCapacityOwnedLastSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtmIfTxCapacityOwnedLastSlot.setStatus("current")


class _DtmIfRouteMetric_Type(Unsigned32):
    """Custom type dtmIfRouteMetric based on Unsigned32"""
    defaultValue = 1


_DtmIfRouteMetric_Object = MibTableColumn
dtmIfRouteMetric = _DtmIfRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 23),
    _DtmIfRouteMetric_Type()
)
dtmIfRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtmIfRouteMetric.setStatus("current")


class _DtmIfLinkClass_Type(Integer32):
    """Custom type dtmIfLinkClass based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nailed", 3),
          ("normal", 1),
          ("persistent", 2))
    )


_DtmIfLinkClass_Type.__name__ = "Integer32"
_DtmIfLinkClass_Object = MibTableColumn
dtmIfLinkClass = _DtmIfLinkClass_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 24),
    _DtmIfLinkClass_Type()
)
dtmIfLinkClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtmIfLinkClass.setStatus("current")


class _DtmIfPurpose_Type(SnmpAdminString):
    """Custom type dtmIfPurpose based on SnmpAdminString"""
    defaultHexValue = ""


_DtmIfPurpose_Object = MibTableColumn
dtmIfPurpose = _DtmIfPurpose_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 25),
    _DtmIfPurpose_Type()
)
dtmIfPurpose.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtmIfPurpose.setStatus("current")


class _DtmIfSyncEnabled_Type(Integer32):
    """Custom type dtmIfSyncEnabled based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_DtmIfSyncEnabled_Type.__name__ = "Integer32"
_DtmIfSyncEnabled_Object = MibTableColumn
dtmIfSyncEnabled = _DtmIfSyncEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 26),
    _DtmIfSyncEnabled_Type()
)
dtmIfSyncEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtmIfSyncEnabled.setStatus("current")
_DtmLinkStateGroup_ObjectIdentity = ObjectIdentity
dtmLinkStateGroup = _DtmLinkStateGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3)
)
_DtmLinkStateTableLastChangedTime_Type = DateAndTime
_DtmLinkStateTableLastChangedTime_Object = MibScalar
dtmLinkStateTableLastChangedTime = _DtmLinkStateTableLastChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 1),
    _DtmLinkStateTableLastChangedTime_Type()
)
dtmLinkStateTableLastChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmLinkStateTableLastChangedTime.setStatus("current")
_DtmLinkStateNrOfLinks_Type = Unsigned32
_DtmLinkStateNrOfLinks_Object = MibScalar
dtmLinkStateNrOfLinks = _DtmLinkStateNrOfLinks_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 2),
    _DtmLinkStateNrOfLinks_Type()
)
dtmLinkStateNrOfLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmLinkStateNrOfLinks.setStatus("current")
_DtmLinkStateTable_Object = MibTable
dtmLinkStateTable = _DtmLinkStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 3)
)
if mibBuilder.loadTexts:
    dtmLinkStateTable.setStatus("current")
_DtmLinkStateEntry_Object = MibTableRow
dtmLinkStateEntry = _DtmLinkStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 3, 1)
)
dtmLinkStateEntry.setIndexNames(
    (0, "NETI-DTM-MIB", "dtmLinkStateIndex"),
)
if mibBuilder.loadTexts:
    dtmLinkStateEntry.setStatus("current")
_DtmLinkStateIndex_Type = Unsigned32
_DtmLinkStateIndex_Object = MibTableColumn
dtmLinkStateIndex = _DtmLinkStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 3, 1, 1),
    _DtmLinkStateIndex_Type()
)
dtmLinkStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmLinkStateIndex.setStatus("current")


class _DtmLinkStateType_Type(Integer32):
    """Custom type dtmLinkStateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("looped", 2),
          ("open", 3),
          ("unknown", 1))
    )


_DtmLinkStateType_Type.__name__ = "Integer32"
_DtmLinkStateType_Object = MibTableColumn
dtmLinkStateType = _DtmLinkStateType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 3, 1, 2),
    _DtmLinkStateType_Type()
)
dtmLinkStateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmLinkStateType.setStatus("current")
_DtmLinkStateLocalIf_Type = DisplayString
_DtmLinkStateLocalIf_Object = MibTableColumn
dtmLinkStateLocalIf = _DtmLinkStateLocalIf_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 3, 1, 3),
    _DtmLinkStateLocalIf_Type()
)
dtmLinkStateLocalIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmLinkStateLocalIf.setStatus("current")
_DtmLinkStateNrOfIfs_Type = Unsigned32
_DtmLinkStateNrOfIfs_Object = MibScalar
dtmLinkStateNrOfIfs = _DtmLinkStateNrOfIfs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 4),
    _DtmLinkStateNrOfIfs_Type()
)
dtmLinkStateNrOfIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmLinkStateNrOfIfs.setStatus("current")
_DtmLinkStateIfTable_Object = MibTable
dtmLinkStateIfTable = _DtmLinkStateIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 5)
)
if mibBuilder.loadTexts:
    dtmLinkStateIfTable.setStatus("current")
_DtmLinkStateIfEntry_Object = MibTableRow
dtmLinkStateIfEntry = _DtmLinkStateIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 5, 1)
)
dtmLinkStateIfEntry.setIndexNames(
    (0, "NETI-DTM-MIB", "dtmLinkStateIndex"),
    (0, "NETI-DTM-MIB", "dtmLinkStateIfIndex"),
)
if mibBuilder.loadTexts:
    dtmLinkStateIfEntry.setStatus("current")
_DtmLinkStateIfIndex_Type = Unsigned32
_DtmLinkStateIfIndex_Object = MibTableColumn
dtmLinkStateIfIndex = _DtmLinkStateIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 5, 1, 1),
    _DtmLinkStateIfIndex_Type()
)
dtmLinkStateIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmLinkStateIfIndex.setStatus("current")
_DtmLinkStateIfMacAddress_Type = MacAddress
_DtmLinkStateIfMacAddress_Object = MibTableColumn
dtmLinkStateIfMacAddress = _DtmLinkStateIfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 5, 1, 2),
    _DtmLinkStateIfMacAddress_Type()
)
dtmLinkStateIfMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmLinkStateIfMacAddress.setStatus("current")
_DtmLinkStateIfNodeMacAddress_Type = MacAddress
_DtmLinkStateIfNodeMacAddress_Object = MibTableColumn
dtmLinkStateIfNodeMacAddress = _DtmLinkStateIfNodeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 5, 1, 3),
    _DtmLinkStateIfNodeMacAddress_Type()
)
dtmLinkStateIfNodeMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmLinkStateIfNodeMacAddress.setStatus("current")
_DtmLinkStateIfNodeAddress_Type = DtmAddress
_DtmLinkStateIfNodeAddress_Object = MibTableColumn
dtmLinkStateIfNodeAddress = _DtmLinkStateIfNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 5, 1, 4),
    _DtmLinkStateIfNodeAddress_Type()
)
dtmLinkStateIfNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmLinkStateIfNodeAddress.setStatus("current")
_DtmLinkStateLocalSubIf_Type = DisplayString
_DtmLinkStateLocalSubIf_Object = MibTableColumn
dtmLinkStateLocalSubIf = _DtmLinkStateLocalSubIf_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 5, 1, 5),
    _DtmLinkStateLocalSubIf_Type()
)
dtmLinkStateLocalSubIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmLinkStateLocalSubIf.setStatus("current")


class _DtmLinkStateIfNodeStatus_Type(Integer32):
    """Custom type dtmLinkStateIfNodeStatus based on Integer32"""
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
        *(("downKeep", 5),
          ("limited", 3),
          ("loopback", 7),
          ("noControl", 4),
          ("notApplicable", 0),
          ("pending", 6),
          ("recover", 2),
          ("up", 1))
    )


_DtmLinkStateIfNodeStatus_Type.__name__ = "Integer32"
_DtmLinkStateIfNodeStatus_Object = MibTableColumn
dtmLinkStateIfNodeStatus = _DtmLinkStateIfNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 5, 1, 6),
    _DtmLinkStateIfNodeStatus_Type()
)
dtmLinkStateIfNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmLinkStateIfNodeStatus.setStatus("current")
_DtmRouteGroup_ObjectIdentity = ObjectIdentity
dtmRouteGroup = _DtmRouteGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 4)
)
_DtmDrpNodeRouteMetric_Type = Unsigned32
_DtmDrpNodeRouteMetric_Object = MibScalar
dtmDrpNodeRouteMetric = _DtmDrpNodeRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 4, 2),
    _DtmDrpNodeRouteMetric_Type()
)
dtmDrpNodeRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtmDrpNodeRouteMetric.setStatus("current")


class _DtmDrpNodeType_Type(Integer32):
    """Custom type dtmDrpNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("endNode", 2),
          ("switch", 1))
    )


_DtmDrpNodeType_Type.__name__ = "Integer32"
_DtmDrpNodeType_Object = MibScalar
dtmDrpNodeType = _DtmDrpNodeType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 4, 3),
    _DtmDrpNodeType_Type()
)
dtmDrpNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtmDrpNodeType.setStatus("current")
_DtmDrpAreaNumber_Type = Unsigned32
_DtmDrpAreaNumber_Object = MibScalar
dtmDrpAreaNumber = _DtmDrpAreaNumber_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 4, 4),
    _DtmDrpAreaNumber_Type()
)
dtmDrpAreaNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtmDrpAreaNumber.setStatus("current")
_DtmDrpDetectAreaNumber_Type = TruthValue
_DtmDrpDetectAreaNumber_Object = MibScalar
dtmDrpDetectAreaNumber = _DtmDrpDetectAreaNumber_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 4, 5),
    _DtmDrpDetectAreaNumber_Type()
)
dtmDrpDetectAreaNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtmDrpDetectAreaNumber.setStatus("current")
_DtmDrpDetectDefaultGateway_Type = TruthValue
_DtmDrpDetectDefaultGateway_Object = MibScalar
dtmDrpDetectDefaultGateway = _DtmDrpDetectDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 4, 6),
    _DtmDrpDetectDefaultGateway_Type()
)
dtmDrpDetectDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtmDrpDetectDefaultGateway.setStatus("current")
_DtmHistoryGroup_ObjectIdentity = ObjectIdentity
dtmHistoryGroup = _DtmHistoryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 5)
)
_DtmNodeGroup_ObjectIdentity = ObjectIdentity
dtmNodeGroup = _DtmNodeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 6)
)


class _DtmNodeStatus_Type(Integer32):
    """Custom type dtmNodeStatus based on Integer32"""
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
        *(("limited", 3),
          ("noControl", 4),
          ("recover", 2),
          ("up", 1))
    )


_DtmNodeStatus_Type.__name__ = "Integer32"
_DtmNodeStatus_Object = MibScalar
dtmNodeStatus = _DtmNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 6, 1),
    _DtmNodeStatus_Type()
)
dtmNodeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtmNodeStatus.setStatus("current")
_DtmNodeRestartOnError_Type = TruthValue
_DtmNodeRestartOnError_Object = MibScalar
dtmNodeRestartOnError = _DtmNodeRestartOnError_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 6, 2),
    _DtmNodeRestartOnError_Type()
)
dtmNodeRestartOnError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtmNodeRestartOnError.setStatus("current")
_DtmNodeId_Type = MacAddress
_DtmNodeId_Object = MibScalar
dtmNodeId = _DtmNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 6, 3),
    _DtmNodeId_Type()
)
dtmNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmNodeId.setStatus("current")
_DtmSyncGroup_ObjectIdentity = ObjectIdentity
dtmSyncGroup = _DtmSyncGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7)
)
_DtmSyncNodeId_Type = MacAddress
_DtmSyncNodeId_Object = MibScalar
dtmSyncNodeId = _DtmSyncNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 1),
    _DtmSyncNodeId_Type()
)
dtmSyncNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmSyncNodeId.setStatus("current")
_DtmCurrentTimingSourceName_Type = DisplayString
_DtmCurrentTimingSourceName_Object = MibScalar
dtmCurrentTimingSourceName = _DtmCurrentTimingSourceName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 2),
    _DtmCurrentTimingSourceName_Type()
)
dtmCurrentTimingSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmCurrentTimingSourceName.setStatus("current")
_DtmCurrentTimingSourcePeerId_Type = MacAddress
_DtmCurrentTimingSourcePeerId_Object = MibScalar
dtmCurrentTimingSourcePeerId = _DtmCurrentTimingSourcePeerId_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 3),
    _DtmCurrentTimingSourcePeerId_Type()
)
dtmCurrentTimingSourcePeerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmCurrentTimingSourcePeerId.setStatus("current")


class _DtmTimeScaleStatus_Type(Integer32):
    """Custom type dtmTimeScaleStatus based on Integer32"""
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
        *(("compensated", 4),
          ("notSupported", 1),
          ("reassigned", 3),
          ("uninitiated", 2))
    )


_DtmTimeScaleStatus_Type.__name__ = "Integer32"
_DtmTimeScaleStatus_Object = MibScalar
dtmTimeScaleStatus = _DtmTimeScaleStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 4),
    _DtmTimeScaleStatus_Type()
)
dtmTimeScaleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmTimeScaleStatus.setStatus("current")
_DtmTimeSourceCalibrationReference_Type = Integer32
_DtmTimeSourceCalibrationReference_Object = MibScalar
dtmTimeSourceCalibrationReference = _DtmTimeSourceCalibrationReference_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 5),
    _DtmTimeSourceCalibrationReference_Type()
)
dtmTimeSourceCalibrationReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtmTimeSourceCalibrationReference.setStatus("current")
_DtmTimeSourceTable_Object = MibTable
dtmTimeSourceTable = _DtmTimeSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 6)
)
if mibBuilder.loadTexts:
    dtmTimeSourceTable.setStatus("current")
_DtmTimeSourceEntry_Object = MibTableRow
dtmTimeSourceEntry = _DtmTimeSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 6, 1)
)
dtmTimeSourceEntry.setIndexNames(
    (0, "NETI-DTM-MIB", "dtmTimeSourceIndex"),
)
if mibBuilder.loadTexts:
    dtmTimeSourceEntry.setStatus("current")


class _DtmTimeSourceIndex_Type(Integer32):
    """Custom type dtmTimeSourceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DtmTimeSourceIndex_Type.__name__ = "Integer32"
_DtmTimeSourceIndex_Object = MibTableColumn
dtmTimeSourceIndex = _DtmTimeSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 6, 1, 1),
    _DtmTimeSourceIndex_Type()
)
dtmTimeSourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dtmTimeSourceIndex.setStatus("current")
_DtmTimeSourceName_Type = DisplayString
_DtmTimeSourceName_Object = MibTableColumn
dtmTimeSourceName = _DtmTimeSourceName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 6, 1, 2),
    _DtmTimeSourceName_Type()
)
dtmTimeSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmTimeSourceName.setStatus("current")


class _DtmTimeSourceAdminStatus_Type(Integer32):
    """Custom type dtmTimeSourceAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_DtmTimeSourceAdminStatus_Type.__name__ = "Integer32"
_DtmTimeSourceAdminStatus_Object = MibTableColumn
dtmTimeSourceAdminStatus = _DtmTimeSourceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 6, 1, 3),
    _DtmTimeSourceAdminStatus_Type()
)
dtmTimeSourceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtmTimeSourceAdminStatus.setStatus("current")


class _DtmTimeSourceOperStatus_Type(Integer32):
    """Custom type dtmTimeSourceOperStatus based on Integer32"""
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
        *(("absent", 3),
          ("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 4),
          ("up", 1))
    )


_DtmTimeSourceOperStatus_Type.__name__ = "Integer32"
_DtmTimeSourceOperStatus_Object = MibTableColumn
dtmTimeSourceOperStatus = _DtmTimeSourceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 6, 1, 4),
    _DtmTimeSourceOperStatus_Type()
)
dtmTimeSourceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmTimeSourceOperStatus.setStatus("current")


class _DtmTimeSourceType_Type(Integer32):
    """Custom type dtmTimeSourceType based on Integer32"""
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
        *(("dsyp", 1),
          ("internal", 4),
          ("sqc", 2),
          ("ssm", 3))
    )


_DtmTimeSourceType_Type.__name__ = "Integer32"
_DtmTimeSourceType_Object = MibTableColumn
dtmTimeSourceType = _DtmTimeSourceType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 6, 1, 5),
    _DtmTimeSourceType_Type()
)
dtmTimeSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmTimeSourceType.setStatus("current")
_DtmTimeSourceRef_Type = RowPointer
_DtmTimeSourceRef_Object = MibTableColumn
dtmTimeSourceRef = _DtmTimeSourceRef_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 6, 1, 6),
    _DtmTimeSourceRef_Type()
)
dtmTimeSourceRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmTimeSourceRef.setStatus("current")
_DtmTimeSourceRoundTripTime_Type = Unsigned32
_DtmTimeSourceRoundTripTime_Object = MibTableColumn
dtmTimeSourceRoundTripTime = _DtmTimeSourceRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 6, 1, 7),
    _DtmTimeSourceRoundTripTime_Type()
)
dtmTimeSourceRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmTimeSourceRoundTripTime.setStatus("current")
_DtmTimeSourceTimeError_Type = Integer32
_DtmTimeSourceTimeError_Object = MibTableColumn
dtmTimeSourceTimeError = _DtmTimeSourceTimeError_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 6, 1, 8),
    _DtmTimeSourceTimeError_Type()
)
dtmTimeSourceTimeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmTimeSourceTimeError.setStatus("current")
_DtmTimeSourceCalibrationTimeError_Type = Integer32
_DtmTimeSourceCalibrationTimeError_Object = MibTableColumn
dtmTimeSourceCalibrationTimeError = _DtmTimeSourceCalibrationTimeError_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 6, 1, 9),
    _DtmTimeSourceCalibrationTimeError_Type()
)
dtmTimeSourceCalibrationTimeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtmTimeSourceCalibrationTimeError.setStatus("current")


class _DtmTimeSourceCalibrationRatio_Type(Integer32):
    """Custom type dtmTimeSourceCalibrationRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-499999, 499999),
    )


_DtmTimeSourceCalibrationRatio_Type.__name__ = "Integer32"
_DtmTimeSourceCalibrationRatio_Object = MibTableColumn
dtmTimeSourceCalibrationRatio = _DtmTimeSourceCalibrationRatio_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 6, 1, 10),
    _DtmTimeSourceCalibrationRatio_Type()
)
dtmTimeSourceCalibrationRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtmTimeSourceCalibrationRatio.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETI-DTM-MIB",
    **{"DtmAddress": DtmAddress,
       "DtmSourceRoute": DtmSourceRoute,
       "netiDTMMIB": netiDTMMIB,
       "netiDTMMIBObjects": netiDTMMIBObjects,
       "dtmAddrGroup": dtmAddrGroup,
       "dtmAddrTable": dtmAddrTable,
       "dtmAddrEntry": dtmAddrEntry,
       "dtmAddrEntryIndex": dtmAddrEntryIndex,
       "dtmAddrEntryAddr": dtmAddrEntryAddr,
       "dtmAddrEntryIsAlias": dtmAddrEntryIsAlias,
       "dtmAddrEntryAddrType": dtmAddrEntryAddrType,
       "dtmAddrEntryRowStatus": dtmAddrEntryRowStatus,
       "dtmHostsTable": dtmHostsTable,
       "dtmHostsEntry": dtmHostsEntry,
       "dtmHostsEntryIndex": dtmHostsEntryIndex,
       "dtmHostsEntryAddr": dtmHostsEntryAddr,
       "dtmHostsEntryName": dtmHostsEntryName,
       "dtmHostsEntryRowStatus": dtmHostsEntryRowStatus,
       "dtmIfGroup": dtmIfGroup,
       "dtmIfTable": dtmIfTable,
       "dtmIfEntry": dtmIfEntry,
       "dtmIfIndex": dtmIfIndex,
       "dtmIfName": dtmIfName,
       "dtmIfMacAddress": dtmIfMacAddress,
       "dtmIfTxCapacity": dtmIfTxCapacity,
       "dtmIfTxCapacityCtrl": dtmIfTxCapacityCtrl,
       "dtmIfTxCapacityStart": dtmIfTxCapacityStart,
       "dtmIfTxCapacityOwned": dtmIfTxCapacityOwned,
       "dtmIfTxCapacityBorrowed": dtmIfTxCapacityBorrowed,
       "dtmIfTxCapacityMaxLend": dtmIfTxCapacityMaxLend,
       "dtmIfTxCapacityLent": dtmIfTxCapacityLent,
       "dtmIfTxCapacityUsed": dtmIfTxCapacityUsed,
       "dtmIfRxCapacity": dtmIfRxCapacity,
       "dtmIfRxCapacityUsed": dtmIfRxCapacityUsed,
       "dtmIfIfIndex": dtmIfIfIndex,
       "dtmIfAdminStatus": dtmIfAdminStatus,
       "dtmIfOperStatus": dtmIfOperStatus,
       "dtmIfRowStatus": dtmIfRowStatus,
       "dtmIfAbsent": dtmIfAbsent,
       "dtmIfLOS": dtmIfLOS,
       "dtmIfReducedCtrlCapacity": dtmIfReducedCtrlCapacity,
       "dtmIfTxCapacityOwnedFirstSlot": dtmIfTxCapacityOwnedFirstSlot,
       "dtmIfTxCapacityOwnedLastSlot": dtmIfTxCapacityOwnedLastSlot,
       "dtmIfRouteMetric": dtmIfRouteMetric,
       "dtmIfLinkClass": dtmIfLinkClass,
       "dtmIfPurpose": dtmIfPurpose,
       "dtmIfSyncEnabled": dtmIfSyncEnabled,
       "dtmLinkStateGroup": dtmLinkStateGroup,
       "dtmLinkStateTableLastChangedTime": dtmLinkStateTableLastChangedTime,
       "dtmLinkStateNrOfLinks": dtmLinkStateNrOfLinks,
       "dtmLinkStateTable": dtmLinkStateTable,
       "dtmLinkStateEntry": dtmLinkStateEntry,
       "dtmLinkStateIndex": dtmLinkStateIndex,
       "dtmLinkStateType": dtmLinkStateType,
       "dtmLinkStateLocalIf": dtmLinkStateLocalIf,
       "dtmLinkStateNrOfIfs": dtmLinkStateNrOfIfs,
       "dtmLinkStateIfTable": dtmLinkStateIfTable,
       "dtmLinkStateIfEntry": dtmLinkStateIfEntry,
       "dtmLinkStateIfIndex": dtmLinkStateIfIndex,
       "dtmLinkStateIfMacAddress": dtmLinkStateIfMacAddress,
       "dtmLinkStateIfNodeMacAddress": dtmLinkStateIfNodeMacAddress,
       "dtmLinkStateIfNodeAddress": dtmLinkStateIfNodeAddress,
       "dtmLinkStateLocalSubIf": dtmLinkStateLocalSubIf,
       "dtmLinkStateIfNodeStatus": dtmLinkStateIfNodeStatus,
       "dtmRouteGroup": dtmRouteGroup,
       "dtmDrpNodeRouteMetric": dtmDrpNodeRouteMetric,
       "dtmDrpNodeType": dtmDrpNodeType,
       "dtmDrpAreaNumber": dtmDrpAreaNumber,
       "dtmDrpDetectAreaNumber": dtmDrpDetectAreaNumber,
       "dtmDrpDetectDefaultGateway": dtmDrpDetectDefaultGateway,
       "dtmHistoryGroup": dtmHistoryGroup,
       "dtmNodeGroup": dtmNodeGroup,
       "dtmNodeStatus": dtmNodeStatus,
       "dtmNodeRestartOnError": dtmNodeRestartOnError,
       "dtmNodeId": dtmNodeId,
       "dtmSyncGroup": dtmSyncGroup,
       "dtmSyncNodeId": dtmSyncNodeId,
       "dtmCurrentTimingSourceName": dtmCurrentTimingSourceName,
       "dtmCurrentTimingSourcePeerId": dtmCurrentTimingSourcePeerId,
       "dtmTimeScaleStatus": dtmTimeScaleStatus,
       "dtmTimeSourceCalibrationReference": dtmTimeSourceCalibrationReference,
       "dtmTimeSourceTable": dtmTimeSourceTable,
       "dtmTimeSourceEntry": dtmTimeSourceEntry,
       "dtmTimeSourceIndex": dtmTimeSourceIndex,
       "dtmTimeSourceName": dtmTimeSourceName,
       "dtmTimeSourceAdminStatus": dtmTimeSourceAdminStatus,
       "dtmTimeSourceOperStatus": dtmTimeSourceOperStatus,
       "dtmTimeSourceType": dtmTimeSourceType,
       "dtmTimeSourceRef": dtmTimeSourceRef,
       "dtmTimeSourceRoundTripTime": dtmTimeSourceRoundTripTime,
       "dtmTimeSourceTimeError": dtmTimeSourceTimeError,
       "dtmTimeSourceCalibrationTimeError": dtmTimeSourceCalibrationTimeError,
       "dtmTimeSourceCalibrationRatio": dtmTimeSourceCalibrationRatio}
)
