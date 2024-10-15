# SNMP MIB module (BAY-STACK-OSPF-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAY-STACK-OSPF-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:16 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(AreaID,
 RouterID) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "AreaID",
    "RouterID")

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

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackOspfExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 14)
)
bayStackOspfExtMib.setRevisions(
        ("2009-11-10 00:00",
         "2006-09-26 00:00",
         "2006-09-14 00:00",
         "2006-06-13 00:00",
         "2005-12-01 00:00",
         "2005-10-20 00:00",
         "2005-10-11 00:00",
         "2005-09-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BsoeNotifications_ObjectIdentity = ObjectIdentity
bsoeNotifications = _BsoeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 0)
)
_BsoeObjects_ObjectIdentity = ObjectIdentity
bsoeObjects = _BsoeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1)
)
_BsoeScalars_ObjectIdentity = ObjectIdentity
bsoeScalars = _BsoeScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 1)
)


class _BsoeApplyRedistribute_Type(Integer32):
    """Custom type bsoeApplyRedistribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 5),
          ("direct", 1),
          ("none", 0),
          ("ospf", 4),
          ("rip", 3),
          ("static", 2))
    )


_BsoeApplyRedistribute_Type.__name__ = "Integer32"
_BsoeApplyRedistribute_Object = MibScalar
bsoeApplyRedistribute = _BsoeApplyRedistribute_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 1, 1),
    _BsoeApplyRedistribute_Type()
)
bsoeApplyRedistribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsoeApplyRedistribute.setStatus("current")


class _BsoeHardwareCompatibilityMode_Type(Integer32):
    """Custom type bsoeHardwareCompatibilityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ers5510", 1),
          ("noneErs5510", 2))
    )


_BsoeHardwareCompatibilityMode_Type.__name__ = "Integer32"
_BsoeHardwareCompatibilityMode_Object = MibScalar
bsoeHardwareCompatibilityMode = _BsoeHardwareCompatibilityMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 1, 2),
    _BsoeHardwareCompatibilityMode_Type()
)
bsoeHardwareCompatibilityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsoeHardwareCompatibilityMode.setStatus("current")
_BsoeOspfIfExtTable_Object = MibTable
bsoeOspfIfExtTable = _BsoeOspfIfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 2)
)
if mibBuilder.loadTexts:
    bsoeOspfIfExtTable.setStatus("current")
_BsoeOspfIfExtEntry_Object = MibTableRow
bsoeOspfIfExtEntry = _BsoeOspfIfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 2, 1)
)
bsoeOspfIfExtEntry.setIndexNames(
    (0, "BAY-STACK-OSPF-EXT-MIB", "bsoeOspfIfIpAddress"),
    (0, "BAY-STACK-OSPF-EXT-MIB", "bsoeOspfAddressLessIf"),
)
if mibBuilder.loadTexts:
    bsoeOspfIfExtEntry.setStatus("current")
_BsoeOspfIfIpAddress_Type = IpAddress
_BsoeOspfIfIpAddress_Object = MibTableColumn
bsoeOspfIfIpAddress = _BsoeOspfIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 2, 1, 1),
    _BsoeOspfIfIpAddress_Type()
)
bsoeOspfIfIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsoeOspfIfIpAddress.setStatus("current")


class _BsoeOspfAddressLessIf_Type(Integer32):
    """Custom type bsoeOspfAddressLessIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BsoeOspfAddressLessIf_Type.__name__ = "Integer32"
_BsoeOspfAddressLessIf_Object = MibTableColumn
bsoeOspfAddressLessIf = _BsoeOspfAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 2, 1, 2),
    _BsoeOspfAddressLessIf_Type()
)
bsoeOspfAddressLessIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsoeOspfAddressLessIf.setStatus("current")


class _BsoeOspfIfExtAdvertiseWhenDown_Type(TruthValue):
    """Custom type bsoeOspfIfExtAdvertiseWhenDown based on TruthValue"""


_BsoeOspfIfExtAdvertiseWhenDown_Object = MibTableColumn
bsoeOspfIfExtAdvertiseWhenDown = _BsoeOspfIfExtAdvertiseWhenDown_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 2, 1, 3),
    _BsoeOspfIfExtAdvertiseWhenDown_Type()
)
bsoeOspfIfExtAdvertiseWhenDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsoeOspfIfExtAdvertiseWhenDown.setStatus("current")


class _BsoeOspfIfExtPrimaryMd5Key_Type(Integer32):
    """Custom type bsoeOspfIfExtPrimaryMd5Key based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BsoeOspfIfExtPrimaryMd5Key_Type.__name__ = "Integer32"
_BsoeOspfIfExtPrimaryMd5Key_Object = MibTableColumn
bsoeOspfIfExtPrimaryMd5Key = _BsoeOspfIfExtPrimaryMd5Key_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 2, 1, 4),
    _BsoeOspfIfExtPrimaryMd5Key_Type()
)
bsoeOspfIfExtPrimaryMd5Key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsoeOspfIfExtPrimaryMd5Key.setStatus("current")


class _BsoeOspfIfExtMtuIgnore_Type(TruthValue):
    """Custom type bsoeOspfIfExtMtuIgnore based on TruthValue"""


_BsoeOspfIfExtMtuIgnore_Object = MibTableColumn
bsoeOspfIfExtMtuIgnore = _BsoeOspfIfExtMtuIgnore_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 2, 1, 5),
    _BsoeOspfIfExtMtuIgnore_Type()
)
bsoeOspfIfExtMtuIgnore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsoeOspfIfExtMtuIgnore.setStatus("current")


class _BsoeOspfIfExtType_Type(Integer32):
    """Custom type bsoeOspfIfExtType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("passive", 2))
    )


_BsoeOspfIfExtType_Type.__name__ = "Integer32"
_BsoeOspfIfExtType_Object = MibTableColumn
bsoeOspfIfExtType = _BsoeOspfIfExtType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 2, 1, 6),
    _BsoeOspfIfExtType_Type()
)
bsoeOspfIfExtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsoeOspfIfExtType.setStatus("current")
_BsoeMessageDigestTable_Object = MibTable
bsoeMessageDigestTable = _BsoeMessageDigestTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 3)
)
if mibBuilder.loadTexts:
    bsoeMessageDigestTable.setStatus("current")
_BsoeMessageDigestEntry_Object = MibTableRow
bsoeMessageDigestEntry = _BsoeMessageDigestEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 3, 1)
)
bsoeMessageDigestEntry.setIndexNames(
    (0, "BAY-STACK-OSPF-EXT-MIB", "bsoeMessageDigestIpAddress"),
    (0, "BAY-STACK-OSPF-EXT-MIB", "bsoeMessageDigestAddressLessIf"),
    (0, "BAY-STACK-OSPF-EXT-MIB", "bsoeMessageDigestIndex"),
    (0, "BAY-STACK-OSPF-EXT-MIB", "bsoeMessageDigestType"),
)
if mibBuilder.loadTexts:
    bsoeMessageDigestEntry.setStatus("current")
_BsoeMessageDigestIpAddress_Type = IpAddress
_BsoeMessageDigestIpAddress_Object = MibTableColumn
bsoeMessageDigestIpAddress = _BsoeMessageDigestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 3, 1, 1),
    _BsoeMessageDigestIpAddress_Type()
)
bsoeMessageDigestIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsoeMessageDigestIpAddress.setStatus("current")


class _BsoeMessageDigestAddressLessIf_Type(Integer32):
    """Custom type bsoeMessageDigestAddressLessIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BsoeMessageDigestAddressLessIf_Type.__name__ = "Integer32"
_BsoeMessageDigestAddressLessIf_Object = MibTableColumn
bsoeMessageDigestAddressLessIf = _BsoeMessageDigestAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 3, 1, 2),
    _BsoeMessageDigestAddressLessIf_Type()
)
bsoeMessageDigestAddressLessIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsoeMessageDigestAddressLessIf.setStatus("current")


class _BsoeMessageDigestIndex_Type(Integer32):
    """Custom type bsoeMessageDigestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BsoeMessageDigestIndex_Type.__name__ = "Integer32"
_BsoeMessageDigestIndex_Object = MibTableColumn
bsoeMessageDigestIndex = _BsoeMessageDigestIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 3, 1, 3),
    _BsoeMessageDigestIndex_Type()
)
bsoeMessageDigestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsoeMessageDigestIndex.setStatus("current")


class _BsoeMessageDigestType_Type(Integer32):
    """Custom type bsoeMessageDigestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("md5", 1)
    )


_BsoeMessageDigestType_Type.__name__ = "Integer32"
_BsoeMessageDigestType_Object = MibTableColumn
bsoeMessageDigestType = _BsoeMessageDigestType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 3, 1, 4),
    _BsoeMessageDigestType_Type()
)
bsoeMessageDigestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsoeMessageDigestType.setStatus("current")


class _BsoeMessageDigestKey_Type(OctetString):
    """Custom type bsoeMessageDigestKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BsoeMessageDigestKey_Type.__name__ = "OctetString"
_BsoeMessageDigestKey_Object = MibTableColumn
bsoeMessageDigestKey = _BsoeMessageDigestKey_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 3, 1, 5),
    _BsoeMessageDigestKey_Type()
)
bsoeMessageDigestKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsoeMessageDigestKey.setStatus("current")
_BsoeMessageDigestRowStatus_Type = RowStatus
_BsoeMessageDigestRowStatus_Object = MibTableColumn
bsoeMessageDigestRowStatus = _BsoeMessageDigestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 3, 1, 6),
    _BsoeMessageDigestRowStatus_Type()
)
bsoeMessageDigestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsoeMessageDigestRowStatus.setStatus("current")
_BsoeOspfNbrExtTable_Object = MibTable
bsoeOspfNbrExtTable = _BsoeOspfNbrExtTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 4)
)
if mibBuilder.loadTexts:
    bsoeOspfNbrExtTable.setStatus("current")
_BsoeOspfNbrExtEntry_Object = MibTableRow
bsoeOspfNbrExtEntry = _BsoeOspfNbrExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 4, 1)
)
bsoeOspfNbrExtEntry.setIndexNames(
    (0, "BAY-STACK-OSPF-EXT-MIB", "bsoeOspfNbrExtIpAddr"),
    (0, "BAY-STACK-OSPF-EXT-MIB", "bsoeOspfNbrExtAddressLessIndex"),
)
if mibBuilder.loadTexts:
    bsoeOspfNbrExtEntry.setStatus("current")
_BsoeOspfNbrExtIpAddr_Type = IpAddress
_BsoeOspfNbrExtIpAddr_Object = MibTableColumn
bsoeOspfNbrExtIpAddr = _BsoeOspfNbrExtIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 4, 1, 1),
    _BsoeOspfNbrExtIpAddr_Type()
)
bsoeOspfNbrExtIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsoeOspfNbrExtIpAddr.setStatus("current")
_BsoeOspfNbrExtAddressLessIndex_Type = InterfaceIndex
_BsoeOspfNbrExtAddressLessIndex_Object = MibTableColumn
bsoeOspfNbrExtAddressLessIndex = _BsoeOspfNbrExtAddressLessIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 4, 1, 2),
    _BsoeOspfNbrExtAddressLessIndex_Type()
)
bsoeOspfNbrExtAddressLessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsoeOspfNbrExtAddressLessIndex.setStatus("current")
_BsoeOspfNbrExtInterfaceAddr_Type = IpAddress
_BsoeOspfNbrExtInterfaceAddr_Object = MibTableColumn
bsoeOspfNbrExtInterfaceAddr = _BsoeOspfNbrExtInterfaceAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 4, 1, 3),
    _BsoeOspfNbrExtInterfaceAddr_Type()
)
bsoeOspfNbrExtInterfaceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsoeOspfNbrExtInterfaceAddr.setStatus("current")
_BsoeOspfVirtIfExtTable_Object = MibTable
bsoeOspfVirtIfExtTable = _BsoeOspfVirtIfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 5)
)
if mibBuilder.loadTexts:
    bsoeOspfVirtIfExtTable.setStatus("current")
_BsoeOspfVirtIfExtEntry_Object = MibTableRow
bsoeOspfVirtIfExtEntry = _BsoeOspfVirtIfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 5, 1)
)
bsoeOspfVirtIfExtEntry.setIndexNames(
    (0, "BAY-STACK-OSPF-EXT-MIB", "bsoeOspfVirtIfExtAreaId"),
    (0, "BAY-STACK-OSPF-EXT-MIB", "bsoeOspfVirtIfExtNeighbor"),
)
if mibBuilder.loadTexts:
    bsoeOspfVirtIfExtEntry.setStatus("current")
_BsoeOspfVirtIfExtAreaId_Type = AreaID
_BsoeOspfVirtIfExtAreaId_Object = MibTableColumn
bsoeOspfVirtIfExtAreaId = _BsoeOspfVirtIfExtAreaId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 5, 1, 1),
    _BsoeOspfVirtIfExtAreaId_Type()
)
bsoeOspfVirtIfExtAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsoeOspfVirtIfExtAreaId.setStatus("current")
_BsoeOspfVirtIfExtNeighbor_Type = RouterID
_BsoeOspfVirtIfExtNeighbor_Object = MibTableColumn
bsoeOspfVirtIfExtNeighbor = _BsoeOspfVirtIfExtNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 5, 1, 2),
    _BsoeOspfVirtIfExtNeighbor_Type()
)
bsoeOspfVirtIfExtNeighbor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsoeOspfVirtIfExtNeighbor.setStatus("current")


class _BsoeOspfVirtIfExtPrimaryMd5Key_Type(Integer32):
    """Custom type bsoeOspfVirtIfExtPrimaryMd5Key based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BsoeOspfVirtIfExtPrimaryMd5Key_Type.__name__ = "Integer32"
_BsoeOspfVirtIfExtPrimaryMd5Key_Object = MibTableColumn
bsoeOspfVirtIfExtPrimaryMd5Key = _BsoeOspfVirtIfExtPrimaryMd5Key_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 5, 1, 3),
    _BsoeOspfVirtIfExtPrimaryMd5Key_Type()
)
bsoeOspfVirtIfExtPrimaryMd5Key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsoeOspfVirtIfExtPrimaryMd5Key.setStatus("current")


class _BsoeOspfVirtIfExtType_Type(Integer32):
    """Custom type bsoeOspfVirtIfExtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 2),
          ("manual", 1))
    )


_BsoeOspfVirtIfExtType_Type.__name__ = "Integer32"
_BsoeOspfVirtIfExtType_Object = MibTableColumn
bsoeOspfVirtIfExtType = _BsoeOspfVirtIfExtType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 5, 1, 4),
    _BsoeOspfVirtIfExtType_Type()
)
bsoeOspfVirtIfExtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsoeOspfVirtIfExtType.setStatus("current")
_BsoeVirtIfMessageDigestTable_Object = MibTable
bsoeVirtIfMessageDigestTable = _BsoeVirtIfMessageDigestTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 6)
)
if mibBuilder.loadTexts:
    bsoeVirtIfMessageDigestTable.setStatus("current")
_BsoeVirtIfMessageDigestEntry_Object = MibTableRow
bsoeVirtIfMessageDigestEntry = _BsoeVirtIfMessageDigestEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 6, 1)
)
bsoeVirtIfMessageDigestEntry.setIndexNames(
    (0, "BAY-STACK-OSPF-EXT-MIB", "bsoeVirtIfMessageDigestAreaId"),
    (0, "BAY-STACK-OSPF-EXT-MIB", "bsoeVirtIfMessageDigestNeighbor"),
    (0, "BAY-STACK-OSPF-EXT-MIB", "bsoeVirtIfMessageDigestIndex"),
    (0, "BAY-STACK-OSPF-EXT-MIB", "bsoeVirtIfMessageDigestType"),
)
if mibBuilder.loadTexts:
    bsoeVirtIfMessageDigestEntry.setStatus("current")
_BsoeVirtIfMessageDigestAreaId_Type = AreaID
_BsoeVirtIfMessageDigestAreaId_Object = MibTableColumn
bsoeVirtIfMessageDigestAreaId = _BsoeVirtIfMessageDigestAreaId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 6, 1, 1),
    _BsoeVirtIfMessageDigestAreaId_Type()
)
bsoeVirtIfMessageDigestAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsoeVirtIfMessageDigestAreaId.setStatus("current")
_BsoeVirtIfMessageDigestNeighbor_Type = RouterID
_BsoeVirtIfMessageDigestNeighbor_Object = MibTableColumn
bsoeVirtIfMessageDigestNeighbor = _BsoeVirtIfMessageDigestNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 6, 1, 2),
    _BsoeVirtIfMessageDigestNeighbor_Type()
)
bsoeVirtIfMessageDigestNeighbor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsoeVirtIfMessageDigestNeighbor.setStatus("current")


class _BsoeVirtIfMessageDigestIndex_Type(Integer32):
    """Custom type bsoeVirtIfMessageDigestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BsoeVirtIfMessageDigestIndex_Type.__name__ = "Integer32"
_BsoeVirtIfMessageDigestIndex_Object = MibTableColumn
bsoeVirtIfMessageDigestIndex = _BsoeVirtIfMessageDigestIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 6, 1, 3),
    _BsoeVirtIfMessageDigestIndex_Type()
)
bsoeVirtIfMessageDigestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsoeVirtIfMessageDigestIndex.setStatus("current")


class _BsoeVirtIfMessageDigestType_Type(Integer32):
    """Custom type bsoeVirtIfMessageDigestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("md5", 1)
    )


_BsoeVirtIfMessageDigestType_Type.__name__ = "Integer32"
_BsoeVirtIfMessageDigestType_Object = MibTableColumn
bsoeVirtIfMessageDigestType = _BsoeVirtIfMessageDigestType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 6, 1, 4),
    _BsoeVirtIfMessageDigestType_Type()
)
bsoeVirtIfMessageDigestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsoeVirtIfMessageDigestType.setStatus("current")


class _BsoeVirtIfMessageDigestKey_Type(OctetString):
    """Custom type bsoeVirtIfMessageDigestKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BsoeVirtIfMessageDigestKey_Type.__name__ = "OctetString"
_BsoeVirtIfMessageDigestKey_Object = MibTableColumn
bsoeVirtIfMessageDigestKey = _BsoeVirtIfMessageDigestKey_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 6, 1, 5),
    _BsoeVirtIfMessageDigestKey_Type()
)
bsoeVirtIfMessageDigestKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsoeVirtIfMessageDigestKey.setStatus("current")
_BsoeVirtIfMessageDigestRowStatus_Type = RowStatus
_BsoeVirtIfMessageDigestRowStatus_Object = MibTableColumn
bsoeVirtIfMessageDigestRowStatus = _BsoeVirtIfMessageDigestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 14, 1, 6, 1, 6),
    _BsoeVirtIfMessageDigestRowStatus_Type()
)
bsoeVirtIfMessageDigestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsoeVirtIfMessageDigestRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-OSPF-EXT-MIB",
    **{"bayStackOspfExtMib": bayStackOspfExtMib,
       "bsoeNotifications": bsoeNotifications,
       "bsoeObjects": bsoeObjects,
       "bsoeScalars": bsoeScalars,
       "bsoeApplyRedistribute": bsoeApplyRedistribute,
       "bsoeHardwareCompatibilityMode": bsoeHardwareCompatibilityMode,
       "bsoeOspfIfExtTable": bsoeOspfIfExtTable,
       "bsoeOspfIfExtEntry": bsoeOspfIfExtEntry,
       "bsoeOspfIfIpAddress": bsoeOspfIfIpAddress,
       "bsoeOspfAddressLessIf": bsoeOspfAddressLessIf,
       "bsoeOspfIfExtAdvertiseWhenDown": bsoeOspfIfExtAdvertiseWhenDown,
       "bsoeOspfIfExtPrimaryMd5Key": bsoeOspfIfExtPrimaryMd5Key,
       "bsoeOspfIfExtMtuIgnore": bsoeOspfIfExtMtuIgnore,
       "bsoeOspfIfExtType": bsoeOspfIfExtType,
       "bsoeMessageDigestTable": bsoeMessageDigestTable,
       "bsoeMessageDigestEntry": bsoeMessageDigestEntry,
       "bsoeMessageDigestIpAddress": bsoeMessageDigestIpAddress,
       "bsoeMessageDigestAddressLessIf": bsoeMessageDigestAddressLessIf,
       "bsoeMessageDigestIndex": bsoeMessageDigestIndex,
       "bsoeMessageDigestType": bsoeMessageDigestType,
       "bsoeMessageDigestKey": bsoeMessageDigestKey,
       "bsoeMessageDigestRowStatus": bsoeMessageDigestRowStatus,
       "bsoeOspfNbrExtTable": bsoeOspfNbrExtTable,
       "bsoeOspfNbrExtEntry": bsoeOspfNbrExtEntry,
       "bsoeOspfNbrExtIpAddr": bsoeOspfNbrExtIpAddr,
       "bsoeOspfNbrExtAddressLessIndex": bsoeOspfNbrExtAddressLessIndex,
       "bsoeOspfNbrExtInterfaceAddr": bsoeOspfNbrExtInterfaceAddr,
       "bsoeOspfVirtIfExtTable": bsoeOspfVirtIfExtTable,
       "bsoeOspfVirtIfExtEntry": bsoeOspfVirtIfExtEntry,
       "bsoeOspfVirtIfExtAreaId": bsoeOspfVirtIfExtAreaId,
       "bsoeOspfVirtIfExtNeighbor": bsoeOspfVirtIfExtNeighbor,
       "bsoeOspfVirtIfExtPrimaryMd5Key": bsoeOspfVirtIfExtPrimaryMd5Key,
       "bsoeOspfVirtIfExtType": bsoeOspfVirtIfExtType,
       "bsoeVirtIfMessageDigestTable": bsoeVirtIfMessageDigestTable,
       "bsoeVirtIfMessageDigestEntry": bsoeVirtIfMessageDigestEntry,
       "bsoeVirtIfMessageDigestAreaId": bsoeVirtIfMessageDigestAreaId,
       "bsoeVirtIfMessageDigestNeighbor": bsoeVirtIfMessageDigestNeighbor,
       "bsoeVirtIfMessageDigestIndex": bsoeVirtIfMessageDigestIndex,
       "bsoeVirtIfMessageDigestType": bsoeVirtIfMessageDigestType,
       "bsoeVirtIfMessageDigestKey": bsoeVirtIfMessageDigestKey,
       "bsoeVirtIfMessageDigestRowStatus": bsoeVirtIfMessageDigestRowStatus}
)
