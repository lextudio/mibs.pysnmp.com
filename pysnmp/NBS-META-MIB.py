# SNMP MIB module (NBS-META-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NBS-META-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:51 2024
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

(InterfaceIndex,
 nbs) = mibBuilder.importSymbols(
    "NBS-CMMC-MIB",
    "InterfaceIndex",
    "nbs")

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

metaMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 205)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MetaMibGrp_ObjectIdentity = ObjectIdentity
metaMibGrp = _MetaMibGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 205, 1)
)
if mibBuilder.loadTexts:
    metaMibGrp.setStatus("current")
_MetaMibFeatureTableSize_Type = Integer32
_MetaMibFeatureTableSize_Object = MibScalar
metaMibFeatureTableSize = _MetaMibFeatureTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 1),
    _MetaMibFeatureTableSize_Type()
)
metaMibFeatureTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metaMibFeatureTableSize.setStatus("current")
_MetaMibFeatureTable_Object = MibTable
metaMibFeatureTable = _MetaMibFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 2)
)
if mibBuilder.loadTexts:
    metaMibFeatureTable.setStatus("current")
_MetaMibFeatureEntry_Object = MibTableRow
metaMibFeatureEntry = _MetaMibFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 2, 1)
)
metaMibFeatureEntry.setIndexNames(
    (0, "NBS-META-MIB", "metaMibFeatureID"),
)
if mibBuilder.loadTexts:
    metaMibFeatureEntry.setStatus("current")
_MetaMibFeatureID_Type = Integer32
_MetaMibFeatureID_Object = MibTableColumn
metaMibFeatureID = _MetaMibFeatureID_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 2, 1, 1),
    _MetaMibFeatureID_Type()
)
metaMibFeatureID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    metaMibFeatureID.setStatus("current")


class _MetaMibFeatureFamily_Type(DisplayString):
    """Custom type metaMibFeatureFamily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MetaMibFeatureFamily_Type.__name__ = "DisplayString"
_MetaMibFeatureFamily_Object = MibTableColumn
metaMibFeatureFamily = _MetaMibFeatureFamily_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 2, 1, 2),
    _MetaMibFeatureFamily_Type()
)
metaMibFeatureFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metaMibFeatureFamily.setStatus("current")


class _MetaMibFeatureName_Type(DisplayString):
    """Custom type metaMibFeatureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MetaMibFeatureName_Type.__name__ = "DisplayString"
_MetaMibFeatureName_Object = MibTableColumn
metaMibFeatureName = _MetaMibFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 2, 1, 3),
    _MetaMibFeatureName_Type()
)
metaMibFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metaMibFeatureName.setStatus("current")
_MetaMibFeatureDesc_Type = DisplayString
_MetaMibFeatureDesc_Object = MibTableColumn
metaMibFeatureDesc = _MetaMibFeatureDesc_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 2, 1, 4),
    _MetaMibFeatureDesc_Type()
)
metaMibFeatureDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metaMibFeatureDesc.setStatus("current")


class _MetaMibFeatureUnits_Type(DisplayString):
    """Custom type metaMibFeatureUnits based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MetaMibFeatureUnits_Type.__name__ = "DisplayString"
_MetaMibFeatureUnits_Object = MibTableColumn
metaMibFeatureUnits = _MetaMibFeatureUnits_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 2, 1, 5),
    _MetaMibFeatureUnits_Type()
)
metaMibFeatureUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metaMibFeatureUnits.setStatus("current")


class _MetaMibFeatureType_Type(Integer32):
    """Custom type metaMibFeatureType based on Integer32"""
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
        *(("enum", 1),
          ("float", 4),
          ("integer", 3),
          ("string", 2))
    )


_MetaMibFeatureType_Type.__name__ = "Integer32"
_MetaMibFeatureType_Object = MibTableColumn
metaMibFeatureType = _MetaMibFeatureType_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 2, 1, 6),
    _MetaMibFeatureType_Type()
)
metaMibFeatureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metaMibFeatureType.setStatus("current")
_MetaMibVariableTableSize_Type = Integer32
_MetaMibVariableTableSize_Object = MibScalar
metaMibVariableTableSize = _MetaMibVariableTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 3),
    _MetaMibVariableTableSize_Type()
)
metaMibVariableTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metaMibVariableTableSize.setStatus("current")
_MetaMibVariableTable_Object = MibTable
metaMibVariableTable = _MetaMibVariableTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 4)
)
if mibBuilder.loadTexts:
    metaMibVariableTable.setStatus("current")
_MetaMibVariableEntry_Object = MibTableRow
metaMibVariableEntry = _MetaMibVariableEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1)
)
metaMibVariableEntry.setIndexNames(
    (0, "NBS-META-MIB", "metaMibVariableIfIndex"),
    (0, "NBS-META-MIB", "metaMibVariableID"),
)
if mibBuilder.loadTexts:
    metaMibVariableEntry.setStatus("current")
_MetaMibVariableIfIndex_Type = InterfaceIndex
_MetaMibVariableIfIndex_Object = MibTableColumn
metaMibVariableIfIndex = _MetaMibVariableIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 1),
    _MetaMibVariableIfIndex_Type()
)
metaMibVariableIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    metaMibVariableIfIndex.setStatus("current")
_MetaMibVariableID_Type = Integer32
_MetaMibVariableID_Object = MibTableColumn
metaMibVariableID = _MetaMibVariableID_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 2),
    _MetaMibVariableID_Type()
)
metaMibVariableID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    metaMibVariableID.setStatus("current")


class _MetaMibVariableCaps_Type(DisplayString):
    """Custom type metaMibVariableCaps based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MetaMibVariableCaps_Type.__name__ = "DisplayString"
_MetaMibVariableCaps_Object = MibTableColumn
metaMibVariableCaps = _MetaMibVariableCaps_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 3),
    _MetaMibVariableCaps_Type()
)
metaMibVariableCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metaMibVariableCaps.setStatus("current")


class _MetaMibVariableDefault_Type(DisplayString):
    """Custom type metaMibVariableDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MetaMibVariableDefault_Type.__name__ = "DisplayString"
_MetaMibVariableDefault_Object = MibTableColumn
metaMibVariableDefault = _MetaMibVariableDefault_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 4),
    _MetaMibVariableDefault_Type()
)
metaMibVariableDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metaMibVariableDefault.setStatus("current")


class _MetaMibVariableJumper_Type(DisplayString):
    """Custom type metaMibVariableJumper based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MetaMibVariableJumper_Type.__name__ = "DisplayString"
_MetaMibVariableJumper_Object = MibTableColumn
metaMibVariableJumper = _MetaMibVariableJumper_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 5),
    _MetaMibVariableJumper_Type()
)
metaMibVariableJumper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metaMibVariableJumper.setStatus("current")


class _MetaMibVariableOper_Type(DisplayString):
    """Custom type metaMibVariableOper based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MetaMibVariableOper_Type.__name__ = "DisplayString"
_MetaMibVariableOper_Object = MibTableColumn
metaMibVariableOper = _MetaMibVariableOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 6),
    _MetaMibVariableOper_Type()
)
metaMibVariableOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metaMibVariableOper.setStatus("current")


class _MetaMibVariableAdmin_Type(DisplayString):
    """Custom type metaMibVariableAdmin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MetaMibVariableAdmin_Type.__name__ = "DisplayString"
_MetaMibVariableAdmin_Object = MibTableColumn
metaMibVariableAdmin = _MetaMibVariableAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 7),
    _MetaMibVariableAdmin_Type()
)
metaMibVariableAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    metaMibVariableAdmin.setStatus("current")


class _MetaMibVariableStatus_Type(DisplayString):
    """Custom type metaMibVariableStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MetaMibVariableStatus_Type.__name__ = "DisplayString"
_MetaMibVariableStatus_Object = MibTableColumn
metaMibVariableStatus = _MetaMibVariableStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 8),
    _MetaMibVariableStatus_Type()
)
metaMibVariableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metaMibVariableStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-META-MIB",
    **{"metaMib": metaMib,
       "metaMibGrp": metaMibGrp,
       "metaMibFeatureTableSize": metaMibFeatureTableSize,
       "metaMibFeatureTable": metaMibFeatureTable,
       "metaMibFeatureEntry": metaMibFeatureEntry,
       "metaMibFeatureID": metaMibFeatureID,
       "metaMibFeatureFamily": metaMibFeatureFamily,
       "metaMibFeatureName": metaMibFeatureName,
       "metaMibFeatureDesc": metaMibFeatureDesc,
       "metaMibFeatureUnits": metaMibFeatureUnits,
       "metaMibFeatureType": metaMibFeatureType,
       "metaMibVariableTableSize": metaMibVariableTableSize,
       "metaMibVariableTable": metaMibVariableTable,
       "metaMibVariableEntry": metaMibVariableEntry,
       "metaMibVariableIfIndex": metaMibVariableIfIndex,
       "metaMibVariableID": metaMibVariableID,
       "metaMibVariableCaps": metaMibVariableCaps,
       "metaMibVariableDefault": metaMibVariableDefault,
       "metaMibVariableJumper": metaMibVariableJumper,
       "metaMibVariableOper": metaMibVariableOper,
       "metaMibVariableAdmin": metaMibVariableAdmin,
       "metaMibVariableStatus": metaMibVariableStatus}
)
