# SNMP MIB module (TDMCLK-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TDMCLK-OPT-MIB
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
_Cdx6500TdmClkTable_Object = MibTable
cdx6500TdmClkTable = _Cdx6500TdmClkTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 24)
)
if mibBuilder.loadTexts:
    cdx6500TdmClkTable.setStatus("mandatory")
_Cdx6500TdmClkCfgEntry_Object = MibTableRow
cdx6500TdmClkCfgEntry = _Cdx6500TdmClkCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 24, 1)
)
cdx6500TdmClkCfgEntry.setIndexNames(
    (0, "TDMCLK-OPT-MIB", "cdx6500TdmClkEntryNumber"),
)
if mibBuilder.loadTexts:
    cdx6500TdmClkCfgEntry.setStatus("mandatory")
_Cdx6500TdmClkEntryNumber_Type = Integer32
_Cdx6500TdmClkEntryNumber_Object = MibTableColumn
cdx6500TdmClkEntryNumber = _Cdx6500TdmClkEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 24, 1, 1),
    _Cdx6500TdmClkEntryNumber_Type()
)
cdx6500TdmClkEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TdmClkEntryNumber.setStatus("mandatory")
_Cdx6500TdmClkPriority_Type = Integer32
_Cdx6500TdmClkPriority_Object = MibTableColumn
cdx6500TdmClkPriority = _Cdx6500TdmClkPriority_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 24, 1, 2),
    _Cdx6500TdmClkPriority_Type()
)
cdx6500TdmClkPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TdmClkPriority.setStatus("mandatory")
_Cdx6500Statistics_ObjectIdentity = ObjectIdentity
cdx6500Statistics = _Cdx6500Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3)
)
_Cdx6500StatOtherStatsGroup_ObjectIdentity = ObjectIdentity
cdx6500StatOtherStatsGroup = _Cdx6500StatOtherStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2)
)
_Cdx6500STTdmClkGroup_ObjectIdentity = ObjectIdentity
cdx6500STTdmClkGroup = _Cdx6500STTdmClkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 13)
)


class _TdmClkStatus_Type(DisplayString):
    """Custom type tdmClkStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TdmClkStatus_Type.__name__ = "DisplayString"
_TdmClkStatus_Object = MibScalar
tdmClkStatus = _TdmClkStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 13, 1),
    _TdmClkStatus_Type()
)
tdmClkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmClkStatus.setStatus("optional")
_TdmClkRegisteredTDMTable_Object = MibTable
tdmClkRegisteredTDMTable = _TdmClkRegisteredTDMTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 13, 2)
)
if mibBuilder.loadTexts:
    tdmClkRegisteredTDMTable.setStatus("mandatory")
_TdmClkRegisteredTDMEntry_Object = MibTableRow
tdmClkRegisteredTDMEntry = _TdmClkRegisteredTDMEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 13, 2, 1)
)
tdmClkRegisteredTDMEntry.setIndexNames(
    (0, "TDMCLK-OPT-MIB", "cdx6500TdmClkEntryNumber"),
)
if mibBuilder.loadTexts:
    tdmClkRegisteredTDMEntry.setStatus("mandatory")
_TdmClkRegisteredTDMEntryNumber_Type = Integer32
_TdmClkRegisteredTDMEntryNumber_Object = MibTableColumn
tdmClkRegisteredTDMEntryNumber = _TdmClkRegisteredTDMEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 13, 2, 1, 1),
    _TdmClkRegisteredTDMEntryNumber_Type()
)
tdmClkRegisteredTDMEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmClkRegisteredTDMEntryNumber.setStatus("mandatory")
_TdmClkRegisteredTDM_Type = DisplayString
_TdmClkRegisteredTDM_Object = MibTableColumn
tdmClkRegisteredTDM = _TdmClkRegisteredTDM_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 13, 2, 1, 2),
    _TdmClkRegisteredTDM_Type()
)
tdmClkRegisteredTDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmClkRegisteredTDM.setStatus("optional")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TDMCLK-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgGeneralGroup": cdx6500CfgGeneralGroup,
       "cdx6500TdmClkTable": cdx6500TdmClkTable,
       "cdx6500TdmClkCfgEntry": cdx6500TdmClkCfgEntry,
       "cdx6500TdmClkEntryNumber": cdx6500TdmClkEntryNumber,
       "cdx6500TdmClkPriority": cdx6500TdmClkPriority,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatOtherStatsGroup": cdx6500StatOtherStatsGroup,
       "cdx6500STTdmClkGroup": cdx6500STTdmClkGroup,
       "tdmClkStatus": tdmClkStatus,
       "tdmClkRegisteredTDMTable": tdmClkRegisteredTDMTable,
       "tdmClkRegisteredTDMEntry": tdmClkRegisteredTDMEntry,
       "tdmClkRegisteredTDMEntryNumber": tdmClkRegisteredTDMEntryNumber,
       "tdmClkRegisteredTDM": tdmClkRegisteredTDM}
)
