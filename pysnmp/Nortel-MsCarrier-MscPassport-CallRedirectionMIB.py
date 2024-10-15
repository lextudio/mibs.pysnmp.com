# SNMP MIB module (Nortel-MsCarrier-MscPassport-CallRedirectionMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-CallRedirectionMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:04 2024
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
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
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
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
    "Link",
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

_MscCrs_ObjectIdentity = ObjectIdentity
mscCrs = _MscCrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132)
)
_MscCrsRowStatusTable_Object = MibTable
mscCrsRowStatusTable = _MscCrsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 1)
)
if mibBuilder.loadTexts:
    mscCrsRowStatusTable.setStatus("mandatory")
_MscCrsRowStatusEntry_Object = MibTableRow
mscCrsRowStatusEntry = _MscCrsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 1, 1)
)
mscCrsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CallRedirectionMIB", "mscCrsIndex"),
)
if mibBuilder.loadTexts:
    mscCrsRowStatusEntry.setStatus("mandatory")
_MscCrsRowStatus_Type = RowStatus
_MscCrsRowStatus_Object = MibTableColumn
mscCrsRowStatus = _MscCrsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 1, 1, 1),
    _MscCrsRowStatus_Type()
)
mscCrsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscCrsRowStatus.setStatus("mandatory")
_MscCrsComponentName_Type = DisplayString
_MscCrsComponentName_Object = MibTableColumn
mscCrsComponentName = _MscCrsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 1, 1, 2),
    _MscCrsComponentName_Type()
)
mscCrsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCrsComponentName.setStatus("mandatory")
_MscCrsStorageType_Type = StorageType
_MscCrsStorageType_Object = MibTableColumn
mscCrsStorageType = _MscCrsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 1, 1, 4),
    _MscCrsStorageType_Type()
)
mscCrsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCrsStorageType.setStatus("mandatory")
_MscCrsIndex_Type = NonReplicated
_MscCrsIndex_Object = MibTableColumn
mscCrsIndex = _MscCrsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 1, 1, 10),
    _MscCrsIndex_Type()
)
mscCrsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscCrsIndex.setStatus("mandatory")
_MscCrsPAddr_ObjectIdentity = ObjectIdentity
mscCrsPAddr = _MscCrsPAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 2)
)
_MscCrsPAddrRowStatusTable_Object = MibTable
mscCrsPAddrRowStatusTable = _MscCrsPAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 2, 1)
)
if mibBuilder.loadTexts:
    mscCrsPAddrRowStatusTable.setStatus("mandatory")
_MscCrsPAddrRowStatusEntry_Object = MibTableRow
mscCrsPAddrRowStatusEntry = _MscCrsPAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 2, 1, 1)
)
mscCrsPAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CallRedirectionMIB", "mscCrsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CallRedirectionMIB", "mscCrsPAddrIndex"),
)
if mibBuilder.loadTexts:
    mscCrsPAddrRowStatusEntry.setStatus("mandatory")
_MscCrsPAddrRowStatus_Type = RowStatus
_MscCrsPAddrRowStatus_Object = MibTableColumn
mscCrsPAddrRowStatus = _MscCrsPAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 2, 1, 1, 1),
    _MscCrsPAddrRowStatus_Type()
)
mscCrsPAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscCrsPAddrRowStatus.setStatus("mandatory")
_MscCrsPAddrComponentName_Type = DisplayString
_MscCrsPAddrComponentName_Object = MibTableColumn
mscCrsPAddrComponentName = _MscCrsPAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 2, 1, 1, 2),
    _MscCrsPAddrComponentName_Type()
)
mscCrsPAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCrsPAddrComponentName.setStatus("mandatory")
_MscCrsPAddrStorageType_Type = StorageType
_MscCrsPAddrStorageType_Object = MibTableColumn
mscCrsPAddrStorageType = _MscCrsPAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 2, 1, 1, 4),
    _MscCrsPAddrStorageType_Type()
)
mscCrsPAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCrsPAddrStorageType.setStatus("mandatory")


class _MscCrsPAddrIndex_Type(AsciiStringIndex):
    """Custom type mscCrsPAddrIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_MscCrsPAddrIndex_Type.__name__ = "AsciiStringIndex"
_MscCrsPAddrIndex_Object = MibTableColumn
mscCrsPAddrIndex = _MscCrsPAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 2, 1, 1, 10),
    _MscCrsPAddrIndex_Type()
)
mscCrsPAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscCrsPAddrIndex.setStatus("mandatory")
_MscCrsPAddrSRidMid_ObjectIdentity = ObjectIdentity
mscCrsPAddrSRidMid = _MscCrsPAddrSRidMid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 2, 2)
)
_MscCrsPAddrSRidMidRowStatusTable_Object = MibTable
mscCrsPAddrSRidMidRowStatusTable = _MscCrsPAddrSRidMidRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscCrsPAddrSRidMidRowStatusTable.setStatus("mandatory")
_MscCrsPAddrSRidMidRowStatusEntry_Object = MibTableRow
mscCrsPAddrSRidMidRowStatusEntry = _MscCrsPAddrSRidMidRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 2, 2, 1, 1)
)
mscCrsPAddrSRidMidRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CallRedirectionMIB", "mscCrsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CallRedirectionMIB", "mscCrsPAddrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CallRedirectionMIB", "mscCrsPAddrSRidMidIndex"),
)
if mibBuilder.loadTexts:
    mscCrsPAddrSRidMidRowStatusEntry.setStatus("mandatory")
_MscCrsPAddrSRidMidRowStatus_Type = RowStatus
_MscCrsPAddrSRidMidRowStatus_Object = MibTableColumn
mscCrsPAddrSRidMidRowStatus = _MscCrsPAddrSRidMidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 2, 2, 1, 1, 1),
    _MscCrsPAddrSRidMidRowStatus_Type()
)
mscCrsPAddrSRidMidRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscCrsPAddrSRidMidRowStatus.setStatus("mandatory")
_MscCrsPAddrSRidMidComponentName_Type = DisplayString
_MscCrsPAddrSRidMidComponentName_Object = MibTableColumn
mscCrsPAddrSRidMidComponentName = _MscCrsPAddrSRidMidComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 2, 2, 1, 1, 2),
    _MscCrsPAddrSRidMidComponentName_Type()
)
mscCrsPAddrSRidMidComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCrsPAddrSRidMidComponentName.setStatus("mandatory")
_MscCrsPAddrSRidMidStorageType_Type = StorageType
_MscCrsPAddrSRidMidStorageType_Object = MibTableColumn
mscCrsPAddrSRidMidStorageType = _MscCrsPAddrSRidMidStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 2, 2, 1, 1, 4),
    _MscCrsPAddrSRidMidStorageType_Type()
)
mscCrsPAddrSRidMidStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCrsPAddrSRidMidStorageType.setStatus("mandatory")
_MscCrsPAddrSRidMidIndex_Type = NonReplicated
_MscCrsPAddrSRidMidIndex_Object = MibTableColumn
mscCrsPAddrSRidMidIndex = _MscCrsPAddrSRidMidIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 2, 2, 1, 1, 10),
    _MscCrsPAddrSRidMidIndex_Type()
)
mscCrsPAddrSRidMidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscCrsPAddrSRidMidIndex.setStatus("mandatory")
_MscCrsPAddrSRidMidRidMidProvTable_Object = MibTable
mscCrsPAddrSRidMidRidMidProvTable = _MscCrsPAddrSRidMidRidMidProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscCrsPAddrSRidMidRidMidProvTable.setStatus("mandatory")
_MscCrsPAddrSRidMidRidMidProvEntry_Object = MibTableRow
mscCrsPAddrSRidMidRidMidProvEntry = _MscCrsPAddrSRidMidRidMidProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 2, 2, 10, 1)
)
mscCrsPAddrSRidMidRidMidProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CallRedirectionMIB", "mscCrsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CallRedirectionMIB", "mscCrsPAddrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CallRedirectionMIB", "mscCrsPAddrSRidMidIndex"),
)
if mibBuilder.loadTexts:
    mscCrsPAddrSRidMidRidMidProvEntry.setStatus("mandatory")


class _MscCrsPAddrSRidMidRoutingId_Type(Unsigned32):
    """Custom type mscCrsPAddrSRidMidRoutingId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 126),
    )


_MscCrsPAddrSRidMidRoutingId_Type.__name__ = "Unsigned32"
_MscCrsPAddrSRidMidRoutingId_Object = MibTableColumn
mscCrsPAddrSRidMidRoutingId = _MscCrsPAddrSRidMidRoutingId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 2, 2, 10, 1, 2),
    _MscCrsPAddrSRidMidRoutingId_Type()
)
mscCrsPAddrSRidMidRoutingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscCrsPAddrSRidMidRoutingId.setStatus("mandatory")


class _MscCrsPAddrSRidMidModuleId_Type(Unsigned32):
    """Custom type mscCrsPAddrSRidMidModuleId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1909),
    )


_MscCrsPAddrSRidMidModuleId_Type.__name__ = "Unsigned32"
_MscCrsPAddrSRidMidModuleId_Object = MibTableColumn
mscCrsPAddrSRidMidModuleId = _MscCrsPAddrSRidMidModuleId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 2, 2, 10, 1, 3),
    _MscCrsPAddrSRidMidModuleId_Type()
)
mscCrsPAddrSRidMidModuleId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscCrsPAddrSRidMidModuleId.setStatus("mandatory")
_MscCrsPAddrSAddr_ObjectIdentity = ObjectIdentity
mscCrsPAddrSAddr = _MscCrsPAddrSAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 2, 3)
)
_MscCrsPAddrSAddrRowStatusTable_Object = MibTable
mscCrsPAddrSAddrRowStatusTable = _MscCrsPAddrSAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mscCrsPAddrSAddrRowStatusTable.setStatus("mandatory")
_MscCrsPAddrSAddrRowStatusEntry_Object = MibTableRow
mscCrsPAddrSAddrRowStatusEntry = _MscCrsPAddrSAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 2, 3, 1, 1)
)
mscCrsPAddrSAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CallRedirectionMIB", "mscCrsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CallRedirectionMIB", "mscCrsPAddrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CallRedirectionMIB", "mscCrsPAddrSAddrIndex"),
)
if mibBuilder.loadTexts:
    mscCrsPAddrSAddrRowStatusEntry.setStatus("mandatory")
_MscCrsPAddrSAddrRowStatus_Type = RowStatus
_MscCrsPAddrSAddrRowStatus_Object = MibTableColumn
mscCrsPAddrSAddrRowStatus = _MscCrsPAddrSAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 2, 3, 1, 1, 1),
    _MscCrsPAddrSAddrRowStatus_Type()
)
mscCrsPAddrSAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscCrsPAddrSAddrRowStatus.setStatus("mandatory")
_MscCrsPAddrSAddrComponentName_Type = DisplayString
_MscCrsPAddrSAddrComponentName_Object = MibTableColumn
mscCrsPAddrSAddrComponentName = _MscCrsPAddrSAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 2, 3, 1, 1, 2),
    _MscCrsPAddrSAddrComponentName_Type()
)
mscCrsPAddrSAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCrsPAddrSAddrComponentName.setStatus("mandatory")
_MscCrsPAddrSAddrStorageType_Type = StorageType
_MscCrsPAddrSAddrStorageType_Object = MibTableColumn
mscCrsPAddrSAddrStorageType = _MscCrsPAddrSAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 2, 3, 1, 1, 4),
    _MscCrsPAddrSAddrStorageType_Type()
)
mscCrsPAddrSAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCrsPAddrSAddrStorageType.setStatus("mandatory")


class _MscCrsPAddrSAddrIndex_Type(Integer32):
    """Custom type mscCrsPAddrSAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_MscCrsPAddrSAddrIndex_Type.__name__ = "Integer32"
_MscCrsPAddrSAddrIndex_Object = MibTableColumn
mscCrsPAddrSAddrIndex = _MscCrsPAddrSAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 2, 3, 1, 1, 10),
    _MscCrsPAddrSAddrIndex_Type()
)
mscCrsPAddrSAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscCrsPAddrSAddrIndex.setStatus("mandatory")
_MscCrsPAddrSAddrSecAddrProvTable_Object = MibTable
mscCrsPAddrSAddrSecAddrProvTable = _MscCrsPAddrSAddrSecAddrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 2, 3, 10)
)
if mibBuilder.loadTexts:
    mscCrsPAddrSAddrSecAddrProvTable.setStatus("mandatory")
_MscCrsPAddrSAddrSecAddrProvEntry_Object = MibTableRow
mscCrsPAddrSAddrSecAddrProvEntry = _MscCrsPAddrSAddrSecAddrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 2, 3, 10, 1)
)
mscCrsPAddrSAddrSecAddrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CallRedirectionMIB", "mscCrsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CallRedirectionMIB", "mscCrsPAddrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CallRedirectionMIB", "mscCrsPAddrSAddrIndex"),
)
if mibBuilder.loadTexts:
    mscCrsPAddrSAddrSecAddrProvEntry.setStatus("mandatory")


class _MscCrsPAddrSAddrAddress_Type(AsciiString):
    """Custom type mscCrsPAddrSAddrAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_MscCrsPAddrSAddrAddress_Type.__name__ = "AsciiString"
_MscCrsPAddrSAddrAddress_Object = MibTableColumn
mscCrsPAddrSAddrAddress = _MscCrsPAddrSAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 2, 3, 10, 1, 3),
    _MscCrsPAddrSAddrAddress_Type()
)
mscCrsPAddrSAddrAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscCrsPAddrSAddrAddress.setStatus("mandatory")
_MscCrsAltRid_ObjectIdentity = ObjectIdentity
mscCrsAltRid = _MscCrsAltRid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 3)
)
_MscCrsAltRidRowStatusTable_Object = MibTable
mscCrsAltRidRowStatusTable = _MscCrsAltRidRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 3, 1)
)
if mibBuilder.loadTexts:
    mscCrsAltRidRowStatusTable.setStatus("mandatory")
_MscCrsAltRidRowStatusEntry_Object = MibTableRow
mscCrsAltRidRowStatusEntry = _MscCrsAltRidRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 3, 1, 1)
)
mscCrsAltRidRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CallRedirectionMIB", "mscCrsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CallRedirectionMIB", "mscCrsAltRidIndex"),
)
if mibBuilder.loadTexts:
    mscCrsAltRidRowStatusEntry.setStatus("mandatory")
_MscCrsAltRidRowStatus_Type = RowStatus
_MscCrsAltRidRowStatus_Object = MibTableColumn
mscCrsAltRidRowStatus = _MscCrsAltRidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 3, 1, 1, 1),
    _MscCrsAltRidRowStatus_Type()
)
mscCrsAltRidRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscCrsAltRidRowStatus.setStatus("mandatory")
_MscCrsAltRidComponentName_Type = DisplayString
_MscCrsAltRidComponentName_Object = MibTableColumn
mscCrsAltRidComponentName = _MscCrsAltRidComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 3, 1, 1, 2),
    _MscCrsAltRidComponentName_Type()
)
mscCrsAltRidComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCrsAltRidComponentName.setStatus("mandatory")
_MscCrsAltRidStorageType_Type = StorageType
_MscCrsAltRidStorageType_Object = MibTableColumn
mscCrsAltRidStorageType = _MscCrsAltRidStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 3, 1, 1, 4),
    _MscCrsAltRidStorageType_Type()
)
mscCrsAltRidStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCrsAltRidStorageType.setStatus("mandatory")
_MscCrsAltRidIndex_Type = NonReplicated
_MscCrsAltRidIndex_Object = MibTableColumn
mscCrsAltRidIndex = _MscCrsAltRidIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 3, 1, 1, 10),
    _MscCrsAltRidIndex_Type()
)
mscCrsAltRidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscCrsAltRidIndex.setStatus("mandatory")
_MscCrsAltRidAltRidProvTable_Object = MibTable
mscCrsAltRidAltRidProvTable = _MscCrsAltRidAltRidProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 3, 10)
)
if mibBuilder.loadTexts:
    mscCrsAltRidAltRidProvTable.setStatus("mandatory")
_MscCrsAltRidAltRidProvEntry_Object = MibTableRow
mscCrsAltRidAltRidProvEntry = _MscCrsAltRidAltRidProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 3, 10, 1)
)
mscCrsAltRidAltRidProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CallRedirectionMIB", "mscCrsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CallRedirectionMIB", "mscCrsAltRidIndex"),
)
if mibBuilder.loadTexts:
    mscCrsAltRidAltRidProvEntry.setStatus("mandatory")


class _MscCrsAltRidRoutingId_Type(Unsigned32):
    """Custom type mscCrsAltRidRoutingId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 126),
    )


_MscCrsAltRidRoutingId_Type.__name__ = "Unsigned32"
_MscCrsAltRidRoutingId_Object = MibTableColumn
mscCrsAltRidRoutingId = _MscCrsAltRidRoutingId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 3, 10, 1, 2),
    _MscCrsAltRidRoutingId_Type()
)
mscCrsAltRidRoutingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscCrsAltRidRoutingId.setStatus("mandatory")
_MscCrsProvTable_Object = MibTable
mscCrsProvTable = _MscCrsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 10)
)
if mibBuilder.loadTexts:
    mscCrsProvTable.setStatus("mandatory")
_MscCrsProvEntry_Object = MibTableRow
mscCrsProvEntry = _MscCrsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 10, 1)
)
mscCrsProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CallRedirectionMIB", "mscCrsIndex"),
)
if mibBuilder.loadTexts:
    mscCrsProvEntry.setStatus("mandatory")
_MscCrsLogicalProcessor_Type = Link
_MscCrsLogicalProcessor_Object = MibTableColumn
mscCrsLogicalProcessor = _MscCrsLogicalProcessor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 10, 1, 2),
    _MscCrsLogicalProcessor_Type()
)
mscCrsLogicalProcessor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscCrsLogicalProcessor.setStatus("mandatory")
_MscCrsStateTable_Object = MibTable
mscCrsStateTable = _MscCrsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 11)
)
if mibBuilder.loadTexts:
    mscCrsStateTable.setStatus("mandatory")
_MscCrsStateEntry_Object = MibTableRow
mscCrsStateEntry = _MscCrsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 11, 1)
)
mscCrsStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CallRedirectionMIB", "mscCrsIndex"),
)
if mibBuilder.loadTexts:
    mscCrsStateEntry.setStatus("mandatory")


class _MscCrsAdminState_Type(Integer32):
    """Custom type mscCrsAdminState based on Integer32"""
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


_MscCrsAdminState_Type.__name__ = "Integer32"
_MscCrsAdminState_Object = MibTableColumn
mscCrsAdminState = _MscCrsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 11, 1, 1),
    _MscCrsAdminState_Type()
)
mscCrsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCrsAdminState.setStatus("mandatory")


class _MscCrsOperationalState_Type(Integer32):
    """Custom type mscCrsOperationalState based on Integer32"""
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


_MscCrsOperationalState_Type.__name__ = "Integer32"
_MscCrsOperationalState_Object = MibTableColumn
mscCrsOperationalState = _MscCrsOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 11, 1, 2),
    _MscCrsOperationalState_Type()
)
mscCrsOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCrsOperationalState.setStatus("mandatory")


class _MscCrsUsageState_Type(Integer32):
    """Custom type mscCrsUsageState based on Integer32"""
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


_MscCrsUsageState_Type.__name__ = "Integer32"
_MscCrsUsageState_Object = MibTableColumn
mscCrsUsageState = _MscCrsUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 11, 1, 3),
    _MscCrsUsageState_Type()
)
mscCrsUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCrsUsageState.setStatus("mandatory")
_MscCrsStatTable_Object = MibTable
mscCrsStatTable = _MscCrsStatTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 12)
)
if mibBuilder.loadTexts:
    mscCrsStatTable.setStatus("mandatory")
_MscCrsStatEntry_Object = MibTableRow
mscCrsStatEntry = _MscCrsStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 12, 1)
)
mscCrsStatEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CallRedirectionMIB", "mscCrsIndex"),
)
if mibBuilder.loadTexts:
    mscCrsStatEntry.setStatus("mandatory")


class _MscCrsTotalAddresses_Type(Unsigned32):
    """Custom type mscCrsTotalAddresses based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscCrsTotalAddresses_Type.__name__ = "Unsigned32"
_MscCrsTotalAddresses_Object = MibTableColumn
mscCrsTotalAddresses = _MscCrsTotalAddresses_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 12, 1, 2),
    _MscCrsTotalAddresses_Type()
)
mscCrsTotalAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCrsTotalAddresses.setStatus("mandatory")
_MscCrsRequestsReceived_Type = Counter32
_MscCrsRequestsReceived_Object = MibTableColumn
mscCrsRequestsReceived = _MscCrsRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 12, 1, 3),
    _MscCrsRequestsReceived_Type()
)
mscCrsRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCrsRequestsReceived.setStatus("mandatory")
_MscCrsPrimaryMatches_Type = Counter32
_MscCrsPrimaryMatches_Object = MibTableColumn
mscCrsPrimaryMatches = _MscCrsPrimaryMatches_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 12, 1, 4),
    _MscCrsPrimaryMatches_Type()
)
mscCrsPrimaryMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCrsPrimaryMatches.setStatus("mandatory")
_MscCrsSecAddressListExhausted_Type = Counter32
_MscCrsSecAddressListExhausted_Object = MibTableColumn
mscCrsSecAddressListExhausted = _MscCrsSecAddressListExhausted_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 12, 1, 5),
    _MscCrsSecAddressListExhausted_Type()
)
mscCrsSecAddressListExhausted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCrsSecAddressListExhausted.setStatus("mandatory")
_MscCrsMaxAddrLenExceeded_Type = Counter32
_MscCrsMaxAddrLenExceeded_Object = MibTableColumn
mscCrsMaxAddrLenExceeded = _MscCrsMaxAddrLenExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 12, 1, 6),
    _MscCrsMaxAddrLenExceeded_Type()
)
mscCrsMaxAddrLenExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCrsMaxAddrLenExceeded.setStatus("mandatory")
_MscCrsSecRidMidUnsuccessful_Type = Counter32
_MscCrsSecRidMidUnsuccessful_Object = MibTableColumn
mscCrsSecRidMidUnsuccessful = _MscCrsSecRidMidUnsuccessful_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 12, 1, 7),
    _MscCrsSecRidMidUnsuccessful_Type()
)
mscCrsSecRidMidUnsuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCrsSecRidMidUnsuccessful.setStatus("mandatory")
_MscCrsSecAddrUnsuccessful_Type = Counter32
_MscCrsSecAddrUnsuccessful_Object = MibTableColumn
mscCrsSecAddrUnsuccessful = _MscCrsSecAddrUnsuccessful_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 12, 1, 8),
    _MscCrsSecAddrUnsuccessful_Type()
)
mscCrsSecAddrUnsuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCrsSecAddrUnsuccessful.setStatus("mandatory")
_MscCrsRidRedirected_Type = Counter32
_MscCrsRidRedirected_Object = MibTableColumn
mscCrsRidRedirected = _MscCrsRidRedirected_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 12, 1, 9),
    _MscCrsRidRedirected_Type()
)
mscCrsRidRedirected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCrsRidRedirected.setStatus("mandatory")
_MscCrsRidMidRedirected_Type = Counter32
_MscCrsRidMidRedirected_Object = MibTableColumn
mscCrsRidMidRedirected = _MscCrsRidMidRedirected_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 12, 1, 10),
    _MscCrsRidMidRedirected_Type()
)
mscCrsRidMidRedirected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCrsRidMidRedirected.setStatus("mandatory")
_MscCrsAddressRedirected_Type = Counter32
_MscCrsAddressRedirected_Object = MibTableColumn
mscCrsAddressRedirected = _MscCrsAddressRedirected_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 12, 1, 11),
    _MscCrsAddressRedirected_Type()
)
mscCrsAddressRedirected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCrsAddressRedirected.setStatus("mandatory")
_MscCrsAltRidUnsuccessful_Type = Counter32
_MscCrsAltRidUnsuccessful_Object = MibTableColumn
mscCrsAltRidUnsuccessful = _MscCrsAltRidUnsuccessful_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 132, 12, 1, 12),
    _MscCrsAltRidUnsuccessful_Type()
)
mscCrsAltRidUnsuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCrsAltRidUnsuccessful.setStatus("mandatory")
_CallRedirectionMIB_ObjectIdentity = ObjectIdentity
callRedirectionMIB = _CallRedirectionMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 132)
)
_CallRedirectionGroup_ObjectIdentity = ObjectIdentity
callRedirectionGroup = _CallRedirectionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 132, 1)
)
_CallRedirectionGroupCA_ObjectIdentity = ObjectIdentity
callRedirectionGroupCA = _CallRedirectionGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 132, 1, 1)
)
_CallRedirectionGroupCA02_ObjectIdentity = ObjectIdentity
callRedirectionGroupCA02 = _CallRedirectionGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 132, 1, 1, 3)
)
_CallRedirectionGroupCA02A_ObjectIdentity = ObjectIdentity
callRedirectionGroupCA02A = _CallRedirectionGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 132, 1, 1, 3, 2)
)
_CallRedirectionCapabilities_ObjectIdentity = ObjectIdentity
callRedirectionCapabilities = _CallRedirectionCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 132, 3)
)
_CallRedirectionCapabilitiesCA_ObjectIdentity = ObjectIdentity
callRedirectionCapabilitiesCA = _CallRedirectionCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 132, 3, 1)
)
_CallRedirectionCapabilitiesCA02_ObjectIdentity = ObjectIdentity
callRedirectionCapabilitiesCA02 = _CallRedirectionCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 132, 3, 1, 3)
)
_CallRedirectionCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
callRedirectionCapabilitiesCA02A = _CallRedirectionCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 132, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-CallRedirectionMIB",
    **{"mscCrs": mscCrs,
       "mscCrsRowStatusTable": mscCrsRowStatusTable,
       "mscCrsRowStatusEntry": mscCrsRowStatusEntry,
       "mscCrsRowStatus": mscCrsRowStatus,
       "mscCrsComponentName": mscCrsComponentName,
       "mscCrsStorageType": mscCrsStorageType,
       "mscCrsIndex": mscCrsIndex,
       "mscCrsPAddr": mscCrsPAddr,
       "mscCrsPAddrRowStatusTable": mscCrsPAddrRowStatusTable,
       "mscCrsPAddrRowStatusEntry": mscCrsPAddrRowStatusEntry,
       "mscCrsPAddrRowStatus": mscCrsPAddrRowStatus,
       "mscCrsPAddrComponentName": mscCrsPAddrComponentName,
       "mscCrsPAddrStorageType": mscCrsPAddrStorageType,
       "mscCrsPAddrIndex": mscCrsPAddrIndex,
       "mscCrsPAddrSRidMid": mscCrsPAddrSRidMid,
       "mscCrsPAddrSRidMidRowStatusTable": mscCrsPAddrSRidMidRowStatusTable,
       "mscCrsPAddrSRidMidRowStatusEntry": mscCrsPAddrSRidMidRowStatusEntry,
       "mscCrsPAddrSRidMidRowStatus": mscCrsPAddrSRidMidRowStatus,
       "mscCrsPAddrSRidMidComponentName": mscCrsPAddrSRidMidComponentName,
       "mscCrsPAddrSRidMidStorageType": mscCrsPAddrSRidMidStorageType,
       "mscCrsPAddrSRidMidIndex": mscCrsPAddrSRidMidIndex,
       "mscCrsPAddrSRidMidRidMidProvTable": mscCrsPAddrSRidMidRidMidProvTable,
       "mscCrsPAddrSRidMidRidMidProvEntry": mscCrsPAddrSRidMidRidMidProvEntry,
       "mscCrsPAddrSRidMidRoutingId": mscCrsPAddrSRidMidRoutingId,
       "mscCrsPAddrSRidMidModuleId": mscCrsPAddrSRidMidModuleId,
       "mscCrsPAddrSAddr": mscCrsPAddrSAddr,
       "mscCrsPAddrSAddrRowStatusTable": mscCrsPAddrSAddrRowStatusTable,
       "mscCrsPAddrSAddrRowStatusEntry": mscCrsPAddrSAddrRowStatusEntry,
       "mscCrsPAddrSAddrRowStatus": mscCrsPAddrSAddrRowStatus,
       "mscCrsPAddrSAddrComponentName": mscCrsPAddrSAddrComponentName,
       "mscCrsPAddrSAddrStorageType": mscCrsPAddrSAddrStorageType,
       "mscCrsPAddrSAddrIndex": mscCrsPAddrSAddrIndex,
       "mscCrsPAddrSAddrSecAddrProvTable": mscCrsPAddrSAddrSecAddrProvTable,
       "mscCrsPAddrSAddrSecAddrProvEntry": mscCrsPAddrSAddrSecAddrProvEntry,
       "mscCrsPAddrSAddrAddress": mscCrsPAddrSAddrAddress,
       "mscCrsAltRid": mscCrsAltRid,
       "mscCrsAltRidRowStatusTable": mscCrsAltRidRowStatusTable,
       "mscCrsAltRidRowStatusEntry": mscCrsAltRidRowStatusEntry,
       "mscCrsAltRidRowStatus": mscCrsAltRidRowStatus,
       "mscCrsAltRidComponentName": mscCrsAltRidComponentName,
       "mscCrsAltRidStorageType": mscCrsAltRidStorageType,
       "mscCrsAltRidIndex": mscCrsAltRidIndex,
       "mscCrsAltRidAltRidProvTable": mscCrsAltRidAltRidProvTable,
       "mscCrsAltRidAltRidProvEntry": mscCrsAltRidAltRidProvEntry,
       "mscCrsAltRidRoutingId": mscCrsAltRidRoutingId,
       "mscCrsProvTable": mscCrsProvTable,
       "mscCrsProvEntry": mscCrsProvEntry,
       "mscCrsLogicalProcessor": mscCrsLogicalProcessor,
       "mscCrsStateTable": mscCrsStateTable,
       "mscCrsStateEntry": mscCrsStateEntry,
       "mscCrsAdminState": mscCrsAdminState,
       "mscCrsOperationalState": mscCrsOperationalState,
       "mscCrsUsageState": mscCrsUsageState,
       "mscCrsStatTable": mscCrsStatTable,
       "mscCrsStatEntry": mscCrsStatEntry,
       "mscCrsTotalAddresses": mscCrsTotalAddresses,
       "mscCrsRequestsReceived": mscCrsRequestsReceived,
       "mscCrsPrimaryMatches": mscCrsPrimaryMatches,
       "mscCrsSecAddressListExhausted": mscCrsSecAddressListExhausted,
       "mscCrsMaxAddrLenExceeded": mscCrsMaxAddrLenExceeded,
       "mscCrsSecRidMidUnsuccessful": mscCrsSecRidMidUnsuccessful,
       "mscCrsSecAddrUnsuccessful": mscCrsSecAddrUnsuccessful,
       "mscCrsRidRedirected": mscCrsRidRedirected,
       "mscCrsRidMidRedirected": mscCrsRidMidRedirected,
       "mscCrsAddressRedirected": mscCrsAddressRedirected,
       "mscCrsAltRidUnsuccessful": mscCrsAltRidUnsuccessful,
       "callRedirectionMIB": callRedirectionMIB,
       "callRedirectionGroup": callRedirectionGroup,
       "callRedirectionGroupCA": callRedirectionGroupCA,
       "callRedirectionGroupCA02": callRedirectionGroupCA02,
       "callRedirectionGroupCA02A": callRedirectionGroupCA02A,
       "callRedirectionCapabilities": callRedirectionCapabilities,
       "callRedirectionCapabilitiesCA": callRedirectionCapabilitiesCA,
       "callRedirectionCapabilitiesCA02": callRedirectionCapabilitiesCA02,
       "callRedirectionCapabilitiesCA02A": callRedirectionCapabilitiesCA02A}
)
