# SNMP MIB module (Nortel-MsCarrier-MscPassport-AppnMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-AppnMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:45 2024
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
 Gauge32,
 Integer32,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 AsciiStringIndex,
 DashedHexString,
 DigitString,
 EnterpriseDateAndTime,
 Hex,
 HexString,
 Link,
 NonReplicated,
 PassportCounter64) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
    "DashedHexString",
    "DigitString",
    "EnterpriseDateAndTime",
    "Hex",
    "HexString",
    "Link",
    "NonReplicated",
    "PassportCounter64")

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

_MscAppn_ObjectIdentity = ObjectIdentity
mscAppn = _MscAppn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110)
)
_MscAppnRowStatusTable_Object = MibTable
mscAppnRowStatusTable = _MscAppnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 1)
)
if mibBuilder.loadTexts:
    mscAppnRowStatusTable.setStatus("mandatory")
_MscAppnRowStatusEntry_Object = MibTableRow
mscAppnRowStatusEntry = _MscAppnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 1, 1)
)
mscAppnRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
)
if mibBuilder.loadTexts:
    mscAppnRowStatusEntry.setStatus("mandatory")
_MscAppnRowStatus_Type = RowStatus
_MscAppnRowStatus_Object = MibTableColumn
mscAppnRowStatus = _MscAppnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 1, 1, 1),
    _MscAppnRowStatus_Type()
)
mscAppnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnRowStatus.setStatus("mandatory")
_MscAppnComponentName_Type = DisplayString
_MscAppnComponentName_Object = MibTableColumn
mscAppnComponentName = _MscAppnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 1, 1, 2),
    _MscAppnComponentName_Type()
)
mscAppnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnComponentName.setStatus("mandatory")
_MscAppnStorageType_Type = StorageType
_MscAppnStorageType_Object = MibTableColumn
mscAppnStorageType = _MscAppnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 1, 1, 4),
    _MscAppnStorageType_Type()
)
mscAppnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnStorageType.setStatus("mandatory")


class _MscAppnIndex_Type(AsciiStringIndex):
    """Custom type mscAppnIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_MscAppnIndex_Type.__name__ = "AsciiStringIndex"
_MscAppnIndex_Object = MibTableColumn
mscAppnIndex = _MscAppnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 1, 1, 10),
    _MscAppnIndex_Type()
)
mscAppnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnIndex.setStatus("mandatory")
_MscAppnDna_ObjectIdentity = ObjectIdentity
mscAppnDna = _MscAppnDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2)
)
_MscAppnDnaRowStatusTable_Object = MibTable
mscAppnDnaRowStatusTable = _MscAppnDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 1)
)
if mibBuilder.loadTexts:
    mscAppnDnaRowStatusTable.setStatus("mandatory")
_MscAppnDnaRowStatusEntry_Object = MibTableRow
mscAppnDnaRowStatusEntry = _MscAppnDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 1, 1)
)
mscAppnDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDnaIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDnaRowStatusEntry.setStatus("mandatory")
_MscAppnDnaRowStatus_Type = RowStatus
_MscAppnDnaRowStatus_Object = MibTableColumn
mscAppnDnaRowStatus = _MscAppnDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 1, 1, 1),
    _MscAppnDnaRowStatus_Type()
)
mscAppnDnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDnaRowStatus.setStatus("mandatory")
_MscAppnDnaComponentName_Type = DisplayString
_MscAppnDnaComponentName_Object = MibTableColumn
mscAppnDnaComponentName = _MscAppnDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 1, 1, 2),
    _MscAppnDnaComponentName_Type()
)
mscAppnDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDnaComponentName.setStatus("mandatory")
_MscAppnDnaStorageType_Type = StorageType
_MscAppnDnaStorageType_Object = MibTableColumn
mscAppnDnaStorageType = _MscAppnDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 1, 1, 4),
    _MscAppnDnaStorageType_Type()
)
mscAppnDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDnaStorageType.setStatus("mandatory")
_MscAppnDnaIndex_Type = NonReplicated
_MscAppnDnaIndex_Object = MibTableColumn
mscAppnDnaIndex = _MscAppnDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 1, 1, 10),
    _MscAppnDnaIndex_Type()
)
mscAppnDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnDnaIndex.setStatus("mandatory")
_MscAppnDnaHgM_ObjectIdentity = ObjectIdentity
mscAppnDnaHgM = _MscAppnDnaHgM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 2)
)
_MscAppnDnaHgMRowStatusTable_Object = MibTable
mscAppnDnaHgMRowStatusTable = _MscAppnDnaHgMRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscAppnDnaHgMRowStatusTable.setStatus("mandatory")
_MscAppnDnaHgMRowStatusEntry_Object = MibTableRow
mscAppnDnaHgMRowStatusEntry = _MscAppnDnaHgMRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 2, 1, 1)
)
mscAppnDnaHgMRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDnaHgMIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDnaHgMRowStatusEntry.setStatus("mandatory")
_MscAppnDnaHgMRowStatus_Type = RowStatus
_MscAppnDnaHgMRowStatus_Object = MibTableColumn
mscAppnDnaHgMRowStatus = _MscAppnDnaHgMRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 2, 1, 1, 1),
    _MscAppnDnaHgMRowStatus_Type()
)
mscAppnDnaHgMRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDnaHgMRowStatus.setStatus("mandatory")
_MscAppnDnaHgMComponentName_Type = DisplayString
_MscAppnDnaHgMComponentName_Object = MibTableColumn
mscAppnDnaHgMComponentName = _MscAppnDnaHgMComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 2, 1, 1, 2),
    _MscAppnDnaHgMComponentName_Type()
)
mscAppnDnaHgMComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDnaHgMComponentName.setStatus("mandatory")
_MscAppnDnaHgMStorageType_Type = StorageType
_MscAppnDnaHgMStorageType_Object = MibTableColumn
mscAppnDnaHgMStorageType = _MscAppnDnaHgMStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 2, 1, 1, 4),
    _MscAppnDnaHgMStorageType_Type()
)
mscAppnDnaHgMStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDnaHgMStorageType.setStatus("mandatory")
_MscAppnDnaHgMIndex_Type = NonReplicated
_MscAppnDnaHgMIndex_Object = MibTableColumn
mscAppnDnaHgMIndex = _MscAppnDnaHgMIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 2, 1, 1, 10),
    _MscAppnDnaHgMIndex_Type()
)
mscAppnDnaHgMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnDnaHgMIndex.setStatus("mandatory")
_MscAppnDnaHgMHgAddr_ObjectIdentity = ObjectIdentity
mscAppnDnaHgMHgAddr = _MscAppnDnaHgMHgAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 2, 2)
)
_MscAppnDnaHgMHgAddrRowStatusTable_Object = MibTable
mscAppnDnaHgMHgAddrRowStatusTable = _MscAppnDnaHgMHgAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscAppnDnaHgMHgAddrRowStatusTable.setStatus("mandatory")
_MscAppnDnaHgMHgAddrRowStatusEntry_Object = MibTableRow
mscAppnDnaHgMHgAddrRowStatusEntry = _MscAppnDnaHgMHgAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 2, 2, 1, 1)
)
mscAppnDnaHgMHgAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDnaHgMIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDnaHgMHgAddrIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDnaHgMHgAddrRowStatusEntry.setStatus("mandatory")
_MscAppnDnaHgMHgAddrRowStatus_Type = RowStatus
_MscAppnDnaHgMHgAddrRowStatus_Object = MibTableColumn
mscAppnDnaHgMHgAddrRowStatus = _MscAppnDnaHgMHgAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 2, 2, 1, 1, 1),
    _MscAppnDnaHgMHgAddrRowStatus_Type()
)
mscAppnDnaHgMHgAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDnaHgMHgAddrRowStatus.setStatus("mandatory")
_MscAppnDnaHgMHgAddrComponentName_Type = DisplayString
_MscAppnDnaHgMHgAddrComponentName_Object = MibTableColumn
mscAppnDnaHgMHgAddrComponentName = _MscAppnDnaHgMHgAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 2, 2, 1, 1, 2),
    _MscAppnDnaHgMHgAddrComponentName_Type()
)
mscAppnDnaHgMHgAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDnaHgMHgAddrComponentName.setStatus("mandatory")
_MscAppnDnaHgMHgAddrStorageType_Type = StorageType
_MscAppnDnaHgMHgAddrStorageType_Object = MibTableColumn
mscAppnDnaHgMHgAddrStorageType = _MscAppnDnaHgMHgAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 2, 2, 1, 1, 4),
    _MscAppnDnaHgMHgAddrStorageType_Type()
)
mscAppnDnaHgMHgAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDnaHgMHgAddrStorageType.setStatus("mandatory")


class _MscAppnDnaHgMHgAddrIndex_Type(Integer32):
    """Custom type mscAppnDnaHgMHgAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MscAppnDnaHgMHgAddrIndex_Type.__name__ = "Integer32"
_MscAppnDnaHgMHgAddrIndex_Object = MibTableColumn
mscAppnDnaHgMHgAddrIndex = _MscAppnDnaHgMHgAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 2, 2, 1, 1, 10),
    _MscAppnDnaHgMHgAddrIndex_Type()
)
mscAppnDnaHgMHgAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnDnaHgMHgAddrIndex.setStatus("mandatory")
_MscAppnDnaHgMHgAddrAddrTable_Object = MibTable
mscAppnDnaHgMHgAddrAddrTable = _MscAppnDnaHgMHgAddrAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscAppnDnaHgMHgAddrAddrTable.setStatus("mandatory")
_MscAppnDnaHgMHgAddrAddrEntry_Object = MibTableRow
mscAppnDnaHgMHgAddrAddrEntry = _MscAppnDnaHgMHgAddrAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 2, 2, 10, 1)
)
mscAppnDnaHgMHgAddrAddrEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDnaHgMIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDnaHgMHgAddrIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDnaHgMHgAddrAddrEntry.setStatus("mandatory")


class _MscAppnDnaHgMHgAddrNumberingPlanIndicator_Type(Integer32):
    """Custom type mscAppnDnaHgMHgAddrNumberingPlanIndicator based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_MscAppnDnaHgMHgAddrNumberingPlanIndicator_Type.__name__ = "Integer32"
_MscAppnDnaHgMHgAddrNumberingPlanIndicator_Object = MibTableColumn
mscAppnDnaHgMHgAddrNumberingPlanIndicator = _MscAppnDnaHgMHgAddrNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 2, 2, 10, 1, 1),
    _MscAppnDnaHgMHgAddrNumberingPlanIndicator_Type()
)
mscAppnDnaHgMHgAddrNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDnaHgMHgAddrNumberingPlanIndicator.setStatus("mandatory")


class _MscAppnDnaHgMHgAddrDataNetworkAddress_Type(DigitString):
    """Custom type mscAppnDnaHgMHgAddrDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscAppnDnaHgMHgAddrDataNetworkAddress_Type.__name__ = "DigitString"
_MscAppnDnaHgMHgAddrDataNetworkAddress_Object = MibTableColumn
mscAppnDnaHgMHgAddrDataNetworkAddress = _MscAppnDnaHgMHgAddrDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 2, 2, 10, 1, 2),
    _MscAppnDnaHgMHgAddrDataNetworkAddress_Type()
)
mscAppnDnaHgMHgAddrDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDnaHgMHgAddrDataNetworkAddress.setStatus("mandatory")
_MscAppnDnaHgMIfTable_Object = MibTable
mscAppnDnaHgMIfTable = _MscAppnDnaHgMIfTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscAppnDnaHgMIfTable.setStatus("mandatory")
_MscAppnDnaHgMIfEntry_Object = MibTableRow
mscAppnDnaHgMIfEntry = _MscAppnDnaHgMIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 2, 10, 1)
)
mscAppnDnaHgMIfEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDnaHgMIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDnaHgMIfEntry.setStatus("mandatory")


class _MscAppnDnaHgMAvailabilityUpdateThreshold_Type(Unsigned32):
    """Custom type mscAppnDnaHgMAvailabilityUpdateThreshold based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscAppnDnaHgMAvailabilityUpdateThreshold_Type.__name__ = "Unsigned32"
_MscAppnDnaHgMAvailabilityUpdateThreshold_Object = MibTableColumn
mscAppnDnaHgMAvailabilityUpdateThreshold = _MscAppnDnaHgMAvailabilityUpdateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 2, 10, 1, 1),
    _MscAppnDnaHgMAvailabilityUpdateThreshold_Type()
)
mscAppnDnaHgMAvailabilityUpdateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDnaHgMAvailabilityUpdateThreshold.setStatus("mandatory")
_MscAppnDnaHgMOpTable_Object = MibTable
mscAppnDnaHgMOpTable = _MscAppnDnaHgMOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 2, 11)
)
if mibBuilder.loadTexts:
    mscAppnDnaHgMOpTable.setStatus("mandatory")
_MscAppnDnaHgMOpEntry_Object = MibTableRow
mscAppnDnaHgMOpEntry = _MscAppnDnaHgMOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 2, 11, 1)
)
mscAppnDnaHgMOpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDnaHgMIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDnaHgMOpEntry.setStatus("mandatory")


class _MscAppnDnaHgMMaxAvailableChannels_Type(Unsigned32):
    """Custom type mscAppnDnaHgMMaxAvailableChannels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscAppnDnaHgMMaxAvailableChannels_Type.__name__ = "Unsigned32"
_MscAppnDnaHgMMaxAvailableChannels_Object = MibTableColumn
mscAppnDnaHgMMaxAvailableChannels = _MscAppnDnaHgMMaxAvailableChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 2, 11, 1, 1),
    _MscAppnDnaHgMMaxAvailableChannels_Type()
)
mscAppnDnaHgMMaxAvailableChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDnaHgMMaxAvailableChannels.setStatus("mandatory")


class _MscAppnDnaHgMAvailableChannels_Type(Unsigned32):
    """Custom type mscAppnDnaHgMAvailableChannels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscAppnDnaHgMAvailableChannels_Type.__name__ = "Unsigned32"
_MscAppnDnaHgMAvailableChannels_Object = MibTableColumn
mscAppnDnaHgMAvailableChannels = _MscAppnDnaHgMAvailableChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 2, 11, 1, 2),
    _MscAppnDnaHgMAvailableChannels_Type()
)
mscAppnDnaHgMAvailableChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDnaHgMAvailableChannels.setStatus("mandatory")


class _MscAppnDnaHgMAvailabilityDelta_Type(Integer32):
    """Custom type mscAppnDnaHgMAvailabilityDelta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4096, 4096),
    )


_MscAppnDnaHgMAvailabilityDelta_Type.__name__ = "Integer32"
_MscAppnDnaHgMAvailabilityDelta_Object = MibTableColumn
mscAppnDnaHgMAvailabilityDelta = _MscAppnDnaHgMAvailabilityDelta_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 2, 11, 1, 3),
    _MscAppnDnaHgMAvailabilityDelta_Type()
)
mscAppnDnaHgMAvailabilityDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDnaHgMAvailabilityDelta.setStatus("mandatory")
_MscAppnDnaCug_ObjectIdentity = ObjectIdentity
mscAppnDnaCug = _MscAppnDnaCug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 3)
)
_MscAppnDnaCugRowStatusTable_Object = MibTable
mscAppnDnaCugRowStatusTable = _MscAppnDnaCugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mscAppnDnaCugRowStatusTable.setStatus("mandatory")
_MscAppnDnaCugRowStatusEntry_Object = MibTableRow
mscAppnDnaCugRowStatusEntry = _MscAppnDnaCugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 3, 1, 1)
)
mscAppnDnaCugRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDnaCugIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDnaCugRowStatusEntry.setStatus("mandatory")
_MscAppnDnaCugRowStatus_Type = RowStatus
_MscAppnDnaCugRowStatus_Object = MibTableColumn
mscAppnDnaCugRowStatus = _MscAppnDnaCugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 3, 1, 1, 1),
    _MscAppnDnaCugRowStatus_Type()
)
mscAppnDnaCugRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDnaCugRowStatus.setStatus("mandatory")
_MscAppnDnaCugComponentName_Type = DisplayString
_MscAppnDnaCugComponentName_Object = MibTableColumn
mscAppnDnaCugComponentName = _MscAppnDnaCugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 3, 1, 1, 2),
    _MscAppnDnaCugComponentName_Type()
)
mscAppnDnaCugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDnaCugComponentName.setStatus("mandatory")
_MscAppnDnaCugStorageType_Type = StorageType
_MscAppnDnaCugStorageType_Object = MibTableColumn
mscAppnDnaCugStorageType = _MscAppnDnaCugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 3, 1, 1, 4),
    _MscAppnDnaCugStorageType_Type()
)
mscAppnDnaCugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDnaCugStorageType.setStatus("mandatory")


class _MscAppnDnaCugIndex_Type(Integer32):
    """Custom type mscAppnDnaCugIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscAppnDnaCugIndex_Type.__name__ = "Integer32"
_MscAppnDnaCugIndex_Object = MibTableColumn
mscAppnDnaCugIndex = _MscAppnDnaCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 3, 1, 1, 10),
    _MscAppnDnaCugIndex_Type()
)
mscAppnDnaCugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnDnaCugIndex.setStatus("mandatory")
_MscAppnDnaCugCugOptionsTable_Object = MibTable
mscAppnDnaCugCugOptionsTable = _MscAppnDnaCugCugOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 3, 10)
)
if mibBuilder.loadTexts:
    mscAppnDnaCugCugOptionsTable.setStatus("mandatory")
_MscAppnDnaCugCugOptionsEntry_Object = MibTableRow
mscAppnDnaCugCugOptionsEntry = _MscAppnDnaCugCugOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 3, 10, 1)
)
mscAppnDnaCugCugOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDnaCugIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDnaCugCugOptionsEntry.setStatus("mandatory")


class _MscAppnDnaCugType_Type(Integer32):
    """Custom type mscAppnDnaCugType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("international", 1),
          ("national", 0))
    )


_MscAppnDnaCugType_Type.__name__ = "Integer32"
_MscAppnDnaCugType_Object = MibTableColumn
mscAppnDnaCugType = _MscAppnDnaCugType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 3, 10, 1, 1),
    _MscAppnDnaCugType_Type()
)
mscAppnDnaCugType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDnaCugType.setStatus("mandatory")


class _MscAppnDnaCugDnic_Type(DigitString):
    """Custom type mscAppnDnaCugDnic based on DigitString"""
    defaultHexValue = "30303030"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_MscAppnDnaCugDnic_Type.__name__ = "DigitString"
_MscAppnDnaCugDnic_Object = MibTableColumn
mscAppnDnaCugDnic = _MscAppnDnaCugDnic_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 3, 10, 1, 2),
    _MscAppnDnaCugDnic_Type()
)
mscAppnDnaCugDnic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDnaCugDnic.setStatus("mandatory")


class _MscAppnDnaCugInterlockCode_Type(Unsigned32):
    """Custom type mscAppnDnaCugInterlockCode based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnDnaCugInterlockCode_Type.__name__ = "Unsigned32"
_MscAppnDnaCugInterlockCode_Object = MibTableColumn
mscAppnDnaCugInterlockCode = _MscAppnDnaCugInterlockCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 3, 10, 1, 3),
    _MscAppnDnaCugInterlockCode_Type()
)
mscAppnDnaCugInterlockCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDnaCugInterlockCode.setStatus("mandatory")


class _MscAppnDnaCugPreferential_Type(Integer32):
    """Custom type mscAppnDnaCugPreferential based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MscAppnDnaCugPreferential_Type.__name__ = "Integer32"
_MscAppnDnaCugPreferential_Object = MibTableColumn
mscAppnDnaCugPreferential = _MscAppnDnaCugPreferential_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 3, 10, 1, 4),
    _MscAppnDnaCugPreferential_Type()
)
mscAppnDnaCugPreferential.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDnaCugPreferential.setStatus("mandatory")


class _MscAppnDnaCugOutCalls_Type(Integer32):
    """Custom type mscAppnDnaCugOutCalls based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_MscAppnDnaCugOutCalls_Type.__name__ = "Integer32"
_MscAppnDnaCugOutCalls_Object = MibTableColumn
mscAppnDnaCugOutCalls = _MscAppnDnaCugOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 3, 10, 1, 5),
    _MscAppnDnaCugOutCalls_Type()
)
mscAppnDnaCugOutCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDnaCugOutCalls.setStatus("mandatory")


class _MscAppnDnaCugIncCalls_Type(Integer32):
    """Custom type mscAppnDnaCugIncCalls based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_MscAppnDnaCugIncCalls_Type.__name__ = "Integer32"
_MscAppnDnaCugIncCalls_Object = MibTableColumn
mscAppnDnaCugIncCalls = _MscAppnDnaCugIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 3, 10, 1, 6),
    _MscAppnDnaCugIncCalls_Type()
)
mscAppnDnaCugIncCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDnaCugIncCalls.setStatus("mandatory")


class _MscAppnDnaCugPrivileged_Type(Integer32):
    """Custom type mscAppnDnaCugPrivileged based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MscAppnDnaCugPrivileged_Type.__name__ = "Integer32"
_MscAppnDnaCugPrivileged_Object = MibTableColumn
mscAppnDnaCugPrivileged = _MscAppnDnaCugPrivileged_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 3, 10, 1, 7),
    _MscAppnDnaCugPrivileged_Type()
)
mscAppnDnaCugPrivileged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDnaCugPrivileged.setStatus("mandatory")
_MscAppnDnaAddressTable_Object = MibTable
mscAppnDnaAddressTable = _MscAppnDnaAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 10)
)
if mibBuilder.loadTexts:
    mscAppnDnaAddressTable.setStatus("mandatory")
_MscAppnDnaAddressEntry_Object = MibTableRow
mscAppnDnaAddressEntry = _MscAppnDnaAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 10, 1)
)
mscAppnDnaAddressEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDnaIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDnaAddressEntry.setStatus("mandatory")


class _MscAppnDnaNumberingPlanIndicator_Type(Integer32):
    """Custom type mscAppnDnaNumberingPlanIndicator based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_MscAppnDnaNumberingPlanIndicator_Type.__name__ = "Integer32"
_MscAppnDnaNumberingPlanIndicator_Object = MibTableColumn
mscAppnDnaNumberingPlanIndicator = _MscAppnDnaNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 10, 1, 1),
    _MscAppnDnaNumberingPlanIndicator_Type()
)
mscAppnDnaNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDnaNumberingPlanIndicator.setStatus("mandatory")


class _MscAppnDnaDataNetworkAddress_Type(DigitString):
    """Custom type mscAppnDnaDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscAppnDnaDataNetworkAddress_Type.__name__ = "DigitString"
_MscAppnDnaDataNetworkAddress_Object = MibTableColumn
mscAppnDnaDataNetworkAddress = _MscAppnDnaDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 10, 1, 2),
    _MscAppnDnaDataNetworkAddress_Type()
)
mscAppnDnaDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDnaDataNetworkAddress.setStatus("mandatory")
_MscAppnDnaOutgoingOptionsTable_Object = MibTable
mscAppnDnaOutgoingOptionsTable = _MscAppnDnaOutgoingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 12)
)
if mibBuilder.loadTexts:
    mscAppnDnaOutgoingOptionsTable.setStatus("mandatory")
_MscAppnDnaOutgoingOptionsEntry_Object = MibTableRow
mscAppnDnaOutgoingOptionsEntry = _MscAppnDnaOutgoingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 12, 1)
)
mscAppnDnaOutgoingOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDnaIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDnaOutgoingOptionsEntry.setStatus("mandatory")


class _MscAppnDnaOutDefaultPriority_Type(Integer32):
    """Custom type mscAppnDnaOutDefaultPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("normal", 0))
    )


_MscAppnDnaOutDefaultPriority_Type.__name__ = "Integer32"
_MscAppnDnaOutDefaultPriority_Object = MibTableColumn
mscAppnDnaOutDefaultPriority = _MscAppnDnaOutDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 12, 1, 7),
    _MscAppnDnaOutDefaultPriority_Type()
)
mscAppnDnaOutDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDnaOutDefaultPriority.setStatus("mandatory")


class _MscAppnDnaOutDefaultPathSensitivity_Type(Integer32):
    """Custom type mscAppnDnaOutDefaultPathSensitivity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("delay", 1),
          ("throughput", 0))
    )


_MscAppnDnaOutDefaultPathSensitivity_Type.__name__ = "Integer32"
_MscAppnDnaOutDefaultPathSensitivity_Object = MibTableColumn
mscAppnDnaOutDefaultPathSensitivity = _MscAppnDnaOutDefaultPathSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 12, 1, 11),
    _MscAppnDnaOutDefaultPathSensitivity_Type()
)
mscAppnDnaOutDefaultPathSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDnaOutDefaultPathSensitivity.setStatus("obsolete")


class _MscAppnDnaOutPathSensitivityOverRide_Type(Integer32):
    """Custom type mscAppnDnaOutPathSensitivityOverRide based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MscAppnDnaOutPathSensitivityOverRide_Type.__name__ = "Integer32"
_MscAppnDnaOutPathSensitivityOverRide_Object = MibTableColumn
mscAppnDnaOutPathSensitivityOverRide = _MscAppnDnaOutPathSensitivityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 12, 1, 12),
    _MscAppnDnaOutPathSensitivityOverRide_Type()
)
mscAppnDnaOutPathSensitivityOverRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDnaOutPathSensitivityOverRide.setStatus("obsolete")


class _MscAppnDnaOutDefaultPathReliability_Type(Integer32):
    """Custom type mscAppnDnaOutDefaultPathReliability based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 0),
          ("normal", 1))
    )


_MscAppnDnaOutDefaultPathReliability_Type.__name__ = "Integer32"
_MscAppnDnaOutDefaultPathReliability_Object = MibTableColumn
mscAppnDnaOutDefaultPathReliability = _MscAppnDnaOutDefaultPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 12, 1, 14),
    _MscAppnDnaOutDefaultPathReliability_Type()
)
mscAppnDnaOutDefaultPathReliability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDnaOutDefaultPathReliability.setStatus("mandatory")


class _MscAppnDnaOutAccess_Type(Integer32):
    """Custom type mscAppnDnaOutAccess based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_MscAppnDnaOutAccess_Type.__name__ = "Integer32"
_MscAppnDnaOutAccess_Object = MibTableColumn
mscAppnDnaOutAccess = _MscAppnDnaOutAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 12, 1, 17),
    _MscAppnDnaOutAccess_Type()
)
mscAppnDnaOutAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDnaOutAccess.setStatus("mandatory")


class _MscAppnDnaDefaultTransferPriority_Type(Integer32):
    """Custom type mscAppnDnaDefaultTransferPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              9)
        )
    )
    namedValues = NamedValues(
        *(("high", 9),
          ("normal", 0))
    )


_MscAppnDnaDefaultTransferPriority_Type.__name__ = "Integer32"
_MscAppnDnaDefaultTransferPriority_Object = MibTableColumn
mscAppnDnaDefaultTransferPriority = _MscAppnDnaDefaultTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 12, 1, 18),
    _MscAppnDnaDefaultTransferPriority_Type()
)
mscAppnDnaDefaultTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDnaDefaultTransferPriority.setStatus("mandatory")


class _MscAppnDnaTransferPriorityOverRide_Type(Integer32):
    """Custom type mscAppnDnaTransferPriorityOverRide based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MscAppnDnaTransferPriorityOverRide_Type.__name__ = "Integer32"
_MscAppnDnaTransferPriorityOverRide_Object = MibTableColumn
mscAppnDnaTransferPriorityOverRide = _MscAppnDnaTransferPriorityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 12, 1, 19),
    _MscAppnDnaTransferPriorityOverRide_Type()
)
mscAppnDnaTransferPriorityOverRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDnaTransferPriorityOverRide.setStatus("mandatory")
_MscAppnDnaIncomingOptionsTable_Object = MibTable
mscAppnDnaIncomingOptionsTable = _MscAppnDnaIncomingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 13)
)
if mibBuilder.loadTexts:
    mscAppnDnaIncomingOptionsTable.setStatus("mandatory")
_MscAppnDnaIncomingOptionsEntry_Object = MibTableRow
mscAppnDnaIncomingOptionsEntry = _MscAppnDnaIncomingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 13, 1)
)
mscAppnDnaIncomingOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDnaIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDnaIncomingOptionsEntry.setStatus("mandatory")


class _MscAppnDnaIncAccess_Type(Integer32):
    """Custom type mscAppnDnaIncAccess based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_MscAppnDnaIncAccess_Type.__name__ = "Integer32"
_MscAppnDnaIncAccess_Object = MibTableColumn
mscAppnDnaIncAccess = _MscAppnDnaIncAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 13, 1, 9),
    _MscAppnDnaIncAccess_Type()
)
mscAppnDnaIncAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDnaIncAccess.setStatus("mandatory")
_MscAppnDnaCallOptionsTable_Object = MibTable
mscAppnDnaCallOptionsTable = _MscAppnDnaCallOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 14)
)
if mibBuilder.loadTexts:
    mscAppnDnaCallOptionsTable.setStatus("mandatory")
_MscAppnDnaCallOptionsEntry_Object = MibTableRow
mscAppnDnaCallOptionsEntry = _MscAppnDnaCallOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 14, 1)
)
mscAppnDnaCallOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDnaIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDnaCallOptionsEntry.setStatus("mandatory")


class _MscAppnDnaDefaultRecvFrmNetworkThruputClass_Type(Unsigned32):
    """Custom type mscAppnDnaDefaultRecvFrmNetworkThruputClass based on Unsigned32"""
    defaultValue = 13

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscAppnDnaDefaultRecvFrmNetworkThruputClass_Type.__name__ = "Unsigned32"
_MscAppnDnaDefaultRecvFrmNetworkThruputClass_Object = MibTableColumn
mscAppnDnaDefaultRecvFrmNetworkThruputClass = _MscAppnDnaDefaultRecvFrmNetworkThruputClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 14, 1, 5),
    _MscAppnDnaDefaultRecvFrmNetworkThruputClass_Type()
)
mscAppnDnaDefaultRecvFrmNetworkThruputClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDnaDefaultRecvFrmNetworkThruputClass.setStatus("mandatory")


class _MscAppnDnaDefaultSendToNetworkThruputClass_Type(Unsigned32):
    """Custom type mscAppnDnaDefaultSendToNetworkThruputClass based on Unsigned32"""
    defaultValue = 13

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscAppnDnaDefaultSendToNetworkThruputClass_Type.__name__ = "Unsigned32"
_MscAppnDnaDefaultSendToNetworkThruputClass_Object = MibTableColumn
mscAppnDnaDefaultSendToNetworkThruputClass = _MscAppnDnaDefaultSendToNetworkThruputClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 14, 1, 6),
    _MscAppnDnaDefaultSendToNetworkThruputClass_Type()
)
mscAppnDnaDefaultSendToNetworkThruputClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDnaDefaultSendToNetworkThruputClass.setStatus("mandatory")


class _MscAppnDnaDefaultRecvFrmNetworkWindowSize_Type(Unsigned32):
    """Custom type mscAppnDnaDefaultRecvFrmNetworkWindowSize based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_MscAppnDnaDefaultRecvFrmNetworkWindowSize_Type.__name__ = "Unsigned32"
_MscAppnDnaDefaultRecvFrmNetworkWindowSize_Object = MibTableColumn
mscAppnDnaDefaultRecvFrmNetworkWindowSize = _MscAppnDnaDefaultRecvFrmNetworkWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 14, 1, 7),
    _MscAppnDnaDefaultRecvFrmNetworkWindowSize_Type()
)
mscAppnDnaDefaultRecvFrmNetworkWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDnaDefaultRecvFrmNetworkWindowSize.setStatus("mandatory")


class _MscAppnDnaDefaultSendToNetworkWindowSize_Type(Unsigned32):
    """Custom type mscAppnDnaDefaultSendToNetworkWindowSize based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_MscAppnDnaDefaultSendToNetworkWindowSize_Type.__name__ = "Unsigned32"
_MscAppnDnaDefaultSendToNetworkWindowSize_Object = MibTableColumn
mscAppnDnaDefaultSendToNetworkWindowSize = _MscAppnDnaDefaultSendToNetworkWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 14, 1, 8),
    _MscAppnDnaDefaultSendToNetworkWindowSize_Type()
)
mscAppnDnaDefaultSendToNetworkWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDnaDefaultSendToNetworkWindowSize.setStatus("mandatory")


class _MscAppnDnaAccountClass_Type(Unsigned32):
    """Custom type mscAppnDnaAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnDnaAccountClass_Type.__name__ = "Unsigned32"
_MscAppnDnaAccountClass_Object = MibTableColumn
mscAppnDnaAccountClass = _MscAppnDnaAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 14, 1, 10),
    _MscAppnDnaAccountClass_Type()
)
mscAppnDnaAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDnaAccountClass.setStatus("mandatory")


class _MscAppnDnaAccountCollection_Type(OctetString):
    """Custom type mscAppnDnaAccountCollection based on OctetString"""
    defaultHexValue = "80"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAppnDnaAccountCollection_Type.__name__ = "OctetString"
_MscAppnDnaAccountCollection_Object = MibTableColumn
mscAppnDnaAccountCollection = _MscAppnDnaAccountCollection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 14, 1, 11),
    _MscAppnDnaAccountCollection_Type()
)
mscAppnDnaAccountCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDnaAccountCollection.setStatus("mandatory")


class _MscAppnDnaServiceExchange_Type(Unsigned32):
    """Custom type mscAppnDnaServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnDnaServiceExchange_Type.__name__ = "Unsigned32"
_MscAppnDnaServiceExchange_Object = MibTableColumn
mscAppnDnaServiceExchange = _MscAppnDnaServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 2, 14, 1, 12),
    _MscAppnDnaServiceExchange_Type()
)
mscAppnDnaServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDnaServiceExchange.setStatus("mandatory")
_MscAppnDlci_ObjectIdentity = ObjectIdentity
mscAppnDlci = _MscAppnDlci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3)
)
_MscAppnDlciRowStatusTable_Object = MibTable
mscAppnDlciRowStatusTable = _MscAppnDlciRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 1)
)
if mibBuilder.loadTexts:
    mscAppnDlciRowStatusTable.setStatus("mandatory")
_MscAppnDlciRowStatusEntry_Object = MibTableRow
mscAppnDlciRowStatusEntry = _MscAppnDlciRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 1, 1)
)
mscAppnDlciRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDlciRowStatusEntry.setStatus("mandatory")
_MscAppnDlciRowStatus_Type = RowStatus
_MscAppnDlciRowStatus_Object = MibTableColumn
mscAppnDlciRowStatus = _MscAppnDlciRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 1, 1, 1),
    _MscAppnDlciRowStatus_Type()
)
mscAppnDlciRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciRowStatus.setStatus("mandatory")
_MscAppnDlciComponentName_Type = DisplayString
_MscAppnDlciComponentName_Object = MibTableColumn
mscAppnDlciComponentName = _MscAppnDlciComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 1, 1, 2),
    _MscAppnDlciComponentName_Type()
)
mscAppnDlciComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciComponentName.setStatus("mandatory")
_MscAppnDlciStorageType_Type = StorageType
_MscAppnDlciStorageType_Object = MibTableColumn
mscAppnDlciStorageType = _MscAppnDlciStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 1, 1, 4),
    _MscAppnDlciStorageType_Type()
)
mscAppnDlciStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciStorageType.setStatus("mandatory")


class _MscAppnDlciIndex_Type(Integer32):
    """Custom type mscAppnDlciIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 4095),
    )


_MscAppnDlciIndex_Type.__name__ = "Integer32"
_MscAppnDlciIndex_Object = MibTableColumn
mscAppnDlciIndex = _MscAppnDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 1, 1, 10),
    _MscAppnDlciIndex_Type()
)
mscAppnDlciIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnDlciIndex.setStatus("mandatory")
_MscAppnDlciDc_ObjectIdentity = ObjectIdentity
mscAppnDlciDc = _MscAppnDlciDc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 2)
)
_MscAppnDlciDcRowStatusTable_Object = MibTable
mscAppnDlciDcRowStatusTable = _MscAppnDlciDcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscAppnDlciDcRowStatusTable.setStatus("mandatory")
_MscAppnDlciDcRowStatusEntry_Object = MibTableRow
mscAppnDlciDcRowStatusEntry = _MscAppnDlciDcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 2, 1, 1)
)
mscAppnDlciDcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciDcIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDlciDcRowStatusEntry.setStatus("mandatory")
_MscAppnDlciDcRowStatus_Type = RowStatus
_MscAppnDlciDcRowStatus_Object = MibTableColumn
mscAppnDlciDcRowStatus = _MscAppnDlciDcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 2, 1, 1, 1),
    _MscAppnDlciDcRowStatus_Type()
)
mscAppnDlciDcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciDcRowStatus.setStatus("mandatory")
_MscAppnDlciDcComponentName_Type = DisplayString
_MscAppnDlciDcComponentName_Object = MibTableColumn
mscAppnDlciDcComponentName = _MscAppnDlciDcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 2, 1, 1, 2),
    _MscAppnDlciDcComponentName_Type()
)
mscAppnDlciDcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciDcComponentName.setStatus("mandatory")
_MscAppnDlciDcStorageType_Type = StorageType
_MscAppnDlciDcStorageType_Object = MibTableColumn
mscAppnDlciDcStorageType = _MscAppnDlciDcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 2, 1, 1, 4),
    _MscAppnDlciDcStorageType_Type()
)
mscAppnDlciDcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciDcStorageType.setStatus("mandatory")
_MscAppnDlciDcIndex_Type = NonReplicated
_MscAppnDlciDcIndex_Object = MibTableColumn
mscAppnDlciDcIndex = _MscAppnDlciDcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 2, 1, 1, 10),
    _MscAppnDlciDcIndex_Type()
)
mscAppnDlciDcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnDlciDcIndex.setStatus("mandatory")
_MscAppnDlciDcOptionsTable_Object = MibTable
mscAppnDlciDcOptionsTable = _MscAppnDlciDcOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscAppnDlciDcOptionsTable.setStatus("mandatory")
_MscAppnDlciDcOptionsEntry_Object = MibTableRow
mscAppnDlciDcOptionsEntry = _MscAppnDlciDcOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 2, 10, 1)
)
mscAppnDlciDcOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciDcIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDlciDcOptionsEntry.setStatus("mandatory")


class _MscAppnDlciDcRemoteNpi_Type(Integer32):
    """Custom type mscAppnDlciDcRemoteNpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_MscAppnDlciDcRemoteNpi_Type.__name__ = "Integer32"
_MscAppnDlciDcRemoteNpi_Object = MibTableColumn
mscAppnDlciDcRemoteNpi = _MscAppnDlciDcRemoteNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 2, 10, 1, 3),
    _MscAppnDlciDcRemoteNpi_Type()
)
mscAppnDlciDcRemoteNpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciDcRemoteNpi.setStatus("mandatory")


class _MscAppnDlciDcRemoteDna_Type(DigitString):
    """Custom type mscAppnDlciDcRemoteDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscAppnDlciDcRemoteDna_Type.__name__ = "DigitString"
_MscAppnDlciDcRemoteDna_Object = MibTableColumn
mscAppnDlciDcRemoteDna = _MscAppnDlciDcRemoteDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 2, 10, 1, 4),
    _MscAppnDlciDcRemoteDna_Type()
)
mscAppnDlciDcRemoteDna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciDcRemoteDna.setStatus("mandatory")


class _MscAppnDlciDcRemoteDlci_Type(Unsigned32):
    """Custom type mscAppnDlciDcRemoteDlci based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MscAppnDlciDcRemoteDlci_Type.__name__ = "Unsigned32"
_MscAppnDlciDcRemoteDlci_Object = MibTableColumn
mscAppnDlciDcRemoteDlci = _MscAppnDlciDcRemoteDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 2, 10, 1, 5),
    _MscAppnDlciDcRemoteDlci_Type()
)
mscAppnDlciDcRemoteDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciDcRemoteDlci.setStatus("mandatory")


class _MscAppnDlciDcType_Type(Integer32):
    """Custom type mscAppnDlciDcType based on Integer32"""
    defaultValue = 1

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
        *(("permanentBackupSlave", 3),
          ("permanentMaster", 1),
          ("permanentSlave", 2),
          ("permanentSlaveWithBackup", 4))
    )


_MscAppnDlciDcType_Type.__name__ = "Integer32"
_MscAppnDlciDcType_Object = MibTableColumn
mscAppnDlciDcType = _MscAppnDlciDcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 2, 10, 1, 6),
    _MscAppnDlciDcType_Type()
)
mscAppnDlciDcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciDcType.setStatus("mandatory")


class _MscAppnDlciDcTransferPriority_Type(Integer32):
    """Custom type mscAppnDlciDcTransferPriority based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              9,
              255)
        )
    )
    namedValues = NamedValues(
        *(("high", 9),
          ("normal", 0),
          ("useDnaDefTP", 255))
    )


_MscAppnDlciDcTransferPriority_Type.__name__ = "Integer32"
_MscAppnDlciDcTransferPriority_Object = MibTableColumn
mscAppnDlciDcTransferPriority = _MscAppnDlciDcTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 2, 10, 1, 9),
    _MscAppnDlciDcTransferPriority_Type()
)
mscAppnDlciDcTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciDcTransferPriority.setStatus("mandatory")


class _MscAppnDlciDcDiscardPriority_Type(Integer32):
    """Custom type mscAppnDlciDcDiscardPriority based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("normal", 0),
          ("useDnaDefPriority", 3))
    )


_MscAppnDlciDcDiscardPriority_Type.__name__ = "Integer32"
_MscAppnDlciDcDiscardPriority_Object = MibTableColumn
mscAppnDlciDcDiscardPriority = _MscAppnDlciDcDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 2, 10, 1, 10),
    _MscAppnDlciDcDiscardPriority_Type()
)
mscAppnDlciDcDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciDcDiscardPriority.setStatus("mandatory")
_MscAppnDlciDcNfaTable_Object = MibTable
mscAppnDlciDcNfaTable = _MscAppnDlciDcNfaTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 2, 283)
)
if mibBuilder.loadTexts:
    mscAppnDlciDcNfaTable.setStatus("obsolete")
_MscAppnDlciDcNfaEntry_Object = MibTableRow
mscAppnDlciDcNfaEntry = _MscAppnDlciDcNfaEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 2, 283, 1)
)
mscAppnDlciDcNfaEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciDcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciDcNfaIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDlciDcNfaEntry.setStatus("obsolete")


class _MscAppnDlciDcNfaIndex_Type(Integer32):
    """Custom type mscAppnDlciDcNfaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(48, 48),
    )


_MscAppnDlciDcNfaIndex_Type.__name__ = "Integer32"
_MscAppnDlciDcNfaIndex_Object = MibTableColumn
mscAppnDlciDcNfaIndex = _MscAppnDlciDcNfaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 2, 283, 1, 1),
    _MscAppnDlciDcNfaIndex_Type()
)
mscAppnDlciDcNfaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnDlciDcNfaIndex.setStatus("obsolete")


class _MscAppnDlciDcNfaValue_Type(HexString):
    """Custom type mscAppnDlciDcNfaValue based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MscAppnDlciDcNfaValue_Type.__name__ = "HexString"
_MscAppnDlciDcNfaValue_Object = MibTableColumn
mscAppnDlciDcNfaValue = _MscAppnDlciDcNfaValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 2, 283, 1, 2),
    _MscAppnDlciDcNfaValue_Type()
)
mscAppnDlciDcNfaValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciDcNfaValue.setStatus("obsolete")
_MscAppnDlciDcNfaRowStatus_Type = RowStatus
_MscAppnDlciDcNfaRowStatus_Object = MibTableColumn
mscAppnDlciDcNfaRowStatus = _MscAppnDlciDcNfaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 2, 283, 1, 3),
    _MscAppnDlciDcNfaRowStatus_Type()
)
mscAppnDlciDcNfaRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscAppnDlciDcNfaRowStatus.setStatus("obsolete")
_MscAppnDlciVc_ObjectIdentity = ObjectIdentity
mscAppnDlciVc = _MscAppnDlciVc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3)
)
_MscAppnDlciVcRowStatusTable_Object = MibTable
mscAppnDlciVcRowStatusTable = _MscAppnDlciVcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 1)
)
if mibBuilder.loadTexts:
    mscAppnDlciVcRowStatusTable.setStatus("mandatory")
_MscAppnDlciVcRowStatusEntry_Object = MibTableRow
mscAppnDlciVcRowStatusEntry = _MscAppnDlciVcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 1, 1)
)
mscAppnDlciVcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciVcIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDlciVcRowStatusEntry.setStatus("mandatory")
_MscAppnDlciVcRowStatus_Type = RowStatus
_MscAppnDlciVcRowStatus_Object = MibTableColumn
mscAppnDlciVcRowStatus = _MscAppnDlciVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 1, 1, 1),
    _MscAppnDlciVcRowStatus_Type()
)
mscAppnDlciVcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcRowStatus.setStatus("mandatory")
_MscAppnDlciVcComponentName_Type = DisplayString
_MscAppnDlciVcComponentName_Object = MibTableColumn
mscAppnDlciVcComponentName = _MscAppnDlciVcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 1, 1, 2),
    _MscAppnDlciVcComponentName_Type()
)
mscAppnDlciVcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcComponentName.setStatus("mandatory")
_MscAppnDlciVcStorageType_Type = StorageType
_MscAppnDlciVcStorageType_Object = MibTableColumn
mscAppnDlciVcStorageType = _MscAppnDlciVcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 1, 1, 4),
    _MscAppnDlciVcStorageType_Type()
)
mscAppnDlciVcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcStorageType.setStatus("mandatory")
_MscAppnDlciVcIndex_Type = NonReplicated
_MscAppnDlciVcIndex_Object = MibTableColumn
mscAppnDlciVcIndex = _MscAppnDlciVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 1, 1, 10),
    _MscAppnDlciVcIndex_Type()
)
mscAppnDlciVcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnDlciVcIndex.setStatus("mandatory")
_MscAppnDlciVcCadTable_Object = MibTable
mscAppnDlciVcCadTable = _MscAppnDlciVcCadTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 10)
)
if mibBuilder.loadTexts:
    mscAppnDlciVcCadTable.setStatus("mandatory")
_MscAppnDlciVcCadEntry_Object = MibTableRow
mscAppnDlciVcCadEntry = _MscAppnDlciVcCadEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 10, 1)
)
mscAppnDlciVcCadEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciVcIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDlciVcCadEntry.setStatus("mandatory")


class _MscAppnDlciVcType_Type(Integer32):
    """Custom type mscAppnDlciVcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("spvc", 2),
          ("svc", 0))
    )


_MscAppnDlciVcType_Type.__name__ = "Integer32"
_MscAppnDlciVcType_Object = MibTableColumn
mscAppnDlciVcType = _MscAppnDlciVcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 10, 1, 1),
    _MscAppnDlciVcType_Type()
)
mscAppnDlciVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcType.setStatus("mandatory")


class _MscAppnDlciVcState_Type(Integer32):
    """Custom type mscAppnDlciVcState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("creating", 0),
          ("dataTransferP4", 4),
          ("dceClearIndicationP7", 7),
          ("dceWaitingP3", 3),
          ("dteClearRequestP6", 6),
          ("dteWaitingP2", 2),
          ("readyP1", 1),
          ("termination", 8),
          ("unsupportedP5", 5))
    )


_MscAppnDlciVcState_Type.__name__ = "Integer32"
_MscAppnDlciVcState_Object = MibTableColumn
mscAppnDlciVcState = _MscAppnDlciVcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 10, 1, 2),
    _MscAppnDlciVcState_Type()
)
mscAppnDlciVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcState.setStatus("mandatory")


class _MscAppnDlciVcPreviousState_Type(Integer32):
    """Custom type mscAppnDlciVcPreviousState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("creating", 0),
          ("dataTransferP4", 4),
          ("dceClearIndicationP7", 7),
          ("dceWaitingP3", 3),
          ("dteClearRequestP6", 6),
          ("dteWaitingP2", 2),
          ("readyP1", 1),
          ("termination", 8),
          ("unsupportedP5", 5))
    )


_MscAppnDlciVcPreviousState_Type.__name__ = "Integer32"
_MscAppnDlciVcPreviousState_Object = MibTableColumn
mscAppnDlciVcPreviousState = _MscAppnDlciVcPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 10, 1, 3),
    _MscAppnDlciVcPreviousState_Type()
)
mscAppnDlciVcPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcPreviousState.setStatus("mandatory")


class _MscAppnDlciVcDiagnosticCode_Type(Unsigned32):
    """Custom type mscAppnDlciVcDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnDlciVcDiagnosticCode_Type.__name__ = "Unsigned32"
_MscAppnDlciVcDiagnosticCode_Object = MibTableColumn
mscAppnDlciVcDiagnosticCode = _MscAppnDlciVcDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 10, 1, 4),
    _MscAppnDlciVcDiagnosticCode_Type()
)
mscAppnDlciVcDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcDiagnosticCode.setStatus("mandatory")


class _MscAppnDlciVcPreviousDiagnosticCode_Type(Unsigned32):
    """Custom type mscAppnDlciVcPreviousDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnDlciVcPreviousDiagnosticCode_Type.__name__ = "Unsigned32"
_MscAppnDlciVcPreviousDiagnosticCode_Object = MibTableColumn
mscAppnDlciVcPreviousDiagnosticCode = _MscAppnDlciVcPreviousDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 10, 1, 5),
    _MscAppnDlciVcPreviousDiagnosticCode_Type()
)
mscAppnDlciVcPreviousDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcPreviousDiagnosticCode.setStatus("mandatory")


class _MscAppnDlciVcCalledNpi_Type(Integer32):
    """Custom type mscAppnDlciVcCalledNpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_MscAppnDlciVcCalledNpi_Type.__name__ = "Integer32"
_MscAppnDlciVcCalledNpi_Object = MibTableColumn
mscAppnDlciVcCalledNpi = _MscAppnDlciVcCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 10, 1, 6),
    _MscAppnDlciVcCalledNpi_Type()
)
mscAppnDlciVcCalledNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcCalledNpi.setStatus("mandatory")


class _MscAppnDlciVcCalledDna_Type(DigitString):
    """Custom type mscAppnDlciVcCalledDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscAppnDlciVcCalledDna_Type.__name__ = "DigitString"
_MscAppnDlciVcCalledDna_Object = MibTableColumn
mscAppnDlciVcCalledDna = _MscAppnDlciVcCalledDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 10, 1, 7),
    _MscAppnDlciVcCalledDna_Type()
)
mscAppnDlciVcCalledDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcCalledDna.setStatus("mandatory")


class _MscAppnDlciVcCalledLcn_Type(Unsigned32):
    """Custom type mscAppnDlciVcCalledLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscAppnDlciVcCalledLcn_Type.__name__ = "Unsigned32"
_MscAppnDlciVcCalledLcn_Object = MibTableColumn
mscAppnDlciVcCalledLcn = _MscAppnDlciVcCalledLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 10, 1, 8),
    _MscAppnDlciVcCalledLcn_Type()
)
mscAppnDlciVcCalledLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcCalledLcn.setStatus("mandatory")


class _MscAppnDlciVcCallingNpi_Type(Integer32):
    """Custom type mscAppnDlciVcCallingNpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_MscAppnDlciVcCallingNpi_Type.__name__ = "Integer32"
_MscAppnDlciVcCallingNpi_Object = MibTableColumn
mscAppnDlciVcCallingNpi = _MscAppnDlciVcCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 10, 1, 9),
    _MscAppnDlciVcCallingNpi_Type()
)
mscAppnDlciVcCallingNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcCallingNpi.setStatus("mandatory")


class _MscAppnDlciVcCallingDna_Type(DigitString):
    """Custom type mscAppnDlciVcCallingDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscAppnDlciVcCallingDna_Type.__name__ = "DigitString"
_MscAppnDlciVcCallingDna_Object = MibTableColumn
mscAppnDlciVcCallingDna = _MscAppnDlciVcCallingDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 10, 1, 10),
    _MscAppnDlciVcCallingDna_Type()
)
mscAppnDlciVcCallingDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcCallingDna.setStatus("mandatory")


class _MscAppnDlciVcCallingLcn_Type(Unsigned32):
    """Custom type mscAppnDlciVcCallingLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscAppnDlciVcCallingLcn_Type.__name__ = "Unsigned32"
_MscAppnDlciVcCallingLcn_Object = MibTableColumn
mscAppnDlciVcCallingLcn = _MscAppnDlciVcCallingLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 10, 1, 11),
    _MscAppnDlciVcCallingLcn_Type()
)
mscAppnDlciVcCallingLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcCallingLcn.setStatus("mandatory")


class _MscAppnDlciVcAccountingEnabled_Type(Integer32):
    """Custom type mscAppnDlciVcAccountingEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 0))
    )


_MscAppnDlciVcAccountingEnabled_Type.__name__ = "Integer32"
_MscAppnDlciVcAccountingEnabled_Object = MibTableColumn
mscAppnDlciVcAccountingEnabled = _MscAppnDlciVcAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 10, 1, 12),
    _MscAppnDlciVcAccountingEnabled_Type()
)
mscAppnDlciVcAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcAccountingEnabled.setStatus("mandatory")


class _MscAppnDlciVcFastSelectCall_Type(Integer32):
    """Custom type mscAppnDlciVcFastSelectCall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MscAppnDlciVcFastSelectCall_Type.__name__ = "Integer32"
_MscAppnDlciVcFastSelectCall_Object = MibTableColumn
mscAppnDlciVcFastSelectCall = _MscAppnDlciVcFastSelectCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 10, 1, 13),
    _MscAppnDlciVcFastSelectCall_Type()
)
mscAppnDlciVcFastSelectCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcFastSelectCall.setStatus("mandatory")


class _MscAppnDlciVcPathReliability_Type(Integer32):
    """Custom type mscAppnDlciVcPathReliability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 0),
          ("normal", 1))
    )


_MscAppnDlciVcPathReliability_Type.__name__ = "Integer32"
_MscAppnDlciVcPathReliability_Object = MibTableColumn
mscAppnDlciVcPathReliability = _MscAppnDlciVcPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 10, 1, 19),
    _MscAppnDlciVcPathReliability_Type()
)
mscAppnDlciVcPathReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcPathReliability.setStatus("mandatory")


class _MscAppnDlciVcAccountingEnd_Type(Integer32):
    """Custom type mscAppnDlciVcAccountingEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("calledEnd", 1),
          ("callingEnd", 0))
    )


_MscAppnDlciVcAccountingEnd_Type.__name__ = "Integer32"
_MscAppnDlciVcAccountingEnd_Object = MibTableColumn
mscAppnDlciVcAccountingEnd = _MscAppnDlciVcAccountingEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 10, 1, 20),
    _MscAppnDlciVcAccountingEnd_Type()
)
mscAppnDlciVcAccountingEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcAccountingEnd.setStatus("mandatory")


class _MscAppnDlciVcPriority_Type(Integer32):
    """Custom type mscAppnDlciVcPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("normal", 0))
    )


_MscAppnDlciVcPriority_Type.__name__ = "Integer32"
_MscAppnDlciVcPriority_Object = MibTableColumn
mscAppnDlciVcPriority = _MscAppnDlciVcPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 10, 1, 21),
    _MscAppnDlciVcPriority_Type()
)
mscAppnDlciVcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcPriority.setStatus("mandatory")


class _MscAppnDlciVcSegmentSize_Type(Unsigned32):
    """Custom type mscAppnDlciVcSegmentSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscAppnDlciVcSegmentSize_Type.__name__ = "Unsigned32"
_MscAppnDlciVcSegmentSize_Object = MibTableColumn
mscAppnDlciVcSegmentSize = _MscAppnDlciVcSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 10, 1, 22),
    _MscAppnDlciVcSegmentSize_Type()
)
mscAppnDlciVcSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcSegmentSize.setStatus("mandatory")


class _MscAppnDlciVcMaxSubnetPktSize_Type(Unsigned32):
    """Custom type mscAppnDlciVcMaxSubnetPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscAppnDlciVcMaxSubnetPktSize_Type.__name__ = "Unsigned32"
_MscAppnDlciVcMaxSubnetPktSize_Object = MibTableColumn
mscAppnDlciVcMaxSubnetPktSize = _MscAppnDlciVcMaxSubnetPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 10, 1, 27),
    _MscAppnDlciVcMaxSubnetPktSize_Type()
)
mscAppnDlciVcMaxSubnetPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcMaxSubnetPktSize.setStatus("mandatory")


class _MscAppnDlciVcRcosToNetwork_Type(Integer32):
    """Custom type mscAppnDlciVcRcosToNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delay", 1),
          ("multimedia", 2),
          ("throughput", 0))
    )


_MscAppnDlciVcRcosToNetwork_Type.__name__ = "Integer32"
_MscAppnDlciVcRcosToNetwork_Object = MibTableColumn
mscAppnDlciVcRcosToNetwork = _MscAppnDlciVcRcosToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 10, 1, 28),
    _MscAppnDlciVcRcosToNetwork_Type()
)
mscAppnDlciVcRcosToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcRcosToNetwork.setStatus("mandatory")


class _MscAppnDlciVcRcosFromNetwork_Type(Integer32):
    """Custom type mscAppnDlciVcRcosFromNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delay", 1),
          ("multimedia", 2),
          ("throughput", 0))
    )


_MscAppnDlciVcRcosFromNetwork_Type.__name__ = "Integer32"
_MscAppnDlciVcRcosFromNetwork_Object = MibTableColumn
mscAppnDlciVcRcosFromNetwork = _MscAppnDlciVcRcosFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 10, 1, 29),
    _MscAppnDlciVcRcosFromNetwork_Type()
)
mscAppnDlciVcRcosFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcRcosFromNetwork.setStatus("mandatory")


class _MscAppnDlciVcEmissionPriorityToNetwork_Type(Integer32):
    """Custom type mscAppnDlciVcEmissionPriorityToNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("interrupting", 2),
          ("normal", 0))
    )


_MscAppnDlciVcEmissionPriorityToNetwork_Type.__name__ = "Integer32"
_MscAppnDlciVcEmissionPriorityToNetwork_Object = MibTableColumn
mscAppnDlciVcEmissionPriorityToNetwork = _MscAppnDlciVcEmissionPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 10, 1, 30),
    _MscAppnDlciVcEmissionPriorityToNetwork_Type()
)
mscAppnDlciVcEmissionPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcEmissionPriorityToNetwork.setStatus("mandatory")


class _MscAppnDlciVcEmissionPriorityFromNetwork_Type(Integer32):
    """Custom type mscAppnDlciVcEmissionPriorityFromNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("interrupting", 2),
          ("normal", 0))
    )


_MscAppnDlciVcEmissionPriorityFromNetwork_Type.__name__ = "Integer32"
_MscAppnDlciVcEmissionPriorityFromNetwork_Object = MibTableColumn
mscAppnDlciVcEmissionPriorityFromNetwork = _MscAppnDlciVcEmissionPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 10, 1, 31),
    _MscAppnDlciVcEmissionPriorityFromNetwork_Type()
)
mscAppnDlciVcEmissionPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcEmissionPriorityFromNetwork.setStatus("mandatory")


class _MscAppnDlciVcDataPath_Type(AsciiString):
    """Custom type mscAppnDlciVcDataPath based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscAppnDlciVcDataPath_Type.__name__ = "AsciiString"
_MscAppnDlciVcDataPath_Object = MibTableColumn
mscAppnDlciVcDataPath = _MscAppnDlciVcDataPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 10, 1, 32),
    _MscAppnDlciVcDataPath_Type()
)
mscAppnDlciVcDataPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcDataPath.setStatus("mandatory")
_MscAppnDlciVcIntdTable_Object = MibTable
mscAppnDlciVcIntdTable = _MscAppnDlciVcIntdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 11)
)
if mibBuilder.loadTexts:
    mscAppnDlciVcIntdTable.setStatus("mandatory")
_MscAppnDlciVcIntdEntry_Object = MibTableRow
mscAppnDlciVcIntdEntry = _MscAppnDlciVcIntdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 11, 1)
)
mscAppnDlciVcIntdEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciVcIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDlciVcIntdEntry.setStatus("mandatory")


class _MscAppnDlciVcCallReferenceNumber_Type(Hex):
    """Custom type mscAppnDlciVcCallReferenceNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscAppnDlciVcCallReferenceNumber_Type.__name__ = "Hex"
_MscAppnDlciVcCallReferenceNumber_Object = MibTableColumn
mscAppnDlciVcCallReferenceNumber = _MscAppnDlciVcCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 11, 1, 1),
    _MscAppnDlciVcCallReferenceNumber_Type()
)
mscAppnDlciVcCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcCallReferenceNumber.setStatus("mandatory")


class _MscAppnDlciVcElapsedTimeTillNow_Type(Unsigned32):
    """Custom type mscAppnDlciVcElapsedTimeTillNow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscAppnDlciVcElapsedTimeTillNow_Type.__name__ = "Unsigned32"
_MscAppnDlciVcElapsedTimeTillNow_Object = MibTableColumn
mscAppnDlciVcElapsedTimeTillNow = _MscAppnDlciVcElapsedTimeTillNow_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 11, 1, 2),
    _MscAppnDlciVcElapsedTimeTillNow_Type()
)
mscAppnDlciVcElapsedTimeTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcElapsedTimeTillNow.setStatus("mandatory")


class _MscAppnDlciVcSegmentsRx_Type(Unsigned32):
    """Custom type mscAppnDlciVcSegmentsRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscAppnDlciVcSegmentsRx_Type.__name__ = "Unsigned32"
_MscAppnDlciVcSegmentsRx_Object = MibTableColumn
mscAppnDlciVcSegmentsRx = _MscAppnDlciVcSegmentsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 11, 1, 3),
    _MscAppnDlciVcSegmentsRx_Type()
)
mscAppnDlciVcSegmentsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcSegmentsRx.setStatus("mandatory")


class _MscAppnDlciVcSegmentsSent_Type(Unsigned32):
    """Custom type mscAppnDlciVcSegmentsSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscAppnDlciVcSegmentsSent_Type.__name__ = "Unsigned32"
_MscAppnDlciVcSegmentsSent_Object = MibTableColumn
mscAppnDlciVcSegmentsSent = _MscAppnDlciVcSegmentsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 11, 1, 4),
    _MscAppnDlciVcSegmentsSent_Type()
)
mscAppnDlciVcSegmentsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcSegmentsSent.setStatus("mandatory")


class _MscAppnDlciVcStartTime_Type(EnterpriseDateAndTime):
    """Custom type mscAppnDlciVcStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscAppnDlciVcStartTime_Type.__name__ = "EnterpriseDateAndTime"
_MscAppnDlciVcStartTime_Object = MibTableColumn
mscAppnDlciVcStartTime = _MscAppnDlciVcStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 11, 1, 5),
    _MscAppnDlciVcStartTime_Type()
)
mscAppnDlciVcStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcStartTime.setStatus("mandatory")
_MscAppnDlciVcFrdTable_Object = MibTable
mscAppnDlciVcFrdTable = _MscAppnDlciVcFrdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 12)
)
if mibBuilder.loadTexts:
    mscAppnDlciVcFrdTable.setStatus("mandatory")
_MscAppnDlciVcFrdEntry_Object = MibTableRow
mscAppnDlciVcFrdEntry = _MscAppnDlciVcFrdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 12, 1)
)
mscAppnDlciVcFrdEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciVcIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDlciVcFrdEntry.setStatus("mandatory")


class _MscAppnDlciVcFrmCongestedToSubnet_Type(Unsigned32):
    """Custom type mscAppnDlciVcFrmCongestedToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscAppnDlciVcFrmCongestedToSubnet_Type.__name__ = "Unsigned32"
_MscAppnDlciVcFrmCongestedToSubnet_Object = MibTableColumn
mscAppnDlciVcFrmCongestedToSubnet = _MscAppnDlciVcFrmCongestedToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 12, 1, 2),
    _MscAppnDlciVcFrmCongestedToSubnet_Type()
)
mscAppnDlciVcFrmCongestedToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcFrmCongestedToSubnet.setStatus("mandatory")


class _MscAppnDlciVcCannotForwardToSubnet_Type(Unsigned32):
    """Custom type mscAppnDlciVcCannotForwardToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscAppnDlciVcCannotForwardToSubnet_Type.__name__ = "Unsigned32"
_MscAppnDlciVcCannotForwardToSubnet_Object = MibTableColumn
mscAppnDlciVcCannotForwardToSubnet = _MscAppnDlciVcCannotForwardToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 12, 1, 3),
    _MscAppnDlciVcCannotForwardToSubnet_Type()
)
mscAppnDlciVcCannotForwardToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcCannotForwardToSubnet.setStatus("mandatory")


class _MscAppnDlciVcNotDataXferToSubnet_Type(Unsigned32):
    """Custom type mscAppnDlciVcNotDataXferToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscAppnDlciVcNotDataXferToSubnet_Type.__name__ = "Unsigned32"
_MscAppnDlciVcNotDataXferToSubnet_Object = MibTableColumn
mscAppnDlciVcNotDataXferToSubnet = _MscAppnDlciVcNotDataXferToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 12, 1, 4),
    _MscAppnDlciVcNotDataXferToSubnet_Type()
)
mscAppnDlciVcNotDataXferToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcNotDataXferToSubnet.setStatus("mandatory")


class _MscAppnDlciVcOutOfRangeFrmFromSubnet_Type(Unsigned32):
    """Custom type mscAppnDlciVcOutOfRangeFrmFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscAppnDlciVcOutOfRangeFrmFromSubnet_Type.__name__ = "Unsigned32"
_MscAppnDlciVcOutOfRangeFrmFromSubnet_Object = MibTableColumn
mscAppnDlciVcOutOfRangeFrmFromSubnet = _MscAppnDlciVcOutOfRangeFrmFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 12, 1, 5),
    _MscAppnDlciVcOutOfRangeFrmFromSubnet_Type()
)
mscAppnDlciVcOutOfRangeFrmFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcOutOfRangeFrmFromSubnet.setStatus("mandatory")


class _MscAppnDlciVcCombErrorsFromSubnet_Type(Unsigned32):
    """Custom type mscAppnDlciVcCombErrorsFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscAppnDlciVcCombErrorsFromSubnet_Type.__name__ = "Unsigned32"
_MscAppnDlciVcCombErrorsFromSubnet_Object = MibTableColumn
mscAppnDlciVcCombErrorsFromSubnet = _MscAppnDlciVcCombErrorsFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 12, 1, 6),
    _MscAppnDlciVcCombErrorsFromSubnet_Type()
)
mscAppnDlciVcCombErrorsFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcCombErrorsFromSubnet.setStatus("mandatory")


class _MscAppnDlciVcDuplicatesFromSubnet_Type(Unsigned32):
    """Custom type mscAppnDlciVcDuplicatesFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscAppnDlciVcDuplicatesFromSubnet_Type.__name__ = "Unsigned32"
_MscAppnDlciVcDuplicatesFromSubnet_Object = MibTableColumn
mscAppnDlciVcDuplicatesFromSubnet = _MscAppnDlciVcDuplicatesFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 12, 1, 7),
    _MscAppnDlciVcDuplicatesFromSubnet_Type()
)
mscAppnDlciVcDuplicatesFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcDuplicatesFromSubnet.setStatus("mandatory")


class _MscAppnDlciVcNotDataXferFromSubnet_Type(Unsigned32):
    """Custom type mscAppnDlciVcNotDataXferFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscAppnDlciVcNotDataXferFromSubnet_Type.__name__ = "Unsigned32"
_MscAppnDlciVcNotDataXferFromSubnet_Object = MibTableColumn
mscAppnDlciVcNotDataXferFromSubnet = _MscAppnDlciVcNotDataXferFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 12, 1, 8),
    _MscAppnDlciVcNotDataXferFromSubnet_Type()
)
mscAppnDlciVcNotDataXferFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcNotDataXferFromSubnet.setStatus("mandatory")


class _MscAppnDlciVcFrmLossTimeouts_Type(Unsigned32):
    """Custom type mscAppnDlciVcFrmLossTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscAppnDlciVcFrmLossTimeouts_Type.__name__ = "Unsigned32"
_MscAppnDlciVcFrmLossTimeouts_Object = MibTableColumn
mscAppnDlciVcFrmLossTimeouts = _MscAppnDlciVcFrmLossTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 12, 1, 9),
    _MscAppnDlciVcFrmLossTimeouts_Type()
)
mscAppnDlciVcFrmLossTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcFrmLossTimeouts.setStatus("mandatory")


class _MscAppnDlciVcOoSeqByteCntExceeded_Type(Unsigned32):
    """Custom type mscAppnDlciVcOoSeqByteCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscAppnDlciVcOoSeqByteCntExceeded_Type.__name__ = "Unsigned32"
_MscAppnDlciVcOoSeqByteCntExceeded_Object = MibTableColumn
mscAppnDlciVcOoSeqByteCntExceeded = _MscAppnDlciVcOoSeqByteCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 12, 1, 10),
    _MscAppnDlciVcOoSeqByteCntExceeded_Type()
)
mscAppnDlciVcOoSeqByteCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcOoSeqByteCntExceeded.setStatus("mandatory")


class _MscAppnDlciVcPeakOoSeqPktCount_Type(Unsigned32):
    """Custom type mscAppnDlciVcPeakOoSeqPktCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscAppnDlciVcPeakOoSeqPktCount_Type.__name__ = "Unsigned32"
_MscAppnDlciVcPeakOoSeqPktCount_Object = MibTableColumn
mscAppnDlciVcPeakOoSeqPktCount = _MscAppnDlciVcPeakOoSeqPktCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 12, 1, 11),
    _MscAppnDlciVcPeakOoSeqPktCount_Type()
)
mscAppnDlciVcPeakOoSeqPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcPeakOoSeqPktCount.setStatus("mandatory")


class _MscAppnDlciVcPeakOoSeqFrmForwarded_Type(Unsigned32):
    """Custom type mscAppnDlciVcPeakOoSeqFrmForwarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscAppnDlciVcPeakOoSeqFrmForwarded_Type.__name__ = "Unsigned32"
_MscAppnDlciVcPeakOoSeqFrmForwarded_Object = MibTableColumn
mscAppnDlciVcPeakOoSeqFrmForwarded = _MscAppnDlciVcPeakOoSeqFrmForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 12, 1, 12),
    _MscAppnDlciVcPeakOoSeqFrmForwarded_Type()
)
mscAppnDlciVcPeakOoSeqFrmForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcPeakOoSeqFrmForwarded.setStatus("mandatory")


class _MscAppnDlciVcSendSequenceNumber_Type(Unsigned32):
    """Custom type mscAppnDlciVcSendSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscAppnDlciVcSendSequenceNumber_Type.__name__ = "Unsigned32"
_MscAppnDlciVcSendSequenceNumber_Object = MibTableColumn
mscAppnDlciVcSendSequenceNumber = _MscAppnDlciVcSendSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 12, 1, 13),
    _MscAppnDlciVcSendSequenceNumber_Type()
)
mscAppnDlciVcSendSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcSendSequenceNumber.setStatus("mandatory")


class _MscAppnDlciVcPktRetryTimeouts_Type(Unsigned32):
    """Custom type mscAppnDlciVcPktRetryTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscAppnDlciVcPktRetryTimeouts_Type.__name__ = "Unsigned32"
_MscAppnDlciVcPktRetryTimeouts_Object = MibTableColumn
mscAppnDlciVcPktRetryTimeouts = _MscAppnDlciVcPktRetryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 12, 1, 15),
    _MscAppnDlciVcPktRetryTimeouts_Type()
)
mscAppnDlciVcPktRetryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcPktRetryTimeouts.setStatus("mandatory")


class _MscAppnDlciVcPeakRetryQueueSize_Type(Unsigned32):
    """Custom type mscAppnDlciVcPeakRetryQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscAppnDlciVcPeakRetryQueueSize_Type.__name__ = "Unsigned32"
_MscAppnDlciVcPeakRetryQueueSize_Object = MibTableColumn
mscAppnDlciVcPeakRetryQueueSize = _MscAppnDlciVcPeakRetryQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 12, 1, 16),
    _MscAppnDlciVcPeakRetryQueueSize_Type()
)
mscAppnDlciVcPeakRetryQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcPeakRetryQueueSize.setStatus("mandatory")


class _MscAppnDlciVcSubnetRecoveries_Type(Unsigned32):
    """Custom type mscAppnDlciVcSubnetRecoveries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscAppnDlciVcSubnetRecoveries_Type.__name__ = "Unsigned32"
_MscAppnDlciVcSubnetRecoveries_Object = MibTableColumn
mscAppnDlciVcSubnetRecoveries = _MscAppnDlciVcSubnetRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 12, 1, 17),
    _MscAppnDlciVcSubnetRecoveries_Type()
)
mscAppnDlciVcSubnetRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcSubnetRecoveries.setStatus("mandatory")


class _MscAppnDlciVcOoSeqPktCntExceeded_Type(Unsigned32):
    """Custom type mscAppnDlciVcOoSeqPktCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnDlciVcOoSeqPktCntExceeded_Type.__name__ = "Unsigned32"
_MscAppnDlciVcOoSeqPktCntExceeded_Object = MibTableColumn
mscAppnDlciVcOoSeqPktCntExceeded = _MscAppnDlciVcOoSeqPktCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 12, 1, 19),
    _MscAppnDlciVcOoSeqPktCntExceeded_Type()
)
mscAppnDlciVcOoSeqPktCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcOoSeqPktCntExceeded.setStatus("mandatory")


class _MscAppnDlciVcPeakOoSeqByteCount_Type(Unsigned32):
    """Custom type mscAppnDlciVcPeakOoSeqByteCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_MscAppnDlciVcPeakOoSeqByteCount_Type.__name__ = "Unsigned32"
_MscAppnDlciVcPeakOoSeqByteCount_Object = MibTableColumn
mscAppnDlciVcPeakOoSeqByteCount = _MscAppnDlciVcPeakOoSeqByteCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 12, 1, 20),
    _MscAppnDlciVcPeakOoSeqByteCount_Type()
)
mscAppnDlciVcPeakOoSeqByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcPeakOoSeqByteCount.setStatus("mandatory")
_MscAppnDlciVcDmepTable_Object = MibTable
mscAppnDlciVcDmepTable = _MscAppnDlciVcDmepTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 417)
)
if mibBuilder.loadTexts:
    mscAppnDlciVcDmepTable.setStatus("mandatory")
_MscAppnDlciVcDmepEntry_Object = MibTableRow
mscAppnDlciVcDmepEntry = _MscAppnDlciVcDmepEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 417, 1)
)
mscAppnDlciVcDmepEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciVcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciVcDmepValue"),
)
if mibBuilder.loadTexts:
    mscAppnDlciVcDmepEntry.setStatus("mandatory")
_MscAppnDlciVcDmepValue_Type = RowPointer
_MscAppnDlciVcDmepValue_Object = MibTableColumn
mscAppnDlciVcDmepValue = _MscAppnDlciVcDmepValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 3, 417, 1, 1),
    _MscAppnDlciVcDmepValue_Type()
)
mscAppnDlciVcDmepValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciVcDmepValue.setStatus("mandatory")
_MscAppnDlciBnnLsDef_ObjectIdentity = ObjectIdentity
mscAppnDlciBnnLsDef = _MscAppnDlciBnnLsDef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 4)
)
_MscAppnDlciBnnLsDefRowStatusTable_Object = MibTable
mscAppnDlciBnnLsDefRowStatusTable = _MscAppnDlciBnnLsDefRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 4, 1)
)
if mibBuilder.loadTexts:
    mscAppnDlciBnnLsDefRowStatusTable.setStatus("mandatory")
_MscAppnDlciBnnLsDefRowStatusEntry_Object = MibTableRow
mscAppnDlciBnnLsDefRowStatusEntry = _MscAppnDlciBnnLsDefRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 4, 1, 1)
)
mscAppnDlciBnnLsDefRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciBnnLsDefIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDlciBnnLsDefRowStatusEntry.setStatus("mandatory")
_MscAppnDlciBnnLsDefRowStatus_Type = RowStatus
_MscAppnDlciBnnLsDefRowStatus_Object = MibTableColumn
mscAppnDlciBnnLsDefRowStatus = _MscAppnDlciBnnLsDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 4, 1, 1, 1),
    _MscAppnDlciBnnLsDefRowStatus_Type()
)
mscAppnDlciBnnLsDefRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciBnnLsDefRowStatus.setStatus("mandatory")
_MscAppnDlciBnnLsDefComponentName_Type = DisplayString
_MscAppnDlciBnnLsDefComponentName_Object = MibTableColumn
mscAppnDlciBnnLsDefComponentName = _MscAppnDlciBnnLsDefComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 4, 1, 1, 2),
    _MscAppnDlciBnnLsDefComponentName_Type()
)
mscAppnDlciBnnLsDefComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciBnnLsDefComponentName.setStatus("mandatory")
_MscAppnDlciBnnLsDefStorageType_Type = StorageType
_MscAppnDlciBnnLsDefStorageType_Object = MibTableColumn
mscAppnDlciBnnLsDefStorageType = _MscAppnDlciBnnLsDefStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 4, 1, 1, 4),
    _MscAppnDlciBnnLsDefStorageType_Type()
)
mscAppnDlciBnnLsDefStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciBnnLsDefStorageType.setStatus("mandatory")


class _MscAppnDlciBnnLsDefIndex_Type(Integer32):
    """Custom type mscAppnDlciBnnLsDefIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(12, 12),
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(24, 24),
        ValueRangeConstraint(28, 28),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(44, 44),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(52, 52),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(68, 68),
        ValueRangeConstraint(72, 72),
        ValueRangeConstraint(76, 76),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(84, 84),
        ValueRangeConstraint(88, 88),
        ValueRangeConstraint(92, 92),
        ValueRangeConstraint(96, 96),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(104, 104),
        ValueRangeConstraint(108, 108),
        ValueRangeConstraint(112, 112),
        ValueRangeConstraint(116, 116),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(124, 124),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(132, 132),
        ValueRangeConstraint(136, 136),
        ValueRangeConstraint(140, 140),
        ValueRangeConstraint(144, 144),
        ValueRangeConstraint(148, 148),
        ValueRangeConstraint(152, 152),
        ValueRangeConstraint(156, 156),
        ValueRangeConstraint(160, 160),
        ValueRangeConstraint(164, 164),
        ValueRangeConstraint(168, 168),
        ValueRangeConstraint(172, 172),
        ValueRangeConstraint(176, 176),
        ValueRangeConstraint(180, 180),
        ValueRangeConstraint(184, 184),
        ValueRangeConstraint(188, 188),
        ValueRangeConstraint(192, 192),
        ValueRangeConstraint(196, 196),
        ValueRangeConstraint(200, 200),
        ValueRangeConstraint(204, 204),
        ValueRangeConstraint(208, 208),
        ValueRangeConstraint(212, 212),
        ValueRangeConstraint(216, 216),
        ValueRangeConstraint(220, 220),
        ValueRangeConstraint(224, 224),
        ValueRangeConstraint(228, 228),
        ValueRangeConstraint(232, 232),
        ValueRangeConstraint(236, 236),
        ValueRangeConstraint(240, 240),
        ValueRangeConstraint(244, 244),
        ValueRangeConstraint(248, 248),
        ValueRangeConstraint(252, 252),
    )


_MscAppnDlciBnnLsDefIndex_Type.__name__ = "Integer32"
_MscAppnDlciBnnLsDefIndex_Object = MibTableColumn
mscAppnDlciBnnLsDefIndex = _MscAppnDlciBnnLsDefIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 4, 1, 1, 10),
    _MscAppnDlciBnnLsDefIndex_Type()
)
mscAppnDlciBnnLsDefIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnDlciBnnLsDefIndex.setStatus("mandatory")
_MscAppnDlciBnnLsDefProvTable_Object = MibTable
mscAppnDlciBnnLsDefProvTable = _MscAppnDlciBnnLsDefProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 4, 2)
)
if mibBuilder.loadTexts:
    mscAppnDlciBnnLsDefProvTable.setStatus("mandatory")
_MscAppnDlciBnnLsDefProvEntry_Object = MibTableRow
mscAppnDlciBnnLsDefProvEntry = _MscAppnDlciBnnLsDefProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 4, 2, 1)
)
mscAppnDlciBnnLsDefProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciBnnLsDefIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDlciBnnLsDefProvEntry.setStatus("mandatory")


class _MscAppnDlciBnnLsDefDspuService_Type(Integer32):
    """Custom type mscAppnDlciBnnLsDefDspuService based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dlur", 2),
          ("none", 0))
    )


_MscAppnDlciBnnLsDefDspuService_Type.__name__ = "Integer32"
_MscAppnDlciBnnLsDefDspuService_Object = MibTableColumn
mscAppnDlciBnnLsDefDspuService = _MscAppnDlciBnnLsDefDspuService_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 4, 2, 1, 1),
    _MscAppnDlciBnnLsDefDspuService_Type()
)
mscAppnDlciBnnLsDefDspuService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciBnnLsDefDspuService.setStatus("mandatory")


class _MscAppnDlciBnnLsDefAdjacentCpName_Type(AsciiString):
    """Custom type mscAppnDlciBnnLsDefAdjacentCpName based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_MscAppnDlciBnnLsDefAdjacentCpName_Type.__name__ = "AsciiString"
_MscAppnDlciBnnLsDefAdjacentCpName_Object = MibTableColumn
mscAppnDlciBnnLsDefAdjacentCpName = _MscAppnDlciBnnLsDefAdjacentCpName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 4, 2, 1, 2),
    _MscAppnDlciBnnLsDefAdjacentCpName_Type()
)
mscAppnDlciBnnLsDefAdjacentCpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciBnnLsDefAdjacentCpName.setStatus("mandatory")


class _MscAppnDlciBnnLsDefAdjacentCpType_Type(Integer32):
    """Custom type mscAppnDlciBnnLsDefAdjacentCpType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("appnNode", 0),
          ("backLevelLenNode", 5),
          ("dlurNoXID", 9),
          ("dlurXID", 8),
          ("endNode", 3),
          ("hostXID0", 7),
          ("hostXID3", 6),
          ("networkNode", 2))
    )


_MscAppnDlciBnnLsDefAdjacentCpType_Type.__name__ = "Integer32"
_MscAppnDlciBnnLsDefAdjacentCpType_Object = MibTableColumn
mscAppnDlciBnnLsDefAdjacentCpType = _MscAppnDlciBnnLsDefAdjacentCpType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 4, 2, 1, 3),
    _MscAppnDlciBnnLsDefAdjacentCpType_Type()
)
mscAppnDlciBnnLsDefAdjacentCpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciBnnLsDefAdjacentCpType.setStatus("mandatory")


class _MscAppnDlciBnnLsDefTgNum_Type(Unsigned32):
    """Custom type mscAppnDlciBnnLsDefTgNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_MscAppnDlciBnnLsDefTgNum_Type.__name__ = "Unsigned32"
_MscAppnDlciBnnLsDefTgNum_Object = MibTableColumn
mscAppnDlciBnnLsDefTgNum = _MscAppnDlciBnnLsDefTgNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 4, 2, 1, 5),
    _MscAppnDlciBnnLsDefTgNum_Type()
)
mscAppnDlciBnnLsDefTgNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciBnnLsDefTgNum.setStatus("mandatory")


class _MscAppnDlciBnnLsDefDlusName_Type(AsciiString):
    """Custom type mscAppnDlciBnnLsDefDlusName based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_MscAppnDlciBnnLsDefDlusName_Type.__name__ = "AsciiString"
_MscAppnDlciBnnLsDefDlusName_Object = MibTableColumn
mscAppnDlciBnnLsDefDlusName = _MscAppnDlciBnnLsDefDlusName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 4, 2, 1, 6),
    _MscAppnDlciBnnLsDefDlusName_Type()
)
mscAppnDlciBnnLsDefDlusName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciBnnLsDefDlusName.setStatus("mandatory")


class _MscAppnDlciBnnLsDefBackupDlusName_Type(AsciiString):
    """Custom type mscAppnDlciBnnLsDefBackupDlusName based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_MscAppnDlciBnnLsDefBackupDlusName_Type.__name__ = "AsciiString"
_MscAppnDlciBnnLsDefBackupDlusName_Object = MibTableColumn
mscAppnDlciBnnLsDefBackupDlusName = _MscAppnDlciBnnLsDefBackupDlusName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 4, 2, 1, 7),
    _MscAppnDlciBnnLsDefBackupDlusName_Type()
)
mscAppnDlciBnnLsDefBackupDlusName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciBnnLsDefBackupDlusName.setStatus("mandatory")


class _MscAppnDlciBnnLsDefHprSupported_Type(Integer32):
    """Custom type mscAppnDlciBnnLsDefHprSupported based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("sameAsNode", 1))
    )


_MscAppnDlciBnnLsDefHprSupported_Type.__name__ = "Integer32"
_MscAppnDlciBnnLsDefHprSupported_Object = MibTableColumn
mscAppnDlciBnnLsDefHprSupported = _MscAppnDlciBnnLsDefHprSupported_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 4, 2, 1, 8),
    _MscAppnDlciBnnLsDefHprSupported_Type()
)
mscAppnDlciBnnLsDefHprSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciBnnLsDefHprSupported.setStatus("mandatory")


class _MscAppnDlciBnnLsDefAdjacentNodeID_Type(Hex):
    """Custom type mscAppnDlciBnnLsDefAdjacentNodeID based on Hex"""
    defaultValue = 0

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAppnDlciBnnLsDefAdjacentNodeID_Type.__name__ = "Hex"
_MscAppnDlciBnnLsDefAdjacentNodeID_Object = MibTableColumn
mscAppnDlciBnnLsDefAdjacentNodeID = _MscAppnDlciBnnLsDefAdjacentNodeID_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 4, 2, 1, 9),
    _MscAppnDlciBnnLsDefAdjacentNodeID_Type()
)
mscAppnDlciBnnLsDefAdjacentNodeID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciBnnLsDefAdjacentNodeID.setStatus("mandatory")


class _MscAppnDlciBnnLsDefCpCpSessionSupport_Type(Integer32):
    """Custom type mscAppnDlciBnnLsDefCpCpSessionSupport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MscAppnDlciBnnLsDefCpCpSessionSupport_Type.__name__ = "Integer32"
_MscAppnDlciBnnLsDefCpCpSessionSupport_Object = MibTableColumn
mscAppnDlciBnnLsDefCpCpSessionSupport = _MscAppnDlciBnnLsDefCpCpSessionSupport_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 4, 2, 1, 10),
    _MscAppnDlciBnnLsDefCpCpSessionSupport_Type()
)
mscAppnDlciBnnLsDefCpCpSessionSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciBnnLsDefCpCpSessionSupport.setStatus("mandatory")


class _MscAppnDlciBnnLsDefMaxTxBtuSize_Type(Unsigned32):
    """Custom type mscAppnDlciBnnLsDefMaxTxBtuSize based on Unsigned32"""
    defaultValue = 2048

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(99, 32768),
    )


_MscAppnDlciBnnLsDefMaxTxBtuSize_Type.__name__ = "Unsigned32"
_MscAppnDlciBnnLsDefMaxTxBtuSize_Object = MibTableColumn
mscAppnDlciBnnLsDefMaxTxBtuSize = _MscAppnDlciBnnLsDefMaxTxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 4, 2, 1, 11),
    _MscAppnDlciBnnLsDefMaxTxBtuSize_Type()
)
mscAppnDlciBnnLsDefMaxTxBtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciBnnLsDefMaxTxBtuSize.setStatus("mandatory")


class _MscAppnDlciBnnLsDefLsRole_Type(Integer32):
    """Custom type mscAppnDlciBnnLsDefLsRole based on Integer32"""
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
        *(("negotiable", 0),
          ("primary", 1),
          ("secondary", 2))
    )


_MscAppnDlciBnnLsDefLsRole_Type.__name__ = "Integer32"
_MscAppnDlciBnnLsDefLsRole_Object = MibTableColumn
mscAppnDlciBnnLsDefLsRole = _MscAppnDlciBnnLsDefLsRole_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 4, 2, 1, 12),
    _MscAppnDlciBnnLsDefLsRole_Type()
)
mscAppnDlciBnnLsDefLsRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciBnnLsDefLsRole.setStatus("mandatory")
_MscAppnDlciSp_ObjectIdentity = ObjectIdentity
mscAppnDlciSp = _MscAppnDlciSp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 5)
)
_MscAppnDlciSpRowStatusTable_Object = MibTable
mscAppnDlciSpRowStatusTable = _MscAppnDlciSpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 5, 1)
)
if mibBuilder.loadTexts:
    mscAppnDlciSpRowStatusTable.setStatus("mandatory")
_MscAppnDlciSpRowStatusEntry_Object = MibTableRow
mscAppnDlciSpRowStatusEntry = _MscAppnDlciSpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 5, 1, 1)
)
mscAppnDlciSpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciSpIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDlciSpRowStatusEntry.setStatus("mandatory")
_MscAppnDlciSpRowStatus_Type = RowStatus
_MscAppnDlciSpRowStatus_Object = MibTableColumn
mscAppnDlciSpRowStatus = _MscAppnDlciSpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 5, 1, 1, 1),
    _MscAppnDlciSpRowStatus_Type()
)
mscAppnDlciSpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciSpRowStatus.setStatus("mandatory")
_MscAppnDlciSpComponentName_Type = DisplayString
_MscAppnDlciSpComponentName_Object = MibTableColumn
mscAppnDlciSpComponentName = _MscAppnDlciSpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 5, 1, 1, 2),
    _MscAppnDlciSpComponentName_Type()
)
mscAppnDlciSpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciSpComponentName.setStatus("mandatory")
_MscAppnDlciSpStorageType_Type = StorageType
_MscAppnDlciSpStorageType_Object = MibTableColumn
mscAppnDlciSpStorageType = _MscAppnDlciSpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 5, 1, 1, 4),
    _MscAppnDlciSpStorageType_Type()
)
mscAppnDlciSpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciSpStorageType.setStatus("mandatory")
_MscAppnDlciSpIndex_Type = NonReplicated
_MscAppnDlciSpIndex_Object = MibTableColumn
mscAppnDlciSpIndex = _MscAppnDlciSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 5, 1, 1, 10),
    _MscAppnDlciSpIndex_Type()
)
mscAppnDlciSpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnDlciSpIndex.setStatus("mandatory")
_MscAppnDlciSpParmsTable_Object = MibTable
mscAppnDlciSpParmsTable = _MscAppnDlciSpParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 5, 11)
)
if mibBuilder.loadTexts:
    mscAppnDlciSpParmsTable.setStatus("mandatory")
_MscAppnDlciSpParmsEntry_Object = MibTableRow
mscAppnDlciSpParmsEntry = _MscAppnDlciSpParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 5, 11, 1)
)
mscAppnDlciSpParmsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciSpIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDlciSpParmsEntry.setStatus("mandatory")


class _MscAppnDlciSpRateEnforcement_Type(Integer32):
    """Custom type mscAppnDlciSpRateEnforcement based on Integer32"""
    defaultValue = 1

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


_MscAppnDlciSpRateEnforcement_Type.__name__ = "Integer32"
_MscAppnDlciSpRateEnforcement_Object = MibTableColumn
mscAppnDlciSpRateEnforcement = _MscAppnDlciSpRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 5, 11, 1, 1),
    _MscAppnDlciSpRateEnforcement_Type()
)
mscAppnDlciSpRateEnforcement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciSpRateEnforcement.setStatus("mandatory")


class _MscAppnDlciSpCommittedInformationRate_Type(Unsigned32):
    """Custom type mscAppnDlciSpCommittedInformationRate based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MscAppnDlciSpCommittedInformationRate_Type.__name__ = "Unsigned32"
_MscAppnDlciSpCommittedInformationRate_Object = MibTableColumn
mscAppnDlciSpCommittedInformationRate = _MscAppnDlciSpCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 5, 11, 1, 2),
    _MscAppnDlciSpCommittedInformationRate_Type()
)
mscAppnDlciSpCommittedInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciSpCommittedInformationRate.setStatus("mandatory")


class _MscAppnDlciSpCommittedBurstSize_Type(Unsigned32):
    """Custom type mscAppnDlciSpCommittedBurstSize based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MscAppnDlciSpCommittedBurstSize_Type.__name__ = "Unsigned32"
_MscAppnDlciSpCommittedBurstSize_Object = MibTableColumn
mscAppnDlciSpCommittedBurstSize = _MscAppnDlciSpCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 5, 11, 1, 3),
    _MscAppnDlciSpCommittedBurstSize_Type()
)
mscAppnDlciSpCommittedBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciSpCommittedBurstSize.setStatus("mandatory")


class _MscAppnDlciSpExcessBurstSize_Type(Unsigned32):
    """Custom type mscAppnDlciSpExcessBurstSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MscAppnDlciSpExcessBurstSize_Type.__name__ = "Unsigned32"
_MscAppnDlciSpExcessBurstSize_Object = MibTableColumn
mscAppnDlciSpExcessBurstSize = _MscAppnDlciSpExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 5, 11, 1, 4),
    _MscAppnDlciSpExcessBurstSize_Type()
)
mscAppnDlciSpExcessBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciSpExcessBurstSize.setStatus("mandatory")


class _MscAppnDlciSpMeasurementInterval_Type(Unsigned32):
    """Custom type mscAppnDlciSpMeasurementInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25500),
    )


_MscAppnDlciSpMeasurementInterval_Type.__name__ = "Unsigned32"
_MscAppnDlciSpMeasurementInterval_Object = MibTableColumn
mscAppnDlciSpMeasurementInterval = _MscAppnDlciSpMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 5, 11, 1, 5),
    _MscAppnDlciSpMeasurementInterval_Type()
)
mscAppnDlciSpMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciSpMeasurementInterval.setStatus("mandatory")
_MscAppnDlciBanLsDef_ObjectIdentity = ObjectIdentity
mscAppnDlciBanLsDef = _MscAppnDlciBanLsDef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 6)
)
_MscAppnDlciBanLsDefRowStatusTable_Object = MibTable
mscAppnDlciBanLsDefRowStatusTable = _MscAppnDlciBanLsDefRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 6, 1)
)
if mibBuilder.loadTexts:
    mscAppnDlciBanLsDefRowStatusTable.setStatus("mandatory")
_MscAppnDlciBanLsDefRowStatusEntry_Object = MibTableRow
mscAppnDlciBanLsDefRowStatusEntry = _MscAppnDlciBanLsDefRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 6, 1, 1)
)
mscAppnDlciBanLsDefRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciBanLsDefMacIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciBanLsDefSapIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDlciBanLsDefRowStatusEntry.setStatus("mandatory")
_MscAppnDlciBanLsDefRowStatus_Type = RowStatus
_MscAppnDlciBanLsDefRowStatus_Object = MibTableColumn
mscAppnDlciBanLsDefRowStatus = _MscAppnDlciBanLsDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 6, 1, 1, 1),
    _MscAppnDlciBanLsDefRowStatus_Type()
)
mscAppnDlciBanLsDefRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciBanLsDefRowStatus.setStatus("mandatory")
_MscAppnDlciBanLsDefComponentName_Type = DisplayString
_MscAppnDlciBanLsDefComponentName_Object = MibTableColumn
mscAppnDlciBanLsDefComponentName = _MscAppnDlciBanLsDefComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 6, 1, 1, 2),
    _MscAppnDlciBanLsDefComponentName_Type()
)
mscAppnDlciBanLsDefComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciBanLsDefComponentName.setStatus("mandatory")
_MscAppnDlciBanLsDefStorageType_Type = StorageType
_MscAppnDlciBanLsDefStorageType_Object = MibTableColumn
mscAppnDlciBanLsDefStorageType = _MscAppnDlciBanLsDefStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 6, 1, 1, 4),
    _MscAppnDlciBanLsDefStorageType_Type()
)
mscAppnDlciBanLsDefStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciBanLsDefStorageType.setStatus("mandatory")


class _MscAppnDlciBanLsDefMacIndex_Type(DashedHexString):
    """Custom type mscAppnDlciBanLsDefMacIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscAppnDlciBanLsDefMacIndex_Type.__name__ = "DashedHexString"
_MscAppnDlciBanLsDefMacIndex_Object = MibTableColumn
mscAppnDlciBanLsDefMacIndex = _MscAppnDlciBanLsDefMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 6, 1, 1, 10),
    _MscAppnDlciBanLsDefMacIndex_Type()
)
mscAppnDlciBanLsDefMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnDlciBanLsDefMacIndex.setStatus("mandatory")


class _MscAppnDlciBanLsDefSapIndex_Type(Integer32):
    """Custom type mscAppnDlciBanLsDefSapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(12, 12),
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(24, 24),
        ValueRangeConstraint(28, 28),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(44, 44),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(52, 52),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(68, 68),
        ValueRangeConstraint(72, 72),
        ValueRangeConstraint(76, 76),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(84, 84),
        ValueRangeConstraint(88, 88),
        ValueRangeConstraint(92, 92),
        ValueRangeConstraint(96, 96),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(104, 104),
        ValueRangeConstraint(108, 108),
        ValueRangeConstraint(112, 112),
        ValueRangeConstraint(116, 116),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(124, 124),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(132, 132),
        ValueRangeConstraint(136, 136),
        ValueRangeConstraint(140, 140),
        ValueRangeConstraint(144, 144),
        ValueRangeConstraint(148, 148),
        ValueRangeConstraint(152, 152),
        ValueRangeConstraint(156, 156),
        ValueRangeConstraint(160, 160),
        ValueRangeConstraint(164, 164),
        ValueRangeConstraint(168, 168),
        ValueRangeConstraint(172, 172),
        ValueRangeConstraint(176, 176),
        ValueRangeConstraint(180, 180),
        ValueRangeConstraint(184, 184),
        ValueRangeConstraint(188, 188),
        ValueRangeConstraint(192, 192),
        ValueRangeConstraint(196, 196),
        ValueRangeConstraint(200, 200),
        ValueRangeConstraint(204, 204),
        ValueRangeConstraint(208, 208),
        ValueRangeConstraint(212, 212),
        ValueRangeConstraint(216, 216),
        ValueRangeConstraint(220, 220),
        ValueRangeConstraint(224, 224),
        ValueRangeConstraint(228, 228),
        ValueRangeConstraint(232, 232),
        ValueRangeConstraint(236, 236),
        ValueRangeConstraint(240, 240),
        ValueRangeConstraint(244, 244),
        ValueRangeConstraint(248, 248),
        ValueRangeConstraint(252, 252),
    )


_MscAppnDlciBanLsDefSapIndex_Type.__name__ = "Integer32"
_MscAppnDlciBanLsDefSapIndex_Object = MibTableColumn
mscAppnDlciBanLsDefSapIndex = _MscAppnDlciBanLsDefSapIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 6, 1, 1, 11),
    _MscAppnDlciBanLsDefSapIndex_Type()
)
mscAppnDlciBanLsDefSapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnDlciBanLsDefSapIndex.setStatus("mandatory")
_MscAppnDlciBanLsDefProvTable_Object = MibTable
mscAppnDlciBanLsDefProvTable = _MscAppnDlciBanLsDefProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 6, 2)
)
if mibBuilder.loadTexts:
    mscAppnDlciBanLsDefProvTable.setStatus("mandatory")
_MscAppnDlciBanLsDefProvEntry_Object = MibTableRow
mscAppnDlciBanLsDefProvEntry = _MscAppnDlciBanLsDefProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 6, 2, 1)
)
mscAppnDlciBanLsDefProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciBanLsDefMacIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciBanLsDefSapIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDlciBanLsDefProvEntry.setStatus("mandatory")


class _MscAppnDlciBanLsDefDspuService_Type(Integer32):
    """Custom type mscAppnDlciBanLsDefDspuService based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dlur", 2),
          ("none", 0))
    )


_MscAppnDlciBanLsDefDspuService_Type.__name__ = "Integer32"
_MscAppnDlciBanLsDefDspuService_Object = MibTableColumn
mscAppnDlciBanLsDefDspuService = _MscAppnDlciBanLsDefDspuService_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 6, 2, 1, 1),
    _MscAppnDlciBanLsDefDspuService_Type()
)
mscAppnDlciBanLsDefDspuService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciBanLsDefDspuService.setStatus("mandatory")


class _MscAppnDlciBanLsDefAdjacentCpName_Type(AsciiString):
    """Custom type mscAppnDlciBanLsDefAdjacentCpName based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_MscAppnDlciBanLsDefAdjacentCpName_Type.__name__ = "AsciiString"
_MscAppnDlciBanLsDefAdjacentCpName_Object = MibTableColumn
mscAppnDlciBanLsDefAdjacentCpName = _MscAppnDlciBanLsDefAdjacentCpName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 6, 2, 1, 2),
    _MscAppnDlciBanLsDefAdjacentCpName_Type()
)
mscAppnDlciBanLsDefAdjacentCpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciBanLsDefAdjacentCpName.setStatus("mandatory")


class _MscAppnDlciBanLsDefAdjacentCpType_Type(Integer32):
    """Custom type mscAppnDlciBanLsDefAdjacentCpType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("appnNode", 0),
          ("backLevelLenNode", 5),
          ("dlurNoXID", 9),
          ("dlurXID", 8),
          ("endNode", 3),
          ("hostXID0", 7),
          ("hostXID3", 6),
          ("networkNode", 2))
    )


_MscAppnDlciBanLsDefAdjacentCpType_Type.__name__ = "Integer32"
_MscAppnDlciBanLsDefAdjacentCpType_Object = MibTableColumn
mscAppnDlciBanLsDefAdjacentCpType = _MscAppnDlciBanLsDefAdjacentCpType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 6, 2, 1, 3),
    _MscAppnDlciBanLsDefAdjacentCpType_Type()
)
mscAppnDlciBanLsDefAdjacentCpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciBanLsDefAdjacentCpType.setStatus("mandatory")


class _MscAppnDlciBanLsDefTgNum_Type(Unsigned32):
    """Custom type mscAppnDlciBanLsDefTgNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_MscAppnDlciBanLsDefTgNum_Type.__name__ = "Unsigned32"
_MscAppnDlciBanLsDefTgNum_Object = MibTableColumn
mscAppnDlciBanLsDefTgNum = _MscAppnDlciBanLsDefTgNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 6, 2, 1, 5),
    _MscAppnDlciBanLsDefTgNum_Type()
)
mscAppnDlciBanLsDefTgNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciBanLsDefTgNum.setStatus("mandatory")


class _MscAppnDlciBanLsDefDlusName_Type(AsciiString):
    """Custom type mscAppnDlciBanLsDefDlusName based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_MscAppnDlciBanLsDefDlusName_Type.__name__ = "AsciiString"
_MscAppnDlciBanLsDefDlusName_Object = MibTableColumn
mscAppnDlciBanLsDefDlusName = _MscAppnDlciBanLsDefDlusName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 6, 2, 1, 6),
    _MscAppnDlciBanLsDefDlusName_Type()
)
mscAppnDlciBanLsDefDlusName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciBanLsDefDlusName.setStatus("mandatory")


class _MscAppnDlciBanLsDefBackupDlusName_Type(AsciiString):
    """Custom type mscAppnDlciBanLsDefBackupDlusName based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_MscAppnDlciBanLsDefBackupDlusName_Type.__name__ = "AsciiString"
_MscAppnDlciBanLsDefBackupDlusName_Object = MibTableColumn
mscAppnDlciBanLsDefBackupDlusName = _MscAppnDlciBanLsDefBackupDlusName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 6, 2, 1, 7),
    _MscAppnDlciBanLsDefBackupDlusName_Type()
)
mscAppnDlciBanLsDefBackupDlusName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciBanLsDefBackupDlusName.setStatus("mandatory")


class _MscAppnDlciBanLsDefHprSupported_Type(Integer32):
    """Custom type mscAppnDlciBanLsDefHprSupported based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("sameAsNode", 1))
    )


_MscAppnDlciBanLsDefHprSupported_Type.__name__ = "Integer32"
_MscAppnDlciBanLsDefHprSupported_Object = MibTableColumn
mscAppnDlciBanLsDefHprSupported = _MscAppnDlciBanLsDefHprSupported_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 6, 2, 1, 8),
    _MscAppnDlciBanLsDefHprSupported_Type()
)
mscAppnDlciBanLsDefHprSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciBanLsDefHprSupported.setStatus("mandatory")


class _MscAppnDlciBanLsDefAdjacentNodeID_Type(Hex):
    """Custom type mscAppnDlciBanLsDefAdjacentNodeID based on Hex"""
    defaultValue = 0

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAppnDlciBanLsDefAdjacentNodeID_Type.__name__ = "Hex"
_MscAppnDlciBanLsDefAdjacentNodeID_Object = MibTableColumn
mscAppnDlciBanLsDefAdjacentNodeID = _MscAppnDlciBanLsDefAdjacentNodeID_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 6, 2, 1, 9),
    _MscAppnDlciBanLsDefAdjacentNodeID_Type()
)
mscAppnDlciBanLsDefAdjacentNodeID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciBanLsDefAdjacentNodeID.setStatus("mandatory")


class _MscAppnDlciBanLsDefCpCpSessionSupport_Type(Integer32):
    """Custom type mscAppnDlciBanLsDefCpCpSessionSupport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MscAppnDlciBanLsDefCpCpSessionSupport_Type.__name__ = "Integer32"
_MscAppnDlciBanLsDefCpCpSessionSupport_Object = MibTableColumn
mscAppnDlciBanLsDefCpCpSessionSupport = _MscAppnDlciBanLsDefCpCpSessionSupport_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 6, 2, 1, 10),
    _MscAppnDlciBanLsDefCpCpSessionSupport_Type()
)
mscAppnDlciBanLsDefCpCpSessionSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciBanLsDefCpCpSessionSupport.setStatus("mandatory")


class _MscAppnDlciBanLsDefMaxTxBtuSize_Type(Unsigned32):
    """Custom type mscAppnDlciBanLsDefMaxTxBtuSize based on Unsigned32"""
    defaultValue = 2048

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(99, 32768),
    )


_MscAppnDlciBanLsDefMaxTxBtuSize_Type.__name__ = "Unsigned32"
_MscAppnDlciBanLsDefMaxTxBtuSize_Object = MibTableColumn
mscAppnDlciBanLsDefMaxTxBtuSize = _MscAppnDlciBanLsDefMaxTxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 6, 2, 1, 11),
    _MscAppnDlciBanLsDefMaxTxBtuSize_Type()
)
mscAppnDlciBanLsDefMaxTxBtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciBanLsDefMaxTxBtuSize.setStatus("mandatory")


class _MscAppnDlciBanLsDefLsRole_Type(Integer32):
    """Custom type mscAppnDlciBanLsDefLsRole based on Integer32"""
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
        *(("negotiable", 0),
          ("primary", 1),
          ("secondary", 2))
    )


_MscAppnDlciBanLsDefLsRole_Type.__name__ = "Integer32"
_MscAppnDlciBanLsDefLsRole_Object = MibTableColumn
mscAppnDlciBanLsDefLsRole = _MscAppnDlciBanLsDefLsRole_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 6, 2, 1, 12),
    _MscAppnDlciBanLsDefLsRole_Type()
)
mscAppnDlciBanLsDefLsRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciBanLsDefLsRole.setStatus("mandatory")
_MscAppnDlciBan_ObjectIdentity = ObjectIdentity
mscAppnDlciBan = _MscAppnDlciBan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 7)
)
_MscAppnDlciBanRowStatusTable_Object = MibTable
mscAppnDlciBanRowStatusTable = _MscAppnDlciBanRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 7, 1)
)
if mibBuilder.loadTexts:
    mscAppnDlciBanRowStatusTable.setStatus("mandatory")
_MscAppnDlciBanRowStatusEntry_Object = MibTableRow
mscAppnDlciBanRowStatusEntry = _MscAppnDlciBanRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 7, 1, 1)
)
mscAppnDlciBanRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciBanIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDlciBanRowStatusEntry.setStatus("mandatory")
_MscAppnDlciBanRowStatus_Type = RowStatus
_MscAppnDlciBanRowStatus_Object = MibTableColumn
mscAppnDlciBanRowStatus = _MscAppnDlciBanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 7, 1, 1, 1),
    _MscAppnDlciBanRowStatus_Type()
)
mscAppnDlciBanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciBanRowStatus.setStatus("mandatory")
_MscAppnDlciBanComponentName_Type = DisplayString
_MscAppnDlciBanComponentName_Object = MibTableColumn
mscAppnDlciBanComponentName = _MscAppnDlciBanComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 7, 1, 1, 2),
    _MscAppnDlciBanComponentName_Type()
)
mscAppnDlciBanComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciBanComponentName.setStatus("mandatory")
_MscAppnDlciBanStorageType_Type = StorageType
_MscAppnDlciBanStorageType_Object = MibTableColumn
mscAppnDlciBanStorageType = _MscAppnDlciBanStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 7, 1, 1, 4),
    _MscAppnDlciBanStorageType_Type()
)
mscAppnDlciBanStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciBanStorageType.setStatus("mandatory")
_MscAppnDlciBanIndex_Type = NonReplicated
_MscAppnDlciBanIndex_Object = MibTableColumn
mscAppnDlciBanIndex = _MscAppnDlciBanIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 7, 1, 1, 10),
    _MscAppnDlciBanIndex_Type()
)
mscAppnDlciBanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnDlciBanIndex.setStatus("mandatory")
_MscAppnDlciBanProvTable_Object = MibTable
mscAppnDlciBanProvTable = _MscAppnDlciBanProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 7, 2)
)
if mibBuilder.loadTexts:
    mscAppnDlciBanProvTable.setStatus("mandatory")
_MscAppnDlciBanProvEntry_Object = MibTableRow
mscAppnDlciBanProvEntry = _MscAppnDlciBanProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 7, 2, 1)
)
mscAppnDlciBanProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciBanIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDlciBanProvEntry.setStatus("mandatory")


class _MscAppnDlciBanLocalMac_Type(DashedHexString):
    """Custom type mscAppnDlciBanLocalMac based on DashedHexString"""
    defaultHexValue = "4fff00000000"

    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscAppnDlciBanLocalMac_Type.__name__ = "DashedHexString"
_MscAppnDlciBanLocalMac_Object = MibTableColumn
mscAppnDlciBanLocalMac = _MscAppnDlciBanLocalMac_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 7, 2, 1, 1),
    _MscAppnDlciBanLocalMac_Type()
)
mscAppnDlciBanLocalMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciBanLocalMac.setStatus("mandatory")


class _MscAppnDlciBanLocalSap_Type(Hex):
    """Custom type mscAppnDlciBanLocalSap based on Hex"""
    defaultValue = 4

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(12, 12),
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(24, 24),
        ValueRangeConstraint(28, 28),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(44, 44),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(52, 52),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(68, 68),
        ValueRangeConstraint(72, 72),
        ValueRangeConstraint(76, 76),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(84, 84),
        ValueRangeConstraint(88, 88),
        ValueRangeConstraint(92, 92),
        ValueRangeConstraint(96, 96),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(104, 104),
        ValueRangeConstraint(108, 108),
        ValueRangeConstraint(112, 112),
        ValueRangeConstraint(116, 116),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(124, 124),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(132, 132),
        ValueRangeConstraint(136, 136),
        ValueRangeConstraint(140, 140),
        ValueRangeConstraint(144, 144),
        ValueRangeConstraint(148, 148),
        ValueRangeConstraint(152, 152),
        ValueRangeConstraint(156, 156),
        ValueRangeConstraint(160, 160),
        ValueRangeConstraint(164, 164),
        ValueRangeConstraint(168, 168),
        ValueRangeConstraint(172, 172),
        ValueRangeConstraint(176, 176),
        ValueRangeConstraint(180, 180),
        ValueRangeConstraint(184, 184),
        ValueRangeConstraint(188, 188),
        ValueRangeConstraint(192, 192),
        ValueRangeConstraint(196, 196),
        ValueRangeConstraint(200, 200),
        ValueRangeConstraint(204, 204),
        ValueRangeConstraint(208, 208),
        ValueRangeConstraint(212, 212),
        ValueRangeConstraint(216, 216),
        ValueRangeConstraint(220, 220),
        ValueRangeConstraint(224, 224),
        ValueRangeConstraint(228, 228),
        ValueRangeConstraint(232, 232),
        ValueRangeConstraint(236, 236),
        ValueRangeConstraint(240, 240),
        ValueRangeConstraint(244, 244),
        ValueRangeConstraint(248, 248),
        ValueRangeConstraint(252, 252),
    )


_MscAppnDlciBanLocalSap_Type.__name__ = "Hex"
_MscAppnDlciBanLocalSap_Object = MibTableColumn
mscAppnDlciBanLocalSap = _MscAppnDlciBanLocalSap_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 7, 2, 1, 2),
    _MscAppnDlciBanLocalSap_Type()
)
mscAppnDlciBanLocalSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlciBanLocalSap.setStatus("mandatory")
_MscAppnDlciStateTable_Object = MibTable
mscAppnDlciStateTable = _MscAppnDlciStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 10)
)
if mibBuilder.loadTexts:
    mscAppnDlciStateTable.setStatus("mandatory")
_MscAppnDlciStateEntry_Object = MibTableRow
mscAppnDlciStateEntry = _MscAppnDlciStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 10, 1)
)
mscAppnDlciStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDlciStateEntry.setStatus("mandatory")


class _MscAppnDlciAdminState_Type(Integer32):
    """Custom type mscAppnDlciAdminState based on Integer32"""
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


_MscAppnDlciAdminState_Type.__name__ = "Integer32"
_MscAppnDlciAdminState_Object = MibTableColumn
mscAppnDlciAdminState = _MscAppnDlciAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 10, 1, 1),
    _MscAppnDlciAdminState_Type()
)
mscAppnDlciAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciAdminState.setStatus("mandatory")


class _MscAppnDlciOperationalState_Type(Integer32):
    """Custom type mscAppnDlciOperationalState based on Integer32"""
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


_MscAppnDlciOperationalState_Type.__name__ = "Integer32"
_MscAppnDlciOperationalState_Object = MibTableColumn
mscAppnDlciOperationalState = _MscAppnDlciOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 10, 1, 2),
    _MscAppnDlciOperationalState_Type()
)
mscAppnDlciOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciOperationalState.setStatus("mandatory")


class _MscAppnDlciUsageState_Type(Integer32):
    """Custom type mscAppnDlciUsageState based on Integer32"""
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


_MscAppnDlciUsageState_Type.__name__ = "Integer32"
_MscAppnDlciUsageState_Object = MibTableColumn
mscAppnDlciUsageState = _MscAppnDlciUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 10, 1, 3),
    _MscAppnDlciUsageState_Type()
)
mscAppnDlciUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciUsageState.setStatus("mandatory")
_MscAppnDlciSpOpTable_Object = MibTable
mscAppnDlciSpOpTable = _MscAppnDlciSpOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 12)
)
if mibBuilder.loadTexts:
    mscAppnDlciSpOpTable.setStatus("mandatory")
_MscAppnDlciSpOpEntry_Object = MibTableRow
mscAppnDlciSpOpEntry = _MscAppnDlciSpOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 12, 1)
)
mscAppnDlciSpOpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlciIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDlciSpOpEntry.setStatus("mandatory")


class _MscAppnDlciRateEnforcement_Type(Integer32):
    """Custom type mscAppnDlciRateEnforcement based on Integer32"""
    defaultValue = 0

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


_MscAppnDlciRateEnforcement_Type.__name__ = "Integer32"
_MscAppnDlciRateEnforcement_Object = MibTableColumn
mscAppnDlciRateEnforcement = _MscAppnDlciRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 12, 1, 1),
    _MscAppnDlciRateEnforcement_Type()
)
mscAppnDlciRateEnforcement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciRateEnforcement.setStatus("mandatory")


class _MscAppnDlciCommittedInformationRate_Type(Gauge32):
    """Custom type mscAppnDlciCommittedInformationRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAppnDlciCommittedInformationRate_Type.__name__ = "Gauge32"
_MscAppnDlciCommittedInformationRate_Object = MibTableColumn
mscAppnDlciCommittedInformationRate = _MscAppnDlciCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 12, 1, 2),
    _MscAppnDlciCommittedInformationRate_Type()
)
mscAppnDlciCommittedInformationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciCommittedInformationRate.setStatus("mandatory")


class _MscAppnDlciCommittedBurstSize_Type(Gauge32):
    """Custom type mscAppnDlciCommittedBurstSize based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAppnDlciCommittedBurstSize_Type.__name__ = "Gauge32"
_MscAppnDlciCommittedBurstSize_Object = MibTableColumn
mscAppnDlciCommittedBurstSize = _MscAppnDlciCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 12, 1, 3),
    _MscAppnDlciCommittedBurstSize_Type()
)
mscAppnDlciCommittedBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciCommittedBurstSize.setStatus("mandatory")


class _MscAppnDlciExcessInformationRate_Type(Gauge32):
    """Custom type mscAppnDlciExcessInformationRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAppnDlciExcessInformationRate_Type.__name__ = "Gauge32"
_MscAppnDlciExcessInformationRate_Object = MibTableColumn
mscAppnDlciExcessInformationRate = _MscAppnDlciExcessInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 12, 1, 4),
    _MscAppnDlciExcessInformationRate_Type()
)
mscAppnDlciExcessInformationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciExcessInformationRate.setStatus("mandatory")


class _MscAppnDlciExcessBurstSize_Type(Gauge32):
    """Custom type mscAppnDlciExcessBurstSize based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_MscAppnDlciExcessBurstSize_Type.__name__ = "Gauge32"
_MscAppnDlciExcessBurstSize_Object = MibTableColumn
mscAppnDlciExcessBurstSize = _MscAppnDlciExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 12, 1, 5),
    _MscAppnDlciExcessBurstSize_Type()
)
mscAppnDlciExcessBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciExcessBurstSize.setStatus("mandatory")


class _MscAppnDlciMeasurementInterval_Type(Gauge32):
    """Custom type mscAppnDlciMeasurementInterval based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25500),
    )


_MscAppnDlciMeasurementInterval_Type.__name__ = "Gauge32"
_MscAppnDlciMeasurementInterval_Object = MibTableColumn
mscAppnDlciMeasurementInterval = _MscAppnDlciMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 3, 12, 1, 6),
    _MscAppnDlciMeasurementInterval_Type()
)
mscAppnDlciMeasurementInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlciMeasurementInterval.setStatus("mandatory")
_MscAppnLcn_ObjectIdentity = ObjectIdentity
mscAppnLcn = _MscAppnLcn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4)
)
_MscAppnLcnRowStatusTable_Object = MibTable
mscAppnLcnRowStatusTable = _MscAppnLcnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 1)
)
if mibBuilder.loadTexts:
    mscAppnLcnRowStatusTable.setStatus("mandatory")
_MscAppnLcnRowStatusEntry_Object = MibTableRow
mscAppnLcnRowStatusEntry = _MscAppnLcnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 1, 1)
)
mscAppnLcnRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnLcnIndex"),
)
if mibBuilder.loadTexts:
    mscAppnLcnRowStatusEntry.setStatus("mandatory")
_MscAppnLcnRowStatus_Type = RowStatus
_MscAppnLcnRowStatus_Object = MibTableColumn
mscAppnLcnRowStatus = _MscAppnLcnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 1, 1, 1),
    _MscAppnLcnRowStatus_Type()
)
mscAppnLcnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnLcnRowStatus.setStatus("mandatory")
_MscAppnLcnComponentName_Type = DisplayString
_MscAppnLcnComponentName_Object = MibTableColumn
mscAppnLcnComponentName = _MscAppnLcnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 1, 1, 2),
    _MscAppnLcnComponentName_Type()
)
mscAppnLcnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnComponentName.setStatus("mandatory")
_MscAppnLcnStorageType_Type = StorageType
_MscAppnLcnStorageType_Object = MibTableColumn
mscAppnLcnStorageType = _MscAppnLcnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 1, 1, 4),
    _MscAppnLcnStorageType_Type()
)
mscAppnLcnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnStorageType.setStatus("mandatory")


class _MscAppnLcnIndex_Type(Integer32):
    """Custom type mscAppnLcnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_MscAppnLcnIndex_Type.__name__ = "Integer32"
_MscAppnLcnIndex_Object = MibTableColumn
mscAppnLcnIndex = _MscAppnLcnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 1, 1, 10),
    _MscAppnLcnIndex_Type()
)
mscAppnLcnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnLcnIndex.setStatus("mandatory")
_MscAppnLcnDc_ObjectIdentity = ObjectIdentity
mscAppnLcnDc = _MscAppnLcnDc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 2)
)
_MscAppnLcnDcRowStatusTable_Object = MibTable
mscAppnLcnDcRowStatusTable = _MscAppnLcnDcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mscAppnLcnDcRowStatusTable.setStatus("mandatory")
_MscAppnLcnDcRowStatusEntry_Object = MibTableRow
mscAppnLcnDcRowStatusEntry = _MscAppnLcnDcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 2, 1, 1)
)
mscAppnLcnDcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnLcnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnLcnDcIndex"),
)
if mibBuilder.loadTexts:
    mscAppnLcnDcRowStatusEntry.setStatus("mandatory")
_MscAppnLcnDcRowStatus_Type = RowStatus
_MscAppnLcnDcRowStatus_Object = MibTableColumn
mscAppnLcnDcRowStatus = _MscAppnLcnDcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 2, 1, 1, 1),
    _MscAppnLcnDcRowStatus_Type()
)
mscAppnLcnDcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnDcRowStatus.setStatus("mandatory")
_MscAppnLcnDcComponentName_Type = DisplayString
_MscAppnLcnDcComponentName_Object = MibTableColumn
mscAppnLcnDcComponentName = _MscAppnLcnDcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 2, 1, 1, 2),
    _MscAppnLcnDcComponentName_Type()
)
mscAppnLcnDcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnDcComponentName.setStatus("mandatory")
_MscAppnLcnDcStorageType_Type = StorageType
_MscAppnLcnDcStorageType_Object = MibTableColumn
mscAppnLcnDcStorageType = _MscAppnLcnDcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 2, 1, 1, 4),
    _MscAppnLcnDcStorageType_Type()
)
mscAppnLcnDcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnDcStorageType.setStatus("mandatory")
_MscAppnLcnDcIndex_Type = NonReplicated
_MscAppnLcnDcIndex_Object = MibTableColumn
mscAppnLcnDcIndex = _MscAppnLcnDcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 2, 1, 1, 10),
    _MscAppnLcnDcIndex_Type()
)
mscAppnLcnDcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnLcnDcIndex.setStatus("mandatory")
_MscAppnLcnDcOptionsTable_Object = MibTable
mscAppnLcnDcOptionsTable = _MscAppnLcnDcOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 2, 10)
)
if mibBuilder.loadTexts:
    mscAppnLcnDcOptionsTable.setStatus("mandatory")
_MscAppnLcnDcOptionsEntry_Object = MibTableRow
mscAppnLcnDcOptionsEntry = _MscAppnLcnDcOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 2, 10, 1)
)
mscAppnLcnDcOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnLcnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnLcnDcIndex"),
)
if mibBuilder.loadTexts:
    mscAppnLcnDcOptionsEntry.setStatus("mandatory")


class _MscAppnLcnDcRemoteNpi_Type(Integer32):
    """Custom type mscAppnLcnDcRemoteNpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_MscAppnLcnDcRemoteNpi_Type.__name__ = "Integer32"
_MscAppnLcnDcRemoteNpi_Object = MibTableColumn
mscAppnLcnDcRemoteNpi = _MscAppnLcnDcRemoteNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 2, 10, 1, 3),
    _MscAppnLcnDcRemoteNpi_Type()
)
mscAppnLcnDcRemoteNpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnLcnDcRemoteNpi.setStatus("mandatory")


class _MscAppnLcnDcRemoteDna_Type(DigitString):
    """Custom type mscAppnLcnDcRemoteDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscAppnLcnDcRemoteDna_Type.__name__ = "DigitString"
_MscAppnLcnDcRemoteDna_Object = MibTableColumn
mscAppnLcnDcRemoteDna = _MscAppnLcnDcRemoteDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 2, 10, 1, 4),
    _MscAppnLcnDcRemoteDna_Type()
)
mscAppnLcnDcRemoteDna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnLcnDcRemoteDna.setStatus("mandatory")


class _MscAppnLcnDcTransferPriority_Type(Integer32):
    """Custom type mscAppnLcnDcTransferPriority based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              9,
              255)
        )
    )
    namedValues = NamedValues(
        *(("high", 9),
          ("normal", 0),
          ("useDnaDefTP", 255))
    )


_MscAppnLcnDcTransferPriority_Type.__name__ = "Integer32"
_MscAppnLcnDcTransferPriority_Object = MibTableColumn
mscAppnLcnDcTransferPriority = _MscAppnLcnDcTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 2, 10, 1, 9),
    _MscAppnLcnDcTransferPriority_Type()
)
mscAppnLcnDcTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnLcnDcTransferPriority.setStatus("mandatory")


class _MscAppnLcnDcDiscardPriority_Type(Integer32):
    """Custom type mscAppnLcnDcDiscardPriority based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("normal", 0),
          ("useDnaDefPriority", 3))
    )


_MscAppnLcnDcDiscardPriority_Type.__name__ = "Integer32"
_MscAppnLcnDcDiscardPriority_Object = MibTableColumn
mscAppnLcnDcDiscardPriority = _MscAppnLcnDcDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 2, 10, 1, 10),
    _MscAppnLcnDcDiscardPriority_Type()
)
mscAppnLcnDcDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnLcnDcDiscardPriority.setStatus("mandatory")
_MscAppnLcnVc_ObjectIdentity = ObjectIdentity
mscAppnLcnVc = _MscAppnLcnVc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3)
)
_MscAppnLcnVcRowStatusTable_Object = MibTable
mscAppnLcnVcRowStatusTable = _MscAppnLcnVcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 1)
)
if mibBuilder.loadTexts:
    mscAppnLcnVcRowStatusTable.setStatus("mandatory")
_MscAppnLcnVcRowStatusEntry_Object = MibTableRow
mscAppnLcnVcRowStatusEntry = _MscAppnLcnVcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 1, 1)
)
mscAppnLcnVcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnLcnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnLcnVcIndex"),
)
if mibBuilder.loadTexts:
    mscAppnLcnVcRowStatusEntry.setStatus("mandatory")
_MscAppnLcnVcRowStatus_Type = RowStatus
_MscAppnLcnVcRowStatus_Object = MibTableColumn
mscAppnLcnVcRowStatus = _MscAppnLcnVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 1, 1, 1),
    _MscAppnLcnVcRowStatus_Type()
)
mscAppnLcnVcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcRowStatus.setStatus("mandatory")
_MscAppnLcnVcComponentName_Type = DisplayString
_MscAppnLcnVcComponentName_Object = MibTableColumn
mscAppnLcnVcComponentName = _MscAppnLcnVcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 1, 1, 2),
    _MscAppnLcnVcComponentName_Type()
)
mscAppnLcnVcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcComponentName.setStatus("mandatory")
_MscAppnLcnVcStorageType_Type = StorageType
_MscAppnLcnVcStorageType_Object = MibTableColumn
mscAppnLcnVcStorageType = _MscAppnLcnVcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 1, 1, 4),
    _MscAppnLcnVcStorageType_Type()
)
mscAppnLcnVcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcStorageType.setStatus("mandatory")
_MscAppnLcnVcIndex_Type = NonReplicated
_MscAppnLcnVcIndex_Object = MibTableColumn
mscAppnLcnVcIndex = _MscAppnLcnVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 1, 1, 10),
    _MscAppnLcnVcIndex_Type()
)
mscAppnLcnVcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnLcnVcIndex.setStatus("mandatory")
_MscAppnLcnVcCadTable_Object = MibTable
mscAppnLcnVcCadTable = _MscAppnLcnVcCadTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 10)
)
if mibBuilder.loadTexts:
    mscAppnLcnVcCadTable.setStatus("mandatory")
_MscAppnLcnVcCadEntry_Object = MibTableRow
mscAppnLcnVcCadEntry = _MscAppnLcnVcCadEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 10, 1)
)
mscAppnLcnVcCadEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnLcnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnLcnVcIndex"),
)
if mibBuilder.loadTexts:
    mscAppnLcnVcCadEntry.setStatus("mandatory")


class _MscAppnLcnVcType_Type(Integer32):
    """Custom type mscAppnLcnVcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("svc", 0))
    )


_MscAppnLcnVcType_Type.__name__ = "Integer32"
_MscAppnLcnVcType_Object = MibTableColumn
mscAppnLcnVcType = _MscAppnLcnVcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 10, 1, 1),
    _MscAppnLcnVcType_Type()
)
mscAppnLcnVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcType.setStatus("mandatory")


class _MscAppnLcnVcState_Type(Integer32):
    """Custom type mscAppnLcnVcState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("creating", 0),
          ("dataTransferP4", 4),
          ("dceClearIndicationP7", 7),
          ("dceWaitingP3", 3),
          ("dteClearRequestP6", 6),
          ("dteWaitingP2", 2),
          ("readyP1", 1),
          ("termination", 8),
          ("unsupportedP5", 5))
    )


_MscAppnLcnVcState_Type.__name__ = "Integer32"
_MscAppnLcnVcState_Object = MibTableColumn
mscAppnLcnVcState = _MscAppnLcnVcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 10, 1, 2),
    _MscAppnLcnVcState_Type()
)
mscAppnLcnVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcState.setStatus("mandatory")


class _MscAppnLcnVcPreviousState_Type(Integer32):
    """Custom type mscAppnLcnVcPreviousState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("creating", 0),
          ("dataTransferP4", 4),
          ("dceClearIndicationP7", 7),
          ("dceWaitingP3", 3),
          ("dteClearRequestP6", 6),
          ("dteWaitingP2", 2),
          ("readyP1", 1),
          ("termination", 8),
          ("unsupportedP5", 5))
    )


_MscAppnLcnVcPreviousState_Type.__name__ = "Integer32"
_MscAppnLcnVcPreviousState_Object = MibTableColumn
mscAppnLcnVcPreviousState = _MscAppnLcnVcPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 10, 1, 3),
    _MscAppnLcnVcPreviousState_Type()
)
mscAppnLcnVcPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcPreviousState.setStatus("mandatory")


class _MscAppnLcnVcDiagnosticCode_Type(Unsigned32):
    """Custom type mscAppnLcnVcDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnLcnVcDiagnosticCode_Type.__name__ = "Unsigned32"
_MscAppnLcnVcDiagnosticCode_Object = MibTableColumn
mscAppnLcnVcDiagnosticCode = _MscAppnLcnVcDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 10, 1, 4),
    _MscAppnLcnVcDiagnosticCode_Type()
)
mscAppnLcnVcDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcDiagnosticCode.setStatus("mandatory")


class _MscAppnLcnVcPreviousDiagnosticCode_Type(Unsigned32):
    """Custom type mscAppnLcnVcPreviousDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnLcnVcPreviousDiagnosticCode_Type.__name__ = "Unsigned32"
_MscAppnLcnVcPreviousDiagnosticCode_Object = MibTableColumn
mscAppnLcnVcPreviousDiagnosticCode = _MscAppnLcnVcPreviousDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 10, 1, 5),
    _MscAppnLcnVcPreviousDiagnosticCode_Type()
)
mscAppnLcnVcPreviousDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcPreviousDiagnosticCode.setStatus("mandatory")


class _MscAppnLcnVcCalledNpi_Type(Integer32):
    """Custom type mscAppnLcnVcCalledNpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_MscAppnLcnVcCalledNpi_Type.__name__ = "Integer32"
_MscAppnLcnVcCalledNpi_Object = MibTableColumn
mscAppnLcnVcCalledNpi = _MscAppnLcnVcCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 10, 1, 6),
    _MscAppnLcnVcCalledNpi_Type()
)
mscAppnLcnVcCalledNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcCalledNpi.setStatus("mandatory")


class _MscAppnLcnVcCalledDna_Type(DigitString):
    """Custom type mscAppnLcnVcCalledDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscAppnLcnVcCalledDna_Type.__name__ = "DigitString"
_MscAppnLcnVcCalledDna_Object = MibTableColumn
mscAppnLcnVcCalledDna = _MscAppnLcnVcCalledDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 10, 1, 7),
    _MscAppnLcnVcCalledDna_Type()
)
mscAppnLcnVcCalledDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcCalledDna.setStatus("mandatory")


class _MscAppnLcnVcCalledLcn_Type(Unsigned32):
    """Custom type mscAppnLcnVcCalledLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscAppnLcnVcCalledLcn_Type.__name__ = "Unsigned32"
_MscAppnLcnVcCalledLcn_Object = MibTableColumn
mscAppnLcnVcCalledLcn = _MscAppnLcnVcCalledLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 10, 1, 8),
    _MscAppnLcnVcCalledLcn_Type()
)
mscAppnLcnVcCalledLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcCalledLcn.setStatus("mandatory")


class _MscAppnLcnVcCallingNpi_Type(Integer32):
    """Custom type mscAppnLcnVcCallingNpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_MscAppnLcnVcCallingNpi_Type.__name__ = "Integer32"
_MscAppnLcnVcCallingNpi_Object = MibTableColumn
mscAppnLcnVcCallingNpi = _MscAppnLcnVcCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 10, 1, 9),
    _MscAppnLcnVcCallingNpi_Type()
)
mscAppnLcnVcCallingNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcCallingNpi.setStatus("mandatory")


class _MscAppnLcnVcCallingDna_Type(DigitString):
    """Custom type mscAppnLcnVcCallingDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscAppnLcnVcCallingDna_Type.__name__ = "DigitString"
_MscAppnLcnVcCallingDna_Object = MibTableColumn
mscAppnLcnVcCallingDna = _MscAppnLcnVcCallingDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 10, 1, 10),
    _MscAppnLcnVcCallingDna_Type()
)
mscAppnLcnVcCallingDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcCallingDna.setStatus("mandatory")


class _MscAppnLcnVcCallingLcn_Type(Unsigned32):
    """Custom type mscAppnLcnVcCallingLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscAppnLcnVcCallingLcn_Type.__name__ = "Unsigned32"
_MscAppnLcnVcCallingLcn_Object = MibTableColumn
mscAppnLcnVcCallingLcn = _MscAppnLcnVcCallingLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 10, 1, 11),
    _MscAppnLcnVcCallingLcn_Type()
)
mscAppnLcnVcCallingLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcCallingLcn.setStatus("mandatory")


class _MscAppnLcnVcAccountingEnabled_Type(Integer32):
    """Custom type mscAppnLcnVcAccountingEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 0))
    )


_MscAppnLcnVcAccountingEnabled_Type.__name__ = "Integer32"
_MscAppnLcnVcAccountingEnabled_Object = MibTableColumn
mscAppnLcnVcAccountingEnabled = _MscAppnLcnVcAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 10, 1, 12),
    _MscAppnLcnVcAccountingEnabled_Type()
)
mscAppnLcnVcAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcAccountingEnabled.setStatus("mandatory")


class _MscAppnLcnVcFastSelectCall_Type(Integer32):
    """Custom type mscAppnLcnVcFastSelectCall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MscAppnLcnVcFastSelectCall_Type.__name__ = "Integer32"
_MscAppnLcnVcFastSelectCall_Object = MibTableColumn
mscAppnLcnVcFastSelectCall = _MscAppnLcnVcFastSelectCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 10, 1, 13),
    _MscAppnLcnVcFastSelectCall_Type()
)
mscAppnLcnVcFastSelectCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcFastSelectCall.setStatus("mandatory")


class _MscAppnLcnVcLocalRxPktSize_Type(Integer32):
    """Custom type mscAppnLcnVcLocalRxPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("n1024", 10),
          ("n128", 7),
          ("n16", 4),
          ("n2048", 11),
          ("n256", 8),
          ("n32", 5),
          ("n4096", 12),
          ("n512", 9),
          ("n64", 6),
          ("unknown", 0))
    )


_MscAppnLcnVcLocalRxPktSize_Type.__name__ = "Integer32"
_MscAppnLcnVcLocalRxPktSize_Object = MibTableColumn
mscAppnLcnVcLocalRxPktSize = _MscAppnLcnVcLocalRxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 10, 1, 14),
    _MscAppnLcnVcLocalRxPktSize_Type()
)
mscAppnLcnVcLocalRxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcLocalRxPktSize.setStatus("mandatory")


class _MscAppnLcnVcLocalTxPktSize_Type(Integer32):
    """Custom type mscAppnLcnVcLocalTxPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("n1024", 10),
          ("n128", 7),
          ("n16", 4),
          ("n2048", 11),
          ("n256", 8),
          ("n32", 5),
          ("n4096", 12),
          ("n512", 9),
          ("n64", 6),
          ("unknown", 0))
    )


_MscAppnLcnVcLocalTxPktSize_Type.__name__ = "Integer32"
_MscAppnLcnVcLocalTxPktSize_Object = MibTableColumn
mscAppnLcnVcLocalTxPktSize = _MscAppnLcnVcLocalTxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 10, 1, 15),
    _MscAppnLcnVcLocalTxPktSize_Type()
)
mscAppnLcnVcLocalTxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcLocalTxPktSize.setStatus("mandatory")


class _MscAppnLcnVcLocalTxWindowSize_Type(Unsigned32):
    """Custom type mscAppnLcnVcLocalTxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MscAppnLcnVcLocalTxWindowSize_Type.__name__ = "Unsigned32"
_MscAppnLcnVcLocalTxWindowSize_Object = MibTableColumn
mscAppnLcnVcLocalTxWindowSize = _MscAppnLcnVcLocalTxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 10, 1, 16),
    _MscAppnLcnVcLocalTxWindowSize_Type()
)
mscAppnLcnVcLocalTxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcLocalTxWindowSize.setStatus("mandatory")


class _MscAppnLcnVcLocalRxWindowSize_Type(Unsigned32):
    """Custom type mscAppnLcnVcLocalRxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MscAppnLcnVcLocalRxWindowSize_Type.__name__ = "Unsigned32"
_MscAppnLcnVcLocalRxWindowSize_Object = MibTableColumn
mscAppnLcnVcLocalRxWindowSize = _MscAppnLcnVcLocalRxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 10, 1, 17),
    _MscAppnLcnVcLocalRxWindowSize_Type()
)
mscAppnLcnVcLocalRxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcLocalRxWindowSize.setStatus("mandatory")


class _MscAppnLcnVcPathReliability_Type(Integer32):
    """Custom type mscAppnLcnVcPathReliability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 0),
          ("normal", 1))
    )


_MscAppnLcnVcPathReliability_Type.__name__ = "Integer32"
_MscAppnLcnVcPathReliability_Object = MibTableColumn
mscAppnLcnVcPathReliability = _MscAppnLcnVcPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 10, 1, 19),
    _MscAppnLcnVcPathReliability_Type()
)
mscAppnLcnVcPathReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcPathReliability.setStatus("mandatory")


class _MscAppnLcnVcAccountingEnd_Type(Integer32):
    """Custom type mscAppnLcnVcAccountingEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("calledEnd", 1),
          ("callingEnd", 0))
    )


_MscAppnLcnVcAccountingEnd_Type.__name__ = "Integer32"
_MscAppnLcnVcAccountingEnd_Object = MibTableColumn
mscAppnLcnVcAccountingEnd = _MscAppnLcnVcAccountingEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 10, 1, 20),
    _MscAppnLcnVcAccountingEnd_Type()
)
mscAppnLcnVcAccountingEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcAccountingEnd.setStatus("mandatory")


class _MscAppnLcnVcPriority_Type(Integer32):
    """Custom type mscAppnLcnVcPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("normal", 0))
    )


_MscAppnLcnVcPriority_Type.__name__ = "Integer32"
_MscAppnLcnVcPriority_Object = MibTableColumn
mscAppnLcnVcPriority = _MscAppnLcnVcPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 10, 1, 21),
    _MscAppnLcnVcPriority_Type()
)
mscAppnLcnVcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcPriority.setStatus("mandatory")


class _MscAppnLcnVcSegmentSize_Type(Unsigned32):
    """Custom type mscAppnLcnVcSegmentSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscAppnLcnVcSegmentSize_Type.__name__ = "Unsigned32"
_MscAppnLcnVcSegmentSize_Object = MibTableColumn
mscAppnLcnVcSegmentSize = _MscAppnLcnVcSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 10, 1, 22),
    _MscAppnLcnVcSegmentSize_Type()
)
mscAppnLcnVcSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcSegmentSize.setStatus("mandatory")


class _MscAppnLcnVcSubnetTxPktSize_Type(Integer32):
    """Custom type mscAppnLcnVcSubnetTxPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("n1024", 10),
          ("n128", 7),
          ("n16", 4),
          ("n2048", 11),
          ("n256", 8),
          ("n32", 5),
          ("n4096", 12),
          ("n512", 9),
          ("n64", 6),
          ("unknown", 0))
    )


_MscAppnLcnVcSubnetTxPktSize_Type.__name__ = "Integer32"
_MscAppnLcnVcSubnetTxPktSize_Object = MibTableColumn
mscAppnLcnVcSubnetTxPktSize = _MscAppnLcnVcSubnetTxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 10, 1, 23),
    _MscAppnLcnVcSubnetTxPktSize_Type()
)
mscAppnLcnVcSubnetTxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcSubnetTxPktSize.setStatus("mandatory")


class _MscAppnLcnVcSubnetTxWindowSize_Type(Unsigned32):
    """Custom type mscAppnLcnVcSubnetTxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscAppnLcnVcSubnetTxWindowSize_Type.__name__ = "Unsigned32"
_MscAppnLcnVcSubnetTxWindowSize_Object = MibTableColumn
mscAppnLcnVcSubnetTxWindowSize = _MscAppnLcnVcSubnetTxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 10, 1, 24),
    _MscAppnLcnVcSubnetTxWindowSize_Type()
)
mscAppnLcnVcSubnetTxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcSubnetTxWindowSize.setStatus("mandatory")


class _MscAppnLcnVcSubnetRxPktSize_Type(Integer32):
    """Custom type mscAppnLcnVcSubnetRxPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("n1024", 10),
          ("n128", 7),
          ("n16", 4),
          ("n2048", 11),
          ("n256", 8),
          ("n32", 5),
          ("n4096", 12),
          ("n512", 9),
          ("n64", 6),
          ("unknown", 0))
    )


_MscAppnLcnVcSubnetRxPktSize_Type.__name__ = "Integer32"
_MscAppnLcnVcSubnetRxPktSize_Object = MibTableColumn
mscAppnLcnVcSubnetRxPktSize = _MscAppnLcnVcSubnetRxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 10, 1, 25),
    _MscAppnLcnVcSubnetRxPktSize_Type()
)
mscAppnLcnVcSubnetRxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcSubnetRxPktSize.setStatus("mandatory")


class _MscAppnLcnVcSubnetRxWindowSize_Type(Unsigned32):
    """Custom type mscAppnLcnVcSubnetRxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscAppnLcnVcSubnetRxWindowSize_Type.__name__ = "Unsigned32"
_MscAppnLcnVcSubnetRxWindowSize_Object = MibTableColumn
mscAppnLcnVcSubnetRxWindowSize = _MscAppnLcnVcSubnetRxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 10, 1, 26),
    _MscAppnLcnVcSubnetRxWindowSize_Type()
)
mscAppnLcnVcSubnetRxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcSubnetRxWindowSize.setStatus("mandatory")


class _MscAppnLcnVcMaxSubnetPktSize_Type(Unsigned32):
    """Custom type mscAppnLcnVcMaxSubnetPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscAppnLcnVcMaxSubnetPktSize_Type.__name__ = "Unsigned32"
_MscAppnLcnVcMaxSubnetPktSize_Object = MibTableColumn
mscAppnLcnVcMaxSubnetPktSize = _MscAppnLcnVcMaxSubnetPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 10, 1, 27),
    _MscAppnLcnVcMaxSubnetPktSize_Type()
)
mscAppnLcnVcMaxSubnetPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcMaxSubnetPktSize.setStatus("mandatory")


class _MscAppnLcnVcTransferPriorityToNetwork_Type(Integer32):
    """Custom type mscAppnLcnVcTransferPriorityToNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              9)
        )
    )
    namedValues = NamedValues(
        *(("high", 9),
          ("normal", 0))
    )


_MscAppnLcnVcTransferPriorityToNetwork_Type.__name__ = "Integer32"
_MscAppnLcnVcTransferPriorityToNetwork_Object = MibTableColumn
mscAppnLcnVcTransferPriorityToNetwork = _MscAppnLcnVcTransferPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 10, 1, 28),
    _MscAppnLcnVcTransferPriorityToNetwork_Type()
)
mscAppnLcnVcTransferPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcTransferPriorityToNetwork.setStatus("mandatory")


class _MscAppnLcnVcTransferPriorityFromNetwork_Type(Integer32):
    """Custom type mscAppnLcnVcTransferPriorityFromNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              9)
        )
    )
    namedValues = NamedValues(
        *(("high", 9),
          ("normal", 0))
    )


_MscAppnLcnVcTransferPriorityFromNetwork_Type.__name__ = "Integer32"
_MscAppnLcnVcTransferPriorityFromNetwork_Object = MibTableColumn
mscAppnLcnVcTransferPriorityFromNetwork = _MscAppnLcnVcTransferPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 10, 1, 29),
    _MscAppnLcnVcTransferPriorityFromNetwork_Type()
)
mscAppnLcnVcTransferPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcTransferPriorityFromNetwork.setStatus("mandatory")
_MscAppnLcnVcIntdTable_Object = MibTable
mscAppnLcnVcIntdTable = _MscAppnLcnVcIntdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 11)
)
if mibBuilder.loadTexts:
    mscAppnLcnVcIntdTable.setStatus("mandatory")
_MscAppnLcnVcIntdEntry_Object = MibTableRow
mscAppnLcnVcIntdEntry = _MscAppnLcnVcIntdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 11, 1)
)
mscAppnLcnVcIntdEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnLcnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnLcnVcIndex"),
)
if mibBuilder.loadTexts:
    mscAppnLcnVcIntdEntry.setStatus("mandatory")


class _MscAppnLcnVcCallReferenceNumber_Type(Hex):
    """Custom type mscAppnLcnVcCallReferenceNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscAppnLcnVcCallReferenceNumber_Type.__name__ = "Hex"
_MscAppnLcnVcCallReferenceNumber_Object = MibTableColumn
mscAppnLcnVcCallReferenceNumber = _MscAppnLcnVcCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 11, 1, 1),
    _MscAppnLcnVcCallReferenceNumber_Type()
)
mscAppnLcnVcCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcCallReferenceNumber.setStatus("mandatory")


class _MscAppnLcnVcElapsedTimeTillNow_Type(Unsigned32):
    """Custom type mscAppnLcnVcElapsedTimeTillNow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscAppnLcnVcElapsedTimeTillNow_Type.__name__ = "Unsigned32"
_MscAppnLcnVcElapsedTimeTillNow_Object = MibTableColumn
mscAppnLcnVcElapsedTimeTillNow = _MscAppnLcnVcElapsedTimeTillNow_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 11, 1, 2),
    _MscAppnLcnVcElapsedTimeTillNow_Type()
)
mscAppnLcnVcElapsedTimeTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcElapsedTimeTillNow.setStatus("mandatory")


class _MscAppnLcnVcSegmentsRx_Type(Unsigned32):
    """Custom type mscAppnLcnVcSegmentsRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscAppnLcnVcSegmentsRx_Type.__name__ = "Unsigned32"
_MscAppnLcnVcSegmentsRx_Object = MibTableColumn
mscAppnLcnVcSegmentsRx = _MscAppnLcnVcSegmentsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 11, 1, 3),
    _MscAppnLcnVcSegmentsRx_Type()
)
mscAppnLcnVcSegmentsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcSegmentsRx.setStatus("mandatory")


class _MscAppnLcnVcSegmentsSent_Type(Unsigned32):
    """Custom type mscAppnLcnVcSegmentsSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscAppnLcnVcSegmentsSent_Type.__name__ = "Unsigned32"
_MscAppnLcnVcSegmentsSent_Object = MibTableColumn
mscAppnLcnVcSegmentsSent = _MscAppnLcnVcSegmentsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 11, 1, 4),
    _MscAppnLcnVcSegmentsSent_Type()
)
mscAppnLcnVcSegmentsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcSegmentsSent.setStatus("mandatory")


class _MscAppnLcnVcStartTime_Type(EnterpriseDateAndTime):
    """Custom type mscAppnLcnVcStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscAppnLcnVcStartTime_Type.__name__ = "EnterpriseDateAndTime"
_MscAppnLcnVcStartTime_Object = MibTableColumn
mscAppnLcnVcStartTime = _MscAppnLcnVcStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 11, 1, 5),
    _MscAppnLcnVcStartTime_Type()
)
mscAppnLcnVcStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcStartTime.setStatus("mandatory")
_MscAppnLcnVcStatsTable_Object = MibTable
mscAppnLcnVcStatsTable = _MscAppnLcnVcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 12)
)
if mibBuilder.loadTexts:
    mscAppnLcnVcStatsTable.setStatus("mandatory")
_MscAppnLcnVcStatsEntry_Object = MibTableRow
mscAppnLcnVcStatsEntry = _MscAppnLcnVcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 12, 1)
)
mscAppnLcnVcStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnLcnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnLcnVcIndex"),
)
if mibBuilder.loadTexts:
    mscAppnLcnVcStatsEntry.setStatus("mandatory")


class _MscAppnLcnVcAckStackingTimeouts_Type(Unsigned32):
    """Custom type mscAppnLcnVcAckStackingTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscAppnLcnVcAckStackingTimeouts_Type.__name__ = "Unsigned32"
_MscAppnLcnVcAckStackingTimeouts_Object = MibTableColumn
mscAppnLcnVcAckStackingTimeouts = _MscAppnLcnVcAckStackingTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 12, 1, 1),
    _MscAppnLcnVcAckStackingTimeouts_Type()
)
mscAppnLcnVcAckStackingTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcAckStackingTimeouts.setStatus("mandatory")


class _MscAppnLcnVcOutOfRangeFrmFromSubnet_Type(Unsigned32):
    """Custom type mscAppnLcnVcOutOfRangeFrmFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscAppnLcnVcOutOfRangeFrmFromSubnet_Type.__name__ = "Unsigned32"
_MscAppnLcnVcOutOfRangeFrmFromSubnet_Object = MibTableColumn
mscAppnLcnVcOutOfRangeFrmFromSubnet = _MscAppnLcnVcOutOfRangeFrmFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 12, 1, 2),
    _MscAppnLcnVcOutOfRangeFrmFromSubnet_Type()
)
mscAppnLcnVcOutOfRangeFrmFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcOutOfRangeFrmFromSubnet.setStatus("mandatory")


class _MscAppnLcnVcDuplicatesFromSubnet_Type(Unsigned32):
    """Custom type mscAppnLcnVcDuplicatesFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscAppnLcnVcDuplicatesFromSubnet_Type.__name__ = "Unsigned32"
_MscAppnLcnVcDuplicatesFromSubnet_Object = MibTableColumn
mscAppnLcnVcDuplicatesFromSubnet = _MscAppnLcnVcDuplicatesFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 12, 1, 3),
    _MscAppnLcnVcDuplicatesFromSubnet_Type()
)
mscAppnLcnVcDuplicatesFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcDuplicatesFromSubnet.setStatus("mandatory")


class _MscAppnLcnVcFrmRetryTimeouts_Type(Unsigned32):
    """Custom type mscAppnLcnVcFrmRetryTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscAppnLcnVcFrmRetryTimeouts_Type.__name__ = "Unsigned32"
_MscAppnLcnVcFrmRetryTimeouts_Object = MibTableColumn
mscAppnLcnVcFrmRetryTimeouts = _MscAppnLcnVcFrmRetryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 12, 1, 4),
    _MscAppnLcnVcFrmRetryTimeouts_Type()
)
mscAppnLcnVcFrmRetryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcFrmRetryTimeouts.setStatus("mandatory")


class _MscAppnLcnVcPeakRetryQueueSize_Type(Unsigned32):
    """Custom type mscAppnLcnVcPeakRetryQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscAppnLcnVcPeakRetryQueueSize_Type.__name__ = "Unsigned32"
_MscAppnLcnVcPeakRetryQueueSize_Object = MibTableColumn
mscAppnLcnVcPeakRetryQueueSize = _MscAppnLcnVcPeakRetryQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 12, 1, 5),
    _MscAppnLcnVcPeakRetryQueueSize_Type()
)
mscAppnLcnVcPeakRetryQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcPeakRetryQueueSize.setStatus("mandatory")


class _MscAppnLcnVcPeakOoSeqQueueSize_Type(Unsigned32):
    """Custom type mscAppnLcnVcPeakOoSeqQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscAppnLcnVcPeakOoSeqQueueSize_Type.__name__ = "Unsigned32"
_MscAppnLcnVcPeakOoSeqQueueSize_Object = MibTableColumn
mscAppnLcnVcPeakOoSeqQueueSize = _MscAppnLcnVcPeakOoSeqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 12, 1, 6),
    _MscAppnLcnVcPeakOoSeqQueueSize_Type()
)
mscAppnLcnVcPeakOoSeqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcPeakOoSeqQueueSize.setStatus("mandatory")


class _MscAppnLcnVcPeakOoSeqFrmForwarded_Type(Unsigned32):
    """Custom type mscAppnLcnVcPeakOoSeqFrmForwarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscAppnLcnVcPeakOoSeqFrmForwarded_Type.__name__ = "Unsigned32"
_MscAppnLcnVcPeakOoSeqFrmForwarded_Object = MibTableColumn
mscAppnLcnVcPeakOoSeqFrmForwarded = _MscAppnLcnVcPeakOoSeqFrmForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 12, 1, 7),
    _MscAppnLcnVcPeakOoSeqFrmForwarded_Type()
)
mscAppnLcnVcPeakOoSeqFrmForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcPeakOoSeqFrmForwarded.setStatus("mandatory")


class _MscAppnLcnVcPeakStackedAcksRx_Type(Unsigned32):
    """Custom type mscAppnLcnVcPeakStackedAcksRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscAppnLcnVcPeakStackedAcksRx_Type.__name__ = "Unsigned32"
_MscAppnLcnVcPeakStackedAcksRx_Object = MibTableColumn
mscAppnLcnVcPeakStackedAcksRx = _MscAppnLcnVcPeakStackedAcksRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 12, 1, 8),
    _MscAppnLcnVcPeakStackedAcksRx_Type()
)
mscAppnLcnVcPeakStackedAcksRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcPeakStackedAcksRx.setStatus("mandatory")


class _MscAppnLcnVcSubnetRecoveries_Type(Unsigned32):
    """Custom type mscAppnLcnVcSubnetRecoveries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscAppnLcnVcSubnetRecoveries_Type.__name__ = "Unsigned32"
_MscAppnLcnVcSubnetRecoveries_Object = MibTableColumn
mscAppnLcnVcSubnetRecoveries = _MscAppnLcnVcSubnetRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 12, 1, 9),
    _MscAppnLcnVcSubnetRecoveries_Type()
)
mscAppnLcnVcSubnetRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcSubnetRecoveries.setStatus("mandatory")


class _MscAppnLcnVcWindowClosuresToSubnet_Type(Unsigned32):
    """Custom type mscAppnLcnVcWindowClosuresToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscAppnLcnVcWindowClosuresToSubnet_Type.__name__ = "Unsigned32"
_MscAppnLcnVcWindowClosuresToSubnet_Object = MibTableColumn
mscAppnLcnVcWindowClosuresToSubnet = _MscAppnLcnVcWindowClosuresToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 12, 1, 10),
    _MscAppnLcnVcWindowClosuresToSubnet_Type()
)
mscAppnLcnVcWindowClosuresToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcWindowClosuresToSubnet.setStatus("mandatory")


class _MscAppnLcnVcWindowClosuresFromSubnet_Type(Unsigned32):
    """Custom type mscAppnLcnVcWindowClosuresFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscAppnLcnVcWindowClosuresFromSubnet_Type.__name__ = "Unsigned32"
_MscAppnLcnVcWindowClosuresFromSubnet_Object = MibTableColumn
mscAppnLcnVcWindowClosuresFromSubnet = _MscAppnLcnVcWindowClosuresFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 12, 1, 11),
    _MscAppnLcnVcWindowClosuresFromSubnet_Type()
)
mscAppnLcnVcWindowClosuresFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcWindowClosuresFromSubnet.setStatus("mandatory")


class _MscAppnLcnVcWrTriggers_Type(Unsigned32):
    """Custom type mscAppnLcnVcWrTriggers based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscAppnLcnVcWrTriggers_Type.__name__ = "Unsigned32"
_MscAppnLcnVcWrTriggers_Object = MibTableColumn
mscAppnLcnVcWrTriggers = _MscAppnLcnVcWrTriggers_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 3, 12, 1, 12),
    _MscAppnLcnVcWrTriggers_Type()
)
mscAppnLcnVcWrTriggers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnVcWrTriggers.setStatus("mandatory")
_MscAppnLcnStateTable_Object = MibTable
mscAppnLcnStateTable = _MscAppnLcnStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 10)
)
if mibBuilder.loadTexts:
    mscAppnLcnStateTable.setStatus("mandatory")
_MscAppnLcnStateEntry_Object = MibTableRow
mscAppnLcnStateEntry = _MscAppnLcnStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 10, 1)
)
mscAppnLcnStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnLcnIndex"),
)
if mibBuilder.loadTexts:
    mscAppnLcnStateEntry.setStatus("mandatory")


class _MscAppnLcnAdminState_Type(Integer32):
    """Custom type mscAppnLcnAdminState based on Integer32"""
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


_MscAppnLcnAdminState_Type.__name__ = "Integer32"
_MscAppnLcnAdminState_Object = MibTableColumn
mscAppnLcnAdminState = _MscAppnLcnAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 10, 1, 1),
    _MscAppnLcnAdminState_Type()
)
mscAppnLcnAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnAdminState.setStatus("mandatory")


class _MscAppnLcnOperationalState_Type(Integer32):
    """Custom type mscAppnLcnOperationalState based on Integer32"""
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


_MscAppnLcnOperationalState_Type.__name__ = "Integer32"
_MscAppnLcnOperationalState_Object = MibTableColumn
mscAppnLcnOperationalState = _MscAppnLcnOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 10, 1, 2),
    _MscAppnLcnOperationalState_Type()
)
mscAppnLcnOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnOperationalState.setStatus("mandatory")


class _MscAppnLcnUsageState_Type(Integer32):
    """Custom type mscAppnLcnUsageState based on Integer32"""
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


_MscAppnLcnUsageState_Type.__name__ = "Integer32"
_MscAppnLcnUsageState_Object = MibTableColumn
mscAppnLcnUsageState = _MscAppnLcnUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 4, 10, 1, 3),
    _MscAppnLcnUsageState_Type()
)
mscAppnLcnUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLcnUsageState.setStatus("mandatory")
_MscAppnPort_ObjectIdentity = ObjectIdentity
mscAppnPort = _MscAppnPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5)
)
_MscAppnPortRowStatusTable_Object = MibTable
mscAppnPortRowStatusTable = _MscAppnPortRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 1)
)
if mibBuilder.loadTexts:
    mscAppnPortRowStatusTable.setStatus("mandatory")
_MscAppnPortRowStatusEntry_Object = MibTableRow
mscAppnPortRowStatusEntry = _MscAppnPortRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 1, 1)
)
mscAppnPortRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnPortIndex"),
)
if mibBuilder.loadTexts:
    mscAppnPortRowStatusEntry.setStatus("mandatory")
_MscAppnPortRowStatus_Type = RowStatus
_MscAppnPortRowStatus_Object = MibTableColumn
mscAppnPortRowStatus = _MscAppnPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 1, 1, 1),
    _MscAppnPortRowStatus_Type()
)
mscAppnPortRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnPortRowStatus.setStatus("mandatory")
_MscAppnPortComponentName_Type = DisplayString
_MscAppnPortComponentName_Object = MibTableColumn
mscAppnPortComponentName = _MscAppnPortComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 1, 1, 2),
    _MscAppnPortComponentName_Type()
)
mscAppnPortComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnPortComponentName.setStatus("mandatory")
_MscAppnPortStorageType_Type = StorageType
_MscAppnPortStorageType_Object = MibTableColumn
mscAppnPortStorageType = _MscAppnPortStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 1, 1, 4),
    _MscAppnPortStorageType_Type()
)
mscAppnPortStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnPortStorageType.setStatus("mandatory")


class _MscAppnPortIndex_Type(AsciiStringIndex):
    """Custom type mscAppnPortIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MscAppnPortIndex_Type.__name__ = "AsciiStringIndex"
_MscAppnPortIndex_Object = MibTableColumn
mscAppnPortIndex = _MscAppnPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 1, 1, 10),
    _MscAppnPortIndex_Type()
)
mscAppnPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnPortIndex.setStatus("mandatory")
_MscAppnPortConfigTable_Object = MibTable
mscAppnPortConfigTable = _MscAppnPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 10)
)
if mibBuilder.loadTexts:
    mscAppnPortConfigTable.setStatus("mandatory")
_MscAppnPortConfigEntry_Object = MibTableRow
mscAppnPortConfigEntry = _MscAppnPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 10, 1)
)
mscAppnPortConfigEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnPortIndex"),
)
if mibBuilder.loadTexts:
    mscAppnPortConfigEntry.setStatus("mandatory")


class _MscAppnPortType_Type(Integer32):
    """Custom type mscAppnPortType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonSwitched", 1),
          ("sharedAccessFacilities", 3),
          ("switched", 2))
    )


_MscAppnPortType_Type.__name__ = "Integer32"
_MscAppnPortType_Object = MibTableColumn
mscAppnPortType = _MscAppnPortType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 10, 1, 1),
    _MscAppnPortType_Type()
)
mscAppnPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnPortType.setStatus("mandatory")


class _MscAppnPortMaxRxBtuSize_Type(Unsigned32):
    """Custom type mscAppnPortMaxRxBtuSize based on Unsigned32"""
    defaultValue = 2048

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnPortMaxRxBtuSize_Type.__name__ = "Unsigned32"
_MscAppnPortMaxRxBtuSize_Object = MibTableColumn
mscAppnPortMaxRxBtuSize = _MscAppnPortMaxRxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 10, 1, 2),
    _MscAppnPortMaxRxBtuSize_Type()
)
mscAppnPortMaxRxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnPortMaxRxBtuSize.setStatus("mandatory")


class _MscAppnPortMaxTxBtuSize_Type(Unsigned32):
    """Custom type mscAppnPortMaxTxBtuSize based on Unsigned32"""
    defaultValue = 2048

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnPortMaxTxBtuSize_Type.__name__ = "Unsigned32"
_MscAppnPortMaxTxBtuSize_Object = MibTableColumn
mscAppnPortMaxTxBtuSize = _MscAppnPortMaxTxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 10, 1, 3),
    _MscAppnPortMaxTxBtuSize_Type()
)
mscAppnPortMaxTxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnPortMaxTxBtuSize.setStatus("mandatory")


class _MscAppnPortTotLinkActLim_Type(Unsigned32):
    """Custom type mscAppnPortTotLinkActLim based on Unsigned32"""
    defaultValue = 99

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_MscAppnPortTotLinkActLim_Type.__name__ = "Unsigned32"
_MscAppnPortTotLinkActLim_Object = MibTableColumn
mscAppnPortTotLinkActLim = _MscAppnPortTotLinkActLim_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 10, 1, 4),
    _MscAppnPortTotLinkActLim_Type()
)
mscAppnPortTotLinkActLim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnPortTotLinkActLim.setStatus("mandatory")


class _MscAppnPortInbLinkActLim_Type(Unsigned32):
    """Custom type mscAppnPortInbLinkActLim based on Unsigned32"""
    defaultValue = 97

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_MscAppnPortInbLinkActLim_Type.__name__ = "Unsigned32"
_MscAppnPortInbLinkActLim_Object = MibTableColumn
mscAppnPortInbLinkActLim = _MscAppnPortInbLinkActLim_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 10, 1, 5),
    _MscAppnPortInbLinkActLim_Type()
)
mscAppnPortInbLinkActLim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnPortInbLinkActLim.setStatus("mandatory")


class _MscAppnPortOutLinkActLim_Type(Unsigned32):
    """Custom type mscAppnPortOutLinkActLim based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_MscAppnPortOutLinkActLim_Type.__name__ = "Unsigned32"
_MscAppnPortOutLinkActLim_Object = MibTableColumn
mscAppnPortOutLinkActLim = _MscAppnPortOutLinkActLim_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 10, 1, 6),
    _MscAppnPortOutLinkActLim_Type()
)
mscAppnPortOutLinkActLim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnPortOutLinkActLim.setStatus("mandatory")


class _MscAppnPortLsRole_Type(Integer32):
    """Custom type mscAppnPortLsRole based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("negotiable", 3),
          ("primary", 1),
          ("secondary", 2))
    )


_MscAppnPortLsRole_Type.__name__ = "Integer32"
_MscAppnPortLsRole_Object = MibTableColumn
mscAppnPortLsRole = _MscAppnPortLsRole_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 10, 1, 7),
    _MscAppnPortLsRole_Type()
)
mscAppnPortLsRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnPortLsRole.setStatus("mandatory")


class _MscAppnPortActXidExchLim_Type(Unsigned32):
    """Custom type mscAppnPortActXidExchLim based on Unsigned32"""
    defaultValue = 9

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnPortActXidExchLim_Type.__name__ = "Unsigned32"
_MscAppnPortActXidExchLim_Object = MibTableColumn
mscAppnPortActXidExchLim = _MscAppnPortActXidExchLim_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 10, 1, 8),
    _MscAppnPortActXidExchLim_Type()
)
mscAppnPortActXidExchLim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnPortActXidExchLim.setStatus("mandatory")


class _MscAppnPortNonactXidExchLim_Type(Unsigned32):
    """Custom type mscAppnPortNonactXidExchLim based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnPortNonactXidExchLim_Type.__name__ = "Unsigned32"
_MscAppnPortNonactXidExchLim_Object = MibTableColumn
mscAppnPortNonactXidExchLim = _MscAppnPortNonactXidExchLim_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 10, 1, 9),
    _MscAppnPortNonactXidExchLim_Type()
)
mscAppnPortNonactXidExchLim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnPortNonactXidExchLim.setStatus("mandatory")


class _MscAppnPortLsXmitRxCap_Type(Integer32):
    """Custom type mscAppnPortLsXmitRxCap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("twa", 0),
          ("tws", 1))
    )


_MscAppnPortLsXmitRxCap_Type.__name__ = "Integer32"
_MscAppnPortLsXmitRxCap_Object = MibTableColumn
mscAppnPortLsXmitRxCap = _MscAppnPortLsXmitRxCap_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 10, 1, 10),
    _MscAppnPortLsXmitRxCap_Type()
)
mscAppnPortLsXmitRxCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnPortLsXmitRxCap.setStatus("mandatory")


class _MscAppnPortMaxIfrmRxWindow_Type(Unsigned32):
    """Custom type mscAppnPortMaxIfrmRxWindow based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_MscAppnPortMaxIfrmRxWindow_Type.__name__ = "Unsigned32"
_MscAppnPortMaxIfrmRxWindow_Object = MibTableColumn
mscAppnPortMaxIfrmRxWindow = _MscAppnPortMaxIfrmRxWindow_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 10, 1, 11),
    _MscAppnPortMaxIfrmRxWindow_Type()
)
mscAppnPortMaxIfrmRxWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnPortMaxIfrmRxWindow.setStatus("mandatory")


class _MscAppnPortTargetPacingCount_Type(Unsigned32):
    """Custom type mscAppnPortTargetPacingCount based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnPortTargetPacingCount_Type.__name__ = "Unsigned32"
_MscAppnPortTargetPacingCount_Object = MibTableColumn
mscAppnPortTargetPacingCount = _MscAppnPortTargetPacingCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 10, 1, 12),
    _MscAppnPortTargetPacingCount_Type()
)
mscAppnPortTargetPacingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnPortTargetPacingCount.setStatus("mandatory")
_MscAppnPortOperTable_Object = MibTable
mscAppnPortOperTable = _MscAppnPortOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 11)
)
if mibBuilder.loadTexts:
    mscAppnPortOperTable.setStatus("mandatory")
_MscAppnPortOperEntry_Object = MibTableRow
mscAppnPortOperEntry = _MscAppnPortOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 11, 1)
)
mscAppnPortOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnPortIndex"),
)
if mibBuilder.loadTexts:
    mscAppnPortOperEntry.setStatus("mandatory")


class _MscAppnPortState_Type(Integer32):
    """Custom type mscAppnPortState based on Integer32"""
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
        *(("active", 3),
          ("inactive", 1),
          ("pendingActive", 2),
          ("pendingInactive", 4))
    )


_MscAppnPortState_Type.__name__ = "Integer32"
_MscAppnPortState_Object = MibTableColumn
mscAppnPortState = _MscAppnPortState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 11, 1, 1),
    _MscAppnPortState_Type()
)
mscAppnPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnPortState.setStatus("mandatory")


class _MscAppnPortDlcType_Type(Integer32):
    """Custom type mscAppnPortDlcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("frameRelay", 30),
          ("other", 1),
          ("sdlc", 2),
          ("tokenRing", 6),
          ("x25", 31))
    )


_MscAppnPortDlcType_Type.__name__ = "Integer32"
_MscAppnPortDlcType_Object = MibTableColumn
mscAppnPortDlcType = _MscAppnPortDlcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 11, 1, 2),
    _MscAppnPortDlcType_Type()
)
mscAppnPortDlcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnPortDlcType.setStatus("mandatory")


class _MscAppnPortSimRim_Type(Integer32):
    """Custom type mscAppnPortSimRim based on Integer32"""
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


_MscAppnPortSimRim_Type.__name__ = "Integer32"
_MscAppnPortSimRim_Object = MibTableColumn
mscAppnPortSimRim = _MscAppnPortSimRim_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 11, 1, 3),
    _MscAppnPortSimRim_Type()
)
mscAppnPortSimRim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnPortSimRim.setStatus("mandatory")
_MscAppnPortDefinedLsGoodXids_Type = PassportCounter64
_MscAppnPortDefinedLsGoodXids_Object = MibTableColumn
mscAppnPortDefinedLsGoodXids = _MscAppnPortDefinedLsGoodXids_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 11, 1, 4),
    _MscAppnPortDefinedLsGoodXids_Type()
)
mscAppnPortDefinedLsGoodXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnPortDefinedLsGoodXids.setStatus("mandatory")
_MscAppnPortDefinedLsBadXids_Type = PassportCounter64
_MscAppnPortDefinedLsBadXids_Object = MibTableColumn
mscAppnPortDefinedLsBadXids = _MscAppnPortDefinedLsBadXids_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 11, 1, 5),
    _MscAppnPortDefinedLsBadXids_Type()
)
mscAppnPortDefinedLsBadXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnPortDefinedLsBadXids.setStatus("mandatory")
_MscAppnPortDynLsGoodXids_Type = PassportCounter64
_MscAppnPortDynLsGoodXids_Object = MibTableColumn
mscAppnPortDynLsGoodXids = _MscAppnPortDynLsGoodXids_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 11, 1, 6),
    _MscAppnPortDynLsGoodXids_Type()
)
mscAppnPortDynLsGoodXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnPortDynLsGoodXids.setStatus("mandatory")
_MscAppnPortDynLsBadXids_Type = PassportCounter64
_MscAppnPortDynLsBadXids_Object = MibTableColumn
mscAppnPortDynLsBadXids = _MscAppnPortDynLsBadXids_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 11, 1, 7),
    _MscAppnPortDynLsBadXids_Type()
)
mscAppnPortDynLsBadXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnPortDynLsBadXids.setStatus("mandatory")
_MscAppnPortTgCharTable_Object = MibTable
mscAppnPortTgCharTable = _MscAppnPortTgCharTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 12)
)
if mibBuilder.loadTexts:
    mscAppnPortTgCharTable.setStatus("mandatory")
_MscAppnPortTgCharEntry_Object = MibTableRow
mscAppnPortTgCharEntry = _MscAppnPortTgCharEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 12, 1)
)
mscAppnPortTgCharEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnPortIndex"),
)
if mibBuilder.loadTexts:
    mscAppnPortTgCharEntry.setStatus("mandatory")


class _MscAppnPortEffectiveCap_Type(Integer32):
    """Custom type mscAppnPortEffectiveCap based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("min", 0),
          ("n1000kbps", 101),
          ("n10100Mbps", 208),
          ("n101Gbps", 234),
          ("n1020Mbps", 181),
          ("n1050bps", 22),
          ("n106kbps", 75),
          ("n10800bps", 49),
          ("n1080kbps", 102),
          ("n108Mbps", 155),
          ("n1100Mbps", 182),
          ("n11100kbps", 129),
          ("n111Gbps", 235),
          ("n11300Mbps", 209),
          ("n1130bps", 23),
          ("n1150kbps", 103),
          ("n115kbps", 76),
          ("n1180Mbps", 183),
          ("n118Mbps", 156),
          ("n12000bps", 50),
          ("n1200bps", 24),
          ("n121Gbps", 236),
          ("n12300kbps", 130),
          ("n1230kbps", 104),
          ("n125kbps", 77),
          ("n12600Mbps", 210),
          ("n1260Mbps", 184),
          ("n128Mbps", 157),
          ("n131Gbps", 237),
          ("n13200bps", 51),
          ("n134kbps", 78),
          ("n13500kbps", 131),
          ("n1350bps", 25),
          ("n13800Mbps", 211),
          ("n1380kbps", 105),
          ("n138Mbps", 158),
          ("n141Gbps", 238),
          ("n1420Mbps", 185),
          ("n14400bps", 52),
          ("n144kbps", 79),
          ("n14700kbps", 132),
          ("n147Mbps", 159),
          ("n1500bps", 26),
          ("n15100Mbps", 212),
          ("n151Gbps", 239),
          ("n1540kbps", 106),
          ("n154kbps", 80),
          ("n15600bps", 53),
          ("n1570Mbps", 186),
          ("n157Mbps", 160),
          ("n160Gbps", 240),
          ("n16Gbps", 213),
          ("n16Mbps", 133),
          ("n1700Mbps", 187),
          ("n1700bps", 27),
          ("n1700kbps", 107),
          ("n170bps", 1),
          ("n170kbps", 81),
          ("n17Mbps", 134),
          ("n17kbps", 54),
          ("n1800bps", 28),
          ("n1800kbps", 108),
          ("n180Gbps", 241),
          ("n180Mbps", 161),
          ("n18Gbps", 214),
          ("n18Mbps", 135),
          ("n18kbps", 55),
          ("n1900Mbps", 188),
          ("n190bps", 2),
          ("n190kbps", 82),
          ("n19Gbps", 215),
          ("n19kbps", 56),
          ("n2000Mbps", 189),
          ("n2000bps", 29),
          ("n2000kbps", 109),
          ("n200Gbps", 242),
          ("n200Mbps", 162),
          ("n20Gbps", 216),
          ("n20Mbps", 136),
          ("n2100bps", 30),
          ("n210bps", 3),
          ("n210kbps", 83),
          ("n2200Mbps", 190),
          ("n2200kbps", 110),
          ("n220Gbps", 243),
          ("n220Mbps", 163),
          ("n22Mbps", 137),
          ("n22kbps", 57),
          ("n2300bps", 31),
          ("n2300kbps", 111),
          ("n230bps", 4),
          ("n230kbps", 84),
          ("n23Gbps", 217),
          ("n2400Mbps", 191),
          ("n2400bps", 32),
          ("n240Gbps", 244),
          ("n240Mbps", 164),
          ("n240bps", 5),
          ("n24kbps", 58),
          ("n2500Mbps", 192),
          ("n2500kbps", 112),
          ("n250kbps", 85),
          ("n25Gbps", 218),
          ("n25Mbps", 138),
          ("n260Gbps", 245),
          ("n260Mbps", 165),
          ("n260bps", 6),
          ("n26kbps", 59),
          ("n2700bps", 33),
          ("n270kbps", 86),
          ("n27Mbps", 139),
          ("n2800Mbps", 193),
          ("n2800kbps", 113),
          ("n280Gbps", 246),
          ("n280Mbps", 166),
          ("n280bps", 7),
          ("n28Gbps", 219),
          ("n290Mbps", 167),
          ("n290kbps", 87),
          ("n29Mbps", 140),
          ("n29kbps", 60),
          ("n3000bps", 34),
          ("n300Gbps", 247),
          ("n300bps", 8),
          ("n30Gbps", 220),
          ("n3100Mbps", 194),
          ("n3100kbps", 114),
          ("n310Mbps", 168),
          ("n310kbps", 88),
          ("n31kbps", 61),
          ("n320Gbps", 248),
          ("n32Mbps", 141),
          ("n3300bps", 35),
          ("n33Gbps", 221),
          ("n3400kbps", 115),
          ("n340bps", 9),
          ("n34Mbps", 142),
          ("n34kbps", 62),
          ("n3500Mbps", 195),
          ("n350Mbps", 169),
          ("n350kbps", 89),
          ("n35Gbps", 222),
          ("n3600bps", 36),
          ("n360Gbps", 249),
          ("n36kbps", 63),
          ("n3700kbps", 116),
          ("n37Mbps", 143),
          ("n3800Mbps", 196),
          ("n380bps", 10),
          ("n380kbps", 90),
          ("n38Gbps", 223),
          ("n38kbps", 64),
          ("n3900bps", 37),
          ("n390Mbps", 170),
          ("n39Mbps", 144),
          ("n4000kbps", 117),
          ("n400Gbps", 250),
          ("n40Gbps", 224),
          ("n4100Mbps", 197),
          ("n410bps", 11),
          ("n4200bps", 38),
          ("n420kbps", 91),
          ("n4300kbps", 118),
          ("n430Mbps", 171),
          ("n43kbps", 65),
          ("n4400Mbps", 198),
          ("n440Gbps", 251),
          ("n44Mbps", 145),
          ("n4500bps", 39),
          ("n450bps", 12),
          ("n45Gbps", 225),
          ("n4600kbps", 119),
          ("n460kbps", 92),
          ("n4700Mbps", 199),
          ("n470Mbps", 172),
          ("n4800bps", 40),
          ("n480Gbps", 252),
          ("n48kbps", 66),
          ("n4900kbps", 120),
          ("n490bps", 13),
          ("n49Mbps", 146),
          ("n5000Mbps", 200),
          ("n500kbps", 93),
          ("n50Gbps", 226),
          ("n510Mbps", 173),
          ("n520Gbps", 253),
          ("n530bps", 14),
          ("n53kbps", 67),
          ("n5400bps", 41),
          ("n540kbps", 94),
          ("n54Mbps", 147),
          ("n5500kbps", 121),
          ("n550Mbps", 174),
          ("n55Gbps", 227),
          ("n560Gbps", 254),
          ("n560bps", 15),
          ("n5700Mbps", 201),
          ("n580kbps", 95),
          ("n58kbps", 68),
          ("n590Mbps", 175),
          ("n59Mbps", 148),
          ("n6000bps", 42),
          ("n600Gbps", 255),
          ("n600bps", 16),
          ("n60Gbps", 228),
          ("n6100kbps", 122),
          ("n610kbps", 96),
          ("n62kbps", 69),
          ("n6300Mbps", 202),
          ("n630Mbps", 176),
          ("n64Mbps", 149),
          ("n65Gbps", 229),
          ("n6600bps", 43),
          ("n67kbps", 70),
          ("n6800kbps", 123),
          ("n680bps", 17),
          ("n6900Mbps", 203),
          ("n690kbps", 97),
          ("n69Mbps", 150),
          ("n70Gbps", 230),
          ("n710Mbps", 177),
          ("n7200bps", 44),
          ("n72kbps", 71),
          ("n7400kbps", 124),
          ("n74Mbps", 151),
          ("n7500Mbps", 204),
          ("n750bps", 18),
          ("n75Gbps", 231),
          ("n770kbps", 98),
          ("n77kbps", 72),
          ("n7800bps", 45),
          ("n790Mbps", 178),
          ("n79Mbps", 152),
          ("n8000kbps", 125),
          ("n81Gbps", 232),
          ("n8200Mbps", 205),
          ("n830bps", 19),
          ("n8400bps", 46),
          ("n840kbps", 99),
          ("n8600kbps", 126),
          ("n86kbps", 73),
          ("n870Mbps", 179),
          ("n8800Mbps", 206),
          ("n88Mbps", 153),
          ("n9000bps", 47),
          ("n900bps", 20),
          ("n91Gbps", 233),
          ("n9200kbps", 127),
          ("n920kbps", 100),
          ("n9400Mbps", 207),
          ("n940Mbps", 180),
          ("n9600bps", 48),
          ("n96kbps", 74),
          ("n9800kbps", 128),
          ("n980bps", 21),
          ("n98Mbps", 154))
    )


_MscAppnPortEffectiveCap_Type.__name__ = "Integer32"
_MscAppnPortEffectiveCap_Object = MibTableColumn
mscAppnPortEffectiveCap = _MscAppnPortEffectiveCap_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 12, 1, 1),
    _MscAppnPortEffectiveCap_Type()
)
mscAppnPortEffectiveCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnPortEffectiveCap.setStatus("mandatory")


class _MscAppnPortConnectCost_Type(Integer32):
    """Custom type mscAppnPortConnectCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnPortConnectCost_Type.__name__ = "Integer32"
_MscAppnPortConnectCost_Object = MibTableColumn
mscAppnPortConnectCost = _MscAppnPortConnectCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 12, 1, 2),
    _MscAppnPortConnectCost_Type()
)
mscAppnPortConnectCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnPortConnectCost.setStatus("mandatory")


class _MscAppnPortByteCost_Type(Integer32):
    """Custom type mscAppnPortByteCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnPortByteCost_Type.__name__ = "Integer32"
_MscAppnPortByteCost_Object = MibTableColumn
mscAppnPortByteCost = _MscAppnPortByteCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 12, 1, 3),
    _MscAppnPortByteCost_Type()
)
mscAppnPortByteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnPortByteCost.setStatus("mandatory")


class _MscAppnPortSecurity_Type(Integer32):
    """Custom type mscAppnPortSecurity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              32,
              64,
              96,
              128,
              160,
              192)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 160),
          ("guardedConduit", 128),
          ("guardedRadiation", 192),
          ("nonSecure", 1),
          ("publicSwitchedNetwork", 32),
          ("secureConduit", 96),
          ("unKnown", 0),
          ("undergroundCable", 64))
    )


_MscAppnPortSecurity_Type.__name__ = "Integer32"
_MscAppnPortSecurity_Object = MibTableColumn
mscAppnPortSecurity = _MscAppnPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 12, 1, 4),
    _MscAppnPortSecurity_Type()
)
mscAppnPortSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnPortSecurity.setStatus("mandatory")


class _MscAppnPortPropagationDelay_Type(Integer32):
    """Custom type mscAppnPortPropagationDelay based on Integer32"""
    defaultValue = 113

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              76,
              113,
              145,
              153)
        )
    )
    namedValues = NamedValues(
        *(("long", 153),
          ("minimum", 0),
          ("negligible", 76),
          ("packetSwitched", 145),
          ("terrestrial", 113))
    )


_MscAppnPortPropagationDelay_Type.__name__ = "Integer32"
_MscAppnPortPropagationDelay_Object = MibTableColumn
mscAppnPortPropagationDelay = _MscAppnPortPropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 12, 1, 5),
    _MscAppnPortPropagationDelay_Type()
)
mscAppnPortPropagationDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnPortPropagationDelay.setStatus("mandatory")


class _MscAppnPortUserDefinedParm1_Type(Unsigned32):
    """Custom type mscAppnPortUserDefinedParm1 based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnPortUserDefinedParm1_Type.__name__ = "Unsigned32"
_MscAppnPortUserDefinedParm1_Object = MibTableColumn
mscAppnPortUserDefinedParm1 = _MscAppnPortUserDefinedParm1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 12, 1, 7),
    _MscAppnPortUserDefinedParm1_Type()
)
mscAppnPortUserDefinedParm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnPortUserDefinedParm1.setStatus("mandatory")


class _MscAppnPortUserDefinedParm2_Type(Unsigned32):
    """Custom type mscAppnPortUserDefinedParm2 based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnPortUserDefinedParm2_Type.__name__ = "Unsigned32"
_MscAppnPortUserDefinedParm2_Object = MibTableColumn
mscAppnPortUserDefinedParm2 = _MscAppnPortUserDefinedParm2_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 12, 1, 8),
    _MscAppnPortUserDefinedParm2_Type()
)
mscAppnPortUserDefinedParm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnPortUserDefinedParm2.setStatus("mandatory")


class _MscAppnPortUserDefinedParm3_Type(Unsigned32):
    """Custom type mscAppnPortUserDefinedParm3 based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnPortUserDefinedParm3_Type.__name__ = "Unsigned32"
_MscAppnPortUserDefinedParm3_Object = MibTableColumn
mscAppnPortUserDefinedParm3 = _MscAppnPortUserDefinedParm3_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 5, 12, 1, 9),
    _MscAppnPortUserDefinedParm3_Type()
)
mscAppnPortUserDefinedParm3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnPortUserDefinedParm3.setStatus("mandatory")
_MscAppnLs_ObjectIdentity = ObjectIdentity
mscAppnLs = _MscAppnLs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6)
)
_MscAppnLsRowStatusTable_Object = MibTable
mscAppnLsRowStatusTable = _MscAppnLsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 1)
)
if mibBuilder.loadTexts:
    mscAppnLsRowStatusTable.setStatus("mandatory")
_MscAppnLsRowStatusEntry_Object = MibTableRow
mscAppnLsRowStatusEntry = _MscAppnLsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 1, 1)
)
mscAppnLsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnLsIndex"),
)
if mibBuilder.loadTexts:
    mscAppnLsRowStatusEntry.setStatus("mandatory")
_MscAppnLsRowStatus_Type = RowStatus
_MscAppnLsRowStatus_Object = MibTableColumn
mscAppnLsRowStatus = _MscAppnLsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 1, 1, 1),
    _MscAppnLsRowStatus_Type()
)
mscAppnLsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsRowStatus.setStatus("mandatory")
_MscAppnLsComponentName_Type = DisplayString
_MscAppnLsComponentName_Object = MibTableColumn
mscAppnLsComponentName = _MscAppnLsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 1, 1, 2),
    _MscAppnLsComponentName_Type()
)
mscAppnLsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsComponentName.setStatus("mandatory")
_MscAppnLsStorageType_Type = StorageType
_MscAppnLsStorageType_Object = MibTableColumn
mscAppnLsStorageType = _MscAppnLsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 1, 1, 4),
    _MscAppnLsStorageType_Type()
)
mscAppnLsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsStorageType.setStatus("mandatory")


class _MscAppnLsIndex_Type(AsciiStringIndex):
    """Custom type mscAppnLsIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MscAppnLsIndex_Type.__name__ = "AsciiStringIndex"
_MscAppnLsIndex_Object = MibTableColumn
mscAppnLsIndex = _MscAppnLsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 1, 1, 10),
    _MscAppnLsIndex_Type()
)
mscAppnLsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnLsIndex.setStatus("mandatory")
_MscAppnLsLsVcReferenceTable_Object = MibTable
mscAppnLsLsVcReferenceTable = _MscAppnLsLsVcReferenceTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 10)
)
if mibBuilder.loadTexts:
    mscAppnLsLsVcReferenceTable.setStatus("mandatory")
_MscAppnLsLsVcReferenceEntry_Object = MibTableRow
mscAppnLsLsVcReferenceEntry = _MscAppnLsLsVcReferenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 10, 1)
)
mscAppnLsLsVcReferenceEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnLsIndex"),
)
if mibBuilder.loadTexts:
    mscAppnLsLsVcReferenceEntry.setStatus("mandatory")
_MscAppnLsName_Type = RowPointer
_MscAppnLsName_Object = MibTableColumn
mscAppnLsName = _MscAppnLsName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 10, 1, 1),
    _MscAppnLsName_Type()
)
mscAppnLsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsName.setStatus("mandatory")


class _MscAppnLsSap_Type(Hex):
    """Custom type mscAppnLsSap based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 252),
    )


_MscAppnLsSap_Type.__name__ = "Hex"
_MscAppnLsSap_Object = MibTableColumn
mscAppnLsSap = _MscAppnLsSap_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 10, 1, 2),
    _MscAppnLsSap_Type()
)
mscAppnLsSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsSap.setStatus("mandatory")
_MscAppnLsConfigTable_Object = MibTable
mscAppnLsConfigTable = _MscAppnLsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 11)
)
if mibBuilder.loadTexts:
    mscAppnLsConfigTable.setStatus("mandatory")
_MscAppnLsConfigEntry_Object = MibTableRow
mscAppnLsConfigEntry = _MscAppnLsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 11, 1)
)
mscAppnLsConfigEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnLsIndex"),
)
if mibBuilder.loadTexts:
    mscAppnLsConfigEntry.setStatus("mandatory")


class _MscAppnLsPortName_Type(AsciiString):
    """Custom type mscAppnLsPortName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MscAppnLsPortName_Type.__name__ = "AsciiString"
_MscAppnLsPortName_Object = MibTableColumn
mscAppnLsPortName = _MscAppnLsPortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 11, 1, 1),
    _MscAppnLsPortName_Type()
)
mscAppnLsPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsPortName.setStatus("mandatory")


class _MscAppnLsFeatures_Type(OctetString):
    """Custom type mscAppnLsFeatures based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAppnLsFeatures_Type.__name__ = "OctetString"
_MscAppnLsFeatures_Object = MibTableColumn
mscAppnLsFeatures = _MscAppnLsFeatures_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 11, 1, 4),
    _MscAppnLsFeatures_Type()
)
mscAppnLsFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsFeatures.setStatus("mandatory")


class _MscAppnLsMaxTxBtuSize_Type(Unsigned32):
    """Custom type mscAppnLsMaxTxBtuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscAppnLsMaxTxBtuSize_Type.__name__ = "Unsigned32"
_MscAppnLsMaxTxBtuSize_Object = MibTableColumn
mscAppnLsMaxTxBtuSize = _MscAppnLsMaxTxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 11, 1, 6),
    _MscAppnLsMaxTxBtuSize_Type()
)
mscAppnLsMaxTxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsMaxTxBtuSize.setStatus("mandatory")
_MscAppnLsOperTable_Object = MibTable
mscAppnLsOperTable = _MscAppnLsOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 12)
)
if mibBuilder.loadTexts:
    mscAppnLsOperTable.setStatus("mandatory")
_MscAppnLsOperEntry_Object = MibTableRow
mscAppnLsOperEntry = _MscAppnLsOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 12, 1)
)
mscAppnLsOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnLsIndex"),
)
if mibBuilder.loadTexts:
    mscAppnLsOperEntry.setStatus("mandatory")


class _MscAppnLsDlcType_Type(Integer32):
    """Custom type mscAppnLsDlcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("llc2", 30),
          ("other", 1),
          ("sdlc", 2),
          ("tokenRing", 6),
          ("x25", 31))
    )


_MscAppnLsDlcType_Type.__name__ = "Integer32"
_MscAppnLsDlcType_Object = MibTableColumn
mscAppnLsDlcType = _MscAppnLsDlcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 12, 1, 1),
    _MscAppnLsDlcType_Type()
)
mscAppnLsDlcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsDlcType.setStatus("mandatory")


class _MscAppnLsLinkStationState_Type(Integer32):
    """Custom type mscAppnLsLinkStationState based on Integer32"""
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
        *(("active", 3),
          ("inactive", 1),
          ("pendingActive", 2),
          ("pendingInactive", 4))
    )


_MscAppnLsLinkStationState_Type.__name__ = "Integer32"
_MscAppnLsLinkStationState_Object = MibTableColumn
mscAppnLsLinkStationState = _MscAppnLsLinkStationState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 12, 1, 2),
    _MscAppnLsLinkStationState_Type()
)
mscAppnLsLinkStationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsLinkStationState.setStatus("mandatory")


class _MscAppnLsLinkStationSubState_Type(Integer32):
    """Custom type mscAppnLsLinkStationSubState based on Integer32"""
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
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("active", 6),
          ("inactive", 1),
          ("pendDeact", 15),
          ("pendRcvConnInd", 12),
          ("pendSendConnRsp", 13),
          ("pendXidExch", 3),
          ("sentActAs", 4),
          ("sentConnReq", 11),
          ("sentConnRsp", 14),
          ("sentCreateTg", 10),
          ("sentDeactAsOrd", 7),
          ("sentDestroyTg", 9),
          ("sentDiscOrd", 8),
          ("sentReqOpnstn", 2),
          ("sentSentMode", 5))
    )


_MscAppnLsLinkStationSubState_Type.__name__ = "Integer32"
_MscAppnLsLinkStationSubState_Object = MibTableColumn
mscAppnLsLinkStationSubState = _MscAppnLsLinkStationSubState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 12, 1, 3),
    _MscAppnLsLinkStationSubState_Type()
)
mscAppnLsLinkStationSubState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsLinkStationSubState.setStatus("mandatory")


class _MscAppnLsActSessCount_Type(Gauge32):
    """Custom type mscAppnLsActSessCount based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnLsActSessCount_Type.__name__ = "Gauge32"
_MscAppnLsActSessCount_Object = MibTableColumn
mscAppnLsActSessCount = _MscAppnLsActSessCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 12, 1, 4),
    _MscAppnLsActSessCount_Type()
)
mscAppnLsActSessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsActSessCount.setStatus("mandatory")


class _MscAppnLsActualCpName_Type(AsciiString):
    """Custom type mscAppnLsActualCpName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_MscAppnLsActualCpName_Type.__name__ = "AsciiString"
_MscAppnLsActualCpName_Object = MibTableColumn
mscAppnLsActualCpName = _MscAppnLsActualCpName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 12, 1, 5),
    _MscAppnLsActualCpName_Type()
)
mscAppnLsActualCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsActualCpName.setStatus("mandatory")


class _MscAppnLsActualCpType_Type(Integer32):
    """Custom type mscAppnLsActualCpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("endNode", 2),
          ("lowEntryNode", 4),
          ("networkNode", 1),
          ("toBeDetermined", 0))
    )


_MscAppnLsActualCpType_Type.__name__ = "Integer32"
_MscAppnLsActualCpType_Object = MibTableColumn
mscAppnLsActualCpType = _MscAppnLsActualCpType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 12, 1, 6),
    _MscAppnLsActualCpType_Type()
)
mscAppnLsActualCpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsActualCpType.setStatus("mandatory")


class _MscAppnLsDlcName_Type(AsciiString):
    """Custom type mscAppnLsDlcName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MscAppnLsDlcName_Type.__name__ = "AsciiString"
_MscAppnLsDlcName_Object = MibTableColumn
mscAppnLsDlcName = _MscAppnLsDlcName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 12, 1, 7),
    _MscAppnLsDlcName_Type()
)
mscAppnLsDlcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsDlcName.setStatus("mandatory")


class _MscAppnLsDynamicOrDefined_Type(Integer32):
    """Custom type mscAppnLsDynamicOrDefined based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("defined", 2),
          ("dynamic", 1))
    )


_MscAppnLsDynamicOrDefined_Type.__name__ = "Integer32"
_MscAppnLsDynamicOrDefined_Object = MibTableColumn
mscAppnLsDynamicOrDefined = _MscAppnLsDynamicOrDefined_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 12, 1, 8),
    _MscAppnLsDynamicOrDefined_Type()
)
mscAppnLsDynamicOrDefined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsDynamicOrDefined.setStatus("mandatory")


class _MscAppnLsMigration_Type(Integer32):
    """Custom type mscAppnLsMigration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unknown", 3),
          ("yes", 1))
    )


_MscAppnLsMigration_Type.__name__ = "Integer32"
_MscAppnLsMigration_Object = MibTableColumn
mscAppnLsMigration = _MscAppnLsMigration_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 12, 1, 9),
    _MscAppnLsMigration_Type()
)
mscAppnLsMigration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsMigration.setStatus("mandatory")


class _MscAppnLsTgNum_Type(Unsigned32):
    """Custom type mscAppnLsTgNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnLsTgNum_Type.__name__ = "Unsigned32"
_MscAppnLsTgNum_Object = MibTableColumn
mscAppnLsTgNum = _MscAppnLsTgNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 12, 1, 10),
    _MscAppnLsTgNum_Type()
)
mscAppnLsTgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsTgNum.setStatus("mandatory")


class _MscAppnLsHprSupport_Type(Integer32):
    """Custom type mscAppnLsHprSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("anr", 1),
          ("none", 0),
          ("rtp", 2))
    )


_MscAppnLsHprSupport_Type.__name__ = "Integer32"
_MscAppnLsHprSupport_Object = MibTableColumn
mscAppnLsHprSupport = _MscAppnLsHprSupport_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 12, 1, 11),
    _MscAppnLsHprSupport_Type()
)
mscAppnLsHprSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsHprSupport.setStatus("mandatory")


class _MscAppnLsAnrLabel_Type(Hex):
    """Custom type mscAppnLsAnrLabel based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnLsAnrLabel_Type.__name__ = "Hex"
_MscAppnLsAnrLabel_Object = MibTableColumn
mscAppnLsAnrLabel = _MscAppnLsAnrLabel_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 12, 1, 12),
    _MscAppnLsAnrLabel_Type()
)
mscAppnLsAnrLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsAnrLabel.setStatus("mandatory")
_MscAppnLsTgCharTable_Object = MibTable
mscAppnLsTgCharTable = _MscAppnLsTgCharTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 13)
)
if mibBuilder.loadTexts:
    mscAppnLsTgCharTable.setStatus("mandatory")
_MscAppnLsTgCharEntry_Object = MibTableRow
mscAppnLsTgCharEntry = _MscAppnLsTgCharEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 13, 1)
)
mscAppnLsTgCharEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnLsIndex"),
)
if mibBuilder.loadTexts:
    mscAppnLsTgCharEntry.setStatus("mandatory")


class _MscAppnLsEffectiveCap_Type(Integer32):
    """Custom type mscAppnLsEffectiveCap based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("min", 0),
          ("n1000kbps", 101),
          ("n10100Mbps", 208),
          ("n101Gbps", 234),
          ("n1020Mbps", 181),
          ("n1050bps", 22),
          ("n106kbps", 75),
          ("n10800bps", 49),
          ("n1080kbps", 102),
          ("n108Mbps", 155),
          ("n1100Mbps", 182),
          ("n11100kbps", 129),
          ("n111Gbps", 235),
          ("n11300Mbps", 209),
          ("n1130bps", 23),
          ("n1150kbps", 103),
          ("n115kbps", 76),
          ("n1180Mbps", 183),
          ("n118Mbps", 156),
          ("n12000bps", 50),
          ("n1200bps", 24),
          ("n121Gbps", 236),
          ("n12300kbps", 130),
          ("n1230kbps", 104),
          ("n125kbps", 77),
          ("n12600Mbps", 210),
          ("n1260Mbps", 184),
          ("n128Mbps", 157),
          ("n131Gbps", 237),
          ("n13200bps", 51),
          ("n134kbps", 78),
          ("n13500kbps", 131),
          ("n1350bps", 25),
          ("n13800Mbps", 211),
          ("n1380kbps", 105),
          ("n138Mbps", 158),
          ("n141Gbps", 238),
          ("n1420Mbps", 185),
          ("n14400bps", 52),
          ("n144kbps", 79),
          ("n14700kbps", 132),
          ("n147Mbps", 159),
          ("n1500bps", 26),
          ("n15100Mbps", 212),
          ("n151Gbps", 239),
          ("n1540kbps", 106),
          ("n154kbps", 80),
          ("n15600bps", 53),
          ("n1570Mbps", 186),
          ("n157Mbps", 160),
          ("n160Gbps", 240),
          ("n16Gbps", 213),
          ("n16Mbps", 133),
          ("n1700Mbps", 187),
          ("n1700bps", 27),
          ("n1700kbps", 107),
          ("n170bps", 1),
          ("n170kbps", 81),
          ("n17Mbps", 134),
          ("n17kbps", 54),
          ("n1800bps", 28),
          ("n1800kbps", 108),
          ("n180Gbps", 241),
          ("n180Mbps", 161),
          ("n18Gbps", 214),
          ("n18Mbps", 135),
          ("n18kbps", 55),
          ("n1900Mbps", 188),
          ("n190bps", 2),
          ("n190kbps", 82),
          ("n19Gbps", 215),
          ("n19kbps", 56),
          ("n2000Mbps", 189),
          ("n2000bps", 29),
          ("n2000kbps", 109),
          ("n200Gbps", 242),
          ("n200Mbps", 162),
          ("n20Gbps", 216),
          ("n20Mbps", 136),
          ("n2100bps", 30),
          ("n210bps", 3),
          ("n210kbps", 83),
          ("n2200Mbps", 190),
          ("n2200kbps", 110),
          ("n220Gbps", 243),
          ("n220Mbps", 163),
          ("n22Mbps", 137),
          ("n22kbps", 57),
          ("n2300bps", 31),
          ("n2300kbps", 111),
          ("n230bps", 4),
          ("n230kbps", 84),
          ("n23Gbps", 217),
          ("n2400Mbps", 191),
          ("n2400bps", 32),
          ("n240Gbps", 244),
          ("n240Mbps", 164),
          ("n240bps", 5),
          ("n24kbps", 58),
          ("n2500Mbps", 192),
          ("n2500kbps", 112),
          ("n250kbps", 85),
          ("n25Gbps", 218),
          ("n25Mbps", 138),
          ("n260Gbps", 245),
          ("n260Mbps", 165),
          ("n260bps", 6),
          ("n26kbps", 59),
          ("n2700bps", 33),
          ("n270kbps", 86),
          ("n27Mbps", 139),
          ("n2800Mbps", 193),
          ("n2800kbps", 113),
          ("n280Gbps", 246),
          ("n280Mbps", 166),
          ("n280bps", 7),
          ("n28Gbps", 219),
          ("n290Mbps", 167),
          ("n290kbps", 87),
          ("n29Mbps", 140),
          ("n29kbps", 60),
          ("n3000bps", 34),
          ("n300Gbps", 247),
          ("n300bps", 8),
          ("n30Gbps", 220),
          ("n3100Mbps", 194),
          ("n3100kbps", 114),
          ("n310Mbps", 168),
          ("n310kbps", 88),
          ("n31kbps", 61),
          ("n320Gbps", 248),
          ("n32Mbps", 141),
          ("n3300bps", 35),
          ("n33Gbps", 221),
          ("n3400kbps", 115),
          ("n340bps", 9),
          ("n34Mbps", 142),
          ("n34kbps", 62),
          ("n3500Mbps", 195),
          ("n350Mbps", 169),
          ("n350kbps", 89),
          ("n35Gbps", 222),
          ("n3600bps", 36),
          ("n360Gbps", 249),
          ("n36kbps", 63),
          ("n3700kbps", 116),
          ("n37Mbps", 143),
          ("n3800Mbps", 196),
          ("n380bps", 10),
          ("n380kbps", 90),
          ("n38Gbps", 223),
          ("n38kbps", 64),
          ("n3900bps", 37),
          ("n390Mbps", 170),
          ("n39Mbps", 144),
          ("n4000kbps", 117),
          ("n400Gbps", 250),
          ("n40Gbps", 224),
          ("n4100Mbps", 197),
          ("n410bps", 11),
          ("n4200bps", 38),
          ("n420kbps", 91),
          ("n4300kbps", 118),
          ("n430Mbps", 171),
          ("n43kbps", 65),
          ("n4400Mbps", 198),
          ("n440Gbps", 251),
          ("n44Mbps", 145),
          ("n4500bps", 39),
          ("n450bps", 12),
          ("n45Gbps", 225),
          ("n4600kbps", 119),
          ("n460kbps", 92),
          ("n4700Mbps", 199),
          ("n470Mbps", 172),
          ("n4800bps", 40),
          ("n480Gbps", 252),
          ("n48kbps", 66),
          ("n4900kbps", 120),
          ("n490bps", 13),
          ("n49Mbps", 146),
          ("n5000Mbps", 200),
          ("n500kbps", 93),
          ("n50Gbps", 226),
          ("n510Mbps", 173),
          ("n520Gbps", 253),
          ("n530bps", 14),
          ("n53kbps", 67),
          ("n5400bps", 41),
          ("n540kbps", 94),
          ("n54Mbps", 147),
          ("n5500kbps", 121),
          ("n550Mbps", 174),
          ("n55Gbps", 227),
          ("n560Gbps", 254),
          ("n560bps", 15),
          ("n5700Mbps", 201),
          ("n580kbps", 95),
          ("n58kbps", 68),
          ("n590Mbps", 175),
          ("n59Mbps", 148),
          ("n6000bps", 42),
          ("n600Gbps", 255),
          ("n600bps", 16),
          ("n60Gbps", 228),
          ("n6100kbps", 122),
          ("n610kbps", 96),
          ("n62kbps", 69),
          ("n6300Mbps", 202),
          ("n630Mbps", 176),
          ("n64Mbps", 149),
          ("n65Gbps", 229),
          ("n6600bps", 43),
          ("n67kbps", 70),
          ("n6800kbps", 123),
          ("n680bps", 17),
          ("n6900Mbps", 203),
          ("n690kbps", 97),
          ("n69Mbps", 150),
          ("n70Gbps", 230),
          ("n710Mbps", 177),
          ("n7200bps", 44),
          ("n72kbps", 71),
          ("n7400kbps", 124),
          ("n74Mbps", 151),
          ("n7500Mbps", 204),
          ("n750bps", 18),
          ("n75Gbps", 231),
          ("n770kbps", 98),
          ("n77kbps", 72),
          ("n7800bps", 45),
          ("n790Mbps", 178),
          ("n79Mbps", 152),
          ("n8000kbps", 125),
          ("n81Gbps", 232),
          ("n8200Mbps", 205),
          ("n830bps", 19),
          ("n8400bps", 46),
          ("n840kbps", 99),
          ("n8600kbps", 126),
          ("n86kbps", 73),
          ("n870Mbps", 179),
          ("n8800Mbps", 206),
          ("n88Mbps", 153),
          ("n9000bps", 47),
          ("n900bps", 20),
          ("n91Gbps", 233),
          ("n9200kbps", 127),
          ("n920kbps", 100),
          ("n9400Mbps", 207),
          ("n940Mbps", 180),
          ("n9600bps", 48),
          ("n96kbps", 74),
          ("n9800kbps", 128),
          ("n980bps", 21),
          ("n98Mbps", 154))
    )


_MscAppnLsEffectiveCap_Type.__name__ = "Integer32"
_MscAppnLsEffectiveCap_Object = MibTableColumn
mscAppnLsEffectiveCap = _MscAppnLsEffectiveCap_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 13, 1, 1),
    _MscAppnLsEffectiveCap_Type()
)
mscAppnLsEffectiveCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsEffectiveCap.setStatus("mandatory")


class _MscAppnLsConnectCost_Type(Integer32):
    """Custom type mscAppnLsConnectCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnLsConnectCost_Type.__name__ = "Integer32"
_MscAppnLsConnectCost_Object = MibTableColumn
mscAppnLsConnectCost = _MscAppnLsConnectCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 13, 1, 2),
    _MscAppnLsConnectCost_Type()
)
mscAppnLsConnectCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsConnectCost.setStatus("mandatory")


class _MscAppnLsByteCost_Type(Integer32):
    """Custom type mscAppnLsByteCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnLsByteCost_Type.__name__ = "Integer32"
_MscAppnLsByteCost_Object = MibTableColumn
mscAppnLsByteCost = _MscAppnLsByteCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 13, 1, 3),
    _MscAppnLsByteCost_Type()
)
mscAppnLsByteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsByteCost.setStatus("mandatory")


class _MscAppnLsSecurity_Type(Integer32):
    """Custom type mscAppnLsSecurity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              32,
              64,
              96,
              128,
              160,
              192)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 160),
          ("guardedConduit", 128),
          ("guardedRadiation", 192),
          ("nonSecure", 1),
          ("publicSwitchedNetwork", 32),
          ("secureConduit", 96),
          ("unKnown", 0),
          ("undergroundCable", 64))
    )


_MscAppnLsSecurity_Type.__name__ = "Integer32"
_MscAppnLsSecurity_Object = MibTableColumn
mscAppnLsSecurity = _MscAppnLsSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 13, 1, 4),
    _MscAppnLsSecurity_Type()
)
mscAppnLsSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsSecurity.setStatus("mandatory")


class _MscAppnLsPropagationDelay_Type(Integer32):
    """Custom type mscAppnLsPropagationDelay based on Integer32"""
    defaultValue = 113

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              76,
              113,
              145,
              153)
        )
    )
    namedValues = NamedValues(
        *(("long", 153),
          ("minimum", 0),
          ("negligible", 76),
          ("packetSwitched", 145),
          ("terrestrial", 113))
    )


_MscAppnLsPropagationDelay_Type.__name__ = "Integer32"
_MscAppnLsPropagationDelay_Object = MibTableColumn
mscAppnLsPropagationDelay = _MscAppnLsPropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 13, 1, 5),
    _MscAppnLsPropagationDelay_Type()
)
mscAppnLsPropagationDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsPropagationDelay.setStatus("mandatory")


class _MscAppnLsUserDefinedParm1_Type(Unsigned32):
    """Custom type mscAppnLsUserDefinedParm1 based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnLsUserDefinedParm1_Type.__name__ = "Unsigned32"
_MscAppnLsUserDefinedParm1_Object = MibTableColumn
mscAppnLsUserDefinedParm1 = _MscAppnLsUserDefinedParm1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 13, 1, 7),
    _MscAppnLsUserDefinedParm1_Type()
)
mscAppnLsUserDefinedParm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsUserDefinedParm1.setStatus("mandatory")


class _MscAppnLsUserDefinedParm2_Type(Unsigned32):
    """Custom type mscAppnLsUserDefinedParm2 based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnLsUserDefinedParm2_Type.__name__ = "Unsigned32"
_MscAppnLsUserDefinedParm2_Object = MibTableColumn
mscAppnLsUserDefinedParm2 = _MscAppnLsUserDefinedParm2_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 13, 1, 8),
    _MscAppnLsUserDefinedParm2_Type()
)
mscAppnLsUserDefinedParm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsUserDefinedParm2.setStatus("mandatory")


class _MscAppnLsUserDefinedParm3_Type(Unsigned32):
    """Custom type mscAppnLsUserDefinedParm3 based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnLsUserDefinedParm3_Type.__name__ = "Unsigned32"
_MscAppnLsUserDefinedParm3_Object = MibTableColumn
mscAppnLsUserDefinedParm3 = _MscAppnLsUserDefinedParm3_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 13, 1, 9),
    _MscAppnLsUserDefinedParm3_Type()
)
mscAppnLsUserDefinedParm3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsUserDefinedParm3.setStatus("mandatory")
_MscAppnLsStatsTable_Object = MibTable
mscAppnLsStatsTable = _MscAppnLsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 14)
)
if mibBuilder.loadTexts:
    mscAppnLsStatsTable.setStatus("mandatory")
_MscAppnLsStatsEntry_Object = MibTableRow
mscAppnLsStatsEntry = _MscAppnLsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 14, 1)
)
mscAppnLsStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnLsIndex"),
)
if mibBuilder.loadTexts:
    mscAppnLsStatsEntry.setStatus("mandatory")
_MscAppnLsInXidBytes_Type = PassportCounter64
_MscAppnLsInXidBytes_Object = MibTableColumn
mscAppnLsInXidBytes = _MscAppnLsInXidBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 14, 1, 1),
    _MscAppnLsInXidBytes_Type()
)
mscAppnLsInXidBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsInXidBytes.setStatus("mandatory")
_MscAppnLsInMsgBytes_Type = PassportCounter64
_MscAppnLsInMsgBytes_Object = MibTableColumn
mscAppnLsInMsgBytes = _MscAppnLsInMsgBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 14, 1, 2),
    _MscAppnLsInMsgBytes_Type()
)
mscAppnLsInMsgBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsInMsgBytes.setStatus("mandatory")
_MscAppnLsInXidFrames_Type = PassportCounter64
_MscAppnLsInXidFrames_Object = MibTableColumn
mscAppnLsInXidFrames = _MscAppnLsInXidFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 14, 1, 3),
    _MscAppnLsInXidFrames_Type()
)
mscAppnLsInXidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsInXidFrames.setStatus("mandatory")
_MscAppnLsInMsgFrames_Type = PassportCounter64
_MscAppnLsInMsgFrames_Object = MibTableColumn
mscAppnLsInMsgFrames = _MscAppnLsInMsgFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 14, 1, 4),
    _MscAppnLsInMsgFrames_Type()
)
mscAppnLsInMsgFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsInMsgFrames.setStatus("mandatory")
_MscAppnLsOutXidBytes_Type = PassportCounter64
_MscAppnLsOutXidBytes_Object = MibTableColumn
mscAppnLsOutXidBytes = _MscAppnLsOutXidBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 14, 1, 5),
    _MscAppnLsOutXidBytes_Type()
)
mscAppnLsOutXidBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsOutXidBytes.setStatus("mandatory")
_MscAppnLsOutMsgBytes_Type = PassportCounter64
_MscAppnLsOutMsgBytes_Object = MibTableColumn
mscAppnLsOutMsgBytes = _MscAppnLsOutMsgBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 14, 1, 6),
    _MscAppnLsOutMsgBytes_Type()
)
mscAppnLsOutMsgBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsOutMsgBytes.setStatus("mandatory")
_MscAppnLsOutXidFrames_Type = PassportCounter64
_MscAppnLsOutXidFrames_Object = MibTableColumn
mscAppnLsOutXidFrames = _MscAppnLsOutXidFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 14, 1, 7),
    _MscAppnLsOutXidFrames_Type()
)
mscAppnLsOutXidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsOutXidFrames.setStatus("mandatory")
_MscAppnLsOutMsgFrames_Type = PassportCounter64
_MscAppnLsOutMsgFrames_Object = MibTableColumn
mscAppnLsOutMsgFrames = _MscAppnLsOutMsgFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 14, 1, 8),
    _MscAppnLsOutMsgFrames_Type()
)
mscAppnLsOutMsgFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsOutMsgFrames.setStatus("mandatory")
_MscAppnLsInInvalidSnaFrames_Type = PassportCounter64
_MscAppnLsInInvalidSnaFrames_Object = MibTableColumn
mscAppnLsInInvalidSnaFrames = _MscAppnLsInInvalidSnaFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 14, 1, 9),
    _MscAppnLsInInvalidSnaFrames_Type()
)
mscAppnLsInInvalidSnaFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsInInvalidSnaFrames.setStatus("mandatory")
_MscAppnLsInSessionControlFrames_Type = PassportCounter64
_MscAppnLsInSessionControlFrames_Object = MibTableColumn
mscAppnLsInSessionControlFrames = _MscAppnLsInSessionControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 14, 1, 10),
    _MscAppnLsInSessionControlFrames_Type()
)
mscAppnLsInSessionControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsInSessionControlFrames.setStatus("mandatory")
_MscAppnLsOutSessionControlFrames_Type = PassportCounter64
_MscAppnLsOutSessionControlFrames_Object = MibTableColumn
mscAppnLsOutSessionControlFrames = _MscAppnLsOutSessionControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 14, 1, 11),
    _MscAppnLsOutSessionControlFrames_Type()
)
mscAppnLsOutSessionControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsOutSessionControlFrames.setStatus("mandatory")
_MscAppnLsEchoResponse_Type = PassportCounter64
_MscAppnLsEchoResponse_Object = MibTableColumn
mscAppnLsEchoResponse = _MscAppnLsEchoResponse_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 14, 1, 12),
    _MscAppnLsEchoResponse_Type()
)
mscAppnLsEchoResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsEchoResponse.setStatus("mandatory")
_MscAppnLsCurrentDelay_Type = PassportCounter64
_MscAppnLsCurrentDelay_Object = MibTableColumn
mscAppnLsCurrentDelay = _MscAppnLsCurrentDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 14, 1, 13),
    _MscAppnLsCurrentDelay_Type()
)
mscAppnLsCurrentDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsCurrentDelay.setStatus("mandatory")
_MscAppnLsMaxDelay_Type = PassportCounter64
_MscAppnLsMaxDelay_Object = MibTableColumn
mscAppnLsMaxDelay = _MscAppnLsMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 14, 1, 14),
    _MscAppnLsMaxDelay_Type()
)
mscAppnLsMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsMaxDelay.setStatus("mandatory")
_MscAppnLsMinDelay_Type = PassportCounter64
_MscAppnLsMinDelay_Object = MibTableColumn
mscAppnLsMinDelay = _MscAppnLsMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 14, 1, 15),
    _MscAppnLsMinDelay_Type()
)
mscAppnLsMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsMinDelay.setStatus("mandatory")
_MscAppnLsGoodXids_Type = PassportCounter64
_MscAppnLsGoodXids_Object = MibTableColumn
mscAppnLsGoodXids = _MscAppnLsGoodXids_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 14, 1, 17),
    _MscAppnLsGoodXids_Type()
)
mscAppnLsGoodXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsGoodXids.setStatus("mandatory")
_MscAppnLsBadXids_Type = PassportCounter64
_MscAppnLsBadXids_Object = MibTableColumn
mscAppnLsBadXids = _MscAppnLsBadXids_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 6, 14, 1, 18),
    _MscAppnLsBadXids_Type()
)
mscAppnLsBadXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLsBadXids.setStatus("mandatory")
_MscAppnDirEnt_ObjectIdentity = ObjectIdentity
mscAppnDirEnt = _MscAppnDirEnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 7)
)
_MscAppnDirEntRowStatusTable_Object = MibTable
mscAppnDirEntRowStatusTable = _MscAppnDirEntRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 7, 1)
)
if mibBuilder.loadTexts:
    mscAppnDirEntRowStatusTable.setStatus("mandatory")
_MscAppnDirEntRowStatusEntry_Object = MibTableRow
mscAppnDirEntRowStatusEntry = _MscAppnDirEntRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 7, 1, 1)
)
mscAppnDirEntRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDirEntIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDirEntRowStatusEntry.setStatus("mandatory")
_MscAppnDirEntRowStatus_Type = RowStatus
_MscAppnDirEntRowStatus_Object = MibTableColumn
mscAppnDirEntRowStatus = _MscAppnDirEntRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 7, 1, 1, 1),
    _MscAppnDirEntRowStatus_Type()
)
mscAppnDirEntRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDirEntRowStatus.setStatus("mandatory")
_MscAppnDirEntComponentName_Type = DisplayString
_MscAppnDirEntComponentName_Object = MibTableColumn
mscAppnDirEntComponentName = _MscAppnDirEntComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 7, 1, 1, 2),
    _MscAppnDirEntComponentName_Type()
)
mscAppnDirEntComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDirEntComponentName.setStatus("mandatory")
_MscAppnDirEntStorageType_Type = StorageType
_MscAppnDirEntStorageType_Object = MibTableColumn
mscAppnDirEntStorageType = _MscAppnDirEntStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 7, 1, 1, 4),
    _MscAppnDirEntStorageType_Type()
)
mscAppnDirEntStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDirEntStorageType.setStatus("mandatory")


class _MscAppnDirEntIndex_Type(AsciiStringIndex):
    """Custom type mscAppnDirEntIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_MscAppnDirEntIndex_Type.__name__ = "AsciiStringIndex"
_MscAppnDirEntIndex_Object = MibTableColumn
mscAppnDirEntIndex = _MscAppnDirEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 7, 1, 1, 10),
    _MscAppnDirEntIndex_Type()
)
mscAppnDirEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnDirEntIndex.setStatus("mandatory")
_MscAppnDirEntOperTable_Object = MibTable
mscAppnDirEntOperTable = _MscAppnDirEntOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 7, 10)
)
if mibBuilder.loadTexts:
    mscAppnDirEntOperTable.setStatus("mandatory")
_MscAppnDirEntOperEntry_Object = MibTableRow
mscAppnDirEntOperEntry = _MscAppnDirEntOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 7, 10, 1)
)
mscAppnDirEntOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDirEntIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDirEntOperEntry.setStatus("mandatory")


class _MscAppnDirEntServerName_Type(AsciiString):
    """Custom type mscAppnDirEntServerName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_MscAppnDirEntServerName_Type.__name__ = "AsciiString"
_MscAppnDirEntServerName_Object = MibTableColumn
mscAppnDirEntServerName = _MscAppnDirEntServerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 7, 10, 1, 1),
    _MscAppnDirEntServerName_Type()
)
mscAppnDirEntServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDirEntServerName.setStatus("mandatory")


class _MscAppnDirEntLuOwnerName_Type(AsciiString):
    """Custom type mscAppnDirEntLuOwnerName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_MscAppnDirEntLuOwnerName_Type.__name__ = "AsciiString"
_MscAppnDirEntLuOwnerName_Object = MibTableColumn
mscAppnDirEntLuOwnerName = _MscAppnDirEntLuOwnerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 7, 10, 1, 2),
    _MscAppnDirEntLuOwnerName_Type()
)
mscAppnDirEntLuOwnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDirEntLuOwnerName.setStatus("mandatory")


class _MscAppnDirEntLocation_Type(Integer32):
    """Custom type mscAppnDirEntLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("domain", 1),
          ("local", 0),
          ("xdomain", 2))
    )


_MscAppnDirEntLocation_Type.__name__ = "Integer32"
_MscAppnDirEntLocation_Object = MibTableColumn
mscAppnDirEntLocation = _MscAppnDirEntLocation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 7, 10, 1, 3),
    _MscAppnDirEntLocation_Type()
)
mscAppnDirEntLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDirEntLocation.setStatus("mandatory")


class _MscAppnDirEntEntryType_Type(Integer32):
    """Custom type mscAppnDirEntEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cache", 0),
          ("home", 3),
          ("register", 2))
    )


_MscAppnDirEntEntryType_Type.__name__ = "Integer32"
_MscAppnDirEntEntryType_Object = MibTableColumn
mscAppnDirEntEntryType = _MscAppnDirEntEntryType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 7, 10, 1, 4),
    _MscAppnDirEntEntryType_Type()
)
mscAppnDirEntEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDirEntEntryType.setStatus("mandatory")


class _MscAppnDirEntWildCard_Type(Integer32):
    """Custom type mscAppnDirEntWildCard based on Integer32"""
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
        *(("explicit", 2),
          ("fullWildcard", 4),
          ("other", 1),
          ("partialWildcard", 3))
    )


_MscAppnDirEntWildCard_Type.__name__ = "Integer32"
_MscAppnDirEntWildCard_Object = MibTableColumn
mscAppnDirEntWildCard = _MscAppnDirEntWildCard_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 7, 10, 1, 5),
    _MscAppnDirEntWildCard_Type()
)
mscAppnDirEntWildCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDirEntWildCard.setStatus("mandatory")
_MscAppnAdjNn_ObjectIdentity = ObjectIdentity
mscAppnAdjNn = _MscAppnAdjNn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 8)
)
_MscAppnAdjNnRowStatusTable_Object = MibTable
mscAppnAdjNnRowStatusTable = _MscAppnAdjNnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 8, 1)
)
if mibBuilder.loadTexts:
    mscAppnAdjNnRowStatusTable.setStatus("mandatory")
_MscAppnAdjNnRowStatusEntry_Object = MibTableRow
mscAppnAdjNnRowStatusEntry = _MscAppnAdjNnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 8, 1, 1)
)
mscAppnAdjNnRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnAdjNnIndex"),
)
if mibBuilder.loadTexts:
    mscAppnAdjNnRowStatusEntry.setStatus("mandatory")
_MscAppnAdjNnRowStatus_Type = RowStatus
_MscAppnAdjNnRowStatus_Object = MibTableColumn
mscAppnAdjNnRowStatus = _MscAppnAdjNnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 8, 1, 1, 1),
    _MscAppnAdjNnRowStatus_Type()
)
mscAppnAdjNnRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnAdjNnRowStatus.setStatus("mandatory")
_MscAppnAdjNnComponentName_Type = DisplayString
_MscAppnAdjNnComponentName_Object = MibTableColumn
mscAppnAdjNnComponentName = _MscAppnAdjNnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 8, 1, 1, 2),
    _MscAppnAdjNnComponentName_Type()
)
mscAppnAdjNnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnAdjNnComponentName.setStatus("mandatory")
_MscAppnAdjNnStorageType_Type = StorageType
_MscAppnAdjNnStorageType_Object = MibTableColumn
mscAppnAdjNnStorageType = _MscAppnAdjNnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 8, 1, 1, 4),
    _MscAppnAdjNnStorageType_Type()
)
mscAppnAdjNnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnAdjNnStorageType.setStatus("mandatory")


class _MscAppnAdjNnIndex_Type(AsciiStringIndex):
    """Custom type mscAppnAdjNnIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_MscAppnAdjNnIndex_Type.__name__ = "AsciiStringIndex"
_MscAppnAdjNnIndex_Object = MibTableColumn
mscAppnAdjNnIndex = _MscAppnAdjNnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 8, 1, 1, 10),
    _MscAppnAdjNnIndex_Type()
)
mscAppnAdjNnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnAdjNnIndex.setStatus("mandatory")
_MscAppnAdjNnOperTable_Object = MibTable
mscAppnAdjNnOperTable = _MscAppnAdjNnOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 8, 10)
)
if mibBuilder.loadTexts:
    mscAppnAdjNnOperTable.setStatus("mandatory")
_MscAppnAdjNnOperEntry_Object = MibTableRow
mscAppnAdjNnOperEntry = _MscAppnAdjNnOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 8, 10, 1)
)
mscAppnAdjNnOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnAdjNnIndex"),
)
if mibBuilder.loadTexts:
    mscAppnAdjNnOperEntry.setStatus("mandatory")


class _MscAppnAdjNnCpCpSessStatus_Type(Integer32):
    """Custom type mscAppnAdjNnCpCpSessStatus based on Integer32"""
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
        *(("active", 1),
          ("conLoserActive", 2),
          ("conWinnerActive", 3),
          ("inactive", 4))
    )


_MscAppnAdjNnCpCpSessStatus_Type.__name__ = "Integer32"
_MscAppnAdjNnCpCpSessStatus_Object = MibTableColumn
mscAppnAdjNnCpCpSessStatus = _MscAppnAdjNnCpCpSessStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 8, 10, 1, 1),
    _MscAppnAdjNnCpCpSessStatus_Type()
)
mscAppnAdjNnCpCpSessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnAdjNnCpCpSessStatus.setStatus("mandatory")
_MscAppnAdjNnOutOfSeqTdus_Type = PassportCounter64
_MscAppnAdjNnOutOfSeqTdus_Object = MibTableColumn
mscAppnAdjNnOutOfSeqTdus = _MscAppnAdjNnOutOfSeqTdus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 8, 10, 1, 2),
    _MscAppnAdjNnOutOfSeqTdus_Type()
)
mscAppnAdjNnOutOfSeqTdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnAdjNnOutOfSeqTdus.setStatus("mandatory")


class _MscAppnAdjNnLastFrsnSent_Type(Unsigned32):
    """Custom type mscAppnAdjNnLastFrsnSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAppnAdjNnLastFrsnSent_Type.__name__ = "Unsigned32"
_MscAppnAdjNnLastFrsnSent_Object = MibTableColumn
mscAppnAdjNnLastFrsnSent = _MscAppnAdjNnLastFrsnSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 8, 10, 1, 3),
    _MscAppnAdjNnLastFrsnSent_Type()
)
mscAppnAdjNnLastFrsnSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnAdjNnLastFrsnSent.setStatus("mandatory")


class _MscAppnAdjNnLastFrsnReceived_Type(Unsigned32):
    """Custom type mscAppnAdjNnLastFrsnReceived based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAppnAdjNnLastFrsnReceived_Type.__name__ = "Unsigned32"
_MscAppnAdjNnLastFrsnReceived_Object = MibTableColumn
mscAppnAdjNnLastFrsnReceived = _MscAppnAdjNnLastFrsnReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 8, 10, 1, 4),
    _MscAppnAdjNnLastFrsnReceived_Type()
)
mscAppnAdjNnLastFrsnReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnAdjNnLastFrsnReceived.setStatus("mandatory")
_MscAppnNn_ObjectIdentity = ObjectIdentity
mscAppnNn = _MscAppnNn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 9)
)
_MscAppnNnRowStatusTable_Object = MibTable
mscAppnNnRowStatusTable = _MscAppnNnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 9, 1)
)
if mibBuilder.loadTexts:
    mscAppnNnRowStatusTable.setStatus("mandatory")
_MscAppnNnRowStatusEntry_Object = MibTableRow
mscAppnNnRowStatusEntry = _MscAppnNnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 9, 1, 1)
)
mscAppnNnRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnNnIndex"),
)
if mibBuilder.loadTexts:
    mscAppnNnRowStatusEntry.setStatus("mandatory")
_MscAppnNnRowStatus_Type = RowStatus
_MscAppnNnRowStatus_Object = MibTableColumn
mscAppnNnRowStatus = _MscAppnNnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 9, 1, 1, 1),
    _MscAppnNnRowStatus_Type()
)
mscAppnNnRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnNnRowStatus.setStatus("mandatory")
_MscAppnNnComponentName_Type = DisplayString
_MscAppnNnComponentName_Object = MibTableColumn
mscAppnNnComponentName = _MscAppnNnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 9, 1, 1, 2),
    _MscAppnNnComponentName_Type()
)
mscAppnNnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnNnComponentName.setStatus("mandatory")
_MscAppnNnStorageType_Type = StorageType
_MscAppnNnStorageType_Object = MibTableColumn
mscAppnNnStorageType = _MscAppnNnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 9, 1, 1, 4),
    _MscAppnNnStorageType_Type()
)
mscAppnNnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnNnStorageType.setStatus("mandatory")


class _MscAppnNnIndex_Type(AsciiStringIndex):
    """Custom type mscAppnNnIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_MscAppnNnIndex_Type.__name__ = "AsciiStringIndex"
_MscAppnNnIndex_Object = MibTableColumn
mscAppnNnIndex = _MscAppnNnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 9, 1, 1, 10),
    _MscAppnNnIndex_Type()
)
mscAppnNnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnNnIndex.setStatus("mandatory")
_MscAppnNnOperTable_Object = MibTable
mscAppnNnOperTable = _MscAppnNnOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 9, 10)
)
if mibBuilder.loadTexts:
    mscAppnNnOperTable.setStatus("mandatory")
_MscAppnNnOperEntry_Object = MibTableRow
mscAppnNnOperEntry = _MscAppnNnOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 9, 10, 1)
)
mscAppnNnOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnNnIndex"),
)
if mibBuilder.loadTexts:
    mscAppnNnOperEntry.setStatus("mandatory")


class _MscAppnNnDaysLeft_Type(Unsigned32):
    """Custom type mscAppnNnDaysLeft based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MscAppnNnDaysLeft_Type.__name__ = "Unsigned32"
_MscAppnNnDaysLeft_Object = MibTableColumn
mscAppnNnDaysLeft = _MscAppnNnDaysLeft_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 9, 10, 1, 2),
    _MscAppnNnDaysLeft_Type()
)
mscAppnNnDaysLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnNnDaysLeft.setStatus("mandatory")


class _MscAppnNnNodeType_Type(Integer32):
    """Custom type mscAppnNnNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("networkNode", 1),
          ("toBeDetermined", 0),
          ("virtualRoutingNode", 3))
    )


_MscAppnNnNodeType_Type.__name__ = "Integer32"
_MscAppnNnNodeType_Object = MibTableColumn
mscAppnNnNodeType = _MscAppnNnNodeType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 9, 10, 1, 3),
    _MscAppnNnNodeType_Type()
)
mscAppnNnNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnNnNodeType.setStatus("mandatory")


class _MscAppnNnResourceSequenceNumber_Type(Unsigned32):
    """Custom type mscAppnNnResourceSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAppnNnResourceSequenceNumber_Type.__name__ = "Unsigned32"
_MscAppnNnResourceSequenceNumber_Object = MibTableColumn
mscAppnNnResourceSequenceNumber = _MscAppnNnResourceSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 9, 10, 1, 4),
    _MscAppnNnResourceSequenceNumber_Type()
)
mscAppnNnResourceSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnNnResourceSequenceNumber.setStatus("mandatory")


class _MscAppnNnRouteAdditionResistance_Type(Integer32):
    """Custom type mscAppnNnRouteAdditionResistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnNnRouteAdditionResistance_Type.__name__ = "Integer32"
_MscAppnNnRouteAdditionResistance_Object = MibTableColumn
mscAppnNnRouteAdditionResistance = _MscAppnNnRouteAdditionResistance_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 9, 10, 1, 5),
    _MscAppnNnRouteAdditionResistance_Type()
)
mscAppnNnRouteAdditionResistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnNnRouteAdditionResistance.setStatus("mandatory")


class _MscAppnNnStatus_Type(OctetString):
    """Custom type mscAppnNnStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAppnNnStatus_Type.__name__ = "OctetString"
_MscAppnNnStatus_Object = MibTableColumn
mscAppnNnStatus = _MscAppnNnStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 9, 10, 1, 6),
    _MscAppnNnStatus_Type()
)
mscAppnNnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnNnStatus.setStatus("mandatory")


class _MscAppnNnFunctionSupported_Type(OctetString):
    """Custom type mscAppnNnFunctionSupported based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAppnNnFunctionSupported_Type.__name__ = "OctetString"
_MscAppnNnFunctionSupported_Object = MibTableColumn
mscAppnNnFunctionSupported = _MscAppnNnFunctionSupported_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 9, 10, 1, 7),
    _MscAppnNnFunctionSupported_Type()
)
mscAppnNnFunctionSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnNnFunctionSupported.setStatus("mandatory")
_MscAppnLocTg_ObjectIdentity = ObjectIdentity
mscAppnLocTg = _MscAppnLocTg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 10)
)
_MscAppnLocTgRowStatusTable_Object = MibTable
mscAppnLocTgRowStatusTable = _MscAppnLocTgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 10, 1)
)
if mibBuilder.loadTexts:
    mscAppnLocTgRowStatusTable.setStatus("mandatory")
_MscAppnLocTgRowStatusEntry_Object = MibTableRow
mscAppnLocTgRowStatusEntry = _MscAppnLocTgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 10, 1, 1)
)
mscAppnLocTgRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnLocTgDestFqcpNameIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnLocTgTransmissionGroupIndex"),
)
if mibBuilder.loadTexts:
    mscAppnLocTgRowStatusEntry.setStatus("mandatory")
_MscAppnLocTgRowStatus_Type = RowStatus
_MscAppnLocTgRowStatus_Object = MibTableColumn
mscAppnLocTgRowStatus = _MscAppnLocTgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 10, 1, 1, 1),
    _MscAppnLocTgRowStatus_Type()
)
mscAppnLocTgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLocTgRowStatus.setStatus("mandatory")
_MscAppnLocTgComponentName_Type = DisplayString
_MscAppnLocTgComponentName_Object = MibTableColumn
mscAppnLocTgComponentName = _MscAppnLocTgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 10, 1, 1, 2),
    _MscAppnLocTgComponentName_Type()
)
mscAppnLocTgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLocTgComponentName.setStatus("mandatory")
_MscAppnLocTgStorageType_Type = StorageType
_MscAppnLocTgStorageType_Object = MibTableColumn
mscAppnLocTgStorageType = _MscAppnLocTgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 10, 1, 1, 4),
    _MscAppnLocTgStorageType_Type()
)
mscAppnLocTgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLocTgStorageType.setStatus("mandatory")


class _MscAppnLocTgDestFqcpNameIndex_Type(AsciiStringIndex):
    """Custom type mscAppnLocTgDestFqcpNameIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_MscAppnLocTgDestFqcpNameIndex_Type.__name__ = "AsciiStringIndex"
_MscAppnLocTgDestFqcpNameIndex_Object = MibTableColumn
mscAppnLocTgDestFqcpNameIndex = _MscAppnLocTgDestFqcpNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 10, 1, 1, 10),
    _MscAppnLocTgDestFqcpNameIndex_Type()
)
mscAppnLocTgDestFqcpNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnLocTgDestFqcpNameIndex.setStatus("mandatory")


class _MscAppnLocTgTransmissionGroupIndex_Type(Integer32):
    """Custom type mscAppnLocTgTransmissionGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnLocTgTransmissionGroupIndex_Type.__name__ = "Integer32"
_MscAppnLocTgTransmissionGroupIndex_Object = MibTableColumn
mscAppnLocTgTransmissionGroupIndex = _MscAppnLocTgTransmissionGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 10, 1, 1, 11),
    _MscAppnLocTgTransmissionGroupIndex_Type()
)
mscAppnLocTgTransmissionGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnLocTgTransmissionGroupIndex.setStatus("mandatory")
_MscAppnLocTgOperTable_Object = MibTable
mscAppnLocTgOperTable = _MscAppnLocTgOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 10, 10)
)
if mibBuilder.loadTexts:
    mscAppnLocTgOperTable.setStatus("mandatory")
_MscAppnLocTgOperEntry_Object = MibTableRow
mscAppnLocTgOperEntry = _MscAppnLocTgOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 10, 10, 1)
)
mscAppnLocTgOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnLocTgDestFqcpNameIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnLocTgTransmissionGroupIndex"),
)
if mibBuilder.loadTexts:
    mscAppnLocTgOperEntry.setStatus("mandatory")


class _MscAppnLocTgStatus_Type(OctetString):
    """Custom type mscAppnLocTgStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAppnLocTgStatus_Type.__name__ = "OctetString"
_MscAppnLocTgStatus_Object = MibTableColumn
mscAppnLocTgStatus = _MscAppnLocTgStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 10, 10, 1, 1),
    _MscAppnLocTgStatus_Type()
)
mscAppnLocTgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLocTgStatus.setStatus("mandatory")


class _MscAppnLocTgResourceSequenceNumber_Type(Unsigned32):
    """Custom type mscAppnLocTgResourceSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAppnLocTgResourceSequenceNumber_Type.__name__ = "Unsigned32"
_MscAppnLocTgResourceSequenceNumber_Object = MibTableColumn
mscAppnLocTgResourceSequenceNumber = _MscAppnLocTgResourceSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 10, 10, 1, 2),
    _MscAppnLocTgResourceSequenceNumber_Type()
)
mscAppnLocTgResourceSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLocTgResourceSequenceNumber.setStatus("mandatory")
_MscAppnLocTgLinkAddressTable_Object = MibTable
mscAppnLocTgLinkAddressTable = _MscAppnLocTgLinkAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 10, 11)
)
if mibBuilder.loadTexts:
    mscAppnLocTgLinkAddressTable.setStatus("mandatory")
_MscAppnLocTgLinkAddressEntry_Object = MibTableRow
mscAppnLocTgLinkAddressEntry = _MscAppnLocTgLinkAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 10, 11, 1)
)
mscAppnLocTgLinkAddressEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnLocTgDestFqcpNameIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnLocTgTransmissionGroupIndex"),
)
if mibBuilder.loadTexts:
    mscAppnLocTgLinkAddressEntry.setStatus("mandatory")


class _MscAppnLocTgDlcData_Type(HexString):
    """Custom type mscAppnLocTgDlcData based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscAppnLocTgDlcData_Type.__name__ = "HexString"
_MscAppnLocTgDlcData_Object = MibTableColumn
mscAppnLocTgDlcData = _MscAppnLocTgDlcData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 10, 11, 1, 1),
    _MscAppnLocTgDlcData_Type()
)
mscAppnLocTgDlcData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLocTgDlcData.setStatus("mandatory")
_MscAppnLocTgTgCharTable_Object = MibTable
mscAppnLocTgTgCharTable = _MscAppnLocTgTgCharTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 10, 12)
)
if mibBuilder.loadTexts:
    mscAppnLocTgTgCharTable.setStatus("mandatory")
_MscAppnLocTgTgCharEntry_Object = MibTableRow
mscAppnLocTgTgCharEntry = _MscAppnLocTgTgCharEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 10, 12, 1)
)
mscAppnLocTgTgCharEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnLocTgDestFqcpNameIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnLocTgTransmissionGroupIndex"),
)
if mibBuilder.loadTexts:
    mscAppnLocTgTgCharEntry.setStatus("mandatory")


class _MscAppnLocTgEffectiveCap_Type(Integer32):
    """Custom type mscAppnLocTgEffectiveCap based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("min", 0),
          ("n1000kbps", 101),
          ("n10100Mbps", 208),
          ("n101Gbps", 234),
          ("n1020Mbps", 181),
          ("n1050bps", 22),
          ("n106kbps", 75),
          ("n10800bps", 49),
          ("n1080kbps", 102),
          ("n108Mbps", 155),
          ("n1100Mbps", 182),
          ("n11100kbps", 129),
          ("n111Gbps", 235),
          ("n11300Mbps", 209),
          ("n1130bps", 23),
          ("n1150kbps", 103),
          ("n115kbps", 76),
          ("n1180Mbps", 183),
          ("n118Mbps", 156),
          ("n12000bps", 50),
          ("n1200bps", 24),
          ("n121Gbps", 236),
          ("n12300kbps", 130),
          ("n1230kbps", 104),
          ("n125kbps", 77),
          ("n12600Mbps", 210),
          ("n1260Mbps", 184),
          ("n128Mbps", 157),
          ("n131Gbps", 237),
          ("n13200bps", 51),
          ("n134kbps", 78),
          ("n13500kbps", 131),
          ("n1350bps", 25),
          ("n13800Mbps", 211),
          ("n1380kbps", 105),
          ("n138Mbps", 158),
          ("n141Gbps", 238),
          ("n1420Mbps", 185),
          ("n14400bps", 52),
          ("n144kbps", 79),
          ("n14700kbps", 132),
          ("n147Mbps", 159),
          ("n1500bps", 26),
          ("n15100Mbps", 212),
          ("n151Gbps", 239),
          ("n1540kbps", 106),
          ("n154kbps", 80),
          ("n15600bps", 53),
          ("n1570Mbps", 186),
          ("n157Mbps", 160),
          ("n160Gbps", 240),
          ("n16Gbps", 213),
          ("n16Mbps", 133),
          ("n1700Mbps", 187),
          ("n1700bps", 27),
          ("n1700kbps", 107),
          ("n170bps", 1),
          ("n170kbps", 81),
          ("n17Mbps", 134),
          ("n17kbps", 54),
          ("n1800bps", 28),
          ("n1800kbps", 108),
          ("n180Gbps", 241),
          ("n180Mbps", 161),
          ("n18Gbps", 214),
          ("n18Mbps", 135),
          ("n18kbps", 55),
          ("n1900Mbps", 188),
          ("n190bps", 2),
          ("n190kbps", 82),
          ("n19Gbps", 215),
          ("n19kbps", 56),
          ("n2000Mbps", 189),
          ("n2000bps", 29),
          ("n2000kbps", 109),
          ("n200Gbps", 242),
          ("n200Mbps", 162),
          ("n20Gbps", 216),
          ("n20Mbps", 136),
          ("n2100bps", 30),
          ("n210bps", 3),
          ("n210kbps", 83),
          ("n2200Mbps", 190),
          ("n2200kbps", 110),
          ("n220Gbps", 243),
          ("n220Mbps", 163),
          ("n22Mbps", 137),
          ("n22kbps", 57),
          ("n2300bps", 31),
          ("n2300kbps", 111),
          ("n230bps", 4),
          ("n230kbps", 84),
          ("n23Gbps", 217),
          ("n2400Mbps", 191),
          ("n2400bps", 32),
          ("n240Gbps", 244),
          ("n240Mbps", 164),
          ("n240bps", 5),
          ("n24kbps", 58),
          ("n2500Mbps", 192),
          ("n2500kbps", 112),
          ("n250kbps", 85),
          ("n25Gbps", 218),
          ("n25Mbps", 138),
          ("n260Gbps", 245),
          ("n260Mbps", 165),
          ("n260bps", 6),
          ("n26kbps", 59),
          ("n2700bps", 33),
          ("n270kbps", 86),
          ("n27Mbps", 139),
          ("n2800Mbps", 193),
          ("n2800kbps", 113),
          ("n280Gbps", 246),
          ("n280Mbps", 166),
          ("n280bps", 7),
          ("n28Gbps", 219),
          ("n290Mbps", 167),
          ("n290kbps", 87),
          ("n29Mbps", 140),
          ("n29kbps", 60),
          ("n3000bps", 34),
          ("n300Gbps", 247),
          ("n300bps", 8),
          ("n30Gbps", 220),
          ("n3100Mbps", 194),
          ("n3100kbps", 114),
          ("n310Mbps", 168),
          ("n310kbps", 88),
          ("n31kbps", 61),
          ("n320Gbps", 248),
          ("n32Mbps", 141),
          ("n3300bps", 35),
          ("n33Gbps", 221),
          ("n3400kbps", 115),
          ("n340bps", 9),
          ("n34Mbps", 142),
          ("n34kbps", 62),
          ("n3500Mbps", 195),
          ("n350Mbps", 169),
          ("n350kbps", 89),
          ("n35Gbps", 222),
          ("n3600bps", 36),
          ("n360Gbps", 249),
          ("n36kbps", 63),
          ("n3700kbps", 116),
          ("n37Mbps", 143),
          ("n3800Mbps", 196),
          ("n380bps", 10),
          ("n380kbps", 90),
          ("n38Gbps", 223),
          ("n38kbps", 64),
          ("n3900bps", 37),
          ("n390Mbps", 170),
          ("n39Mbps", 144),
          ("n4000kbps", 117),
          ("n400Gbps", 250),
          ("n40Gbps", 224),
          ("n4100Mbps", 197),
          ("n410bps", 11),
          ("n4200bps", 38),
          ("n420kbps", 91),
          ("n4300kbps", 118),
          ("n430Mbps", 171),
          ("n43kbps", 65),
          ("n4400Mbps", 198),
          ("n440Gbps", 251),
          ("n44Mbps", 145),
          ("n4500bps", 39),
          ("n450bps", 12),
          ("n45Gbps", 225),
          ("n4600kbps", 119),
          ("n460kbps", 92),
          ("n4700Mbps", 199),
          ("n470Mbps", 172),
          ("n4800bps", 40),
          ("n480Gbps", 252),
          ("n48kbps", 66),
          ("n4900kbps", 120),
          ("n490bps", 13),
          ("n49Mbps", 146),
          ("n5000Mbps", 200),
          ("n500kbps", 93),
          ("n50Gbps", 226),
          ("n510Mbps", 173),
          ("n520Gbps", 253),
          ("n530bps", 14),
          ("n53kbps", 67),
          ("n5400bps", 41),
          ("n540kbps", 94),
          ("n54Mbps", 147),
          ("n5500kbps", 121),
          ("n550Mbps", 174),
          ("n55Gbps", 227),
          ("n560Gbps", 254),
          ("n560bps", 15),
          ("n5700Mbps", 201),
          ("n580kbps", 95),
          ("n58kbps", 68),
          ("n590Mbps", 175),
          ("n59Mbps", 148),
          ("n6000bps", 42),
          ("n600Gbps", 255),
          ("n600bps", 16),
          ("n60Gbps", 228),
          ("n6100kbps", 122),
          ("n610kbps", 96),
          ("n62kbps", 69),
          ("n6300Mbps", 202),
          ("n630Mbps", 176),
          ("n64Mbps", 149),
          ("n65Gbps", 229),
          ("n6600bps", 43),
          ("n67kbps", 70),
          ("n6800kbps", 123),
          ("n680bps", 17),
          ("n6900Mbps", 203),
          ("n690kbps", 97),
          ("n69Mbps", 150),
          ("n70Gbps", 230),
          ("n710Mbps", 177),
          ("n7200bps", 44),
          ("n72kbps", 71),
          ("n7400kbps", 124),
          ("n74Mbps", 151),
          ("n7500Mbps", 204),
          ("n750bps", 18),
          ("n75Gbps", 231),
          ("n770kbps", 98),
          ("n77kbps", 72),
          ("n7800bps", 45),
          ("n790Mbps", 178),
          ("n79Mbps", 152),
          ("n8000kbps", 125),
          ("n81Gbps", 232),
          ("n8200Mbps", 205),
          ("n830bps", 19),
          ("n8400bps", 46),
          ("n840kbps", 99),
          ("n8600kbps", 126),
          ("n86kbps", 73),
          ("n870Mbps", 179),
          ("n8800Mbps", 206),
          ("n88Mbps", 153),
          ("n9000bps", 47),
          ("n900bps", 20),
          ("n91Gbps", 233),
          ("n9200kbps", 127),
          ("n920kbps", 100),
          ("n9400Mbps", 207),
          ("n940Mbps", 180),
          ("n9600bps", 48),
          ("n96kbps", 74),
          ("n9800kbps", 128),
          ("n980bps", 21),
          ("n98Mbps", 154))
    )


_MscAppnLocTgEffectiveCap_Type.__name__ = "Integer32"
_MscAppnLocTgEffectiveCap_Object = MibTableColumn
mscAppnLocTgEffectiveCap = _MscAppnLocTgEffectiveCap_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 10, 12, 1, 1),
    _MscAppnLocTgEffectiveCap_Type()
)
mscAppnLocTgEffectiveCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLocTgEffectiveCap.setStatus("mandatory")


class _MscAppnLocTgConnectCost_Type(Integer32):
    """Custom type mscAppnLocTgConnectCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnLocTgConnectCost_Type.__name__ = "Integer32"
_MscAppnLocTgConnectCost_Object = MibTableColumn
mscAppnLocTgConnectCost = _MscAppnLocTgConnectCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 10, 12, 1, 2),
    _MscAppnLocTgConnectCost_Type()
)
mscAppnLocTgConnectCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLocTgConnectCost.setStatus("mandatory")


class _MscAppnLocTgByteCost_Type(Integer32):
    """Custom type mscAppnLocTgByteCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnLocTgByteCost_Type.__name__ = "Integer32"
_MscAppnLocTgByteCost_Object = MibTableColumn
mscAppnLocTgByteCost = _MscAppnLocTgByteCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 10, 12, 1, 3),
    _MscAppnLocTgByteCost_Type()
)
mscAppnLocTgByteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLocTgByteCost.setStatus("mandatory")


class _MscAppnLocTgSecurity_Type(Integer32):
    """Custom type mscAppnLocTgSecurity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              32,
              64,
              96,
              128,
              160,
              192)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 160),
          ("guardedConduit", 128),
          ("guardedRadiation", 192),
          ("nonSecure", 1),
          ("publicSwitchedNetwork", 32),
          ("secureConduit", 96),
          ("unKnown", 0),
          ("undergroundCable", 64))
    )


_MscAppnLocTgSecurity_Type.__name__ = "Integer32"
_MscAppnLocTgSecurity_Object = MibTableColumn
mscAppnLocTgSecurity = _MscAppnLocTgSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 10, 12, 1, 4),
    _MscAppnLocTgSecurity_Type()
)
mscAppnLocTgSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLocTgSecurity.setStatus("mandatory")


class _MscAppnLocTgPropagationDelay_Type(Integer32):
    """Custom type mscAppnLocTgPropagationDelay based on Integer32"""
    defaultValue = 113

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              76,
              113,
              145,
              153)
        )
    )
    namedValues = NamedValues(
        *(("long", 153),
          ("minimum", 0),
          ("negligible", 76),
          ("packetSwitched", 145),
          ("terrestrial", 113))
    )


_MscAppnLocTgPropagationDelay_Type.__name__ = "Integer32"
_MscAppnLocTgPropagationDelay_Object = MibTableColumn
mscAppnLocTgPropagationDelay = _MscAppnLocTgPropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 10, 12, 1, 5),
    _MscAppnLocTgPropagationDelay_Type()
)
mscAppnLocTgPropagationDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLocTgPropagationDelay.setStatus("mandatory")


class _MscAppnLocTgUserDefinedParm1_Type(Unsigned32):
    """Custom type mscAppnLocTgUserDefinedParm1 based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnLocTgUserDefinedParm1_Type.__name__ = "Unsigned32"
_MscAppnLocTgUserDefinedParm1_Object = MibTableColumn
mscAppnLocTgUserDefinedParm1 = _MscAppnLocTgUserDefinedParm1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 10, 12, 1, 7),
    _MscAppnLocTgUserDefinedParm1_Type()
)
mscAppnLocTgUserDefinedParm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLocTgUserDefinedParm1.setStatus("mandatory")


class _MscAppnLocTgUserDefinedParm2_Type(Unsigned32):
    """Custom type mscAppnLocTgUserDefinedParm2 based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnLocTgUserDefinedParm2_Type.__name__ = "Unsigned32"
_MscAppnLocTgUserDefinedParm2_Object = MibTableColumn
mscAppnLocTgUserDefinedParm2 = _MscAppnLocTgUserDefinedParm2_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 10, 12, 1, 8),
    _MscAppnLocTgUserDefinedParm2_Type()
)
mscAppnLocTgUserDefinedParm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLocTgUserDefinedParm2.setStatus("mandatory")


class _MscAppnLocTgUserDefinedParm3_Type(Unsigned32):
    """Custom type mscAppnLocTgUserDefinedParm3 based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnLocTgUserDefinedParm3_Type.__name__ = "Unsigned32"
_MscAppnLocTgUserDefinedParm3_Object = MibTableColumn
mscAppnLocTgUserDefinedParm3 = _MscAppnLocTgUserDefinedParm3_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 10, 12, 1, 9),
    _MscAppnLocTgUserDefinedParm3_Type()
)
mscAppnLocTgUserDefinedParm3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnLocTgUserDefinedParm3.setStatus("mandatory")
_MscAppnIsrSess_ObjectIdentity = ObjectIdentity
mscAppnIsrSess = _MscAppnIsrSess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11)
)
_MscAppnIsrSessRowStatusTable_Object = MibTable
mscAppnIsrSessRowStatusTable = _MscAppnIsrSessRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 1)
)
if mibBuilder.loadTexts:
    mscAppnIsrSessRowStatusTable.setStatus("mandatory")
_MscAppnIsrSessRowStatusEntry_Object = MibTableRow
mscAppnIsrSessRowStatusEntry = _MscAppnIsrSessRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 1, 1)
)
mscAppnIsrSessRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIsrSessFqcpNameIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIsrSessProcedureCorrelationIdIndex"),
)
if mibBuilder.loadTexts:
    mscAppnIsrSessRowStatusEntry.setStatus("mandatory")
_MscAppnIsrSessRowStatus_Type = RowStatus
_MscAppnIsrSessRowStatus_Object = MibTableColumn
mscAppnIsrSessRowStatus = _MscAppnIsrSessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 1, 1, 1),
    _MscAppnIsrSessRowStatus_Type()
)
mscAppnIsrSessRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessRowStatus.setStatus("mandatory")
_MscAppnIsrSessComponentName_Type = DisplayString
_MscAppnIsrSessComponentName_Object = MibTableColumn
mscAppnIsrSessComponentName = _MscAppnIsrSessComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 1, 1, 2),
    _MscAppnIsrSessComponentName_Type()
)
mscAppnIsrSessComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessComponentName.setStatus("mandatory")
_MscAppnIsrSessStorageType_Type = StorageType
_MscAppnIsrSessStorageType_Object = MibTableColumn
mscAppnIsrSessStorageType = _MscAppnIsrSessStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 1, 1, 4),
    _MscAppnIsrSessStorageType_Type()
)
mscAppnIsrSessStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessStorageType.setStatus("mandatory")


class _MscAppnIsrSessFqcpNameIndex_Type(AsciiStringIndex):
    """Custom type mscAppnIsrSessFqcpNameIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_MscAppnIsrSessFqcpNameIndex_Type.__name__ = "AsciiStringIndex"
_MscAppnIsrSessFqcpNameIndex_Object = MibTableColumn
mscAppnIsrSessFqcpNameIndex = _MscAppnIsrSessFqcpNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 1, 1, 10),
    _MscAppnIsrSessFqcpNameIndex_Type()
)
mscAppnIsrSessFqcpNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnIsrSessFqcpNameIndex.setStatus("mandatory")


class _MscAppnIsrSessProcedureCorrelationIdIndex_Type(HexString):
    """Custom type mscAppnIsrSessProcedureCorrelationIdIndex based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscAppnIsrSessProcedureCorrelationIdIndex_Type.__name__ = "HexString"
_MscAppnIsrSessProcedureCorrelationIdIndex_Object = MibTableColumn
mscAppnIsrSessProcedureCorrelationIdIndex = _MscAppnIsrSessProcedureCorrelationIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 1, 1, 11),
    _MscAppnIsrSessProcedureCorrelationIdIndex_Type()
)
mscAppnIsrSessProcedureCorrelationIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnIsrSessProcedureCorrelationIdIndex.setStatus("mandatory")
_MscAppnIsrSessOperTable_Object = MibTable
mscAppnIsrSessOperTable = _MscAppnIsrSessOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 10)
)
if mibBuilder.loadTexts:
    mscAppnIsrSessOperTable.setStatus("mandatory")
_MscAppnIsrSessOperEntry_Object = MibTableRow
mscAppnIsrSessOperEntry = _MscAppnIsrSessOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 10, 1)
)
mscAppnIsrSessOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIsrSessFqcpNameIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIsrSessProcedureCorrelationIdIndex"),
)
if mibBuilder.loadTexts:
    mscAppnIsrSessOperEntry.setStatus("mandatory")


class _MscAppnIsrSessTransmissionPriority_Type(Integer32):
    """Custom type mscAppnIsrSessTransmissionPriority based on Integer32"""
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
        *(("high", 3),
          ("low", 1),
          ("medium", 2),
          ("network", 4))
    )


_MscAppnIsrSessTransmissionPriority_Type.__name__ = "Integer32"
_MscAppnIsrSessTransmissionPriority_Object = MibTableColumn
mscAppnIsrSessTransmissionPriority = _MscAppnIsrSessTransmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 10, 1, 1),
    _MscAppnIsrSessTransmissionPriority_Type()
)
mscAppnIsrSessTransmissionPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessTransmissionPriority.setStatus("mandatory")


class _MscAppnIsrSessCosName_Type(AsciiString):
    """Custom type mscAppnIsrSessCosName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MscAppnIsrSessCosName_Type.__name__ = "AsciiString"
_MscAppnIsrSessCosName_Object = MibTableColumn
mscAppnIsrSessCosName = _MscAppnIsrSessCosName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 10, 1, 2),
    _MscAppnIsrSessCosName_Type()
)
mscAppnIsrSessCosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessCosName.setStatus("mandatory")


class _MscAppnIsrSessLimitedResource_Type(Integer32):
    """Custom type mscAppnIsrSessLimitedResource based on Integer32"""
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


_MscAppnIsrSessLimitedResource_Type.__name__ = "Integer32"
_MscAppnIsrSessLimitedResource_Object = MibTableColumn
mscAppnIsrSessLimitedResource = _MscAppnIsrSessLimitedResource_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 10, 1, 3),
    _MscAppnIsrSessLimitedResource_Type()
)
mscAppnIsrSessLimitedResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessLimitedResource.setStatus("mandatory")
_MscAppnIsrSessPriStats_ObjectIdentity = ObjectIdentity
mscAppnIsrSessPriStats = _MscAppnIsrSessPriStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 100)
)
_MscAppnIsrSessPriStatsRowStatusTable_Object = MibTable
mscAppnIsrSessPriStatsRowStatusTable = _MscAppnIsrSessPriStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 100, 1)
)
if mibBuilder.loadTexts:
    mscAppnIsrSessPriStatsRowStatusTable.setStatus("mandatory")
_MscAppnIsrSessPriStatsRowStatusEntry_Object = MibTableRow
mscAppnIsrSessPriStatsRowStatusEntry = _MscAppnIsrSessPriStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 100, 1, 1)
)
mscAppnIsrSessPriStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIsrSessFqcpNameIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIsrSessProcedureCorrelationIdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIsrSessPriStatsIndex"),
)
if mibBuilder.loadTexts:
    mscAppnIsrSessPriStatsRowStatusEntry.setStatus("mandatory")
_MscAppnIsrSessPriStatsRowStatus_Type = RowStatus
_MscAppnIsrSessPriStatsRowStatus_Object = MibTableColumn
mscAppnIsrSessPriStatsRowStatus = _MscAppnIsrSessPriStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 100, 1, 1, 1),
    _MscAppnIsrSessPriStatsRowStatus_Type()
)
mscAppnIsrSessPriStatsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessPriStatsRowStatus.setStatus("mandatory")
_MscAppnIsrSessPriStatsComponentName_Type = DisplayString
_MscAppnIsrSessPriStatsComponentName_Object = MibTableColumn
mscAppnIsrSessPriStatsComponentName = _MscAppnIsrSessPriStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 100, 1, 1, 2),
    _MscAppnIsrSessPriStatsComponentName_Type()
)
mscAppnIsrSessPriStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessPriStatsComponentName.setStatus("mandatory")
_MscAppnIsrSessPriStatsStorageType_Type = StorageType
_MscAppnIsrSessPriStatsStorageType_Object = MibTableColumn
mscAppnIsrSessPriStatsStorageType = _MscAppnIsrSessPriStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 100, 1, 1, 4),
    _MscAppnIsrSessPriStatsStorageType_Type()
)
mscAppnIsrSessPriStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessPriStatsStorageType.setStatus("mandatory")
_MscAppnIsrSessPriStatsIndex_Type = NonReplicated
_MscAppnIsrSessPriStatsIndex_Object = MibTableColumn
mscAppnIsrSessPriStatsIndex = _MscAppnIsrSessPriStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 100, 1, 1, 10),
    _MscAppnIsrSessPriStatsIndex_Type()
)
mscAppnIsrSessPriStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnIsrSessPriStatsIndex.setStatus("mandatory")
_MscAppnIsrSessPriStatsStatsTable_Object = MibTable
mscAppnIsrSessPriStatsStatsTable = _MscAppnIsrSessPriStatsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 100, 10)
)
if mibBuilder.loadTexts:
    mscAppnIsrSessPriStatsStatsTable.setStatus("mandatory")
_MscAppnIsrSessPriStatsStatsEntry_Object = MibTableRow
mscAppnIsrSessPriStatsStatsEntry = _MscAppnIsrSessPriStatsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 100, 10, 1)
)
mscAppnIsrSessPriStatsStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIsrSessFqcpNameIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIsrSessProcedureCorrelationIdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIsrSessPriStatsIndex"),
)
if mibBuilder.loadTexts:
    mscAppnIsrSessPriStatsStatsEntry.setStatus("mandatory")


class _MscAppnIsrSessPriStatsRxRuSize_Type(Unsigned32):
    """Custom type mscAppnIsrSessPriStatsRxRuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnIsrSessPriStatsRxRuSize_Type.__name__ = "Unsigned32"
_MscAppnIsrSessPriStatsRxRuSize_Object = MibTableColumn
mscAppnIsrSessPriStatsRxRuSize = _MscAppnIsrSessPriStatsRxRuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 100, 10, 1, 1),
    _MscAppnIsrSessPriStatsRxRuSize_Type()
)
mscAppnIsrSessPriStatsRxRuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessPriStatsRxRuSize.setStatus("mandatory")


class _MscAppnIsrSessPriStatsMaxTxBtuSize_Type(Unsigned32):
    """Custom type mscAppnIsrSessPriStatsMaxTxBtuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnIsrSessPriStatsMaxTxBtuSize_Type.__name__ = "Unsigned32"
_MscAppnIsrSessPriStatsMaxTxBtuSize_Object = MibTableColumn
mscAppnIsrSessPriStatsMaxTxBtuSize = _MscAppnIsrSessPriStatsMaxTxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 100, 10, 1, 2),
    _MscAppnIsrSessPriStatsMaxTxBtuSize_Type()
)
mscAppnIsrSessPriStatsMaxTxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessPriStatsMaxTxBtuSize.setStatus("mandatory")


class _MscAppnIsrSessPriStatsMaxRxBtuSize_Type(Unsigned32):
    """Custom type mscAppnIsrSessPriStatsMaxRxBtuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnIsrSessPriStatsMaxRxBtuSize_Type.__name__ = "Unsigned32"
_MscAppnIsrSessPriStatsMaxRxBtuSize_Object = MibTableColumn
mscAppnIsrSessPriStatsMaxRxBtuSize = _MscAppnIsrSessPriStatsMaxRxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 100, 10, 1, 3),
    _MscAppnIsrSessPriStatsMaxRxBtuSize_Type()
)
mscAppnIsrSessPriStatsMaxRxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessPriStatsMaxRxBtuSize.setStatus("mandatory")


class _MscAppnIsrSessPriStatsMaxTxPacWin_Type(Integer32):
    """Custom type mscAppnIsrSessPriStatsMaxTxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscAppnIsrSessPriStatsMaxTxPacWin_Type.__name__ = "Integer32"
_MscAppnIsrSessPriStatsMaxTxPacWin_Object = MibTableColumn
mscAppnIsrSessPriStatsMaxTxPacWin = _MscAppnIsrSessPriStatsMaxTxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 100, 10, 1, 4),
    _MscAppnIsrSessPriStatsMaxTxPacWin_Type()
)
mscAppnIsrSessPriStatsMaxTxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessPriStatsMaxTxPacWin.setStatus("mandatory")


class _MscAppnIsrSessPriStatsCurTxPacWin_Type(Integer32):
    """Custom type mscAppnIsrSessPriStatsCurTxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscAppnIsrSessPriStatsCurTxPacWin_Type.__name__ = "Integer32"
_MscAppnIsrSessPriStatsCurTxPacWin_Object = MibTableColumn
mscAppnIsrSessPriStatsCurTxPacWin = _MscAppnIsrSessPriStatsCurTxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 100, 10, 1, 5),
    _MscAppnIsrSessPriStatsCurTxPacWin_Type()
)
mscAppnIsrSessPriStatsCurTxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessPriStatsCurTxPacWin.setStatus("mandatory")


class _MscAppnIsrSessPriStatsMaxRxPacWin_Type(Integer32):
    """Custom type mscAppnIsrSessPriStatsMaxRxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscAppnIsrSessPriStatsMaxRxPacWin_Type.__name__ = "Integer32"
_MscAppnIsrSessPriStatsMaxRxPacWin_Object = MibTableColumn
mscAppnIsrSessPriStatsMaxRxPacWin = _MscAppnIsrSessPriStatsMaxRxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 100, 10, 1, 6),
    _MscAppnIsrSessPriStatsMaxRxPacWin_Type()
)
mscAppnIsrSessPriStatsMaxRxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessPriStatsMaxRxPacWin.setStatus("mandatory")


class _MscAppnIsrSessPriStatsCurRxPacWin_Type(Integer32):
    """Custom type mscAppnIsrSessPriStatsCurRxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscAppnIsrSessPriStatsCurRxPacWin_Type.__name__ = "Integer32"
_MscAppnIsrSessPriStatsCurRxPacWin_Object = MibTableColumn
mscAppnIsrSessPriStatsCurRxPacWin = _MscAppnIsrSessPriStatsCurRxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 100, 10, 1, 7),
    _MscAppnIsrSessPriStatsCurRxPacWin_Type()
)
mscAppnIsrSessPriStatsCurRxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessPriStatsCurRxPacWin.setStatus("mandatory")
_MscAppnIsrSessPriStatsTxDataframes_Type = PassportCounter64
_MscAppnIsrSessPriStatsTxDataframes_Object = MibTableColumn
mscAppnIsrSessPriStatsTxDataframes = _MscAppnIsrSessPriStatsTxDataframes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 100, 10, 1, 8),
    _MscAppnIsrSessPriStatsTxDataframes_Type()
)
mscAppnIsrSessPriStatsTxDataframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessPriStatsTxDataframes.setStatus("mandatory")
_MscAppnIsrSessPriStatsTxFmdFrames_Type = PassportCounter64
_MscAppnIsrSessPriStatsTxFmdFrames_Object = MibTableColumn
mscAppnIsrSessPriStatsTxFmdFrames = _MscAppnIsrSessPriStatsTxFmdFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 100, 10, 1, 9),
    _MscAppnIsrSessPriStatsTxFmdFrames_Type()
)
mscAppnIsrSessPriStatsTxFmdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessPriStatsTxFmdFrames.setStatus("mandatory")
_MscAppnIsrSessPriStatsTxDataBytes_Type = PassportCounter64
_MscAppnIsrSessPriStatsTxDataBytes_Object = MibTableColumn
mscAppnIsrSessPriStatsTxDataBytes = _MscAppnIsrSessPriStatsTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 100, 10, 1, 10),
    _MscAppnIsrSessPriStatsTxDataBytes_Type()
)
mscAppnIsrSessPriStatsTxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessPriStatsTxDataBytes.setStatus("mandatory")
_MscAppnIsrSessPriStatsRxDataFrames_Type = PassportCounter64
_MscAppnIsrSessPriStatsRxDataFrames_Object = MibTableColumn
mscAppnIsrSessPriStatsRxDataFrames = _MscAppnIsrSessPriStatsRxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 100, 10, 1, 11),
    _MscAppnIsrSessPriStatsRxDataFrames_Type()
)
mscAppnIsrSessPriStatsRxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessPriStatsRxDataFrames.setStatus("mandatory")
_MscAppnIsrSessPriStatsRxFmdFrames_Type = PassportCounter64
_MscAppnIsrSessPriStatsRxFmdFrames_Object = MibTableColumn
mscAppnIsrSessPriStatsRxFmdFrames = _MscAppnIsrSessPriStatsRxFmdFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 100, 10, 1, 12),
    _MscAppnIsrSessPriStatsRxFmdFrames_Type()
)
mscAppnIsrSessPriStatsRxFmdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessPriStatsRxFmdFrames.setStatus("mandatory")
_MscAppnIsrSessPriStatsRxDataBytes_Type = PassportCounter64
_MscAppnIsrSessPriStatsRxDataBytes_Object = MibTableColumn
mscAppnIsrSessPriStatsRxDataBytes = _MscAppnIsrSessPriStatsRxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 100, 10, 1, 13),
    _MscAppnIsrSessPriStatsRxDataBytes_Type()
)
mscAppnIsrSessPriStatsRxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessPriStatsRxDataBytes.setStatus("mandatory")


class _MscAppnIsrSessPriStatsSidh_Type(Hex):
    """Custom type mscAppnIsrSessPriStatsSidh based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnIsrSessPriStatsSidh_Type.__name__ = "Hex"
_MscAppnIsrSessPriStatsSidh_Object = MibTableColumn
mscAppnIsrSessPriStatsSidh = _MscAppnIsrSessPriStatsSidh_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 100, 10, 1, 14),
    _MscAppnIsrSessPriStatsSidh_Type()
)
mscAppnIsrSessPriStatsSidh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessPriStatsSidh.setStatus("mandatory")


class _MscAppnIsrSessPriStatsSidl_Type(Hex):
    """Custom type mscAppnIsrSessPriStatsSidl based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnIsrSessPriStatsSidl_Type.__name__ = "Hex"
_MscAppnIsrSessPriStatsSidl_Object = MibTableColumn
mscAppnIsrSessPriStatsSidl = _MscAppnIsrSessPriStatsSidl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 100, 10, 1, 15),
    _MscAppnIsrSessPriStatsSidl_Type()
)
mscAppnIsrSessPriStatsSidl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessPriStatsSidl.setStatus("mandatory")


class _MscAppnIsrSessPriStatsOdai_Type(Integer32):
    """Custom type mscAppnIsrSessPriStatsOdai based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("primary", 0),
          ("secondary", 1))
    )


_MscAppnIsrSessPriStatsOdai_Type.__name__ = "Integer32"
_MscAppnIsrSessPriStatsOdai_Object = MibTableColumn
mscAppnIsrSessPriStatsOdai = _MscAppnIsrSessPriStatsOdai_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 100, 10, 1, 16),
    _MscAppnIsrSessPriStatsOdai_Type()
)
mscAppnIsrSessPriStatsOdai.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessPriStatsOdai.setStatus("mandatory")


class _MscAppnIsrSessPriStatsLsName_Type(AsciiString):
    """Custom type mscAppnIsrSessPriStatsLsName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MscAppnIsrSessPriStatsLsName_Type.__name__ = "AsciiString"
_MscAppnIsrSessPriStatsLsName_Object = MibTableColumn
mscAppnIsrSessPriStatsLsName = _MscAppnIsrSessPriStatsLsName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 100, 10, 1, 17),
    _MscAppnIsrSessPriStatsLsName_Type()
)
mscAppnIsrSessPriStatsLsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessPriStatsLsName.setStatus("mandatory")
_MscAppnIsrSessSecStats_ObjectIdentity = ObjectIdentity
mscAppnIsrSessSecStats = _MscAppnIsrSessSecStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 101)
)
_MscAppnIsrSessSecStatsRowStatusTable_Object = MibTable
mscAppnIsrSessSecStatsRowStatusTable = _MscAppnIsrSessSecStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 101, 1)
)
if mibBuilder.loadTexts:
    mscAppnIsrSessSecStatsRowStatusTable.setStatus("mandatory")
_MscAppnIsrSessSecStatsRowStatusEntry_Object = MibTableRow
mscAppnIsrSessSecStatsRowStatusEntry = _MscAppnIsrSessSecStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 101, 1, 1)
)
mscAppnIsrSessSecStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIsrSessFqcpNameIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIsrSessProcedureCorrelationIdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIsrSessSecStatsIndex"),
)
if mibBuilder.loadTexts:
    mscAppnIsrSessSecStatsRowStatusEntry.setStatus("mandatory")
_MscAppnIsrSessSecStatsRowStatus_Type = RowStatus
_MscAppnIsrSessSecStatsRowStatus_Object = MibTableColumn
mscAppnIsrSessSecStatsRowStatus = _MscAppnIsrSessSecStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 101, 1, 1, 1),
    _MscAppnIsrSessSecStatsRowStatus_Type()
)
mscAppnIsrSessSecStatsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessSecStatsRowStatus.setStatus("mandatory")
_MscAppnIsrSessSecStatsComponentName_Type = DisplayString
_MscAppnIsrSessSecStatsComponentName_Object = MibTableColumn
mscAppnIsrSessSecStatsComponentName = _MscAppnIsrSessSecStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 101, 1, 1, 2),
    _MscAppnIsrSessSecStatsComponentName_Type()
)
mscAppnIsrSessSecStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessSecStatsComponentName.setStatus("mandatory")
_MscAppnIsrSessSecStatsStorageType_Type = StorageType
_MscAppnIsrSessSecStatsStorageType_Object = MibTableColumn
mscAppnIsrSessSecStatsStorageType = _MscAppnIsrSessSecStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 101, 1, 1, 4),
    _MscAppnIsrSessSecStatsStorageType_Type()
)
mscAppnIsrSessSecStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessSecStatsStorageType.setStatus("mandatory")
_MscAppnIsrSessSecStatsIndex_Type = NonReplicated
_MscAppnIsrSessSecStatsIndex_Object = MibTableColumn
mscAppnIsrSessSecStatsIndex = _MscAppnIsrSessSecStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 101, 1, 1, 10),
    _MscAppnIsrSessSecStatsIndex_Type()
)
mscAppnIsrSessSecStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnIsrSessSecStatsIndex.setStatus("mandatory")
_MscAppnIsrSessSecStatsStatsTable_Object = MibTable
mscAppnIsrSessSecStatsStatsTable = _MscAppnIsrSessSecStatsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 101, 10)
)
if mibBuilder.loadTexts:
    mscAppnIsrSessSecStatsStatsTable.setStatus("mandatory")
_MscAppnIsrSessSecStatsStatsEntry_Object = MibTableRow
mscAppnIsrSessSecStatsStatsEntry = _MscAppnIsrSessSecStatsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 101, 10, 1)
)
mscAppnIsrSessSecStatsStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIsrSessFqcpNameIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIsrSessProcedureCorrelationIdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIsrSessSecStatsIndex"),
)
if mibBuilder.loadTexts:
    mscAppnIsrSessSecStatsStatsEntry.setStatus("mandatory")


class _MscAppnIsrSessSecStatsRxRuSize_Type(Unsigned32):
    """Custom type mscAppnIsrSessSecStatsRxRuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnIsrSessSecStatsRxRuSize_Type.__name__ = "Unsigned32"
_MscAppnIsrSessSecStatsRxRuSize_Object = MibTableColumn
mscAppnIsrSessSecStatsRxRuSize = _MscAppnIsrSessSecStatsRxRuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 101, 10, 1, 1),
    _MscAppnIsrSessSecStatsRxRuSize_Type()
)
mscAppnIsrSessSecStatsRxRuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessSecStatsRxRuSize.setStatus("mandatory")


class _MscAppnIsrSessSecStatsMaxTxBtuSize_Type(Unsigned32):
    """Custom type mscAppnIsrSessSecStatsMaxTxBtuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnIsrSessSecStatsMaxTxBtuSize_Type.__name__ = "Unsigned32"
_MscAppnIsrSessSecStatsMaxTxBtuSize_Object = MibTableColumn
mscAppnIsrSessSecStatsMaxTxBtuSize = _MscAppnIsrSessSecStatsMaxTxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 101, 10, 1, 2),
    _MscAppnIsrSessSecStatsMaxTxBtuSize_Type()
)
mscAppnIsrSessSecStatsMaxTxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessSecStatsMaxTxBtuSize.setStatus("mandatory")


class _MscAppnIsrSessSecStatsMaxRxBtuSize_Type(Unsigned32):
    """Custom type mscAppnIsrSessSecStatsMaxRxBtuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnIsrSessSecStatsMaxRxBtuSize_Type.__name__ = "Unsigned32"
_MscAppnIsrSessSecStatsMaxRxBtuSize_Object = MibTableColumn
mscAppnIsrSessSecStatsMaxRxBtuSize = _MscAppnIsrSessSecStatsMaxRxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 101, 10, 1, 3),
    _MscAppnIsrSessSecStatsMaxRxBtuSize_Type()
)
mscAppnIsrSessSecStatsMaxRxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessSecStatsMaxRxBtuSize.setStatus("mandatory")


class _MscAppnIsrSessSecStatsMaxTxPacWin_Type(Integer32):
    """Custom type mscAppnIsrSessSecStatsMaxTxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscAppnIsrSessSecStatsMaxTxPacWin_Type.__name__ = "Integer32"
_MscAppnIsrSessSecStatsMaxTxPacWin_Object = MibTableColumn
mscAppnIsrSessSecStatsMaxTxPacWin = _MscAppnIsrSessSecStatsMaxTxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 101, 10, 1, 4),
    _MscAppnIsrSessSecStatsMaxTxPacWin_Type()
)
mscAppnIsrSessSecStatsMaxTxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessSecStatsMaxTxPacWin.setStatus("mandatory")


class _MscAppnIsrSessSecStatsCurTxPacWin_Type(Integer32):
    """Custom type mscAppnIsrSessSecStatsCurTxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscAppnIsrSessSecStatsCurTxPacWin_Type.__name__ = "Integer32"
_MscAppnIsrSessSecStatsCurTxPacWin_Object = MibTableColumn
mscAppnIsrSessSecStatsCurTxPacWin = _MscAppnIsrSessSecStatsCurTxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 101, 10, 1, 5),
    _MscAppnIsrSessSecStatsCurTxPacWin_Type()
)
mscAppnIsrSessSecStatsCurTxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessSecStatsCurTxPacWin.setStatus("mandatory")


class _MscAppnIsrSessSecStatsMaxRxPacWin_Type(Integer32):
    """Custom type mscAppnIsrSessSecStatsMaxRxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscAppnIsrSessSecStatsMaxRxPacWin_Type.__name__ = "Integer32"
_MscAppnIsrSessSecStatsMaxRxPacWin_Object = MibTableColumn
mscAppnIsrSessSecStatsMaxRxPacWin = _MscAppnIsrSessSecStatsMaxRxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 101, 10, 1, 6),
    _MscAppnIsrSessSecStatsMaxRxPacWin_Type()
)
mscAppnIsrSessSecStatsMaxRxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessSecStatsMaxRxPacWin.setStatus("mandatory")


class _MscAppnIsrSessSecStatsCurRxPacWin_Type(Integer32):
    """Custom type mscAppnIsrSessSecStatsCurRxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscAppnIsrSessSecStatsCurRxPacWin_Type.__name__ = "Integer32"
_MscAppnIsrSessSecStatsCurRxPacWin_Object = MibTableColumn
mscAppnIsrSessSecStatsCurRxPacWin = _MscAppnIsrSessSecStatsCurRxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 101, 10, 1, 7),
    _MscAppnIsrSessSecStatsCurRxPacWin_Type()
)
mscAppnIsrSessSecStatsCurRxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessSecStatsCurRxPacWin.setStatus("mandatory")
_MscAppnIsrSessSecStatsTxDataframes_Type = PassportCounter64
_MscAppnIsrSessSecStatsTxDataframes_Object = MibTableColumn
mscAppnIsrSessSecStatsTxDataframes = _MscAppnIsrSessSecStatsTxDataframes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 101, 10, 1, 8),
    _MscAppnIsrSessSecStatsTxDataframes_Type()
)
mscAppnIsrSessSecStatsTxDataframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessSecStatsTxDataframes.setStatus("mandatory")
_MscAppnIsrSessSecStatsTxFmdFrames_Type = PassportCounter64
_MscAppnIsrSessSecStatsTxFmdFrames_Object = MibTableColumn
mscAppnIsrSessSecStatsTxFmdFrames = _MscAppnIsrSessSecStatsTxFmdFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 101, 10, 1, 9),
    _MscAppnIsrSessSecStatsTxFmdFrames_Type()
)
mscAppnIsrSessSecStatsTxFmdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessSecStatsTxFmdFrames.setStatus("mandatory")
_MscAppnIsrSessSecStatsTxDataBytes_Type = PassportCounter64
_MscAppnIsrSessSecStatsTxDataBytes_Object = MibTableColumn
mscAppnIsrSessSecStatsTxDataBytes = _MscAppnIsrSessSecStatsTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 101, 10, 1, 10),
    _MscAppnIsrSessSecStatsTxDataBytes_Type()
)
mscAppnIsrSessSecStatsTxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessSecStatsTxDataBytes.setStatus("mandatory")
_MscAppnIsrSessSecStatsRxDataFrames_Type = PassportCounter64
_MscAppnIsrSessSecStatsRxDataFrames_Object = MibTableColumn
mscAppnIsrSessSecStatsRxDataFrames = _MscAppnIsrSessSecStatsRxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 101, 10, 1, 11),
    _MscAppnIsrSessSecStatsRxDataFrames_Type()
)
mscAppnIsrSessSecStatsRxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessSecStatsRxDataFrames.setStatus("mandatory")
_MscAppnIsrSessSecStatsRxFmdFrames_Type = PassportCounter64
_MscAppnIsrSessSecStatsRxFmdFrames_Object = MibTableColumn
mscAppnIsrSessSecStatsRxFmdFrames = _MscAppnIsrSessSecStatsRxFmdFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 101, 10, 1, 12),
    _MscAppnIsrSessSecStatsRxFmdFrames_Type()
)
mscAppnIsrSessSecStatsRxFmdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessSecStatsRxFmdFrames.setStatus("mandatory")
_MscAppnIsrSessSecStatsRxDataBytes_Type = PassportCounter64
_MscAppnIsrSessSecStatsRxDataBytes_Object = MibTableColumn
mscAppnIsrSessSecStatsRxDataBytes = _MscAppnIsrSessSecStatsRxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 101, 10, 1, 13),
    _MscAppnIsrSessSecStatsRxDataBytes_Type()
)
mscAppnIsrSessSecStatsRxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessSecStatsRxDataBytes.setStatus("mandatory")


class _MscAppnIsrSessSecStatsSidh_Type(Hex):
    """Custom type mscAppnIsrSessSecStatsSidh based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnIsrSessSecStatsSidh_Type.__name__ = "Hex"
_MscAppnIsrSessSecStatsSidh_Object = MibTableColumn
mscAppnIsrSessSecStatsSidh = _MscAppnIsrSessSecStatsSidh_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 101, 10, 1, 14),
    _MscAppnIsrSessSecStatsSidh_Type()
)
mscAppnIsrSessSecStatsSidh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessSecStatsSidh.setStatus("mandatory")


class _MscAppnIsrSessSecStatsSidl_Type(Hex):
    """Custom type mscAppnIsrSessSecStatsSidl based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnIsrSessSecStatsSidl_Type.__name__ = "Hex"
_MscAppnIsrSessSecStatsSidl_Object = MibTableColumn
mscAppnIsrSessSecStatsSidl = _MscAppnIsrSessSecStatsSidl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 101, 10, 1, 15),
    _MscAppnIsrSessSecStatsSidl_Type()
)
mscAppnIsrSessSecStatsSidl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessSecStatsSidl.setStatus("mandatory")


class _MscAppnIsrSessSecStatsOdai_Type(Integer32):
    """Custom type mscAppnIsrSessSecStatsOdai based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("primary", 0),
          ("secondary", 1))
    )


_MscAppnIsrSessSecStatsOdai_Type.__name__ = "Integer32"
_MscAppnIsrSessSecStatsOdai_Object = MibTableColumn
mscAppnIsrSessSecStatsOdai = _MscAppnIsrSessSecStatsOdai_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 101, 10, 1, 16),
    _MscAppnIsrSessSecStatsOdai_Type()
)
mscAppnIsrSessSecStatsOdai.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessSecStatsOdai.setStatus("mandatory")


class _MscAppnIsrSessSecStatsLsName_Type(AsciiString):
    """Custom type mscAppnIsrSessSecStatsLsName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MscAppnIsrSessSecStatsLsName_Type.__name__ = "AsciiString"
_MscAppnIsrSessSecStatsLsName_Object = MibTableColumn
mscAppnIsrSessSecStatsLsName = _MscAppnIsrSessSecStatsLsName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 11, 101, 10, 1, 17),
    _MscAppnIsrSessSecStatsLsName_Type()
)
mscAppnIsrSessSecStatsLsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnIsrSessSecStatsLsName.setStatus("mandatory")
_MscAppnNnTg_ObjectIdentity = ObjectIdentity
mscAppnNnTg = _MscAppnNnTg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 12)
)
_MscAppnNnTgRowStatusTable_Object = MibTable
mscAppnNnTgRowStatusTable = _MscAppnNnTgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 12, 1)
)
if mibBuilder.loadTexts:
    mscAppnNnTgRowStatusTable.setStatus("mandatory")
_MscAppnNnTgRowStatusEntry_Object = MibTableRow
mscAppnNnTgRowStatusEntry = _MscAppnNnTgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 12, 1, 1)
)
mscAppnNnTgRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnNnTgOwnerFqcpNameIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnNnTgDestFqcpNameIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnNnTgTransmissionGroupIndex"),
)
if mibBuilder.loadTexts:
    mscAppnNnTgRowStatusEntry.setStatus("mandatory")
_MscAppnNnTgRowStatus_Type = RowStatus
_MscAppnNnTgRowStatus_Object = MibTableColumn
mscAppnNnTgRowStatus = _MscAppnNnTgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 12, 1, 1, 1),
    _MscAppnNnTgRowStatus_Type()
)
mscAppnNnTgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnNnTgRowStatus.setStatus("mandatory")
_MscAppnNnTgComponentName_Type = DisplayString
_MscAppnNnTgComponentName_Object = MibTableColumn
mscAppnNnTgComponentName = _MscAppnNnTgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 12, 1, 1, 2),
    _MscAppnNnTgComponentName_Type()
)
mscAppnNnTgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnNnTgComponentName.setStatus("mandatory")
_MscAppnNnTgStorageType_Type = StorageType
_MscAppnNnTgStorageType_Object = MibTableColumn
mscAppnNnTgStorageType = _MscAppnNnTgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 12, 1, 1, 4),
    _MscAppnNnTgStorageType_Type()
)
mscAppnNnTgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnNnTgStorageType.setStatus("mandatory")


class _MscAppnNnTgOwnerFqcpNameIndex_Type(AsciiStringIndex):
    """Custom type mscAppnNnTgOwnerFqcpNameIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_MscAppnNnTgOwnerFqcpNameIndex_Type.__name__ = "AsciiStringIndex"
_MscAppnNnTgOwnerFqcpNameIndex_Object = MibTableColumn
mscAppnNnTgOwnerFqcpNameIndex = _MscAppnNnTgOwnerFqcpNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 12, 1, 1, 10),
    _MscAppnNnTgOwnerFqcpNameIndex_Type()
)
mscAppnNnTgOwnerFqcpNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnNnTgOwnerFqcpNameIndex.setStatus("mandatory")


class _MscAppnNnTgDestFqcpNameIndex_Type(AsciiStringIndex):
    """Custom type mscAppnNnTgDestFqcpNameIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_MscAppnNnTgDestFqcpNameIndex_Type.__name__ = "AsciiStringIndex"
_MscAppnNnTgDestFqcpNameIndex_Object = MibTableColumn
mscAppnNnTgDestFqcpNameIndex = _MscAppnNnTgDestFqcpNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 12, 1, 1, 11),
    _MscAppnNnTgDestFqcpNameIndex_Type()
)
mscAppnNnTgDestFqcpNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnNnTgDestFqcpNameIndex.setStatus("mandatory")


class _MscAppnNnTgTransmissionGroupIndex_Type(Integer32):
    """Custom type mscAppnNnTgTransmissionGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnNnTgTransmissionGroupIndex_Type.__name__ = "Integer32"
_MscAppnNnTgTransmissionGroupIndex_Object = MibTableColumn
mscAppnNnTgTransmissionGroupIndex = _MscAppnNnTgTransmissionGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 12, 1, 1, 12),
    _MscAppnNnTgTransmissionGroupIndex_Type()
)
mscAppnNnTgTransmissionGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnNnTgTransmissionGroupIndex.setStatus("mandatory")
_MscAppnNnTgOperTable_Object = MibTable
mscAppnNnTgOperTable = _MscAppnNnTgOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 12, 10)
)
if mibBuilder.loadTexts:
    mscAppnNnTgOperTable.setStatus("mandatory")
_MscAppnNnTgOperEntry_Object = MibTableRow
mscAppnNnTgOperEntry = _MscAppnNnTgOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 12, 10, 1)
)
mscAppnNnTgOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnNnTgOwnerFqcpNameIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnNnTgDestFqcpNameIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnNnTgTransmissionGroupIndex"),
)
if mibBuilder.loadTexts:
    mscAppnNnTgOperEntry.setStatus("mandatory")


class _MscAppnNnTgFlowReductionSequenceNumber_Type(Unsigned32):
    """Custom type mscAppnNnTgFlowReductionSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAppnNnTgFlowReductionSequenceNumber_Type.__name__ = "Unsigned32"
_MscAppnNnTgFlowReductionSequenceNumber_Object = MibTableColumn
mscAppnNnTgFlowReductionSequenceNumber = _MscAppnNnTgFlowReductionSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 12, 10, 1, 1),
    _MscAppnNnTgFlowReductionSequenceNumber_Type()
)
mscAppnNnTgFlowReductionSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnNnTgFlowReductionSequenceNumber.setStatus("mandatory")


class _MscAppnNnTgDaysLeft_Type(Unsigned32):
    """Custom type mscAppnNnTgDaysLeft based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MscAppnNnTgDaysLeft_Type.__name__ = "Unsigned32"
_MscAppnNnTgDaysLeft_Object = MibTableColumn
mscAppnNnTgDaysLeft = _MscAppnNnTgDaysLeft_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 12, 10, 1, 2),
    _MscAppnNnTgDaysLeft_Type()
)
mscAppnNnTgDaysLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnNnTgDaysLeft.setStatus("mandatory")


class _MscAppnNnTgResourceSequenceNumber_Type(Unsigned32):
    """Custom type mscAppnNnTgResourceSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAppnNnTgResourceSequenceNumber_Type.__name__ = "Unsigned32"
_MscAppnNnTgResourceSequenceNumber_Object = MibTableColumn
mscAppnNnTgResourceSequenceNumber = _MscAppnNnTgResourceSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 12, 10, 1, 3),
    _MscAppnNnTgResourceSequenceNumber_Type()
)
mscAppnNnTgResourceSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnNnTgResourceSequenceNumber.setStatus("mandatory")


class _MscAppnNnTgStatus_Type(OctetString):
    """Custom type mscAppnNnTgStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAppnNnTgStatus_Type.__name__ = "OctetString"
_MscAppnNnTgStatus_Object = MibTableColumn
mscAppnNnTgStatus = _MscAppnNnTgStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 12, 10, 1, 4),
    _MscAppnNnTgStatus_Type()
)
mscAppnNnTgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnNnTgStatus.setStatus("mandatory")
_MscAppnNnTgLinkAddressTable_Object = MibTable
mscAppnNnTgLinkAddressTable = _MscAppnNnTgLinkAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 12, 11)
)
if mibBuilder.loadTexts:
    mscAppnNnTgLinkAddressTable.setStatus("mandatory")
_MscAppnNnTgLinkAddressEntry_Object = MibTableRow
mscAppnNnTgLinkAddressEntry = _MscAppnNnTgLinkAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 12, 11, 1)
)
mscAppnNnTgLinkAddressEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnNnTgOwnerFqcpNameIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnNnTgDestFqcpNameIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnNnTgTransmissionGroupIndex"),
)
if mibBuilder.loadTexts:
    mscAppnNnTgLinkAddressEntry.setStatus("mandatory")


class _MscAppnNnTgDlcData_Type(HexString):
    """Custom type mscAppnNnTgDlcData based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscAppnNnTgDlcData_Type.__name__ = "HexString"
_MscAppnNnTgDlcData_Object = MibTableColumn
mscAppnNnTgDlcData = _MscAppnNnTgDlcData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 12, 11, 1, 1),
    _MscAppnNnTgDlcData_Type()
)
mscAppnNnTgDlcData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnNnTgDlcData.setStatus("mandatory")
_MscAppnNnTgTgCharTable_Object = MibTable
mscAppnNnTgTgCharTable = _MscAppnNnTgTgCharTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 12, 12)
)
if mibBuilder.loadTexts:
    mscAppnNnTgTgCharTable.setStatus("mandatory")
_MscAppnNnTgTgCharEntry_Object = MibTableRow
mscAppnNnTgTgCharEntry = _MscAppnNnTgTgCharEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 12, 12, 1)
)
mscAppnNnTgTgCharEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnNnTgOwnerFqcpNameIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnNnTgDestFqcpNameIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnNnTgTransmissionGroupIndex"),
)
if mibBuilder.loadTexts:
    mscAppnNnTgTgCharEntry.setStatus("mandatory")


class _MscAppnNnTgEffectiveCap_Type(Integer32):
    """Custom type mscAppnNnTgEffectiveCap based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("min", 0),
          ("n1000kbps", 101),
          ("n10100Mbps", 208),
          ("n101Gbps", 234),
          ("n1020Mbps", 181),
          ("n1050bps", 22),
          ("n106kbps", 75),
          ("n10800bps", 49),
          ("n1080kbps", 102),
          ("n108Mbps", 155),
          ("n1100Mbps", 182),
          ("n11100kbps", 129),
          ("n111Gbps", 235),
          ("n11300Mbps", 209),
          ("n1130bps", 23),
          ("n1150kbps", 103),
          ("n115kbps", 76),
          ("n1180Mbps", 183),
          ("n118Mbps", 156),
          ("n12000bps", 50),
          ("n1200bps", 24),
          ("n121Gbps", 236),
          ("n12300kbps", 130),
          ("n1230kbps", 104),
          ("n125kbps", 77),
          ("n12600Mbps", 210),
          ("n1260Mbps", 184),
          ("n128Mbps", 157),
          ("n131Gbps", 237),
          ("n13200bps", 51),
          ("n134kbps", 78),
          ("n13500kbps", 131),
          ("n1350bps", 25),
          ("n13800Mbps", 211),
          ("n1380kbps", 105),
          ("n138Mbps", 158),
          ("n141Gbps", 238),
          ("n1420Mbps", 185),
          ("n14400bps", 52),
          ("n144kbps", 79),
          ("n14700kbps", 132),
          ("n147Mbps", 159),
          ("n1500bps", 26),
          ("n15100Mbps", 212),
          ("n151Gbps", 239),
          ("n1540kbps", 106),
          ("n154kbps", 80),
          ("n15600bps", 53),
          ("n1570Mbps", 186),
          ("n157Mbps", 160),
          ("n160Gbps", 240),
          ("n16Gbps", 213),
          ("n16Mbps", 133),
          ("n1700Mbps", 187),
          ("n1700bps", 27),
          ("n1700kbps", 107),
          ("n170bps", 1),
          ("n170kbps", 81),
          ("n17Mbps", 134),
          ("n17kbps", 54),
          ("n1800bps", 28),
          ("n1800kbps", 108),
          ("n180Gbps", 241),
          ("n180Mbps", 161),
          ("n18Gbps", 214),
          ("n18Mbps", 135),
          ("n18kbps", 55),
          ("n1900Mbps", 188),
          ("n190bps", 2),
          ("n190kbps", 82),
          ("n19Gbps", 215),
          ("n19kbps", 56),
          ("n2000Mbps", 189),
          ("n2000bps", 29),
          ("n2000kbps", 109),
          ("n200Gbps", 242),
          ("n200Mbps", 162),
          ("n20Gbps", 216),
          ("n20Mbps", 136),
          ("n2100bps", 30),
          ("n210bps", 3),
          ("n210kbps", 83),
          ("n2200Mbps", 190),
          ("n2200kbps", 110),
          ("n220Gbps", 243),
          ("n220Mbps", 163),
          ("n22Mbps", 137),
          ("n22kbps", 57),
          ("n2300bps", 31),
          ("n2300kbps", 111),
          ("n230bps", 4),
          ("n230kbps", 84),
          ("n23Gbps", 217),
          ("n2400Mbps", 191),
          ("n2400bps", 32),
          ("n240Gbps", 244),
          ("n240Mbps", 164),
          ("n240bps", 5),
          ("n24kbps", 58),
          ("n2500Mbps", 192),
          ("n2500kbps", 112),
          ("n250kbps", 85),
          ("n25Gbps", 218),
          ("n25Mbps", 138),
          ("n260Gbps", 245),
          ("n260Mbps", 165),
          ("n260bps", 6),
          ("n26kbps", 59),
          ("n2700bps", 33),
          ("n270kbps", 86),
          ("n27Mbps", 139),
          ("n2800Mbps", 193),
          ("n2800kbps", 113),
          ("n280Gbps", 246),
          ("n280Mbps", 166),
          ("n280bps", 7),
          ("n28Gbps", 219),
          ("n290Mbps", 167),
          ("n290kbps", 87),
          ("n29Mbps", 140),
          ("n29kbps", 60),
          ("n3000bps", 34),
          ("n300Gbps", 247),
          ("n300bps", 8),
          ("n30Gbps", 220),
          ("n3100Mbps", 194),
          ("n3100kbps", 114),
          ("n310Mbps", 168),
          ("n310kbps", 88),
          ("n31kbps", 61),
          ("n320Gbps", 248),
          ("n32Mbps", 141),
          ("n3300bps", 35),
          ("n33Gbps", 221),
          ("n3400kbps", 115),
          ("n340bps", 9),
          ("n34Mbps", 142),
          ("n34kbps", 62),
          ("n3500Mbps", 195),
          ("n350Mbps", 169),
          ("n350kbps", 89),
          ("n35Gbps", 222),
          ("n3600bps", 36),
          ("n360Gbps", 249),
          ("n36kbps", 63),
          ("n3700kbps", 116),
          ("n37Mbps", 143),
          ("n3800Mbps", 196),
          ("n380bps", 10),
          ("n380kbps", 90),
          ("n38Gbps", 223),
          ("n38kbps", 64),
          ("n3900bps", 37),
          ("n390Mbps", 170),
          ("n39Mbps", 144),
          ("n4000kbps", 117),
          ("n400Gbps", 250),
          ("n40Gbps", 224),
          ("n4100Mbps", 197),
          ("n410bps", 11),
          ("n4200bps", 38),
          ("n420kbps", 91),
          ("n4300kbps", 118),
          ("n430Mbps", 171),
          ("n43kbps", 65),
          ("n4400Mbps", 198),
          ("n440Gbps", 251),
          ("n44Mbps", 145),
          ("n4500bps", 39),
          ("n450bps", 12),
          ("n45Gbps", 225),
          ("n4600kbps", 119),
          ("n460kbps", 92),
          ("n4700Mbps", 199),
          ("n470Mbps", 172),
          ("n4800bps", 40),
          ("n480Gbps", 252),
          ("n48kbps", 66),
          ("n4900kbps", 120),
          ("n490bps", 13),
          ("n49Mbps", 146),
          ("n5000Mbps", 200),
          ("n500kbps", 93),
          ("n50Gbps", 226),
          ("n510Mbps", 173),
          ("n520Gbps", 253),
          ("n530bps", 14),
          ("n53kbps", 67),
          ("n5400bps", 41),
          ("n540kbps", 94),
          ("n54Mbps", 147),
          ("n5500kbps", 121),
          ("n550Mbps", 174),
          ("n55Gbps", 227),
          ("n560Gbps", 254),
          ("n560bps", 15),
          ("n5700Mbps", 201),
          ("n580kbps", 95),
          ("n58kbps", 68),
          ("n590Mbps", 175),
          ("n59Mbps", 148),
          ("n6000bps", 42),
          ("n600Gbps", 255),
          ("n600bps", 16),
          ("n60Gbps", 228),
          ("n6100kbps", 122),
          ("n610kbps", 96),
          ("n62kbps", 69),
          ("n6300Mbps", 202),
          ("n630Mbps", 176),
          ("n64Mbps", 149),
          ("n65Gbps", 229),
          ("n6600bps", 43),
          ("n67kbps", 70),
          ("n6800kbps", 123),
          ("n680bps", 17),
          ("n6900Mbps", 203),
          ("n690kbps", 97),
          ("n69Mbps", 150),
          ("n70Gbps", 230),
          ("n710Mbps", 177),
          ("n7200bps", 44),
          ("n72kbps", 71),
          ("n7400kbps", 124),
          ("n74Mbps", 151),
          ("n7500Mbps", 204),
          ("n750bps", 18),
          ("n75Gbps", 231),
          ("n770kbps", 98),
          ("n77kbps", 72),
          ("n7800bps", 45),
          ("n790Mbps", 178),
          ("n79Mbps", 152),
          ("n8000kbps", 125),
          ("n81Gbps", 232),
          ("n8200Mbps", 205),
          ("n830bps", 19),
          ("n8400bps", 46),
          ("n840kbps", 99),
          ("n8600kbps", 126),
          ("n86kbps", 73),
          ("n870Mbps", 179),
          ("n8800Mbps", 206),
          ("n88Mbps", 153),
          ("n9000bps", 47),
          ("n900bps", 20),
          ("n91Gbps", 233),
          ("n9200kbps", 127),
          ("n920kbps", 100),
          ("n9400Mbps", 207),
          ("n940Mbps", 180),
          ("n9600bps", 48),
          ("n96kbps", 74),
          ("n9800kbps", 128),
          ("n980bps", 21),
          ("n98Mbps", 154))
    )


_MscAppnNnTgEffectiveCap_Type.__name__ = "Integer32"
_MscAppnNnTgEffectiveCap_Object = MibTableColumn
mscAppnNnTgEffectiveCap = _MscAppnNnTgEffectiveCap_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 12, 12, 1, 1),
    _MscAppnNnTgEffectiveCap_Type()
)
mscAppnNnTgEffectiveCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnNnTgEffectiveCap.setStatus("mandatory")


class _MscAppnNnTgConnectCost_Type(Integer32):
    """Custom type mscAppnNnTgConnectCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnNnTgConnectCost_Type.__name__ = "Integer32"
_MscAppnNnTgConnectCost_Object = MibTableColumn
mscAppnNnTgConnectCost = _MscAppnNnTgConnectCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 12, 12, 1, 2),
    _MscAppnNnTgConnectCost_Type()
)
mscAppnNnTgConnectCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnNnTgConnectCost.setStatus("mandatory")


class _MscAppnNnTgByteCost_Type(Integer32):
    """Custom type mscAppnNnTgByteCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnNnTgByteCost_Type.__name__ = "Integer32"
_MscAppnNnTgByteCost_Object = MibTableColumn
mscAppnNnTgByteCost = _MscAppnNnTgByteCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 12, 12, 1, 3),
    _MscAppnNnTgByteCost_Type()
)
mscAppnNnTgByteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnNnTgByteCost.setStatus("mandatory")


class _MscAppnNnTgSecurity_Type(Integer32):
    """Custom type mscAppnNnTgSecurity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              32,
              64,
              96,
              128,
              160,
              192)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 160),
          ("guardedConduit", 128),
          ("guardedRadiation", 192),
          ("nonSecure", 1),
          ("publicSwitchedNetwork", 32),
          ("secureConduit", 96),
          ("unKnown", 0),
          ("undergroundCable", 64))
    )


_MscAppnNnTgSecurity_Type.__name__ = "Integer32"
_MscAppnNnTgSecurity_Object = MibTableColumn
mscAppnNnTgSecurity = _MscAppnNnTgSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 12, 12, 1, 4),
    _MscAppnNnTgSecurity_Type()
)
mscAppnNnTgSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnNnTgSecurity.setStatus("mandatory")


class _MscAppnNnTgPropagationDelay_Type(Integer32):
    """Custom type mscAppnNnTgPropagationDelay based on Integer32"""
    defaultValue = 113

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              76,
              113,
              145,
              153)
        )
    )
    namedValues = NamedValues(
        *(("long", 153),
          ("minimum", 0),
          ("negligible", 76),
          ("packetSwitched", 145),
          ("terrestrial", 113))
    )


_MscAppnNnTgPropagationDelay_Type.__name__ = "Integer32"
_MscAppnNnTgPropagationDelay_Object = MibTableColumn
mscAppnNnTgPropagationDelay = _MscAppnNnTgPropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 12, 12, 1, 5),
    _MscAppnNnTgPropagationDelay_Type()
)
mscAppnNnTgPropagationDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnNnTgPropagationDelay.setStatus("mandatory")


class _MscAppnNnTgUserDefinedParm1_Type(Unsigned32):
    """Custom type mscAppnNnTgUserDefinedParm1 based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnNnTgUserDefinedParm1_Type.__name__ = "Unsigned32"
_MscAppnNnTgUserDefinedParm1_Object = MibTableColumn
mscAppnNnTgUserDefinedParm1 = _MscAppnNnTgUserDefinedParm1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 12, 12, 1, 7),
    _MscAppnNnTgUserDefinedParm1_Type()
)
mscAppnNnTgUserDefinedParm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnNnTgUserDefinedParm1.setStatus("mandatory")


class _MscAppnNnTgUserDefinedParm2_Type(Unsigned32):
    """Custom type mscAppnNnTgUserDefinedParm2 based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnNnTgUserDefinedParm2_Type.__name__ = "Unsigned32"
_MscAppnNnTgUserDefinedParm2_Object = MibTableColumn
mscAppnNnTgUserDefinedParm2 = _MscAppnNnTgUserDefinedParm2_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 12, 12, 1, 8),
    _MscAppnNnTgUserDefinedParm2_Type()
)
mscAppnNnTgUserDefinedParm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnNnTgUserDefinedParm2.setStatus("mandatory")


class _MscAppnNnTgUserDefinedParm3_Type(Unsigned32):
    """Custom type mscAppnNnTgUserDefinedParm3 based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnNnTgUserDefinedParm3_Type.__name__ = "Unsigned32"
_MscAppnNnTgUserDefinedParm3_Object = MibTableColumn
mscAppnNnTgUserDefinedParm3 = _MscAppnNnTgUserDefinedParm3_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 12, 12, 1, 9),
    _MscAppnNnTgUserDefinedParm3_Type()
)
mscAppnNnTgUserDefinedParm3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnNnTgUserDefinedParm3.setStatus("mandatory")
_MscAppnRtp_ObjectIdentity = ObjectIdentity
mscAppnRtp = _MscAppnRtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13)
)
_MscAppnRtpRowStatusTable_Object = MibTable
mscAppnRtpRowStatusTable = _MscAppnRtpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 1)
)
if mibBuilder.loadTexts:
    mscAppnRtpRowStatusTable.setStatus("mandatory")
_MscAppnRtpRowStatusEntry_Object = MibTableRow
mscAppnRtpRowStatusEntry = _MscAppnRtpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 1, 1)
)
mscAppnRtpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnRtpIndex"),
)
if mibBuilder.loadTexts:
    mscAppnRtpRowStatusEntry.setStatus("mandatory")
_MscAppnRtpRowStatus_Type = RowStatus
_MscAppnRtpRowStatus_Object = MibTableColumn
mscAppnRtpRowStatus = _MscAppnRtpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 1, 1, 1),
    _MscAppnRtpRowStatus_Type()
)
mscAppnRtpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpRowStatus.setStatus("mandatory")
_MscAppnRtpComponentName_Type = DisplayString
_MscAppnRtpComponentName_Object = MibTableColumn
mscAppnRtpComponentName = _MscAppnRtpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 1, 1, 2),
    _MscAppnRtpComponentName_Type()
)
mscAppnRtpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpComponentName.setStatus("mandatory")
_MscAppnRtpStorageType_Type = StorageType
_MscAppnRtpStorageType_Object = MibTableColumn
mscAppnRtpStorageType = _MscAppnRtpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 1, 1, 4),
    _MscAppnRtpStorageType_Type()
)
mscAppnRtpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpStorageType.setStatus("mandatory")


class _MscAppnRtpIndex_Type(AsciiStringIndex):
    """Custom type mscAppnRtpIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MscAppnRtpIndex_Type.__name__ = "AsciiStringIndex"
_MscAppnRtpIndex_Object = MibTableColumn
mscAppnRtpIndex = _MscAppnRtpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 1, 1, 10),
    _MscAppnRtpIndex_Type()
)
mscAppnRtpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnRtpIndex.setStatus("mandatory")
_MscAppnRtpOperTable_Object = MibTable
mscAppnRtpOperTable = _MscAppnRtpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 10)
)
if mibBuilder.loadTexts:
    mscAppnRtpOperTable.setStatus("mandatory")
_MscAppnRtpOperEntry_Object = MibTableRow
mscAppnRtpOperEntry = _MscAppnRtpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 10, 1)
)
mscAppnRtpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnRtpIndex"),
)
if mibBuilder.loadTexts:
    mscAppnRtpOperEntry.setStatus("mandatory")


class _MscAppnRtpLocalLsName_Type(AsciiString):
    """Custom type mscAppnRtpLocalLsName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MscAppnRtpLocalLsName_Type.__name__ = "AsciiString"
_MscAppnRtpLocalLsName_Object = MibTableColumn
mscAppnRtpLocalLsName = _MscAppnRtpLocalLsName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 10, 1, 1),
    _MscAppnRtpLocalLsName_Type()
)
mscAppnRtpLocalLsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpLocalLsName.setStatus("mandatory")


class _MscAppnRtpRemoteCpName_Type(AsciiString):
    """Custom type mscAppnRtpRemoteCpName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_MscAppnRtpRemoteCpName_Type.__name__ = "AsciiString"
_MscAppnRtpRemoteCpName_Object = MibTableColumn
mscAppnRtpRemoteCpName = _MscAppnRtpRemoteCpName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 10, 1, 2),
    _MscAppnRtpRemoteCpName_Type()
)
mscAppnRtpRemoteCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpRemoteCpName.setStatus("mandatory")


class _MscAppnRtpCosName_Type(AsciiString):
    """Custom type mscAppnRtpCosName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MscAppnRtpCosName_Type.__name__ = "AsciiString"
_MscAppnRtpCosName_Object = MibTableColumn
mscAppnRtpCosName = _MscAppnRtpCosName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 10, 1, 3),
    _MscAppnRtpCosName_Type()
)
mscAppnRtpCosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpCosName.setStatus("mandatory")


class _MscAppnRtpActiveSessions_Type(Integer32):
    """Custom type mscAppnRtpActiveSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscAppnRtpActiveSessions_Type.__name__ = "Integer32"
_MscAppnRtpActiveSessions_Object = MibTableColumn
mscAppnRtpActiveSessions = _MscAppnRtpActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 10, 1, 4),
    _MscAppnRtpActiveSessions_Type()
)
mscAppnRtpActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpActiveSessions.setStatus("mandatory")


class _MscAppnRtpLocalTcid_Type(HexString):
    """Custom type mscAppnRtpLocalTcid based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscAppnRtpLocalTcid_Type.__name__ = "HexString"
_MscAppnRtpLocalTcid_Object = MibTableColumn
mscAppnRtpLocalTcid = _MscAppnRtpLocalTcid_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 10, 1, 5),
    _MscAppnRtpLocalTcid_Type()
)
mscAppnRtpLocalTcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpLocalTcid.setStatus("mandatory")


class _MscAppnRtpRemoteTcid_Type(HexString):
    """Custom type mscAppnRtpRemoteTcid based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscAppnRtpRemoteTcid_Type.__name__ = "HexString"
_MscAppnRtpRemoteTcid_Object = MibTableColumn
mscAppnRtpRemoteTcid = _MscAppnRtpRemoteTcid_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 10, 1, 6),
    _MscAppnRtpRemoteTcid_Type()
)
mscAppnRtpRemoteTcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpRemoteTcid.setStatus("mandatory")


class _MscAppnRtpIdleTimer_Type(Unsigned32):
    """Custom type mscAppnRtpIdleTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAppnRtpIdleTimer_Type.__name__ = "Unsigned32"
_MscAppnRtpIdleTimer_Object = MibTableColumn
mscAppnRtpIdleTimer = _MscAppnRtpIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 10, 1, 7),
    _MscAppnRtpIdleTimer_Type()
)
mscAppnRtpIdleTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpIdleTimer.setStatus("mandatory")


class _MscAppnRtpMaxBtuSize_Type(Integer32):
    """Custom type mscAppnRtpMaxBtuSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscAppnRtpMaxBtuSize_Type.__name__ = "Integer32"
_MscAppnRtpMaxBtuSize_Object = MibTableColumn
mscAppnRtpMaxBtuSize = _MscAppnRtpMaxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 10, 1, 8),
    _MscAppnRtpMaxBtuSize_Type()
)
mscAppnRtpMaxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpMaxBtuSize.setStatus("mandatory")
_MscAppnRtpStatsTable_Object = MibTable
mscAppnRtpStatsTable = _MscAppnRtpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 11)
)
if mibBuilder.loadTexts:
    mscAppnRtpStatsTable.setStatus("mandatory")
_MscAppnRtpStatsEntry_Object = MibTableRow
mscAppnRtpStatsEntry = _MscAppnRtpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 11, 1)
)
mscAppnRtpStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnRtpIndex"),
)
if mibBuilder.loadTexts:
    mscAppnRtpStatsEntry.setStatus("mandatory")
_MscAppnRtpTxBytes_Type = PassportCounter64
_MscAppnRtpTxBytes_Object = MibTableColumn
mscAppnRtpTxBytes = _MscAppnRtpTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 11, 1, 1),
    _MscAppnRtpTxBytes_Type()
)
mscAppnRtpTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpTxBytes.setStatus("mandatory")
_MscAppnRtpRxBytes_Type = PassportCounter64
_MscAppnRtpRxBytes_Object = MibTableColumn
mscAppnRtpRxBytes = _MscAppnRtpRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 11, 1, 2),
    _MscAppnRtpRxBytes_Type()
)
mscAppnRtpRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpRxBytes.setStatus("mandatory")
_MscAppnRtpBytesResent_Type = PassportCounter64
_MscAppnRtpBytesResent_Object = MibTableColumn
mscAppnRtpBytesResent = _MscAppnRtpBytesResent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 11, 1, 3),
    _MscAppnRtpBytesResent_Type()
)
mscAppnRtpBytesResent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpBytesResent.setStatus("mandatory")
_MscAppnRtpBytesDiscarded_Type = PassportCounter64
_MscAppnRtpBytesDiscarded_Object = MibTableColumn
mscAppnRtpBytesDiscarded = _MscAppnRtpBytesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 11, 1, 4),
    _MscAppnRtpBytesDiscarded_Type()
)
mscAppnRtpBytesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpBytesDiscarded.setStatus("mandatory")
_MscAppnRtpPktTx_Type = PassportCounter64
_MscAppnRtpPktTx_Object = MibTableColumn
mscAppnRtpPktTx = _MscAppnRtpPktTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 11, 1, 5),
    _MscAppnRtpPktTx_Type()
)
mscAppnRtpPktTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpPktTx.setStatus("mandatory")
_MscAppnRtpPktRx_Type = PassportCounter64
_MscAppnRtpPktRx_Object = MibTableColumn
mscAppnRtpPktRx = _MscAppnRtpPktRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 11, 1, 6),
    _MscAppnRtpPktRx_Type()
)
mscAppnRtpPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpPktRx.setStatus("mandatory")
_MscAppnRtpPktResent_Type = PassportCounter64
_MscAppnRtpPktResent_Object = MibTableColumn
mscAppnRtpPktResent = _MscAppnRtpPktResent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 11, 1, 7),
    _MscAppnRtpPktResent_Type()
)
mscAppnRtpPktResent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpPktResent.setStatus("mandatory")
_MscAppnRtpPktDiscard_Type = PassportCounter64
_MscAppnRtpPktDiscard_Object = MibTableColumn
mscAppnRtpPktDiscard = _MscAppnRtpPktDiscard_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 11, 1, 8),
    _MscAppnRtpPktDiscard_Type()
)
mscAppnRtpPktDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpPktDiscard.setStatus("mandatory")
_MscAppnRtpLostFrames_Type = PassportCounter64
_MscAppnRtpLostFrames_Object = MibTableColumn
mscAppnRtpLostFrames = _MscAppnRtpLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 11, 1, 9),
    _MscAppnRtpLostFrames_Type()
)
mscAppnRtpLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpLostFrames.setStatus("mandatory")


class _MscAppnRtpCurTxRate_Type(Gauge32):
    """Custom type mscAppnRtpCurTxRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAppnRtpCurTxRate_Type.__name__ = "Gauge32"
_MscAppnRtpCurTxRate_Object = MibTableColumn
mscAppnRtpCurTxRate = _MscAppnRtpCurTxRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 11, 1, 10),
    _MscAppnRtpCurTxRate_Type()
)
mscAppnRtpCurTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpCurTxRate.setStatus("mandatory")


class _MscAppnRtpMaxTxRate_Type(Gauge32):
    """Custom type mscAppnRtpMaxTxRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAppnRtpMaxTxRate_Type.__name__ = "Gauge32"
_MscAppnRtpMaxTxRate_Object = MibTableColumn
mscAppnRtpMaxTxRate = _MscAppnRtpMaxTxRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 11, 1, 11),
    _MscAppnRtpMaxTxRate_Type()
)
mscAppnRtpMaxTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpMaxTxRate.setStatus("mandatory")


class _MscAppnRtpMinTxRate_Type(Gauge32):
    """Custom type mscAppnRtpMinTxRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAppnRtpMinTxRate_Type.__name__ = "Gauge32"
_MscAppnRtpMinTxRate_Object = MibTableColumn
mscAppnRtpMinTxRate = _MscAppnRtpMinTxRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 11, 1, 12),
    _MscAppnRtpMinTxRate_Type()
)
mscAppnRtpMinTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpMinTxRate.setStatus("mandatory")


class _MscAppnRtpCurRxRate_Type(Gauge32):
    """Custom type mscAppnRtpCurRxRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAppnRtpCurRxRate_Type.__name__ = "Gauge32"
_MscAppnRtpCurRxRate_Object = MibTableColumn
mscAppnRtpCurRxRate = _MscAppnRtpCurRxRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 11, 1, 13),
    _MscAppnRtpCurRxRate_Type()
)
mscAppnRtpCurRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpCurRxRate.setStatus("mandatory")


class _MscAppnRtpMaxRxRate_Type(Gauge32):
    """Custom type mscAppnRtpMaxRxRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAppnRtpMaxRxRate_Type.__name__ = "Gauge32"
_MscAppnRtpMaxRxRate_Object = MibTableColumn
mscAppnRtpMaxRxRate = _MscAppnRtpMaxRxRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 11, 1, 14),
    _MscAppnRtpMaxRxRate_Type()
)
mscAppnRtpMaxRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpMaxRxRate.setStatus("mandatory")


class _MscAppnRtpMinRxRate_Type(Gauge32):
    """Custom type mscAppnRtpMinRxRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAppnRtpMinRxRate_Type.__name__ = "Gauge32"
_MscAppnRtpMinRxRate_Object = MibTableColumn
mscAppnRtpMinRxRate = _MscAppnRtpMinRxRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 11, 1, 15),
    _MscAppnRtpMinRxRate_Type()
)
mscAppnRtpMinRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpMinRxRate.setStatus("mandatory")


class _MscAppnRtpBurstSize_Type(Gauge32):
    """Custom type mscAppnRtpBurstSize based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAppnRtpBurstSize_Type.__name__ = "Gauge32"
_MscAppnRtpBurstSize_Object = MibTableColumn
mscAppnRtpBurstSize = _MscAppnRtpBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 11, 1, 16),
    _MscAppnRtpBurstSize_Type()
)
mscAppnRtpBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpBurstSize.setStatus("mandatory")
_MscAppnRtpUptime_Type = TimeTicks
_MscAppnRtpUptime_Object = MibTableColumn
mscAppnRtpUptime = _MscAppnRtpUptime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 11, 1, 17),
    _MscAppnRtpUptime_Type()
)
mscAppnRtpUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpUptime.setStatus("mandatory")


class _MscAppnRtpSmoothRoundTripTime_Type(Gauge32):
    """Custom type mscAppnRtpSmoothRoundTripTime based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAppnRtpSmoothRoundTripTime_Type.__name__ = "Gauge32"
_MscAppnRtpSmoothRoundTripTime_Object = MibTableColumn
mscAppnRtpSmoothRoundTripTime = _MscAppnRtpSmoothRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 11, 1, 18),
    _MscAppnRtpSmoothRoundTripTime_Type()
)
mscAppnRtpSmoothRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpSmoothRoundTripTime.setStatus("mandatory")


class _MscAppnRtpLastRoundTripTime_Type(Gauge32):
    """Custom type mscAppnRtpLastRoundTripTime based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAppnRtpLastRoundTripTime_Type.__name__ = "Gauge32"
_MscAppnRtpLastRoundTripTime_Object = MibTableColumn
mscAppnRtpLastRoundTripTime = _MscAppnRtpLastRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 11, 1, 19),
    _MscAppnRtpLastRoundTripTime_Type()
)
mscAppnRtpLastRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpLastRoundTripTime.setStatus("mandatory")


class _MscAppnRtpShortReqTimer_Type(Gauge32):
    """Custom type mscAppnRtpShortReqTimer based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAppnRtpShortReqTimer_Type.__name__ = "Gauge32"
_MscAppnRtpShortReqTimer_Object = MibTableColumn
mscAppnRtpShortReqTimer = _MscAppnRtpShortReqTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 11, 1, 20),
    _MscAppnRtpShortReqTimer_Type()
)
mscAppnRtpShortReqTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpShortReqTimer.setStatus("mandatory")
_MscAppnRtpShortReqTimeouts_Type = PassportCounter64
_MscAppnRtpShortReqTimeouts_Object = MibTableColumn
mscAppnRtpShortReqTimeouts = _MscAppnRtpShortReqTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 11, 1, 21),
    _MscAppnRtpShortReqTimeouts_Type()
)
mscAppnRtpShortReqTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpShortReqTimeouts.setStatus("mandatory")
_MscAppnRtpIdleTimeouts_Type = PassportCounter64
_MscAppnRtpIdleTimeouts_Object = MibTableColumn
mscAppnRtpIdleTimeouts = _MscAppnRtpIdleTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 11, 1, 22),
    _MscAppnRtpIdleTimeouts_Type()
)
mscAppnRtpIdleTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpIdleTimeouts.setStatus("mandatory")
_MscAppnRtpRxInvalidSnaFrames_Type = PassportCounter64
_MscAppnRtpRxInvalidSnaFrames_Object = MibTableColumn
mscAppnRtpRxInvalidSnaFrames = _MscAppnRtpRxInvalidSnaFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 11, 1, 23),
    _MscAppnRtpRxInvalidSnaFrames_Type()
)
mscAppnRtpRxInvalidSnaFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpRxInvalidSnaFrames.setStatus("mandatory")
_MscAppnRtpInSessionControlFrames_Type = PassportCounter64
_MscAppnRtpInSessionControlFrames_Object = MibTableColumn
mscAppnRtpInSessionControlFrames = _MscAppnRtpInSessionControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 11, 1, 24),
    _MscAppnRtpInSessionControlFrames_Type()
)
mscAppnRtpInSessionControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpInSessionControlFrames.setStatus("mandatory")
_MscAppnRtpOutSessionControlFrames_Type = PassportCounter64
_MscAppnRtpOutSessionControlFrames_Object = MibTableColumn
mscAppnRtpOutSessionControlFrames = _MscAppnRtpOutSessionControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 13, 11, 1, 25),
    _MscAppnRtpOutSessionControlFrames_Type()
)
mscAppnRtpOutSessionControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnRtpOutSessionControlFrames.setStatus("mandatory")
_MscAppnDlu_ObjectIdentity = ObjectIdentity
mscAppnDlu = _MscAppnDlu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14)
)
_MscAppnDluRowStatusTable_Object = MibTable
mscAppnDluRowStatusTable = _MscAppnDluRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 1)
)
if mibBuilder.loadTexts:
    mscAppnDluRowStatusTable.setStatus("mandatory")
_MscAppnDluRowStatusEntry_Object = MibTableRow
mscAppnDluRowStatusEntry = _MscAppnDluRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 1, 1)
)
mscAppnDluRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDluIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDluRowStatusEntry.setStatus("mandatory")
_MscAppnDluRowStatus_Type = RowStatus
_MscAppnDluRowStatus_Object = MibTableColumn
mscAppnDluRowStatus = _MscAppnDluRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 1, 1, 1),
    _MscAppnDluRowStatus_Type()
)
mscAppnDluRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluRowStatus.setStatus("mandatory")
_MscAppnDluComponentName_Type = DisplayString
_MscAppnDluComponentName_Object = MibTableColumn
mscAppnDluComponentName = _MscAppnDluComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 1, 1, 2),
    _MscAppnDluComponentName_Type()
)
mscAppnDluComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluComponentName.setStatus("mandatory")
_MscAppnDluStorageType_Type = StorageType
_MscAppnDluStorageType_Object = MibTableColumn
mscAppnDluStorageType = _MscAppnDluStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 1, 1, 4),
    _MscAppnDluStorageType_Type()
)
mscAppnDluStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluStorageType.setStatus("mandatory")


class _MscAppnDluIndex_Type(AsciiStringIndex):
    """Custom type mscAppnDluIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MscAppnDluIndex_Type.__name__ = "AsciiStringIndex"
_MscAppnDluIndex_Object = MibTableColumn
mscAppnDluIndex = _MscAppnDluIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 1, 1, 10),
    _MscAppnDluIndex_Type()
)
mscAppnDluIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnDluIndex.setStatus("mandatory")
_MscAppnDluOperTable_Object = MibTable
mscAppnDluOperTable = _MscAppnDluOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 10)
)
if mibBuilder.loadTexts:
    mscAppnDluOperTable.setStatus("mandatory")
_MscAppnDluOperEntry_Object = MibTableRow
mscAppnDluOperEntry = _MscAppnDluOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 10, 1)
)
mscAppnDluOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDluIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDluOperEntry.setStatus("mandatory")


class _MscAppnDluSscpSessActive_Type(Integer32):
    """Custom type mscAppnDluSscpSessActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_MscAppnDluSscpSessActive_Type.__name__ = "Integer32"
_MscAppnDluSscpSessActive_Object = MibTableColumn
mscAppnDluSscpSessActive = _MscAppnDluSscpSessActive_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 10, 1, 1),
    _MscAppnDluSscpSessActive_Type()
)
mscAppnDluSscpSessActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluSscpSessActive.setStatus("mandatory")


class _MscAppnDluPluSessActive_Type(Integer32):
    """Custom type mscAppnDluPluSessActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_MscAppnDluPluSessActive_Type.__name__ = "Integer32"
_MscAppnDluPluSessActive_Object = MibTableColumn
mscAppnDluPluSessActive = _MscAppnDluPluSessActive_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 10, 1, 2),
    _MscAppnDluPluSessActive_Type()
)
mscAppnDluPluSessActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluPluSessActive.setStatus("mandatory")


class _MscAppnDluDlusName_Type(AsciiString):
    """Custom type mscAppnDluDlusName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_MscAppnDluDlusName_Type.__name__ = "AsciiString"
_MscAppnDluDlusName_Object = MibTableColumn
mscAppnDluDlusName = _MscAppnDluDlusName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 10, 1, 3),
    _MscAppnDluDlusName_Type()
)
mscAppnDluDlusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluDlusName.setStatus("mandatory")


class _MscAppnDluPluName_Type(AsciiString):
    """Custom type mscAppnDluPluName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_MscAppnDluPluName_Type.__name__ = "AsciiString"
_MscAppnDluPluName_Object = MibTableColumn
mscAppnDluPluName = _MscAppnDluPluName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 10, 1, 4),
    _MscAppnDluPluName_Type()
)
mscAppnDluPluName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluPluName.setStatus("mandatory")


class _MscAppnDluNauAddress_Type(Integer32):
    """Custom type mscAppnDluNauAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnDluNauAddress_Type.__name__ = "Integer32"
_MscAppnDluNauAddress_Object = MibTableColumn
mscAppnDluNauAddress = _MscAppnDluNauAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 10, 1, 5),
    _MscAppnDluNauAddress_Type()
)
mscAppnDluNauAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluNauAddress.setStatus("mandatory")
_MscAppnDluSscp_ObjectIdentity = ObjectIdentity
mscAppnDluSscp = _MscAppnDluSscp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 100)
)
_MscAppnDluSscpRowStatusTable_Object = MibTable
mscAppnDluSscpRowStatusTable = _MscAppnDluSscpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 100, 1)
)
if mibBuilder.loadTexts:
    mscAppnDluSscpRowStatusTable.setStatus("mandatory")
_MscAppnDluSscpRowStatusEntry_Object = MibTableRow
mscAppnDluSscpRowStatusEntry = _MscAppnDluSscpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 100, 1, 1)
)
mscAppnDluSscpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDluIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDluSscpIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDluSscpRowStatusEntry.setStatus("mandatory")
_MscAppnDluSscpRowStatus_Type = RowStatus
_MscAppnDluSscpRowStatus_Object = MibTableColumn
mscAppnDluSscpRowStatus = _MscAppnDluSscpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 100, 1, 1, 1),
    _MscAppnDluSscpRowStatus_Type()
)
mscAppnDluSscpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluSscpRowStatus.setStatus("mandatory")
_MscAppnDluSscpComponentName_Type = DisplayString
_MscAppnDluSscpComponentName_Object = MibTableColumn
mscAppnDluSscpComponentName = _MscAppnDluSscpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 100, 1, 1, 2),
    _MscAppnDluSscpComponentName_Type()
)
mscAppnDluSscpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluSscpComponentName.setStatus("mandatory")
_MscAppnDluSscpStorageType_Type = StorageType
_MscAppnDluSscpStorageType_Object = MibTableColumn
mscAppnDluSscpStorageType = _MscAppnDluSscpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 100, 1, 1, 4),
    _MscAppnDluSscpStorageType_Type()
)
mscAppnDluSscpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluSscpStorageType.setStatus("mandatory")
_MscAppnDluSscpIndex_Type = NonReplicated
_MscAppnDluSscpIndex_Object = MibTableColumn
mscAppnDluSscpIndex = _MscAppnDluSscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 100, 1, 1, 10),
    _MscAppnDluSscpIndex_Type()
)
mscAppnDluSscpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnDluSscpIndex.setStatus("mandatory")
_MscAppnDluSscpStatsTable_Object = MibTable
mscAppnDluSscpStatsTable = _MscAppnDluSscpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 100, 10)
)
if mibBuilder.loadTexts:
    mscAppnDluSscpStatsTable.setStatus("mandatory")
_MscAppnDluSscpStatsEntry_Object = MibTableRow
mscAppnDluSscpStatsEntry = _MscAppnDluSscpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 100, 10, 1)
)
mscAppnDluSscpStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDluIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDluSscpIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDluSscpStatsEntry.setStatus("mandatory")


class _MscAppnDluSscpRxRuSize_Type(Unsigned32):
    """Custom type mscAppnDluSscpRxRuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnDluSscpRxRuSize_Type.__name__ = "Unsigned32"
_MscAppnDluSscpRxRuSize_Object = MibTableColumn
mscAppnDluSscpRxRuSize = _MscAppnDluSscpRxRuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 100, 10, 1, 1),
    _MscAppnDluSscpRxRuSize_Type()
)
mscAppnDluSscpRxRuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluSscpRxRuSize.setStatus("mandatory")


class _MscAppnDluSscpMaxTxBtuSize_Type(Unsigned32):
    """Custom type mscAppnDluSscpMaxTxBtuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnDluSscpMaxTxBtuSize_Type.__name__ = "Unsigned32"
_MscAppnDluSscpMaxTxBtuSize_Object = MibTableColumn
mscAppnDluSscpMaxTxBtuSize = _MscAppnDluSscpMaxTxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 100, 10, 1, 2),
    _MscAppnDluSscpMaxTxBtuSize_Type()
)
mscAppnDluSscpMaxTxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluSscpMaxTxBtuSize.setStatus("mandatory")


class _MscAppnDluSscpMaxRxBtuSize_Type(Unsigned32):
    """Custom type mscAppnDluSscpMaxRxBtuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnDluSscpMaxRxBtuSize_Type.__name__ = "Unsigned32"
_MscAppnDluSscpMaxRxBtuSize_Object = MibTableColumn
mscAppnDluSscpMaxRxBtuSize = _MscAppnDluSscpMaxRxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 100, 10, 1, 3),
    _MscAppnDluSscpMaxRxBtuSize_Type()
)
mscAppnDluSscpMaxRxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluSscpMaxRxBtuSize.setStatus("mandatory")


class _MscAppnDluSscpMaxTxPacWin_Type(Integer32):
    """Custom type mscAppnDluSscpMaxTxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscAppnDluSscpMaxTxPacWin_Type.__name__ = "Integer32"
_MscAppnDluSscpMaxTxPacWin_Object = MibTableColumn
mscAppnDluSscpMaxTxPacWin = _MscAppnDluSscpMaxTxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 100, 10, 1, 4),
    _MscAppnDluSscpMaxTxPacWin_Type()
)
mscAppnDluSscpMaxTxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluSscpMaxTxPacWin.setStatus("mandatory")


class _MscAppnDluSscpCurTxPacWin_Type(Integer32):
    """Custom type mscAppnDluSscpCurTxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscAppnDluSscpCurTxPacWin_Type.__name__ = "Integer32"
_MscAppnDluSscpCurTxPacWin_Object = MibTableColumn
mscAppnDluSscpCurTxPacWin = _MscAppnDluSscpCurTxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 100, 10, 1, 5),
    _MscAppnDluSscpCurTxPacWin_Type()
)
mscAppnDluSscpCurTxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluSscpCurTxPacWin.setStatus("mandatory")


class _MscAppnDluSscpMaxRxPacWin_Type(Integer32):
    """Custom type mscAppnDluSscpMaxRxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscAppnDluSscpMaxRxPacWin_Type.__name__ = "Integer32"
_MscAppnDluSscpMaxRxPacWin_Object = MibTableColumn
mscAppnDluSscpMaxRxPacWin = _MscAppnDluSscpMaxRxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 100, 10, 1, 6),
    _MscAppnDluSscpMaxRxPacWin_Type()
)
mscAppnDluSscpMaxRxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluSscpMaxRxPacWin.setStatus("mandatory")


class _MscAppnDluSscpCurRxPacWin_Type(Integer32):
    """Custom type mscAppnDluSscpCurRxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscAppnDluSscpCurRxPacWin_Type.__name__ = "Integer32"
_MscAppnDluSscpCurRxPacWin_Object = MibTableColumn
mscAppnDluSscpCurRxPacWin = _MscAppnDluSscpCurRxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 100, 10, 1, 7),
    _MscAppnDluSscpCurRxPacWin_Type()
)
mscAppnDluSscpCurRxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluSscpCurRxPacWin.setStatus("mandatory")
_MscAppnDluSscpTxDataframes_Type = PassportCounter64
_MscAppnDluSscpTxDataframes_Object = MibTableColumn
mscAppnDluSscpTxDataframes = _MscAppnDluSscpTxDataframes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 100, 10, 1, 8),
    _MscAppnDluSscpTxDataframes_Type()
)
mscAppnDluSscpTxDataframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluSscpTxDataframes.setStatus("mandatory")
_MscAppnDluSscpTxFmdFrames_Type = PassportCounter64
_MscAppnDluSscpTxFmdFrames_Object = MibTableColumn
mscAppnDluSscpTxFmdFrames = _MscAppnDluSscpTxFmdFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 100, 10, 1, 9),
    _MscAppnDluSscpTxFmdFrames_Type()
)
mscAppnDluSscpTxFmdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluSscpTxFmdFrames.setStatus("mandatory")
_MscAppnDluSscpTxDataBytes_Type = PassportCounter64
_MscAppnDluSscpTxDataBytes_Object = MibTableColumn
mscAppnDluSscpTxDataBytes = _MscAppnDluSscpTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 100, 10, 1, 10),
    _MscAppnDluSscpTxDataBytes_Type()
)
mscAppnDluSscpTxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluSscpTxDataBytes.setStatus("mandatory")
_MscAppnDluSscpRxDataFrames_Type = PassportCounter64
_MscAppnDluSscpRxDataFrames_Object = MibTableColumn
mscAppnDluSscpRxDataFrames = _MscAppnDluSscpRxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 100, 10, 1, 11),
    _MscAppnDluSscpRxDataFrames_Type()
)
mscAppnDluSscpRxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluSscpRxDataFrames.setStatus("mandatory")
_MscAppnDluSscpRxFmdFrames_Type = PassportCounter64
_MscAppnDluSscpRxFmdFrames_Object = MibTableColumn
mscAppnDluSscpRxFmdFrames = _MscAppnDluSscpRxFmdFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 100, 10, 1, 12),
    _MscAppnDluSscpRxFmdFrames_Type()
)
mscAppnDluSscpRxFmdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluSscpRxFmdFrames.setStatus("mandatory")
_MscAppnDluSscpRxDataBytes_Type = PassportCounter64
_MscAppnDluSscpRxDataBytes_Object = MibTableColumn
mscAppnDluSscpRxDataBytes = _MscAppnDluSscpRxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 100, 10, 1, 13),
    _MscAppnDluSscpRxDataBytes_Type()
)
mscAppnDluSscpRxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluSscpRxDataBytes.setStatus("mandatory")


class _MscAppnDluSscpSidh_Type(Hex):
    """Custom type mscAppnDluSscpSidh based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnDluSscpSidh_Type.__name__ = "Hex"
_MscAppnDluSscpSidh_Object = MibTableColumn
mscAppnDluSscpSidh = _MscAppnDluSscpSidh_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 100, 10, 1, 14),
    _MscAppnDluSscpSidh_Type()
)
mscAppnDluSscpSidh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluSscpSidh.setStatus("mandatory")


class _MscAppnDluSscpSidl_Type(Hex):
    """Custom type mscAppnDluSscpSidl based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnDluSscpSidl_Type.__name__ = "Hex"
_MscAppnDluSscpSidl_Object = MibTableColumn
mscAppnDluSscpSidl = _MscAppnDluSscpSidl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 100, 10, 1, 15),
    _MscAppnDluSscpSidl_Type()
)
mscAppnDluSscpSidl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluSscpSidl.setStatus("mandatory")


class _MscAppnDluSscpOdai_Type(Integer32):
    """Custom type mscAppnDluSscpOdai based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("primary", 0),
          ("secondary", 1))
    )


_MscAppnDluSscpOdai_Type.__name__ = "Integer32"
_MscAppnDluSscpOdai_Object = MibTableColumn
mscAppnDluSscpOdai = _MscAppnDluSscpOdai_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 100, 10, 1, 16),
    _MscAppnDluSscpOdai_Type()
)
mscAppnDluSscpOdai.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluSscpOdai.setStatus("mandatory")


class _MscAppnDluSscpLsName_Type(AsciiString):
    """Custom type mscAppnDluSscpLsName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MscAppnDluSscpLsName_Type.__name__ = "AsciiString"
_MscAppnDluSscpLsName_Object = MibTableColumn
mscAppnDluSscpLsName = _MscAppnDluSscpLsName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 100, 10, 1, 17),
    _MscAppnDluSscpLsName_Type()
)
mscAppnDluSscpLsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluSscpLsName.setStatus("mandatory")
_MscAppnDluUsStat_ObjectIdentity = ObjectIdentity
mscAppnDluUsStat = _MscAppnDluUsStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 101)
)
_MscAppnDluUsStatRowStatusTable_Object = MibTable
mscAppnDluUsStatRowStatusTable = _MscAppnDluUsStatRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 101, 1)
)
if mibBuilder.loadTexts:
    mscAppnDluUsStatRowStatusTable.setStatus("mandatory")
_MscAppnDluUsStatRowStatusEntry_Object = MibTableRow
mscAppnDluUsStatRowStatusEntry = _MscAppnDluUsStatRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 101, 1, 1)
)
mscAppnDluUsStatRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDluIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDluUsStatIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDluUsStatRowStatusEntry.setStatus("mandatory")
_MscAppnDluUsStatRowStatus_Type = RowStatus
_MscAppnDluUsStatRowStatus_Object = MibTableColumn
mscAppnDluUsStatRowStatus = _MscAppnDluUsStatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 101, 1, 1, 1),
    _MscAppnDluUsStatRowStatus_Type()
)
mscAppnDluUsStatRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluUsStatRowStatus.setStatus("mandatory")
_MscAppnDluUsStatComponentName_Type = DisplayString
_MscAppnDluUsStatComponentName_Object = MibTableColumn
mscAppnDluUsStatComponentName = _MscAppnDluUsStatComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 101, 1, 1, 2),
    _MscAppnDluUsStatComponentName_Type()
)
mscAppnDluUsStatComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluUsStatComponentName.setStatus("mandatory")
_MscAppnDluUsStatStorageType_Type = StorageType
_MscAppnDluUsStatStorageType_Object = MibTableColumn
mscAppnDluUsStatStorageType = _MscAppnDluUsStatStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 101, 1, 1, 4),
    _MscAppnDluUsStatStorageType_Type()
)
mscAppnDluUsStatStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluUsStatStorageType.setStatus("mandatory")
_MscAppnDluUsStatIndex_Type = NonReplicated
_MscAppnDluUsStatIndex_Object = MibTableColumn
mscAppnDluUsStatIndex = _MscAppnDluUsStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 101, 1, 1, 10),
    _MscAppnDluUsStatIndex_Type()
)
mscAppnDluUsStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnDluUsStatIndex.setStatus("mandatory")
_MscAppnDluUsStatStatsTable_Object = MibTable
mscAppnDluUsStatStatsTable = _MscAppnDluUsStatStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 101, 10)
)
if mibBuilder.loadTexts:
    mscAppnDluUsStatStatsTable.setStatus("mandatory")
_MscAppnDluUsStatStatsEntry_Object = MibTableRow
mscAppnDluUsStatStatsEntry = _MscAppnDluUsStatStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 101, 10, 1)
)
mscAppnDluUsStatStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDluIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDluUsStatIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDluUsStatStatsEntry.setStatus("mandatory")


class _MscAppnDluUsStatRxRuSize_Type(Unsigned32):
    """Custom type mscAppnDluUsStatRxRuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnDluUsStatRxRuSize_Type.__name__ = "Unsigned32"
_MscAppnDluUsStatRxRuSize_Object = MibTableColumn
mscAppnDluUsStatRxRuSize = _MscAppnDluUsStatRxRuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 101, 10, 1, 1),
    _MscAppnDluUsStatRxRuSize_Type()
)
mscAppnDluUsStatRxRuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluUsStatRxRuSize.setStatus("mandatory")


class _MscAppnDluUsStatMaxTxBtuSize_Type(Unsigned32):
    """Custom type mscAppnDluUsStatMaxTxBtuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnDluUsStatMaxTxBtuSize_Type.__name__ = "Unsigned32"
_MscAppnDluUsStatMaxTxBtuSize_Object = MibTableColumn
mscAppnDluUsStatMaxTxBtuSize = _MscAppnDluUsStatMaxTxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 101, 10, 1, 2),
    _MscAppnDluUsStatMaxTxBtuSize_Type()
)
mscAppnDluUsStatMaxTxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluUsStatMaxTxBtuSize.setStatus("mandatory")


class _MscAppnDluUsStatMaxRxBtuSize_Type(Unsigned32):
    """Custom type mscAppnDluUsStatMaxRxBtuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnDluUsStatMaxRxBtuSize_Type.__name__ = "Unsigned32"
_MscAppnDluUsStatMaxRxBtuSize_Object = MibTableColumn
mscAppnDluUsStatMaxRxBtuSize = _MscAppnDluUsStatMaxRxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 101, 10, 1, 3),
    _MscAppnDluUsStatMaxRxBtuSize_Type()
)
mscAppnDluUsStatMaxRxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluUsStatMaxRxBtuSize.setStatus("mandatory")


class _MscAppnDluUsStatMaxTxPacWin_Type(Integer32):
    """Custom type mscAppnDluUsStatMaxTxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscAppnDluUsStatMaxTxPacWin_Type.__name__ = "Integer32"
_MscAppnDluUsStatMaxTxPacWin_Object = MibTableColumn
mscAppnDluUsStatMaxTxPacWin = _MscAppnDluUsStatMaxTxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 101, 10, 1, 4),
    _MscAppnDluUsStatMaxTxPacWin_Type()
)
mscAppnDluUsStatMaxTxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluUsStatMaxTxPacWin.setStatus("mandatory")


class _MscAppnDluUsStatCurTxPacWin_Type(Integer32):
    """Custom type mscAppnDluUsStatCurTxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscAppnDluUsStatCurTxPacWin_Type.__name__ = "Integer32"
_MscAppnDluUsStatCurTxPacWin_Object = MibTableColumn
mscAppnDluUsStatCurTxPacWin = _MscAppnDluUsStatCurTxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 101, 10, 1, 5),
    _MscAppnDluUsStatCurTxPacWin_Type()
)
mscAppnDluUsStatCurTxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluUsStatCurTxPacWin.setStatus("mandatory")


class _MscAppnDluUsStatMaxRxPacWin_Type(Integer32):
    """Custom type mscAppnDluUsStatMaxRxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscAppnDluUsStatMaxRxPacWin_Type.__name__ = "Integer32"
_MscAppnDluUsStatMaxRxPacWin_Object = MibTableColumn
mscAppnDluUsStatMaxRxPacWin = _MscAppnDluUsStatMaxRxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 101, 10, 1, 6),
    _MscAppnDluUsStatMaxRxPacWin_Type()
)
mscAppnDluUsStatMaxRxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluUsStatMaxRxPacWin.setStatus("mandatory")


class _MscAppnDluUsStatCurRxPacWin_Type(Integer32):
    """Custom type mscAppnDluUsStatCurRxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscAppnDluUsStatCurRxPacWin_Type.__name__ = "Integer32"
_MscAppnDluUsStatCurRxPacWin_Object = MibTableColumn
mscAppnDluUsStatCurRxPacWin = _MscAppnDluUsStatCurRxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 101, 10, 1, 7),
    _MscAppnDluUsStatCurRxPacWin_Type()
)
mscAppnDluUsStatCurRxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluUsStatCurRxPacWin.setStatus("mandatory")
_MscAppnDluUsStatTxDataframes_Type = PassportCounter64
_MscAppnDluUsStatTxDataframes_Object = MibTableColumn
mscAppnDluUsStatTxDataframes = _MscAppnDluUsStatTxDataframes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 101, 10, 1, 8),
    _MscAppnDluUsStatTxDataframes_Type()
)
mscAppnDluUsStatTxDataframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluUsStatTxDataframes.setStatus("mandatory")
_MscAppnDluUsStatTxFmdFrames_Type = PassportCounter64
_MscAppnDluUsStatTxFmdFrames_Object = MibTableColumn
mscAppnDluUsStatTxFmdFrames = _MscAppnDluUsStatTxFmdFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 101, 10, 1, 9),
    _MscAppnDluUsStatTxFmdFrames_Type()
)
mscAppnDluUsStatTxFmdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluUsStatTxFmdFrames.setStatus("mandatory")
_MscAppnDluUsStatTxDataBytes_Type = PassportCounter64
_MscAppnDluUsStatTxDataBytes_Object = MibTableColumn
mscAppnDluUsStatTxDataBytes = _MscAppnDluUsStatTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 101, 10, 1, 10),
    _MscAppnDluUsStatTxDataBytes_Type()
)
mscAppnDluUsStatTxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluUsStatTxDataBytes.setStatus("mandatory")
_MscAppnDluUsStatRxDataFrames_Type = PassportCounter64
_MscAppnDluUsStatRxDataFrames_Object = MibTableColumn
mscAppnDluUsStatRxDataFrames = _MscAppnDluUsStatRxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 101, 10, 1, 11),
    _MscAppnDluUsStatRxDataFrames_Type()
)
mscAppnDluUsStatRxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluUsStatRxDataFrames.setStatus("mandatory")
_MscAppnDluUsStatRxFmdFrames_Type = PassportCounter64
_MscAppnDluUsStatRxFmdFrames_Object = MibTableColumn
mscAppnDluUsStatRxFmdFrames = _MscAppnDluUsStatRxFmdFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 101, 10, 1, 12),
    _MscAppnDluUsStatRxFmdFrames_Type()
)
mscAppnDluUsStatRxFmdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluUsStatRxFmdFrames.setStatus("mandatory")
_MscAppnDluUsStatRxDataBytes_Type = PassportCounter64
_MscAppnDluUsStatRxDataBytes_Object = MibTableColumn
mscAppnDluUsStatRxDataBytes = _MscAppnDluUsStatRxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 101, 10, 1, 13),
    _MscAppnDluUsStatRxDataBytes_Type()
)
mscAppnDluUsStatRxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluUsStatRxDataBytes.setStatus("mandatory")


class _MscAppnDluUsStatSidh_Type(Hex):
    """Custom type mscAppnDluUsStatSidh based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnDluUsStatSidh_Type.__name__ = "Hex"
_MscAppnDluUsStatSidh_Object = MibTableColumn
mscAppnDluUsStatSidh = _MscAppnDluUsStatSidh_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 101, 10, 1, 14),
    _MscAppnDluUsStatSidh_Type()
)
mscAppnDluUsStatSidh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluUsStatSidh.setStatus("mandatory")


class _MscAppnDluUsStatSidl_Type(Hex):
    """Custom type mscAppnDluUsStatSidl based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnDluUsStatSidl_Type.__name__ = "Hex"
_MscAppnDluUsStatSidl_Object = MibTableColumn
mscAppnDluUsStatSidl = _MscAppnDluUsStatSidl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 101, 10, 1, 15),
    _MscAppnDluUsStatSidl_Type()
)
mscAppnDluUsStatSidl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluUsStatSidl.setStatus("mandatory")


class _MscAppnDluUsStatOdai_Type(Integer32):
    """Custom type mscAppnDluUsStatOdai based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("primary", 0),
          ("secondary", 1))
    )


_MscAppnDluUsStatOdai_Type.__name__ = "Integer32"
_MscAppnDluUsStatOdai_Object = MibTableColumn
mscAppnDluUsStatOdai = _MscAppnDluUsStatOdai_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 101, 10, 1, 16),
    _MscAppnDluUsStatOdai_Type()
)
mscAppnDluUsStatOdai.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluUsStatOdai.setStatus("mandatory")


class _MscAppnDluUsStatLsName_Type(AsciiString):
    """Custom type mscAppnDluUsStatLsName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MscAppnDluUsStatLsName_Type.__name__ = "AsciiString"
_MscAppnDluUsStatLsName_Object = MibTableColumn
mscAppnDluUsStatLsName = _MscAppnDluUsStatLsName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 101, 10, 1, 17),
    _MscAppnDluUsStatLsName_Type()
)
mscAppnDluUsStatLsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluUsStatLsName.setStatus("mandatory")
_MscAppnDluDsStat_ObjectIdentity = ObjectIdentity
mscAppnDluDsStat = _MscAppnDluDsStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 102)
)
_MscAppnDluDsStatRowStatusTable_Object = MibTable
mscAppnDluDsStatRowStatusTable = _MscAppnDluDsStatRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 102, 1)
)
if mibBuilder.loadTexts:
    mscAppnDluDsStatRowStatusTable.setStatus("mandatory")
_MscAppnDluDsStatRowStatusEntry_Object = MibTableRow
mscAppnDluDsStatRowStatusEntry = _MscAppnDluDsStatRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 102, 1, 1)
)
mscAppnDluDsStatRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDluIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDluDsStatIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDluDsStatRowStatusEntry.setStatus("mandatory")
_MscAppnDluDsStatRowStatus_Type = RowStatus
_MscAppnDluDsStatRowStatus_Object = MibTableColumn
mscAppnDluDsStatRowStatus = _MscAppnDluDsStatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 102, 1, 1, 1),
    _MscAppnDluDsStatRowStatus_Type()
)
mscAppnDluDsStatRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluDsStatRowStatus.setStatus("mandatory")
_MscAppnDluDsStatComponentName_Type = DisplayString
_MscAppnDluDsStatComponentName_Object = MibTableColumn
mscAppnDluDsStatComponentName = _MscAppnDluDsStatComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 102, 1, 1, 2),
    _MscAppnDluDsStatComponentName_Type()
)
mscAppnDluDsStatComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluDsStatComponentName.setStatus("mandatory")
_MscAppnDluDsStatStorageType_Type = StorageType
_MscAppnDluDsStatStorageType_Object = MibTableColumn
mscAppnDluDsStatStorageType = _MscAppnDluDsStatStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 102, 1, 1, 4),
    _MscAppnDluDsStatStorageType_Type()
)
mscAppnDluDsStatStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluDsStatStorageType.setStatus("mandatory")
_MscAppnDluDsStatIndex_Type = NonReplicated
_MscAppnDluDsStatIndex_Object = MibTableColumn
mscAppnDluDsStatIndex = _MscAppnDluDsStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 102, 1, 1, 10),
    _MscAppnDluDsStatIndex_Type()
)
mscAppnDluDsStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnDluDsStatIndex.setStatus("mandatory")
_MscAppnDluDsStatStatsTable_Object = MibTable
mscAppnDluDsStatStatsTable = _MscAppnDluDsStatStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 102, 10)
)
if mibBuilder.loadTexts:
    mscAppnDluDsStatStatsTable.setStatus("mandatory")
_MscAppnDluDsStatStatsEntry_Object = MibTableRow
mscAppnDluDsStatStatsEntry = _MscAppnDluDsStatStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 102, 10, 1)
)
mscAppnDluDsStatStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDluIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDluDsStatIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDluDsStatStatsEntry.setStatus("mandatory")


class _MscAppnDluDsStatRxRuSize_Type(Unsigned32):
    """Custom type mscAppnDluDsStatRxRuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnDluDsStatRxRuSize_Type.__name__ = "Unsigned32"
_MscAppnDluDsStatRxRuSize_Object = MibTableColumn
mscAppnDluDsStatRxRuSize = _MscAppnDluDsStatRxRuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 102, 10, 1, 1),
    _MscAppnDluDsStatRxRuSize_Type()
)
mscAppnDluDsStatRxRuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluDsStatRxRuSize.setStatus("mandatory")


class _MscAppnDluDsStatMaxTxBtuSize_Type(Unsigned32):
    """Custom type mscAppnDluDsStatMaxTxBtuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnDluDsStatMaxTxBtuSize_Type.__name__ = "Unsigned32"
_MscAppnDluDsStatMaxTxBtuSize_Object = MibTableColumn
mscAppnDluDsStatMaxTxBtuSize = _MscAppnDluDsStatMaxTxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 102, 10, 1, 2),
    _MscAppnDluDsStatMaxTxBtuSize_Type()
)
mscAppnDluDsStatMaxTxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluDsStatMaxTxBtuSize.setStatus("mandatory")


class _MscAppnDluDsStatMaxRxBtuSize_Type(Unsigned32):
    """Custom type mscAppnDluDsStatMaxRxBtuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnDluDsStatMaxRxBtuSize_Type.__name__ = "Unsigned32"
_MscAppnDluDsStatMaxRxBtuSize_Object = MibTableColumn
mscAppnDluDsStatMaxRxBtuSize = _MscAppnDluDsStatMaxRxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 102, 10, 1, 3),
    _MscAppnDluDsStatMaxRxBtuSize_Type()
)
mscAppnDluDsStatMaxRxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluDsStatMaxRxBtuSize.setStatus("mandatory")


class _MscAppnDluDsStatMaxTxPacWin_Type(Integer32):
    """Custom type mscAppnDluDsStatMaxTxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscAppnDluDsStatMaxTxPacWin_Type.__name__ = "Integer32"
_MscAppnDluDsStatMaxTxPacWin_Object = MibTableColumn
mscAppnDluDsStatMaxTxPacWin = _MscAppnDluDsStatMaxTxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 102, 10, 1, 4),
    _MscAppnDluDsStatMaxTxPacWin_Type()
)
mscAppnDluDsStatMaxTxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluDsStatMaxTxPacWin.setStatus("mandatory")


class _MscAppnDluDsStatCurTxPacWin_Type(Integer32):
    """Custom type mscAppnDluDsStatCurTxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscAppnDluDsStatCurTxPacWin_Type.__name__ = "Integer32"
_MscAppnDluDsStatCurTxPacWin_Object = MibTableColumn
mscAppnDluDsStatCurTxPacWin = _MscAppnDluDsStatCurTxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 102, 10, 1, 5),
    _MscAppnDluDsStatCurTxPacWin_Type()
)
mscAppnDluDsStatCurTxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluDsStatCurTxPacWin.setStatus("mandatory")


class _MscAppnDluDsStatMaxRxPacWin_Type(Integer32):
    """Custom type mscAppnDluDsStatMaxRxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscAppnDluDsStatMaxRxPacWin_Type.__name__ = "Integer32"
_MscAppnDluDsStatMaxRxPacWin_Object = MibTableColumn
mscAppnDluDsStatMaxRxPacWin = _MscAppnDluDsStatMaxRxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 102, 10, 1, 6),
    _MscAppnDluDsStatMaxRxPacWin_Type()
)
mscAppnDluDsStatMaxRxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluDsStatMaxRxPacWin.setStatus("mandatory")


class _MscAppnDluDsStatCurRxPacWin_Type(Integer32):
    """Custom type mscAppnDluDsStatCurRxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscAppnDluDsStatCurRxPacWin_Type.__name__ = "Integer32"
_MscAppnDluDsStatCurRxPacWin_Object = MibTableColumn
mscAppnDluDsStatCurRxPacWin = _MscAppnDluDsStatCurRxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 102, 10, 1, 7),
    _MscAppnDluDsStatCurRxPacWin_Type()
)
mscAppnDluDsStatCurRxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluDsStatCurRxPacWin.setStatus("mandatory")
_MscAppnDluDsStatTxDataframes_Type = PassportCounter64
_MscAppnDluDsStatTxDataframes_Object = MibTableColumn
mscAppnDluDsStatTxDataframes = _MscAppnDluDsStatTxDataframes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 102, 10, 1, 8),
    _MscAppnDluDsStatTxDataframes_Type()
)
mscAppnDluDsStatTxDataframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluDsStatTxDataframes.setStatus("mandatory")
_MscAppnDluDsStatTxFmdFrames_Type = PassportCounter64
_MscAppnDluDsStatTxFmdFrames_Object = MibTableColumn
mscAppnDluDsStatTxFmdFrames = _MscAppnDluDsStatTxFmdFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 102, 10, 1, 9),
    _MscAppnDluDsStatTxFmdFrames_Type()
)
mscAppnDluDsStatTxFmdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluDsStatTxFmdFrames.setStatus("mandatory")
_MscAppnDluDsStatTxDataBytes_Type = PassportCounter64
_MscAppnDluDsStatTxDataBytes_Object = MibTableColumn
mscAppnDluDsStatTxDataBytes = _MscAppnDluDsStatTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 102, 10, 1, 10),
    _MscAppnDluDsStatTxDataBytes_Type()
)
mscAppnDluDsStatTxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluDsStatTxDataBytes.setStatus("mandatory")
_MscAppnDluDsStatRxDataFrames_Type = PassportCounter64
_MscAppnDluDsStatRxDataFrames_Object = MibTableColumn
mscAppnDluDsStatRxDataFrames = _MscAppnDluDsStatRxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 102, 10, 1, 11),
    _MscAppnDluDsStatRxDataFrames_Type()
)
mscAppnDluDsStatRxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluDsStatRxDataFrames.setStatus("mandatory")
_MscAppnDluDsStatRxFmdFrames_Type = PassportCounter64
_MscAppnDluDsStatRxFmdFrames_Object = MibTableColumn
mscAppnDluDsStatRxFmdFrames = _MscAppnDluDsStatRxFmdFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 102, 10, 1, 12),
    _MscAppnDluDsStatRxFmdFrames_Type()
)
mscAppnDluDsStatRxFmdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluDsStatRxFmdFrames.setStatus("mandatory")
_MscAppnDluDsStatRxDataBytes_Type = PassportCounter64
_MscAppnDluDsStatRxDataBytes_Object = MibTableColumn
mscAppnDluDsStatRxDataBytes = _MscAppnDluDsStatRxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 102, 10, 1, 13),
    _MscAppnDluDsStatRxDataBytes_Type()
)
mscAppnDluDsStatRxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluDsStatRxDataBytes.setStatus("mandatory")


class _MscAppnDluDsStatSidh_Type(Hex):
    """Custom type mscAppnDluDsStatSidh based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnDluDsStatSidh_Type.__name__ = "Hex"
_MscAppnDluDsStatSidh_Object = MibTableColumn
mscAppnDluDsStatSidh = _MscAppnDluDsStatSidh_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 102, 10, 1, 14),
    _MscAppnDluDsStatSidh_Type()
)
mscAppnDluDsStatSidh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluDsStatSidh.setStatus("mandatory")


class _MscAppnDluDsStatSidl_Type(Hex):
    """Custom type mscAppnDluDsStatSidl based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnDluDsStatSidl_Type.__name__ = "Hex"
_MscAppnDluDsStatSidl_Object = MibTableColumn
mscAppnDluDsStatSidl = _MscAppnDluDsStatSidl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 102, 10, 1, 15),
    _MscAppnDluDsStatSidl_Type()
)
mscAppnDluDsStatSidl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluDsStatSidl.setStatus("mandatory")


class _MscAppnDluDsStatOdai_Type(Integer32):
    """Custom type mscAppnDluDsStatOdai based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("primary", 0),
          ("secondary", 1))
    )


_MscAppnDluDsStatOdai_Type.__name__ = "Integer32"
_MscAppnDluDsStatOdai_Object = MibTableColumn
mscAppnDluDsStatOdai = _MscAppnDluDsStatOdai_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 102, 10, 1, 16),
    _MscAppnDluDsStatOdai_Type()
)
mscAppnDluDsStatOdai.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluDsStatOdai.setStatus("mandatory")


class _MscAppnDluDsStatLsName_Type(AsciiString):
    """Custom type mscAppnDluDsStatLsName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MscAppnDluDsStatLsName_Type.__name__ = "AsciiString"
_MscAppnDluDsStatLsName_Object = MibTableColumn
mscAppnDluDsStatLsName = _MscAppnDluDsStatLsName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 14, 102, 10, 1, 17),
    _MscAppnDluDsStatLsName_Type()
)
mscAppnDluDsStatLsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDluDsStatLsName.setStatus("mandatory")
_MscAppnDlus_ObjectIdentity = ObjectIdentity
mscAppnDlus = _MscAppnDlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 15)
)
_MscAppnDlusRowStatusTable_Object = MibTable
mscAppnDlusRowStatusTable = _MscAppnDlusRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 15, 1)
)
if mibBuilder.loadTexts:
    mscAppnDlusRowStatusTable.setStatus("mandatory")
_MscAppnDlusRowStatusEntry_Object = MibTableRow
mscAppnDlusRowStatusEntry = _MscAppnDlusRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 15, 1, 1)
)
mscAppnDlusRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlusIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDlusRowStatusEntry.setStatus("mandatory")
_MscAppnDlusRowStatus_Type = RowStatus
_MscAppnDlusRowStatus_Object = MibTableColumn
mscAppnDlusRowStatus = _MscAppnDlusRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 15, 1, 1, 1),
    _MscAppnDlusRowStatus_Type()
)
mscAppnDlusRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlusRowStatus.setStatus("mandatory")
_MscAppnDlusComponentName_Type = DisplayString
_MscAppnDlusComponentName_Object = MibTableColumn
mscAppnDlusComponentName = _MscAppnDlusComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 15, 1, 1, 2),
    _MscAppnDlusComponentName_Type()
)
mscAppnDlusComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlusComponentName.setStatus("mandatory")
_MscAppnDlusStorageType_Type = StorageType
_MscAppnDlusStorageType_Object = MibTableColumn
mscAppnDlusStorageType = _MscAppnDlusStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 15, 1, 1, 4),
    _MscAppnDlusStorageType_Type()
)
mscAppnDlusStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlusStorageType.setStatus("mandatory")


class _MscAppnDlusIndex_Type(AsciiStringIndex):
    """Custom type mscAppnDlusIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_MscAppnDlusIndex_Type.__name__ = "AsciiStringIndex"
_MscAppnDlusIndex_Object = MibTableColumn
mscAppnDlusIndex = _MscAppnDlusIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 15, 1, 1, 10),
    _MscAppnDlusIndex_Type()
)
mscAppnDlusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnDlusIndex.setStatus("mandatory")
_MscAppnDlusOperTable_Object = MibTable
mscAppnDlusOperTable = _MscAppnDlusOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 15, 10)
)
if mibBuilder.loadTexts:
    mscAppnDlusOperTable.setStatus("mandatory")
_MscAppnDlusOperEntry_Object = MibTableRow
mscAppnDlusOperEntry = _MscAppnDlusOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 15, 10, 1)
)
mscAppnDlusOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlusIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDlusOperEntry.setStatus("mandatory")


class _MscAppnDlusPrimaryDlus_Type(Integer32):
    """Custom type mscAppnDlusPrimaryDlus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MscAppnDlusPrimaryDlus_Type.__name__ = "Integer32"
_MscAppnDlusPrimaryDlus_Object = MibTableColumn
mscAppnDlusPrimaryDlus = _MscAppnDlusPrimaryDlus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 15, 10, 1, 1),
    _MscAppnDlusPrimaryDlus_Type()
)
mscAppnDlusPrimaryDlus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlusPrimaryDlus.setStatus("mandatory")


class _MscAppnDlusPipeState_Type(Integer32):
    """Custom type mscAppnDlusPipeState based on Integer32"""
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
        *(("active", 2),
          ("inactive", 0),
          ("pendingActive", 1),
          ("pendingInactive", 3))
    )


_MscAppnDlusPipeState_Type.__name__ = "Integer32"
_MscAppnDlusPipeState_Object = MibTableColumn
mscAppnDlusPipeState = _MscAppnDlusPipeState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 15, 10, 1, 2),
    _MscAppnDlusPipeState_Type()
)
mscAppnDlusPipeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlusPipeState.setStatus("mandatory")


class _MscAppnDlusActivePUs_Type(Gauge32):
    """Custom type mscAppnDlusActivePUs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscAppnDlusActivePUs_Type.__name__ = "Gauge32"
_MscAppnDlusActivePUs_Object = MibTableColumn
mscAppnDlusActivePUs = _MscAppnDlusActivePUs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 15, 10, 1, 3),
    _MscAppnDlusActivePUs_Type()
)
mscAppnDlusActivePUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlusActivePUs.setStatus("mandatory")
_MscAppnDlusDlusStatTable_Object = MibTable
mscAppnDlusDlusStatTable = _MscAppnDlusDlusStatTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 15, 11)
)
if mibBuilder.loadTexts:
    mscAppnDlusDlusStatTable.setStatus("mandatory")
_MscAppnDlusDlusStatEntry_Object = MibTableRow
mscAppnDlusDlusStatEntry = _MscAppnDlusDlusStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 15, 11, 1)
)
mscAppnDlusDlusStatEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDlusIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDlusDlusStatEntry.setStatus("mandatory")
_MscAppnDlusReqActPuTx_Type = PassportCounter64
_MscAppnDlusReqActPuTx_Object = MibTableColumn
mscAppnDlusReqActPuTx = _MscAppnDlusReqActPuTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 15, 11, 1, 1),
    _MscAppnDlusReqActPuTx_Type()
)
mscAppnDlusReqActPuTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlusReqActPuTx.setStatus("mandatory")
_MscAppnDlusReqActPuRspRx_Type = PassportCounter64
_MscAppnDlusReqActPuRspRx_Object = MibTableColumn
mscAppnDlusReqActPuRspRx = _MscAppnDlusReqActPuRspRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 15, 11, 1, 2),
    _MscAppnDlusReqActPuRspRx_Type()
)
mscAppnDlusReqActPuRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlusReqActPuRspRx.setStatus("mandatory")
_MscAppnDlusActPuRx_Type = PassportCounter64
_MscAppnDlusActPuRx_Object = MibTableColumn
mscAppnDlusActPuRx = _MscAppnDlusActPuRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 15, 11, 1, 3),
    _MscAppnDlusActPuRx_Type()
)
mscAppnDlusActPuRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlusActPuRx.setStatus("mandatory")
_MscAppnDlusActPuRspTx_Type = PassportCounter64
_MscAppnDlusActPuRspTx_Object = MibTableColumn
mscAppnDlusActPuRspTx = _MscAppnDlusActPuRspTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 15, 11, 1, 4),
    _MscAppnDlusActPuRspTx_Type()
)
mscAppnDlusActPuRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlusActPuRspTx.setStatus("mandatory")
_MscAppnDlusReqDactPuTx_Type = PassportCounter64
_MscAppnDlusReqDactPuTx_Object = MibTableColumn
mscAppnDlusReqDactPuTx = _MscAppnDlusReqDactPuTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 15, 11, 1, 5),
    _MscAppnDlusReqDactPuTx_Type()
)
mscAppnDlusReqDactPuTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlusReqDactPuTx.setStatus("mandatory")
_MscAppnDlusReqDactPuRspRx_Type = PassportCounter64
_MscAppnDlusReqDactPuRspRx_Object = MibTableColumn
mscAppnDlusReqDactPuRspRx = _MscAppnDlusReqDactPuRspRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 15, 11, 1, 6),
    _MscAppnDlusReqDactPuRspRx_Type()
)
mscAppnDlusReqDactPuRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlusReqDactPuRspRx.setStatus("mandatory")
_MscAppnDlusDactPuRx_Type = PassportCounter64
_MscAppnDlusDactPuRx_Object = MibTableColumn
mscAppnDlusDactPuRx = _MscAppnDlusDactPuRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 15, 11, 1, 7),
    _MscAppnDlusDactPuRx_Type()
)
mscAppnDlusDactPuRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlusDactPuRx.setStatus("mandatory")
_MscAppnDlusDactPuRspTx_Type = PassportCounter64
_MscAppnDlusDactPuRspTx_Object = MibTableColumn
mscAppnDlusDactPuRspTx = _MscAppnDlusDactPuRspTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 15, 11, 1, 8),
    _MscAppnDlusDactPuRspTx_Type()
)
mscAppnDlusDactPuRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlusDactPuRspTx.setStatus("mandatory")
_MscAppnDlusActLuRx_Type = PassportCounter64
_MscAppnDlusActLuRx_Object = MibTableColumn
mscAppnDlusActLuRx = _MscAppnDlusActLuRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 15, 11, 1, 9),
    _MscAppnDlusActLuRx_Type()
)
mscAppnDlusActLuRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlusActLuRx.setStatus("mandatory")
_MscAppnDlusActLuRspTx_Type = PassportCounter64
_MscAppnDlusActLuRspTx_Object = MibTableColumn
mscAppnDlusActLuRspTx = _MscAppnDlusActLuRspTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 15, 11, 1, 10),
    _MscAppnDlusActLuRspTx_Type()
)
mscAppnDlusActLuRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlusActLuRspTx.setStatus("mandatory")
_MscAppnDlusDactLuRx_Type = PassportCounter64
_MscAppnDlusDactLuRx_Object = MibTableColumn
mscAppnDlusDactLuRx = _MscAppnDlusDactLuRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 15, 11, 1, 11),
    _MscAppnDlusDactLuRx_Type()
)
mscAppnDlusDactLuRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlusDactLuRx.setStatus("mandatory")
_MscAppnDlusDactLuRspTx_Type = PassportCounter64
_MscAppnDlusDactLuRspTx_Object = MibTableColumn
mscAppnDlusDactLuRspTx = _MscAppnDlusDactLuRspTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 15, 11, 1, 12),
    _MscAppnDlusDactLuRspTx_Type()
)
mscAppnDlusDactLuRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlusDactLuRspTx.setStatus("mandatory")
_MscAppnDlusSscpPuMuRx_Type = PassportCounter64
_MscAppnDlusSscpPuMuRx_Object = MibTableColumn
mscAppnDlusSscpPuMuRx = _MscAppnDlusSscpPuMuRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 15, 11, 1, 13),
    _MscAppnDlusSscpPuMuRx_Type()
)
mscAppnDlusSscpPuMuRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlusSscpPuMuRx.setStatus("mandatory")
_MscAppnDlusSscpPuMuTx_Type = PassportCounter64
_MscAppnDlusSscpPuMuTx_Object = MibTableColumn
mscAppnDlusSscpPuMuTx = _MscAppnDlusSscpPuMuTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 15, 11, 1, 14),
    _MscAppnDlusSscpPuMuTx_Type()
)
mscAppnDlusSscpPuMuTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlusSscpPuMuTx.setStatus("mandatory")
_MscAppnDlusSscpLuMuRx_Type = PassportCounter64
_MscAppnDlusSscpLuMuRx_Object = MibTableColumn
mscAppnDlusSscpLuMuRx = _MscAppnDlusSscpLuMuRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 15, 11, 1, 15),
    _MscAppnDlusSscpLuMuRx_Type()
)
mscAppnDlusSscpLuMuRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlusSscpLuMuRx.setStatus("mandatory")
_MscAppnDlusSscpLuMuTx_Type = PassportCounter64
_MscAppnDlusSscpLuMuTx_Object = MibTableColumn
mscAppnDlusSscpLuMuTx = _MscAppnDlusSscpLuMuTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 15, 11, 1, 16),
    _MscAppnDlusSscpLuMuTx_Type()
)
mscAppnDlusSscpLuMuTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDlusSscpLuMuTx.setStatus("mandatory")
_MscAppnDLUR_ObjectIdentity = ObjectIdentity
mscAppnDLUR = _MscAppnDLUR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 16)
)
_MscAppnDLURRowStatusTable_Object = MibTable
mscAppnDLURRowStatusTable = _MscAppnDLURRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 16, 1)
)
if mibBuilder.loadTexts:
    mscAppnDLURRowStatusTable.setStatus("mandatory")
_MscAppnDLURRowStatusEntry_Object = MibTableRow
mscAppnDLURRowStatusEntry = _MscAppnDLURRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 16, 1, 1)
)
mscAppnDLURRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDLURIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDLURRowStatusEntry.setStatus("mandatory")
_MscAppnDLURRowStatus_Type = RowStatus
_MscAppnDLURRowStatus_Object = MibTableColumn
mscAppnDLURRowStatus = _MscAppnDLURRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 16, 1, 1, 1),
    _MscAppnDLURRowStatus_Type()
)
mscAppnDLURRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDLURRowStatus.setStatus("mandatory")
_MscAppnDLURComponentName_Type = DisplayString
_MscAppnDLURComponentName_Object = MibTableColumn
mscAppnDLURComponentName = _MscAppnDLURComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 16, 1, 1, 2),
    _MscAppnDLURComponentName_Type()
)
mscAppnDLURComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDLURComponentName.setStatus("mandatory")
_MscAppnDLURStorageType_Type = StorageType
_MscAppnDLURStorageType_Object = MibTableColumn
mscAppnDLURStorageType = _MscAppnDLURStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 16, 1, 1, 4),
    _MscAppnDLURStorageType_Type()
)
mscAppnDLURStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDLURStorageType.setStatus("mandatory")
_MscAppnDLURIndex_Type = NonReplicated
_MscAppnDLURIndex_Object = MibTableColumn
mscAppnDLURIndex = _MscAppnDLURIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 16, 1, 1, 10),
    _MscAppnDLURIndex_Type()
)
mscAppnDLURIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnDLURIndex.setStatus("mandatory")
_MscAppnDLURDlurParmsTable_Object = MibTable
mscAppnDLURDlurParmsTable = _MscAppnDLURDlurParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 16, 2)
)
if mibBuilder.loadTexts:
    mscAppnDLURDlurParmsTable.setStatus("mandatory")
_MscAppnDLURDlurParmsEntry_Object = MibTableRow
mscAppnDLURDlurParmsEntry = _MscAppnDLURDlurParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 16, 2, 1)
)
mscAppnDLURDlurParmsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnDLURIndex"),
)
if mibBuilder.loadTexts:
    mscAppnDLURDlurParmsEntry.setStatus("mandatory")


class _MscAppnDLURPrimaryDefDlusName_Type(AsciiString):
    """Custom type mscAppnDLURPrimaryDefDlusName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_MscAppnDLURPrimaryDefDlusName_Type.__name__ = "AsciiString"
_MscAppnDLURPrimaryDefDlusName_Object = MibTableColumn
mscAppnDLURPrimaryDefDlusName = _MscAppnDLURPrimaryDefDlusName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 16, 2, 1, 2),
    _MscAppnDLURPrimaryDefDlusName_Type()
)
mscAppnDLURPrimaryDefDlusName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDLURPrimaryDefDlusName.setStatus("mandatory")


class _MscAppnDLURSecondaryDefDlusName_Type(AsciiString):
    """Custom type mscAppnDLURSecondaryDefDlusName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_MscAppnDLURSecondaryDefDlusName_Type.__name__ = "AsciiString"
_MscAppnDLURSecondaryDefDlusName_Object = MibTableColumn
mscAppnDLURSecondaryDefDlusName = _MscAppnDLURSecondaryDefDlusName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 16, 2, 1, 3),
    _MscAppnDLURSecondaryDefDlusName_Type()
)
mscAppnDLURSecondaryDefDlusName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDLURSecondaryDefDlusName.setStatus("mandatory")


class _MscAppnDLURDlusRetryTimeout_Type(Unsigned32):
    """Custom type mscAppnDLURDlusRetryTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscAppnDLURDlusRetryTimeout_Type.__name__ = "Unsigned32"
_MscAppnDLURDlusRetryTimeout_Object = MibTableColumn
mscAppnDLURDlusRetryTimeout = _MscAppnDLURDlusRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 16, 2, 1, 4),
    _MscAppnDLURDlusRetryTimeout_Type()
)
mscAppnDLURDlusRetryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDLURDlusRetryTimeout.setStatus("mandatory")


class _MscAppnDLURDlusRetryLimit_Type(Unsigned32):
    """Custom type mscAppnDLURDlusRetryLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnDLURDlusRetryLimit_Type.__name__ = "Unsigned32"
_MscAppnDLURDlusRetryLimit_Object = MibTableColumn
mscAppnDLURDlusRetryLimit = _MscAppnDLURDlusRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 16, 2, 1, 5),
    _MscAppnDLURDlusRetryLimit_Type()
)
mscAppnDLURDlusRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDLURDlusRetryLimit.setStatus("mandatory")
_MscAppnCos_ObjectIdentity = ObjectIdentity
mscAppnCos = _MscAppnCos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17)
)
_MscAppnCosRowStatusTable_Object = MibTable
mscAppnCosRowStatusTable = _MscAppnCosRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 1)
)
if mibBuilder.loadTexts:
    mscAppnCosRowStatusTable.setStatus("mandatory")
_MscAppnCosRowStatusEntry_Object = MibTableRow
mscAppnCosRowStatusEntry = _MscAppnCosRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 1, 1)
)
mscAppnCosRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnCosIndex"),
)
if mibBuilder.loadTexts:
    mscAppnCosRowStatusEntry.setStatus("mandatory")
_MscAppnCosRowStatus_Type = RowStatus
_MscAppnCosRowStatus_Object = MibTableColumn
mscAppnCosRowStatus = _MscAppnCosRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 1, 1, 1),
    _MscAppnCosRowStatus_Type()
)
mscAppnCosRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnCosRowStatus.setStatus("mandatory")
_MscAppnCosComponentName_Type = DisplayString
_MscAppnCosComponentName_Object = MibTableColumn
mscAppnCosComponentName = _MscAppnCosComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 1, 1, 2),
    _MscAppnCosComponentName_Type()
)
mscAppnCosComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnCosComponentName.setStatus("mandatory")
_MscAppnCosStorageType_Type = StorageType
_MscAppnCosStorageType_Object = MibTableColumn
mscAppnCosStorageType = _MscAppnCosStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 1, 1, 4),
    _MscAppnCosStorageType_Type()
)
mscAppnCosStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnCosStorageType.setStatus("mandatory")


class _MscAppnCosIndex_Type(AsciiStringIndex):
    """Custom type mscAppnCosIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MscAppnCosIndex_Type.__name__ = "AsciiStringIndex"
_MscAppnCosIndex_Object = MibTableColumn
mscAppnCosIndex = _MscAppnCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 1, 1, 10),
    _MscAppnCosIndex_Type()
)
mscAppnCosIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnCosIndex.setStatus("mandatory")
_MscAppnCosTg_ObjectIdentity = ObjectIdentity
mscAppnCosTg = _MscAppnCosTg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 10)
)
_MscAppnCosTgRowStatusTable_Object = MibTable
mscAppnCosTgRowStatusTable = _MscAppnCosTgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 10, 1)
)
if mibBuilder.loadTexts:
    mscAppnCosTgRowStatusTable.setStatus("mandatory")
_MscAppnCosTgRowStatusEntry_Object = MibTableRow
mscAppnCosTgRowStatusEntry = _MscAppnCosTgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 10, 1, 1)
)
mscAppnCosTgRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnCosIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnCosTgIndex"),
)
if mibBuilder.loadTexts:
    mscAppnCosTgRowStatusEntry.setStatus("mandatory")
_MscAppnCosTgRowStatus_Type = RowStatus
_MscAppnCosTgRowStatus_Object = MibTableColumn
mscAppnCosTgRowStatus = _MscAppnCosTgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 10, 1, 1, 1),
    _MscAppnCosTgRowStatus_Type()
)
mscAppnCosTgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnCosTgRowStatus.setStatus("mandatory")
_MscAppnCosTgComponentName_Type = DisplayString
_MscAppnCosTgComponentName_Object = MibTableColumn
mscAppnCosTgComponentName = _MscAppnCosTgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 10, 1, 1, 2),
    _MscAppnCosTgComponentName_Type()
)
mscAppnCosTgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnCosTgComponentName.setStatus("mandatory")
_MscAppnCosTgStorageType_Type = StorageType
_MscAppnCosTgStorageType_Object = MibTableColumn
mscAppnCosTgStorageType = _MscAppnCosTgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 10, 1, 1, 4),
    _MscAppnCosTgStorageType_Type()
)
mscAppnCosTgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnCosTgStorageType.setStatus("mandatory")


class _MscAppnCosTgIndex_Type(Integer32):
    """Custom type mscAppnCosTgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscAppnCosTgIndex_Type.__name__ = "Integer32"
_MscAppnCosTgIndex_Object = MibTableColumn
mscAppnCosTgIndex = _MscAppnCosTgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 10, 1, 1, 10),
    _MscAppnCosTgIndex_Type()
)
mscAppnCosTgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnCosTgIndex.setStatus("mandatory")
_MscAppnCosTgProvTable_Object = MibTable
mscAppnCosTgProvTable = _MscAppnCosTgProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 10, 10)
)
if mibBuilder.loadTexts:
    mscAppnCosTgProvTable.setStatus("mandatory")
_MscAppnCosTgProvEntry_Object = MibTableRow
mscAppnCosTgProvEntry = _MscAppnCosTgProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 10, 10, 1)
)
mscAppnCosTgProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnCosIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnCosTgIndex"),
)
if mibBuilder.loadTexts:
    mscAppnCosTgProvEntry.setStatus("mandatory")


class _MscAppnCosTgMinEffectiveCapacity_Type(Integer32):
    """Custom type mscAppnCosTgMinEffectiveCapacity based on Integer32"""
    defaultValue = 0

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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("max", 255),
          ("min", 0),
          ("n1000kbps", 101),
          ("n10100Mbps", 208),
          ("n101Gbps", 234),
          ("n1020Mbps", 181),
          ("n1050bps", 22),
          ("n106kbps", 75),
          ("n10800bps", 49),
          ("n1080kbps", 102),
          ("n108Mbps", 155),
          ("n1100Mbps", 182),
          ("n11100kbps", 129),
          ("n111Gbps", 235),
          ("n11300Mbps", 209),
          ("n1130bps", 23),
          ("n1150kbps", 103),
          ("n115kbps", 76),
          ("n1180Mbps", 183),
          ("n118Mbps", 156),
          ("n12000bps", 50),
          ("n1200bps", 24),
          ("n121Gbps", 236),
          ("n12300kbps", 130),
          ("n1230kbps", 104),
          ("n125kbps", 77),
          ("n12600Mbps", 210),
          ("n1260Mbps", 184),
          ("n128Mbps", 157),
          ("n131Gbps", 237),
          ("n13200bps", 51),
          ("n134kbps", 78),
          ("n13500kbps", 131),
          ("n1350bps", 25),
          ("n13800Mbps", 211),
          ("n1380kbps", 105),
          ("n138Mbps", 158),
          ("n141Gbps", 238),
          ("n1420Mbps", 185),
          ("n14400bps", 52),
          ("n144kbps", 79),
          ("n14700kbps", 132),
          ("n147Mbps", 159),
          ("n1500bps", 26),
          ("n15100Mbps", 212),
          ("n151Gbps", 239),
          ("n1540kbps", 106),
          ("n154kbps", 80),
          ("n15600bps", 53),
          ("n1570Mbps", 186),
          ("n157Mbps", 160),
          ("n160Gbps", 240),
          ("n16Gbps", 213),
          ("n16Mbps", 133),
          ("n1700Mbps", 187),
          ("n1700bps", 27),
          ("n1700kbps", 107),
          ("n170bps", 1),
          ("n170kbps", 81),
          ("n17Mbps", 134),
          ("n17kbps", 54),
          ("n1800bps", 28),
          ("n1800kbps", 108),
          ("n180Gbps", 241),
          ("n180Mbps", 161),
          ("n18Gbps", 214),
          ("n18Mbps", 135),
          ("n18kbps", 55),
          ("n1900Mbps", 188),
          ("n190bps", 2),
          ("n190kbps", 82),
          ("n19Gbps", 215),
          ("n19kbps", 56),
          ("n2000Mbps", 189),
          ("n2000bps", 29),
          ("n2000kbps", 109),
          ("n200Gbps", 242),
          ("n200Mbps", 162),
          ("n20Gbps", 216),
          ("n20Mbps", 136),
          ("n2100bps", 30),
          ("n210bps", 3),
          ("n210kbps", 83),
          ("n2200Mbps", 190),
          ("n2200kbps", 110),
          ("n220Gbps", 243),
          ("n220Mbps", 163),
          ("n22Mbps", 137),
          ("n22kbps", 57),
          ("n2300bps", 31),
          ("n2300kbps", 111),
          ("n230bps", 4),
          ("n230kbps", 84),
          ("n23Gbps", 217),
          ("n2400Mbps", 191),
          ("n2400bps", 32),
          ("n240Gbps", 244),
          ("n240Mbps", 164),
          ("n240bps", 5),
          ("n24kbps", 58),
          ("n2500Mbps", 192),
          ("n2500kbps", 112),
          ("n250kbps", 85),
          ("n25Gbps", 218),
          ("n25Mbps", 138),
          ("n260Gbps", 245),
          ("n260Mbps", 165),
          ("n260bps", 6),
          ("n26kbps", 59),
          ("n2700bps", 33),
          ("n270kbps", 86),
          ("n27Mbps", 139),
          ("n2800Mbps", 193),
          ("n2800kbps", 113),
          ("n280Gbps", 246),
          ("n280Mbps", 166),
          ("n280bps", 7),
          ("n28Gbps", 219),
          ("n290Mbps", 167),
          ("n290kbps", 87),
          ("n29Mbps", 140),
          ("n29kbps", 60),
          ("n3000bps", 34),
          ("n300Gbps", 247),
          ("n300bps", 8),
          ("n30Gbps", 220),
          ("n3100Mbps", 194),
          ("n3100kbps", 114),
          ("n310Mbps", 168),
          ("n310kbps", 88),
          ("n31kbps", 61),
          ("n320Gbps", 248),
          ("n32Mbps", 141),
          ("n3300bps", 35),
          ("n33Gbps", 221),
          ("n3400kbps", 115),
          ("n340bps", 9),
          ("n34Mbps", 142),
          ("n34kbps", 62),
          ("n3500Mbps", 195),
          ("n350Mbps", 169),
          ("n350kbps", 89),
          ("n35Gbps", 222),
          ("n3600bps", 36),
          ("n360Gbps", 249),
          ("n36kbps", 63),
          ("n3700kbps", 116),
          ("n37Mbps", 143),
          ("n3800Mbps", 196),
          ("n380bps", 10),
          ("n380kbps", 90),
          ("n38Gbps", 223),
          ("n38kbps", 64),
          ("n3900bps", 37),
          ("n390Mbps", 170),
          ("n39Mbps", 144),
          ("n4000kbps", 117),
          ("n400Gbps", 250),
          ("n40Gbps", 224),
          ("n4100Mbps", 197),
          ("n410bps", 11),
          ("n4200bps", 38),
          ("n420kbps", 91),
          ("n4300kbps", 118),
          ("n430Mbps", 171),
          ("n43kbps", 65),
          ("n4400Mbps", 198),
          ("n440Gbps", 251),
          ("n44Mbps", 145),
          ("n4500bps", 39),
          ("n450bps", 12),
          ("n45Gbps", 225),
          ("n4600kbps", 119),
          ("n460kbps", 92),
          ("n4700Mbps", 199),
          ("n470Mbps", 172),
          ("n4800bps", 40),
          ("n480Gbps", 252),
          ("n48kbps", 66),
          ("n4900kbps", 120),
          ("n490bps", 13),
          ("n49Mbps", 146),
          ("n5000Mbps", 200),
          ("n500kbps", 93),
          ("n50Gbps", 226),
          ("n510Mbps", 173),
          ("n520Gbps", 253),
          ("n530bps", 14),
          ("n53kbps", 67),
          ("n5400bps", 41),
          ("n540kbps", 94),
          ("n54Mbps", 147),
          ("n5500kbps", 121),
          ("n550Mbps", 174),
          ("n55Gbps", 227),
          ("n560Gbps", 254),
          ("n560bps", 15),
          ("n5700Mbps", 201),
          ("n580kbps", 95),
          ("n58kbps", 68),
          ("n590Mbps", 175),
          ("n59Mbps", 148),
          ("n6000bps", 42),
          ("n600bps", 16),
          ("n60Gbps", 228),
          ("n6100kbps", 122),
          ("n610kbps", 96),
          ("n62kbps", 69),
          ("n6300Mbps", 202),
          ("n630Mbps", 176),
          ("n64Mbps", 149),
          ("n65Gbps", 229),
          ("n6600bps", 43),
          ("n67kbps", 70),
          ("n6800kbps", 123),
          ("n680bps", 17),
          ("n6900Mbps", 203),
          ("n690kbps", 97),
          ("n69Mbps", 150),
          ("n70Gbps", 230),
          ("n710Mbps", 177),
          ("n7200bps", 44),
          ("n72kbps", 71),
          ("n7400kbps", 124),
          ("n74Mbps", 151),
          ("n7500Mbps", 204),
          ("n750bps", 18),
          ("n75Gbps", 231),
          ("n770kbps", 98),
          ("n77kbps", 72),
          ("n7800bps", 45),
          ("n790Mbps", 178),
          ("n79Mbps", 152),
          ("n8000kbps", 125),
          ("n81Gbps", 232),
          ("n8200Mbps", 205),
          ("n830bps", 19),
          ("n8400bps", 46),
          ("n840kbps", 99),
          ("n8600kbps", 126),
          ("n86kbps", 73),
          ("n870Mbps", 179),
          ("n8800Mbps", 206),
          ("n88Mbps", 153),
          ("n9000bps", 47),
          ("n900bps", 20),
          ("n91Gbps", 233),
          ("n9200kbps", 127),
          ("n920kbps", 100),
          ("n9400Mbps", 207),
          ("n940Mbps", 180),
          ("n9600bps", 48),
          ("n96kbps", 74),
          ("n9800kbps", 128),
          ("n980bps", 21),
          ("n98Mbps", 154))
    )


_MscAppnCosTgMinEffectiveCapacity_Type.__name__ = "Integer32"
_MscAppnCosTgMinEffectiveCapacity_Object = MibTableColumn
mscAppnCosTgMinEffectiveCapacity = _MscAppnCosTgMinEffectiveCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 10, 10, 1, 1),
    _MscAppnCosTgMinEffectiveCapacity_Type()
)
mscAppnCosTgMinEffectiveCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnCosTgMinEffectiveCapacity.setStatus("mandatory")


class _MscAppnCosTgMaxEffectiveCapacity_Type(Integer32):
    """Custom type mscAppnCosTgMaxEffectiveCapacity based on Integer32"""
    defaultValue = 255

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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("max", 255),
          ("min", 0),
          ("n1000kbps", 101),
          ("n10100Mbps", 208),
          ("n101Gbps", 234),
          ("n1020Mbps", 181),
          ("n1050bps", 22),
          ("n106kbps", 75),
          ("n10800bps", 49),
          ("n1080kbps", 102),
          ("n108Mbps", 155),
          ("n1100Mbps", 182),
          ("n11100kbps", 129),
          ("n111Gbps", 235),
          ("n11300Mbps", 209),
          ("n1130bps", 23),
          ("n1150kbps", 103),
          ("n115kbps", 76),
          ("n1180Mbps", 183),
          ("n118Mbps", 156),
          ("n12000bps", 50),
          ("n1200bps", 24),
          ("n121Gbps", 236),
          ("n12300kbps", 130),
          ("n1230kbps", 104),
          ("n125kbps", 77),
          ("n12600Mbps", 210),
          ("n1260Mbps", 184),
          ("n128Mbps", 157),
          ("n131Gbps", 237),
          ("n13200bps", 51),
          ("n134kbps", 78),
          ("n13500kbps", 131),
          ("n1350bps", 25),
          ("n13800Mbps", 211),
          ("n1380kbps", 105),
          ("n138Mbps", 158),
          ("n141Gbps", 238),
          ("n1420Mbps", 185),
          ("n14400bps", 52),
          ("n144kbps", 79),
          ("n14700kbps", 132),
          ("n147Mbps", 159),
          ("n1500bps", 26),
          ("n15100Mbps", 212),
          ("n151Gbps", 239),
          ("n1540kbps", 106),
          ("n154kbps", 80),
          ("n15600bps", 53),
          ("n1570Mbps", 186),
          ("n157Mbps", 160),
          ("n160Gbps", 240),
          ("n16Gbps", 213),
          ("n16Mbps", 133),
          ("n1700Mbps", 187),
          ("n1700bps", 27),
          ("n1700kbps", 107),
          ("n170bps", 1),
          ("n170kbps", 81),
          ("n17Mbps", 134),
          ("n17kbps", 54),
          ("n1800bps", 28),
          ("n1800kbps", 108),
          ("n180Gbps", 241),
          ("n180Mbps", 161),
          ("n18Gbps", 214),
          ("n18Mbps", 135),
          ("n18kbps", 55),
          ("n1900Mbps", 188),
          ("n190bps", 2),
          ("n190kbps", 82),
          ("n19Gbps", 215),
          ("n19kbps", 56),
          ("n2000Mbps", 189),
          ("n2000bps", 29),
          ("n2000kbps", 109),
          ("n200Gbps", 242),
          ("n200Mbps", 162),
          ("n20Gbps", 216),
          ("n20Mbps", 136),
          ("n2100bps", 30),
          ("n210bps", 3),
          ("n210kbps", 83),
          ("n2200Mbps", 190),
          ("n2200kbps", 110),
          ("n220Gbps", 243),
          ("n220Mbps", 163),
          ("n22Mbps", 137),
          ("n22kbps", 57),
          ("n2300bps", 31),
          ("n2300kbps", 111),
          ("n230bps", 4),
          ("n230kbps", 84),
          ("n23Gbps", 217),
          ("n2400Mbps", 191),
          ("n2400bps", 32),
          ("n240Gbps", 244),
          ("n240Mbps", 164),
          ("n240bps", 5),
          ("n24kbps", 58),
          ("n2500Mbps", 192),
          ("n2500kbps", 112),
          ("n250kbps", 85),
          ("n25Gbps", 218),
          ("n25Mbps", 138),
          ("n260Gbps", 245),
          ("n260Mbps", 165),
          ("n260bps", 6),
          ("n26kbps", 59),
          ("n2700bps", 33),
          ("n270kbps", 86),
          ("n27Mbps", 139),
          ("n2800Mbps", 193),
          ("n2800kbps", 113),
          ("n280Gbps", 246),
          ("n280Mbps", 166),
          ("n280bps", 7),
          ("n28Gbps", 219),
          ("n290Mbps", 167),
          ("n290kbps", 87),
          ("n29Mbps", 140),
          ("n29kbps", 60),
          ("n3000bps", 34),
          ("n300Gbps", 247),
          ("n300bps", 8),
          ("n30Gbps", 220),
          ("n3100Mbps", 194),
          ("n3100kbps", 114),
          ("n310Mbps", 168),
          ("n310kbps", 88),
          ("n31kbps", 61),
          ("n320Gbps", 248),
          ("n32Mbps", 141),
          ("n3300bps", 35),
          ("n33Gbps", 221),
          ("n3400kbps", 115),
          ("n340bps", 9),
          ("n34Mbps", 142),
          ("n34kbps", 62),
          ("n3500Mbps", 195),
          ("n350Mbps", 169),
          ("n350kbps", 89),
          ("n35Gbps", 222),
          ("n3600bps", 36),
          ("n360Gbps", 249),
          ("n36kbps", 63),
          ("n3700kbps", 116),
          ("n37Mbps", 143),
          ("n3800Mbps", 196),
          ("n380bps", 10),
          ("n380kbps", 90),
          ("n38Gbps", 223),
          ("n38kbps", 64),
          ("n3900bps", 37),
          ("n390Mbps", 170),
          ("n39Mbps", 144),
          ("n4000kbps", 117),
          ("n400Gbps", 250),
          ("n40Gbps", 224),
          ("n4100Mbps", 197),
          ("n410bps", 11),
          ("n4200bps", 38),
          ("n420kbps", 91),
          ("n4300kbps", 118),
          ("n430Mbps", 171),
          ("n43kbps", 65),
          ("n4400Mbps", 198),
          ("n440Gbps", 251),
          ("n44Mbps", 145),
          ("n4500bps", 39),
          ("n450bps", 12),
          ("n45Gbps", 225),
          ("n4600kbps", 119),
          ("n460kbps", 92),
          ("n4700Mbps", 199),
          ("n470Mbps", 172),
          ("n4800bps", 40),
          ("n480Gbps", 252),
          ("n48kbps", 66),
          ("n4900kbps", 120),
          ("n490bps", 13),
          ("n49Mbps", 146),
          ("n5000Mbps", 200),
          ("n500kbps", 93),
          ("n50Gbps", 226),
          ("n510Mbps", 173),
          ("n520Gbps", 253),
          ("n530bps", 14),
          ("n53kbps", 67),
          ("n5400bps", 41),
          ("n540kbps", 94),
          ("n54Mbps", 147),
          ("n5500kbps", 121),
          ("n550Mbps", 174),
          ("n55Gbps", 227),
          ("n560Gbps", 254),
          ("n560bps", 15),
          ("n5700Mbps", 201),
          ("n580kbps", 95),
          ("n58kbps", 68),
          ("n590Mbps", 175),
          ("n59Mbps", 148),
          ("n6000bps", 42),
          ("n600bps", 16),
          ("n60Gbps", 228),
          ("n6100kbps", 122),
          ("n610kbps", 96),
          ("n62kbps", 69),
          ("n6300Mbps", 202),
          ("n630Mbps", 176),
          ("n64Mbps", 149),
          ("n65Gbps", 229),
          ("n6600bps", 43),
          ("n67kbps", 70),
          ("n6800kbps", 123),
          ("n680bps", 17),
          ("n6900Mbps", 203),
          ("n690kbps", 97),
          ("n69Mbps", 150),
          ("n70Gbps", 230),
          ("n710Mbps", 177),
          ("n7200bps", 44),
          ("n72kbps", 71),
          ("n7400kbps", 124),
          ("n74Mbps", 151),
          ("n7500Mbps", 204),
          ("n750bps", 18),
          ("n75Gbps", 231),
          ("n770kbps", 98),
          ("n77kbps", 72),
          ("n7800bps", 45),
          ("n790Mbps", 178),
          ("n79Mbps", 152),
          ("n8000kbps", 125),
          ("n81Gbps", 232),
          ("n8200Mbps", 205),
          ("n830bps", 19),
          ("n8400bps", 46),
          ("n840kbps", 99),
          ("n8600kbps", 126),
          ("n86kbps", 73),
          ("n870Mbps", 179),
          ("n8800Mbps", 206),
          ("n88Mbps", 153),
          ("n9000bps", 47),
          ("n900bps", 20),
          ("n91Gbps", 233),
          ("n9200kbps", 127),
          ("n920kbps", 100),
          ("n9400Mbps", 207),
          ("n940Mbps", 180),
          ("n9600bps", 48),
          ("n96kbps", 74),
          ("n9800kbps", 128),
          ("n980bps", 21),
          ("n98Mbps", 154))
    )


_MscAppnCosTgMaxEffectiveCapacity_Type.__name__ = "Integer32"
_MscAppnCosTgMaxEffectiveCapacity_Object = MibTableColumn
mscAppnCosTgMaxEffectiveCapacity = _MscAppnCosTgMaxEffectiveCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 10, 10, 1, 2),
    _MscAppnCosTgMaxEffectiveCapacity_Type()
)
mscAppnCosTgMaxEffectiveCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnCosTgMaxEffectiveCapacity.setStatus("mandatory")


class _MscAppnCosTgMinConnectCost_Type(Integer32):
    """Custom type mscAppnCosTgMinConnectCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnCosTgMinConnectCost_Type.__name__ = "Integer32"
_MscAppnCosTgMinConnectCost_Object = MibTableColumn
mscAppnCosTgMinConnectCost = _MscAppnCosTgMinConnectCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 10, 10, 1, 3),
    _MscAppnCosTgMinConnectCost_Type()
)
mscAppnCosTgMinConnectCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnCosTgMinConnectCost.setStatus("mandatory")


class _MscAppnCosTgMaxConnectCost_Type(Integer32):
    """Custom type mscAppnCosTgMaxConnectCost based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnCosTgMaxConnectCost_Type.__name__ = "Integer32"
_MscAppnCosTgMaxConnectCost_Object = MibTableColumn
mscAppnCosTgMaxConnectCost = _MscAppnCosTgMaxConnectCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 10, 10, 1, 4),
    _MscAppnCosTgMaxConnectCost_Type()
)
mscAppnCosTgMaxConnectCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnCosTgMaxConnectCost.setStatus("mandatory")


class _MscAppnCosTgMinByteCost_Type(Integer32):
    """Custom type mscAppnCosTgMinByteCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnCosTgMinByteCost_Type.__name__ = "Integer32"
_MscAppnCosTgMinByteCost_Object = MibTableColumn
mscAppnCosTgMinByteCost = _MscAppnCosTgMinByteCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 10, 10, 1, 5),
    _MscAppnCosTgMinByteCost_Type()
)
mscAppnCosTgMinByteCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnCosTgMinByteCost.setStatus("mandatory")


class _MscAppnCosTgMaxByteCost_Type(Integer32):
    """Custom type mscAppnCosTgMaxByteCost based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnCosTgMaxByteCost_Type.__name__ = "Integer32"
_MscAppnCosTgMaxByteCost_Object = MibTableColumn
mscAppnCosTgMaxByteCost = _MscAppnCosTgMaxByteCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 10, 10, 1, 6),
    _MscAppnCosTgMaxByteCost_Type()
)
mscAppnCosTgMaxByteCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnCosTgMaxByteCost.setStatus("mandatory")


class _MscAppnCosTgMinSecurity_Type(Integer32):
    """Custom type mscAppnCosTgMinSecurity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              32,
              64,
              96,
              128,
              160,
              192)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 160),
          ("guardedConduit", 128),
          ("guardedRadiation", 192),
          ("nonSecure", 1),
          ("publicSwitchedNetwork", 32),
          ("secureConduit", 96),
          ("undergroundCable", 64))
    )


_MscAppnCosTgMinSecurity_Type.__name__ = "Integer32"
_MscAppnCosTgMinSecurity_Object = MibTableColumn
mscAppnCosTgMinSecurity = _MscAppnCosTgMinSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 10, 10, 1, 7),
    _MscAppnCosTgMinSecurity_Type()
)
mscAppnCosTgMinSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnCosTgMinSecurity.setStatus("mandatory")


class _MscAppnCosTgMaxSecurity_Type(Integer32):
    """Custom type mscAppnCosTgMaxSecurity based on Integer32"""
    defaultValue = 192

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              32,
              64,
              96,
              128,
              160,
              192)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 160),
          ("guardedConduit", 128),
          ("guardedRadiation", 192),
          ("nonSecure", 1),
          ("publicSwitchedNetwork", 32),
          ("secureConduit", 96),
          ("undergroundCable", 64))
    )


_MscAppnCosTgMaxSecurity_Type.__name__ = "Integer32"
_MscAppnCosTgMaxSecurity_Object = MibTableColumn
mscAppnCosTgMaxSecurity = _MscAppnCosTgMaxSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 10, 10, 1, 8),
    _MscAppnCosTgMaxSecurity_Type()
)
mscAppnCosTgMaxSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnCosTgMaxSecurity.setStatus("mandatory")


class _MscAppnCosTgMinPropDelay_Type(Integer32):
    """Custom type mscAppnCosTgMinPropDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              76,
              113,
              145,
              153,
              255)
        )
    )
    namedValues = NamedValues(
        *(("long", 153),
          ("maximum", 255),
          ("minimum", 0),
          ("negligible", 76),
          ("packetSwitched", 145),
          ("terrestrial", 113))
    )


_MscAppnCosTgMinPropDelay_Type.__name__ = "Integer32"
_MscAppnCosTgMinPropDelay_Object = MibTableColumn
mscAppnCosTgMinPropDelay = _MscAppnCosTgMinPropDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 10, 10, 1, 9),
    _MscAppnCosTgMinPropDelay_Type()
)
mscAppnCosTgMinPropDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnCosTgMinPropDelay.setStatus("mandatory")


class _MscAppnCosTgMaxPropDelay_Type(Integer32):
    """Custom type mscAppnCosTgMaxPropDelay based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              76,
              113,
              145,
              153,
              255)
        )
    )
    namedValues = NamedValues(
        *(("long", 153),
          ("maximum", 255),
          ("minimum", 0),
          ("negligible", 76),
          ("packetSwitched", 145),
          ("terrestrial", 113))
    )


_MscAppnCosTgMaxPropDelay_Type.__name__ = "Integer32"
_MscAppnCosTgMaxPropDelay_Object = MibTableColumn
mscAppnCosTgMaxPropDelay = _MscAppnCosTgMaxPropDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 10, 10, 1, 10),
    _MscAppnCosTgMaxPropDelay_Type()
)
mscAppnCosTgMaxPropDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnCosTgMaxPropDelay.setStatus("mandatory")


class _MscAppnCosTgMinModemClass_Type(Integer32):
    """Custom type mscAppnCosTgMinModemClass based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnCosTgMinModemClass_Type.__name__ = "Integer32"
_MscAppnCosTgMinModemClass_Object = MibTableColumn
mscAppnCosTgMinModemClass = _MscAppnCosTgMinModemClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 10, 10, 1, 11),
    _MscAppnCosTgMinModemClass_Type()
)
mscAppnCosTgMinModemClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnCosTgMinModemClass.setStatus("mandatory")


class _MscAppnCosTgMaxModemClass_Type(Integer32):
    """Custom type mscAppnCosTgMaxModemClass based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnCosTgMaxModemClass_Type.__name__ = "Integer32"
_MscAppnCosTgMaxModemClass_Object = MibTableColumn
mscAppnCosTgMaxModemClass = _MscAppnCosTgMaxModemClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 10, 10, 1, 12),
    _MscAppnCosTgMaxModemClass_Type()
)
mscAppnCosTgMaxModemClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnCosTgMaxModemClass.setStatus("mandatory")


class _MscAppnCosTgMinUserDefParm1_Type(Integer32):
    """Custom type mscAppnCosTgMinUserDefParm1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnCosTgMinUserDefParm1_Type.__name__ = "Integer32"
_MscAppnCosTgMinUserDefParm1_Object = MibTableColumn
mscAppnCosTgMinUserDefParm1 = _MscAppnCosTgMinUserDefParm1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 10, 10, 1, 13),
    _MscAppnCosTgMinUserDefParm1_Type()
)
mscAppnCosTgMinUserDefParm1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnCosTgMinUserDefParm1.setStatus("mandatory")


class _MscAppnCosTgMaxUserDefParm1_Type(Integer32):
    """Custom type mscAppnCosTgMaxUserDefParm1 based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnCosTgMaxUserDefParm1_Type.__name__ = "Integer32"
_MscAppnCosTgMaxUserDefParm1_Object = MibTableColumn
mscAppnCosTgMaxUserDefParm1 = _MscAppnCosTgMaxUserDefParm1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 10, 10, 1, 14),
    _MscAppnCosTgMaxUserDefParm1_Type()
)
mscAppnCosTgMaxUserDefParm1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnCosTgMaxUserDefParm1.setStatus("mandatory")


class _MscAppnCosTgMinUserDefParm2_Type(Integer32):
    """Custom type mscAppnCosTgMinUserDefParm2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnCosTgMinUserDefParm2_Type.__name__ = "Integer32"
_MscAppnCosTgMinUserDefParm2_Object = MibTableColumn
mscAppnCosTgMinUserDefParm2 = _MscAppnCosTgMinUserDefParm2_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 10, 10, 1, 15),
    _MscAppnCosTgMinUserDefParm2_Type()
)
mscAppnCosTgMinUserDefParm2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnCosTgMinUserDefParm2.setStatus("mandatory")


class _MscAppnCosTgMaxUserDefParm2_Type(Integer32):
    """Custom type mscAppnCosTgMaxUserDefParm2 based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnCosTgMaxUserDefParm2_Type.__name__ = "Integer32"
_MscAppnCosTgMaxUserDefParm2_Object = MibTableColumn
mscAppnCosTgMaxUserDefParm2 = _MscAppnCosTgMaxUserDefParm2_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 10, 10, 1, 16),
    _MscAppnCosTgMaxUserDefParm2_Type()
)
mscAppnCosTgMaxUserDefParm2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnCosTgMaxUserDefParm2.setStatus("mandatory")


class _MscAppnCosTgMinUserDefParm3_Type(Integer32):
    """Custom type mscAppnCosTgMinUserDefParm3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnCosTgMinUserDefParm3_Type.__name__ = "Integer32"
_MscAppnCosTgMinUserDefParm3_Object = MibTableColumn
mscAppnCosTgMinUserDefParm3 = _MscAppnCosTgMinUserDefParm3_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 10, 10, 1, 17),
    _MscAppnCosTgMinUserDefParm3_Type()
)
mscAppnCosTgMinUserDefParm3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnCosTgMinUserDefParm3.setStatus("mandatory")


class _MscAppnCosTgMaxUserDefParm3_Type(Integer32):
    """Custom type mscAppnCosTgMaxUserDefParm3 based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnCosTgMaxUserDefParm3_Type.__name__ = "Integer32"
_MscAppnCosTgMaxUserDefParm3_Object = MibTableColumn
mscAppnCosTgMaxUserDefParm3 = _MscAppnCosTgMaxUserDefParm3_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 10, 10, 1, 18),
    _MscAppnCosTgMaxUserDefParm3_Type()
)
mscAppnCosTgMaxUserDefParm3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnCosTgMaxUserDefParm3.setStatus("mandatory")
_MscAppnCosNode_ObjectIdentity = ObjectIdentity
mscAppnCosNode = _MscAppnCosNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 11)
)
_MscAppnCosNodeRowStatusTable_Object = MibTable
mscAppnCosNodeRowStatusTable = _MscAppnCosNodeRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 11, 1)
)
if mibBuilder.loadTexts:
    mscAppnCosNodeRowStatusTable.setStatus("mandatory")
_MscAppnCosNodeRowStatusEntry_Object = MibTableRow
mscAppnCosNodeRowStatusEntry = _MscAppnCosNodeRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 11, 1, 1)
)
mscAppnCosNodeRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnCosIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnCosNodeIndex"),
)
if mibBuilder.loadTexts:
    mscAppnCosNodeRowStatusEntry.setStatus("mandatory")
_MscAppnCosNodeRowStatus_Type = RowStatus
_MscAppnCosNodeRowStatus_Object = MibTableColumn
mscAppnCosNodeRowStatus = _MscAppnCosNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 11, 1, 1, 1),
    _MscAppnCosNodeRowStatus_Type()
)
mscAppnCosNodeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnCosNodeRowStatus.setStatus("mandatory")
_MscAppnCosNodeComponentName_Type = DisplayString
_MscAppnCosNodeComponentName_Object = MibTableColumn
mscAppnCosNodeComponentName = _MscAppnCosNodeComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 11, 1, 1, 2),
    _MscAppnCosNodeComponentName_Type()
)
mscAppnCosNodeComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnCosNodeComponentName.setStatus("mandatory")
_MscAppnCosNodeStorageType_Type = StorageType
_MscAppnCosNodeStorageType_Object = MibTableColumn
mscAppnCosNodeStorageType = _MscAppnCosNodeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 11, 1, 1, 4),
    _MscAppnCosNodeStorageType_Type()
)
mscAppnCosNodeStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnCosNodeStorageType.setStatus("mandatory")


class _MscAppnCosNodeIndex_Type(Integer32):
    """Custom type mscAppnCosNodeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscAppnCosNodeIndex_Type.__name__ = "Integer32"
_MscAppnCosNodeIndex_Object = MibTableColumn
mscAppnCosNodeIndex = _MscAppnCosNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 11, 1, 1, 10),
    _MscAppnCosNodeIndex_Type()
)
mscAppnCosNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnCosNodeIndex.setStatus("mandatory")
_MscAppnCosNodeProvTable_Object = MibTable
mscAppnCosNodeProvTable = _MscAppnCosNodeProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 11, 10)
)
if mibBuilder.loadTexts:
    mscAppnCosNodeProvTable.setStatus("mandatory")
_MscAppnCosNodeProvEntry_Object = MibTableRow
mscAppnCosNodeProvEntry = _MscAppnCosNodeProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 11, 10, 1)
)
mscAppnCosNodeProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnCosIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnCosNodeIndex"),
)
if mibBuilder.loadTexts:
    mscAppnCosNodeProvEntry.setStatus("mandatory")


class _MscAppnCosNodeMinRouteAddResistance_Type(Integer32):
    """Custom type mscAppnCosNodeMinRouteAddResistance based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnCosNodeMinRouteAddResistance_Type.__name__ = "Integer32"
_MscAppnCosNodeMinRouteAddResistance_Object = MibTableColumn
mscAppnCosNodeMinRouteAddResistance = _MscAppnCosNodeMinRouteAddResistance_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 11, 10, 1, 1),
    _MscAppnCosNodeMinRouteAddResistance_Type()
)
mscAppnCosNodeMinRouteAddResistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnCosNodeMinRouteAddResistance.setStatus("mandatory")


class _MscAppnCosNodeMaxRouteAddResistance_Type(Integer32):
    """Custom type mscAppnCosNodeMaxRouteAddResistance based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnCosNodeMaxRouteAddResistance_Type.__name__ = "Integer32"
_MscAppnCosNodeMaxRouteAddResistance_Object = MibTableColumn
mscAppnCosNodeMaxRouteAddResistance = _MscAppnCosNodeMaxRouteAddResistance_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 11, 10, 1, 2),
    _MscAppnCosNodeMaxRouteAddResistance_Type()
)
mscAppnCosNodeMaxRouteAddResistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnCosNodeMaxRouteAddResistance.setStatus("mandatory")


class _MscAppnCosNodeMinStatus_Type(Integer32):
    """Custom type mscAppnCosNodeMinStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("congested", 1),
          ("uncongested", 0))
    )


_MscAppnCosNodeMinStatus_Type.__name__ = "Integer32"
_MscAppnCosNodeMinStatus_Object = MibTableColumn
mscAppnCosNodeMinStatus = _MscAppnCosNodeMinStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 11, 10, 1, 3),
    _MscAppnCosNodeMinStatus_Type()
)
mscAppnCosNodeMinStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnCosNodeMinStatus.setStatus("mandatory")


class _MscAppnCosNodeMaxStatus_Type(Integer32):
    """Custom type mscAppnCosNodeMaxStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("congested", 1),
          ("uncongested", 0))
    )


_MscAppnCosNodeMaxStatus_Type.__name__ = "Integer32"
_MscAppnCosNodeMaxStatus_Object = MibTableColumn
mscAppnCosNodeMaxStatus = _MscAppnCosNodeMaxStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 11, 10, 1, 4),
    _MscAppnCosNodeMaxStatus_Type()
)
mscAppnCosNodeMaxStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnCosNodeMaxStatus.setStatus("mandatory")
_MscAppnCosProvTable_Object = MibTable
mscAppnCosProvTable = _MscAppnCosProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 104)
)
if mibBuilder.loadTexts:
    mscAppnCosProvTable.setStatus("mandatory")
_MscAppnCosProvEntry_Object = MibTableRow
mscAppnCosProvEntry = _MscAppnCosProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 104, 1)
)
mscAppnCosProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnCosIndex"),
)
if mibBuilder.loadTexts:
    mscAppnCosProvEntry.setStatus("mandatory")


class _MscAppnCosTransmissionPriority_Type(Integer32):
    """Custom type mscAppnCosTransmissionPriority based on Integer32"""
    defaultValue = 1

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
        *(("high", 3),
          ("low", 1),
          ("medium", 2),
          ("network", 4))
    )


_MscAppnCosTransmissionPriority_Type.__name__ = "Integer32"
_MscAppnCosTransmissionPriority_Object = MibTableColumn
mscAppnCosTransmissionPriority = _MscAppnCosTransmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 17, 104, 1, 1),
    _MscAppnCosTransmissionPriority_Type()
)
mscAppnCosTransmissionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnCosTransmissionPriority.setStatus("mandatory")
_MscAppnFrSvc_ObjectIdentity = ObjectIdentity
mscAppnFrSvc = _MscAppnFrSvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 18)
)
_MscAppnFrSvcRowStatusTable_Object = MibTable
mscAppnFrSvcRowStatusTable = _MscAppnFrSvcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 18, 1)
)
if mibBuilder.loadTexts:
    mscAppnFrSvcRowStatusTable.setStatus("mandatory")
_MscAppnFrSvcRowStatusEntry_Object = MibTableRow
mscAppnFrSvcRowStatusEntry = _MscAppnFrSvcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 18, 1, 1)
)
mscAppnFrSvcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnFrSvcIndex"),
)
if mibBuilder.loadTexts:
    mscAppnFrSvcRowStatusEntry.setStatus("mandatory")
_MscAppnFrSvcRowStatus_Type = RowStatus
_MscAppnFrSvcRowStatus_Object = MibTableColumn
mscAppnFrSvcRowStatus = _MscAppnFrSvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 18, 1, 1, 1),
    _MscAppnFrSvcRowStatus_Type()
)
mscAppnFrSvcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnFrSvcRowStatus.setStatus("mandatory")
_MscAppnFrSvcComponentName_Type = DisplayString
_MscAppnFrSvcComponentName_Object = MibTableColumn
mscAppnFrSvcComponentName = _MscAppnFrSvcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 18, 1, 1, 2),
    _MscAppnFrSvcComponentName_Type()
)
mscAppnFrSvcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnFrSvcComponentName.setStatus("mandatory")
_MscAppnFrSvcStorageType_Type = StorageType
_MscAppnFrSvcStorageType_Object = MibTableColumn
mscAppnFrSvcStorageType = _MscAppnFrSvcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 18, 1, 1, 4),
    _MscAppnFrSvcStorageType_Type()
)
mscAppnFrSvcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnFrSvcStorageType.setStatus("mandatory")
_MscAppnFrSvcIndex_Type = NonReplicated
_MscAppnFrSvcIndex_Object = MibTableColumn
mscAppnFrSvcIndex = _MscAppnFrSvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 18, 1, 1, 10),
    _MscAppnFrSvcIndex_Type()
)
mscAppnFrSvcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAppnFrSvcIndex.setStatus("mandatory")
_MscAppnFrSvcBanTable_Object = MibTable
mscAppnFrSvcBanTable = _MscAppnFrSvcBanTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 18, 10)
)
if mibBuilder.loadTexts:
    mscAppnFrSvcBanTable.setStatus("mandatory")
_MscAppnFrSvcBanEntry_Object = MibTableRow
mscAppnFrSvcBanEntry = _MscAppnFrSvcBanEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 18, 10, 1)
)
mscAppnFrSvcBanEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnFrSvcIndex"),
)
if mibBuilder.loadTexts:
    mscAppnFrSvcBanEntry.setStatus("mandatory")


class _MscAppnFrSvcBanLocalMac_Type(DashedHexString):
    """Custom type mscAppnFrSvcBanLocalMac based on DashedHexString"""
    defaultHexValue = "4fff00000000"

    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscAppnFrSvcBanLocalMac_Type.__name__ = "DashedHexString"
_MscAppnFrSvcBanLocalMac_Object = MibTableColumn
mscAppnFrSvcBanLocalMac = _MscAppnFrSvcBanLocalMac_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 18, 10, 1, 1),
    _MscAppnFrSvcBanLocalMac_Type()
)
mscAppnFrSvcBanLocalMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnFrSvcBanLocalMac.setStatus("mandatory")


class _MscAppnFrSvcBanLocalSap_Type(Hex):
    """Custom type mscAppnFrSvcBanLocalSap based on Hex"""
    defaultValue = 4

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(12, 12),
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(24, 24),
        ValueRangeConstraint(28, 28),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(44, 44),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(52, 52),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(68, 68),
        ValueRangeConstraint(72, 72),
        ValueRangeConstraint(76, 76),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(84, 84),
        ValueRangeConstraint(88, 88),
        ValueRangeConstraint(92, 92),
        ValueRangeConstraint(96, 96),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(104, 104),
        ValueRangeConstraint(108, 108),
        ValueRangeConstraint(112, 112),
        ValueRangeConstraint(116, 116),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(124, 124),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(132, 132),
        ValueRangeConstraint(136, 136),
        ValueRangeConstraint(140, 140),
        ValueRangeConstraint(144, 144),
        ValueRangeConstraint(148, 148),
        ValueRangeConstraint(152, 152),
        ValueRangeConstraint(156, 156),
        ValueRangeConstraint(160, 160),
        ValueRangeConstraint(164, 164),
        ValueRangeConstraint(168, 168),
        ValueRangeConstraint(172, 172),
        ValueRangeConstraint(176, 176),
        ValueRangeConstraint(180, 180),
        ValueRangeConstraint(184, 184),
        ValueRangeConstraint(188, 188),
        ValueRangeConstraint(192, 192),
        ValueRangeConstraint(196, 196),
        ValueRangeConstraint(200, 200),
        ValueRangeConstraint(204, 204),
        ValueRangeConstraint(208, 208),
        ValueRangeConstraint(212, 212),
        ValueRangeConstraint(216, 216),
        ValueRangeConstraint(220, 220),
        ValueRangeConstraint(224, 224),
        ValueRangeConstraint(228, 228),
        ValueRangeConstraint(232, 232),
        ValueRangeConstraint(236, 236),
        ValueRangeConstraint(240, 240),
        ValueRangeConstraint(244, 244),
        ValueRangeConstraint(248, 248),
        ValueRangeConstraint(252, 252),
    )


_MscAppnFrSvcBanLocalSap_Type.__name__ = "Hex"
_MscAppnFrSvcBanLocalSap_Object = MibTableColumn
mscAppnFrSvcBanLocalSap = _MscAppnFrSvcBanLocalSap_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 18, 10, 1, 2),
    _MscAppnFrSvcBanLocalSap_Type()
)
mscAppnFrSvcBanLocalSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnFrSvcBanLocalSap.setStatus("mandatory")
_MscAppnFrSvcProvisionedTable_Object = MibTable
mscAppnFrSvcProvisionedTable = _MscAppnFrSvcProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 18, 11)
)
if mibBuilder.loadTexts:
    mscAppnFrSvcProvisionedTable.setStatus("mandatory")
_MscAppnFrSvcProvisionedEntry_Object = MibTableRow
mscAppnFrSvcProvisionedEntry = _MscAppnFrSvcProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 18, 11, 1)
)
mscAppnFrSvcProvisionedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnFrSvcIndex"),
)
if mibBuilder.loadTexts:
    mscAppnFrSvcProvisionedEntry.setStatus("mandatory")


class _MscAppnFrSvcMaximumFrameRelaySvcs_Type(Unsigned32):
    """Custom type mscAppnFrSvcMaximumFrameRelaySvcs based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3072),
    )


_MscAppnFrSvcMaximumFrameRelaySvcs_Type.__name__ = "Unsigned32"
_MscAppnFrSvcMaximumFrameRelaySvcs_Object = MibTableColumn
mscAppnFrSvcMaximumFrameRelaySvcs = _MscAppnFrSvcMaximumFrameRelaySvcs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 18, 11, 1, 1),
    _MscAppnFrSvcMaximumFrameRelaySvcs_Type()
)
mscAppnFrSvcMaximumFrameRelaySvcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnFrSvcMaximumFrameRelaySvcs.setStatus("mandatory")


class _MscAppnFrSvcRateEnforcement_Type(Integer32):
    """Custom type mscAppnFrSvcRateEnforcement based on Integer32"""
    defaultValue = 1

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


_MscAppnFrSvcRateEnforcement_Type.__name__ = "Integer32"
_MscAppnFrSvcRateEnforcement_Object = MibTableColumn
mscAppnFrSvcRateEnforcement = _MscAppnFrSvcRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 18, 11, 1, 2),
    _MscAppnFrSvcRateEnforcement_Type()
)
mscAppnFrSvcRateEnforcement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnFrSvcRateEnforcement.setStatus("mandatory")


class _MscAppnFrSvcMaximumCir_Type(Unsigned32):
    """Custom type mscAppnFrSvcMaximumCir based on Unsigned32"""
    defaultValue = 2048000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52000000),
    )


_MscAppnFrSvcMaximumCir_Type.__name__ = "Unsigned32"
_MscAppnFrSvcMaximumCir_Object = MibTableColumn
mscAppnFrSvcMaximumCir = _MscAppnFrSvcMaximumCir_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 18, 11, 1, 4),
    _MscAppnFrSvcMaximumCir_Type()
)
mscAppnFrSvcMaximumCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnFrSvcMaximumCir.setStatus("mandatory")
_MscAppnFrSvcOperationalTable_Object = MibTable
mscAppnFrSvcOperationalTable = _MscAppnFrSvcOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 18, 12)
)
if mibBuilder.loadTexts:
    mscAppnFrSvcOperationalTable.setStatus("mandatory")
_MscAppnFrSvcOperationalEntry_Object = MibTableRow
mscAppnFrSvcOperationalEntry = _MscAppnFrSvcOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 18, 12, 1)
)
mscAppnFrSvcOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnFrSvcIndex"),
)
if mibBuilder.loadTexts:
    mscAppnFrSvcOperationalEntry.setStatus("mandatory")


class _MscAppnFrSvcCurrentNumberOfSvcCalls_Type(Gauge32):
    """Custom type mscAppnFrSvcCurrentNumberOfSvcCalls based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3072),
    )


_MscAppnFrSvcCurrentNumberOfSvcCalls_Type.__name__ = "Gauge32"
_MscAppnFrSvcCurrentNumberOfSvcCalls_Object = MibTableColumn
mscAppnFrSvcCurrentNumberOfSvcCalls = _MscAppnFrSvcCurrentNumberOfSvcCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 18, 12, 1, 1),
    _MscAppnFrSvcCurrentNumberOfSvcCalls_Type()
)
mscAppnFrSvcCurrentNumberOfSvcCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnFrSvcCurrentNumberOfSvcCalls.setStatus("mandatory")
_MscAppnProcessParmsTable_Object = MibTable
mscAppnProcessParmsTable = _MscAppnProcessParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 100)
)
if mibBuilder.loadTexts:
    mscAppnProcessParmsTable.setStatus("mandatory")
_MscAppnProcessParmsEntry_Object = MibTableRow
mscAppnProcessParmsEntry = _MscAppnProcessParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 100, 1)
)
mscAppnProcessParmsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
)
if mibBuilder.loadTexts:
    mscAppnProcessParmsEntry.setStatus("mandatory")
_MscAppnLogicalProcessor_Type = Link
_MscAppnLogicalProcessor_Object = MibTableColumn
mscAppnLogicalProcessor = _MscAppnLogicalProcessor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 100, 1, 1),
    _MscAppnLogicalProcessor_Type()
)
mscAppnLogicalProcessor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnLogicalProcessor.setStatus("mandatory")


class _MscAppnMaximumSvcs_Type(Unsigned32):
    """Custom type mscAppnMaximumSvcs based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_MscAppnMaximumSvcs_Type.__name__ = "Unsigned32"
_MscAppnMaximumSvcs_Object = MibTableColumn
mscAppnMaximumSvcs = _MscAppnMaximumSvcs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 100, 1, 22),
    _MscAppnMaximumSvcs_Type()
)
mscAppnMaximumSvcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnMaximumSvcs.setStatus("mandatory")


class _MscAppnMaximumLinkStations_Type(Unsigned32):
    """Custom type mscAppnMaximumLinkStations based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_MscAppnMaximumLinkStations_Type.__name__ = "Unsigned32"
_MscAppnMaximumLinkStations_Object = MibTableColumn
mscAppnMaximumLinkStations = _MscAppnMaximumLinkStations_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 100, 1, 23),
    _MscAppnMaximumLinkStations_Type()
)
mscAppnMaximumLinkStations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnMaximumLinkStations.setStatus("mandatory")
_MscAppnControlPointCreateParmsTable_Object = MibTable
mscAppnControlPointCreateParmsTable = _MscAppnControlPointCreateParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 101)
)
if mibBuilder.loadTexts:
    mscAppnControlPointCreateParmsTable.setStatus("mandatory")
_MscAppnControlPointCreateParmsEntry_Object = MibTableRow
mscAppnControlPointCreateParmsEntry = _MscAppnControlPointCreateParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 101, 1)
)
mscAppnControlPointCreateParmsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
)
if mibBuilder.loadTexts:
    mscAppnControlPointCreateParmsEntry.setStatus("mandatory")


class _MscAppnFqCpName_Type(AsciiString):
    """Custom type mscAppnFqCpName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_MscAppnFqCpName_Type.__name__ = "AsciiString"
_MscAppnFqCpName_Object = MibTableColumn
mscAppnFqCpName = _MscAppnFqCpName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 101, 1, 1),
    _MscAppnFqCpName_Type()
)
mscAppnFqCpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnFqCpName.setStatus("mandatory")


class _MscAppnBlockNumber_Type(Hex):
    """Custom type mscAppnBlockNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MscAppnBlockNumber_Type.__name__ = "Hex"
_MscAppnBlockNumber_Object = MibTableColumn
mscAppnBlockNumber = _MscAppnBlockNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 101, 1, 3),
    _MscAppnBlockNumber_Type()
)
mscAppnBlockNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnBlockNumber.setStatus("mandatory")


class _MscAppnIdNumber_Type(Hex):
    """Custom type mscAppnIdNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_MscAppnIdNumber_Type.__name__ = "Hex"
_MscAppnIdNumber_Object = MibTableColumn
mscAppnIdNumber = _MscAppnIdNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 101, 1, 4),
    _MscAppnIdNumber_Type()
)
mscAppnIdNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnIdNumber.setStatus("mandatory")


class _MscAppnRouteAdditionResistance_Type(Unsigned32):
    """Custom type mscAppnRouteAdditionResistance based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAppnRouteAdditionResistance_Type.__name__ = "Unsigned32"
_MscAppnRouteAdditionResistance_Object = MibTableColumn
mscAppnRouteAdditionResistance = _MscAppnRouteAdditionResistance_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 101, 1, 5),
    _MscAppnRouteAdditionResistance_Type()
)
mscAppnRouteAdditionResistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnRouteAdditionResistance.setStatus("mandatory")


class _MscAppnFeatures_Type(OctetString):
    """Custom type mscAppnFeatures based on OctetString"""
    defaultHexValue = "80"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAppnFeatures_Type.__name__ = "OctetString"
_MscAppnFeatures_Object = MibTableColumn
mscAppnFeatures = _MscAppnFeatures_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 101, 1, 6),
    _MscAppnFeatures_Type()
)
mscAppnFeatures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnFeatures.setStatus("mandatory")


class _MscAppnMaximumLocates_Type(Unsigned32):
    """Custom type mscAppnMaximumLocates based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnMaximumLocates_Type.__name__ = "Unsigned32"
_MscAppnMaximumLocates_Object = MibTableColumn
mscAppnMaximumLocates = _MscAppnMaximumLocates_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 101, 1, 7),
    _MscAppnMaximumLocates_Type()
)
mscAppnMaximumLocates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnMaximumLocates.setStatus("mandatory")


class _MscAppnMaximumDirectorySize_Type(Unsigned32):
    """Custom type mscAppnMaximumDirectorySize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnMaximumDirectorySize_Type.__name__ = "Unsigned32"
_MscAppnMaximumDirectorySize_Object = MibTableColumn
mscAppnMaximumDirectorySize = _MscAppnMaximumDirectorySize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 101, 1, 8),
    _MscAppnMaximumDirectorySize_Type()
)
mscAppnMaximumDirectorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnMaximumDirectorySize.setStatus("mandatory")


class _MscAppnMdsTxAlertQueueSize_Type(Unsigned32):
    """Custom type mscAppnMdsTxAlertQueueSize based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnMdsTxAlertQueueSize_Type.__name__ = "Unsigned32"
_MscAppnMdsTxAlertQueueSize_Object = MibTableColumn
mscAppnMdsTxAlertQueueSize = _MscAppnMdsTxAlertQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 101, 1, 9),
    _MscAppnMdsTxAlertQueueSize_Type()
)
mscAppnMdsTxAlertQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnMdsTxAlertQueueSize.setStatus("mandatory")


class _MscAppnTreeCacheSize_Type(Unsigned32):
    """Custom type mscAppnTreeCacheSize based on Unsigned32"""
    defaultValue = 40

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 65535),
    )


_MscAppnTreeCacheSize_Type.__name__ = "Unsigned32"
_MscAppnTreeCacheSize_Object = MibTableColumn
mscAppnTreeCacheSize = _MscAppnTreeCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 101, 1, 10),
    _MscAppnTreeCacheSize_Type()
)
mscAppnTreeCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnTreeCacheSize.setStatus("mandatory")


class _MscAppnTreeCacheUseLimit_Type(Unsigned32):
    """Custom type mscAppnTreeCacheUseLimit based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscAppnTreeCacheUseLimit_Type.__name__ = "Unsigned32"
_MscAppnTreeCacheUseLimit_Object = MibTableColumn
mscAppnTreeCacheUseLimit = _MscAppnTreeCacheUseLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 101, 1, 11),
    _MscAppnTreeCacheUseLimit_Type()
)
mscAppnTreeCacheUseLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnTreeCacheUseLimit.setStatus("mandatory")


class _MscAppnMaximumTopologyNodes_Type(Unsigned32):
    """Custom type mscAppnMaximumTopologyNodes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnMaximumTopologyNodes_Type.__name__ = "Unsigned32"
_MscAppnMaximumTopologyNodes_Object = MibTableColumn
mscAppnMaximumTopologyNodes = _MscAppnMaximumTopologyNodes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 101, 1, 12),
    _MscAppnMaximumTopologyNodes_Type()
)
mscAppnMaximumTopologyNodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnMaximumTopologyNodes.setStatus("mandatory")


class _MscAppnMaximumTopologyTgs_Type(Unsigned32):
    """Custom type mscAppnMaximumTopologyTgs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnMaximumTopologyTgs_Type.__name__ = "Unsigned32"
_MscAppnMaximumTopologyTgs_Object = MibTableColumn
mscAppnMaximumTopologyTgs = _MscAppnMaximumTopologyTgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 101, 1, 13),
    _MscAppnMaximumTopologyTgs_Type()
)
mscAppnMaximumTopologyTgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnMaximumTopologyTgs.setStatus("mandatory")


class _MscAppnMaximumIsrSessions_Type(Unsigned32):
    """Custom type mscAppnMaximumIsrSessions based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 65535),
    )


_MscAppnMaximumIsrSessions_Type.__name__ = "Unsigned32"
_MscAppnMaximumIsrSessions_Object = MibTableColumn
mscAppnMaximumIsrSessions = _MscAppnMaximumIsrSessions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 101, 1, 14),
    _MscAppnMaximumIsrSessions_Type()
)
mscAppnMaximumIsrSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnMaximumIsrSessions.setStatus("mandatory")


class _MscAppnIsrUpperCongestionThreshold_Type(Unsigned32):
    """Custom type mscAppnIsrUpperCongestionThreshold based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnIsrUpperCongestionThreshold_Type.__name__ = "Unsigned32"
_MscAppnIsrUpperCongestionThreshold_Object = MibTableColumn
mscAppnIsrUpperCongestionThreshold = _MscAppnIsrUpperCongestionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 101, 1, 15),
    _MscAppnIsrUpperCongestionThreshold_Type()
)
mscAppnIsrUpperCongestionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnIsrUpperCongestionThreshold.setStatus("mandatory")


class _MscAppnIsrLowerCongestionThreshold_Type(Unsigned32):
    """Custom type mscAppnIsrLowerCongestionThreshold based on Unsigned32"""
    defaultValue = 400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnIsrLowerCongestionThreshold_Type.__name__ = "Unsigned32"
_MscAppnIsrLowerCongestionThreshold_Object = MibTableColumn
mscAppnIsrLowerCongestionThreshold = _MscAppnIsrLowerCongestionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 101, 1, 16),
    _MscAppnIsrLowerCongestionThreshold_Type()
)
mscAppnIsrLowerCongestionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnIsrLowerCongestionThreshold.setStatus("mandatory")


class _MscAppnIsrMaxRuSize_Type(Unsigned32):
    """Custom type mscAppnIsrMaxRuSize based on Unsigned32"""
    defaultValue = 4096

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnIsrMaxRuSize_Type.__name__ = "Unsigned32"
_MscAppnIsrMaxRuSize_Object = MibTableColumn
mscAppnIsrMaxRuSize = _MscAppnIsrMaxRuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 101, 1, 17),
    _MscAppnIsrMaxRuSize_Type()
)
mscAppnIsrMaxRuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnIsrMaxRuSize.setStatus("mandatory")


class _MscAppnIsrRxPacingWindow_Type(Unsigned32):
    """Custom type mscAppnIsrRxPacingWindow based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscAppnIsrRxPacingWindow_Type.__name__ = "Unsigned32"
_MscAppnIsrRxPacingWindow_Object = MibTableColumn
mscAppnIsrRxPacingWindow = _MscAppnIsrRxPacingWindow_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 101, 1, 18),
    _MscAppnIsrRxPacingWindow_Type()
)
mscAppnIsrRxPacingWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnIsrRxPacingWindow.setStatus("mandatory")


class _MscAppnLocateTimeout_Type(Unsigned32):
    """Custom type mscAppnLocateTimeout based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAppnLocateTimeout_Type.__name__ = "Unsigned32"
_MscAppnLocateTimeout_Object = MibTableColumn
mscAppnLocateTimeout = _MscAppnLocateTimeout_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 101, 1, 19),
    _MscAppnLocateTimeout_Type()
)
mscAppnLocateTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnLocateTimeout.setStatus("mandatory")


class _MscAppnHprSupport_Type(Integer32):
    """Custom type mscAppnHprSupport based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("anrOnly", 1),
          ("none", 0),
          ("rtp", 2))
    )


_MscAppnHprSupport_Type.__name__ = "Integer32"
_MscAppnHprSupport_Object = MibTableColumn
mscAppnHprSupport = _MscAppnHprSupport_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 101, 1, 20),
    _MscAppnHprSupport_Type()
)
mscAppnHprSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnHprSupport.setStatus("mandatory")


class _MscAppnDlurSupport_Type(Integer32):
    """Custom type mscAppnDlurSupport based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MscAppnDlurSupport_Type.__name__ = "Integer32"
_MscAppnDlurSupport_Object = MibTableColumn
mscAppnDlurSupport = _MscAppnDlurSupport_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 101, 1, 21),
    _MscAppnDlurSupport_Type()
)
mscAppnDlurSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAppnDlurSupport.setStatus("mandatory")
_MscAppnStateTable_Object = MibTable
mscAppnStateTable = _MscAppnStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 102)
)
if mibBuilder.loadTexts:
    mscAppnStateTable.setStatus("mandatory")
_MscAppnStateEntry_Object = MibTableRow
mscAppnStateEntry = _MscAppnStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 102, 1)
)
mscAppnStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
)
if mibBuilder.loadTexts:
    mscAppnStateEntry.setStatus("mandatory")


class _MscAppnAdminState_Type(Integer32):
    """Custom type mscAppnAdminState based on Integer32"""
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


_MscAppnAdminState_Type.__name__ = "Integer32"
_MscAppnAdminState_Object = MibTableColumn
mscAppnAdminState = _MscAppnAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 102, 1, 1),
    _MscAppnAdminState_Type()
)
mscAppnAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnAdminState.setStatus("mandatory")


class _MscAppnOperationalState_Type(Integer32):
    """Custom type mscAppnOperationalState based on Integer32"""
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


_MscAppnOperationalState_Type.__name__ = "Integer32"
_MscAppnOperationalState_Object = MibTableColumn
mscAppnOperationalState = _MscAppnOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 102, 1, 2),
    _MscAppnOperationalState_Type()
)
mscAppnOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnOperationalState.setStatus("mandatory")


class _MscAppnUsageState_Type(Integer32):
    """Custom type mscAppnUsageState based on Integer32"""
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


_MscAppnUsageState_Type.__name__ = "Integer32"
_MscAppnUsageState_Object = MibTableColumn
mscAppnUsageState = _MscAppnUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 102, 1, 3),
    _MscAppnUsageState_Type()
)
mscAppnUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnUsageState.setStatus("mandatory")
_MscAppnOperationalTable_Object = MibTable
mscAppnOperationalTable = _MscAppnOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 103)
)
if mibBuilder.loadTexts:
    mscAppnOperationalTable.setStatus("mandatory")
_MscAppnOperationalEntry_Object = MibTableRow
mscAppnOperationalEntry = _MscAppnOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 103, 1)
)
mscAppnOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AppnMIB", "mscAppnIndex"),
)
if mibBuilder.loadTexts:
    mscAppnOperationalEntry.setStatus("mandatory")


class _MscAppnUpTime_Type(Unsigned32):
    """Custom type mscAppnUpTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAppnUpTime_Type.__name__ = "Unsigned32"
_MscAppnUpTime_Object = MibTableColumn
mscAppnUpTime = _MscAppnUpTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 103, 1, 1),
    _MscAppnUpTime_Type()
)
mscAppnUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnUpTime.setStatus("mandatory")


class _MscAppnHeapSpaceLimit_Type(Gauge32):
    """Custom type mscAppnHeapSpaceLimit based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAppnHeapSpaceLimit_Type.__name__ = "Gauge32"
_MscAppnHeapSpaceLimit_Object = MibTableColumn
mscAppnHeapSpaceLimit = _MscAppnHeapSpaceLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 103, 1, 2),
    _MscAppnHeapSpaceLimit_Type()
)
mscAppnHeapSpaceLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnHeapSpaceLimit.setStatus("mandatory")


class _MscAppnHeapSpaceCurrent_Type(Gauge32):
    """Custom type mscAppnHeapSpaceCurrent based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAppnHeapSpaceCurrent_Type.__name__ = "Gauge32"
_MscAppnHeapSpaceCurrent_Object = MibTableColumn
mscAppnHeapSpaceCurrent = _MscAppnHeapSpaceCurrent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 103, 1, 3),
    _MscAppnHeapSpaceCurrent_Type()
)
mscAppnHeapSpaceCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnHeapSpaceCurrent.setStatus("mandatory")


class _MscAppnMemWarningThreshold_Type(Unsigned32):
    """Custom type mscAppnMemWarningThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAppnMemWarningThreshold_Type.__name__ = "Unsigned32"
_MscAppnMemWarningThreshold_Object = MibTableColumn
mscAppnMemWarningThreshold = _MscAppnMemWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 103, 1, 4),
    _MscAppnMemWarningThreshold_Type()
)
mscAppnMemWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnMemWarningThreshold.setStatus("mandatory")


class _MscAppnMemCriticalThreshold_Type(Unsigned32):
    """Custom type mscAppnMemCriticalThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAppnMemCriticalThreshold_Type.__name__ = "Unsigned32"
_MscAppnMemCriticalThreshold_Object = MibTableColumn
mscAppnMemCriticalThreshold = _MscAppnMemCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 103, 1, 5),
    _MscAppnMemCriticalThreshold_Type()
)
mscAppnMemCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnMemCriticalThreshold.setStatus("mandatory")


class _MscAppnNnFunctionsSupported_Type(OctetString):
    """Custom type mscAppnNnFunctionsSupported based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAppnNnFunctionsSupported_Type.__name__ = "OctetString"
_MscAppnNnFunctionsSupported_Object = MibTableColumn
mscAppnNnFunctionsSupported = _MscAppnNnFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 103, 1, 6),
    _MscAppnNnFunctionsSupported_Type()
)
mscAppnNnFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnNnFunctionsSupported.setStatus("mandatory")


class _MscAppnGeneralFunctionsSupported_Type(OctetString):
    """Custom type mscAppnGeneralFunctionsSupported based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAppnGeneralFunctionsSupported_Type.__name__ = "OctetString"
_MscAppnGeneralFunctionsSupported_Object = MibTableColumn
mscAppnGeneralFunctionsSupported = _MscAppnGeneralFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 103, 1, 7),
    _MscAppnGeneralFunctionsSupported_Type()
)
mscAppnGeneralFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnGeneralFunctionsSupported.setStatus("mandatory")


class _MscAppnStatus_Type(OctetString):
    """Custom type mscAppnStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAppnStatus_Type.__name__ = "OctetString"
_MscAppnStatus_Object = MibTableColumn
mscAppnStatus = _MscAppnStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 103, 1, 8),
    _MscAppnStatus_Type()
)
mscAppnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnStatus.setStatus("mandatory")


class _MscAppnFlowReductionSequenceNumber_Type(Unsigned32):
    """Custom type mscAppnFlowReductionSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAppnFlowReductionSequenceNumber_Type.__name__ = "Unsigned32"
_MscAppnFlowReductionSequenceNumber_Object = MibTableColumn
mscAppnFlowReductionSequenceNumber = _MscAppnFlowReductionSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 103, 1, 9),
    _MscAppnFlowReductionSequenceNumber_Type()
)
mscAppnFlowReductionSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnFlowReductionSequenceNumber.setStatus("mandatory")


class _MscAppnResourceSequenceNumber_Type(Unsigned32):
    """Custom type mscAppnResourceSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAppnResourceSequenceNumber_Type.__name__ = "Unsigned32"
_MscAppnResourceSequenceNumber_Object = MibTableColumn
mscAppnResourceSequenceNumber = _MscAppnResourceSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 103, 1, 10),
    _MscAppnResourceSequenceNumber_Type()
)
mscAppnResourceSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnResourceSequenceNumber.setStatus("mandatory")
_MscAppnDefinedLsGoodXids_Type = PassportCounter64
_MscAppnDefinedLsGoodXids_Object = MibTableColumn
mscAppnDefinedLsGoodXids = _MscAppnDefinedLsGoodXids_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 103, 1, 11),
    _MscAppnDefinedLsGoodXids_Type()
)
mscAppnDefinedLsGoodXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDefinedLsGoodXids.setStatus("mandatory")
_MscAppnDefinedLsBadXids_Type = PassportCounter64
_MscAppnDefinedLsBadXids_Object = MibTableColumn
mscAppnDefinedLsBadXids = _MscAppnDefinedLsBadXids_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 103, 1, 12),
    _MscAppnDefinedLsBadXids_Type()
)
mscAppnDefinedLsBadXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDefinedLsBadXids.setStatus("mandatory")
_MscAppnDynamicLsGoodXids_Type = PassportCounter64
_MscAppnDynamicLsGoodXids_Object = MibTableColumn
mscAppnDynamicLsGoodXids = _MscAppnDynamicLsGoodXids_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 103, 1, 13),
    _MscAppnDynamicLsGoodXids_Type()
)
mscAppnDynamicLsGoodXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDynamicLsGoodXids.setStatus("mandatory")
_MscAppnDynamicLsBadXids_Type = PassportCounter64
_MscAppnDynamicLsBadXids_Object = MibTableColumn
mscAppnDynamicLsBadXids = _MscAppnDynamicLsBadXids_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 103, 1, 14),
    _MscAppnDynamicLsBadXids_Type()
)
mscAppnDynamicLsBadXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnDynamicLsBadXids.setStatus("mandatory")


class _MscAppnActiveSvcs_Type(Unsigned32):
    """Custom type mscAppnActiveSvcs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscAppnActiveSvcs_Type.__name__ = "Unsigned32"
_MscAppnActiveSvcs_Object = MibTableColumn
mscAppnActiveSvcs = _MscAppnActiveSvcs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 103, 1, 15),
    _MscAppnActiveSvcs_Type()
)
mscAppnActiveSvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnActiveSvcs.setStatus("mandatory")


class _MscAppnActiveLinkStations_Type(Unsigned32):
    """Custom type mscAppnActiveLinkStations based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscAppnActiveLinkStations_Type.__name__ = "Unsigned32"
_MscAppnActiveLinkStations_Object = MibTableColumn
mscAppnActiveLinkStations = _MscAppnActiveLinkStations_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 110, 103, 1, 16),
    _MscAppnActiveLinkStations_Type()
)
mscAppnActiveLinkStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAppnActiveLinkStations.setStatus("mandatory")
_AppnMIB_ObjectIdentity = ObjectIdentity
appnMIB = _AppnMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 29)
)
_AppnGroup_ObjectIdentity = ObjectIdentity
appnGroup = _AppnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 29, 1)
)
_AppnGroupCA_ObjectIdentity = ObjectIdentity
appnGroupCA = _AppnGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 29, 1, 1)
)
_AppnGroupCA02_ObjectIdentity = ObjectIdentity
appnGroupCA02 = _AppnGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 29, 1, 1, 3)
)
_AppnGroupCA02DevelopmentLoad_ObjectIdentity = ObjectIdentity
appnGroupCA02DevelopmentLoad = _AppnGroupCA02DevelopmentLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 29, 1, 1, 3, 1)
)
_AppnGroupCA0214_ObjectIdentity = ObjectIdentity
appnGroupCA0214 = _AppnGroupCA0214_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 29, 1, 1, 3, 1, 14)
)
_AppnGroupCA0214A_ObjectIdentity = ObjectIdentity
appnGroupCA0214A = _AppnGroupCA0214A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 29, 1, 1, 3, 1, 14, 1)
)
_AppnCapabilities_ObjectIdentity = ObjectIdentity
appnCapabilities = _AppnCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 29, 3)
)
_AppnCapabilitiesCA_ObjectIdentity = ObjectIdentity
appnCapabilitiesCA = _AppnCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 29, 3, 1)
)
_AppnCapabilitiesCA02_ObjectIdentity = ObjectIdentity
appnCapabilitiesCA02 = _AppnCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 29, 3, 1, 3)
)
_AppnCapabilitiesCA02DevelopmentLoad_ObjectIdentity = ObjectIdentity
appnCapabilitiesCA02DevelopmentLoad = _AppnCapabilitiesCA02DevelopmentLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 29, 3, 1, 3, 1)
)
_AppnCapabilitiesCA0214_ObjectIdentity = ObjectIdentity
appnCapabilitiesCA0214 = _AppnCapabilitiesCA0214_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 29, 3, 1, 3, 1, 14)
)
_AppnCapabilitiesCA0214A_ObjectIdentity = ObjectIdentity
appnCapabilitiesCA0214A = _AppnCapabilitiesCA0214A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 29, 3, 1, 3, 1, 14, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-AppnMIB",
    **{"mscAppn": mscAppn,
       "mscAppnRowStatusTable": mscAppnRowStatusTable,
       "mscAppnRowStatusEntry": mscAppnRowStatusEntry,
       "mscAppnRowStatus": mscAppnRowStatus,
       "mscAppnComponentName": mscAppnComponentName,
       "mscAppnStorageType": mscAppnStorageType,
       "mscAppnIndex": mscAppnIndex,
       "mscAppnDna": mscAppnDna,
       "mscAppnDnaRowStatusTable": mscAppnDnaRowStatusTable,
       "mscAppnDnaRowStatusEntry": mscAppnDnaRowStatusEntry,
       "mscAppnDnaRowStatus": mscAppnDnaRowStatus,
       "mscAppnDnaComponentName": mscAppnDnaComponentName,
       "mscAppnDnaStorageType": mscAppnDnaStorageType,
       "mscAppnDnaIndex": mscAppnDnaIndex,
       "mscAppnDnaHgM": mscAppnDnaHgM,
       "mscAppnDnaHgMRowStatusTable": mscAppnDnaHgMRowStatusTable,
       "mscAppnDnaHgMRowStatusEntry": mscAppnDnaHgMRowStatusEntry,
       "mscAppnDnaHgMRowStatus": mscAppnDnaHgMRowStatus,
       "mscAppnDnaHgMComponentName": mscAppnDnaHgMComponentName,
       "mscAppnDnaHgMStorageType": mscAppnDnaHgMStorageType,
       "mscAppnDnaHgMIndex": mscAppnDnaHgMIndex,
       "mscAppnDnaHgMHgAddr": mscAppnDnaHgMHgAddr,
       "mscAppnDnaHgMHgAddrRowStatusTable": mscAppnDnaHgMHgAddrRowStatusTable,
       "mscAppnDnaHgMHgAddrRowStatusEntry": mscAppnDnaHgMHgAddrRowStatusEntry,
       "mscAppnDnaHgMHgAddrRowStatus": mscAppnDnaHgMHgAddrRowStatus,
       "mscAppnDnaHgMHgAddrComponentName": mscAppnDnaHgMHgAddrComponentName,
       "mscAppnDnaHgMHgAddrStorageType": mscAppnDnaHgMHgAddrStorageType,
       "mscAppnDnaHgMHgAddrIndex": mscAppnDnaHgMHgAddrIndex,
       "mscAppnDnaHgMHgAddrAddrTable": mscAppnDnaHgMHgAddrAddrTable,
       "mscAppnDnaHgMHgAddrAddrEntry": mscAppnDnaHgMHgAddrAddrEntry,
       "mscAppnDnaHgMHgAddrNumberingPlanIndicator": mscAppnDnaHgMHgAddrNumberingPlanIndicator,
       "mscAppnDnaHgMHgAddrDataNetworkAddress": mscAppnDnaHgMHgAddrDataNetworkAddress,
       "mscAppnDnaHgMIfTable": mscAppnDnaHgMIfTable,
       "mscAppnDnaHgMIfEntry": mscAppnDnaHgMIfEntry,
       "mscAppnDnaHgMAvailabilityUpdateThreshold": mscAppnDnaHgMAvailabilityUpdateThreshold,
       "mscAppnDnaHgMOpTable": mscAppnDnaHgMOpTable,
       "mscAppnDnaHgMOpEntry": mscAppnDnaHgMOpEntry,
       "mscAppnDnaHgMMaxAvailableChannels": mscAppnDnaHgMMaxAvailableChannels,
       "mscAppnDnaHgMAvailableChannels": mscAppnDnaHgMAvailableChannels,
       "mscAppnDnaHgMAvailabilityDelta": mscAppnDnaHgMAvailabilityDelta,
       "mscAppnDnaCug": mscAppnDnaCug,
       "mscAppnDnaCugRowStatusTable": mscAppnDnaCugRowStatusTable,
       "mscAppnDnaCugRowStatusEntry": mscAppnDnaCugRowStatusEntry,
       "mscAppnDnaCugRowStatus": mscAppnDnaCugRowStatus,
       "mscAppnDnaCugComponentName": mscAppnDnaCugComponentName,
       "mscAppnDnaCugStorageType": mscAppnDnaCugStorageType,
       "mscAppnDnaCugIndex": mscAppnDnaCugIndex,
       "mscAppnDnaCugCugOptionsTable": mscAppnDnaCugCugOptionsTable,
       "mscAppnDnaCugCugOptionsEntry": mscAppnDnaCugCugOptionsEntry,
       "mscAppnDnaCugType": mscAppnDnaCugType,
       "mscAppnDnaCugDnic": mscAppnDnaCugDnic,
       "mscAppnDnaCugInterlockCode": mscAppnDnaCugInterlockCode,
       "mscAppnDnaCugPreferential": mscAppnDnaCugPreferential,
       "mscAppnDnaCugOutCalls": mscAppnDnaCugOutCalls,
       "mscAppnDnaCugIncCalls": mscAppnDnaCugIncCalls,
       "mscAppnDnaCugPrivileged": mscAppnDnaCugPrivileged,
       "mscAppnDnaAddressTable": mscAppnDnaAddressTable,
       "mscAppnDnaAddressEntry": mscAppnDnaAddressEntry,
       "mscAppnDnaNumberingPlanIndicator": mscAppnDnaNumberingPlanIndicator,
       "mscAppnDnaDataNetworkAddress": mscAppnDnaDataNetworkAddress,
       "mscAppnDnaOutgoingOptionsTable": mscAppnDnaOutgoingOptionsTable,
       "mscAppnDnaOutgoingOptionsEntry": mscAppnDnaOutgoingOptionsEntry,
       "mscAppnDnaOutDefaultPriority": mscAppnDnaOutDefaultPriority,
       "mscAppnDnaOutDefaultPathSensitivity": mscAppnDnaOutDefaultPathSensitivity,
       "mscAppnDnaOutPathSensitivityOverRide": mscAppnDnaOutPathSensitivityOverRide,
       "mscAppnDnaOutDefaultPathReliability": mscAppnDnaOutDefaultPathReliability,
       "mscAppnDnaOutAccess": mscAppnDnaOutAccess,
       "mscAppnDnaDefaultTransferPriority": mscAppnDnaDefaultTransferPriority,
       "mscAppnDnaTransferPriorityOverRide": mscAppnDnaTransferPriorityOverRide,
       "mscAppnDnaIncomingOptionsTable": mscAppnDnaIncomingOptionsTable,
       "mscAppnDnaIncomingOptionsEntry": mscAppnDnaIncomingOptionsEntry,
       "mscAppnDnaIncAccess": mscAppnDnaIncAccess,
       "mscAppnDnaCallOptionsTable": mscAppnDnaCallOptionsTable,
       "mscAppnDnaCallOptionsEntry": mscAppnDnaCallOptionsEntry,
       "mscAppnDnaDefaultRecvFrmNetworkThruputClass": mscAppnDnaDefaultRecvFrmNetworkThruputClass,
       "mscAppnDnaDefaultSendToNetworkThruputClass": mscAppnDnaDefaultSendToNetworkThruputClass,
       "mscAppnDnaDefaultRecvFrmNetworkWindowSize": mscAppnDnaDefaultRecvFrmNetworkWindowSize,
       "mscAppnDnaDefaultSendToNetworkWindowSize": mscAppnDnaDefaultSendToNetworkWindowSize,
       "mscAppnDnaAccountClass": mscAppnDnaAccountClass,
       "mscAppnDnaAccountCollection": mscAppnDnaAccountCollection,
       "mscAppnDnaServiceExchange": mscAppnDnaServiceExchange,
       "mscAppnDlci": mscAppnDlci,
       "mscAppnDlciRowStatusTable": mscAppnDlciRowStatusTable,
       "mscAppnDlciRowStatusEntry": mscAppnDlciRowStatusEntry,
       "mscAppnDlciRowStatus": mscAppnDlciRowStatus,
       "mscAppnDlciComponentName": mscAppnDlciComponentName,
       "mscAppnDlciStorageType": mscAppnDlciStorageType,
       "mscAppnDlciIndex": mscAppnDlciIndex,
       "mscAppnDlciDc": mscAppnDlciDc,
       "mscAppnDlciDcRowStatusTable": mscAppnDlciDcRowStatusTable,
       "mscAppnDlciDcRowStatusEntry": mscAppnDlciDcRowStatusEntry,
       "mscAppnDlciDcRowStatus": mscAppnDlciDcRowStatus,
       "mscAppnDlciDcComponentName": mscAppnDlciDcComponentName,
       "mscAppnDlciDcStorageType": mscAppnDlciDcStorageType,
       "mscAppnDlciDcIndex": mscAppnDlciDcIndex,
       "mscAppnDlciDcOptionsTable": mscAppnDlciDcOptionsTable,
       "mscAppnDlciDcOptionsEntry": mscAppnDlciDcOptionsEntry,
       "mscAppnDlciDcRemoteNpi": mscAppnDlciDcRemoteNpi,
       "mscAppnDlciDcRemoteDna": mscAppnDlciDcRemoteDna,
       "mscAppnDlciDcRemoteDlci": mscAppnDlciDcRemoteDlci,
       "mscAppnDlciDcType": mscAppnDlciDcType,
       "mscAppnDlciDcTransferPriority": mscAppnDlciDcTransferPriority,
       "mscAppnDlciDcDiscardPriority": mscAppnDlciDcDiscardPriority,
       "mscAppnDlciDcNfaTable": mscAppnDlciDcNfaTable,
       "mscAppnDlciDcNfaEntry": mscAppnDlciDcNfaEntry,
       "mscAppnDlciDcNfaIndex": mscAppnDlciDcNfaIndex,
       "mscAppnDlciDcNfaValue": mscAppnDlciDcNfaValue,
       "mscAppnDlciDcNfaRowStatus": mscAppnDlciDcNfaRowStatus,
       "mscAppnDlciVc": mscAppnDlciVc,
       "mscAppnDlciVcRowStatusTable": mscAppnDlciVcRowStatusTable,
       "mscAppnDlciVcRowStatusEntry": mscAppnDlciVcRowStatusEntry,
       "mscAppnDlciVcRowStatus": mscAppnDlciVcRowStatus,
       "mscAppnDlciVcComponentName": mscAppnDlciVcComponentName,
       "mscAppnDlciVcStorageType": mscAppnDlciVcStorageType,
       "mscAppnDlciVcIndex": mscAppnDlciVcIndex,
       "mscAppnDlciVcCadTable": mscAppnDlciVcCadTable,
       "mscAppnDlciVcCadEntry": mscAppnDlciVcCadEntry,
       "mscAppnDlciVcType": mscAppnDlciVcType,
       "mscAppnDlciVcState": mscAppnDlciVcState,
       "mscAppnDlciVcPreviousState": mscAppnDlciVcPreviousState,
       "mscAppnDlciVcDiagnosticCode": mscAppnDlciVcDiagnosticCode,
       "mscAppnDlciVcPreviousDiagnosticCode": mscAppnDlciVcPreviousDiagnosticCode,
       "mscAppnDlciVcCalledNpi": mscAppnDlciVcCalledNpi,
       "mscAppnDlciVcCalledDna": mscAppnDlciVcCalledDna,
       "mscAppnDlciVcCalledLcn": mscAppnDlciVcCalledLcn,
       "mscAppnDlciVcCallingNpi": mscAppnDlciVcCallingNpi,
       "mscAppnDlciVcCallingDna": mscAppnDlciVcCallingDna,
       "mscAppnDlciVcCallingLcn": mscAppnDlciVcCallingLcn,
       "mscAppnDlciVcAccountingEnabled": mscAppnDlciVcAccountingEnabled,
       "mscAppnDlciVcFastSelectCall": mscAppnDlciVcFastSelectCall,
       "mscAppnDlciVcPathReliability": mscAppnDlciVcPathReliability,
       "mscAppnDlciVcAccountingEnd": mscAppnDlciVcAccountingEnd,
       "mscAppnDlciVcPriority": mscAppnDlciVcPriority,
       "mscAppnDlciVcSegmentSize": mscAppnDlciVcSegmentSize,
       "mscAppnDlciVcMaxSubnetPktSize": mscAppnDlciVcMaxSubnetPktSize,
       "mscAppnDlciVcRcosToNetwork": mscAppnDlciVcRcosToNetwork,
       "mscAppnDlciVcRcosFromNetwork": mscAppnDlciVcRcosFromNetwork,
       "mscAppnDlciVcEmissionPriorityToNetwork": mscAppnDlciVcEmissionPriorityToNetwork,
       "mscAppnDlciVcEmissionPriorityFromNetwork": mscAppnDlciVcEmissionPriorityFromNetwork,
       "mscAppnDlciVcDataPath": mscAppnDlciVcDataPath,
       "mscAppnDlciVcIntdTable": mscAppnDlciVcIntdTable,
       "mscAppnDlciVcIntdEntry": mscAppnDlciVcIntdEntry,
       "mscAppnDlciVcCallReferenceNumber": mscAppnDlciVcCallReferenceNumber,
       "mscAppnDlciVcElapsedTimeTillNow": mscAppnDlciVcElapsedTimeTillNow,
       "mscAppnDlciVcSegmentsRx": mscAppnDlciVcSegmentsRx,
       "mscAppnDlciVcSegmentsSent": mscAppnDlciVcSegmentsSent,
       "mscAppnDlciVcStartTime": mscAppnDlciVcStartTime,
       "mscAppnDlciVcFrdTable": mscAppnDlciVcFrdTable,
       "mscAppnDlciVcFrdEntry": mscAppnDlciVcFrdEntry,
       "mscAppnDlciVcFrmCongestedToSubnet": mscAppnDlciVcFrmCongestedToSubnet,
       "mscAppnDlciVcCannotForwardToSubnet": mscAppnDlciVcCannotForwardToSubnet,
       "mscAppnDlciVcNotDataXferToSubnet": mscAppnDlciVcNotDataXferToSubnet,
       "mscAppnDlciVcOutOfRangeFrmFromSubnet": mscAppnDlciVcOutOfRangeFrmFromSubnet,
       "mscAppnDlciVcCombErrorsFromSubnet": mscAppnDlciVcCombErrorsFromSubnet,
       "mscAppnDlciVcDuplicatesFromSubnet": mscAppnDlciVcDuplicatesFromSubnet,
       "mscAppnDlciVcNotDataXferFromSubnet": mscAppnDlciVcNotDataXferFromSubnet,
       "mscAppnDlciVcFrmLossTimeouts": mscAppnDlciVcFrmLossTimeouts,
       "mscAppnDlciVcOoSeqByteCntExceeded": mscAppnDlciVcOoSeqByteCntExceeded,
       "mscAppnDlciVcPeakOoSeqPktCount": mscAppnDlciVcPeakOoSeqPktCount,
       "mscAppnDlciVcPeakOoSeqFrmForwarded": mscAppnDlciVcPeakOoSeqFrmForwarded,
       "mscAppnDlciVcSendSequenceNumber": mscAppnDlciVcSendSequenceNumber,
       "mscAppnDlciVcPktRetryTimeouts": mscAppnDlciVcPktRetryTimeouts,
       "mscAppnDlciVcPeakRetryQueueSize": mscAppnDlciVcPeakRetryQueueSize,
       "mscAppnDlciVcSubnetRecoveries": mscAppnDlciVcSubnetRecoveries,
       "mscAppnDlciVcOoSeqPktCntExceeded": mscAppnDlciVcOoSeqPktCntExceeded,
       "mscAppnDlciVcPeakOoSeqByteCount": mscAppnDlciVcPeakOoSeqByteCount,
       "mscAppnDlciVcDmepTable": mscAppnDlciVcDmepTable,
       "mscAppnDlciVcDmepEntry": mscAppnDlciVcDmepEntry,
       "mscAppnDlciVcDmepValue": mscAppnDlciVcDmepValue,
       "mscAppnDlciBnnLsDef": mscAppnDlciBnnLsDef,
       "mscAppnDlciBnnLsDefRowStatusTable": mscAppnDlciBnnLsDefRowStatusTable,
       "mscAppnDlciBnnLsDefRowStatusEntry": mscAppnDlciBnnLsDefRowStatusEntry,
       "mscAppnDlciBnnLsDefRowStatus": mscAppnDlciBnnLsDefRowStatus,
       "mscAppnDlciBnnLsDefComponentName": mscAppnDlciBnnLsDefComponentName,
       "mscAppnDlciBnnLsDefStorageType": mscAppnDlciBnnLsDefStorageType,
       "mscAppnDlciBnnLsDefIndex": mscAppnDlciBnnLsDefIndex,
       "mscAppnDlciBnnLsDefProvTable": mscAppnDlciBnnLsDefProvTable,
       "mscAppnDlciBnnLsDefProvEntry": mscAppnDlciBnnLsDefProvEntry,
       "mscAppnDlciBnnLsDefDspuService": mscAppnDlciBnnLsDefDspuService,
       "mscAppnDlciBnnLsDefAdjacentCpName": mscAppnDlciBnnLsDefAdjacentCpName,
       "mscAppnDlciBnnLsDefAdjacentCpType": mscAppnDlciBnnLsDefAdjacentCpType,
       "mscAppnDlciBnnLsDefTgNum": mscAppnDlciBnnLsDefTgNum,
       "mscAppnDlciBnnLsDefDlusName": mscAppnDlciBnnLsDefDlusName,
       "mscAppnDlciBnnLsDefBackupDlusName": mscAppnDlciBnnLsDefBackupDlusName,
       "mscAppnDlciBnnLsDefHprSupported": mscAppnDlciBnnLsDefHprSupported,
       "mscAppnDlciBnnLsDefAdjacentNodeID": mscAppnDlciBnnLsDefAdjacentNodeID,
       "mscAppnDlciBnnLsDefCpCpSessionSupport": mscAppnDlciBnnLsDefCpCpSessionSupport,
       "mscAppnDlciBnnLsDefMaxTxBtuSize": mscAppnDlciBnnLsDefMaxTxBtuSize,
       "mscAppnDlciBnnLsDefLsRole": mscAppnDlciBnnLsDefLsRole,
       "mscAppnDlciSp": mscAppnDlciSp,
       "mscAppnDlciSpRowStatusTable": mscAppnDlciSpRowStatusTable,
       "mscAppnDlciSpRowStatusEntry": mscAppnDlciSpRowStatusEntry,
       "mscAppnDlciSpRowStatus": mscAppnDlciSpRowStatus,
       "mscAppnDlciSpComponentName": mscAppnDlciSpComponentName,
       "mscAppnDlciSpStorageType": mscAppnDlciSpStorageType,
       "mscAppnDlciSpIndex": mscAppnDlciSpIndex,
       "mscAppnDlciSpParmsTable": mscAppnDlciSpParmsTable,
       "mscAppnDlciSpParmsEntry": mscAppnDlciSpParmsEntry,
       "mscAppnDlciSpRateEnforcement": mscAppnDlciSpRateEnforcement,
       "mscAppnDlciSpCommittedInformationRate": mscAppnDlciSpCommittedInformationRate,
       "mscAppnDlciSpCommittedBurstSize": mscAppnDlciSpCommittedBurstSize,
       "mscAppnDlciSpExcessBurstSize": mscAppnDlciSpExcessBurstSize,
       "mscAppnDlciSpMeasurementInterval": mscAppnDlciSpMeasurementInterval,
       "mscAppnDlciBanLsDef": mscAppnDlciBanLsDef,
       "mscAppnDlciBanLsDefRowStatusTable": mscAppnDlciBanLsDefRowStatusTable,
       "mscAppnDlciBanLsDefRowStatusEntry": mscAppnDlciBanLsDefRowStatusEntry,
       "mscAppnDlciBanLsDefRowStatus": mscAppnDlciBanLsDefRowStatus,
       "mscAppnDlciBanLsDefComponentName": mscAppnDlciBanLsDefComponentName,
       "mscAppnDlciBanLsDefStorageType": mscAppnDlciBanLsDefStorageType,
       "mscAppnDlciBanLsDefMacIndex": mscAppnDlciBanLsDefMacIndex,
       "mscAppnDlciBanLsDefSapIndex": mscAppnDlciBanLsDefSapIndex,
       "mscAppnDlciBanLsDefProvTable": mscAppnDlciBanLsDefProvTable,
       "mscAppnDlciBanLsDefProvEntry": mscAppnDlciBanLsDefProvEntry,
       "mscAppnDlciBanLsDefDspuService": mscAppnDlciBanLsDefDspuService,
       "mscAppnDlciBanLsDefAdjacentCpName": mscAppnDlciBanLsDefAdjacentCpName,
       "mscAppnDlciBanLsDefAdjacentCpType": mscAppnDlciBanLsDefAdjacentCpType,
       "mscAppnDlciBanLsDefTgNum": mscAppnDlciBanLsDefTgNum,
       "mscAppnDlciBanLsDefDlusName": mscAppnDlciBanLsDefDlusName,
       "mscAppnDlciBanLsDefBackupDlusName": mscAppnDlciBanLsDefBackupDlusName,
       "mscAppnDlciBanLsDefHprSupported": mscAppnDlciBanLsDefHprSupported,
       "mscAppnDlciBanLsDefAdjacentNodeID": mscAppnDlciBanLsDefAdjacentNodeID,
       "mscAppnDlciBanLsDefCpCpSessionSupport": mscAppnDlciBanLsDefCpCpSessionSupport,
       "mscAppnDlciBanLsDefMaxTxBtuSize": mscAppnDlciBanLsDefMaxTxBtuSize,
       "mscAppnDlciBanLsDefLsRole": mscAppnDlciBanLsDefLsRole,
       "mscAppnDlciBan": mscAppnDlciBan,
       "mscAppnDlciBanRowStatusTable": mscAppnDlciBanRowStatusTable,
       "mscAppnDlciBanRowStatusEntry": mscAppnDlciBanRowStatusEntry,
       "mscAppnDlciBanRowStatus": mscAppnDlciBanRowStatus,
       "mscAppnDlciBanComponentName": mscAppnDlciBanComponentName,
       "mscAppnDlciBanStorageType": mscAppnDlciBanStorageType,
       "mscAppnDlciBanIndex": mscAppnDlciBanIndex,
       "mscAppnDlciBanProvTable": mscAppnDlciBanProvTable,
       "mscAppnDlciBanProvEntry": mscAppnDlciBanProvEntry,
       "mscAppnDlciBanLocalMac": mscAppnDlciBanLocalMac,
       "mscAppnDlciBanLocalSap": mscAppnDlciBanLocalSap,
       "mscAppnDlciStateTable": mscAppnDlciStateTable,
       "mscAppnDlciStateEntry": mscAppnDlciStateEntry,
       "mscAppnDlciAdminState": mscAppnDlciAdminState,
       "mscAppnDlciOperationalState": mscAppnDlciOperationalState,
       "mscAppnDlciUsageState": mscAppnDlciUsageState,
       "mscAppnDlciSpOpTable": mscAppnDlciSpOpTable,
       "mscAppnDlciSpOpEntry": mscAppnDlciSpOpEntry,
       "mscAppnDlciRateEnforcement": mscAppnDlciRateEnforcement,
       "mscAppnDlciCommittedInformationRate": mscAppnDlciCommittedInformationRate,
       "mscAppnDlciCommittedBurstSize": mscAppnDlciCommittedBurstSize,
       "mscAppnDlciExcessInformationRate": mscAppnDlciExcessInformationRate,
       "mscAppnDlciExcessBurstSize": mscAppnDlciExcessBurstSize,
       "mscAppnDlciMeasurementInterval": mscAppnDlciMeasurementInterval,
       "mscAppnLcn": mscAppnLcn,
       "mscAppnLcnRowStatusTable": mscAppnLcnRowStatusTable,
       "mscAppnLcnRowStatusEntry": mscAppnLcnRowStatusEntry,
       "mscAppnLcnRowStatus": mscAppnLcnRowStatus,
       "mscAppnLcnComponentName": mscAppnLcnComponentName,
       "mscAppnLcnStorageType": mscAppnLcnStorageType,
       "mscAppnLcnIndex": mscAppnLcnIndex,
       "mscAppnLcnDc": mscAppnLcnDc,
       "mscAppnLcnDcRowStatusTable": mscAppnLcnDcRowStatusTable,
       "mscAppnLcnDcRowStatusEntry": mscAppnLcnDcRowStatusEntry,
       "mscAppnLcnDcRowStatus": mscAppnLcnDcRowStatus,
       "mscAppnLcnDcComponentName": mscAppnLcnDcComponentName,
       "mscAppnLcnDcStorageType": mscAppnLcnDcStorageType,
       "mscAppnLcnDcIndex": mscAppnLcnDcIndex,
       "mscAppnLcnDcOptionsTable": mscAppnLcnDcOptionsTable,
       "mscAppnLcnDcOptionsEntry": mscAppnLcnDcOptionsEntry,
       "mscAppnLcnDcRemoteNpi": mscAppnLcnDcRemoteNpi,
       "mscAppnLcnDcRemoteDna": mscAppnLcnDcRemoteDna,
       "mscAppnLcnDcTransferPriority": mscAppnLcnDcTransferPriority,
       "mscAppnLcnDcDiscardPriority": mscAppnLcnDcDiscardPriority,
       "mscAppnLcnVc": mscAppnLcnVc,
       "mscAppnLcnVcRowStatusTable": mscAppnLcnVcRowStatusTable,
       "mscAppnLcnVcRowStatusEntry": mscAppnLcnVcRowStatusEntry,
       "mscAppnLcnVcRowStatus": mscAppnLcnVcRowStatus,
       "mscAppnLcnVcComponentName": mscAppnLcnVcComponentName,
       "mscAppnLcnVcStorageType": mscAppnLcnVcStorageType,
       "mscAppnLcnVcIndex": mscAppnLcnVcIndex,
       "mscAppnLcnVcCadTable": mscAppnLcnVcCadTable,
       "mscAppnLcnVcCadEntry": mscAppnLcnVcCadEntry,
       "mscAppnLcnVcType": mscAppnLcnVcType,
       "mscAppnLcnVcState": mscAppnLcnVcState,
       "mscAppnLcnVcPreviousState": mscAppnLcnVcPreviousState,
       "mscAppnLcnVcDiagnosticCode": mscAppnLcnVcDiagnosticCode,
       "mscAppnLcnVcPreviousDiagnosticCode": mscAppnLcnVcPreviousDiagnosticCode,
       "mscAppnLcnVcCalledNpi": mscAppnLcnVcCalledNpi,
       "mscAppnLcnVcCalledDna": mscAppnLcnVcCalledDna,
       "mscAppnLcnVcCalledLcn": mscAppnLcnVcCalledLcn,
       "mscAppnLcnVcCallingNpi": mscAppnLcnVcCallingNpi,
       "mscAppnLcnVcCallingDna": mscAppnLcnVcCallingDna,
       "mscAppnLcnVcCallingLcn": mscAppnLcnVcCallingLcn,
       "mscAppnLcnVcAccountingEnabled": mscAppnLcnVcAccountingEnabled,
       "mscAppnLcnVcFastSelectCall": mscAppnLcnVcFastSelectCall,
       "mscAppnLcnVcLocalRxPktSize": mscAppnLcnVcLocalRxPktSize,
       "mscAppnLcnVcLocalTxPktSize": mscAppnLcnVcLocalTxPktSize,
       "mscAppnLcnVcLocalTxWindowSize": mscAppnLcnVcLocalTxWindowSize,
       "mscAppnLcnVcLocalRxWindowSize": mscAppnLcnVcLocalRxWindowSize,
       "mscAppnLcnVcPathReliability": mscAppnLcnVcPathReliability,
       "mscAppnLcnVcAccountingEnd": mscAppnLcnVcAccountingEnd,
       "mscAppnLcnVcPriority": mscAppnLcnVcPriority,
       "mscAppnLcnVcSegmentSize": mscAppnLcnVcSegmentSize,
       "mscAppnLcnVcSubnetTxPktSize": mscAppnLcnVcSubnetTxPktSize,
       "mscAppnLcnVcSubnetTxWindowSize": mscAppnLcnVcSubnetTxWindowSize,
       "mscAppnLcnVcSubnetRxPktSize": mscAppnLcnVcSubnetRxPktSize,
       "mscAppnLcnVcSubnetRxWindowSize": mscAppnLcnVcSubnetRxWindowSize,
       "mscAppnLcnVcMaxSubnetPktSize": mscAppnLcnVcMaxSubnetPktSize,
       "mscAppnLcnVcTransferPriorityToNetwork": mscAppnLcnVcTransferPriorityToNetwork,
       "mscAppnLcnVcTransferPriorityFromNetwork": mscAppnLcnVcTransferPriorityFromNetwork,
       "mscAppnLcnVcIntdTable": mscAppnLcnVcIntdTable,
       "mscAppnLcnVcIntdEntry": mscAppnLcnVcIntdEntry,
       "mscAppnLcnVcCallReferenceNumber": mscAppnLcnVcCallReferenceNumber,
       "mscAppnLcnVcElapsedTimeTillNow": mscAppnLcnVcElapsedTimeTillNow,
       "mscAppnLcnVcSegmentsRx": mscAppnLcnVcSegmentsRx,
       "mscAppnLcnVcSegmentsSent": mscAppnLcnVcSegmentsSent,
       "mscAppnLcnVcStartTime": mscAppnLcnVcStartTime,
       "mscAppnLcnVcStatsTable": mscAppnLcnVcStatsTable,
       "mscAppnLcnVcStatsEntry": mscAppnLcnVcStatsEntry,
       "mscAppnLcnVcAckStackingTimeouts": mscAppnLcnVcAckStackingTimeouts,
       "mscAppnLcnVcOutOfRangeFrmFromSubnet": mscAppnLcnVcOutOfRangeFrmFromSubnet,
       "mscAppnLcnVcDuplicatesFromSubnet": mscAppnLcnVcDuplicatesFromSubnet,
       "mscAppnLcnVcFrmRetryTimeouts": mscAppnLcnVcFrmRetryTimeouts,
       "mscAppnLcnVcPeakRetryQueueSize": mscAppnLcnVcPeakRetryQueueSize,
       "mscAppnLcnVcPeakOoSeqQueueSize": mscAppnLcnVcPeakOoSeqQueueSize,
       "mscAppnLcnVcPeakOoSeqFrmForwarded": mscAppnLcnVcPeakOoSeqFrmForwarded,
       "mscAppnLcnVcPeakStackedAcksRx": mscAppnLcnVcPeakStackedAcksRx,
       "mscAppnLcnVcSubnetRecoveries": mscAppnLcnVcSubnetRecoveries,
       "mscAppnLcnVcWindowClosuresToSubnet": mscAppnLcnVcWindowClosuresToSubnet,
       "mscAppnLcnVcWindowClosuresFromSubnet": mscAppnLcnVcWindowClosuresFromSubnet,
       "mscAppnLcnVcWrTriggers": mscAppnLcnVcWrTriggers,
       "mscAppnLcnStateTable": mscAppnLcnStateTable,
       "mscAppnLcnStateEntry": mscAppnLcnStateEntry,
       "mscAppnLcnAdminState": mscAppnLcnAdminState,
       "mscAppnLcnOperationalState": mscAppnLcnOperationalState,
       "mscAppnLcnUsageState": mscAppnLcnUsageState,
       "mscAppnPort": mscAppnPort,
       "mscAppnPortRowStatusTable": mscAppnPortRowStatusTable,
       "mscAppnPortRowStatusEntry": mscAppnPortRowStatusEntry,
       "mscAppnPortRowStatus": mscAppnPortRowStatus,
       "mscAppnPortComponentName": mscAppnPortComponentName,
       "mscAppnPortStorageType": mscAppnPortStorageType,
       "mscAppnPortIndex": mscAppnPortIndex,
       "mscAppnPortConfigTable": mscAppnPortConfigTable,
       "mscAppnPortConfigEntry": mscAppnPortConfigEntry,
       "mscAppnPortType": mscAppnPortType,
       "mscAppnPortMaxRxBtuSize": mscAppnPortMaxRxBtuSize,
       "mscAppnPortMaxTxBtuSize": mscAppnPortMaxTxBtuSize,
       "mscAppnPortTotLinkActLim": mscAppnPortTotLinkActLim,
       "mscAppnPortInbLinkActLim": mscAppnPortInbLinkActLim,
       "mscAppnPortOutLinkActLim": mscAppnPortOutLinkActLim,
       "mscAppnPortLsRole": mscAppnPortLsRole,
       "mscAppnPortActXidExchLim": mscAppnPortActXidExchLim,
       "mscAppnPortNonactXidExchLim": mscAppnPortNonactXidExchLim,
       "mscAppnPortLsXmitRxCap": mscAppnPortLsXmitRxCap,
       "mscAppnPortMaxIfrmRxWindow": mscAppnPortMaxIfrmRxWindow,
       "mscAppnPortTargetPacingCount": mscAppnPortTargetPacingCount,
       "mscAppnPortOperTable": mscAppnPortOperTable,
       "mscAppnPortOperEntry": mscAppnPortOperEntry,
       "mscAppnPortState": mscAppnPortState,
       "mscAppnPortDlcType": mscAppnPortDlcType,
       "mscAppnPortSimRim": mscAppnPortSimRim,
       "mscAppnPortDefinedLsGoodXids": mscAppnPortDefinedLsGoodXids,
       "mscAppnPortDefinedLsBadXids": mscAppnPortDefinedLsBadXids,
       "mscAppnPortDynLsGoodXids": mscAppnPortDynLsGoodXids,
       "mscAppnPortDynLsBadXids": mscAppnPortDynLsBadXids,
       "mscAppnPortTgCharTable": mscAppnPortTgCharTable,
       "mscAppnPortTgCharEntry": mscAppnPortTgCharEntry,
       "mscAppnPortEffectiveCap": mscAppnPortEffectiveCap,
       "mscAppnPortConnectCost": mscAppnPortConnectCost,
       "mscAppnPortByteCost": mscAppnPortByteCost,
       "mscAppnPortSecurity": mscAppnPortSecurity,
       "mscAppnPortPropagationDelay": mscAppnPortPropagationDelay,
       "mscAppnPortUserDefinedParm1": mscAppnPortUserDefinedParm1,
       "mscAppnPortUserDefinedParm2": mscAppnPortUserDefinedParm2,
       "mscAppnPortUserDefinedParm3": mscAppnPortUserDefinedParm3,
       "mscAppnLs": mscAppnLs,
       "mscAppnLsRowStatusTable": mscAppnLsRowStatusTable,
       "mscAppnLsRowStatusEntry": mscAppnLsRowStatusEntry,
       "mscAppnLsRowStatus": mscAppnLsRowStatus,
       "mscAppnLsComponentName": mscAppnLsComponentName,
       "mscAppnLsStorageType": mscAppnLsStorageType,
       "mscAppnLsIndex": mscAppnLsIndex,
       "mscAppnLsLsVcReferenceTable": mscAppnLsLsVcReferenceTable,
       "mscAppnLsLsVcReferenceEntry": mscAppnLsLsVcReferenceEntry,
       "mscAppnLsName": mscAppnLsName,
       "mscAppnLsSap": mscAppnLsSap,
       "mscAppnLsConfigTable": mscAppnLsConfigTable,
       "mscAppnLsConfigEntry": mscAppnLsConfigEntry,
       "mscAppnLsPortName": mscAppnLsPortName,
       "mscAppnLsFeatures": mscAppnLsFeatures,
       "mscAppnLsMaxTxBtuSize": mscAppnLsMaxTxBtuSize,
       "mscAppnLsOperTable": mscAppnLsOperTable,
       "mscAppnLsOperEntry": mscAppnLsOperEntry,
       "mscAppnLsDlcType": mscAppnLsDlcType,
       "mscAppnLsLinkStationState": mscAppnLsLinkStationState,
       "mscAppnLsLinkStationSubState": mscAppnLsLinkStationSubState,
       "mscAppnLsActSessCount": mscAppnLsActSessCount,
       "mscAppnLsActualCpName": mscAppnLsActualCpName,
       "mscAppnLsActualCpType": mscAppnLsActualCpType,
       "mscAppnLsDlcName": mscAppnLsDlcName,
       "mscAppnLsDynamicOrDefined": mscAppnLsDynamicOrDefined,
       "mscAppnLsMigration": mscAppnLsMigration,
       "mscAppnLsTgNum": mscAppnLsTgNum,
       "mscAppnLsHprSupport": mscAppnLsHprSupport,
       "mscAppnLsAnrLabel": mscAppnLsAnrLabel,
       "mscAppnLsTgCharTable": mscAppnLsTgCharTable,
       "mscAppnLsTgCharEntry": mscAppnLsTgCharEntry,
       "mscAppnLsEffectiveCap": mscAppnLsEffectiveCap,
       "mscAppnLsConnectCost": mscAppnLsConnectCost,
       "mscAppnLsByteCost": mscAppnLsByteCost,
       "mscAppnLsSecurity": mscAppnLsSecurity,
       "mscAppnLsPropagationDelay": mscAppnLsPropagationDelay,
       "mscAppnLsUserDefinedParm1": mscAppnLsUserDefinedParm1,
       "mscAppnLsUserDefinedParm2": mscAppnLsUserDefinedParm2,
       "mscAppnLsUserDefinedParm3": mscAppnLsUserDefinedParm3,
       "mscAppnLsStatsTable": mscAppnLsStatsTable,
       "mscAppnLsStatsEntry": mscAppnLsStatsEntry,
       "mscAppnLsInXidBytes": mscAppnLsInXidBytes,
       "mscAppnLsInMsgBytes": mscAppnLsInMsgBytes,
       "mscAppnLsInXidFrames": mscAppnLsInXidFrames,
       "mscAppnLsInMsgFrames": mscAppnLsInMsgFrames,
       "mscAppnLsOutXidBytes": mscAppnLsOutXidBytes,
       "mscAppnLsOutMsgBytes": mscAppnLsOutMsgBytes,
       "mscAppnLsOutXidFrames": mscAppnLsOutXidFrames,
       "mscAppnLsOutMsgFrames": mscAppnLsOutMsgFrames,
       "mscAppnLsInInvalidSnaFrames": mscAppnLsInInvalidSnaFrames,
       "mscAppnLsInSessionControlFrames": mscAppnLsInSessionControlFrames,
       "mscAppnLsOutSessionControlFrames": mscAppnLsOutSessionControlFrames,
       "mscAppnLsEchoResponse": mscAppnLsEchoResponse,
       "mscAppnLsCurrentDelay": mscAppnLsCurrentDelay,
       "mscAppnLsMaxDelay": mscAppnLsMaxDelay,
       "mscAppnLsMinDelay": mscAppnLsMinDelay,
       "mscAppnLsGoodXids": mscAppnLsGoodXids,
       "mscAppnLsBadXids": mscAppnLsBadXids,
       "mscAppnDirEnt": mscAppnDirEnt,
       "mscAppnDirEntRowStatusTable": mscAppnDirEntRowStatusTable,
       "mscAppnDirEntRowStatusEntry": mscAppnDirEntRowStatusEntry,
       "mscAppnDirEntRowStatus": mscAppnDirEntRowStatus,
       "mscAppnDirEntComponentName": mscAppnDirEntComponentName,
       "mscAppnDirEntStorageType": mscAppnDirEntStorageType,
       "mscAppnDirEntIndex": mscAppnDirEntIndex,
       "mscAppnDirEntOperTable": mscAppnDirEntOperTable,
       "mscAppnDirEntOperEntry": mscAppnDirEntOperEntry,
       "mscAppnDirEntServerName": mscAppnDirEntServerName,
       "mscAppnDirEntLuOwnerName": mscAppnDirEntLuOwnerName,
       "mscAppnDirEntLocation": mscAppnDirEntLocation,
       "mscAppnDirEntEntryType": mscAppnDirEntEntryType,
       "mscAppnDirEntWildCard": mscAppnDirEntWildCard,
       "mscAppnAdjNn": mscAppnAdjNn,
       "mscAppnAdjNnRowStatusTable": mscAppnAdjNnRowStatusTable,
       "mscAppnAdjNnRowStatusEntry": mscAppnAdjNnRowStatusEntry,
       "mscAppnAdjNnRowStatus": mscAppnAdjNnRowStatus,
       "mscAppnAdjNnComponentName": mscAppnAdjNnComponentName,
       "mscAppnAdjNnStorageType": mscAppnAdjNnStorageType,
       "mscAppnAdjNnIndex": mscAppnAdjNnIndex,
       "mscAppnAdjNnOperTable": mscAppnAdjNnOperTable,
       "mscAppnAdjNnOperEntry": mscAppnAdjNnOperEntry,
       "mscAppnAdjNnCpCpSessStatus": mscAppnAdjNnCpCpSessStatus,
       "mscAppnAdjNnOutOfSeqTdus": mscAppnAdjNnOutOfSeqTdus,
       "mscAppnAdjNnLastFrsnSent": mscAppnAdjNnLastFrsnSent,
       "mscAppnAdjNnLastFrsnReceived": mscAppnAdjNnLastFrsnReceived,
       "mscAppnNn": mscAppnNn,
       "mscAppnNnRowStatusTable": mscAppnNnRowStatusTable,
       "mscAppnNnRowStatusEntry": mscAppnNnRowStatusEntry,
       "mscAppnNnRowStatus": mscAppnNnRowStatus,
       "mscAppnNnComponentName": mscAppnNnComponentName,
       "mscAppnNnStorageType": mscAppnNnStorageType,
       "mscAppnNnIndex": mscAppnNnIndex,
       "mscAppnNnOperTable": mscAppnNnOperTable,
       "mscAppnNnOperEntry": mscAppnNnOperEntry,
       "mscAppnNnDaysLeft": mscAppnNnDaysLeft,
       "mscAppnNnNodeType": mscAppnNnNodeType,
       "mscAppnNnResourceSequenceNumber": mscAppnNnResourceSequenceNumber,
       "mscAppnNnRouteAdditionResistance": mscAppnNnRouteAdditionResistance,
       "mscAppnNnStatus": mscAppnNnStatus,
       "mscAppnNnFunctionSupported": mscAppnNnFunctionSupported,
       "mscAppnLocTg": mscAppnLocTg,
       "mscAppnLocTgRowStatusTable": mscAppnLocTgRowStatusTable,
       "mscAppnLocTgRowStatusEntry": mscAppnLocTgRowStatusEntry,
       "mscAppnLocTgRowStatus": mscAppnLocTgRowStatus,
       "mscAppnLocTgComponentName": mscAppnLocTgComponentName,
       "mscAppnLocTgStorageType": mscAppnLocTgStorageType,
       "mscAppnLocTgDestFqcpNameIndex": mscAppnLocTgDestFqcpNameIndex,
       "mscAppnLocTgTransmissionGroupIndex": mscAppnLocTgTransmissionGroupIndex,
       "mscAppnLocTgOperTable": mscAppnLocTgOperTable,
       "mscAppnLocTgOperEntry": mscAppnLocTgOperEntry,
       "mscAppnLocTgStatus": mscAppnLocTgStatus,
       "mscAppnLocTgResourceSequenceNumber": mscAppnLocTgResourceSequenceNumber,
       "mscAppnLocTgLinkAddressTable": mscAppnLocTgLinkAddressTable,
       "mscAppnLocTgLinkAddressEntry": mscAppnLocTgLinkAddressEntry,
       "mscAppnLocTgDlcData": mscAppnLocTgDlcData,
       "mscAppnLocTgTgCharTable": mscAppnLocTgTgCharTable,
       "mscAppnLocTgTgCharEntry": mscAppnLocTgTgCharEntry,
       "mscAppnLocTgEffectiveCap": mscAppnLocTgEffectiveCap,
       "mscAppnLocTgConnectCost": mscAppnLocTgConnectCost,
       "mscAppnLocTgByteCost": mscAppnLocTgByteCost,
       "mscAppnLocTgSecurity": mscAppnLocTgSecurity,
       "mscAppnLocTgPropagationDelay": mscAppnLocTgPropagationDelay,
       "mscAppnLocTgUserDefinedParm1": mscAppnLocTgUserDefinedParm1,
       "mscAppnLocTgUserDefinedParm2": mscAppnLocTgUserDefinedParm2,
       "mscAppnLocTgUserDefinedParm3": mscAppnLocTgUserDefinedParm3,
       "mscAppnIsrSess": mscAppnIsrSess,
       "mscAppnIsrSessRowStatusTable": mscAppnIsrSessRowStatusTable,
       "mscAppnIsrSessRowStatusEntry": mscAppnIsrSessRowStatusEntry,
       "mscAppnIsrSessRowStatus": mscAppnIsrSessRowStatus,
       "mscAppnIsrSessComponentName": mscAppnIsrSessComponentName,
       "mscAppnIsrSessStorageType": mscAppnIsrSessStorageType,
       "mscAppnIsrSessFqcpNameIndex": mscAppnIsrSessFqcpNameIndex,
       "mscAppnIsrSessProcedureCorrelationIdIndex": mscAppnIsrSessProcedureCorrelationIdIndex,
       "mscAppnIsrSessOperTable": mscAppnIsrSessOperTable,
       "mscAppnIsrSessOperEntry": mscAppnIsrSessOperEntry,
       "mscAppnIsrSessTransmissionPriority": mscAppnIsrSessTransmissionPriority,
       "mscAppnIsrSessCosName": mscAppnIsrSessCosName,
       "mscAppnIsrSessLimitedResource": mscAppnIsrSessLimitedResource,
       "mscAppnIsrSessPriStats": mscAppnIsrSessPriStats,
       "mscAppnIsrSessPriStatsRowStatusTable": mscAppnIsrSessPriStatsRowStatusTable,
       "mscAppnIsrSessPriStatsRowStatusEntry": mscAppnIsrSessPriStatsRowStatusEntry,
       "mscAppnIsrSessPriStatsRowStatus": mscAppnIsrSessPriStatsRowStatus,
       "mscAppnIsrSessPriStatsComponentName": mscAppnIsrSessPriStatsComponentName,
       "mscAppnIsrSessPriStatsStorageType": mscAppnIsrSessPriStatsStorageType,
       "mscAppnIsrSessPriStatsIndex": mscAppnIsrSessPriStatsIndex,
       "mscAppnIsrSessPriStatsStatsTable": mscAppnIsrSessPriStatsStatsTable,
       "mscAppnIsrSessPriStatsStatsEntry": mscAppnIsrSessPriStatsStatsEntry,
       "mscAppnIsrSessPriStatsRxRuSize": mscAppnIsrSessPriStatsRxRuSize,
       "mscAppnIsrSessPriStatsMaxTxBtuSize": mscAppnIsrSessPriStatsMaxTxBtuSize,
       "mscAppnIsrSessPriStatsMaxRxBtuSize": mscAppnIsrSessPriStatsMaxRxBtuSize,
       "mscAppnIsrSessPriStatsMaxTxPacWin": mscAppnIsrSessPriStatsMaxTxPacWin,
       "mscAppnIsrSessPriStatsCurTxPacWin": mscAppnIsrSessPriStatsCurTxPacWin,
       "mscAppnIsrSessPriStatsMaxRxPacWin": mscAppnIsrSessPriStatsMaxRxPacWin,
       "mscAppnIsrSessPriStatsCurRxPacWin": mscAppnIsrSessPriStatsCurRxPacWin,
       "mscAppnIsrSessPriStatsTxDataframes": mscAppnIsrSessPriStatsTxDataframes,
       "mscAppnIsrSessPriStatsTxFmdFrames": mscAppnIsrSessPriStatsTxFmdFrames,
       "mscAppnIsrSessPriStatsTxDataBytes": mscAppnIsrSessPriStatsTxDataBytes,
       "mscAppnIsrSessPriStatsRxDataFrames": mscAppnIsrSessPriStatsRxDataFrames,
       "mscAppnIsrSessPriStatsRxFmdFrames": mscAppnIsrSessPriStatsRxFmdFrames,
       "mscAppnIsrSessPriStatsRxDataBytes": mscAppnIsrSessPriStatsRxDataBytes,
       "mscAppnIsrSessPriStatsSidh": mscAppnIsrSessPriStatsSidh,
       "mscAppnIsrSessPriStatsSidl": mscAppnIsrSessPriStatsSidl,
       "mscAppnIsrSessPriStatsOdai": mscAppnIsrSessPriStatsOdai,
       "mscAppnIsrSessPriStatsLsName": mscAppnIsrSessPriStatsLsName,
       "mscAppnIsrSessSecStats": mscAppnIsrSessSecStats,
       "mscAppnIsrSessSecStatsRowStatusTable": mscAppnIsrSessSecStatsRowStatusTable,
       "mscAppnIsrSessSecStatsRowStatusEntry": mscAppnIsrSessSecStatsRowStatusEntry,
       "mscAppnIsrSessSecStatsRowStatus": mscAppnIsrSessSecStatsRowStatus,
       "mscAppnIsrSessSecStatsComponentName": mscAppnIsrSessSecStatsComponentName,
       "mscAppnIsrSessSecStatsStorageType": mscAppnIsrSessSecStatsStorageType,
       "mscAppnIsrSessSecStatsIndex": mscAppnIsrSessSecStatsIndex,
       "mscAppnIsrSessSecStatsStatsTable": mscAppnIsrSessSecStatsStatsTable,
       "mscAppnIsrSessSecStatsStatsEntry": mscAppnIsrSessSecStatsStatsEntry,
       "mscAppnIsrSessSecStatsRxRuSize": mscAppnIsrSessSecStatsRxRuSize,
       "mscAppnIsrSessSecStatsMaxTxBtuSize": mscAppnIsrSessSecStatsMaxTxBtuSize,
       "mscAppnIsrSessSecStatsMaxRxBtuSize": mscAppnIsrSessSecStatsMaxRxBtuSize,
       "mscAppnIsrSessSecStatsMaxTxPacWin": mscAppnIsrSessSecStatsMaxTxPacWin,
       "mscAppnIsrSessSecStatsCurTxPacWin": mscAppnIsrSessSecStatsCurTxPacWin,
       "mscAppnIsrSessSecStatsMaxRxPacWin": mscAppnIsrSessSecStatsMaxRxPacWin,
       "mscAppnIsrSessSecStatsCurRxPacWin": mscAppnIsrSessSecStatsCurRxPacWin,
       "mscAppnIsrSessSecStatsTxDataframes": mscAppnIsrSessSecStatsTxDataframes,
       "mscAppnIsrSessSecStatsTxFmdFrames": mscAppnIsrSessSecStatsTxFmdFrames,
       "mscAppnIsrSessSecStatsTxDataBytes": mscAppnIsrSessSecStatsTxDataBytes,
       "mscAppnIsrSessSecStatsRxDataFrames": mscAppnIsrSessSecStatsRxDataFrames,
       "mscAppnIsrSessSecStatsRxFmdFrames": mscAppnIsrSessSecStatsRxFmdFrames,
       "mscAppnIsrSessSecStatsRxDataBytes": mscAppnIsrSessSecStatsRxDataBytes,
       "mscAppnIsrSessSecStatsSidh": mscAppnIsrSessSecStatsSidh,
       "mscAppnIsrSessSecStatsSidl": mscAppnIsrSessSecStatsSidl,
       "mscAppnIsrSessSecStatsOdai": mscAppnIsrSessSecStatsOdai,
       "mscAppnIsrSessSecStatsLsName": mscAppnIsrSessSecStatsLsName,
       "mscAppnNnTg": mscAppnNnTg,
       "mscAppnNnTgRowStatusTable": mscAppnNnTgRowStatusTable,
       "mscAppnNnTgRowStatusEntry": mscAppnNnTgRowStatusEntry,
       "mscAppnNnTgRowStatus": mscAppnNnTgRowStatus,
       "mscAppnNnTgComponentName": mscAppnNnTgComponentName,
       "mscAppnNnTgStorageType": mscAppnNnTgStorageType,
       "mscAppnNnTgOwnerFqcpNameIndex": mscAppnNnTgOwnerFqcpNameIndex,
       "mscAppnNnTgDestFqcpNameIndex": mscAppnNnTgDestFqcpNameIndex,
       "mscAppnNnTgTransmissionGroupIndex": mscAppnNnTgTransmissionGroupIndex,
       "mscAppnNnTgOperTable": mscAppnNnTgOperTable,
       "mscAppnNnTgOperEntry": mscAppnNnTgOperEntry,
       "mscAppnNnTgFlowReductionSequenceNumber": mscAppnNnTgFlowReductionSequenceNumber,
       "mscAppnNnTgDaysLeft": mscAppnNnTgDaysLeft,
       "mscAppnNnTgResourceSequenceNumber": mscAppnNnTgResourceSequenceNumber,
       "mscAppnNnTgStatus": mscAppnNnTgStatus,
       "mscAppnNnTgLinkAddressTable": mscAppnNnTgLinkAddressTable,
       "mscAppnNnTgLinkAddressEntry": mscAppnNnTgLinkAddressEntry,
       "mscAppnNnTgDlcData": mscAppnNnTgDlcData,
       "mscAppnNnTgTgCharTable": mscAppnNnTgTgCharTable,
       "mscAppnNnTgTgCharEntry": mscAppnNnTgTgCharEntry,
       "mscAppnNnTgEffectiveCap": mscAppnNnTgEffectiveCap,
       "mscAppnNnTgConnectCost": mscAppnNnTgConnectCost,
       "mscAppnNnTgByteCost": mscAppnNnTgByteCost,
       "mscAppnNnTgSecurity": mscAppnNnTgSecurity,
       "mscAppnNnTgPropagationDelay": mscAppnNnTgPropagationDelay,
       "mscAppnNnTgUserDefinedParm1": mscAppnNnTgUserDefinedParm1,
       "mscAppnNnTgUserDefinedParm2": mscAppnNnTgUserDefinedParm2,
       "mscAppnNnTgUserDefinedParm3": mscAppnNnTgUserDefinedParm3,
       "mscAppnRtp": mscAppnRtp,
       "mscAppnRtpRowStatusTable": mscAppnRtpRowStatusTable,
       "mscAppnRtpRowStatusEntry": mscAppnRtpRowStatusEntry,
       "mscAppnRtpRowStatus": mscAppnRtpRowStatus,
       "mscAppnRtpComponentName": mscAppnRtpComponentName,
       "mscAppnRtpStorageType": mscAppnRtpStorageType,
       "mscAppnRtpIndex": mscAppnRtpIndex,
       "mscAppnRtpOperTable": mscAppnRtpOperTable,
       "mscAppnRtpOperEntry": mscAppnRtpOperEntry,
       "mscAppnRtpLocalLsName": mscAppnRtpLocalLsName,
       "mscAppnRtpRemoteCpName": mscAppnRtpRemoteCpName,
       "mscAppnRtpCosName": mscAppnRtpCosName,
       "mscAppnRtpActiveSessions": mscAppnRtpActiveSessions,
       "mscAppnRtpLocalTcid": mscAppnRtpLocalTcid,
       "mscAppnRtpRemoteTcid": mscAppnRtpRemoteTcid,
       "mscAppnRtpIdleTimer": mscAppnRtpIdleTimer,
       "mscAppnRtpMaxBtuSize": mscAppnRtpMaxBtuSize,
       "mscAppnRtpStatsTable": mscAppnRtpStatsTable,
       "mscAppnRtpStatsEntry": mscAppnRtpStatsEntry,
       "mscAppnRtpTxBytes": mscAppnRtpTxBytes,
       "mscAppnRtpRxBytes": mscAppnRtpRxBytes,
       "mscAppnRtpBytesResent": mscAppnRtpBytesResent,
       "mscAppnRtpBytesDiscarded": mscAppnRtpBytesDiscarded,
       "mscAppnRtpPktTx": mscAppnRtpPktTx,
       "mscAppnRtpPktRx": mscAppnRtpPktRx,
       "mscAppnRtpPktResent": mscAppnRtpPktResent,
       "mscAppnRtpPktDiscard": mscAppnRtpPktDiscard,
       "mscAppnRtpLostFrames": mscAppnRtpLostFrames,
       "mscAppnRtpCurTxRate": mscAppnRtpCurTxRate,
       "mscAppnRtpMaxTxRate": mscAppnRtpMaxTxRate,
       "mscAppnRtpMinTxRate": mscAppnRtpMinTxRate,
       "mscAppnRtpCurRxRate": mscAppnRtpCurRxRate,
       "mscAppnRtpMaxRxRate": mscAppnRtpMaxRxRate,
       "mscAppnRtpMinRxRate": mscAppnRtpMinRxRate,
       "mscAppnRtpBurstSize": mscAppnRtpBurstSize,
       "mscAppnRtpUptime": mscAppnRtpUptime,
       "mscAppnRtpSmoothRoundTripTime": mscAppnRtpSmoothRoundTripTime,
       "mscAppnRtpLastRoundTripTime": mscAppnRtpLastRoundTripTime,
       "mscAppnRtpShortReqTimer": mscAppnRtpShortReqTimer,
       "mscAppnRtpShortReqTimeouts": mscAppnRtpShortReqTimeouts,
       "mscAppnRtpIdleTimeouts": mscAppnRtpIdleTimeouts,
       "mscAppnRtpRxInvalidSnaFrames": mscAppnRtpRxInvalidSnaFrames,
       "mscAppnRtpInSessionControlFrames": mscAppnRtpInSessionControlFrames,
       "mscAppnRtpOutSessionControlFrames": mscAppnRtpOutSessionControlFrames,
       "mscAppnDlu": mscAppnDlu,
       "mscAppnDluRowStatusTable": mscAppnDluRowStatusTable,
       "mscAppnDluRowStatusEntry": mscAppnDluRowStatusEntry,
       "mscAppnDluRowStatus": mscAppnDluRowStatus,
       "mscAppnDluComponentName": mscAppnDluComponentName,
       "mscAppnDluStorageType": mscAppnDluStorageType,
       "mscAppnDluIndex": mscAppnDluIndex,
       "mscAppnDluOperTable": mscAppnDluOperTable,
       "mscAppnDluOperEntry": mscAppnDluOperEntry,
       "mscAppnDluSscpSessActive": mscAppnDluSscpSessActive,
       "mscAppnDluPluSessActive": mscAppnDluPluSessActive,
       "mscAppnDluDlusName": mscAppnDluDlusName,
       "mscAppnDluPluName": mscAppnDluPluName,
       "mscAppnDluNauAddress": mscAppnDluNauAddress,
       "mscAppnDluSscp": mscAppnDluSscp,
       "mscAppnDluSscpRowStatusTable": mscAppnDluSscpRowStatusTable,
       "mscAppnDluSscpRowStatusEntry": mscAppnDluSscpRowStatusEntry,
       "mscAppnDluSscpRowStatus": mscAppnDluSscpRowStatus,
       "mscAppnDluSscpComponentName": mscAppnDluSscpComponentName,
       "mscAppnDluSscpStorageType": mscAppnDluSscpStorageType,
       "mscAppnDluSscpIndex": mscAppnDluSscpIndex,
       "mscAppnDluSscpStatsTable": mscAppnDluSscpStatsTable,
       "mscAppnDluSscpStatsEntry": mscAppnDluSscpStatsEntry,
       "mscAppnDluSscpRxRuSize": mscAppnDluSscpRxRuSize,
       "mscAppnDluSscpMaxTxBtuSize": mscAppnDluSscpMaxTxBtuSize,
       "mscAppnDluSscpMaxRxBtuSize": mscAppnDluSscpMaxRxBtuSize,
       "mscAppnDluSscpMaxTxPacWin": mscAppnDluSscpMaxTxPacWin,
       "mscAppnDluSscpCurTxPacWin": mscAppnDluSscpCurTxPacWin,
       "mscAppnDluSscpMaxRxPacWin": mscAppnDluSscpMaxRxPacWin,
       "mscAppnDluSscpCurRxPacWin": mscAppnDluSscpCurRxPacWin,
       "mscAppnDluSscpTxDataframes": mscAppnDluSscpTxDataframes,
       "mscAppnDluSscpTxFmdFrames": mscAppnDluSscpTxFmdFrames,
       "mscAppnDluSscpTxDataBytes": mscAppnDluSscpTxDataBytes,
       "mscAppnDluSscpRxDataFrames": mscAppnDluSscpRxDataFrames,
       "mscAppnDluSscpRxFmdFrames": mscAppnDluSscpRxFmdFrames,
       "mscAppnDluSscpRxDataBytes": mscAppnDluSscpRxDataBytes,
       "mscAppnDluSscpSidh": mscAppnDluSscpSidh,
       "mscAppnDluSscpSidl": mscAppnDluSscpSidl,
       "mscAppnDluSscpOdai": mscAppnDluSscpOdai,
       "mscAppnDluSscpLsName": mscAppnDluSscpLsName,
       "mscAppnDluUsStat": mscAppnDluUsStat,
       "mscAppnDluUsStatRowStatusTable": mscAppnDluUsStatRowStatusTable,
       "mscAppnDluUsStatRowStatusEntry": mscAppnDluUsStatRowStatusEntry,
       "mscAppnDluUsStatRowStatus": mscAppnDluUsStatRowStatus,
       "mscAppnDluUsStatComponentName": mscAppnDluUsStatComponentName,
       "mscAppnDluUsStatStorageType": mscAppnDluUsStatStorageType,
       "mscAppnDluUsStatIndex": mscAppnDluUsStatIndex,
       "mscAppnDluUsStatStatsTable": mscAppnDluUsStatStatsTable,
       "mscAppnDluUsStatStatsEntry": mscAppnDluUsStatStatsEntry,
       "mscAppnDluUsStatRxRuSize": mscAppnDluUsStatRxRuSize,
       "mscAppnDluUsStatMaxTxBtuSize": mscAppnDluUsStatMaxTxBtuSize,
       "mscAppnDluUsStatMaxRxBtuSize": mscAppnDluUsStatMaxRxBtuSize,
       "mscAppnDluUsStatMaxTxPacWin": mscAppnDluUsStatMaxTxPacWin,
       "mscAppnDluUsStatCurTxPacWin": mscAppnDluUsStatCurTxPacWin,
       "mscAppnDluUsStatMaxRxPacWin": mscAppnDluUsStatMaxRxPacWin,
       "mscAppnDluUsStatCurRxPacWin": mscAppnDluUsStatCurRxPacWin,
       "mscAppnDluUsStatTxDataframes": mscAppnDluUsStatTxDataframes,
       "mscAppnDluUsStatTxFmdFrames": mscAppnDluUsStatTxFmdFrames,
       "mscAppnDluUsStatTxDataBytes": mscAppnDluUsStatTxDataBytes,
       "mscAppnDluUsStatRxDataFrames": mscAppnDluUsStatRxDataFrames,
       "mscAppnDluUsStatRxFmdFrames": mscAppnDluUsStatRxFmdFrames,
       "mscAppnDluUsStatRxDataBytes": mscAppnDluUsStatRxDataBytes,
       "mscAppnDluUsStatSidh": mscAppnDluUsStatSidh,
       "mscAppnDluUsStatSidl": mscAppnDluUsStatSidl,
       "mscAppnDluUsStatOdai": mscAppnDluUsStatOdai,
       "mscAppnDluUsStatLsName": mscAppnDluUsStatLsName,
       "mscAppnDluDsStat": mscAppnDluDsStat,
       "mscAppnDluDsStatRowStatusTable": mscAppnDluDsStatRowStatusTable,
       "mscAppnDluDsStatRowStatusEntry": mscAppnDluDsStatRowStatusEntry,
       "mscAppnDluDsStatRowStatus": mscAppnDluDsStatRowStatus,
       "mscAppnDluDsStatComponentName": mscAppnDluDsStatComponentName,
       "mscAppnDluDsStatStorageType": mscAppnDluDsStatStorageType,
       "mscAppnDluDsStatIndex": mscAppnDluDsStatIndex,
       "mscAppnDluDsStatStatsTable": mscAppnDluDsStatStatsTable,
       "mscAppnDluDsStatStatsEntry": mscAppnDluDsStatStatsEntry,
       "mscAppnDluDsStatRxRuSize": mscAppnDluDsStatRxRuSize,
       "mscAppnDluDsStatMaxTxBtuSize": mscAppnDluDsStatMaxTxBtuSize,
       "mscAppnDluDsStatMaxRxBtuSize": mscAppnDluDsStatMaxRxBtuSize,
       "mscAppnDluDsStatMaxTxPacWin": mscAppnDluDsStatMaxTxPacWin,
       "mscAppnDluDsStatCurTxPacWin": mscAppnDluDsStatCurTxPacWin,
       "mscAppnDluDsStatMaxRxPacWin": mscAppnDluDsStatMaxRxPacWin,
       "mscAppnDluDsStatCurRxPacWin": mscAppnDluDsStatCurRxPacWin,
       "mscAppnDluDsStatTxDataframes": mscAppnDluDsStatTxDataframes,
       "mscAppnDluDsStatTxFmdFrames": mscAppnDluDsStatTxFmdFrames,
       "mscAppnDluDsStatTxDataBytes": mscAppnDluDsStatTxDataBytes,
       "mscAppnDluDsStatRxDataFrames": mscAppnDluDsStatRxDataFrames,
       "mscAppnDluDsStatRxFmdFrames": mscAppnDluDsStatRxFmdFrames,
       "mscAppnDluDsStatRxDataBytes": mscAppnDluDsStatRxDataBytes,
       "mscAppnDluDsStatSidh": mscAppnDluDsStatSidh,
       "mscAppnDluDsStatSidl": mscAppnDluDsStatSidl,
       "mscAppnDluDsStatOdai": mscAppnDluDsStatOdai,
       "mscAppnDluDsStatLsName": mscAppnDluDsStatLsName,
       "mscAppnDlus": mscAppnDlus,
       "mscAppnDlusRowStatusTable": mscAppnDlusRowStatusTable,
       "mscAppnDlusRowStatusEntry": mscAppnDlusRowStatusEntry,
       "mscAppnDlusRowStatus": mscAppnDlusRowStatus,
       "mscAppnDlusComponentName": mscAppnDlusComponentName,
       "mscAppnDlusStorageType": mscAppnDlusStorageType,
       "mscAppnDlusIndex": mscAppnDlusIndex,
       "mscAppnDlusOperTable": mscAppnDlusOperTable,
       "mscAppnDlusOperEntry": mscAppnDlusOperEntry,
       "mscAppnDlusPrimaryDlus": mscAppnDlusPrimaryDlus,
       "mscAppnDlusPipeState": mscAppnDlusPipeState,
       "mscAppnDlusActivePUs": mscAppnDlusActivePUs,
       "mscAppnDlusDlusStatTable": mscAppnDlusDlusStatTable,
       "mscAppnDlusDlusStatEntry": mscAppnDlusDlusStatEntry,
       "mscAppnDlusReqActPuTx": mscAppnDlusReqActPuTx,
       "mscAppnDlusReqActPuRspRx": mscAppnDlusReqActPuRspRx,
       "mscAppnDlusActPuRx": mscAppnDlusActPuRx,
       "mscAppnDlusActPuRspTx": mscAppnDlusActPuRspTx,
       "mscAppnDlusReqDactPuTx": mscAppnDlusReqDactPuTx,
       "mscAppnDlusReqDactPuRspRx": mscAppnDlusReqDactPuRspRx,
       "mscAppnDlusDactPuRx": mscAppnDlusDactPuRx,
       "mscAppnDlusDactPuRspTx": mscAppnDlusDactPuRspTx,
       "mscAppnDlusActLuRx": mscAppnDlusActLuRx,
       "mscAppnDlusActLuRspTx": mscAppnDlusActLuRspTx,
       "mscAppnDlusDactLuRx": mscAppnDlusDactLuRx,
       "mscAppnDlusDactLuRspTx": mscAppnDlusDactLuRspTx,
       "mscAppnDlusSscpPuMuRx": mscAppnDlusSscpPuMuRx,
       "mscAppnDlusSscpPuMuTx": mscAppnDlusSscpPuMuTx,
       "mscAppnDlusSscpLuMuRx": mscAppnDlusSscpLuMuRx,
       "mscAppnDlusSscpLuMuTx": mscAppnDlusSscpLuMuTx,
       "mscAppnDLUR": mscAppnDLUR,
       "mscAppnDLURRowStatusTable": mscAppnDLURRowStatusTable,
       "mscAppnDLURRowStatusEntry": mscAppnDLURRowStatusEntry,
       "mscAppnDLURRowStatus": mscAppnDLURRowStatus,
       "mscAppnDLURComponentName": mscAppnDLURComponentName,
       "mscAppnDLURStorageType": mscAppnDLURStorageType,
       "mscAppnDLURIndex": mscAppnDLURIndex,
       "mscAppnDLURDlurParmsTable": mscAppnDLURDlurParmsTable,
       "mscAppnDLURDlurParmsEntry": mscAppnDLURDlurParmsEntry,
       "mscAppnDLURPrimaryDefDlusName": mscAppnDLURPrimaryDefDlusName,
       "mscAppnDLURSecondaryDefDlusName": mscAppnDLURSecondaryDefDlusName,
       "mscAppnDLURDlusRetryTimeout": mscAppnDLURDlusRetryTimeout,
       "mscAppnDLURDlusRetryLimit": mscAppnDLURDlusRetryLimit,
       "mscAppnCos": mscAppnCos,
       "mscAppnCosRowStatusTable": mscAppnCosRowStatusTable,
       "mscAppnCosRowStatusEntry": mscAppnCosRowStatusEntry,
       "mscAppnCosRowStatus": mscAppnCosRowStatus,
       "mscAppnCosComponentName": mscAppnCosComponentName,
       "mscAppnCosStorageType": mscAppnCosStorageType,
       "mscAppnCosIndex": mscAppnCosIndex,
       "mscAppnCosTg": mscAppnCosTg,
       "mscAppnCosTgRowStatusTable": mscAppnCosTgRowStatusTable,
       "mscAppnCosTgRowStatusEntry": mscAppnCosTgRowStatusEntry,
       "mscAppnCosTgRowStatus": mscAppnCosTgRowStatus,
       "mscAppnCosTgComponentName": mscAppnCosTgComponentName,
       "mscAppnCosTgStorageType": mscAppnCosTgStorageType,
       "mscAppnCosTgIndex": mscAppnCosTgIndex,
       "mscAppnCosTgProvTable": mscAppnCosTgProvTable,
       "mscAppnCosTgProvEntry": mscAppnCosTgProvEntry,
       "mscAppnCosTgMinEffectiveCapacity": mscAppnCosTgMinEffectiveCapacity,
       "mscAppnCosTgMaxEffectiveCapacity": mscAppnCosTgMaxEffectiveCapacity,
       "mscAppnCosTgMinConnectCost": mscAppnCosTgMinConnectCost,
       "mscAppnCosTgMaxConnectCost": mscAppnCosTgMaxConnectCost,
       "mscAppnCosTgMinByteCost": mscAppnCosTgMinByteCost,
       "mscAppnCosTgMaxByteCost": mscAppnCosTgMaxByteCost,
       "mscAppnCosTgMinSecurity": mscAppnCosTgMinSecurity,
       "mscAppnCosTgMaxSecurity": mscAppnCosTgMaxSecurity,
       "mscAppnCosTgMinPropDelay": mscAppnCosTgMinPropDelay,
       "mscAppnCosTgMaxPropDelay": mscAppnCosTgMaxPropDelay,
       "mscAppnCosTgMinModemClass": mscAppnCosTgMinModemClass,
       "mscAppnCosTgMaxModemClass": mscAppnCosTgMaxModemClass,
       "mscAppnCosTgMinUserDefParm1": mscAppnCosTgMinUserDefParm1,
       "mscAppnCosTgMaxUserDefParm1": mscAppnCosTgMaxUserDefParm1,
       "mscAppnCosTgMinUserDefParm2": mscAppnCosTgMinUserDefParm2,
       "mscAppnCosTgMaxUserDefParm2": mscAppnCosTgMaxUserDefParm2,
       "mscAppnCosTgMinUserDefParm3": mscAppnCosTgMinUserDefParm3,
       "mscAppnCosTgMaxUserDefParm3": mscAppnCosTgMaxUserDefParm3,
       "mscAppnCosNode": mscAppnCosNode,
       "mscAppnCosNodeRowStatusTable": mscAppnCosNodeRowStatusTable,
       "mscAppnCosNodeRowStatusEntry": mscAppnCosNodeRowStatusEntry,
       "mscAppnCosNodeRowStatus": mscAppnCosNodeRowStatus,
       "mscAppnCosNodeComponentName": mscAppnCosNodeComponentName,
       "mscAppnCosNodeStorageType": mscAppnCosNodeStorageType,
       "mscAppnCosNodeIndex": mscAppnCosNodeIndex,
       "mscAppnCosNodeProvTable": mscAppnCosNodeProvTable,
       "mscAppnCosNodeProvEntry": mscAppnCosNodeProvEntry,
       "mscAppnCosNodeMinRouteAddResistance": mscAppnCosNodeMinRouteAddResistance,
       "mscAppnCosNodeMaxRouteAddResistance": mscAppnCosNodeMaxRouteAddResistance,
       "mscAppnCosNodeMinStatus": mscAppnCosNodeMinStatus,
       "mscAppnCosNodeMaxStatus": mscAppnCosNodeMaxStatus,
       "mscAppnCosProvTable": mscAppnCosProvTable,
       "mscAppnCosProvEntry": mscAppnCosProvEntry,
       "mscAppnCosTransmissionPriority": mscAppnCosTransmissionPriority,
       "mscAppnFrSvc": mscAppnFrSvc,
       "mscAppnFrSvcRowStatusTable": mscAppnFrSvcRowStatusTable,
       "mscAppnFrSvcRowStatusEntry": mscAppnFrSvcRowStatusEntry,
       "mscAppnFrSvcRowStatus": mscAppnFrSvcRowStatus,
       "mscAppnFrSvcComponentName": mscAppnFrSvcComponentName,
       "mscAppnFrSvcStorageType": mscAppnFrSvcStorageType,
       "mscAppnFrSvcIndex": mscAppnFrSvcIndex,
       "mscAppnFrSvcBanTable": mscAppnFrSvcBanTable,
       "mscAppnFrSvcBanEntry": mscAppnFrSvcBanEntry,
       "mscAppnFrSvcBanLocalMac": mscAppnFrSvcBanLocalMac,
       "mscAppnFrSvcBanLocalSap": mscAppnFrSvcBanLocalSap,
       "mscAppnFrSvcProvisionedTable": mscAppnFrSvcProvisionedTable,
       "mscAppnFrSvcProvisionedEntry": mscAppnFrSvcProvisionedEntry,
       "mscAppnFrSvcMaximumFrameRelaySvcs": mscAppnFrSvcMaximumFrameRelaySvcs,
       "mscAppnFrSvcRateEnforcement": mscAppnFrSvcRateEnforcement,
       "mscAppnFrSvcMaximumCir": mscAppnFrSvcMaximumCir,
       "mscAppnFrSvcOperationalTable": mscAppnFrSvcOperationalTable,
       "mscAppnFrSvcOperationalEntry": mscAppnFrSvcOperationalEntry,
       "mscAppnFrSvcCurrentNumberOfSvcCalls": mscAppnFrSvcCurrentNumberOfSvcCalls,
       "mscAppnProcessParmsTable": mscAppnProcessParmsTable,
       "mscAppnProcessParmsEntry": mscAppnProcessParmsEntry,
       "mscAppnLogicalProcessor": mscAppnLogicalProcessor,
       "mscAppnMaximumSvcs": mscAppnMaximumSvcs,
       "mscAppnMaximumLinkStations": mscAppnMaximumLinkStations,
       "mscAppnControlPointCreateParmsTable": mscAppnControlPointCreateParmsTable,
       "mscAppnControlPointCreateParmsEntry": mscAppnControlPointCreateParmsEntry,
       "mscAppnFqCpName": mscAppnFqCpName,
       "mscAppnBlockNumber": mscAppnBlockNumber,
       "mscAppnIdNumber": mscAppnIdNumber,
       "mscAppnRouteAdditionResistance": mscAppnRouteAdditionResistance,
       "mscAppnFeatures": mscAppnFeatures,
       "mscAppnMaximumLocates": mscAppnMaximumLocates,
       "mscAppnMaximumDirectorySize": mscAppnMaximumDirectorySize,
       "mscAppnMdsTxAlertQueueSize": mscAppnMdsTxAlertQueueSize,
       "mscAppnTreeCacheSize": mscAppnTreeCacheSize,
       "mscAppnTreeCacheUseLimit": mscAppnTreeCacheUseLimit,
       "mscAppnMaximumTopologyNodes": mscAppnMaximumTopologyNodes,
       "mscAppnMaximumTopologyTgs": mscAppnMaximumTopologyTgs,
       "mscAppnMaximumIsrSessions": mscAppnMaximumIsrSessions,
       "mscAppnIsrUpperCongestionThreshold": mscAppnIsrUpperCongestionThreshold,
       "mscAppnIsrLowerCongestionThreshold": mscAppnIsrLowerCongestionThreshold,
       "mscAppnIsrMaxRuSize": mscAppnIsrMaxRuSize,
       "mscAppnIsrRxPacingWindow": mscAppnIsrRxPacingWindow,
       "mscAppnLocateTimeout": mscAppnLocateTimeout,
       "mscAppnHprSupport": mscAppnHprSupport,
       "mscAppnDlurSupport": mscAppnDlurSupport,
       "mscAppnStateTable": mscAppnStateTable,
       "mscAppnStateEntry": mscAppnStateEntry,
       "mscAppnAdminState": mscAppnAdminState,
       "mscAppnOperationalState": mscAppnOperationalState,
       "mscAppnUsageState": mscAppnUsageState,
       "mscAppnOperationalTable": mscAppnOperationalTable,
       "mscAppnOperationalEntry": mscAppnOperationalEntry,
       "mscAppnUpTime": mscAppnUpTime,
       "mscAppnHeapSpaceLimit": mscAppnHeapSpaceLimit,
       "mscAppnHeapSpaceCurrent": mscAppnHeapSpaceCurrent,
       "mscAppnMemWarningThreshold": mscAppnMemWarningThreshold,
       "mscAppnMemCriticalThreshold": mscAppnMemCriticalThreshold,
       "mscAppnNnFunctionsSupported": mscAppnNnFunctionsSupported,
       "mscAppnGeneralFunctionsSupported": mscAppnGeneralFunctionsSupported,
       "mscAppnStatus": mscAppnStatus,
       "mscAppnFlowReductionSequenceNumber": mscAppnFlowReductionSequenceNumber,
       "mscAppnResourceSequenceNumber": mscAppnResourceSequenceNumber,
       "mscAppnDefinedLsGoodXids": mscAppnDefinedLsGoodXids,
       "mscAppnDefinedLsBadXids": mscAppnDefinedLsBadXids,
       "mscAppnDynamicLsGoodXids": mscAppnDynamicLsGoodXids,
       "mscAppnDynamicLsBadXids": mscAppnDynamicLsBadXids,
       "mscAppnActiveSvcs": mscAppnActiveSvcs,
       "mscAppnActiveLinkStations": mscAppnActiveLinkStations,
       "appnMIB": appnMIB,
       "appnGroup": appnGroup,
       "appnGroupCA": appnGroupCA,
       "appnGroupCA02": appnGroupCA02,
       "appnGroupCA02DevelopmentLoad": appnGroupCA02DevelopmentLoad,
       "appnGroupCA0214": appnGroupCA0214,
       "appnGroupCA0214A": appnGroupCA0214A,
       "appnCapabilities": appnCapabilities,
       "appnCapabilitiesCA": appnCapabilitiesCA,
       "appnCapabilitiesCA02": appnCapabilitiesCA02,
       "appnCapabilitiesCA02DevelopmentLoad": appnCapabilitiesCA02DevelopmentLoad,
       "appnCapabilitiesCA0214": appnCapabilitiesCA0214,
       "appnCapabilitiesCA0214A": appnCapabilitiesCA0214A}
)
