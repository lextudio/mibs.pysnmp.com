# SNMP MIB module (ALCATEL-IND1-UDLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-UDLD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:29 2024
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

(softentIND1Udld,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Udld")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

alcatelIND1UDLDMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1)
)
alcatelIND1UDLDMIB.setRevisions(
        ("2007-02-14 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1UDLDMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1UDLDMIBObjects = _AlcatelIND1UDLDMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1UDLDMIBObjects.setStatus("current")


class _AlaUdldGlobalStatus_Type(Integer32):
    """Custom type alaUdldGlobalStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaUdldGlobalStatus_Type.__name__ = "Integer32"
_AlaUdldGlobalStatus_Object = MibScalar
alaUdldGlobalStatus = _AlaUdldGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 1),
    _AlaUdldGlobalStatus_Type()
)
alaUdldGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaUdldGlobalStatus.setStatus("current")


class _AlaUdldGlobalClearStats_Type(Integer32):
    """Custom type alaUdldGlobalClearStats based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaUdldGlobalClearStats_Type.__name__ = "Integer32"
_AlaUdldGlobalClearStats_Object = MibScalar
alaUdldGlobalClearStats = _AlaUdldGlobalClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 2),
    _AlaUdldGlobalClearStats_Type()
)
alaUdldGlobalClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaUdldGlobalClearStats.setStatus("current")


class _AlaUdldGlobalConfigUdldMode_Type(Integer32):
    """Custom type alaUdldGlobalConfigUdldMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggressive", 2),
          ("normal", 1))
    )


_AlaUdldGlobalConfigUdldMode_Type.__name__ = "Integer32"
_AlaUdldGlobalConfigUdldMode_Object = MibScalar
alaUdldGlobalConfigUdldMode = _AlaUdldGlobalConfigUdldMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 3),
    _AlaUdldGlobalConfigUdldMode_Type()
)
alaUdldGlobalConfigUdldMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaUdldGlobalConfigUdldMode.setStatus("current")


class _AlaUdldGlobalConfigUdldProbeIntervalTimer_Type(Unsigned32):
    """Custom type alaUdldGlobalConfigUdldProbeIntervalTimer based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 90),
    )


_AlaUdldGlobalConfigUdldProbeIntervalTimer_Type.__name__ = "Unsigned32"
_AlaUdldGlobalConfigUdldProbeIntervalTimer_Object = MibScalar
alaUdldGlobalConfigUdldProbeIntervalTimer = _AlaUdldGlobalConfigUdldProbeIntervalTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 4),
    _AlaUdldGlobalConfigUdldProbeIntervalTimer_Type()
)
alaUdldGlobalConfigUdldProbeIntervalTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaUdldGlobalConfigUdldProbeIntervalTimer.setStatus("current")
if mibBuilder.loadTexts:
    alaUdldGlobalConfigUdldProbeIntervalTimer.setUnits("seconds")


class _AlaUdldGlobalConfigUdldDetectionPeriodTimer_Type(Unsigned32):
    """Custom type alaUdldGlobalConfigUdldDetectionPeriodTimer based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 15),
    )


_AlaUdldGlobalConfigUdldDetectionPeriodTimer_Type.__name__ = "Unsigned32"
_AlaUdldGlobalConfigUdldDetectionPeriodTimer_Object = MibScalar
alaUdldGlobalConfigUdldDetectionPeriodTimer = _AlaUdldGlobalConfigUdldDetectionPeriodTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 5),
    _AlaUdldGlobalConfigUdldDetectionPeriodTimer_Type()
)
alaUdldGlobalConfigUdldDetectionPeriodTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaUdldGlobalConfigUdldDetectionPeriodTimer.setStatus("current")
if mibBuilder.loadTexts:
    alaUdldGlobalConfigUdldDetectionPeriodTimer.setUnits("seconds")
_UdldPortConfig_ObjectIdentity = ObjectIdentity
udldPortConfig = _UdldPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 6)
)
_AlaUdldPortConfigTable_Object = MibTable
alaUdldPortConfigTable = _AlaUdldPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    alaUdldPortConfigTable.setStatus("current")
_AlaUdldPortConfigEntry_Object = MibTableRow
alaUdldPortConfigEntry = _AlaUdldPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 6, 1, 1)
)
alaUdldPortConfigEntry.setIndexNames(
    (0, "ALCATEL-IND1-UDLD-MIB", "alaUdldPortConfigIfIndex"),
)
if mibBuilder.loadTexts:
    alaUdldPortConfigEntry.setStatus("current")
_AlaUdldPortConfigIfIndex_Type = InterfaceIndex
_AlaUdldPortConfigIfIndex_Object = MibTableColumn
alaUdldPortConfigIfIndex = _AlaUdldPortConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 6, 1, 1, 1),
    _AlaUdldPortConfigIfIndex_Type()
)
alaUdldPortConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaUdldPortConfigIfIndex.setStatus("current")


class _AlaUdldPortConfigUdldStatus_Type(Integer32):
    """Custom type alaUdldPortConfigUdldStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaUdldPortConfigUdldStatus_Type.__name__ = "Integer32"
_AlaUdldPortConfigUdldStatus_Object = MibTableColumn
alaUdldPortConfigUdldStatus = _AlaUdldPortConfigUdldStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 6, 1, 1, 2),
    _AlaUdldPortConfigUdldStatus_Type()
)
alaUdldPortConfigUdldStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaUdldPortConfigUdldStatus.setStatus("current")


class _AlaUdldPortConfigUdldMode_Type(Integer32):
    """Custom type alaUdldPortConfigUdldMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggressive", 2),
          ("normal", 1))
    )


_AlaUdldPortConfigUdldMode_Type.__name__ = "Integer32"
_AlaUdldPortConfigUdldMode_Object = MibTableColumn
alaUdldPortConfigUdldMode = _AlaUdldPortConfigUdldMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 6, 1, 1, 3),
    _AlaUdldPortConfigUdldMode_Type()
)
alaUdldPortConfigUdldMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaUdldPortConfigUdldMode.setStatus("current")


class _AlaUdldPortConfigUdldProbeIntervalTimer_Type(Unsigned32):
    """Custom type alaUdldPortConfigUdldProbeIntervalTimer based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 90),
    )


_AlaUdldPortConfigUdldProbeIntervalTimer_Type.__name__ = "Unsigned32"
_AlaUdldPortConfigUdldProbeIntervalTimer_Object = MibTableColumn
alaUdldPortConfigUdldProbeIntervalTimer = _AlaUdldPortConfigUdldProbeIntervalTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 6, 1, 1, 4),
    _AlaUdldPortConfigUdldProbeIntervalTimer_Type()
)
alaUdldPortConfigUdldProbeIntervalTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaUdldPortConfigUdldProbeIntervalTimer.setStatus("current")
if mibBuilder.loadTexts:
    alaUdldPortConfigUdldProbeIntervalTimer.setUnits("seconds")


class _AlaUdldPortConfigUdldDetectionPeriodTimer_Type(Unsigned32):
    """Custom type alaUdldPortConfigUdldDetectionPeriodTimer based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 15),
    )


_AlaUdldPortConfigUdldDetectionPeriodTimer_Type.__name__ = "Unsigned32"
_AlaUdldPortConfigUdldDetectionPeriodTimer_Object = MibTableColumn
alaUdldPortConfigUdldDetectionPeriodTimer = _AlaUdldPortConfigUdldDetectionPeriodTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 6, 1, 1, 5),
    _AlaUdldPortConfigUdldDetectionPeriodTimer_Type()
)
alaUdldPortConfigUdldDetectionPeriodTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaUdldPortConfigUdldDetectionPeriodTimer.setStatus("current")
if mibBuilder.loadTexts:
    alaUdldPortConfigUdldDetectionPeriodTimer.setUnits("seconds")


class _AlaUdldPortConfigUdldOperationalStatus_Type(Integer32):
    """Custom type alaUdldPortConfigUdldOperationalStatus based on Integer32"""
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
        *(("bidirectional", 3),
          ("notapplicable", 0),
          ("shutdown", 1),
          ("undetermined", 2))
    )


_AlaUdldPortConfigUdldOperationalStatus_Type.__name__ = "Integer32"
_AlaUdldPortConfigUdldOperationalStatus_Object = MibTableColumn
alaUdldPortConfigUdldOperationalStatus = _AlaUdldPortConfigUdldOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 6, 1, 1, 6),
    _AlaUdldPortConfigUdldOperationalStatus_Type()
)
alaUdldPortConfigUdldOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaUdldPortConfigUdldOperationalStatus.setStatus("current")
_UdldPortStats_ObjectIdentity = ObjectIdentity
udldPortStats = _UdldPortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 7)
)
_AlaUdldPortStatsTable_Object = MibTable
alaUdldPortStatsTable = _AlaUdldPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    alaUdldPortStatsTable.setStatus("current")
_AlaUdldPortStatsEntry_Object = MibTableRow
alaUdldPortStatsEntry = _AlaUdldPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 7, 1, 1)
)
alaUdldPortStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-UDLD-MIB", "alaUdldPortStatsIfIndex"),
)
if mibBuilder.loadTexts:
    alaUdldPortStatsEntry.setStatus("current")
_AlaUdldPortStatsIfIndex_Type = InterfaceIndex
_AlaUdldPortStatsIfIndex_Object = MibTableColumn
alaUdldPortStatsIfIndex = _AlaUdldPortStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 7, 1, 1, 1),
    _AlaUdldPortStatsIfIndex_Type()
)
alaUdldPortStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaUdldPortStatsIfIndex.setStatus("current")


class _AlaUdldNumUDLDNeighbors_Type(Unsigned32):
    """Custom type alaUdldNumUDLDNeighbors based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AlaUdldNumUDLDNeighbors_Type.__name__ = "Unsigned32"
_AlaUdldNumUDLDNeighbors_Object = MibTableColumn
alaUdldNumUDLDNeighbors = _AlaUdldNumUDLDNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 7, 1, 1, 2),
    _AlaUdldNumUDLDNeighbors_Type()
)
alaUdldNumUDLDNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaUdldNumUDLDNeighbors.setStatus("current")


class _AlaUdldPortStatsClear_Type(Integer32):
    """Custom type alaUdldPortStatsClear based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaUdldPortStatsClear_Type.__name__ = "Integer32"
_AlaUdldPortStatsClear_Object = MibTableColumn
alaUdldPortStatsClear = _AlaUdldPortStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 7, 1, 1, 3),
    _AlaUdldPortStatsClear_Type()
)
alaUdldPortStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaUdldPortStatsClear.setStatus("current")
_AlaUdldPortNumProbeSent_Type = Counter32
_AlaUdldPortNumProbeSent_Object = MibTableColumn
alaUdldPortNumProbeSent = _AlaUdldPortNumProbeSent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 7, 1, 1, 4),
    _AlaUdldPortNumProbeSent_Type()
)
alaUdldPortNumProbeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaUdldPortNumProbeSent.setStatus("current")
_AlaUdldPortNumEchoSent_Type = Counter32
_AlaUdldPortNumEchoSent_Object = MibTableColumn
alaUdldPortNumEchoSent = _AlaUdldPortNumEchoSent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 7, 1, 1, 5),
    _AlaUdldPortNumEchoSent_Type()
)
alaUdldPortNumEchoSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaUdldPortNumEchoSent.setStatus("current")
_AlaUdldPortNumInvalidRcvd_Type = Counter32
_AlaUdldPortNumInvalidRcvd_Object = MibTableColumn
alaUdldPortNumInvalidRcvd = _AlaUdldPortNumInvalidRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 7, 1, 1, 6),
    _AlaUdldPortNumInvalidRcvd_Type()
)
alaUdldPortNumInvalidRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaUdldPortNumInvalidRcvd.setStatus("current")
_AlaUdldPortNumFlushRcvd_Type = Counter32
_AlaUdldPortNumFlushRcvd_Object = MibTableColumn
alaUdldPortNumFlushRcvd = _AlaUdldPortNumFlushRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 7, 1, 1, 7),
    _AlaUdldPortNumFlushRcvd_Type()
)
alaUdldPortNumFlushRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaUdldPortNumFlushRcvd.setStatus("current")
_UdldPortNeighborStats_ObjectIdentity = ObjectIdentity
udldPortNeighborStats = _UdldPortNeighborStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 8)
)
_AlaUdldPortNeighborStatsTable_Object = MibTable
alaUdldPortNeighborStatsTable = _AlaUdldPortNeighborStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    alaUdldPortNeighborStatsTable.setStatus("current")
_AlaUdldPortNeighborStatsEntry_Object = MibTableRow
alaUdldPortNeighborStatsEntry = _AlaUdldPortNeighborStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 8, 1, 1)
)
alaUdldPortNeighborStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-UDLD-MIB", "alaUdldPortNeighborStatsIfIndex"),
    (0, "ALCATEL-IND1-UDLD-MIB", "alaUdldNeighborIfIndex"),
)
if mibBuilder.loadTexts:
    alaUdldPortNeighborStatsEntry.setStatus("current")
_AlaUdldPortNeighborStatsIfIndex_Type = InterfaceIndex
_AlaUdldPortNeighborStatsIfIndex_Object = MibTableColumn
alaUdldPortNeighborStatsIfIndex = _AlaUdldPortNeighborStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 8, 1, 1, 1),
    _AlaUdldPortNeighborStatsIfIndex_Type()
)
alaUdldPortNeighborStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaUdldPortNeighborStatsIfIndex.setStatus("current")


class _AlaUdldNeighborIfIndex_Type(Unsigned32):
    """Custom type alaUdldNeighborIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_AlaUdldNeighborIfIndex_Type.__name__ = "Unsigned32"
_AlaUdldNeighborIfIndex_Object = MibTableColumn
alaUdldNeighborIfIndex = _AlaUdldNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 8, 1, 1, 2),
    _AlaUdldNeighborIfIndex_Type()
)
alaUdldNeighborIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaUdldNeighborIfIndex.setStatus("current")


class _AlaUdldNeighborName_Type(SnmpAdminString):
    """Custom type alaUdldNeighborName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaUdldNeighborName_Type.__name__ = "SnmpAdminString"
_AlaUdldNeighborName_Object = MibTableColumn
alaUdldNeighborName = _AlaUdldNeighborName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 8, 1, 1, 3),
    _AlaUdldNeighborName_Type()
)
alaUdldNeighborName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaUdldNeighborName.setStatus("current")
_AlaUdldNumHelloRcvd_Type = Counter32
_AlaUdldNumHelloRcvd_Object = MibTableColumn
alaUdldNumHelloRcvd = _AlaUdldNumHelloRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 8, 1, 1, 4),
    _AlaUdldNumHelloRcvd_Type()
)
alaUdldNumHelloRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaUdldNumHelloRcvd.setStatus("current")
_AlaUdldNumEchoRcvd_Type = Counter32
_AlaUdldNumEchoRcvd_Object = MibTableColumn
alaUdldNumEchoRcvd = _AlaUdldNumEchoRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 8, 1, 1, 5),
    _AlaUdldNumEchoRcvd_Type()
)
alaUdldNumEchoRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaUdldNumEchoRcvd.setStatus("current")


class _AlaUdldPrevState_Type(Integer32):
    """Custom type alaUdldPrevState based on Integer32"""
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
        *(("bidirectional", 3),
          ("notapplicable", 0),
          ("shutdown", 1),
          ("undetermined", 2))
    )


_AlaUdldPrevState_Type.__name__ = "Integer32"
_AlaUdldPrevState_Object = MibScalar
alaUdldPrevState = _AlaUdldPrevState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 9),
    _AlaUdldPrevState_Type()
)
alaUdldPrevState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaUdldPrevState.setStatus("current")


class _AlaUdldCurrentState_Type(Integer32):
    """Custom type alaUdldCurrentState based on Integer32"""
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
        *(("bidirectional", 3),
          ("notapplicable", 0),
          ("shutdown", 1),
          ("undetermined", 2))
    )


_AlaUdldCurrentState_Type.__name__ = "Integer32"
_AlaUdldCurrentState_Object = MibScalar
alaUdldCurrentState = _AlaUdldCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 10),
    _AlaUdldCurrentState_Type()
)
alaUdldCurrentState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaUdldCurrentState.setStatus("current")
_AlaUdldPortIfIndex_Type = InterfaceIndex
_AlaUdldPortIfIndex_Object = MibScalar
alaUdldPortIfIndex = _AlaUdldPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 1, 11),
    _AlaUdldPortIfIndex_Type()
)
alaUdldPortIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaUdldPortIfIndex.setStatus("current")
_AlcatelIND1UDLDMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1UDLDMIBConformance = _AlcatelIND1UDLDMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1UDLDMIBConformance.setStatus("current")
_AlcatelIND1UDLDMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1UDLDMIBGroups = _AlcatelIND1UDLDMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1UDLDMIBGroups.setStatus("current")
_AlcatelIND1UDLDMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1UDLDMIBCompliances = _AlcatelIND1UDLDMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1UDLDMIBCompliances.setStatus("current")
_AlaUdldEvents_ObjectIdentity = ObjectIdentity
alaUdldEvents = _AlaUdldEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 3)
)

# Managed Objects groups

udldPortBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 2, 1, 1)
)
udldPortBaseGroup.setObjects(
      *(("ALCATEL-IND1-UDLD-MIB", "alaUdldGlobalStatus"),
        ("ALCATEL-IND1-UDLD-MIB", "alaUdldGlobalClearStats"),
        ("ALCATEL-IND1-UDLD-MIB", "alaUdldGlobalConfigUdldMode"),
        ("ALCATEL-IND1-UDLD-MIB", "alaUdldGlobalConfigUdldProbeIntervalTimer"),
        ("ALCATEL-IND1-UDLD-MIB", "alaUdldGlobalConfigUdldDetectionPeriodTimer"),
        ("ALCATEL-IND1-UDLD-MIB", "alaUdldPrevState"),
        ("ALCATEL-IND1-UDLD-MIB", "alaUdldCurrentState"),
        ("ALCATEL-IND1-UDLD-MIB", "alaUdldPortIfIndex"))
)
if mibBuilder.loadTexts:
    udldPortBaseGroup.setStatus("current")

udldPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 2, 1, 2)
)
udldPortConfigGroup.setObjects(
      *(("ALCATEL-IND1-UDLD-MIB", "alaUdldPortConfigUdldStatus"),
        ("ALCATEL-IND1-UDLD-MIB", "alaUdldPortConfigUdldMode"),
        ("ALCATEL-IND1-UDLD-MIB", "alaUdldPortConfigUdldProbeIntervalTimer"),
        ("ALCATEL-IND1-UDLD-MIB", "alaUdldPortConfigUdldDetectionPeriodTimer"),
        ("ALCATEL-IND1-UDLD-MIB", "alaUdldPortConfigUdldOperationalStatus"))
)
if mibBuilder.loadTexts:
    udldPortConfigGroup.setStatus("current")

udldPortStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 2, 1, 3)
)
udldPortStatsGroup.setObjects(
      *(("ALCATEL-IND1-UDLD-MIB", "alaUdldNumUDLDNeighbors"),
        ("ALCATEL-IND1-UDLD-MIB", "alaUdldPortStatsClear"),
        ("ALCATEL-IND1-UDLD-MIB", "alaUdldPortNumProbeSent"),
        ("ALCATEL-IND1-UDLD-MIB", "alaUdldPortNumEchoSent"),
        ("ALCATEL-IND1-UDLD-MIB", "alaUdldPortNumInvalidRcvd"),
        ("ALCATEL-IND1-UDLD-MIB", "alaUdldPortNumFlushRcvd"))
)
if mibBuilder.loadTexts:
    udldPortStatsGroup.setStatus("current")

udldPortNeighborStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 2, 1, 4)
)
udldPortNeighborStatsGroup.setObjects(
      *(("ALCATEL-IND1-UDLD-MIB", "alaUdldNeighborName"),
        ("ALCATEL-IND1-UDLD-MIB", "alaUdldNumHelloRcvd"),
        ("ALCATEL-IND1-UDLD-MIB", "alaUdldNumEchoRcvd"))
)
if mibBuilder.loadTexts:
    udldPortNeighborStatsGroup.setStatus("current")


# Notification objects

udldStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 3, 0, 1)
)
udldStateChange.setObjects(
      *(("ALCATEL-IND1-UDLD-MIB", "alaUdldPortIfIndex"),
        ("ALCATEL-IND1-UDLD-MIB", "alaUdldPrevState"),
        ("ALCATEL-IND1-UDLD-MIB", "alaUdldCurrentState"))
)
if mibBuilder.loadTexts:
    udldStateChange.setStatus(
        "current"
    )


# Notifications groups

udldPortTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 2, 1, 5)
)
udldPortTrapGroup.setObjects(
    ("ALCATEL-IND1-UDLD-MIB", "udldStateChange")
)
if mibBuilder.loadTexts:
    udldPortTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1UDLDMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1UDLDMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-UDLD-MIB",
    **{"alcatelIND1UDLDMIB": alcatelIND1UDLDMIB,
       "alcatelIND1UDLDMIBObjects": alcatelIND1UDLDMIBObjects,
       "alaUdldGlobalStatus": alaUdldGlobalStatus,
       "alaUdldGlobalClearStats": alaUdldGlobalClearStats,
       "alaUdldGlobalConfigUdldMode": alaUdldGlobalConfigUdldMode,
       "alaUdldGlobalConfigUdldProbeIntervalTimer": alaUdldGlobalConfigUdldProbeIntervalTimer,
       "alaUdldGlobalConfigUdldDetectionPeriodTimer": alaUdldGlobalConfigUdldDetectionPeriodTimer,
       "udldPortConfig": udldPortConfig,
       "alaUdldPortConfigTable": alaUdldPortConfigTable,
       "alaUdldPortConfigEntry": alaUdldPortConfigEntry,
       "alaUdldPortConfigIfIndex": alaUdldPortConfigIfIndex,
       "alaUdldPortConfigUdldStatus": alaUdldPortConfigUdldStatus,
       "alaUdldPortConfigUdldMode": alaUdldPortConfigUdldMode,
       "alaUdldPortConfigUdldProbeIntervalTimer": alaUdldPortConfigUdldProbeIntervalTimer,
       "alaUdldPortConfigUdldDetectionPeriodTimer": alaUdldPortConfigUdldDetectionPeriodTimer,
       "alaUdldPortConfigUdldOperationalStatus": alaUdldPortConfigUdldOperationalStatus,
       "udldPortStats": udldPortStats,
       "alaUdldPortStatsTable": alaUdldPortStatsTable,
       "alaUdldPortStatsEntry": alaUdldPortStatsEntry,
       "alaUdldPortStatsIfIndex": alaUdldPortStatsIfIndex,
       "alaUdldNumUDLDNeighbors": alaUdldNumUDLDNeighbors,
       "alaUdldPortStatsClear": alaUdldPortStatsClear,
       "alaUdldPortNumProbeSent": alaUdldPortNumProbeSent,
       "alaUdldPortNumEchoSent": alaUdldPortNumEchoSent,
       "alaUdldPortNumInvalidRcvd": alaUdldPortNumInvalidRcvd,
       "alaUdldPortNumFlushRcvd": alaUdldPortNumFlushRcvd,
       "udldPortNeighborStats": udldPortNeighborStats,
       "alaUdldPortNeighborStatsTable": alaUdldPortNeighborStatsTable,
       "alaUdldPortNeighborStatsEntry": alaUdldPortNeighborStatsEntry,
       "alaUdldPortNeighborStatsIfIndex": alaUdldPortNeighborStatsIfIndex,
       "alaUdldNeighborIfIndex": alaUdldNeighborIfIndex,
       "alaUdldNeighborName": alaUdldNeighborName,
       "alaUdldNumHelloRcvd": alaUdldNumHelloRcvd,
       "alaUdldNumEchoRcvd": alaUdldNumEchoRcvd,
       "alaUdldPrevState": alaUdldPrevState,
       "alaUdldCurrentState": alaUdldCurrentState,
       "alaUdldPortIfIndex": alaUdldPortIfIndex,
       "alcatelIND1UDLDMIBConformance": alcatelIND1UDLDMIBConformance,
       "alcatelIND1UDLDMIBGroups": alcatelIND1UDLDMIBGroups,
       "udldPortBaseGroup": udldPortBaseGroup,
       "udldPortConfigGroup": udldPortConfigGroup,
       "udldPortStatsGroup": udldPortStatsGroup,
       "udldPortNeighborStatsGroup": udldPortNeighborStatsGroup,
       "udldPortTrapGroup": udldPortTrapGroup,
       "alcatelIND1UDLDMIBCompliances": alcatelIND1UDLDMIBCompliances,
       "alcatelIND1UDLDMIBCompliance": alcatelIND1UDLDMIBCompliance,
       "alaUdldEvents": alaUdldEvents,
       "udldStateChange": udldStateChange}
)
