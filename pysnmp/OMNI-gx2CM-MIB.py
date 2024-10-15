# SNMP MIB module (OMNI-gx2CM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNI-gx2CM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:13 2024
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

(gx2Cm,) = mibBuilder.importSymbols(
    "GX2HFC-MIB",
    "gx2Cm")

(gi,
 motproxies) = mibBuilder.importSymbols(
    "NLS-BBNIDENT-MIB",
    "gi",
    "motproxies")

(trapChangedObjectId,
 trapChangedValueDisplayString,
 trapChangedValueInteger,
 trapIdentifier,
 trapNETrapLastTrapTimeStamp,
 trapNetworkElemAdminState,
 trapNetworkElemAlarmStatus,
 trapNetworkElemAvailStatus,
 trapNetworkElemModelNumber,
 trapNetworkElemOperState,
 trapNetworkElemSerialNum,
 trapPerceivedSeverity,
 trapText) = mibBuilder.importSymbols(
    "NLSBBN-TRAPS-MIB",
    "trapChangedObjectId",
    "trapChangedValueDisplayString",
    "trapChangedValueInteger",
    "trapIdentifier",
    "trapNETrapLastTrapTimeStamp",
    "trapNetworkElemAdminState",
    "trapNetworkElemAlarmStatus",
    "trapNetworkElemAvailStatus",
    "trapNetworkElemModelNumber",
    "trapNetworkElemOperState",
    "trapNetworkElemSerialNum",
    "trapPerceivedSeverity",
    "trapText")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class Float(Counter32):
    """Custom type Float based on Counter32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Gx2cmDescriptor_ObjectIdentity = ObjectIdentity
gx2cmDescriptor = _Gx2cmDescriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 1)
)
_Gx2cmFactoryTable_Object = MibTable
gx2cmFactoryTable = _Gx2cmFactoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    gx2cmFactoryTable.setStatus("mandatory")
_Gx2cmFactoryEntry_Object = MibTableRow
gx2cmFactoryEntry = _Gx2cmFactoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 2, 1)
)
gx2cmFactoryEntry.setIndexNames(
    (0, "OMNI-gx2CM-MIB", "gx2cmFactoryTableIndex"),
)
if mibBuilder.loadTexts:
    gx2cmFactoryEntry.setStatus("mandatory")


class _Gx2cmFactoryTableIndex_Type(Integer32):
    """Custom type gx2cmFactoryTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2cmFactoryTableIndex_Type.__name__ = "Integer32"
_Gx2cmFactoryTableIndex_Object = MibTableColumn
gx2cmFactoryTableIndex = _Gx2cmFactoryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 2, 1, 1),
    _Gx2cmFactoryTableIndex_Type()
)
gx2cmFactoryTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2cmFactoryTableIndex.setStatus("mandatory")
_BootControlByte_Type = Integer32
_BootControlByte_Object = MibTableColumn
bootControlByte = _BootControlByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 2, 1, 2),
    _BootControlByte_Type()
)
bootControlByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootControlByte.setStatus("mandatory")
_BootStatusByte_Type = Integer32
_BootStatusByte_Object = MibTableColumn
bootStatusByte = _BootStatusByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 2, 1, 3),
    _BootStatusByte_Type()
)
bootStatusByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootStatusByte.setStatus("mandatory")
_Bank0CRC_Type = Integer32
_Bank0CRC_Object = MibTableColumn
bank0CRC = _Bank0CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 2, 1, 4),
    _Bank0CRC_Type()
)
bank0CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bank0CRC.setStatus("mandatory")
_Bank1CRC_Type = Integer32
_Bank1CRC_Object = MibTableColumn
bank1CRC = _Bank1CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 2, 1, 5),
    _Bank1CRC_Type()
)
bank1CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bank1CRC.setStatus("mandatory")
_PrgEEPROMByte_Type = Integer32
_PrgEEPROMByte_Object = MibTableColumn
prgEEPROMByte = _PrgEEPROMByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 2, 1, 6),
    _PrgEEPROMByte_Type()
)
prgEEPROMByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prgEEPROMByte.setStatus("mandatory")
_FactoryCRC_Type = Integer32
_FactoryCRC_Object = MibTableColumn
factoryCRC = _FactoryCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 2, 1, 7),
    _FactoryCRC_Type()
)
factoryCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    factoryCRC.setStatus("mandatory")
_CalculateCRC_Type = Integer32
_CalculateCRC_Object = MibTableColumn
calculateCRC = _CalculateCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 2, 1, 8),
    _CalculateCRC_Type()
)
calculateCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calculateCRC.setStatus("mandatory")
_HourMeter_Type = Integer32
_HourMeter_Object = MibTableColumn
hourMeter = _HourMeter_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 2, 1, 9),
    _HourMeter_Type()
)
hourMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hourMeter.setStatus("mandatory")
_FlashPrgCnt0_Type = Integer32
_FlashPrgCnt0_Object = MibTableColumn
flashPrgCnt0 = _FlashPrgCnt0_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 2, 1, 10),
    _FlashPrgCnt0_Type()
)
flashPrgCnt0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashPrgCnt0.setStatus("mandatory")
_FlashPrgCnt1_Type = Integer32
_FlashPrgCnt1_Object = MibTableColumn
flashPrgCnt1 = _FlashPrgCnt1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 2, 1, 11),
    _FlashPrgCnt1_Type()
)
flashPrgCnt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashPrgCnt1.setStatus("mandatory")


class _FlashBank0_Type(DisplayString):
    """Custom type flashBank0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FlashBank0_Type.__name__ = "DisplayString"
_FlashBank0_Object = MibTableColumn
flashBank0 = _FlashBank0_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 2, 1, 12),
    _FlashBank0_Type()
)
flashBank0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashBank0.setStatus("mandatory")


class _FlashBank1_Type(DisplayString):
    """Custom type flashBank1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FlashBank1_Type.__name__ = "DisplayString"
_FlashBank1_Object = MibTableColumn
flashBank1 = _FlashBank1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 2, 1, 13),
    _FlashBank1_Type()
)
flashBank1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashBank1.setStatus("mandatory")


class _LocalMacAdd_Type(DisplayString):
    """Custom type localMacAdd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LocalMacAdd_Type.__name__ = "DisplayString"
_LocalMacAdd_Object = MibTableColumn
localMacAdd = _LocalMacAdd_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 2, 1, 14),
    _LocalMacAdd_Type()
)
localMacAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localMacAdd.setStatus("mandatory")


class _NetWorkMacAdd_Type(DisplayString):
    """Custom type netWorkMacAdd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NetWorkMacAdd_Type.__name__ = "DisplayString"
_NetWorkMacAdd_Object = MibTableColumn
netWorkMacAdd = _NetWorkMacAdd_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 2, 1, 15),
    _NetWorkMacAdd_Type()
)
netWorkMacAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netWorkMacAdd.setStatus("mandatory")
_Gx2cmNetworkTable_Object = MibTable
gx2cmNetworkTable = _Gx2cmNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    gx2cmNetworkTable.setStatus("mandatory")
_Gx2cmNetworkEntry_Object = MibTableRow
gx2cmNetworkEntry = _Gx2cmNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2)
)
gx2cmNetworkEntry.setIndexNames(
    (0, "OMNI-gx2CM-MIB", "gx2cmNetworkTableIndex"),
)
if mibBuilder.loadTexts:
    gx2cmNetworkEntry.setStatus("mandatory")


class _Gx2cmNetworkTableIndex_Type(Integer32):
    """Custom type gx2cmNetworkTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2cmNetworkTableIndex_Type.__name__ = "Integer32"
_Gx2cmNetworkTableIndex_Object = MibTableColumn
gx2cmNetworkTableIndex = _Gx2cmNetworkTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 1),
    _Gx2cmNetworkTableIndex_Type()
)
gx2cmNetworkTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2cmNetworkTableIndex.setStatus("mandatory")


class _LabelLocalEthIPAdd_Type(DisplayString):
    """Custom type labelLocalEthIPAdd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelLocalEthIPAdd_Type.__name__ = "DisplayString"
_LabelLocalEthIPAdd_Object = MibTableColumn
labelLocalEthIPAdd = _LabelLocalEthIPAdd_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 2),
    _LabelLocalEthIPAdd_Type()
)
labelLocalEthIPAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelLocalEthIPAdd.setStatus("optional")


class _ValueLocalEthIPAdd_Type(DisplayString):
    """Custom type valueLocalEthIPAdd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ValueLocalEthIPAdd_Type.__name__ = "DisplayString"
_ValueLocalEthIPAdd_Object = MibTableColumn
valueLocalEthIPAdd = _ValueLocalEthIPAdd_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 3),
    _ValueLocalEthIPAdd_Type()
)
valueLocalEthIPAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueLocalEthIPAdd.setStatus("mandatory")


class _LabelLocalEthMask_Type(DisplayString):
    """Custom type labelLocalEthMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelLocalEthMask_Type.__name__ = "DisplayString"
_LabelLocalEthMask_Object = MibTableColumn
labelLocalEthMask = _LabelLocalEthMask_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 4),
    _LabelLocalEthMask_Type()
)
labelLocalEthMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelLocalEthMask.setStatus("optional")


class _ValueLocalEthMask_Type(DisplayString):
    """Custom type valueLocalEthMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ValueLocalEthMask_Type.__name__ = "DisplayString"
_ValueLocalEthMask_Object = MibTableColumn
valueLocalEthMask = _ValueLocalEthMask_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 5),
    _ValueLocalEthMask_Type()
)
valueLocalEthMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueLocalEthMask.setStatus("mandatory")


class _LabelNetworkEthAdd_Type(DisplayString):
    """Custom type labelNetworkEthAdd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelNetworkEthAdd_Type.__name__ = "DisplayString"
_LabelNetworkEthAdd_Object = MibTableColumn
labelNetworkEthAdd = _LabelNetworkEthAdd_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 6),
    _LabelNetworkEthAdd_Type()
)
labelNetworkEthAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelNetworkEthAdd.setStatus("optional")


class _ValueNetworkEthAdd_Type(DisplayString):
    """Custom type valueNetworkEthAdd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ValueNetworkEthAdd_Type.__name__ = "DisplayString"
_ValueNetworkEthAdd_Object = MibTableColumn
valueNetworkEthAdd = _ValueNetworkEthAdd_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 7),
    _ValueNetworkEthAdd_Type()
)
valueNetworkEthAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueNetworkEthAdd.setStatus("mandatory")


class _LabelNetworkEthMask_Type(DisplayString):
    """Custom type labelNetworkEthMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelNetworkEthMask_Type.__name__ = "DisplayString"
_LabelNetworkEthMask_Object = MibTableColumn
labelNetworkEthMask = _LabelNetworkEthMask_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 8),
    _LabelNetworkEthMask_Type()
)
labelNetworkEthMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelNetworkEthMask.setStatus("optional")


class _ValueNetworkEthMask_Type(DisplayString):
    """Custom type valueNetworkEthMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ValueNetworkEthMask_Type.__name__ = "DisplayString"
_ValueNetworkEthMask_Object = MibTableColumn
valueNetworkEthMask = _ValueNetworkEthMask_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 9),
    _ValueNetworkEthMask_Type()
)
valueNetworkEthMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueNetworkEthMask.setStatus("mandatory")


class _LabelShelfSerialNum_Type(DisplayString):
    """Custom type labelShelfSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelShelfSerialNum_Type.__name__ = "DisplayString"
_LabelShelfSerialNum_Object = MibTableColumn
labelShelfSerialNum = _LabelShelfSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 10),
    _LabelShelfSerialNum_Type()
)
labelShelfSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelShelfSerialNum.setStatus("optional")


class _ValueShelfSerialNum_Type(DisplayString):
    """Custom type valueShelfSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ValueShelfSerialNum_Type.__name__ = "DisplayString"
_ValueShelfSerialNum_Object = MibTableColumn
valueShelfSerialNum = _ValueShelfSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 11),
    _ValueShelfSerialNum_Type()
)
valueShelfSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valueShelfSerialNum.setStatus("mandatory")


class _LabelGateWayIPAdd_Type(DisplayString):
    """Custom type labelGateWayIPAdd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelGateWayIPAdd_Type.__name__ = "DisplayString"
_LabelGateWayIPAdd_Object = MibTableColumn
labelGateWayIPAdd = _LabelGateWayIPAdd_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 12),
    _LabelGateWayIPAdd_Type()
)
labelGateWayIPAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelGateWayIPAdd.setStatus("optional")


class _ValueGateWayIPAdd_Type(DisplayString):
    """Custom type valueGateWayIPAdd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ValueGateWayIPAdd_Type.__name__ = "DisplayString"
_ValueGateWayIPAdd_Object = MibTableColumn
valueGateWayIPAdd = _ValueGateWayIPAdd_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 13),
    _ValueGateWayIPAdd_Type()
)
valueGateWayIPAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueGateWayIPAdd.setStatus("mandatory")


class _LabelTrapDestination_Type(DisplayString):
    """Custom type labelTrapDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelTrapDestination_Type.__name__ = "DisplayString"
_LabelTrapDestination_Object = MibTableColumn
labelTrapDestination = _LabelTrapDestination_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 14),
    _LabelTrapDestination_Type()
)
labelTrapDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelTrapDestination.setStatus("optional")


class _ValueTrapDestination_Type(DisplayString):
    """Custom type valueTrapDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ValueTrapDestination_Type.__name__ = "DisplayString"
_ValueTrapDestination_Object = MibTableColumn
valueTrapDestination = _ValueTrapDestination_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 15),
    _ValueTrapDestination_Type()
)
valueTrapDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueTrapDestination.setStatus("mandatory")


class _LabelTFTPserver_Type(DisplayString):
    """Custom type labelTFTPserver based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelTFTPserver_Type.__name__ = "DisplayString"
_LabelTFTPserver_Object = MibTableColumn
labelTFTPserver = _LabelTFTPserver_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 16),
    _LabelTFTPserver_Type()
)
labelTFTPserver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelTFTPserver.setStatus("optional")


class _ValueTFTPserver_Type(DisplayString):
    """Custom type valueTFTPserver based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ValueTFTPserver_Type.__name__ = "DisplayString"
_ValueTFTPserver_Object = MibTableColumn
valueTFTPserver = _ValueTFTPserver_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 17),
    _ValueTFTPserver_Type()
)
valueTFTPserver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueTFTPserver.setStatus("mandatory")


class _LabelTrap2Destination_Type(DisplayString):
    """Custom type labelTrap2Destination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelTrap2Destination_Type.__name__ = "DisplayString"
_LabelTrap2Destination_Object = MibTableColumn
labelTrap2Destination = _LabelTrap2Destination_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 18),
    _LabelTrap2Destination_Type()
)
labelTrap2Destination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelTrap2Destination.setStatus("optional")


class _ValueTrap2Destination_Type(DisplayString):
    """Custom type valueTrap2Destination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ValueTrap2Destination_Type.__name__ = "DisplayString"
_ValueTrap2Destination_Object = MibTableColumn
valueTrap2Destination = _ValueTrap2Destination_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 19),
    _ValueTrap2Destination_Type()
)
valueTrap2Destination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueTrap2Destination.setStatus("mandatory")


class _LabelTrap3Destination_Type(DisplayString):
    """Custom type labelTrap3Destination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelTrap3Destination_Type.__name__ = "DisplayString"
_LabelTrap3Destination_Object = MibTableColumn
labelTrap3Destination = _LabelTrap3Destination_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 20),
    _LabelTrap3Destination_Type()
)
labelTrap3Destination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelTrap3Destination.setStatus("optional")


class _ValueTrap3Destination_Type(DisplayString):
    """Custom type valueTrap3Destination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ValueTrap3Destination_Type.__name__ = "DisplayString"
_ValueTrap3Destination_Object = MibTableColumn
valueTrap3Destination = _ValueTrap3Destination_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 21),
    _ValueTrap3Destination_Type()
)
valueTrap3Destination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueTrap3Destination.setStatus("mandatory")


class _LabelTrap4Destination_Type(DisplayString):
    """Custom type labelTrap4Destination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelTrap4Destination_Type.__name__ = "DisplayString"
_LabelTrap4Destination_Object = MibTableColumn
labelTrap4Destination = _LabelTrap4Destination_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 22),
    _LabelTrap4Destination_Type()
)
labelTrap4Destination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelTrap4Destination.setStatus("optional")


class _ValueTrap4Destination_Type(DisplayString):
    """Custom type valueTrap4Destination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ValueTrap4Destination_Type.__name__ = "DisplayString"
_ValueTrap4Destination_Object = MibTableColumn
valueTrap4Destination = _ValueTrap4Destination_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 23),
    _ValueTrap4Destination_Type()
)
valueTrap4Destination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueTrap4Destination.setStatus("mandatory")


class _LabelTrap5Destination_Type(DisplayString):
    """Custom type labelTrap5Destination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelTrap5Destination_Type.__name__ = "DisplayString"
_LabelTrap5Destination_Object = MibTableColumn
labelTrap5Destination = _LabelTrap5Destination_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 24),
    _LabelTrap5Destination_Type()
)
labelTrap5Destination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelTrap5Destination.setStatus("optional")


class _ValueTrap5Destination_Type(DisplayString):
    """Custom type valueTrap5Destination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ValueTrap5Destination_Type.__name__ = "DisplayString"
_ValueTrap5Destination_Object = MibTableColumn
valueTrap5Destination = _ValueTrap5Destination_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 25),
    _ValueTrap5Destination_Type()
)
valueTrap5Destination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueTrap5Destination.setStatus("mandatory")


class _LabelISDNMode_Type(DisplayString):
    """Custom type labelISDNMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelISDNMode_Type.__name__ = "DisplayString"
_LabelISDNMode_Object = MibTableColumn
labelISDNMode = _LabelISDNMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 26),
    _LabelISDNMode_Type()
)
labelISDNMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelISDNMode.setStatus("optional")


class _ValueISDNMode_Type(Integer32):
    """Custom type valueISDNMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ValueISDNMode_Type.__name__ = "Integer32"
_ValueISDNMode_Object = MibTableColumn
valueISDNMode = _ValueISDNMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 27),
    _ValueISDNMode_Type()
)
valueISDNMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueISDNMode.setStatus("mandatory")


class _LabelISDNModemIPAddress_Type(DisplayString):
    """Custom type labelISDNModemIPAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelISDNModemIPAddress_Type.__name__ = "DisplayString"
_LabelISDNModemIPAddress_Object = MibTableColumn
labelISDNModemIPAddress = _LabelISDNModemIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 28),
    _LabelISDNModemIPAddress_Type()
)
labelISDNModemIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelISDNModemIPAddress.setStatus("optional")


class _ValueISDNModemIPAddress_Type(DisplayString):
    """Custom type valueISDNModemIPAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ValueISDNModemIPAddress_Type.__name__ = "DisplayString"
_ValueISDNModemIPAddress_Object = MibTableColumn
valueISDNModemIPAddress = _ValueISDNModemIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 29),
    _ValueISDNModemIPAddress_Type()
)
valueISDNModemIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueISDNModemIPAddress.setStatus("mandatory")


class _LabelISDNTrapTimeout_Type(DisplayString):
    """Custom type labelISDNTrapTimeout based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelISDNTrapTimeout_Type.__name__ = "DisplayString"
_LabelISDNTrapTimeout_Object = MibTableColumn
labelISDNTrapTimeout = _LabelISDNTrapTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 30),
    _LabelISDNTrapTimeout_Type()
)
labelISDNTrapTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelISDNTrapTimeout.setStatus("optional")


class _ValueISDNTrapTimeout_Type(Integer32):
    """Custom type valueISDNTrapTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_ValueISDNTrapTimeout_Type.__name__ = "Integer32"
_ValueISDNTrapTimeout_Object = MibTableColumn
valueISDNTrapTimeout = _ValueISDNTrapTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 31),
    _ValueISDNTrapTimeout_Type()
)
valueISDNTrapTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueISDNTrapTimeout.setStatus("mandatory")


class _LabelISDNPingTimeout_Type(DisplayString):
    """Custom type labelISDNPingTimeout based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelISDNPingTimeout_Type.__name__ = "DisplayString"
_LabelISDNPingTimeout_Object = MibTableColumn
labelISDNPingTimeout = _LabelISDNPingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 32),
    _LabelISDNPingTimeout_Type()
)
labelISDNPingTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelISDNPingTimeout.setStatus("optional")


class _ValueISDNPingTimeout_Type(Integer32):
    """Custom type valueISDNPingTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_ValueISDNPingTimeout_Type.__name__ = "Integer32"
_ValueISDNPingTimeout_Object = MibTableColumn
valueISDNPingTimeout = _ValueISDNPingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 33),
    _ValueISDNPingTimeout_Type()
)
valueISDNPingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueISDNPingTimeout.setStatus("mandatory")


class _LabelISDNBackoffTimer_Type(DisplayString):
    """Custom type labelISDNBackoffTimer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelISDNBackoffTimer_Type.__name__ = "DisplayString"
_LabelISDNBackoffTimer_Object = MibTableColumn
labelISDNBackoffTimer = _LabelISDNBackoffTimer_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 34),
    _LabelISDNBackoffTimer_Type()
)
labelISDNBackoffTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelISDNBackoffTimer.setStatus("optional")


class _ValueISDNBackoffTimer_Type(Integer32):
    """Custom type valueISDNBackoffTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_ValueISDNBackoffTimer_Type.__name__ = "Integer32"
_ValueISDNBackoffTimer_Object = MibTableColumn
valueISDNBackoffTimer = _ValueISDNBackoffTimer_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 3, 2, 35),
    _ValueISDNBackoffTimer_Type()
)
valueISDNBackoffTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueISDNBackoffTimer.setStatus("mandatory")
_Gx2cmAnalogTable_Object = MibTable
gx2cmAnalogTable = _Gx2cmAnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 4)
)
if mibBuilder.loadTexts:
    gx2cmAnalogTable.setStatus("mandatory")
_Gx2cmAnalogEntry_Object = MibTableRow
gx2cmAnalogEntry = _Gx2cmAnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 4, 3)
)
gx2cmAnalogEntry.setIndexNames(
    (0, "OMNI-gx2CM-MIB", "gx2cmTableIndex"),
)
if mibBuilder.loadTexts:
    gx2cmAnalogEntry.setStatus("mandatory")


class _Gx2cmTableIndex_Type(Integer32):
    """Custom type gx2cmTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2cmTableIndex_Type.__name__ = "Integer32"
_Gx2cmTableIndex_Object = MibTableColumn
gx2cmTableIndex = _Gx2cmTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 4, 3, 1),
    _Gx2cmTableIndex_Type()
)
gx2cmTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2cmTableIndex.setStatus("mandatory")


class _LabelModTemp_Type(DisplayString):
    """Custom type labelModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelModTemp_Type.__name__ = "DisplayString"
_LabelModTemp_Object = MibTableColumn
labelModTemp = _LabelModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 4, 3, 2),
    _LabelModTemp_Type()
)
labelModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelModTemp.setStatus("optional")


class _UomModTemp_Type(DisplayString):
    """Custom type uomModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_UomModTemp_Type.__name__ = "DisplayString"
_UomModTemp_Object = MibTableColumn
uomModTemp = _UomModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 4, 3, 3),
    _UomModTemp_Type()
)
uomModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uomModTemp.setStatus("optional")
_MajorHighModTemp_Type = Float
_MajorHighModTemp_Object = MibTableColumn
majorHighModTemp = _MajorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 4, 3, 4),
    _MajorHighModTemp_Type()
)
majorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    majorHighModTemp.setStatus("mandatory")
_MajorLowModTemp_Type = Float
_MajorLowModTemp_Object = MibTableColumn
majorLowModTemp = _MajorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 4, 3, 5),
    _MajorLowModTemp_Type()
)
majorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    majorLowModTemp.setStatus("mandatory")
_MinorHighModTemp_Type = Float
_MinorHighModTemp_Object = MibTableColumn
minorHighModTemp = _MinorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 4, 3, 6),
    _MinorHighModTemp_Type()
)
minorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minorHighModTemp.setStatus("mandatory")
_MinorLowModTemp_Type = Float
_MinorLowModTemp_Object = MibTableColumn
minorLowModTemp = _MinorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 4, 3, 7),
    _MinorLowModTemp_Type()
)
minorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minorLowModTemp.setStatus("mandatory")
_CurrentValueModTemp_Type = Float
_CurrentValueModTemp_Object = MibTableColumn
currentValueModTemp = _CurrentValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 4, 3, 8),
    _CurrentValueModTemp_Type()
)
currentValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentValueModTemp.setStatus("mandatory")


class _StateFlagModTemp_Type(Integer32):
    """Custom type stateFlagModTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_StateFlagModTemp_Type.__name__ = "Integer32"
_StateFlagModTemp_Object = MibTableColumn
stateFlagModTemp = _StateFlagModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 4, 3, 9),
    _StateFlagModTemp_Type()
)
stateFlagModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateFlagModTemp.setStatus("mandatory")
_MinValueModTemp_Type = Float
_MinValueModTemp_Object = MibTableColumn
minValueModTemp = _MinValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 4, 3, 10),
    _MinValueModTemp_Type()
)
minValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minValueModTemp.setStatus("optional")
_MaxValueModTemp_Type = Float
_MaxValueModTemp_Object = MibTableColumn
maxValueModTemp = _MaxValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 4, 3, 11),
    _MaxValueModTemp_Type()
)
maxValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxValueModTemp.setStatus("optional")


class _AlarmStateModTemp_Type(Integer32):
    """Custom type alarmStateModTemp based on Integer32"""
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
        *(("informational", 6),
          ("majorHighAlarm", 5),
          ("majorLowAlarm", 2),
          ("minorHighAlarm", 4),
          ("minorLowAlarm", 3),
          ("noAlarm", 1))
    )


_AlarmStateModTemp_Type.__name__ = "Integer32"
_AlarmStateModTemp_Object = MibTableColumn
alarmStateModTemp = _AlarmStateModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 4, 3, 12),
    _AlarmStateModTemp_Type()
)
alarmStateModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStateModTemp.setStatus("mandatory")
_Gx2cmDigitalTable_Object = MibTable
gx2cmDigitalTable = _Gx2cmDigitalTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 5)
)
if mibBuilder.loadTexts:
    gx2cmDigitalTable.setStatus("mandatory")
_Gx2cmDigitalEntry_Object = MibTableRow
gx2cmDigitalEntry = _Gx2cmDigitalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 5, 4)
)
gx2cmDigitalEntry.setIndexNames(
    (0, "OMNI-gx2CM-MIB", "gx2cmDigitalTableIndex"),
)
if mibBuilder.loadTexts:
    gx2cmDigitalEntry.setStatus("mandatory")


class _Gx2cmDigitalTableIndex_Type(Integer32):
    """Custom type gx2cmDigitalTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2cmDigitalTableIndex_Type.__name__ = "Integer32"
_Gx2cmDigitalTableIndex_Object = MibTableColumn
gx2cmDigitalTableIndex = _Gx2cmDigitalTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 5, 4, 1),
    _Gx2cmDigitalTableIndex_Type()
)
gx2cmDigitalTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2cmDigitalTableIndex.setStatus("mandatory")


class _LabelRemoteLocal_Type(DisplayString):
    """Custom type labelRemoteLocal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelRemoteLocal_Type.__name__ = "DisplayString"
_LabelRemoteLocal_Object = MibTableColumn
labelRemoteLocal = _LabelRemoteLocal_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 5, 4, 2),
    _LabelRemoteLocal_Type()
)
labelRemoteLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelRemoteLocal.setStatus("obsolete")


class _EnumRemoteLocal_Type(DisplayString):
    """Custom type enumRemoteLocal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EnumRemoteLocal_Type.__name__ = "DisplayString"
_EnumRemoteLocal_Object = MibTableColumn
enumRemoteLocal = _EnumRemoteLocal_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 5, 4, 3),
    _EnumRemoteLocal_Type()
)
enumRemoteLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enumRemoteLocal.setStatus("obsolete")


class _ValueRemoteLocal_Type(Integer32):
    """Custom type valueRemoteLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_ValueRemoteLocal_Type.__name__ = "Integer32"
_ValueRemoteLocal_Object = MibTableColumn
valueRemoteLocal = _ValueRemoteLocal_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 5, 4, 4),
    _ValueRemoteLocal_Type()
)
valueRemoteLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueRemoteLocal.setStatus("obsolete")


class _StateFlagRemoteLocal_Type(Integer32):
    """Custom type stateFlagRemoteLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_StateFlagRemoteLocal_Type.__name__ = "Integer32"
_StateFlagRemoteLocal_Object = MibTableColumn
stateFlagRemoteLocal = _StateFlagRemoteLocal_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 5, 4, 5),
    _StateFlagRemoteLocal_Type()
)
stateFlagRemoteLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateFlagRemoteLocal.setStatus("obsolete")


class _LabelResetSlot_Type(DisplayString):
    """Custom type labelResetSlot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelResetSlot_Type.__name__ = "DisplayString"
_LabelResetSlot_Object = MibTableColumn
labelResetSlot = _LabelResetSlot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 5, 4, 6),
    _LabelResetSlot_Type()
)
labelResetSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelResetSlot.setStatus("optional")


class _EnumResetSlot_Type(DisplayString):
    """Custom type enumResetSlot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EnumResetSlot_Type.__name__ = "DisplayString"
_EnumResetSlot_Object = MibTableColumn
enumResetSlot = _EnumResetSlot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 5, 4, 7),
    _EnumResetSlot_Type()
)
enumResetSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enumResetSlot.setStatus("optional")
_ValueResetSlot_Type = Integer32
_ValueResetSlot_Object = MibTableColumn
valueResetSlot = _ValueResetSlot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 5, 4, 8),
    _ValueResetSlot_Type()
)
valueResetSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueResetSlot.setStatus("mandatory")


class _StateResetSlot_Type(Integer32):
    """Custom type stateResetSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_StateResetSlot_Type.__name__ = "Integer32"
_StateResetSlot_Object = MibTableColumn
stateResetSlot = _StateResetSlot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 5, 4, 9),
    _StateResetSlot_Type()
)
stateResetSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateResetSlot.setStatus("mandatory")


class _LabelIdShelf_Type(DisplayString):
    """Custom type labelIdShelf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelIdShelf_Type.__name__ = "DisplayString"
_LabelIdShelf_Object = MibTableColumn
labelIdShelf = _LabelIdShelf_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 5, 4, 10),
    _LabelIdShelf_Type()
)
labelIdShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelIdShelf.setStatus("optional")


class _EnumIdShelf_Type(DisplayString):
    """Custom type enumIdShelf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EnumIdShelf_Type.__name__ = "DisplayString"
_EnumIdShelf_Object = MibTableColumn
enumIdShelf = _EnumIdShelf_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 5, 4, 11),
    _EnumIdShelf_Type()
)
enumIdShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enumIdShelf.setStatus("optional")


class _ValueIdShelf_Type(Integer32):
    """Custom type valueIdShelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ValueIdShelf_Type.__name__ = "Integer32"
_ValueIdShelf_Object = MibTableColumn
valueIdShelf = _ValueIdShelf_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 5, 4, 12),
    _ValueIdShelf_Type()
)
valueIdShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueIdShelf.setStatus("mandatory")


class _StateFlagIdShelf_Type(Integer32):
    """Custom type stateFlagIdShelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_StateFlagIdShelf_Type.__name__ = "Integer32"
_StateFlagIdShelf_Object = MibTableColumn
stateFlagIdShelf = _StateFlagIdShelf_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 5, 4, 13),
    _StateFlagIdShelf_Type()
)
stateFlagIdShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateFlagIdShelf.setStatus("mandatory")


class _LabelResetAlarm_Type(DisplayString):
    """Custom type labelResetAlarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelResetAlarm_Type.__name__ = "DisplayString"
_LabelResetAlarm_Object = MibTableColumn
labelResetAlarm = _LabelResetAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 5, 4, 14),
    _LabelResetAlarm_Type()
)
labelResetAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelResetAlarm.setStatus("optional")


class _EnumResetAlarm_Type(DisplayString):
    """Custom type enumResetAlarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EnumResetAlarm_Type.__name__ = "DisplayString"
_EnumResetAlarm_Object = MibTableColumn
enumResetAlarm = _EnumResetAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 5, 4, 15),
    _EnumResetAlarm_Type()
)
enumResetAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enumResetAlarm.setStatus("optional")
_ValueResetAlarm_Type = Integer32
_ValueResetAlarm_Object = MibTableColumn
valueResetAlarm = _ValueResetAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 5, 4, 16),
    _ValueResetAlarm_Type()
)
valueResetAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueResetAlarm.setStatus("mandatory")


class _StateFlagResetAlarm_Type(Integer32):
    """Custom type stateFlagResetAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_StateFlagResetAlarm_Type.__name__ = "Integer32"
_StateFlagResetAlarm_Object = MibTableColumn
stateFlagResetAlarm = _StateFlagResetAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 5, 4, 17),
    _StateFlagResetAlarm_Type()
)
stateFlagResetAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateFlagResetAlarm.setStatus("mandatory")
_Gx2cmStatusTable_Object = MibTable
gx2cmStatusTable = _Gx2cmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 6)
)
if mibBuilder.loadTexts:
    gx2cmStatusTable.setStatus("mandatory")
_Gx2cmStatusEntry_Object = MibTableRow
gx2cmStatusEntry = _Gx2cmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 6, 5)
)
gx2cmStatusEntry.setIndexNames(
    (0, "OMNI-gx2CM-MIB", "gx2cmStatusTableIndex"),
)
if mibBuilder.loadTexts:
    gx2cmStatusEntry.setStatus("mandatory")


class _Gx2cmStatusTableIndex_Type(Integer32):
    """Custom type gx2cmStatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2cmStatusTableIndex_Type.__name__ = "Integer32"
_Gx2cmStatusTableIndex_Object = MibTableColumn
gx2cmStatusTableIndex = _Gx2cmStatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 6, 5, 1),
    _Gx2cmStatusTableIndex_Type()
)
gx2cmStatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2cmStatusTableIndex.setStatus("mandatory")


class _LabelShelfAlarm_Type(DisplayString):
    """Custom type labelShelfAlarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelShelfAlarm_Type.__name__ = "DisplayString"
_LabelShelfAlarm_Object = MibTableColumn
labelShelfAlarm = _LabelShelfAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 6, 5, 2),
    _LabelShelfAlarm_Type()
)
labelShelfAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelShelfAlarm.setStatus("optional")


class _ValueShelfAlarm_Type(Integer32):
    """Custom type valueShelfAlarm based on Integer32"""
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
        *(("critical", 6),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_ValueShelfAlarm_Type.__name__ = "Integer32"
_ValueShelfAlarm_Object = MibTableColumn
valueShelfAlarm = _ValueShelfAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 6, 5, 3),
    _ValueShelfAlarm_Type()
)
valueShelfAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valueShelfAlarm.setStatus("mandatory")


class _StateShelfAlarm_Type(Integer32):
    """Custom type stateShelfAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_StateShelfAlarm_Type.__name__ = "Integer32"
_StateShelfAlarm_Object = MibTableColumn
stateShelfAlarm = _StateShelfAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 6, 5, 4),
    _StateShelfAlarm_Type()
)
stateShelfAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateShelfAlarm.setStatus("mandatory")


class _LabelDataCrc_Type(DisplayString):
    """Custom type labelDataCrc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelDataCrc_Type.__name__ = "DisplayString"
_LabelDataCrc_Object = MibTableColumn
labelDataCrc = _LabelDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 6, 5, 5),
    _LabelDataCrc_Type()
)
labelDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelDataCrc.setStatus("optional")


class _ValueDataCrc_Type(Integer32):
    """Custom type valueDataCrc based on Integer32"""
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
        *(("critical", 6),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_ValueDataCrc_Type.__name__ = "Integer32"
_ValueDataCrc_Object = MibTableColumn
valueDataCrc = _ValueDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 6, 5, 6),
    _ValueDataCrc_Type()
)
valueDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valueDataCrc.setStatus("mandatory")


class _StateDataCrc_Type(Integer32):
    """Custom type stateDataCrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_StateDataCrc_Type.__name__ = "Integer32"
_StateDataCrc_Object = MibTableColumn
stateDataCrc = _StateDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 6, 5, 7),
    _StateDataCrc_Type()
)
stateDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateDataCrc.setStatus("mandatory")


class _LabelFlashStatus_Type(DisplayString):
    """Custom type labelFlashStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelFlashStatus_Type.__name__ = "DisplayString"
_LabelFlashStatus_Object = MibTableColumn
labelFlashStatus = _LabelFlashStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 6, 5, 8),
    _LabelFlashStatus_Type()
)
labelFlashStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelFlashStatus.setStatus("optional")


class _ValueFlashStatus_Type(Integer32):
    """Custom type valueFlashStatus based on Integer32"""
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
        *(("critical", 6),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_ValueFlashStatus_Type.__name__ = "Integer32"
_ValueFlashStatus_Object = MibTableColumn
valueFlashStatus = _ValueFlashStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 6, 5, 9),
    _ValueFlashStatus_Type()
)
valueFlashStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valueFlashStatus.setStatus("mandatory")


class _StateFlashStatus_Type(Integer32):
    """Custom type stateFlashStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_StateFlashStatus_Type.__name__ = "Integer32"
_StateFlashStatus_Object = MibTableColumn
stateFlashStatus = _StateFlashStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 6, 5, 10),
    _StateFlashStatus_Type()
)
stateFlashStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateFlashStatus.setStatus("mandatory")


class _LabelBootStatus_Type(DisplayString):
    """Custom type labelBootStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelBootStatus_Type.__name__ = "DisplayString"
_LabelBootStatus_Object = MibTableColumn
labelBootStatus = _LabelBootStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 6, 5, 11),
    _LabelBootStatus_Type()
)
labelBootStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelBootStatus.setStatus("optional")


class _ValueBootStatus_Type(Integer32):
    """Custom type valueBootStatus based on Integer32"""
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
        *(("critical", 6),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_ValueBootStatus_Type.__name__ = "Integer32"
_ValueBootStatus_Object = MibTableColumn
valueBootStatus = _ValueBootStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 6, 5, 12),
    _ValueBootStatus_Type()
)
valueBootStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valueBootStatus.setStatus("mandatory")


class _StateBootStatus_Type(Integer32):
    """Custom type stateBootStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_StateBootStatus_Type.__name__ = "Integer32"
_StateBootStatus_Object = MibTableColumn
stateBootStatus = _StateBootStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 6, 5, 13),
    _StateBootStatus_Type()
)
stateBootStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateBootStatus.setStatus("mandatory")


class _LabelAlmLimCrc_Type(DisplayString):
    """Custom type labelAlmLimCrc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelAlmLimCrc_Type.__name__ = "DisplayString"
_LabelAlmLimCrc_Object = MibTableColumn
labelAlmLimCrc = _LabelAlmLimCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 6, 5, 14),
    _LabelAlmLimCrc_Type()
)
labelAlmLimCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelAlmLimCrc.setStatus("optional")


class _ValueAlmLimCrc_Type(Integer32):
    """Custom type valueAlmLimCrc based on Integer32"""
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
        *(("critical", 6),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_ValueAlmLimCrc_Type.__name__ = "Integer32"
_ValueAlmLimCrc_Object = MibTableColumn
valueAlmLimCrc = _ValueAlmLimCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 6, 5, 15),
    _ValueAlmLimCrc_Type()
)
valueAlmLimCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valueAlmLimCrc.setStatus("mandatory")


class _StateAlmLimCrc_Type(Integer32):
    """Custom type stateAlmLimCrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_StateAlmLimCrc_Type.__name__ = "Integer32"
_StateAlmLimCrc_Object = MibTableColumn
stateAlmLimCrc = _StateAlmLimCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 6, 5, 16),
    _StateAlmLimCrc_Type()
)
stateAlmLimCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateAlmLimCrc.setStatus("mandatory")
_Gx2cmAMCTable_Object = MibTable
gx2cmAMCTable = _Gx2cmAMCTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7)
)
if mibBuilder.loadTexts:
    gx2cmAMCTable.setStatus("mandatory")
_Gx2cmAMCEntry_Object = MibTableRow
gx2cmAMCEntry = _Gx2cmAMCEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6)
)
gx2cmAMCEntry.setIndexNames(
    (0, "OMNI-gx2CM-MIB", "gx2cmAMCTableIndex"),
)
if mibBuilder.loadTexts:
    gx2cmAMCEntry.setStatus("mandatory")


class _Gx2cmAMCTableIndex_Type(Integer32):
    """Custom type gx2cmAMCTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2cmAMCTableIndex_Type.__name__ = "Integer32"
_Gx2cmAMCTableIndex_Object = MibTableColumn
gx2cmAMCTableIndex = _Gx2cmAMCTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 1),
    _Gx2cmAMCTableIndex_Type()
)
gx2cmAMCTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2cmAMCTableIndex.setStatus("mandatory")


class _ValueAMCslot1_Type(Integer32):
    """Custom type valueAMCslot1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("force", 3))
    )


_ValueAMCslot1_Type.__name__ = "Integer32"
_ValueAMCslot1_Object = MibTableColumn
valueAMCslot1 = _ValueAMCslot1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 2),
    _ValueAMCslot1_Type()
)
valueAMCslot1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueAMCslot1.setStatus("mandatory")


class _SerialAMCslot1_Type(DisplayString):
    """Custom type serialAMCslot1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SerialAMCslot1_Type.__name__ = "DisplayString"
_SerialAMCslot1_Object = MibTableColumn
serialAMCslot1 = _SerialAMCslot1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 3),
    _SerialAMCslot1_Type()
)
serialAMCslot1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialAMCslot1.setStatus("mandatory")
_AgentIDAMCslot1_Type = Integer32
_AgentIDAMCslot1_Object = MibTableColumn
agentIDAMCslot1 = _AgentIDAMCslot1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 4),
    _AgentIDAMCslot1_Type()
)
agentIDAMCslot1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIDAMCslot1.setStatus("mandatory")


class _ValueAMCslot2_Type(Integer32):
    """Custom type valueAMCslot2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("force", 3))
    )


_ValueAMCslot2_Type.__name__ = "Integer32"
_ValueAMCslot2_Object = MibTableColumn
valueAMCslot2 = _ValueAMCslot2_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 5),
    _ValueAMCslot2_Type()
)
valueAMCslot2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueAMCslot2.setStatus("mandatory")


class _SerialAMCslot2_Type(DisplayString):
    """Custom type serialAMCslot2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SerialAMCslot2_Type.__name__ = "DisplayString"
_SerialAMCslot2_Object = MibTableColumn
serialAMCslot2 = _SerialAMCslot2_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 6),
    _SerialAMCslot2_Type()
)
serialAMCslot2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialAMCslot2.setStatus("mandatory")
_AgentIDAMCslot2_Type = Integer32
_AgentIDAMCslot2_Object = MibTableColumn
agentIDAMCslot2 = _AgentIDAMCslot2_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 7),
    _AgentIDAMCslot2_Type()
)
agentIDAMCslot2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIDAMCslot2.setStatus("mandatory")


class _ValueAMCslot3_Type(Integer32):
    """Custom type valueAMCslot3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("force", 3))
    )


_ValueAMCslot3_Type.__name__ = "Integer32"
_ValueAMCslot3_Object = MibTableColumn
valueAMCslot3 = _ValueAMCslot3_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 8),
    _ValueAMCslot3_Type()
)
valueAMCslot3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueAMCslot3.setStatus("mandatory")


class _SerialAMCslot3_Type(DisplayString):
    """Custom type serialAMCslot3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SerialAMCslot3_Type.__name__ = "DisplayString"
_SerialAMCslot3_Object = MibTableColumn
serialAMCslot3 = _SerialAMCslot3_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 9),
    _SerialAMCslot3_Type()
)
serialAMCslot3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialAMCslot3.setStatus("mandatory")
_AgentIDAMCslot3_Type = Integer32
_AgentIDAMCslot3_Object = MibTableColumn
agentIDAMCslot3 = _AgentIDAMCslot3_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 10),
    _AgentIDAMCslot3_Type()
)
agentIDAMCslot3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIDAMCslot3.setStatus("mandatory")


class _ValueAMCslot4_Type(Integer32):
    """Custom type valueAMCslot4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("force", 3))
    )


_ValueAMCslot4_Type.__name__ = "Integer32"
_ValueAMCslot4_Object = MibTableColumn
valueAMCslot4 = _ValueAMCslot4_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 11),
    _ValueAMCslot4_Type()
)
valueAMCslot4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueAMCslot4.setStatus("mandatory")


class _SerialAMCslot4_Type(DisplayString):
    """Custom type serialAMCslot4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SerialAMCslot4_Type.__name__ = "DisplayString"
_SerialAMCslot4_Object = MibTableColumn
serialAMCslot4 = _SerialAMCslot4_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 12),
    _SerialAMCslot4_Type()
)
serialAMCslot4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialAMCslot4.setStatus("mandatory")
_AgentIDAMCslot4_Type = Integer32
_AgentIDAMCslot4_Object = MibTableColumn
agentIDAMCslot4 = _AgentIDAMCslot4_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 13),
    _AgentIDAMCslot4_Type()
)
agentIDAMCslot4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIDAMCslot4.setStatus("mandatory")


class _ValueAMCslot5_Type(Integer32):
    """Custom type valueAMCslot5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("force", 3))
    )


_ValueAMCslot5_Type.__name__ = "Integer32"
_ValueAMCslot5_Object = MibTableColumn
valueAMCslot5 = _ValueAMCslot5_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 14),
    _ValueAMCslot5_Type()
)
valueAMCslot5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueAMCslot5.setStatus("mandatory")


class _SerialAMCslot5_Type(DisplayString):
    """Custom type serialAMCslot5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SerialAMCslot5_Type.__name__ = "DisplayString"
_SerialAMCslot5_Object = MibTableColumn
serialAMCslot5 = _SerialAMCslot5_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 15),
    _SerialAMCslot5_Type()
)
serialAMCslot5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialAMCslot5.setStatus("mandatory")
_AgentIDAMCslot5_Type = Integer32
_AgentIDAMCslot5_Object = MibTableColumn
agentIDAMCslot5 = _AgentIDAMCslot5_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 16),
    _AgentIDAMCslot5_Type()
)
agentIDAMCslot5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIDAMCslot5.setStatus("mandatory")


class _ValueAMCslot6_Type(Integer32):
    """Custom type valueAMCslot6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("force", 3))
    )


_ValueAMCslot6_Type.__name__ = "Integer32"
_ValueAMCslot6_Object = MibTableColumn
valueAMCslot6 = _ValueAMCslot6_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 17),
    _ValueAMCslot6_Type()
)
valueAMCslot6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueAMCslot6.setStatus("mandatory")


class _SerialAMCslot6_Type(DisplayString):
    """Custom type serialAMCslot6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SerialAMCslot6_Type.__name__ = "DisplayString"
_SerialAMCslot6_Object = MibTableColumn
serialAMCslot6 = _SerialAMCslot6_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 18),
    _SerialAMCslot6_Type()
)
serialAMCslot6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialAMCslot6.setStatus("mandatory")
_AgentIDAMCslot6_Type = Integer32
_AgentIDAMCslot6_Object = MibTableColumn
agentIDAMCslot6 = _AgentIDAMCslot6_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 19),
    _AgentIDAMCslot6_Type()
)
agentIDAMCslot6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIDAMCslot6.setStatus("mandatory")


class _ValueAMCslot7_Type(Integer32):
    """Custom type valueAMCslot7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("force", 3))
    )


_ValueAMCslot7_Type.__name__ = "Integer32"
_ValueAMCslot7_Object = MibTableColumn
valueAMCslot7 = _ValueAMCslot7_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 20),
    _ValueAMCslot7_Type()
)
valueAMCslot7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueAMCslot7.setStatus("mandatory")


class _SerialAMCslot7_Type(DisplayString):
    """Custom type serialAMCslot7 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SerialAMCslot7_Type.__name__ = "DisplayString"
_SerialAMCslot7_Object = MibTableColumn
serialAMCslot7 = _SerialAMCslot7_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 21),
    _SerialAMCslot7_Type()
)
serialAMCslot7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialAMCslot7.setStatus("mandatory")
_AgentIDAMCslot7_Type = Integer32
_AgentIDAMCslot7_Object = MibTableColumn
agentIDAMCslot7 = _AgentIDAMCslot7_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 22),
    _AgentIDAMCslot7_Type()
)
agentIDAMCslot7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIDAMCslot7.setStatus("mandatory")


class _ValueAMCslot8_Type(Integer32):
    """Custom type valueAMCslot8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("force", 3))
    )


_ValueAMCslot8_Type.__name__ = "Integer32"
_ValueAMCslot8_Object = MibTableColumn
valueAMCslot8 = _ValueAMCslot8_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 23),
    _ValueAMCslot8_Type()
)
valueAMCslot8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueAMCslot8.setStatus("mandatory")


class _SerialAMCslot8_Type(DisplayString):
    """Custom type serialAMCslot8 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SerialAMCslot8_Type.__name__ = "DisplayString"
_SerialAMCslot8_Object = MibTableColumn
serialAMCslot8 = _SerialAMCslot8_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 24),
    _SerialAMCslot8_Type()
)
serialAMCslot8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialAMCslot8.setStatus("mandatory")
_AgentIDAMCslot8_Type = Integer32
_AgentIDAMCslot8_Object = MibTableColumn
agentIDAMCslot8 = _AgentIDAMCslot8_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 25),
    _AgentIDAMCslot8_Type()
)
agentIDAMCslot8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIDAMCslot8.setStatus("mandatory")


class _ValueAMCslot9_Type(Integer32):
    """Custom type valueAMCslot9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("force", 3))
    )


_ValueAMCslot9_Type.__name__ = "Integer32"
_ValueAMCslot9_Object = MibTableColumn
valueAMCslot9 = _ValueAMCslot9_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 26),
    _ValueAMCslot9_Type()
)
valueAMCslot9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueAMCslot9.setStatus("mandatory")


class _SerialAMCslot9_Type(DisplayString):
    """Custom type serialAMCslot9 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SerialAMCslot9_Type.__name__ = "DisplayString"
_SerialAMCslot9_Object = MibTableColumn
serialAMCslot9 = _SerialAMCslot9_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 27),
    _SerialAMCslot9_Type()
)
serialAMCslot9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialAMCslot9.setStatus("mandatory")
_AgentIDAMCslot9_Type = Integer32
_AgentIDAMCslot9_Object = MibTableColumn
agentIDAMCslot9 = _AgentIDAMCslot9_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 28),
    _AgentIDAMCslot9_Type()
)
agentIDAMCslot9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIDAMCslot9.setStatus("mandatory")


class _ValueAMCslot10_Type(Integer32):
    """Custom type valueAMCslot10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("force", 3))
    )


_ValueAMCslot10_Type.__name__ = "Integer32"
_ValueAMCslot10_Object = MibTableColumn
valueAMCslot10 = _ValueAMCslot10_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 29),
    _ValueAMCslot10_Type()
)
valueAMCslot10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueAMCslot10.setStatus("mandatory")


class _SerialAMCslot10_Type(DisplayString):
    """Custom type serialAMCslot10 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SerialAMCslot10_Type.__name__ = "DisplayString"
_SerialAMCslot10_Object = MibTableColumn
serialAMCslot10 = _SerialAMCslot10_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 30),
    _SerialAMCslot10_Type()
)
serialAMCslot10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialAMCslot10.setStatus("mandatory")
_AgentIDAMCslot10_Type = Integer32
_AgentIDAMCslot10_Object = MibTableColumn
agentIDAMCslot10 = _AgentIDAMCslot10_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 31),
    _AgentIDAMCslot10_Type()
)
agentIDAMCslot10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIDAMCslot10.setStatus("mandatory")


class _ValueAMCslot11_Type(Integer32):
    """Custom type valueAMCslot11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("force", 3))
    )


_ValueAMCslot11_Type.__name__ = "Integer32"
_ValueAMCslot11_Object = MibTableColumn
valueAMCslot11 = _ValueAMCslot11_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 32),
    _ValueAMCslot11_Type()
)
valueAMCslot11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueAMCslot11.setStatus("mandatory")


class _SerialAMCslot11_Type(DisplayString):
    """Custom type serialAMCslot11 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SerialAMCslot11_Type.__name__ = "DisplayString"
_SerialAMCslot11_Object = MibTableColumn
serialAMCslot11 = _SerialAMCslot11_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 33),
    _SerialAMCslot11_Type()
)
serialAMCslot11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialAMCslot11.setStatus("mandatory")
_AgentIDAMCslot11_Type = Integer32
_AgentIDAMCslot11_Object = MibTableColumn
agentIDAMCslot11 = _AgentIDAMCslot11_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 34),
    _AgentIDAMCslot11_Type()
)
agentIDAMCslot11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIDAMCslot11.setStatus("mandatory")


class _ValueAMCslot12_Type(Integer32):
    """Custom type valueAMCslot12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("force", 3))
    )


_ValueAMCslot12_Type.__name__ = "Integer32"
_ValueAMCslot12_Object = MibTableColumn
valueAMCslot12 = _ValueAMCslot12_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 35),
    _ValueAMCslot12_Type()
)
valueAMCslot12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueAMCslot12.setStatus("mandatory")


class _SerialAMCslot12_Type(DisplayString):
    """Custom type serialAMCslot12 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SerialAMCslot12_Type.__name__ = "DisplayString"
_SerialAMCslot12_Object = MibTableColumn
serialAMCslot12 = _SerialAMCslot12_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 36),
    _SerialAMCslot12_Type()
)
serialAMCslot12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialAMCslot12.setStatus("mandatory")
_AgentIDAMCslot12_Type = Integer32
_AgentIDAMCslot12_Object = MibTableColumn
agentIDAMCslot12 = _AgentIDAMCslot12_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 37),
    _AgentIDAMCslot12_Type()
)
agentIDAMCslot12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIDAMCslot12.setStatus("mandatory")


class _ValueAMCslot13_Type(Integer32):
    """Custom type valueAMCslot13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("force", 3))
    )


_ValueAMCslot13_Type.__name__ = "Integer32"
_ValueAMCslot13_Object = MibTableColumn
valueAMCslot13 = _ValueAMCslot13_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 38),
    _ValueAMCslot13_Type()
)
valueAMCslot13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueAMCslot13.setStatus("mandatory")


class _SerialAMCslot13_Type(DisplayString):
    """Custom type serialAMCslot13 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SerialAMCslot13_Type.__name__ = "DisplayString"
_SerialAMCslot13_Object = MibTableColumn
serialAMCslot13 = _SerialAMCslot13_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 39),
    _SerialAMCslot13_Type()
)
serialAMCslot13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialAMCslot13.setStatus("mandatory")
_AgentIDAMCslot13_Type = Integer32
_AgentIDAMCslot13_Object = MibTableColumn
agentIDAMCslot13 = _AgentIDAMCslot13_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 40),
    _AgentIDAMCslot13_Type()
)
agentIDAMCslot13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIDAMCslot13.setStatus("mandatory")


class _ValueAMCslot14_Type(Integer32):
    """Custom type valueAMCslot14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("force", 3))
    )


_ValueAMCslot14_Type.__name__ = "Integer32"
_ValueAMCslot14_Object = MibTableColumn
valueAMCslot14 = _ValueAMCslot14_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 41),
    _ValueAMCslot14_Type()
)
valueAMCslot14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueAMCslot14.setStatus("mandatory")


class _SerialAMCslot14_Type(DisplayString):
    """Custom type serialAMCslot14 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SerialAMCslot14_Type.__name__ = "DisplayString"
_SerialAMCslot14_Object = MibTableColumn
serialAMCslot14 = _SerialAMCslot14_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 42),
    _SerialAMCslot14_Type()
)
serialAMCslot14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialAMCslot14.setStatus("mandatory")
_AgentIDAMCslot14_Type = Integer32
_AgentIDAMCslot14_Object = MibTableColumn
agentIDAMCslot14 = _AgentIDAMCslot14_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 43),
    _AgentIDAMCslot14_Type()
)
agentIDAMCslot14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIDAMCslot14.setStatus("mandatory")


class _ValueAMCslot15_Type(Integer32):
    """Custom type valueAMCslot15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("force", 3))
    )


_ValueAMCslot15_Type.__name__ = "Integer32"
_ValueAMCslot15_Object = MibTableColumn
valueAMCslot15 = _ValueAMCslot15_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 44),
    _ValueAMCslot15_Type()
)
valueAMCslot15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueAMCslot15.setStatus("mandatory")


class _SerialAMCslot15_Type(DisplayString):
    """Custom type serialAMCslot15 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SerialAMCslot15_Type.__name__ = "DisplayString"
_SerialAMCslot15_Object = MibTableColumn
serialAMCslot15 = _SerialAMCslot15_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 45),
    _SerialAMCslot15_Type()
)
serialAMCslot15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialAMCslot15.setStatus("mandatory")
_AgentIDAMCslot15_Type = Integer32
_AgentIDAMCslot15_Object = MibTableColumn
agentIDAMCslot15 = _AgentIDAMCslot15_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 46),
    _AgentIDAMCslot15_Type()
)
agentIDAMCslot15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIDAMCslot15.setStatus("mandatory")


class _ValueAMCslot16_Type(Integer32):
    """Custom type valueAMCslot16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("force", 3))
    )


_ValueAMCslot16_Type.__name__ = "Integer32"
_ValueAMCslot16_Object = MibTableColumn
valueAMCslot16 = _ValueAMCslot16_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 47),
    _ValueAMCslot16_Type()
)
valueAMCslot16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueAMCslot16.setStatus("mandatory")


class _SerialAMCslot16_Type(DisplayString):
    """Custom type serialAMCslot16 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SerialAMCslot16_Type.__name__ = "DisplayString"
_SerialAMCslot16_Object = MibTableColumn
serialAMCslot16 = _SerialAMCslot16_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 48),
    _SerialAMCslot16_Type()
)
serialAMCslot16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialAMCslot16.setStatus("mandatory")
_AgentIDAMCslot16_Type = Integer32
_AgentIDAMCslot16_Object = MibTableColumn
agentIDAMCslot16 = _AgentIDAMCslot16_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 49),
    _AgentIDAMCslot16_Type()
)
agentIDAMCslot16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIDAMCslot16.setStatus("mandatory")


class _ValueAMCslot17_Type(Integer32):
    """Custom type valueAMCslot17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("force", 3))
    )


_ValueAMCslot17_Type.__name__ = "Integer32"
_ValueAMCslot17_Object = MibTableColumn
valueAMCslot17 = _ValueAMCslot17_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 50),
    _ValueAMCslot17_Type()
)
valueAMCslot17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueAMCslot17.setStatus("mandatory")


class _SerialAMCslot17_Type(DisplayString):
    """Custom type serialAMCslot17 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SerialAMCslot17_Type.__name__ = "DisplayString"
_SerialAMCslot17_Object = MibTableColumn
serialAMCslot17 = _SerialAMCslot17_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 51),
    _SerialAMCslot17_Type()
)
serialAMCslot17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialAMCslot17.setStatus("mandatory")
_AgentIDAMCslot17_Type = Integer32
_AgentIDAMCslot17_Object = MibTableColumn
agentIDAMCslot17 = _AgentIDAMCslot17_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 52),
    _AgentIDAMCslot17_Type()
)
agentIDAMCslot17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIDAMCslot17.setStatus("mandatory")


class _ValueAMCslot18_Type(Integer32):
    """Custom type valueAMCslot18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("force", 3))
    )


_ValueAMCslot18_Type.__name__ = "Integer32"
_ValueAMCslot18_Object = MibTableColumn
valueAMCslot18 = _ValueAMCslot18_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 53),
    _ValueAMCslot18_Type()
)
valueAMCslot18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueAMCslot18.setStatus("mandatory")


class _SerialAMCslot18_Type(DisplayString):
    """Custom type serialAMCslot18 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SerialAMCslot18_Type.__name__ = "DisplayString"
_SerialAMCslot18_Object = MibTableColumn
serialAMCslot18 = _SerialAMCslot18_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 54),
    _SerialAMCslot18_Type()
)
serialAMCslot18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialAMCslot18.setStatus("mandatory")
_AgentIDAMCslot18_Type = Integer32
_AgentIDAMCslot18_Object = MibTableColumn
agentIDAMCslot18 = _AgentIDAMCslot18_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 55),
    _AgentIDAMCslot18_Type()
)
agentIDAMCslot18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIDAMCslot18.setStatus("mandatory")


class _AutoQuickSwapCnt_Type(Integer32):
    """Custom type autoQuickSwapCnt based on Integer32"""
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
        *(("oneday", 3),
          ("onehour", 2),
          ("oneweek", 4),
          ("timeroff", 1))
    )


_AutoQuickSwapCnt_Type.__name__ = "Integer32"
_AutoQuickSwapCnt_Object = MibTableColumn
autoQuickSwapCnt = _AutoQuickSwapCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 7, 6, 56),
    _AutoQuickSwapCnt_Type()
)
autoQuickSwapCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoQuickSwapCnt.setStatus("mandatory")
_Gx2cmSecurityTable_Object = MibTable
gx2cmSecurityTable = _Gx2cmSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 8)
)
if mibBuilder.loadTexts:
    gx2cmSecurityTable.setStatus("mandatory")
_Gx2cmSecurityEntry_Object = MibTableRow
gx2cmSecurityEntry = _Gx2cmSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 8, 7)
)
gx2cmSecurityEntry.setIndexNames(
    (0, "OMNI-gx2CM-MIB", "gx2cmSecurityTableIndex"),
)
if mibBuilder.loadTexts:
    gx2cmSecurityEntry.setStatus("mandatory")


class _Gx2cmSecurityTableIndex_Type(Integer32):
    """Custom type gx2cmSecurityTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2cmSecurityTableIndex_Type.__name__ = "Integer32"
_Gx2cmSecurityTableIndex_Object = MibTableColumn
gx2cmSecurityTableIndex = _Gx2cmSecurityTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 8, 7, 1),
    _Gx2cmSecurityTableIndex_Type()
)
gx2cmSecurityTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2cmSecurityTableIndex.setStatus("mandatory")


class _LabelSecurityMode_Type(DisplayString):
    """Custom type labelSecurityMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelSecurityMode_Type.__name__ = "DisplayString"
_LabelSecurityMode_Object = MibTableColumn
labelSecurityMode = _LabelSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 8, 7, 2),
    _LabelSecurityMode_Type()
)
labelSecurityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelSecurityMode.setStatus("optional")


class _EnumSecurityMode_Type(DisplayString):
    """Custom type enumSecurityMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EnumSecurityMode_Type.__name__ = "DisplayString"
_EnumSecurityMode_Object = MibTableColumn
enumSecurityMode = _EnumSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 8, 7, 3),
    _EnumSecurityMode_Type()
)
enumSecurityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enumSecurityMode.setStatus("optional")


class _ValueSecurityMode_Type(Integer32):
    """Custom type valueSecurityMode based on Integer32"""
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
        *(("factory-access", 3),
          ("local-write-only", 5),
          ("operator-access", 2),
          ("read-only", 1),
          ("remote-write-only", 4))
    )


_ValueSecurityMode_Type.__name__ = "Integer32"
_ValueSecurityMode_Object = MibTableColumn
valueSecurityMode = _ValueSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 8, 7, 4),
    _ValueSecurityMode_Type()
)
valueSecurityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valueSecurityMode.setStatus("mandatory")


class _StateSecurityMode_Type(Integer32):
    """Custom type stateSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_StateSecurityMode_Type.__name__ = "Integer32"
_StateSecurityMode_Object = MibTableColumn
stateSecurityMode = _StateSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 8, 7, 5),
    _StateSecurityMode_Type()
)
stateSecurityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateSecurityMode.setStatus("mandatory")


class _LabelPassword_Type(DisplayString):
    """Custom type labelPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelPassword_Type.__name__ = "DisplayString"
_LabelPassword_Object = MibTableColumn
labelPassword = _LabelPassword_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 8, 7, 6),
    _LabelPassword_Type()
)
labelPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelPassword.setStatus("optional")


class _ValuePassword_Type(DisplayString):
    """Custom type valuePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ValuePassword_Type.__name__ = "DisplayString"
_ValuePassword_Object = MibTableColumn
valuePassword = _ValuePassword_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 8, 7, 7),
    _ValuePassword_Type()
)
valuePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuePassword.setStatus("mandatory")


class _StatePassword_Type(Integer32):
    """Custom type statePassword based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_StatePassword_Type.__name__ = "Integer32"
_StatePassword_Object = MibTableColumn
statePassword = _StatePassword_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 8, 7, 8),
    _StatePassword_Type()
)
statePassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statePassword.setStatus("mandatory")


class _LabelFactoryChgString_Type(DisplayString):
    """Custom type labelFactoryChgString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelFactoryChgString_Type.__name__ = "DisplayString"
_LabelFactoryChgString_Object = MibTableColumn
labelFactoryChgString = _LabelFactoryChgString_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 8, 7, 9),
    _LabelFactoryChgString_Type()
)
labelFactoryChgString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelFactoryChgString.setStatus("optional")


class _ValueFactoryChgString_Type(DisplayString):
    """Custom type valueFactoryChgString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ValueFactoryChgString_Type.__name__ = "DisplayString"
_ValueFactoryChgString_Object = MibTableColumn
valueFactoryChgString = _ValueFactoryChgString_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 8, 7, 10),
    _ValueFactoryChgString_Type()
)
valueFactoryChgString.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    valueFactoryChgString.setStatus("mandatory")


class _StateFactoryChgString_Type(Integer32):
    """Custom type stateFactoryChgString based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_StateFactoryChgString_Type.__name__ = "Integer32"
_StateFactoryChgString_Object = MibTableColumn
stateFactoryChgString = _StateFactoryChgString_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 8, 7, 11),
    _StateFactoryChgString_Type()
)
stateFactoryChgString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateFactoryChgString.setStatus("mandatory")


class _LabelOperatorChgString_Type(DisplayString):
    """Custom type labelOperatorChgString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelOperatorChgString_Type.__name__ = "DisplayString"
_LabelOperatorChgString_Object = MibTableColumn
labelOperatorChgString = _LabelOperatorChgString_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 8, 7, 12),
    _LabelOperatorChgString_Type()
)
labelOperatorChgString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelOperatorChgString.setStatus("optional")


class _ValueOperatorChgString_Type(DisplayString):
    """Custom type valueOperatorChgString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ValueOperatorChgString_Type.__name__ = "DisplayString"
_ValueOperatorChgString_Object = MibTableColumn
valueOperatorChgString = _ValueOperatorChgString_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 8, 7, 13),
    _ValueOperatorChgString_Type()
)
valueOperatorChgString.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    valueOperatorChgString.setStatus("mandatory")


class _StateOperatorChgString_Type(Integer32):
    """Custom type stateOperatorChgString based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_StateOperatorChgString_Type.__name__ = "Integer32"
_StateOperatorChgString_Object = MibTableColumn
stateOperatorChgString = _StateOperatorChgString_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 8, 7, 14),
    _StateOperatorChgString_Type()
)
stateOperatorChgString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateOperatorChgString.setStatus("mandatory")


class _LabelReadOnlyChgString_Type(DisplayString):
    """Custom type labelReadOnlyChgString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelReadOnlyChgString_Type.__name__ = "DisplayString"
_LabelReadOnlyChgString_Object = MibTableColumn
labelReadOnlyChgString = _LabelReadOnlyChgString_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 8, 7, 15),
    _LabelReadOnlyChgString_Type()
)
labelReadOnlyChgString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelReadOnlyChgString.setStatus("optional")


class _ValueReadOnlyChgString_Type(DisplayString):
    """Custom type valueReadOnlyChgString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ValueReadOnlyChgString_Type.__name__ = "DisplayString"
_ValueReadOnlyChgString_Object = MibTableColumn
valueReadOnlyChgString = _ValueReadOnlyChgString_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 8, 7, 16),
    _ValueReadOnlyChgString_Type()
)
valueReadOnlyChgString.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    valueReadOnlyChgString.setStatus("mandatory")


class _StateReadOnlyChgString_Type(Integer32):
    """Custom type stateReadOnlyChgString based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_StateReadOnlyChgString_Type.__name__ = "Integer32"
_StateReadOnlyChgString_Object = MibTableColumn
stateReadOnlyChgString = _StateReadOnlyChgString_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 8, 7, 17),
    _StateReadOnlyChgString_Type()
)
stateReadOnlyChgString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateReadOnlyChgString.setStatus("mandatory")


class _LabelRemoteOnlyChgString_Type(DisplayString):
    """Custom type labelRemoteOnlyChgString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelRemoteOnlyChgString_Type.__name__ = "DisplayString"
_LabelRemoteOnlyChgString_Object = MibTableColumn
labelRemoteOnlyChgString = _LabelRemoteOnlyChgString_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 8, 7, 18),
    _LabelRemoteOnlyChgString_Type()
)
labelRemoteOnlyChgString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelRemoteOnlyChgString.setStatus("optional")


class _ValueRemoteOnlyChgString_Type(DisplayString):
    """Custom type valueRemoteOnlyChgString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ValueRemoteOnlyChgString_Type.__name__ = "DisplayString"
_ValueRemoteOnlyChgString_Object = MibTableColumn
valueRemoteOnlyChgString = _ValueRemoteOnlyChgString_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 8, 7, 19),
    _ValueRemoteOnlyChgString_Type()
)
valueRemoteOnlyChgString.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    valueRemoteOnlyChgString.setStatus("mandatory")


class _StateRemoteOnlyChgString_Type(Integer32):
    """Custom type stateRemoteOnlyChgString based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_StateRemoteOnlyChgString_Type.__name__ = "Integer32"
_StateRemoteOnlyChgString_Object = MibTableColumn
stateRemoteOnlyChgString = _StateRemoteOnlyChgString_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 8, 7, 20),
    _StateRemoteOnlyChgString_Type()
)
stateRemoteOnlyChgString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateRemoteOnlyChgString.setStatus("mandatory")


class _LabelLocalOnlyChgString_Type(DisplayString):
    """Custom type labelLocalOnlyChgString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LabelLocalOnlyChgString_Type.__name__ = "DisplayString"
_LabelLocalOnlyChgString_Object = MibTableColumn
labelLocalOnlyChgString = _LabelLocalOnlyChgString_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 8, 7, 21),
    _LabelLocalOnlyChgString_Type()
)
labelLocalOnlyChgString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelLocalOnlyChgString.setStatus("optional")


class _ValueLocalOnlyChgString_Type(DisplayString):
    """Custom type valueLocalOnlyChgString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ValueLocalOnlyChgString_Type.__name__ = "DisplayString"
_ValueLocalOnlyChgString_Object = MibTableColumn
valueLocalOnlyChgString = _ValueLocalOnlyChgString_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 8, 7, 22),
    _ValueLocalOnlyChgString_Type()
)
valueLocalOnlyChgString.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    valueLocalOnlyChgString.setStatus("mandatory")


class _StateLocalOnlyChgString_Type(Integer32):
    """Custom type stateLocalOnlyChgString based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_StateLocalOnlyChgString_Type.__name__ = "Integer32"
_StateLocalOnlyChgString_Object = MibTableColumn
stateLocalOnlyChgString = _StateLocalOnlyChgString_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 8, 7, 23),
    _StateLocalOnlyChgString_Type()
)
stateLocalOnlyChgString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateLocalOnlyChgString.setStatus("mandatory")
_Gx2cmDiagnosticTable_Object = MibTable
gx2cmDiagnosticTable = _Gx2cmDiagnosticTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9)
)
if mibBuilder.loadTexts:
    gx2cmDiagnosticTable.setStatus("mandatory")
_Gx2cmDiagnosticEntry_Object = MibTableRow
gx2cmDiagnosticEntry = _Gx2cmDiagnosticEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8)
)
gx2cmDiagnosticEntry.setIndexNames(
    (0, "OMNI-gx2CM-MIB", "gx2cmDiagnosticTableIndex"),
)
if mibBuilder.loadTexts:
    gx2cmDiagnosticEntry.setStatus("mandatory")


class _Gx2cmDiagnosticTableIndex_Type(Integer32):
    """Custom type gx2cmDiagnosticTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2cmDiagnosticTableIndex_Type.__name__ = "Integer32"
_Gx2cmDiagnosticTableIndex_Object = MibTableColumn
gx2cmDiagnosticTableIndex = _Gx2cmDiagnosticTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 1),
    _Gx2cmDiagnosticTableIndex_Type()
)
gx2cmDiagnosticTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2cmDiagnosticTableIndex.setStatus("mandatory")


class _LedTestValue_Type(Integer32):
    """Custom type ledTestValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_LedTestValue_Type.__name__ = "Integer32"
_LedTestValue_Object = MibTableColumn
ledTestValue = _LedTestValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 2),
    _LedTestValue_Type()
)
ledTestValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ledTestValue.setStatus("mandatory")
_BpTestCnt_Type = Integer32
_BpTestCnt_Object = MibTableColumn
bpTestCnt = _BpTestCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 3),
    _BpTestCnt_Type()
)
bpTestCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bpTestCnt.setStatus("mandatory")
_SuccessTransSlot1_Type = Integer32
_SuccessTransSlot1_Object = MibTableColumn
successTransSlot1 = _SuccessTransSlot1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 4),
    _SuccessTransSlot1_Type()
)
successTransSlot1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    successTransSlot1.setStatus("mandatory")
_SuccessTransSlot2_Type = Integer32
_SuccessTransSlot2_Object = MibTableColumn
successTransSlot2 = _SuccessTransSlot2_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 5),
    _SuccessTransSlot2_Type()
)
successTransSlot2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    successTransSlot2.setStatus("mandatory")
_SuccessTransSlot3_Type = Integer32
_SuccessTransSlot3_Object = MibTableColumn
successTransSlot3 = _SuccessTransSlot3_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 6),
    _SuccessTransSlot3_Type()
)
successTransSlot3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    successTransSlot3.setStatus("mandatory")
_SuccessTransSlot4_Type = Integer32
_SuccessTransSlot4_Object = MibTableColumn
successTransSlot4 = _SuccessTransSlot4_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 7),
    _SuccessTransSlot4_Type()
)
successTransSlot4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    successTransSlot4.setStatus("mandatory")
_SuccessTransSlot5_Type = Integer32
_SuccessTransSlot5_Object = MibTableColumn
successTransSlot5 = _SuccessTransSlot5_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 8),
    _SuccessTransSlot5_Type()
)
successTransSlot5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    successTransSlot5.setStatus("mandatory")
_SuccessTransSlot6_Type = Integer32
_SuccessTransSlot6_Object = MibTableColumn
successTransSlot6 = _SuccessTransSlot6_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 9),
    _SuccessTransSlot6_Type()
)
successTransSlot6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    successTransSlot6.setStatus("mandatory")
_SuccessTransSlot7_Type = Integer32
_SuccessTransSlot7_Object = MibTableColumn
successTransSlot7 = _SuccessTransSlot7_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 10),
    _SuccessTransSlot7_Type()
)
successTransSlot7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    successTransSlot7.setStatus("mandatory")
_SuccessTransSlot8_Type = Integer32
_SuccessTransSlot8_Object = MibTableColumn
successTransSlot8 = _SuccessTransSlot8_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 11),
    _SuccessTransSlot8_Type()
)
successTransSlot8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    successTransSlot8.setStatus("mandatory")
_SuccessTransSlot9_Type = Integer32
_SuccessTransSlot9_Object = MibTableColumn
successTransSlot9 = _SuccessTransSlot9_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 12),
    _SuccessTransSlot9_Type()
)
successTransSlot9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    successTransSlot9.setStatus("mandatory")
_SuccessTransSlot10_Type = Integer32
_SuccessTransSlot10_Object = MibTableColumn
successTransSlot10 = _SuccessTransSlot10_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 13),
    _SuccessTransSlot10_Type()
)
successTransSlot10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    successTransSlot10.setStatus("mandatory")
_SuccessTransSlot11_Type = Integer32
_SuccessTransSlot11_Object = MibTableColumn
successTransSlot11 = _SuccessTransSlot11_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 14),
    _SuccessTransSlot11_Type()
)
successTransSlot11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    successTransSlot11.setStatus("mandatory")
_SuccessTransSlot12_Type = Integer32
_SuccessTransSlot12_Object = MibTableColumn
successTransSlot12 = _SuccessTransSlot12_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 15),
    _SuccessTransSlot12_Type()
)
successTransSlot12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    successTransSlot12.setStatus("mandatory")
_SuccessTransSlot13_Type = Integer32
_SuccessTransSlot13_Object = MibTableColumn
successTransSlot13 = _SuccessTransSlot13_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 16),
    _SuccessTransSlot13_Type()
)
successTransSlot13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    successTransSlot13.setStatus("mandatory")
_SuccessTransSlot14_Type = Integer32
_SuccessTransSlot14_Object = MibTableColumn
successTransSlot14 = _SuccessTransSlot14_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 17),
    _SuccessTransSlot14_Type()
)
successTransSlot14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    successTransSlot14.setStatus("mandatory")
_SuccessTransSlot15_Type = Integer32
_SuccessTransSlot15_Object = MibTableColumn
successTransSlot15 = _SuccessTransSlot15_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 18),
    _SuccessTransSlot15_Type()
)
successTransSlot15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    successTransSlot15.setStatus("mandatory")
_SuccessTransSlot16_Type = Integer32
_SuccessTransSlot16_Object = MibTableColumn
successTransSlot16 = _SuccessTransSlot16_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 19),
    _SuccessTransSlot16_Type()
)
successTransSlot16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    successTransSlot16.setStatus("mandatory")
_SuccessTransSlot17_Type = Integer32
_SuccessTransSlot17_Object = MibTableColumn
successTransSlot17 = _SuccessTransSlot17_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 20),
    _SuccessTransSlot17_Type()
)
successTransSlot17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    successTransSlot17.setStatus("mandatory")
_SuccessTransSlot18_Type = Integer32
_SuccessTransSlot18_Object = MibTableColumn
successTransSlot18 = _SuccessTransSlot18_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 21),
    _SuccessTransSlot18_Type()
)
successTransSlot18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    successTransSlot18.setStatus("mandatory")
_FailureTransSlot1_Type = Integer32
_FailureTransSlot1_Object = MibTableColumn
failureTransSlot1 = _FailureTransSlot1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 22),
    _FailureTransSlot1_Type()
)
failureTransSlot1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    failureTransSlot1.setStatus("mandatory")
_FailureTransSlot2_Type = Integer32
_FailureTransSlot2_Object = MibTableColumn
failureTransSlot2 = _FailureTransSlot2_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 23),
    _FailureTransSlot2_Type()
)
failureTransSlot2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    failureTransSlot2.setStatus("mandatory")
_FailureTransSlot3_Type = Integer32
_FailureTransSlot3_Object = MibTableColumn
failureTransSlot3 = _FailureTransSlot3_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 24),
    _FailureTransSlot3_Type()
)
failureTransSlot3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    failureTransSlot3.setStatus("mandatory")
_FailureTransSlot4_Type = Integer32
_FailureTransSlot4_Object = MibTableColumn
failureTransSlot4 = _FailureTransSlot4_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 25),
    _FailureTransSlot4_Type()
)
failureTransSlot4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    failureTransSlot4.setStatus("mandatory")
_FailureTransSlot5_Type = Integer32
_FailureTransSlot5_Object = MibTableColumn
failureTransSlot5 = _FailureTransSlot5_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 26),
    _FailureTransSlot5_Type()
)
failureTransSlot5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    failureTransSlot5.setStatus("mandatory")
_FailureTransSlot6_Type = Integer32
_FailureTransSlot6_Object = MibTableColumn
failureTransSlot6 = _FailureTransSlot6_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 27),
    _FailureTransSlot6_Type()
)
failureTransSlot6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    failureTransSlot6.setStatus("mandatory")
_FailureTransSlot7_Type = Integer32
_FailureTransSlot7_Object = MibTableColumn
failureTransSlot7 = _FailureTransSlot7_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 28),
    _FailureTransSlot7_Type()
)
failureTransSlot7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    failureTransSlot7.setStatus("mandatory")
_FailureTransSlot8_Type = Integer32
_FailureTransSlot8_Object = MibTableColumn
failureTransSlot8 = _FailureTransSlot8_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 29),
    _FailureTransSlot8_Type()
)
failureTransSlot8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    failureTransSlot8.setStatus("mandatory")
_FailureTransSlot9_Type = Integer32
_FailureTransSlot9_Object = MibTableColumn
failureTransSlot9 = _FailureTransSlot9_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 30),
    _FailureTransSlot9_Type()
)
failureTransSlot9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    failureTransSlot9.setStatus("mandatory")
_FailureTransSlot10_Type = Integer32
_FailureTransSlot10_Object = MibTableColumn
failureTransSlot10 = _FailureTransSlot10_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 31),
    _FailureTransSlot10_Type()
)
failureTransSlot10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    failureTransSlot10.setStatus("mandatory")
_FailureTransSlot11_Type = Integer32
_FailureTransSlot11_Object = MibTableColumn
failureTransSlot11 = _FailureTransSlot11_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 32),
    _FailureTransSlot11_Type()
)
failureTransSlot11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    failureTransSlot11.setStatus("mandatory")
_FailureTransSlot12_Type = Integer32
_FailureTransSlot12_Object = MibTableColumn
failureTransSlot12 = _FailureTransSlot12_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 33),
    _FailureTransSlot12_Type()
)
failureTransSlot12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    failureTransSlot12.setStatus("mandatory")
_FailureTransSlot13_Type = Integer32
_FailureTransSlot13_Object = MibTableColumn
failureTransSlot13 = _FailureTransSlot13_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 34),
    _FailureTransSlot13_Type()
)
failureTransSlot13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    failureTransSlot13.setStatus("mandatory")
_FailureTransSlot14_Type = Integer32
_FailureTransSlot14_Object = MibTableColumn
failureTransSlot14 = _FailureTransSlot14_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 35),
    _FailureTransSlot14_Type()
)
failureTransSlot14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    failureTransSlot14.setStatus("mandatory")
_FailureTransSlot15_Type = Integer32
_FailureTransSlot15_Object = MibTableColumn
failureTransSlot15 = _FailureTransSlot15_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 36),
    _FailureTransSlot15_Type()
)
failureTransSlot15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    failureTransSlot15.setStatus("mandatory")
_FailureTransSlot16_Type = Integer32
_FailureTransSlot16_Object = MibTableColumn
failureTransSlot16 = _FailureTransSlot16_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 37),
    _FailureTransSlot16_Type()
)
failureTransSlot16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    failureTransSlot16.setStatus("mandatory")
_FailureTransSlot17_Type = Integer32
_FailureTransSlot17_Object = MibTableColumn
failureTransSlot17 = _FailureTransSlot17_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 38),
    _FailureTransSlot17_Type()
)
failureTransSlot17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    failureTransSlot17.setStatus("mandatory")
_FailureTransSlot18_Type = Integer32
_FailureTransSlot18_Object = MibTableColumn
failureTransSlot18 = _FailureTransSlot18_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 39),
    _FailureTransSlot18_Type()
)
failureTransSlot18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    failureTransSlot18.setStatus("mandatory")
_FanTestMode_Type = Integer32
_FanTestMode_Object = MibTableColumn
fanTestMode = _FanTestMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 40),
    _FanTestMode_Type()
)
fanTestMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanTestMode.setStatus("mandatory")


class _FanControl_Type(Integer32):
    """Custom type fanControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FanControl_Type.__name__ = "Integer32"
_FanControl_Object = MibTableColumn
fanControl = _FanControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 41),
    _FanControl_Type()
)
fanControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanControl.setStatus("mandatory")
_RelayTestMode_Type = Integer32
_RelayTestMode_Object = MibTableColumn
relayTestMode = _RelayTestMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 42),
    _RelayTestMode_Type()
)
relayTestMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayTestMode.setStatus("mandatory")


class _RelayControl_Type(Integer32):
    """Custom type relayControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 1))
    )


_RelayControl_Type.__name__ = "Integer32"
_RelayControl_Object = MibTableColumn
relayControl = _RelayControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 43),
    _RelayControl_Type()
)
relayControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayControl.setStatus("mandatory")


class _SlotPollMode_Type(Integer32):
    """Custom type slotPollMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_SlotPollMode_Type.__name__ = "Integer32"
_SlotPollMode_Object = MibTableColumn
slotPollMode = _SlotPollMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 44),
    _SlotPollMode_Type()
)
slotPollMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotPollMode.setStatus("mandatory")
_BootCount_Type = Integer32
_BootCount_Object = MibTableColumn
bootCount = _BootCount_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 45),
    _BootCount_Type()
)
bootCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootCount.setStatus("mandatory")


class _ObjectTableData_Type(DisplayString):
    """Custom type objectTableData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ObjectTableData_Type.__name__ = "DisplayString"
_ObjectTableData_Object = MibTableColumn
objectTableData = _ObjectTableData_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 46),
    _ObjectTableData_Type()
)
objectTableData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    objectTableData.setStatus("mandatory")
_SetSysTime_Type = Integer32
_SetSysTime_Object = MibTableColumn
setSysTime = _SetSysTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 9, 8, 47),
    _SetSysTime_Type()
)
setSysTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setSysTime.setStatus("mandatory")
_Gx2cmDownloadTable_Object = MibTable
gx2cmDownloadTable = _Gx2cmDownloadTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 10)
)
if mibBuilder.loadTexts:
    gx2cmDownloadTable.setStatus("mandatory")
_Gx2cmDownloadEntry_Object = MibTableRow
gx2cmDownloadEntry = _Gx2cmDownloadEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 10, 9)
)
gx2cmDownloadEntry.setIndexNames(
    (0, "OMNI-gx2CM-MIB", "gx2cmDownloadTableIndex"),
)
if mibBuilder.loadTexts:
    gx2cmDownloadEntry.setStatus("mandatory")


class _Gx2cmDownloadTableIndex_Type(Integer32):
    """Custom type gx2cmDownloadTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2cmDownloadTableIndex_Type.__name__ = "Integer32"
_Gx2cmDownloadTableIndex_Object = MibTableColumn
gx2cmDownloadTableIndex = _Gx2cmDownloadTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 10, 9, 1),
    _Gx2cmDownloadTableIndex_Type()
)
gx2cmDownloadTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2cmDownloadTableIndex.setStatus("mandatory")
_DownloadValue_Type = Integer32
_DownloadValue_Object = MibTableColumn
downloadValue = _DownloadValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 10, 9, 2),
    _DownloadValue_Type()
)
downloadValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadValue.setStatus("mandatory")


class _AutoDownloadReset_Type(Integer32):
    """Custom type autoDownloadReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 2),
          ("deactivate", 1))
    )


_AutoDownloadReset_Type.__name__ = "Integer32"
_AutoDownloadReset_Object = MibTableColumn
autoDownloadReset = _AutoDownloadReset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 10, 9, 3),
    _AutoDownloadReset_Type()
)
autoDownloadReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoDownloadReset.setStatus("mandatory")


class _DownloadFilename_Type(DisplayString):
    """Custom type downloadFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DownloadFilename_Type.__name__ = "DisplayString"
_DownloadFilename_Object = MibTableColumn
downloadFilename = _DownloadFilename_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 10, 9, 4),
    _DownloadFilename_Type()
)
downloadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadFilename.setStatus("mandatory")
_DownloadState_Type = Integer32
_DownloadState_Object = MibTableColumn
downloadState = _DownloadState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 10, 9, 5),
    _DownloadState_Type()
)
downloadState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadState.setStatus("mandatory")
_SwitchFwBank_Type = Integer32
_SwitchFwBank_Object = MibTableColumn
switchFwBank = _SwitchFwBank_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 10, 9, 6),
    _SwitchFwBank_Type()
)
switchFwBank.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchFwBank.setStatus("mandatory")
_CmTrapHistoryTable_Object = MibTable
cmTrapHistoryTable = _CmTrapHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 11)
)
if mibBuilder.loadTexts:
    cmTrapHistoryTable.setStatus("mandatory")
_CmTrapHistoryEntry_Object = MibTableRow
cmTrapHistoryEntry = _CmTrapHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 11, 10)
)
cmTrapHistoryEntry.setIndexNames(
    (0, "OMNI-gx2CM-MIB", "cmTrapHistoryTableIndex"),
)
if mibBuilder.loadTexts:
    cmTrapHistoryEntry.setStatus("mandatory")


class _CmTrapHistoryTableIndex_Type(Integer32):
    """Custom type cmTrapHistoryTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmTrapHistoryTableIndex_Type.__name__ = "Integer32"
_CmTrapHistoryTableIndex_Object = MibTableColumn
cmTrapHistoryTableIndex = _CmTrapHistoryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 11, 10, 1),
    _CmTrapHistoryTableIndex_Type()
)
cmTrapHistoryTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapHistoryTableIndex.setStatus("mandatory")


class _NetrapId_Type(Integer32):
    """Custom type netrapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NetrapId_Type.__name__ = "Integer32"
_NetrapId_Object = MibTableColumn
netrapId = _NetrapId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 11, 10, 2),
    _NetrapId_Type()
)
netrapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netrapId.setStatus("mandatory")


class _NetrapNetworkElemModelNumber_Type(DisplayString):
    """Custom type netrapNetworkElemModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NetrapNetworkElemModelNumber_Type.__name__ = "DisplayString"
_NetrapNetworkElemModelNumber_Object = MibTableColumn
netrapNetworkElemModelNumber = _NetrapNetworkElemModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 11, 10, 3),
    _NetrapNetworkElemModelNumber_Type()
)
netrapNetworkElemModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netrapNetworkElemModelNumber.setStatus("mandatory")


class _NetrapNetworkElemSerialNum_Type(DisplayString):
    """Custom type netrapNetworkElemSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NetrapNetworkElemSerialNum_Type.__name__ = "DisplayString"
_NetrapNetworkElemSerialNum_Object = MibTableColumn
netrapNetworkElemSerialNum = _NetrapNetworkElemSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 11, 10, 4),
    _NetrapNetworkElemSerialNum_Type()
)
netrapNetworkElemSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netrapNetworkElemSerialNum.setStatus("mandatory")


class _NetrapPerceivedSeverity_Type(Integer32):
    """Custom type netrapPerceivedSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NetrapPerceivedSeverity_Type.__name__ = "Integer32"
_NetrapPerceivedSeverity_Object = MibTableColumn
netrapPerceivedSeverity = _NetrapPerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 11, 10, 5),
    _NetrapPerceivedSeverity_Type()
)
netrapPerceivedSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netrapPerceivedSeverity.setStatus("mandatory")


class _NetrapNetworkElemOperState_Type(Integer32):
    """Custom type netrapNetworkElemOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NetrapNetworkElemOperState_Type.__name__ = "Integer32"
_NetrapNetworkElemOperState_Object = MibTableColumn
netrapNetworkElemOperState = _NetrapNetworkElemOperState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 11, 10, 6),
    _NetrapNetworkElemOperState_Type()
)
netrapNetworkElemOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netrapNetworkElemOperState.setStatus("mandatory")


class _NetrapNetworkElemAlarmStatus_Type(Integer32):
    """Custom type netrapNetworkElemAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NetrapNetworkElemAlarmStatus_Type.__name__ = "Integer32"
_NetrapNetworkElemAlarmStatus_Object = MibTableColumn
netrapNetworkElemAlarmStatus = _NetrapNetworkElemAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 11, 10, 7),
    _NetrapNetworkElemAlarmStatus_Type()
)
netrapNetworkElemAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netrapNetworkElemAlarmStatus.setStatus("mandatory")


class _NetrapNetworkElemAdminState_Type(Integer32):
    """Custom type netrapNetworkElemAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NetrapNetworkElemAdminState_Type.__name__ = "Integer32"
_NetrapNetworkElemAdminState_Object = MibTableColumn
netrapNetworkElemAdminState = _NetrapNetworkElemAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 11, 10, 8),
    _NetrapNetworkElemAdminState_Type()
)
netrapNetworkElemAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netrapNetworkElemAdminState.setStatus("mandatory")


class _NetrapNetworkElemAvailStatus_Type(Integer32):
    """Custom type netrapNetworkElemAvailStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NetrapNetworkElemAvailStatus_Type.__name__ = "Integer32"
_NetrapNetworkElemAvailStatus_Object = MibTableColumn
netrapNetworkElemAvailStatus = _NetrapNetworkElemAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 11, 10, 9),
    _NetrapNetworkElemAvailStatus_Type()
)
netrapNetworkElemAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netrapNetworkElemAvailStatus.setStatus("mandatory")


class _NetrapText_Type(DisplayString):
    """Custom type netrapText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NetrapText_Type.__name__ = "DisplayString"
_NetrapText_Object = MibTableColumn
netrapText = _NetrapText_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 11, 10, 10),
    _NetrapText_Type()
)
netrapText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netrapText.setStatus("mandatory")
_NetrapLastTrapTimeStamp_Type = TimeTicks
_NetrapLastTrapTimeStamp_Object = MibTableColumn
netrapLastTrapTimeStamp = _NetrapLastTrapTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 11, 10, 11),
    _NetrapLastTrapTimeStamp_Type()
)
netrapLastTrapTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netrapLastTrapTimeStamp.setStatus("mandatory")


class _NetrapChangedObjectId_Type(DisplayString):
    """Custom type netrapChangedObjectId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NetrapChangedObjectId_Type.__name__ = "DisplayString"
_NetrapChangedObjectId_Object = MibTableColumn
netrapChangedObjectId = _NetrapChangedObjectId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 11, 10, 12),
    _NetrapChangedObjectId_Type()
)
netrapChangedObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netrapChangedObjectId.setStatus("mandatory")


class _NetrapAdditionalInfoInteger1_Type(Integer32):
    """Custom type netrapAdditionalInfoInteger1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NetrapAdditionalInfoInteger1_Type.__name__ = "Integer32"
_NetrapAdditionalInfoInteger1_Object = MibTableColumn
netrapAdditionalInfoInteger1 = _NetrapAdditionalInfoInteger1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 11, 10, 13),
    _NetrapAdditionalInfoInteger1_Type()
)
netrapAdditionalInfoInteger1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netrapAdditionalInfoInteger1.setStatus("mandatory")


class _NetrapAdditionalInfoInteger2_Type(Integer32):
    """Custom type netrapAdditionalInfoInteger2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NetrapAdditionalInfoInteger2_Type.__name__ = "Integer32"
_NetrapAdditionalInfoInteger2_Object = MibTableColumn
netrapAdditionalInfoInteger2 = _NetrapAdditionalInfoInteger2_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 11, 10, 14),
    _NetrapAdditionalInfoInteger2_Type()
)
netrapAdditionalInfoInteger2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netrapAdditionalInfoInteger2.setStatus("mandatory")


class _NetrapAdditionalInfoInteger3_Type(Integer32):
    """Custom type netrapAdditionalInfoInteger3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NetrapAdditionalInfoInteger3_Type.__name__ = "Integer32"
_NetrapAdditionalInfoInteger3_Object = MibTableColumn
netrapAdditionalInfoInteger3 = _NetrapAdditionalInfoInteger3_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 11, 10, 15),
    _NetrapAdditionalInfoInteger3_Type()
)
netrapAdditionalInfoInteger3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netrapAdditionalInfoInteger3.setStatus("mandatory")


class _NetrapChangedValueDisplayString_Type(DisplayString):
    """Custom type netrapChangedValueDisplayString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NetrapChangedValueDisplayString_Type.__name__ = "DisplayString"
_NetrapChangedValueDisplayString_Object = MibTableColumn
netrapChangedValueDisplayString = _NetrapChangedValueDisplayString_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 11, 10, 16),
    _NetrapChangedValueDisplayString_Type()
)
netrapChangedValueDisplayString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netrapChangedValueDisplayString.setStatus("mandatory")


class _NetrapChangedValueOID_Type(DisplayString):
    """Custom type netrapChangedValueOID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NetrapChangedValueOID_Type.__name__ = "DisplayString"
_NetrapChangedValueOID_Object = MibTableColumn
netrapChangedValueOID = _NetrapChangedValueOID_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 11, 10, 17),
    _NetrapChangedValueOID_Type()
)
netrapChangedValueOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netrapChangedValueOID.setStatus("mandatory")


class _NetrapChangedValueIpAddress_Type(Integer32):
    """Custom type netrapChangedValueIpAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NetrapChangedValueIpAddress_Type.__name__ = "Integer32"
_NetrapChangedValueIpAddress_Object = MibTableColumn
netrapChangedValueIpAddress = _NetrapChangedValueIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 11, 10, 18),
    _NetrapChangedValueIpAddress_Type()
)
netrapChangedValueIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netrapChangedValueIpAddress.setStatus("mandatory")


class _NetrapChangedValueInteger_Type(Integer32):
    """Custom type netrapChangedValueInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NetrapChangedValueInteger_Type.__name__ = "Integer32"
_NetrapChangedValueInteger_Object = MibTableColumn
netrapChangedValueInteger = _NetrapChangedValueInteger_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 11, 10, 19),
    _NetrapChangedValueInteger_Type()
)
netrapChangedValueInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netrapChangedValueInteger.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapCMConfigChangeInteger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 0, 1)
)
trapCMConfigChangeInteger.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapCMConfigChangeInteger.setStatus(
        ""
    )

trapCMConfigChangeDisplayString = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 0, 2)
)
trapCMConfigChangeDisplayString.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueDisplayString"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapCMConfigChangeDisplayString.setStatus(
        ""
    )

trapCMModuleTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 0, 3)
)
trapCMModuleTempAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapCMModuleTempAlarm.setStatus(
        ""
    )

trapCMEEPROMAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 0, 4)
)
trapCMEEPROMAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapCMEEPROMAlarm.setStatus(
        ""
    )

trapCMFlashAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 0, 5)
)
trapCMFlashAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapCMFlashAlarm.setStatus(
        ""
    )

trapCMHardwareAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 0, 6)
)
trapCMHardwareAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapCMHardwareAlarm.setStatus(
        ""
    )

trapCMInitEEPROMAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 0, 7)
)
trapCMInitEEPROMAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapCMInitEEPROMAlarm.setStatus(
        ""
    )

trapCMBootAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3, 0, 8)
)
trapCMBootAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapCMBootAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNI-gx2CM-MIB",
    **{"Float": Float,
       "trapCMConfigChangeInteger": trapCMConfigChangeInteger,
       "trapCMConfigChangeDisplayString": trapCMConfigChangeDisplayString,
       "trapCMModuleTempAlarm": trapCMModuleTempAlarm,
       "trapCMEEPROMAlarm": trapCMEEPROMAlarm,
       "trapCMFlashAlarm": trapCMFlashAlarm,
       "trapCMHardwareAlarm": trapCMHardwareAlarm,
       "trapCMInitEEPROMAlarm": trapCMInitEEPROMAlarm,
       "trapCMBootAlarm": trapCMBootAlarm,
       "gx2cmDescriptor": gx2cmDescriptor,
       "gx2cmFactoryTable": gx2cmFactoryTable,
       "gx2cmFactoryEntry": gx2cmFactoryEntry,
       "gx2cmFactoryTableIndex": gx2cmFactoryTableIndex,
       "bootControlByte": bootControlByte,
       "bootStatusByte": bootStatusByte,
       "bank0CRC": bank0CRC,
       "bank1CRC": bank1CRC,
       "prgEEPROMByte": prgEEPROMByte,
       "factoryCRC": factoryCRC,
       "calculateCRC": calculateCRC,
       "hourMeter": hourMeter,
       "flashPrgCnt0": flashPrgCnt0,
       "flashPrgCnt1": flashPrgCnt1,
       "flashBank0": flashBank0,
       "flashBank1": flashBank1,
       "localMacAdd": localMacAdd,
       "netWorkMacAdd": netWorkMacAdd,
       "gx2cmNetworkTable": gx2cmNetworkTable,
       "gx2cmNetworkEntry": gx2cmNetworkEntry,
       "gx2cmNetworkTableIndex": gx2cmNetworkTableIndex,
       "labelLocalEthIPAdd": labelLocalEthIPAdd,
       "valueLocalEthIPAdd": valueLocalEthIPAdd,
       "labelLocalEthMask": labelLocalEthMask,
       "valueLocalEthMask": valueLocalEthMask,
       "labelNetworkEthAdd": labelNetworkEthAdd,
       "valueNetworkEthAdd": valueNetworkEthAdd,
       "labelNetworkEthMask": labelNetworkEthMask,
       "valueNetworkEthMask": valueNetworkEthMask,
       "labelShelfSerialNum": labelShelfSerialNum,
       "valueShelfSerialNum": valueShelfSerialNum,
       "labelGateWayIPAdd": labelGateWayIPAdd,
       "valueGateWayIPAdd": valueGateWayIPAdd,
       "labelTrapDestination": labelTrapDestination,
       "valueTrapDestination": valueTrapDestination,
       "labelTFTPserver": labelTFTPserver,
       "valueTFTPserver": valueTFTPserver,
       "labelTrap2Destination": labelTrap2Destination,
       "valueTrap2Destination": valueTrap2Destination,
       "labelTrap3Destination": labelTrap3Destination,
       "valueTrap3Destination": valueTrap3Destination,
       "labelTrap4Destination": labelTrap4Destination,
       "valueTrap4Destination": valueTrap4Destination,
       "labelTrap5Destination": labelTrap5Destination,
       "valueTrap5Destination": valueTrap5Destination,
       "labelISDNMode": labelISDNMode,
       "valueISDNMode": valueISDNMode,
       "labelISDNModemIPAddress": labelISDNModemIPAddress,
       "valueISDNModemIPAddress": valueISDNModemIPAddress,
       "labelISDNTrapTimeout": labelISDNTrapTimeout,
       "valueISDNTrapTimeout": valueISDNTrapTimeout,
       "labelISDNPingTimeout": labelISDNPingTimeout,
       "valueISDNPingTimeout": valueISDNPingTimeout,
       "labelISDNBackoffTimer": labelISDNBackoffTimer,
       "valueISDNBackoffTimer": valueISDNBackoffTimer,
       "gx2cmAnalogTable": gx2cmAnalogTable,
       "gx2cmAnalogEntry": gx2cmAnalogEntry,
       "gx2cmTableIndex": gx2cmTableIndex,
       "labelModTemp": labelModTemp,
       "uomModTemp": uomModTemp,
       "majorHighModTemp": majorHighModTemp,
       "majorLowModTemp": majorLowModTemp,
       "minorHighModTemp": minorHighModTemp,
       "minorLowModTemp": minorLowModTemp,
       "currentValueModTemp": currentValueModTemp,
       "stateFlagModTemp": stateFlagModTemp,
       "minValueModTemp": minValueModTemp,
       "maxValueModTemp": maxValueModTemp,
       "alarmStateModTemp": alarmStateModTemp,
       "gx2cmDigitalTable": gx2cmDigitalTable,
       "gx2cmDigitalEntry": gx2cmDigitalEntry,
       "gx2cmDigitalTableIndex": gx2cmDigitalTableIndex,
       "labelRemoteLocal": labelRemoteLocal,
       "enumRemoteLocal": enumRemoteLocal,
       "valueRemoteLocal": valueRemoteLocal,
       "stateFlagRemoteLocal": stateFlagRemoteLocal,
       "labelResetSlot": labelResetSlot,
       "enumResetSlot": enumResetSlot,
       "valueResetSlot": valueResetSlot,
       "stateResetSlot": stateResetSlot,
       "labelIdShelf": labelIdShelf,
       "enumIdShelf": enumIdShelf,
       "valueIdShelf": valueIdShelf,
       "stateFlagIdShelf": stateFlagIdShelf,
       "labelResetAlarm": labelResetAlarm,
       "enumResetAlarm": enumResetAlarm,
       "valueResetAlarm": valueResetAlarm,
       "stateFlagResetAlarm": stateFlagResetAlarm,
       "gx2cmStatusTable": gx2cmStatusTable,
       "gx2cmStatusEntry": gx2cmStatusEntry,
       "gx2cmStatusTableIndex": gx2cmStatusTableIndex,
       "labelShelfAlarm": labelShelfAlarm,
       "valueShelfAlarm": valueShelfAlarm,
       "stateShelfAlarm": stateShelfAlarm,
       "labelDataCrc": labelDataCrc,
       "valueDataCrc": valueDataCrc,
       "stateDataCrc": stateDataCrc,
       "labelFlashStatus": labelFlashStatus,
       "valueFlashStatus": valueFlashStatus,
       "stateFlashStatus": stateFlashStatus,
       "labelBootStatus": labelBootStatus,
       "valueBootStatus": valueBootStatus,
       "stateBootStatus": stateBootStatus,
       "labelAlmLimCrc": labelAlmLimCrc,
       "valueAlmLimCrc": valueAlmLimCrc,
       "stateAlmLimCrc": stateAlmLimCrc,
       "gx2cmAMCTable": gx2cmAMCTable,
       "gx2cmAMCEntry": gx2cmAMCEntry,
       "gx2cmAMCTableIndex": gx2cmAMCTableIndex,
       "valueAMCslot1": valueAMCslot1,
       "serialAMCslot1": serialAMCslot1,
       "agentIDAMCslot1": agentIDAMCslot1,
       "valueAMCslot2": valueAMCslot2,
       "serialAMCslot2": serialAMCslot2,
       "agentIDAMCslot2": agentIDAMCslot2,
       "valueAMCslot3": valueAMCslot3,
       "serialAMCslot3": serialAMCslot3,
       "agentIDAMCslot3": agentIDAMCslot3,
       "valueAMCslot4": valueAMCslot4,
       "serialAMCslot4": serialAMCslot4,
       "agentIDAMCslot4": agentIDAMCslot4,
       "valueAMCslot5": valueAMCslot5,
       "serialAMCslot5": serialAMCslot5,
       "agentIDAMCslot5": agentIDAMCslot5,
       "valueAMCslot6": valueAMCslot6,
       "serialAMCslot6": serialAMCslot6,
       "agentIDAMCslot6": agentIDAMCslot6,
       "valueAMCslot7": valueAMCslot7,
       "serialAMCslot7": serialAMCslot7,
       "agentIDAMCslot7": agentIDAMCslot7,
       "valueAMCslot8": valueAMCslot8,
       "serialAMCslot8": serialAMCslot8,
       "agentIDAMCslot8": agentIDAMCslot8,
       "valueAMCslot9": valueAMCslot9,
       "serialAMCslot9": serialAMCslot9,
       "agentIDAMCslot9": agentIDAMCslot9,
       "valueAMCslot10": valueAMCslot10,
       "serialAMCslot10": serialAMCslot10,
       "agentIDAMCslot10": agentIDAMCslot10,
       "valueAMCslot11": valueAMCslot11,
       "serialAMCslot11": serialAMCslot11,
       "agentIDAMCslot11": agentIDAMCslot11,
       "valueAMCslot12": valueAMCslot12,
       "serialAMCslot12": serialAMCslot12,
       "agentIDAMCslot12": agentIDAMCslot12,
       "valueAMCslot13": valueAMCslot13,
       "serialAMCslot13": serialAMCslot13,
       "agentIDAMCslot13": agentIDAMCslot13,
       "valueAMCslot14": valueAMCslot14,
       "serialAMCslot14": serialAMCslot14,
       "agentIDAMCslot14": agentIDAMCslot14,
       "valueAMCslot15": valueAMCslot15,
       "serialAMCslot15": serialAMCslot15,
       "agentIDAMCslot15": agentIDAMCslot15,
       "valueAMCslot16": valueAMCslot16,
       "serialAMCslot16": serialAMCslot16,
       "agentIDAMCslot16": agentIDAMCslot16,
       "valueAMCslot17": valueAMCslot17,
       "serialAMCslot17": serialAMCslot17,
       "agentIDAMCslot17": agentIDAMCslot17,
       "valueAMCslot18": valueAMCslot18,
       "serialAMCslot18": serialAMCslot18,
       "agentIDAMCslot18": agentIDAMCslot18,
       "autoQuickSwapCnt": autoQuickSwapCnt,
       "gx2cmSecurityTable": gx2cmSecurityTable,
       "gx2cmSecurityEntry": gx2cmSecurityEntry,
       "gx2cmSecurityTableIndex": gx2cmSecurityTableIndex,
       "labelSecurityMode": labelSecurityMode,
       "enumSecurityMode": enumSecurityMode,
       "valueSecurityMode": valueSecurityMode,
       "stateSecurityMode": stateSecurityMode,
       "labelPassword": labelPassword,
       "valuePassword": valuePassword,
       "statePassword": statePassword,
       "labelFactoryChgString": labelFactoryChgString,
       "valueFactoryChgString": valueFactoryChgString,
       "stateFactoryChgString": stateFactoryChgString,
       "labelOperatorChgString": labelOperatorChgString,
       "valueOperatorChgString": valueOperatorChgString,
       "stateOperatorChgString": stateOperatorChgString,
       "labelReadOnlyChgString": labelReadOnlyChgString,
       "valueReadOnlyChgString": valueReadOnlyChgString,
       "stateReadOnlyChgString": stateReadOnlyChgString,
       "labelRemoteOnlyChgString": labelRemoteOnlyChgString,
       "valueRemoteOnlyChgString": valueRemoteOnlyChgString,
       "stateRemoteOnlyChgString": stateRemoteOnlyChgString,
       "labelLocalOnlyChgString": labelLocalOnlyChgString,
       "valueLocalOnlyChgString": valueLocalOnlyChgString,
       "stateLocalOnlyChgString": stateLocalOnlyChgString,
       "gx2cmDiagnosticTable": gx2cmDiagnosticTable,
       "gx2cmDiagnosticEntry": gx2cmDiagnosticEntry,
       "gx2cmDiagnosticTableIndex": gx2cmDiagnosticTableIndex,
       "ledTestValue": ledTestValue,
       "bpTestCnt": bpTestCnt,
       "successTransSlot1": successTransSlot1,
       "successTransSlot2": successTransSlot2,
       "successTransSlot3": successTransSlot3,
       "successTransSlot4": successTransSlot4,
       "successTransSlot5": successTransSlot5,
       "successTransSlot6": successTransSlot6,
       "successTransSlot7": successTransSlot7,
       "successTransSlot8": successTransSlot8,
       "successTransSlot9": successTransSlot9,
       "successTransSlot10": successTransSlot10,
       "successTransSlot11": successTransSlot11,
       "successTransSlot12": successTransSlot12,
       "successTransSlot13": successTransSlot13,
       "successTransSlot14": successTransSlot14,
       "successTransSlot15": successTransSlot15,
       "successTransSlot16": successTransSlot16,
       "successTransSlot17": successTransSlot17,
       "successTransSlot18": successTransSlot18,
       "failureTransSlot1": failureTransSlot1,
       "failureTransSlot2": failureTransSlot2,
       "failureTransSlot3": failureTransSlot3,
       "failureTransSlot4": failureTransSlot4,
       "failureTransSlot5": failureTransSlot5,
       "failureTransSlot6": failureTransSlot6,
       "failureTransSlot7": failureTransSlot7,
       "failureTransSlot8": failureTransSlot8,
       "failureTransSlot9": failureTransSlot9,
       "failureTransSlot10": failureTransSlot10,
       "failureTransSlot11": failureTransSlot11,
       "failureTransSlot12": failureTransSlot12,
       "failureTransSlot13": failureTransSlot13,
       "failureTransSlot14": failureTransSlot14,
       "failureTransSlot15": failureTransSlot15,
       "failureTransSlot16": failureTransSlot16,
       "failureTransSlot17": failureTransSlot17,
       "failureTransSlot18": failureTransSlot18,
       "fanTestMode": fanTestMode,
       "fanControl": fanControl,
       "relayTestMode": relayTestMode,
       "relayControl": relayControl,
       "slotPollMode": slotPollMode,
       "bootCount": bootCount,
       "objectTableData": objectTableData,
       "setSysTime": setSysTime,
       "gx2cmDownloadTable": gx2cmDownloadTable,
       "gx2cmDownloadEntry": gx2cmDownloadEntry,
       "gx2cmDownloadTableIndex": gx2cmDownloadTableIndex,
       "downloadValue": downloadValue,
       "autoDownloadReset": autoDownloadReset,
       "downloadFilename": downloadFilename,
       "downloadState": downloadState,
       "switchFwBank": switchFwBank,
       "cmTrapHistoryTable": cmTrapHistoryTable,
       "cmTrapHistoryEntry": cmTrapHistoryEntry,
       "cmTrapHistoryTableIndex": cmTrapHistoryTableIndex,
       "netrapId": netrapId,
       "netrapNetworkElemModelNumber": netrapNetworkElemModelNumber,
       "netrapNetworkElemSerialNum": netrapNetworkElemSerialNum,
       "netrapPerceivedSeverity": netrapPerceivedSeverity,
       "netrapNetworkElemOperState": netrapNetworkElemOperState,
       "netrapNetworkElemAlarmStatus": netrapNetworkElemAlarmStatus,
       "netrapNetworkElemAdminState": netrapNetworkElemAdminState,
       "netrapNetworkElemAvailStatus": netrapNetworkElemAvailStatus,
       "netrapText": netrapText,
       "netrapLastTrapTimeStamp": netrapLastTrapTimeStamp,
       "netrapChangedObjectId": netrapChangedObjectId,
       "netrapAdditionalInfoInteger1": netrapAdditionalInfoInteger1,
       "netrapAdditionalInfoInteger2": netrapAdditionalInfoInteger2,
       "netrapAdditionalInfoInteger3": netrapAdditionalInfoInteger3,
       "netrapChangedValueDisplayString": netrapChangedValueDisplayString,
       "netrapChangedValueOID": netrapChangedValueOID,
       "netrapChangedValueIpAddress": netrapChangedValueIpAddress,
       "netrapChangedValueInteger": netrapChangedValueInteger}
)
