# SNMP MIB module (Nortel-Magellan-Passport-DataIsdnMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-DataIsdnMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:33 2024
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

(DisplayString,
 Integer32,
 InterfaceIndex,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "DisplayString",
    "Integer32",
    "InterfaceIndex",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 DigitString,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "DigitString",
    "NonReplicated")

(components,
 passportMIBs) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "components",
    "passportMIBs")

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

_DataSigChan_ObjectIdentity = ObjectIdentity
dataSigChan = _DataSigChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120)
)
_DataSigChanRowStatusTable_Object = MibTable
dataSigChanRowStatusTable = _DataSigChanRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 1)
)
if mibBuilder.loadTexts:
    dataSigChanRowStatusTable.setStatus("mandatory")
_DataSigChanRowStatusEntry_Object = MibTableRow
dataSigChanRowStatusEntry = _DataSigChanRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 1, 1)
)
dataSigChanRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanRowStatusEntry.setStatus("mandatory")
_DataSigChanRowStatus_Type = RowStatus
_DataSigChanRowStatus_Object = MibTableColumn
dataSigChanRowStatus = _DataSigChanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 1, 1, 1),
    _DataSigChanRowStatus_Type()
)
dataSigChanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanRowStatus.setStatus("mandatory")
_DataSigChanComponentName_Type = DisplayString
_DataSigChanComponentName_Object = MibTableColumn
dataSigChanComponentName = _DataSigChanComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 1, 1, 2),
    _DataSigChanComponentName_Type()
)
dataSigChanComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanComponentName.setStatus("mandatory")
_DataSigChanStorageType_Type = StorageType
_DataSigChanStorageType_Object = MibTableColumn
dataSigChanStorageType = _DataSigChanStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 1, 1, 4),
    _DataSigChanStorageType_Type()
)
dataSigChanStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanStorageType.setStatus("mandatory")


class _DataSigChanIndex_Type(Integer32):
    """Custom type dataSigChanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DataSigChanIndex_Type.__name__ = "Integer32"
_DataSigChanIndex_Object = MibTableColumn
dataSigChanIndex = _DataSigChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 1, 1, 10),
    _DataSigChanIndex_Type()
)
dataSigChanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataSigChanIndex.setStatus("mandatory")
_DataSigChanCc_ObjectIdentity = ObjectIdentity
dataSigChanCc = _DataSigChanCc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2)
)
_DataSigChanCcRowStatusTable_Object = MibTable
dataSigChanCcRowStatusTable = _DataSigChanCcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 1)
)
if mibBuilder.loadTexts:
    dataSigChanCcRowStatusTable.setStatus("mandatory")
_DataSigChanCcRowStatusEntry_Object = MibTableRow
dataSigChanCcRowStatusEntry = _DataSigChanCcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 1, 1)
)
dataSigChanCcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanCcRowStatusEntry.setStatus("mandatory")
_DataSigChanCcRowStatus_Type = RowStatus
_DataSigChanCcRowStatus_Object = MibTableColumn
dataSigChanCcRowStatus = _DataSigChanCcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 1, 1, 1),
    _DataSigChanCcRowStatus_Type()
)
dataSigChanCcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcRowStatus.setStatus("mandatory")
_DataSigChanCcComponentName_Type = DisplayString
_DataSigChanCcComponentName_Object = MibTableColumn
dataSigChanCcComponentName = _DataSigChanCcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 1, 1, 2),
    _DataSigChanCcComponentName_Type()
)
dataSigChanCcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcComponentName.setStatus("mandatory")
_DataSigChanCcStorageType_Type = StorageType
_DataSigChanCcStorageType_Object = MibTableColumn
dataSigChanCcStorageType = _DataSigChanCcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 1, 1, 4),
    _DataSigChanCcStorageType_Type()
)
dataSigChanCcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcStorageType.setStatus("mandatory")
_DataSigChanCcIndex_Type = NonReplicated
_DataSigChanCcIndex_Object = MibTableColumn
dataSigChanCcIndex = _DataSigChanCcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 1, 1, 10),
    _DataSigChanCcIndex_Type()
)
dataSigChanCcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataSigChanCcIndex.setStatus("mandatory")
_DataSigChanCcCg_ObjectIdentity = ObjectIdentity
dataSigChanCcCg = _DataSigChanCcCg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2)
)
_DataSigChanCcCgRowStatusTable_Object = MibTable
dataSigChanCcCgRowStatusTable = _DataSigChanCcCgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dataSigChanCcCgRowStatusTable.setStatus("mandatory")
_DataSigChanCcCgRowStatusEntry_Object = MibTableRow
dataSigChanCcCgRowStatusEntry = _DataSigChanCcCgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 1, 1)
)
dataSigChanCcCgRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcCgIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanCcCgRowStatusEntry.setStatus("mandatory")
_DataSigChanCcCgRowStatus_Type = RowStatus
_DataSigChanCcCgRowStatus_Object = MibTableColumn
dataSigChanCcCgRowStatus = _DataSigChanCcCgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 1, 1, 1),
    _DataSigChanCcCgRowStatus_Type()
)
dataSigChanCcCgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanCcCgRowStatus.setStatus("mandatory")
_DataSigChanCcCgComponentName_Type = DisplayString
_DataSigChanCcCgComponentName_Object = MibTableColumn
dataSigChanCcCgComponentName = _DataSigChanCcCgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 1, 1, 2),
    _DataSigChanCcCgComponentName_Type()
)
dataSigChanCcCgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcCgComponentName.setStatus("mandatory")
_DataSigChanCcCgStorageType_Type = StorageType
_DataSigChanCcCgStorageType_Object = MibTableColumn
dataSigChanCcCgStorageType = _DataSigChanCcCgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 1, 1, 4),
    _DataSigChanCcCgStorageType_Type()
)
dataSigChanCcCgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcCgStorageType.setStatus("mandatory")


class _DataSigChanCcCgIndex_Type(Integer32):
    """Custom type dataSigChanCcCgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_DataSigChanCcCgIndex_Type.__name__ = "Integer32"
_DataSigChanCcCgIndex_Object = MibTableColumn
dataSigChanCcCgIndex = _DataSigChanCcCgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 1, 1, 10),
    _DataSigChanCcCgIndex_Type()
)
dataSigChanCcCgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataSigChanCcCgIndex.setStatus("mandatory")
_DataSigChanCcCgCgpn_ObjectIdentity = ObjectIdentity
dataSigChanCcCgCgpn = _DataSigChanCcCgCgpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 2)
)
_DataSigChanCcCgCgpnRowStatusTable_Object = MibTable
dataSigChanCcCgCgpnRowStatusTable = _DataSigChanCcCgCgpnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dataSigChanCcCgCgpnRowStatusTable.setStatus("mandatory")
_DataSigChanCcCgCgpnRowStatusEntry_Object = MibTableRow
dataSigChanCcCgCgpnRowStatusEntry = _DataSigChanCcCgCgpnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 2, 1, 1)
)
dataSigChanCcCgCgpnRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcCgIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcCgCgpnIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanCcCgCgpnRowStatusEntry.setStatus("mandatory")
_DataSigChanCcCgCgpnRowStatus_Type = RowStatus
_DataSigChanCcCgCgpnRowStatus_Object = MibTableColumn
dataSigChanCcCgCgpnRowStatus = _DataSigChanCcCgCgpnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 2, 1, 1, 1),
    _DataSigChanCcCgCgpnRowStatus_Type()
)
dataSigChanCcCgCgpnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanCcCgCgpnRowStatus.setStatus("mandatory")
_DataSigChanCcCgCgpnComponentName_Type = DisplayString
_DataSigChanCcCgCgpnComponentName_Object = MibTableColumn
dataSigChanCcCgCgpnComponentName = _DataSigChanCcCgCgpnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 2, 1, 1, 2),
    _DataSigChanCcCgCgpnComponentName_Type()
)
dataSigChanCcCgCgpnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcCgCgpnComponentName.setStatus("mandatory")
_DataSigChanCcCgCgpnStorageType_Type = StorageType
_DataSigChanCcCgCgpnStorageType_Object = MibTableColumn
dataSigChanCcCgCgpnStorageType = _DataSigChanCcCgCgpnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 2, 1, 1, 4),
    _DataSigChanCcCgCgpnStorageType_Type()
)
dataSigChanCcCgCgpnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcCgCgpnStorageType.setStatus("mandatory")


class _DataSigChanCcCgCgpnIndex_Type(DigitString):
    """Custom type dataSigChanCcCgCgpnIndex based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 14),
    )


_DataSigChanCcCgCgpnIndex_Type.__name__ = "DigitString"
_DataSigChanCcCgCgpnIndex_Object = MibTableColumn
dataSigChanCcCgCgpnIndex = _DataSigChanCcCgCgpnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 2, 1, 1, 10),
    _DataSigChanCcCgCgpnIndex_Type()
)
dataSigChanCcCgCgpnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataSigChanCcCgCgpnIndex.setStatus("mandatory")
_DataSigChanCcCgBch_ObjectIdentity = ObjectIdentity
dataSigChanCcCgBch = _DataSigChanCcCgBch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 3)
)
_DataSigChanCcCgBchRowStatusTable_Object = MibTable
dataSigChanCcCgBchRowStatusTable = _DataSigChanCcCgBchRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    dataSigChanCcCgBchRowStatusTable.setStatus("mandatory")
_DataSigChanCcCgBchRowStatusEntry_Object = MibTableRow
dataSigChanCcCgBchRowStatusEntry = _DataSigChanCcCgBchRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 3, 1, 1)
)
dataSigChanCcCgBchRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcCgIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcCgBchIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanCcCgBchRowStatusEntry.setStatus("mandatory")
_DataSigChanCcCgBchRowStatus_Type = RowStatus
_DataSigChanCcCgBchRowStatus_Object = MibTableColumn
dataSigChanCcCgBchRowStatus = _DataSigChanCcCgBchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 3, 1, 1, 1),
    _DataSigChanCcCgBchRowStatus_Type()
)
dataSigChanCcCgBchRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcCgBchRowStatus.setStatus("mandatory")
_DataSigChanCcCgBchComponentName_Type = DisplayString
_DataSigChanCcCgBchComponentName_Object = MibTableColumn
dataSigChanCcCgBchComponentName = _DataSigChanCcCgBchComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 3, 1, 1, 2),
    _DataSigChanCcCgBchComponentName_Type()
)
dataSigChanCcCgBchComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcCgBchComponentName.setStatus("mandatory")
_DataSigChanCcCgBchStorageType_Type = StorageType
_DataSigChanCcCgBchStorageType_Object = MibTableColumn
dataSigChanCcCgBchStorageType = _DataSigChanCcCgBchStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 3, 1, 1, 4),
    _DataSigChanCcCgBchStorageType_Type()
)
dataSigChanCcCgBchStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcCgBchStorageType.setStatus("mandatory")


class _DataSigChanCcCgBchIndex_Type(Integer32):
    """Custom type dataSigChanCcCgBchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_DataSigChanCcCgBchIndex_Type.__name__ = "Integer32"
_DataSigChanCcCgBchIndex_Object = MibTableColumn
dataSigChanCcCgBchIndex = _DataSigChanCcCgBchIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 3, 1, 1, 10),
    _DataSigChanCcCgBchIndex_Type()
)
dataSigChanCcCgBchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataSigChanCcCgBchIndex.setStatus("mandatory")
_DataSigChanCcCgBchBchanOpDataTable_Object = MibTable
dataSigChanCcCgBchBchanOpDataTable = _DataSigChanCcCgBchBchanOpDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    dataSigChanCcCgBchBchanOpDataTable.setStatus("mandatory")
_DataSigChanCcCgBchBchanOpDataEntry_Object = MibTableRow
dataSigChanCcCgBchBchanOpDataEntry = _DataSigChanCcCgBchBchanOpDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 3, 2, 1)
)
dataSigChanCcCgBchBchanOpDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcCgIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcCgBchIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanCcCgBchBchanOpDataEntry.setStatus("mandatory")


class _DataSigChanCcCgBchState_Type(Integer32):
    """Custom type dataSigChanCcCgBchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("busy", 1),
          ("disabled", 2),
          ("idle", 0),
          ("noProtocolProvisioned", 3))
    )


_DataSigChanCcCgBchState_Type.__name__ = "Integer32"
_DataSigChanCcCgBchState_Object = MibTableColumn
dataSigChanCcCgBchState = _DataSigChanCcCgBchState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 3, 2, 1, 1),
    _DataSigChanCcCgBchState_Type()
)
dataSigChanCcCgBchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcCgBchState.setStatus("mandatory")


class _DataSigChanCcCgBchCallingPartyNumber_Type(DigitString):
    """Custom type dataSigChanCcCgBchCallingPartyNumber based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 14),
    )


_DataSigChanCcCgBchCallingPartyNumber_Type.__name__ = "DigitString"
_DataSigChanCcCgBchCallingPartyNumber_Object = MibTableColumn
dataSigChanCcCgBchCallingPartyNumber = _DataSigChanCcCgBchCallingPartyNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 3, 2, 1, 2),
    _DataSigChanCcCgBchCallingPartyNumber_Type()
)
dataSigChanCcCgBchCallingPartyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcCgBchCallingPartyNumber.setStatus("mandatory")


class _DataSigChanCcCgBchLastQ931ClearCause_Type(Integer32):
    """Custom type dataSigChanCcCgBchLastQ931ClearCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DataSigChanCcCgBchLastQ931ClearCause_Type.__name__ = "Integer32"
_DataSigChanCcCgBchLastQ931ClearCause_Object = MibTableColumn
dataSigChanCcCgBchLastQ931ClearCause = _DataSigChanCcCgBchLastQ931ClearCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 3, 2, 1, 3),
    _DataSigChanCcCgBchLastQ931ClearCause_Type()
)
dataSigChanCcCgBchLastQ931ClearCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcCgBchLastQ931ClearCause.setStatus("mandatory")


class _DataSigChanCcCgBchRunningApplication_Type(AsciiString):
    """Custom type dataSigChanCcCgBchRunningApplication based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DataSigChanCcCgBchRunningApplication_Type.__name__ = "AsciiString"
_DataSigChanCcCgBchRunningApplication_Object = MibTableColumn
dataSigChanCcCgBchRunningApplication = _DataSigChanCcCgBchRunningApplication_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 3, 2, 1, 4),
    _DataSigChanCcCgBchRunningApplication_Type()
)
dataSigChanCcCgBchRunningApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcCgBchRunningApplication.setStatus("mandatory")
_DataSigChanCcCgCidDataTable_Object = MibTable
dataSigChanCcCgCidDataTable = _DataSigChanCcCgCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 10)
)
if mibBuilder.loadTexts:
    dataSigChanCcCgCidDataTable.setStatus("mandatory")
_DataSigChanCcCgCidDataEntry_Object = MibTableRow
dataSigChanCcCgCidDataEntry = _DataSigChanCcCgCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 10, 1)
)
dataSigChanCcCgCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcCgIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanCcCgCidDataEntry.setStatus("mandatory")


class _DataSigChanCcCgCustomerIdentifier_Type(Unsigned32):
    """Custom type dataSigChanCcCgCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_DataSigChanCcCgCustomerIdentifier_Type.__name__ = "Unsigned32"
_DataSigChanCcCgCustomerIdentifier_Object = MibTableColumn
dataSigChanCcCgCustomerIdentifier = _DataSigChanCcCgCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 10, 1, 1),
    _DataSigChanCcCgCustomerIdentifier_Type()
)
dataSigChanCcCgCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanCcCgCustomerIdentifier.setStatus("mandatory")
_DataSigChanCcCgProvTable_Object = MibTable
dataSigChanCcCgProvTable = _DataSigChanCcCgProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 11)
)
if mibBuilder.loadTexts:
    dataSigChanCcCgProvTable.setStatus("mandatory")
_DataSigChanCcCgProvEntry_Object = MibTableRow
dataSigChanCcCgProvEntry = _DataSigChanCcCgProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 11, 1)
)
dataSigChanCcCgProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcCgIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanCcCgProvEntry.setStatus("mandatory")


class _DataSigChanCcCgCommentText_Type(AsciiString):
    """Custom type dataSigChanCcCgCommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_DataSigChanCcCgCommentText_Type.__name__ = "AsciiString"
_DataSigChanCcCgCommentText_Object = MibTableColumn
dataSigChanCcCgCommentText = _DataSigChanCcCgCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 11, 1, 1),
    _DataSigChanCcCgCommentText_Type()
)
dataSigChanCcCgCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanCcCgCommentText.setStatus("mandatory")


class _DataSigChanCcCgScreeningIndicator_Type(OctetString):
    """Custom type dataSigChanCcCgScreeningIndicator based on OctetString"""
    defaultHexValue = "50"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DataSigChanCcCgScreeningIndicator_Type.__name__ = "OctetString"
_DataSigChanCcCgScreeningIndicator_Object = MibTableColumn
dataSigChanCcCgScreeningIndicator = _DataSigChanCcCgScreeningIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 11, 1, 2),
    _DataSigChanCcCgScreeningIndicator_Type()
)
dataSigChanCcCgScreeningIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanCcCgScreeningIndicator.setStatus("mandatory")


class _DataSigChanCcCgChannelAssignmentOrder_Type(Integer32):
    """Custom type dataSigChanCcCgChannelAssignmentOrder based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ascending", 0),
          ("descending", 1))
    )


_DataSigChanCcCgChannelAssignmentOrder_Type.__name__ = "Integer32"
_DataSigChanCcCgChannelAssignmentOrder_Object = MibTableColumn
dataSigChanCcCgChannelAssignmentOrder = _DataSigChanCcCgChannelAssignmentOrder_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 11, 1, 3),
    _DataSigChanCcCgChannelAssignmentOrder_Type()
)
dataSigChanCcCgChannelAssignmentOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanCcCgChannelAssignmentOrder.setStatus("mandatory")


class _DataSigChanCcCgChannelList_Type(OctetString):
    """Custom type dataSigChanCcCgChannelList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_DataSigChanCcCgChannelList_Type.__name__ = "OctetString"
_DataSigChanCcCgChannelList_Object = MibTableColumn
dataSigChanCcCgChannelList = _DataSigChanCcCgChannelList_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 11, 1, 4),
    _DataSigChanCcCgChannelList_Type()
)
dataSigChanCcCgChannelList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanCcCgChannelList.setStatus("mandatory")
_DataSigChanCcCgStatsTable_Object = MibTable
dataSigChanCcCgStatsTable = _DataSigChanCcCgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 12)
)
if mibBuilder.loadTexts:
    dataSigChanCcCgStatsTable.setStatus("mandatory")
_DataSigChanCcCgStatsEntry_Object = MibTableRow
dataSigChanCcCgStatsEntry = _DataSigChanCcCgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 12, 1)
)
dataSigChanCcCgStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcCgIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanCcCgStatsEntry.setStatus("mandatory")


class _DataSigChanCcCgTotalInCalls_Type(Unsigned32):
    """Custom type dataSigChanCcCgTotalInCalls based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanCcCgTotalInCalls_Type.__name__ = "Unsigned32"
_DataSigChanCcCgTotalInCalls_Object = MibTableColumn
dataSigChanCcCgTotalInCalls = _DataSigChanCcCgTotalInCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 12, 1, 1),
    _DataSigChanCcCgTotalInCalls_Type()
)
dataSigChanCcCgTotalInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcCgTotalInCalls.setStatus("mandatory")


class _DataSigChanCcCgSuccessfullInCalls_Type(Unsigned32):
    """Custom type dataSigChanCcCgSuccessfullInCalls based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanCcCgSuccessfullInCalls_Type.__name__ = "Unsigned32"
_DataSigChanCcCgSuccessfullInCalls_Object = MibTableColumn
dataSigChanCcCgSuccessfullInCalls = _DataSigChanCcCgSuccessfullInCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 12, 1, 2),
    _DataSigChanCcCgSuccessfullInCalls_Type()
)
dataSigChanCcCgSuccessfullInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcCgSuccessfullInCalls.setStatus("mandatory")


class _DataSigChanCcCgRejectedNoChanAvail_Type(Unsigned32):
    """Custom type dataSigChanCcCgRejectedNoChanAvail based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanCcCgRejectedNoChanAvail_Type.__name__ = "Unsigned32"
_DataSigChanCcCgRejectedNoChanAvail_Object = MibTableColumn
dataSigChanCcCgRejectedNoChanAvail = _DataSigChanCcCgRejectedNoChanAvail_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 12, 1, 3),
    _DataSigChanCcCgRejectedNoChanAvail_Type()
)
dataSigChanCcCgRejectedNoChanAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcCgRejectedNoChanAvail.setStatus("mandatory")


class _DataSigChanCcCgIdleChannelCount_Type(Integer32):
    """Custom type dataSigChanCcCgIdleChannelCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DataSigChanCcCgIdleChannelCount_Type.__name__ = "Integer32"
_DataSigChanCcCgIdleChannelCount_Object = MibTableColumn
dataSigChanCcCgIdleChannelCount = _DataSigChanCcCgIdleChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 12, 1, 4),
    _DataSigChanCcCgIdleChannelCount_Type()
)
dataSigChanCcCgIdleChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcCgIdleChannelCount.setStatus("mandatory")


class _DataSigChanCcCgBusyChannelCount_Type(Integer32):
    """Custom type dataSigChanCcCgBusyChannelCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DataSigChanCcCgBusyChannelCount_Type.__name__ = "Integer32"
_DataSigChanCcCgBusyChannelCount_Object = MibTableColumn
dataSigChanCcCgBusyChannelCount = _DataSigChanCcCgBusyChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 2, 12, 1, 5),
    _DataSigChanCcCgBusyChannelCount_Type()
)
dataSigChanCcCgBusyChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcCgBusyChannelCount.setStatus("mandatory")
_DataSigChanCcTr_ObjectIdentity = ObjectIdentity
dataSigChanCcTr = _DataSigChanCcTr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 3)
)
_DataSigChanCcTrRowStatusTable_Object = MibTable
dataSigChanCcTrRowStatusTable = _DataSigChanCcTrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 3, 1)
)
if mibBuilder.loadTexts:
    dataSigChanCcTrRowStatusTable.setStatus("mandatory")
_DataSigChanCcTrRowStatusEntry_Object = MibTableRow
dataSigChanCcTrRowStatusEntry = _DataSigChanCcTrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 3, 1, 1)
)
dataSigChanCcTrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcTrIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanCcTrRowStatusEntry.setStatus("mandatory")
_DataSigChanCcTrRowStatus_Type = RowStatus
_DataSigChanCcTrRowStatus_Object = MibTableColumn
dataSigChanCcTrRowStatus = _DataSigChanCcTrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 3, 1, 1, 1),
    _DataSigChanCcTrRowStatus_Type()
)
dataSigChanCcTrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanCcTrRowStatus.setStatus("mandatory")
_DataSigChanCcTrComponentName_Type = DisplayString
_DataSigChanCcTrComponentName_Object = MibTableColumn
dataSigChanCcTrComponentName = _DataSigChanCcTrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 3, 1, 1, 2),
    _DataSigChanCcTrComponentName_Type()
)
dataSigChanCcTrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcTrComponentName.setStatus("mandatory")
_DataSigChanCcTrStorageType_Type = StorageType
_DataSigChanCcTrStorageType_Object = MibTableColumn
dataSigChanCcTrStorageType = _DataSigChanCcTrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 3, 1, 1, 4),
    _DataSigChanCcTrStorageType_Type()
)
dataSigChanCcTrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcTrStorageType.setStatus("mandatory")
_DataSigChanCcTrIndex_Type = NonReplicated
_DataSigChanCcTrIndex_Object = MibTableColumn
dataSigChanCcTrIndex = _DataSigChanCcTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 3, 1, 1, 10),
    _DataSigChanCcTrIndex_Type()
)
dataSigChanCcTrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataSigChanCcTrIndex.setStatus("mandatory")
_DataSigChanCcTrPri_ObjectIdentity = ObjectIdentity
dataSigChanCcTrPri = _DataSigChanCcTrPri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 3, 2)
)
_DataSigChanCcTrPriRowStatusTable_Object = MibTable
dataSigChanCcTrPriRowStatusTable = _DataSigChanCcTrPriRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    dataSigChanCcTrPriRowStatusTable.setStatus("mandatory")
_DataSigChanCcTrPriRowStatusEntry_Object = MibTableRow
dataSigChanCcTrPriRowStatusEntry = _DataSigChanCcTrPriRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 3, 2, 1, 1)
)
dataSigChanCcTrPriRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcTrIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcTrPriIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanCcTrPriRowStatusEntry.setStatus("mandatory")
_DataSigChanCcTrPriRowStatus_Type = RowStatus
_DataSigChanCcTrPriRowStatus_Object = MibTableColumn
dataSigChanCcTrPriRowStatus = _DataSigChanCcTrPriRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 3, 2, 1, 1, 1),
    _DataSigChanCcTrPriRowStatus_Type()
)
dataSigChanCcTrPriRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcTrPriRowStatus.setStatus("mandatory")
_DataSigChanCcTrPriComponentName_Type = DisplayString
_DataSigChanCcTrPriComponentName_Object = MibTableColumn
dataSigChanCcTrPriComponentName = _DataSigChanCcTrPriComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 3, 2, 1, 1, 2),
    _DataSigChanCcTrPriComponentName_Type()
)
dataSigChanCcTrPriComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcTrPriComponentName.setStatus("mandatory")
_DataSigChanCcTrPriStorageType_Type = StorageType
_DataSigChanCcTrPriStorageType_Object = MibTableColumn
dataSigChanCcTrPriStorageType = _DataSigChanCcTrPriStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 3, 2, 1, 1, 4),
    _DataSigChanCcTrPriStorageType_Type()
)
dataSigChanCcTrPriStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcTrPriStorageType.setStatus("mandatory")


class _DataSigChanCcTrPriIndex_Type(Integer32):
    """Custom type dataSigChanCcTrPriIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_DataSigChanCcTrPriIndex_Type.__name__ = "Integer32"
_DataSigChanCcTrPriIndex_Object = MibTableColumn
dataSigChanCcTrPriIndex = _DataSigChanCcTrPriIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 3, 2, 1, 1, 10),
    _DataSigChanCcTrPriIndex_Type()
)
dataSigChanCcTrPriIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataSigChanCcTrPriIndex.setStatus("mandatory")
_DataSigChanCcTrPriBch_ObjectIdentity = ObjectIdentity
dataSigChanCcTrPriBch = _DataSigChanCcTrPriBch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 3, 2, 2)
)
_DataSigChanCcTrPriBchRowStatusTable_Object = MibTable
dataSigChanCcTrPriBchRowStatusTable = _DataSigChanCcTrPriBchRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dataSigChanCcTrPriBchRowStatusTable.setStatus("mandatory")
_DataSigChanCcTrPriBchRowStatusEntry_Object = MibTableRow
dataSigChanCcTrPriBchRowStatusEntry = _DataSigChanCcTrPriBchRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 3, 2, 2, 1, 1)
)
dataSigChanCcTrPriBchRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcTrIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcTrPriIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcTrPriBchIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanCcTrPriBchRowStatusEntry.setStatus("mandatory")
_DataSigChanCcTrPriBchRowStatus_Type = RowStatus
_DataSigChanCcTrPriBchRowStatus_Object = MibTableColumn
dataSigChanCcTrPriBchRowStatus = _DataSigChanCcTrPriBchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 3, 2, 2, 1, 1, 1),
    _DataSigChanCcTrPriBchRowStatus_Type()
)
dataSigChanCcTrPriBchRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcTrPriBchRowStatus.setStatus("mandatory")
_DataSigChanCcTrPriBchComponentName_Type = DisplayString
_DataSigChanCcTrPriBchComponentName_Object = MibTableColumn
dataSigChanCcTrPriBchComponentName = _DataSigChanCcTrPriBchComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 3, 2, 2, 1, 1, 2),
    _DataSigChanCcTrPriBchComponentName_Type()
)
dataSigChanCcTrPriBchComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcTrPriBchComponentName.setStatus("mandatory")
_DataSigChanCcTrPriBchStorageType_Type = StorageType
_DataSigChanCcTrPriBchStorageType_Object = MibTableColumn
dataSigChanCcTrPriBchStorageType = _DataSigChanCcTrPriBchStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 3, 2, 2, 1, 1, 4),
    _DataSigChanCcTrPriBchStorageType_Type()
)
dataSigChanCcTrPriBchStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcTrPriBchStorageType.setStatus("mandatory")


class _DataSigChanCcTrPriBchIndex_Type(Integer32):
    """Custom type dataSigChanCcTrPriBchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_DataSigChanCcTrPriBchIndex_Type.__name__ = "Integer32"
_DataSigChanCcTrPriBchIndex_Object = MibTableColumn
dataSigChanCcTrPriBchIndex = _DataSigChanCcTrPriBchIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 3, 2, 2, 1, 1, 10),
    _DataSigChanCcTrPriBchIndex_Type()
)
dataSigChanCcTrPriBchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataSigChanCcTrPriBchIndex.setStatus("mandatory")
_DataSigChanCcBch_ObjectIdentity = ObjectIdentity
dataSigChanCcBch = _DataSigChanCcBch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 4)
)
_DataSigChanCcBchRowStatusTable_Object = MibTable
dataSigChanCcBchRowStatusTable = _DataSigChanCcBchRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 4, 1)
)
if mibBuilder.loadTexts:
    dataSigChanCcBchRowStatusTable.setStatus("mandatory")
_DataSigChanCcBchRowStatusEntry_Object = MibTableRow
dataSigChanCcBchRowStatusEntry = _DataSigChanCcBchRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 4, 1, 1)
)
dataSigChanCcBchRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcBchIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanCcBchRowStatusEntry.setStatus("mandatory")
_DataSigChanCcBchRowStatus_Type = RowStatus
_DataSigChanCcBchRowStatus_Object = MibTableColumn
dataSigChanCcBchRowStatus = _DataSigChanCcBchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 4, 1, 1, 1),
    _DataSigChanCcBchRowStatus_Type()
)
dataSigChanCcBchRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcBchRowStatus.setStatus("mandatory")
_DataSigChanCcBchComponentName_Type = DisplayString
_DataSigChanCcBchComponentName_Object = MibTableColumn
dataSigChanCcBchComponentName = _DataSigChanCcBchComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 4, 1, 1, 2),
    _DataSigChanCcBchComponentName_Type()
)
dataSigChanCcBchComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcBchComponentName.setStatus("mandatory")
_DataSigChanCcBchStorageType_Type = StorageType
_DataSigChanCcBchStorageType_Object = MibTableColumn
dataSigChanCcBchStorageType = _DataSigChanCcBchStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 4, 1, 1, 4),
    _DataSigChanCcBchStorageType_Type()
)
dataSigChanCcBchStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcBchStorageType.setStatus("mandatory")


class _DataSigChanCcBchIndex_Type(Integer32):
    """Custom type dataSigChanCcBchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_DataSigChanCcBchIndex_Type.__name__ = "Integer32"
_DataSigChanCcBchIndex_Object = MibTableColumn
dataSigChanCcBchIndex = _DataSigChanCcBchIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 4, 1, 1, 10),
    _DataSigChanCcBchIndex_Type()
)
dataSigChanCcBchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataSigChanCcBchIndex.setStatus("mandatory")
_DataSigChanCcBchBchanOpDataTable_Object = MibTable
dataSigChanCcBchBchanOpDataTable = _DataSigChanCcBchBchanOpDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 4, 2)
)
if mibBuilder.loadTexts:
    dataSigChanCcBchBchanOpDataTable.setStatus("mandatory")
_DataSigChanCcBchBchanOpDataEntry_Object = MibTableRow
dataSigChanCcBchBchanOpDataEntry = _DataSigChanCcBchBchanOpDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 4, 2, 1)
)
dataSigChanCcBchBchanOpDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcBchIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanCcBchBchanOpDataEntry.setStatus("mandatory")


class _DataSigChanCcBchState_Type(Integer32):
    """Custom type dataSigChanCcBchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("busy", 1),
          ("disabled", 2),
          ("idle", 0),
          ("noProtocolProvisioned", 3))
    )


_DataSigChanCcBchState_Type.__name__ = "Integer32"
_DataSigChanCcBchState_Object = MibTableColumn
dataSigChanCcBchState = _DataSigChanCcBchState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 4, 2, 1, 1),
    _DataSigChanCcBchState_Type()
)
dataSigChanCcBchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcBchState.setStatus("mandatory")


class _DataSigChanCcBchCallingPartyNumber_Type(DigitString):
    """Custom type dataSigChanCcBchCallingPartyNumber based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 14),
    )


_DataSigChanCcBchCallingPartyNumber_Type.__name__ = "DigitString"
_DataSigChanCcBchCallingPartyNumber_Object = MibTableColumn
dataSigChanCcBchCallingPartyNumber = _DataSigChanCcBchCallingPartyNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 4, 2, 1, 2),
    _DataSigChanCcBchCallingPartyNumber_Type()
)
dataSigChanCcBchCallingPartyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcBchCallingPartyNumber.setStatus("mandatory")


class _DataSigChanCcBchLastQ931ClearCause_Type(Integer32):
    """Custom type dataSigChanCcBchLastQ931ClearCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DataSigChanCcBchLastQ931ClearCause_Type.__name__ = "Integer32"
_DataSigChanCcBchLastQ931ClearCause_Object = MibTableColumn
dataSigChanCcBchLastQ931ClearCause = _DataSigChanCcBchLastQ931ClearCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 4, 2, 1, 3),
    _DataSigChanCcBchLastQ931ClearCause_Type()
)
dataSigChanCcBchLastQ931ClearCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcBchLastQ931ClearCause.setStatus("mandatory")


class _DataSigChanCcBchRunningApplication_Type(AsciiString):
    """Custom type dataSigChanCcBchRunningApplication based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DataSigChanCcBchRunningApplication_Type.__name__ = "AsciiString"
_DataSigChanCcBchRunningApplication_Object = MibTableColumn
dataSigChanCcBchRunningApplication = _DataSigChanCcBchRunningApplication_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 4, 2, 1, 4),
    _DataSigChanCcBchRunningApplication_Type()
)
dataSigChanCcBchRunningApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcBchRunningApplication.setStatus("mandatory")
_DataSigChanCcStatsTable_Object = MibTable
dataSigChanCcStatsTable = _DataSigChanCcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 10)
)
if mibBuilder.loadTexts:
    dataSigChanCcStatsTable.setStatus("mandatory")
_DataSigChanCcStatsEntry_Object = MibTableRow
dataSigChanCcStatsEntry = _DataSigChanCcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 10, 1)
)
dataSigChanCcStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanCcIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanCcStatsEntry.setStatus("mandatory")


class _DataSigChanCcTotalValidInCalls_Type(Unsigned32):
    """Custom type dataSigChanCcTotalValidInCalls based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanCcTotalValidInCalls_Type.__name__ = "Unsigned32"
_DataSigChanCcTotalValidInCalls_Object = MibTableColumn
dataSigChanCcTotalValidInCalls = _DataSigChanCcTotalValidInCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 10, 1, 1),
    _DataSigChanCcTotalValidInCalls_Type()
)
dataSigChanCcTotalValidInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcTotalValidInCalls.setStatus("mandatory")


class _DataSigChanCcSuccessfullInCalls_Type(Unsigned32):
    """Custom type dataSigChanCcSuccessfullInCalls based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanCcSuccessfullInCalls_Type.__name__ = "Unsigned32"
_DataSigChanCcSuccessfullInCalls_Object = MibTableColumn
dataSigChanCcSuccessfullInCalls = _DataSigChanCcSuccessfullInCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 10, 1, 2),
    _DataSigChanCcSuccessfullInCalls_Type()
)
dataSigChanCcSuccessfullInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcSuccessfullInCalls.setStatus("mandatory")


class _DataSigChanCcInInvalidCapability_Type(Unsigned32):
    """Custom type dataSigChanCcInInvalidCapability based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanCcInInvalidCapability_Type.__name__ = "Unsigned32"
_DataSigChanCcInInvalidCapability_Object = MibTableColumn
dataSigChanCcInInvalidCapability = _DataSigChanCcInInvalidCapability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 10, 1, 3),
    _DataSigChanCcInInvalidCapability_Type()
)
dataSigChanCcInInvalidCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcInInvalidCapability.setStatus("mandatory")


class _DataSigChanCcInInvalidScreen_Type(Unsigned32):
    """Custom type dataSigChanCcInInvalidScreen based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanCcInInvalidScreen_Type.__name__ = "Unsigned32"
_DataSigChanCcInInvalidScreen_Object = MibTableColumn
dataSigChanCcInInvalidScreen = _DataSigChanCcInInvalidScreen_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 10, 1, 4),
    _DataSigChanCcInInvalidScreen_Type()
)
dataSigChanCcInInvalidScreen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcInInvalidScreen.setStatus("mandatory")


class _DataSigChanCcInInvalidCgpn_Type(Unsigned32):
    """Custom type dataSigChanCcInInvalidCgpn based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanCcInInvalidCgpn_Type.__name__ = "Unsigned32"
_DataSigChanCcInInvalidCgpn_Object = MibTableColumn
dataSigChanCcInInvalidCgpn = _DataSigChanCcInInvalidCgpn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 10, 1, 5),
    _DataSigChanCcInInvalidCgpn_Type()
)
dataSigChanCcInInvalidCgpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcInInvalidCgpn.setStatus("mandatory")


class _DataSigChanCcInChannelBusy_Type(Unsigned32):
    """Custom type dataSigChanCcInChannelBusy based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanCcInChannelBusy_Type.__name__ = "Unsigned32"
_DataSigChanCcInChannelBusy_Object = MibTableColumn
dataSigChanCcInChannelBusy = _DataSigChanCcInChannelBusy_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 10, 1, 6),
    _DataSigChanCcInChannelBusy_Type()
)
dataSigChanCcInChannelBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcInChannelBusy.setStatus("mandatory")


class _DataSigChanCcLastClearCause_Type(Integer32):
    """Custom type dataSigChanCcLastClearCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DataSigChanCcLastClearCause_Type.__name__ = "Integer32"
_DataSigChanCcLastClearCause_Object = MibTableColumn
dataSigChanCcLastClearCause = _DataSigChanCcLastClearCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 10, 1, 7),
    _DataSigChanCcLastClearCause_Type()
)
dataSigChanCcLastClearCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcLastClearCause.setStatus("mandatory")


class _DataSigChanCcLastClearedCallingPartyNumber_Type(DigitString):
    """Custom type dataSigChanCcLastClearedCallingPartyNumber based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 14),
    )


_DataSigChanCcLastClearedCallingPartyNumber_Type.__name__ = "DigitString"
_DataSigChanCcLastClearedCallingPartyNumber_Object = MibTableColumn
dataSigChanCcLastClearedCallingPartyNumber = _DataSigChanCcLastClearedCallingPartyNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 2, 10, 1, 8),
    _DataSigChanCcLastClearedCallingPartyNumber_Type()
)
dataSigChanCcLastClearedCallingPartyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanCcLastClearedCallingPartyNumber.setStatus("mandatory")
_DataSigChanProvTable_Object = MibTable
dataSigChanProvTable = _DataSigChanProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 100)
)
if mibBuilder.loadTexts:
    dataSigChanProvTable.setStatus("mandatory")
_DataSigChanProvEntry_Object = MibTableRow
dataSigChanProvEntry = _DataSigChanProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 100, 1)
)
dataSigChanProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanProvEntry.setStatus("mandatory")


class _DataSigChanCommentText_Type(AsciiString):
    """Custom type dataSigChanCommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_DataSigChanCommentText_Type.__name__ = "AsciiString"
_DataSigChanCommentText_Object = MibTableColumn
dataSigChanCommentText = _DataSigChanCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 100, 1, 1),
    _DataSigChanCommentText_Type()
)
dataSigChanCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanCommentText.setStatus("mandatory")
_DataSigChanCidDataTable_Object = MibTable
dataSigChanCidDataTable = _DataSigChanCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 101)
)
if mibBuilder.loadTexts:
    dataSigChanCidDataTable.setStatus("mandatory")
_DataSigChanCidDataEntry_Object = MibTableRow
dataSigChanCidDataEntry = _DataSigChanCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 101, 1)
)
dataSigChanCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanCidDataEntry.setStatus("mandatory")


class _DataSigChanCustomerIdentifier_Type(Unsigned32):
    """Custom type dataSigChanCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_DataSigChanCustomerIdentifier_Type.__name__ = "Unsigned32"
_DataSigChanCustomerIdentifier_Object = MibTableColumn
dataSigChanCustomerIdentifier = _DataSigChanCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 101, 1, 1),
    _DataSigChanCustomerIdentifier_Type()
)
dataSigChanCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanCustomerIdentifier.setStatus("mandatory")
_DataSigChanIfEntryTable_Object = MibTable
dataSigChanIfEntryTable = _DataSigChanIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 102)
)
if mibBuilder.loadTexts:
    dataSigChanIfEntryTable.setStatus("mandatory")
_DataSigChanIfEntryEntry_Object = MibTableRow
dataSigChanIfEntryEntry = _DataSigChanIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 102, 1)
)
dataSigChanIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanIfEntryEntry.setStatus("mandatory")


class _DataSigChanIfAdminStatus_Type(Integer32):
    """Custom type dataSigChanIfAdminStatus based on Integer32"""
    defaultValue = 1

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


_DataSigChanIfAdminStatus_Type.__name__ = "Integer32"
_DataSigChanIfAdminStatus_Object = MibTableColumn
dataSigChanIfAdminStatus = _DataSigChanIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 102, 1, 1),
    _DataSigChanIfAdminStatus_Type()
)
dataSigChanIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanIfAdminStatus.setStatus("mandatory")


class _DataSigChanIfIndex_Type(InterfaceIndex):
    """Custom type dataSigChanIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DataSigChanIfIndex_Type.__name__ = "InterfaceIndex"
_DataSigChanIfIndex_Object = MibTableColumn
dataSigChanIfIndex = _DataSigChanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 102, 1, 2),
    _DataSigChanIfIndex_Type()
)
dataSigChanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanIfIndex.setStatus("mandatory")
_DataSigChanStateTable_Object = MibTable
dataSigChanStateTable = _DataSigChanStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 103)
)
if mibBuilder.loadTexts:
    dataSigChanStateTable.setStatus("mandatory")
_DataSigChanStateEntry_Object = MibTableRow
dataSigChanStateEntry = _DataSigChanStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 103, 1)
)
dataSigChanStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanStateEntry.setStatus("mandatory")


class _DataSigChanAdminState_Type(Integer32):
    """Custom type dataSigChanAdminState based on Integer32"""
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
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_DataSigChanAdminState_Type.__name__ = "Integer32"
_DataSigChanAdminState_Object = MibTableColumn
dataSigChanAdminState = _DataSigChanAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 103, 1, 1),
    _DataSigChanAdminState_Type()
)
dataSigChanAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanAdminState.setStatus("mandatory")


class _DataSigChanOperationalState_Type(Integer32):
    """Custom type dataSigChanOperationalState based on Integer32"""
    defaultValue = 0

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


_DataSigChanOperationalState_Type.__name__ = "Integer32"
_DataSigChanOperationalState_Object = MibTableColumn
dataSigChanOperationalState = _DataSigChanOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 103, 1, 2),
    _DataSigChanOperationalState_Type()
)
dataSigChanOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanOperationalState.setStatus("mandatory")


class _DataSigChanUsageState_Type(Integer32):
    """Custom type dataSigChanUsageState based on Integer32"""
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
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_DataSigChanUsageState_Type.__name__ = "Integer32"
_DataSigChanUsageState_Object = MibTableColumn
dataSigChanUsageState = _DataSigChanUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 103, 1, 3),
    _DataSigChanUsageState_Type()
)
dataSigChanUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanUsageState.setStatus("mandatory")
_DataSigChanOperStatusTable_Object = MibTable
dataSigChanOperStatusTable = _DataSigChanOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 104)
)
if mibBuilder.loadTexts:
    dataSigChanOperStatusTable.setStatus("mandatory")
_DataSigChanOperStatusEntry_Object = MibTableRow
dataSigChanOperStatusEntry = _DataSigChanOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 104, 1)
)
dataSigChanOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanOperStatusEntry.setStatus("mandatory")


class _DataSigChanSnmpOperStatus_Type(Integer32):
    """Custom type dataSigChanSnmpOperStatus based on Integer32"""
    defaultValue = 1

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


_DataSigChanSnmpOperStatus_Type.__name__ = "Integer32"
_DataSigChanSnmpOperStatus_Object = MibTableColumn
dataSigChanSnmpOperStatus = _DataSigChanSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 104, 1, 1),
    _DataSigChanSnmpOperStatus_Type()
)
dataSigChanSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanSnmpOperStatus.setStatus("mandatory")
_DataIsdnMIB_ObjectIdentity = ObjectIdentity
dataIsdnMIB = _DataIsdnMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 113)
)
_DataIsdnGroup_ObjectIdentity = ObjectIdentity
dataIsdnGroup = _DataIsdnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 113, 1)
)
_DataIsdnGroupBD_ObjectIdentity = ObjectIdentity
dataIsdnGroupBD = _DataIsdnGroupBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 113, 1, 4)
)
_DataIsdnGroupBD01_ObjectIdentity = ObjectIdentity
dataIsdnGroupBD01 = _DataIsdnGroupBD01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 113, 1, 4, 2)
)
_DataIsdnGroupBD01A_ObjectIdentity = ObjectIdentity
dataIsdnGroupBD01A = _DataIsdnGroupBD01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 113, 1, 4, 2, 2)
)
_DataIsdnCapabilities_ObjectIdentity = ObjectIdentity
dataIsdnCapabilities = _DataIsdnCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 113, 3)
)
_DataIsdnCapabilitiesBD_ObjectIdentity = ObjectIdentity
dataIsdnCapabilitiesBD = _DataIsdnCapabilitiesBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 113, 3, 4)
)
_DataIsdnCapabilitiesBD01_ObjectIdentity = ObjectIdentity
dataIsdnCapabilitiesBD01 = _DataIsdnCapabilitiesBD01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 113, 3, 4, 2)
)
_DataIsdnCapabilitiesBD01A_ObjectIdentity = ObjectIdentity
dataIsdnCapabilitiesBD01A = _DataIsdnCapabilitiesBD01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 113, 3, 4, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-DataIsdnMIB",
    **{"dataSigChan": dataSigChan,
       "dataSigChanRowStatusTable": dataSigChanRowStatusTable,
       "dataSigChanRowStatusEntry": dataSigChanRowStatusEntry,
       "dataSigChanRowStatus": dataSigChanRowStatus,
       "dataSigChanComponentName": dataSigChanComponentName,
       "dataSigChanStorageType": dataSigChanStorageType,
       "dataSigChanIndex": dataSigChanIndex,
       "dataSigChanCc": dataSigChanCc,
       "dataSigChanCcRowStatusTable": dataSigChanCcRowStatusTable,
       "dataSigChanCcRowStatusEntry": dataSigChanCcRowStatusEntry,
       "dataSigChanCcRowStatus": dataSigChanCcRowStatus,
       "dataSigChanCcComponentName": dataSigChanCcComponentName,
       "dataSigChanCcStorageType": dataSigChanCcStorageType,
       "dataSigChanCcIndex": dataSigChanCcIndex,
       "dataSigChanCcCg": dataSigChanCcCg,
       "dataSigChanCcCgRowStatusTable": dataSigChanCcCgRowStatusTable,
       "dataSigChanCcCgRowStatusEntry": dataSigChanCcCgRowStatusEntry,
       "dataSigChanCcCgRowStatus": dataSigChanCcCgRowStatus,
       "dataSigChanCcCgComponentName": dataSigChanCcCgComponentName,
       "dataSigChanCcCgStorageType": dataSigChanCcCgStorageType,
       "dataSigChanCcCgIndex": dataSigChanCcCgIndex,
       "dataSigChanCcCgCgpn": dataSigChanCcCgCgpn,
       "dataSigChanCcCgCgpnRowStatusTable": dataSigChanCcCgCgpnRowStatusTable,
       "dataSigChanCcCgCgpnRowStatusEntry": dataSigChanCcCgCgpnRowStatusEntry,
       "dataSigChanCcCgCgpnRowStatus": dataSigChanCcCgCgpnRowStatus,
       "dataSigChanCcCgCgpnComponentName": dataSigChanCcCgCgpnComponentName,
       "dataSigChanCcCgCgpnStorageType": dataSigChanCcCgCgpnStorageType,
       "dataSigChanCcCgCgpnIndex": dataSigChanCcCgCgpnIndex,
       "dataSigChanCcCgBch": dataSigChanCcCgBch,
       "dataSigChanCcCgBchRowStatusTable": dataSigChanCcCgBchRowStatusTable,
       "dataSigChanCcCgBchRowStatusEntry": dataSigChanCcCgBchRowStatusEntry,
       "dataSigChanCcCgBchRowStatus": dataSigChanCcCgBchRowStatus,
       "dataSigChanCcCgBchComponentName": dataSigChanCcCgBchComponentName,
       "dataSigChanCcCgBchStorageType": dataSigChanCcCgBchStorageType,
       "dataSigChanCcCgBchIndex": dataSigChanCcCgBchIndex,
       "dataSigChanCcCgBchBchanOpDataTable": dataSigChanCcCgBchBchanOpDataTable,
       "dataSigChanCcCgBchBchanOpDataEntry": dataSigChanCcCgBchBchanOpDataEntry,
       "dataSigChanCcCgBchState": dataSigChanCcCgBchState,
       "dataSigChanCcCgBchCallingPartyNumber": dataSigChanCcCgBchCallingPartyNumber,
       "dataSigChanCcCgBchLastQ931ClearCause": dataSigChanCcCgBchLastQ931ClearCause,
       "dataSigChanCcCgBchRunningApplication": dataSigChanCcCgBchRunningApplication,
       "dataSigChanCcCgCidDataTable": dataSigChanCcCgCidDataTable,
       "dataSigChanCcCgCidDataEntry": dataSigChanCcCgCidDataEntry,
       "dataSigChanCcCgCustomerIdentifier": dataSigChanCcCgCustomerIdentifier,
       "dataSigChanCcCgProvTable": dataSigChanCcCgProvTable,
       "dataSigChanCcCgProvEntry": dataSigChanCcCgProvEntry,
       "dataSigChanCcCgCommentText": dataSigChanCcCgCommentText,
       "dataSigChanCcCgScreeningIndicator": dataSigChanCcCgScreeningIndicator,
       "dataSigChanCcCgChannelAssignmentOrder": dataSigChanCcCgChannelAssignmentOrder,
       "dataSigChanCcCgChannelList": dataSigChanCcCgChannelList,
       "dataSigChanCcCgStatsTable": dataSigChanCcCgStatsTable,
       "dataSigChanCcCgStatsEntry": dataSigChanCcCgStatsEntry,
       "dataSigChanCcCgTotalInCalls": dataSigChanCcCgTotalInCalls,
       "dataSigChanCcCgSuccessfullInCalls": dataSigChanCcCgSuccessfullInCalls,
       "dataSigChanCcCgRejectedNoChanAvail": dataSigChanCcCgRejectedNoChanAvail,
       "dataSigChanCcCgIdleChannelCount": dataSigChanCcCgIdleChannelCount,
       "dataSigChanCcCgBusyChannelCount": dataSigChanCcCgBusyChannelCount,
       "dataSigChanCcTr": dataSigChanCcTr,
       "dataSigChanCcTrRowStatusTable": dataSigChanCcTrRowStatusTable,
       "dataSigChanCcTrRowStatusEntry": dataSigChanCcTrRowStatusEntry,
       "dataSigChanCcTrRowStatus": dataSigChanCcTrRowStatus,
       "dataSigChanCcTrComponentName": dataSigChanCcTrComponentName,
       "dataSigChanCcTrStorageType": dataSigChanCcTrStorageType,
       "dataSigChanCcTrIndex": dataSigChanCcTrIndex,
       "dataSigChanCcTrPri": dataSigChanCcTrPri,
       "dataSigChanCcTrPriRowStatusTable": dataSigChanCcTrPriRowStatusTable,
       "dataSigChanCcTrPriRowStatusEntry": dataSigChanCcTrPriRowStatusEntry,
       "dataSigChanCcTrPriRowStatus": dataSigChanCcTrPriRowStatus,
       "dataSigChanCcTrPriComponentName": dataSigChanCcTrPriComponentName,
       "dataSigChanCcTrPriStorageType": dataSigChanCcTrPriStorageType,
       "dataSigChanCcTrPriIndex": dataSigChanCcTrPriIndex,
       "dataSigChanCcTrPriBch": dataSigChanCcTrPriBch,
       "dataSigChanCcTrPriBchRowStatusTable": dataSigChanCcTrPriBchRowStatusTable,
       "dataSigChanCcTrPriBchRowStatusEntry": dataSigChanCcTrPriBchRowStatusEntry,
       "dataSigChanCcTrPriBchRowStatus": dataSigChanCcTrPriBchRowStatus,
       "dataSigChanCcTrPriBchComponentName": dataSigChanCcTrPriBchComponentName,
       "dataSigChanCcTrPriBchStorageType": dataSigChanCcTrPriBchStorageType,
       "dataSigChanCcTrPriBchIndex": dataSigChanCcTrPriBchIndex,
       "dataSigChanCcBch": dataSigChanCcBch,
       "dataSigChanCcBchRowStatusTable": dataSigChanCcBchRowStatusTable,
       "dataSigChanCcBchRowStatusEntry": dataSigChanCcBchRowStatusEntry,
       "dataSigChanCcBchRowStatus": dataSigChanCcBchRowStatus,
       "dataSigChanCcBchComponentName": dataSigChanCcBchComponentName,
       "dataSigChanCcBchStorageType": dataSigChanCcBchStorageType,
       "dataSigChanCcBchIndex": dataSigChanCcBchIndex,
       "dataSigChanCcBchBchanOpDataTable": dataSigChanCcBchBchanOpDataTable,
       "dataSigChanCcBchBchanOpDataEntry": dataSigChanCcBchBchanOpDataEntry,
       "dataSigChanCcBchState": dataSigChanCcBchState,
       "dataSigChanCcBchCallingPartyNumber": dataSigChanCcBchCallingPartyNumber,
       "dataSigChanCcBchLastQ931ClearCause": dataSigChanCcBchLastQ931ClearCause,
       "dataSigChanCcBchRunningApplication": dataSigChanCcBchRunningApplication,
       "dataSigChanCcStatsTable": dataSigChanCcStatsTable,
       "dataSigChanCcStatsEntry": dataSigChanCcStatsEntry,
       "dataSigChanCcTotalValidInCalls": dataSigChanCcTotalValidInCalls,
       "dataSigChanCcSuccessfullInCalls": dataSigChanCcSuccessfullInCalls,
       "dataSigChanCcInInvalidCapability": dataSigChanCcInInvalidCapability,
       "dataSigChanCcInInvalidScreen": dataSigChanCcInInvalidScreen,
       "dataSigChanCcInInvalidCgpn": dataSigChanCcInInvalidCgpn,
       "dataSigChanCcInChannelBusy": dataSigChanCcInChannelBusy,
       "dataSigChanCcLastClearCause": dataSigChanCcLastClearCause,
       "dataSigChanCcLastClearedCallingPartyNumber": dataSigChanCcLastClearedCallingPartyNumber,
       "dataSigChanProvTable": dataSigChanProvTable,
       "dataSigChanProvEntry": dataSigChanProvEntry,
       "dataSigChanCommentText": dataSigChanCommentText,
       "dataSigChanCidDataTable": dataSigChanCidDataTable,
       "dataSigChanCidDataEntry": dataSigChanCidDataEntry,
       "dataSigChanCustomerIdentifier": dataSigChanCustomerIdentifier,
       "dataSigChanIfEntryTable": dataSigChanIfEntryTable,
       "dataSigChanIfEntryEntry": dataSigChanIfEntryEntry,
       "dataSigChanIfAdminStatus": dataSigChanIfAdminStatus,
       "dataSigChanIfIndex": dataSigChanIfIndex,
       "dataSigChanStateTable": dataSigChanStateTable,
       "dataSigChanStateEntry": dataSigChanStateEntry,
       "dataSigChanAdminState": dataSigChanAdminState,
       "dataSigChanOperationalState": dataSigChanOperationalState,
       "dataSigChanUsageState": dataSigChanUsageState,
       "dataSigChanOperStatusTable": dataSigChanOperStatusTable,
       "dataSigChanOperStatusEntry": dataSigChanOperStatusEntry,
       "dataSigChanSnmpOperStatus": dataSigChanSnmpOperStatus,
       "dataIsdnMIB": dataIsdnMIB,
       "dataIsdnGroup": dataIsdnGroup,
       "dataIsdnGroupBD": dataIsdnGroupBD,
       "dataIsdnGroupBD01": dataIsdnGroupBD01,
       "dataIsdnGroupBD01A": dataIsdnGroupBD01A,
       "dataIsdnCapabilities": dataIsdnCapabilities,
       "dataIsdnCapabilitiesBD": dataIsdnCapabilitiesBD,
       "dataIsdnCapabilitiesBD01": dataIsdnCapabilitiesBD01,
       "dataIsdnCapabilitiesBD01A": dataIsdnCapabilitiesBD01A}
)
