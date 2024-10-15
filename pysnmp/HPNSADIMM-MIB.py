# SNMP MIB module (HPNSADIMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPNSADIMM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:18 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Hpnsa_ObjectIdentity = ObjectIdentity
hpnsa = _Hpnsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23)
)
_HpnsaDIMM_ObjectIdentity = ObjectIdentity
hpnsaDIMM = _HpnsaDIMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 21)
)
_HpnsaDIMMMibRev_ObjectIdentity = ObjectIdentity
hpnsaDIMMMibRev = _HpnsaDIMMMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 21, 1)
)


class _HpnsaDIMMMibRevMajor_Type(Integer32):
    """Custom type hpnsaDIMMMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnsaDIMMMibRevMajor_Type.__name__ = "Integer32"
_HpnsaDIMMMibRevMajor_Object = MibScalar
hpnsaDIMMMibRevMajor = _HpnsaDIMMMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 21, 1, 1),
    _HpnsaDIMMMibRevMajor_Type()
)
hpnsaDIMMMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaDIMMMibRevMajor.setStatus("mandatory")


class _HpnsaDIMMMibRevMinor_Type(Integer32):
    """Custom type hpnsaDIMMMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaDIMMMibRevMinor_Type.__name__ = "Integer32"
_HpnsaDIMMMibRevMinor_Object = MibScalar
hpnsaDIMMMibRevMinor = _HpnsaDIMMMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 21, 1, 2),
    _HpnsaDIMMMibRevMinor_Type()
)
hpnsaDIMMMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaDIMMMibRevMinor.setStatus("mandatory")
_HpnsaDIMMAgent_ObjectIdentity = ObjectIdentity
hpnsaDIMMAgent = _HpnsaDIMMAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 21, 2)
)
_HpnsaDIMMAgentTable_Object = MibTable
hpnsaDIMMAgentTable = _HpnsaDIMMAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 21, 2, 1)
)
if mibBuilder.loadTexts:
    hpnsaDIMMAgentTable.setStatus("mandatory")
_HpnsaDIMMAgentEntry_Object = MibTableRow
hpnsaDIMMAgentEntry = _HpnsaDIMMAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 21, 2, 1, 1)
)
hpnsaDIMMAgentEntry.setIndexNames(
    (0, "HPNSADIMM-MIB", "hpnsaDIMMAgentIndex"),
)
if mibBuilder.loadTexts:
    hpnsaDIMMAgentEntry.setStatus("mandatory")


class _HpnsaDIMMAgentIndex_Type(Integer32):
    """Custom type hpnsaDIMMAgentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaDIMMAgentIndex_Type.__name__ = "Integer32"
_HpnsaDIMMAgentIndex_Object = MibTableColumn
hpnsaDIMMAgentIndex = _HpnsaDIMMAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 21, 2, 1, 1, 1),
    _HpnsaDIMMAgentIndex_Type()
)
hpnsaDIMMAgentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaDIMMAgentIndex.setStatus("mandatory")


class _HpnsaDIMMAgentName_Type(DisplayString):
    """Custom type hpnsaDIMMAgentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaDIMMAgentName_Type.__name__ = "DisplayString"
_HpnsaDIMMAgentName_Object = MibTableColumn
hpnsaDIMMAgentName = _HpnsaDIMMAgentName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 21, 2, 1, 1, 2),
    _HpnsaDIMMAgentName_Type()
)
hpnsaDIMMAgentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaDIMMAgentName.setStatus("mandatory")


class _HpnsaDIMMAgentVersion_Type(DisplayString):
    """Custom type hpnsaDIMMAgentVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HpnsaDIMMAgentVersion_Type.__name__ = "DisplayString"
_HpnsaDIMMAgentVersion_Object = MibTableColumn
hpnsaDIMMAgentVersion = _HpnsaDIMMAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 21, 2, 1, 1, 3),
    _HpnsaDIMMAgentVersion_Type()
)
hpnsaDIMMAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaDIMMAgentVersion.setStatus("mandatory")


class _HpnsaDIMMAgentDate_Type(OctetString):
    """Custom type hpnsaDIMMAgentDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_HpnsaDIMMAgentDate_Type.__name__ = "OctetString"
_HpnsaDIMMAgentDate_Object = MibTableColumn
hpnsaDIMMAgentDate = _HpnsaDIMMAgentDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 21, 2, 1, 1, 4),
    _HpnsaDIMMAgentDate_Type()
)
hpnsaDIMMAgentDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaDIMMAgentDate.setStatus("mandatory")
_HpnsaDIMMInfo_ObjectIdentity = ObjectIdentity
hpnsaDIMMInfo = _HpnsaDIMMInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 21, 3)
)
_HpnsaDIMMTable_Object = MibTable
hpnsaDIMMTable = _HpnsaDIMMTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 21, 3, 1)
)
if mibBuilder.loadTexts:
    hpnsaDIMMTable.setStatus("mandatory")
_HpnsaDIMMEntry_Object = MibTableRow
hpnsaDIMMEntry = _HpnsaDIMMEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 21, 3, 1, 1)
)
hpnsaDIMMEntry.setIndexNames(
    (0, "HPNSADIMM-MIB", "hpnsaDIMMSlotIndex"),
)
if mibBuilder.loadTexts:
    hpnsaDIMMEntry.setStatus("mandatory")


class _HpnsaDIMMSlotIndex_Type(Integer32):
    """Custom type hpnsaDIMMSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaDIMMSlotIndex_Type.__name__ = "Integer32"
_HpnsaDIMMSlotIndex_Object = MibTableColumn
hpnsaDIMMSlotIndex = _HpnsaDIMMSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 21, 3, 1, 1, 1),
    _HpnsaDIMMSlotIndex_Type()
)
hpnsaDIMMSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaDIMMSlotIndex.setStatus("mandatory")
_HpnsaDIMMSize_Type = Integer32
_HpnsaDIMMSize_Object = MibTableColumn
hpnsaDIMMSize = _HpnsaDIMMSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 21, 3, 1, 1, 2),
    _HpnsaDIMMSize_Type()
)
hpnsaDIMMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaDIMMSize.setStatus("mandatory")


class _HpnsaDIMMType_Type(Integer32):
    """Custom type hpnsaDIMMType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dimm-ECC", 2),
          ("dimm-NONE", 0),
          ("dimm-Parity", 1))
    )


_HpnsaDIMMType_Type.__name__ = "Integer32"
_HpnsaDIMMType_Object = MibTableColumn
hpnsaDIMMType = _HpnsaDIMMType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 21, 3, 1, 1, 3),
    _HpnsaDIMMType_Type()
)
hpnsaDIMMType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaDIMMType.setStatus("mandatory")
_HpnsaDIMMSpeed_Type = Integer32
_HpnsaDIMMSpeed_Object = MibTableColumn
hpnsaDIMMSpeed = _HpnsaDIMMSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 21, 3, 1, 1, 4),
    _HpnsaDIMMSpeed_Type()
)
hpnsaDIMMSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaDIMMSpeed.setStatus("mandatory")


class _HpnsaDIMMManufacturer_Type(DisplayString):
    """Custom type hpnsaDIMMManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaDIMMManufacturer_Type.__name__ = "DisplayString"
_HpnsaDIMMManufacturer_Object = MibTableColumn
hpnsaDIMMManufacturer = _HpnsaDIMMManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 21, 3, 1, 1, 5),
    _HpnsaDIMMManufacturer_Type()
)
hpnsaDIMMManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaDIMMManufacturer.setStatus("mandatory")


class _HpnsaDIMMManufacturerPartNumber_Type(DisplayString):
    """Custom type hpnsaDIMMManufacturerPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaDIMMManufacturerPartNumber_Type.__name__ = "DisplayString"
_HpnsaDIMMManufacturerPartNumber_Object = MibTableColumn
hpnsaDIMMManufacturerPartNumber = _HpnsaDIMMManufacturerPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 21, 3, 1, 1, 6),
    _HpnsaDIMMManufacturerPartNumber_Type()
)
hpnsaDIMMManufacturerPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaDIMMManufacturerPartNumber.setStatus("mandatory")


class _HpnsaDIMMManufactureDateCode_Type(OctetString):
    """Custom type hpnsaDIMMManufactureDateCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_HpnsaDIMMManufactureDateCode_Type.__name__ = "OctetString"
_HpnsaDIMMManufactureDateCode_Object = MibScalar
hpnsaDIMMManufactureDateCode = _HpnsaDIMMManufactureDateCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 21, 3, 1, 1, 7),
    _HpnsaDIMMManufactureDateCode_Type()
)
hpnsaDIMMManufactureDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaDIMMManufactureDateCode.setStatus("mandatory")


class _HpnsaDIMMDramType_Type(Integer32):
    """Custom type hpnsaDIMMDramType based on Integer32"""
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
        *(("dimm-ExtendedDataOut", 2),
          ("dimm-FastPageMode", 1),
          ("dimm-PipelinedNibble", 3),
          ("dimm-Synchronous", 4))
    )


_HpnsaDIMMDramType_Type.__name__ = "Integer32"
_HpnsaDIMMDramType_Object = MibTableColumn
hpnsaDIMMDramType = _HpnsaDIMMDramType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 21, 3, 1, 1, 8),
    _HpnsaDIMMDramType_Type()
)
hpnsaDIMMDramType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaDIMMDramType.setStatus("mandatory")
_HpnsaDIMMHPLocalEntry_Object = MibTableRow
hpnsaDIMMHPLocalEntry = _HpnsaDIMMHPLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 21, 3, 1, 2)
)
hpnsaDIMMHPLocalEntry.setIndexNames(
    (0, "HPNSADIMM-MIB", "hpnsaDIMMHPSlotIndex"),
)
if mibBuilder.loadTexts:
    hpnsaDIMMHPLocalEntry.setStatus("mandatory")


class _HpnsaDIMMHPSlotIndex_Type(Integer32):
    """Custom type hpnsaDIMMHPSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaDIMMHPSlotIndex_Type.__name__ = "Integer32"
_HpnsaDIMMHPSlotIndex_Object = MibTableColumn
hpnsaDIMMHPSlotIndex = _HpnsaDIMMHPSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 21, 3, 1, 2, 1),
    _HpnsaDIMMHPSlotIndex_Type()
)
hpnsaDIMMHPSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaDIMMHPSlotIndex.setStatus("mandatory")


class _HpnsaDIMMHPProductNumber_Type(DisplayString):
    """Custom type hpnsaDIMMHPProductNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_HpnsaDIMMHPProductNumber_Type.__name__ = "DisplayString"
_HpnsaDIMMHPProductNumber_Object = MibTableColumn
hpnsaDIMMHPProductNumber = _HpnsaDIMMHPProductNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 21, 3, 1, 2, 2),
    _HpnsaDIMMHPProductNumber_Type()
)
hpnsaDIMMHPProductNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaDIMMHPProductNumber.setStatus("mandatory")
_HpnsaDIMMSerialNumber_Type = Integer32
_HpnsaDIMMSerialNumber_Object = MibScalar
hpnsaDIMMSerialNumber = _HpnsaDIMMSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 21, 3, 1, 2, 3),
    _HpnsaDIMMSerialNumber_Type()
)
hpnsaDIMMSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaDIMMSerialNumber.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPNSADIMM-MIB",
    **{"hp": hp,
       "nm": nm,
       "hpnsa": hpnsa,
       "hpnsaDIMM": hpnsaDIMM,
       "hpnsaDIMMMibRev": hpnsaDIMMMibRev,
       "hpnsaDIMMMibRevMajor": hpnsaDIMMMibRevMajor,
       "hpnsaDIMMMibRevMinor": hpnsaDIMMMibRevMinor,
       "hpnsaDIMMAgent": hpnsaDIMMAgent,
       "hpnsaDIMMAgentTable": hpnsaDIMMAgentTable,
       "hpnsaDIMMAgentEntry": hpnsaDIMMAgentEntry,
       "hpnsaDIMMAgentIndex": hpnsaDIMMAgentIndex,
       "hpnsaDIMMAgentName": hpnsaDIMMAgentName,
       "hpnsaDIMMAgentVersion": hpnsaDIMMAgentVersion,
       "hpnsaDIMMAgentDate": hpnsaDIMMAgentDate,
       "hpnsaDIMMInfo": hpnsaDIMMInfo,
       "hpnsaDIMMTable": hpnsaDIMMTable,
       "hpnsaDIMMEntry": hpnsaDIMMEntry,
       "hpnsaDIMMSlotIndex": hpnsaDIMMSlotIndex,
       "hpnsaDIMMSize": hpnsaDIMMSize,
       "hpnsaDIMMType": hpnsaDIMMType,
       "hpnsaDIMMSpeed": hpnsaDIMMSpeed,
       "hpnsaDIMMManufacturer": hpnsaDIMMManufacturer,
       "hpnsaDIMMManufacturerPartNumber": hpnsaDIMMManufacturerPartNumber,
       "hpnsaDIMMManufactureDateCode": hpnsaDIMMManufactureDateCode,
       "hpnsaDIMMDramType": hpnsaDIMMDramType,
       "hpnsaDIMMHPLocalEntry": hpnsaDIMMHPLocalEntry,
       "hpnsaDIMMHPSlotIndex": hpnsaDIMMHPSlotIndex,
       "hpnsaDIMMHPProductNumber": hpnsaDIMMHPProductNumber,
       "hpnsaDIMMSerialNumber": hpnsaDIMMSerialNumber}
)
