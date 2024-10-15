# SNMP MIB module (ELTEX-MES-IF-EXTENSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MES-IF-EXTENSION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:43 2024
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

(eltMesIfExtensionMIB,) = mibBuilder.importSymbols(
    "ELTEX-MES-MNG-MIB",
    "eltMesIfExtensionMIB")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesIfExtensionMIBObjects_ObjectIdentity = ObjectIdentity
eltMesIfExtensionMIBObjects = _EltMesIfExtensionMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1)
)
_EltMesIfExtDot1qCustomEtherType_ObjectIdentity = ObjectIdentity
eltMesIfExtDot1qCustomEtherType = _EltMesIfExtDot1qCustomEtherType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 3)
)
_EltIfDot1qCustomEgressEtherTypeTable_Object = MibTable
eltIfDot1qCustomEgressEtherTypeTable = _EltIfDot1qCustomEgressEtherTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 3, 1)
)
if mibBuilder.loadTexts:
    eltIfDot1qCustomEgressEtherTypeTable.setStatus("current")
_EltIfDot1qCustomEgressEtherTypeEntry_Object = MibTableRow
eltIfDot1qCustomEgressEtherTypeEntry = _EltIfDot1qCustomEgressEtherTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 3, 1, 1)
)
eltIfDot1qCustomEgressEtherTypeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltIfDot1qCustomEgressEtherTypeEntry.setStatus("current")


class _EltIfDot1qCustomEgressEtherType_Type(Integer32):
    """Custom type eltIfDot1qCustomEgressEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltIfDot1qCustomEgressEtherType_Type.__name__ = "Integer32"
_EltIfDot1qCustomEgressEtherType_Object = MibTableColumn
eltIfDot1qCustomEgressEtherType = _EltIfDot1qCustomEgressEtherType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 3, 1, 1, 1),
    _EltIfDot1qCustomEgressEtherType_Type()
)
eltIfDot1qCustomEgressEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIfDot1qCustomEgressEtherType.setStatus("current")
_EltIfDot1qCustomIngressEtherTypeTable_Object = MibTable
eltIfDot1qCustomIngressEtherTypeTable = _EltIfDot1qCustomIngressEtherTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 3, 2)
)
if mibBuilder.loadTexts:
    eltIfDot1qCustomIngressEtherTypeTable.setStatus("current")
_EltIfDot1qCustomIngressEtherTypeEntry_Object = MibTableRow
eltIfDot1qCustomIngressEtherTypeEntry = _EltIfDot1qCustomIngressEtherTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 3, 2, 1)
)
eltIfDot1qCustomIngressEtherTypeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltIfDot1qCustomIngressEtherTypeEntry.setStatus("current")


class _EltIfDot1qCustomIngressEtherType1_Type(Integer32):
    """Custom type eltIfDot1qCustomIngressEtherType1 based on Integer32"""
    defaultValue = 33024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(33024, 33024),
    )


_EltIfDot1qCustomIngressEtherType1_Type.__name__ = "Integer32"
_EltIfDot1qCustomIngressEtherType1_Object = MibTableColumn
eltIfDot1qCustomIngressEtherType1 = _EltIfDot1qCustomIngressEtherType1_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 3, 2, 1, 1),
    _EltIfDot1qCustomIngressEtherType1_Type()
)
eltIfDot1qCustomIngressEtherType1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIfDot1qCustomIngressEtherType1.setStatus("current")


class _EltIfDot1qCustomIngressEtherType2_Type(Integer32):
    """Custom type eltIfDot1qCustomIngressEtherType2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 33023),
        ValueRangeConstraint(33025, 65535),
    )


_EltIfDot1qCustomIngressEtherType2_Type.__name__ = "Integer32"
_EltIfDot1qCustomIngressEtherType2_Object = MibTableColumn
eltIfDot1qCustomIngressEtherType2 = _EltIfDot1qCustomIngressEtherType2_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 3, 2, 1, 2),
    _EltIfDot1qCustomIngressEtherType2_Type()
)
eltIfDot1qCustomIngressEtherType2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIfDot1qCustomIngressEtherType2.setStatus("current")


class _EltIfDot1qCustomIngressEtherType3_Type(Integer32):
    """Custom type eltIfDot1qCustomIngressEtherType3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 33023),
        ValueRangeConstraint(33025, 65535),
    )


_EltIfDot1qCustomIngressEtherType3_Type.__name__ = "Integer32"
_EltIfDot1qCustomIngressEtherType3_Object = MibTableColumn
eltIfDot1qCustomIngressEtherType3 = _EltIfDot1qCustomIngressEtherType3_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 3, 2, 1, 3),
    _EltIfDot1qCustomIngressEtherType3_Type()
)
eltIfDot1qCustomIngressEtherType3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIfDot1qCustomIngressEtherType3.setStatus("current")


class _EltIfDot1qCustomIngressEtherType4_Type(Integer32):
    """Custom type eltIfDot1qCustomIngressEtherType4 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 33023),
        ValueRangeConstraint(33025, 65535),
    )


_EltIfDot1qCustomIngressEtherType4_Type.__name__ = "Integer32"
_EltIfDot1qCustomIngressEtherType4_Object = MibTableColumn
eltIfDot1qCustomIngressEtherType4 = _EltIfDot1qCustomIngressEtherType4_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 3, 2, 1, 4),
    _EltIfDot1qCustomIngressEtherType4_Type()
)
eltIfDot1qCustomIngressEtherType4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIfDot1qCustomIngressEtherType4.setStatus("current")


class _EltIfDot1qCustomIngressEtherType5_Type(Integer32):
    """Custom type eltIfDot1qCustomIngressEtherType5 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 33023),
        ValueRangeConstraint(33025, 65535),
    )


_EltIfDot1qCustomIngressEtherType5_Type.__name__ = "Integer32"
_EltIfDot1qCustomIngressEtherType5_Object = MibTableColumn
eltIfDot1qCustomIngressEtherType5 = _EltIfDot1qCustomIngressEtherType5_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 3, 2, 1, 5),
    _EltIfDot1qCustomIngressEtherType5_Type()
)
eltIfDot1qCustomIngressEtherType5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIfDot1qCustomIngressEtherType5.setStatus("current")


class _EltIfDot1qCustomIngressEtherType6_Type(Integer32):
    """Custom type eltIfDot1qCustomIngressEtherType6 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 33023),
        ValueRangeConstraint(33025, 65535),
    )


_EltIfDot1qCustomIngressEtherType6_Type.__name__ = "Integer32"
_EltIfDot1qCustomIngressEtherType6_Object = MibTableColumn
eltIfDot1qCustomIngressEtherType6 = _EltIfDot1qCustomIngressEtherType6_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 3, 2, 1, 6),
    _EltIfDot1qCustomIngressEtherType6_Type()
)
eltIfDot1qCustomIngressEtherType6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIfDot1qCustomIngressEtherType6.setStatus("current")


class _EltIfDot1qCustomIngressEtherType7_Type(Integer32):
    """Custom type eltIfDot1qCustomIngressEtherType7 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 33023),
        ValueRangeConstraint(33025, 65535),
    )


_EltIfDot1qCustomIngressEtherType7_Type.__name__ = "Integer32"
_EltIfDot1qCustomIngressEtherType7_Object = MibTableColumn
eltIfDot1qCustomIngressEtherType7 = _EltIfDot1qCustomIngressEtherType7_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 3, 2, 1, 7),
    _EltIfDot1qCustomIngressEtherType7_Type()
)
eltIfDot1qCustomIngressEtherType7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIfDot1qCustomIngressEtherType7.setStatus("current")
_EltMesIfExtDot1q_ObjectIdentity = ObjectIdentity
eltMesIfExtDot1q = _EltMesIfExtDot1q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 4)
)
_EltIfDot1qIngressCvlanTable_Object = MibTable
eltIfDot1qIngressCvlanTable = _EltIfDot1qIngressCvlanTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 4, 1)
)
if mibBuilder.loadTexts:
    eltIfDot1qIngressCvlanTable.setStatus("current")
_EltIfDot1qIngressCvlanEntry_Object = MibTableRow
eltIfDot1qIngressCvlanEntry = _EltIfDot1qIngressCvlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 4, 1, 1)
)
eltIfDot1qIngressCvlanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltIfDot1qIngressCvlanEntry.setStatus("current")


class _EltIfDot1qIngressCvlanTag_Type(Integer32):
    """Custom type eltIfDot1qIngressCvlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_EltIfDot1qIngressCvlanTag_Type.__name__ = "Integer32"
_EltIfDot1qIngressCvlanTag_Object = MibTableColumn
eltIfDot1qIngressCvlanTag = _EltIfDot1qIngressCvlanTag_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276, 1, 4, 1, 1, 1),
    _EltIfDot1qIngressCvlanTag_Type()
)
eltIfDot1qIngressCvlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIfDot1qIngressCvlanTag.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-IF-EXTENSION-MIB",
    **{"eltMesIfExtensionMIBObjects": eltMesIfExtensionMIBObjects,
       "eltMesIfExtDot1qCustomEtherType": eltMesIfExtDot1qCustomEtherType,
       "eltIfDot1qCustomEgressEtherTypeTable": eltIfDot1qCustomEgressEtherTypeTable,
       "eltIfDot1qCustomEgressEtherTypeEntry": eltIfDot1qCustomEgressEtherTypeEntry,
       "eltIfDot1qCustomEgressEtherType": eltIfDot1qCustomEgressEtherType,
       "eltIfDot1qCustomIngressEtherTypeTable": eltIfDot1qCustomIngressEtherTypeTable,
       "eltIfDot1qCustomIngressEtherTypeEntry": eltIfDot1qCustomIngressEtherTypeEntry,
       "eltIfDot1qCustomIngressEtherType1": eltIfDot1qCustomIngressEtherType1,
       "eltIfDot1qCustomIngressEtherType2": eltIfDot1qCustomIngressEtherType2,
       "eltIfDot1qCustomIngressEtherType3": eltIfDot1qCustomIngressEtherType3,
       "eltIfDot1qCustomIngressEtherType4": eltIfDot1qCustomIngressEtherType4,
       "eltIfDot1qCustomIngressEtherType5": eltIfDot1qCustomIngressEtherType5,
       "eltIfDot1qCustomIngressEtherType6": eltIfDot1qCustomIngressEtherType6,
       "eltIfDot1qCustomIngressEtherType7": eltIfDot1qCustomIngressEtherType7,
       "eltMesIfExtDot1q": eltMesIfExtDot1q,
       "eltIfDot1qIngressCvlanTable": eltIfDot1qIngressCvlanTable,
       "eltIfDot1qIngressCvlanEntry": eltIfDot1qIngressCvlanEntry,
       "eltIfDot1qIngressCvlanTag": eltIfDot1qIngressCvlanTag}
)
