# SNMP MIB module (CT-HSIMPHYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CT-HSIMPHYS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:01 2024
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

(ctHSIMPhysMib,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctHSIMPhysMib")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HsimInfo_ObjectIdentity = ObjectIdentity
hsimInfo = _HsimInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1)
)
_HsimBoardRev_Type = DisplayString
_HsimBoardRev_Object = MibScalar
hsimBoardRev = _HsimBoardRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 1),
    _HsimBoardRev_Type()
)
hsimBoardRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsimBoardRev.setStatus("mandatory")
_HsimBoardId_Type = DisplayString
_HsimBoardId_Object = MibScalar
hsimBoardId = _HsimBoardId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 2),
    _HsimBoardId_Type()
)
hsimBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsimBoardId.setStatus("mandatory")
_HsimEpldRev_Type = DisplayString
_HsimEpldRev_Object = MibScalar
hsimEpldRev = _HsimEpldRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 3),
    _HsimEpldRev_Type()
)
hsimEpldRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsimEpldRev.setStatus("mandatory")
_HsimEpldId_Type = DisplayString
_HsimEpldId_Object = MibScalar
hsimEpldId = _HsimEpldId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 4),
    _HsimEpldId_Type()
)
hsimEpldId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsimEpldId.setStatus("mandatory")
_HsimFsbRev_Type = DisplayString
_HsimFsbRev_Object = MibScalar
hsimFsbRev = _HsimFsbRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 5),
    _HsimFsbRev_Type()
)
hsimFsbRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsimFsbRev.setStatus("mandatory")
_HsimSsbRev_Type = DisplayString
_HsimSsbRev_Object = MibScalar
hsimSsbRev = _HsimSsbRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 6),
    _HsimSsbRev_Type()
)
hsimSsbRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsimSsbRev.setStatus("mandatory")
_HsimFwRev_Type = DisplayString
_HsimFwRev_Object = MibScalar
hsimFwRev = _HsimFwRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 7),
    _HsimFwRev_Type()
)
hsimFwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsimFwRev.setStatus("mandatory")
_HsimPeripheralMBusInfo_ObjectIdentity = ObjectIdentity
hsimPeripheralMBusInfo = _HsimPeripheralMBusInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 8)
)
_MBusNumberBoardsInstalled_Type = Integer32
_MBusNumberBoardsInstalled_Object = MibScalar
mBusNumberBoardsInstalled = _MBusNumberBoardsInstalled_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 8, 1),
    _MBusNumberBoardsInstalled_Type()
)
mBusNumberBoardsInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBusNumberBoardsInstalled.setStatus("mandatory")
_MBusBoardTable_Object = MibTable
mBusBoardTable = _MBusBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 8, 2)
)
if mibBuilder.loadTexts:
    mBusBoardTable.setStatus("mandatory")
_MBusBoardEntry_Object = MibTableRow
mBusBoardEntry = _MBusBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 8, 2, 1)
)
mBusBoardEntry.setIndexNames(
    (0, "CT-HSIMPHYS-MIB", "mBusBoardID"),
)
if mibBuilder.loadTexts:
    mBusBoardEntry.setStatus("mandatory")
_MBusBoardID_Type = Integer32
_MBusBoardID_Object = MibTableColumn
mBusBoardID = _MBusBoardID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 8, 2, 1, 1),
    _MBusBoardID_Type()
)
mBusBoardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBusBoardID.setStatus("mandatory")


class _MBusBoardEntryType_Type(Integer32):
    """Custom type mBusBoardEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cmm", 2),
          ("unknown", 1))
    )


_MBusBoardEntryType_Type.__name__ = "Integer32"
_MBusBoardEntryType_Object = MibTableColumn
mBusBoardEntryType = _MBusBoardEntryType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 8, 2, 1, 2),
    _MBusBoardEntryType_Type()
)
mBusBoardEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBusBoardEntryType.setStatus("mandatory")
_MBusBoardOIDPointer_Type = ObjectIdentifier
_MBusBoardOIDPointer_Object = MibTableColumn
mBusBoardOIDPointer = _MBusBoardOIDPointer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 8, 2, 1, 3),
    _MBusBoardOIDPointer_Type()
)
mBusBoardOIDPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBusBoardOIDPointer.setStatus("mandatory")
_HsimPeripheralWpimInfo_ObjectIdentity = ObjectIdentity
hsimPeripheralWpimInfo = _HsimPeripheralWpimInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 9)
)
_WpimNumberBoardsInstalled_Type = Integer32
_WpimNumberBoardsInstalled_Object = MibScalar
wpimNumberBoardsInstalled = _WpimNumberBoardsInstalled_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 9, 1),
    _WpimNumberBoardsInstalled_Type()
)
wpimNumberBoardsInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpimNumberBoardsInstalled.setStatus("mandatory")
_WpimBoardTable_Object = MibTable
wpimBoardTable = _WpimBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 9, 2)
)
if mibBuilder.loadTexts:
    wpimBoardTable.setStatus("mandatory")
_WpimBoardEntry_Object = MibTableRow
wpimBoardEntry = _WpimBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 9, 2, 1)
)
wpimBoardEntry.setIndexNames(
    (0, "CT-HSIMPHYS-MIB", "wpimBoardID"),
)
if mibBuilder.loadTexts:
    wpimBoardEntry.setStatus("mandatory")
_WpimBoardID_Type = Integer32
_WpimBoardID_Object = MibTableColumn
wpimBoardID = _WpimBoardID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 9, 2, 1, 1),
    _WpimBoardID_Type()
)
wpimBoardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpimBoardID.setStatus("mandatory")
_WpimBoardEntryType_Type = ObjectIdentifier
_WpimBoardEntryType_Object = MibTableColumn
wpimBoardEntryType = _WpimBoardEntryType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 9, 2, 1, 2),
    _WpimBoardEntryType_Type()
)
wpimBoardEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpimBoardEntryType.setStatus("mandatory")
_WpimBoardOIDPointer_Type = ObjectIdentifier
_WpimBoardOIDPointer_Object = MibTableColumn
wpimBoardOIDPointer = _WpimBoardOIDPointer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 9, 2, 1, 3),
    _WpimBoardOIDPointer_Type()
)
wpimBoardOIDPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpimBoardOIDPointer.setStatus("mandatory")
_HsimLocalHwDevicesInfo_ObjectIdentity = ObjectIdentity
hsimLocalHwDevicesInfo = _HsimLocalHwDevicesInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 10)
)
_LocalHwDevicesTable_Object = MibTable
localHwDevicesTable = _LocalHwDevicesTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 10, 1)
)
if mibBuilder.loadTexts:
    localHwDevicesTable.setStatus("mandatory")
_LocalHwDevicesEntry_Object = MibTableRow
localHwDevicesEntry = _LocalHwDevicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 10, 1, 1)
)
localHwDevicesEntry.setIndexNames(
    (0, "CT-HSIMPHYS-MIB", "localHwDeviceID"),
)
if mibBuilder.loadTexts:
    localHwDevicesEntry.setStatus("mandatory")
_LocalHwDeviceID_Type = Integer32
_LocalHwDeviceID_Object = MibTableColumn
localHwDeviceID = _LocalHwDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 10, 1, 1, 1),
    _LocalHwDeviceID_Type()
)
localHwDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localHwDeviceID.setStatus("mandatory")


class _LocalHwDeviceType_Type(Integer32):
    """Custom type localHwDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mitelMT8985", 3),
          ("siemensMunich32", 2),
          ("unknown", 1))
    )


_LocalHwDeviceType_Type.__name__ = "Integer32"
_LocalHwDeviceType_Object = MibTableColumn
localHwDeviceType = _LocalHwDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 10, 1, 1, 2),
    _LocalHwDeviceType_Type()
)
localHwDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localHwDeviceType.setStatus("mandatory")


class _LocalHwDeviceOperStatus_Type(Integer32):
    """Custom type localHwDeviceOperStatus based on Integer32"""
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
        *(("dormant", 5),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_LocalHwDeviceOperStatus_Type.__name__ = "Integer32"
_LocalHwDeviceOperStatus_Object = MibTableColumn
localHwDeviceOperStatus = _LocalHwDeviceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 10, 1, 1, 3),
    _LocalHwDeviceOperStatus_Type()
)
localHwDeviceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localHwDeviceOperStatus.setStatus("mandatory")


class _LocalHwDeviceAdminStatus_Type(Integer32):
    """Custom type localHwDeviceAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LocalHwDeviceAdminStatus_Type.__name__ = "Integer32"
_LocalHwDeviceAdminStatus_Object = MibTableColumn
localHwDeviceAdminStatus = _LocalHwDeviceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 10, 1, 1, 4),
    _LocalHwDeviceAdminStatus_Type()
)
localHwDeviceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localHwDeviceAdminStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CT-HSIMPHYS-MIB",
    **{"hsimInfo": hsimInfo,
       "hsimBoardRev": hsimBoardRev,
       "hsimBoardId": hsimBoardId,
       "hsimEpldRev": hsimEpldRev,
       "hsimEpldId": hsimEpldId,
       "hsimFsbRev": hsimFsbRev,
       "hsimSsbRev": hsimSsbRev,
       "hsimFwRev": hsimFwRev,
       "hsimPeripheralMBusInfo": hsimPeripheralMBusInfo,
       "mBusNumberBoardsInstalled": mBusNumberBoardsInstalled,
       "mBusBoardTable": mBusBoardTable,
       "mBusBoardEntry": mBusBoardEntry,
       "mBusBoardID": mBusBoardID,
       "mBusBoardEntryType": mBusBoardEntryType,
       "mBusBoardOIDPointer": mBusBoardOIDPointer,
       "hsimPeripheralWpimInfo": hsimPeripheralWpimInfo,
       "wpimNumberBoardsInstalled": wpimNumberBoardsInstalled,
       "wpimBoardTable": wpimBoardTable,
       "wpimBoardEntry": wpimBoardEntry,
       "wpimBoardID": wpimBoardID,
       "wpimBoardEntryType": wpimBoardEntryType,
       "wpimBoardOIDPointer": wpimBoardOIDPointer,
       "hsimLocalHwDevicesInfo": hsimLocalHwDevicesInfo,
       "localHwDevicesTable": localHwDevicesTable,
       "localHwDevicesEntry": localHwDevicesEntry,
       "localHwDeviceID": localHwDeviceID,
       "localHwDeviceType": localHwDeviceType,
       "localHwDeviceOperStatus": localHwDeviceOperStatus,
       "localHwDeviceAdminStatus": localHwDeviceAdminStatus}
)
