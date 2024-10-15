# SNMP MIB module (ERI-DNX-STS1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ERI-DNX-STS1-MIB
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
 trapSequence) = mibBuilder.importSymbols(
    "ERI-DNX-SMC-MIB",
    "DecisionType",
    "FunctionSwitch",
    "LinkCmdStatus",
    "LinkPortAddress",
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

eriDNXSts1MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 644, 3, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VtGroupType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vt1-5-ds1", 1),
          ("vt2-0-e1", 0))
    )



# MIB Managed Objects in the order of their OIDs

_DnxSTS1_ObjectIdentity = ObjectIdentity
dnxSTS1 = _DnxSTS1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3)
)
_DnxSTS1Enterprise_ObjectIdentity = ObjectIdentity
dnxSTS1Enterprise = _DnxSTS1Enterprise_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 0)
)
if mibBuilder.loadTexts:
    dnxSTS1Enterprise.setStatus("current")
_Sts1Config_ObjectIdentity = ObjectIdentity
sts1Config = _Sts1Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1)
)
_Sts1MapperConfigTable_Object = MibTable
sts1MapperConfigTable = _Sts1MapperConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    sts1MapperConfigTable.setStatus("current")
_Sts1MapperConfigEntry_Object = MibTableRow
sts1MapperConfigEntry = _Sts1MapperConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 1, 1)
)
sts1MapperConfigEntry.setIndexNames(
    (0, "ERI-DNX-STS1-MIB", "sts1MapperAddr"),
)
if mibBuilder.loadTexts:
    sts1MapperConfigEntry.setStatus("current")
_Sts1MapperAddr_Type = LinkPortAddress
_Sts1MapperAddr_Object = MibTableColumn
sts1MapperAddr = _Sts1MapperAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 1, 1, 1),
    _Sts1MapperAddr_Type()
)
sts1MapperAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1MapperAddr.setStatus("current")
_Sts1MapperResource_Type = Integer32
_Sts1MapperResource_Object = MibTableColumn
sts1MapperResource = _Sts1MapperResource_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 1, 1, 2),
    _Sts1MapperResource_Type()
)
sts1MapperResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1MapperResource.setStatus("current")
_Sts1VtGroup1_Type = VtGroupType
_Sts1VtGroup1_Object = MibTableColumn
sts1VtGroup1 = _Sts1VtGroup1_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 1, 1, 3),
    _Sts1VtGroup1_Type()
)
sts1VtGroup1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1VtGroup1.setStatus("current")
_Sts1VtGroup2_Type = VtGroupType
_Sts1VtGroup2_Object = MibTableColumn
sts1VtGroup2 = _Sts1VtGroup2_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 1, 1, 4),
    _Sts1VtGroup2_Type()
)
sts1VtGroup2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1VtGroup2.setStatus("current")
_Sts1VtGroup3_Type = VtGroupType
_Sts1VtGroup3_Object = MibTableColumn
sts1VtGroup3 = _Sts1VtGroup3_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 1, 1, 5),
    _Sts1VtGroup3_Type()
)
sts1VtGroup3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1VtGroup3.setStatus("current")
_Sts1VtGroup4_Type = VtGroupType
_Sts1VtGroup4_Object = MibTableColumn
sts1VtGroup4 = _Sts1VtGroup4_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 1, 1, 6),
    _Sts1VtGroup4_Type()
)
sts1VtGroup4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1VtGroup4.setStatus("current")
_Sts1VtGroup5_Type = VtGroupType
_Sts1VtGroup5_Object = MibTableColumn
sts1VtGroup5 = _Sts1VtGroup5_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 1, 1, 7),
    _Sts1VtGroup5_Type()
)
sts1VtGroup5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1VtGroup5.setStatus("current")
_Sts1VtGroup6_Type = VtGroupType
_Sts1VtGroup6_Object = MibTableColumn
sts1VtGroup6 = _Sts1VtGroup6_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 1, 1, 8),
    _Sts1VtGroup6_Type()
)
sts1VtGroup6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1VtGroup6.setStatus("current")
_Sts1VtGroup7_Type = VtGroupType
_Sts1VtGroup7_Object = MibTableColumn
sts1VtGroup7 = _Sts1VtGroup7_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 1, 1, 9),
    _Sts1VtGroup7_Type()
)
sts1VtGroup7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1VtGroup7.setStatus("current")


class _Sts1VtMapping_Type(Integer32):
    """Custom type sts1VtMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sequencialFrm", 1),
          ("standardVT", 0))
    )


_Sts1VtMapping_Type.__name__ = "Integer32"
_Sts1VtMapping_Object = MibTableColumn
sts1VtMapping = _Sts1VtMapping_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 1, 1, 10),
    _Sts1VtMapping_Type()
)
sts1VtMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1VtMapping.setStatus("current")


class _Sts1Timing_Type(Integer32):
    """Custom type sts1Timing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ec1-Line", 1),
          ("internal", 0))
    )


_Sts1Timing_Type.__name__ = "Integer32"
_Sts1Timing_Object = MibTableColumn
sts1Timing = _Sts1Timing_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 1, 1, 11),
    _Sts1Timing_Type()
)
sts1Timing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts1Timing.setStatus("current")
_Sts1ShortCable_Type = FunctionSwitch
_Sts1ShortCable_Object = MibTableColumn
sts1ShortCable = _Sts1ShortCable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 1, 1, 12),
    _Sts1ShortCable_Type()
)
sts1ShortCable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts1ShortCable.setStatus("current")
_Sts1MaprCmdStatus_Type = LinkCmdStatus
_Sts1MaprCmdStatus_Object = MibTableColumn
sts1MaprCmdStatus = _Sts1MaprCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 1, 1, 13),
    _Sts1MaprCmdStatus_Type()
)
sts1MaprCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts1MaprCmdStatus.setStatus("current")
_Sts1T1E1LinkConfigTable_Object = MibTable
sts1T1E1LinkConfigTable = _Sts1T1E1LinkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    sts1T1E1LinkConfigTable.setStatus("current")
_Sts1T1E1LinkConfigEntry_Object = MibTableRow
sts1T1E1LinkConfigEntry = _Sts1T1E1LinkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 2, 1)
)
sts1T1E1LinkConfigEntry.setIndexNames(
    (0, "ERI-DNX-STS1-MIB", "sts1T1E1CfgLinkAddr"),
)
if mibBuilder.loadTexts:
    sts1T1E1LinkConfigEntry.setStatus("current")
_Sts1T1E1CfgLinkAddr_Type = LinkPortAddress
_Sts1T1E1CfgLinkAddr_Object = MibTableColumn
sts1T1E1CfgLinkAddr = _Sts1T1E1CfgLinkAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 2, 1, 1),
    _Sts1T1E1CfgLinkAddr_Type()
)
sts1T1E1CfgLinkAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1T1E1CfgLinkAddr.setStatus("current")
_Sts1T1E1CfgResource_Type = Integer32
_Sts1T1E1CfgResource_Object = MibTableColumn
sts1T1E1CfgResource = _Sts1T1E1CfgResource_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 2, 1, 2),
    _Sts1T1E1CfgResource_Type()
)
sts1T1E1CfgResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1T1E1CfgResource.setStatus("current")


class _Sts1T1E1CfgLinkName_Type(DisplayString):
    """Custom type sts1T1E1CfgLinkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Sts1T1E1CfgLinkName_Type.__name__ = "DisplayString"
_Sts1T1E1CfgLinkName_Object = MibTableColumn
sts1T1E1CfgLinkName = _Sts1T1E1CfgLinkName_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 2, 1, 3),
    _Sts1T1E1CfgLinkName_Type()
)
sts1T1E1CfgLinkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts1T1E1CfgLinkName.setStatus("current")
_Sts1T1E1Status_Type = PortStatus
_Sts1T1E1Status_Object = MibTableColumn
sts1T1E1Status = _Sts1T1E1Status_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 2, 1, 4),
    _Sts1T1E1Status_Type()
)
sts1T1E1Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts1T1E1Status.setStatus("current")


class _Sts1T1E1Clear_Type(Integer32):
    """Custom type sts1T1E1Clear based on Integer32"""
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


_Sts1T1E1Clear_Type.__name__ = "Integer32"
_Sts1T1E1Clear_Object = MibTableColumn
sts1T1E1Clear = _Sts1T1E1Clear_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 2, 1, 5),
    _Sts1T1E1Clear_Type()
)
sts1T1E1Clear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts1T1E1Clear.setStatus("current")


class _Sts1T1E1Framing_Type(Integer32):
    """Custom type sts1T1E1Framing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("t1D4", 6),
          ("t1Esf", 5),
          ("t1Unframed", 7))
    )


_Sts1T1E1Framing_Type.__name__ = "Integer32"
_Sts1T1E1Framing_Object = MibTableColumn
sts1T1E1Framing = _Sts1T1E1Framing_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 2, 1, 6),
    _Sts1T1E1Framing_Type()
)
sts1T1E1Framing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts1T1E1Framing.setStatus("current")
_Sts1T1E1NetLoop_Type = FunctionSwitch
_Sts1T1E1NetLoop_Object = MibTableColumn
sts1T1E1NetLoop = _Sts1T1E1NetLoop_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 2, 1, 7),
    _Sts1T1E1NetLoop_Type()
)
sts1T1E1NetLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts1T1E1NetLoop.setStatus("current")
_Sts1T1E1YelAlrm_Type = DecisionType
_Sts1T1E1YelAlrm_Object = MibTableColumn
sts1T1E1YelAlrm = _Sts1T1E1YelAlrm_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 2, 1, 8),
    _Sts1T1E1YelAlrm_Type()
)
sts1T1E1YelAlrm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts1T1E1YelAlrm.setStatus("current")


class _Sts1T1E1RecoverTime_Type(Integer32):
    """Custom type sts1T1E1RecoverTime based on Integer32"""
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


_Sts1T1E1RecoverTime_Type.__name__ = "Integer32"
_Sts1T1E1RecoverTime_Object = MibTableColumn
sts1T1E1RecoverTime = _Sts1T1E1RecoverTime_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 2, 1, 9),
    _Sts1T1E1RecoverTime_Type()
)
sts1T1E1RecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts1T1E1RecoverTime.setStatus("current")


class _Sts1T1E1EsfFormat_Type(Integer32):
    """Custom type sts1T1E1EsfFormat based on Integer32"""
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


_Sts1T1E1EsfFormat_Type.__name__ = "Integer32"
_Sts1T1E1EsfFormat_Object = MibTableColumn
sts1T1E1EsfFormat = _Sts1T1E1EsfFormat_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 2, 1, 10),
    _Sts1T1E1EsfFormat_Type()
)
sts1T1E1EsfFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts1T1E1EsfFormat.setStatus("current")


class _Sts1T1E1IdleCode_Type(Integer32):
    """Custom type sts1T1E1IdleCode based on Integer32"""
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


_Sts1T1E1IdleCode_Type.__name__ = "Integer32"
_Sts1T1E1IdleCode_Object = MibTableColumn
sts1T1E1IdleCode = _Sts1T1E1IdleCode_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 2, 1, 11),
    _Sts1T1E1IdleCode_Type()
)
sts1T1E1IdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts1T1E1IdleCode.setStatus("current")
_Sts1T1E1CfgCmdStatus_Type = LinkCmdStatus
_Sts1T1E1CfgCmdStatus_Object = MibTableColumn
sts1T1E1CfgCmdStatus = _Sts1T1E1CfgCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 2, 1, 12),
    _Sts1T1E1CfgCmdStatus_Type()
)
sts1T1E1CfgCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts1T1E1CfgCmdStatus.setStatus("current")
_Sts1T1E1Gr303Facility_Type = DecisionType
_Sts1T1E1Gr303Facility_Object = MibTableColumn
sts1T1E1Gr303Facility = _Sts1T1E1Gr303Facility_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 2, 1, 13),
    _Sts1T1E1Gr303Facility_Type()
)
sts1T1E1Gr303Facility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1T1E1Gr303Facility.setStatus("obsolete")
_Sts1Diag_ObjectIdentity = ObjectIdentity
sts1Diag = _Sts1Diag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2)
)
_Sts1MapperStatusTable_Object = MibTable
sts1MapperStatusTable = _Sts1MapperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    sts1MapperStatusTable.setStatus("current")
_Sts1MapperStatusEntry_Object = MibTableRow
sts1MapperStatusEntry = _Sts1MapperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 1, 1)
)
sts1MapperStatusEntry.setIndexNames(
    (0, "ERI-DNX-STS1-MIB", "sts1MapperStatusAddr"),
)
if mibBuilder.loadTexts:
    sts1MapperStatusEntry.setStatus("current")
_Sts1MapperStatusAddr_Type = LinkPortAddress
_Sts1MapperStatusAddr_Object = MibTableColumn
sts1MapperStatusAddr = _Sts1MapperStatusAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 1, 1, 1),
    _Sts1MapperStatusAddr_Type()
)
sts1MapperStatusAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1MapperStatusAddr.setStatus("current")
_Sts1MapperStatusResource_Type = Integer32
_Sts1MapperStatusResource_Object = MibTableColumn
sts1MapperStatusResource = _Sts1MapperStatusResource_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 1, 1, 2),
    _Sts1MapperStatusResource_Type()
)
sts1MapperStatusResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1MapperStatusResource.setStatus("current")


class _Sts1MapperStatusState_Type(Integer32):
    """Custom type sts1MapperStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              32,
              256,
              512,
              1024,
              8192,
              131072,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("ais", 1024),
          ("errors", 2147483647),
          ("lof", 32),
          ("lomf", 131072),
          ("lop", 256),
          ("los", 8192),
          ("ok", 0),
          ("oof", 512))
    )


_Sts1MapperStatusState_Type.__name__ = "Integer32"
_Sts1MapperStatusState_Object = MibTableColumn
sts1MapperStatusState = _Sts1MapperStatusState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 1, 1, 3),
    _Sts1MapperStatusState_Type()
)
sts1MapperStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1MapperStatusState.setStatus("current")
_Sts1MapperStatusLOSErrs_Type = Counter32
_Sts1MapperStatusLOSErrs_Object = MibTableColumn
sts1MapperStatusLOSErrs = _Sts1MapperStatusLOSErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 1, 1, 4),
    _Sts1MapperStatusLOSErrs_Type()
)
sts1MapperStatusLOSErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1MapperStatusLOSErrs.setStatus("current")
_Sts1MapperStatusOOFErrs_Type = Counter32
_Sts1MapperStatusOOFErrs_Object = MibTableColumn
sts1MapperStatusOOFErrs = _Sts1MapperStatusOOFErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 1, 1, 5),
    _Sts1MapperStatusOOFErrs_Type()
)
sts1MapperStatusOOFErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1MapperStatusOOFErrs.setStatus("current")
_Sts1MapperStatusLOFErrs_Type = Counter32
_Sts1MapperStatusLOFErrs_Object = MibTableColumn
sts1MapperStatusLOFErrs = _Sts1MapperStatusLOFErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 1, 1, 6),
    _Sts1MapperStatusLOFErrs_Type()
)
sts1MapperStatusLOFErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1MapperStatusLOFErrs.setStatus("current")
_Sts1MapperStatusLOPtrErrs_Type = Counter32
_Sts1MapperStatusLOPtrErrs_Object = MibTableColumn
sts1MapperStatusLOPtrErrs = _Sts1MapperStatusLOPtrErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 1, 1, 7),
    _Sts1MapperStatusLOPtrErrs_Type()
)
sts1MapperStatusLOPtrErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1MapperStatusLOPtrErrs.setStatus("current")
_Sts1MapperStatusAISErrs_Type = Counter32
_Sts1MapperStatusAISErrs_Object = MibTableColumn
sts1MapperStatusAISErrs = _Sts1MapperStatusAISErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 1, 1, 8),
    _Sts1MapperStatusAISErrs_Type()
)
sts1MapperStatusAISErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1MapperStatusAISErrs.setStatus("current")
_Sts1MapperStatusMultiFErrs_Type = Counter32
_Sts1MapperStatusMultiFErrs_Object = MibTableColumn
sts1MapperStatusMultiFErrs = _Sts1MapperStatusMultiFErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 1, 1, 9),
    _Sts1MapperStatusMultiFErrs_Type()
)
sts1MapperStatusMultiFErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1MapperStatusMultiFErrs.setStatus("current")
_Sts1MapperStatusRxTraceErrs_Type = Counter32
_Sts1MapperStatusRxTraceErrs_Object = MibTableColumn
sts1MapperStatusRxTraceErrs = _Sts1MapperStatusRxTraceErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 1, 1, 10),
    _Sts1MapperStatusRxTraceErrs_Type()
)
sts1MapperStatusRxTraceErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1MapperStatusRxTraceErrs.setStatus("current")
_Sts1MapperStatusTotErrSecs_Type = Counter32
_Sts1MapperStatusTotErrSecs_Object = MibTableColumn
sts1MapperStatusTotErrSecs = _Sts1MapperStatusTotErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 1, 1, 11),
    _Sts1MapperStatusTotErrSecs_Type()
)
sts1MapperStatusTotErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1MapperStatusTotErrSecs.setStatus("current")


class _Sts1MapperStatusCmdStatus_Type(Integer32):
    """Custom type sts1MapperStatusCmdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              14,
              101,
              114,
              200,
              206,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("clear-successful", 114),
          ("clearErrors", 14),
          ("err-field-cannot-be-set", 206),
          ("err-general-test-error", 200),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-snmp-parse-failed", 500),
          ("ready-for-command", 0),
          ("update", 1),
          ("update-successful", 101))
    )


_Sts1MapperStatusCmdStatus_Type.__name__ = "Integer32"
_Sts1MapperStatusCmdStatus_Object = MibTableColumn
sts1MapperStatusCmdStatus = _Sts1MapperStatusCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 1, 1, 12),
    _Sts1MapperStatusCmdStatus_Type()
)
sts1MapperStatusCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts1MapperStatusCmdStatus.setStatus("current")
_Sts1LIUTable_Object = MibTable
sts1LIUTable = _Sts1LIUTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 2)
)
if mibBuilder.loadTexts:
    sts1LIUTable.setStatus("current")
_Sts1LIUEntry_Object = MibTableRow
sts1LIUEntry = _Sts1LIUEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 2, 1)
)
sts1LIUEntry.setIndexNames(
    (0, "ERI-DNX-STS1-MIB", "sts1LIUAddr"),
)
if mibBuilder.loadTexts:
    sts1LIUEntry.setStatus("current")
_Sts1LIUAddr_Type = LinkPortAddress
_Sts1LIUAddr_Object = MibTableColumn
sts1LIUAddr = _Sts1LIUAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 2, 1, 1),
    _Sts1LIUAddr_Type()
)
sts1LIUAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1LIUAddr.setStatus("current")
_Sts1LIUResource_Type = Integer32
_Sts1LIUResource_Object = MibTableColumn
sts1LIUResource = _Sts1LIUResource_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 2, 1, 2),
    _Sts1LIUResource_Type()
)
sts1LIUResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1LIUResource.setStatus("current")


class _Sts1LIUBertState_Type(Integer32):
    """Custom type sts1LIUBertState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(44,
              45)
        )
    )
    namedValues = NamedValues(
        *(("liu-bert", 44),
          ("off", 45))
    )


_Sts1LIUBertState_Type.__name__ = "Integer32"
_Sts1LIUBertState_Object = MibTableColumn
sts1LIUBertState = _Sts1LIUBertState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 2, 1, 3),
    _Sts1LIUBertState_Type()
)
sts1LIUBertState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts1LIUBertState.setStatus("current")
_Sts1LIUBertErrSecs_Type = Counter32
_Sts1LIUBertErrSecs_Object = MibTableColumn
sts1LIUBertErrSecs = _Sts1LIUBertErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 2, 1, 4),
    _Sts1LIUBertErrSecs_Type()
)
sts1LIUBertErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1LIUBertErrSecs.setStatus("current")
_Sts1LIUBertDuration_Type = Counter32
_Sts1LIUBertDuration_Object = MibTableColumn
sts1LIUBertDuration = _Sts1LIUBertDuration_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 2, 1, 5),
    _Sts1LIUBertDuration_Type()
)
sts1LIUBertDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1LIUBertDuration.setStatus("current")


class _Sts1LIULoopType_Type(Integer32):
    """Custom type sts1LIULoopType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              39)
        )
    )
    namedValues = NamedValues(
        *(("liu", 39),
          ("mapper", 1),
          ("off", 0))
    )


_Sts1LIULoopType_Type.__name__ = "Integer32"
_Sts1LIULoopType_Object = MibTableColumn
sts1LIULoopType = _Sts1LIULoopType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 2, 1, 6),
    _Sts1LIULoopType_Type()
)
sts1LIULoopType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts1LIULoopType.setStatus("current")
_Sts1LIUDigitalErrs_Type = Counter32
_Sts1LIUDigitalErrs_Object = MibTableColumn
sts1LIUDigitalErrs = _Sts1LIUDigitalErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 2, 1, 7),
    _Sts1LIUDigitalErrs_Type()
)
sts1LIUDigitalErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1LIUDigitalErrs.setStatus("current")
_Sts1LIUAnalogErrs_Type = Counter32
_Sts1LIUAnalogErrs_Object = MibTableColumn
sts1LIUAnalogErrs = _Sts1LIUAnalogErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 2, 1, 8),
    _Sts1LIUAnalogErrs_Type()
)
sts1LIUAnalogErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1LIUAnalogErrs.setStatus("current")
_Sts1LIUExcessZeros_Type = Counter32
_Sts1LIUExcessZeros_Object = MibTableColumn
sts1LIUExcessZeros = _Sts1LIUExcessZeros_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 2, 1, 9),
    _Sts1LIUExcessZeros_Type()
)
sts1LIUExcessZeros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1LIUExcessZeros.setStatus("current")
_Sts1LIUCodingViolationErrs_Type = Counter32
_Sts1LIUCodingViolationErrs_Object = MibTableColumn
sts1LIUCodingViolationErrs = _Sts1LIUCodingViolationErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 2, 1, 10),
    _Sts1LIUCodingViolationErrs_Type()
)
sts1LIUCodingViolationErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1LIUCodingViolationErrs.setStatus("current")
_Sts1LIUPRBSErrs_Type = Counter32
_Sts1LIUPRBSErrs_Object = MibTableColumn
sts1LIUPRBSErrs = _Sts1LIUPRBSErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 2, 1, 11),
    _Sts1LIUPRBSErrs_Type()
)
sts1LIUPRBSErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1LIUPRBSErrs.setStatus("current")


class _Sts1LIUCmdStatus_Type(Integer32):
    """Custom type sts1LIUCmdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              14,
              101,
              114,
              200,
              202,
              203,
              205,
              206,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("clear-successful", 114),
          ("clearErrors", 14),
          ("err-field-cannot-be-set", 206),
          ("err-general-test-error", 200),
          ("err-invalid-bert-type", 203),
          ("err-invalid-loop-type", 202),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-snmp-parse-failed", 500),
          ("err-test-in-progress", 205),
          ("ready-for-command", 0),
          ("update", 1),
          ("update-successful", 101))
    )


_Sts1LIUCmdStatus_Type.__name__ = "Integer32"
_Sts1LIUCmdStatus_Object = MibTableColumn
sts1LIUCmdStatus = _Sts1LIUCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 2, 1, 12),
    _Sts1LIUCmdStatus_Type()
)
sts1LIUCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sts1LIUCmdStatus.setStatus("current")

# Managed Objects groups


# Notification objects

sts1MapperConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 0, 1)
)
sts1MapperConfigTrap.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-STS1-MIB", "sts1MapperAddr"),
        ("ERI-DNX-STS1-MIB", "sts1MaprCmdStatus"))
)
if mibBuilder.loadTexts:
    sts1MapperConfigTrap.setStatus(
        "current"
    )

sts1T1E1ConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 0, 2)
)
sts1T1E1ConfigTrap.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-STS1-MIB", "sts1T1E1CfgLinkAddr"),
        ("ERI-DNX-STS1-MIB", "sts1T1E1CfgCmdStatus"))
)
if mibBuilder.loadTexts:
    sts1T1E1ConfigTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ERI-DNX-STS1-MIB",
    **{"VtGroupType": VtGroupType,
       "dnxSTS1": dnxSTS1,
       "dnxSTS1Enterprise": dnxSTS1Enterprise,
       "sts1MapperConfigTrap": sts1MapperConfigTrap,
       "sts1T1E1ConfigTrap": sts1T1E1ConfigTrap,
       "sts1Config": sts1Config,
       "sts1MapperConfigTable": sts1MapperConfigTable,
       "sts1MapperConfigEntry": sts1MapperConfigEntry,
       "sts1MapperAddr": sts1MapperAddr,
       "sts1MapperResource": sts1MapperResource,
       "sts1VtGroup1": sts1VtGroup1,
       "sts1VtGroup2": sts1VtGroup2,
       "sts1VtGroup3": sts1VtGroup3,
       "sts1VtGroup4": sts1VtGroup4,
       "sts1VtGroup5": sts1VtGroup5,
       "sts1VtGroup6": sts1VtGroup6,
       "sts1VtGroup7": sts1VtGroup7,
       "sts1VtMapping": sts1VtMapping,
       "sts1Timing": sts1Timing,
       "sts1ShortCable": sts1ShortCable,
       "sts1MaprCmdStatus": sts1MaprCmdStatus,
       "sts1T1E1LinkConfigTable": sts1T1E1LinkConfigTable,
       "sts1T1E1LinkConfigEntry": sts1T1E1LinkConfigEntry,
       "sts1T1E1CfgLinkAddr": sts1T1E1CfgLinkAddr,
       "sts1T1E1CfgResource": sts1T1E1CfgResource,
       "sts1T1E1CfgLinkName": sts1T1E1CfgLinkName,
       "sts1T1E1Status": sts1T1E1Status,
       "sts1T1E1Clear": sts1T1E1Clear,
       "sts1T1E1Framing": sts1T1E1Framing,
       "sts1T1E1NetLoop": sts1T1E1NetLoop,
       "sts1T1E1YelAlrm": sts1T1E1YelAlrm,
       "sts1T1E1RecoverTime": sts1T1E1RecoverTime,
       "sts1T1E1EsfFormat": sts1T1E1EsfFormat,
       "sts1T1E1IdleCode": sts1T1E1IdleCode,
       "sts1T1E1CfgCmdStatus": sts1T1E1CfgCmdStatus,
       "sts1T1E1Gr303Facility": sts1T1E1Gr303Facility,
       "sts1Diag": sts1Diag,
       "sts1MapperStatusTable": sts1MapperStatusTable,
       "sts1MapperStatusEntry": sts1MapperStatusEntry,
       "sts1MapperStatusAddr": sts1MapperStatusAddr,
       "sts1MapperStatusResource": sts1MapperStatusResource,
       "sts1MapperStatusState": sts1MapperStatusState,
       "sts1MapperStatusLOSErrs": sts1MapperStatusLOSErrs,
       "sts1MapperStatusOOFErrs": sts1MapperStatusOOFErrs,
       "sts1MapperStatusLOFErrs": sts1MapperStatusLOFErrs,
       "sts1MapperStatusLOPtrErrs": sts1MapperStatusLOPtrErrs,
       "sts1MapperStatusAISErrs": sts1MapperStatusAISErrs,
       "sts1MapperStatusMultiFErrs": sts1MapperStatusMultiFErrs,
       "sts1MapperStatusRxTraceErrs": sts1MapperStatusRxTraceErrs,
       "sts1MapperStatusTotErrSecs": sts1MapperStatusTotErrSecs,
       "sts1MapperStatusCmdStatus": sts1MapperStatusCmdStatus,
       "sts1LIUTable": sts1LIUTable,
       "sts1LIUEntry": sts1LIUEntry,
       "sts1LIUAddr": sts1LIUAddr,
       "sts1LIUResource": sts1LIUResource,
       "sts1LIUBertState": sts1LIUBertState,
       "sts1LIUBertErrSecs": sts1LIUBertErrSecs,
       "sts1LIUBertDuration": sts1LIUBertDuration,
       "sts1LIULoopType": sts1LIULoopType,
       "sts1LIUDigitalErrs": sts1LIUDigitalErrs,
       "sts1LIUAnalogErrs": sts1LIUAnalogErrs,
       "sts1LIUExcessZeros": sts1LIUExcessZeros,
       "sts1LIUCodingViolationErrs": sts1LIUCodingViolationErrs,
       "sts1LIUPRBSErrs": sts1LIUPRBSErrs,
       "sts1LIUCmdStatus": sts1LIUCmdStatus,
       "eriDNXSts1MIB": eriDNXSts1MIB}
)
