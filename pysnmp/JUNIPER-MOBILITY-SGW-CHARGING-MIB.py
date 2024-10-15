# SNMP MIB module (JUNIPER-MOBILITY-SGW-CHARGING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-MOBILITY-SGW-CHARGING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:55 2024
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

(jnxMobileGatewaySgw,) = mibBuilder.importSymbols(
    "JUNIPER-MBG-SMI",
    "jnxMobileGatewaySgw")

(jnxMbgGwIndex,
 jnxMbgGwName) = mibBuilder.importSymbols(
    "JUNIPER-MOBILE-GATEWAYS",
    "jnxMbgGwIndex",
    "jnxMbgGwName")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

jnxMbgSgwChargingMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3)
)
jnxMbgSgwChargingMib.setRevisions(
        ("2011-10-10 14:30",
         "2012-03-16 14:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxMbgSgwCgNotifications_ObjectIdentity = ObjectIdentity
jnxMbgSgwCgNotifications = _JnxMbgSgwCgNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 0)
)
_JnxMbgSgwChargingObjects_ObjectIdentity = ObjectIdentity
jnxMbgSgwChargingObjects = _JnxMbgSgwChargingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1)
)
_JnxMbgSgwCgLpsStatsTable_Object = MibTable
jnxMbgSgwCgLpsStatsTable = _JnxMbgSgwCgLpsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    jnxMbgSgwCgLpsStatsTable.setStatus("current")
_JnxMbgSgwCgLpsStatsEntry_Object = MibTableRow
jnxMbgSgwCgLpsStatsEntry = _JnxMbgSgwCgLpsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 1, 1)
)
jnxMbgSgwCgLpsStatsEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
)
if mibBuilder.loadTexts:
    jnxMbgSgwCgLpsStatsEntry.setStatus("current")
_JnxMbgSgwCgFilesOnLcStorage_Type = Gauge32
_JnxMbgSgwCgFilesOnLcStorage_Object = MibTableColumn
jnxMbgSgwCgFilesOnLcStorage = _JnxMbgSgwCgFilesOnLcStorage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 1, 1, 1),
    _JnxMbgSgwCgFilesOnLcStorage_Type()
)
jnxMbgSgwCgFilesOnLcStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgFilesOnLcStorage.setStatus("current")
_JnxMbgSgwCgLcStorageAvailSpace_Type = Gauge32
_JnxMbgSgwCgLcStorageAvailSpace_Object = MibTableColumn
jnxMbgSgwCgLcStorageAvailSpace = _JnxMbgSgwCgLcStorageAvailSpace_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 1, 1, 2),
    _JnxMbgSgwCgLcStorageAvailSpace_Type()
)
jnxMbgSgwCgLcStorageAvailSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgLcStorageAvailSpace.setStatus("current")
if mibBuilder.loadTexts:
    jnxMbgSgwCgLcStorageAvailSpace.setUnits("MBytes")
_JnxMbgSgwCgCgfGroupsStatsTable_Object = MibTable
jnxMbgSgwCgCgfGroupsStatsTable = _JnxMbgSgwCgCgfGroupsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfGroupsStatsTable.setStatus("current")
_JnxMbgSgwCgCgfGroupStatsEntry_Object = MibTableRow
jnxMbgSgwCgCgfGroupStatsEntry = _JnxMbgSgwCgCgfGroupStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 2, 1)
)
jnxMbgSgwCgCgfGroupStatsEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
    (0, "JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgCgfGrpProfId"),
)
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfGroupStatsEntry.setStatus("current")
_JnxMbgSgwCgCgfGrpProfId_Type = Unsigned32
_JnxMbgSgwCgCgfGrpProfId_Object = MibTableColumn
jnxMbgSgwCgCgfGrpProfId = _JnxMbgSgwCgCgfGrpProfId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 2, 1, 1),
    _JnxMbgSgwCgCgfGrpProfId_Type()
)
jnxMbgSgwCgCgfGrpProfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfGrpProfId.setStatus("current")
_JnxMbgSgwCgCgfGrpDRTReqTx_Type = Counter32
_JnxMbgSgwCgCgfGrpDRTReqTx_Object = MibTableColumn
jnxMbgSgwCgCgfGrpDRTReqTx = _JnxMbgSgwCgCgfGrpDRTReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 2, 1, 2),
    _JnxMbgSgwCgCgfGrpDRTReqTx_Type()
)
jnxMbgSgwCgCgfGrpDRTReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfGrpDRTReqTx.setStatus("current")
_JnxMbgSgwCgCgfGrpDRTReqRx_Type = Counter32
_JnxMbgSgwCgCgfGrpDRTReqRx_Object = MibTableColumn
jnxMbgSgwCgCgfGrpDRTReqRx = _JnxMbgSgwCgCgfGrpDRTReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 2, 1, 3),
    _JnxMbgSgwCgCgfGrpDRTReqRx_Type()
)
jnxMbgSgwCgCgfGrpDRTReqRx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfGrpDRTReqRx.setStatus("obsolete")
_JnxMbgSgwCgCgfGrpDRTReqTmout_Type = Counter32
_JnxMbgSgwCgCgfGrpDRTReqTmout_Object = MibTableColumn
jnxMbgSgwCgCgfGrpDRTReqTmout = _JnxMbgSgwCgCgfGrpDRTReqTmout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 2, 1, 4),
    _JnxMbgSgwCgCgfGrpDRTReqTmout_Type()
)
jnxMbgSgwCgCgfGrpDRTReqTmout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfGrpDRTReqTmout.setStatus("current")
_JnxMbgSgwCgCgfGrpDRTSucRspRx_Type = Counter32
_JnxMbgSgwCgCgfGrpDRTSucRspRx_Object = MibTableColumn
jnxMbgSgwCgCgfGrpDRTSucRspRx = _JnxMbgSgwCgCgfGrpDRTSucRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 2, 1, 5),
    _JnxMbgSgwCgCgfGrpDRTSucRspRx_Type()
)
jnxMbgSgwCgCgfGrpDRTSucRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfGrpDRTSucRspRx.setStatus("current")
_JnxMbgSgwCgCgfGrpDRTErrRspRx_Type = Counter32
_JnxMbgSgwCgCgfGrpDRTErrRspRx_Object = MibTableColumn
jnxMbgSgwCgCgfGrpDRTErrRspRx = _JnxMbgSgwCgCgfGrpDRTErrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 2, 1, 6),
    _JnxMbgSgwCgCgfGrpDRTErrRspRx_Type()
)
jnxMbgSgwCgCgfGrpDRTErrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfGrpDRTErrRspRx.setStatus("current")
_JnxMbgSgwCgCgfGrpRediReqRx_Type = Counter32
_JnxMbgSgwCgCgfGrpRediReqRx_Object = MibTableColumn
jnxMbgSgwCgCgfGrpRediReqRx = _JnxMbgSgwCgCgfGrpRediReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 2, 1, 7),
    _JnxMbgSgwCgCgfGrpRediReqRx_Type()
)
jnxMbgSgwCgCgfGrpRediReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfGrpRediReqRx.setStatus("current")
_JnxMbgSgwCgCgfGrpRediRspTx_Type = Counter32
_JnxMbgSgwCgCgfGrpRediRspTx_Object = MibTableColumn
jnxMbgSgwCgCgfGrpRediRspTx = _JnxMbgSgwCgCgfGrpRediRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 2, 1, 8),
    _JnxMbgSgwCgCgfGrpRediRspTx_Type()
)
jnxMbgSgwCgCgfGrpRediRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfGrpRediRspTx.setStatus("current")
_JnxMbgSgwCgCgfGrpSwitchovers_Type = Counter32
_JnxMbgSgwCgCgfGrpSwitchovers_Object = MibTableColumn
jnxMbgSgwCgCgfGrpSwitchovers = _JnxMbgSgwCgCgfGrpSwitchovers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 2, 1, 9),
    _JnxMbgSgwCgCgfGrpSwitchovers_Type()
)
jnxMbgSgwCgCgfGrpSwitchovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfGrpSwitchovers.setStatus("current")
_JnxMbgSgwCgCgfGrpBatchReqTx_Type = Counter32
_JnxMbgSgwCgCgfGrpBatchReqTx_Object = MibTableColumn
jnxMbgSgwCgCgfGrpBatchReqTx = _JnxMbgSgwCgCgfGrpBatchReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 2, 1, 10),
    _JnxMbgSgwCgCgfGrpBatchReqTx_Type()
)
jnxMbgSgwCgCgfGrpBatchReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfGrpBatchReqTx.setStatus("current")
_JnxMbgSgwCgCgfGrpBatchRspErrors_Type = Counter32
_JnxMbgSgwCgCgfGrpBatchRspErrors_Object = MibTableColumn
jnxMbgSgwCgCgfGrpBatchRspErrors = _JnxMbgSgwCgCgfGrpBatchRspErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 2, 1, 11),
    _JnxMbgSgwCgCgfGrpBatchRspErrors_Type()
)
jnxMbgSgwCgCgfGrpBatchRspErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfGrpBatchRspErrors.setStatus("current")
_JnxMbgSgwCgCgfGrpBatchCDRsTx_Type = Counter32
_JnxMbgSgwCgCgfGrpBatchCDRsTx_Object = MibTableColumn
jnxMbgSgwCgCgfGrpBatchCDRsTx = _JnxMbgSgwCgCgfGrpBatchCDRsTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 2, 1, 12),
    _JnxMbgSgwCgCgfGrpBatchCDRsTx_Type()
)
jnxMbgSgwCgCgfGrpBatchCDRsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfGrpBatchCDRsTx.setStatus("current")
_JnxMbgSgwCgCgfGroupTotalWFA_Type = Counter32
_JnxMbgSgwCgCgfGroupTotalWFA_Object = MibTableColumn
jnxMbgSgwCgCgfGroupTotalWFA = _JnxMbgSgwCgCgfGroupTotalWFA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 2, 1, 13),
    _JnxMbgSgwCgCgfGroupTotalWFA_Type()
)
jnxMbgSgwCgCgfGroupTotalWFA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfGroupTotalWFA.setStatus("current")
_JnxMbgSgwCgCgfGroupProfName_Type = DisplayString
_JnxMbgSgwCgCgfGroupProfName_Object = MibTableColumn
jnxMbgSgwCgCgfGroupProfName = _JnxMbgSgwCgCgfGroupProfName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 2, 1, 14),
    _JnxMbgSgwCgCgfGroupProfName_Type()
)
jnxMbgSgwCgCgfGroupProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfGroupProfName.setStatus("current")
_JnxMbgSgwCgNotificationVars_ObjectIdentity = ObjectIdentity
jnxMbgSgwCgNotificationVars = _JnxMbgSgwCgNotificationVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 3)
)


class _JnxMbgSgwCgServerName_Type(DisplayString):
    """Custom type jnxMbgSgwCgServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_JnxMbgSgwCgServerName_Type.__name__ = "DisplayString"
_JnxMbgSgwCgServerName_Object = MibScalar
jnxMbgSgwCgServerName = _JnxMbgSgwCgServerName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 3, 1),
    _JnxMbgSgwCgServerName_Type()
)
jnxMbgSgwCgServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSgwCgServerName.setStatus("current")


class _JnxMbgSgwCgServicePicName_Type(DisplayString):
    """Custom type jnxMbgSgwCgServicePicName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_JnxMbgSgwCgServicePicName_Type.__name__ = "DisplayString"
_JnxMbgSgwCgServicePicName_Object = MibScalar
jnxMbgSgwCgServicePicName = _JnxMbgSgwCgServicePicName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 3, 2),
    _JnxMbgSgwCgServicePicName_Type()
)
jnxMbgSgwCgServicePicName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSgwCgServicePicName.setStatus("current")


class _JnxMbgSgwCgCDRDest_Type(Integer32):
    """Custom type jnxMbgSgwCgCDRDest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cdrbackup", 2),
          ("cdrcgf", 1),
          ("cdrnobackup", 3))
    )


_JnxMbgSgwCgCDRDest_Type.__name__ = "Integer32"
_JnxMbgSgwCgCDRDest_Object = MibScalar
jnxMbgSgwCgCDRDest = _JnxMbgSgwCgCDRDest_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 3, 3),
    _JnxMbgSgwCgCDRDest_Type()
)
jnxMbgSgwCgCDRDest.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCDRDest.setStatus("current")


class _JnxMbgSgwCgTSPName_Type(DisplayString):
    """Custom type jnxMbgSgwCgTSPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_JnxMbgSgwCgTSPName_Type.__name__ = "DisplayString"
_JnxMbgSgwCgTSPName_Object = MibScalar
jnxMbgSgwCgTSPName = _JnxMbgSgwCgTSPName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 3, 4),
    _JnxMbgSgwCgTSPName_Type()
)
jnxMbgSgwCgTSPName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSgwCgTSPName.setStatus("current")


class _JnxMbgSgwCgMemLimit_Type(Integer32):
    """Custom type jnxMbgSgwCgMemLimit based on Integer32"""
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
        *(("memfulldisconnectexistnew", 3),
          ("memfulldisconnectexistnewrslvd", 4),
          ("memfulldisconnectnew", 1),
          ("memfulldisconnectnewrslvd", 2))
    )


_JnxMbgSgwCgMemLimit_Type.__name__ = "Integer32"
_JnxMbgSgwCgMemLimit_Object = MibScalar
jnxMbgSgwCgMemLimit = _JnxMbgSgwCgMemLimit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 3, 5),
    _JnxMbgSgwCgMemLimit_Type()
)
jnxMbgSgwCgMemLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSgwCgMemLimit.setStatus("current")


class _JnxMbgSgwCgLcsSpace_Type(Integer32):
    """Custom type jnxMbgSgwCgLcsSpace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localstoragememlevel1", 1),
          ("localstoragememlevel2", 2),
          ("localstoragememlevel3", 3))
    )


_JnxMbgSgwCgLcsSpace_Type.__name__ = "Integer32"
_JnxMbgSgwCgLcsSpace_Object = MibScalar
jnxMbgSgwCgLcsSpace = _JnxMbgSgwCgLcsSpace_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 3, 6),
    _JnxMbgSgwCgLcsSpace_Type()
)
jnxMbgSgwCgLcsSpace.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSgwCgLcsSpace.setStatus("current")
_JnxMbgSgwCgLcsUtil_Type = Gauge32
_JnxMbgSgwCgLcsUtil_Object = MibScalar
jnxMbgSgwCgLcsUtil = _JnxMbgSgwCgLcsUtil_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 3, 7),
    _JnxMbgSgwCgLcsUtil_Type()
)
jnxMbgSgwCgLcsUtil.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSgwCgLcsUtil.setStatus("current")
if mibBuilder.loadTexts:
    jnxMbgSgwCgLcsUtil.setUnits("percent")


class _JnxMbgSgwCgAlarmStatus_Type(Integer32):
    """Custom type jnxMbgSgwCgAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 2),
          ("raised", 1))
    )


_JnxMbgSgwCgAlarmStatus_Type.__name__ = "Integer32"
_JnxMbgSgwCgAlarmStatus_Object = MibScalar
jnxMbgSgwCgAlarmStatus = _JnxMbgSgwCgAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 3, 8),
    _JnxMbgSgwCgAlarmStatus_Type()
)
jnxMbgSgwCgAlarmStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSgwCgAlarmStatus.setStatus("current")
_JnxMbgSgwCgProfileName_Type = DisplayString
_JnxMbgSgwCgProfileName_Object = MibScalar
jnxMbgSgwCgProfileName = _JnxMbgSgwCgProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 3, 9),
    _JnxMbgSgwCgProfileName_Type()
)
jnxMbgSgwCgProfileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSgwCgProfileName.setStatus("current")
_JnxMbgSgwCgPrevMMState_Type = DisplayString
_JnxMbgSgwCgPrevMMState_Object = MibScalar
jnxMbgSgwCgPrevMMState = _JnxMbgSgwCgPrevMMState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 3, 10),
    _JnxMbgSgwCgPrevMMState_Type()
)
jnxMbgSgwCgPrevMMState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSgwCgPrevMMState.setStatus("current")
_JnxMbgSgwCgNewMMState_Type = DisplayString
_JnxMbgSgwCgNewMMState_Object = MibScalar
jnxMbgSgwCgNewMMState = _JnxMbgSgwCgNewMMState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 3, 11),
    _JnxMbgSgwCgNewMMState_Type()
)
jnxMbgSgwCgNewMMState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSgwCgNewMMState.setStatus("current")
_JnxMbgSgwCgTProfileName_Type = DisplayString
_JnxMbgSgwCgTProfileName_Object = MibScalar
jnxMbgSgwCgTProfileName = _JnxMbgSgwCgTProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 3, 12),
    _JnxMbgSgwCgTProfileName_Type()
)
jnxMbgSgwCgTProfileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSgwCgTProfileName.setStatus("current")
_JnxMbgSgwCgTPrevMMState_Type = DisplayString
_JnxMbgSgwCgTPrevMMState_Object = MibScalar
jnxMbgSgwCgTPrevMMState = _JnxMbgSgwCgTPrevMMState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 3, 13),
    _JnxMbgSgwCgTPrevMMState_Type()
)
jnxMbgSgwCgTPrevMMState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSgwCgTPrevMMState.setStatus("current")
_JnxMbgSgwCgTNewMMState_Type = DisplayString
_JnxMbgSgwCgTNewMMState_Object = MibScalar
jnxMbgSgwCgTNewMMState = _JnxMbgSgwCgTNewMMState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 3, 14),
    _JnxMbgSgwCgTNewMMState_Type()
)
jnxMbgSgwCgTNewMMState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSgwCgTNewMMState.setStatus("current")
_JnxMbgSgwCgSGwName_Type = DisplayString
_JnxMbgSgwCgSGwName_Object = MibScalar
jnxMbgSgwCgSGwName = _JnxMbgSgwCgSGwName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 3, 15),
    _JnxMbgSgwCgSGwName_Type()
)
jnxMbgSgwCgSGwName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSgwCgSGwName.setStatus("current")
_JnxMbgSgwCgCgfProfName_Type = DisplayString
_JnxMbgSgwCgCgfProfName_Object = MibScalar
jnxMbgSgwCgCgfProfName = _JnxMbgSgwCgCgfProfName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 3, 16),
    _JnxMbgSgwCgCgfProfName_Type()
)
jnxMbgSgwCgCgfProfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfProfName.setStatus("current")
_JnxMbgSgwCgCgfStatsTable_Object = MibTable
jnxMbgSgwCgCgfStatsTable = _JnxMbgSgwCgCgfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4)
)
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfStatsTable.setStatus("current")
_JnxMbgSgwCgCgfStatsEntry_Object = MibTableRow
jnxMbgSgwCgCgfStatsEntry = _JnxMbgSgwCgCgfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1)
)
jnxMbgSgwCgCgfStatsEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
    (0, "JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgCgfIndex"),
)
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfStatsEntry.setStatus("current")
_JnxMbgSgwCgCgfIndex_Type = Unsigned32
_JnxMbgSgwCgCgfIndex_Object = MibTableColumn
jnxMbgSgwCgCgfIndex = _JnxMbgSgwCgCgfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1, 1),
    _JnxMbgSgwCgCgfIndex_Type()
)
jnxMbgSgwCgCgfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfIndex.setStatus("current")
_JnxMbgSgwCgCgfIpAddress_Type = IpAddress
_JnxMbgSgwCgCgfIpAddress_Object = MibTableColumn
jnxMbgSgwCgCgfIpAddress = _JnxMbgSgwCgCgfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1, 2),
    _JnxMbgSgwCgCgfIpAddress_Type()
)
jnxMbgSgwCgCgfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfIpAddress.setStatus("current")


class _JnxMbgSgwCgCgfStatus_Type(Integer32):
    """Custom type jnxMbgSgwCgCgfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_JnxMbgSgwCgCgfStatus_Type.__name__ = "Integer32"
_JnxMbgSgwCgCgfStatus_Object = MibTableColumn
jnxMbgSgwCgCgfStatus = _JnxMbgSgwCgCgfStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1, 3),
    _JnxMbgSgwCgCgfStatus_Type()
)
jnxMbgSgwCgCgfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfStatus.setStatus("current")
_JnxMbgSgwCgCgfUpDuration_Type = Counter64
_JnxMbgSgwCgCgfUpDuration_Object = MibTableColumn
jnxMbgSgwCgCgfUpDuration = _JnxMbgSgwCgCgfUpDuration_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1, 4),
    _JnxMbgSgwCgCgfUpDuration_Type()
)
jnxMbgSgwCgCgfUpDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfUpDuration.setStatus("obsolete")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfUpDuration.setUnits("minutes")
_JnxMbgSgwCgCgfDownDuration_Type = Counter64
_JnxMbgSgwCgCgfDownDuration_Object = MibTableColumn
jnxMbgSgwCgCgfDownDuration = _JnxMbgSgwCgCgfDownDuration_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1, 5),
    _JnxMbgSgwCgCgfDownDuration_Type()
)
jnxMbgSgwCgCgfDownDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfDownDuration.setStatus("obsolete")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfDownDuration.setUnits("minutes")
_JnxMbgSgwCgCgfEchoReqTx_Type = Counter64
_JnxMbgSgwCgCgfEchoReqTx_Object = MibTableColumn
jnxMbgSgwCgCgfEchoReqTx = _JnxMbgSgwCgCgfEchoReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1, 6),
    _JnxMbgSgwCgCgfEchoReqTx_Type()
)
jnxMbgSgwCgCgfEchoReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfEchoReqTx.setStatus("current")
_JnxMbgSgwCgCgfEchoReqRx_Type = Counter64
_JnxMbgSgwCgCgfEchoReqRx_Object = MibTableColumn
jnxMbgSgwCgCgfEchoReqRx = _JnxMbgSgwCgCgfEchoReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1, 7),
    _JnxMbgSgwCgCgfEchoReqRx_Type()
)
jnxMbgSgwCgCgfEchoReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfEchoReqRx.setStatus("current")
_JnxMbgSgwCgCgfEchoReqTmout_Type = Counter64
_JnxMbgSgwCgCgfEchoReqTmout_Object = MibTableColumn
jnxMbgSgwCgCgfEchoReqTmout = _JnxMbgSgwCgCgfEchoReqTmout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1, 8),
    _JnxMbgSgwCgCgfEchoReqTmout_Type()
)
jnxMbgSgwCgCgfEchoReqTmout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfEchoReqTmout.setStatus("current")
_JnxMbgSgwCgCgfEchoRespTx_Type = Counter64
_JnxMbgSgwCgCgfEchoRespTx_Object = MibTableColumn
jnxMbgSgwCgCgfEchoRespTx = _JnxMbgSgwCgCgfEchoRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1, 9),
    _JnxMbgSgwCgCgfEchoRespTx_Type()
)
jnxMbgSgwCgCgfEchoRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfEchoRespTx.setStatus("current")
_JnxMbgSgwCgCgfEchoRespRx_Type = Counter64
_JnxMbgSgwCgCgfEchoRespRx_Object = MibTableColumn
jnxMbgSgwCgCgfEchoRespRx = _JnxMbgSgwCgCgfEchoRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1, 10),
    _JnxMbgSgwCgCgfEchoRespRx_Type()
)
jnxMbgSgwCgCgfEchoRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfEchoRespRx.setStatus("current")
_JnxMbgSgwCgCgfVerUnsuppTx_Type = Counter64
_JnxMbgSgwCgCgfVerUnsuppTx_Object = MibTableColumn
jnxMbgSgwCgCgfVerUnsuppTx = _JnxMbgSgwCgCgfVerUnsuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1, 11),
    _JnxMbgSgwCgCgfVerUnsuppTx_Type()
)
jnxMbgSgwCgCgfVerUnsuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfVerUnsuppTx.setStatus("current")
_JnxMbgSgwCgCgfVerUnsuppRx_Type = Counter64
_JnxMbgSgwCgCgfVerUnsuppRx_Object = MibTableColumn
jnxMbgSgwCgCgfVerUnsuppRx = _JnxMbgSgwCgCgfVerUnsuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1, 12),
    _JnxMbgSgwCgCgfVerUnsuppRx_Type()
)
jnxMbgSgwCgCgfVerUnsuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfVerUnsuppRx.setStatus("current")
_JnxMbgSgwCgCgfNodeAliveReqTx_Type = Counter64
_JnxMbgSgwCgCgfNodeAliveReqTx_Object = MibTableColumn
jnxMbgSgwCgCgfNodeAliveReqTx = _JnxMbgSgwCgCgfNodeAliveReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1, 13),
    _JnxMbgSgwCgCgfNodeAliveReqTx_Type()
)
jnxMbgSgwCgCgfNodeAliveReqTx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfNodeAliveReqTx.setStatus("obsolete")
_JnxMbgSgwCgCgfNodeAliveReqRx_Type = Counter64
_JnxMbgSgwCgCgfNodeAliveReqRx_Object = MibTableColumn
jnxMbgSgwCgCgfNodeAliveReqRx = _JnxMbgSgwCgCgfNodeAliveReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1, 14),
    _JnxMbgSgwCgCgfNodeAliveReqRx_Type()
)
jnxMbgSgwCgCgfNodeAliveReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfNodeAliveReqRx.setStatus("current")
_JnxMbgSgwCgCgfNodeAliveReqTmout_Type = Counter64
_JnxMbgSgwCgCgfNodeAliveReqTmout_Object = MibTableColumn
jnxMbgSgwCgCgfNodeAliveReqTmout = _JnxMbgSgwCgCgfNodeAliveReqTmout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1, 15),
    _JnxMbgSgwCgCgfNodeAliveReqTmout_Type()
)
jnxMbgSgwCgCgfNodeAliveReqTmout.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfNodeAliveReqTmout.setStatus("obsolete")
_JnxMbgSgwCgCgfNodeAliveRespTx_Type = Counter64
_JnxMbgSgwCgCgfNodeAliveRespTx_Object = MibTableColumn
jnxMbgSgwCgCgfNodeAliveRespTx = _JnxMbgSgwCgCgfNodeAliveRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1, 16),
    _JnxMbgSgwCgCgfNodeAliveRespTx_Type()
)
jnxMbgSgwCgCgfNodeAliveRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfNodeAliveRespTx.setStatus("current")
_JnxMbgSgwCgCgfNodeAliveRespRx_Type = Counter64
_JnxMbgSgwCgCgfNodeAliveRespRx_Object = MibTableColumn
jnxMbgSgwCgCgfNodeAliveRespRx = _JnxMbgSgwCgCgfNodeAliveRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1, 17),
    _JnxMbgSgwCgCgfNodeAliveRespRx_Type()
)
jnxMbgSgwCgCgfNodeAliveRespRx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfNodeAliveRespRx.setStatus("obsolete")
_JnxMbgSgwCgCgfRedirectReqRx_Type = Counter64
_JnxMbgSgwCgCgfRedirectReqRx_Object = MibTableColumn
jnxMbgSgwCgCgfRedirectReqRx = _JnxMbgSgwCgCgfRedirectReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1, 18),
    _JnxMbgSgwCgCgfRedirectReqRx_Type()
)
jnxMbgSgwCgCgfRedirectReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfRedirectReqRx.setStatus("current")
_JnxMbgSgwCgCgfRedirectRespTx_Type = Counter64
_JnxMbgSgwCgCgfRedirectRespTx_Object = MibTableColumn
jnxMbgSgwCgCgfRedirectRespTx = _JnxMbgSgwCgCgfRedirectRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1, 19),
    _JnxMbgSgwCgCgfRedirectRespTx_Type()
)
jnxMbgSgwCgCgfRedirectRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfRedirectRespTx.setStatus("current")
_JnxMbgSgwCgCgfDRTReqTx_Type = Counter64
_JnxMbgSgwCgCgfDRTReqTx_Object = MibTableColumn
jnxMbgSgwCgCgfDRTReqTx = _JnxMbgSgwCgCgfDRTReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1, 20),
    _JnxMbgSgwCgCgfDRTReqTx_Type()
)
jnxMbgSgwCgCgfDRTReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfDRTReqTx.setStatus("current")
_JnxMbgSgwCgCgfDRTReqTmout_Type = Counter64
_JnxMbgSgwCgCgfDRTReqTmout_Object = MibTableColumn
jnxMbgSgwCgCgfDRTReqTmout = _JnxMbgSgwCgCgfDRTReqTmout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1, 21),
    _JnxMbgSgwCgCgfDRTReqTmout_Type()
)
jnxMbgSgwCgCgfDRTReqTmout.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfDRTReqTmout.setStatus("obsolete")
_JnxMbgSgwCgCgfDRTSuccRespRx_Type = Counter64
_JnxMbgSgwCgCgfDRTSuccRespRx_Object = MibTableColumn
jnxMbgSgwCgCgfDRTSuccRespRx = _JnxMbgSgwCgCgfDRTSuccRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1, 22),
    _JnxMbgSgwCgCgfDRTSuccRespRx_Type()
)
jnxMbgSgwCgCgfDRTSuccRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfDRTSuccRespRx.setStatus("current")
_JnxMbgSgwCgCgfDRTErrRespRx_Type = Counter64
_JnxMbgSgwCgCgfDRTErrRespRx_Object = MibTableColumn
jnxMbgSgwCgCgfDRTErrRespRx = _JnxMbgSgwCgCgfDRTErrRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1, 23),
    _JnxMbgSgwCgCgfDRTErrRespRx_Type()
)
jnxMbgSgwCgCgfDRTErrRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfDRTErrRespRx.setStatus("current")
_JnxMbgSgwCgCgfCdrTx_Type = Counter64
_JnxMbgSgwCgCgfCdrTx_Object = MibTableColumn
jnxMbgSgwCgCgfCdrTx = _JnxMbgSgwCgCgfCdrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1, 24),
    _JnxMbgSgwCgCgfCdrTx_Type()
)
jnxMbgSgwCgCgfCdrTx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfCdrTx.setStatus("obsolete")
_JnxMbgSgwCgCgfDRTRTTMean_Type = Counter64
_JnxMbgSgwCgCgfDRTRTTMean_Object = MibTableColumn
jnxMbgSgwCgCgfDRTRTTMean = _JnxMbgSgwCgCgfDRTRTTMean_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1, 25),
    _JnxMbgSgwCgCgfDRTRTTMean_Type()
)
jnxMbgSgwCgCgfDRTRTTMean.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfDRTRTTMean.setStatus("obsolete")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfDRTRTTMean.setUnits("seconds")
_JnxMbgSgwCgCgfDRTRTTMin_Type = Counter64
_JnxMbgSgwCgCgfDRTRTTMin_Object = MibTableColumn
jnxMbgSgwCgCgfDRTRTTMin = _JnxMbgSgwCgCgfDRTRTTMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1, 26),
    _JnxMbgSgwCgCgfDRTRTTMin_Type()
)
jnxMbgSgwCgCgfDRTRTTMin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfDRTRTTMin.setStatus("obsolete")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfDRTRTTMin.setUnits("seconds")
_JnxMbgSgwCgCgfDRTRTTMax_Type = Counter64
_JnxMbgSgwCgCgfDRTRTTMax_Object = MibTableColumn
jnxMbgSgwCgCgfDRTRTTMax = _JnxMbgSgwCgCgfDRTRTTMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1, 27),
    _JnxMbgSgwCgCgfDRTRTTMax_Type()
)
jnxMbgSgwCgCgfDRTRTTMax.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfDRTRTTMax.setStatus("obsolete")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfDRTRTTMax.setUnits("seconds")
_JnxMbgSgwCgCgfTransToDownState_Type = Counter64
_JnxMbgSgwCgCgfTransToDownState_Object = MibTableColumn
jnxMbgSgwCgCgfTransToDownState = _JnxMbgSgwCgCgfTransToDownState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1, 28),
    _JnxMbgSgwCgCgfTransToDownState_Type()
)
jnxMbgSgwCgCgfTransToDownState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfTransToDownState.setStatus("obsolete")
_JnxMbgSgwCgCgfContainers_Type = Counter64
_JnxMbgSgwCgCgfContainers_Object = MibTableColumn
jnxMbgSgwCgCgfContainers = _JnxMbgSgwCgCgfContainers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1, 29),
    _JnxMbgSgwCgCgfContainers_Type()
)
jnxMbgSgwCgCgfContainers.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfContainers.setStatus("obsolete")
_JnxMbgSgwCgCgfProfileName_Type = DisplayString
_JnxMbgSgwCgCgfProfileName_Object = MibTableColumn
jnxMbgSgwCgCgfProfileName = _JnxMbgSgwCgCgfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 4, 1, 30),
    _JnxMbgSgwCgCgfProfileName_Type()
)
jnxMbgSgwCgCgfProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCgfProfileName.setStatus("current")
_JnxMbgSgwCgGlobalStatsTable_Object = MibTable
jnxMbgSgwCgGlobalStatsTable = _JnxMbgSgwCgGlobalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 5)
)
if mibBuilder.loadTexts:
    jnxMbgSgwCgGlobalStatsTable.setStatus("current")
_JnxMbgSgwCgGlobalStatsEntry_Object = MibTableRow
jnxMbgSgwCgGlobalStatsEntry = _JnxMbgSgwCgGlobalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 5, 1)
)
jnxMbgSgwCgGlobalStatsEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
)
if mibBuilder.loadTexts:
    jnxMbgSgwCgGlobalStatsEntry.setStatus("current")
_JnxMbgSgwCgCdrSendErrors_Type = Counter64
_JnxMbgSgwCgCdrSendErrors_Object = MibTableColumn
jnxMbgSgwCgCdrSendErrors = _JnxMbgSgwCgCdrSendErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 5, 1, 1),
    _JnxMbgSgwCgCdrSendErrors_Type()
)
jnxMbgSgwCgCdrSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCdrSendErrors.setStatus("current")
_JnxMbgSgwCgCdrEncodeErrors_Type = Counter64
_JnxMbgSgwCgCdrEncodeErrors_Object = MibTableColumn
jnxMbgSgwCgCdrEncodeErrors = _JnxMbgSgwCgCdrEncodeErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 5, 1, 2),
    _JnxMbgSgwCgCdrEncodeErrors_Type()
)
jnxMbgSgwCgCdrEncodeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCdrEncodeErrors.setStatus("current")
_JnxMbgSgwCgCdrAllocFailures_Type = Counter64
_JnxMbgSgwCgCdrAllocFailures_Object = MibTableColumn
jnxMbgSgwCgCdrAllocFailures = _JnxMbgSgwCgCdrAllocFailures_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 5, 1, 3),
    _JnxMbgSgwCgCdrAllocFailures_Type()
)
jnxMbgSgwCgCdrAllocFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCdrAllocFailures.setStatus("current")
_JnxMbgSgwCgContFailures_Type = Counter64
_JnxMbgSgwCgContFailures_Object = MibTableColumn
jnxMbgSgwCgContFailures = _JnxMbgSgwCgContFailures_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 5, 1, 4),
    _JnxMbgSgwCgContFailures_Type()
)
jnxMbgSgwCgContFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgContFailures.setStatus("current")
_JnxMbgSgwCgCmBearersCreated_Type = Counter64
_JnxMbgSgwCgCmBearersCreated_Object = MibTableColumn
jnxMbgSgwCgCmBearersCreated = _JnxMbgSgwCgCmBearersCreated_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 5, 1, 5),
    _JnxMbgSgwCgCmBearersCreated_Type()
)
jnxMbgSgwCgCmBearersCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCmBearersCreated.setStatus("current")
_JnxMbgSgwCgCmBearersDeleted_Type = Counter64
_JnxMbgSgwCgCmBearersDeleted_Object = MibTableColumn
jnxMbgSgwCgCmBearersDeleted = _JnxMbgSgwCgCmBearersDeleted_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 1, 5, 1, 6),
    _JnxMbgSgwCgCmBearersDeleted_Type()
)
jnxMbgSgwCgCmBearersDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCgCmBearersDeleted.setStatus("current")

# Managed Objects groups


# Notification objects

jnxMbgSgwCgGtpGWUpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 0, 1)
)
jnxMbgSgwCgGtpGWUpNotify.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgServerName"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgServicePicName"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwCgGtpGWUpNotify.setStatus(
        "current"
    )

jnxMbgSgwCgGtpGWDownNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 0, 2)
)
jnxMbgSgwCgGtpGWDownNotify.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgServerName"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgServicePicName"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwCgGtpGWDownNotify.setStatus(
        "current"
    )

jnxMbgSgwCgCDRDestNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 0, 3)
)
jnxMbgSgwCgCDRDestNotify.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgCDRDest"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgTSPName"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgCgfIpAddress"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwCgCDRDestNotify.setStatus(
        "current"
    )

jnxMbgSgwCgServiceUpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 0, 4)
)
jnxMbgSgwCgServiceUpNotify.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgServicePicName"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwCgServiceUpNotify.setStatus(
        "current"
    )

jnxMbgSgwCgMMStateChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 0, 5)
)
jnxMbgSgwCgMMStateChangeNotify.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgProfileName"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgPrevMMState"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgNewMMState"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwCgMMStateChangeNotify.setStatus(
        "current"
    )

jnxMbgSgwCgTMMStateChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 0, 6)
)
jnxMbgSgwCgTMMStateChangeNotify.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgTProfileName"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgTPrevMMState"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgTNewMMState"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwCgTMMStateChangeNotify.setStatus(
        "current"
    )

jnxMbgSgwCgMemHighThresNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 0, 7)
)
jnxMbgSgwCgMemHighThresNotify.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgTSPName"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgServicePicName"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgMemLimit"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgAlarmStatus"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwCgMemHighThresNotify.setStatus(
        "current"
    )

jnxMbgSgwCgMemMediumThresNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 0, 8)
)
jnxMbgSgwCgMemMediumThresNotify.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgTSPName"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgServicePicName"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgMemLimit"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgAlarmStatus"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwCgMemMediumThresNotify.setStatus(
        "current"
    )

jnxMbgSgwCgMemLowThresNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 0, 9)
)
jnxMbgSgwCgMemLowThresNotify.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgTSPName"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgServicePicName"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgMemLimit"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgAlarmStatus"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwCgMemLowThresNotify.setStatus(
        "current"
    )

jnxMbgSgwCgLcsThresHighNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 0, 10)
)
jnxMbgSgwCgLcsThresHighNotify.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgAlarmStatus"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgLcsUtil"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwCgLcsThresHighNotify.setStatus(
        "current"
    )

jnxMbgSgwCgLcsThresMediumNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 0, 11)
)
jnxMbgSgwCgLcsThresMediumNotify.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgAlarmStatus"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgLcsUtil"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwCgLcsThresMediumNotify.setStatus(
        "current"
    )

jnxMbgSgwCgLcsThresLowNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 3, 0, 12)
)
jnxMbgSgwCgLcsThresLowNotify.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgAlarmStatus"),
        ("JUNIPER-MOBILITY-SGW-CHARGING-MIB", "jnxMbgSgwCgLcsUtil"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwCgLcsThresLowNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-MOBILITY-SGW-CHARGING-MIB",
    **{"jnxMbgSgwChargingMib": jnxMbgSgwChargingMib,
       "jnxMbgSgwCgNotifications": jnxMbgSgwCgNotifications,
       "jnxMbgSgwCgGtpGWUpNotify": jnxMbgSgwCgGtpGWUpNotify,
       "jnxMbgSgwCgGtpGWDownNotify": jnxMbgSgwCgGtpGWDownNotify,
       "jnxMbgSgwCgCDRDestNotify": jnxMbgSgwCgCDRDestNotify,
       "jnxMbgSgwCgServiceUpNotify": jnxMbgSgwCgServiceUpNotify,
       "jnxMbgSgwCgMMStateChangeNotify": jnxMbgSgwCgMMStateChangeNotify,
       "jnxMbgSgwCgTMMStateChangeNotify": jnxMbgSgwCgTMMStateChangeNotify,
       "jnxMbgSgwCgMemHighThresNotify": jnxMbgSgwCgMemHighThresNotify,
       "jnxMbgSgwCgMemMediumThresNotify": jnxMbgSgwCgMemMediumThresNotify,
       "jnxMbgSgwCgMemLowThresNotify": jnxMbgSgwCgMemLowThresNotify,
       "jnxMbgSgwCgLcsThresHighNotify": jnxMbgSgwCgLcsThresHighNotify,
       "jnxMbgSgwCgLcsThresMediumNotify": jnxMbgSgwCgLcsThresMediumNotify,
       "jnxMbgSgwCgLcsThresLowNotify": jnxMbgSgwCgLcsThresLowNotify,
       "jnxMbgSgwChargingObjects": jnxMbgSgwChargingObjects,
       "jnxMbgSgwCgLpsStatsTable": jnxMbgSgwCgLpsStatsTable,
       "jnxMbgSgwCgLpsStatsEntry": jnxMbgSgwCgLpsStatsEntry,
       "jnxMbgSgwCgFilesOnLcStorage": jnxMbgSgwCgFilesOnLcStorage,
       "jnxMbgSgwCgLcStorageAvailSpace": jnxMbgSgwCgLcStorageAvailSpace,
       "jnxMbgSgwCgCgfGroupsStatsTable": jnxMbgSgwCgCgfGroupsStatsTable,
       "jnxMbgSgwCgCgfGroupStatsEntry": jnxMbgSgwCgCgfGroupStatsEntry,
       "jnxMbgSgwCgCgfGrpProfId": jnxMbgSgwCgCgfGrpProfId,
       "jnxMbgSgwCgCgfGrpDRTReqTx": jnxMbgSgwCgCgfGrpDRTReqTx,
       "jnxMbgSgwCgCgfGrpDRTReqRx": jnxMbgSgwCgCgfGrpDRTReqRx,
       "jnxMbgSgwCgCgfGrpDRTReqTmout": jnxMbgSgwCgCgfGrpDRTReqTmout,
       "jnxMbgSgwCgCgfGrpDRTSucRspRx": jnxMbgSgwCgCgfGrpDRTSucRspRx,
       "jnxMbgSgwCgCgfGrpDRTErrRspRx": jnxMbgSgwCgCgfGrpDRTErrRspRx,
       "jnxMbgSgwCgCgfGrpRediReqRx": jnxMbgSgwCgCgfGrpRediReqRx,
       "jnxMbgSgwCgCgfGrpRediRspTx": jnxMbgSgwCgCgfGrpRediRspTx,
       "jnxMbgSgwCgCgfGrpSwitchovers": jnxMbgSgwCgCgfGrpSwitchovers,
       "jnxMbgSgwCgCgfGrpBatchReqTx": jnxMbgSgwCgCgfGrpBatchReqTx,
       "jnxMbgSgwCgCgfGrpBatchRspErrors": jnxMbgSgwCgCgfGrpBatchRspErrors,
       "jnxMbgSgwCgCgfGrpBatchCDRsTx": jnxMbgSgwCgCgfGrpBatchCDRsTx,
       "jnxMbgSgwCgCgfGroupTotalWFA": jnxMbgSgwCgCgfGroupTotalWFA,
       "jnxMbgSgwCgCgfGroupProfName": jnxMbgSgwCgCgfGroupProfName,
       "jnxMbgSgwCgNotificationVars": jnxMbgSgwCgNotificationVars,
       "jnxMbgSgwCgServerName": jnxMbgSgwCgServerName,
       "jnxMbgSgwCgServicePicName": jnxMbgSgwCgServicePicName,
       "jnxMbgSgwCgCDRDest": jnxMbgSgwCgCDRDest,
       "jnxMbgSgwCgTSPName": jnxMbgSgwCgTSPName,
       "jnxMbgSgwCgMemLimit": jnxMbgSgwCgMemLimit,
       "jnxMbgSgwCgLcsSpace": jnxMbgSgwCgLcsSpace,
       "jnxMbgSgwCgLcsUtil": jnxMbgSgwCgLcsUtil,
       "jnxMbgSgwCgAlarmStatus": jnxMbgSgwCgAlarmStatus,
       "jnxMbgSgwCgProfileName": jnxMbgSgwCgProfileName,
       "jnxMbgSgwCgPrevMMState": jnxMbgSgwCgPrevMMState,
       "jnxMbgSgwCgNewMMState": jnxMbgSgwCgNewMMState,
       "jnxMbgSgwCgTProfileName": jnxMbgSgwCgTProfileName,
       "jnxMbgSgwCgTPrevMMState": jnxMbgSgwCgTPrevMMState,
       "jnxMbgSgwCgTNewMMState": jnxMbgSgwCgTNewMMState,
       "jnxMbgSgwCgSGwName": jnxMbgSgwCgSGwName,
       "jnxMbgSgwCgCgfProfName": jnxMbgSgwCgCgfProfName,
       "jnxMbgSgwCgCgfStatsTable": jnxMbgSgwCgCgfStatsTable,
       "jnxMbgSgwCgCgfStatsEntry": jnxMbgSgwCgCgfStatsEntry,
       "jnxMbgSgwCgCgfIndex": jnxMbgSgwCgCgfIndex,
       "jnxMbgSgwCgCgfIpAddress": jnxMbgSgwCgCgfIpAddress,
       "jnxMbgSgwCgCgfStatus": jnxMbgSgwCgCgfStatus,
       "jnxMbgSgwCgCgfUpDuration": jnxMbgSgwCgCgfUpDuration,
       "jnxMbgSgwCgCgfDownDuration": jnxMbgSgwCgCgfDownDuration,
       "jnxMbgSgwCgCgfEchoReqTx": jnxMbgSgwCgCgfEchoReqTx,
       "jnxMbgSgwCgCgfEchoReqRx": jnxMbgSgwCgCgfEchoReqRx,
       "jnxMbgSgwCgCgfEchoReqTmout": jnxMbgSgwCgCgfEchoReqTmout,
       "jnxMbgSgwCgCgfEchoRespTx": jnxMbgSgwCgCgfEchoRespTx,
       "jnxMbgSgwCgCgfEchoRespRx": jnxMbgSgwCgCgfEchoRespRx,
       "jnxMbgSgwCgCgfVerUnsuppTx": jnxMbgSgwCgCgfVerUnsuppTx,
       "jnxMbgSgwCgCgfVerUnsuppRx": jnxMbgSgwCgCgfVerUnsuppRx,
       "jnxMbgSgwCgCgfNodeAliveReqTx": jnxMbgSgwCgCgfNodeAliveReqTx,
       "jnxMbgSgwCgCgfNodeAliveReqRx": jnxMbgSgwCgCgfNodeAliveReqRx,
       "jnxMbgSgwCgCgfNodeAliveReqTmout": jnxMbgSgwCgCgfNodeAliveReqTmout,
       "jnxMbgSgwCgCgfNodeAliveRespTx": jnxMbgSgwCgCgfNodeAliveRespTx,
       "jnxMbgSgwCgCgfNodeAliveRespRx": jnxMbgSgwCgCgfNodeAliveRespRx,
       "jnxMbgSgwCgCgfRedirectReqRx": jnxMbgSgwCgCgfRedirectReqRx,
       "jnxMbgSgwCgCgfRedirectRespTx": jnxMbgSgwCgCgfRedirectRespTx,
       "jnxMbgSgwCgCgfDRTReqTx": jnxMbgSgwCgCgfDRTReqTx,
       "jnxMbgSgwCgCgfDRTReqTmout": jnxMbgSgwCgCgfDRTReqTmout,
       "jnxMbgSgwCgCgfDRTSuccRespRx": jnxMbgSgwCgCgfDRTSuccRespRx,
       "jnxMbgSgwCgCgfDRTErrRespRx": jnxMbgSgwCgCgfDRTErrRespRx,
       "jnxMbgSgwCgCgfCdrTx": jnxMbgSgwCgCgfCdrTx,
       "jnxMbgSgwCgCgfDRTRTTMean": jnxMbgSgwCgCgfDRTRTTMean,
       "jnxMbgSgwCgCgfDRTRTTMin": jnxMbgSgwCgCgfDRTRTTMin,
       "jnxMbgSgwCgCgfDRTRTTMax": jnxMbgSgwCgCgfDRTRTTMax,
       "jnxMbgSgwCgCgfTransToDownState": jnxMbgSgwCgCgfTransToDownState,
       "jnxMbgSgwCgCgfContainers": jnxMbgSgwCgCgfContainers,
       "jnxMbgSgwCgCgfProfileName": jnxMbgSgwCgCgfProfileName,
       "jnxMbgSgwCgGlobalStatsTable": jnxMbgSgwCgGlobalStatsTable,
       "jnxMbgSgwCgGlobalStatsEntry": jnxMbgSgwCgGlobalStatsEntry,
       "jnxMbgSgwCgCdrSendErrors": jnxMbgSgwCgCdrSendErrors,
       "jnxMbgSgwCgCdrEncodeErrors": jnxMbgSgwCgCdrEncodeErrors,
       "jnxMbgSgwCgCdrAllocFailures": jnxMbgSgwCgCdrAllocFailures,
       "jnxMbgSgwCgContFailures": jnxMbgSgwCgContFailures,
       "jnxMbgSgwCgCmBearersCreated": jnxMbgSgwCgCmBearersCreated,
       "jnxMbgSgwCgCmBearersDeleted": jnxMbgSgwCgCmBearersDeleted}
)
