# SNMP MIB module (RADLAN-WBA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-WBA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:00 2024
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

(InetAddress,
 InetAddressIPv6,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressType")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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

(DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

rlWBA = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 230)
)
rlWBA.setRevisions(
        ("2010-07-05 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RlWBAStatusType(Integer32, TextualConvention):
    status = "current"
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
        *(("authenticated", 5),
          ("authenticating", 4),
          ("failAuthen", 2),
          ("inProcess", 1),
          ("pending", 3),
          ("unknown", 0),
          ("waitAck", 6))
    )



class RlWBARetryFlagOp(Integer32, TextualConvention):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_RlWBAAuxiliaryTable_Object = MibTable
rlWBAAuxiliaryTable = _RlWBAAuxiliaryTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 230, 1)
)
if mibBuilder.loadTexts:
    rlWBAAuxiliaryTable.setStatus("current")
_RlWBAAuxiliaryEntry_Object = MibTableRow
rlWBAAuxiliaryEntry = _RlWBAAuxiliaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 230, 1, 1)
)
rlWBAAuxiliaryEntry.setIndexNames(
    (0, "RADLAN-WBA-MIB", "rlWBAIp"),
)
if mibBuilder.loadTexts:
    rlWBAAuxiliaryEntry.setStatus("current")
_RlWBAIp_Type = InetAddress
_RlWBAIp_Object = MibTableColumn
rlWBAIp = _RlWBAIp_Object(
    (1, 3, 6, 1, 4, 1, 89, 230, 1, 1, 1),
    _RlWBAIp_Type()
)
rlWBAIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlWBAIp.setStatus("current")
_RlWBAStatus_Type = RlWBAStatusType
_RlWBAStatus_Object = MibTableColumn
rlWBAStatus = _RlWBAStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 230, 1, 1, 2),
    _RlWBAStatus_Type()
)
rlWBAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlWBAStatus.setStatus("current")
_RlAuxFailReason_Type = Integer32
_RlAuxFailReason_Object = MibTableColumn
rlAuxFailReason = _RlAuxFailReason_Object(
    (1, 3, 6, 1, 4, 1, 89, 230, 1, 1, 3),
    _RlAuxFailReason_Type()
)
rlAuxFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAuxFailReason.setStatus("current")


class _RlIsRetryFlag_Type(RlWBARetryFlagOp):
    """Custom type rlIsRetryFlag based on RlWBARetryFlagOp"""


_RlIsRetryFlag_Object = MibTableColumn
rlIsRetryFlag = _RlIsRetryFlag_Object(
    (1, 3, 6, 1, 4, 1, 89, 230, 1, 1, 4),
    _RlIsRetryFlag_Type()
)
rlIsRetryFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIsRetryFlag.setStatus("current")


class _RlWBAUsername_Type(DisplayString):
    """Custom type rlWBAUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlWBAUsername_Type.__name__ = "DisplayString"
_RlWBAUsername_Object = MibTableColumn
rlWBAUsername = _RlWBAUsername_Object(
    (1, 3, 6, 1, 4, 1, 89, 230, 1, 1, 5),
    _RlWBAUsername_Type()
)
rlWBAUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlWBAUsername.setStatus("current")


class _RlWBAPassword_Type(DisplayString):
    """Custom type rlWBAPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RlWBAPassword_Type.__name__ = "DisplayString"
_RlWBAPassword_Object = MibTableColumn
rlWBAPassword = _RlWBAPassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 230, 1, 1, 6),
    _RlWBAPassword_Type()
)
rlWBAPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlWBAPassword.setStatus("current")
_RlWBAImageTable_Object = MibTable
rlWBAImageTable = _RlWBAImageTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 230, 2)
)
if mibBuilder.loadTexts:
    rlWBAImageTable.setStatus("current")
_RlWBAImageEntry_Object = MibTableRow
rlWBAImageEntry = _RlWBAImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 230, 2, 1)
)
rlWBAImageEntry.setIndexNames(
    (0, "RADLAN-WBA-MIB", "rlWBAImageNumber"),
    (0, "RADLAN-WBA-MIB", "rlWBAImageIndex"),
)
if mibBuilder.loadTexts:
    rlWBAImageEntry.setStatus("current")


class _RlWBAImageNumber_Type(Integer32):
    """Custom type rlWBAImageNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RlWBAImageNumber_Type.__name__ = "Integer32"
_RlWBAImageNumber_Object = MibTableColumn
rlWBAImageNumber = _RlWBAImageNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 230, 2, 1, 1),
    _RlWBAImageNumber_Type()
)
rlWBAImageNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlWBAImageNumber.setStatus("current")


class _RlWBAImageIndex_Type(Integer32):
    """Custom type rlWBAImageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_RlWBAImageIndex_Type.__name__ = "Integer32"
_RlWBAImageIndex_Object = MibTableColumn
rlWBAImageIndex = _RlWBAImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 230, 2, 1, 2),
    _RlWBAImageIndex_Type()
)
rlWBAImageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlWBAImageIndex.setStatus("current")
_RlWBAImageText_Type = OctetString
_RlWBAImageText_Object = MibTableColumn
rlWBAImageText = _RlWBAImageText_Object(
    (1, 3, 6, 1, 4, 1, 89, 230, 2, 1, 3),
    _RlWBAImageText_Type()
)
rlWBAImageText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlWBAImageText.setStatus("current")
_RlWBADataTable_Object = MibTable
rlWBADataTable = _RlWBADataTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 230, 3)
)
if mibBuilder.loadTexts:
    rlWBADataTable.setStatus("current")
_RlWBADataEntry_Object = MibTableRow
rlWBADataEntry = _RlWBADataEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 230, 3, 1)
)
rlWBADataEntry.setIndexNames(
    (0, "RADLAN-WBA-MIB", "rlWBADataNumber"),
    (0, "RADLAN-WBA-MIB", "rlWBADataIndex"),
)
if mibBuilder.loadTexts:
    rlWBADataEntry.setStatus("current")


class _RlWBADataNumber_Type(Integer32):
    """Custom type rlWBADataNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RlWBADataNumber_Type.__name__ = "Integer32"
_RlWBADataNumber_Object = MibTableColumn
rlWBADataNumber = _RlWBADataNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 230, 3, 1, 1),
    _RlWBADataNumber_Type()
)
rlWBADataNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlWBADataNumber.setStatus("current")


class _RlWBADataIndex_Type(Integer32):
    """Custom type rlWBADataIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_RlWBADataIndex_Type.__name__ = "Integer32"
_RlWBADataIndex_Object = MibTableColumn
rlWBADataIndex = _RlWBADataIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 230, 3, 1, 2),
    _RlWBADataIndex_Type()
)
rlWBADataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlWBADataIndex.setStatus("current")
_RlWBADataText_Type = SnmpAdminString
_RlWBADataText_Object = MibTableColumn
rlWBADataText = _RlWBADataText_Object(
    (1, 3, 6, 1, 4, 1, 89, 230, 3, 1, 3),
    _RlWBADataText_Type()
)
rlWBADataText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlWBADataText.setStatus("current")
_RlWBAImageInfoTable_Object = MibTable
rlWBAImageInfoTable = _RlWBAImageInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 230, 4)
)
if mibBuilder.loadTexts:
    rlWBAImageInfoTable.setStatus("current")
_RlWBAImageInfoEntry_Object = MibTableRow
rlWBAImageInfoEntry = _RlWBAImageInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 230, 4, 1)
)
rlWBAImageInfoEntry.setIndexNames(
    (0, "RADLAN-WBA-MIB", "rlWBAImageInfoNumber"),
)
if mibBuilder.loadTexts:
    rlWBAImageInfoEntry.setStatus("current")


class _RlWBAImageInfoNumber_Type(Integer32):
    """Custom type rlWBAImageInfoNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RlWBAImageInfoNumber_Type.__name__ = "Integer32"
_RlWBAImageInfoNumber_Object = MibTableColumn
rlWBAImageInfoNumber = _RlWBAImageInfoNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 230, 4, 1, 1),
    _RlWBAImageInfoNumber_Type()
)
rlWBAImageInfoNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlWBAImageInfoNumber.setStatus("current")
_RlWBAImageInfoName_Type = SnmpAdminString
_RlWBAImageInfoName_Object = MibTableColumn
rlWBAImageInfoName = _RlWBAImageInfoName_Object(
    (1, 3, 6, 1, 4, 1, 89, 230, 4, 1, 2),
    _RlWBAImageInfoName_Type()
)
rlWBAImageInfoName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlWBAImageInfoName.setStatus("current")
_RlWBAImageInfoSize_Type = Integer32
_RlWBAImageInfoSize_Object = MibTableColumn
rlWBAImageInfoSize = _RlWBAImageInfoSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 230, 4, 1, 3),
    _RlWBAImageInfoSize_Type()
)
rlWBAImageInfoSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlWBAImageInfoSize.setStatus("current")
_RlWBAImageClear_Type = Integer32
_RlWBAImageClear_Object = MibScalar
rlWBAImageClear = _RlWBAImageClear_Object(
    (1, 3, 6, 1, 4, 1, 89, 230, 5),
    _RlWBAImageClear_Type()
)
rlWBAImageClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlWBAImageClear.setStatus("current")
_RlWBADataClear_Type = Integer32
_RlWBADataClear_Object = MibScalar
rlWBADataClear = _RlWBADataClear_Object(
    (1, 3, 6, 1, 4, 1, 89, 230, 6),
    _RlWBADataClear_Type()
)
rlWBADataClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlWBADataClear.setStatus("current")
_RlWBAImageDownloadFinishStatus_Type = Integer32
_RlWBAImageDownloadFinishStatus_Object = MibScalar
rlWBAImageDownloadFinishStatus = _RlWBAImageDownloadFinishStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 230, 7),
    _RlWBAImageDownloadFinishStatus_Type()
)
rlWBAImageDownloadFinishStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlWBAImageDownloadFinishStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-WBA-MIB",
    **{"RlWBAStatusType": RlWBAStatusType,
       "RlWBARetryFlagOp": RlWBARetryFlagOp,
       "rlWBA": rlWBA,
       "rlWBAAuxiliaryTable": rlWBAAuxiliaryTable,
       "rlWBAAuxiliaryEntry": rlWBAAuxiliaryEntry,
       "rlWBAIp": rlWBAIp,
       "rlWBAStatus": rlWBAStatus,
       "rlAuxFailReason": rlAuxFailReason,
       "rlIsRetryFlag": rlIsRetryFlag,
       "rlWBAUsername": rlWBAUsername,
       "rlWBAPassword": rlWBAPassword,
       "rlWBAImageTable": rlWBAImageTable,
       "rlWBAImageEntry": rlWBAImageEntry,
       "rlWBAImageNumber": rlWBAImageNumber,
       "rlWBAImageIndex": rlWBAImageIndex,
       "rlWBAImageText": rlWBAImageText,
       "rlWBADataTable": rlWBADataTable,
       "rlWBADataEntry": rlWBADataEntry,
       "rlWBADataNumber": rlWBADataNumber,
       "rlWBADataIndex": rlWBADataIndex,
       "rlWBADataText": rlWBADataText,
       "rlWBAImageInfoTable": rlWBAImageInfoTable,
       "rlWBAImageInfoEntry": rlWBAImageInfoEntry,
       "rlWBAImageInfoNumber": rlWBAImageInfoNumber,
       "rlWBAImageInfoName": rlWBAImageInfoName,
       "rlWBAImageInfoSize": rlWBAImageInfoSize,
       "rlWBAImageClear": rlWBAImageClear,
       "rlWBADataClear": rlWBADataClear,
       "rlWBAImageDownloadFinishStatus": rlWBAImageDownloadFinishStatus}
)
