# SNMP MIB module (APPIAN-PPORT-SONET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPIAN-PPORT-SONET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:42 2024
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

(AcAdminStatus,
 AcNodeId,
 AcOpStatus,
 AcPortNumber,
 AcSlotNumber,
 acPport) = mibBuilder.importSymbols(
    "APPIAN-SMI-MIB",
    "AcAdminStatus",
    "AcNodeId",
    "AcOpStatus",
    "AcPortNumber",
    "AcSlotNumber",
    "acPport")

(PerfIntervalCount,) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfIntervalCount")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

acSonet = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6)
)
acSonet.setRevisions(
        ("1900-02-23 16:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AcTraceString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )



# MIB Managed Objects in the order of their OIDs

_AcSonetObjects_ObjectIdentity = ObjectIdentity
acSonetObjects = _AcSonetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1)
)
_AcSonetPort_ObjectIdentity = ObjectIdentity
acSonetPort = _AcSonetPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1)
)
_AcSonetPortTable_Object = MibTable
acSonetPortTable = _AcSonetPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    acSonetPortTable.setStatus("current")
_AcSonetPortEntry_Object = MibTableRow
acSonetPortEntry = _AcSonetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 1, 1)
)
acSonetPortEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPortNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPortSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPortPort"),
)
if mibBuilder.loadTexts:
    acSonetPortEntry.setStatus("current")
_AcSonetPortNodeId_Type = AcNodeId
_AcSonetPortNodeId_Object = MibTableColumn
acSonetPortNodeId = _AcSonetPortNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 1, 1, 1),
    _AcSonetPortNodeId_Type()
)
acSonetPortNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPortNodeId.setStatus("current")
_AcSonetPortSlot_Type = AcSlotNumber
_AcSonetPortSlot_Object = MibTableColumn
acSonetPortSlot = _AcSonetPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 1, 1, 2),
    _AcSonetPortSlot_Type()
)
acSonetPortSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPortSlot.setStatus("current")
_AcSonetPortPort_Type = AcPortNumber
_AcSonetPortPort_Object = MibTableColumn
acSonetPortPort = _AcSonetPortPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 1, 1, 3),
    _AcSonetPortPort_Type()
)
acSonetPortPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPortPort.setStatus("current")


class _AcSonetPortAdminStatus_Type(AcAdminStatus):
    """Custom type acSonetPortAdminStatus based on AcAdminStatus"""


_AcSonetPortAdminStatus_Object = MibTableColumn
acSonetPortAdminStatus = _AcSonetPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 1, 1, 4),
    _AcSonetPortAdminStatus_Type()
)
acSonetPortAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSonetPortAdminStatus.setStatus("current")
_AcSonetPortOpStatus_Type = AcOpStatus
_AcSonetPortOpStatus_Object = MibTableColumn
acSonetPortOpStatus = _AcSonetPortOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 1, 1, 5),
    _AcSonetPortOpStatus_Type()
)
acSonetPortOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetPortOpStatus.setStatus("current")
_AcSonetPortOpCode_Type = Integer32
_AcSonetPortOpCode_Object = MibTableColumn
acSonetPortOpCode = _AcSonetPortOpCode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 1, 1, 6),
    _AcSonetPortOpCode_Type()
)
acSonetPortOpCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetPortOpCode.setStatus("current")


class _AcSonetPortMediumType_Type(Integer32):
    """Custom type acSonetPortMediumType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdh", 2),
          ("sonet", 1))
    )


_AcSonetPortMediumType_Type.__name__ = "Integer32"
_AcSonetPortMediumType_Object = MibTableColumn
acSonetPortMediumType = _AcSonetPortMediumType_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 1, 1, 7),
    _AcSonetPortMediumType_Type()
)
acSonetPortMediumType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSonetPortMediumType.setStatus("current")


class _AcSonetPortTimeElapsed_Type(Integer32):
    """Custom type acSonetPortTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_AcSonetPortTimeElapsed_Type.__name__ = "Integer32"
_AcSonetPortTimeElapsed_Object = MibTableColumn
acSonetPortTimeElapsed = _AcSonetPortTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 1, 1, 8),
    _AcSonetPortTimeElapsed_Type()
)
acSonetPortTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetPortTimeElapsed.setStatus("current")


class _AcSonetPortValidIntervals_Type(Integer32):
    """Custom type acSonetPortValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AcSonetPortValidIntervals_Type.__name__ = "Integer32"
_AcSonetPortValidIntervals_Object = MibTableColumn
acSonetPortValidIntervals = _AcSonetPortValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 1, 1, 9),
    _AcSonetPortValidIntervals_Type()
)
acSonetPortValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetPortValidIntervals.setStatus("current")


class _AcSonetPortMediumLineCoding_Type(Integer32):
    """Custom type acSonetPortMediumLineCoding based on Integer32"""
    defaultValue = 4

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
        *(("b3zs", 2),
          ("cmi", 3),
          ("nrz", 4),
          ("other", 1),
          ("rz", 5))
    )


_AcSonetPortMediumLineCoding_Type.__name__ = "Integer32"
_AcSonetPortMediumLineCoding_Object = MibTableColumn
acSonetPortMediumLineCoding = _AcSonetPortMediumLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 1, 1, 10),
    _AcSonetPortMediumLineCoding_Type()
)
acSonetPortMediumLineCoding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSonetPortMediumLineCoding.setStatus("current")


class _AcSonetPortMediumLineType_Type(Integer32):
    """Custom type acSonetPortMediumLineType based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("coax", 5),
          ("intermediate", 7),
          ("long-single", 3),
          ("multi", 4),
          ("other", 1),
          ("short-single", 2),
          ("utp", 6))
    )


_AcSonetPortMediumLineType_Type.__name__ = "Integer32"
_AcSonetPortMediumLineType_Object = MibTableColumn
acSonetPortMediumLineType = _AcSonetPortMediumLineType_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 1, 1, 11),
    _AcSonetPortMediumLineType_Type()
)
acSonetPortMediumLineType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSonetPortMediumLineType.setStatus("current")


class _AcSonetPortTransmitterEnable_Type(TruthValue):
    """Custom type acSonetPortTransmitterEnable based on TruthValue"""


_AcSonetPortTransmitterEnable_Object = MibTableColumn
acSonetPortTransmitterEnable = _AcSonetPortTransmitterEnable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 1, 1, 12),
    _AcSonetPortTransmitterEnable_Type()
)
acSonetPortTransmitterEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSonetPortTransmitterEnable.setStatus("current")


class _AcSonetPortCircuitIdentifier_Type(DisplayString):
    """Custom type acSonetPortCircuitIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcSonetPortCircuitIdentifier_Type.__name__ = "DisplayString"
_AcSonetPortCircuitIdentifier_Object = MibTableColumn
acSonetPortCircuitIdentifier = _AcSonetPortCircuitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 1, 1, 13),
    _AcSonetPortCircuitIdentifier_Type()
)
acSonetPortCircuitIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSonetPortCircuitIdentifier.setStatus("current")


class _AcSonetPortInvalidIntervals_Type(Integer32):
    """Custom type acSonetPortInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AcSonetPortInvalidIntervals_Type.__name__ = "Integer32"
_AcSonetPortInvalidIntervals_Object = MibTableColumn
acSonetPortInvalidIntervals = _AcSonetPortInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 1, 1, 14),
    _AcSonetPortInvalidIntervals_Type()
)
acSonetPortInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetPortInvalidIntervals.setStatus("current")


class _AcSonetPortLoopbackConfig_Type(Integer32):
    """Custom type acSonetPortLoopbackConfig based on Integer32"""
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
        *(("facility", 1),
          ("none", 0),
          ("other", 3),
          ("terminal", 2))
    )


_AcSonetPortLoopbackConfig_Type.__name__ = "Integer32"
_AcSonetPortLoopbackConfig_Object = MibTableColumn
acSonetPortLoopbackConfig = _AcSonetPortLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 1, 1, 15),
    _AcSonetPortLoopbackConfig_Type()
)
acSonetPortLoopbackConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSonetPortLoopbackConfig.setStatus("current")


class _AcSonetPortResetCurrentPMregs_Type(TruthValue):
    """Custom type acSonetPortResetCurrentPMregs based on TruthValue"""


_AcSonetPortResetCurrentPMregs_Object = MibTableColumn
acSonetPortResetCurrentPMregs = _AcSonetPortResetCurrentPMregs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 1, 1, 16),
    _AcSonetPortResetCurrentPMregs_Type()
)
acSonetPortResetCurrentPMregs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSonetPortResetCurrentPMregs.setStatus("current")


class _AcSonetPortResetAllPMregs_Type(TruthValue):
    """Custom type acSonetPortResetAllPMregs based on TruthValue"""


_AcSonetPortResetAllPMregs_Object = MibTableColumn
acSonetPortResetAllPMregs = _AcSonetPortResetAllPMregs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 1, 1, 17),
    _AcSonetPortResetAllPMregs_Type()
)
acSonetPortResetAllPMregs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSonetPortResetAllPMregs.setStatus("current")


class _AcSonetPortConnectionType_Type(Integer32):
    """Custom type acSonetPortConnectionType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interconnect", 2),
          ("ring", 1))
    )


_AcSonetPortConnectionType_Type.__name__ = "Integer32"
_AcSonetPortConnectionType_Object = MibTableColumn
acSonetPortConnectionType = _AcSonetPortConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 1, 1, 18),
    _AcSonetPortConnectionType_Type()
)
acSonetPortConnectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSonetPortConnectionType.setStatus("current")


class _AcSonetPortRingIdentifier_Type(Integer32):
    """Custom type acSonetPortRingIdentifier based on Integer32"""
    defaultValue = 1


_AcSonetPortRingIdentifier_Object = MibTableColumn
acSonetPortRingIdentifier = _AcSonetPortRingIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 1, 1, 19),
    _AcSonetPortRingIdentifier_Type()
)
acSonetPortRingIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSonetPortRingIdentifier.setStatus("current")


class _AcSonetPortRingName_Type(DisplayString):
    """Custom type acSonetPortRingName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcSonetPortRingName_Type.__name__ = "DisplayString"
_AcSonetPortRingName_Object = MibTableColumn
acSonetPortRingName = _AcSonetPortRingName_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 1, 1, 20),
    _AcSonetPortRingName_Type()
)
acSonetPortRingName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSonetPortRingName.setStatus("current")
_AcSonetThresholdTable_Object = MibTable
acSonetThresholdTable = _AcSonetThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    acSonetThresholdTable.setStatus("current")
_AcSonetThresholdEntry_Object = MibTableRow
acSonetThresholdEntry = _AcSonetThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 2, 1)
)
acSonetThresholdEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetThresholdNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetThresholdSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetThresholdPort"),
)
if mibBuilder.loadTexts:
    acSonetThresholdEntry.setStatus("current")
_AcSonetThresholdNodeId_Type = AcNodeId
_AcSonetThresholdNodeId_Object = MibTableColumn
acSonetThresholdNodeId = _AcSonetThresholdNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 2, 1, 1),
    _AcSonetThresholdNodeId_Type()
)
acSonetThresholdNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetThresholdNodeId.setStatus("current")
_AcSonetThresholdSlot_Type = AcSlotNumber
_AcSonetThresholdSlot_Object = MibTableColumn
acSonetThresholdSlot = _AcSonetThresholdSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 2, 1, 2),
    _AcSonetThresholdSlot_Type()
)
acSonetThresholdSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetThresholdSlot.setStatus("current")
_AcSonetThresholdPort_Type = AcPortNumber
_AcSonetThresholdPort_Object = MibTableColumn
acSonetThresholdPort = _AcSonetThresholdPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 2, 1, 3),
    _AcSonetThresholdPort_Type()
)
acSonetThresholdPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetThresholdPort.setStatus("current")


class _AcSonetThresholdSESSet_Type(Integer32):
    """Custom type acSonetThresholdSESSet based on Integer32"""
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
        *(("ansi93", 3),
          ("ansi97", 5),
          ("bellcore", 2),
          ("itu", 4),
          ("other", 1))
    )


_AcSonetThresholdSESSet_Type.__name__ = "Integer32"
_AcSonetThresholdSESSet_Object = MibTableColumn
acSonetThresholdSESSet = _AcSonetThresholdSESSet_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 2, 1, 4),
    _AcSonetThresholdSESSet_Type()
)
acSonetThresholdSESSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetThresholdSESSet.setStatus("current")
_AcSonetDCCTable_Object = MibTable
acSonetDCCTable = _AcSonetDCCTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 3)
)
if mibBuilder.loadTexts:
    acSonetDCCTable.setStatus("current")
_AcSonetDCCEntry_Object = MibTableRow
acSonetDCCEntry = _AcSonetDCCEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 3, 1)
)
acSonetDCCEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetDCCNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetDCCSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetDCCPort"),
)
if mibBuilder.loadTexts:
    acSonetDCCEntry.setStatus("current")
_AcSonetDCCNodeId_Type = AcNodeId
_AcSonetDCCNodeId_Object = MibTableColumn
acSonetDCCNodeId = _AcSonetDCCNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 3, 1, 1),
    _AcSonetDCCNodeId_Type()
)
acSonetDCCNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetDCCNodeId.setStatus("current")
_AcSonetDCCSlot_Type = AcSlotNumber
_AcSonetDCCSlot_Object = MibTableColumn
acSonetDCCSlot = _AcSonetDCCSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 3, 1, 2),
    _AcSonetDCCSlot_Type()
)
acSonetDCCSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetDCCSlot.setStatus("current")
_AcSonetDCCPort_Type = AcPortNumber
_AcSonetDCCPort_Object = MibTableColumn
acSonetDCCPort = _AcSonetDCCPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 3, 1, 3),
    _AcSonetDCCPort_Type()
)
acSonetDCCPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetDCCPort.setStatus("current")


class _AcSonetDCCSectionEnable_Type(TruthValue):
    """Custom type acSonetDCCSectionEnable based on TruthValue"""


_AcSonetDCCSectionEnable_Object = MibTableColumn
acSonetDCCSectionEnable = _AcSonetDCCSectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 3, 1, 4),
    _AcSonetDCCSectionEnable_Type()
)
acSonetDCCSectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetDCCSectionEnable.setStatus("current")


class _AcSonetDCCLineEnable_Type(TruthValue):
    """Custom type acSonetDCCLineEnable based on TruthValue"""


_AcSonetDCCLineEnable_Object = MibTableColumn
acSonetDCCLineEnable = _AcSonetDCCLineEnable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 3, 1, 5),
    _AcSonetDCCLineEnable_Type()
)
acSonetDCCLineEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetDCCLineEnable.setStatus("current")


class _AcSonetDCCAppianEnable_Type(TruthValue):
    """Custom type acSonetDCCAppianEnable based on TruthValue"""


_AcSonetDCCAppianEnable_Object = MibTableColumn
acSonetDCCAppianEnable = _AcSonetDCCAppianEnable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 3, 1, 6),
    _AcSonetDCCAppianEnable_Type()
)
acSonetDCCAppianEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetDCCAppianEnable.setStatus("current")
_AcSonetDCCSectionFail_Type = TruthValue
_AcSonetDCCSectionFail_Object = MibTableColumn
acSonetDCCSectionFail = _AcSonetDCCSectionFail_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 3, 1, 7),
    _AcSonetDCCSectionFail_Type()
)
acSonetDCCSectionFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetDCCSectionFail.setStatus("current")
_AcSonetDCCLineFail_Type = TruthValue
_AcSonetDCCLineFail_Object = MibTableColumn
acSonetDCCLineFail = _AcSonetDCCLineFail_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 3, 1, 8),
    _AcSonetDCCLineFail_Type()
)
acSonetDCCLineFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetDCCLineFail.setStatus("current")
_AcSonetDCCAppianFail_Type = TruthValue
_AcSonetDCCAppianFail_Object = MibTableColumn
acSonetDCCAppianFail = _AcSonetDCCAppianFail_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 3, 1, 9),
    _AcSonetDCCAppianFail_Type()
)
acSonetDCCAppianFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetDCCAppianFail.setStatus("current")
_AcSonetPortProtectionTable_Object = MibTable
acSonetPortProtectionTable = _AcSonetPortProtectionTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 4)
)
if mibBuilder.loadTexts:
    acSonetPortProtectionTable.setStatus("current")
_AcSonetPortProtectionEntry_Object = MibTableRow
acSonetPortProtectionEntry = _AcSonetPortProtectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 4, 1)
)
acSonetPortProtectionEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPortProtectionNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPortProtectionSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPortProtectionPort"),
)
if mibBuilder.loadTexts:
    acSonetPortProtectionEntry.setStatus("current")
_AcSonetPortProtectionNodeId_Type = AcNodeId
_AcSonetPortProtectionNodeId_Object = MibTableColumn
acSonetPortProtectionNodeId = _AcSonetPortProtectionNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 4, 1, 1),
    _AcSonetPortProtectionNodeId_Type()
)
acSonetPortProtectionNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPortProtectionNodeId.setStatus("current")
_AcSonetPortProtectionSlot_Type = AcSlotNumber
_AcSonetPortProtectionSlot_Object = MibTableColumn
acSonetPortProtectionSlot = _AcSonetPortProtectionSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 4, 1, 2),
    _AcSonetPortProtectionSlot_Type()
)
acSonetPortProtectionSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPortProtectionSlot.setStatus("current")
_AcSonetPortProtectionPort_Type = AcPortNumber
_AcSonetPortProtectionPort_Object = MibTableColumn
acSonetPortProtectionPort = _AcSonetPortProtectionPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 4, 1, 3),
    _AcSonetPortProtectionPort_Type()
)
acSonetPortProtectionPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPortProtectionPort.setStatus("current")


class _AcSonetPortProtectionType_Type(Integer32):
    """Custom type acSonetPortProtectionType based on Integer32"""
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
        *(("east", 4),
          ("match", 5),
          ("protection", 2),
          ("ring", 6),
          ("west", 3),
          ("working", 1))
    )


_AcSonetPortProtectionType_Type.__name__ = "Integer32"
_AcSonetPortProtectionType_Object = MibTableColumn
acSonetPortProtectionType = _AcSonetPortProtectionType_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 4, 1, 4),
    _AcSonetPortProtectionType_Type()
)
acSonetPortProtectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetPortProtectionType.setStatus("current")
_AcSonetSection_ObjectIdentity = ObjectIdentity
acSonetSection = _AcSonetSection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2)
)
_AcSonetSection15MinuteIntervalTable_Object = MibTable
acSonetSection15MinuteIntervalTable = _AcSonetSection15MinuteIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    acSonetSection15MinuteIntervalTable.setStatus("current")
_AcSonetSection15MinuteIntervalEntry_Object = MibTableRow
acSonetSection15MinuteIntervalEntry = _AcSonetSection15MinuteIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 1, 1)
)
acSonetSection15MinuteIntervalEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalPort"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalNumber"),
)
if mibBuilder.loadTexts:
    acSonetSection15MinuteIntervalEntry.setStatus("current")
_AcSonetSection15MinuteIntervalNodeId_Type = AcNodeId
_AcSonetSection15MinuteIntervalNodeId_Object = MibTableColumn
acSonetSection15MinuteIntervalNodeId = _AcSonetSection15MinuteIntervalNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 1, 1, 1),
    _AcSonetSection15MinuteIntervalNodeId_Type()
)
acSonetSection15MinuteIntervalNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetSection15MinuteIntervalNodeId.setStatus("current")
_AcSonetSection15MinuteIntervalSlot_Type = AcSlotNumber
_AcSonetSection15MinuteIntervalSlot_Object = MibTableColumn
acSonetSection15MinuteIntervalSlot = _AcSonetSection15MinuteIntervalSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 1, 1, 2),
    _AcSonetSection15MinuteIntervalSlot_Type()
)
acSonetSection15MinuteIntervalSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetSection15MinuteIntervalSlot.setStatus("current")
_AcSonetSection15MinuteIntervalPort_Type = AcPortNumber
_AcSonetSection15MinuteIntervalPort_Object = MibTableColumn
acSonetSection15MinuteIntervalPort = _AcSonetSection15MinuteIntervalPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 1, 1, 3),
    _AcSonetSection15MinuteIntervalPort_Type()
)
acSonetSection15MinuteIntervalPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetSection15MinuteIntervalPort.setStatus("current")


class _AcSonetSection15MinuteIntervalNumber_Type(Integer32):
    """Custom type acSonetSection15MinuteIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 98),
    )


_AcSonetSection15MinuteIntervalNumber_Type.__name__ = "Integer32"
_AcSonetSection15MinuteIntervalNumber_Object = MibTableColumn
acSonetSection15MinuteIntervalNumber = _AcSonetSection15MinuteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 1, 1, 4),
    _AcSonetSection15MinuteIntervalNumber_Type()
)
acSonetSection15MinuteIntervalNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetSection15MinuteIntervalNumber.setStatus("current")
_AcSonetSection15MinuteIntervalValidStats_Type = TruthValue
_AcSonetSection15MinuteIntervalValidStats_Object = MibTableColumn
acSonetSection15MinuteIntervalValidStats = _AcSonetSection15MinuteIntervalValidStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 1, 1, 5),
    _AcSonetSection15MinuteIntervalValidStats_Type()
)
acSonetSection15MinuteIntervalValidStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetSection15MinuteIntervalValidStats.setStatus("current")


class _AcSonetSection15MinuteIntervalResetStats_Type(TruthValue):
    """Custom type acSonetSection15MinuteIntervalResetStats based on TruthValue"""


_AcSonetSection15MinuteIntervalResetStats_Object = MibTableColumn
acSonetSection15MinuteIntervalResetStats = _AcSonetSection15MinuteIntervalResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 1, 1, 6),
    _AcSonetSection15MinuteIntervalResetStats_Type()
)
acSonetSection15MinuteIntervalResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetSection15MinuteIntervalResetStats.setStatus("current")


class _AcSonetSection15MinuteIntervalStatus_Type(Integer32):
    """Custom type acSonetSection15MinuteIntervalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AcSonetSection15MinuteIntervalStatus_Type.__name__ = "Integer32"
_AcSonetSection15MinuteIntervalStatus_Object = MibTableColumn
acSonetSection15MinuteIntervalStatus = _AcSonetSection15MinuteIntervalStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 1, 1, 7),
    _AcSonetSection15MinuteIntervalStatus_Type()
)
acSonetSection15MinuteIntervalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetSection15MinuteIntervalStatus.setStatus("current")
_AcSonetSection15MinuteIntervalESs_Type = PerfIntervalCount
_AcSonetSection15MinuteIntervalESs_Object = MibTableColumn
acSonetSection15MinuteIntervalESs = _AcSonetSection15MinuteIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 1, 1, 8),
    _AcSonetSection15MinuteIntervalESs_Type()
)
acSonetSection15MinuteIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetSection15MinuteIntervalESs.setStatus("current")
_AcSonetSection15MinuteIntervalSESs_Type = PerfIntervalCount
_AcSonetSection15MinuteIntervalSESs_Object = MibTableColumn
acSonetSection15MinuteIntervalSESs = _AcSonetSection15MinuteIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 1, 1, 9),
    _AcSonetSection15MinuteIntervalSESs_Type()
)
acSonetSection15MinuteIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetSection15MinuteIntervalSESs.setStatus("current")
_AcSonetSection15MinuteIntervalSEFSs_Type = PerfIntervalCount
_AcSonetSection15MinuteIntervalSEFSs_Object = MibTableColumn
acSonetSection15MinuteIntervalSEFSs = _AcSonetSection15MinuteIntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 1, 1, 10),
    _AcSonetSection15MinuteIntervalSEFSs_Type()
)
acSonetSection15MinuteIntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetSection15MinuteIntervalSEFSs.setStatus("current")
_AcSonetSection15MinuteIntervalCVs_Type = PerfIntervalCount
_AcSonetSection15MinuteIntervalCVs_Object = MibTableColumn
acSonetSection15MinuteIntervalCVs = _AcSonetSection15MinuteIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 1, 1, 11),
    _AcSonetSection15MinuteIntervalCVs_Type()
)
acSonetSection15MinuteIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetSection15MinuteIntervalCVs.setStatus("current")
_AcSonetSectionDayIntervalTable_Object = MibTable
acSonetSectionDayIntervalTable = _AcSonetSectionDayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    acSonetSectionDayIntervalTable.setStatus("current")
_AcSonetSectionDayIntervalEntry_Object = MibTableRow
acSonetSectionDayIntervalEntry = _AcSonetSectionDayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 2, 1)
)
acSonetSectionDayIntervalEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalPort"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalNumber"),
)
if mibBuilder.loadTexts:
    acSonetSectionDayIntervalEntry.setStatus("current")
_AcSonetSectionDayIntervalNodeId_Type = AcNodeId
_AcSonetSectionDayIntervalNodeId_Object = MibTableColumn
acSonetSectionDayIntervalNodeId = _AcSonetSectionDayIntervalNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 2, 1, 1),
    _AcSonetSectionDayIntervalNodeId_Type()
)
acSonetSectionDayIntervalNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetSectionDayIntervalNodeId.setStatus("current")
_AcSonetSectionDayIntervalSlot_Type = AcSlotNumber
_AcSonetSectionDayIntervalSlot_Object = MibTableColumn
acSonetSectionDayIntervalSlot = _AcSonetSectionDayIntervalSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 2, 1, 2),
    _AcSonetSectionDayIntervalSlot_Type()
)
acSonetSectionDayIntervalSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetSectionDayIntervalSlot.setStatus("current")
_AcSonetSectionDayIntervalPort_Type = AcPortNumber
_AcSonetSectionDayIntervalPort_Object = MibTableColumn
acSonetSectionDayIntervalPort = _AcSonetSectionDayIntervalPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 2, 1, 3),
    _AcSonetSectionDayIntervalPort_Type()
)
acSonetSectionDayIntervalPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetSectionDayIntervalPort.setStatus("current")


class _AcSonetSectionDayIntervalNumber_Type(Integer32):
    """Custom type acSonetSectionDayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_AcSonetSectionDayIntervalNumber_Type.__name__ = "Integer32"
_AcSonetSectionDayIntervalNumber_Object = MibTableColumn
acSonetSectionDayIntervalNumber = _AcSonetSectionDayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 2, 1, 4),
    _AcSonetSectionDayIntervalNumber_Type()
)
acSonetSectionDayIntervalNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetSectionDayIntervalNumber.setStatus("current")
_AcSonetSectionDayIntervalValidStats_Type = TruthValue
_AcSonetSectionDayIntervalValidStats_Object = MibTableColumn
acSonetSectionDayIntervalValidStats = _AcSonetSectionDayIntervalValidStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 2, 1, 5),
    _AcSonetSectionDayIntervalValidStats_Type()
)
acSonetSectionDayIntervalValidStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetSectionDayIntervalValidStats.setStatus("current")


class _AcSonetSectionDayIntervalResetStats_Type(TruthValue):
    """Custom type acSonetSectionDayIntervalResetStats based on TruthValue"""


_AcSonetSectionDayIntervalResetStats_Object = MibTableColumn
acSonetSectionDayIntervalResetStats = _AcSonetSectionDayIntervalResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 2, 1, 6),
    _AcSonetSectionDayIntervalResetStats_Type()
)
acSonetSectionDayIntervalResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetSectionDayIntervalResetStats.setStatus("current")


class _AcSonetSectionDayIntervalStatus_Type(Integer32):
    """Custom type acSonetSectionDayIntervalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AcSonetSectionDayIntervalStatus_Type.__name__ = "Integer32"
_AcSonetSectionDayIntervalStatus_Object = MibTableColumn
acSonetSectionDayIntervalStatus = _AcSonetSectionDayIntervalStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 2, 1, 7),
    _AcSonetSectionDayIntervalStatus_Type()
)
acSonetSectionDayIntervalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetSectionDayIntervalStatus.setStatus("current")
_AcSonetSectionDayIntervalESs_Type = PerfIntervalCount
_AcSonetSectionDayIntervalESs_Object = MibTableColumn
acSonetSectionDayIntervalESs = _AcSonetSectionDayIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 2, 1, 8),
    _AcSonetSectionDayIntervalESs_Type()
)
acSonetSectionDayIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetSectionDayIntervalESs.setStatus("current")
_AcSonetSectionDayIntervalSESs_Type = PerfIntervalCount
_AcSonetSectionDayIntervalSESs_Object = MibTableColumn
acSonetSectionDayIntervalSESs = _AcSonetSectionDayIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 2, 1, 9),
    _AcSonetSectionDayIntervalSESs_Type()
)
acSonetSectionDayIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetSectionDayIntervalSESs.setStatus("current")
_AcSonetSectionDayIntervalSEFSs_Type = PerfIntervalCount
_AcSonetSectionDayIntervalSEFSs_Object = MibTableColumn
acSonetSectionDayIntervalSEFSs = _AcSonetSectionDayIntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 2, 1, 10),
    _AcSonetSectionDayIntervalSEFSs_Type()
)
acSonetSectionDayIntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetSectionDayIntervalSEFSs.setStatus("current")
_AcSonetSectionDayIntervalCVs_Type = PerfIntervalCount
_AcSonetSectionDayIntervalCVs_Object = MibTableColumn
acSonetSectionDayIntervalCVs = _AcSonetSectionDayIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 2, 1, 11),
    _AcSonetSectionDayIntervalCVs_Type()
)
acSonetSectionDayIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetSectionDayIntervalCVs.setStatus("current")
_AcSonetSectionThresholdTable_Object = MibTable
acSonetSectionThresholdTable = _AcSonetSectionThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 3)
)
if mibBuilder.loadTexts:
    acSonetSectionThresholdTable.setStatus("current")
_AcSonetSectionThresholdEntry_Object = MibTableRow
acSonetSectionThresholdEntry = _AcSonetSectionThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 3, 1)
)
acSonetSectionThresholdEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetSectionThresholdNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetSectionThresholdSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetSectionThresholdPort"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetSectionThresholdSelectionNum"),
)
if mibBuilder.loadTexts:
    acSonetSectionThresholdEntry.setStatus("current")
_AcSonetSectionThresholdNodeId_Type = AcNodeId
_AcSonetSectionThresholdNodeId_Object = MibTableColumn
acSonetSectionThresholdNodeId = _AcSonetSectionThresholdNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 3, 1, 1),
    _AcSonetSectionThresholdNodeId_Type()
)
acSonetSectionThresholdNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetSectionThresholdNodeId.setStatus("current")
_AcSonetSectionThresholdSlot_Type = AcSlotNumber
_AcSonetSectionThresholdSlot_Object = MibTableColumn
acSonetSectionThresholdSlot = _AcSonetSectionThresholdSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 3, 1, 2),
    _AcSonetSectionThresholdSlot_Type()
)
acSonetSectionThresholdSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetSectionThresholdSlot.setStatus("current")
_AcSonetSectionThresholdPort_Type = AcPortNumber
_AcSonetSectionThresholdPort_Object = MibTableColumn
acSonetSectionThresholdPort = _AcSonetSectionThresholdPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 3, 1, 3),
    _AcSonetSectionThresholdPort_Type()
)
acSonetSectionThresholdPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetSectionThresholdPort.setStatus("current")


class _AcSonetSectionThresholdSelectionNum_Type(Integer32):
    """Custom type acSonetSectionThresholdSelectionNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("day", 2),
          ("minute", 1))
    )


_AcSonetSectionThresholdSelectionNum_Type.__name__ = "Integer32"
_AcSonetSectionThresholdSelectionNum_Object = MibTableColumn
acSonetSectionThresholdSelectionNum = _AcSonetSectionThresholdSelectionNum_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 3, 1, 4),
    _AcSonetSectionThresholdSelectionNum_Type()
)
acSonetSectionThresholdSelectionNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetSectionThresholdSelectionNum.setStatus("current")
_AcSonetSectionThresholdAdminStatus_Type = AcAdminStatus
_AcSonetSectionThresholdAdminStatus_Object = MibTableColumn
acSonetSectionThresholdAdminStatus = _AcSonetSectionThresholdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 3, 1, 5),
    _AcSonetSectionThresholdAdminStatus_Type()
)
acSonetSectionThresholdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetSectionThresholdAdminStatus.setStatus("deprecated")


class _AcSonetSectionThresholdESs_Type(Integer32):
    """Custom type acSonetSectionThresholdESs based on Integer32"""
    defaultValue = 0


_AcSonetSectionThresholdESs_Object = MibTableColumn
acSonetSectionThresholdESs = _AcSonetSectionThresholdESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 3, 1, 6),
    _AcSonetSectionThresholdESs_Type()
)
acSonetSectionThresholdESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetSectionThresholdESs.setStatus("current")


class _AcSonetSectionThresholdSESs_Type(Integer32):
    """Custom type acSonetSectionThresholdSESs based on Integer32"""
    defaultValue = 0


_AcSonetSectionThresholdSESs_Object = MibTableColumn
acSonetSectionThresholdSESs = _AcSonetSectionThresholdSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 3, 1, 7),
    _AcSonetSectionThresholdSESs_Type()
)
acSonetSectionThresholdSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetSectionThresholdSESs.setStatus("current")


class _AcSonetSectionThresholdSEFSs_Type(Integer32):
    """Custom type acSonetSectionThresholdSEFSs based on Integer32"""
    defaultValue = 0


_AcSonetSectionThresholdSEFSs_Object = MibTableColumn
acSonetSectionThresholdSEFSs = _AcSonetSectionThresholdSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 3, 1, 8),
    _AcSonetSectionThresholdSEFSs_Type()
)
acSonetSectionThresholdSEFSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetSectionThresholdSEFSs.setStatus("current")


class _AcSonetSectionThresholdCVs_Type(Integer32):
    """Custom type acSonetSectionThresholdCVs based on Integer32"""
    defaultValue = 0


_AcSonetSectionThresholdCVs_Object = MibTableColumn
acSonetSectionThresholdCVs = _AcSonetSectionThresholdCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 3, 1, 9),
    _AcSonetSectionThresholdCVs_Type()
)
acSonetSectionThresholdCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetSectionThresholdCVs.setStatus("current")
_AcSonetSectionTIMTable_Object = MibTable
acSonetSectionTIMTable = _AcSonetSectionTIMTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 4)
)
if mibBuilder.loadTexts:
    acSonetSectionTIMTable.setStatus("current")
_AcSonetSectionTIMEntry_Object = MibTableRow
acSonetSectionTIMEntry = _AcSonetSectionTIMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 4, 1)
)
acSonetSectionTIMEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetSectionTIMNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetSectionTIMSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetSectionTIMPort"),
)
if mibBuilder.loadTexts:
    acSonetSectionTIMEntry.setStatus("current")
_AcSonetSectionTIMNodeId_Type = AcNodeId
_AcSonetSectionTIMNodeId_Object = MibTableColumn
acSonetSectionTIMNodeId = _AcSonetSectionTIMNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 4, 1, 1),
    _AcSonetSectionTIMNodeId_Type()
)
acSonetSectionTIMNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetSectionTIMNodeId.setStatus("current")
_AcSonetSectionTIMSlot_Type = AcSlotNumber
_AcSonetSectionTIMSlot_Object = MibTableColumn
acSonetSectionTIMSlot = _AcSonetSectionTIMSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 4, 1, 2),
    _AcSonetSectionTIMSlot_Type()
)
acSonetSectionTIMSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetSectionTIMSlot.setStatus("current")
_AcSonetSectionTIMPort_Type = AcPortNumber
_AcSonetSectionTIMPort_Object = MibTableColumn
acSonetSectionTIMPort = _AcSonetSectionTIMPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 4, 1, 3),
    _AcSonetSectionTIMPort_Type()
)
acSonetSectionTIMPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetSectionTIMPort.setStatus("current")
_AcSonetSectionTIMGenerateEnable_Type = TruthValue
_AcSonetSectionTIMGenerateEnable_Object = MibTableColumn
acSonetSectionTIMGenerateEnable = _AcSonetSectionTIMGenerateEnable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 4, 1, 4),
    _AcSonetSectionTIMGenerateEnable_Type()
)
acSonetSectionTIMGenerateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetSectionTIMGenerateEnable.setStatus("current")


class _AcSonetSectionTIMDetectEnable_Type(TruthValue):
    """Custom type acSonetSectionTIMDetectEnable based on TruthValue"""


_AcSonetSectionTIMDetectEnable_Object = MibTableColumn
acSonetSectionTIMDetectEnable = _AcSonetSectionTIMDetectEnable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 4, 1, 5),
    _AcSonetSectionTIMDetectEnable_Type()
)
acSonetSectionTIMDetectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetSectionTIMDetectEnable.setStatus("current")
_AcSonetSectionTIMTransmitedString_Type = AcTraceString
_AcSonetSectionTIMTransmitedString_Object = MibTableColumn
acSonetSectionTIMTransmitedString = _AcSonetSectionTIMTransmitedString_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 4, 1, 6),
    _AcSonetSectionTIMTransmitedString_Type()
)
acSonetSectionTIMTransmitedString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetSectionTIMTransmitedString.setStatus("current")
_AcSonetSectionTIMExpectedString_Type = AcTraceString
_AcSonetSectionTIMExpectedString_Object = MibTableColumn
acSonetSectionTIMExpectedString = _AcSonetSectionTIMExpectedString_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 4, 1, 7),
    _AcSonetSectionTIMExpectedString_Type()
)
acSonetSectionTIMExpectedString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetSectionTIMExpectedString.setStatus("current")
_AcSonetSectionTIMReceivedString_Type = AcTraceString
_AcSonetSectionTIMReceivedString_Object = MibTableColumn
acSonetSectionTIMReceivedString = _AcSonetSectionTIMReceivedString_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 4, 1, 8),
    _AcSonetSectionTIMReceivedString_Type()
)
acSonetSectionTIMReceivedString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetSectionTIMReceivedString.setStatus("current")
_AcSonetSectionTIMFailure_Type = TruthValue
_AcSonetSectionTIMFailure_Object = MibTableColumn
acSonetSectionTIMFailure = _AcSonetSectionTIMFailure_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 4, 1, 9),
    _AcSonetSectionTIMFailure_Type()
)
acSonetSectionTIMFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetSectionTIMFailure.setStatus("current")


class _AcSonetSectionTIMFormat_Type(Integer32):
    """Custom type acSonetSectionTIMFormat based on Integer32"""
    defaultValue = 0

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
        *(("t16", 3),
          ("t16-crc7", 5),
          ("t16-msb1", 4),
          ("t64", 1),
          ("t64-crlf", 2),
          ("void", 0))
    )


_AcSonetSectionTIMFormat_Type.__name__ = "Integer32"
_AcSonetSectionTIMFormat_Object = MibTableColumn
acSonetSectionTIMFormat = _AcSonetSectionTIMFormat_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 4, 1, 10),
    _AcSonetSectionTIMFormat_Type()
)
acSonetSectionTIMFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetSectionTIMFormat.setStatus("current")


class _AcSonetSectionTIMMismatchZeros_Type(TruthValue):
    """Custom type acSonetSectionTIMMismatchZeros based on TruthValue"""


_AcSonetSectionTIMMismatchZeros_Object = MibTableColumn
acSonetSectionTIMMismatchZeros = _AcSonetSectionTIMMismatchZeros_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 4, 1, 11),
    _AcSonetSectionTIMMismatchZeros_Type()
)
acSonetSectionTIMMismatchZeros.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetSectionTIMMismatchZeros.setStatus("current")
_AcSonetSectionSSMTable_Object = MibTable
acSonetSectionSSMTable = _AcSonetSectionSSMTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 5)
)
if mibBuilder.loadTexts:
    acSonetSectionSSMTable.setStatus("current")
_AcSonetSectionSSMEntry_Object = MibTableRow
acSonetSectionSSMEntry = _AcSonetSectionSSMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 5, 1)
)
acSonetSectionSSMEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetSectionSSMNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetSectionSSMSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetSectionSSMPort"),
)
if mibBuilder.loadTexts:
    acSonetSectionSSMEntry.setStatus("current")
_AcSonetSectionSSMNodeId_Type = AcNodeId
_AcSonetSectionSSMNodeId_Object = MibTableColumn
acSonetSectionSSMNodeId = _AcSonetSectionSSMNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 5, 1, 1),
    _AcSonetSectionSSMNodeId_Type()
)
acSonetSectionSSMNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetSectionSSMNodeId.setStatus("current")
_AcSonetSectionSSMSlot_Type = AcSlotNumber
_AcSonetSectionSSMSlot_Object = MibTableColumn
acSonetSectionSSMSlot = _AcSonetSectionSSMSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 5, 1, 2),
    _AcSonetSectionSSMSlot_Type()
)
acSonetSectionSSMSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetSectionSSMSlot.setStatus("current")
_AcSonetSectionSSMPort_Type = AcPortNumber
_AcSonetSectionSSMPort_Object = MibTableColumn
acSonetSectionSSMPort = _AcSonetSectionSSMPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 5, 1, 3),
    _AcSonetSectionSSMPort_Type()
)
acSonetSectionSSMPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetSectionSSMPort.setStatus("current")


class _AcSonetSectionSSMDetectEnable_Type(TruthValue):
    """Custom type acSonetSectionSSMDetectEnable based on TruthValue"""


_AcSonetSectionSSMDetectEnable_Object = MibTableColumn
acSonetSectionSSMDetectEnable = _AcSonetSectionSSMDetectEnable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 5, 1, 4),
    _AcSonetSectionSSMDetectEnable_Type()
)
acSonetSectionSSMDetectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetSectionSSMDetectEnable.setStatus("current")


class _AcSonetSectionSSMTransmitedValue_Type(Integer32):
    """Custom type acSonetSectionSSMTransmitedValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcSonetSectionSSMTransmitedValue_Type.__name__ = "Integer32"
_AcSonetSectionSSMTransmitedValue_Object = MibTableColumn
acSonetSectionSSMTransmitedValue = _AcSonetSectionSSMTransmitedValue_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 5, 1, 5),
    _AcSonetSectionSSMTransmitedValue_Type()
)
acSonetSectionSSMTransmitedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetSectionSSMTransmitedValue.setStatus("current")


class _AcSonetSectionSSMReceivedValue_Type(Integer32):
    """Custom type acSonetSectionSSMReceivedValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcSonetSectionSSMReceivedValue_Type.__name__ = "Integer32"
_AcSonetSectionSSMReceivedValue_Object = MibTableColumn
acSonetSectionSSMReceivedValue = _AcSonetSectionSSMReceivedValue_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 5, 1, 6),
    _AcSonetSectionSSMReceivedValue_Type()
)
acSonetSectionSSMReceivedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetSectionSSMReceivedValue.setStatus("current")
_AcSonetLine_ObjectIdentity = ObjectIdentity
acSonetLine = _AcSonetLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3)
)
_AcSonetLine15MinuteIntervalTable_Object = MibTable
acSonetLine15MinuteIntervalTable = _AcSonetLine15MinuteIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    acSonetLine15MinuteIntervalTable.setStatus("current")
_AcSonetLine15MinuteIntervalEntry_Object = MibTableRow
acSonetLine15MinuteIntervalEntry = _AcSonetLine15MinuteIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 1, 1)
)
acSonetLine15MinuteIntervalEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalPort"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalNumber"),
)
if mibBuilder.loadTexts:
    acSonetLine15MinuteIntervalEntry.setStatus("current")
_AcSonetLine15MinuteIntervalNodeId_Type = AcNodeId
_AcSonetLine15MinuteIntervalNodeId_Object = MibTableColumn
acSonetLine15MinuteIntervalNodeId = _AcSonetLine15MinuteIntervalNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 1, 1, 1),
    _AcSonetLine15MinuteIntervalNodeId_Type()
)
acSonetLine15MinuteIntervalNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetLine15MinuteIntervalNodeId.setStatus("current")
_AcSonetLine15MinuteIntervalSlot_Type = AcSlotNumber
_AcSonetLine15MinuteIntervalSlot_Object = MibTableColumn
acSonetLine15MinuteIntervalSlot = _AcSonetLine15MinuteIntervalSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 1, 1, 2),
    _AcSonetLine15MinuteIntervalSlot_Type()
)
acSonetLine15MinuteIntervalSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetLine15MinuteIntervalSlot.setStatus("current")
_AcSonetLine15MinuteIntervalPort_Type = AcPortNumber
_AcSonetLine15MinuteIntervalPort_Object = MibTableColumn
acSonetLine15MinuteIntervalPort = _AcSonetLine15MinuteIntervalPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 1, 1, 3),
    _AcSonetLine15MinuteIntervalPort_Type()
)
acSonetLine15MinuteIntervalPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetLine15MinuteIntervalPort.setStatus("current")


class _AcSonetLine15MinuteIntervalNumber_Type(Integer32):
    """Custom type acSonetLine15MinuteIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 98),
    )


_AcSonetLine15MinuteIntervalNumber_Type.__name__ = "Integer32"
_AcSonetLine15MinuteIntervalNumber_Object = MibTableColumn
acSonetLine15MinuteIntervalNumber = _AcSonetLine15MinuteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 1, 1, 4),
    _AcSonetLine15MinuteIntervalNumber_Type()
)
acSonetLine15MinuteIntervalNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetLine15MinuteIntervalNumber.setStatus("current")
_AcSonetLine15MinuteIntervalValidStats_Type = TruthValue
_AcSonetLine15MinuteIntervalValidStats_Object = MibTableColumn
acSonetLine15MinuteIntervalValidStats = _AcSonetLine15MinuteIntervalValidStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 1, 1, 5),
    _AcSonetLine15MinuteIntervalValidStats_Type()
)
acSonetLine15MinuteIntervalValidStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetLine15MinuteIntervalValidStats.setStatus("current")
_AcSonetLine15MinuteIntervalResetStats_Type = TruthValue
_AcSonetLine15MinuteIntervalResetStats_Object = MibTableColumn
acSonetLine15MinuteIntervalResetStats = _AcSonetLine15MinuteIntervalResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 1, 1, 6),
    _AcSonetLine15MinuteIntervalResetStats_Type()
)
acSonetLine15MinuteIntervalResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetLine15MinuteIntervalResetStats.setStatus("current")


class _AcSonetLine15MinuteIntervalStatus_Type(Integer32):
    """Custom type acSonetLine15MinuteIntervalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AcSonetLine15MinuteIntervalStatus_Type.__name__ = "Integer32"
_AcSonetLine15MinuteIntervalStatus_Object = MibTableColumn
acSonetLine15MinuteIntervalStatus = _AcSonetLine15MinuteIntervalStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 1, 1, 7),
    _AcSonetLine15MinuteIntervalStatus_Type()
)
acSonetLine15MinuteIntervalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetLine15MinuteIntervalStatus.setStatus("current")
_AcSonetLine15MinuteIntervalESs_Type = PerfIntervalCount
_AcSonetLine15MinuteIntervalESs_Object = MibTableColumn
acSonetLine15MinuteIntervalESs = _AcSonetLine15MinuteIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 1, 1, 8),
    _AcSonetLine15MinuteIntervalESs_Type()
)
acSonetLine15MinuteIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetLine15MinuteIntervalESs.setStatus("current")
_AcSonetLine15MinuteIntervalSESs_Type = PerfIntervalCount
_AcSonetLine15MinuteIntervalSESs_Object = MibTableColumn
acSonetLine15MinuteIntervalSESs = _AcSonetLine15MinuteIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 1, 1, 9),
    _AcSonetLine15MinuteIntervalSESs_Type()
)
acSonetLine15MinuteIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetLine15MinuteIntervalSESs.setStatus("current")
_AcSonetLine15MinuteIntervalCVs_Type = PerfIntervalCount
_AcSonetLine15MinuteIntervalCVs_Object = MibTableColumn
acSonetLine15MinuteIntervalCVs = _AcSonetLine15MinuteIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 1, 1, 10),
    _AcSonetLine15MinuteIntervalCVs_Type()
)
acSonetLine15MinuteIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetLine15MinuteIntervalCVs.setStatus("current")
_AcSonetLine15MinuteIntervalUASs_Type = PerfIntervalCount
_AcSonetLine15MinuteIntervalUASs_Object = MibTableColumn
acSonetLine15MinuteIntervalUASs = _AcSonetLine15MinuteIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 1, 1, 11),
    _AcSonetLine15MinuteIntervalUASs_Type()
)
acSonetLine15MinuteIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetLine15MinuteIntervalUASs.setStatus("current")
_AcSonetLine15MinuteIntervalBER_Type = PerfIntervalCount
_AcSonetLine15MinuteIntervalBER_Object = MibTableColumn
acSonetLine15MinuteIntervalBER = _AcSonetLine15MinuteIntervalBER_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 1, 1, 12),
    _AcSonetLine15MinuteIntervalBER_Type()
)
acSonetLine15MinuteIntervalBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetLine15MinuteIntervalBER.setStatus("current")
_AcSonetLineDayIntervalTable_Object = MibTable
acSonetLineDayIntervalTable = _AcSonetLineDayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 2)
)
if mibBuilder.loadTexts:
    acSonetLineDayIntervalTable.setStatus("current")
_AcSonetLineDayIntervalEntry_Object = MibTableRow
acSonetLineDayIntervalEntry = _AcSonetLineDayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 2, 1)
)
acSonetLineDayIntervalEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalPort"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalNumber"),
)
if mibBuilder.loadTexts:
    acSonetLineDayIntervalEntry.setStatus("current")
_AcSonetLineDayIntervalNodeId_Type = AcNodeId
_AcSonetLineDayIntervalNodeId_Object = MibTableColumn
acSonetLineDayIntervalNodeId = _AcSonetLineDayIntervalNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 2, 1, 1),
    _AcSonetLineDayIntervalNodeId_Type()
)
acSonetLineDayIntervalNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetLineDayIntervalNodeId.setStatus("current")
_AcSonetLineDayIntervalSlot_Type = AcSlotNumber
_AcSonetLineDayIntervalSlot_Object = MibTableColumn
acSonetLineDayIntervalSlot = _AcSonetLineDayIntervalSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 2, 1, 2),
    _AcSonetLineDayIntervalSlot_Type()
)
acSonetLineDayIntervalSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetLineDayIntervalSlot.setStatus("current")
_AcSonetLineDayIntervalPort_Type = AcPortNumber
_AcSonetLineDayIntervalPort_Object = MibTableColumn
acSonetLineDayIntervalPort = _AcSonetLineDayIntervalPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 2, 1, 3),
    _AcSonetLineDayIntervalPort_Type()
)
acSonetLineDayIntervalPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetLineDayIntervalPort.setStatus("current")


class _AcSonetLineDayIntervalNumber_Type(Integer32):
    """Custom type acSonetLineDayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_AcSonetLineDayIntervalNumber_Type.__name__ = "Integer32"
_AcSonetLineDayIntervalNumber_Object = MibTableColumn
acSonetLineDayIntervalNumber = _AcSonetLineDayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 2, 1, 4),
    _AcSonetLineDayIntervalNumber_Type()
)
acSonetLineDayIntervalNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetLineDayIntervalNumber.setStatus("current")
_AcSonetLineDayIntervalValidStats_Type = TruthValue
_AcSonetLineDayIntervalValidStats_Object = MibTableColumn
acSonetLineDayIntervalValidStats = _AcSonetLineDayIntervalValidStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 2, 1, 5),
    _AcSonetLineDayIntervalValidStats_Type()
)
acSonetLineDayIntervalValidStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetLineDayIntervalValidStats.setStatus("current")
_AcSonetLineDayIntervalResetStats_Type = TruthValue
_AcSonetLineDayIntervalResetStats_Object = MibTableColumn
acSonetLineDayIntervalResetStats = _AcSonetLineDayIntervalResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 2, 1, 6),
    _AcSonetLineDayIntervalResetStats_Type()
)
acSonetLineDayIntervalResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetLineDayIntervalResetStats.setStatus("current")


class _AcSonetLineDayIntervalStatus_Type(Integer32):
    """Custom type acSonetLineDayIntervalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AcSonetLineDayIntervalStatus_Type.__name__ = "Integer32"
_AcSonetLineDayIntervalStatus_Object = MibTableColumn
acSonetLineDayIntervalStatus = _AcSonetLineDayIntervalStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 2, 1, 7),
    _AcSonetLineDayIntervalStatus_Type()
)
acSonetLineDayIntervalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetLineDayIntervalStatus.setStatus("current")
_AcSonetLineDayIntervalESs_Type = PerfIntervalCount
_AcSonetLineDayIntervalESs_Object = MibTableColumn
acSonetLineDayIntervalESs = _AcSonetLineDayIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 2, 1, 8),
    _AcSonetLineDayIntervalESs_Type()
)
acSonetLineDayIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetLineDayIntervalESs.setStatus("current")
_AcSonetLineDayIntervalSESs_Type = PerfIntervalCount
_AcSonetLineDayIntervalSESs_Object = MibTableColumn
acSonetLineDayIntervalSESs = _AcSonetLineDayIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 2, 1, 9),
    _AcSonetLineDayIntervalSESs_Type()
)
acSonetLineDayIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetLineDayIntervalSESs.setStatus("current")
_AcSonetLineDayIntervalCVs_Type = PerfIntervalCount
_AcSonetLineDayIntervalCVs_Object = MibTableColumn
acSonetLineDayIntervalCVs = _AcSonetLineDayIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 2, 1, 10),
    _AcSonetLineDayIntervalCVs_Type()
)
acSonetLineDayIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetLineDayIntervalCVs.setStatus("current")
_AcSonetLineDayIntervalUASs_Type = PerfIntervalCount
_AcSonetLineDayIntervalUASs_Object = MibTableColumn
acSonetLineDayIntervalUASs = _AcSonetLineDayIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 2, 1, 11),
    _AcSonetLineDayIntervalUASs_Type()
)
acSonetLineDayIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetLineDayIntervalUASs.setStatus("current")
_AcSonetLineDayIntervalBER_Type = PerfIntervalCount
_AcSonetLineDayIntervalBER_Object = MibTableColumn
acSonetLineDayIntervalBER = _AcSonetLineDayIntervalBER_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 2, 1, 12),
    _AcSonetLineDayIntervalBER_Type()
)
acSonetLineDayIntervalBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetLineDayIntervalBER.setStatus("deprecated")
_AcSonetLineThresholdTable_Object = MibTable
acSonetLineThresholdTable = _AcSonetLineThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 3)
)
if mibBuilder.loadTexts:
    acSonetLineThresholdTable.setStatus("current")
_AcSonetLineThresholdEntry_Object = MibTableRow
acSonetLineThresholdEntry = _AcSonetLineThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 3, 1)
)
acSonetLineThresholdEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetLineThresholdNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetLineThresholdSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetLineThresholdPort"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetLineThresholdSelectionNum"),
)
if mibBuilder.loadTexts:
    acSonetLineThresholdEntry.setStatus("current")
_AcSonetLineThresholdNodeId_Type = AcNodeId
_AcSonetLineThresholdNodeId_Object = MibTableColumn
acSonetLineThresholdNodeId = _AcSonetLineThresholdNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 3, 1, 1),
    _AcSonetLineThresholdNodeId_Type()
)
acSonetLineThresholdNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetLineThresholdNodeId.setStatus("current")
_AcSonetLineThresholdSlot_Type = AcSlotNumber
_AcSonetLineThresholdSlot_Object = MibTableColumn
acSonetLineThresholdSlot = _AcSonetLineThresholdSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 3, 1, 2),
    _AcSonetLineThresholdSlot_Type()
)
acSonetLineThresholdSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetLineThresholdSlot.setStatus("current")
_AcSonetLineThresholdPort_Type = AcPortNumber
_AcSonetLineThresholdPort_Object = MibTableColumn
acSonetLineThresholdPort = _AcSonetLineThresholdPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 3, 1, 3),
    _AcSonetLineThresholdPort_Type()
)
acSonetLineThresholdPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetLineThresholdPort.setStatus("current")


class _AcSonetLineThresholdSelectionNum_Type(Integer32):
    """Custom type acSonetLineThresholdSelectionNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("day", 2),
          ("minute", 1))
    )


_AcSonetLineThresholdSelectionNum_Type.__name__ = "Integer32"
_AcSonetLineThresholdSelectionNum_Object = MibTableColumn
acSonetLineThresholdSelectionNum = _AcSonetLineThresholdSelectionNum_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 3, 1, 4),
    _AcSonetLineThresholdSelectionNum_Type()
)
acSonetLineThresholdSelectionNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetLineThresholdSelectionNum.setStatus("current")
_AcSonetLineThresholdAdminStatus_Type = AcAdminStatus
_AcSonetLineThresholdAdminStatus_Object = MibTableColumn
acSonetLineThresholdAdminStatus = _AcSonetLineThresholdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 3, 1, 5),
    _AcSonetLineThresholdAdminStatus_Type()
)
acSonetLineThresholdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetLineThresholdAdminStatus.setStatus("deprecated")


class _AcSonetLineThresholdESs_Type(Integer32):
    """Custom type acSonetLineThresholdESs based on Integer32"""
    defaultValue = 0


_AcSonetLineThresholdESs_Object = MibTableColumn
acSonetLineThresholdESs = _AcSonetLineThresholdESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 3, 1, 6),
    _AcSonetLineThresholdESs_Type()
)
acSonetLineThresholdESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetLineThresholdESs.setStatus("current")


class _AcSonetLineThresholdSESs_Type(Integer32):
    """Custom type acSonetLineThresholdSESs based on Integer32"""
    defaultValue = 0


_AcSonetLineThresholdSESs_Object = MibTableColumn
acSonetLineThresholdSESs = _AcSonetLineThresholdSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 3, 1, 7),
    _AcSonetLineThresholdSESs_Type()
)
acSonetLineThresholdSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetLineThresholdSESs.setStatus("current")


class _AcSonetLineThresholdCVs_Type(Integer32):
    """Custom type acSonetLineThresholdCVs based on Integer32"""
    defaultValue = 0


_AcSonetLineThresholdCVs_Object = MibTableColumn
acSonetLineThresholdCVs = _AcSonetLineThresholdCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 3, 1, 8),
    _AcSonetLineThresholdCVs_Type()
)
acSonetLineThresholdCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetLineThresholdCVs.setStatus("current")


class _AcSonetLineThresholdUASs_Type(Integer32):
    """Custom type acSonetLineThresholdUASs based on Integer32"""
    defaultValue = 0


_AcSonetLineThresholdUASs_Object = MibTableColumn
acSonetLineThresholdUASs = _AcSonetLineThresholdUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 3, 1, 9),
    _AcSonetLineThresholdUASs_Type()
)
acSonetLineThresholdUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetLineThresholdUASs.setStatus("current")
_AcSonetLineProtectionTable_Object = MibTable
acSonetLineProtectionTable = _AcSonetLineProtectionTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 4)
)
if mibBuilder.loadTexts:
    acSonetLineProtectionTable.setStatus("current")
_AcSonetLineProtectionEntry_Object = MibTableRow
acSonetLineProtectionEntry = _AcSonetLineProtectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 4, 1)
)
acSonetLineProtectionEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionPort"),
)
if mibBuilder.loadTexts:
    acSonetLineProtectionEntry.setStatus("current")
_AcSonetLineProtectionNodeId_Type = AcNodeId
_AcSonetLineProtectionNodeId_Object = MibTableColumn
acSonetLineProtectionNodeId = _AcSonetLineProtectionNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 4, 1, 1),
    _AcSonetLineProtectionNodeId_Type()
)
acSonetLineProtectionNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetLineProtectionNodeId.setStatus("current")
_AcSonetLineProtectionSlot_Type = AcSlotNumber
_AcSonetLineProtectionSlot_Object = MibTableColumn
acSonetLineProtectionSlot = _AcSonetLineProtectionSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 4, 1, 2),
    _AcSonetLineProtectionSlot_Type()
)
acSonetLineProtectionSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetLineProtectionSlot.setStatus("current")
_AcSonetLineProtectionPort_Type = AcPortNumber
_AcSonetLineProtectionPort_Object = MibTableColumn
acSonetLineProtectionPort = _AcSonetLineProtectionPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 4, 1, 3),
    _AcSonetLineProtectionPort_Type()
)
acSonetLineProtectionPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetLineProtectionPort.setStatus("current")


class _AcSonetLineProtectionArchitecture_Type(Integer32):
    """Custom type acSonetLineProtectionArchitecture based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("one-plus-one", 2),
          ("one-to-one", 3))
    )


_AcSonetLineProtectionArchitecture_Type.__name__ = "Integer32"
_AcSonetLineProtectionArchitecture_Object = MibTableColumn
acSonetLineProtectionArchitecture = _AcSonetLineProtectionArchitecture_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 4, 1, 4),
    _AcSonetLineProtectionArchitecture_Type()
)
acSonetLineProtectionArchitecture.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetLineProtectionArchitecture.setStatus("current")


class _AcSonetLineProtectionOpMode_Type(Integer32):
    """Custom type acSonetLineProtectionOpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 2),
          ("unidirectional", 1))
    )


_AcSonetLineProtectionOpMode_Type.__name__ = "Integer32"
_AcSonetLineProtectionOpMode_Object = MibTableColumn
acSonetLineProtectionOpMode = _AcSonetLineProtectionOpMode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 4, 1, 5),
    _AcSonetLineProtectionOpMode_Type()
)
acSonetLineProtectionOpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetLineProtectionOpMode.setStatus("current")


class _AcSonetLineProtectionSwitchType_Type(Integer32):
    """Custom type acSonetLineProtectionSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonrevertive", 2),
          ("revertive", 1))
    )


_AcSonetLineProtectionSwitchType_Type.__name__ = "Integer32"
_AcSonetLineProtectionSwitchType_Object = MibTableColumn
acSonetLineProtectionSwitchType = _AcSonetLineProtectionSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 4, 1, 6),
    _AcSonetLineProtectionSwitchType_Type()
)
acSonetLineProtectionSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetLineProtectionSwitchType.setStatus("current")


class _AcSonetLineProtectionSFThreshold_Type(Integer32):
    """Custom type acSonetLineProtectionSFThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 5),
    )


_AcSonetLineProtectionSFThreshold_Type.__name__ = "Integer32"
_AcSonetLineProtectionSFThreshold_Object = MibTableColumn
acSonetLineProtectionSFThreshold = _AcSonetLineProtectionSFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 4, 1, 7),
    _AcSonetLineProtectionSFThreshold_Type()
)
acSonetLineProtectionSFThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetLineProtectionSFThreshold.setStatus("current")


class _AcSonetLineProtectionSDThreshold_Type(Integer32):
    """Custom type acSonetLineProtectionSDThreshold based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 9),
    )


_AcSonetLineProtectionSDThreshold_Type.__name__ = "Integer32"
_AcSonetLineProtectionSDThreshold_Object = MibTableColumn
acSonetLineProtectionSDThreshold = _AcSonetLineProtectionSDThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 4, 1, 8),
    _AcSonetLineProtectionSDThreshold_Type()
)
acSonetLineProtectionSDThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetLineProtectionSDThreshold.setStatus("current")


class _AcSonetLineProtectionActiveTraffic_Type(TruthValue):
    """Custom type acSonetLineProtectionActiveTraffic based on TruthValue"""


_AcSonetLineProtectionActiveTraffic_Object = MibTableColumn
acSonetLineProtectionActiveTraffic = _AcSonetLineProtectionActiveTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 4, 1, 9),
    _AcSonetLineProtectionActiveTraffic_Type()
)
acSonetLineProtectionActiveTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetLineProtectionActiveTraffic.setStatus("current")
_AcSonetLineProtectionProtectionSwitch_Type = TruthValue
_AcSonetLineProtectionProtectionSwitch_Object = MibTableColumn
acSonetLineProtectionProtectionSwitch = _AcSonetLineProtectionProtectionSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 4, 1, 10),
    _AcSonetLineProtectionProtectionSwitch_Type()
)
acSonetLineProtectionProtectionSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetLineProtectionProtectionSwitch.setStatus("current")
_AcSonetLineProtectionFail_Type = TruthValue
_AcSonetLineProtectionFail_Object = MibTableColumn
acSonetLineProtectionFail = _AcSonetLineProtectionFail_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 4, 1, 11),
    _AcSonetLineProtectionFail_Type()
)
acSonetLineProtectionFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetLineProtectionFail.setStatus("current")
_AcSonetLineProtectionChannelMismatchFail_Type = TruthValue
_AcSonetLineProtectionChannelMismatchFail_Object = MibTableColumn
acSonetLineProtectionChannelMismatchFail = _AcSonetLineProtectionChannelMismatchFail_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 4, 1, 12),
    _AcSonetLineProtectionChannelMismatchFail_Type()
)
acSonetLineProtectionChannelMismatchFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetLineProtectionChannelMismatchFail.setStatus("current")
_AcSonetLineProtectionModeMismatchFail_Type = TruthValue
_AcSonetLineProtectionModeMismatchFail_Object = MibTableColumn
acSonetLineProtectionModeMismatchFail = _AcSonetLineProtectionModeMismatchFail_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 4, 1, 13),
    _AcSonetLineProtectionModeMismatchFail_Type()
)
acSonetLineProtectionModeMismatchFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetLineProtectionModeMismatchFail.setStatus("current")
_AcSonetLineProtectionFarEndLineFail_Type = TruthValue
_AcSonetLineProtectionFarEndLineFail_Object = MibTableColumn
acSonetLineProtectionFarEndLineFail = _AcSonetLineProtectionFarEndLineFail_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 4, 1, 14),
    _AcSonetLineProtectionFarEndLineFail_Type()
)
acSonetLineProtectionFarEndLineFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetLineProtectionFarEndLineFail.setStatus("current")


class _AcSonetLineProtectionWTRTime_Type(Integer32):
    """Custom type acSonetLineProtectionWTRTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 720),
    )


_AcSonetLineProtectionWTRTime_Type.__name__ = "Integer32"
_AcSonetLineProtectionWTRTime_Object = MibTableColumn
acSonetLineProtectionWTRTime = _AcSonetLineProtectionWTRTime_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 4, 1, 15),
    _AcSonetLineProtectionWTRTime_Type()
)
acSonetLineProtectionWTRTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetLineProtectionWTRTime.setStatus("current")


class _AcSonetLineProtectionManCommand_Type(Integer32):
    """Custom type acSonetLineProtectionManCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("clear-lockout-working", 9),
          ("exercise", 7),
          ("force-protection", 4),
          ("force-working", 3),
          ("lockout-protection", 2),
          ("lockout-working", 8),
          ("manual-protection", 6),
          ("manual-working", 5))
    )


_AcSonetLineProtectionManCommand_Type.__name__ = "Integer32"
_AcSonetLineProtectionManCommand_Object = MibTableColumn
acSonetLineProtectionManCommand = _AcSonetLineProtectionManCommand_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 4, 1, 16),
    _AcSonetLineProtectionManCommand_Type()
)
acSonetLineProtectionManCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetLineProtectionManCommand.setStatus("current")
_AcSonetFarEndLine_ObjectIdentity = ObjectIdentity
acSonetFarEndLine = _AcSonetFarEndLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4)
)
_AcSonetFarEndLine15MinuteIntervalTable_Object = MibTable
acSonetFarEndLine15MinuteIntervalTable = _AcSonetFarEndLine15MinuteIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 1)
)
if mibBuilder.loadTexts:
    acSonetFarEndLine15MinuteIntervalTable.setStatus("current")
_AcSonetFarEndLine15MinuteIntervalEntry_Object = MibTableRow
acSonetFarEndLine15MinuteIntervalEntry = _AcSonetFarEndLine15MinuteIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 1, 1)
)
acSonetFarEndLine15MinuteIntervalEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalPort"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalNumber"),
)
if mibBuilder.loadTexts:
    acSonetFarEndLine15MinuteIntervalEntry.setStatus("current")
_AcSonetFarEndLine15MinuteIntervalNodeId_Type = AcNodeId
_AcSonetFarEndLine15MinuteIntervalNodeId_Object = MibTableColumn
acSonetFarEndLine15MinuteIntervalNodeId = _AcSonetFarEndLine15MinuteIntervalNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 1, 1, 1),
    _AcSonetFarEndLine15MinuteIntervalNodeId_Type()
)
acSonetFarEndLine15MinuteIntervalNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndLine15MinuteIntervalNodeId.setStatus("current")
_AcSonetFarEndLine15MinuteIntervalSlot_Type = AcSlotNumber
_AcSonetFarEndLine15MinuteIntervalSlot_Object = MibTableColumn
acSonetFarEndLine15MinuteIntervalSlot = _AcSonetFarEndLine15MinuteIntervalSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 1, 1, 2),
    _AcSonetFarEndLine15MinuteIntervalSlot_Type()
)
acSonetFarEndLine15MinuteIntervalSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndLine15MinuteIntervalSlot.setStatus("current")
_AcSonetFarEndLine15MinuteIntervalPort_Type = AcPortNumber
_AcSonetFarEndLine15MinuteIntervalPort_Object = MibTableColumn
acSonetFarEndLine15MinuteIntervalPort = _AcSonetFarEndLine15MinuteIntervalPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 1, 1, 3),
    _AcSonetFarEndLine15MinuteIntervalPort_Type()
)
acSonetFarEndLine15MinuteIntervalPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndLine15MinuteIntervalPort.setStatus("current")


class _AcSonetFarEndLine15MinuteIntervalNumber_Type(Integer32):
    """Custom type acSonetFarEndLine15MinuteIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 98),
    )


_AcSonetFarEndLine15MinuteIntervalNumber_Type.__name__ = "Integer32"
_AcSonetFarEndLine15MinuteIntervalNumber_Object = MibTableColumn
acSonetFarEndLine15MinuteIntervalNumber = _AcSonetFarEndLine15MinuteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 1, 1, 4),
    _AcSonetFarEndLine15MinuteIntervalNumber_Type()
)
acSonetFarEndLine15MinuteIntervalNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndLine15MinuteIntervalNumber.setStatus("current")
_AcSonetFarEndLine15MinuteIntervalValidStats_Type = TruthValue
_AcSonetFarEndLine15MinuteIntervalValidStats_Object = MibTableColumn
acSonetFarEndLine15MinuteIntervalValidStats = _AcSonetFarEndLine15MinuteIntervalValidStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 1, 1, 5),
    _AcSonetFarEndLine15MinuteIntervalValidStats_Type()
)
acSonetFarEndLine15MinuteIntervalValidStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetFarEndLine15MinuteIntervalValidStats.setStatus("current")
_AcSonetFarEndLine15MinuteIntervalResetStats_Type = TruthValue
_AcSonetFarEndLine15MinuteIntervalResetStats_Object = MibTableColumn
acSonetFarEndLine15MinuteIntervalResetStats = _AcSonetFarEndLine15MinuteIntervalResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 1, 1, 6),
    _AcSonetFarEndLine15MinuteIntervalResetStats_Type()
)
acSonetFarEndLine15MinuteIntervalResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetFarEndLine15MinuteIntervalResetStats.setStatus("current")
_AcSonetFarEndLine15MinuteIntervalESs_Type = PerfIntervalCount
_AcSonetFarEndLine15MinuteIntervalESs_Object = MibTableColumn
acSonetFarEndLine15MinuteIntervalESs = _AcSonetFarEndLine15MinuteIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 1, 1, 7),
    _AcSonetFarEndLine15MinuteIntervalESs_Type()
)
acSonetFarEndLine15MinuteIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetFarEndLine15MinuteIntervalESs.setStatus("current")
_AcSonetFarEndLine15MinuteIntervalSESs_Type = PerfIntervalCount
_AcSonetFarEndLine15MinuteIntervalSESs_Object = MibTableColumn
acSonetFarEndLine15MinuteIntervalSESs = _AcSonetFarEndLine15MinuteIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 1, 1, 8),
    _AcSonetFarEndLine15MinuteIntervalSESs_Type()
)
acSonetFarEndLine15MinuteIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetFarEndLine15MinuteIntervalSESs.setStatus("current")
_AcSonetFarEndLine15MinuteIntervalCVs_Type = PerfIntervalCount
_AcSonetFarEndLine15MinuteIntervalCVs_Object = MibTableColumn
acSonetFarEndLine15MinuteIntervalCVs = _AcSonetFarEndLine15MinuteIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 1, 1, 9),
    _AcSonetFarEndLine15MinuteIntervalCVs_Type()
)
acSonetFarEndLine15MinuteIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetFarEndLine15MinuteIntervalCVs.setStatus("current")
_AcSonetFarEndLine15MinuteIntervalUASs_Type = PerfIntervalCount
_AcSonetFarEndLine15MinuteIntervalUASs_Object = MibTableColumn
acSonetFarEndLine15MinuteIntervalUASs = _AcSonetFarEndLine15MinuteIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 1, 1, 10),
    _AcSonetFarEndLine15MinuteIntervalUASs_Type()
)
acSonetFarEndLine15MinuteIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetFarEndLine15MinuteIntervalUASs.setStatus("current")
_AcSonetFarEndLineDayIntervalTable_Object = MibTable
acSonetFarEndLineDayIntervalTable = _AcSonetFarEndLineDayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 2)
)
if mibBuilder.loadTexts:
    acSonetFarEndLineDayIntervalTable.setStatus("current")
_AcSonetFarEndLineDayIntervalEntry_Object = MibTableRow
acSonetFarEndLineDayIntervalEntry = _AcSonetFarEndLineDayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 2, 1)
)
acSonetFarEndLineDayIntervalEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalPort"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalNumber"),
)
if mibBuilder.loadTexts:
    acSonetFarEndLineDayIntervalEntry.setStatus("current")
_AcSonetFarEndLineDayIntervalNodeId_Type = AcNodeId
_AcSonetFarEndLineDayIntervalNodeId_Object = MibTableColumn
acSonetFarEndLineDayIntervalNodeId = _AcSonetFarEndLineDayIntervalNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 2, 1, 1),
    _AcSonetFarEndLineDayIntervalNodeId_Type()
)
acSonetFarEndLineDayIntervalNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndLineDayIntervalNodeId.setStatus("current")
_AcSonetFarEndLineDayIntervalSlot_Type = AcSlotNumber
_AcSonetFarEndLineDayIntervalSlot_Object = MibTableColumn
acSonetFarEndLineDayIntervalSlot = _AcSonetFarEndLineDayIntervalSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 2, 1, 2),
    _AcSonetFarEndLineDayIntervalSlot_Type()
)
acSonetFarEndLineDayIntervalSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndLineDayIntervalSlot.setStatus("current")
_AcSonetFarEndLineDayIntervalPort_Type = AcPortNumber
_AcSonetFarEndLineDayIntervalPort_Object = MibTableColumn
acSonetFarEndLineDayIntervalPort = _AcSonetFarEndLineDayIntervalPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 2, 1, 3),
    _AcSonetFarEndLineDayIntervalPort_Type()
)
acSonetFarEndLineDayIntervalPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndLineDayIntervalPort.setStatus("current")


class _AcSonetFarEndLineDayIntervalNumber_Type(Integer32):
    """Custom type acSonetFarEndLineDayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_AcSonetFarEndLineDayIntervalNumber_Type.__name__ = "Integer32"
_AcSonetFarEndLineDayIntervalNumber_Object = MibTableColumn
acSonetFarEndLineDayIntervalNumber = _AcSonetFarEndLineDayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 2, 1, 4),
    _AcSonetFarEndLineDayIntervalNumber_Type()
)
acSonetFarEndLineDayIntervalNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndLineDayIntervalNumber.setStatus("current")
_AcSonetFarEndLineDayIntervalValidStats_Type = TruthValue
_AcSonetFarEndLineDayIntervalValidStats_Object = MibTableColumn
acSonetFarEndLineDayIntervalValidStats = _AcSonetFarEndLineDayIntervalValidStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 2, 1, 5),
    _AcSonetFarEndLineDayIntervalValidStats_Type()
)
acSonetFarEndLineDayIntervalValidStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetFarEndLineDayIntervalValidStats.setStatus("current")
_AcSonetFarEndLineDayIntervalResetStats_Type = TruthValue
_AcSonetFarEndLineDayIntervalResetStats_Object = MibTableColumn
acSonetFarEndLineDayIntervalResetStats = _AcSonetFarEndLineDayIntervalResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 2, 1, 6),
    _AcSonetFarEndLineDayIntervalResetStats_Type()
)
acSonetFarEndLineDayIntervalResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetFarEndLineDayIntervalResetStats.setStatus("current")
_AcSonetFarEndLineDayIntervalESs_Type = PerfIntervalCount
_AcSonetFarEndLineDayIntervalESs_Object = MibTableColumn
acSonetFarEndLineDayIntervalESs = _AcSonetFarEndLineDayIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 2, 1, 7),
    _AcSonetFarEndLineDayIntervalESs_Type()
)
acSonetFarEndLineDayIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetFarEndLineDayIntervalESs.setStatus("current")
_AcSonetFarEndLineDayIntervalSESs_Type = PerfIntervalCount
_AcSonetFarEndLineDayIntervalSESs_Object = MibTableColumn
acSonetFarEndLineDayIntervalSESs = _AcSonetFarEndLineDayIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 2, 1, 8),
    _AcSonetFarEndLineDayIntervalSESs_Type()
)
acSonetFarEndLineDayIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetFarEndLineDayIntervalSESs.setStatus("current")
_AcSonetFarEndLineDayIntervalCVs_Type = PerfIntervalCount
_AcSonetFarEndLineDayIntervalCVs_Object = MibTableColumn
acSonetFarEndLineDayIntervalCVs = _AcSonetFarEndLineDayIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 2, 1, 9),
    _AcSonetFarEndLineDayIntervalCVs_Type()
)
acSonetFarEndLineDayIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetFarEndLineDayIntervalCVs.setStatus("current")
_AcSonetFarEndLineDayIntervalUASs_Type = PerfIntervalCount
_AcSonetFarEndLineDayIntervalUASs_Object = MibTableColumn
acSonetFarEndLineDayIntervalUASs = _AcSonetFarEndLineDayIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 2, 1, 10),
    _AcSonetFarEndLineDayIntervalUASs_Type()
)
acSonetFarEndLineDayIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetFarEndLineDayIntervalUASs.setStatus("current")
_AcSonetFarEndLineThresholdTable_Object = MibTable
acSonetFarEndLineThresholdTable = _AcSonetFarEndLineThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 3)
)
if mibBuilder.loadTexts:
    acSonetFarEndLineThresholdTable.setStatus("current")
_AcSonetFarEndLineThresholdEntry_Object = MibTableRow
acSonetFarEndLineThresholdEntry = _AcSonetFarEndLineThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 3, 1)
)
acSonetFarEndLineThresholdEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineThresholdNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineThresholdSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineThresholdPort"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineThresholdSelectionNum"),
)
if mibBuilder.loadTexts:
    acSonetFarEndLineThresholdEntry.setStatus("current")
_AcSonetFarEndLineThresholdNodeId_Type = AcNodeId
_AcSonetFarEndLineThresholdNodeId_Object = MibTableColumn
acSonetFarEndLineThresholdNodeId = _AcSonetFarEndLineThresholdNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 3, 1, 1),
    _AcSonetFarEndLineThresholdNodeId_Type()
)
acSonetFarEndLineThresholdNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndLineThresholdNodeId.setStatus("current")
_AcSonetFarEndLineThresholdSlot_Type = AcSlotNumber
_AcSonetFarEndLineThresholdSlot_Object = MibTableColumn
acSonetFarEndLineThresholdSlot = _AcSonetFarEndLineThresholdSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 3, 1, 2),
    _AcSonetFarEndLineThresholdSlot_Type()
)
acSonetFarEndLineThresholdSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndLineThresholdSlot.setStatus("current")
_AcSonetFarEndLineThresholdPort_Type = AcPortNumber
_AcSonetFarEndLineThresholdPort_Object = MibTableColumn
acSonetFarEndLineThresholdPort = _AcSonetFarEndLineThresholdPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 3, 1, 3),
    _AcSonetFarEndLineThresholdPort_Type()
)
acSonetFarEndLineThresholdPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndLineThresholdPort.setStatus("current")


class _AcSonetFarEndLineThresholdSelectionNum_Type(Integer32):
    """Custom type acSonetFarEndLineThresholdSelectionNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("day", 2),
          ("minute", 1))
    )


_AcSonetFarEndLineThresholdSelectionNum_Type.__name__ = "Integer32"
_AcSonetFarEndLineThresholdSelectionNum_Object = MibTableColumn
acSonetFarEndLineThresholdSelectionNum = _AcSonetFarEndLineThresholdSelectionNum_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 3, 1, 4),
    _AcSonetFarEndLineThresholdSelectionNum_Type()
)
acSonetFarEndLineThresholdSelectionNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndLineThresholdSelectionNum.setStatus("current")
_AcSonetFarEndLineThresholdAdminStatus_Type = AcAdminStatus
_AcSonetFarEndLineThresholdAdminStatus_Object = MibTableColumn
acSonetFarEndLineThresholdAdminStatus = _AcSonetFarEndLineThresholdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 3, 1, 5),
    _AcSonetFarEndLineThresholdAdminStatus_Type()
)
acSonetFarEndLineThresholdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetFarEndLineThresholdAdminStatus.setStatus("deprecated")


class _AcSonetFarEndLineThresholdESs_Type(Integer32):
    """Custom type acSonetFarEndLineThresholdESs based on Integer32"""
    defaultValue = 0


_AcSonetFarEndLineThresholdESs_Object = MibTableColumn
acSonetFarEndLineThresholdESs = _AcSonetFarEndLineThresholdESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 3, 1, 6),
    _AcSonetFarEndLineThresholdESs_Type()
)
acSonetFarEndLineThresholdESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetFarEndLineThresholdESs.setStatus("current")


class _AcSonetFarEndLineThresholdSESs_Type(Integer32):
    """Custom type acSonetFarEndLineThresholdSESs based on Integer32"""
    defaultValue = 0


_AcSonetFarEndLineThresholdSESs_Object = MibTableColumn
acSonetFarEndLineThresholdSESs = _AcSonetFarEndLineThresholdSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 3, 1, 7),
    _AcSonetFarEndLineThresholdSESs_Type()
)
acSonetFarEndLineThresholdSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetFarEndLineThresholdSESs.setStatus("current")


class _AcSonetFarEndLineThresholdCVs_Type(Integer32):
    """Custom type acSonetFarEndLineThresholdCVs based on Integer32"""
    defaultValue = 0


_AcSonetFarEndLineThresholdCVs_Object = MibTableColumn
acSonetFarEndLineThresholdCVs = _AcSonetFarEndLineThresholdCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 3, 1, 8),
    _AcSonetFarEndLineThresholdCVs_Type()
)
acSonetFarEndLineThresholdCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetFarEndLineThresholdCVs.setStatus("current")


class _AcSonetFarEndLineThresholdUASs_Type(Integer32):
    """Custom type acSonetFarEndLineThresholdUASs based on Integer32"""
    defaultValue = 0


_AcSonetFarEndLineThresholdUASs_Object = MibTableColumn
acSonetFarEndLineThresholdUASs = _AcSonetFarEndLineThresholdUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 3, 1, 9),
    _AcSonetFarEndLineThresholdUASs_Type()
)
acSonetFarEndLineThresholdUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetFarEndLineThresholdUASs.setStatus("current")
_AcSonetObjectsPath_ObjectIdentity = ObjectIdentity
acSonetObjectsPath = _AcSonetObjectsPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2)
)
_AcSonetPath_ObjectIdentity = ObjectIdentity
acSonetPath = _AcSonetPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1)
)
_AcSonetPath15MinuteIntervalTable_Object = MibTable
acSonetPath15MinuteIntervalTable = _AcSonetPath15MinuteIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    acSonetPath15MinuteIntervalTable.setStatus("current")
_AcSonetPath15MinuteIntervalEntry_Object = MibTableRow
acSonetPath15MinuteIntervalEntry = _AcSonetPath15MinuteIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 1, 1)
)
acSonetPath15MinuteIntervalEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPort"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPath"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNumber"),
)
if mibBuilder.loadTexts:
    acSonetPath15MinuteIntervalEntry.setStatus("current")
_AcSonetPath15MinuteIntervalNodeId_Type = AcNodeId
_AcSonetPath15MinuteIntervalNodeId_Object = MibTableColumn
acSonetPath15MinuteIntervalNodeId = _AcSonetPath15MinuteIntervalNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 1, 1, 1),
    _AcSonetPath15MinuteIntervalNodeId_Type()
)
acSonetPath15MinuteIntervalNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPath15MinuteIntervalNodeId.setStatus("current")
_AcSonetPath15MinuteIntervalSlot_Type = AcSlotNumber
_AcSonetPath15MinuteIntervalSlot_Object = MibTableColumn
acSonetPath15MinuteIntervalSlot = _AcSonetPath15MinuteIntervalSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 1, 1, 2),
    _AcSonetPath15MinuteIntervalSlot_Type()
)
acSonetPath15MinuteIntervalSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPath15MinuteIntervalSlot.setStatus("current")
_AcSonetPath15MinuteIntervalPort_Type = AcPortNumber
_AcSonetPath15MinuteIntervalPort_Object = MibTableColumn
acSonetPath15MinuteIntervalPort = _AcSonetPath15MinuteIntervalPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 1, 1, 3),
    _AcSonetPath15MinuteIntervalPort_Type()
)
acSonetPath15MinuteIntervalPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPath15MinuteIntervalPort.setStatus("current")
_AcSonetPath15MinuteIntervalPath_Type = Integer32
_AcSonetPath15MinuteIntervalPath_Object = MibTableColumn
acSonetPath15MinuteIntervalPath = _AcSonetPath15MinuteIntervalPath_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 1, 1, 4),
    _AcSonetPath15MinuteIntervalPath_Type()
)
acSonetPath15MinuteIntervalPath.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPath15MinuteIntervalPath.setStatus("current")


class _AcSonetPath15MinuteIntervalNumber_Type(Integer32):
    """Custom type acSonetPath15MinuteIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 98),
    )


_AcSonetPath15MinuteIntervalNumber_Type.__name__ = "Integer32"
_AcSonetPath15MinuteIntervalNumber_Object = MibTableColumn
acSonetPath15MinuteIntervalNumber = _AcSonetPath15MinuteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 1, 1, 5),
    _AcSonetPath15MinuteIntervalNumber_Type()
)
acSonetPath15MinuteIntervalNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPath15MinuteIntervalNumber.setStatus("current")


class _AcSonetPath15MinuteIntervalStatus_Type(Integer32):
    """Custom type acSonetPath15MinuteIntervalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 62),
    )


_AcSonetPath15MinuteIntervalStatus_Type.__name__ = "Integer32"
_AcSonetPath15MinuteIntervalStatus_Object = MibTableColumn
acSonetPath15MinuteIntervalStatus = _AcSonetPath15MinuteIntervalStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 1, 1, 6),
    _AcSonetPath15MinuteIntervalStatus_Type()
)
acSonetPath15MinuteIntervalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetPath15MinuteIntervalStatus.setStatus("current")
_AcSonetPath15MinuteIntervalValidStats_Type = TruthValue
_AcSonetPath15MinuteIntervalValidStats_Object = MibTableColumn
acSonetPath15MinuteIntervalValidStats = _AcSonetPath15MinuteIntervalValidStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 1, 1, 7),
    _AcSonetPath15MinuteIntervalValidStats_Type()
)
acSonetPath15MinuteIntervalValidStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetPath15MinuteIntervalValidStats.setStatus("current")
_AcSonetPath15MinuteIntervalResetStats_Type = TruthValue
_AcSonetPath15MinuteIntervalResetStats_Object = MibTableColumn
acSonetPath15MinuteIntervalResetStats = _AcSonetPath15MinuteIntervalResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 1, 1, 8),
    _AcSonetPath15MinuteIntervalResetStats_Type()
)
acSonetPath15MinuteIntervalResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetPath15MinuteIntervalResetStats.setStatus("current")
_AcSonetPath15MinuteIntervalESs_Type = PerfIntervalCount
_AcSonetPath15MinuteIntervalESs_Object = MibTableColumn
acSonetPath15MinuteIntervalESs = _AcSonetPath15MinuteIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 1, 1, 9),
    _AcSonetPath15MinuteIntervalESs_Type()
)
acSonetPath15MinuteIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetPath15MinuteIntervalESs.setStatus("current")
_AcSonetPath15MinuteIntervalSESs_Type = PerfIntervalCount
_AcSonetPath15MinuteIntervalSESs_Object = MibTableColumn
acSonetPath15MinuteIntervalSESs = _AcSonetPath15MinuteIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 1, 1, 10),
    _AcSonetPath15MinuteIntervalSESs_Type()
)
acSonetPath15MinuteIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetPath15MinuteIntervalSESs.setStatus("current")
_AcSonetPath15MinuteIntervalCVs_Type = PerfIntervalCount
_AcSonetPath15MinuteIntervalCVs_Object = MibTableColumn
acSonetPath15MinuteIntervalCVs = _AcSonetPath15MinuteIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 1, 1, 11),
    _AcSonetPath15MinuteIntervalCVs_Type()
)
acSonetPath15MinuteIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetPath15MinuteIntervalCVs.setStatus("current")
_AcSonetPath15MinuteIntervalUASs_Type = PerfIntervalCount
_AcSonetPath15MinuteIntervalUASs_Object = MibTableColumn
acSonetPath15MinuteIntervalUASs = _AcSonetPath15MinuteIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 1, 1, 12),
    _AcSonetPath15MinuteIntervalUASs_Type()
)
acSonetPath15MinuteIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetPath15MinuteIntervalUASs.setStatus("current")
_AcSonetPath15MinuteIntervalBER_Type = PerfIntervalCount
_AcSonetPath15MinuteIntervalBER_Object = MibTableColumn
acSonetPath15MinuteIntervalBER = _AcSonetPath15MinuteIntervalBER_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 1, 1, 13),
    _AcSonetPath15MinuteIntervalBER_Type()
)
acSonetPath15MinuteIntervalBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetPath15MinuteIntervalBER.setStatus("current")
_AcSonetPathDayIntervalTable_Object = MibTable
acSonetPathDayIntervalTable = _AcSonetPathDayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 2)
)
if mibBuilder.loadTexts:
    acSonetPathDayIntervalTable.setStatus("current")
_AcSonetPathDayIntervalEntry_Object = MibTableRow
acSonetPathDayIntervalEntry = _AcSonetPathDayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 2, 1)
)
acSonetPathDayIntervalEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalPort"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalPath"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalNumber"),
)
if mibBuilder.loadTexts:
    acSonetPathDayIntervalEntry.setStatus("current")
_AcSonetPathDayIntervalNodeId_Type = AcNodeId
_AcSonetPathDayIntervalNodeId_Object = MibTableColumn
acSonetPathDayIntervalNodeId = _AcSonetPathDayIntervalNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 2, 1, 1),
    _AcSonetPathDayIntervalNodeId_Type()
)
acSonetPathDayIntervalNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPathDayIntervalNodeId.setStatus("current")
_AcSonetPathDayIntervalSlot_Type = AcSlotNumber
_AcSonetPathDayIntervalSlot_Object = MibTableColumn
acSonetPathDayIntervalSlot = _AcSonetPathDayIntervalSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 2, 1, 2),
    _AcSonetPathDayIntervalSlot_Type()
)
acSonetPathDayIntervalSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPathDayIntervalSlot.setStatus("current")
_AcSonetPathDayIntervalPort_Type = AcPortNumber
_AcSonetPathDayIntervalPort_Object = MibTableColumn
acSonetPathDayIntervalPort = _AcSonetPathDayIntervalPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 2, 1, 3),
    _AcSonetPathDayIntervalPort_Type()
)
acSonetPathDayIntervalPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPathDayIntervalPort.setStatus("current")
_AcSonetPathDayIntervalPath_Type = Integer32
_AcSonetPathDayIntervalPath_Object = MibTableColumn
acSonetPathDayIntervalPath = _AcSonetPathDayIntervalPath_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 2, 1, 4),
    _AcSonetPathDayIntervalPath_Type()
)
acSonetPathDayIntervalPath.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPathDayIntervalPath.setStatus("current")


class _AcSonetPathDayIntervalNumber_Type(Integer32):
    """Custom type acSonetPathDayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_AcSonetPathDayIntervalNumber_Type.__name__ = "Integer32"
_AcSonetPathDayIntervalNumber_Object = MibTableColumn
acSonetPathDayIntervalNumber = _AcSonetPathDayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 2, 1, 5),
    _AcSonetPathDayIntervalNumber_Type()
)
acSonetPathDayIntervalNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPathDayIntervalNumber.setStatus("current")


class _AcSonetPathDayIntervalStatus_Type(Integer32):
    """Custom type acSonetPathDayIntervalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 62),
    )


_AcSonetPathDayIntervalStatus_Type.__name__ = "Integer32"
_AcSonetPathDayIntervalStatus_Object = MibTableColumn
acSonetPathDayIntervalStatus = _AcSonetPathDayIntervalStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 2, 1, 6),
    _AcSonetPathDayIntervalStatus_Type()
)
acSonetPathDayIntervalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetPathDayIntervalStatus.setStatus("current")
_AcSonetPathDayIntervalValidStats_Type = TruthValue
_AcSonetPathDayIntervalValidStats_Object = MibTableColumn
acSonetPathDayIntervalValidStats = _AcSonetPathDayIntervalValidStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 2, 1, 7),
    _AcSonetPathDayIntervalValidStats_Type()
)
acSonetPathDayIntervalValidStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetPathDayIntervalValidStats.setStatus("current")
_AcSonetPathDayIntervalResetStats_Type = TruthValue
_AcSonetPathDayIntervalResetStats_Object = MibTableColumn
acSonetPathDayIntervalResetStats = _AcSonetPathDayIntervalResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 2, 1, 8),
    _AcSonetPathDayIntervalResetStats_Type()
)
acSonetPathDayIntervalResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetPathDayIntervalResetStats.setStatus("current")
_AcSonetPathDayIntervalESs_Type = PerfIntervalCount
_AcSonetPathDayIntervalESs_Object = MibTableColumn
acSonetPathDayIntervalESs = _AcSonetPathDayIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 2, 1, 9),
    _AcSonetPathDayIntervalESs_Type()
)
acSonetPathDayIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetPathDayIntervalESs.setStatus("current")
_AcSonetPathDayIntervalSESs_Type = PerfIntervalCount
_AcSonetPathDayIntervalSESs_Object = MibTableColumn
acSonetPathDayIntervalSESs = _AcSonetPathDayIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 2, 1, 10),
    _AcSonetPathDayIntervalSESs_Type()
)
acSonetPathDayIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetPathDayIntervalSESs.setStatus("current")
_AcSonetPathDayIntervalCVs_Type = PerfIntervalCount
_AcSonetPathDayIntervalCVs_Object = MibTableColumn
acSonetPathDayIntervalCVs = _AcSonetPathDayIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 2, 1, 11),
    _AcSonetPathDayIntervalCVs_Type()
)
acSonetPathDayIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetPathDayIntervalCVs.setStatus("current")
_AcSonetPathDayIntervalUASs_Type = PerfIntervalCount
_AcSonetPathDayIntervalUASs_Object = MibTableColumn
acSonetPathDayIntervalUASs = _AcSonetPathDayIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 2, 1, 12),
    _AcSonetPathDayIntervalUASs_Type()
)
acSonetPathDayIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetPathDayIntervalUASs.setStatus("current")
_AcSonetPathDayIntervalBER_Type = PerfIntervalCount
_AcSonetPathDayIntervalBER_Object = MibTableColumn
acSonetPathDayIntervalBER = _AcSonetPathDayIntervalBER_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 2, 1, 13),
    _AcSonetPathDayIntervalBER_Type()
)
acSonetPathDayIntervalBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetPathDayIntervalBER.setStatus("deprecated")
_AcSonetPathThresholdTable_Object = MibTable
acSonetPathThresholdTable = _AcSonetPathThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 3)
)
if mibBuilder.loadTexts:
    acSonetPathThresholdTable.setStatus("current")
_AcSonetPathThresholdEntry_Object = MibTableRow
acSonetPathThresholdEntry = _AcSonetPathThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 3, 1)
)
acSonetPathThresholdEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPathThresholdNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPathThresholdSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPathThresholdPort"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPathThresholdPath"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPathThresholdSelectionNum"),
)
if mibBuilder.loadTexts:
    acSonetPathThresholdEntry.setStatus("current")
_AcSonetPathThresholdNodeId_Type = AcNodeId
_AcSonetPathThresholdNodeId_Object = MibTableColumn
acSonetPathThresholdNodeId = _AcSonetPathThresholdNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 3, 1, 1),
    _AcSonetPathThresholdNodeId_Type()
)
acSonetPathThresholdNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPathThresholdNodeId.setStatus("current")
_AcSonetPathThresholdSlot_Type = AcSlotNumber
_AcSonetPathThresholdSlot_Object = MibTableColumn
acSonetPathThresholdSlot = _AcSonetPathThresholdSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 3, 1, 2),
    _AcSonetPathThresholdSlot_Type()
)
acSonetPathThresholdSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPathThresholdSlot.setStatus("current")
_AcSonetPathThresholdPort_Type = AcPortNumber
_AcSonetPathThresholdPort_Object = MibTableColumn
acSonetPathThresholdPort = _AcSonetPathThresholdPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 3, 1, 3),
    _AcSonetPathThresholdPort_Type()
)
acSonetPathThresholdPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPathThresholdPort.setStatus("current")
_AcSonetPathThresholdPath_Type = Integer32
_AcSonetPathThresholdPath_Object = MibTableColumn
acSonetPathThresholdPath = _AcSonetPathThresholdPath_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 3, 1, 4),
    _AcSonetPathThresholdPath_Type()
)
acSonetPathThresholdPath.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPathThresholdPath.setStatus("current")


class _AcSonetPathThresholdSelectionNum_Type(Integer32):
    """Custom type acSonetPathThresholdSelectionNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("day", 2),
          ("minute", 1))
    )


_AcSonetPathThresholdSelectionNum_Type.__name__ = "Integer32"
_AcSonetPathThresholdSelectionNum_Object = MibTableColumn
acSonetPathThresholdSelectionNum = _AcSonetPathThresholdSelectionNum_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 3, 1, 5),
    _AcSonetPathThresholdSelectionNum_Type()
)
acSonetPathThresholdSelectionNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPathThresholdSelectionNum.setStatus("current")
_AcSonetPathThresholdAdminStatus_Type = AcAdminStatus
_AcSonetPathThresholdAdminStatus_Object = MibTableColumn
acSonetPathThresholdAdminStatus = _AcSonetPathThresholdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 3, 1, 6),
    _AcSonetPathThresholdAdminStatus_Type()
)
acSonetPathThresholdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetPathThresholdAdminStatus.setStatus("deprecated")


class _AcSonetPathThresholdESs_Type(Integer32):
    """Custom type acSonetPathThresholdESs based on Integer32"""
    defaultValue = 0


_AcSonetPathThresholdESs_Object = MibTableColumn
acSonetPathThresholdESs = _AcSonetPathThresholdESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 3, 1, 7),
    _AcSonetPathThresholdESs_Type()
)
acSonetPathThresholdESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetPathThresholdESs.setStatus("current")


class _AcSonetPathThresholdSESs_Type(Integer32):
    """Custom type acSonetPathThresholdSESs based on Integer32"""
    defaultValue = 0


_AcSonetPathThresholdSESs_Object = MibTableColumn
acSonetPathThresholdSESs = _AcSonetPathThresholdSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 3, 1, 8),
    _AcSonetPathThresholdSESs_Type()
)
acSonetPathThresholdSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetPathThresholdSESs.setStatus("current")


class _AcSonetPathThresholdCVs_Type(Integer32):
    """Custom type acSonetPathThresholdCVs based on Integer32"""
    defaultValue = 0


_AcSonetPathThresholdCVs_Object = MibTableColumn
acSonetPathThresholdCVs = _AcSonetPathThresholdCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 3, 1, 9),
    _AcSonetPathThresholdCVs_Type()
)
acSonetPathThresholdCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetPathThresholdCVs.setStatus("current")


class _AcSonetPathThresholdUASs_Type(Integer32):
    """Custom type acSonetPathThresholdUASs based on Integer32"""
    defaultValue = 0


_AcSonetPathThresholdUASs_Object = MibTableColumn
acSonetPathThresholdUASs = _AcSonetPathThresholdUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 3, 1, 10),
    _AcSonetPathThresholdUASs_Type()
)
acSonetPathThresholdUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetPathThresholdUASs.setStatus("current")
_AcSonetPathRDITable_Object = MibTable
acSonetPathRDITable = _AcSonetPathRDITable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 4)
)
if mibBuilder.loadTexts:
    acSonetPathRDITable.setStatus("current")
_AcSonetPathRDIEntry_Object = MibTableRow
acSonetPathRDIEntry = _AcSonetPathRDIEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 4, 1)
)
acSonetPathRDIEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPathRDINodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPathRDISlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPathRDIPort"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPathRDIPath"),
)
if mibBuilder.loadTexts:
    acSonetPathRDIEntry.setStatus("current")
_AcSonetPathRDINodeId_Type = AcNodeId
_AcSonetPathRDINodeId_Object = MibTableColumn
acSonetPathRDINodeId = _AcSonetPathRDINodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 4, 1, 1),
    _AcSonetPathRDINodeId_Type()
)
acSonetPathRDINodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPathRDINodeId.setStatus("current")
_AcSonetPathRDISlot_Type = AcSlotNumber
_AcSonetPathRDISlot_Object = MibTableColumn
acSonetPathRDISlot = _AcSonetPathRDISlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 4, 1, 2),
    _AcSonetPathRDISlot_Type()
)
acSonetPathRDISlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPathRDISlot.setStatus("current")
_AcSonetPathRDIPort_Type = AcPortNumber
_AcSonetPathRDIPort_Object = MibTableColumn
acSonetPathRDIPort = _AcSonetPathRDIPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 4, 1, 3),
    _AcSonetPathRDIPort_Type()
)
acSonetPathRDIPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPathRDIPort.setStatus("current")
_AcSonetPathRDIPath_Type = Integer32
_AcSonetPathRDIPath_Object = MibTableColumn
acSonetPathRDIPath = _AcSonetPathRDIPath_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 4, 1, 4),
    _AcSonetPathRDIPath_Type()
)
acSonetPathRDIPath.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPathRDIPath.setStatus("current")


class _AcSonetPathRDIOpMode_Type(Integer32):
    """Custom type acSonetPathRDIOpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("erdi", 2),
          ("rdi", 1))
    )


_AcSonetPathRDIOpMode_Type.__name__ = "Integer32"
_AcSonetPathRDIOpMode_Object = MibTableColumn
acSonetPathRDIOpMode = _AcSonetPathRDIOpMode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 4, 1, 5),
    _AcSonetPathRDIOpMode_Type()
)
acSonetPathRDIOpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetPathRDIOpMode.setStatus("current")
_AcSonetPathTIMTable_Object = MibTable
acSonetPathTIMTable = _AcSonetPathTIMTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 5)
)
if mibBuilder.loadTexts:
    acSonetPathTIMTable.setStatus("current")
_AcSonetPathTIMEntry_Object = MibTableRow
acSonetPathTIMEntry = _AcSonetPathTIMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 5, 1)
)
acSonetPathTIMEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPathTIMNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPathTIMSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPathTIMPort"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPathTIMPath"),
)
if mibBuilder.loadTexts:
    acSonetPathTIMEntry.setStatus("current")
_AcSonetPathTIMNodeId_Type = AcNodeId
_AcSonetPathTIMNodeId_Object = MibTableColumn
acSonetPathTIMNodeId = _AcSonetPathTIMNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 5, 1, 1),
    _AcSonetPathTIMNodeId_Type()
)
acSonetPathTIMNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPathTIMNodeId.setStatus("current")
_AcSonetPathTIMSlot_Type = AcSlotNumber
_AcSonetPathTIMSlot_Object = MibTableColumn
acSonetPathTIMSlot = _AcSonetPathTIMSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 5, 1, 2),
    _AcSonetPathTIMSlot_Type()
)
acSonetPathTIMSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPathTIMSlot.setStatus("current")
_AcSonetPathTIMPort_Type = AcPortNumber
_AcSonetPathTIMPort_Object = MibTableColumn
acSonetPathTIMPort = _AcSonetPathTIMPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 5, 1, 3),
    _AcSonetPathTIMPort_Type()
)
acSonetPathTIMPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPathTIMPort.setStatus("current")
_AcSonetPathTIMPath_Type = Integer32
_AcSonetPathTIMPath_Object = MibTableColumn
acSonetPathTIMPath = _AcSonetPathTIMPath_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 5, 1, 4),
    _AcSonetPathTIMPath_Type()
)
acSonetPathTIMPath.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPathTIMPath.setStatus("current")
_AcSonetPathTIMGenerateEnable_Type = TruthValue
_AcSonetPathTIMGenerateEnable_Object = MibTableColumn
acSonetPathTIMGenerateEnable = _AcSonetPathTIMGenerateEnable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 5, 1, 5),
    _AcSonetPathTIMGenerateEnable_Type()
)
acSonetPathTIMGenerateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetPathTIMGenerateEnable.setStatus("current")


class _AcSonetPathTIMDetectEnable_Type(TruthValue):
    """Custom type acSonetPathTIMDetectEnable based on TruthValue"""


_AcSonetPathTIMDetectEnable_Object = MibTableColumn
acSonetPathTIMDetectEnable = _AcSonetPathTIMDetectEnable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 5, 1, 6),
    _AcSonetPathTIMDetectEnable_Type()
)
acSonetPathTIMDetectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetPathTIMDetectEnable.setStatus("current")
_AcSonetPathTIMTransmitedString_Type = AcTraceString
_AcSonetPathTIMTransmitedString_Object = MibTableColumn
acSonetPathTIMTransmitedString = _AcSonetPathTIMTransmitedString_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 5, 1, 7),
    _AcSonetPathTIMTransmitedString_Type()
)
acSonetPathTIMTransmitedString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetPathTIMTransmitedString.setStatus("current")
_AcSonetPathTIMExpectedString_Type = AcTraceString
_AcSonetPathTIMExpectedString_Object = MibTableColumn
acSonetPathTIMExpectedString = _AcSonetPathTIMExpectedString_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 5, 1, 8),
    _AcSonetPathTIMExpectedString_Type()
)
acSonetPathTIMExpectedString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetPathTIMExpectedString.setStatus("current")
_AcSonetPathTIMReceivedString_Type = AcTraceString
_AcSonetPathTIMReceivedString_Object = MibTableColumn
acSonetPathTIMReceivedString = _AcSonetPathTIMReceivedString_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 5, 1, 9),
    _AcSonetPathTIMReceivedString_Type()
)
acSonetPathTIMReceivedString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetPathTIMReceivedString.setStatus("current")
_AcSonetPathTIMFailure_Type = TruthValue
_AcSonetPathTIMFailure_Object = MibTableColumn
acSonetPathTIMFailure = _AcSonetPathTIMFailure_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 5, 1, 10),
    _AcSonetPathTIMFailure_Type()
)
acSonetPathTIMFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetPathTIMFailure.setStatus("current")


class _AcSonetPathTIMFormat_Type(Integer32):
    """Custom type acSonetPathTIMFormat based on Integer32"""
    defaultValue = 0

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
        *(("t16", 3),
          ("t16-crc7", 5),
          ("t16-msb1", 4),
          ("t64", 1),
          ("t64-crlf", 2),
          ("void", 0))
    )


_AcSonetPathTIMFormat_Type.__name__ = "Integer32"
_AcSonetPathTIMFormat_Object = MibTableColumn
acSonetPathTIMFormat = _AcSonetPathTIMFormat_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 5, 1, 11),
    _AcSonetPathTIMFormat_Type()
)
acSonetPathTIMFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetPathTIMFormat.setStatus("current")


class _AcSonetPathTIMMismatchZeros_Type(TruthValue):
    """Custom type acSonetPathTIMMismatchZeros based on TruthValue"""


_AcSonetPathTIMMismatchZeros_Object = MibTableColumn
acSonetPathTIMMismatchZeros = _AcSonetPathTIMMismatchZeros_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 5, 1, 12),
    _AcSonetPathTIMMismatchZeros_Type()
)
acSonetPathTIMMismatchZeros.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetPathTIMMismatchZeros.setStatus("current")
_AcSonetPathPLMTable_Object = MibTable
acSonetPathPLMTable = _AcSonetPathPLMTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 6)
)
if mibBuilder.loadTexts:
    acSonetPathPLMTable.setStatus("current")
_AcSonetPathPLMEntry_Object = MibTableRow
acSonetPathPLMEntry = _AcSonetPathPLMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 6, 1)
)
acSonetPathPLMEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPathPLMNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPathPLMSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPathPLMPort"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPathPLMPath"),
)
if mibBuilder.loadTexts:
    acSonetPathPLMEntry.setStatus("current")
_AcSonetPathPLMNodeId_Type = AcNodeId
_AcSonetPathPLMNodeId_Object = MibTableColumn
acSonetPathPLMNodeId = _AcSonetPathPLMNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 6, 1, 1),
    _AcSonetPathPLMNodeId_Type()
)
acSonetPathPLMNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPathPLMNodeId.setStatus("current")
_AcSonetPathPLMSlot_Type = AcSlotNumber
_AcSonetPathPLMSlot_Object = MibTableColumn
acSonetPathPLMSlot = _AcSonetPathPLMSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 6, 1, 2),
    _AcSonetPathPLMSlot_Type()
)
acSonetPathPLMSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPathPLMSlot.setStatus("current")
_AcSonetPathPLMPort_Type = AcPortNumber
_AcSonetPathPLMPort_Object = MibTableColumn
acSonetPathPLMPort = _AcSonetPathPLMPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 6, 1, 3),
    _AcSonetPathPLMPort_Type()
)
acSonetPathPLMPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPathPLMPort.setStatus("current")
_AcSonetPathPLMPath_Type = Integer32
_AcSonetPathPLMPath_Object = MibTableColumn
acSonetPathPLMPath = _AcSonetPathPLMPath_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 6, 1, 4),
    _AcSonetPathPLMPath_Type()
)
acSonetPathPLMPath.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPathPLMPath.setStatus("current")


class _AcSonetPathPLMDetectEnable_Type(TruthValue):
    """Custom type acSonetPathPLMDetectEnable based on TruthValue"""


_AcSonetPathPLMDetectEnable_Object = MibTableColumn
acSonetPathPLMDetectEnable = _AcSonetPathPLMDetectEnable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 6, 1, 5),
    _AcSonetPathPLMDetectEnable_Type()
)
acSonetPathPLMDetectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetPathPLMDetectEnable.setStatus("current")


class _AcSonetPathPLMTransmitedValue_Type(Integer32):
    """Custom type acSonetPathPLMTransmitedValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcSonetPathPLMTransmitedValue_Type.__name__ = "Integer32"
_AcSonetPathPLMTransmitedValue_Object = MibTableColumn
acSonetPathPLMTransmitedValue = _AcSonetPathPLMTransmitedValue_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 6, 1, 6),
    _AcSonetPathPLMTransmitedValue_Type()
)
acSonetPathPLMTransmitedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetPathPLMTransmitedValue.setStatus("current")


class _AcSonetPathPLMExpectedValue_Type(Integer32):
    """Custom type acSonetPathPLMExpectedValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcSonetPathPLMExpectedValue_Type.__name__ = "Integer32"
_AcSonetPathPLMExpectedValue_Object = MibTableColumn
acSonetPathPLMExpectedValue = _AcSonetPathPLMExpectedValue_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 6, 1, 7),
    _AcSonetPathPLMExpectedValue_Type()
)
acSonetPathPLMExpectedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetPathPLMExpectedValue.setStatus("current")
_AcSonetPathPLMReceivedValue_Type = Integer32
_AcSonetPathPLMReceivedValue_Object = MibTableColumn
acSonetPathPLMReceivedValue = _AcSonetPathPLMReceivedValue_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 6, 1, 8),
    _AcSonetPathPLMReceivedValue_Type()
)
acSonetPathPLMReceivedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetPathPLMReceivedValue.setStatus("current")
_AcSonetPathPLMMismatchFailure_Type = TruthValue
_AcSonetPathPLMMismatchFailure_Object = MibTableColumn
acSonetPathPLMMismatchFailure = _AcSonetPathPLMMismatchFailure_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 6, 1, 9),
    _AcSonetPathPLMMismatchFailure_Type()
)
acSonetPathPLMMismatchFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetPathPLMMismatchFailure.setStatus("current")
_AcSonetPathPLMUnequipped_Type = TruthValue
_AcSonetPathPLMUnequipped_Object = MibTableColumn
acSonetPathPLMUnequipped = _AcSonetPathPLMUnequipped_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 6, 1, 10),
    _AcSonetPathPLMUnequipped_Type()
)
acSonetPathPLMUnequipped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetPathPLMUnequipped.setStatus("current")
_AcSonetPathProtectionTable_Object = MibTable
acSonetPathProtectionTable = _AcSonetPathProtectionTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 7)
)
if mibBuilder.loadTexts:
    acSonetPathProtectionTable.setStatus("current")
_AcSonetPathProtectionEntry_Object = MibTableRow
acSonetPathProtectionEntry = _AcSonetPathProtectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 7, 1)
)
acSonetPathProtectionEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPathProtectionNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPathProtectionSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPathProtectionPort"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetPathProtectionPath"),
)
if mibBuilder.loadTexts:
    acSonetPathProtectionEntry.setStatus("current")
_AcSonetPathProtectionNodeId_Type = AcNodeId
_AcSonetPathProtectionNodeId_Object = MibTableColumn
acSonetPathProtectionNodeId = _AcSonetPathProtectionNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 7, 1, 1),
    _AcSonetPathProtectionNodeId_Type()
)
acSonetPathProtectionNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPathProtectionNodeId.setStatus("current")
_AcSonetPathProtectionSlot_Type = AcSlotNumber
_AcSonetPathProtectionSlot_Object = MibTableColumn
acSonetPathProtectionSlot = _AcSonetPathProtectionSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 7, 1, 2),
    _AcSonetPathProtectionSlot_Type()
)
acSonetPathProtectionSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPathProtectionSlot.setStatus("current")
_AcSonetPathProtectionPort_Type = AcPortNumber
_AcSonetPathProtectionPort_Object = MibTableColumn
acSonetPathProtectionPort = _AcSonetPathProtectionPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 7, 1, 3),
    _AcSonetPathProtectionPort_Type()
)
acSonetPathProtectionPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPathProtectionPort.setStatus("current")
_AcSonetPathProtectionPath_Type = Integer32
_AcSonetPathProtectionPath_Object = MibTableColumn
acSonetPathProtectionPath = _AcSonetPathProtectionPath_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 7, 1, 4),
    _AcSonetPathProtectionPath_Type()
)
acSonetPathProtectionPath.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetPathProtectionPath.setStatus("current")


class _AcSonetPathProtectionSwitchType_Type(Integer32):
    """Custom type acSonetPathProtectionSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonrevertive", 2),
          ("revertive", 1))
    )


_AcSonetPathProtectionSwitchType_Type.__name__ = "Integer32"
_AcSonetPathProtectionSwitchType_Object = MibTableColumn
acSonetPathProtectionSwitchType = _AcSonetPathProtectionSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 7, 1, 5),
    _AcSonetPathProtectionSwitchType_Type()
)
acSonetPathProtectionSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetPathProtectionSwitchType.setStatus("current")


class _AcSonetPathProtectionSFThreshold_Type(Integer32):
    """Custom type acSonetPathProtectionSFThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 5),
    )


_AcSonetPathProtectionSFThreshold_Type.__name__ = "Integer32"
_AcSonetPathProtectionSFThreshold_Object = MibTableColumn
acSonetPathProtectionSFThreshold = _AcSonetPathProtectionSFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 7, 1, 6),
    _AcSonetPathProtectionSFThreshold_Type()
)
acSonetPathProtectionSFThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetPathProtectionSFThreshold.setStatus("current")


class _AcSonetPathProtectionSDThreshold_Type(Integer32):
    """Custom type acSonetPathProtectionSDThreshold based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 9),
    )


_AcSonetPathProtectionSDThreshold_Type.__name__ = "Integer32"
_AcSonetPathProtectionSDThreshold_Object = MibTableColumn
acSonetPathProtectionSDThreshold = _AcSonetPathProtectionSDThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 7, 1, 7),
    _AcSonetPathProtectionSDThreshold_Type()
)
acSonetPathProtectionSDThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetPathProtectionSDThreshold.setStatus("current")
_AcSonetPathProtectionActiveTraffic_Type = TruthValue
_AcSonetPathProtectionActiveTraffic_Object = MibTableColumn
acSonetPathProtectionActiveTraffic = _AcSonetPathProtectionActiveTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 7, 1, 8),
    _AcSonetPathProtectionActiveTraffic_Type()
)
acSonetPathProtectionActiveTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetPathProtectionActiveTraffic.setStatus("current")
_AcSonetPathProtectionProtectionSwitch_Type = TruthValue
_AcSonetPathProtectionProtectionSwitch_Object = MibTableColumn
acSonetPathProtectionProtectionSwitch = _AcSonetPathProtectionProtectionSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 7, 1, 9),
    _AcSonetPathProtectionProtectionSwitch_Type()
)
acSonetPathProtectionProtectionSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetPathProtectionProtectionSwitch.setStatus("current")


class _AcSonetPathProtectionWTRTime_Type(Integer32):
    """Custom type acSonetPathProtectionWTRTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 720),
    )


_AcSonetPathProtectionWTRTime_Type.__name__ = "Integer32"
_AcSonetPathProtectionWTRTime_Object = MibTableColumn
acSonetPathProtectionWTRTime = _AcSonetPathProtectionWTRTime_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 7, 1, 10),
    _AcSonetPathProtectionWTRTime_Type()
)
acSonetPathProtectionWTRTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetPathProtectionWTRTime.setStatus("current")


class _AcSonetPathProtectionWTITime_Type(Integer32):
    """Custom type acSonetPathProtectionWTITime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_AcSonetPathProtectionWTITime_Type.__name__ = "Integer32"
_AcSonetPathProtectionWTITime_Object = MibTableColumn
acSonetPathProtectionWTITime = _AcSonetPathProtectionWTITime_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 7, 1, 11),
    _AcSonetPathProtectionWTITime_Type()
)
acSonetPathProtectionWTITime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetPathProtectionWTITime.setStatus("current")


class _AcSonetPathProtectionWTCTime_Type(Integer32):
    """Custom type acSonetPathProtectionWTCTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 720),
    )


_AcSonetPathProtectionWTCTime_Type.__name__ = "Integer32"
_AcSonetPathProtectionWTCTime_Object = MibTableColumn
acSonetPathProtectionWTCTime = _AcSonetPathProtectionWTCTime_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 7, 1, 12),
    _AcSonetPathProtectionWTCTime_Type()
)
acSonetPathProtectionWTCTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetPathProtectionWTCTime.setStatus("current")


class _AcSonetPathProtectionWTRelTime_Type(Integer32):
    """Custom type acSonetPathProtectionWTRelTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_AcSonetPathProtectionWTRelTime_Type.__name__ = "Integer32"
_AcSonetPathProtectionWTRelTime_Object = MibTableColumn
acSonetPathProtectionWTRelTime = _AcSonetPathProtectionWTRelTime_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 7, 1, 13),
    _AcSonetPathProtectionWTRelTime_Type()
)
acSonetPathProtectionWTRelTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetPathProtectionWTRelTime.setStatus("current")


class _AcSonetPathProtectionManSwitch_Type(Integer32):
    """Custom type acSonetPathProtectionManSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("clear-lockout-working", 9),
          ("exercise", 7),
          ("extra-traffic", 10),
          ("force-protection", 4),
          ("force-working", 3),
          ("lockout-protection", 2),
          ("lockout-working", 8),
          ("manual-protection", 6),
          ("manual-working", 5))
    )


_AcSonetPathProtectionManSwitch_Type.__name__ = "Integer32"
_AcSonetPathProtectionManSwitch_Object = MibTableColumn
acSonetPathProtectionManSwitch = _AcSonetPathProtectionManSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 7, 1, 14),
    _AcSonetPathProtectionManSwitch_Type()
)
acSonetPathProtectionManSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetPathProtectionManSwitch.setStatus("current")


class _AcSonetPathProtectionSwitchOpStatus_Type(Integer32):
    """Custom type acSonetPathProtectionSwitchOpStatus based on Integer32"""
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
        *(("bridged", 2),
          ("extra-traffic", 5),
          ("idle", 1),
          ("passthrough", 4),
          ("switched", 3))
    )


_AcSonetPathProtectionSwitchOpStatus_Type.__name__ = "Integer32"
_AcSonetPathProtectionSwitchOpStatus_Object = MibTableColumn
acSonetPathProtectionSwitchOpStatus = _AcSonetPathProtectionSwitchOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 7, 1, 15),
    _AcSonetPathProtectionSwitchOpStatus_Type()
)
acSonetPathProtectionSwitchOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetPathProtectionSwitchOpStatus.setStatus("current")


class _AcSonetPathProtectionProtectionMode_Type(Integer32):
    """Custom type acSonetPathProtectionProtectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("odp", 1),
          ("upsr", 2))
    )


_AcSonetPathProtectionProtectionMode_Type.__name__ = "Integer32"
_AcSonetPathProtectionProtectionMode_Object = MibTableColumn
acSonetPathProtectionProtectionMode = _AcSonetPathProtectionProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 7, 1, 16),
    _AcSonetPathProtectionProtectionMode_Type()
)
acSonetPathProtectionProtectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetPathProtectionProtectionMode.setStatus("deprecated")
_AcSonetFarEndPath_ObjectIdentity = ObjectIdentity
acSonetFarEndPath = _AcSonetFarEndPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2)
)
_AcSonetFarEndPath15MinuteIntervalTable_Object = MibTable
acSonetFarEndPath15MinuteIntervalTable = _AcSonetFarEndPath15MinuteIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 1)
)
if mibBuilder.loadTexts:
    acSonetFarEndPath15MinuteIntervalTable.setStatus("current")
_AcSonetFarEndPath15MinuteIntervalEntry_Object = MibTableRow
acSonetFarEndPath15MinuteIntervalEntry = _AcSonetFarEndPath15MinuteIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 1, 1)
)
acSonetFarEndPath15MinuteIntervalEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalPort"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalPath"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalNumber"),
)
if mibBuilder.loadTexts:
    acSonetFarEndPath15MinuteIntervalEntry.setStatus("current")
_AcSonetFarEndPath15MinuteIntervalNodeId_Type = AcNodeId
_AcSonetFarEndPath15MinuteIntervalNodeId_Object = MibTableColumn
acSonetFarEndPath15MinuteIntervalNodeId = _AcSonetFarEndPath15MinuteIntervalNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 1, 1, 1),
    _AcSonetFarEndPath15MinuteIntervalNodeId_Type()
)
acSonetFarEndPath15MinuteIntervalNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndPath15MinuteIntervalNodeId.setStatus("current")
_AcSonetFarEndPath15MinuteIntervalSlot_Type = AcSlotNumber
_AcSonetFarEndPath15MinuteIntervalSlot_Object = MibTableColumn
acSonetFarEndPath15MinuteIntervalSlot = _AcSonetFarEndPath15MinuteIntervalSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 1, 1, 2),
    _AcSonetFarEndPath15MinuteIntervalSlot_Type()
)
acSonetFarEndPath15MinuteIntervalSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndPath15MinuteIntervalSlot.setStatus("current")
_AcSonetFarEndPath15MinuteIntervalPort_Type = AcPortNumber
_AcSonetFarEndPath15MinuteIntervalPort_Object = MibTableColumn
acSonetFarEndPath15MinuteIntervalPort = _AcSonetFarEndPath15MinuteIntervalPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 1, 1, 3),
    _AcSonetFarEndPath15MinuteIntervalPort_Type()
)
acSonetFarEndPath15MinuteIntervalPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndPath15MinuteIntervalPort.setStatus("current")
_AcSonetFarEndPath15MinuteIntervalPath_Type = Integer32
_AcSonetFarEndPath15MinuteIntervalPath_Object = MibTableColumn
acSonetFarEndPath15MinuteIntervalPath = _AcSonetFarEndPath15MinuteIntervalPath_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 1, 1, 4),
    _AcSonetFarEndPath15MinuteIntervalPath_Type()
)
acSonetFarEndPath15MinuteIntervalPath.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndPath15MinuteIntervalPath.setStatus("current")


class _AcSonetFarEndPath15MinuteIntervalNumber_Type(Integer32):
    """Custom type acSonetFarEndPath15MinuteIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 98),
    )


_AcSonetFarEndPath15MinuteIntervalNumber_Type.__name__ = "Integer32"
_AcSonetFarEndPath15MinuteIntervalNumber_Object = MibTableColumn
acSonetFarEndPath15MinuteIntervalNumber = _AcSonetFarEndPath15MinuteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 1, 1, 5),
    _AcSonetFarEndPath15MinuteIntervalNumber_Type()
)
acSonetFarEndPath15MinuteIntervalNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndPath15MinuteIntervalNumber.setStatus("current")
_AcSonetFarEndPath15MinuteIntervalValidStats_Type = TruthValue
_AcSonetFarEndPath15MinuteIntervalValidStats_Object = MibTableColumn
acSonetFarEndPath15MinuteIntervalValidStats = _AcSonetFarEndPath15MinuteIntervalValidStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 1, 1, 6),
    _AcSonetFarEndPath15MinuteIntervalValidStats_Type()
)
acSonetFarEndPath15MinuteIntervalValidStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetFarEndPath15MinuteIntervalValidStats.setStatus("current")
_AcSonetFarEndPath15MinuteIntervalResetStats_Type = TruthValue
_AcSonetFarEndPath15MinuteIntervalResetStats_Object = MibTableColumn
acSonetFarEndPath15MinuteIntervalResetStats = _AcSonetFarEndPath15MinuteIntervalResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 1, 1, 7),
    _AcSonetFarEndPath15MinuteIntervalResetStats_Type()
)
acSonetFarEndPath15MinuteIntervalResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetFarEndPath15MinuteIntervalResetStats.setStatus("current")
_AcSonetFarEndPath15MinuteIntervalESs_Type = PerfIntervalCount
_AcSonetFarEndPath15MinuteIntervalESs_Object = MibTableColumn
acSonetFarEndPath15MinuteIntervalESs = _AcSonetFarEndPath15MinuteIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 1, 1, 8),
    _AcSonetFarEndPath15MinuteIntervalESs_Type()
)
acSonetFarEndPath15MinuteIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetFarEndPath15MinuteIntervalESs.setStatus("current")
_AcSonetFarEndPath15MinuteIntervalSESs_Type = PerfIntervalCount
_AcSonetFarEndPath15MinuteIntervalSESs_Object = MibTableColumn
acSonetFarEndPath15MinuteIntervalSESs = _AcSonetFarEndPath15MinuteIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 1, 1, 9),
    _AcSonetFarEndPath15MinuteIntervalSESs_Type()
)
acSonetFarEndPath15MinuteIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetFarEndPath15MinuteIntervalSESs.setStatus("current")
_AcSonetFarEndPath15MinuteIntervalCVs_Type = PerfIntervalCount
_AcSonetFarEndPath15MinuteIntervalCVs_Object = MibTableColumn
acSonetFarEndPath15MinuteIntervalCVs = _AcSonetFarEndPath15MinuteIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 1, 1, 10),
    _AcSonetFarEndPath15MinuteIntervalCVs_Type()
)
acSonetFarEndPath15MinuteIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetFarEndPath15MinuteIntervalCVs.setStatus("current")
_AcSonetFarEndPath15MinuteIntervalUASs_Type = PerfIntervalCount
_AcSonetFarEndPath15MinuteIntervalUASs_Object = MibTableColumn
acSonetFarEndPath15MinuteIntervalUASs = _AcSonetFarEndPath15MinuteIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 1, 1, 11),
    _AcSonetFarEndPath15MinuteIntervalUASs_Type()
)
acSonetFarEndPath15MinuteIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetFarEndPath15MinuteIntervalUASs.setStatus("current")
_AcSonetFarEndPathDayIntervalTable_Object = MibTable
acSonetFarEndPathDayIntervalTable = _AcSonetFarEndPathDayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 2)
)
if mibBuilder.loadTexts:
    acSonetFarEndPathDayIntervalTable.setStatus("current")
_AcSonetFarEndPathDayIntervalEntry_Object = MibTableRow
acSonetFarEndPathDayIntervalEntry = _AcSonetFarEndPathDayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 2, 1)
)
acSonetFarEndPathDayIntervalEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalPort"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalPath"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalNumber"),
)
if mibBuilder.loadTexts:
    acSonetFarEndPathDayIntervalEntry.setStatus("current")
_AcSonetFarEndPathDayIntervalNodeId_Type = AcNodeId
_AcSonetFarEndPathDayIntervalNodeId_Object = MibTableColumn
acSonetFarEndPathDayIntervalNodeId = _AcSonetFarEndPathDayIntervalNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 2, 1, 1),
    _AcSonetFarEndPathDayIntervalNodeId_Type()
)
acSonetFarEndPathDayIntervalNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndPathDayIntervalNodeId.setStatus("current")
_AcSonetFarEndPathDayIntervalSlot_Type = AcSlotNumber
_AcSonetFarEndPathDayIntervalSlot_Object = MibTableColumn
acSonetFarEndPathDayIntervalSlot = _AcSonetFarEndPathDayIntervalSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 2, 1, 2),
    _AcSonetFarEndPathDayIntervalSlot_Type()
)
acSonetFarEndPathDayIntervalSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndPathDayIntervalSlot.setStatus("current")
_AcSonetFarEndPathDayIntervalPort_Type = AcPortNumber
_AcSonetFarEndPathDayIntervalPort_Object = MibTableColumn
acSonetFarEndPathDayIntervalPort = _AcSonetFarEndPathDayIntervalPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 2, 1, 3),
    _AcSonetFarEndPathDayIntervalPort_Type()
)
acSonetFarEndPathDayIntervalPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndPathDayIntervalPort.setStatus("current")
_AcSonetFarEndPathDayIntervalPath_Type = Integer32
_AcSonetFarEndPathDayIntervalPath_Object = MibTableColumn
acSonetFarEndPathDayIntervalPath = _AcSonetFarEndPathDayIntervalPath_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 2, 1, 4),
    _AcSonetFarEndPathDayIntervalPath_Type()
)
acSonetFarEndPathDayIntervalPath.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndPathDayIntervalPath.setStatus("current")


class _AcSonetFarEndPathDayIntervalNumber_Type(Integer32):
    """Custom type acSonetFarEndPathDayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_AcSonetFarEndPathDayIntervalNumber_Type.__name__ = "Integer32"
_AcSonetFarEndPathDayIntervalNumber_Object = MibTableColumn
acSonetFarEndPathDayIntervalNumber = _AcSonetFarEndPathDayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 2, 1, 5),
    _AcSonetFarEndPathDayIntervalNumber_Type()
)
acSonetFarEndPathDayIntervalNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndPathDayIntervalNumber.setStatus("current")
_AcSonetFarEndPathDayIntervalValidStats_Type = TruthValue
_AcSonetFarEndPathDayIntervalValidStats_Object = MibTableColumn
acSonetFarEndPathDayIntervalValidStats = _AcSonetFarEndPathDayIntervalValidStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 2, 1, 6),
    _AcSonetFarEndPathDayIntervalValidStats_Type()
)
acSonetFarEndPathDayIntervalValidStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetFarEndPathDayIntervalValidStats.setStatus("current")
_AcSonetFarEndPathDayIntervalResetStats_Type = TruthValue
_AcSonetFarEndPathDayIntervalResetStats_Object = MibTableColumn
acSonetFarEndPathDayIntervalResetStats = _AcSonetFarEndPathDayIntervalResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 2, 1, 7),
    _AcSonetFarEndPathDayIntervalResetStats_Type()
)
acSonetFarEndPathDayIntervalResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetFarEndPathDayIntervalResetStats.setStatus("current")
_AcSonetFarEndPathDayIntervalESs_Type = PerfIntervalCount
_AcSonetFarEndPathDayIntervalESs_Object = MibTableColumn
acSonetFarEndPathDayIntervalESs = _AcSonetFarEndPathDayIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 2, 1, 8),
    _AcSonetFarEndPathDayIntervalESs_Type()
)
acSonetFarEndPathDayIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetFarEndPathDayIntervalESs.setStatus("current")
_AcSonetFarEndPathDayIntervalSESs_Type = PerfIntervalCount
_AcSonetFarEndPathDayIntervalSESs_Object = MibTableColumn
acSonetFarEndPathDayIntervalSESs = _AcSonetFarEndPathDayIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 2, 1, 9),
    _AcSonetFarEndPathDayIntervalSESs_Type()
)
acSonetFarEndPathDayIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetFarEndPathDayIntervalSESs.setStatus("current")
_AcSonetFarEndPathDayIntervalCVs_Type = PerfIntervalCount
_AcSonetFarEndPathDayIntervalCVs_Object = MibTableColumn
acSonetFarEndPathDayIntervalCVs = _AcSonetFarEndPathDayIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 2, 1, 10),
    _AcSonetFarEndPathDayIntervalCVs_Type()
)
acSonetFarEndPathDayIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetFarEndPathDayIntervalCVs.setStatus("current")
_AcSonetFarEndPathDayIntervalUASs_Type = PerfIntervalCount
_AcSonetFarEndPathDayIntervalUASs_Object = MibTableColumn
acSonetFarEndPathDayIntervalUASs = _AcSonetFarEndPathDayIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 2, 1, 11),
    _AcSonetFarEndPathDayIntervalUASs_Type()
)
acSonetFarEndPathDayIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetFarEndPathDayIntervalUASs.setStatus("current")
_AcSonetFarEndPathThresholdTable_Object = MibTable
acSonetFarEndPathThresholdTable = _AcSonetFarEndPathThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 3)
)
if mibBuilder.loadTexts:
    acSonetFarEndPathThresholdTable.setStatus("current")
_AcSonetFarEndPathThresholdEntry_Object = MibTableRow
acSonetFarEndPathThresholdEntry = _AcSonetFarEndPathThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 3, 1)
)
acSonetFarEndPathThresholdEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathThresholdNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathThresholdSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathThresholdPort"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathThresholdPath"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathThresholdSelectionNum"),
)
if mibBuilder.loadTexts:
    acSonetFarEndPathThresholdEntry.setStatus("current")
_AcSonetFarEndPathThresholdNodeId_Type = AcNodeId
_AcSonetFarEndPathThresholdNodeId_Object = MibTableColumn
acSonetFarEndPathThresholdNodeId = _AcSonetFarEndPathThresholdNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 3, 1, 1),
    _AcSonetFarEndPathThresholdNodeId_Type()
)
acSonetFarEndPathThresholdNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndPathThresholdNodeId.setStatus("current")
_AcSonetFarEndPathThresholdSlot_Type = AcSlotNumber
_AcSonetFarEndPathThresholdSlot_Object = MibTableColumn
acSonetFarEndPathThresholdSlot = _AcSonetFarEndPathThresholdSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 3, 1, 2),
    _AcSonetFarEndPathThresholdSlot_Type()
)
acSonetFarEndPathThresholdSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndPathThresholdSlot.setStatus("current")
_AcSonetFarEndPathThresholdPort_Type = AcPortNumber
_AcSonetFarEndPathThresholdPort_Object = MibTableColumn
acSonetFarEndPathThresholdPort = _AcSonetFarEndPathThresholdPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 3, 1, 3),
    _AcSonetFarEndPathThresholdPort_Type()
)
acSonetFarEndPathThresholdPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndPathThresholdPort.setStatus("current")
_AcSonetFarEndPathThresholdPath_Type = Integer32
_AcSonetFarEndPathThresholdPath_Object = MibTableColumn
acSonetFarEndPathThresholdPath = _AcSonetFarEndPathThresholdPath_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 3, 1, 4),
    _AcSonetFarEndPathThresholdPath_Type()
)
acSonetFarEndPathThresholdPath.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndPathThresholdPath.setStatus("current")


class _AcSonetFarEndPathThresholdSelectionNum_Type(Integer32):
    """Custom type acSonetFarEndPathThresholdSelectionNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("day", 2),
          ("minute", 1))
    )


_AcSonetFarEndPathThresholdSelectionNum_Type.__name__ = "Integer32"
_AcSonetFarEndPathThresholdSelectionNum_Object = MibTableColumn
acSonetFarEndPathThresholdSelectionNum = _AcSonetFarEndPathThresholdSelectionNum_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 3, 1, 5),
    _AcSonetFarEndPathThresholdSelectionNum_Type()
)
acSonetFarEndPathThresholdSelectionNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndPathThresholdSelectionNum.setStatus("current")
_AcSonetFarEndPathThresholdAdminStatus_Type = AcAdminStatus
_AcSonetFarEndPathThresholdAdminStatus_Object = MibTableColumn
acSonetFarEndPathThresholdAdminStatus = _AcSonetFarEndPathThresholdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 3, 1, 6),
    _AcSonetFarEndPathThresholdAdminStatus_Type()
)
acSonetFarEndPathThresholdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetFarEndPathThresholdAdminStatus.setStatus("deprecated")


class _AcSonetFarEndPathThresholdESs_Type(Integer32):
    """Custom type acSonetFarEndPathThresholdESs based on Integer32"""
    defaultValue = 0


_AcSonetFarEndPathThresholdESs_Object = MibTableColumn
acSonetFarEndPathThresholdESs = _AcSonetFarEndPathThresholdESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 3, 1, 7),
    _AcSonetFarEndPathThresholdESs_Type()
)
acSonetFarEndPathThresholdESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetFarEndPathThresholdESs.setStatus("current")


class _AcSonetFarEndPathThresholdSESs_Type(Integer32):
    """Custom type acSonetFarEndPathThresholdSESs based on Integer32"""
    defaultValue = 0


_AcSonetFarEndPathThresholdSESs_Object = MibTableColumn
acSonetFarEndPathThresholdSESs = _AcSonetFarEndPathThresholdSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 3, 1, 8),
    _AcSonetFarEndPathThresholdSESs_Type()
)
acSonetFarEndPathThresholdSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetFarEndPathThresholdSESs.setStatus("current")


class _AcSonetFarEndPathThresholdCVs_Type(Integer32):
    """Custom type acSonetFarEndPathThresholdCVs based on Integer32"""
    defaultValue = 0


_AcSonetFarEndPathThresholdCVs_Object = MibTableColumn
acSonetFarEndPathThresholdCVs = _AcSonetFarEndPathThresholdCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 3, 1, 9),
    _AcSonetFarEndPathThresholdCVs_Type()
)
acSonetFarEndPathThresholdCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetFarEndPathThresholdCVs.setStatus("current")


class _AcSonetFarEndPathThresholdUASs_Type(Integer32):
    """Custom type acSonetFarEndPathThresholdUASs based on Integer32"""
    defaultValue = 0


_AcSonetFarEndPathThresholdUASs_Object = MibTableColumn
acSonetFarEndPathThresholdUASs = _AcSonetFarEndPathThresholdUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 3, 1, 10),
    _AcSonetFarEndPathThresholdUASs_Type()
)
acSonetFarEndPathThresholdUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetFarEndPathThresholdUASs.setStatus("current")
_AcSonetObjectsVT_ObjectIdentity = ObjectIdentity
acSonetObjectsVT = _AcSonetObjectsVT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3)
)
_AcSonetVT_ObjectIdentity = ObjectIdentity
acSonetVT = _AcSonetVT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1)
)
_AcSonetVT15MinuteIntervalTable_Object = MibTable
acSonetVT15MinuteIntervalTable = _AcSonetVT15MinuteIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 1)
)
if mibBuilder.loadTexts:
    acSonetVT15MinuteIntervalTable.setStatus("current")
_AcSonetVT15MinuteIntervalEntry_Object = MibTableRow
acSonetVT15MinuteIntervalEntry = _AcSonetVT15MinuteIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 1, 1)
)
acSonetVT15MinuteIntervalEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalPort"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalVT"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNumber"),
)
if mibBuilder.loadTexts:
    acSonetVT15MinuteIntervalEntry.setStatus("current")
_AcSonetVT15MinuteIntervalNodeId_Type = AcNodeId
_AcSonetVT15MinuteIntervalNodeId_Object = MibTableColumn
acSonetVT15MinuteIntervalNodeId = _AcSonetVT15MinuteIntervalNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 1, 1, 1),
    _AcSonetVT15MinuteIntervalNodeId_Type()
)
acSonetVT15MinuteIntervalNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetVT15MinuteIntervalNodeId.setStatus("current")
_AcSonetVT15MinuteIntervalSlot_Type = AcSlotNumber
_AcSonetVT15MinuteIntervalSlot_Object = MibTableColumn
acSonetVT15MinuteIntervalSlot = _AcSonetVT15MinuteIntervalSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 1, 1, 2),
    _AcSonetVT15MinuteIntervalSlot_Type()
)
acSonetVT15MinuteIntervalSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetVT15MinuteIntervalSlot.setStatus("current")
_AcSonetVT15MinuteIntervalPort_Type = AcPortNumber
_AcSonetVT15MinuteIntervalPort_Object = MibTableColumn
acSonetVT15MinuteIntervalPort = _AcSonetVT15MinuteIntervalPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 1, 1, 3),
    _AcSonetVT15MinuteIntervalPort_Type()
)
acSonetVT15MinuteIntervalPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetVT15MinuteIntervalPort.setStatus("current")
_AcSonetVT15MinuteIntervalVT_Type = Integer32
_AcSonetVT15MinuteIntervalVT_Object = MibTableColumn
acSonetVT15MinuteIntervalVT = _AcSonetVT15MinuteIntervalVT_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 1, 1, 4),
    _AcSonetVT15MinuteIntervalVT_Type()
)
acSonetVT15MinuteIntervalVT.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetVT15MinuteIntervalVT.setStatus("current")


class _AcSonetVT15MinuteIntervalNumber_Type(Integer32):
    """Custom type acSonetVT15MinuteIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 98),
    )


_AcSonetVT15MinuteIntervalNumber_Type.__name__ = "Integer32"
_AcSonetVT15MinuteIntervalNumber_Object = MibTableColumn
acSonetVT15MinuteIntervalNumber = _AcSonetVT15MinuteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 1, 1, 5),
    _AcSonetVT15MinuteIntervalNumber_Type()
)
acSonetVT15MinuteIntervalNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetVT15MinuteIntervalNumber.setStatus("current")


class _AcSonetVT15MinuteIntervalStatus_Type(Integer32):
    """Custom type acSonetVT15MinuteIntervalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 192),
    )


_AcSonetVT15MinuteIntervalStatus_Type.__name__ = "Integer32"
_AcSonetVT15MinuteIntervalStatus_Object = MibTableColumn
acSonetVT15MinuteIntervalStatus = _AcSonetVT15MinuteIntervalStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 1, 1, 7),
    _AcSonetVT15MinuteIntervalStatus_Type()
)
acSonetVT15MinuteIntervalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetVT15MinuteIntervalStatus.setStatus("current")
_AcSonetVT15MinuteIntervalValidStats_Type = TruthValue
_AcSonetVT15MinuteIntervalValidStats_Object = MibTableColumn
acSonetVT15MinuteIntervalValidStats = _AcSonetVT15MinuteIntervalValidStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 1, 1, 8),
    _AcSonetVT15MinuteIntervalValidStats_Type()
)
acSonetVT15MinuteIntervalValidStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetVT15MinuteIntervalValidStats.setStatus("current")
_AcSonetVT15MinuteIntervalResetStats_Type = TruthValue
_AcSonetVT15MinuteIntervalResetStats_Object = MibTableColumn
acSonetVT15MinuteIntervalResetStats = _AcSonetVT15MinuteIntervalResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 1, 1, 9),
    _AcSonetVT15MinuteIntervalResetStats_Type()
)
acSonetVT15MinuteIntervalResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetVT15MinuteIntervalResetStats.setStatus("current")
_AcSonetVT15MinuteIntervalESs_Type = PerfIntervalCount
_AcSonetVT15MinuteIntervalESs_Object = MibTableColumn
acSonetVT15MinuteIntervalESs = _AcSonetVT15MinuteIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 1, 1, 10),
    _AcSonetVT15MinuteIntervalESs_Type()
)
acSonetVT15MinuteIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetVT15MinuteIntervalESs.setStatus("current")
_AcSonetVT15MinuteIntervalSESs_Type = PerfIntervalCount
_AcSonetVT15MinuteIntervalSESs_Object = MibTableColumn
acSonetVT15MinuteIntervalSESs = _AcSonetVT15MinuteIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 1, 1, 11),
    _AcSonetVT15MinuteIntervalSESs_Type()
)
acSonetVT15MinuteIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetVT15MinuteIntervalSESs.setStatus("current")
_AcSonetVT15MinuteIntervalCVs_Type = PerfIntervalCount
_AcSonetVT15MinuteIntervalCVs_Object = MibTableColumn
acSonetVT15MinuteIntervalCVs = _AcSonetVT15MinuteIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 1, 1, 12),
    _AcSonetVT15MinuteIntervalCVs_Type()
)
acSonetVT15MinuteIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetVT15MinuteIntervalCVs.setStatus("current")
_AcSonetVT15MinuteIntervalUASs_Type = PerfIntervalCount
_AcSonetVT15MinuteIntervalUASs_Object = MibTableColumn
acSonetVT15MinuteIntervalUASs = _AcSonetVT15MinuteIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 1, 1, 13),
    _AcSonetVT15MinuteIntervalUASs_Type()
)
acSonetVT15MinuteIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetVT15MinuteIntervalUASs.setStatus("current")
_AcSonetVT15MinuteIntervalBER_Type = PerfIntervalCount
_AcSonetVT15MinuteIntervalBER_Object = MibTableColumn
acSonetVT15MinuteIntervalBER = _AcSonetVT15MinuteIntervalBER_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 1, 1, 14),
    _AcSonetVT15MinuteIntervalBER_Type()
)
acSonetVT15MinuteIntervalBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetVT15MinuteIntervalBER.setStatus("current")
_AcSonetVTDayIntervalTable_Object = MibTable
acSonetVTDayIntervalTable = _AcSonetVTDayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 2)
)
if mibBuilder.loadTexts:
    acSonetVTDayIntervalTable.setStatus("current")
_AcSonetVTDayIntervalEntry_Object = MibTableRow
acSonetVTDayIntervalEntry = _AcSonetVTDayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 2, 1)
)
acSonetVTDayIntervalEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalPort"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalVT"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalNumber"),
)
if mibBuilder.loadTexts:
    acSonetVTDayIntervalEntry.setStatus("current")
_AcSonetVTDayIntervalNodeId_Type = AcNodeId
_AcSonetVTDayIntervalNodeId_Object = MibTableColumn
acSonetVTDayIntervalNodeId = _AcSonetVTDayIntervalNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 2, 1, 1),
    _AcSonetVTDayIntervalNodeId_Type()
)
acSonetVTDayIntervalNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetVTDayIntervalNodeId.setStatus("current")
_AcSonetVTDayIntervalSlot_Type = AcSlotNumber
_AcSonetVTDayIntervalSlot_Object = MibTableColumn
acSonetVTDayIntervalSlot = _AcSonetVTDayIntervalSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 2, 1, 2),
    _AcSonetVTDayIntervalSlot_Type()
)
acSonetVTDayIntervalSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetVTDayIntervalSlot.setStatus("current")
_AcSonetVTDayIntervalPort_Type = AcPortNumber
_AcSonetVTDayIntervalPort_Object = MibTableColumn
acSonetVTDayIntervalPort = _AcSonetVTDayIntervalPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 2, 1, 3),
    _AcSonetVTDayIntervalPort_Type()
)
acSonetVTDayIntervalPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetVTDayIntervalPort.setStatus("current")
_AcSonetVTDayIntervalVT_Type = Integer32
_AcSonetVTDayIntervalVT_Object = MibTableColumn
acSonetVTDayIntervalVT = _AcSonetVTDayIntervalVT_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 2, 1, 4),
    _AcSonetVTDayIntervalVT_Type()
)
acSonetVTDayIntervalVT.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetVTDayIntervalVT.setStatus("current")


class _AcSonetVTDayIntervalNumber_Type(Integer32):
    """Custom type acSonetVTDayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_AcSonetVTDayIntervalNumber_Type.__name__ = "Integer32"
_AcSonetVTDayIntervalNumber_Object = MibTableColumn
acSonetVTDayIntervalNumber = _AcSonetVTDayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 2, 1, 5),
    _AcSonetVTDayIntervalNumber_Type()
)
acSonetVTDayIntervalNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetVTDayIntervalNumber.setStatus("current")


class _AcSonetVTDayIntervalStatus_Type(Integer32):
    """Custom type acSonetVTDayIntervalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 192),
    )


_AcSonetVTDayIntervalStatus_Type.__name__ = "Integer32"
_AcSonetVTDayIntervalStatus_Object = MibTableColumn
acSonetVTDayIntervalStatus = _AcSonetVTDayIntervalStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 2, 1, 6),
    _AcSonetVTDayIntervalStatus_Type()
)
acSonetVTDayIntervalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetVTDayIntervalStatus.setStatus("current")
_AcSonetVTDayIntervalValidStats_Type = TruthValue
_AcSonetVTDayIntervalValidStats_Object = MibTableColumn
acSonetVTDayIntervalValidStats = _AcSonetVTDayIntervalValidStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 2, 1, 7),
    _AcSonetVTDayIntervalValidStats_Type()
)
acSonetVTDayIntervalValidStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetVTDayIntervalValidStats.setStatus("current")
_AcSonetVTDayIntervalResetStats_Type = TruthValue
_AcSonetVTDayIntervalResetStats_Object = MibTableColumn
acSonetVTDayIntervalResetStats = _AcSonetVTDayIntervalResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 2, 1, 8),
    _AcSonetVTDayIntervalResetStats_Type()
)
acSonetVTDayIntervalResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetVTDayIntervalResetStats.setStatus("current")
_AcSonetVTDayIntervalESs_Type = PerfIntervalCount
_AcSonetVTDayIntervalESs_Object = MibTableColumn
acSonetVTDayIntervalESs = _AcSonetVTDayIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 2, 1, 9),
    _AcSonetVTDayIntervalESs_Type()
)
acSonetVTDayIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetVTDayIntervalESs.setStatus("current")
_AcSonetVTDayIntervalSESs_Type = PerfIntervalCount
_AcSonetVTDayIntervalSESs_Object = MibTableColumn
acSonetVTDayIntervalSESs = _AcSonetVTDayIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 2, 1, 10),
    _AcSonetVTDayIntervalSESs_Type()
)
acSonetVTDayIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetVTDayIntervalSESs.setStatus("current")
_AcSonetVTDayIntervalCVs_Type = PerfIntervalCount
_AcSonetVTDayIntervalCVs_Object = MibTableColumn
acSonetVTDayIntervalCVs = _AcSonetVTDayIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 2, 1, 11),
    _AcSonetVTDayIntervalCVs_Type()
)
acSonetVTDayIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetVTDayIntervalCVs.setStatus("current")
_AcSonetVTDayIntervalUASs_Type = PerfIntervalCount
_AcSonetVTDayIntervalUASs_Object = MibTableColumn
acSonetVTDayIntervalUASs = _AcSonetVTDayIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 2, 1, 12),
    _AcSonetVTDayIntervalUASs_Type()
)
acSonetVTDayIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetVTDayIntervalUASs.setStatus("current")
_AcSonetVTDayIntervalBER_Type = PerfIntervalCount
_AcSonetVTDayIntervalBER_Object = MibTableColumn
acSonetVTDayIntervalBER = _AcSonetVTDayIntervalBER_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 2, 1, 13),
    _AcSonetVTDayIntervalBER_Type()
)
acSonetVTDayIntervalBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetVTDayIntervalBER.setStatus("deprecated")
_AcSonetVTThresholdTable_Object = MibTable
acSonetVTThresholdTable = _AcSonetVTThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 3)
)
if mibBuilder.loadTexts:
    acSonetVTThresholdTable.setStatus("current")
_AcSonetVTThresholdEntry_Object = MibTableRow
acSonetVTThresholdEntry = _AcSonetVTThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 3, 1)
)
acSonetVTThresholdEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetVTThresholdNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetVTThresholdSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetVTThresholdPort"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetVTThresholdVT"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetVTThresholdSelectionNum"),
)
if mibBuilder.loadTexts:
    acSonetVTThresholdEntry.setStatus("current")
_AcSonetVTThresholdNodeId_Type = AcNodeId
_AcSonetVTThresholdNodeId_Object = MibTableColumn
acSonetVTThresholdNodeId = _AcSonetVTThresholdNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 3, 1, 1),
    _AcSonetVTThresholdNodeId_Type()
)
acSonetVTThresholdNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetVTThresholdNodeId.setStatus("current")
_AcSonetVTThresholdSlot_Type = AcSlotNumber
_AcSonetVTThresholdSlot_Object = MibTableColumn
acSonetVTThresholdSlot = _AcSonetVTThresholdSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 3, 1, 2),
    _AcSonetVTThresholdSlot_Type()
)
acSonetVTThresholdSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetVTThresholdSlot.setStatus("current")
_AcSonetVTThresholdPort_Type = AcPortNumber
_AcSonetVTThresholdPort_Object = MibTableColumn
acSonetVTThresholdPort = _AcSonetVTThresholdPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 3, 1, 3),
    _AcSonetVTThresholdPort_Type()
)
acSonetVTThresholdPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetVTThresholdPort.setStatus("current")
_AcSonetVTThresholdVT_Type = Integer32
_AcSonetVTThresholdVT_Object = MibTableColumn
acSonetVTThresholdVT = _AcSonetVTThresholdVT_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 3, 1, 4),
    _AcSonetVTThresholdVT_Type()
)
acSonetVTThresholdVT.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetVTThresholdVT.setStatus("current")


class _AcSonetVTThresholdSelectionNum_Type(Integer32):
    """Custom type acSonetVTThresholdSelectionNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("day", 2),
          ("minute", 1))
    )


_AcSonetVTThresholdSelectionNum_Type.__name__ = "Integer32"
_AcSonetVTThresholdSelectionNum_Object = MibTableColumn
acSonetVTThresholdSelectionNum = _AcSonetVTThresholdSelectionNum_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 3, 1, 5),
    _AcSonetVTThresholdSelectionNum_Type()
)
acSonetVTThresholdSelectionNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetVTThresholdSelectionNum.setStatus("current")
_AcSonetVTThresholdAdminStatus_Type = AcAdminStatus
_AcSonetVTThresholdAdminStatus_Object = MibTableColumn
acSonetVTThresholdAdminStatus = _AcSonetVTThresholdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 3, 1, 6),
    _AcSonetVTThresholdAdminStatus_Type()
)
acSonetVTThresholdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetVTThresholdAdminStatus.setStatus("deprecated")


class _AcSonetVTThresholdESs_Type(Integer32):
    """Custom type acSonetVTThresholdESs based on Integer32"""
    defaultValue = 0


_AcSonetVTThresholdESs_Object = MibTableColumn
acSonetVTThresholdESs = _AcSonetVTThresholdESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 3, 1, 7),
    _AcSonetVTThresholdESs_Type()
)
acSonetVTThresholdESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetVTThresholdESs.setStatus("current")


class _AcSonetVTThresholdSESs_Type(Integer32):
    """Custom type acSonetVTThresholdSESs based on Integer32"""
    defaultValue = 0


_AcSonetVTThresholdSESs_Object = MibTableColumn
acSonetVTThresholdSESs = _AcSonetVTThresholdSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 3, 1, 8),
    _AcSonetVTThresholdSESs_Type()
)
acSonetVTThresholdSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetVTThresholdSESs.setStatus("current")


class _AcSonetVTThresholdCVs_Type(Integer32):
    """Custom type acSonetVTThresholdCVs based on Integer32"""
    defaultValue = 0


_AcSonetVTThresholdCVs_Object = MibTableColumn
acSonetVTThresholdCVs = _AcSonetVTThresholdCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 3, 1, 9),
    _AcSonetVTThresholdCVs_Type()
)
acSonetVTThresholdCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetVTThresholdCVs.setStatus("current")


class _AcSonetVTThresholdUASs_Type(Integer32):
    """Custom type acSonetVTThresholdUASs based on Integer32"""
    defaultValue = 0


_AcSonetVTThresholdUASs_Object = MibTableColumn
acSonetVTThresholdUASs = _AcSonetVTThresholdUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 3, 1, 10),
    _AcSonetVTThresholdUASs_Type()
)
acSonetVTThresholdUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetVTThresholdUASs.setStatus("current")
_AcSonetVTRDITable_Object = MibTable
acSonetVTRDITable = _AcSonetVTRDITable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 4)
)
if mibBuilder.loadTexts:
    acSonetVTRDITable.setStatus("current")
_AcSonetVTRDIEntry_Object = MibTableRow
acSonetVTRDIEntry = _AcSonetVTRDIEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 4, 1)
)
acSonetVTRDIEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetVTRDINodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetVTRDISlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetVTRDIPort"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetVTRDIVT"),
)
if mibBuilder.loadTexts:
    acSonetVTRDIEntry.setStatus("current")
_AcSonetVTRDINodeId_Type = AcNodeId
_AcSonetVTRDINodeId_Object = MibTableColumn
acSonetVTRDINodeId = _AcSonetVTRDINodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 4, 1, 1),
    _AcSonetVTRDINodeId_Type()
)
acSonetVTRDINodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetVTRDINodeId.setStatus("current")
_AcSonetVTRDISlot_Type = AcSlotNumber
_AcSonetVTRDISlot_Object = MibTableColumn
acSonetVTRDISlot = _AcSonetVTRDISlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 4, 1, 2),
    _AcSonetVTRDISlot_Type()
)
acSonetVTRDISlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetVTRDISlot.setStatus("current")
_AcSonetVTRDIPort_Type = AcPortNumber
_AcSonetVTRDIPort_Object = MibTableColumn
acSonetVTRDIPort = _AcSonetVTRDIPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 4, 1, 3),
    _AcSonetVTRDIPort_Type()
)
acSonetVTRDIPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetVTRDIPort.setStatus("current")
_AcSonetVTRDIVT_Type = Integer32
_AcSonetVTRDIVT_Object = MibTableColumn
acSonetVTRDIVT = _AcSonetVTRDIVT_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 4, 1, 4),
    _AcSonetVTRDIVT_Type()
)
acSonetVTRDIVT.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetVTRDIVT.setStatus("current")


class _AcSonetVTRDIOpMode_Type(Integer32):
    """Custom type acSonetVTRDIOpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("erdi", 2),
          ("rdi", 1))
    )


_AcSonetVTRDIOpMode_Type.__name__ = "Integer32"
_AcSonetVTRDIOpMode_Object = MibTableColumn
acSonetVTRDIOpMode = _AcSonetVTRDIOpMode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 4, 1, 5),
    _AcSonetVTRDIOpMode_Type()
)
acSonetVTRDIOpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetVTRDIOpMode.setStatus("current")
_AcSonetVTPLMTable_Object = MibTable
acSonetVTPLMTable = _AcSonetVTPLMTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 5)
)
if mibBuilder.loadTexts:
    acSonetVTPLMTable.setStatus("current")
_AcSonetVTPLMEntry_Object = MibTableRow
acSonetVTPLMEntry = _AcSonetVTPLMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 5, 1)
)
acSonetVTPLMEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetVTPLMNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetVTPLMSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetVTPLMPort"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetVTPLMVT"),
)
if mibBuilder.loadTexts:
    acSonetVTPLMEntry.setStatus("current")
_AcSonetVTPLMNodeId_Type = AcNodeId
_AcSonetVTPLMNodeId_Object = MibTableColumn
acSonetVTPLMNodeId = _AcSonetVTPLMNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 5, 1, 1),
    _AcSonetVTPLMNodeId_Type()
)
acSonetVTPLMNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetVTPLMNodeId.setStatus("current")
_AcSonetVTPLMSlot_Type = AcSlotNumber
_AcSonetVTPLMSlot_Object = MibTableColumn
acSonetVTPLMSlot = _AcSonetVTPLMSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 5, 1, 2),
    _AcSonetVTPLMSlot_Type()
)
acSonetVTPLMSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetVTPLMSlot.setStatus("current")
_AcSonetVTPLMPort_Type = AcPortNumber
_AcSonetVTPLMPort_Object = MibTableColumn
acSonetVTPLMPort = _AcSonetVTPLMPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 5, 1, 3),
    _AcSonetVTPLMPort_Type()
)
acSonetVTPLMPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetVTPLMPort.setStatus("current")
_AcSonetVTPLMVT_Type = Integer32
_AcSonetVTPLMVT_Object = MibTableColumn
acSonetVTPLMVT = _AcSonetVTPLMVT_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 5, 1, 4),
    _AcSonetVTPLMVT_Type()
)
acSonetVTPLMVT.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetVTPLMVT.setStatus("current")


class _AcSonetVTPLMDetectEnable_Type(TruthValue):
    """Custom type acSonetVTPLMDetectEnable based on TruthValue"""


_AcSonetVTPLMDetectEnable_Object = MibTableColumn
acSonetVTPLMDetectEnable = _AcSonetVTPLMDetectEnable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 5, 1, 5),
    _AcSonetVTPLMDetectEnable_Type()
)
acSonetVTPLMDetectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetVTPLMDetectEnable.setStatus("current")


class _AcSonetVTPLMTransmitedValue_Type(Integer32):
    """Custom type acSonetVTPLMTransmitedValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcSonetVTPLMTransmitedValue_Type.__name__ = "Integer32"
_AcSonetVTPLMTransmitedValue_Object = MibTableColumn
acSonetVTPLMTransmitedValue = _AcSonetVTPLMTransmitedValue_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 5, 1, 6),
    _AcSonetVTPLMTransmitedValue_Type()
)
acSonetVTPLMTransmitedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetVTPLMTransmitedValue.setStatus("current")


class _AcSonetVTPLMExpectedValue_Type(Integer32):
    """Custom type acSonetVTPLMExpectedValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcSonetVTPLMExpectedValue_Type.__name__ = "Integer32"
_AcSonetVTPLMExpectedValue_Object = MibTableColumn
acSonetVTPLMExpectedValue = _AcSonetVTPLMExpectedValue_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 5, 1, 7),
    _AcSonetVTPLMExpectedValue_Type()
)
acSonetVTPLMExpectedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetVTPLMExpectedValue.setStatus("current")
_AcSonetVTPLMReceivedValue_Type = Integer32
_AcSonetVTPLMReceivedValue_Object = MibTableColumn
acSonetVTPLMReceivedValue = _AcSonetVTPLMReceivedValue_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 5, 1, 8),
    _AcSonetVTPLMReceivedValue_Type()
)
acSonetVTPLMReceivedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetVTPLMReceivedValue.setStatus("current")
_AcSonetVTPLMMismatchFailure_Type = TruthValue
_AcSonetVTPLMMismatchFailure_Object = MibTableColumn
acSonetVTPLMMismatchFailure = _AcSonetVTPLMMismatchFailure_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 5, 1, 9),
    _AcSonetVTPLMMismatchFailure_Type()
)
acSonetVTPLMMismatchFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetVTPLMMismatchFailure.setStatus("current")
_AcSonetVTPLMUnequipped_Type = TruthValue
_AcSonetVTPLMUnequipped_Object = MibTableColumn
acSonetVTPLMUnequipped = _AcSonetVTPLMUnequipped_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 5, 1, 10),
    _AcSonetVTPLMUnequipped_Type()
)
acSonetVTPLMUnequipped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetVTPLMUnequipped.setStatus("current")
_AcSonetVTProtectionTable_Object = MibTable
acSonetVTProtectionTable = _AcSonetVTProtectionTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 6)
)
if mibBuilder.loadTexts:
    acSonetVTProtectionTable.setStatus("current")
_AcSonetVTProtectionEntry_Object = MibTableRow
acSonetVTProtectionEntry = _AcSonetVTProtectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 6, 1)
)
acSonetVTProtectionEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetVTProtectionNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetVTProtectionSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetVTProtectionPort"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetVTProtectionVT"),
)
if mibBuilder.loadTexts:
    acSonetVTProtectionEntry.setStatus("current")
_AcSonetVTProtectionNodeId_Type = AcNodeId
_AcSonetVTProtectionNodeId_Object = MibTableColumn
acSonetVTProtectionNodeId = _AcSonetVTProtectionNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 6, 1, 1),
    _AcSonetVTProtectionNodeId_Type()
)
acSonetVTProtectionNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetVTProtectionNodeId.setStatus("current")
_AcSonetVTProtectionSlot_Type = AcSlotNumber
_AcSonetVTProtectionSlot_Object = MibTableColumn
acSonetVTProtectionSlot = _AcSonetVTProtectionSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 6, 1, 2),
    _AcSonetVTProtectionSlot_Type()
)
acSonetVTProtectionSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetVTProtectionSlot.setStatus("current")
_AcSonetVTProtectionPort_Type = AcPortNumber
_AcSonetVTProtectionPort_Object = MibTableColumn
acSonetVTProtectionPort = _AcSonetVTProtectionPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 6, 1, 3),
    _AcSonetVTProtectionPort_Type()
)
acSonetVTProtectionPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetVTProtectionPort.setStatus("current")
_AcSonetVTProtectionVT_Type = Integer32
_AcSonetVTProtectionVT_Object = MibTableColumn
acSonetVTProtectionVT = _AcSonetVTProtectionVT_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 6, 1, 4),
    _AcSonetVTProtectionVT_Type()
)
acSonetVTProtectionVT.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetVTProtectionVT.setStatus("current")


class _AcSonetVTProtectionSwitchType_Type(Integer32):
    """Custom type acSonetVTProtectionSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonrevertive", 2),
          ("revertive", 1))
    )


_AcSonetVTProtectionSwitchType_Type.__name__ = "Integer32"
_AcSonetVTProtectionSwitchType_Object = MibTableColumn
acSonetVTProtectionSwitchType = _AcSonetVTProtectionSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 6, 1, 5),
    _AcSonetVTProtectionSwitchType_Type()
)
acSonetVTProtectionSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetVTProtectionSwitchType.setStatus("current")


class _AcSonetVTProtectionSFThreshold_Type(Integer32):
    """Custom type acSonetVTProtectionSFThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 5),
    )


_AcSonetVTProtectionSFThreshold_Type.__name__ = "Integer32"
_AcSonetVTProtectionSFThreshold_Object = MibTableColumn
acSonetVTProtectionSFThreshold = _AcSonetVTProtectionSFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 6, 1, 6),
    _AcSonetVTProtectionSFThreshold_Type()
)
acSonetVTProtectionSFThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetVTProtectionSFThreshold.setStatus("current")


class _AcSonetVTProtectionSDThreshold_Type(Integer32):
    """Custom type acSonetVTProtectionSDThreshold based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 8),
    )


_AcSonetVTProtectionSDThreshold_Type.__name__ = "Integer32"
_AcSonetVTProtectionSDThreshold_Object = MibTableColumn
acSonetVTProtectionSDThreshold = _AcSonetVTProtectionSDThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 6, 1, 7),
    _AcSonetVTProtectionSDThreshold_Type()
)
acSonetVTProtectionSDThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetVTProtectionSDThreshold.setStatus("current")
_AcSonetVTProtectionProtectionSwitch_Type = TruthValue
_AcSonetVTProtectionProtectionSwitch_Object = MibTableColumn
acSonetVTProtectionProtectionSwitch = _AcSonetVTProtectionProtectionSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 6, 1, 8),
    _AcSonetVTProtectionProtectionSwitch_Type()
)
acSonetVTProtectionProtectionSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetVTProtectionProtectionSwitch.setStatus("current")


class _AcSonetVTProtectionWTRTime_Type(Integer32):
    """Custom type acSonetVTProtectionWTRTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 720),
    )


_AcSonetVTProtectionWTRTime_Type.__name__ = "Integer32"
_AcSonetVTProtectionWTRTime_Object = MibTableColumn
acSonetVTProtectionWTRTime = _AcSonetVTProtectionWTRTime_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 6, 1, 9),
    _AcSonetVTProtectionWTRTime_Type()
)
acSonetVTProtectionWTRTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetVTProtectionWTRTime.setStatus("current")


class _AcSonetVTProtectionManSwitch_Type(Integer32):
    """Custom type acSonetVTProtectionManSwitch based on Integer32"""
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
        *(("clear", 1),
          ("force-protection", 4),
          ("force-working", 3),
          ("lockout-protection", 2),
          ("manual-protection", 6),
          ("manual-working", 5))
    )


_AcSonetVTProtectionManSwitch_Type.__name__ = "Integer32"
_AcSonetVTProtectionManSwitch_Object = MibTableColumn
acSonetVTProtectionManSwitch = _AcSonetVTProtectionManSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 6, 1, 10),
    _AcSonetVTProtectionManSwitch_Type()
)
acSonetVTProtectionManSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetVTProtectionManSwitch.setStatus("current")
_AcSonetVTProtectionActiveTraffic_Type = TruthValue
_AcSonetVTProtectionActiveTraffic_Object = MibTableColumn
acSonetVTProtectionActiveTraffic = _AcSonetVTProtectionActiveTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 6, 1, 11),
    _AcSonetVTProtectionActiveTraffic_Type()
)
acSonetVTProtectionActiveTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetVTProtectionActiveTraffic.setStatus("current")
_AcSonetFarEndVT_ObjectIdentity = ObjectIdentity
acSonetFarEndVT = _AcSonetFarEndVT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2)
)
_AcSonetFarEndVT15MinuteIntervalTable_Object = MibTable
acSonetFarEndVT15MinuteIntervalTable = _AcSonetFarEndVT15MinuteIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 1)
)
if mibBuilder.loadTexts:
    acSonetFarEndVT15MinuteIntervalTable.setStatus("current")
_AcSonetFarEndVT15MinuteIntervalEntry_Object = MibTableRow
acSonetFarEndVT15MinuteIntervalEntry = _AcSonetFarEndVT15MinuteIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 1, 1)
)
acSonetFarEndVT15MinuteIntervalEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalPort"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalVT"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalNumber"),
)
if mibBuilder.loadTexts:
    acSonetFarEndVT15MinuteIntervalEntry.setStatus("current")
_AcSonetFarEndVT15MinuteIntervalNodeId_Type = AcNodeId
_AcSonetFarEndVT15MinuteIntervalNodeId_Object = MibTableColumn
acSonetFarEndVT15MinuteIntervalNodeId = _AcSonetFarEndVT15MinuteIntervalNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 1, 1, 1),
    _AcSonetFarEndVT15MinuteIntervalNodeId_Type()
)
acSonetFarEndVT15MinuteIntervalNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndVT15MinuteIntervalNodeId.setStatus("current")
_AcSonetFarEndVT15MinuteIntervalSlot_Type = AcSlotNumber
_AcSonetFarEndVT15MinuteIntervalSlot_Object = MibTableColumn
acSonetFarEndVT15MinuteIntervalSlot = _AcSonetFarEndVT15MinuteIntervalSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 1, 1, 2),
    _AcSonetFarEndVT15MinuteIntervalSlot_Type()
)
acSonetFarEndVT15MinuteIntervalSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndVT15MinuteIntervalSlot.setStatus("current")
_AcSonetFarEndVT15MinuteIntervalPort_Type = AcPortNumber
_AcSonetFarEndVT15MinuteIntervalPort_Object = MibTableColumn
acSonetFarEndVT15MinuteIntervalPort = _AcSonetFarEndVT15MinuteIntervalPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 1, 1, 3),
    _AcSonetFarEndVT15MinuteIntervalPort_Type()
)
acSonetFarEndVT15MinuteIntervalPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndVT15MinuteIntervalPort.setStatus("current")
_AcSonetFarEndVT15MinuteIntervalVT_Type = Integer32
_AcSonetFarEndVT15MinuteIntervalVT_Object = MibTableColumn
acSonetFarEndVT15MinuteIntervalVT = _AcSonetFarEndVT15MinuteIntervalVT_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 1, 1, 4),
    _AcSonetFarEndVT15MinuteIntervalVT_Type()
)
acSonetFarEndVT15MinuteIntervalVT.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndVT15MinuteIntervalVT.setStatus("current")


class _AcSonetFarEndVT15MinuteIntervalNumber_Type(Integer32):
    """Custom type acSonetFarEndVT15MinuteIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 98),
    )


_AcSonetFarEndVT15MinuteIntervalNumber_Type.__name__ = "Integer32"
_AcSonetFarEndVT15MinuteIntervalNumber_Object = MibTableColumn
acSonetFarEndVT15MinuteIntervalNumber = _AcSonetFarEndVT15MinuteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 1, 1, 5),
    _AcSonetFarEndVT15MinuteIntervalNumber_Type()
)
acSonetFarEndVT15MinuteIntervalNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndVT15MinuteIntervalNumber.setStatus("current")
_AcSonetFarEndVT15MinuteIntervalValidStats_Type = TruthValue
_AcSonetFarEndVT15MinuteIntervalValidStats_Object = MibTableColumn
acSonetFarEndVT15MinuteIntervalValidStats = _AcSonetFarEndVT15MinuteIntervalValidStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 1, 1, 6),
    _AcSonetFarEndVT15MinuteIntervalValidStats_Type()
)
acSonetFarEndVT15MinuteIntervalValidStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetFarEndVT15MinuteIntervalValidStats.setStatus("current")
_AcSonetFarEndVT15MinuteIntervalResetStats_Type = TruthValue
_AcSonetFarEndVT15MinuteIntervalResetStats_Object = MibTableColumn
acSonetFarEndVT15MinuteIntervalResetStats = _AcSonetFarEndVT15MinuteIntervalResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 1, 1, 7),
    _AcSonetFarEndVT15MinuteIntervalResetStats_Type()
)
acSonetFarEndVT15MinuteIntervalResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetFarEndVT15MinuteIntervalResetStats.setStatus("current")
_AcSonetFarEndVT15MinuteIntervalESs_Type = PerfIntervalCount
_AcSonetFarEndVT15MinuteIntervalESs_Object = MibTableColumn
acSonetFarEndVT15MinuteIntervalESs = _AcSonetFarEndVT15MinuteIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 1, 1, 8),
    _AcSonetFarEndVT15MinuteIntervalESs_Type()
)
acSonetFarEndVT15MinuteIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetFarEndVT15MinuteIntervalESs.setStatus("current")
_AcSonetFarEndVT15MinuteIntervalSESs_Type = PerfIntervalCount
_AcSonetFarEndVT15MinuteIntervalSESs_Object = MibTableColumn
acSonetFarEndVT15MinuteIntervalSESs = _AcSonetFarEndVT15MinuteIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 1, 1, 9),
    _AcSonetFarEndVT15MinuteIntervalSESs_Type()
)
acSonetFarEndVT15MinuteIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetFarEndVT15MinuteIntervalSESs.setStatus("current")
_AcSonetFarEndVT15MinuteIntervalCVs_Type = PerfIntervalCount
_AcSonetFarEndVT15MinuteIntervalCVs_Object = MibTableColumn
acSonetFarEndVT15MinuteIntervalCVs = _AcSonetFarEndVT15MinuteIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 1, 1, 10),
    _AcSonetFarEndVT15MinuteIntervalCVs_Type()
)
acSonetFarEndVT15MinuteIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetFarEndVT15MinuteIntervalCVs.setStatus("current")
_AcSonetFarEndVT15MinuteIntervalUASs_Type = PerfIntervalCount
_AcSonetFarEndVT15MinuteIntervalUASs_Object = MibTableColumn
acSonetFarEndVT15MinuteIntervalUASs = _AcSonetFarEndVT15MinuteIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 1, 1, 11),
    _AcSonetFarEndVT15MinuteIntervalUASs_Type()
)
acSonetFarEndVT15MinuteIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetFarEndVT15MinuteIntervalUASs.setStatus("current")
_AcSonetFarEndVTDayIntervalTable_Object = MibTable
acSonetFarEndVTDayIntervalTable = _AcSonetFarEndVTDayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 2)
)
if mibBuilder.loadTexts:
    acSonetFarEndVTDayIntervalTable.setStatus("current")
_AcSonetFarEndVTDayIntervalEntry_Object = MibTableRow
acSonetFarEndVTDayIntervalEntry = _AcSonetFarEndVTDayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 2, 1)
)
acSonetFarEndVTDayIntervalEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalPort"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalVT"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalNumber"),
)
if mibBuilder.loadTexts:
    acSonetFarEndVTDayIntervalEntry.setStatus("current")
_AcSonetFarEndVTDayIntervalNodeId_Type = AcNodeId
_AcSonetFarEndVTDayIntervalNodeId_Object = MibTableColumn
acSonetFarEndVTDayIntervalNodeId = _AcSonetFarEndVTDayIntervalNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 2, 1, 1),
    _AcSonetFarEndVTDayIntervalNodeId_Type()
)
acSonetFarEndVTDayIntervalNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndVTDayIntervalNodeId.setStatus("current")
_AcSonetFarEndVTDayIntervalSlot_Type = AcSlotNumber
_AcSonetFarEndVTDayIntervalSlot_Object = MibTableColumn
acSonetFarEndVTDayIntervalSlot = _AcSonetFarEndVTDayIntervalSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 2, 1, 2),
    _AcSonetFarEndVTDayIntervalSlot_Type()
)
acSonetFarEndVTDayIntervalSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndVTDayIntervalSlot.setStatus("current")
_AcSonetFarEndVTDayIntervalPort_Type = AcPortNumber
_AcSonetFarEndVTDayIntervalPort_Object = MibTableColumn
acSonetFarEndVTDayIntervalPort = _AcSonetFarEndVTDayIntervalPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 2, 1, 3),
    _AcSonetFarEndVTDayIntervalPort_Type()
)
acSonetFarEndVTDayIntervalPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndVTDayIntervalPort.setStatus("current")
_AcSonetFarEndVTDayIntervalVT_Type = Integer32
_AcSonetFarEndVTDayIntervalVT_Object = MibTableColumn
acSonetFarEndVTDayIntervalVT = _AcSonetFarEndVTDayIntervalVT_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 2, 1, 4),
    _AcSonetFarEndVTDayIntervalVT_Type()
)
acSonetFarEndVTDayIntervalVT.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndVTDayIntervalVT.setStatus("current")


class _AcSonetFarEndVTDayIntervalNumber_Type(Integer32):
    """Custom type acSonetFarEndVTDayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_AcSonetFarEndVTDayIntervalNumber_Type.__name__ = "Integer32"
_AcSonetFarEndVTDayIntervalNumber_Object = MibTableColumn
acSonetFarEndVTDayIntervalNumber = _AcSonetFarEndVTDayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 2, 1, 5),
    _AcSonetFarEndVTDayIntervalNumber_Type()
)
acSonetFarEndVTDayIntervalNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndVTDayIntervalNumber.setStatus("current")
_AcSonetFarEndVTDayIntervalValidStats_Type = TruthValue
_AcSonetFarEndVTDayIntervalValidStats_Object = MibTableColumn
acSonetFarEndVTDayIntervalValidStats = _AcSonetFarEndVTDayIntervalValidStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 2, 1, 6),
    _AcSonetFarEndVTDayIntervalValidStats_Type()
)
acSonetFarEndVTDayIntervalValidStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetFarEndVTDayIntervalValidStats.setStatus("current")
_AcSonetFarEndVTDayIntervalResetStats_Type = TruthValue
_AcSonetFarEndVTDayIntervalResetStats_Object = MibTableColumn
acSonetFarEndVTDayIntervalResetStats = _AcSonetFarEndVTDayIntervalResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 2, 1, 7),
    _AcSonetFarEndVTDayIntervalResetStats_Type()
)
acSonetFarEndVTDayIntervalResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetFarEndVTDayIntervalResetStats.setStatus("current")
_AcSonetFarEndVTDayIntervalESs_Type = PerfIntervalCount
_AcSonetFarEndVTDayIntervalESs_Object = MibTableColumn
acSonetFarEndVTDayIntervalESs = _AcSonetFarEndVTDayIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 2, 1, 8),
    _AcSonetFarEndVTDayIntervalESs_Type()
)
acSonetFarEndVTDayIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetFarEndVTDayIntervalESs.setStatus("current")
_AcSonetFarEndVTDayIntervalSESs_Type = PerfIntervalCount
_AcSonetFarEndVTDayIntervalSESs_Object = MibTableColumn
acSonetFarEndVTDayIntervalSESs = _AcSonetFarEndVTDayIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 2, 1, 9),
    _AcSonetFarEndVTDayIntervalSESs_Type()
)
acSonetFarEndVTDayIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetFarEndVTDayIntervalSESs.setStatus("current")
_AcSonetFarEndVTDayIntervalCVs_Type = PerfIntervalCount
_AcSonetFarEndVTDayIntervalCVs_Object = MibTableColumn
acSonetFarEndVTDayIntervalCVs = _AcSonetFarEndVTDayIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 2, 1, 10),
    _AcSonetFarEndVTDayIntervalCVs_Type()
)
acSonetFarEndVTDayIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetFarEndVTDayIntervalCVs.setStatus("current")
_AcSonetFarEndVTDayIntervalUASs_Type = PerfIntervalCount
_AcSonetFarEndVTDayIntervalUASs_Object = MibTableColumn
acSonetFarEndVTDayIntervalUASs = _AcSonetFarEndVTDayIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 2, 1, 11),
    _AcSonetFarEndVTDayIntervalUASs_Type()
)
acSonetFarEndVTDayIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSonetFarEndVTDayIntervalUASs.setStatus("current")
_AcSonetFarEndVTThresholdTable_Object = MibTable
acSonetFarEndVTThresholdTable = _AcSonetFarEndVTThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 3)
)
if mibBuilder.loadTexts:
    acSonetFarEndVTThresholdTable.setStatus("current")
_AcSonetFarEndVTThresholdEntry_Object = MibTableRow
acSonetFarEndVTThresholdEntry = _AcSonetFarEndVTThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 3, 1)
)
acSonetFarEndVTThresholdEntry.setIndexNames(
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTThresholdNodeId"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTThresholdSlot"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTThresholdPort"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTThresholdVT"),
    (0, "APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTThresholdSelectionNum"),
)
if mibBuilder.loadTexts:
    acSonetFarEndVTThresholdEntry.setStatus("current")
_AcSonetFarEndVTThresholdNodeId_Type = AcNodeId
_AcSonetFarEndVTThresholdNodeId_Object = MibTableColumn
acSonetFarEndVTThresholdNodeId = _AcSonetFarEndVTThresholdNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 3, 1, 1),
    _AcSonetFarEndVTThresholdNodeId_Type()
)
acSonetFarEndVTThresholdNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndVTThresholdNodeId.setStatus("current")
_AcSonetFarEndVTThresholdSlot_Type = AcSlotNumber
_AcSonetFarEndVTThresholdSlot_Object = MibTableColumn
acSonetFarEndVTThresholdSlot = _AcSonetFarEndVTThresholdSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 3, 1, 2),
    _AcSonetFarEndVTThresholdSlot_Type()
)
acSonetFarEndVTThresholdSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndVTThresholdSlot.setStatus("current")
_AcSonetFarEndVTThresholdPort_Type = AcPortNumber
_AcSonetFarEndVTThresholdPort_Object = MibTableColumn
acSonetFarEndVTThresholdPort = _AcSonetFarEndVTThresholdPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 3, 1, 3),
    _AcSonetFarEndVTThresholdPort_Type()
)
acSonetFarEndVTThresholdPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndVTThresholdPort.setStatus("current")
_AcSonetFarEndVTThresholdVT_Type = Integer32
_AcSonetFarEndVTThresholdVT_Object = MibTableColumn
acSonetFarEndVTThresholdVT = _AcSonetFarEndVTThresholdVT_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 3, 1, 4),
    _AcSonetFarEndVTThresholdVT_Type()
)
acSonetFarEndVTThresholdVT.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndVTThresholdVT.setStatus("current")


class _AcSonetFarEndVTThresholdSelectionNum_Type(Integer32):
    """Custom type acSonetFarEndVTThresholdSelectionNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("day", 2),
          ("minute", 1))
    )


_AcSonetFarEndVTThresholdSelectionNum_Type.__name__ = "Integer32"
_AcSonetFarEndVTThresholdSelectionNum_Object = MibTableColumn
acSonetFarEndVTThresholdSelectionNum = _AcSonetFarEndVTThresholdSelectionNum_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 3, 1, 5),
    _AcSonetFarEndVTThresholdSelectionNum_Type()
)
acSonetFarEndVTThresholdSelectionNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSonetFarEndVTThresholdSelectionNum.setStatus("current")
_AcSonetFarEndVTThresholdAdminStatus_Type = AcAdminStatus
_AcSonetFarEndVTThresholdAdminStatus_Object = MibTableColumn
acSonetFarEndVTThresholdAdminStatus = _AcSonetFarEndVTThresholdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 3, 1, 6),
    _AcSonetFarEndVTThresholdAdminStatus_Type()
)
acSonetFarEndVTThresholdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetFarEndVTThresholdAdminStatus.setStatus("deprecated")


class _AcSonetFarEndVTThresholdESs_Type(Integer32):
    """Custom type acSonetFarEndVTThresholdESs based on Integer32"""
    defaultValue = 0


_AcSonetFarEndVTThresholdESs_Object = MibTableColumn
acSonetFarEndVTThresholdESs = _AcSonetFarEndVTThresholdESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 3, 1, 7),
    _AcSonetFarEndVTThresholdESs_Type()
)
acSonetFarEndVTThresholdESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetFarEndVTThresholdESs.setStatus("current")


class _AcSonetFarEndVTThresholdSESs_Type(Integer32):
    """Custom type acSonetFarEndVTThresholdSESs based on Integer32"""
    defaultValue = 0


_AcSonetFarEndVTThresholdSESs_Object = MibTableColumn
acSonetFarEndVTThresholdSESs = _AcSonetFarEndVTThresholdSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 3, 1, 8),
    _AcSonetFarEndVTThresholdSESs_Type()
)
acSonetFarEndVTThresholdSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetFarEndVTThresholdSESs.setStatus("current")


class _AcSonetFarEndVTThresholdCVs_Type(Integer32):
    """Custom type acSonetFarEndVTThresholdCVs based on Integer32"""
    defaultValue = 0


_AcSonetFarEndVTThresholdCVs_Object = MibTableColumn
acSonetFarEndVTThresholdCVs = _AcSonetFarEndVTThresholdCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 3, 1, 9),
    _AcSonetFarEndVTThresholdCVs_Type()
)
acSonetFarEndVTThresholdCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetFarEndVTThresholdCVs.setStatus("current")


class _AcSonetFarEndVTThresholdUASs_Type(Integer32):
    """Custom type acSonetFarEndVTThresholdUASs based on Integer32"""
    defaultValue = 0


_AcSonetFarEndVTThresholdUASs_Object = MibTableColumn
acSonetFarEndVTThresholdUASs = _AcSonetFarEndVTThresholdUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 3, 1, 10),
    _AcSonetFarEndVTThresholdUASs_Type()
)
acSonetFarEndVTThresholdUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSonetFarEndVTThresholdUASs.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPIAN-PPORT-SONET-MIB",
    **{"AcTraceString": AcTraceString,
       "acSonet": acSonet,
       "acSonetObjects": acSonetObjects,
       "acSonetPort": acSonetPort,
       "acSonetPortTable": acSonetPortTable,
       "acSonetPortEntry": acSonetPortEntry,
       "acSonetPortNodeId": acSonetPortNodeId,
       "acSonetPortSlot": acSonetPortSlot,
       "acSonetPortPort": acSonetPortPort,
       "acSonetPortAdminStatus": acSonetPortAdminStatus,
       "acSonetPortOpStatus": acSonetPortOpStatus,
       "acSonetPortOpCode": acSonetPortOpCode,
       "acSonetPortMediumType": acSonetPortMediumType,
       "acSonetPortTimeElapsed": acSonetPortTimeElapsed,
       "acSonetPortValidIntervals": acSonetPortValidIntervals,
       "acSonetPortMediumLineCoding": acSonetPortMediumLineCoding,
       "acSonetPortMediumLineType": acSonetPortMediumLineType,
       "acSonetPortTransmitterEnable": acSonetPortTransmitterEnable,
       "acSonetPortCircuitIdentifier": acSonetPortCircuitIdentifier,
       "acSonetPortInvalidIntervals": acSonetPortInvalidIntervals,
       "acSonetPortLoopbackConfig": acSonetPortLoopbackConfig,
       "acSonetPortResetCurrentPMregs": acSonetPortResetCurrentPMregs,
       "acSonetPortResetAllPMregs": acSonetPortResetAllPMregs,
       "acSonetPortConnectionType": acSonetPortConnectionType,
       "acSonetPortRingIdentifier": acSonetPortRingIdentifier,
       "acSonetPortRingName": acSonetPortRingName,
       "acSonetThresholdTable": acSonetThresholdTable,
       "acSonetThresholdEntry": acSonetThresholdEntry,
       "acSonetThresholdNodeId": acSonetThresholdNodeId,
       "acSonetThresholdSlot": acSonetThresholdSlot,
       "acSonetThresholdPort": acSonetThresholdPort,
       "acSonetThresholdSESSet": acSonetThresholdSESSet,
       "acSonetDCCTable": acSonetDCCTable,
       "acSonetDCCEntry": acSonetDCCEntry,
       "acSonetDCCNodeId": acSonetDCCNodeId,
       "acSonetDCCSlot": acSonetDCCSlot,
       "acSonetDCCPort": acSonetDCCPort,
       "acSonetDCCSectionEnable": acSonetDCCSectionEnable,
       "acSonetDCCLineEnable": acSonetDCCLineEnable,
       "acSonetDCCAppianEnable": acSonetDCCAppianEnable,
       "acSonetDCCSectionFail": acSonetDCCSectionFail,
       "acSonetDCCLineFail": acSonetDCCLineFail,
       "acSonetDCCAppianFail": acSonetDCCAppianFail,
       "acSonetPortProtectionTable": acSonetPortProtectionTable,
       "acSonetPortProtectionEntry": acSonetPortProtectionEntry,
       "acSonetPortProtectionNodeId": acSonetPortProtectionNodeId,
       "acSonetPortProtectionSlot": acSonetPortProtectionSlot,
       "acSonetPortProtectionPort": acSonetPortProtectionPort,
       "acSonetPortProtectionType": acSonetPortProtectionType,
       "acSonetSection": acSonetSection,
       "acSonetSection15MinuteIntervalTable": acSonetSection15MinuteIntervalTable,
       "acSonetSection15MinuteIntervalEntry": acSonetSection15MinuteIntervalEntry,
       "acSonetSection15MinuteIntervalNodeId": acSonetSection15MinuteIntervalNodeId,
       "acSonetSection15MinuteIntervalSlot": acSonetSection15MinuteIntervalSlot,
       "acSonetSection15MinuteIntervalPort": acSonetSection15MinuteIntervalPort,
       "acSonetSection15MinuteIntervalNumber": acSonetSection15MinuteIntervalNumber,
       "acSonetSection15MinuteIntervalValidStats": acSonetSection15MinuteIntervalValidStats,
       "acSonetSection15MinuteIntervalResetStats": acSonetSection15MinuteIntervalResetStats,
       "acSonetSection15MinuteIntervalStatus": acSonetSection15MinuteIntervalStatus,
       "acSonetSection15MinuteIntervalESs": acSonetSection15MinuteIntervalESs,
       "acSonetSection15MinuteIntervalSESs": acSonetSection15MinuteIntervalSESs,
       "acSonetSection15MinuteIntervalSEFSs": acSonetSection15MinuteIntervalSEFSs,
       "acSonetSection15MinuteIntervalCVs": acSonetSection15MinuteIntervalCVs,
       "acSonetSectionDayIntervalTable": acSonetSectionDayIntervalTable,
       "acSonetSectionDayIntervalEntry": acSonetSectionDayIntervalEntry,
       "acSonetSectionDayIntervalNodeId": acSonetSectionDayIntervalNodeId,
       "acSonetSectionDayIntervalSlot": acSonetSectionDayIntervalSlot,
       "acSonetSectionDayIntervalPort": acSonetSectionDayIntervalPort,
       "acSonetSectionDayIntervalNumber": acSonetSectionDayIntervalNumber,
       "acSonetSectionDayIntervalValidStats": acSonetSectionDayIntervalValidStats,
       "acSonetSectionDayIntervalResetStats": acSonetSectionDayIntervalResetStats,
       "acSonetSectionDayIntervalStatus": acSonetSectionDayIntervalStatus,
       "acSonetSectionDayIntervalESs": acSonetSectionDayIntervalESs,
       "acSonetSectionDayIntervalSESs": acSonetSectionDayIntervalSESs,
       "acSonetSectionDayIntervalSEFSs": acSonetSectionDayIntervalSEFSs,
       "acSonetSectionDayIntervalCVs": acSonetSectionDayIntervalCVs,
       "acSonetSectionThresholdTable": acSonetSectionThresholdTable,
       "acSonetSectionThresholdEntry": acSonetSectionThresholdEntry,
       "acSonetSectionThresholdNodeId": acSonetSectionThresholdNodeId,
       "acSonetSectionThresholdSlot": acSonetSectionThresholdSlot,
       "acSonetSectionThresholdPort": acSonetSectionThresholdPort,
       "acSonetSectionThresholdSelectionNum": acSonetSectionThresholdSelectionNum,
       "acSonetSectionThresholdAdminStatus": acSonetSectionThresholdAdminStatus,
       "acSonetSectionThresholdESs": acSonetSectionThresholdESs,
       "acSonetSectionThresholdSESs": acSonetSectionThresholdSESs,
       "acSonetSectionThresholdSEFSs": acSonetSectionThresholdSEFSs,
       "acSonetSectionThresholdCVs": acSonetSectionThresholdCVs,
       "acSonetSectionTIMTable": acSonetSectionTIMTable,
       "acSonetSectionTIMEntry": acSonetSectionTIMEntry,
       "acSonetSectionTIMNodeId": acSonetSectionTIMNodeId,
       "acSonetSectionTIMSlot": acSonetSectionTIMSlot,
       "acSonetSectionTIMPort": acSonetSectionTIMPort,
       "acSonetSectionTIMGenerateEnable": acSonetSectionTIMGenerateEnable,
       "acSonetSectionTIMDetectEnable": acSonetSectionTIMDetectEnable,
       "acSonetSectionTIMTransmitedString": acSonetSectionTIMTransmitedString,
       "acSonetSectionTIMExpectedString": acSonetSectionTIMExpectedString,
       "acSonetSectionTIMReceivedString": acSonetSectionTIMReceivedString,
       "acSonetSectionTIMFailure": acSonetSectionTIMFailure,
       "acSonetSectionTIMFormat": acSonetSectionTIMFormat,
       "acSonetSectionTIMMismatchZeros": acSonetSectionTIMMismatchZeros,
       "acSonetSectionSSMTable": acSonetSectionSSMTable,
       "acSonetSectionSSMEntry": acSonetSectionSSMEntry,
       "acSonetSectionSSMNodeId": acSonetSectionSSMNodeId,
       "acSonetSectionSSMSlot": acSonetSectionSSMSlot,
       "acSonetSectionSSMPort": acSonetSectionSSMPort,
       "acSonetSectionSSMDetectEnable": acSonetSectionSSMDetectEnable,
       "acSonetSectionSSMTransmitedValue": acSonetSectionSSMTransmitedValue,
       "acSonetSectionSSMReceivedValue": acSonetSectionSSMReceivedValue,
       "acSonetLine": acSonetLine,
       "acSonetLine15MinuteIntervalTable": acSonetLine15MinuteIntervalTable,
       "acSonetLine15MinuteIntervalEntry": acSonetLine15MinuteIntervalEntry,
       "acSonetLine15MinuteIntervalNodeId": acSonetLine15MinuteIntervalNodeId,
       "acSonetLine15MinuteIntervalSlot": acSonetLine15MinuteIntervalSlot,
       "acSonetLine15MinuteIntervalPort": acSonetLine15MinuteIntervalPort,
       "acSonetLine15MinuteIntervalNumber": acSonetLine15MinuteIntervalNumber,
       "acSonetLine15MinuteIntervalValidStats": acSonetLine15MinuteIntervalValidStats,
       "acSonetLine15MinuteIntervalResetStats": acSonetLine15MinuteIntervalResetStats,
       "acSonetLine15MinuteIntervalStatus": acSonetLine15MinuteIntervalStatus,
       "acSonetLine15MinuteIntervalESs": acSonetLine15MinuteIntervalESs,
       "acSonetLine15MinuteIntervalSESs": acSonetLine15MinuteIntervalSESs,
       "acSonetLine15MinuteIntervalCVs": acSonetLine15MinuteIntervalCVs,
       "acSonetLine15MinuteIntervalUASs": acSonetLine15MinuteIntervalUASs,
       "acSonetLine15MinuteIntervalBER": acSonetLine15MinuteIntervalBER,
       "acSonetLineDayIntervalTable": acSonetLineDayIntervalTable,
       "acSonetLineDayIntervalEntry": acSonetLineDayIntervalEntry,
       "acSonetLineDayIntervalNodeId": acSonetLineDayIntervalNodeId,
       "acSonetLineDayIntervalSlot": acSonetLineDayIntervalSlot,
       "acSonetLineDayIntervalPort": acSonetLineDayIntervalPort,
       "acSonetLineDayIntervalNumber": acSonetLineDayIntervalNumber,
       "acSonetLineDayIntervalValidStats": acSonetLineDayIntervalValidStats,
       "acSonetLineDayIntervalResetStats": acSonetLineDayIntervalResetStats,
       "acSonetLineDayIntervalStatus": acSonetLineDayIntervalStatus,
       "acSonetLineDayIntervalESs": acSonetLineDayIntervalESs,
       "acSonetLineDayIntervalSESs": acSonetLineDayIntervalSESs,
       "acSonetLineDayIntervalCVs": acSonetLineDayIntervalCVs,
       "acSonetLineDayIntervalUASs": acSonetLineDayIntervalUASs,
       "acSonetLineDayIntervalBER": acSonetLineDayIntervalBER,
       "acSonetLineThresholdTable": acSonetLineThresholdTable,
       "acSonetLineThresholdEntry": acSonetLineThresholdEntry,
       "acSonetLineThresholdNodeId": acSonetLineThresholdNodeId,
       "acSonetLineThresholdSlot": acSonetLineThresholdSlot,
       "acSonetLineThresholdPort": acSonetLineThresholdPort,
       "acSonetLineThresholdSelectionNum": acSonetLineThresholdSelectionNum,
       "acSonetLineThresholdAdminStatus": acSonetLineThresholdAdminStatus,
       "acSonetLineThresholdESs": acSonetLineThresholdESs,
       "acSonetLineThresholdSESs": acSonetLineThresholdSESs,
       "acSonetLineThresholdCVs": acSonetLineThresholdCVs,
       "acSonetLineThresholdUASs": acSonetLineThresholdUASs,
       "acSonetLineProtectionTable": acSonetLineProtectionTable,
       "acSonetLineProtectionEntry": acSonetLineProtectionEntry,
       "acSonetLineProtectionNodeId": acSonetLineProtectionNodeId,
       "acSonetLineProtectionSlot": acSonetLineProtectionSlot,
       "acSonetLineProtectionPort": acSonetLineProtectionPort,
       "acSonetLineProtectionArchitecture": acSonetLineProtectionArchitecture,
       "acSonetLineProtectionOpMode": acSonetLineProtectionOpMode,
       "acSonetLineProtectionSwitchType": acSonetLineProtectionSwitchType,
       "acSonetLineProtectionSFThreshold": acSonetLineProtectionSFThreshold,
       "acSonetLineProtectionSDThreshold": acSonetLineProtectionSDThreshold,
       "acSonetLineProtectionActiveTraffic": acSonetLineProtectionActiveTraffic,
       "acSonetLineProtectionProtectionSwitch": acSonetLineProtectionProtectionSwitch,
       "acSonetLineProtectionFail": acSonetLineProtectionFail,
       "acSonetLineProtectionChannelMismatchFail": acSonetLineProtectionChannelMismatchFail,
       "acSonetLineProtectionModeMismatchFail": acSonetLineProtectionModeMismatchFail,
       "acSonetLineProtectionFarEndLineFail": acSonetLineProtectionFarEndLineFail,
       "acSonetLineProtectionWTRTime": acSonetLineProtectionWTRTime,
       "acSonetLineProtectionManCommand": acSonetLineProtectionManCommand,
       "acSonetFarEndLine": acSonetFarEndLine,
       "acSonetFarEndLine15MinuteIntervalTable": acSonetFarEndLine15MinuteIntervalTable,
       "acSonetFarEndLine15MinuteIntervalEntry": acSonetFarEndLine15MinuteIntervalEntry,
       "acSonetFarEndLine15MinuteIntervalNodeId": acSonetFarEndLine15MinuteIntervalNodeId,
       "acSonetFarEndLine15MinuteIntervalSlot": acSonetFarEndLine15MinuteIntervalSlot,
       "acSonetFarEndLine15MinuteIntervalPort": acSonetFarEndLine15MinuteIntervalPort,
       "acSonetFarEndLine15MinuteIntervalNumber": acSonetFarEndLine15MinuteIntervalNumber,
       "acSonetFarEndLine15MinuteIntervalValidStats": acSonetFarEndLine15MinuteIntervalValidStats,
       "acSonetFarEndLine15MinuteIntervalResetStats": acSonetFarEndLine15MinuteIntervalResetStats,
       "acSonetFarEndLine15MinuteIntervalESs": acSonetFarEndLine15MinuteIntervalESs,
       "acSonetFarEndLine15MinuteIntervalSESs": acSonetFarEndLine15MinuteIntervalSESs,
       "acSonetFarEndLine15MinuteIntervalCVs": acSonetFarEndLine15MinuteIntervalCVs,
       "acSonetFarEndLine15MinuteIntervalUASs": acSonetFarEndLine15MinuteIntervalUASs,
       "acSonetFarEndLineDayIntervalTable": acSonetFarEndLineDayIntervalTable,
       "acSonetFarEndLineDayIntervalEntry": acSonetFarEndLineDayIntervalEntry,
       "acSonetFarEndLineDayIntervalNodeId": acSonetFarEndLineDayIntervalNodeId,
       "acSonetFarEndLineDayIntervalSlot": acSonetFarEndLineDayIntervalSlot,
       "acSonetFarEndLineDayIntervalPort": acSonetFarEndLineDayIntervalPort,
       "acSonetFarEndLineDayIntervalNumber": acSonetFarEndLineDayIntervalNumber,
       "acSonetFarEndLineDayIntervalValidStats": acSonetFarEndLineDayIntervalValidStats,
       "acSonetFarEndLineDayIntervalResetStats": acSonetFarEndLineDayIntervalResetStats,
       "acSonetFarEndLineDayIntervalESs": acSonetFarEndLineDayIntervalESs,
       "acSonetFarEndLineDayIntervalSESs": acSonetFarEndLineDayIntervalSESs,
       "acSonetFarEndLineDayIntervalCVs": acSonetFarEndLineDayIntervalCVs,
       "acSonetFarEndLineDayIntervalUASs": acSonetFarEndLineDayIntervalUASs,
       "acSonetFarEndLineThresholdTable": acSonetFarEndLineThresholdTable,
       "acSonetFarEndLineThresholdEntry": acSonetFarEndLineThresholdEntry,
       "acSonetFarEndLineThresholdNodeId": acSonetFarEndLineThresholdNodeId,
       "acSonetFarEndLineThresholdSlot": acSonetFarEndLineThresholdSlot,
       "acSonetFarEndLineThresholdPort": acSonetFarEndLineThresholdPort,
       "acSonetFarEndLineThresholdSelectionNum": acSonetFarEndLineThresholdSelectionNum,
       "acSonetFarEndLineThresholdAdminStatus": acSonetFarEndLineThresholdAdminStatus,
       "acSonetFarEndLineThresholdESs": acSonetFarEndLineThresholdESs,
       "acSonetFarEndLineThresholdSESs": acSonetFarEndLineThresholdSESs,
       "acSonetFarEndLineThresholdCVs": acSonetFarEndLineThresholdCVs,
       "acSonetFarEndLineThresholdUASs": acSonetFarEndLineThresholdUASs,
       "acSonetObjectsPath": acSonetObjectsPath,
       "acSonetPath": acSonetPath,
       "acSonetPath15MinuteIntervalTable": acSonetPath15MinuteIntervalTable,
       "acSonetPath15MinuteIntervalEntry": acSonetPath15MinuteIntervalEntry,
       "acSonetPath15MinuteIntervalNodeId": acSonetPath15MinuteIntervalNodeId,
       "acSonetPath15MinuteIntervalSlot": acSonetPath15MinuteIntervalSlot,
       "acSonetPath15MinuteIntervalPort": acSonetPath15MinuteIntervalPort,
       "acSonetPath15MinuteIntervalPath": acSonetPath15MinuteIntervalPath,
       "acSonetPath15MinuteIntervalNumber": acSonetPath15MinuteIntervalNumber,
       "acSonetPath15MinuteIntervalStatus": acSonetPath15MinuteIntervalStatus,
       "acSonetPath15MinuteIntervalValidStats": acSonetPath15MinuteIntervalValidStats,
       "acSonetPath15MinuteIntervalResetStats": acSonetPath15MinuteIntervalResetStats,
       "acSonetPath15MinuteIntervalESs": acSonetPath15MinuteIntervalESs,
       "acSonetPath15MinuteIntervalSESs": acSonetPath15MinuteIntervalSESs,
       "acSonetPath15MinuteIntervalCVs": acSonetPath15MinuteIntervalCVs,
       "acSonetPath15MinuteIntervalUASs": acSonetPath15MinuteIntervalUASs,
       "acSonetPath15MinuteIntervalBER": acSonetPath15MinuteIntervalBER,
       "acSonetPathDayIntervalTable": acSonetPathDayIntervalTable,
       "acSonetPathDayIntervalEntry": acSonetPathDayIntervalEntry,
       "acSonetPathDayIntervalNodeId": acSonetPathDayIntervalNodeId,
       "acSonetPathDayIntervalSlot": acSonetPathDayIntervalSlot,
       "acSonetPathDayIntervalPort": acSonetPathDayIntervalPort,
       "acSonetPathDayIntervalPath": acSonetPathDayIntervalPath,
       "acSonetPathDayIntervalNumber": acSonetPathDayIntervalNumber,
       "acSonetPathDayIntervalStatus": acSonetPathDayIntervalStatus,
       "acSonetPathDayIntervalValidStats": acSonetPathDayIntervalValidStats,
       "acSonetPathDayIntervalResetStats": acSonetPathDayIntervalResetStats,
       "acSonetPathDayIntervalESs": acSonetPathDayIntervalESs,
       "acSonetPathDayIntervalSESs": acSonetPathDayIntervalSESs,
       "acSonetPathDayIntervalCVs": acSonetPathDayIntervalCVs,
       "acSonetPathDayIntervalUASs": acSonetPathDayIntervalUASs,
       "acSonetPathDayIntervalBER": acSonetPathDayIntervalBER,
       "acSonetPathThresholdTable": acSonetPathThresholdTable,
       "acSonetPathThresholdEntry": acSonetPathThresholdEntry,
       "acSonetPathThresholdNodeId": acSonetPathThresholdNodeId,
       "acSonetPathThresholdSlot": acSonetPathThresholdSlot,
       "acSonetPathThresholdPort": acSonetPathThresholdPort,
       "acSonetPathThresholdPath": acSonetPathThresholdPath,
       "acSonetPathThresholdSelectionNum": acSonetPathThresholdSelectionNum,
       "acSonetPathThresholdAdminStatus": acSonetPathThresholdAdminStatus,
       "acSonetPathThresholdESs": acSonetPathThresholdESs,
       "acSonetPathThresholdSESs": acSonetPathThresholdSESs,
       "acSonetPathThresholdCVs": acSonetPathThresholdCVs,
       "acSonetPathThresholdUASs": acSonetPathThresholdUASs,
       "acSonetPathRDITable": acSonetPathRDITable,
       "acSonetPathRDIEntry": acSonetPathRDIEntry,
       "acSonetPathRDINodeId": acSonetPathRDINodeId,
       "acSonetPathRDISlot": acSonetPathRDISlot,
       "acSonetPathRDIPort": acSonetPathRDIPort,
       "acSonetPathRDIPath": acSonetPathRDIPath,
       "acSonetPathRDIOpMode": acSonetPathRDIOpMode,
       "acSonetPathTIMTable": acSonetPathTIMTable,
       "acSonetPathTIMEntry": acSonetPathTIMEntry,
       "acSonetPathTIMNodeId": acSonetPathTIMNodeId,
       "acSonetPathTIMSlot": acSonetPathTIMSlot,
       "acSonetPathTIMPort": acSonetPathTIMPort,
       "acSonetPathTIMPath": acSonetPathTIMPath,
       "acSonetPathTIMGenerateEnable": acSonetPathTIMGenerateEnable,
       "acSonetPathTIMDetectEnable": acSonetPathTIMDetectEnable,
       "acSonetPathTIMTransmitedString": acSonetPathTIMTransmitedString,
       "acSonetPathTIMExpectedString": acSonetPathTIMExpectedString,
       "acSonetPathTIMReceivedString": acSonetPathTIMReceivedString,
       "acSonetPathTIMFailure": acSonetPathTIMFailure,
       "acSonetPathTIMFormat": acSonetPathTIMFormat,
       "acSonetPathTIMMismatchZeros": acSonetPathTIMMismatchZeros,
       "acSonetPathPLMTable": acSonetPathPLMTable,
       "acSonetPathPLMEntry": acSonetPathPLMEntry,
       "acSonetPathPLMNodeId": acSonetPathPLMNodeId,
       "acSonetPathPLMSlot": acSonetPathPLMSlot,
       "acSonetPathPLMPort": acSonetPathPLMPort,
       "acSonetPathPLMPath": acSonetPathPLMPath,
       "acSonetPathPLMDetectEnable": acSonetPathPLMDetectEnable,
       "acSonetPathPLMTransmitedValue": acSonetPathPLMTransmitedValue,
       "acSonetPathPLMExpectedValue": acSonetPathPLMExpectedValue,
       "acSonetPathPLMReceivedValue": acSonetPathPLMReceivedValue,
       "acSonetPathPLMMismatchFailure": acSonetPathPLMMismatchFailure,
       "acSonetPathPLMUnequipped": acSonetPathPLMUnequipped,
       "acSonetPathProtectionTable": acSonetPathProtectionTable,
       "acSonetPathProtectionEntry": acSonetPathProtectionEntry,
       "acSonetPathProtectionNodeId": acSonetPathProtectionNodeId,
       "acSonetPathProtectionSlot": acSonetPathProtectionSlot,
       "acSonetPathProtectionPort": acSonetPathProtectionPort,
       "acSonetPathProtectionPath": acSonetPathProtectionPath,
       "acSonetPathProtectionSwitchType": acSonetPathProtectionSwitchType,
       "acSonetPathProtectionSFThreshold": acSonetPathProtectionSFThreshold,
       "acSonetPathProtectionSDThreshold": acSonetPathProtectionSDThreshold,
       "acSonetPathProtectionActiveTraffic": acSonetPathProtectionActiveTraffic,
       "acSonetPathProtectionProtectionSwitch": acSonetPathProtectionProtectionSwitch,
       "acSonetPathProtectionWTRTime": acSonetPathProtectionWTRTime,
       "acSonetPathProtectionWTITime": acSonetPathProtectionWTITime,
       "acSonetPathProtectionWTCTime": acSonetPathProtectionWTCTime,
       "acSonetPathProtectionWTRelTime": acSonetPathProtectionWTRelTime,
       "acSonetPathProtectionManSwitch": acSonetPathProtectionManSwitch,
       "acSonetPathProtectionSwitchOpStatus": acSonetPathProtectionSwitchOpStatus,
       "acSonetPathProtectionProtectionMode": acSonetPathProtectionProtectionMode,
       "acSonetFarEndPath": acSonetFarEndPath,
       "acSonetFarEndPath15MinuteIntervalTable": acSonetFarEndPath15MinuteIntervalTable,
       "acSonetFarEndPath15MinuteIntervalEntry": acSonetFarEndPath15MinuteIntervalEntry,
       "acSonetFarEndPath15MinuteIntervalNodeId": acSonetFarEndPath15MinuteIntervalNodeId,
       "acSonetFarEndPath15MinuteIntervalSlot": acSonetFarEndPath15MinuteIntervalSlot,
       "acSonetFarEndPath15MinuteIntervalPort": acSonetFarEndPath15MinuteIntervalPort,
       "acSonetFarEndPath15MinuteIntervalPath": acSonetFarEndPath15MinuteIntervalPath,
       "acSonetFarEndPath15MinuteIntervalNumber": acSonetFarEndPath15MinuteIntervalNumber,
       "acSonetFarEndPath15MinuteIntervalValidStats": acSonetFarEndPath15MinuteIntervalValidStats,
       "acSonetFarEndPath15MinuteIntervalResetStats": acSonetFarEndPath15MinuteIntervalResetStats,
       "acSonetFarEndPath15MinuteIntervalESs": acSonetFarEndPath15MinuteIntervalESs,
       "acSonetFarEndPath15MinuteIntervalSESs": acSonetFarEndPath15MinuteIntervalSESs,
       "acSonetFarEndPath15MinuteIntervalCVs": acSonetFarEndPath15MinuteIntervalCVs,
       "acSonetFarEndPath15MinuteIntervalUASs": acSonetFarEndPath15MinuteIntervalUASs,
       "acSonetFarEndPathDayIntervalTable": acSonetFarEndPathDayIntervalTable,
       "acSonetFarEndPathDayIntervalEntry": acSonetFarEndPathDayIntervalEntry,
       "acSonetFarEndPathDayIntervalNodeId": acSonetFarEndPathDayIntervalNodeId,
       "acSonetFarEndPathDayIntervalSlot": acSonetFarEndPathDayIntervalSlot,
       "acSonetFarEndPathDayIntervalPort": acSonetFarEndPathDayIntervalPort,
       "acSonetFarEndPathDayIntervalPath": acSonetFarEndPathDayIntervalPath,
       "acSonetFarEndPathDayIntervalNumber": acSonetFarEndPathDayIntervalNumber,
       "acSonetFarEndPathDayIntervalValidStats": acSonetFarEndPathDayIntervalValidStats,
       "acSonetFarEndPathDayIntervalResetStats": acSonetFarEndPathDayIntervalResetStats,
       "acSonetFarEndPathDayIntervalESs": acSonetFarEndPathDayIntervalESs,
       "acSonetFarEndPathDayIntervalSESs": acSonetFarEndPathDayIntervalSESs,
       "acSonetFarEndPathDayIntervalCVs": acSonetFarEndPathDayIntervalCVs,
       "acSonetFarEndPathDayIntervalUASs": acSonetFarEndPathDayIntervalUASs,
       "acSonetFarEndPathThresholdTable": acSonetFarEndPathThresholdTable,
       "acSonetFarEndPathThresholdEntry": acSonetFarEndPathThresholdEntry,
       "acSonetFarEndPathThresholdNodeId": acSonetFarEndPathThresholdNodeId,
       "acSonetFarEndPathThresholdSlot": acSonetFarEndPathThresholdSlot,
       "acSonetFarEndPathThresholdPort": acSonetFarEndPathThresholdPort,
       "acSonetFarEndPathThresholdPath": acSonetFarEndPathThresholdPath,
       "acSonetFarEndPathThresholdSelectionNum": acSonetFarEndPathThresholdSelectionNum,
       "acSonetFarEndPathThresholdAdminStatus": acSonetFarEndPathThresholdAdminStatus,
       "acSonetFarEndPathThresholdESs": acSonetFarEndPathThresholdESs,
       "acSonetFarEndPathThresholdSESs": acSonetFarEndPathThresholdSESs,
       "acSonetFarEndPathThresholdCVs": acSonetFarEndPathThresholdCVs,
       "acSonetFarEndPathThresholdUASs": acSonetFarEndPathThresholdUASs,
       "acSonetObjectsVT": acSonetObjectsVT,
       "acSonetVT": acSonetVT,
       "acSonetVT15MinuteIntervalTable": acSonetVT15MinuteIntervalTable,
       "acSonetVT15MinuteIntervalEntry": acSonetVT15MinuteIntervalEntry,
       "acSonetVT15MinuteIntervalNodeId": acSonetVT15MinuteIntervalNodeId,
       "acSonetVT15MinuteIntervalSlot": acSonetVT15MinuteIntervalSlot,
       "acSonetVT15MinuteIntervalPort": acSonetVT15MinuteIntervalPort,
       "acSonetVT15MinuteIntervalVT": acSonetVT15MinuteIntervalVT,
       "acSonetVT15MinuteIntervalNumber": acSonetVT15MinuteIntervalNumber,
       "acSonetVT15MinuteIntervalStatus": acSonetVT15MinuteIntervalStatus,
       "acSonetVT15MinuteIntervalValidStats": acSonetVT15MinuteIntervalValidStats,
       "acSonetVT15MinuteIntervalResetStats": acSonetVT15MinuteIntervalResetStats,
       "acSonetVT15MinuteIntervalESs": acSonetVT15MinuteIntervalESs,
       "acSonetVT15MinuteIntervalSESs": acSonetVT15MinuteIntervalSESs,
       "acSonetVT15MinuteIntervalCVs": acSonetVT15MinuteIntervalCVs,
       "acSonetVT15MinuteIntervalUASs": acSonetVT15MinuteIntervalUASs,
       "acSonetVT15MinuteIntervalBER": acSonetVT15MinuteIntervalBER,
       "acSonetVTDayIntervalTable": acSonetVTDayIntervalTable,
       "acSonetVTDayIntervalEntry": acSonetVTDayIntervalEntry,
       "acSonetVTDayIntervalNodeId": acSonetVTDayIntervalNodeId,
       "acSonetVTDayIntervalSlot": acSonetVTDayIntervalSlot,
       "acSonetVTDayIntervalPort": acSonetVTDayIntervalPort,
       "acSonetVTDayIntervalVT": acSonetVTDayIntervalVT,
       "acSonetVTDayIntervalNumber": acSonetVTDayIntervalNumber,
       "acSonetVTDayIntervalStatus": acSonetVTDayIntervalStatus,
       "acSonetVTDayIntervalValidStats": acSonetVTDayIntervalValidStats,
       "acSonetVTDayIntervalResetStats": acSonetVTDayIntervalResetStats,
       "acSonetVTDayIntervalESs": acSonetVTDayIntervalESs,
       "acSonetVTDayIntervalSESs": acSonetVTDayIntervalSESs,
       "acSonetVTDayIntervalCVs": acSonetVTDayIntervalCVs,
       "acSonetVTDayIntervalUASs": acSonetVTDayIntervalUASs,
       "acSonetVTDayIntervalBER": acSonetVTDayIntervalBER,
       "acSonetVTThresholdTable": acSonetVTThresholdTable,
       "acSonetVTThresholdEntry": acSonetVTThresholdEntry,
       "acSonetVTThresholdNodeId": acSonetVTThresholdNodeId,
       "acSonetVTThresholdSlot": acSonetVTThresholdSlot,
       "acSonetVTThresholdPort": acSonetVTThresholdPort,
       "acSonetVTThresholdVT": acSonetVTThresholdVT,
       "acSonetVTThresholdSelectionNum": acSonetVTThresholdSelectionNum,
       "acSonetVTThresholdAdminStatus": acSonetVTThresholdAdminStatus,
       "acSonetVTThresholdESs": acSonetVTThresholdESs,
       "acSonetVTThresholdSESs": acSonetVTThresholdSESs,
       "acSonetVTThresholdCVs": acSonetVTThresholdCVs,
       "acSonetVTThresholdUASs": acSonetVTThresholdUASs,
       "acSonetVTRDITable": acSonetVTRDITable,
       "acSonetVTRDIEntry": acSonetVTRDIEntry,
       "acSonetVTRDINodeId": acSonetVTRDINodeId,
       "acSonetVTRDISlot": acSonetVTRDISlot,
       "acSonetVTRDIPort": acSonetVTRDIPort,
       "acSonetVTRDIVT": acSonetVTRDIVT,
       "acSonetVTRDIOpMode": acSonetVTRDIOpMode,
       "acSonetVTPLMTable": acSonetVTPLMTable,
       "acSonetVTPLMEntry": acSonetVTPLMEntry,
       "acSonetVTPLMNodeId": acSonetVTPLMNodeId,
       "acSonetVTPLMSlot": acSonetVTPLMSlot,
       "acSonetVTPLMPort": acSonetVTPLMPort,
       "acSonetVTPLMVT": acSonetVTPLMVT,
       "acSonetVTPLMDetectEnable": acSonetVTPLMDetectEnable,
       "acSonetVTPLMTransmitedValue": acSonetVTPLMTransmitedValue,
       "acSonetVTPLMExpectedValue": acSonetVTPLMExpectedValue,
       "acSonetVTPLMReceivedValue": acSonetVTPLMReceivedValue,
       "acSonetVTPLMMismatchFailure": acSonetVTPLMMismatchFailure,
       "acSonetVTPLMUnequipped": acSonetVTPLMUnequipped,
       "acSonetVTProtectionTable": acSonetVTProtectionTable,
       "acSonetVTProtectionEntry": acSonetVTProtectionEntry,
       "acSonetVTProtectionNodeId": acSonetVTProtectionNodeId,
       "acSonetVTProtectionSlot": acSonetVTProtectionSlot,
       "acSonetVTProtectionPort": acSonetVTProtectionPort,
       "acSonetVTProtectionVT": acSonetVTProtectionVT,
       "acSonetVTProtectionSwitchType": acSonetVTProtectionSwitchType,
       "acSonetVTProtectionSFThreshold": acSonetVTProtectionSFThreshold,
       "acSonetVTProtectionSDThreshold": acSonetVTProtectionSDThreshold,
       "acSonetVTProtectionProtectionSwitch": acSonetVTProtectionProtectionSwitch,
       "acSonetVTProtectionWTRTime": acSonetVTProtectionWTRTime,
       "acSonetVTProtectionManSwitch": acSonetVTProtectionManSwitch,
       "acSonetVTProtectionActiveTraffic": acSonetVTProtectionActiveTraffic,
       "acSonetFarEndVT": acSonetFarEndVT,
       "acSonetFarEndVT15MinuteIntervalTable": acSonetFarEndVT15MinuteIntervalTable,
       "acSonetFarEndVT15MinuteIntervalEntry": acSonetFarEndVT15MinuteIntervalEntry,
       "acSonetFarEndVT15MinuteIntervalNodeId": acSonetFarEndVT15MinuteIntervalNodeId,
       "acSonetFarEndVT15MinuteIntervalSlot": acSonetFarEndVT15MinuteIntervalSlot,
       "acSonetFarEndVT15MinuteIntervalPort": acSonetFarEndVT15MinuteIntervalPort,
       "acSonetFarEndVT15MinuteIntervalVT": acSonetFarEndVT15MinuteIntervalVT,
       "acSonetFarEndVT15MinuteIntervalNumber": acSonetFarEndVT15MinuteIntervalNumber,
       "acSonetFarEndVT15MinuteIntervalValidStats": acSonetFarEndVT15MinuteIntervalValidStats,
       "acSonetFarEndVT15MinuteIntervalResetStats": acSonetFarEndVT15MinuteIntervalResetStats,
       "acSonetFarEndVT15MinuteIntervalESs": acSonetFarEndVT15MinuteIntervalESs,
       "acSonetFarEndVT15MinuteIntervalSESs": acSonetFarEndVT15MinuteIntervalSESs,
       "acSonetFarEndVT15MinuteIntervalCVs": acSonetFarEndVT15MinuteIntervalCVs,
       "acSonetFarEndVT15MinuteIntervalUASs": acSonetFarEndVT15MinuteIntervalUASs,
       "acSonetFarEndVTDayIntervalTable": acSonetFarEndVTDayIntervalTable,
       "acSonetFarEndVTDayIntervalEntry": acSonetFarEndVTDayIntervalEntry,
       "acSonetFarEndVTDayIntervalNodeId": acSonetFarEndVTDayIntervalNodeId,
       "acSonetFarEndVTDayIntervalSlot": acSonetFarEndVTDayIntervalSlot,
       "acSonetFarEndVTDayIntervalPort": acSonetFarEndVTDayIntervalPort,
       "acSonetFarEndVTDayIntervalVT": acSonetFarEndVTDayIntervalVT,
       "acSonetFarEndVTDayIntervalNumber": acSonetFarEndVTDayIntervalNumber,
       "acSonetFarEndVTDayIntervalValidStats": acSonetFarEndVTDayIntervalValidStats,
       "acSonetFarEndVTDayIntervalResetStats": acSonetFarEndVTDayIntervalResetStats,
       "acSonetFarEndVTDayIntervalESs": acSonetFarEndVTDayIntervalESs,
       "acSonetFarEndVTDayIntervalSESs": acSonetFarEndVTDayIntervalSESs,
       "acSonetFarEndVTDayIntervalCVs": acSonetFarEndVTDayIntervalCVs,
       "acSonetFarEndVTDayIntervalUASs": acSonetFarEndVTDayIntervalUASs,
       "acSonetFarEndVTThresholdTable": acSonetFarEndVTThresholdTable,
       "acSonetFarEndVTThresholdEntry": acSonetFarEndVTThresholdEntry,
       "acSonetFarEndVTThresholdNodeId": acSonetFarEndVTThresholdNodeId,
       "acSonetFarEndVTThresholdSlot": acSonetFarEndVTThresholdSlot,
       "acSonetFarEndVTThresholdPort": acSonetFarEndVTThresholdPort,
       "acSonetFarEndVTThresholdVT": acSonetFarEndVTThresholdVT,
       "acSonetFarEndVTThresholdSelectionNum": acSonetFarEndVTThresholdSelectionNum,
       "acSonetFarEndVTThresholdAdminStatus": acSonetFarEndVTThresholdAdminStatus,
       "acSonetFarEndVTThresholdESs": acSonetFarEndVTThresholdESs,
       "acSonetFarEndVTThresholdSESs": acSonetFarEndVTThresholdSESs,
       "acSonetFarEndVTThresholdCVs": acSonetFarEndVTThresholdCVs,
       "acSonetFarEndVTThresholdUASs": acSonetFarEndVTThresholdUASs}
)
