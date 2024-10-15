# SNMP MIB module (Nortel-Magellan-Passport-CallRedirectionMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-CallRedirectionMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:29 2024
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

(Counter32,
 DisplayString,
 Integer32,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Integer32",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 AsciiStringIndex,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
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

_Crs_ObjectIdentity = ObjectIdentity
crs = _Crs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132)
)
_CrsRowStatusTable_Object = MibTable
crsRowStatusTable = _CrsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 1)
)
if mibBuilder.loadTexts:
    crsRowStatusTable.setStatus("mandatory")
_CrsRowStatusEntry_Object = MibTableRow
crsRowStatusEntry = _CrsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 1, 1)
)
crsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CallRedirectionMIB", "crsIndex"),
)
if mibBuilder.loadTexts:
    crsRowStatusEntry.setStatus("mandatory")
_CrsRowStatus_Type = RowStatus
_CrsRowStatus_Object = MibTableColumn
crsRowStatus = _CrsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 1, 1, 1),
    _CrsRowStatus_Type()
)
crsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crsRowStatus.setStatus("mandatory")
_CrsComponentName_Type = DisplayString
_CrsComponentName_Object = MibTableColumn
crsComponentName = _CrsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 1, 1, 2),
    _CrsComponentName_Type()
)
crsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crsComponentName.setStatus("mandatory")
_CrsStorageType_Type = StorageType
_CrsStorageType_Object = MibTableColumn
crsStorageType = _CrsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 1, 1, 4),
    _CrsStorageType_Type()
)
crsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crsStorageType.setStatus("mandatory")
_CrsIndex_Type = NonReplicated
_CrsIndex_Object = MibTableColumn
crsIndex = _CrsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 1, 1, 10),
    _CrsIndex_Type()
)
crsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crsIndex.setStatus("mandatory")
_CrsPAddr_ObjectIdentity = ObjectIdentity
crsPAddr = _CrsPAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 2)
)
_CrsPAddrRowStatusTable_Object = MibTable
crsPAddrRowStatusTable = _CrsPAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 2, 1)
)
if mibBuilder.loadTexts:
    crsPAddrRowStatusTable.setStatus("mandatory")
_CrsPAddrRowStatusEntry_Object = MibTableRow
crsPAddrRowStatusEntry = _CrsPAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 2, 1, 1)
)
crsPAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CallRedirectionMIB", "crsIndex"),
    (0, "Nortel-Magellan-Passport-CallRedirectionMIB", "crsPAddrIndex"),
)
if mibBuilder.loadTexts:
    crsPAddrRowStatusEntry.setStatus("mandatory")
_CrsPAddrRowStatus_Type = RowStatus
_CrsPAddrRowStatus_Object = MibTableColumn
crsPAddrRowStatus = _CrsPAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 2, 1, 1, 1),
    _CrsPAddrRowStatus_Type()
)
crsPAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crsPAddrRowStatus.setStatus("mandatory")
_CrsPAddrComponentName_Type = DisplayString
_CrsPAddrComponentName_Object = MibTableColumn
crsPAddrComponentName = _CrsPAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 2, 1, 1, 2),
    _CrsPAddrComponentName_Type()
)
crsPAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crsPAddrComponentName.setStatus("mandatory")
_CrsPAddrStorageType_Type = StorageType
_CrsPAddrStorageType_Object = MibTableColumn
crsPAddrStorageType = _CrsPAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 2, 1, 1, 4),
    _CrsPAddrStorageType_Type()
)
crsPAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crsPAddrStorageType.setStatus("mandatory")


class _CrsPAddrIndex_Type(AsciiStringIndex):
    """Custom type crsPAddrIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_CrsPAddrIndex_Type.__name__ = "AsciiStringIndex"
_CrsPAddrIndex_Object = MibTableColumn
crsPAddrIndex = _CrsPAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 2, 1, 1, 10),
    _CrsPAddrIndex_Type()
)
crsPAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crsPAddrIndex.setStatus("mandatory")
_CrsPAddrSRidMid_ObjectIdentity = ObjectIdentity
crsPAddrSRidMid = _CrsPAddrSRidMid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 2, 2)
)
_CrsPAddrSRidMidRowStatusTable_Object = MibTable
crsPAddrSRidMidRowStatusTable = _CrsPAddrSRidMidRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 2, 2, 1)
)
if mibBuilder.loadTexts:
    crsPAddrSRidMidRowStatusTable.setStatus("mandatory")
_CrsPAddrSRidMidRowStatusEntry_Object = MibTableRow
crsPAddrSRidMidRowStatusEntry = _CrsPAddrSRidMidRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 2, 2, 1, 1)
)
crsPAddrSRidMidRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CallRedirectionMIB", "crsIndex"),
    (0, "Nortel-Magellan-Passport-CallRedirectionMIB", "crsPAddrIndex"),
    (0, "Nortel-Magellan-Passport-CallRedirectionMIB", "crsPAddrSRidMidIndex"),
)
if mibBuilder.loadTexts:
    crsPAddrSRidMidRowStatusEntry.setStatus("mandatory")
_CrsPAddrSRidMidRowStatus_Type = RowStatus
_CrsPAddrSRidMidRowStatus_Object = MibTableColumn
crsPAddrSRidMidRowStatus = _CrsPAddrSRidMidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 2, 2, 1, 1, 1),
    _CrsPAddrSRidMidRowStatus_Type()
)
crsPAddrSRidMidRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crsPAddrSRidMidRowStatus.setStatus("mandatory")
_CrsPAddrSRidMidComponentName_Type = DisplayString
_CrsPAddrSRidMidComponentName_Object = MibTableColumn
crsPAddrSRidMidComponentName = _CrsPAddrSRidMidComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 2, 2, 1, 1, 2),
    _CrsPAddrSRidMidComponentName_Type()
)
crsPAddrSRidMidComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crsPAddrSRidMidComponentName.setStatus("mandatory")
_CrsPAddrSRidMidStorageType_Type = StorageType
_CrsPAddrSRidMidStorageType_Object = MibTableColumn
crsPAddrSRidMidStorageType = _CrsPAddrSRidMidStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 2, 2, 1, 1, 4),
    _CrsPAddrSRidMidStorageType_Type()
)
crsPAddrSRidMidStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crsPAddrSRidMidStorageType.setStatus("mandatory")
_CrsPAddrSRidMidIndex_Type = NonReplicated
_CrsPAddrSRidMidIndex_Object = MibTableColumn
crsPAddrSRidMidIndex = _CrsPAddrSRidMidIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 2, 2, 1, 1, 10),
    _CrsPAddrSRidMidIndex_Type()
)
crsPAddrSRidMidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crsPAddrSRidMidIndex.setStatus("mandatory")
_CrsPAddrSRidMidRidMidProvTable_Object = MibTable
crsPAddrSRidMidRidMidProvTable = _CrsPAddrSRidMidRidMidProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 2, 2, 10)
)
if mibBuilder.loadTexts:
    crsPAddrSRidMidRidMidProvTable.setStatus("mandatory")
_CrsPAddrSRidMidRidMidProvEntry_Object = MibTableRow
crsPAddrSRidMidRidMidProvEntry = _CrsPAddrSRidMidRidMidProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 2, 2, 10, 1)
)
crsPAddrSRidMidRidMidProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CallRedirectionMIB", "crsIndex"),
    (0, "Nortel-Magellan-Passport-CallRedirectionMIB", "crsPAddrIndex"),
    (0, "Nortel-Magellan-Passport-CallRedirectionMIB", "crsPAddrSRidMidIndex"),
)
if mibBuilder.loadTexts:
    crsPAddrSRidMidRidMidProvEntry.setStatus("mandatory")


class _CrsPAddrSRidMidRoutingId_Type(Unsigned32):
    """Custom type crsPAddrSRidMidRoutingId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 126),
    )


_CrsPAddrSRidMidRoutingId_Type.__name__ = "Unsigned32"
_CrsPAddrSRidMidRoutingId_Object = MibTableColumn
crsPAddrSRidMidRoutingId = _CrsPAddrSRidMidRoutingId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 2, 2, 10, 1, 2),
    _CrsPAddrSRidMidRoutingId_Type()
)
crsPAddrSRidMidRoutingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crsPAddrSRidMidRoutingId.setStatus("mandatory")


class _CrsPAddrSRidMidModuleId_Type(Unsigned32):
    """Custom type crsPAddrSRidMidModuleId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1909),
    )


_CrsPAddrSRidMidModuleId_Type.__name__ = "Unsigned32"
_CrsPAddrSRidMidModuleId_Object = MibTableColumn
crsPAddrSRidMidModuleId = _CrsPAddrSRidMidModuleId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 2, 2, 10, 1, 3),
    _CrsPAddrSRidMidModuleId_Type()
)
crsPAddrSRidMidModuleId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crsPAddrSRidMidModuleId.setStatus("mandatory")
_CrsPAddrSAddr_ObjectIdentity = ObjectIdentity
crsPAddrSAddr = _CrsPAddrSAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 2, 3)
)
_CrsPAddrSAddrRowStatusTable_Object = MibTable
crsPAddrSAddrRowStatusTable = _CrsPAddrSAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 2, 3, 1)
)
if mibBuilder.loadTexts:
    crsPAddrSAddrRowStatusTable.setStatus("mandatory")
_CrsPAddrSAddrRowStatusEntry_Object = MibTableRow
crsPAddrSAddrRowStatusEntry = _CrsPAddrSAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 2, 3, 1, 1)
)
crsPAddrSAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CallRedirectionMIB", "crsIndex"),
    (0, "Nortel-Magellan-Passport-CallRedirectionMIB", "crsPAddrIndex"),
    (0, "Nortel-Magellan-Passport-CallRedirectionMIB", "crsPAddrSAddrIndex"),
)
if mibBuilder.loadTexts:
    crsPAddrSAddrRowStatusEntry.setStatus("mandatory")
_CrsPAddrSAddrRowStatus_Type = RowStatus
_CrsPAddrSAddrRowStatus_Object = MibTableColumn
crsPAddrSAddrRowStatus = _CrsPAddrSAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 2, 3, 1, 1, 1),
    _CrsPAddrSAddrRowStatus_Type()
)
crsPAddrSAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crsPAddrSAddrRowStatus.setStatus("mandatory")
_CrsPAddrSAddrComponentName_Type = DisplayString
_CrsPAddrSAddrComponentName_Object = MibTableColumn
crsPAddrSAddrComponentName = _CrsPAddrSAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 2, 3, 1, 1, 2),
    _CrsPAddrSAddrComponentName_Type()
)
crsPAddrSAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crsPAddrSAddrComponentName.setStatus("mandatory")
_CrsPAddrSAddrStorageType_Type = StorageType
_CrsPAddrSAddrStorageType_Object = MibTableColumn
crsPAddrSAddrStorageType = _CrsPAddrSAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 2, 3, 1, 1, 4),
    _CrsPAddrSAddrStorageType_Type()
)
crsPAddrSAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crsPAddrSAddrStorageType.setStatus("mandatory")


class _CrsPAddrSAddrIndex_Type(Integer32):
    """Custom type crsPAddrSAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_CrsPAddrSAddrIndex_Type.__name__ = "Integer32"
_CrsPAddrSAddrIndex_Object = MibTableColumn
crsPAddrSAddrIndex = _CrsPAddrSAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 2, 3, 1, 1, 10),
    _CrsPAddrSAddrIndex_Type()
)
crsPAddrSAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crsPAddrSAddrIndex.setStatus("mandatory")
_CrsPAddrSAddrSecAddrProvTable_Object = MibTable
crsPAddrSAddrSecAddrProvTable = _CrsPAddrSAddrSecAddrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 2, 3, 10)
)
if mibBuilder.loadTexts:
    crsPAddrSAddrSecAddrProvTable.setStatus("mandatory")
_CrsPAddrSAddrSecAddrProvEntry_Object = MibTableRow
crsPAddrSAddrSecAddrProvEntry = _CrsPAddrSAddrSecAddrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 2, 3, 10, 1)
)
crsPAddrSAddrSecAddrProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CallRedirectionMIB", "crsIndex"),
    (0, "Nortel-Magellan-Passport-CallRedirectionMIB", "crsPAddrIndex"),
    (0, "Nortel-Magellan-Passport-CallRedirectionMIB", "crsPAddrSAddrIndex"),
)
if mibBuilder.loadTexts:
    crsPAddrSAddrSecAddrProvEntry.setStatus("mandatory")


class _CrsPAddrSAddrAddress_Type(AsciiString):
    """Custom type crsPAddrSAddrAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_CrsPAddrSAddrAddress_Type.__name__ = "AsciiString"
_CrsPAddrSAddrAddress_Object = MibTableColumn
crsPAddrSAddrAddress = _CrsPAddrSAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 2, 3, 10, 1, 3),
    _CrsPAddrSAddrAddress_Type()
)
crsPAddrSAddrAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crsPAddrSAddrAddress.setStatus("mandatory")
_CrsAltRid_ObjectIdentity = ObjectIdentity
crsAltRid = _CrsAltRid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 3)
)
_CrsAltRidRowStatusTable_Object = MibTable
crsAltRidRowStatusTable = _CrsAltRidRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 3, 1)
)
if mibBuilder.loadTexts:
    crsAltRidRowStatusTable.setStatus("mandatory")
_CrsAltRidRowStatusEntry_Object = MibTableRow
crsAltRidRowStatusEntry = _CrsAltRidRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 3, 1, 1)
)
crsAltRidRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CallRedirectionMIB", "crsIndex"),
    (0, "Nortel-Magellan-Passport-CallRedirectionMIB", "crsAltRidIndex"),
)
if mibBuilder.loadTexts:
    crsAltRidRowStatusEntry.setStatus("mandatory")
_CrsAltRidRowStatus_Type = RowStatus
_CrsAltRidRowStatus_Object = MibTableColumn
crsAltRidRowStatus = _CrsAltRidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 3, 1, 1, 1),
    _CrsAltRidRowStatus_Type()
)
crsAltRidRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crsAltRidRowStatus.setStatus("mandatory")
_CrsAltRidComponentName_Type = DisplayString
_CrsAltRidComponentName_Object = MibTableColumn
crsAltRidComponentName = _CrsAltRidComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 3, 1, 1, 2),
    _CrsAltRidComponentName_Type()
)
crsAltRidComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crsAltRidComponentName.setStatus("mandatory")
_CrsAltRidStorageType_Type = StorageType
_CrsAltRidStorageType_Object = MibTableColumn
crsAltRidStorageType = _CrsAltRidStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 3, 1, 1, 4),
    _CrsAltRidStorageType_Type()
)
crsAltRidStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crsAltRidStorageType.setStatus("mandatory")
_CrsAltRidIndex_Type = NonReplicated
_CrsAltRidIndex_Object = MibTableColumn
crsAltRidIndex = _CrsAltRidIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 3, 1, 1, 10),
    _CrsAltRidIndex_Type()
)
crsAltRidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crsAltRidIndex.setStatus("mandatory")
_CrsAltRidAltRidProvTable_Object = MibTable
crsAltRidAltRidProvTable = _CrsAltRidAltRidProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 3, 10)
)
if mibBuilder.loadTexts:
    crsAltRidAltRidProvTable.setStatus("mandatory")
_CrsAltRidAltRidProvEntry_Object = MibTableRow
crsAltRidAltRidProvEntry = _CrsAltRidAltRidProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 3, 10, 1)
)
crsAltRidAltRidProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CallRedirectionMIB", "crsIndex"),
    (0, "Nortel-Magellan-Passport-CallRedirectionMIB", "crsAltRidIndex"),
)
if mibBuilder.loadTexts:
    crsAltRidAltRidProvEntry.setStatus("mandatory")


class _CrsAltRidRoutingId_Type(Unsigned32):
    """Custom type crsAltRidRoutingId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 126),
    )


_CrsAltRidRoutingId_Type.__name__ = "Unsigned32"
_CrsAltRidRoutingId_Object = MibTableColumn
crsAltRidRoutingId = _CrsAltRidRoutingId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 3, 10, 1, 2),
    _CrsAltRidRoutingId_Type()
)
crsAltRidRoutingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crsAltRidRoutingId.setStatus("mandatory")
_CrsProvTable_Object = MibTable
crsProvTable = _CrsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 10)
)
if mibBuilder.loadTexts:
    crsProvTable.setStatus("mandatory")
_CrsProvEntry_Object = MibTableRow
crsProvEntry = _CrsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 10, 1)
)
crsProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CallRedirectionMIB", "crsIndex"),
)
if mibBuilder.loadTexts:
    crsProvEntry.setStatus("mandatory")
_CrsLogicalProcessor_Type = Link
_CrsLogicalProcessor_Object = MibTableColumn
crsLogicalProcessor = _CrsLogicalProcessor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 10, 1, 2),
    _CrsLogicalProcessor_Type()
)
crsLogicalProcessor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crsLogicalProcessor.setStatus("mandatory")
_CrsStateTable_Object = MibTable
crsStateTable = _CrsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 11)
)
if mibBuilder.loadTexts:
    crsStateTable.setStatus("mandatory")
_CrsStateEntry_Object = MibTableRow
crsStateEntry = _CrsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 11, 1)
)
crsStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CallRedirectionMIB", "crsIndex"),
)
if mibBuilder.loadTexts:
    crsStateEntry.setStatus("mandatory")


class _CrsAdminState_Type(Integer32):
    """Custom type crsAdminState based on Integer32"""
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


_CrsAdminState_Type.__name__ = "Integer32"
_CrsAdminState_Object = MibTableColumn
crsAdminState = _CrsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 11, 1, 1),
    _CrsAdminState_Type()
)
crsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crsAdminState.setStatus("mandatory")


class _CrsOperationalState_Type(Integer32):
    """Custom type crsOperationalState based on Integer32"""
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


_CrsOperationalState_Type.__name__ = "Integer32"
_CrsOperationalState_Object = MibTableColumn
crsOperationalState = _CrsOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 11, 1, 2),
    _CrsOperationalState_Type()
)
crsOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crsOperationalState.setStatus("mandatory")


class _CrsUsageState_Type(Integer32):
    """Custom type crsUsageState based on Integer32"""
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


_CrsUsageState_Type.__name__ = "Integer32"
_CrsUsageState_Object = MibTableColumn
crsUsageState = _CrsUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 11, 1, 3),
    _CrsUsageState_Type()
)
crsUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crsUsageState.setStatus("mandatory")
_CrsStatTable_Object = MibTable
crsStatTable = _CrsStatTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 12)
)
if mibBuilder.loadTexts:
    crsStatTable.setStatus("mandatory")
_CrsStatEntry_Object = MibTableRow
crsStatEntry = _CrsStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 12, 1)
)
crsStatEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CallRedirectionMIB", "crsIndex"),
)
if mibBuilder.loadTexts:
    crsStatEntry.setStatus("mandatory")


class _CrsTotalAddresses_Type(Unsigned32):
    """Custom type crsTotalAddresses based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CrsTotalAddresses_Type.__name__ = "Unsigned32"
_CrsTotalAddresses_Object = MibTableColumn
crsTotalAddresses = _CrsTotalAddresses_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 12, 1, 2),
    _CrsTotalAddresses_Type()
)
crsTotalAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crsTotalAddresses.setStatus("mandatory")
_CrsRequestsReceived_Type = Counter32
_CrsRequestsReceived_Object = MibTableColumn
crsRequestsReceived = _CrsRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 12, 1, 3),
    _CrsRequestsReceived_Type()
)
crsRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crsRequestsReceived.setStatus("mandatory")
_CrsPrimaryMatches_Type = Counter32
_CrsPrimaryMatches_Object = MibTableColumn
crsPrimaryMatches = _CrsPrimaryMatches_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 12, 1, 4),
    _CrsPrimaryMatches_Type()
)
crsPrimaryMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crsPrimaryMatches.setStatus("mandatory")
_CrsSecAddressListExhausted_Type = Counter32
_CrsSecAddressListExhausted_Object = MibTableColumn
crsSecAddressListExhausted = _CrsSecAddressListExhausted_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 12, 1, 5),
    _CrsSecAddressListExhausted_Type()
)
crsSecAddressListExhausted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crsSecAddressListExhausted.setStatus("mandatory")
_CrsMaxAddrLenExceeded_Type = Counter32
_CrsMaxAddrLenExceeded_Object = MibTableColumn
crsMaxAddrLenExceeded = _CrsMaxAddrLenExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 12, 1, 6),
    _CrsMaxAddrLenExceeded_Type()
)
crsMaxAddrLenExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crsMaxAddrLenExceeded.setStatus("mandatory")
_CrsSecRidMidUnsuccessful_Type = Counter32
_CrsSecRidMidUnsuccessful_Object = MibTableColumn
crsSecRidMidUnsuccessful = _CrsSecRidMidUnsuccessful_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 12, 1, 7),
    _CrsSecRidMidUnsuccessful_Type()
)
crsSecRidMidUnsuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crsSecRidMidUnsuccessful.setStatus("mandatory")
_CrsSecAddrUnsuccessful_Type = Counter32
_CrsSecAddrUnsuccessful_Object = MibTableColumn
crsSecAddrUnsuccessful = _CrsSecAddrUnsuccessful_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 12, 1, 8),
    _CrsSecAddrUnsuccessful_Type()
)
crsSecAddrUnsuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crsSecAddrUnsuccessful.setStatus("mandatory")
_CrsRidRedirected_Type = Counter32
_CrsRidRedirected_Object = MibTableColumn
crsRidRedirected = _CrsRidRedirected_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 12, 1, 9),
    _CrsRidRedirected_Type()
)
crsRidRedirected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crsRidRedirected.setStatus("mandatory")
_CrsRidMidRedirected_Type = Counter32
_CrsRidMidRedirected_Object = MibTableColumn
crsRidMidRedirected = _CrsRidMidRedirected_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 12, 1, 10),
    _CrsRidMidRedirected_Type()
)
crsRidMidRedirected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crsRidMidRedirected.setStatus("mandatory")
_CrsAddressRedirected_Type = Counter32
_CrsAddressRedirected_Object = MibTableColumn
crsAddressRedirected = _CrsAddressRedirected_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 12, 1, 11),
    _CrsAddressRedirected_Type()
)
crsAddressRedirected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crsAddressRedirected.setStatus("mandatory")
_CrsAltRidUnsuccessful_Type = Counter32
_CrsAltRidUnsuccessful_Object = MibTableColumn
crsAltRidUnsuccessful = _CrsAltRidUnsuccessful_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 132, 12, 1, 12),
    _CrsAltRidUnsuccessful_Type()
)
crsAltRidUnsuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crsAltRidUnsuccessful.setStatus("mandatory")
_CallRedirectionMIB_ObjectIdentity = ObjectIdentity
callRedirectionMIB = _CallRedirectionMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 132)
)
_CallRedirectionGroup_ObjectIdentity = ObjectIdentity
callRedirectionGroup = _CallRedirectionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 132, 1)
)
_CallRedirectionGroupBE_ObjectIdentity = ObjectIdentity
callRedirectionGroupBE = _CallRedirectionGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 132, 1, 5)
)
_CallRedirectionGroupBE01_ObjectIdentity = ObjectIdentity
callRedirectionGroupBE01 = _CallRedirectionGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 132, 1, 5, 2)
)
_CallRedirectionGroupBE01A_ObjectIdentity = ObjectIdentity
callRedirectionGroupBE01A = _CallRedirectionGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 132, 1, 5, 2, 2)
)
_CallRedirectionCapabilities_ObjectIdentity = ObjectIdentity
callRedirectionCapabilities = _CallRedirectionCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 132, 3)
)
_CallRedirectionCapabilitiesBE_ObjectIdentity = ObjectIdentity
callRedirectionCapabilitiesBE = _CallRedirectionCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 132, 3, 5)
)
_CallRedirectionCapabilitiesBE01_ObjectIdentity = ObjectIdentity
callRedirectionCapabilitiesBE01 = _CallRedirectionCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 132, 3, 5, 2)
)
_CallRedirectionCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
callRedirectionCapabilitiesBE01A = _CallRedirectionCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 132, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-CallRedirectionMIB",
    **{"crs": crs,
       "crsRowStatusTable": crsRowStatusTable,
       "crsRowStatusEntry": crsRowStatusEntry,
       "crsRowStatus": crsRowStatus,
       "crsComponentName": crsComponentName,
       "crsStorageType": crsStorageType,
       "crsIndex": crsIndex,
       "crsPAddr": crsPAddr,
       "crsPAddrRowStatusTable": crsPAddrRowStatusTable,
       "crsPAddrRowStatusEntry": crsPAddrRowStatusEntry,
       "crsPAddrRowStatus": crsPAddrRowStatus,
       "crsPAddrComponentName": crsPAddrComponentName,
       "crsPAddrStorageType": crsPAddrStorageType,
       "crsPAddrIndex": crsPAddrIndex,
       "crsPAddrSRidMid": crsPAddrSRidMid,
       "crsPAddrSRidMidRowStatusTable": crsPAddrSRidMidRowStatusTable,
       "crsPAddrSRidMidRowStatusEntry": crsPAddrSRidMidRowStatusEntry,
       "crsPAddrSRidMidRowStatus": crsPAddrSRidMidRowStatus,
       "crsPAddrSRidMidComponentName": crsPAddrSRidMidComponentName,
       "crsPAddrSRidMidStorageType": crsPAddrSRidMidStorageType,
       "crsPAddrSRidMidIndex": crsPAddrSRidMidIndex,
       "crsPAddrSRidMidRidMidProvTable": crsPAddrSRidMidRidMidProvTable,
       "crsPAddrSRidMidRidMidProvEntry": crsPAddrSRidMidRidMidProvEntry,
       "crsPAddrSRidMidRoutingId": crsPAddrSRidMidRoutingId,
       "crsPAddrSRidMidModuleId": crsPAddrSRidMidModuleId,
       "crsPAddrSAddr": crsPAddrSAddr,
       "crsPAddrSAddrRowStatusTable": crsPAddrSAddrRowStatusTable,
       "crsPAddrSAddrRowStatusEntry": crsPAddrSAddrRowStatusEntry,
       "crsPAddrSAddrRowStatus": crsPAddrSAddrRowStatus,
       "crsPAddrSAddrComponentName": crsPAddrSAddrComponentName,
       "crsPAddrSAddrStorageType": crsPAddrSAddrStorageType,
       "crsPAddrSAddrIndex": crsPAddrSAddrIndex,
       "crsPAddrSAddrSecAddrProvTable": crsPAddrSAddrSecAddrProvTable,
       "crsPAddrSAddrSecAddrProvEntry": crsPAddrSAddrSecAddrProvEntry,
       "crsPAddrSAddrAddress": crsPAddrSAddrAddress,
       "crsAltRid": crsAltRid,
       "crsAltRidRowStatusTable": crsAltRidRowStatusTable,
       "crsAltRidRowStatusEntry": crsAltRidRowStatusEntry,
       "crsAltRidRowStatus": crsAltRidRowStatus,
       "crsAltRidComponentName": crsAltRidComponentName,
       "crsAltRidStorageType": crsAltRidStorageType,
       "crsAltRidIndex": crsAltRidIndex,
       "crsAltRidAltRidProvTable": crsAltRidAltRidProvTable,
       "crsAltRidAltRidProvEntry": crsAltRidAltRidProvEntry,
       "crsAltRidRoutingId": crsAltRidRoutingId,
       "crsProvTable": crsProvTable,
       "crsProvEntry": crsProvEntry,
       "crsLogicalProcessor": crsLogicalProcessor,
       "crsStateTable": crsStateTable,
       "crsStateEntry": crsStateEntry,
       "crsAdminState": crsAdminState,
       "crsOperationalState": crsOperationalState,
       "crsUsageState": crsUsageState,
       "crsStatTable": crsStatTable,
       "crsStatEntry": crsStatEntry,
       "crsTotalAddresses": crsTotalAddresses,
       "crsRequestsReceived": crsRequestsReceived,
       "crsPrimaryMatches": crsPrimaryMatches,
       "crsSecAddressListExhausted": crsSecAddressListExhausted,
       "crsMaxAddrLenExceeded": crsMaxAddrLenExceeded,
       "crsSecRidMidUnsuccessful": crsSecRidMidUnsuccessful,
       "crsSecAddrUnsuccessful": crsSecAddrUnsuccessful,
       "crsRidRedirected": crsRidRedirected,
       "crsRidMidRedirected": crsRidMidRedirected,
       "crsAddressRedirected": crsAddressRedirected,
       "crsAltRidUnsuccessful": crsAltRidUnsuccessful,
       "callRedirectionMIB": callRedirectionMIB,
       "callRedirectionGroup": callRedirectionGroup,
       "callRedirectionGroupBE": callRedirectionGroupBE,
       "callRedirectionGroupBE01": callRedirectionGroupBE01,
       "callRedirectionGroupBE01A": callRedirectionGroupBE01A,
       "callRedirectionCapabilities": callRedirectionCapabilities,
       "callRedirectionCapabilitiesBE": callRedirectionCapabilitiesBE,
       "callRedirectionCapabilitiesBE01": callRedirectionCapabilitiesBE01,
       "callRedirectionCapabilitiesBE01A": callRedirectionCapabilitiesBE01A}
)
