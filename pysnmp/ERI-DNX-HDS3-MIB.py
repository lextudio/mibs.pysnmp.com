# SNMP MIB module (ERI-DNX-HDS3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ERI-DNX-HDS3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:24 2024
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
 OneByteField,
 PortStatus,
 devices,
 trapSequence) = mibBuilder.importSymbols(
    "ERI-DNX-SMC-MIB",
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

eriDNXHybridDS3MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 644, 3, 5)
)
eriDNXHybridDS3MIB.setRevisions(
        ("2003-01-27 00:00",
         "2002-04-08 00:00",
         "2002-03-14 00:00",
         "2002-01-04 00:00",
         "2001-10-10 00:00",
         "2001-04-03 00:00",
         "2001-03-01 00:00",
         "2000-09-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DS2GroupType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ds1", 1),
          ("e1", 0))
    )



# MIB Managed Objects in the order of their OIDs

_DnxHDS3_ObjectIdentity = ObjectIdentity
dnxHDS3 = _DnxHDS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2)
)
_DnxHDS3Enterprise_ObjectIdentity = ObjectIdentity
dnxHDS3Enterprise = _DnxHDS3Enterprise_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 0)
)
if mibBuilder.loadTexts:
    dnxHDS3Enterprise.setStatus("current")
_Hds3Config_ObjectIdentity = ObjectIdentity
hds3Config = _Hds3Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1)
)
_Hds3PortConfigTable_Object = MibTable
hds3PortConfigTable = _Hds3PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hds3PortConfigTable.setStatus("current")
_Hds3PortConfigEntry_Object = MibTableRow
hds3PortConfigEntry = _Hds3PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 1, 1)
)
hds3PortConfigEntry.setIndexNames(
    (0, "ERI-DNX-HDS3-MIB", "hds3PortCfgAddr"),
)
if mibBuilder.loadTexts:
    hds3PortConfigEntry.setStatus("current")
_Hds3PortCfgAddr_Type = LinkPortAddress
_Hds3PortCfgAddr_Object = MibTableColumn
hds3PortCfgAddr = _Hds3PortCfgAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 1, 1, 1),
    _Hds3PortCfgAddr_Type()
)
hds3PortCfgAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3PortCfgAddr.setStatus("current")
_Hds3PortCfgResource_Type = Integer32
_Hds3PortCfgResource_Object = MibTableColumn
hds3PortCfgResource = _Hds3PortCfgResource_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 1, 1, 2),
    _Hds3PortCfgResource_Type()
)
hds3PortCfgResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3PortCfgResource.setStatus("current")


class _Hds3PortCfgName_Type(DisplayString):
    """Custom type hds3PortCfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Hds3PortCfgName_Type.__name__ = "DisplayString"
_Hds3PortCfgName_Object = MibTableColumn
hds3PortCfgName = _Hds3PortCfgName_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 1, 1, 3),
    _Hds3PortCfgName_Type()
)
hds3PortCfgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3PortCfgName.setStatus("current")


class _Hds3FacilityId_Type(DisplayString):
    """Custom type hds3FacilityId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 37),
    )


_Hds3FacilityId_Type.__name__ = "DisplayString"
_Hds3FacilityId_Object = MibTableColumn
hds3FacilityId = _Hds3FacilityId_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 1, 1, 4),
    _Hds3FacilityId_Type()
)
hds3FacilityId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3FacilityId.setStatus("obsolete")


class _Hds3EquipmentId_Type(DisplayString):
    """Custom type hds3EquipmentId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_Hds3EquipmentId_Type.__name__ = "DisplayString"
_Hds3EquipmentId_Object = MibTableColumn
hds3EquipmentId = _Hds3EquipmentId_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 1, 1, 5),
    _Hds3EquipmentId_Type()
)
hds3EquipmentId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3EquipmentId.setStatus("obsolete")


class _Hds3Location_Type(DisplayString):
    """Custom type hds3Location based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Hds3Location_Type.__name__ = "DisplayString"
_Hds3Location_Object = MibTableColumn
hds3Location = _Hds3Location_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 1, 1, 6),
    _Hds3Location_Type()
)
hds3Location.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3Location.setStatus("obsolete")


class _Hds3FrameId_Type(DisplayString):
    """Custom type hds3FrameId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_Hds3FrameId_Type.__name__ = "DisplayString"
_Hds3FrameId_Object = MibTableColumn
hds3FrameId = _Hds3FrameId_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 1, 1, 7),
    _Hds3FrameId_Type()
)
hds3FrameId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3FrameId.setStatus("obsolete")


class _Hds3UnitName_Type(DisplayString):
    """Custom type hds3UnitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_Hds3UnitName_Type.__name__ = "DisplayString"
_Hds3UnitName_Object = MibTableColumn
hds3UnitName = _Hds3UnitName_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 1, 1, 8),
    _Hds3UnitName_Type()
)
hds3UnitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3UnitName.setStatus("obsolete")


class _Hds3PortNumber_Type(DisplayString):
    """Custom type hds3PortNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 37),
    )


_Hds3PortNumber_Type.__name__ = "DisplayString"
_Hds3PortNumber_Object = MibTableColumn
hds3PortNumber = _Hds3PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 1, 1, 9),
    _Hds3PortNumber_Type()
)
hds3PortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3PortNumber.setStatus("obsolete")


class _Hds3Generator_Type(DisplayString):
    """Custom type hds3Generator based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 37),
    )


_Hds3Generator_Type.__name__ = "DisplayString"
_Hds3Generator_Object = MibTableColumn
hds3Generator = _Hds3Generator_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 1, 1, 10),
    _Hds3Generator_Type()
)
hds3Generator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3Generator.setStatus("obsolete")


class _Hds3M13OpMode_Type(Integer32):
    """Custom type hds3M13OpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bellcoreM13", 0),
          ("c-bitParity", 1))
    )


_Hds3M13OpMode_Type.__name__ = "Integer32"
_Hds3M13OpMode_Object = MibTableColumn
hds3M13OpMode = _Hds3M13OpMode_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 1, 1, 11),
    _Hds3M13OpMode_Type()
)
hds3M13OpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3M13OpMode.setStatus("current")
_Hds3RcvLoopTiming_Type = FunctionSwitch
_Hds3RcvLoopTiming_Object = MibTableColumn
hds3RcvLoopTiming = _Hds3RcvLoopTiming_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 1, 1, 12),
    _Hds3RcvLoopTiming_Type()
)
hds3RcvLoopTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3RcvLoopTiming.setStatus("current")
_Hds3ShortCable_Type = DecisionType
_Hds3ShortCable_Object = MibTableColumn
hds3ShortCable = _Hds3ShortCable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 1, 1, 13),
    _Hds3ShortCable_Type()
)
hds3ShortCable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3ShortCable.setStatus("current")


class _Hds3M13RemLoop_Type(Integer32):
    """Custom type hds3M13RemLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("first-cbit-inverted", 2),
          ("second-cbit-inverted", 1),
          ("third-cbit-inverted", 0))
    )


_Hds3M13RemLoop_Type.__name__ = "Integer32"
_Hds3M13RemLoop_Object = MibTableColumn
hds3M13RemLoop = _Hds3M13RemLoop_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 1, 1, 14),
    _Hds3M13RemLoop_Type()
)
hds3M13RemLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3M13RemLoop.setStatus("current")
_Hds3FEACLoopbackReq_Type = FunctionSwitch
_Hds3FEACLoopbackReq_Object = MibTableColumn
hds3FEACLoopbackReq = _Hds3FEACLoopbackReq_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 1, 1, 15),
    _Hds3FEACLoopbackReq_Type()
)
hds3FEACLoopbackReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3FEACLoopbackReq.setStatus("current")


class _Hds3XmtAISLocalLoop_Type(Integer32):
    """Custom type hds3XmtAISLocalLoop based on Integer32"""
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
        *(("framed-1010-cbitZero", 1),
          ("framed-allones-cbitZero", 2),
          ("none", 0),
          ("unframed-allones", 3))
    )


_Hds3XmtAISLocalLoop_Type.__name__ = "Integer32"
_Hds3XmtAISLocalLoop_Object = MibTableColumn
hds3XmtAISLocalLoop = _Hds3XmtAISLocalLoop_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 1, 1, 16),
    _Hds3XmtAISLocalLoop_Type()
)
hds3XmtAISLocalLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3XmtAISLocalLoop.setStatus("current")


class _Hds3RcvAIS_Type(Integer32):
    """Custom type hds3RcvAIS based on Integer32"""
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
        *(("cbitZero-noPayloadBits", 2),
          ("framed1010-cbitZero", 3),
          ("framed1010-noOverheadBits", 1),
          ("framed1111-noOverheadBits", 4),
          ("unframed-allones", 5))
    )


_Hds3RcvAIS_Type.__name__ = "Integer32"
_Hds3RcvAIS_Object = MibTableColumn
hds3RcvAIS = _Hds3RcvAIS_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 1, 1, 17),
    _Hds3RcvAIS_Type()
)
hds3RcvAIS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3RcvAIS.setStatus("current")


class _Hds3XmtAIS_Type(Integer32):
    """Custom type hds3XmtAIS based on Integer32"""
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
        *(("framed-1010-cbitZero", 1),
          ("framed-allones-cbitZero", 2),
          ("none", 0),
          ("unframed-allones", 3))
    )


_Hds3XmtAIS_Type.__name__ = "Integer32"
_Hds3XmtAIS_Object = MibTableColumn
hds3XmtAIS = _Hds3XmtAIS_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 1, 1, 18),
    _Hds3XmtAIS_Type()
)
hds3XmtAIS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3XmtAIS.setStatus("current")
_Hds3DS2Group1_Type = DS2GroupType
_Hds3DS2Group1_Object = MibTableColumn
hds3DS2Group1 = _Hds3DS2Group1_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 1, 1, 19),
    _Hds3DS2Group1_Type()
)
hds3DS2Group1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3DS2Group1.setStatus("current")
_Hds3DS2Group2_Type = DS2GroupType
_Hds3DS2Group2_Object = MibTableColumn
hds3DS2Group2 = _Hds3DS2Group2_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 1, 1, 20),
    _Hds3DS2Group2_Type()
)
hds3DS2Group2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3DS2Group2.setStatus("current")
_Hds3DS2Group3_Type = DS2GroupType
_Hds3DS2Group3_Object = MibTableColumn
hds3DS2Group3 = _Hds3DS2Group3_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 1, 1, 21),
    _Hds3DS2Group3_Type()
)
hds3DS2Group3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3DS2Group3.setStatus("current")
_Hds3DS2Group4_Type = DS2GroupType
_Hds3DS2Group4_Object = MibTableColumn
hds3DS2Group4 = _Hds3DS2Group4_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 1, 1, 22),
    _Hds3DS2Group4_Type()
)
hds3DS2Group4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3DS2Group4.setStatus("current")
_Hds3DS2Group5_Type = DS2GroupType
_Hds3DS2Group5_Object = MibTableColumn
hds3DS2Group5 = _Hds3DS2Group5_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 1, 1, 23),
    _Hds3DS2Group5_Type()
)
hds3DS2Group5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3DS2Group5.setStatus("current")
_Hds3DS2Group6_Type = DS2GroupType
_Hds3DS2Group6_Object = MibTableColumn
hds3DS2Group6 = _Hds3DS2Group6_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 1, 1, 24),
    _Hds3DS2Group6_Type()
)
hds3DS2Group6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3DS2Group6.setStatus("current")
_Hds3DS2Group7_Type = DS2GroupType
_Hds3DS2Group7_Object = MibTableColumn
hds3DS2Group7 = _Hds3DS2Group7_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 1, 1, 25),
    _Hds3DS2Group7_Type()
)
hds3DS2Group7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3DS2Group7.setStatus("current")
_Hds3CmdStatus_Type = LinkCmdStatus
_Hds3CmdStatus_Object = MibTableColumn
hds3CmdStatus = _Hds3CmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 1, 1, 26),
    _Hds3CmdStatus_Type()
)
hds3CmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3CmdStatus.setStatus("current")
_Hds3T1E1LinkConfigTable_Object = MibTable
hds3T1E1LinkConfigTable = _Hds3T1E1LinkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hds3T1E1LinkConfigTable.setStatus("current")
_Hds3T1E1LinkConfigEntry_Object = MibTableRow
hds3T1E1LinkConfigEntry = _Hds3T1E1LinkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 2, 1)
)
hds3T1E1LinkConfigEntry.setIndexNames(
    (0, "ERI-DNX-HDS3-MIB", "hds3T1E1CfgLinkAddr"),
)
if mibBuilder.loadTexts:
    hds3T1E1LinkConfigEntry.setStatus("current")
_Hds3T1E1CfgLinkAddr_Type = LinkPortAddress
_Hds3T1E1CfgLinkAddr_Object = MibTableColumn
hds3T1E1CfgLinkAddr = _Hds3T1E1CfgLinkAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 2, 1, 1),
    _Hds3T1E1CfgLinkAddr_Type()
)
hds3T1E1CfgLinkAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3T1E1CfgLinkAddr.setStatus("current")
_Hds3T1E1CfgResource_Type = Integer32
_Hds3T1E1CfgResource_Object = MibTableColumn
hds3T1E1CfgResource = _Hds3T1E1CfgResource_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 2, 1, 2),
    _Hds3T1E1CfgResource_Type()
)
hds3T1E1CfgResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3T1E1CfgResource.setStatus("current")


class _Hds3T1E1CfgLinkName_Type(DisplayString):
    """Custom type hds3T1E1CfgLinkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Hds3T1E1CfgLinkName_Type.__name__ = "DisplayString"
_Hds3T1E1CfgLinkName_Object = MibTableColumn
hds3T1E1CfgLinkName = _Hds3T1E1CfgLinkName_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 2, 1, 3),
    _Hds3T1E1CfgLinkName_Type()
)
hds3T1E1CfgLinkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3T1E1CfgLinkName.setStatus("current")
_Hds3T1E1Status_Type = PortStatus
_Hds3T1E1Status_Object = MibTableColumn
hds3T1E1Status = _Hds3T1E1Status_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 2, 1, 4),
    _Hds3T1E1Status_Type()
)
hds3T1E1Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3T1E1Status.setStatus("current")


class _Hds3T1E1Clear_Type(Integer32):
    """Custom type hds3T1E1Clear based on Integer32"""
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


_Hds3T1E1Clear_Type.__name__ = "Integer32"
_Hds3T1E1Clear_Object = MibTableColumn
hds3T1E1Clear = _Hds3T1E1Clear_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 2, 1, 5),
    _Hds3T1E1Clear_Type()
)
hds3T1E1Clear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3T1E1Clear.setStatus("current")


class _Hds3T1E1Framing_Type(Integer32):
    """Custom type hds3T1E1Framing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("e1", 0),
          ("e1Cas", 2),
          ("e1CasCrc", 3),
          ("e1Crc", 1),
          ("e1Unframed", 4),
          ("t1D4", 6),
          ("t1Esf", 5),
          ("t1Unframed", 7))
    )


_Hds3T1E1Framing_Type.__name__ = "Integer32"
_Hds3T1E1Framing_Object = MibTableColumn
hds3T1E1Framing = _Hds3T1E1Framing_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 2, 1, 6),
    _Hds3T1E1Framing_Type()
)
hds3T1E1Framing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3T1E1Framing.setStatus("current")
_Hds3T1E1NetLoop_Type = FunctionSwitch
_Hds3T1E1NetLoop_Object = MibTableColumn
hds3T1E1NetLoop = _Hds3T1E1NetLoop_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 2, 1, 7),
    _Hds3T1E1NetLoop_Type()
)
hds3T1E1NetLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3T1E1NetLoop.setStatus("current")
_Hds3T1E1YelAlrm_Type = DecisionType
_Hds3T1E1YelAlrm_Object = MibTableColumn
hds3T1E1YelAlrm = _Hds3T1E1YelAlrm_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 2, 1, 8),
    _Hds3T1E1YelAlrm_Type()
)
hds3T1E1YelAlrm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3T1E1YelAlrm.setStatus("current")


class _Hds3T1E1RecoverTime_Type(Integer32):
    """Custom type hds3T1E1RecoverTime based on Integer32"""
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


_Hds3T1E1RecoverTime_Type.__name__ = "Integer32"
_Hds3T1E1RecoverTime_Object = MibTableColumn
hds3T1E1RecoverTime = _Hds3T1E1RecoverTime_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 2, 1, 9),
    _Hds3T1E1RecoverTime_Type()
)
hds3T1E1RecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3T1E1RecoverTime.setStatus("current")


class _Hds3T1E1EsfFormat_Type(Integer32):
    """Custom type hds3T1E1EsfFormat based on Integer32"""
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


_Hds3T1E1EsfFormat_Type.__name__ = "Integer32"
_Hds3T1E1EsfFormat_Object = MibTableColumn
hds3T1E1EsfFormat = _Hds3T1E1EsfFormat_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 2, 1, 10),
    _Hds3T1E1EsfFormat_Type()
)
hds3T1E1EsfFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3T1E1EsfFormat.setStatus("current")


class _Hds3T1E1IdleCode_Type(Integer32):
    """Custom type hds3T1E1IdleCode based on Integer32"""
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


_Hds3T1E1IdleCode_Type.__name__ = "Integer32"
_Hds3T1E1IdleCode_Object = MibTableColumn
hds3T1E1IdleCode = _Hds3T1E1IdleCode_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 2, 1, 11),
    _Hds3T1E1IdleCode_Type()
)
hds3T1E1IdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3T1E1IdleCode.setStatus("current")
_Hds3T1E1CfgCmdStatus_Type = LinkCmdStatus
_Hds3T1E1CfgCmdStatus_Object = MibTableColumn
hds3T1E1CfgCmdStatus = _Hds3T1E1CfgCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 2, 1, 12),
    _Hds3T1E1CfgCmdStatus_Type()
)
hds3T1E1CfgCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3T1E1CfgCmdStatus.setStatus("current")
_Hds3T1E1Gr303Facility_Type = DecisionType
_Hds3T1E1Gr303Facility_Object = MibTableColumn
hds3T1E1Gr303Facility = _Hds3T1E1Gr303Facility_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 2, 1, 13),
    _Hds3T1E1Gr303Facility_Type()
)
hds3T1E1Gr303Facility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3T1E1Gr303Facility.setStatus("obsolete")
_Hds3T1E1NationalBits_Type = OneByteField
_Hds3T1E1NationalBits_Object = MibTableColumn
hds3T1E1NationalBits = _Hds3T1E1NationalBits_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 2, 1, 14),
    _Hds3T1E1NationalBits_Type()
)
hds3T1E1NationalBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3T1E1NationalBits.setStatus("current")
_Hds3T1E1InterNational_Type = OneByteField
_Hds3T1E1InterNational_Object = MibTableColumn
hds3T1E1InterNational = _Hds3T1E1InterNational_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 1, 2, 1, 15),
    _Hds3T1E1InterNational_Type()
)
hds3T1E1InterNational.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3T1E1InterNational.setStatus("current")
_Hds3Diag_ObjectIdentity = ObjectIdentity
hds3Diag = _Hds3Diag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2)
)
_Hds3FramerStatusTable_Object = MibTable
hds3FramerStatusTable = _Hds3FramerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hds3FramerStatusTable.setStatus("current")
_Hds3FramerStatusEntry_Object = MibTableRow
hds3FramerStatusEntry = _Hds3FramerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 1, 1)
)
hds3FramerStatusEntry.setIndexNames(
    (0, "ERI-DNX-HDS3-MIB", "hds3FramerStatusAddr"),
)
if mibBuilder.loadTexts:
    hds3FramerStatusEntry.setStatus("current")
_Hds3FramerStatusAddr_Type = LinkPortAddress
_Hds3FramerStatusAddr_Object = MibTableColumn
hds3FramerStatusAddr = _Hds3FramerStatusAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 1, 1, 1),
    _Hds3FramerStatusAddr_Type()
)
hds3FramerStatusAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3FramerStatusAddr.setStatus("current")
_Hds3FramerStatusResource_Type = Integer32
_Hds3FramerStatusResource_Object = MibTableColumn
hds3FramerStatusResource = _Hds3FramerStatusResource_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 1, 1, 2),
    _Hds3FramerStatusResource_Type()
)
hds3FramerStatusResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3FramerStatusResource.setStatus("current")


class _Hds3FramerStatusState_Type(Integer32):
    """Custom type hds3FramerStatusState based on Integer32"""
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


_Hds3FramerStatusState_Type.__name__ = "Integer32"
_Hds3FramerStatusState_Object = MibTableColumn
hds3FramerStatusState = _Hds3FramerStatusState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 1, 1, 3),
    _Hds3FramerStatusState_Type()
)
hds3FramerStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3FramerStatusState.setStatus("current")
_Hds3FramerStatusRedAlrmErrSecs_Type = Counter32
_Hds3FramerStatusRedAlrmErrSecs_Object = MibTableColumn
hds3FramerStatusRedAlrmErrSecs = _Hds3FramerStatusRedAlrmErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 1, 1, 4),
    _Hds3FramerStatusRedAlrmErrSecs_Type()
)
hds3FramerStatusRedAlrmErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3FramerStatusRedAlrmErrSecs.setStatus("current")
_Hds3FramerStatusLOSErrSecs_Type = Counter32
_Hds3FramerStatusLOSErrSecs_Object = MibTableColumn
hds3FramerStatusLOSErrSecs = _Hds3FramerStatusLOSErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 1, 1, 5),
    _Hds3FramerStatusLOSErrSecs_Type()
)
hds3FramerStatusLOSErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3FramerStatusLOSErrSecs.setStatus("current")
_Hds3FramerStatusOOFErrSecs_Type = Counter32
_Hds3FramerStatusOOFErrSecs_Object = MibTableColumn
hds3FramerStatusOOFErrSecs = _Hds3FramerStatusOOFErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 1, 1, 6),
    _Hds3FramerStatusOOFErrSecs_Type()
)
hds3FramerStatusOOFErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3FramerStatusOOFErrSecs.setStatus("current")
_Hds3FramerStatusAISErrSecs_Type = Counter32
_Hds3FramerStatusAISErrSecs_Object = MibTableColumn
hds3FramerStatusAISErrSecs = _Hds3FramerStatusAISErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 1, 1, 7),
    _Hds3FramerStatusAISErrSecs_Type()
)
hds3FramerStatusAISErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3FramerStatusAISErrSecs.setStatus("current")
_Hds3FramerStatusRcvIdleErrSecs_Type = Counter32
_Hds3FramerStatusRcvIdleErrSecs_Object = MibTableColumn
hds3FramerStatusRcvIdleErrSecs = _Hds3FramerStatusRcvIdleErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 1, 1, 8),
    _Hds3FramerStatusRcvIdleErrSecs_Type()
)
hds3FramerStatusRcvIdleErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3FramerStatusRcvIdleErrSecs.setStatus("current")
_Hds3FramerStatusFarEndRcvErrSecs_Type = Counter32
_Hds3FramerStatusFarEndRcvErrSecs_Object = MibTableColumn
hds3FramerStatusFarEndRcvErrSecs = _Hds3FramerStatusFarEndRcvErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 1, 1, 9),
    _Hds3FramerStatusFarEndRcvErrSecs_Type()
)
hds3FramerStatusFarEndRcvErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3FramerStatusFarEndRcvErrSecs.setStatus("current")
_Hds3FramerStatusCFAErrSecs_Type = Counter32
_Hds3FramerStatusCFAErrSecs_Object = MibTableColumn
hds3FramerStatusCFAErrSecs = _Hds3FramerStatusCFAErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 1, 1, 10),
    _Hds3FramerStatusCFAErrSecs_Type()
)
hds3FramerStatusCFAErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3FramerStatusCFAErrSecs.setStatus("current")
_Hds3FramerStatusTotErrSecs_Type = Counter32
_Hds3FramerStatusTotErrSecs_Object = MibTableColumn
hds3FramerStatusTotErrSecs = _Hds3FramerStatusTotErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 1, 1, 11),
    _Hds3FramerStatusTotErrSecs_Type()
)
hds3FramerStatusTotErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3FramerStatusTotErrSecs.setStatus("current")
_Hds3FramerStatusPbitParityErrs_Type = Counter32
_Hds3FramerStatusPbitParityErrs_Object = MibTableColumn
hds3FramerStatusPbitParityErrs = _Hds3FramerStatusPbitParityErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 1, 1, 12),
    _Hds3FramerStatusPbitParityErrs_Type()
)
hds3FramerStatusPbitParityErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3FramerStatusPbitParityErrs.setStatus("current")
_Hds3FramerStatusCbitParityErrs_Type = Counter32
_Hds3FramerStatusCbitParityErrs_Object = MibTableColumn
hds3FramerStatusCbitParityErrs = _Hds3FramerStatusCbitParityErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 1, 1, 13),
    _Hds3FramerStatusCbitParityErrs_Type()
)
hds3FramerStatusCbitParityErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3FramerStatusCbitParityErrs.setStatus("current")
_Hds3FramerStatusFebeErrs_Type = Counter32
_Hds3FramerStatusFebeErrs_Object = MibTableColumn
hds3FramerStatusFebeErrs = _Hds3FramerStatusFebeErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 1, 1, 14),
    _Hds3FramerStatusFebeErrs_Type()
)
hds3FramerStatusFebeErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3FramerStatusFebeErrs.setStatus("current")
_Hds3FramerStatusLCVErrs_Type = Counter32
_Hds3FramerStatusLCVErrs_Object = MibTableColumn
hds3FramerStatusLCVErrs = _Hds3FramerStatusLCVErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 1, 1, 15),
    _Hds3FramerStatusLCVErrs_Type()
)
hds3FramerStatusLCVErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3FramerStatusLCVErrs.setStatus("current")
_Hds3FramerStatusFramingErrs_Type = Counter32
_Hds3FramerStatusFramingErrs_Object = MibTableColumn
hds3FramerStatusFramingErrs = _Hds3FramerStatusFramingErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 1, 1, 16),
    _Hds3FramerStatusFramingErrs_Type()
)
hds3FramerStatusFramingErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3FramerStatusFramingErrs.setStatus("current")
_Hds3FramerStatusExcessZeroErrs_Type = Counter32
_Hds3FramerStatusExcessZeroErrs_Object = MibTableColumn
hds3FramerStatusExcessZeroErrs = _Hds3FramerStatusExcessZeroErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 1, 1, 17),
    _Hds3FramerStatusExcessZeroErrs_Type()
)
hds3FramerStatusExcessZeroErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3FramerStatusExcessZeroErrs.setStatus("current")


class _Hds3FramerStatusInsErrMode_Type(Integer32):
    """Custom type hds3FramerStatusInsErrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              8)
        )
    )
    namedValues = NamedValues(
        *(("allErrors", 8),
          ("c-bit-parity", 3),
          ("febe", 1),
          ("frame-alignment", 5),
          ("multiframe-align", 4),
          ("p-bit-parity", 2))
    )


_Hds3FramerStatusInsErrMode_Type.__name__ = "Integer32"
_Hds3FramerStatusInsErrMode_Object = MibTableColumn
hds3FramerStatusInsErrMode = _Hds3FramerStatusInsErrMode_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 1, 1, 18),
    _Hds3FramerStatusInsErrMode_Type()
)
hds3FramerStatusInsErrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3FramerStatusInsErrMode.setStatus("current")


class _Hds3FramerStatusCmdStatus_Type(Integer32):
    """Custom type hds3FramerStatusCmdStatus based on Integer32"""
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
          ("err-invalid-command", 208),
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


_Hds3FramerStatusCmdStatus_Type.__name__ = "Integer32"
_Hds3FramerStatusCmdStatus_Object = MibTableColumn
hds3FramerStatusCmdStatus = _Hds3FramerStatusCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 1, 1, 19),
    _Hds3FramerStatusCmdStatus_Type()
)
hds3FramerStatusCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3FramerStatusCmdStatus.setStatus("current")
_Hds3LIUTable_Object = MibTable
hds3LIUTable = _Hds3LIUTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hds3LIUTable.setStatus("current")
_Hds3LIUEntry_Object = MibTableRow
hds3LIUEntry = _Hds3LIUEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 2, 1)
)
hds3LIUEntry.setIndexNames(
    (0, "ERI-DNX-HDS3-MIB", "hds3LIUAddr"),
)
if mibBuilder.loadTexts:
    hds3LIUEntry.setStatus("current")
_Hds3LIUAddr_Type = LinkPortAddress
_Hds3LIUAddr_Object = MibTableColumn
hds3LIUAddr = _Hds3LIUAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 2, 1, 1),
    _Hds3LIUAddr_Type()
)
hds3LIUAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3LIUAddr.setStatus("current")
_Hds3LIUResource_Type = Integer32
_Hds3LIUResource_Object = MibTableColumn
hds3LIUResource = _Hds3LIUResource_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 2, 1, 2),
    _Hds3LIUResource_Type()
)
hds3LIUResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3LIUResource.setStatus("current")


class _Hds3LIUBertState_Type(Integer32):
    """Custom type hds3LIUBertState based on Integer32"""
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


_Hds3LIUBertState_Type.__name__ = "Integer32"
_Hds3LIUBertState_Object = MibTableColumn
hds3LIUBertState = _Hds3LIUBertState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 2, 1, 3),
    _Hds3LIUBertState_Type()
)
hds3LIUBertState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3LIUBertState.setStatus("current")
_Hds3LIUBertErrSecs_Type = Counter32
_Hds3LIUBertErrSecs_Object = MibTableColumn
hds3LIUBertErrSecs = _Hds3LIUBertErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 2, 1, 4),
    _Hds3LIUBertErrSecs_Type()
)
hds3LIUBertErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3LIUBertErrSecs.setStatus("current")
_Hds3LIUBertDuration_Type = Counter32
_Hds3LIUBertDuration_Object = MibTableColumn
hds3LIUBertDuration = _Hds3LIUBertDuration_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 2, 1, 5),
    _Hds3LIUBertDuration_Type()
)
hds3LIUBertDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3LIUBertDuration.setStatus("current")


class _Hds3LIULoopType_Type(Integer32):
    """Custom type hds3LIULoopType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              36,
              39)
        )
    )
    namedValues = NamedValues(
        *(("ds3-line", 36),
          ("ds3-local", 1),
          ("liu", 39),
          ("off", 0))
    )


_Hds3LIULoopType_Type.__name__ = "Integer32"
_Hds3LIULoopType_Object = MibTableColumn
hds3LIULoopType = _Hds3LIULoopType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 2, 1, 6),
    _Hds3LIULoopType_Type()
)
hds3LIULoopType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3LIULoopType.setStatus("current")
_Hds3LIUDigitalErrs_Type = Counter32
_Hds3LIUDigitalErrs_Object = MibTableColumn
hds3LIUDigitalErrs = _Hds3LIUDigitalErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 2, 1, 7),
    _Hds3LIUDigitalErrs_Type()
)
hds3LIUDigitalErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3LIUDigitalErrs.setStatus("current")
_Hds3LIUAnalogErrs_Type = Counter32
_Hds3LIUAnalogErrs_Object = MibTableColumn
hds3LIUAnalogErrs = _Hds3LIUAnalogErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 2, 1, 8),
    _Hds3LIUAnalogErrs_Type()
)
hds3LIUAnalogErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3LIUAnalogErrs.setStatus("current")
_Hds3LIUExcessZeroErrs_Type = Counter32
_Hds3LIUExcessZeroErrs_Object = MibTableColumn
hds3LIUExcessZeroErrs = _Hds3LIUExcessZeroErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 2, 1, 9),
    _Hds3LIUExcessZeroErrs_Type()
)
hds3LIUExcessZeroErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3LIUExcessZeroErrs.setStatus("current")
_Hds3LIUCodingViolationErrs_Type = Counter32
_Hds3LIUCodingViolationErrs_Object = MibTableColumn
hds3LIUCodingViolationErrs = _Hds3LIUCodingViolationErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 2, 1, 10),
    _Hds3LIUCodingViolationErrs_Type()
)
hds3LIUCodingViolationErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3LIUCodingViolationErrs.setStatus("current")
_Hds3LIUPRBSCheckErrs_Type = Counter32
_Hds3LIUPRBSCheckErrs_Object = MibTableColumn
hds3LIUPRBSCheckErrs = _Hds3LIUPRBSCheckErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 2, 1, 11),
    _Hds3LIUPRBSCheckErrs_Type()
)
hds3LIUPRBSCheckErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hds3LIUPRBSCheckErrs.setStatus("current")


class _Hds3LIUCmdStatus_Type(Integer32):
    """Custom type hds3LIUCmdStatus based on Integer32"""
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
          ("err-general-liu-error", 200),
          ("err-invalid-bert-type", 203),
          ("err-invalid-command", 208),
          ("err-invalid-loop-type", 202),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-snmp-parse-failed", 500),
          ("err-test-in-progress", 205),
          ("ready-for-command", 0),
          ("update", 1),
          ("update-successful", 101))
    )


_Hds3LIUCmdStatus_Type.__name__ = "Integer32"
_Hds3LIUCmdStatus_Object = MibTableColumn
hds3LIUCmdStatus = _Hds3LIUCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 2, 2, 1, 12),
    _Hds3LIUCmdStatus_Type()
)
hds3LIUCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hds3LIUCmdStatus.setStatus("current")

# Managed Objects groups


# Notification objects

hds3PortConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 0, 1)
)
hds3PortConfigTrap.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-HDS3-MIB", "hds3PortCfgAddr"),
        ("ERI-DNX-HDS3-MIB", "hds3CmdStatus"))
)
if mibBuilder.loadTexts:
    hds3PortConfigTrap.setStatus(
        "current"
    )

hds3T1E1ConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 2, 0, 2)
)
hds3T1E1ConfigTrap.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-HDS3-MIB", "hds3T1E1CfgLinkAddr"),
        ("ERI-DNX-HDS3-MIB", "hds3T1E1CfgCmdStatus"))
)
if mibBuilder.loadTexts:
    hds3T1E1ConfigTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ERI-DNX-HDS3-MIB",
    **{"DS2GroupType": DS2GroupType,
       "dnxHDS3": dnxHDS3,
       "dnxHDS3Enterprise": dnxHDS3Enterprise,
       "hds3PortConfigTrap": hds3PortConfigTrap,
       "hds3T1E1ConfigTrap": hds3T1E1ConfigTrap,
       "hds3Config": hds3Config,
       "hds3PortConfigTable": hds3PortConfigTable,
       "hds3PortConfigEntry": hds3PortConfigEntry,
       "hds3PortCfgAddr": hds3PortCfgAddr,
       "hds3PortCfgResource": hds3PortCfgResource,
       "hds3PortCfgName": hds3PortCfgName,
       "hds3FacilityId": hds3FacilityId,
       "hds3EquipmentId": hds3EquipmentId,
       "hds3Location": hds3Location,
       "hds3FrameId": hds3FrameId,
       "hds3UnitName": hds3UnitName,
       "hds3PortNumber": hds3PortNumber,
       "hds3Generator": hds3Generator,
       "hds3M13OpMode": hds3M13OpMode,
       "hds3RcvLoopTiming": hds3RcvLoopTiming,
       "hds3ShortCable": hds3ShortCable,
       "hds3M13RemLoop": hds3M13RemLoop,
       "hds3FEACLoopbackReq": hds3FEACLoopbackReq,
       "hds3XmtAISLocalLoop": hds3XmtAISLocalLoop,
       "hds3RcvAIS": hds3RcvAIS,
       "hds3XmtAIS": hds3XmtAIS,
       "hds3DS2Group1": hds3DS2Group1,
       "hds3DS2Group2": hds3DS2Group2,
       "hds3DS2Group3": hds3DS2Group3,
       "hds3DS2Group4": hds3DS2Group4,
       "hds3DS2Group5": hds3DS2Group5,
       "hds3DS2Group6": hds3DS2Group6,
       "hds3DS2Group7": hds3DS2Group7,
       "hds3CmdStatus": hds3CmdStatus,
       "hds3T1E1LinkConfigTable": hds3T1E1LinkConfigTable,
       "hds3T1E1LinkConfigEntry": hds3T1E1LinkConfigEntry,
       "hds3T1E1CfgLinkAddr": hds3T1E1CfgLinkAddr,
       "hds3T1E1CfgResource": hds3T1E1CfgResource,
       "hds3T1E1CfgLinkName": hds3T1E1CfgLinkName,
       "hds3T1E1Status": hds3T1E1Status,
       "hds3T1E1Clear": hds3T1E1Clear,
       "hds3T1E1Framing": hds3T1E1Framing,
       "hds3T1E1NetLoop": hds3T1E1NetLoop,
       "hds3T1E1YelAlrm": hds3T1E1YelAlrm,
       "hds3T1E1RecoverTime": hds3T1E1RecoverTime,
       "hds3T1E1EsfFormat": hds3T1E1EsfFormat,
       "hds3T1E1IdleCode": hds3T1E1IdleCode,
       "hds3T1E1CfgCmdStatus": hds3T1E1CfgCmdStatus,
       "hds3T1E1Gr303Facility": hds3T1E1Gr303Facility,
       "hds3T1E1NationalBits": hds3T1E1NationalBits,
       "hds3T1E1InterNational": hds3T1E1InterNational,
       "hds3Diag": hds3Diag,
       "hds3FramerStatusTable": hds3FramerStatusTable,
       "hds3FramerStatusEntry": hds3FramerStatusEntry,
       "hds3FramerStatusAddr": hds3FramerStatusAddr,
       "hds3FramerStatusResource": hds3FramerStatusResource,
       "hds3FramerStatusState": hds3FramerStatusState,
       "hds3FramerStatusRedAlrmErrSecs": hds3FramerStatusRedAlrmErrSecs,
       "hds3FramerStatusLOSErrSecs": hds3FramerStatusLOSErrSecs,
       "hds3FramerStatusOOFErrSecs": hds3FramerStatusOOFErrSecs,
       "hds3FramerStatusAISErrSecs": hds3FramerStatusAISErrSecs,
       "hds3FramerStatusRcvIdleErrSecs": hds3FramerStatusRcvIdleErrSecs,
       "hds3FramerStatusFarEndRcvErrSecs": hds3FramerStatusFarEndRcvErrSecs,
       "hds3FramerStatusCFAErrSecs": hds3FramerStatusCFAErrSecs,
       "hds3FramerStatusTotErrSecs": hds3FramerStatusTotErrSecs,
       "hds3FramerStatusPbitParityErrs": hds3FramerStatusPbitParityErrs,
       "hds3FramerStatusCbitParityErrs": hds3FramerStatusCbitParityErrs,
       "hds3FramerStatusFebeErrs": hds3FramerStatusFebeErrs,
       "hds3FramerStatusLCVErrs": hds3FramerStatusLCVErrs,
       "hds3FramerStatusFramingErrs": hds3FramerStatusFramingErrs,
       "hds3FramerStatusExcessZeroErrs": hds3FramerStatusExcessZeroErrs,
       "hds3FramerStatusInsErrMode": hds3FramerStatusInsErrMode,
       "hds3FramerStatusCmdStatus": hds3FramerStatusCmdStatus,
       "hds3LIUTable": hds3LIUTable,
       "hds3LIUEntry": hds3LIUEntry,
       "hds3LIUAddr": hds3LIUAddr,
       "hds3LIUResource": hds3LIUResource,
       "hds3LIUBertState": hds3LIUBertState,
       "hds3LIUBertErrSecs": hds3LIUBertErrSecs,
       "hds3LIUBertDuration": hds3LIUBertDuration,
       "hds3LIULoopType": hds3LIULoopType,
       "hds3LIUDigitalErrs": hds3LIUDigitalErrs,
       "hds3LIUAnalogErrs": hds3LIUAnalogErrs,
       "hds3LIUExcessZeroErrs": hds3LIUExcessZeroErrs,
       "hds3LIUCodingViolationErrs": hds3LIUCodingViolationErrs,
       "hds3LIUPRBSCheckErrs": hds3LIUPRBSCheckErrs,
       "hds3LIUCmdStatus": hds3LIUCmdStatus,
       "eriDNXHybridDS3MIB": eriDNXHybridDS3MIB}
)
