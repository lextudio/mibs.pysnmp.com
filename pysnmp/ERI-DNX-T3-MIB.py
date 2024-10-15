# SNMP MIB module (ERI-DNX-T3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ERI-DNX-T3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:30 2024
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

(DecisionType,
 FunctionSwitch,
 LinkCmdStatus,
 LinkPortAddress,
 PortStatus,
 devices,
 dnx,
 trapSequence) = mibBuilder.importSymbols(
    "ERI-DNX-SMC-MIB",
    "DecisionType",
    "FunctionSwitch",
    "LinkCmdStatus",
    "LinkPortAddress",
    "PortStatus",
    "devices",
    "dnx",
    "trapSequence")

(eriMibs,) = mibBuilder.importSymbols(
    "ERI-ROOT-SMI",
    "eriMibs")

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

eriDNXT3MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 644, 3, 3)
)
eriDNXT3MIB.setRevisions(
        ("2002-08-19 00:00",
         "2002-04-11 00:00",
         "2001-04-01 00:00",
         "2000-09-15 00:00",
         "2000-07-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DnxT3_ObjectIdentity = ObjectIdentity
dnxT3 = _DnxT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1)
)
_DnxT3Enterprise_ObjectIdentity = ObjectIdentity
dnxT3Enterprise = _DnxT3Enterprise_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 0)
)
if mibBuilder.loadTexts:
    dnxT3Enterprise.setStatus("current")
_T3Config_ObjectIdentity = ObjectIdentity
t3Config = _T3Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1)
)
_T3PortConfigTable_Object = MibTable
t3PortConfigTable = _T3PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    t3PortConfigTable.setStatus("current")
_T3PortConfigEntry_Object = MibTableRow
t3PortConfigEntry = _T3PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1)
)
t3PortConfigEntry.setIndexNames(
    (0, "ERI-DNX-T3-MIB", "t3CfgAddr"),
)
if mibBuilder.loadTexts:
    t3PortConfigEntry.setStatus("current")
_T3CfgAddr_Type = LinkPortAddress
_T3CfgAddr_Object = MibTableColumn
t3CfgAddr = _T3CfgAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 1),
    _T3CfgAddr_Type()
)
t3CfgAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3CfgAddr.setStatus("current")
_T3CfgResource_Type = Integer32
_T3CfgResource_Object = MibTableColumn
t3CfgResource = _T3CfgResource_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 2),
    _T3CfgResource_Type()
)
t3CfgResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3CfgResource.setStatus("current")


class _T3CfgCircuitName_Type(DisplayString):
    """Custom type t3CfgCircuitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_T3CfgCircuitName_Type.__name__ = "DisplayString"
_T3CfgCircuitName_Object = MibTableColumn
t3CfgCircuitName = _T3CfgCircuitName_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 3),
    _T3CfgCircuitName_Type()
)
t3CfgCircuitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3CfgCircuitName.setStatus("current")


class _T3FacilityId_Type(DisplayString):
    """Custom type t3FacilityId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 37),
    )


_T3FacilityId_Type.__name__ = "DisplayString"
_T3FacilityId_Object = MibTableColumn
t3FacilityId = _T3FacilityId_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 4),
    _T3FacilityId_Type()
)
t3FacilityId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3FacilityId.setStatus("current")


class _T3EquipmentId_Type(DisplayString):
    """Custom type t3EquipmentId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_T3EquipmentId_Type.__name__ = "DisplayString"
_T3EquipmentId_Object = MibTableColumn
t3EquipmentId = _T3EquipmentId_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 5),
    _T3EquipmentId_Type()
)
t3EquipmentId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3EquipmentId.setStatus("current")


class _T3Location_Type(DisplayString):
    """Custom type t3Location based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_T3Location_Type.__name__ = "DisplayString"
_T3Location_Object = MibTableColumn
t3Location = _T3Location_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 6),
    _T3Location_Type()
)
t3Location.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3Location.setStatus("current")


class _T3FrameId_Type(DisplayString):
    """Custom type t3FrameId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_T3FrameId_Type.__name__ = "DisplayString"
_T3FrameId_Object = MibTableColumn
t3FrameId = _T3FrameId_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 7),
    _T3FrameId_Type()
)
t3FrameId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3FrameId.setStatus("current")


class _T3UnitName_Type(DisplayString):
    """Custom type t3UnitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_T3UnitName_Type.__name__ = "DisplayString"
_T3UnitName_Object = MibTableColumn
t3UnitName = _T3UnitName_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 8),
    _T3UnitName_Type()
)
t3UnitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3UnitName.setStatus("current")


class _T3PortNumber_Type(DisplayString):
    """Custom type t3PortNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 37),
    )


_T3PortNumber_Type.__name__ = "DisplayString"
_T3PortNumber_Object = MibTableColumn
t3PortNumber = _T3PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 9),
    _T3PortNumber_Type()
)
t3PortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3PortNumber.setStatus("current")


class _T3Generator_Type(DisplayString):
    """Custom type t3Generator based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 37),
    )


_T3Generator_Type.__name__ = "DisplayString"
_T3Generator_Object = MibTableColumn
t3Generator = _T3Generator_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 10),
    _T3Generator_Type()
)
t3Generator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3Generator.setStatus("current")


class _T3M13OpMode_Type(Integer32):
    """Custom type t3M13OpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bellcoreM13", 1),
          ("c-bit", 0))
    )


_T3M13OpMode_Type.__name__ = "Integer32"
_T3M13OpMode_Object = MibTableColumn
t3M13OpMode = _T3M13OpMode_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 11),
    _T3M13OpMode_Type()
)
t3M13OpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3M13OpMode.setStatus("current")
_T3RcvLoopTiming_Type = FunctionSwitch
_T3RcvLoopTiming_Object = MibTableColumn
t3RcvLoopTiming = _T3RcvLoopTiming_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 12),
    _T3RcvLoopTiming_Type()
)
t3RcvLoopTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3RcvLoopTiming.setStatus("current")
_T3ShortCable_Type = DecisionType
_T3ShortCable_Object = MibTableColumn
t3ShortCable = _T3ShortCable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 13),
    _T3ShortCable_Type()
)
t3ShortCable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3ShortCable.setStatus("current")


class _T3M13RemLoop_Type(Integer32):
    """Custom type t3M13RemLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("first-cbit-inverted", 2),
          ("first-cbit-stuffbit-inverted", 6),
          ("second-cbit-inverted", 1),
          ("second-cbit-stuffbit-inverted", 5),
          ("stuffbit-inverted", 7),
          ("stuffbit-is-one", 9),
          ("stuffbit-is-zero", 8),
          ("third-cbit-inverted", 0),
          ("third-cbit-stuffbit-inverted", 4))
    )


_T3M13RemLoop_Type.__name__ = "Integer32"
_T3M13RemLoop_Object = MibTableColumn
t3M13RemLoop = _T3M13RemLoop_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 14),
    _T3M13RemLoop_Type()
)
t3M13RemLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3M13RemLoop.setStatus("current")


class _T3RcvAIS_Type(Integer32):
    """Custom type t3RcvAIS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("framed1010-Cbit0-Xbit1", 1),
          ("framed1010-Cbit0-noXbit", 0),
          ("framed1010-noCbit-noXbit", 2),
          ("framed1111-noCbit-noXbit", 3),
          ("unframed-allones", 5),
          ("unframed1010", 4))
    )


_T3RcvAIS_Type.__name__ = "Integer32"
_T3RcvAIS_Object = MibTableColumn
t3RcvAIS = _T3RcvAIS_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 15),
    _T3RcvAIS_Type()
)
t3RcvAIS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3RcvAIS.setStatus("current")


class _T3XmtAIS_Type(Integer32):
    """Custom type t3XmtAIS based on Integer32"""
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
        *(("ansi", 0),
          ("framed-allones-Cbit1", 1),
          ("unframed-allones", 3),
          ("unframed1010", 2))
    )


_T3XmtAIS_Type.__name__ = "Integer32"
_T3XmtAIS_Object = MibTableColumn
t3XmtAIS = _T3XmtAIS_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 16),
    _T3XmtAIS_Type()
)
t3XmtAIS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3XmtAIS.setStatus("current")
_T3CmdStatus_Type = LinkCmdStatus
_T3CmdStatus_Object = MibTableColumn
t3CmdStatus = _T3CmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 17),
    _T3CmdStatus_Type()
)
t3CmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3CmdStatus.setStatus("current")
_T3T1LinkConfigTable_Object = MibTable
t3T1LinkConfigTable = _T3T1LinkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    t3T1LinkConfigTable.setStatus("current")
_T3T1LinkConfigEntry_Object = MibTableRow
t3T1LinkConfigEntry = _T3T1LinkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1)
)
t3T1LinkConfigEntry.setIndexNames(
    (0, "ERI-DNX-T3-MIB", "t3T1CfgLinkAddr"),
)
if mibBuilder.loadTexts:
    t3T1LinkConfigEntry.setStatus("current")
_T3T1CfgLinkAddr_Type = LinkPortAddress
_T3T1CfgLinkAddr_Object = MibTableColumn
t3T1CfgLinkAddr = _T3T1CfgLinkAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 1),
    _T3T1CfgLinkAddr_Type()
)
t3T1CfgLinkAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3T1CfgLinkAddr.setStatus("current")
_T3T1CfgResource_Type = Integer32
_T3T1CfgResource_Object = MibTableColumn
t3T1CfgResource = _T3T1CfgResource_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 2),
    _T3T1CfgResource_Type()
)
t3T1CfgResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3T1CfgResource.setStatus("current")


class _T3T1CfgLinkName_Type(DisplayString):
    """Custom type t3T1CfgLinkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_T3T1CfgLinkName_Type.__name__ = "DisplayString"
_T3T1CfgLinkName_Object = MibTableColumn
t3T1CfgLinkName = _T3T1CfgLinkName_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 3),
    _T3T1CfgLinkName_Type()
)
t3T1CfgLinkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3T1CfgLinkName.setStatus("current")
_T3T1Status_Type = PortStatus
_T3T1Status_Object = MibTableColumn
t3T1Status = _T3T1Status_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 4),
    _T3T1Status_Type()
)
t3T1Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3T1Status.setStatus("current")


class _T3T1Framing_Type(Integer32):
    """Custom type t3T1Framing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("d4", 1),
          ("esf", 3))
    )


_T3T1Framing_Type.__name__ = "Integer32"
_T3T1Framing_Object = MibTableColumn
t3T1Framing = _T3T1Framing_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 5),
    _T3T1Framing_Type()
)
t3T1Framing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3T1Framing.setStatus("current")


class _T3T1Density_Type(Integer32):
    """Custom type t3T1Density based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("att-62411", 1),
          ("clear", 0))
    )


_T3T1Density_Type.__name__ = "Integer32"
_T3T1Density_Object = MibTableColumn
t3T1Density = _T3T1Density_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 6),
    _T3T1Density_Type()
)
t3T1Density.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3T1Density.setStatus("current")
_T3T1NetLoop_Type = FunctionSwitch
_T3T1NetLoop_Object = MibTableColumn
t3T1NetLoop = _T3T1NetLoop_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 7),
    _T3T1NetLoop_Type()
)
t3T1NetLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3T1NetLoop.setStatus("current")
_T3T1YelAlrm_Type = DecisionType
_T3T1YelAlrm_Object = MibTableColumn
t3T1YelAlrm = _T3T1YelAlrm_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 8),
    _T3T1YelAlrm_Type()
)
t3T1YelAlrm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3T1YelAlrm.setStatus("current")


class _T3T1RecoverTime_Type(Integer32):
    """Custom type t3T1RecoverTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              10,
              15)
        )
    )
    namedValues = NamedValues(
        *(("timeout-10-secs", 10),
          ("timeout-15-secs", 15),
          ("timeout-3-secs", 3))
    )


_T3T1RecoverTime_Type.__name__ = "Integer32"
_T3T1RecoverTime_Object = MibTableColumn
t3T1RecoverTime = _T3T1RecoverTime_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 9),
    _T3T1RecoverTime_Type()
)
t3T1RecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3T1RecoverTime.setStatus("current")


class _T3T1EsfFormat_Type(Integer32):
    """Custom type t3T1EsfFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ansi-t1-403", 1),
          ("att-54016", 0))
    )


_T3T1EsfFormat_Type.__name__ = "Integer32"
_T3T1EsfFormat_Object = MibTableColumn
t3T1EsfFormat = _T3T1EsfFormat_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 10),
    _T3T1EsfFormat_Type()
)
t3T1EsfFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3T1EsfFormat.setStatus("current")


class _T3T1IdleCode_Type(Integer32):
    """Custom type t3T1IdleCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("busy", 0),
          ("idle", 1))
    )


_T3T1IdleCode_Type.__name__ = "Integer32"
_T3T1IdleCode_Object = MibTableColumn
t3T1IdleCode = _T3T1IdleCode_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 11),
    _T3T1IdleCode_Type()
)
t3T1IdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3T1IdleCode.setStatus("current")
_T3T1CfgCmdStatus_Type = LinkCmdStatus
_T3T1CfgCmdStatus_Object = MibTableColumn
t3T1CfgCmdStatus = _T3T1CfgCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 12),
    _T3T1CfgCmdStatus_Type()
)
t3T1CfgCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3T1CfgCmdStatus.setStatus("current")
_T3Diag_ObjectIdentity = ObjectIdentity
t3Diag = _T3Diag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 2)
)

# Managed Objects groups


# Notification objects

t3PortConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 0, 1)
)
t3PortConfigTrap.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-T3-MIB", "t3CfgAddr"),
        ("ERI-DNX-T3-MIB", "t3CmdStatus"))
)
if mibBuilder.loadTexts:
    t3PortConfigTrap.setStatus(
        "current"
    )

t3T1ConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 0, 2)
)
t3T1ConfigTrap.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-T3-MIB", "t3T1CfgLinkAddr"),
        ("ERI-DNX-T3-MIB", "t3T1CfgCmdStatus"))
)
if mibBuilder.loadTexts:
    t3T1ConfigTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ERI-DNX-T3-MIB",
    **{"dnxT3": dnxT3,
       "dnxT3Enterprise": dnxT3Enterprise,
       "t3PortConfigTrap": t3PortConfigTrap,
       "t3T1ConfigTrap": t3T1ConfigTrap,
       "t3Config": t3Config,
       "t3PortConfigTable": t3PortConfigTable,
       "t3PortConfigEntry": t3PortConfigEntry,
       "t3CfgAddr": t3CfgAddr,
       "t3CfgResource": t3CfgResource,
       "t3CfgCircuitName": t3CfgCircuitName,
       "t3FacilityId": t3FacilityId,
       "t3EquipmentId": t3EquipmentId,
       "t3Location": t3Location,
       "t3FrameId": t3FrameId,
       "t3UnitName": t3UnitName,
       "t3PortNumber": t3PortNumber,
       "t3Generator": t3Generator,
       "t3M13OpMode": t3M13OpMode,
       "t3RcvLoopTiming": t3RcvLoopTiming,
       "t3ShortCable": t3ShortCable,
       "t3M13RemLoop": t3M13RemLoop,
       "t3RcvAIS": t3RcvAIS,
       "t3XmtAIS": t3XmtAIS,
       "t3CmdStatus": t3CmdStatus,
       "t3T1LinkConfigTable": t3T1LinkConfigTable,
       "t3T1LinkConfigEntry": t3T1LinkConfigEntry,
       "t3T1CfgLinkAddr": t3T1CfgLinkAddr,
       "t3T1CfgResource": t3T1CfgResource,
       "t3T1CfgLinkName": t3T1CfgLinkName,
       "t3T1Status": t3T1Status,
       "t3T1Framing": t3T1Framing,
       "t3T1Density": t3T1Density,
       "t3T1NetLoop": t3T1NetLoop,
       "t3T1YelAlrm": t3T1YelAlrm,
       "t3T1RecoverTime": t3T1RecoverTime,
       "t3T1EsfFormat": t3T1EsfFormat,
       "t3T1IdleCode": t3T1IdleCode,
       "t3T1CfgCmdStatus": t3T1CfgCmdStatus,
       "t3Diag": t3Diag,
       "eriDNXT3MIB": eriDNXT3MIB}
)
