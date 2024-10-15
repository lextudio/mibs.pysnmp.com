# SNMP MIB module (Nortel-MsCarrier-MscPassport-DataIsdnMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-DataIsdnMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:09 2024
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
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "DisplayString",
    "Integer32",
    "InterfaceIndex",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 DigitString,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "DigitString",
    "NonReplicated")

(mscComponents,
 mscPassportMIBs) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscComponents",
    "mscPassportMIBs")

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

_MscDataSigChan_ObjectIdentity = ObjectIdentity
mscDataSigChan = _MscDataSigChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120)
)
_MscDataSigChanRowStatusTable_Object = MibTable
mscDataSigChanRowStatusTable = _MscDataSigChanRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 1)
)
if mibBuilder.loadTexts:
    mscDataSigChanRowStatusTable.setStatus("mandatory")
_MscDataSigChanRowStatusEntry_Object = MibTableRow
mscDataSigChanRowStatusEntry = _MscDataSigChanRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 1, 1)
)
mscDataSigChanRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanRowStatusEntry.setStatus("mandatory")
_MscDataSigChanRowStatus_Type = RowStatus
_MscDataSigChanRowStatus_Object = MibTableColumn
mscDataSigChanRowStatus = _MscDataSigChanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 1, 1, 1),
    _MscDataSigChanRowStatus_Type()
)
mscDataSigChanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanRowStatus.setStatus("mandatory")
_MscDataSigChanComponentName_Type = DisplayString
_MscDataSigChanComponentName_Object = MibTableColumn
mscDataSigChanComponentName = _MscDataSigChanComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 1, 1, 2),
    _MscDataSigChanComponentName_Type()
)
mscDataSigChanComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanComponentName.setStatus("mandatory")
_MscDataSigChanStorageType_Type = StorageType
_MscDataSigChanStorageType_Object = MibTableColumn
mscDataSigChanStorageType = _MscDataSigChanStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 1, 1, 4),
    _MscDataSigChanStorageType_Type()
)
mscDataSigChanStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanStorageType.setStatus("mandatory")


class _MscDataSigChanIndex_Type(Integer32):
    """Custom type mscDataSigChanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscDataSigChanIndex_Type.__name__ = "Integer32"
_MscDataSigChanIndex_Object = MibTableColumn
mscDataSigChanIndex = _MscDataSigChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 1, 1, 10),
    _MscDataSigChanIndex_Type()
)
mscDataSigChanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDataSigChanIndex.setStatus("mandatory")
_MscDataSigChanCc_ObjectIdentity = ObjectIdentity
mscDataSigChanCc = _MscDataSigChanCc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2)
)
_MscDataSigChanCcRowStatusTable_Object = MibTable
mscDataSigChanCcRowStatusTable = _MscDataSigChanCcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 1)
)
if mibBuilder.loadTexts:
    mscDataSigChanCcRowStatusTable.setStatus("mandatory")
_MscDataSigChanCcRowStatusEntry_Object = MibTableRow
mscDataSigChanCcRowStatusEntry = _MscDataSigChanCcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 1, 1)
)
mscDataSigChanCcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanCcRowStatusEntry.setStatus("mandatory")
_MscDataSigChanCcRowStatus_Type = RowStatus
_MscDataSigChanCcRowStatus_Object = MibTableColumn
mscDataSigChanCcRowStatus = _MscDataSigChanCcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 1, 1, 1),
    _MscDataSigChanCcRowStatus_Type()
)
mscDataSigChanCcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcRowStatus.setStatus("mandatory")
_MscDataSigChanCcComponentName_Type = DisplayString
_MscDataSigChanCcComponentName_Object = MibTableColumn
mscDataSigChanCcComponentName = _MscDataSigChanCcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 1, 1, 2),
    _MscDataSigChanCcComponentName_Type()
)
mscDataSigChanCcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcComponentName.setStatus("mandatory")
_MscDataSigChanCcStorageType_Type = StorageType
_MscDataSigChanCcStorageType_Object = MibTableColumn
mscDataSigChanCcStorageType = _MscDataSigChanCcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 1, 1, 4),
    _MscDataSigChanCcStorageType_Type()
)
mscDataSigChanCcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcStorageType.setStatus("mandatory")
_MscDataSigChanCcIndex_Type = NonReplicated
_MscDataSigChanCcIndex_Object = MibTableColumn
mscDataSigChanCcIndex = _MscDataSigChanCcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 1, 1, 10),
    _MscDataSigChanCcIndex_Type()
)
mscDataSigChanCcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDataSigChanCcIndex.setStatus("mandatory")
_MscDataSigChanCcCg_ObjectIdentity = ObjectIdentity
mscDataSigChanCcCg = _MscDataSigChanCcCg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2)
)
_MscDataSigChanCcCgRowStatusTable_Object = MibTable
mscDataSigChanCcCgRowStatusTable = _MscDataSigChanCcCgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscDataSigChanCcCgRowStatusTable.setStatus("mandatory")
_MscDataSigChanCcCgRowStatusEntry_Object = MibTableRow
mscDataSigChanCcCgRowStatusEntry = _MscDataSigChanCcCgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 1, 1)
)
mscDataSigChanCcCgRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcCgIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanCcCgRowStatusEntry.setStatus("mandatory")
_MscDataSigChanCcCgRowStatus_Type = RowStatus
_MscDataSigChanCcCgRowStatus_Object = MibTableColumn
mscDataSigChanCcCgRowStatus = _MscDataSigChanCcCgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 1, 1, 1),
    _MscDataSigChanCcCgRowStatus_Type()
)
mscDataSigChanCcCgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanCcCgRowStatus.setStatus("mandatory")
_MscDataSigChanCcCgComponentName_Type = DisplayString
_MscDataSigChanCcCgComponentName_Object = MibTableColumn
mscDataSigChanCcCgComponentName = _MscDataSigChanCcCgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 1, 1, 2),
    _MscDataSigChanCcCgComponentName_Type()
)
mscDataSigChanCcCgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcCgComponentName.setStatus("mandatory")
_MscDataSigChanCcCgStorageType_Type = StorageType
_MscDataSigChanCcCgStorageType_Object = MibTableColumn
mscDataSigChanCcCgStorageType = _MscDataSigChanCcCgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 1, 1, 4),
    _MscDataSigChanCcCgStorageType_Type()
)
mscDataSigChanCcCgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcCgStorageType.setStatus("mandatory")


class _MscDataSigChanCcCgIndex_Type(Integer32):
    """Custom type mscDataSigChanCcCgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_MscDataSigChanCcCgIndex_Type.__name__ = "Integer32"
_MscDataSigChanCcCgIndex_Object = MibTableColumn
mscDataSigChanCcCgIndex = _MscDataSigChanCcCgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 1, 1, 10),
    _MscDataSigChanCcCgIndex_Type()
)
mscDataSigChanCcCgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDataSigChanCcCgIndex.setStatus("mandatory")
_MscDataSigChanCcCgCgpn_ObjectIdentity = ObjectIdentity
mscDataSigChanCcCgCgpn = _MscDataSigChanCcCgCgpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 2)
)
_MscDataSigChanCcCgCgpnRowStatusTable_Object = MibTable
mscDataSigChanCcCgCgpnRowStatusTable = _MscDataSigChanCcCgCgpnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscDataSigChanCcCgCgpnRowStatusTable.setStatus("mandatory")
_MscDataSigChanCcCgCgpnRowStatusEntry_Object = MibTableRow
mscDataSigChanCcCgCgpnRowStatusEntry = _MscDataSigChanCcCgCgpnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 2, 1, 1)
)
mscDataSigChanCcCgCgpnRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcCgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcCgCgpnIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanCcCgCgpnRowStatusEntry.setStatus("mandatory")
_MscDataSigChanCcCgCgpnRowStatus_Type = RowStatus
_MscDataSigChanCcCgCgpnRowStatus_Object = MibTableColumn
mscDataSigChanCcCgCgpnRowStatus = _MscDataSigChanCcCgCgpnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 2, 1, 1, 1),
    _MscDataSigChanCcCgCgpnRowStatus_Type()
)
mscDataSigChanCcCgCgpnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanCcCgCgpnRowStatus.setStatus("mandatory")
_MscDataSigChanCcCgCgpnComponentName_Type = DisplayString
_MscDataSigChanCcCgCgpnComponentName_Object = MibTableColumn
mscDataSigChanCcCgCgpnComponentName = _MscDataSigChanCcCgCgpnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 2, 1, 1, 2),
    _MscDataSigChanCcCgCgpnComponentName_Type()
)
mscDataSigChanCcCgCgpnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcCgCgpnComponentName.setStatus("mandatory")
_MscDataSigChanCcCgCgpnStorageType_Type = StorageType
_MscDataSigChanCcCgCgpnStorageType_Object = MibTableColumn
mscDataSigChanCcCgCgpnStorageType = _MscDataSigChanCcCgCgpnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 2, 1, 1, 4),
    _MscDataSigChanCcCgCgpnStorageType_Type()
)
mscDataSigChanCcCgCgpnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcCgCgpnStorageType.setStatus("mandatory")


class _MscDataSigChanCcCgCgpnIndex_Type(DigitString):
    """Custom type mscDataSigChanCcCgCgpnIndex based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 14),
    )


_MscDataSigChanCcCgCgpnIndex_Type.__name__ = "DigitString"
_MscDataSigChanCcCgCgpnIndex_Object = MibTableColumn
mscDataSigChanCcCgCgpnIndex = _MscDataSigChanCcCgCgpnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 2, 1, 1, 10),
    _MscDataSigChanCcCgCgpnIndex_Type()
)
mscDataSigChanCcCgCgpnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDataSigChanCcCgCgpnIndex.setStatus("mandatory")
_MscDataSigChanCcCgBch_ObjectIdentity = ObjectIdentity
mscDataSigChanCcCgBch = _MscDataSigChanCcCgBch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 3)
)
_MscDataSigChanCcCgBchRowStatusTable_Object = MibTable
mscDataSigChanCcCgBchRowStatusTable = _MscDataSigChanCcCgBchRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mscDataSigChanCcCgBchRowStatusTable.setStatus("mandatory")
_MscDataSigChanCcCgBchRowStatusEntry_Object = MibTableRow
mscDataSigChanCcCgBchRowStatusEntry = _MscDataSigChanCcCgBchRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 3, 1, 1)
)
mscDataSigChanCcCgBchRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcCgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcCgBchIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanCcCgBchRowStatusEntry.setStatus("mandatory")
_MscDataSigChanCcCgBchRowStatus_Type = RowStatus
_MscDataSigChanCcCgBchRowStatus_Object = MibTableColumn
mscDataSigChanCcCgBchRowStatus = _MscDataSigChanCcCgBchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 3, 1, 1, 1),
    _MscDataSigChanCcCgBchRowStatus_Type()
)
mscDataSigChanCcCgBchRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcCgBchRowStatus.setStatus("mandatory")
_MscDataSigChanCcCgBchComponentName_Type = DisplayString
_MscDataSigChanCcCgBchComponentName_Object = MibTableColumn
mscDataSigChanCcCgBchComponentName = _MscDataSigChanCcCgBchComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 3, 1, 1, 2),
    _MscDataSigChanCcCgBchComponentName_Type()
)
mscDataSigChanCcCgBchComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcCgBchComponentName.setStatus("mandatory")
_MscDataSigChanCcCgBchStorageType_Type = StorageType
_MscDataSigChanCcCgBchStorageType_Object = MibTableColumn
mscDataSigChanCcCgBchStorageType = _MscDataSigChanCcCgBchStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 3, 1, 1, 4),
    _MscDataSigChanCcCgBchStorageType_Type()
)
mscDataSigChanCcCgBchStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcCgBchStorageType.setStatus("mandatory")


class _MscDataSigChanCcCgBchIndex_Type(Integer32):
    """Custom type mscDataSigChanCcCgBchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_MscDataSigChanCcCgBchIndex_Type.__name__ = "Integer32"
_MscDataSigChanCcCgBchIndex_Object = MibTableColumn
mscDataSigChanCcCgBchIndex = _MscDataSigChanCcCgBchIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 3, 1, 1, 10),
    _MscDataSigChanCcCgBchIndex_Type()
)
mscDataSigChanCcCgBchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDataSigChanCcCgBchIndex.setStatus("mandatory")
_MscDataSigChanCcCgBchBchanOpDataTable_Object = MibTable
mscDataSigChanCcCgBchBchanOpDataTable = _MscDataSigChanCcCgBchBchanOpDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    mscDataSigChanCcCgBchBchanOpDataTable.setStatus("mandatory")
_MscDataSigChanCcCgBchBchanOpDataEntry_Object = MibTableRow
mscDataSigChanCcCgBchBchanOpDataEntry = _MscDataSigChanCcCgBchBchanOpDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 3, 2, 1)
)
mscDataSigChanCcCgBchBchanOpDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcCgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcCgBchIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanCcCgBchBchanOpDataEntry.setStatus("mandatory")


class _MscDataSigChanCcCgBchState_Type(Integer32):
    """Custom type mscDataSigChanCcCgBchState based on Integer32"""
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


_MscDataSigChanCcCgBchState_Type.__name__ = "Integer32"
_MscDataSigChanCcCgBchState_Object = MibTableColumn
mscDataSigChanCcCgBchState = _MscDataSigChanCcCgBchState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 3, 2, 1, 1),
    _MscDataSigChanCcCgBchState_Type()
)
mscDataSigChanCcCgBchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcCgBchState.setStatus("mandatory")


class _MscDataSigChanCcCgBchCallingPartyNumber_Type(DigitString):
    """Custom type mscDataSigChanCcCgBchCallingPartyNumber based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 14),
    )


_MscDataSigChanCcCgBchCallingPartyNumber_Type.__name__ = "DigitString"
_MscDataSigChanCcCgBchCallingPartyNumber_Object = MibTableColumn
mscDataSigChanCcCgBchCallingPartyNumber = _MscDataSigChanCcCgBchCallingPartyNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 3, 2, 1, 2),
    _MscDataSigChanCcCgBchCallingPartyNumber_Type()
)
mscDataSigChanCcCgBchCallingPartyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcCgBchCallingPartyNumber.setStatus("mandatory")


class _MscDataSigChanCcCgBchLastQ931ClearCause_Type(Integer32):
    """Custom type mscDataSigChanCcCgBchLastQ931ClearCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscDataSigChanCcCgBchLastQ931ClearCause_Type.__name__ = "Integer32"
_MscDataSigChanCcCgBchLastQ931ClearCause_Object = MibTableColumn
mscDataSigChanCcCgBchLastQ931ClearCause = _MscDataSigChanCcCgBchLastQ931ClearCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 3, 2, 1, 3),
    _MscDataSigChanCcCgBchLastQ931ClearCause_Type()
)
mscDataSigChanCcCgBchLastQ931ClearCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcCgBchLastQ931ClearCause.setStatus("mandatory")


class _MscDataSigChanCcCgBchRunningApplication_Type(AsciiString):
    """Custom type mscDataSigChanCcCgBchRunningApplication based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MscDataSigChanCcCgBchRunningApplication_Type.__name__ = "AsciiString"
_MscDataSigChanCcCgBchRunningApplication_Object = MibTableColumn
mscDataSigChanCcCgBchRunningApplication = _MscDataSigChanCcCgBchRunningApplication_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 3, 2, 1, 4),
    _MscDataSigChanCcCgBchRunningApplication_Type()
)
mscDataSigChanCcCgBchRunningApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcCgBchRunningApplication.setStatus("mandatory")
_MscDataSigChanCcCgCidDataTable_Object = MibTable
mscDataSigChanCcCgCidDataTable = _MscDataSigChanCcCgCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscDataSigChanCcCgCidDataTable.setStatus("mandatory")
_MscDataSigChanCcCgCidDataEntry_Object = MibTableRow
mscDataSigChanCcCgCidDataEntry = _MscDataSigChanCcCgCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 10, 1)
)
mscDataSigChanCcCgCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcCgIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanCcCgCidDataEntry.setStatus("mandatory")


class _MscDataSigChanCcCgCustomerIdentifier_Type(Unsigned32):
    """Custom type mscDataSigChanCcCgCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscDataSigChanCcCgCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscDataSigChanCcCgCustomerIdentifier_Object = MibTableColumn
mscDataSigChanCcCgCustomerIdentifier = _MscDataSigChanCcCgCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 10, 1, 1),
    _MscDataSigChanCcCgCustomerIdentifier_Type()
)
mscDataSigChanCcCgCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanCcCgCustomerIdentifier.setStatus("mandatory")
_MscDataSigChanCcCgProvTable_Object = MibTable
mscDataSigChanCcCgProvTable = _MscDataSigChanCcCgProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 11)
)
if mibBuilder.loadTexts:
    mscDataSigChanCcCgProvTable.setStatus("mandatory")
_MscDataSigChanCcCgProvEntry_Object = MibTableRow
mscDataSigChanCcCgProvEntry = _MscDataSigChanCcCgProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 11, 1)
)
mscDataSigChanCcCgProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcCgIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanCcCgProvEntry.setStatus("mandatory")


class _MscDataSigChanCcCgCommentText_Type(AsciiString):
    """Custom type mscDataSigChanCcCgCommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscDataSigChanCcCgCommentText_Type.__name__ = "AsciiString"
_MscDataSigChanCcCgCommentText_Object = MibTableColumn
mscDataSigChanCcCgCommentText = _MscDataSigChanCcCgCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 11, 1, 1),
    _MscDataSigChanCcCgCommentText_Type()
)
mscDataSigChanCcCgCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanCcCgCommentText.setStatus("mandatory")


class _MscDataSigChanCcCgScreeningIndicator_Type(OctetString):
    """Custom type mscDataSigChanCcCgScreeningIndicator based on OctetString"""
    defaultHexValue = "50"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscDataSigChanCcCgScreeningIndicator_Type.__name__ = "OctetString"
_MscDataSigChanCcCgScreeningIndicator_Object = MibTableColumn
mscDataSigChanCcCgScreeningIndicator = _MscDataSigChanCcCgScreeningIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 11, 1, 2),
    _MscDataSigChanCcCgScreeningIndicator_Type()
)
mscDataSigChanCcCgScreeningIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanCcCgScreeningIndicator.setStatus("mandatory")


class _MscDataSigChanCcCgChannelAssignmentOrder_Type(Integer32):
    """Custom type mscDataSigChanCcCgChannelAssignmentOrder based on Integer32"""
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


_MscDataSigChanCcCgChannelAssignmentOrder_Type.__name__ = "Integer32"
_MscDataSigChanCcCgChannelAssignmentOrder_Object = MibTableColumn
mscDataSigChanCcCgChannelAssignmentOrder = _MscDataSigChanCcCgChannelAssignmentOrder_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 11, 1, 3),
    _MscDataSigChanCcCgChannelAssignmentOrder_Type()
)
mscDataSigChanCcCgChannelAssignmentOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanCcCgChannelAssignmentOrder.setStatus("mandatory")


class _MscDataSigChanCcCgChannelList_Type(OctetString):
    """Custom type mscDataSigChanCcCgChannelList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_MscDataSigChanCcCgChannelList_Type.__name__ = "OctetString"
_MscDataSigChanCcCgChannelList_Object = MibTableColumn
mscDataSigChanCcCgChannelList = _MscDataSigChanCcCgChannelList_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 11, 1, 4),
    _MscDataSigChanCcCgChannelList_Type()
)
mscDataSigChanCcCgChannelList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanCcCgChannelList.setStatus("mandatory")
_MscDataSigChanCcCgStatsTable_Object = MibTable
mscDataSigChanCcCgStatsTable = _MscDataSigChanCcCgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 12)
)
if mibBuilder.loadTexts:
    mscDataSigChanCcCgStatsTable.setStatus("mandatory")
_MscDataSigChanCcCgStatsEntry_Object = MibTableRow
mscDataSigChanCcCgStatsEntry = _MscDataSigChanCcCgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 12, 1)
)
mscDataSigChanCcCgStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcCgIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanCcCgStatsEntry.setStatus("mandatory")


class _MscDataSigChanCcCgTotalInCalls_Type(Unsigned32):
    """Custom type mscDataSigChanCcCgTotalInCalls based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanCcCgTotalInCalls_Type.__name__ = "Unsigned32"
_MscDataSigChanCcCgTotalInCalls_Object = MibTableColumn
mscDataSigChanCcCgTotalInCalls = _MscDataSigChanCcCgTotalInCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 12, 1, 1),
    _MscDataSigChanCcCgTotalInCalls_Type()
)
mscDataSigChanCcCgTotalInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcCgTotalInCalls.setStatus("mandatory")


class _MscDataSigChanCcCgSuccessfullInCalls_Type(Unsigned32):
    """Custom type mscDataSigChanCcCgSuccessfullInCalls based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanCcCgSuccessfullInCalls_Type.__name__ = "Unsigned32"
_MscDataSigChanCcCgSuccessfullInCalls_Object = MibTableColumn
mscDataSigChanCcCgSuccessfullInCalls = _MscDataSigChanCcCgSuccessfullInCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 12, 1, 2),
    _MscDataSigChanCcCgSuccessfullInCalls_Type()
)
mscDataSigChanCcCgSuccessfullInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcCgSuccessfullInCalls.setStatus("mandatory")


class _MscDataSigChanCcCgRejectedNoChanAvail_Type(Unsigned32):
    """Custom type mscDataSigChanCcCgRejectedNoChanAvail based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanCcCgRejectedNoChanAvail_Type.__name__ = "Unsigned32"
_MscDataSigChanCcCgRejectedNoChanAvail_Object = MibTableColumn
mscDataSigChanCcCgRejectedNoChanAvail = _MscDataSigChanCcCgRejectedNoChanAvail_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 12, 1, 3),
    _MscDataSigChanCcCgRejectedNoChanAvail_Type()
)
mscDataSigChanCcCgRejectedNoChanAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcCgRejectedNoChanAvail.setStatus("mandatory")


class _MscDataSigChanCcCgIdleChannelCount_Type(Integer32):
    """Custom type mscDataSigChanCcCgIdleChannelCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscDataSigChanCcCgIdleChannelCount_Type.__name__ = "Integer32"
_MscDataSigChanCcCgIdleChannelCount_Object = MibTableColumn
mscDataSigChanCcCgIdleChannelCount = _MscDataSigChanCcCgIdleChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 12, 1, 4),
    _MscDataSigChanCcCgIdleChannelCount_Type()
)
mscDataSigChanCcCgIdleChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcCgIdleChannelCount.setStatus("mandatory")


class _MscDataSigChanCcCgBusyChannelCount_Type(Integer32):
    """Custom type mscDataSigChanCcCgBusyChannelCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscDataSigChanCcCgBusyChannelCount_Type.__name__ = "Integer32"
_MscDataSigChanCcCgBusyChannelCount_Object = MibTableColumn
mscDataSigChanCcCgBusyChannelCount = _MscDataSigChanCcCgBusyChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 2, 12, 1, 5),
    _MscDataSigChanCcCgBusyChannelCount_Type()
)
mscDataSigChanCcCgBusyChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcCgBusyChannelCount.setStatus("mandatory")
_MscDataSigChanCcTr_ObjectIdentity = ObjectIdentity
mscDataSigChanCcTr = _MscDataSigChanCcTr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 3)
)
_MscDataSigChanCcTrRowStatusTable_Object = MibTable
mscDataSigChanCcTrRowStatusTable = _MscDataSigChanCcTrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mscDataSigChanCcTrRowStatusTable.setStatus("mandatory")
_MscDataSigChanCcTrRowStatusEntry_Object = MibTableRow
mscDataSigChanCcTrRowStatusEntry = _MscDataSigChanCcTrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 3, 1, 1)
)
mscDataSigChanCcTrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcTrIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanCcTrRowStatusEntry.setStatus("mandatory")
_MscDataSigChanCcTrRowStatus_Type = RowStatus
_MscDataSigChanCcTrRowStatus_Object = MibTableColumn
mscDataSigChanCcTrRowStatus = _MscDataSigChanCcTrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 3, 1, 1, 1),
    _MscDataSigChanCcTrRowStatus_Type()
)
mscDataSigChanCcTrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanCcTrRowStatus.setStatus("mandatory")
_MscDataSigChanCcTrComponentName_Type = DisplayString
_MscDataSigChanCcTrComponentName_Object = MibTableColumn
mscDataSigChanCcTrComponentName = _MscDataSigChanCcTrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 3, 1, 1, 2),
    _MscDataSigChanCcTrComponentName_Type()
)
mscDataSigChanCcTrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcTrComponentName.setStatus("mandatory")
_MscDataSigChanCcTrStorageType_Type = StorageType
_MscDataSigChanCcTrStorageType_Object = MibTableColumn
mscDataSigChanCcTrStorageType = _MscDataSigChanCcTrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 3, 1, 1, 4),
    _MscDataSigChanCcTrStorageType_Type()
)
mscDataSigChanCcTrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcTrStorageType.setStatus("mandatory")
_MscDataSigChanCcTrIndex_Type = NonReplicated
_MscDataSigChanCcTrIndex_Object = MibTableColumn
mscDataSigChanCcTrIndex = _MscDataSigChanCcTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 3, 1, 1, 10),
    _MscDataSigChanCcTrIndex_Type()
)
mscDataSigChanCcTrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDataSigChanCcTrIndex.setStatus("mandatory")
_MscDataSigChanCcTrPri_ObjectIdentity = ObjectIdentity
mscDataSigChanCcTrPri = _MscDataSigChanCcTrPri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 3, 2)
)
_MscDataSigChanCcTrPriRowStatusTable_Object = MibTable
mscDataSigChanCcTrPriRowStatusTable = _MscDataSigChanCcTrPriRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscDataSigChanCcTrPriRowStatusTable.setStatus("mandatory")
_MscDataSigChanCcTrPriRowStatusEntry_Object = MibTableRow
mscDataSigChanCcTrPriRowStatusEntry = _MscDataSigChanCcTrPriRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 3, 2, 1, 1)
)
mscDataSigChanCcTrPriRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcTrPriIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanCcTrPriRowStatusEntry.setStatus("mandatory")
_MscDataSigChanCcTrPriRowStatus_Type = RowStatus
_MscDataSigChanCcTrPriRowStatus_Object = MibTableColumn
mscDataSigChanCcTrPriRowStatus = _MscDataSigChanCcTrPriRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 3, 2, 1, 1, 1),
    _MscDataSigChanCcTrPriRowStatus_Type()
)
mscDataSigChanCcTrPriRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcTrPriRowStatus.setStatus("mandatory")
_MscDataSigChanCcTrPriComponentName_Type = DisplayString
_MscDataSigChanCcTrPriComponentName_Object = MibTableColumn
mscDataSigChanCcTrPriComponentName = _MscDataSigChanCcTrPriComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 3, 2, 1, 1, 2),
    _MscDataSigChanCcTrPriComponentName_Type()
)
mscDataSigChanCcTrPriComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcTrPriComponentName.setStatus("mandatory")
_MscDataSigChanCcTrPriStorageType_Type = StorageType
_MscDataSigChanCcTrPriStorageType_Object = MibTableColumn
mscDataSigChanCcTrPriStorageType = _MscDataSigChanCcTrPriStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 3, 2, 1, 1, 4),
    _MscDataSigChanCcTrPriStorageType_Type()
)
mscDataSigChanCcTrPriStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcTrPriStorageType.setStatus("mandatory")


class _MscDataSigChanCcTrPriIndex_Type(Integer32):
    """Custom type mscDataSigChanCcTrPriIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscDataSigChanCcTrPriIndex_Type.__name__ = "Integer32"
_MscDataSigChanCcTrPriIndex_Object = MibTableColumn
mscDataSigChanCcTrPriIndex = _MscDataSigChanCcTrPriIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 3, 2, 1, 1, 10),
    _MscDataSigChanCcTrPriIndex_Type()
)
mscDataSigChanCcTrPriIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDataSigChanCcTrPriIndex.setStatus("mandatory")
_MscDataSigChanCcTrPriBch_ObjectIdentity = ObjectIdentity
mscDataSigChanCcTrPriBch = _MscDataSigChanCcTrPriBch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 3, 2, 2)
)
_MscDataSigChanCcTrPriBchRowStatusTable_Object = MibTable
mscDataSigChanCcTrPriBchRowStatusTable = _MscDataSigChanCcTrPriBchRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscDataSigChanCcTrPriBchRowStatusTable.setStatus("mandatory")
_MscDataSigChanCcTrPriBchRowStatusEntry_Object = MibTableRow
mscDataSigChanCcTrPriBchRowStatusEntry = _MscDataSigChanCcTrPriBchRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 3, 2, 2, 1, 1)
)
mscDataSigChanCcTrPriBchRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcTrPriIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcTrPriBchIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanCcTrPriBchRowStatusEntry.setStatus("mandatory")
_MscDataSigChanCcTrPriBchRowStatus_Type = RowStatus
_MscDataSigChanCcTrPriBchRowStatus_Object = MibTableColumn
mscDataSigChanCcTrPriBchRowStatus = _MscDataSigChanCcTrPriBchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 3, 2, 2, 1, 1, 1),
    _MscDataSigChanCcTrPriBchRowStatus_Type()
)
mscDataSigChanCcTrPriBchRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcTrPriBchRowStatus.setStatus("mandatory")
_MscDataSigChanCcTrPriBchComponentName_Type = DisplayString
_MscDataSigChanCcTrPriBchComponentName_Object = MibTableColumn
mscDataSigChanCcTrPriBchComponentName = _MscDataSigChanCcTrPriBchComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 3, 2, 2, 1, 1, 2),
    _MscDataSigChanCcTrPriBchComponentName_Type()
)
mscDataSigChanCcTrPriBchComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcTrPriBchComponentName.setStatus("mandatory")
_MscDataSigChanCcTrPriBchStorageType_Type = StorageType
_MscDataSigChanCcTrPriBchStorageType_Object = MibTableColumn
mscDataSigChanCcTrPriBchStorageType = _MscDataSigChanCcTrPriBchStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 3, 2, 2, 1, 1, 4),
    _MscDataSigChanCcTrPriBchStorageType_Type()
)
mscDataSigChanCcTrPriBchStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcTrPriBchStorageType.setStatus("mandatory")


class _MscDataSigChanCcTrPriBchIndex_Type(Integer32):
    """Custom type mscDataSigChanCcTrPriBchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_MscDataSigChanCcTrPriBchIndex_Type.__name__ = "Integer32"
_MscDataSigChanCcTrPriBchIndex_Object = MibTableColumn
mscDataSigChanCcTrPriBchIndex = _MscDataSigChanCcTrPriBchIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 3, 2, 2, 1, 1, 10),
    _MscDataSigChanCcTrPriBchIndex_Type()
)
mscDataSigChanCcTrPriBchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDataSigChanCcTrPriBchIndex.setStatus("mandatory")
_MscDataSigChanCcBch_ObjectIdentity = ObjectIdentity
mscDataSigChanCcBch = _MscDataSigChanCcBch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 4)
)
_MscDataSigChanCcBchRowStatusTable_Object = MibTable
mscDataSigChanCcBchRowStatusTable = _MscDataSigChanCcBchRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 4, 1)
)
if mibBuilder.loadTexts:
    mscDataSigChanCcBchRowStatusTable.setStatus("mandatory")
_MscDataSigChanCcBchRowStatusEntry_Object = MibTableRow
mscDataSigChanCcBchRowStatusEntry = _MscDataSigChanCcBchRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 4, 1, 1)
)
mscDataSigChanCcBchRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcBchIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanCcBchRowStatusEntry.setStatus("mandatory")
_MscDataSigChanCcBchRowStatus_Type = RowStatus
_MscDataSigChanCcBchRowStatus_Object = MibTableColumn
mscDataSigChanCcBchRowStatus = _MscDataSigChanCcBchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 4, 1, 1, 1),
    _MscDataSigChanCcBchRowStatus_Type()
)
mscDataSigChanCcBchRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcBchRowStatus.setStatus("mandatory")
_MscDataSigChanCcBchComponentName_Type = DisplayString
_MscDataSigChanCcBchComponentName_Object = MibTableColumn
mscDataSigChanCcBchComponentName = _MscDataSigChanCcBchComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 4, 1, 1, 2),
    _MscDataSigChanCcBchComponentName_Type()
)
mscDataSigChanCcBchComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcBchComponentName.setStatus("mandatory")
_MscDataSigChanCcBchStorageType_Type = StorageType
_MscDataSigChanCcBchStorageType_Object = MibTableColumn
mscDataSigChanCcBchStorageType = _MscDataSigChanCcBchStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 4, 1, 1, 4),
    _MscDataSigChanCcBchStorageType_Type()
)
mscDataSigChanCcBchStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcBchStorageType.setStatus("mandatory")


class _MscDataSigChanCcBchIndex_Type(Integer32):
    """Custom type mscDataSigChanCcBchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_MscDataSigChanCcBchIndex_Type.__name__ = "Integer32"
_MscDataSigChanCcBchIndex_Object = MibTableColumn
mscDataSigChanCcBchIndex = _MscDataSigChanCcBchIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 4, 1, 1, 10),
    _MscDataSigChanCcBchIndex_Type()
)
mscDataSigChanCcBchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDataSigChanCcBchIndex.setStatus("mandatory")
_MscDataSigChanCcBchBchanOpDataTable_Object = MibTable
mscDataSigChanCcBchBchanOpDataTable = _MscDataSigChanCcBchBchanOpDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 4, 2)
)
if mibBuilder.loadTexts:
    mscDataSigChanCcBchBchanOpDataTable.setStatus("mandatory")
_MscDataSigChanCcBchBchanOpDataEntry_Object = MibTableRow
mscDataSigChanCcBchBchanOpDataEntry = _MscDataSigChanCcBchBchanOpDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 4, 2, 1)
)
mscDataSigChanCcBchBchanOpDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcBchIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanCcBchBchanOpDataEntry.setStatus("mandatory")


class _MscDataSigChanCcBchState_Type(Integer32):
    """Custom type mscDataSigChanCcBchState based on Integer32"""
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


_MscDataSigChanCcBchState_Type.__name__ = "Integer32"
_MscDataSigChanCcBchState_Object = MibTableColumn
mscDataSigChanCcBchState = _MscDataSigChanCcBchState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 4, 2, 1, 1),
    _MscDataSigChanCcBchState_Type()
)
mscDataSigChanCcBchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcBchState.setStatus("mandatory")


class _MscDataSigChanCcBchCallingPartyNumber_Type(DigitString):
    """Custom type mscDataSigChanCcBchCallingPartyNumber based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 14),
    )


_MscDataSigChanCcBchCallingPartyNumber_Type.__name__ = "DigitString"
_MscDataSigChanCcBchCallingPartyNumber_Object = MibTableColumn
mscDataSigChanCcBchCallingPartyNumber = _MscDataSigChanCcBchCallingPartyNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 4, 2, 1, 2),
    _MscDataSigChanCcBchCallingPartyNumber_Type()
)
mscDataSigChanCcBchCallingPartyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcBchCallingPartyNumber.setStatus("mandatory")


class _MscDataSigChanCcBchLastQ931ClearCause_Type(Integer32):
    """Custom type mscDataSigChanCcBchLastQ931ClearCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscDataSigChanCcBchLastQ931ClearCause_Type.__name__ = "Integer32"
_MscDataSigChanCcBchLastQ931ClearCause_Object = MibTableColumn
mscDataSigChanCcBchLastQ931ClearCause = _MscDataSigChanCcBchLastQ931ClearCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 4, 2, 1, 3),
    _MscDataSigChanCcBchLastQ931ClearCause_Type()
)
mscDataSigChanCcBchLastQ931ClearCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcBchLastQ931ClearCause.setStatus("mandatory")


class _MscDataSigChanCcBchRunningApplication_Type(AsciiString):
    """Custom type mscDataSigChanCcBchRunningApplication based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MscDataSigChanCcBchRunningApplication_Type.__name__ = "AsciiString"
_MscDataSigChanCcBchRunningApplication_Object = MibTableColumn
mscDataSigChanCcBchRunningApplication = _MscDataSigChanCcBchRunningApplication_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 4, 2, 1, 4),
    _MscDataSigChanCcBchRunningApplication_Type()
)
mscDataSigChanCcBchRunningApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcBchRunningApplication.setStatus("mandatory")
_MscDataSigChanCcStatsTable_Object = MibTable
mscDataSigChanCcStatsTable = _MscDataSigChanCcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 10)
)
if mibBuilder.loadTexts:
    mscDataSigChanCcStatsTable.setStatus("mandatory")
_MscDataSigChanCcStatsEntry_Object = MibTableRow
mscDataSigChanCcStatsEntry = _MscDataSigChanCcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 10, 1)
)
mscDataSigChanCcStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanCcIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanCcStatsEntry.setStatus("mandatory")


class _MscDataSigChanCcTotalValidInCalls_Type(Unsigned32):
    """Custom type mscDataSigChanCcTotalValidInCalls based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanCcTotalValidInCalls_Type.__name__ = "Unsigned32"
_MscDataSigChanCcTotalValidInCalls_Object = MibTableColumn
mscDataSigChanCcTotalValidInCalls = _MscDataSigChanCcTotalValidInCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 10, 1, 1),
    _MscDataSigChanCcTotalValidInCalls_Type()
)
mscDataSigChanCcTotalValidInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcTotalValidInCalls.setStatus("mandatory")


class _MscDataSigChanCcSuccessfullInCalls_Type(Unsigned32):
    """Custom type mscDataSigChanCcSuccessfullInCalls based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanCcSuccessfullInCalls_Type.__name__ = "Unsigned32"
_MscDataSigChanCcSuccessfullInCalls_Object = MibTableColumn
mscDataSigChanCcSuccessfullInCalls = _MscDataSigChanCcSuccessfullInCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 10, 1, 2),
    _MscDataSigChanCcSuccessfullInCalls_Type()
)
mscDataSigChanCcSuccessfullInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcSuccessfullInCalls.setStatus("mandatory")


class _MscDataSigChanCcInInvalidCapability_Type(Unsigned32):
    """Custom type mscDataSigChanCcInInvalidCapability based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanCcInInvalidCapability_Type.__name__ = "Unsigned32"
_MscDataSigChanCcInInvalidCapability_Object = MibTableColumn
mscDataSigChanCcInInvalidCapability = _MscDataSigChanCcInInvalidCapability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 10, 1, 3),
    _MscDataSigChanCcInInvalidCapability_Type()
)
mscDataSigChanCcInInvalidCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcInInvalidCapability.setStatus("mandatory")


class _MscDataSigChanCcInInvalidScreen_Type(Unsigned32):
    """Custom type mscDataSigChanCcInInvalidScreen based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanCcInInvalidScreen_Type.__name__ = "Unsigned32"
_MscDataSigChanCcInInvalidScreen_Object = MibTableColumn
mscDataSigChanCcInInvalidScreen = _MscDataSigChanCcInInvalidScreen_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 10, 1, 4),
    _MscDataSigChanCcInInvalidScreen_Type()
)
mscDataSigChanCcInInvalidScreen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcInInvalidScreen.setStatus("mandatory")


class _MscDataSigChanCcInInvalidCgpn_Type(Unsigned32):
    """Custom type mscDataSigChanCcInInvalidCgpn based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanCcInInvalidCgpn_Type.__name__ = "Unsigned32"
_MscDataSigChanCcInInvalidCgpn_Object = MibTableColumn
mscDataSigChanCcInInvalidCgpn = _MscDataSigChanCcInInvalidCgpn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 10, 1, 5),
    _MscDataSigChanCcInInvalidCgpn_Type()
)
mscDataSigChanCcInInvalidCgpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcInInvalidCgpn.setStatus("mandatory")


class _MscDataSigChanCcInChannelBusy_Type(Unsigned32):
    """Custom type mscDataSigChanCcInChannelBusy based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanCcInChannelBusy_Type.__name__ = "Unsigned32"
_MscDataSigChanCcInChannelBusy_Object = MibTableColumn
mscDataSigChanCcInChannelBusy = _MscDataSigChanCcInChannelBusy_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 10, 1, 6),
    _MscDataSigChanCcInChannelBusy_Type()
)
mscDataSigChanCcInChannelBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcInChannelBusy.setStatus("mandatory")


class _MscDataSigChanCcLastClearCause_Type(Integer32):
    """Custom type mscDataSigChanCcLastClearCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscDataSigChanCcLastClearCause_Type.__name__ = "Integer32"
_MscDataSigChanCcLastClearCause_Object = MibTableColumn
mscDataSigChanCcLastClearCause = _MscDataSigChanCcLastClearCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 10, 1, 7),
    _MscDataSigChanCcLastClearCause_Type()
)
mscDataSigChanCcLastClearCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcLastClearCause.setStatus("mandatory")


class _MscDataSigChanCcLastClearedCallingPartyNumber_Type(DigitString):
    """Custom type mscDataSigChanCcLastClearedCallingPartyNumber based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 14),
    )


_MscDataSigChanCcLastClearedCallingPartyNumber_Type.__name__ = "DigitString"
_MscDataSigChanCcLastClearedCallingPartyNumber_Object = MibTableColumn
mscDataSigChanCcLastClearedCallingPartyNumber = _MscDataSigChanCcLastClearedCallingPartyNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 2, 10, 1, 8),
    _MscDataSigChanCcLastClearedCallingPartyNumber_Type()
)
mscDataSigChanCcLastClearedCallingPartyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanCcLastClearedCallingPartyNumber.setStatus("mandatory")
_MscDataSigChanProvTable_Object = MibTable
mscDataSigChanProvTable = _MscDataSigChanProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 100)
)
if mibBuilder.loadTexts:
    mscDataSigChanProvTable.setStatus("mandatory")
_MscDataSigChanProvEntry_Object = MibTableRow
mscDataSigChanProvEntry = _MscDataSigChanProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 100, 1)
)
mscDataSigChanProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanProvEntry.setStatus("mandatory")


class _MscDataSigChanCommentText_Type(AsciiString):
    """Custom type mscDataSigChanCommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscDataSigChanCommentText_Type.__name__ = "AsciiString"
_MscDataSigChanCommentText_Object = MibTableColumn
mscDataSigChanCommentText = _MscDataSigChanCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 100, 1, 1),
    _MscDataSigChanCommentText_Type()
)
mscDataSigChanCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanCommentText.setStatus("mandatory")
_MscDataSigChanCidDataTable_Object = MibTable
mscDataSigChanCidDataTable = _MscDataSigChanCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 101)
)
if mibBuilder.loadTexts:
    mscDataSigChanCidDataTable.setStatus("mandatory")
_MscDataSigChanCidDataEntry_Object = MibTableRow
mscDataSigChanCidDataEntry = _MscDataSigChanCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 101, 1)
)
mscDataSigChanCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanCidDataEntry.setStatus("mandatory")


class _MscDataSigChanCustomerIdentifier_Type(Unsigned32):
    """Custom type mscDataSigChanCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscDataSigChanCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscDataSigChanCustomerIdentifier_Object = MibTableColumn
mscDataSigChanCustomerIdentifier = _MscDataSigChanCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 101, 1, 1),
    _MscDataSigChanCustomerIdentifier_Type()
)
mscDataSigChanCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanCustomerIdentifier.setStatus("mandatory")
_MscDataSigChanIfEntryTable_Object = MibTable
mscDataSigChanIfEntryTable = _MscDataSigChanIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 102)
)
if mibBuilder.loadTexts:
    mscDataSigChanIfEntryTable.setStatus("mandatory")
_MscDataSigChanIfEntryEntry_Object = MibTableRow
mscDataSigChanIfEntryEntry = _MscDataSigChanIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 102, 1)
)
mscDataSigChanIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanIfEntryEntry.setStatus("mandatory")


class _MscDataSigChanIfAdminStatus_Type(Integer32):
    """Custom type mscDataSigChanIfAdminStatus based on Integer32"""
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


_MscDataSigChanIfAdminStatus_Type.__name__ = "Integer32"
_MscDataSigChanIfAdminStatus_Object = MibTableColumn
mscDataSigChanIfAdminStatus = _MscDataSigChanIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 102, 1, 1),
    _MscDataSigChanIfAdminStatus_Type()
)
mscDataSigChanIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanIfAdminStatus.setStatus("mandatory")


class _MscDataSigChanIfIndex_Type(InterfaceIndex):
    """Custom type mscDataSigChanIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscDataSigChanIfIndex_Type.__name__ = "InterfaceIndex"
_MscDataSigChanIfIndex_Object = MibTableColumn
mscDataSigChanIfIndex = _MscDataSigChanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 102, 1, 2),
    _MscDataSigChanIfIndex_Type()
)
mscDataSigChanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanIfIndex.setStatus("mandatory")
_MscDataSigChanStateTable_Object = MibTable
mscDataSigChanStateTable = _MscDataSigChanStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 103)
)
if mibBuilder.loadTexts:
    mscDataSigChanStateTable.setStatus("mandatory")
_MscDataSigChanStateEntry_Object = MibTableRow
mscDataSigChanStateEntry = _MscDataSigChanStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 103, 1)
)
mscDataSigChanStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanStateEntry.setStatus("mandatory")


class _MscDataSigChanAdminState_Type(Integer32):
    """Custom type mscDataSigChanAdminState based on Integer32"""
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


_MscDataSigChanAdminState_Type.__name__ = "Integer32"
_MscDataSigChanAdminState_Object = MibTableColumn
mscDataSigChanAdminState = _MscDataSigChanAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 103, 1, 1),
    _MscDataSigChanAdminState_Type()
)
mscDataSigChanAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanAdminState.setStatus("mandatory")


class _MscDataSigChanOperationalState_Type(Integer32):
    """Custom type mscDataSigChanOperationalState based on Integer32"""
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


_MscDataSigChanOperationalState_Type.__name__ = "Integer32"
_MscDataSigChanOperationalState_Object = MibTableColumn
mscDataSigChanOperationalState = _MscDataSigChanOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 103, 1, 2),
    _MscDataSigChanOperationalState_Type()
)
mscDataSigChanOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanOperationalState.setStatus("mandatory")


class _MscDataSigChanUsageState_Type(Integer32):
    """Custom type mscDataSigChanUsageState based on Integer32"""
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


_MscDataSigChanUsageState_Type.__name__ = "Integer32"
_MscDataSigChanUsageState_Object = MibTableColumn
mscDataSigChanUsageState = _MscDataSigChanUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 103, 1, 3),
    _MscDataSigChanUsageState_Type()
)
mscDataSigChanUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanUsageState.setStatus("mandatory")
_MscDataSigChanOperStatusTable_Object = MibTable
mscDataSigChanOperStatusTable = _MscDataSigChanOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 104)
)
if mibBuilder.loadTexts:
    mscDataSigChanOperStatusTable.setStatus("mandatory")
_MscDataSigChanOperStatusEntry_Object = MibTableRow
mscDataSigChanOperStatusEntry = _MscDataSigChanOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 104, 1)
)
mscDataSigChanOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanOperStatusEntry.setStatus("mandatory")


class _MscDataSigChanSnmpOperStatus_Type(Integer32):
    """Custom type mscDataSigChanSnmpOperStatus based on Integer32"""
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


_MscDataSigChanSnmpOperStatus_Type.__name__ = "Integer32"
_MscDataSigChanSnmpOperStatus_Object = MibTableColumn
mscDataSigChanSnmpOperStatus = _MscDataSigChanSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 104, 1, 1),
    _MscDataSigChanSnmpOperStatus_Type()
)
mscDataSigChanSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanSnmpOperStatus.setStatus("mandatory")
_DataIsdnMIB_ObjectIdentity = ObjectIdentity
dataIsdnMIB = _DataIsdnMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 113)
)
_DataIsdnGroup_ObjectIdentity = ObjectIdentity
dataIsdnGroup = _DataIsdnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 113, 1)
)
_DataIsdnGroupCA_ObjectIdentity = ObjectIdentity
dataIsdnGroupCA = _DataIsdnGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 113, 1, 1)
)
_DataIsdnGroupCA02_ObjectIdentity = ObjectIdentity
dataIsdnGroupCA02 = _DataIsdnGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 113, 1, 1, 3)
)
_DataIsdnGroupCA02A_ObjectIdentity = ObjectIdentity
dataIsdnGroupCA02A = _DataIsdnGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 113, 1, 1, 3, 2)
)
_DataIsdnCapabilities_ObjectIdentity = ObjectIdentity
dataIsdnCapabilities = _DataIsdnCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 113, 3)
)
_DataIsdnCapabilitiesCA_ObjectIdentity = ObjectIdentity
dataIsdnCapabilitiesCA = _DataIsdnCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 113, 3, 1)
)
_DataIsdnCapabilitiesCA02_ObjectIdentity = ObjectIdentity
dataIsdnCapabilitiesCA02 = _DataIsdnCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 113, 3, 1, 3)
)
_DataIsdnCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
dataIsdnCapabilitiesCA02A = _DataIsdnCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 113, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-DataIsdnMIB",
    **{"mscDataSigChan": mscDataSigChan,
       "mscDataSigChanRowStatusTable": mscDataSigChanRowStatusTable,
       "mscDataSigChanRowStatusEntry": mscDataSigChanRowStatusEntry,
       "mscDataSigChanRowStatus": mscDataSigChanRowStatus,
       "mscDataSigChanComponentName": mscDataSigChanComponentName,
       "mscDataSigChanStorageType": mscDataSigChanStorageType,
       "mscDataSigChanIndex": mscDataSigChanIndex,
       "mscDataSigChanCc": mscDataSigChanCc,
       "mscDataSigChanCcRowStatusTable": mscDataSigChanCcRowStatusTable,
       "mscDataSigChanCcRowStatusEntry": mscDataSigChanCcRowStatusEntry,
       "mscDataSigChanCcRowStatus": mscDataSigChanCcRowStatus,
       "mscDataSigChanCcComponentName": mscDataSigChanCcComponentName,
       "mscDataSigChanCcStorageType": mscDataSigChanCcStorageType,
       "mscDataSigChanCcIndex": mscDataSigChanCcIndex,
       "mscDataSigChanCcCg": mscDataSigChanCcCg,
       "mscDataSigChanCcCgRowStatusTable": mscDataSigChanCcCgRowStatusTable,
       "mscDataSigChanCcCgRowStatusEntry": mscDataSigChanCcCgRowStatusEntry,
       "mscDataSigChanCcCgRowStatus": mscDataSigChanCcCgRowStatus,
       "mscDataSigChanCcCgComponentName": mscDataSigChanCcCgComponentName,
       "mscDataSigChanCcCgStorageType": mscDataSigChanCcCgStorageType,
       "mscDataSigChanCcCgIndex": mscDataSigChanCcCgIndex,
       "mscDataSigChanCcCgCgpn": mscDataSigChanCcCgCgpn,
       "mscDataSigChanCcCgCgpnRowStatusTable": mscDataSigChanCcCgCgpnRowStatusTable,
       "mscDataSigChanCcCgCgpnRowStatusEntry": mscDataSigChanCcCgCgpnRowStatusEntry,
       "mscDataSigChanCcCgCgpnRowStatus": mscDataSigChanCcCgCgpnRowStatus,
       "mscDataSigChanCcCgCgpnComponentName": mscDataSigChanCcCgCgpnComponentName,
       "mscDataSigChanCcCgCgpnStorageType": mscDataSigChanCcCgCgpnStorageType,
       "mscDataSigChanCcCgCgpnIndex": mscDataSigChanCcCgCgpnIndex,
       "mscDataSigChanCcCgBch": mscDataSigChanCcCgBch,
       "mscDataSigChanCcCgBchRowStatusTable": mscDataSigChanCcCgBchRowStatusTable,
       "mscDataSigChanCcCgBchRowStatusEntry": mscDataSigChanCcCgBchRowStatusEntry,
       "mscDataSigChanCcCgBchRowStatus": mscDataSigChanCcCgBchRowStatus,
       "mscDataSigChanCcCgBchComponentName": mscDataSigChanCcCgBchComponentName,
       "mscDataSigChanCcCgBchStorageType": mscDataSigChanCcCgBchStorageType,
       "mscDataSigChanCcCgBchIndex": mscDataSigChanCcCgBchIndex,
       "mscDataSigChanCcCgBchBchanOpDataTable": mscDataSigChanCcCgBchBchanOpDataTable,
       "mscDataSigChanCcCgBchBchanOpDataEntry": mscDataSigChanCcCgBchBchanOpDataEntry,
       "mscDataSigChanCcCgBchState": mscDataSigChanCcCgBchState,
       "mscDataSigChanCcCgBchCallingPartyNumber": mscDataSigChanCcCgBchCallingPartyNumber,
       "mscDataSigChanCcCgBchLastQ931ClearCause": mscDataSigChanCcCgBchLastQ931ClearCause,
       "mscDataSigChanCcCgBchRunningApplication": mscDataSigChanCcCgBchRunningApplication,
       "mscDataSigChanCcCgCidDataTable": mscDataSigChanCcCgCidDataTable,
       "mscDataSigChanCcCgCidDataEntry": mscDataSigChanCcCgCidDataEntry,
       "mscDataSigChanCcCgCustomerIdentifier": mscDataSigChanCcCgCustomerIdentifier,
       "mscDataSigChanCcCgProvTable": mscDataSigChanCcCgProvTable,
       "mscDataSigChanCcCgProvEntry": mscDataSigChanCcCgProvEntry,
       "mscDataSigChanCcCgCommentText": mscDataSigChanCcCgCommentText,
       "mscDataSigChanCcCgScreeningIndicator": mscDataSigChanCcCgScreeningIndicator,
       "mscDataSigChanCcCgChannelAssignmentOrder": mscDataSigChanCcCgChannelAssignmentOrder,
       "mscDataSigChanCcCgChannelList": mscDataSigChanCcCgChannelList,
       "mscDataSigChanCcCgStatsTable": mscDataSigChanCcCgStatsTable,
       "mscDataSigChanCcCgStatsEntry": mscDataSigChanCcCgStatsEntry,
       "mscDataSigChanCcCgTotalInCalls": mscDataSigChanCcCgTotalInCalls,
       "mscDataSigChanCcCgSuccessfullInCalls": mscDataSigChanCcCgSuccessfullInCalls,
       "mscDataSigChanCcCgRejectedNoChanAvail": mscDataSigChanCcCgRejectedNoChanAvail,
       "mscDataSigChanCcCgIdleChannelCount": mscDataSigChanCcCgIdleChannelCount,
       "mscDataSigChanCcCgBusyChannelCount": mscDataSigChanCcCgBusyChannelCount,
       "mscDataSigChanCcTr": mscDataSigChanCcTr,
       "mscDataSigChanCcTrRowStatusTable": mscDataSigChanCcTrRowStatusTable,
       "mscDataSigChanCcTrRowStatusEntry": mscDataSigChanCcTrRowStatusEntry,
       "mscDataSigChanCcTrRowStatus": mscDataSigChanCcTrRowStatus,
       "mscDataSigChanCcTrComponentName": mscDataSigChanCcTrComponentName,
       "mscDataSigChanCcTrStorageType": mscDataSigChanCcTrStorageType,
       "mscDataSigChanCcTrIndex": mscDataSigChanCcTrIndex,
       "mscDataSigChanCcTrPri": mscDataSigChanCcTrPri,
       "mscDataSigChanCcTrPriRowStatusTable": mscDataSigChanCcTrPriRowStatusTable,
       "mscDataSigChanCcTrPriRowStatusEntry": mscDataSigChanCcTrPriRowStatusEntry,
       "mscDataSigChanCcTrPriRowStatus": mscDataSigChanCcTrPriRowStatus,
       "mscDataSigChanCcTrPriComponentName": mscDataSigChanCcTrPriComponentName,
       "mscDataSigChanCcTrPriStorageType": mscDataSigChanCcTrPriStorageType,
       "mscDataSigChanCcTrPriIndex": mscDataSigChanCcTrPriIndex,
       "mscDataSigChanCcTrPriBch": mscDataSigChanCcTrPriBch,
       "mscDataSigChanCcTrPriBchRowStatusTable": mscDataSigChanCcTrPriBchRowStatusTable,
       "mscDataSigChanCcTrPriBchRowStatusEntry": mscDataSigChanCcTrPriBchRowStatusEntry,
       "mscDataSigChanCcTrPriBchRowStatus": mscDataSigChanCcTrPriBchRowStatus,
       "mscDataSigChanCcTrPriBchComponentName": mscDataSigChanCcTrPriBchComponentName,
       "mscDataSigChanCcTrPriBchStorageType": mscDataSigChanCcTrPriBchStorageType,
       "mscDataSigChanCcTrPriBchIndex": mscDataSigChanCcTrPriBchIndex,
       "mscDataSigChanCcBch": mscDataSigChanCcBch,
       "mscDataSigChanCcBchRowStatusTable": mscDataSigChanCcBchRowStatusTable,
       "mscDataSigChanCcBchRowStatusEntry": mscDataSigChanCcBchRowStatusEntry,
       "mscDataSigChanCcBchRowStatus": mscDataSigChanCcBchRowStatus,
       "mscDataSigChanCcBchComponentName": mscDataSigChanCcBchComponentName,
       "mscDataSigChanCcBchStorageType": mscDataSigChanCcBchStorageType,
       "mscDataSigChanCcBchIndex": mscDataSigChanCcBchIndex,
       "mscDataSigChanCcBchBchanOpDataTable": mscDataSigChanCcBchBchanOpDataTable,
       "mscDataSigChanCcBchBchanOpDataEntry": mscDataSigChanCcBchBchanOpDataEntry,
       "mscDataSigChanCcBchState": mscDataSigChanCcBchState,
       "mscDataSigChanCcBchCallingPartyNumber": mscDataSigChanCcBchCallingPartyNumber,
       "mscDataSigChanCcBchLastQ931ClearCause": mscDataSigChanCcBchLastQ931ClearCause,
       "mscDataSigChanCcBchRunningApplication": mscDataSigChanCcBchRunningApplication,
       "mscDataSigChanCcStatsTable": mscDataSigChanCcStatsTable,
       "mscDataSigChanCcStatsEntry": mscDataSigChanCcStatsEntry,
       "mscDataSigChanCcTotalValidInCalls": mscDataSigChanCcTotalValidInCalls,
       "mscDataSigChanCcSuccessfullInCalls": mscDataSigChanCcSuccessfullInCalls,
       "mscDataSigChanCcInInvalidCapability": mscDataSigChanCcInInvalidCapability,
       "mscDataSigChanCcInInvalidScreen": mscDataSigChanCcInInvalidScreen,
       "mscDataSigChanCcInInvalidCgpn": mscDataSigChanCcInInvalidCgpn,
       "mscDataSigChanCcInChannelBusy": mscDataSigChanCcInChannelBusy,
       "mscDataSigChanCcLastClearCause": mscDataSigChanCcLastClearCause,
       "mscDataSigChanCcLastClearedCallingPartyNumber": mscDataSigChanCcLastClearedCallingPartyNumber,
       "mscDataSigChanProvTable": mscDataSigChanProvTable,
       "mscDataSigChanProvEntry": mscDataSigChanProvEntry,
       "mscDataSigChanCommentText": mscDataSigChanCommentText,
       "mscDataSigChanCidDataTable": mscDataSigChanCidDataTable,
       "mscDataSigChanCidDataEntry": mscDataSigChanCidDataEntry,
       "mscDataSigChanCustomerIdentifier": mscDataSigChanCustomerIdentifier,
       "mscDataSigChanIfEntryTable": mscDataSigChanIfEntryTable,
       "mscDataSigChanIfEntryEntry": mscDataSigChanIfEntryEntry,
       "mscDataSigChanIfAdminStatus": mscDataSigChanIfAdminStatus,
       "mscDataSigChanIfIndex": mscDataSigChanIfIndex,
       "mscDataSigChanStateTable": mscDataSigChanStateTable,
       "mscDataSigChanStateEntry": mscDataSigChanStateEntry,
       "mscDataSigChanAdminState": mscDataSigChanAdminState,
       "mscDataSigChanOperationalState": mscDataSigChanOperationalState,
       "mscDataSigChanUsageState": mscDataSigChanUsageState,
       "mscDataSigChanOperStatusTable": mscDataSigChanOperStatusTable,
       "mscDataSigChanOperStatusEntry": mscDataSigChanOperStatusEntry,
       "mscDataSigChanSnmpOperStatus": mscDataSigChanSnmpOperStatus,
       "dataIsdnMIB": dataIsdnMIB,
       "dataIsdnGroup": dataIsdnGroup,
       "dataIsdnGroupCA": dataIsdnGroupCA,
       "dataIsdnGroupCA02": dataIsdnGroupCA02,
       "dataIsdnGroupCA02A": dataIsdnGroupCA02A,
       "dataIsdnCapabilities": dataIsdnCapabilities,
       "dataIsdnCapabilitiesCA": dataIsdnCapabilitiesCA,
       "dataIsdnCapabilitiesCA02": dataIsdnCapabilitiesCA02,
       "dataIsdnCapabilitiesCA02A": dataIsdnCapabilitiesCA02A}
)
