# SNMP MIB module (SEI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SEI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:50:17 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class MemAddress(OctetString):
    """Custom type MemAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )





class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sei_ObjectIdentity = ObjectIdentity
sei = _Sei_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 175)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 175, 1)
)
_Suminet_ObjectIdentity = ObjectIdentity
suminet = _Suminet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 175, 1, 1)
)
_Sn3500_ObjectIdentity = ObjectIdentity
sn3500 = _Sn3500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 175, 1, 1, 1)
)
_S35Products_ObjectIdentity = ObjectIdentity
s35Products = _S35Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 1)
)
_S35Model00_ObjectIdentity = ObjectIdentity
s35Model00 = _S35Model00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 1, 1)
)
_S35System_ObjectIdentity = ObjectIdentity
s35System = _S35System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2)
)
_S35Box_ObjectIdentity = ObjectIdentity
s35Box = _S35Box_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 1)
)
_S35BoxFor00_ObjectIdentity = ObjectIdentity
s35BoxFor00 = _S35BoxFor00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 1, 1)
)


class _S35BoxFor00PowerState_Type(Integer32):
    """Custom type s35BoxFor00PowerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_S35BoxFor00PowerState_Type.__name__ = "Integer32"
_S35BoxFor00PowerState_Object = MibScalar
s35BoxFor00PowerState = _S35BoxFor00PowerState_Object(
    (1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 1, 1, 1),
    _S35BoxFor00PowerState_Type()
)
s35BoxFor00PowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s35BoxFor00PowerState.setStatus("mandatory")


class _S35BoxFor00FanState_Type(Integer32):
    """Custom type s35BoxFor00FanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stopping", 2),
          ("working", 1))
    )


_S35BoxFor00FanState_Type.__name__ = "Integer32"
_S35BoxFor00FanState_Object = MibScalar
s35BoxFor00FanState = _S35BoxFor00FanState_Object(
    (1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 1, 1, 2),
    _S35BoxFor00FanState_Type()
)
s35BoxFor00FanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s35BoxFor00FanState.setStatus("mandatory")


class _S35BoxFor00StationID_Type(Integer32):
    """Custom type s35BoxFor00StationID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 511),
    )


_S35BoxFor00StationID_Type.__name__ = "Integer32"
_S35BoxFor00StationID_Object = MibScalar
s35BoxFor00StationID = _S35BoxFor00StationID_Object(
    (1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 1, 1, 3),
    _S35BoxFor00StationID_Type()
)
s35BoxFor00StationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s35BoxFor00StationID.setStatus("mandatory")


class _S35BoxFor00LedState_Type(Integer32):
    """Custom type s35BoxFor00LedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S35BoxFor00LedState_Type.__name__ = "Integer32"
_S35BoxFor00LedState_Object = MibScalar
s35BoxFor00LedState = _S35BoxFor00LedState_Object(
    (1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 1, 1, 4),
    _S35BoxFor00LedState_Type()
)
s35BoxFor00LedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s35BoxFor00LedState.setStatus("mandatory")
_S35Board_ObjectIdentity = ObjectIdentity
s35Board = _S35Board_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 2)
)
_S35BoardNumber_Type = Integer32
_S35BoardNumber_Object = MibScalar
s35BoardNumber = _S35BoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 2, 1),
    _S35BoardNumber_Type()
)
s35BoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s35BoardNumber.setStatus("mandatory")
_S35BoardTable_Object = MibTable
s35BoardTable = _S35BoardTable_Object(
    (1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    s35BoardTable.setStatus("mandatory")
_S35BoardEntry_Object = MibTableRow
s35BoardEntry = _S35BoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 2, 2, 1)
)
s35BoardEntry.setIndexNames(
    (0, "SEI-MIB", "s35BoardIndex"),
)
if mibBuilder.loadTexts:
    s35BoardEntry.setStatus("mandatory")
_S35BoardIndex_Type = Integer32
_S35BoardIndex_Object = MibTableColumn
s35BoardIndex = _S35BoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 2, 2, 1, 1),
    _S35BoardIndex_Type()
)
s35BoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s35BoardIndex.setStatus("mandatory")


class _S35BoardType_Type(Integer32):
    """Custom type s35BoardType based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("accelerator", 12),
          ("ethernet-30p-1M", 4),
          ("ethernet-noparity", 5),
          ("ethernet-parity", 6),
          ("fddi-00-1M", 2),
          ("fddi-00-512K", 1),
          ("fddi-30-1M", 3),
          ("fddi-LBR-30", 14),
          ("hsds", 10),
          ("memory-30p-12M", 13),
          ("sn3200-vab", 11),
          ("tokenring-16M", 8),
          ("tokenring-4M", 7),
          ("v35", 9))
    )


_S35BoardType_Type.__name__ = "Integer32"
_S35BoardType_Object = MibTableColumn
s35BoardType = _S35BoardType_Object(
    (1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 2, 2, 1, 2),
    _S35BoardType_Type()
)
s35BoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s35BoardType.setStatus("mandatory")


class _S35BoardCpuType_Type(Integer32):
    """Custom type s35BoardCpuType based on Integer32"""
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
        *(("am29200", 6),
          ("mc68000", 2),
          ("mc68010", 5),
          ("mc68030", 3),
          ("mc68302", 4),
          ("nothing", 1))
    )


_S35BoardCpuType_Type.__name__ = "Integer32"
_S35BoardCpuType_Object = MibTableColumn
s35BoardCpuType = _S35BoardCpuType_Object(
    (1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 2, 2, 1, 3),
    _S35BoardCpuType_Type()
)
s35BoardCpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s35BoardCpuType.setStatus("mandatory")


class _S35BoardHardwareRevision_Type(DisplayString):
    """Custom type s35BoardHardwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_S35BoardHardwareRevision_Type.__name__ = "DisplayString"
_S35BoardHardwareRevision_Object = MibTableColumn
s35BoardHardwareRevision = _S35BoardHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 2, 2, 1, 4),
    _S35BoardHardwareRevision_Type()
)
s35BoardHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s35BoardHardwareRevision.setStatus("optional")


class _S35BoardLedState_Type(Integer32):
    """Custom type s35BoardLedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_S35BoardLedState_Type.__name__ = "Integer32"
_S35BoardLedState_Object = MibTableColumn
s35BoardLedState = _S35BoardLedState_Object(
    (1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 2, 2, 1, 5),
    _S35BoardLedState_Type()
)
s35BoardLedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s35BoardLedState.setStatus("mandatory")


class _S35BoardDipInformation_Type(Integer32):
    """Custom type s35BoardDipInformation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S35BoardDipInformation_Type.__name__ = "Integer32"
_S35BoardDipInformation_Object = MibTableColumn
s35BoardDipInformation = _S35BoardDipInformation_Object(
    (1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 2, 2, 1, 6),
    _S35BoardDipInformation_Type()
)
s35BoardDipInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s35BoardDipInformation.setStatus("mandatory")


class _S35BoardRomRevision_Type(DisplayString):
    """Custom type s35BoardRomRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_S35BoardRomRevision_Type.__name__ = "DisplayString"
_S35BoardRomRevision_Object = MibTableColumn
s35BoardRomRevision = _S35BoardRomRevision_Object(
    (1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 2, 2, 1, 7),
    _S35BoardRomRevision_Type()
)
s35BoardRomRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s35BoardRomRevision.setStatus("optional")
_S35BoardSerialNumber_Type = Integer32
_S35BoardSerialNumber_Object = MibTableColumn
s35BoardSerialNumber = _S35BoardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 2, 2, 1, 8),
    _S35BoardSerialNumber_Type()
)
s35BoardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s35BoardSerialNumber.setStatus("optional")
_S35BoardIf_ObjectIdentity = ObjectIdentity
s35BoardIf = _S35BoardIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 4)
)
_S35BoardIfNumber_Type = Integer32
_S35BoardIfNumber_Object = MibScalar
s35BoardIfNumber = _S35BoardIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 4, 1),
    _S35BoardIfNumber_Type()
)
s35BoardIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s35BoardIfNumber.setStatus("mandatory")
_S35BoardIfTable_Object = MibTable
s35BoardIfTable = _S35BoardIfTable_Object(
    (1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    s35BoardIfTable.setStatus("mandatory")
_S35BoardIfEntry_Object = MibTableRow
s35BoardIfEntry = _S35BoardIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 4, 2, 1)
)
s35BoardIfEntry.setIndexNames(
    (0, "SEI-MIB", "s35BoardIfBoardIndex"),
    (0, "SEI-MIB", "s35BoardIfIndex"),
)
if mibBuilder.loadTexts:
    s35BoardIfEntry.setStatus("mandatory")
_S35BoardIfBoardIndex_Type = Integer32
_S35BoardIfBoardIndex_Object = MibTableColumn
s35BoardIfBoardIndex = _S35BoardIfBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 4, 2, 1, 1),
    _S35BoardIfBoardIndex_Type()
)
s35BoardIfBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s35BoardIfBoardIndex.setStatus("mandatory")
_S35BoardIfIndex_Type = Integer32
_S35BoardIfIndex_Object = MibTableColumn
s35BoardIfIndex = _S35BoardIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 4, 2, 1, 2),
    _S35BoardIfIndex_Type()
)
s35BoardIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s35BoardIfIndex.setStatus("mandatory")


class _S35BoardIfInitialized_Type(Integer32):
    """Custom type s35BoardIfInitialized based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initialized", 1),
          ("uninitialized", 2))
    )


_S35BoardIfInitialized_Type.__name__ = "Integer32"
_S35BoardIfInitialized_Object = MibTableColumn
s35BoardIfInitialized = _S35BoardIfInitialized_Object(
    (1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 4, 2, 1, 3),
    _S35BoardIfInitialized_Type()
)
s35BoardIfInitialized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s35BoardIfInitialized.setStatus("mandatory")
_Sumistation_ObjectIdentity = ObjectIdentity
sumistation = _Sumistation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 175, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SEI-MIB",
    **{"MemAddress": MemAddress,
       "MacAddress": MacAddress,
       "sei": sei,
       "products": products,
       "suminet": suminet,
       "sn3500": sn3500,
       "s35Products": s35Products,
       "s35Model00": s35Model00,
       "s35System": s35System,
       "s35Box": s35Box,
       "s35BoxFor00": s35BoxFor00,
       "s35BoxFor00PowerState": s35BoxFor00PowerState,
       "s35BoxFor00FanState": s35BoxFor00FanState,
       "s35BoxFor00StationID": s35BoxFor00StationID,
       "s35BoxFor00LedState": s35BoxFor00LedState,
       "s35Board": s35Board,
       "s35BoardNumber": s35BoardNumber,
       "s35BoardTable": s35BoardTable,
       "s35BoardEntry": s35BoardEntry,
       "s35BoardIndex": s35BoardIndex,
       "s35BoardType": s35BoardType,
       "s35BoardCpuType": s35BoardCpuType,
       "s35BoardHardwareRevision": s35BoardHardwareRevision,
       "s35BoardLedState": s35BoardLedState,
       "s35BoardDipInformation": s35BoardDipInformation,
       "s35BoardRomRevision": s35BoardRomRevision,
       "s35BoardSerialNumber": s35BoardSerialNumber,
       "s35BoardIf": s35BoardIf,
       "s35BoardIfNumber": s35BoardIfNumber,
       "s35BoardIfTable": s35BoardIfTable,
       "s35BoardIfEntry": s35BoardIfEntry,
       "s35BoardIfBoardIndex": s35BoardIfBoardIndex,
       "s35BoardIfIndex": s35BoardIfIndex,
       "s35BoardIfInitialized": s35BoardIfInitialized,
       "sumistation": sumistation}
)
