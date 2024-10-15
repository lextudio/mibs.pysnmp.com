# SNMP MIB module (Nortel-Magellan-Passport-AppnMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-AppnMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:14 2024
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
 PassportCounter64,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "PassportCounter64",
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
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
    "DashedHexString",
    "DigitString",
    "EnterpriseDateAndTime",
    "Hex",
    "HexString",
    "Link",
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

_Appn_ObjectIdentity = ObjectIdentity
appn = _Appn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110)
)
_AppnRowStatusTable_Object = MibTable
appnRowStatusTable = _AppnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 1)
)
if mibBuilder.loadTexts:
    appnRowStatusTable.setStatus("mandatory")
_AppnRowStatusEntry_Object = MibTableRow
appnRowStatusEntry = _AppnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 1, 1)
)
appnRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
)
if mibBuilder.loadTexts:
    appnRowStatusEntry.setStatus("mandatory")
_AppnRowStatus_Type = RowStatus
_AppnRowStatus_Object = MibTableColumn
appnRowStatus = _AppnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 1, 1, 1),
    _AppnRowStatus_Type()
)
appnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnRowStatus.setStatus("mandatory")
_AppnComponentName_Type = DisplayString
_AppnComponentName_Object = MibTableColumn
appnComponentName = _AppnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 1, 1, 2),
    _AppnComponentName_Type()
)
appnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnComponentName.setStatus("mandatory")
_AppnStorageType_Type = StorageType
_AppnStorageType_Object = MibTableColumn
appnStorageType = _AppnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 1, 1, 4),
    _AppnStorageType_Type()
)
appnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnStorageType.setStatus("mandatory")


class _AppnIndex_Type(AsciiStringIndex):
    """Custom type appnIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppnIndex_Type.__name__ = "AsciiStringIndex"
_AppnIndex_Object = MibTableColumn
appnIndex = _AppnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 1, 1, 10),
    _AppnIndex_Type()
)
appnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnIndex.setStatus("mandatory")
_AppnDna_ObjectIdentity = ObjectIdentity
appnDna = _AppnDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2)
)
_AppnDnaRowStatusTable_Object = MibTable
appnDnaRowStatusTable = _AppnDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 1)
)
if mibBuilder.loadTexts:
    appnDnaRowStatusTable.setStatus("mandatory")
_AppnDnaRowStatusEntry_Object = MibTableRow
appnDnaRowStatusEntry = _AppnDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 1, 1)
)
appnDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDnaIndex"),
)
if mibBuilder.loadTexts:
    appnDnaRowStatusEntry.setStatus("mandatory")
_AppnDnaRowStatus_Type = RowStatus
_AppnDnaRowStatus_Object = MibTableColumn
appnDnaRowStatus = _AppnDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 1, 1, 1),
    _AppnDnaRowStatus_Type()
)
appnDnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDnaRowStatus.setStatus("mandatory")
_AppnDnaComponentName_Type = DisplayString
_AppnDnaComponentName_Object = MibTableColumn
appnDnaComponentName = _AppnDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 1, 1, 2),
    _AppnDnaComponentName_Type()
)
appnDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDnaComponentName.setStatus("mandatory")
_AppnDnaStorageType_Type = StorageType
_AppnDnaStorageType_Object = MibTableColumn
appnDnaStorageType = _AppnDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 1, 1, 4),
    _AppnDnaStorageType_Type()
)
appnDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDnaStorageType.setStatus("mandatory")
_AppnDnaIndex_Type = NonReplicated
_AppnDnaIndex_Object = MibTableColumn
appnDnaIndex = _AppnDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 1, 1, 10),
    _AppnDnaIndex_Type()
)
appnDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnDnaIndex.setStatus("mandatory")
_AppnDnaHgM_ObjectIdentity = ObjectIdentity
appnDnaHgM = _AppnDnaHgM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 2)
)
_AppnDnaHgMRowStatusTable_Object = MibTable
appnDnaHgMRowStatusTable = _AppnDnaHgMRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 2, 1)
)
if mibBuilder.loadTexts:
    appnDnaHgMRowStatusTable.setStatus("mandatory")
_AppnDnaHgMRowStatusEntry_Object = MibTableRow
appnDnaHgMRowStatusEntry = _AppnDnaHgMRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 2, 1, 1)
)
appnDnaHgMRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDnaIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDnaHgMIndex"),
)
if mibBuilder.loadTexts:
    appnDnaHgMRowStatusEntry.setStatus("mandatory")
_AppnDnaHgMRowStatus_Type = RowStatus
_AppnDnaHgMRowStatus_Object = MibTableColumn
appnDnaHgMRowStatus = _AppnDnaHgMRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 2, 1, 1, 1),
    _AppnDnaHgMRowStatus_Type()
)
appnDnaHgMRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDnaHgMRowStatus.setStatus("mandatory")
_AppnDnaHgMComponentName_Type = DisplayString
_AppnDnaHgMComponentName_Object = MibTableColumn
appnDnaHgMComponentName = _AppnDnaHgMComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 2, 1, 1, 2),
    _AppnDnaHgMComponentName_Type()
)
appnDnaHgMComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDnaHgMComponentName.setStatus("mandatory")
_AppnDnaHgMStorageType_Type = StorageType
_AppnDnaHgMStorageType_Object = MibTableColumn
appnDnaHgMStorageType = _AppnDnaHgMStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 2, 1, 1, 4),
    _AppnDnaHgMStorageType_Type()
)
appnDnaHgMStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDnaHgMStorageType.setStatus("mandatory")
_AppnDnaHgMIndex_Type = NonReplicated
_AppnDnaHgMIndex_Object = MibTableColumn
appnDnaHgMIndex = _AppnDnaHgMIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 2, 1, 1, 10),
    _AppnDnaHgMIndex_Type()
)
appnDnaHgMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnDnaHgMIndex.setStatus("mandatory")
_AppnDnaHgMHgAddr_ObjectIdentity = ObjectIdentity
appnDnaHgMHgAddr = _AppnDnaHgMHgAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 2, 2)
)
_AppnDnaHgMHgAddrRowStatusTable_Object = MibTable
appnDnaHgMHgAddrRowStatusTable = _AppnDnaHgMHgAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    appnDnaHgMHgAddrRowStatusTable.setStatus("mandatory")
_AppnDnaHgMHgAddrRowStatusEntry_Object = MibTableRow
appnDnaHgMHgAddrRowStatusEntry = _AppnDnaHgMHgAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 2, 2, 1, 1)
)
appnDnaHgMHgAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDnaIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDnaHgMIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDnaHgMHgAddrIndex"),
)
if mibBuilder.loadTexts:
    appnDnaHgMHgAddrRowStatusEntry.setStatus("mandatory")
_AppnDnaHgMHgAddrRowStatus_Type = RowStatus
_AppnDnaHgMHgAddrRowStatus_Object = MibTableColumn
appnDnaHgMHgAddrRowStatus = _AppnDnaHgMHgAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 2, 2, 1, 1, 1),
    _AppnDnaHgMHgAddrRowStatus_Type()
)
appnDnaHgMHgAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDnaHgMHgAddrRowStatus.setStatus("mandatory")
_AppnDnaHgMHgAddrComponentName_Type = DisplayString
_AppnDnaHgMHgAddrComponentName_Object = MibTableColumn
appnDnaHgMHgAddrComponentName = _AppnDnaHgMHgAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 2, 2, 1, 1, 2),
    _AppnDnaHgMHgAddrComponentName_Type()
)
appnDnaHgMHgAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDnaHgMHgAddrComponentName.setStatus("mandatory")
_AppnDnaHgMHgAddrStorageType_Type = StorageType
_AppnDnaHgMHgAddrStorageType_Object = MibTableColumn
appnDnaHgMHgAddrStorageType = _AppnDnaHgMHgAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 2, 2, 1, 1, 4),
    _AppnDnaHgMHgAddrStorageType_Type()
)
appnDnaHgMHgAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDnaHgMHgAddrStorageType.setStatus("mandatory")


class _AppnDnaHgMHgAddrIndex_Type(Integer32):
    """Custom type appnDnaHgMHgAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AppnDnaHgMHgAddrIndex_Type.__name__ = "Integer32"
_AppnDnaHgMHgAddrIndex_Object = MibTableColumn
appnDnaHgMHgAddrIndex = _AppnDnaHgMHgAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 2, 2, 1, 1, 10),
    _AppnDnaHgMHgAddrIndex_Type()
)
appnDnaHgMHgAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnDnaHgMHgAddrIndex.setStatus("mandatory")
_AppnDnaHgMHgAddrAddrTable_Object = MibTable
appnDnaHgMHgAddrAddrTable = _AppnDnaHgMHgAddrAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 2, 2, 10)
)
if mibBuilder.loadTexts:
    appnDnaHgMHgAddrAddrTable.setStatus("mandatory")
_AppnDnaHgMHgAddrAddrEntry_Object = MibTableRow
appnDnaHgMHgAddrAddrEntry = _AppnDnaHgMHgAddrAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 2, 2, 10, 1)
)
appnDnaHgMHgAddrAddrEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDnaIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDnaHgMIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDnaHgMHgAddrIndex"),
)
if mibBuilder.loadTexts:
    appnDnaHgMHgAddrAddrEntry.setStatus("mandatory")


class _AppnDnaHgMHgAddrNumberingPlanIndicator_Type(Integer32):
    """Custom type appnDnaHgMHgAddrNumberingPlanIndicator based on Integer32"""
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


_AppnDnaHgMHgAddrNumberingPlanIndicator_Type.__name__ = "Integer32"
_AppnDnaHgMHgAddrNumberingPlanIndicator_Object = MibTableColumn
appnDnaHgMHgAddrNumberingPlanIndicator = _AppnDnaHgMHgAddrNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 2, 2, 10, 1, 1),
    _AppnDnaHgMHgAddrNumberingPlanIndicator_Type()
)
appnDnaHgMHgAddrNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDnaHgMHgAddrNumberingPlanIndicator.setStatus("mandatory")


class _AppnDnaHgMHgAddrDataNetworkAddress_Type(DigitString):
    """Custom type appnDnaHgMHgAddrDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AppnDnaHgMHgAddrDataNetworkAddress_Type.__name__ = "DigitString"
_AppnDnaHgMHgAddrDataNetworkAddress_Object = MibTableColumn
appnDnaHgMHgAddrDataNetworkAddress = _AppnDnaHgMHgAddrDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 2, 2, 10, 1, 2),
    _AppnDnaHgMHgAddrDataNetworkAddress_Type()
)
appnDnaHgMHgAddrDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDnaHgMHgAddrDataNetworkAddress.setStatus("mandatory")
_AppnDnaHgMIfTable_Object = MibTable
appnDnaHgMIfTable = _AppnDnaHgMIfTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 2, 10)
)
if mibBuilder.loadTexts:
    appnDnaHgMIfTable.setStatus("mandatory")
_AppnDnaHgMIfEntry_Object = MibTableRow
appnDnaHgMIfEntry = _AppnDnaHgMIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 2, 10, 1)
)
appnDnaHgMIfEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDnaIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDnaHgMIndex"),
)
if mibBuilder.loadTexts:
    appnDnaHgMIfEntry.setStatus("mandatory")


class _AppnDnaHgMAvailabilityUpdateThreshold_Type(Unsigned32):
    """Custom type appnDnaHgMAvailabilityUpdateThreshold based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AppnDnaHgMAvailabilityUpdateThreshold_Type.__name__ = "Unsigned32"
_AppnDnaHgMAvailabilityUpdateThreshold_Object = MibTableColumn
appnDnaHgMAvailabilityUpdateThreshold = _AppnDnaHgMAvailabilityUpdateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 2, 10, 1, 1),
    _AppnDnaHgMAvailabilityUpdateThreshold_Type()
)
appnDnaHgMAvailabilityUpdateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDnaHgMAvailabilityUpdateThreshold.setStatus("mandatory")
_AppnDnaHgMOpTable_Object = MibTable
appnDnaHgMOpTable = _AppnDnaHgMOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 2, 11)
)
if mibBuilder.loadTexts:
    appnDnaHgMOpTable.setStatus("mandatory")
_AppnDnaHgMOpEntry_Object = MibTableRow
appnDnaHgMOpEntry = _AppnDnaHgMOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 2, 11, 1)
)
appnDnaHgMOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDnaIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDnaHgMIndex"),
)
if mibBuilder.loadTexts:
    appnDnaHgMOpEntry.setStatus("mandatory")


class _AppnDnaHgMMaxAvailableChannels_Type(Unsigned32):
    """Custom type appnDnaHgMMaxAvailableChannels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AppnDnaHgMMaxAvailableChannels_Type.__name__ = "Unsigned32"
_AppnDnaHgMMaxAvailableChannels_Object = MibTableColumn
appnDnaHgMMaxAvailableChannels = _AppnDnaHgMMaxAvailableChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 2, 11, 1, 1),
    _AppnDnaHgMMaxAvailableChannels_Type()
)
appnDnaHgMMaxAvailableChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDnaHgMMaxAvailableChannels.setStatus("mandatory")


class _AppnDnaHgMAvailableChannels_Type(Unsigned32):
    """Custom type appnDnaHgMAvailableChannels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AppnDnaHgMAvailableChannels_Type.__name__ = "Unsigned32"
_AppnDnaHgMAvailableChannels_Object = MibTableColumn
appnDnaHgMAvailableChannels = _AppnDnaHgMAvailableChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 2, 11, 1, 2),
    _AppnDnaHgMAvailableChannels_Type()
)
appnDnaHgMAvailableChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDnaHgMAvailableChannels.setStatus("mandatory")


class _AppnDnaHgMAvailabilityDelta_Type(Integer32):
    """Custom type appnDnaHgMAvailabilityDelta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4096, 4096),
    )


_AppnDnaHgMAvailabilityDelta_Type.__name__ = "Integer32"
_AppnDnaHgMAvailabilityDelta_Object = MibTableColumn
appnDnaHgMAvailabilityDelta = _AppnDnaHgMAvailabilityDelta_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 2, 11, 1, 3),
    _AppnDnaHgMAvailabilityDelta_Type()
)
appnDnaHgMAvailabilityDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDnaHgMAvailabilityDelta.setStatus("mandatory")
_AppnDnaCug_ObjectIdentity = ObjectIdentity
appnDnaCug = _AppnDnaCug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 3)
)
_AppnDnaCugRowStatusTable_Object = MibTable
appnDnaCugRowStatusTable = _AppnDnaCugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 3, 1)
)
if mibBuilder.loadTexts:
    appnDnaCugRowStatusTable.setStatus("mandatory")
_AppnDnaCugRowStatusEntry_Object = MibTableRow
appnDnaCugRowStatusEntry = _AppnDnaCugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 3, 1, 1)
)
appnDnaCugRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDnaIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDnaCugIndex"),
)
if mibBuilder.loadTexts:
    appnDnaCugRowStatusEntry.setStatus("mandatory")
_AppnDnaCugRowStatus_Type = RowStatus
_AppnDnaCugRowStatus_Object = MibTableColumn
appnDnaCugRowStatus = _AppnDnaCugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 3, 1, 1, 1),
    _AppnDnaCugRowStatus_Type()
)
appnDnaCugRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDnaCugRowStatus.setStatus("mandatory")
_AppnDnaCugComponentName_Type = DisplayString
_AppnDnaCugComponentName_Object = MibTableColumn
appnDnaCugComponentName = _AppnDnaCugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 3, 1, 1, 2),
    _AppnDnaCugComponentName_Type()
)
appnDnaCugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDnaCugComponentName.setStatus("mandatory")
_AppnDnaCugStorageType_Type = StorageType
_AppnDnaCugStorageType_Object = MibTableColumn
appnDnaCugStorageType = _AppnDnaCugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 3, 1, 1, 4),
    _AppnDnaCugStorageType_Type()
)
appnDnaCugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDnaCugStorageType.setStatus("mandatory")


class _AppnDnaCugIndex_Type(Integer32):
    """Custom type appnDnaCugIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AppnDnaCugIndex_Type.__name__ = "Integer32"
_AppnDnaCugIndex_Object = MibTableColumn
appnDnaCugIndex = _AppnDnaCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 3, 1, 1, 10),
    _AppnDnaCugIndex_Type()
)
appnDnaCugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnDnaCugIndex.setStatus("mandatory")
_AppnDnaCugCugOptionsTable_Object = MibTable
appnDnaCugCugOptionsTable = _AppnDnaCugCugOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 3, 10)
)
if mibBuilder.loadTexts:
    appnDnaCugCugOptionsTable.setStatus("mandatory")
_AppnDnaCugCugOptionsEntry_Object = MibTableRow
appnDnaCugCugOptionsEntry = _AppnDnaCugCugOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 3, 10, 1)
)
appnDnaCugCugOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDnaIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDnaCugIndex"),
)
if mibBuilder.loadTexts:
    appnDnaCugCugOptionsEntry.setStatus("mandatory")


class _AppnDnaCugType_Type(Integer32):
    """Custom type appnDnaCugType based on Integer32"""
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


_AppnDnaCugType_Type.__name__ = "Integer32"
_AppnDnaCugType_Object = MibTableColumn
appnDnaCugType = _AppnDnaCugType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 3, 10, 1, 1),
    _AppnDnaCugType_Type()
)
appnDnaCugType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDnaCugType.setStatus("mandatory")


class _AppnDnaCugDnic_Type(DigitString):
    """Custom type appnDnaCugDnic based on DigitString"""
    defaultHexValue = "30303030"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AppnDnaCugDnic_Type.__name__ = "DigitString"
_AppnDnaCugDnic_Object = MibTableColumn
appnDnaCugDnic = _AppnDnaCugDnic_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 3, 10, 1, 2),
    _AppnDnaCugDnic_Type()
)
appnDnaCugDnic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDnaCugDnic.setStatus("mandatory")


class _AppnDnaCugInterlockCode_Type(Unsigned32):
    """Custom type appnDnaCugInterlockCode based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnDnaCugInterlockCode_Type.__name__ = "Unsigned32"
_AppnDnaCugInterlockCode_Object = MibTableColumn
appnDnaCugInterlockCode = _AppnDnaCugInterlockCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 3, 10, 1, 3),
    _AppnDnaCugInterlockCode_Type()
)
appnDnaCugInterlockCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDnaCugInterlockCode.setStatus("mandatory")


class _AppnDnaCugPreferential_Type(Integer32):
    """Custom type appnDnaCugPreferential based on Integer32"""
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


_AppnDnaCugPreferential_Type.__name__ = "Integer32"
_AppnDnaCugPreferential_Object = MibTableColumn
appnDnaCugPreferential = _AppnDnaCugPreferential_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 3, 10, 1, 4),
    _AppnDnaCugPreferential_Type()
)
appnDnaCugPreferential.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDnaCugPreferential.setStatus("mandatory")


class _AppnDnaCugOutCalls_Type(Integer32):
    """Custom type appnDnaCugOutCalls based on Integer32"""
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


_AppnDnaCugOutCalls_Type.__name__ = "Integer32"
_AppnDnaCugOutCalls_Object = MibTableColumn
appnDnaCugOutCalls = _AppnDnaCugOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 3, 10, 1, 5),
    _AppnDnaCugOutCalls_Type()
)
appnDnaCugOutCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDnaCugOutCalls.setStatus("mandatory")


class _AppnDnaCugIncCalls_Type(Integer32):
    """Custom type appnDnaCugIncCalls based on Integer32"""
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


_AppnDnaCugIncCalls_Type.__name__ = "Integer32"
_AppnDnaCugIncCalls_Object = MibTableColumn
appnDnaCugIncCalls = _AppnDnaCugIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 3, 10, 1, 6),
    _AppnDnaCugIncCalls_Type()
)
appnDnaCugIncCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDnaCugIncCalls.setStatus("mandatory")


class _AppnDnaCugPrivileged_Type(Integer32):
    """Custom type appnDnaCugPrivileged based on Integer32"""
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


_AppnDnaCugPrivileged_Type.__name__ = "Integer32"
_AppnDnaCugPrivileged_Object = MibTableColumn
appnDnaCugPrivileged = _AppnDnaCugPrivileged_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 3, 10, 1, 7),
    _AppnDnaCugPrivileged_Type()
)
appnDnaCugPrivileged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDnaCugPrivileged.setStatus("mandatory")
_AppnDnaAddressTable_Object = MibTable
appnDnaAddressTable = _AppnDnaAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 10)
)
if mibBuilder.loadTexts:
    appnDnaAddressTable.setStatus("mandatory")
_AppnDnaAddressEntry_Object = MibTableRow
appnDnaAddressEntry = _AppnDnaAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 10, 1)
)
appnDnaAddressEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDnaIndex"),
)
if mibBuilder.loadTexts:
    appnDnaAddressEntry.setStatus("mandatory")


class _AppnDnaNumberingPlanIndicator_Type(Integer32):
    """Custom type appnDnaNumberingPlanIndicator based on Integer32"""
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


_AppnDnaNumberingPlanIndicator_Type.__name__ = "Integer32"
_AppnDnaNumberingPlanIndicator_Object = MibTableColumn
appnDnaNumberingPlanIndicator = _AppnDnaNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 10, 1, 1),
    _AppnDnaNumberingPlanIndicator_Type()
)
appnDnaNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDnaNumberingPlanIndicator.setStatus("mandatory")


class _AppnDnaDataNetworkAddress_Type(DigitString):
    """Custom type appnDnaDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AppnDnaDataNetworkAddress_Type.__name__ = "DigitString"
_AppnDnaDataNetworkAddress_Object = MibTableColumn
appnDnaDataNetworkAddress = _AppnDnaDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 10, 1, 2),
    _AppnDnaDataNetworkAddress_Type()
)
appnDnaDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDnaDataNetworkAddress.setStatus("mandatory")
_AppnDnaOutgoingOptionsTable_Object = MibTable
appnDnaOutgoingOptionsTable = _AppnDnaOutgoingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 12)
)
if mibBuilder.loadTexts:
    appnDnaOutgoingOptionsTable.setStatus("mandatory")
_AppnDnaOutgoingOptionsEntry_Object = MibTableRow
appnDnaOutgoingOptionsEntry = _AppnDnaOutgoingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 12, 1)
)
appnDnaOutgoingOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDnaIndex"),
)
if mibBuilder.loadTexts:
    appnDnaOutgoingOptionsEntry.setStatus("mandatory")


class _AppnDnaOutDefaultPriority_Type(Integer32):
    """Custom type appnDnaOutDefaultPriority based on Integer32"""
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


_AppnDnaOutDefaultPriority_Type.__name__ = "Integer32"
_AppnDnaOutDefaultPriority_Object = MibTableColumn
appnDnaOutDefaultPriority = _AppnDnaOutDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 12, 1, 7),
    _AppnDnaOutDefaultPriority_Type()
)
appnDnaOutDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDnaOutDefaultPriority.setStatus("mandatory")


class _AppnDnaOutDefaultPathSensitivity_Type(Integer32):
    """Custom type appnDnaOutDefaultPathSensitivity based on Integer32"""
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


_AppnDnaOutDefaultPathSensitivity_Type.__name__ = "Integer32"
_AppnDnaOutDefaultPathSensitivity_Object = MibTableColumn
appnDnaOutDefaultPathSensitivity = _AppnDnaOutDefaultPathSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 12, 1, 11),
    _AppnDnaOutDefaultPathSensitivity_Type()
)
appnDnaOutDefaultPathSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDnaOutDefaultPathSensitivity.setStatus("obsolete")


class _AppnDnaOutPathSensitivityOverRide_Type(Integer32):
    """Custom type appnDnaOutPathSensitivityOverRide based on Integer32"""
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


_AppnDnaOutPathSensitivityOverRide_Type.__name__ = "Integer32"
_AppnDnaOutPathSensitivityOverRide_Object = MibTableColumn
appnDnaOutPathSensitivityOverRide = _AppnDnaOutPathSensitivityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 12, 1, 12),
    _AppnDnaOutPathSensitivityOverRide_Type()
)
appnDnaOutPathSensitivityOverRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDnaOutPathSensitivityOverRide.setStatus("obsolete")


class _AppnDnaOutDefaultPathReliability_Type(Integer32):
    """Custom type appnDnaOutDefaultPathReliability based on Integer32"""
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


_AppnDnaOutDefaultPathReliability_Type.__name__ = "Integer32"
_AppnDnaOutDefaultPathReliability_Object = MibTableColumn
appnDnaOutDefaultPathReliability = _AppnDnaOutDefaultPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 12, 1, 14),
    _AppnDnaOutDefaultPathReliability_Type()
)
appnDnaOutDefaultPathReliability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDnaOutDefaultPathReliability.setStatus("mandatory")


class _AppnDnaOutAccess_Type(Integer32):
    """Custom type appnDnaOutAccess based on Integer32"""
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


_AppnDnaOutAccess_Type.__name__ = "Integer32"
_AppnDnaOutAccess_Object = MibTableColumn
appnDnaOutAccess = _AppnDnaOutAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 12, 1, 17),
    _AppnDnaOutAccess_Type()
)
appnDnaOutAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDnaOutAccess.setStatus("mandatory")


class _AppnDnaDefaultTransferPriority_Type(Integer32):
    """Custom type appnDnaDefaultTransferPriority based on Integer32"""
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


_AppnDnaDefaultTransferPriority_Type.__name__ = "Integer32"
_AppnDnaDefaultTransferPriority_Object = MibTableColumn
appnDnaDefaultTransferPriority = _AppnDnaDefaultTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 12, 1, 18),
    _AppnDnaDefaultTransferPriority_Type()
)
appnDnaDefaultTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDnaDefaultTransferPriority.setStatus("mandatory")


class _AppnDnaTransferPriorityOverRide_Type(Integer32):
    """Custom type appnDnaTransferPriorityOverRide based on Integer32"""
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


_AppnDnaTransferPriorityOverRide_Type.__name__ = "Integer32"
_AppnDnaTransferPriorityOverRide_Object = MibTableColumn
appnDnaTransferPriorityOverRide = _AppnDnaTransferPriorityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 12, 1, 19),
    _AppnDnaTransferPriorityOverRide_Type()
)
appnDnaTransferPriorityOverRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDnaTransferPriorityOverRide.setStatus("mandatory")
_AppnDnaIncomingOptionsTable_Object = MibTable
appnDnaIncomingOptionsTable = _AppnDnaIncomingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 13)
)
if mibBuilder.loadTexts:
    appnDnaIncomingOptionsTable.setStatus("mandatory")
_AppnDnaIncomingOptionsEntry_Object = MibTableRow
appnDnaIncomingOptionsEntry = _AppnDnaIncomingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 13, 1)
)
appnDnaIncomingOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDnaIndex"),
)
if mibBuilder.loadTexts:
    appnDnaIncomingOptionsEntry.setStatus("mandatory")


class _AppnDnaIncAccess_Type(Integer32):
    """Custom type appnDnaIncAccess based on Integer32"""
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


_AppnDnaIncAccess_Type.__name__ = "Integer32"
_AppnDnaIncAccess_Object = MibTableColumn
appnDnaIncAccess = _AppnDnaIncAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 13, 1, 9),
    _AppnDnaIncAccess_Type()
)
appnDnaIncAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDnaIncAccess.setStatus("mandatory")
_AppnDnaCallOptionsTable_Object = MibTable
appnDnaCallOptionsTable = _AppnDnaCallOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 14)
)
if mibBuilder.loadTexts:
    appnDnaCallOptionsTable.setStatus("mandatory")
_AppnDnaCallOptionsEntry_Object = MibTableRow
appnDnaCallOptionsEntry = _AppnDnaCallOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 14, 1)
)
appnDnaCallOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDnaIndex"),
)
if mibBuilder.loadTexts:
    appnDnaCallOptionsEntry.setStatus("mandatory")


class _AppnDnaDefaultRecvFrmNetworkThruputClass_Type(Unsigned32):
    """Custom type appnDnaDefaultRecvFrmNetworkThruputClass based on Unsigned32"""
    defaultValue = 13

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AppnDnaDefaultRecvFrmNetworkThruputClass_Type.__name__ = "Unsigned32"
_AppnDnaDefaultRecvFrmNetworkThruputClass_Object = MibTableColumn
appnDnaDefaultRecvFrmNetworkThruputClass = _AppnDnaDefaultRecvFrmNetworkThruputClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 14, 1, 5),
    _AppnDnaDefaultRecvFrmNetworkThruputClass_Type()
)
appnDnaDefaultRecvFrmNetworkThruputClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDnaDefaultRecvFrmNetworkThruputClass.setStatus("mandatory")


class _AppnDnaDefaultSendToNetworkThruputClass_Type(Unsigned32):
    """Custom type appnDnaDefaultSendToNetworkThruputClass based on Unsigned32"""
    defaultValue = 13

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AppnDnaDefaultSendToNetworkThruputClass_Type.__name__ = "Unsigned32"
_AppnDnaDefaultSendToNetworkThruputClass_Object = MibTableColumn
appnDnaDefaultSendToNetworkThruputClass = _AppnDnaDefaultSendToNetworkThruputClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 14, 1, 6),
    _AppnDnaDefaultSendToNetworkThruputClass_Type()
)
appnDnaDefaultSendToNetworkThruputClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDnaDefaultSendToNetworkThruputClass.setStatus("mandatory")


class _AppnDnaDefaultRecvFrmNetworkWindowSize_Type(Unsigned32):
    """Custom type appnDnaDefaultRecvFrmNetworkWindowSize based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AppnDnaDefaultRecvFrmNetworkWindowSize_Type.__name__ = "Unsigned32"
_AppnDnaDefaultRecvFrmNetworkWindowSize_Object = MibTableColumn
appnDnaDefaultRecvFrmNetworkWindowSize = _AppnDnaDefaultRecvFrmNetworkWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 14, 1, 7),
    _AppnDnaDefaultRecvFrmNetworkWindowSize_Type()
)
appnDnaDefaultRecvFrmNetworkWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDnaDefaultRecvFrmNetworkWindowSize.setStatus("mandatory")


class _AppnDnaDefaultSendToNetworkWindowSize_Type(Unsigned32):
    """Custom type appnDnaDefaultSendToNetworkWindowSize based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AppnDnaDefaultSendToNetworkWindowSize_Type.__name__ = "Unsigned32"
_AppnDnaDefaultSendToNetworkWindowSize_Object = MibTableColumn
appnDnaDefaultSendToNetworkWindowSize = _AppnDnaDefaultSendToNetworkWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 14, 1, 8),
    _AppnDnaDefaultSendToNetworkWindowSize_Type()
)
appnDnaDefaultSendToNetworkWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDnaDefaultSendToNetworkWindowSize.setStatus("mandatory")


class _AppnDnaAccountClass_Type(Unsigned32):
    """Custom type appnDnaAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnDnaAccountClass_Type.__name__ = "Unsigned32"
_AppnDnaAccountClass_Object = MibTableColumn
appnDnaAccountClass = _AppnDnaAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 14, 1, 10),
    _AppnDnaAccountClass_Type()
)
appnDnaAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDnaAccountClass.setStatus("mandatory")


class _AppnDnaAccountCollection_Type(OctetString):
    """Custom type appnDnaAccountCollection based on OctetString"""
    defaultHexValue = "80"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AppnDnaAccountCollection_Type.__name__ = "OctetString"
_AppnDnaAccountCollection_Object = MibTableColumn
appnDnaAccountCollection = _AppnDnaAccountCollection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 14, 1, 11),
    _AppnDnaAccountCollection_Type()
)
appnDnaAccountCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDnaAccountCollection.setStatus("mandatory")


class _AppnDnaServiceExchange_Type(Unsigned32):
    """Custom type appnDnaServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnDnaServiceExchange_Type.__name__ = "Unsigned32"
_AppnDnaServiceExchange_Object = MibTableColumn
appnDnaServiceExchange = _AppnDnaServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 2, 14, 1, 12),
    _AppnDnaServiceExchange_Type()
)
appnDnaServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDnaServiceExchange.setStatus("mandatory")
_AppnDlci_ObjectIdentity = ObjectIdentity
appnDlci = _AppnDlci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3)
)
_AppnDlciRowStatusTable_Object = MibTable
appnDlciRowStatusTable = _AppnDlciRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 1)
)
if mibBuilder.loadTexts:
    appnDlciRowStatusTable.setStatus("mandatory")
_AppnDlciRowStatusEntry_Object = MibTableRow
appnDlciRowStatusEntry = _AppnDlciRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 1, 1)
)
appnDlciRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciIndex"),
)
if mibBuilder.loadTexts:
    appnDlciRowStatusEntry.setStatus("mandatory")
_AppnDlciRowStatus_Type = RowStatus
_AppnDlciRowStatus_Object = MibTableColumn
appnDlciRowStatus = _AppnDlciRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 1, 1, 1),
    _AppnDlciRowStatus_Type()
)
appnDlciRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciRowStatus.setStatus("mandatory")
_AppnDlciComponentName_Type = DisplayString
_AppnDlciComponentName_Object = MibTableColumn
appnDlciComponentName = _AppnDlciComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 1, 1, 2),
    _AppnDlciComponentName_Type()
)
appnDlciComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciComponentName.setStatus("mandatory")
_AppnDlciStorageType_Type = StorageType
_AppnDlciStorageType_Object = MibTableColumn
appnDlciStorageType = _AppnDlciStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 1, 1, 4),
    _AppnDlciStorageType_Type()
)
appnDlciStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciStorageType.setStatus("mandatory")


class _AppnDlciIndex_Type(Integer32):
    """Custom type appnDlciIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 4095),
    )


_AppnDlciIndex_Type.__name__ = "Integer32"
_AppnDlciIndex_Object = MibTableColumn
appnDlciIndex = _AppnDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 1, 1, 10),
    _AppnDlciIndex_Type()
)
appnDlciIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnDlciIndex.setStatus("mandatory")
_AppnDlciDc_ObjectIdentity = ObjectIdentity
appnDlciDc = _AppnDlciDc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 2)
)
_AppnDlciDcRowStatusTable_Object = MibTable
appnDlciDcRowStatusTable = _AppnDlciDcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 2, 1)
)
if mibBuilder.loadTexts:
    appnDlciDcRowStatusTable.setStatus("mandatory")
_AppnDlciDcRowStatusEntry_Object = MibTableRow
appnDlciDcRowStatusEntry = _AppnDlciDcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 2, 1, 1)
)
appnDlciDcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciDcIndex"),
)
if mibBuilder.loadTexts:
    appnDlciDcRowStatusEntry.setStatus("mandatory")
_AppnDlciDcRowStatus_Type = RowStatus
_AppnDlciDcRowStatus_Object = MibTableColumn
appnDlciDcRowStatus = _AppnDlciDcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 2, 1, 1, 1),
    _AppnDlciDcRowStatus_Type()
)
appnDlciDcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciDcRowStatus.setStatus("mandatory")
_AppnDlciDcComponentName_Type = DisplayString
_AppnDlciDcComponentName_Object = MibTableColumn
appnDlciDcComponentName = _AppnDlciDcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 2, 1, 1, 2),
    _AppnDlciDcComponentName_Type()
)
appnDlciDcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciDcComponentName.setStatus("mandatory")
_AppnDlciDcStorageType_Type = StorageType
_AppnDlciDcStorageType_Object = MibTableColumn
appnDlciDcStorageType = _AppnDlciDcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 2, 1, 1, 4),
    _AppnDlciDcStorageType_Type()
)
appnDlciDcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciDcStorageType.setStatus("mandatory")
_AppnDlciDcIndex_Type = NonReplicated
_AppnDlciDcIndex_Object = MibTableColumn
appnDlciDcIndex = _AppnDlciDcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 2, 1, 1, 10),
    _AppnDlciDcIndex_Type()
)
appnDlciDcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnDlciDcIndex.setStatus("mandatory")
_AppnDlciDcOptionsTable_Object = MibTable
appnDlciDcOptionsTable = _AppnDlciDcOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 2, 10)
)
if mibBuilder.loadTexts:
    appnDlciDcOptionsTable.setStatus("mandatory")
_AppnDlciDcOptionsEntry_Object = MibTableRow
appnDlciDcOptionsEntry = _AppnDlciDcOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 2, 10, 1)
)
appnDlciDcOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciDcIndex"),
)
if mibBuilder.loadTexts:
    appnDlciDcOptionsEntry.setStatus("mandatory")


class _AppnDlciDcRemoteNpi_Type(Integer32):
    """Custom type appnDlciDcRemoteNpi based on Integer32"""
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


_AppnDlciDcRemoteNpi_Type.__name__ = "Integer32"
_AppnDlciDcRemoteNpi_Object = MibTableColumn
appnDlciDcRemoteNpi = _AppnDlciDcRemoteNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 2, 10, 1, 3),
    _AppnDlciDcRemoteNpi_Type()
)
appnDlciDcRemoteNpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciDcRemoteNpi.setStatus("mandatory")


class _AppnDlciDcRemoteDna_Type(DigitString):
    """Custom type appnDlciDcRemoteDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AppnDlciDcRemoteDna_Type.__name__ = "DigitString"
_AppnDlciDcRemoteDna_Object = MibTableColumn
appnDlciDcRemoteDna = _AppnDlciDcRemoteDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 2, 10, 1, 4),
    _AppnDlciDcRemoteDna_Type()
)
appnDlciDcRemoteDna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciDcRemoteDna.setStatus("mandatory")


class _AppnDlciDcRemoteDlci_Type(Unsigned32):
    """Custom type appnDlciDcRemoteDlci based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AppnDlciDcRemoteDlci_Type.__name__ = "Unsigned32"
_AppnDlciDcRemoteDlci_Object = MibTableColumn
appnDlciDcRemoteDlci = _AppnDlciDcRemoteDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 2, 10, 1, 5),
    _AppnDlciDcRemoteDlci_Type()
)
appnDlciDcRemoteDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciDcRemoteDlci.setStatus("mandatory")


class _AppnDlciDcType_Type(Integer32):
    """Custom type appnDlciDcType based on Integer32"""
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


_AppnDlciDcType_Type.__name__ = "Integer32"
_AppnDlciDcType_Object = MibTableColumn
appnDlciDcType = _AppnDlciDcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 2, 10, 1, 6),
    _AppnDlciDcType_Type()
)
appnDlciDcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciDcType.setStatus("mandatory")


class _AppnDlciDcTransferPriority_Type(Integer32):
    """Custom type appnDlciDcTransferPriority based on Integer32"""
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


_AppnDlciDcTransferPriority_Type.__name__ = "Integer32"
_AppnDlciDcTransferPriority_Object = MibTableColumn
appnDlciDcTransferPriority = _AppnDlciDcTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 2, 10, 1, 9),
    _AppnDlciDcTransferPriority_Type()
)
appnDlciDcTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciDcTransferPriority.setStatus("mandatory")


class _AppnDlciDcDiscardPriority_Type(Integer32):
    """Custom type appnDlciDcDiscardPriority based on Integer32"""
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


_AppnDlciDcDiscardPriority_Type.__name__ = "Integer32"
_AppnDlciDcDiscardPriority_Object = MibTableColumn
appnDlciDcDiscardPriority = _AppnDlciDcDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 2, 10, 1, 10),
    _AppnDlciDcDiscardPriority_Type()
)
appnDlciDcDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciDcDiscardPriority.setStatus("mandatory")
_AppnDlciDcNfaTable_Object = MibTable
appnDlciDcNfaTable = _AppnDlciDcNfaTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 2, 283)
)
if mibBuilder.loadTexts:
    appnDlciDcNfaTable.setStatus("obsolete")
_AppnDlciDcNfaEntry_Object = MibTableRow
appnDlciDcNfaEntry = _AppnDlciDcNfaEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 2, 283, 1)
)
appnDlciDcNfaEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciDcIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciDcNfaIndex"),
)
if mibBuilder.loadTexts:
    appnDlciDcNfaEntry.setStatus("obsolete")


class _AppnDlciDcNfaIndex_Type(Integer32):
    """Custom type appnDlciDcNfaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(48, 48),
    )


_AppnDlciDcNfaIndex_Type.__name__ = "Integer32"
_AppnDlciDcNfaIndex_Object = MibTableColumn
appnDlciDcNfaIndex = _AppnDlciDcNfaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 2, 283, 1, 1),
    _AppnDlciDcNfaIndex_Type()
)
appnDlciDcNfaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnDlciDcNfaIndex.setStatus("obsolete")


class _AppnDlciDcNfaValue_Type(HexString):
    """Custom type appnDlciDcNfaValue based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AppnDlciDcNfaValue_Type.__name__ = "HexString"
_AppnDlciDcNfaValue_Object = MibTableColumn
appnDlciDcNfaValue = _AppnDlciDcNfaValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 2, 283, 1, 2),
    _AppnDlciDcNfaValue_Type()
)
appnDlciDcNfaValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciDcNfaValue.setStatus("obsolete")
_AppnDlciDcNfaRowStatus_Type = RowStatus
_AppnDlciDcNfaRowStatus_Object = MibTableColumn
appnDlciDcNfaRowStatus = _AppnDlciDcNfaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 2, 283, 1, 3),
    _AppnDlciDcNfaRowStatus_Type()
)
appnDlciDcNfaRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    appnDlciDcNfaRowStatus.setStatus("obsolete")
_AppnDlciVc_ObjectIdentity = ObjectIdentity
appnDlciVc = _AppnDlciVc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3)
)
_AppnDlciVcRowStatusTable_Object = MibTable
appnDlciVcRowStatusTable = _AppnDlciVcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 1)
)
if mibBuilder.loadTexts:
    appnDlciVcRowStatusTable.setStatus("mandatory")
_AppnDlciVcRowStatusEntry_Object = MibTableRow
appnDlciVcRowStatusEntry = _AppnDlciVcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 1, 1)
)
appnDlciVcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciVcIndex"),
)
if mibBuilder.loadTexts:
    appnDlciVcRowStatusEntry.setStatus("mandatory")
_AppnDlciVcRowStatus_Type = RowStatus
_AppnDlciVcRowStatus_Object = MibTableColumn
appnDlciVcRowStatus = _AppnDlciVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 1, 1, 1),
    _AppnDlciVcRowStatus_Type()
)
appnDlciVcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcRowStatus.setStatus("mandatory")
_AppnDlciVcComponentName_Type = DisplayString
_AppnDlciVcComponentName_Object = MibTableColumn
appnDlciVcComponentName = _AppnDlciVcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 1, 1, 2),
    _AppnDlciVcComponentName_Type()
)
appnDlciVcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcComponentName.setStatus("mandatory")
_AppnDlciVcStorageType_Type = StorageType
_AppnDlciVcStorageType_Object = MibTableColumn
appnDlciVcStorageType = _AppnDlciVcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 1, 1, 4),
    _AppnDlciVcStorageType_Type()
)
appnDlciVcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcStorageType.setStatus("mandatory")
_AppnDlciVcIndex_Type = NonReplicated
_AppnDlciVcIndex_Object = MibTableColumn
appnDlciVcIndex = _AppnDlciVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 1, 1, 10),
    _AppnDlciVcIndex_Type()
)
appnDlciVcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnDlciVcIndex.setStatus("mandatory")
_AppnDlciVcCadTable_Object = MibTable
appnDlciVcCadTable = _AppnDlciVcCadTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 10)
)
if mibBuilder.loadTexts:
    appnDlciVcCadTable.setStatus("mandatory")
_AppnDlciVcCadEntry_Object = MibTableRow
appnDlciVcCadEntry = _AppnDlciVcCadEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 10, 1)
)
appnDlciVcCadEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciVcIndex"),
)
if mibBuilder.loadTexts:
    appnDlciVcCadEntry.setStatus("mandatory")


class _AppnDlciVcType_Type(Integer32):
    """Custom type appnDlciVcType based on Integer32"""
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


_AppnDlciVcType_Type.__name__ = "Integer32"
_AppnDlciVcType_Object = MibTableColumn
appnDlciVcType = _AppnDlciVcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 10, 1, 1),
    _AppnDlciVcType_Type()
)
appnDlciVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcType.setStatus("mandatory")


class _AppnDlciVcState_Type(Integer32):
    """Custom type appnDlciVcState based on Integer32"""
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


_AppnDlciVcState_Type.__name__ = "Integer32"
_AppnDlciVcState_Object = MibTableColumn
appnDlciVcState = _AppnDlciVcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 10, 1, 2),
    _AppnDlciVcState_Type()
)
appnDlciVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcState.setStatus("mandatory")


class _AppnDlciVcPreviousState_Type(Integer32):
    """Custom type appnDlciVcPreviousState based on Integer32"""
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


_AppnDlciVcPreviousState_Type.__name__ = "Integer32"
_AppnDlciVcPreviousState_Object = MibTableColumn
appnDlciVcPreviousState = _AppnDlciVcPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 10, 1, 3),
    _AppnDlciVcPreviousState_Type()
)
appnDlciVcPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcPreviousState.setStatus("mandatory")


class _AppnDlciVcDiagnosticCode_Type(Unsigned32):
    """Custom type appnDlciVcDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnDlciVcDiagnosticCode_Type.__name__ = "Unsigned32"
_AppnDlciVcDiagnosticCode_Object = MibTableColumn
appnDlciVcDiagnosticCode = _AppnDlciVcDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 10, 1, 4),
    _AppnDlciVcDiagnosticCode_Type()
)
appnDlciVcDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcDiagnosticCode.setStatus("mandatory")


class _AppnDlciVcPreviousDiagnosticCode_Type(Unsigned32):
    """Custom type appnDlciVcPreviousDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnDlciVcPreviousDiagnosticCode_Type.__name__ = "Unsigned32"
_AppnDlciVcPreviousDiagnosticCode_Object = MibTableColumn
appnDlciVcPreviousDiagnosticCode = _AppnDlciVcPreviousDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 10, 1, 5),
    _AppnDlciVcPreviousDiagnosticCode_Type()
)
appnDlciVcPreviousDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcPreviousDiagnosticCode.setStatus("mandatory")


class _AppnDlciVcCalledNpi_Type(Integer32):
    """Custom type appnDlciVcCalledNpi based on Integer32"""
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


_AppnDlciVcCalledNpi_Type.__name__ = "Integer32"
_AppnDlciVcCalledNpi_Object = MibTableColumn
appnDlciVcCalledNpi = _AppnDlciVcCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 10, 1, 6),
    _AppnDlciVcCalledNpi_Type()
)
appnDlciVcCalledNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcCalledNpi.setStatus("mandatory")


class _AppnDlciVcCalledDna_Type(DigitString):
    """Custom type appnDlciVcCalledDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AppnDlciVcCalledDna_Type.__name__ = "DigitString"
_AppnDlciVcCalledDna_Object = MibTableColumn
appnDlciVcCalledDna = _AppnDlciVcCalledDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 10, 1, 7),
    _AppnDlciVcCalledDna_Type()
)
appnDlciVcCalledDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcCalledDna.setStatus("mandatory")


class _AppnDlciVcCalledLcn_Type(Unsigned32):
    """Custom type appnDlciVcCalledLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AppnDlciVcCalledLcn_Type.__name__ = "Unsigned32"
_AppnDlciVcCalledLcn_Object = MibTableColumn
appnDlciVcCalledLcn = _AppnDlciVcCalledLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 10, 1, 8),
    _AppnDlciVcCalledLcn_Type()
)
appnDlciVcCalledLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcCalledLcn.setStatus("mandatory")


class _AppnDlciVcCallingNpi_Type(Integer32):
    """Custom type appnDlciVcCallingNpi based on Integer32"""
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


_AppnDlciVcCallingNpi_Type.__name__ = "Integer32"
_AppnDlciVcCallingNpi_Object = MibTableColumn
appnDlciVcCallingNpi = _AppnDlciVcCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 10, 1, 9),
    _AppnDlciVcCallingNpi_Type()
)
appnDlciVcCallingNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcCallingNpi.setStatus("mandatory")


class _AppnDlciVcCallingDna_Type(DigitString):
    """Custom type appnDlciVcCallingDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AppnDlciVcCallingDna_Type.__name__ = "DigitString"
_AppnDlciVcCallingDna_Object = MibTableColumn
appnDlciVcCallingDna = _AppnDlciVcCallingDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 10, 1, 10),
    _AppnDlciVcCallingDna_Type()
)
appnDlciVcCallingDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcCallingDna.setStatus("mandatory")


class _AppnDlciVcCallingLcn_Type(Unsigned32):
    """Custom type appnDlciVcCallingLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AppnDlciVcCallingLcn_Type.__name__ = "Unsigned32"
_AppnDlciVcCallingLcn_Object = MibTableColumn
appnDlciVcCallingLcn = _AppnDlciVcCallingLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 10, 1, 11),
    _AppnDlciVcCallingLcn_Type()
)
appnDlciVcCallingLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcCallingLcn.setStatus("mandatory")


class _AppnDlciVcAccountingEnabled_Type(Integer32):
    """Custom type appnDlciVcAccountingEnabled based on Integer32"""
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


_AppnDlciVcAccountingEnabled_Type.__name__ = "Integer32"
_AppnDlciVcAccountingEnabled_Object = MibTableColumn
appnDlciVcAccountingEnabled = _AppnDlciVcAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 10, 1, 12),
    _AppnDlciVcAccountingEnabled_Type()
)
appnDlciVcAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcAccountingEnabled.setStatus("mandatory")


class _AppnDlciVcFastSelectCall_Type(Integer32):
    """Custom type appnDlciVcFastSelectCall based on Integer32"""
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


_AppnDlciVcFastSelectCall_Type.__name__ = "Integer32"
_AppnDlciVcFastSelectCall_Object = MibTableColumn
appnDlciVcFastSelectCall = _AppnDlciVcFastSelectCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 10, 1, 13),
    _AppnDlciVcFastSelectCall_Type()
)
appnDlciVcFastSelectCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcFastSelectCall.setStatus("mandatory")


class _AppnDlciVcPathReliability_Type(Integer32):
    """Custom type appnDlciVcPathReliability based on Integer32"""
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


_AppnDlciVcPathReliability_Type.__name__ = "Integer32"
_AppnDlciVcPathReliability_Object = MibTableColumn
appnDlciVcPathReliability = _AppnDlciVcPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 10, 1, 19),
    _AppnDlciVcPathReliability_Type()
)
appnDlciVcPathReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcPathReliability.setStatus("mandatory")


class _AppnDlciVcAccountingEnd_Type(Integer32):
    """Custom type appnDlciVcAccountingEnd based on Integer32"""
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


_AppnDlciVcAccountingEnd_Type.__name__ = "Integer32"
_AppnDlciVcAccountingEnd_Object = MibTableColumn
appnDlciVcAccountingEnd = _AppnDlciVcAccountingEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 10, 1, 20),
    _AppnDlciVcAccountingEnd_Type()
)
appnDlciVcAccountingEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcAccountingEnd.setStatus("mandatory")


class _AppnDlciVcPriority_Type(Integer32):
    """Custom type appnDlciVcPriority based on Integer32"""
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


_AppnDlciVcPriority_Type.__name__ = "Integer32"
_AppnDlciVcPriority_Object = MibTableColumn
appnDlciVcPriority = _AppnDlciVcPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 10, 1, 21),
    _AppnDlciVcPriority_Type()
)
appnDlciVcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcPriority.setStatus("mandatory")


class _AppnDlciVcSegmentSize_Type(Unsigned32):
    """Custom type appnDlciVcSegmentSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AppnDlciVcSegmentSize_Type.__name__ = "Unsigned32"
_AppnDlciVcSegmentSize_Object = MibTableColumn
appnDlciVcSegmentSize = _AppnDlciVcSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 10, 1, 22),
    _AppnDlciVcSegmentSize_Type()
)
appnDlciVcSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcSegmentSize.setStatus("mandatory")


class _AppnDlciVcMaxSubnetPktSize_Type(Unsigned32):
    """Custom type appnDlciVcMaxSubnetPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AppnDlciVcMaxSubnetPktSize_Type.__name__ = "Unsigned32"
_AppnDlciVcMaxSubnetPktSize_Object = MibTableColumn
appnDlciVcMaxSubnetPktSize = _AppnDlciVcMaxSubnetPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 10, 1, 27),
    _AppnDlciVcMaxSubnetPktSize_Type()
)
appnDlciVcMaxSubnetPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcMaxSubnetPktSize.setStatus("mandatory")


class _AppnDlciVcRcosToNetwork_Type(Integer32):
    """Custom type appnDlciVcRcosToNetwork based on Integer32"""
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


_AppnDlciVcRcosToNetwork_Type.__name__ = "Integer32"
_AppnDlciVcRcosToNetwork_Object = MibTableColumn
appnDlciVcRcosToNetwork = _AppnDlciVcRcosToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 10, 1, 28),
    _AppnDlciVcRcosToNetwork_Type()
)
appnDlciVcRcosToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcRcosToNetwork.setStatus("mandatory")


class _AppnDlciVcRcosFromNetwork_Type(Integer32):
    """Custom type appnDlciVcRcosFromNetwork based on Integer32"""
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


_AppnDlciVcRcosFromNetwork_Type.__name__ = "Integer32"
_AppnDlciVcRcosFromNetwork_Object = MibTableColumn
appnDlciVcRcosFromNetwork = _AppnDlciVcRcosFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 10, 1, 29),
    _AppnDlciVcRcosFromNetwork_Type()
)
appnDlciVcRcosFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcRcosFromNetwork.setStatus("mandatory")


class _AppnDlciVcEmissionPriorityToNetwork_Type(Integer32):
    """Custom type appnDlciVcEmissionPriorityToNetwork based on Integer32"""
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


_AppnDlciVcEmissionPriorityToNetwork_Type.__name__ = "Integer32"
_AppnDlciVcEmissionPriorityToNetwork_Object = MibTableColumn
appnDlciVcEmissionPriorityToNetwork = _AppnDlciVcEmissionPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 10, 1, 30),
    _AppnDlciVcEmissionPriorityToNetwork_Type()
)
appnDlciVcEmissionPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcEmissionPriorityToNetwork.setStatus("mandatory")


class _AppnDlciVcEmissionPriorityFromNetwork_Type(Integer32):
    """Custom type appnDlciVcEmissionPriorityFromNetwork based on Integer32"""
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


_AppnDlciVcEmissionPriorityFromNetwork_Type.__name__ = "Integer32"
_AppnDlciVcEmissionPriorityFromNetwork_Object = MibTableColumn
appnDlciVcEmissionPriorityFromNetwork = _AppnDlciVcEmissionPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 10, 1, 31),
    _AppnDlciVcEmissionPriorityFromNetwork_Type()
)
appnDlciVcEmissionPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcEmissionPriorityFromNetwork.setStatus("mandatory")


class _AppnDlciVcDataPath_Type(AsciiString):
    """Custom type appnDlciVcDataPath based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AppnDlciVcDataPath_Type.__name__ = "AsciiString"
_AppnDlciVcDataPath_Object = MibTableColumn
appnDlciVcDataPath = _AppnDlciVcDataPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 10, 1, 32),
    _AppnDlciVcDataPath_Type()
)
appnDlciVcDataPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcDataPath.setStatus("mandatory")
_AppnDlciVcIntdTable_Object = MibTable
appnDlciVcIntdTable = _AppnDlciVcIntdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 11)
)
if mibBuilder.loadTexts:
    appnDlciVcIntdTable.setStatus("mandatory")
_AppnDlciVcIntdEntry_Object = MibTableRow
appnDlciVcIntdEntry = _AppnDlciVcIntdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 11, 1)
)
appnDlciVcIntdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciVcIndex"),
)
if mibBuilder.loadTexts:
    appnDlciVcIntdEntry.setStatus("mandatory")


class _AppnDlciVcCallReferenceNumber_Type(Hex):
    """Custom type appnDlciVcCallReferenceNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_AppnDlciVcCallReferenceNumber_Type.__name__ = "Hex"
_AppnDlciVcCallReferenceNumber_Object = MibTableColumn
appnDlciVcCallReferenceNumber = _AppnDlciVcCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 11, 1, 1),
    _AppnDlciVcCallReferenceNumber_Type()
)
appnDlciVcCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcCallReferenceNumber.setStatus("mandatory")


class _AppnDlciVcElapsedTimeTillNow_Type(Unsigned32):
    """Custom type appnDlciVcElapsedTimeTillNow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_AppnDlciVcElapsedTimeTillNow_Type.__name__ = "Unsigned32"
_AppnDlciVcElapsedTimeTillNow_Object = MibTableColumn
appnDlciVcElapsedTimeTillNow = _AppnDlciVcElapsedTimeTillNow_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 11, 1, 2),
    _AppnDlciVcElapsedTimeTillNow_Type()
)
appnDlciVcElapsedTimeTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcElapsedTimeTillNow.setStatus("mandatory")


class _AppnDlciVcSegmentsRx_Type(Unsigned32):
    """Custom type appnDlciVcSegmentsRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_AppnDlciVcSegmentsRx_Type.__name__ = "Unsigned32"
_AppnDlciVcSegmentsRx_Object = MibTableColumn
appnDlciVcSegmentsRx = _AppnDlciVcSegmentsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 11, 1, 3),
    _AppnDlciVcSegmentsRx_Type()
)
appnDlciVcSegmentsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcSegmentsRx.setStatus("mandatory")


class _AppnDlciVcSegmentsSent_Type(Unsigned32):
    """Custom type appnDlciVcSegmentsSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_AppnDlciVcSegmentsSent_Type.__name__ = "Unsigned32"
_AppnDlciVcSegmentsSent_Object = MibTableColumn
appnDlciVcSegmentsSent = _AppnDlciVcSegmentsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 11, 1, 4),
    _AppnDlciVcSegmentsSent_Type()
)
appnDlciVcSegmentsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcSegmentsSent.setStatus("mandatory")


class _AppnDlciVcStartTime_Type(EnterpriseDateAndTime):
    """Custom type appnDlciVcStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_AppnDlciVcStartTime_Type.__name__ = "EnterpriseDateAndTime"
_AppnDlciVcStartTime_Object = MibTableColumn
appnDlciVcStartTime = _AppnDlciVcStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 11, 1, 5),
    _AppnDlciVcStartTime_Type()
)
appnDlciVcStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcStartTime.setStatus("mandatory")
_AppnDlciVcFrdTable_Object = MibTable
appnDlciVcFrdTable = _AppnDlciVcFrdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 12)
)
if mibBuilder.loadTexts:
    appnDlciVcFrdTable.setStatus("mandatory")
_AppnDlciVcFrdEntry_Object = MibTableRow
appnDlciVcFrdEntry = _AppnDlciVcFrdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 12, 1)
)
appnDlciVcFrdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciVcIndex"),
)
if mibBuilder.loadTexts:
    appnDlciVcFrdEntry.setStatus("mandatory")


class _AppnDlciVcFrmCongestedToSubnet_Type(Unsigned32):
    """Custom type appnDlciVcFrmCongestedToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AppnDlciVcFrmCongestedToSubnet_Type.__name__ = "Unsigned32"
_AppnDlciVcFrmCongestedToSubnet_Object = MibTableColumn
appnDlciVcFrmCongestedToSubnet = _AppnDlciVcFrmCongestedToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 12, 1, 2),
    _AppnDlciVcFrmCongestedToSubnet_Type()
)
appnDlciVcFrmCongestedToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcFrmCongestedToSubnet.setStatus("mandatory")


class _AppnDlciVcCannotForwardToSubnet_Type(Unsigned32):
    """Custom type appnDlciVcCannotForwardToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AppnDlciVcCannotForwardToSubnet_Type.__name__ = "Unsigned32"
_AppnDlciVcCannotForwardToSubnet_Object = MibTableColumn
appnDlciVcCannotForwardToSubnet = _AppnDlciVcCannotForwardToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 12, 1, 3),
    _AppnDlciVcCannotForwardToSubnet_Type()
)
appnDlciVcCannotForwardToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcCannotForwardToSubnet.setStatus("mandatory")


class _AppnDlciVcNotDataXferToSubnet_Type(Unsigned32):
    """Custom type appnDlciVcNotDataXferToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AppnDlciVcNotDataXferToSubnet_Type.__name__ = "Unsigned32"
_AppnDlciVcNotDataXferToSubnet_Object = MibTableColumn
appnDlciVcNotDataXferToSubnet = _AppnDlciVcNotDataXferToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 12, 1, 4),
    _AppnDlciVcNotDataXferToSubnet_Type()
)
appnDlciVcNotDataXferToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcNotDataXferToSubnet.setStatus("mandatory")


class _AppnDlciVcOutOfRangeFrmFromSubnet_Type(Unsigned32):
    """Custom type appnDlciVcOutOfRangeFrmFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AppnDlciVcOutOfRangeFrmFromSubnet_Type.__name__ = "Unsigned32"
_AppnDlciVcOutOfRangeFrmFromSubnet_Object = MibTableColumn
appnDlciVcOutOfRangeFrmFromSubnet = _AppnDlciVcOutOfRangeFrmFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 12, 1, 5),
    _AppnDlciVcOutOfRangeFrmFromSubnet_Type()
)
appnDlciVcOutOfRangeFrmFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcOutOfRangeFrmFromSubnet.setStatus("mandatory")


class _AppnDlciVcCombErrorsFromSubnet_Type(Unsigned32):
    """Custom type appnDlciVcCombErrorsFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AppnDlciVcCombErrorsFromSubnet_Type.__name__ = "Unsigned32"
_AppnDlciVcCombErrorsFromSubnet_Object = MibTableColumn
appnDlciVcCombErrorsFromSubnet = _AppnDlciVcCombErrorsFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 12, 1, 6),
    _AppnDlciVcCombErrorsFromSubnet_Type()
)
appnDlciVcCombErrorsFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcCombErrorsFromSubnet.setStatus("mandatory")


class _AppnDlciVcDuplicatesFromSubnet_Type(Unsigned32):
    """Custom type appnDlciVcDuplicatesFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AppnDlciVcDuplicatesFromSubnet_Type.__name__ = "Unsigned32"
_AppnDlciVcDuplicatesFromSubnet_Object = MibTableColumn
appnDlciVcDuplicatesFromSubnet = _AppnDlciVcDuplicatesFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 12, 1, 7),
    _AppnDlciVcDuplicatesFromSubnet_Type()
)
appnDlciVcDuplicatesFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcDuplicatesFromSubnet.setStatus("mandatory")


class _AppnDlciVcNotDataXferFromSubnet_Type(Unsigned32):
    """Custom type appnDlciVcNotDataXferFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AppnDlciVcNotDataXferFromSubnet_Type.__name__ = "Unsigned32"
_AppnDlciVcNotDataXferFromSubnet_Object = MibTableColumn
appnDlciVcNotDataXferFromSubnet = _AppnDlciVcNotDataXferFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 12, 1, 8),
    _AppnDlciVcNotDataXferFromSubnet_Type()
)
appnDlciVcNotDataXferFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcNotDataXferFromSubnet.setStatus("mandatory")


class _AppnDlciVcFrmLossTimeouts_Type(Unsigned32):
    """Custom type appnDlciVcFrmLossTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AppnDlciVcFrmLossTimeouts_Type.__name__ = "Unsigned32"
_AppnDlciVcFrmLossTimeouts_Object = MibTableColumn
appnDlciVcFrmLossTimeouts = _AppnDlciVcFrmLossTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 12, 1, 9),
    _AppnDlciVcFrmLossTimeouts_Type()
)
appnDlciVcFrmLossTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcFrmLossTimeouts.setStatus("mandatory")


class _AppnDlciVcOoSeqByteCntExceeded_Type(Unsigned32):
    """Custom type appnDlciVcOoSeqByteCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AppnDlciVcOoSeqByteCntExceeded_Type.__name__ = "Unsigned32"
_AppnDlciVcOoSeqByteCntExceeded_Object = MibTableColumn
appnDlciVcOoSeqByteCntExceeded = _AppnDlciVcOoSeqByteCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 12, 1, 10),
    _AppnDlciVcOoSeqByteCntExceeded_Type()
)
appnDlciVcOoSeqByteCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcOoSeqByteCntExceeded.setStatus("mandatory")


class _AppnDlciVcPeakOoSeqPktCount_Type(Unsigned32):
    """Custom type appnDlciVcPeakOoSeqPktCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AppnDlciVcPeakOoSeqPktCount_Type.__name__ = "Unsigned32"
_AppnDlciVcPeakOoSeqPktCount_Object = MibTableColumn
appnDlciVcPeakOoSeqPktCount = _AppnDlciVcPeakOoSeqPktCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 12, 1, 11),
    _AppnDlciVcPeakOoSeqPktCount_Type()
)
appnDlciVcPeakOoSeqPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcPeakOoSeqPktCount.setStatus("mandatory")


class _AppnDlciVcPeakOoSeqFrmForwarded_Type(Unsigned32):
    """Custom type appnDlciVcPeakOoSeqFrmForwarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AppnDlciVcPeakOoSeqFrmForwarded_Type.__name__ = "Unsigned32"
_AppnDlciVcPeakOoSeqFrmForwarded_Object = MibTableColumn
appnDlciVcPeakOoSeqFrmForwarded = _AppnDlciVcPeakOoSeqFrmForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 12, 1, 12),
    _AppnDlciVcPeakOoSeqFrmForwarded_Type()
)
appnDlciVcPeakOoSeqFrmForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcPeakOoSeqFrmForwarded.setStatus("mandatory")


class _AppnDlciVcSendSequenceNumber_Type(Unsigned32):
    """Custom type appnDlciVcSendSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AppnDlciVcSendSequenceNumber_Type.__name__ = "Unsigned32"
_AppnDlciVcSendSequenceNumber_Object = MibTableColumn
appnDlciVcSendSequenceNumber = _AppnDlciVcSendSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 12, 1, 13),
    _AppnDlciVcSendSequenceNumber_Type()
)
appnDlciVcSendSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcSendSequenceNumber.setStatus("mandatory")


class _AppnDlciVcPktRetryTimeouts_Type(Unsigned32):
    """Custom type appnDlciVcPktRetryTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AppnDlciVcPktRetryTimeouts_Type.__name__ = "Unsigned32"
_AppnDlciVcPktRetryTimeouts_Object = MibTableColumn
appnDlciVcPktRetryTimeouts = _AppnDlciVcPktRetryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 12, 1, 15),
    _AppnDlciVcPktRetryTimeouts_Type()
)
appnDlciVcPktRetryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcPktRetryTimeouts.setStatus("mandatory")


class _AppnDlciVcPeakRetryQueueSize_Type(Unsigned32):
    """Custom type appnDlciVcPeakRetryQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AppnDlciVcPeakRetryQueueSize_Type.__name__ = "Unsigned32"
_AppnDlciVcPeakRetryQueueSize_Object = MibTableColumn
appnDlciVcPeakRetryQueueSize = _AppnDlciVcPeakRetryQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 12, 1, 16),
    _AppnDlciVcPeakRetryQueueSize_Type()
)
appnDlciVcPeakRetryQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcPeakRetryQueueSize.setStatus("mandatory")


class _AppnDlciVcSubnetRecoveries_Type(Unsigned32):
    """Custom type appnDlciVcSubnetRecoveries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AppnDlciVcSubnetRecoveries_Type.__name__ = "Unsigned32"
_AppnDlciVcSubnetRecoveries_Object = MibTableColumn
appnDlciVcSubnetRecoveries = _AppnDlciVcSubnetRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 12, 1, 17),
    _AppnDlciVcSubnetRecoveries_Type()
)
appnDlciVcSubnetRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcSubnetRecoveries.setStatus("mandatory")


class _AppnDlciVcOoSeqPktCntExceeded_Type(Unsigned32):
    """Custom type appnDlciVcOoSeqPktCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnDlciVcOoSeqPktCntExceeded_Type.__name__ = "Unsigned32"
_AppnDlciVcOoSeqPktCntExceeded_Object = MibTableColumn
appnDlciVcOoSeqPktCntExceeded = _AppnDlciVcOoSeqPktCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 12, 1, 19),
    _AppnDlciVcOoSeqPktCntExceeded_Type()
)
appnDlciVcOoSeqPktCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcOoSeqPktCntExceeded.setStatus("mandatory")


class _AppnDlciVcPeakOoSeqByteCount_Type(Unsigned32):
    """Custom type appnDlciVcPeakOoSeqByteCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_AppnDlciVcPeakOoSeqByteCount_Type.__name__ = "Unsigned32"
_AppnDlciVcPeakOoSeqByteCount_Object = MibTableColumn
appnDlciVcPeakOoSeqByteCount = _AppnDlciVcPeakOoSeqByteCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 12, 1, 20),
    _AppnDlciVcPeakOoSeqByteCount_Type()
)
appnDlciVcPeakOoSeqByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcPeakOoSeqByteCount.setStatus("mandatory")
_AppnDlciVcDmepTable_Object = MibTable
appnDlciVcDmepTable = _AppnDlciVcDmepTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 417)
)
if mibBuilder.loadTexts:
    appnDlciVcDmepTable.setStatus("mandatory")
_AppnDlciVcDmepEntry_Object = MibTableRow
appnDlciVcDmepEntry = _AppnDlciVcDmepEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 417, 1)
)
appnDlciVcDmepEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciVcIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciVcDmepValue"),
)
if mibBuilder.loadTexts:
    appnDlciVcDmepEntry.setStatus("mandatory")
_AppnDlciVcDmepValue_Type = RowPointer
_AppnDlciVcDmepValue_Object = MibTableColumn
appnDlciVcDmepValue = _AppnDlciVcDmepValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 3, 417, 1, 1),
    _AppnDlciVcDmepValue_Type()
)
appnDlciVcDmepValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciVcDmepValue.setStatus("mandatory")
_AppnDlciBnnLsDef_ObjectIdentity = ObjectIdentity
appnDlciBnnLsDef = _AppnDlciBnnLsDef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 4)
)
_AppnDlciBnnLsDefRowStatusTable_Object = MibTable
appnDlciBnnLsDefRowStatusTable = _AppnDlciBnnLsDefRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 4, 1)
)
if mibBuilder.loadTexts:
    appnDlciBnnLsDefRowStatusTable.setStatus("mandatory")
_AppnDlciBnnLsDefRowStatusEntry_Object = MibTableRow
appnDlciBnnLsDefRowStatusEntry = _AppnDlciBnnLsDefRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 4, 1, 1)
)
appnDlciBnnLsDefRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciBnnLsDefIndex"),
)
if mibBuilder.loadTexts:
    appnDlciBnnLsDefRowStatusEntry.setStatus("mandatory")
_AppnDlciBnnLsDefRowStatus_Type = RowStatus
_AppnDlciBnnLsDefRowStatus_Object = MibTableColumn
appnDlciBnnLsDefRowStatus = _AppnDlciBnnLsDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 4, 1, 1, 1),
    _AppnDlciBnnLsDefRowStatus_Type()
)
appnDlciBnnLsDefRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciBnnLsDefRowStatus.setStatus("mandatory")
_AppnDlciBnnLsDefComponentName_Type = DisplayString
_AppnDlciBnnLsDefComponentName_Object = MibTableColumn
appnDlciBnnLsDefComponentName = _AppnDlciBnnLsDefComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 4, 1, 1, 2),
    _AppnDlciBnnLsDefComponentName_Type()
)
appnDlciBnnLsDefComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciBnnLsDefComponentName.setStatus("mandatory")
_AppnDlciBnnLsDefStorageType_Type = StorageType
_AppnDlciBnnLsDefStorageType_Object = MibTableColumn
appnDlciBnnLsDefStorageType = _AppnDlciBnnLsDefStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 4, 1, 1, 4),
    _AppnDlciBnnLsDefStorageType_Type()
)
appnDlciBnnLsDefStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciBnnLsDefStorageType.setStatus("mandatory")


class _AppnDlciBnnLsDefIndex_Type(Integer32):
    """Custom type appnDlciBnnLsDefIndex based on Integer32"""
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


_AppnDlciBnnLsDefIndex_Type.__name__ = "Integer32"
_AppnDlciBnnLsDefIndex_Object = MibTableColumn
appnDlciBnnLsDefIndex = _AppnDlciBnnLsDefIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 4, 1, 1, 10),
    _AppnDlciBnnLsDefIndex_Type()
)
appnDlciBnnLsDefIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnDlciBnnLsDefIndex.setStatus("mandatory")
_AppnDlciBnnLsDefProvTable_Object = MibTable
appnDlciBnnLsDefProvTable = _AppnDlciBnnLsDefProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 4, 2)
)
if mibBuilder.loadTexts:
    appnDlciBnnLsDefProvTable.setStatus("mandatory")
_AppnDlciBnnLsDefProvEntry_Object = MibTableRow
appnDlciBnnLsDefProvEntry = _AppnDlciBnnLsDefProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 4, 2, 1)
)
appnDlciBnnLsDefProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciBnnLsDefIndex"),
)
if mibBuilder.loadTexts:
    appnDlciBnnLsDefProvEntry.setStatus("mandatory")


class _AppnDlciBnnLsDefDspuService_Type(Integer32):
    """Custom type appnDlciBnnLsDefDspuService based on Integer32"""
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


_AppnDlciBnnLsDefDspuService_Type.__name__ = "Integer32"
_AppnDlciBnnLsDefDspuService_Object = MibTableColumn
appnDlciBnnLsDefDspuService = _AppnDlciBnnLsDefDspuService_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 4, 2, 1, 1),
    _AppnDlciBnnLsDefDspuService_Type()
)
appnDlciBnnLsDefDspuService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciBnnLsDefDspuService.setStatus("mandatory")


class _AppnDlciBnnLsDefAdjacentCpName_Type(AsciiString):
    """Custom type appnDlciBnnLsDefAdjacentCpName based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_AppnDlciBnnLsDefAdjacentCpName_Type.__name__ = "AsciiString"
_AppnDlciBnnLsDefAdjacentCpName_Object = MibTableColumn
appnDlciBnnLsDefAdjacentCpName = _AppnDlciBnnLsDefAdjacentCpName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 4, 2, 1, 2),
    _AppnDlciBnnLsDefAdjacentCpName_Type()
)
appnDlciBnnLsDefAdjacentCpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciBnnLsDefAdjacentCpName.setStatus("mandatory")


class _AppnDlciBnnLsDefAdjacentCpType_Type(Integer32):
    """Custom type appnDlciBnnLsDefAdjacentCpType based on Integer32"""
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


_AppnDlciBnnLsDefAdjacentCpType_Type.__name__ = "Integer32"
_AppnDlciBnnLsDefAdjacentCpType_Object = MibTableColumn
appnDlciBnnLsDefAdjacentCpType = _AppnDlciBnnLsDefAdjacentCpType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 4, 2, 1, 3),
    _AppnDlciBnnLsDefAdjacentCpType_Type()
)
appnDlciBnnLsDefAdjacentCpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciBnnLsDefAdjacentCpType.setStatus("mandatory")


class _AppnDlciBnnLsDefTgNum_Type(Unsigned32):
    """Custom type appnDlciBnnLsDefTgNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_AppnDlciBnnLsDefTgNum_Type.__name__ = "Unsigned32"
_AppnDlciBnnLsDefTgNum_Object = MibTableColumn
appnDlciBnnLsDefTgNum = _AppnDlciBnnLsDefTgNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 4, 2, 1, 5),
    _AppnDlciBnnLsDefTgNum_Type()
)
appnDlciBnnLsDefTgNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciBnnLsDefTgNum.setStatus("mandatory")


class _AppnDlciBnnLsDefDlusName_Type(AsciiString):
    """Custom type appnDlciBnnLsDefDlusName based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_AppnDlciBnnLsDefDlusName_Type.__name__ = "AsciiString"
_AppnDlciBnnLsDefDlusName_Object = MibTableColumn
appnDlciBnnLsDefDlusName = _AppnDlciBnnLsDefDlusName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 4, 2, 1, 6),
    _AppnDlciBnnLsDefDlusName_Type()
)
appnDlciBnnLsDefDlusName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciBnnLsDefDlusName.setStatus("mandatory")


class _AppnDlciBnnLsDefBackupDlusName_Type(AsciiString):
    """Custom type appnDlciBnnLsDefBackupDlusName based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_AppnDlciBnnLsDefBackupDlusName_Type.__name__ = "AsciiString"
_AppnDlciBnnLsDefBackupDlusName_Object = MibTableColumn
appnDlciBnnLsDefBackupDlusName = _AppnDlciBnnLsDefBackupDlusName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 4, 2, 1, 7),
    _AppnDlciBnnLsDefBackupDlusName_Type()
)
appnDlciBnnLsDefBackupDlusName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciBnnLsDefBackupDlusName.setStatus("mandatory")


class _AppnDlciBnnLsDefHprSupported_Type(Integer32):
    """Custom type appnDlciBnnLsDefHprSupported based on Integer32"""
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


_AppnDlciBnnLsDefHprSupported_Type.__name__ = "Integer32"
_AppnDlciBnnLsDefHprSupported_Object = MibTableColumn
appnDlciBnnLsDefHprSupported = _AppnDlciBnnLsDefHprSupported_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 4, 2, 1, 8),
    _AppnDlciBnnLsDefHprSupported_Type()
)
appnDlciBnnLsDefHprSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciBnnLsDefHprSupported.setStatus("mandatory")


class _AppnDlciBnnLsDefAdjacentNodeID_Type(Hex):
    """Custom type appnDlciBnnLsDefAdjacentNodeID based on Hex"""
    defaultValue = 0

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AppnDlciBnnLsDefAdjacentNodeID_Type.__name__ = "Hex"
_AppnDlciBnnLsDefAdjacentNodeID_Object = MibTableColumn
appnDlciBnnLsDefAdjacentNodeID = _AppnDlciBnnLsDefAdjacentNodeID_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 4, 2, 1, 9),
    _AppnDlciBnnLsDefAdjacentNodeID_Type()
)
appnDlciBnnLsDefAdjacentNodeID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciBnnLsDefAdjacentNodeID.setStatus("mandatory")


class _AppnDlciBnnLsDefCpCpSessionSupport_Type(Integer32):
    """Custom type appnDlciBnnLsDefCpCpSessionSupport based on Integer32"""
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


_AppnDlciBnnLsDefCpCpSessionSupport_Type.__name__ = "Integer32"
_AppnDlciBnnLsDefCpCpSessionSupport_Object = MibTableColumn
appnDlciBnnLsDefCpCpSessionSupport = _AppnDlciBnnLsDefCpCpSessionSupport_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 4, 2, 1, 10),
    _AppnDlciBnnLsDefCpCpSessionSupport_Type()
)
appnDlciBnnLsDefCpCpSessionSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciBnnLsDefCpCpSessionSupport.setStatus("mandatory")


class _AppnDlciBnnLsDefMaxTxBtuSize_Type(Unsigned32):
    """Custom type appnDlciBnnLsDefMaxTxBtuSize based on Unsigned32"""
    defaultValue = 2048

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(99, 32768),
    )


_AppnDlciBnnLsDefMaxTxBtuSize_Type.__name__ = "Unsigned32"
_AppnDlciBnnLsDefMaxTxBtuSize_Object = MibTableColumn
appnDlciBnnLsDefMaxTxBtuSize = _AppnDlciBnnLsDefMaxTxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 4, 2, 1, 11),
    _AppnDlciBnnLsDefMaxTxBtuSize_Type()
)
appnDlciBnnLsDefMaxTxBtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciBnnLsDefMaxTxBtuSize.setStatus("mandatory")


class _AppnDlciBnnLsDefLsRole_Type(Integer32):
    """Custom type appnDlciBnnLsDefLsRole based on Integer32"""
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


_AppnDlciBnnLsDefLsRole_Type.__name__ = "Integer32"
_AppnDlciBnnLsDefLsRole_Object = MibTableColumn
appnDlciBnnLsDefLsRole = _AppnDlciBnnLsDefLsRole_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 4, 2, 1, 12),
    _AppnDlciBnnLsDefLsRole_Type()
)
appnDlciBnnLsDefLsRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciBnnLsDefLsRole.setStatus("mandatory")
_AppnDlciSp_ObjectIdentity = ObjectIdentity
appnDlciSp = _AppnDlciSp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 5)
)
_AppnDlciSpRowStatusTable_Object = MibTable
appnDlciSpRowStatusTable = _AppnDlciSpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 5, 1)
)
if mibBuilder.loadTexts:
    appnDlciSpRowStatusTable.setStatus("mandatory")
_AppnDlciSpRowStatusEntry_Object = MibTableRow
appnDlciSpRowStatusEntry = _AppnDlciSpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 5, 1, 1)
)
appnDlciSpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciSpIndex"),
)
if mibBuilder.loadTexts:
    appnDlciSpRowStatusEntry.setStatus("mandatory")
_AppnDlciSpRowStatus_Type = RowStatus
_AppnDlciSpRowStatus_Object = MibTableColumn
appnDlciSpRowStatus = _AppnDlciSpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 5, 1, 1, 1),
    _AppnDlciSpRowStatus_Type()
)
appnDlciSpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciSpRowStatus.setStatus("mandatory")
_AppnDlciSpComponentName_Type = DisplayString
_AppnDlciSpComponentName_Object = MibTableColumn
appnDlciSpComponentName = _AppnDlciSpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 5, 1, 1, 2),
    _AppnDlciSpComponentName_Type()
)
appnDlciSpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciSpComponentName.setStatus("mandatory")
_AppnDlciSpStorageType_Type = StorageType
_AppnDlciSpStorageType_Object = MibTableColumn
appnDlciSpStorageType = _AppnDlciSpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 5, 1, 1, 4),
    _AppnDlciSpStorageType_Type()
)
appnDlciSpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciSpStorageType.setStatus("mandatory")
_AppnDlciSpIndex_Type = NonReplicated
_AppnDlciSpIndex_Object = MibTableColumn
appnDlciSpIndex = _AppnDlciSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 5, 1, 1, 10),
    _AppnDlciSpIndex_Type()
)
appnDlciSpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnDlciSpIndex.setStatus("mandatory")
_AppnDlciSpParmsTable_Object = MibTable
appnDlciSpParmsTable = _AppnDlciSpParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 5, 11)
)
if mibBuilder.loadTexts:
    appnDlciSpParmsTable.setStatus("mandatory")
_AppnDlciSpParmsEntry_Object = MibTableRow
appnDlciSpParmsEntry = _AppnDlciSpParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 5, 11, 1)
)
appnDlciSpParmsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciSpIndex"),
)
if mibBuilder.loadTexts:
    appnDlciSpParmsEntry.setStatus("mandatory")


class _AppnDlciSpRateEnforcement_Type(Integer32):
    """Custom type appnDlciSpRateEnforcement based on Integer32"""
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


_AppnDlciSpRateEnforcement_Type.__name__ = "Integer32"
_AppnDlciSpRateEnforcement_Object = MibTableColumn
appnDlciSpRateEnforcement = _AppnDlciSpRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 5, 11, 1, 1),
    _AppnDlciSpRateEnforcement_Type()
)
appnDlciSpRateEnforcement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciSpRateEnforcement.setStatus("mandatory")


class _AppnDlciSpCommittedInformationRate_Type(Unsigned32):
    """Custom type appnDlciSpCommittedInformationRate based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_AppnDlciSpCommittedInformationRate_Type.__name__ = "Unsigned32"
_AppnDlciSpCommittedInformationRate_Object = MibTableColumn
appnDlciSpCommittedInformationRate = _AppnDlciSpCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 5, 11, 1, 2),
    _AppnDlciSpCommittedInformationRate_Type()
)
appnDlciSpCommittedInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciSpCommittedInformationRate.setStatus("mandatory")


class _AppnDlciSpCommittedBurstSize_Type(Unsigned32):
    """Custom type appnDlciSpCommittedBurstSize based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_AppnDlciSpCommittedBurstSize_Type.__name__ = "Unsigned32"
_AppnDlciSpCommittedBurstSize_Object = MibTableColumn
appnDlciSpCommittedBurstSize = _AppnDlciSpCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 5, 11, 1, 3),
    _AppnDlciSpCommittedBurstSize_Type()
)
appnDlciSpCommittedBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciSpCommittedBurstSize.setStatus("mandatory")


class _AppnDlciSpExcessBurstSize_Type(Unsigned32):
    """Custom type appnDlciSpExcessBurstSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_AppnDlciSpExcessBurstSize_Type.__name__ = "Unsigned32"
_AppnDlciSpExcessBurstSize_Object = MibTableColumn
appnDlciSpExcessBurstSize = _AppnDlciSpExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 5, 11, 1, 4),
    _AppnDlciSpExcessBurstSize_Type()
)
appnDlciSpExcessBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciSpExcessBurstSize.setStatus("mandatory")


class _AppnDlciSpMeasurementInterval_Type(Unsigned32):
    """Custom type appnDlciSpMeasurementInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25500),
    )


_AppnDlciSpMeasurementInterval_Type.__name__ = "Unsigned32"
_AppnDlciSpMeasurementInterval_Object = MibTableColumn
appnDlciSpMeasurementInterval = _AppnDlciSpMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 5, 11, 1, 5),
    _AppnDlciSpMeasurementInterval_Type()
)
appnDlciSpMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciSpMeasurementInterval.setStatus("mandatory")
_AppnDlciBanLsDef_ObjectIdentity = ObjectIdentity
appnDlciBanLsDef = _AppnDlciBanLsDef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 6)
)
_AppnDlciBanLsDefRowStatusTable_Object = MibTable
appnDlciBanLsDefRowStatusTable = _AppnDlciBanLsDefRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 6, 1)
)
if mibBuilder.loadTexts:
    appnDlciBanLsDefRowStatusTable.setStatus("mandatory")
_AppnDlciBanLsDefRowStatusEntry_Object = MibTableRow
appnDlciBanLsDefRowStatusEntry = _AppnDlciBanLsDefRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 6, 1, 1)
)
appnDlciBanLsDefRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciBanLsDefMacIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciBanLsDefSapIndex"),
)
if mibBuilder.loadTexts:
    appnDlciBanLsDefRowStatusEntry.setStatus("mandatory")
_AppnDlciBanLsDefRowStatus_Type = RowStatus
_AppnDlciBanLsDefRowStatus_Object = MibTableColumn
appnDlciBanLsDefRowStatus = _AppnDlciBanLsDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 6, 1, 1, 1),
    _AppnDlciBanLsDefRowStatus_Type()
)
appnDlciBanLsDefRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciBanLsDefRowStatus.setStatus("mandatory")
_AppnDlciBanLsDefComponentName_Type = DisplayString
_AppnDlciBanLsDefComponentName_Object = MibTableColumn
appnDlciBanLsDefComponentName = _AppnDlciBanLsDefComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 6, 1, 1, 2),
    _AppnDlciBanLsDefComponentName_Type()
)
appnDlciBanLsDefComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciBanLsDefComponentName.setStatus("mandatory")
_AppnDlciBanLsDefStorageType_Type = StorageType
_AppnDlciBanLsDefStorageType_Object = MibTableColumn
appnDlciBanLsDefStorageType = _AppnDlciBanLsDefStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 6, 1, 1, 4),
    _AppnDlciBanLsDefStorageType_Type()
)
appnDlciBanLsDefStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciBanLsDefStorageType.setStatus("mandatory")


class _AppnDlciBanLsDefMacIndex_Type(DashedHexString):
    """Custom type appnDlciBanLsDefMacIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AppnDlciBanLsDefMacIndex_Type.__name__ = "DashedHexString"
_AppnDlciBanLsDefMacIndex_Object = MibTableColumn
appnDlciBanLsDefMacIndex = _AppnDlciBanLsDefMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 6, 1, 1, 10),
    _AppnDlciBanLsDefMacIndex_Type()
)
appnDlciBanLsDefMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnDlciBanLsDefMacIndex.setStatus("mandatory")


class _AppnDlciBanLsDefSapIndex_Type(Integer32):
    """Custom type appnDlciBanLsDefSapIndex based on Integer32"""
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


_AppnDlciBanLsDefSapIndex_Type.__name__ = "Integer32"
_AppnDlciBanLsDefSapIndex_Object = MibTableColumn
appnDlciBanLsDefSapIndex = _AppnDlciBanLsDefSapIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 6, 1, 1, 11),
    _AppnDlciBanLsDefSapIndex_Type()
)
appnDlciBanLsDefSapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnDlciBanLsDefSapIndex.setStatus("mandatory")
_AppnDlciBanLsDefProvTable_Object = MibTable
appnDlciBanLsDefProvTable = _AppnDlciBanLsDefProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 6, 2)
)
if mibBuilder.loadTexts:
    appnDlciBanLsDefProvTable.setStatus("mandatory")
_AppnDlciBanLsDefProvEntry_Object = MibTableRow
appnDlciBanLsDefProvEntry = _AppnDlciBanLsDefProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 6, 2, 1)
)
appnDlciBanLsDefProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciBanLsDefMacIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciBanLsDefSapIndex"),
)
if mibBuilder.loadTexts:
    appnDlciBanLsDefProvEntry.setStatus("mandatory")


class _AppnDlciBanLsDefDspuService_Type(Integer32):
    """Custom type appnDlciBanLsDefDspuService based on Integer32"""
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


_AppnDlciBanLsDefDspuService_Type.__name__ = "Integer32"
_AppnDlciBanLsDefDspuService_Object = MibTableColumn
appnDlciBanLsDefDspuService = _AppnDlciBanLsDefDspuService_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 6, 2, 1, 1),
    _AppnDlciBanLsDefDspuService_Type()
)
appnDlciBanLsDefDspuService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciBanLsDefDspuService.setStatus("mandatory")


class _AppnDlciBanLsDefAdjacentCpName_Type(AsciiString):
    """Custom type appnDlciBanLsDefAdjacentCpName based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_AppnDlciBanLsDefAdjacentCpName_Type.__name__ = "AsciiString"
_AppnDlciBanLsDefAdjacentCpName_Object = MibTableColumn
appnDlciBanLsDefAdjacentCpName = _AppnDlciBanLsDefAdjacentCpName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 6, 2, 1, 2),
    _AppnDlciBanLsDefAdjacentCpName_Type()
)
appnDlciBanLsDefAdjacentCpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciBanLsDefAdjacentCpName.setStatus("mandatory")


class _AppnDlciBanLsDefAdjacentCpType_Type(Integer32):
    """Custom type appnDlciBanLsDefAdjacentCpType based on Integer32"""
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


_AppnDlciBanLsDefAdjacentCpType_Type.__name__ = "Integer32"
_AppnDlciBanLsDefAdjacentCpType_Object = MibTableColumn
appnDlciBanLsDefAdjacentCpType = _AppnDlciBanLsDefAdjacentCpType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 6, 2, 1, 3),
    _AppnDlciBanLsDefAdjacentCpType_Type()
)
appnDlciBanLsDefAdjacentCpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciBanLsDefAdjacentCpType.setStatus("mandatory")


class _AppnDlciBanLsDefTgNum_Type(Unsigned32):
    """Custom type appnDlciBanLsDefTgNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_AppnDlciBanLsDefTgNum_Type.__name__ = "Unsigned32"
_AppnDlciBanLsDefTgNum_Object = MibTableColumn
appnDlciBanLsDefTgNum = _AppnDlciBanLsDefTgNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 6, 2, 1, 5),
    _AppnDlciBanLsDefTgNum_Type()
)
appnDlciBanLsDefTgNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciBanLsDefTgNum.setStatus("mandatory")


class _AppnDlciBanLsDefDlusName_Type(AsciiString):
    """Custom type appnDlciBanLsDefDlusName based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_AppnDlciBanLsDefDlusName_Type.__name__ = "AsciiString"
_AppnDlciBanLsDefDlusName_Object = MibTableColumn
appnDlciBanLsDefDlusName = _AppnDlciBanLsDefDlusName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 6, 2, 1, 6),
    _AppnDlciBanLsDefDlusName_Type()
)
appnDlciBanLsDefDlusName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciBanLsDefDlusName.setStatus("mandatory")


class _AppnDlciBanLsDefBackupDlusName_Type(AsciiString):
    """Custom type appnDlciBanLsDefBackupDlusName based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_AppnDlciBanLsDefBackupDlusName_Type.__name__ = "AsciiString"
_AppnDlciBanLsDefBackupDlusName_Object = MibTableColumn
appnDlciBanLsDefBackupDlusName = _AppnDlciBanLsDefBackupDlusName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 6, 2, 1, 7),
    _AppnDlciBanLsDefBackupDlusName_Type()
)
appnDlciBanLsDefBackupDlusName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciBanLsDefBackupDlusName.setStatus("mandatory")


class _AppnDlciBanLsDefHprSupported_Type(Integer32):
    """Custom type appnDlciBanLsDefHprSupported based on Integer32"""
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


_AppnDlciBanLsDefHprSupported_Type.__name__ = "Integer32"
_AppnDlciBanLsDefHprSupported_Object = MibTableColumn
appnDlciBanLsDefHprSupported = _AppnDlciBanLsDefHprSupported_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 6, 2, 1, 8),
    _AppnDlciBanLsDefHprSupported_Type()
)
appnDlciBanLsDefHprSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciBanLsDefHprSupported.setStatus("mandatory")


class _AppnDlciBanLsDefAdjacentNodeID_Type(Hex):
    """Custom type appnDlciBanLsDefAdjacentNodeID based on Hex"""
    defaultValue = 0

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AppnDlciBanLsDefAdjacentNodeID_Type.__name__ = "Hex"
_AppnDlciBanLsDefAdjacentNodeID_Object = MibTableColumn
appnDlciBanLsDefAdjacentNodeID = _AppnDlciBanLsDefAdjacentNodeID_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 6, 2, 1, 9),
    _AppnDlciBanLsDefAdjacentNodeID_Type()
)
appnDlciBanLsDefAdjacentNodeID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciBanLsDefAdjacentNodeID.setStatus("mandatory")


class _AppnDlciBanLsDefCpCpSessionSupport_Type(Integer32):
    """Custom type appnDlciBanLsDefCpCpSessionSupport based on Integer32"""
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


_AppnDlciBanLsDefCpCpSessionSupport_Type.__name__ = "Integer32"
_AppnDlciBanLsDefCpCpSessionSupport_Object = MibTableColumn
appnDlciBanLsDefCpCpSessionSupport = _AppnDlciBanLsDefCpCpSessionSupport_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 6, 2, 1, 10),
    _AppnDlciBanLsDefCpCpSessionSupport_Type()
)
appnDlciBanLsDefCpCpSessionSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciBanLsDefCpCpSessionSupport.setStatus("mandatory")


class _AppnDlciBanLsDefMaxTxBtuSize_Type(Unsigned32):
    """Custom type appnDlciBanLsDefMaxTxBtuSize based on Unsigned32"""
    defaultValue = 2048

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(99, 32768),
    )


_AppnDlciBanLsDefMaxTxBtuSize_Type.__name__ = "Unsigned32"
_AppnDlciBanLsDefMaxTxBtuSize_Object = MibTableColumn
appnDlciBanLsDefMaxTxBtuSize = _AppnDlciBanLsDefMaxTxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 6, 2, 1, 11),
    _AppnDlciBanLsDefMaxTxBtuSize_Type()
)
appnDlciBanLsDefMaxTxBtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciBanLsDefMaxTxBtuSize.setStatus("mandatory")


class _AppnDlciBanLsDefLsRole_Type(Integer32):
    """Custom type appnDlciBanLsDefLsRole based on Integer32"""
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


_AppnDlciBanLsDefLsRole_Type.__name__ = "Integer32"
_AppnDlciBanLsDefLsRole_Object = MibTableColumn
appnDlciBanLsDefLsRole = _AppnDlciBanLsDefLsRole_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 6, 2, 1, 12),
    _AppnDlciBanLsDefLsRole_Type()
)
appnDlciBanLsDefLsRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciBanLsDefLsRole.setStatus("mandatory")
_AppnDlciBan_ObjectIdentity = ObjectIdentity
appnDlciBan = _AppnDlciBan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 7)
)
_AppnDlciBanRowStatusTable_Object = MibTable
appnDlciBanRowStatusTable = _AppnDlciBanRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 7, 1)
)
if mibBuilder.loadTexts:
    appnDlciBanRowStatusTable.setStatus("mandatory")
_AppnDlciBanRowStatusEntry_Object = MibTableRow
appnDlciBanRowStatusEntry = _AppnDlciBanRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 7, 1, 1)
)
appnDlciBanRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciBanIndex"),
)
if mibBuilder.loadTexts:
    appnDlciBanRowStatusEntry.setStatus("mandatory")
_AppnDlciBanRowStatus_Type = RowStatus
_AppnDlciBanRowStatus_Object = MibTableColumn
appnDlciBanRowStatus = _AppnDlciBanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 7, 1, 1, 1),
    _AppnDlciBanRowStatus_Type()
)
appnDlciBanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciBanRowStatus.setStatus("mandatory")
_AppnDlciBanComponentName_Type = DisplayString
_AppnDlciBanComponentName_Object = MibTableColumn
appnDlciBanComponentName = _AppnDlciBanComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 7, 1, 1, 2),
    _AppnDlciBanComponentName_Type()
)
appnDlciBanComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciBanComponentName.setStatus("mandatory")
_AppnDlciBanStorageType_Type = StorageType
_AppnDlciBanStorageType_Object = MibTableColumn
appnDlciBanStorageType = _AppnDlciBanStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 7, 1, 1, 4),
    _AppnDlciBanStorageType_Type()
)
appnDlciBanStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciBanStorageType.setStatus("mandatory")
_AppnDlciBanIndex_Type = NonReplicated
_AppnDlciBanIndex_Object = MibTableColumn
appnDlciBanIndex = _AppnDlciBanIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 7, 1, 1, 10),
    _AppnDlciBanIndex_Type()
)
appnDlciBanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnDlciBanIndex.setStatus("mandatory")
_AppnDlciBanProvTable_Object = MibTable
appnDlciBanProvTable = _AppnDlciBanProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 7, 2)
)
if mibBuilder.loadTexts:
    appnDlciBanProvTable.setStatus("mandatory")
_AppnDlciBanProvEntry_Object = MibTableRow
appnDlciBanProvEntry = _AppnDlciBanProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 7, 2, 1)
)
appnDlciBanProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciBanIndex"),
)
if mibBuilder.loadTexts:
    appnDlciBanProvEntry.setStatus("mandatory")


class _AppnDlciBanLocalMac_Type(DashedHexString):
    """Custom type appnDlciBanLocalMac based on DashedHexString"""
    defaultHexValue = "4fff00000000"

    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AppnDlciBanLocalMac_Type.__name__ = "DashedHexString"
_AppnDlciBanLocalMac_Object = MibTableColumn
appnDlciBanLocalMac = _AppnDlciBanLocalMac_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 7, 2, 1, 1),
    _AppnDlciBanLocalMac_Type()
)
appnDlciBanLocalMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciBanLocalMac.setStatus("mandatory")


class _AppnDlciBanLocalSap_Type(Hex):
    """Custom type appnDlciBanLocalSap based on Hex"""
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


_AppnDlciBanLocalSap_Type.__name__ = "Hex"
_AppnDlciBanLocalSap_Object = MibTableColumn
appnDlciBanLocalSap = _AppnDlciBanLocalSap_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 7, 2, 1, 2),
    _AppnDlciBanLocalSap_Type()
)
appnDlciBanLocalSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciBanLocalSap.setStatus("mandatory")
_AppnDlciCn_ObjectIdentity = ObjectIdentity
appnDlciCn = _AppnDlciCn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 8)
)
_AppnDlciCnRowStatusTable_Object = MibTable
appnDlciCnRowStatusTable = _AppnDlciCnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 8, 1)
)
if mibBuilder.loadTexts:
    appnDlciCnRowStatusTable.setStatus("mandatory")
_AppnDlciCnRowStatusEntry_Object = MibTableRow
appnDlciCnRowStatusEntry = _AppnDlciCnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 8, 1, 1)
)
appnDlciCnRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciCnIndex"),
)
if mibBuilder.loadTexts:
    appnDlciCnRowStatusEntry.setStatus("mandatory")
_AppnDlciCnRowStatus_Type = RowStatus
_AppnDlciCnRowStatus_Object = MibTableColumn
appnDlciCnRowStatus = _AppnDlciCnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 8, 1, 1, 1),
    _AppnDlciCnRowStatus_Type()
)
appnDlciCnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlciCnRowStatus.setStatus("mandatory")
_AppnDlciCnComponentName_Type = DisplayString
_AppnDlciCnComponentName_Object = MibTableColumn
appnDlciCnComponentName = _AppnDlciCnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 8, 1, 1, 2),
    _AppnDlciCnComponentName_Type()
)
appnDlciCnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciCnComponentName.setStatus("mandatory")
_AppnDlciCnStorageType_Type = StorageType
_AppnDlciCnStorageType_Object = MibTableColumn
appnDlciCnStorageType = _AppnDlciCnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 8, 1, 1, 4),
    _AppnDlciCnStorageType_Type()
)
appnDlciCnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciCnStorageType.setStatus("mandatory")


class _AppnDlciCnIndex_Type(AsciiStringIndex):
    """Custom type appnDlciCnIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppnDlciCnIndex_Type.__name__ = "AsciiStringIndex"
_AppnDlciCnIndex_Object = MibTableColumn
appnDlciCnIndex = _AppnDlciCnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 8, 1, 1, 10),
    _AppnDlciCnIndex_Type()
)
appnDlciCnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnDlciCnIndex.setStatus("mandatory")
_AppnDlciStateTable_Object = MibTable
appnDlciStateTable = _AppnDlciStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 10)
)
if mibBuilder.loadTexts:
    appnDlciStateTable.setStatus("mandatory")
_AppnDlciStateEntry_Object = MibTableRow
appnDlciStateEntry = _AppnDlciStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 10, 1)
)
appnDlciStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciIndex"),
)
if mibBuilder.loadTexts:
    appnDlciStateEntry.setStatus("mandatory")


class _AppnDlciAdminState_Type(Integer32):
    """Custom type appnDlciAdminState based on Integer32"""
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


_AppnDlciAdminState_Type.__name__ = "Integer32"
_AppnDlciAdminState_Object = MibTableColumn
appnDlciAdminState = _AppnDlciAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 10, 1, 1),
    _AppnDlciAdminState_Type()
)
appnDlciAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciAdminState.setStatus("mandatory")


class _AppnDlciOperationalState_Type(Integer32):
    """Custom type appnDlciOperationalState based on Integer32"""
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


_AppnDlciOperationalState_Type.__name__ = "Integer32"
_AppnDlciOperationalState_Object = MibTableColumn
appnDlciOperationalState = _AppnDlciOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 10, 1, 2),
    _AppnDlciOperationalState_Type()
)
appnDlciOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciOperationalState.setStatus("mandatory")


class _AppnDlciUsageState_Type(Integer32):
    """Custom type appnDlciUsageState based on Integer32"""
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


_AppnDlciUsageState_Type.__name__ = "Integer32"
_AppnDlciUsageState_Object = MibTableColumn
appnDlciUsageState = _AppnDlciUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 10, 1, 3),
    _AppnDlciUsageState_Type()
)
appnDlciUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciUsageState.setStatus("mandatory")
_AppnDlciSpOpTable_Object = MibTable
appnDlciSpOpTable = _AppnDlciSpOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 12)
)
if mibBuilder.loadTexts:
    appnDlciSpOpTable.setStatus("mandatory")
_AppnDlciSpOpEntry_Object = MibTableRow
appnDlciSpOpEntry = _AppnDlciSpOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 12, 1)
)
appnDlciSpOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlciIndex"),
)
if mibBuilder.loadTexts:
    appnDlciSpOpEntry.setStatus("mandatory")


class _AppnDlciRateEnforcement_Type(Integer32):
    """Custom type appnDlciRateEnforcement based on Integer32"""
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


_AppnDlciRateEnforcement_Type.__name__ = "Integer32"
_AppnDlciRateEnforcement_Object = MibTableColumn
appnDlciRateEnforcement = _AppnDlciRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 12, 1, 1),
    _AppnDlciRateEnforcement_Type()
)
appnDlciRateEnforcement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciRateEnforcement.setStatus("mandatory")


class _AppnDlciCommittedInformationRate_Type(Gauge32):
    """Custom type appnDlciCommittedInformationRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AppnDlciCommittedInformationRate_Type.__name__ = "Gauge32"
_AppnDlciCommittedInformationRate_Object = MibTableColumn
appnDlciCommittedInformationRate = _AppnDlciCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 12, 1, 2),
    _AppnDlciCommittedInformationRate_Type()
)
appnDlciCommittedInformationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciCommittedInformationRate.setStatus("mandatory")


class _AppnDlciCommittedBurstSize_Type(Gauge32):
    """Custom type appnDlciCommittedBurstSize based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AppnDlciCommittedBurstSize_Type.__name__ = "Gauge32"
_AppnDlciCommittedBurstSize_Object = MibTableColumn
appnDlciCommittedBurstSize = _AppnDlciCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 12, 1, 3),
    _AppnDlciCommittedBurstSize_Type()
)
appnDlciCommittedBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciCommittedBurstSize.setStatus("mandatory")


class _AppnDlciExcessInformationRate_Type(Gauge32):
    """Custom type appnDlciExcessInformationRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AppnDlciExcessInformationRate_Type.__name__ = "Gauge32"
_AppnDlciExcessInformationRate_Object = MibTableColumn
appnDlciExcessInformationRate = _AppnDlciExcessInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 12, 1, 4),
    _AppnDlciExcessInformationRate_Type()
)
appnDlciExcessInformationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciExcessInformationRate.setStatus("mandatory")


class _AppnDlciExcessBurstSize_Type(Gauge32):
    """Custom type appnDlciExcessBurstSize based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_AppnDlciExcessBurstSize_Type.__name__ = "Gauge32"
_AppnDlciExcessBurstSize_Object = MibTableColumn
appnDlciExcessBurstSize = _AppnDlciExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 12, 1, 5),
    _AppnDlciExcessBurstSize_Type()
)
appnDlciExcessBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciExcessBurstSize.setStatus("mandatory")


class _AppnDlciMeasurementInterval_Type(Gauge32):
    """Custom type appnDlciMeasurementInterval based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25500),
    )


_AppnDlciMeasurementInterval_Type.__name__ = "Gauge32"
_AppnDlciMeasurementInterval_Object = MibTableColumn
appnDlciMeasurementInterval = _AppnDlciMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 3, 12, 1, 6),
    _AppnDlciMeasurementInterval_Type()
)
appnDlciMeasurementInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlciMeasurementInterval.setStatus("mandatory")
_AppnLcn_ObjectIdentity = ObjectIdentity
appnLcn = _AppnLcn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4)
)
_AppnLcnRowStatusTable_Object = MibTable
appnLcnRowStatusTable = _AppnLcnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 1)
)
if mibBuilder.loadTexts:
    appnLcnRowStatusTable.setStatus("mandatory")
_AppnLcnRowStatusEntry_Object = MibTableRow
appnLcnRowStatusEntry = _AppnLcnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 1, 1)
)
appnLcnRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnLcnIndex"),
)
if mibBuilder.loadTexts:
    appnLcnRowStatusEntry.setStatus("mandatory")
_AppnLcnRowStatus_Type = RowStatus
_AppnLcnRowStatus_Object = MibTableColumn
appnLcnRowStatus = _AppnLcnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 1, 1, 1),
    _AppnLcnRowStatus_Type()
)
appnLcnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnLcnRowStatus.setStatus("mandatory")
_AppnLcnComponentName_Type = DisplayString
_AppnLcnComponentName_Object = MibTableColumn
appnLcnComponentName = _AppnLcnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 1, 1, 2),
    _AppnLcnComponentName_Type()
)
appnLcnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnComponentName.setStatus("mandatory")
_AppnLcnStorageType_Type = StorageType
_AppnLcnStorageType_Object = MibTableColumn
appnLcnStorageType = _AppnLcnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 1, 1, 4),
    _AppnLcnStorageType_Type()
)
appnLcnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnStorageType.setStatus("mandatory")


class _AppnLcnIndex_Type(Integer32):
    """Custom type appnLcnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AppnLcnIndex_Type.__name__ = "Integer32"
_AppnLcnIndex_Object = MibTableColumn
appnLcnIndex = _AppnLcnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 1, 1, 10),
    _AppnLcnIndex_Type()
)
appnLcnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnLcnIndex.setStatus("mandatory")
_AppnLcnDc_ObjectIdentity = ObjectIdentity
appnLcnDc = _AppnLcnDc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 2)
)
_AppnLcnDcRowStatusTable_Object = MibTable
appnLcnDcRowStatusTable = _AppnLcnDcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 2, 1)
)
if mibBuilder.loadTexts:
    appnLcnDcRowStatusTable.setStatus("mandatory")
_AppnLcnDcRowStatusEntry_Object = MibTableRow
appnLcnDcRowStatusEntry = _AppnLcnDcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 2, 1, 1)
)
appnLcnDcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnLcnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnLcnDcIndex"),
)
if mibBuilder.loadTexts:
    appnLcnDcRowStatusEntry.setStatus("mandatory")
_AppnLcnDcRowStatus_Type = RowStatus
_AppnLcnDcRowStatus_Object = MibTableColumn
appnLcnDcRowStatus = _AppnLcnDcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 2, 1, 1, 1),
    _AppnLcnDcRowStatus_Type()
)
appnLcnDcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnDcRowStatus.setStatus("mandatory")
_AppnLcnDcComponentName_Type = DisplayString
_AppnLcnDcComponentName_Object = MibTableColumn
appnLcnDcComponentName = _AppnLcnDcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 2, 1, 1, 2),
    _AppnLcnDcComponentName_Type()
)
appnLcnDcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnDcComponentName.setStatus("mandatory")
_AppnLcnDcStorageType_Type = StorageType
_AppnLcnDcStorageType_Object = MibTableColumn
appnLcnDcStorageType = _AppnLcnDcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 2, 1, 1, 4),
    _AppnLcnDcStorageType_Type()
)
appnLcnDcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnDcStorageType.setStatus("mandatory")
_AppnLcnDcIndex_Type = NonReplicated
_AppnLcnDcIndex_Object = MibTableColumn
appnLcnDcIndex = _AppnLcnDcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 2, 1, 1, 10),
    _AppnLcnDcIndex_Type()
)
appnLcnDcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnLcnDcIndex.setStatus("mandatory")
_AppnLcnDcOptionsTable_Object = MibTable
appnLcnDcOptionsTable = _AppnLcnDcOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 2, 10)
)
if mibBuilder.loadTexts:
    appnLcnDcOptionsTable.setStatus("mandatory")
_AppnLcnDcOptionsEntry_Object = MibTableRow
appnLcnDcOptionsEntry = _AppnLcnDcOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 2, 10, 1)
)
appnLcnDcOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnLcnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnLcnDcIndex"),
)
if mibBuilder.loadTexts:
    appnLcnDcOptionsEntry.setStatus("mandatory")


class _AppnLcnDcRemoteNpi_Type(Integer32):
    """Custom type appnLcnDcRemoteNpi based on Integer32"""
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


_AppnLcnDcRemoteNpi_Type.__name__ = "Integer32"
_AppnLcnDcRemoteNpi_Object = MibTableColumn
appnLcnDcRemoteNpi = _AppnLcnDcRemoteNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 2, 10, 1, 3),
    _AppnLcnDcRemoteNpi_Type()
)
appnLcnDcRemoteNpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnLcnDcRemoteNpi.setStatus("mandatory")


class _AppnLcnDcRemoteDna_Type(DigitString):
    """Custom type appnLcnDcRemoteDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AppnLcnDcRemoteDna_Type.__name__ = "DigitString"
_AppnLcnDcRemoteDna_Object = MibTableColumn
appnLcnDcRemoteDna = _AppnLcnDcRemoteDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 2, 10, 1, 4),
    _AppnLcnDcRemoteDna_Type()
)
appnLcnDcRemoteDna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnLcnDcRemoteDna.setStatus("mandatory")


class _AppnLcnDcTransferPriority_Type(Integer32):
    """Custom type appnLcnDcTransferPriority based on Integer32"""
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


_AppnLcnDcTransferPriority_Type.__name__ = "Integer32"
_AppnLcnDcTransferPriority_Object = MibTableColumn
appnLcnDcTransferPriority = _AppnLcnDcTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 2, 10, 1, 9),
    _AppnLcnDcTransferPriority_Type()
)
appnLcnDcTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnLcnDcTransferPriority.setStatus("mandatory")


class _AppnLcnDcDiscardPriority_Type(Integer32):
    """Custom type appnLcnDcDiscardPriority based on Integer32"""
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


_AppnLcnDcDiscardPriority_Type.__name__ = "Integer32"
_AppnLcnDcDiscardPriority_Object = MibTableColumn
appnLcnDcDiscardPriority = _AppnLcnDcDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 2, 10, 1, 10),
    _AppnLcnDcDiscardPriority_Type()
)
appnLcnDcDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnLcnDcDiscardPriority.setStatus("mandatory")
_AppnLcnVc_ObjectIdentity = ObjectIdentity
appnLcnVc = _AppnLcnVc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3)
)
_AppnLcnVcRowStatusTable_Object = MibTable
appnLcnVcRowStatusTable = _AppnLcnVcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 1)
)
if mibBuilder.loadTexts:
    appnLcnVcRowStatusTable.setStatus("mandatory")
_AppnLcnVcRowStatusEntry_Object = MibTableRow
appnLcnVcRowStatusEntry = _AppnLcnVcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 1, 1)
)
appnLcnVcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnLcnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnLcnVcIndex"),
)
if mibBuilder.loadTexts:
    appnLcnVcRowStatusEntry.setStatus("mandatory")
_AppnLcnVcRowStatus_Type = RowStatus
_AppnLcnVcRowStatus_Object = MibTableColumn
appnLcnVcRowStatus = _AppnLcnVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 1, 1, 1),
    _AppnLcnVcRowStatus_Type()
)
appnLcnVcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcRowStatus.setStatus("mandatory")
_AppnLcnVcComponentName_Type = DisplayString
_AppnLcnVcComponentName_Object = MibTableColumn
appnLcnVcComponentName = _AppnLcnVcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 1, 1, 2),
    _AppnLcnVcComponentName_Type()
)
appnLcnVcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcComponentName.setStatus("mandatory")
_AppnLcnVcStorageType_Type = StorageType
_AppnLcnVcStorageType_Object = MibTableColumn
appnLcnVcStorageType = _AppnLcnVcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 1, 1, 4),
    _AppnLcnVcStorageType_Type()
)
appnLcnVcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcStorageType.setStatus("mandatory")
_AppnLcnVcIndex_Type = NonReplicated
_AppnLcnVcIndex_Object = MibTableColumn
appnLcnVcIndex = _AppnLcnVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 1, 1, 10),
    _AppnLcnVcIndex_Type()
)
appnLcnVcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnLcnVcIndex.setStatus("mandatory")
_AppnLcnVcCadTable_Object = MibTable
appnLcnVcCadTable = _AppnLcnVcCadTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 10)
)
if mibBuilder.loadTexts:
    appnLcnVcCadTable.setStatus("mandatory")
_AppnLcnVcCadEntry_Object = MibTableRow
appnLcnVcCadEntry = _AppnLcnVcCadEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 10, 1)
)
appnLcnVcCadEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnLcnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnLcnVcIndex"),
)
if mibBuilder.loadTexts:
    appnLcnVcCadEntry.setStatus("mandatory")


class _AppnLcnVcType_Type(Integer32):
    """Custom type appnLcnVcType based on Integer32"""
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


_AppnLcnVcType_Type.__name__ = "Integer32"
_AppnLcnVcType_Object = MibTableColumn
appnLcnVcType = _AppnLcnVcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 10, 1, 1),
    _AppnLcnVcType_Type()
)
appnLcnVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcType.setStatus("mandatory")


class _AppnLcnVcState_Type(Integer32):
    """Custom type appnLcnVcState based on Integer32"""
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


_AppnLcnVcState_Type.__name__ = "Integer32"
_AppnLcnVcState_Object = MibTableColumn
appnLcnVcState = _AppnLcnVcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 10, 1, 2),
    _AppnLcnVcState_Type()
)
appnLcnVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcState.setStatus("mandatory")


class _AppnLcnVcPreviousState_Type(Integer32):
    """Custom type appnLcnVcPreviousState based on Integer32"""
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


_AppnLcnVcPreviousState_Type.__name__ = "Integer32"
_AppnLcnVcPreviousState_Object = MibTableColumn
appnLcnVcPreviousState = _AppnLcnVcPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 10, 1, 3),
    _AppnLcnVcPreviousState_Type()
)
appnLcnVcPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcPreviousState.setStatus("mandatory")


class _AppnLcnVcDiagnosticCode_Type(Unsigned32):
    """Custom type appnLcnVcDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnLcnVcDiagnosticCode_Type.__name__ = "Unsigned32"
_AppnLcnVcDiagnosticCode_Object = MibTableColumn
appnLcnVcDiagnosticCode = _AppnLcnVcDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 10, 1, 4),
    _AppnLcnVcDiagnosticCode_Type()
)
appnLcnVcDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcDiagnosticCode.setStatus("mandatory")


class _AppnLcnVcPreviousDiagnosticCode_Type(Unsigned32):
    """Custom type appnLcnVcPreviousDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnLcnVcPreviousDiagnosticCode_Type.__name__ = "Unsigned32"
_AppnLcnVcPreviousDiagnosticCode_Object = MibTableColumn
appnLcnVcPreviousDiagnosticCode = _AppnLcnVcPreviousDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 10, 1, 5),
    _AppnLcnVcPreviousDiagnosticCode_Type()
)
appnLcnVcPreviousDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcPreviousDiagnosticCode.setStatus("mandatory")


class _AppnLcnVcCalledNpi_Type(Integer32):
    """Custom type appnLcnVcCalledNpi based on Integer32"""
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


_AppnLcnVcCalledNpi_Type.__name__ = "Integer32"
_AppnLcnVcCalledNpi_Object = MibTableColumn
appnLcnVcCalledNpi = _AppnLcnVcCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 10, 1, 6),
    _AppnLcnVcCalledNpi_Type()
)
appnLcnVcCalledNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcCalledNpi.setStatus("mandatory")


class _AppnLcnVcCalledDna_Type(DigitString):
    """Custom type appnLcnVcCalledDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AppnLcnVcCalledDna_Type.__name__ = "DigitString"
_AppnLcnVcCalledDna_Object = MibTableColumn
appnLcnVcCalledDna = _AppnLcnVcCalledDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 10, 1, 7),
    _AppnLcnVcCalledDna_Type()
)
appnLcnVcCalledDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcCalledDna.setStatus("mandatory")


class _AppnLcnVcCalledLcn_Type(Unsigned32):
    """Custom type appnLcnVcCalledLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AppnLcnVcCalledLcn_Type.__name__ = "Unsigned32"
_AppnLcnVcCalledLcn_Object = MibTableColumn
appnLcnVcCalledLcn = _AppnLcnVcCalledLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 10, 1, 8),
    _AppnLcnVcCalledLcn_Type()
)
appnLcnVcCalledLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcCalledLcn.setStatus("mandatory")


class _AppnLcnVcCallingNpi_Type(Integer32):
    """Custom type appnLcnVcCallingNpi based on Integer32"""
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


_AppnLcnVcCallingNpi_Type.__name__ = "Integer32"
_AppnLcnVcCallingNpi_Object = MibTableColumn
appnLcnVcCallingNpi = _AppnLcnVcCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 10, 1, 9),
    _AppnLcnVcCallingNpi_Type()
)
appnLcnVcCallingNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcCallingNpi.setStatus("mandatory")


class _AppnLcnVcCallingDna_Type(DigitString):
    """Custom type appnLcnVcCallingDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AppnLcnVcCallingDna_Type.__name__ = "DigitString"
_AppnLcnVcCallingDna_Object = MibTableColumn
appnLcnVcCallingDna = _AppnLcnVcCallingDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 10, 1, 10),
    _AppnLcnVcCallingDna_Type()
)
appnLcnVcCallingDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcCallingDna.setStatus("mandatory")


class _AppnLcnVcCallingLcn_Type(Unsigned32):
    """Custom type appnLcnVcCallingLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AppnLcnVcCallingLcn_Type.__name__ = "Unsigned32"
_AppnLcnVcCallingLcn_Object = MibTableColumn
appnLcnVcCallingLcn = _AppnLcnVcCallingLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 10, 1, 11),
    _AppnLcnVcCallingLcn_Type()
)
appnLcnVcCallingLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcCallingLcn.setStatus("mandatory")


class _AppnLcnVcAccountingEnabled_Type(Integer32):
    """Custom type appnLcnVcAccountingEnabled based on Integer32"""
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


_AppnLcnVcAccountingEnabled_Type.__name__ = "Integer32"
_AppnLcnVcAccountingEnabled_Object = MibTableColumn
appnLcnVcAccountingEnabled = _AppnLcnVcAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 10, 1, 12),
    _AppnLcnVcAccountingEnabled_Type()
)
appnLcnVcAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcAccountingEnabled.setStatus("mandatory")


class _AppnLcnVcFastSelectCall_Type(Integer32):
    """Custom type appnLcnVcFastSelectCall based on Integer32"""
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


_AppnLcnVcFastSelectCall_Type.__name__ = "Integer32"
_AppnLcnVcFastSelectCall_Object = MibTableColumn
appnLcnVcFastSelectCall = _AppnLcnVcFastSelectCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 10, 1, 13),
    _AppnLcnVcFastSelectCall_Type()
)
appnLcnVcFastSelectCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcFastSelectCall.setStatus("mandatory")


class _AppnLcnVcLocalRxPktSize_Type(Integer32):
    """Custom type appnLcnVcLocalRxPktSize based on Integer32"""
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


_AppnLcnVcLocalRxPktSize_Type.__name__ = "Integer32"
_AppnLcnVcLocalRxPktSize_Object = MibTableColumn
appnLcnVcLocalRxPktSize = _AppnLcnVcLocalRxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 10, 1, 14),
    _AppnLcnVcLocalRxPktSize_Type()
)
appnLcnVcLocalRxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcLocalRxPktSize.setStatus("mandatory")


class _AppnLcnVcLocalTxPktSize_Type(Integer32):
    """Custom type appnLcnVcLocalTxPktSize based on Integer32"""
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


_AppnLcnVcLocalTxPktSize_Type.__name__ = "Integer32"
_AppnLcnVcLocalTxPktSize_Object = MibTableColumn
appnLcnVcLocalTxPktSize = _AppnLcnVcLocalTxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 10, 1, 15),
    _AppnLcnVcLocalTxPktSize_Type()
)
appnLcnVcLocalTxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcLocalTxPktSize.setStatus("mandatory")


class _AppnLcnVcLocalTxWindowSize_Type(Unsigned32):
    """Custom type appnLcnVcLocalTxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AppnLcnVcLocalTxWindowSize_Type.__name__ = "Unsigned32"
_AppnLcnVcLocalTxWindowSize_Object = MibTableColumn
appnLcnVcLocalTxWindowSize = _AppnLcnVcLocalTxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 10, 1, 16),
    _AppnLcnVcLocalTxWindowSize_Type()
)
appnLcnVcLocalTxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcLocalTxWindowSize.setStatus("mandatory")


class _AppnLcnVcLocalRxWindowSize_Type(Unsigned32):
    """Custom type appnLcnVcLocalRxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AppnLcnVcLocalRxWindowSize_Type.__name__ = "Unsigned32"
_AppnLcnVcLocalRxWindowSize_Object = MibTableColumn
appnLcnVcLocalRxWindowSize = _AppnLcnVcLocalRxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 10, 1, 17),
    _AppnLcnVcLocalRxWindowSize_Type()
)
appnLcnVcLocalRxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcLocalRxWindowSize.setStatus("mandatory")


class _AppnLcnVcPathReliability_Type(Integer32):
    """Custom type appnLcnVcPathReliability based on Integer32"""
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


_AppnLcnVcPathReliability_Type.__name__ = "Integer32"
_AppnLcnVcPathReliability_Object = MibTableColumn
appnLcnVcPathReliability = _AppnLcnVcPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 10, 1, 19),
    _AppnLcnVcPathReliability_Type()
)
appnLcnVcPathReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcPathReliability.setStatus("mandatory")


class _AppnLcnVcAccountingEnd_Type(Integer32):
    """Custom type appnLcnVcAccountingEnd based on Integer32"""
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


_AppnLcnVcAccountingEnd_Type.__name__ = "Integer32"
_AppnLcnVcAccountingEnd_Object = MibTableColumn
appnLcnVcAccountingEnd = _AppnLcnVcAccountingEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 10, 1, 20),
    _AppnLcnVcAccountingEnd_Type()
)
appnLcnVcAccountingEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcAccountingEnd.setStatus("mandatory")


class _AppnLcnVcPriority_Type(Integer32):
    """Custom type appnLcnVcPriority based on Integer32"""
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


_AppnLcnVcPriority_Type.__name__ = "Integer32"
_AppnLcnVcPriority_Object = MibTableColumn
appnLcnVcPriority = _AppnLcnVcPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 10, 1, 21),
    _AppnLcnVcPriority_Type()
)
appnLcnVcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcPriority.setStatus("mandatory")


class _AppnLcnVcSegmentSize_Type(Unsigned32):
    """Custom type appnLcnVcSegmentSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AppnLcnVcSegmentSize_Type.__name__ = "Unsigned32"
_AppnLcnVcSegmentSize_Object = MibTableColumn
appnLcnVcSegmentSize = _AppnLcnVcSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 10, 1, 22),
    _AppnLcnVcSegmentSize_Type()
)
appnLcnVcSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcSegmentSize.setStatus("mandatory")


class _AppnLcnVcSubnetTxPktSize_Type(Integer32):
    """Custom type appnLcnVcSubnetTxPktSize based on Integer32"""
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


_AppnLcnVcSubnetTxPktSize_Type.__name__ = "Integer32"
_AppnLcnVcSubnetTxPktSize_Object = MibTableColumn
appnLcnVcSubnetTxPktSize = _AppnLcnVcSubnetTxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 10, 1, 23),
    _AppnLcnVcSubnetTxPktSize_Type()
)
appnLcnVcSubnetTxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcSubnetTxPktSize.setStatus("mandatory")


class _AppnLcnVcSubnetTxWindowSize_Type(Unsigned32):
    """Custom type appnLcnVcSubnetTxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AppnLcnVcSubnetTxWindowSize_Type.__name__ = "Unsigned32"
_AppnLcnVcSubnetTxWindowSize_Object = MibTableColumn
appnLcnVcSubnetTxWindowSize = _AppnLcnVcSubnetTxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 10, 1, 24),
    _AppnLcnVcSubnetTxWindowSize_Type()
)
appnLcnVcSubnetTxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcSubnetTxWindowSize.setStatus("mandatory")


class _AppnLcnVcSubnetRxPktSize_Type(Integer32):
    """Custom type appnLcnVcSubnetRxPktSize based on Integer32"""
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


_AppnLcnVcSubnetRxPktSize_Type.__name__ = "Integer32"
_AppnLcnVcSubnetRxPktSize_Object = MibTableColumn
appnLcnVcSubnetRxPktSize = _AppnLcnVcSubnetRxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 10, 1, 25),
    _AppnLcnVcSubnetRxPktSize_Type()
)
appnLcnVcSubnetRxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcSubnetRxPktSize.setStatus("mandatory")


class _AppnLcnVcSubnetRxWindowSize_Type(Unsigned32):
    """Custom type appnLcnVcSubnetRxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AppnLcnVcSubnetRxWindowSize_Type.__name__ = "Unsigned32"
_AppnLcnVcSubnetRxWindowSize_Object = MibTableColumn
appnLcnVcSubnetRxWindowSize = _AppnLcnVcSubnetRxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 10, 1, 26),
    _AppnLcnVcSubnetRxWindowSize_Type()
)
appnLcnVcSubnetRxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcSubnetRxWindowSize.setStatus("mandatory")


class _AppnLcnVcMaxSubnetPktSize_Type(Unsigned32):
    """Custom type appnLcnVcMaxSubnetPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AppnLcnVcMaxSubnetPktSize_Type.__name__ = "Unsigned32"
_AppnLcnVcMaxSubnetPktSize_Object = MibTableColumn
appnLcnVcMaxSubnetPktSize = _AppnLcnVcMaxSubnetPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 10, 1, 27),
    _AppnLcnVcMaxSubnetPktSize_Type()
)
appnLcnVcMaxSubnetPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcMaxSubnetPktSize.setStatus("mandatory")


class _AppnLcnVcTransferPriorityToNetwork_Type(Integer32):
    """Custom type appnLcnVcTransferPriorityToNetwork based on Integer32"""
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


_AppnLcnVcTransferPriorityToNetwork_Type.__name__ = "Integer32"
_AppnLcnVcTransferPriorityToNetwork_Object = MibTableColumn
appnLcnVcTransferPriorityToNetwork = _AppnLcnVcTransferPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 10, 1, 28),
    _AppnLcnVcTransferPriorityToNetwork_Type()
)
appnLcnVcTransferPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcTransferPriorityToNetwork.setStatus("mandatory")


class _AppnLcnVcTransferPriorityFromNetwork_Type(Integer32):
    """Custom type appnLcnVcTransferPriorityFromNetwork based on Integer32"""
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


_AppnLcnVcTransferPriorityFromNetwork_Type.__name__ = "Integer32"
_AppnLcnVcTransferPriorityFromNetwork_Object = MibTableColumn
appnLcnVcTransferPriorityFromNetwork = _AppnLcnVcTransferPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 10, 1, 29),
    _AppnLcnVcTransferPriorityFromNetwork_Type()
)
appnLcnVcTransferPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcTransferPriorityFromNetwork.setStatus("mandatory")
_AppnLcnVcIntdTable_Object = MibTable
appnLcnVcIntdTable = _AppnLcnVcIntdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 11)
)
if mibBuilder.loadTexts:
    appnLcnVcIntdTable.setStatus("mandatory")
_AppnLcnVcIntdEntry_Object = MibTableRow
appnLcnVcIntdEntry = _AppnLcnVcIntdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 11, 1)
)
appnLcnVcIntdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnLcnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnLcnVcIndex"),
)
if mibBuilder.loadTexts:
    appnLcnVcIntdEntry.setStatus("mandatory")


class _AppnLcnVcCallReferenceNumber_Type(Hex):
    """Custom type appnLcnVcCallReferenceNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_AppnLcnVcCallReferenceNumber_Type.__name__ = "Hex"
_AppnLcnVcCallReferenceNumber_Object = MibTableColumn
appnLcnVcCallReferenceNumber = _AppnLcnVcCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 11, 1, 1),
    _AppnLcnVcCallReferenceNumber_Type()
)
appnLcnVcCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcCallReferenceNumber.setStatus("mandatory")


class _AppnLcnVcElapsedTimeTillNow_Type(Unsigned32):
    """Custom type appnLcnVcElapsedTimeTillNow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_AppnLcnVcElapsedTimeTillNow_Type.__name__ = "Unsigned32"
_AppnLcnVcElapsedTimeTillNow_Object = MibTableColumn
appnLcnVcElapsedTimeTillNow = _AppnLcnVcElapsedTimeTillNow_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 11, 1, 2),
    _AppnLcnVcElapsedTimeTillNow_Type()
)
appnLcnVcElapsedTimeTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcElapsedTimeTillNow.setStatus("mandatory")


class _AppnLcnVcSegmentsRx_Type(Unsigned32):
    """Custom type appnLcnVcSegmentsRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_AppnLcnVcSegmentsRx_Type.__name__ = "Unsigned32"
_AppnLcnVcSegmentsRx_Object = MibTableColumn
appnLcnVcSegmentsRx = _AppnLcnVcSegmentsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 11, 1, 3),
    _AppnLcnVcSegmentsRx_Type()
)
appnLcnVcSegmentsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcSegmentsRx.setStatus("mandatory")


class _AppnLcnVcSegmentsSent_Type(Unsigned32):
    """Custom type appnLcnVcSegmentsSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_AppnLcnVcSegmentsSent_Type.__name__ = "Unsigned32"
_AppnLcnVcSegmentsSent_Object = MibTableColumn
appnLcnVcSegmentsSent = _AppnLcnVcSegmentsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 11, 1, 4),
    _AppnLcnVcSegmentsSent_Type()
)
appnLcnVcSegmentsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcSegmentsSent.setStatus("mandatory")


class _AppnLcnVcStartTime_Type(EnterpriseDateAndTime):
    """Custom type appnLcnVcStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_AppnLcnVcStartTime_Type.__name__ = "EnterpriseDateAndTime"
_AppnLcnVcStartTime_Object = MibTableColumn
appnLcnVcStartTime = _AppnLcnVcStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 11, 1, 5),
    _AppnLcnVcStartTime_Type()
)
appnLcnVcStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcStartTime.setStatus("mandatory")
_AppnLcnVcStatsTable_Object = MibTable
appnLcnVcStatsTable = _AppnLcnVcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 12)
)
if mibBuilder.loadTexts:
    appnLcnVcStatsTable.setStatus("mandatory")
_AppnLcnVcStatsEntry_Object = MibTableRow
appnLcnVcStatsEntry = _AppnLcnVcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 12, 1)
)
appnLcnVcStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnLcnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnLcnVcIndex"),
)
if mibBuilder.loadTexts:
    appnLcnVcStatsEntry.setStatus("mandatory")


class _AppnLcnVcAckStackingTimeouts_Type(Unsigned32):
    """Custom type appnLcnVcAckStackingTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AppnLcnVcAckStackingTimeouts_Type.__name__ = "Unsigned32"
_AppnLcnVcAckStackingTimeouts_Object = MibTableColumn
appnLcnVcAckStackingTimeouts = _AppnLcnVcAckStackingTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 12, 1, 1),
    _AppnLcnVcAckStackingTimeouts_Type()
)
appnLcnVcAckStackingTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcAckStackingTimeouts.setStatus("mandatory")


class _AppnLcnVcOutOfRangeFrmFromSubnet_Type(Unsigned32):
    """Custom type appnLcnVcOutOfRangeFrmFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AppnLcnVcOutOfRangeFrmFromSubnet_Type.__name__ = "Unsigned32"
_AppnLcnVcOutOfRangeFrmFromSubnet_Object = MibTableColumn
appnLcnVcOutOfRangeFrmFromSubnet = _AppnLcnVcOutOfRangeFrmFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 12, 1, 2),
    _AppnLcnVcOutOfRangeFrmFromSubnet_Type()
)
appnLcnVcOutOfRangeFrmFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcOutOfRangeFrmFromSubnet.setStatus("mandatory")


class _AppnLcnVcDuplicatesFromSubnet_Type(Unsigned32):
    """Custom type appnLcnVcDuplicatesFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AppnLcnVcDuplicatesFromSubnet_Type.__name__ = "Unsigned32"
_AppnLcnVcDuplicatesFromSubnet_Object = MibTableColumn
appnLcnVcDuplicatesFromSubnet = _AppnLcnVcDuplicatesFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 12, 1, 3),
    _AppnLcnVcDuplicatesFromSubnet_Type()
)
appnLcnVcDuplicatesFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcDuplicatesFromSubnet.setStatus("mandatory")


class _AppnLcnVcFrmRetryTimeouts_Type(Unsigned32):
    """Custom type appnLcnVcFrmRetryTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AppnLcnVcFrmRetryTimeouts_Type.__name__ = "Unsigned32"
_AppnLcnVcFrmRetryTimeouts_Object = MibTableColumn
appnLcnVcFrmRetryTimeouts = _AppnLcnVcFrmRetryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 12, 1, 4),
    _AppnLcnVcFrmRetryTimeouts_Type()
)
appnLcnVcFrmRetryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcFrmRetryTimeouts.setStatus("mandatory")


class _AppnLcnVcPeakRetryQueueSize_Type(Unsigned32):
    """Custom type appnLcnVcPeakRetryQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AppnLcnVcPeakRetryQueueSize_Type.__name__ = "Unsigned32"
_AppnLcnVcPeakRetryQueueSize_Object = MibTableColumn
appnLcnVcPeakRetryQueueSize = _AppnLcnVcPeakRetryQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 12, 1, 5),
    _AppnLcnVcPeakRetryQueueSize_Type()
)
appnLcnVcPeakRetryQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcPeakRetryQueueSize.setStatus("mandatory")


class _AppnLcnVcPeakOoSeqQueueSize_Type(Unsigned32):
    """Custom type appnLcnVcPeakOoSeqQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AppnLcnVcPeakOoSeqQueueSize_Type.__name__ = "Unsigned32"
_AppnLcnVcPeakOoSeqQueueSize_Object = MibTableColumn
appnLcnVcPeakOoSeqQueueSize = _AppnLcnVcPeakOoSeqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 12, 1, 6),
    _AppnLcnVcPeakOoSeqQueueSize_Type()
)
appnLcnVcPeakOoSeqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcPeakOoSeqQueueSize.setStatus("mandatory")


class _AppnLcnVcPeakOoSeqFrmForwarded_Type(Unsigned32):
    """Custom type appnLcnVcPeakOoSeqFrmForwarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AppnLcnVcPeakOoSeqFrmForwarded_Type.__name__ = "Unsigned32"
_AppnLcnVcPeakOoSeqFrmForwarded_Object = MibTableColumn
appnLcnVcPeakOoSeqFrmForwarded = _AppnLcnVcPeakOoSeqFrmForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 12, 1, 7),
    _AppnLcnVcPeakOoSeqFrmForwarded_Type()
)
appnLcnVcPeakOoSeqFrmForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcPeakOoSeqFrmForwarded.setStatus("mandatory")


class _AppnLcnVcPeakStackedAcksRx_Type(Unsigned32):
    """Custom type appnLcnVcPeakStackedAcksRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AppnLcnVcPeakStackedAcksRx_Type.__name__ = "Unsigned32"
_AppnLcnVcPeakStackedAcksRx_Object = MibTableColumn
appnLcnVcPeakStackedAcksRx = _AppnLcnVcPeakStackedAcksRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 12, 1, 8),
    _AppnLcnVcPeakStackedAcksRx_Type()
)
appnLcnVcPeakStackedAcksRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcPeakStackedAcksRx.setStatus("mandatory")


class _AppnLcnVcSubnetRecoveries_Type(Unsigned32):
    """Custom type appnLcnVcSubnetRecoveries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AppnLcnVcSubnetRecoveries_Type.__name__ = "Unsigned32"
_AppnLcnVcSubnetRecoveries_Object = MibTableColumn
appnLcnVcSubnetRecoveries = _AppnLcnVcSubnetRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 12, 1, 9),
    _AppnLcnVcSubnetRecoveries_Type()
)
appnLcnVcSubnetRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcSubnetRecoveries.setStatus("mandatory")


class _AppnLcnVcWindowClosuresToSubnet_Type(Unsigned32):
    """Custom type appnLcnVcWindowClosuresToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AppnLcnVcWindowClosuresToSubnet_Type.__name__ = "Unsigned32"
_AppnLcnVcWindowClosuresToSubnet_Object = MibTableColumn
appnLcnVcWindowClosuresToSubnet = _AppnLcnVcWindowClosuresToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 12, 1, 10),
    _AppnLcnVcWindowClosuresToSubnet_Type()
)
appnLcnVcWindowClosuresToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcWindowClosuresToSubnet.setStatus("mandatory")


class _AppnLcnVcWindowClosuresFromSubnet_Type(Unsigned32):
    """Custom type appnLcnVcWindowClosuresFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AppnLcnVcWindowClosuresFromSubnet_Type.__name__ = "Unsigned32"
_AppnLcnVcWindowClosuresFromSubnet_Object = MibTableColumn
appnLcnVcWindowClosuresFromSubnet = _AppnLcnVcWindowClosuresFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 12, 1, 11),
    _AppnLcnVcWindowClosuresFromSubnet_Type()
)
appnLcnVcWindowClosuresFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcWindowClosuresFromSubnet.setStatus("mandatory")


class _AppnLcnVcWrTriggers_Type(Unsigned32):
    """Custom type appnLcnVcWrTriggers based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AppnLcnVcWrTriggers_Type.__name__ = "Unsigned32"
_AppnLcnVcWrTriggers_Object = MibTableColumn
appnLcnVcWrTriggers = _AppnLcnVcWrTriggers_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 3, 12, 1, 12),
    _AppnLcnVcWrTriggers_Type()
)
appnLcnVcWrTriggers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnVcWrTriggers.setStatus("mandatory")
_AppnLcnStateTable_Object = MibTable
appnLcnStateTable = _AppnLcnStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 10)
)
if mibBuilder.loadTexts:
    appnLcnStateTable.setStatus("mandatory")
_AppnLcnStateEntry_Object = MibTableRow
appnLcnStateEntry = _AppnLcnStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 10, 1)
)
appnLcnStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnLcnIndex"),
)
if mibBuilder.loadTexts:
    appnLcnStateEntry.setStatus("mandatory")


class _AppnLcnAdminState_Type(Integer32):
    """Custom type appnLcnAdminState based on Integer32"""
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


_AppnLcnAdminState_Type.__name__ = "Integer32"
_AppnLcnAdminState_Object = MibTableColumn
appnLcnAdminState = _AppnLcnAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 10, 1, 1),
    _AppnLcnAdminState_Type()
)
appnLcnAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnAdminState.setStatus("mandatory")


class _AppnLcnOperationalState_Type(Integer32):
    """Custom type appnLcnOperationalState based on Integer32"""
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


_AppnLcnOperationalState_Type.__name__ = "Integer32"
_AppnLcnOperationalState_Object = MibTableColumn
appnLcnOperationalState = _AppnLcnOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 10, 1, 2),
    _AppnLcnOperationalState_Type()
)
appnLcnOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnOperationalState.setStatus("mandatory")


class _AppnLcnUsageState_Type(Integer32):
    """Custom type appnLcnUsageState based on Integer32"""
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


_AppnLcnUsageState_Type.__name__ = "Integer32"
_AppnLcnUsageState_Object = MibTableColumn
appnLcnUsageState = _AppnLcnUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 4, 10, 1, 3),
    _AppnLcnUsageState_Type()
)
appnLcnUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLcnUsageState.setStatus("mandatory")
_AppnPort_ObjectIdentity = ObjectIdentity
appnPort = _AppnPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5)
)
_AppnPortRowStatusTable_Object = MibTable
appnPortRowStatusTable = _AppnPortRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 1)
)
if mibBuilder.loadTexts:
    appnPortRowStatusTable.setStatus("mandatory")
_AppnPortRowStatusEntry_Object = MibTableRow
appnPortRowStatusEntry = _AppnPortRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 1, 1)
)
appnPortRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnPortIndex"),
)
if mibBuilder.loadTexts:
    appnPortRowStatusEntry.setStatus("mandatory")
_AppnPortRowStatus_Type = RowStatus
_AppnPortRowStatus_Object = MibTableColumn
appnPortRowStatus = _AppnPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 1, 1, 1),
    _AppnPortRowStatus_Type()
)
appnPortRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortRowStatus.setStatus("mandatory")
_AppnPortComponentName_Type = DisplayString
_AppnPortComponentName_Object = MibTableColumn
appnPortComponentName = _AppnPortComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 1, 1, 2),
    _AppnPortComponentName_Type()
)
appnPortComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortComponentName.setStatus("mandatory")
_AppnPortStorageType_Type = StorageType
_AppnPortStorageType_Object = MibTableColumn
appnPortStorageType = _AppnPortStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 1, 1, 4),
    _AppnPortStorageType_Type()
)
appnPortStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortStorageType.setStatus("mandatory")


class _AppnPortIndex_Type(AsciiStringIndex):
    """Custom type appnPortIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppnPortIndex_Type.__name__ = "AsciiStringIndex"
_AppnPortIndex_Object = MibTableColumn
appnPortIndex = _AppnPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 1, 1, 10),
    _AppnPortIndex_Type()
)
appnPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnPortIndex.setStatus("mandatory")
_AppnPortConfigTable_Object = MibTable
appnPortConfigTable = _AppnPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 10)
)
if mibBuilder.loadTexts:
    appnPortConfigTable.setStatus("mandatory")
_AppnPortConfigEntry_Object = MibTableRow
appnPortConfigEntry = _AppnPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 10, 1)
)
appnPortConfigEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnPortIndex"),
)
if mibBuilder.loadTexts:
    appnPortConfigEntry.setStatus("mandatory")


class _AppnPortType_Type(Integer32):
    """Custom type appnPortType based on Integer32"""
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


_AppnPortType_Type.__name__ = "Integer32"
_AppnPortType_Object = MibTableColumn
appnPortType = _AppnPortType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 10, 1, 1),
    _AppnPortType_Type()
)
appnPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortType.setStatus("mandatory")


class _AppnPortMaxRxBtuSize_Type(Unsigned32):
    """Custom type appnPortMaxRxBtuSize based on Unsigned32"""
    defaultValue = 2048

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnPortMaxRxBtuSize_Type.__name__ = "Unsigned32"
_AppnPortMaxRxBtuSize_Object = MibTableColumn
appnPortMaxRxBtuSize = _AppnPortMaxRxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 10, 1, 2),
    _AppnPortMaxRxBtuSize_Type()
)
appnPortMaxRxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortMaxRxBtuSize.setStatus("mandatory")


class _AppnPortMaxTxBtuSize_Type(Unsigned32):
    """Custom type appnPortMaxTxBtuSize based on Unsigned32"""
    defaultValue = 2048

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnPortMaxTxBtuSize_Type.__name__ = "Unsigned32"
_AppnPortMaxTxBtuSize_Object = MibTableColumn
appnPortMaxTxBtuSize = _AppnPortMaxTxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 10, 1, 3),
    _AppnPortMaxTxBtuSize_Type()
)
appnPortMaxTxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortMaxTxBtuSize.setStatus("mandatory")


class _AppnPortTotLinkActLim_Type(Unsigned32):
    """Custom type appnPortTotLinkActLim based on Unsigned32"""
    defaultValue = 99

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AppnPortTotLinkActLim_Type.__name__ = "Unsigned32"
_AppnPortTotLinkActLim_Object = MibTableColumn
appnPortTotLinkActLim = _AppnPortTotLinkActLim_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 10, 1, 4),
    _AppnPortTotLinkActLim_Type()
)
appnPortTotLinkActLim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortTotLinkActLim.setStatus("mandatory")


class _AppnPortInbLinkActLim_Type(Unsigned32):
    """Custom type appnPortInbLinkActLim based on Unsigned32"""
    defaultValue = 97

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AppnPortInbLinkActLim_Type.__name__ = "Unsigned32"
_AppnPortInbLinkActLim_Object = MibTableColumn
appnPortInbLinkActLim = _AppnPortInbLinkActLim_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 10, 1, 5),
    _AppnPortInbLinkActLim_Type()
)
appnPortInbLinkActLim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortInbLinkActLim.setStatus("mandatory")


class _AppnPortOutLinkActLim_Type(Unsigned32):
    """Custom type appnPortOutLinkActLim based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AppnPortOutLinkActLim_Type.__name__ = "Unsigned32"
_AppnPortOutLinkActLim_Object = MibTableColumn
appnPortOutLinkActLim = _AppnPortOutLinkActLim_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 10, 1, 6),
    _AppnPortOutLinkActLim_Type()
)
appnPortOutLinkActLim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortOutLinkActLim.setStatus("mandatory")


class _AppnPortLsRole_Type(Integer32):
    """Custom type appnPortLsRole based on Integer32"""
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


_AppnPortLsRole_Type.__name__ = "Integer32"
_AppnPortLsRole_Object = MibTableColumn
appnPortLsRole = _AppnPortLsRole_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 10, 1, 7),
    _AppnPortLsRole_Type()
)
appnPortLsRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortLsRole.setStatus("mandatory")


class _AppnPortActXidExchLim_Type(Unsigned32):
    """Custom type appnPortActXidExchLim based on Unsigned32"""
    defaultValue = 9

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnPortActXidExchLim_Type.__name__ = "Unsigned32"
_AppnPortActXidExchLim_Object = MibTableColumn
appnPortActXidExchLim = _AppnPortActXidExchLim_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 10, 1, 8),
    _AppnPortActXidExchLim_Type()
)
appnPortActXidExchLim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortActXidExchLim.setStatus("mandatory")


class _AppnPortNonactXidExchLim_Type(Unsigned32):
    """Custom type appnPortNonactXidExchLim based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnPortNonactXidExchLim_Type.__name__ = "Unsigned32"
_AppnPortNonactXidExchLim_Object = MibTableColumn
appnPortNonactXidExchLim = _AppnPortNonactXidExchLim_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 10, 1, 9),
    _AppnPortNonactXidExchLim_Type()
)
appnPortNonactXidExchLim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortNonactXidExchLim.setStatus("mandatory")


class _AppnPortLsXmitRxCap_Type(Integer32):
    """Custom type appnPortLsXmitRxCap based on Integer32"""
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


_AppnPortLsXmitRxCap_Type.__name__ = "Integer32"
_AppnPortLsXmitRxCap_Object = MibTableColumn
appnPortLsXmitRxCap = _AppnPortLsXmitRxCap_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 10, 1, 10),
    _AppnPortLsXmitRxCap_Type()
)
appnPortLsXmitRxCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortLsXmitRxCap.setStatus("mandatory")


class _AppnPortMaxIfrmRxWindow_Type(Unsigned32):
    """Custom type appnPortMaxIfrmRxWindow based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_AppnPortMaxIfrmRxWindow_Type.__name__ = "Unsigned32"
_AppnPortMaxIfrmRxWindow_Object = MibTableColumn
appnPortMaxIfrmRxWindow = _AppnPortMaxIfrmRxWindow_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 10, 1, 11),
    _AppnPortMaxIfrmRxWindow_Type()
)
appnPortMaxIfrmRxWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortMaxIfrmRxWindow.setStatus("mandatory")


class _AppnPortTargetPacingCount_Type(Unsigned32):
    """Custom type appnPortTargetPacingCount based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnPortTargetPacingCount_Type.__name__ = "Unsigned32"
_AppnPortTargetPacingCount_Object = MibTableColumn
appnPortTargetPacingCount = _AppnPortTargetPacingCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 10, 1, 12),
    _AppnPortTargetPacingCount_Type()
)
appnPortTargetPacingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortTargetPacingCount.setStatus("mandatory")
_AppnPortOperTable_Object = MibTable
appnPortOperTable = _AppnPortOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 11)
)
if mibBuilder.loadTexts:
    appnPortOperTable.setStatus("mandatory")
_AppnPortOperEntry_Object = MibTableRow
appnPortOperEntry = _AppnPortOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 11, 1)
)
appnPortOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnPortIndex"),
)
if mibBuilder.loadTexts:
    appnPortOperEntry.setStatus("mandatory")


class _AppnPortState_Type(Integer32):
    """Custom type appnPortState based on Integer32"""
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


_AppnPortState_Type.__name__ = "Integer32"
_AppnPortState_Object = MibTableColumn
appnPortState = _AppnPortState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 11, 1, 1),
    _AppnPortState_Type()
)
appnPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortState.setStatus("mandatory")


class _AppnPortDlcType_Type(Integer32):
    """Custom type appnPortDlcType based on Integer32"""
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


_AppnPortDlcType_Type.__name__ = "Integer32"
_AppnPortDlcType_Object = MibTableColumn
appnPortDlcType = _AppnPortDlcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 11, 1, 2),
    _AppnPortDlcType_Type()
)
appnPortDlcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortDlcType.setStatus("mandatory")


class _AppnPortSimRim_Type(Integer32):
    """Custom type appnPortSimRim based on Integer32"""
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


_AppnPortSimRim_Type.__name__ = "Integer32"
_AppnPortSimRim_Object = MibTableColumn
appnPortSimRim = _AppnPortSimRim_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 11, 1, 3),
    _AppnPortSimRim_Type()
)
appnPortSimRim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortSimRim.setStatus("mandatory")
_AppnPortDefinedLsGoodXids_Type = PassportCounter64
_AppnPortDefinedLsGoodXids_Object = MibTableColumn
appnPortDefinedLsGoodXids = _AppnPortDefinedLsGoodXids_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 11, 1, 4),
    _AppnPortDefinedLsGoodXids_Type()
)
appnPortDefinedLsGoodXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortDefinedLsGoodXids.setStatus("mandatory")
_AppnPortDefinedLsBadXids_Type = PassportCounter64
_AppnPortDefinedLsBadXids_Object = MibTableColumn
appnPortDefinedLsBadXids = _AppnPortDefinedLsBadXids_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 11, 1, 5),
    _AppnPortDefinedLsBadXids_Type()
)
appnPortDefinedLsBadXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortDefinedLsBadXids.setStatus("mandatory")
_AppnPortDynLsGoodXids_Type = PassportCounter64
_AppnPortDynLsGoodXids_Object = MibTableColumn
appnPortDynLsGoodXids = _AppnPortDynLsGoodXids_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 11, 1, 6),
    _AppnPortDynLsGoodXids_Type()
)
appnPortDynLsGoodXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortDynLsGoodXids.setStatus("mandatory")
_AppnPortDynLsBadXids_Type = PassportCounter64
_AppnPortDynLsBadXids_Object = MibTableColumn
appnPortDynLsBadXids = _AppnPortDynLsBadXids_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 11, 1, 7),
    _AppnPortDynLsBadXids_Type()
)
appnPortDynLsBadXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortDynLsBadXids.setStatus("mandatory")
_AppnPortTgCharTable_Object = MibTable
appnPortTgCharTable = _AppnPortTgCharTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 12)
)
if mibBuilder.loadTexts:
    appnPortTgCharTable.setStatus("mandatory")
_AppnPortTgCharEntry_Object = MibTableRow
appnPortTgCharEntry = _AppnPortTgCharEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 12, 1)
)
appnPortTgCharEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnPortIndex"),
)
if mibBuilder.loadTexts:
    appnPortTgCharEntry.setStatus("mandatory")


class _AppnPortEffectiveCap_Type(Integer32):
    """Custom type appnPortEffectiveCap based on Integer32"""
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


_AppnPortEffectiveCap_Type.__name__ = "Integer32"
_AppnPortEffectiveCap_Object = MibTableColumn
appnPortEffectiveCap = _AppnPortEffectiveCap_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 12, 1, 1),
    _AppnPortEffectiveCap_Type()
)
appnPortEffectiveCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortEffectiveCap.setStatus("mandatory")


class _AppnPortConnectCost_Type(Integer32):
    """Custom type appnPortConnectCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnPortConnectCost_Type.__name__ = "Integer32"
_AppnPortConnectCost_Object = MibTableColumn
appnPortConnectCost = _AppnPortConnectCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 12, 1, 2),
    _AppnPortConnectCost_Type()
)
appnPortConnectCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortConnectCost.setStatus("mandatory")


class _AppnPortByteCost_Type(Integer32):
    """Custom type appnPortByteCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnPortByteCost_Type.__name__ = "Integer32"
_AppnPortByteCost_Object = MibTableColumn
appnPortByteCost = _AppnPortByteCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 12, 1, 3),
    _AppnPortByteCost_Type()
)
appnPortByteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortByteCost.setStatus("mandatory")


class _AppnPortSecurity_Type(Integer32):
    """Custom type appnPortSecurity based on Integer32"""
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


_AppnPortSecurity_Type.__name__ = "Integer32"
_AppnPortSecurity_Object = MibTableColumn
appnPortSecurity = _AppnPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 12, 1, 4),
    _AppnPortSecurity_Type()
)
appnPortSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortSecurity.setStatus("mandatory")


class _AppnPortPropagationDelay_Type(Integer32):
    """Custom type appnPortPropagationDelay based on Integer32"""
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


_AppnPortPropagationDelay_Type.__name__ = "Integer32"
_AppnPortPropagationDelay_Object = MibTableColumn
appnPortPropagationDelay = _AppnPortPropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 12, 1, 5),
    _AppnPortPropagationDelay_Type()
)
appnPortPropagationDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortPropagationDelay.setStatus("mandatory")


class _AppnPortUserDefinedParm1_Type(Unsigned32):
    """Custom type appnPortUserDefinedParm1 based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnPortUserDefinedParm1_Type.__name__ = "Unsigned32"
_AppnPortUserDefinedParm1_Object = MibTableColumn
appnPortUserDefinedParm1 = _AppnPortUserDefinedParm1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 12, 1, 7),
    _AppnPortUserDefinedParm1_Type()
)
appnPortUserDefinedParm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortUserDefinedParm1.setStatus("mandatory")


class _AppnPortUserDefinedParm2_Type(Unsigned32):
    """Custom type appnPortUserDefinedParm2 based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnPortUserDefinedParm2_Type.__name__ = "Unsigned32"
_AppnPortUserDefinedParm2_Object = MibTableColumn
appnPortUserDefinedParm2 = _AppnPortUserDefinedParm2_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 12, 1, 8),
    _AppnPortUserDefinedParm2_Type()
)
appnPortUserDefinedParm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortUserDefinedParm2.setStatus("mandatory")


class _AppnPortUserDefinedParm3_Type(Unsigned32):
    """Custom type appnPortUserDefinedParm3 based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnPortUserDefinedParm3_Type.__name__ = "Unsigned32"
_AppnPortUserDefinedParm3_Object = MibTableColumn
appnPortUserDefinedParm3 = _AppnPortUserDefinedParm3_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 5, 12, 1, 9),
    _AppnPortUserDefinedParm3_Type()
)
appnPortUserDefinedParm3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortUserDefinedParm3.setStatus("mandatory")
_AppnLs_ObjectIdentity = ObjectIdentity
appnLs = _AppnLs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6)
)
_AppnLsRowStatusTable_Object = MibTable
appnLsRowStatusTable = _AppnLsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 1)
)
if mibBuilder.loadTexts:
    appnLsRowStatusTable.setStatus("mandatory")
_AppnLsRowStatusEntry_Object = MibTableRow
appnLsRowStatusEntry = _AppnLsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 1, 1)
)
appnLsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnLsIndex"),
)
if mibBuilder.loadTexts:
    appnLsRowStatusEntry.setStatus("mandatory")
_AppnLsRowStatus_Type = RowStatus
_AppnLsRowStatus_Object = MibTableColumn
appnLsRowStatus = _AppnLsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 1, 1, 1),
    _AppnLsRowStatus_Type()
)
appnLsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsRowStatus.setStatus("mandatory")
_AppnLsComponentName_Type = DisplayString
_AppnLsComponentName_Object = MibTableColumn
appnLsComponentName = _AppnLsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 1, 1, 2),
    _AppnLsComponentName_Type()
)
appnLsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsComponentName.setStatus("mandatory")
_AppnLsStorageType_Type = StorageType
_AppnLsStorageType_Object = MibTableColumn
appnLsStorageType = _AppnLsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 1, 1, 4),
    _AppnLsStorageType_Type()
)
appnLsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsStorageType.setStatus("mandatory")


class _AppnLsIndex_Type(AsciiStringIndex):
    """Custom type appnLsIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppnLsIndex_Type.__name__ = "AsciiStringIndex"
_AppnLsIndex_Object = MibTableColumn
appnLsIndex = _AppnLsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 1, 1, 10),
    _AppnLsIndex_Type()
)
appnLsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnLsIndex.setStatus("mandatory")
_AppnLsLsVcReferenceTable_Object = MibTable
appnLsLsVcReferenceTable = _AppnLsLsVcReferenceTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 10)
)
if mibBuilder.loadTexts:
    appnLsLsVcReferenceTable.setStatus("mandatory")
_AppnLsLsVcReferenceEntry_Object = MibTableRow
appnLsLsVcReferenceEntry = _AppnLsLsVcReferenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 10, 1)
)
appnLsLsVcReferenceEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnLsIndex"),
)
if mibBuilder.loadTexts:
    appnLsLsVcReferenceEntry.setStatus("mandatory")
_AppnLsName_Type = RowPointer
_AppnLsName_Object = MibTableColumn
appnLsName = _AppnLsName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 10, 1, 1),
    _AppnLsName_Type()
)
appnLsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsName.setStatus("mandatory")


class _AppnLsSap_Type(Hex):
    """Custom type appnLsSap based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 252),
    )


_AppnLsSap_Type.__name__ = "Hex"
_AppnLsSap_Object = MibTableColumn
appnLsSap = _AppnLsSap_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 10, 1, 2),
    _AppnLsSap_Type()
)
appnLsSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsSap.setStatus("mandatory")
_AppnLsConfigTable_Object = MibTable
appnLsConfigTable = _AppnLsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 11)
)
if mibBuilder.loadTexts:
    appnLsConfigTable.setStatus("mandatory")
_AppnLsConfigEntry_Object = MibTableRow
appnLsConfigEntry = _AppnLsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 11, 1)
)
appnLsConfigEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnLsIndex"),
)
if mibBuilder.loadTexts:
    appnLsConfigEntry.setStatus("mandatory")


class _AppnLsPortName_Type(AsciiString):
    """Custom type appnLsPortName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppnLsPortName_Type.__name__ = "AsciiString"
_AppnLsPortName_Object = MibTableColumn
appnLsPortName = _AppnLsPortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 11, 1, 1),
    _AppnLsPortName_Type()
)
appnLsPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsPortName.setStatus("mandatory")


class _AppnLsFeatures_Type(OctetString):
    """Custom type appnLsFeatures based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AppnLsFeatures_Type.__name__ = "OctetString"
_AppnLsFeatures_Object = MibTableColumn
appnLsFeatures = _AppnLsFeatures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 11, 1, 4),
    _AppnLsFeatures_Type()
)
appnLsFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsFeatures.setStatus("mandatory")


class _AppnLsMaxTxBtuSize_Type(Unsigned32):
    """Custom type appnLsMaxTxBtuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AppnLsMaxTxBtuSize_Type.__name__ = "Unsigned32"
_AppnLsMaxTxBtuSize_Object = MibTableColumn
appnLsMaxTxBtuSize = _AppnLsMaxTxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 11, 1, 6),
    _AppnLsMaxTxBtuSize_Type()
)
appnLsMaxTxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsMaxTxBtuSize.setStatus("mandatory")
_AppnLsOperTable_Object = MibTable
appnLsOperTable = _AppnLsOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 12)
)
if mibBuilder.loadTexts:
    appnLsOperTable.setStatus("mandatory")
_AppnLsOperEntry_Object = MibTableRow
appnLsOperEntry = _AppnLsOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 12, 1)
)
appnLsOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnLsIndex"),
)
if mibBuilder.loadTexts:
    appnLsOperEntry.setStatus("mandatory")


class _AppnLsDlcType_Type(Integer32):
    """Custom type appnLsDlcType based on Integer32"""
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


_AppnLsDlcType_Type.__name__ = "Integer32"
_AppnLsDlcType_Object = MibTableColumn
appnLsDlcType = _AppnLsDlcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 12, 1, 1),
    _AppnLsDlcType_Type()
)
appnLsDlcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsDlcType.setStatus("mandatory")


class _AppnLsLinkStationState_Type(Integer32):
    """Custom type appnLsLinkStationState based on Integer32"""
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


_AppnLsLinkStationState_Type.__name__ = "Integer32"
_AppnLsLinkStationState_Object = MibTableColumn
appnLsLinkStationState = _AppnLsLinkStationState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 12, 1, 2),
    _AppnLsLinkStationState_Type()
)
appnLsLinkStationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsLinkStationState.setStatus("mandatory")


class _AppnLsLinkStationSubState_Type(Integer32):
    """Custom type appnLsLinkStationSubState based on Integer32"""
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


_AppnLsLinkStationSubState_Type.__name__ = "Integer32"
_AppnLsLinkStationSubState_Object = MibTableColumn
appnLsLinkStationSubState = _AppnLsLinkStationSubState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 12, 1, 3),
    _AppnLsLinkStationSubState_Type()
)
appnLsLinkStationSubState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsLinkStationSubState.setStatus("mandatory")


class _AppnLsActSessCount_Type(Gauge32):
    """Custom type appnLsActSessCount based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnLsActSessCount_Type.__name__ = "Gauge32"
_AppnLsActSessCount_Object = MibTableColumn
appnLsActSessCount = _AppnLsActSessCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 12, 1, 4),
    _AppnLsActSessCount_Type()
)
appnLsActSessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsActSessCount.setStatus("mandatory")


class _AppnLsActualCpName_Type(AsciiString):
    """Custom type appnLsActualCpName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_AppnLsActualCpName_Type.__name__ = "AsciiString"
_AppnLsActualCpName_Object = MibTableColumn
appnLsActualCpName = _AppnLsActualCpName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 12, 1, 5),
    _AppnLsActualCpName_Type()
)
appnLsActualCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsActualCpName.setStatus("mandatory")


class _AppnLsActualCpType_Type(Integer32):
    """Custom type appnLsActualCpType based on Integer32"""
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


_AppnLsActualCpType_Type.__name__ = "Integer32"
_AppnLsActualCpType_Object = MibTableColumn
appnLsActualCpType = _AppnLsActualCpType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 12, 1, 6),
    _AppnLsActualCpType_Type()
)
appnLsActualCpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsActualCpType.setStatus("mandatory")


class _AppnLsDlcName_Type(AsciiString):
    """Custom type appnLsDlcName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppnLsDlcName_Type.__name__ = "AsciiString"
_AppnLsDlcName_Object = MibTableColumn
appnLsDlcName = _AppnLsDlcName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 12, 1, 7),
    _AppnLsDlcName_Type()
)
appnLsDlcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsDlcName.setStatus("mandatory")


class _AppnLsDynamicOrDefined_Type(Integer32):
    """Custom type appnLsDynamicOrDefined based on Integer32"""
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


_AppnLsDynamicOrDefined_Type.__name__ = "Integer32"
_AppnLsDynamicOrDefined_Object = MibTableColumn
appnLsDynamicOrDefined = _AppnLsDynamicOrDefined_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 12, 1, 8),
    _AppnLsDynamicOrDefined_Type()
)
appnLsDynamicOrDefined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsDynamicOrDefined.setStatus("mandatory")


class _AppnLsMigration_Type(Integer32):
    """Custom type appnLsMigration based on Integer32"""
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


_AppnLsMigration_Type.__name__ = "Integer32"
_AppnLsMigration_Object = MibTableColumn
appnLsMigration = _AppnLsMigration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 12, 1, 9),
    _AppnLsMigration_Type()
)
appnLsMigration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsMigration.setStatus("mandatory")


class _AppnLsTgNum_Type(Unsigned32):
    """Custom type appnLsTgNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnLsTgNum_Type.__name__ = "Unsigned32"
_AppnLsTgNum_Object = MibTableColumn
appnLsTgNum = _AppnLsTgNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 12, 1, 10),
    _AppnLsTgNum_Type()
)
appnLsTgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsTgNum.setStatus("mandatory")


class _AppnLsHprSupport_Type(Integer32):
    """Custom type appnLsHprSupport based on Integer32"""
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


_AppnLsHprSupport_Type.__name__ = "Integer32"
_AppnLsHprSupport_Object = MibTableColumn
appnLsHprSupport = _AppnLsHprSupport_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 12, 1, 11),
    _AppnLsHprSupport_Type()
)
appnLsHprSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsHprSupport.setStatus("mandatory")


class _AppnLsAnrLabel_Type(Hex):
    """Custom type appnLsAnrLabel based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnLsAnrLabel_Type.__name__ = "Hex"
_AppnLsAnrLabel_Object = MibTableColumn
appnLsAnrLabel = _AppnLsAnrLabel_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 12, 1, 12),
    _AppnLsAnrLabel_Type()
)
appnLsAnrLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsAnrLabel.setStatus("mandatory")
_AppnLsTgCharTable_Object = MibTable
appnLsTgCharTable = _AppnLsTgCharTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 13)
)
if mibBuilder.loadTexts:
    appnLsTgCharTable.setStatus("mandatory")
_AppnLsTgCharEntry_Object = MibTableRow
appnLsTgCharEntry = _AppnLsTgCharEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 13, 1)
)
appnLsTgCharEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnLsIndex"),
)
if mibBuilder.loadTexts:
    appnLsTgCharEntry.setStatus("mandatory")


class _AppnLsEffectiveCap_Type(Integer32):
    """Custom type appnLsEffectiveCap based on Integer32"""
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


_AppnLsEffectiveCap_Type.__name__ = "Integer32"
_AppnLsEffectiveCap_Object = MibTableColumn
appnLsEffectiveCap = _AppnLsEffectiveCap_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 13, 1, 1),
    _AppnLsEffectiveCap_Type()
)
appnLsEffectiveCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsEffectiveCap.setStatus("mandatory")


class _AppnLsConnectCost_Type(Integer32):
    """Custom type appnLsConnectCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnLsConnectCost_Type.__name__ = "Integer32"
_AppnLsConnectCost_Object = MibTableColumn
appnLsConnectCost = _AppnLsConnectCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 13, 1, 2),
    _AppnLsConnectCost_Type()
)
appnLsConnectCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsConnectCost.setStatus("mandatory")


class _AppnLsByteCost_Type(Integer32):
    """Custom type appnLsByteCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnLsByteCost_Type.__name__ = "Integer32"
_AppnLsByteCost_Object = MibTableColumn
appnLsByteCost = _AppnLsByteCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 13, 1, 3),
    _AppnLsByteCost_Type()
)
appnLsByteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsByteCost.setStatus("mandatory")


class _AppnLsSecurity_Type(Integer32):
    """Custom type appnLsSecurity based on Integer32"""
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


_AppnLsSecurity_Type.__name__ = "Integer32"
_AppnLsSecurity_Object = MibTableColumn
appnLsSecurity = _AppnLsSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 13, 1, 4),
    _AppnLsSecurity_Type()
)
appnLsSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsSecurity.setStatus("mandatory")


class _AppnLsPropagationDelay_Type(Integer32):
    """Custom type appnLsPropagationDelay based on Integer32"""
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


_AppnLsPropagationDelay_Type.__name__ = "Integer32"
_AppnLsPropagationDelay_Object = MibTableColumn
appnLsPropagationDelay = _AppnLsPropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 13, 1, 5),
    _AppnLsPropagationDelay_Type()
)
appnLsPropagationDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsPropagationDelay.setStatus("mandatory")


class _AppnLsUserDefinedParm1_Type(Unsigned32):
    """Custom type appnLsUserDefinedParm1 based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnLsUserDefinedParm1_Type.__name__ = "Unsigned32"
_AppnLsUserDefinedParm1_Object = MibTableColumn
appnLsUserDefinedParm1 = _AppnLsUserDefinedParm1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 13, 1, 7),
    _AppnLsUserDefinedParm1_Type()
)
appnLsUserDefinedParm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsUserDefinedParm1.setStatus("mandatory")


class _AppnLsUserDefinedParm2_Type(Unsigned32):
    """Custom type appnLsUserDefinedParm2 based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnLsUserDefinedParm2_Type.__name__ = "Unsigned32"
_AppnLsUserDefinedParm2_Object = MibTableColumn
appnLsUserDefinedParm2 = _AppnLsUserDefinedParm2_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 13, 1, 8),
    _AppnLsUserDefinedParm2_Type()
)
appnLsUserDefinedParm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsUserDefinedParm2.setStatus("mandatory")


class _AppnLsUserDefinedParm3_Type(Unsigned32):
    """Custom type appnLsUserDefinedParm3 based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnLsUserDefinedParm3_Type.__name__ = "Unsigned32"
_AppnLsUserDefinedParm3_Object = MibTableColumn
appnLsUserDefinedParm3 = _AppnLsUserDefinedParm3_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 13, 1, 9),
    _AppnLsUserDefinedParm3_Type()
)
appnLsUserDefinedParm3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsUserDefinedParm3.setStatus("mandatory")
_AppnLsStatsTable_Object = MibTable
appnLsStatsTable = _AppnLsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 14)
)
if mibBuilder.loadTexts:
    appnLsStatsTable.setStatus("mandatory")
_AppnLsStatsEntry_Object = MibTableRow
appnLsStatsEntry = _AppnLsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 14, 1)
)
appnLsStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnLsIndex"),
)
if mibBuilder.loadTexts:
    appnLsStatsEntry.setStatus("mandatory")
_AppnLsInXidBytes_Type = PassportCounter64
_AppnLsInXidBytes_Object = MibTableColumn
appnLsInXidBytes = _AppnLsInXidBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 14, 1, 1),
    _AppnLsInXidBytes_Type()
)
appnLsInXidBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsInXidBytes.setStatus("mandatory")
_AppnLsInMsgBytes_Type = PassportCounter64
_AppnLsInMsgBytes_Object = MibTableColumn
appnLsInMsgBytes = _AppnLsInMsgBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 14, 1, 2),
    _AppnLsInMsgBytes_Type()
)
appnLsInMsgBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsInMsgBytes.setStatus("mandatory")
_AppnLsInXidFrames_Type = PassportCounter64
_AppnLsInXidFrames_Object = MibTableColumn
appnLsInXidFrames = _AppnLsInXidFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 14, 1, 3),
    _AppnLsInXidFrames_Type()
)
appnLsInXidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsInXidFrames.setStatus("mandatory")
_AppnLsInMsgFrames_Type = PassportCounter64
_AppnLsInMsgFrames_Object = MibTableColumn
appnLsInMsgFrames = _AppnLsInMsgFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 14, 1, 4),
    _AppnLsInMsgFrames_Type()
)
appnLsInMsgFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsInMsgFrames.setStatus("mandatory")
_AppnLsOutXidBytes_Type = PassportCounter64
_AppnLsOutXidBytes_Object = MibTableColumn
appnLsOutXidBytes = _AppnLsOutXidBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 14, 1, 5),
    _AppnLsOutXidBytes_Type()
)
appnLsOutXidBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsOutXidBytes.setStatus("mandatory")
_AppnLsOutMsgBytes_Type = PassportCounter64
_AppnLsOutMsgBytes_Object = MibTableColumn
appnLsOutMsgBytes = _AppnLsOutMsgBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 14, 1, 6),
    _AppnLsOutMsgBytes_Type()
)
appnLsOutMsgBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsOutMsgBytes.setStatus("mandatory")
_AppnLsOutXidFrames_Type = PassportCounter64
_AppnLsOutXidFrames_Object = MibTableColumn
appnLsOutXidFrames = _AppnLsOutXidFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 14, 1, 7),
    _AppnLsOutXidFrames_Type()
)
appnLsOutXidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsOutXidFrames.setStatus("mandatory")
_AppnLsOutMsgFrames_Type = PassportCounter64
_AppnLsOutMsgFrames_Object = MibTableColumn
appnLsOutMsgFrames = _AppnLsOutMsgFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 14, 1, 8),
    _AppnLsOutMsgFrames_Type()
)
appnLsOutMsgFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsOutMsgFrames.setStatus("mandatory")
_AppnLsInInvalidSnaFrames_Type = PassportCounter64
_AppnLsInInvalidSnaFrames_Object = MibTableColumn
appnLsInInvalidSnaFrames = _AppnLsInInvalidSnaFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 14, 1, 9),
    _AppnLsInInvalidSnaFrames_Type()
)
appnLsInInvalidSnaFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsInInvalidSnaFrames.setStatus("mandatory")
_AppnLsInSessionControlFrames_Type = PassportCounter64
_AppnLsInSessionControlFrames_Object = MibTableColumn
appnLsInSessionControlFrames = _AppnLsInSessionControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 14, 1, 10),
    _AppnLsInSessionControlFrames_Type()
)
appnLsInSessionControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsInSessionControlFrames.setStatus("mandatory")
_AppnLsOutSessionControlFrames_Type = PassportCounter64
_AppnLsOutSessionControlFrames_Object = MibTableColumn
appnLsOutSessionControlFrames = _AppnLsOutSessionControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 14, 1, 11),
    _AppnLsOutSessionControlFrames_Type()
)
appnLsOutSessionControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsOutSessionControlFrames.setStatus("mandatory")
_AppnLsEchoResponse_Type = PassportCounter64
_AppnLsEchoResponse_Object = MibTableColumn
appnLsEchoResponse = _AppnLsEchoResponse_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 14, 1, 12),
    _AppnLsEchoResponse_Type()
)
appnLsEchoResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsEchoResponse.setStatus("mandatory")
_AppnLsCurrentDelay_Type = PassportCounter64
_AppnLsCurrentDelay_Object = MibTableColumn
appnLsCurrentDelay = _AppnLsCurrentDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 14, 1, 13),
    _AppnLsCurrentDelay_Type()
)
appnLsCurrentDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsCurrentDelay.setStatus("mandatory")
_AppnLsMaxDelay_Type = PassportCounter64
_AppnLsMaxDelay_Object = MibTableColumn
appnLsMaxDelay = _AppnLsMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 14, 1, 14),
    _AppnLsMaxDelay_Type()
)
appnLsMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsMaxDelay.setStatus("mandatory")
_AppnLsMinDelay_Type = PassportCounter64
_AppnLsMinDelay_Object = MibTableColumn
appnLsMinDelay = _AppnLsMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 14, 1, 15),
    _AppnLsMinDelay_Type()
)
appnLsMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsMinDelay.setStatus("mandatory")
_AppnLsGoodXids_Type = PassportCounter64
_AppnLsGoodXids_Object = MibTableColumn
appnLsGoodXids = _AppnLsGoodXids_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 14, 1, 17),
    _AppnLsGoodXids_Type()
)
appnLsGoodXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsGoodXids.setStatus("mandatory")
_AppnLsBadXids_Type = PassportCounter64
_AppnLsBadXids_Object = MibTableColumn
appnLsBadXids = _AppnLsBadXids_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 6, 14, 1, 18),
    _AppnLsBadXids_Type()
)
appnLsBadXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsBadXids.setStatus("mandatory")
_AppnDirEnt_ObjectIdentity = ObjectIdentity
appnDirEnt = _AppnDirEnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 7)
)
_AppnDirEntRowStatusTable_Object = MibTable
appnDirEntRowStatusTable = _AppnDirEntRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 7, 1)
)
if mibBuilder.loadTexts:
    appnDirEntRowStatusTable.setStatus("mandatory")
_AppnDirEntRowStatusEntry_Object = MibTableRow
appnDirEntRowStatusEntry = _AppnDirEntRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 7, 1, 1)
)
appnDirEntRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDirEntIndex"),
)
if mibBuilder.loadTexts:
    appnDirEntRowStatusEntry.setStatus("mandatory")
_AppnDirEntRowStatus_Type = RowStatus
_AppnDirEntRowStatus_Object = MibTableColumn
appnDirEntRowStatus = _AppnDirEntRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 7, 1, 1, 1),
    _AppnDirEntRowStatus_Type()
)
appnDirEntRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDirEntRowStatus.setStatus("mandatory")
_AppnDirEntComponentName_Type = DisplayString
_AppnDirEntComponentName_Object = MibTableColumn
appnDirEntComponentName = _AppnDirEntComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 7, 1, 1, 2),
    _AppnDirEntComponentName_Type()
)
appnDirEntComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDirEntComponentName.setStatus("mandatory")
_AppnDirEntStorageType_Type = StorageType
_AppnDirEntStorageType_Object = MibTableColumn
appnDirEntStorageType = _AppnDirEntStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 7, 1, 1, 4),
    _AppnDirEntStorageType_Type()
)
appnDirEntStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDirEntStorageType.setStatus("mandatory")


class _AppnDirEntIndex_Type(AsciiStringIndex):
    """Custom type appnDirEntIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppnDirEntIndex_Type.__name__ = "AsciiStringIndex"
_AppnDirEntIndex_Object = MibTableColumn
appnDirEntIndex = _AppnDirEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 7, 1, 1, 10),
    _AppnDirEntIndex_Type()
)
appnDirEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnDirEntIndex.setStatus("mandatory")
_AppnDirEntOperTable_Object = MibTable
appnDirEntOperTable = _AppnDirEntOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 7, 10)
)
if mibBuilder.loadTexts:
    appnDirEntOperTable.setStatus("mandatory")
_AppnDirEntOperEntry_Object = MibTableRow
appnDirEntOperEntry = _AppnDirEntOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 7, 10, 1)
)
appnDirEntOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDirEntIndex"),
)
if mibBuilder.loadTexts:
    appnDirEntOperEntry.setStatus("mandatory")


class _AppnDirEntServerName_Type(AsciiString):
    """Custom type appnDirEntServerName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_AppnDirEntServerName_Type.__name__ = "AsciiString"
_AppnDirEntServerName_Object = MibTableColumn
appnDirEntServerName = _AppnDirEntServerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 7, 10, 1, 1),
    _AppnDirEntServerName_Type()
)
appnDirEntServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDirEntServerName.setStatus("mandatory")


class _AppnDirEntLuOwnerName_Type(AsciiString):
    """Custom type appnDirEntLuOwnerName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_AppnDirEntLuOwnerName_Type.__name__ = "AsciiString"
_AppnDirEntLuOwnerName_Object = MibTableColumn
appnDirEntLuOwnerName = _AppnDirEntLuOwnerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 7, 10, 1, 2),
    _AppnDirEntLuOwnerName_Type()
)
appnDirEntLuOwnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDirEntLuOwnerName.setStatus("mandatory")


class _AppnDirEntLocation_Type(Integer32):
    """Custom type appnDirEntLocation based on Integer32"""
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


_AppnDirEntLocation_Type.__name__ = "Integer32"
_AppnDirEntLocation_Object = MibTableColumn
appnDirEntLocation = _AppnDirEntLocation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 7, 10, 1, 3),
    _AppnDirEntLocation_Type()
)
appnDirEntLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDirEntLocation.setStatus("mandatory")


class _AppnDirEntEntryType_Type(Integer32):
    """Custom type appnDirEntEntryType based on Integer32"""
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


_AppnDirEntEntryType_Type.__name__ = "Integer32"
_AppnDirEntEntryType_Object = MibTableColumn
appnDirEntEntryType = _AppnDirEntEntryType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 7, 10, 1, 4),
    _AppnDirEntEntryType_Type()
)
appnDirEntEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDirEntEntryType.setStatus("mandatory")


class _AppnDirEntWildCard_Type(Integer32):
    """Custom type appnDirEntWildCard based on Integer32"""
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


_AppnDirEntWildCard_Type.__name__ = "Integer32"
_AppnDirEntWildCard_Object = MibTableColumn
appnDirEntWildCard = _AppnDirEntWildCard_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 7, 10, 1, 5),
    _AppnDirEntWildCard_Type()
)
appnDirEntWildCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDirEntWildCard.setStatus("mandatory")
_AppnAdjNn_ObjectIdentity = ObjectIdentity
appnAdjNn = _AppnAdjNn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 8)
)
_AppnAdjNnRowStatusTable_Object = MibTable
appnAdjNnRowStatusTable = _AppnAdjNnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 8, 1)
)
if mibBuilder.loadTexts:
    appnAdjNnRowStatusTable.setStatus("mandatory")
_AppnAdjNnRowStatusEntry_Object = MibTableRow
appnAdjNnRowStatusEntry = _AppnAdjNnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 8, 1, 1)
)
appnAdjNnRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnAdjNnIndex"),
)
if mibBuilder.loadTexts:
    appnAdjNnRowStatusEntry.setStatus("mandatory")
_AppnAdjNnRowStatus_Type = RowStatus
_AppnAdjNnRowStatus_Object = MibTableColumn
appnAdjNnRowStatus = _AppnAdjNnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 8, 1, 1, 1),
    _AppnAdjNnRowStatus_Type()
)
appnAdjNnRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnAdjNnRowStatus.setStatus("mandatory")
_AppnAdjNnComponentName_Type = DisplayString
_AppnAdjNnComponentName_Object = MibTableColumn
appnAdjNnComponentName = _AppnAdjNnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 8, 1, 1, 2),
    _AppnAdjNnComponentName_Type()
)
appnAdjNnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnAdjNnComponentName.setStatus("mandatory")
_AppnAdjNnStorageType_Type = StorageType
_AppnAdjNnStorageType_Object = MibTableColumn
appnAdjNnStorageType = _AppnAdjNnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 8, 1, 1, 4),
    _AppnAdjNnStorageType_Type()
)
appnAdjNnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnAdjNnStorageType.setStatus("mandatory")


class _AppnAdjNnIndex_Type(AsciiStringIndex):
    """Custom type appnAdjNnIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppnAdjNnIndex_Type.__name__ = "AsciiStringIndex"
_AppnAdjNnIndex_Object = MibTableColumn
appnAdjNnIndex = _AppnAdjNnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 8, 1, 1, 10),
    _AppnAdjNnIndex_Type()
)
appnAdjNnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnAdjNnIndex.setStatus("mandatory")
_AppnAdjNnOperTable_Object = MibTable
appnAdjNnOperTable = _AppnAdjNnOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 8, 10)
)
if mibBuilder.loadTexts:
    appnAdjNnOperTable.setStatus("mandatory")
_AppnAdjNnOperEntry_Object = MibTableRow
appnAdjNnOperEntry = _AppnAdjNnOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 8, 10, 1)
)
appnAdjNnOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnAdjNnIndex"),
)
if mibBuilder.loadTexts:
    appnAdjNnOperEntry.setStatus("mandatory")


class _AppnAdjNnCpCpSessStatus_Type(Integer32):
    """Custom type appnAdjNnCpCpSessStatus based on Integer32"""
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


_AppnAdjNnCpCpSessStatus_Type.__name__ = "Integer32"
_AppnAdjNnCpCpSessStatus_Object = MibTableColumn
appnAdjNnCpCpSessStatus = _AppnAdjNnCpCpSessStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 8, 10, 1, 1),
    _AppnAdjNnCpCpSessStatus_Type()
)
appnAdjNnCpCpSessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnAdjNnCpCpSessStatus.setStatus("mandatory")
_AppnAdjNnOutOfSeqTdus_Type = PassportCounter64
_AppnAdjNnOutOfSeqTdus_Object = MibTableColumn
appnAdjNnOutOfSeqTdus = _AppnAdjNnOutOfSeqTdus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 8, 10, 1, 2),
    _AppnAdjNnOutOfSeqTdus_Type()
)
appnAdjNnOutOfSeqTdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnAdjNnOutOfSeqTdus.setStatus("mandatory")


class _AppnAdjNnLastFrsnSent_Type(Unsigned32):
    """Custom type appnAdjNnLastFrsnSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AppnAdjNnLastFrsnSent_Type.__name__ = "Unsigned32"
_AppnAdjNnLastFrsnSent_Object = MibTableColumn
appnAdjNnLastFrsnSent = _AppnAdjNnLastFrsnSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 8, 10, 1, 3),
    _AppnAdjNnLastFrsnSent_Type()
)
appnAdjNnLastFrsnSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnAdjNnLastFrsnSent.setStatus("mandatory")


class _AppnAdjNnLastFrsnReceived_Type(Unsigned32):
    """Custom type appnAdjNnLastFrsnReceived based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AppnAdjNnLastFrsnReceived_Type.__name__ = "Unsigned32"
_AppnAdjNnLastFrsnReceived_Object = MibTableColumn
appnAdjNnLastFrsnReceived = _AppnAdjNnLastFrsnReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 8, 10, 1, 4),
    _AppnAdjNnLastFrsnReceived_Type()
)
appnAdjNnLastFrsnReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnAdjNnLastFrsnReceived.setStatus("mandatory")
_AppnNn_ObjectIdentity = ObjectIdentity
appnNn = _AppnNn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 9)
)
_AppnNnRowStatusTable_Object = MibTable
appnNnRowStatusTable = _AppnNnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 9, 1)
)
if mibBuilder.loadTexts:
    appnNnRowStatusTable.setStatus("mandatory")
_AppnNnRowStatusEntry_Object = MibTableRow
appnNnRowStatusEntry = _AppnNnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 9, 1, 1)
)
appnNnRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnNnIndex"),
)
if mibBuilder.loadTexts:
    appnNnRowStatusEntry.setStatus("mandatory")
_AppnNnRowStatus_Type = RowStatus
_AppnNnRowStatus_Object = MibTableColumn
appnNnRowStatus = _AppnNnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 9, 1, 1, 1),
    _AppnNnRowStatus_Type()
)
appnNnRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnRowStatus.setStatus("mandatory")
_AppnNnComponentName_Type = DisplayString
_AppnNnComponentName_Object = MibTableColumn
appnNnComponentName = _AppnNnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 9, 1, 1, 2),
    _AppnNnComponentName_Type()
)
appnNnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnComponentName.setStatus("mandatory")
_AppnNnStorageType_Type = StorageType
_AppnNnStorageType_Object = MibTableColumn
appnNnStorageType = _AppnNnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 9, 1, 1, 4),
    _AppnNnStorageType_Type()
)
appnNnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnStorageType.setStatus("mandatory")


class _AppnNnIndex_Type(AsciiStringIndex):
    """Custom type appnNnIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppnNnIndex_Type.__name__ = "AsciiStringIndex"
_AppnNnIndex_Object = MibTableColumn
appnNnIndex = _AppnNnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 9, 1, 1, 10),
    _AppnNnIndex_Type()
)
appnNnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnNnIndex.setStatus("mandatory")
_AppnNnOperTable_Object = MibTable
appnNnOperTable = _AppnNnOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 9, 10)
)
if mibBuilder.loadTexts:
    appnNnOperTable.setStatus("mandatory")
_AppnNnOperEntry_Object = MibTableRow
appnNnOperEntry = _AppnNnOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 9, 10, 1)
)
appnNnOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnNnIndex"),
)
if mibBuilder.loadTexts:
    appnNnOperEntry.setStatus("mandatory")


class _AppnNnDaysLeft_Type(Unsigned32):
    """Custom type appnNnDaysLeft based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_AppnNnDaysLeft_Type.__name__ = "Unsigned32"
_AppnNnDaysLeft_Object = MibTableColumn
appnNnDaysLeft = _AppnNnDaysLeft_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 9, 10, 1, 2),
    _AppnNnDaysLeft_Type()
)
appnNnDaysLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnDaysLeft.setStatus("mandatory")


class _AppnNnNodeType_Type(Integer32):
    """Custom type appnNnNodeType based on Integer32"""
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


_AppnNnNodeType_Type.__name__ = "Integer32"
_AppnNnNodeType_Object = MibTableColumn
appnNnNodeType = _AppnNnNodeType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 9, 10, 1, 3),
    _AppnNnNodeType_Type()
)
appnNnNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnNodeType.setStatus("mandatory")


class _AppnNnResourceSequenceNumber_Type(Unsigned32):
    """Custom type appnNnResourceSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AppnNnResourceSequenceNumber_Type.__name__ = "Unsigned32"
_AppnNnResourceSequenceNumber_Object = MibTableColumn
appnNnResourceSequenceNumber = _AppnNnResourceSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 9, 10, 1, 4),
    _AppnNnResourceSequenceNumber_Type()
)
appnNnResourceSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnResourceSequenceNumber.setStatus("mandatory")


class _AppnNnRouteAdditionResistance_Type(Integer32):
    """Custom type appnNnRouteAdditionResistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnNnRouteAdditionResistance_Type.__name__ = "Integer32"
_AppnNnRouteAdditionResistance_Object = MibTableColumn
appnNnRouteAdditionResistance = _AppnNnRouteAdditionResistance_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 9, 10, 1, 5),
    _AppnNnRouteAdditionResistance_Type()
)
appnNnRouteAdditionResistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnRouteAdditionResistance.setStatus("mandatory")


class _AppnNnStatus_Type(OctetString):
    """Custom type appnNnStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AppnNnStatus_Type.__name__ = "OctetString"
_AppnNnStatus_Object = MibTableColumn
appnNnStatus = _AppnNnStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 9, 10, 1, 6),
    _AppnNnStatus_Type()
)
appnNnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnStatus.setStatus("mandatory")


class _AppnNnFunctionSupported_Type(OctetString):
    """Custom type appnNnFunctionSupported based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AppnNnFunctionSupported_Type.__name__ = "OctetString"
_AppnNnFunctionSupported_Object = MibTableColumn
appnNnFunctionSupported = _AppnNnFunctionSupported_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 9, 10, 1, 7),
    _AppnNnFunctionSupported_Type()
)
appnNnFunctionSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnFunctionSupported.setStatus("mandatory")
_AppnLocTg_ObjectIdentity = ObjectIdentity
appnLocTg = _AppnLocTg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 10)
)
_AppnLocTgRowStatusTable_Object = MibTable
appnLocTgRowStatusTable = _AppnLocTgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 10, 1)
)
if mibBuilder.loadTexts:
    appnLocTgRowStatusTable.setStatus("mandatory")
_AppnLocTgRowStatusEntry_Object = MibTableRow
appnLocTgRowStatusEntry = _AppnLocTgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 10, 1, 1)
)
appnLocTgRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnLocTgDestFqcpNameIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnLocTgTransmissionGroupIndex"),
)
if mibBuilder.loadTexts:
    appnLocTgRowStatusEntry.setStatus("mandatory")
_AppnLocTgRowStatus_Type = RowStatus
_AppnLocTgRowStatus_Object = MibTableColumn
appnLocTgRowStatus = _AppnLocTgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 10, 1, 1, 1),
    _AppnLocTgRowStatus_Type()
)
appnLocTgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocTgRowStatus.setStatus("mandatory")
_AppnLocTgComponentName_Type = DisplayString
_AppnLocTgComponentName_Object = MibTableColumn
appnLocTgComponentName = _AppnLocTgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 10, 1, 1, 2),
    _AppnLocTgComponentName_Type()
)
appnLocTgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocTgComponentName.setStatus("mandatory")
_AppnLocTgStorageType_Type = StorageType
_AppnLocTgStorageType_Object = MibTableColumn
appnLocTgStorageType = _AppnLocTgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 10, 1, 1, 4),
    _AppnLocTgStorageType_Type()
)
appnLocTgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocTgStorageType.setStatus("mandatory")


class _AppnLocTgDestFqcpNameIndex_Type(AsciiStringIndex):
    """Custom type appnLocTgDestFqcpNameIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_AppnLocTgDestFqcpNameIndex_Type.__name__ = "AsciiStringIndex"
_AppnLocTgDestFqcpNameIndex_Object = MibTableColumn
appnLocTgDestFqcpNameIndex = _AppnLocTgDestFqcpNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 10, 1, 1, 10),
    _AppnLocTgDestFqcpNameIndex_Type()
)
appnLocTgDestFqcpNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnLocTgDestFqcpNameIndex.setStatus("mandatory")


class _AppnLocTgTransmissionGroupIndex_Type(Integer32):
    """Custom type appnLocTgTransmissionGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnLocTgTransmissionGroupIndex_Type.__name__ = "Integer32"
_AppnLocTgTransmissionGroupIndex_Object = MibTableColumn
appnLocTgTransmissionGroupIndex = _AppnLocTgTransmissionGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 10, 1, 1, 11),
    _AppnLocTgTransmissionGroupIndex_Type()
)
appnLocTgTransmissionGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnLocTgTransmissionGroupIndex.setStatus("mandatory")
_AppnLocTgOperTable_Object = MibTable
appnLocTgOperTable = _AppnLocTgOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 10, 10)
)
if mibBuilder.loadTexts:
    appnLocTgOperTable.setStatus("mandatory")
_AppnLocTgOperEntry_Object = MibTableRow
appnLocTgOperEntry = _AppnLocTgOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 10, 10, 1)
)
appnLocTgOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnLocTgDestFqcpNameIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnLocTgTransmissionGroupIndex"),
)
if mibBuilder.loadTexts:
    appnLocTgOperEntry.setStatus("mandatory")


class _AppnLocTgStatus_Type(OctetString):
    """Custom type appnLocTgStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AppnLocTgStatus_Type.__name__ = "OctetString"
_AppnLocTgStatus_Object = MibTableColumn
appnLocTgStatus = _AppnLocTgStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 10, 10, 1, 1),
    _AppnLocTgStatus_Type()
)
appnLocTgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocTgStatus.setStatus("mandatory")


class _AppnLocTgResourceSequenceNumber_Type(Unsigned32):
    """Custom type appnLocTgResourceSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AppnLocTgResourceSequenceNumber_Type.__name__ = "Unsigned32"
_AppnLocTgResourceSequenceNumber_Object = MibTableColumn
appnLocTgResourceSequenceNumber = _AppnLocTgResourceSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 10, 10, 1, 2),
    _AppnLocTgResourceSequenceNumber_Type()
)
appnLocTgResourceSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocTgResourceSequenceNumber.setStatus("mandatory")
_AppnLocTgLinkAddressTable_Object = MibTable
appnLocTgLinkAddressTable = _AppnLocTgLinkAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 10, 11)
)
if mibBuilder.loadTexts:
    appnLocTgLinkAddressTable.setStatus("mandatory")
_AppnLocTgLinkAddressEntry_Object = MibTableRow
appnLocTgLinkAddressEntry = _AppnLocTgLinkAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 10, 11, 1)
)
appnLocTgLinkAddressEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnLocTgDestFqcpNameIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnLocTgTransmissionGroupIndex"),
)
if mibBuilder.loadTexts:
    appnLocTgLinkAddressEntry.setStatus("mandatory")


class _AppnLocTgDlcData_Type(HexString):
    """Custom type appnLocTgDlcData based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AppnLocTgDlcData_Type.__name__ = "HexString"
_AppnLocTgDlcData_Object = MibTableColumn
appnLocTgDlcData = _AppnLocTgDlcData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 10, 11, 1, 1),
    _AppnLocTgDlcData_Type()
)
appnLocTgDlcData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocTgDlcData.setStatus("mandatory")
_AppnLocTgTgCharTable_Object = MibTable
appnLocTgTgCharTable = _AppnLocTgTgCharTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 10, 12)
)
if mibBuilder.loadTexts:
    appnLocTgTgCharTable.setStatus("mandatory")
_AppnLocTgTgCharEntry_Object = MibTableRow
appnLocTgTgCharEntry = _AppnLocTgTgCharEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 10, 12, 1)
)
appnLocTgTgCharEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnLocTgDestFqcpNameIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnLocTgTransmissionGroupIndex"),
)
if mibBuilder.loadTexts:
    appnLocTgTgCharEntry.setStatus("mandatory")


class _AppnLocTgEffectiveCap_Type(Integer32):
    """Custom type appnLocTgEffectiveCap based on Integer32"""
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


_AppnLocTgEffectiveCap_Type.__name__ = "Integer32"
_AppnLocTgEffectiveCap_Object = MibTableColumn
appnLocTgEffectiveCap = _AppnLocTgEffectiveCap_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 10, 12, 1, 1),
    _AppnLocTgEffectiveCap_Type()
)
appnLocTgEffectiveCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocTgEffectiveCap.setStatus("mandatory")


class _AppnLocTgConnectCost_Type(Integer32):
    """Custom type appnLocTgConnectCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnLocTgConnectCost_Type.__name__ = "Integer32"
_AppnLocTgConnectCost_Object = MibTableColumn
appnLocTgConnectCost = _AppnLocTgConnectCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 10, 12, 1, 2),
    _AppnLocTgConnectCost_Type()
)
appnLocTgConnectCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocTgConnectCost.setStatus("mandatory")


class _AppnLocTgByteCost_Type(Integer32):
    """Custom type appnLocTgByteCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnLocTgByteCost_Type.__name__ = "Integer32"
_AppnLocTgByteCost_Object = MibTableColumn
appnLocTgByteCost = _AppnLocTgByteCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 10, 12, 1, 3),
    _AppnLocTgByteCost_Type()
)
appnLocTgByteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocTgByteCost.setStatus("mandatory")


class _AppnLocTgSecurity_Type(Integer32):
    """Custom type appnLocTgSecurity based on Integer32"""
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


_AppnLocTgSecurity_Type.__name__ = "Integer32"
_AppnLocTgSecurity_Object = MibTableColumn
appnLocTgSecurity = _AppnLocTgSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 10, 12, 1, 4),
    _AppnLocTgSecurity_Type()
)
appnLocTgSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocTgSecurity.setStatus("mandatory")


class _AppnLocTgPropagationDelay_Type(Integer32):
    """Custom type appnLocTgPropagationDelay based on Integer32"""
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


_AppnLocTgPropagationDelay_Type.__name__ = "Integer32"
_AppnLocTgPropagationDelay_Object = MibTableColumn
appnLocTgPropagationDelay = _AppnLocTgPropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 10, 12, 1, 5),
    _AppnLocTgPropagationDelay_Type()
)
appnLocTgPropagationDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocTgPropagationDelay.setStatus("mandatory")


class _AppnLocTgUserDefinedParm1_Type(Unsigned32):
    """Custom type appnLocTgUserDefinedParm1 based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnLocTgUserDefinedParm1_Type.__name__ = "Unsigned32"
_AppnLocTgUserDefinedParm1_Object = MibTableColumn
appnLocTgUserDefinedParm1 = _AppnLocTgUserDefinedParm1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 10, 12, 1, 7),
    _AppnLocTgUserDefinedParm1_Type()
)
appnLocTgUserDefinedParm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocTgUserDefinedParm1.setStatus("mandatory")


class _AppnLocTgUserDefinedParm2_Type(Unsigned32):
    """Custom type appnLocTgUserDefinedParm2 based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnLocTgUserDefinedParm2_Type.__name__ = "Unsigned32"
_AppnLocTgUserDefinedParm2_Object = MibTableColumn
appnLocTgUserDefinedParm2 = _AppnLocTgUserDefinedParm2_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 10, 12, 1, 8),
    _AppnLocTgUserDefinedParm2_Type()
)
appnLocTgUserDefinedParm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocTgUserDefinedParm2.setStatus("mandatory")


class _AppnLocTgUserDefinedParm3_Type(Unsigned32):
    """Custom type appnLocTgUserDefinedParm3 based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnLocTgUserDefinedParm3_Type.__name__ = "Unsigned32"
_AppnLocTgUserDefinedParm3_Object = MibTableColumn
appnLocTgUserDefinedParm3 = _AppnLocTgUserDefinedParm3_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 10, 12, 1, 9),
    _AppnLocTgUserDefinedParm3_Type()
)
appnLocTgUserDefinedParm3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocTgUserDefinedParm3.setStatus("mandatory")
_AppnIsrSess_ObjectIdentity = ObjectIdentity
appnIsrSess = _AppnIsrSess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11)
)
_AppnIsrSessRowStatusTable_Object = MibTable
appnIsrSessRowStatusTable = _AppnIsrSessRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 1)
)
if mibBuilder.loadTexts:
    appnIsrSessRowStatusTable.setStatus("mandatory")
_AppnIsrSessRowStatusEntry_Object = MibTableRow
appnIsrSessRowStatusEntry = _AppnIsrSessRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 1, 1)
)
appnIsrSessRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIsrSessFqcpNameIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIsrSessProcedureCorrelationIdIndex"),
)
if mibBuilder.loadTexts:
    appnIsrSessRowStatusEntry.setStatus("mandatory")
_AppnIsrSessRowStatus_Type = RowStatus
_AppnIsrSessRowStatus_Object = MibTableColumn
appnIsrSessRowStatus = _AppnIsrSessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 1, 1, 1),
    _AppnIsrSessRowStatus_Type()
)
appnIsrSessRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessRowStatus.setStatus("mandatory")
_AppnIsrSessComponentName_Type = DisplayString
_AppnIsrSessComponentName_Object = MibTableColumn
appnIsrSessComponentName = _AppnIsrSessComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 1, 1, 2),
    _AppnIsrSessComponentName_Type()
)
appnIsrSessComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessComponentName.setStatus("mandatory")
_AppnIsrSessStorageType_Type = StorageType
_AppnIsrSessStorageType_Object = MibTableColumn
appnIsrSessStorageType = _AppnIsrSessStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 1, 1, 4),
    _AppnIsrSessStorageType_Type()
)
appnIsrSessStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessStorageType.setStatus("mandatory")


class _AppnIsrSessFqcpNameIndex_Type(AsciiStringIndex):
    """Custom type appnIsrSessFqcpNameIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_AppnIsrSessFqcpNameIndex_Type.__name__ = "AsciiStringIndex"
_AppnIsrSessFqcpNameIndex_Object = MibTableColumn
appnIsrSessFqcpNameIndex = _AppnIsrSessFqcpNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 1, 1, 10),
    _AppnIsrSessFqcpNameIndex_Type()
)
appnIsrSessFqcpNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnIsrSessFqcpNameIndex.setStatus("mandatory")


class _AppnIsrSessProcedureCorrelationIdIndex_Type(HexString):
    """Custom type appnIsrSessProcedureCorrelationIdIndex based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_AppnIsrSessProcedureCorrelationIdIndex_Type.__name__ = "HexString"
_AppnIsrSessProcedureCorrelationIdIndex_Object = MibTableColumn
appnIsrSessProcedureCorrelationIdIndex = _AppnIsrSessProcedureCorrelationIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 1, 1, 11),
    _AppnIsrSessProcedureCorrelationIdIndex_Type()
)
appnIsrSessProcedureCorrelationIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnIsrSessProcedureCorrelationIdIndex.setStatus("mandatory")
_AppnIsrSessOperTable_Object = MibTable
appnIsrSessOperTable = _AppnIsrSessOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 10)
)
if mibBuilder.loadTexts:
    appnIsrSessOperTable.setStatus("mandatory")
_AppnIsrSessOperEntry_Object = MibTableRow
appnIsrSessOperEntry = _AppnIsrSessOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 10, 1)
)
appnIsrSessOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIsrSessFqcpNameIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIsrSessProcedureCorrelationIdIndex"),
)
if mibBuilder.loadTexts:
    appnIsrSessOperEntry.setStatus("mandatory")


class _AppnIsrSessTransmissionPriority_Type(Integer32):
    """Custom type appnIsrSessTransmissionPriority based on Integer32"""
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


_AppnIsrSessTransmissionPriority_Type.__name__ = "Integer32"
_AppnIsrSessTransmissionPriority_Object = MibTableColumn
appnIsrSessTransmissionPriority = _AppnIsrSessTransmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 10, 1, 1),
    _AppnIsrSessTransmissionPriority_Type()
)
appnIsrSessTransmissionPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessTransmissionPriority.setStatus("mandatory")


class _AppnIsrSessCosName_Type(AsciiString):
    """Custom type appnIsrSessCosName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppnIsrSessCosName_Type.__name__ = "AsciiString"
_AppnIsrSessCosName_Object = MibTableColumn
appnIsrSessCosName = _AppnIsrSessCosName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 10, 1, 2),
    _AppnIsrSessCosName_Type()
)
appnIsrSessCosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessCosName.setStatus("mandatory")


class _AppnIsrSessLimitedResource_Type(Integer32):
    """Custom type appnIsrSessLimitedResource based on Integer32"""
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


_AppnIsrSessLimitedResource_Type.__name__ = "Integer32"
_AppnIsrSessLimitedResource_Object = MibTableColumn
appnIsrSessLimitedResource = _AppnIsrSessLimitedResource_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 10, 1, 3),
    _AppnIsrSessLimitedResource_Type()
)
appnIsrSessLimitedResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessLimitedResource.setStatus("mandatory")
_AppnIsrSessPriStats_ObjectIdentity = ObjectIdentity
appnIsrSessPriStats = _AppnIsrSessPriStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 100)
)
_AppnIsrSessPriStatsRowStatusTable_Object = MibTable
appnIsrSessPriStatsRowStatusTable = _AppnIsrSessPriStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 100, 1)
)
if mibBuilder.loadTexts:
    appnIsrSessPriStatsRowStatusTable.setStatus("mandatory")
_AppnIsrSessPriStatsRowStatusEntry_Object = MibTableRow
appnIsrSessPriStatsRowStatusEntry = _AppnIsrSessPriStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 100, 1, 1)
)
appnIsrSessPriStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIsrSessFqcpNameIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIsrSessProcedureCorrelationIdIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIsrSessPriStatsIndex"),
)
if mibBuilder.loadTexts:
    appnIsrSessPriStatsRowStatusEntry.setStatus("mandatory")
_AppnIsrSessPriStatsRowStatus_Type = RowStatus
_AppnIsrSessPriStatsRowStatus_Object = MibTableColumn
appnIsrSessPriStatsRowStatus = _AppnIsrSessPriStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 100, 1, 1, 1),
    _AppnIsrSessPriStatsRowStatus_Type()
)
appnIsrSessPriStatsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessPriStatsRowStatus.setStatus("mandatory")
_AppnIsrSessPriStatsComponentName_Type = DisplayString
_AppnIsrSessPriStatsComponentName_Object = MibTableColumn
appnIsrSessPriStatsComponentName = _AppnIsrSessPriStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 100, 1, 1, 2),
    _AppnIsrSessPriStatsComponentName_Type()
)
appnIsrSessPriStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessPriStatsComponentName.setStatus("mandatory")
_AppnIsrSessPriStatsStorageType_Type = StorageType
_AppnIsrSessPriStatsStorageType_Object = MibTableColumn
appnIsrSessPriStatsStorageType = _AppnIsrSessPriStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 100, 1, 1, 4),
    _AppnIsrSessPriStatsStorageType_Type()
)
appnIsrSessPriStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessPriStatsStorageType.setStatus("mandatory")
_AppnIsrSessPriStatsIndex_Type = NonReplicated
_AppnIsrSessPriStatsIndex_Object = MibTableColumn
appnIsrSessPriStatsIndex = _AppnIsrSessPriStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 100, 1, 1, 10),
    _AppnIsrSessPriStatsIndex_Type()
)
appnIsrSessPriStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnIsrSessPriStatsIndex.setStatus("mandatory")
_AppnIsrSessPriStatsStatsTable_Object = MibTable
appnIsrSessPriStatsStatsTable = _AppnIsrSessPriStatsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 100, 10)
)
if mibBuilder.loadTexts:
    appnIsrSessPriStatsStatsTable.setStatus("mandatory")
_AppnIsrSessPriStatsStatsEntry_Object = MibTableRow
appnIsrSessPriStatsStatsEntry = _AppnIsrSessPriStatsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 100, 10, 1)
)
appnIsrSessPriStatsStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIsrSessFqcpNameIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIsrSessProcedureCorrelationIdIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIsrSessPriStatsIndex"),
)
if mibBuilder.loadTexts:
    appnIsrSessPriStatsStatsEntry.setStatus("mandatory")


class _AppnIsrSessPriStatsRxRuSize_Type(Unsigned32):
    """Custom type appnIsrSessPriStatsRxRuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnIsrSessPriStatsRxRuSize_Type.__name__ = "Unsigned32"
_AppnIsrSessPriStatsRxRuSize_Object = MibTableColumn
appnIsrSessPriStatsRxRuSize = _AppnIsrSessPriStatsRxRuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 100, 10, 1, 1),
    _AppnIsrSessPriStatsRxRuSize_Type()
)
appnIsrSessPriStatsRxRuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessPriStatsRxRuSize.setStatus("mandatory")


class _AppnIsrSessPriStatsMaxTxBtuSize_Type(Unsigned32):
    """Custom type appnIsrSessPriStatsMaxTxBtuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnIsrSessPriStatsMaxTxBtuSize_Type.__name__ = "Unsigned32"
_AppnIsrSessPriStatsMaxTxBtuSize_Object = MibTableColumn
appnIsrSessPriStatsMaxTxBtuSize = _AppnIsrSessPriStatsMaxTxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 100, 10, 1, 2),
    _AppnIsrSessPriStatsMaxTxBtuSize_Type()
)
appnIsrSessPriStatsMaxTxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessPriStatsMaxTxBtuSize.setStatus("mandatory")


class _AppnIsrSessPriStatsMaxRxBtuSize_Type(Unsigned32):
    """Custom type appnIsrSessPriStatsMaxRxBtuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnIsrSessPriStatsMaxRxBtuSize_Type.__name__ = "Unsigned32"
_AppnIsrSessPriStatsMaxRxBtuSize_Object = MibTableColumn
appnIsrSessPriStatsMaxRxBtuSize = _AppnIsrSessPriStatsMaxRxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 100, 10, 1, 3),
    _AppnIsrSessPriStatsMaxRxBtuSize_Type()
)
appnIsrSessPriStatsMaxRxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessPriStatsMaxRxBtuSize.setStatus("mandatory")


class _AppnIsrSessPriStatsMaxTxPacWin_Type(Integer32):
    """Custom type appnIsrSessPriStatsMaxTxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AppnIsrSessPriStatsMaxTxPacWin_Type.__name__ = "Integer32"
_AppnIsrSessPriStatsMaxTxPacWin_Object = MibTableColumn
appnIsrSessPriStatsMaxTxPacWin = _AppnIsrSessPriStatsMaxTxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 100, 10, 1, 4),
    _AppnIsrSessPriStatsMaxTxPacWin_Type()
)
appnIsrSessPriStatsMaxTxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessPriStatsMaxTxPacWin.setStatus("mandatory")


class _AppnIsrSessPriStatsCurTxPacWin_Type(Integer32):
    """Custom type appnIsrSessPriStatsCurTxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AppnIsrSessPriStatsCurTxPacWin_Type.__name__ = "Integer32"
_AppnIsrSessPriStatsCurTxPacWin_Object = MibTableColumn
appnIsrSessPriStatsCurTxPacWin = _AppnIsrSessPriStatsCurTxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 100, 10, 1, 5),
    _AppnIsrSessPriStatsCurTxPacWin_Type()
)
appnIsrSessPriStatsCurTxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessPriStatsCurTxPacWin.setStatus("mandatory")


class _AppnIsrSessPriStatsMaxRxPacWin_Type(Integer32):
    """Custom type appnIsrSessPriStatsMaxRxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AppnIsrSessPriStatsMaxRxPacWin_Type.__name__ = "Integer32"
_AppnIsrSessPriStatsMaxRxPacWin_Object = MibTableColumn
appnIsrSessPriStatsMaxRxPacWin = _AppnIsrSessPriStatsMaxRxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 100, 10, 1, 6),
    _AppnIsrSessPriStatsMaxRxPacWin_Type()
)
appnIsrSessPriStatsMaxRxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessPriStatsMaxRxPacWin.setStatus("mandatory")


class _AppnIsrSessPriStatsCurRxPacWin_Type(Integer32):
    """Custom type appnIsrSessPriStatsCurRxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AppnIsrSessPriStatsCurRxPacWin_Type.__name__ = "Integer32"
_AppnIsrSessPriStatsCurRxPacWin_Object = MibTableColumn
appnIsrSessPriStatsCurRxPacWin = _AppnIsrSessPriStatsCurRxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 100, 10, 1, 7),
    _AppnIsrSessPriStatsCurRxPacWin_Type()
)
appnIsrSessPriStatsCurRxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessPriStatsCurRxPacWin.setStatus("mandatory")
_AppnIsrSessPriStatsTxDataframes_Type = PassportCounter64
_AppnIsrSessPriStatsTxDataframes_Object = MibTableColumn
appnIsrSessPriStatsTxDataframes = _AppnIsrSessPriStatsTxDataframes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 100, 10, 1, 8),
    _AppnIsrSessPriStatsTxDataframes_Type()
)
appnIsrSessPriStatsTxDataframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessPriStatsTxDataframes.setStatus("mandatory")
_AppnIsrSessPriStatsTxFmdFrames_Type = PassportCounter64
_AppnIsrSessPriStatsTxFmdFrames_Object = MibTableColumn
appnIsrSessPriStatsTxFmdFrames = _AppnIsrSessPriStatsTxFmdFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 100, 10, 1, 9),
    _AppnIsrSessPriStatsTxFmdFrames_Type()
)
appnIsrSessPriStatsTxFmdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessPriStatsTxFmdFrames.setStatus("mandatory")
_AppnIsrSessPriStatsTxDataBytes_Type = PassportCounter64
_AppnIsrSessPriStatsTxDataBytes_Object = MibTableColumn
appnIsrSessPriStatsTxDataBytes = _AppnIsrSessPriStatsTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 100, 10, 1, 10),
    _AppnIsrSessPriStatsTxDataBytes_Type()
)
appnIsrSessPriStatsTxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessPriStatsTxDataBytes.setStatus("mandatory")
_AppnIsrSessPriStatsRxDataFrames_Type = PassportCounter64
_AppnIsrSessPriStatsRxDataFrames_Object = MibTableColumn
appnIsrSessPriStatsRxDataFrames = _AppnIsrSessPriStatsRxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 100, 10, 1, 11),
    _AppnIsrSessPriStatsRxDataFrames_Type()
)
appnIsrSessPriStatsRxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessPriStatsRxDataFrames.setStatus("mandatory")
_AppnIsrSessPriStatsRxFmdFrames_Type = PassportCounter64
_AppnIsrSessPriStatsRxFmdFrames_Object = MibTableColumn
appnIsrSessPriStatsRxFmdFrames = _AppnIsrSessPriStatsRxFmdFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 100, 10, 1, 12),
    _AppnIsrSessPriStatsRxFmdFrames_Type()
)
appnIsrSessPriStatsRxFmdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessPriStatsRxFmdFrames.setStatus("mandatory")
_AppnIsrSessPriStatsRxDataBytes_Type = PassportCounter64
_AppnIsrSessPriStatsRxDataBytes_Object = MibTableColumn
appnIsrSessPriStatsRxDataBytes = _AppnIsrSessPriStatsRxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 100, 10, 1, 13),
    _AppnIsrSessPriStatsRxDataBytes_Type()
)
appnIsrSessPriStatsRxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessPriStatsRxDataBytes.setStatus("mandatory")


class _AppnIsrSessPriStatsSidh_Type(Hex):
    """Custom type appnIsrSessPriStatsSidh based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnIsrSessPriStatsSidh_Type.__name__ = "Hex"
_AppnIsrSessPriStatsSidh_Object = MibTableColumn
appnIsrSessPriStatsSidh = _AppnIsrSessPriStatsSidh_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 100, 10, 1, 14),
    _AppnIsrSessPriStatsSidh_Type()
)
appnIsrSessPriStatsSidh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessPriStatsSidh.setStatus("mandatory")


class _AppnIsrSessPriStatsSidl_Type(Hex):
    """Custom type appnIsrSessPriStatsSidl based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnIsrSessPriStatsSidl_Type.__name__ = "Hex"
_AppnIsrSessPriStatsSidl_Object = MibTableColumn
appnIsrSessPriStatsSidl = _AppnIsrSessPriStatsSidl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 100, 10, 1, 15),
    _AppnIsrSessPriStatsSidl_Type()
)
appnIsrSessPriStatsSidl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessPriStatsSidl.setStatus("mandatory")


class _AppnIsrSessPriStatsOdai_Type(Integer32):
    """Custom type appnIsrSessPriStatsOdai based on Integer32"""
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


_AppnIsrSessPriStatsOdai_Type.__name__ = "Integer32"
_AppnIsrSessPriStatsOdai_Object = MibTableColumn
appnIsrSessPriStatsOdai = _AppnIsrSessPriStatsOdai_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 100, 10, 1, 16),
    _AppnIsrSessPriStatsOdai_Type()
)
appnIsrSessPriStatsOdai.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessPriStatsOdai.setStatus("mandatory")


class _AppnIsrSessPriStatsLsName_Type(AsciiString):
    """Custom type appnIsrSessPriStatsLsName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppnIsrSessPriStatsLsName_Type.__name__ = "AsciiString"
_AppnIsrSessPriStatsLsName_Object = MibTableColumn
appnIsrSessPriStatsLsName = _AppnIsrSessPriStatsLsName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 100, 10, 1, 17),
    _AppnIsrSessPriStatsLsName_Type()
)
appnIsrSessPriStatsLsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessPriStatsLsName.setStatus("mandatory")
_AppnIsrSessSecStats_ObjectIdentity = ObjectIdentity
appnIsrSessSecStats = _AppnIsrSessSecStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 101)
)
_AppnIsrSessSecStatsRowStatusTable_Object = MibTable
appnIsrSessSecStatsRowStatusTable = _AppnIsrSessSecStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 101, 1)
)
if mibBuilder.loadTexts:
    appnIsrSessSecStatsRowStatusTable.setStatus("mandatory")
_AppnIsrSessSecStatsRowStatusEntry_Object = MibTableRow
appnIsrSessSecStatsRowStatusEntry = _AppnIsrSessSecStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 101, 1, 1)
)
appnIsrSessSecStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIsrSessFqcpNameIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIsrSessProcedureCorrelationIdIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIsrSessSecStatsIndex"),
)
if mibBuilder.loadTexts:
    appnIsrSessSecStatsRowStatusEntry.setStatus("mandatory")
_AppnIsrSessSecStatsRowStatus_Type = RowStatus
_AppnIsrSessSecStatsRowStatus_Object = MibTableColumn
appnIsrSessSecStatsRowStatus = _AppnIsrSessSecStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 101, 1, 1, 1),
    _AppnIsrSessSecStatsRowStatus_Type()
)
appnIsrSessSecStatsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessSecStatsRowStatus.setStatus("mandatory")
_AppnIsrSessSecStatsComponentName_Type = DisplayString
_AppnIsrSessSecStatsComponentName_Object = MibTableColumn
appnIsrSessSecStatsComponentName = _AppnIsrSessSecStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 101, 1, 1, 2),
    _AppnIsrSessSecStatsComponentName_Type()
)
appnIsrSessSecStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessSecStatsComponentName.setStatus("mandatory")
_AppnIsrSessSecStatsStorageType_Type = StorageType
_AppnIsrSessSecStatsStorageType_Object = MibTableColumn
appnIsrSessSecStatsStorageType = _AppnIsrSessSecStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 101, 1, 1, 4),
    _AppnIsrSessSecStatsStorageType_Type()
)
appnIsrSessSecStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessSecStatsStorageType.setStatus("mandatory")
_AppnIsrSessSecStatsIndex_Type = NonReplicated
_AppnIsrSessSecStatsIndex_Object = MibTableColumn
appnIsrSessSecStatsIndex = _AppnIsrSessSecStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 101, 1, 1, 10),
    _AppnIsrSessSecStatsIndex_Type()
)
appnIsrSessSecStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnIsrSessSecStatsIndex.setStatus("mandatory")
_AppnIsrSessSecStatsStatsTable_Object = MibTable
appnIsrSessSecStatsStatsTable = _AppnIsrSessSecStatsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 101, 10)
)
if mibBuilder.loadTexts:
    appnIsrSessSecStatsStatsTable.setStatus("mandatory")
_AppnIsrSessSecStatsStatsEntry_Object = MibTableRow
appnIsrSessSecStatsStatsEntry = _AppnIsrSessSecStatsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 101, 10, 1)
)
appnIsrSessSecStatsStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIsrSessFqcpNameIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIsrSessProcedureCorrelationIdIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIsrSessSecStatsIndex"),
)
if mibBuilder.loadTexts:
    appnIsrSessSecStatsStatsEntry.setStatus("mandatory")


class _AppnIsrSessSecStatsRxRuSize_Type(Unsigned32):
    """Custom type appnIsrSessSecStatsRxRuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnIsrSessSecStatsRxRuSize_Type.__name__ = "Unsigned32"
_AppnIsrSessSecStatsRxRuSize_Object = MibTableColumn
appnIsrSessSecStatsRxRuSize = _AppnIsrSessSecStatsRxRuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 101, 10, 1, 1),
    _AppnIsrSessSecStatsRxRuSize_Type()
)
appnIsrSessSecStatsRxRuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessSecStatsRxRuSize.setStatus("mandatory")


class _AppnIsrSessSecStatsMaxTxBtuSize_Type(Unsigned32):
    """Custom type appnIsrSessSecStatsMaxTxBtuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnIsrSessSecStatsMaxTxBtuSize_Type.__name__ = "Unsigned32"
_AppnIsrSessSecStatsMaxTxBtuSize_Object = MibTableColumn
appnIsrSessSecStatsMaxTxBtuSize = _AppnIsrSessSecStatsMaxTxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 101, 10, 1, 2),
    _AppnIsrSessSecStatsMaxTxBtuSize_Type()
)
appnIsrSessSecStatsMaxTxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessSecStatsMaxTxBtuSize.setStatus("mandatory")


class _AppnIsrSessSecStatsMaxRxBtuSize_Type(Unsigned32):
    """Custom type appnIsrSessSecStatsMaxRxBtuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnIsrSessSecStatsMaxRxBtuSize_Type.__name__ = "Unsigned32"
_AppnIsrSessSecStatsMaxRxBtuSize_Object = MibTableColumn
appnIsrSessSecStatsMaxRxBtuSize = _AppnIsrSessSecStatsMaxRxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 101, 10, 1, 3),
    _AppnIsrSessSecStatsMaxRxBtuSize_Type()
)
appnIsrSessSecStatsMaxRxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessSecStatsMaxRxBtuSize.setStatus("mandatory")


class _AppnIsrSessSecStatsMaxTxPacWin_Type(Integer32):
    """Custom type appnIsrSessSecStatsMaxTxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AppnIsrSessSecStatsMaxTxPacWin_Type.__name__ = "Integer32"
_AppnIsrSessSecStatsMaxTxPacWin_Object = MibTableColumn
appnIsrSessSecStatsMaxTxPacWin = _AppnIsrSessSecStatsMaxTxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 101, 10, 1, 4),
    _AppnIsrSessSecStatsMaxTxPacWin_Type()
)
appnIsrSessSecStatsMaxTxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessSecStatsMaxTxPacWin.setStatus("mandatory")


class _AppnIsrSessSecStatsCurTxPacWin_Type(Integer32):
    """Custom type appnIsrSessSecStatsCurTxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AppnIsrSessSecStatsCurTxPacWin_Type.__name__ = "Integer32"
_AppnIsrSessSecStatsCurTxPacWin_Object = MibTableColumn
appnIsrSessSecStatsCurTxPacWin = _AppnIsrSessSecStatsCurTxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 101, 10, 1, 5),
    _AppnIsrSessSecStatsCurTxPacWin_Type()
)
appnIsrSessSecStatsCurTxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessSecStatsCurTxPacWin.setStatus("mandatory")


class _AppnIsrSessSecStatsMaxRxPacWin_Type(Integer32):
    """Custom type appnIsrSessSecStatsMaxRxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AppnIsrSessSecStatsMaxRxPacWin_Type.__name__ = "Integer32"
_AppnIsrSessSecStatsMaxRxPacWin_Object = MibTableColumn
appnIsrSessSecStatsMaxRxPacWin = _AppnIsrSessSecStatsMaxRxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 101, 10, 1, 6),
    _AppnIsrSessSecStatsMaxRxPacWin_Type()
)
appnIsrSessSecStatsMaxRxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessSecStatsMaxRxPacWin.setStatus("mandatory")


class _AppnIsrSessSecStatsCurRxPacWin_Type(Integer32):
    """Custom type appnIsrSessSecStatsCurRxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AppnIsrSessSecStatsCurRxPacWin_Type.__name__ = "Integer32"
_AppnIsrSessSecStatsCurRxPacWin_Object = MibTableColumn
appnIsrSessSecStatsCurRxPacWin = _AppnIsrSessSecStatsCurRxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 101, 10, 1, 7),
    _AppnIsrSessSecStatsCurRxPacWin_Type()
)
appnIsrSessSecStatsCurRxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessSecStatsCurRxPacWin.setStatus("mandatory")
_AppnIsrSessSecStatsTxDataframes_Type = PassportCounter64
_AppnIsrSessSecStatsTxDataframes_Object = MibTableColumn
appnIsrSessSecStatsTxDataframes = _AppnIsrSessSecStatsTxDataframes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 101, 10, 1, 8),
    _AppnIsrSessSecStatsTxDataframes_Type()
)
appnIsrSessSecStatsTxDataframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessSecStatsTxDataframes.setStatus("mandatory")
_AppnIsrSessSecStatsTxFmdFrames_Type = PassportCounter64
_AppnIsrSessSecStatsTxFmdFrames_Object = MibTableColumn
appnIsrSessSecStatsTxFmdFrames = _AppnIsrSessSecStatsTxFmdFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 101, 10, 1, 9),
    _AppnIsrSessSecStatsTxFmdFrames_Type()
)
appnIsrSessSecStatsTxFmdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessSecStatsTxFmdFrames.setStatus("mandatory")
_AppnIsrSessSecStatsTxDataBytes_Type = PassportCounter64
_AppnIsrSessSecStatsTxDataBytes_Object = MibTableColumn
appnIsrSessSecStatsTxDataBytes = _AppnIsrSessSecStatsTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 101, 10, 1, 10),
    _AppnIsrSessSecStatsTxDataBytes_Type()
)
appnIsrSessSecStatsTxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessSecStatsTxDataBytes.setStatus("mandatory")
_AppnIsrSessSecStatsRxDataFrames_Type = PassportCounter64
_AppnIsrSessSecStatsRxDataFrames_Object = MibTableColumn
appnIsrSessSecStatsRxDataFrames = _AppnIsrSessSecStatsRxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 101, 10, 1, 11),
    _AppnIsrSessSecStatsRxDataFrames_Type()
)
appnIsrSessSecStatsRxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessSecStatsRxDataFrames.setStatus("mandatory")
_AppnIsrSessSecStatsRxFmdFrames_Type = PassportCounter64
_AppnIsrSessSecStatsRxFmdFrames_Object = MibTableColumn
appnIsrSessSecStatsRxFmdFrames = _AppnIsrSessSecStatsRxFmdFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 101, 10, 1, 12),
    _AppnIsrSessSecStatsRxFmdFrames_Type()
)
appnIsrSessSecStatsRxFmdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessSecStatsRxFmdFrames.setStatus("mandatory")
_AppnIsrSessSecStatsRxDataBytes_Type = PassportCounter64
_AppnIsrSessSecStatsRxDataBytes_Object = MibTableColumn
appnIsrSessSecStatsRxDataBytes = _AppnIsrSessSecStatsRxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 101, 10, 1, 13),
    _AppnIsrSessSecStatsRxDataBytes_Type()
)
appnIsrSessSecStatsRxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessSecStatsRxDataBytes.setStatus("mandatory")


class _AppnIsrSessSecStatsSidh_Type(Hex):
    """Custom type appnIsrSessSecStatsSidh based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnIsrSessSecStatsSidh_Type.__name__ = "Hex"
_AppnIsrSessSecStatsSidh_Object = MibTableColumn
appnIsrSessSecStatsSidh = _AppnIsrSessSecStatsSidh_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 101, 10, 1, 14),
    _AppnIsrSessSecStatsSidh_Type()
)
appnIsrSessSecStatsSidh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessSecStatsSidh.setStatus("mandatory")


class _AppnIsrSessSecStatsSidl_Type(Hex):
    """Custom type appnIsrSessSecStatsSidl based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnIsrSessSecStatsSidl_Type.__name__ = "Hex"
_AppnIsrSessSecStatsSidl_Object = MibTableColumn
appnIsrSessSecStatsSidl = _AppnIsrSessSecStatsSidl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 101, 10, 1, 15),
    _AppnIsrSessSecStatsSidl_Type()
)
appnIsrSessSecStatsSidl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessSecStatsSidl.setStatus("mandatory")


class _AppnIsrSessSecStatsOdai_Type(Integer32):
    """Custom type appnIsrSessSecStatsOdai based on Integer32"""
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


_AppnIsrSessSecStatsOdai_Type.__name__ = "Integer32"
_AppnIsrSessSecStatsOdai_Object = MibTableColumn
appnIsrSessSecStatsOdai = _AppnIsrSessSecStatsOdai_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 101, 10, 1, 16),
    _AppnIsrSessSecStatsOdai_Type()
)
appnIsrSessSecStatsOdai.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessSecStatsOdai.setStatus("mandatory")


class _AppnIsrSessSecStatsLsName_Type(AsciiString):
    """Custom type appnIsrSessSecStatsLsName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppnIsrSessSecStatsLsName_Type.__name__ = "AsciiString"
_AppnIsrSessSecStatsLsName_Object = MibTableColumn
appnIsrSessSecStatsLsName = _AppnIsrSessSecStatsLsName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 11, 101, 10, 1, 17),
    _AppnIsrSessSecStatsLsName_Type()
)
appnIsrSessSecStatsLsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsrSessSecStatsLsName.setStatus("mandatory")
_AppnNnTg_ObjectIdentity = ObjectIdentity
appnNnTg = _AppnNnTg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 12)
)
_AppnNnTgRowStatusTable_Object = MibTable
appnNnTgRowStatusTable = _AppnNnTgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 12, 1)
)
if mibBuilder.loadTexts:
    appnNnTgRowStatusTable.setStatus("mandatory")
_AppnNnTgRowStatusEntry_Object = MibTableRow
appnNnTgRowStatusEntry = _AppnNnTgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 12, 1, 1)
)
appnNnTgRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnNnTgOwnerFqcpNameIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnNnTgDestFqcpNameIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnNnTgTransmissionGroupIndex"),
)
if mibBuilder.loadTexts:
    appnNnTgRowStatusEntry.setStatus("mandatory")
_AppnNnTgRowStatus_Type = RowStatus
_AppnNnTgRowStatus_Object = MibTableColumn
appnNnTgRowStatus = _AppnNnTgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 12, 1, 1, 1),
    _AppnNnTgRowStatus_Type()
)
appnNnTgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgRowStatus.setStatus("mandatory")
_AppnNnTgComponentName_Type = DisplayString
_AppnNnTgComponentName_Object = MibTableColumn
appnNnTgComponentName = _AppnNnTgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 12, 1, 1, 2),
    _AppnNnTgComponentName_Type()
)
appnNnTgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgComponentName.setStatus("mandatory")
_AppnNnTgStorageType_Type = StorageType
_AppnNnTgStorageType_Object = MibTableColumn
appnNnTgStorageType = _AppnNnTgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 12, 1, 1, 4),
    _AppnNnTgStorageType_Type()
)
appnNnTgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgStorageType.setStatus("mandatory")


class _AppnNnTgOwnerFqcpNameIndex_Type(AsciiStringIndex):
    """Custom type appnNnTgOwnerFqcpNameIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_AppnNnTgOwnerFqcpNameIndex_Type.__name__ = "AsciiStringIndex"
_AppnNnTgOwnerFqcpNameIndex_Object = MibTableColumn
appnNnTgOwnerFqcpNameIndex = _AppnNnTgOwnerFqcpNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 12, 1, 1, 10),
    _AppnNnTgOwnerFqcpNameIndex_Type()
)
appnNnTgOwnerFqcpNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnNnTgOwnerFqcpNameIndex.setStatus("mandatory")


class _AppnNnTgDestFqcpNameIndex_Type(AsciiStringIndex):
    """Custom type appnNnTgDestFqcpNameIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_AppnNnTgDestFqcpNameIndex_Type.__name__ = "AsciiStringIndex"
_AppnNnTgDestFqcpNameIndex_Object = MibTableColumn
appnNnTgDestFqcpNameIndex = _AppnNnTgDestFqcpNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 12, 1, 1, 11),
    _AppnNnTgDestFqcpNameIndex_Type()
)
appnNnTgDestFqcpNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnNnTgDestFqcpNameIndex.setStatus("mandatory")


class _AppnNnTgTransmissionGroupIndex_Type(Integer32):
    """Custom type appnNnTgTransmissionGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnNnTgTransmissionGroupIndex_Type.__name__ = "Integer32"
_AppnNnTgTransmissionGroupIndex_Object = MibTableColumn
appnNnTgTransmissionGroupIndex = _AppnNnTgTransmissionGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 12, 1, 1, 12),
    _AppnNnTgTransmissionGroupIndex_Type()
)
appnNnTgTransmissionGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnNnTgTransmissionGroupIndex.setStatus("mandatory")
_AppnNnTgOperTable_Object = MibTable
appnNnTgOperTable = _AppnNnTgOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 12, 10)
)
if mibBuilder.loadTexts:
    appnNnTgOperTable.setStatus("mandatory")
_AppnNnTgOperEntry_Object = MibTableRow
appnNnTgOperEntry = _AppnNnTgOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 12, 10, 1)
)
appnNnTgOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnNnTgOwnerFqcpNameIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnNnTgDestFqcpNameIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnNnTgTransmissionGroupIndex"),
)
if mibBuilder.loadTexts:
    appnNnTgOperEntry.setStatus("mandatory")


class _AppnNnTgFlowReductionSequenceNumber_Type(Unsigned32):
    """Custom type appnNnTgFlowReductionSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AppnNnTgFlowReductionSequenceNumber_Type.__name__ = "Unsigned32"
_AppnNnTgFlowReductionSequenceNumber_Object = MibTableColumn
appnNnTgFlowReductionSequenceNumber = _AppnNnTgFlowReductionSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 12, 10, 1, 1),
    _AppnNnTgFlowReductionSequenceNumber_Type()
)
appnNnTgFlowReductionSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgFlowReductionSequenceNumber.setStatus("mandatory")


class _AppnNnTgDaysLeft_Type(Unsigned32):
    """Custom type appnNnTgDaysLeft based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_AppnNnTgDaysLeft_Type.__name__ = "Unsigned32"
_AppnNnTgDaysLeft_Object = MibTableColumn
appnNnTgDaysLeft = _AppnNnTgDaysLeft_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 12, 10, 1, 2),
    _AppnNnTgDaysLeft_Type()
)
appnNnTgDaysLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgDaysLeft.setStatus("mandatory")


class _AppnNnTgResourceSequenceNumber_Type(Unsigned32):
    """Custom type appnNnTgResourceSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AppnNnTgResourceSequenceNumber_Type.__name__ = "Unsigned32"
_AppnNnTgResourceSequenceNumber_Object = MibTableColumn
appnNnTgResourceSequenceNumber = _AppnNnTgResourceSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 12, 10, 1, 3),
    _AppnNnTgResourceSequenceNumber_Type()
)
appnNnTgResourceSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgResourceSequenceNumber.setStatus("mandatory")


class _AppnNnTgStatus_Type(OctetString):
    """Custom type appnNnTgStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AppnNnTgStatus_Type.__name__ = "OctetString"
_AppnNnTgStatus_Object = MibTableColumn
appnNnTgStatus = _AppnNnTgStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 12, 10, 1, 4),
    _AppnNnTgStatus_Type()
)
appnNnTgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgStatus.setStatus("mandatory")
_AppnNnTgLinkAddressTable_Object = MibTable
appnNnTgLinkAddressTable = _AppnNnTgLinkAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 12, 11)
)
if mibBuilder.loadTexts:
    appnNnTgLinkAddressTable.setStatus("mandatory")
_AppnNnTgLinkAddressEntry_Object = MibTableRow
appnNnTgLinkAddressEntry = _AppnNnTgLinkAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 12, 11, 1)
)
appnNnTgLinkAddressEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnNnTgOwnerFqcpNameIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnNnTgDestFqcpNameIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnNnTgTransmissionGroupIndex"),
)
if mibBuilder.loadTexts:
    appnNnTgLinkAddressEntry.setStatus("mandatory")


class _AppnNnTgDlcData_Type(HexString):
    """Custom type appnNnTgDlcData based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AppnNnTgDlcData_Type.__name__ = "HexString"
_AppnNnTgDlcData_Object = MibTableColumn
appnNnTgDlcData = _AppnNnTgDlcData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 12, 11, 1, 1),
    _AppnNnTgDlcData_Type()
)
appnNnTgDlcData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgDlcData.setStatus("mandatory")
_AppnNnTgTgCharTable_Object = MibTable
appnNnTgTgCharTable = _AppnNnTgTgCharTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 12, 12)
)
if mibBuilder.loadTexts:
    appnNnTgTgCharTable.setStatus("mandatory")
_AppnNnTgTgCharEntry_Object = MibTableRow
appnNnTgTgCharEntry = _AppnNnTgTgCharEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 12, 12, 1)
)
appnNnTgTgCharEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnNnTgOwnerFqcpNameIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnNnTgDestFqcpNameIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnNnTgTransmissionGroupIndex"),
)
if mibBuilder.loadTexts:
    appnNnTgTgCharEntry.setStatus("mandatory")


class _AppnNnTgEffectiveCap_Type(Integer32):
    """Custom type appnNnTgEffectiveCap based on Integer32"""
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


_AppnNnTgEffectiveCap_Type.__name__ = "Integer32"
_AppnNnTgEffectiveCap_Object = MibTableColumn
appnNnTgEffectiveCap = _AppnNnTgEffectiveCap_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 12, 12, 1, 1),
    _AppnNnTgEffectiveCap_Type()
)
appnNnTgEffectiveCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgEffectiveCap.setStatus("mandatory")


class _AppnNnTgConnectCost_Type(Integer32):
    """Custom type appnNnTgConnectCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnNnTgConnectCost_Type.__name__ = "Integer32"
_AppnNnTgConnectCost_Object = MibTableColumn
appnNnTgConnectCost = _AppnNnTgConnectCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 12, 12, 1, 2),
    _AppnNnTgConnectCost_Type()
)
appnNnTgConnectCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgConnectCost.setStatus("mandatory")


class _AppnNnTgByteCost_Type(Integer32):
    """Custom type appnNnTgByteCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnNnTgByteCost_Type.__name__ = "Integer32"
_AppnNnTgByteCost_Object = MibTableColumn
appnNnTgByteCost = _AppnNnTgByteCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 12, 12, 1, 3),
    _AppnNnTgByteCost_Type()
)
appnNnTgByteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgByteCost.setStatus("mandatory")


class _AppnNnTgSecurity_Type(Integer32):
    """Custom type appnNnTgSecurity based on Integer32"""
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


_AppnNnTgSecurity_Type.__name__ = "Integer32"
_AppnNnTgSecurity_Object = MibTableColumn
appnNnTgSecurity = _AppnNnTgSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 12, 12, 1, 4),
    _AppnNnTgSecurity_Type()
)
appnNnTgSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgSecurity.setStatus("mandatory")


class _AppnNnTgPropagationDelay_Type(Integer32):
    """Custom type appnNnTgPropagationDelay based on Integer32"""
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


_AppnNnTgPropagationDelay_Type.__name__ = "Integer32"
_AppnNnTgPropagationDelay_Object = MibTableColumn
appnNnTgPropagationDelay = _AppnNnTgPropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 12, 12, 1, 5),
    _AppnNnTgPropagationDelay_Type()
)
appnNnTgPropagationDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgPropagationDelay.setStatus("mandatory")


class _AppnNnTgUserDefinedParm1_Type(Unsigned32):
    """Custom type appnNnTgUserDefinedParm1 based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnNnTgUserDefinedParm1_Type.__name__ = "Unsigned32"
_AppnNnTgUserDefinedParm1_Object = MibTableColumn
appnNnTgUserDefinedParm1 = _AppnNnTgUserDefinedParm1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 12, 12, 1, 7),
    _AppnNnTgUserDefinedParm1_Type()
)
appnNnTgUserDefinedParm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgUserDefinedParm1.setStatus("mandatory")


class _AppnNnTgUserDefinedParm2_Type(Unsigned32):
    """Custom type appnNnTgUserDefinedParm2 based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnNnTgUserDefinedParm2_Type.__name__ = "Unsigned32"
_AppnNnTgUserDefinedParm2_Object = MibTableColumn
appnNnTgUserDefinedParm2 = _AppnNnTgUserDefinedParm2_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 12, 12, 1, 8),
    _AppnNnTgUserDefinedParm2_Type()
)
appnNnTgUserDefinedParm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgUserDefinedParm2.setStatus("mandatory")


class _AppnNnTgUserDefinedParm3_Type(Unsigned32):
    """Custom type appnNnTgUserDefinedParm3 based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnNnTgUserDefinedParm3_Type.__name__ = "Unsigned32"
_AppnNnTgUserDefinedParm3_Object = MibTableColumn
appnNnTgUserDefinedParm3 = _AppnNnTgUserDefinedParm3_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 12, 12, 1, 9),
    _AppnNnTgUserDefinedParm3_Type()
)
appnNnTgUserDefinedParm3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgUserDefinedParm3.setStatus("mandatory")
_AppnRtp_ObjectIdentity = ObjectIdentity
appnRtp = _AppnRtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13)
)
_AppnRtpRowStatusTable_Object = MibTable
appnRtpRowStatusTable = _AppnRtpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 1)
)
if mibBuilder.loadTexts:
    appnRtpRowStatusTable.setStatus("mandatory")
_AppnRtpRowStatusEntry_Object = MibTableRow
appnRtpRowStatusEntry = _AppnRtpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 1, 1)
)
appnRtpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnRtpIndex"),
)
if mibBuilder.loadTexts:
    appnRtpRowStatusEntry.setStatus("mandatory")
_AppnRtpRowStatus_Type = RowStatus
_AppnRtpRowStatus_Object = MibTableColumn
appnRtpRowStatus = _AppnRtpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 1, 1, 1),
    _AppnRtpRowStatus_Type()
)
appnRtpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpRowStatus.setStatus("mandatory")
_AppnRtpComponentName_Type = DisplayString
_AppnRtpComponentName_Object = MibTableColumn
appnRtpComponentName = _AppnRtpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 1, 1, 2),
    _AppnRtpComponentName_Type()
)
appnRtpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpComponentName.setStatus("mandatory")
_AppnRtpStorageType_Type = StorageType
_AppnRtpStorageType_Object = MibTableColumn
appnRtpStorageType = _AppnRtpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 1, 1, 4),
    _AppnRtpStorageType_Type()
)
appnRtpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpStorageType.setStatus("mandatory")


class _AppnRtpIndex_Type(AsciiStringIndex):
    """Custom type appnRtpIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppnRtpIndex_Type.__name__ = "AsciiStringIndex"
_AppnRtpIndex_Object = MibTableColumn
appnRtpIndex = _AppnRtpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 1, 1, 10),
    _AppnRtpIndex_Type()
)
appnRtpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnRtpIndex.setStatus("mandatory")
_AppnRtpOperTable_Object = MibTable
appnRtpOperTable = _AppnRtpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 10)
)
if mibBuilder.loadTexts:
    appnRtpOperTable.setStatus("mandatory")
_AppnRtpOperEntry_Object = MibTableRow
appnRtpOperEntry = _AppnRtpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 10, 1)
)
appnRtpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnRtpIndex"),
)
if mibBuilder.loadTexts:
    appnRtpOperEntry.setStatus("mandatory")


class _AppnRtpLocalLsName_Type(AsciiString):
    """Custom type appnRtpLocalLsName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppnRtpLocalLsName_Type.__name__ = "AsciiString"
_AppnRtpLocalLsName_Object = MibTableColumn
appnRtpLocalLsName = _AppnRtpLocalLsName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 10, 1, 1),
    _AppnRtpLocalLsName_Type()
)
appnRtpLocalLsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpLocalLsName.setStatus("mandatory")


class _AppnRtpRemoteCpName_Type(AsciiString):
    """Custom type appnRtpRemoteCpName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppnRtpRemoteCpName_Type.__name__ = "AsciiString"
_AppnRtpRemoteCpName_Object = MibTableColumn
appnRtpRemoteCpName = _AppnRtpRemoteCpName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 10, 1, 2),
    _AppnRtpRemoteCpName_Type()
)
appnRtpRemoteCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpRemoteCpName.setStatus("mandatory")


class _AppnRtpCosName_Type(AsciiString):
    """Custom type appnRtpCosName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppnRtpCosName_Type.__name__ = "AsciiString"
_AppnRtpCosName_Object = MibTableColumn
appnRtpCosName = _AppnRtpCosName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 10, 1, 3),
    _AppnRtpCosName_Type()
)
appnRtpCosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpCosName.setStatus("mandatory")


class _AppnRtpActiveSessions_Type(Integer32):
    """Custom type appnRtpActiveSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AppnRtpActiveSessions_Type.__name__ = "Integer32"
_AppnRtpActiveSessions_Object = MibTableColumn
appnRtpActiveSessions = _AppnRtpActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 10, 1, 4),
    _AppnRtpActiveSessions_Type()
)
appnRtpActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpActiveSessions.setStatus("mandatory")


class _AppnRtpLocalTcid_Type(HexString):
    """Custom type appnRtpLocalTcid based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_AppnRtpLocalTcid_Type.__name__ = "HexString"
_AppnRtpLocalTcid_Object = MibTableColumn
appnRtpLocalTcid = _AppnRtpLocalTcid_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 10, 1, 5),
    _AppnRtpLocalTcid_Type()
)
appnRtpLocalTcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpLocalTcid.setStatus("mandatory")


class _AppnRtpRemoteTcid_Type(HexString):
    """Custom type appnRtpRemoteTcid based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_AppnRtpRemoteTcid_Type.__name__ = "HexString"
_AppnRtpRemoteTcid_Object = MibTableColumn
appnRtpRemoteTcid = _AppnRtpRemoteTcid_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 10, 1, 6),
    _AppnRtpRemoteTcid_Type()
)
appnRtpRemoteTcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpRemoteTcid.setStatus("mandatory")


class _AppnRtpIdleTimer_Type(Unsigned32):
    """Custom type appnRtpIdleTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AppnRtpIdleTimer_Type.__name__ = "Unsigned32"
_AppnRtpIdleTimer_Object = MibTableColumn
appnRtpIdleTimer = _AppnRtpIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 10, 1, 7),
    _AppnRtpIdleTimer_Type()
)
appnRtpIdleTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpIdleTimer.setStatus("mandatory")


class _AppnRtpMaxBtuSize_Type(Integer32):
    """Custom type appnRtpMaxBtuSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AppnRtpMaxBtuSize_Type.__name__ = "Integer32"
_AppnRtpMaxBtuSize_Object = MibTableColumn
appnRtpMaxBtuSize = _AppnRtpMaxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 10, 1, 8),
    _AppnRtpMaxBtuSize_Type()
)
appnRtpMaxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpMaxBtuSize.setStatus("mandatory")
_AppnRtpStatsTable_Object = MibTable
appnRtpStatsTable = _AppnRtpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 11)
)
if mibBuilder.loadTexts:
    appnRtpStatsTable.setStatus("mandatory")
_AppnRtpStatsEntry_Object = MibTableRow
appnRtpStatsEntry = _AppnRtpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 11, 1)
)
appnRtpStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnRtpIndex"),
)
if mibBuilder.loadTexts:
    appnRtpStatsEntry.setStatus("mandatory")
_AppnRtpTxBytes_Type = PassportCounter64
_AppnRtpTxBytes_Object = MibTableColumn
appnRtpTxBytes = _AppnRtpTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 11, 1, 1),
    _AppnRtpTxBytes_Type()
)
appnRtpTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpTxBytes.setStatus("mandatory")
_AppnRtpRxBytes_Type = PassportCounter64
_AppnRtpRxBytes_Object = MibTableColumn
appnRtpRxBytes = _AppnRtpRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 11, 1, 2),
    _AppnRtpRxBytes_Type()
)
appnRtpRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpRxBytes.setStatus("mandatory")
_AppnRtpBytesResent_Type = PassportCounter64
_AppnRtpBytesResent_Object = MibTableColumn
appnRtpBytesResent = _AppnRtpBytesResent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 11, 1, 3),
    _AppnRtpBytesResent_Type()
)
appnRtpBytesResent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpBytesResent.setStatus("mandatory")
_AppnRtpBytesDiscarded_Type = PassportCounter64
_AppnRtpBytesDiscarded_Object = MibTableColumn
appnRtpBytesDiscarded = _AppnRtpBytesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 11, 1, 4),
    _AppnRtpBytesDiscarded_Type()
)
appnRtpBytesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpBytesDiscarded.setStatus("mandatory")
_AppnRtpPktTx_Type = PassportCounter64
_AppnRtpPktTx_Object = MibTableColumn
appnRtpPktTx = _AppnRtpPktTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 11, 1, 5),
    _AppnRtpPktTx_Type()
)
appnRtpPktTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpPktTx.setStatus("mandatory")
_AppnRtpPktRx_Type = PassportCounter64
_AppnRtpPktRx_Object = MibTableColumn
appnRtpPktRx = _AppnRtpPktRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 11, 1, 6),
    _AppnRtpPktRx_Type()
)
appnRtpPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpPktRx.setStatus("mandatory")
_AppnRtpPktResent_Type = PassportCounter64
_AppnRtpPktResent_Object = MibTableColumn
appnRtpPktResent = _AppnRtpPktResent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 11, 1, 7),
    _AppnRtpPktResent_Type()
)
appnRtpPktResent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpPktResent.setStatus("mandatory")
_AppnRtpPktDiscard_Type = PassportCounter64
_AppnRtpPktDiscard_Object = MibTableColumn
appnRtpPktDiscard = _AppnRtpPktDiscard_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 11, 1, 8),
    _AppnRtpPktDiscard_Type()
)
appnRtpPktDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpPktDiscard.setStatus("mandatory")
_AppnRtpLostFrames_Type = PassportCounter64
_AppnRtpLostFrames_Object = MibTableColumn
appnRtpLostFrames = _AppnRtpLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 11, 1, 9),
    _AppnRtpLostFrames_Type()
)
appnRtpLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpLostFrames.setStatus("mandatory")


class _AppnRtpCurTxRate_Type(Gauge32):
    """Custom type appnRtpCurTxRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AppnRtpCurTxRate_Type.__name__ = "Gauge32"
_AppnRtpCurTxRate_Object = MibTableColumn
appnRtpCurTxRate = _AppnRtpCurTxRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 11, 1, 10),
    _AppnRtpCurTxRate_Type()
)
appnRtpCurTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpCurTxRate.setStatus("mandatory")


class _AppnRtpMaxTxRate_Type(Gauge32):
    """Custom type appnRtpMaxTxRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AppnRtpMaxTxRate_Type.__name__ = "Gauge32"
_AppnRtpMaxTxRate_Object = MibTableColumn
appnRtpMaxTxRate = _AppnRtpMaxTxRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 11, 1, 11),
    _AppnRtpMaxTxRate_Type()
)
appnRtpMaxTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpMaxTxRate.setStatus("mandatory")


class _AppnRtpMinTxRate_Type(Gauge32):
    """Custom type appnRtpMinTxRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AppnRtpMinTxRate_Type.__name__ = "Gauge32"
_AppnRtpMinTxRate_Object = MibTableColumn
appnRtpMinTxRate = _AppnRtpMinTxRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 11, 1, 12),
    _AppnRtpMinTxRate_Type()
)
appnRtpMinTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpMinTxRate.setStatus("mandatory")


class _AppnRtpCurRxRate_Type(Gauge32):
    """Custom type appnRtpCurRxRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AppnRtpCurRxRate_Type.__name__ = "Gauge32"
_AppnRtpCurRxRate_Object = MibTableColumn
appnRtpCurRxRate = _AppnRtpCurRxRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 11, 1, 13),
    _AppnRtpCurRxRate_Type()
)
appnRtpCurRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpCurRxRate.setStatus("mandatory")


class _AppnRtpMaxRxRate_Type(Gauge32):
    """Custom type appnRtpMaxRxRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AppnRtpMaxRxRate_Type.__name__ = "Gauge32"
_AppnRtpMaxRxRate_Object = MibTableColumn
appnRtpMaxRxRate = _AppnRtpMaxRxRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 11, 1, 14),
    _AppnRtpMaxRxRate_Type()
)
appnRtpMaxRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpMaxRxRate.setStatus("mandatory")


class _AppnRtpMinRxRate_Type(Gauge32):
    """Custom type appnRtpMinRxRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AppnRtpMinRxRate_Type.__name__ = "Gauge32"
_AppnRtpMinRxRate_Object = MibTableColumn
appnRtpMinRxRate = _AppnRtpMinRxRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 11, 1, 15),
    _AppnRtpMinRxRate_Type()
)
appnRtpMinRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpMinRxRate.setStatus("mandatory")


class _AppnRtpBurstSize_Type(Gauge32):
    """Custom type appnRtpBurstSize based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AppnRtpBurstSize_Type.__name__ = "Gauge32"
_AppnRtpBurstSize_Object = MibTableColumn
appnRtpBurstSize = _AppnRtpBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 11, 1, 16),
    _AppnRtpBurstSize_Type()
)
appnRtpBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpBurstSize.setStatus("mandatory")
_AppnRtpUptime_Type = TimeTicks
_AppnRtpUptime_Object = MibTableColumn
appnRtpUptime = _AppnRtpUptime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 11, 1, 17),
    _AppnRtpUptime_Type()
)
appnRtpUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpUptime.setStatus("mandatory")


class _AppnRtpSmoothRoundTripTime_Type(Gauge32):
    """Custom type appnRtpSmoothRoundTripTime based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AppnRtpSmoothRoundTripTime_Type.__name__ = "Gauge32"
_AppnRtpSmoothRoundTripTime_Object = MibTableColumn
appnRtpSmoothRoundTripTime = _AppnRtpSmoothRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 11, 1, 18),
    _AppnRtpSmoothRoundTripTime_Type()
)
appnRtpSmoothRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpSmoothRoundTripTime.setStatus("mandatory")


class _AppnRtpLastRoundTripTime_Type(Gauge32):
    """Custom type appnRtpLastRoundTripTime based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AppnRtpLastRoundTripTime_Type.__name__ = "Gauge32"
_AppnRtpLastRoundTripTime_Object = MibTableColumn
appnRtpLastRoundTripTime = _AppnRtpLastRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 11, 1, 19),
    _AppnRtpLastRoundTripTime_Type()
)
appnRtpLastRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpLastRoundTripTime.setStatus("mandatory")


class _AppnRtpShortReqTimer_Type(Gauge32):
    """Custom type appnRtpShortReqTimer based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AppnRtpShortReqTimer_Type.__name__ = "Gauge32"
_AppnRtpShortReqTimer_Object = MibTableColumn
appnRtpShortReqTimer = _AppnRtpShortReqTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 11, 1, 20),
    _AppnRtpShortReqTimer_Type()
)
appnRtpShortReqTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpShortReqTimer.setStatus("mandatory")
_AppnRtpShortReqTimeouts_Type = PassportCounter64
_AppnRtpShortReqTimeouts_Object = MibTableColumn
appnRtpShortReqTimeouts = _AppnRtpShortReqTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 11, 1, 21),
    _AppnRtpShortReqTimeouts_Type()
)
appnRtpShortReqTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpShortReqTimeouts.setStatus("mandatory")
_AppnRtpIdleTimeouts_Type = PassportCounter64
_AppnRtpIdleTimeouts_Object = MibTableColumn
appnRtpIdleTimeouts = _AppnRtpIdleTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 11, 1, 22),
    _AppnRtpIdleTimeouts_Type()
)
appnRtpIdleTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpIdleTimeouts.setStatus("mandatory")
_AppnRtpRxInvalidSnaFrames_Type = PassportCounter64
_AppnRtpRxInvalidSnaFrames_Object = MibTableColumn
appnRtpRxInvalidSnaFrames = _AppnRtpRxInvalidSnaFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 11, 1, 23),
    _AppnRtpRxInvalidSnaFrames_Type()
)
appnRtpRxInvalidSnaFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpRxInvalidSnaFrames.setStatus("mandatory")
_AppnRtpInSessionControlFrames_Type = PassportCounter64
_AppnRtpInSessionControlFrames_Object = MibTableColumn
appnRtpInSessionControlFrames = _AppnRtpInSessionControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 11, 1, 24),
    _AppnRtpInSessionControlFrames_Type()
)
appnRtpInSessionControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpInSessionControlFrames.setStatus("mandatory")
_AppnRtpOutSessionControlFrames_Type = PassportCounter64
_AppnRtpOutSessionControlFrames_Object = MibTableColumn
appnRtpOutSessionControlFrames = _AppnRtpOutSessionControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 13, 11, 1, 25),
    _AppnRtpOutSessionControlFrames_Type()
)
appnRtpOutSessionControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnRtpOutSessionControlFrames.setStatus("mandatory")
_AppnDlu_ObjectIdentity = ObjectIdentity
appnDlu = _AppnDlu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14)
)
_AppnDluRowStatusTable_Object = MibTable
appnDluRowStatusTable = _AppnDluRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 1)
)
if mibBuilder.loadTexts:
    appnDluRowStatusTable.setStatus("mandatory")
_AppnDluRowStatusEntry_Object = MibTableRow
appnDluRowStatusEntry = _AppnDluRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 1, 1)
)
appnDluRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDluIndex"),
)
if mibBuilder.loadTexts:
    appnDluRowStatusEntry.setStatus("mandatory")
_AppnDluRowStatus_Type = RowStatus
_AppnDluRowStatus_Object = MibTableColumn
appnDluRowStatus = _AppnDluRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 1, 1, 1),
    _AppnDluRowStatus_Type()
)
appnDluRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluRowStatus.setStatus("mandatory")
_AppnDluComponentName_Type = DisplayString
_AppnDluComponentName_Object = MibTableColumn
appnDluComponentName = _AppnDluComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 1, 1, 2),
    _AppnDluComponentName_Type()
)
appnDluComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluComponentName.setStatus("mandatory")
_AppnDluStorageType_Type = StorageType
_AppnDluStorageType_Object = MibTableColumn
appnDluStorageType = _AppnDluStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 1, 1, 4),
    _AppnDluStorageType_Type()
)
appnDluStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluStorageType.setStatus("mandatory")


class _AppnDluIndex_Type(AsciiStringIndex):
    """Custom type appnDluIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppnDluIndex_Type.__name__ = "AsciiStringIndex"
_AppnDluIndex_Object = MibTableColumn
appnDluIndex = _AppnDluIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 1, 1, 10),
    _AppnDluIndex_Type()
)
appnDluIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnDluIndex.setStatus("mandatory")
_AppnDluOperTable_Object = MibTable
appnDluOperTable = _AppnDluOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 10)
)
if mibBuilder.loadTexts:
    appnDluOperTable.setStatus("mandatory")
_AppnDluOperEntry_Object = MibTableRow
appnDluOperEntry = _AppnDluOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 10, 1)
)
appnDluOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDluIndex"),
)
if mibBuilder.loadTexts:
    appnDluOperEntry.setStatus("mandatory")


class _AppnDluSscpSessActive_Type(Integer32):
    """Custom type appnDluSscpSessActive based on Integer32"""
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


_AppnDluSscpSessActive_Type.__name__ = "Integer32"
_AppnDluSscpSessActive_Object = MibTableColumn
appnDluSscpSessActive = _AppnDluSscpSessActive_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 10, 1, 1),
    _AppnDluSscpSessActive_Type()
)
appnDluSscpSessActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluSscpSessActive.setStatus("mandatory")


class _AppnDluPluSessActive_Type(Integer32):
    """Custom type appnDluPluSessActive based on Integer32"""
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


_AppnDluPluSessActive_Type.__name__ = "Integer32"
_AppnDluPluSessActive_Object = MibTableColumn
appnDluPluSessActive = _AppnDluPluSessActive_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 10, 1, 2),
    _AppnDluPluSessActive_Type()
)
appnDluPluSessActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluPluSessActive.setStatus("mandatory")


class _AppnDluDlusName_Type(AsciiString):
    """Custom type appnDluDlusName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_AppnDluDlusName_Type.__name__ = "AsciiString"
_AppnDluDlusName_Object = MibTableColumn
appnDluDlusName = _AppnDluDlusName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 10, 1, 3),
    _AppnDluDlusName_Type()
)
appnDluDlusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluDlusName.setStatus("mandatory")


class _AppnDluPluName_Type(AsciiString):
    """Custom type appnDluPluName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_AppnDluPluName_Type.__name__ = "AsciiString"
_AppnDluPluName_Object = MibTableColumn
appnDluPluName = _AppnDluPluName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 10, 1, 4),
    _AppnDluPluName_Type()
)
appnDluPluName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluPluName.setStatus("mandatory")


class _AppnDluNauAddress_Type(Integer32):
    """Custom type appnDluNauAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnDluNauAddress_Type.__name__ = "Integer32"
_AppnDluNauAddress_Object = MibTableColumn
appnDluNauAddress = _AppnDluNauAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 10, 1, 5),
    _AppnDluNauAddress_Type()
)
appnDluNauAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluNauAddress.setStatus("mandatory")
_AppnDluSscp_ObjectIdentity = ObjectIdentity
appnDluSscp = _AppnDluSscp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 100)
)
_AppnDluSscpRowStatusTable_Object = MibTable
appnDluSscpRowStatusTable = _AppnDluSscpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 100, 1)
)
if mibBuilder.loadTexts:
    appnDluSscpRowStatusTable.setStatus("mandatory")
_AppnDluSscpRowStatusEntry_Object = MibTableRow
appnDluSscpRowStatusEntry = _AppnDluSscpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 100, 1, 1)
)
appnDluSscpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDluIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDluSscpIndex"),
)
if mibBuilder.loadTexts:
    appnDluSscpRowStatusEntry.setStatus("mandatory")
_AppnDluSscpRowStatus_Type = RowStatus
_AppnDluSscpRowStatus_Object = MibTableColumn
appnDluSscpRowStatus = _AppnDluSscpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 100, 1, 1, 1),
    _AppnDluSscpRowStatus_Type()
)
appnDluSscpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluSscpRowStatus.setStatus("mandatory")
_AppnDluSscpComponentName_Type = DisplayString
_AppnDluSscpComponentName_Object = MibTableColumn
appnDluSscpComponentName = _AppnDluSscpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 100, 1, 1, 2),
    _AppnDluSscpComponentName_Type()
)
appnDluSscpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluSscpComponentName.setStatus("mandatory")
_AppnDluSscpStorageType_Type = StorageType
_AppnDluSscpStorageType_Object = MibTableColumn
appnDluSscpStorageType = _AppnDluSscpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 100, 1, 1, 4),
    _AppnDluSscpStorageType_Type()
)
appnDluSscpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluSscpStorageType.setStatus("mandatory")
_AppnDluSscpIndex_Type = NonReplicated
_AppnDluSscpIndex_Object = MibTableColumn
appnDluSscpIndex = _AppnDluSscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 100, 1, 1, 10),
    _AppnDluSscpIndex_Type()
)
appnDluSscpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnDluSscpIndex.setStatus("mandatory")
_AppnDluSscpStatsTable_Object = MibTable
appnDluSscpStatsTable = _AppnDluSscpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 100, 10)
)
if mibBuilder.loadTexts:
    appnDluSscpStatsTable.setStatus("mandatory")
_AppnDluSscpStatsEntry_Object = MibTableRow
appnDluSscpStatsEntry = _AppnDluSscpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 100, 10, 1)
)
appnDluSscpStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDluIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDluSscpIndex"),
)
if mibBuilder.loadTexts:
    appnDluSscpStatsEntry.setStatus("mandatory")


class _AppnDluSscpRxRuSize_Type(Unsigned32):
    """Custom type appnDluSscpRxRuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnDluSscpRxRuSize_Type.__name__ = "Unsigned32"
_AppnDluSscpRxRuSize_Object = MibTableColumn
appnDluSscpRxRuSize = _AppnDluSscpRxRuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 100, 10, 1, 1),
    _AppnDluSscpRxRuSize_Type()
)
appnDluSscpRxRuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluSscpRxRuSize.setStatus("mandatory")


class _AppnDluSscpMaxTxBtuSize_Type(Unsigned32):
    """Custom type appnDluSscpMaxTxBtuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnDluSscpMaxTxBtuSize_Type.__name__ = "Unsigned32"
_AppnDluSscpMaxTxBtuSize_Object = MibTableColumn
appnDluSscpMaxTxBtuSize = _AppnDluSscpMaxTxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 100, 10, 1, 2),
    _AppnDluSscpMaxTxBtuSize_Type()
)
appnDluSscpMaxTxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluSscpMaxTxBtuSize.setStatus("mandatory")


class _AppnDluSscpMaxRxBtuSize_Type(Unsigned32):
    """Custom type appnDluSscpMaxRxBtuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnDluSscpMaxRxBtuSize_Type.__name__ = "Unsigned32"
_AppnDluSscpMaxRxBtuSize_Object = MibTableColumn
appnDluSscpMaxRxBtuSize = _AppnDluSscpMaxRxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 100, 10, 1, 3),
    _AppnDluSscpMaxRxBtuSize_Type()
)
appnDluSscpMaxRxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluSscpMaxRxBtuSize.setStatus("mandatory")


class _AppnDluSscpMaxTxPacWin_Type(Integer32):
    """Custom type appnDluSscpMaxTxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AppnDluSscpMaxTxPacWin_Type.__name__ = "Integer32"
_AppnDluSscpMaxTxPacWin_Object = MibTableColumn
appnDluSscpMaxTxPacWin = _AppnDluSscpMaxTxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 100, 10, 1, 4),
    _AppnDluSscpMaxTxPacWin_Type()
)
appnDluSscpMaxTxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluSscpMaxTxPacWin.setStatus("mandatory")


class _AppnDluSscpCurTxPacWin_Type(Integer32):
    """Custom type appnDluSscpCurTxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AppnDluSscpCurTxPacWin_Type.__name__ = "Integer32"
_AppnDluSscpCurTxPacWin_Object = MibTableColumn
appnDluSscpCurTxPacWin = _AppnDluSscpCurTxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 100, 10, 1, 5),
    _AppnDluSscpCurTxPacWin_Type()
)
appnDluSscpCurTxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluSscpCurTxPacWin.setStatus("mandatory")


class _AppnDluSscpMaxRxPacWin_Type(Integer32):
    """Custom type appnDluSscpMaxRxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AppnDluSscpMaxRxPacWin_Type.__name__ = "Integer32"
_AppnDluSscpMaxRxPacWin_Object = MibTableColumn
appnDluSscpMaxRxPacWin = _AppnDluSscpMaxRxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 100, 10, 1, 6),
    _AppnDluSscpMaxRxPacWin_Type()
)
appnDluSscpMaxRxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluSscpMaxRxPacWin.setStatus("mandatory")


class _AppnDluSscpCurRxPacWin_Type(Integer32):
    """Custom type appnDluSscpCurRxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AppnDluSscpCurRxPacWin_Type.__name__ = "Integer32"
_AppnDluSscpCurRxPacWin_Object = MibTableColumn
appnDluSscpCurRxPacWin = _AppnDluSscpCurRxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 100, 10, 1, 7),
    _AppnDluSscpCurRxPacWin_Type()
)
appnDluSscpCurRxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluSscpCurRxPacWin.setStatus("mandatory")
_AppnDluSscpTxDataframes_Type = PassportCounter64
_AppnDluSscpTxDataframes_Object = MibTableColumn
appnDluSscpTxDataframes = _AppnDluSscpTxDataframes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 100, 10, 1, 8),
    _AppnDluSscpTxDataframes_Type()
)
appnDluSscpTxDataframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluSscpTxDataframes.setStatus("mandatory")
_AppnDluSscpTxFmdFrames_Type = PassportCounter64
_AppnDluSscpTxFmdFrames_Object = MibTableColumn
appnDluSscpTxFmdFrames = _AppnDluSscpTxFmdFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 100, 10, 1, 9),
    _AppnDluSscpTxFmdFrames_Type()
)
appnDluSscpTxFmdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluSscpTxFmdFrames.setStatus("mandatory")
_AppnDluSscpTxDataBytes_Type = PassportCounter64
_AppnDluSscpTxDataBytes_Object = MibTableColumn
appnDluSscpTxDataBytes = _AppnDluSscpTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 100, 10, 1, 10),
    _AppnDluSscpTxDataBytes_Type()
)
appnDluSscpTxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluSscpTxDataBytes.setStatus("mandatory")
_AppnDluSscpRxDataFrames_Type = PassportCounter64
_AppnDluSscpRxDataFrames_Object = MibTableColumn
appnDluSscpRxDataFrames = _AppnDluSscpRxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 100, 10, 1, 11),
    _AppnDluSscpRxDataFrames_Type()
)
appnDluSscpRxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluSscpRxDataFrames.setStatus("mandatory")
_AppnDluSscpRxFmdFrames_Type = PassportCounter64
_AppnDluSscpRxFmdFrames_Object = MibTableColumn
appnDluSscpRxFmdFrames = _AppnDluSscpRxFmdFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 100, 10, 1, 12),
    _AppnDluSscpRxFmdFrames_Type()
)
appnDluSscpRxFmdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluSscpRxFmdFrames.setStatus("mandatory")
_AppnDluSscpRxDataBytes_Type = PassportCounter64
_AppnDluSscpRxDataBytes_Object = MibTableColumn
appnDluSscpRxDataBytes = _AppnDluSscpRxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 100, 10, 1, 13),
    _AppnDluSscpRxDataBytes_Type()
)
appnDluSscpRxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluSscpRxDataBytes.setStatus("mandatory")


class _AppnDluSscpSidh_Type(Hex):
    """Custom type appnDluSscpSidh based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnDluSscpSidh_Type.__name__ = "Hex"
_AppnDluSscpSidh_Object = MibTableColumn
appnDluSscpSidh = _AppnDluSscpSidh_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 100, 10, 1, 14),
    _AppnDluSscpSidh_Type()
)
appnDluSscpSidh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluSscpSidh.setStatus("mandatory")


class _AppnDluSscpSidl_Type(Hex):
    """Custom type appnDluSscpSidl based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnDluSscpSidl_Type.__name__ = "Hex"
_AppnDluSscpSidl_Object = MibTableColumn
appnDluSscpSidl = _AppnDluSscpSidl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 100, 10, 1, 15),
    _AppnDluSscpSidl_Type()
)
appnDluSscpSidl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluSscpSidl.setStatus("mandatory")


class _AppnDluSscpOdai_Type(Integer32):
    """Custom type appnDluSscpOdai based on Integer32"""
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


_AppnDluSscpOdai_Type.__name__ = "Integer32"
_AppnDluSscpOdai_Object = MibTableColumn
appnDluSscpOdai = _AppnDluSscpOdai_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 100, 10, 1, 16),
    _AppnDluSscpOdai_Type()
)
appnDluSscpOdai.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluSscpOdai.setStatus("mandatory")


class _AppnDluSscpLsName_Type(AsciiString):
    """Custom type appnDluSscpLsName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppnDluSscpLsName_Type.__name__ = "AsciiString"
_AppnDluSscpLsName_Object = MibTableColumn
appnDluSscpLsName = _AppnDluSscpLsName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 100, 10, 1, 17),
    _AppnDluSscpLsName_Type()
)
appnDluSscpLsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluSscpLsName.setStatus("mandatory")
_AppnDluUsStat_ObjectIdentity = ObjectIdentity
appnDluUsStat = _AppnDluUsStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 101)
)
_AppnDluUsStatRowStatusTable_Object = MibTable
appnDluUsStatRowStatusTable = _AppnDluUsStatRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 101, 1)
)
if mibBuilder.loadTexts:
    appnDluUsStatRowStatusTable.setStatus("mandatory")
_AppnDluUsStatRowStatusEntry_Object = MibTableRow
appnDluUsStatRowStatusEntry = _AppnDluUsStatRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 101, 1, 1)
)
appnDluUsStatRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDluIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDluUsStatIndex"),
)
if mibBuilder.loadTexts:
    appnDluUsStatRowStatusEntry.setStatus("mandatory")
_AppnDluUsStatRowStatus_Type = RowStatus
_AppnDluUsStatRowStatus_Object = MibTableColumn
appnDluUsStatRowStatus = _AppnDluUsStatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 101, 1, 1, 1),
    _AppnDluUsStatRowStatus_Type()
)
appnDluUsStatRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluUsStatRowStatus.setStatus("mandatory")
_AppnDluUsStatComponentName_Type = DisplayString
_AppnDluUsStatComponentName_Object = MibTableColumn
appnDluUsStatComponentName = _AppnDluUsStatComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 101, 1, 1, 2),
    _AppnDluUsStatComponentName_Type()
)
appnDluUsStatComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluUsStatComponentName.setStatus("mandatory")
_AppnDluUsStatStorageType_Type = StorageType
_AppnDluUsStatStorageType_Object = MibTableColumn
appnDluUsStatStorageType = _AppnDluUsStatStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 101, 1, 1, 4),
    _AppnDluUsStatStorageType_Type()
)
appnDluUsStatStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluUsStatStorageType.setStatus("mandatory")
_AppnDluUsStatIndex_Type = NonReplicated
_AppnDluUsStatIndex_Object = MibTableColumn
appnDluUsStatIndex = _AppnDluUsStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 101, 1, 1, 10),
    _AppnDluUsStatIndex_Type()
)
appnDluUsStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnDluUsStatIndex.setStatus("mandatory")
_AppnDluUsStatStatsTable_Object = MibTable
appnDluUsStatStatsTable = _AppnDluUsStatStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 101, 10)
)
if mibBuilder.loadTexts:
    appnDluUsStatStatsTable.setStatus("mandatory")
_AppnDluUsStatStatsEntry_Object = MibTableRow
appnDluUsStatStatsEntry = _AppnDluUsStatStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 101, 10, 1)
)
appnDluUsStatStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDluIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDluUsStatIndex"),
)
if mibBuilder.loadTexts:
    appnDluUsStatStatsEntry.setStatus("mandatory")


class _AppnDluUsStatRxRuSize_Type(Unsigned32):
    """Custom type appnDluUsStatRxRuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnDluUsStatRxRuSize_Type.__name__ = "Unsigned32"
_AppnDluUsStatRxRuSize_Object = MibTableColumn
appnDluUsStatRxRuSize = _AppnDluUsStatRxRuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 101, 10, 1, 1),
    _AppnDluUsStatRxRuSize_Type()
)
appnDluUsStatRxRuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluUsStatRxRuSize.setStatus("mandatory")


class _AppnDluUsStatMaxTxBtuSize_Type(Unsigned32):
    """Custom type appnDluUsStatMaxTxBtuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnDluUsStatMaxTxBtuSize_Type.__name__ = "Unsigned32"
_AppnDluUsStatMaxTxBtuSize_Object = MibTableColumn
appnDluUsStatMaxTxBtuSize = _AppnDluUsStatMaxTxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 101, 10, 1, 2),
    _AppnDluUsStatMaxTxBtuSize_Type()
)
appnDluUsStatMaxTxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluUsStatMaxTxBtuSize.setStatus("mandatory")


class _AppnDluUsStatMaxRxBtuSize_Type(Unsigned32):
    """Custom type appnDluUsStatMaxRxBtuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnDluUsStatMaxRxBtuSize_Type.__name__ = "Unsigned32"
_AppnDluUsStatMaxRxBtuSize_Object = MibTableColumn
appnDluUsStatMaxRxBtuSize = _AppnDluUsStatMaxRxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 101, 10, 1, 3),
    _AppnDluUsStatMaxRxBtuSize_Type()
)
appnDluUsStatMaxRxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluUsStatMaxRxBtuSize.setStatus("mandatory")


class _AppnDluUsStatMaxTxPacWin_Type(Integer32):
    """Custom type appnDluUsStatMaxTxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AppnDluUsStatMaxTxPacWin_Type.__name__ = "Integer32"
_AppnDluUsStatMaxTxPacWin_Object = MibTableColumn
appnDluUsStatMaxTxPacWin = _AppnDluUsStatMaxTxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 101, 10, 1, 4),
    _AppnDluUsStatMaxTxPacWin_Type()
)
appnDluUsStatMaxTxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluUsStatMaxTxPacWin.setStatus("mandatory")


class _AppnDluUsStatCurTxPacWin_Type(Integer32):
    """Custom type appnDluUsStatCurTxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AppnDluUsStatCurTxPacWin_Type.__name__ = "Integer32"
_AppnDluUsStatCurTxPacWin_Object = MibTableColumn
appnDluUsStatCurTxPacWin = _AppnDluUsStatCurTxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 101, 10, 1, 5),
    _AppnDluUsStatCurTxPacWin_Type()
)
appnDluUsStatCurTxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluUsStatCurTxPacWin.setStatus("mandatory")


class _AppnDluUsStatMaxRxPacWin_Type(Integer32):
    """Custom type appnDluUsStatMaxRxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AppnDluUsStatMaxRxPacWin_Type.__name__ = "Integer32"
_AppnDluUsStatMaxRxPacWin_Object = MibTableColumn
appnDluUsStatMaxRxPacWin = _AppnDluUsStatMaxRxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 101, 10, 1, 6),
    _AppnDluUsStatMaxRxPacWin_Type()
)
appnDluUsStatMaxRxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluUsStatMaxRxPacWin.setStatus("mandatory")


class _AppnDluUsStatCurRxPacWin_Type(Integer32):
    """Custom type appnDluUsStatCurRxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AppnDluUsStatCurRxPacWin_Type.__name__ = "Integer32"
_AppnDluUsStatCurRxPacWin_Object = MibTableColumn
appnDluUsStatCurRxPacWin = _AppnDluUsStatCurRxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 101, 10, 1, 7),
    _AppnDluUsStatCurRxPacWin_Type()
)
appnDluUsStatCurRxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluUsStatCurRxPacWin.setStatus("mandatory")
_AppnDluUsStatTxDataframes_Type = PassportCounter64
_AppnDluUsStatTxDataframes_Object = MibTableColumn
appnDluUsStatTxDataframes = _AppnDluUsStatTxDataframes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 101, 10, 1, 8),
    _AppnDluUsStatTxDataframes_Type()
)
appnDluUsStatTxDataframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluUsStatTxDataframes.setStatus("mandatory")
_AppnDluUsStatTxFmdFrames_Type = PassportCounter64
_AppnDluUsStatTxFmdFrames_Object = MibTableColumn
appnDluUsStatTxFmdFrames = _AppnDluUsStatTxFmdFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 101, 10, 1, 9),
    _AppnDluUsStatTxFmdFrames_Type()
)
appnDluUsStatTxFmdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluUsStatTxFmdFrames.setStatus("mandatory")
_AppnDluUsStatTxDataBytes_Type = PassportCounter64
_AppnDluUsStatTxDataBytes_Object = MibTableColumn
appnDluUsStatTxDataBytes = _AppnDluUsStatTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 101, 10, 1, 10),
    _AppnDluUsStatTxDataBytes_Type()
)
appnDluUsStatTxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluUsStatTxDataBytes.setStatus("mandatory")
_AppnDluUsStatRxDataFrames_Type = PassportCounter64
_AppnDluUsStatRxDataFrames_Object = MibTableColumn
appnDluUsStatRxDataFrames = _AppnDluUsStatRxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 101, 10, 1, 11),
    _AppnDluUsStatRxDataFrames_Type()
)
appnDluUsStatRxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluUsStatRxDataFrames.setStatus("mandatory")
_AppnDluUsStatRxFmdFrames_Type = PassportCounter64
_AppnDluUsStatRxFmdFrames_Object = MibTableColumn
appnDluUsStatRxFmdFrames = _AppnDluUsStatRxFmdFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 101, 10, 1, 12),
    _AppnDluUsStatRxFmdFrames_Type()
)
appnDluUsStatRxFmdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluUsStatRxFmdFrames.setStatus("mandatory")
_AppnDluUsStatRxDataBytes_Type = PassportCounter64
_AppnDluUsStatRxDataBytes_Object = MibTableColumn
appnDluUsStatRxDataBytes = _AppnDluUsStatRxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 101, 10, 1, 13),
    _AppnDluUsStatRxDataBytes_Type()
)
appnDluUsStatRxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluUsStatRxDataBytes.setStatus("mandatory")


class _AppnDluUsStatSidh_Type(Hex):
    """Custom type appnDluUsStatSidh based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnDluUsStatSidh_Type.__name__ = "Hex"
_AppnDluUsStatSidh_Object = MibTableColumn
appnDluUsStatSidh = _AppnDluUsStatSidh_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 101, 10, 1, 14),
    _AppnDluUsStatSidh_Type()
)
appnDluUsStatSidh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluUsStatSidh.setStatus("mandatory")


class _AppnDluUsStatSidl_Type(Hex):
    """Custom type appnDluUsStatSidl based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnDluUsStatSidl_Type.__name__ = "Hex"
_AppnDluUsStatSidl_Object = MibTableColumn
appnDluUsStatSidl = _AppnDluUsStatSidl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 101, 10, 1, 15),
    _AppnDluUsStatSidl_Type()
)
appnDluUsStatSidl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluUsStatSidl.setStatus("mandatory")


class _AppnDluUsStatOdai_Type(Integer32):
    """Custom type appnDluUsStatOdai based on Integer32"""
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


_AppnDluUsStatOdai_Type.__name__ = "Integer32"
_AppnDluUsStatOdai_Object = MibTableColumn
appnDluUsStatOdai = _AppnDluUsStatOdai_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 101, 10, 1, 16),
    _AppnDluUsStatOdai_Type()
)
appnDluUsStatOdai.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluUsStatOdai.setStatus("mandatory")


class _AppnDluUsStatLsName_Type(AsciiString):
    """Custom type appnDluUsStatLsName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppnDluUsStatLsName_Type.__name__ = "AsciiString"
_AppnDluUsStatLsName_Object = MibTableColumn
appnDluUsStatLsName = _AppnDluUsStatLsName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 101, 10, 1, 17),
    _AppnDluUsStatLsName_Type()
)
appnDluUsStatLsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluUsStatLsName.setStatus("mandatory")
_AppnDluDsStat_ObjectIdentity = ObjectIdentity
appnDluDsStat = _AppnDluDsStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 102)
)
_AppnDluDsStatRowStatusTable_Object = MibTable
appnDluDsStatRowStatusTable = _AppnDluDsStatRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 102, 1)
)
if mibBuilder.loadTexts:
    appnDluDsStatRowStatusTable.setStatus("mandatory")
_AppnDluDsStatRowStatusEntry_Object = MibTableRow
appnDluDsStatRowStatusEntry = _AppnDluDsStatRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 102, 1, 1)
)
appnDluDsStatRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDluIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDluDsStatIndex"),
)
if mibBuilder.loadTexts:
    appnDluDsStatRowStatusEntry.setStatus("mandatory")
_AppnDluDsStatRowStatus_Type = RowStatus
_AppnDluDsStatRowStatus_Object = MibTableColumn
appnDluDsStatRowStatus = _AppnDluDsStatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 102, 1, 1, 1),
    _AppnDluDsStatRowStatus_Type()
)
appnDluDsStatRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluDsStatRowStatus.setStatus("mandatory")
_AppnDluDsStatComponentName_Type = DisplayString
_AppnDluDsStatComponentName_Object = MibTableColumn
appnDluDsStatComponentName = _AppnDluDsStatComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 102, 1, 1, 2),
    _AppnDluDsStatComponentName_Type()
)
appnDluDsStatComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluDsStatComponentName.setStatus("mandatory")
_AppnDluDsStatStorageType_Type = StorageType
_AppnDluDsStatStorageType_Object = MibTableColumn
appnDluDsStatStorageType = _AppnDluDsStatStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 102, 1, 1, 4),
    _AppnDluDsStatStorageType_Type()
)
appnDluDsStatStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluDsStatStorageType.setStatus("mandatory")
_AppnDluDsStatIndex_Type = NonReplicated
_AppnDluDsStatIndex_Object = MibTableColumn
appnDluDsStatIndex = _AppnDluDsStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 102, 1, 1, 10),
    _AppnDluDsStatIndex_Type()
)
appnDluDsStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnDluDsStatIndex.setStatus("mandatory")
_AppnDluDsStatStatsTable_Object = MibTable
appnDluDsStatStatsTable = _AppnDluDsStatStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 102, 10)
)
if mibBuilder.loadTexts:
    appnDluDsStatStatsTable.setStatus("mandatory")
_AppnDluDsStatStatsEntry_Object = MibTableRow
appnDluDsStatStatsEntry = _AppnDluDsStatStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 102, 10, 1)
)
appnDluDsStatStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDluIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDluDsStatIndex"),
)
if mibBuilder.loadTexts:
    appnDluDsStatStatsEntry.setStatus("mandatory")


class _AppnDluDsStatRxRuSize_Type(Unsigned32):
    """Custom type appnDluDsStatRxRuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnDluDsStatRxRuSize_Type.__name__ = "Unsigned32"
_AppnDluDsStatRxRuSize_Object = MibTableColumn
appnDluDsStatRxRuSize = _AppnDluDsStatRxRuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 102, 10, 1, 1),
    _AppnDluDsStatRxRuSize_Type()
)
appnDluDsStatRxRuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluDsStatRxRuSize.setStatus("mandatory")


class _AppnDluDsStatMaxTxBtuSize_Type(Unsigned32):
    """Custom type appnDluDsStatMaxTxBtuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnDluDsStatMaxTxBtuSize_Type.__name__ = "Unsigned32"
_AppnDluDsStatMaxTxBtuSize_Object = MibTableColumn
appnDluDsStatMaxTxBtuSize = _AppnDluDsStatMaxTxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 102, 10, 1, 2),
    _AppnDluDsStatMaxTxBtuSize_Type()
)
appnDluDsStatMaxTxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluDsStatMaxTxBtuSize.setStatus("mandatory")


class _AppnDluDsStatMaxRxBtuSize_Type(Unsigned32):
    """Custom type appnDluDsStatMaxRxBtuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnDluDsStatMaxRxBtuSize_Type.__name__ = "Unsigned32"
_AppnDluDsStatMaxRxBtuSize_Object = MibTableColumn
appnDluDsStatMaxRxBtuSize = _AppnDluDsStatMaxRxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 102, 10, 1, 3),
    _AppnDluDsStatMaxRxBtuSize_Type()
)
appnDluDsStatMaxRxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluDsStatMaxRxBtuSize.setStatus("mandatory")


class _AppnDluDsStatMaxTxPacWin_Type(Integer32):
    """Custom type appnDluDsStatMaxTxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AppnDluDsStatMaxTxPacWin_Type.__name__ = "Integer32"
_AppnDluDsStatMaxTxPacWin_Object = MibTableColumn
appnDluDsStatMaxTxPacWin = _AppnDluDsStatMaxTxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 102, 10, 1, 4),
    _AppnDluDsStatMaxTxPacWin_Type()
)
appnDluDsStatMaxTxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluDsStatMaxTxPacWin.setStatus("mandatory")


class _AppnDluDsStatCurTxPacWin_Type(Integer32):
    """Custom type appnDluDsStatCurTxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AppnDluDsStatCurTxPacWin_Type.__name__ = "Integer32"
_AppnDluDsStatCurTxPacWin_Object = MibTableColumn
appnDluDsStatCurTxPacWin = _AppnDluDsStatCurTxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 102, 10, 1, 5),
    _AppnDluDsStatCurTxPacWin_Type()
)
appnDluDsStatCurTxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluDsStatCurTxPacWin.setStatus("mandatory")


class _AppnDluDsStatMaxRxPacWin_Type(Integer32):
    """Custom type appnDluDsStatMaxRxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AppnDluDsStatMaxRxPacWin_Type.__name__ = "Integer32"
_AppnDluDsStatMaxRxPacWin_Object = MibTableColumn
appnDluDsStatMaxRxPacWin = _AppnDluDsStatMaxRxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 102, 10, 1, 6),
    _AppnDluDsStatMaxRxPacWin_Type()
)
appnDluDsStatMaxRxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluDsStatMaxRxPacWin.setStatus("mandatory")


class _AppnDluDsStatCurRxPacWin_Type(Integer32):
    """Custom type appnDluDsStatCurRxPacWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AppnDluDsStatCurRxPacWin_Type.__name__ = "Integer32"
_AppnDluDsStatCurRxPacWin_Object = MibTableColumn
appnDluDsStatCurRxPacWin = _AppnDluDsStatCurRxPacWin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 102, 10, 1, 7),
    _AppnDluDsStatCurRxPacWin_Type()
)
appnDluDsStatCurRxPacWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluDsStatCurRxPacWin.setStatus("mandatory")
_AppnDluDsStatTxDataframes_Type = PassportCounter64
_AppnDluDsStatTxDataframes_Object = MibTableColumn
appnDluDsStatTxDataframes = _AppnDluDsStatTxDataframes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 102, 10, 1, 8),
    _AppnDluDsStatTxDataframes_Type()
)
appnDluDsStatTxDataframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluDsStatTxDataframes.setStatus("mandatory")
_AppnDluDsStatTxFmdFrames_Type = PassportCounter64
_AppnDluDsStatTxFmdFrames_Object = MibTableColumn
appnDluDsStatTxFmdFrames = _AppnDluDsStatTxFmdFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 102, 10, 1, 9),
    _AppnDluDsStatTxFmdFrames_Type()
)
appnDluDsStatTxFmdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluDsStatTxFmdFrames.setStatus("mandatory")
_AppnDluDsStatTxDataBytes_Type = PassportCounter64
_AppnDluDsStatTxDataBytes_Object = MibTableColumn
appnDluDsStatTxDataBytes = _AppnDluDsStatTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 102, 10, 1, 10),
    _AppnDluDsStatTxDataBytes_Type()
)
appnDluDsStatTxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluDsStatTxDataBytes.setStatus("mandatory")
_AppnDluDsStatRxDataFrames_Type = PassportCounter64
_AppnDluDsStatRxDataFrames_Object = MibTableColumn
appnDluDsStatRxDataFrames = _AppnDluDsStatRxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 102, 10, 1, 11),
    _AppnDluDsStatRxDataFrames_Type()
)
appnDluDsStatRxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluDsStatRxDataFrames.setStatus("mandatory")
_AppnDluDsStatRxFmdFrames_Type = PassportCounter64
_AppnDluDsStatRxFmdFrames_Object = MibTableColumn
appnDluDsStatRxFmdFrames = _AppnDluDsStatRxFmdFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 102, 10, 1, 12),
    _AppnDluDsStatRxFmdFrames_Type()
)
appnDluDsStatRxFmdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluDsStatRxFmdFrames.setStatus("mandatory")
_AppnDluDsStatRxDataBytes_Type = PassportCounter64
_AppnDluDsStatRxDataBytes_Object = MibTableColumn
appnDluDsStatRxDataBytes = _AppnDluDsStatRxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 102, 10, 1, 13),
    _AppnDluDsStatRxDataBytes_Type()
)
appnDluDsStatRxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluDsStatRxDataBytes.setStatus("mandatory")


class _AppnDluDsStatSidh_Type(Hex):
    """Custom type appnDluDsStatSidh based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnDluDsStatSidh_Type.__name__ = "Hex"
_AppnDluDsStatSidh_Object = MibTableColumn
appnDluDsStatSidh = _AppnDluDsStatSidh_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 102, 10, 1, 14),
    _AppnDluDsStatSidh_Type()
)
appnDluDsStatSidh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluDsStatSidh.setStatus("mandatory")


class _AppnDluDsStatSidl_Type(Hex):
    """Custom type appnDluDsStatSidl based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnDluDsStatSidl_Type.__name__ = "Hex"
_AppnDluDsStatSidl_Object = MibTableColumn
appnDluDsStatSidl = _AppnDluDsStatSidl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 102, 10, 1, 15),
    _AppnDluDsStatSidl_Type()
)
appnDluDsStatSidl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluDsStatSidl.setStatus("mandatory")


class _AppnDluDsStatOdai_Type(Integer32):
    """Custom type appnDluDsStatOdai based on Integer32"""
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


_AppnDluDsStatOdai_Type.__name__ = "Integer32"
_AppnDluDsStatOdai_Object = MibTableColumn
appnDluDsStatOdai = _AppnDluDsStatOdai_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 102, 10, 1, 16),
    _AppnDluDsStatOdai_Type()
)
appnDluDsStatOdai.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluDsStatOdai.setStatus("mandatory")


class _AppnDluDsStatLsName_Type(AsciiString):
    """Custom type appnDluDsStatLsName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppnDluDsStatLsName_Type.__name__ = "AsciiString"
_AppnDluDsStatLsName_Object = MibTableColumn
appnDluDsStatLsName = _AppnDluDsStatLsName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 14, 102, 10, 1, 17),
    _AppnDluDsStatLsName_Type()
)
appnDluDsStatLsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDluDsStatLsName.setStatus("mandatory")
_AppnDlus_ObjectIdentity = ObjectIdentity
appnDlus = _AppnDlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 15)
)
_AppnDlusRowStatusTable_Object = MibTable
appnDlusRowStatusTable = _AppnDlusRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 15, 1)
)
if mibBuilder.loadTexts:
    appnDlusRowStatusTable.setStatus("mandatory")
_AppnDlusRowStatusEntry_Object = MibTableRow
appnDlusRowStatusEntry = _AppnDlusRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 15, 1, 1)
)
appnDlusRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlusIndex"),
)
if mibBuilder.loadTexts:
    appnDlusRowStatusEntry.setStatus("mandatory")
_AppnDlusRowStatus_Type = RowStatus
_AppnDlusRowStatus_Object = MibTableColumn
appnDlusRowStatus = _AppnDlusRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 15, 1, 1, 1),
    _AppnDlusRowStatus_Type()
)
appnDlusRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlusRowStatus.setStatus("mandatory")
_AppnDlusComponentName_Type = DisplayString
_AppnDlusComponentName_Object = MibTableColumn
appnDlusComponentName = _AppnDlusComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 15, 1, 1, 2),
    _AppnDlusComponentName_Type()
)
appnDlusComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlusComponentName.setStatus("mandatory")
_AppnDlusStorageType_Type = StorageType
_AppnDlusStorageType_Object = MibTableColumn
appnDlusStorageType = _AppnDlusStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 15, 1, 1, 4),
    _AppnDlusStorageType_Type()
)
appnDlusStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlusStorageType.setStatus("mandatory")


class _AppnDlusIndex_Type(AsciiStringIndex):
    """Custom type appnDlusIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppnDlusIndex_Type.__name__ = "AsciiStringIndex"
_AppnDlusIndex_Object = MibTableColumn
appnDlusIndex = _AppnDlusIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 15, 1, 1, 10),
    _AppnDlusIndex_Type()
)
appnDlusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnDlusIndex.setStatus("mandatory")
_AppnDlusOperTable_Object = MibTable
appnDlusOperTable = _AppnDlusOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 15, 10)
)
if mibBuilder.loadTexts:
    appnDlusOperTable.setStatus("mandatory")
_AppnDlusOperEntry_Object = MibTableRow
appnDlusOperEntry = _AppnDlusOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 15, 10, 1)
)
appnDlusOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlusIndex"),
)
if mibBuilder.loadTexts:
    appnDlusOperEntry.setStatus("mandatory")


class _AppnDlusPrimaryDlus_Type(Integer32):
    """Custom type appnDlusPrimaryDlus based on Integer32"""
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


_AppnDlusPrimaryDlus_Type.__name__ = "Integer32"
_AppnDlusPrimaryDlus_Object = MibTableColumn
appnDlusPrimaryDlus = _AppnDlusPrimaryDlus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 15, 10, 1, 1),
    _AppnDlusPrimaryDlus_Type()
)
appnDlusPrimaryDlus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlusPrimaryDlus.setStatus("mandatory")


class _AppnDlusPipeState_Type(Integer32):
    """Custom type appnDlusPipeState based on Integer32"""
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


_AppnDlusPipeState_Type.__name__ = "Integer32"
_AppnDlusPipeState_Object = MibTableColumn
appnDlusPipeState = _AppnDlusPipeState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 15, 10, 1, 2),
    _AppnDlusPipeState_Type()
)
appnDlusPipeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlusPipeState.setStatus("mandatory")


class _AppnDlusActivePUs_Type(Gauge32):
    """Custom type appnDlusActivePUs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AppnDlusActivePUs_Type.__name__ = "Gauge32"
_AppnDlusActivePUs_Object = MibTableColumn
appnDlusActivePUs = _AppnDlusActivePUs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 15, 10, 1, 3),
    _AppnDlusActivePUs_Type()
)
appnDlusActivePUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlusActivePUs.setStatus("mandatory")
_AppnDlusDlusStatTable_Object = MibTable
appnDlusDlusStatTable = _AppnDlusDlusStatTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 15, 11)
)
if mibBuilder.loadTexts:
    appnDlusDlusStatTable.setStatus("mandatory")
_AppnDlusDlusStatEntry_Object = MibTableRow
appnDlusDlusStatEntry = _AppnDlusDlusStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 15, 11, 1)
)
appnDlusDlusStatEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDlusIndex"),
)
if mibBuilder.loadTexts:
    appnDlusDlusStatEntry.setStatus("mandatory")
_AppnDlusReqActPuTx_Type = PassportCounter64
_AppnDlusReqActPuTx_Object = MibTableColumn
appnDlusReqActPuTx = _AppnDlusReqActPuTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 15, 11, 1, 1),
    _AppnDlusReqActPuTx_Type()
)
appnDlusReqActPuTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlusReqActPuTx.setStatus("mandatory")
_AppnDlusReqActPuRspRx_Type = PassportCounter64
_AppnDlusReqActPuRspRx_Object = MibTableColumn
appnDlusReqActPuRspRx = _AppnDlusReqActPuRspRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 15, 11, 1, 2),
    _AppnDlusReqActPuRspRx_Type()
)
appnDlusReqActPuRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlusReqActPuRspRx.setStatus("mandatory")
_AppnDlusActPuRx_Type = PassportCounter64
_AppnDlusActPuRx_Object = MibTableColumn
appnDlusActPuRx = _AppnDlusActPuRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 15, 11, 1, 3),
    _AppnDlusActPuRx_Type()
)
appnDlusActPuRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlusActPuRx.setStatus("mandatory")
_AppnDlusActPuRspTx_Type = PassportCounter64
_AppnDlusActPuRspTx_Object = MibTableColumn
appnDlusActPuRspTx = _AppnDlusActPuRspTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 15, 11, 1, 4),
    _AppnDlusActPuRspTx_Type()
)
appnDlusActPuRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlusActPuRspTx.setStatus("mandatory")
_AppnDlusReqDactPuTx_Type = PassportCounter64
_AppnDlusReqDactPuTx_Object = MibTableColumn
appnDlusReqDactPuTx = _AppnDlusReqDactPuTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 15, 11, 1, 5),
    _AppnDlusReqDactPuTx_Type()
)
appnDlusReqDactPuTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlusReqDactPuTx.setStatus("mandatory")
_AppnDlusReqDactPuRspRx_Type = PassportCounter64
_AppnDlusReqDactPuRspRx_Object = MibTableColumn
appnDlusReqDactPuRspRx = _AppnDlusReqDactPuRspRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 15, 11, 1, 6),
    _AppnDlusReqDactPuRspRx_Type()
)
appnDlusReqDactPuRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlusReqDactPuRspRx.setStatus("mandatory")
_AppnDlusDactPuRx_Type = PassportCounter64
_AppnDlusDactPuRx_Object = MibTableColumn
appnDlusDactPuRx = _AppnDlusDactPuRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 15, 11, 1, 7),
    _AppnDlusDactPuRx_Type()
)
appnDlusDactPuRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlusDactPuRx.setStatus("mandatory")
_AppnDlusDactPuRspTx_Type = PassportCounter64
_AppnDlusDactPuRspTx_Object = MibTableColumn
appnDlusDactPuRspTx = _AppnDlusDactPuRspTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 15, 11, 1, 8),
    _AppnDlusDactPuRspTx_Type()
)
appnDlusDactPuRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlusDactPuRspTx.setStatus("mandatory")
_AppnDlusActLuRx_Type = PassportCounter64
_AppnDlusActLuRx_Object = MibTableColumn
appnDlusActLuRx = _AppnDlusActLuRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 15, 11, 1, 9),
    _AppnDlusActLuRx_Type()
)
appnDlusActLuRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlusActLuRx.setStatus("mandatory")
_AppnDlusActLuRspTx_Type = PassportCounter64
_AppnDlusActLuRspTx_Object = MibTableColumn
appnDlusActLuRspTx = _AppnDlusActLuRspTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 15, 11, 1, 10),
    _AppnDlusActLuRspTx_Type()
)
appnDlusActLuRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlusActLuRspTx.setStatus("mandatory")
_AppnDlusDactLuRx_Type = PassportCounter64
_AppnDlusDactLuRx_Object = MibTableColumn
appnDlusDactLuRx = _AppnDlusDactLuRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 15, 11, 1, 11),
    _AppnDlusDactLuRx_Type()
)
appnDlusDactLuRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlusDactLuRx.setStatus("mandatory")
_AppnDlusDactLuRspTx_Type = PassportCounter64
_AppnDlusDactLuRspTx_Object = MibTableColumn
appnDlusDactLuRspTx = _AppnDlusDactLuRspTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 15, 11, 1, 12),
    _AppnDlusDactLuRspTx_Type()
)
appnDlusDactLuRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlusDactLuRspTx.setStatus("mandatory")
_AppnDlusSscpPuMuRx_Type = PassportCounter64
_AppnDlusSscpPuMuRx_Object = MibTableColumn
appnDlusSscpPuMuRx = _AppnDlusSscpPuMuRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 15, 11, 1, 13),
    _AppnDlusSscpPuMuRx_Type()
)
appnDlusSscpPuMuRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlusSscpPuMuRx.setStatus("mandatory")
_AppnDlusSscpPuMuTx_Type = PassportCounter64
_AppnDlusSscpPuMuTx_Object = MibTableColumn
appnDlusSscpPuMuTx = _AppnDlusSscpPuMuTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 15, 11, 1, 14),
    _AppnDlusSscpPuMuTx_Type()
)
appnDlusSscpPuMuTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlusSscpPuMuTx.setStatus("mandatory")
_AppnDlusSscpLuMuRx_Type = PassportCounter64
_AppnDlusSscpLuMuRx_Object = MibTableColumn
appnDlusSscpLuMuRx = _AppnDlusSscpLuMuRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 15, 11, 1, 15),
    _AppnDlusSscpLuMuRx_Type()
)
appnDlusSscpLuMuRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlusSscpLuMuRx.setStatus("mandatory")
_AppnDlusSscpLuMuTx_Type = PassportCounter64
_AppnDlusSscpLuMuTx_Object = MibTableColumn
appnDlusSscpLuMuTx = _AppnDlusSscpLuMuTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 15, 11, 1, 16),
    _AppnDlusSscpLuMuTx_Type()
)
appnDlusSscpLuMuTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDlusSscpLuMuTx.setStatus("mandatory")
_AppnDLUR_ObjectIdentity = ObjectIdentity
appnDLUR = _AppnDLUR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 16)
)
_AppnDLURRowStatusTable_Object = MibTable
appnDLURRowStatusTable = _AppnDLURRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 16, 1)
)
if mibBuilder.loadTexts:
    appnDLURRowStatusTable.setStatus("mandatory")
_AppnDLURRowStatusEntry_Object = MibTableRow
appnDLURRowStatusEntry = _AppnDLURRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 16, 1, 1)
)
appnDLURRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDLURIndex"),
)
if mibBuilder.loadTexts:
    appnDLURRowStatusEntry.setStatus("mandatory")
_AppnDLURRowStatus_Type = RowStatus
_AppnDLURRowStatus_Object = MibTableColumn
appnDLURRowStatus = _AppnDLURRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 16, 1, 1, 1),
    _AppnDLURRowStatus_Type()
)
appnDLURRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDLURRowStatus.setStatus("mandatory")
_AppnDLURComponentName_Type = DisplayString
_AppnDLURComponentName_Object = MibTableColumn
appnDLURComponentName = _AppnDLURComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 16, 1, 1, 2),
    _AppnDLURComponentName_Type()
)
appnDLURComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDLURComponentName.setStatus("mandatory")
_AppnDLURStorageType_Type = StorageType
_AppnDLURStorageType_Object = MibTableColumn
appnDLURStorageType = _AppnDLURStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 16, 1, 1, 4),
    _AppnDLURStorageType_Type()
)
appnDLURStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDLURStorageType.setStatus("mandatory")
_AppnDLURIndex_Type = NonReplicated
_AppnDLURIndex_Object = MibTableColumn
appnDLURIndex = _AppnDLURIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 16, 1, 1, 10),
    _AppnDLURIndex_Type()
)
appnDLURIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnDLURIndex.setStatus("mandatory")
_AppnDLURDlurParmsTable_Object = MibTable
appnDLURDlurParmsTable = _AppnDLURDlurParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 16, 2)
)
if mibBuilder.loadTexts:
    appnDLURDlurParmsTable.setStatus("mandatory")
_AppnDLURDlurParmsEntry_Object = MibTableRow
appnDLURDlurParmsEntry = _AppnDLURDlurParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 16, 2, 1)
)
appnDLURDlurParmsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnDLURIndex"),
)
if mibBuilder.loadTexts:
    appnDLURDlurParmsEntry.setStatus("mandatory")


class _AppnDLURPrimaryDefDlusName_Type(AsciiString):
    """Custom type appnDLURPrimaryDefDlusName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_AppnDLURPrimaryDefDlusName_Type.__name__ = "AsciiString"
_AppnDLURPrimaryDefDlusName_Object = MibTableColumn
appnDLURPrimaryDefDlusName = _AppnDLURPrimaryDefDlusName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 16, 2, 1, 2),
    _AppnDLURPrimaryDefDlusName_Type()
)
appnDLURPrimaryDefDlusName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDLURPrimaryDefDlusName.setStatus("mandatory")


class _AppnDLURSecondaryDefDlusName_Type(AsciiString):
    """Custom type appnDLURSecondaryDefDlusName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_AppnDLURSecondaryDefDlusName_Type.__name__ = "AsciiString"
_AppnDLURSecondaryDefDlusName_Object = MibTableColumn
appnDLURSecondaryDefDlusName = _AppnDLURSecondaryDefDlusName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 16, 2, 1, 3),
    _AppnDLURSecondaryDefDlusName_Type()
)
appnDLURSecondaryDefDlusName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDLURSecondaryDefDlusName.setStatus("mandatory")


class _AppnDLURDlusRetryTimeout_Type(Unsigned32):
    """Custom type appnDLURDlusRetryTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AppnDLURDlusRetryTimeout_Type.__name__ = "Unsigned32"
_AppnDLURDlusRetryTimeout_Object = MibTableColumn
appnDLURDlusRetryTimeout = _AppnDLURDlusRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 16, 2, 1, 4),
    _AppnDLURDlusRetryTimeout_Type()
)
appnDLURDlusRetryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDLURDlusRetryTimeout.setStatus("mandatory")


class _AppnDLURDlusRetryLimit_Type(Unsigned32):
    """Custom type appnDLURDlusRetryLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnDLURDlusRetryLimit_Type.__name__ = "Unsigned32"
_AppnDLURDlusRetryLimit_Object = MibTableColumn
appnDLURDlusRetryLimit = _AppnDLURDlusRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 16, 2, 1, 5),
    _AppnDLURDlusRetryLimit_Type()
)
appnDLURDlusRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDLURDlusRetryLimit.setStatus("mandatory")
_AppnCos_ObjectIdentity = ObjectIdentity
appnCos = _AppnCos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17)
)
_AppnCosRowStatusTable_Object = MibTable
appnCosRowStatusTable = _AppnCosRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 1)
)
if mibBuilder.loadTexts:
    appnCosRowStatusTable.setStatus("mandatory")
_AppnCosRowStatusEntry_Object = MibTableRow
appnCosRowStatusEntry = _AppnCosRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 1, 1)
)
appnCosRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnCosIndex"),
)
if mibBuilder.loadTexts:
    appnCosRowStatusEntry.setStatus("mandatory")
_AppnCosRowStatus_Type = RowStatus
_AppnCosRowStatus_Object = MibTableColumn
appnCosRowStatus = _AppnCosRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 1, 1, 1),
    _AppnCosRowStatus_Type()
)
appnCosRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnCosRowStatus.setStatus("mandatory")
_AppnCosComponentName_Type = DisplayString
_AppnCosComponentName_Object = MibTableColumn
appnCosComponentName = _AppnCosComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 1, 1, 2),
    _AppnCosComponentName_Type()
)
appnCosComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCosComponentName.setStatus("mandatory")
_AppnCosStorageType_Type = StorageType
_AppnCosStorageType_Object = MibTableColumn
appnCosStorageType = _AppnCosStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 1, 1, 4),
    _AppnCosStorageType_Type()
)
appnCosStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCosStorageType.setStatus("mandatory")


class _AppnCosIndex_Type(AsciiStringIndex):
    """Custom type appnCosIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppnCosIndex_Type.__name__ = "AsciiStringIndex"
_AppnCosIndex_Object = MibTableColumn
appnCosIndex = _AppnCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 1, 1, 10),
    _AppnCosIndex_Type()
)
appnCosIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnCosIndex.setStatus("mandatory")
_AppnCosTg_ObjectIdentity = ObjectIdentity
appnCosTg = _AppnCosTg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 10)
)
_AppnCosTgRowStatusTable_Object = MibTable
appnCosTgRowStatusTable = _AppnCosTgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 10, 1)
)
if mibBuilder.loadTexts:
    appnCosTgRowStatusTable.setStatus("mandatory")
_AppnCosTgRowStatusEntry_Object = MibTableRow
appnCosTgRowStatusEntry = _AppnCosTgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 10, 1, 1)
)
appnCosTgRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnCosIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnCosTgIndex"),
)
if mibBuilder.loadTexts:
    appnCosTgRowStatusEntry.setStatus("mandatory")
_AppnCosTgRowStatus_Type = RowStatus
_AppnCosTgRowStatus_Object = MibTableColumn
appnCosTgRowStatus = _AppnCosTgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 10, 1, 1, 1),
    _AppnCosTgRowStatus_Type()
)
appnCosTgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnCosTgRowStatus.setStatus("mandatory")
_AppnCosTgComponentName_Type = DisplayString
_AppnCosTgComponentName_Object = MibTableColumn
appnCosTgComponentName = _AppnCosTgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 10, 1, 1, 2),
    _AppnCosTgComponentName_Type()
)
appnCosTgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCosTgComponentName.setStatus("mandatory")
_AppnCosTgStorageType_Type = StorageType
_AppnCosTgStorageType_Object = MibTableColumn
appnCosTgStorageType = _AppnCosTgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 10, 1, 1, 4),
    _AppnCosTgStorageType_Type()
)
appnCosTgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCosTgStorageType.setStatus("mandatory")


class _AppnCosTgIndex_Type(Integer32):
    """Custom type appnCosTgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AppnCosTgIndex_Type.__name__ = "Integer32"
_AppnCosTgIndex_Object = MibTableColumn
appnCosTgIndex = _AppnCosTgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 10, 1, 1, 10),
    _AppnCosTgIndex_Type()
)
appnCosTgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnCosTgIndex.setStatus("mandatory")
_AppnCosTgProvTable_Object = MibTable
appnCosTgProvTable = _AppnCosTgProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 10, 10)
)
if mibBuilder.loadTexts:
    appnCosTgProvTable.setStatus("mandatory")
_AppnCosTgProvEntry_Object = MibTableRow
appnCosTgProvEntry = _AppnCosTgProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 10, 10, 1)
)
appnCosTgProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnCosIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnCosTgIndex"),
)
if mibBuilder.loadTexts:
    appnCosTgProvEntry.setStatus("mandatory")


class _AppnCosTgMinEffectiveCapacity_Type(Integer32):
    """Custom type appnCosTgMinEffectiveCapacity based on Integer32"""
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


_AppnCosTgMinEffectiveCapacity_Type.__name__ = "Integer32"
_AppnCosTgMinEffectiveCapacity_Object = MibTableColumn
appnCosTgMinEffectiveCapacity = _AppnCosTgMinEffectiveCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 10, 10, 1, 1),
    _AppnCosTgMinEffectiveCapacity_Type()
)
appnCosTgMinEffectiveCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnCosTgMinEffectiveCapacity.setStatus("mandatory")


class _AppnCosTgMaxEffectiveCapacity_Type(Integer32):
    """Custom type appnCosTgMaxEffectiveCapacity based on Integer32"""
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


_AppnCosTgMaxEffectiveCapacity_Type.__name__ = "Integer32"
_AppnCosTgMaxEffectiveCapacity_Object = MibTableColumn
appnCosTgMaxEffectiveCapacity = _AppnCosTgMaxEffectiveCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 10, 10, 1, 2),
    _AppnCosTgMaxEffectiveCapacity_Type()
)
appnCosTgMaxEffectiveCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnCosTgMaxEffectiveCapacity.setStatus("mandatory")


class _AppnCosTgMinConnectCost_Type(Integer32):
    """Custom type appnCosTgMinConnectCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnCosTgMinConnectCost_Type.__name__ = "Integer32"
_AppnCosTgMinConnectCost_Object = MibTableColumn
appnCosTgMinConnectCost = _AppnCosTgMinConnectCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 10, 10, 1, 3),
    _AppnCosTgMinConnectCost_Type()
)
appnCosTgMinConnectCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnCosTgMinConnectCost.setStatus("mandatory")


class _AppnCosTgMaxConnectCost_Type(Integer32):
    """Custom type appnCosTgMaxConnectCost based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnCosTgMaxConnectCost_Type.__name__ = "Integer32"
_AppnCosTgMaxConnectCost_Object = MibTableColumn
appnCosTgMaxConnectCost = _AppnCosTgMaxConnectCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 10, 10, 1, 4),
    _AppnCosTgMaxConnectCost_Type()
)
appnCosTgMaxConnectCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnCosTgMaxConnectCost.setStatus("mandatory")


class _AppnCosTgMinByteCost_Type(Integer32):
    """Custom type appnCosTgMinByteCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnCosTgMinByteCost_Type.__name__ = "Integer32"
_AppnCosTgMinByteCost_Object = MibTableColumn
appnCosTgMinByteCost = _AppnCosTgMinByteCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 10, 10, 1, 5),
    _AppnCosTgMinByteCost_Type()
)
appnCosTgMinByteCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnCosTgMinByteCost.setStatus("mandatory")


class _AppnCosTgMaxByteCost_Type(Integer32):
    """Custom type appnCosTgMaxByteCost based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnCosTgMaxByteCost_Type.__name__ = "Integer32"
_AppnCosTgMaxByteCost_Object = MibTableColumn
appnCosTgMaxByteCost = _AppnCosTgMaxByteCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 10, 10, 1, 6),
    _AppnCosTgMaxByteCost_Type()
)
appnCosTgMaxByteCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnCosTgMaxByteCost.setStatus("mandatory")


class _AppnCosTgMinSecurity_Type(Integer32):
    """Custom type appnCosTgMinSecurity based on Integer32"""
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


_AppnCosTgMinSecurity_Type.__name__ = "Integer32"
_AppnCosTgMinSecurity_Object = MibTableColumn
appnCosTgMinSecurity = _AppnCosTgMinSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 10, 10, 1, 7),
    _AppnCosTgMinSecurity_Type()
)
appnCosTgMinSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnCosTgMinSecurity.setStatus("mandatory")


class _AppnCosTgMaxSecurity_Type(Integer32):
    """Custom type appnCosTgMaxSecurity based on Integer32"""
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


_AppnCosTgMaxSecurity_Type.__name__ = "Integer32"
_AppnCosTgMaxSecurity_Object = MibTableColumn
appnCosTgMaxSecurity = _AppnCosTgMaxSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 10, 10, 1, 8),
    _AppnCosTgMaxSecurity_Type()
)
appnCosTgMaxSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnCosTgMaxSecurity.setStatus("mandatory")


class _AppnCosTgMinPropDelay_Type(Integer32):
    """Custom type appnCosTgMinPropDelay based on Integer32"""
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


_AppnCosTgMinPropDelay_Type.__name__ = "Integer32"
_AppnCosTgMinPropDelay_Object = MibTableColumn
appnCosTgMinPropDelay = _AppnCosTgMinPropDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 10, 10, 1, 9),
    _AppnCosTgMinPropDelay_Type()
)
appnCosTgMinPropDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnCosTgMinPropDelay.setStatus("mandatory")


class _AppnCosTgMaxPropDelay_Type(Integer32):
    """Custom type appnCosTgMaxPropDelay based on Integer32"""
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


_AppnCosTgMaxPropDelay_Type.__name__ = "Integer32"
_AppnCosTgMaxPropDelay_Object = MibTableColumn
appnCosTgMaxPropDelay = _AppnCosTgMaxPropDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 10, 10, 1, 10),
    _AppnCosTgMaxPropDelay_Type()
)
appnCosTgMaxPropDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnCosTgMaxPropDelay.setStatus("mandatory")


class _AppnCosTgMinModemClass_Type(Integer32):
    """Custom type appnCosTgMinModemClass based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnCosTgMinModemClass_Type.__name__ = "Integer32"
_AppnCosTgMinModemClass_Object = MibTableColumn
appnCosTgMinModemClass = _AppnCosTgMinModemClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 10, 10, 1, 11),
    _AppnCosTgMinModemClass_Type()
)
appnCosTgMinModemClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnCosTgMinModemClass.setStatus("mandatory")


class _AppnCosTgMaxModemClass_Type(Integer32):
    """Custom type appnCosTgMaxModemClass based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnCosTgMaxModemClass_Type.__name__ = "Integer32"
_AppnCosTgMaxModemClass_Object = MibTableColumn
appnCosTgMaxModemClass = _AppnCosTgMaxModemClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 10, 10, 1, 12),
    _AppnCosTgMaxModemClass_Type()
)
appnCosTgMaxModemClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnCosTgMaxModemClass.setStatus("mandatory")


class _AppnCosTgMinUserDefParm1_Type(Integer32):
    """Custom type appnCosTgMinUserDefParm1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnCosTgMinUserDefParm1_Type.__name__ = "Integer32"
_AppnCosTgMinUserDefParm1_Object = MibTableColumn
appnCosTgMinUserDefParm1 = _AppnCosTgMinUserDefParm1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 10, 10, 1, 13),
    _AppnCosTgMinUserDefParm1_Type()
)
appnCosTgMinUserDefParm1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnCosTgMinUserDefParm1.setStatus("mandatory")


class _AppnCosTgMaxUserDefParm1_Type(Integer32):
    """Custom type appnCosTgMaxUserDefParm1 based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnCosTgMaxUserDefParm1_Type.__name__ = "Integer32"
_AppnCosTgMaxUserDefParm1_Object = MibTableColumn
appnCosTgMaxUserDefParm1 = _AppnCosTgMaxUserDefParm1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 10, 10, 1, 14),
    _AppnCosTgMaxUserDefParm1_Type()
)
appnCosTgMaxUserDefParm1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnCosTgMaxUserDefParm1.setStatus("mandatory")


class _AppnCosTgMinUserDefParm2_Type(Integer32):
    """Custom type appnCosTgMinUserDefParm2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnCosTgMinUserDefParm2_Type.__name__ = "Integer32"
_AppnCosTgMinUserDefParm2_Object = MibTableColumn
appnCosTgMinUserDefParm2 = _AppnCosTgMinUserDefParm2_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 10, 10, 1, 15),
    _AppnCosTgMinUserDefParm2_Type()
)
appnCosTgMinUserDefParm2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnCosTgMinUserDefParm2.setStatus("mandatory")


class _AppnCosTgMaxUserDefParm2_Type(Integer32):
    """Custom type appnCosTgMaxUserDefParm2 based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnCosTgMaxUserDefParm2_Type.__name__ = "Integer32"
_AppnCosTgMaxUserDefParm2_Object = MibTableColumn
appnCosTgMaxUserDefParm2 = _AppnCosTgMaxUserDefParm2_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 10, 10, 1, 16),
    _AppnCosTgMaxUserDefParm2_Type()
)
appnCosTgMaxUserDefParm2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnCosTgMaxUserDefParm2.setStatus("mandatory")


class _AppnCosTgMinUserDefParm3_Type(Integer32):
    """Custom type appnCosTgMinUserDefParm3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnCosTgMinUserDefParm3_Type.__name__ = "Integer32"
_AppnCosTgMinUserDefParm3_Object = MibTableColumn
appnCosTgMinUserDefParm3 = _AppnCosTgMinUserDefParm3_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 10, 10, 1, 17),
    _AppnCosTgMinUserDefParm3_Type()
)
appnCosTgMinUserDefParm3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnCosTgMinUserDefParm3.setStatus("mandatory")


class _AppnCosTgMaxUserDefParm3_Type(Integer32):
    """Custom type appnCosTgMaxUserDefParm3 based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnCosTgMaxUserDefParm3_Type.__name__ = "Integer32"
_AppnCosTgMaxUserDefParm3_Object = MibTableColumn
appnCosTgMaxUserDefParm3 = _AppnCosTgMaxUserDefParm3_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 10, 10, 1, 18),
    _AppnCosTgMaxUserDefParm3_Type()
)
appnCosTgMaxUserDefParm3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnCosTgMaxUserDefParm3.setStatus("mandatory")
_AppnCosNode_ObjectIdentity = ObjectIdentity
appnCosNode = _AppnCosNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 11)
)
_AppnCosNodeRowStatusTable_Object = MibTable
appnCosNodeRowStatusTable = _AppnCosNodeRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 11, 1)
)
if mibBuilder.loadTexts:
    appnCosNodeRowStatusTable.setStatus("mandatory")
_AppnCosNodeRowStatusEntry_Object = MibTableRow
appnCosNodeRowStatusEntry = _AppnCosNodeRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 11, 1, 1)
)
appnCosNodeRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnCosIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnCosNodeIndex"),
)
if mibBuilder.loadTexts:
    appnCosNodeRowStatusEntry.setStatus("mandatory")
_AppnCosNodeRowStatus_Type = RowStatus
_AppnCosNodeRowStatus_Object = MibTableColumn
appnCosNodeRowStatus = _AppnCosNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 11, 1, 1, 1),
    _AppnCosNodeRowStatus_Type()
)
appnCosNodeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnCosNodeRowStatus.setStatus("mandatory")
_AppnCosNodeComponentName_Type = DisplayString
_AppnCosNodeComponentName_Object = MibTableColumn
appnCosNodeComponentName = _AppnCosNodeComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 11, 1, 1, 2),
    _AppnCosNodeComponentName_Type()
)
appnCosNodeComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCosNodeComponentName.setStatus("mandatory")
_AppnCosNodeStorageType_Type = StorageType
_AppnCosNodeStorageType_Object = MibTableColumn
appnCosNodeStorageType = _AppnCosNodeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 11, 1, 1, 4),
    _AppnCosNodeStorageType_Type()
)
appnCosNodeStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCosNodeStorageType.setStatus("mandatory")


class _AppnCosNodeIndex_Type(Integer32):
    """Custom type appnCosNodeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AppnCosNodeIndex_Type.__name__ = "Integer32"
_AppnCosNodeIndex_Object = MibTableColumn
appnCosNodeIndex = _AppnCosNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 11, 1, 1, 10),
    _AppnCosNodeIndex_Type()
)
appnCosNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnCosNodeIndex.setStatus("mandatory")
_AppnCosNodeProvTable_Object = MibTable
appnCosNodeProvTable = _AppnCosNodeProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 11, 10)
)
if mibBuilder.loadTexts:
    appnCosNodeProvTable.setStatus("mandatory")
_AppnCosNodeProvEntry_Object = MibTableRow
appnCosNodeProvEntry = _AppnCosNodeProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 11, 10, 1)
)
appnCosNodeProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnCosIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnCosNodeIndex"),
)
if mibBuilder.loadTexts:
    appnCosNodeProvEntry.setStatus("mandatory")


class _AppnCosNodeMinRouteAddResistance_Type(Integer32):
    """Custom type appnCosNodeMinRouteAddResistance based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnCosNodeMinRouteAddResistance_Type.__name__ = "Integer32"
_AppnCosNodeMinRouteAddResistance_Object = MibTableColumn
appnCosNodeMinRouteAddResistance = _AppnCosNodeMinRouteAddResistance_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 11, 10, 1, 1),
    _AppnCosNodeMinRouteAddResistance_Type()
)
appnCosNodeMinRouteAddResistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnCosNodeMinRouteAddResistance.setStatus("mandatory")


class _AppnCosNodeMaxRouteAddResistance_Type(Integer32):
    """Custom type appnCosNodeMaxRouteAddResistance based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnCosNodeMaxRouteAddResistance_Type.__name__ = "Integer32"
_AppnCosNodeMaxRouteAddResistance_Object = MibTableColumn
appnCosNodeMaxRouteAddResistance = _AppnCosNodeMaxRouteAddResistance_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 11, 10, 1, 2),
    _AppnCosNodeMaxRouteAddResistance_Type()
)
appnCosNodeMaxRouteAddResistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnCosNodeMaxRouteAddResistance.setStatus("mandatory")


class _AppnCosNodeMinStatus_Type(Integer32):
    """Custom type appnCosNodeMinStatus based on Integer32"""
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


_AppnCosNodeMinStatus_Type.__name__ = "Integer32"
_AppnCosNodeMinStatus_Object = MibTableColumn
appnCosNodeMinStatus = _AppnCosNodeMinStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 11, 10, 1, 3),
    _AppnCosNodeMinStatus_Type()
)
appnCosNodeMinStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnCosNodeMinStatus.setStatus("mandatory")


class _AppnCosNodeMaxStatus_Type(Integer32):
    """Custom type appnCosNodeMaxStatus based on Integer32"""
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


_AppnCosNodeMaxStatus_Type.__name__ = "Integer32"
_AppnCosNodeMaxStatus_Object = MibTableColumn
appnCosNodeMaxStatus = _AppnCosNodeMaxStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 11, 10, 1, 4),
    _AppnCosNodeMaxStatus_Type()
)
appnCosNodeMaxStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnCosNodeMaxStatus.setStatus("mandatory")
_AppnCosProvTable_Object = MibTable
appnCosProvTable = _AppnCosProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 104)
)
if mibBuilder.loadTexts:
    appnCosProvTable.setStatus("mandatory")
_AppnCosProvEntry_Object = MibTableRow
appnCosProvEntry = _AppnCosProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 104, 1)
)
appnCosProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnCosIndex"),
)
if mibBuilder.loadTexts:
    appnCosProvEntry.setStatus("mandatory")


class _AppnCosTransmissionPriority_Type(Integer32):
    """Custom type appnCosTransmissionPriority based on Integer32"""
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


_AppnCosTransmissionPriority_Type.__name__ = "Integer32"
_AppnCosTransmissionPriority_Object = MibTableColumn
appnCosTransmissionPriority = _AppnCosTransmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 17, 104, 1, 1),
    _AppnCosTransmissionPriority_Type()
)
appnCosTransmissionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnCosTransmissionPriority.setStatus("mandatory")
_AppnFrSvc_ObjectIdentity = ObjectIdentity
appnFrSvc = _AppnFrSvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 18)
)
_AppnFrSvcRowStatusTable_Object = MibTable
appnFrSvcRowStatusTable = _AppnFrSvcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 18, 1)
)
if mibBuilder.loadTexts:
    appnFrSvcRowStatusTable.setStatus("mandatory")
_AppnFrSvcRowStatusEntry_Object = MibTableRow
appnFrSvcRowStatusEntry = _AppnFrSvcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 18, 1, 1)
)
appnFrSvcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnFrSvcIndex"),
)
if mibBuilder.loadTexts:
    appnFrSvcRowStatusEntry.setStatus("mandatory")
_AppnFrSvcRowStatus_Type = RowStatus
_AppnFrSvcRowStatus_Object = MibTableColumn
appnFrSvcRowStatus = _AppnFrSvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 18, 1, 1, 1),
    _AppnFrSvcRowStatus_Type()
)
appnFrSvcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnFrSvcRowStatus.setStatus("mandatory")
_AppnFrSvcComponentName_Type = DisplayString
_AppnFrSvcComponentName_Object = MibTableColumn
appnFrSvcComponentName = _AppnFrSvcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 18, 1, 1, 2),
    _AppnFrSvcComponentName_Type()
)
appnFrSvcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnFrSvcComponentName.setStatus("mandatory")
_AppnFrSvcStorageType_Type = StorageType
_AppnFrSvcStorageType_Object = MibTableColumn
appnFrSvcStorageType = _AppnFrSvcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 18, 1, 1, 4),
    _AppnFrSvcStorageType_Type()
)
appnFrSvcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnFrSvcStorageType.setStatus("mandatory")
_AppnFrSvcIndex_Type = NonReplicated
_AppnFrSvcIndex_Object = MibTableColumn
appnFrSvcIndex = _AppnFrSvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 18, 1, 1, 10),
    _AppnFrSvcIndex_Type()
)
appnFrSvcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnFrSvcIndex.setStatus("mandatory")
_AppnFrSvcBanTable_Object = MibTable
appnFrSvcBanTable = _AppnFrSvcBanTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 18, 10)
)
if mibBuilder.loadTexts:
    appnFrSvcBanTable.setStatus("mandatory")
_AppnFrSvcBanEntry_Object = MibTableRow
appnFrSvcBanEntry = _AppnFrSvcBanEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 18, 10, 1)
)
appnFrSvcBanEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnFrSvcIndex"),
)
if mibBuilder.loadTexts:
    appnFrSvcBanEntry.setStatus("mandatory")


class _AppnFrSvcBanLocalMac_Type(DashedHexString):
    """Custom type appnFrSvcBanLocalMac based on DashedHexString"""
    defaultHexValue = "4fff00000000"

    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AppnFrSvcBanLocalMac_Type.__name__ = "DashedHexString"
_AppnFrSvcBanLocalMac_Object = MibTableColumn
appnFrSvcBanLocalMac = _AppnFrSvcBanLocalMac_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 18, 10, 1, 1),
    _AppnFrSvcBanLocalMac_Type()
)
appnFrSvcBanLocalMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnFrSvcBanLocalMac.setStatus("mandatory")


class _AppnFrSvcBanLocalSap_Type(Hex):
    """Custom type appnFrSvcBanLocalSap based on Hex"""
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


_AppnFrSvcBanLocalSap_Type.__name__ = "Hex"
_AppnFrSvcBanLocalSap_Object = MibTableColumn
appnFrSvcBanLocalSap = _AppnFrSvcBanLocalSap_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 18, 10, 1, 2),
    _AppnFrSvcBanLocalSap_Type()
)
appnFrSvcBanLocalSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnFrSvcBanLocalSap.setStatus("mandatory")
_AppnFrSvcProvisionedTable_Object = MibTable
appnFrSvcProvisionedTable = _AppnFrSvcProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 18, 11)
)
if mibBuilder.loadTexts:
    appnFrSvcProvisionedTable.setStatus("mandatory")
_AppnFrSvcProvisionedEntry_Object = MibTableRow
appnFrSvcProvisionedEntry = _AppnFrSvcProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 18, 11, 1)
)
appnFrSvcProvisionedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnFrSvcIndex"),
)
if mibBuilder.loadTexts:
    appnFrSvcProvisionedEntry.setStatus("mandatory")


class _AppnFrSvcMaximumFrameRelaySvcs_Type(Unsigned32):
    """Custom type appnFrSvcMaximumFrameRelaySvcs based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3072),
    )


_AppnFrSvcMaximumFrameRelaySvcs_Type.__name__ = "Unsigned32"
_AppnFrSvcMaximumFrameRelaySvcs_Object = MibTableColumn
appnFrSvcMaximumFrameRelaySvcs = _AppnFrSvcMaximumFrameRelaySvcs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 18, 11, 1, 1),
    _AppnFrSvcMaximumFrameRelaySvcs_Type()
)
appnFrSvcMaximumFrameRelaySvcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnFrSvcMaximumFrameRelaySvcs.setStatus("mandatory")


class _AppnFrSvcRateEnforcement_Type(Integer32):
    """Custom type appnFrSvcRateEnforcement based on Integer32"""
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


_AppnFrSvcRateEnforcement_Type.__name__ = "Integer32"
_AppnFrSvcRateEnforcement_Object = MibTableColumn
appnFrSvcRateEnforcement = _AppnFrSvcRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 18, 11, 1, 2),
    _AppnFrSvcRateEnforcement_Type()
)
appnFrSvcRateEnforcement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnFrSvcRateEnforcement.setStatus("mandatory")


class _AppnFrSvcMaximumCir_Type(Unsigned32):
    """Custom type appnFrSvcMaximumCir based on Unsigned32"""
    defaultValue = 2048000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52000000),
    )


_AppnFrSvcMaximumCir_Type.__name__ = "Unsigned32"
_AppnFrSvcMaximumCir_Object = MibTableColumn
appnFrSvcMaximumCir = _AppnFrSvcMaximumCir_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 18, 11, 1, 4),
    _AppnFrSvcMaximumCir_Type()
)
appnFrSvcMaximumCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnFrSvcMaximumCir.setStatus("mandatory")
_AppnFrSvcOperationalTable_Object = MibTable
appnFrSvcOperationalTable = _AppnFrSvcOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 18, 12)
)
if mibBuilder.loadTexts:
    appnFrSvcOperationalTable.setStatus("mandatory")
_AppnFrSvcOperationalEntry_Object = MibTableRow
appnFrSvcOperationalEntry = _AppnFrSvcOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 18, 12, 1)
)
appnFrSvcOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnFrSvcIndex"),
)
if mibBuilder.loadTexts:
    appnFrSvcOperationalEntry.setStatus("mandatory")


class _AppnFrSvcCurrentNumberOfSvcCalls_Type(Gauge32):
    """Custom type appnFrSvcCurrentNumberOfSvcCalls based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3072),
    )


_AppnFrSvcCurrentNumberOfSvcCalls_Type.__name__ = "Gauge32"
_AppnFrSvcCurrentNumberOfSvcCalls_Object = MibTableColumn
appnFrSvcCurrentNumberOfSvcCalls = _AppnFrSvcCurrentNumberOfSvcCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 18, 12, 1, 1),
    _AppnFrSvcCurrentNumberOfSvcCalls_Type()
)
appnFrSvcCurrentNumberOfSvcCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnFrSvcCurrentNumberOfSvcCalls.setStatus("mandatory")
_AppnCn_ObjectIdentity = ObjectIdentity
appnCn = _AppnCn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 19)
)
_AppnCnRowStatusTable_Object = MibTable
appnCnRowStatusTable = _AppnCnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 19, 1)
)
if mibBuilder.loadTexts:
    appnCnRowStatusTable.setStatus("mandatory")
_AppnCnRowStatusEntry_Object = MibTableRow
appnCnRowStatusEntry = _AppnCnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 19, 1, 1)
)
appnCnRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnCnIndex"),
)
if mibBuilder.loadTexts:
    appnCnRowStatusEntry.setStatus("mandatory")
_AppnCnRowStatus_Type = RowStatus
_AppnCnRowStatus_Object = MibTableColumn
appnCnRowStatus = _AppnCnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 19, 1, 1, 1),
    _AppnCnRowStatus_Type()
)
appnCnRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCnRowStatus.setStatus("mandatory")
_AppnCnComponentName_Type = DisplayString
_AppnCnComponentName_Object = MibTableColumn
appnCnComponentName = _AppnCnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 19, 1, 1, 2),
    _AppnCnComponentName_Type()
)
appnCnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCnComponentName.setStatus("mandatory")
_AppnCnStorageType_Type = StorageType
_AppnCnStorageType_Object = MibTableColumn
appnCnStorageType = _AppnCnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 19, 1, 1, 4),
    _AppnCnStorageType_Type()
)
appnCnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCnStorageType.setStatus("mandatory")


class _AppnCnIndex_Type(AsciiStringIndex):
    """Custom type appnCnIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppnCnIndex_Type.__name__ = "AsciiStringIndex"
_AppnCnIndex_Object = MibTableColumn
appnCnIndex = _AppnCnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 19, 1, 1, 10),
    _AppnCnIndex_Type()
)
appnCnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnCnIndex.setStatus("mandatory")
_AppnCnOperTable_Object = MibTable
appnCnOperTable = _AppnCnOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 19, 5)
)
if mibBuilder.loadTexts:
    appnCnOperTable.setStatus("mandatory")
_AppnCnOperEntry_Object = MibTableRow
appnCnOperEntry = _AppnCnOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 19, 5, 1)
)
appnCnOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnCnIndex"),
)
if mibBuilder.loadTexts:
    appnCnOperEntry.setStatus("mandatory")


class _AppnCnNumberActivePorts_Type(Gauge32):
    """Custom type appnCnNumberActivePorts based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AppnCnNumberActivePorts_Type.__name__ = "Gauge32"
_AppnCnNumberActivePorts_Object = MibTableColumn
appnCnNumberActivePorts = _AppnCnNumberActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 19, 5, 1, 219),
    _AppnCnNumberActivePorts_Type()
)
appnCnNumberActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCnNumberActivePorts.setStatus("mandatory")
_AppnProcessParmsTable_Object = MibTable
appnProcessParmsTable = _AppnProcessParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 100)
)
if mibBuilder.loadTexts:
    appnProcessParmsTable.setStatus("mandatory")
_AppnProcessParmsEntry_Object = MibTableRow
appnProcessParmsEntry = _AppnProcessParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 100, 1)
)
appnProcessParmsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
)
if mibBuilder.loadTexts:
    appnProcessParmsEntry.setStatus("mandatory")
_AppnLogicalProcessor_Type = Link
_AppnLogicalProcessor_Object = MibTableColumn
appnLogicalProcessor = _AppnLogicalProcessor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 100, 1, 1),
    _AppnLogicalProcessor_Type()
)
appnLogicalProcessor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnLogicalProcessor.setStatus("mandatory")


class _AppnMaximumSvcs_Type(Unsigned32):
    """Custom type appnMaximumSvcs based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AppnMaximumSvcs_Type.__name__ = "Unsigned32"
_AppnMaximumSvcs_Object = MibTableColumn
appnMaximumSvcs = _AppnMaximumSvcs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 100, 1, 22),
    _AppnMaximumSvcs_Type()
)
appnMaximumSvcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnMaximumSvcs.setStatus("mandatory")


class _AppnMaximumLinkStations_Type(Unsigned32):
    """Custom type appnMaximumLinkStations based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AppnMaximumLinkStations_Type.__name__ = "Unsigned32"
_AppnMaximumLinkStations_Object = MibTableColumn
appnMaximumLinkStations = _AppnMaximumLinkStations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 100, 1, 23),
    _AppnMaximumLinkStations_Type()
)
appnMaximumLinkStations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnMaximumLinkStations.setStatus("mandatory")
_AppnControlPointCreateParmsTable_Object = MibTable
appnControlPointCreateParmsTable = _AppnControlPointCreateParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 101)
)
if mibBuilder.loadTexts:
    appnControlPointCreateParmsTable.setStatus("mandatory")
_AppnControlPointCreateParmsEntry_Object = MibTableRow
appnControlPointCreateParmsEntry = _AppnControlPointCreateParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 101, 1)
)
appnControlPointCreateParmsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
)
if mibBuilder.loadTexts:
    appnControlPointCreateParmsEntry.setStatus("mandatory")


class _AppnFqCpName_Type(AsciiString):
    """Custom type appnFqCpName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_AppnFqCpName_Type.__name__ = "AsciiString"
_AppnFqCpName_Object = MibTableColumn
appnFqCpName = _AppnFqCpName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 101, 1, 1),
    _AppnFqCpName_Type()
)
appnFqCpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnFqCpName.setStatus("mandatory")


class _AppnBlockNumber_Type(Hex):
    """Custom type appnBlockNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AppnBlockNumber_Type.__name__ = "Hex"
_AppnBlockNumber_Object = MibTableColumn
appnBlockNumber = _AppnBlockNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 101, 1, 3),
    _AppnBlockNumber_Type()
)
appnBlockNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnBlockNumber.setStatus("mandatory")


class _AppnIdNumber_Type(Hex):
    """Custom type appnIdNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_AppnIdNumber_Type.__name__ = "Hex"
_AppnIdNumber_Object = MibTableColumn
appnIdNumber = _AppnIdNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 101, 1, 4),
    _AppnIdNumber_Type()
)
appnIdNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnIdNumber.setStatus("mandatory")


class _AppnRouteAdditionResistance_Type(Unsigned32):
    """Custom type appnRouteAdditionResistance based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnRouteAdditionResistance_Type.__name__ = "Unsigned32"
_AppnRouteAdditionResistance_Object = MibTableColumn
appnRouteAdditionResistance = _AppnRouteAdditionResistance_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 101, 1, 5),
    _AppnRouteAdditionResistance_Type()
)
appnRouteAdditionResistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnRouteAdditionResistance.setStatus("mandatory")


class _AppnFeatures_Type(OctetString):
    """Custom type appnFeatures based on OctetString"""
    defaultHexValue = "80"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AppnFeatures_Type.__name__ = "OctetString"
_AppnFeatures_Object = MibTableColumn
appnFeatures = _AppnFeatures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 101, 1, 6),
    _AppnFeatures_Type()
)
appnFeatures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnFeatures.setStatus("mandatory")


class _AppnMaximumLocates_Type(Unsigned32):
    """Custom type appnMaximumLocates based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnMaximumLocates_Type.__name__ = "Unsigned32"
_AppnMaximumLocates_Object = MibTableColumn
appnMaximumLocates = _AppnMaximumLocates_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 101, 1, 7),
    _AppnMaximumLocates_Type()
)
appnMaximumLocates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnMaximumLocates.setStatus("mandatory")


class _AppnMaximumDirectorySize_Type(Unsigned32):
    """Custom type appnMaximumDirectorySize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnMaximumDirectorySize_Type.__name__ = "Unsigned32"
_AppnMaximumDirectorySize_Object = MibTableColumn
appnMaximumDirectorySize = _AppnMaximumDirectorySize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 101, 1, 8),
    _AppnMaximumDirectorySize_Type()
)
appnMaximumDirectorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnMaximumDirectorySize.setStatus("mandatory")


class _AppnMdsTxAlertQueueSize_Type(Unsigned32):
    """Custom type appnMdsTxAlertQueueSize based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnMdsTxAlertQueueSize_Type.__name__ = "Unsigned32"
_AppnMdsTxAlertQueueSize_Object = MibTableColumn
appnMdsTxAlertQueueSize = _AppnMdsTxAlertQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 101, 1, 9),
    _AppnMdsTxAlertQueueSize_Type()
)
appnMdsTxAlertQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnMdsTxAlertQueueSize.setStatus("mandatory")


class _AppnTreeCacheSize_Type(Unsigned32):
    """Custom type appnTreeCacheSize based on Unsigned32"""
    defaultValue = 40

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 65535),
    )


_AppnTreeCacheSize_Type.__name__ = "Unsigned32"
_AppnTreeCacheSize_Object = MibTableColumn
appnTreeCacheSize = _AppnTreeCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 101, 1, 10),
    _AppnTreeCacheSize_Type()
)
appnTreeCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnTreeCacheSize.setStatus("mandatory")


class _AppnTreeCacheUseLimit_Type(Unsigned32):
    """Custom type appnTreeCacheUseLimit based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AppnTreeCacheUseLimit_Type.__name__ = "Unsigned32"
_AppnTreeCacheUseLimit_Object = MibTableColumn
appnTreeCacheUseLimit = _AppnTreeCacheUseLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 101, 1, 11),
    _AppnTreeCacheUseLimit_Type()
)
appnTreeCacheUseLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnTreeCacheUseLimit.setStatus("mandatory")


class _AppnMaximumTopologyNodes_Type(Unsigned32):
    """Custom type appnMaximumTopologyNodes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnMaximumTopologyNodes_Type.__name__ = "Unsigned32"
_AppnMaximumTopologyNodes_Object = MibTableColumn
appnMaximumTopologyNodes = _AppnMaximumTopologyNodes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 101, 1, 12),
    _AppnMaximumTopologyNodes_Type()
)
appnMaximumTopologyNodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnMaximumTopologyNodes.setStatus("mandatory")


class _AppnMaximumTopologyTgs_Type(Unsigned32):
    """Custom type appnMaximumTopologyTgs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnMaximumTopologyTgs_Type.__name__ = "Unsigned32"
_AppnMaximumTopologyTgs_Object = MibTableColumn
appnMaximumTopologyTgs = _AppnMaximumTopologyTgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 101, 1, 13),
    _AppnMaximumTopologyTgs_Type()
)
appnMaximumTopologyTgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnMaximumTopologyTgs.setStatus("mandatory")


class _AppnMaximumIsrSessions_Type(Unsigned32):
    """Custom type appnMaximumIsrSessions based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 65535),
    )


_AppnMaximumIsrSessions_Type.__name__ = "Unsigned32"
_AppnMaximumIsrSessions_Object = MibTableColumn
appnMaximumIsrSessions = _AppnMaximumIsrSessions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 101, 1, 14),
    _AppnMaximumIsrSessions_Type()
)
appnMaximumIsrSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnMaximumIsrSessions.setStatus("mandatory")


class _AppnIsrUpperCongestionThreshold_Type(Unsigned32):
    """Custom type appnIsrUpperCongestionThreshold based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnIsrUpperCongestionThreshold_Type.__name__ = "Unsigned32"
_AppnIsrUpperCongestionThreshold_Object = MibTableColumn
appnIsrUpperCongestionThreshold = _AppnIsrUpperCongestionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 101, 1, 15),
    _AppnIsrUpperCongestionThreshold_Type()
)
appnIsrUpperCongestionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnIsrUpperCongestionThreshold.setStatus("mandatory")


class _AppnIsrLowerCongestionThreshold_Type(Unsigned32):
    """Custom type appnIsrLowerCongestionThreshold based on Unsigned32"""
    defaultValue = 400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnIsrLowerCongestionThreshold_Type.__name__ = "Unsigned32"
_AppnIsrLowerCongestionThreshold_Object = MibTableColumn
appnIsrLowerCongestionThreshold = _AppnIsrLowerCongestionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 101, 1, 16),
    _AppnIsrLowerCongestionThreshold_Type()
)
appnIsrLowerCongestionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnIsrLowerCongestionThreshold.setStatus("mandatory")


class _AppnIsrMaxRuSize_Type(Unsigned32):
    """Custom type appnIsrMaxRuSize based on Unsigned32"""
    defaultValue = 4096

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnIsrMaxRuSize_Type.__name__ = "Unsigned32"
_AppnIsrMaxRuSize_Object = MibTableColumn
appnIsrMaxRuSize = _AppnIsrMaxRuSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 101, 1, 17),
    _AppnIsrMaxRuSize_Type()
)
appnIsrMaxRuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnIsrMaxRuSize.setStatus("mandatory")


class _AppnIsrRxPacingWindow_Type(Unsigned32):
    """Custom type appnIsrRxPacingWindow based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AppnIsrRxPacingWindow_Type.__name__ = "Unsigned32"
_AppnIsrRxPacingWindow_Object = MibTableColumn
appnIsrRxPacingWindow = _AppnIsrRxPacingWindow_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 101, 1, 18),
    _AppnIsrRxPacingWindow_Type()
)
appnIsrRxPacingWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnIsrRxPacingWindow.setStatus("mandatory")


class _AppnLocateTimeout_Type(Unsigned32):
    """Custom type appnLocateTimeout based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AppnLocateTimeout_Type.__name__ = "Unsigned32"
_AppnLocateTimeout_Object = MibTableColumn
appnLocateTimeout = _AppnLocateTimeout_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 101, 1, 19),
    _AppnLocateTimeout_Type()
)
appnLocateTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnLocateTimeout.setStatus("mandatory")


class _AppnHprSupport_Type(Integer32):
    """Custom type appnHprSupport based on Integer32"""
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


_AppnHprSupport_Type.__name__ = "Integer32"
_AppnHprSupport_Object = MibTableColumn
appnHprSupport = _AppnHprSupport_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 101, 1, 20),
    _AppnHprSupport_Type()
)
appnHprSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnHprSupport.setStatus("mandatory")


class _AppnDlurSupport_Type(Integer32):
    """Custom type appnDlurSupport based on Integer32"""
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


_AppnDlurSupport_Type.__name__ = "Integer32"
_AppnDlurSupport_Object = MibTableColumn
appnDlurSupport = _AppnDlurSupport_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 101, 1, 21),
    _AppnDlurSupport_Type()
)
appnDlurSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnDlurSupport.setStatus("mandatory")
_AppnStateTable_Object = MibTable
appnStateTable = _AppnStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 102)
)
if mibBuilder.loadTexts:
    appnStateTable.setStatus("mandatory")
_AppnStateEntry_Object = MibTableRow
appnStateEntry = _AppnStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 102, 1)
)
appnStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
)
if mibBuilder.loadTexts:
    appnStateEntry.setStatus("mandatory")


class _AppnAdminState_Type(Integer32):
    """Custom type appnAdminState based on Integer32"""
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


_AppnAdminState_Type.__name__ = "Integer32"
_AppnAdminState_Object = MibTableColumn
appnAdminState = _AppnAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 102, 1, 1),
    _AppnAdminState_Type()
)
appnAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnAdminState.setStatus("mandatory")


class _AppnOperationalState_Type(Integer32):
    """Custom type appnOperationalState based on Integer32"""
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


_AppnOperationalState_Type.__name__ = "Integer32"
_AppnOperationalState_Object = MibTableColumn
appnOperationalState = _AppnOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 102, 1, 2),
    _AppnOperationalState_Type()
)
appnOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnOperationalState.setStatus("mandatory")


class _AppnUsageState_Type(Integer32):
    """Custom type appnUsageState based on Integer32"""
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


_AppnUsageState_Type.__name__ = "Integer32"
_AppnUsageState_Object = MibTableColumn
appnUsageState = _AppnUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 102, 1, 3),
    _AppnUsageState_Type()
)
appnUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnUsageState.setStatus("mandatory")
_AppnOperationalTable_Object = MibTable
appnOperationalTable = _AppnOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 103)
)
if mibBuilder.loadTexts:
    appnOperationalTable.setStatus("mandatory")
_AppnOperationalEntry_Object = MibTableRow
appnOperationalEntry = _AppnOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 103, 1)
)
appnOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AppnMIB", "appnIndex"),
)
if mibBuilder.loadTexts:
    appnOperationalEntry.setStatus("mandatory")


class _AppnUpTime_Type(Unsigned32):
    """Custom type appnUpTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AppnUpTime_Type.__name__ = "Unsigned32"
_AppnUpTime_Object = MibTableColumn
appnUpTime = _AppnUpTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 103, 1, 1),
    _AppnUpTime_Type()
)
appnUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnUpTime.setStatus("mandatory")


class _AppnHeapSpaceLimit_Type(Gauge32):
    """Custom type appnHeapSpaceLimit based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AppnHeapSpaceLimit_Type.__name__ = "Gauge32"
_AppnHeapSpaceLimit_Object = MibTableColumn
appnHeapSpaceLimit = _AppnHeapSpaceLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 103, 1, 2),
    _AppnHeapSpaceLimit_Type()
)
appnHeapSpaceLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnHeapSpaceLimit.setStatus("mandatory")


class _AppnHeapSpaceCurrent_Type(Gauge32):
    """Custom type appnHeapSpaceCurrent based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AppnHeapSpaceCurrent_Type.__name__ = "Gauge32"
_AppnHeapSpaceCurrent_Object = MibTableColumn
appnHeapSpaceCurrent = _AppnHeapSpaceCurrent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 103, 1, 3),
    _AppnHeapSpaceCurrent_Type()
)
appnHeapSpaceCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnHeapSpaceCurrent.setStatus("mandatory")


class _AppnMemWarningThreshold_Type(Unsigned32):
    """Custom type appnMemWarningThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AppnMemWarningThreshold_Type.__name__ = "Unsigned32"
_AppnMemWarningThreshold_Object = MibTableColumn
appnMemWarningThreshold = _AppnMemWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 103, 1, 4),
    _AppnMemWarningThreshold_Type()
)
appnMemWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnMemWarningThreshold.setStatus("mandatory")


class _AppnMemCriticalThreshold_Type(Unsigned32):
    """Custom type appnMemCriticalThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AppnMemCriticalThreshold_Type.__name__ = "Unsigned32"
_AppnMemCriticalThreshold_Object = MibTableColumn
appnMemCriticalThreshold = _AppnMemCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 103, 1, 5),
    _AppnMemCriticalThreshold_Type()
)
appnMemCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnMemCriticalThreshold.setStatus("mandatory")


class _AppnNnFunctionsSupported_Type(OctetString):
    """Custom type appnNnFunctionsSupported based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AppnNnFunctionsSupported_Type.__name__ = "OctetString"
_AppnNnFunctionsSupported_Object = MibTableColumn
appnNnFunctionsSupported = _AppnNnFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 103, 1, 6),
    _AppnNnFunctionsSupported_Type()
)
appnNnFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnFunctionsSupported.setStatus("mandatory")


class _AppnGeneralFunctionsSupported_Type(OctetString):
    """Custom type appnGeneralFunctionsSupported based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AppnGeneralFunctionsSupported_Type.__name__ = "OctetString"
_AppnGeneralFunctionsSupported_Object = MibTableColumn
appnGeneralFunctionsSupported = _AppnGeneralFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 103, 1, 7),
    _AppnGeneralFunctionsSupported_Type()
)
appnGeneralFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnGeneralFunctionsSupported.setStatus("mandatory")


class _AppnStatus_Type(OctetString):
    """Custom type appnStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AppnStatus_Type.__name__ = "OctetString"
_AppnStatus_Object = MibTableColumn
appnStatus = _AppnStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 103, 1, 8),
    _AppnStatus_Type()
)
appnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnStatus.setStatus("mandatory")


class _AppnFlowReductionSequenceNumber_Type(Unsigned32):
    """Custom type appnFlowReductionSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AppnFlowReductionSequenceNumber_Type.__name__ = "Unsigned32"
_AppnFlowReductionSequenceNumber_Object = MibTableColumn
appnFlowReductionSequenceNumber = _AppnFlowReductionSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 103, 1, 9),
    _AppnFlowReductionSequenceNumber_Type()
)
appnFlowReductionSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnFlowReductionSequenceNumber.setStatus("mandatory")


class _AppnResourceSequenceNumber_Type(Unsigned32):
    """Custom type appnResourceSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AppnResourceSequenceNumber_Type.__name__ = "Unsigned32"
_AppnResourceSequenceNumber_Object = MibTableColumn
appnResourceSequenceNumber = _AppnResourceSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 103, 1, 10),
    _AppnResourceSequenceNumber_Type()
)
appnResourceSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnResourceSequenceNumber.setStatus("mandatory")
_AppnDefinedLsGoodXids_Type = PassportCounter64
_AppnDefinedLsGoodXids_Object = MibTableColumn
appnDefinedLsGoodXids = _AppnDefinedLsGoodXids_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 103, 1, 11),
    _AppnDefinedLsGoodXids_Type()
)
appnDefinedLsGoodXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDefinedLsGoodXids.setStatus("mandatory")
_AppnDefinedLsBadXids_Type = PassportCounter64
_AppnDefinedLsBadXids_Object = MibTableColumn
appnDefinedLsBadXids = _AppnDefinedLsBadXids_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 103, 1, 12),
    _AppnDefinedLsBadXids_Type()
)
appnDefinedLsBadXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDefinedLsBadXids.setStatus("mandatory")
_AppnDynamicLsGoodXids_Type = PassportCounter64
_AppnDynamicLsGoodXids_Object = MibTableColumn
appnDynamicLsGoodXids = _AppnDynamicLsGoodXids_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 103, 1, 13),
    _AppnDynamicLsGoodXids_Type()
)
appnDynamicLsGoodXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDynamicLsGoodXids.setStatus("mandatory")
_AppnDynamicLsBadXids_Type = PassportCounter64
_AppnDynamicLsBadXids_Object = MibTableColumn
appnDynamicLsBadXids = _AppnDynamicLsBadXids_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 103, 1, 14),
    _AppnDynamicLsBadXids_Type()
)
appnDynamicLsBadXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDynamicLsBadXids.setStatus("mandatory")


class _AppnActiveSvcs_Type(Unsigned32):
    """Custom type appnActiveSvcs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AppnActiveSvcs_Type.__name__ = "Unsigned32"
_AppnActiveSvcs_Object = MibTableColumn
appnActiveSvcs = _AppnActiveSvcs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 103, 1, 15),
    _AppnActiveSvcs_Type()
)
appnActiveSvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnActiveSvcs.setStatus("mandatory")


class _AppnActiveLinkStations_Type(Unsigned32):
    """Custom type appnActiveLinkStations based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AppnActiveLinkStations_Type.__name__ = "Unsigned32"
_AppnActiveLinkStations_Object = MibTableColumn
appnActiveLinkStations = _AppnActiveLinkStations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 110, 103, 1, 16),
    _AppnActiveLinkStations_Type()
)
appnActiveLinkStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnActiveLinkStations.setStatus("mandatory")
_AppnMIB_ObjectIdentity = ObjectIdentity
appnMIB = _AppnMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 29)
)
_AppnGroup_ObjectIdentity = ObjectIdentity
appnGroup = _AppnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 29, 1)
)
_AppnGroupBE_ObjectIdentity = ObjectIdentity
appnGroupBE = _AppnGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 29, 1, 5)
)
_AppnGroupBE01_ObjectIdentity = ObjectIdentity
appnGroupBE01 = _AppnGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 29, 1, 5, 2)
)
_AppnGroupBE01A_ObjectIdentity = ObjectIdentity
appnGroupBE01A = _AppnGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 29, 1, 5, 2, 2)
)
_AppnCapabilities_ObjectIdentity = ObjectIdentity
appnCapabilities = _AppnCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 29, 3)
)
_AppnCapabilitiesBE_ObjectIdentity = ObjectIdentity
appnCapabilitiesBE = _AppnCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 29, 3, 5)
)
_AppnCapabilitiesBE01_ObjectIdentity = ObjectIdentity
appnCapabilitiesBE01 = _AppnCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 29, 3, 5, 2)
)
_AppnCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
appnCapabilitiesBE01A = _AppnCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 29, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-AppnMIB",
    **{"appn": appn,
       "appnRowStatusTable": appnRowStatusTable,
       "appnRowStatusEntry": appnRowStatusEntry,
       "appnRowStatus": appnRowStatus,
       "appnComponentName": appnComponentName,
       "appnStorageType": appnStorageType,
       "appnIndex": appnIndex,
       "appnDna": appnDna,
       "appnDnaRowStatusTable": appnDnaRowStatusTable,
       "appnDnaRowStatusEntry": appnDnaRowStatusEntry,
       "appnDnaRowStatus": appnDnaRowStatus,
       "appnDnaComponentName": appnDnaComponentName,
       "appnDnaStorageType": appnDnaStorageType,
       "appnDnaIndex": appnDnaIndex,
       "appnDnaHgM": appnDnaHgM,
       "appnDnaHgMRowStatusTable": appnDnaHgMRowStatusTable,
       "appnDnaHgMRowStatusEntry": appnDnaHgMRowStatusEntry,
       "appnDnaHgMRowStatus": appnDnaHgMRowStatus,
       "appnDnaHgMComponentName": appnDnaHgMComponentName,
       "appnDnaHgMStorageType": appnDnaHgMStorageType,
       "appnDnaHgMIndex": appnDnaHgMIndex,
       "appnDnaHgMHgAddr": appnDnaHgMHgAddr,
       "appnDnaHgMHgAddrRowStatusTable": appnDnaHgMHgAddrRowStatusTable,
       "appnDnaHgMHgAddrRowStatusEntry": appnDnaHgMHgAddrRowStatusEntry,
       "appnDnaHgMHgAddrRowStatus": appnDnaHgMHgAddrRowStatus,
       "appnDnaHgMHgAddrComponentName": appnDnaHgMHgAddrComponentName,
       "appnDnaHgMHgAddrStorageType": appnDnaHgMHgAddrStorageType,
       "appnDnaHgMHgAddrIndex": appnDnaHgMHgAddrIndex,
       "appnDnaHgMHgAddrAddrTable": appnDnaHgMHgAddrAddrTable,
       "appnDnaHgMHgAddrAddrEntry": appnDnaHgMHgAddrAddrEntry,
       "appnDnaHgMHgAddrNumberingPlanIndicator": appnDnaHgMHgAddrNumberingPlanIndicator,
       "appnDnaHgMHgAddrDataNetworkAddress": appnDnaHgMHgAddrDataNetworkAddress,
       "appnDnaHgMIfTable": appnDnaHgMIfTable,
       "appnDnaHgMIfEntry": appnDnaHgMIfEntry,
       "appnDnaHgMAvailabilityUpdateThreshold": appnDnaHgMAvailabilityUpdateThreshold,
       "appnDnaHgMOpTable": appnDnaHgMOpTable,
       "appnDnaHgMOpEntry": appnDnaHgMOpEntry,
       "appnDnaHgMMaxAvailableChannels": appnDnaHgMMaxAvailableChannels,
       "appnDnaHgMAvailableChannels": appnDnaHgMAvailableChannels,
       "appnDnaHgMAvailabilityDelta": appnDnaHgMAvailabilityDelta,
       "appnDnaCug": appnDnaCug,
       "appnDnaCugRowStatusTable": appnDnaCugRowStatusTable,
       "appnDnaCugRowStatusEntry": appnDnaCugRowStatusEntry,
       "appnDnaCugRowStatus": appnDnaCugRowStatus,
       "appnDnaCugComponentName": appnDnaCugComponentName,
       "appnDnaCugStorageType": appnDnaCugStorageType,
       "appnDnaCugIndex": appnDnaCugIndex,
       "appnDnaCugCugOptionsTable": appnDnaCugCugOptionsTable,
       "appnDnaCugCugOptionsEntry": appnDnaCugCugOptionsEntry,
       "appnDnaCugType": appnDnaCugType,
       "appnDnaCugDnic": appnDnaCugDnic,
       "appnDnaCugInterlockCode": appnDnaCugInterlockCode,
       "appnDnaCugPreferential": appnDnaCugPreferential,
       "appnDnaCugOutCalls": appnDnaCugOutCalls,
       "appnDnaCugIncCalls": appnDnaCugIncCalls,
       "appnDnaCugPrivileged": appnDnaCugPrivileged,
       "appnDnaAddressTable": appnDnaAddressTable,
       "appnDnaAddressEntry": appnDnaAddressEntry,
       "appnDnaNumberingPlanIndicator": appnDnaNumberingPlanIndicator,
       "appnDnaDataNetworkAddress": appnDnaDataNetworkAddress,
       "appnDnaOutgoingOptionsTable": appnDnaOutgoingOptionsTable,
       "appnDnaOutgoingOptionsEntry": appnDnaOutgoingOptionsEntry,
       "appnDnaOutDefaultPriority": appnDnaOutDefaultPriority,
       "appnDnaOutDefaultPathSensitivity": appnDnaOutDefaultPathSensitivity,
       "appnDnaOutPathSensitivityOverRide": appnDnaOutPathSensitivityOverRide,
       "appnDnaOutDefaultPathReliability": appnDnaOutDefaultPathReliability,
       "appnDnaOutAccess": appnDnaOutAccess,
       "appnDnaDefaultTransferPriority": appnDnaDefaultTransferPriority,
       "appnDnaTransferPriorityOverRide": appnDnaTransferPriorityOverRide,
       "appnDnaIncomingOptionsTable": appnDnaIncomingOptionsTable,
       "appnDnaIncomingOptionsEntry": appnDnaIncomingOptionsEntry,
       "appnDnaIncAccess": appnDnaIncAccess,
       "appnDnaCallOptionsTable": appnDnaCallOptionsTable,
       "appnDnaCallOptionsEntry": appnDnaCallOptionsEntry,
       "appnDnaDefaultRecvFrmNetworkThruputClass": appnDnaDefaultRecvFrmNetworkThruputClass,
       "appnDnaDefaultSendToNetworkThruputClass": appnDnaDefaultSendToNetworkThruputClass,
       "appnDnaDefaultRecvFrmNetworkWindowSize": appnDnaDefaultRecvFrmNetworkWindowSize,
       "appnDnaDefaultSendToNetworkWindowSize": appnDnaDefaultSendToNetworkWindowSize,
       "appnDnaAccountClass": appnDnaAccountClass,
       "appnDnaAccountCollection": appnDnaAccountCollection,
       "appnDnaServiceExchange": appnDnaServiceExchange,
       "appnDlci": appnDlci,
       "appnDlciRowStatusTable": appnDlciRowStatusTable,
       "appnDlciRowStatusEntry": appnDlciRowStatusEntry,
       "appnDlciRowStatus": appnDlciRowStatus,
       "appnDlciComponentName": appnDlciComponentName,
       "appnDlciStorageType": appnDlciStorageType,
       "appnDlciIndex": appnDlciIndex,
       "appnDlciDc": appnDlciDc,
       "appnDlciDcRowStatusTable": appnDlciDcRowStatusTable,
       "appnDlciDcRowStatusEntry": appnDlciDcRowStatusEntry,
       "appnDlciDcRowStatus": appnDlciDcRowStatus,
       "appnDlciDcComponentName": appnDlciDcComponentName,
       "appnDlciDcStorageType": appnDlciDcStorageType,
       "appnDlciDcIndex": appnDlciDcIndex,
       "appnDlciDcOptionsTable": appnDlciDcOptionsTable,
       "appnDlciDcOptionsEntry": appnDlciDcOptionsEntry,
       "appnDlciDcRemoteNpi": appnDlciDcRemoteNpi,
       "appnDlciDcRemoteDna": appnDlciDcRemoteDna,
       "appnDlciDcRemoteDlci": appnDlciDcRemoteDlci,
       "appnDlciDcType": appnDlciDcType,
       "appnDlciDcTransferPriority": appnDlciDcTransferPriority,
       "appnDlciDcDiscardPriority": appnDlciDcDiscardPriority,
       "appnDlciDcNfaTable": appnDlciDcNfaTable,
       "appnDlciDcNfaEntry": appnDlciDcNfaEntry,
       "appnDlciDcNfaIndex": appnDlciDcNfaIndex,
       "appnDlciDcNfaValue": appnDlciDcNfaValue,
       "appnDlciDcNfaRowStatus": appnDlciDcNfaRowStatus,
       "appnDlciVc": appnDlciVc,
       "appnDlciVcRowStatusTable": appnDlciVcRowStatusTable,
       "appnDlciVcRowStatusEntry": appnDlciVcRowStatusEntry,
       "appnDlciVcRowStatus": appnDlciVcRowStatus,
       "appnDlciVcComponentName": appnDlciVcComponentName,
       "appnDlciVcStorageType": appnDlciVcStorageType,
       "appnDlciVcIndex": appnDlciVcIndex,
       "appnDlciVcCadTable": appnDlciVcCadTable,
       "appnDlciVcCadEntry": appnDlciVcCadEntry,
       "appnDlciVcType": appnDlciVcType,
       "appnDlciVcState": appnDlciVcState,
       "appnDlciVcPreviousState": appnDlciVcPreviousState,
       "appnDlciVcDiagnosticCode": appnDlciVcDiagnosticCode,
       "appnDlciVcPreviousDiagnosticCode": appnDlciVcPreviousDiagnosticCode,
       "appnDlciVcCalledNpi": appnDlciVcCalledNpi,
       "appnDlciVcCalledDna": appnDlciVcCalledDna,
       "appnDlciVcCalledLcn": appnDlciVcCalledLcn,
       "appnDlciVcCallingNpi": appnDlciVcCallingNpi,
       "appnDlciVcCallingDna": appnDlciVcCallingDna,
       "appnDlciVcCallingLcn": appnDlciVcCallingLcn,
       "appnDlciVcAccountingEnabled": appnDlciVcAccountingEnabled,
       "appnDlciVcFastSelectCall": appnDlciVcFastSelectCall,
       "appnDlciVcPathReliability": appnDlciVcPathReliability,
       "appnDlciVcAccountingEnd": appnDlciVcAccountingEnd,
       "appnDlciVcPriority": appnDlciVcPriority,
       "appnDlciVcSegmentSize": appnDlciVcSegmentSize,
       "appnDlciVcMaxSubnetPktSize": appnDlciVcMaxSubnetPktSize,
       "appnDlciVcRcosToNetwork": appnDlciVcRcosToNetwork,
       "appnDlciVcRcosFromNetwork": appnDlciVcRcosFromNetwork,
       "appnDlciVcEmissionPriorityToNetwork": appnDlciVcEmissionPriorityToNetwork,
       "appnDlciVcEmissionPriorityFromNetwork": appnDlciVcEmissionPriorityFromNetwork,
       "appnDlciVcDataPath": appnDlciVcDataPath,
       "appnDlciVcIntdTable": appnDlciVcIntdTable,
       "appnDlciVcIntdEntry": appnDlciVcIntdEntry,
       "appnDlciVcCallReferenceNumber": appnDlciVcCallReferenceNumber,
       "appnDlciVcElapsedTimeTillNow": appnDlciVcElapsedTimeTillNow,
       "appnDlciVcSegmentsRx": appnDlciVcSegmentsRx,
       "appnDlciVcSegmentsSent": appnDlciVcSegmentsSent,
       "appnDlciVcStartTime": appnDlciVcStartTime,
       "appnDlciVcFrdTable": appnDlciVcFrdTable,
       "appnDlciVcFrdEntry": appnDlciVcFrdEntry,
       "appnDlciVcFrmCongestedToSubnet": appnDlciVcFrmCongestedToSubnet,
       "appnDlciVcCannotForwardToSubnet": appnDlciVcCannotForwardToSubnet,
       "appnDlciVcNotDataXferToSubnet": appnDlciVcNotDataXferToSubnet,
       "appnDlciVcOutOfRangeFrmFromSubnet": appnDlciVcOutOfRangeFrmFromSubnet,
       "appnDlciVcCombErrorsFromSubnet": appnDlciVcCombErrorsFromSubnet,
       "appnDlciVcDuplicatesFromSubnet": appnDlciVcDuplicatesFromSubnet,
       "appnDlciVcNotDataXferFromSubnet": appnDlciVcNotDataXferFromSubnet,
       "appnDlciVcFrmLossTimeouts": appnDlciVcFrmLossTimeouts,
       "appnDlciVcOoSeqByteCntExceeded": appnDlciVcOoSeqByteCntExceeded,
       "appnDlciVcPeakOoSeqPktCount": appnDlciVcPeakOoSeqPktCount,
       "appnDlciVcPeakOoSeqFrmForwarded": appnDlciVcPeakOoSeqFrmForwarded,
       "appnDlciVcSendSequenceNumber": appnDlciVcSendSequenceNumber,
       "appnDlciVcPktRetryTimeouts": appnDlciVcPktRetryTimeouts,
       "appnDlciVcPeakRetryQueueSize": appnDlciVcPeakRetryQueueSize,
       "appnDlciVcSubnetRecoveries": appnDlciVcSubnetRecoveries,
       "appnDlciVcOoSeqPktCntExceeded": appnDlciVcOoSeqPktCntExceeded,
       "appnDlciVcPeakOoSeqByteCount": appnDlciVcPeakOoSeqByteCount,
       "appnDlciVcDmepTable": appnDlciVcDmepTable,
       "appnDlciVcDmepEntry": appnDlciVcDmepEntry,
       "appnDlciVcDmepValue": appnDlciVcDmepValue,
       "appnDlciBnnLsDef": appnDlciBnnLsDef,
       "appnDlciBnnLsDefRowStatusTable": appnDlciBnnLsDefRowStatusTable,
       "appnDlciBnnLsDefRowStatusEntry": appnDlciBnnLsDefRowStatusEntry,
       "appnDlciBnnLsDefRowStatus": appnDlciBnnLsDefRowStatus,
       "appnDlciBnnLsDefComponentName": appnDlciBnnLsDefComponentName,
       "appnDlciBnnLsDefStorageType": appnDlciBnnLsDefStorageType,
       "appnDlciBnnLsDefIndex": appnDlciBnnLsDefIndex,
       "appnDlciBnnLsDefProvTable": appnDlciBnnLsDefProvTable,
       "appnDlciBnnLsDefProvEntry": appnDlciBnnLsDefProvEntry,
       "appnDlciBnnLsDefDspuService": appnDlciBnnLsDefDspuService,
       "appnDlciBnnLsDefAdjacentCpName": appnDlciBnnLsDefAdjacentCpName,
       "appnDlciBnnLsDefAdjacentCpType": appnDlciBnnLsDefAdjacentCpType,
       "appnDlciBnnLsDefTgNum": appnDlciBnnLsDefTgNum,
       "appnDlciBnnLsDefDlusName": appnDlciBnnLsDefDlusName,
       "appnDlciBnnLsDefBackupDlusName": appnDlciBnnLsDefBackupDlusName,
       "appnDlciBnnLsDefHprSupported": appnDlciBnnLsDefHprSupported,
       "appnDlciBnnLsDefAdjacentNodeID": appnDlciBnnLsDefAdjacentNodeID,
       "appnDlciBnnLsDefCpCpSessionSupport": appnDlciBnnLsDefCpCpSessionSupport,
       "appnDlciBnnLsDefMaxTxBtuSize": appnDlciBnnLsDefMaxTxBtuSize,
       "appnDlciBnnLsDefLsRole": appnDlciBnnLsDefLsRole,
       "appnDlciSp": appnDlciSp,
       "appnDlciSpRowStatusTable": appnDlciSpRowStatusTable,
       "appnDlciSpRowStatusEntry": appnDlciSpRowStatusEntry,
       "appnDlciSpRowStatus": appnDlciSpRowStatus,
       "appnDlciSpComponentName": appnDlciSpComponentName,
       "appnDlciSpStorageType": appnDlciSpStorageType,
       "appnDlciSpIndex": appnDlciSpIndex,
       "appnDlciSpParmsTable": appnDlciSpParmsTable,
       "appnDlciSpParmsEntry": appnDlciSpParmsEntry,
       "appnDlciSpRateEnforcement": appnDlciSpRateEnforcement,
       "appnDlciSpCommittedInformationRate": appnDlciSpCommittedInformationRate,
       "appnDlciSpCommittedBurstSize": appnDlciSpCommittedBurstSize,
       "appnDlciSpExcessBurstSize": appnDlciSpExcessBurstSize,
       "appnDlciSpMeasurementInterval": appnDlciSpMeasurementInterval,
       "appnDlciBanLsDef": appnDlciBanLsDef,
       "appnDlciBanLsDefRowStatusTable": appnDlciBanLsDefRowStatusTable,
       "appnDlciBanLsDefRowStatusEntry": appnDlciBanLsDefRowStatusEntry,
       "appnDlciBanLsDefRowStatus": appnDlciBanLsDefRowStatus,
       "appnDlciBanLsDefComponentName": appnDlciBanLsDefComponentName,
       "appnDlciBanLsDefStorageType": appnDlciBanLsDefStorageType,
       "appnDlciBanLsDefMacIndex": appnDlciBanLsDefMacIndex,
       "appnDlciBanLsDefSapIndex": appnDlciBanLsDefSapIndex,
       "appnDlciBanLsDefProvTable": appnDlciBanLsDefProvTable,
       "appnDlciBanLsDefProvEntry": appnDlciBanLsDefProvEntry,
       "appnDlciBanLsDefDspuService": appnDlciBanLsDefDspuService,
       "appnDlciBanLsDefAdjacentCpName": appnDlciBanLsDefAdjacentCpName,
       "appnDlciBanLsDefAdjacentCpType": appnDlciBanLsDefAdjacentCpType,
       "appnDlciBanLsDefTgNum": appnDlciBanLsDefTgNum,
       "appnDlciBanLsDefDlusName": appnDlciBanLsDefDlusName,
       "appnDlciBanLsDefBackupDlusName": appnDlciBanLsDefBackupDlusName,
       "appnDlciBanLsDefHprSupported": appnDlciBanLsDefHprSupported,
       "appnDlciBanLsDefAdjacentNodeID": appnDlciBanLsDefAdjacentNodeID,
       "appnDlciBanLsDefCpCpSessionSupport": appnDlciBanLsDefCpCpSessionSupport,
       "appnDlciBanLsDefMaxTxBtuSize": appnDlciBanLsDefMaxTxBtuSize,
       "appnDlciBanLsDefLsRole": appnDlciBanLsDefLsRole,
       "appnDlciBan": appnDlciBan,
       "appnDlciBanRowStatusTable": appnDlciBanRowStatusTable,
       "appnDlciBanRowStatusEntry": appnDlciBanRowStatusEntry,
       "appnDlciBanRowStatus": appnDlciBanRowStatus,
       "appnDlciBanComponentName": appnDlciBanComponentName,
       "appnDlciBanStorageType": appnDlciBanStorageType,
       "appnDlciBanIndex": appnDlciBanIndex,
       "appnDlciBanProvTable": appnDlciBanProvTable,
       "appnDlciBanProvEntry": appnDlciBanProvEntry,
       "appnDlciBanLocalMac": appnDlciBanLocalMac,
       "appnDlciBanLocalSap": appnDlciBanLocalSap,
       "appnDlciCn": appnDlciCn,
       "appnDlciCnRowStatusTable": appnDlciCnRowStatusTable,
       "appnDlciCnRowStatusEntry": appnDlciCnRowStatusEntry,
       "appnDlciCnRowStatus": appnDlciCnRowStatus,
       "appnDlciCnComponentName": appnDlciCnComponentName,
       "appnDlciCnStorageType": appnDlciCnStorageType,
       "appnDlciCnIndex": appnDlciCnIndex,
       "appnDlciStateTable": appnDlciStateTable,
       "appnDlciStateEntry": appnDlciStateEntry,
       "appnDlciAdminState": appnDlciAdminState,
       "appnDlciOperationalState": appnDlciOperationalState,
       "appnDlciUsageState": appnDlciUsageState,
       "appnDlciSpOpTable": appnDlciSpOpTable,
       "appnDlciSpOpEntry": appnDlciSpOpEntry,
       "appnDlciRateEnforcement": appnDlciRateEnforcement,
       "appnDlciCommittedInformationRate": appnDlciCommittedInformationRate,
       "appnDlciCommittedBurstSize": appnDlciCommittedBurstSize,
       "appnDlciExcessInformationRate": appnDlciExcessInformationRate,
       "appnDlciExcessBurstSize": appnDlciExcessBurstSize,
       "appnDlciMeasurementInterval": appnDlciMeasurementInterval,
       "appnLcn": appnLcn,
       "appnLcnRowStatusTable": appnLcnRowStatusTable,
       "appnLcnRowStatusEntry": appnLcnRowStatusEntry,
       "appnLcnRowStatus": appnLcnRowStatus,
       "appnLcnComponentName": appnLcnComponentName,
       "appnLcnStorageType": appnLcnStorageType,
       "appnLcnIndex": appnLcnIndex,
       "appnLcnDc": appnLcnDc,
       "appnLcnDcRowStatusTable": appnLcnDcRowStatusTable,
       "appnLcnDcRowStatusEntry": appnLcnDcRowStatusEntry,
       "appnLcnDcRowStatus": appnLcnDcRowStatus,
       "appnLcnDcComponentName": appnLcnDcComponentName,
       "appnLcnDcStorageType": appnLcnDcStorageType,
       "appnLcnDcIndex": appnLcnDcIndex,
       "appnLcnDcOptionsTable": appnLcnDcOptionsTable,
       "appnLcnDcOptionsEntry": appnLcnDcOptionsEntry,
       "appnLcnDcRemoteNpi": appnLcnDcRemoteNpi,
       "appnLcnDcRemoteDna": appnLcnDcRemoteDna,
       "appnLcnDcTransferPriority": appnLcnDcTransferPriority,
       "appnLcnDcDiscardPriority": appnLcnDcDiscardPriority,
       "appnLcnVc": appnLcnVc,
       "appnLcnVcRowStatusTable": appnLcnVcRowStatusTable,
       "appnLcnVcRowStatusEntry": appnLcnVcRowStatusEntry,
       "appnLcnVcRowStatus": appnLcnVcRowStatus,
       "appnLcnVcComponentName": appnLcnVcComponentName,
       "appnLcnVcStorageType": appnLcnVcStorageType,
       "appnLcnVcIndex": appnLcnVcIndex,
       "appnLcnVcCadTable": appnLcnVcCadTable,
       "appnLcnVcCadEntry": appnLcnVcCadEntry,
       "appnLcnVcType": appnLcnVcType,
       "appnLcnVcState": appnLcnVcState,
       "appnLcnVcPreviousState": appnLcnVcPreviousState,
       "appnLcnVcDiagnosticCode": appnLcnVcDiagnosticCode,
       "appnLcnVcPreviousDiagnosticCode": appnLcnVcPreviousDiagnosticCode,
       "appnLcnVcCalledNpi": appnLcnVcCalledNpi,
       "appnLcnVcCalledDna": appnLcnVcCalledDna,
       "appnLcnVcCalledLcn": appnLcnVcCalledLcn,
       "appnLcnVcCallingNpi": appnLcnVcCallingNpi,
       "appnLcnVcCallingDna": appnLcnVcCallingDna,
       "appnLcnVcCallingLcn": appnLcnVcCallingLcn,
       "appnLcnVcAccountingEnabled": appnLcnVcAccountingEnabled,
       "appnLcnVcFastSelectCall": appnLcnVcFastSelectCall,
       "appnLcnVcLocalRxPktSize": appnLcnVcLocalRxPktSize,
       "appnLcnVcLocalTxPktSize": appnLcnVcLocalTxPktSize,
       "appnLcnVcLocalTxWindowSize": appnLcnVcLocalTxWindowSize,
       "appnLcnVcLocalRxWindowSize": appnLcnVcLocalRxWindowSize,
       "appnLcnVcPathReliability": appnLcnVcPathReliability,
       "appnLcnVcAccountingEnd": appnLcnVcAccountingEnd,
       "appnLcnVcPriority": appnLcnVcPriority,
       "appnLcnVcSegmentSize": appnLcnVcSegmentSize,
       "appnLcnVcSubnetTxPktSize": appnLcnVcSubnetTxPktSize,
       "appnLcnVcSubnetTxWindowSize": appnLcnVcSubnetTxWindowSize,
       "appnLcnVcSubnetRxPktSize": appnLcnVcSubnetRxPktSize,
       "appnLcnVcSubnetRxWindowSize": appnLcnVcSubnetRxWindowSize,
       "appnLcnVcMaxSubnetPktSize": appnLcnVcMaxSubnetPktSize,
       "appnLcnVcTransferPriorityToNetwork": appnLcnVcTransferPriorityToNetwork,
       "appnLcnVcTransferPriorityFromNetwork": appnLcnVcTransferPriorityFromNetwork,
       "appnLcnVcIntdTable": appnLcnVcIntdTable,
       "appnLcnVcIntdEntry": appnLcnVcIntdEntry,
       "appnLcnVcCallReferenceNumber": appnLcnVcCallReferenceNumber,
       "appnLcnVcElapsedTimeTillNow": appnLcnVcElapsedTimeTillNow,
       "appnLcnVcSegmentsRx": appnLcnVcSegmentsRx,
       "appnLcnVcSegmentsSent": appnLcnVcSegmentsSent,
       "appnLcnVcStartTime": appnLcnVcStartTime,
       "appnLcnVcStatsTable": appnLcnVcStatsTable,
       "appnLcnVcStatsEntry": appnLcnVcStatsEntry,
       "appnLcnVcAckStackingTimeouts": appnLcnVcAckStackingTimeouts,
       "appnLcnVcOutOfRangeFrmFromSubnet": appnLcnVcOutOfRangeFrmFromSubnet,
       "appnLcnVcDuplicatesFromSubnet": appnLcnVcDuplicatesFromSubnet,
       "appnLcnVcFrmRetryTimeouts": appnLcnVcFrmRetryTimeouts,
       "appnLcnVcPeakRetryQueueSize": appnLcnVcPeakRetryQueueSize,
       "appnLcnVcPeakOoSeqQueueSize": appnLcnVcPeakOoSeqQueueSize,
       "appnLcnVcPeakOoSeqFrmForwarded": appnLcnVcPeakOoSeqFrmForwarded,
       "appnLcnVcPeakStackedAcksRx": appnLcnVcPeakStackedAcksRx,
       "appnLcnVcSubnetRecoveries": appnLcnVcSubnetRecoveries,
       "appnLcnVcWindowClosuresToSubnet": appnLcnVcWindowClosuresToSubnet,
       "appnLcnVcWindowClosuresFromSubnet": appnLcnVcWindowClosuresFromSubnet,
       "appnLcnVcWrTriggers": appnLcnVcWrTriggers,
       "appnLcnStateTable": appnLcnStateTable,
       "appnLcnStateEntry": appnLcnStateEntry,
       "appnLcnAdminState": appnLcnAdminState,
       "appnLcnOperationalState": appnLcnOperationalState,
       "appnLcnUsageState": appnLcnUsageState,
       "appnPort": appnPort,
       "appnPortRowStatusTable": appnPortRowStatusTable,
       "appnPortRowStatusEntry": appnPortRowStatusEntry,
       "appnPortRowStatus": appnPortRowStatus,
       "appnPortComponentName": appnPortComponentName,
       "appnPortStorageType": appnPortStorageType,
       "appnPortIndex": appnPortIndex,
       "appnPortConfigTable": appnPortConfigTable,
       "appnPortConfigEntry": appnPortConfigEntry,
       "appnPortType": appnPortType,
       "appnPortMaxRxBtuSize": appnPortMaxRxBtuSize,
       "appnPortMaxTxBtuSize": appnPortMaxTxBtuSize,
       "appnPortTotLinkActLim": appnPortTotLinkActLim,
       "appnPortInbLinkActLim": appnPortInbLinkActLim,
       "appnPortOutLinkActLim": appnPortOutLinkActLim,
       "appnPortLsRole": appnPortLsRole,
       "appnPortActXidExchLim": appnPortActXidExchLim,
       "appnPortNonactXidExchLim": appnPortNonactXidExchLim,
       "appnPortLsXmitRxCap": appnPortLsXmitRxCap,
       "appnPortMaxIfrmRxWindow": appnPortMaxIfrmRxWindow,
       "appnPortTargetPacingCount": appnPortTargetPacingCount,
       "appnPortOperTable": appnPortOperTable,
       "appnPortOperEntry": appnPortOperEntry,
       "appnPortState": appnPortState,
       "appnPortDlcType": appnPortDlcType,
       "appnPortSimRim": appnPortSimRim,
       "appnPortDefinedLsGoodXids": appnPortDefinedLsGoodXids,
       "appnPortDefinedLsBadXids": appnPortDefinedLsBadXids,
       "appnPortDynLsGoodXids": appnPortDynLsGoodXids,
       "appnPortDynLsBadXids": appnPortDynLsBadXids,
       "appnPortTgCharTable": appnPortTgCharTable,
       "appnPortTgCharEntry": appnPortTgCharEntry,
       "appnPortEffectiveCap": appnPortEffectiveCap,
       "appnPortConnectCost": appnPortConnectCost,
       "appnPortByteCost": appnPortByteCost,
       "appnPortSecurity": appnPortSecurity,
       "appnPortPropagationDelay": appnPortPropagationDelay,
       "appnPortUserDefinedParm1": appnPortUserDefinedParm1,
       "appnPortUserDefinedParm2": appnPortUserDefinedParm2,
       "appnPortUserDefinedParm3": appnPortUserDefinedParm3,
       "appnLs": appnLs,
       "appnLsRowStatusTable": appnLsRowStatusTable,
       "appnLsRowStatusEntry": appnLsRowStatusEntry,
       "appnLsRowStatus": appnLsRowStatus,
       "appnLsComponentName": appnLsComponentName,
       "appnLsStorageType": appnLsStorageType,
       "appnLsIndex": appnLsIndex,
       "appnLsLsVcReferenceTable": appnLsLsVcReferenceTable,
       "appnLsLsVcReferenceEntry": appnLsLsVcReferenceEntry,
       "appnLsName": appnLsName,
       "appnLsSap": appnLsSap,
       "appnLsConfigTable": appnLsConfigTable,
       "appnLsConfigEntry": appnLsConfigEntry,
       "appnLsPortName": appnLsPortName,
       "appnLsFeatures": appnLsFeatures,
       "appnLsMaxTxBtuSize": appnLsMaxTxBtuSize,
       "appnLsOperTable": appnLsOperTable,
       "appnLsOperEntry": appnLsOperEntry,
       "appnLsDlcType": appnLsDlcType,
       "appnLsLinkStationState": appnLsLinkStationState,
       "appnLsLinkStationSubState": appnLsLinkStationSubState,
       "appnLsActSessCount": appnLsActSessCount,
       "appnLsActualCpName": appnLsActualCpName,
       "appnLsActualCpType": appnLsActualCpType,
       "appnLsDlcName": appnLsDlcName,
       "appnLsDynamicOrDefined": appnLsDynamicOrDefined,
       "appnLsMigration": appnLsMigration,
       "appnLsTgNum": appnLsTgNum,
       "appnLsHprSupport": appnLsHprSupport,
       "appnLsAnrLabel": appnLsAnrLabel,
       "appnLsTgCharTable": appnLsTgCharTable,
       "appnLsTgCharEntry": appnLsTgCharEntry,
       "appnLsEffectiveCap": appnLsEffectiveCap,
       "appnLsConnectCost": appnLsConnectCost,
       "appnLsByteCost": appnLsByteCost,
       "appnLsSecurity": appnLsSecurity,
       "appnLsPropagationDelay": appnLsPropagationDelay,
       "appnLsUserDefinedParm1": appnLsUserDefinedParm1,
       "appnLsUserDefinedParm2": appnLsUserDefinedParm2,
       "appnLsUserDefinedParm3": appnLsUserDefinedParm3,
       "appnLsStatsTable": appnLsStatsTable,
       "appnLsStatsEntry": appnLsStatsEntry,
       "appnLsInXidBytes": appnLsInXidBytes,
       "appnLsInMsgBytes": appnLsInMsgBytes,
       "appnLsInXidFrames": appnLsInXidFrames,
       "appnLsInMsgFrames": appnLsInMsgFrames,
       "appnLsOutXidBytes": appnLsOutXidBytes,
       "appnLsOutMsgBytes": appnLsOutMsgBytes,
       "appnLsOutXidFrames": appnLsOutXidFrames,
       "appnLsOutMsgFrames": appnLsOutMsgFrames,
       "appnLsInInvalidSnaFrames": appnLsInInvalidSnaFrames,
       "appnLsInSessionControlFrames": appnLsInSessionControlFrames,
       "appnLsOutSessionControlFrames": appnLsOutSessionControlFrames,
       "appnLsEchoResponse": appnLsEchoResponse,
       "appnLsCurrentDelay": appnLsCurrentDelay,
       "appnLsMaxDelay": appnLsMaxDelay,
       "appnLsMinDelay": appnLsMinDelay,
       "appnLsGoodXids": appnLsGoodXids,
       "appnLsBadXids": appnLsBadXids,
       "appnDirEnt": appnDirEnt,
       "appnDirEntRowStatusTable": appnDirEntRowStatusTable,
       "appnDirEntRowStatusEntry": appnDirEntRowStatusEntry,
       "appnDirEntRowStatus": appnDirEntRowStatus,
       "appnDirEntComponentName": appnDirEntComponentName,
       "appnDirEntStorageType": appnDirEntStorageType,
       "appnDirEntIndex": appnDirEntIndex,
       "appnDirEntOperTable": appnDirEntOperTable,
       "appnDirEntOperEntry": appnDirEntOperEntry,
       "appnDirEntServerName": appnDirEntServerName,
       "appnDirEntLuOwnerName": appnDirEntLuOwnerName,
       "appnDirEntLocation": appnDirEntLocation,
       "appnDirEntEntryType": appnDirEntEntryType,
       "appnDirEntWildCard": appnDirEntWildCard,
       "appnAdjNn": appnAdjNn,
       "appnAdjNnRowStatusTable": appnAdjNnRowStatusTable,
       "appnAdjNnRowStatusEntry": appnAdjNnRowStatusEntry,
       "appnAdjNnRowStatus": appnAdjNnRowStatus,
       "appnAdjNnComponentName": appnAdjNnComponentName,
       "appnAdjNnStorageType": appnAdjNnStorageType,
       "appnAdjNnIndex": appnAdjNnIndex,
       "appnAdjNnOperTable": appnAdjNnOperTable,
       "appnAdjNnOperEntry": appnAdjNnOperEntry,
       "appnAdjNnCpCpSessStatus": appnAdjNnCpCpSessStatus,
       "appnAdjNnOutOfSeqTdus": appnAdjNnOutOfSeqTdus,
       "appnAdjNnLastFrsnSent": appnAdjNnLastFrsnSent,
       "appnAdjNnLastFrsnReceived": appnAdjNnLastFrsnReceived,
       "appnNn": appnNn,
       "appnNnRowStatusTable": appnNnRowStatusTable,
       "appnNnRowStatusEntry": appnNnRowStatusEntry,
       "appnNnRowStatus": appnNnRowStatus,
       "appnNnComponentName": appnNnComponentName,
       "appnNnStorageType": appnNnStorageType,
       "appnNnIndex": appnNnIndex,
       "appnNnOperTable": appnNnOperTable,
       "appnNnOperEntry": appnNnOperEntry,
       "appnNnDaysLeft": appnNnDaysLeft,
       "appnNnNodeType": appnNnNodeType,
       "appnNnResourceSequenceNumber": appnNnResourceSequenceNumber,
       "appnNnRouteAdditionResistance": appnNnRouteAdditionResistance,
       "appnNnStatus": appnNnStatus,
       "appnNnFunctionSupported": appnNnFunctionSupported,
       "appnLocTg": appnLocTg,
       "appnLocTgRowStatusTable": appnLocTgRowStatusTable,
       "appnLocTgRowStatusEntry": appnLocTgRowStatusEntry,
       "appnLocTgRowStatus": appnLocTgRowStatus,
       "appnLocTgComponentName": appnLocTgComponentName,
       "appnLocTgStorageType": appnLocTgStorageType,
       "appnLocTgDestFqcpNameIndex": appnLocTgDestFqcpNameIndex,
       "appnLocTgTransmissionGroupIndex": appnLocTgTransmissionGroupIndex,
       "appnLocTgOperTable": appnLocTgOperTable,
       "appnLocTgOperEntry": appnLocTgOperEntry,
       "appnLocTgStatus": appnLocTgStatus,
       "appnLocTgResourceSequenceNumber": appnLocTgResourceSequenceNumber,
       "appnLocTgLinkAddressTable": appnLocTgLinkAddressTable,
       "appnLocTgLinkAddressEntry": appnLocTgLinkAddressEntry,
       "appnLocTgDlcData": appnLocTgDlcData,
       "appnLocTgTgCharTable": appnLocTgTgCharTable,
       "appnLocTgTgCharEntry": appnLocTgTgCharEntry,
       "appnLocTgEffectiveCap": appnLocTgEffectiveCap,
       "appnLocTgConnectCost": appnLocTgConnectCost,
       "appnLocTgByteCost": appnLocTgByteCost,
       "appnLocTgSecurity": appnLocTgSecurity,
       "appnLocTgPropagationDelay": appnLocTgPropagationDelay,
       "appnLocTgUserDefinedParm1": appnLocTgUserDefinedParm1,
       "appnLocTgUserDefinedParm2": appnLocTgUserDefinedParm2,
       "appnLocTgUserDefinedParm3": appnLocTgUserDefinedParm3,
       "appnIsrSess": appnIsrSess,
       "appnIsrSessRowStatusTable": appnIsrSessRowStatusTable,
       "appnIsrSessRowStatusEntry": appnIsrSessRowStatusEntry,
       "appnIsrSessRowStatus": appnIsrSessRowStatus,
       "appnIsrSessComponentName": appnIsrSessComponentName,
       "appnIsrSessStorageType": appnIsrSessStorageType,
       "appnIsrSessFqcpNameIndex": appnIsrSessFqcpNameIndex,
       "appnIsrSessProcedureCorrelationIdIndex": appnIsrSessProcedureCorrelationIdIndex,
       "appnIsrSessOperTable": appnIsrSessOperTable,
       "appnIsrSessOperEntry": appnIsrSessOperEntry,
       "appnIsrSessTransmissionPriority": appnIsrSessTransmissionPriority,
       "appnIsrSessCosName": appnIsrSessCosName,
       "appnIsrSessLimitedResource": appnIsrSessLimitedResource,
       "appnIsrSessPriStats": appnIsrSessPriStats,
       "appnIsrSessPriStatsRowStatusTable": appnIsrSessPriStatsRowStatusTable,
       "appnIsrSessPriStatsRowStatusEntry": appnIsrSessPriStatsRowStatusEntry,
       "appnIsrSessPriStatsRowStatus": appnIsrSessPriStatsRowStatus,
       "appnIsrSessPriStatsComponentName": appnIsrSessPriStatsComponentName,
       "appnIsrSessPriStatsStorageType": appnIsrSessPriStatsStorageType,
       "appnIsrSessPriStatsIndex": appnIsrSessPriStatsIndex,
       "appnIsrSessPriStatsStatsTable": appnIsrSessPriStatsStatsTable,
       "appnIsrSessPriStatsStatsEntry": appnIsrSessPriStatsStatsEntry,
       "appnIsrSessPriStatsRxRuSize": appnIsrSessPriStatsRxRuSize,
       "appnIsrSessPriStatsMaxTxBtuSize": appnIsrSessPriStatsMaxTxBtuSize,
       "appnIsrSessPriStatsMaxRxBtuSize": appnIsrSessPriStatsMaxRxBtuSize,
       "appnIsrSessPriStatsMaxTxPacWin": appnIsrSessPriStatsMaxTxPacWin,
       "appnIsrSessPriStatsCurTxPacWin": appnIsrSessPriStatsCurTxPacWin,
       "appnIsrSessPriStatsMaxRxPacWin": appnIsrSessPriStatsMaxRxPacWin,
       "appnIsrSessPriStatsCurRxPacWin": appnIsrSessPriStatsCurRxPacWin,
       "appnIsrSessPriStatsTxDataframes": appnIsrSessPriStatsTxDataframes,
       "appnIsrSessPriStatsTxFmdFrames": appnIsrSessPriStatsTxFmdFrames,
       "appnIsrSessPriStatsTxDataBytes": appnIsrSessPriStatsTxDataBytes,
       "appnIsrSessPriStatsRxDataFrames": appnIsrSessPriStatsRxDataFrames,
       "appnIsrSessPriStatsRxFmdFrames": appnIsrSessPriStatsRxFmdFrames,
       "appnIsrSessPriStatsRxDataBytes": appnIsrSessPriStatsRxDataBytes,
       "appnIsrSessPriStatsSidh": appnIsrSessPriStatsSidh,
       "appnIsrSessPriStatsSidl": appnIsrSessPriStatsSidl,
       "appnIsrSessPriStatsOdai": appnIsrSessPriStatsOdai,
       "appnIsrSessPriStatsLsName": appnIsrSessPriStatsLsName,
       "appnIsrSessSecStats": appnIsrSessSecStats,
       "appnIsrSessSecStatsRowStatusTable": appnIsrSessSecStatsRowStatusTable,
       "appnIsrSessSecStatsRowStatusEntry": appnIsrSessSecStatsRowStatusEntry,
       "appnIsrSessSecStatsRowStatus": appnIsrSessSecStatsRowStatus,
       "appnIsrSessSecStatsComponentName": appnIsrSessSecStatsComponentName,
       "appnIsrSessSecStatsStorageType": appnIsrSessSecStatsStorageType,
       "appnIsrSessSecStatsIndex": appnIsrSessSecStatsIndex,
       "appnIsrSessSecStatsStatsTable": appnIsrSessSecStatsStatsTable,
       "appnIsrSessSecStatsStatsEntry": appnIsrSessSecStatsStatsEntry,
       "appnIsrSessSecStatsRxRuSize": appnIsrSessSecStatsRxRuSize,
       "appnIsrSessSecStatsMaxTxBtuSize": appnIsrSessSecStatsMaxTxBtuSize,
       "appnIsrSessSecStatsMaxRxBtuSize": appnIsrSessSecStatsMaxRxBtuSize,
       "appnIsrSessSecStatsMaxTxPacWin": appnIsrSessSecStatsMaxTxPacWin,
       "appnIsrSessSecStatsCurTxPacWin": appnIsrSessSecStatsCurTxPacWin,
       "appnIsrSessSecStatsMaxRxPacWin": appnIsrSessSecStatsMaxRxPacWin,
       "appnIsrSessSecStatsCurRxPacWin": appnIsrSessSecStatsCurRxPacWin,
       "appnIsrSessSecStatsTxDataframes": appnIsrSessSecStatsTxDataframes,
       "appnIsrSessSecStatsTxFmdFrames": appnIsrSessSecStatsTxFmdFrames,
       "appnIsrSessSecStatsTxDataBytes": appnIsrSessSecStatsTxDataBytes,
       "appnIsrSessSecStatsRxDataFrames": appnIsrSessSecStatsRxDataFrames,
       "appnIsrSessSecStatsRxFmdFrames": appnIsrSessSecStatsRxFmdFrames,
       "appnIsrSessSecStatsRxDataBytes": appnIsrSessSecStatsRxDataBytes,
       "appnIsrSessSecStatsSidh": appnIsrSessSecStatsSidh,
       "appnIsrSessSecStatsSidl": appnIsrSessSecStatsSidl,
       "appnIsrSessSecStatsOdai": appnIsrSessSecStatsOdai,
       "appnIsrSessSecStatsLsName": appnIsrSessSecStatsLsName,
       "appnNnTg": appnNnTg,
       "appnNnTgRowStatusTable": appnNnTgRowStatusTable,
       "appnNnTgRowStatusEntry": appnNnTgRowStatusEntry,
       "appnNnTgRowStatus": appnNnTgRowStatus,
       "appnNnTgComponentName": appnNnTgComponentName,
       "appnNnTgStorageType": appnNnTgStorageType,
       "appnNnTgOwnerFqcpNameIndex": appnNnTgOwnerFqcpNameIndex,
       "appnNnTgDestFqcpNameIndex": appnNnTgDestFqcpNameIndex,
       "appnNnTgTransmissionGroupIndex": appnNnTgTransmissionGroupIndex,
       "appnNnTgOperTable": appnNnTgOperTable,
       "appnNnTgOperEntry": appnNnTgOperEntry,
       "appnNnTgFlowReductionSequenceNumber": appnNnTgFlowReductionSequenceNumber,
       "appnNnTgDaysLeft": appnNnTgDaysLeft,
       "appnNnTgResourceSequenceNumber": appnNnTgResourceSequenceNumber,
       "appnNnTgStatus": appnNnTgStatus,
       "appnNnTgLinkAddressTable": appnNnTgLinkAddressTable,
       "appnNnTgLinkAddressEntry": appnNnTgLinkAddressEntry,
       "appnNnTgDlcData": appnNnTgDlcData,
       "appnNnTgTgCharTable": appnNnTgTgCharTable,
       "appnNnTgTgCharEntry": appnNnTgTgCharEntry,
       "appnNnTgEffectiveCap": appnNnTgEffectiveCap,
       "appnNnTgConnectCost": appnNnTgConnectCost,
       "appnNnTgByteCost": appnNnTgByteCost,
       "appnNnTgSecurity": appnNnTgSecurity,
       "appnNnTgPropagationDelay": appnNnTgPropagationDelay,
       "appnNnTgUserDefinedParm1": appnNnTgUserDefinedParm1,
       "appnNnTgUserDefinedParm2": appnNnTgUserDefinedParm2,
       "appnNnTgUserDefinedParm3": appnNnTgUserDefinedParm3,
       "appnRtp": appnRtp,
       "appnRtpRowStatusTable": appnRtpRowStatusTable,
       "appnRtpRowStatusEntry": appnRtpRowStatusEntry,
       "appnRtpRowStatus": appnRtpRowStatus,
       "appnRtpComponentName": appnRtpComponentName,
       "appnRtpStorageType": appnRtpStorageType,
       "appnRtpIndex": appnRtpIndex,
       "appnRtpOperTable": appnRtpOperTable,
       "appnRtpOperEntry": appnRtpOperEntry,
       "appnRtpLocalLsName": appnRtpLocalLsName,
       "appnRtpRemoteCpName": appnRtpRemoteCpName,
       "appnRtpCosName": appnRtpCosName,
       "appnRtpActiveSessions": appnRtpActiveSessions,
       "appnRtpLocalTcid": appnRtpLocalTcid,
       "appnRtpRemoteTcid": appnRtpRemoteTcid,
       "appnRtpIdleTimer": appnRtpIdleTimer,
       "appnRtpMaxBtuSize": appnRtpMaxBtuSize,
       "appnRtpStatsTable": appnRtpStatsTable,
       "appnRtpStatsEntry": appnRtpStatsEntry,
       "appnRtpTxBytes": appnRtpTxBytes,
       "appnRtpRxBytes": appnRtpRxBytes,
       "appnRtpBytesResent": appnRtpBytesResent,
       "appnRtpBytesDiscarded": appnRtpBytesDiscarded,
       "appnRtpPktTx": appnRtpPktTx,
       "appnRtpPktRx": appnRtpPktRx,
       "appnRtpPktResent": appnRtpPktResent,
       "appnRtpPktDiscard": appnRtpPktDiscard,
       "appnRtpLostFrames": appnRtpLostFrames,
       "appnRtpCurTxRate": appnRtpCurTxRate,
       "appnRtpMaxTxRate": appnRtpMaxTxRate,
       "appnRtpMinTxRate": appnRtpMinTxRate,
       "appnRtpCurRxRate": appnRtpCurRxRate,
       "appnRtpMaxRxRate": appnRtpMaxRxRate,
       "appnRtpMinRxRate": appnRtpMinRxRate,
       "appnRtpBurstSize": appnRtpBurstSize,
       "appnRtpUptime": appnRtpUptime,
       "appnRtpSmoothRoundTripTime": appnRtpSmoothRoundTripTime,
       "appnRtpLastRoundTripTime": appnRtpLastRoundTripTime,
       "appnRtpShortReqTimer": appnRtpShortReqTimer,
       "appnRtpShortReqTimeouts": appnRtpShortReqTimeouts,
       "appnRtpIdleTimeouts": appnRtpIdleTimeouts,
       "appnRtpRxInvalidSnaFrames": appnRtpRxInvalidSnaFrames,
       "appnRtpInSessionControlFrames": appnRtpInSessionControlFrames,
       "appnRtpOutSessionControlFrames": appnRtpOutSessionControlFrames,
       "appnDlu": appnDlu,
       "appnDluRowStatusTable": appnDluRowStatusTable,
       "appnDluRowStatusEntry": appnDluRowStatusEntry,
       "appnDluRowStatus": appnDluRowStatus,
       "appnDluComponentName": appnDluComponentName,
       "appnDluStorageType": appnDluStorageType,
       "appnDluIndex": appnDluIndex,
       "appnDluOperTable": appnDluOperTable,
       "appnDluOperEntry": appnDluOperEntry,
       "appnDluSscpSessActive": appnDluSscpSessActive,
       "appnDluPluSessActive": appnDluPluSessActive,
       "appnDluDlusName": appnDluDlusName,
       "appnDluPluName": appnDluPluName,
       "appnDluNauAddress": appnDluNauAddress,
       "appnDluSscp": appnDluSscp,
       "appnDluSscpRowStatusTable": appnDluSscpRowStatusTable,
       "appnDluSscpRowStatusEntry": appnDluSscpRowStatusEntry,
       "appnDluSscpRowStatus": appnDluSscpRowStatus,
       "appnDluSscpComponentName": appnDluSscpComponentName,
       "appnDluSscpStorageType": appnDluSscpStorageType,
       "appnDluSscpIndex": appnDluSscpIndex,
       "appnDluSscpStatsTable": appnDluSscpStatsTable,
       "appnDluSscpStatsEntry": appnDluSscpStatsEntry,
       "appnDluSscpRxRuSize": appnDluSscpRxRuSize,
       "appnDluSscpMaxTxBtuSize": appnDluSscpMaxTxBtuSize,
       "appnDluSscpMaxRxBtuSize": appnDluSscpMaxRxBtuSize,
       "appnDluSscpMaxTxPacWin": appnDluSscpMaxTxPacWin,
       "appnDluSscpCurTxPacWin": appnDluSscpCurTxPacWin,
       "appnDluSscpMaxRxPacWin": appnDluSscpMaxRxPacWin,
       "appnDluSscpCurRxPacWin": appnDluSscpCurRxPacWin,
       "appnDluSscpTxDataframes": appnDluSscpTxDataframes,
       "appnDluSscpTxFmdFrames": appnDluSscpTxFmdFrames,
       "appnDluSscpTxDataBytes": appnDluSscpTxDataBytes,
       "appnDluSscpRxDataFrames": appnDluSscpRxDataFrames,
       "appnDluSscpRxFmdFrames": appnDluSscpRxFmdFrames,
       "appnDluSscpRxDataBytes": appnDluSscpRxDataBytes,
       "appnDluSscpSidh": appnDluSscpSidh,
       "appnDluSscpSidl": appnDluSscpSidl,
       "appnDluSscpOdai": appnDluSscpOdai,
       "appnDluSscpLsName": appnDluSscpLsName,
       "appnDluUsStat": appnDluUsStat,
       "appnDluUsStatRowStatusTable": appnDluUsStatRowStatusTable,
       "appnDluUsStatRowStatusEntry": appnDluUsStatRowStatusEntry,
       "appnDluUsStatRowStatus": appnDluUsStatRowStatus,
       "appnDluUsStatComponentName": appnDluUsStatComponentName,
       "appnDluUsStatStorageType": appnDluUsStatStorageType,
       "appnDluUsStatIndex": appnDluUsStatIndex,
       "appnDluUsStatStatsTable": appnDluUsStatStatsTable,
       "appnDluUsStatStatsEntry": appnDluUsStatStatsEntry,
       "appnDluUsStatRxRuSize": appnDluUsStatRxRuSize,
       "appnDluUsStatMaxTxBtuSize": appnDluUsStatMaxTxBtuSize,
       "appnDluUsStatMaxRxBtuSize": appnDluUsStatMaxRxBtuSize,
       "appnDluUsStatMaxTxPacWin": appnDluUsStatMaxTxPacWin,
       "appnDluUsStatCurTxPacWin": appnDluUsStatCurTxPacWin,
       "appnDluUsStatMaxRxPacWin": appnDluUsStatMaxRxPacWin,
       "appnDluUsStatCurRxPacWin": appnDluUsStatCurRxPacWin,
       "appnDluUsStatTxDataframes": appnDluUsStatTxDataframes,
       "appnDluUsStatTxFmdFrames": appnDluUsStatTxFmdFrames,
       "appnDluUsStatTxDataBytes": appnDluUsStatTxDataBytes,
       "appnDluUsStatRxDataFrames": appnDluUsStatRxDataFrames,
       "appnDluUsStatRxFmdFrames": appnDluUsStatRxFmdFrames,
       "appnDluUsStatRxDataBytes": appnDluUsStatRxDataBytes,
       "appnDluUsStatSidh": appnDluUsStatSidh,
       "appnDluUsStatSidl": appnDluUsStatSidl,
       "appnDluUsStatOdai": appnDluUsStatOdai,
       "appnDluUsStatLsName": appnDluUsStatLsName,
       "appnDluDsStat": appnDluDsStat,
       "appnDluDsStatRowStatusTable": appnDluDsStatRowStatusTable,
       "appnDluDsStatRowStatusEntry": appnDluDsStatRowStatusEntry,
       "appnDluDsStatRowStatus": appnDluDsStatRowStatus,
       "appnDluDsStatComponentName": appnDluDsStatComponentName,
       "appnDluDsStatStorageType": appnDluDsStatStorageType,
       "appnDluDsStatIndex": appnDluDsStatIndex,
       "appnDluDsStatStatsTable": appnDluDsStatStatsTable,
       "appnDluDsStatStatsEntry": appnDluDsStatStatsEntry,
       "appnDluDsStatRxRuSize": appnDluDsStatRxRuSize,
       "appnDluDsStatMaxTxBtuSize": appnDluDsStatMaxTxBtuSize,
       "appnDluDsStatMaxRxBtuSize": appnDluDsStatMaxRxBtuSize,
       "appnDluDsStatMaxTxPacWin": appnDluDsStatMaxTxPacWin,
       "appnDluDsStatCurTxPacWin": appnDluDsStatCurTxPacWin,
       "appnDluDsStatMaxRxPacWin": appnDluDsStatMaxRxPacWin,
       "appnDluDsStatCurRxPacWin": appnDluDsStatCurRxPacWin,
       "appnDluDsStatTxDataframes": appnDluDsStatTxDataframes,
       "appnDluDsStatTxFmdFrames": appnDluDsStatTxFmdFrames,
       "appnDluDsStatTxDataBytes": appnDluDsStatTxDataBytes,
       "appnDluDsStatRxDataFrames": appnDluDsStatRxDataFrames,
       "appnDluDsStatRxFmdFrames": appnDluDsStatRxFmdFrames,
       "appnDluDsStatRxDataBytes": appnDluDsStatRxDataBytes,
       "appnDluDsStatSidh": appnDluDsStatSidh,
       "appnDluDsStatSidl": appnDluDsStatSidl,
       "appnDluDsStatOdai": appnDluDsStatOdai,
       "appnDluDsStatLsName": appnDluDsStatLsName,
       "appnDlus": appnDlus,
       "appnDlusRowStatusTable": appnDlusRowStatusTable,
       "appnDlusRowStatusEntry": appnDlusRowStatusEntry,
       "appnDlusRowStatus": appnDlusRowStatus,
       "appnDlusComponentName": appnDlusComponentName,
       "appnDlusStorageType": appnDlusStorageType,
       "appnDlusIndex": appnDlusIndex,
       "appnDlusOperTable": appnDlusOperTable,
       "appnDlusOperEntry": appnDlusOperEntry,
       "appnDlusPrimaryDlus": appnDlusPrimaryDlus,
       "appnDlusPipeState": appnDlusPipeState,
       "appnDlusActivePUs": appnDlusActivePUs,
       "appnDlusDlusStatTable": appnDlusDlusStatTable,
       "appnDlusDlusStatEntry": appnDlusDlusStatEntry,
       "appnDlusReqActPuTx": appnDlusReqActPuTx,
       "appnDlusReqActPuRspRx": appnDlusReqActPuRspRx,
       "appnDlusActPuRx": appnDlusActPuRx,
       "appnDlusActPuRspTx": appnDlusActPuRspTx,
       "appnDlusReqDactPuTx": appnDlusReqDactPuTx,
       "appnDlusReqDactPuRspRx": appnDlusReqDactPuRspRx,
       "appnDlusDactPuRx": appnDlusDactPuRx,
       "appnDlusDactPuRspTx": appnDlusDactPuRspTx,
       "appnDlusActLuRx": appnDlusActLuRx,
       "appnDlusActLuRspTx": appnDlusActLuRspTx,
       "appnDlusDactLuRx": appnDlusDactLuRx,
       "appnDlusDactLuRspTx": appnDlusDactLuRspTx,
       "appnDlusSscpPuMuRx": appnDlusSscpPuMuRx,
       "appnDlusSscpPuMuTx": appnDlusSscpPuMuTx,
       "appnDlusSscpLuMuRx": appnDlusSscpLuMuRx,
       "appnDlusSscpLuMuTx": appnDlusSscpLuMuTx,
       "appnDLUR": appnDLUR,
       "appnDLURRowStatusTable": appnDLURRowStatusTable,
       "appnDLURRowStatusEntry": appnDLURRowStatusEntry,
       "appnDLURRowStatus": appnDLURRowStatus,
       "appnDLURComponentName": appnDLURComponentName,
       "appnDLURStorageType": appnDLURStorageType,
       "appnDLURIndex": appnDLURIndex,
       "appnDLURDlurParmsTable": appnDLURDlurParmsTable,
       "appnDLURDlurParmsEntry": appnDLURDlurParmsEntry,
       "appnDLURPrimaryDefDlusName": appnDLURPrimaryDefDlusName,
       "appnDLURSecondaryDefDlusName": appnDLURSecondaryDefDlusName,
       "appnDLURDlusRetryTimeout": appnDLURDlusRetryTimeout,
       "appnDLURDlusRetryLimit": appnDLURDlusRetryLimit,
       "appnCos": appnCos,
       "appnCosRowStatusTable": appnCosRowStatusTable,
       "appnCosRowStatusEntry": appnCosRowStatusEntry,
       "appnCosRowStatus": appnCosRowStatus,
       "appnCosComponentName": appnCosComponentName,
       "appnCosStorageType": appnCosStorageType,
       "appnCosIndex": appnCosIndex,
       "appnCosTg": appnCosTg,
       "appnCosTgRowStatusTable": appnCosTgRowStatusTable,
       "appnCosTgRowStatusEntry": appnCosTgRowStatusEntry,
       "appnCosTgRowStatus": appnCosTgRowStatus,
       "appnCosTgComponentName": appnCosTgComponentName,
       "appnCosTgStorageType": appnCosTgStorageType,
       "appnCosTgIndex": appnCosTgIndex,
       "appnCosTgProvTable": appnCosTgProvTable,
       "appnCosTgProvEntry": appnCosTgProvEntry,
       "appnCosTgMinEffectiveCapacity": appnCosTgMinEffectiveCapacity,
       "appnCosTgMaxEffectiveCapacity": appnCosTgMaxEffectiveCapacity,
       "appnCosTgMinConnectCost": appnCosTgMinConnectCost,
       "appnCosTgMaxConnectCost": appnCosTgMaxConnectCost,
       "appnCosTgMinByteCost": appnCosTgMinByteCost,
       "appnCosTgMaxByteCost": appnCosTgMaxByteCost,
       "appnCosTgMinSecurity": appnCosTgMinSecurity,
       "appnCosTgMaxSecurity": appnCosTgMaxSecurity,
       "appnCosTgMinPropDelay": appnCosTgMinPropDelay,
       "appnCosTgMaxPropDelay": appnCosTgMaxPropDelay,
       "appnCosTgMinModemClass": appnCosTgMinModemClass,
       "appnCosTgMaxModemClass": appnCosTgMaxModemClass,
       "appnCosTgMinUserDefParm1": appnCosTgMinUserDefParm1,
       "appnCosTgMaxUserDefParm1": appnCosTgMaxUserDefParm1,
       "appnCosTgMinUserDefParm2": appnCosTgMinUserDefParm2,
       "appnCosTgMaxUserDefParm2": appnCosTgMaxUserDefParm2,
       "appnCosTgMinUserDefParm3": appnCosTgMinUserDefParm3,
       "appnCosTgMaxUserDefParm3": appnCosTgMaxUserDefParm3,
       "appnCosNode": appnCosNode,
       "appnCosNodeRowStatusTable": appnCosNodeRowStatusTable,
       "appnCosNodeRowStatusEntry": appnCosNodeRowStatusEntry,
       "appnCosNodeRowStatus": appnCosNodeRowStatus,
       "appnCosNodeComponentName": appnCosNodeComponentName,
       "appnCosNodeStorageType": appnCosNodeStorageType,
       "appnCosNodeIndex": appnCosNodeIndex,
       "appnCosNodeProvTable": appnCosNodeProvTable,
       "appnCosNodeProvEntry": appnCosNodeProvEntry,
       "appnCosNodeMinRouteAddResistance": appnCosNodeMinRouteAddResistance,
       "appnCosNodeMaxRouteAddResistance": appnCosNodeMaxRouteAddResistance,
       "appnCosNodeMinStatus": appnCosNodeMinStatus,
       "appnCosNodeMaxStatus": appnCosNodeMaxStatus,
       "appnCosProvTable": appnCosProvTable,
       "appnCosProvEntry": appnCosProvEntry,
       "appnCosTransmissionPriority": appnCosTransmissionPriority,
       "appnFrSvc": appnFrSvc,
       "appnFrSvcRowStatusTable": appnFrSvcRowStatusTable,
       "appnFrSvcRowStatusEntry": appnFrSvcRowStatusEntry,
       "appnFrSvcRowStatus": appnFrSvcRowStatus,
       "appnFrSvcComponentName": appnFrSvcComponentName,
       "appnFrSvcStorageType": appnFrSvcStorageType,
       "appnFrSvcIndex": appnFrSvcIndex,
       "appnFrSvcBanTable": appnFrSvcBanTable,
       "appnFrSvcBanEntry": appnFrSvcBanEntry,
       "appnFrSvcBanLocalMac": appnFrSvcBanLocalMac,
       "appnFrSvcBanLocalSap": appnFrSvcBanLocalSap,
       "appnFrSvcProvisionedTable": appnFrSvcProvisionedTable,
       "appnFrSvcProvisionedEntry": appnFrSvcProvisionedEntry,
       "appnFrSvcMaximumFrameRelaySvcs": appnFrSvcMaximumFrameRelaySvcs,
       "appnFrSvcRateEnforcement": appnFrSvcRateEnforcement,
       "appnFrSvcMaximumCir": appnFrSvcMaximumCir,
       "appnFrSvcOperationalTable": appnFrSvcOperationalTable,
       "appnFrSvcOperationalEntry": appnFrSvcOperationalEntry,
       "appnFrSvcCurrentNumberOfSvcCalls": appnFrSvcCurrentNumberOfSvcCalls,
       "appnCn": appnCn,
       "appnCnRowStatusTable": appnCnRowStatusTable,
       "appnCnRowStatusEntry": appnCnRowStatusEntry,
       "appnCnRowStatus": appnCnRowStatus,
       "appnCnComponentName": appnCnComponentName,
       "appnCnStorageType": appnCnStorageType,
       "appnCnIndex": appnCnIndex,
       "appnCnOperTable": appnCnOperTable,
       "appnCnOperEntry": appnCnOperEntry,
       "appnCnNumberActivePorts": appnCnNumberActivePorts,
       "appnProcessParmsTable": appnProcessParmsTable,
       "appnProcessParmsEntry": appnProcessParmsEntry,
       "appnLogicalProcessor": appnLogicalProcessor,
       "appnMaximumSvcs": appnMaximumSvcs,
       "appnMaximumLinkStations": appnMaximumLinkStations,
       "appnControlPointCreateParmsTable": appnControlPointCreateParmsTable,
       "appnControlPointCreateParmsEntry": appnControlPointCreateParmsEntry,
       "appnFqCpName": appnFqCpName,
       "appnBlockNumber": appnBlockNumber,
       "appnIdNumber": appnIdNumber,
       "appnRouteAdditionResistance": appnRouteAdditionResistance,
       "appnFeatures": appnFeatures,
       "appnMaximumLocates": appnMaximumLocates,
       "appnMaximumDirectorySize": appnMaximumDirectorySize,
       "appnMdsTxAlertQueueSize": appnMdsTxAlertQueueSize,
       "appnTreeCacheSize": appnTreeCacheSize,
       "appnTreeCacheUseLimit": appnTreeCacheUseLimit,
       "appnMaximumTopologyNodes": appnMaximumTopologyNodes,
       "appnMaximumTopologyTgs": appnMaximumTopologyTgs,
       "appnMaximumIsrSessions": appnMaximumIsrSessions,
       "appnIsrUpperCongestionThreshold": appnIsrUpperCongestionThreshold,
       "appnIsrLowerCongestionThreshold": appnIsrLowerCongestionThreshold,
       "appnIsrMaxRuSize": appnIsrMaxRuSize,
       "appnIsrRxPacingWindow": appnIsrRxPacingWindow,
       "appnLocateTimeout": appnLocateTimeout,
       "appnHprSupport": appnHprSupport,
       "appnDlurSupport": appnDlurSupport,
       "appnStateTable": appnStateTable,
       "appnStateEntry": appnStateEntry,
       "appnAdminState": appnAdminState,
       "appnOperationalState": appnOperationalState,
       "appnUsageState": appnUsageState,
       "appnOperationalTable": appnOperationalTable,
       "appnOperationalEntry": appnOperationalEntry,
       "appnUpTime": appnUpTime,
       "appnHeapSpaceLimit": appnHeapSpaceLimit,
       "appnHeapSpaceCurrent": appnHeapSpaceCurrent,
       "appnMemWarningThreshold": appnMemWarningThreshold,
       "appnMemCriticalThreshold": appnMemCriticalThreshold,
       "appnNnFunctionsSupported": appnNnFunctionsSupported,
       "appnGeneralFunctionsSupported": appnGeneralFunctionsSupported,
       "appnStatus": appnStatus,
       "appnFlowReductionSequenceNumber": appnFlowReductionSequenceNumber,
       "appnResourceSequenceNumber": appnResourceSequenceNumber,
       "appnDefinedLsGoodXids": appnDefinedLsGoodXids,
       "appnDefinedLsBadXids": appnDefinedLsBadXids,
       "appnDynamicLsGoodXids": appnDynamicLsGoodXids,
       "appnDynamicLsBadXids": appnDynamicLsBadXids,
       "appnActiveSvcs": appnActiveSvcs,
       "appnActiveLinkStations": appnActiveLinkStations,
       "appnMIB": appnMIB,
       "appnGroup": appnGroup,
       "appnGroupBE": appnGroupBE,
       "appnGroupBE01": appnGroupBE01,
       "appnGroupBE01A": appnGroupBE01A,
       "appnCapabilities": appnCapabilities,
       "appnCapabilitiesBE": appnCapabilitiesBE,
       "appnCapabilitiesBE01": appnCapabilitiesBE01,
       "appnCapabilitiesBE01A": appnCapabilitiesBE01A}
)
