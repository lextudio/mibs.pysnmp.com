# SNMP MIB module (ATM-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATM-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:57 2024
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
_Cdx6500PPCTATMPortTable_Object = MibTable
cdx6500PPCTATMPortTable = _Cdx6500PPCTATMPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 35)
)
if mibBuilder.loadTexts:
    cdx6500PPCTATMPortTable.setStatus("mandatory")
_Cdx6500PPCTATMPortEntry_Object = MibTableRow
cdx6500PPCTATMPortEntry = _Cdx6500PPCTATMPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 35, 1)
)
cdx6500PPCTATMPortEntry.setIndexNames(
    (0, "ATM-OPT-MIB", "atmPCfgPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPCTATMPortEntry.setStatus("mandatory")
_AtmPCfgPortNumber_Type = Integer32
_AtmPCfgPortNumber_Object = MibTableColumn
atmPCfgPortNumber = _AtmPCfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 35, 1, 1),
    _AtmPCfgPortNumber_Type()
)
atmPCfgPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPCfgPortNumber.setStatus("mandatory")


class _AtmPCfgPortType_Type(Integer32):
    """Custom type atmPCfgPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            57
        )
    )
    namedValues = NamedValues(
        ("atm", 57)
    )


_AtmPCfgPortType_Type.__name__ = "Integer32"
_AtmPCfgPortType_Object = MibTableColumn
atmPCfgPortType = _AtmPCfgPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 35, 1, 2),
    _AtmPCfgPortType_Type()
)
atmPCfgPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPCfgPortType.setStatus("mandatory")
_AtmPCfgMaxVPIRange_Type = Integer32
_AtmPCfgMaxVPIRange_Object = MibTableColumn
atmPCfgMaxVPIRange = _AtmPCfgMaxVPIRange_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 35, 1, 3),
    _AtmPCfgMaxVPIRange_Type()
)
atmPCfgMaxVPIRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPCfgMaxVPIRange.setStatus("deprecated")
_AtmPCfgMaxVCIRange_Type = Integer32
_AtmPCfgMaxVCIRange_Object = MibTableColumn
atmPCfgMaxVCIRange = _AtmPCfgMaxVCIRange_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 35, 1, 4),
    _AtmPCfgMaxVCIRange_Type()
)
atmPCfgMaxVCIRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPCfgMaxVCIRange.setStatus("deprecated")
_AtmPCfgLinkAssuranceTimer_Type = Integer32
_AtmPCfgLinkAssuranceTimer_Object = MibTableColumn
atmPCfgLinkAssuranceTimer = _AtmPCfgLinkAssuranceTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 35, 1, 5),
    _AtmPCfgLinkAssuranceTimer_Type()
)
atmPCfgLinkAssuranceTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPCfgLinkAssuranceTimer.setStatus("deprecated")
_AtmPCfgLinkAssuranceCount_Type = Integer32
_AtmPCfgLinkAssuranceCount_Object = MibTableColumn
atmPCfgLinkAssuranceCount = _AtmPCfgLinkAssuranceCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 35, 1, 6),
    _AtmPCfgLinkAssuranceCount_Type()
)
atmPCfgLinkAssuranceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPCfgLinkAssuranceCount.setStatus("deprecated")
_AtmPCfgCCActDeactTimer_Type = Integer32
_AtmPCfgCCActDeactTimer_Object = MibTableColumn
atmPCfgCCActDeactTimer = _AtmPCfgCCActDeactTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 35, 1, 7),
    _AtmPCfgCCActDeactTimer_Type()
)
atmPCfgCCActDeactTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPCfgCCActDeactTimer.setStatus("deprecated")
_AtmPCfgCCActDeactCount_Type = Integer32
_AtmPCfgCCActDeactCount_Object = MibTableColumn
atmPCfgCCActDeactCount = _AtmPCfgCCActDeactCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 35, 1, 8),
    _AtmPCfgCCActDeactCount_Type()
)
atmPCfgCCActDeactCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPCfgCCActDeactCount.setStatus("deprecated")


class _AtmPCfgVCCTrafficPrioritization_Type(Integer32):
    """Custom type atmPCfgVCCTrafficPrioritization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("priority", 3),
          ("sequence", 2))
    )


_AtmPCfgVCCTrafficPrioritization_Type.__name__ = "Integer32"
_AtmPCfgVCCTrafficPrioritization_Object = MibTableColumn
atmPCfgVCCTrafficPrioritization = _AtmPCfgVCCTrafficPrioritization_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 35, 1, 9),
    _AtmPCfgVCCTrafficPrioritization_Type()
)
atmPCfgVCCTrafficPrioritization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPCfgVCCTrafficPrioritization.setStatus("mandatory")
_Cdx6500PCTStationProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTStationProtocolGroup = _Cdx6500PCTStationProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3)
)
_Cdx6500SPCTATMStationTable_Object = MibTable
cdx6500SPCTATMStationTable = _Cdx6500SPCTATMStationTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 10)
)
if mibBuilder.loadTexts:
    cdx6500SPCTATMStationTable.setStatus("mandatory")
_Cdx6500SPCTATMStationEntry_Object = MibTableRow
cdx6500SPCTATMStationEntry = _Cdx6500SPCTATMStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 10, 1)
)
cdx6500SPCTATMStationEntry.setIndexNames(
    (0, "ATM-OPT-MIB", "atmSCfgPortNumber"),
    (0, "ATM-OPT-MIB", "atmSCfgStnNumber"),
)
if mibBuilder.loadTexts:
    cdx6500SPCTATMStationEntry.setStatus("mandatory")
_AtmSCfgPortNumber_Type = Integer32
_AtmSCfgPortNumber_Object = MibTableColumn
atmSCfgPortNumber = _AtmSCfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 10, 1, 1),
    _AtmSCfgPortNumber_Type()
)
atmSCfgPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSCfgPortNumber.setStatus("mandatory")
_AtmSCfgStnNumber_Type = Integer32
_AtmSCfgStnNumber_Object = MibTableColumn
atmSCfgStnNumber = _AtmSCfgStnNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 10, 1, 2),
    _AtmSCfgStnNumber_Type()
)
atmSCfgStnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSCfgStnNumber.setStatus("mandatory")
_AtmSCfgVPI_Type = Integer32
_AtmSCfgVPI_Object = MibTableColumn
atmSCfgVPI = _AtmSCfgVPI_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 10, 1, 3),
    _AtmSCfgVPI_Type()
)
atmSCfgVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSCfgVPI.setStatus("mandatory")
_AtmSCfgVCI_Type = Integer32
_AtmSCfgVCI_Object = MibTableColumn
atmSCfgVCI = _AtmSCfgVCI_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 10, 1, 4),
    _AtmSCfgVCI_Type()
)
atmSCfgVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSCfgVCI.setStatus("mandatory")


class _AtmSCfgLinkAssuranceMethod_Type(Integer32):
    """Custom type atmSCfgLinkAssuranceMethod based on Integer32"""
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
        *(("disabled", 1),
          ("enabled", 3),
          ("loopback", 2),
          ("nogotiate", 4))
    )


_AtmSCfgLinkAssuranceMethod_Type.__name__ = "Integer32"
_AtmSCfgLinkAssuranceMethod_Object = MibTableColumn
atmSCfgLinkAssuranceMethod = _AtmSCfgLinkAssuranceMethod_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 10, 1, 5),
    _AtmSCfgLinkAssuranceMethod_Type()
)
atmSCfgLinkAssuranceMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSCfgLinkAssuranceMethod.setStatus("mandatory")


class _AtmSCfgTrafficServiceCategory_Type(Integer32):
    """Custom type atmSCfgTrafficServiceCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 2),
          ("ubr", 1),
          ("vbr", 3))
    )


_AtmSCfgTrafficServiceCategory_Type.__name__ = "Integer32"
_AtmSCfgTrafficServiceCategory_Object = MibTableColumn
atmSCfgTrafficServiceCategory = _AtmSCfgTrafficServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 10, 1, 6),
    _AtmSCfgTrafficServiceCategory_Type()
)
atmSCfgTrafficServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSCfgTrafficServiceCategory.setStatus("mandatory")
_AtmSCfgPeakCellRate_Type = Integer32
_AtmSCfgPeakCellRate_Object = MibTableColumn
atmSCfgPeakCellRate = _AtmSCfgPeakCellRate_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 10, 1, 7),
    _AtmSCfgPeakCellRate_Type()
)
atmSCfgPeakCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSCfgPeakCellRate.setStatus("mandatory")


class _AtmSCfgVBRTrafficShaping_Type(Integer32):
    """Custom type atmSCfgVBRTrafficShaping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dual", 1),
          ("single", 2))
    )


_AtmSCfgVBRTrafficShaping_Type.__name__ = "Integer32"
_AtmSCfgVBRTrafficShaping_Object = MibTableColumn
atmSCfgVBRTrafficShaping = _AtmSCfgVBRTrafficShaping_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 10, 1, 8),
    _AtmSCfgVBRTrafficShaping_Type()
)
atmSCfgVBRTrafficShaping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSCfgVBRTrafficShaping.setStatus("mandatory")


class _AtmSCfgVCCPriorityLevel_Type(Integer32):
    """Custom type atmSCfgVCCPriorityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("normal", 1))
    )


_AtmSCfgVCCPriorityLevel_Type.__name__ = "Integer32"
_AtmSCfgVCCPriorityLevel_Object = MibTableColumn
atmSCfgVCCPriorityLevel = _AtmSCfgVCCPriorityLevel_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 10, 1, 9),
    _AtmSCfgVCCPriorityLevel_Type()
)
atmSCfgVCCPriorityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSCfgVCCPriorityLevel.setStatus("mandatory")


class _AtmSCfgSustainableCellRate_Type(Integer32):
    """Custom type atmSCfgSustainableCellRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 30000),
    )


_AtmSCfgSustainableCellRate_Type.__name__ = "Integer32"
_AtmSCfgSustainableCellRate_Object = MibTableColumn
atmSCfgSustainableCellRate = _AtmSCfgSustainableCellRate_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 10, 1, 10),
    _AtmSCfgSustainableCellRate_Type()
)
atmSCfgSustainableCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSCfgSustainableCellRate.setStatus("deprecated")


class _AtmSCfgMaximumBustSize_Type(Integer32):
    """Custom type atmSCfgMaximumBustSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtmSCfgMaximumBustSize_Type.__name__ = "Integer32"
_AtmSCfgMaximumBustSize_Object = MibTableColumn
atmSCfgMaximumBustSize = _AtmSCfgMaximumBustSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 10, 1, 11),
    _AtmSCfgMaximumBustSize_Type()
)
atmSCfgMaximumBustSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSCfgMaximumBustSize.setStatus("deprecated")
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
_Cdx6500PPSTATMPStatsTable_ObjectIdentity = ObjectIdentity
cdx6500PPSTATMPStatsTable = _Cdx6500PPSTATMPStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 36)
)
_Cdx6500PPSTATMPortTable_Object = MibTable
cdx6500PPSTATMPortTable = _Cdx6500PPSTATMPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 36, 1)
)
if mibBuilder.loadTexts:
    cdx6500PPSTATMPortTable.setStatus("mandatory")
_Cdx6500PPSTATMPortEntry_Object = MibTableRow
cdx6500PPSTATMPortEntry = _Cdx6500PPSTATMPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 36, 1, 1)
)
cdx6500PPSTATMPortEntry.setIndexNames(
    (0, "ATM-OPT-MIB", "atmPStatsPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPSTATMPortEntry.setStatus("mandatory")
_AtmPStatsPortNumber_Type = Integer32
_AtmPStatsPortNumber_Object = MibTableColumn
atmPStatsPortNumber = _AtmPStatsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 36, 1, 1, 1),
    _AtmPStatsPortNumber_Type()
)
atmPStatsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPStatsPortNumber.setStatus("mandatory")


class _AtmPStatsPortType_Type(Integer32):
    """Custom type atmPStatsPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            57
        )
    )
    namedValues = NamedValues(
        ("atm", 57)
    )


_AtmPStatsPortType_Type.__name__ = "Integer32"
_AtmPStatsPortType_Object = MibTableColumn
atmPStatsPortType = _AtmPStatsPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 36, 1, 1, 2),
    _AtmPStatsPortType_Type()
)
atmPStatsPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPStatsPortType.setStatus("mandatory")
_AtmPStatsPortStatus_Type = DisplayString
_AtmPStatsPortStatus_Object = MibTableColumn
atmPStatsPortStatus = _AtmPStatsPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 36, 1, 1, 3),
    _AtmPStatsPortStatus_Type()
)
atmPStatsPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPStatsPortStatus.setStatus("mandatory")
_Cdx6500PPSTATMDataSummaryTable_Object = MibTable
cdx6500PPSTATMDataSummaryTable = _Cdx6500PPSTATMDataSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 36, 2)
)
if mibBuilder.loadTexts:
    cdx6500PPSTATMDataSummaryTable.setStatus("mandatory")
_Cdx6500PPSTATMDataSummaryEntry_Object = MibTableRow
cdx6500PPSTATMDataSummaryEntry = _Cdx6500PPSTATMDataSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 36, 2, 1)
)
cdx6500PPSTATMDataSummaryEntry.setIndexNames(
    (0, "ATM-OPT-MIB", "atmDataSummPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPSTATMDataSummaryEntry.setStatus("mandatory")
_AtmDataSummPortNumber_Type = Integer32
_AtmDataSummPortNumber_Object = MibTableColumn
atmDataSummPortNumber = _AtmDataSummPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 36, 2, 1, 1),
    _AtmDataSummPortNumber_Type()
)
atmDataSummPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDataSummPortNumber.setStatus("mandatory")
_AtmPStatsOctetsInTotal_Type = Counter32
_AtmPStatsOctetsInTotal_Object = MibTableColumn
atmPStatsOctetsInTotal = _AtmPStatsOctetsInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 36, 2, 1, 2),
    _AtmPStatsOctetsInTotal_Type()
)
atmPStatsOctetsInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPStatsOctetsInTotal.setStatus("mandatory")
_AtmPStatsOctetsOutTotal_Type = Counter32
_AtmPStatsOctetsOutTotal_Object = MibTableColumn
atmPStatsOctetsOutTotal = _AtmPStatsOctetsOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 36, 2, 1, 3),
    _AtmPStatsOctetsOutTotal_Type()
)
atmPStatsOctetsOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPStatsOctetsOutTotal.setStatus("mandatory")
_AtmPStatsOctetsInPerSec_Type = Integer32
_AtmPStatsOctetsInPerSec_Object = MibTableColumn
atmPStatsOctetsInPerSec = _AtmPStatsOctetsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 36, 2, 1, 4),
    _AtmPStatsOctetsInPerSec_Type()
)
atmPStatsOctetsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPStatsOctetsInPerSec.setStatus("mandatory")
_AtmPStatsOctetsOutPerSec_Type = Integer32
_AtmPStatsOctetsOutPerSec_Object = MibTableColumn
atmPStatsOctetsOutPerSec = _AtmPStatsOctetsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 36, 2, 1, 5),
    _AtmPStatsOctetsOutPerSec_Type()
)
atmPStatsOctetsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPStatsOctetsOutPerSec.setStatus("mandatory")
_AtmPStatsFramesInTotal_Type = Counter32
_AtmPStatsFramesInTotal_Object = MibTableColumn
atmPStatsFramesInTotal = _AtmPStatsFramesInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 36, 2, 1, 6),
    _AtmPStatsFramesInTotal_Type()
)
atmPStatsFramesInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPStatsFramesInTotal.setStatus("mandatory")
_AtmPStatsFramesOutTotal_Type = Counter32
_AtmPStatsFramesOutTotal_Object = MibTableColumn
atmPStatsFramesOutTotal = _AtmPStatsFramesOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 36, 2, 1, 7),
    _AtmPStatsFramesOutTotal_Type()
)
atmPStatsFramesOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPStatsFramesOutTotal.setStatus("mandatory")
_AtmPStatsFramesInPerSec_Type = Integer32
_AtmPStatsFramesInPerSec_Object = MibTableColumn
atmPStatsFramesInPerSec = _AtmPStatsFramesInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 36, 2, 1, 8),
    _AtmPStatsFramesInPerSec_Type()
)
atmPStatsFramesInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPStatsFramesInPerSec.setStatus("mandatory")
_AtmPStatsFramesOutPerSec_Type = Integer32
_AtmPStatsFramesOutPerSec_Object = MibTableColumn
atmPStatsFramesOutPerSec = _AtmPStatsFramesOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 36, 2, 1, 9),
    _AtmPStatsFramesOutPerSec_Type()
)
atmPStatsFramesOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPStatsFramesOutPerSec.setStatus("mandatory")
_AtmPStatsOAMCellInTotal_Type = Counter32
_AtmPStatsOAMCellInTotal_Object = MibTableColumn
atmPStatsOAMCellInTotal = _AtmPStatsOAMCellInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 36, 2, 1, 10),
    _AtmPStatsOAMCellInTotal_Type()
)
atmPStatsOAMCellInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPStatsOAMCellInTotal.setStatus("mandatory")
_AtmPStatsOAMCellOutTotal_Type = Counter32
_AtmPStatsOAMCellOutTotal_Object = MibTableColumn
atmPStatsOAMCellOutTotal = _AtmPStatsOAMCellOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 36, 2, 1, 11),
    _AtmPStatsOAMCellOutTotal_Type()
)
atmPStatsOAMCellOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPStatsOAMCellOutTotal.setStatus("mandatory")
_AtmPStatsATMCellInTotal_Type = Counter32
_AtmPStatsATMCellInTotal_Object = MibTableColumn
atmPStatsATMCellInTotal = _AtmPStatsATMCellInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 36, 2, 1, 12),
    _AtmPStatsATMCellInTotal_Type()
)
atmPStatsATMCellInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPStatsATMCellInTotal.setStatus("mandatory")
_AtmPStatsATMCellOutTotal_Type = Counter32
_AtmPStatsATMCellOutTotal_Object = MibTableColumn
atmPStatsATMCellOutTotal = _AtmPStatsATMCellOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 36, 2, 1, 13),
    _AtmPStatsATMCellOutTotal_Type()
)
atmPStatsATMCellOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPStatsATMCellOutTotal.setStatus("mandatory")
_AtmPStatsErrorCellCor_Type = Integer32
_AtmPStatsErrorCellCor_Object = MibTableColumn
atmPStatsErrorCellCor = _AtmPStatsErrorCellCor_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 36, 2, 1, 14),
    _AtmPStatsErrorCellCor_Type()
)
atmPStatsErrorCellCor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPStatsErrorCellCor.setStatus("mandatory")
_AtmPStatsErrorCellDis_Type = Integer32
_AtmPStatsErrorCellDis_Object = MibTableColumn
atmPStatsErrorCellDis = _AtmPStatsErrorCellDis_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 36, 2, 1, 15),
    _AtmPStatsErrorCellDis_Type()
)
atmPStatsErrorCellDis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPStatsErrorCellDis.setStatus("mandatory")
_AtmPStatsCellDelineateState_Type = DisplayString
_AtmPStatsCellDelineateState_Object = MibTableColumn
atmPStatsCellDelineateState = _AtmPStatsCellDelineateState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 36, 2, 1, 16),
    _AtmPStatsCellDelineateState_Type()
)
atmPStatsCellDelineateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPStatsCellDelineateState.setStatus("mandatory")
_AtmPStatsCellStateChangeTime_Type = DisplayString
_AtmPStatsCellStateChangeTime_Object = MibTableColumn
atmPStatsCellStateChangeTime = _AtmPStatsCellStateChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 36, 2, 1, 17),
    _AtmPStatsCellStateChangeTime_Type()
)
atmPStatsCellStateChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPStatsCellStateChangeTime.setStatus("mandatory")
_AtmPStatsDiscardedFrames_Type = Counter32
_AtmPStatsDiscardedFrames_Object = MibTableColumn
atmPStatsDiscardedFrames = _AtmPStatsDiscardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 36, 2, 1, 18),
    _AtmPStatsDiscardedFrames_Type()
)
atmPStatsDiscardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPStatsDiscardedFrames.setStatus("mandatory")
_Cdx6500PSTStationProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTStationProtocolGroup = _Cdx6500PSTStationProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3)
)
_Cdx6500SPSTATMSStatsTable_ObjectIdentity = ObjectIdentity
cdx6500SPSTATMSStatsTable = _Cdx6500SPSTATMSStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11)
)
_AtmSGenStatsTable_Object = MibTable
atmSGenStatsTable = _AtmSGenStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 1)
)
if mibBuilder.loadTexts:
    atmSGenStatsTable.setStatus("mandatory")
_Cdx6500atmSGenStatsEntry_Object = MibTableRow
cdx6500atmSGenStatsEntry = _Cdx6500atmSGenStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 1, 1)
)
cdx6500atmSGenStatsEntry.setIndexNames(
    (0, "ATM-OPT-MIB", "atmSGenStatsPortNumber"),
    (0, "ATM-OPT-MIB", "atmSGenStatsStnNumber"),
)
if mibBuilder.loadTexts:
    cdx6500atmSGenStatsEntry.setStatus("mandatory")
_AtmSGenStatsPortNumber_Type = Integer32
_AtmSGenStatsPortNumber_Object = MibTableColumn
atmSGenStatsPortNumber = _AtmSGenStatsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 1, 1, 1),
    _AtmSGenStatsPortNumber_Type()
)
atmSGenStatsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSGenStatsPortNumber.setStatus("mandatory")
_AtmSGenStatsStnNumber_Type = Integer32
_AtmSGenStatsStnNumber_Object = MibTableColumn
atmSGenStatsStnNumber = _AtmSGenStatsStnNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 1, 1, 2),
    _AtmSGenStatsStnNumber_Type()
)
atmSGenStatsStnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSGenStatsStnNumber.setStatus("mandatory")
_AtmSStatsStnStatus_Type = DisplayString
_AtmSStatsStnStatus_Object = MibTableColumn
atmSStatsStnStatus = _AtmSStatsStnStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 1, 1, 3),
    _AtmSStatsStnStatus_Type()
)
atmSStatsStnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSStatsStnStatus.setStatus("mandatory")
_AtmSStatsVPI_Type = Integer32
_AtmSStatsVPI_Object = MibTableColumn
atmSStatsVPI = _AtmSStatsVPI_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 1, 1, 4),
    _AtmSStatsVPI_Type()
)
atmSStatsVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSStatsVPI.setStatus("mandatory")
_AtmSStatsVCI_Type = Integer32
_AtmSStatsVCI_Object = MibTableColumn
atmSStatsVCI = _AtmSStatsVCI_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 1, 1, 5),
    _AtmSStatsVCI_Type()
)
atmSStatsVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSStatsVCI.setStatus("mandatory")


class _AtmSStatsAdmState_Type(Integer32):
    """Custom type atmSStatsAdmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AtmSStatsAdmState_Type.__name__ = "Integer32"
_AtmSStatsAdmState_Object = MibTableColumn
atmSStatsAdmState = _AtmSStatsAdmState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 1, 1, 6),
    _AtmSStatsAdmState_Type()
)
atmSStatsAdmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSStatsAdmState.setStatus("mandatory")
_AtmSStatsPeer_Type = Integer32
_AtmSStatsPeer_Object = MibTableColumn
atmSStatsPeer = _AtmSStatsPeer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 1, 1, 7),
    _AtmSStatsPeer_Type()
)
atmSStatsPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSStatsPeer.setStatus("mandatory")
_AtmSStatsAdjacent_Type = Integer32
_AtmSStatsAdjacent_Object = MibTableColumn
atmSStatsAdjacent = _AtmSStatsAdjacent_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 1, 1, 8),
    _AtmSStatsAdjacent_Type()
)
atmSStatsAdjacent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSStatsAdjacent.setStatus("mandatory")
_AtmSDataSummaryStatsTable_Object = MibTable
atmSDataSummaryStatsTable = _AtmSDataSummaryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 2)
)
if mibBuilder.loadTexts:
    atmSDataSummaryStatsTable.setStatus("mandatory")
_Cdx6500atmSDataSummaryStatsEntry_Object = MibTableRow
cdx6500atmSDataSummaryStatsEntry = _Cdx6500atmSDataSummaryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 2, 1)
)
cdx6500atmSDataSummaryStatsEntry.setIndexNames(
    (0, "ATM-OPT-MIB", "atmSDataSummStatsPortNumber"),
    (0, "ATM-OPT-MIB", "atmSDataSummStatsStnNumber"),
)
if mibBuilder.loadTexts:
    cdx6500atmSDataSummaryStatsEntry.setStatus("mandatory")
_AtmSDataSummStatsPortNumber_Type = Integer32
_AtmSDataSummStatsPortNumber_Object = MibTableColumn
atmSDataSummStatsPortNumber = _AtmSDataSummStatsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 2, 1, 1),
    _AtmSDataSummStatsPortNumber_Type()
)
atmSDataSummStatsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSDataSummStatsPortNumber.setStatus("mandatory")
_AtmSDataSummStatsStnNumber_Type = Integer32
_AtmSDataSummStatsStnNumber_Object = MibTableColumn
atmSDataSummStatsStnNumber = _AtmSDataSummStatsStnNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 2, 1, 2),
    _AtmSDataSummStatsStnNumber_Type()
)
atmSDataSummStatsStnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSDataSummStatsStnNumber.setStatus("mandatory")
_AtmSStatsOctetsInTotal_Type = Counter32
_AtmSStatsOctetsInTotal_Object = MibTableColumn
atmSStatsOctetsInTotal = _AtmSStatsOctetsInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 2, 1, 3),
    _AtmSStatsOctetsInTotal_Type()
)
atmSStatsOctetsInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSStatsOctetsInTotal.setStatus("mandatory")
_AtmSStatsOctetsOutTotal_Type = Counter32
_AtmSStatsOctetsOutTotal_Object = MibTableColumn
atmSStatsOctetsOutTotal = _AtmSStatsOctetsOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 2, 1, 4),
    _AtmSStatsOctetsOutTotal_Type()
)
atmSStatsOctetsOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSStatsOctetsOutTotal.setStatus("mandatory")
_AtmSStatsFrameInTotal_Type = Counter32
_AtmSStatsFrameInTotal_Object = MibTableColumn
atmSStatsFrameInTotal = _AtmSStatsFrameInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 2, 1, 5),
    _AtmSStatsFrameInTotal_Type()
)
atmSStatsFrameInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSStatsFrameInTotal.setStatus("mandatory")
_AtmSStatsFrameOutTotal_Type = Counter32
_AtmSStatsFrameOutTotal_Object = MibTableColumn
atmSStatsFrameOutTotal = _AtmSStatsFrameOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 2, 1, 6),
    _AtmSStatsFrameOutTotal_Type()
)
atmSStatsFrameOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSStatsFrameOutTotal.setStatus("mandatory")
_AtmSStatsF5CellInTotal_Type = Counter32
_AtmSStatsF5CellInTotal_Object = MibTableColumn
atmSStatsF5CellInTotal = _AtmSStatsF5CellInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 2, 1, 7),
    _AtmSStatsF5CellInTotal_Type()
)
atmSStatsF5CellInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSStatsF5CellInTotal.setStatus("mandatory")
_AtmSStatsF5CellOutTotal_Type = Counter32
_AtmSStatsF5CellOutTotal_Object = MibTableColumn
atmSStatsF5CellOutTotal = _AtmSStatsF5CellOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 2, 1, 8),
    _AtmSStatsF5CellOutTotal_Type()
)
atmSStatsF5CellOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSStatsF5CellOutTotal.setStatus("mandatory")
_AtmSStatsAISCellInTotal_Type = Counter32
_AtmSStatsAISCellInTotal_Object = MibTableColumn
atmSStatsAISCellInTotal = _AtmSStatsAISCellInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 2, 1, 9),
    _AtmSStatsAISCellInTotal_Type()
)
atmSStatsAISCellInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSStatsAISCellInTotal.setStatus("mandatory")
_AtmSStatsRDICellInTotal_Type = Counter32
_AtmSStatsRDICellInTotal_Object = MibTableColumn
atmSStatsRDICellInTotal = _AtmSStatsRDICellInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 2, 1, 10),
    _AtmSStatsRDICellInTotal_Type()
)
atmSStatsRDICellInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSStatsRDICellInTotal.setStatus("mandatory")
_AtmSStatsRDICellOutTotal_Type = Counter32
_AtmSStatsRDICellOutTotal_Object = MibTableColumn
atmSStatsRDICellOutTotal = _AtmSStatsRDICellOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 2, 1, 11),
    _AtmSStatsRDICellOutTotal_Type()
)
atmSStatsRDICellOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSStatsRDICellOutTotal.setStatus("mandatory")
_AtmSStatsCCCellInTotal_Type = Counter32
_AtmSStatsCCCellInTotal_Object = MibTableColumn
atmSStatsCCCellInTotal = _AtmSStatsCCCellInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 2, 1, 12),
    _AtmSStatsCCCellInTotal_Type()
)
atmSStatsCCCellInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSStatsCCCellInTotal.setStatus("mandatory")
_AtmSStatsCCCellOutTotal_Type = Counter32
_AtmSStatsCCCellOutTotal_Object = MibTableColumn
atmSStatsCCCellOutTotal = _AtmSStatsCCCellOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 2, 1, 13),
    _AtmSStatsCCCellOutTotal_Type()
)
atmSStatsCCCellOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSStatsCCCellOutTotal.setStatus("mandatory")
_AtmSStatsVCFailure_Type = Integer32
_AtmSStatsVCFailure_Object = MibTableColumn
atmSStatsVCFailure = _AtmSStatsVCFailure_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 2, 1, 14),
    _AtmSStatsVCFailure_Type()
)
atmSStatsVCFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSStatsVCFailure.setStatus("mandatory")
_AtmSStatsVCAssuranceState_Type = DisplayString
_AtmSStatsVCAssuranceState_Object = MibTableColumn
atmSStatsVCAssuranceState = _AtmSStatsVCAssuranceState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 2, 1, 15),
    _AtmSStatsVCAssuranceState_Type()
)
atmSStatsVCAssuranceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSStatsVCAssuranceState.setStatus("mandatory")
_AtmSStatsOctetsInPerSec_Type = Counter32
_AtmSStatsOctetsInPerSec_Object = MibTableColumn
atmSStatsOctetsInPerSec = _AtmSStatsOctetsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 2, 1, 16),
    _AtmSStatsOctetsInPerSec_Type()
)
atmSStatsOctetsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSStatsOctetsInPerSec.setStatus("mandatory")
_AtmSStatsOctetsOutPerSec_Type = Counter32
_AtmSStatsOctetsOutPerSec_Object = MibTableColumn
atmSStatsOctetsOutPerSec = _AtmSStatsOctetsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 2, 1, 17),
    _AtmSStatsOctetsOutPerSec_Type()
)
atmSStatsOctetsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSStatsOctetsOutPerSec.setStatus("mandatory")
_AtmSStatsFramesInPerSec_Type = Counter32
_AtmSStatsFramesInPerSec_Object = MibTableColumn
atmSStatsFramesInPerSec = _AtmSStatsFramesInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 2, 1, 18),
    _AtmSStatsFramesInPerSec_Type()
)
atmSStatsFramesInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSStatsFramesInPerSec.setStatus("mandatory")
_AtmSStatsFramesOutPerSec_Type = Counter32
_AtmSStatsFramesOutPerSec_Object = MibTableColumn
atmSStatsFramesOutPerSec = _AtmSStatsFramesOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 2, 1, 19),
    _AtmSStatsFramesOutPerSec_Type()
)
atmSStatsFramesOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSStatsFramesOutPerSec.setStatus("mandatory")
_AtmSStatsDiscardedFrames_Type = Counter32
_AtmSStatsDiscardedFrames_Object = MibTableColumn
atmSStatsDiscardedFrames = _AtmSStatsDiscardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 2, 1, 20),
    _AtmSStatsDiscardedFrames_Type()
)
atmSStatsDiscardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSStatsDiscardedFrames.setStatus("mandatory")
_AtmSStatsCIBitInForIWF_Type = Counter32
_AtmSStatsCIBitInForIWF_Object = MibTableColumn
atmSStatsCIBitInForIWF = _AtmSStatsCIBitInForIWF_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 2, 1, 21),
    _AtmSStatsCIBitInForIWF_Type()
)
atmSStatsCIBitInForIWF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSStatsCIBitInForIWF.setStatus("mandatory")
_AtmSStatsCIBitOutForIWF_Type = Counter32
_AtmSStatsCIBitOutForIWF_Object = MibTableColumn
atmSStatsCIBitOutForIWF = _AtmSStatsCIBitOutForIWF_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 2, 1, 22),
    _AtmSStatsCIBitOutForIWF_Type()
)
atmSStatsCIBitOutForIWF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSStatsCIBitOutForIWF.setStatus("mandatory")
_AtmSStatsCLPBitInForIWF_Type = Counter32
_AtmSStatsCLPBitInForIWF_Object = MibTableColumn
atmSStatsCLPBitInForIWF = _AtmSStatsCLPBitInForIWF_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 2, 1, 23),
    _AtmSStatsCLPBitInForIWF_Type()
)
atmSStatsCLPBitInForIWF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSStatsCLPBitInForIWF.setStatus("mandatory")
_AtmSStatsCLPBitOutForIWF_Type = Counter32
_AtmSStatsCLPBitOutForIWF_Object = MibTableColumn
atmSStatsCLPBitOutForIWF = _AtmSStatsCLPBitOutForIWF_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 2, 1, 24),
    _AtmSStatsCLPBitOutForIWF_Type()
)
atmSStatsCLPBitOutForIWF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSStatsCLPBitOutForIWF.setStatus("mandatory")
_AtmSStatsUUBitInForIWF_Type = Counter32
_AtmSStatsUUBitInForIWF_Object = MibTableColumn
atmSStatsUUBitInForIWF = _AtmSStatsUUBitInForIWF_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 2, 1, 25),
    _AtmSStatsUUBitInForIWF_Type()
)
atmSStatsUUBitInForIWF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSStatsUUBitInForIWF.setStatus("mandatory")
_AtmSStatsUUBitOutForIWF_Type = Counter32
_AtmSStatsUUBitOutForIWF_Object = MibTableColumn
atmSStatsUUBitOutForIWF = _AtmSStatsUUBitOutForIWF_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 11, 2, 1, 26),
    _AtmSStatsUUBitOutForIWF_Type()
)
atmSStatsUUBitOutForIWF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSStatsUUBitOutForIWF.setStatus("mandatory")
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)
_Cdx6500ContATMTable_ObjectIdentity = ObjectIdentity
cdx6500ContATMTable = _Cdx6500ContATMTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 24)
)
_Cdx6500ATMPContTable_Object = MibTable
cdx6500ATMPContTable = _Cdx6500ATMPContTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 24, 1)
)
if mibBuilder.loadTexts:
    cdx6500ATMPContTable.setStatus("mandatory")
_Cdx6500ATMPContEntry_Object = MibTableRow
cdx6500ATMPContEntry = _Cdx6500ATMPContEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 24, 1, 1)
)
cdx6500ATMPContEntry.setIndexNames(
    (0, "ATM-OPT-MIB", "atmPContPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500ATMPContEntry.setStatus("mandatory")
_AtmPContPortNumber_Type = Integer32
_AtmPContPortNumber_Object = MibTableColumn
atmPContPortNumber = _AtmPContPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 24, 1, 1, 1),
    _AtmPContPortNumber_Type()
)
atmPContPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmPContPortNumber.setStatus("mandatory")


class _AtmPContPortControl_Type(Integer32):
    """Custom type atmPContPortControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boot", 1),
          ("resetstats", 2))
    )


_AtmPContPortControl_Type.__name__ = "Integer32"
_AtmPContPortControl_Object = MibTableColumn
atmPContPortControl = _AtmPContPortControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 24, 1, 1, 2),
    _AtmPContPortControl_Type()
)
atmPContPortControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    atmPContPortControl.setStatus("mandatory")
_Cdx6500ATMSContTable_Object = MibTable
cdx6500ATMSContTable = _Cdx6500ATMSContTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 24, 2)
)
if mibBuilder.loadTexts:
    cdx6500ATMSContTable.setStatus("mandatory")
_Cdx6500ATMSContEntry_Object = MibTableRow
cdx6500ATMSContEntry = _Cdx6500ATMSContEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 24, 2, 1)
)
cdx6500ATMSContEntry.setIndexNames(
    (0, "ATM-OPT-MIB", "atmSContPortNumber"),
    (0, "ATM-OPT-MIB", "atmSContStnNumber"),
)
if mibBuilder.loadTexts:
    cdx6500ATMSContEntry.setStatus("mandatory")


class _AtmSContPortNumber_Type(Integer32):
    """Custom type atmSContPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AtmSContPortNumber_Type.__name__ = "Integer32"
_AtmSContPortNumber_Object = MibTableColumn
atmSContPortNumber = _AtmSContPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 24, 2, 1, 1),
    _AtmSContPortNumber_Type()
)
atmSContPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmSContPortNumber.setStatus("mandatory")


class _AtmSContStnNumber_Type(Integer32):
    """Custom type atmSContStnNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_AtmSContStnNumber_Type.__name__ = "Integer32"
_AtmSContStnNumber_Object = MibTableColumn
atmSContStnNumber = _AtmSContStnNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 24, 2, 1, 2),
    _AtmSContStnNumber_Type()
)
atmSContStnNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmSContStnNumber.setStatus("mandatory")


class _AtmSContStnControl_Type(Integer32):
    """Custom type atmSContStnControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boot", 1),
          ("resetstats", 2))
    )


_AtmSContStnControl_Type.__name__ = "Integer32"
_AtmSContStnControl_Object = MibTableColumn
atmSContStnControl = _AtmSContStnControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 24, 2, 1, 3),
    _AtmSContStnControl_Type()
)
atmSContStnControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    atmSContStnControl.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATM-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PPCTATMPortTable": cdx6500PPCTATMPortTable,
       "cdx6500PPCTATMPortEntry": cdx6500PPCTATMPortEntry,
       "atmPCfgPortNumber": atmPCfgPortNumber,
       "atmPCfgPortType": atmPCfgPortType,
       "atmPCfgMaxVPIRange": atmPCfgMaxVPIRange,
       "atmPCfgMaxVCIRange": atmPCfgMaxVCIRange,
       "atmPCfgLinkAssuranceTimer": atmPCfgLinkAssuranceTimer,
       "atmPCfgLinkAssuranceCount": atmPCfgLinkAssuranceCount,
       "atmPCfgCCActDeactTimer": atmPCfgCCActDeactTimer,
       "atmPCfgCCActDeactCount": atmPCfgCCActDeactCount,
       "atmPCfgVCCTrafficPrioritization": atmPCfgVCCTrafficPrioritization,
       "cdx6500PCTStationProtocolGroup": cdx6500PCTStationProtocolGroup,
       "cdx6500SPCTATMStationTable": cdx6500SPCTATMStationTable,
       "cdx6500SPCTATMStationEntry": cdx6500SPCTATMStationEntry,
       "atmSCfgPortNumber": atmSCfgPortNumber,
       "atmSCfgStnNumber": atmSCfgStnNumber,
       "atmSCfgVPI": atmSCfgVPI,
       "atmSCfgVCI": atmSCfgVCI,
       "atmSCfgLinkAssuranceMethod": atmSCfgLinkAssuranceMethod,
       "atmSCfgTrafficServiceCategory": atmSCfgTrafficServiceCategory,
       "atmSCfgPeakCellRate": atmSCfgPeakCellRate,
       "atmSCfgVBRTrafficShaping": atmSCfgVBRTrafficShaping,
       "atmSCfgVCCPriorityLevel": atmSCfgVCCPriorityLevel,
       "atmSCfgSustainableCellRate": atmSCfgSustainableCellRate,
       "atmSCfgMaximumBustSize": atmSCfgMaximumBustSize,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PPSTATMPStatsTable": cdx6500PPSTATMPStatsTable,
       "cdx6500PPSTATMPortTable": cdx6500PPSTATMPortTable,
       "cdx6500PPSTATMPortEntry": cdx6500PPSTATMPortEntry,
       "atmPStatsPortNumber": atmPStatsPortNumber,
       "atmPStatsPortType": atmPStatsPortType,
       "atmPStatsPortStatus": atmPStatsPortStatus,
       "cdx6500PPSTATMDataSummaryTable": cdx6500PPSTATMDataSummaryTable,
       "cdx6500PPSTATMDataSummaryEntry": cdx6500PPSTATMDataSummaryEntry,
       "atmDataSummPortNumber": atmDataSummPortNumber,
       "atmPStatsOctetsInTotal": atmPStatsOctetsInTotal,
       "atmPStatsOctetsOutTotal": atmPStatsOctetsOutTotal,
       "atmPStatsOctetsInPerSec": atmPStatsOctetsInPerSec,
       "atmPStatsOctetsOutPerSec": atmPStatsOctetsOutPerSec,
       "atmPStatsFramesInTotal": atmPStatsFramesInTotal,
       "atmPStatsFramesOutTotal": atmPStatsFramesOutTotal,
       "atmPStatsFramesInPerSec": atmPStatsFramesInPerSec,
       "atmPStatsFramesOutPerSec": atmPStatsFramesOutPerSec,
       "atmPStatsOAMCellInTotal": atmPStatsOAMCellInTotal,
       "atmPStatsOAMCellOutTotal": atmPStatsOAMCellOutTotal,
       "atmPStatsATMCellInTotal": atmPStatsATMCellInTotal,
       "atmPStatsATMCellOutTotal": atmPStatsATMCellOutTotal,
       "atmPStatsErrorCellCor": atmPStatsErrorCellCor,
       "atmPStatsErrorCellDis": atmPStatsErrorCellDis,
       "atmPStatsCellDelineateState": atmPStatsCellDelineateState,
       "atmPStatsCellStateChangeTime": atmPStatsCellStateChangeTime,
       "atmPStatsDiscardedFrames": atmPStatsDiscardedFrames,
       "cdx6500PSTStationProtocolGroup": cdx6500PSTStationProtocolGroup,
       "cdx6500SPSTATMSStatsTable": cdx6500SPSTATMSStatsTable,
       "atmSGenStatsTable": atmSGenStatsTable,
       "cdx6500atmSGenStatsEntry": cdx6500atmSGenStatsEntry,
       "atmSGenStatsPortNumber": atmSGenStatsPortNumber,
       "atmSGenStatsStnNumber": atmSGenStatsStnNumber,
       "atmSStatsStnStatus": atmSStatsStnStatus,
       "atmSStatsVPI": atmSStatsVPI,
       "atmSStatsVCI": atmSStatsVCI,
       "atmSStatsAdmState": atmSStatsAdmState,
       "atmSStatsPeer": atmSStatsPeer,
       "atmSStatsAdjacent": atmSStatsAdjacent,
       "atmSDataSummaryStatsTable": atmSDataSummaryStatsTable,
       "cdx6500atmSDataSummaryStatsEntry": cdx6500atmSDataSummaryStatsEntry,
       "atmSDataSummStatsPortNumber": atmSDataSummStatsPortNumber,
       "atmSDataSummStatsStnNumber": atmSDataSummStatsStnNumber,
       "atmSStatsOctetsInTotal": atmSStatsOctetsInTotal,
       "atmSStatsOctetsOutTotal": atmSStatsOctetsOutTotal,
       "atmSStatsFrameInTotal": atmSStatsFrameInTotal,
       "atmSStatsFrameOutTotal": atmSStatsFrameOutTotal,
       "atmSStatsF5CellInTotal": atmSStatsF5CellInTotal,
       "atmSStatsF5CellOutTotal": atmSStatsF5CellOutTotal,
       "atmSStatsAISCellInTotal": atmSStatsAISCellInTotal,
       "atmSStatsRDICellInTotal": atmSStatsRDICellInTotal,
       "atmSStatsRDICellOutTotal": atmSStatsRDICellOutTotal,
       "atmSStatsCCCellInTotal": atmSStatsCCCellInTotal,
       "atmSStatsCCCellOutTotal": atmSStatsCCCellOutTotal,
       "atmSStatsVCFailure": atmSStatsVCFailure,
       "atmSStatsVCAssuranceState": atmSStatsVCAssuranceState,
       "atmSStatsOctetsInPerSec": atmSStatsOctetsInPerSec,
       "atmSStatsOctetsOutPerSec": atmSStatsOctetsOutPerSec,
       "atmSStatsFramesInPerSec": atmSStatsFramesInPerSec,
       "atmSStatsFramesOutPerSec": atmSStatsFramesOutPerSec,
       "atmSStatsDiscardedFrames": atmSStatsDiscardedFrames,
       "atmSStatsCIBitInForIWF": atmSStatsCIBitInForIWF,
       "atmSStatsCIBitOutForIWF": atmSStatsCIBitOutForIWF,
       "atmSStatsCLPBitInForIWF": atmSStatsCLPBitInForIWF,
       "atmSStatsCLPBitOutForIWF": atmSStatsCLPBitOutForIWF,
       "atmSStatsUUBitInForIWF": atmSStatsUUBitInForIWF,
       "atmSStatsUUBitOutForIWF": atmSStatsUUBitOutForIWF,
       "cdx6500Controls": cdx6500Controls,
       "cdx6500ContATMTable": cdx6500ContATMTable,
       "cdx6500ATMPContTable": cdx6500ATMPContTable,
       "cdx6500ATMPContEntry": cdx6500ATMPContEntry,
       "atmPContPortNumber": atmPContPortNumber,
       "atmPContPortControl": atmPContPortControl,
       "cdx6500ATMSContTable": cdx6500ATMSContTable,
       "cdx6500ATMSContEntry": cdx6500ATMSContEntry,
       "atmSContPortNumber": atmSContPortNumber,
       "atmSContStnNumber": atmSContStnNumber,
       "atmSContStnControl": atmSContStnControl}
)
