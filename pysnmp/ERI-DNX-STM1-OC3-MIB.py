# SNMP MIB module (ERI-DNX-STM1-OC3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ERI-DNX-STM1-OC3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:29 2024
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

(LinkCmdStatus,
 LinkPortAddress,
 NestSlotAddress,
 OneByteField,
 PortStatus,
 devices,
 trapSequence) = mibBuilder.importSymbols(
    "ERI-DNX-SMC-MIB",
    "LinkCmdStatus",
    "LinkPortAddress",
    "NestSlotAddress",
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

eriDNXStm1Oc3MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 644, 3, 9)
)
eriDNXStm1Oc3MIB.setRevisions(
        ("2003-05-05 00:00",
         "2003-02-27 00:00",
         "2002-04-19 00:00",
         "2002-04-12 00:00",
         "2002-03-01 00:00",
         "2002-01-04 00:00",
         "2001-11-12 00:00",
         "2001-08-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PayLoadGroupType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e1", 0),
          ("t1", 1))
    )



# MIB Managed Objects in the order of their OIDs

_DnxStm1Oc3_ObjectIdentity = ObjectIdentity
dnxStm1Oc3 = _DnxStm1Oc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7)
)
_DnxStm1Oc3Enterprise_ObjectIdentity = ObjectIdentity
dnxStm1Oc3Enterprise = _DnxStm1Oc3Enterprise_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 0)
)
if mibBuilder.loadTexts:
    dnxStm1Oc3Enterprise.setStatus("current")
_OpticalConfig_ObjectIdentity = ObjectIdentity
opticalConfig = _OpticalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 1)
)
_OpticalDevConfigTable_Object = MibTable
opticalDevConfigTable = _OpticalDevConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    opticalDevConfigTable.setStatus("current")
_OpticalDevConfigEntry_Object = MibTableRow
opticalDevConfigEntry = _OpticalDevConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 1, 1, 1)
)
opticalDevConfigEntry.setIndexNames(
    (0, "ERI-DNX-STM1-OC3-MIB", "optDevCfgAddr"),
)
if mibBuilder.loadTexts:
    opticalDevConfigEntry.setStatus("current")
_OptDevCfgAddr_Type = NestSlotAddress
_OptDevCfgAddr_Object = MibTableColumn
optDevCfgAddr = _OptDevCfgAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 1, 1, 1, 1),
    _OptDevCfgAddr_Type()
)
optDevCfgAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optDevCfgAddr.setStatus("current")
_OptDevCfgResource_Type = Integer32
_OptDevCfgResource_Object = MibTableColumn
optDevCfgResource = _OptDevCfgResource_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 1, 1, 1, 2),
    _OptDevCfgResource_Type()
)
optDevCfgResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optDevCfgResource.setStatus("current")


class _OptDevType_Type(Integer32):
    """Custom type optDevType based on Integer32"""
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
        *(("oc3", 1),
          ("oc3X", 3),
          ("stm1", 0),
          ("stm1X", 2))
    )


_OptDevType_Type.__name__ = "Integer32"
_OptDevType_Object = MibTableColumn
optDevType = _OptDevType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 1, 1, 1, 3),
    _OptDevType_Type()
)
optDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optDevType.setStatus("current")


class _OptDevMultiplexMode_Type(Integer32):
    """Custom type optDevMultiplexMode based on Integer32"""
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
        *(("au3", 0),
          ("au4", 1),
          ("au4-vc3-Seq", 4),
          ("sts-3", 2),
          ("sts-3c", 3))
    )


_OptDevMultiplexMode_Type.__name__ = "Integer32"
_OptDevMultiplexMode_Object = MibTableColumn
optDevMultiplexMode = _OptDevMultiplexMode_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 1, 1, 1, 4),
    _OptDevMultiplexMode_Type()
)
optDevMultiplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optDevMultiplexMode.setStatus("current")


class _OptLineTiming_Type(Integer32):
    """Custom type optLineTiming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("loop", 1))
    )


_OptLineTiming_Type.__name__ = "Integer32"
_OptLineTiming_Object = MibTableColumn
optLineTiming = _OptLineTiming_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 1, 1, 1, 5),
    _OptLineTiming_Type()
)
optLineTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optLineTiming.setStatus("current")
_OptDevPayload1_Type = PayLoadGroupType
_OptDevPayload1_Object = MibTableColumn
optDevPayload1 = _OptDevPayload1_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 1, 1, 1, 6),
    _OptDevPayload1_Type()
)
optDevPayload1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optDevPayload1.setStatus("current")
_OptDevPayload2_Type = PayLoadGroupType
_OptDevPayload2_Object = MibTableColumn
optDevPayload2 = _OptDevPayload2_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 1, 1, 1, 7),
    _OptDevPayload2_Type()
)
optDevPayload2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optDevPayload2.setStatus("current")
_OptDevPayload3_Type = PayLoadGroupType
_OptDevPayload3_Object = MibTableColumn
optDevPayload3 = _OptDevPayload3_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 1, 1, 1, 8),
    _OptDevPayload3_Type()
)
optDevPayload3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optDevPayload3.setStatus("current")


class _OptDevCmdStatus_Type(Integer32):
    """Custom type optDevCmdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              101,
              400,
              402,
              403,
              414,
              415,
              416,
              419,
              421,
              424,
              427,
              450,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("err-au4Seq-cannot-be-mixed-framing", 402),
          ("err-data-locked-by-another-user", 450),
          ("err-device-is-protection-module", 414),
          ("err-general-opt-config-error", 400),
          ("err-invalid-line-timing", 421),
          ("err-invalid-multiplex-map", 415),
          ("err-invalid-opt-dev-command", 403),
          ("err-invalid-payload-framing", 416),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-invalid-xlink-nest-num", 419),
          ("err-snmp-parse-failed", 500),
          ("err-ts-alloc-not-applicable", 424),
          ("err-xlink-pair-not-applicable", 427),
          ("ready-for-command", 0),
          ("update-config", 1),
          ("update-successful", 101))
    )


_OptDevCmdStatus_Type.__name__ = "Integer32"
_OptDevCmdStatus_Object = MibTableColumn
optDevCmdStatus = _OptDevCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 1, 1, 1, 9),
    _OptDevCmdStatus_Type()
)
optDevCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optDevCmdStatus.setStatus("current")


class _OptDevTsAlloc_Type(Integer32):
    """Custom type optDevTsAlloc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 1),
          ("normal", 0))
    )


_OptDevTsAlloc_Type.__name__ = "Integer32"
_OptDevTsAlloc_Object = MibTableColumn
optDevTsAlloc = _OptDevTsAlloc_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 1, 1, 1, 10),
    _OptDevTsAlloc_Type()
)
optDevTsAlloc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optDevTsAlloc.setStatus("current")


class _OptDevAssignedToNest_Type(Integer32):
    """Custom type optDevAssignedToNest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 8),
    )


_OptDevAssignedToNest_Type.__name__ = "Integer32"
_OptDevAssignedToNest_Object = MibTableColumn
optDevAssignedToNest = _OptDevAssignedToNest_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 1, 1, 1, 11),
    _OptDevAssignedToNest_Type()
)
optDevAssignedToNest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optDevAssignedToNest.setStatus("current")
_OptT1E1LinkConfigTable_Object = MibTable
optT1E1LinkConfigTable = _OptT1E1LinkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 1, 2)
)
if mibBuilder.loadTexts:
    optT1E1LinkConfigTable.setStatus("current")
_OptT1E1LinkConfigEntry_Object = MibTableRow
optT1E1LinkConfigEntry = _OptT1E1LinkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 1, 2, 1)
)
optT1E1LinkConfigEntry.setIndexNames(
    (0, "ERI-DNX-STM1-OC3-MIB", "optT1E1CfgLinkAddr"),
)
if mibBuilder.loadTexts:
    optT1E1LinkConfigEntry.setStatus("current")
_OptT1E1CfgLinkAddr_Type = LinkPortAddress
_OptT1E1CfgLinkAddr_Object = MibTableColumn
optT1E1CfgLinkAddr = _OptT1E1CfgLinkAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 1, 2, 1, 1),
    _OptT1E1CfgLinkAddr_Type()
)
optT1E1CfgLinkAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optT1E1CfgLinkAddr.setStatus("current")
_OptT1E1CfgResource_Type = Integer32
_OptT1E1CfgResource_Object = MibTableColumn
optT1E1CfgResource = _OptT1E1CfgResource_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 1, 2, 1, 2),
    _OptT1E1CfgResource_Type()
)
optT1E1CfgResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optT1E1CfgResource.setStatus("current")


class _OptT1E1CfgLinkName_Type(DisplayString):
    """Custom type optT1E1CfgLinkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_OptT1E1CfgLinkName_Type.__name__ = "DisplayString"
_OptT1E1CfgLinkName_Object = MibTableColumn
optT1E1CfgLinkName = _OptT1E1CfgLinkName_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 1, 2, 1, 3),
    _OptT1E1CfgLinkName_Type()
)
optT1E1CfgLinkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optT1E1CfgLinkName.setStatus("current")
_OptT1E1Status_Type = PortStatus
_OptT1E1Status_Object = MibTableColumn
optT1E1Status = _OptT1E1Status_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 1, 2, 1, 4),
    _OptT1E1Status_Type()
)
optT1E1Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optT1E1Status.setStatus("current")


class _OptT1E1Clear_Type(Integer32):
    """Custom type optT1E1Clear based on Integer32"""
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


_OptT1E1Clear_Type.__name__ = "Integer32"
_OptT1E1Clear_Object = MibTableColumn
optT1E1Clear = _OptT1E1Clear_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 1, 2, 1, 5),
    _OptT1E1Clear_Type()
)
optT1E1Clear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optT1E1Clear.setStatus("current")


class _OptT1E1Framing_Type(Integer32):
    """Custom type optT1E1Framing based on Integer32"""
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


_OptT1E1Framing_Type.__name__ = "Integer32"
_OptT1E1Framing_Object = MibTableColumn
optT1E1Framing = _OptT1E1Framing_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 1, 2, 1, 6),
    _OptT1E1Framing_Type()
)
optT1E1Framing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optT1E1Framing.setStatus("current")


class _OptT1E1RecoverTime_Type(Integer32):
    """Custom type optT1E1RecoverTime based on Integer32"""
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


_OptT1E1RecoverTime_Type.__name__ = "Integer32"
_OptT1E1RecoverTime_Object = MibTableColumn
optT1E1RecoverTime = _OptT1E1RecoverTime_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 1, 2, 1, 7),
    _OptT1E1RecoverTime_Type()
)
optT1E1RecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optT1E1RecoverTime.setStatus("current")


class _OptT1E1EsfFormat_Type(Integer32):
    """Custom type optT1E1EsfFormat based on Integer32"""
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


_OptT1E1EsfFormat_Type.__name__ = "Integer32"
_OptT1E1EsfFormat_Object = MibTableColumn
optT1E1EsfFormat = _OptT1E1EsfFormat_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 1, 2, 1, 8),
    _OptT1E1EsfFormat_Type()
)
optT1E1EsfFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optT1E1EsfFormat.setStatus("current")


class _OptT1E1UnusedTSs_Type(Integer32):
    """Custom type optT1E1UnusedTSs based on Integer32"""
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


_OptT1E1UnusedTSs_Type.__name__ = "Integer32"
_OptT1E1UnusedTSs_Object = MibTableColumn
optT1E1UnusedTSs = _OptT1E1UnusedTSs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 1, 2, 1, 9),
    _OptT1E1UnusedTSs_Type()
)
optT1E1UnusedTSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optT1E1UnusedTSs.setStatus("current")
_OptT1E1CfgCmdStatus_Type = LinkCmdStatus
_OptT1E1CfgCmdStatus_Object = MibTableColumn
optT1E1CfgCmdStatus = _OptT1E1CfgCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 1, 2, 1, 10),
    _OptT1E1CfgCmdStatus_Type()
)
optT1E1CfgCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optT1E1CfgCmdStatus.setStatus("current")
_OptT1E1NationalBits_Type = OneByteField
_OptT1E1NationalBits_Object = MibTableColumn
optT1E1NationalBits = _OptT1E1NationalBits_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 1, 2, 1, 11),
    _OptT1E1NationalBits_Type()
)
optT1E1NationalBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optT1E1NationalBits.setStatus("current")
_OptT1E1InterNational_Type = OneByteField
_OptT1E1InterNational_Object = MibTableColumn
optT1E1InterNational = _OptT1E1InterNational_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 1, 2, 1, 12),
    _OptT1E1InterNational_Type()
)
optT1E1InterNational.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optT1E1InterNational.setStatus("current")
_OpticalDiag_ObjectIdentity = ObjectIdentity
opticalDiag = _OpticalDiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2)
)
_OpticalTUStatusTable_Object = MibTable
opticalTUStatusTable = _OpticalTUStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 1)
)
if mibBuilder.loadTexts:
    opticalTUStatusTable.setStatus("current")
_OpticalTUStatusEntry_Object = MibTableRow
opticalTUStatusEntry = _OpticalTUStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 1, 1)
)
opticalTUStatusEntry.setIndexNames(
    (0, "ERI-DNX-STM1-OC3-MIB", "optTUStatusAddr"),
)
if mibBuilder.loadTexts:
    opticalTUStatusEntry.setStatus("current")
_OptTUStatusAddr_Type = LinkPortAddress
_OptTUStatusAddr_Object = MibTableColumn
optTUStatusAddr = _OptTUStatusAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 1, 1, 1),
    _OptTUStatusAddr_Type()
)
optTUStatusAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optTUStatusAddr.setStatus("current")
_OptTUStatusResrcId_Type = Integer32
_OptTUStatusResrcId_Object = MibTableColumn
optTUStatusResrcId = _OptTUStatusResrcId_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 1, 1, 2),
    _OptTUStatusResrcId_Type()
)
optTUStatusResrcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optTUStatusResrcId.setStatus("current")


class _OptTUStatusLinkState_Type(Integer32):
    """Custom type optTUStatusLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              8,
              32,
              64,
              2048,
              4096,
              65535,
              2097152,
              4194304,
              6291456,
              8388608,
              1073741824,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("ais", 8),
          ("cfa", 4096),
          ("errors", 2147483647),
          ("lof", 32),
          ("los", 64),
          ("ok", 0),
          ("oos", 65535),
          ("red", 2048),
          ("rxSlip", 4194304),
          ("sef", 8388608),
          ("slip", 6291456),
          ("txSlip", 2097152),
          ("underTest", 1073741824),
          ("yel", 2))
    )


_OptTUStatusLinkState_Type.__name__ = "Integer32"
_OptTUStatusLinkState_Object = MibTableColumn
optTUStatusLinkState = _OptTUStatusLinkState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 1, 1, 3),
    _OptTUStatusLinkState_Type()
)
optTUStatusLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optTUStatusLinkState.setStatus("current")
_OptTUStatusErrSecs_Type = Counter32
_OptTUStatusErrSecs_Object = MibTableColumn
optTUStatusErrSecs = _OptTUStatusErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 1, 1, 4),
    _OptTUStatusErrSecs_Type()
)
optTUStatusErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optTUStatusErrSecs.setStatus("current")
_OptTUStatusAisErrs_Type = Counter32
_OptTUStatusAisErrs_Object = MibTableColumn
optTUStatusAisErrs = _OptTUStatusAisErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 1, 1, 5),
    _OptTUStatusAisErrs_Type()
)
optTUStatusAisErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optTUStatusAisErrs.setStatus("current")
_OptTUStatusLopErrs_Type = Counter32
_OptTUStatusLopErrs_Object = MibTableColumn
optTUStatusLopErrs = _OptTUStatusLopErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 1, 1, 6),
    _OptTUStatusLopErrs_Type()
)
optTUStatusLopErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optTUStatusLopErrs.setStatus("current")
_OptTUStatusRdiTUErrs_Type = Counter32
_OptTUStatusRdiTUErrs_Object = MibTableColumn
optTUStatusRdiTUErrs = _OptTUStatusRdiTUErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 1, 1, 7),
    _OptTUStatusRdiTUErrs_Type()
)
optTUStatusRdiTUErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optTUStatusRdiTUErrs.setStatus("current")
_OptTUStatusRfiTUErrs_Type = Counter32
_OptTUStatusRfiTUErrs_Object = MibTableColumn
optTUStatusRfiTUErrs = _OptTUStatusRfiTUErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 1, 1, 8),
    _OptTUStatusRfiTUErrs_Type()
)
optTUStatusRfiTUErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optTUStatusRfiTUErrs.setStatus("current")
_OptTUStatusPSLMErrs_Type = Counter32
_OptTUStatusPSLMErrs_Object = MibTableColumn
optTUStatusPSLMErrs = _OptTUStatusPSLMErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 1, 1, 9),
    _OptTUStatusPSLMErrs_Type()
)
optTUStatusPSLMErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optTUStatusPSLMErrs.setStatus("current")
_OptTUStatusPSLUErrs_Type = Counter32
_OptTUStatusPSLUErrs_Object = MibTableColumn
optTUStatusPSLUErrs = _OptTUStatusPSLUErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 1, 1, 10),
    _OptTUStatusPSLUErrs_Type()
)
optTUStatusPSLUErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optTUStatusPSLUErrs.setStatus("current")
_OptTUStatusErrFreeSecs_Type = Counter32
_OptTUStatusErrFreeSecs_Object = MibTableColumn
optTUStatusErrFreeSecs = _OptTUStatusErrFreeSecs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 1, 1, 11),
    _OptTUStatusErrFreeSecs_Type()
)
optTUStatusErrFreeSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optTUStatusErrFreeSecs.setStatus("current")
_OpticalMapperStatusTable_Object = MibTable
opticalMapperStatusTable = _OpticalMapperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 2)
)
if mibBuilder.loadTexts:
    opticalMapperStatusTable.setStatus("current")
_OpticalMapperStatusEntry_Object = MibTableRow
opticalMapperStatusEntry = _OpticalMapperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 2, 1)
)
opticalMapperStatusEntry.setIndexNames(
    (0, "ERI-DNX-STM1-OC3-MIB", "optMapperStatusAddr"),
)
if mibBuilder.loadTexts:
    opticalMapperStatusEntry.setStatus("current")
_OptMapperStatusAddr_Type = LinkPortAddress
_OptMapperStatusAddr_Object = MibTableColumn
optMapperStatusAddr = _OptMapperStatusAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 2, 1, 1),
    _OptMapperStatusAddr_Type()
)
optMapperStatusAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optMapperStatusAddr.setStatus("current")
_OptMapperStatusResrcId_Type = Integer32
_OptMapperStatusResrcId_Object = MibTableColumn
optMapperStatusResrcId = _OptMapperStatusResrcId_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 2, 1, 2),
    _OptMapperStatusResrcId_Type()
)
optMapperStatusResrcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optMapperStatusResrcId.setStatus("current")


class _OptMapperState_Type(Integer32):
    """Custom type optMapperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              8,
              16,
              32,
              64,
              128,
              2048,
              4096,
              65535,
              2097152,
              4194304,
              6291456,
              8388608,
              1073741824,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("ais", 8),
          ("cfa", 4096),
          ("errors", 2147483647),
          ("lof", 32),
          ("lop", 16),
          ("los", 64),
          ("ok", 0),
          ("oos", 65535),
          ("rdi", 128),
          ("red", 2048),
          ("rxSlip", 4194304),
          ("sef", 8388608),
          ("slip", 6291456),
          ("txSlip", 2097152),
          ("underTest", 1073741824),
          ("yel", 2))
    )


_OptMapperState_Type.__name__ = "Integer32"
_OptMapperState_Object = MibTableColumn
optMapperState = _OptMapperState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 2, 1, 3),
    _OptMapperState_Type()
)
optMapperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optMapperState.setStatus("current")
_OptMapperErrSecs_Type = Counter32
_OptMapperErrSecs_Object = MibTableColumn
optMapperErrSecs = _OptMapperErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 2, 1, 4),
    _OptMapperErrSecs_Type()
)
optMapperErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optMapperErrSecs.setStatus("current")
_OptMapperErrFreeSecs_Type = Counter32
_OptMapperErrFreeSecs_Object = MibTableColumn
optMapperErrFreeSecs = _OptMapperErrFreeSecs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 2, 1, 5),
    _OptMapperErrFreeSecs_Type()
)
optMapperErrFreeSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optMapperErrFreeSecs.setStatus("current")


class _OptMapperLoop_Type(Integer32):
    """Custom type optMapperLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("line", 3),
          ("local", 1),
          ("off", 0))
    )


_OptMapperLoop_Type.__name__ = "Integer32"
_OptMapperLoop_Object = MibTableColumn
optMapperLoop = _OptMapperLoop_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 2, 1, 6),
    _OptMapperLoop_Type()
)
optMapperLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optMapperLoop.setStatus("current")
_OptMapperPathLOPErrs_Type = Counter32
_OptMapperPathLOPErrs_Object = MibTableColumn
optMapperPathLOPErrs = _OptMapperPathLOPErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 2, 1, 7),
    _OptMapperPathLOPErrs_Type()
)
optMapperPathLOPErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optMapperPathLOPErrs.setStatus("current")
_OptMapperPathAISErrs_Type = Counter32
_OptMapperPathAISErrs_Object = MibTableColumn
optMapperPathAISErrs = _OptMapperPathAISErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 2, 1, 8),
    _OptMapperPathAISErrs_Type()
)
optMapperPathAISErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optMapperPathAISErrs.setStatus("current")
_OptMapperPathRDIErrs_Type = Counter32
_OptMapperPathRDIErrs_Object = MibTableColumn
optMapperPathRDIErrs = _OptMapperPathRDIErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 2, 1, 9),
    _OptMapperPathRDIErrs_Type()
)
optMapperPathRDIErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optMapperPathRDIErrs.setStatus("current")


class _OptMapperCmdStatus_Type(Integer32):
    """Custom type optMapperCmdStatus based on Integer32"""
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
          ("err-invalid-loop-type", 202),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-snmp-parse-failed", 500),
          ("ready-for-command", 0),
          ("update-successful", 101),
          ("updateTest", 1))
    )


_OptMapperCmdStatus_Type.__name__ = "Integer32"
_OptMapperCmdStatus_Object = MibTableColumn
optMapperCmdStatus = _OptMapperCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 2, 1, 10),
    _OptMapperCmdStatus_Type()
)
optMapperCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optMapperCmdStatus.setStatus("current")
_OpticalTransportStatusTable_Object = MibTable
opticalTransportStatusTable = _OpticalTransportStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 3)
)
if mibBuilder.loadTexts:
    opticalTransportStatusTable.setStatus("current")
_OpticalTransportStatusEntry_Object = MibTableRow
opticalTransportStatusEntry = _OpticalTransportStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 3, 1)
)
opticalTransportStatusEntry.setIndexNames(
    (0, "ERI-DNX-STM1-OC3-MIB", "optTransportStatusAddr"),
)
if mibBuilder.loadTexts:
    opticalTransportStatusEntry.setStatus("current")
_OptTransportStatusAddr_Type = NestSlotAddress
_OptTransportStatusAddr_Object = MibTableColumn
optTransportStatusAddr = _OptTransportStatusAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 3, 1, 1),
    _OptTransportStatusAddr_Type()
)
optTransportStatusAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optTransportStatusAddr.setStatus("current")
_OptTransportStatusResrcId_Type = Integer32
_OptTransportStatusResrcId_Object = MibTableColumn
optTransportStatusResrcId = _OptTransportStatusResrcId_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 3, 1, 2),
    _OptTransportStatusResrcId_Type()
)
optTransportStatusResrcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optTransportStatusResrcId.setStatus("current")


class _OptTransportLaserState_Type(Integer32):
    """Custom type optTransportLaserState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OptTransportLaserState_Type.__name__ = "Integer32"
_OptTransportLaserState_Object = MibTableColumn
optTransportLaserState = _OptTransportLaserState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 3, 1, 3),
    _OptTransportLaserState_Type()
)
optTransportLaserState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optTransportLaserState.setStatus("current")
_OptTransportErrSecs_Type = Counter32
_OptTransportErrSecs_Object = MibTableColumn
optTransportErrSecs = _OptTransportErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 3, 1, 4),
    _OptTransportErrSecs_Type()
)
optTransportErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optTransportErrSecs.setStatus("current")
_OptTransportErrFreeSecs_Type = Counter32
_OptTransportErrFreeSecs_Object = MibTableColumn
optTransportErrFreeSecs = _OptTransportErrFreeSecs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 3, 1, 5),
    _OptTransportErrFreeSecs_Type()
)
optTransportErrFreeSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optTransportErrFreeSecs.setStatus("current")


class _OptTransportLoop_Type(Integer32):
    """Custom type optTransportLoop based on Integer32"""
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
        *(("facility", 2),
          ("off", 0),
          ("pathFacility", 3),
          ("terminal", 1))
    )


_OptTransportLoop_Type.__name__ = "Integer32"
_OptTransportLoop_Object = MibTableColumn
optTransportLoop = _OptTransportLoop_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 3, 1, 6),
    _OptTransportLoop_Type()
)
optTransportLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optTransportLoop.setStatus("current")
_OptTransportLineAISErrs_Type = Counter32
_OptTransportLineAISErrs_Object = MibTableColumn
optTransportLineAISErrs = _OptTransportLineAISErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 3, 1, 7),
    _OptTransportLineAISErrs_Type()
)
optTransportLineAISErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optTransportLineAISErrs.setStatus("current")
_OptTransportLineRDIErrs_Type = Counter32
_OptTransportLineRDIErrs_Object = MibTableColumn
optTransportLineRDIErrs = _OptTransportLineRDIErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 3, 1, 8),
    _OptTransportLineRDIErrs_Type()
)
optTransportLineRDIErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optTransportLineRDIErrs.setStatus("current")
_OptTransportLineOOFErrs_Type = Counter32
_OptTransportLineOOFErrs_Object = MibTableColumn
optTransportLineOOFErrs = _OptTransportLineOOFErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 3, 1, 9),
    _OptTransportLineOOFErrs_Type()
)
optTransportLineOOFErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optTransportLineOOFErrs.setStatus("current")
_OptTransportLineLOFErrs_Type = Counter32
_OptTransportLineLOFErrs_Object = MibTableColumn
optTransportLineLOFErrs = _OptTransportLineLOFErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 3, 1, 10),
    _OptTransportLineLOFErrs_Type()
)
optTransportLineLOFErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optTransportLineLOFErrs.setStatus("current")
_OptTransportLineLOSErrs_Type = Counter32
_OptTransportLineLOSErrs_Object = MibTableColumn
optTransportLineLOSErrs = _OptTransportLineLOSErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 3, 1, 11),
    _OptTransportLineLOSErrs_Type()
)
optTransportLineLOSErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optTransportLineLOSErrs.setStatus("current")


class _OptTransportCmdStatus_Type(Integer32):
    """Custom type optTransportCmdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              14,
              101,
              114,
              400,
              402,
              406,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("clear-successful", 114),
          ("clearErrors", 14),
          ("err-field-cannot-be-set", 406),
          ("err-general-test-error", 400),
          ("err-invalid-loop-type", 402),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-snmp-parse-failed", 500),
          ("ready-for-command", 0),
          ("update-successful", 101),
          ("updateTest", 1))
    )


_OptTransportCmdStatus_Type.__name__ = "Integer32"
_OptTransportCmdStatus_Object = MibTableColumn
optTransportCmdStatus = _OptTransportCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 2, 3, 1, 12),
    _OptTransportCmdStatus_Type()
)
optTransportCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optTransportCmdStatus.setStatus("current")

# Managed Objects groups


# Notification objects

optDevConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 0, 1)
)
optDevConfigTrap.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-STM1-OC3-MIB", "optDevCfgAddr"),
        ("ERI-DNX-STM1-OC3-MIB", "optDevCmdStatus"))
)
if mibBuilder.loadTexts:
    optDevConfigTrap.setStatus(
        "current"
    )

optT1E1ConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 7, 0, 2)
)
optT1E1ConfigTrap.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-STM1-OC3-MIB", "optT1E1CfgLinkAddr"),
        ("ERI-DNX-STM1-OC3-MIB", "optT1E1CfgCmdStatus"))
)
if mibBuilder.loadTexts:
    optT1E1ConfigTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ERI-DNX-STM1-OC3-MIB",
    **{"PayLoadGroupType": PayLoadGroupType,
       "dnxStm1Oc3": dnxStm1Oc3,
       "dnxStm1Oc3Enterprise": dnxStm1Oc3Enterprise,
       "optDevConfigTrap": optDevConfigTrap,
       "optT1E1ConfigTrap": optT1E1ConfigTrap,
       "opticalConfig": opticalConfig,
       "opticalDevConfigTable": opticalDevConfigTable,
       "opticalDevConfigEntry": opticalDevConfigEntry,
       "optDevCfgAddr": optDevCfgAddr,
       "optDevCfgResource": optDevCfgResource,
       "optDevType": optDevType,
       "optDevMultiplexMode": optDevMultiplexMode,
       "optLineTiming": optLineTiming,
       "optDevPayload1": optDevPayload1,
       "optDevPayload2": optDevPayload2,
       "optDevPayload3": optDevPayload3,
       "optDevCmdStatus": optDevCmdStatus,
       "optDevTsAlloc": optDevTsAlloc,
       "optDevAssignedToNest": optDevAssignedToNest,
       "optT1E1LinkConfigTable": optT1E1LinkConfigTable,
       "optT1E1LinkConfigEntry": optT1E1LinkConfigEntry,
       "optT1E1CfgLinkAddr": optT1E1CfgLinkAddr,
       "optT1E1CfgResource": optT1E1CfgResource,
       "optT1E1CfgLinkName": optT1E1CfgLinkName,
       "optT1E1Status": optT1E1Status,
       "optT1E1Clear": optT1E1Clear,
       "optT1E1Framing": optT1E1Framing,
       "optT1E1RecoverTime": optT1E1RecoverTime,
       "optT1E1EsfFormat": optT1E1EsfFormat,
       "optT1E1UnusedTSs": optT1E1UnusedTSs,
       "optT1E1CfgCmdStatus": optT1E1CfgCmdStatus,
       "optT1E1NationalBits": optT1E1NationalBits,
       "optT1E1InterNational": optT1E1InterNational,
       "opticalDiag": opticalDiag,
       "opticalTUStatusTable": opticalTUStatusTable,
       "opticalTUStatusEntry": opticalTUStatusEntry,
       "optTUStatusAddr": optTUStatusAddr,
       "optTUStatusResrcId": optTUStatusResrcId,
       "optTUStatusLinkState": optTUStatusLinkState,
       "optTUStatusErrSecs": optTUStatusErrSecs,
       "optTUStatusAisErrs": optTUStatusAisErrs,
       "optTUStatusLopErrs": optTUStatusLopErrs,
       "optTUStatusRdiTUErrs": optTUStatusRdiTUErrs,
       "optTUStatusRfiTUErrs": optTUStatusRfiTUErrs,
       "optTUStatusPSLMErrs": optTUStatusPSLMErrs,
       "optTUStatusPSLUErrs": optTUStatusPSLUErrs,
       "optTUStatusErrFreeSecs": optTUStatusErrFreeSecs,
       "opticalMapperStatusTable": opticalMapperStatusTable,
       "opticalMapperStatusEntry": opticalMapperStatusEntry,
       "optMapperStatusAddr": optMapperStatusAddr,
       "optMapperStatusResrcId": optMapperStatusResrcId,
       "optMapperState": optMapperState,
       "optMapperErrSecs": optMapperErrSecs,
       "optMapperErrFreeSecs": optMapperErrFreeSecs,
       "optMapperLoop": optMapperLoop,
       "optMapperPathLOPErrs": optMapperPathLOPErrs,
       "optMapperPathAISErrs": optMapperPathAISErrs,
       "optMapperPathRDIErrs": optMapperPathRDIErrs,
       "optMapperCmdStatus": optMapperCmdStatus,
       "opticalTransportStatusTable": opticalTransportStatusTable,
       "opticalTransportStatusEntry": opticalTransportStatusEntry,
       "optTransportStatusAddr": optTransportStatusAddr,
       "optTransportStatusResrcId": optTransportStatusResrcId,
       "optTransportLaserState": optTransportLaserState,
       "optTransportErrSecs": optTransportErrSecs,
       "optTransportErrFreeSecs": optTransportErrFreeSecs,
       "optTransportLoop": optTransportLoop,
       "optTransportLineAISErrs": optTransportLineAISErrs,
       "optTransportLineRDIErrs": optTransportLineRDIErrs,
       "optTransportLineOOFErrs": optTransportLineOOFErrs,
       "optTransportLineLOFErrs": optTransportLineLOFErrs,
       "optTransportLineLOSErrs": optTransportLineLOSErrs,
       "optTransportCmdStatus": optTransportCmdStatus,
       "eriDNXStm1Oc3MIB": eriDNXStm1Oc3MIB}
)
