# SNMP MIB module (Unisphere-Data-ACCOUNTING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-ACCOUNTING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:16 2024
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

(acctngFileEntry,
 acctngSelectionEntry,
 acctngSelectionIndex) = mibBuilder.importSymbols(
    "ACCOUNTING-CONTROL-MIB",
    "acctngFileEntry",
    "acctngSelectionEntry",
    "acctngSelectionIndex")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(usdIfType,) = mibBuilder.importSymbols(
    "Unisphere-Data-IF-MIB",
    "usdIfType")

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdPolicyAttachmentType,) = mibBuilder.importSymbols(
    "Unisphere-Data-POLICY-MIB",
    "UsdPolicyAttachmentType")

(UsdAcctngAdminType,
 UsdAcctngOperType) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdAcctngAdminType",
    "UsdAcctngOperType")


# MODULE-IDENTITY

usdAcctngMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24)
)
usdAcctngMIB.setRevisions(
        ("2001-12-05 14:16",
         "2001-11-19 19:00",
         "2001-03-26 13:22",
         "2000-11-07 19:00",
         "2000-07-21 00:00",
         "2000-03-20 00:00",
         "2000-01-17 00:00",
         "1999-10-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdAcctngMIBObjects_ObjectIdentity = ObjectIdentity
usdAcctngMIBObjects = _UsdAcctngMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1)
)
_UsdAcctngSelectionControl_ObjectIdentity = ObjectIdentity
usdAcctngSelectionControl = _UsdAcctngSelectionControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 1)
)
_UsdAcctngSelectionTable_Object = MibTable
usdAcctngSelectionTable = _UsdAcctngSelectionTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 1, 1)
)
if mibBuilder.loadTexts:
    usdAcctngSelectionTable.setStatus("current")
_UsdAcctngSelectionEntry_Object = MibTableRow
usdAcctngSelectionEntry = _UsdAcctngSelectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    usdAcctngSelectionEntry.setStatus("current")


class _UsdAcctngSelectionType_Type(Bits):
    """Custom type usdAcctngSelectionType based on Bits"""
    namedValues = NamedValues(
        *(("connectionLessLayer2", 1),
          ("ietfAccountControl", 0))
    )

_UsdAcctngSelectionType_Type.__name__ = "Bits"
_UsdAcctngSelectionType_Object = MibTableColumn
usdAcctngSelectionType = _UsdAcctngSelectionType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 1, 1, 1, 1),
    _UsdAcctngSelectionType_Type()
)
usdAcctngSelectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAcctngSelectionType.setStatus("current")


class _UsdAcctngSelectionMode_Type(Integer32):
    """Custom type usdAcctngSelectionMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absoluteCounterValues", 1),
          ("deltaCounterValues", 2))
    )


_UsdAcctngSelectionMode_Type.__name__ = "Integer32"
_UsdAcctngSelectionMode_Object = MibTableColumn
usdAcctngSelectionMode = _UsdAcctngSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 1, 1, 1, 2),
    _UsdAcctngSelectionMode_Type()
)
usdAcctngSelectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAcctngSelectionMode.setStatus("current")


class _UsdAcctngSelectionSubtreeType_Type(Integer32):
    """Custom type usdAcctngSelectionSubtreeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lineCard", 1),
          ("systemController", 2),
          ("unknown", 0))
    )


_UsdAcctngSelectionSubtreeType_Type.__name__ = "Integer32"
_UsdAcctngSelectionSubtreeType_Object = MibTableColumn
usdAcctngSelectionSubtreeType = _UsdAcctngSelectionSubtreeType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 1, 1, 1, 3),
    _UsdAcctngSelectionSubtreeType_Type()
)
usdAcctngSelectionSubtreeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAcctngSelectionSubtreeType.setStatus("deprecated")


class _UsdAcctngSelectionMaxIfStackLevels_Type(Integer32):
    """Custom type usdAcctngSelectionMaxIfStackLevels based on Integer32"""
    defaultValue = 0


_UsdAcctngSelectionMaxIfStackLevels_Object = MibTableColumn
usdAcctngSelectionMaxIfStackLevels = _UsdAcctngSelectionMaxIfStackLevels_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 1, 1, 1, 4),
    _UsdAcctngSelectionMaxIfStackLevels_Type()
)
usdAcctngSelectionMaxIfStackLevels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAcctngSelectionMaxIfStackLevels.setStatus("current")


class _UsdAcctngSelectionPolicyName_Type(DisplayString):
    """Custom type usdAcctngSelectionPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_UsdAcctngSelectionPolicyName_Type.__name__ = "DisplayString"
_UsdAcctngSelectionPolicyName_Object = MibTableColumn
usdAcctngSelectionPolicyName = _UsdAcctngSelectionPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 1, 1, 1, 5),
    _UsdAcctngSelectionPolicyName_Type()
)
usdAcctngSelectionPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAcctngSelectionPolicyName.setStatus("current")
_UsdAcctngSelectionPolicyType_Type = UsdPolicyAttachmentType
_UsdAcctngSelectionPolicyType_Object = MibTableColumn
usdAcctngSelectionPolicyType = _UsdAcctngSelectionPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 1, 1, 1, 6),
    _UsdAcctngSelectionPolicyType_Type()
)
usdAcctngSelectionPolicyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAcctngSelectionPolicyType.setStatus("current")
_UsdAcctngSelectionIfStackStartTable_Object = MibTable
usdAcctngSelectionIfStackStartTable = _UsdAcctngSelectionIfStackStartTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 1, 3)
)
if mibBuilder.loadTexts:
    usdAcctngSelectionIfStackStartTable.setStatus("current")
_UsdAcctngSelectionIfStackStartEntry_Object = MibTableRow
usdAcctngSelectionIfStackStartEntry = _UsdAcctngSelectionIfStackStartEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 1, 3, 1)
)
usdAcctngSelectionIfStackStartEntry.setIndexNames(
    (0, "ACCOUNTING-CONTROL-MIB", "acctngSelectionIndex"),
    (0, "Unisphere-Data-ACCOUNTING-MIB", "usdAcctngSelectionIfStackIfIndex"),
)
if mibBuilder.loadTexts:
    usdAcctngSelectionIfStackStartEntry.setStatus("current")
_UsdAcctngSelectionIfStackIfIndex_Type = InterfaceIndex
_UsdAcctngSelectionIfStackIfIndex_Object = MibTableColumn
usdAcctngSelectionIfStackIfIndex = _UsdAcctngSelectionIfStackIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 1, 3, 1, 1),
    _UsdAcctngSelectionIfStackIfIndex_Type()
)
usdAcctngSelectionIfStackIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdAcctngSelectionIfStackIfIndex.setStatus("current")
_UsdAcctngSelectionIfStackRowStatus_Type = RowStatus
_UsdAcctngSelectionIfStackRowStatus_Object = MibTableColumn
usdAcctngSelectionIfStackRowStatus = _UsdAcctngSelectionIfStackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 1, 3, 1, 2),
    _UsdAcctngSelectionIfStackRowStatus_Type()
)
usdAcctngSelectionIfStackRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAcctngSelectionIfStackRowStatus.setStatus("current")
_UsdAcctngFileControl_ObjectIdentity = ObjectIdentity
usdAcctngFileControl = _UsdAcctngFileControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 2)
)
_UsdAcctngFileTable_Object = MibTable
usdAcctngFileTable = _UsdAcctngFileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 2, 1)
)
if mibBuilder.loadTexts:
    usdAcctngFileTable.setStatus("current")
_UsdAcctngFileEntry_Object = MibTableRow
usdAcctngFileEntry = _UsdAcctngFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    usdAcctngFileEntry.setStatus("current")


class _UsdAcctngFileXferMode_Type(Integer32):
    """Custom type usdAcctngFileXferMode based on Integer32"""
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
        *(("usdAcctngAutomatedTransfer", 2),
          ("usdAcctngManualTransfer", 1),
          ("usdAcctngRedundantTransfer", 4),
          ("usdAcctngTransferOnFileFull", 3))
    )


_UsdAcctngFileXferMode_Type.__name__ = "Integer32"
_UsdAcctngFileXferMode_Object = MibTableColumn
usdAcctngFileXferMode = _UsdAcctngFileXferMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 2, 1, 1, 1),
    _UsdAcctngFileXferMode_Type()
)
usdAcctngFileXferMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAcctngFileXferMode.setStatus("current")


class _UsdAcctngFileXferIndex_Type(Integer32):
    """Custom type usdAcctngFileXferIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsdAcctngFileXferIndex_Type.__name__ = "Integer32"
_UsdAcctngFileXferIndex_Object = MibTableColumn
usdAcctngFileXferIndex = _UsdAcctngFileXferIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 2, 1, 1, 2),
    _UsdAcctngFileXferIndex_Type()
)
usdAcctngFileXferIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAcctngFileXferIndex.setStatus("current")


class _UsdAcctngFileXferSecondaryIndex_Type(Integer32):
    """Custom type usdAcctngFileXferSecondaryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsdAcctngFileXferSecondaryIndex_Type.__name__ = "Integer32"
_UsdAcctngFileXferSecondaryIndex_Object = MibTableColumn
usdAcctngFileXferSecondaryIndex = _UsdAcctngFileXferSecondaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 2, 1, 1, 3),
    _UsdAcctngFileXferSecondaryIndex_Type()
)
usdAcctngFileXferSecondaryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAcctngFileXferSecondaryIndex.setStatus("current")
_UsdAcctngInterfaceControl_ObjectIdentity = ObjectIdentity
usdAcctngInterfaceControl = _UsdAcctngInterfaceControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 3)
)
_UsdAcctngInterfaceTable_Object = MibTable
usdAcctngInterfaceTable = _UsdAcctngInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 3, 1)
)
if mibBuilder.loadTexts:
    usdAcctngInterfaceTable.setStatus("current")
_UsdAcctngInterfaceEntry_Object = MibTableRow
usdAcctngInterfaceEntry = _UsdAcctngInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 3, 1, 1)
)
usdAcctngInterfaceEntry.setIndexNames(
    (0, "Unisphere-Data-IF-MIB", "usdIfType"),
)
if mibBuilder.loadTexts:
    usdAcctngInterfaceEntry.setStatus("current")
_UsdAcctngInterfaceAdminStatus_Type = UsdAcctngAdminType
_UsdAcctngInterfaceAdminStatus_Object = MibTableColumn
usdAcctngInterfaceAdminStatus = _UsdAcctngInterfaceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 3, 1, 1, 1),
    _UsdAcctngInterfaceAdminStatus_Type()
)
usdAcctngInterfaceAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAcctngInterfaceAdminStatus.setStatus("current")
_UsdAcctngInterfaceOperStatus_Type = UsdAcctngOperType
_UsdAcctngInterfaceOperStatus_Object = MibTableColumn
usdAcctngInterfaceOperStatus = _UsdAcctngInterfaceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 3, 1, 1, 2),
    _UsdAcctngInterfaceOperStatus_Type()
)
usdAcctngInterfaceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAcctngInterfaceOperStatus.setStatus("current")
_UsdAcctngInterfaceRowStatus_Type = RowStatus
_UsdAcctngInterfaceRowStatus_Object = MibTableColumn
usdAcctngInterfaceRowStatus = _UsdAcctngInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 3, 1, 1, 3),
    _UsdAcctngInterfaceRowStatus_Type()
)
usdAcctngInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAcctngInterfaceRowStatus.setStatus("current")


class _UsdAcctngInterfaceAccntgFileIndex_Type(Integer32):
    """Custom type usdAcctngInterfaceAccntgFileIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdAcctngInterfaceAccntgFileIndex_Type.__name__ = "Integer32"
_UsdAcctngInterfaceAccntgFileIndex_Object = MibTableColumn
usdAcctngInterfaceAccntgFileIndex = _UsdAcctngInterfaceAccntgFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 3, 1, 1, 4),
    _UsdAcctngInterfaceAccntgFileIndex_Type()
)
usdAcctngInterfaceAccntgFileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAcctngInterfaceAccntgFileIndex.setStatus("current")
_UsdAcctngSelectionSchema_ObjectIdentity = ObjectIdentity
usdAcctngSelectionSchema = _UsdAcctngSelectionSchema_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2)
)
if mibBuilder.loadTexts:
    usdAcctngSelectionSchema.setStatus("current")
_UsdAcctngSelectionSchemaIf_ObjectIdentity = ObjectIdentity
usdAcctngSelectionSchemaIf = _UsdAcctngSelectionSchemaIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1)
)
_UsdAcctngIfInOctets_ObjectIdentity = ObjectIdentity
usdAcctngIfInOctets = _UsdAcctngIfInOctets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 1)
)
_UsdAcctngIfInUcastPkts_ObjectIdentity = ObjectIdentity
usdAcctngIfInUcastPkts = _UsdAcctngIfInUcastPkts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 2)
)
_UsdAcctngIfInDiscards_ObjectIdentity = ObjectIdentity
usdAcctngIfInDiscards = _UsdAcctngIfInDiscards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 3)
)
_UsdAcctngIfInErrors_ObjectIdentity = ObjectIdentity
usdAcctngIfInErrors = _UsdAcctngIfInErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 4)
)
_UsdAcctngIfInUnknownProtos_ObjectIdentity = ObjectIdentity
usdAcctngIfInUnknownProtos = _UsdAcctngIfInUnknownProtos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 5)
)
_UsdAcctngIfOutOctets_ObjectIdentity = ObjectIdentity
usdAcctngIfOutOctets = _UsdAcctngIfOutOctets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 6)
)
_UsdAcctngIfOutUcastPkts_ObjectIdentity = ObjectIdentity
usdAcctngIfOutUcastPkts = _UsdAcctngIfOutUcastPkts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 7)
)
_UsdAcctngIfOutDiscards_ObjectIdentity = ObjectIdentity
usdAcctngIfOutDiscards = _UsdAcctngIfOutDiscards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 8)
)
_UsdAcctngIfOutErrors_ObjectIdentity = ObjectIdentity
usdAcctngIfOutErrors = _UsdAcctngIfOutErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 9)
)
_UsdAcctngIfCorrelator_ObjectIdentity = ObjectIdentity
usdAcctngIfCorrelator = _UsdAcctngIfCorrelator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 10)
)
_UsdAcctngIfInPolicedOctets_ObjectIdentity = ObjectIdentity
usdAcctngIfInPolicedOctets = _UsdAcctngIfInPolicedOctets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 11)
)
_UsdAcctngIfInPolicedPkts_ObjectIdentity = ObjectIdentity
usdAcctngIfInPolicedPkts = _UsdAcctngIfInPolicedPkts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 12)
)
_UsdAcctngIfInSpoofedPkts_ObjectIdentity = ObjectIdentity
usdAcctngIfInSpoofedPkts = _UsdAcctngIfInSpoofedPkts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 13)
)
_UsdAcctngIfOutPolicedOctets_ObjectIdentity = ObjectIdentity
usdAcctngIfOutPolicedOctets = _UsdAcctngIfOutPolicedOctets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 14)
)
_UsdAcctngIfOutPolicedPkts_ObjectIdentity = ObjectIdentity
usdAcctngIfOutPolicedPkts = _UsdAcctngIfOutPolicedPkts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 15)
)
_UsdAcctngIfOutSchedulerDropOctets_ObjectIdentity = ObjectIdentity
usdAcctngIfOutSchedulerDropOctets = _UsdAcctngIfOutSchedulerDropOctets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 16)
)
_UsdAcctngIfOutSchedulerDropPkts_ObjectIdentity = ObjectIdentity
usdAcctngIfOutSchedulerDropPkts = _UsdAcctngIfOutSchedulerDropPkts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 17)
)
_UsdAcctngIfLowerInterface_ObjectIdentity = ObjectIdentity
usdAcctngIfLowerInterface = _UsdAcctngIfLowerInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 18)
)
_UsdAcctngIfTimeOffset_ObjectIdentity = ObjectIdentity
usdAcctngIfTimeOffset = _UsdAcctngIfTimeOffset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 19)
)
_UsdAcctngifInMulticastPkts_ObjectIdentity = ObjectIdentity
usdAcctngifInMulticastPkts = _UsdAcctngifInMulticastPkts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 20)
)
_UsdAcctngifInBroadcastPkts_ObjectIdentity = ObjectIdentity
usdAcctngifInBroadcastPkts = _UsdAcctngifInBroadcastPkts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 21)
)
_UsdAcctngifOutMulticastPkts_ObjectIdentity = ObjectIdentity
usdAcctngifOutMulticastPkts = _UsdAcctngifOutMulticastPkts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 22)
)
_UsdAcctngifOutBroadcastPkts_ObjectIdentity = ObjectIdentity
usdAcctngifOutBroadcastPkts = _UsdAcctngifOutBroadcastPkts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 23)
)
_UsdAcctngSelectionSchemaIfStack_ObjectIdentity = ObjectIdentity
usdAcctngSelectionSchemaIfStack = _UsdAcctngSelectionSchemaIfStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 3)
)
_UsdAcctngSelectionSchemaSystem_ObjectIdentity = ObjectIdentity
usdAcctngSelectionSchemaSystem = _UsdAcctngSelectionSchemaSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 4)
)
_UsdAcctngSelectionSchemaPolicy_ObjectIdentity = ObjectIdentity
usdAcctngSelectionSchemaPolicy = _UsdAcctngSelectionSchemaPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 5)
)
_UsdAcctngGreenPackets_ObjectIdentity = ObjectIdentity
usdAcctngGreenPackets = _UsdAcctngGreenPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 5, 1)
)
_UsdAcctngUpperGreenPackets_ObjectIdentity = ObjectIdentity
usdAcctngUpperGreenPackets = _UsdAcctngUpperGreenPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 5, 2)
)
_UsdAcctngYellowPackets_ObjectIdentity = ObjectIdentity
usdAcctngYellowPackets = _UsdAcctngYellowPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 5, 3)
)
_UsdAcctngUpperYellowPackets_ObjectIdentity = ObjectIdentity
usdAcctngUpperYellowPackets = _UsdAcctngUpperYellowPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 5, 4)
)
_UsdAcctngRedPackets_ObjectIdentity = ObjectIdentity
usdAcctngRedPackets = _UsdAcctngRedPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 5, 5)
)
_UsdAcctngUpperRedPackets_ObjectIdentity = ObjectIdentity
usdAcctngUpperRedPackets = _UsdAcctngUpperRedPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 5, 6)
)
_UsdAcctngGreenBytes_ObjectIdentity = ObjectIdentity
usdAcctngGreenBytes = _UsdAcctngGreenBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 5, 7)
)
_UsdAcctngUpperGreenBytes_ObjectIdentity = ObjectIdentity
usdAcctngUpperGreenBytes = _UsdAcctngUpperGreenBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 5, 8)
)
_UsdAcctngYellowBytes_ObjectIdentity = ObjectIdentity
usdAcctngYellowBytes = _UsdAcctngYellowBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 5, 9)
)
_UsdAcctngUpperYellowBytes_ObjectIdentity = ObjectIdentity
usdAcctngUpperYellowBytes = _UsdAcctngUpperYellowBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 5, 10)
)
_UsdAcctngRedBytes_ObjectIdentity = ObjectIdentity
usdAcctngRedBytes = _UsdAcctngRedBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 5, 11)
)
_UsdAcctngUpperRedBytes_ObjectIdentity = ObjectIdentity
usdAcctngUpperRedBytes = _UsdAcctngUpperRedBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 5, 12)
)
_UsdAcctngConformance_ObjectIdentity = ObjectIdentity
usdAcctngConformance = _UsdAcctngConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 3)
)
_UsdAcctngGroups_ObjectIdentity = ObjectIdentity
usdAcctngGroups = _UsdAcctngGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 3, 1)
)
_UsdAcctngCompliances_ObjectIdentity = ObjectIdentity
usdAcctngCompliances = _UsdAcctngCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 3, 2)
)
acctngSelectionEntry.registerAugmentions(
    ("Unisphere-Data-ACCOUNTING-MIB",
     "usdAcctngSelectionEntry")
)
usdAcctngSelectionEntry.setIndexNames(*acctngSelectionEntry.getIndexNames())
acctngFileEntry.registerAugmentions(
    ("Unisphere-Data-ACCOUNTING-MIB",
     "usdAcctngFileEntry")
)
usdAcctngFileEntry.setIndexNames(*acctngFileEntry.getIndexNames())

# Managed Objects groups

usdAcctngBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 3, 1, 1)
)
usdAcctngBasicGroup.setObjects(
      *(("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngSelectionType"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngSelectionMode"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngSelectionSubtreeType"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngSelectionMaxIfStackLevels"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngSelectionIfStackRowStatus"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngFileXferMode"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngFileXferIndex"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngFileXferSecondaryIndex"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngInterfaceAdminStatus"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngInterfaceOperStatus"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngInterfaceRowStatus"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngInterfaceAccntgFileIndex"))
)
if mibBuilder.loadTexts:
    usdAcctngBasicGroup.setStatus("obsolete")

usdAcctngBasicGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 3, 1, 2)
)
usdAcctngBasicGroup2.setObjects(
      *(("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngSelectionType"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngSelectionMode"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngSelectionMaxIfStackLevels"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngSelectionIfStackRowStatus"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngFileXferMode"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngFileXferIndex"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngFileXferSecondaryIndex"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngInterfaceAdminStatus"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngInterfaceOperStatus"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngInterfaceRowStatus"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngInterfaceAccntgFileIndex"))
)
if mibBuilder.loadTexts:
    usdAcctngBasicGroup2.setStatus("obsolete")

usdAcctngBasicGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 3, 1, 3)
)
usdAcctngBasicGroup3.setObjects(
      *(("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngSelectionType"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngSelectionMode"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngSelectionMaxIfStackLevels"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngSelectionPolicyName"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngSelectionPolicyType"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngSelectionIfStackRowStatus"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngFileXferMode"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngFileXferIndex"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngFileXferSecondaryIndex"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngInterfaceAdminStatus"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngInterfaceOperStatus"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngInterfaceRowStatus"),
        ("Unisphere-Data-ACCOUNTING-MIB", "usdAcctngInterfaceAccntgFileIndex"))
)
if mibBuilder.loadTexts:
    usdAcctngBasicGroup3.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdAcctngCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 3, 2, 1)
)
if mibBuilder.loadTexts:
    usdAcctngCompliance.setStatus(
        "obsolete"
    )

usdAcctngCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 3, 2, 2)
)
if mibBuilder.loadTexts:
    usdAcctngCompliance2.setStatus(
        "obsolete"
    )

usdAcctngCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 3, 2, 3)
)
if mibBuilder.loadTexts:
    usdAcctngCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-ACCOUNTING-MIB",
    **{"usdAcctngMIB": usdAcctngMIB,
       "usdAcctngMIBObjects": usdAcctngMIBObjects,
       "usdAcctngSelectionControl": usdAcctngSelectionControl,
       "usdAcctngSelectionTable": usdAcctngSelectionTable,
       "usdAcctngSelectionEntry": usdAcctngSelectionEntry,
       "usdAcctngSelectionType": usdAcctngSelectionType,
       "usdAcctngSelectionMode": usdAcctngSelectionMode,
       "usdAcctngSelectionSubtreeType": usdAcctngSelectionSubtreeType,
       "usdAcctngSelectionMaxIfStackLevels": usdAcctngSelectionMaxIfStackLevels,
       "usdAcctngSelectionPolicyName": usdAcctngSelectionPolicyName,
       "usdAcctngSelectionPolicyType": usdAcctngSelectionPolicyType,
       "usdAcctngSelectionIfStackStartTable": usdAcctngSelectionIfStackStartTable,
       "usdAcctngSelectionIfStackStartEntry": usdAcctngSelectionIfStackStartEntry,
       "usdAcctngSelectionIfStackIfIndex": usdAcctngSelectionIfStackIfIndex,
       "usdAcctngSelectionIfStackRowStatus": usdAcctngSelectionIfStackRowStatus,
       "usdAcctngFileControl": usdAcctngFileControl,
       "usdAcctngFileTable": usdAcctngFileTable,
       "usdAcctngFileEntry": usdAcctngFileEntry,
       "usdAcctngFileXferMode": usdAcctngFileXferMode,
       "usdAcctngFileXferIndex": usdAcctngFileXferIndex,
       "usdAcctngFileXferSecondaryIndex": usdAcctngFileXferSecondaryIndex,
       "usdAcctngInterfaceControl": usdAcctngInterfaceControl,
       "usdAcctngInterfaceTable": usdAcctngInterfaceTable,
       "usdAcctngInterfaceEntry": usdAcctngInterfaceEntry,
       "usdAcctngInterfaceAdminStatus": usdAcctngInterfaceAdminStatus,
       "usdAcctngInterfaceOperStatus": usdAcctngInterfaceOperStatus,
       "usdAcctngInterfaceRowStatus": usdAcctngInterfaceRowStatus,
       "usdAcctngInterfaceAccntgFileIndex": usdAcctngInterfaceAccntgFileIndex,
       "usdAcctngSelectionSchema": usdAcctngSelectionSchema,
       "usdAcctngSelectionSchemaIf": usdAcctngSelectionSchemaIf,
       "usdAcctngIfInOctets": usdAcctngIfInOctets,
       "usdAcctngIfInUcastPkts": usdAcctngIfInUcastPkts,
       "usdAcctngIfInDiscards": usdAcctngIfInDiscards,
       "usdAcctngIfInErrors": usdAcctngIfInErrors,
       "usdAcctngIfInUnknownProtos": usdAcctngIfInUnknownProtos,
       "usdAcctngIfOutOctets": usdAcctngIfOutOctets,
       "usdAcctngIfOutUcastPkts": usdAcctngIfOutUcastPkts,
       "usdAcctngIfOutDiscards": usdAcctngIfOutDiscards,
       "usdAcctngIfOutErrors": usdAcctngIfOutErrors,
       "usdAcctngIfCorrelator": usdAcctngIfCorrelator,
       "usdAcctngIfInPolicedOctets": usdAcctngIfInPolicedOctets,
       "usdAcctngIfInPolicedPkts": usdAcctngIfInPolicedPkts,
       "usdAcctngIfInSpoofedPkts": usdAcctngIfInSpoofedPkts,
       "usdAcctngIfOutPolicedOctets": usdAcctngIfOutPolicedOctets,
       "usdAcctngIfOutPolicedPkts": usdAcctngIfOutPolicedPkts,
       "usdAcctngIfOutSchedulerDropOctets": usdAcctngIfOutSchedulerDropOctets,
       "usdAcctngIfOutSchedulerDropPkts": usdAcctngIfOutSchedulerDropPkts,
       "usdAcctngIfLowerInterface": usdAcctngIfLowerInterface,
       "usdAcctngIfTimeOffset": usdAcctngIfTimeOffset,
       "usdAcctngifInMulticastPkts": usdAcctngifInMulticastPkts,
       "usdAcctngifInBroadcastPkts": usdAcctngifInBroadcastPkts,
       "usdAcctngifOutMulticastPkts": usdAcctngifOutMulticastPkts,
       "usdAcctngifOutBroadcastPkts": usdAcctngifOutBroadcastPkts,
       "usdAcctngSelectionSchemaIfStack": usdAcctngSelectionSchemaIfStack,
       "usdAcctngSelectionSchemaSystem": usdAcctngSelectionSchemaSystem,
       "usdAcctngSelectionSchemaPolicy": usdAcctngSelectionSchemaPolicy,
       "usdAcctngGreenPackets": usdAcctngGreenPackets,
       "usdAcctngUpperGreenPackets": usdAcctngUpperGreenPackets,
       "usdAcctngYellowPackets": usdAcctngYellowPackets,
       "usdAcctngUpperYellowPackets": usdAcctngUpperYellowPackets,
       "usdAcctngRedPackets": usdAcctngRedPackets,
       "usdAcctngUpperRedPackets": usdAcctngUpperRedPackets,
       "usdAcctngGreenBytes": usdAcctngGreenBytes,
       "usdAcctngUpperGreenBytes": usdAcctngUpperGreenBytes,
       "usdAcctngYellowBytes": usdAcctngYellowBytes,
       "usdAcctngUpperYellowBytes": usdAcctngUpperYellowBytes,
       "usdAcctngRedBytes": usdAcctngRedBytes,
       "usdAcctngUpperRedBytes": usdAcctngUpperRedBytes,
       "usdAcctngConformance": usdAcctngConformance,
       "usdAcctngGroups": usdAcctngGroups,
       "usdAcctngBasicGroup": usdAcctngBasicGroup,
       "usdAcctngBasicGroup2": usdAcctngBasicGroup2,
       "usdAcctngBasicGroup3": usdAcctngBasicGroup3,
       "usdAcctngCompliances": usdAcctngCompliances,
       "usdAcctngCompliance": usdAcctngCompliance,
       "usdAcctngCompliance2": usdAcctngCompliance2,
       "usdAcctngCompliance3": usdAcctngCompliance3}
)
