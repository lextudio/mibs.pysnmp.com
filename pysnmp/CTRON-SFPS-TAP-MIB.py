# SNMP MIB module (CTRON-SFPS-TAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SFPS-TAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:33 2024
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

(sfpsCallTap,
 sfpsTap,
 sfpsTapStats) = mibBuilder.importSymbols(
    "CTRON-SFPS-INCLUDE-MIB",
    "sfpsCallTap",
    "sfpsTap",
    "sfpsTapStats")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _SfpsCallTapVerb_Type(Integer32):
    """Custom type sfpsCallTapVerb based on Integer32"""
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
        *(("call-tap", 2),
          ("call-untap", 3),
          ("other", 1),
          ("vlan-tap", 4),
          ("vlan-untap", 5))
    )


_SfpsCallTapVerb_Type.__name__ = "Integer32"
_SfpsCallTapVerb_Object = MibScalar
sfpsCallTapVerb = _SfpsCallTapVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 11, 1),
    _SfpsCallTapVerb_Type()
)
sfpsCallTapVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsCallTapVerb.setStatus("mandatory")


class _SfpsCallTapHeaderType_Type(Integer32):
    """Custom type sfpsCallTapHeaderType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("atm-vpi-vci", 3),
          ("mac-da-sa", 2),
          ("other", 1))
    )


_SfpsCallTapHeaderType_Type.__name__ = "Integer32"
_SfpsCallTapHeaderType_Object = MibScalar
sfpsCallTapHeaderType = _SfpsCallTapHeaderType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 11, 2),
    _SfpsCallTapHeaderType_Type()
)
sfpsCallTapHeaderType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsCallTapHeaderType.setStatus("mandatory")
_SfpsCallTapHeaderLength_Type = Integer32
_SfpsCallTapHeaderLength_Object = MibScalar
sfpsCallTapHeaderLength = _SfpsCallTapHeaderLength_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 11, 3),
    _SfpsCallTapHeaderLength_Type()
)
sfpsCallTapHeaderLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsCallTapHeaderLength.setStatus("mandatory")
_SfpsCallTapHeaderValue_Type = DisplayString
_SfpsCallTapHeaderValue_Object = MibScalar
sfpsCallTapHeaderValue = _SfpsCallTapHeaderValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 11, 4),
    _SfpsCallTapHeaderValue_Type()
)
sfpsCallTapHeaderValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsCallTapHeaderValue.setStatus("mandatory")


class _SfpsCallTapArgDirection_Type(Integer32):
    """Custom type sfpsCallTapArgDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bi", 2),
          ("other", 1),
          ("uni", 3))
    )


_SfpsCallTapArgDirection_Type.__name__ = "Integer32"
_SfpsCallTapArgDirection_Object = MibScalar
sfpsCallTapArgDirection = _SfpsCallTapArgDirection_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 11, 5),
    _SfpsCallTapArgDirection_Type()
)
sfpsCallTapArgDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsCallTapArgDirection.setStatus("mandatory")
_SfpsCallTapProbeSwitch_Type = OctetString
_SfpsCallTapProbeSwitch_Object = MibScalar
sfpsCallTapProbeSwitch = _SfpsCallTapProbeSwitch_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 11, 6),
    _SfpsCallTapProbeSwitch_Type()
)
sfpsCallTapProbeSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsCallTapProbeSwitch.setStatus("mandatory")
_SfpsCallTapProbePort_Type = Integer32
_SfpsCallTapProbePort_Object = MibScalar
sfpsCallTapProbePort = _SfpsCallTapProbePort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 11, 7),
    _SfpsCallTapProbePort_Type()
)
sfpsCallTapProbePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsCallTapProbePort.setStatus("mandatory")
_SfpsTapTable_Object = MibTable
sfpsTapTable = _SfpsTapTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1)
)
if mibBuilder.loadTexts:
    sfpsTapTable.setStatus("mandatory")
_SfpsTapEntry_Object = MibTableRow
sfpsTapEntry = _SfpsTapEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1)
)
sfpsTapEntry.setIndexNames(
    (0, "CTRON-SFPS-TAP-MIB", "sfpsTapHeaderDASA"),
)
if mibBuilder.loadTexts:
    sfpsTapEntry.setStatus("mandatory")
_SfpsTapHeaderDASA_Type = DisplayString
_SfpsTapHeaderDASA_Object = MibTableColumn
sfpsTapHeaderDASA = _SfpsTapHeaderDASA_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 1),
    _SfpsTapHeaderDASA_Type()
)
sfpsTapHeaderDASA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTapHeaderDASA.setStatus("mandatory")
_SfpsTapRQPort_Type = Integer32
_SfpsTapRQPort_Object = MibTableColumn
sfpsTapRQPort = _SfpsTapRQPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 2),
    _SfpsTapRQPort_Type()
)
sfpsTapRQPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTapRQPort.setStatus("mandatory")
_SfpsTapRSPPort_Type = Integer32
_SfpsTapRSPPort_Object = MibTableColumn
sfpsTapRSPPort = _SfpsTapRSPPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 3),
    _SfpsTapRSPPort_Type()
)
sfpsTapRSPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTapRSPPort.setStatus("mandatory")
_SfpsTapRetries_Type = Integer32
_SfpsTapRetries_Object = MibTableColumn
sfpsTapRetries = _SfpsTapRetries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 4),
    _SfpsTapRetries_Type()
)
sfpsTapRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTapRetries.setStatus("mandatory")


class _SfpsTapSwitchState_Type(Integer32):
    """Custom type sfpsTapSwitchState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("awaitingTapRsps", 1),
          ("awaitingUnTapRsps", 5),
          ("receivingTapRsps", 2),
          ("receivingUnTapRsps", 6),
          ("retryingTapRequest", 3),
          ("retryingUnTapRequest", 7),
          ("tapActive", 4),
          ("unassigned", 8))
    )


_SfpsTapSwitchState_Type.__name__ = "Integer32"
_SfpsTapSwitchState_Object = MibTableColumn
sfpsTapSwitchState = _SfpsTapSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 5),
    _SfpsTapSwitchState_Type()
)
sfpsTapSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTapSwitchState.setStatus("mandatory")


class _SfpsTapSwitchType_Type(Integer32):
    """Custom type sfpsTapSwitchType based on Integer32"""
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
        *(("intermediate", 2),
          ("originatingTap", 1),
          ("originatingUntap", 4),
          ("terminal", 3))
    )


_SfpsTapSwitchType_Type.__name__ = "Integer32"
_SfpsTapSwitchType_Object = MibTableColumn
sfpsTapSwitchType = _SfpsTapSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 6),
    _SfpsTapSwitchType_Type()
)
sfpsTapSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTapSwitchType.setStatus("mandatory")


class _SfpsTapSwitchStatus_Type(Integer32):
    """Custom type sfpsTapSwitchStatus based on Integer32"""
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
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("alterCnx", 7),
          ("alterCnxDone", 8),
          ("decisionUnknown", 4),
          ("disableOutport", 1),
          ("halfCnx", 6),
          ("halfCnxDone", 9),
          ("keepOutport", 2),
          ("probeNotFound", 3),
          ("tapDeleteCnx", 11),
          ("tapFilterCnx", 13),
          ("tapIgnore", 10),
          ("tapMarkCnx", 12),
          ("tapSharedMedia", 14),
          ("unassigned", 5))
    )


_SfpsTapSwitchStatus_Type.__name__ = "Integer32"
_SfpsTapSwitchStatus_Object = MibTableColumn
sfpsTapSwitchStatus = _SfpsTapSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 7),
    _SfpsTapSwitchStatus_Type()
)
sfpsTapSwitchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTapSwitchStatus.setStatus("mandatory")


class _SfpsTapDirection_Type(Integer32):
    """Custom type sfpsTapDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bi-Directional", 2),
          ("other", 1),
          ("uni-Directional", 3))
    )


_SfpsTapDirection_Type.__name__ = "Integer32"
_SfpsTapDirection_Object = MibTableColumn
sfpsTapDirection = _SfpsTapDirection_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 8),
    _SfpsTapDirection_Type()
)
sfpsTapDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTapDirection.setStatus("mandatory")
_SfpsTapDirectRouteMAC_Type = DisplayString
_SfpsTapDirectRouteMAC_Object = MibTableColumn
sfpsTapDirectRouteMAC = _SfpsTapDirectRouteMAC_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 9),
    _SfpsTapDirectRouteMAC_Type()
)
sfpsTapDirectRouteMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTapDirectRouteMAC.setStatus("mandatory")


class _SfpsTapResponseStatus_Type(Integer32):
    """Custom type sfpsTapResponseStatus based on Integer32"""
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
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("alterCnx", 7),
          ("alterCnxDone", 8),
          ("decisionUnknown", 4),
          ("disableOutport", 1),
          ("halfCnx", 6),
          ("halfCnxDone", 9),
          ("keepOutport", 2),
          ("probeNotFound", 3),
          ("tapDeleteCnx", 11),
          ("tapFilterCnx", 13),
          ("tapIgnore", 10),
          ("tapMarkCnx", 12),
          ("tapSharedMedia", 14),
          ("unassigned", 5))
    )


_SfpsTapResponseStatus_Type.__name__ = "Integer32"
_SfpsTapResponseStatus_Object = MibTableColumn
sfpsTapResponseStatus = _SfpsTapResponseStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 10),
    _SfpsTapResponseStatus_Type()
)
sfpsTapResponseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTapResponseStatus.setStatus("mandatory")
_SfpsTapProbeSwitchMac_Type = DisplayString
_SfpsTapProbeSwitchMac_Object = MibTableColumn
sfpsTapProbeSwitchMac = _SfpsTapProbeSwitchMac_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 11),
    _SfpsTapProbeSwitchMac_Type()
)
sfpsTapProbeSwitchMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTapProbeSwitchMac.setStatus("mandatory")
_SfpsTapProbePort_Type = Integer32
_SfpsTapProbePort_Object = MibTableColumn
sfpsTapProbePort = _SfpsTapProbePort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 12),
    _SfpsTapProbePort_Type()
)
sfpsTapProbePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTapProbePort.setStatus("mandatory")
_SfpsTapStatsTapReqCnt_Type = Integer32
_SfpsTapStatsTapReqCnt_Object = MibScalar
sfpsTapStatsTapReqCnt = _SfpsTapStatsTapReqCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 13, 1),
    _SfpsTapStatsTapReqCnt_Type()
)
sfpsTapStatsTapReqCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTapStatsTapReqCnt.setStatus("mandatory")
_SfpsTapStatsTapRespCnt_Type = Integer32
_SfpsTapStatsTapRespCnt_Object = MibScalar
sfpsTapStatsTapRespCnt = _SfpsTapStatsTapRespCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 13, 2),
    _SfpsTapStatsTapRespCnt_Type()
)
sfpsTapStatsTapRespCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTapStatsTapRespCnt.setStatus("mandatory")
_SfpsTapStatsUntapReqCnt_Type = Integer32
_SfpsTapStatsUntapReqCnt_Object = MibScalar
sfpsTapStatsUntapReqCnt = _SfpsTapStatsUntapReqCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 13, 3),
    _SfpsTapStatsUntapReqCnt_Type()
)
sfpsTapStatsUntapReqCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTapStatsUntapReqCnt.setStatus("mandatory")
_SfpsTapStatsUntapRespCnt_Type = Integer32
_SfpsTapStatsUntapRespCnt_Object = MibScalar
sfpsTapStatsUntapRespCnt = _SfpsTapStatsUntapRespCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 13, 4),
    _SfpsTapStatsUntapRespCnt_Type()
)
sfpsTapStatsUntapRespCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTapStatsUntapRespCnt.setStatus("mandatory")
_SfpsTapStatsErrorCnt_Type = Integer32
_SfpsTapStatsErrorCnt_Object = MibScalar
sfpsTapStatsErrorCnt = _SfpsTapStatsErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 13, 5),
    _SfpsTapStatsErrorCnt_Type()
)
sfpsTapStatsErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTapStatsErrorCnt.setStatus("mandatory")
_SfpsTapStatsStaleEntCnt_Type = Integer32
_SfpsTapStatsStaleEntCnt_Object = MibScalar
sfpsTapStatsStaleEntCnt = _SfpsTapStatsStaleEntCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 13, 6),
    _SfpsTapStatsStaleEntCnt_Type()
)
sfpsTapStatsStaleEntCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTapStatsStaleEntCnt.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SFPS-TAP-MIB",
    **{"sfpsCallTapVerb": sfpsCallTapVerb,
       "sfpsCallTapHeaderType": sfpsCallTapHeaderType,
       "sfpsCallTapHeaderLength": sfpsCallTapHeaderLength,
       "sfpsCallTapHeaderValue": sfpsCallTapHeaderValue,
       "sfpsCallTapArgDirection": sfpsCallTapArgDirection,
       "sfpsCallTapProbeSwitch": sfpsCallTapProbeSwitch,
       "sfpsCallTapProbePort": sfpsCallTapProbePort,
       "sfpsTapTable": sfpsTapTable,
       "sfpsTapEntry": sfpsTapEntry,
       "sfpsTapHeaderDASA": sfpsTapHeaderDASA,
       "sfpsTapRQPort": sfpsTapRQPort,
       "sfpsTapRSPPort": sfpsTapRSPPort,
       "sfpsTapRetries": sfpsTapRetries,
       "sfpsTapSwitchState": sfpsTapSwitchState,
       "sfpsTapSwitchType": sfpsTapSwitchType,
       "sfpsTapSwitchStatus": sfpsTapSwitchStatus,
       "sfpsTapDirection": sfpsTapDirection,
       "sfpsTapDirectRouteMAC": sfpsTapDirectRouteMAC,
       "sfpsTapResponseStatus": sfpsTapResponseStatus,
       "sfpsTapProbeSwitchMac": sfpsTapProbeSwitchMac,
       "sfpsTapProbePort": sfpsTapProbePort,
       "sfpsTapStatsTapReqCnt": sfpsTapStatsTapReqCnt,
       "sfpsTapStatsTapRespCnt": sfpsTapStatsTapRespCnt,
       "sfpsTapStatsUntapReqCnt": sfpsTapStatsUntapReqCnt,
       "sfpsTapStatsUntapRespCnt": sfpsTapStatsUntapRespCnt,
       "sfpsTapStatsErrorCnt": sfpsTapStatsErrorCnt,
       "sfpsTapStatsStaleEntCnt": sfpsTapStatsStaleEntCnt}
)
