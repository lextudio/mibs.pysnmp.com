# SNMP MIB module (PDN-HDSL2-SHDSL-LINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-HDSL2-SHDSL-LINE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:42 2024
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

(Hdsl2Shdsl1DayIntervalCount,
 Hdsl2ShdslPerfCurrDayCount,
 Hdsl2ShdslPerfTimeElapsed,
 hdsl2ShdslEndpointSide,
 hdsl2ShdslEndpointThreshCRCanomalies,
 hdsl2ShdslEndpointThreshES,
 hdsl2ShdslEndpointThreshLOSWS,
 hdsl2ShdslEndpointThreshLoopAttenuation,
 hdsl2ShdslEndpointThreshSES,
 hdsl2ShdslEndpointThreshSNRMargin,
 hdsl2ShdslEndpointThreshUAS,
 hdsl2ShdslInvIndex,
 hdsl2ShdslSpanConfProfileName) = mibBuilder.importSymbols(
    "HDSL2-SHDSL-LINE-MIB",
    "Hdsl2Shdsl1DayIntervalCount",
    "Hdsl2ShdslPerfCurrDayCount",
    "Hdsl2ShdslPerfTimeElapsed",
    "hdsl2ShdslEndpointSide",
    "hdsl2ShdslEndpointThreshCRCanomalies",
    "hdsl2ShdslEndpointThreshES",
    "hdsl2ShdslEndpointThreshLOSWS",
    "hdsl2ShdslEndpointThreshLoopAttenuation",
    "hdsl2ShdslEndpointThreshSES",
    "hdsl2ShdslEndpointThreshSNRMargin",
    "hdsl2ShdslEndpointThreshUAS",
    "hdsl2ShdslInvIndex",
    "hdsl2ShdslSpanConfProfileName")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(pdn_interfaces,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-interfaces")

(PerfCurrentCount,
 PerfIntervalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount")

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

pdnHdsl2ShdslLineMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23)
)
pdnHdsl2ShdslLineMIB.setRevisions(
        ("2005-01-28 00:00",
         "2004-04-27 00:00",
         "2004-04-21 00:00",
         "2004-01-16 15:00",
         "2003-11-06 15:00",
         "2003-10-23 15:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PdnHdsl2ShdslWirePair(Integer32, TextualConvention):
    status = "current"
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
        *(("wirePair1", 1),
          ("wirePair2", 2),
          ("wirePair3", 3),
          ("wirePair4", 4))
    )



# MIB Managed Objects in the order of their OIDs

_PdnHdsl2ShdslLineNotifications_ObjectIdentity = ObjectIdentity
pdnHdsl2ShdslLineNotifications = _PdnHdsl2ShdslLineNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 0)
)
_PdnHdsl2ShdslLineObjects_ObjectIdentity = ObjectIdentity
pdnHdsl2ShdslLineObjects = _PdnHdsl2ShdslLineObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1)
)
_PdnHdsl2ShdslSpanStatusExtTable_Object = MibTable
pdnHdsl2ShdslSpanStatusExtTable = _PdnHdsl2ShdslSpanStatusExtTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 1)
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdslSpanStatusExtTable.setStatus("current")
_PdnHdsl2ShdslSpanStatusExtEntry_Object = MibTableRow
pdnHdsl2ShdslSpanStatusExtEntry = _PdnHdsl2ShdslSpanStatusExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 1, 1)
)
pdnHdsl2ShdslSpanStatusExtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdslSpanStatusExtEntry.setStatus("current")
_PdnHdsl2ShdslStatusMaxAttainableLineRate_Type = Unsigned32
_PdnHdsl2ShdslStatusMaxAttainableLineRate_Object = MibTableColumn
pdnHdsl2ShdslStatusMaxAttainableLineRate = _PdnHdsl2ShdslStatusMaxAttainableLineRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 1, 1, 1),
    _PdnHdsl2ShdslStatusMaxAttainableLineRate_Type()
)
pdnHdsl2ShdslStatusMaxAttainableLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslStatusMaxAttainableLineRate.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslStatusMaxAttainableLineRate.setUnits("bps")
_PdnHdsl2ShdslStatusActualLineRate_Type = Unsigned32
_PdnHdsl2ShdslStatusActualLineRate_Object = MibTableColumn
pdnHdsl2ShdslStatusActualLineRate = _PdnHdsl2ShdslStatusActualLineRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 1, 1, 2),
    _PdnHdsl2ShdslStatusActualLineRate_Type()
)
pdnHdsl2ShdslStatusActualLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslStatusActualLineRate.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslStatusActualLineRate.setUnits("bps")
_PdnHdsl2ShdslEndpointConfTable_Object = MibTable
pdnHdsl2ShdslEndpointConfTable = _PdnHdsl2ShdslEndpointConfTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 2)
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointConfTable.setStatus("current")
_PdnHdsl2ShdslEndpointConfEntry_Object = MibTableRow
pdnHdsl2ShdslEndpointConfEntry = _PdnHdsl2ShdslEndpointConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 2, 1)
)
pdnHdsl2ShdslEndpointConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslInvIndex"),
    (0, "HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointSide"),
    (0, "PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointWirePair"),
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointConfEntry.setStatus("current")
_PdnHdsl2ShdslEndpointWirePair_Type = PdnHdsl2ShdslWirePair
_PdnHdsl2ShdslEndpointWirePair_Object = MibTableColumn
pdnHdsl2ShdslEndpointWirePair = _PdnHdsl2ShdslEndpointWirePair_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 2, 1, 1),
    _PdnHdsl2ShdslEndpointWirePair_Type()
)
pdnHdsl2ShdslEndpointWirePair.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointWirePair.setStatus("current")


class _PdnHdsl2ShdslEndpointAlarmConfProfile_Type(SnmpAdminString):
    """Custom type pdnHdsl2ShdslEndpointAlarmConfProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PdnHdsl2ShdslEndpointAlarmConfProfile_Type.__name__ = "SnmpAdminString"
_PdnHdsl2ShdslEndpointAlarmConfProfile_Object = MibTableColumn
pdnHdsl2ShdslEndpointAlarmConfProfile = _PdnHdsl2ShdslEndpointAlarmConfProfile_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 2, 1, 2),
    _PdnHdsl2ShdslEndpointAlarmConfProfile_Type()
)
pdnHdsl2ShdslEndpointAlarmConfProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointAlarmConfProfile.setStatus("current")
_PdnHdsl2ShdslEndpointCurrTable_Object = MibTable
pdnHdsl2ShdslEndpointCurrTable = _PdnHdsl2ShdslEndpointCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 3)
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurrTable.setStatus("current")
_PdnHdsl2ShdslEndpointCurrEntry_Object = MibTableRow
pdnHdsl2ShdslEndpointCurrEntry = _PdnHdsl2ShdslEndpointCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 3, 1)
)
pdnHdsl2ShdslEndpointCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslInvIndex"),
    (0, "HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointSide"),
    (0, "PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointWirePair"),
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurrEntry.setStatus("current")


class _PdnHdsl2ShdslEndpointCurrAtn_Type(Integer32):
    """Custom type pdnHdsl2ShdslEndpointCurrAtn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 128),
    )


_PdnHdsl2ShdslEndpointCurrAtn_Type.__name__ = "Integer32"
_PdnHdsl2ShdslEndpointCurrAtn_Object = MibTableColumn
pdnHdsl2ShdslEndpointCurrAtn = _PdnHdsl2ShdslEndpointCurrAtn_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 3, 1, 1),
    _PdnHdsl2ShdslEndpointCurrAtn_Type()
)
pdnHdsl2ShdslEndpointCurrAtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurrAtn.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurrAtn.setUnits("dB")


class _PdnHdsl2ShdslEndpointCurrSnrMgn_Type(Integer32):
    """Custom type pdnHdsl2ShdslEndpointCurrSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 128),
    )


_PdnHdsl2ShdslEndpointCurrSnrMgn_Type.__name__ = "Integer32"
_PdnHdsl2ShdslEndpointCurrSnrMgn_Object = MibTableColumn
pdnHdsl2ShdslEndpointCurrSnrMgn = _PdnHdsl2ShdslEndpointCurrSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 3, 1, 2),
    _PdnHdsl2ShdslEndpointCurrSnrMgn_Type()
)
pdnHdsl2ShdslEndpointCurrSnrMgn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurrSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurrSnrMgn.setUnits("dB")


class _PdnHdsl2ShdslEndpointCurrStatus_Type(Bits):
    """Custom type pdnHdsl2ShdslEndpointCurrStatus based on Bits"""
    namedValues = NamedValues(
        *(("configInitFailure", 7),
          ("dcContinuityFault", 3),
          ("deviceFault", 2),
          ("loopAttenuationAlarm", 5),
          ("loopbackActive", 10),
          ("loswFailureAlarm", 6),
          ("noDefect", 0),
          ("noNeighborPresent", 9),
          ("powerBackoff", 1),
          ("protocolInitFailure", 8),
          ("snrMarginAlarm", 4))
    )

_PdnHdsl2ShdslEndpointCurrStatus_Type.__name__ = "Bits"
_PdnHdsl2ShdslEndpointCurrStatus_Object = MibTableColumn
pdnHdsl2ShdslEndpointCurrStatus = _PdnHdsl2ShdslEndpointCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 3, 1, 3),
    _PdnHdsl2ShdslEndpointCurrStatus_Type()
)
pdnHdsl2ShdslEndpointCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurrStatus.setStatus("current")
_PdnHdsl2ShdslEndpointES_Type = Counter32
_PdnHdsl2ShdslEndpointES_Object = MibTableColumn
pdnHdsl2ShdslEndpointES = _PdnHdsl2ShdslEndpointES_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 3, 1, 4),
    _PdnHdsl2ShdslEndpointES_Type()
)
pdnHdsl2ShdslEndpointES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointES.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointES.setUnits("seconds")
_PdnHdsl2ShdslEndpointSES_Type = Counter32
_PdnHdsl2ShdslEndpointSES_Object = MibTableColumn
pdnHdsl2ShdslEndpointSES = _PdnHdsl2ShdslEndpointSES_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 3, 1, 5),
    _PdnHdsl2ShdslEndpointSES_Type()
)
pdnHdsl2ShdslEndpointSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointSES.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointSES.setUnits("seconds")
_PdnHdsl2ShdslEndpointCRCanomalies_Type = Counter32
_PdnHdsl2ShdslEndpointCRCanomalies_Object = MibTableColumn
pdnHdsl2ShdslEndpointCRCanomalies = _PdnHdsl2ShdslEndpointCRCanomalies_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 3, 1, 6),
    _PdnHdsl2ShdslEndpointCRCanomalies_Type()
)
pdnHdsl2ShdslEndpointCRCanomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCRCanomalies.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCRCanomalies.setUnits("detected CRC Anomalies")
_PdnHdsl2ShdslEndpointLOSWS_Type = Counter32
_PdnHdsl2ShdslEndpointLOSWS_Object = MibTableColumn
pdnHdsl2ShdslEndpointLOSWS = _PdnHdsl2ShdslEndpointLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 3, 1, 7),
    _PdnHdsl2ShdslEndpointLOSWS_Type()
)
pdnHdsl2ShdslEndpointLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointLOSWS.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointLOSWS.setUnits("seconds")
_PdnHdsl2ShdslEndpointUAS_Type = Counter32
_PdnHdsl2ShdslEndpointUAS_Object = MibTableColumn
pdnHdsl2ShdslEndpointUAS = _PdnHdsl2ShdslEndpointUAS_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 3, 1, 8),
    _PdnHdsl2ShdslEndpointUAS_Type()
)
pdnHdsl2ShdslEndpointUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointUAS.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointUAS.setUnits("seconds")
_PdnHdsl2ShdslEndpointCurr15MinTimeElapsed_Type = Hdsl2ShdslPerfTimeElapsed
_PdnHdsl2ShdslEndpointCurr15MinTimeElapsed_Object = MibTableColumn
pdnHdsl2ShdslEndpointCurr15MinTimeElapsed = _PdnHdsl2ShdslEndpointCurr15MinTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 3, 1, 9),
    _PdnHdsl2ShdslEndpointCurr15MinTimeElapsed_Type()
)
pdnHdsl2ShdslEndpointCurr15MinTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurr15MinTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurr15MinTimeElapsed.setUnits("seconds")
_PdnHdsl2ShdslEndpointCurr15MinES_Type = PerfCurrentCount
_PdnHdsl2ShdslEndpointCurr15MinES_Object = MibTableColumn
pdnHdsl2ShdslEndpointCurr15MinES = _PdnHdsl2ShdslEndpointCurr15MinES_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 3, 1, 10),
    _PdnHdsl2ShdslEndpointCurr15MinES_Type()
)
pdnHdsl2ShdslEndpointCurr15MinES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurr15MinES.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurr15MinES.setUnits("seconds")
_PdnHdsl2ShdslEndpointCurr15MinSES_Type = PerfCurrentCount
_PdnHdsl2ShdslEndpointCurr15MinSES_Object = MibTableColumn
pdnHdsl2ShdslEndpointCurr15MinSES = _PdnHdsl2ShdslEndpointCurr15MinSES_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 3, 1, 11),
    _PdnHdsl2ShdslEndpointCurr15MinSES_Type()
)
pdnHdsl2ShdslEndpointCurr15MinSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurr15MinSES.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurr15MinSES.setUnits("seconds")
_PdnHdsl2ShdslEndpointCurr15MinCRCanomalies_Type = PerfCurrentCount
_PdnHdsl2ShdslEndpointCurr15MinCRCanomalies_Object = MibTableColumn
pdnHdsl2ShdslEndpointCurr15MinCRCanomalies = _PdnHdsl2ShdslEndpointCurr15MinCRCanomalies_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 3, 1, 12),
    _PdnHdsl2ShdslEndpointCurr15MinCRCanomalies_Type()
)
pdnHdsl2ShdslEndpointCurr15MinCRCanomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurr15MinCRCanomalies.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurr15MinCRCanomalies.setUnits("detected CRC Anomalies")
_PdnHdsl2ShdslEndpointCurr15MinLOSWS_Type = PerfCurrentCount
_PdnHdsl2ShdslEndpointCurr15MinLOSWS_Object = MibTableColumn
pdnHdsl2ShdslEndpointCurr15MinLOSWS = _PdnHdsl2ShdslEndpointCurr15MinLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 3, 1, 13),
    _PdnHdsl2ShdslEndpointCurr15MinLOSWS_Type()
)
pdnHdsl2ShdslEndpointCurr15MinLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurr15MinLOSWS.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurr15MinLOSWS.setUnits("seconds")
_PdnHdsl2ShdslEndpointCurr15MinUAS_Type = PerfCurrentCount
_PdnHdsl2ShdslEndpointCurr15MinUAS_Object = MibTableColumn
pdnHdsl2ShdslEndpointCurr15MinUAS = _PdnHdsl2ShdslEndpointCurr15MinUAS_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 3, 1, 14),
    _PdnHdsl2ShdslEndpointCurr15MinUAS_Type()
)
pdnHdsl2ShdslEndpointCurr15MinUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurr15MinUAS.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurr15MinUAS.setUnits("seconds")
_PdnHdsl2ShdslEndpointCurr1DayTimeElapsed_Type = Hdsl2ShdslPerfTimeElapsed
_PdnHdsl2ShdslEndpointCurr1DayTimeElapsed_Object = MibTableColumn
pdnHdsl2ShdslEndpointCurr1DayTimeElapsed = _PdnHdsl2ShdslEndpointCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 3, 1, 15),
    _PdnHdsl2ShdslEndpointCurr1DayTimeElapsed_Type()
)
pdnHdsl2ShdslEndpointCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurr1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurr1DayTimeElapsed.setUnits("seconds")
_PdnHdsl2ShdslEndpointCurr1DayES_Type = Hdsl2ShdslPerfCurrDayCount
_PdnHdsl2ShdslEndpointCurr1DayES_Object = MibTableColumn
pdnHdsl2ShdslEndpointCurr1DayES = _PdnHdsl2ShdslEndpointCurr1DayES_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 3, 1, 16),
    _PdnHdsl2ShdslEndpointCurr1DayES_Type()
)
pdnHdsl2ShdslEndpointCurr1DayES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurr1DayES.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurr1DayES.setUnits("seconds")
_PdnHdsl2ShdslEndpointCurr1DaySES_Type = Hdsl2ShdslPerfCurrDayCount
_PdnHdsl2ShdslEndpointCurr1DaySES_Object = MibTableColumn
pdnHdsl2ShdslEndpointCurr1DaySES = _PdnHdsl2ShdslEndpointCurr1DaySES_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 3, 1, 17),
    _PdnHdsl2ShdslEndpointCurr1DaySES_Type()
)
pdnHdsl2ShdslEndpointCurr1DaySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurr1DaySES.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurr1DaySES.setUnits("seconds")
_PdnHdsl2ShdslEndpointCurr1DayCRCanomalies_Type = Hdsl2ShdslPerfCurrDayCount
_PdnHdsl2ShdslEndpointCurr1DayCRCanomalies_Object = MibTableColumn
pdnHdsl2ShdslEndpointCurr1DayCRCanomalies = _PdnHdsl2ShdslEndpointCurr1DayCRCanomalies_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 3, 1, 18),
    _PdnHdsl2ShdslEndpointCurr1DayCRCanomalies_Type()
)
pdnHdsl2ShdslEndpointCurr1DayCRCanomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurr1DayCRCanomalies.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurr1DayCRCanomalies.setUnits("detected CRC Anomalies")
_PdnHdsl2ShdslEndpointCurr1DayLOSWS_Type = Hdsl2ShdslPerfCurrDayCount
_PdnHdsl2ShdslEndpointCurr1DayLOSWS_Object = MibTableColumn
pdnHdsl2ShdslEndpointCurr1DayLOSWS = _PdnHdsl2ShdslEndpointCurr1DayLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 3, 1, 19),
    _PdnHdsl2ShdslEndpointCurr1DayLOSWS_Type()
)
pdnHdsl2ShdslEndpointCurr1DayLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurr1DayLOSWS.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurr1DayLOSWS.setUnits("seconds")
_PdnHdsl2ShdslEndpointCurr1DayUAS_Type = Hdsl2ShdslPerfCurrDayCount
_PdnHdsl2ShdslEndpointCurr1DayUAS_Object = MibTableColumn
pdnHdsl2ShdslEndpointCurr1DayUAS = _PdnHdsl2ShdslEndpointCurr1DayUAS_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 3, 1, 20),
    _PdnHdsl2ShdslEndpointCurr1DayUAS_Type()
)
pdnHdsl2ShdslEndpointCurr1DayUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurr1DayUAS.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurr1DayUAS.setUnits("seconds")
_PdnHdsl2Shdsl15MinIntervalTable_Object = MibTable
pdnHdsl2Shdsl15MinIntervalTable = _PdnHdsl2Shdsl15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 4)
)
if mibBuilder.loadTexts:
    pdnHdsl2Shdsl15MinIntervalTable.setStatus("current")
_PdnHdsl2Shdsl15MinIntervalEntry_Object = MibTableRow
pdnHdsl2Shdsl15MinIntervalEntry = _PdnHdsl2Shdsl15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 4, 1)
)
pdnHdsl2Shdsl15MinIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslInvIndex"),
    (0, "HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointSide"),
    (0, "PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointWirePair"),
    (0, "PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2Shdsl15MinIntervalNumber"),
)
if mibBuilder.loadTexts:
    pdnHdsl2Shdsl15MinIntervalEntry.setStatus("current")


class _PdnHdsl2Shdsl15MinIntervalNumber_Type(Unsigned32):
    """Custom type pdnHdsl2Shdsl15MinIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PdnHdsl2Shdsl15MinIntervalNumber_Type.__name__ = "Unsigned32"
_PdnHdsl2Shdsl15MinIntervalNumber_Object = MibTableColumn
pdnHdsl2Shdsl15MinIntervalNumber = _PdnHdsl2Shdsl15MinIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 4, 1, 1),
    _PdnHdsl2Shdsl15MinIntervalNumber_Type()
)
pdnHdsl2Shdsl15MinIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnHdsl2Shdsl15MinIntervalNumber.setStatus("current")
_PdnHdsl2Shdsl15MinIntervalES_Type = PerfIntervalCount
_PdnHdsl2Shdsl15MinIntervalES_Object = MibTableColumn
pdnHdsl2Shdsl15MinIntervalES = _PdnHdsl2Shdsl15MinIntervalES_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 4, 1, 2),
    _PdnHdsl2Shdsl15MinIntervalES_Type()
)
pdnHdsl2Shdsl15MinIntervalES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2Shdsl15MinIntervalES.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2Shdsl15MinIntervalES.setUnits("seconds")
_PdnHdsl2Shdsl15MinIntervalSES_Type = PerfIntervalCount
_PdnHdsl2Shdsl15MinIntervalSES_Object = MibTableColumn
pdnHdsl2Shdsl15MinIntervalSES = _PdnHdsl2Shdsl15MinIntervalSES_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 4, 1, 3),
    _PdnHdsl2Shdsl15MinIntervalSES_Type()
)
pdnHdsl2Shdsl15MinIntervalSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2Shdsl15MinIntervalSES.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2Shdsl15MinIntervalSES.setUnits("seconds")
_PdnHdsl2Shdsl15MinIntervalCRCanomalies_Type = PerfIntervalCount
_PdnHdsl2Shdsl15MinIntervalCRCanomalies_Object = MibTableColumn
pdnHdsl2Shdsl15MinIntervalCRCanomalies = _PdnHdsl2Shdsl15MinIntervalCRCanomalies_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 4, 1, 4),
    _PdnHdsl2Shdsl15MinIntervalCRCanomalies_Type()
)
pdnHdsl2Shdsl15MinIntervalCRCanomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2Shdsl15MinIntervalCRCanomalies.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2Shdsl15MinIntervalCRCanomalies.setUnits("detected CRC Anomalies")
_PdnHdsl2Shdsl15MinIntervalLOSWS_Type = PerfIntervalCount
_PdnHdsl2Shdsl15MinIntervalLOSWS_Object = MibTableColumn
pdnHdsl2Shdsl15MinIntervalLOSWS = _PdnHdsl2Shdsl15MinIntervalLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 4, 1, 5),
    _PdnHdsl2Shdsl15MinIntervalLOSWS_Type()
)
pdnHdsl2Shdsl15MinIntervalLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2Shdsl15MinIntervalLOSWS.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2Shdsl15MinIntervalLOSWS.setUnits("seconds")
_PdnHdsl2Shdsl15MinIntervalUAS_Type = PerfIntervalCount
_PdnHdsl2Shdsl15MinIntervalUAS_Object = MibTableColumn
pdnHdsl2Shdsl15MinIntervalUAS = _PdnHdsl2Shdsl15MinIntervalUAS_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 4, 1, 6),
    _PdnHdsl2Shdsl15MinIntervalUAS_Type()
)
pdnHdsl2Shdsl15MinIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2Shdsl15MinIntervalUAS.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2Shdsl15MinIntervalUAS.setUnits("seconds")
_PdnHdsl2Shdsl1DayIntervalTable_Object = MibTable
pdnHdsl2Shdsl1DayIntervalTable = _PdnHdsl2Shdsl1DayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 5)
)
if mibBuilder.loadTexts:
    pdnHdsl2Shdsl1DayIntervalTable.setStatus("current")
_PdnHdsl2Shdsl1DayIntervalEntry_Object = MibTableRow
pdnHdsl2Shdsl1DayIntervalEntry = _PdnHdsl2Shdsl1DayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 5, 1)
)
pdnHdsl2Shdsl1DayIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslInvIndex"),
    (0, "HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointSide"),
    (0, "PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointWirePair"),
    (0, "PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2Shdsl1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    pdnHdsl2Shdsl1DayIntervalEntry.setStatus("current")


class _PdnHdsl2Shdsl1DayIntervalNumber_Type(Unsigned32):
    """Custom type pdnHdsl2Shdsl1DayIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_PdnHdsl2Shdsl1DayIntervalNumber_Type.__name__ = "Unsigned32"
_PdnHdsl2Shdsl1DayIntervalNumber_Object = MibTableColumn
pdnHdsl2Shdsl1DayIntervalNumber = _PdnHdsl2Shdsl1DayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 5, 1, 1),
    _PdnHdsl2Shdsl1DayIntervalNumber_Type()
)
pdnHdsl2Shdsl1DayIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnHdsl2Shdsl1DayIntervalNumber.setStatus("current")
_PdnHdsl2Shdsl1DayIntervalMoniSecs_Type = Hdsl2ShdslPerfTimeElapsed
_PdnHdsl2Shdsl1DayIntervalMoniSecs_Object = MibTableColumn
pdnHdsl2Shdsl1DayIntervalMoniSecs = _PdnHdsl2Shdsl1DayIntervalMoniSecs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 5, 1, 2),
    _PdnHdsl2Shdsl1DayIntervalMoniSecs_Type()
)
pdnHdsl2Shdsl1DayIntervalMoniSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2Shdsl1DayIntervalMoniSecs.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2Shdsl1DayIntervalMoniSecs.setUnits("seconds")
_PdnHdsl2Shdsl1DayIntervalES_Type = Hdsl2Shdsl1DayIntervalCount
_PdnHdsl2Shdsl1DayIntervalES_Object = MibTableColumn
pdnHdsl2Shdsl1DayIntervalES = _PdnHdsl2Shdsl1DayIntervalES_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 5, 1, 3),
    _PdnHdsl2Shdsl1DayIntervalES_Type()
)
pdnHdsl2Shdsl1DayIntervalES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2Shdsl1DayIntervalES.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2Shdsl1DayIntervalES.setUnits("seconds")
_PdnHdsl2Shdsl1DayIntervalSES_Type = Hdsl2Shdsl1DayIntervalCount
_PdnHdsl2Shdsl1DayIntervalSES_Object = MibTableColumn
pdnHdsl2Shdsl1DayIntervalSES = _PdnHdsl2Shdsl1DayIntervalSES_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 5, 1, 4),
    _PdnHdsl2Shdsl1DayIntervalSES_Type()
)
pdnHdsl2Shdsl1DayIntervalSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2Shdsl1DayIntervalSES.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2Shdsl1DayIntervalSES.setUnits("seconds")
_PdnHdsl2Shdsl1DayIntervalCRCanomalies_Type = Hdsl2Shdsl1DayIntervalCount
_PdnHdsl2Shdsl1DayIntervalCRCanomalies_Object = MibTableColumn
pdnHdsl2Shdsl1DayIntervalCRCanomalies = _PdnHdsl2Shdsl1DayIntervalCRCanomalies_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 5, 1, 5),
    _PdnHdsl2Shdsl1DayIntervalCRCanomalies_Type()
)
pdnHdsl2Shdsl1DayIntervalCRCanomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2Shdsl1DayIntervalCRCanomalies.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2Shdsl1DayIntervalCRCanomalies.setUnits("detected CRC Anomalies")
_PdnHdsl2Shdsl1DayIntervalLOSWS_Type = Hdsl2Shdsl1DayIntervalCount
_PdnHdsl2Shdsl1DayIntervalLOSWS_Object = MibTableColumn
pdnHdsl2Shdsl1DayIntervalLOSWS = _PdnHdsl2Shdsl1DayIntervalLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 5, 1, 6),
    _PdnHdsl2Shdsl1DayIntervalLOSWS_Type()
)
pdnHdsl2Shdsl1DayIntervalLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2Shdsl1DayIntervalLOSWS.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2Shdsl1DayIntervalLOSWS.setUnits("seconds")
_PdnHdsl2Shdsl1DayIntervalUAS_Type = Hdsl2Shdsl1DayIntervalCount
_PdnHdsl2Shdsl1DayIntervalUAS_Object = MibTableColumn
pdnHdsl2Shdsl1DayIntervalUAS = _PdnHdsl2Shdsl1DayIntervalUAS_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 5, 1, 7),
    _PdnHdsl2Shdsl1DayIntervalUAS_Type()
)
pdnHdsl2Shdsl1DayIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdsl2Shdsl1DayIntervalUAS.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2Shdsl1DayIntervalUAS.setUnits("seconds")
_PdnHdsl2ShdslSpanConfProfileExtTable_Object = MibTable
pdnHdsl2ShdslSpanConfProfileExtTable = _PdnHdsl2ShdslSpanConfProfileExtTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 6)
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdslSpanConfProfileExtTable.setStatus("current")
_PdnHdsl2ShdslSpanConfProfileExtEntry_Object = MibTableRow
pdnHdsl2ShdslSpanConfProfileExtEntry = _PdnHdsl2ShdslSpanConfProfileExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 6, 1)
)
pdnHdsl2ShdslSpanConfProfileExtEntry.setIndexNames(
    (1, "HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslSpanConfProfileName"),
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdslSpanConfProfileExtEntry.setStatus("current")


class _PdnHdsl2ShdslSpanConfWireInterface_Type(Integer32):
    """Custom type pdnHdsl2ShdslSpanConfWireInterface based on Integer32"""
    defaultValue = 1

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
        *(("eightWire", 4),
          ("fourWire", 2),
          ("sixWire", 3),
          ("twoWire", 1))
    )


_PdnHdsl2ShdslSpanConfWireInterface_Type.__name__ = "Integer32"
_PdnHdsl2ShdslSpanConfWireInterface_Object = MibTableColumn
pdnHdsl2ShdslSpanConfWireInterface = _PdnHdsl2ShdslSpanConfWireInterface_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 6, 1, 1),
    _PdnHdsl2ShdslSpanConfWireInterface_Type()
)
pdnHdsl2ShdslSpanConfWireInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslSpanConfWireInterface.setStatus("current")


class _PdnHdsl2ShdslSpanConfMinLineRate_Type(Unsigned32):
    """Custom type pdnHdsl2ShdslSpanConfMinLineRate based on Unsigned32"""
    defaultValue = 155200


_PdnHdsl2ShdslSpanConfMinLineRate_Object = MibTableColumn
pdnHdsl2ShdslSpanConfMinLineRate = _PdnHdsl2ShdslSpanConfMinLineRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 6, 1, 2),
    _PdnHdsl2ShdslSpanConfMinLineRate_Type()
)
pdnHdsl2ShdslSpanConfMinLineRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslSpanConfMinLineRate.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslSpanConfMinLineRate.setUnits("bps")


class _PdnHdsl2ShdslSpanConfMaxLineRate_Type(Unsigned32):
    """Custom type pdnHdsl2ShdslSpanConfMaxLineRate based on Unsigned32"""
    defaultValue = 155200


_PdnHdsl2ShdslSpanConfMaxLineRate_Object = MibTableColumn
pdnHdsl2ShdslSpanConfMaxLineRate = _PdnHdsl2ShdslSpanConfMaxLineRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 6, 1, 3),
    _PdnHdsl2ShdslSpanConfMaxLineRate_Type()
)
pdnHdsl2ShdslSpanConfMaxLineRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslSpanConfMaxLineRate.setStatus("current")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslSpanConfMaxLineRate.setUnits("bps")
_PdnHdsl2ShdslIfTable_Object = MibTable
pdnHdsl2ShdslIfTable = _PdnHdsl2ShdslIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 7)
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdslIfTable.setStatus("current")
_PdnHdsl2ShdslIfEntry_Object = MibTableRow
pdnHdsl2ShdslIfEntry = _PdnHdsl2ShdslIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 7, 1)
)
pdnHdsl2ShdslIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdslIfEntry.setStatus("current")


class _PdnHdsl2ShdslIfTableEquipMode_Type(Integer32):
    """Custom type pdnHdsl2ShdslIfTableEquipMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("coMode", 1),
          ("cpeMode", 2))
    )


_PdnHdsl2ShdslIfTableEquipMode_Type.__name__ = "Integer32"
_PdnHdsl2ShdslIfTableEquipMode_Object = MibTableColumn
pdnHdsl2ShdslIfTableEquipMode = _PdnHdsl2ShdslIfTableEquipMode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 7, 1, 1),
    _PdnHdsl2ShdslIfTableEquipMode_Type()
)
pdnHdsl2ShdslIfTableEquipMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslIfTableEquipMode.setStatus("current")


class _PdnHdsl2ShdslExtendedRateMode_Type(Integer32):
    """Custom type pdnHdsl2ShdslExtendedRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("payload5696", 2))
    )


_PdnHdsl2ShdslExtendedRateMode_Type.__name__ = "Integer32"
_PdnHdsl2ShdslExtendedRateMode_Object = MibScalar
pdnHdsl2ShdslExtendedRateMode = _PdnHdsl2ShdslExtendedRateMode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 1, 8),
    _PdnHdsl2ShdslExtendedRateMode_Type()
)
pdnHdsl2ShdslExtendedRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnHdsl2ShdslExtendedRateMode.setStatus("current")
_PdnHdsl2ShdslLineAFNs_ObjectIdentity = ObjectIdentity
pdnHdsl2ShdslLineAFNs = _PdnHdsl2ShdslLineAFNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 2)
)
_PdnHdsl2ShdslLineConformance_ObjectIdentity = ObjectIdentity
pdnHdsl2ShdslLineConformance = _PdnHdsl2ShdslLineConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 3)
)
_PdnHdsl2ShdslLineCompliances_ObjectIdentity = ObjectIdentity
pdnHdsl2ShdslLineCompliances = _PdnHdsl2ShdslLineCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 3, 1)
)
_PdnHdsl2ShdslLineGroups_ObjectIdentity = ObjectIdentity
pdnHdsl2ShdslLineGroups = _PdnHdsl2ShdslLineGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 3, 2)
)
_PdnHdsl2ShdslLineObjGroups_ObjectIdentity = ObjectIdentity
pdnHdsl2ShdslLineObjGroups = _PdnHdsl2ShdslLineObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 3, 2, 1)
)
_PdnHdsl2ShdslLineAfnGroups_ObjectIdentity = ObjectIdentity
pdnHdsl2ShdslLineAfnGroups = _PdnHdsl2ShdslLineAfnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 3, 2, 2)
)
_PdnHdsl2ShdslLineNtfyGroups_ObjectIdentity = ObjectIdentity
pdnHdsl2ShdslLineNtfyGroups = _PdnHdsl2ShdslLineNtfyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 3, 2, 3)
)

# Managed Objects groups

pdnHdsl2ShdslSpanShdslStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 3, 2, 1, 1)
)
pdnHdsl2ShdslSpanShdslStatusGroup.setObjects(
      *(("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslStatusMaxAttainableLineRate"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslStatusActualLineRate"))
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdslSpanShdslStatusGroup.setStatus("current")

pdnHdsl2ShdslEndpointConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 3, 2, 1, 2)
)
pdnHdsl2ShdslEndpointConfGroup.setObjects(
    ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointAlarmConfProfile")
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointConfGroup.setStatus("current")

pdnHdsl2ShdslEndpointCurrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 3, 2, 1, 3)
)
pdnHdsl2ShdslEndpointCurrGroup.setObjects(
      *(("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointCurrAtn"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointCurrSnrMgn"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointCurrStatus"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointES"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointSES"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointCRCanomalies"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointLOSWS"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointUAS"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointCurr15MinTimeElapsed"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointCurr15MinES"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointCurr15MinSES"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointCurr15MinCRCanomalies"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointCurr15MinLOSWS"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointCurr15MinUAS"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointCurr1DayTimeElapsed"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointCurr1DayES"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointCurr1DaySES"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointCurr1DayCRCanomalies"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointCurr1DayLOSWS"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointCurr1DayUAS"))
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdslEndpointCurrGroup.setStatus("current")

pdnHdsl2Shdsl15MinIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 3, 2, 1, 4)
)
pdnHdsl2Shdsl15MinIntervalGroup.setObjects(
      *(("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2Shdsl15MinIntervalES"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2Shdsl15MinIntervalSES"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2Shdsl15MinIntervalCRCanomalies"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2Shdsl15MinIntervalLOSWS"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2Shdsl15MinIntervalUAS"))
)
if mibBuilder.loadTexts:
    pdnHdsl2Shdsl15MinIntervalGroup.setStatus("current")

pdnHdsl2Shdsl1DayIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 3, 2, 1, 5)
)
pdnHdsl2Shdsl1DayIntervalGroup.setObjects(
      *(("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2Shdsl1DayIntervalMoniSecs"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2Shdsl1DayIntervalES"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2Shdsl1DayIntervalSES"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2Shdsl1DayIntervalCRCanomalies"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2Shdsl1DayIntervalLOSWS"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2Shdsl1DayIntervalUAS"))
)
if mibBuilder.loadTexts:
    pdnHdsl2Shdsl1DayIntervalGroup.setStatus("current")

pdnHdsl2ShdslSpanConfProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 3, 2, 1, 6)
)
pdnHdsl2ShdslSpanConfProfileGroup.setObjects(
      *(("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslSpanConfWireInterface"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslSpanConfMinLineRate"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslSpanConfMaxLineRate"))
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdslSpanConfProfileGroup.setStatus("current")

pdnHdsl2ShdslIfTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 3, 2, 1, 7)
)
pdnHdsl2ShdslIfTableGroup.setObjects(
    ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslIfTableEquipMode")
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdslIfTableGroup.setStatus("current")

pdnHdsl2ShdslExtendedRateModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 3, 2, 1, 8)
)
pdnHdsl2ShdslExtendedRateModeGroup.setObjects(
    ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslExtendedRateMode")
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdslExtendedRateModeGroup.setStatus("current")


# Notification objects

pdnHdsl2ShdslLoopAttenCrossing = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 0, 1)
)
pdnHdsl2ShdslLoopAttenCrossing.setObjects(
      *(("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointCurrAtn"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointThreshLoopAttenuation"))
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdslLoopAttenCrossing.setStatus(
        "current"
    )

pdnHdsl2ShdslSNRMarginCrossing = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 0, 2)
)
pdnHdsl2ShdslSNRMarginCrossing.setObjects(
      *(("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointCurrSnrMgn"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointThreshSNRMargin"))
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdslSNRMarginCrossing.setStatus(
        "current"
    )

pdnHdsl2ShdslPerfESThresh = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 0, 3)
)
pdnHdsl2ShdslPerfESThresh.setObjects(
      *(("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointCurr15MinES"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointThreshES"))
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdslPerfESThresh.setStatus(
        "current"
    )

pdnHdsl2ShdslPerfSESThresh = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 0, 4)
)
pdnHdsl2ShdslPerfSESThresh.setObjects(
      *(("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointCurr15MinSES"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointThreshSES"))
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdslPerfSESThresh.setStatus(
        "current"
    )

pdnHdsl2ShdslPerfCRCanomaliesThresh = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 0, 5)
)
pdnHdsl2ShdslPerfCRCanomaliesThresh.setObjects(
      *(("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointCurr15MinCRCanomalies"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointThreshCRCanomalies"))
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdslPerfCRCanomaliesThresh.setStatus(
        "current"
    )

pdnHdsl2ShdslPerfLOSWSThresh = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 0, 6)
)
pdnHdsl2ShdslPerfLOSWSThresh.setObjects(
      *(("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointCurr15MinLOSWS"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointThreshLOSWS"))
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdslPerfLOSWSThresh.setStatus(
        "current"
    )

pdnHdsl2ShdslPerfUASThresh = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 0, 7)
)
pdnHdsl2ShdslPerfUASThresh.setObjects(
      *(("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointCurr15MinUAS"),
        ("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslEndpointThreshUAS"))
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdslPerfUASThresh.setStatus(
        "current"
    )

pdnHdsl2ShdslpowerBackoff = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 0, 8)
)
pdnHdsl2ShdslpowerBackoff.setObjects(
    ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointCurrStatus")
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdslpowerBackoff.setStatus(
        "current"
    )

pdnHdsl2ShdsldeviceFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 0, 9)
)
pdnHdsl2ShdsldeviceFault.setObjects(
    ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointCurrStatus")
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdsldeviceFault.setStatus(
        "current"
    )

pdnHdsl2ShdsldcContinuityFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 0, 10)
)
pdnHdsl2ShdsldcContinuityFault.setObjects(
    ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointCurrStatus")
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdsldcContinuityFault.setStatus(
        "current"
    )

pdnHdsl2ShdslconfigInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 0, 11)
)
pdnHdsl2ShdslconfigInitFailure.setObjects(
    ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointCurrStatus")
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdslconfigInitFailure.setStatus(
        "current"
    )

pdnHdsl2ShdslprotocolInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 0, 12)
)
pdnHdsl2ShdslprotocolInitFailure.setObjects(
    ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointCurrStatus")
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdslprotocolInitFailure.setStatus(
        "current"
    )

pdnHdsl2ShdslnoNeighborPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 0, 13)
)
pdnHdsl2ShdslnoNeighborPresent.setObjects(
    ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslEndpointCurrStatus")
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdslnoNeighborPresent.setStatus(
        "current"
    )


# Notifications groups

pdnHdsl2ShdslNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 3, 2, 3, 1)
)
pdnHdsl2ShdslNotificationGroup.setObjects(
      *(("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslLoopAttenCrossing"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslSNRMarginCrossing"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslPerfESThresh"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslPerfSESThresh"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslPerfCRCanomaliesThresh"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslPerfLOSWSThresh"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslPerfUASThresh"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslpowerBackoff"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdsldeviceFault"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdsldcContinuityFault"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslconfigInitFailure"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslprotocolInitFailure"),
        ("PDN-HDSL2-SHDSL-LINE-MIB", "pdnHdsl2ShdslnoNeighborPresent"))
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdslNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

pdnHdsl2ShdslLineMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 23, 3, 1, 1)
)
if mibBuilder.loadTexts:
    pdnHdsl2ShdslLineMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-HDSL2-SHDSL-LINE-MIB",
    **{"PdnHdsl2ShdslWirePair": PdnHdsl2ShdslWirePair,
       "pdnHdsl2ShdslLineMIB": pdnHdsl2ShdslLineMIB,
       "pdnHdsl2ShdslLineNotifications": pdnHdsl2ShdslLineNotifications,
       "pdnHdsl2ShdslLoopAttenCrossing": pdnHdsl2ShdslLoopAttenCrossing,
       "pdnHdsl2ShdslSNRMarginCrossing": pdnHdsl2ShdslSNRMarginCrossing,
       "pdnHdsl2ShdslPerfESThresh": pdnHdsl2ShdslPerfESThresh,
       "pdnHdsl2ShdslPerfSESThresh": pdnHdsl2ShdslPerfSESThresh,
       "pdnHdsl2ShdslPerfCRCanomaliesThresh": pdnHdsl2ShdslPerfCRCanomaliesThresh,
       "pdnHdsl2ShdslPerfLOSWSThresh": pdnHdsl2ShdslPerfLOSWSThresh,
       "pdnHdsl2ShdslPerfUASThresh": pdnHdsl2ShdslPerfUASThresh,
       "pdnHdsl2ShdslpowerBackoff": pdnHdsl2ShdslpowerBackoff,
       "pdnHdsl2ShdsldeviceFault": pdnHdsl2ShdsldeviceFault,
       "pdnHdsl2ShdsldcContinuityFault": pdnHdsl2ShdsldcContinuityFault,
       "pdnHdsl2ShdslconfigInitFailure": pdnHdsl2ShdslconfigInitFailure,
       "pdnHdsl2ShdslprotocolInitFailure": pdnHdsl2ShdslprotocolInitFailure,
       "pdnHdsl2ShdslnoNeighborPresent": pdnHdsl2ShdslnoNeighborPresent,
       "pdnHdsl2ShdslLineObjects": pdnHdsl2ShdslLineObjects,
       "pdnHdsl2ShdslSpanStatusExtTable": pdnHdsl2ShdslSpanStatusExtTable,
       "pdnHdsl2ShdslSpanStatusExtEntry": pdnHdsl2ShdslSpanStatusExtEntry,
       "pdnHdsl2ShdslStatusMaxAttainableLineRate": pdnHdsl2ShdslStatusMaxAttainableLineRate,
       "pdnHdsl2ShdslStatusActualLineRate": pdnHdsl2ShdslStatusActualLineRate,
       "pdnHdsl2ShdslEndpointConfTable": pdnHdsl2ShdslEndpointConfTable,
       "pdnHdsl2ShdslEndpointConfEntry": pdnHdsl2ShdslEndpointConfEntry,
       "pdnHdsl2ShdslEndpointWirePair": pdnHdsl2ShdslEndpointWirePair,
       "pdnHdsl2ShdslEndpointAlarmConfProfile": pdnHdsl2ShdslEndpointAlarmConfProfile,
       "pdnHdsl2ShdslEndpointCurrTable": pdnHdsl2ShdslEndpointCurrTable,
       "pdnHdsl2ShdslEndpointCurrEntry": pdnHdsl2ShdslEndpointCurrEntry,
       "pdnHdsl2ShdslEndpointCurrAtn": pdnHdsl2ShdslEndpointCurrAtn,
       "pdnHdsl2ShdslEndpointCurrSnrMgn": pdnHdsl2ShdslEndpointCurrSnrMgn,
       "pdnHdsl2ShdslEndpointCurrStatus": pdnHdsl2ShdslEndpointCurrStatus,
       "pdnHdsl2ShdslEndpointES": pdnHdsl2ShdslEndpointES,
       "pdnHdsl2ShdslEndpointSES": pdnHdsl2ShdslEndpointSES,
       "pdnHdsl2ShdslEndpointCRCanomalies": pdnHdsl2ShdslEndpointCRCanomalies,
       "pdnHdsl2ShdslEndpointLOSWS": pdnHdsl2ShdslEndpointLOSWS,
       "pdnHdsl2ShdslEndpointUAS": pdnHdsl2ShdslEndpointUAS,
       "pdnHdsl2ShdslEndpointCurr15MinTimeElapsed": pdnHdsl2ShdslEndpointCurr15MinTimeElapsed,
       "pdnHdsl2ShdslEndpointCurr15MinES": pdnHdsl2ShdslEndpointCurr15MinES,
       "pdnHdsl2ShdslEndpointCurr15MinSES": pdnHdsl2ShdslEndpointCurr15MinSES,
       "pdnHdsl2ShdslEndpointCurr15MinCRCanomalies": pdnHdsl2ShdslEndpointCurr15MinCRCanomalies,
       "pdnHdsl2ShdslEndpointCurr15MinLOSWS": pdnHdsl2ShdslEndpointCurr15MinLOSWS,
       "pdnHdsl2ShdslEndpointCurr15MinUAS": pdnHdsl2ShdslEndpointCurr15MinUAS,
       "pdnHdsl2ShdslEndpointCurr1DayTimeElapsed": pdnHdsl2ShdslEndpointCurr1DayTimeElapsed,
       "pdnHdsl2ShdslEndpointCurr1DayES": pdnHdsl2ShdslEndpointCurr1DayES,
       "pdnHdsl2ShdslEndpointCurr1DaySES": pdnHdsl2ShdslEndpointCurr1DaySES,
       "pdnHdsl2ShdslEndpointCurr1DayCRCanomalies": pdnHdsl2ShdslEndpointCurr1DayCRCanomalies,
       "pdnHdsl2ShdslEndpointCurr1DayLOSWS": pdnHdsl2ShdslEndpointCurr1DayLOSWS,
       "pdnHdsl2ShdslEndpointCurr1DayUAS": pdnHdsl2ShdslEndpointCurr1DayUAS,
       "pdnHdsl2Shdsl15MinIntervalTable": pdnHdsl2Shdsl15MinIntervalTable,
       "pdnHdsl2Shdsl15MinIntervalEntry": pdnHdsl2Shdsl15MinIntervalEntry,
       "pdnHdsl2Shdsl15MinIntervalNumber": pdnHdsl2Shdsl15MinIntervalNumber,
       "pdnHdsl2Shdsl15MinIntervalES": pdnHdsl2Shdsl15MinIntervalES,
       "pdnHdsl2Shdsl15MinIntervalSES": pdnHdsl2Shdsl15MinIntervalSES,
       "pdnHdsl2Shdsl15MinIntervalCRCanomalies": pdnHdsl2Shdsl15MinIntervalCRCanomalies,
       "pdnHdsl2Shdsl15MinIntervalLOSWS": pdnHdsl2Shdsl15MinIntervalLOSWS,
       "pdnHdsl2Shdsl15MinIntervalUAS": pdnHdsl2Shdsl15MinIntervalUAS,
       "pdnHdsl2Shdsl1DayIntervalTable": pdnHdsl2Shdsl1DayIntervalTable,
       "pdnHdsl2Shdsl1DayIntervalEntry": pdnHdsl2Shdsl1DayIntervalEntry,
       "pdnHdsl2Shdsl1DayIntervalNumber": pdnHdsl2Shdsl1DayIntervalNumber,
       "pdnHdsl2Shdsl1DayIntervalMoniSecs": pdnHdsl2Shdsl1DayIntervalMoniSecs,
       "pdnHdsl2Shdsl1DayIntervalES": pdnHdsl2Shdsl1DayIntervalES,
       "pdnHdsl2Shdsl1DayIntervalSES": pdnHdsl2Shdsl1DayIntervalSES,
       "pdnHdsl2Shdsl1DayIntervalCRCanomalies": pdnHdsl2Shdsl1DayIntervalCRCanomalies,
       "pdnHdsl2Shdsl1DayIntervalLOSWS": pdnHdsl2Shdsl1DayIntervalLOSWS,
       "pdnHdsl2Shdsl1DayIntervalUAS": pdnHdsl2Shdsl1DayIntervalUAS,
       "pdnHdsl2ShdslSpanConfProfileExtTable": pdnHdsl2ShdslSpanConfProfileExtTable,
       "pdnHdsl2ShdslSpanConfProfileExtEntry": pdnHdsl2ShdslSpanConfProfileExtEntry,
       "pdnHdsl2ShdslSpanConfWireInterface": pdnHdsl2ShdslSpanConfWireInterface,
       "pdnHdsl2ShdslSpanConfMinLineRate": pdnHdsl2ShdslSpanConfMinLineRate,
       "pdnHdsl2ShdslSpanConfMaxLineRate": pdnHdsl2ShdslSpanConfMaxLineRate,
       "pdnHdsl2ShdslIfTable": pdnHdsl2ShdslIfTable,
       "pdnHdsl2ShdslIfEntry": pdnHdsl2ShdslIfEntry,
       "pdnHdsl2ShdslIfTableEquipMode": pdnHdsl2ShdslIfTableEquipMode,
       "pdnHdsl2ShdslExtendedRateMode": pdnHdsl2ShdslExtendedRateMode,
       "pdnHdsl2ShdslLineAFNs": pdnHdsl2ShdslLineAFNs,
       "pdnHdsl2ShdslLineConformance": pdnHdsl2ShdslLineConformance,
       "pdnHdsl2ShdslLineCompliances": pdnHdsl2ShdslLineCompliances,
       "pdnHdsl2ShdslLineMIBCompliance": pdnHdsl2ShdslLineMIBCompliance,
       "pdnHdsl2ShdslLineGroups": pdnHdsl2ShdslLineGroups,
       "pdnHdsl2ShdslLineObjGroups": pdnHdsl2ShdslLineObjGroups,
       "pdnHdsl2ShdslSpanShdslStatusGroup": pdnHdsl2ShdslSpanShdslStatusGroup,
       "pdnHdsl2ShdslEndpointConfGroup": pdnHdsl2ShdslEndpointConfGroup,
       "pdnHdsl2ShdslEndpointCurrGroup": pdnHdsl2ShdslEndpointCurrGroup,
       "pdnHdsl2Shdsl15MinIntervalGroup": pdnHdsl2Shdsl15MinIntervalGroup,
       "pdnHdsl2Shdsl1DayIntervalGroup": pdnHdsl2Shdsl1DayIntervalGroup,
       "pdnHdsl2ShdslSpanConfProfileGroup": pdnHdsl2ShdslSpanConfProfileGroup,
       "pdnHdsl2ShdslIfTableGroup": pdnHdsl2ShdslIfTableGroup,
       "pdnHdsl2ShdslExtendedRateModeGroup": pdnHdsl2ShdslExtendedRateModeGroup,
       "pdnHdsl2ShdslLineAfnGroups": pdnHdsl2ShdslLineAfnGroups,
       "pdnHdsl2ShdslLineNtfyGroups": pdnHdsl2ShdslLineNtfyGroups,
       "pdnHdsl2ShdslNotificationGroup": pdnHdsl2ShdslNotificationGroup}
)
