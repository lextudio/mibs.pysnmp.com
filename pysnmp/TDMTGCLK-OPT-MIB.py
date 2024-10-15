# SNMP MIB module (TDMTGCLK-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TDMTGCLK-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:02 2024
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
_Cdx6500CfgGeneralGroup_ObjectIdentity = ObjectIdentity
cdx6500CfgGeneralGroup = _Cdx6500CfgGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2)
)
_Cdx6500TdmtgClkTable_Object = MibTable
cdx6500TdmtgClkTable = _Cdx6500TdmtgClkTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 29)
)
if mibBuilder.loadTexts:
    cdx6500TdmtgClkTable.setStatus("mandatory")
_Cdx6500TdmtgClkCfgEntry_Object = MibTableRow
cdx6500TdmtgClkCfgEntry = _Cdx6500TdmtgClkCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 29, 1)
)
cdx6500TdmtgClkCfgEntry.setIndexNames(
    (0, "TDMTGCLK-OPT-MIB", "cdx6500TdmtgClkEntryNumber"),
)
if mibBuilder.loadTexts:
    cdx6500TdmtgClkCfgEntry.setStatus("mandatory")
_Cdx6500TdmtgClkEntryNumber_Type = Integer32
_Cdx6500TdmtgClkEntryNumber_Object = MibTableColumn
cdx6500TdmtgClkEntryNumber = _Cdx6500TdmtgClkEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 29, 1, 1),
    _Cdx6500TdmtgClkEntryNumber_Type()
)
cdx6500TdmtgClkEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TdmtgClkEntryNumber.setStatus("mandatory")
_Cdx6500TdmtgCardNumber_Type = Integer32
_Cdx6500TdmtgCardNumber_Object = MibTableColumn
cdx6500TdmtgCardNumber = _Cdx6500TdmtgCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 29, 1, 2),
    _Cdx6500TdmtgCardNumber_Type()
)
cdx6500TdmtgCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TdmtgCardNumber.setStatus("mandatory")


class _Cdx6500TdmtgCardClkParticipation_Type(Integer32):
    """Custom type cdx6500TdmtgCardClkParticipation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("system-clock", 2))
    )


_Cdx6500TdmtgCardClkParticipation_Type.__name__ = "Integer32"
_Cdx6500TdmtgCardClkParticipation_Object = MibTableColumn
cdx6500TdmtgCardClkParticipation = _Cdx6500TdmtgCardClkParticipation_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 29, 1, 3),
    _Cdx6500TdmtgCardClkParticipation_Type()
)
cdx6500TdmtgCardClkParticipation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TdmtgCardClkParticipation.setStatus("mandatory")


class _Cdx6500TdmtgGroup1ClkParticipation_Type(Integer32):
    """Custom type cdx6500TdmtgGroup1ClkParticipation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("card-clock", 2),
          ("group-clock", 1))
    )


_Cdx6500TdmtgGroup1ClkParticipation_Type.__name__ = "Integer32"
_Cdx6500TdmtgGroup1ClkParticipation_Object = MibTableColumn
cdx6500TdmtgGroup1ClkParticipation = _Cdx6500TdmtgGroup1ClkParticipation_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 29, 1, 4),
    _Cdx6500TdmtgGroup1ClkParticipation_Type()
)
cdx6500TdmtgGroup1ClkParticipation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TdmtgGroup1ClkParticipation.setStatus("mandatory")


class _Cdx6500TdmtgGroup2ClkParticipation_Type(Integer32):
    """Custom type cdx6500TdmtgGroup2ClkParticipation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("card-clock", 2),
          ("group-clock", 1))
    )


_Cdx6500TdmtgGroup2ClkParticipation_Type.__name__ = "Integer32"
_Cdx6500TdmtgGroup2ClkParticipation_Object = MibTableColumn
cdx6500TdmtgGroup2ClkParticipation = _Cdx6500TdmtgGroup2ClkParticipation_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 29, 1, 5),
    _Cdx6500TdmtgGroup2ClkParticipation_Type()
)
cdx6500TdmtgGroup2ClkParticipation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TdmtgGroup2ClkParticipation.setStatus("mandatory")


class _Cdx6500TdmtgGroup3ClkParticipation_Type(Integer32):
    """Custom type cdx6500TdmtgGroup3ClkParticipation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("card-clock", 2),
          ("group-clock", 1))
    )


_Cdx6500TdmtgGroup3ClkParticipation_Type.__name__ = "Integer32"
_Cdx6500TdmtgGroup3ClkParticipation_Object = MibTableColumn
cdx6500TdmtgGroup3ClkParticipation = _Cdx6500TdmtgGroup3ClkParticipation_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 29, 1, 6),
    _Cdx6500TdmtgGroup3ClkParticipation_Type()
)
cdx6500TdmtgGroup3ClkParticipation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TdmtgGroup3ClkParticipation.setStatus("mandatory")
_Cdx6500Statistics_ObjectIdentity = ObjectIdentity
cdx6500Statistics = _Cdx6500Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3)
)
_Cdx6500StatOtherStatsGroup_ObjectIdentity = ObjectIdentity
cdx6500StatOtherStatsGroup = _Cdx6500StatOtherStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2)
)
_Cdx6500STTdmtgClkGroup_ObjectIdentity = ObjectIdentity
cdx6500STTdmtgClkGroup = _Cdx6500STTdmtgClkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 17)
)


class _Cdx6500TdmtgStatSystemClkStatus_Type(DisplayString):
    """Custom type cdx6500TdmtgStatSystemClkStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cdx6500TdmtgStatSystemClkStatus_Type.__name__ = "DisplayString"
_Cdx6500TdmtgStatSystemClkStatus_Object = MibScalar
cdx6500TdmtgStatSystemClkStatus = _Cdx6500TdmtgStatSystemClkStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 17, 1),
    _Cdx6500TdmtgStatSystemClkStatus_Type()
)
cdx6500TdmtgStatSystemClkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TdmtgStatSystemClkStatus.setStatus("optional")
_Cdx6500TdmtgStatCardClkRegisteredTable_Object = MibTable
cdx6500TdmtgStatCardClkRegisteredTable = _Cdx6500TdmtgStatCardClkRegisteredTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 17, 2)
)
if mibBuilder.loadTexts:
    cdx6500TdmtgStatCardClkRegisteredTable.setStatus("mandatory")
_Cdx6500TdmtgStatClkRegisteredEntry_Object = MibTableRow
cdx6500TdmtgStatClkRegisteredEntry = _Cdx6500TdmtgStatClkRegisteredEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 17, 2, 1)
)
cdx6500TdmtgStatClkRegisteredEntry.setIndexNames(
    (0, "TDMTGCLK-OPT-MIB", "cdx6500TdmtgStatClkRegisteredEntryNumber"),
)
if mibBuilder.loadTexts:
    cdx6500TdmtgStatClkRegisteredEntry.setStatus("mandatory")
_Cdx6500TdmtgStatClkRegisteredEntryNumber_Type = Integer32
_Cdx6500TdmtgStatClkRegisteredEntryNumber_Object = MibTableColumn
cdx6500TdmtgStatClkRegisteredEntryNumber = _Cdx6500TdmtgStatClkRegisteredEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 17, 2, 1, 1),
    _Cdx6500TdmtgStatClkRegisteredEntryNumber_Type()
)
cdx6500TdmtgStatClkRegisteredEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TdmtgStatClkRegisteredEntryNumber.setStatus("mandatory")
_Cdx6500TdmtgStatCardClkRegistered_Type = DisplayString
_Cdx6500TdmtgStatCardClkRegistered_Object = MibTableColumn
cdx6500TdmtgStatCardClkRegistered = _Cdx6500TdmtgStatCardClkRegistered_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 17, 2, 1, 2),
    _Cdx6500TdmtgStatCardClkRegistered_Type()
)
cdx6500TdmtgStatCardClkRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TdmtgStatCardClkRegistered.setStatus("optional")
_Cdx6500TdmtgStatGroupCardClkRegisteredTable_Object = MibTable
cdx6500TdmtgStatGroupCardClkRegisteredTable = _Cdx6500TdmtgStatGroupCardClkRegisteredTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 17, 3)
)
if mibBuilder.loadTexts:
    cdx6500TdmtgStatGroupCardClkRegisteredTable.setStatus("mandatory")
_Cdx6500TdmtgStatGroupClkRegisteredEntry_Object = MibTableRow
cdx6500TdmtgStatGroupClkRegisteredEntry = _Cdx6500TdmtgStatGroupClkRegisteredEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 17, 3, 1)
)
cdx6500TdmtgStatGroupClkRegisteredEntry.setIndexNames(
    (0, "TDMTGCLK-OPT-MIB", "cdx6500TdmtgStatClkEntryNumber"),
    (0, "TDMTGCLK-OPT-MIB", "cdx6500TdmtgStatGroupClkRegisteredEntryNumber"),
)
if mibBuilder.loadTexts:
    cdx6500TdmtgStatGroupClkRegisteredEntry.setStatus("mandatory")
_Cdx6500TdmtgStatClkEntryNumber_Type = Integer32
_Cdx6500TdmtgStatClkEntryNumber_Object = MibTableColumn
cdx6500TdmtgStatClkEntryNumber = _Cdx6500TdmtgStatClkEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 17, 3, 1, 1),
    _Cdx6500TdmtgStatClkEntryNumber_Type()
)
cdx6500TdmtgStatClkEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TdmtgStatClkEntryNumber.setStatus("mandatory")
_Cdx6500TdmtgStatGroupClkRegisteredEntryNumber_Type = Integer32
_Cdx6500TdmtgStatGroupClkRegisteredEntryNumber_Object = MibTableColumn
cdx6500TdmtgStatGroupClkRegisteredEntryNumber = _Cdx6500TdmtgStatGroupClkRegisteredEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 17, 3, 1, 2),
    _Cdx6500TdmtgStatGroupClkRegisteredEntryNumber_Type()
)
cdx6500TdmtgStatGroupClkRegisteredEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TdmtgStatGroupClkRegisteredEntryNumber.setStatus("mandatory")
_Cdx6500TdmtgStatGroupCardClkRegistered_Type = DisplayString
_Cdx6500TdmtgStatGroupCardClkRegistered_Object = MibTableColumn
cdx6500TdmtgStatGroupCardClkRegistered = _Cdx6500TdmtgStatGroupCardClkRegistered_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 17, 3, 1, 3),
    _Cdx6500TdmtgStatGroupCardClkRegistered_Type()
)
cdx6500TdmtgStatGroupCardClkRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TdmtgStatGroupCardClkRegistered.setStatus("optional")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TDMTGCLK-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgGeneralGroup": cdx6500CfgGeneralGroup,
       "cdx6500TdmtgClkTable": cdx6500TdmtgClkTable,
       "cdx6500TdmtgClkCfgEntry": cdx6500TdmtgClkCfgEntry,
       "cdx6500TdmtgClkEntryNumber": cdx6500TdmtgClkEntryNumber,
       "cdx6500TdmtgCardNumber": cdx6500TdmtgCardNumber,
       "cdx6500TdmtgCardClkParticipation": cdx6500TdmtgCardClkParticipation,
       "cdx6500TdmtgGroup1ClkParticipation": cdx6500TdmtgGroup1ClkParticipation,
       "cdx6500TdmtgGroup2ClkParticipation": cdx6500TdmtgGroup2ClkParticipation,
       "cdx6500TdmtgGroup3ClkParticipation": cdx6500TdmtgGroup3ClkParticipation,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatOtherStatsGroup": cdx6500StatOtherStatsGroup,
       "cdx6500STTdmtgClkGroup": cdx6500STTdmtgClkGroup,
       "cdx6500TdmtgStatSystemClkStatus": cdx6500TdmtgStatSystemClkStatus,
       "cdx6500TdmtgStatCardClkRegisteredTable": cdx6500TdmtgStatCardClkRegisteredTable,
       "cdx6500TdmtgStatClkRegisteredEntry": cdx6500TdmtgStatClkRegisteredEntry,
       "cdx6500TdmtgStatClkRegisteredEntryNumber": cdx6500TdmtgStatClkRegisteredEntryNumber,
       "cdx6500TdmtgStatCardClkRegistered": cdx6500TdmtgStatCardClkRegistered,
       "cdx6500TdmtgStatGroupCardClkRegisteredTable": cdx6500TdmtgStatGroupCardClkRegisteredTable,
       "cdx6500TdmtgStatGroupClkRegisteredEntry": cdx6500TdmtgStatGroupClkRegisteredEntry,
       "cdx6500TdmtgStatClkEntryNumber": cdx6500TdmtgStatClkEntryNumber,
       "cdx6500TdmtgStatGroupClkRegisteredEntryNumber": cdx6500TdmtgStatGroupClkRegisteredEntryNumber,
       "cdx6500TdmtgStatGroupCardClkRegistered": cdx6500TdmtgStatGroupCardClkRegistered}
)
