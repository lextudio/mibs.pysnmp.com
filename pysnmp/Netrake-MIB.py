# SNMP MIB module (Netrake-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Netrake-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:11 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

netrake = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10950)
)
netrake.setRevisions(
        ("2001-09-20 10:05",
         "2006-12-13 10:05",
         "2007-01-05 10:05")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1)
)
_NCite_ObjectIdentity = ObjectIdentity
nCite = _NCite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1)
)
_Chassis_ObjectIdentity = ObjectIdentity
chassis = _Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1)
)
_ChasGen_ObjectIdentity = ObjectIdentity
chasGen = _ChasGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 1)
)
_ChasSerNum_Type = DisplayString
_ChasSerNum_Object = MibScalar
chasSerNum = _ChasSerNum_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 1, 1),
    _ChasSerNum_Type()
)
chasSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSerNum.setStatus("current")


class _ChasLedStatus_Type(Integer32):
    """Custom type chasLedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_ChasLedStatus_Type.__name__ = "Integer32"
_ChasLedStatus_Object = MibScalar
chasLedStatus = _ChasLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 1, 2),
    _ChasLedStatus_Type()
)
chasLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasLedStatus.setStatus("current")


class _ChasPOSTMode_Type(Integer32):
    """Custom type chasPOSTMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fastPOST", 0),
          ("fullPost", 1))
    )


_ChasPOSTMode_Type.__name__ = "Integer32"
_ChasPOSTMode_Object = MibScalar
chasPOSTMode = _ChasPOSTMode_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 1, 3),
    _ChasPOSTMode_Type()
)
chasPOSTMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasPOSTMode.setStatus("current")


class _ChasType_Type(Integer32):
    """Custom type chasType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bff", 1),
          ("sff", 2),
          ("unknown", 0))
    )


_ChasType_Type.__name__ = "Integer32"
_ChasType_Object = MibScalar
chasType = _ChasType_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 1, 4),
    _ChasType_Type()
)
chasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasType.setStatus("current")
_ChasPwr_ObjectIdentity = ObjectIdentity
chasPwr = _ChasPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 2)
)
_ChasPwrSupplyTable_Object = MibTable
chasPwrSupplyTable = _ChasPwrSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    chasPwrSupplyTable.setStatus("current")
_ChasPwrSupplyEntry_Object = MibTableRow
chasPwrSupplyEntry = _ChasPwrSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 2, 1, 1)
)
chasPwrSupplyEntry.setIndexNames(
    (0, "Netrake-MIB", "chasPwrSupplyIndex"),
)
if mibBuilder.loadTexts:
    chasPwrSupplyEntry.setStatus("current")
_ChasPwrSupplyIndex_Type = Integer32
_ChasPwrSupplyIndex_Object = MibTableColumn
chasPwrSupplyIndex = _ChasPwrSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 2, 1, 1, 1),
    _ChasPwrSupplyIndex_Type()
)
chasPwrSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPwrSupplyIndex.setStatus("current")


class _ChasPwrSupplyOperStatus_Type(Integer32):
    """Custom type chasPwrSupplyOperStatus based on Integer32"""
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
        *(("fault", 3),
          ("normal", 2),
          ("notPresent", 4),
          ("unknown", 1))
    )


_ChasPwrSupplyOperStatus_Type.__name__ = "Integer32"
_ChasPwrSupplyOperStatus_Object = MibTableColumn
chasPwrSupplyOperStatus = _ChasPwrSupplyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 2, 1, 1, 2),
    _ChasPwrSupplyOperStatus_Type()
)
chasPwrSupplyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPwrSupplyOperStatus.setStatus("current")
_ChasPwrSupplyDesc_Type = DisplayString
_ChasPwrSupplyDesc_Object = MibTableColumn
chasPwrSupplyDesc = _ChasPwrSupplyDesc_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 2, 1, 1, 3),
    _ChasPwrSupplyDesc_Type()
)
chasPwrSupplyDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPwrSupplyDesc.setStatus("current")


class _ChasPwrTrapAck_Type(Integer32):
    """Custom type chasPwrTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("notAck", 0))
    )


_ChasPwrTrapAck_Type.__name__ = "Integer32"
_ChasPwrTrapAck_Object = MibScalar
chasPwrTrapAck = _ChasPwrTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 2, 3),
    _ChasPwrTrapAck_Type()
)
chasPwrTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasPwrTrapAck.setStatus("current")
_ChasPwrTrapAckSource_Type = IpAddress
_ChasPwrTrapAckSource_Object = MibScalar
chasPwrTrapAckSource = _ChasPwrTrapAckSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 2, 4),
    _ChasPwrTrapAckSource_Type()
)
chasPwrTrapAckSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasPwrTrapAckSource.setStatus("current")
_ChasFan_ObjectIdentity = ObjectIdentity
chasFan = _ChasFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 3)
)
_ChasFanTable_Object = MibTable
chasFanTable = _ChasFanTable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    chasFanTable.setStatus("current")
_ChasFanEntry_Object = MibTableRow
chasFanEntry = _ChasFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 3, 1, 1)
)
chasFanEntry.setIndexNames(
    (0, "Netrake-MIB", "chasFanIndex"),
)
if mibBuilder.loadTexts:
    chasFanEntry.setStatus("current")
_ChasFanIndex_Type = Integer32
_ChasFanIndex_Object = MibTableColumn
chasFanIndex = _ChasFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 3, 1, 1, 1),
    _ChasFanIndex_Type()
)
chasFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasFanIndex.setStatus("current")


class _ChasFanOperStatus_Type(Integer32):
    """Custom type chasFanOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dev_fail", 1),
          ("dev_not_present", 3),
          ("dev_ok", 0),
          ("dev_present", 2),
          ("unknown", 4))
    )


_ChasFanOperStatus_Type.__name__ = "Integer32"
_ChasFanOperStatus_Object = MibTableColumn
chasFanOperStatus = _ChasFanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 3, 1, 1, 2),
    _ChasFanOperStatus_Type()
)
chasFanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasFanOperStatus.setStatus("current")
_ChasFanDescription_Type = DisplayString
_ChasFanDescription_Object = MibTableColumn
chasFanDescription = _ChasFanDescription_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 3, 1, 1, 3),
    _ChasFanDescription_Type()
)
chasFanDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasFanDescription.setStatus("current")


class _ChasFanTrapAck_Type(Integer32):
    """Custom type chasFanTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("notAck", 0))
    )


_ChasFanTrapAck_Type.__name__ = "Integer32"
_ChasFanTrapAck_Object = MibScalar
chasFanTrapAck = _ChasFanTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 3, 3),
    _ChasFanTrapAck_Type()
)
chasFanTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasFanTrapAck.setStatus("current")
_ChasFanTrapAckSource_Type = IpAddress
_ChasFanTrapAckSource_Object = MibScalar
chasFanTrapAckSource = _ChasFanTrapAckSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 3, 4),
    _ChasFanTrapAckSource_Type()
)
chasFanTrapAckSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasFanTrapAckSource.setStatus("current")
_ChasBrd_ObjectIdentity = ObjectIdentity
chasBrd = _ChasBrd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 4)
)
_ChasBrdTable_Object = MibTable
chasBrdTable = _ChasBrdTable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    chasBrdTable.setStatus("current")
_ChasBrdEntry_Object = MibTableRow
chasBrdEntry = _ChasBrdEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 4, 1, 1)
)
chasBrdEntry.setIndexNames(
    (0, "Netrake-MIB", "chasBrdSlotNum"),
)
if mibBuilder.loadTexts:
    chasBrdEntry.setStatus("current")


class _ChasBrdSlotNum_Type(Integer32):
    """Custom type chasBrdSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_ChasBrdSlotNum_Type.__name__ = "Integer32"
_ChasBrdSlotNum_Object = MibTableColumn
chasBrdSlotNum = _ChasBrdSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 4, 1, 1, 1),
    _ChasBrdSlotNum_Type()
)
chasBrdSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasBrdSlotNum.setStatus("current")
_ChasBrdDescription_Type = DisplayString
_ChasBrdDescription_Object = MibTableColumn
chasBrdDescription = _ChasBrdDescription_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 4, 1, 1, 2),
    _ChasBrdDescription_Type()
)
chasBrdDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasBrdDescription.setStatus("current")


class _ChasBrdType_Type(Integer32):
    """Custom type chasBrdType based on Integer32"""
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
        *(("controlProc", 2),
          ("fastEther", 5),
          ("gigE", 4),
          ("managementProc", 1),
          ("netrakeControlProcessor", 3),
          ("noBoardPresent", 0))
    )


_ChasBrdType_Type.__name__ = "Integer32"
_ChasBrdType_Object = MibTableColumn
chasBrdType = _ChasBrdType_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 4, 1, 1, 3),
    _ChasBrdType_Type()
)
chasBrdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasBrdType.setStatus("current")


class _ChasBrdOccSlots_Type(Integer32):
    """Custom type chasBrdOccSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_ChasBrdOccSlots_Type.__name__ = "Integer32"
_ChasBrdOccSlots_Object = MibTableColumn
chasBrdOccSlots = _ChasBrdOccSlots_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 4, 1, 1, 4),
    _ChasBrdOccSlots_Type()
)
chasBrdOccSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasBrdOccSlots.setStatus("current")
_ChasBrdMaxPorts_Type = Integer32
_ChasBrdMaxPorts_Object = MibTableColumn
chasBrdMaxPorts = _ChasBrdMaxPorts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 4, 1, 1, 5),
    _ChasBrdMaxPorts_Type()
)
chasBrdMaxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasBrdMaxPorts.setStatus("current")
_ChasBrdSlotLabel_Type = DisplayString
_ChasBrdSlotLabel_Object = MibTableColumn
chasBrdSlotLabel = _ChasBrdSlotLabel_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 4, 1, 1, 6),
    _ChasBrdSlotLabel_Type()
)
chasBrdSlotLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasBrdSlotLabel.setStatus("current")


class _ChasBrdStatusLeds_Type(Integer32):
    """Custom type chasBrdStatusLeds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_ChasBrdStatusLeds_Type.__name__ = "Integer32"
_ChasBrdStatusLeds_Object = MibTableColumn
chasBrdStatusLeds = _ChasBrdStatusLeds_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 4, 1, 1, 7),
    _ChasBrdStatusLeds_Type()
)
chasBrdStatusLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasBrdStatusLeds.setStatus("current")
_ChasBrdState_Type = DisplayString
_ChasBrdState_Object = MibTableColumn
chasBrdState = _ChasBrdState_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 4, 1, 1, 8),
    _ChasBrdState_Type()
)
chasBrdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasBrdState.setStatus("current")


class _ChasBrdPwr_Type(Integer32):
    """Custom type chasBrdPwr based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("powerOff", 2),
          ("powerOn", 1))
    )


_ChasBrdPwr_Type.__name__ = "Integer32"
_ChasBrdPwr_Object = MibTableColumn
chasBrdPwr = _ChasBrdPwr_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 4, 1, 1, 9),
    _ChasBrdPwr_Type()
)
chasBrdPwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasBrdPwr.setStatus("current")


class _ChasBrdIfIndex_Type(Integer32):
    """Custom type chasBrdIfIndex based on Integer32"""
    defaultValue = 0


_ChasBrdIfIndex_Object = MibTableColumn
chasBrdIfIndex = _ChasBrdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 4, 1, 1, 10),
    _ChasBrdIfIndex_Type()
)
chasBrdIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasBrdIfIndex.setStatus("current")
_ChasBrdSerialNum_Type = DisplayString
_ChasBrdSerialNum_Object = MibTableColumn
chasBrdSerialNum = _ChasBrdSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 4, 1, 1, 11),
    _ChasBrdSerialNum_Type()
)
chasBrdSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasBrdSerialNum.setStatus("current")


class _ChasBrdReset_Type(Integer32):
    """Custom type chasBrdReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("resetCold", 1),
          ("resetWarm", 2))
    )


_ChasBrdReset_Type.__name__ = "Integer32"
_ChasBrdReset_Object = MibTableColumn
chasBrdReset = _ChasBrdReset_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 4, 1, 1, 12),
    _ChasBrdReset_Type()
)
chasBrdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasBrdReset.setStatus("current")


class _ChasBrdStateChangeTrapAck_Type(Integer32):
    """Custom type chasBrdStateChangeTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("notAck", 0))
    )


_ChasBrdStateChangeTrapAck_Type.__name__ = "Integer32"
_ChasBrdStateChangeTrapAck_Object = MibScalar
chasBrdStateChangeTrapAck = _ChasBrdStateChangeTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 4, 3),
    _ChasBrdStateChangeTrapAck_Type()
)
chasBrdStateChangeTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasBrdStateChangeTrapAck.setStatus("current")
_ChasBrdStateChangeTrapAckSource_Type = IpAddress
_ChasBrdStateChangeTrapAckSource_Object = MibScalar
chasBrdStateChangeTrapAckSource = _ChasBrdStateChangeTrapAckSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 4, 4),
    _ChasBrdStateChangeTrapAckSource_Type()
)
chasBrdStateChangeTrapAckSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasBrdStateChangeTrapAckSource.setStatus("current")
_NCiteSystem_ObjectIdentity = ObjectIdentity
nCiteSystem = _NCiteSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 2)
)
_ResourceUsageTable_Object = MibTable
resourceUsageTable = _ResourceUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    resourceUsageTable.setStatus("current")
_ResourceUsageEntry_Object = MibTableRow
resourceUsageEntry = _ResourceUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 2, 1, 1)
)
resourceUsageEntry.setIndexNames(
    (0, "Netrake-MIB", "processorIndex"),
)
if mibBuilder.loadTexts:
    resourceUsageEntry.setStatus("current")


class _ProcessorIndex_Type(Integer32):
    """Custom type processorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("controlProcA", 2),
          ("controlProcB", 3),
          ("managementProc", 1))
    )


_ProcessorIndex_Type.__name__ = "Integer32"
_ProcessorIndex_Object = MibTableColumn
processorIndex = _ProcessorIndex_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 2, 1, 1, 1),
    _ProcessorIndex_Type()
)
processorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorIndex.setStatus("current")


class _MemTotal_Type(Integer32):
    """Custom type memTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MemTotal_Type.__name__ = "Integer32"
_MemTotal_Object = MibTableColumn
memTotal = _MemTotal_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 2, 1, 1, 2),
    _MemTotal_Type()
)
memTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotal.setStatus("current")
_MemUsed_Type = Integer32
_MemUsed_Object = MibTableColumn
memUsed = _MemUsed_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 2, 1, 1, 3),
    _MemUsed_Type()
)
memUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memUsed.setStatus("current")
_CpuUsage_Type = Integer32
_CpuUsage_Object = MibTableColumn
cpuUsage = _CpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 2, 1, 1, 4),
    _CpuUsage_Type()
)
cpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUsage.setStatus("current")
_SystemSoftwareVersion_Type = DisplayString
_SystemSoftwareVersion_Object = MibScalar
systemSoftwareVersion = _SystemSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 2, 2),
    _SystemSoftwareVersion_Type()
)
systemSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSoftwareVersion.setStatus("current")


class _SystemRestoreFlag_Type(Integer32):
    """Custom type systemRestoreFlag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("outOfSync", 1),
          ("refreshStarted", 2))
    )


_SystemRestoreFlag_Type.__name__ = "Integer32"
_SystemRestoreFlag_Object = MibScalar
systemRestoreFlag = _SystemRestoreFlag_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 2, 3),
    _SystemRestoreFlag_Type()
)
systemRestoreFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemRestoreFlag.setStatus("deprecated")
_SystemOperState_Type = DisplayString
_SystemOperState_Object = MibScalar
systemOperState = _SystemOperState_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 2, 4),
    _SystemOperState_Type()
)
systemOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemOperState.setStatus("current")


class _SystemAdminState_Type(Integer32):
    """Custom type systemAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_SystemAdminState_Type.__name__ = "Integer32"
_SystemAdminState_Object = MibScalar
systemAdminState = _SystemAdminState_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 2, 5),
    _SystemAdminState_Type()
)
systemAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemAdminState.setStatus("current")


class _SystemOperStateChangeTrapAck_Type(Integer32):
    """Custom type systemOperStateChangeTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("notAck", 0))
    )


_SystemOperStateChangeTrapAck_Type.__name__ = "Integer32"
_SystemOperStateChangeTrapAck_Object = MibScalar
systemOperStateChangeTrapAck = _SystemOperStateChangeTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 2, 7),
    _SystemOperStateChangeTrapAck_Type()
)
systemOperStateChangeTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemOperStateChangeTrapAck.setStatus("current")
_SystemOperStateChangeTrapAckSource_Type = IpAddress
_SystemOperStateChangeTrapAckSource_Object = MibScalar
systemOperStateChangeTrapAckSource = _SystemOperStateChangeTrapAckSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 2, 8),
    _SystemOperStateChangeTrapAckSource_Type()
)
systemOperStateChangeTrapAckSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemOperStateChangeTrapAckSource.setStatus("current")
_SystemTrapAckTable_Object = MibTable
systemTrapAckTable = _SystemTrapAckTable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 2, 9)
)
if mibBuilder.loadTexts:
    systemTrapAckTable.setStatus("current")
_SystemTrapAckEntry_Object = MibTableRow
systemTrapAckEntry = _SystemTrapAckEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 2, 9, 1)
)
systemTrapAckEntry.setIndexNames(
    (0, "Netrake-MIB", "systemSnmpMgrIpAddress"),
)
if mibBuilder.loadTexts:
    systemTrapAckEntry.setStatus("current")
_SystemSnmpMgrIpAddress_Type = IpAddress
_SystemSnmpMgrIpAddress_Object = MibTableColumn
systemSnmpMgrIpAddress = _SystemSnmpMgrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 2, 9, 1, 1),
    _SystemSnmpMgrIpAddress_Type()
)
systemSnmpMgrIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSnmpMgrIpAddress.setStatus("current")


class _SystemTrapNoAck_Type(Integer32):
    """Custom type systemTrapNoAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ackNotReceived", 1),
          ("ok", 0))
    )


_SystemTrapNoAck_Type.__name__ = "Integer32"
_SystemTrapNoAck_Object = MibTableColumn
systemTrapNoAck = _SystemTrapNoAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 2, 9, 1, 2),
    _SystemTrapNoAck_Type()
)
systemTrapNoAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemTrapNoAck.setStatus("current")
_Alarm_ObjectIdentity = ObjectIdentity
alarm = _Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 3)
)
_ActiveAlarmTable_Object = MibTable
activeAlarmTable = _ActiveAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    activeAlarmTable.setStatus("current")
_ActiveAlarmEntry_Object = MibTableRow
activeAlarmEntry = _ActiveAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 3, 1, 1)
)
activeAlarmEntry.setIndexNames(
    (0, "Netrake-MIB", "activeAlarmIndex"),
)
if mibBuilder.loadTexts:
    activeAlarmEntry.setStatus("current")


class _ActiveAlarmIndex_Type(Integer32):
    """Custom type activeAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_ActiveAlarmIndex_Type.__name__ = "Integer32"
_ActiveAlarmIndex_Object = MibTableColumn
activeAlarmIndex = _ActiveAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 3, 1, 1, 1),
    _ActiveAlarmIndex_Type()
)
activeAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmIndex.setStatus("current")


class _ActiveAlarmId_Type(Integer32):
    """Custom type activeAlarmId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_ActiveAlarmId_Type.__name__ = "Integer32"
_ActiveAlarmId_Object = MibTableColumn
activeAlarmId = _ActiveAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 3, 1, 1, 2),
    _ActiveAlarmId_Type()
)
activeAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmId.setStatus("current")


class _ActiveAlarmType_Type(Integer32):
    """Custom type activeAlarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_ActiveAlarmType_Type.__name__ = "Integer32"
_ActiveAlarmType_Object = MibTableColumn
activeAlarmType = _ActiveAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 3, 1, 1, 3),
    _ActiveAlarmType_Type()
)
activeAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmType.setStatus("current")


class _ActiveAlarmServiceAffecting_Type(Integer32):
    """Custom type activeAlarmServiceAffecting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notServiceAffecting", 1),
          ("serviceAffecting", 2))
    )


_ActiveAlarmServiceAffecting_Type.__name__ = "Integer32"
_ActiveAlarmServiceAffecting_Object = MibTableColumn
activeAlarmServiceAffecting = _ActiveAlarmServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 3, 1, 1, 4),
    _ActiveAlarmServiceAffecting_Type()
)
activeAlarmServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmServiceAffecting.setStatus("current")


class _ActiveAlarmCategory_Type(Integer32):
    """Custom type activeAlarmCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 1),
          ("service", 3),
          ("software", 2))
    )


_ActiveAlarmCategory_Type.__name__ = "Integer32"
_ActiveAlarmCategory_Object = MibTableColumn
activeAlarmCategory = _ActiveAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 3, 1, 1, 5),
    _ActiveAlarmCategory_Type()
)
activeAlarmCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmCategory.setStatus("current")
_ActiveAlarmTimeStamp_Type = DateAndTime
_ActiveAlarmTimeStamp_Object = MibTableColumn
activeAlarmTimeStamp = _ActiveAlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 3, 1, 1, 6),
    _ActiveAlarmTimeStamp_Type()
)
activeAlarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmTimeStamp.setStatus("current")


class _ActiveAlarmSlotNum_Type(Integer32):
    """Custom type activeAlarmSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_ActiveAlarmSlotNum_Type.__name__ = "Integer32"
_ActiveAlarmSlotNum_Object = MibTableColumn
activeAlarmSlotNum = _ActiveAlarmSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 3, 1, 1, 7),
    _ActiveAlarmSlotNum_Type()
)
activeAlarmSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmSlotNum.setStatus("current")


class _ActiveAlarmPortNum_Type(Integer32):
    """Custom type activeAlarmPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ActiveAlarmPortNum_Type.__name__ = "Integer32"
_ActiveAlarmPortNum_Object = MibTableColumn
activeAlarmPortNum = _ActiveAlarmPortNum_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 3, 1, 1, 8),
    _ActiveAlarmPortNum_Type()
)
activeAlarmPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmPortNum.setStatus("current")
_ActiveAlarmSysUpTime_Type = TimeTicks
_ActiveAlarmSysUpTime_Object = MibTableColumn
activeAlarmSysUpTime = _ActiveAlarmSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 3, 1, 1, 9),
    _ActiveAlarmSysUpTime_Type()
)
activeAlarmSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmSysUpTime.setStatus("current")


class _ActiveAlarmDevType_Type(Integer32):
    """Custom type activeAlarmDevType based on Integer32"""
    defaultValue = 0

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
        *(("chassisFan", 6),
          ("chassisPowerSupply", 7),
          ("controlProc", 2),
          ("fastEther", 5),
          ("gigE", 4),
          ("managementProc", 1),
          ("netrakeControlProcessor", 3),
          ("oc12", 8),
          ("unknown", 0))
    )


_ActiveAlarmDevType_Type.__name__ = "Integer32"
_ActiveAlarmDevType_Object = MibTableColumn
activeAlarmDevType = _ActiveAlarmDevType_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 3, 1, 1, 10),
    _ActiveAlarmDevType_Type()
)
activeAlarmDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmDevType.setStatus("current")


class _ActiveAlarmAdditionalInfo_Type(DisplayString):
    """Custom type activeAlarmAdditionalInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ActiveAlarmAdditionalInfo_Type.__name__ = "DisplayString"
_ActiveAlarmAdditionalInfo_Object = MibTableColumn
activeAlarmAdditionalInfo = _ActiveAlarmAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 3, 1, 1, 11),
    _ActiveAlarmAdditionalInfo_Type()
)
activeAlarmAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmAdditionalInfo.setStatus("current")


class _ActiveAlarmOccurances_Type(Integer32):
    """Custom type activeAlarmOccurances based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_ActiveAlarmOccurances_Type.__name__ = "Integer32"
_ActiveAlarmOccurances_Object = MibTableColumn
activeAlarmOccurances = _ActiveAlarmOccurances_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 3, 1, 1, 12),
    _ActiveAlarmOccurances_Type()
)
activeAlarmOccurances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmOccurances.setStatus("current")
_AcitveAlarmReportingSource_Type = Integer32
_AcitveAlarmReportingSource_Object = MibTableColumn
acitveAlarmReportingSource = _AcitveAlarmReportingSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 3, 1, 1, 13),
    _AcitveAlarmReportingSource_Type()
)
acitveAlarmReportingSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acitveAlarmReportingSource.setStatus("deprecated")


class _ActiveAlarmSeverity_Type(Integer32):
    """Custom type activeAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("clear", 5),
          ("critical", 1),
          ("info", 6),
          ("major", 2),
          ("minor", 3),
          ("unknown", 0),
          ("warning", 4))
    )


_ActiveAlarmSeverity_Type.__name__ = "Integer32"
_ActiveAlarmSeverity_Object = MibTableColumn
activeAlarmSeverity = _ActiveAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 3, 1, 1, 14),
    _ActiveAlarmSeverity_Type()
)
activeAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmSeverity.setStatus("current")
_ActiveAlarmDisplayString_Type = DisplayString
_ActiveAlarmDisplayString_Object = MibTableColumn
activeAlarmDisplayString = _ActiveAlarmDisplayString_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 3, 1, 1, 15),
    _ActiveAlarmDisplayString_Type()
)
activeAlarmDisplayString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmDisplayString.setStatus("current")
_ActiveAlarmSubType_Type = Integer32
_ActiveAlarmSubType_Object = MibTableColumn
activeAlarmSubType = _ActiveAlarmSubType_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 3, 1, 1, 16),
    _ActiveAlarmSubType_Type()
)
activeAlarmSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmSubType.setStatus("current")


class _ActiveAlarmEventFlag_Type(Integer32):
    """Custom type activeAlarmEventFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("event", 2))
    )


_ActiveAlarmEventFlag_Type.__name__ = "Integer32"
_ActiveAlarmEventFlag_Object = MibTableColumn
activeAlarmEventFlag = _ActiveAlarmEventFlag_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 3, 1, 1, 17),
    _ActiveAlarmEventFlag_Type()
)
activeAlarmEventFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmEventFlag.setStatus("current")
_HistEvent_ObjectIdentity = ObjectIdentity
histEvent = _HistEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 3, 2)
)
_PostEvent_ObjectIdentity = ObjectIdentity
postEvent = _PostEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 3, 4)
)


class _ActiveAlarmAcknowledge_Type(Integer32):
    """Custom type activeAlarmAcknowledge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("acknowledge", 1),
          ("cleared", 0))
    )


_ActiveAlarmAcknowledge_Type.__name__ = "Integer32"
_ActiveAlarmAcknowledge_Object = MibScalar
activeAlarmAcknowledge = _ActiveAlarmAcknowledge_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 3, 5),
    _ActiveAlarmAcknowledge_Type()
)
activeAlarmAcknowledge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeAlarmAcknowledge.setStatus("current")


class _ActiveAlarmID_Type(Integer32):
    """Custom type activeAlarmID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_ActiveAlarmID_Type.__name__ = "Integer32"
_ActiveAlarmID_Object = MibScalar
activeAlarmID = _ActiveAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 3, 6),
    _ActiveAlarmID_Type()
)
activeAlarmID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeAlarmID.setStatus("current")
_EventAcknowledge_ObjectIdentity = ObjectIdentity
eventAcknowledge = _EventAcknowledge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 3, 7)
)


class _EventID_Type(Integer32):
    """Custom type eventID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EventID_Type.__name__ = "Integer32"
_EventID_Object = MibScalar
eventID = _EventID_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 3, 8),
    _EventID_Type()
)
eventID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventID.setStatus("deprecated")
_ActiveAlarmAcknowledgeSource_Type = IpAddress
_ActiveAlarmAcknowledgeSource_Object = MibScalar
activeAlarmAcknowledgeSource = _ActiveAlarmAcknowledgeSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 3, 9),
    _ActiveAlarmAcknowledgeSource_Type()
)
activeAlarmAcknowledgeSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeAlarmAcknowledgeSource.setStatus("current")
_SwitchNotifications_ObjectIdentity = ObjectIdentity
switchNotifications = _SwitchNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 4)
)


class _ColdStartTrapEnable_Type(Integer32):
    """Custom type coldStartTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ColdStartTrapEnable_Type.__name__ = "Integer32"
_ColdStartTrapEnable_Object = MibScalar
coldStartTrapEnable = _ColdStartTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 4, 1),
    _ColdStartTrapEnable_Type()
)
coldStartTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coldStartTrapEnable.setStatus("current")


class _ColdStartTrapAck_Type(Integer32):
    """Custom type coldStartTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("notAck", 0))
    )


_ColdStartTrapAck_Type.__name__ = "Integer32"
_ColdStartTrapAck_Object = MibScalar
coldStartTrapAck = _ColdStartTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 4, 3),
    _ColdStartTrapAck_Type()
)
coldStartTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coldStartTrapAck.setStatus("current")
_ColdStartTrapAckSource_Type = IpAddress
_ColdStartTrapAckSource_Object = MibScalar
coldStartTrapAckSource = _ColdStartTrapAckSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 4, 4),
    _ColdStartTrapAckSource_Type()
)
coldStartTrapAckSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coldStartTrapAckSource.setStatus("current")
_NCiteRedundant_ObjectIdentity = ObjectIdentity
nCiteRedundant = _NCiteRedundant_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 5)
)
_RedundantPort1IpAddr_Type = IpAddress
_RedundantPort1IpAddr_Object = MibScalar
redundantPort1IpAddr = _RedundantPort1IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 5, 1),
    _RedundantPort1IpAddr_Type()
)
redundantPort1IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantPort1IpAddr.setStatus("current")
_RedundantPort2IpAddr_Type = IpAddress
_RedundantPort2IpAddr_Object = MibScalar
redundantPort2IpAddr = _RedundantPort2IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 5, 2),
    _RedundantPort2IpAddr_Type()
)
redundantPort2IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantPort2IpAddr.setStatus("current")


class _RedundantAdminState_Type(Integer32):
    """Custom type redundantAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("redundant", 2),
          ("standAlone", 1))
    )


_RedundantAdminState_Type.__name__ = "Integer32"
_RedundantAdminState_Object = MibScalar
redundantAdminState = _RedundantAdminState_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 5, 3),
    _RedundantAdminState_Type()
)
redundantAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantAdminState.setStatus("current")


class _RedundantMateName_Type(DisplayString):
    """Custom type redundantMateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RedundantMateName_Type.__name__ = "DisplayString"
_RedundantMateName_Object = MibScalar
redundantMateName = _RedundantMateName_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 5, 4),
    _RedundantMateName_Type()
)
redundantMateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantMateName.setStatus("current")


class _RedundantConfigChangeTrapAck_Type(Integer32):
    """Custom type redundantConfigChangeTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("notAck", 0))
    )


_RedundantConfigChangeTrapAck_Type.__name__ = "Integer32"
_RedundantConfigChangeTrapAck_Object = MibScalar
redundantConfigChangeTrapAck = _RedundantConfigChangeTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 5, 6),
    _RedundantConfigChangeTrapAck_Type()
)
redundantConfigChangeTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantConfigChangeTrapAck.setStatus("current")
_RedundantPort1NetMask_Type = IpAddress
_RedundantPort1NetMask_Object = MibScalar
redundantPort1NetMask = _RedundantPort1NetMask_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 5, 8),
    _RedundantPort1NetMask_Type()
)
redundantPort1NetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantPort1NetMask.setStatus("current")
_RedundantPort2NetMask_Type = IpAddress
_RedundantPort2NetMask_Object = MibScalar
redundantPort2NetMask = _RedundantPort2NetMask_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 5, 9),
    _RedundantPort2NetMask_Type()
)
redundantPort2NetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantPort2NetMask.setStatus("current")


class _RedundantFailbackThresh_Type(Integer32):
    """Custom type redundantFailbackThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_RedundantFailbackThresh_Type.__name__ = "Integer32"
_RedundantFailbackThresh_Object = MibScalar
redundantFailbackThresh = _RedundantFailbackThresh_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 5, 10),
    _RedundantFailbackThresh_Type()
)
redundantFailbackThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantFailbackThresh.setStatus("current")


class _RedundantRedirectorFlag_Type(Integer32):
    """Custom type redundantRedirectorFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RedundantRedirectorFlag_Type.__name__ = "Integer32"
_RedundantRedirectorFlag_Object = MibScalar
redundantRedirectorFlag = _RedundantRedirectorFlag_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 5, 11),
    _RedundantRedirectorFlag_Type()
)
redundantRedirectorFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantRedirectorFlag.setStatus("current")


class _RedundantFailbackThreshChangeTrapAck_Type(Integer32):
    """Custom type redundantFailbackThreshChangeTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("default", 0))
    )


_RedundantFailbackThreshChangeTrapAck_Type.__name__ = "Integer32"
_RedundantFailbackThreshChangeTrapAck_Object = MibScalar
redundantFailbackThreshChangeTrapAck = _RedundantFailbackThreshChangeTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 5, 13),
    _RedundantFailbackThreshChangeTrapAck_Type()
)
redundantFailbackThreshChangeTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantFailbackThreshChangeTrapAck.setStatus("current")


class _RedundantRedirectorFlagChangeTrapAck_Type(Integer32):
    """Custom type redundantRedirectorFlagChangeTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("default", 0))
    )


_RedundantRedirectorFlagChangeTrapAck_Type.__name__ = "Integer32"
_RedundantRedirectorFlagChangeTrapAck_Object = MibScalar
redundantRedirectorFlagChangeTrapAck = _RedundantRedirectorFlagChangeTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 5, 15),
    _RedundantRedirectorFlagChangeTrapAck_Type()
)
redundantRedirectorFlagChangeTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantRedirectorFlagChangeTrapAck.setStatus("current")


class _RedundantAutoFailbackFlag_Type(Integer32):
    """Custom type redundantAutoFailbackFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RedundantAutoFailbackFlag_Type.__name__ = "Integer32"
_RedundantAutoFailbackFlag_Object = MibScalar
redundantAutoFailbackFlag = _RedundantAutoFailbackFlag_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 5, 16),
    _RedundantAutoFailbackFlag_Type()
)
redundantAutoFailbackFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantAutoFailbackFlag.setStatus("current")


class _RedundantAutoFailbackFlagChangeTrapAck_Type(Integer32):
    """Custom type redundantAutoFailbackFlagChangeTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("default", 0))
    )


_RedundantAutoFailbackFlagChangeTrapAck_Type.__name__ = "Integer32"
_RedundantAutoFailbackFlagChangeTrapAck_Object = MibScalar
redundantAutoFailbackFlagChangeTrapAck = _RedundantAutoFailbackFlagChangeTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 5, 18),
    _RedundantAutoFailbackFlagChangeTrapAck_Type()
)
redundantAutoFailbackFlagChangeTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantAutoFailbackFlagChangeTrapAck.setStatus("current")
_RedundantConfigChangeTrapAckSource_Type = IpAddress
_RedundantConfigChangeTrapAckSource_Object = MibScalar
redundantConfigChangeTrapAckSource = _RedundantConfigChangeTrapAckSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 5, 19),
    _RedundantConfigChangeTrapAckSource_Type()
)
redundantConfigChangeTrapAckSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantConfigChangeTrapAckSource.setStatus("current")
_RedundantFailbackThreshChangeTrapAckSource_Type = IpAddress
_RedundantFailbackThreshChangeTrapAckSource_Object = MibScalar
redundantFailbackThreshChangeTrapAckSource = _RedundantFailbackThreshChangeTrapAckSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 5, 20),
    _RedundantFailbackThreshChangeTrapAckSource_Type()
)
redundantFailbackThreshChangeTrapAckSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantFailbackThreshChangeTrapAckSource.setStatus("current")
_RedundantRedirectorFlagChangeTrapAckSource_Type = IpAddress
_RedundantRedirectorFlagChangeTrapAckSource_Object = MibScalar
redundantRedirectorFlagChangeTrapAckSource = _RedundantRedirectorFlagChangeTrapAckSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 5, 21),
    _RedundantRedirectorFlagChangeTrapAckSource_Type()
)
redundantRedirectorFlagChangeTrapAckSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantRedirectorFlagChangeTrapAckSource.setStatus("current")
_RedundantAutoFailbackFlagChangeTrapAckSource_Type = IpAddress
_RedundantAutoFailbackFlagChangeTrapAckSource_Object = MibScalar
redundantAutoFailbackFlagChangeTrapAckSource = _RedundantAutoFailbackFlagChangeTrapAckSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 5, 22),
    _RedundantAutoFailbackFlagChangeTrapAckSource_Type()
)
redundantAutoFailbackFlagChangeTrapAckSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantAutoFailbackFlagChangeTrapAckSource.setStatus("current")
_NCiteStats_ObjectIdentity = ObjectIdentity
nCiteStats = _NCiteStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6)
)
_GlobalCounters_ObjectIdentity = ObjectIdentity
globalCounters = _GlobalCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 1)
)
_TotalPacketsXmitCPA_Type = Counter64
_TotalPacketsXmitCPA_Object = MibScalar
totalPacketsXmitCPA = _TotalPacketsXmitCPA_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 1, 1),
    _TotalPacketsXmitCPA_Type()
)
totalPacketsXmitCPA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalPacketsXmitCPA.setStatus("current")
_NumPacketsDiscardCPA_Type = Counter64
_NumPacketsDiscardCPA_Object = MibScalar
numPacketsDiscardCPA = _NumPacketsDiscardCPA_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 1, 2),
    _NumPacketsDiscardCPA_Type()
)
numPacketsDiscardCPA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numPacketsDiscardCPA.setStatus("current")
_TotalPacketsXmitCPB_Type = Counter64
_TotalPacketsXmitCPB_Object = MibScalar
totalPacketsXmitCPB = _TotalPacketsXmitCPB_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 1, 3),
    _TotalPacketsXmitCPB_Type()
)
totalPacketsXmitCPB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalPacketsXmitCPB.setStatus("current")
_NumPacketsDiscardCPB_Type = Counter64
_NumPacketsDiscardCPB_Object = MibScalar
numPacketsDiscardCPB = _NumPacketsDiscardCPB_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 1, 4),
    _NumPacketsDiscardCPB_Type()
)
numPacketsDiscardCPB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numPacketsDiscardCPB.setStatus("current")
_TotalPacketsXmit_Type = Counter64
_TotalPacketsXmit_Object = MibScalar
totalPacketsXmit = _TotalPacketsXmit_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 1, 5),
    _TotalPacketsXmit_Type()
)
totalPacketsXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalPacketsXmit.setStatus("current")
_TotalPacketsDiscard_Type = Counter64
_TotalPacketsDiscard_Object = MibScalar
totalPacketsDiscard = _TotalPacketsDiscard_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 1, 6),
    _TotalPacketsDiscard_Type()
)
totalPacketsDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalPacketsDiscard.setStatus("current")
_GigEStats_ObjectIdentity = ObjectIdentity
gigEStats = _GigEStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2)
)
_GigEStatsTable_Object = MibTable
gigEStatsTable = _GigEStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    gigEStatsTable.setStatus("current")
_GigEStatsEntry_Object = MibTableRow
gigEStatsEntry = _GigEStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1)
)
gigEStatsEntry.setIndexNames(
    (0, "Netrake-MIB", "gigEStatsPortIndex"),
    (0, "Netrake-MIB", "gigEStatsSlotNum"),
)
if mibBuilder.loadTexts:
    gigEStatsEntry.setStatus("current")


class _GigEStatsPortIndex_Type(Integer32):
    """Custom type gigEStatsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_GigEStatsPortIndex_Type.__name__ = "Integer32"
_GigEStatsPortIndex_Object = MibTableColumn
gigEStatsPortIndex = _GigEStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 1),
    _GigEStatsPortIndex_Type()
)
gigEStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigEStatsPortIndex.setStatus("current")


class _GigEStatsSlotNum_Type(Integer32):
    """Custom type gigEStatsSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_GigEStatsSlotNum_Type.__name__ = "Integer32"
_GigEStatsSlotNum_Object = MibTableColumn
gigEStatsSlotNum = _GigEStatsSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 2),
    _GigEStatsSlotNum_Type()
)
gigEStatsSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigEStatsSlotNum.setStatus("current")
_LinkStatusChanges_Type = Counter64
_LinkStatusChanges_Object = MibTableColumn
linkStatusChanges = _LinkStatusChanges_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 3),
    _LinkStatusChanges_Type()
)
linkStatusChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusChanges.setStatus("current")
_FramesRcvdOkCount_Type = Counter64
_FramesRcvdOkCount_Object = MibTableColumn
framesRcvdOkCount = _FramesRcvdOkCount_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 4),
    _FramesRcvdOkCount_Type()
)
framesRcvdOkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    framesRcvdOkCount.setStatus("current")
_OctetsRcvdOkCount_Type = Counter64
_OctetsRcvdOkCount_Object = MibTableColumn
octetsRcvdOkCount = _OctetsRcvdOkCount_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 5),
    _OctetsRcvdOkCount_Type()
)
octetsRcvdOkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetsRcvdOkCount.setStatus("current")
_FramesRcvdCount_Type = Counter64
_FramesRcvdCount_Object = MibTableColumn
framesRcvdCount = _FramesRcvdCount_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 6),
    _FramesRcvdCount_Type()
)
framesRcvdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    framesRcvdCount.setStatus("current")
_OctetsRcvdCount_Type = Counter64
_OctetsRcvdCount_Object = MibTableColumn
octetsRcvdCount = _OctetsRcvdCount_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 7),
    _OctetsRcvdCount_Type()
)
octetsRcvdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetsRcvdCount.setStatus("current")
_FrameSeqErrCount_Type = Counter64
_FrameSeqErrCount_Object = MibTableColumn
frameSeqErrCount = _FrameSeqErrCount_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 8),
    _FrameSeqErrCount_Type()
)
frameSeqErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameSeqErrCount.setStatus("current")
_LostFramesMacErrCount_Type = Counter64
_LostFramesMacErrCount_Object = MibTableColumn
lostFramesMacErrCount = _LostFramesMacErrCount_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 9),
    _LostFramesMacErrCount_Type()
)
lostFramesMacErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lostFramesMacErrCount.setStatus("current")
_RcvdFrames64Octets_Type = Counter64
_RcvdFrames64Octets_Object = MibTableColumn
rcvdFrames64Octets = _RcvdFrames64Octets_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 10),
    _RcvdFrames64Octets_Type()
)
rcvdFrames64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvdFrames64Octets.setStatus("current")
_OctetsRcvd1519toMax_Type = Counter64
_OctetsRcvd1519toMax_Object = MibTableColumn
octetsRcvd1519toMax = _OctetsRcvd1519toMax_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 11),
    _OctetsRcvd1519toMax_Type()
)
octetsRcvd1519toMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetsRcvd1519toMax.setStatus("current")
_XmitFrames64Octets_Type = Counter64
_XmitFrames64Octets_Object = MibTableColumn
xmitFrames64Octets = _XmitFrames64Octets_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 12),
    _XmitFrames64Octets_Type()
)
xmitFrames64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmitFrames64Octets.setStatus("current")
_OctetsXmit1024to1518_Type = Counter64
_OctetsXmit1024to1518_Object = MibTableColumn
octetsXmit1024to1518 = _OctetsXmit1024to1518_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 13),
    _OctetsXmit1024to1518_Type()
)
octetsXmit1024to1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetsXmit1024to1518.setStatus("current")
_OctetsXmitCount_Type = Counter64
_OctetsXmitCount_Object = MibTableColumn
octetsXmitCount = _OctetsXmitCount_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 14),
    _OctetsXmitCount_Type()
)
octetsXmitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetsXmitCount.setStatus("current")
_UnicastFramesXmitOk_Type = Counter64
_UnicastFramesXmitOk_Object = MibTableColumn
unicastFramesXmitOk = _UnicastFramesXmitOk_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 15),
    _UnicastFramesXmitOk_Type()
)
unicastFramesXmitOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unicastFramesXmitOk.setStatus("current")
_UnicastFramesRcvdOk_Type = Counter64
_UnicastFramesRcvdOk_Object = MibTableColumn
unicastFramesRcvdOk = _UnicastFramesRcvdOk_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 16),
    _UnicastFramesRcvdOk_Type()
)
unicastFramesRcvdOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unicastFramesRcvdOk.setStatus("current")
_BroadcastFramesXmitOk_Type = Counter64
_BroadcastFramesXmitOk_Object = MibTableColumn
broadcastFramesXmitOk = _BroadcastFramesXmitOk_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 17),
    _BroadcastFramesXmitOk_Type()
)
broadcastFramesXmitOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    broadcastFramesXmitOk.setStatus("current")
_BroadcastFramesRcvdOk_Type = Counter64
_BroadcastFramesRcvdOk_Object = MibTableColumn
broadcastFramesRcvdOk = _BroadcastFramesRcvdOk_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 18),
    _BroadcastFramesRcvdOk_Type()
)
broadcastFramesRcvdOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    broadcastFramesRcvdOk.setStatus("current")
_MulticastFramesXmitOk_Type = Counter64
_MulticastFramesXmitOk_Object = MibTableColumn
multicastFramesXmitOk = _MulticastFramesXmitOk_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 19),
    _MulticastFramesXmitOk_Type()
)
multicastFramesXmitOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastFramesXmitOk.setStatus("current")
_MulticastFramesRcvdOk_Type = Counter64
_MulticastFramesRcvdOk_Object = MibTableColumn
multicastFramesRcvdOk = _MulticastFramesRcvdOk_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 20),
    _MulticastFramesRcvdOk_Type()
)
multicastFramesRcvdOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastFramesRcvdOk.setStatus("current")
_OctetsRcvd65to127_Type = Counter64
_OctetsRcvd65to127_Object = MibTableColumn
octetsRcvd65to127 = _OctetsRcvd65to127_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 21),
    _OctetsRcvd65to127_Type()
)
octetsRcvd65to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetsRcvd65to127.setStatus("current")
_OctetsXmit65to127_Type = Counter64
_OctetsXmit65to127_Object = MibTableColumn
octetsXmit65to127 = _OctetsXmit65to127_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 22),
    _OctetsXmit65to127_Type()
)
octetsXmit65to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetsXmit65to127.setStatus("current")
_OctetRcvd128to255_Type = Counter64
_OctetRcvd128to255_Object = MibTableColumn
octetRcvd128to255 = _OctetRcvd128to255_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 23),
    _OctetRcvd128to255_Type()
)
octetRcvd128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetRcvd128to255.setStatus("current")
_OctetsXmit128to255_Type = Counter64
_OctetsXmit128to255_Object = MibTableColumn
octetsXmit128to255 = _OctetsXmit128to255_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 24),
    _OctetsXmit128to255_Type()
)
octetsXmit128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetsXmit128to255.setStatus("current")
_OctetsRcvd256to511_Type = Counter64
_OctetsRcvd256to511_Object = MibTableColumn
octetsRcvd256to511 = _OctetsRcvd256to511_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 25),
    _OctetsRcvd256to511_Type()
)
octetsRcvd256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetsRcvd256to511.setStatus("current")
_OctetsXmit256to511_Type = Counter64
_OctetsXmit256to511_Object = MibTableColumn
octetsXmit256to511 = _OctetsXmit256to511_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 26),
    _OctetsXmit256to511_Type()
)
octetsXmit256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetsXmit256to511.setStatus("current")
_OctetsRcvd512to1023_Type = Counter64
_OctetsRcvd512to1023_Object = MibTableColumn
octetsRcvd512to1023 = _OctetsRcvd512to1023_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 27),
    _OctetsRcvd512to1023_Type()
)
octetsRcvd512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetsRcvd512to1023.setStatus("current")
_OctetsXmit512to1023_Type = Counter64
_OctetsXmit512to1023_Object = MibTableColumn
octetsXmit512to1023 = _OctetsXmit512to1023_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 28),
    _OctetsXmit512to1023_Type()
)
octetsXmit512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetsXmit512to1023.setStatus("current")
_OctetsRcvd1024to1518_Type = Counter64
_OctetsRcvd1024to1518_Object = MibTableColumn
octetsRcvd1024to1518 = _OctetsRcvd1024to1518_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 29),
    _OctetsRcvd1024to1518_Type()
)
octetsRcvd1024to1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetsRcvd1024to1518.setStatus("current")
_OctetsXmit1519toMax_Type = Counter64
_OctetsXmit1519toMax_Object = MibTableColumn
octetsXmit1519toMax = _OctetsXmit1519toMax_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 30),
    _OctetsXmit1519toMax_Type()
)
octetsXmit1519toMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetsXmit1519toMax.setStatus("current")
_UnderSizeFramesRcvd_Type = Counter64
_UnderSizeFramesRcvd_Object = MibTableColumn
underSizeFramesRcvd = _UnderSizeFramesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 31),
    _UnderSizeFramesRcvd_Type()
)
underSizeFramesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    underSizeFramesRcvd.setStatus("current")
_JabbersRcvd_Type = Counter64
_JabbersRcvd_Object = MibTableColumn
jabbersRcvd = _JabbersRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 2, 1, 1, 32),
    _JabbersRcvd_Type()
)
jabbersRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jabbersRcvd.setStatus("current")
_ServiceStats_ObjectIdentity = ObjectIdentity
serviceStats = _ServiceStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 3)
)
_ServiceStatsTable_Object = MibTable
serviceStatsTable = _ServiceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    serviceStatsTable.setStatus("current")
_ServiceStatsEntry_Object = MibTableRow
serviceStatsEntry = _ServiceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 3, 1, 1)
)
serviceStatsEntry.setIndexNames(
    (0, "Netrake-MIB", "serviceStatsPortIndex"),
    (0, "Netrake-MIB", "serviceStatsSlotId"),
)
if mibBuilder.loadTexts:
    serviceStatsEntry.setStatus("current")


class _ServiceStatsPortIndex_Type(Integer32):
    """Custom type serviceStatsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_ServiceStatsPortIndex_Type.__name__ = "Integer32"
_ServiceStatsPortIndex_Object = MibTableColumn
serviceStatsPortIndex = _ServiceStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 3, 1, 1, 1),
    _ServiceStatsPortIndex_Type()
)
serviceStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceStatsPortIndex.setStatus("current")
_ServiceStatsSlotId_Type = Integer32
_ServiceStatsSlotId_Object = MibTableColumn
serviceStatsSlotId = _ServiceStatsSlotId_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 3, 1, 1, 2),
    _ServiceStatsSlotId_Type()
)
serviceStatsSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceStatsSlotId.setStatus("current")
_RealTimeTotalPackets_Type = Counter64
_RealTimeTotalPackets_Object = MibTableColumn
realTimeTotalPackets = _RealTimeTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 3, 1, 1, 3),
    _RealTimeTotalPackets_Type()
)
realTimeTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realTimeTotalPackets.setStatus("current")
_RealTimeDiscardPackets_Type = Counter64
_RealTimeDiscardPackets_Object = MibTableColumn
realTimeDiscardPackets = _RealTimeDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 3, 1, 1, 4),
    _RealTimeDiscardPackets_Type()
)
realTimeDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realTimeDiscardPackets.setStatus("current")
_NrtTotalPackets_Type = Counter64
_NrtTotalPackets_Object = MibTableColumn
nrtTotalPackets = _NrtTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 3, 1, 1, 5),
    _NrtTotalPackets_Type()
)
nrtTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrtTotalPackets.setStatus("current")
_NrtDiscardPackets_Type = Counter64
_NrtDiscardPackets_Object = MibTableColumn
nrtDiscardPackets = _NrtDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 3, 1, 1, 6),
    _NrtDiscardPackets_Type()
)
nrtDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrtDiscardPackets.setStatus("current")
_BestEffortTotalPackets_Type = Counter64
_BestEffortTotalPackets_Object = MibTableColumn
bestEffortTotalPackets = _BestEffortTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 3, 1, 1, 7),
    _BestEffortTotalPackets_Type()
)
bestEffortTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bestEffortTotalPackets.setStatus("current")
_BestEffortDiscardPackets_Type = Counter64
_BestEffortDiscardPackets_Object = MibTableColumn
bestEffortDiscardPackets = _BestEffortDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 3, 1, 1, 8),
    _BestEffortDiscardPackets_Type()
)
bestEffortDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bestEffortDiscardPackets.setStatus("current")
_RedundancyStats_ObjectIdentity = ObjectIdentity
redundancyStats = _RedundancyStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 4)
)
_RedundPairedModeTimeTicks_Type = Counter64
_RedundPairedModeTimeTicks_Object = MibScalar
redundPairedModeTimeTicks = _RedundPairedModeTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 4, 1),
    _RedundPairedModeTimeTicks_Type()
)
redundPairedModeTimeTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundPairedModeTimeTicks.setStatus("current")
_RedundRecoveryModeTimeTicks_Type = Counter64
_RedundRecoveryModeTimeTicks_Object = MibScalar
redundRecoveryModeTimeTicks = _RedundRecoveryModeTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 4, 2),
    _RedundRecoveryModeTimeTicks_Type()
)
redundRecoveryModeTimeTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundRecoveryModeTimeTicks.setStatus("current")
_RedundNumRedundLinkFailures_Type = Counter64
_RedundNumRedundLinkFailures_Object = MibScalar
redundNumRedundLinkFailures = _RedundNumRedundLinkFailures_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 4, 3),
    _RedundNumRedundLinkFailures_Type()
)
redundNumRedundLinkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundNumRedundLinkFailures.setStatus("current")
_RedundActiveMateCalls_Type = Counter64
_RedundActiveMateCalls_Object = MibScalar
redundActiveMateCalls = _RedundActiveMateCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 4, 4),
    _RedundActiveMateCalls_Type()
)
redundActiveMateCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundActiveMateCalls.setStatus("current")
_RedundActiveMateRegist_Type = Counter64
_RedundActiveMateRegist_Object = MibScalar
redundActiveMateRegist = _RedundActiveMateRegist_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 4, 5),
    _RedundActiveMateRegist_Type()
)
redundActiveMateRegist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundActiveMateRegist.setStatus("current")
_PolicyStats_ObjectIdentity = ObjectIdentity
policyStats = _PolicyStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 5)
)
_PolicyCountersTable_Object = MibTable
policyCountersTable = _PolicyCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 5, 1)
)
if mibBuilder.loadTexts:
    policyCountersTable.setStatus("current")
_PolicyCountersEntry_Object = MibTableRow
policyCountersEntry = _PolicyCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 5, 1, 1)
)
policyCountersEntry.setIndexNames(
    (0, "Netrake-MIB", "policyIndex"),
)
if mibBuilder.loadTexts:
    policyCountersEntry.setStatus("current")
_PolicyIndex_Type = OctetString
_PolicyIndex_Object = MibTableColumn
policyIndex = _PolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 5, 1, 1, 1),
    _PolicyIndex_Type()
)
policyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyIndex.setStatus("current")
_PolicyTotalPacketsA_Type = Counter64
_PolicyTotalPacketsA_Object = MibTableColumn
policyTotalPacketsA = _PolicyTotalPacketsA_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 5, 1, 1, 2),
    _PolicyTotalPacketsA_Type()
)
policyTotalPacketsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyTotalPacketsA.setStatus("current")
_PolicyTotalPacketsB_Type = Counter64
_PolicyTotalPacketsB_Object = MibTableColumn
policyTotalPacketsB = _PolicyTotalPacketsB_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 5, 1, 1, 3),
    _PolicyTotalPacketsB_Type()
)
policyTotalPacketsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyTotalPacketsB.setStatus("current")
_PolicyTotalPackets_Type = Counter64
_PolicyTotalPackets_Object = MibTableColumn
policyTotalPackets = _PolicyTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 5, 1, 1, 4),
    _PolicyTotalPackets_Type()
)
policyTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyTotalPackets.setStatus("current")


class _PolicyStatsReset_Type(Integer32):
    """Custom type policyStatsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_PolicyStatsReset_Type.__name__ = "Integer32"
_PolicyStatsReset_Object = MibScalar
policyStatsReset = _PolicyStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 5, 2),
    _PolicyStatsReset_Type()
)
policyStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyStatsReset.setStatus("current")
_SipStats_ObjectIdentity = ObjectIdentity
sipStats = _SipStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6)
)
_SipStatCallsInitiating_Type = Counter64
_SipStatCallsInitiating_Object = MibScalar
sipStatCallsInitiating = _SipStatCallsInitiating_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 1),
    _SipStatCallsInitiating_Type()
)
sipStatCallsInitiating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatCallsInitiating.setStatus("current")
_SipStatNonLocalActiveCalls_Type = Counter64
_SipStatNonLocalActiveCalls_Object = MibScalar
sipStatNonLocalActiveCalls = _SipStatNonLocalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 2),
    _SipStatNonLocalActiveCalls_Type()
)
sipStatNonLocalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatNonLocalActiveCalls.setStatus("deprecated")
_SipStatLocalActiveCalls_Type = Counter64
_SipStatLocalActiveCalls_Object = MibScalar
sipStatLocalActiveCalls = _SipStatLocalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 3),
    _SipStatLocalActiveCalls_Type()
)
sipStatLocalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatLocalActiveCalls.setStatus("current")
_SipStatTermCalls_Type = Counter64
_SipStatTermCalls_Object = MibScalar
sipStatTermCalls = _SipStatTermCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 4),
    _SipStatTermCalls_Type()
)
sipStatTermCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatTermCalls.setStatus("current")
_SipStatPeakActiveCalls_Type = Counter64
_SipStatPeakActiveCalls_Object = MibScalar
sipStatPeakActiveCalls = _SipStatPeakActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 5),
    _SipStatPeakActiveCalls_Type()
)
sipStatPeakActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatPeakActiveCalls.setStatus("deprecated")
_SipStatTotalActiveCalls_Type = Counter64
_SipStatTotalActiveCalls_Object = MibScalar
sipStatTotalActiveCalls = _SipStatTotalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 6),
    _SipStatTotalActiveCalls_Type()
)
sipStatTotalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatTotalActiveCalls.setStatus("current")
_SipStatCallsCompletedSuccess_Type = Counter64
_SipStatCallsCompletedSuccess_Object = MibScalar
sipStatCallsCompletedSuccess = _SipStatCallsCompletedSuccess_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 7),
    _SipStatCallsCompletedSuccess_Type()
)
sipStatCallsCompletedSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatCallsCompletedSuccess.setStatus("current")
_SipStatCallsFailed_Type = Counter64
_SipStatCallsFailed_Object = MibScalar
sipStatCallsFailed = _SipStatCallsFailed_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 8),
    _SipStatCallsFailed_Type()
)
sipStatCallsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatCallsFailed.setStatus("current")
_SipStatCallsAbandoned_Type = Counter64
_SipStatCallsAbandoned_Object = MibScalar
sipStatCallsAbandoned = _SipStatCallsAbandoned_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 9),
    _SipStatCallsAbandoned_Type()
)
sipStatCallsAbandoned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatCallsAbandoned.setStatus("current")
_SipStatCallsDropped_Type = Counter64
_SipStatCallsDropped_Object = MibScalar
sipStatCallsDropped = _SipStatCallsDropped_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 10),
    _SipStatCallsDropped_Type()
)
sipStatCallsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatCallsDropped.setStatus("deprecated")
_SipStatCallsDegraded_Type = Counter64
_SipStatCallsDegraded_Object = MibScalar
sipStatCallsDegraded = _SipStatCallsDegraded_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 11),
    _SipStatCallsDegraded_Type()
)
sipStatCallsDegraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatCallsDegraded.setStatus("current")
_SipStatAuthFailures_Type = Counter64
_SipStatAuthFailures_Object = MibScalar
sipStatAuthFailures = _SipStatAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 12),
    _SipStatAuthFailures_Type()
)
sipStatAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatAuthFailures.setStatus("deprecated")
_SipStatCallMediaTimeouts_Type = Counter64
_SipStatCallMediaTimeouts_Object = MibScalar
sipStatCallMediaTimeouts = _SipStatCallMediaTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 13),
    _SipStatCallMediaTimeouts_Type()
)
sipStatCallMediaTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatCallMediaTimeouts.setStatus("current")
_SipStatCallInitTimeouts_Type = Counter64
_SipStatCallInitTimeouts_Object = MibScalar
sipStatCallInitTimeouts = _SipStatCallInitTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 14),
    _SipStatCallInitTimeouts_Type()
)
sipStatCallInitTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatCallInitTimeouts.setStatus("current")
_SipStatTermTimeouts_Type = Counter64
_SipStatTermTimeouts_Object = MibScalar
sipStatTermTimeouts = _SipStatTermTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 15),
    _SipStatTermTimeouts_Type()
)
sipStatTermTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatTermTimeouts.setStatus("current")
_SipStatMsgErrs_Type = Counter64
_SipStatMsgErrs_Object = MibScalar
sipStatMsgErrs = _SipStatMsgErrs_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 16),
    _SipStatMsgErrs_Type()
)
sipStatMsgErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatMsgErrs.setStatus("deprecated")
_SipStatCallsProcessed_Type = Counter64
_SipStatCallsProcessed_Object = MibScalar
sipStatCallsProcessed = _SipStatCallsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 17),
    _SipStatCallsProcessed_Type()
)
sipStatCallsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatCallsProcessed.setStatus("current")
_SipStatPeakNonLocalCalls_Type = Counter64
_SipStatPeakNonLocalCalls_Object = MibScalar
sipStatPeakNonLocalCalls = _SipStatPeakNonLocalCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 18),
    _SipStatPeakNonLocalCalls_Type()
)
sipStatPeakNonLocalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatPeakNonLocalCalls.setStatus("deprecated")
_SipStatPeakLocalCalls_Type = Counter64
_SipStatPeakLocalCalls_Object = MibScalar
sipStatPeakLocalCalls = _SipStatPeakLocalCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 19),
    _SipStatPeakLocalCalls_Type()
)
sipStatPeakLocalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatPeakLocalCalls.setStatus("current")
_SipStatRedirectSuccess_Type = Counter64
_SipStatRedirectSuccess_Object = MibScalar
sipStatRedirectSuccess = _SipStatRedirectSuccess_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 20),
    _SipStatRedirectSuccess_Type()
)
sipStatRedirectSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatRedirectSuccess.setStatus("deprecated")
_SipStatRedirectFailures_Type = Counter64
_SipStatRedirectFailures_Object = MibScalar
sipStatRedirectFailures = _SipStatRedirectFailures_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 21),
    _SipStatRedirectFailures_Type()
)
sipStatRedirectFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatRedirectFailures.setStatus("deprecated")
_SipStatMessageRoutingFailures_Type = Counter64
_SipStatMessageRoutingFailures_Object = MibScalar
sipStatMessageRoutingFailures = _SipStatMessageRoutingFailures_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 22),
    _SipStatMessageRoutingFailures_Type()
)
sipStatMessageRoutingFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatMessageRoutingFailures.setStatus("deprecated")
_SipStatAuthenticationChallenges_Type = Counter64
_SipStatAuthenticationChallenges_Object = MibScalar
sipStatAuthenticationChallenges = _SipStatAuthenticationChallenges_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 23),
    _SipStatAuthenticationChallenges_Type()
)
sipStatAuthenticationChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatAuthenticationChallenges.setStatus("current")
_SipStatRTPFWTraversalTimeouts_Type = Counter64
_SipStatRTPFWTraversalTimeouts_Object = MibScalar
sipStatRTPFWTraversalTimeouts = _SipStatRTPFWTraversalTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 24),
    _SipStatRTPFWTraversalTimeouts_Type()
)
sipStatRTPFWTraversalTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatRTPFWTraversalTimeouts.setStatus("current")
_SipStatMessagesReroutedToMate_Type = Counter64
_SipStatMessagesReroutedToMate_Object = MibScalar
sipStatMessagesReroutedToMate = _SipStatMessagesReroutedToMate_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 25),
    _SipStatMessagesReroutedToMate_Type()
)
sipStatMessagesReroutedToMate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatMessagesReroutedToMate.setStatus("deprecated")
_SipStatSameSideActiveCalls_Type = Counter64
_SipStatSameSideActiveCalls_Object = MibScalar
sipStatSameSideActiveCalls = _SipStatSameSideActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 26),
    _SipStatSameSideActiveCalls_Type()
)
sipStatSameSideActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatSameSideActiveCalls.setStatus("current")
_SipStatNormalActiveCalls_Type = Counter64
_SipStatNormalActiveCalls_Object = MibScalar
sipStatNormalActiveCalls = _SipStatNormalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 27),
    _SipStatNormalActiveCalls_Type()
)
sipStatNormalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatNormalActiveCalls.setStatus("current")
_SipStatPeakSameSideActiveCalls_Type = Counter64
_SipStatPeakSameSideActiveCalls_Object = MibScalar
sipStatPeakSameSideActiveCalls = _SipStatPeakSameSideActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 28),
    _SipStatPeakSameSideActiveCalls_Type()
)
sipStatPeakSameSideActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatPeakSameSideActiveCalls.setStatus("current")
_SipStatPeakNormalActiveCalls_Type = Counter64
_SipStatPeakNormalActiveCalls_Object = MibScalar
sipStatPeakNormalActiveCalls = _SipStatPeakNormalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 29),
    _SipStatPeakNormalActiveCalls_Type()
)
sipStatPeakNormalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatPeakNormalActiveCalls.setStatus("current")
_SipStatCurrentFaxSessions_Type = Counter64
_SipStatCurrentFaxSessions_Object = MibScalar
sipStatCurrentFaxSessions = _SipStatCurrentFaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 30),
    _SipStatCurrentFaxSessions_Type()
)
sipStatCurrentFaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatCurrentFaxSessions.setStatus("deprecated")
_SipStatPeakFaxSessions_Type = Counter64
_SipStatPeakFaxSessions_Object = MibScalar
sipStatPeakFaxSessions = _SipStatPeakFaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 31),
    _SipStatPeakFaxSessions_Type()
)
sipStatPeakFaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatPeakFaxSessions.setStatus("deprecated")
_SipStatTotalFaxSessions_Type = Counter64
_SipStatTotalFaxSessions_Object = MibScalar
sipStatTotalFaxSessions = _SipStatTotalFaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 32),
    _SipStatTotalFaxSessions_Type()
)
sipStatTotalFaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatTotalFaxSessions.setStatus("deprecated")
_SipStatPeakTotalActiveCalls_Type = Counter64
_SipStatPeakTotalActiveCalls_Object = MibScalar
sipStatPeakTotalActiveCalls = _SipStatPeakTotalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 6, 33),
    _SipStatPeakTotalActiveCalls_Type()
)
sipStatPeakTotalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatPeakTotalActiveCalls.setStatus("current")
_VlanStats_ObjectIdentity = ObjectIdentity
vlanStats = _VlanStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 7)
)
_VlanStatsTable_Object = MibTable
vlanStatsTable = _VlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 7, 2)
)
if mibBuilder.loadTexts:
    vlanStatsTable.setStatus("current")
_VlanStatsEntry_Object = MibTableRow
vlanStatsEntry = _VlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 7, 2, 1)
)
vlanStatsEntry.setIndexNames(
    (0, "Netrake-MIB", "vlanStatsSlotNum"),
    (0, "Netrake-MIB", "vlanStatsPortNum"),
    (0, "Netrake-MIB", "vlanStatsVlanLabel"),
)
if mibBuilder.loadTexts:
    vlanStatsEntry.setStatus("current")


class _VlanStatsSlotNum_Type(Integer32):
    """Custom type vlanStatsSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_VlanStatsSlotNum_Type.__name__ = "Integer32"
_VlanStatsSlotNum_Object = MibTableColumn
vlanStatsSlotNum = _VlanStatsSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 7, 2, 1, 1),
    _VlanStatsSlotNum_Type()
)
vlanStatsSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanStatsSlotNum.setStatus("current")


class _VlanStatsPortNum_Type(Integer32):
    """Custom type vlanStatsPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_VlanStatsPortNum_Type.__name__ = "Integer32"
_VlanStatsPortNum_Object = MibTableColumn
vlanStatsPortNum = _VlanStatsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 7, 2, 1, 2),
    _VlanStatsPortNum_Type()
)
vlanStatsPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanStatsPortNum.setStatus("current")
_VlanStatsVlanLabel_Type = Integer32
_VlanStatsVlanLabel_Object = MibTableColumn
vlanStatsVlanLabel = _VlanStatsVlanLabel_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 7, 2, 1, 3),
    _VlanStatsVlanLabel_Type()
)
vlanStatsVlanLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanStatsVlanLabel.setStatus("current")
_VlanTotalPacketsXmit_Type = Counter64
_VlanTotalPacketsXmit_Object = MibTableColumn
vlanTotalPacketsXmit = _VlanTotalPacketsXmit_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 7, 2, 1, 4),
    _VlanTotalPacketsXmit_Type()
)
vlanTotalPacketsXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTotalPacketsXmit.setStatus("current")
_VlanTotalPacketsRcvd_Type = Counter64
_VlanTotalPacketsRcvd_Object = MibTableColumn
vlanTotalPacketsRcvd = _VlanTotalPacketsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 7, 2, 1, 5),
    _VlanTotalPacketsRcvd_Type()
)
vlanTotalPacketsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTotalPacketsRcvd.setStatus("current")


class _VlanStatsReset_Type(Integer32):
    """Custom type vlanStatsReset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_VlanStatsReset_Type.__name__ = "Integer32"
_VlanStatsReset_Object = MibScalar
vlanStatsReset = _VlanStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 7, 3),
    _VlanStatsReset_Type()
)
vlanStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStatsReset.setStatus("current")
_CustSipStats_ObjectIdentity = ObjectIdentity
custSipStats = _CustSipStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 8)
)
_CustSipStatsTable_Object = MibTable
custSipStatsTable = _CustSipStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 8, 1)
)
if mibBuilder.loadTexts:
    custSipStatsTable.setStatus("current")
_CustSipStatsEntry_Object = MibTableRow
custSipStatsEntry = _CustSipStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 8, 1, 1)
)
custSipStatsEntry.setIndexNames(
    (0, "Netrake-MIB", "custSipStatId"),
)
if mibBuilder.loadTexts:
    custSipStatsEntry.setStatus("current")
_CustSipStatId_Type = Integer32
_CustSipStatId_Object = MibTableColumn
custSipStatId = _CustSipStatId_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 8, 1, 1, 1),
    _CustSipStatId_Type()
)
custSipStatId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipStatId.setStatus("current")
_CustSipStatCallsInitiating_Type = Counter64
_CustSipStatCallsInitiating_Object = MibTableColumn
custSipStatCallsInitiating = _CustSipStatCallsInitiating_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 8, 1, 1, 2),
    _CustSipStatCallsInitiating_Type()
)
custSipStatCallsInitiating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipStatCallsInitiating.setStatus("current")
_CustSipStatNonLocalActiveCalls_Type = Counter64
_CustSipStatNonLocalActiveCalls_Object = MibTableColumn
custSipStatNonLocalActiveCalls = _CustSipStatNonLocalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 8, 1, 1, 3),
    _CustSipStatNonLocalActiveCalls_Type()
)
custSipStatNonLocalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipStatNonLocalActiveCalls.setStatus("deprecated")
_CustSipStatLocalActiveCalls_Type = Counter64
_CustSipStatLocalActiveCalls_Object = MibTableColumn
custSipStatLocalActiveCalls = _CustSipStatLocalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 8, 1, 1, 4),
    _CustSipStatLocalActiveCalls_Type()
)
custSipStatLocalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipStatLocalActiveCalls.setStatus("current")
_CustSipStatTermCalls_Type = Counter64
_CustSipStatTermCalls_Object = MibTableColumn
custSipStatTermCalls = _CustSipStatTermCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 8, 1, 1, 5),
    _CustSipStatTermCalls_Type()
)
custSipStatTermCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipStatTermCalls.setStatus("current")
_CustSipStatPeakActiveCalls_Type = Counter64
_CustSipStatPeakActiveCalls_Object = MibTableColumn
custSipStatPeakActiveCalls = _CustSipStatPeakActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 8, 1, 1, 6),
    _CustSipStatPeakActiveCalls_Type()
)
custSipStatPeakActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipStatPeakActiveCalls.setStatus("deprecated")
_CustSipStatTotalActiveCalls_Type = Counter64
_CustSipStatTotalActiveCalls_Object = MibTableColumn
custSipStatTotalActiveCalls = _CustSipStatTotalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 8, 1, 1, 7),
    _CustSipStatTotalActiveCalls_Type()
)
custSipStatTotalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipStatTotalActiveCalls.setStatus("current")
_CustSipStatCallsCompletedSuccess_Type = Counter64
_CustSipStatCallsCompletedSuccess_Object = MibTableColumn
custSipStatCallsCompletedSuccess = _CustSipStatCallsCompletedSuccess_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 8, 1, 1, 8),
    _CustSipStatCallsCompletedSuccess_Type()
)
custSipStatCallsCompletedSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipStatCallsCompletedSuccess.setStatus("current")
_CustSipStatCallsFailed_Type = Counter64
_CustSipStatCallsFailed_Object = MibTableColumn
custSipStatCallsFailed = _CustSipStatCallsFailed_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 8, 1, 1, 9),
    _CustSipStatCallsFailed_Type()
)
custSipStatCallsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipStatCallsFailed.setStatus("current")
_CustSipStatCallsAbandoned_Type = Counter64
_CustSipStatCallsAbandoned_Object = MibTableColumn
custSipStatCallsAbandoned = _CustSipStatCallsAbandoned_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 8, 1, 1, 10),
    _CustSipStatCallsAbandoned_Type()
)
custSipStatCallsAbandoned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipStatCallsAbandoned.setStatus("current")
_CustSipStatCallsDropped_Type = Counter64
_CustSipStatCallsDropped_Object = MibTableColumn
custSipStatCallsDropped = _CustSipStatCallsDropped_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 8, 1, 1, 11),
    _CustSipStatCallsDropped_Type()
)
custSipStatCallsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipStatCallsDropped.setStatus("deprecated")
_CustSipStatCallsDegraded_Type = Counter64
_CustSipStatCallsDegraded_Object = MibTableColumn
custSipStatCallsDegraded = _CustSipStatCallsDegraded_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 8, 1, 1, 12),
    _CustSipStatCallsDegraded_Type()
)
custSipStatCallsDegraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipStatCallsDegraded.setStatus("current")
_CustSipStatCallMediaTimeouts_Type = Counter64
_CustSipStatCallMediaTimeouts_Object = MibTableColumn
custSipStatCallMediaTimeouts = _CustSipStatCallMediaTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 8, 1, 1, 13),
    _CustSipStatCallMediaTimeouts_Type()
)
custSipStatCallMediaTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipStatCallMediaTimeouts.setStatus("current")
_CustSipStatCallInitTimeouts_Type = Counter64
_CustSipStatCallInitTimeouts_Object = MibTableColumn
custSipStatCallInitTimeouts = _CustSipStatCallInitTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 8, 1, 1, 14),
    _CustSipStatCallInitTimeouts_Type()
)
custSipStatCallInitTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipStatCallInitTimeouts.setStatus("current")
_CustSipStatTermTimeouts_Type = Counter64
_CustSipStatTermTimeouts_Object = MibTableColumn
custSipStatTermTimeouts = _CustSipStatTermTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 8, 1, 1, 15),
    _CustSipStatTermTimeouts_Type()
)
custSipStatTermTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipStatTermTimeouts.setStatus("current")
_CustSipStatCallsProcessed_Type = Counter64
_CustSipStatCallsProcessed_Object = MibTableColumn
custSipStatCallsProcessed = _CustSipStatCallsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 8, 1, 1, 16),
    _CustSipStatCallsProcessed_Type()
)
custSipStatCallsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipStatCallsProcessed.setStatus("current")
_CustSipPeakNonLocalCalls_Type = Counter64
_CustSipPeakNonLocalCalls_Object = MibTableColumn
custSipPeakNonLocalCalls = _CustSipPeakNonLocalCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 8, 1, 1, 17),
    _CustSipPeakNonLocalCalls_Type()
)
custSipPeakNonLocalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipPeakNonLocalCalls.setStatus("deprecated")
_CustSipPeakLocalCalls_Type = Counter64
_CustSipPeakLocalCalls_Object = MibTableColumn
custSipPeakLocalCalls = _CustSipPeakLocalCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 8, 1, 1, 18),
    _CustSipPeakLocalCalls_Type()
)
custSipPeakLocalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipPeakLocalCalls.setStatus("current")
_CustSipAuthenticationChallenges_Type = Counter64
_CustSipAuthenticationChallenges_Object = MibTableColumn
custSipAuthenticationChallenges = _CustSipAuthenticationChallenges_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 8, 1, 1, 19),
    _CustSipAuthenticationChallenges_Type()
)
custSipAuthenticationChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipAuthenticationChallenges.setStatus("current")
_CustSipRTPFWTraversalTimeouts_Type = Counter64
_CustSipRTPFWTraversalTimeouts_Object = MibTableColumn
custSipRTPFWTraversalTimeouts = _CustSipRTPFWTraversalTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 8, 1, 1, 20),
    _CustSipRTPFWTraversalTimeouts_Type()
)
custSipRTPFWTraversalTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipRTPFWTraversalTimeouts.setStatus("current")
_CustSipSameSideActiveCalls_Type = Counter64
_CustSipSameSideActiveCalls_Object = MibTableColumn
custSipSameSideActiveCalls = _CustSipSameSideActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 8, 1, 1, 21),
    _CustSipSameSideActiveCalls_Type()
)
custSipSameSideActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipSameSideActiveCalls.setStatus("current")
_CustSipNormalActiveCalls_Type = Counter64
_CustSipNormalActiveCalls_Object = MibTableColumn
custSipNormalActiveCalls = _CustSipNormalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 8, 1, 1, 22),
    _CustSipNormalActiveCalls_Type()
)
custSipNormalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipNormalActiveCalls.setStatus("current")
_CustSipPeakNormalActiveCalls_Type = Counter64
_CustSipPeakNormalActiveCalls_Object = MibTableColumn
custSipPeakNormalActiveCalls = _CustSipPeakNormalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 8, 1, 1, 23),
    _CustSipPeakNormalActiveCalls_Type()
)
custSipPeakNormalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipPeakNormalActiveCalls.setStatus("current")
_CustSipPeakTotalActive_Type = Counter64
_CustSipPeakTotalActive_Object = MibTableColumn
custSipPeakTotalActive = _CustSipPeakTotalActive_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 8, 1, 1, 24),
    _CustSipPeakTotalActive_Type()
)
custSipPeakTotalActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipPeakTotalActive.setStatus("current")


class _NCiteStatsConfigReset_Type(Integer32):
    """Custom type nCiteStatsConfigReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_NCiteStatsConfigReset_Type.__name__ = "Integer32"
_NCiteStatsConfigReset_Object = MibScalar
nCiteStatsConfigReset = _NCiteStatsConfigReset_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 9),
    _NCiteStatsConfigReset_Type()
)
nCiteStatsConfigReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nCiteStatsConfigReset.setStatus("current")
_NCiteSessionDetailRecord_ObjectIdentity = ObjectIdentity
nCiteSessionDetailRecord = _NCiteSessionDetailRecord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 10)
)


class _NCiteSDRCollectionCycle_Type(Integer32):
    """Custom type nCiteSDRCollectionCycle based on Integer32"""
    defaultValue = 5


_NCiteSDRCollectionCycle_Object = MibScalar
nCiteSDRCollectionCycle = _NCiteSDRCollectionCycle_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 10, 1),
    _NCiteSDRCollectionCycle_Type()
)
nCiteSDRCollectionCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nCiteSDRCollectionCycle.setStatus("current")
_NCIteSDRLastSent_Type = DateAndTime
_NCIteSDRLastSent_Object = MibScalar
nCIteSDRLastSent = _NCIteSDRLastSent_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 10, 2),
    _NCIteSDRLastSent_Type()
)
nCIteSDRLastSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nCIteSDRLastSent.setStatus("current")


class _NCiteSDREnable_Type(Integer32):
    """Custom type nCiteSDREnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NCiteSDREnable_Type.__name__ = "Integer32"
_NCiteSDREnable_Object = MibScalar
nCiteSDREnable = _NCiteSDREnable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 10, 3),
    _NCiteSDREnable_Type()
)
nCiteSDREnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nCiteSDREnable.setStatus("current")


class _NCiteSDRSentTrapAck_Type(Integer32):
    """Custom type nCiteSDRSentTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("notAck", 0))
    )


_NCiteSDRSentTrapAck_Type.__name__ = "Integer32"
_NCiteSDRSentTrapAck_Object = MibScalar
nCiteSDRSentTrapAck = _NCiteSDRSentTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 10, 5),
    _NCiteSDRSentTrapAck_Type()
)
nCiteSDRSentTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nCiteSDRSentTrapAck.setStatus("current")
_NCiteSDRSentTrapAckSource_Type = IpAddress
_NCiteSDRSentTrapAckSource_Object = MibScalar
nCiteSDRSentTrapAckSource = _NCiteSDRSentTrapAckSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 10, 6),
    _NCiteSDRSentTrapAckSource_Type()
)
nCiteSDRSentTrapAckSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nCiteSDRSentTrapAckSource.setStatus("current")
_RegistrationStats_ObjectIdentity = ObjectIdentity
registrationStats = _RegistrationStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 11)
)
_RegStatNumInitiating_Type = Counter64
_RegStatNumInitiating_Object = MibScalar
regStatNumInitiating = _RegStatNumInitiating_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 11, 1),
    _RegStatNumInitiating_Type()
)
regStatNumInitiating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatNumInitiating.setStatus("current")
_RegStatNumActive_Type = Counter64
_RegStatNumActive_Object = MibScalar
regStatNumActive = _RegStatNumActive_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 11, 2),
    _RegStatNumActive_Type()
)
regStatNumActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatNumActive.setStatus("current")
_RegStatPeak_Type = Counter64
_RegStatPeak_Object = MibScalar
regStatPeak = _RegStatPeak_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 11, 3),
    _RegStatPeak_Type()
)
regStatPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatPeak.setStatus("current")
_RegStatUpdateSuccess_Type = Counter64
_RegStatUpdateSuccess_Object = MibScalar
regStatUpdateSuccess = _RegStatUpdateSuccess_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 11, 4),
    _RegStatUpdateSuccess_Type()
)
regStatUpdateSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatUpdateSuccess.setStatus("current")
_RegStatUpdateFailed_Type = Counter64
_RegStatUpdateFailed_Object = MibScalar
regStatUpdateFailed = _RegStatUpdateFailed_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 11, 5),
    _RegStatUpdateFailed_Type()
)
regStatUpdateFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatUpdateFailed.setStatus("current")
_RegStatExpired_Type = Counter64
_RegStatExpired_Object = MibScalar
regStatExpired = _RegStatExpired_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 11, 6),
    _RegStatExpired_Type()
)
regStatExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatExpired.setStatus("current")
_RegStatDropped_Type = Counter64
_RegStatDropped_Object = MibScalar
regStatDropped = _RegStatDropped_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 11, 7),
    _RegStatDropped_Type()
)
regStatDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatDropped.setStatus("deprecated")
_RegStatAuthFailures_Type = Counter64
_RegStatAuthFailures_Object = MibScalar
regStatAuthFailures = _RegStatAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 11, 8),
    _RegStatAuthFailures_Type()
)
regStatAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatAuthFailures.setStatus("current")
_RegStatInitSipTimeouts_Type = Counter64
_RegStatInitSipTimeouts_Object = MibScalar
regStatInitSipTimeouts = _RegStatInitSipTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 11, 9),
    _RegStatInitSipTimeouts_Type()
)
regStatInitSipTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatInitSipTimeouts.setStatus("current")
_RegStatTermSipTimeouts_Type = Counter64
_RegStatTermSipTimeouts_Object = MibScalar
regStatTermSipTimeouts = _RegStatTermSipTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 11, 10),
    _RegStatTermSipTimeouts_Type()
)
regStatTermSipTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatTermSipTimeouts.setStatus("current")
_RegStatTerminating_Type = Counter64
_RegStatTerminating_Object = MibScalar
regStatTerminating = _RegStatTerminating_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 11, 11),
    _RegStatTerminating_Type()
)
regStatTerminating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatTerminating.setStatus("current")
_RegStatFailed_Type = Counter64
_RegStatFailed_Object = MibScalar
regStatFailed = _RegStatFailed_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 11, 12),
    _RegStatFailed_Type()
)
regStatFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatFailed.setStatus("current")
_RegStatAuthenticationChallenges_Type = Counter64
_RegStatAuthenticationChallenges_Object = MibScalar
regStatAuthenticationChallenges = _RegStatAuthenticationChallenges_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 11, 13),
    _RegStatAuthenticationChallenges_Type()
)
regStatAuthenticationChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatAuthenticationChallenges.setStatus("current")
_RegStatUnauthReg_Type = Counter64
_RegStatUnauthReg_Object = MibScalar
regStatUnauthReg = _RegStatUnauthReg_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 11, 14),
    _RegStatUnauthReg_Type()
)
regStatUnauthReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regStatUnauthReg.setStatus("current")
_CustRegStats_ObjectIdentity = ObjectIdentity
custRegStats = _CustRegStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 12)
)
_CustRegStatsTable_Object = MibTable
custRegStatsTable = _CustRegStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 12, 1)
)
if mibBuilder.loadTexts:
    custRegStatsTable.setStatus("current")
_CustRegStatsEntry_Object = MibTableRow
custRegStatsEntry = _CustRegStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 12, 1, 1)
)
custRegStatsEntry.setIndexNames(
    (0, "Netrake-MIB", "custRegStatId"),
)
if mibBuilder.loadTexts:
    custRegStatsEntry.setStatus("current")
_CustRegStatId_Type = Integer32
_CustRegStatId_Object = MibTableColumn
custRegStatId = _CustRegStatId_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 12, 1, 1, 1),
    _CustRegStatId_Type()
)
custRegStatId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custRegStatId.setStatus("current")
_CustRegStatNumInitiated_Type = Counter64
_CustRegStatNumInitiated_Object = MibTableColumn
custRegStatNumInitiated = _CustRegStatNumInitiated_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 12, 1, 1, 2),
    _CustRegStatNumInitiated_Type()
)
custRegStatNumInitiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custRegStatNumInitiated.setStatus("current")
_CustRegStatNumActive_Type = Counter64
_CustRegStatNumActive_Object = MibTableColumn
custRegStatNumActive = _CustRegStatNumActive_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 12, 1, 1, 3),
    _CustRegStatNumActive_Type()
)
custRegStatNumActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custRegStatNumActive.setStatus("current")
_CustRegStatPeak_Type = Counter64
_CustRegStatPeak_Object = MibTableColumn
custRegStatPeak = _CustRegStatPeak_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 12, 1, 1, 4),
    _CustRegStatPeak_Type()
)
custRegStatPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custRegStatPeak.setStatus("current")
_CustRegStatUpdateSuccess_Type = Counter64
_CustRegStatUpdateSuccess_Object = MibTableColumn
custRegStatUpdateSuccess = _CustRegStatUpdateSuccess_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 12, 1, 1, 5),
    _CustRegStatUpdateSuccess_Type()
)
custRegStatUpdateSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custRegStatUpdateSuccess.setStatus("current")
_CustRegStatUpdateFailed_Type = Counter64
_CustRegStatUpdateFailed_Object = MibTableColumn
custRegStatUpdateFailed = _CustRegStatUpdateFailed_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 12, 1, 1, 6),
    _CustRegStatUpdateFailed_Type()
)
custRegStatUpdateFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custRegStatUpdateFailed.setStatus("current")
_CustRegStatExpired_Type = Counter64
_CustRegStatExpired_Object = MibTableColumn
custRegStatExpired = _CustRegStatExpired_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 12, 1, 1, 7),
    _CustRegStatExpired_Type()
)
custRegStatExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custRegStatExpired.setStatus("current")
_CustRegStatDropped_Type = Counter64
_CustRegStatDropped_Object = MibTableColumn
custRegStatDropped = _CustRegStatDropped_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 12, 1, 1, 8),
    _CustRegStatDropped_Type()
)
custRegStatDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custRegStatDropped.setStatus("deprecated")
_CustRegStatInitSipTimeouts_Type = Counter64
_CustRegStatInitSipTimeouts_Object = MibTableColumn
custRegStatInitSipTimeouts = _CustRegStatInitSipTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 12, 1, 1, 9),
    _CustRegStatInitSipTimeouts_Type()
)
custRegStatInitSipTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custRegStatInitSipTimeouts.setStatus("current")
_CustRegStatTermSipTimeouts_Type = Counter64
_CustRegStatTermSipTimeouts_Object = MibTableColumn
custRegStatTermSipTimeouts = _CustRegStatTermSipTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 12, 1, 1, 10),
    _CustRegStatTermSipTimeouts_Type()
)
custRegStatTermSipTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custRegStatTermSipTimeouts.setStatus("current")
_CustRegStatTerminating_Type = Counter64
_CustRegStatTerminating_Object = MibTableColumn
custRegStatTerminating = _CustRegStatTerminating_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 12, 1, 1, 11),
    _CustRegStatTerminating_Type()
)
custRegStatTerminating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custRegStatTerminating.setStatus("current")
_CustRegStatFailed_Type = Counter64
_CustRegStatFailed_Object = MibTableColumn
custRegStatFailed = _CustRegStatFailed_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 12, 1, 1, 12),
    _CustRegStatFailed_Type()
)
custRegStatFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custRegStatFailed.setStatus("current")
_CustRegAuthenticationChallenges_Type = Counter64
_CustRegAuthenticationChallenges_Object = MibTableColumn
custRegAuthenticationChallenges = _CustRegAuthenticationChallenges_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 12, 1, 1, 13),
    _CustRegAuthenticationChallenges_Type()
)
custRegAuthenticationChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custRegAuthenticationChallenges.setStatus("current")
_CustRegStatUnauthorizedReg_Type = Counter64
_CustRegStatUnauthorizedReg_Object = MibTableColumn
custRegStatUnauthorizedReg = _CustRegStatUnauthorizedReg_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 12, 1, 1, 14),
    _CustRegStatUnauthorizedReg_Type()
)
custRegStatUnauthorizedReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custRegStatUnauthorizedReg.setStatus("current")
_NtsStats_ObjectIdentity = ObjectIdentity
ntsStats = _NtsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 13)
)
_NtsStatNumCust_Type = Counter64
_NtsStatNumCust_Object = MibScalar
ntsStatNumCust = _NtsStatNumCust_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 13, 1),
    _NtsStatNumCust_Type()
)
ntsStatNumCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntsStatNumCust.setStatus("current")
_NtsStatAuthFailures_Type = Counter64
_NtsStatAuthFailures_Object = MibScalar
ntsStatAuthFailures = _NtsStatAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 13, 2),
    _NtsStatAuthFailures_Type()
)
ntsStatAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntsStatAuthFailures.setStatus("current")
_NtsStatCustConnected_Type = Counter64
_NtsStatCustConnected_Object = MibScalar
ntsStatCustConnected = _NtsStatCustConnected_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 13, 3),
    _NtsStatCustConnected_Type()
)
ntsStatCustConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntsStatCustConnected.setStatus("current")
_RogueStats_ObjectIdentity = ObjectIdentity
rogueStats = _RogueStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 14)
)
_EdrCurrentCallCount_Type = Counter64
_EdrCurrentCallCount_Object = MibScalar
edrCurrentCallCount = _EdrCurrentCallCount_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 14, 1),
    _EdrCurrentCallCount_Type()
)
edrCurrentCallCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edrCurrentCallCount.setStatus("current")
_EdrPeakCallCount_Type = Counter64
_EdrPeakCallCount_Object = MibScalar
edrPeakCallCount = _EdrPeakCallCount_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 14, 2),
    _EdrPeakCallCount_Type()
)
edrPeakCallCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edrPeakCallCount.setStatus("current")
_EdrTotalCallsRogue_Type = Counter64
_EdrTotalCallsRogue_Object = MibScalar
edrTotalCallsRogue = _EdrTotalCallsRogue_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 14, 3),
    _EdrTotalCallsRogue_Type()
)
edrTotalCallsRogue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edrTotalCallsRogue.setStatus("current")
_EdrLastDetection_Type = DateAndTime
_EdrLastDetection_Object = MibScalar
edrLastDetection = _EdrLastDetection_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 14, 4),
    _EdrLastDetection_Type()
)
edrLastDetection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edrLastDetection.setStatus("current")
_LrdCurrentCallCount_Type = Counter64
_LrdCurrentCallCount_Object = MibScalar
lrdCurrentCallCount = _LrdCurrentCallCount_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 14, 5),
    _LrdCurrentCallCount_Type()
)
lrdCurrentCallCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrdCurrentCallCount.setStatus("current")
_LrdPeakCallCount_Type = Counter64
_LrdPeakCallCount_Object = MibScalar
lrdPeakCallCount = _LrdPeakCallCount_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 14, 6),
    _LrdPeakCallCount_Type()
)
lrdPeakCallCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrdPeakCallCount.setStatus("current")
_LrdTotalCallsRogue_Type = Counter64
_LrdTotalCallsRogue_Object = MibScalar
lrdTotalCallsRogue = _LrdTotalCallsRogue_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 14, 7),
    _LrdTotalCallsRogue_Type()
)
lrdTotalCallsRogue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrdTotalCallsRogue.setStatus("current")
_LrdLastDetection_Type = DateAndTime
_LrdLastDetection_Object = MibScalar
lrdLastDetection = _LrdLastDetection_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 14, 8),
    _LrdLastDetection_Type()
)
lrdLastDetection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrdLastDetection.setStatus("current")


class _NCiteStatsReset_Type(Integer32):
    """Custom type nCiteStatsReset based on Integer32"""
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
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("h323RegStats", 8),
          ("h323Stats", 7),
          ("mediaStats", 9),
          ("ntsStats", 4),
          ("registrationStats", 2),
          ("rogueStats", 3),
          ("sipCommonStats", 10),
          ("sipEvtDlgStats", 11),
          ("sipH323Stats", 6),
          ("sipStats", 1),
          ("voIpStats", 5))
    )


_NCiteStatsReset_Type.__name__ = "Integer32"
_NCiteStatsReset_Object = MibScalar
nCiteStatsReset = _NCiteStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 15),
    _NCiteStatsReset_Type()
)
nCiteStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nCiteStatsReset.setStatus("current")
_CustNtsStats_ObjectIdentity = ObjectIdentity
custNtsStats = _CustNtsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 16)
)
_CustNtsStatsTable_Object = MibTable
custNtsStatsTable = _CustNtsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 16, 1)
)
if mibBuilder.loadTexts:
    custNtsStatsTable.setStatus("current")
_CustNtsStatsEntry_Object = MibTableRow
custNtsStatsEntry = _CustNtsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 16, 1, 1)
)
custNtsStatsEntry.setIndexNames(
    (0, "Netrake-MIB", "custNtsStatId"),
)
if mibBuilder.loadTexts:
    custNtsStatsEntry.setStatus("current")
_CustNtsStatId_Type = Integer32
_CustNtsStatId_Object = MibTableColumn
custNtsStatId = _CustNtsStatId_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 16, 1, 1, 1),
    _CustNtsStatId_Type()
)
custNtsStatId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custNtsStatId.setStatus("current")
_CustNtsAuthorizationFailed_Type = Counter64
_CustNtsAuthorizationFailed_Object = MibTableColumn
custNtsAuthorizationFailed = _CustNtsAuthorizationFailed_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 16, 1, 1, 2),
    _CustNtsAuthorizationFailed_Type()
)
custNtsAuthorizationFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custNtsAuthorizationFailed.setStatus("current")
_SipH323Stats_ObjectIdentity = ObjectIdentity
sipH323Stats = _SipH323Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17)
)
_SipH323CallsInitiating_Type = Counter64
_SipH323CallsInitiating_Object = MibScalar
sipH323CallsInitiating = _SipH323CallsInitiating_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17, 1),
    _SipH323CallsInitiating_Type()
)
sipH323CallsInitiating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipH323CallsInitiating.setStatus("current")
_SipH323LocalActiveCalls_Type = Counter64
_SipH323LocalActiveCalls_Object = MibScalar
sipH323LocalActiveCalls = _SipH323LocalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17, 2),
    _SipH323LocalActiveCalls_Type()
)
sipH323LocalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipH323LocalActiveCalls.setStatus("current")
_SipH323TermCalls_Type = Counter64
_SipH323TermCalls_Object = MibScalar
sipH323TermCalls = _SipH323TermCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17, 3),
    _SipH323TermCalls_Type()
)
sipH323TermCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipH323TermCalls.setStatus("current")
_SipH323PeakTotalActiveCalls_Type = Counter64
_SipH323PeakTotalActiveCalls_Object = MibScalar
sipH323PeakTotalActiveCalls = _SipH323PeakTotalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17, 4),
    _SipH323PeakTotalActiveCalls_Type()
)
sipH323PeakTotalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipH323PeakTotalActiveCalls.setStatus("current")
_SipH323TotalActiveCalls_Type = Counter64
_SipH323TotalActiveCalls_Object = MibScalar
sipH323TotalActiveCalls = _SipH323TotalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17, 5),
    _SipH323TotalActiveCalls_Type()
)
sipH323TotalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipH323TotalActiveCalls.setStatus("current")
_SipH323CallsCompletedSuccess_Type = Counter64
_SipH323CallsCompletedSuccess_Object = MibScalar
sipH323CallsCompletedSuccess = _SipH323CallsCompletedSuccess_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17, 6),
    _SipH323CallsCompletedSuccess_Type()
)
sipH323CallsCompletedSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipH323CallsCompletedSuccess.setStatus("current")
_SipH323CallsFailed_Type = Counter64
_SipH323CallsFailed_Object = MibScalar
sipH323CallsFailed = _SipH323CallsFailed_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17, 7),
    _SipH323CallsFailed_Type()
)
sipH323CallsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipH323CallsFailed.setStatus("current")
_SipH323CallsAbandoned_Type = Counter64
_SipH323CallsAbandoned_Object = MibScalar
sipH323CallsAbandoned = _SipH323CallsAbandoned_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17, 8),
    _SipH323CallsAbandoned_Type()
)
sipH323CallsAbandoned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipH323CallsAbandoned.setStatus("current")
_SipH323CallsDropped_Type = Counter64
_SipH323CallsDropped_Object = MibScalar
sipH323CallsDropped = _SipH323CallsDropped_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17, 9),
    _SipH323CallsDropped_Type()
)
sipH323CallsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipH323CallsDropped.setStatus("deprecated")
_SipH323CallsDegraded_Type = Counter64
_SipH323CallsDegraded_Object = MibScalar
sipH323CallsDegraded = _SipH323CallsDegraded_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17, 10),
    _SipH323CallsDegraded_Type()
)
sipH323CallsDegraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipH323CallsDegraded.setStatus("current")
_SipH323AuthFailures_Type = Counter64
_SipH323AuthFailures_Object = MibScalar
sipH323AuthFailures = _SipH323AuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17, 11),
    _SipH323AuthFailures_Type()
)
sipH323AuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipH323AuthFailures.setStatus("current")
_SipH323CallMediaTimeouts_Type = Counter64
_SipH323CallMediaTimeouts_Object = MibScalar
sipH323CallMediaTimeouts = _SipH323CallMediaTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17, 12),
    _SipH323CallMediaTimeouts_Type()
)
sipH323CallMediaTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipH323CallMediaTimeouts.setStatus("current")
_SipH323CallInitTimeouts_Type = Counter64
_SipH323CallInitTimeouts_Object = MibScalar
sipH323CallInitTimeouts = _SipH323CallInitTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17, 13),
    _SipH323CallInitTimeouts_Type()
)
sipH323CallInitTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipH323CallInitTimeouts.setStatus("current")
_SipH323TermTimeouts_Type = Counter64
_SipH323TermTimeouts_Object = MibScalar
sipH323TermTimeouts = _SipH323TermTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17, 14),
    _SipH323TermTimeouts_Type()
)
sipH323TermTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipH323TermTimeouts.setStatus("current")
_SipH323MsgErrs_Type = Counter64
_SipH323MsgErrs_Object = MibScalar
sipH323MsgErrs = _SipH323MsgErrs_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17, 15),
    _SipH323MsgErrs_Type()
)
sipH323MsgErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipH323MsgErrs.setStatus("current")
_SipH323CallsProcessed_Type = Counter64
_SipH323CallsProcessed_Object = MibScalar
sipH323CallsProcessed = _SipH323CallsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17, 16),
    _SipH323CallsProcessed_Type()
)
sipH323CallsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipH323CallsProcessed.setStatus("current")
_SipH323PeakLocalCalls_Type = Counter64
_SipH323PeakLocalCalls_Object = MibScalar
sipH323PeakLocalCalls = _SipH323PeakLocalCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17, 17),
    _SipH323PeakLocalCalls_Type()
)
sipH323PeakLocalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipH323PeakLocalCalls.setStatus("current")
_SipH323RedirectSuccess_Type = Counter64
_SipH323RedirectSuccess_Object = MibScalar
sipH323RedirectSuccess = _SipH323RedirectSuccess_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17, 18),
    _SipH323RedirectSuccess_Type()
)
sipH323RedirectSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipH323RedirectSuccess.setStatus("deprecated")
_SipH323RedirectFailures_Type = Counter64
_SipH323RedirectFailures_Object = MibScalar
sipH323RedirectFailures = _SipH323RedirectFailures_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17, 19),
    _SipH323RedirectFailures_Type()
)
sipH323RedirectFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipH323RedirectFailures.setStatus("deprecated")
_SipH323MessageRoutingFailures_Type = Counter64
_SipH323MessageRoutingFailures_Object = MibScalar
sipH323MessageRoutingFailures = _SipH323MessageRoutingFailures_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17, 20),
    _SipH323MessageRoutingFailures_Type()
)
sipH323MessageRoutingFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipH323MessageRoutingFailures.setStatus("current")
_SipH323AuthenticationChallenges_Type = Counter64
_SipH323AuthenticationChallenges_Object = MibScalar
sipH323AuthenticationChallenges = _SipH323AuthenticationChallenges_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17, 21),
    _SipH323AuthenticationChallenges_Type()
)
sipH323AuthenticationChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipH323AuthenticationChallenges.setStatus("current")
_SipH323RTPFWTraversalTimeouts_Type = Counter64
_SipH323RTPFWTraversalTimeouts_Object = MibScalar
sipH323RTPFWTraversalTimeouts = _SipH323RTPFWTraversalTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17, 22),
    _SipH323RTPFWTraversalTimeouts_Type()
)
sipH323RTPFWTraversalTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipH323RTPFWTraversalTimeouts.setStatus("current")
_SipH323MessagesReroutedToMate_Type = Counter64
_SipH323MessagesReroutedToMate_Object = MibScalar
sipH323MessagesReroutedToMate = _SipH323MessagesReroutedToMate_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17, 23),
    _SipH323MessagesReroutedToMate_Type()
)
sipH323MessagesReroutedToMate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipH323MessagesReroutedToMate.setStatus("deprecated")
_SipH323SameSideActiveCalls_Type = Counter64
_SipH323SameSideActiveCalls_Object = MibScalar
sipH323SameSideActiveCalls = _SipH323SameSideActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17, 24),
    _SipH323SameSideActiveCalls_Type()
)
sipH323SameSideActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipH323SameSideActiveCalls.setStatus("current")
_SipH323NormalActiveCalls_Type = Counter64
_SipH323NormalActiveCalls_Object = MibScalar
sipH323NormalActiveCalls = _SipH323NormalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17, 25),
    _SipH323NormalActiveCalls_Type()
)
sipH323NormalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipH323NormalActiveCalls.setStatus("current")
_SipH323PeakSameSideActiveCalls_Type = Counter64
_SipH323PeakSameSideActiveCalls_Object = MibScalar
sipH323PeakSameSideActiveCalls = _SipH323PeakSameSideActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17, 26),
    _SipH323PeakSameSideActiveCalls_Type()
)
sipH323PeakSameSideActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipH323PeakSameSideActiveCalls.setStatus("current")
_SipH323PeakNormalActiveCalls_Type = Counter64
_SipH323PeakNormalActiveCalls_Object = MibScalar
sipH323PeakNormalActiveCalls = _SipH323PeakNormalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17, 27),
    _SipH323PeakNormalActiveCalls_Type()
)
sipH323PeakNormalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipH323PeakNormalActiveCalls.setStatus("current")
_SipH323CurrentFaxSessions_Type = Counter64
_SipH323CurrentFaxSessions_Object = MibScalar
sipH323CurrentFaxSessions = _SipH323CurrentFaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17, 28),
    _SipH323CurrentFaxSessions_Type()
)
sipH323CurrentFaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipH323CurrentFaxSessions.setStatus("deprecated")
_SipH323PeakFaxSessions_Type = Counter64
_SipH323PeakFaxSessions_Object = MibScalar
sipH323PeakFaxSessions = _SipH323PeakFaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17, 29),
    _SipH323PeakFaxSessions_Type()
)
sipH323PeakFaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipH323PeakFaxSessions.setStatus("deprecated")
_SipH323TotalFaxSessions_Type = Counter64
_SipH323TotalFaxSessions_Object = MibScalar
sipH323TotalFaxSessions = _SipH323TotalFaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 17, 30),
    _SipH323TotalFaxSessions_Type()
)
sipH323TotalFaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipH323TotalFaxSessions.setStatus("deprecated")
_H323Stats_ObjectIdentity = ObjectIdentity
h323Stats = _H323Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 18)
)
_H323CallsInitiating_Type = Counter64
_H323CallsInitiating_Object = MibScalar
h323CallsInitiating = _H323CallsInitiating_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 18, 1),
    _H323CallsInitiating_Type()
)
h323CallsInitiating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323CallsInitiating.setStatus("current")
_H323LocalActiveCalls_Type = Counter64
_H323LocalActiveCalls_Object = MibScalar
h323LocalActiveCalls = _H323LocalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 18, 2),
    _H323LocalActiveCalls_Type()
)
h323LocalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323LocalActiveCalls.setStatus("current")
_H323TermCalls_Type = Counter64
_H323TermCalls_Object = MibScalar
h323TermCalls = _H323TermCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 18, 3),
    _H323TermCalls_Type()
)
h323TermCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323TermCalls.setStatus("current")
_H323PeakTotalActiveCalls_Type = Counter64
_H323PeakTotalActiveCalls_Object = MibScalar
h323PeakTotalActiveCalls = _H323PeakTotalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 18, 4),
    _H323PeakTotalActiveCalls_Type()
)
h323PeakTotalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323PeakTotalActiveCalls.setStatus("current")
_H323TotalActiveCalls_Type = Counter64
_H323TotalActiveCalls_Object = MibScalar
h323TotalActiveCalls = _H323TotalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 18, 5),
    _H323TotalActiveCalls_Type()
)
h323TotalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323TotalActiveCalls.setStatus("current")
_H323CallsCompletedSuccess_Type = Counter64
_H323CallsCompletedSuccess_Object = MibScalar
h323CallsCompletedSuccess = _H323CallsCompletedSuccess_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 18, 6),
    _H323CallsCompletedSuccess_Type()
)
h323CallsCompletedSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323CallsCompletedSuccess.setStatus("current")
_H323CallsFailed_Type = Counter64
_H323CallsFailed_Object = MibScalar
h323CallsFailed = _H323CallsFailed_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 18, 7),
    _H323CallsFailed_Type()
)
h323CallsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323CallsFailed.setStatus("current")
_H323CallsAbandoned_Type = Counter64
_H323CallsAbandoned_Object = MibScalar
h323CallsAbandoned = _H323CallsAbandoned_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 18, 8),
    _H323CallsAbandoned_Type()
)
h323CallsAbandoned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323CallsAbandoned.setStatus("current")
_H323CallsDropped_Type = Counter64
_H323CallsDropped_Object = MibScalar
h323CallsDropped = _H323CallsDropped_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 18, 9),
    _H323CallsDropped_Type()
)
h323CallsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323CallsDropped.setStatus("deprecated")
_H323CallsDegraded_Type = Counter64
_H323CallsDegraded_Object = MibScalar
h323CallsDegraded = _H323CallsDegraded_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 18, 10),
    _H323CallsDegraded_Type()
)
h323CallsDegraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323CallsDegraded.setStatus("current")
_H323AuthFailures_Type = Counter64
_H323AuthFailures_Object = MibScalar
h323AuthFailures = _H323AuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 18, 11),
    _H323AuthFailures_Type()
)
h323AuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323AuthFailures.setStatus("current")
_H323CallMediaTimeouts_Type = Counter64
_H323CallMediaTimeouts_Object = MibScalar
h323CallMediaTimeouts = _H323CallMediaTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 18, 12),
    _H323CallMediaTimeouts_Type()
)
h323CallMediaTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323CallMediaTimeouts.setStatus("current")
_H323CallInitTimeouts_Type = Counter64
_H323CallInitTimeouts_Object = MibScalar
h323CallInitTimeouts = _H323CallInitTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 18, 13),
    _H323CallInitTimeouts_Type()
)
h323CallInitTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323CallInitTimeouts.setStatus("current")
_H323TermTimeouts_Type = Counter64
_H323TermTimeouts_Object = MibScalar
h323TermTimeouts = _H323TermTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 18, 14),
    _H323TermTimeouts_Type()
)
h323TermTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323TermTimeouts.setStatus("current")
_H323MsgErrs_Type = Counter64
_H323MsgErrs_Object = MibScalar
h323MsgErrs = _H323MsgErrs_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 18, 15),
    _H323MsgErrs_Type()
)
h323MsgErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323MsgErrs.setStatus("current")
_H323CallsProcessed_Type = Counter64
_H323CallsProcessed_Object = MibScalar
h323CallsProcessed = _H323CallsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 18, 16),
    _H323CallsProcessed_Type()
)
h323CallsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323CallsProcessed.setStatus("current")
_H323PeakLocalCalls_Type = Counter64
_H323PeakLocalCalls_Object = MibScalar
h323PeakLocalCalls = _H323PeakLocalCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 18, 17),
    _H323PeakLocalCalls_Type()
)
h323PeakLocalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323PeakLocalCalls.setStatus("current")
_H323MessageRoutingFailures_Type = Counter64
_H323MessageRoutingFailures_Object = MibScalar
h323MessageRoutingFailures = _H323MessageRoutingFailures_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 18, 18),
    _H323MessageRoutingFailures_Type()
)
h323MessageRoutingFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323MessageRoutingFailures.setStatus("current")
_H323AuthenticationChallenges_Type = Counter64
_H323AuthenticationChallenges_Object = MibScalar
h323AuthenticationChallenges = _H323AuthenticationChallenges_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 18, 19),
    _H323AuthenticationChallenges_Type()
)
h323AuthenticationChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323AuthenticationChallenges.setStatus("current")
_H323RTPFWTraversalTimeouts_Type = Counter64
_H323RTPFWTraversalTimeouts_Object = MibScalar
h323RTPFWTraversalTimeouts = _H323RTPFWTraversalTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 18, 20),
    _H323RTPFWTraversalTimeouts_Type()
)
h323RTPFWTraversalTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323RTPFWTraversalTimeouts.setStatus("current")
_H323SameSideActiveCalls_Type = Counter64
_H323SameSideActiveCalls_Object = MibScalar
h323SameSideActiveCalls = _H323SameSideActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 18, 21),
    _H323SameSideActiveCalls_Type()
)
h323SameSideActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323SameSideActiveCalls.setStatus("current")
_H323NormalActiveCalls_Type = Counter64
_H323NormalActiveCalls_Object = MibScalar
h323NormalActiveCalls = _H323NormalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 18, 22),
    _H323NormalActiveCalls_Type()
)
h323NormalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323NormalActiveCalls.setStatus("current")
_H323PeakSameSideActiveCalls_Type = Counter64
_H323PeakSameSideActiveCalls_Object = MibScalar
h323PeakSameSideActiveCalls = _H323PeakSameSideActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 18, 23),
    _H323PeakSameSideActiveCalls_Type()
)
h323PeakSameSideActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323PeakSameSideActiveCalls.setStatus("current")
_H323PeakNormalActiveCalls_Type = Counter64
_H323PeakNormalActiveCalls_Object = MibScalar
h323PeakNormalActiveCalls = _H323PeakNormalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 18, 24),
    _H323PeakNormalActiveCalls_Type()
)
h323PeakNormalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323PeakNormalActiveCalls.setStatus("current")
_H323CurrentFaxSessions_Type = Counter64
_H323CurrentFaxSessions_Object = MibScalar
h323CurrentFaxSessions = _H323CurrentFaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 18, 25),
    _H323CurrentFaxSessions_Type()
)
h323CurrentFaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323CurrentFaxSessions.setStatus("deprecated")
_H323PeakFaxSessions_Type = Counter64
_H323PeakFaxSessions_Object = MibScalar
h323PeakFaxSessions = _H323PeakFaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 18, 26),
    _H323PeakFaxSessions_Type()
)
h323PeakFaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323PeakFaxSessions.setStatus("deprecated")
_H323TotalFaxSessions_Type = Counter64
_H323TotalFaxSessions_Object = MibScalar
h323TotalFaxSessions = _H323TotalFaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 18, 27),
    _H323TotalFaxSessions_Type()
)
h323TotalFaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323TotalFaxSessions.setStatus("deprecated")
_VoIpStats_ObjectIdentity = ObjectIdentity
voIpStats = _VoIpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19)
)
_VoIpCallsInitiating_Type = Counter64
_VoIpCallsInitiating_Object = MibScalar
voIpCallsInitiating = _VoIpCallsInitiating_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19, 1),
    _VoIpCallsInitiating_Type()
)
voIpCallsInitiating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voIpCallsInitiating.setStatus("current")
_VoIpLocalActiveCalls_Type = Counter64
_VoIpLocalActiveCalls_Object = MibScalar
voIpLocalActiveCalls = _VoIpLocalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19, 2),
    _VoIpLocalActiveCalls_Type()
)
voIpLocalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voIpLocalActiveCalls.setStatus("current")
_VoIpTermCalls_Type = Counter64
_VoIpTermCalls_Object = MibScalar
voIpTermCalls = _VoIpTermCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19, 3),
    _VoIpTermCalls_Type()
)
voIpTermCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voIpTermCalls.setStatus("current")
_VoIpPeakTotalActiveCalls_Type = Counter64
_VoIpPeakTotalActiveCalls_Object = MibScalar
voIpPeakTotalActiveCalls = _VoIpPeakTotalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19, 4),
    _VoIpPeakTotalActiveCalls_Type()
)
voIpPeakTotalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voIpPeakTotalActiveCalls.setStatus("current")
_VoIpTotalActiveCalls_Type = Counter64
_VoIpTotalActiveCalls_Object = MibScalar
voIpTotalActiveCalls = _VoIpTotalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19, 5),
    _VoIpTotalActiveCalls_Type()
)
voIpTotalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voIpTotalActiveCalls.setStatus("current")
_VoIpCallsCompletedSuccess_Type = Counter64
_VoIpCallsCompletedSuccess_Object = MibScalar
voIpCallsCompletedSuccess = _VoIpCallsCompletedSuccess_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19, 6),
    _VoIpCallsCompletedSuccess_Type()
)
voIpCallsCompletedSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voIpCallsCompletedSuccess.setStatus("current")
_VoIpCallsFailed_Type = Counter64
_VoIpCallsFailed_Object = MibScalar
voIpCallsFailed = _VoIpCallsFailed_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19, 7),
    _VoIpCallsFailed_Type()
)
voIpCallsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voIpCallsFailed.setStatus("current")
_VoIpCallsAbandoned_Type = Counter64
_VoIpCallsAbandoned_Object = MibScalar
voIpCallsAbandoned = _VoIpCallsAbandoned_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19, 8),
    _VoIpCallsAbandoned_Type()
)
voIpCallsAbandoned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voIpCallsAbandoned.setStatus("current")
_VoIpCallsDropped_Type = Counter64
_VoIpCallsDropped_Object = MibScalar
voIpCallsDropped = _VoIpCallsDropped_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19, 9),
    _VoIpCallsDropped_Type()
)
voIpCallsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voIpCallsDropped.setStatus("deprecated")
_VoIpCallsDegraded_Type = Counter64
_VoIpCallsDegraded_Object = MibScalar
voIpCallsDegraded = _VoIpCallsDegraded_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19, 10),
    _VoIpCallsDegraded_Type()
)
voIpCallsDegraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voIpCallsDegraded.setStatus("current")
_VoIpAuthFailures_Type = Counter64
_VoIpAuthFailures_Object = MibScalar
voIpAuthFailures = _VoIpAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19, 11),
    _VoIpAuthFailures_Type()
)
voIpAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voIpAuthFailures.setStatus("current")
_VoIpCallMediaTimeouts_Type = Counter64
_VoIpCallMediaTimeouts_Object = MibScalar
voIpCallMediaTimeouts = _VoIpCallMediaTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19, 12),
    _VoIpCallMediaTimeouts_Type()
)
voIpCallMediaTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voIpCallMediaTimeouts.setStatus("current")
_VoIpCallInitTimeouts_Type = Counter64
_VoIpCallInitTimeouts_Object = MibScalar
voIpCallInitTimeouts = _VoIpCallInitTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19, 13),
    _VoIpCallInitTimeouts_Type()
)
voIpCallInitTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voIpCallInitTimeouts.setStatus("current")
_VoIpTermTimeouts_Type = Counter64
_VoIpTermTimeouts_Object = MibScalar
voIpTermTimeouts = _VoIpTermTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19, 14),
    _VoIpTermTimeouts_Type()
)
voIpTermTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voIpTermTimeouts.setStatus("current")
_VoIpMsgErrs_Type = Counter64
_VoIpMsgErrs_Object = MibScalar
voIpMsgErrs = _VoIpMsgErrs_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19, 15),
    _VoIpMsgErrs_Type()
)
voIpMsgErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voIpMsgErrs.setStatus("current")
_VoIpCallsProcessed_Type = Counter64
_VoIpCallsProcessed_Object = MibScalar
voIpCallsProcessed = _VoIpCallsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19, 16),
    _VoIpCallsProcessed_Type()
)
voIpCallsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voIpCallsProcessed.setStatus("current")
_VoIpPeakLocalCalls_Type = Counter64
_VoIpPeakLocalCalls_Object = MibScalar
voIpPeakLocalCalls = _VoIpPeakLocalCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19, 17),
    _VoIpPeakLocalCalls_Type()
)
voIpPeakLocalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voIpPeakLocalCalls.setStatus("current")
_VoIpRedirectSuccess_Type = Counter64
_VoIpRedirectSuccess_Object = MibScalar
voIpRedirectSuccess = _VoIpRedirectSuccess_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19, 18),
    _VoIpRedirectSuccess_Type()
)
voIpRedirectSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voIpRedirectSuccess.setStatus("deprecated")
_VoIpRedirectFailures_Type = Counter64
_VoIpRedirectFailures_Object = MibScalar
voIpRedirectFailures = _VoIpRedirectFailures_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19, 19),
    _VoIpRedirectFailures_Type()
)
voIpRedirectFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voIpRedirectFailures.setStatus("deprecated")
_VoIpMessageRoutingFailures_Type = Counter64
_VoIpMessageRoutingFailures_Object = MibScalar
voIpMessageRoutingFailures = _VoIpMessageRoutingFailures_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19, 20),
    _VoIpMessageRoutingFailures_Type()
)
voIpMessageRoutingFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voIpMessageRoutingFailures.setStatus("current")
_VoIpAuthenticationChallenges_Type = Counter64
_VoIpAuthenticationChallenges_Object = MibScalar
voIpAuthenticationChallenges = _VoIpAuthenticationChallenges_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19, 21),
    _VoIpAuthenticationChallenges_Type()
)
voIpAuthenticationChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voIpAuthenticationChallenges.setStatus("current")
_VoIpRTPFWTraversalTimeouts_Type = Counter64
_VoIpRTPFWTraversalTimeouts_Object = MibScalar
voIpRTPFWTraversalTimeouts = _VoIpRTPFWTraversalTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19, 22),
    _VoIpRTPFWTraversalTimeouts_Type()
)
voIpRTPFWTraversalTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voIpRTPFWTraversalTimeouts.setStatus("current")
_VoIpMessagesReroutedToMate_Type = Counter64
_VoIpMessagesReroutedToMate_Object = MibScalar
voIpMessagesReroutedToMate = _VoIpMessagesReroutedToMate_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19, 23),
    _VoIpMessagesReroutedToMate_Type()
)
voIpMessagesReroutedToMate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voIpMessagesReroutedToMate.setStatus("deprecated")
_VoIpSameSideActiveCalls_Type = Counter64
_VoIpSameSideActiveCalls_Object = MibScalar
voIpSameSideActiveCalls = _VoIpSameSideActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19, 24),
    _VoIpSameSideActiveCalls_Type()
)
voIpSameSideActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voIpSameSideActiveCalls.setStatus("current")
_VoIpNormalActiveCalls_Type = Counter64
_VoIpNormalActiveCalls_Object = MibScalar
voIpNormalActiveCalls = _VoIpNormalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19, 25),
    _VoIpNormalActiveCalls_Type()
)
voIpNormalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voIpNormalActiveCalls.setStatus("current")
_VoIpPeakSameSideActiveCalls_Type = Counter64
_VoIpPeakSameSideActiveCalls_Object = MibScalar
voIpPeakSameSideActiveCalls = _VoIpPeakSameSideActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19, 26),
    _VoIpPeakSameSideActiveCalls_Type()
)
voIpPeakSameSideActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voIpPeakSameSideActiveCalls.setStatus("current")
_VoIpPeakNormalActiveCalls_Type = Counter64
_VoIpPeakNormalActiveCalls_Object = MibScalar
voIpPeakNormalActiveCalls = _VoIpPeakNormalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19, 27),
    _VoIpPeakNormalActiveCalls_Type()
)
voIpPeakNormalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voIpPeakNormalActiveCalls.setStatus("current")
_VoIpCurrentFaxSessions_Type = Counter64
_VoIpCurrentFaxSessions_Object = MibScalar
voIpCurrentFaxSessions = _VoIpCurrentFaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19, 28),
    _VoIpCurrentFaxSessions_Type()
)
voIpCurrentFaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voIpCurrentFaxSessions.setStatus("deprecated")
_VoIpPeakFaxSessions_Type = Counter64
_VoIpPeakFaxSessions_Object = MibScalar
voIpPeakFaxSessions = _VoIpPeakFaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19, 29),
    _VoIpPeakFaxSessions_Type()
)
voIpPeakFaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voIpPeakFaxSessions.setStatus("deprecated")
_VoIpTotalFaxSessions_Type = Counter64
_VoIpTotalFaxSessions_Object = MibScalar
voIpTotalFaxSessions = _VoIpTotalFaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 19, 30),
    _VoIpTotalFaxSessions_Type()
)
voIpTotalFaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voIpTotalFaxSessions.setStatus("deprecated")
_CustSipH323Stats_ObjectIdentity = ObjectIdentity
custSipH323Stats = _CustSipH323Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 20)
)
_CustSipH323StatsTable_Object = MibTable
custSipH323StatsTable = _CustSipH323StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 20, 1)
)
if mibBuilder.loadTexts:
    custSipH323StatsTable.setStatus("current")
_CustSipH323StatsEntry_Object = MibTableRow
custSipH323StatsEntry = _CustSipH323StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 20, 1, 1)
)
custSipH323StatsEntry.setIndexNames(
    (0, "Netrake-MIB", "custSipH323Id"),
)
if mibBuilder.loadTexts:
    custSipH323StatsEntry.setStatus("current")
_CustSipH323Id_Type = Integer32
_CustSipH323Id_Object = MibTableColumn
custSipH323Id = _CustSipH323Id_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 20, 1, 1, 1),
    _CustSipH323Id_Type()
)
custSipH323Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipH323Id.setStatus("current")
_CustSipH323CallsInitiating_Type = Counter64
_CustSipH323CallsInitiating_Object = MibTableColumn
custSipH323CallsInitiating = _CustSipH323CallsInitiating_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 20, 1, 1, 2),
    _CustSipH323CallsInitiating_Type()
)
custSipH323CallsInitiating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipH323CallsInitiating.setStatus("current")
_CustSipH323LocalActiveCalls_Type = Counter64
_CustSipH323LocalActiveCalls_Object = MibTableColumn
custSipH323LocalActiveCalls = _CustSipH323LocalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 20, 1, 1, 3),
    _CustSipH323LocalActiveCalls_Type()
)
custSipH323LocalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipH323LocalActiveCalls.setStatus("current")
_CustSipH323TermCalls_Type = Counter64
_CustSipH323TermCalls_Object = MibTableColumn
custSipH323TermCalls = _CustSipH323TermCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 20, 1, 1, 4),
    _CustSipH323TermCalls_Type()
)
custSipH323TermCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipH323TermCalls.setStatus("current")
_CustSipH323PeakTotalActiveCalls_Type = Counter64
_CustSipH323PeakTotalActiveCalls_Object = MibTableColumn
custSipH323PeakTotalActiveCalls = _CustSipH323PeakTotalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 20, 1, 1, 5),
    _CustSipH323PeakTotalActiveCalls_Type()
)
custSipH323PeakTotalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipH323PeakTotalActiveCalls.setStatus("current")
_CustSipH323TotalActiveCalls_Type = Counter64
_CustSipH323TotalActiveCalls_Object = MibTableColumn
custSipH323TotalActiveCalls = _CustSipH323TotalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 20, 1, 1, 6),
    _CustSipH323TotalActiveCalls_Type()
)
custSipH323TotalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipH323TotalActiveCalls.setStatus("current")
_CustSipH323CallsCompletedSuccess_Type = Counter64
_CustSipH323CallsCompletedSuccess_Object = MibTableColumn
custSipH323CallsCompletedSuccess = _CustSipH323CallsCompletedSuccess_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 20, 1, 1, 7),
    _CustSipH323CallsCompletedSuccess_Type()
)
custSipH323CallsCompletedSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipH323CallsCompletedSuccess.setStatus("current")
_CustSipH323CallsFailed_Type = Counter64
_CustSipH323CallsFailed_Object = MibTableColumn
custSipH323CallsFailed = _CustSipH323CallsFailed_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 20, 1, 1, 8),
    _CustSipH323CallsFailed_Type()
)
custSipH323CallsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipH323CallsFailed.setStatus("current")
_CustSipH323CallsAbandoned_Type = Counter64
_CustSipH323CallsAbandoned_Object = MibTableColumn
custSipH323CallsAbandoned = _CustSipH323CallsAbandoned_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 20, 1, 1, 9),
    _CustSipH323CallsAbandoned_Type()
)
custSipH323CallsAbandoned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipH323CallsAbandoned.setStatus("current")
_CustSipH323CallsDropped_Type = Counter64
_CustSipH323CallsDropped_Object = MibTableColumn
custSipH323CallsDropped = _CustSipH323CallsDropped_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 20, 1, 1, 10),
    _CustSipH323CallsDropped_Type()
)
custSipH323CallsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipH323CallsDropped.setStatus("deprecated")
_CustSipH323CallsDegraded_Type = Counter64
_CustSipH323CallsDegraded_Object = MibTableColumn
custSipH323CallsDegraded = _CustSipH323CallsDegraded_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 20, 1, 1, 11),
    _CustSipH323CallsDegraded_Type()
)
custSipH323CallsDegraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipH323CallsDegraded.setStatus("current")
_CustSipH323CallMediaTimeouts_Type = Counter64
_CustSipH323CallMediaTimeouts_Object = MibTableColumn
custSipH323CallMediaTimeouts = _CustSipH323CallMediaTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 20, 1, 1, 12),
    _CustSipH323CallMediaTimeouts_Type()
)
custSipH323CallMediaTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipH323CallMediaTimeouts.setStatus("current")
_CustSipH323CallInitTimeouts_Type = Counter64
_CustSipH323CallInitTimeouts_Object = MibTableColumn
custSipH323CallInitTimeouts = _CustSipH323CallInitTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 20, 1, 1, 13),
    _CustSipH323CallInitTimeouts_Type()
)
custSipH323CallInitTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipH323CallInitTimeouts.setStatus("current")
_CustSipH323TermTimeouts_Type = Counter64
_CustSipH323TermTimeouts_Object = MibTableColumn
custSipH323TermTimeouts = _CustSipH323TermTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 20, 1, 1, 14),
    _CustSipH323TermTimeouts_Type()
)
custSipH323TermTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipH323TermTimeouts.setStatus("current")
_CustSipH323CallsProcessed_Type = Counter64
_CustSipH323CallsProcessed_Object = MibTableColumn
custSipH323CallsProcessed = _CustSipH323CallsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 20, 1, 1, 15),
    _CustSipH323CallsProcessed_Type()
)
custSipH323CallsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipH323CallsProcessed.setStatus("current")
_CustSipH323PeakLocalCalls_Type = Counter64
_CustSipH323PeakLocalCalls_Object = MibTableColumn
custSipH323PeakLocalCalls = _CustSipH323PeakLocalCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 20, 1, 1, 16),
    _CustSipH323PeakLocalCalls_Type()
)
custSipH323PeakLocalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipH323PeakLocalCalls.setStatus("current")
_CustSipH323AuthenticationChallenges_Type = Counter64
_CustSipH323AuthenticationChallenges_Object = MibTableColumn
custSipH323AuthenticationChallenges = _CustSipH323AuthenticationChallenges_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 20, 1, 1, 17),
    _CustSipH323AuthenticationChallenges_Type()
)
custSipH323AuthenticationChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipH323AuthenticationChallenges.setStatus("current")
_CustSipH323RTPFWTraversalTimeouts_Type = Counter64
_CustSipH323RTPFWTraversalTimeouts_Object = MibTableColumn
custSipH323RTPFWTraversalTimeouts = _CustSipH323RTPFWTraversalTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 20, 1, 1, 18),
    _CustSipH323RTPFWTraversalTimeouts_Type()
)
custSipH323RTPFWTraversalTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipH323RTPFWTraversalTimeouts.setStatus("current")
_CustSipH323SameSideActiveCalls_Type = Counter64
_CustSipH323SameSideActiveCalls_Object = MibTableColumn
custSipH323SameSideActiveCalls = _CustSipH323SameSideActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 20, 1, 1, 19),
    _CustSipH323SameSideActiveCalls_Type()
)
custSipH323SameSideActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipH323SameSideActiveCalls.setStatus("current")
_CustSipH323NormalActiveCalls_Type = Counter64
_CustSipH323NormalActiveCalls_Object = MibTableColumn
custSipH323NormalActiveCalls = _CustSipH323NormalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 20, 1, 1, 20),
    _CustSipH323NormalActiveCalls_Type()
)
custSipH323NormalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipH323NormalActiveCalls.setStatus("current")
_CustSipH323PeakNormalActiveCalls_Type = Counter64
_CustSipH323PeakNormalActiveCalls_Object = MibTableColumn
custSipH323PeakNormalActiveCalls = _CustSipH323PeakNormalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 20, 1, 1, 21),
    _CustSipH323PeakNormalActiveCalls_Type()
)
custSipH323PeakNormalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custSipH323PeakNormalActiveCalls.setStatus("current")
_CustH323Stats_ObjectIdentity = ObjectIdentity
custH323Stats = _CustH323Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 21)
)
_CustH323StatsTable_Object = MibTable
custH323StatsTable = _CustH323StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 21, 1)
)
if mibBuilder.loadTexts:
    custH323StatsTable.setStatus("current")
_CustH323StatsEntry_Object = MibTableRow
custH323StatsEntry = _CustH323StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 21, 1, 1)
)
custH323StatsEntry.setIndexNames(
    (0, "Netrake-MIB", "custH323Id"),
)
if mibBuilder.loadTexts:
    custH323StatsEntry.setStatus("current")
_CustH323Id_Type = Integer32
_CustH323Id_Object = MibTableColumn
custH323Id = _CustH323Id_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 21, 1, 1, 1),
    _CustH323Id_Type()
)
custH323Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custH323Id.setStatus("current")
_CustH323CallsInitiating_Type = Counter64
_CustH323CallsInitiating_Object = MibTableColumn
custH323CallsInitiating = _CustH323CallsInitiating_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 21, 1, 1, 2),
    _CustH323CallsInitiating_Type()
)
custH323CallsInitiating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custH323CallsInitiating.setStatus("current")
_CustH323LocalActiveCalls_Type = Counter64
_CustH323LocalActiveCalls_Object = MibTableColumn
custH323LocalActiveCalls = _CustH323LocalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 21, 1, 1, 3),
    _CustH323LocalActiveCalls_Type()
)
custH323LocalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custH323LocalActiveCalls.setStatus("current")
_CustH323TermCalls_Type = Counter64
_CustH323TermCalls_Object = MibTableColumn
custH323TermCalls = _CustH323TermCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 21, 1, 1, 4),
    _CustH323TermCalls_Type()
)
custH323TermCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custH323TermCalls.setStatus("current")
_CustH323PeakTotalActiveCalls_Type = Counter64
_CustH323PeakTotalActiveCalls_Object = MibTableColumn
custH323PeakTotalActiveCalls = _CustH323PeakTotalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 21, 1, 1, 5),
    _CustH323PeakTotalActiveCalls_Type()
)
custH323PeakTotalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custH323PeakTotalActiveCalls.setStatus("current")
_CustH323TotalActiveCalls_Type = Counter64
_CustH323TotalActiveCalls_Object = MibTableColumn
custH323TotalActiveCalls = _CustH323TotalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 21, 1, 1, 6),
    _CustH323TotalActiveCalls_Type()
)
custH323TotalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custH323TotalActiveCalls.setStatus("current")
_CustH323CallsCompletedSuccess_Type = Counter64
_CustH323CallsCompletedSuccess_Object = MibTableColumn
custH323CallsCompletedSuccess = _CustH323CallsCompletedSuccess_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 21, 1, 1, 7),
    _CustH323CallsCompletedSuccess_Type()
)
custH323CallsCompletedSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custH323CallsCompletedSuccess.setStatus("current")
_CustH323CallsFailed_Type = Counter64
_CustH323CallsFailed_Object = MibTableColumn
custH323CallsFailed = _CustH323CallsFailed_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 21, 1, 1, 8),
    _CustH323CallsFailed_Type()
)
custH323CallsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custH323CallsFailed.setStatus("current")
_CustH323CallsAbandoned_Type = Counter64
_CustH323CallsAbandoned_Object = MibTableColumn
custH323CallsAbandoned = _CustH323CallsAbandoned_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 21, 1, 1, 9),
    _CustH323CallsAbandoned_Type()
)
custH323CallsAbandoned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custH323CallsAbandoned.setStatus("current")
_CustH323CallsDropped_Type = Counter64
_CustH323CallsDropped_Object = MibTableColumn
custH323CallsDropped = _CustH323CallsDropped_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 21, 1, 1, 10),
    _CustH323CallsDropped_Type()
)
custH323CallsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custH323CallsDropped.setStatus("deprecated")
_CustH323CallsDegraded_Type = Counter64
_CustH323CallsDegraded_Object = MibTableColumn
custH323CallsDegraded = _CustH323CallsDegraded_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 21, 1, 1, 11),
    _CustH323CallsDegraded_Type()
)
custH323CallsDegraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custH323CallsDegraded.setStatus("current")
_CustH323CallMediaTimeouts_Type = Counter64
_CustH323CallMediaTimeouts_Object = MibTableColumn
custH323CallMediaTimeouts = _CustH323CallMediaTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 21, 1, 1, 12),
    _CustH323CallMediaTimeouts_Type()
)
custH323CallMediaTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custH323CallMediaTimeouts.setStatus("current")
_CustH323CallInitTimeouts_Type = Counter64
_CustH323CallInitTimeouts_Object = MibTableColumn
custH323CallInitTimeouts = _CustH323CallInitTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 21, 1, 1, 13),
    _CustH323CallInitTimeouts_Type()
)
custH323CallInitTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custH323CallInitTimeouts.setStatus("current")
_CustH323TermTimeouts_Type = Counter64
_CustH323TermTimeouts_Object = MibTableColumn
custH323TermTimeouts = _CustH323TermTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 21, 1, 1, 14),
    _CustH323TermTimeouts_Type()
)
custH323TermTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custH323TermTimeouts.setStatus("current")
_CustH323CallsProcessed_Type = Counter64
_CustH323CallsProcessed_Object = MibTableColumn
custH323CallsProcessed = _CustH323CallsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 21, 1, 1, 15),
    _CustH323CallsProcessed_Type()
)
custH323CallsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custH323CallsProcessed.setStatus("current")
_CustH323PeakLocalCalls_Type = Counter64
_CustH323PeakLocalCalls_Object = MibTableColumn
custH323PeakLocalCalls = _CustH323PeakLocalCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 21, 1, 1, 16),
    _CustH323PeakLocalCalls_Type()
)
custH323PeakLocalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custH323PeakLocalCalls.setStatus("current")
_CustH323AuthenticationChallenges_Type = Counter64
_CustH323AuthenticationChallenges_Object = MibTableColumn
custH323AuthenticationChallenges = _CustH323AuthenticationChallenges_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 21, 1, 1, 17),
    _CustH323AuthenticationChallenges_Type()
)
custH323AuthenticationChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custH323AuthenticationChallenges.setStatus("current")
_CustH323RTPFWTraversalTimeouts_Type = Counter64
_CustH323RTPFWTraversalTimeouts_Object = MibTableColumn
custH323RTPFWTraversalTimeouts = _CustH323RTPFWTraversalTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 21, 1, 1, 18),
    _CustH323RTPFWTraversalTimeouts_Type()
)
custH323RTPFWTraversalTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custH323RTPFWTraversalTimeouts.setStatus("current")
_CustH323SameSideActiveCalls_Type = Counter64
_CustH323SameSideActiveCalls_Object = MibTableColumn
custH323SameSideActiveCalls = _CustH323SameSideActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 21, 1, 1, 19),
    _CustH323SameSideActiveCalls_Type()
)
custH323SameSideActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custH323SameSideActiveCalls.setStatus("current")
_CustH323NormalActiveCalls_Type = Counter64
_CustH323NormalActiveCalls_Object = MibTableColumn
custH323NormalActiveCalls = _CustH323NormalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 21, 1, 1, 20),
    _CustH323NormalActiveCalls_Type()
)
custH323NormalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custH323NormalActiveCalls.setStatus("current")
_CustH323PeakNormalActiveCalls_Type = Counter64
_CustH323PeakNormalActiveCalls_Object = MibTableColumn
custH323PeakNormalActiveCalls = _CustH323PeakNormalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 21, 1, 1, 21),
    _CustH323PeakNormalActiveCalls_Type()
)
custH323PeakNormalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custH323PeakNormalActiveCalls.setStatus("current")
_CustVoIpStats_ObjectIdentity = ObjectIdentity
custVoIpStats = _CustVoIpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 22)
)
_CustVoIpStatsTable_Object = MibTable
custVoIpStatsTable = _CustVoIpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 22, 1)
)
if mibBuilder.loadTexts:
    custVoIpStatsTable.setStatus("current")
_CustVoIpStatsEntry_Object = MibTableRow
custVoIpStatsEntry = _CustVoIpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 22, 1, 1)
)
custVoIpStatsEntry.setIndexNames(
    (0, "Netrake-MIB", "custVoIpId"),
)
if mibBuilder.loadTexts:
    custVoIpStatsEntry.setStatus("current")
_CustVoIpId_Type = Integer32
_CustVoIpId_Object = MibTableColumn
custVoIpId = _CustVoIpId_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 22, 1, 1, 1),
    _CustVoIpId_Type()
)
custVoIpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custVoIpId.setStatus("current")
_CustVoIpCallsInitiating_Type = Counter64
_CustVoIpCallsInitiating_Object = MibTableColumn
custVoIpCallsInitiating = _CustVoIpCallsInitiating_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 22, 1, 1, 2),
    _CustVoIpCallsInitiating_Type()
)
custVoIpCallsInitiating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custVoIpCallsInitiating.setStatus("current")
_CustVoIpLocalActiveCalls_Type = Counter64
_CustVoIpLocalActiveCalls_Object = MibTableColumn
custVoIpLocalActiveCalls = _CustVoIpLocalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 22, 1, 1, 3),
    _CustVoIpLocalActiveCalls_Type()
)
custVoIpLocalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custVoIpLocalActiveCalls.setStatus("current")
_CustVoIpTermCalls_Type = Counter64
_CustVoIpTermCalls_Object = MibTableColumn
custVoIpTermCalls = _CustVoIpTermCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 22, 1, 1, 4),
    _CustVoIpTermCalls_Type()
)
custVoIpTermCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custVoIpTermCalls.setStatus("current")
_CustVoIpPeakTotalActiveCalls_Type = Counter64
_CustVoIpPeakTotalActiveCalls_Object = MibTableColumn
custVoIpPeakTotalActiveCalls = _CustVoIpPeakTotalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 22, 1, 1, 5),
    _CustVoIpPeakTotalActiveCalls_Type()
)
custVoIpPeakTotalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custVoIpPeakTotalActiveCalls.setStatus("current")
_CustVoIpTotalActiveCalls_Type = Counter64
_CustVoIpTotalActiveCalls_Object = MibTableColumn
custVoIpTotalActiveCalls = _CustVoIpTotalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 22, 1, 1, 6),
    _CustVoIpTotalActiveCalls_Type()
)
custVoIpTotalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custVoIpTotalActiveCalls.setStatus("current")
_CustVoIpCallsCompletedSuccess_Type = Counter64
_CustVoIpCallsCompletedSuccess_Object = MibTableColumn
custVoIpCallsCompletedSuccess = _CustVoIpCallsCompletedSuccess_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 22, 1, 1, 7),
    _CustVoIpCallsCompletedSuccess_Type()
)
custVoIpCallsCompletedSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custVoIpCallsCompletedSuccess.setStatus("current")
_CustVoIpCallsFailed_Type = Counter64
_CustVoIpCallsFailed_Object = MibTableColumn
custVoIpCallsFailed = _CustVoIpCallsFailed_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 22, 1, 1, 8),
    _CustVoIpCallsFailed_Type()
)
custVoIpCallsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custVoIpCallsFailed.setStatus("current")
_CustVoIpCallsAbandoned_Type = Counter64
_CustVoIpCallsAbandoned_Object = MibTableColumn
custVoIpCallsAbandoned = _CustVoIpCallsAbandoned_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 22, 1, 1, 9),
    _CustVoIpCallsAbandoned_Type()
)
custVoIpCallsAbandoned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custVoIpCallsAbandoned.setStatus("current")
_CustVoIpCallsDropped_Type = Counter64
_CustVoIpCallsDropped_Object = MibTableColumn
custVoIpCallsDropped = _CustVoIpCallsDropped_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 22, 1, 1, 10),
    _CustVoIpCallsDropped_Type()
)
custVoIpCallsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custVoIpCallsDropped.setStatus("deprecated")
_CustVoIpCallsDegraded_Type = Counter64
_CustVoIpCallsDegraded_Object = MibTableColumn
custVoIpCallsDegraded = _CustVoIpCallsDegraded_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 22, 1, 1, 11),
    _CustVoIpCallsDegraded_Type()
)
custVoIpCallsDegraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custVoIpCallsDegraded.setStatus("current")
_CustVoIpCallMediaTimeouts_Type = Counter64
_CustVoIpCallMediaTimeouts_Object = MibTableColumn
custVoIpCallMediaTimeouts = _CustVoIpCallMediaTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 22, 1, 1, 12),
    _CustVoIpCallMediaTimeouts_Type()
)
custVoIpCallMediaTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custVoIpCallMediaTimeouts.setStatus("current")
_CustVoIpCallInitTimeouts_Type = Counter64
_CustVoIpCallInitTimeouts_Object = MibTableColumn
custVoIpCallInitTimeouts = _CustVoIpCallInitTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 22, 1, 1, 13),
    _CustVoIpCallInitTimeouts_Type()
)
custVoIpCallInitTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custVoIpCallInitTimeouts.setStatus("current")
_CustVoIpTermTimeouts_Type = Counter64
_CustVoIpTermTimeouts_Object = MibTableColumn
custVoIpTermTimeouts = _CustVoIpTermTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 22, 1, 1, 14),
    _CustVoIpTermTimeouts_Type()
)
custVoIpTermTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custVoIpTermTimeouts.setStatus("current")
_CustVoIpCallsProcessed_Type = Counter64
_CustVoIpCallsProcessed_Object = MibTableColumn
custVoIpCallsProcessed = _CustVoIpCallsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 22, 1, 1, 15),
    _CustVoIpCallsProcessed_Type()
)
custVoIpCallsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custVoIpCallsProcessed.setStatus("current")
_CustVoIpPeakLocalCalls_Type = Counter64
_CustVoIpPeakLocalCalls_Object = MibTableColumn
custVoIpPeakLocalCalls = _CustVoIpPeakLocalCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 22, 1, 1, 16),
    _CustVoIpPeakLocalCalls_Type()
)
custVoIpPeakLocalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custVoIpPeakLocalCalls.setStatus("current")
_CustVoIpAuthenticationChallenges_Type = Counter64
_CustVoIpAuthenticationChallenges_Object = MibTableColumn
custVoIpAuthenticationChallenges = _CustVoIpAuthenticationChallenges_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 22, 1, 1, 17),
    _CustVoIpAuthenticationChallenges_Type()
)
custVoIpAuthenticationChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custVoIpAuthenticationChallenges.setStatus("current")
_CustVoIpRTPFWTraversalTimeouts_Type = Counter64
_CustVoIpRTPFWTraversalTimeouts_Object = MibTableColumn
custVoIpRTPFWTraversalTimeouts = _CustVoIpRTPFWTraversalTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 22, 1, 1, 18),
    _CustVoIpRTPFWTraversalTimeouts_Type()
)
custVoIpRTPFWTraversalTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custVoIpRTPFWTraversalTimeouts.setStatus("current")
_CustVoIpSameSideActiveCalls_Type = Counter64
_CustVoIpSameSideActiveCalls_Object = MibTableColumn
custVoIpSameSideActiveCalls = _CustVoIpSameSideActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 22, 1, 1, 19),
    _CustVoIpSameSideActiveCalls_Type()
)
custVoIpSameSideActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custVoIpSameSideActiveCalls.setStatus("current")
_CustVoIpNormalActiveCalls_Type = Counter64
_CustVoIpNormalActiveCalls_Object = MibTableColumn
custVoIpNormalActiveCalls = _CustVoIpNormalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 22, 1, 1, 20),
    _CustVoIpNormalActiveCalls_Type()
)
custVoIpNormalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custVoIpNormalActiveCalls.setStatus("current")
_CustVoIpPeakNormalActiveCalls_Type = Counter64
_CustVoIpPeakNormalActiveCalls_Object = MibTableColumn
custVoIpPeakNormalActiveCalls = _CustVoIpPeakNormalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 22, 1, 1, 21),
    _CustVoIpPeakNormalActiveCalls_Type()
)
custVoIpPeakNormalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custVoIpPeakNormalActiveCalls.setStatus("current")
_MediaStats_ObjectIdentity = ObjectIdentity
mediaStats = _MediaStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 23)
)
_MediaStatCurrentAudioSessions_Type = Counter64
_MediaStatCurrentAudioSessions_Object = MibScalar
mediaStatCurrentAudioSessions = _MediaStatCurrentAudioSessions_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 23, 1),
    _MediaStatCurrentAudioSessions_Type()
)
mediaStatCurrentAudioSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaStatCurrentAudioSessions.setStatus("current")
_MediaStatPeakAudioSessions_Type = Counter64
_MediaStatPeakAudioSessions_Object = MibScalar
mediaStatPeakAudioSessions = _MediaStatPeakAudioSessions_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 23, 2),
    _MediaStatPeakAudioSessions_Type()
)
mediaStatPeakAudioSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaStatPeakAudioSessions.setStatus("current")
_MediaStatTotalAudioSessions_Type = Counter64
_MediaStatTotalAudioSessions_Object = MibScalar
mediaStatTotalAudioSessions = _MediaStatTotalAudioSessions_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 23, 3),
    _MediaStatTotalAudioSessions_Type()
)
mediaStatTotalAudioSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaStatTotalAudioSessions.setStatus("current")
_MediaStatCurrentVideoSessions_Type = Counter64
_MediaStatCurrentVideoSessions_Object = MibScalar
mediaStatCurrentVideoSessions = _MediaStatCurrentVideoSessions_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 23, 4),
    _MediaStatCurrentVideoSessions_Type()
)
mediaStatCurrentVideoSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaStatCurrentVideoSessions.setStatus("current")
_MediaStatPeakVideoSessions_Type = Counter64
_MediaStatPeakVideoSessions_Object = MibScalar
mediaStatPeakVideoSessions = _MediaStatPeakVideoSessions_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 23, 5),
    _MediaStatPeakVideoSessions_Type()
)
mediaStatPeakVideoSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaStatPeakVideoSessions.setStatus("current")
_MediaStatTotalVideoSessions_Type = Counter64
_MediaStatTotalVideoSessions_Object = MibScalar
mediaStatTotalVideoSessions = _MediaStatTotalVideoSessions_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 23, 6),
    _MediaStatTotalVideoSessions_Type()
)
mediaStatTotalVideoSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaStatTotalVideoSessions.setStatus("current")
_MediaStatCurrentFaxSessions_Type = Counter64
_MediaStatCurrentFaxSessions_Object = MibScalar
mediaStatCurrentFaxSessions = _MediaStatCurrentFaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 23, 7),
    _MediaStatCurrentFaxSessions_Type()
)
mediaStatCurrentFaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaStatCurrentFaxSessions.setStatus("current")
_MediaStatPeakFaxSessions_Type = Counter64
_MediaStatPeakFaxSessions_Object = MibScalar
mediaStatPeakFaxSessions = _MediaStatPeakFaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 23, 8),
    _MediaStatPeakFaxSessions_Type()
)
mediaStatPeakFaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaStatPeakFaxSessions.setStatus("current")
_MediaStatTotalFaxSessions_Type = Counter64
_MediaStatTotalFaxSessions_Object = MibScalar
mediaStatTotalFaxSessions = _MediaStatTotalFaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 23, 9),
    _MediaStatTotalFaxSessions_Type()
)
mediaStatTotalFaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaStatTotalFaxSessions.setStatus("current")
_MediaStatTotalFailures_Type = Counter64
_MediaStatTotalFailures_Object = MibScalar
mediaStatTotalFailures = _MediaStatTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 23, 10),
    _MediaStatTotalFailures_Type()
)
mediaStatTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaStatTotalFailures.setStatus("current")
_H323RegStats_ObjectIdentity = ObjectIdentity
h323RegStats = _H323RegStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 24)
)
_H323RegStatActiveReg_Type = Counter64
_H323RegStatActiveReg_Object = MibScalar
h323RegStatActiveReg = _H323RegStatActiveReg_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 24, 1),
    _H323RegStatActiveReg_Type()
)
h323RegStatActiveReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323RegStatActiveReg.setStatus("current")
_H323RegStatExpiredReg_Type = Counter64
_H323RegStatExpiredReg_Object = MibScalar
h323RegStatExpiredReg = _H323RegStatExpiredReg_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 24, 2),
    _H323RegStatExpiredReg_Type()
)
h323RegStatExpiredReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323RegStatExpiredReg.setStatus("current")
_H323RegStatUnauthorizedReg_Type = Counter64
_H323RegStatUnauthorizedReg_Object = MibScalar
h323RegStatUnauthorizedReg = _H323RegStatUnauthorizedReg_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 24, 3),
    _H323RegStatUnauthorizedReg_Type()
)
h323RegStatUnauthorizedReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323RegStatUnauthorizedReg.setStatus("current")
_H323RegStatPeakActiveReg_Type = Counter64
_H323RegStatPeakActiveReg_Object = MibScalar
h323RegStatPeakActiveReg = _H323RegStatPeakActiveReg_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 24, 4),
    _H323RegStatPeakActiveReg_Type()
)
h323RegStatPeakActiveReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323RegStatPeakActiveReg.setStatus("current")
_H323RegStatUpdateComplete_Type = Counter64
_H323RegStatUpdateComplete_Object = MibScalar
h323RegStatUpdateComplete = _H323RegStatUpdateComplete_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 24, 5),
    _H323RegStatUpdateComplete_Type()
)
h323RegStatUpdateComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323RegStatUpdateComplete.setStatus("current")
_H323RegStatUpdateFailures_Type = Counter64
_H323RegStatUpdateFailures_Object = MibScalar
h323RegStatUpdateFailures = _H323RegStatUpdateFailures_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 24, 6),
    _H323RegStatUpdateFailures_Type()
)
h323RegStatUpdateFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323RegStatUpdateFailures.setStatus("current")
_H323RegStatAuthFailures_Type = Counter64
_H323RegStatAuthFailures_Object = MibScalar
h323RegStatAuthFailures = _H323RegStatAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 24, 7),
    _H323RegStatAuthFailures_Type()
)
h323RegStatAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323RegStatAuthFailures.setStatus("current")
_CustH323RegStats_ObjectIdentity = ObjectIdentity
custH323RegStats = _CustH323RegStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 25)
)
_CustH323RegStatsTable_Object = MibTable
custH323RegStatsTable = _CustH323RegStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 25, 1)
)
if mibBuilder.loadTexts:
    custH323RegStatsTable.setStatus("current")
_CustH323RegStatsEntry_Object = MibTableRow
custH323RegStatsEntry = _CustH323RegStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 25, 1, 1)
)
custH323RegStatsEntry.setIndexNames(
    (0, "Netrake-MIB", "custH323RegStatId"),
)
if mibBuilder.loadTexts:
    custH323RegStatsEntry.setStatus("current")
_CustH323RegStatId_Type = Integer32
_CustH323RegStatId_Object = MibTableColumn
custH323RegStatId = _CustH323RegStatId_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 25, 1, 1, 1),
    _CustH323RegStatId_Type()
)
custH323RegStatId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custH323RegStatId.setStatus("current")
_CustH323RegStatActiveReg_Type = Counter64
_CustH323RegStatActiveReg_Object = MibTableColumn
custH323RegStatActiveReg = _CustH323RegStatActiveReg_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 25, 1, 1, 2),
    _CustH323RegStatActiveReg_Type()
)
custH323RegStatActiveReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custH323RegStatActiveReg.setStatus("current")
_CustH323RegStatExpiredReg_Type = Counter64
_CustH323RegStatExpiredReg_Object = MibTableColumn
custH323RegStatExpiredReg = _CustH323RegStatExpiredReg_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 25, 1, 1, 3),
    _CustH323RegStatExpiredReg_Type()
)
custH323RegStatExpiredReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custH323RegStatExpiredReg.setStatus("current")
_CustH323RegStatUnauthorizedReg_Type = Counter64
_CustH323RegStatUnauthorizedReg_Object = MibTableColumn
custH323RegStatUnauthorizedReg = _CustH323RegStatUnauthorizedReg_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 25, 1, 1, 4),
    _CustH323RegStatUnauthorizedReg_Type()
)
custH323RegStatUnauthorizedReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custH323RegStatUnauthorizedReg.setStatus("current")
_CustH323RegStatPeakActiveReg_Type = Counter64
_CustH323RegStatPeakActiveReg_Object = MibTableColumn
custH323RegStatPeakActiveReg = _CustH323RegStatPeakActiveReg_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 25, 1, 1, 5),
    _CustH323RegStatPeakActiveReg_Type()
)
custH323RegStatPeakActiveReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custH323RegStatPeakActiveReg.setStatus("current")
_CustH323RegStatUpdateComplete_Type = Counter64
_CustH323RegStatUpdateComplete_Object = MibTableColumn
custH323RegStatUpdateComplete = _CustH323RegStatUpdateComplete_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 25, 1, 1, 6),
    _CustH323RegStatUpdateComplete_Type()
)
custH323RegStatUpdateComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custH323RegStatUpdateComplete.setStatus("current")
_CustH323RegStatUpdateFailures_Type = Counter64
_CustH323RegStatUpdateFailures_Object = MibTableColumn
custH323RegStatUpdateFailures = _CustH323RegStatUpdateFailures_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 25, 1, 1, 7),
    _CustH323RegStatUpdateFailures_Type()
)
custH323RegStatUpdateFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custH323RegStatUpdateFailures.setStatus("current")
_CustH323RegStatAuthFailures_Type = Counter64
_CustH323RegStatAuthFailures_Object = MibTableColumn
custH323RegStatAuthFailures = _CustH323RegStatAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 25, 1, 1, 8),
    _CustH323RegStatAuthFailures_Type()
)
custH323RegStatAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custH323RegStatAuthFailures.setStatus("current")
_SipCommonStats_ObjectIdentity = ObjectIdentity
sipCommonStats = _SipCommonStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 26)
)
_SipCommonStatsDiscontinuityTimer_Type = TimeTicks
_SipCommonStatsDiscontinuityTimer_Object = MibScalar
sipCommonStatsDiscontinuityTimer = _SipCommonStatsDiscontinuityTimer_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 26, 1),
    _SipCommonStatsDiscontinuityTimer_Type()
)
sipCommonStatsDiscontinuityTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonStatsDiscontinuityTimer.setStatus("current")
_SipCommonStatsScalars_ObjectIdentity = ObjectIdentity
sipCommonStatsScalars = _SipCommonStatsScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 26, 2)
)
_SipCommonStatsTotalMessageErrors_Type = Counter32
_SipCommonStatsTotalMessageErrors_Object = MibScalar
sipCommonStatsTotalMessageErrors = _SipCommonStatsTotalMessageErrors_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 26, 2, 1),
    _SipCommonStatsTotalMessageErrors_Type()
)
sipCommonStatsTotalMessageErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonStatsTotalMessageErrors.setStatus("current")
_SipCommonStatsTotalMessageRoutingFailures_Type = Counter32
_SipCommonStatsTotalMessageRoutingFailures_Object = MibScalar
sipCommonStatsTotalMessageRoutingFailures = _SipCommonStatsTotalMessageRoutingFailures_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 26, 2, 2),
    _SipCommonStatsTotalMessageRoutingFailures_Type()
)
sipCommonStatsTotalMessageRoutingFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonStatsTotalMessageRoutingFailures.setStatus("current")
_SipCommonStatsTotalMessageTransmitFailures_Type = Counter32
_SipCommonStatsTotalMessageTransmitFailures_Object = MibScalar
sipCommonStatsTotalMessageTransmitFailures = _SipCommonStatsTotalMessageTransmitFailures_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 26, 2, 3),
    _SipCommonStatsTotalMessageTransmitFailures_Type()
)
sipCommonStatsTotalMessageTransmitFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonStatsTotalMessageTransmitFailures.setStatus("current")
_SipCommonStatsTotalAuthenticationFailures_Type = Counter32
_SipCommonStatsTotalAuthenticationFailures_Object = MibScalar
sipCommonStatsTotalAuthenticationFailures = _SipCommonStatsTotalAuthenticationFailures_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 26, 2, 4),
    _SipCommonStatsTotalAuthenticationFailures_Type()
)
sipCommonStatsTotalAuthenticationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonStatsTotalAuthenticationFailures.setStatus("current")
_SipEvtDlgStats_ObjectIdentity = ObjectIdentity
sipEvtDlgStats = _SipEvtDlgStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 27)
)
_SipEvtDlgStatsDiscontinuityTimer_Type = TimeTicks
_SipEvtDlgStatsDiscontinuityTimer_Object = MibScalar
sipEvtDlgStatsDiscontinuityTimer = _SipEvtDlgStatsDiscontinuityTimer_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 27, 1),
    _SipEvtDlgStatsDiscontinuityTimer_Type()
)
sipEvtDlgStatsDiscontinuityTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipEvtDlgStatsDiscontinuityTimer.setStatus("current")
_SipEvtDlgStatsScalars_ObjectIdentity = ObjectIdentity
sipEvtDlgStatsScalars = _SipEvtDlgStatsScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 27, 2)
)
_SipEvtDlgStatsActiveDialogs_Type = Gauge32
_SipEvtDlgStatsActiveDialogs_Object = MibScalar
sipEvtDlgStatsActiveDialogs = _SipEvtDlgStatsActiveDialogs_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 27, 2, 1),
    _SipEvtDlgStatsActiveDialogs_Type()
)
sipEvtDlgStatsActiveDialogs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipEvtDlgStatsActiveDialogs.setStatus("current")
_SipEvtDlgStatsPeakActiveDialogs_Type = Gauge32
_SipEvtDlgStatsPeakActiveDialogs_Object = MibScalar
sipEvtDlgStatsPeakActiveDialogs = _SipEvtDlgStatsPeakActiveDialogs_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 27, 2, 2),
    _SipEvtDlgStatsPeakActiveDialogs_Type()
)
sipEvtDlgStatsPeakActiveDialogs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipEvtDlgStatsPeakActiveDialogs.setStatus("current")
_SipEvtDlgStatsTerminatedDialogs_Type = Counter32
_SipEvtDlgStatsTerminatedDialogs_Object = MibScalar
sipEvtDlgStatsTerminatedDialogs = _SipEvtDlgStatsTerminatedDialogs_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 27, 2, 3),
    _SipEvtDlgStatsTerminatedDialogs_Type()
)
sipEvtDlgStatsTerminatedDialogs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipEvtDlgStatsTerminatedDialogs.setStatus("current")
_SipEvtDlgStatsExpiredDialogs_Type = Counter32
_SipEvtDlgStatsExpiredDialogs_Object = MibScalar
sipEvtDlgStatsExpiredDialogs = _SipEvtDlgStatsExpiredDialogs_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 27, 2, 4),
    _SipEvtDlgStatsExpiredDialogs_Type()
)
sipEvtDlgStatsExpiredDialogs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipEvtDlgStatsExpiredDialogs.setStatus("current")
_SipEvtDlgStatsFailedDialogs_Type = Counter32
_SipEvtDlgStatsFailedDialogs_Object = MibScalar
sipEvtDlgStatsFailedDialogs = _SipEvtDlgStatsFailedDialogs_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 27, 2, 5),
    _SipEvtDlgStatsFailedDialogs_Type()
)
sipEvtDlgStatsFailedDialogs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipEvtDlgStatsFailedDialogs.setStatus("current")
_SipEvtDlgStatsUnauthorizedDialogs_Type = Counter32
_SipEvtDlgStatsUnauthorizedDialogs_Object = MibScalar
sipEvtDlgStatsUnauthorizedDialogs = _SipEvtDlgStatsUnauthorizedDialogs_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 27, 2, 6),
    _SipEvtDlgStatsUnauthorizedDialogs_Type()
)
sipEvtDlgStatsUnauthorizedDialogs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipEvtDlgStatsUnauthorizedDialogs.setStatus("current")
_SipEvtDlgStatsAuthenticationChallenges_Type = Counter32
_SipEvtDlgStatsAuthenticationChallenges_Object = MibScalar
sipEvtDlgStatsAuthenticationChallenges = _SipEvtDlgStatsAuthenticationChallenges_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 27, 2, 7),
    _SipEvtDlgStatsAuthenticationChallenges_Type()
)
sipEvtDlgStatsAuthenticationChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipEvtDlgStatsAuthenticationChallenges.setStatus("current")
_SipEvtDlgCustStatsTable_Object = MibTable
sipEvtDlgCustStatsTable = _SipEvtDlgCustStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 27, 3)
)
if mibBuilder.loadTexts:
    sipEvtDlgCustStatsTable.setStatus("current")
_SipEvtDlgCustStatsEntry_Object = MibTableRow
sipEvtDlgCustStatsEntry = _SipEvtDlgCustStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 27, 3, 1)
)
sipEvtDlgCustStatsEntry.setIndexNames(
    (0, "Netrake-MIB", "sipEvtDlgCustStatsIndex"),
)
if mibBuilder.loadTexts:
    sipEvtDlgCustStatsEntry.setStatus("current")
_SipEvtDlgCustStatsIndex_Type = Integer32
_SipEvtDlgCustStatsIndex_Object = MibTableColumn
sipEvtDlgCustStatsIndex = _SipEvtDlgCustStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 27, 3, 1, 1),
    _SipEvtDlgCustStatsIndex_Type()
)
sipEvtDlgCustStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipEvtDlgCustStatsIndex.setStatus("current")
_SipEvtDlgCustStatsActiveDialogs_Type = Gauge32
_SipEvtDlgCustStatsActiveDialogs_Object = MibTableColumn
sipEvtDlgCustStatsActiveDialogs = _SipEvtDlgCustStatsActiveDialogs_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 27, 3, 1, 2),
    _SipEvtDlgCustStatsActiveDialogs_Type()
)
sipEvtDlgCustStatsActiveDialogs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipEvtDlgCustStatsActiveDialogs.setStatus("current")
_SipEvtDlgCustStatsPeakActiveDialogs_Type = Gauge32
_SipEvtDlgCustStatsPeakActiveDialogs_Object = MibTableColumn
sipEvtDlgCustStatsPeakActiveDialogs = _SipEvtDlgCustStatsPeakActiveDialogs_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 27, 3, 1, 3),
    _SipEvtDlgCustStatsPeakActiveDialogs_Type()
)
sipEvtDlgCustStatsPeakActiveDialogs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipEvtDlgCustStatsPeakActiveDialogs.setStatus("current")
_SipEvtDlgCustStatsTerminatedDialogs_Type = Counter32
_SipEvtDlgCustStatsTerminatedDialogs_Object = MibTableColumn
sipEvtDlgCustStatsTerminatedDialogs = _SipEvtDlgCustStatsTerminatedDialogs_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 27, 3, 1, 4),
    _SipEvtDlgCustStatsTerminatedDialogs_Type()
)
sipEvtDlgCustStatsTerminatedDialogs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipEvtDlgCustStatsTerminatedDialogs.setStatus("current")
_SipEvtDlgCustStatsExpiredDialogs_Type = Counter32
_SipEvtDlgCustStatsExpiredDialogs_Object = MibTableColumn
sipEvtDlgCustStatsExpiredDialogs = _SipEvtDlgCustStatsExpiredDialogs_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 27, 3, 1, 5),
    _SipEvtDlgCustStatsExpiredDialogs_Type()
)
sipEvtDlgCustStatsExpiredDialogs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipEvtDlgCustStatsExpiredDialogs.setStatus("current")
_SipEvtDlgCustStatsFailedDialogs_Type = Counter32
_SipEvtDlgCustStatsFailedDialogs_Object = MibTableColumn
sipEvtDlgCustStatsFailedDialogs = _SipEvtDlgCustStatsFailedDialogs_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 27, 3, 1, 6),
    _SipEvtDlgCustStatsFailedDialogs_Type()
)
sipEvtDlgCustStatsFailedDialogs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipEvtDlgCustStatsFailedDialogs.setStatus("current")
_SipEvtDlgCustStatsUnauthorizedDialogs_Type = Counter32
_SipEvtDlgCustStatsUnauthorizedDialogs_Object = MibTableColumn
sipEvtDlgCustStatsUnauthorizedDialogs = _SipEvtDlgCustStatsUnauthorizedDialogs_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 27, 3, 1, 7),
    _SipEvtDlgCustStatsUnauthorizedDialogs_Type()
)
sipEvtDlgCustStatsUnauthorizedDialogs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipEvtDlgCustStatsUnauthorizedDialogs.setStatus("current")
_SipEvtDlgCustStatsAuthenticationChallenges_Type = Counter32
_SipEvtDlgCustStatsAuthenticationChallenges_Object = MibTableColumn
sipEvtDlgCustStatsAuthenticationChallenges = _SipEvtDlgCustStatsAuthenticationChallenges_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 27, 3, 1, 8),
    _SipEvtDlgCustStatsAuthenticationChallenges_Type()
)
sipEvtDlgCustStatsAuthenticationChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipEvtDlgCustStatsAuthenticationChallenges.setStatus("current")
_Diagnostics_ObjectIdentity = ObjectIdentity
diagnostics = _Diagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 7)
)
_RunDiagGroup_ObjectIdentity = ObjectIdentity
runDiagGroup = _RunDiagGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 7, 2)
)


class _DiagType_Type(Integer32):
    """Custom type diagType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("cardExtLoopback", 6),
          ("cardIntLoopback", 5),
          ("nCiteFullExtLoopback", 2),
          ("nCiteFullIntLoopback", 1),
          ("nCiteInterfaceExtLoopback", 4),
          ("nCiteInterfaceIntLoopback", 3),
          ("portExtLoopback", 8),
          ("portIntLoopback", 7))
    )


_DiagType_Type.__name__ = "Integer32"
_DiagType_Object = MibScalar
diagType = _DiagType_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 7, 2, 1),
    _DiagType_Type()
)
diagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diagType.setStatus("deprecated")


class _DiagDeviceSlotNum_Type(Integer32):
    """Custom type diagDeviceSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_DiagDeviceSlotNum_Type.__name__ = "Integer32"
_DiagDeviceSlotNum_Object = MibScalar
diagDeviceSlotNum = _DiagDeviceSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 7, 2, 2),
    _DiagDeviceSlotNum_Type()
)
diagDeviceSlotNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diagDeviceSlotNum.setStatus("deprecated")


class _DiagDevPortNum_Type(Integer32):
    """Custom type diagDevPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_DiagDevPortNum_Type.__name__ = "Integer32"
_DiagDevPortNum_Object = MibScalar
diagDevPortNum = _DiagDevPortNum_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 7, 2, 3),
    _DiagDevPortNum_Type()
)
diagDevPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diagDevPortNum.setStatus("deprecated")


class _DiagStartCmd_Type(Integer32):
    """Custom type diagStartCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("runDiag", 1))
    )


_DiagStartCmd_Type.__name__ = "Integer32"
_DiagStartCmd_Object = MibScalar
diagStartCmd = _DiagStartCmd_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 7, 2, 4),
    _DiagStartCmd_Type()
)
diagStartCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diagStartCmd.setStatus("deprecated")
_DiagResultsTable_Object = MibTable
diagResultsTable = _DiagResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 7, 3)
)
if mibBuilder.loadTexts:
    diagResultsTable.setStatus("deprecated")
_DiagResultsEntry_Object = MibTableRow
diagResultsEntry = _DiagResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 7, 3, 1)
)
diagResultsEntry.setIndexNames(
    (0, "Netrake-MIB", "diagRsltIndex"),
)
if mibBuilder.loadTexts:
    diagResultsEntry.setStatus("deprecated")
_DiagRsltIndex_Type = Integer32
_DiagRsltIndex_Object = MibTableColumn
diagRsltIndex = _DiagRsltIndex_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 7, 3, 1, 1),
    _DiagRsltIndex_Type()
)
diagRsltIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagRsltIndex.setStatus("deprecated")
_DiagRsltStartTimeStamp_Type = DateAndTime
_DiagRsltStartTimeStamp_Object = MibTableColumn
diagRsltStartTimeStamp = _DiagRsltStartTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 7, 3, 1, 2),
    _DiagRsltStartTimeStamp_Type()
)
diagRsltStartTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagRsltStartTimeStamp.setStatus("deprecated")
_DiagRsltCompleteTimeStamp_Type = DateAndTime
_DiagRsltCompleteTimeStamp_Object = MibTableColumn
diagRsltCompleteTimeStamp = _DiagRsltCompleteTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 7, 3, 1, 3),
    _DiagRsltCompleteTimeStamp_Type()
)
diagRsltCompleteTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagRsltCompleteTimeStamp.setStatus("deprecated")


class _DiagRsltDesc_Type(DisplayString):
    """Custom type diagRsltDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DiagRsltDesc_Type.__name__ = "DisplayString"
_DiagRsltDesc_Object = MibTableColumn
diagRsltDesc = _DiagRsltDesc_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 7, 3, 1, 4),
    _DiagRsltDesc_Type()
)
diagRsltDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagRsltDesc.setStatus("deprecated")


class _DiagRsltType_Type(Integer32):
    """Custom type diagRsltType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("cardExtLoopback", 6),
          ("cardIntLoopback", 5),
          ("nCiteFullExtLoopback", 2),
          ("nCiteFullIntLoopback", 1),
          ("nCiteInterfaceExtLoopback", 4),
          ("nCiteInterfaceIntLoopback", 3),
          ("portExtLoopback", 8),
          ("portIntLoopback", 7))
    )


_DiagRsltType_Type.__name__ = "Integer32"
_DiagRsltType_Object = MibTableColumn
diagRsltType = _DiagRsltType_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 7, 3, 1, 5),
    _DiagRsltType_Type()
)
diagRsltType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagRsltType.setStatus("deprecated")


class _DiagRsltDeviceSlotNum_Type(Integer32):
    """Custom type diagRsltDeviceSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_DiagRsltDeviceSlotNum_Type.__name__ = "Integer32"
_DiagRsltDeviceSlotNum_Object = MibTableColumn
diagRsltDeviceSlotNum = _DiagRsltDeviceSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 7, 3, 1, 6),
    _DiagRsltDeviceSlotNum_Type()
)
diagRsltDeviceSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagRsltDeviceSlotNum.setStatus("deprecated")


class _DiagRsltDevicePortNum_Type(Integer32):
    """Custom type diagRsltDevicePortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_DiagRsltDevicePortNum_Type.__name__ = "Integer32"
_DiagRsltDevicePortNum_Object = MibTableColumn
diagRsltDevicePortNum = _DiagRsltDevicePortNum_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 7, 3, 1, 7),
    _DiagRsltDevicePortNum_Type()
)
diagRsltDevicePortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagRsltDevicePortNum.setStatus("deprecated")
_DiagRsltID_Type = Integer32
_DiagRsltID_Object = MibScalar
diagRsltID = _DiagRsltID_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 7, 6),
    _DiagRsltID_Type()
)
diagRsltID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diagRsltID.setStatus("deprecated")


class _DiagRsltAcknowledge_Type(Integer32):
    """Custom type diagRsltAcknowledge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("acknowledge", 1),
          ("default", 0))
    )


_DiagRsltAcknowledge_Type.__name__ = "Integer32"
_DiagRsltAcknowledge_Object = MibScalar
diagRsltAcknowledge = _DiagRsltAcknowledge_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 7, 7),
    _DiagRsltAcknowledge_Type()
)
diagRsltAcknowledge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diagRsltAcknowledge.setStatus("deprecated")


class _DiagStartedTrapAck_Type(Integer32):
    """Custom type diagStartedTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("notAck", 0))
    )


_DiagStartedTrapAck_Type.__name__ = "Integer32"
_DiagStartedTrapAck_Object = MibScalar
diagStartedTrapAck = _DiagStartedTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 7, 8),
    _DiagStartedTrapAck_Type()
)
diagStartedTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diagStartedTrapAck.setStatus("deprecated")


class _DiagCompleteTrapAck_Type(Integer32):
    """Custom type diagCompleteTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("notAck", 0))
    )


_DiagCompleteTrapAck_Type.__name__ = "Integer32"
_DiagCompleteTrapAck_Object = MibScalar
diagCompleteTrapAck = _DiagCompleteTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 7, 9),
    _DiagCompleteTrapAck_Type()
)
diagCompleteTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diagCompleteTrapAck.setStatus("deprecated")
_DiagStartedTrapAckSource_Type = IpAddress
_DiagStartedTrapAckSource_Object = MibScalar
diagStartedTrapAckSource = _DiagStartedTrapAckSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 7, 10),
    _DiagStartedTrapAckSource_Type()
)
diagStartedTrapAckSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diagStartedTrapAckSource.setStatus("deprecated")
_DiagCompleteTrapAckSource_Type = IpAddress
_DiagCompleteTrapAckSource_Object = MibScalar
diagCompleteTrapAckSource = _DiagCompleteTrapAckSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 7, 11),
    _DiagCompleteTrapAckSource_Type()
)
diagCompleteTrapAckSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diagCompleteTrapAckSource.setStatus("deprecated")
_PolicyProvisioning_ObjectIdentity = ObjectIdentity
policyProvisioning = _PolicyProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8)
)


class _ActiveImgName_Type(DisplayString):
    """Custom type activeImgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ActiveImgName_Type.__name__ = "DisplayString"
_ActiveImgName_Object = MibScalar
activeImgName = _ActiveImgName_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 1),
    _ActiveImgName_Type()
)
activeImgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeImgName.setStatus("current")


class _ActiveImgPidSideAFilename_Type(DisplayString):
    """Custom type activeImgPidSideAFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ActiveImgPidSideAFilename_Type.__name__ = "DisplayString"
_ActiveImgPidSideAFilename_Object = MibScalar
activeImgPidSideAFilename = _ActiveImgPidSideAFilename_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 2),
    _ActiveImgPidSideAFilename_Type()
)
activeImgPidSideAFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeImgPidSideAFilename.setStatus("deprecated")


class _ActiveImgPidSideBFilename_Type(DisplayString):
    """Custom type activeImgPidSideBFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ActiveImgPidSideBFilename_Type.__name__ = "DisplayString"
_ActiveImgPidSideBFilename_Object = MibScalar
activeImgPidSideBFilename = _ActiveImgPidSideBFilename_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 3),
    _ActiveImgPidSideBFilename_Type()
)
activeImgPidSideBFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeImgPidSideBFilename.setStatus("deprecated")
_ActiveImgDwnldTimeStamp_Type = DateAndTime
_ActiveImgDwnldTimeStamp_Object = MibScalar
activeImgDwnldTimeStamp = _ActiveImgDwnldTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 4),
    _ActiveImgDwnldTimeStamp_Type()
)
activeImgDwnldTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeImgDwnldTimeStamp.setStatus("current")
_ActiveImgBuildStartTimeStamp_Type = DateAndTime
_ActiveImgBuildStartTimeStamp_Object = MibScalar
activeImgBuildStartTimeStamp = _ActiveImgBuildStartTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 5),
    _ActiveImgBuildStartTimeStamp_Type()
)
activeImgBuildStartTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeImgBuildStartTimeStamp.setStatus("deprecated")
_ActiveImgBuildCompleteTimeStamp_Type = DateAndTime
_ActiveImgBuildCompleteTimeStamp_Object = MibScalar
activeImgBuildCompleteTimeStamp = _ActiveImgBuildCompleteTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 6),
    _ActiveImgBuildCompleteTimeStamp_Type()
)
activeImgBuildCompleteTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeImgBuildCompleteTimeStamp.setStatus("deprecated")
_ActiveImgActivatedTimeStamp_Type = DateAndTime
_ActiveImgActivatedTimeStamp_Object = MibScalar
activeImgActivatedTimeStamp = _ActiveImgActivatedTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 7),
    _ActiveImgActivatedTimeStamp_Type()
)
activeImgActivatedTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeImgActivatedTimeStamp.setStatus("current")


class _CommitImgName_Type(DisplayString):
    """Custom type commitImgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CommitImgName_Type.__name__ = "DisplayString"
_CommitImgName_Object = MibScalar
commitImgName = _CommitImgName_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 8),
    _CommitImgName_Type()
)
commitImgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commitImgName.setStatus("current")
_CommitImgDwnldTimeStamp_Type = DateAndTime
_CommitImgDwnldTimeStamp_Object = MibScalar
commitImgDwnldTimeStamp = _CommitImgDwnldTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 9),
    _CommitImgDwnldTimeStamp_Type()
)
commitImgDwnldTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commitImgDwnldTimeStamp.setStatus("deprecated")
_CommitImgBuildStartTimeStamp_Type = DateAndTime
_CommitImgBuildStartTimeStamp_Object = MibScalar
commitImgBuildStartTimeStamp = _CommitImgBuildStartTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 10),
    _CommitImgBuildStartTimeStamp_Type()
)
commitImgBuildStartTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commitImgBuildStartTimeStamp.setStatus("deprecated")
_CommitImgBuildCompleteTimeStamp_Type = DateAndTime
_CommitImgBuildCompleteTimeStamp_Object = MibScalar
commitImgBuildCompleteTimeStamp = _CommitImgBuildCompleteTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 11),
    _CommitImgBuildCompleteTimeStamp_Type()
)
commitImgBuildCompleteTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commitImgBuildCompleteTimeStamp.setStatus("deprecated")
_CommitImgActivatedTimeStamp_Type = DateAndTime
_CommitImgActivatedTimeStamp_Object = MibScalar
commitImgActivatedTimeStamp = _CommitImgActivatedTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 12),
    _CommitImgActivatedTimeStamp_Type()
)
commitImgActivatedTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commitImgActivatedTimeStamp.setStatus("current")
_CommitImgTimeStamp_Type = DateAndTime
_CommitImgTimeStamp_Object = MibScalar
commitImgTimeStamp = _CommitImgTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 13),
    _CommitImgTimeStamp_Type()
)
commitImgTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commitImgTimeStamp.setStatus("current")


class _NextImgName_Type(DisplayString):
    """Custom type nextImgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NextImgName_Type.__name__ = "DisplayString"
_NextImgName_Object = MibScalar
nextImgName = _NextImgName_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 16),
    _NextImgName_Type()
)
nextImgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextImgName.setStatus("deprecated")


class _NextImgState_Type(Integer32):
    """Custom type nextImgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("buildComplete", 2),
          ("buildInProgress", 1),
          ("cleared", 0))
    )


_NextImgState_Type.__name__ = "Integer32"
_NextImgState_Object = MibScalar
nextImgState = _NextImgState_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 17),
    _NextImgState_Type()
)
nextImgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextImgState.setStatus("deprecated")
_NextImgDwnldTimeStamp_Type = DateAndTime
_NextImgDwnldTimeStamp_Object = MibScalar
nextImgDwnldTimeStamp = _NextImgDwnldTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 18),
    _NextImgDwnldTimeStamp_Type()
)
nextImgDwnldTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextImgDwnldTimeStamp.setStatus("deprecated")
_NextImgBuildStartTimeStamp_Type = DateAndTime
_NextImgBuildStartTimeStamp_Object = MibScalar
nextImgBuildStartTimeStamp = _NextImgBuildStartTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 19),
    _NextImgBuildStartTimeStamp_Type()
)
nextImgBuildStartTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextImgBuildStartTimeStamp.setStatus("deprecated")
_NextImgBuildCompleteTimeStamp_Type = DateAndTime
_NextImgBuildCompleteTimeStamp_Object = MibScalar
nextImgBuildCompleteTimeStamp = _NextImgBuildCompleteTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 20),
    _NextImgBuildCompleteTimeStamp_Type()
)
nextImgBuildCompleteTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextImgBuildCompleteTimeStamp.setStatus("deprecated")


class _NewActiveImgTrapAck_Type(Integer32):
    """Custom type newActiveImgTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("notAck", 0))
    )


_NewActiveImgTrapAck_Type.__name__ = "Integer32"
_NewActiveImgTrapAck_Object = MibScalar
newActiveImgTrapAck = _NewActiveImgTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 24),
    _NewActiveImgTrapAck_Type()
)
newActiveImgTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newActiveImgTrapAck.setStatus("current")


class _NewCommittedImgTrapAck_Type(Integer32):
    """Custom type newCommittedImgTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("notAck", 0))
    )


_NewCommittedImgTrapAck_Type.__name__ = "Integer32"
_NewCommittedImgTrapAck_Object = MibScalar
newCommittedImgTrapAck = _NewCommittedImgTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 25),
    _NewCommittedImgTrapAck_Type()
)
newCommittedImgTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newCommittedImgTrapAck.setStatus("current")


class _BuildStartedTrapAck_Type(Integer32):
    """Custom type buildStartedTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("notAck", 0))
    )


_BuildStartedTrapAck_Type.__name__ = "Integer32"
_BuildStartedTrapAck_Object = MibScalar
buildStartedTrapAck = _BuildStartedTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 26),
    _BuildStartedTrapAck_Type()
)
buildStartedTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buildStartedTrapAck.setStatus("deprecated")


class _BuildCompleteTrapAck_Type(Integer32):
    """Custom type buildCompleteTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("notAck", 0))
    )


_BuildCompleteTrapAck_Type.__name__ = "Integer32"
_BuildCompleteTrapAck_Object = MibScalar
buildCompleteTrapAck = _BuildCompleteTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 27),
    _BuildCompleteTrapAck_Type()
)
buildCompleteTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buildCompleteTrapAck.setStatus("deprecated")


class _NewNextTrapAck_Type(Integer32):
    """Custom type newNextTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("notAck", 0))
    )


_NewNextTrapAck_Type.__name__ = "Integer32"
_NewNextTrapAck_Object = MibScalar
newNextTrapAck = _NewNextTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 28),
    _NewNextTrapAck_Type()
)
newNextTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newNextTrapAck.setStatus("deprecated")
_NewActiveImgTrapAckSource_Type = IpAddress
_NewActiveImgTrapAckSource_Object = MibScalar
newActiveImgTrapAckSource = _NewActiveImgTrapAckSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 29),
    _NewActiveImgTrapAckSource_Type()
)
newActiveImgTrapAckSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newActiveImgTrapAckSource.setStatus("current")
_NewCommittedImgTrapAckSource_Type = IpAddress
_NewCommittedImgTrapAckSource_Object = MibScalar
newCommittedImgTrapAckSource = _NewCommittedImgTrapAckSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 30),
    _NewCommittedImgTrapAckSource_Type()
)
newCommittedImgTrapAckSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newCommittedImgTrapAckSource.setStatus("current")
_BuildStartedTrapAckSource_Type = IpAddress
_BuildStartedTrapAckSource_Object = MibScalar
buildStartedTrapAckSource = _BuildStartedTrapAckSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 31),
    _BuildStartedTrapAckSource_Type()
)
buildStartedTrapAckSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buildStartedTrapAckSource.setStatus("deprecated")
_BuildCompleteTrapAckSource_Type = IpAddress
_BuildCompleteTrapAckSource_Object = MibScalar
buildCompleteTrapAckSource = _BuildCompleteTrapAckSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 32),
    _BuildCompleteTrapAckSource_Type()
)
buildCompleteTrapAckSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buildCompleteTrapAckSource.setStatus("deprecated")
_NewNextTrapAckSource_Type = IpAddress
_NewNextTrapAckSource_Object = MibScalar
newNextTrapAckSource = _NewNextTrapAckSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 33),
    _NewNextTrapAckSource_Type()
)
newNextTrapAckSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newNextTrapAckSource.setStatus("deprecated")
_NCiteStaticRoutes_ObjectIdentity = ObjectIdentity
nCiteStaticRoutes = _NCiteStaticRoutes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 9)
)
_StaticRoutesTable_Object = MibTable
staticRoutesTable = _StaticRoutesTable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    staticRoutesTable.setStatus("current")
_StaticRoutesEntry_Object = MibTableRow
staticRoutesEntry = _StaticRoutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 9, 1, 1)
)
staticRoutesEntry.setIndexNames(
    (0, "Netrake-MIB", "staticRouteDest"),
    (0, "Netrake-MIB", "staticRouteNextHop"),
    (0, "Netrake-MIB", "staticRouteNetMask"),
)
if mibBuilder.loadTexts:
    staticRoutesEntry.setStatus("current")
_StaticRouteDest_Type = IpAddress
_StaticRouteDest_Object = MibTableColumn
staticRouteDest = _StaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 9, 1, 1, 1),
    _StaticRouteDest_Type()
)
staticRouteDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteDest.setStatus("current")
_StaticRouteNextHop_Type = IpAddress
_StaticRouteNextHop_Object = MibTableColumn
staticRouteNextHop = _StaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 9, 1, 1, 2),
    _StaticRouteNextHop_Type()
)
staticRouteNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteNextHop.setStatus("current")


class _StaticRouteNetMask_Type(IpAddress):
    """Custom type staticRouteNetMask based on IpAddress"""
    defaultHexValue = "00000000"


_StaticRouteNetMask_Object = MibTableColumn
staticRouteNetMask = _StaticRouteNetMask_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 9, 1, 1, 3),
    _StaticRouteNetMask_Type()
)
staticRouteNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteNetMask.setStatus("current")


class _StaticRouteIngressVlanTag_Type(Integer32):
    """Custom type staticRouteIngressVlanTag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_StaticRouteIngressVlanTag_Type.__name__ = "Integer32"
_StaticRouteIngressVlanTag_Object = MibTableColumn
staticRouteIngressVlanTag = _StaticRouteIngressVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 9, 1, 1, 4),
    _StaticRouteIngressVlanTag_Type()
)
staticRouteIngressVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteIngressVlanTag.setStatus("deprecated")


class _StaticRouteMetric1_Type(Integer32):
    """Custom type staticRouteMetric1 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_StaticRouteMetric1_Type.__name__ = "Integer32"
_StaticRouteMetric1_Object = MibTableColumn
staticRouteMetric1 = _StaticRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 9, 1, 1, 5),
    _StaticRouteMetric1_Type()
)
staticRouteMetric1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteMetric1.setStatus("current")


class _StaticRouteAdminState_Type(Integer32):
    """Custom type staticRouteAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_StaticRouteAdminState_Type.__name__ = "Integer32"
_StaticRouteAdminState_Object = MibTableColumn
staticRouteAdminState = _StaticRouteAdminState_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 9, 1, 1, 6),
    _StaticRouteAdminState_Type()
)
staticRouteAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteAdminState.setStatus("current")


class _StaticRouteIngressProtocol_Type(Integer32):
    """Custom type staticRouteIngressProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("general", 0),
          ("vlan", 1))
    )


_StaticRouteIngressProtocol_Type.__name__ = "Integer32"
_StaticRouteIngressProtocol_Object = MibTableColumn
staticRouteIngressProtocol = _StaticRouteIngressProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 9, 1, 1, 7),
    _StaticRouteIngressProtocol_Type()
)
staticRouteIngressProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteIngressProtocol.setStatus("deprecated")
_StaticRouteOperState_Type = DisplayString
_StaticRouteOperState_Object = MibTableColumn
staticRouteOperState = _StaticRouteOperState_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 9, 1, 1, 8),
    _StaticRouteOperState_Type()
)
staticRouteOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRouteOperState.setStatus("current")


class _StaticRouteType_Type(Integer32):
    """Custom type staticRouteType based on Integer32"""
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
        *(("dcHostRoute", 5),
          ("dcNetRoute", 6),
          ("defaultRoute", 3),
          ("discovered", 2),
          ("mgmtRoute", 4),
          ("userDefined", 1))
    )


_StaticRouteType_Type.__name__ = "Integer32"
_StaticRouteType_Object = MibTableColumn
staticRouteType = _StaticRouteType_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 9, 1, 1, 9),
    _StaticRouteType_Type()
)
staticRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRouteType.setStatus("current")
_StaticRouteRowStatus_Type = RowStatus
_StaticRouteRowStatus_Object = MibTableColumn
staticRouteRowStatus = _StaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 9, 1, 1, 10),
    _StaticRouteRowStatus_Type()
)
staticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticRouteRowStatus.setStatus("current")


class _StaticRouteVrdTag_Type(Integer32):
    """Custom type staticRouteVrdTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_StaticRouteVrdTag_Type.__name__ = "Integer32"
_StaticRouteVrdTag_Object = MibTableColumn
staticRouteVrdTag = _StaticRouteVrdTag_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 9, 1, 1, 11),
    _StaticRouteVrdTag_Type()
)
staticRouteVrdTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRouteVrdTag.setStatus("current")


class _StaticRouteEgressVlan_Type(Integer32):
    """Custom type staticRouteEgressVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_StaticRouteEgressVlan_Type.__name__ = "Integer32"
_StaticRouteEgressVlan_Object = MibTableColumn
staticRouteEgressVlan = _StaticRouteEgressVlan_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 9, 1, 1, 12),
    _StaticRouteEgressVlan_Type()
)
staticRouteEgressVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRouteEgressVlan.setStatus("current")


class _StaticRoutesRefreshNeeded_Type(Integer32):
    """Custom type staticRoutesRefreshNeeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("refresh", 1))
    )


_StaticRoutesRefreshNeeded_Type.__name__ = "Integer32"
_StaticRoutesRefreshNeeded_Object = MibScalar
staticRoutesRefreshNeeded = _StaticRoutesRefreshNeeded_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 9, 3),
    _StaticRoutesRefreshNeeded_Type()
)
staticRoutesRefreshNeeded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRoutesRefreshNeeded.setStatus("current")


class _StaticRouteChangeTrapAck_Type(Integer32):
    """Custom type staticRouteChangeTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("notAck", 0))
    )


_StaticRouteChangeTrapAck_Type.__name__ = "Integer32"
_StaticRouteChangeTrapAck_Object = MibScalar
staticRouteChangeTrapAck = _StaticRouteChangeTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 9, 5),
    _StaticRouteChangeTrapAck_Type()
)
staticRouteChangeTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteChangeTrapAck.setStatus("current")


class _StaticRouteRefreshTrapAck_Type(Integer32):
    """Custom type staticRouteRefreshTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("notAck", 0))
    )


_StaticRouteRefreshTrapAck_Type.__name__ = "Integer32"
_StaticRouteRefreshTrapAck_Object = MibScalar
staticRouteRefreshTrapAck = _StaticRouteRefreshTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 9, 6),
    _StaticRouteRefreshTrapAck_Type()
)
staticRouteRefreshTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteRefreshTrapAck.setStatus("current")
_StaticRouteChangeTrapAckSource_Type = IpAddress
_StaticRouteChangeTrapAckSource_Object = MibScalar
staticRouteChangeTrapAckSource = _StaticRouteChangeTrapAckSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 9, 7),
    _StaticRouteChangeTrapAckSource_Type()
)
staticRouteChangeTrapAckSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteChangeTrapAckSource.setStatus("current")
_StaticRouteRefreshTrapAckSource_Type = IpAddress
_StaticRouteRefreshTrapAckSource_Object = MibScalar
staticRouteRefreshTrapAckSource = _StaticRouteRefreshTrapAckSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 9, 8),
    _StaticRouteRefreshTrapAckSource_Type()
)
staticRouteRefreshTrapAckSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteRefreshTrapAckSource.setStatus("current")
_NCiteArpConfig_ObjectIdentity = ObjectIdentity
nCiteArpConfig = _NCiteArpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 10)
)


class _ArpVerifTimerRetryCount_Type(Integer32):
    """Custom type arpVerifTimerRetryCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_ArpVerifTimerRetryCount_Type.__name__ = "Integer32"
_ArpVerifTimerRetryCount_Object = MibScalar
arpVerifTimerRetryCount = _ArpVerifTimerRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 10, 1),
    _ArpVerifTimerRetryCount_Type()
)
arpVerifTimerRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpVerifTimerRetryCount.setStatus("current")
_ArpNextHopIP_Type = IpAddress
_ArpNextHopIP_Object = MibScalar
arpNextHopIP = _ArpNextHopIP_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 10, 2),
    _ArpNextHopIP_Type()
)
arpNextHopIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpNextHopIP.setStatus("current")
_ArpMacAddr_Type = DisplayString
_ArpMacAddr_Object = MibScalar
arpMacAddr = _ArpMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 10, 3),
    _ArpMacAddr_Type()
)
arpMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpMacAddr.setStatus("current")


class _ArpRefreshNeeded_Type(Integer32):
    """Custom type arpRefreshNeeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_ArpRefreshNeeded_Type.__name__ = "Integer32"
_ArpRefreshNeeded_Object = MibScalar
arpRefreshNeeded = _ArpRefreshNeeded_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 10, 4),
    _ArpRefreshNeeded_Type()
)
arpRefreshNeeded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpRefreshNeeded.setStatus("current")


class _ArpRefreshTrapAck_Type(Integer32):
    """Custom type arpRefreshTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("notAck", 0))
    )


_ArpRefreshTrapAck_Type.__name__ = "Integer32"
_ArpRefreshTrapAck_Object = MibScalar
arpRefreshTrapAck = _ArpRefreshTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 10, 6),
    _ArpRefreshTrapAck_Type()
)
arpRefreshTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpRefreshTrapAck.setStatus("current")


class _ArpUpdateMacTrapAck_Type(Integer32):
    """Custom type arpUpdateMacTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("noAck", 0))
    )


_ArpUpdateMacTrapAck_Type.__name__ = "Integer32"
_ArpUpdateMacTrapAck_Object = MibScalar
arpUpdateMacTrapAck = _ArpUpdateMacTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 10, 8),
    _ArpUpdateMacTrapAck_Type()
)
arpUpdateMacTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpUpdateMacTrapAck.setStatus("current")


class _ArpTrapOper_Type(Integer32):
    """Custom type arpTrapOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("addUpdate", 0),
          ("delete", 1))
    )


_ArpTrapOper_Type.__name__ = "Integer32"
_ArpTrapOper_Object = MibScalar
arpTrapOper = _ArpTrapOper_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 10, 9),
    _ArpTrapOper_Type()
)
arpTrapOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpTrapOper.setStatus("current")


class _ArpOperTimerFreq_Type(Integer32):
    """Custom type arpOperTimerFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_ArpOperTimerFreq_Type.__name__ = "Integer32"
_ArpOperTimerFreq_Object = MibScalar
arpOperTimerFreq = _ArpOperTimerFreq_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 10, 10),
    _ArpOperTimerFreq_Type()
)
arpOperTimerFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpOperTimerFreq.setStatus("current")


class _ArpOperTimerRetryCount_Type(Integer32):
    """Custom type arpOperTimerRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_ArpOperTimerRetryCount_Type.__name__ = "Integer32"
_ArpOperTimerRetryCount_Object = MibScalar
arpOperTimerRetryCount = _ArpOperTimerRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 10, 11),
    _ArpOperTimerRetryCount_Type()
)
arpOperTimerRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpOperTimerRetryCount.setStatus("current")


class _ArpVerifTimerChangeTrapAck_Type(Integer32):
    """Custom type arpVerifTimerChangeTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("default", 0))
    )


_ArpVerifTimerChangeTrapAck_Type.__name__ = "Integer32"
_ArpVerifTimerChangeTrapAck_Object = MibScalar
arpVerifTimerChangeTrapAck = _ArpVerifTimerChangeTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 10, 13),
    _ArpVerifTimerChangeTrapAck_Type()
)
arpVerifTimerChangeTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpVerifTimerChangeTrapAck.setStatus("current")


class _ArpOperTimerChangeTrapAck_Type(Integer32):
    """Custom type arpOperTimerChangeTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("default", 0))
    )


_ArpOperTimerChangeTrapAck_Type.__name__ = "Integer32"
_ArpOperTimerChangeTrapAck_Object = MibScalar
arpOperTimerChangeTrapAck = _ArpOperTimerChangeTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 10, 15),
    _ArpOperTimerChangeTrapAck_Type()
)
arpOperTimerChangeTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpOperTimerChangeTrapAck.setStatus("current")
_ArpRefreshTrapAckSource_Type = IpAddress
_ArpRefreshTrapAckSource_Object = MibScalar
arpRefreshTrapAckSource = _ArpRefreshTrapAckSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 10, 16),
    _ArpRefreshTrapAckSource_Type()
)
arpRefreshTrapAckSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpRefreshTrapAckSource.setStatus("current")
_ArpUpdateMacTrapAckSource_Type = IpAddress
_ArpUpdateMacTrapAckSource_Object = MibScalar
arpUpdateMacTrapAckSource = _ArpUpdateMacTrapAckSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 10, 17),
    _ArpUpdateMacTrapAckSource_Type()
)
arpUpdateMacTrapAckSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpUpdateMacTrapAckSource.setStatus("current")
_ArpVerifTimerChangeTrapAckSource_Type = IpAddress
_ArpVerifTimerChangeTrapAckSource_Object = MibScalar
arpVerifTimerChangeTrapAckSource = _ArpVerifTimerChangeTrapAckSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 10, 18),
    _ArpVerifTimerChangeTrapAckSource_Type()
)
arpVerifTimerChangeTrapAckSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpVerifTimerChangeTrapAckSource.setStatus("current")
_ArpOperTimerChangeTrapAckSource_Type = IpAddress
_ArpOperTimerChangeTrapAckSource_Object = MibScalar
arpOperTimerChangeTrapAckSource = _ArpOperTimerChangeTrapAckSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 10, 19),
    _ArpOperTimerChangeTrapAckSource_Type()
)
arpOperTimerChangeTrapAckSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpOperTimerChangeTrapAckSource.setStatus("current")
_IpPortConfig_ObjectIdentity = ObjectIdentity
ipPortConfig = _IpPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 11)
)
_IpPortConfigTable_Object = MibTable
ipPortConfigTable = _IpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    ipPortConfigTable.setStatus("current")
_IpPortConfigEntry_Object = MibTableRow
ipPortConfigEntry = _IpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 11, 1, 1)
)
ipPortConfigEntry.setIndexNames(
    (0, "Netrake-MIB", "ipPortConfigSlotNum"),
    (0, "Netrake-MIB", "ipPortConfigPortNum"),
    (0, "Netrake-MIB", "ipPortConfigIpAddr"),
)
if mibBuilder.loadTexts:
    ipPortConfigEntry.setStatus("current")


class _IpPortConfigSlotNum_Type(Integer32):
    """Custom type ipPortConfigSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_IpPortConfigSlotNum_Type.__name__ = "Integer32"
_IpPortConfigSlotNum_Object = MibTableColumn
ipPortConfigSlotNum = _IpPortConfigSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 11, 1, 1, 1),
    _IpPortConfigSlotNum_Type()
)
ipPortConfigSlotNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPortConfigSlotNum.setStatus("current")


class _IpPortConfigPortNum_Type(Integer32):
    """Custom type ipPortConfigPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_IpPortConfigPortNum_Type.__name__ = "Integer32"
_IpPortConfigPortNum_Object = MibTableColumn
ipPortConfigPortNum = _IpPortConfigPortNum_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 11, 1, 1, 2),
    _IpPortConfigPortNum_Type()
)
ipPortConfigPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPortConfigPortNum.setStatus("current")
_IpPortConfigIpAddr_Type = IpAddress
_IpPortConfigIpAddr_Object = MibTableColumn
ipPortConfigIpAddr = _IpPortConfigIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 11, 1, 1, 3),
    _IpPortConfigIpAddr_Type()
)
ipPortConfigIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPortConfigIpAddr.setStatus("current")


class _IpPortVlanTag_Type(Integer32):
    """Custom type ipPortVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4097),
    )


_IpPortVlanTag_Type.__name__ = "Integer32"
_IpPortVlanTag_Object = MibTableColumn
ipPortVlanTag = _IpPortVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 11, 1, 1, 4),
    _IpPortVlanTag_Type()
)
ipPortVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPortVlanTag.setStatus("current")
_IpPortConfigNetMask_Type = IpAddress
_IpPortConfigNetMask_Object = MibTableColumn
ipPortConfigNetMask = _IpPortConfigNetMask_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 11, 1, 1, 5),
    _IpPortConfigNetMask_Type()
)
ipPortConfigNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPortConfigNetMask.setStatus("current")


class _IpPortConfigAdminState_Type(Integer32):
    """Custom type ipPortConfigAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_IpPortConfigAdminState_Type.__name__ = "Integer32"
_IpPortConfigAdminState_Object = MibTableColumn
ipPortConfigAdminState = _IpPortConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 11, 1, 1, 6),
    _IpPortConfigAdminState_Type()
)
ipPortConfigAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPortConfigAdminState.setStatus("current")


class _IpPortConfigOperState_Type(Integer32):
    """Custom type ipPortConfigOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_IpPortConfigOperState_Type.__name__ = "Integer32"
_IpPortConfigOperState_Object = MibTableColumn
ipPortConfigOperState = _IpPortConfigOperState_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 11, 1, 1, 7),
    _IpPortConfigOperState_Type()
)
ipPortConfigOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPortConfigOperState.setStatus("current")
_IpPortRowStatus_Type = RowStatus
_IpPortRowStatus_Object = MibTableColumn
ipPortRowStatus = _IpPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 11, 1, 1, 8),
    _IpPortRowStatus_Type()
)
ipPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipPortRowStatus.setStatus("current")


class _IpPortVrdTag_Type(Integer32):
    """Custom type ipPortVrdTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_IpPortVrdTag_Type.__name__ = "Integer32"
_IpPortVrdTag_Object = MibTableColumn
ipPortVrdTag = _IpPortVrdTag_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 11, 1, 1, 9),
    _IpPortVrdTag_Type()
)
ipPortVrdTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPortVrdTag.setStatus("current")


class _IpPortConfigChangeTrapAck_Type(Integer32):
    """Custom type ipPortConfigChangeTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("notAck", 0))
    )


_IpPortConfigChangeTrapAck_Type.__name__ = "Integer32"
_IpPortConfigChangeTrapAck_Object = MibScalar
ipPortConfigChangeTrapAck = _IpPortConfigChangeTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 11, 3),
    _IpPortConfigChangeTrapAck_Type()
)
ipPortConfigChangeTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPortConfigChangeTrapAck.setStatus("current")
_IpPortPlaceHolder_Type = Integer32
_IpPortPlaceHolder_Object = MibScalar
ipPortPlaceHolder = _IpPortPlaceHolder_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 11, 4),
    _IpPortPlaceHolder_Type()
)
ipPortPlaceHolder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPortPlaceHolder.setStatus("current")
_IpPortRefreshOpStates_Type = Integer32
_IpPortRefreshOpStates_Object = MibScalar
ipPortRefreshOpStates = _IpPortRefreshOpStates_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 11, 5),
    _IpPortRefreshOpStates_Type()
)
ipPortRefreshOpStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPortRefreshOpStates.setStatus("current")


class _IpPortRefreshTrapAck_Type(Integer32):
    """Custom type ipPortRefreshTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("noAck", 0))
    )


_IpPortRefreshTrapAck_Type.__name__ = "Integer32"
_IpPortRefreshTrapAck_Object = MibScalar
ipPortRefreshTrapAck = _IpPortRefreshTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 11, 7),
    _IpPortRefreshTrapAck_Type()
)
ipPortRefreshTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPortRefreshTrapAck.setStatus("current")
_IpPortAutoNegTable_Object = MibTable
ipPortAutoNegTable = _IpPortAutoNegTable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 11, 8)
)
if mibBuilder.loadTexts:
    ipPortAutoNegTable.setStatus("current")
_IpPortAutoNegEntry_Object = MibTableRow
ipPortAutoNegEntry = _IpPortAutoNegEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 11, 8, 1)
)
ipPortAutoNegEntry.setIndexNames(
    (0, "Netrake-MIB", "ipPortAutoNegSlotNum"),
    (0, "Netrake-MIB", "ipPortAutoNegPortNum"),
)
if mibBuilder.loadTexts:
    ipPortAutoNegEntry.setStatus("current")
_IpPortAutoNegSlotNum_Type = Integer32
_IpPortAutoNegSlotNum_Object = MibTableColumn
ipPortAutoNegSlotNum = _IpPortAutoNegSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 11, 8, 1, 1),
    _IpPortAutoNegSlotNum_Type()
)
ipPortAutoNegSlotNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPortAutoNegSlotNum.setStatus("current")
_IpPortAutoNegPortNum_Type = Integer32
_IpPortAutoNegPortNum_Object = MibTableColumn
ipPortAutoNegPortNum = _IpPortAutoNegPortNum_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 11, 8, 1, 2),
    _IpPortAutoNegPortNum_Type()
)
ipPortAutoNegPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPortAutoNegPortNum.setStatus("current")


class _IpPortAutoNegFlag_Type(Integer32):
    """Custom type ipPortAutoNegFlag based on Integer32"""
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


_IpPortAutoNegFlag_Type.__name__ = "Integer32"
_IpPortAutoNegFlag_Object = MibTableColumn
ipPortAutoNegFlag = _IpPortAutoNegFlag_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 11, 8, 1, 3),
    _IpPortAutoNegFlag_Type()
)
ipPortAutoNegFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPortAutoNegFlag.setStatus("current")


class _IpPortAutoNegChangeTrapAck_Type(Integer32):
    """Custom type ipPortAutoNegChangeTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("default", 0))
    )


_IpPortAutoNegChangeTrapAck_Type.__name__ = "Integer32"
_IpPortAutoNegChangeTrapAck_Object = MibScalar
ipPortAutoNegChangeTrapAck = _IpPortAutoNegChangeTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 11, 10),
    _IpPortAutoNegChangeTrapAck_Type()
)
ipPortAutoNegChangeTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPortAutoNegChangeTrapAck.setStatus("current")
_IpPortConfigChangeTrapAckSource_Type = IpAddress
_IpPortConfigChangeTrapAckSource_Object = MibScalar
ipPortConfigChangeTrapAckSource = _IpPortConfigChangeTrapAckSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 11, 11),
    _IpPortConfigChangeTrapAckSource_Type()
)
ipPortConfigChangeTrapAckSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPortConfigChangeTrapAckSource.setStatus("current")
_IpPortRefreshTrapAckSource_Type = IpAddress
_IpPortRefreshTrapAckSource_Object = MibScalar
ipPortRefreshTrapAckSource = _IpPortRefreshTrapAckSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 11, 12),
    _IpPortRefreshTrapAckSource_Type()
)
ipPortRefreshTrapAckSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPortRefreshTrapAckSource.setStatus("current")
_IpPortAutoNegChangeTrapAckSource_Type = IpAddress
_IpPortAutoNegChangeTrapAckSource_Object = MibScalar
ipPortAutoNegChangeTrapAckSource = _IpPortAutoNegChangeTrapAckSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 11, 13),
    _IpPortAutoNegChangeTrapAckSource_Type()
)
ipPortAutoNegChangeTrapAckSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPortAutoNegChangeTrapAckSource.setStatus("current")


class _NCiteOutSyncFlag_Type(Integer32):
    """Custom type nCiteOutSyncFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_NCiteOutSyncFlag_Type.__name__ = "Integer32"
_NCiteOutSyncFlag_Object = MibScalar
nCiteOutSyncFlag = _NCiteOutSyncFlag_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 12),
    _NCiteOutSyncFlag_Type()
)
nCiteOutSyncFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nCiteOutSyncFlag.setStatus("deprecated")


class _TrapAckEnable_Type(Integer32):
    """Custom type trapAckEnable based on Integer32"""
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


_TrapAckEnable_Type.__name__ = "Integer32"
_TrapAckEnable_Object = MibScalar
trapAckEnable = _TrapAckEnable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 13),
    _TrapAckEnable_Type()
)
trapAckEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapAckEnable.setStatus("current")


class _LinkUpTrapAck_Type(Integer32):
    """Custom type linkUpTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("notAck", 0))
    )


_LinkUpTrapAck_Type.__name__ = "Integer32"
_LinkUpTrapAck_Object = MibScalar
linkUpTrapAck = _LinkUpTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 14),
    _LinkUpTrapAck_Type()
)
linkUpTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkUpTrapAck.setStatus("current")


class _LinkDownTrapAck_Type(Integer32):
    """Custom type linkDownTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("notAck", 0))
    )


_LinkDownTrapAck_Type.__name__ = "Integer32"
_LinkDownTrapAck_Object = MibScalar
linkDownTrapAck = _LinkDownTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 15),
    _LinkDownTrapAck_Type()
)
linkDownTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkDownTrapAck.setStatus("current")
_NCiteNTA_ObjectIdentity = ObjectIdentity
nCiteNTA = _NCiteNTA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 16)
)
_NCiteNTATable_Object = MibTable
nCiteNTATable = _NCiteNTATable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 16, 1)
)
if mibBuilder.loadTexts:
    nCiteNTATable.setStatus("current")
_NCiteNTAEntry_Object = MibTableRow
nCiteNTAEntry = _NCiteNTAEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 16, 1, 1)
)
nCiteNTAEntry.setIndexNames(
    (0, "Netrake-MIB", "nCiteNTACustomerId"),
)
if mibBuilder.loadTexts:
    nCiteNTAEntry.setStatus("current")
_NCiteNTACustomerId_Type = Integer32
_NCiteNTACustomerId_Object = MibTableColumn
nCiteNTACustomerId = _NCiteNTACustomerId_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 16, 1, 1, 1),
    _NCiteNTACustomerId_Type()
)
nCiteNTACustomerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nCiteNTACustomerId.setStatus("current")


class _NCiteNTAStatus_Type(Integer32):
    """Custom type nCiteNTAStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 1),
          ("connected", 2),
          ("noNTSClient", 0))
    )


_NCiteNTAStatus_Type.__name__ = "Integer32"
_NCiteNTAStatus_Object = MibTableColumn
nCiteNTAStatus = _NCiteNTAStatus_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 16, 1, 1, 2),
    _NCiteNTAStatus_Type()
)
nCiteNTAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nCiteNTAStatus.setStatus("current")
_NCiteRogue_ObjectIdentity = ObjectIdentity
nCiteRogue = _NCiteRogue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17)
)
_EdrQuarantineListTable_Object = MibTable
edrQuarantineListTable = _EdrQuarantineListTable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 1)
)
if mibBuilder.loadTexts:
    edrQuarantineListTable.setStatus("current")
_EdrQuarantineListEntry_Object = MibTableRow
edrQuarantineListEntry = _EdrQuarantineListEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 1, 1)
)
edrQuarantineListEntry.setIndexNames(
    (0, "Netrake-MIB", "erdQLUniqueId"),
)
if mibBuilder.loadTexts:
    edrQuarantineListEntry.setStatus("current")
_ErdQLUniqueId_Type = Integer32
_ErdQLUniqueId_Object = MibTableColumn
erdQLUniqueId = _ErdQLUniqueId_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 1, 1, 1),
    _ErdQLUniqueId_Type()
)
erdQLUniqueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erdQLUniqueId.setStatus("current")


class _EdrQLCallId_Type(DisplayString):
    """Custom type edrQLCallId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EdrQLCallId_Type.__name__ = "DisplayString"
_EdrQLCallId_Object = MibTableColumn
edrQLCallId = _EdrQLCallId_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 1, 1, 2),
    _EdrQLCallId_Type()
)
edrQLCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edrQLCallId.setStatus("current")
_EdrQLTimestamp_Type = DateAndTime
_EdrQLTimestamp_Object = MibTableColumn
edrQLTimestamp = _EdrQLTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 1, 1, 3),
    _EdrQLTimestamp_Type()
)
edrQLTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edrQLTimestamp.setStatus("current")
_EdrQLFrom_Type = DisplayString
_EdrQLFrom_Object = MibTableColumn
edrQLFrom = _EdrQLFrom_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 1, 1, 4),
    _EdrQLFrom_Type()
)
edrQLFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edrQLFrom.setStatus("current")
_EdrQLTo_Type = DisplayString
_EdrQLTo_Object = MibTableColumn
edrQLTo = _EdrQLTo_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 1, 1, 5),
    _EdrQLTo_Type()
)
edrQLTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edrQLTo.setStatus("current")
_EdrQLRequestURI_Type = DisplayString
_EdrQLRequestURI_Object = MibTableColumn
edrQLRequestURI = _EdrQLRequestURI_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 1, 1, 6),
    _EdrQLRequestURI_Type()
)
edrQLRequestURI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edrQLRequestURI.setStatus("current")
_EdrQLSrcMediaIpPort_Type = DisplayString
_EdrQLSrcMediaIpPort_Object = MibTableColumn
edrQLSrcMediaIpPort = _EdrQLSrcMediaIpPort_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 1, 1, 7),
    _EdrQLSrcMediaIpPort_Type()
)
edrQLSrcMediaIpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edrQLSrcMediaIpPort.setStatus("current")
_EdrQLDestMediaAnchorIpPort_Type = DisplayString
_EdrQLDestMediaAnchorIpPort_Object = MibTableColumn
edrQLDestMediaAnchorIpPort = _EdrQLDestMediaAnchorIpPort_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 1, 1, 8),
    _EdrQLDestMediaAnchorIpPort_Type()
)
edrQLDestMediaAnchorIpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edrQLDestMediaAnchorIpPort.setStatus("current")
_EdrQLDestMediaIpPort_Type = DisplayString
_EdrQLDestMediaIpPort_Object = MibTableColumn
edrQLDestMediaIpPort = _EdrQLDestMediaIpPort_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 1, 1, 9),
    _EdrQLDestMediaIpPort_Type()
)
edrQLDestMediaIpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edrQLDestMediaIpPort.setStatus("current")


class _EdrQLRogueStatus_Type(DisplayString):
    """Custom type edrQLRogueStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EdrQLRogueStatus_Type.__name__ = "DisplayString"
_EdrQLRogueStatus_Object = MibTableColumn
edrQLRogueStatus = _EdrQLRogueStatus_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 1, 1, 10),
    _EdrQLRogueStatus_Type()
)
edrQLRogueStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edrQLRogueStatus.setStatus("current")


class _EdrQLPerformGarbageCollection_Type(Integer32):
    """Custom type edrQLPerformGarbageCollection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("start", 1))
    )


_EdrQLPerformGarbageCollection_Type.__name__ = "Integer32"
_EdrQLPerformGarbageCollection_Object = MibTableColumn
edrQLPerformGarbageCollection = _EdrQLPerformGarbageCollection_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 1, 1, 11),
    _EdrQLPerformGarbageCollection_Type()
)
edrQLPerformGarbageCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edrQLPerformGarbageCollection.setStatus("current")
_ErdQL2SrcMediaIpPort_Type = DisplayString
_ErdQL2SrcMediaIpPort_Object = MibTableColumn
erdQL2SrcMediaIpPort = _ErdQL2SrcMediaIpPort_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 1, 1, 12),
    _ErdQL2SrcMediaIpPort_Type()
)
erdQL2SrcMediaIpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erdQL2SrcMediaIpPort.setStatus("current")
_ErdQL2DestMediaAnchorIpPort_Type = DisplayString
_ErdQL2DestMediaAnchorIpPort_Object = MibTableColumn
erdQL2DestMediaAnchorIpPort = _ErdQL2DestMediaAnchorIpPort_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 1, 1, 13),
    _ErdQL2DestMediaAnchorIpPort_Type()
)
erdQL2DestMediaAnchorIpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erdQL2DestMediaAnchorIpPort.setStatus("current")
_ErdQL2DestMediaIpPort_Type = DisplayString
_ErdQL2DestMediaIpPort_Object = MibTableColumn
erdQL2DestMediaIpPort = _ErdQL2DestMediaIpPort_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 1, 1, 14),
    _ErdQL2DestMediaIpPort_Type()
)
erdQL2DestMediaIpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erdQL2DestMediaIpPort.setStatus("current")
_EdrGarbageCollectionState_Type = DisplayString
_EdrGarbageCollectionState_Object = MibScalar
edrGarbageCollectionState = _EdrGarbageCollectionState_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 2),
    _EdrGarbageCollectionState_Type()
)
edrGarbageCollectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edrGarbageCollectionState.setStatus("current")
_EdrLastGarbageCollection_Type = DateAndTime
_EdrLastGarbageCollection_Object = MibScalar
edrLastGarbageCollection = _EdrLastGarbageCollection_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 3),
    _EdrLastGarbageCollection_Type()
)
edrLastGarbageCollection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edrLastGarbageCollection.setStatus("current")
_EdrNextTrafficCheck_Type = DateAndTime
_EdrNextTrafficCheck_Object = MibScalar
edrNextTrafficCheck = _EdrNextTrafficCheck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 4),
    _EdrNextTrafficCheck_Type()
)
edrNextTrafficCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edrNextTrafficCheck.setStatus("current")


class _EdrPerformGarbageCollection_Type(Integer32):
    """Custom type edrPerformGarbageCollection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("start", 1))
    )


_EdrPerformGarbageCollection_Type.__name__ = "Integer32"
_EdrPerformGarbageCollection_Object = MibScalar
edrPerformGarbageCollection = _EdrPerformGarbageCollection_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 5),
    _EdrPerformGarbageCollection_Type()
)
edrPerformGarbageCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edrPerformGarbageCollection.setStatus("current")


class _EdrGarbageCollectionStatus_Type(Integer32):
    """Custom type edrGarbageCollectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("entryNotFound", 1),
          ("success", 0))
    )


_EdrGarbageCollectionStatus_Type.__name__ = "Integer32"
_EdrGarbageCollectionStatus_Object = MibScalar
edrGarbageCollectionStatus = _EdrGarbageCollectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 6),
    _EdrGarbageCollectionStatus_Type()
)
edrGarbageCollectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edrGarbageCollectionStatus.setStatus("current")


class _EdrGarbageCollectionCompleteTrapAck_Type(Integer32):
    """Custom type edrGarbageCollectionCompleteTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("notAck", 0))
    )


_EdrGarbageCollectionCompleteTrapAck_Type.__name__ = "Integer32"
_EdrGarbageCollectionCompleteTrapAck_Object = MibScalar
edrGarbageCollectionCompleteTrapAck = _EdrGarbageCollectionCompleteTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 8),
    _EdrGarbageCollectionCompleteTrapAck_Type()
)
edrGarbageCollectionCompleteTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edrGarbageCollectionCompleteTrapAck.setStatus("current")
_LrdTable_Object = MibTable
lrdTable = _LrdTable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 9)
)
if mibBuilder.loadTexts:
    lrdTable.setStatus("current")
_LrdEntry_Object = MibTableRow
lrdEntry = _LrdEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 9, 1)
)
lrdEntry.setIndexNames(
    (0, "Netrake-MIB", "lrdUniqueId"),
)
if mibBuilder.loadTexts:
    lrdEntry.setStatus("current")


class _LrdUniqueId_Type(Integer32):
    """Custom type lrdUniqueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_LrdUniqueId_Type.__name__ = "Integer32"
_LrdUniqueId_Object = MibTableColumn
lrdUniqueId = _LrdUniqueId_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 9, 1, 1),
    _LrdUniqueId_Type()
)
lrdUniqueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrdUniqueId.setStatus("current")
_LrdCallId_Type = DisplayString
_LrdCallId_Object = MibTableColumn
lrdCallId = _LrdCallId_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 9, 1, 2),
    _LrdCallId_Type()
)
lrdCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrdCallId.setStatus("current")
_LrdRequestURI_Type = DisplayString
_LrdRequestURI_Object = MibTableColumn
lrdRequestURI = _LrdRequestURI_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 9, 1, 3),
    _LrdRequestURI_Type()
)
lrdRequestURI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrdRequestURI.setStatus("current")
_LrdFrom_Type = DisplayString
_LrdFrom_Object = MibTableColumn
lrdFrom = _LrdFrom_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 9, 1, 4),
    _LrdFrom_Type()
)
lrdFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrdFrom.setStatus("current")
_LrdTo_Type = DisplayString
_LrdTo_Object = MibTableColumn
lrdTo = _LrdTo_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 9, 1, 5),
    _LrdTo_Type()
)
lrdTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrdTo.setStatus("current")
_LrdCallerState_Type = DisplayString
_LrdCallerState_Object = MibTableColumn
lrdCallerState = _LrdCallerState_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 9, 1, 6),
    _LrdCallerState_Type()
)
lrdCallerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrdCallerState.setStatus("current")
_LrdCallerMediaAnchorIPPort_Type = DisplayString
_LrdCallerMediaAnchorIPPort_Object = MibTableColumn
lrdCallerMediaAnchorIPPort = _LrdCallerMediaAnchorIPPort_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 9, 1, 7),
    _LrdCallerMediaAnchorIPPort_Type()
)
lrdCallerMediaAnchorIPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrdCallerMediaAnchorIPPort.setStatus("current")
_LrdCallerDestIPPort_Type = DisplayString
_LrdCallerDestIPPort_Object = MibTableColumn
lrdCallerDestIPPort = _LrdCallerDestIPPort_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 9, 1, 8),
    _LrdCallerDestIPPort_Type()
)
lrdCallerDestIPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrdCallerDestIPPort.setStatus("current")
_LrdCallerSourceIPPort1_Type = DisplayString
_LrdCallerSourceIPPort1_Object = MibTableColumn
lrdCallerSourceIPPort1 = _LrdCallerSourceIPPort1_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 9, 1, 9),
    _LrdCallerSourceIPPort1_Type()
)
lrdCallerSourceIPPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrdCallerSourceIPPort1.setStatus("current")
_LrdCallerSourceIPPort2_Type = DisplayString
_LrdCallerSourceIPPort2_Object = MibTableColumn
lrdCallerSourceIPPort2 = _LrdCallerSourceIPPort2_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 9, 1, 10),
    _LrdCallerSourceIPPort2_Type()
)
lrdCallerSourceIPPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrdCallerSourceIPPort2.setStatus("current")
_LrdCallerReason_Type = DisplayString
_LrdCallerReason_Object = MibTableColumn
lrdCallerReason = _LrdCallerReason_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 9, 1, 11),
    _LrdCallerReason_Type()
)
lrdCallerReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrdCallerReason.setStatus("current")
_LrdCallerTimeDetect_Type = DateAndTime
_LrdCallerTimeDetect_Object = MibTableColumn
lrdCallerTimeDetect = _LrdCallerTimeDetect_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 9, 1, 12),
    _LrdCallerTimeDetect_Type()
)
lrdCallerTimeDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrdCallerTimeDetect.setStatus("current")
_LrdCalleeState_Type = DisplayString
_LrdCalleeState_Object = MibTableColumn
lrdCalleeState = _LrdCalleeState_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 9, 1, 13),
    _LrdCalleeState_Type()
)
lrdCalleeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrdCalleeState.setStatus("current")
_LrdCalleeMediaAnchorIPPort_Type = DisplayString
_LrdCalleeMediaAnchorIPPort_Object = MibTableColumn
lrdCalleeMediaAnchorIPPort = _LrdCalleeMediaAnchorIPPort_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 9, 1, 14),
    _LrdCalleeMediaAnchorIPPort_Type()
)
lrdCalleeMediaAnchorIPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrdCalleeMediaAnchorIPPort.setStatus("current")
_LrdCalleeDestIPPort_Type = DisplayString
_LrdCalleeDestIPPort_Object = MibTableColumn
lrdCalleeDestIPPort = _LrdCalleeDestIPPort_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 9, 1, 15),
    _LrdCalleeDestIPPort_Type()
)
lrdCalleeDestIPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrdCalleeDestIPPort.setStatus("current")
_LrdCalleeSourceIPPort1_Type = DisplayString
_LrdCalleeSourceIPPort1_Object = MibTableColumn
lrdCalleeSourceIPPort1 = _LrdCalleeSourceIPPort1_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 9, 1, 16),
    _LrdCalleeSourceIPPort1_Type()
)
lrdCalleeSourceIPPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrdCalleeSourceIPPort1.setStatus("current")
_LrdCalleeSourceIPPort2_Type = DisplayString
_LrdCalleeSourceIPPort2_Object = MibTableColumn
lrdCalleeSourceIPPort2 = _LrdCalleeSourceIPPort2_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 9, 1, 17),
    _LrdCalleeSourceIPPort2_Type()
)
lrdCalleeSourceIPPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrdCalleeSourceIPPort2.setStatus("current")
_LrdCalleeReason_Type = DisplayString
_LrdCalleeReason_Object = MibTableColumn
lrdCalleeReason = _LrdCalleeReason_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 9, 1, 18),
    _LrdCalleeReason_Type()
)
lrdCalleeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrdCalleeReason.setStatus("current")
_LrdCalleeTimeDetect_Type = DisplayString
_LrdCalleeTimeDetect_Object = MibTableColumn
lrdCalleeTimeDetect = _LrdCalleeTimeDetect_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 9, 1, 19),
    _LrdCalleeTimeDetect_Type()
)
lrdCalleeTimeDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lrdCalleeTimeDetect.setStatus("current")
_EdrGarbageCollectionCompleteTrapAckSource_Type = IpAddress
_EdrGarbageCollectionCompleteTrapAckSource_Object = MibScalar
edrGarbageCollectionCompleteTrapAckSource = _EdrGarbageCollectionCompleteTrapAckSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 10),
    _EdrGarbageCollectionCompleteTrapAckSource_Type()
)
edrGarbageCollectionCompleteTrapAckSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edrGarbageCollectionCompleteTrapAckSource.setStatus("current")
_LicenseInfo_ObjectIdentity = ObjectIdentity
licenseInfo = _LicenseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 18)
)
_LicenseTable_Object = MibTable
licenseTable = _LicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 18, 1)
)
if mibBuilder.loadTexts:
    licenseTable.setStatus("current")
_LicenseEntry_Object = MibTableRow
licenseEntry = _LicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 18, 1, 1)
)
licenseEntry.setIndexNames(
    (0, "Netrake-MIB", "licenseIndex"),
)
if mibBuilder.loadTexts:
    licenseEntry.setStatus("current")
_LicenseIndex_Type = Integer32
_LicenseIndex_Object = MibTableColumn
licenseIndex = _LicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 18, 1, 1, 1),
    _LicenseIndex_Type()
)
licenseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseIndex.setStatus("current")


class _LicenseFeatureName_Type(Integer32):
    """Custom type licenseFeatureName based on Integer32"""
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
        *(("globalCac", 0),
          ("globalReg", 7),
          ("nts", 2),
          ("redundancy", 1),
          ("rogueDetect", 3),
          ("totalCust", 4),
          ("totalNtsCust", 5),
          ("totalVlanCust", 6))
    )


_LicenseFeatureName_Type.__name__ = "Integer32"
_LicenseFeatureName_Object = MibTableColumn
licenseFeatureName = _LicenseFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 18, 1, 1, 2),
    _LicenseFeatureName_Type()
)
licenseFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseFeatureName.setStatus("deprecated")


class _LicenseValue_Type(Integer32):
    """Custom type licenseValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_LicenseValue_Type.__name__ = "Integer32"
_LicenseValue_Object = MibTableColumn
licenseValue = _LicenseValue_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 18, 1, 1, 3),
    _LicenseValue_Type()
)
licenseValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseValue.setStatus("current")
_LicenseInstallDate_Type = DateAndTime
_LicenseInstallDate_Object = MibTableColumn
licenseInstallDate = _LicenseInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 18, 1, 1, 4),
    _LicenseInstallDate_Type()
)
licenseInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseInstallDate.setStatus("current")
_LicenseExpirationDate_Type = DateAndTime
_LicenseExpirationDate_Object = MibTableColumn
licenseExpirationDate = _LicenseExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 18, 1, 1, 5),
    _LicenseExpirationDate_Type()
)
licenseExpirationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseExpirationDate.setStatus("current")
_LicenseFeatureDisplayName_Type = DisplayString
_LicenseFeatureDisplayName_Object = MibTableColumn
licenseFeatureDisplayName = _LicenseFeatureDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 18, 1, 1, 6),
    _LicenseFeatureDisplayName_Type()
)
licenseFeatureDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseFeatureDisplayName.setStatus("current")
_LicenseFileName_Type = DisplayString
_LicenseFileName_Object = MibScalar
licenseFileName = _LicenseFileName_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 18, 2),
    _LicenseFileName_Type()
)
licenseFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseFileName.setStatus("current")


class _LicenseFileChangeTrapAck_Type(Integer32):
    """Custom type licenseFileChangeTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("notAck", 0))
    )


_LicenseFileChangeTrapAck_Type.__name__ = "Integer32"
_LicenseFileChangeTrapAck_Object = MibScalar
licenseFileChangeTrapAck = _LicenseFileChangeTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 18, 4),
    _LicenseFileChangeTrapAck_Type()
)
licenseFileChangeTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenseFileChangeTrapAck.setStatus("current")
_LicenseFileChangeTrapAckSource_Type = IpAddress
_LicenseFileChangeTrapAckSource_Object = MibScalar
licenseFileChangeTrapAckSource = _LicenseFileChangeTrapAckSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 18, 5),
    _LicenseFileChangeTrapAckSource_Type()
)
licenseFileChangeTrapAckSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenseFileChangeTrapAckSource.setStatus("current")
_NCiteRIPConfig_ObjectIdentity = ObjectIdentity
nCiteRIPConfig = _NCiteRIPConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 19)
)


class _NCiteRipState_Type(Integer32):
    """Custom type nCiteRipState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NCiteRipState_Type.__name__ = "Integer32"
_NCiteRipState_Object = MibScalar
nCiteRipState = _NCiteRipState_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 19, 1),
    _NCiteRipState_Type()
)
nCiteRipState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nCiteRipState.setStatus("current")
_NCiteRipPortConfigTable_Object = MibTable
nCiteRipPortConfigTable = _NCiteRipPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 19, 2)
)
if mibBuilder.loadTexts:
    nCiteRipPortConfigTable.setStatus("current")
_NCiteRipPortConfigEntry_Object = MibTableRow
nCiteRipPortConfigEntry = _NCiteRipPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 19, 2, 1)
)
nCiteRipPortConfigEntry.setIndexNames(
    (0, "Netrake-MIB", "nCiteRipPortSlotNum"),
    (0, "Netrake-MIB", "nCiteRipPortNum"),
)
if mibBuilder.loadTexts:
    nCiteRipPortConfigEntry.setStatus("current")
_NCiteRipPortSlotNum_Type = Integer32
_NCiteRipPortSlotNum_Object = MibTableColumn
nCiteRipPortSlotNum = _NCiteRipPortSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 19, 2, 1, 1),
    _NCiteRipPortSlotNum_Type()
)
nCiteRipPortSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nCiteRipPortSlotNum.setStatus("current")
_NCiteRipPortNum_Type = Integer32
_NCiteRipPortNum_Object = MibTableColumn
nCiteRipPortNum = _NCiteRipPortNum_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 19, 2, 1, 2),
    _NCiteRipPortNum_Type()
)
nCiteRipPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nCiteRipPortNum.setStatus("current")


class _NCiteRipPortPrimary_Type(Integer32):
    """Custom type nCiteRipPortPrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("primary", 1),
          ("secondary", 2))
    )


_NCiteRipPortPrimary_Type.__name__ = "Integer32"
_NCiteRipPortPrimary_Object = MibTableColumn
nCiteRipPortPrimary = _NCiteRipPortPrimary_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 19, 2, 1, 3),
    _NCiteRipPortPrimary_Type()
)
nCiteRipPortPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nCiteRipPortPrimary.setStatus("current")
_NCiteRipInterfacesTable_Object = MibTable
nCiteRipInterfacesTable = _NCiteRipInterfacesTable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 19, 3)
)
if mibBuilder.loadTexts:
    nCiteRipInterfacesTable.setStatus("current")
_NCiteRipInterfacesEntry_Object = MibTableRow
nCiteRipInterfacesEntry = _NCiteRipInterfacesEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 19, 3, 1)
)
nCiteRipInterfacesEntry.setIndexNames(
    (0, "Netrake-MIB", "nCiteRipInterafacesSlotNum"),
    (0, "Netrake-MIB", "nCiteRipInterfacesPortNum"),
    (0, "Netrake-MIB", "nCiteRipInterfacesIPAddr"),
)
if mibBuilder.loadTexts:
    nCiteRipInterfacesEntry.setStatus("current")
_NCiteRipInterafacesSlotNum_Type = Integer32
_NCiteRipInterafacesSlotNum_Object = MibTableColumn
nCiteRipInterafacesSlotNum = _NCiteRipInterafacesSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 19, 3, 1, 1),
    _NCiteRipInterafacesSlotNum_Type()
)
nCiteRipInterafacesSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nCiteRipInterafacesSlotNum.setStatus("current")
_NCiteRipInterfacesPortNum_Type = Integer32
_NCiteRipInterfacesPortNum_Object = MibTableColumn
nCiteRipInterfacesPortNum = _NCiteRipInterfacesPortNum_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 19, 3, 1, 2),
    _NCiteRipInterfacesPortNum_Type()
)
nCiteRipInterfacesPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nCiteRipInterfacesPortNum.setStatus("current")
_NCiteRipInterfacesIPAddr_Type = IpAddress
_NCiteRipInterfacesIPAddr_Object = MibTableColumn
nCiteRipInterfacesIPAddr = _NCiteRipInterfacesIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 19, 3, 1, 3),
    _NCiteRipInterfacesIPAddr_Type()
)
nCiteRipInterfacesIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nCiteRipInterfacesIPAddr.setStatus("current")
_NCiteAuthConfig_ObjectIdentity = ObjectIdentity
nCiteAuthConfig = _NCiteAuthConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 20)
)


class _AuthConfigLocalOverride_Type(Integer32):
    """Custom type authConfigLocalOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AuthConfigLocalOverride_Type.__name__ = "Integer32"
_AuthConfigLocalOverride_Object = MibScalar
authConfigLocalOverride = _AuthConfigLocalOverride_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 20, 1),
    _AuthConfigLocalOverride_Type()
)
authConfigLocalOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authConfigLocalOverride.setStatus("current")


class _AuthConfigRadiusRetryCount_Type(Integer32):
    """Custom type authConfigRadiusRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AuthConfigRadiusRetryCount_Type.__name__ = "Integer32"
_AuthConfigRadiusRetryCount_Object = MibScalar
authConfigRadiusRetryCount = _AuthConfigRadiusRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 20, 2),
    _AuthConfigRadiusRetryCount_Type()
)
authConfigRadiusRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authConfigRadiusRetryCount.setStatus("current")


class _AuthConfigRadiusRetryInterval_Type(Integer32):
    """Custom type authConfigRadiusRetryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AuthConfigRadiusRetryInterval_Type.__name__ = "Integer32"
_AuthConfigRadiusRetryInterval_Object = MibScalar
authConfigRadiusRetryInterval = _AuthConfigRadiusRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 20, 3),
    _AuthConfigRadiusRetryInterval_Type()
)
authConfigRadiusRetryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authConfigRadiusRetryInterval.setStatus("current")
_AuthConfigRadiusServersTable_Object = MibTable
authConfigRadiusServersTable = _AuthConfigRadiusServersTable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 20, 4)
)
if mibBuilder.loadTexts:
    authConfigRadiusServersTable.setStatus("current")
_AuthConfigRadiusServersEntry_Object = MibTableRow
authConfigRadiusServersEntry = _AuthConfigRadiusServersEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 20, 4, 1)
)
authConfigRadiusServersEntry.setIndexNames(
    (0, "Netrake-MIB", "authConfigRadiusServerIp"),
)
if mibBuilder.loadTexts:
    authConfigRadiusServersEntry.setStatus("current")
_AuthConfigRadiusServerIp_Type = IpAddress
_AuthConfigRadiusServerIp_Object = MibTableColumn
authConfigRadiusServerIp = _AuthConfigRadiusServerIp_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 20, 4, 1, 1),
    _AuthConfigRadiusServerIp_Type()
)
authConfigRadiusServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authConfigRadiusServerIp.setStatus("current")
_AuthConfigRadiusServerPort_Type = Integer32
_AuthConfigRadiusServerPort_Object = MibTableColumn
authConfigRadiusServerPort = _AuthConfigRadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 20, 4, 1, 2),
    _AuthConfigRadiusServerPort_Type()
)
authConfigRadiusServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authConfigRadiusServerPort.setStatus("current")


class _AuthConfigRadiusServerPriority_Type(Integer32):
    """Custom type authConfigRadiusServerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AuthConfigRadiusServerPriority_Type.__name__ = "Integer32"
_AuthConfigRadiusServerPriority_Object = MibTableColumn
authConfigRadiusServerPriority = _AuthConfigRadiusServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 20, 4, 1, 3),
    _AuthConfigRadiusServerPriority_Type()
)
authConfigRadiusServerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authConfigRadiusServerPriority.setStatus("current")
_LinkUpTrapAckSource_Type = IpAddress
_LinkUpTrapAckSource_Object = MibScalar
linkUpTrapAckSource = _LinkUpTrapAckSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 21),
    _LinkUpTrapAckSource_Type()
)
linkUpTrapAckSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkUpTrapAckSource.setStatus("current")
_LinkDownTrapAckSource_Type = IpAddress
_LinkDownTrapAckSource_Object = MibScalar
linkDownTrapAckSource = _LinkDownTrapAckSource_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 22),
    _LinkDownTrapAckSource_Type()
)
linkDownTrapAckSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkDownTrapAckSource.setStatus("current")
_NrObjectIDs_ObjectIdentity = ObjectIdentity
nrObjectIDs = _NrObjectIDs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 3)
)
_NrSessionBorderController_ObjectIdentity = ObjectIdentity
nrSessionBorderController = _NrSessionBorderController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 3, 1)
)
_NrSBCSE_ObjectIdentity = ObjectIdentity
nrSBCSE = _NrSBCSE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 3, 1, 1)
)
_NrSBCwNcp_ObjectIdentity = ObjectIdentity
nrSBCwNcp = _NrSBCwNcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 3, 1, 1, 1)
)
_NrSBCwNte_ObjectIdentity = ObjectIdentity
nrSBCwNte = _NrSBCwNte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 3, 1, 1, 2)
)
_NrSBCDE_ObjectIdentity = ObjectIdentity
nrSBCDE = _NrSBCDE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 3, 1, 2)
)

# Managed Objects groups


# Notification objects

chasPwrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 2, 2)
)
chasPwrTrap.setObjects(
      *(("Netrake-MIB", "chasPwrSupplyIndex"),
        ("Netrake-MIB", "chasPwrSupplyOperStatus"))
)
if mibBuilder.loadTexts:
    chasPwrTrap.setStatus(
        "current"
    )

chasFanTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 3, 2)
)
chasFanTrap.setObjects(
      *(("Netrake-MIB", "chasFanIndex"),
        ("Netrake-MIB", "chasFanOperStatus"))
)
if mibBuilder.loadTexts:
    chasFanTrap.setStatus(
        "current"
    )

chasBrdStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 1, 4, 2)
)
chasBrdStateChangeTrap.setObjects(
      *(("Netrake-MIB", "chasBrdSlotNum"),
        ("Netrake-MIB", "chasBrdType"),
        ("Netrake-MIB", "chasBrdState"))
)
if mibBuilder.loadTexts:
    chasBrdStateChangeTrap.setStatus(
        "current"
    )

systemOperStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 2, 6)
)
systemOperStateChangeTrap.setObjects(
    ("Netrake-MIB", "systemOperState")
)
if mibBuilder.loadTexts:
    systemOperStateChangeTrap.setStatus(
        "current"
    )

postAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 3, 3)
)
postAlarm.setObjects(
      *(("Netrake-MIB", "acitveAlarmReportingSource"),
        ("Netrake-MIB", "activeAlarmAdditionalInfo"),
        ("Netrake-MIB", "activeAlarmCategory"),
        ("Netrake-MIB", "activeAlarmDevType"),
        ("Netrake-MIB", "activeAlarmDisplayString"),
        ("Netrake-MIB", "activeAlarmId"),
        ("Netrake-MIB", "activeAlarmOccurances"),
        ("Netrake-MIB", "activeAlarmPortNum"),
        ("Netrake-MIB", "activeAlarmServiceAffecting"),
        ("Netrake-MIB", "activeAlarmSeverity"),
        ("Netrake-MIB", "activeAlarmSlotNum"),
        ("Netrake-MIB", "activeAlarmSysUpTime"),
        ("Netrake-MIB", "activeAlarmTimeStamp"),
        ("Netrake-MIB", "activeAlarmType"),
        ("Netrake-MIB", "activeAlarmSubType"),
        ("Netrake-MIB", "activeAlarmEventFlag"))
)
if mibBuilder.loadTexts:
    postAlarm.setStatus(
        "current"
    )

coldStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 4, 2)
)
coldStartTrap.setObjects(
      *(("Netrake-MIB", "systemRestoreFlag"),
        ("Netrake-MIB", "systemSoftwareVersion"))
)
if mibBuilder.loadTexts:
    coldStartTrap.setStatus(
        "current"
    )

redundantConfigChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 5, 7)
)
redundantConfigChangeTrap.setObjects(
      *(("Netrake-MIB", "redundantPairName"),
        ("Netrake-MIB", "redundantPort1IpAddr"),
        ("Netrake-MIB", "redundantPort2IpAddr"),
        ("Netrake-MIB", "redundantAdminState"),
        ("Netrake-MIB", "redundantPort1NetMask"),
        ("Netrake-MIB", "redundantPort2NetMask"))
)
if mibBuilder.loadTexts:
    redundantConfigChangeTrap.setStatus(
        "current"
    )

redundantFailbackThreshChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 5, 12)
)
redundantFailbackThreshChangeTrap.setObjects(
    ("Netrake-MIB", "redundantFailbackThresh")
)
if mibBuilder.loadTexts:
    redundantFailbackThreshChangeTrap.setStatus(
        "current"
    )

redundantRedirectorFlagChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 5, 14)
)
redundantRedirectorFlagChangeTrap.setObjects(
    ("Netrake-MIB", "redundantRedirectorFlag")
)
if mibBuilder.loadTexts:
    redundantRedirectorFlagChangeTrap.setStatus(
        "current"
    )

redundantAutoFailbackChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 5, 17)
)
redundantAutoFailbackChangeTrap.setObjects(
    ("Netrake-MIB", "redundantAutoFailbackFlag")
)
if mibBuilder.loadTexts:
    redundantAutoFailbackChangeTrap.setStatus(
        "current"
    )

nCiteSDRSentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 6, 10, 4)
)
nCiteSDRSentTrap.setObjects(
    ("Netrake-MIB", "nCIteSDRLastSent")
)
if mibBuilder.loadTexts:
    nCiteSDRSentTrap.setStatus(
        "current"
    )

diagStartedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 7, 4)
)
diagStartedTrap.setObjects(
    ("Netrake-MIB", "diagType")
)
if mibBuilder.loadTexts:
    diagStartedTrap.setStatus(
        "deprecated"
    )

diagCompleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 7, 5)
)
diagCompleteTrap.setObjects(
      *(("Netrake-MIB", "diagRsltIndex"),
        ("Netrake-MIB", "diagRsltCompleteTimeStamp"),
        ("Netrake-MIB", "diagRsltDesc"),
        ("Netrake-MIB", "diagRsltDevicePortNum"),
        ("Netrake-MIB", "diagRsltDeviceSlotNum"),
        ("Netrake-MIB", "diagRsltType"))
)
if mibBuilder.loadTexts:
    diagCompleteTrap.setStatus(
        "deprecated"
    )

newActiveImgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 14)
)
newActiveImgTrap.setObjects(
      *(("Netrake-MIB", "activeImgActivatedTimeStamp"),
        ("Netrake-MIB", "activeImgName"),
        ("Netrake-MIB", "activeImgPidSideAFilename"),
        ("Netrake-MIB", "activeImgPidSideBFilename"))
)
if mibBuilder.loadTexts:
    newActiveImgTrap.setStatus(
        "current"
    )

newCommittedImgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 15)
)
newCommittedImgTrap.setObjects(
      *(("Netrake-MIB", "commitImgTimeStamp"),
        ("Netrake-MIB", "commitImgName"))
)
if mibBuilder.loadTexts:
    newCommittedImgTrap.setStatus(
        "current"
    )

buildStartedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 21)
)
buildStartedTrap.setObjects(
      *(("Netrake-MIB", "nextImg"),
        ("Netrake-MIB", "nextImgState"))
)
if mibBuilder.loadTexts:
    buildStartedTrap.setStatus(
        "deprecated"
    )

buildCompleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 22)
)
buildCompleteTrap.setObjects(
      *(("Netrake-MIB", "nextImgName"),
        ("Netrake-MIB", "nextImgState"),
        ("Netrake-MIB", "nextImgBuildCompleteTimeStamp"))
)
if mibBuilder.loadTexts:
    buildCompleteTrap.setStatus(
        "deprecated"
    )

newNextTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 8, 23)
)
newNextTrap.setObjects(
      *(("Netrake-MIB", "nextImgName"),
        ("Netrake-MIB", "nextImgState"))
)
if mibBuilder.loadTexts:
    newNextTrap.setStatus(
        "deprecated"
    )

staticRouteChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 9, 2)
)
staticRouteChange.setObjects(
      *(("Netrake-MIB", "staticRouteAdminState"),
        ("Netrake-MIB", "staticRouteDest"),
        ("Netrake-MIB", "staticRouteIngressVlanTag"),
        ("Netrake-MIB", "staticRouteIngressProtocol"),
        ("Netrake-MIB", "staticRouteMetric1"),
        ("Netrake-MIB", "staticRouteNetMask"),
        ("Netrake-MIB", "staticRouteNextHop"),
        ("Netrake-MIB", "staticRouteOperState"),
        ("Netrake-MIB", "staticRouteRowStatus"),
        ("Netrake-MIB", "staticRouteType"))
)
if mibBuilder.loadTexts:
    staticRouteChange.setStatus(
        "current"
    )

staticRoutesRefreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 9, 4)
)
staticRoutesRefreshTrap.setObjects(
    ("Netrake-MIB", "staticRoutesRefreshNeeded")
)
if mibBuilder.loadTexts:
    staticRoutesRefreshTrap.setStatus(
        "current"
    )

arpRefreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 10, 5)
)
arpRefreshTrap.setObjects(
    ("Netrake-MIB", "arpRefreshNeeded")
)
if mibBuilder.loadTexts:
    arpRefreshTrap.setStatus(
        "current"
    )

arpUpdateMacTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 10, 7)
)
arpUpdateMacTrap.setObjects(
      *(("Netrake-MIB", "arpMacAddr"),
        ("Netrake-MIB", "arpNextHopIP"),
        ("Netrake-MIB", "arpTrapOper"))
)
if mibBuilder.loadTexts:
    arpUpdateMacTrap.setStatus(
        "current"
    )

arpVerifTimerChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 10, 12)
)
arpVerifTimerChangeTrap.setObjects(
    ("Netrake-MIB", "arpVerifTimerRetryCount")
)
if mibBuilder.loadTexts:
    arpVerifTimerChangeTrap.setStatus(
        "current"
    )

arpOperTimerChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 10, 14)
)
arpOperTimerChangeTrap.setObjects(
      *(("Netrake-MIB", "arpOperTimerFreq"),
        ("Netrake-MIB", "arpOperTimerRetryCount"))
)
if mibBuilder.loadTexts:
    arpOperTimerChangeTrap.setStatus(
        "current"
    )

ipPortConfigChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 11, 2)
)
ipPortConfigChangeTrap.setObjects(
      *(("Netrake-MIB", "ipPortConfigIpAddr"),
        ("Netrake-MIB", "ipPortConfigNetMask"),
        ("Netrake-MIB", "ipPortConfigOperState"),
        ("Netrake-MIB", "ipPortConfigPortNum"),
        ("Netrake-MIB", "ipPortConfigSlotNum"),
        ("Netrake-MIB", "ipPortVlanTag"),
        ("Netrake-MIB", "ipPortVrdTag"),
        ("Netrake-MIB", "ipPortConfigAdminState"),
        ("Netrake-MIB", "ipPortRowStatus"))
)
if mibBuilder.loadTexts:
    ipPortConfigChangeTrap.setStatus(
        "current"
    )

ipPortRefreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 11, 6)
)
ipPortRefreshTrap.setObjects(
    ("Netrake-MIB", "ipPortRefreshOpStates")
)
if mibBuilder.loadTexts:
    ipPortRefreshTrap.setStatus(
        "current"
    )

ipPortAutoNegChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 11, 9)
)
ipPortAutoNegChangeTrap.setObjects(
      *(("Netrake-MIB", "ipPortAutoNegFlag"),
        ("Netrake-MIB", "ipPortAutoNegPortNum"),
        ("Netrake-MIB", "ipPortAutoNegSlotNum"))
)
if mibBuilder.loadTexts:
    ipPortAutoNegChangeTrap.setStatus(
        "current"
    )

nCiteNTAReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 16, 2)
)
if mibBuilder.loadTexts:
    nCiteNTAReset.setStatus(
        "current"
    )

edrGarbageCollectionComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 17, 7)
)
edrGarbageCollectionComplete.setObjects(
      *(("Netrake-MIB", "edrGarbageCollectionStatus"),
        ("Netrake-MIB", "edrGarbageCollectionState"),
        ("Netrake-MIB", "edrLastGarbageCollection"),
        ("Netrake-MIB", "edrNextTrafficCheck"))
)
if mibBuilder.loadTexts:
    edrGarbageCollectionComplete.setStatus(
        "current"
    )

licenseFileChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 1, 18, 3)
)
licenseFileChangeTrap.setObjects(
    ("Netrake-MIB", "licenseFileName")
)
if mibBuilder.loadTexts:
    licenseFileChangeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Netrake-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "netrake": netrake,
       "products": products,
       "nCite": nCite,
       "chassis": chassis,
       "chasGen": chasGen,
       "chasSerNum": chasSerNum,
       "chasLedStatus": chasLedStatus,
       "chasPOSTMode": chasPOSTMode,
       "chasType": chasType,
       "chasPwr": chasPwr,
       "chasPwrSupplyTable": chasPwrSupplyTable,
       "chasPwrSupplyEntry": chasPwrSupplyEntry,
       "chasPwrSupplyIndex": chasPwrSupplyIndex,
       "chasPwrSupplyOperStatus": chasPwrSupplyOperStatus,
       "chasPwrSupplyDesc": chasPwrSupplyDesc,
       "chasPwrTrap": chasPwrTrap,
       "chasPwrTrapAck": chasPwrTrapAck,
       "chasPwrTrapAckSource": chasPwrTrapAckSource,
       "chasFan": chasFan,
       "chasFanTable": chasFanTable,
       "chasFanEntry": chasFanEntry,
       "chasFanIndex": chasFanIndex,
       "chasFanOperStatus": chasFanOperStatus,
       "chasFanDescription": chasFanDescription,
       "chasFanTrap": chasFanTrap,
       "chasFanTrapAck": chasFanTrapAck,
       "chasFanTrapAckSource": chasFanTrapAckSource,
       "chasBrd": chasBrd,
       "chasBrdTable": chasBrdTable,
       "chasBrdEntry": chasBrdEntry,
       "chasBrdSlotNum": chasBrdSlotNum,
       "chasBrdDescription": chasBrdDescription,
       "chasBrdType": chasBrdType,
       "chasBrdOccSlots": chasBrdOccSlots,
       "chasBrdMaxPorts": chasBrdMaxPorts,
       "chasBrdSlotLabel": chasBrdSlotLabel,
       "chasBrdStatusLeds": chasBrdStatusLeds,
       "chasBrdState": chasBrdState,
       "chasBrdPwr": chasBrdPwr,
       "chasBrdIfIndex": chasBrdIfIndex,
       "chasBrdSerialNum": chasBrdSerialNum,
       "chasBrdReset": chasBrdReset,
       "chasBrdStateChangeTrap": chasBrdStateChangeTrap,
       "chasBrdStateChangeTrapAck": chasBrdStateChangeTrapAck,
       "chasBrdStateChangeTrapAckSource": chasBrdStateChangeTrapAckSource,
       "nCiteSystem": nCiteSystem,
       "resourceUsageTable": resourceUsageTable,
       "resourceUsageEntry": resourceUsageEntry,
       "processorIndex": processorIndex,
       "memTotal": memTotal,
       "memUsed": memUsed,
       "cpuUsage": cpuUsage,
       "systemSoftwareVersion": systemSoftwareVersion,
       "systemRestoreFlag": systemRestoreFlag,
       "systemOperState": systemOperState,
       "systemAdminState": systemAdminState,
       "systemOperStateChangeTrap": systemOperStateChangeTrap,
       "systemOperStateChangeTrapAck": systemOperStateChangeTrapAck,
       "systemOperStateChangeTrapAckSource": systemOperStateChangeTrapAckSource,
       "systemTrapAckTable": systemTrapAckTable,
       "systemTrapAckEntry": systemTrapAckEntry,
       "systemSnmpMgrIpAddress": systemSnmpMgrIpAddress,
       "systemTrapNoAck": systemTrapNoAck,
       "alarm": alarm,
       "activeAlarmTable": activeAlarmTable,
       "activeAlarmEntry": activeAlarmEntry,
       "activeAlarmIndex": activeAlarmIndex,
       "activeAlarmId": activeAlarmId,
       "activeAlarmType": activeAlarmType,
       "activeAlarmServiceAffecting": activeAlarmServiceAffecting,
       "activeAlarmCategory": activeAlarmCategory,
       "activeAlarmTimeStamp": activeAlarmTimeStamp,
       "activeAlarmSlotNum": activeAlarmSlotNum,
       "activeAlarmPortNum": activeAlarmPortNum,
       "activeAlarmSysUpTime": activeAlarmSysUpTime,
       "activeAlarmDevType": activeAlarmDevType,
       "activeAlarmAdditionalInfo": activeAlarmAdditionalInfo,
       "activeAlarmOccurances": activeAlarmOccurances,
       "acitveAlarmReportingSource": acitveAlarmReportingSource,
       "activeAlarmSeverity": activeAlarmSeverity,
       "activeAlarmDisplayString": activeAlarmDisplayString,
       "activeAlarmSubType": activeAlarmSubType,
       "activeAlarmEventFlag": activeAlarmEventFlag,
       "histEvent": histEvent,
       "postAlarm": postAlarm,
       "postEvent": postEvent,
       "activeAlarmAcknowledge": activeAlarmAcknowledge,
       "activeAlarmID": activeAlarmID,
       "eventAcknowledge": eventAcknowledge,
       "eventID": eventID,
       "activeAlarmAcknowledgeSource": activeAlarmAcknowledgeSource,
       "switchNotifications": switchNotifications,
       "coldStartTrapEnable": coldStartTrapEnable,
       "coldStartTrap": coldStartTrap,
       "coldStartTrapAck": coldStartTrapAck,
       "coldStartTrapAckSource": coldStartTrapAckSource,
       "nCiteRedundant": nCiteRedundant,
       "redundantPort1IpAddr": redundantPort1IpAddr,
       "redundantPort2IpAddr": redundantPort2IpAddr,
       "redundantAdminState": redundantAdminState,
       "redundantMateName": redundantMateName,
       "redundantConfigChangeTrapAck": redundantConfigChangeTrapAck,
       "redundantConfigChangeTrap": redundantConfigChangeTrap,
       "redundantPort1NetMask": redundantPort1NetMask,
       "redundantPort2NetMask": redundantPort2NetMask,
       "redundantFailbackThresh": redundantFailbackThresh,
       "redundantRedirectorFlag": redundantRedirectorFlag,
       "redundantFailbackThreshChangeTrap": redundantFailbackThreshChangeTrap,
       "redundantFailbackThreshChangeTrapAck": redundantFailbackThreshChangeTrapAck,
       "redundantRedirectorFlagChangeTrap": redundantRedirectorFlagChangeTrap,
       "redundantRedirectorFlagChangeTrapAck": redundantRedirectorFlagChangeTrapAck,
       "redundantAutoFailbackFlag": redundantAutoFailbackFlag,
       "redundantAutoFailbackChangeTrap": redundantAutoFailbackChangeTrap,
       "redundantAutoFailbackFlagChangeTrapAck": redundantAutoFailbackFlagChangeTrapAck,
       "redundantConfigChangeTrapAckSource": redundantConfigChangeTrapAckSource,
       "redundantFailbackThreshChangeTrapAckSource": redundantFailbackThreshChangeTrapAckSource,
       "redundantRedirectorFlagChangeTrapAckSource": redundantRedirectorFlagChangeTrapAckSource,
       "redundantAutoFailbackFlagChangeTrapAckSource": redundantAutoFailbackFlagChangeTrapAckSource,
       "nCiteStats": nCiteStats,
       "globalCounters": globalCounters,
       "totalPacketsXmitCPA": totalPacketsXmitCPA,
       "numPacketsDiscardCPA": numPacketsDiscardCPA,
       "totalPacketsXmitCPB": totalPacketsXmitCPB,
       "numPacketsDiscardCPB": numPacketsDiscardCPB,
       "totalPacketsXmit": totalPacketsXmit,
       "totalPacketsDiscard": totalPacketsDiscard,
       "gigEStats": gigEStats,
       "gigEStatsTable": gigEStatsTable,
       "gigEStatsEntry": gigEStatsEntry,
       "gigEStatsPortIndex": gigEStatsPortIndex,
       "gigEStatsSlotNum": gigEStatsSlotNum,
       "linkStatusChanges": linkStatusChanges,
       "framesRcvdOkCount": framesRcvdOkCount,
       "octetsRcvdOkCount": octetsRcvdOkCount,
       "framesRcvdCount": framesRcvdCount,
       "octetsRcvdCount": octetsRcvdCount,
       "frameSeqErrCount": frameSeqErrCount,
       "lostFramesMacErrCount": lostFramesMacErrCount,
       "rcvdFrames64Octets": rcvdFrames64Octets,
       "octetsRcvd1519toMax": octetsRcvd1519toMax,
       "xmitFrames64Octets": xmitFrames64Octets,
       "octetsXmit1024to1518": octetsXmit1024to1518,
       "octetsXmitCount": octetsXmitCount,
       "unicastFramesXmitOk": unicastFramesXmitOk,
       "unicastFramesRcvdOk": unicastFramesRcvdOk,
       "broadcastFramesXmitOk": broadcastFramesXmitOk,
       "broadcastFramesRcvdOk": broadcastFramesRcvdOk,
       "multicastFramesXmitOk": multicastFramesXmitOk,
       "multicastFramesRcvdOk": multicastFramesRcvdOk,
       "octetsRcvd65to127": octetsRcvd65to127,
       "octetsXmit65to127": octetsXmit65to127,
       "octetRcvd128to255": octetRcvd128to255,
       "octetsXmit128to255": octetsXmit128to255,
       "octetsRcvd256to511": octetsRcvd256to511,
       "octetsXmit256to511": octetsXmit256to511,
       "octetsRcvd512to1023": octetsRcvd512to1023,
       "octetsXmit512to1023": octetsXmit512to1023,
       "octetsRcvd1024to1518": octetsRcvd1024to1518,
       "octetsXmit1519toMax": octetsXmit1519toMax,
       "underSizeFramesRcvd": underSizeFramesRcvd,
       "jabbersRcvd": jabbersRcvd,
       "serviceStats": serviceStats,
       "serviceStatsTable": serviceStatsTable,
       "serviceStatsEntry": serviceStatsEntry,
       "serviceStatsPortIndex": serviceStatsPortIndex,
       "serviceStatsSlotId": serviceStatsSlotId,
       "realTimeTotalPackets": realTimeTotalPackets,
       "realTimeDiscardPackets": realTimeDiscardPackets,
       "nrtTotalPackets": nrtTotalPackets,
       "nrtDiscardPackets": nrtDiscardPackets,
       "bestEffortTotalPackets": bestEffortTotalPackets,
       "bestEffortDiscardPackets": bestEffortDiscardPackets,
       "redundancyStats": redundancyStats,
       "redundPairedModeTimeTicks": redundPairedModeTimeTicks,
       "redundRecoveryModeTimeTicks": redundRecoveryModeTimeTicks,
       "redundNumRedundLinkFailures": redundNumRedundLinkFailures,
       "redundActiveMateCalls": redundActiveMateCalls,
       "redundActiveMateRegist": redundActiveMateRegist,
       "policyStats": policyStats,
       "policyCountersTable": policyCountersTable,
       "policyCountersEntry": policyCountersEntry,
       "policyIndex": policyIndex,
       "policyTotalPacketsA": policyTotalPacketsA,
       "policyTotalPacketsB": policyTotalPacketsB,
       "policyTotalPackets": policyTotalPackets,
       "policyStatsReset": policyStatsReset,
       "sipStats": sipStats,
       "sipStatCallsInitiating": sipStatCallsInitiating,
       "sipStatNonLocalActiveCalls": sipStatNonLocalActiveCalls,
       "sipStatLocalActiveCalls": sipStatLocalActiveCalls,
       "sipStatTermCalls": sipStatTermCalls,
       "sipStatPeakActiveCalls": sipStatPeakActiveCalls,
       "sipStatTotalActiveCalls": sipStatTotalActiveCalls,
       "sipStatCallsCompletedSuccess": sipStatCallsCompletedSuccess,
       "sipStatCallsFailed": sipStatCallsFailed,
       "sipStatCallsAbandoned": sipStatCallsAbandoned,
       "sipStatCallsDropped": sipStatCallsDropped,
       "sipStatCallsDegraded": sipStatCallsDegraded,
       "sipStatAuthFailures": sipStatAuthFailures,
       "sipStatCallMediaTimeouts": sipStatCallMediaTimeouts,
       "sipStatCallInitTimeouts": sipStatCallInitTimeouts,
       "sipStatTermTimeouts": sipStatTermTimeouts,
       "sipStatMsgErrs": sipStatMsgErrs,
       "sipStatCallsProcessed": sipStatCallsProcessed,
       "sipStatPeakNonLocalCalls": sipStatPeakNonLocalCalls,
       "sipStatPeakLocalCalls": sipStatPeakLocalCalls,
       "sipStatRedirectSuccess": sipStatRedirectSuccess,
       "sipStatRedirectFailures": sipStatRedirectFailures,
       "sipStatMessageRoutingFailures": sipStatMessageRoutingFailures,
       "sipStatAuthenticationChallenges": sipStatAuthenticationChallenges,
       "sipStatRTPFWTraversalTimeouts": sipStatRTPFWTraversalTimeouts,
       "sipStatMessagesReroutedToMate": sipStatMessagesReroutedToMate,
       "sipStatSameSideActiveCalls": sipStatSameSideActiveCalls,
       "sipStatNormalActiveCalls": sipStatNormalActiveCalls,
       "sipStatPeakSameSideActiveCalls": sipStatPeakSameSideActiveCalls,
       "sipStatPeakNormalActiveCalls": sipStatPeakNormalActiveCalls,
       "sipStatCurrentFaxSessions": sipStatCurrentFaxSessions,
       "sipStatPeakFaxSessions": sipStatPeakFaxSessions,
       "sipStatTotalFaxSessions": sipStatTotalFaxSessions,
       "sipStatPeakTotalActiveCalls": sipStatPeakTotalActiveCalls,
       "vlanStats": vlanStats,
       "vlanStatsTable": vlanStatsTable,
       "vlanStatsEntry": vlanStatsEntry,
       "vlanStatsSlotNum": vlanStatsSlotNum,
       "vlanStatsPortNum": vlanStatsPortNum,
       "vlanStatsVlanLabel": vlanStatsVlanLabel,
       "vlanTotalPacketsXmit": vlanTotalPacketsXmit,
       "vlanTotalPacketsRcvd": vlanTotalPacketsRcvd,
       "vlanStatsReset": vlanStatsReset,
       "custSipStats": custSipStats,
       "custSipStatsTable": custSipStatsTable,
       "custSipStatsEntry": custSipStatsEntry,
       "custSipStatId": custSipStatId,
       "custSipStatCallsInitiating": custSipStatCallsInitiating,
       "custSipStatNonLocalActiveCalls": custSipStatNonLocalActiveCalls,
       "custSipStatLocalActiveCalls": custSipStatLocalActiveCalls,
       "custSipStatTermCalls": custSipStatTermCalls,
       "custSipStatPeakActiveCalls": custSipStatPeakActiveCalls,
       "custSipStatTotalActiveCalls": custSipStatTotalActiveCalls,
       "custSipStatCallsCompletedSuccess": custSipStatCallsCompletedSuccess,
       "custSipStatCallsFailed": custSipStatCallsFailed,
       "custSipStatCallsAbandoned": custSipStatCallsAbandoned,
       "custSipStatCallsDropped": custSipStatCallsDropped,
       "custSipStatCallsDegraded": custSipStatCallsDegraded,
       "custSipStatCallMediaTimeouts": custSipStatCallMediaTimeouts,
       "custSipStatCallInitTimeouts": custSipStatCallInitTimeouts,
       "custSipStatTermTimeouts": custSipStatTermTimeouts,
       "custSipStatCallsProcessed": custSipStatCallsProcessed,
       "custSipPeakNonLocalCalls": custSipPeakNonLocalCalls,
       "custSipPeakLocalCalls": custSipPeakLocalCalls,
       "custSipAuthenticationChallenges": custSipAuthenticationChallenges,
       "custSipRTPFWTraversalTimeouts": custSipRTPFWTraversalTimeouts,
       "custSipSameSideActiveCalls": custSipSameSideActiveCalls,
       "custSipNormalActiveCalls": custSipNormalActiveCalls,
       "custSipPeakNormalActiveCalls": custSipPeakNormalActiveCalls,
       "custSipPeakTotalActive": custSipPeakTotalActive,
       "nCiteStatsConfigReset": nCiteStatsConfigReset,
       "nCiteSessionDetailRecord": nCiteSessionDetailRecord,
       "nCiteSDRCollectionCycle": nCiteSDRCollectionCycle,
       "nCIteSDRLastSent": nCIteSDRLastSent,
       "nCiteSDREnable": nCiteSDREnable,
       "nCiteSDRSentTrap": nCiteSDRSentTrap,
       "nCiteSDRSentTrapAck": nCiteSDRSentTrapAck,
       "nCiteSDRSentTrapAckSource": nCiteSDRSentTrapAckSource,
       "registrationStats": registrationStats,
       "regStatNumInitiating": regStatNumInitiating,
       "regStatNumActive": regStatNumActive,
       "regStatPeak": regStatPeak,
       "regStatUpdateSuccess": regStatUpdateSuccess,
       "regStatUpdateFailed": regStatUpdateFailed,
       "regStatExpired": regStatExpired,
       "regStatDropped": regStatDropped,
       "regStatAuthFailures": regStatAuthFailures,
       "regStatInitSipTimeouts": regStatInitSipTimeouts,
       "regStatTermSipTimeouts": regStatTermSipTimeouts,
       "regStatTerminating": regStatTerminating,
       "regStatFailed": regStatFailed,
       "regStatAuthenticationChallenges": regStatAuthenticationChallenges,
       "regStatUnauthReg": regStatUnauthReg,
       "custRegStats": custRegStats,
       "custRegStatsTable": custRegStatsTable,
       "custRegStatsEntry": custRegStatsEntry,
       "custRegStatId": custRegStatId,
       "custRegStatNumInitiated": custRegStatNumInitiated,
       "custRegStatNumActive": custRegStatNumActive,
       "custRegStatPeak": custRegStatPeak,
       "custRegStatUpdateSuccess": custRegStatUpdateSuccess,
       "custRegStatUpdateFailed": custRegStatUpdateFailed,
       "custRegStatExpired": custRegStatExpired,
       "custRegStatDropped": custRegStatDropped,
       "custRegStatInitSipTimeouts": custRegStatInitSipTimeouts,
       "custRegStatTermSipTimeouts": custRegStatTermSipTimeouts,
       "custRegStatTerminating": custRegStatTerminating,
       "custRegStatFailed": custRegStatFailed,
       "custRegAuthenticationChallenges": custRegAuthenticationChallenges,
       "custRegStatUnauthorizedReg": custRegStatUnauthorizedReg,
       "ntsStats": ntsStats,
       "ntsStatNumCust": ntsStatNumCust,
       "ntsStatAuthFailures": ntsStatAuthFailures,
       "ntsStatCustConnected": ntsStatCustConnected,
       "rogueStats": rogueStats,
       "edrCurrentCallCount": edrCurrentCallCount,
       "edrPeakCallCount": edrPeakCallCount,
       "edrTotalCallsRogue": edrTotalCallsRogue,
       "edrLastDetection": edrLastDetection,
       "lrdCurrentCallCount": lrdCurrentCallCount,
       "lrdPeakCallCount": lrdPeakCallCount,
       "lrdTotalCallsRogue": lrdTotalCallsRogue,
       "lrdLastDetection": lrdLastDetection,
       "nCiteStatsReset": nCiteStatsReset,
       "custNtsStats": custNtsStats,
       "custNtsStatsTable": custNtsStatsTable,
       "custNtsStatsEntry": custNtsStatsEntry,
       "custNtsStatId": custNtsStatId,
       "custNtsAuthorizationFailed": custNtsAuthorizationFailed,
       "sipH323Stats": sipH323Stats,
       "sipH323CallsInitiating": sipH323CallsInitiating,
       "sipH323LocalActiveCalls": sipH323LocalActiveCalls,
       "sipH323TermCalls": sipH323TermCalls,
       "sipH323PeakTotalActiveCalls": sipH323PeakTotalActiveCalls,
       "sipH323TotalActiveCalls": sipH323TotalActiveCalls,
       "sipH323CallsCompletedSuccess": sipH323CallsCompletedSuccess,
       "sipH323CallsFailed": sipH323CallsFailed,
       "sipH323CallsAbandoned": sipH323CallsAbandoned,
       "sipH323CallsDropped": sipH323CallsDropped,
       "sipH323CallsDegraded": sipH323CallsDegraded,
       "sipH323AuthFailures": sipH323AuthFailures,
       "sipH323CallMediaTimeouts": sipH323CallMediaTimeouts,
       "sipH323CallInitTimeouts": sipH323CallInitTimeouts,
       "sipH323TermTimeouts": sipH323TermTimeouts,
       "sipH323MsgErrs": sipH323MsgErrs,
       "sipH323CallsProcessed": sipH323CallsProcessed,
       "sipH323PeakLocalCalls": sipH323PeakLocalCalls,
       "sipH323RedirectSuccess": sipH323RedirectSuccess,
       "sipH323RedirectFailures": sipH323RedirectFailures,
       "sipH323MessageRoutingFailures": sipH323MessageRoutingFailures,
       "sipH323AuthenticationChallenges": sipH323AuthenticationChallenges,
       "sipH323RTPFWTraversalTimeouts": sipH323RTPFWTraversalTimeouts,
       "sipH323MessagesReroutedToMate": sipH323MessagesReroutedToMate,
       "sipH323SameSideActiveCalls": sipH323SameSideActiveCalls,
       "sipH323NormalActiveCalls": sipH323NormalActiveCalls,
       "sipH323PeakSameSideActiveCalls": sipH323PeakSameSideActiveCalls,
       "sipH323PeakNormalActiveCalls": sipH323PeakNormalActiveCalls,
       "sipH323CurrentFaxSessions": sipH323CurrentFaxSessions,
       "sipH323PeakFaxSessions": sipH323PeakFaxSessions,
       "sipH323TotalFaxSessions": sipH323TotalFaxSessions,
       "h323Stats": h323Stats,
       "h323CallsInitiating": h323CallsInitiating,
       "h323LocalActiveCalls": h323LocalActiveCalls,
       "h323TermCalls": h323TermCalls,
       "h323PeakTotalActiveCalls": h323PeakTotalActiveCalls,
       "h323TotalActiveCalls": h323TotalActiveCalls,
       "h323CallsCompletedSuccess": h323CallsCompletedSuccess,
       "h323CallsFailed": h323CallsFailed,
       "h323CallsAbandoned": h323CallsAbandoned,
       "h323CallsDropped": h323CallsDropped,
       "h323CallsDegraded": h323CallsDegraded,
       "h323AuthFailures": h323AuthFailures,
       "h323CallMediaTimeouts": h323CallMediaTimeouts,
       "h323CallInitTimeouts": h323CallInitTimeouts,
       "h323TermTimeouts": h323TermTimeouts,
       "h323MsgErrs": h323MsgErrs,
       "h323CallsProcessed": h323CallsProcessed,
       "h323PeakLocalCalls": h323PeakLocalCalls,
       "h323MessageRoutingFailures": h323MessageRoutingFailures,
       "h323AuthenticationChallenges": h323AuthenticationChallenges,
       "h323RTPFWTraversalTimeouts": h323RTPFWTraversalTimeouts,
       "h323SameSideActiveCalls": h323SameSideActiveCalls,
       "h323NormalActiveCalls": h323NormalActiveCalls,
       "h323PeakSameSideActiveCalls": h323PeakSameSideActiveCalls,
       "h323PeakNormalActiveCalls": h323PeakNormalActiveCalls,
       "h323CurrentFaxSessions": h323CurrentFaxSessions,
       "h323PeakFaxSessions": h323PeakFaxSessions,
       "h323TotalFaxSessions": h323TotalFaxSessions,
       "voIpStats": voIpStats,
       "voIpCallsInitiating": voIpCallsInitiating,
       "voIpLocalActiveCalls": voIpLocalActiveCalls,
       "voIpTermCalls": voIpTermCalls,
       "voIpPeakTotalActiveCalls": voIpPeakTotalActiveCalls,
       "voIpTotalActiveCalls": voIpTotalActiveCalls,
       "voIpCallsCompletedSuccess": voIpCallsCompletedSuccess,
       "voIpCallsFailed": voIpCallsFailed,
       "voIpCallsAbandoned": voIpCallsAbandoned,
       "voIpCallsDropped": voIpCallsDropped,
       "voIpCallsDegraded": voIpCallsDegraded,
       "voIpAuthFailures": voIpAuthFailures,
       "voIpCallMediaTimeouts": voIpCallMediaTimeouts,
       "voIpCallInitTimeouts": voIpCallInitTimeouts,
       "voIpTermTimeouts": voIpTermTimeouts,
       "voIpMsgErrs": voIpMsgErrs,
       "voIpCallsProcessed": voIpCallsProcessed,
       "voIpPeakLocalCalls": voIpPeakLocalCalls,
       "voIpRedirectSuccess": voIpRedirectSuccess,
       "voIpRedirectFailures": voIpRedirectFailures,
       "voIpMessageRoutingFailures": voIpMessageRoutingFailures,
       "voIpAuthenticationChallenges": voIpAuthenticationChallenges,
       "voIpRTPFWTraversalTimeouts": voIpRTPFWTraversalTimeouts,
       "voIpMessagesReroutedToMate": voIpMessagesReroutedToMate,
       "voIpSameSideActiveCalls": voIpSameSideActiveCalls,
       "voIpNormalActiveCalls": voIpNormalActiveCalls,
       "voIpPeakSameSideActiveCalls": voIpPeakSameSideActiveCalls,
       "voIpPeakNormalActiveCalls": voIpPeakNormalActiveCalls,
       "voIpCurrentFaxSessions": voIpCurrentFaxSessions,
       "voIpPeakFaxSessions": voIpPeakFaxSessions,
       "voIpTotalFaxSessions": voIpTotalFaxSessions,
       "custSipH323Stats": custSipH323Stats,
       "custSipH323StatsTable": custSipH323StatsTable,
       "custSipH323StatsEntry": custSipH323StatsEntry,
       "custSipH323Id": custSipH323Id,
       "custSipH323CallsInitiating": custSipH323CallsInitiating,
       "custSipH323LocalActiveCalls": custSipH323LocalActiveCalls,
       "custSipH323TermCalls": custSipH323TermCalls,
       "custSipH323PeakTotalActiveCalls": custSipH323PeakTotalActiveCalls,
       "custSipH323TotalActiveCalls": custSipH323TotalActiveCalls,
       "custSipH323CallsCompletedSuccess": custSipH323CallsCompletedSuccess,
       "custSipH323CallsFailed": custSipH323CallsFailed,
       "custSipH323CallsAbandoned": custSipH323CallsAbandoned,
       "custSipH323CallsDropped": custSipH323CallsDropped,
       "custSipH323CallsDegraded": custSipH323CallsDegraded,
       "custSipH323CallMediaTimeouts": custSipH323CallMediaTimeouts,
       "custSipH323CallInitTimeouts": custSipH323CallInitTimeouts,
       "custSipH323TermTimeouts": custSipH323TermTimeouts,
       "custSipH323CallsProcessed": custSipH323CallsProcessed,
       "custSipH323PeakLocalCalls": custSipH323PeakLocalCalls,
       "custSipH323AuthenticationChallenges": custSipH323AuthenticationChallenges,
       "custSipH323RTPFWTraversalTimeouts": custSipH323RTPFWTraversalTimeouts,
       "custSipH323SameSideActiveCalls": custSipH323SameSideActiveCalls,
       "custSipH323NormalActiveCalls": custSipH323NormalActiveCalls,
       "custSipH323PeakNormalActiveCalls": custSipH323PeakNormalActiveCalls,
       "custH323Stats": custH323Stats,
       "custH323StatsTable": custH323StatsTable,
       "custH323StatsEntry": custH323StatsEntry,
       "custH323Id": custH323Id,
       "custH323CallsInitiating": custH323CallsInitiating,
       "custH323LocalActiveCalls": custH323LocalActiveCalls,
       "custH323TermCalls": custH323TermCalls,
       "custH323PeakTotalActiveCalls": custH323PeakTotalActiveCalls,
       "custH323TotalActiveCalls": custH323TotalActiveCalls,
       "custH323CallsCompletedSuccess": custH323CallsCompletedSuccess,
       "custH323CallsFailed": custH323CallsFailed,
       "custH323CallsAbandoned": custH323CallsAbandoned,
       "custH323CallsDropped": custH323CallsDropped,
       "custH323CallsDegraded": custH323CallsDegraded,
       "custH323CallMediaTimeouts": custH323CallMediaTimeouts,
       "custH323CallInitTimeouts": custH323CallInitTimeouts,
       "custH323TermTimeouts": custH323TermTimeouts,
       "custH323CallsProcessed": custH323CallsProcessed,
       "custH323PeakLocalCalls": custH323PeakLocalCalls,
       "custH323AuthenticationChallenges": custH323AuthenticationChallenges,
       "custH323RTPFWTraversalTimeouts": custH323RTPFWTraversalTimeouts,
       "custH323SameSideActiveCalls": custH323SameSideActiveCalls,
       "custH323NormalActiveCalls": custH323NormalActiveCalls,
       "custH323PeakNormalActiveCalls": custH323PeakNormalActiveCalls,
       "custVoIpStats": custVoIpStats,
       "custVoIpStatsTable": custVoIpStatsTable,
       "custVoIpStatsEntry": custVoIpStatsEntry,
       "custVoIpId": custVoIpId,
       "custVoIpCallsInitiating": custVoIpCallsInitiating,
       "custVoIpLocalActiveCalls": custVoIpLocalActiveCalls,
       "custVoIpTermCalls": custVoIpTermCalls,
       "custVoIpPeakTotalActiveCalls": custVoIpPeakTotalActiveCalls,
       "custVoIpTotalActiveCalls": custVoIpTotalActiveCalls,
       "custVoIpCallsCompletedSuccess": custVoIpCallsCompletedSuccess,
       "custVoIpCallsFailed": custVoIpCallsFailed,
       "custVoIpCallsAbandoned": custVoIpCallsAbandoned,
       "custVoIpCallsDropped": custVoIpCallsDropped,
       "custVoIpCallsDegraded": custVoIpCallsDegraded,
       "custVoIpCallMediaTimeouts": custVoIpCallMediaTimeouts,
       "custVoIpCallInitTimeouts": custVoIpCallInitTimeouts,
       "custVoIpTermTimeouts": custVoIpTermTimeouts,
       "custVoIpCallsProcessed": custVoIpCallsProcessed,
       "custVoIpPeakLocalCalls": custVoIpPeakLocalCalls,
       "custVoIpAuthenticationChallenges": custVoIpAuthenticationChallenges,
       "custVoIpRTPFWTraversalTimeouts": custVoIpRTPFWTraversalTimeouts,
       "custVoIpSameSideActiveCalls": custVoIpSameSideActiveCalls,
       "custVoIpNormalActiveCalls": custVoIpNormalActiveCalls,
       "custVoIpPeakNormalActiveCalls": custVoIpPeakNormalActiveCalls,
       "mediaStats": mediaStats,
       "mediaStatCurrentAudioSessions": mediaStatCurrentAudioSessions,
       "mediaStatPeakAudioSessions": mediaStatPeakAudioSessions,
       "mediaStatTotalAudioSessions": mediaStatTotalAudioSessions,
       "mediaStatCurrentVideoSessions": mediaStatCurrentVideoSessions,
       "mediaStatPeakVideoSessions": mediaStatPeakVideoSessions,
       "mediaStatTotalVideoSessions": mediaStatTotalVideoSessions,
       "mediaStatCurrentFaxSessions": mediaStatCurrentFaxSessions,
       "mediaStatPeakFaxSessions": mediaStatPeakFaxSessions,
       "mediaStatTotalFaxSessions": mediaStatTotalFaxSessions,
       "mediaStatTotalFailures": mediaStatTotalFailures,
       "h323RegStats": h323RegStats,
       "h323RegStatActiveReg": h323RegStatActiveReg,
       "h323RegStatExpiredReg": h323RegStatExpiredReg,
       "h323RegStatUnauthorizedReg": h323RegStatUnauthorizedReg,
       "h323RegStatPeakActiveReg": h323RegStatPeakActiveReg,
       "h323RegStatUpdateComplete": h323RegStatUpdateComplete,
       "h323RegStatUpdateFailures": h323RegStatUpdateFailures,
       "h323RegStatAuthFailures": h323RegStatAuthFailures,
       "custH323RegStats": custH323RegStats,
       "custH323RegStatsTable": custH323RegStatsTable,
       "custH323RegStatsEntry": custH323RegStatsEntry,
       "custH323RegStatId": custH323RegStatId,
       "custH323RegStatActiveReg": custH323RegStatActiveReg,
       "custH323RegStatExpiredReg": custH323RegStatExpiredReg,
       "custH323RegStatUnauthorizedReg": custH323RegStatUnauthorizedReg,
       "custH323RegStatPeakActiveReg": custH323RegStatPeakActiveReg,
       "custH323RegStatUpdateComplete": custH323RegStatUpdateComplete,
       "custH323RegStatUpdateFailures": custH323RegStatUpdateFailures,
       "custH323RegStatAuthFailures": custH323RegStatAuthFailures,
       "sipCommonStats": sipCommonStats,
       "sipCommonStatsDiscontinuityTimer": sipCommonStatsDiscontinuityTimer,
       "sipCommonStatsScalars": sipCommonStatsScalars,
       "sipCommonStatsTotalMessageErrors": sipCommonStatsTotalMessageErrors,
       "sipCommonStatsTotalMessageRoutingFailures": sipCommonStatsTotalMessageRoutingFailures,
       "sipCommonStatsTotalMessageTransmitFailures": sipCommonStatsTotalMessageTransmitFailures,
       "sipCommonStatsTotalAuthenticationFailures": sipCommonStatsTotalAuthenticationFailures,
       "sipEvtDlgStats": sipEvtDlgStats,
       "sipEvtDlgStatsDiscontinuityTimer": sipEvtDlgStatsDiscontinuityTimer,
       "sipEvtDlgStatsScalars": sipEvtDlgStatsScalars,
       "sipEvtDlgStatsActiveDialogs": sipEvtDlgStatsActiveDialogs,
       "sipEvtDlgStatsPeakActiveDialogs": sipEvtDlgStatsPeakActiveDialogs,
       "sipEvtDlgStatsTerminatedDialogs": sipEvtDlgStatsTerminatedDialogs,
       "sipEvtDlgStatsExpiredDialogs": sipEvtDlgStatsExpiredDialogs,
       "sipEvtDlgStatsFailedDialogs": sipEvtDlgStatsFailedDialogs,
       "sipEvtDlgStatsUnauthorizedDialogs": sipEvtDlgStatsUnauthorizedDialogs,
       "sipEvtDlgStatsAuthenticationChallenges": sipEvtDlgStatsAuthenticationChallenges,
       "sipEvtDlgCustStatsTable": sipEvtDlgCustStatsTable,
       "sipEvtDlgCustStatsEntry": sipEvtDlgCustStatsEntry,
       "sipEvtDlgCustStatsIndex": sipEvtDlgCustStatsIndex,
       "sipEvtDlgCustStatsActiveDialogs": sipEvtDlgCustStatsActiveDialogs,
       "sipEvtDlgCustStatsPeakActiveDialogs": sipEvtDlgCustStatsPeakActiveDialogs,
       "sipEvtDlgCustStatsTerminatedDialogs": sipEvtDlgCustStatsTerminatedDialogs,
       "sipEvtDlgCustStatsExpiredDialogs": sipEvtDlgCustStatsExpiredDialogs,
       "sipEvtDlgCustStatsFailedDialogs": sipEvtDlgCustStatsFailedDialogs,
       "sipEvtDlgCustStatsUnauthorizedDialogs": sipEvtDlgCustStatsUnauthorizedDialogs,
       "sipEvtDlgCustStatsAuthenticationChallenges": sipEvtDlgCustStatsAuthenticationChallenges,
       "diagnostics": diagnostics,
       "runDiagGroup": runDiagGroup,
       "diagType": diagType,
       "diagDeviceSlotNum": diagDeviceSlotNum,
       "diagDevPortNum": diagDevPortNum,
       "diagStartCmd": diagStartCmd,
       "diagResultsTable": diagResultsTable,
       "diagResultsEntry": diagResultsEntry,
       "diagRsltIndex": diagRsltIndex,
       "diagRsltStartTimeStamp": diagRsltStartTimeStamp,
       "diagRsltCompleteTimeStamp": diagRsltCompleteTimeStamp,
       "diagRsltDesc": diagRsltDesc,
       "diagRsltType": diagRsltType,
       "diagRsltDeviceSlotNum": diagRsltDeviceSlotNum,
       "diagRsltDevicePortNum": diagRsltDevicePortNum,
       "diagStartedTrap": diagStartedTrap,
       "diagCompleteTrap": diagCompleteTrap,
       "diagRsltID": diagRsltID,
       "diagRsltAcknowledge": diagRsltAcknowledge,
       "diagStartedTrapAck": diagStartedTrapAck,
       "diagCompleteTrapAck": diagCompleteTrapAck,
       "diagStartedTrapAckSource": diagStartedTrapAckSource,
       "diagCompleteTrapAckSource": diagCompleteTrapAckSource,
       "policyProvisioning": policyProvisioning,
       "activeImgName": activeImgName,
       "activeImgPidSideAFilename": activeImgPidSideAFilename,
       "activeImgPidSideBFilename": activeImgPidSideBFilename,
       "activeImgDwnldTimeStamp": activeImgDwnldTimeStamp,
       "activeImgBuildStartTimeStamp": activeImgBuildStartTimeStamp,
       "activeImgBuildCompleteTimeStamp": activeImgBuildCompleteTimeStamp,
       "activeImgActivatedTimeStamp": activeImgActivatedTimeStamp,
       "commitImgName": commitImgName,
       "commitImgDwnldTimeStamp": commitImgDwnldTimeStamp,
       "commitImgBuildStartTimeStamp": commitImgBuildStartTimeStamp,
       "commitImgBuildCompleteTimeStamp": commitImgBuildCompleteTimeStamp,
       "commitImgActivatedTimeStamp": commitImgActivatedTimeStamp,
       "commitImgTimeStamp": commitImgTimeStamp,
       "newActiveImgTrap": newActiveImgTrap,
       "newCommittedImgTrap": newCommittedImgTrap,
       "nextImgName": nextImgName,
       "nextImgState": nextImgState,
       "nextImgDwnldTimeStamp": nextImgDwnldTimeStamp,
       "nextImgBuildStartTimeStamp": nextImgBuildStartTimeStamp,
       "nextImgBuildCompleteTimeStamp": nextImgBuildCompleteTimeStamp,
       "buildStartedTrap": buildStartedTrap,
       "buildCompleteTrap": buildCompleteTrap,
       "newNextTrap": newNextTrap,
       "newActiveImgTrapAck": newActiveImgTrapAck,
       "newCommittedImgTrapAck": newCommittedImgTrapAck,
       "buildStartedTrapAck": buildStartedTrapAck,
       "buildCompleteTrapAck": buildCompleteTrapAck,
       "newNextTrapAck": newNextTrapAck,
       "newActiveImgTrapAckSource": newActiveImgTrapAckSource,
       "newCommittedImgTrapAckSource": newCommittedImgTrapAckSource,
       "buildStartedTrapAckSource": buildStartedTrapAckSource,
       "buildCompleteTrapAckSource": buildCompleteTrapAckSource,
       "newNextTrapAckSource": newNextTrapAckSource,
       "nCiteStaticRoutes": nCiteStaticRoutes,
       "staticRoutesTable": staticRoutesTable,
       "staticRoutesEntry": staticRoutesEntry,
       "staticRouteDest": staticRouteDest,
       "staticRouteNextHop": staticRouteNextHop,
       "staticRouteNetMask": staticRouteNetMask,
       "staticRouteIngressVlanTag": staticRouteIngressVlanTag,
       "staticRouteMetric1": staticRouteMetric1,
       "staticRouteAdminState": staticRouteAdminState,
       "staticRouteIngressProtocol": staticRouteIngressProtocol,
       "staticRouteOperState": staticRouteOperState,
       "staticRouteType": staticRouteType,
       "staticRouteRowStatus": staticRouteRowStatus,
       "staticRouteVrdTag": staticRouteVrdTag,
       "staticRouteEgressVlan": staticRouteEgressVlan,
       "staticRouteChange": staticRouteChange,
       "staticRoutesRefreshNeeded": staticRoutesRefreshNeeded,
       "staticRoutesRefreshTrap": staticRoutesRefreshTrap,
       "staticRouteChangeTrapAck": staticRouteChangeTrapAck,
       "staticRouteRefreshTrapAck": staticRouteRefreshTrapAck,
       "staticRouteChangeTrapAckSource": staticRouteChangeTrapAckSource,
       "staticRouteRefreshTrapAckSource": staticRouteRefreshTrapAckSource,
       "nCiteArpConfig": nCiteArpConfig,
       "arpVerifTimerRetryCount": arpVerifTimerRetryCount,
       "arpNextHopIP": arpNextHopIP,
       "arpMacAddr": arpMacAddr,
       "arpRefreshNeeded": arpRefreshNeeded,
       "arpRefreshTrap": arpRefreshTrap,
       "arpRefreshTrapAck": arpRefreshTrapAck,
       "arpUpdateMacTrap": arpUpdateMacTrap,
       "arpUpdateMacTrapAck": arpUpdateMacTrapAck,
       "arpTrapOper": arpTrapOper,
       "arpOperTimerFreq": arpOperTimerFreq,
       "arpOperTimerRetryCount": arpOperTimerRetryCount,
       "arpVerifTimerChangeTrap": arpVerifTimerChangeTrap,
       "arpVerifTimerChangeTrapAck": arpVerifTimerChangeTrapAck,
       "arpOperTimerChangeTrap": arpOperTimerChangeTrap,
       "arpOperTimerChangeTrapAck": arpOperTimerChangeTrapAck,
       "arpRefreshTrapAckSource": arpRefreshTrapAckSource,
       "arpUpdateMacTrapAckSource": arpUpdateMacTrapAckSource,
       "arpVerifTimerChangeTrapAckSource": arpVerifTimerChangeTrapAckSource,
       "arpOperTimerChangeTrapAckSource": arpOperTimerChangeTrapAckSource,
       "ipPortConfig": ipPortConfig,
       "ipPortConfigTable": ipPortConfigTable,
       "ipPortConfigEntry": ipPortConfigEntry,
       "ipPortConfigSlotNum": ipPortConfigSlotNum,
       "ipPortConfigPortNum": ipPortConfigPortNum,
       "ipPortConfigIpAddr": ipPortConfigIpAddr,
       "ipPortVlanTag": ipPortVlanTag,
       "ipPortConfigNetMask": ipPortConfigNetMask,
       "ipPortConfigAdminState": ipPortConfigAdminState,
       "ipPortConfigOperState": ipPortConfigOperState,
       "ipPortRowStatus": ipPortRowStatus,
       "ipPortVrdTag": ipPortVrdTag,
       "ipPortConfigChangeTrap": ipPortConfigChangeTrap,
       "ipPortConfigChangeTrapAck": ipPortConfigChangeTrapAck,
       "ipPortPlaceHolder": ipPortPlaceHolder,
       "ipPortRefreshOpStates": ipPortRefreshOpStates,
       "ipPortRefreshTrap": ipPortRefreshTrap,
       "ipPortRefreshTrapAck": ipPortRefreshTrapAck,
       "ipPortAutoNegTable": ipPortAutoNegTable,
       "ipPortAutoNegEntry": ipPortAutoNegEntry,
       "ipPortAutoNegSlotNum": ipPortAutoNegSlotNum,
       "ipPortAutoNegPortNum": ipPortAutoNegPortNum,
       "ipPortAutoNegFlag": ipPortAutoNegFlag,
       "ipPortAutoNegChangeTrap": ipPortAutoNegChangeTrap,
       "ipPortAutoNegChangeTrapAck": ipPortAutoNegChangeTrapAck,
       "ipPortConfigChangeTrapAckSource": ipPortConfigChangeTrapAckSource,
       "ipPortRefreshTrapAckSource": ipPortRefreshTrapAckSource,
       "ipPortAutoNegChangeTrapAckSource": ipPortAutoNegChangeTrapAckSource,
       "nCiteOutSyncFlag": nCiteOutSyncFlag,
       "trapAckEnable": trapAckEnable,
       "linkUpTrapAck": linkUpTrapAck,
       "linkDownTrapAck": linkDownTrapAck,
       "nCiteNTA": nCiteNTA,
       "nCiteNTATable": nCiteNTATable,
       "nCiteNTAEntry": nCiteNTAEntry,
       "nCiteNTACustomerId": nCiteNTACustomerId,
       "nCiteNTAStatus": nCiteNTAStatus,
       "nCiteNTAReset": nCiteNTAReset,
       "nCiteRogue": nCiteRogue,
       "edrQuarantineListTable": edrQuarantineListTable,
       "edrQuarantineListEntry": edrQuarantineListEntry,
       "erdQLUniqueId": erdQLUniqueId,
       "edrQLCallId": edrQLCallId,
       "edrQLTimestamp": edrQLTimestamp,
       "edrQLFrom": edrQLFrom,
       "edrQLTo": edrQLTo,
       "edrQLRequestURI": edrQLRequestURI,
       "edrQLSrcMediaIpPort": edrQLSrcMediaIpPort,
       "edrQLDestMediaAnchorIpPort": edrQLDestMediaAnchorIpPort,
       "edrQLDestMediaIpPort": edrQLDestMediaIpPort,
       "edrQLRogueStatus": edrQLRogueStatus,
       "edrQLPerformGarbageCollection": edrQLPerformGarbageCollection,
       "erdQL2SrcMediaIpPort": erdQL2SrcMediaIpPort,
       "erdQL2DestMediaAnchorIpPort": erdQL2DestMediaAnchorIpPort,
       "erdQL2DestMediaIpPort": erdQL2DestMediaIpPort,
       "edrGarbageCollectionState": edrGarbageCollectionState,
       "edrLastGarbageCollection": edrLastGarbageCollection,
       "edrNextTrafficCheck": edrNextTrafficCheck,
       "edrPerformGarbageCollection": edrPerformGarbageCollection,
       "edrGarbageCollectionStatus": edrGarbageCollectionStatus,
       "edrGarbageCollectionComplete": edrGarbageCollectionComplete,
       "edrGarbageCollectionCompleteTrapAck": edrGarbageCollectionCompleteTrapAck,
       "lrdTable": lrdTable,
       "lrdEntry": lrdEntry,
       "lrdUniqueId": lrdUniqueId,
       "lrdCallId": lrdCallId,
       "lrdRequestURI": lrdRequestURI,
       "lrdFrom": lrdFrom,
       "lrdTo": lrdTo,
       "lrdCallerState": lrdCallerState,
       "lrdCallerMediaAnchorIPPort": lrdCallerMediaAnchorIPPort,
       "lrdCallerDestIPPort": lrdCallerDestIPPort,
       "lrdCallerSourceIPPort1": lrdCallerSourceIPPort1,
       "lrdCallerSourceIPPort2": lrdCallerSourceIPPort2,
       "lrdCallerReason": lrdCallerReason,
       "lrdCallerTimeDetect": lrdCallerTimeDetect,
       "lrdCalleeState": lrdCalleeState,
       "lrdCalleeMediaAnchorIPPort": lrdCalleeMediaAnchorIPPort,
       "lrdCalleeDestIPPort": lrdCalleeDestIPPort,
       "lrdCalleeSourceIPPort1": lrdCalleeSourceIPPort1,
       "lrdCalleeSourceIPPort2": lrdCalleeSourceIPPort2,
       "lrdCalleeReason": lrdCalleeReason,
       "lrdCalleeTimeDetect": lrdCalleeTimeDetect,
       "edrGarbageCollectionCompleteTrapAckSource": edrGarbageCollectionCompleteTrapAckSource,
       "licenseInfo": licenseInfo,
       "licenseTable": licenseTable,
       "licenseEntry": licenseEntry,
       "licenseIndex": licenseIndex,
       "licenseFeatureName": licenseFeatureName,
       "licenseValue": licenseValue,
       "licenseInstallDate": licenseInstallDate,
       "licenseExpirationDate": licenseExpirationDate,
       "licenseFeatureDisplayName": licenseFeatureDisplayName,
       "licenseFileName": licenseFileName,
       "licenseFileChangeTrap": licenseFileChangeTrap,
       "licenseFileChangeTrapAck": licenseFileChangeTrapAck,
       "licenseFileChangeTrapAckSource": licenseFileChangeTrapAckSource,
       "nCiteRIPConfig": nCiteRIPConfig,
       "nCiteRipState": nCiteRipState,
       "nCiteRipPortConfigTable": nCiteRipPortConfigTable,
       "nCiteRipPortConfigEntry": nCiteRipPortConfigEntry,
       "nCiteRipPortSlotNum": nCiteRipPortSlotNum,
       "nCiteRipPortNum": nCiteRipPortNum,
       "nCiteRipPortPrimary": nCiteRipPortPrimary,
       "nCiteRipInterfacesTable": nCiteRipInterfacesTable,
       "nCiteRipInterfacesEntry": nCiteRipInterfacesEntry,
       "nCiteRipInterafacesSlotNum": nCiteRipInterafacesSlotNum,
       "nCiteRipInterfacesPortNum": nCiteRipInterfacesPortNum,
       "nCiteRipInterfacesIPAddr": nCiteRipInterfacesIPAddr,
       "nCiteAuthConfig": nCiteAuthConfig,
       "authConfigLocalOverride": authConfigLocalOverride,
       "authConfigRadiusRetryCount": authConfigRadiusRetryCount,
       "authConfigRadiusRetryInterval": authConfigRadiusRetryInterval,
       "authConfigRadiusServersTable": authConfigRadiusServersTable,
       "authConfigRadiusServersEntry": authConfigRadiusServersEntry,
       "authConfigRadiusServerIp": authConfigRadiusServerIp,
       "authConfigRadiusServerPort": authConfigRadiusServerPort,
       "authConfigRadiusServerPriority": authConfigRadiusServerPriority,
       "linkUpTrapAckSource": linkUpTrapAckSource,
       "linkDownTrapAckSource": linkDownTrapAckSource,
       "nrObjectIDs": nrObjectIDs,
       "nrSessionBorderController": nrSessionBorderController,
       "nrSBCSE": nrSBCSE,
       "nrSBCwNcp": nrSBCwNcp,
       "nrSBCwNte": nrSBCwNte,
       "nrSBCDE": nrSBCDE}
)
