# SNMP MIB module (Wellfleet-NML-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-NML-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:47 2024
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
 Opaque,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 mgmt,
 mib_2) = mibBuilder.importSymbols(
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
    "Opaque",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mgmt",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfBridgeGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfBridgeGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfBrNativeModeLan_ObjectIdentity = ObjectIdentity
wfBrNativeModeLan = _WfBrNativeModeLan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 5)
)
_WfNmlBaseTable_Object = MibTable
wfNmlBaseTable = _WfNmlBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    wfNmlBaseTable.setStatus("mandatory")
_WfNmlBaseEntry_Object = MibTableRow
wfNmlBaseEntry = _WfNmlBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 5, 2, 1)
)
wfNmlBaseEntry.setIndexNames(
    (0, "Wellfleet-NML-MIB", "wfNmlCircuit"),
)
if mibBuilder.loadTexts:
    wfNmlBaseEntry.setStatus("mandatory")


class _WfNmlDelete_Type(Integer32):
    """Custom type wfNmlDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfNmlDelete_Type.__name__ = "Integer32"
_WfNmlDelete_Object = MibTableColumn
wfNmlDelete = _WfNmlDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 5, 2, 1, 1),
    _WfNmlDelete_Type()
)
wfNmlDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNmlDelete.setStatus("mandatory")


class _WfNmlDisable_Type(Integer32):
    """Custom type wfNmlDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfNmlDisable_Type.__name__ = "Integer32"
_WfNmlDisable_Object = MibTableColumn
wfNmlDisable = _WfNmlDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 5, 2, 1, 2),
    _WfNmlDisable_Type()
)
wfNmlDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNmlDisable.setStatus("mandatory")
_WfNmlCircuit_Type = Integer32
_WfNmlCircuit_Object = MibTableColumn
wfNmlCircuit = _WfNmlCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 5, 2, 1, 3),
    _WfNmlCircuit_Type()
)
wfNmlCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNmlCircuit.setStatus("mandatory")


class _WfNmlAddSecurityHeader_Type(Integer32):
    """Custom type wfNmlAddSecurityHeader based on Integer32"""
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
        *(("add", 1),
          ("check", 2),
          ("drop", 3))
    )


_WfNmlAddSecurityHeader_Type.__name__ = "Integer32"
_WfNmlAddSecurityHeader_Object = MibTableColumn
wfNmlAddSecurityHeader = _WfNmlAddSecurityHeader_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 5, 2, 1, 4),
    _WfNmlAddSecurityHeader_Type()
)
wfNmlAddSecurityHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNmlAddSecurityHeader.setStatus("mandatory")


class _WfNmlSAIDType_Type(Integer32):
    """Custom type wfNmlSAIDType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("group", 2),
          ("individual", 1))
    )


_WfNmlSAIDType_Type.__name__ = "Integer32"
_WfNmlSAIDType_Object = MibTableColumn
wfNmlSAIDType = _WfNmlSAIDType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 5, 2, 1, 5),
    _WfNmlSAIDType_Type()
)
wfNmlSAIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNmlSAIDType.setStatus("mandatory")
_WfNmlSAIDValue_Type = Integer32
_WfNmlSAIDValue_Object = MibTableColumn
wfNmlSAIDValue = _WfNmlSAIDValue_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 5, 2, 1, 6),
    _WfNmlSAIDValue_Type()
)
wfNmlSAIDValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNmlSAIDValue.setStatus("mandatory")
_WfNmlCUGValue_Type = Integer32
_WfNmlCUGValue_Object = MibTableColumn
wfNmlCUGValue = _WfNmlCUGValue_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 5, 2, 1, 7),
    _WfNmlCUGValue_Type()
)
wfNmlCUGValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNmlCUGValue.setStatus("mandatory")


class _WfNmlCUGDrop_Type(Integer32):
    """Custom type wfNmlCUGDrop based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("forward", 2))
    )


_WfNmlCUGDrop_Type.__name__ = "Integer32"
_WfNmlCUGDrop_Object = MibTableColumn
wfNmlCUGDrop = _WfNmlCUGDrop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 5, 2, 1, 8),
    _WfNmlCUGDrop_Type()
)
wfNmlCUGDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNmlCUGDrop.setStatus("mandatory")
_WfNmlCUGPacketsDropped_Type = Integer32
_WfNmlCUGPacketsDropped_Object = MibTableColumn
wfNmlCUGPacketsDropped = _WfNmlCUGPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 5, 2, 1, 9),
    _WfNmlCUGPacketsDropped_Type()
)
wfNmlCUGPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNmlCUGPacketsDropped.setStatus("mandatory")
_WfNmlTrafficFilterTable_Object = MibTable
wfNmlTrafficFilterTable = _WfNmlTrafficFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 5, 3)
)
if mibBuilder.loadTexts:
    wfNmlTrafficFilterTable.setStatus("mandatory")
_WfNmlTrafficFilterEntry_Object = MibTableRow
wfNmlTrafficFilterEntry = _WfNmlTrafficFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 5, 3, 1)
)
wfNmlTrafficFilterEntry.setIndexNames(
    (0, "Wellfleet-NML-MIB", "wfNmlTrafficFilterCircuit"),
    (0, "Wellfleet-NML-MIB", "wfNmlTrafficFilterRuleNumber"),
    (0, "Wellfleet-NML-MIB", "wfNmlTrafficFilterFragment"),
)
if mibBuilder.loadTexts:
    wfNmlTrafficFilterEntry.setStatus("mandatory")


class _WfNmlTrafficFilterCreate_Type(Integer32):
    """Custom type wfNmlTrafficFilterCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfNmlTrafficFilterCreate_Type.__name__ = "Integer32"
_WfNmlTrafficFilterCreate_Object = MibTableColumn
wfNmlTrafficFilterCreate = _WfNmlTrafficFilterCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 5, 3, 1, 1),
    _WfNmlTrafficFilterCreate_Type()
)
wfNmlTrafficFilterCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNmlTrafficFilterCreate.setStatus("mandatory")


class _WfNmlTrafficFilterEnable_Type(Integer32):
    """Custom type wfNmlTrafficFilterEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfNmlTrafficFilterEnable_Type.__name__ = "Integer32"
_WfNmlTrafficFilterEnable_Object = MibTableColumn
wfNmlTrafficFilterEnable = _WfNmlTrafficFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 5, 3, 1, 2),
    _WfNmlTrafficFilterEnable_Type()
)
wfNmlTrafficFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNmlTrafficFilterEnable.setStatus("mandatory")


class _WfNmlTrafficFilterStatus_Type(Integer32):
    """Custom type wfNmlTrafficFilterStatus based on Integer32"""
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
        *(("active", 1),
          ("error", 2),
          ("inactive", 3))
    )


_WfNmlTrafficFilterStatus_Type.__name__ = "Integer32"
_WfNmlTrafficFilterStatus_Object = MibTableColumn
wfNmlTrafficFilterStatus = _WfNmlTrafficFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 5, 3, 1, 3),
    _WfNmlTrafficFilterStatus_Type()
)
wfNmlTrafficFilterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNmlTrafficFilterStatus.setStatus("mandatory")
_WfNmlTrafficFilterCounter_Type = Counter32
_WfNmlTrafficFilterCounter_Object = MibTableColumn
wfNmlTrafficFilterCounter = _WfNmlTrafficFilterCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 5, 3, 1, 4),
    _WfNmlTrafficFilterCounter_Type()
)
wfNmlTrafficFilterCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNmlTrafficFilterCounter.setStatus("mandatory")
_WfNmlTrafficFilterDefinition_Type = Opaque
_WfNmlTrafficFilterDefinition_Object = MibTableColumn
wfNmlTrafficFilterDefinition = _WfNmlTrafficFilterDefinition_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 5, 3, 1, 5),
    _WfNmlTrafficFilterDefinition_Type()
)
wfNmlTrafficFilterDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNmlTrafficFilterDefinition.setStatus("mandatory")
_WfNmlTrafficFilterReserved_Type = Integer32
_WfNmlTrafficFilterReserved_Object = MibTableColumn
wfNmlTrafficFilterReserved = _WfNmlTrafficFilterReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 5, 3, 1, 6),
    _WfNmlTrafficFilterReserved_Type()
)
wfNmlTrafficFilterReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNmlTrafficFilterReserved.setStatus("mandatory")
_WfNmlTrafficFilterCircuit_Type = Integer32
_WfNmlTrafficFilterCircuit_Object = MibTableColumn
wfNmlTrafficFilterCircuit = _WfNmlTrafficFilterCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 5, 3, 1, 7),
    _WfNmlTrafficFilterCircuit_Type()
)
wfNmlTrafficFilterCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNmlTrafficFilterCircuit.setStatus("mandatory")
_WfNmlTrafficFilterRuleNumber_Type = Integer32
_WfNmlTrafficFilterRuleNumber_Object = MibTableColumn
wfNmlTrafficFilterRuleNumber = _WfNmlTrafficFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 5, 3, 1, 8),
    _WfNmlTrafficFilterRuleNumber_Type()
)
wfNmlTrafficFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNmlTrafficFilterRuleNumber.setStatus("mandatory")
_WfNmlTrafficFilterFragment_Type = Integer32
_WfNmlTrafficFilterFragment_Object = MibTableColumn
wfNmlTrafficFilterFragment = _WfNmlTrafficFilterFragment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 5, 3, 1, 9),
    _WfNmlTrafficFilterFragment_Type()
)
wfNmlTrafficFilterFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNmlTrafficFilterFragment.setStatus("mandatory")
_WfNmlTrafficFilterName_Type = DisplayString
_WfNmlTrafficFilterName_Object = MibTableColumn
wfNmlTrafficFilterName = _WfNmlTrafficFilterName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 5, 3, 1, 10),
    _WfNmlTrafficFilterName_Type()
)
wfNmlTrafficFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNmlTrafficFilterName.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-NML-MIB",
    **{"wfBrNativeModeLan": wfBrNativeModeLan,
       "wfNmlBaseTable": wfNmlBaseTable,
       "wfNmlBaseEntry": wfNmlBaseEntry,
       "wfNmlDelete": wfNmlDelete,
       "wfNmlDisable": wfNmlDisable,
       "wfNmlCircuit": wfNmlCircuit,
       "wfNmlAddSecurityHeader": wfNmlAddSecurityHeader,
       "wfNmlSAIDType": wfNmlSAIDType,
       "wfNmlSAIDValue": wfNmlSAIDValue,
       "wfNmlCUGValue": wfNmlCUGValue,
       "wfNmlCUGDrop": wfNmlCUGDrop,
       "wfNmlCUGPacketsDropped": wfNmlCUGPacketsDropped,
       "wfNmlTrafficFilterTable": wfNmlTrafficFilterTable,
       "wfNmlTrafficFilterEntry": wfNmlTrafficFilterEntry,
       "wfNmlTrafficFilterCreate": wfNmlTrafficFilterCreate,
       "wfNmlTrafficFilterEnable": wfNmlTrafficFilterEnable,
       "wfNmlTrafficFilterStatus": wfNmlTrafficFilterStatus,
       "wfNmlTrafficFilterCounter": wfNmlTrafficFilterCounter,
       "wfNmlTrafficFilterDefinition": wfNmlTrafficFilterDefinition,
       "wfNmlTrafficFilterReserved": wfNmlTrafficFilterReserved,
       "wfNmlTrafficFilterCircuit": wfNmlTrafficFilterCircuit,
       "wfNmlTrafficFilterRuleNumber": wfNmlTrafficFilterRuleNumber,
       "wfNmlTrafficFilterFragment": wfNmlTrafficFilterFragment,
       "wfNmlTrafficFilterName": wfNmlTrafficFilterName}
)
