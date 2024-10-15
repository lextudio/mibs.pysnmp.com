# SNMP MIB module (REPEATER-REV4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REPEATER-REV4-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:54 2024
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

(repeaterRev4,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "repeaterRev4")

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

_Repeaterrev4_ObjectIdentity = ObjectIdentity
repeaterrev4 = _Repeaterrev4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4)
)
_Rptr_ObjectIdentity = ObjectIdentity
rptr = _Rptr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1)
)
_RptrMgmt_ObjectIdentity = ObjectIdentity
rptrMgmt = _RptrMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 1)
)


class _RptrMgmtName_Type(DisplayString):
    """Custom type rptrMgmtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_RptrMgmtName_Type.__name__ = "DisplayString"
_RptrMgmtName_Object = MibScalar
rptrMgmtName = _RptrMgmtName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 1, 1),
    _RptrMgmtName_Type()
)
rptrMgmtName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrMgmtName.setStatus("mandatory")
_RptrMgmtPortCount_Type = Integer32
_RptrMgmtPortCount_Object = MibScalar
rptrMgmtPortCount = _RptrMgmtPortCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 1, 2),
    _RptrMgmtPortCount_Type()
)
rptrMgmtPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMgmtPortCount.setStatus("mandatory")


class _RptrMgmtPortsEnable_Type(Integer32):
    """Custom type rptrMgmtPortsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("noEnable", 1))
    )


_RptrMgmtPortsEnable_Type.__name__ = "Integer32"
_RptrMgmtPortsEnable_Object = MibScalar
rptrMgmtPortsEnable = _RptrMgmtPortsEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 1, 3),
    _RptrMgmtPortsEnable_Type()
)
rptrMgmtPortsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrMgmtPortsEnable.setStatus("mandatory")
_RptrMgmtPortsOn_Type = Integer32
_RptrMgmtPortsOn_Object = MibScalar
rptrMgmtPortsOn = _RptrMgmtPortsOn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 1, 4),
    _RptrMgmtPortsOn_Type()
)
rptrMgmtPortsOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMgmtPortsOn.setStatus("mandatory")
_RptrMgmtPortsOper_Type = Integer32
_RptrMgmtPortsOper_Object = MibScalar
rptrMgmtPortsOper = _RptrMgmtPortsOper_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 1, 5),
    _RptrMgmtPortsOper_Type()
)
rptrMgmtPortsOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMgmtPortsOper.setStatus("mandatory")
_RptrMgmtBoardMap_Type = Integer32
_RptrMgmtBoardMap_Object = MibScalar
rptrMgmtBoardMap = _RptrMgmtBoardMap_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 1, 6),
    _RptrMgmtBoardMap_Type()
)
rptrMgmtBoardMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMgmtBoardMap.setStatus("mandatory")
_RptrMgmtInterfaceNum_Type = Integer32
_RptrMgmtInterfaceNum_Object = MibScalar
rptrMgmtInterfaceNum = _RptrMgmtInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 1, 7),
    _RptrMgmtInterfaceNum_Type()
)
rptrMgmtInterfaceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMgmtInterfaceNum.setStatus("mandatory")


class _RptrMgmtResetCounters_Type(Integer32):
    """Custom type rptrMgmtResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reseStaticCounters", 2))
    )


_RptrMgmtResetCounters_Type.__name__ = "Integer32"
_RptrMgmtResetCounters_Object = MibScalar
rptrMgmtResetCounters = _RptrMgmtResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 1, 8),
    _RptrMgmtResetCounters_Type()
)
rptrMgmtResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrMgmtResetCounters.setStatus("mandatory")
_RptrStats_ObjectIdentity = ObjectIdentity
rptrStats = _RptrStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 2)
)
_RptrPktStats_ObjectIdentity = ObjectIdentity
rptrPktStats = _RptrPktStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 2, 1)
)
_RptrPktStatsPackets_Type = Counter32
_RptrPktStatsPackets_Object = MibScalar
rptrPktStatsPackets = _RptrPktStatsPackets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 2, 1, 1),
    _RptrPktStatsPackets_Type()
)
rptrPktStatsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPktStatsPackets.setStatus("mandatory")
_RptrPktStatsBytes_Type = Counter32
_RptrPktStatsBytes_Object = MibScalar
rptrPktStatsBytes = _RptrPktStatsBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 2, 1, 2),
    _RptrPktStatsBytes_Type()
)
rptrPktStatsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPktStatsBytes.setStatus("mandatory")
_RptrPktStatsColls_Type = Counter32
_RptrPktStatsColls_Object = MibScalar
rptrPktStatsColls = _RptrPktStatsColls_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 2, 1, 3),
    _RptrPktStatsColls_Type()
)
rptrPktStatsColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPktStatsColls.setStatus("mandatory")
_RptrPktStatsErrors_Type = Counter32
_RptrPktStatsErrors_Object = MibScalar
rptrPktStatsErrors = _RptrPktStatsErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 2, 1, 4),
    _RptrPktStatsErrors_Type()
)
rptrPktStatsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPktStatsErrors.setStatus("mandatory")
_RptrPktStatsAlign_Type = Counter32
_RptrPktStatsAlign_Object = MibScalar
rptrPktStatsAlign = _RptrPktStatsAlign_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 2, 1, 5),
    _RptrPktStatsAlign_Type()
)
rptrPktStatsAlign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPktStatsAlign.setStatus("mandatory")
_RptrPktStatsCRC_Type = Counter32
_RptrPktStatsCRC_Object = MibScalar
rptrPktStatsCRC = _RptrPktStatsCRC_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 2, 1, 6),
    _RptrPktStatsCRC_Type()
)
rptrPktStatsCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPktStatsCRC.setStatus("mandatory")
_RptrPktStatsOOW_Type = Counter32
_RptrPktStatsOOW_Object = MibScalar
rptrPktStatsOOW = _RptrPktStatsOOW_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 2, 1, 7),
    _RptrPktStatsOOW_Type()
)
rptrPktStatsOOW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPktStatsOOW.setStatus("mandatory")
_RptrPktStatsNoRsc_Type = Counter32
_RptrPktStatsNoRsc_Object = MibScalar
rptrPktStatsNoRsc = _RptrPktStatsNoRsc_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 2, 1, 8),
    _RptrPktStatsNoRsc_Type()
)
rptrPktStatsNoRsc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPktStatsNoRsc.setStatus("mandatory")
_RptrPktStatsBroadcasts_Type = Counter32
_RptrPktStatsBroadcasts_Object = MibScalar
rptrPktStatsBroadcasts = _RptrPktStatsBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 2, 1, 9),
    _RptrPktStatsBroadcasts_Type()
)
rptrPktStatsBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPktStatsBroadcasts.setStatus("mandatory")
_RptrPktStatsMulticasts_Type = Counter32
_RptrPktStatsMulticasts_Object = MibScalar
rptrPktStatsMulticasts = _RptrPktStatsMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 2, 1, 10),
    _RptrPktStatsMulticasts_Type()
)
rptrPktStatsMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPktStatsMulticasts.setStatus("mandatory")
_RptrProtocols_ObjectIdentity = ObjectIdentity
rptrProtocols = _RptrProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 2, 2)
)
_RptrProtocolsOSI_Type = Counter32
_RptrProtocolsOSI_Object = MibScalar
rptrProtocolsOSI = _RptrProtocolsOSI_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 2, 2, 1),
    _RptrProtocolsOSI_Type()
)
rptrProtocolsOSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrProtocolsOSI.setStatus("mandatory")
_RptrProtocolsNovell_Type = Counter32
_RptrProtocolsNovell_Object = MibScalar
rptrProtocolsNovell = _RptrProtocolsNovell_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 2, 2, 2),
    _RptrProtocolsNovell_Type()
)
rptrProtocolsNovell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrProtocolsNovell.setStatus("mandatory")
_RptrProtocolsBanyan_Type = Counter32
_RptrProtocolsBanyan_Object = MibScalar
rptrProtocolsBanyan = _RptrProtocolsBanyan_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 2, 2, 3),
    _RptrProtocolsBanyan_Type()
)
rptrProtocolsBanyan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrProtocolsBanyan.setStatus("mandatory")
_RptrProtocolsDECNet_Type = Counter32
_RptrProtocolsDECNet_Object = MibScalar
rptrProtocolsDECNet = _RptrProtocolsDECNet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 2, 2, 4),
    _RptrProtocolsDECNet_Type()
)
rptrProtocolsDECNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrProtocolsDECNet.setStatus("mandatory")
_RptrProtocolsXNS_Type = Counter32
_RptrProtocolsXNS_Object = MibScalar
rptrProtocolsXNS = _RptrProtocolsXNS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 2, 2, 5),
    _RptrProtocolsXNS_Type()
)
rptrProtocolsXNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrProtocolsXNS.setStatus("mandatory")
_RptrProtocolsIP_Type = Counter32
_RptrProtocolsIP_Object = MibScalar
rptrProtocolsIP = _RptrProtocolsIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 2, 2, 6),
    _RptrProtocolsIP_Type()
)
rptrProtocolsIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrProtocolsIP.setStatus("mandatory")
_RptrProtocolsCtron_Type = Counter32
_RptrProtocolsCtron_Object = MibScalar
rptrProtocolsCtron = _RptrProtocolsCtron_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 2, 2, 7),
    _RptrProtocolsCtron_Type()
)
rptrProtocolsCtron.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrProtocolsCtron.setStatus("mandatory")
_RptrProtocolsAppletalk_Type = Counter32
_RptrProtocolsAppletalk_Object = MibScalar
rptrProtocolsAppletalk = _RptrProtocolsAppletalk_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 2, 2, 8),
    _RptrProtocolsAppletalk_Type()
)
rptrProtocolsAppletalk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrProtocolsAppletalk.setStatus("mandatory")
_RptrProtocolsOther_Type = Counter32
_RptrProtocolsOther_Object = MibScalar
rptrProtocolsOther = _RptrProtocolsOther_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 2, 2, 9),
    _RptrProtocolsOther_Type()
)
rptrProtocolsOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrProtocolsOther.setStatus("mandatory")
_RptrFrameSizes_ObjectIdentity = ObjectIdentity
rptrFrameSizes = _RptrFrameSizes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 2, 3)
)
_RptrFrameSzRunt_Type = Counter32
_RptrFrameSzRunt_Object = MibScalar
rptrFrameSzRunt = _RptrFrameSzRunt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 2, 3, 1),
    _RptrFrameSzRunt_Type()
)
rptrFrameSzRunt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrFrameSzRunt.setStatus("mandatory")
_RptrFrameSz64To127_Type = Counter32
_RptrFrameSz64To127_Object = MibScalar
rptrFrameSz64To127 = _RptrFrameSz64To127_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 2, 3, 2),
    _RptrFrameSz64To127_Type()
)
rptrFrameSz64To127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrFrameSz64To127.setStatus("mandatory")
_RptrFrameSz128To255_Type = Counter32
_RptrFrameSz128To255_Object = MibScalar
rptrFrameSz128To255 = _RptrFrameSz128To255_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 2, 3, 3),
    _RptrFrameSz128To255_Type()
)
rptrFrameSz128To255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrFrameSz128To255.setStatus("mandatory")
_RptrFrameSz256To511_Type = Counter32
_RptrFrameSz256To511_Object = MibScalar
rptrFrameSz256To511 = _RptrFrameSz256To511_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 2, 3, 4),
    _RptrFrameSz256To511_Type()
)
rptrFrameSz256To511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrFrameSz256To511.setStatus("mandatory")
_RptrFrameSz512To1023_Type = Counter32
_RptrFrameSz512To1023_Object = MibScalar
rptrFrameSz512To1023 = _RptrFrameSz512To1023_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 2, 3, 5),
    _RptrFrameSz512To1023_Type()
)
rptrFrameSz512To1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrFrameSz512To1023.setStatus("mandatory")
_RptrFrameSz1024To1518_Type = Counter32
_RptrFrameSz1024To1518_Object = MibScalar
rptrFrameSz1024To1518 = _RptrFrameSz1024To1518_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 2, 3, 6),
    _RptrFrameSz1024To1518_Type()
)
rptrFrameSz1024To1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrFrameSz1024To1518.setStatus("mandatory")
_RptrFrameSzGiant_Type = Counter32
_RptrFrameSzGiant_Object = MibScalar
rptrFrameSzGiant = _RptrFrameSzGiant_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 2, 3, 7),
    _RptrFrameSzGiant_Type()
)
rptrFrameSzGiant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrFrameSzGiant.setStatus("mandatory")
_RptrAlarms_ObjectIdentity = ObjectIdentity
rptrAlarms = _RptrAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 3)
)


class _RptrAlarmsTrafEnable_Type(Integer32):
    """Custom type rptrAlarmsTrafEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RptrAlarmsTrafEnable_Type.__name__ = "Integer32"
_RptrAlarmsTrafEnable_Object = MibScalar
rptrAlarmsTrafEnable = _RptrAlarmsTrafEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 3, 1),
    _RptrAlarmsTrafEnable_Type()
)
rptrAlarmsTrafEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrAlarmsTrafEnable.setStatus("mandatory")
_RptrAlarmsTrafThreshold_Type = Integer32
_RptrAlarmsTrafThreshold_Object = MibScalar
rptrAlarmsTrafThreshold = _RptrAlarmsTrafThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 3, 2),
    _RptrAlarmsTrafThreshold_Type()
)
rptrAlarmsTrafThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrAlarmsTrafThreshold.setStatus("mandatory")


class _RptrAlarmsCollEnable_Type(Integer32):
    """Custom type rptrAlarmsCollEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RptrAlarmsCollEnable_Type.__name__ = "Integer32"
_RptrAlarmsCollEnable_Object = MibScalar
rptrAlarmsCollEnable = _RptrAlarmsCollEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 3, 3),
    _RptrAlarmsCollEnable_Type()
)
rptrAlarmsCollEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrAlarmsCollEnable.setStatus("mandatory")


class _RptrAlarmsCollThreshold_Type(Integer32):
    """Custom type rptrAlarmsCollThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RptrAlarmsCollThreshold_Type.__name__ = "Integer32"
_RptrAlarmsCollThreshold_Object = MibScalar
rptrAlarmsCollThreshold = _RptrAlarmsCollThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 3, 4),
    _RptrAlarmsCollThreshold_Type()
)
rptrAlarmsCollThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrAlarmsCollThreshold.setStatus("mandatory")


class _RptrAlarmsErrEnable_Type(Integer32):
    """Custom type rptrAlarmsErrEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RptrAlarmsErrEnable_Type.__name__ = "Integer32"
_RptrAlarmsErrEnable_Object = MibScalar
rptrAlarmsErrEnable = _RptrAlarmsErrEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 3, 5),
    _RptrAlarmsErrEnable_Type()
)
rptrAlarmsErrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrAlarmsErrEnable.setStatus("mandatory")


class _RptrAlarmsErrThreshold_Type(Integer32):
    """Custom type rptrAlarmsErrThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RptrAlarmsErrThreshold_Type.__name__ = "Integer32"
_RptrAlarmsErrThreshold_Object = MibScalar
rptrAlarmsErrThreshold = _RptrAlarmsErrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 3, 6),
    _RptrAlarmsErrThreshold_Type()
)
rptrAlarmsErrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrAlarmsErrThreshold.setStatus("mandatory")
_RptrAlarmsErrSource_Type = Integer32
_RptrAlarmsErrSource_Object = MibScalar
rptrAlarmsErrSource = _RptrAlarmsErrSource_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 3, 7),
    _RptrAlarmsErrSource_Type()
)
rptrAlarmsErrSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrAlarmsErrSource.setStatus("mandatory")


class _RptrAlarmsAlarmTimebase_Type(Integer32):
    """Custom type rptrAlarmsAlarmTimebase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 999999),
    )


_RptrAlarmsAlarmTimebase_Type.__name__ = "Integer32"
_RptrAlarmsAlarmTimebase_Object = MibScalar
rptrAlarmsAlarmTimebase = _RptrAlarmsAlarmTimebase_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 3, 8),
    _RptrAlarmsAlarmTimebase_Type()
)
rptrAlarmsAlarmTimebase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrAlarmsAlarmTimebase.setStatus("mandatory")


class _RptrAlarmsBroadEnable_Type(Integer32):
    """Custom type rptrAlarmsBroadEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RptrAlarmsBroadEnable_Type.__name__ = "Integer32"
_RptrAlarmsBroadEnable_Object = MibScalar
rptrAlarmsBroadEnable = _RptrAlarmsBroadEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 3, 9),
    _RptrAlarmsBroadEnable_Type()
)
rptrAlarmsBroadEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrAlarmsBroadEnable.setStatus("mandatory")
_RptrAlarmsBroadThreshold_Type = Integer32
_RptrAlarmsBroadThreshold_Object = MibScalar
rptrAlarmsBroadThreshold = _RptrAlarmsBroadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 3, 10),
    _RptrAlarmsBroadThreshold_Type()
)
rptrAlarmsBroadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrAlarmsBroadThreshold.setStatus("mandatory")
_RptrRedundancy_ObjectIdentity = ObjectIdentity
rptrRedundancy = _RptrRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 4)
)
_RptrRedund_ObjectIdentity = ObjectIdentity
rptrRedund = _RptrRedund_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 4, 1)
)


class _RptrRedundReset_Type(Integer32):
    """Custom type rptrRedundReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_RptrRedundReset_Type.__name__ = "Integer32"
_RptrRedundReset_Object = MibScalar
rptrRedundReset = _RptrRedundReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 4, 1, 1),
    _RptrRedundReset_Type()
)
rptrRedundReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrRedundReset.setStatus("mandatory")
_RptrRedundPollInterval_Type = Integer32
_RptrRedundPollInterval_Object = MibScalar
rptrRedundPollInterval = _RptrRedundPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 4, 1, 2),
    _RptrRedundPollInterval_Type()
)
rptrRedundPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrRedundPollInterval.setStatus("mandatory")


class _RptrRedundTestTOD_Type(DisplayString):
    """Custom type rptrRedundTestTOD based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_RptrRedundTestTOD_Type.__name__ = "DisplayString"
_RptrRedundTestTOD_Object = MibScalar
rptrRedundTestTOD = _RptrRedundTestTOD_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 4, 1, 3),
    _RptrRedundTestTOD_Type()
)
rptrRedundTestTOD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrRedundTestTOD.setStatus("mandatory")


class _RptrRedundPerformTest_Type(Integer32):
    """Custom type rptrRedundPerformTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noTest", 1),
          ("test", 2))
    )


_RptrRedundPerformTest_Type.__name__ = "Integer32"
_RptrRedundPerformTest_Object = MibScalar
rptrRedundPerformTest = _RptrRedundPerformTest_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 4, 1, 4),
    _RptrRedundPerformTest_Type()
)
rptrRedundPerformTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrRedundPerformTest.setStatus("mandatory")
_RptrRedundMaxCrcts_Type = Integer32
_RptrRedundMaxCrcts_Object = MibScalar
rptrRedundMaxCrcts = _RptrRedundMaxCrcts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 4, 1, 5),
    _RptrRedundMaxCrcts_Type()
)
rptrRedundMaxCrcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrRedundMaxCrcts.setStatus("mandatory")
_RptrRedundCrctTable_Object = MibTable
rptrRedundCrctTable = _RptrRedundCrctTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 4, 2)
)
if mibBuilder.loadTexts:
    rptrRedundCrctTable.setStatus("mandatory")
_RptrRedundCrctEntry_Object = MibTableRow
rptrRedundCrctEntry = _RptrRedundCrctEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 4, 2, 1)
)
rptrRedundCrctEntry.setIndexNames(
    (0, "REPEATER-REV4-MIB", "rptrRedundCrctId"),
)
if mibBuilder.loadTexts:
    rptrRedundCrctEntry.setStatus("mandatory")
_RptrRedundCrctId_Type = Integer32
_RptrRedundCrctId_Object = MibTableColumn
rptrRedundCrctId = _RptrRedundCrctId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 4, 2, 1, 1),
    _RptrRedundCrctId_Type()
)
rptrRedundCrctId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrRedundCrctId.setStatus("mandatory")
_RptrRedundCrctName_Type = OctetString
_RptrRedundCrctName_Object = MibTableColumn
rptrRedundCrctName = _RptrRedundCrctName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 4, 2, 1, 2),
    _RptrRedundCrctName_Type()
)
rptrRedundCrctName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrRedundCrctName.setStatus("mandatory")
_RptrRedundCrctRetrys_Type = Integer32
_RptrRedundCrctRetrys_Object = MibTableColumn
rptrRedundCrctRetrys = _RptrRedundCrctRetrys_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 4, 2, 1, 3),
    _RptrRedundCrctRetrys_Type()
)
rptrRedundCrctRetrys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrRedundCrctRetrys.setStatus("mandatory")
_RptrRedundCrctNumBPs_Type = Integer32
_RptrRedundCrctNumBPs_Object = MibTableColumn
rptrRedundCrctNumBPs = _RptrRedundCrctNumBPs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 4, 2, 1, 4),
    _RptrRedundCrctNumBPs_Type()
)
rptrRedundCrctNumBPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrRedundCrctNumBPs.setStatus("mandatory")
_RptrRedundCrctNumAddr_Type = Integer32
_RptrRedundCrctNumAddr_Object = MibTableColumn
rptrRedundCrctNumAddr = _RptrRedundCrctNumAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 4, 2, 1, 5),
    _RptrRedundCrctNumAddr_Type()
)
rptrRedundCrctNumAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrRedundCrctNumAddr.setStatus("mandatory")
_RptrRedundCrctAddAddr_Type = IpAddress
_RptrRedundCrctAddAddr_Object = MibTableColumn
rptrRedundCrctAddAddr = _RptrRedundCrctAddAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 4, 2, 1, 6),
    _RptrRedundCrctAddAddr_Type()
)
rptrRedundCrctAddAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrRedundCrctAddAddr.setStatus("mandatory")
_RptrRedundCrctDelAddr_Type = IpAddress
_RptrRedundCrctDelAddr_Object = MibTableColumn
rptrRedundCrctDelAddr = _RptrRedundCrctDelAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 4, 2, 1, 7),
    _RptrRedundCrctDelAddr_Type()
)
rptrRedundCrctDelAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrRedundCrctDelAddr.setStatus("mandatory")


class _RptrRedundCrctEnable_Type(Integer32):
    """Custom type rptrRedundCrctEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RptrRedundCrctEnable_Type.__name__ = "Integer32"
_RptrRedundCrctEnable_Object = MibTableColumn
rptrRedundCrctEnable = _RptrRedundCrctEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 4, 2, 1, 8),
    _RptrRedundCrctEnable_Type()
)
rptrRedundCrctEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrRedundCrctEnable.setStatus("mandatory")


class _RptrRedundCrctReset_Type(Integer32):
    """Custom type rptrRedundCrctReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_RptrRedundCrctReset_Type.__name__ = "Integer32"
_RptrRedundCrctReset_Object = MibTableColumn
rptrRedundCrctReset = _RptrRedundCrctReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 4, 2, 1, 9),
    _RptrRedundCrctReset_Type()
)
rptrRedundCrctReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrRedundCrctReset.setStatus("mandatory")
_RptrRedundPortTable_Object = MibTable
rptrRedundPortTable = _RptrRedundPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 4, 3)
)
if mibBuilder.loadTexts:
    rptrRedundPortTable.setStatus("mandatory")
_RptrRedundPortEntry_Object = MibTableRow
rptrRedundPortEntry = _RptrRedundPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 4, 3, 1)
)
rptrRedundPortEntry.setIndexNames(
    (0, "REPEATER-REV4-MIB", "rptrRedundPortCrctId"),
    (0, "REPEATER-REV4-MIB", "rptrRedundPortId"),
)
if mibBuilder.loadTexts:
    rptrRedundPortEntry.setStatus("mandatory")
_RptrRedundPortId_Type = Integer32
_RptrRedundPortId_Object = MibTableColumn
rptrRedundPortId = _RptrRedundPortId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 4, 3, 1, 1),
    _RptrRedundPortId_Type()
)
rptrRedundPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrRedundPortId.setStatus("mandatory")
_RptrRedundPortCrctId_Type = Integer32
_RptrRedundPortCrctId_Object = MibTableColumn
rptrRedundPortCrctId = _RptrRedundPortCrctId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 4, 3, 1, 2),
    _RptrRedundPortCrctId_Type()
)
rptrRedundPortCrctId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrRedundPortCrctId.setStatus("mandatory")
_RptrRedundPortNum_Type = Integer32
_RptrRedundPortNum_Object = MibTableColumn
rptrRedundPortNum = _RptrRedundPortNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 4, 3, 1, 3),
    _RptrRedundPortNum_Type()
)
rptrRedundPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrRedundPortNum.setStatus("mandatory")
_RptrRedundPortBoardNum_Type = Integer32
_RptrRedundPortBoardNum_Object = MibTableColumn
rptrRedundPortBoardNum = _RptrRedundPortBoardNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 4, 3, 1, 4),
    _RptrRedundPortBoardNum_Type()
)
rptrRedundPortBoardNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrRedundPortBoardNum.setStatus("mandatory")


class _RptrRedundPortType_Type(Integer32):
    """Custom type rptrRedundPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 3),
          ("notUsed", 1),
          ("primary", 2))
    )


_RptrRedundPortType_Type.__name__ = "Integer32"
_RptrRedundPortType_Object = MibTableColumn
rptrRedundPortType = _RptrRedundPortType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 4, 3, 1, 5),
    _RptrRedundPortType_Type()
)
rptrRedundPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrRedundPortType.setStatus("mandatory")
_RptrRedundAddrTable_Object = MibTable
rptrRedundAddrTable = _RptrRedundAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 4, 4)
)
if mibBuilder.loadTexts:
    rptrRedundAddrTable.setStatus("mandatory")
_RptrRedundAddrEntry_Object = MibTableRow
rptrRedundAddrEntry = _RptrRedundAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 4, 4, 1)
)
rptrRedundAddrEntry.setIndexNames(
    (0, "REPEATER-REV4-MIB", "rptrRedundAddrCrctId"),
    (0, "REPEATER-REV4-MIB", "rptrRedundAddrId"),
)
if mibBuilder.loadTexts:
    rptrRedundAddrEntry.setStatus("mandatory")
_RptrRedundAddrId_Type = Integer32
_RptrRedundAddrId_Object = MibTableColumn
rptrRedundAddrId = _RptrRedundAddrId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 4, 4, 1, 1),
    _RptrRedundAddrId_Type()
)
rptrRedundAddrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrRedundAddrId.setStatus("mandatory")
_RptrRedundAddrCrctId_Type = Integer32
_RptrRedundAddrCrctId_Object = MibTableColumn
rptrRedundAddrCrctId = _RptrRedundAddrCrctId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 4, 4, 1, 2),
    _RptrRedundAddrCrctId_Type()
)
rptrRedundAddrCrctId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrRedundAddrCrctId.setStatus("mandatory")
_RptrRedundAddrIPAddr_Type = IpAddress
_RptrRedundAddrIPAddr_Object = MibTableColumn
rptrRedundAddrIPAddr = _RptrRedundAddrIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 4, 4, 1, 3),
    _RptrRedundAddrIPAddr_Type()
)
rptrRedundAddrIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrRedundAddrIPAddr.setStatus("mandatory")
_RptrSourceAddress_ObjectIdentity = ObjectIdentity
rptrSourceAddress = _RptrSourceAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 5)
)
_RptrSrcAddrListTable_Object = MibTable
rptrSrcAddrListTable = _RptrSrcAddrListTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 5, 1)
)
if mibBuilder.loadTexts:
    rptrSrcAddrListTable.setStatus("mandatory")
_RptrSrcAddrListEntry_Object = MibTableRow
rptrSrcAddrListEntry = _RptrSrcAddrListEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 5, 1, 1)
)
rptrSrcAddrListEntry.setIndexNames(
    (0, "REPEATER-REV4-MIB", "rptrSrcAddrListId"),
)
if mibBuilder.loadTexts:
    rptrSrcAddrListEntry.setStatus("mandatory")
_RptrSrcAddrListId_Type = Integer32
_RptrSrcAddrListId_Object = MibTableColumn
rptrSrcAddrListId = _RptrSrcAddrListId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 5, 1, 1, 1),
    _RptrSrcAddrListId_Type()
)
rptrSrcAddrListId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSrcAddrListId.setStatus("mandatory")


class _RptrSrcAddrAddressList_Type(OctetString):
    """Custom type rptrSrcAddrAddressList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_RptrSrcAddrAddressList_Type.__name__ = "OctetString"
_RptrSrcAddrAddressList_Object = MibTableColumn
rptrSrcAddrAddressList = _RptrSrcAddrAddressList_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 5, 1, 1, 2),
    _RptrSrcAddrAddressList_Type()
)
rptrSrcAddrAddressList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSrcAddrAddressList.setStatus("mandatory")
_RptrSrcAddrSrcTable_Object = MibTable
rptrSrcAddrSrcTable = _RptrSrcAddrSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 5, 2)
)
if mibBuilder.loadTexts:
    rptrSrcAddrSrcTable.setStatus("mandatory")
_RptrSrcAddrSrcTableEntry_Object = MibTableRow
rptrSrcAddrSrcTableEntry = _RptrSrcAddrSrcTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 5, 2, 1)
)
rptrSrcAddrSrcTableEntry.setIndexNames(
    (0, "REPEATER-REV4-MIB", "rptrSrcAddrSrcTableEntryId"),
)
if mibBuilder.loadTexts:
    rptrSrcAddrSrcTableEntry.setStatus("mandatory")


class _RptrSrcAddrSrcTableEntryId_Type(OctetString):
    """Custom type rptrSrcAddrSrcTableEntryId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_RptrSrcAddrSrcTableEntryId_Type.__name__ = "OctetString"
_RptrSrcAddrSrcTableEntryId_Object = MibTableColumn
rptrSrcAddrSrcTableEntryId = _RptrSrcAddrSrcTableEntryId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 5, 2, 1, 1),
    _RptrSrcAddrSrcTableEntryId_Type()
)
rptrSrcAddrSrcTableEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSrcAddrSrcTableEntryId.setStatus("mandatory")
_RptrSrcAddrSrcTableEntryPort_Type = Integer32
_RptrSrcAddrSrcTableEntryPort_Object = MibTableColumn
rptrSrcAddrSrcTableEntryPort = _RptrSrcAddrSrcTableEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 5, 2, 1, 2),
    _RptrSrcAddrSrcTableEntryPort_Type()
)
rptrSrcAddrSrcTableEntryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSrcAddrSrcTableEntryPort.setStatus("mandatory")
_RptrSrcAddrSrcTableEntryPortGroup_Type = Integer32
_RptrSrcAddrSrcTableEntryPortGroup_Object = MibTableColumn
rptrSrcAddrSrcTableEntryPortGroup = _RptrSrcAddrSrcTableEntryPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 5, 2, 1, 3),
    _RptrSrcAddrSrcTableEntryPortGroup_Type()
)
rptrSrcAddrSrcTableEntryPortGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSrcAddrSrcTableEntryPortGroup.setStatus("mandatory")
_RptrSrcAddrMgmt_ObjectIdentity = ObjectIdentity
rptrSrcAddrMgmt = _RptrSrcAddrMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 5, 3)
)
_RptrSrcAddrMgmtSrcAgeInterval_Type = Integer32
_RptrSrcAddrMgmtSrcAgeInterval_Object = MibScalar
rptrSrcAddrMgmtSrcAgeInterval = _RptrSrcAddrMgmtSrcAgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 5, 3, 1),
    _RptrSrcAddrMgmtSrcAgeInterval_Type()
)
rptrSrcAddrMgmtSrcAgeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrSrcAddrMgmtSrcAgeInterval.setStatus("mandatory")


class _RptrSrcAddrMgmtPortLock_Type(Integer32):
    """Custom type rptrSrcAddrMgmtPortLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lock", 2),
          ("portMisMatch", 3),
          ("unlock", 1))
    )


_RptrSrcAddrMgmtPortLock_Type.__name__ = "Integer32"
_RptrSrcAddrMgmtPortLock_Object = MibScalar
rptrSrcAddrMgmtPortLock = _RptrSrcAddrMgmtPortLock_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 5, 3, 2),
    _RptrSrcAddrMgmtPortLock_Type()
)
rptrSrcAddrMgmtPortLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrSrcAddrMgmtPortLock.setStatus("mandatory")
_RptrSrcAddrMgmtActiveUsers_Type = Integer32
_RptrSrcAddrMgmtActiveUsers_Object = MibScalar
rptrSrcAddrMgmtActiveUsers = _RptrSrcAddrMgmtActiveUsers_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 5, 3, 3),
    _RptrSrcAddrMgmtActiveUsers_Type()
)
rptrSrcAddrMgmtActiveUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSrcAddrMgmtActiveUsers.setStatus("mandatory")


class _RptrSrcAddrMgmtHashType_Type(Integer32):
    """Custom type rptrSrcAddrMgmtHashType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("decHash", 2),
          ("noDecHash", 1))
    )


_RptrSrcAddrMgmtHashType_Type.__name__ = "Integer32"
_RptrSrcAddrMgmtHashType_Object = MibScalar
rptrSrcAddrMgmtHashType = _RptrSrcAddrMgmtHashType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 5, 3, 4),
    _RptrSrcAddrMgmtHashType_Type()
)
rptrSrcAddrMgmtHashType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrSrcAddrMgmtHashType.setStatus("mandatory")
_RptrTrap_ObjectIdentity = ObjectIdentity
rptrTrap = _RptrTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 6)
)
_RptrHwTrapSet_ObjectIdentity = ObjectIdentity
rptrHwTrapSet = _RptrHwTrapSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 6, 1)
)


class _RptrHwTrapSetLink_Type(Integer32):
    """Custom type rptrHwTrapSetLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("other", 3))
    )


_RptrHwTrapSetLink_Type.__name__ = "Integer32"
_RptrHwTrapSetLink_Object = MibScalar
rptrHwTrapSetLink = _RptrHwTrapSetLink_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 6, 1, 1),
    _RptrHwTrapSetLink_Type()
)
rptrHwTrapSetLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrHwTrapSetLink.setStatus("mandatory")


class _RptrHwTrapSetSeg_Type(Integer32):
    """Custom type rptrHwTrapSetSeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("other", 3))
    )


_RptrHwTrapSetSeg_Type.__name__ = "Integer32"
_RptrHwTrapSetSeg_Object = MibScalar
rptrHwTrapSetSeg = _RptrHwTrapSetSeg_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 6, 1, 2),
    _RptrHwTrapSetSeg_Type()
)
rptrHwTrapSetSeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrHwTrapSetSeg.setStatus("mandatory")
_RptrSaTrapSet_ObjectIdentity = ObjectIdentity
rptrSaTrapSet = _RptrSaTrapSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 6, 2)
)


class _RptrSaTrapSetSrcaddr_Type(Integer32):
    """Custom type rptrSaTrapSetSrcaddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("other", 3))
    )


_RptrSaTrapSetSrcaddr_Type.__name__ = "Integer32"
_RptrSaTrapSetSrcaddr_Object = MibScalar
rptrSaTrapSetSrcaddr = _RptrSaTrapSetSrcaddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 6, 2, 1),
    _RptrSaTrapSetSrcaddr_Type()
)
rptrSaTrapSetSrcaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrSaTrapSetSrcaddr.setStatus("mandatory")
_RptrSaSecurity_ObjectIdentity = ObjectIdentity
rptrSaSecurity = _RptrSaSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 7)
)


class _RptrSecurityLockState_Type(Integer32):
    """Custom type rptrSecurityLockState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lock", 2),
          ("portMisMatch", 3),
          ("unlock", 1))
    )


_RptrSecurityLockState_Type.__name__ = "Integer32"
_RptrSecurityLockState_Object = MibScalar
rptrSecurityLockState = _RptrSecurityLockState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 7, 1),
    _RptrSecurityLockState_Type()
)
rptrSecurityLockState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrSecurityLockState.setStatus("mandatory")


class _RptrSecuritySecureState_Type(Integer32):
    """Custom type rptrSecuritySecureState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonSecure", 2),
          ("portMisMatch", 3),
          ("secure", 1))
    )


_RptrSecuritySecureState_Type.__name__ = "Integer32"
_RptrSecuritySecureState_Object = MibScalar
rptrSecuritySecureState = _RptrSecuritySecureState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 7, 2),
    _RptrSecuritySecureState_Type()
)
rptrSecuritySecureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrSecuritySecureState.setStatus("mandatory")


class _RptrSecurityLearnState_Type(Integer32):
    """Custom type rptrSecurityLearnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("learn", 1),
          ("noLearn", 2),
          ("portMisMatch", 3))
    )


_RptrSecurityLearnState_Type.__name__ = "Integer32"
_RptrSecurityLearnState_Object = MibScalar
rptrSecurityLearnState = _RptrSecurityLearnState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 7, 3),
    _RptrSecurityLearnState_Type()
)
rptrSecurityLearnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrSecurityLearnState.setStatus("mandatory")


class _RptrSecurityLearnMode_Type(Integer32):
    """Custom type rptrSecurityLearnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("continuous", 2),
          ("oneTime", 1),
          ("portMisMatch", 3))
    )


_RptrSecurityLearnMode_Type.__name__ = "Integer32"
_RptrSecurityLearnMode_Object = MibScalar
rptrSecurityLearnMode = _RptrSecurityLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 1, 7, 4),
    _RptrSecurityLearnMode_Type()
)
rptrSecurityLearnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrSecurityLearnMode.setStatus("mandatory")
_RptrPortGroup_ObjectIdentity = ObjectIdentity
rptrPortGroup = _RptrPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2)
)
_RptrPortGrpMgmtTable_Object = MibTable
rptrPortGrpMgmtTable = _RptrPortGrpMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    rptrPortGrpMgmtTable.setStatus("mandatory")
_RptrPortGrpMgmtEntry_Object = MibTableRow
rptrPortGrpMgmtEntry = _RptrPortGrpMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 1, 1)
)
rptrPortGrpMgmtEntry.setIndexNames(
    (0, "REPEATER-REV4-MIB", "rptrPortGrpMgmtGrpId"),
)
if mibBuilder.loadTexts:
    rptrPortGrpMgmtEntry.setStatus("mandatory")
_RptrPortGrpMgmtGrpId_Type = Integer32
_RptrPortGrpMgmtGrpId_Object = MibTableColumn
rptrPortGrpMgmtGrpId = _RptrPortGrpMgmtGrpId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 1, 1, 1),
    _RptrPortGrpMgmtGrpId_Type()
)
rptrPortGrpMgmtGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpMgmtGrpId.setStatus("mandatory")


class _RptrPortGrpMgmtName_Type(DisplayString):
    """Custom type rptrPortGrpMgmtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_RptrPortGrpMgmtName_Type.__name__ = "DisplayString"
_RptrPortGrpMgmtName_Object = MibTableColumn
rptrPortGrpMgmtName = _RptrPortGrpMgmtName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 1, 1, 2),
    _RptrPortGrpMgmtName_Type()
)
rptrPortGrpMgmtName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortGrpMgmtName.setStatus("mandatory")
_RptrPortGrpMgmtPortCount_Type = Integer32
_RptrPortGrpMgmtPortCount_Object = MibTableColumn
rptrPortGrpMgmtPortCount = _RptrPortGrpMgmtPortCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 1, 1, 3),
    _RptrPortGrpMgmtPortCount_Type()
)
rptrPortGrpMgmtPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpMgmtPortCount.setStatus("mandatory")


class _RptrPortGrpMgmtPortsEnable_Type(Integer32):
    """Custom type rptrPortGrpMgmtPortsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("noEnable", 1))
    )


_RptrPortGrpMgmtPortsEnable_Type.__name__ = "Integer32"
_RptrPortGrpMgmtPortsEnable_Object = MibTableColumn
rptrPortGrpMgmtPortsEnable = _RptrPortGrpMgmtPortsEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 1, 1, 4),
    _RptrPortGrpMgmtPortsEnable_Type()
)
rptrPortGrpMgmtPortsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortGrpMgmtPortsEnable.setStatus("mandatory")
_RptrPortGrpMgmtPortsOn_Type = Integer32
_RptrPortGrpMgmtPortsOn_Object = MibTableColumn
rptrPortGrpMgmtPortsOn = _RptrPortGrpMgmtPortsOn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 1, 1, 5),
    _RptrPortGrpMgmtPortsOn_Type()
)
rptrPortGrpMgmtPortsOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpMgmtPortsOn.setStatus("mandatory")
_RptrPortGrpMgmtPortsOper_Type = Integer32
_RptrPortGrpMgmtPortsOper_Object = MibTableColumn
rptrPortGrpMgmtPortsOper = _RptrPortGrpMgmtPortsOper_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 1, 1, 6),
    _RptrPortGrpMgmtPortsOper_Type()
)
rptrPortGrpMgmtPortsOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpMgmtPortsOper.setStatus("mandatory")
_RptrPortGrpMgmtLogPortCount_Type = Integer32
_RptrPortGrpMgmtLogPortCount_Object = MibTableColumn
rptrPortGrpMgmtLogPortCount = _RptrPortGrpMgmtLogPortCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 1, 1, 7),
    _RptrPortGrpMgmtLogPortCount_Type()
)
rptrPortGrpMgmtLogPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpMgmtLogPortCount.setStatus("mandatory")
_RptrPortGrpStats_ObjectIdentity = ObjectIdentity
rptrPortGrpStats = _RptrPortGrpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2)
)
_RptrPortGrpPktStatsTbl_Object = MibTable
rptrPortGrpPktStatsTbl = _RptrPortGrpPktStatsTbl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rptrPortGrpPktStatsTbl.setStatus("mandatory")
_RptrPortGrpPktStatsEntry_Object = MibTableRow
rptrPortGrpPktStatsEntry = _RptrPortGrpPktStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 1, 1)
)
rptrPortGrpPktStatsEntry.setIndexNames(
    (0, "REPEATER-REV4-MIB", "rptrPortGrpPktStatsId"),
)
if mibBuilder.loadTexts:
    rptrPortGrpPktStatsEntry.setStatus("mandatory")
_RptrPortGrpPktStatsId_Type = Integer32
_RptrPortGrpPktStatsId_Object = MibTableColumn
rptrPortGrpPktStatsId = _RptrPortGrpPktStatsId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 1, 1, 1),
    _RptrPortGrpPktStatsId_Type()
)
rptrPortGrpPktStatsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpPktStatsId.setStatus("mandatory")
_RptrPortGrpPktStatsPkts_Type = Counter32
_RptrPortGrpPktStatsPkts_Object = MibTableColumn
rptrPortGrpPktStatsPkts = _RptrPortGrpPktStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 1, 1, 2),
    _RptrPortGrpPktStatsPkts_Type()
)
rptrPortGrpPktStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpPktStatsPkts.setStatus("mandatory")
_RptrPortGrpPktStatsBytes_Type = Counter32
_RptrPortGrpPktStatsBytes_Object = MibTableColumn
rptrPortGrpPktStatsBytes = _RptrPortGrpPktStatsBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 1, 1, 3),
    _RptrPortGrpPktStatsBytes_Type()
)
rptrPortGrpPktStatsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpPktStatsBytes.setStatus("mandatory")
_RptrPortGrpPktStatsColls_Type = Counter32
_RptrPortGrpPktStatsColls_Object = MibTableColumn
rptrPortGrpPktStatsColls = _RptrPortGrpPktStatsColls_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 1, 1, 4),
    _RptrPortGrpPktStatsColls_Type()
)
rptrPortGrpPktStatsColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpPktStatsColls.setStatus("mandatory")
_RptrPortGrpPktStatsErrors_Type = Counter32
_RptrPortGrpPktStatsErrors_Object = MibTableColumn
rptrPortGrpPktStatsErrors = _RptrPortGrpPktStatsErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 1, 1, 5),
    _RptrPortGrpPktStatsErrors_Type()
)
rptrPortGrpPktStatsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpPktStatsErrors.setStatus("mandatory")
_RptrPortGrpPktStatsAlign_Type = Counter32
_RptrPortGrpPktStatsAlign_Object = MibTableColumn
rptrPortGrpPktStatsAlign = _RptrPortGrpPktStatsAlign_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 1, 1, 6),
    _RptrPortGrpPktStatsAlign_Type()
)
rptrPortGrpPktStatsAlign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpPktStatsAlign.setStatus("mandatory")
_RptrPortGrpPktStatsCRC_Type = Counter32
_RptrPortGrpPktStatsCRC_Object = MibTableColumn
rptrPortGrpPktStatsCRC = _RptrPortGrpPktStatsCRC_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 1, 1, 7),
    _RptrPortGrpPktStatsCRC_Type()
)
rptrPortGrpPktStatsCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpPktStatsCRC.setStatus("mandatory")
_RptrPortGrpPktStatsOOW_Type = Counter32
_RptrPortGrpPktStatsOOW_Object = MibTableColumn
rptrPortGrpPktStatsOOW = _RptrPortGrpPktStatsOOW_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 1, 1, 8),
    _RptrPortGrpPktStatsOOW_Type()
)
rptrPortGrpPktStatsOOW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpPktStatsOOW.setStatus("mandatory")
_RptrPortGrpPktStatsBroadcasts_Type = Counter32
_RptrPortGrpPktStatsBroadcasts_Object = MibTableColumn
rptrPortGrpPktStatsBroadcasts = _RptrPortGrpPktStatsBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 1, 1, 9),
    _RptrPortGrpPktStatsBroadcasts_Type()
)
rptrPortGrpPktStatsBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpPktStatsBroadcasts.setStatus("mandatory")
_RptrPortGrpPktStatsMulticasts_Type = Counter32
_RptrPortGrpPktStatsMulticasts_Object = MibTableColumn
rptrPortGrpPktStatsMulticasts = _RptrPortGrpPktStatsMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 1, 1, 10),
    _RptrPortGrpPktStatsMulticasts_Type()
)
rptrPortGrpPktStatsMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpPktStatsMulticasts.setStatus("mandatory")
_RptrPortGrpProtocolTbl_Object = MibTable
rptrPortGrpProtocolTbl = _RptrPortGrpProtocolTbl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 2)
)
if mibBuilder.loadTexts:
    rptrPortGrpProtocolTbl.setStatus("mandatory")
_RptrPortGrpProtocolEntry_Object = MibTableRow
rptrPortGrpProtocolEntry = _RptrPortGrpProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 2, 1)
)
rptrPortGrpProtocolEntry.setIndexNames(
    (0, "REPEATER-REV4-MIB", "rptrPortGrpProtocolId"),
)
if mibBuilder.loadTexts:
    rptrPortGrpProtocolEntry.setStatus("mandatory")
_RptrPortGrpProtocolId_Type = Integer32
_RptrPortGrpProtocolId_Object = MibTableColumn
rptrPortGrpProtocolId = _RptrPortGrpProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 2, 1, 1),
    _RptrPortGrpProtocolId_Type()
)
rptrPortGrpProtocolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpProtocolId.setStatus("mandatory")
_RptrPortGrpProtocolOSI_Type = Counter32
_RptrPortGrpProtocolOSI_Object = MibTableColumn
rptrPortGrpProtocolOSI = _RptrPortGrpProtocolOSI_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 2, 1, 2),
    _RptrPortGrpProtocolOSI_Type()
)
rptrPortGrpProtocolOSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpProtocolOSI.setStatus("mandatory")
_RptrPortGrpProtocolNovell_Type = Counter32
_RptrPortGrpProtocolNovell_Object = MibTableColumn
rptrPortGrpProtocolNovell = _RptrPortGrpProtocolNovell_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 2, 1, 3),
    _RptrPortGrpProtocolNovell_Type()
)
rptrPortGrpProtocolNovell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpProtocolNovell.setStatus("mandatory")
_RptrPortGrpProtocolBanyan_Type = Counter32
_RptrPortGrpProtocolBanyan_Object = MibTableColumn
rptrPortGrpProtocolBanyan = _RptrPortGrpProtocolBanyan_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 2, 1, 4),
    _RptrPortGrpProtocolBanyan_Type()
)
rptrPortGrpProtocolBanyan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpProtocolBanyan.setStatus("mandatory")
_RptrPortGrpProtocolDECNet_Type = Counter32
_RptrPortGrpProtocolDECNet_Object = MibTableColumn
rptrPortGrpProtocolDECNet = _RptrPortGrpProtocolDECNet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 2, 1, 5),
    _RptrPortGrpProtocolDECNet_Type()
)
rptrPortGrpProtocolDECNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpProtocolDECNet.setStatus("mandatory")
_RptrPortGrpProtocolXNS_Type = Counter32
_RptrPortGrpProtocolXNS_Object = MibTableColumn
rptrPortGrpProtocolXNS = _RptrPortGrpProtocolXNS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 2, 1, 6),
    _RptrPortGrpProtocolXNS_Type()
)
rptrPortGrpProtocolXNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpProtocolXNS.setStatus("mandatory")
_RptrPortGrpProtocolIP_Type = Counter32
_RptrPortGrpProtocolIP_Object = MibTableColumn
rptrPortGrpProtocolIP = _RptrPortGrpProtocolIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 2, 1, 7),
    _RptrPortGrpProtocolIP_Type()
)
rptrPortGrpProtocolIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpProtocolIP.setStatus("mandatory")
_RptrPortGrpProtocolCtron_Type = Counter32
_RptrPortGrpProtocolCtron_Object = MibTableColumn
rptrPortGrpProtocolCtron = _RptrPortGrpProtocolCtron_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 2, 1, 8),
    _RptrPortGrpProtocolCtron_Type()
)
rptrPortGrpProtocolCtron.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpProtocolCtron.setStatus("mandatory")
_RptrPortGrpProtocolAppletalk_Type = Counter32
_RptrPortGrpProtocolAppletalk_Object = MibTableColumn
rptrPortGrpProtocolAppletalk = _RptrPortGrpProtocolAppletalk_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 2, 1, 9),
    _RptrPortGrpProtocolAppletalk_Type()
)
rptrPortGrpProtocolAppletalk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpProtocolAppletalk.setStatus("mandatory")
_RptrPortGrpProtocolOther_Type = Counter32
_RptrPortGrpProtocolOther_Object = MibTableColumn
rptrPortGrpProtocolOther = _RptrPortGrpProtocolOther_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 2, 1, 10),
    _RptrPortGrpProtocolOther_Type()
)
rptrPortGrpProtocolOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpProtocolOther.setStatus("mandatory")
_RptrPortGrpFrameSzTbl_Object = MibTable
rptrPortGrpFrameSzTbl = _RptrPortGrpFrameSzTbl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 3)
)
if mibBuilder.loadTexts:
    rptrPortGrpFrameSzTbl.setStatus("mandatory")
_RptrPortGrpFrameSzEntry_Object = MibTableRow
rptrPortGrpFrameSzEntry = _RptrPortGrpFrameSzEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 3, 1)
)
rptrPortGrpFrameSzEntry.setIndexNames(
    (0, "REPEATER-REV4-MIB", "rptrPortGrpFrameSzId"),
)
if mibBuilder.loadTexts:
    rptrPortGrpFrameSzEntry.setStatus("mandatory")
_RptrPortGrpFrameSzId_Type = Integer32
_RptrPortGrpFrameSzId_Object = MibTableColumn
rptrPortGrpFrameSzId = _RptrPortGrpFrameSzId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 3, 1, 1),
    _RptrPortGrpFrameSzId_Type()
)
rptrPortGrpFrameSzId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpFrameSzId.setStatus("mandatory")
_RptrPortGrpFrameSzRunt_Type = Counter32
_RptrPortGrpFrameSzRunt_Object = MibTableColumn
rptrPortGrpFrameSzRunt = _RptrPortGrpFrameSzRunt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 3, 1, 2),
    _RptrPortGrpFrameSzRunt_Type()
)
rptrPortGrpFrameSzRunt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpFrameSzRunt.setStatus("mandatory")
_RptrPortGrpFrameSz64To127_Type = Counter32
_RptrPortGrpFrameSz64To127_Object = MibTableColumn
rptrPortGrpFrameSz64To127 = _RptrPortGrpFrameSz64To127_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 3, 1, 3),
    _RptrPortGrpFrameSz64To127_Type()
)
rptrPortGrpFrameSz64To127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpFrameSz64To127.setStatus("mandatory")
_RptrPortGrpFrameSz128To255_Type = Counter32
_RptrPortGrpFrameSz128To255_Object = MibTableColumn
rptrPortGrpFrameSz128To255 = _RptrPortGrpFrameSz128To255_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 3, 1, 4),
    _RptrPortGrpFrameSz128To255_Type()
)
rptrPortGrpFrameSz128To255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpFrameSz128To255.setStatus("mandatory")
_RptrPortGrpFrameSz256To511_Type = Counter32
_RptrPortGrpFrameSz256To511_Object = MibTableColumn
rptrPortGrpFrameSz256To511 = _RptrPortGrpFrameSz256To511_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 3, 1, 5),
    _RptrPortGrpFrameSz256To511_Type()
)
rptrPortGrpFrameSz256To511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpFrameSz256To511.setStatus("mandatory")
_RptrPortGrpFrameSz512To1023_Type = Counter32
_RptrPortGrpFrameSz512To1023_Object = MibTableColumn
rptrPortGrpFrameSz512To1023 = _RptrPortGrpFrameSz512To1023_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 3, 1, 6),
    _RptrPortGrpFrameSz512To1023_Type()
)
rptrPortGrpFrameSz512To1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpFrameSz512To1023.setStatus("mandatory")
_RptrPortGrpFrameSz1024To1518_Type = Counter32
_RptrPortGrpFrameSz1024To1518_Object = MibTableColumn
rptrPortGrpFrameSz1024To1518 = _RptrPortGrpFrameSz1024To1518_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 3, 1, 7),
    _RptrPortGrpFrameSz1024To1518_Type()
)
rptrPortGrpFrameSz1024To1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpFrameSz1024To1518.setStatus("mandatory")
_RptrPortGrpFrameSzGiant_Type = Counter32
_RptrPortGrpFrameSzGiant_Object = MibTableColumn
rptrPortGrpFrameSzGiant = _RptrPortGrpFrameSzGiant_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 2, 3, 1, 8),
    _RptrPortGrpFrameSzGiant_Type()
)
rptrPortGrpFrameSzGiant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpFrameSzGiant.setStatus("mandatory")
_RptrPortGrpAlarmTable_Object = MibTable
rptrPortGrpAlarmTable = _RptrPortGrpAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 3)
)
if mibBuilder.loadTexts:
    rptrPortGrpAlarmTable.setStatus("mandatory")
_RptrPortGrpAlarmEntry_Object = MibTableRow
rptrPortGrpAlarmEntry = _RptrPortGrpAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 3, 1)
)
rptrPortGrpAlarmEntry.setIndexNames(
    (0, "REPEATER-REV4-MIB", "rptrPortGrpAlarmId"),
)
if mibBuilder.loadTexts:
    rptrPortGrpAlarmEntry.setStatus("mandatory")
_RptrPortGrpAlarmId_Type = Integer32
_RptrPortGrpAlarmId_Object = MibTableColumn
rptrPortGrpAlarmId = _RptrPortGrpAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 3, 1, 1),
    _RptrPortGrpAlarmId_Type()
)
rptrPortGrpAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpAlarmId.setStatus("mandatory")


class _RptrPortGrpAlarmTrafEnable_Type(Integer32):
    """Custom type rptrPortGrpAlarmTrafEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RptrPortGrpAlarmTrafEnable_Type.__name__ = "Integer32"
_RptrPortGrpAlarmTrafEnable_Object = MibTableColumn
rptrPortGrpAlarmTrafEnable = _RptrPortGrpAlarmTrafEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 3, 1, 2),
    _RptrPortGrpAlarmTrafEnable_Type()
)
rptrPortGrpAlarmTrafEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortGrpAlarmTrafEnable.setStatus("mandatory")
_RptrPortGrpAlarmTrafThreshold_Type = Integer32
_RptrPortGrpAlarmTrafThreshold_Object = MibTableColumn
rptrPortGrpAlarmTrafThreshold = _RptrPortGrpAlarmTrafThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 3, 1, 3),
    _RptrPortGrpAlarmTrafThreshold_Type()
)
rptrPortGrpAlarmTrafThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortGrpAlarmTrafThreshold.setStatus("mandatory")


class _RptrPortGrpAlarmTrafGrpDisable_Type(Integer32):
    """Custom type rptrPortGrpAlarmTrafGrpDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RptrPortGrpAlarmTrafGrpDisable_Type.__name__ = "Integer32"
_RptrPortGrpAlarmTrafGrpDisable_Object = MibTableColumn
rptrPortGrpAlarmTrafGrpDisable = _RptrPortGrpAlarmTrafGrpDisable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 3, 1, 4),
    _RptrPortGrpAlarmTrafGrpDisable_Type()
)
rptrPortGrpAlarmTrafGrpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortGrpAlarmTrafGrpDisable.setStatus("mandatory")


class _RptrPortGrpAlarmCollEnable_Type(Integer32):
    """Custom type rptrPortGrpAlarmCollEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RptrPortGrpAlarmCollEnable_Type.__name__ = "Integer32"
_RptrPortGrpAlarmCollEnable_Object = MibTableColumn
rptrPortGrpAlarmCollEnable = _RptrPortGrpAlarmCollEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 3, 1, 5),
    _RptrPortGrpAlarmCollEnable_Type()
)
rptrPortGrpAlarmCollEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortGrpAlarmCollEnable.setStatus("mandatory")


class _RptrPortGrpAlarmCollThreshold_Type(Integer32):
    """Custom type rptrPortGrpAlarmCollThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )


_RptrPortGrpAlarmCollThreshold_Type.__name__ = "Integer32"
_RptrPortGrpAlarmCollThreshold_Object = MibTableColumn
rptrPortGrpAlarmCollThreshold = _RptrPortGrpAlarmCollThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 3, 1, 6),
    _RptrPortGrpAlarmCollThreshold_Type()
)
rptrPortGrpAlarmCollThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortGrpAlarmCollThreshold.setStatus("mandatory")


class _RptrPortGrpAlarmCollBdDisable_Type(Integer32):
    """Custom type rptrPortGrpAlarmCollBdDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RptrPortGrpAlarmCollBdDisable_Type.__name__ = "Integer32"
_RptrPortGrpAlarmCollBdDisable_Object = MibTableColumn
rptrPortGrpAlarmCollBdDisable = _RptrPortGrpAlarmCollBdDisable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 3, 1, 7),
    _RptrPortGrpAlarmCollBdDisable_Type()
)
rptrPortGrpAlarmCollBdDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortGrpAlarmCollBdDisable.setStatus("mandatory")


class _RptrPortGrpAlarmErrEnable_Type(Integer32):
    """Custom type rptrPortGrpAlarmErrEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RptrPortGrpAlarmErrEnable_Type.__name__ = "Integer32"
_RptrPortGrpAlarmErrEnable_Object = MibTableColumn
rptrPortGrpAlarmErrEnable = _RptrPortGrpAlarmErrEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 3, 1, 8),
    _RptrPortGrpAlarmErrEnable_Type()
)
rptrPortGrpAlarmErrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortGrpAlarmErrEnable.setStatus("mandatory")


class _RptrPortGrpAlarmErrThreshold_Type(Integer32):
    """Custom type rptrPortGrpAlarmErrThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RptrPortGrpAlarmErrThreshold_Type.__name__ = "Integer32"
_RptrPortGrpAlarmErrThreshold_Object = MibTableColumn
rptrPortGrpAlarmErrThreshold = _RptrPortGrpAlarmErrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 3, 1, 9),
    _RptrPortGrpAlarmErrThreshold_Type()
)
rptrPortGrpAlarmErrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortGrpAlarmErrThreshold.setStatus("mandatory")
_RptrPortGrpAlarmErrSource_Type = Integer32
_RptrPortGrpAlarmErrSource_Object = MibTableColumn
rptrPortGrpAlarmErrSource = _RptrPortGrpAlarmErrSource_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 3, 1, 10),
    _RptrPortGrpAlarmErrSource_Type()
)
rptrPortGrpAlarmErrSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortGrpAlarmErrSource.setStatus("mandatory")


class _RptrPortGrpAlarmErrGrpDisable_Type(Integer32):
    """Custom type rptrPortGrpAlarmErrGrpDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RptrPortGrpAlarmErrGrpDisable_Type.__name__ = "Integer32"
_RptrPortGrpAlarmErrGrpDisable_Object = MibTableColumn
rptrPortGrpAlarmErrGrpDisable = _RptrPortGrpAlarmErrGrpDisable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 3, 1, 11),
    _RptrPortGrpAlarmErrGrpDisable_Type()
)
rptrPortGrpAlarmErrGrpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortGrpAlarmErrGrpDisable.setStatus("mandatory")


class _RptrPortGrpAlarmBroadEnable_Type(Integer32):
    """Custom type rptrPortGrpAlarmBroadEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RptrPortGrpAlarmBroadEnable_Type.__name__ = "Integer32"
_RptrPortGrpAlarmBroadEnable_Object = MibTableColumn
rptrPortGrpAlarmBroadEnable = _RptrPortGrpAlarmBroadEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 3, 1, 12),
    _RptrPortGrpAlarmBroadEnable_Type()
)
rptrPortGrpAlarmBroadEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortGrpAlarmBroadEnable.setStatus("mandatory")
_RptrPortGrpAlarmBroadThreshold_Type = Integer32
_RptrPortGrpAlarmBroadThreshold_Object = MibTableColumn
rptrPortGrpAlarmBroadThreshold = _RptrPortGrpAlarmBroadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 3, 1, 13),
    _RptrPortGrpAlarmBroadThreshold_Type()
)
rptrPortGrpAlarmBroadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortGrpAlarmBroadThreshold.setStatus("mandatory")


class _RptrPortGrpAlarmBroadGrpDisable_Type(Integer32):
    """Custom type rptrPortGrpAlarmBroadGrpDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RptrPortGrpAlarmBroadGrpDisable_Type.__name__ = "Integer32"
_RptrPortGrpAlarmBroadGrpDisable_Object = MibTableColumn
rptrPortGrpAlarmBroadGrpDisable = _RptrPortGrpAlarmBroadGrpDisable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 3, 1, 14),
    _RptrPortGrpAlarmBroadGrpDisable_Type()
)
rptrPortGrpAlarmBroadGrpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortGrpAlarmBroadGrpDisable.setStatus("mandatory")
_RptrPortGrpSrcAddrTable_Object = MibTable
rptrPortGrpSrcAddrTable = _RptrPortGrpSrcAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 4)
)
if mibBuilder.loadTexts:
    rptrPortGrpSrcAddrTable.setStatus("mandatory")
_RptrPortGrpSrcAddrEntry_Object = MibTableRow
rptrPortGrpSrcAddrEntry = _RptrPortGrpSrcAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 4, 1)
)
rptrPortGrpSrcAddrEntry.setIndexNames(
    (0, "REPEATER-REV4-MIB", "rptrPortGrpSrcAddrId"),
)
if mibBuilder.loadTexts:
    rptrPortGrpSrcAddrEntry.setStatus("mandatory")
_RptrPortGrpSrcAddrId_Type = Integer32
_RptrPortGrpSrcAddrId_Object = MibTableColumn
rptrPortGrpSrcAddrId = _RptrPortGrpSrcAddrId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 4, 1, 1),
    _RptrPortGrpSrcAddrId_Type()
)
rptrPortGrpSrcAddrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpSrcAddrId.setStatus("mandatory")
_RptrPortGrpSrcAddrActiveUsers_Type = Integer32
_RptrPortGrpSrcAddrActiveUsers_Object = MibTableColumn
rptrPortGrpSrcAddrActiveUsers = _RptrPortGrpSrcAddrActiveUsers_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 4, 1, 2),
    _RptrPortGrpSrcAddrActiveUsers_Type()
)
rptrPortGrpSrcAddrActiveUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpSrcAddrActiveUsers.setStatus("mandatory")
_RptrPortGrpTrap_ObjectIdentity = ObjectIdentity
rptrPortGrpTrap = _RptrPortGrpTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 5)
)
_RptrPortGrpHwTrapSet_ObjectIdentity = ObjectIdentity
rptrPortGrpHwTrapSet = _RptrPortGrpHwTrapSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 5, 1)
)
_RptrPortGrpHwTrapTable_Object = MibTable
rptrPortGrpHwTrapTable = _RptrPortGrpHwTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    rptrPortGrpHwTrapTable.setStatus("mandatory")
_RptrPortGrpHwTrapEntry_Object = MibTableRow
rptrPortGrpHwTrapEntry = _RptrPortGrpHwTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 5, 1, 1, 1)
)
rptrPortGrpHwTrapEntry.setIndexNames(
    (0, "REPEATER-REV4-MIB", "rptrPortGrpHwTrapSetGrpId"),
)
if mibBuilder.loadTexts:
    rptrPortGrpHwTrapEntry.setStatus("mandatory")
_RptrPortGrpHwTrapSetGrpId_Type = Integer32
_RptrPortGrpHwTrapSetGrpId_Object = MibTableColumn
rptrPortGrpHwTrapSetGrpId = _RptrPortGrpHwTrapSetGrpId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 5, 1, 1, 1, 1),
    _RptrPortGrpHwTrapSetGrpId_Type()
)
rptrPortGrpHwTrapSetGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpHwTrapSetGrpId.setStatus("mandatory")


class _RptrPortGrpHwTrapSetLink_Type(Integer32):
    """Custom type rptrPortGrpHwTrapSetLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("other", 3))
    )


_RptrPortGrpHwTrapSetLink_Type.__name__ = "Integer32"
_RptrPortGrpHwTrapSetLink_Object = MibTableColumn
rptrPortGrpHwTrapSetLink = _RptrPortGrpHwTrapSetLink_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 5, 1, 1, 1, 2),
    _RptrPortGrpHwTrapSetLink_Type()
)
rptrPortGrpHwTrapSetLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortGrpHwTrapSetLink.setStatus("mandatory")


class _RptrPortGrpHwTrapSetSeg_Type(Integer32):
    """Custom type rptrPortGrpHwTrapSetSeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("other", 3))
    )


_RptrPortGrpHwTrapSetSeg_Type.__name__ = "Integer32"
_RptrPortGrpHwTrapSetSeg_Object = MibTableColumn
rptrPortGrpHwTrapSetSeg = _RptrPortGrpHwTrapSetSeg_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 5, 1, 1, 1, 3),
    _RptrPortGrpHwTrapSetSeg_Type()
)
rptrPortGrpHwTrapSetSeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortGrpHwTrapSetSeg.setStatus("mandatory")
_RptrPortGrpSaTrapSet_ObjectIdentity = ObjectIdentity
rptrPortGrpSaTrapSet = _RptrPortGrpSaTrapSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 5, 2)
)
_RptrPortGrpSaTrapTable_Object = MibTable
rptrPortGrpSaTrapTable = _RptrPortGrpSaTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    rptrPortGrpSaTrapTable.setStatus("mandatory")
_RptrPortGrpSaTrapEntry_Object = MibTableRow
rptrPortGrpSaTrapEntry = _RptrPortGrpSaTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 5, 2, 1, 1)
)
rptrPortGrpSaTrapEntry.setIndexNames(
    (0, "REPEATER-REV4-MIB", "rptrPortGrpSaTrapSetGrpId"),
)
if mibBuilder.loadTexts:
    rptrPortGrpSaTrapEntry.setStatus("mandatory")
_RptrPortGrpSaTrapSetGrpId_Type = Integer32
_RptrPortGrpSaTrapSetGrpId_Object = MibTableColumn
rptrPortGrpSaTrapSetGrpId = _RptrPortGrpSaTrapSetGrpId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 5, 2, 1, 1, 1),
    _RptrPortGrpSaTrapSetGrpId_Type()
)
rptrPortGrpSaTrapSetGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpSaTrapSetGrpId.setStatus("mandatory")


class _RptrPortGrpSaTrapSetSrcaddr_Type(Integer32):
    """Custom type rptrPortGrpSaTrapSetSrcaddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("other", 3))
    )


_RptrPortGrpSaTrapSetSrcaddr_Type.__name__ = "Integer32"
_RptrPortGrpSaTrapSetSrcaddr_Object = MibTableColumn
rptrPortGrpSaTrapSetSrcaddr = _RptrPortGrpSaTrapSetSrcaddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 5, 2, 1, 1, 2),
    _RptrPortGrpSaTrapSetSrcaddr_Type()
)
rptrPortGrpSaTrapSetSrcaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortGrpSaTrapSetSrcaddr.setStatus("mandatory")
_RptrPortGrpSrcAddrLockTable_Object = MibTable
rptrPortGrpSrcAddrLockTable = _RptrPortGrpSrcAddrLockTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 6)
)
if mibBuilder.loadTexts:
    rptrPortGrpSrcAddrLockTable.setStatus("mandatory")
_RptrPortGrpSrcAddrLockEntry_Object = MibTableRow
rptrPortGrpSrcAddrLockEntry = _RptrPortGrpSrcAddrLockEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 6, 1)
)
rptrPortGrpSrcAddrLockEntry.setIndexNames(
    (0, "REPEATER-REV4-MIB", "rptrPortGrpSrcAddrLockGrpId"),
)
if mibBuilder.loadTexts:
    rptrPortGrpSrcAddrLockEntry.setStatus("mandatory")
_RptrPortGrpSrcAddrLockGrpId_Type = Integer32
_RptrPortGrpSrcAddrLockGrpId_Object = MibTableColumn
rptrPortGrpSrcAddrLockGrpId = _RptrPortGrpSrcAddrLockGrpId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 6, 1, 1),
    _RptrPortGrpSrcAddrLockGrpId_Type()
)
rptrPortGrpSrcAddrLockGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpSrcAddrLockGrpId.setStatus("mandatory")


class _RptrPortGrpSrcAddrLock_Type(Integer32):
    """Custom type rptrPortGrpSrcAddrLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lock", 2),
          ("portMisMatch", 3),
          ("unlock", 1))
    )


_RptrPortGrpSrcAddrLock_Type.__name__ = "Integer32"
_RptrPortGrpSrcAddrLock_Object = MibTableColumn
rptrPortGrpSrcAddrLock = _RptrPortGrpSrcAddrLock_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 6, 1, 2),
    _RptrPortGrpSrcAddrLock_Type()
)
rptrPortGrpSrcAddrLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortGrpSrcAddrLock.setStatus("mandatory")


class _RptrPortGrpSASecuritySecureState_Type(Integer32):
    """Custom type rptrPortGrpSASecuritySecureState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonSecure", 2),
          ("portMisMatch", 3),
          ("secure", 1))
    )


_RptrPortGrpSASecuritySecureState_Type.__name__ = "Integer32"
_RptrPortGrpSASecuritySecureState_Object = MibTableColumn
rptrPortGrpSASecuritySecureState = _RptrPortGrpSASecuritySecureState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 6, 1, 3),
    _RptrPortGrpSASecuritySecureState_Type()
)
rptrPortGrpSASecuritySecureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGrpSASecuritySecureState.setStatus("mandatory")


class _RptrPortGrpSASecurityLearnState_Type(Integer32):
    """Custom type rptrPortGrpSASecurityLearnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("learn", 1),
          ("noLearn", 2),
          ("portMisMatch", 3))
    )


_RptrPortGrpSASecurityLearnState_Type.__name__ = "Integer32"
_RptrPortGrpSASecurityLearnState_Object = MibTableColumn
rptrPortGrpSASecurityLearnState = _RptrPortGrpSASecurityLearnState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 6, 1, 4),
    _RptrPortGrpSASecurityLearnState_Type()
)
rptrPortGrpSASecurityLearnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortGrpSASecurityLearnState.setStatus("mandatory")


class _RptrPortGrpSASecurityLearnMode_Type(Integer32):
    """Custom type rptrPortGrpSASecurityLearnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("continuous", 2),
          ("oneTime", 1),
          ("portMisMatch", 3))
    )


_RptrPortGrpSASecurityLearnMode_Type.__name__ = "Integer32"
_RptrPortGrpSASecurityLearnMode_Object = MibTableColumn
rptrPortGrpSASecurityLearnMode = _RptrPortGrpSASecurityLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 2, 6, 1, 5),
    _RptrPortGrpSASecurityLearnMode_Type()
)
rptrPortGrpSASecurityLearnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortGrpSASecurityLearnMode.setStatus("mandatory")
_RptrPort_ObjectIdentity = ObjectIdentity
rptrPort = _RptrPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3)
)
_RptrPortMgmtTable_Object = MibTable
rptrPortMgmtTable = _RptrPortMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    rptrPortMgmtTable.setStatus("mandatory")
_RptrPortMgmtEntry_Object = MibTableRow
rptrPortMgmtEntry = _RptrPortMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 1, 1)
)
rptrPortMgmtEntry.setIndexNames(
    (0, "REPEATER-REV4-MIB", "rptrPortMgmtPortGrpId"),
    (0, "REPEATER-REV4-MIB", "rptrPortMgmtPortId"),
)
if mibBuilder.loadTexts:
    rptrPortMgmtEntry.setStatus("mandatory")
_RptrPortMgmtPortId_Type = Integer32
_RptrPortMgmtPortId_Object = MibTableColumn
rptrPortMgmtPortId = _RptrPortMgmtPortId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 1, 1, 1),
    _RptrPortMgmtPortId_Type()
)
rptrPortMgmtPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortMgmtPortId.setStatus("mandatory")
_RptrPortMgmtPortGrpId_Type = Integer32
_RptrPortMgmtPortGrpId_Object = MibTableColumn
rptrPortMgmtPortGrpId = _RptrPortMgmtPortGrpId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 1, 1, 2),
    _RptrPortMgmtPortGrpId_Type()
)
rptrPortMgmtPortGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortMgmtPortGrpId.setStatus("mandatory")


class _RptrPortMgmtName_Type(DisplayString):
    """Custom type rptrPortMgmtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_RptrPortMgmtName_Type.__name__ = "DisplayString"
_RptrPortMgmtName_Object = MibTableColumn
rptrPortMgmtName = _RptrPortMgmtName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 1, 1, 3),
    _RptrPortMgmtName_Type()
)
rptrPortMgmtName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortMgmtName.setStatus("mandatory")


class _RptrPortMgmtAdminState_Type(Integer32):
    """Custom type rptrPortMgmtAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RptrPortMgmtAdminState_Type.__name__ = "Integer32"
_RptrPortMgmtAdminState_Object = MibTableColumn
rptrPortMgmtAdminState = _RptrPortMgmtAdminState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 1, 1, 4),
    _RptrPortMgmtAdminState_Type()
)
rptrPortMgmtAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortMgmtAdminState.setStatus("mandatory")


class _RptrPortMgmtOperState_Type(Integer32):
    """Custom type rptrPortMgmtOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notOperational", 1),
          ("operational", 2))
    )


_RptrPortMgmtOperState_Type.__name__ = "Integer32"
_RptrPortMgmtOperState_Object = MibTableColumn
rptrPortMgmtOperState = _RptrPortMgmtOperState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 1, 1, 5),
    _RptrPortMgmtOperState_Type()
)
rptrPortMgmtOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortMgmtOperState.setStatus("mandatory")
_RptrPortMgmtPortType_Type = ObjectIdentifier
_RptrPortMgmtPortType_Object = MibTableColumn
rptrPortMgmtPortType = _RptrPortMgmtPortType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 1, 1, 6),
    _RptrPortMgmtPortType_Type()
)
rptrPortMgmtPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortMgmtPortType.setStatus("mandatory")
_RptrPortStats_ObjectIdentity = ObjectIdentity
rptrPortStats = _RptrPortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2)
)
_RptrPortPktStatsTbl_Object = MibTable
rptrPortPktStatsTbl = _RptrPortPktStatsTbl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 1)
)
if mibBuilder.loadTexts:
    rptrPortPktStatsTbl.setStatus("mandatory")
_RptrPortPktStatsEntry_Object = MibTableRow
rptrPortPktStatsEntry = _RptrPortPktStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 1, 1)
)
rptrPortPktStatsEntry.setIndexNames(
    (0, "REPEATER-REV4-MIB", "rptrPortPktStatsPortGrpId"),
    (0, "REPEATER-REV4-MIB", "rptrPortPktStatsPortId"),
)
if mibBuilder.loadTexts:
    rptrPortPktStatsEntry.setStatus("mandatory")
_RptrPortPktStatsPortId_Type = Integer32
_RptrPortPktStatsPortId_Object = MibTableColumn
rptrPortPktStatsPortId = _RptrPortPktStatsPortId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 1, 1, 1),
    _RptrPortPktStatsPortId_Type()
)
rptrPortPktStatsPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortPktStatsPortId.setStatus("mandatory")
_RptrPortPktStatsPortGrpId_Type = Integer32
_RptrPortPktStatsPortGrpId_Object = MibTableColumn
rptrPortPktStatsPortGrpId = _RptrPortPktStatsPortGrpId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 1, 1, 2),
    _RptrPortPktStatsPortGrpId_Type()
)
rptrPortPktStatsPortGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortPktStatsPortGrpId.setStatus("mandatory")
_RptrPortPktStatsPackets_Type = Counter32
_RptrPortPktStatsPackets_Object = MibTableColumn
rptrPortPktStatsPackets = _RptrPortPktStatsPackets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 1, 1, 3),
    _RptrPortPktStatsPackets_Type()
)
rptrPortPktStatsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortPktStatsPackets.setStatus("mandatory")
_RptrPortPktStatsBytes_Type = Counter32
_RptrPortPktStatsBytes_Object = MibTableColumn
rptrPortPktStatsBytes = _RptrPortPktStatsBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 1, 1, 4),
    _RptrPortPktStatsBytes_Type()
)
rptrPortPktStatsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortPktStatsBytes.setStatus("mandatory")
_RptrPortPktStatsColls_Type = Counter32
_RptrPortPktStatsColls_Object = MibTableColumn
rptrPortPktStatsColls = _RptrPortPktStatsColls_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 1, 1, 5),
    _RptrPortPktStatsColls_Type()
)
rptrPortPktStatsColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortPktStatsColls.setStatus("mandatory")
_RptrPortPktStatsErrors_Type = Counter32
_RptrPortPktStatsErrors_Object = MibTableColumn
rptrPortPktStatsErrors = _RptrPortPktStatsErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 1, 1, 6),
    _RptrPortPktStatsErrors_Type()
)
rptrPortPktStatsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortPktStatsErrors.setStatus("mandatory")
_RptrPortPktStatsAlign_Type = Counter32
_RptrPortPktStatsAlign_Object = MibTableColumn
rptrPortPktStatsAlign = _RptrPortPktStatsAlign_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 1, 1, 7),
    _RptrPortPktStatsAlign_Type()
)
rptrPortPktStatsAlign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortPktStatsAlign.setStatus("mandatory")
_RptrPortPktStatsCRC_Type = Counter32
_RptrPortPktStatsCRC_Object = MibTableColumn
rptrPortPktStatsCRC = _RptrPortPktStatsCRC_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 1, 1, 8),
    _RptrPortPktStatsCRC_Type()
)
rptrPortPktStatsCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortPktStatsCRC.setStatus("mandatory")
_RptrPortPktStatsOOW_Type = Counter32
_RptrPortPktStatsOOW_Object = MibTableColumn
rptrPortPktStatsOOW = _RptrPortPktStatsOOW_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 1, 1, 9),
    _RptrPortPktStatsOOW_Type()
)
rptrPortPktStatsOOW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortPktStatsOOW.setStatus("mandatory")
_RptrPortPktStatsBroadcasts_Type = Counter32
_RptrPortPktStatsBroadcasts_Object = MibTableColumn
rptrPortPktStatsBroadcasts = _RptrPortPktStatsBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 1, 1, 10),
    _RptrPortPktStatsBroadcasts_Type()
)
rptrPortPktStatsBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortPktStatsBroadcasts.setStatus("mandatory")
_RptrPortPktStatsMulticasts_Type = Counter32
_RptrPortPktStatsMulticasts_Object = MibTableColumn
rptrPortPktStatsMulticasts = _RptrPortPktStatsMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 1, 1, 11),
    _RptrPortPktStatsMulticasts_Type()
)
rptrPortPktStatsMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortPktStatsMulticasts.setStatus("mandatory")
_RptrPortProtocolTbl_Object = MibTable
rptrPortProtocolTbl = _RptrPortProtocolTbl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 2)
)
if mibBuilder.loadTexts:
    rptrPortProtocolTbl.setStatus("mandatory")
_RptrPortProtocolEntry_Object = MibTableRow
rptrPortProtocolEntry = _RptrPortProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 2, 1)
)
rptrPortProtocolEntry.setIndexNames(
    (0, "REPEATER-REV4-MIB", "rptrPortProtocolPortGrpId"),
    (0, "REPEATER-REV4-MIB", "rptrPortProtocolPortId"),
)
if mibBuilder.loadTexts:
    rptrPortProtocolEntry.setStatus("mandatory")
_RptrPortProtocolPortId_Type = Integer32
_RptrPortProtocolPortId_Object = MibTableColumn
rptrPortProtocolPortId = _RptrPortProtocolPortId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 2, 1, 1),
    _RptrPortProtocolPortId_Type()
)
rptrPortProtocolPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortProtocolPortId.setStatus("mandatory")
_RptrPortProtocolPortGrpId_Type = Integer32
_RptrPortProtocolPortGrpId_Object = MibTableColumn
rptrPortProtocolPortGrpId = _RptrPortProtocolPortGrpId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 2, 1, 2),
    _RptrPortProtocolPortGrpId_Type()
)
rptrPortProtocolPortGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortProtocolPortGrpId.setStatus("mandatory")
_RptrPortProtocolOSI_Type = Counter32
_RptrPortProtocolOSI_Object = MibTableColumn
rptrPortProtocolOSI = _RptrPortProtocolOSI_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 2, 1, 3),
    _RptrPortProtocolOSI_Type()
)
rptrPortProtocolOSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortProtocolOSI.setStatus("mandatory")
_RptrPortProtocolNovell_Type = Counter32
_RptrPortProtocolNovell_Object = MibTableColumn
rptrPortProtocolNovell = _RptrPortProtocolNovell_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 2, 1, 4),
    _RptrPortProtocolNovell_Type()
)
rptrPortProtocolNovell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortProtocolNovell.setStatus("mandatory")
_RptrPortProtocolBanyan_Type = Counter32
_RptrPortProtocolBanyan_Object = MibTableColumn
rptrPortProtocolBanyan = _RptrPortProtocolBanyan_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 2, 1, 5),
    _RptrPortProtocolBanyan_Type()
)
rptrPortProtocolBanyan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortProtocolBanyan.setStatus("mandatory")
_RptrPortProtocolDECNet_Type = Counter32
_RptrPortProtocolDECNet_Object = MibTableColumn
rptrPortProtocolDECNet = _RptrPortProtocolDECNet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 2, 1, 6),
    _RptrPortProtocolDECNet_Type()
)
rptrPortProtocolDECNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortProtocolDECNet.setStatus("mandatory")
_RptrPortProtocolXNS_Type = Counter32
_RptrPortProtocolXNS_Object = MibTableColumn
rptrPortProtocolXNS = _RptrPortProtocolXNS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 2, 1, 7),
    _RptrPortProtocolXNS_Type()
)
rptrPortProtocolXNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortProtocolXNS.setStatus("mandatory")
_RptrPortProtocolIP_Type = Counter32
_RptrPortProtocolIP_Object = MibTableColumn
rptrPortProtocolIP = _RptrPortProtocolIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 2, 1, 8),
    _RptrPortProtocolIP_Type()
)
rptrPortProtocolIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortProtocolIP.setStatus("mandatory")
_RptrPortProtocolCtron_Type = Counter32
_RptrPortProtocolCtron_Object = MibTableColumn
rptrPortProtocolCtron = _RptrPortProtocolCtron_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 2, 1, 9),
    _RptrPortProtocolCtron_Type()
)
rptrPortProtocolCtron.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortProtocolCtron.setStatus("mandatory")
_RptrPortProtocolAppletalk_Type = Counter32
_RptrPortProtocolAppletalk_Object = MibTableColumn
rptrPortProtocolAppletalk = _RptrPortProtocolAppletalk_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 2, 1, 10),
    _RptrPortProtocolAppletalk_Type()
)
rptrPortProtocolAppletalk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortProtocolAppletalk.setStatus("mandatory")
_RptrPortProtocolOther_Type = Counter32
_RptrPortProtocolOther_Object = MibTableColumn
rptrPortProtocolOther = _RptrPortProtocolOther_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 2, 1, 11),
    _RptrPortProtocolOther_Type()
)
rptrPortProtocolOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortProtocolOther.setStatus("mandatory")
_RptrPortFrameSzTbl_Object = MibTable
rptrPortFrameSzTbl = _RptrPortFrameSzTbl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 3)
)
if mibBuilder.loadTexts:
    rptrPortFrameSzTbl.setStatus("mandatory")
_RptrPortFrameSzEntry_Object = MibTableRow
rptrPortFrameSzEntry = _RptrPortFrameSzEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 3, 1)
)
rptrPortFrameSzEntry.setIndexNames(
    (0, "REPEATER-REV4-MIB", "rptrPortFrameSzPortGrpId"),
    (0, "REPEATER-REV4-MIB", "rptrPortFrameSzPortId"),
)
if mibBuilder.loadTexts:
    rptrPortFrameSzEntry.setStatus("mandatory")
_RptrPortFrameSzPortId_Type = Integer32
_RptrPortFrameSzPortId_Object = MibTableColumn
rptrPortFrameSzPortId = _RptrPortFrameSzPortId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 3, 1, 1),
    _RptrPortFrameSzPortId_Type()
)
rptrPortFrameSzPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortFrameSzPortId.setStatus("mandatory")
_RptrPortFrameSzPortGrpId_Type = Integer32
_RptrPortFrameSzPortGrpId_Object = MibTableColumn
rptrPortFrameSzPortGrpId = _RptrPortFrameSzPortGrpId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 3, 1, 2),
    _RptrPortFrameSzPortGrpId_Type()
)
rptrPortFrameSzPortGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortFrameSzPortGrpId.setStatus("mandatory")
_RptrPortFrameSzRunt_Type = Counter32
_RptrPortFrameSzRunt_Object = MibTableColumn
rptrPortFrameSzRunt = _RptrPortFrameSzRunt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 3, 1, 3),
    _RptrPortFrameSzRunt_Type()
)
rptrPortFrameSzRunt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortFrameSzRunt.setStatus("mandatory")
_RptrPortFrameSz64To127_Type = Counter32
_RptrPortFrameSz64To127_Object = MibTableColumn
rptrPortFrameSz64To127 = _RptrPortFrameSz64To127_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 3, 1, 4),
    _RptrPortFrameSz64To127_Type()
)
rptrPortFrameSz64To127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortFrameSz64To127.setStatus("mandatory")
_RptrPortFrameSz128To255_Type = Counter32
_RptrPortFrameSz128To255_Object = MibTableColumn
rptrPortFrameSz128To255 = _RptrPortFrameSz128To255_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 3, 1, 5),
    _RptrPortFrameSz128To255_Type()
)
rptrPortFrameSz128To255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortFrameSz128To255.setStatus("mandatory")
_RptrPortFrameSz256To511_Type = Counter32
_RptrPortFrameSz256To511_Object = MibTableColumn
rptrPortFrameSz256To511 = _RptrPortFrameSz256To511_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 3, 1, 6),
    _RptrPortFrameSz256To511_Type()
)
rptrPortFrameSz256To511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortFrameSz256To511.setStatus("mandatory")
_RptrPortFrameSz512To1023_Type = Counter32
_RptrPortFrameSz512To1023_Object = MibTableColumn
rptrPortFrameSz512To1023 = _RptrPortFrameSz512To1023_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 3, 1, 7),
    _RptrPortFrameSz512To1023_Type()
)
rptrPortFrameSz512To1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortFrameSz512To1023.setStatus("mandatory")
_RptrPortFrameSz1024To1518_Type = Counter32
_RptrPortFrameSz1024To1518_Object = MibTableColumn
rptrPortFrameSz1024To1518 = _RptrPortFrameSz1024To1518_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 3, 1, 8),
    _RptrPortFrameSz1024To1518_Type()
)
rptrPortFrameSz1024To1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortFrameSz1024To1518.setStatus("mandatory")
_RptrPortFrameSzGiant_Type = Counter32
_RptrPortFrameSzGiant_Object = MibTableColumn
rptrPortFrameSzGiant = _RptrPortFrameSzGiant_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 2, 3, 1, 9),
    _RptrPortFrameSzGiant_Type()
)
rptrPortFrameSzGiant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortFrameSzGiant.setStatus("mandatory")
_RptrPortAlarmTable_Object = MibTable
rptrPortAlarmTable = _RptrPortAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 3)
)
if mibBuilder.loadTexts:
    rptrPortAlarmTable.setStatus("mandatory")
_RptrPortAlarmEntry_Object = MibTableRow
rptrPortAlarmEntry = _RptrPortAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 3, 1)
)
rptrPortAlarmEntry.setIndexNames(
    (0, "REPEATER-REV4-MIB", "rptrPortAlarmPortGrpId"),
    (0, "REPEATER-REV4-MIB", "rptrPortAlarmPortId"),
)
if mibBuilder.loadTexts:
    rptrPortAlarmEntry.setStatus("mandatory")
_RptrPortAlarmPortId_Type = Integer32
_RptrPortAlarmPortId_Object = MibTableColumn
rptrPortAlarmPortId = _RptrPortAlarmPortId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 3, 1, 1),
    _RptrPortAlarmPortId_Type()
)
rptrPortAlarmPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortAlarmPortId.setStatus("mandatory")
_RptrPortAlarmPortGrpId_Type = Integer32
_RptrPortAlarmPortGrpId_Object = MibTableColumn
rptrPortAlarmPortGrpId = _RptrPortAlarmPortGrpId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 3, 1, 2),
    _RptrPortAlarmPortGrpId_Type()
)
rptrPortAlarmPortGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortAlarmPortGrpId.setStatus("mandatory")


class _RptrPortAlarmTrafEnable_Type(Integer32):
    """Custom type rptrPortAlarmTrafEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RptrPortAlarmTrafEnable_Type.__name__ = "Integer32"
_RptrPortAlarmTrafEnable_Object = MibTableColumn
rptrPortAlarmTrafEnable = _RptrPortAlarmTrafEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 3, 1, 3),
    _RptrPortAlarmTrafEnable_Type()
)
rptrPortAlarmTrafEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortAlarmTrafEnable.setStatus("mandatory")
_RptrPortAlarmTrafThreshold_Type = Integer32
_RptrPortAlarmTrafThreshold_Object = MibTableColumn
rptrPortAlarmTrafThreshold = _RptrPortAlarmTrafThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 3, 1, 4),
    _RptrPortAlarmTrafThreshold_Type()
)
rptrPortAlarmTrafThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortAlarmTrafThreshold.setStatus("mandatory")


class _RptrPortAlarmTrafPortDisable_Type(Integer32):
    """Custom type rptrPortAlarmTrafPortDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RptrPortAlarmTrafPortDisable_Type.__name__ = "Integer32"
_RptrPortAlarmTrafPortDisable_Object = MibTableColumn
rptrPortAlarmTrafPortDisable = _RptrPortAlarmTrafPortDisable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 3, 1, 5),
    _RptrPortAlarmTrafPortDisable_Type()
)
rptrPortAlarmTrafPortDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortAlarmTrafPortDisable.setStatus("mandatory")


class _RptrPortAlarmCollEnable_Type(Integer32):
    """Custom type rptrPortAlarmCollEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RptrPortAlarmCollEnable_Type.__name__ = "Integer32"
_RptrPortAlarmCollEnable_Object = MibTableColumn
rptrPortAlarmCollEnable = _RptrPortAlarmCollEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 3, 1, 6),
    _RptrPortAlarmCollEnable_Type()
)
rptrPortAlarmCollEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortAlarmCollEnable.setStatus("mandatory")


class _RptrPortAlarmCollThreshold_Type(Integer32):
    """Custom type rptrPortAlarmCollThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )


_RptrPortAlarmCollThreshold_Type.__name__ = "Integer32"
_RptrPortAlarmCollThreshold_Object = MibTableColumn
rptrPortAlarmCollThreshold = _RptrPortAlarmCollThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 3, 1, 7),
    _RptrPortAlarmCollThreshold_Type()
)
rptrPortAlarmCollThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortAlarmCollThreshold.setStatus("mandatory")


class _RptrPortAlarmCollPortDisable_Type(Integer32):
    """Custom type rptrPortAlarmCollPortDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RptrPortAlarmCollPortDisable_Type.__name__ = "Integer32"
_RptrPortAlarmCollPortDisable_Object = MibTableColumn
rptrPortAlarmCollPortDisable = _RptrPortAlarmCollPortDisable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 3, 1, 8),
    _RptrPortAlarmCollPortDisable_Type()
)
rptrPortAlarmCollPortDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortAlarmCollPortDisable.setStatus("mandatory")


class _RptrPortAlarmErrEnable_Type(Integer32):
    """Custom type rptrPortAlarmErrEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RptrPortAlarmErrEnable_Type.__name__ = "Integer32"
_RptrPortAlarmErrEnable_Object = MibTableColumn
rptrPortAlarmErrEnable = _RptrPortAlarmErrEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 3, 1, 9),
    _RptrPortAlarmErrEnable_Type()
)
rptrPortAlarmErrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortAlarmErrEnable.setStatus("mandatory")


class _RptrPortAlarmErrThreshold_Type(Integer32):
    """Custom type rptrPortAlarmErrThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RptrPortAlarmErrThreshold_Type.__name__ = "Integer32"
_RptrPortAlarmErrThreshold_Object = MibTableColumn
rptrPortAlarmErrThreshold = _RptrPortAlarmErrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 3, 1, 10),
    _RptrPortAlarmErrThreshold_Type()
)
rptrPortAlarmErrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortAlarmErrThreshold.setStatus("mandatory")
_RptrPortAlarmErrSource_Type = Integer32
_RptrPortAlarmErrSource_Object = MibTableColumn
rptrPortAlarmErrSource = _RptrPortAlarmErrSource_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 3, 1, 11),
    _RptrPortAlarmErrSource_Type()
)
rptrPortAlarmErrSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortAlarmErrSource.setStatus("mandatory")


class _RptrPortAlarmErrPortDisable_Type(Integer32):
    """Custom type rptrPortAlarmErrPortDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RptrPortAlarmErrPortDisable_Type.__name__ = "Integer32"
_RptrPortAlarmErrPortDisable_Object = MibTableColumn
rptrPortAlarmErrPortDisable = _RptrPortAlarmErrPortDisable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 3, 1, 12),
    _RptrPortAlarmErrPortDisable_Type()
)
rptrPortAlarmErrPortDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortAlarmErrPortDisable.setStatus("mandatory")


class _RptrPortAlarmBroadEnable_Type(Integer32):
    """Custom type rptrPortAlarmBroadEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RptrPortAlarmBroadEnable_Type.__name__ = "Integer32"
_RptrPortAlarmBroadEnable_Object = MibTableColumn
rptrPortAlarmBroadEnable = _RptrPortAlarmBroadEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 3, 1, 13),
    _RptrPortAlarmBroadEnable_Type()
)
rptrPortAlarmBroadEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortAlarmBroadEnable.setStatus("mandatory")
_RptrPortAlarmBroadThreshold_Type = Integer32
_RptrPortAlarmBroadThreshold_Object = MibTableColumn
rptrPortAlarmBroadThreshold = _RptrPortAlarmBroadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 3, 1, 14),
    _RptrPortAlarmBroadThreshold_Type()
)
rptrPortAlarmBroadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortAlarmBroadThreshold.setStatus("mandatory")


class _RptrPortAlarmBroadPortDisable_Type(Integer32):
    """Custom type rptrPortAlarmBroadPortDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RptrPortAlarmBroadPortDisable_Type.__name__ = "Integer32"
_RptrPortAlarmBroadPortDisable_Object = MibTableColumn
rptrPortAlarmBroadPortDisable = _RptrPortAlarmBroadPortDisable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 3, 1, 15),
    _RptrPortAlarmBroadPortDisable_Type()
)
rptrPortAlarmBroadPortDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortAlarmBroadPortDisable.setStatus("mandatory")
_RptrPortRedundTable_Object = MibTable
rptrPortRedundTable = _RptrPortRedundTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 4)
)
if mibBuilder.loadTexts:
    rptrPortRedundTable.setStatus("mandatory")
_RptrPortRedundEntry_Object = MibTableRow
rptrPortRedundEntry = _RptrPortRedundEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 4, 1)
)
rptrPortRedundEntry.setIndexNames(
    (0, "REPEATER-REV4-MIB", "rptrPortRedundPortGrpId"),
    (0, "REPEATER-REV4-MIB", "rptrPortRedundPortId"),
)
if mibBuilder.loadTexts:
    rptrPortRedundEntry.setStatus("mandatory")
_RptrPortRedundPortId_Type = Integer32
_RptrPortRedundPortId_Object = MibTableColumn
rptrPortRedundPortId = _RptrPortRedundPortId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 4, 1, 1),
    _RptrPortRedundPortId_Type()
)
rptrPortRedundPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortRedundPortId.setStatus("mandatory")
_RptrPortRedundPortGrpId_Type = Integer32
_RptrPortRedundPortGrpId_Object = MibTableColumn
rptrPortRedundPortGrpId = _RptrPortRedundPortGrpId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 4, 1, 2),
    _RptrPortRedundPortGrpId_Type()
)
rptrPortRedundPortGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortRedundPortGrpId.setStatus("mandatory")
_RptrPortRedundCrctNum_Type = Integer32
_RptrPortRedundCrctNum_Object = MibTableColumn
rptrPortRedundCrctNum = _RptrPortRedundCrctNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 4, 1, 3),
    _RptrPortRedundCrctNum_Type()
)
rptrPortRedundCrctNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortRedundCrctNum.setStatus("mandatory")


class _RptrPortRedundType_Type(Integer32):
    """Custom type rptrPortRedundType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 3),
          ("notUsed", 1),
          ("primary", 2))
    )


_RptrPortRedundType_Type.__name__ = "Integer32"
_RptrPortRedundType_Object = MibTableColumn
rptrPortRedundType = _RptrPortRedundType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 4, 1, 4),
    _RptrPortRedundType_Type()
)
rptrPortRedundType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortRedundType.setStatus("mandatory")


class _RptrPortRedundStatus_Type(Integer32):
    """Custom type rptrPortRedundStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 3),
          ("notUsed", 1))
    )


_RptrPortRedundStatus_Type.__name__ = "Integer32"
_RptrPortRedundStatus_Object = MibTableColumn
rptrPortRedundStatus = _RptrPortRedundStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 4, 1, 5),
    _RptrPortRedundStatus_Type()
)
rptrPortRedundStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortRedundStatus.setStatus("mandatory")
_RptrPortSrcAddrTable_Object = MibTable
rptrPortSrcAddrTable = _RptrPortSrcAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 5)
)
if mibBuilder.loadTexts:
    rptrPortSrcAddrTable.setStatus("mandatory")
_RptrPortSrcAddrEntry_Object = MibTableRow
rptrPortSrcAddrEntry = _RptrPortSrcAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 5, 1)
)
rptrPortSrcAddrEntry.setIndexNames(
    (0, "REPEATER-REV4-MIB", "rptrPortSrcAddrPortGrpId"),
    (0, "REPEATER-REV4-MIB", "rptrPortSrcAddrPortId"),
)
if mibBuilder.loadTexts:
    rptrPortSrcAddrEntry.setStatus("mandatory")
_RptrPortSrcAddrPortId_Type = Integer32
_RptrPortSrcAddrPortId_Object = MibTableColumn
rptrPortSrcAddrPortId = _RptrPortSrcAddrPortId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 5, 1, 1),
    _RptrPortSrcAddrPortId_Type()
)
rptrPortSrcAddrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortSrcAddrPortId.setStatus("mandatory")
_RptrPortSrcAddrPortGrpId_Type = Integer32
_RptrPortSrcAddrPortGrpId_Object = MibTableColumn
rptrPortSrcAddrPortGrpId = _RptrPortSrcAddrPortGrpId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 5, 1, 2),
    _RptrPortSrcAddrPortGrpId_Type()
)
rptrPortSrcAddrPortGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortSrcAddrPortGrpId.setStatus("mandatory")


class _RptrPortSrcAddrTopoState_Type(Integer32):
    """Custom type rptrPortSrcAddrTopoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("station", 1),
          ("trunk", 2))
    )


_RptrPortSrcAddrTopoState_Type.__name__ = "Integer32"
_RptrPortSrcAddrTopoState_Object = MibTableColumn
rptrPortSrcAddrTopoState = _RptrPortSrcAddrTopoState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 5, 1, 3),
    _RptrPortSrcAddrTopoState_Type()
)
rptrPortSrcAddrTopoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortSrcAddrTopoState.setStatus("mandatory")


class _RptrPortSrcAddrForceTrunk_Type(Integer32):
    """Custom type rptrPortSrcAddrForceTrunk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("force", 2),
          ("noForce", 1))
    )


_RptrPortSrcAddrForceTrunk_Type.__name__ = "Integer32"
_RptrPortSrcAddrForceTrunk_Object = MibTableColumn
rptrPortSrcAddrForceTrunk = _RptrPortSrcAddrForceTrunk_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 5, 1, 4),
    _RptrPortSrcAddrForceTrunk_Type()
)
rptrPortSrcAddrForceTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortSrcAddrForceTrunk.setStatus("mandatory")
_RptrPortSrcAddrActiveUsers_Type = Integer32
_RptrPortSrcAddrActiveUsers_Object = MibTableColumn
rptrPortSrcAddrActiveUsers = _RptrPortSrcAddrActiveUsers_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 5, 1, 5),
    _RptrPortSrcAddrActiveUsers_Type()
)
rptrPortSrcAddrActiveUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortSrcAddrActiveUsers.setStatus("mandatory")
_RptrPortSrcAddrListTable_Object = MibTable
rptrPortSrcAddrListTable = _RptrPortSrcAddrListTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 6)
)
if mibBuilder.loadTexts:
    rptrPortSrcAddrListTable.setStatus("mandatory")
_RptrPortSrcAddrListEntry_Object = MibTableRow
rptrPortSrcAddrListEntry = _RptrPortSrcAddrListEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 6, 1)
)
rptrPortSrcAddrListEntry.setIndexNames(
    (0, "REPEATER-REV4-MIB", "rptrPortSrcAddrListPortGrpId"),
    (0, "REPEATER-REV4-MIB", "rptrPortSrcAddrListPortId"),
    (0, "REPEATER-REV4-MIB", "rptrPortSrcAddrListId"),
)
if mibBuilder.loadTexts:
    rptrPortSrcAddrListEntry.setStatus("mandatory")
_RptrPortSrcAddrListId_Type = Integer32
_RptrPortSrcAddrListId_Object = MibTableColumn
rptrPortSrcAddrListId = _RptrPortSrcAddrListId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 6, 1, 1),
    _RptrPortSrcAddrListId_Type()
)
rptrPortSrcAddrListId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortSrcAddrListId.setStatus("mandatory")
_RptrPortSrcAddrListPortId_Type = Integer32
_RptrPortSrcAddrListPortId_Object = MibTableColumn
rptrPortSrcAddrListPortId = _RptrPortSrcAddrListPortId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 6, 1, 2),
    _RptrPortSrcAddrListPortId_Type()
)
rptrPortSrcAddrListPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortSrcAddrListPortId.setStatus("mandatory")
_RptrPortSrcAddrListPortGrpId_Type = Integer32
_RptrPortSrcAddrListPortGrpId_Object = MibTableColumn
rptrPortSrcAddrListPortGrpId = _RptrPortSrcAddrListPortGrpId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 6, 1, 3),
    _RptrPortSrcAddrListPortGrpId_Type()
)
rptrPortSrcAddrListPortGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortSrcAddrListPortGrpId.setStatus("mandatory")
_RptrPortSrcAddrAddressList_Type = OctetString
_RptrPortSrcAddrAddressList_Object = MibTableColumn
rptrPortSrcAddrAddressList = _RptrPortSrcAddrAddressList_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 6, 1, 4),
    _RptrPortSrcAddrAddressList_Type()
)
rptrPortSrcAddrAddressList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortSrcAddrAddressList.setStatus("mandatory")
_RptrPortHardwareTable_Object = MibTable
rptrPortHardwareTable = _RptrPortHardwareTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 7)
)
if mibBuilder.loadTexts:
    rptrPortHardwareTable.setStatus("mandatory")
_RptrPortHardwareEntry_Object = MibTableRow
rptrPortHardwareEntry = _RptrPortHardwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 7, 1)
)
rptrPortHardwareEntry.setIndexNames(
    (0, "REPEATER-REV4-MIB", "rptrPortHardwarePortGrpId"),
    (0, "REPEATER-REV4-MIB", "rptrPortHardwarePortId"),
)
if mibBuilder.loadTexts:
    rptrPortHardwareEntry.setStatus("mandatory")
_RptrPortHardwarePortId_Type = Integer32
_RptrPortHardwarePortId_Object = MibTableColumn
rptrPortHardwarePortId = _RptrPortHardwarePortId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 7, 1, 1),
    _RptrPortHardwarePortId_Type()
)
rptrPortHardwarePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortHardwarePortId.setStatus("mandatory")
_RptrPortHardwarePortGrpId_Type = Integer32
_RptrPortHardwarePortGrpId_Object = MibTableColumn
rptrPortHardwarePortGrpId = _RptrPortHardwarePortGrpId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 7, 1, 2),
    _RptrPortHardwarePortGrpId_Type()
)
rptrPortHardwarePortGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortHardwarePortGrpId.setStatus("mandatory")


class _RptrPortHardwareSegStatus_Type(Integer32):
    """Custom type rptrPortHardwareSegStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSegmented", 1),
          ("segmented", 2))
    )


_RptrPortHardwareSegStatus_Type.__name__ = "Integer32"
_RptrPortHardwareSegStatus_Object = MibTableColumn
rptrPortHardwareSegStatus = _RptrPortHardwareSegStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 7, 1, 3),
    _RptrPortHardwareSegStatus_Type()
)
rptrPortHardwareSegStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortHardwareSegStatus.setStatus("mandatory")


class _RptrPortHardwareLinkStatus_Type(Integer32):
    """Custom type rptrPortHardwareLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("linked", 2),
          ("notApplicable", 3),
          ("notLinked", 1))
    )


_RptrPortHardwareLinkStatus_Type.__name__ = "Integer32"
_RptrPortHardwareLinkStatus_Object = MibTableColumn
rptrPortHardwareLinkStatus = _RptrPortHardwareLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 7, 1, 4),
    _RptrPortHardwareLinkStatus_Type()
)
rptrPortHardwareLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortHardwareLinkStatus.setStatus("mandatory")
_RptrPortTrap_ObjectIdentity = ObjectIdentity
rptrPortTrap = _RptrPortTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 8)
)
_RptrPortHwTrapSet_ObjectIdentity = ObjectIdentity
rptrPortHwTrapSet = _RptrPortHwTrapSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 8, 1)
)
_RptrPortHwTrapTable_Object = MibTable
rptrPortHwTrapTable = _RptrPortHwTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 8, 1, 1)
)
if mibBuilder.loadTexts:
    rptrPortHwTrapTable.setStatus("mandatory")
_RptrPortHwTrapEntry_Object = MibTableRow
rptrPortHwTrapEntry = _RptrPortHwTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 8, 1, 1, 1)
)
rptrPortHwTrapEntry.setIndexNames(
    (0, "REPEATER-REV4-MIB", "rptrPortHwTrapSetPortGrpId"),
    (0, "REPEATER-REV4-MIB", "rptrPortHwTrapSetPortId"),
)
if mibBuilder.loadTexts:
    rptrPortHwTrapEntry.setStatus("mandatory")
_RptrPortHwTrapSetPortId_Type = Integer32
_RptrPortHwTrapSetPortId_Object = MibTableColumn
rptrPortHwTrapSetPortId = _RptrPortHwTrapSetPortId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 8, 1, 1, 1, 1),
    _RptrPortHwTrapSetPortId_Type()
)
rptrPortHwTrapSetPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortHwTrapSetPortId.setStatus("mandatory")
_RptrPortHwTrapSetPortGrpId_Type = Integer32
_RptrPortHwTrapSetPortGrpId_Object = MibTableColumn
rptrPortHwTrapSetPortGrpId = _RptrPortHwTrapSetPortGrpId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 8, 1, 1, 1, 2),
    _RptrPortHwTrapSetPortGrpId_Type()
)
rptrPortHwTrapSetPortGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortHwTrapSetPortGrpId.setStatus("mandatory")


class _RptrPortHwTrapSetLink_Type(Integer32):
    """Custom type rptrPortHwTrapSetLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RptrPortHwTrapSetLink_Type.__name__ = "Integer32"
_RptrPortHwTrapSetLink_Object = MibTableColumn
rptrPortHwTrapSetLink = _RptrPortHwTrapSetLink_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 8, 1, 1, 1, 3),
    _RptrPortHwTrapSetLink_Type()
)
rptrPortHwTrapSetLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortHwTrapSetLink.setStatus("mandatory")


class _RptrPortHwTrapSetSeg_Type(Integer32):
    """Custom type rptrPortHwTrapSetSeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RptrPortHwTrapSetSeg_Type.__name__ = "Integer32"
_RptrPortHwTrapSetSeg_Object = MibTableColumn
rptrPortHwTrapSetSeg = _RptrPortHwTrapSetSeg_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 8, 1, 1, 1, 4),
    _RptrPortHwTrapSetSeg_Type()
)
rptrPortHwTrapSetSeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortHwTrapSetSeg.setStatus("mandatory")
_RptrPortSaTrapSet_ObjectIdentity = ObjectIdentity
rptrPortSaTrapSet = _RptrPortSaTrapSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 8, 2)
)
_RptrPortSaTrapTable_Object = MibTable
rptrPortSaTrapTable = _RptrPortSaTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 8, 2, 1)
)
if mibBuilder.loadTexts:
    rptrPortSaTrapTable.setStatus("mandatory")
_RptrPortSaTrapEntry_Object = MibTableRow
rptrPortSaTrapEntry = _RptrPortSaTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 8, 2, 1, 1)
)
rptrPortSaTrapEntry.setIndexNames(
    (0, "REPEATER-REV4-MIB", "rptrPortSaTrapSetPortGrpId"),
    (0, "REPEATER-REV4-MIB", "rptrPortSaTrapSetPortId"),
)
if mibBuilder.loadTexts:
    rptrPortSaTrapEntry.setStatus("mandatory")
_RptrPortSaTrapSetPortId_Type = Integer32
_RptrPortSaTrapSetPortId_Object = MibTableColumn
rptrPortSaTrapSetPortId = _RptrPortSaTrapSetPortId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 8, 2, 1, 1, 1),
    _RptrPortSaTrapSetPortId_Type()
)
rptrPortSaTrapSetPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortSaTrapSetPortId.setStatus("mandatory")
_RptrPortSaTrapSetPortGrpId_Type = Integer32
_RptrPortSaTrapSetPortGrpId_Object = MibTableColumn
rptrPortSaTrapSetPortGrpId = _RptrPortSaTrapSetPortGrpId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 8, 2, 1, 1, 2),
    _RptrPortSaTrapSetPortGrpId_Type()
)
rptrPortSaTrapSetPortGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortSaTrapSetPortGrpId.setStatus("mandatory")


class _RptrPortSaTrapSetSrcaddr_Type(Integer32):
    """Custom type rptrPortSaTrapSetSrcaddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RptrPortSaTrapSetSrcaddr_Type.__name__ = "Integer32"
_RptrPortSaTrapSetSrcaddr_Object = MibTableColumn
rptrPortSaTrapSetSrcaddr = _RptrPortSaTrapSetSrcaddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 8, 2, 1, 1, 3),
    _RptrPortSaTrapSetSrcaddr_Type()
)
rptrPortSaTrapSetSrcaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortSaTrapSetSrcaddr.setStatus("mandatory")
_RptrPortSecurity_ObjectIdentity = ObjectIdentity
rptrPortSecurity = _RptrPortSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 9)
)
_RptrPortSecurityTable_Object = MibTable
rptrPortSecurityTable = _RptrPortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 9, 1)
)
if mibBuilder.loadTexts:
    rptrPortSecurityTable.setStatus("mandatory")
_RptrPortSecurityEntry_Object = MibTableRow
rptrPortSecurityEntry = _RptrPortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 9, 1, 1)
)
rptrPortSecurityEntry.setIndexNames(
    (0, "REPEATER-REV4-MIB", "rptrPortSecurityPortGrpId"),
    (0, "REPEATER-REV4-MIB", "rptrPortSecurityPortId"),
)
if mibBuilder.loadTexts:
    rptrPortSecurityEntry.setStatus("mandatory")
_RptrPortSecurityPortGrpId_Type = Integer32
_RptrPortSecurityPortGrpId_Object = MibTableColumn
rptrPortSecurityPortGrpId = _RptrPortSecurityPortGrpId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 9, 1, 1, 1),
    _RptrPortSecurityPortGrpId_Type()
)
rptrPortSecurityPortGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortSecurityPortGrpId.setStatus("mandatory")
_RptrPortSecurityPortId_Type = Integer32
_RptrPortSecurityPortId_Object = MibTableColumn
rptrPortSecurityPortId = _RptrPortSecurityPortId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 9, 1, 1, 2),
    _RptrPortSecurityPortId_Type()
)
rptrPortSecurityPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortSecurityPortId.setStatus("mandatory")


class _RptrPortSecurityLockStatus_Type(Integer32):
    """Custom type rptrPortSecurityLockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lock", 2),
          ("unlock", 1))
    )


_RptrPortSecurityLockStatus_Type.__name__ = "Integer32"
_RptrPortSecurityLockStatus_Object = MibTableColumn
rptrPortSecurityLockStatus = _RptrPortSecurityLockStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 9, 1, 1, 3),
    _RptrPortSecurityLockStatus_Type()
)
rptrPortSecurityLockStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortSecurityLockStatus.setStatus("mandatory")


class _RptrPortSecurityLockAddAddress_Type(OctetString):
    """Custom type rptrPortSecurityLockAddAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_RptrPortSecurityLockAddAddress_Type.__name__ = "OctetString"
_RptrPortSecurityLockAddAddress_Object = MibTableColumn
rptrPortSecurityLockAddAddress = _RptrPortSecurityLockAddAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 9, 1, 1, 4),
    _RptrPortSecurityLockAddAddress_Type()
)
rptrPortSecurityLockAddAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortSecurityLockAddAddress.setStatus("mandatory")
_RptrPortSecurityLockDelAddress_Type = OctetString
_RptrPortSecurityLockDelAddress_Object = MibTableColumn
rptrPortSecurityLockDelAddress = _RptrPortSecurityLockDelAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 9, 1, 1, 5),
    _RptrPortSecurityLockDelAddress_Type()
)
rptrPortSecurityLockDelAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortSecurityLockDelAddress.setStatus("mandatory")


class _RptrPortSecurityDisableOnViolation_Type(Integer32):
    """Custom type rptrPortSecurityDisableOnViolation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("noDisable", 1))
    )


_RptrPortSecurityDisableOnViolation_Type.__name__ = "Integer32"
_RptrPortSecurityDisableOnViolation_Object = MibTableColumn
rptrPortSecurityDisableOnViolation = _RptrPortSecurityDisableOnViolation_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 9, 1, 1, 6),
    _RptrPortSecurityDisableOnViolation_Type()
)
rptrPortSecurityDisableOnViolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortSecurityDisableOnViolation.setStatus("mandatory")


class _RptrPortSecurityFullSecEnabled_Type(Integer32):
    """Custom type rptrPortSecurityFullSecEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullSecurity", 2),
          ("partialSecurity", 1))
    )


_RptrPortSecurityFullSecEnabled_Type.__name__ = "Integer32"
_RptrPortSecurityFullSecEnabled_Object = MibTableColumn
rptrPortSecurityFullSecEnabled = _RptrPortSecurityFullSecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 9, 1, 1, 7),
    _RptrPortSecurityFullSecEnabled_Type()
)
rptrPortSecurityFullSecEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortSecurityFullSecEnabled.setStatus("mandatory")


class _RptrPortSecuritySecureState_Type(Integer32):
    """Custom type rptrPortSecuritySecureState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonSecure", 2),
          ("secure", 1))
    )


_RptrPortSecuritySecureState_Type.__name__ = "Integer32"
_RptrPortSecuritySecureState_Object = MibTableColumn
rptrPortSecuritySecureState = _RptrPortSecuritySecureState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 9, 1, 1, 8),
    _RptrPortSecuritySecureState_Type()
)
rptrPortSecuritySecureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortSecuritySecureState.setStatus("mandatory")


class _RptrPortSecurityForceNonSecure_Type(Integer32):
    """Custom type rptrPortSecurityForceNonSecure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceNonSecure", 2),
          ("noForce", 1))
    )


_RptrPortSecurityForceNonSecure_Type.__name__ = "Integer32"
_RptrPortSecurityForceNonSecure_Object = MibTableColumn
rptrPortSecurityForceNonSecure = _RptrPortSecurityForceNonSecure_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 9, 1, 1, 9),
    _RptrPortSecurityForceNonSecure_Type()
)
rptrPortSecurityForceNonSecure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortSecurityForceNonSecure.setStatus("mandatory")


class _RptrPortSecurityLearnState_Type(Integer32):
    """Custom type rptrPortSecurityLearnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("learn", 1),
          ("noLearn", 2))
    )


_RptrPortSecurityLearnState_Type.__name__ = "Integer32"
_RptrPortSecurityLearnState_Object = MibTableColumn
rptrPortSecurityLearnState = _RptrPortSecurityLearnState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 9, 1, 1, 10),
    _RptrPortSecurityLearnState_Type()
)
rptrPortSecurityLearnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortSecurityLearnState.setStatus("mandatory")


class _RptrPortSecurityLearnMode_Type(Integer32):
    """Custom type rptrPortSecurityLearnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("continuous", 2),
          ("oneTime", 1))
    )


_RptrPortSecurityLearnMode_Type.__name__ = "Integer32"
_RptrPortSecurityLearnMode_Object = MibTableColumn
rptrPortSecurityLearnMode = _RptrPortSecurityLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 9, 1, 1, 11),
    _RptrPortSecurityLearnMode_Type()
)
rptrPortSecurityLearnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortSecurityLearnMode.setStatus("mandatory")
_RptrPortSecurityListTable_Object = MibTable
rptrPortSecurityListTable = _RptrPortSecurityListTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 9, 2)
)
if mibBuilder.loadTexts:
    rptrPortSecurityListTable.setStatus("mandatory")
_RptrPortSecurityListEntry_Object = MibTableRow
rptrPortSecurityListEntry = _RptrPortSecurityListEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 9, 2, 1)
)
rptrPortSecurityListEntry.setIndexNames(
    (0, "REPEATER-REV4-MIB", "rptrPortSecurityListPortGrpId"),
    (0, "REPEATER-REV4-MIB", "rptrPortSecurityListPortId"),
    (0, "REPEATER-REV4-MIB", "rptrPortSecurityListIndex"),
)
if mibBuilder.loadTexts:
    rptrPortSecurityListEntry.setStatus("mandatory")
_RptrPortSecurityListPortGrpId_Type = Integer32
_RptrPortSecurityListPortGrpId_Object = MibTableColumn
rptrPortSecurityListPortGrpId = _RptrPortSecurityListPortGrpId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 9, 2, 1, 1),
    _RptrPortSecurityListPortGrpId_Type()
)
rptrPortSecurityListPortGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortSecurityListPortGrpId.setStatus("mandatory")
_RptrPortSecurityListPortId_Type = Integer32
_RptrPortSecurityListPortId_Object = MibTableColumn
rptrPortSecurityListPortId = _RptrPortSecurityListPortId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 9, 2, 1, 2),
    _RptrPortSecurityListPortId_Type()
)
rptrPortSecurityListPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortSecurityListPortId.setStatus("mandatory")
_RptrPortSecurityListIndex_Type = Integer32
_RptrPortSecurityListIndex_Object = MibTableColumn
rptrPortSecurityListIndex = _RptrPortSecurityListIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 9, 2, 1, 3),
    _RptrPortSecurityListIndex_Type()
)
rptrPortSecurityListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortSecurityListIndex.setStatus("mandatory")
_RptrPortSecurityListAddress_Type = OctetString
_RptrPortSecurityListAddress_Object = MibTableColumn
rptrPortSecurityListAddress = _RptrPortSecurityListAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 3, 9, 2, 1, 4),
    _RptrPortSecurityListAddress_Type()
)
rptrPortSecurityListAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortSecurityListAddress.setStatus("mandatory")
_RptrPortAssoc_ObjectIdentity = ObjectIdentity
rptrPortAssoc = _RptrPortAssoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 4)
)
_RptrPortAssocTable_Object = MibTable
rptrPortAssocTable = _RptrPortAssocTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 4, 1)
)
if mibBuilder.loadTexts:
    rptrPortAssocTable.setStatus("mandatory")
_RptrPortAssocEntry_Object = MibTableRow
rptrPortAssocEntry = _RptrPortAssocEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 4, 1, 1)
)
rptrPortAssocEntry.setIndexNames(
    (0, "REPEATER-REV4-MIB", "rptrPortAssocBoard"),
)
if mibBuilder.loadTexts:
    rptrPortAssocEntry.setStatus("mandatory")
_RptrPortAssocBoard_Type = Integer32
_RptrPortAssocBoard_Object = MibTableColumn
rptrPortAssocBoard = _RptrPortAssocBoard_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 4, 1, 1, 1),
    _RptrPortAssocBoard_Type()
)
rptrPortAssocBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortAssocBoard.setStatus("mandatory")


class _RptrPortAssocStatus_Type(Integer32):
    """Custom type rptrPortAssocStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("defaultPort", 1),
          ("otherPort", 2))
    )


_RptrPortAssocStatus_Type.__name__ = "Integer32"
_RptrPortAssocStatus_Object = MibTableColumn
rptrPortAssocStatus = _RptrPortAssocStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1, 4, 4, 1, 1, 2),
    _RptrPortAssocStatus_Type()
)
rptrPortAssocStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortAssocStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REPEATER-REV4-MIB",
    **{"repeaterrev4": repeaterrev4,
       "rptr": rptr,
       "rptrMgmt": rptrMgmt,
       "rptrMgmtName": rptrMgmtName,
       "rptrMgmtPortCount": rptrMgmtPortCount,
       "rptrMgmtPortsEnable": rptrMgmtPortsEnable,
       "rptrMgmtPortsOn": rptrMgmtPortsOn,
       "rptrMgmtPortsOper": rptrMgmtPortsOper,
       "rptrMgmtBoardMap": rptrMgmtBoardMap,
       "rptrMgmtInterfaceNum": rptrMgmtInterfaceNum,
       "rptrMgmtResetCounters": rptrMgmtResetCounters,
       "rptrStats": rptrStats,
       "rptrPktStats": rptrPktStats,
       "rptrPktStatsPackets": rptrPktStatsPackets,
       "rptrPktStatsBytes": rptrPktStatsBytes,
       "rptrPktStatsColls": rptrPktStatsColls,
       "rptrPktStatsErrors": rptrPktStatsErrors,
       "rptrPktStatsAlign": rptrPktStatsAlign,
       "rptrPktStatsCRC": rptrPktStatsCRC,
       "rptrPktStatsOOW": rptrPktStatsOOW,
       "rptrPktStatsNoRsc": rptrPktStatsNoRsc,
       "rptrPktStatsBroadcasts": rptrPktStatsBroadcasts,
       "rptrPktStatsMulticasts": rptrPktStatsMulticasts,
       "rptrProtocols": rptrProtocols,
       "rptrProtocolsOSI": rptrProtocolsOSI,
       "rptrProtocolsNovell": rptrProtocolsNovell,
       "rptrProtocolsBanyan": rptrProtocolsBanyan,
       "rptrProtocolsDECNet": rptrProtocolsDECNet,
       "rptrProtocolsXNS": rptrProtocolsXNS,
       "rptrProtocolsIP": rptrProtocolsIP,
       "rptrProtocolsCtron": rptrProtocolsCtron,
       "rptrProtocolsAppletalk": rptrProtocolsAppletalk,
       "rptrProtocolsOther": rptrProtocolsOther,
       "rptrFrameSizes": rptrFrameSizes,
       "rptrFrameSzRunt": rptrFrameSzRunt,
       "rptrFrameSz64To127": rptrFrameSz64To127,
       "rptrFrameSz128To255": rptrFrameSz128To255,
       "rptrFrameSz256To511": rptrFrameSz256To511,
       "rptrFrameSz512To1023": rptrFrameSz512To1023,
       "rptrFrameSz1024To1518": rptrFrameSz1024To1518,
       "rptrFrameSzGiant": rptrFrameSzGiant,
       "rptrAlarms": rptrAlarms,
       "rptrAlarmsTrafEnable": rptrAlarmsTrafEnable,
       "rptrAlarmsTrafThreshold": rptrAlarmsTrafThreshold,
       "rptrAlarmsCollEnable": rptrAlarmsCollEnable,
       "rptrAlarmsCollThreshold": rptrAlarmsCollThreshold,
       "rptrAlarmsErrEnable": rptrAlarmsErrEnable,
       "rptrAlarmsErrThreshold": rptrAlarmsErrThreshold,
       "rptrAlarmsErrSource": rptrAlarmsErrSource,
       "rptrAlarmsAlarmTimebase": rptrAlarmsAlarmTimebase,
       "rptrAlarmsBroadEnable": rptrAlarmsBroadEnable,
       "rptrAlarmsBroadThreshold": rptrAlarmsBroadThreshold,
       "rptrRedundancy": rptrRedundancy,
       "rptrRedund": rptrRedund,
       "rptrRedundReset": rptrRedundReset,
       "rptrRedundPollInterval": rptrRedundPollInterval,
       "rptrRedundTestTOD": rptrRedundTestTOD,
       "rptrRedundPerformTest": rptrRedundPerformTest,
       "rptrRedundMaxCrcts": rptrRedundMaxCrcts,
       "rptrRedundCrctTable": rptrRedundCrctTable,
       "rptrRedundCrctEntry": rptrRedundCrctEntry,
       "rptrRedundCrctId": rptrRedundCrctId,
       "rptrRedundCrctName": rptrRedundCrctName,
       "rptrRedundCrctRetrys": rptrRedundCrctRetrys,
       "rptrRedundCrctNumBPs": rptrRedundCrctNumBPs,
       "rptrRedundCrctNumAddr": rptrRedundCrctNumAddr,
       "rptrRedundCrctAddAddr": rptrRedundCrctAddAddr,
       "rptrRedundCrctDelAddr": rptrRedundCrctDelAddr,
       "rptrRedundCrctEnable": rptrRedundCrctEnable,
       "rptrRedundCrctReset": rptrRedundCrctReset,
       "rptrRedundPortTable": rptrRedundPortTable,
       "rptrRedundPortEntry": rptrRedundPortEntry,
       "rptrRedundPortId": rptrRedundPortId,
       "rptrRedundPortCrctId": rptrRedundPortCrctId,
       "rptrRedundPortNum": rptrRedundPortNum,
       "rptrRedundPortBoardNum": rptrRedundPortBoardNum,
       "rptrRedundPortType": rptrRedundPortType,
       "rptrRedundAddrTable": rptrRedundAddrTable,
       "rptrRedundAddrEntry": rptrRedundAddrEntry,
       "rptrRedundAddrId": rptrRedundAddrId,
       "rptrRedundAddrCrctId": rptrRedundAddrCrctId,
       "rptrRedundAddrIPAddr": rptrRedundAddrIPAddr,
       "rptrSourceAddress": rptrSourceAddress,
       "rptrSrcAddrListTable": rptrSrcAddrListTable,
       "rptrSrcAddrListEntry": rptrSrcAddrListEntry,
       "rptrSrcAddrListId": rptrSrcAddrListId,
       "rptrSrcAddrAddressList": rptrSrcAddrAddressList,
       "rptrSrcAddrSrcTable": rptrSrcAddrSrcTable,
       "rptrSrcAddrSrcTableEntry": rptrSrcAddrSrcTableEntry,
       "rptrSrcAddrSrcTableEntryId": rptrSrcAddrSrcTableEntryId,
       "rptrSrcAddrSrcTableEntryPort": rptrSrcAddrSrcTableEntryPort,
       "rptrSrcAddrSrcTableEntryPortGroup": rptrSrcAddrSrcTableEntryPortGroup,
       "rptrSrcAddrMgmt": rptrSrcAddrMgmt,
       "rptrSrcAddrMgmtSrcAgeInterval": rptrSrcAddrMgmtSrcAgeInterval,
       "rptrSrcAddrMgmtPortLock": rptrSrcAddrMgmtPortLock,
       "rptrSrcAddrMgmtActiveUsers": rptrSrcAddrMgmtActiveUsers,
       "rptrSrcAddrMgmtHashType": rptrSrcAddrMgmtHashType,
       "rptrTrap": rptrTrap,
       "rptrHwTrapSet": rptrHwTrapSet,
       "rptrHwTrapSetLink": rptrHwTrapSetLink,
       "rptrHwTrapSetSeg": rptrHwTrapSetSeg,
       "rptrSaTrapSet": rptrSaTrapSet,
       "rptrSaTrapSetSrcaddr": rptrSaTrapSetSrcaddr,
       "rptrSaSecurity": rptrSaSecurity,
       "rptrSecurityLockState": rptrSecurityLockState,
       "rptrSecuritySecureState": rptrSecuritySecureState,
       "rptrSecurityLearnState": rptrSecurityLearnState,
       "rptrSecurityLearnMode": rptrSecurityLearnMode,
       "rptrPortGroup": rptrPortGroup,
       "rptrPortGrpMgmtTable": rptrPortGrpMgmtTable,
       "rptrPortGrpMgmtEntry": rptrPortGrpMgmtEntry,
       "rptrPortGrpMgmtGrpId": rptrPortGrpMgmtGrpId,
       "rptrPortGrpMgmtName": rptrPortGrpMgmtName,
       "rptrPortGrpMgmtPortCount": rptrPortGrpMgmtPortCount,
       "rptrPortGrpMgmtPortsEnable": rptrPortGrpMgmtPortsEnable,
       "rptrPortGrpMgmtPortsOn": rptrPortGrpMgmtPortsOn,
       "rptrPortGrpMgmtPortsOper": rptrPortGrpMgmtPortsOper,
       "rptrPortGrpMgmtLogPortCount": rptrPortGrpMgmtLogPortCount,
       "rptrPortGrpStats": rptrPortGrpStats,
       "rptrPortGrpPktStatsTbl": rptrPortGrpPktStatsTbl,
       "rptrPortGrpPktStatsEntry": rptrPortGrpPktStatsEntry,
       "rptrPortGrpPktStatsId": rptrPortGrpPktStatsId,
       "rptrPortGrpPktStatsPkts": rptrPortGrpPktStatsPkts,
       "rptrPortGrpPktStatsBytes": rptrPortGrpPktStatsBytes,
       "rptrPortGrpPktStatsColls": rptrPortGrpPktStatsColls,
       "rptrPortGrpPktStatsErrors": rptrPortGrpPktStatsErrors,
       "rptrPortGrpPktStatsAlign": rptrPortGrpPktStatsAlign,
       "rptrPortGrpPktStatsCRC": rptrPortGrpPktStatsCRC,
       "rptrPortGrpPktStatsOOW": rptrPortGrpPktStatsOOW,
       "rptrPortGrpPktStatsBroadcasts": rptrPortGrpPktStatsBroadcasts,
       "rptrPortGrpPktStatsMulticasts": rptrPortGrpPktStatsMulticasts,
       "rptrPortGrpProtocolTbl": rptrPortGrpProtocolTbl,
       "rptrPortGrpProtocolEntry": rptrPortGrpProtocolEntry,
       "rptrPortGrpProtocolId": rptrPortGrpProtocolId,
       "rptrPortGrpProtocolOSI": rptrPortGrpProtocolOSI,
       "rptrPortGrpProtocolNovell": rptrPortGrpProtocolNovell,
       "rptrPortGrpProtocolBanyan": rptrPortGrpProtocolBanyan,
       "rptrPortGrpProtocolDECNet": rptrPortGrpProtocolDECNet,
       "rptrPortGrpProtocolXNS": rptrPortGrpProtocolXNS,
       "rptrPortGrpProtocolIP": rptrPortGrpProtocolIP,
       "rptrPortGrpProtocolCtron": rptrPortGrpProtocolCtron,
       "rptrPortGrpProtocolAppletalk": rptrPortGrpProtocolAppletalk,
       "rptrPortGrpProtocolOther": rptrPortGrpProtocolOther,
       "rptrPortGrpFrameSzTbl": rptrPortGrpFrameSzTbl,
       "rptrPortGrpFrameSzEntry": rptrPortGrpFrameSzEntry,
       "rptrPortGrpFrameSzId": rptrPortGrpFrameSzId,
       "rptrPortGrpFrameSzRunt": rptrPortGrpFrameSzRunt,
       "rptrPortGrpFrameSz64To127": rptrPortGrpFrameSz64To127,
       "rptrPortGrpFrameSz128To255": rptrPortGrpFrameSz128To255,
       "rptrPortGrpFrameSz256To511": rptrPortGrpFrameSz256To511,
       "rptrPortGrpFrameSz512To1023": rptrPortGrpFrameSz512To1023,
       "rptrPortGrpFrameSz1024To1518": rptrPortGrpFrameSz1024To1518,
       "rptrPortGrpFrameSzGiant": rptrPortGrpFrameSzGiant,
       "rptrPortGrpAlarmTable": rptrPortGrpAlarmTable,
       "rptrPortGrpAlarmEntry": rptrPortGrpAlarmEntry,
       "rptrPortGrpAlarmId": rptrPortGrpAlarmId,
       "rptrPortGrpAlarmTrafEnable": rptrPortGrpAlarmTrafEnable,
       "rptrPortGrpAlarmTrafThreshold": rptrPortGrpAlarmTrafThreshold,
       "rptrPortGrpAlarmTrafGrpDisable": rptrPortGrpAlarmTrafGrpDisable,
       "rptrPortGrpAlarmCollEnable": rptrPortGrpAlarmCollEnable,
       "rptrPortGrpAlarmCollThreshold": rptrPortGrpAlarmCollThreshold,
       "rptrPortGrpAlarmCollBdDisable": rptrPortGrpAlarmCollBdDisable,
       "rptrPortGrpAlarmErrEnable": rptrPortGrpAlarmErrEnable,
       "rptrPortGrpAlarmErrThreshold": rptrPortGrpAlarmErrThreshold,
       "rptrPortGrpAlarmErrSource": rptrPortGrpAlarmErrSource,
       "rptrPortGrpAlarmErrGrpDisable": rptrPortGrpAlarmErrGrpDisable,
       "rptrPortGrpAlarmBroadEnable": rptrPortGrpAlarmBroadEnable,
       "rptrPortGrpAlarmBroadThreshold": rptrPortGrpAlarmBroadThreshold,
       "rptrPortGrpAlarmBroadGrpDisable": rptrPortGrpAlarmBroadGrpDisable,
       "rptrPortGrpSrcAddrTable": rptrPortGrpSrcAddrTable,
       "rptrPortGrpSrcAddrEntry": rptrPortGrpSrcAddrEntry,
       "rptrPortGrpSrcAddrId": rptrPortGrpSrcAddrId,
       "rptrPortGrpSrcAddrActiveUsers": rptrPortGrpSrcAddrActiveUsers,
       "rptrPortGrpTrap": rptrPortGrpTrap,
       "rptrPortGrpHwTrapSet": rptrPortGrpHwTrapSet,
       "rptrPortGrpHwTrapTable": rptrPortGrpHwTrapTable,
       "rptrPortGrpHwTrapEntry": rptrPortGrpHwTrapEntry,
       "rptrPortGrpHwTrapSetGrpId": rptrPortGrpHwTrapSetGrpId,
       "rptrPortGrpHwTrapSetLink": rptrPortGrpHwTrapSetLink,
       "rptrPortGrpHwTrapSetSeg": rptrPortGrpHwTrapSetSeg,
       "rptrPortGrpSaTrapSet": rptrPortGrpSaTrapSet,
       "rptrPortGrpSaTrapTable": rptrPortGrpSaTrapTable,
       "rptrPortGrpSaTrapEntry": rptrPortGrpSaTrapEntry,
       "rptrPortGrpSaTrapSetGrpId": rptrPortGrpSaTrapSetGrpId,
       "rptrPortGrpSaTrapSetSrcaddr": rptrPortGrpSaTrapSetSrcaddr,
       "rptrPortGrpSrcAddrLockTable": rptrPortGrpSrcAddrLockTable,
       "rptrPortGrpSrcAddrLockEntry": rptrPortGrpSrcAddrLockEntry,
       "rptrPortGrpSrcAddrLockGrpId": rptrPortGrpSrcAddrLockGrpId,
       "rptrPortGrpSrcAddrLock": rptrPortGrpSrcAddrLock,
       "rptrPortGrpSASecuritySecureState": rptrPortGrpSASecuritySecureState,
       "rptrPortGrpSASecurityLearnState": rptrPortGrpSASecurityLearnState,
       "rptrPortGrpSASecurityLearnMode": rptrPortGrpSASecurityLearnMode,
       "rptrPort": rptrPort,
       "rptrPortMgmtTable": rptrPortMgmtTable,
       "rptrPortMgmtEntry": rptrPortMgmtEntry,
       "rptrPortMgmtPortId": rptrPortMgmtPortId,
       "rptrPortMgmtPortGrpId": rptrPortMgmtPortGrpId,
       "rptrPortMgmtName": rptrPortMgmtName,
       "rptrPortMgmtAdminState": rptrPortMgmtAdminState,
       "rptrPortMgmtOperState": rptrPortMgmtOperState,
       "rptrPortMgmtPortType": rptrPortMgmtPortType,
       "rptrPortStats": rptrPortStats,
       "rptrPortPktStatsTbl": rptrPortPktStatsTbl,
       "rptrPortPktStatsEntry": rptrPortPktStatsEntry,
       "rptrPortPktStatsPortId": rptrPortPktStatsPortId,
       "rptrPortPktStatsPortGrpId": rptrPortPktStatsPortGrpId,
       "rptrPortPktStatsPackets": rptrPortPktStatsPackets,
       "rptrPortPktStatsBytes": rptrPortPktStatsBytes,
       "rptrPortPktStatsColls": rptrPortPktStatsColls,
       "rptrPortPktStatsErrors": rptrPortPktStatsErrors,
       "rptrPortPktStatsAlign": rptrPortPktStatsAlign,
       "rptrPortPktStatsCRC": rptrPortPktStatsCRC,
       "rptrPortPktStatsOOW": rptrPortPktStatsOOW,
       "rptrPortPktStatsBroadcasts": rptrPortPktStatsBroadcasts,
       "rptrPortPktStatsMulticasts": rptrPortPktStatsMulticasts,
       "rptrPortProtocolTbl": rptrPortProtocolTbl,
       "rptrPortProtocolEntry": rptrPortProtocolEntry,
       "rptrPortProtocolPortId": rptrPortProtocolPortId,
       "rptrPortProtocolPortGrpId": rptrPortProtocolPortGrpId,
       "rptrPortProtocolOSI": rptrPortProtocolOSI,
       "rptrPortProtocolNovell": rptrPortProtocolNovell,
       "rptrPortProtocolBanyan": rptrPortProtocolBanyan,
       "rptrPortProtocolDECNet": rptrPortProtocolDECNet,
       "rptrPortProtocolXNS": rptrPortProtocolXNS,
       "rptrPortProtocolIP": rptrPortProtocolIP,
       "rptrPortProtocolCtron": rptrPortProtocolCtron,
       "rptrPortProtocolAppletalk": rptrPortProtocolAppletalk,
       "rptrPortProtocolOther": rptrPortProtocolOther,
       "rptrPortFrameSzTbl": rptrPortFrameSzTbl,
       "rptrPortFrameSzEntry": rptrPortFrameSzEntry,
       "rptrPortFrameSzPortId": rptrPortFrameSzPortId,
       "rptrPortFrameSzPortGrpId": rptrPortFrameSzPortGrpId,
       "rptrPortFrameSzRunt": rptrPortFrameSzRunt,
       "rptrPortFrameSz64To127": rptrPortFrameSz64To127,
       "rptrPortFrameSz128To255": rptrPortFrameSz128To255,
       "rptrPortFrameSz256To511": rptrPortFrameSz256To511,
       "rptrPortFrameSz512To1023": rptrPortFrameSz512To1023,
       "rptrPortFrameSz1024To1518": rptrPortFrameSz1024To1518,
       "rptrPortFrameSzGiant": rptrPortFrameSzGiant,
       "rptrPortAlarmTable": rptrPortAlarmTable,
       "rptrPortAlarmEntry": rptrPortAlarmEntry,
       "rptrPortAlarmPortId": rptrPortAlarmPortId,
       "rptrPortAlarmPortGrpId": rptrPortAlarmPortGrpId,
       "rptrPortAlarmTrafEnable": rptrPortAlarmTrafEnable,
       "rptrPortAlarmTrafThreshold": rptrPortAlarmTrafThreshold,
       "rptrPortAlarmTrafPortDisable": rptrPortAlarmTrafPortDisable,
       "rptrPortAlarmCollEnable": rptrPortAlarmCollEnable,
       "rptrPortAlarmCollThreshold": rptrPortAlarmCollThreshold,
       "rptrPortAlarmCollPortDisable": rptrPortAlarmCollPortDisable,
       "rptrPortAlarmErrEnable": rptrPortAlarmErrEnable,
       "rptrPortAlarmErrThreshold": rptrPortAlarmErrThreshold,
       "rptrPortAlarmErrSource": rptrPortAlarmErrSource,
       "rptrPortAlarmErrPortDisable": rptrPortAlarmErrPortDisable,
       "rptrPortAlarmBroadEnable": rptrPortAlarmBroadEnable,
       "rptrPortAlarmBroadThreshold": rptrPortAlarmBroadThreshold,
       "rptrPortAlarmBroadPortDisable": rptrPortAlarmBroadPortDisable,
       "rptrPortRedundTable": rptrPortRedundTable,
       "rptrPortRedundEntry": rptrPortRedundEntry,
       "rptrPortRedundPortId": rptrPortRedundPortId,
       "rptrPortRedundPortGrpId": rptrPortRedundPortGrpId,
       "rptrPortRedundCrctNum": rptrPortRedundCrctNum,
       "rptrPortRedundType": rptrPortRedundType,
       "rptrPortRedundStatus": rptrPortRedundStatus,
       "rptrPortSrcAddrTable": rptrPortSrcAddrTable,
       "rptrPortSrcAddrEntry": rptrPortSrcAddrEntry,
       "rptrPortSrcAddrPortId": rptrPortSrcAddrPortId,
       "rptrPortSrcAddrPortGrpId": rptrPortSrcAddrPortGrpId,
       "rptrPortSrcAddrTopoState": rptrPortSrcAddrTopoState,
       "rptrPortSrcAddrForceTrunk": rptrPortSrcAddrForceTrunk,
       "rptrPortSrcAddrActiveUsers": rptrPortSrcAddrActiveUsers,
       "rptrPortSrcAddrListTable": rptrPortSrcAddrListTable,
       "rptrPortSrcAddrListEntry": rptrPortSrcAddrListEntry,
       "rptrPortSrcAddrListId": rptrPortSrcAddrListId,
       "rptrPortSrcAddrListPortId": rptrPortSrcAddrListPortId,
       "rptrPortSrcAddrListPortGrpId": rptrPortSrcAddrListPortGrpId,
       "rptrPortSrcAddrAddressList": rptrPortSrcAddrAddressList,
       "rptrPortHardwareTable": rptrPortHardwareTable,
       "rptrPortHardwareEntry": rptrPortHardwareEntry,
       "rptrPortHardwarePortId": rptrPortHardwarePortId,
       "rptrPortHardwarePortGrpId": rptrPortHardwarePortGrpId,
       "rptrPortHardwareSegStatus": rptrPortHardwareSegStatus,
       "rptrPortHardwareLinkStatus": rptrPortHardwareLinkStatus,
       "rptrPortTrap": rptrPortTrap,
       "rptrPortHwTrapSet": rptrPortHwTrapSet,
       "rptrPortHwTrapTable": rptrPortHwTrapTable,
       "rptrPortHwTrapEntry": rptrPortHwTrapEntry,
       "rptrPortHwTrapSetPortId": rptrPortHwTrapSetPortId,
       "rptrPortHwTrapSetPortGrpId": rptrPortHwTrapSetPortGrpId,
       "rptrPortHwTrapSetLink": rptrPortHwTrapSetLink,
       "rptrPortHwTrapSetSeg": rptrPortHwTrapSetSeg,
       "rptrPortSaTrapSet": rptrPortSaTrapSet,
       "rptrPortSaTrapTable": rptrPortSaTrapTable,
       "rptrPortSaTrapEntry": rptrPortSaTrapEntry,
       "rptrPortSaTrapSetPortId": rptrPortSaTrapSetPortId,
       "rptrPortSaTrapSetPortGrpId": rptrPortSaTrapSetPortGrpId,
       "rptrPortSaTrapSetSrcaddr": rptrPortSaTrapSetSrcaddr,
       "rptrPortSecurity": rptrPortSecurity,
       "rptrPortSecurityTable": rptrPortSecurityTable,
       "rptrPortSecurityEntry": rptrPortSecurityEntry,
       "rptrPortSecurityPortGrpId": rptrPortSecurityPortGrpId,
       "rptrPortSecurityPortId": rptrPortSecurityPortId,
       "rptrPortSecurityLockStatus": rptrPortSecurityLockStatus,
       "rptrPortSecurityLockAddAddress": rptrPortSecurityLockAddAddress,
       "rptrPortSecurityLockDelAddress": rptrPortSecurityLockDelAddress,
       "rptrPortSecurityDisableOnViolation": rptrPortSecurityDisableOnViolation,
       "rptrPortSecurityFullSecEnabled": rptrPortSecurityFullSecEnabled,
       "rptrPortSecuritySecureState": rptrPortSecuritySecureState,
       "rptrPortSecurityForceNonSecure": rptrPortSecurityForceNonSecure,
       "rptrPortSecurityLearnState": rptrPortSecurityLearnState,
       "rptrPortSecurityLearnMode": rptrPortSecurityLearnMode,
       "rptrPortSecurityListTable": rptrPortSecurityListTable,
       "rptrPortSecurityListEntry": rptrPortSecurityListEntry,
       "rptrPortSecurityListPortGrpId": rptrPortSecurityListPortGrpId,
       "rptrPortSecurityListPortId": rptrPortSecurityListPortId,
       "rptrPortSecurityListIndex": rptrPortSecurityListIndex,
       "rptrPortSecurityListAddress": rptrPortSecurityListAddress,
       "rptrPortAssoc": rptrPortAssoc,
       "rptrPortAssocTable": rptrPortAssocTable,
       "rptrPortAssocEntry": rptrPortAssocEntry,
       "rptrPortAssocBoard": rptrPortAssocBoard,
       "rptrPortAssocStatus": rptrPortAssocStatus}
)
