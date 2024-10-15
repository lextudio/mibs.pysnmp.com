# SNMP MIB module (XYLAN-FLT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-FLT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:01 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress")

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

(xylanFltArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanFltArch")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XylanFltStatus_ObjectIdentity = ObjectIdentity
xylanFltStatus = _XylanFltStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 1)
)


class _XylanFltActiveAdminState_Type(Integer32):
    """Custom type xylanFltActiveAdminState based on Integer32"""
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


_XylanFltActiveAdminState_Type.__name__ = "Integer32"
_XylanFltActiveAdminState_Object = MibScalar
xylanFltActiveAdminState = _XylanFltActiveAdminState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 1, 1),
    _XylanFltActiveAdminState_Type()
)
xylanFltActiveAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltActiveAdminState.setStatus("mandatory")


class _XylanFltActiveOperState_Type(Integer32):
    """Custom type xylanFltActiveOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("deactivating", 2),
          ("inactive", 3),
          ("initializing", 0))
    )


_XylanFltActiveOperState_Type.__name__ = "Integer32"
_XylanFltActiveOperState_Object = MibScalar
xylanFltActiveOperState = _XylanFltActiveOperState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 1, 2),
    _XylanFltActiveOperState_Type()
)
xylanFltActiveOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltActiveOperState.setStatus("mandatory")


class _XylanFltConfigAdminState_Type(Integer32):
    """Custom type xylanFltConfigAdminState based on Integer32"""
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


_XylanFltConfigAdminState_Type.__name__ = "Integer32"
_XylanFltConfigAdminState_Object = MibScalar
xylanFltConfigAdminState = _XylanFltConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 1, 3),
    _XylanFltConfigAdminState_Type()
)
xylanFltConfigAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanFltConfigAdminState.setStatus("mandatory")
_XylanFltCommit_Type = Integer32
_XylanFltCommit_Object = MibScalar
xylanFltCommit = _XylanFltCommit_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 1, 4),
    _XylanFltCommit_Type()
)
xylanFltCommit.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    xylanFltCommit.setStatus("mandatory")
_XylanFltStaticConfig_ObjectIdentity = ObjectIdentity
xylanFltStaticConfig = _XylanFltStaticConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2)
)
_XylanFltGroups_ObjectIdentity = ObjectIdentity
xylanFltGroups = _XylanFltGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 1)
)
_XylanFltGroupTable_Object = MibTable
xylanFltGroupTable = _XylanFltGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xylanFltGroupTable.setStatus("mandatory")
_XylanFltGroupEntry_Object = MibTableRow
xylanFltGroupEntry = _XylanFltGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 1, 1, 1)
)
xylanFltGroupEntry.setIndexNames(
    (0, "XYLAN-FLT-MIB", "xylanFltGroupIndex"),
)
if mibBuilder.loadTexts:
    xylanFltGroupEntry.setStatus("mandatory")


class _XylanFltGroupIndex_Type(OctetString):
    """Custom type xylanFltGroupIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(30, 30),
    )


_XylanFltGroupIndex_Type.__name__ = "OctetString"
_XylanFltGroupIndex_Object = MibTableColumn
xylanFltGroupIndex = _XylanFltGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 1, 1, 1, 1),
    _XylanFltGroupIndex_Type()
)
xylanFltGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltGroupIndex.setStatus("mandatory")


class _XylanFltGroupAdminState_Type(Integer32):
    """Custom type xylanFltGroupAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("delete", 2))
    )


_XylanFltGroupAdminState_Type.__name__ = "Integer32"
_XylanFltGroupAdminState_Object = MibTableColumn
xylanFltGroupAdminState = _XylanFltGroupAdminState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 1, 1, 1, 2),
    _XylanFltGroupAdminState_Type()
)
xylanFltGroupAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanFltGroupAdminState.setStatus("mandatory")


class _XylanFltGroupProtocol_Type(Integer32):
    """Custom type xylanFltGroupProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("ipx", 2),
          ("na", 0))
    )


_XylanFltGroupProtocol_Type.__name__ = "Integer32"
_XylanFltGroupProtocol_Object = MibTableColumn
xylanFltGroupProtocol = _XylanFltGroupProtocol_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 1, 1, 1, 3),
    _XylanFltGroupProtocol_Type()
)
xylanFltGroupProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanFltGroupProtocol.setStatus("mandatory")


class _XylanFltGroupAdrType_Type(Integer32):
    """Custom type xylanFltGroupAdrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destination", 1),
          ("na", 0),
          ("source", 2))
    )


_XylanFltGroupAdrType_Type.__name__ = "Integer32"
_XylanFltGroupAdrType_Object = MibTableColumn
xylanFltGroupAdrType = _XylanFltGroupAdrType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 1, 1, 1, 4),
    _XylanFltGroupAdrType_Type()
)
xylanFltGroupAdrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanFltGroupAdrType.setStatus("mandatory")
_XylanFltRuleListTable_Object = MibTable
xylanFltRuleListTable = _XylanFltRuleListTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 1, 2)
)
if mibBuilder.loadTexts:
    xylanFltRuleListTable.setStatus("mandatory")
_XylanFltRuleListEntry_Object = MibTableRow
xylanFltRuleListEntry = _XylanFltRuleListEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 1, 2, 1)
)
xylanFltRuleListEntry.setIndexNames(
    (0, "XYLAN-FLT-MIB", "xylanFltGroupIndex"),
    (0, "XYLAN-FLT-MIB", "xylanFltRuleListIndex"),
)
if mibBuilder.loadTexts:
    xylanFltRuleListEntry.setStatus("mandatory")


class _XylanFltRuleListIndex_Type(OctetString):
    """Custom type xylanFltRuleListIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(47, 47),
    )


_XylanFltRuleListIndex_Type.__name__ = "OctetString"
_XylanFltRuleListIndex_Object = MibTableColumn
xylanFltRuleListIndex = _XylanFltRuleListIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 1, 2, 1, 1),
    _XylanFltRuleListIndex_Type()
)
xylanFltRuleListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltRuleListIndex.setStatus("mandatory")


class _XylanFltRuleListAdminState_Type(Integer32):
    """Custom type xylanFltRuleListAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("delete", 2))
    )


_XylanFltRuleListAdminState_Type.__name__ = "Integer32"
_XylanFltRuleListAdminState_Object = MibTableColumn
xylanFltRuleListAdminState = _XylanFltRuleListAdminState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 1, 2, 1, 2),
    _XylanFltRuleListAdminState_Type()
)
xylanFltRuleListAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanFltRuleListAdminState.setStatus("mandatory")


class _XylanFltRuleListRule_Type(Integer32):
    """Custom type xylanFltRuleListRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_XylanFltRuleListRule_Type.__name__ = "Integer32"
_XylanFltRuleListRule_Object = MibTableColumn
xylanFltRuleListRule = _XylanFltRuleListRule_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 1, 2, 1, 3),
    _XylanFltRuleListRule_Type()
)
xylanFltRuleListRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanFltRuleListRule.setStatus("mandatory")
_XylanFltServices_ObjectIdentity = ObjectIdentity
xylanFltServices = _XylanFltServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 2)
)
_XylanFltServiceTable_Object = MibTable
xylanFltServiceTable = _XylanFltServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 2, 1)
)
if mibBuilder.loadTexts:
    xylanFltServiceTable.setStatus("mandatory")
_XylanFltServiceEntry_Object = MibTableRow
xylanFltServiceEntry = _XylanFltServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 2, 1, 1)
)
xylanFltServiceEntry.setIndexNames(
    (0, "XYLAN-FLT-MIB", "xylanFltServiceIndex"),
)
if mibBuilder.loadTexts:
    xylanFltServiceEntry.setStatus("mandatory")


class _XylanFltServiceIndex_Type(OctetString):
    """Custom type xylanFltServiceIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_XylanFltServiceIndex_Type.__name__ = "OctetString"
_XylanFltServiceIndex_Object = MibTableColumn
xylanFltServiceIndex = _XylanFltServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 2, 1, 1, 1),
    _XylanFltServiceIndex_Type()
)
xylanFltServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltServiceIndex.setStatus("mandatory")


class _XylanFltServiceAdminState_Type(Integer32):
    """Custom type xylanFltServiceAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("delete", 2))
    )


_XylanFltServiceAdminState_Type.__name__ = "Integer32"
_XylanFltServiceAdminState_Object = MibTableColumn
xylanFltServiceAdminState = _XylanFltServiceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 2, 1, 1, 2),
    _XylanFltServiceAdminState_Type()
)
xylanFltServiceAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanFltServiceAdminState.setStatus("mandatory")
_XylanFltServiceNumberTable_Object = MibTable
xylanFltServiceNumberTable = _XylanFltServiceNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 2, 2)
)
if mibBuilder.loadTexts:
    xylanFltServiceNumberTable.setStatus("mandatory")
_XylanFltServiceNumberEntry_Object = MibTableRow
xylanFltServiceNumberEntry = _XylanFltServiceNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 2, 2, 1)
)
xylanFltServiceNumberEntry.setIndexNames(
    (0, "XYLAN-FLT-MIB", "xylanFltServiceIndex"),
    (0, "XYLAN-FLT-MIB", "xylanFltServiceNumberIndex"),
)
if mibBuilder.loadTexts:
    xylanFltServiceNumberEntry.setStatus("mandatory")


class _XylanFltServiceNumberIndex_Type(OctetString):
    """Custom type xylanFltServiceNumberIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )


_XylanFltServiceNumberIndex_Type.__name__ = "OctetString"
_XylanFltServiceNumberIndex_Object = MibTableColumn
xylanFltServiceNumberIndex = _XylanFltServiceNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 2, 2, 1, 1),
    _XylanFltServiceNumberIndex_Type()
)
xylanFltServiceNumberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltServiceNumberIndex.setStatus("mandatory")


class _XylanFltServiceNumberAdminState_Type(Integer32):
    """Custom type xylanFltServiceNumberAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("delete", 2))
    )


_XylanFltServiceNumberAdminState_Type.__name__ = "Integer32"
_XylanFltServiceNumberAdminState_Object = MibTableColumn
xylanFltServiceNumberAdminState = _XylanFltServiceNumberAdminState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 2, 2, 1, 2),
    _XylanFltServiceNumberAdminState_Type()
)
xylanFltServiceNumberAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanFltServiceNumberAdminState.setStatus("mandatory")
_XylanFltServiceGroupTable_Object = MibTable
xylanFltServiceGroupTable = _XylanFltServiceGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 2, 3)
)
if mibBuilder.loadTexts:
    xylanFltServiceGroupTable.setStatus("mandatory")
_XylanFltServiceGroupEntry_Object = MibTableRow
xylanFltServiceGroupEntry = _XylanFltServiceGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 2, 3, 1)
)
xylanFltServiceGroupEntry.setIndexNames(
    (0, "XYLAN-FLT-MIB", "xylanFltServiceIndex"),
    (0, "XYLAN-FLT-MIB", "xylanFltServiceGroupIndex"),
)
if mibBuilder.loadTexts:
    xylanFltServiceGroupEntry.setStatus("mandatory")


class _XylanFltServiceGroupIndex_Type(OctetString):
    """Custom type xylanFltServiceGroupIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(44, 44),
    )


_XylanFltServiceGroupIndex_Type.__name__ = "OctetString"
_XylanFltServiceGroupIndex_Object = MibTableColumn
xylanFltServiceGroupIndex = _XylanFltServiceGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 2, 3, 1, 1),
    _XylanFltServiceGroupIndex_Type()
)
xylanFltServiceGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltServiceGroupIndex.setStatus("mandatory")


class _XylanFltServiceGroupAdminState_Type(Integer32):
    """Custom type xylanFltServiceGroupAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("delete", 2))
    )


_XylanFltServiceGroupAdminState_Type.__name__ = "Integer32"
_XylanFltServiceGroupAdminState_Object = MibTableColumn
xylanFltServiceGroupAdminState = _XylanFltServiceGroupAdminState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 2, 3, 1, 2),
    _XylanFltServiceGroupAdminState_Type()
)
xylanFltServiceGroupAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanFltServiceGroupAdminState.setStatus("mandatory")
_XylanFltGlobals_ObjectIdentity = ObjectIdentity
xylanFltGlobals = _XylanFltGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 3)
)


class _XylanFltGlobalIPRule_Type(Integer32):
    """Custom type xylanFltGlobalIPRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_XylanFltGlobalIPRule_Type.__name__ = "Integer32"
_XylanFltGlobalIPRule_Object = MibScalar
xylanFltGlobalIPRule = _XylanFltGlobalIPRule_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 3, 1),
    _XylanFltGlobalIPRule_Type()
)
xylanFltGlobalIPRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanFltGlobalIPRule.setStatus("mandatory")


class _XylanFltGlobalIPXRule_Type(Integer32):
    """Custom type xylanFltGlobalIPXRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_XylanFltGlobalIPXRule_Type.__name__ = "Integer32"
_XylanFltGlobalIPXRule_Object = MibScalar
xylanFltGlobalIPXRule = _XylanFltGlobalIPXRule_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 3, 2),
    _XylanFltGlobalIPXRule_Type()
)
xylanFltGlobalIPXRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanFltGlobalIPXRule.setStatus("mandatory")


class _XylanFltGlobalPrecedence_Type(Integer32):
    """Custom type xylanFltGlobalPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destination", 1),
          ("source", 2))
    )


_XylanFltGlobalPrecedence_Type.__name__ = "Integer32"
_XylanFltGlobalPrecedence_Object = MibScalar
xylanFltGlobalPrecedence = _XylanFltGlobalPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 3, 3),
    _XylanFltGlobalPrecedence_Type()
)
xylanFltGlobalPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanFltGlobalPrecedence.setStatus("mandatory")
_XylanFltGlobalGroupTable_Object = MibTable
xylanFltGlobalGroupTable = _XylanFltGlobalGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 3, 4)
)
if mibBuilder.loadTexts:
    xylanFltGlobalGroupTable.setStatus("mandatory")
_XylanFltGlobalGroupEntry_Object = MibTableRow
xylanFltGlobalGroupEntry = _XylanFltGlobalGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 3, 4, 1)
)
xylanFltGlobalGroupEntry.setIndexNames(
    (0, "XYLAN-FLT-MIB", "xylanFltGlobalGroupIndex"),
)
if mibBuilder.loadTexts:
    xylanFltGlobalGroupEntry.setStatus("mandatory")


class _XylanFltGlobalGroupIndex_Type(OctetString):
    """Custom type xylanFltGlobalGroupIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(44, 44),
    )


_XylanFltGlobalGroupIndex_Type.__name__ = "OctetString"
_XylanFltGlobalGroupIndex_Object = MibTableColumn
xylanFltGlobalGroupIndex = _XylanFltGlobalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 3, 4, 1, 1),
    _XylanFltGlobalGroupIndex_Type()
)
xylanFltGlobalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltGlobalGroupIndex.setStatus("mandatory")


class _XylanFltGlobalGroupAdminState_Type(Integer32):
    """Custom type xylanFltGlobalGroupAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("delete", 2))
    )


_XylanFltGlobalGroupAdminState_Type.__name__ = "Integer32"
_XylanFltGlobalGroupAdminState_Object = MibTableColumn
xylanFltGlobalGroupAdminState = _XylanFltGlobalGroupAdminState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 3, 4, 1, 2),
    _XylanFltGlobalGroupAdminState_Type()
)
xylanFltGlobalGroupAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanFltGlobalGroupAdminState.setStatus("mandatory")
_XylanFltGlobalServiceTable_Object = MibTable
xylanFltGlobalServiceTable = _XylanFltGlobalServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 3, 5)
)
if mibBuilder.loadTexts:
    xylanFltGlobalServiceTable.setStatus("mandatory")
_XylanFltGlobalServiceEntry_Object = MibTableRow
xylanFltGlobalServiceEntry = _XylanFltGlobalServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 3, 5, 1)
)
xylanFltGlobalServiceEntry.setIndexNames(
    (0, "XYLAN-FLT-MIB", "xylanFltGlobalServiceIndex"),
)
if mibBuilder.loadTexts:
    xylanFltGlobalServiceEntry.setStatus("mandatory")


class _XylanFltGlobalServiceIndex_Type(OctetString):
    """Custom type xylanFltGlobalServiceIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(44, 44),
    )


_XylanFltGlobalServiceIndex_Type.__name__ = "OctetString"
_XylanFltGlobalServiceIndex_Object = MibTableColumn
xylanFltGlobalServiceIndex = _XylanFltGlobalServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 3, 5, 1, 1),
    _XylanFltGlobalServiceIndex_Type()
)
xylanFltGlobalServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltGlobalServiceIndex.setStatus("mandatory")


class _XylanFltGlobalServiceAdminState_Type(Integer32):
    """Custom type xylanFltGlobalServiceAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("delete", 2))
    )


_XylanFltGlobalServiceAdminState_Type.__name__ = "Integer32"
_XylanFltGlobalServiceAdminState_Object = MibTableColumn
xylanFltGlobalServiceAdminState = _XylanFltGlobalServiceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 2, 3, 5, 1, 2),
    _XylanFltGlobalServiceAdminState_Type()
)
xylanFltGlobalServiceAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanFltGlobalServiceAdminState.setStatus("mandatory")
_XylanFltActiveConfig_ObjectIdentity = ObjectIdentity
xylanFltActiveConfig = _XylanFltActiveConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3)
)
_XylanFltIpServicePortTbl_Object = MibTable
xylanFltIpServicePortTbl = _XylanFltIpServicePortTbl_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 1)
)
if mibBuilder.loadTexts:
    xylanFltIpServicePortTbl.setStatus("mandatory")
_XylanFltIpServicePortTblEntry_Object = MibTableRow
xylanFltIpServicePortTblEntry = _XylanFltIpServicePortTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 1, 1)
)
xylanFltIpServicePortTblEntry.setIndexNames(
    (0, "XYLAN-FLT-MIB", "xylanFltIpServicePortName"),
    (0, "XYLAN-FLT-MIB", "xylanFltIpServicePortNumber"),
)
if mibBuilder.loadTexts:
    xylanFltIpServicePortTblEntry.setStatus("mandatory")


class _XylanFltIpServicePortName_Type(DisplayString):
    """Custom type xylanFltIpServicePortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_XylanFltIpServicePortName_Type.__name__ = "DisplayString"
_XylanFltIpServicePortName_Object = MibTableColumn
xylanFltIpServicePortName = _XylanFltIpServicePortName_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 1, 1, 1),
    _XylanFltIpServicePortName_Type()
)
xylanFltIpServicePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltIpServicePortName.setStatus("mandatory")
_XylanFltIpServicePortNumber_Type = Integer32
_XylanFltIpServicePortNumber_Object = MibTableColumn
xylanFltIpServicePortNumber = _XylanFltIpServicePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 1, 1, 2),
    _XylanFltIpServicePortNumber_Type()
)
xylanFltIpServicePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltIpServicePortNumber.setStatus("mandatory")
_XylanFltIpServiceRuleTbl_Object = MibTable
xylanFltIpServiceRuleTbl = _XylanFltIpServiceRuleTbl_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 2)
)
if mibBuilder.loadTexts:
    xylanFltIpServiceRuleTbl.setStatus("mandatory")
_XylanFltIpServiceRuleTblEntry_Object = MibTableRow
xylanFltIpServiceRuleTblEntry = _XylanFltIpServiceRuleTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 2, 1)
)
xylanFltIpServiceRuleTblEntry.setIndexNames(
    (0, "XYLAN-FLT-MIB", "xylanFltIpServiceRuleName"),
    (0, "XYLAN-FLT-MIB", "xylanFltIpServiceRuleID"),
)
if mibBuilder.loadTexts:
    xylanFltIpServiceRuleTblEntry.setStatus("mandatory")


class _XylanFltIpServiceRuleName_Type(DisplayString):
    """Custom type xylanFltIpServiceRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_XylanFltIpServiceRuleName_Type.__name__ = "DisplayString"
_XylanFltIpServiceRuleName_Object = MibTableColumn
xylanFltIpServiceRuleName = _XylanFltIpServiceRuleName_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 2, 1, 1),
    _XylanFltIpServiceRuleName_Type()
)
xylanFltIpServiceRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltIpServiceRuleName.setStatus("mandatory")
_XylanFltIpServiceRuleID_Type = Integer32
_XylanFltIpServiceRuleID_Object = MibTableColumn
xylanFltIpServiceRuleID = _XylanFltIpServiceRuleID_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 2, 1, 2),
    _XylanFltIpServiceRuleID_Type()
)
xylanFltIpServiceRuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltIpServiceRuleID.setStatus("mandatory")
_XylanFltIpServiceRuleDest_Type = IpAddress
_XylanFltIpServiceRuleDest_Object = MibTableColumn
xylanFltIpServiceRuleDest = _XylanFltIpServiceRuleDest_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 2, 1, 3),
    _XylanFltIpServiceRuleDest_Type()
)
xylanFltIpServiceRuleDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltIpServiceRuleDest.setStatus("mandatory")


class _XylanFltIpServiceRuleDestMask_Type(OctetString):
    """Custom type xylanFltIpServiceRuleDestMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_XylanFltIpServiceRuleDestMask_Type.__name__ = "OctetString"
_XylanFltIpServiceRuleDestMask_Object = MibTableColumn
xylanFltIpServiceRuleDestMask = _XylanFltIpServiceRuleDestMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 2, 1, 4),
    _XylanFltIpServiceRuleDestMask_Type()
)
xylanFltIpServiceRuleDestMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltIpServiceRuleDestMask.setStatus("mandatory")
_XylanFltIpServiceRuleSrc_Type = IpAddress
_XylanFltIpServiceRuleSrc_Object = MibTableColumn
xylanFltIpServiceRuleSrc = _XylanFltIpServiceRuleSrc_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 2, 1, 5),
    _XylanFltIpServiceRuleSrc_Type()
)
xylanFltIpServiceRuleSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltIpServiceRuleSrc.setStatus("mandatory")


class _XylanFltIpServiceRuleSrcMask_Type(OctetString):
    """Custom type xylanFltIpServiceRuleSrcMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_XylanFltIpServiceRuleSrcMask_Type.__name__ = "OctetString"
_XylanFltIpServiceRuleSrcMask_Object = MibTableColumn
xylanFltIpServiceRuleSrcMask = _XylanFltIpServiceRuleSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 2, 1, 6),
    _XylanFltIpServiceRuleSrcMask_Type()
)
xylanFltIpServiceRuleSrcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltIpServiceRuleSrcMask.setStatus("mandatory")


class _XylanFltIpServiceRuleDisp_Type(Integer32):
    """Custom type xylanFltIpServiceRuleDisp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_XylanFltIpServiceRuleDisp_Type.__name__ = "Integer32"
_XylanFltIpServiceRuleDisp_Object = MibTableColumn
xylanFltIpServiceRuleDisp = _XylanFltIpServiceRuleDisp_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 2, 1, 7),
    _XylanFltIpServiceRuleDisp_Type()
)
xylanFltIpServiceRuleDisp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltIpServiceRuleDisp.setStatus("mandatory")
_XylanFltIpServiceRuleCount_Type = Integer32
_XylanFltIpServiceRuleCount_Object = MibTableColumn
xylanFltIpServiceRuleCount = _XylanFltIpServiceRuleCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 2, 1, 8),
    _XylanFltIpServiceRuleCount_Type()
)
xylanFltIpServiceRuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltIpServiceRuleCount.setStatus("mandatory")


class _XylanFltIpServiceRuleGroup_Type(DisplayString):
    """Custom type xylanFltIpServiceRuleGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_XylanFltIpServiceRuleGroup_Type.__name__ = "DisplayString"
_XylanFltIpServiceRuleGroup_Object = MibTableColumn
xylanFltIpServiceRuleGroup = _XylanFltIpServiceRuleGroup_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 2, 1, 9),
    _XylanFltIpServiceRuleGroup_Type()
)
xylanFltIpServiceRuleGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltIpServiceRuleGroup.setStatus("mandatory")
_XylanFltIpxRuleTbl_Object = MibTable
xylanFltIpxRuleTbl = _XylanFltIpxRuleTbl_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 3)
)
if mibBuilder.loadTexts:
    xylanFltIpxRuleTbl.setStatus("mandatory")
_XylanFltIpxRuleTblEntry_Object = MibTableRow
xylanFltIpxRuleTblEntry = _XylanFltIpxRuleTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 3, 1)
)
xylanFltIpxRuleTblEntry.setIndexNames(
    (0, "XYLAN-FLT-MIB", "xylanFltIpxRuleType"),
    (0, "XYLAN-FLT-MIB", "xylanFltIpxRuleID"),
)
if mibBuilder.loadTexts:
    xylanFltIpxRuleTblEntry.setStatus("mandatory")


class _XylanFltIpxRuleType_Type(Integer32):
    """Custom type xylanFltIpxRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("full-address", 1),
          ("global", 4),
          ("invalid", 0),
          ("network", 3),
          ("node", 2))
    )


_XylanFltIpxRuleType_Type.__name__ = "Integer32"
_XylanFltIpxRuleType_Object = MibTableColumn
xylanFltIpxRuleType = _XylanFltIpxRuleType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 3, 1, 1),
    _XylanFltIpxRuleType_Type()
)
xylanFltIpxRuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltIpxRuleType.setStatus("mandatory")
_XylanFltIpxRuleID_Type = Integer32
_XylanFltIpxRuleID_Object = MibTableColumn
xylanFltIpxRuleID = _XylanFltIpxRuleID_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 3, 1, 2),
    _XylanFltIpxRuleID_Type()
)
xylanFltIpxRuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltIpxRuleID.setStatus("mandatory")


class _XylanFltIpxRuleNet_Type(OctetString):
    """Custom type xylanFltIpxRuleNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_XylanFltIpxRuleNet_Type.__name__ = "OctetString"
_XylanFltIpxRuleNet_Object = MibTableColumn
xylanFltIpxRuleNet = _XylanFltIpxRuleNet_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 3, 1, 3),
    _XylanFltIpxRuleNet_Type()
)
xylanFltIpxRuleNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltIpxRuleNet.setStatus("mandatory")


class _XylanFltIpxRuleNode_Type(OctetString):
    """Custom type xylanFltIpxRuleNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_XylanFltIpxRuleNode_Type.__name__ = "OctetString"
_XylanFltIpxRuleNode_Object = MibTableColumn
xylanFltIpxRuleNode = _XylanFltIpxRuleNode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 3, 1, 4),
    _XylanFltIpxRuleNode_Type()
)
xylanFltIpxRuleNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltIpxRuleNode.setStatus("mandatory")


class _XylanFltIpxRuleDisp_Type(Integer32):
    """Custom type xylanFltIpxRuleDisp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_XylanFltIpxRuleDisp_Type.__name__ = "Integer32"
_XylanFltIpxRuleDisp_Object = MibTableColumn
xylanFltIpxRuleDisp = _XylanFltIpxRuleDisp_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 3, 1, 5),
    _XylanFltIpxRuleDisp_Type()
)
xylanFltIpxRuleDisp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltIpxRuleDisp.setStatus("mandatory")
_XylanFltIpxRuleCount_Type = Integer32
_XylanFltIpxRuleCount_Object = MibTableColumn
xylanFltIpxRuleCount = _XylanFltIpxRuleCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 3, 1, 6),
    _XylanFltIpxRuleCount_Type()
)
xylanFltIpxRuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltIpxRuleCount.setStatus("mandatory")


class _XylanFltIpxRuleGroup_Type(DisplayString):
    """Custom type xylanFltIpxRuleGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_XylanFltIpxRuleGroup_Type.__name__ = "DisplayString"
_XylanFltIpxRuleGroup_Object = MibTableColumn
xylanFltIpxRuleGroup = _XylanFltIpxRuleGroup_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 3, 1, 7),
    _XylanFltIpxRuleGroup_Type()
)
xylanFltIpxRuleGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltIpxRuleGroup.setStatus("mandatory")
_XylanFltIpQueries_Object = MibTable
xylanFltIpQueries = _XylanFltIpQueries_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 4)
)
if mibBuilder.loadTexts:
    xylanFltIpQueries.setStatus("mandatory")
_XylanFltIpQuery_Object = MibTableRow
xylanFltIpQuery = _XylanFltIpQuery_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 4, 1)
)
xylanFltIpQuery.setIndexNames(
    (0, "XYLAN-FLT-MIB", "xylanFltIpQueryDest"),
    (0, "XYLAN-FLT-MIB", "xylanFltIpQuerySrc"),
    (0, "XYLAN-FLT-MIB", "xylanFltIpQueryPort"),
)
if mibBuilder.loadTexts:
    xylanFltIpQuery.setStatus("mandatory")
_XylanFltIpQueryDest_Type = IpAddress
_XylanFltIpQueryDest_Object = MibTableColumn
xylanFltIpQueryDest = _XylanFltIpQueryDest_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 4, 1, 1),
    _XylanFltIpQueryDest_Type()
)
xylanFltIpQueryDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltIpQueryDest.setStatus("mandatory")
_XylanFltIpQuerySrc_Type = IpAddress
_XylanFltIpQuerySrc_Object = MibTableColumn
xylanFltIpQuerySrc = _XylanFltIpQuerySrc_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 4, 1, 2),
    _XylanFltIpQuerySrc_Type()
)
xylanFltIpQuerySrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltIpQuerySrc.setStatus("mandatory")


class _XylanFltIpQueryPort_Type(Integer32):
    """Custom type xylanFltIpQueryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XylanFltIpQueryPort_Type.__name__ = "Integer32"
_XylanFltIpQueryPort_Object = MibTableColumn
xylanFltIpQueryPort = _XylanFltIpQueryPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 4, 1, 3),
    _XylanFltIpQueryPort_Type()
)
xylanFltIpQueryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltIpQueryPort.setStatus("mandatory")


class _XylanFltIpQueryDisp_Type(Integer32):
    """Custom type xylanFltIpQueryDisp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_XylanFltIpQueryDisp_Type.__name__ = "Integer32"
_XylanFltIpQueryDisp_Object = MibTableColumn
xylanFltIpQueryDisp = _XylanFltIpQueryDisp_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 4, 1, 4),
    _XylanFltIpQueryDisp_Type()
)
xylanFltIpQueryDisp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltIpQueryDisp.setStatus("mandatory")


class _XylanFltIpQueryService_Type(DisplayString):
    """Custom type xylanFltIpQueryService based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_XylanFltIpQueryService_Type.__name__ = "DisplayString"
_XylanFltIpQueryService_Object = MibTableColumn
xylanFltIpQueryService = _XylanFltIpQueryService_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 4, 1, 5),
    _XylanFltIpQueryService_Type()
)
xylanFltIpQueryService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltIpQueryService.setStatus("mandatory")
_XylanFltIpQueryRuleID_Type = Integer32
_XylanFltIpQueryRuleID_Object = MibTableColumn
xylanFltIpQueryRuleID = _XylanFltIpQueryRuleID_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 4, 1, 6),
    _XylanFltIpQueryRuleID_Type()
)
xylanFltIpQueryRuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltIpQueryRuleID.setStatus("mandatory")
_XylanFltIpxQueries_Object = MibTable
xylanFltIpxQueries = _XylanFltIpxQueries_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 5)
)
if mibBuilder.loadTexts:
    xylanFltIpxQueries.setStatus("mandatory")
_XylanFltIpxQuery_Object = MibTableRow
xylanFltIpxQuery = _XylanFltIpxQuery_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 5, 1)
)
xylanFltIpxQuery.setIndexNames(
    (0, "XYLAN-FLT-MIB", "xylanFltIpxQueryNetwork"),
    (0, "XYLAN-FLT-MIB", "xylanFltIpxQueryNode"),
)
if mibBuilder.loadTexts:
    xylanFltIpxQuery.setStatus("mandatory")


class _XylanFltIpxQueryNetwork_Type(OctetString):
    """Custom type xylanFltIpxQueryNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_XylanFltIpxQueryNetwork_Type.__name__ = "OctetString"
_XylanFltIpxQueryNetwork_Object = MibTableColumn
xylanFltIpxQueryNetwork = _XylanFltIpxQueryNetwork_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 5, 1, 1),
    _XylanFltIpxQueryNetwork_Type()
)
xylanFltIpxQueryNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltIpxQueryNetwork.setStatus("mandatory")


class _XylanFltIpxQueryNode_Type(OctetString):
    """Custom type xylanFltIpxQueryNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_XylanFltIpxQueryNode_Type.__name__ = "OctetString"
_XylanFltIpxQueryNode_Object = MibTableColumn
xylanFltIpxQueryNode = _XylanFltIpxQueryNode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 5, 1, 2),
    _XylanFltIpxQueryNode_Type()
)
xylanFltIpxQueryNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltIpxQueryNode.setStatus("mandatory")


class _XylanFltIpxQueryDisp_Type(Integer32):
    """Custom type xylanFltIpxQueryDisp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_XylanFltIpxQueryDisp_Type.__name__ = "Integer32"
_XylanFltIpxQueryDisp_Object = MibTableColumn
xylanFltIpxQueryDisp = _XylanFltIpxQueryDisp_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 5, 1, 3),
    _XylanFltIpxQueryDisp_Type()
)
xylanFltIpxQueryDisp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltIpxQueryDisp.setStatus("mandatory")


class _XylanFltIpxQueryRuleType_Type(Integer32):
    """Custom type xylanFltIpxQueryRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("full-address", 1),
          ("global", 4),
          ("network", 3),
          ("no-rule-applies", 0),
          ("node", 2))
    )


_XylanFltIpxQueryRuleType_Type.__name__ = "Integer32"
_XylanFltIpxQueryRuleType_Object = MibTableColumn
xylanFltIpxQueryRuleType = _XylanFltIpxQueryRuleType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 5, 1, 4),
    _XylanFltIpxQueryRuleType_Type()
)
xylanFltIpxQueryRuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltIpxQueryRuleType.setStatus("mandatory")
_XylanFltIpxQueryRuleID_Type = Integer32
_XylanFltIpxQueryRuleID_Object = MibTableColumn
xylanFltIpxQueryRuleID = _XylanFltIpxQueryRuleID_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 5, 1, 5),
    _XylanFltIpxQueryRuleID_Type()
)
xylanFltIpxQueryRuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltIpxQueryRuleID.setStatus("mandatory")


class _XylanFltActDefaultIpDisp_Type(Integer32):
    """Custom type xylanFltActDefaultIpDisp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_XylanFltActDefaultIpDisp_Type.__name__ = "Integer32"
_XylanFltActDefaultIpDisp_Object = MibScalar
xylanFltActDefaultIpDisp = _XylanFltActDefaultIpDisp_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 6),
    _XylanFltActDefaultIpDisp_Type()
)
xylanFltActDefaultIpDisp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltActDefaultIpDisp.setStatus("mandatory")


class _XylanFltActIpPrecedence_Type(Integer32):
    """Custom type xylanFltActIpPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destination", 1),
          ("source", 2))
    )


_XylanFltActIpPrecedence_Type.__name__ = "Integer32"
_XylanFltActIpPrecedence_Object = MibScalar
xylanFltActIpPrecedence = _XylanFltActIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 7),
    _XylanFltActIpPrecedence_Type()
)
xylanFltActIpPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltActIpPrecedence.setStatus("mandatory")


class _XylanFltActDefaultIpxDisp_Type(Integer32):
    """Custom type xylanFltActDefaultIpxDisp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_XylanFltActDefaultIpxDisp_Type.__name__ = "Integer32"
_XylanFltActDefaultIpxDisp_Object = MibScalar
xylanFltActDefaultIpxDisp = _XylanFltActDefaultIpxDisp_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 3, 8),
    _XylanFltActDefaultIpxDisp_Type()
)
xylanFltActDefaultIpxDisp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltActDefaultIpxDisp.setStatus("mandatory")
_XylanFltTraps_ObjectIdentity = ObjectIdentity
xylanFltTraps = _XylanFltTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 4)
)
_XylanFltIpTrapInfo_ObjectIdentity = ObjectIdentity
xylanFltIpTrapInfo = _XylanFltIpTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 4, 1)
)
_XylanFltLastIpDenySrc_Type = IpAddress
_XylanFltLastIpDenySrc_Object = MibScalar
xylanFltLastIpDenySrc = _XylanFltLastIpDenySrc_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 4, 1, 1),
    _XylanFltLastIpDenySrc_Type()
)
xylanFltLastIpDenySrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltLastIpDenySrc.setStatus("mandatory")
_XylanFltLastIpDenyDest_Type = IpAddress
_XylanFltLastIpDenyDest_Object = MibScalar
xylanFltLastIpDenyDest = _XylanFltLastIpDenyDest_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 4, 1, 2),
    _XylanFltLastIpDenyDest_Type()
)
xylanFltLastIpDenyDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltLastIpDenyDest.setStatus("mandatory")
_XylanFltLastIpDenyPort_Type = Integer32
_XylanFltLastIpDenyPort_Object = MibScalar
xylanFltLastIpDenyPort = _XylanFltLastIpDenyPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 4, 1, 3),
    _XylanFltLastIpDenyPort_Type()
)
xylanFltLastIpDenyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltLastIpDenyPort.setStatus("mandatory")
_XylanFltIpxTrapInfo_ObjectIdentity = ObjectIdentity
xylanFltIpxTrapInfo = _XylanFltIpxTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 4, 2)
)


class _XylanFltLastIpxDenyNet_Type(OctetString):
    """Custom type xylanFltLastIpxDenyNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_XylanFltLastIpxDenyNet_Type.__name__ = "OctetString"
_XylanFltLastIpxDenyNet_Object = MibScalar
xylanFltLastIpxDenyNet = _XylanFltLastIpxDenyNet_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 4, 2, 1),
    _XylanFltLastIpxDenyNet_Type()
)
xylanFltLastIpxDenyNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltLastIpxDenyNet.setStatus("mandatory")


class _XylanFltLastIpxDenyNode_Type(OctetString):
    """Custom type xylanFltLastIpxDenyNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_XylanFltLastIpxDenyNode_Type.__name__ = "OctetString"
_XylanFltLastIpxDenyNode_Object = MibScalar
xylanFltLastIpxDenyNode = _XylanFltLastIpxDenyNode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 4, 2, 2),
    _XylanFltLastIpxDenyNode_Type()
)
xylanFltLastIpxDenyNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltLastIpxDenyNode.setStatus("mandatory")
_XylanFltCommitTrapInfo_ObjectIdentity = ObjectIdentity
xylanFltCommitTrapInfo = _XylanFltCommitTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 4, 3)
)


class _XylanFltLastCommitTrapReason_Type(Integer32):
    """Custom type xylanFltLastCommitTrapReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("duplicate-service-names", 5),
          ("group-not-found", 2),
          ("ipx-in-non-global-group", 3),
          ("no-trap-sent", 0),
          ("port-in-two-services", 4),
          ("same-ipx-address-for-two-rules", 6),
          ("service-not-found", 1))
    )


_XylanFltLastCommitTrapReason_Type.__name__ = "Integer32"
_XylanFltLastCommitTrapReason_Object = MibScalar
xylanFltLastCommitTrapReason = _XylanFltLastCommitTrapReason_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 4, 3, 1),
    _XylanFltLastCommitTrapReason_Type()
)
xylanFltLastCommitTrapReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltLastCommitTrapReason.setStatus("mandatory")


class _XylanFltLastCommitTrapEntity1_Type(DisplayString):
    """Custom type xylanFltLastCommitTrapEntity1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_XylanFltLastCommitTrapEntity1_Type.__name__ = "DisplayString"
_XylanFltLastCommitTrapEntity1_Object = MibScalar
xylanFltLastCommitTrapEntity1 = _XylanFltLastCommitTrapEntity1_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 4, 3, 2),
    _XylanFltLastCommitTrapEntity1_Type()
)
xylanFltLastCommitTrapEntity1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltLastCommitTrapEntity1.setStatus("mandatory")


class _XylanFltLastCommitTrapEntity2_Type(DisplayString):
    """Custom type xylanFltLastCommitTrapEntity2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_XylanFltLastCommitTrapEntity2_Type.__name__ = "DisplayString"
_XylanFltLastCommitTrapEntity2_Object = MibScalar
xylanFltLastCommitTrapEntity2 = _XylanFltLastCommitTrapEntity2_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 4, 3, 3),
    _XylanFltLastCommitTrapEntity2_Type()
)
xylanFltLastCommitTrapEntity2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltLastCommitTrapEntity2.setStatus("optional")
_XylanFltLastCommitTrapPort_Type = Integer32
_XylanFltLastCommitTrapPort_Object = MibScalar
xylanFltLastCommitTrapPort = _XylanFltLastCommitTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 4, 3, 4),
    _XylanFltLastCommitTrapPort_Type()
)
xylanFltLastCommitTrapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltLastCommitTrapPort.setStatus("optional")


class _XylanFltLastCommitTrapIpxNet_Type(OctetString):
    """Custom type xylanFltLastCommitTrapIpxNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_XylanFltLastCommitTrapIpxNet_Type.__name__ = "OctetString"
_XylanFltLastCommitTrapIpxNet_Object = MibScalar
xylanFltLastCommitTrapIpxNet = _XylanFltLastCommitTrapIpxNet_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 4, 3, 5),
    _XylanFltLastCommitTrapIpxNet_Type()
)
xylanFltLastCommitTrapIpxNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltLastCommitTrapIpxNet.setStatus("optional")


class _XylanFltLastCommitTrapIpxNode_Type(OctetString):
    """Custom type xylanFltLastCommitTrapIpxNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_XylanFltLastCommitTrapIpxNode_Type.__name__ = "OctetString"
_XylanFltLastCommitTrapIpxNode_Object = MibScalar
xylanFltLastCommitTrapIpxNode = _XylanFltLastCommitTrapIpxNode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 22, 4, 3, 6),
    _XylanFltLastCommitTrapIpxNode_Type()
)
xylanFltLastCommitTrapIpxNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanFltLastCommitTrapIpxNode.setStatus("optional")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-FLT-MIB",
    **{"xylanFltStatus": xylanFltStatus,
       "xylanFltActiveAdminState": xylanFltActiveAdminState,
       "xylanFltActiveOperState": xylanFltActiveOperState,
       "xylanFltConfigAdminState": xylanFltConfigAdminState,
       "xylanFltCommit": xylanFltCommit,
       "xylanFltStaticConfig": xylanFltStaticConfig,
       "xylanFltGroups": xylanFltGroups,
       "xylanFltGroupTable": xylanFltGroupTable,
       "xylanFltGroupEntry": xylanFltGroupEntry,
       "xylanFltGroupIndex": xylanFltGroupIndex,
       "xylanFltGroupAdminState": xylanFltGroupAdminState,
       "xylanFltGroupProtocol": xylanFltGroupProtocol,
       "xylanFltGroupAdrType": xylanFltGroupAdrType,
       "xylanFltRuleListTable": xylanFltRuleListTable,
       "xylanFltRuleListEntry": xylanFltRuleListEntry,
       "xylanFltRuleListIndex": xylanFltRuleListIndex,
       "xylanFltRuleListAdminState": xylanFltRuleListAdminState,
       "xylanFltRuleListRule": xylanFltRuleListRule,
       "xylanFltServices": xylanFltServices,
       "xylanFltServiceTable": xylanFltServiceTable,
       "xylanFltServiceEntry": xylanFltServiceEntry,
       "xylanFltServiceIndex": xylanFltServiceIndex,
       "xylanFltServiceAdminState": xylanFltServiceAdminState,
       "xylanFltServiceNumberTable": xylanFltServiceNumberTable,
       "xylanFltServiceNumberEntry": xylanFltServiceNumberEntry,
       "xylanFltServiceNumberIndex": xylanFltServiceNumberIndex,
       "xylanFltServiceNumberAdminState": xylanFltServiceNumberAdminState,
       "xylanFltServiceGroupTable": xylanFltServiceGroupTable,
       "xylanFltServiceGroupEntry": xylanFltServiceGroupEntry,
       "xylanFltServiceGroupIndex": xylanFltServiceGroupIndex,
       "xylanFltServiceGroupAdminState": xylanFltServiceGroupAdminState,
       "xylanFltGlobals": xylanFltGlobals,
       "xylanFltGlobalIPRule": xylanFltGlobalIPRule,
       "xylanFltGlobalIPXRule": xylanFltGlobalIPXRule,
       "xylanFltGlobalPrecedence": xylanFltGlobalPrecedence,
       "xylanFltGlobalGroupTable": xylanFltGlobalGroupTable,
       "xylanFltGlobalGroupEntry": xylanFltGlobalGroupEntry,
       "xylanFltGlobalGroupIndex": xylanFltGlobalGroupIndex,
       "xylanFltGlobalGroupAdminState": xylanFltGlobalGroupAdminState,
       "xylanFltGlobalServiceTable": xylanFltGlobalServiceTable,
       "xylanFltGlobalServiceEntry": xylanFltGlobalServiceEntry,
       "xylanFltGlobalServiceIndex": xylanFltGlobalServiceIndex,
       "xylanFltGlobalServiceAdminState": xylanFltGlobalServiceAdminState,
       "xylanFltActiveConfig": xylanFltActiveConfig,
       "xylanFltIpServicePortTbl": xylanFltIpServicePortTbl,
       "xylanFltIpServicePortTblEntry": xylanFltIpServicePortTblEntry,
       "xylanFltIpServicePortName": xylanFltIpServicePortName,
       "xylanFltIpServicePortNumber": xylanFltIpServicePortNumber,
       "xylanFltIpServiceRuleTbl": xylanFltIpServiceRuleTbl,
       "xylanFltIpServiceRuleTblEntry": xylanFltIpServiceRuleTblEntry,
       "xylanFltIpServiceRuleName": xylanFltIpServiceRuleName,
       "xylanFltIpServiceRuleID": xylanFltIpServiceRuleID,
       "xylanFltIpServiceRuleDest": xylanFltIpServiceRuleDest,
       "xylanFltIpServiceRuleDestMask": xylanFltIpServiceRuleDestMask,
       "xylanFltIpServiceRuleSrc": xylanFltIpServiceRuleSrc,
       "xylanFltIpServiceRuleSrcMask": xylanFltIpServiceRuleSrcMask,
       "xylanFltIpServiceRuleDisp": xylanFltIpServiceRuleDisp,
       "xylanFltIpServiceRuleCount": xylanFltIpServiceRuleCount,
       "xylanFltIpServiceRuleGroup": xylanFltIpServiceRuleGroup,
       "xylanFltIpxRuleTbl": xylanFltIpxRuleTbl,
       "xylanFltIpxRuleTblEntry": xylanFltIpxRuleTblEntry,
       "xylanFltIpxRuleType": xylanFltIpxRuleType,
       "xylanFltIpxRuleID": xylanFltIpxRuleID,
       "xylanFltIpxRuleNet": xylanFltIpxRuleNet,
       "xylanFltIpxRuleNode": xylanFltIpxRuleNode,
       "xylanFltIpxRuleDisp": xylanFltIpxRuleDisp,
       "xylanFltIpxRuleCount": xylanFltIpxRuleCount,
       "xylanFltIpxRuleGroup": xylanFltIpxRuleGroup,
       "xylanFltIpQueries": xylanFltIpQueries,
       "xylanFltIpQuery": xylanFltIpQuery,
       "xylanFltIpQueryDest": xylanFltIpQueryDest,
       "xylanFltIpQuerySrc": xylanFltIpQuerySrc,
       "xylanFltIpQueryPort": xylanFltIpQueryPort,
       "xylanFltIpQueryDisp": xylanFltIpQueryDisp,
       "xylanFltIpQueryService": xylanFltIpQueryService,
       "xylanFltIpQueryRuleID": xylanFltIpQueryRuleID,
       "xylanFltIpxQueries": xylanFltIpxQueries,
       "xylanFltIpxQuery": xylanFltIpxQuery,
       "xylanFltIpxQueryNetwork": xylanFltIpxQueryNetwork,
       "xylanFltIpxQueryNode": xylanFltIpxQueryNode,
       "xylanFltIpxQueryDisp": xylanFltIpxQueryDisp,
       "xylanFltIpxQueryRuleType": xylanFltIpxQueryRuleType,
       "xylanFltIpxQueryRuleID": xylanFltIpxQueryRuleID,
       "xylanFltActDefaultIpDisp": xylanFltActDefaultIpDisp,
       "xylanFltActIpPrecedence": xylanFltActIpPrecedence,
       "xylanFltActDefaultIpxDisp": xylanFltActDefaultIpxDisp,
       "xylanFltTraps": xylanFltTraps,
       "xylanFltIpTrapInfo": xylanFltIpTrapInfo,
       "xylanFltLastIpDenySrc": xylanFltLastIpDenySrc,
       "xylanFltLastIpDenyDest": xylanFltLastIpDenyDest,
       "xylanFltLastIpDenyPort": xylanFltLastIpDenyPort,
       "xylanFltIpxTrapInfo": xylanFltIpxTrapInfo,
       "xylanFltLastIpxDenyNet": xylanFltLastIpxDenyNet,
       "xylanFltLastIpxDenyNode": xylanFltLastIpxDenyNode,
       "xylanFltCommitTrapInfo": xylanFltCommitTrapInfo,
       "xylanFltLastCommitTrapReason": xylanFltLastCommitTrapReason,
       "xylanFltLastCommitTrapEntity1": xylanFltLastCommitTrapEntity1,
       "xylanFltLastCommitTrapEntity2": xylanFltLastCommitTrapEntity2,
       "xylanFltLastCommitTrapPort": xylanFltLastCommitTrapPort,
       "xylanFltLastCommitTrapIpxNet": xylanFltLastCommitTrapIpxNet,
       "xylanFltLastCommitTrapIpxNode": xylanFltLastCommitTrapIpxNode}
)
