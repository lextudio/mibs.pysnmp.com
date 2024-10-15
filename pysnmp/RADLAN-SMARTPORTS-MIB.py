# SNMP MIB module (RADLAN-SMARTPORTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-SMARTPORTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:07 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rlSmartPorts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 140)
)
rlSmartPorts.setRevisions(
        ("2008-07-30 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MacroType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rlSmartPortsMacroGloablVendorProvided", 2),
          ("rlSmartPortsMacroInterfaceVendorProvided", 1),
          ("rlSmartPortsMacroUserCreated", 3))
    )



class RlSmartPortsMacroName(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class RlSmartPortsMacroNameOrZero(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



# MIB Managed Objects in the order of their OIDs

_RlSmartPortsMacroManageTable_Object = MibTable
rlSmartPortsMacroManageTable = _RlSmartPortsMacroManageTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 140, 1)
)
if mibBuilder.loadTexts:
    rlSmartPortsMacroManageTable.setStatus("current")
_RlSmartPortsMacroManageEntry_Object = MibTableRow
rlSmartPortsMacroManageEntry = _RlSmartPortsMacroManageEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 140, 1, 1)
)
rlSmartPortsMacroManageEntry.setIndexNames(
    (1, "RADLAN-SMARTPORTS-MIB", "rlSmartPortsMacroName"),
)
if mibBuilder.loadTexts:
    rlSmartPortsMacroManageEntry.setStatus("current")
_RlSmartPortsMacroName_Type = RlSmartPortsMacroName
_RlSmartPortsMacroName_Object = MibTableColumn
rlSmartPortsMacroName = _RlSmartPortsMacroName_Object(
    (1, 3, 6, 1, 4, 1, 89, 140, 1, 1, 1),
    _RlSmartPortsMacroName_Type()
)
rlSmartPortsMacroName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSmartPortsMacroName.setStatus("current")
_RlSmartPortsMacroIndex_Type = Integer32
_RlSmartPortsMacroIndex_Object = MibTableColumn
rlSmartPortsMacroIndex = _RlSmartPortsMacroIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 140, 1, 1, 2),
    _RlSmartPortsMacroIndex_Type()
)
rlSmartPortsMacroIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSmartPortsMacroIndex.setStatus("current")
_RlSmartPortsMacroType_Type = MacroType
_RlSmartPortsMacroType_Object = MibTableColumn
rlSmartPortsMacroType = _RlSmartPortsMacroType_Object(
    (1, 3, 6, 1, 4, 1, 89, 140, 1, 1, 3),
    _RlSmartPortsMacroType_Type()
)
rlSmartPortsMacroType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSmartPortsMacroType.setStatus("current")
_RlSmartPortsMacroStatus_Type = RowStatus
_RlSmartPortsMacroStatus_Object = MibTableColumn
rlSmartPortsMacroStatus = _RlSmartPortsMacroStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 140, 1, 1, 4),
    _RlSmartPortsMacroStatus_Type()
)
rlSmartPortsMacroStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSmartPortsMacroStatus.setStatus("current")


class _RlSmartPortsMacroKeywords_Type(DisplayString):
    """Custom type rlSmartPortsMacroKeywords based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlSmartPortsMacroKeywords_Type.__name__ = "DisplayString"
_RlSmartPortsMacroKeywords_Object = MibTableColumn
rlSmartPortsMacroKeywords = _RlSmartPortsMacroKeywords_Object(
    (1, 3, 6, 1, 4, 1, 89, 140, 1, 1, 5),
    _RlSmartPortsMacroKeywords_Type()
)
rlSmartPortsMacroKeywords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSmartPortsMacroKeywords.setStatus("current")


class _RlSmartPortsMacroDesc1_Type(DisplayString):
    """Custom type rlSmartPortsMacroDesc1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlSmartPortsMacroDesc1_Type.__name__ = "DisplayString"
_RlSmartPortsMacroDesc1_Object = MibTableColumn
rlSmartPortsMacroDesc1 = _RlSmartPortsMacroDesc1_Object(
    (1, 3, 6, 1, 4, 1, 89, 140, 1, 1, 6),
    _RlSmartPortsMacroDesc1_Type()
)
rlSmartPortsMacroDesc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSmartPortsMacroDesc1.setStatus("current")


class _RlSmartPortsMacroDesc2_Type(DisplayString):
    """Custom type rlSmartPortsMacroDesc2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlSmartPortsMacroDesc2_Type.__name__ = "DisplayString"
_RlSmartPortsMacroDesc2_Object = MibTableColumn
rlSmartPortsMacroDesc2 = _RlSmartPortsMacroDesc2_Object(
    (1, 3, 6, 1, 4, 1, 89, 140, 1, 1, 7),
    _RlSmartPortsMacroDesc2_Type()
)
rlSmartPortsMacroDesc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSmartPortsMacroDesc2.setStatus("current")
_RlSmartPortsMacroContentTable_Object = MibTable
rlSmartPortsMacroContentTable = _RlSmartPortsMacroContentTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 140, 2)
)
if mibBuilder.loadTexts:
    rlSmartPortsMacroContentTable.setStatus("current")
_RlSmartPortsMacroContentEntry_Object = MibTableRow
rlSmartPortsMacroContentEntry = _RlSmartPortsMacroContentEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 140, 2, 1)
)
rlSmartPortsMacroContentEntry.setIndexNames(
    (0, "RADLAN-SMARTPORTS-MIB", "rlSmartPortsMacroIndex"),
    (0, "RADLAN-SMARTPORTS-MIB", "rlSmartPortsMacroOctetIndex"),
)
if mibBuilder.loadTexts:
    rlSmartPortsMacroContentEntry.setStatus("current")


class _RlSmartPortsMacroOctetIndex_Type(Integer32):
    """Custom type rlSmartPortsMacroOctetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_RlSmartPortsMacroOctetIndex_Type.__name__ = "Integer32"
_RlSmartPortsMacroOctetIndex_Object = MibTableColumn
rlSmartPortsMacroOctetIndex = _RlSmartPortsMacroOctetIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 140, 2, 1, 1),
    _RlSmartPortsMacroOctetIndex_Type()
)
rlSmartPortsMacroOctetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSmartPortsMacroOctetIndex.setStatus("current")
_RlSmartPortsMacroText_Type = SnmpAdminString
_RlSmartPortsMacroText_Object = MibTableColumn
rlSmartPortsMacroText = _RlSmartPortsMacroText_Object(
    (1, 3, 6, 1, 4, 1, 89, 140, 2, 1, 2),
    _RlSmartPortsMacroText_Type()
)
rlSmartPortsMacroText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSmartPortsMacroText.setStatus("current")
_RlSmartPortsMacroDescriptionTable_Object = MibTable
rlSmartPortsMacroDescriptionTable = _RlSmartPortsMacroDescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 140, 3)
)
if mibBuilder.loadTexts:
    rlSmartPortsMacroDescriptionTable.setStatus("current")
_RlSmartPortsMacroDescriptionEntry_Object = MibTableRow
rlSmartPortsMacroDescriptionEntry = _RlSmartPortsMacroDescriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 140, 3, 1)
)
rlSmartPortsMacroDescriptionEntry.setIndexNames(
    (0, "RADLAN-SMARTPORTS-MIB", "rlSmartPortsMacroDescriptionIndex"),
)
if mibBuilder.loadTexts:
    rlSmartPortsMacroDescriptionEntry.setStatus("current")
_RlSmartPortsMacroDescriptionIndex_Type = InterfaceIndexOrZero
_RlSmartPortsMacroDescriptionIndex_Object = MibTableColumn
rlSmartPortsMacroDescriptionIndex = _RlSmartPortsMacroDescriptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 140, 3, 1, 1),
    _RlSmartPortsMacroDescriptionIndex_Type()
)
rlSmartPortsMacroDescriptionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSmartPortsMacroDescriptionIndex.setStatus("current")
_RlSmartPortsMacroDescriptionText_Type = SnmpAdminString
_RlSmartPortsMacroDescriptionText_Object = MibTableColumn
rlSmartPortsMacroDescriptionText = _RlSmartPortsMacroDescriptionText_Object(
    (1, 3, 6, 1, 4, 1, 89, 140, 3, 1, 2),
    _RlSmartPortsMacroDescriptionText_Type()
)
rlSmartPortsMacroDescriptionText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSmartPortsMacroDescriptionText.setStatus("current")
_RlSmartPortsMacroDescriptionStatus_Type = RowStatus
_RlSmartPortsMacroDescriptionStatus_Object = MibTableColumn
rlSmartPortsMacroDescriptionStatus = _RlSmartPortsMacroDescriptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 140, 3, 1, 3),
    _RlSmartPortsMacroDescriptionStatus_Type()
)
rlSmartPortsMacroDescriptionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSmartPortsMacroDescriptionStatus.setStatus("current")
_RlSmartPortsFreeIndexes_Type = Integer32
_RlSmartPortsFreeIndexes_Object = MibScalar
rlSmartPortsFreeIndexes = _RlSmartPortsFreeIndexes_Object(
    (1, 3, 6, 1, 4, 1, 89, 140, 4),
    _RlSmartPortsFreeIndexes_Type()
)
rlSmartPortsFreeIndexes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSmartPortsFreeIndexes.setStatus("current")


class _RlSmartPortsDiagMacroName_Type(DisplayString):
    """Custom type rlSmartPortsDiagMacroName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlSmartPortsDiagMacroName_Type.__name__ = "DisplayString"
_RlSmartPortsDiagMacroName_Object = MibScalar
rlSmartPortsDiagMacroName = _RlSmartPortsDiagMacroName_Object(
    (1, 3, 6, 1, 4, 1, 89, 140, 5),
    _RlSmartPortsDiagMacroName_Type()
)
rlSmartPortsDiagMacroName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSmartPortsDiagMacroName.setStatus("current")
_RlSmartPortsDiagLineNumber_Type = Integer32
_RlSmartPortsDiagLineNumber_Object = MibScalar
rlSmartPortsDiagLineNumber = _RlSmartPortsDiagLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 140, 6),
    _RlSmartPortsDiagLineNumber_Type()
)
rlSmartPortsDiagLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSmartPortsDiagLineNumber.setStatus("current")
_RlSmartPortsDiagCommandLine_Type = SnmpAdminString
_RlSmartPortsDiagCommandLine_Object = MibScalar
rlSmartPortsDiagCommandLine = _RlSmartPortsDiagCommandLine_Object(
    (1, 3, 6, 1, 4, 1, 89, 140, 7),
    _RlSmartPortsDiagCommandLine_Type()
)
rlSmartPortsDiagCommandLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSmartPortsDiagCommandLine.setStatus("current")


class _RlSmartPortsCondenseMode_Type(Integer32):
    """Custom type rlSmartPortsCondenseMode based on Integer32"""
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


_RlSmartPortsCondenseMode_Type.__name__ = "Integer32"
_RlSmartPortsCondenseMode_Object = MibScalar
rlSmartPortsCondenseMode = _RlSmartPortsCondenseMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 140, 8),
    _RlSmartPortsCondenseMode_Type()
)
rlSmartPortsCondenseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSmartPortsCondenseMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-SMARTPORTS-MIB",
    **{"MacroType": MacroType,
       "RlSmartPortsMacroName": RlSmartPortsMacroName,
       "RlSmartPortsMacroNameOrZero": RlSmartPortsMacroNameOrZero,
       "rlSmartPorts": rlSmartPorts,
       "rlSmartPortsMacroManageTable": rlSmartPortsMacroManageTable,
       "rlSmartPortsMacroManageEntry": rlSmartPortsMacroManageEntry,
       "rlSmartPortsMacroName": rlSmartPortsMacroName,
       "rlSmartPortsMacroIndex": rlSmartPortsMacroIndex,
       "rlSmartPortsMacroType": rlSmartPortsMacroType,
       "rlSmartPortsMacroStatus": rlSmartPortsMacroStatus,
       "rlSmartPortsMacroKeywords": rlSmartPortsMacroKeywords,
       "rlSmartPortsMacroDesc1": rlSmartPortsMacroDesc1,
       "rlSmartPortsMacroDesc2": rlSmartPortsMacroDesc2,
       "rlSmartPortsMacroContentTable": rlSmartPortsMacroContentTable,
       "rlSmartPortsMacroContentEntry": rlSmartPortsMacroContentEntry,
       "rlSmartPortsMacroOctetIndex": rlSmartPortsMacroOctetIndex,
       "rlSmartPortsMacroText": rlSmartPortsMacroText,
       "rlSmartPortsMacroDescriptionTable": rlSmartPortsMacroDescriptionTable,
       "rlSmartPortsMacroDescriptionEntry": rlSmartPortsMacroDescriptionEntry,
       "rlSmartPortsMacroDescriptionIndex": rlSmartPortsMacroDescriptionIndex,
       "rlSmartPortsMacroDescriptionText": rlSmartPortsMacroDescriptionText,
       "rlSmartPortsMacroDescriptionStatus": rlSmartPortsMacroDescriptionStatus,
       "rlSmartPortsFreeIndexes": rlSmartPortsFreeIndexes,
       "rlSmartPortsDiagMacroName": rlSmartPortsDiagMacroName,
       "rlSmartPortsDiagLineNumber": rlSmartPortsDiagLineNumber,
       "rlSmartPortsDiagCommandLine": rlSmartPortsDiagCommandLine,
       "rlSmartPortsCondenseMode": rlSmartPortsCondenseMode}
)
