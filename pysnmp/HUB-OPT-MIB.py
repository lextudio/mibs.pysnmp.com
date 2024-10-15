# SNMP MIB module (HUB-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUB-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:48 2024
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Codex_ObjectIdentity = ObjectIdentity
codex = _Codex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449)
)
_CdxProductSpecific_ObjectIdentity = ObjectIdentity
cdxProductSpecific = _CdxProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2)
)
_Cdx6500_ObjectIdentity = ObjectIdentity
cdx6500 = _Cdx6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1)
)
_Cdx6500Configuration_ObjectIdentity = ObjectIdentity
cdx6500Configuration = _Cdx6500Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2)
)
_Cdx6500CfgProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500CfgProtocolGroup = _Cdx6500CfgProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1)
)
_Cdx6500PCTPortProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTPortProtocolGroup = _Cdx6500PCTPortProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1)
)
_Cdx6500PPCTHUBPortTable_Object = MibTable
cdx6500PPCTHUBPortTable = _Cdx6500PPCTHUBPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 22)
)
if mibBuilder.loadTexts:
    cdx6500PPCTHUBPortTable.setStatus("mandatory")
_Cdx6500PPCTHUBPortEntry_Object = MibTableRow
cdx6500PPCTHUBPortEntry = _Cdx6500PPCTHUBPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 22, 1)
)
cdx6500PPCTHUBPortEntry.setIndexNames(
    (0, "HUB-OPT-MIB", "cdx6500HUBCfgPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPCTHUBPortEntry.setStatus("mandatory")


class _Cdx6500HUBCfgPortNumber_Type(Integer32):
    """Custom type cdx6500HUBCfgPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(13, 54),
    )


_Cdx6500HUBCfgPortNumber_Type.__name__ = "Integer32"
_Cdx6500HUBCfgPortNumber_Object = MibTableColumn
cdx6500HUBCfgPortNumber = _Cdx6500HUBCfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 22, 1, 1),
    _Cdx6500HUBCfgPortNumber_Type()
)
cdx6500HUBCfgPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500HUBCfgPortNumber.setStatus("mandatory")


class _Cdx6500HUBCfgPortLevel_Type(Integer32):
    """Custom type cdx6500HUBCfgPortLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reduced", 2))
    )


_Cdx6500HUBCfgPortLevel_Type.__name__ = "Integer32"
_Cdx6500HUBCfgPortLevel_Object = MibTableColumn
cdx6500HUBCfgPortLevel = _Cdx6500HUBCfgPortLevel_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 22, 1, 2),
    _Cdx6500HUBCfgPortLevel_Type()
)
cdx6500HUBCfgPortLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500HUBCfgPortLevel.setStatus("mandatory")
_Cdx6500Statistics_ObjectIdentity = ObjectIdentity
cdx6500Statistics = _Cdx6500Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3)
)
_Cdx6500StatProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500StatProtocolGroup = _Cdx6500StatProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1)
)
_Cdx6500PSTPortProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTPortProtocolGroup = _Cdx6500PSTPortProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1)
)
_Cdx6500PPSTHUBPortStatTable_Object = MibTable
cdx6500PPSTHUBPortStatTable = _Cdx6500PPSTHUBPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 23)
)
if mibBuilder.loadTexts:
    cdx6500PPSTHUBPortStatTable.setStatus("mandatory")
_Cdx6500HUBPortStatEntry_Object = MibTableRow
cdx6500HUBPortStatEntry = _Cdx6500HUBPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 23, 1)
)
cdx6500HUBPortStatEntry.setIndexNames(
    (0, "HUB-OPT-MIB", "cdx6500HUBStatPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500HUBPortStatEntry.setStatus("mandatory")


class _Cdx6500HUBStatPortNumber_Type(Integer32):
    """Custom type cdx6500HUBStatPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(13, 54),
    )


_Cdx6500HUBStatPortNumber_Type.__name__ = "Integer32"
_Cdx6500HUBStatPortNumber_Object = MibTableColumn
cdx6500HUBStatPortNumber = _Cdx6500HUBStatPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 23, 1, 1),
    _Cdx6500HUBStatPortNumber_Type()
)
cdx6500HUBStatPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500HUBStatPortNumber.setStatus("mandatory")


class _Cdx6500HUBPortStatus_Type(Integer32):
    """Custom type cdx6500HUBPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_Cdx6500HUBPortStatus_Type.__name__ = "Integer32"
_Cdx6500HUBPortStatus_Object = MibTableColumn
cdx6500HUBPortStatus = _Cdx6500HUBPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 23, 1, 2),
    _Cdx6500HUBPortStatus_Type()
)
cdx6500HUBPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500HUBPortStatus.setStatus("mandatory")


class _Cdx6500HUBPortState_Type(Integer32):
    """Custom type cdx6500HUBPortState based on Integer32"""
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


_Cdx6500HUBPortState_Type.__name__ = "Integer32"
_Cdx6500HUBPortState_Object = MibTableColumn
cdx6500HUBPortState = _Cdx6500HUBPortState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 23, 1, 3),
    _Cdx6500HUBPortState_Type()
)
cdx6500HUBPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500HUBPortState.setStatus("mandatory")


class _Cdx6500HUBPortLevel_Type(Integer32):
    """Custom type cdx6500HUBPortLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reduced", 2))
    )


_Cdx6500HUBPortLevel_Type.__name__ = "Integer32"
_Cdx6500HUBPortLevel_Object = MibTableColumn
cdx6500HUBPortLevel = _Cdx6500HUBPortLevel_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 23, 1, 4),
    _Cdx6500HUBPortLevel_Type()
)
cdx6500HUBPortLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500HUBPortLevel.setStatus("mandatory")


class _Cdx6500HUBPortPolarity_Type(Integer32):
    """Custom type cdx6500HUBPortPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inverted", 2),
          ("nonInverted", 1))
    )


_Cdx6500HUBPortPolarity_Type.__name__ = "Integer32"
_Cdx6500HUBPortPolarity_Object = MibTableColumn
cdx6500HUBPortPolarity = _Cdx6500HUBPortPolarity_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 23, 1, 5),
    _Cdx6500HUBPortPolarity_Type()
)
cdx6500HUBPortPolarity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500HUBPortPolarity.setStatus("mandatory")
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUB-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PPCTHUBPortTable": cdx6500PPCTHUBPortTable,
       "cdx6500PPCTHUBPortEntry": cdx6500PPCTHUBPortEntry,
       "cdx6500HUBCfgPortNumber": cdx6500HUBCfgPortNumber,
       "cdx6500HUBCfgPortLevel": cdx6500HUBCfgPortLevel,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PPSTHUBPortStatTable": cdx6500PPSTHUBPortStatTable,
       "cdx6500HUBPortStatEntry": cdx6500HUBPortStatEntry,
       "cdx6500HUBStatPortNumber": cdx6500HUBStatPortNumber,
       "cdx6500HUBPortStatus": cdx6500HUBPortStatus,
       "cdx6500HUBPortState": cdx6500HUBPortState,
       "cdx6500HUBPortLevel": cdx6500HUBPortLevel,
       "cdx6500HUBPortPolarity": cdx6500HUBPortPolarity,
       "cdx6500Controls": cdx6500Controls}
)
