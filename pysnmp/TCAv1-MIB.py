# SNMP MIB module (TCAv1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TCAv1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:56 2024
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

_Bellcore_ObjectIdentity = ObjectIdentity
bellcore = _Bellcore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 148)
)
_Requirements_ObjectIdentity = ObjectIdentity
requirements = _Requirements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 148, 1)
)
_TcaMIB_ObjectIdentity = ObjectIdentity
tcaMIB = _TcaMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 148, 1, 5)
)
_TcaObjects_ObjectIdentity = ObjectIdentity
tcaObjects = _TcaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 148, 1, 5, 1)
)
_TcaTable_Object = MibTable
tcaTable = _TcaTable_Object(
    (1, 3, 6, 1, 4, 1, 148, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    tcaTable.setStatus("mandatory")
_TcaEntry_Object = MibTableRow
tcaEntry = _TcaEntry_Object(
    (1, 3, 6, 1, 4, 1, 148, 1, 5, 1, 1, 1)
)
tcaEntry.setIndexNames(
    (0, "TCAv1-MIB", "tcaIfIndex"),
    (0, "TCAv1-MIB", "tcaIndex"),
)
if mibBuilder.loadTexts:
    tcaEntry.setStatus("mandatory")


class _TcaIfIndex_Type(Integer32):
    """Custom type tcaIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TcaIfIndex_Type.__name__ = "Integer32"
_TcaIfIndex_Object = MibTableColumn
tcaIfIndex = _TcaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 148, 1, 5, 1, 1, 1, 1),
    _TcaIfIndex_Type()
)
tcaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcaIfIndex.setStatus("mandatory")


class _TcaIndex_Type(Integer32):
    """Custom type tcaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TcaIndex_Type.__name__ = "Integer32"
_TcaIndex_Object = MibTableColumn
tcaIndex = _TcaIndex_Object(
    (1, 3, 6, 1, 4, 1, 148, 1, 5, 1, 1, 1, 2),
    _TcaIndex_Type()
)
tcaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcaIndex.setStatus("mandatory")
_TcaObject_Type = ObjectIdentifier
_TcaObject_Object = MibTableColumn
tcaObject = _TcaObject_Object(
    (1, 3, 6, 1, 4, 1, 148, 1, 5, 1, 1, 1, 3),
    _TcaObject_Type()
)
tcaObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcaObject.setStatus("mandatory")


class _TcaObjectDesc_Type(DisplayString):
    """Custom type tcaObjectDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TcaObjectDesc_Type.__name__ = "DisplayString"
_TcaObjectDesc_Object = MibTableColumn
tcaObjectDesc = _TcaObjectDesc_Object(
    (1, 3, 6, 1, 4, 1, 148, 1, 5, 1, 1, 1, 4),
    _TcaObjectDesc_Type()
)
tcaObjectDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcaObjectDesc.setStatus("mandatory")


class _TcaThreshold_Type(Integer32):
    """Custom type tcaThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TcaThreshold_Type.__name__ = "Integer32"
_TcaThreshold_Object = MibTableColumn
tcaThreshold = _TcaThreshold_Object(
    (1, 3, 6, 1, 4, 1, 148, 1, 5, 1, 1, 1, 5),
    _TcaThreshold_Type()
)
tcaThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcaThreshold.setStatus("mandatory")


class _TcaSampleType_Type(Integer32):
    """Custom type tcaSampleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("intervalAbsoluteValue", 1),
          ("intervalDeltaValue", 2))
    )


_TcaSampleType_Type.__name__ = "Integer32"
_TcaSampleType_Object = MibTableColumn
tcaSampleType = _TcaSampleType_Object(
    (1, 3, 6, 1, 4, 1, 148, 1, 5, 1, 1, 1, 6),
    _TcaSampleType_Type()
)
tcaSampleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcaSampleType.setStatus("mandatory")
_TcaCounts_Type = Counter32
_TcaCounts_Object = MibTableColumn
tcaCounts = _TcaCounts_Object(
    (1, 3, 6, 1, 4, 1, 148, 1, 5, 1, 1, 1, 7),
    _TcaCounts_Type()
)
tcaCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcaCounts.setStatus("mandatory")
_TcaTimeStamp_Type = TimeTicks
_TcaTimeStamp_Object = MibTableColumn
tcaTimeStamp = _TcaTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 148, 1, 5, 1, 1, 1, 8),
    _TcaTimeStamp_Type()
)
tcaTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcaTimeStamp.setStatus("mandatory")


class _TcaTrapEnabler_Type(Integer32):
    """Custom type tcaTrapEnabler based on Integer32"""
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


_TcaTrapEnabler_Type.__name__ = "Integer32"
_TcaTrapEnabler_Object = MibTableColumn
tcaTrapEnabler = _TcaTrapEnabler_Object(
    (1, 3, 6, 1, 4, 1, 148, 1, 5, 1, 1, 1, 9),
    _TcaTrapEnabler_Type()
)
tcaTrapEnabler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcaTrapEnabler.setStatus("mandatory")
_TcaConformance_ObjectIdentity = ObjectIdentity
tcaConformance = _TcaConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 148, 1, 5, 2)
)
_TcaGroups_ObjectIdentity = ObjectIdentity
tcaGroups = _TcaGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 148, 1, 5, 2, 1)
)
_TcaGroup_ObjectIdentity = ObjectIdentity
tcaGroup = _TcaGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 148, 1, 5, 2, 1, 1)
)
_TcaCompliances_ObjectIdentity = ObjectIdentity
tcaCompliances = _TcaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 148, 1, 5, 2, 2)
)
_TcaCompliance_ObjectIdentity = ObjectIdentity
tcaCompliance = _TcaCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 148, 1, 5, 2, 2, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TCAv1-MIB",
    **{"bellcore": bellcore,
       "requirements": requirements,
       "tcaMIB": tcaMIB,
       "tcaObjects": tcaObjects,
       "tcaTable": tcaTable,
       "tcaEntry": tcaEntry,
       "tcaIfIndex": tcaIfIndex,
       "tcaIndex": tcaIndex,
       "tcaObject": tcaObject,
       "tcaObjectDesc": tcaObjectDesc,
       "tcaThreshold": tcaThreshold,
       "tcaSampleType": tcaSampleType,
       "tcaCounts": tcaCounts,
       "tcaTimeStamp": tcaTimeStamp,
       "tcaTrapEnabler": tcaTrapEnabler,
       "tcaConformance": tcaConformance,
       "tcaGroups": tcaGroups,
       "tcaGroup": tcaGroup,
       "tcaCompliances": tcaCompliances,
       "tcaCompliance": tcaCompliance}
)
