# SNMP MIB module (TERAWAVE-teraIpClassification-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TERAWAVE-teraIpClassification-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:17 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Terawave_ObjectIdentity = ObjectIdentity
terawave = _Terawave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513)
)
_TeraIpClassificationGroup_ObjectIdentity = ObjectIdentity
teraIpClassificationGroup = _TeraIpClassificationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 23)
)
_TeraIpClassTable_Object = MibTable
teraIpClassTable = _TeraIpClassTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 23, 1)
)
if mibBuilder.loadTexts:
    teraIpClassTable.setStatus("mandatory")
_TeraIpClassTableEntry_Object = MibTableRow
teraIpClassTableEntry = _TeraIpClassTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 23, 1, 1)
)
teraIpClassTableEntry.setIndexNames(
    (0, "TERAWAVE-teraIpClassification-MIB", "teraIpClassField"),
)
if mibBuilder.loadTexts:
    teraIpClassTableEntry.setStatus("mandatory")
_TeraIpClassField_Type = Integer32
_TeraIpClassField_Object = MibTableColumn
teraIpClassField = _TeraIpClassField_Object(
    (1, 3, 6, 1, 4, 1, 4513, 23, 1, 1, 1),
    _TeraIpClassField_Type()
)
teraIpClassField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraIpClassField.setStatus("mandatory")
_TeraIpClassType_Type = Integer32
_TeraIpClassType_Object = MibTableColumn
teraIpClassType = _TeraIpClassType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 23, 1, 1, 2),
    _TeraIpClassType_Type()
)
teraIpClassType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraIpClassType.setStatus("mandatory")
_TeraIpClassValue_Type = Integer32
_TeraIpClassValue_Object = MibTableColumn
teraIpClassValue = _TeraIpClassValue_Object(
    (1, 3, 6, 1, 4, 1, 4513, 23, 1, 1, 3),
    _TeraIpClassValue_Type()
)
teraIpClassValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraIpClassValue.setStatus("mandatory")
_TeraIpClassMinRange_Type = Integer32
_TeraIpClassMinRange_Object = MibTableColumn
teraIpClassMinRange = _TeraIpClassMinRange_Object(
    (1, 3, 6, 1, 4, 1, 4513, 23, 1, 1, 4),
    _TeraIpClassMinRange_Type()
)
teraIpClassMinRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraIpClassMinRange.setStatus("mandatory")
_TeraIpClassMaxRange_Type = Integer32
_TeraIpClassMaxRange_Object = MibTableColumn
teraIpClassMaxRange = _TeraIpClassMaxRange_Object(
    (1, 3, 6, 1, 4, 1, 4513, 23, 1, 1, 5),
    _TeraIpClassMaxRange_Type()
)
teraIpClassMaxRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraIpClassMaxRange.setStatus("mandatory")
_TeraIpClassIpAddr_Type = IpAddress
_TeraIpClassIpAddr_Object = MibTableColumn
teraIpClassIpAddr = _TeraIpClassIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4513, 23, 1, 1, 6),
    _TeraIpClassIpAddr_Type()
)
teraIpClassIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraIpClassIpAddr.setStatus("mandatory")
_TeraIpClassMask_Type = IpAddress
_TeraIpClassMask_Object = MibTableColumn
teraIpClassMask = _TeraIpClassMask_Object(
    (1, 3, 6, 1, 4, 1, 4513, 23, 1, 1, 7),
    _TeraIpClassMask_Type()
)
teraIpClassMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraIpClassMask.setStatus("mandatory")
_TeraIpClassificationTable_Object = MibTable
teraIpClassificationTable = _TeraIpClassificationTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 23, 2)
)
if mibBuilder.loadTexts:
    teraIpClassificationTable.setStatus("mandatory")
_TeraIpClassificationTableEntry_Object = MibTableRow
teraIpClassificationTableEntry = _TeraIpClassificationTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 23, 2, 1)
)
teraIpClassificationTableEntry.setIndexNames(
    (0, "TERAWAVE-teraIpClassification-MIB", "teraClassificationRule"),
    (0, "TERAWAVE-teraIpClassification-MIB", "teraIpClassField"),
)
if mibBuilder.loadTexts:
    teraIpClassificationTableEntry.setStatus("mandatory")
_TeraClassificationRule_Type = Integer32
_TeraClassificationRule_Object = MibTableColumn
teraClassificationRule = _TeraClassificationRule_Object(
    (1, 3, 6, 1, 4, 1, 4513, 23, 2, 1, 1),
    _TeraClassificationRule_Type()
)
teraClassificationRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraClassificationRule.setStatus("mandatory")
_TeraIpClassificationField_Type = Integer32
_TeraIpClassificationField_Object = MibTableColumn
teraIpClassificationField = _TeraIpClassificationField_Object(
    (1, 3, 6, 1, 4, 1, 4513, 23, 2, 1, 2),
    _TeraIpClassificationField_Type()
)
teraIpClassificationField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraIpClassificationField.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERAWAVE-teraIpClassification-MIB",
    **{"terawave": terawave,
       "teraIpClassificationGroup": teraIpClassificationGroup,
       "teraIpClassTable": teraIpClassTable,
       "teraIpClassTableEntry": teraIpClassTableEntry,
       "teraIpClassField": teraIpClassField,
       "teraIpClassType": teraIpClassType,
       "teraIpClassValue": teraIpClassValue,
       "teraIpClassMinRange": teraIpClassMinRange,
       "teraIpClassMaxRange": teraIpClassMaxRange,
       "teraIpClassIpAddr": teraIpClassIpAddr,
       "teraIpClassMask": teraIpClassMask,
       "teraIpClassificationTable": teraIpClassificationTable,
       "teraIpClassificationTableEntry": teraIpClassificationTableEntry,
       "teraClassificationRule": teraClassificationRule,
       "teraIpClassificationField": teraIpClassificationField}
)
