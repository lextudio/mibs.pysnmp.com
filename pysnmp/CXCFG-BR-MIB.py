# SNMP MIB module (CXCFG-BR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXCFG-BR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:11 2024
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

(Alias,
 cxCfgDot1dBase,
 cxCfgSrBase) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "cxCfgDot1dBase",
    "cxCfgSrBase")

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

_CxCfgDot1dBaseNumOfDBFilterEntries_Type = Integer32
_CxCfgDot1dBaseNumOfDBFilterEntries_Object = MibScalar
cxCfgDot1dBaseNumOfDBFilterEntries = _CxCfgDot1dBaseNumOfDBFilterEntries_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 14, 1),
    _CxCfgDot1dBaseNumOfDBFilterEntries_Type()
)
cxCfgDot1dBaseNumOfDBFilterEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgDot1dBaseNumOfDBFilterEntries.setStatus("mandatory")
_CxCfgDot1dBaseNumOfStaticDBFilterEntries_Type = Integer32
_CxCfgDot1dBaseNumOfStaticDBFilterEntries_Object = MibScalar
cxCfgDot1dBaseNumOfStaticDBFilterEntries = _CxCfgDot1dBaseNumOfStaticDBFilterEntries_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 14, 2),
    _CxCfgDot1dBaseNumOfStaticDBFilterEntries_Type()
)
cxCfgDot1dBaseNumOfStaticDBFilterEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgDot1dBaseNumOfStaticDBFilterEntries.setStatus("mandatory")
_CxCfgDot1dBasePortTable_Object = MibTable
cxCfgDot1dBasePortTable = _CxCfgDot1dBasePortTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 14, 3)
)
if mibBuilder.loadTexts:
    cxCfgDot1dBasePortTable.setStatus("mandatory")
_CxCfgDot1dBasePortEntry_Object = MibTableRow
cxCfgDot1dBasePortEntry = _CxCfgDot1dBasePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 14, 3, 1)
)
cxCfgDot1dBasePortEntry.setIndexNames(
    (0, "CXCFG-BR-MIB", "cxCfgDot1dBasePort"),
)
if mibBuilder.loadTexts:
    cxCfgDot1dBasePortEntry.setStatus("mandatory")


class _CxCfgDot1dBasePort_Type(Integer32):
    """Custom type cxCfgDot1dBasePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CxCfgDot1dBasePort_Type.__name__ = "Integer32"
_CxCfgDot1dBasePort_Object = MibTableColumn
cxCfgDot1dBasePort = _CxCfgDot1dBasePort_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 14, 3, 1, 1),
    _CxCfgDot1dBasePort_Type()
)
cxCfgDot1dBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxCfgDot1dBasePort.setStatus("mandatory")
_CxCfgDot1dBasePortIfIndex_Type = Integer32
_CxCfgDot1dBasePortIfIndex_Object = MibTableColumn
cxCfgDot1dBasePortIfIndex = _CxCfgDot1dBasePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 14, 3, 1, 2),
    _CxCfgDot1dBasePortIfIndex_Type()
)
cxCfgDot1dBasePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxCfgDot1dBasePortIfIndex.setStatus("mandatory")
_CxCfgDot1dBasePortSubnetworkSapAlias_Type = Alias
_CxCfgDot1dBasePortSubnetworkSapAlias_Object = MibTableColumn
cxCfgDot1dBasePortSubnetworkSapAlias = _CxCfgDot1dBasePortSubnetworkSapAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 14, 3, 1, 3),
    _CxCfgDot1dBasePortSubnetworkSapAlias_Type()
)
cxCfgDot1dBasePortSubnetworkSapAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgDot1dBasePortSubnetworkSapAlias.setStatus("mandatory")


class _CxCfgDot1dBasePortRowStatus_Type(Integer32):
    """Custom type cxCfgDot1dBasePortRowStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_CxCfgDot1dBasePortRowStatus_Type.__name__ = "Integer32"
_CxCfgDot1dBasePortRowStatus_Object = MibTableColumn
cxCfgDot1dBasePortRowStatus = _CxCfgDot1dBasePortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 14, 3, 1, 4),
    _CxCfgDot1dBasePortRowStatus_Type()
)
cxCfgDot1dBasePortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgDot1dBasePortRowStatus.setStatus("mandatory")


class _CxCfgDot1dBasePortState_Type(Integer32):
    """Custom type cxCfgDot1dBasePortState based on Integer32"""
    defaultValue = 1

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
        *(("off", 2),
          ("on", 1),
          ("onether", 3),
          ("ontoken", 4))
    )


_CxCfgDot1dBasePortState_Type.__name__ = "Integer32"
_CxCfgDot1dBasePortState_Object = MibTableColumn
cxCfgDot1dBasePortState = _CxCfgDot1dBasePortState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 14, 3, 1, 5),
    _CxCfgDot1dBasePortState_Type()
)
cxCfgDot1dBasePortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgDot1dBasePortState.setStatus("mandatory")


class _CxCfgDot1dBasePortPriority_Type(Integer32):
    """Custom type cxCfgDot1dBasePortPriority based on Integer32"""
    defaultValue = 2

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
        *(("discard", 1),
          ("forward", 2),
          ("priority-high", 4),
          ("priority-low", 3))
    )


_CxCfgDot1dBasePortPriority_Type.__name__ = "Integer32"
_CxCfgDot1dBasePortPriority_Object = MibTableColumn
cxCfgDot1dBasePortPriority = _CxCfgDot1dBasePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 14, 3, 1, 6),
    _CxCfgDot1dBasePortPriority_Type()
)
cxCfgDot1dBasePortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgDot1dBasePortPriority.setStatus("mandatory")


class _CxCfgDot1dBaseMibLevel_Type(Integer32):
    """Custom type cxCfgDot1dBaseMibLevel based on Integer32"""
    defaultValue = 0


_CxCfgDot1dBaseMibLevel_Object = MibScalar
cxCfgDot1dBaseMibLevel = _CxCfgDot1dBaseMibLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 14, 4),
    _CxCfgDot1dBaseMibLevel_Type()
)
cxCfgDot1dBaseMibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxCfgDot1dBaseMibLevel.setStatus("mandatory")
_CxCfgSrBasePortTable_Object = MibTable
cxCfgSrBasePortTable = _CxCfgSrBasePortTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 17, 1)
)
if mibBuilder.loadTexts:
    cxCfgSrBasePortTable.setStatus("mandatory")
_CxCfgSrBasePortEntry_Object = MibTableRow
cxCfgSrBasePortEntry = _CxCfgSrBasePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 17, 1, 1)
)
cxCfgSrBasePortEntry.setIndexNames(
    (0, "CXCFG-BR-MIB", "cxCfgSrBasePort"),
)
if mibBuilder.loadTexts:
    cxCfgSrBasePortEntry.setStatus("mandatory")


class _CxCfgSrBasePort_Type(Integer32):
    """Custom type cxCfgSrBasePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CxCfgSrBasePort_Type.__name__ = "Integer32"
_CxCfgSrBasePort_Object = MibTableColumn
cxCfgSrBasePort = _CxCfgSrBasePort_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 17, 1, 1, 1),
    _CxCfgSrBasePort_Type()
)
cxCfgSrBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxCfgSrBasePort.setStatus("mandatory")
_CxCfgSrBasePortIfIndex_Type = Integer32
_CxCfgSrBasePortIfIndex_Object = MibTableColumn
cxCfgSrBasePortIfIndex = _CxCfgSrBasePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 17, 1, 1, 2),
    _CxCfgSrBasePortIfIndex_Type()
)
cxCfgSrBasePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxCfgSrBasePortIfIndex.setStatus("mandatory")
_CxCfgSrBasePortSubnetworkSapAlias_Type = Alias
_CxCfgSrBasePortSubnetworkSapAlias_Object = MibTableColumn
cxCfgSrBasePortSubnetworkSapAlias = _CxCfgSrBasePortSubnetworkSapAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 17, 1, 1, 3),
    _CxCfgSrBasePortSubnetworkSapAlias_Type()
)
cxCfgSrBasePortSubnetworkSapAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgSrBasePortSubnetworkSapAlias.setStatus("mandatory")


class _CxCfgSrBasePortRowStatus_Type(Integer32):
    """Custom type cxCfgSrBasePortRowStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_CxCfgSrBasePortRowStatus_Type.__name__ = "Integer32"
_CxCfgSrBasePortRowStatus_Object = MibTableColumn
cxCfgSrBasePortRowStatus = _CxCfgSrBasePortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 17, 1, 1, 4),
    _CxCfgSrBasePortRowStatus_Type()
)
cxCfgSrBasePortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgSrBasePortRowStatus.setStatus("mandatory")


class _CxCfgSrBasePortState_Type(Integer32):
    """Custom type cxCfgSrBasePortState based on Integer32"""
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
        *(("off", 2),
          ("on", 1),
          ("ontoken", 3))
    )


_CxCfgSrBasePortState_Type.__name__ = "Integer32"
_CxCfgSrBasePortState_Object = MibTableColumn
cxCfgSrBasePortState = _CxCfgSrBasePortState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 17, 1, 1, 5),
    _CxCfgSrBasePortState_Type()
)
cxCfgSrBasePortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgSrBasePortState.setStatus("mandatory")


class _CxCfgSrBasePortPriority_Type(Integer32):
    """Custom type cxCfgSrBasePortPriority based on Integer32"""
    defaultValue = 2

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
        *(("discard", 1),
          ("forward", 2),
          ("priority-high", 4),
          ("priority-low", 3))
    )


_CxCfgSrBasePortPriority_Type.__name__ = "Integer32"
_CxCfgSrBasePortPriority_Object = MibTableColumn
cxCfgSrBasePortPriority = _CxCfgSrBasePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 17, 1, 1, 6),
    _CxCfgSrBasePortPriority_Type()
)
cxCfgSrBasePortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCfgSrBasePortPriority.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXCFG-BR-MIB",
    **{"cxCfgDot1dBaseNumOfDBFilterEntries": cxCfgDot1dBaseNumOfDBFilterEntries,
       "cxCfgDot1dBaseNumOfStaticDBFilterEntries": cxCfgDot1dBaseNumOfStaticDBFilterEntries,
       "cxCfgDot1dBasePortTable": cxCfgDot1dBasePortTable,
       "cxCfgDot1dBasePortEntry": cxCfgDot1dBasePortEntry,
       "cxCfgDot1dBasePort": cxCfgDot1dBasePort,
       "cxCfgDot1dBasePortIfIndex": cxCfgDot1dBasePortIfIndex,
       "cxCfgDot1dBasePortSubnetworkSapAlias": cxCfgDot1dBasePortSubnetworkSapAlias,
       "cxCfgDot1dBasePortRowStatus": cxCfgDot1dBasePortRowStatus,
       "cxCfgDot1dBasePortState": cxCfgDot1dBasePortState,
       "cxCfgDot1dBasePortPriority": cxCfgDot1dBasePortPriority,
       "cxCfgDot1dBaseMibLevel": cxCfgDot1dBaseMibLevel,
       "cxCfgSrBasePortTable": cxCfgSrBasePortTable,
       "cxCfgSrBasePortEntry": cxCfgSrBasePortEntry,
       "cxCfgSrBasePort": cxCfgSrBasePort,
       "cxCfgSrBasePortIfIndex": cxCfgSrBasePortIfIndex,
       "cxCfgSrBasePortSubnetworkSapAlias": cxCfgSrBasePortSubnetworkSapAlias,
       "cxCfgSrBasePortRowStatus": cxCfgSrBasePortRowStatus,
       "cxCfgSrBasePortState": cxCfgSrBasePortState,
       "cxCfgSrBasePortPriority": cxCfgSrBasePortPriority}
)
