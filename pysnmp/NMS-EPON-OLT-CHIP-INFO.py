# SNMP MIB module (NMS-EPON-OLT-CHIP-INFO) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-EPON-OLT-CHIP-INFO
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:42 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(nmsEPONGroup,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmsEPONGroup")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NmsEponOltChipInfo_ObjectIdentity = ObjectIdentity
nmsEponOltChipInfo = _NmsEponOltChipInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 2)
)
_NmseponoltchipTable_Object = MibTable
nmseponoltchipTable = _NmseponoltchipTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 2, 1)
)
if mibBuilder.loadTexts:
    nmseponoltchipTable.setStatus("mandatory")
_NmsEponOltChipEntry_Object = MibTableRow
nmsEponOltChipEntry = _NmsEponOltChipEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 2, 1, 1)
)
nmsEponOltChipEntry.setIndexNames(
    (0, "NMS-EPON-OLT-CHIP-INFO", "oltChipIndex"),
)
if mibBuilder.loadTexts:
    nmsEponOltChipEntry.setStatus("mandatory")
_OltChipIndex_Type = Integer32
_OltChipIndex_Object = MibTableColumn
oltChipIndex = _OltChipIndex_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 2, 1, 1, 1),
    _OltChipIndex_Type()
)
oltChipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltChipIndex.setStatus("mandatory")
_OltChipSlotID_Type = Integer32
_OltChipSlotID_Object = MibTableColumn
oltChipSlotID = _OltChipSlotID_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 2, 1, 1, 2),
    _OltChipSlotID_Type()
)
oltChipSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltChipSlotID.setStatus("mandatory")
_OltChipModuleID_Type = Integer32
_OltChipModuleID_Object = MibTableColumn
oltChipModuleID = _OltChipModuleID_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 2, 1, 1, 3),
    _OltChipModuleID_Type()
)
oltChipModuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltChipModuleID.setStatus("mandatory")
_OltChipDeviceID_Type = Integer32
_OltChipDeviceID_Object = MibTableColumn
oltChipDeviceID = _OltChipDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 2, 1, 1, 4),
    _OltChipDeviceID_Type()
)
oltChipDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltChipDeviceID.setStatus("mandatory")
_OltChipMACAddress_Type = PhysAddress
_OltChipMACAddress_Object = MibTableColumn
oltChipMACAddress = _OltChipMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 2, 1, 1, 5),
    _OltChipMACAddress_Type()
)
oltChipMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltChipMACAddress.setStatus("mandatory")


class _OltChipStatus_Type(Integer32):
    """Custom type oltChipStatus based on Integer32"""
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
        *(("downloading_image", 5),
          ("operational", 2),
          ("shut_down", 3),
          ("timed_out", 4),
          ("wait_config", 1))
    )


_OltChipStatus_Type.__name__ = "Integer32"
_OltChipStatus_Object = MibTableColumn
oltChipStatus = _OltChipStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 2, 1, 1, 6),
    _OltChipStatus_Type()
)
oltChipStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltChipStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-EPON-OLT-CHIP-INFO",
    **{"nmsEponOltChipInfo": nmsEponOltChipInfo,
       "nmseponoltchipTable": nmseponoltchipTable,
       "nmsEponOltChipEntry": nmsEponOltChipEntry,
       "oltChipIndex": oltChipIndex,
       "oltChipSlotID": oltChipSlotID,
       "oltChipModuleID": oltChipModuleID,
       "oltChipDeviceID": oltChipDeviceID,
       "oltChipMACAddress": oltChipMACAddress,
       "oltChipStatus": oltChipStatus}
)
