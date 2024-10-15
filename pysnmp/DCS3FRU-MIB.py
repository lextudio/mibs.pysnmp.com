# SNMP MIB module (DCS3FRU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DCS3FRU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:26 2024
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
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DellObjectRange(Integer32):
    """Custom type DellObjectRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )





class DellUnsigned8BitRange(Integer32):
    """Custom type DellUnsigned8BitRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class DellUnsigned16BitRange(Integer32):
    """Custom type DellUnsigned16BitRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class DellUnsigned32BitRange(Integer32):
    """Custom type DellUnsigned32BitRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )





class DellDateName(DisplayString):
    """Custom type DellDateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 25),
    )





class DellStatus(Integer32):
    """Custom type DellStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("critical", 5),
          ("nonCritical", 4),
          ("nonRecoverable", 6),
          ("ok", 3),
          ("other", 1),
          ("unknown", 2))
    )





class DellFRUInformationState(Integer32):
    """Custom type DellFRUInformationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("checksumInvalid", 4),
          ("corrupted", 5),
          ("notAvailable", 3),
          ("notSupported", 2),
          ("ok", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dell_ObjectIdentity = ObjectIdentity
dell = _Dell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674)
)
_Server3_ObjectIdentity = ObjectIdentity
server3 = _Server3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892)
)
_BaseboardGroup_ObjectIdentity = ObjectIdentity
baseboardGroup = _BaseboardGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1)
)
_FruGroup_ObjectIdentity = ObjectIdentity
fruGroup = _FruGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000)
)
_FruTable_Object = MibTable
fruTable = _FruTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10)
)
if mibBuilder.loadTexts:
    fruTable.setStatus("mandatory")
_FruTableEntry_Object = MibTableRow
fruTableEntry = _FruTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1)
)
fruTableEntry.setIndexNames(
    (0, "DCS3FRU-MIB", "fruChassisIndex"),
    (0, "DCS3FRU-MIB", "fruIndex"),
)
if mibBuilder.loadTexts:
    fruTableEntry.setStatus("mandatory")
_FruChassisIndex_Type = DellObjectRange
_FruChassisIndex_Object = MibTableColumn
fruChassisIndex = _FruChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 1),
    _FruChassisIndex_Type()
)
fruChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruChassisIndex.setStatus("mandatory")
_FruIndex_Type = DellObjectRange
_FruIndex_Object = MibTableColumn
fruIndex = _FruIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 2),
    _FruIndex_Type()
)
fruIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruIndex.setStatus("mandatory")
_FruInformationStatus_Type = DellStatus
_FruInformationStatus_Object = MibTableColumn
fruInformationStatus = _FruInformationStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 3),
    _FruInformationStatus_Type()
)
fruInformationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruInformationStatus.setStatus("mandatory")
_FruInformationState_Type = DellFRUInformationState
_FruInformationState_Object = MibTableColumn
fruInformationState = _FruInformationState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 4),
    _FruInformationState_Type()
)
fruInformationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruInformationState.setStatus("mandatory")


class _FruDeviceName_Type(DisplayString):
    """Custom type fruDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FruDeviceName_Type.__name__ = "DisplayString"
_FruDeviceName_Object = MibTableColumn
fruDeviceName = _FruDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 5),
    _FruDeviceName_Type()
)
fruDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruDeviceName.setStatus("mandatory")


class _FruManufacturerName_Type(DisplayString):
    """Custom type fruManufacturerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FruManufacturerName_Type.__name__ = "DisplayString"
_FruManufacturerName_Object = MibTableColumn
fruManufacturerName = _FruManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 6),
    _FruManufacturerName_Type()
)
fruManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruManufacturerName.setStatus("mandatory")


class _FruSerialNumberName_Type(DisplayString):
    """Custom type fruSerialNumberName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FruSerialNumberName_Type.__name__ = "DisplayString"
_FruSerialNumberName_Object = MibTableColumn
fruSerialNumberName = _FruSerialNumberName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 7),
    _FruSerialNumberName_Type()
)
fruSerialNumberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruSerialNumberName.setStatus("mandatory")


class _FruPartNumberName_Type(DisplayString):
    """Custom type fruPartNumberName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FruPartNumberName_Type.__name__ = "DisplayString"
_FruPartNumberName_Object = MibTableColumn
fruPartNumberName = _FruPartNumberName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 8),
    _FruPartNumberName_Type()
)
fruPartNumberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruPartNumberName.setStatus("mandatory")


class _FruRevisionName_Type(DisplayString):
    """Custom type fruRevisionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FruRevisionName_Type.__name__ = "DisplayString"
_FruRevisionName_Object = MibTableColumn
fruRevisionName = _FruRevisionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 9),
    _FruRevisionName_Type()
)
fruRevisionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruRevisionName.setStatus("mandatory")
_FruManufacturingDateName_Type = DellDateName
_FruManufacturingDateName_Object = MibTableColumn
fruManufacturingDateName = _FruManufacturingDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 10),
    _FruManufacturingDateName_Type()
)
fruManufacturingDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruManufacturingDateName.setStatus("mandatory")


class _FruAssetTagName_Type(DisplayString):
    """Custom type fruAssetTagName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FruAssetTagName_Type.__name__ = "DisplayString"
_FruAssetTagName_Object = MibTableColumn
fruAssetTagName = _FruAssetTagName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 11),
    _FruAssetTagName_Type()
)
fruAssetTagName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruAssetTagName.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DCS3FRU-MIB",
    **{"DellObjectRange": DellObjectRange,
       "DellUnsigned8BitRange": DellUnsigned8BitRange,
       "DellUnsigned16BitRange": DellUnsigned16BitRange,
       "DellUnsigned32BitRange": DellUnsigned32BitRange,
       "DellDateName": DellDateName,
       "DellStatus": DellStatus,
       "DellFRUInformationState": DellFRUInformationState,
       "dell": dell,
       "server3": server3,
       "baseboardGroup": baseboardGroup,
       "fruGroup": fruGroup,
       "fruTable": fruTable,
       "fruTableEntry": fruTableEntry,
       "fruChassisIndex": fruChassisIndex,
       "fruIndex": fruIndex,
       "fruInformationStatus": fruInformationStatus,
       "fruInformationState": fruInformationState,
       "fruDeviceName": fruDeviceName,
       "fruManufacturerName": fruManufacturerName,
       "fruSerialNumberName": fruSerialNumberName,
       "fruPartNumberName": fruPartNumberName,
       "fruRevisionName": fruRevisionName,
       "fruManufacturingDateName": fruManufacturingDateName,
       "fruAssetTagName": fruAssetTagName}
)
