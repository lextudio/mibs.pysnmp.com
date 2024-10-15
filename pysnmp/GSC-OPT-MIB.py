# SNMP MIB module (GSC-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GSC-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:55 2024
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
_Cdx6500PPCTGSCPortTable_Object = MibTable
cdx6500PPCTGSCPortTable = _Cdx6500PPCTGSCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 29)
)
if mibBuilder.loadTexts:
    cdx6500PPCTGSCPortTable.setStatus("mandatory")
_Cdx6500PPCTGSCPortEntry_Object = MibTableRow
cdx6500PPCTGSCPortEntry = _Cdx6500PPCTGSCPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 29, 1)
)
cdx6500PPCTGSCPortEntry.setIndexNames(
    (0, "GSC-OPT-MIB", "cdx6500GSCPCfgPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPCTGSCPortEntry.setStatus("mandatory")


class _Cdx6500GSCPCfgPortNumber_Type(Integer32):
    """Custom type cdx6500GSCPCfgPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500GSCPCfgPortNumber_Type.__name__ = "Integer32"
_Cdx6500GSCPCfgPortNumber_Object = MibTableColumn
cdx6500GSCPCfgPortNumber = _Cdx6500GSCPCfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 29, 1, 1),
    _Cdx6500GSCPCfgPortNumber_Type()
)
cdx6500GSCPCfgPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPCfgPortNumber.setStatus("mandatory")


class _Cdx6500GSCPCfgPortType_Type(Integer32):
    """Custom type cdx6500GSCPCfgPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            51
        )
    )
    namedValues = NamedValues(
        ("gsc", 51)
    )


_Cdx6500GSCPCfgPortType_Type.__name__ = "Integer32"
_Cdx6500GSCPCfgPortType_Object = MibTableColumn
cdx6500GSCPCfgPortType = _Cdx6500GSCPCfgPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 29, 1, 2),
    _Cdx6500GSCPCfgPortType_Type()
)
cdx6500GSCPCfgPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPCfgPortType.setStatus("mandatory")


class _Cdx6500GSCPCfgSubtype_Type(Integer32):
    """Custom type cdx6500GSCPCfgSubtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gscHpad", 2),
          ("gscTpad", 1))
    )


_Cdx6500GSCPCfgSubtype_Type.__name__ = "Integer32"
_Cdx6500GSCPCfgSubtype_Object = MibTableColumn
cdx6500GSCPCfgSubtype = _Cdx6500GSCPCfgSubtype_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 29, 1, 3),
    _Cdx6500GSCPCfgSubtype_Type()
)
cdx6500GSCPCfgSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPCfgSubtype.setStatus("mandatory")


class _Cdx6500GSCPCfgClockSpeed_Type(Integer32):
    """Custom type cdx6500GSCPCfgClockSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              8,
              13,
              14,
              15,
              16,
              100)
        )
    )
    namedValues = NamedValues(
        *(("nc", 100),
          ("speed1200", 4),
          ("speed1800", 8),
          ("speed19200", 16),
          ("speed2400", 13),
          ("speed4800", 14),
          ("speed9600", 15))
    )


_Cdx6500GSCPCfgClockSpeed_Type.__name__ = "Integer32"
_Cdx6500GSCPCfgClockSpeed_Object = MibTableColumn
cdx6500GSCPCfgClockSpeed = _Cdx6500GSCPCfgClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 29, 1, 4),
    _Cdx6500GSCPCfgClockSpeed_Type()
)
cdx6500GSCPCfgClockSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPCfgClockSpeed.setStatus("mandatory")


class _Cdx6500GSCPCfgNumStations_Type(Integer32):
    """Custom type cdx6500GSCPCfgNumStations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Cdx6500GSCPCfgNumStations_Type.__name__ = "Integer32"
_Cdx6500GSCPCfgNumStations_Object = MibTableColumn
cdx6500GSCPCfgNumStations = _Cdx6500GSCPCfgNumStations_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 29, 1, 5),
    _Cdx6500GSCPCfgNumStations_Type()
)
cdx6500GSCPCfgNumStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPCfgNumStations.setStatus("mandatory")


class _Cdx6500GSCPCfgMinPollPeriod_Type(Integer32):
    """Custom type cdx6500GSCPCfgMinPollPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Cdx6500GSCPCfgMinPollPeriod_Type.__name__ = "Integer32"
_Cdx6500GSCPCfgMinPollPeriod_Object = MibTableColumn
cdx6500GSCPCfgMinPollPeriod = _Cdx6500GSCPCfgMinPollPeriod_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 29, 1, 6),
    _Cdx6500GSCPCfgMinPollPeriod_Type()
)
cdx6500GSCPCfgMinPollPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPCfgMinPollPeriod.setStatus("mandatory")


class _Cdx6500GSCPCfgPollRespTimer_Type(Integer32):
    """Custom type cdx6500GSCPCfgPollRespTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Cdx6500GSCPCfgPollRespTimer_Type.__name__ = "Integer32"
_Cdx6500GSCPCfgPollRespTimer_Object = MibTableColumn
cdx6500GSCPCfgPollRespTimer = _Cdx6500GSCPCfgPollRespTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 29, 1, 7),
    _Cdx6500GSCPCfgPollRespTimer_Type()
)
cdx6500GSCPCfgPollRespTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPCfgPollRespTimer.setStatus("mandatory")


class _Cdx6500GSCPCfgAckTimeOut_Type(Integer32):
    """Custom type cdx6500GSCPCfgAckTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Cdx6500GSCPCfgAckTimeOut_Type.__name__ = "Integer32"
_Cdx6500GSCPCfgAckTimeOut_Object = MibTableColumn
cdx6500GSCPCfgAckTimeOut = _Cdx6500GSCPCfgAckTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 29, 1, 8),
    _Cdx6500GSCPCfgAckTimeOut_Type()
)
cdx6500GSCPCfgAckTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPCfgAckTimeOut.setStatus("mandatory")


class _Cdx6500GSCPCfgInterCharTimeOut_Type(Integer32):
    """Custom type cdx6500GSCPCfgInterCharTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Cdx6500GSCPCfgInterCharTimeOut_Type.__name__ = "Integer32"
_Cdx6500GSCPCfgInterCharTimeOut_Object = MibTableColumn
cdx6500GSCPCfgInterCharTimeOut = _Cdx6500GSCPCfgInterCharTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 29, 1, 9),
    _Cdx6500GSCPCfgInterCharTimeOut_Type()
)
cdx6500GSCPCfgInterCharTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPCfgInterCharTimeOut.setStatus("mandatory")


class _Cdx6500GSCPCfgBroadcastHoldTimeOut_Type(Integer32):
    """Custom type cdx6500GSCPCfgBroadcastHoldTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Cdx6500GSCPCfgBroadcastHoldTimeOut_Type.__name__ = "Integer32"
_Cdx6500GSCPCfgBroadcastHoldTimeOut_Object = MibTableColumn
cdx6500GSCPCfgBroadcastHoldTimeOut = _Cdx6500GSCPCfgBroadcastHoldTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 29, 1, 10),
    _Cdx6500GSCPCfgBroadcastHoldTimeOut_Type()
)
cdx6500GSCPCfgBroadcastHoldTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPCfgBroadcastHoldTimeOut.setStatus("mandatory")


class _Cdx6500GSCPCfgSolicitedTimeOut_Type(Integer32):
    """Custom type cdx6500GSCPCfgSolicitedTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Cdx6500GSCPCfgSolicitedTimeOut_Type.__name__ = "Integer32"
_Cdx6500GSCPCfgSolicitedTimeOut_Object = MibTableColumn
cdx6500GSCPCfgSolicitedTimeOut = _Cdx6500GSCPCfgSolicitedTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 29, 1, 11),
    _Cdx6500GSCPCfgSolicitedTimeOut_Type()
)
cdx6500GSCPCfgSolicitedTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPCfgSolicitedTimeOut.setStatus("mandatory")


class _Cdx6500GSCPCfgIdleDiscTimeOut_Type(Integer32):
    """Custom type cdx6500GSCPCfgIdleDiscTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Cdx6500GSCPCfgIdleDiscTimeOut_Type.__name__ = "Integer32"
_Cdx6500GSCPCfgIdleDiscTimeOut_Object = MibTableColumn
cdx6500GSCPCfgIdleDiscTimeOut = _Cdx6500GSCPCfgIdleDiscTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 29, 1, 12),
    _Cdx6500GSCPCfgIdleDiscTimeOut_Type()
)
cdx6500GSCPCfgIdleDiscTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPCfgIdleDiscTimeOut.setStatus("mandatory")


class _Cdx6500GSCPCfgAutocallRetryTimeOut_Type(Integer32):
    """Custom type cdx6500GSCPCfgAutocallRetryTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Cdx6500GSCPCfgAutocallRetryTimeOut_Type.__name__ = "Integer32"
_Cdx6500GSCPCfgAutocallRetryTimeOut_Object = MibTableColumn
cdx6500GSCPCfgAutocallRetryTimeOut = _Cdx6500GSCPCfgAutocallRetryTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 29, 1, 13),
    _Cdx6500GSCPCfgAutocallRetryTimeOut_Type()
)
cdx6500GSCPCfgAutocallRetryTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPCfgAutocallRetryTimeOut.setStatus("mandatory")


class _Cdx6500GSCPCfgMaxAutocallRetries_Type(Integer32):
    """Custom type cdx6500GSCPCfgMaxAutocallRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Cdx6500GSCPCfgMaxAutocallRetries_Type.__name__ = "Integer32"
_Cdx6500GSCPCfgMaxAutocallRetries_Object = MibTableColumn
cdx6500GSCPCfgMaxAutocallRetries = _Cdx6500GSCPCfgMaxAutocallRetries_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 29, 1, 14),
    _Cdx6500GSCPCfgMaxAutocallRetries_Type()
)
cdx6500GSCPCfgMaxAutocallRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPCfgMaxAutocallRetries.setStatus("mandatory")


class _Cdx6500GSCPCfgN1_Type(Integer32):
    """Custom type cdx6500GSCPCfgN1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Cdx6500GSCPCfgN1_Type.__name__ = "Integer32"
_Cdx6500GSCPCfgN1_Object = MibTableColumn
cdx6500GSCPCfgN1 = _Cdx6500GSCPCfgN1_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 29, 1, 15),
    _Cdx6500GSCPCfgN1_Type()
)
cdx6500GSCPCfgN1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPCfgN1.setStatus("mandatory")


class _Cdx6500GSCPCfgN2_Type(Integer32):
    """Custom type cdx6500GSCPCfgN2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Cdx6500GSCPCfgN2_Type.__name__ = "Integer32"
_Cdx6500GSCPCfgN2_Object = MibTableColumn
cdx6500GSCPCfgN2 = _Cdx6500GSCPCfgN2_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 29, 1, 16),
    _Cdx6500GSCPCfgN2_Type()
)
cdx6500GSCPCfgN2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPCfgN2.setStatus("mandatory")


class _Cdx6500GSCPCfgNumRetries_Type(Integer32):
    """Custom type cdx6500GSCPCfgNumRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Cdx6500GSCPCfgNumRetries_Type.__name__ = "Integer32"
_Cdx6500GSCPCfgNumRetries_Object = MibTableColumn
cdx6500GSCPCfgNumRetries = _Cdx6500GSCPCfgNumRetries_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 29, 1, 17),
    _Cdx6500GSCPCfgNumRetries_Type()
)
cdx6500GSCPCfgNumRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPCfgNumRetries.setStatus("mandatory")


class _Cdx6500GSCPCfgPortAddress_Type(DisplayString):
    """Custom type cdx6500GSCPCfgPortAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500GSCPCfgPortAddress_Type.__name__ = "DisplayString"
_Cdx6500GSCPCfgPortAddress_Object = MibTableColumn
cdx6500GSCPCfgPortAddress = _Cdx6500GSCPCfgPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 29, 1, 18),
    _Cdx6500GSCPCfgPortAddress_Type()
)
cdx6500GSCPCfgPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPCfgPortAddress.setStatus("mandatory")
_Cdx6500GSCPCfgPortOptions_Type = DisplayString
_Cdx6500GSCPCfgPortOptions_Object = MibTableColumn
cdx6500GSCPCfgPortOptions = _Cdx6500GSCPCfgPortOptions_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 29, 1, 19),
    _Cdx6500GSCPCfgPortOptions_Type()
)
cdx6500GSCPCfgPortOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPCfgPortOptions.setStatus("mandatory")


class _Cdx6500GSCPCfgConnType_Type(Integer32):
    """Custom type cdx6500GSCPCfgConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              16,
              100)
        )
    )
    namedValues = NamedValues(
        *(("nc", 100),
          ("simp", 1),
          ("simpa", 16))
    )


_Cdx6500GSCPCfgConnType_Type.__name__ = "Integer32"
_Cdx6500GSCPCfgConnType_Object = MibTableColumn
cdx6500GSCPCfgConnType = _Cdx6500GSCPCfgConnType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 29, 1, 20),
    _Cdx6500GSCPCfgConnType_Type()
)
cdx6500GSCPCfgConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPCfgConnType.setStatus("mandatory")


class _Cdx6500GSCPCfgWakeUpTimer_Type(Integer32):
    """Custom type cdx6500GSCPCfgWakeUpTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_Cdx6500GSCPCfgWakeUpTimer_Type.__name__ = "Integer32"
_Cdx6500GSCPCfgWakeUpTimer_Object = MibTableColumn
cdx6500GSCPCfgWakeUpTimer = _Cdx6500GSCPCfgWakeUpTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 29, 1, 21),
    _Cdx6500GSCPCfgWakeUpTimer_Type()
)
cdx6500GSCPCfgWakeUpTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPCfgWakeUpTimer.setStatus("mandatory")


class _Cdx6500GSCPCfgElectricalInterfaceType_Type(Integer32):
    """Custom type cdx6500GSCPCfgElectricalInterfaceType based on Integer32"""
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


_Cdx6500GSCPCfgElectricalInterfaceType_Type.__name__ = "Integer32"
_Cdx6500GSCPCfgElectricalInterfaceType_Object = MibTableColumn
cdx6500GSCPCfgElectricalInterfaceType = _Cdx6500GSCPCfgElectricalInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 29, 1, 22),
    _Cdx6500GSCPCfgElectricalInterfaceType_Type()
)
cdx6500GSCPCfgElectricalInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPCfgElectricalInterfaceType.setStatus("mandatory")


class _Cdx6500GSCPCfgV24ElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500GSCPCfgV24ElectricalInterfaceOption based on Integer32"""
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


_Cdx6500GSCPCfgV24ElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500GSCPCfgV24ElectricalInterfaceOption_Object = MibTableColumn
cdx6500GSCPCfgV24ElectricalInterfaceOption = _Cdx6500GSCPCfgV24ElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 29, 1, 23),
    _Cdx6500GSCPCfgV24ElectricalInterfaceOption_Type()
)
cdx6500GSCPCfgV24ElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPCfgV24ElectricalInterfaceOption.setStatus("mandatory")


class _Cdx6500GSCPCfgHighSpeedElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500GSCPCfgHighSpeedElectricalInterfaceOption based on Integer32"""
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


_Cdx6500GSCPCfgHighSpeedElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500GSCPCfgHighSpeedElectricalInterfaceOption_Object = MibTableColumn
cdx6500GSCPCfgHighSpeedElectricalInterfaceOption = _Cdx6500GSCPCfgHighSpeedElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 29, 1, 24),
    _Cdx6500GSCPCfgHighSpeedElectricalInterfaceOption_Type()
)
cdx6500GSCPCfgHighSpeedElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPCfgHighSpeedElectricalInterfaceOption.setStatus("mandatory")
_Cdx6500PCTStationProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTStationProtocolGroup = _Cdx6500PCTStationProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3)
)
_Cdx6500SPCTGSCStationTable_Object = MibTable
cdx6500SPCTGSCStationTable = _Cdx6500SPCTGSCStationTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 8)
)
if mibBuilder.loadTexts:
    cdx6500SPCTGSCStationTable.setStatus("mandatory")
_Cdx6500SPCTGSCStationEntry_Object = MibTableRow
cdx6500SPCTGSCStationEntry = _Cdx6500SPCTGSCStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 8, 1)
)
cdx6500SPCTGSCStationEntry.setIndexNames(
    (0, "GSC-OPT-MIB", "cdx6500GSCSCfgPortNumber"),
    (0, "GSC-OPT-MIB", "cdx6500GSCSCfgStationNumber"),
)
if mibBuilder.loadTexts:
    cdx6500SPCTGSCStationEntry.setStatus("mandatory")


class _Cdx6500GSCSCfgPortNumber_Type(Integer32):
    """Custom type cdx6500GSCSCfgPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500GSCSCfgPortNumber_Type.__name__ = "Integer32"
_Cdx6500GSCSCfgPortNumber_Object = MibTableColumn
cdx6500GSCSCfgPortNumber = _Cdx6500GSCSCfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 8, 1, 1),
    _Cdx6500GSCSCfgPortNumber_Type()
)
cdx6500GSCSCfgPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSCfgPortNumber.setStatus("mandatory")


class _Cdx6500GSCSCfgStationNumber_Type(Integer32):
    """Custom type cdx6500GSCSCfgStationNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Cdx6500GSCSCfgStationNumber_Type.__name__ = "Integer32"
_Cdx6500GSCSCfgStationNumber_Object = MibTableColumn
cdx6500GSCSCfgStationNumber = _Cdx6500GSCSCfgStationNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 8, 1, 2),
    _Cdx6500GSCSCfgStationNumber_Type()
)
cdx6500GSCSCfgStationNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSCfgStationNumber.setStatus("mandatory")


class _Cdx6500GSCSCfgStationAddress_Type(Integer32):
    """Custom type cdx6500GSCSCfgStationAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 29),
    )


_Cdx6500GSCSCfgStationAddress_Type.__name__ = "Integer32"
_Cdx6500GSCSCfgStationAddress_Object = MibTableColumn
cdx6500GSCSCfgStationAddress = _Cdx6500GSCSCfgStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 8, 1, 3),
    _Cdx6500GSCSCfgStationAddress_Type()
)
cdx6500GSCSCfgStationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSCfgStationAddress.setStatus("mandatory")


class _Cdx6500GSCSCfgRemoteAddress_Type(Integer32):
    """Custom type cdx6500GSCSCfgRemoteAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 29),
    )


_Cdx6500GSCSCfgRemoteAddress_Type.__name__ = "Integer32"
_Cdx6500GSCSCfgRemoteAddress_Object = MibTableColumn
cdx6500GSCSCfgRemoteAddress = _Cdx6500GSCSCfgRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 8, 1, 4),
    _Cdx6500GSCSCfgRemoteAddress_Type()
)
cdx6500GSCSCfgRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSCfgRemoteAddress.setStatus("mandatory")


class _Cdx6500GSCSCfgAutocallMnem_Type(DisplayString):
    """Custom type cdx6500GSCSCfgAutocallMnem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Cdx6500GSCSCfgAutocallMnem_Type.__name__ = "DisplayString"
_Cdx6500GSCSCfgAutocallMnem_Object = MibTableColumn
cdx6500GSCSCfgAutocallMnem = _Cdx6500GSCSCfgAutocallMnem_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 8, 1, 5),
    _Cdx6500GSCSCfgAutocallMnem_Type()
)
cdx6500GSCSCfgAutocallMnem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSCfgAutocallMnem.setStatus("mandatory")
_Cdx6500GSCSCfgProtocolId_Type = DisplayString
_Cdx6500GSCSCfgProtocolId_Object = MibTableColumn
cdx6500GSCSCfgProtocolId = _Cdx6500GSCSCfgProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 8, 1, 6),
    _Cdx6500GSCSCfgProtocolId_Type()
)
cdx6500GSCSCfgProtocolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSCfgProtocolId.setStatus("mandatory")


class _Cdx6500GSCSCfgBillingRecords_Type(Integer32):
    """Custom type cdx6500GSCSCfgBillingRecords based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("billingOff", 1),
          ("billingOn", 2))
    )


_Cdx6500GSCSCfgBillingRecords_Type.__name__ = "Integer32"
_Cdx6500GSCSCfgBillingRecords_Object = MibTableColumn
cdx6500GSCSCfgBillingRecords = _Cdx6500GSCSCfgBillingRecords_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 8, 1, 7),
    _Cdx6500GSCSCfgBillingRecords_Type()
)
cdx6500GSCSCfgBillingRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSCfgBillingRecords.setStatus("mandatory")


class _Cdx6500GSCSCfgStationOptions_Type(DisplayString):
    """Custom type cdx6500GSCSCfgStationOptions based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 9),
    )


_Cdx6500GSCSCfgStationOptions_Type.__name__ = "DisplayString"
_Cdx6500GSCSCfgStationOptions_Object = MibTableColumn
cdx6500GSCSCfgStationOptions = _Cdx6500GSCSCfgStationOptions_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 8, 1, 8),
    _Cdx6500GSCSCfgStationOptions_Type()
)
cdx6500GSCSCfgStationOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSCfgStationOptions.setStatus("mandatory")
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
_Cdx6500PPSTGSCPortTable_Object = MibTable
cdx6500PPSTGSCPortTable = _Cdx6500PPSTGSCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 30)
)
if mibBuilder.loadTexts:
    cdx6500PPSTGSCPortTable.setStatus("mandatory")
_Cdx6500PPSTGSCPortEntry_Object = MibTableRow
cdx6500PPSTGSCPortEntry = _Cdx6500PPSTGSCPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 30, 1)
)
cdx6500PPSTGSCPortEntry.setIndexNames(
    (0, "GSC-OPT-MIB", "cdx6500GSCPStatPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPSTGSCPortEntry.setStatus("mandatory")


class _Cdx6500GSCPStatPortNumber_Type(Integer32):
    """Custom type cdx6500GSCPStatPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500GSCPStatPortNumber_Type.__name__ = "Integer32"
_Cdx6500GSCPStatPortNumber_Object = MibTableColumn
cdx6500GSCPStatPortNumber = _Cdx6500GSCPStatPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 30, 1, 1),
    _Cdx6500GSCPStatPortNumber_Type()
)
cdx6500GSCPStatPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPStatPortNumber.setStatus("mandatory")


class _Cdx6500GSCPStatPortType_Type(Integer32):
    """Custom type cdx6500GSCPStatPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            51
        )
    )
    namedValues = NamedValues(
        ("gsc", 51)
    )


_Cdx6500GSCPStatPortType_Type.__name__ = "Integer32"
_Cdx6500GSCPStatPortType_Object = MibTableColumn
cdx6500GSCPStatPortType = _Cdx6500GSCPStatPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 30, 1, 2),
    _Cdx6500GSCPStatPortType_Type()
)
cdx6500GSCPStatPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPStatPortType.setStatus("mandatory")


class _Cdx6500GSCPStatSubtype_Type(Integer32):
    """Custom type cdx6500GSCPStatSubtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gscHpad", 2),
          ("gscTpad", 1))
    )


_Cdx6500GSCPStatSubtype_Type.__name__ = "Integer32"
_Cdx6500GSCPStatSubtype_Object = MibTableColumn
cdx6500GSCPStatSubtype = _Cdx6500GSCPStatSubtype_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 30, 1, 3),
    _Cdx6500GSCPStatSubtype_Type()
)
cdx6500GSCPStatSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPStatSubtype.setStatus("mandatory")


class _Cdx6500GSCPStatPortStatus_Type(Integer32):
    """Custom type cdx6500GSCPStatPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              50)
        )
    )
    namedValues = NamedValues(
        *(("busyOut", 2),
          ("disabled", 0),
          ("down", 4),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("up", 3))
    )


_Cdx6500GSCPStatPortStatus_Type.__name__ = "Integer32"
_Cdx6500GSCPStatPortStatus_Object = MibTableColumn
cdx6500GSCPStatPortStatus = _Cdx6500GSCPStatPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 30, 1, 4),
    _Cdx6500GSCPStatPortStatus_Type()
)
cdx6500GSCPStatPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPStatPortStatus.setStatus("mandatory")
_Cdx6500GSCPStatPortSpeed_Type = Integer32
_Cdx6500GSCPStatPortSpeed_Object = MibTableColumn
cdx6500GSCPStatPortSpeed = _Cdx6500GSCPStatPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 30, 1, 5),
    _Cdx6500GSCPStatPortSpeed_Type()
)
cdx6500GSCPStatPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPStatPortSpeed.setStatus("mandatory")
_Cdx6500GSCPStatLastStatsReset_Type = DisplayString
_Cdx6500GSCPStatLastStatsReset_Object = MibTableColumn
cdx6500GSCPStatLastStatsReset = _Cdx6500GSCPStatLastStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 30, 1, 6),
    _Cdx6500GSCPStatLastStatsReset_Type()
)
cdx6500GSCPStatLastStatsReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPStatLastStatsReset.setStatus("mandatory")
_Cdx6500GSCPStatCharsIn_Type = Counter32
_Cdx6500GSCPStatCharsIn_Object = MibTableColumn
cdx6500GSCPStatCharsIn = _Cdx6500GSCPStatCharsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 30, 1, 7),
    _Cdx6500GSCPStatCharsIn_Type()
)
cdx6500GSCPStatCharsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPStatCharsIn.setStatus("mandatory")
_Cdx6500GSCPStatCharsOut_Type = Counter32
_Cdx6500GSCPStatCharsOut_Object = MibTableColumn
cdx6500GSCPStatCharsOut = _Cdx6500GSCPStatCharsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 30, 1, 8),
    _Cdx6500GSCPStatCharsOut_Type()
)
cdx6500GSCPStatCharsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPStatCharsOut.setStatus("mandatory")
_Cdx6500GSCPStatCharsInPerSec_Type = Integer32
_Cdx6500GSCPStatCharsInPerSec_Object = MibTableColumn
cdx6500GSCPStatCharsInPerSec = _Cdx6500GSCPStatCharsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 30, 1, 9),
    _Cdx6500GSCPStatCharsInPerSec_Type()
)
cdx6500GSCPStatCharsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPStatCharsInPerSec.setStatus("mandatory")
_Cdx6500GSCPStatCharsOutPerSec_Type = Integer32
_Cdx6500GSCPStatCharsOutPerSec_Object = MibTableColumn
cdx6500GSCPStatCharsOutPerSec = _Cdx6500GSCPStatCharsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 30, 1, 10),
    _Cdx6500GSCPStatCharsOutPerSec_Type()
)
cdx6500GSCPStatCharsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPStatCharsOutPerSec.setStatus("mandatory")
_Cdx6500GSCPStatOverrunErrs_Type = Counter32
_Cdx6500GSCPStatOverrunErrs_Object = MibTableColumn
cdx6500GSCPStatOverrunErrs = _Cdx6500GSCPStatOverrunErrs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 30, 1, 11),
    _Cdx6500GSCPStatOverrunErrs_Type()
)
cdx6500GSCPStatOverrunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPStatOverrunErrs.setStatus("mandatory")
_Cdx6500GSCPStatChecksumErrs_Type = Counter32
_Cdx6500GSCPStatChecksumErrs_Object = MibTableColumn
cdx6500GSCPStatChecksumErrs = _Cdx6500GSCPStatChecksumErrs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 30, 1, 12),
    _Cdx6500GSCPStatChecksumErrs_Type()
)
cdx6500GSCPStatChecksumErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPStatChecksumErrs.setStatus("mandatory")
_Cdx6500GSCPStatOverlengthFrames_Type = Counter32
_Cdx6500GSCPStatOverlengthFrames_Object = MibTableColumn
cdx6500GSCPStatOverlengthFrames = _Cdx6500GSCPStatOverlengthFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 30, 1, 13),
    _Cdx6500GSCPStatOverlengthFrames_Type()
)
cdx6500GSCPStatOverlengthFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPStatOverlengthFrames.setStatus("mandatory")
_Cdx6500GSCPStatPollRespTimeOuts_Type = Counter32
_Cdx6500GSCPStatPollRespTimeOuts_Object = MibTableColumn
cdx6500GSCPStatPollRespTimeOuts = _Cdx6500GSCPStatPollRespTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 30, 1, 14),
    _Cdx6500GSCPStatPollRespTimeOuts_Type()
)
cdx6500GSCPStatPollRespTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPStatPollRespTimeOuts.setStatus("mandatory")
_Cdx6500GSCPStatIntercharTimeOuts_Type = Counter32
_Cdx6500GSCPStatIntercharTimeOuts_Object = MibTableColumn
cdx6500GSCPStatIntercharTimeOuts = _Cdx6500GSCPStatIntercharTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 30, 1, 15),
    _Cdx6500GSCPStatIntercharTimeOuts_Type()
)
cdx6500GSCPStatIntercharTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPStatIntercharTimeOuts.setStatus("mandatory")
_Cdx6500GSCPStatAckTimeOuts_Type = Counter32
_Cdx6500GSCPStatAckTimeOuts_Object = MibTableColumn
cdx6500GSCPStatAckTimeOuts = _Cdx6500GSCPStatAckTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 30, 1, 16),
    _Cdx6500GSCPStatAckTimeOuts_Type()
)
cdx6500GSCPStatAckTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPStatAckTimeOuts.setStatus("mandatory")
_Cdx6500GSCPStatPADFrames_Type = Counter32
_Cdx6500GSCPStatPADFrames_Object = MibTableColumn
cdx6500GSCPStatPADFrames = _Cdx6500GSCPStatPADFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 30, 1, 17),
    _Cdx6500GSCPStatPADFrames_Type()
)
cdx6500GSCPStatPADFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPStatPADFrames.setStatus("mandatory")
_Cdx6500GSCPStatSADFrames_Type = Counter32
_Cdx6500GSCPStatSADFrames_Object = MibTableColumn
cdx6500GSCPStatSADFrames = _Cdx6500GSCPStatSADFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 30, 1, 18),
    _Cdx6500GSCPStatSADFrames_Type()
)
cdx6500GSCPStatSADFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPStatSADFrames.setStatus("mandatory")
_Cdx6500GSCPStatUADFrames_Type = Counter32
_Cdx6500GSCPStatUADFrames_Object = MibTableColumn
cdx6500GSCPStatUADFrames = _Cdx6500GSCPStatUADFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 30, 1, 19),
    _Cdx6500GSCPStatUADFrames_Type()
)
cdx6500GSCPStatUADFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPStatUADFrames.setStatus("mandatory")
_Cdx6500GSCPStatBROFrames_Type = Counter32
_Cdx6500GSCPStatBROFrames_Object = MibTableColumn
cdx6500GSCPStatBROFrames = _Cdx6500GSCPStatBROFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 30, 1, 20),
    _Cdx6500GSCPStatBROFrames_Type()
)
cdx6500GSCPStatBROFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPStatBROFrames.setStatus("mandatory")
_Cdx6500GSCPStatPADChars_Type = Counter32
_Cdx6500GSCPStatPADChars_Object = MibTableColumn
cdx6500GSCPStatPADChars = _Cdx6500GSCPStatPADChars_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 30, 1, 21),
    _Cdx6500GSCPStatPADChars_Type()
)
cdx6500GSCPStatPADChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPStatPADChars.setStatus("mandatory")
_Cdx6500GSCPStatSADChars_Type = Counter32
_Cdx6500GSCPStatSADChars_Object = MibTableColumn
cdx6500GSCPStatSADChars = _Cdx6500GSCPStatSADChars_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 30, 1, 22),
    _Cdx6500GSCPStatSADChars_Type()
)
cdx6500GSCPStatSADChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPStatSADChars.setStatus("mandatory")
_Cdx6500GSCPStatUADChars_Type = Counter32
_Cdx6500GSCPStatUADChars_Object = MibTableColumn
cdx6500GSCPStatUADChars = _Cdx6500GSCPStatUADChars_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 30, 1, 23),
    _Cdx6500GSCPStatUADChars_Type()
)
cdx6500GSCPStatUADChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPStatUADChars.setStatus("mandatory")
_Cdx6500GSCPStatENQs_Type = Counter32
_Cdx6500GSCPStatENQs_Object = MibTableColumn
cdx6500GSCPStatENQs = _Cdx6500GSCPStatENQs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 30, 1, 24),
    _Cdx6500GSCPStatENQs_Type()
)
cdx6500GSCPStatENQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPStatENQs.setStatus("mandatory")
_Cdx6500GSCPStatPACChars_Type = Counter32
_Cdx6500GSCPStatPACChars_Object = MibTableColumn
cdx6500GSCPStatPACChars = _Cdx6500GSCPStatPACChars_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 30, 1, 25),
    _Cdx6500GSCPStatPACChars_Type()
)
cdx6500GSCPStatPACChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPStatPACChars.setStatus("mandatory")
_Cdx6500GSCPStatSACChars_Type = Counter32
_Cdx6500GSCPStatSACChars_Object = MibTableColumn
cdx6500GSCPStatSACChars = _Cdx6500GSCPStatSACChars_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 30, 1, 26),
    _Cdx6500GSCPStatSACChars_Type()
)
cdx6500GSCPStatSACChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPStatSACChars.setStatus("mandatory")
_Cdx6500GSCPStatUACChars_Type = Counter32
_Cdx6500GSCPStatUACChars_Object = MibTableColumn
cdx6500GSCPStatUACChars = _Cdx6500GSCPStatUACChars_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 30, 1, 27),
    _Cdx6500GSCPStatUACChars_Type()
)
cdx6500GSCPStatUACChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPStatUACChars.setStatus("mandatory")
_Cdx6500GSCPStatPolls_Type = Counter32
_Cdx6500GSCPStatPolls_Object = MibTableColumn
cdx6500GSCPStatPolls = _Cdx6500GSCPStatPolls_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 30, 1, 28),
    _Cdx6500GSCPStatPolls_Type()
)
cdx6500GSCPStatPolls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCPStatPolls.setStatus("mandatory")
_Cdx6500PSTStationProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTStationProtocolGroup = _Cdx6500PSTStationProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3)
)
_Cdx6500SPSTGSCStationTable_Object = MibTable
cdx6500SPSTGSCStationTable = _Cdx6500SPSTGSCStationTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7)
)
if mibBuilder.loadTexts:
    cdx6500SPSTGSCStationTable.setStatus("mandatory")
_Cdx6500SPSTGSCStationEntry_Object = MibTableRow
cdx6500SPSTGSCStationEntry = _Cdx6500SPSTGSCStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1)
)
cdx6500SPSTGSCStationEntry.setIndexNames(
    (0, "GSC-OPT-MIB", "cdx6500GSCSStatPortNumber"),
    (0, "GSC-OPT-MIB", "cdx6500GSCSStatStationNum"),
)
if mibBuilder.loadTexts:
    cdx6500SPSTGSCStationEntry.setStatus("mandatory")


class _Cdx6500GSCSStatPortNumber_Type(Integer32):
    """Custom type cdx6500GSCSStatPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500GSCSStatPortNumber_Type.__name__ = "Integer32"
_Cdx6500GSCSStatPortNumber_Object = MibTableColumn
cdx6500GSCSStatPortNumber = _Cdx6500GSCSStatPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 1),
    _Cdx6500GSCSStatPortNumber_Type()
)
cdx6500GSCSStatPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatPortNumber.setStatus("mandatory")


class _Cdx6500GSCSStatStationNum_Type(Integer32):
    """Custom type cdx6500GSCSStatStationNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Cdx6500GSCSStatStationNum_Type.__name__ = "Integer32"
_Cdx6500GSCSStatStationNum_Object = MibTableColumn
cdx6500GSCSStatStationNum = _Cdx6500GSCSStatStationNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 2),
    _Cdx6500GSCSStatStationNum_Type()
)
cdx6500GSCSStatStationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatStationNum.setStatus("mandatory")


class _Cdx6500GSCSStatPortType_Type(Integer32):
    """Custom type cdx6500GSCSStatPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            51
        )
    )
    namedValues = NamedValues(
        ("gsc", 51)
    )


_Cdx6500GSCSStatPortType_Type.__name__ = "Integer32"
_Cdx6500GSCSStatPortType_Object = MibTableColumn
cdx6500GSCSStatPortType = _Cdx6500GSCSStatPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 3),
    _Cdx6500GSCSStatPortType_Type()
)
cdx6500GSCSStatPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatPortType.setStatus("mandatory")


class _Cdx6500GSCSStatSubtype_Type(Integer32):
    """Custom type cdx6500GSCSStatSubtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gscHpad", 2),
          ("gscTpad", 1))
    )


_Cdx6500GSCSStatSubtype_Type.__name__ = "Integer32"
_Cdx6500GSCSStatSubtype_Object = MibTableColumn
cdx6500GSCSStatSubtype = _Cdx6500GSCSStatSubtype_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 4),
    _Cdx6500GSCSStatSubtype_Type()
)
cdx6500GSCSStatSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatSubtype.setStatus("mandatory")


class _Cdx6500GSCSStatStationAddress_Type(Integer32):
    """Custom type cdx6500GSCSStatStationAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 29),
    )


_Cdx6500GSCSStatStationAddress_Type.__name__ = "Integer32"
_Cdx6500GSCSStatStationAddress_Object = MibTableColumn
cdx6500GSCSStatStationAddress = _Cdx6500GSCSStatStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 5),
    _Cdx6500GSCSStatStationAddress_Type()
)
cdx6500GSCSStatStationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatStationAddress.setStatus("mandatory")


class _Cdx6500GSCSStatStationStatus_Type(Integer32):
    """Custom type cdx6500GSCSStatStationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              50)
        )
    )
    namedValues = NamedValues(
        *(("busyOut", 2),
          ("disabled", 0),
          ("down", 4),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("up", 3))
    )


_Cdx6500GSCSStatStationStatus_Type.__name__ = "Integer32"
_Cdx6500GSCSStatStationStatus_Object = MibTableColumn
cdx6500GSCSStatStationStatus = _Cdx6500GSCSStatStationStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 6),
    _Cdx6500GSCSStatStationStatus_Type()
)
cdx6500GSCSStatStationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatStationStatus.setStatus("mandatory")
_Cdx6500GSCSStatLastStatsReset_Type = DisplayString
_Cdx6500GSCSStatLastStatsReset_Object = MibTableColumn
cdx6500GSCSStatLastStatsReset = _Cdx6500GSCSStatLastStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 7),
    _Cdx6500GSCSStatLastStatsReset_Type()
)
cdx6500GSCSStatLastStatsReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatLastStatsReset.setStatus("mandatory")
_Cdx6500GSCSStatCharsIn_Type = Counter32
_Cdx6500GSCSStatCharsIn_Object = MibTableColumn
cdx6500GSCSStatCharsIn = _Cdx6500GSCSStatCharsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 8),
    _Cdx6500GSCSStatCharsIn_Type()
)
cdx6500GSCSStatCharsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatCharsIn.setStatus("mandatory")
_Cdx6500GSCSStatCharsOut_Type = Counter32
_Cdx6500GSCSStatCharsOut_Object = MibTableColumn
cdx6500GSCSStatCharsOut = _Cdx6500GSCSStatCharsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 9),
    _Cdx6500GSCSStatCharsOut_Type()
)
cdx6500GSCSStatCharsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatCharsOut.setStatus("mandatory")
_Cdx6500GSCSStatCharsInPerSec_Type = Integer32
_Cdx6500GSCSStatCharsInPerSec_Object = MibTableColumn
cdx6500GSCSStatCharsInPerSec = _Cdx6500GSCSStatCharsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 10),
    _Cdx6500GSCSStatCharsInPerSec_Type()
)
cdx6500GSCSStatCharsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatCharsInPerSec.setStatus("mandatory")
_Cdx6500GSCSStatCharsOutPerSec_Type = Integer32
_Cdx6500GSCSStatCharsOutPerSec_Object = MibTableColumn
cdx6500GSCSStatCharsOutPerSec = _Cdx6500GSCSStatCharsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 11),
    _Cdx6500GSCSStatCharsOutPerSec_Type()
)
cdx6500GSCSStatCharsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatCharsOutPerSec.setStatus("mandatory")
_Cdx6500GSCSStatChecksumErrs_Type = Counter32
_Cdx6500GSCSStatChecksumErrs_Object = MibTableColumn
cdx6500GSCSStatChecksumErrs = _Cdx6500GSCSStatChecksumErrs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 12),
    _Cdx6500GSCSStatChecksumErrs_Type()
)
cdx6500GSCSStatChecksumErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatChecksumErrs.setStatus("mandatory")
_Cdx6500GSCSStatOverlengthFrames_Type = Counter32
_Cdx6500GSCSStatOverlengthFrames_Object = MibTableColumn
cdx6500GSCSStatOverlengthFrames = _Cdx6500GSCSStatOverlengthFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 13),
    _Cdx6500GSCSStatOverlengthFrames_Type()
)
cdx6500GSCSStatOverlengthFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatOverlengthFrames.setStatus("mandatory")
_Cdx6500GSCSStatPollRespTimeOuts_Type = Counter32
_Cdx6500GSCSStatPollRespTimeOuts_Object = MibTableColumn
cdx6500GSCSStatPollRespTimeOuts = _Cdx6500GSCSStatPollRespTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 14),
    _Cdx6500GSCSStatPollRespTimeOuts_Type()
)
cdx6500GSCSStatPollRespTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatPollRespTimeOuts.setStatus("mandatory")
_Cdx6500GSCSStatIntercharTimeOuts_Type = Counter32
_Cdx6500GSCSStatIntercharTimeOuts_Object = MibTableColumn
cdx6500GSCSStatIntercharTimeOuts = _Cdx6500GSCSStatIntercharTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 15),
    _Cdx6500GSCSStatIntercharTimeOuts_Type()
)
cdx6500GSCSStatIntercharTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatIntercharTimeOuts.setStatus("mandatory")
_Cdx6500GSCSStatAckTimeOuts_Type = Counter32
_Cdx6500GSCSStatAckTimeOuts_Object = MibTableColumn
cdx6500GSCSStatAckTimeOuts = _Cdx6500GSCSStatAckTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 16),
    _Cdx6500GSCSStatAckTimeOuts_Type()
)
cdx6500GSCSStatAckTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatAckTimeOuts.setStatus("mandatory")
_Cdx6500GSCSStatPADFrames_Type = Counter32
_Cdx6500GSCSStatPADFrames_Object = MibTableColumn
cdx6500GSCSStatPADFrames = _Cdx6500GSCSStatPADFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 17),
    _Cdx6500GSCSStatPADFrames_Type()
)
cdx6500GSCSStatPADFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatPADFrames.setStatus("mandatory")
_Cdx6500GSCSStatSADFrames_Type = Counter32
_Cdx6500GSCSStatSADFrames_Object = MibTableColumn
cdx6500GSCSStatSADFrames = _Cdx6500GSCSStatSADFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 18),
    _Cdx6500GSCSStatSADFrames_Type()
)
cdx6500GSCSStatSADFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatSADFrames.setStatus("mandatory")
_Cdx6500GSCSStatUADFrames_Type = Counter32
_Cdx6500GSCSStatUADFrames_Object = MibTableColumn
cdx6500GSCSStatUADFrames = _Cdx6500GSCSStatUADFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 19),
    _Cdx6500GSCSStatUADFrames_Type()
)
cdx6500GSCSStatUADFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatUADFrames.setStatus("mandatory")
_Cdx6500GSCSStatBROFrames_Type = Counter32
_Cdx6500GSCSStatBROFrames_Object = MibTableColumn
cdx6500GSCSStatBROFrames = _Cdx6500GSCSStatBROFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 20),
    _Cdx6500GSCSStatBROFrames_Type()
)
cdx6500GSCSStatBROFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatBROFrames.setStatus("mandatory")
_Cdx6500GSCSStatPADChars_Type = Counter32
_Cdx6500GSCSStatPADChars_Object = MibTableColumn
cdx6500GSCSStatPADChars = _Cdx6500GSCSStatPADChars_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 21),
    _Cdx6500GSCSStatPADChars_Type()
)
cdx6500GSCSStatPADChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatPADChars.setStatus("mandatory")
_Cdx6500GSCSStatSADChars_Type = Counter32
_Cdx6500GSCSStatSADChars_Object = MibTableColumn
cdx6500GSCSStatSADChars = _Cdx6500GSCSStatSADChars_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 22),
    _Cdx6500GSCSStatSADChars_Type()
)
cdx6500GSCSStatSADChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatSADChars.setStatus("mandatory")
_Cdx6500GSCSStatUADChars_Type = Counter32
_Cdx6500GSCSStatUADChars_Object = MibTableColumn
cdx6500GSCSStatUADChars = _Cdx6500GSCSStatUADChars_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 23),
    _Cdx6500GSCSStatUADChars_Type()
)
cdx6500GSCSStatUADChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatUADChars.setStatus("mandatory")
_Cdx6500GSCSStatENQ_Type = Counter32
_Cdx6500GSCSStatENQ_Object = MibTableColumn
cdx6500GSCSStatENQ = _Cdx6500GSCSStatENQ_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 24),
    _Cdx6500GSCSStatENQ_Type()
)
cdx6500GSCSStatENQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatENQ.setStatus("mandatory")
_Cdx6500GSCSStatPACChars_Type = Counter32
_Cdx6500GSCSStatPACChars_Object = MibTableColumn
cdx6500GSCSStatPACChars = _Cdx6500GSCSStatPACChars_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 25),
    _Cdx6500GSCSStatPACChars_Type()
)
cdx6500GSCSStatPACChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatPACChars.setStatus("mandatory")
_Cdx6500GSCSStatSACChars_Type = Counter32
_Cdx6500GSCSStatSACChars_Object = MibTableColumn
cdx6500GSCSStatSACChars = _Cdx6500GSCSStatSACChars_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 26),
    _Cdx6500GSCSStatSACChars_Type()
)
cdx6500GSCSStatSACChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatSACChars.setStatus("mandatory")
_Cdx6500GSCSStatUACChars_Type = Counter32
_Cdx6500GSCSStatUACChars_Object = MibTableColumn
cdx6500GSCSStatUACChars = _Cdx6500GSCSStatUACChars_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 27),
    _Cdx6500GSCSStatUACChars_Type()
)
cdx6500GSCSStatUACChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatUACChars.setStatus("mandatory")
_Cdx6500GSCSStatPolls_Type = Counter32
_Cdx6500GSCSStatPolls_Object = MibTableColumn
cdx6500GSCSStatPolls = _Cdx6500GSCSStatPolls_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 28),
    _Cdx6500GSCSStatPolls_Type()
)
cdx6500GSCSStatPolls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatPolls.setStatus("mandatory")
_Cdx6500GSCSStatPADMessages_Type = Counter32
_Cdx6500GSCSStatPADMessages_Object = MibTableColumn
cdx6500GSCSStatPADMessages = _Cdx6500GSCSStatPADMessages_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 29),
    _Cdx6500GSCSStatPADMessages_Type()
)
cdx6500GSCSStatPADMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatPADMessages.setStatus("mandatory")
_Cdx6500GSCSStatUADMessages_Type = Counter32
_Cdx6500GSCSStatUADMessages_Object = MibTableColumn
cdx6500GSCSStatUADMessages = _Cdx6500GSCSStatUADMessages_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 30),
    _Cdx6500GSCSStatUADMessages_Type()
)
cdx6500GSCSStatUADMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatUADMessages.setStatus("mandatory")
_Cdx6500GSCSStatSADMessages_Type = Counter32
_Cdx6500GSCSStatSADMessages_Object = MibTableColumn
cdx6500GSCSStatSADMessages = _Cdx6500GSCSStatSADMessages_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 31),
    _Cdx6500GSCSStatSADMessages_Type()
)
cdx6500GSCSStatSADMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatSADMessages.setStatus("mandatory")
_Cdx6500GSCSStatBROMessages_Type = Counter32
_Cdx6500GSCSStatBROMessages_Object = MibTableColumn
cdx6500GSCSStatBROMessages = _Cdx6500GSCSStatBROMessages_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 32),
    _Cdx6500GSCSStatBROMessages_Type()
)
cdx6500GSCSStatBROMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatBROMessages.setStatus("mandatory")
_Cdx6500GSCSStatSolicitAbort_Type = Counter32
_Cdx6500GSCSStatSolicitAbort_Object = MibTableColumn
cdx6500GSCSStatSolicitAbort = _Cdx6500GSCSStatSolicitAbort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 33),
    _Cdx6500GSCSStatSolicitAbort_Type()
)
cdx6500GSCSStatSolicitAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatSolicitAbort.setStatus("mandatory")
_Cdx6500GSCSStatStatusEnq_Type = Counter32
_Cdx6500GSCSStatStatusEnq_Object = MibTableColumn
cdx6500GSCSStatStatusEnq = _Cdx6500GSCSStatStatusEnq_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 34),
    _Cdx6500GSCSStatStatusEnq_Type()
)
cdx6500GSCSStatStatusEnq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatStatusEnq.setStatus("mandatory")
_Cdx6500GSCSStatDeviceUp_Type = Counter32
_Cdx6500GSCSStatDeviceUp_Object = MibTableColumn
cdx6500GSCSStatDeviceUp = _Cdx6500GSCSStatDeviceUp_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 35),
    _Cdx6500GSCSStatDeviceUp_Type()
)
cdx6500GSCSStatDeviceUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatDeviceUp.setStatus("mandatory")
_Cdx6500GSCSStatDeviceDown_Type = Counter32
_Cdx6500GSCSStatDeviceDown_Object = MibTableColumn
cdx6500GSCSStatDeviceDown = _Cdx6500GSCSStatDeviceDown_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 36),
    _Cdx6500GSCSStatDeviceDown_Type()
)
cdx6500GSCSStatDeviceDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatDeviceDown.setStatus("mandatory")


class _Cdx6500GSCSStatCallCurrentStatus_Type(Integer32):
    """Custom type cdx6500GSCSStatCallCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("called", 4),
          ("calling", 3),
          ("connected", 5),
          ("disconnected", 2),
          ("inhibited", 1),
          ("notDefined", 6))
    )


_Cdx6500GSCSStatCallCurrentStatus_Type.__name__ = "Integer32"
_Cdx6500GSCSStatCallCurrentStatus_Object = MibTableColumn
cdx6500GSCSStatCallCurrentStatus = _Cdx6500GSCSStatCallCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 37),
    _Cdx6500GSCSStatCallCurrentStatus_Type()
)
cdx6500GSCSStatCallCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatCallCurrentStatus.setStatus("mandatory")
_Cdx6500GSCSStatLastClrCauseCode_Type = DisplayString
_Cdx6500GSCSStatLastClrCauseCode_Object = MibTableColumn
cdx6500GSCSStatLastClrCauseCode = _Cdx6500GSCSStatLastClrCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 38),
    _Cdx6500GSCSStatLastClrCauseCode_Type()
)
cdx6500GSCSStatLastClrCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatLastClrCauseCode.setStatus("mandatory")
_Cdx6500GSCSStatLastClrDiagCode_Type = DisplayString
_Cdx6500GSCSStatLastClrDiagCode_Object = MibTableColumn
cdx6500GSCSStatLastClrDiagCode = _Cdx6500GSCSStatLastClrDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 39),
    _Cdx6500GSCSStatLastClrDiagCode_Type()
)
cdx6500GSCSStatLastClrDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatLastClrDiagCode.setStatus("mandatory")
_Cdx6500GSCSStatLastInCalledAddress_Type = DisplayString
_Cdx6500GSCSStatLastInCalledAddress_Object = MibTableColumn
cdx6500GSCSStatLastInCalledAddress = _Cdx6500GSCSStatLastInCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 40),
    _Cdx6500GSCSStatLastInCalledAddress_Type()
)
cdx6500GSCSStatLastInCalledAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatLastInCalledAddress.setStatus("mandatory")
_Cdx6500GSCSStatLastInCallingAddress_Type = DisplayString
_Cdx6500GSCSStatLastInCallingAddress_Object = MibTableColumn
cdx6500GSCSStatLastInCallingAddress = _Cdx6500GSCSStatLastInCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 41),
    _Cdx6500GSCSStatLastInCallingAddress_Type()
)
cdx6500GSCSStatLastInCallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatLastInCallingAddress.setStatus("mandatory")
_Cdx6500GSCSStatLastInCallFacilities_Type = DisplayString
_Cdx6500GSCSStatLastInCallFacilities_Object = MibTableColumn
cdx6500GSCSStatLastInCallFacilities = _Cdx6500GSCSStatLastInCallFacilities_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 42),
    _Cdx6500GSCSStatLastInCallFacilities_Type()
)
cdx6500GSCSStatLastInCallFacilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatLastInCallFacilities.setStatus("mandatory")
_Cdx6500GSCSStatLastInCallCUD_Type = DisplayString
_Cdx6500GSCSStatLastInCallCUD_Object = MibTableColumn
cdx6500GSCSStatLastInCallCUD = _Cdx6500GSCSStatLastInCallCUD_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 43),
    _Cdx6500GSCSStatLastInCallCUD_Type()
)
cdx6500GSCSStatLastInCallCUD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatLastInCallCUD.setStatus("mandatory")
_Cdx6500GSCSStatLastOutCalledAddress_Type = DisplayString
_Cdx6500GSCSStatLastOutCalledAddress_Object = MibTableColumn
cdx6500GSCSStatLastOutCalledAddress = _Cdx6500GSCSStatLastOutCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 44),
    _Cdx6500GSCSStatLastOutCalledAddress_Type()
)
cdx6500GSCSStatLastOutCalledAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatLastOutCalledAddress.setStatus("mandatory")
_Cdx6500GSCSStatLastOutCallingAddress_Type = DisplayString
_Cdx6500GSCSStatLastOutCallingAddress_Object = MibTableColumn
cdx6500GSCSStatLastOutCallingAddress = _Cdx6500GSCSStatLastOutCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 45),
    _Cdx6500GSCSStatLastOutCallingAddress_Type()
)
cdx6500GSCSStatLastOutCallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatLastOutCallingAddress.setStatus("mandatory")
_Cdx6500GSCSStatLastOutCallFacilities_Type = DisplayString
_Cdx6500GSCSStatLastOutCallFacilities_Object = MibTableColumn
cdx6500GSCSStatLastOutCallFacilities = _Cdx6500GSCSStatLastOutCallFacilities_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 46),
    _Cdx6500GSCSStatLastOutCallFacilities_Type()
)
cdx6500GSCSStatLastOutCallFacilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatLastOutCallFacilities.setStatus("mandatory")
_Cdx6500GSCSStatLastOutCallCUD_Type = DisplayString
_Cdx6500GSCSStatLastOutCallCUD_Object = MibTableColumn
cdx6500GSCSStatLastOutCallCUD = _Cdx6500GSCSStatLastOutCallCUD_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 7, 1, 47),
    _Cdx6500GSCSStatLastOutCallCUD_Type()
)
cdx6500GSCSStatLastOutCallCUD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GSCSStatLastOutCallCUD.setStatus("mandatory")
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)
_Cdx6500ContGSC_ObjectIdentity = ObjectIdentity
cdx6500ContGSC = _Cdx6500ContGSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 12)
)
_Cdx6500ContGSCPTable_Object = MibTable
cdx6500ContGSCPTable = _Cdx6500ContGSCPTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 12, 1)
)
if mibBuilder.loadTexts:
    cdx6500ContGSCPTable.setStatus("mandatory")
_Cdx6500ContGSCPTableEntry_Object = MibTableRow
cdx6500ContGSCPTableEntry = _Cdx6500ContGSCPTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 12, 1, 1)
)
cdx6500ContGSCPTableEntry.setIndexNames(
    (0, "GSC-OPT-MIB", "cdx6500ContGSCPPortNum"),
)
if mibBuilder.loadTexts:
    cdx6500ContGSCPTableEntry.setStatus("mandatory")


class _Cdx6500ContGSCPPortNum_Type(Integer32):
    """Custom type cdx6500ContGSCPPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500ContGSCPPortNum_Type.__name__ = "Integer32"
_Cdx6500ContGSCPPortNum_Object = MibTableColumn
cdx6500ContGSCPPortNum = _Cdx6500ContGSCPPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 12, 1, 1, 1),
    _Cdx6500ContGSCPPortNum_Type()
)
cdx6500ContGSCPPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdx6500ContGSCPPortNum.setStatus("mandatory")


class _Cdx6500ContGSCPBootPort_Type(Integer32):
    """Custom type cdx6500ContGSCPBootPort based on Integer32"""
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


_Cdx6500ContGSCPBootPort_Type.__name__ = "Integer32"
_Cdx6500ContGSCPBootPort_Object = MibTableColumn
cdx6500ContGSCPBootPort = _Cdx6500ContGSCPBootPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 12, 1, 1, 2),
    _Cdx6500ContGSCPBootPort_Type()
)
cdx6500ContGSCPBootPort.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500ContGSCPBootPort.setStatus("mandatory")


class _Cdx6500ContGSCPEnablePort_Type(Integer32):
    """Custom type cdx6500ContGSCPEnablePort based on Integer32"""
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


_Cdx6500ContGSCPEnablePort_Type.__name__ = "Integer32"
_Cdx6500ContGSCPEnablePort_Object = MibTableColumn
cdx6500ContGSCPEnablePort = _Cdx6500ContGSCPEnablePort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 12, 1, 1, 3),
    _Cdx6500ContGSCPEnablePort_Type()
)
cdx6500ContGSCPEnablePort.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500ContGSCPEnablePort.setStatus("mandatory")


class _Cdx6500ContGSCPDisablePort_Type(Integer32):
    """Custom type cdx6500ContGSCPDisablePort based on Integer32"""
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


_Cdx6500ContGSCPDisablePort_Type.__name__ = "Integer32"
_Cdx6500ContGSCPDisablePort_Object = MibTableColumn
cdx6500ContGSCPDisablePort = _Cdx6500ContGSCPDisablePort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 12, 1, 1, 4),
    _Cdx6500ContGSCPDisablePort_Type()
)
cdx6500ContGSCPDisablePort.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500ContGSCPDisablePort.setStatus("mandatory")
_Cdx6500ContGSCSTable_Object = MibTable
cdx6500ContGSCSTable = _Cdx6500ContGSCSTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 12, 2)
)
if mibBuilder.loadTexts:
    cdx6500ContGSCSTable.setStatus("mandatory")
_Cdx6500ContGSCSTableEntry_Object = MibTableRow
cdx6500ContGSCSTableEntry = _Cdx6500ContGSCSTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 12, 2, 1)
)
cdx6500ContGSCSTableEntry.setIndexNames(
    (0, "GSC-OPT-MIB", "cdx6500ContGSCSPortNum"),
    (0, "GSC-OPT-MIB", "cdx6500ContGSCSStnNum"),
)
if mibBuilder.loadTexts:
    cdx6500ContGSCSTableEntry.setStatus("mandatory")


class _Cdx6500ContGSCSPortNum_Type(Integer32):
    """Custom type cdx6500ContGSCSPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500ContGSCSPortNum_Type.__name__ = "Integer32"
_Cdx6500ContGSCSPortNum_Object = MibTableColumn
cdx6500ContGSCSPortNum = _Cdx6500ContGSCSPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 12, 2, 1, 1),
    _Cdx6500ContGSCSPortNum_Type()
)
cdx6500ContGSCSPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdx6500ContGSCSPortNum.setStatus("mandatory")


class _Cdx6500ContGSCSStnNum_Type(Integer32):
    """Custom type cdx6500ContGSCSStnNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Cdx6500ContGSCSStnNum_Type.__name__ = "Integer32"
_Cdx6500ContGSCSStnNum_Object = MibTableColumn
cdx6500ContGSCSStnNum = _Cdx6500ContGSCSStnNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 12, 2, 1, 2),
    _Cdx6500ContGSCSStnNum_Type()
)
cdx6500ContGSCSStnNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdx6500ContGSCSStnNum.setStatus("mandatory")


class _Cdx6500ContGSCSBootStation_Type(Integer32):
    """Custom type cdx6500ContGSCSBootStation based on Integer32"""
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


_Cdx6500ContGSCSBootStation_Type.__name__ = "Integer32"
_Cdx6500ContGSCSBootStation_Object = MibTableColumn
cdx6500ContGSCSBootStation = _Cdx6500ContGSCSBootStation_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 12, 2, 1, 3),
    _Cdx6500ContGSCSBootStation_Type()
)
cdx6500ContGSCSBootStation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500ContGSCSBootStation.setStatus("mandatory")


class _Cdx6500ContGSCSEnableStation_Type(Integer32):
    """Custom type cdx6500ContGSCSEnableStation based on Integer32"""
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


_Cdx6500ContGSCSEnableStation_Type.__name__ = "Integer32"
_Cdx6500ContGSCSEnableStation_Object = MibTableColumn
cdx6500ContGSCSEnableStation = _Cdx6500ContGSCSEnableStation_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 12, 2, 1, 4),
    _Cdx6500ContGSCSEnableStation_Type()
)
cdx6500ContGSCSEnableStation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500ContGSCSEnableStation.setStatus("mandatory")


class _Cdx6500ContGSCSDisableStation_Type(Integer32):
    """Custom type cdx6500ContGSCSDisableStation based on Integer32"""
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


_Cdx6500ContGSCSDisableStation_Type.__name__ = "Integer32"
_Cdx6500ContGSCSDisableStation_Object = MibTableColumn
cdx6500ContGSCSDisableStation = _Cdx6500ContGSCSDisableStation_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 12, 2, 1, 5),
    _Cdx6500ContGSCSDisableStation_Type()
)
cdx6500ContGSCSDisableStation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500ContGSCSDisableStation.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GSC-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PPCTGSCPortTable": cdx6500PPCTGSCPortTable,
       "cdx6500PPCTGSCPortEntry": cdx6500PPCTGSCPortEntry,
       "cdx6500GSCPCfgPortNumber": cdx6500GSCPCfgPortNumber,
       "cdx6500GSCPCfgPortType": cdx6500GSCPCfgPortType,
       "cdx6500GSCPCfgSubtype": cdx6500GSCPCfgSubtype,
       "cdx6500GSCPCfgClockSpeed": cdx6500GSCPCfgClockSpeed,
       "cdx6500GSCPCfgNumStations": cdx6500GSCPCfgNumStations,
       "cdx6500GSCPCfgMinPollPeriod": cdx6500GSCPCfgMinPollPeriod,
       "cdx6500GSCPCfgPollRespTimer": cdx6500GSCPCfgPollRespTimer,
       "cdx6500GSCPCfgAckTimeOut": cdx6500GSCPCfgAckTimeOut,
       "cdx6500GSCPCfgInterCharTimeOut": cdx6500GSCPCfgInterCharTimeOut,
       "cdx6500GSCPCfgBroadcastHoldTimeOut": cdx6500GSCPCfgBroadcastHoldTimeOut,
       "cdx6500GSCPCfgSolicitedTimeOut": cdx6500GSCPCfgSolicitedTimeOut,
       "cdx6500GSCPCfgIdleDiscTimeOut": cdx6500GSCPCfgIdleDiscTimeOut,
       "cdx6500GSCPCfgAutocallRetryTimeOut": cdx6500GSCPCfgAutocallRetryTimeOut,
       "cdx6500GSCPCfgMaxAutocallRetries": cdx6500GSCPCfgMaxAutocallRetries,
       "cdx6500GSCPCfgN1": cdx6500GSCPCfgN1,
       "cdx6500GSCPCfgN2": cdx6500GSCPCfgN2,
       "cdx6500GSCPCfgNumRetries": cdx6500GSCPCfgNumRetries,
       "cdx6500GSCPCfgPortAddress": cdx6500GSCPCfgPortAddress,
       "cdx6500GSCPCfgPortOptions": cdx6500GSCPCfgPortOptions,
       "cdx6500GSCPCfgConnType": cdx6500GSCPCfgConnType,
       "cdx6500GSCPCfgWakeUpTimer": cdx6500GSCPCfgWakeUpTimer,
       "cdx6500GSCPCfgElectricalInterfaceType": cdx6500GSCPCfgElectricalInterfaceType,
       "cdx6500GSCPCfgV24ElectricalInterfaceOption": cdx6500GSCPCfgV24ElectricalInterfaceOption,
       "cdx6500GSCPCfgHighSpeedElectricalInterfaceOption": cdx6500GSCPCfgHighSpeedElectricalInterfaceOption,
       "cdx6500PCTStationProtocolGroup": cdx6500PCTStationProtocolGroup,
       "cdx6500SPCTGSCStationTable": cdx6500SPCTGSCStationTable,
       "cdx6500SPCTGSCStationEntry": cdx6500SPCTGSCStationEntry,
       "cdx6500GSCSCfgPortNumber": cdx6500GSCSCfgPortNumber,
       "cdx6500GSCSCfgStationNumber": cdx6500GSCSCfgStationNumber,
       "cdx6500GSCSCfgStationAddress": cdx6500GSCSCfgStationAddress,
       "cdx6500GSCSCfgRemoteAddress": cdx6500GSCSCfgRemoteAddress,
       "cdx6500GSCSCfgAutocallMnem": cdx6500GSCSCfgAutocallMnem,
       "cdx6500GSCSCfgProtocolId": cdx6500GSCSCfgProtocolId,
       "cdx6500GSCSCfgBillingRecords": cdx6500GSCSCfgBillingRecords,
       "cdx6500GSCSCfgStationOptions": cdx6500GSCSCfgStationOptions,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PPSTGSCPortTable": cdx6500PPSTGSCPortTable,
       "cdx6500PPSTGSCPortEntry": cdx6500PPSTGSCPortEntry,
       "cdx6500GSCPStatPortNumber": cdx6500GSCPStatPortNumber,
       "cdx6500GSCPStatPortType": cdx6500GSCPStatPortType,
       "cdx6500GSCPStatSubtype": cdx6500GSCPStatSubtype,
       "cdx6500GSCPStatPortStatus": cdx6500GSCPStatPortStatus,
       "cdx6500GSCPStatPortSpeed": cdx6500GSCPStatPortSpeed,
       "cdx6500GSCPStatLastStatsReset": cdx6500GSCPStatLastStatsReset,
       "cdx6500GSCPStatCharsIn": cdx6500GSCPStatCharsIn,
       "cdx6500GSCPStatCharsOut": cdx6500GSCPStatCharsOut,
       "cdx6500GSCPStatCharsInPerSec": cdx6500GSCPStatCharsInPerSec,
       "cdx6500GSCPStatCharsOutPerSec": cdx6500GSCPStatCharsOutPerSec,
       "cdx6500GSCPStatOverrunErrs": cdx6500GSCPStatOverrunErrs,
       "cdx6500GSCPStatChecksumErrs": cdx6500GSCPStatChecksumErrs,
       "cdx6500GSCPStatOverlengthFrames": cdx6500GSCPStatOverlengthFrames,
       "cdx6500GSCPStatPollRespTimeOuts": cdx6500GSCPStatPollRespTimeOuts,
       "cdx6500GSCPStatIntercharTimeOuts": cdx6500GSCPStatIntercharTimeOuts,
       "cdx6500GSCPStatAckTimeOuts": cdx6500GSCPStatAckTimeOuts,
       "cdx6500GSCPStatPADFrames": cdx6500GSCPStatPADFrames,
       "cdx6500GSCPStatSADFrames": cdx6500GSCPStatSADFrames,
       "cdx6500GSCPStatUADFrames": cdx6500GSCPStatUADFrames,
       "cdx6500GSCPStatBROFrames": cdx6500GSCPStatBROFrames,
       "cdx6500GSCPStatPADChars": cdx6500GSCPStatPADChars,
       "cdx6500GSCPStatSADChars": cdx6500GSCPStatSADChars,
       "cdx6500GSCPStatUADChars": cdx6500GSCPStatUADChars,
       "cdx6500GSCPStatENQs": cdx6500GSCPStatENQs,
       "cdx6500GSCPStatPACChars": cdx6500GSCPStatPACChars,
       "cdx6500GSCPStatSACChars": cdx6500GSCPStatSACChars,
       "cdx6500GSCPStatUACChars": cdx6500GSCPStatUACChars,
       "cdx6500GSCPStatPolls": cdx6500GSCPStatPolls,
       "cdx6500PSTStationProtocolGroup": cdx6500PSTStationProtocolGroup,
       "cdx6500SPSTGSCStationTable": cdx6500SPSTGSCStationTable,
       "cdx6500SPSTGSCStationEntry": cdx6500SPSTGSCStationEntry,
       "cdx6500GSCSStatPortNumber": cdx6500GSCSStatPortNumber,
       "cdx6500GSCSStatStationNum": cdx6500GSCSStatStationNum,
       "cdx6500GSCSStatPortType": cdx6500GSCSStatPortType,
       "cdx6500GSCSStatSubtype": cdx6500GSCSStatSubtype,
       "cdx6500GSCSStatStationAddress": cdx6500GSCSStatStationAddress,
       "cdx6500GSCSStatStationStatus": cdx6500GSCSStatStationStatus,
       "cdx6500GSCSStatLastStatsReset": cdx6500GSCSStatLastStatsReset,
       "cdx6500GSCSStatCharsIn": cdx6500GSCSStatCharsIn,
       "cdx6500GSCSStatCharsOut": cdx6500GSCSStatCharsOut,
       "cdx6500GSCSStatCharsInPerSec": cdx6500GSCSStatCharsInPerSec,
       "cdx6500GSCSStatCharsOutPerSec": cdx6500GSCSStatCharsOutPerSec,
       "cdx6500GSCSStatChecksumErrs": cdx6500GSCSStatChecksumErrs,
       "cdx6500GSCSStatOverlengthFrames": cdx6500GSCSStatOverlengthFrames,
       "cdx6500GSCSStatPollRespTimeOuts": cdx6500GSCSStatPollRespTimeOuts,
       "cdx6500GSCSStatIntercharTimeOuts": cdx6500GSCSStatIntercharTimeOuts,
       "cdx6500GSCSStatAckTimeOuts": cdx6500GSCSStatAckTimeOuts,
       "cdx6500GSCSStatPADFrames": cdx6500GSCSStatPADFrames,
       "cdx6500GSCSStatSADFrames": cdx6500GSCSStatSADFrames,
       "cdx6500GSCSStatUADFrames": cdx6500GSCSStatUADFrames,
       "cdx6500GSCSStatBROFrames": cdx6500GSCSStatBROFrames,
       "cdx6500GSCSStatPADChars": cdx6500GSCSStatPADChars,
       "cdx6500GSCSStatSADChars": cdx6500GSCSStatSADChars,
       "cdx6500GSCSStatUADChars": cdx6500GSCSStatUADChars,
       "cdx6500GSCSStatENQ": cdx6500GSCSStatENQ,
       "cdx6500GSCSStatPACChars": cdx6500GSCSStatPACChars,
       "cdx6500GSCSStatSACChars": cdx6500GSCSStatSACChars,
       "cdx6500GSCSStatUACChars": cdx6500GSCSStatUACChars,
       "cdx6500GSCSStatPolls": cdx6500GSCSStatPolls,
       "cdx6500GSCSStatPADMessages": cdx6500GSCSStatPADMessages,
       "cdx6500GSCSStatUADMessages": cdx6500GSCSStatUADMessages,
       "cdx6500GSCSStatSADMessages": cdx6500GSCSStatSADMessages,
       "cdx6500GSCSStatBROMessages": cdx6500GSCSStatBROMessages,
       "cdx6500GSCSStatSolicitAbort": cdx6500GSCSStatSolicitAbort,
       "cdx6500GSCSStatStatusEnq": cdx6500GSCSStatStatusEnq,
       "cdx6500GSCSStatDeviceUp": cdx6500GSCSStatDeviceUp,
       "cdx6500GSCSStatDeviceDown": cdx6500GSCSStatDeviceDown,
       "cdx6500GSCSStatCallCurrentStatus": cdx6500GSCSStatCallCurrentStatus,
       "cdx6500GSCSStatLastClrCauseCode": cdx6500GSCSStatLastClrCauseCode,
       "cdx6500GSCSStatLastClrDiagCode": cdx6500GSCSStatLastClrDiagCode,
       "cdx6500GSCSStatLastInCalledAddress": cdx6500GSCSStatLastInCalledAddress,
       "cdx6500GSCSStatLastInCallingAddress": cdx6500GSCSStatLastInCallingAddress,
       "cdx6500GSCSStatLastInCallFacilities": cdx6500GSCSStatLastInCallFacilities,
       "cdx6500GSCSStatLastInCallCUD": cdx6500GSCSStatLastInCallCUD,
       "cdx6500GSCSStatLastOutCalledAddress": cdx6500GSCSStatLastOutCalledAddress,
       "cdx6500GSCSStatLastOutCallingAddress": cdx6500GSCSStatLastOutCallingAddress,
       "cdx6500GSCSStatLastOutCallFacilities": cdx6500GSCSStatLastOutCallFacilities,
       "cdx6500GSCSStatLastOutCallCUD": cdx6500GSCSStatLastOutCallCUD,
       "cdx6500Controls": cdx6500Controls,
       "cdx6500ContGSC": cdx6500ContGSC,
       "cdx6500ContGSCPTable": cdx6500ContGSCPTable,
       "cdx6500ContGSCPTableEntry": cdx6500ContGSCPTableEntry,
       "cdx6500ContGSCPPortNum": cdx6500ContGSCPPortNum,
       "cdx6500ContGSCPBootPort": cdx6500ContGSCPBootPort,
       "cdx6500ContGSCPEnablePort": cdx6500ContGSCPEnablePort,
       "cdx6500ContGSCPDisablePort": cdx6500ContGSCPDisablePort,
       "cdx6500ContGSCSTable": cdx6500ContGSCSTable,
       "cdx6500ContGSCSTableEntry": cdx6500ContGSCSTableEntry,
       "cdx6500ContGSCSPortNum": cdx6500ContGSCSPortNum,
       "cdx6500ContGSCSStnNum": cdx6500ContGSCSStnNum,
       "cdx6500ContGSCSBootStation": cdx6500ContGSCSBootStation,
       "cdx6500ContGSCSEnableStation": cdx6500ContGSCSEnableStation,
       "cdx6500ContGSCSDisableStation": cdx6500ContGSCSDisableStation}
)
