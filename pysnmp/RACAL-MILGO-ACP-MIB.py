# SNMP MIB module (RACAL-MILGO-ACP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RACAL-MILGO-ACP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:41:08 2024
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

_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Experimental_ObjectIdentity = ObjectIdentity
experimental = _Experimental_ObjectIdentity(
    (1, 3, 6, 1, 3)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Mib_racal_milgo_ObjectIdentity = ObjectIdentity
mib_racal_milgo = _Mib_racal_milgo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 124)
)
_RmAcp_ObjectIdentity = ObjectIdentity
rmAcp = _RmAcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 124, 2)
)
_AcpSys_ObjectIdentity = ObjectIdentity
acpSys = _AcpSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 124, 2, 1)
)
_AcpSysNodeId_Type = OctetString
_AcpSysNodeId_Object = MibScalar
acpSysNodeId = _AcpSysNodeId_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 1, 1),
    _AcpSysNodeId_Type()
)
acpSysNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpSysNodeId.setStatus("mandatory")
_AcpSysAlarm_Type = OctetString
_AcpSysAlarm_Object = MibScalar
acpSysAlarm = _AcpSysAlarm_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 1, 2),
    _AcpSysAlarm_Type()
)
acpSysAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpSysAlarm.setStatus("mandatory")
_AcpSysModTable_Object = MibTable
acpSysModTable = _AcpSysModTable_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 1, 3)
)
if mibBuilder.loadTexts:
    acpSysModTable.setStatus("mandatory")
_AcpSysModEntry_Object = MibTableRow
acpSysModEntry = _AcpSysModEntry_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 1, 3, 1)
)
acpSysModEntry.setIndexNames(
    (0, "RACAL-MILGO-ACP-MIB", "acpSysModType"),
)
if mibBuilder.loadTexts:
    acpSysModEntry.setStatus("mandatory")


class _AcpSysModType_Type(Integer32):
    """Custom type acpSysModType based on Integer32"""
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
        *(("iop", 5),
          ("iopHyb", 4),
          ("iopLan", 2),
          ("iopWan", 3),
          ("me", 6),
          ("nam", 7),
          ("none", 1))
    )


_AcpSysModType_Type.__name__ = "Integer32"
_AcpSysModType_Object = MibTableColumn
acpSysModType = _AcpSysModType_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 1, 3, 1, 1),
    _AcpSysModType_Type()
)
acpSysModType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpSysModType.setStatus("mandatory")


class _AcpSysModStatus_Type(Integer32):
    """Custom type acpSysModStatus based on Integer32"""
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
        *(("config", 7),
          ("diag", 3),
          ("disabled", 9),
          ("failed", 4),
          ("loaded", 6),
          ("loading", 5),
          ("noHardware", 2),
          ("onLine", 8),
          ("reset", 1))
    )


_AcpSysModStatus_Type.__name__ = "Integer32"
_AcpSysModStatus_Object = MibTableColumn
acpSysModStatus = _AcpSysModStatus_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 1, 3, 1, 2),
    _AcpSysModStatus_Type()
)
acpSysModStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpSysModStatus.setStatus("mandatory")
_AcpSysModSwVersion_Type = OctetString
_AcpSysModSwVersion_Object = MibTableColumn
acpSysModSwVersion = _AcpSysModSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 1, 3, 1, 3),
    _AcpSysModSwVersion_Type()
)
acpSysModSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpSysModSwVersion.setStatus("mandatory")
_AcpSysModSwDate_Type = OctetString
_AcpSysModSwDate_Object = MibTableColumn
acpSysModSwDate = _AcpSysModSwDate_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 1, 3, 1, 4),
    _AcpSysModSwDate_Type()
)
acpSysModSwDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpSysModSwDate.setStatus("mandatory")
_AcpSysModSwComment_Type = OctetString
_AcpSysModSwComment_Object = MibTableColumn
acpSysModSwComment = _AcpSysModSwComment_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 1, 3, 1, 5),
    _AcpSysModSwComment_Type()
)
acpSysModSwComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpSysModSwComment.setStatus("mandatory")
_AcpSysModFrontIdProm_Type = OctetString
_AcpSysModFrontIdProm_Object = MibTableColumn
acpSysModFrontIdProm = _AcpSysModFrontIdProm_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 1, 3, 1, 6),
    _AcpSysModFrontIdProm_Type()
)
acpSysModFrontIdProm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpSysModFrontIdProm.setStatus("mandatory")
_AcpSysModRearIdProm_Type = OctetString
_AcpSysModRearIdProm_Object = MibTableColumn
acpSysModRearIdProm = _AcpSysModRearIdProm_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 1, 3, 1, 7),
    _AcpSysModRearIdProm_Type()
)
acpSysModRearIdProm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpSysModRearIdProm.setStatus("mandatory")
_AcpComPort_ObjectIdentity = ObjectIdentity
acpComPort = _AcpComPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 124, 2, 2)
)
_AcpComPortTable_Object = MibTable
acpComPortTable = _AcpComPortTable_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 2, 1)
)
if mibBuilder.loadTexts:
    acpComPortTable.setStatus("mandatory")
_AcpComPortEntry_Object = MibTableRow
acpComPortEntry = _AcpComPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 2, 1, 1)
)
acpComPortEntry.setIndexNames(
    (0, "RACAL-MILGO-ACP-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    acpComPortEntry.setStatus("mandatory")
_AcpComPortQtimer_Type = Integer32
_AcpComPortQtimer_Object = MibScalar
acpComPortQtimer = _AcpComPortQtimer_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 2, 1, 1, 1),
    _AcpComPortQtimer_Type()
)
acpComPortQtimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpComPortQtimer.setStatus("mandatory")
_AcpComPortCongTimer_Type = Integer32
_AcpComPortCongTimer_Object = MibScalar
acpComPortCongTimer = _AcpComPortCongTimer_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 2, 1, 1, 2),
    _AcpComPortCongTimer_Type()
)
acpComPortCongTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpComPortCongTimer.setStatus("mandatory")
_AcpComPortErrMax_Type = Integer32
_AcpComPortErrMax_Object = MibScalar
acpComPortErrMax = _AcpComPortErrMax_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 2, 1, 1, 3),
    _AcpComPortErrMax_Type()
)
acpComPortErrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpComPortErrMax.setStatus("mandatory")
_AcpComPortRxPktsAcp_Type = Counter32
_AcpComPortRxPktsAcp_Object = MibTableColumn
acpComPortRxPktsAcp = _AcpComPortRxPktsAcp_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 2, 1, 1, 4),
    _AcpComPortRxPktsAcp_Type()
)
acpComPortRxPktsAcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpComPortRxPktsAcp.setStatus("mandatory")
_AcpComPortRxPktsKnown_Type = Counter32
_AcpComPortRxPktsKnown_Object = MibTableColumn
acpComPortRxPktsKnown = _AcpComPortRxPktsKnown_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 2, 1, 1, 5),
    _AcpComPortRxPktsKnown_Type()
)
acpComPortRxPktsKnown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpComPortRxPktsKnown.setStatus("mandatory")
_AcpComPortRxPktsUnk_Type = Counter32
_AcpComPortRxPktsUnk_Object = MibTableColumn
acpComPortRxPktsUnk = _AcpComPortRxPktsUnk_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 2, 1, 1, 6),
    _AcpComPortRxPktsUnk_Type()
)
acpComPortRxPktsUnk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpComPortRxPktsUnk.setStatus("mandatory")
_AcpComPortRxOutcomeFilIop_Type = Counter32
_AcpComPortRxOutcomeFilIop_Object = MibTableColumn
acpComPortRxOutcomeFilIop = _AcpComPortRxOutcomeFilIop_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 2, 1, 1, 7),
    _AcpComPortRxOutcomeFilIop_Type()
)
acpComPortRxOutcomeFilIop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpComPortRxOutcomeFilIop.setStatus("mandatory")
_AcpComPortTxPktsAcp_Type = Counter32
_AcpComPortTxPktsAcp_Object = MibTableColumn
acpComPortTxPktsAcp = _AcpComPortTxPktsAcp_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 2, 1, 1, 8),
    _AcpComPortTxPktsAcp_Type()
)
acpComPortTxPktsAcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpComPortTxPktsAcp.setStatus("mandatory")
_AcpComPortTxPktsKnown_Type = Counter32
_AcpComPortTxPktsKnown_Object = MibTableColumn
acpComPortTxPktsKnown = _AcpComPortTxPktsKnown_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 2, 1, 1, 9),
    _AcpComPortTxPktsKnown_Type()
)
acpComPortTxPktsKnown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpComPortTxPktsKnown.setStatus("mandatory")
_AcpComPortTxPktsUnk_Type = Counter32
_AcpComPortTxPktsUnk_Object = MibTableColumn
acpComPortTxPktsUnk = _AcpComPortTxPktsUnk_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 2, 1, 1, 10),
    _AcpComPortTxPktsUnk_Type()
)
acpComPortTxPktsUnk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpComPortTxPktsUnk.setStatus("mandatory")
_AcpComPortRxOutcomeFwd_Type = Counter32
_AcpComPortRxOutcomeFwd_Object = MibTableColumn
acpComPortRxOutcomeFwd = _AcpComPortRxOutcomeFwd_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 2, 1, 1, 11),
    _AcpComPortRxOutcomeFwd_Type()
)
acpComPortRxOutcomeFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpComPortRxOutcomeFwd.setStatus("mandatory")
_AcpComPortRxOutcomeFilLcl_Type = Counter32
_AcpComPortRxOutcomeFilLcl_Object = MibTableColumn
acpComPortRxOutcomeFilLcl = _AcpComPortRxOutcomeFilLcl_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 2, 1, 1, 12),
    _AcpComPortRxOutcomeFilLcl_Type()
)
acpComPortRxOutcomeFilLcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpComPortRxOutcomeFilLcl.setStatus("mandatory")
_AcpComPortRxOutcomeFilNf_Type = Counter32
_AcpComPortRxOutcomeFilNf_Object = MibTableColumn
acpComPortRxOutcomeFilNf = _AcpComPortRxOutcomeFilNf_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 2, 1, 1, 13),
    _AcpComPortRxOutcomeFilNf_Type()
)
acpComPortRxOutcomeFilNf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpComPortRxOutcomeFilNf.setStatus("mandatory")
_AcpComPortRxOutcomeFilSrc_Type = Counter32
_AcpComPortRxOutcomeFilSrc_Object = MibTableColumn
acpComPortRxOutcomeFilSrc = _AcpComPortRxOutcomeFilSrc_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 2, 1, 1, 14),
    _AcpComPortRxOutcomeFilSrc_Type()
)
acpComPortRxOutcomeFilSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpComPortRxOutcomeFilSrc.setStatus("mandatory")
_AcpComPortRxOutcomeFilDest_Type = Counter32
_AcpComPortRxOutcomeFilDest_Object = MibTableColumn
acpComPortRxOutcomeFilDest = _AcpComPortRxOutcomeFilDest_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 2, 1, 1, 15),
    _AcpComPortRxOutcomeFilDest_Type()
)
acpComPortRxOutcomeFilDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpComPortRxOutcomeFilDest.setStatus("mandatory")
_AcpComPortRxFilterChars_Type = Counter32
_AcpComPortRxFilterChars_Object = MibTableColumn
acpComPortRxFilterChars = _AcpComPortRxFilterChars_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 2, 1, 1, 16),
    _AcpComPortRxFilterChars_Type()
)
acpComPortRxFilterChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpComPortRxFilterChars.setStatus("mandatory")
_AcpComPortRxSizeErr_Type = Counter32
_AcpComPortRxSizeErr_Object = MibTableColumn
acpComPortRxSizeErr = _AcpComPortRxSizeErr_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 2, 1, 1, 17),
    _AcpComPortRxSizeErr_Type()
)
acpComPortRxSizeErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpComPortRxSizeErr.setStatus("mandatory")
_AcpComPortRxCrcErr_Type = Counter32
_AcpComPortRxCrcErr_Object = MibTableColumn
acpComPortRxCrcErr = _AcpComPortRxCrcErr_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 2, 1, 1, 18),
    _AcpComPortRxCrcErr_Type()
)
acpComPortRxCrcErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpComPortRxCrcErr.setStatus("mandatory")
_AcpComPortRxFrmErr_Type = Counter32
_AcpComPortRxFrmErr_Object = MibTableColumn
acpComPortRxFrmErr = _AcpComPortRxFrmErr_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 2, 1, 1, 19),
    _AcpComPortRxFrmErr_Type()
)
acpComPortRxFrmErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpComPortRxFrmErr.setStatus("mandatory")
_AcpComPortNzRxUtil_Type = Counter32
_AcpComPortNzRxUtil_Object = MibTableColumn
acpComPortNzRxUtil = _AcpComPortNzRxUtil_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 2, 1, 1, 20),
    _AcpComPortNzRxUtil_Type()
)
acpComPortNzRxUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpComPortNzRxUtil.setStatus("mandatory")
_AcpComPortNzTxUtil_Type = Counter32
_AcpComPortNzTxUtil_Object = MibTableColumn
acpComPortNzTxUtil = _AcpComPortNzTxUtil_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 2, 1, 1, 21),
    _AcpComPortNzTxUtil_Type()
)
acpComPortNzTxUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpComPortNzTxUtil.setStatus("mandatory")
_AcpEnetPort_ObjectIdentity = ObjectIdentity
acpEnetPort = _AcpEnetPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 124, 2, 3)
)
_AcpEnetPortTable_Object = MibTable
acpEnetPortTable = _AcpEnetPortTable_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 3, 1)
)
if mibBuilder.loadTexts:
    acpEnetPortTable.setStatus("mandatory")
_AcpEnetPortEntry_Object = MibTableRow
acpEnetPortEntry = _AcpEnetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 3, 1, 1)
)
acpEnetPortEntry.setIndexNames(
    (0, "RACAL-MILGO-ACP-MIB", "acpEnetPortIgnoreHeartbeat"),
)
if mibBuilder.loadTexts:
    acpEnetPortEntry.setStatus("mandatory")


class _AcpEnetPortIgnoreHeartbeat_Type(Integer32):
    """Custom type acpEnetPortIgnoreHeartbeat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AcpEnetPortIgnoreHeartbeat_Type.__name__ = "Integer32"
_AcpEnetPortIgnoreHeartbeat_Object = MibTableColumn
acpEnetPortIgnoreHeartbeat = _AcpEnetPortIgnoreHeartbeat_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 3, 1, 1, 1),
    _AcpEnetPortIgnoreHeartbeat_Type()
)
acpEnetPortIgnoreHeartbeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpEnetPortIgnoreHeartbeat.setStatus("mandatory")
_AcpEnetPortRxFewDescr_Type = Counter32
_AcpEnetPortRxFewDescr_Object = MibTableColumn
acpEnetPortRxFewDescr = _AcpEnetPortRxFewDescr_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 3, 1, 1, 2),
    _AcpEnetPortRxFewDescr_Type()
)
acpEnetPortRxFewDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpEnetPortRxFewDescr.setStatus("mandatory")
_AcpEnetPortRxNoDescr_Type = Counter32
_AcpEnetPortRxNoDescr_Object = MibTableColumn
acpEnetPortRxNoDescr = _AcpEnetPortRxNoDescr_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 3, 1, 1, 3),
    _AcpEnetPortRxNoDescr_Type()
)
acpEnetPortRxNoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpEnetPortRxNoDescr.setStatus("mandatory")
_AcpEnetPortRxOflo_Type = Counter32
_AcpEnetPortRxOflo_Object = MibTableColumn
acpEnetPortRxOflo = _AcpEnetPortRxOflo_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 3, 1, 1, 4),
    _AcpEnetPortRxOflo_Type()
)
acpEnetPortRxOflo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpEnetPortRxOflo.setStatus("mandatory")
_AcpEnetPortTxDevMem_Type = Counter32
_AcpEnetPortTxDevMem_Object = MibTableColumn
acpEnetPortTxDevMem = _AcpEnetPortTxDevMem_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 3, 1, 1, 5),
    _AcpEnetPortTxDevMem_Type()
)
acpEnetPortTxDevMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpEnetPortTxDevMem.setStatus("mandatory")
_AcpEnetPortTxEnp_Type = Counter32
_AcpEnetPortTxEnp_Object = MibTableColumn
acpEnetPortTxEnp = _AcpEnetPortTxEnp_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 3, 1, 1, 6),
    _AcpEnetPortTxEnp_Type()
)
acpEnetPortTxEnp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpEnetPortTxEnp.setStatus("mandatory")
_AcpEnetPortTxDevInvRead_Type = Counter32
_AcpEnetPortTxDevInvRead_Object = MibTableColumn
acpEnetPortTxDevInvRead = _AcpEnetPortTxDevInvRead_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 3, 1, 1, 7),
    _AcpEnetPortTxDevInvRead_Type()
)
acpEnetPortTxDevInvRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpEnetPortTxDevInvRead.setStatus("mandatory")
_AcpEnetPortTx16Coll_Type = Counter32
_AcpEnetPortTx16Coll_Object = MibTableColumn
acpEnetPortTx16Coll = _AcpEnetPortTx16Coll_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 3, 1, 1, 8),
    _AcpEnetPortTx16Coll_Type()
)
acpEnetPortTx16Coll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpEnetPortTx16Coll.setStatus("mandatory")
_AcpEnetPortTxMissHeart_Type = Counter32
_AcpEnetPortTxMissHeart_Object = MibTableColumn
acpEnetPortTxMissHeart = _AcpEnetPortTxMissHeart_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 3, 1, 1, 9),
    _AcpEnetPortTxMissHeart_Type()
)
acpEnetPortTxMissHeart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpEnetPortTxMissHeart.setStatus("mandatory")
_AcpEnetPortTxDfr_Type = Counter32
_AcpEnetPortTxDfr_Object = MibTableColumn
acpEnetPortTxDfr = _AcpEnetPortTxDfr_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 3, 1, 1, 10),
    _AcpEnetPortTxDfr_Type()
)
acpEnetPortTxDfr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpEnetPortTxDfr.setStatus("mandatory")
_AcpEnetPortTxOneColl_Type = Counter32
_AcpEnetPortTxOneColl_Object = MibTableColumn
acpEnetPortTxOneColl = _AcpEnetPortTxOneColl_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 3, 1, 1, 11),
    _AcpEnetPortTxOneColl_Type()
)
acpEnetPortTxOneColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpEnetPortTxOneColl.setStatus("mandatory")
_AcpEnetPortTxMulColl_Type = Counter32
_AcpEnetPortTxMulColl_Object = MibTableColumn
acpEnetPortTxMulColl = _AcpEnetPortTxMulColl_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 3, 1, 1, 12),
    _AcpEnetPortTxMulColl_Type()
)
acpEnetPortTxMulColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpEnetPortTxMulColl.setStatus("mandatory")
_AcpEnetPortTxLate_Type = Counter32
_AcpEnetPortTxLate_Object = MibTableColumn
acpEnetPortTxLate = _AcpEnetPortTxLate_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 3, 1, 1, 13),
    _AcpEnetPortTxLate_Type()
)
acpEnetPortTxLate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpEnetPortTxLate.setStatus("mandatory")
_AcpEnetPortTxTdr_Type = Counter32
_AcpEnetPortTxTdr_Object = MibTableColumn
acpEnetPortTxTdr = _AcpEnetPortTxTdr_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 3, 1, 1, 14),
    _AcpEnetPortTxTdr_Type()
)
acpEnetPortTxTdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpEnetPortTxTdr.setStatus("mandatory")
_AcpEnetPortLanUtil_Type = Counter32
_AcpEnetPortLanUtil_Object = MibTableColumn
acpEnetPortLanUtil = _AcpEnetPortLanUtil_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 3, 1, 1, 15),
    _AcpEnetPortLanUtil_Type()
)
acpEnetPortLanUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpEnetPortLanUtil.setStatus("mandatory")
_AcpEnetPortRxBrRat_Type = Counter32
_AcpEnetPortRxBrRat_Object = MibTableColumn
acpEnetPortRxBrRat = _AcpEnetPortRxBrRat_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 3, 1, 1, 16),
    _AcpEnetPortRxBrRat_Type()
)
acpEnetPortRxBrRat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpEnetPortRxBrRat.setStatus("mandatory")
_AcpEnetPortTxBrRat_Type = Counter32
_AcpEnetPortTxBrRat_Object = MibTableColumn
acpEnetPortTxBrRat = _AcpEnetPortTxBrRat_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 3, 1, 1, 17),
    _AcpEnetPortTxBrRat_Type()
)
acpEnetPortTxBrRat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpEnetPortTxBrRat.setStatus("mandatory")
_AcpWanPort_ObjectIdentity = ObjectIdentity
acpWanPort = _AcpWanPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 124, 2, 4)
)
_AcpWanPortTable_Object = MibTable
acpWanPortTable = _AcpWanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 4, 1)
)
if mibBuilder.loadTexts:
    acpWanPortTable.setStatus("mandatory")
_AcpWanPortEntry_Object = MibTableRow
acpWanPortEntry = _AcpWanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 4, 1, 1)
)
acpWanPortEntry.setIndexNames(
    (0, "RACAL-MILGO-ACP-MIB", "acpWanPortInvert"),
)
if mibBuilder.loadTexts:
    acpWanPortEntry.setStatus("mandatory")


class _AcpWanPortInvert_Type(Integer32):
    """Custom type acpWanPortInvert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AcpWanPortInvert_Type.__name__ = "Integer32"
_AcpWanPortInvert_Object = MibTableColumn
acpWanPortInvert = _AcpWanPortInvert_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 4, 1, 1, 1),
    _AcpWanPortInvert_Type()
)
acpWanPortInvert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpWanPortInvert.setStatus("mandatory")
_AcpWanPortRxQOflo_Type = Counter32
_AcpWanPortRxQOflo_Object = MibTableColumn
acpWanPortRxQOflo = _AcpWanPortRxQOflo_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 4, 1, 1, 2),
    _AcpWanPortRxQOflo_Type()
)
acpWanPortRxQOflo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpWanPortRxQOflo.setStatus("mandatory")
_AcpWanPortRxUtil_Type = Counter32
_AcpWanPortRxUtil_Object = MibTableColumn
acpWanPortRxUtil = _AcpWanPortRxUtil_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 4, 1, 1, 3),
    _AcpWanPortRxUtil_Type()
)
acpWanPortRxUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpWanPortRxUtil.setStatus("mandatory")
_AcpWanPortTxUtil_Type = Counter32
_AcpWanPortTxUtil_Object = MibTableColumn
acpWanPortTxUtil = _AcpWanPortTxUtil_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 4, 1, 1, 4),
    _AcpWanPortTxUtil_Type()
)
acpWanPortTxUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpWanPortTxUtil.setStatus("mandatory")
_AcpWanPortClock_Type = Integer32
_AcpWanPortClock_Object = MibTableColumn
acpWanPortClock = _AcpWanPortClock_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 4, 1, 1, 5),
    _AcpWanPortClock_Type()
)
acpWanPortClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpWanPortClock.setStatus("mandatory")
_AcpMesh_ObjectIdentity = ObjectIdentity
acpMesh = _AcpMesh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 124, 2, 5)
)


class _AcpMeshProtocol_Type(Integer32):
    """Custom type acpMeshProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enhancedMesh", 2),
          ("spanningTree", 1))
    )


_AcpMeshProtocol_Type.__name__ = "Integer32"
_AcpMeshProtocol_Object = MibScalar
acpMeshProtocol = _AcpMeshProtocol_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 5, 1),
    _AcpMeshProtocol_Type()
)
acpMeshProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpMeshProtocol.setStatus("mandatory")
_AcpMeshBridgeCost_Type = Integer32
_AcpMeshBridgeCost_Object = MibScalar
acpMeshBridgeCost = _AcpMeshBridgeCost_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 5, 2),
    _AcpMeshBridgeCost_Type()
)
acpMeshBridgeCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpMeshBridgeCost.setStatus("mandatory")
_AcpMeshCostTabChanges_Type = Counter32
_AcpMeshCostTabChanges_Object = MibScalar
acpMeshCostTabChanges = _AcpMeshCostTabChanges_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 5, 3),
    _AcpMeshCostTabChanges_Type()
)
acpMeshCostTabChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpMeshCostTabChanges.setStatus("mandatory")
_AcpMeshLastCostTabChange_Type = Counter32
_AcpMeshLastCostTabChange_Object = MibScalar
acpMeshLastCostTabChange = _AcpMeshLastCostTabChange_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 5, 4),
    _AcpMeshLastCostTabChange_Type()
)
acpMeshLastCostTabChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpMeshLastCostTabChange.setStatus("mandatory")
_AcpMeshSubRootAddr_Type = OctetString
_AcpMeshSubRootAddr_Object = MibScalar
acpMeshSubRootAddr = _AcpMeshSubRootAddr_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 5, 5),
    _AcpMeshSubRootAddr_Type()
)
acpMeshSubRootAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpMeshSubRootAddr.setStatus("mandatory")
_AcpMeshCostInfoLost_Type = Counter32
_AcpMeshCostInfoLost_Object = MibScalar
acpMeshCostInfoLost = _AcpMeshCostInfoLost_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 5, 6),
    _AcpMeshCostInfoLost_Type()
)
acpMeshCostInfoLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpMeshCostInfoLost.setStatus("mandatory")
_AcpMeshNodeAddrTabSize_Type = Gauge32
_AcpMeshNodeAddrTabSize_Object = MibScalar
acpMeshNodeAddrTabSize = _AcpMeshNodeAddrTabSize_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 5, 7),
    _AcpMeshNodeAddrTabSize_Type()
)
acpMeshNodeAddrTabSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpMeshNodeAddrTabSize.setStatus("mandatory")
_AcpMeshNodeAddrTabSizePeak_Type = Counter32
_AcpMeshNodeAddrTabSizePeak_Object = MibScalar
acpMeshNodeAddrTabSizePeak = _AcpMeshNodeAddrTabSizePeak_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 5, 8),
    _AcpMeshNodeAddrTabSizePeak_Type()
)
acpMeshNodeAddrTabSizePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpMeshNodeAddrTabSizePeak.setStatus("mandatory")
_AcpMeshPortTable_Object = MibTable
acpMeshPortTable = _AcpMeshPortTable_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 5, 9)
)
if mibBuilder.loadTexts:
    acpMeshPortTable.setStatus("mandatory")
_AcpMeshPortEntry_Object = MibTableRow
acpMeshPortEntry = _AcpMeshPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 5, 9, 1)
)
acpMeshPortEntry.setIndexNames(
    (0, "RACAL-MILGO-ACP-MIB", "acpMeshPortRemoteNodeIfIdx"),
)
if mibBuilder.loadTexts:
    acpMeshPortEntry.setStatus("mandatory")


class _AcpMeshPortDisabledReason_Type(Integer32):
    """Custom type acpMeshPortDisabledReason based on Integer32"""
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
        *(("broken", 1),
          ("looped", 2),
          ("notCommunicating", 4),
          ("stopped", 3))
    )


_AcpMeshPortDisabledReason_Type.__name__ = "Integer32"
_AcpMeshPortDisabledReason_Object = MibTableColumn
acpMeshPortDisabledReason = _AcpMeshPortDisabledReason_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 5, 9, 1, 1),
    _AcpMeshPortDisabledReason_Type()
)
acpMeshPortDisabledReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpMeshPortDisabledReason.setStatus("mandatory")


class _AcpMeshPortBlockingSubstate_Type(Integer32):
    """Custom type acpMeshPortBlockingSubstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 1),
          ("forwarding", 2))
    )


_AcpMeshPortBlockingSubstate_Type.__name__ = "Integer32"
_AcpMeshPortBlockingSubstate_Object = MibTableColumn
acpMeshPortBlockingSubstate = _AcpMeshPortBlockingSubstate_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 5, 9, 1, 2),
    _AcpMeshPortBlockingSubstate_Type()
)
acpMeshPortBlockingSubstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpMeshPortBlockingSubstate.setStatus("mandatory")
_AcpMeshPortLinkCost_Type = Integer32
_AcpMeshPortLinkCost_Object = MibTableColumn
acpMeshPortLinkCost = _AcpMeshPortLinkCost_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 5, 9, 1, 3),
    _AcpMeshPortLinkCost_Type()
)
acpMeshPortLinkCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpMeshPortLinkCost.setStatus("mandatory")
_AcpMeshPortRemoteNodeAddr_Type = OctetString
_AcpMeshPortRemoteNodeAddr_Object = MibTableColumn
acpMeshPortRemoteNodeAddr = _AcpMeshPortRemoteNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 5, 9, 1, 4),
    _AcpMeshPortRemoteNodeAddr_Type()
)
acpMeshPortRemoteNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpMeshPortRemoteNodeAddr.setStatus("mandatory")
_AcpMeshPortSubnetAddr_Type = OctetString
_AcpMeshPortSubnetAddr_Object = MibTableColumn
acpMeshPortSubnetAddr = _AcpMeshPortSubnetAddr_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 5, 9, 1, 5),
    _AcpMeshPortSubnetAddr_Type()
)
acpMeshPortSubnetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpMeshPortSubnetAddr.setStatus("mandatory")
_AcpMeshPortRemoteNodeIfIdx_Type = Integer32
_AcpMeshPortRemoteNodeIfIdx_Object = MibTableColumn
acpMeshPortRemoteNodeIfIdx = _AcpMeshPortRemoteNodeIfIdx_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 5, 9, 1, 6),
    _AcpMeshPortRemoteNodeIfIdx_Type()
)
acpMeshPortRemoteNodeIfIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpMeshPortRemoteNodeIfIdx.setStatus("mandatory")
_AcpTb_ObjectIdentity = ObjectIdentity
acpTb = _AcpTb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 124, 2, 6)
)
_AcpTbAddrTabFree_Type = Gauge32
_AcpTbAddrTabFree_Object = MibScalar
acpTbAddrTabFree = _AcpTbAddrTabFree_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 6, 1),
    _AcpTbAddrTabFree_Type()
)
acpTbAddrTabFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpTbAddrTabFree.setStatus("mandatory")
_AcpTbAddrTabFreePeak_Type = Gauge32
_AcpTbAddrTabFreePeak_Object = MibScalar
acpTbAddrTabFreePeak = _AcpTbAddrTabFreePeak_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 6, 2),
    _AcpTbAddrTabFreePeak_Type()
)
acpTbAddrTabFreePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpTbAddrTabFreePeak.setStatus("mandatory")
_AcpTbDynAddrTabSize_Type = Gauge32
_AcpTbDynAddrTabSize_Object = MibScalar
acpTbDynAddrTabSize = _AcpTbDynAddrTabSize_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 6, 3),
    _AcpTbDynAddrTabSize_Type()
)
acpTbDynAddrTabSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpTbDynAddrTabSize.setStatus("mandatory")
_AcpTbDynAddrTabSizePeak_Type = Gauge32
_AcpTbDynAddrTabSizePeak_Object = MibScalar
acpTbDynAddrTabSizePeak = _AcpTbDynAddrTabSizePeak_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 6, 4),
    _AcpTbDynAddrTabSizePeak_Type()
)
acpTbDynAddrTabSizePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpTbDynAddrTabSizePeak.setStatus("mandatory")
_AcpTbStatAddrTabSize_Type = Gauge32
_AcpTbStatAddrTabSize_Object = MibScalar
acpTbStatAddrTabSize = _AcpTbStatAddrTabSize_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 6, 5),
    _AcpTbStatAddrTabSize_Type()
)
acpTbStatAddrTabSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpTbStatAddrTabSize.setStatus("mandatory")
_AcpTbStatAddrTabSizePeak_Type = Gauge32
_AcpTbStatAddrTabSizePeak_Object = MibScalar
acpTbStatAddrTabSizePeak = _AcpTbStatAddrTabSizePeak_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 6, 6),
    _AcpTbStatAddrTabSizePeak_Type()
)
acpTbStatAddrTabSizePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpTbStatAddrTabSizePeak.setStatus("mandatory")
_AcpTbPortTable_Object = MibTable
acpTbPortTable = _AcpTbPortTable_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 6, 7)
)
if mibBuilder.loadTexts:
    acpTbPortTable.setStatus("mandatory")
_AcpTbPortEntry_Object = MibTableRow
acpTbPortEntry = _AcpTbPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 6, 7, 1)
)
acpTbPortEntry.setIndexNames(
    (0, "RACAL-MILGO-ACP-MIB", "acpTbPortStn"),
)
if mibBuilder.loadTexts:
    acpTbPortEntry.setStatus("mandatory")
_AcpTbPortStn_Type = Integer32
_AcpTbPortStn_Object = MibTableColumn
acpTbPortStn = _AcpTbPortStn_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 6, 7, 1, 1),
    _AcpTbPortStn_Type()
)
acpTbPortStn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpTbPortStn.setStatus("mandatory")
_AcpTbPortTimeForwarding_Type = Integer32
_AcpTbPortTimeForwarding_Object = MibTableColumn
acpTbPortTimeForwarding = _AcpTbPortTimeForwarding_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 6, 7, 1, 2),
    _AcpTbPortTimeForwarding_Type()
)
acpTbPortTimeForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpTbPortTimeForwarding.setStatus("mandatory")
_AcpTbPortTimeNotForwarding_Type = Integer32
_AcpTbPortTimeNotForwarding_Object = MibTableColumn
acpTbPortTimeNotForwarding = _AcpTbPortTimeNotForwarding_Object(
    (1, 3, 6, 1, 4, 1, 124, 2, 6, 7, 1, 3),
    _AcpTbPortTimeNotForwarding_Type()
)
acpTbPortTimeNotForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpTbPortTimeNotForwarding.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RACAL-MILGO-ACP-MIB",
    **{"internet": internet,
       "experimental": experimental,
       "private": private,
       "enterprises": enterprises,
       "mib-racal-milgo": mib_racal_milgo,
       "rmAcp": rmAcp,
       "acpSys": acpSys,
       "acpSysNodeId": acpSysNodeId,
       "acpSysAlarm": acpSysAlarm,
       "acpSysModTable": acpSysModTable,
       "acpSysModEntry": acpSysModEntry,
       "acpSysModType": acpSysModType,
       "acpSysModStatus": acpSysModStatus,
       "acpSysModSwVersion": acpSysModSwVersion,
       "acpSysModSwDate": acpSysModSwDate,
       "acpSysModSwComment": acpSysModSwComment,
       "acpSysModFrontIdProm": acpSysModFrontIdProm,
       "acpSysModRearIdProm": acpSysModRearIdProm,
       "acpComPort": acpComPort,
       "acpComPortTable": acpComPortTable,
       "acpComPortEntry": acpComPortEntry,
       "acpComPortQtimer": acpComPortQtimer,
       "acpComPortCongTimer": acpComPortCongTimer,
       "acpComPortErrMax": acpComPortErrMax,
       "acpComPortRxPktsAcp": acpComPortRxPktsAcp,
       "acpComPortRxPktsKnown": acpComPortRxPktsKnown,
       "acpComPortRxPktsUnk": acpComPortRxPktsUnk,
       "acpComPortRxOutcomeFilIop": acpComPortRxOutcomeFilIop,
       "acpComPortTxPktsAcp": acpComPortTxPktsAcp,
       "acpComPortTxPktsKnown": acpComPortTxPktsKnown,
       "acpComPortTxPktsUnk": acpComPortTxPktsUnk,
       "acpComPortRxOutcomeFwd": acpComPortRxOutcomeFwd,
       "acpComPortRxOutcomeFilLcl": acpComPortRxOutcomeFilLcl,
       "acpComPortRxOutcomeFilNf": acpComPortRxOutcomeFilNf,
       "acpComPortRxOutcomeFilSrc": acpComPortRxOutcomeFilSrc,
       "acpComPortRxOutcomeFilDest": acpComPortRxOutcomeFilDest,
       "acpComPortRxFilterChars": acpComPortRxFilterChars,
       "acpComPortRxSizeErr": acpComPortRxSizeErr,
       "acpComPortRxCrcErr": acpComPortRxCrcErr,
       "acpComPortRxFrmErr": acpComPortRxFrmErr,
       "acpComPortNzRxUtil": acpComPortNzRxUtil,
       "acpComPortNzTxUtil": acpComPortNzTxUtil,
       "acpEnetPort": acpEnetPort,
       "acpEnetPortTable": acpEnetPortTable,
       "acpEnetPortEntry": acpEnetPortEntry,
       "acpEnetPortIgnoreHeartbeat": acpEnetPortIgnoreHeartbeat,
       "acpEnetPortRxFewDescr": acpEnetPortRxFewDescr,
       "acpEnetPortRxNoDescr": acpEnetPortRxNoDescr,
       "acpEnetPortRxOflo": acpEnetPortRxOflo,
       "acpEnetPortTxDevMem": acpEnetPortTxDevMem,
       "acpEnetPortTxEnp": acpEnetPortTxEnp,
       "acpEnetPortTxDevInvRead": acpEnetPortTxDevInvRead,
       "acpEnetPortTx16Coll": acpEnetPortTx16Coll,
       "acpEnetPortTxMissHeart": acpEnetPortTxMissHeart,
       "acpEnetPortTxDfr": acpEnetPortTxDfr,
       "acpEnetPortTxOneColl": acpEnetPortTxOneColl,
       "acpEnetPortTxMulColl": acpEnetPortTxMulColl,
       "acpEnetPortTxLate": acpEnetPortTxLate,
       "acpEnetPortTxTdr": acpEnetPortTxTdr,
       "acpEnetPortLanUtil": acpEnetPortLanUtil,
       "acpEnetPortRxBrRat": acpEnetPortRxBrRat,
       "acpEnetPortTxBrRat": acpEnetPortTxBrRat,
       "acpWanPort": acpWanPort,
       "acpWanPortTable": acpWanPortTable,
       "acpWanPortEntry": acpWanPortEntry,
       "acpWanPortInvert": acpWanPortInvert,
       "acpWanPortRxQOflo": acpWanPortRxQOflo,
       "acpWanPortRxUtil": acpWanPortRxUtil,
       "acpWanPortTxUtil": acpWanPortTxUtil,
       "acpWanPortClock": acpWanPortClock,
       "acpMesh": acpMesh,
       "acpMeshProtocol": acpMeshProtocol,
       "acpMeshBridgeCost": acpMeshBridgeCost,
       "acpMeshCostTabChanges": acpMeshCostTabChanges,
       "acpMeshLastCostTabChange": acpMeshLastCostTabChange,
       "acpMeshSubRootAddr": acpMeshSubRootAddr,
       "acpMeshCostInfoLost": acpMeshCostInfoLost,
       "acpMeshNodeAddrTabSize": acpMeshNodeAddrTabSize,
       "acpMeshNodeAddrTabSizePeak": acpMeshNodeAddrTabSizePeak,
       "acpMeshPortTable": acpMeshPortTable,
       "acpMeshPortEntry": acpMeshPortEntry,
       "acpMeshPortDisabledReason": acpMeshPortDisabledReason,
       "acpMeshPortBlockingSubstate": acpMeshPortBlockingSubstate,
       "acpMeshPortLinkCost": acpMeshPortLinkCost,
       "acpMeshPortRemoteNodeAddr": acpMeshPortRemoteNodeAddr,
       "acpMeshPortSubnetAddr": acpMeshPortSubnetAddr,
       "acpMeshPortRemoteNodeIfIdx": acpMeshPortRemoteNodeIfIdx,
       "acpTb": acpTb,
       "acpTbAddrTabFree": acpTbAddrTabFree,
       "acpTbAddrTabFreePeak": acpTbAddrTabFreePeak,
       "acpTbDynAddrTabSize": acpTbDynAddrTabSize,
       "acpTbDynAddrTabSizePeak": acpTbDynAddrTabSizePeak,
       "acpTbStatAddrTabSize": acpTbStatAddrTabSize,
       "acpTbStatAddrTabSizePeak": acpTbStatAddrTabSizePeak,
       "acpTbPortTable": acpTbPortTable,
       "acpTbPortEntry": acpTbPortEntry,
       "acpTbPortStn": acpTbPortStn,
       "acpTbPortTimeForwarding": acpTbPortTimeForwarding,
       "acpTbPortTimeNotForwarding": acpTbPortTimeNotForwarding}
)
