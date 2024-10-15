# SNMP MIB module (CENTILLION-IF-EXTENSIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CENTILLION-IF-EXTENSIONS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:06 2024
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

(BitField,
 Boolean,
 EnableIndicator,
 MacAddress,
 extensions) = mibBuilder.importSymbols(
    "CENTILLION-ROOT-MIB",
    "BitField",
    "Boolean",
    "EnableIndicator",
    "MacAddress",
    "extensions")

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

_CnIfExtensions_ObjectIdentity = ObjectIdentity
cnIfExtensions = _CnIfExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 3, 2)
)
_CnIfExtnTable_Object = MibTable
cnIfExtnTable = _CnIfExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cnIfExtnTable.setStatus("mandatory")
_CnIfExtnEntry_Object = MibTableRow
cnIfExtnEntry = _CnIfExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1)
)
cnIfExtnEntry.setIndexNames(
    (0, "CENTILLION-IF-EXTENSIONS-MIB", "cnIfExtnIndex"),
)
if mibBuilder.loadTexts:
    cnIfExtnEntry.setStatus("mandatory")
_CnIfExtnIndex_Type = Integer32
_CnIfExtnIndex_Object = MibTableColumn
cnIfExtnIndex = _CnIfExtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 1),
    _CnIfExtnIndex_Type()
)
cnIfExtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnIfExtnIndex.setStatus("mandatory")
_CnIfExtnCardNumber_Type = Integer32
_CnIfExtnCardNumber_Object = MibTableColumn
cnIfExtnCardNumber = _CnIfExtnCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 2),
    _CnIfExtnCardNumber_Type()
)
cnIfExtnCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnIfExtnCardNumber.setStatus("mandatory")
_CnIfExtnPortNumber_Type = Integer32
_CnIfExtnPortNumber_Object = MibTableColumn
cnIfExtnPortNumber = _CnIfExtnPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 3),
    _CnIfExtnPortNumber_Type()
)
cnIfExtnPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnIfExtnPortNumber.setStatus("mandatory")


class _CnIfFilterEnable_Type(Integer32):
    """Custom type cnIfFilterEnable based on Integer32"""
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
        *(("disableAllFilters", 2),
          ("enableInputAndOutputFilters", 4),
          ("enableInputFiltersOnly", 1),
          ("enableOutputFiltersOnly", 3))
    )


_CnIfFilterEnable_Type.__name__ = "Integer32"
_CnIfFilterEnable_Object = MibTableColumn
cnIfFilterEnable = _CnIfFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 4),
    _CnIfFilterEnable_Type()
)
cnIfFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnIfFilterEnable.setStatus("mandatory")
_CnIfFilterDownload_Type = BitField
_CnIfFilterDownload_Object = MibTableColumn
cnIfFilterDownload = _CnIfFilterDownload_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 5),
    _CnIfFilterDownload_Type()
)
cnIfFilterDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnIfFilterDownload.setStatus("mandatory")
_CnIfNetbiosNameFilteringState_Type = EnableIndicator
_CnIfNetbiosNameFilteringState_Object = MibTableColumn
cnIfNetbiosNameFilteringState = _CnIfNetbiosNameFilteringState_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 6),
    _CnIfNetbiosNameFilteringState_Type()
)
cnIfNetbiosNameFilteringState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnIfNetbiosNameFilteringState.setStatus("mandatory")
_CnIfNetbiosBcastDiscard_Type = Boolean
_CnIfNetbiosBcastDiscard_Object = MibTableColumn
cnIfNetbiosBcastDiscard = _CnIfNetbiosBcastDiscard_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 7),
    _CnIfNetbiosBcastDiscard_Type()
)
cnIfNetbiosBcastDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnIfNetbiosBcastDiscard.setStatus("mandatory")
_CnIfNetbiosNameProxyState_Type = EnableIndicator
_CnIfNetbiosNameProxyState_Object = MibTableColumn
cnIfNetbiosNameProxyState = _CnIfNetbiosNameProxyState_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 8),
    _CnIfNetbiosNameProxyState_Type()
)
cnIfNetbiosNameProxyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnIfNetbiosNameProxyState.setStatus("mandatory")
_CnIfForwardingIdentifier_Type = ObjectIdentifier
_CnIfForwardingIdentifier_Object = MibTableColumn
cnIfForwardingIdentifier = _CnIfForwardingIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 9),
    _CnIfForwardingIdentifier_Type()
)
cnIfForwardingIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnIfForwardingIdentifier.setStatus("mandatory")
_CnIfInNoResources_Type = Counter32
_CnIfInNoResources_Object = MibTableColumn
cnIfInNoResources = _CnIfInNoResources_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 10),
    _CnIfInNoResources_Type()
)
cnIfInNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnIfInNoResources.setStatus("mandatory")
_CnIfOutNoResources_Type = Counter32
_CnIfOutNoResources_Object = MibTableColumn
cnIfOutNoResources = _CnIfOutNoResources_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 11),
    _CnIfOutNoResources_Type()
)
cnIfOutNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnIfOutNoResources.setStatus("mandatory")
_CnIfVlanMismatch_Type = Counter32
_CnIfVlanMismatch_Object = MibTableColumn
cnIfVlanMismatch = _CnIfVlanMismatch_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 12),
    _CnIfVlanMismatch_Type()
)
cnIfVlanMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnIfVlanMismatch.setStatus("mandatory")


class _CnIfVlanCapabilities_Type(OctetString):
    """Custom type cnIfVlanCapabilities based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_CnIfVlanCapabilities_Type.__name__ = "OctetString"
_CnIfVlanCapabilities_Object = MibTableColumn
cnIfVlanCapabilities = _CnIfVlanCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 13),
    _CnIfVlanCapabilities_Type()
)
cnIfVlanCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnIfVlanCapabilities.setStatus("mandatory")
_CnIfExtnLocalAdminAddress_Type = MacAddress
_CnIfExtnLocalAdminAddress_Object = MibTableColumn
cnIfExtnLocalAdminAddress = _CnIfExtnLocalAdminAddress_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 14),
    _CnIfExtnLocalAdminAddress_Type()
)
cnIfExtnLocalAdminAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnIfExtnLocalAdminAddress.setStatus("mandatory")


class _CnIfExtnPhyAddressDefault_Type(Integer32):
    """Custom type cnIfExtnPhyAddressDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("useDefaultPhyAddress", 1),
          ("useLocallyAdministeredAddress", 2))
    )


_CnIfExtnPhyAddressDefault_Type.__name__ = "Integer32"
_CnIfExtnPhyAddressDefault_Object = MibTableColumn
cnIfExtnPhyAddressDefault = _CnIfExtnPhyAddressDefault_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 15),
    _CnIfExtnPhyAddressDefault_Type()
)
cnIfExtnPhyAddressDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnIfExtnPhyAddressDefault.setStatus("mandatory")
_CnIfVlanTrunk_Type = EnableIndicator
_CnIfVlanTrunk_Object = MibTableColumn
cnIfVlanTrunk = _CnIfVlanTrunk_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 16),
    _CnIfVlanTrunk_Type()
)
cnIfVlanTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnIfVlanTrunk.setStatus("mandatory")
_CnIfUsrInDiscards_Type = Counter32
_CnIfUsrInDiscards_Object = MibTableColumn
cnIfUsrInDiscards = _CnIfUsrInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 17),
    _CnIfUsrInDiscards_Type()
)
cnIfUsrInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnIfUsrInDiscards.setStatus("mandatory")
_CnIfUsrOutDiscards_Type = Counter32
_CnIfUsrOutDiscards_Object = MibTableColumn
cnIfUsrOutDiscards = _CnIfUsrOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 18),
    _CnIfUsrOutDiscards_Type()
)
cnIfUsrOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnIfUsrOutDiscards.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CENTILLION-IF-EXTENSIONS-MIB",
    **{"cnIfExtensions": cnIfExtensions,
       "cnIfExtnTable": cnIfExtnTable,
       "cnIfExtnEntry": cnIfExtnEntry,
       "cnIfExtnIndex": cnIfExtnIndex,
       "cnIfExtnCardNumber": cnIfExtnCardNumber,
       "cnIfExtnPortNumber": cnIfExtnPortNumber,
       "cnIfFilterEnable": cnIfFilterEnable,
       "cnIfFilterDownload": cnIfFilterDownload,
       "cnIfNetbiosNameFilteringState": cnIfNetbiosNameFilteringState,
       "cnIfNetbiosBcastDiscard": cnIfNetbiosBcastDiscard,
       "cnIfNetbiosNameProxyState": cnIfNetbiosNameProxyState,
       "cnIfForwardingIdentifier": cnIfForwardingIdentifier,
       "cnIfInNoResources": cnIfInNoResources,
       "cnIfOutNoResources": cnIfOutNoResources,
       "cnIfVlanMismatch": cnIfVlanMismatch,
       "cnIfVlanCapabilities": cnIfVlanCapabilities,
       "cnIfExtnLocalAdminAddress": cnIfExtnLocalAdminAddress,
       "cnIfExtnPhyAddressDefault": cnIfExtnPhyAddressDefault,
       "cnIfVlanTrunk": cnIfVlanTrunk,
       "cnIfUsrInDiscards": cnIfUsrInDiscards,
       "cnIfUsrOutDiscards": cnIfUsrOutDiscards}
)
