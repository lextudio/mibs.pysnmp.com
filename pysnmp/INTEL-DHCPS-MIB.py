# SNMP MIB module (INTEL-DHCPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-DHCPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:34 2024
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

(mib2ext,) = mibBuilder.importSymbols(
    "INTEL-GEN-MIB",
    "mib2ext")

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

_Dhcps_ObjectIdentity = ObjectIdentity
dhcps = _Dhcps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 7)
)
_DhcpsInfo_ObjectIdentity = ObjectIdentity
dhcpsInfo = _DhcpsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 7, 1)
)
_DhcpsInfoTable_Object = MibTable
dhcpsInfoTable = _DhcpsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 7, 1, 1)
)
if mibBuilder.loadTexts:
    dhcpsInfoTable.setStatus("mandatory")
_DhcpsInfoEntry_Object = MibTableRow
dhcpsInfoEntry = _DhcpsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 7, 1, 1, 1)
)
dhcpsInfoEntry.setIndexNames(
    (0, "INTEL-DHCPS-MIB", "dhcpsInfoHostAddress"),
)
if mibBuilder.loadTexts:
    dhcpsInfoEntry.setStatus("mandatory")
_DhcpsInfoHostAddress_Type = IpAddress
_DhcpsInfoHostAddress_Object = MibTableColumn
dhcpsInfoHostAddress = _DhcpsInfoHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 7, 1, 1, 1, 1),
    _DhcpsInfoHostAddress_Type()
)
dhcpsInfoHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpsInfoHostAddress.setStatus("mandatory")


class _DhcpsInfoMacAddress_Type(OctetString):
    """Custom type dhcpsInfoMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_DhcpsInfoMacAddress_Type.__name__ = "OctetString"
_DhcpsInfoMacAddress_Object = MibTableColumn
dhcpsInfoMacAddress = _DhcpsInfoMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 7, 1, 1, 1, 2),
    _DhcpsInfoMacAddress_Type()
)
dhcpsInfoMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpsInfoMacAddress.setStatus("mandatory")


class _DhcpsInfoHostName_Type(DisplayString):
    """Custom type dhcpsInfoHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_DhcpsInfoHostName_Type.__name__ = "DisplayString"
_DhcpsInfoHostName_Object = MibTableColumn
dhcpsInfoHostName = _DhcpsInfoHostName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 7, 1, 1, 1, 3),
    _DhcpsInfoHostName_Type()
)
dhcpsInfoHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpsInfoHostName.setStatus("mandatory")
_DhcpsInfoAge_Type = Integer32
_DhcpsInfoAge_Object = MibTableColumn
dhcpsInfoAge = _DhcpsInfoAge_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 7, 1, 1, 1, 4),
    _DhcpsInfoAge_Type()
)
dhcpsInfoAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpsInfoAge.setStatus("mandatory")


class _DhcpsInfoState_Type(Integer32):
    """Custom type dhcpsInfoState based on Integer32"""
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
        *(("assigned", 4),
          ("declined", 2),
          ("deleted", 1),
          ("modified", 5),
          ("obsolete", 9),
          ("offered", 3),
          ("pinged", 6),
          ("released", 8),
          ("reserved", 7))
    )


_DhcpsInfoState_Type.__name__ = "Integer32"
_DhcpsInfoState_Object = MibTableColumn
dhcpsInfoState = _DhcpsInfoState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 7, 1, 1, 1, 5),
    _DhcpsInfoState_Type()
)
dhcpsInfoState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpsInfoState.setStatus("mandatory")
_DhcpsConf_ObjectIdentity = ObjectIdentity
dhcpsConf = _DhcpsConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 7, 2)
)
_DhcpsConfInfoTable_Object = MibTable
dhcpsConfInfoTable = _DhcpsConfInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 1)
)
if mibBuilder.loadTexts:
    dhcpsConfInfoTable.setStatus("mandatory")
_DhcpsConfInfoEntry_Object = MibTableRow
dhcpsConfInfoEntry = _DhcpsConfInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 1, 1)
)
dhcpsConfInfoEntry.setIndexNames(
    (0, "INTEL-DHCPS-MIB", "dhcpsConfInfoId"),
)
if mibBuilder.loadTexts:
    dhcpsConfInfoEntry.setStatus("mandatory")


class _DhcpsConfInfoId_Type(OctetString):
    """Custom type dhcpsConfInfoId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_DhcpsConfInfoId_Type.__name__ = "OctetString"
_DhcpsConfInfoId_Object = MibTableColumn
dhcpsConfInfoId = _DhcpsConfInfoId_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 1, 1, 1),
    _DhcpsConfInfoId_Type()
)
dhcpsConfInfoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpsConfInfoId.setStatus("mandatory")
_DhcpsConfInfoHandle_Type = Integer32
_DhcpsConfInfoHandle_Object = MibTableColumn
dhcpsConfInfoHandle = _DhcpsConfInfoHandle_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 1, 1, 2),
    _DhcpsConfInfoHandle_Type()
)
dhcpsConfInfoHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpsConfInfoHandle.setStatus("mandatory")


class _DhcpsConfInfoType_Type(Integer32):
    """Custom type dhcpsConfInfoType based on Integer32"""
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
        *(("noTable", 1),
          ("tableIndexSize0", 2),
          ("tableIndexSize1", 3),
          ("tableIndexSize2", 4),
          ("tableIndexSize4", 5))
    )


_DhcpsConfInfoType_Type.__name__ = "Integer32"
_DhcpsConfInfoType_Object = MibTableColumn
dhcpsConfInfoType = _DhcpsConfInfoType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 1, 1, 3),
    _DhcpsConfInfoType_Type()
)
dhcpsConfInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpsConfInfoType.setStatus("mandatory")
_DhcpsConfInfoTableOffset_Type = Integer32
_DhcpsConfInfoTableOffset_Object = MibTableColumn
dhcpsConfInfoTableOffset = _DhcpsConfInfoTableOffset_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 1, 1, 4),
    _DhcpsConfInfoTableOffset_Type()
)
dhcpsConfInfoTableOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpsConfInfoTableOffset.setStatus("mandatory")
_DhcpsConfInfoIndexOffset_Type = Integer32
_DhcpsConfInfoIndexOffset_Object = MibTableColumn
dhcpsConfInfoIndexOffset = _DhcpsConfInfoIndexOffset_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 1, 1, 5),
    _DhcpsConfInfoIndexOffset_Type()
)
dhcpsConfInfoIndexOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpsConfInfoIndexOffset.setStatus("mandatory")
_DhcpsConfInfoRecordCount_Type = Integer32
_DhcpsConfInfoRecordCount_Object = MibTableColumn
dhcpsConfInfoRecordCount = _DhcpsConfInfoRecordCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 1, 1, 6),
    _DhcpsConfInfoRecordCount_Type()
)
dhcpsConfInfoRecordCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpsConfInfoRecordCount.setStatus("mandatory")
_DhcpsConfInfoRecordLength_Type = Integer32
_DhcpsConfInfoRecordLength_Object = MibTableColumn
dhcpsConfInfoRecordLength = _DhcpsConfInfoRecordLength_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 1, 1, 7),
    _DhcpsConfInfoRecordLength_Type()
)
dhcpsConfInfoRecordLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpsConfInfoRecordLength.setStatus("mandatory")
_DhcpsConfTable_Object = MibTable
dhcpsConfTable = _DhcpsConfTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 2)
)
if mibBuilder.loadTexts:
    dhcpsConfTable.setStatus("mandatory")
_DhcpsConfEntry_Object = MibTableRow
dhcpsConfEntry = _DhcpsConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 2, 1)
)
dhcpsConfEntry.setIndexNames(
    (0, "INTEL-DHCPS-MIB", "dhcpsConfId"),
    (0, "INTEL-DHCPS-MIB", "dhcpsConfIndex"),
    (0, "INTEL-DHCPS-MIB", "dhcpsConfHandle"),
)
if mibBuilder.loadTexts:
    dhcpsConfEntry.setStatus("mandatory")


class _DhcpsConfId_Type(OctetString):
    """Custom type dhcpsConfId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_DhcpsConfId_Type.__name__ = "OctetString"
_DhcpsConfId_Object = MibTableColumn
dhcpsConfId = _DhcpsConfId_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 2, 1, 1),
    _DhcpsConfId_Type()
)
dhcpsConfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpsConfId.setStatus("mandatory")


class _DhcpsConfIndex_Type(OctetString):
    """Custom type dhcpsConfIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_DhcpsConfIndex_Type.__name__ = "OctetString"
_DhcpsConfIndex_Object = MibTableColumn
dhcpsConfIndex = _DhcpsConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 2, 1, 2),
    _DhcpsConfIndex_Type()
)
dhcpsConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpsConfIndex.setStatus("mandatory")
_DhcpsConfHandle_Type = Integer32
_DhcpsConfHandle_Object = MibTableColumn
dhcpsConfHandle = _DhcpsConfHandle_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 2, 1, 3),
    _DhcpsConfHandle_Type()
)
dhcpsConfHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpsConfHandle.setStatus("mandatory")


class _DhcpsConfData_Type(OctetString):
    """Custom type dhcpsConfData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_DhcpsConfData_Type.__name__ = "OctetString"
_DhcpsConfData_Object = MibTableColumn
dhcpsConfData = _DhcpsConfData_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 2, 1, 4),
    _DhcpsConfData_Type()
)
dhcpsConfData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpsConfData.setStatus("mandatory")
_DhcpsConfOptions_Type = Integer32
_DhcpsConfOptions_Object = MibTableColumn
dhcpsConfOptions = _DhcpsConfOptions_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 2, 1, 5),
    _DhcpsConfOptions_Type()
)
dhcpsConfOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpsConfOptions.setStatus("mandatory")


class _DhcpsConfStatus_Type(Integer32):
    """Custom type dhcpsConfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copy", 3),
          ("delete", 2),
          ("normal", 1))
    )


_DhcpsConfStatus_Type.__name__ = "Integer32"
_DhcpsConfStatus_Object = MibTableColumn
dhcpsConfStatus = _DhcpsConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 7, 2, 2, 1, 6),
    _DhcpsConfStatus_Type()
)
dhcpsConfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpsConfStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-DHCPS-MIB",
    **{"dhcps": dhcps,
       "dhcpsInfo": dhcpsInfo,
       "dhcpsInfoTable": dhcpsInfoTable,
       "dhcpsInfoEntry": dhcpsInfoEntry,
       "dhcpsInfoHostAddress": dhcpsInfoHostAddress,
       "dhcpsInfoMacAddress": dhcpsInfoMacAddress,
       "dhcpsInfoHostName": dhcpsInfoHostName,
       "dhcpsInfoAge": dhcpsInfoAge,
       "dhcpsInfoState": dhcpsInfoState,
       "dhcpsConf": dhcpsConf,
       "dhcpsConfInfoTable": dhcpsConfInfoTable,
       "dhcpsConfInfoEntry": dhcpsConfInfoEntry,
       "dhcpsConfInfoId": dhcpsConfInfoId,
       "dhcpsConfInfoHandle": dhcpsConfInfoHandle,
       "dhcpsConfInfoType": dhcpsConfInfoType,
       "dhcpsConfInfoTableOffset": dhcpsConfInfoTableOffset,
       "dhcpsConfInfoIndexOffset": dhcpsConfInfoIndexOffset,
       "dhcpsConfInfoRecordCount": dhcpsConfInfoRecordCount,
       "dhcpsConfInfoRecordLength": dhcpsConfInfoRecordLength,
       "dhcpsConfTable": dhcpsConfTable,
       "dhcpsConfEntry": dhcpsConfEntry,
       "dhcpsConfId": dhcpsConfId,
       "dhcpsConfIndex": dhcpsConfIndex,
       "dhcpsConfHandle": dhcpsConfHandle,
       "dhcpsConfData": dhcpsConfData,
       "dhcpsConfOptions": dhcpsConfOptions,
       "dhcpsConfStatus": dhcpsConfStatus}
)
