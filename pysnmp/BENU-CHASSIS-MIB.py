# SNMP MIB module (BENU-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BENU-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:50 2024
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

(benuPlatform,) = mibBuilder.importSymbols(
    "BENU-PLATFORM-MIB",
    "benuPlatform")

(ifAdminStatus,
 ifDescr,
 ifIndex,
 ifOperStatus,
 ifType) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAdminStatus",
    "ifDescr",
    "ifIndex",
    "ifOperStatus",
    "ifType")

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


# MODULE-IDENTITY

benuChassisMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1)
)
benuChassisMIB.setRevisions(
        ("2016-11-18 00:00",
         "2016-10-14 00:00",
         "2016-01-26 00:00",
         "2015-10-14 00:00",
         "2015-01-27 00:00",
         "2015-01-05 00:00",
         "2014-11-14 00:00",
         "2014-06-27 00:00",
         "2013-11-25 00:00",
         "2012-12-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BenuChassisNotifObjects_ObjectIdentity = ObjectIdentity
benuChassisNotifObjects = _BenuChassisNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 0)
)
_BenuChassisMIBObjects_ObjectIdentity = ObjectIdentity
benuChassisMIBObjects = _BenuChassisMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1)
)
_BenuChassisInfo_ObjectIdentity = ObjectIdentity
benuChassisInfo = _BenuChassisInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 1)
)


class _BenuChassisType_Type(Integer32):
    """Custom type benuChassisType based on Integer32"""
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
        *(("meg100", 1),
          ("meg1200", 3),
          ("meg400", 2),
          ("meg50", 4),
          ("xMEG10", 6),
          ("xMEG100", 5))
    )


_BenuChassisType_Type.__name__ = "Integer32"
_BenuChassisType_Object = MibScalar
benuChassisType = _BenuChassisType_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 1, 1),
    _BenuChassisType_Type()
)
benuChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuChassisType.setStatus("current")
_BenuChassisHwVersion_Type = DisplayString
_BenuChassisHwVersion_Object = MibScalar
benuChassisHwVersion = _BenuChassisHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 1, 2),
    _BenuChassisHwVersion_Type()
)
benuChassisHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuChassisHwVersion.setStatus("current")
_BenuChassisId_Type = DisplayString
_BenuChassisId_Object = MibScalar
benuChassisId = _BenuChassisId_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 1, 3),
    _BenuChassisId_Type()
)
benuChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuChassisId.setStatus("current")
_BenuChassisNumOfSlots_Type = Integer32
_BenuChassisNumOfSlots_Object = MibScalar
benuChassisNumOfSlots = _BenuChassisNumOfSlots_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 1, 4),
    _BenuChassisNumOfSlots_Type()
)
benuChassisNumOfSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuChassisNumOfSlots.setStatus("current")


class _BenuChassisPowerTrapEnable_Type(Integer32):
    """Custom type benuChassisPowerTrapEnable based on Integer32"""
    defaultValue = 1

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


_BenuChassisPowerTrapEnable_Type.__name__ = "Integer32"
_BenuChassisPowerTrapEnable_Object = MibScalar
benuChassisPowerTrapEnable = _BenuChassisPowerTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 1, 5),
    _BenuChassisPowerTrapEnable_Type()
)
benuChassisPowerTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    benuChassisPowerTrapEnable.setStatus("current")


class _BenuChassisFanTrapEnable_Type(Integer32):
    """Custom type benuChassisFanTrapEnable based on Integer32"""
    defaultValue = 1

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


_BenuChassisFanTrapEnable_Type.__name__ = "Integer32"
_BenuChassisFanTrapEnable_Object = MibScalar
benuChassisFanTrapEnable = _BenuChassisFanTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 1, 6),
    _BenuChassisFanTrapEnable_Type()
)
benuChassisFanTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    benuChassisFanTrapEnable.setStatus("current")


class _BenuChassisSensorTrapEnable_Type(Integer32):
    """Custom type benuChassisSensorTrapEnable based on Integer32"""
    defaultValue = 1

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


_BenuChassisSensorTrapEnable_Type.__name__ = "Integer32"
_BenuChassisSensorTrapEnable_Object = MibScalar
benuChassisSensorTrapEnable = _BenuChassisSensorTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 1, 7),
    _BenuChassisSensorTrapEnable_Type()
)
benuChassisSensorTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    benuChassisSensorTrapEnable.setStatus("current")
_BenuSysUpTimeAtLastChassisChange_Type = TimeTicks
_BenuSysUpTimeAtLastChassisChange_Object = MibScalar
benuSysUpTimeAtLastChassisChange = _BenuSysUpTimeAtLastChassisChange_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 1, 8),
    _BenuSysUpTimeAtLastChassisChange_Type()
)
benuSysUpTimeAtLastChassisChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuSysUpTimeAtLastChassisChange.setStatus("current")
_BenuCardInfo_ObjectIdentity = ObjectIdentity
benuCardInfo = _BenuCardInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 2)
)
_BenuCardTable_Object = MibTable
benuCardTable = _BenuCardTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    benuCardTable.setStatus("current")
_BenuCardEntry_Object = MibTableRow
benuCardEntry = _BenuCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 2, 1, 1)
)
benuCardEntry.setIndexNames(
    (0, "BENU-CHASSIS-MIB", "benuCardIndex"),
)
if mibBuilder.loadTexts:
    benuCardEntry.setStatus("current")


class _BenuCardIndex_Type(Unsigned32):
    """Custom type benuCardIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_BenuCardIndex_Type.__name__ = "Unsigned32"
_BenuCardIndex_Object = MibTableColumn
benuCardIndex = _BenuCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 2, 1, 1, 1),
    _BenuCardIndex_Type()
)
benuCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    benuCardIndex.setStatus("current")


class _BenuCardType_Type(Integer32):
    """Custom type benuCardType based on Integer32"""
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
        *(("inputOutputCard", 5),
          ("rsm", 1),
          ("seFP", 4),
          ("shelfmgr", 3),
          ("switchFabric", 2),
          ("switchMesh", 6),
          ("unknown", 0),
          ("xmeg", 7))
    )


_BenuCardType_Type.__name__ = "Integer32"
_BenuCardType_Object = MibTableColumn
benuCardType = _BenuCardType_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 2, 1, 1, 2),
    _BenuCardType_Type()
)
benuCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuCardType.setStatus("current")
_BenuCardDescr_Type = DisplayString
_BenuCardDescr_Object = MibTableColumn
benuCardDescr = _BenuCardDescr_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 2, 1, 1, 3),
    _BenuCardDescr_Type()
)
benuCardDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuCardDescr.setStatus("current")
_BenuCardSerial_Type = DisplayString
_BenuCardSerial_Object = MibTableColumn
benuCardSerial = _BenuCardSerial_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 2, 1, 1, 4),
    _BenuCardSerial_Type()
)
benuCardSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuCardSerial.setStatus("current")
_BenuCardPartNumber_Type = DisplayString
_BenuCardPartNumber_Object = MibTableColumn
benuCardPartNumber = _BenuCardPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 2, 1, 1, 5),
    _BenuCardPartNumber_Type()
)
benuCardPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuCardPartNumber.setStatus("current")
_BenuCardHwVersion_Type = DisplayString
_BenuCardHwVersion_Object = MibTableColumn
benuCardHwVersion = _BenuCardHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 2, 1, 1, 6),
    _BenuCardHwVersion_Type()
)
benuCardHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuCardHwVersion.setStatus("current")
_BenuCardSwVersion_Type = DisplayString
_BenuCardSwVersion_Object = MibTableColumn
benuCardSwVersion = _BenuCardSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 2, 1, 1, 7),
    _BenuCardSwVersion_Type()
)
benuCardSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuCardSwVersion.setStatus("current")
_BenuCardSlotNumber_Type = Integer32
_BenuCardSlotNumber_Object = MibTableColumn
benuCardSlotNumber = _BenuCardSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 2, 1, 1, 8),
    _BenuCardSlotNumber_Type()
)
benuCardSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuCardSlotNumber.setStatus("current")
_BenuCardRamSize_Type = Integer32
_BenuCardRamSize_Object = MibTableColumn
benuCardRamSize = _BenuCardRamSize_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 2, 1, 1, 9),
    _BenuCardRamSize_Type()
)
benuCardRamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuCardRamSize.setStatus("current")
_BenuCardPrimaryDiskSize_Type = Integer32
_BenuCardPrimaryDiskSize_Object = MibTableColumn
benuCardPrimaryDiskSize = _BenuCardPrimaryDiskSize_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 2, 1, 1, 10),
    _BenuCardPrimaryDiskSize_Type()
)
benuCardPrimaryDiskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuCardPrimaryDiskSize.setStatus("current")
_BenuCardSecondaryDiskSize_Type = Integer32
_BenuCardSecondaryDiskSize_Object = MibTableColumn
benuCardSecondaryDiskSize = _BenuCardSecondaryDiskSize_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 2, 1, 1, 11),
    _BenuCardSecondaryDiskSize_Type()
)
benuCardSecondaryDiskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuCardSecondaryDiskSize.setStatus("current")


class _BenuCardOperStatus_Type(Integer32):
    """Custom type benuCardOperStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("boot", 8),
          ("config", 9),
          ("diag", 7),
          ("down", 3),
          ("flash", 6),
          ("notSpecified", 1),
          ("rom", 5),
          ("standby", 4),
          ("up", 2))
    )


_BenuCardOperStatus_Type.__name__ = "Integer32"
_BenuCardOperStatus_Object = MibTableColumn
benuCardOperStatus = _BenuCardOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 2, 1, 1, 12),
    _BenuCardOperStatus_Type()
)
benuCardOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuCardOperStatus.setStatus("current")
_BenuCardIfInfo_ObjectIdentity = ObjectIdentity
benuCardIfInfo = _BenuCardIfInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 3)
)
_BenuCardIfIndexTable_Object = MibTable
benuCardIfIndexTable = _BenuCardIfIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    benuCardIfIndexTable.setStatus("current")
_BenuCardIfIndexEntry_Object = MibTableRow
benuCardIfIndexEntry = _BenuCardIfIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 3, 1, 1)
)
benuCardIfIndexEntry.setIndexNames(
    (0, "BENU-CHASSIS-MIB", "benuCardIfIndex"),
)
if mibBuilder.loadTexts:
    benuCardIfIndexEntry.setStatus("current")
_BenuCardIfIndex_Type = Unsigned32
_BenuCardIfIndex_Object = MibTableColumn
benuCardIfIndex = _BenuCardIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 3, 1, 1, 1),
    _BenuCardIfIndex_Type()
)
benuCardIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    benuCardIfIndex.setStatus("current")
_BenuCardIfName_Type = DisplayString
_BenuCardIfName_Object = MibTableColumn
benuCardIfName = _BenuCardIfName_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 3, 1, 1, 2),
    _BenuCardIfName_Type()
)
benuCardIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuCardIfName.setStatus("current")
_BenuCardIfPortNumber_Type = Integer32
_BenuCardIfPortNumber_Object = MibTableColumn
benuCardIfPortNumber = _BenuCardIfPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 3, 1, 1, 3),
    _BenuCardIfPortNumber_Type()
)
benuCardIfPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuCardIfPortNumber.setStatus("current")
_BenuCardIfSlotNumber_Type = Integer32
_BenuCardIfSlotNumber_Object = MibTableColumn
benuCardIfSlotNumber = _BenuCardIfSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 3, 1, 1, 4),
    _BenuCardIfSlotNumber_Type()
)
benuCardIfSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuCardIfSlotNumber.setStatus("current")


class _BenuCardIfLinkUpDownEnable_Type(Integer32):
    """Custom type benuCardIfLinkUpDownEnable based on Integer32"""
    defaultValue = 2

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


_BenuCardIfLinkUpDownEnable_Type.__name__ = "Integer32"
_BenuCardIfLinkUpDownEnable_Object = MibTableColumn
benuCardIfLinkUpDownEnable = _BenuCardIfLinkUpDownEnable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 3, 1, 1, 5),
    _BenuCardIfLinkUpDownEnable_Type()
)
benuCardIfLinkUpDownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    benuCardIfLinkUpDownEnable.setStatus("current")


class _BenuCardIfPortType_Type(Integer32):
    """Custom type benuCardIfPortType based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 9),
          ("cable", 8),
          ("ethernet", 1),
          ("fastEthernet", 2),
          ("gigaEthernet", 3),
          ("ip", 10),
          ("ipGre", 5),
          ("l2tp", 7),
          ("lag", 15),
          ("loopback", 13),
          ("max", 16),
          ("multiBind", 11),
          ("multiBindLastResort", 14),
          ("none", 0),
          ("p2p", 12),
          ("tunnel", 4),
          ("vlan", 6))
    )


_BenuCardIfPortType_Type.__name__ = "Integer32"
_BenuCardIfPortType_Object = MibTableColumn
benuCardIfPortType = _BenuCardIfPortType_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 3, 1, 1, 6),
    _BenuCardIfPortType_Type()
)
benuCardIfPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuCardIfPortType.setStatus("current")
_BenuCardIfBindName_Type = DisplayString
_BenuCardIfBindName_Object = MibTableColumn
benuCardIfBindName = _BenuCardIfBindName_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 3, 1, 1, 7),
    _BenuCardIfBindName_Type()
)
benuCardIfBindName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuCardIfBindName.setStatus("current")
_BenuCardIfEncapsulation_Type = DisplayString
_BenuCardIfEncapsulation_Object = MibTableColumn
benuCardIfEncapsulation = _BenuCardIfEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 3, 1, 1, 8),
    _BenuCardIfEncapsulation_Type()
)
benuCardIfEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuCardIfEncapsulation.setStatus("current")


class _BenuCardIfVirtualType_Type(Integer32):
    """Custom type benuCardIfVirtualType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("physical", 1),
          ("virtual", 2))
    )


_BenuCardIfVirtualType_Type.__name__ = "Integer32"
_BenuCardIfVirtualType_Object = MibTableColumn
benuCardIfVirtualType = _BenuCardIfVirtualType_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 3, 1, 1, 9),
    _BenuCardIfVirtualType_Type()
)
benuCardIfVirtualType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuCardIfVirtualType.setStatus("current")
_BenuSensorInfo_ObjectIdentity = ObjectIdentity
benuSensorInfo = _BenuSensorInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 4)
)
_BenuSensorTable_Object = MibTable
benuSensorTable = _BenuSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    benuSensorTable.setStatus("current")
_BenuSensorEntry_Object = MibTableRow
benuSensorEntry = _BenuSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 4, 1, 1)
)
benuSensorEntry.setIndexNames(
    (0, "BENU-CHASSIS-MIB", "benuSensorCardIndex"),
    (0, "BENU-CHASSIS-MIB", "benuSensorIndex"),
)
if mibBuilder.loadTexts:
    benuSensorEntry.setStatus("current")
_BenuSensorCardIndex_Type = Unsigned32
_BenuSensorCardIndex_Object = MibTableColumn
benuSensorCardIndex = _BenuSensorCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 4, 1, 1, 1),
    _BenuSensorCardIndex_Type()
)
benuSensorCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    benuSensorCardIndex.setStatus("current")
_BenuSensorIndex_Type = Unsigned32
_BenuSensorIndex_Object = MibTableColumn
benuSensorIndex = _BenuSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 4, 1, 1, 2),
    _BenuSensorIndex_Type()
)
benuSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    benuSensorIndex.setStatus("current")
_BenuSensorName_Type = DisplayString
_BenuSensorName_Object = MibTableColumn
benuSensorName = _BenuSensorName_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 4, 1, 1, 3),
    _BenuSensorName_Type()
)
benuSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuSensorName.setStatus("current")


class _BenuSensorType_Type(Integer32):
    """Custom type benuSensorType based on Integer32"""
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
        *(("electicCurrent", 3),
          ("fan", 4),
          ("other", 0),
          ("power", 5),
          ("temparature", 1),
          ("voltage", 2))
    )


_BenuSensorType_Type.__name__ = "Integer32"
_BenuSensorType_Object = MibTableColumn
benuSensorType = _BenuSensorType_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 4, 1, 1, 4),
    _BenuSensorType_Type()
)
benuSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuSensorType.setStatus("current")
_BenuSensorValue_Type = Integer32
_BenuSensorValue_Object = MibTableColumn
benuSensorValue = _BenuSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 4, 1, 1, 5),
    _BenuSensorValue_Type()
)
benuSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuSensorValue.setStatus("current")
_BenuSensorMinThresh_Type = Integer32
_BenuSensorMinThresh_Object = MibTableColumn
benuSensorMinThresh = _BenuSensorMinThresh_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 4, 1, 1, 6),
    _BenuSensorMinThresh_Type()
)
benuSensorMinThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuSensorMinThresh.setStatus("current")
_BenuSensorMaxThresh_Type = Integer32
_BenuSensorMaxThresh_Object = MibTableColumn
benuSensorMaxThresh = _BenuSensorMaxThresh_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 4, 1, 1, 7),
    _BenuSensorMaxThresh_Type()
)
benuSensorMaxThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuSensorMaxThresh.setStatus("current")


class _BenuSensorState_Type(Integer32):
    """Custom type benuSensorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("critical", 2),
          ("normal", 1),
          ("other", 0))
    )


_BenuSensorState_Type.__name__ = "Integer32"
_BenuSensorState_Object = MibTableColumn
benuSensorState = _BenuSensorState_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 4, 1, 1, 8),
    _BenuSensorState_Type()
)
benuSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuSensorState.setStatus("current")
_BenuSensorId_Type = Integer32
_BenuSensorId_Object = MibTableColumn
benuSensorId = _BenuSensorId_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 4, 1, 1, 9),
    _BenuSensorId_Type()
)
benuSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuSensorId.setStatus("current")
_BenuChassisGeneralInfo_ObjectIdentity = ObjectIdentity
benuChassisGeneralInfo = _BenuChassisGeneralInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 5)
)
_BenuSysUpTimeSinceLastConfigChange_Type = TimeTicks
_BenuSysUpTimeSinceLastConfigChange_Object = MibScalar
benuSysUpTimeSinceLastConfigChange = _BenuSysUpTimeSinceLastConfigChange_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 5, 1),
    _BenuSysUpTimeSinceLastConfigChange_Type()
)
benuSysUpTimeSinceLastConfigChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuSysUpTimeSinceLastConfigChange.setStatus("current")
_BenuFanInfo_ObjectIdentity = ObjectIdentity
benuFanInfo = _BenuFanInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 6)
)
_BenuFanTable_Object = MibTable
benuFanTable = _BenuFanTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    benuFanTable.setStatus("current")
_BenuFanEntry_Object = MibTableRow
benuFanEntry = _BenuFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 6, 1, 1)
)
benuFanEntry.setIndexNames(
    (0, "BENU-CHASSIS-MIB", "benuFanCardIndex"),
)
if mibBuilder.loadTexts:
    benuFanEntry.setStatus("current")
_BenuFanCardIndex_Type = Unsigned32
_BenuFanCardIndex_Object = MibTableColumn
benuFanCardIndex = _BenuFanCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 6, 1, 1, 1),
    _BenuFanCardIndex_Type()
)
benuFanCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    benuFanCardIndex.setStatus("current")
_BenuFanMaxSpeed_Type = Unsigned32
_BenuFanMaxSpeed_Object = MibTableColumn
benuFanMaxSpeed = _BenuFanMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 6, 1, 1, 2),
    _BenuFanMaxSpeed_Type()
)
benuFanMaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuFanMaxSpeed.setStatus("current")
_BenuFanCurSpeed_Type = Unsigned32
_BenuFanCurSpeed_Object = MibTableColumn
benuFanCurSpeed = _BenuFanCurSpeed_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 6, 1, 1, 3),
    _BenuFanCurSpeed_Type()
)
benuFanCurSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuFanCurSpeed.setStatus("current")
_BenuFanStatus_Type = Integer32
_BenuFanStatus_Object = MibTableColumn
benuFanStatus = _BenuFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 6, 1, 1, 4),
    _BenuFanStatus_Type()
)
benuFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuFanStatus.setStatus("current")
_BenuPowerSupplyInfo_ObjectIdentity = ObjectIdentity
benuPowerSupplyInfo = _BenuPowerSupplyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 7)
)
_BenuPowerSupplyTable_Object = MibTable
benuPowerSupplyTable = _BenuPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    benuPowerSupplyTable.setStatus("current")
_BenuPowerSupplyEntry_Object = MibTableRow
benuPowerSupplyEntry = _BenuPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 7, 1, 1)
)
benuPowerSupplyEntry.setIndexNames(
    (0, "BENU-CHASSIS-MIB", "benuPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    benuPowerSupplyEntry.setStatus("current")


class _BenuPowerSupplyIndex_Type(Integer32):
    """Custom type benuPowerSupplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerA", 1),
          ("powerB", 2))
    )


_BenuPowerSupplyIndex_Type.__name__ = "Integer32"
_BenuPowerSupplyIndex_Object = MibTableColumn
benuPowerSupplyIndex = _BenuPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 7, 1, 1, 1),
    _BenuPowerSupplyIndex_Type()
)
benuPowerSupplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    benuPowerSupplyIndex.setStatus("current")
_BenuPowerSupplyName_Type = DisplayString
_BenuPowerSupplyName_Object = MibTableColumn
benuPowerSupplyName = _BenuPowerSupplyName_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 7, 1, 1, 2),
    _BenuPowerSupplyName_Type()
)
benuPowerSupplyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuPowerSupplyName.setStatus("current")


class _BenuPowerSupplyPresent_Type(Integer32):
    """Custom type benuPowerSupplyPresent based on Integer32"""
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


_BenuPowerSupplyPresent_Type.__name__ = "Integer32"
_BenuPowerSupplyPresent_Object = MibTableColumn
benuPowerSupplyPresent = _BenuPowerSupplyPresent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 7, 1, 1, 3),
    _BenuPowerSupplyPresent_Type()
)
benuPowerSupplyPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuPowerSupplyPresent.setStatus("current")


class _BenuPowerSupplyType_Type(Integer32):
    """Custom type benuPowerSupplyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ac", 1),
          ("dc", 2),
          ("notApplicable", 3))
    )


_BenuPowerSupplyType_Type.__name__ = "Integer32"
_BenuPowerSupplyType_Object = MibTableColumn
benuPowerSupplyType = _BenuPowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 7, 1, 1, 4),
    _BenuPowerSupplyType_Type()
)
benuPowerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuPowerSupplyType.setStatus("current")


class _BenuPowerSupplyPowered_Type(Integer32):
    """Custom type benuPowerSupplyPowered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 3),
          ("notPowered", 2),
          ("powered", 1))
    )


_BenuPowerSupplyPowered_Type.__name__ = "Integer32"
_BenuPowerSupplyPowered_Object = MibTableColumn
benuPowerSupplyPowered = _BenuPowerSupplyPowered_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 1, 7, 1, 1, 5),
    _BenuPowerSupplyPowered_Type()
)
benuPowerSupplyPowered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    benuPowerSupplyPowered.setStatus("current")
_BenuChassisNotifVariables_ObjectIdentity = ObjectIdentity
benuChassisNotifVariables = _BenuChassisNotifVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 2)
)


class _BenuChassisPowerFailureInfo_Type(Integer32):
    """Custom type benuChassisPowerFailureInfo based on Integer32"""
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
        *(("powerFailureA", 1),
          ("powerFailureB", 2),
          ("powerRestoredA", 3),
          ("powerRestoredB", 4))
    )


_BenuChassisPowerFailureInfo_Type.__name__ = "Integer32"
_BenuChassisPowerFailureInfo_Object = MibScalar
benuChassisPowerFailureInfo = _BenuChassisPowerFailureInfo_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 2, 1),
    _BenuChassisPowerFailureInfo_Type()
)
benuChassisPowerFailureInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    benuChassisPowerFailureInfo.setStatus("obsolete")
_BenuChassisFanFailureInfo_Type = DisplayString
_BenuChassisFanFailureInfo_Object = MibScalar
benuChassisFanFailureInfo = _BenuChassisFanFailureInfo_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 2, 2),
    _BenuChassisFanFailureInfo_Type()
)
benuChassisFanFailureInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    benuChassisFanFailureInfo.setStatus("current")
_BenuChassisPowerFailureCardInfo_Type = Unsigned32
_BenuChassisPowerFailureCardInfo_Object = MibScalar
benuChassisPowerFailureCardInfo = _BenuChassisPowerFailureCardInfo_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 2, 3),
    _BenuChassisPowerFailureCardInfo_Type()
)
benuChassisPowerFailureCardInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    benuChassisPowerFailureCardInfo.setStatus("obsolete")


class _BenuChassisPowerInfo_Type(Integer32):
    """Custom type benuChassisPowerInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerSupplyA", 1),
          ("powerSupplyB", 2))
    )


_BenuChassisPowerInfo_Type.__name__ = "Integer32"
_BenuChassisPowerInfo_Object = MibScalar
benuChassisPowerInfo = _BenuChassisPowerInfo_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 2, 4),
    _BenuChassisPowerInfo_Type()
)
benuChassisPowerInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    benuChassisPowerInfo.setStatus("current")

# Managed Objects groups


# Notification objects

benuChassisPowerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 0, 1)
)
benuChassisPowerFailure.setObjects(
      *(("BENU-CHASSIS-MIB", "benuChassisPowerFailureCardInfo"),
        ("BENU-CHASSIS-MIB", "benuChassisPowerFailureInfo"))
)
if mibBuilder.loadTexts:
    benuChassisPowerFailure.setStatus(
        "obsolete"
    )

benuChassisFanFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 0, 2)
)
benuChassisFanFailureTrap.setObjects(
    ("BENU-CHASSIS-MIB", "benuChassisFanFailureInfo")
)
if mibBuilder.loadTexts:
    benuChassisFanFailureTrap.setStatus(
        "current"
    )

benuLinkUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 0, 3)
)
benuLinkUpTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifType"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"))
)
if mibBuilder.loadTexts:
    benuLinkUpTrap.setStatus(
        "current"
    )

benuLinkDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 0, 4)
)
benuLinkDownTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifType"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"))
)
if mibBuilder.loadTexts:
    benuLinkDownTrap.setStatus(
        "current"
    )

benuSensorCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 0, 5)
)
benuSensorCritical.setObjects(
      *(("BENU-CHASSIS-MIB", "benuSensorName"),
        ("BENU-CHASSIS-MIB", "benuSensorType"),
        ("BENU-CHASSIS-MIB", "benuSensorValue"),
        ("BENU-CHASSIS-MIB", "benuSensorId"))
)
if mibBuilder.loadTexts:
    benuSensorCritical.setStatus(
        "current"
    )

benuSensorNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 0, 6)
)
benuSensorNormal.setObjects(
      *(("BENU-CHASSIS-MIB", "benuSensorName"),
        ("BENU-CHASSIS-MIB", "benuSensorType"),
        ("BENU-CHASSIS-MIB", "benuSensorValue"),
        ("BENU-CHASSIS-MIB", "benuSensorId"))
)
if mibBuilder.loadTexts:
    benuSensorNormal.setStatus(
        "current"
    )

benuChassisPowerFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 0, 7)
)
benuChassisPowerFault.setObjects(
    ("BENU-CHASSIS-MIB", "benuChassisPowerInfo")
)
if mibBuilder.loadTexts:
    benuChassisPowerFault.setStatus(
        "current"
    )

benuChassisPowerRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 0, 8)
)
benuChassisPowerRecovery.setObjects(
    ("BENU-CHASSIS-MIB", "benuChassisPowerInfo")
)
if mibBuilder.loadTexts:
    benuChassisPowerRecovery.setStatus(
        "current"
    )

benuChassisPowerPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 0, 9)
)
benuChassisPowerPresent.setObjects(
    ("BENU-CHASSIS-MIB", "benuChassisPowerInfo")
)
if mibBuilder.loadTexts:
    benuChassisPowerPresent.setStatus(
        "current"
    )

benuChassisPowerAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 1, 1, 0, 10)
)
benuChassisPowerAbsent.setObjects(
    ("BENU-CHASSIS-MIB", "benuChassisPowerInfo")
)
if mibBuilder.loadTexts:
    benuChassisPowerAbsent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BENU-CHASSIS-MIB",
    **{"benuChassisMIB": benuChassisMIB,
       "benuChassisNotifObjects": benuChassisNotifObjects,
       "benuChassisPowerFailure": benuChassisPowerFailure,
       "benuChassisFanFailureTrap": benuChassisFanFailureTrap,
       "benuLinkUpTrap": benuLinkUpTrap,
       "benuLinkDownTrap": benuLinkDownTrap,
       "benuSensorCritical": benuSensorCritical,
       "benuSensorNormal": benuSensorNormal,
       "benuChassisPowerFault": benuChassisPowerFault,
       "benuChassisPowerRecovery": benuChassisPowerRecovery,
       "benuChassisPowerPresent": benuChassisPowerPresent,
       "benuChassisPowerAbsent": benuChassisPowerAbsent,
       "benuChassisMIBObjects": benuChassisMIBObjects,
       "benuChassisInfo": benuChassisInfo,
       "benuChassisType": benuChassisType,
       "benuChassisHwVersion": benuChassisHwVersion,
       "benuChassisId": benuChassisId,
       "benuChassisNumOfSlots": benuChassisNumOfSlots,
       "benuChassisPowerTrapEnable": benuChassisPowerTrapEnable,
       "benuChassisFanTrapEnable": benuChassisFanTrapEnable,
       "benuChassisSensorTrapEnable": benuChassisSensorTrapEnable,
       "benuSysUpTimeAtLastChassisChange": benuSysUpTimeAtLastChassisChange,
       "benuCardInfo": benuCardInfo,
       "benuCardTable": benuCardTable,
       "benuCardEntry": benuCardEntry,
       "benuCardIndex": benuCardIndex,
       "benuCardType": benuCardType,
       "benuCardDescr": benuCardDescr,
       "benuCardSerial": benuCardSerial,
       "benuCardPartNumber": benuCardPartNumber,
       "benuCardHwVersion": benuCardHwVersion,
       "benuCardSwVersion": benuCardSwVersion,
       "benuCardSlotNumber": benuCardSlotNumber,
       "benuCardRamSize": benuCardRamSize,
       "benuCardPrimaryDiskSize": benuCardPrimaryDiskSize,
       "benuCardSecondaryDiskSize": benuCardSecondaryDiskSize,
       "benuCardOperStatus": benuCardOperStatus,
       "benuCardIfInfo": benuCardIfInfo,
       "benuCardIfIndexTable": benuCardIfIndexTable,
       "benuCardIfIndexEntry": benuCardIfIndexEntry,
       "benuCardIfIndex": benuCardIfIndex,
       "benuCardIfName": benuCardIfName,
       "benuCardIfPortNumber": benuCardIfPortNumber,
       "benuCardIfSlotNumber": benuCardIfSlotNumber,
       "benuCardIfLinkUpDownEnable": benuCardIfLinkUpDownEnable,
       "benuCardIfPortType": benuCardIfPortType,
       "benuCardIfBindName": benuCardIfBindName,
       "benuCardIfEncapsulation": benuCardIfEncapsulation,
       "benuCardIfVirtualType": benuCardIfVirtualType,
       "benuSensorInfo": benuSensorInfo,
       "benuSensorTable": benuSensorTable,
       "benuSensorEntry": benuSensorEntry,
       "benuSensorCardIndex": benuSensorCardIndex,
       "benuSensorIndex": benuSensorIndex,
       "benuSensorName": benuSensorName,
       "benuSensorType": benuSensorType,
       "benuSensorValue": benuSensorValue,
       "benuSensorMinThresh": benuSensorMinThresh,
       "benuSensorMaxThresh": benuSensorMaxThresh,
       "benuSensorState": benuSensorState,
       "benuSensorId": benuSensorId,
       "benuChassisGeneralInfo": benuChassisGeneralInfo,
       "benuSysUpTimeSinceLastConfigChange": benuSysUpTimeSinceLastConfigChange,
       "benuFanInfo": benuFanInfo,
       "benuFanTable": benuFanTable,
       "benuFanEntry": benuFanEntry,
       "benuFanCardIndex": benuFanCardIndex,
       "benuFanMaxSpeed": benuFanMaxSpeed,
       "benuFanCurSpeed": benuFanCurSpeed,
       "benuFanStatus": benuFanStatus,
       "benuPowerSupplyInfo": benuPowerSupplyInfo,
       "benuPowerSupplyTable": benuPowerSupplyTable,
       "benuPowerSupplyEntry": benuPowerSupplyEntry,
       "benuPowerSupplyIndex": benuPowerSupplyIndex,
       "benuPowerSupplyName": benuPowerSupplyName,
       "benuPowerSupplyPresent": benuPowerSupplyPresent,
       "benuPowerSupplyType": benuPowerSupplyType,
       "benuPowerSupplyPowered": benuPowerSupplyPowered,
       "benuChassisNotifVariables": benuChassisNotifVariables,
       "benuChassisPowerFailureInfo": benuChassisPowerFailureInfo,
       "benuChassisFanFailureInfo": benuChassisFanFailureInfo,
       "benuChassisPowerFailureCardInfo": benuChassisPowerFailureCardInfo,
       "benuChassisPowerInfo": benuChassisPowerInfo}
)
