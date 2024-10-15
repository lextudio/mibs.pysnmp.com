# SNMP MIB module (ISO3201-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ISO3201-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:58 2024
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
_Cdx6500PPCT3201PortTable_Object = MibTable
cdx6500PPCT3201PortTable = _Cdx6500PPCT3201PortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 28)
)
if mibBuilder.loadTexts:
    cdx6500PPCT3201PortTable.setStatus("mandatory")
_Cdx6500PPCT3201PortEntry_Object = MibTableRow
cdx6500PPCT3201PortEntry = _Cdx6500PPCT3201PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 28, 1)
)
cdx6500PPCT3201PortEntry.setIndexNames(
    (0, "ISO3201-OPT-MIB", "iso3201PCfgPortNum"),
)
if mibBuilder.loadTexts:
    cdx6500PPCT3201PortEntry.setStatus("mandatory")


class _Iso3201PCfgPortNum_Type(Integer32):
    """Custom type iso3201PCfgPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Iso3201PCfgPortNum_Type.__name__ = "Integer32"
_Iso3201PCfgPortNum_Object = MibTableColumn
iso3201PCfgPortNum = _Iso3201PCfgPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 28, 1, 1),
    _Iso3201PCfgPortNum_Type()
)
iso3201PCfgPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PCfgPortNum.setStatus("mandatory")


class _Iso3201PCfgPortType_Type(Integer32):
    """Custom type iso3201PCfgPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            50
        )
    )
    namedValues = NamedValues(
        ("iso3201", 50)
    )


_Iso3201PCfgPortType_Type.__name__ = "Integer32"
_Iso3201PCfgPortType_Object = MibTableColumn
iso3201PCfgPortType = _Iso3201PCfgPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 28, 1, 2),
    _Iso3201PCfgPortType_Type()
)
iso3201PCfgPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PCfgPortType.setStatus("mandatory")


class _Iso3201PCfgPortSpeed_Type(Integer32):
    """Custom type iso3201PCfgPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              8,
              13,
              14,
              15,
              16,
              99)
        )
    )
    namedValues = NamedValues(
        *(("speed1200", 4),
          ("speed1800", 8),
          ("speed19200", 16),
          ("speed2400", 13),
          ("speed300", 3),
          ("speed4800", 14),
          ("speed600", 5),
          ("speed7200", 99),
          ("speed9600", 15))
    )


_Iso3201PCfgPortSpeed_Type.__name__ = "Integer32"
_Iso3201PCfgPortSpeed_Object = MibTableColumn
iso3201PCfgPortSpeed = _Iso3201PCfgPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 28, 1, 3),
    _Iso3201PCfgPortSpeed_Type()
)
iso3201PCfgPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PCfgPortSpeed.setStatus("mandatory")


class _Iso3201PCfgNoOfControllers_Type(Integer32):
    """Custom type iso3201PCfgNoOfControllers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Iso3201PCfgNoOfControllers_Type.__name__ = "Integer32"
_Iso3201PCfgNoOfControllers_Object = MibTableColumn
iso3201PCfgNoOfControllers = _Iso3201PCfgNoOfControllers_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 28, 1, 4),
    _Iso3201PCfgNoOfControllers_Type()
)
iso3201PCfgNoOfControllers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PCfgNoOfControllers.setStatus("mandatory")


class _Iso3201PCfgResponseTimeout_Type(Integer32):
    """Custom type iso3201PCfgResponseTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_Iso3201PCfgResponseTimeout_Type.__name__ = "Integer32"
_Iso3201PCfgResponseTimeout_Object = MibTableColumn
iso3201PCfgResponseTimeout = _Iso3201PCfgResponseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 28, 1, 5),
    _Iso3201PCfgResponseTimeout_Type()
)
iso3201PCfgResponseTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PCfgResponseTimeout.setStatus("mandatory")


class _Iso3201PCfgInterChrTimeout_Type(Integer32):
    """Custom type iso3201PCfgInterChrTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Iso3201PCfgInterChrTimeout_Type.__name__ = "Integer32"
_Iso3201PCfgInterChrTimeout_Object = MibTableColumn
iso3201PCfgInterChrTimeout = _Iso3201PCfgInterChrTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 28, 1, 6),
    _Iso3201PCfgInterChrTimeout_Type()
)
iso3201PCfgInterChrTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PCfgInterChrTimeout.setStatus("mandatory")


class _Iso3201PCfgNoOfRetries_Type(Integer32):
    """Custom type iso3201PCfgNoOfRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Iso3201PCfgNoOfRetries_Type.__name__ = "Integer32"
_Iso3201PCfgNoOfRetries_Object = MibTableColumn
iso3201PCfgNoOfRetries = _Iso3201PCfgNoOfRetries_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 28, 1, 7),
    _Iso3201PCfgNoOfRetries_Type()
)
iso3201PCfgNoOfRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PCfgNoOfRetries.setStatus("mandatory")


class _Iso3201PCfgNoOfConsecRetries_Type(Integer32):
    """Custom type iso3201PCfgNoOfConsecRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_Iso3201PCfgNoOfConsecRetries_Type.__name__ = "Integer32"
_Iso3201PCfgNoOfConsecRetries_Object = MibTableColumn
iso3201PCfgNoOfConsecRetries = _Iso3201PCfgNoOfConsecRetries_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 28, 1, 8),
    _Iso3201PCfgNoOfConsecRetries_Type()
)
iso3201PCfgNoOfConsecRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PCfgNoOfConsecRetries.setStatus("mandatory")


class _Iso3201PCfgSlowPollWaitCycle_Type(Integer32):
    """Custom type iso3201PCfgSlowPollWaitCycle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Iso3201PCfgSlowPollWaitCycle_Type.__name__ = "Integer32"
_Iso3201PCfgSlowPollWaitCycle_Object = MibTableColumn
iso3201PCfgSlowPollWaitCycle = _Iso3201PCfgSlowPollWaitCycle_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 28, 1, 9),
    _Iso3201PCfgSlowPollWaitCycle_Type()
)
iso3201PCfgSlowPollWaitCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PCfgSlowPollWaitCycle.setStatus("mandatory")


class _Iso3201PCfgElectricalInterfaceType_Type(Integer32):
    """Custom type iso3201PCfgElectricalInterfaceType based on Integer32"""
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
        *(("none", 5),
          ("v24", 1),
          ("v35", 2),
          ("v36", 3),
          ("x21", 4))
    )


_Iso3201PCfgElectricalInterfaceType_Type.__name__ = "Integer32"
_Iso3201PCfgElectricalInterfaceType_Object = MibTableColumn
iso3201PCfgElectricalInterfaceType = _Iso3201PCfgElectricalInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 28, 1, 10),
    _Iso3201PCfgElectricalInterfaceType_Type()
)
iso3201PCfgElectricalInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PCfgElectricalInterfaceType.setStatus("mandatory")


class _Iso3201PCfgV24ElectricalInterfaceOption_Type(Integer32):
    """Custom type iso3201PCfgV24ElectricalInterfaceOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ri", 1),
          ("tm", 2))
    )


_Iso3201PCfgV24ElectricalInterfaceOption_Type.__name__ = "Integer32"
_Iso3201PCfgV24ElectricalInterfaceOption_Object = MibTableColumn
iso3201PCfgV24ElectricalInterfaceOption = _Iso3201PCfgV24ElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 28, 1, 11),
    _Iso3201PCfgV24ElectricalInterfaceOption_Type()
)
iso3201PCfgV24ElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PCfgV24ElectricalInterfaceOption.setStatus("mandatory")


class _Iso3201PCfgHighSpeedElectricalInterfaceOption_Type(Integer32):
    """Custom type iso3201PCfgHighSpeedElectricalInterfaceOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("xover", 2))
    )


_Iso3201PCfgHighSpeedElectricalInterfaceOption_Type.__name__ = "Integer32"
_Iso3201PCfgHighSpeedElectricalInterfaceOption_Object = MibTableColumn
iso3201PCfgHighSpeedElectricalInterfaceOption = _Iso3201PCfgHighSpeedElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 28, 1, 12),
    _Iso3201PCfgHighSpeedElectricalInterfaceOption_Type()
)
iso3201PCfgHighSpeedElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PCfgHighSpeedElectricalInterfaceOption.setStatus("mandatory")
_Cdx6500PCTStationProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTStationProtocolGroup = _Cdx6500PCTStationProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3)
)
_Cdx6500SPCT3201StnTable_Object = MibTable
cdx6500SPCT3201StnTable = _Cdx6500SPCT3201StnTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 7)
)
if mibBuilder.loadTexts:
    cdx6500SPCT3201StnTable.setStatus("mandatory")
_Cdx6500SPCT3201StnEntry_Object = MibTableRow
cdx6500SPCT3201StnEntry = _Cdx6500SPCT3201StnEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 7, 1)
)
cdx6500SPCT3201StnEntry.setIndexNames(
    (0, "ISO3201-OPT-MIB", "iso3201SCfgPortNum"),
    (0, "ISO3201-OPT-MIB", "iso3201SCfgStnNum"),
)
if mibBuilder.loadTexts:
    cdx6500SPCT3201StnEntry.setStatus("mandatory")


class _Iso3201SCfgPortNum_Type(Integer32):
    """Custom type iso3201SCfgPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Iso3201SCfgPortNum_Type.__name__ = "Integer32"
_Iso3201SCfgPortNum_Object = MibTableColumn
iso3201SCfgPortNum = _Iso3201SCfgPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 7, 1, 1),
    _Iso3201SCfgPortNum_Type()
)
iso3201SCfgPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SCfgPortNum.setStatus("mandatory")


class _Iso3201SCfgStnNum_Type(Integer32):
    """Custom type iso3201SCfgStnNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Iso3201SCfgStnNum_Type.__name__ = "Integer32"
_Iso3201SCfgStnNum_Object = MibTableColumn
iso3201SCfgStnNum = _Iso3201SCfgStnNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 7, 1, 2),
    _Iso3201SCfgStnNum_Type()
)
iso3201SCfgStnNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SCfgStnNum.setStatus("mandatory")
_Iso3201SCfgControllerAddress_Type = DisplayString
_Iso3201SCfgControllerAddress_Object = MibTableColumn
iso3201SCfgControllerAddress = _Iso3201SCfgControllerAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 7, 1, 3),
    _Iso3201SCfgControllerAddress_Type()
)
iso3201SCfgControllerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SCfgControllerAddress.setStatus("mandatory")


class _Iso3201SCfgAutocallMnemonic_Type(DisplayString):
    """Custom type iso3201SCfgAutocallMnemonic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Iso3201SCfgAutocallMnemonic_Type.__name__ = "DisplayString"
_Iso3201SCfgAutocallMnemonic_Object = MibTableColumn
iso3201SCfgAutocallMnemonic = _Iso3201SCfgAutocallMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 7, 1, 4),
    _Iso3201SCfgAutocallMnemonic_Type()
)
iso3201SCfgAutocallMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SCfgAutocallMnemonic.setStatus("mandatory")


class _Iso3201SCfgAutocallTimeout_Type(Integer32):
    """Custom type iso3201SCfgAutocallTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_Iso3201SCfgAutocallTimeout_Type.__name__ = "Integer32"
_Iso3201SCfgAutocallTimeout_Object = MibTableColumn
iso3201SCfgAutocallTimeout = _Iso3201SCfgAutocallTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 7, 1, 5),
    _Iso3201SCfgAutocallTimeout_Type()
)
iso3201SCfgAutocallTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SCfgAutocallTimeout.setStatus("mandatory")


class _Iso3201SCfgMaxNoAutocallAttempts_Type(Integer32):
    """Custom type iso3201SCfgMaxNoAutocallAttempts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Iso3201SCfgMaxNoAutocallAttempts_Type.__name__ = "Integer32"
_Iso3201SCfgMaxNoAutocallAttempts_Object = MibTableColumn
iso3201SCfgMaxNoAutocallAttempts = _Iso3201SCfgMaxNoAutocallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 7, 1, 6),
    _Iso3201SCfgMaxNoAutocallAttempts_Type()
)
iso3201SCfgMaxNoAutocallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SCfgMaxNoAutocallAttempts.setStatus("mandatory")


class _Iso3201SCfgX25Address_Type(DisplayString):
    """Custom type iso3201SCfgX25Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Iso3201SCfgX25Address_Type.__name__ = "DisplayString"
_Iso3201SCfgX25Address_Object = MibTableColumn
iso3201SCfgX25Address = _Iso3201SCfgX25Address_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 7, 1, 7),
    _Iso3201SCfgX25Address_Type()
)
iso3201SCfgX25Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SCfgX25Address.setStatus("mandatory")


class _Iso3201SCfgBillingRecords_Type(Integer32):
    """Custom type iso3201SCfgBillingRecords based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("billingDisabled", 1),
          ("billingEnabled", 2))
    )


_Iso3201SCfgBillingRecords_Type.__name__ = "Integer32"
_Iso3201SCfgBillingRecords_Object = MibTableColumn
iso3201SCfgBillingRecords = _Iso3201SCfgBillingRecords_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 7, 1, 8),
    _Iso3201SCfgBillingRecords_Type()
)
iso3201SCfgBillingRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SCfgBillingRecords.setStatus("mandatory")
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
_Cdx6500PPST3201PStatsTable_Object = MibTable
cdx6500PPST3201PStatsTable = _Cdx6500PPST3201PStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 29)
)
if mibBuilder.loadTexts:
    cdx6500PPST3201PStatsTable.setStatus("mandatory")
_Cdx6500PPST3201PStatsEntry_Object = MibTableRow
cdx6500PPST3201PStatsEntry = _Cdx6500PPST3201PStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 29, 1)
)
cdx6500PPST3201PStatsEntry.setIndexNames(
    (0, "ISO3201-OPT-MIB", "iso3201PStatsPortNum"),
)
if mibBuilder.loadTexts:
    cdx6500PPST3201PStatsEntry.setStatus("mandatory")


class _Iso3201PStatsPortNum_Type(Integer32):
    """Custom type iso3201PStatsPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Iso3201PStatsPortNum_Type.__name__ = "Integer32"
_Iso3201PStatsPortNum_Object = MibTableColumn
iso3201PStatsPortNum = _Iso3201PStatsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 29, 1, 1),
    _Iso3201PStatsPortNum_Type()
)
iso3201PStatsPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PStatsPortNum.setStatus("mandatory")


class _Iso3201PStatsPortStatus_Type(Integer32):
    """Custom type iso3201PStatsPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("up", 2))
    )


_Iso3201PStatsPortStatus_Type.__name__ = "Integer32"
_Iso3201PStatsPortStatus_Object = MibTableColumn
iso3201PStatsPortStatus = _Iso3201PStatsPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 29, 1, 2),
    _Iso3201PStatsPortStatus_Type()
)
iso3201PStatsPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PStatsPortStatus.setStatus("mandatory")


class _Iso3201PStatsPortType_Type(Integer32):
    """Custom type iso3201PStatsPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            50
        )
    )
    namedValues = NamedValues(
        ("iso3201", 50)
    )


_Iso3201PStatsPortType_Type.__name__ = "Integer32"
_Iso3201PStatsPortType_Object = MibTableColumn
iso3201PStatsPortType = _Iso3201PStatsPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 29, 1, 3),
    _Iso3201PStatsPortType_Type()
)
iso3201PStatsPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PStatsPortType.setStatus("mandatory")


class _Iso3201PStatsPortSpeed_Type(Integer32):
    """Custom type iso3201PStatsPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              8,
              13,
              14,
              15,
              16,
              99)
        )
    )
    namedValues = NamedValues(
        *(("speed1200", 4),
          ("speed1800", 8),
          ("speed19200", 16),
          ("speed2400", 13),
          ("speed300", 3),
          ("speed4800", 14),
          ("speed600", 5),
          ("speed7200", 99),
          ("speed9600", 15))
    )


_Iso3201PStatsPortSpeed_Type.__name__ = "Integer32"
_Iso3201PStatsPortSpeed_Object = MibTableColumn
iso3201PStatsPortSpeed = _Iso3201PStatsPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 29, 1, 4),
    _Iso3201PStatsPortSpeed_Type()
)
iso3201PStatsPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PStatsPortSpeed.setStatus("mandatory")
_Iso3201PStatsPortUtilIn_Type = Integer32
_Iso3201PStatsPortUtilIn_Object = MibTableColumn
iso3201PStatsPortUtilIn = _Iso3201PStatsPortUtilIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 29, 1, 5),
    _Iso3201PStatsPortUtilIn_Type()
)
iso3201PStatsPortUtilIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PStatsPortUtilIn.setStatus("mandatory")
_Iso3201PStatsPortUtilOut_Type = Integer32
_Iso3201PStatsPortUtilOut_Object = MibTableColumn
iso3201PStatsPortUtilOut = _Iso3201PStatsPortUtilOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 29, 1, 6),
    _Iso3201PStatsPortUtilOut_Type()
)
iso3201PStatsPortUtilOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PStatsPortUtilOut.setStatus("mandatory")


class _Iso3201PStatsLineStatus_Type(Integer32):
    """Custom type iso3201PStatsLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_Iso3201PStatsLineStatus_Type.__name__ = "Integer32"
_Iso3201PStatsLineStatus_Object = MibTableColumn
iso3201PStatsLineStatus = _Iso3201PStatsLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 29, 1, 7),
    _Iso3201PStatsLineStatus_Type()
)
iso3201PStatsLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PStatsLineStatus.setStatus("mandatory")
_Iso3201PStatsTxChrs_Type = Counter32
_Iso3201PStatsTxChrs_Object = MibTableColumn
iso3201PStatsTxChrs = _Iso3201PStatsTxChrs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 29, 1, 8),
    _Iso3201PStatsTxChrs_Type()
)
iso3201PStatsTxChrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PStatsTxChrs.setStatus("mandatory")
_Iso3201PStatsTxMsgs_Type = Counter32
_Iso3201PStatsTxMsgs_Object = MibTableColumn
iso3201PStatsTxMsgs = _Iso3201PStatsTxMsgs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 29, 1, 9),
    _Iso3201PStatsTxMsgs_Type()
)
iso3201PStatsTxMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PStatsTxMsgs.setStatus("mandatory")
_Iso3201PStatsTxPolls_Type = Counter32
_Iso3201PStatsTxPolls_Object = MibTableColumn
iso3201PStatsTxPolls = _Iso3201PStatsTxPolls_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 29, 1, 10),
    _Iso3201PStatsTxPolls_Type()
)
iso3201PStatsTxPolls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PStatsTxPolls.setStatus("mandatory")
_Iso3201PStatsTxSelects_Type = Counter32
_Iso3201PStatsTxSelects_Object = MibTableColumn
iso3201PStatsTxSelects = _Iso3201PStatsTxSelects_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 29, 1, 11),
    _Iso3201PStatsTxSelects_Type()
)
iso3201PStatsTxSelects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PStatsTxSelects.setStatus("mandatory")
_Iso3201PStatsTxACKs_Type = Counter32
_Iso3201PStatsTxACKs_Object = MibTableColumn
iso3201PStatsTxACKs = _Iso3201PStatsTxACKs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 29, 1, 12),
    _Iso3201PStatsTxACKs_Type()
)
iso3201PStatsTxACKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PStatsTxACKs.setStatus("mandatory")
_Iso3201PStatsTxNAKs_Type = Counter32
_Iso3201PStatsTxNAKs_Object = MibTableColumn
iso3201PStatsTxNAKs = _Iso3201PStatsTxNAKs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 29, 1, 13),
    _Iso3201PStatsTxNAKs_Type()
)
iso3201PStatsTxNAKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PStatsTxNAKs.setStatus("mandatory")
_Iso3201PStatsTxENQs_Type = Counter32
_Iso3201PStatsTxENQs_Object = MibTableColumn
iso3201PStatsTxENQs = _Iso3201PStatsTxENQs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 29, 1, 14),
    _Iso3201PStatsTxENQs_Type()
)
iso3201PStatsTxENQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PStatsTxENQs.setStatus("mandatory")
_Iso3201PStatsRxChrs_Type = Counter32
_Iso3201PStatsRxChrs_Object = MibTableColumn
iso3201PStatsRxChrs = _Iso3201PStatsRxChrs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 29, 1, 15),
    _Iso3201PStatsRxChrs_Type()
)
iso3201PStatsRxChrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PStatsRxChrs.setStatus("mandatory")
_Iso3201PStatsRxMsgs_Type = Counter32
_Iso3201PStatsRxMsgs_Object = MibTableColumn
iso3201PStatsRxMsgs = _Iso3201PStatsRxMsgs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 29, 1, 16),
    _Iso3201PStatsRxMsgs_Type()
)
iso3201PStatsRxMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PStatsRxMsgs.setStatus("mandatory")
_Iso3201PStatsRxACKs_Type = Counter32
_Iso3201PStatsRxACKs_Object = MibTableColumn
iso3201PStatsRxACKs = _Iso3201PStatsRxACKs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 29, 1, 17),
    _Iso3201PStatsRxACKs_Type()
)
iso3201PStatsRxACKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PStatsRxACKs.setStatus("mandatory")
_Iso3201PStatsRxNAKs_Type = Counter32
_Iso3201PStatsRxNAKs_Object = MibTableColumn
iso3201PStatsRxNAKs = _Iso3201PStatsRxNAKs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 29, 1, 18),
    _Iso3201PStatsRxNAKs_Type()
)
iso3201PStatsRxNAKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PStatsRxNAKs.setStatus("mandatory")
_Iso3201PStatsRxENQs_Type = Counter32
_Iso3201PStatsRxENQs_Object = MibTableColumn
iso3201PStatsRxENQs = _Iso3201PStatsRxENQs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 29, 1, 19),
    _Iso3201PStatsRxENQs_Type()
)
iso3201PStatsRxENQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201PStatsRxENQs.setStatus("mandatory")
_Cdx6500PSTStationProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTStationProtocolGroup = _Cdx6500PSTStationProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3)
)
_Cdx6500SPST3201StnTable_ObjectIdentity = ObjectIdentity
cdx6500SPST3201StnTable = _Cdx6500SPST3201StnTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6)
)
_Cdx6500SPST3201SStatsTable_Object = MibTable
cdx6500SPST3201SStatsTable = _Cdx6500SPST3201SStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 1)
)
if mibBuilder.loadTexts:
    cdx6500SPST3201SStatsTable.setStatus("mandatory")
_Cdx6500SPST3201StnEntry_Object = MibTableRow
cdx6500SPST3201StnEntry = _Cdx6500SPST3201StnEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 1, 1)
)
cdx6500SPST3201StnEntry.setIndexNames(
    (0, "ISO3201-OPT-MIB", "iso3201SStatsPortNum"),
    (0, "ISO3201-OPT-MIB", "iso3201SStatsStnNum"),
)
if mibBuilder.loadTexts:
    cdx6500SPST3201StnEntry.setStatus("mandatory")


class _Iso3201SStatsPortNum_Type(Integer32):
    """Custom type iso3201SStatsPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Iso3201SStatsPortNum_Type.__name__ = "Integer32"
_Iso3201SStatsPortNum_Object = MibTableColumn
iso3201SStatsPortNum = _Iso3201SStatsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 1, 1, 1),
    _Iso3201SStatsPortNum_Type()
)
iso3201SStatsPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsPortNum.setStatus("mandatory")


class _Iso3201SStatsStnNum_Type(Integer32):
    """Custom type iso3201SStatsStnNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Iso3201SStatsStnNum_Type.__name__ = "Integer32"
_Iso3201SStatsStnNum_Object = MibTableColumn
iso3201SStatsStnNum = _Iso3201SStatsStnNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 1, 1, 2),
    _Iso3201SStatsStnNum_Type()
)
iso3201SStatsStnNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsStnNum.setStatus("mandatory")
_Iso3201SStatsControllerAddress_Type = DisplayString
_Iso3201SStatsControllerAddress_Object = MibTableColumn
iso3201SStatsControllerAddress = _Iso3201SStatsControllerAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 1, 1, 3),
    _Iso3201SStatsControllerAddress_Type()
)
iso3201SStatsControllerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsControllerAddress.setStatus("mandatory")


class _Iso3201SStatsStnState_Type(Integer32):
    """Custom type iso3201SStatsStnState based on Integer32"""
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
        *(("blocked", 5),
          ("disabled", 1),
          ("down", 2),
          ("suspended", 4),
          ("up", 3))
    )


_Iso3201SStatsStnState_Type.__name__ = "Integer32"
_Iso3201SStatsStnState_Object = MibTableColumn
iso3201SStatsStnState = _Iso3201SStatsStnState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 1, 1, 4),
    _Iso3201SStatsStnState_Type()
)
iso3201SStatsStnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsStnState.setStatus("mandatory")


class _Iso3201SStatsCurrentStatus_Type(Integer32):
    """Custom type iso3201SStatsCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("calling", 2),
          ("connected", 3),
          ("idle", 1))
    )


_Iso3201SStatsCurrentStatus_Type.__name__ = "Integer32"
_Iso3201SStatsCurrentStatus_Object = MibTableColumn
iso3201SStatsCurrentStatus = _Iso3201SStatsCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 1, 1, 5),
    _Iso3201SStatsCurrentStatus_Type()
)
iso3201SStatsCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsCurrentStatus.setStatus("mandatory")
_Iso3201SStatsNoOfAutocallAttmpts_Type = Gauge32
_Iso3201SStatsNoOfAutocallAttmpts_Object = MibTableColumn
iso3201SStatsNoOfAutocallAttmpts = _Iso3201SStatsNoOfAutocallAttmpts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 1, 1, 6),
    _Iso3201SStatsNoOfAutocallAttmpts_Type()
)
iso3201SStatsNoOfAutocallAttmpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsNoOfAutocallAttmpts.setStatus("mandatory")
_Iso3201SStatsNxtAutocallAttmpt_Type = Integer32
_Iso3201SStatsNxtAutocallAttmpt_Object = MibTableColumn
iso3201SStatsNxtAutocallAttmpt = _Iso3201SStatsNxtAutocallAttmpt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 1, 1, 7),
    _Iso3201SStatsNxtAutocallAttmpt_Type()
)
iso3201SStatsNxtAutocallAttmpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsNxtAutocallAttmpt.setStatus("mandatory")
_Iso3201SStatsLastClearCauseCode_Type = DisplayString
_Iso3201SStatsLastClearCauseCode_Object = MibTableColumn
iso3201SStatsLastClearCauseCode = _Iso3201SStatsLastClearCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 1, 1, 8),
    _Iso3201SStatsLastClearCauseCode_Type()
)
iso3201SStatsLastClearCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsLastClearCauseCode.setStatus("mandatory")
_Iso3201SStatsLastClearDiagCode_Type = DisplayString
_Iso3201SStatsLastClearDiagCode_Object = MibTableColumn
iso3201SStatsLastClearDiagCode = _Iso3201SStatsLastClearDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 1, 1, 9),
    _Iso3201SStatsLastClearDiagCode_Type()
)
iso3201SStatsLastClearDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsLastClearDiagCode.setStatus("mandatory")
_Iso3201SStatsLastInCalledAddress_Type = DisplayString
_Iso3201SStatsLastInCalledAddress_Object = MibTableColumn
iso3201SStatsLastInCalledAddress = _Iso3201SStatsLastInCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 1, 1, 10),
    _Iso3201SStatsLastInCalledAddress_Type()
)
iso3201SStatsLastInCalledAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsLastInCalledAddress.setStatus("mandatory")
_Iso3201SStatsLastInCallingAddress_Type = DisplayString
_Iso3201SStatsLastInCallingAddress_Object = MibTableColumn
iso3201SStatsLastInCallingAddress = _Iso3201SStatsLastInCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 1, 1, 11),
    _Iso3201SStatsLastInCallingAddress_Type()
)
iso3201SStatsLastInCallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsLastInCallingAddress.setStatus("mandatory")
_Iso3201SStatsLastInCallFacilities_Type = DisplayString
_Iso3201SStatsLastInCallFacilities_Object = MibTableColumn
iso3201SStatsLastInCallFacilities = _Iso3201SStatsLastInCallFacilities_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 1, 1, 12),
    _Iso3201SStatsLastInCallFacilities_Type()
)
iso3201SStatsLastInCallFacilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsLastInCallFacilities.setStatus("mandatory")
_Iso3201SStatsLastInCallCUD_Type = DisplayString
_Iso3201SStatsLastInCallCUD_Object = MibTableColumn
iso3201SStatsLastInCallCUD = _Iso3201SStatsLastInCallCUD_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 1, 1, 13),
    _Iso3201SStatsLastInCallCUD_Type()
)
iso3201SStatsLastInCallCUD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsLastInCallCUD.setStatus("mandatory")


class _Iso3201SStatsLastOutCalledAddress_Type(DisplayString):
    """Custom type iso3201SStatsLastOutCalledAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Iso3201SStatsLastOutCalledAddress_Type.__name__ = "DisplayString"
_Iso3201SStatsLastOutCalledAddress_Object = MibTableColumn
iso3201SStatsLastOutCalledAddress = _Iso3201SStatsLastOutCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 1, 1, 14),
    _Iso3201SStatsLastOutCalledAddress_Type()
)
iso3201SStatsLastOutCalledAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsLastOutCalledAddress.setStatus("mandatory")


class _Iso3201SStatsLastOutCallingAddress_Type(DisplayString):
    """Custom type iso3201SStatsLastOutCallingAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Iso3201SStatsLastOutCallingAddress_Type.__name__ = "DisplayString"
_Iso3201SStatsLastOutCallingAddress_Object = MibTableColumn
iso3201SStatsLastOutCallingAddress = _Iso3201SStatsLastOutCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 1, 1, 15),
    _Iso3201SStatsLastOutCallingAddress_Type()
)
iso3201SStatsLastOutCallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsLastOutCallingAddress.setStatus("mandatory")
_Iso3201SStatsLastOutCallFacilities_Type = DisplayString
_Iso3201SStatsLastOutCallFacilities_Object = MibTableColumn
iso3201SStatsLastOutCallFacilities = _Iso3201SStatsLastOutCallFacilities_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 1, 1, 16),
    _Iso3201SStatsLastOutCallFacilities_Type()
)
iso3201SStatsLastOutCallFacilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsLastOutCallFacilities.setStatus("mandatory")
_Iso3201SStatsLastOutCallCUD_Type = DisplayString
_Iso3201SStatsLastOutCallCUD_Object = MibTableColumn
iso3201SStatsLastOutCallCUD = _Iso3201SStatsLastOutCallCUD_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 1, 1, 17),
    _Iso3201SStatsLastOutCallCUD_Type()
)
iso3201SStatsLastOutCallCUD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsLastOutCallCUD.setStatus("mandatory")
_Cdx6500SPST3201PktSummTable_Object = MibTable
cdx6500SPST3201PktSummTable = _Cdx6500SPST3201PktSummTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 2)
)
if mibBuilder.loadTexts:
    cdx6500SPST3201PktSummTable.setStatus("mandatory")
_Cdx6500SPST3201PktSummEntry_Object = MibTableRow
cdx6500SPST3201PktSummEntry = _Cdx6500SPST3201PktSummEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 2, 1)
)
cdx6500SPST3201PktSummEntry.setIndexNames(
    (0, "ISO3201-OPT-MIB", "iso3201SStatsPktSummPortNum"),
    (0, "ISO3201-OPT-MIB", "iso3201SStatsPktSummStnNum"),
)
if mibBuilder.loadTexts:
    cdx6500SPST3201PktSummEntry.setStatus("mandatory")


class _Iso3201SStatsPktSummPortNum_Type(Integer32):
    """Custom type iso3201SStatsPktSummPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Iso3201SStatsPktSummPortNum_Type.__name__ = "Integer32"
_Iso3201SStatsPktSummPortNum_Object = MibTableColumn
iso3201SStatsPktSummPortNum = _Iso3201SStatsPktSummPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 2, 1, 1),
    _Iso3201SStatsPktSummPortNum_Type()
)
iso3201SStatsPktSummPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsPktSummPortNum.setStatus("mandatory")


class _Iso3201SStatsPktSummStnNum_Type(Integer32):
    """Custom type iso3201SStatsPktSummStnNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Iso3201SStatsPktSummStnNum_Type.__name__ = "Integer32"
_Iso3201SStatsPktSummStnNum_Object = MibTableColumn
iso3201SStatsPktSummStnNum = _Iso3201SStatsPktSummStnNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 2, 1, 2),
    _Iso3201SStatsPktSummStnNum_Type()
)
iso3201SStatsPktSummStnNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsPktSummStnNum.setStatus("mandatory")
_Iso3201SStatsTxData_Type = Counter32
_Iso3201SStatsTxData_Object = MibTableColumn
iso3201SStatsTxData = _Iso3201SStatsTxData_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 2, 1, 3),
    _Iso3201SStatsTxData_Type()
)
iso3201SStatsTxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsTxData.setStatus("mandatory")
_Iso3201SStatsTxCallRequest_Type = Counter32
_Iso3201SStatsTxCallRequest_Object = MibTableColumn
iso3201SStatsTxCallRequest = _Iso3201SStatsTxCallRequest_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 2, 1, 4),
    _Iso3201SStatsTxCallRequest_Type()
)
iso3201SStatsTxCallRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsTxCallRequest.setStatus("mandatory")
_Iso3201SStatsTxCallAccept_Type = Counter32
_Iso3201SStatsTxCallAccept_Object = MibTableColumn
iso3201SStatsTxCallAccept = _Iso3201SStatsTxCallAccept_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 2, 1, 5),
    _Iso3201SStatsTxCallAccept_Type()
)
iso3201SStatsTxCallAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsTxCallAccept.setStatus("mandatory")
_Iso3201SStatsTxClearRequest_Type = Counter32
_Iso3201SStatsTxClearRequest_Object = MibTableColumn
iso3201SStatsTxClearRequest = _Iso3201SStatsTxClearRequest_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 2, 1, 6),
    _Iso3201SStatsTxClearRequest_Type()
)
iso3201SStatsTxClearRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsTxClearRequest.setStatus("mandatory")
_Iso3201SStatsTxClearConfirm_Type = Counter32
_Iso3201SStatsTxClearConfirm_Object = MibTableColumn
iso3201SStatsTxClearConfirm = _Iso3201SStatsTxClearConfirm_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 2, 1, 7),
    _Iso3201SStatsTxClearConfirm_Type()
)
iso3201SStatsTxClearConfirm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsTxClearConfirm.setStatus("mandatory")
_Iso3201SStatsTxResetRequest_Type = Counter32
_Iso3201SStatsTxResetRequest_Object = MibTableColumn
iso3201SStatsTxResetRequest = _Iso3201SStatsTxResetRequest_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 2, 1, 8),
    _Iso3201SStatsTxResetRequest_Type()
)
iso3201SStatsTxResetRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsTxResetRequest.setStatus("mandatory")
_Iso3201SStatsTxResetConfirm_Type = Counter32
_Iso3201SStatsTxResetConfirm_Object = MibTableColumn
iso3201SStatsTxResetConfirm = _Iso3201SStatsTxResetConfirm_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 2, 1, 9),
    _Iso3201SStatsTxResetConfirm_Type()
)
iso3201SStatsTxResetConfirm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsTxResetConfirm.setStatus("mandatory")
_Iso3201SStatsTxWindowClosed_Type = Gauge32
_Iso3201SStatsTxWindowClosed_Object = MibTableColumn
iso3201SStatsTxWindowClosed = _Iso3201SStatsTxWindowClosed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 2, 1, 10),
    _Iso3201SStatsTxWindowClosed_Type()
)
iso3201SStatsTxWindowClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsTxWindowClosed.setStatus("mandatory")
_Iso3201SStatsRxData_Type = Counter32
_Iso3201SStatsRxData_Object = MibTableColumn
iso3201SStatsRxData = _Iso3201SStatsRxData_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 2, 1, 11),
    _Iso3201SStatsRxData_Type()
)
iso3201SStatsRxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsRxData.setStatus("mandatory")
_Iso3201SStatsRxCallRequest_Type = Counter32
_Iso3201SStatsRxCallRequest_Object = MibTableColumn
iso3201SStatsRxCallRequest = _Iso3201SStatsRxCallRequest_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 2, 1, 12),
    _Iso3201SStatsRxCallRequest_Type()
)
iso3201SStatsRxCallRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsRxCallRequest.setStatus("mandatory")
_Iso3201SStatsRxCallAccept_Type = Counter32
_Iso3201SStatsRxCallAccept_Object = MibTableColumn
iso3201SStatsRxCallAccept = _Iso3201SStatsRxCallAccept_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 2, 1, 13),
    _Iso3201SStatsRxCallAccept_Type()
)
iso3201SStatsRxCallAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsRxCallAccept.setStatus("mandatory")
_Iso3201SStatsRxClearRequest_Type = Counter32
_Iso3201SStatsRxClearRequest_Object = MibTableColumn
iso3201SStatsRxClearRequest = _Iso3201SStatsRxClearRequest_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 2, 1, 14),
    _Iso3201SStatsRxClearRequest_Type()
)
iso3201SStatsRxClearRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsRxClearRequest.setStatus("mandatory")
_Iso3201SStatsRxClearConfirm_Type = Counter32
_Iso3201SStatsRxClearConfirm_Object = MibTableColumn
iso3201SStatsRxClearConfirm = _Iso3201SStatsRxClearConfirm_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 2, 1, 15),
    _Iso3201SStatsRxClearConfirm_Type()
)
iso3201SStatsRxClearConfirm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsRxClearConfirm.setStatus("mandatory")
_Iso3201SStatsRxResetRequest_Type = Counter32
_Iso3201SStatsRxResetRequest_Object = MibTableColumn
iso3201SStatsRxResetRequest = _Iso3201SStatsRxResetRequest_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 2, 1, 16),
    _Iso3201SStatsRxResetRequest_Type()
)
iso3201SStatsRxResetRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsRxResetRequest.setStatus("mandatory")
_Iso3201SStatsRxResetConfirm_Type = Counter32
_Iso3201SStatsRxResetConfirm_Object = MibTableColumn
iso3201SStatsRxResetConfirm = _Iso3201SStatsRxResetConfirm_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 2, 1, 17),
    _Iso3201SStatsRxResetConfirm_Type()
)
iso3201SStatsRxResetConfirm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsRxResetConfirm.setStatus("mandatory")
_Iso3201SStatsRxWindowClosed_Type = Gauge32
_Iso3201SStatsRxWindowClosed_Object = MibTableColumn
iso3201SStatsRxWindowClosed = _Iso3201SStatsRxWindowClosed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 2, 1, 18),
    _Iso3201SStatsRxWindowClosed_Type()
)
iso3201SStatsRxWindowClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsRxWindowClosed.setStatus("mandatory")
_Cdx6500SPST3201SummTable_Object = MibTable
cdx6500SPST3201SummTable = _Cdx6500SPST3201SummTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3)
)
if mibBuilder.loadTexts:
    cdx6500SPST3201SummTable.setStatus("mandatory")
_Cdx6500SPST3201SummEntry_Object = MibTableRow
cdx6500SPST3201SummEntry = _Cdx6500SPST3201SummEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1)
)
cdx6500SPST3201SummEntry.setIndexNames(
    (0, "ISO3201-OPT-MIB", "iso3201SStatsSummPortNum"),
    (0, "ISO3201-OPT-MIB", "iso3201SStatsSummStnNum"),
)
if mibBuilder.loadTexts:
    cdx6500SPST3201SummEntry.setStatus("mandatory")


class _Iso3201SStatsSummPortNum_Type(Integer32):
    """Custom type iso3201SStatsSummPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Iso3201SStatsSummPortNum_Type.__name__ = "Integer32"
_Iso3201SStatsSummPortNum_Object = MibTableColumn
iso3201SStatsSummPortNum = _Iso3201SStatsSummPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1, 1),
    _Iso3201SStatsSummPortNum_Type()
)
iso3201SStatsSummPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsSummPortNum.setStatus("mandatory")


class _Iso3201SStatsSummStnNum_Type(Integer32):
    """Custom type iso3201SStatsSummStnNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Iso3201SStatsSummStnNum_Type.__name__ = "Integer32"
_Iso3201SStatsSummStnNum_Object = MibTableColumn
iso3201SStatsSummStnNum = _Iso3201SStatsSummStnNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1, 2),
    _Iso3201SStatsSummStnNum_Type()
)
iso3201SStatsSummStnNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsSummStnNum.setStatus("mandatory")
_Iso3201SStatsTxPolls_Type = Counter32
_Iso3201SStatsTxPolls_Object = MibTableColumn
iso3201SStatsTxPolls = _Iso3201SStatsTxPolls_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1, 3),
    _Iso3201SStatsTxPolls_Type()
)
iso3201SStatsTxPolls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsTxPolls.setStatus("mandatory")
_Iso3201SStatsTxSelects_Type = Counter32
_Iso3201SStatsTxSelects_Object = MibTableColumn
iso3201SStatsTxSelects = _Iso3201SStatsTxSelects_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1, 4),
    _Iso3201SStatsTxSelects_Type()
)
iso3201SStatsTxSelects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsTxSelects.setStatus("mandatory")
_Iso3201SStatsTxDataBytes_Type = Counter32
_Iso3201SStatsTxDataBytes_Object = MibTableColumn
iso3201SStatsTxDataBytes = _Iso3201SStatsTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1, 5),
    _Iso3201SStatsTxDataBytes_Type()
)
iso3201SStatsTxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsTxDataBytes.setStatus("mandatory")
_Iso3201SStatsTxDataMsgs_Type = Gauge32
_Iso3201SStatsTxDataMsgs_Object = MibTableColumn
iso3201SStatsTxDataMsgs = _Iso3201SStatsTxDataMsgs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1, 6),
    _Iso3201SStatsTxDataMsgs_Type()
)
iso3201SStatsTxDataMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsTxDataMsgs.setStatus("mandatory")
_Iso3201SStatsTxDataMsgsPerHour_Type = Counter32
_Iso3201SStatsTxDataMsgsPerHour_Object = MibTableColumn
iso3201SStatsTxDataMsgsPerHour = _Iso3201SStatsTxDataMsgsPerHour_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1, 7),
    _Iso3201SStatsTxDataMsgsPerHour_Type()
)
iso3201SStatsTxDataMsgsPerHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsTxDataMsgsPerHour.setStatus("mandatory")
_Iso3201SStatsTxAvgMsgLength_Type = Counter32
_Iso3201SStatsTxAvgMsgLength_Object = MibTableColumn
iso3201SStatsTxAvgMsgLength = _Iso3201SStatsTxAvgMsgLength_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1, 8),
    _Iso3201SStatsTxAvgMsgLength_Type()
)
iso3201SStatsTxAvgMsgLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsTxAvgMsgLength.setStatus("mandatory")
_Iso3201SStatsTxMsgsNAKed_Type = Gauge32
_Iso3201SStatsTxMsgsNAKed_Object = MibTableColumn
iso3201SStatsTxMsgsNAKed = _Iso3201SStatsTxMsgsNAKed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1, 9),
    _Iso3201SStatsTxMsgsNAKed_Type()
)
iso3201SStatsTxMsgsNAKed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsTxMsgsNAKed.setStatus("mandatory")
_Iso3201SStatsTxSelectRetryExhausted_Type = Counter32
_Iso3201SStatsTxSelectRetryExhausted_Object = MibTableColumn
iso3201SStatsTxSelectRetryExhausted = _Iso3201SStatsTxSelectRetryExhausted_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1, 10),
    _Iso3201SStatsTxSelectRetryExhausted_Type()
)
iso3201SStatsTxSelectRetryExhausted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsTxSelectRetryExhausted.setStatus("mandatory")
_Iso3201SStatsTxNAKRetryExhausted_Type = Counter32
_Iso3201SStatsTxNAKRetryExhausted_Object = MibTableColumn
iso3201SStatsTxNAKRetryExhausted = _Iso3201SStatsTxNAKRetryExhausted_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1, 11),
    _Iso3201SStatsTxNAKRetryExhausted_Type()
)
iso3201SStatsTxNAKRetryExhausted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsTxNAKRetryExhausted.setStatus("mandatory")
_Iso3201SStatsTxENQs_Type = Gauge32
_Iso3201SStatsTxENQs_Object = MibTableColumn
iso3201SStatsTxENQs = _Iso3201SStatsTxENQs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1, 12),
    _Iso3201SStatsTxENQs_Type()
)
iso3201SStatsTxENQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsTxENQs.setStatus("mandatory")
_Iso3201SStatsTxENQRetryExhausted_Type = Counter32
_Iso3201SStatsTxENQRetryExhausted_Object = MibTableColumn
iso3201SStatsTxENQRetryExhausted = _Iso3201SStatsTxENQRetryExhausted_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1, 13),
    _Iso3201SStatsTxENQRetryExhausted_Type()
)
iso3201SStatsTxENQRetryExhausted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsTxENQRetryExhausted.setStatus("mandatory")
_Iso3201SStatsTxPollingSuspendedByHost_Type = Gauge32
_Iso3201SStatsTxPollingSuspendedByHost_Object = MibTableColumn
iso3201SStatsTxPollingSuspendedByHost = _Iso3201SStatsTxPollingSuspendedByHost_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1, 14),
    _Iso3201SStatsTxPollingSuspendedByHost_Type()
)
iso3201SStatsTxPollingSuspendedByHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsTxPollingSuspendedByHost.setStatus("mandatory")
_Iso3201SStatsRxDataBytes_Type = Counter32
_Iso3201SStatsRxDataBytes_Object = MibTableColumn
iso3201SStatsRxDataBytes = _Iso3201SStatsRxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1, 15),
    _Iso3201SStatsRxDataBytes_Type()
)
iso3201SStatsRxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsRxDataBytes.setStatus("mandatory")
_Iso3201SStatsRxDataMsgs_Type = Gauge32
_Iso3201SStatsRxDataMsgs_Object = MibTableColumn
iso3201SStatsRxDataMsgs = _Iso3201SStatsRxDataMsgs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1, 16),
    _Iso3201SStatsRxDataMsgs_Type()
)
iso3201SStatsRxDataMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsRxDataMsgs.setStatus("mandatory")
_Iso3201SStatsRxDataMsgsPerHour_Type = Counter32
_Iso3201SStatsRxDataMsgsPerHour_Object = MibTableColumn
iso3201SStatsRxDataMsgsPerHour = _Iso3201SStatsRxDataMsgsPerHour_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1, 17),
    _Iso3201SStatsRxDataMsgsPerHour_Type()
)
iso3201SStatsRxDataMsgsPerHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsRxDataMsgsPerHour.setStatus("mandatory")
_Iso3201SStatsRxAvgMsgLength_Type = Counter32
_Iso3201SStatsRxAvgMsgLength_Object = MibTableColumn
iso3201SStatsRxAvgMsgLength = _Iso3201SStatsRxAvgMsgLength_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1, 18),
    _Iso3201SStatsRxAvgMsgLength_Type()
)
iso3201SStatsRxAvgMsgLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsRxAvgMsgLength.setStatus("mandatory")
_Iso3201SStatsRxMsgsNAKed_Type = Gauge32
_Iso3201SStatsRxMsgsNAKed_Object = MibTableColumn
iso3201SStatsRxMsgsNAKed = _Iso3201SStatsRxMsgsNAKed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1, 19),
    _Iso3201SStatsRxMsgsNAKed_Type()
)
iso3201SStatsRxMsgsNAKed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsRxMsgsNAKed.setStatus("mandatory")
_Iso3201SStatsRxMsgsAborted_Type = Gauge32
_Iso3201SStatsRxMsgsAborted_Object = MibTableColumn
iso3201SStatsRxMsgsAborted = _Iso3201SStatsRxMsgsAborted_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1, 20),
    _Iso3201SStatsRxMsgsAborted_Type()
)
iso3201SStatsRxMsgsAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsRxMsgsAborted.setStatus("mandatory")
_Iso3201SStatsRxSelectsNAKed_Type = Gauge32
_Iso3201SStatsRxSelectsNAKed_Object = MibTableColumn
iso3201SStatsRxSelectsNAKed = _Iso3201SStatsRxSelectsNAKed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1, 21),
    _Iso3201SStatsRxSelectsNAKed_Type()
)
iso3201SStatsRxSelectsNAKed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsRxSelectsNAKed.setStatus("mandatory")
_Iso3201SStatsRxInvRespToSelect_Type = Counter32
_Iso3201SStatsRxInvRespToSelect_Object = MibTableColumn
iso3201SStatsRxInvRespToSelect = _Iso3201SStatsRxInvRespToSelect_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1, 22),
    _Iso3201SStatsRxInvRespToSelect_Type()
)
iso3201SStatsRxInvRespToSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsRxInvRespToSelect.setStatus("mandatory")
_Iso3201SStatsRxNAKRetryExhausted_Type = Counter32
_Iso3201SStatsRxNAKRetryExhausted_Object = MibTableColumn
iso3201SStatsRxNAKRetryExhausted = _Iso3201SStatsRxNAKRetryExhausted_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1, 23),
    _Iso3201SStatsRxNAKRetryExhausted_Type()
)
iso3201SStatsRxNAKRetryExhausted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsRxNAKRetryExhausted.setStatus("mandatory")
_Iso3201SStatsRxENQs_Type = Gauge32
_Iso3201SStatsRxENQs_Object = MibTableColumn
iso3201SStatsRxENQs = _Iso3201SStatsRxENQs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1, 24),
    _Iso3201SStatsRxENQs_Type()
)
iso3201SStatsRxENQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsRxENQs.setStatus("mandatory")
_Iso3201SStatsRxENQRetryExhausted_Type = Counter32
_Iso3201SStatsRxENQRetryExhausted_Object = MibTableColumn
iso3201SStatsRxENQRetryExhausted = _Iso3201SStatsRxENQRetryExhausted_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1, 25),
    _Iso3201SStatsRxENQRetryExhausted_Type()
)
iso3201SStatsRxENQRetryExhausted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsRxENQRetryExhausted.setStatus("mandatory")
_Iso3201SStatsRxInterChrTimeout_Type = Counter32
_Iso3201SStatsRxInterChrTimeout_Object = MibTableColumn
iso3201SStatsRxInterChrTimeout = _Iso3201SStatsRxInterChrTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1, 26),
    _Iso3201SStatsRxInterChrTimeout_Type()
)
iso3201SStatsRxInterChrTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsRxInterChrTimeout.setStatus("mandatory")
_Iso3201SStatsRxPollTimeout_Type = Gauge32
_Iso3201SStatsRxPollTimeout_Object = MibTableColumn
iso3201SStatsRxPollTimeout = _Iso3201SStatsRxPollTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1, 27),
    _Iso3201SStatsRxPollTimeout_Type()
)
iso3201SStatsRxPollTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsRxPollTimeout.setStatus("mandatory")
_Iso3201SStatsRxSelectTimeout_Type = Gauge32
_Iso3201SStatsRxSelectTimeout_Object = MibTableColumn
iso3201SStatsRxSelectTimeout = _Iso3201SStatsRxSelectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1, 28),
    _Iso3201SStatsRxSelectTimeout_Type()
)
iso3201SStatsRxSelectTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsRxSelectTimeout.setStatus("mandatory")
_Iso3201SStatsRxReceiveTimeout_Type = Counter32
_Iso3201SStatsRxReceiveTimeout_Object = MibTableColumn
iso3201SStatsRxReceiveTimeout = _Iso3201SStatsRxReceiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1, 29),
    _Iso3201SStatsRxReceiveTimeout_Type()
)
iso3201SStatsRxReceiveTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsRxReceiveTimeout.setStatus("mandatory")
_Iso3201SStatsRxParityErrorsOnCntrl_Type = Gauge32
_Iso3201SStatsRxParityErrorsOnCntrl_Object = MibTableColumn
iso3201SStatsRxParityErrorsOnCntrl = _Iso3201SStatsRxParityErrorsOnCntrl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 6, 3, 1, 30),
    _Iso3201SStatsRxParityErrorsOnCntrl_Type()
)
iso3201SStatsRxParityErrorsOnCntrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iso3201SStatsRxParityErrorsOnCntrl.setStatus("mandatory")
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)
_Cdx6500Cont3201Table_ObjectIdentity = ObjectIdentity
cdx6500Cont3201Table = _Cdx6500Cont3201Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 11)
)
_Cdx6500Cont3201PortTable_Object = MibTable
cdx6500Cont3201PortTable = _Cdx6500Cont3201PortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 11, 1)
)
if mibBuilder.loadTexts:
    cdx6500Cont3201PortTable.setStatus("mandatory")
_Cdx6500Cont3201PortEntry_Object = MibTableRow
cdx6500Cont3201PortEntry = _Cdx6500Cont3201PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 11, 1, 1)
)
cdx6500Cont3201PortEntry.setIndexNames(
    (0, "ISO3201-OPT-MIB", "iso3201PContPortNum"),
)
if mibBuilder.loadTexts:
    cdx6500Cont3201PortEntry.setStatus("mandatory")


class _Iso3201PContPortNum_Type(Integer32):
    """Custom type iso3201PContPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Iso3201PContPortNum_Type.__name__ = "Integer32"
_Iso3201PContPortNum_Object = MibTableColumn
iso3201PContPortNum = _Iso3201PContPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 11, 1, 1, 1),
    _Iso3201PContPortNum_Type()
)
iso3201PContPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iso3201PContPortNum.setStatus("mandatory")


class _Iso3201ContPortBoot_Type(Integer32):
    """Custom type iso3201ContPortBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boot", 1),
          ("noBoot", 2))
    )


_Iso3201ContPortBoot_Type.__name__ = "Integer32"
_Iso3201ContPortBoot_Object = MibTableColumn
iso3201ContPortBoot = _Iso3201ContPortBoot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 11, 1, 1, 2),
    _Iso3201ContPortBoot_Type()
)
iso3201ContPortBoot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    iso3201ContPortBoot.setStatus("mandatory")


class _Iso3201ContPortEnable_Type(Integer32):
    """Custom type iso3201ContPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("noEnable", 2))
    )


_Iso3201ContPortEnable_Type.__name__ = "Integer32"
_Iso3201ContPortEnable_Object = MibTableColumn
iso3201ContPortEnable = _Iso3201ContPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 11, 1, 1, 3),
    _Iso3201ContPortEnable_Type()
)
iso3201ContPortEnable.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    iso3201ContPortEnable.setStatus("mandatory")


class _Iso3201ContPortDisable_Type(Integer32):
    """Custom type iso3201ContPortDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("noDisable", 2))
    )


_Iso3201ContPortDisable_Type.__name__ = "Integer32"
_Iso3201ContPortDisable_Object = MibTableColumn
iso3201ContPortDisable = _Iso3201ContPortDisable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 11, 1, 1, 4),
    _Iso3201ContPortDisable_Type()
)
iso3201ContPortDisable.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    iso3201ContPortDisable.setStatus("mandatory")


class _Iso3201ContPortResetStats_Type(Integer32):
    """Custom type iso3201ContPortResetStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noreset", 2),
          ("reset", 1))
    )


_Iso3201ContPortResetStats_Type.__name__ = "Integer32"
_Iso3201ContPortResetStats_Object = MibTableColumn
iso3201ContPortResetStats = _Iso3201ContPortResetStats_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 11, 1, 1, 5),
    _Iso3201ContPortResetStats_Type()
)
iso3201ContPortResetStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    iso3201ContPortResetStats.setStatus("mandatory")
_Cdx6500Cont3201StnTable_Object = MibTable
cdx6500Cont3201StnTable = _Cdx6500Cont3201StnTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 11, 2)
)
if mibBuilder.loadTexts:
    cdx6500Cont3201StnTable.setStatus("mandatory")
_Cdx6500Cont3201StnEntry_Object = MibTableRow
cdx6500Cont3201StnEntry = _Cdx6500Cont3201StnEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 11, 2, 1)
)
cdx6500Cont3201StnEntry.setIndexNames(
    (0, "ISO3201-OPT-MIB", "iso3201SContPortNum"),
    (0, "ISO3201-OPT-MIB", "iso3201ContStnNum"),
)
if mibBuilder.loadTexts:
    cdx6500Cont3201StnEntry.setStatus("mandatory")


class _Iso3201SContPortNum_Type(Integer32):
    """Custom type iso3201SContPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Iso3201SContPortNum_Type.__name__ = "Integer32"
_Iso3201SContPortNum_Object = MibTableColumn
iso3201SContPortNum = _Iso3201SContPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 11, 2, 1, 1),
    _Iso3201SContPortNum_Type()
)
iso3201SContPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iso3201SContPortNum.setStatus("mandatory")


class _Iso3201ContStnNum_Type(Integer32):
    """Custom type iso3201ContStnNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Iso3201ContStnNum_Type.__name__ = "Integer32"
_Iso3201ContStnNum_Object = MibTableColumn
iso3201ContStnNum = _Iso3201ContStnNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 11, 2, 1, 2),
    _Iso3201ContStnNum_Type()
)
iso3201ContStnNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iso3201ContStnNum.setStatus("mandatory")


class _Iso3201ContStnBoot_Type(Integer32):
    """Custom type iso3201ContStnBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boot", 1),
          ("noBoot", 2))
    )


_Iso3201ContStnBoot_Type.__name__ = "Integer32"
_Iso3201ContStnBoot_Object = MibTableColumn
iso3201ContStnBoot = _Iso3201ContStnBoot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 11, 2, 1, 3),
    _Iso3201ContStnBoot_Type()
)
iso3201ContStnBoot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    iso3201ContStnBoot.setStatus("mandatory")


class _Iso3201ContStnEnable_Type(Integer32):
    """Custom type iso3201ContStnEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("noEnable", 2))
    )


_Iso3201ContStnEnable_Type.__name__ = "Integer32"
_Iso3201ContStnEnable_Object = MibTableColumn
iso3201ContStnEnable = _Iso3201ContStnEnable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 11, 2, 1, 4),
    _Iso3201ContStnEnable_Type()
)
iso3201ContStnEnable.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    iso3201ContStnEnable.setStatus("mandatory")


class _Iso3201ContStnDisable_Type(Integer32):
    """Custom type iso3201ContStnDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("noDisable", 2))
    )


_Iso3201ContStnDisable_Type.__name__ = "Integer32"
_Iso3201ContStnDisable_Object = MibTableColumn
iso3201ContStnDisable = _Iso3201ContStnDisable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 11, 2, 1, 5),
    _Iso3201ContStnDisable_Type()
)
iso3201ContStnDisable.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    iso3201ContStnDisable.setStatus("mandatory")


class _Iso3201ContStnResetStats_Type(Integer32):
    """Custom type iso3201ContStnResetStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 2),
          ("reset", 1))
    )


_Iso3201ContStnResetStats_Type.__name__ = "Integer32"
_Iso3201ContStnResetStats_Object = MibTableColumn
iso3201ContStnResetStats = _Iso3201ContStnResetStats_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 11, 2, 1, 6),
    _Iso3201ContStnResetStats_Type()
)
iso3201ContStnResetStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    iso3201ContStnResetStats.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ISO3201-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PPCT3201PortTable": cdx6500PPCT3201PortTable,
       "cdx6500PPCT3201PortEntry": cdx6500PPCT3201PortEntry,
       "iso3201PCfgPortNum": iso3201PCfgPortNum,
       "iso3201PCfgPortType": iso3201PCfgPortType,
       "iso3201PCfgPortSpeed": iso3201PCfgPortSpeed,
       "iso3201PCfgNoOfControllers": iso3201PCfgNoOfControllers,
       "iso3201PCfgResponseTimeout": iso3201PCfgResponseTimeout,
       "iso3201PCfgInterChrTimeout": iso3201PCfgInterChrTimeout,
       "iso3201PCfgNoOfRetries": iso3201PCfgNoOfRetries,
       "iso3201PCfgNoOfConsecRetries": iso3201PCfgNoOfConsecRetries,
       "iso3201PCfgSlowPollWaitCycle": iso3201PCfgSlowPollWaitCycle,
       "iso3201PCfgElectricalInterfaceType": iso3201PCfgElectricalInterfaceType,
       "iso3201PCfgV24ElectricalInterfaceOption": iso3201PCfgV24ElectricalInterfaceOption,
       "iso3201PCfgHighSpeedElectricalInterfaceOption": iso3201PCfgHighSpeedElectricalInterfaceOption,
       "cdx6500PCTStationProtocolGroup": cdx6500PCTStationProtocolGroup,
       "cdx6500SPCT3201StnTable": cdx6500SPCT3201StnTable,
       "cdx6500SPCT3201StnEntry": cdx6500SPCT3201StnEntry,
       "iso3201SCfgPortNum": iso3201SCfgPortNum,
       "iso3201SCfgStnNum": iso3201SCfgStnNum,
       "iso3201SCfgControllerAddress": iso3201SCfgControllerAddress,
       "iso3201SCfgAutocallMnemonic": iso3201SCfgAutocallMnemonic,
       "iso3201SCfgAutocallTimeout": iso3201SCfgAutocallTimeout,
       "iso3201SCfgMaxNoAutocallAttempts": iso3201SCfgMaxNoAutocallAttempts,
       "iso3201SCfgX25Address": iso3201SCfgX25Address,
       "iso3201SCfgBillingRecords": iso3201SCfgBillingRecords,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PPST3201PStatsTable": cdx6500PPST3201PStatsTable,
       "cdx6500PPST3201PStatsEntry": cdx6500PPST3201PStatsEntry,
       "iso3201PStatsPortNum": iso3201PStatsPortNum,
       "iso3201PStatsPortStatus": iso3201PStatsPortStatus,
       "iso3201PStatsPortType": iso3201PStatsPortType,
       "iso3201PStatsPortSpeed": iso3201PStatsPortSpeed,
       "iso3201PStatsPortUtilIn": iso3201PStatsPortUtilIn,
       "iso3201PStatsPortUtilOut": iso3201PStatsPortUtilOut,
       "iso3201PStatsLineStatus": iso3201PStatsLineStatus,
       "iso3201PStatsTxChrs": iso3201PStatsTxChrs,
       "iso3201PStatsTxMsgs": iso3201PStatsTxMsgs,
       "iso3201PStatsTxPolls": iso3201PStatsTxPolls,
       "iso3201PStatsTxSelects": iso3201PStatsTxSelects,
       "iso3201PStatsTxACKs": iso3201PStatsTxACKs,
       "iso3201PStatsTxNAKs": iso3201PStatsTxNAKs,
       "iso3201PStatsTxENQs": iso3201PStatsTxENQs,
       "iso3201PStatsRxChrs": iso3201PStatsRxChrs,
       "iso3201PStatsRxMsgs": iso3201PStatsRxMsgs,
       "iso3201PStatsRxACKs": iso3201PStatsRxACKs,
       "iso3201PStatsRxNAKs": iso3201PStatsRxNAKs,
       "iso3201PStatsRxENQs": iso3201PStatsRxENQs,
       "cdx6500PSTStationProtocolGroup": cdx6500PSTStationProtocolGroup,
       "cdx6500SPST3201StnTable": cdx6500SPST3201StnTable,
       "cdx6500SPST3201SStatsTable": cdx6500SPST3201SStatsTable,
       "cdx6500SPST3201StnEntry": cdx6500SPST3201StnEntry,
       "iso3201SStatsPortNum": iso3201SStatsPortNum,
       "iso3201SStatsStnNum": iso3201SStatsStnNum,
       "iso3201SStatsControllerAddress": iso3201SStatsControllerAddress,
       "iso3201SStatsStnState": iso3201SStatsStnState,
       "iso3201SStatsCurrentStatus": iso3201SStatsCurrentStatus,
       "iso3201SStatsNoOfAutocallAttmpts": iso3201SStatsNoOfAutocallAttmpts,
       "iso3201SStatsNxtAutocallAttmpt": iso3201SStatsNxtAutocallAttmpt,
       "iso3201SStatsLastClearCauseCode": iso3201SStatsLastClearCauseCode,
       "iso3201SStatsLastClearDiagCode": iso3201SStatsLastClearDiagCode,
       "iso3201SStatsLastInCalledAddress": iso3201SStatsLastInCalledAddress,
       "iso3201SStatsLastInCallingAddress": iso3201SStatsLastInCallingAddress,
       "iso3201SStatsLastInCallFacilities": iso3201SStatsLastInCallFacilities,
       "iso3201SStatsLastInCallCUD": iso3201SStatsLastInCallCUD,
       "iso3201SStatsLastOutCalledAddress": iso3201SStatsLastOutCalledAddress,
       "iso3201SStatsLastOutCallingAddress": iso3201SStatsLastOutCallingAddress,
       "iso3201SStatsLastOutCallFacilities": iso3201SStatsLastOutCallFacilities,
       "iso3201SStatsLastOutCallCUD": iso3201SStatsLastOutCallCUD,
       "cdx6500SPST3201PktSummTable": cdx6500SPST3201PktSummTable,
       "cdx6500SPST3201PktSummEntry": cdx6500SPST3201PktSummEntry,
       "iso3201SStatsPktSummPortNum": iso3201SStatsPktSummPortNum,
       "iso3201SStatsPktSummStnNum": iso3201SStatsPktSummStnNum,
       "iso3201SStatsTxData": iso3201SStatsTxData,
       "iso3201SStatsTxCallRequest": iso3201SStatsTxCallRequest,
       "iso3201SStatsTxCallAccept": iso3201SStatsTxCallAccept,
       "iso3201SStatsTxClearRequest": iso3201SStatsTxClearRequest,
       "iso3201SStatsTxClearConfirm": iso3201SStatsTxClearConfirm,
       "iso3201SStatsTxResetRequest": iso3201SStatsTxResetRequest,
       "iso3201SStatsTxResetConfirm": iso3201SStatsTxResetConfirm,
       "iso3201SStatsTxWindowClosed": iso3201SStatsTxWindowClosed,
       "iso3201SStatsRxData": iso3201SStatsRxData,
       "iso3201SStatsRxCallRequest": iso3201SStatsRxCallRequest,
       "iso3201SStatsRxCallAccept": iso3201SStatsRxCallAccept,
       "iso3201SStatsRxClearRequest": iso3201SStatsRxClearRequest,
       "iso3201SStatsRxClearConfirm": iso3201SStatsRxClearConfirm,
       "iso3201SStatsRxResetRequest": iso3201SStatsRxResetRequest,
       "iso3201SStatsRxResetConfirm": iso3201SStatsRxResetConfirm,
       "iso3201SStatsRxWindowClosed": iso3201SStatsRxWindowClosed,
       "cdx6500SPST3201SummTable": cdx6500SPST3201SummTable,
       "cdx6500SPST3201SummEntry": cdx6500SPST3201SummEntry,
       "iso3201SStatsSummPortNum": iso3201SStatsSummPortNum,
       "iso3201SStatsSummStnNum": iso3201SStatsSummStnNum,
       "iso3201SStatsTxPolls": iso3201SStatsTxPolls,
       "iso3201SStatsTxSelects": iso3201SStatsTxSelects,
       "iso3201SStatsTxDataBytes": iso3201SStatsTxDataBytes,
       "iso3201SStatsTxDataMsgs": iso3201SStatsTxDataMsgs,
       "iso3201SStatsTxDataMsgsPerHour": iso3201SStatsTxDataMsgsPerHour,
       "iso3201SStatsTxAvgMsgLength": iso3201SStatsTxAvgMsgLength,
       "iso3201SStatsTxMsgsNAKed": iso3201SStatsTxMsgsNAKed,
       "iso3201SStatsTxSelectRetryExhausted": iso3201SStatsTxSelectRetryExhausted,
       "iso3201SStatsTxNAKRetryExhausted": iso3201SStatsTxNAKRetryExhausted,
       "iso3201SStatsTxENQs": iso3201SStatsTxENQs,
       "iso3201SStatsTxENQRetryExhausted": iso3201SStatsTxENQRetryExhausted,
       "iso3201SStatsTxPollingSuspendedByHost": iso3201SStatsTxPollingSuspendedByHost,
       "iso3201SStatsRxDataBytes": iso3201SStatsRxDataBytes,
       "iso3201SStatsRxDataMsgs": iso3201SStatsRxDataMsgs,
       "iso3201SStatsRxDataMsgsPerHour": iso3201SStatsRxDataMsgsPerHour,
       "iso3201SStatsRxAvgMsgLength": iso3201SStatsRxAvgMsgLength,
       "iso3201SStatsRxMsgsNAKed": iso3201SStatsRxMsgsNAKed,
       "iso3201SStatsRxMsgsAborted": iso3201SStatsRxMsgsAborted,
       "iso3201SStatsRxSelectsNAKed": iso3201SStatsRxSelectsNAKed,
       "iso3201SStatsRxInvRespToSelect": iso3201SStatsRxInvRespToSelect,
       "iso3201SStatsRxNAKRetryExhausted": iso3201SStatsRxNAKRetryExhausted,
       "iso3201SStatsRxENQs": iso3201SStatsRxENQs,
       "iso3201SStatsRxENQRetryExhausted": iso3201SStatsRxENQRetryExhausted,
       "iso3201SStatsRxInterChrTimeout": iso3201SStatsRxInterChrTimeout,
       "iso3201SStatsRxPollTimeout": iso3201SStatsRxPollTimeout,
       "iso3201SStatsRxSelectTimeout": iso3201SStatsRxSelectTimeout,
       "iso3201SStatsRxReceiveTimeout": iso3201SStatsRxReceiveTimeout,
       "iso3201SStatsRxParityErrorsOnCntrl": iso3201SStatsRxParityErrorsOnCntrl,
       "cdx6500Controls": cdx6500Controls,
       "cdx6500Cont3201Table": cdx6500Cont3201Table,
       "cdx6500Cont3201PortTable": cdx6500Cont3201PortTable,
       "cdx6500Cont3201PortEntry": cdx6500Cont3201PortEntry,
       "iso3201PContPortNum": iso3201PContPortNum,
       "iso3201ContPortBoot": iso3201ContPortBoot,
       "iso3201ContPortEnable": iso3201ContPortEnable,
       "iso3201ContPortDisable": iso3201ContPortDisable,
       "iso3201ContPortResetStats": iso3201ContPortResetStats,
       "cdx6500Cont3201StnTable": cdx6500Cont3201StnTable,
       "cdx6500Cont3201StnEntry": cdx6500Cont3201StnEntry,
       "iso3201SContPortNum": iso3201SContPortNum,
       "iso3201ContStnNum": iso3201ContStnNum,
       "iso3201ContStnBoot": iso3201ContStnBoot,
       "iso3201ContStnEnable": iso3201ContStnEnable,
       "iso3201ContStnDisable": iso3201ContStnDisable,
       "iso3201ContStnResetStats": iso3201ContStnResetStats}
)
