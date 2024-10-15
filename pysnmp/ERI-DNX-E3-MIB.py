# SNMP MIB module (ERI-DNX-E3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ERI-DNX-E3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:23 2024
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

(DataSwitch,
 DecisionType,
 FunctionSwitch,
 LinkCmdStatus,
 LinkPortAddress,
 OneByteField,
 PortStatus,
 devices,
 trapSequence) = mibBuilder.importSymbols(
    "ERI-DNX-SMC-MIB",
    "DataSwitch",
    "DecisionType",
    "FunctionSwitch",
    "LinkCmdStatus",
    "LinkPortAddress",
    "OneByteField",
    "PortStatus",
    "devices",
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

eriDNXE3MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 644, 3, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DnxE3_ObjectIdentity = ObjectIdentity
dnxE3 = _DnxE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8)
)
_DnxE3Enterprise_ObjectIdentity = ObjectIdentity
dnxE3Enterprise = _DnxE3Enterprise_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 0)
)
if mibBuilder.loadTexts:
    dnxE3Enterprise.setStatus("current")
_E3Config_ObjectIdentity = ObjectIdentity
e3Config = _E3Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1)
)
_E3PortConfigTable_Object = MibTable
e3PortConfigTable = _E3PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 1)
)
if mibBuilder.loadTexts:
    e3PortConfigTable.setStatus("current")
_E3PortConfigEntry_Object = MibTableRow
e3PortConfigEntry = _E3PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 1, 1)
)
e3PortConfigEntry.setIndexNames(
    (0, "ERI-DNX-E3-MIB", "e3PortCfgAddr"),
)
if mibBuilder.loadTexts:
    e3PortConfigEntry.setStatus("current")
_E3PortCfgAddr_Type = LinkPortAddress
_E3PortCfgAddr_Object = MibTableColumn
e3PortCfgAddr = _E3PortCfgAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 1, 1, 1),
    _E3PortCfgAddr_Type()
)
e3PortCfgAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3PortCfgAddr.setStatus("current")
_E3PortCfgResource_Type = Integer32
_E3PortCfgResource_Object = MibTableColumn
e3PortCfgResource = _E3PortCfgResource_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 1, 1, 2),
    _E3PortCfgResource_Type()
)
e3PortCfgResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3PortCfgResource.setStatus("current")


class _E3Timing_Type(Integer32):
    """Custom type e3Timing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("internal", 0),
          ("loop", 1))
    )


_E3Timing_Type.__name__ = "Integer32"
_E3Timing_Object = MibTableColumn
e3Timing = _E3Timing_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 1, 1, 3),
    _E3Timing_Type()
)
e3Timing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3Timing.setStatus("current")
_E3ShortCable_Type = DecisionType
_E3ShortCable_Object = MibTableColumn
e3ShortCable = _E3ShortCable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 1, 1, 4),
    _E3ShortCable_Type()
)
e3ShortCable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3ShortCable.setStatus("current")
_E3CmdStatus_Type = LinkCmdStatus
_E3CmdStatus_Object = MibTableColumn
e3CmdStatus = _E3CmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 1, 1, 5),
    _E3CmdStatus_Type()
)
e3CmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3CmdStatus.setStatus("current")
_E3E1LinkConfigTable_Object = MibTable
e3E1LinkConfigTable = _E3E1LinkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 2)
)
if mibBuilder.loadTexts:
    e3E1LinkConfigTable.setStatus("current")
_E3E1LinkConfigEntry_Object = MibTableRow
e3E1LinkConfigEntry = _E3E1LinkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 2, 1)
)
e3E1LinkConfigEntry.setIndexNames(
    (0, "ERI-DNX-E3-MIB", "e3E1CfgLinkAddr"),
)
if mibBuilder.loadTexts:
    e3E1LinkConfigEntry.setStatus("current")
_E3E1CfgLinkAddr_Type = LinkPortAddress
_E3E1CfgLinkAddr_Object = MibTableColumn
e3E1CfgLinkAddr = _E3E1CfgLinkAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 2, 1, 1),
    _E3E1CfgLinkAddr_Type()
)
e3E1CfgLinkAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3E1CfgLinkAddr.setStatus("current")
_E3E1CfgResource_Type = Integer32
_E3E1CfgResource_Object = MibTableColumn
e3E1CfgResource = _E3E1CfgResource_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 2, 1, 2),
    _E3E1CfgResource_Type()
)
e3E1CfgResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3E1CfgResource.setStatus("current")


class _E3E1CfgLinkName_Type(DisplayString):
    """Custom type e3E1CfgLinkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_E3E1CfgLinkName_Type.__name__ = "DisplayString"
_E3E1CfgLinkName_Object = MibTableColumn
e3E1CfgLinkName = _E3E1CfgLinkName_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 2, 1, 3),
    _E3E1CfgLinkName_Type()
)
e3E1CfgLinkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3E1CfgLinkName.setStatus("current")
_E3E1Status_Type = PortStatus
_E3E1Status_Object = MibTableColumn
e3E1Status = _E3E1Status_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 2, 1, 4),
    _E3E1Status_Type()
)
e3E1Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3E1Status.setStatus("current")


class _E3E1Clear_Type(Integer32):
    """Custom type e3E1Clear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("framed", 1),
          ("unframed", 2))
    )


_E3E1Clear_Type.__name__ = "Integer32"
_E3E1Clear_Object = MibTableColumn
e3E1Clear = _E3E1Clear_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 2, 1, 5),
    _E3E1Clear_Type()
)
e3E1Clear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3E1Clear.setStatus("current")


class _E3E1Framing_Type(Integer32):
    """Custom type e3E1Framing based on Integer32"""
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
        *(("e1", 0),
          ("e1Cas", 2),
          ("e1CasCrc", 3),
          ("e1Crc", 1),
          ("e1Unframed", 4))
    )


_E3E1Framing_Type.__name__ = "Integer32"
_E3E1Framing_Object = MibTableColumn
e3E1Framing = _E3E1Framing_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 2, 1, 6),
    _E3E1Framing_Type()
)
e3E1Framing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3E1Framing.setStatus("current")
_E3E1NetLoop_Type = FunctionSwitch
_E3E1NetLoop_Object = MibTableColumn
e3E1NetLoop = _E3E1NetLoop_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 2, 1, 7),
    _E3E1NetLoop_Type()
)
e3E1NetLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3E1NetLoop.setStatus("current")
_E3E1RAI_Type = DecisionType
_E3E1RAI_Object = MibTableColumn
e3E1RAI = _E3E1RAI_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 2, 1, 8),
    _E3E1RAI_Type()
)
e3E1RAI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3E1RAI.setStatus("current")


class _E3E1UnusedTSs_Type(Integer32):
    """Custom type e3E1UnusedTSs based on Integer32"""
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


_E3E1UnusedTSs_Type.__name__ = "Integer32"
_E3E1UnusedTSs_Object = MibTableColumn
e3E1UnusedTSs = _E3E1UnusedTSs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 2, 1, 9),
    _E3E1UnusedTSs_Type()
)
e3E1UnusedTSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3E1UnusedTSs.setStatus("current")
_E3E1NationalBits_Type = OneByteField
_E3E1NationalBits_Object = MibTableColumn
e3E1NationalBits = _E3E1NationalBits_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 2, 1, 10),
    _E3E1NationalBits_Type()
)
e3E1NationalBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3E1NationalBits.setStatus("current")
_E3E1CfgCmdStatus_Type = LinkCmdStatus
_E3E1CfgCmdStatus_Object = MibTableColumn
e3E1CfgCmdStatus = _E3E1CfgCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 2, 1, 11),
    _E3E1CfgCmdStatus_Type()
)
e3E1CfgCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3E1CfgCmdStatus.setStatus("current")
_E3E1InterNational_Type = OneByteField
_E3E1InterNational_Object = MibTableColumn
e3E1InterNational = _E3E1InterNational_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 2, 1, 12),
    _E3E1InterNational_Type()
)
e3E1InterNational.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3E1InterNational.setStatus("current")
_E3Diag_ObjectIdentity = ObjectIdentity
e3Diag = _E3Diag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2)
)
_E3FramerStatusTable_Object = MibTable
e3FramerStatusTable = _E3FramerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1)
)
if mibBuilder.loadTexts:
    e3FramerStatusTable.setStatus("current")
_E3FramerStatusEntry_Object = MibTableRow
e3FramerStatusEntry = _E3FramerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1)
)
e3FramerStatusEntry.setIndexNames(
    (0, "ERI-DNX-E3-MIB", "e3FramerStatusAddr"),
)
if mibBuilder.loadTexts:
    e3FramerStatusEntry.setStatus("current")
_E3FramerStatusAddr_Type = LinkPortAddress
_E3FramerStatusAddr_Object = MibTableColumn
e3FramerStatusAddr = _E3FramerStatusAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 1),
    _E3FramerStatusAddr_Type()
)
e3FramerStatusAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3FramerStatusAddr.setStatus("current")
_E3FramerStatusResource_Type = Integer32
_E3FramerStatusResource_Object = MibTableColumn
e3FramerStatusResource = _E3FramerStatusResource_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 2),
    _E3FramerStatusResource_Type()
)
e3FramerStatusResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3FramerStatusResource.setStatus("current")


class _E3FramerStatusState_Type(Integer32):
    """Custom type e3FramerStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              8,
              32,
              64,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("ais", 8),
          ("errors", 2147483647),
          ("lof", 32),
          ("los", 64),
          ("ok", 0))
    )


_E3FramerStatusState_Type.__name__ = "Integer32"
_E3FramerStatusState_Object = MibTableColumn
e3FramerStatusState = _E3FramerStatusState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 3),
    _E3FramerStatusState_Type()
)
e3FramerStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3FramerStatusState.setStatus("current")
_E3FramerStatusErrSecs_Type = Counter32
_E3FramerStatusErrSecs_Object = MibTableColumn
e3FramerStatusErrSecs = _E3FramerStatusErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 4),
    _E3FramerStatusErrSecs_Type()
)
e3FramerStatusErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3FramerStatusErrSecs.setStatus("current")
_E3FramerStatusOOFErrs_Type = Counter32
_E3FramerStatusOOFErrs_Object = MibTableColumn
e3FramerStatusOOFErrs = _E3FramerStatusOOFErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 5),
    _E3FramerStatusOOFErrs_Type()
)
e3FramerStatusOOFErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3FramerStatusOOFErrs.setStatus("current")
_E3FramerStatusAISSecs_Type = Counter32
_E3FramerStatusAISSecs_Object = MibTableColumn
e3FramerStatusAISSecs = _E3FramerStatusAISSecs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 6),
    _E3FramerStatusAISSecs_Type()
)
e3FramerStatusAISSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3FramerStatusAISSecs.setStatus("current")
_E3FramerStatusFramingErrs_Type = Counter32
_E3FramerStatusFramingErrs_Object = MibTableColumn
e3FramerStatusFramingErrs = _E3FramerStatusFramingErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 7),
    _E3FramerStatusFramingErrs_Type()
)
e3FramerStatusFramingErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3FramerStatusFramingErrs.setStatus("current")


class _E3FramerStatusLoop_Type(Integer32):
    """Custom type e3FramerStatusLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              37,
              38)
        )
    )
    namedValues = NamedValues(
        *(("e3-line", 3),
          ("e3-local", 1),
          ("e3-payload", 4),
          ("liu-line", 38),
          ("liu-local", 37),
          ("off", 0))
    )


_E3FramerStatusLoop_Type.__name__ = "Integer32"
_E3FramerStatusLoop_Object = MibTableColumn
e3FramerStatusLoop = _E3FramerStatusLoop_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 8),
    _E3FramerStatusLoop_Type()
)
e3FramerStatusLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3FramerStatusLoop.setStatus("current")


class _E3FramerStatusBertState_Type(Integer32):
    """Custom type e3FramerStatusBertState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(50,
              61,
              62)
        )
    )
    namedValues = NamedValues(
        *(("bertOff", 50),
          ("framed-2-15th-inv", 62),
          ("framed-2047", 61))
    )


_E3FramerStatusBertState_Type.__name__ = "Integer32"
_E3FramerStatusBertState_Object = MibTableColumn
e3FramerStatusBertState = _E3FramerStatusBertState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 9),
    _E3FramerStatusBertState_Type()
)
e3FramerStatusBertState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3FramerStatusBertState.setStatus("current")
_E3FramerStatusBertSecs_Type = Counter32
_E3FramerStatusBertSecs_Object = MibTableColumn
e3FramerStatusBertSecs = _E3FramerStatusBertSecs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 10),
    _E3FramerStatusBertSecs_Type()
)
e3FramerStatusBertSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3FramerStatusBertSecs.setStatus("current")
_E3FramerStatusBertErrSecs_Type = Counter32
_E3FramerStatusBertErrSecs_Object = MibTableColumn
e3FramerStatusBertErrSecs = _E3FramerStatusBertErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 11),
    _E3FramerStatusBertErrSecs_Type()
)
e3FramerStatusBertErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3FramerStatusBertErrSecs.setStatus("current")
_E3FramerStatusBertSync_Type = DataSwitch
_E3FramerStatusBertSync_Object = MibTableColumn
e3FramerStatusBertSync = _E3FramerStatusBertSync_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 12),
    _E3FramerStatusBertSync_Type()
)
e3FramerStatusBertSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3FramerStatusBertSync.setStatus("current")
_E3FramerStatusLiuRLOSs_Type = Counter32
_E3FramerStatusLiuRLOSs_Object = MibTableColumn
e3FramerStatusLiuRLOSs = _E3FramerStatusLiuRLOSs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 13),
    _E3FramerStatusLiuRLOSs_Type()
)
e3FramerStatusLiuRLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3FramerStatusLiuRLOSs.setStatus("current")
_E3FramerStatusLiuRLOLs_Type = Counter32
_E3FramerStatusLiuRLOLs_Object = MibTableColumn
e3FramerStatusLiuRLOLs = _E3FramerStatusLiuRLOLs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 14),
    _E3FramerStatusLiuRLOLs_Type()
)
e3FramerStatusLiuRLOLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3FramerStatusLiuRLOLs.setStatus("current")
_E3FramerStatusLiuLCVs_Type = Counter32
_E3FramerStatusLiuLCVs_Object = MibTableColumn
e3FramerStatusLiuLCVs = _E3FramerStatusLiuLCVs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 15),
    _E3FramerStatusLiuLCVs_Type()
)
e3FramerStatusLiuLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3FramerStatusLiuLCVs.setStatus("current")


class _E3FramerStatusInsErrMode_Type(Integer32):
    """Custom type e3FramerStatusInsErrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("frame-alignment", 2)
    )


_E3FramerStatusInsErrMode_Type.__name__ = "Integer32"
_E3FramerStatusInsErrMode_Object = MibTableColumn
e3FramerStatusInsErrMode = _E3FramerStatusInsErrMode_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 16),
    _E3FramerStatusInsErrMode_Type()
)
e3FramerStatusInsErrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3FramerStatusInsErrMode.setStatus("current")


class _E3FramerStatusCmdStatus_Type(Integer32):
    """Custom type e3FramerStatusCmdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              14,
              16,
              101,
              114,
              116,
              200,
              202,
              203,
              205,
              206,
              208,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("clear-successful", 114),
          ("clearErrors", 14),
          ("err-field-cannot-be-set", 206),
          ("err-general-framer-error", 200),
          ("err-invalid-bert-type", 203),
          ("err-invalid-command", 208),
          ("err-invalid-loop-type", 202),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-snmp-parse-failed", 500),
          ("err-test-in-progress", 205),
          ("insert-successful", 116),
          ("insertError", 16),
          ("ready-for-command", 0),
          ("update", 1),
          ("update-successful", 101))
    )


_E3FramerStatusCmdStatus_Type.__name__ = "Integer32"
_E3FramerStatusCmdStatus_Object = MibTableColumn
e3FramerStatusCmdStatus = _E3FramerStatusCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 17),
    _E3FramerStatusCmdStatus_Type()
)
e3FramerStatusCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3FramerStatusCmdStatus.setStatus("current")

# Managed Objects groups


# Notification objects

e3PortConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 0, 1)
)
e3PortConfigTrap.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-E3-MIB", "e3PortCfgAddr"),
        ("ERI-DNX-E3-MIB", "e3CmdStatus"))
)
if mibBuilder.loadTexts:
    e3PortConfigTrap.setStatus(
        "current"
    )

e3E1ConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 0, 2)
)
e3E1ConfigTrap.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-E3-MIB", "e3E1CfgLinkAddr"),
        ("ERI-DNX-E3-MIB", "e3E1CfgCmdStatus"))
)
if mibBuilder.loadTexts:
    e3E1ConfigTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ERI-DNX-E3-MIB",
    **{"dnxE3": dnxE3,
       "dnxE3Enterprise": dnxE3Enterprise,
       "e3PortConfigTrap": e3PortConfigTrap,
       "e3E1ConfigTrap": e3E1ConfigTrap,
       "e3Config": e3Config,
       "e3PortConfigTable": e3PortConfigTable,
       "e3PortConfigEntry": e3PortConfigEntry,
       "e3PortCfgAddr": e3PortCfgAddr,
       "e3PortCfgResource": e3PortCfgResource,
       "e3Timing": e3Timing,
       "e3ShortCable": e3ShortCable,
       "e3CmdStatus": e3CmdStatus,
       "e3E1LinkConfigTable": e3E1LinkConfigTable,
       "e3E1LinkConfigEntry": e3E1LinkConfigEntry,
       "e3E1CfgLinkAddr": e3E1CfgLinkAddr,
       "e3E1CfgResource": e3E1CfgResource,
       "e3E1CfgLinkName": e3E1CfgLinkName,
       "e3E1Status": e3E1Status,
       "e3E1Clear": e3E1Clear,
       "e3E1Framing": e3E1Framing,
       "e3E1NetLoop": e3E1NetLoop,
       "e3E1RAI": e3E1RAI,
       "e3E1UnusedTSs": e3E1UnusedTSs,
       "e3E1NationalBits": e3E1NationalBits,
       "e3E1CfgCmdStatus": e3E1CfgCmdStatus,
       "e3E1InterNational": e3E1InterNational,
       "e3Diag": e3Diag,
       "e3FramerStatusTable": e3FramerStatusTable,
       "e3FramerStatusEntry": e3FramerStatusEntry,
       "e3FramerStatusAddr": e3FramerStatusAddr,
       "e3FramerStatusResource": e3FramerStatusResource,
       "e3FramerStatusState": e3FramerStatusState,
       "e3FramerStatusErrSecs": e3FramerStatusErrSecs,
       "e3FramerStatusOOFErrs": e3FramerStatusOOFErrs,
       "e3FramerStatusAISSecs": e3FramerStatusAISSecs,
       "e3FramerStatusFramingErrs": e3FramerStatusFramingErrs,
       "e3FramerStatusLoop": e3FramerStatusLoop,
       "e3FramerStatusBertState": e3FramerStatusBertState,
       "e3FramerStatusBertSecs": e3FramerStatusBertSecs,
       "e3FramerStatusBertErrSecs": e3FramerStatusBertErrSecs,
       "e3FramerStatusBertSync": e3FramerStatusBertSync,
       "e3FramerStatusLiuRLOSs": e3FramerStatusLiuRLOSs,
       "e3FramerStatusLiuRLOLs": e3FramerStatusLiuRLOLs,
       "e3FramerStatusLiuLCVs": e3FramerStatusLiuLCVs,
       "e3FramerStatusInsErrMode": e3FramerStatusInsErrMode,
       "e3FramerStatusCmdStatus": e3FramerStatusCmdStatus,
       "eriDNXE3MIB": eriDNXE3MIB}
)
